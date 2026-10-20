# Research conversation: Search for the paper "HeadQ" about model-visible distortion and score-space correction for KV-cache quantization (arXiv:

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a1274b1642de5ffda.jsonl`
- **Structured JSON:** [`5cd1fd64bae7069985d2.json`](../../sessions/5c/5cd1fd64bae7069985d2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-12T00:20:25.011Z_

Search for the paper "HeadQ" about model-visible distortion and score-space correction for KV-cache quantization (arXiv:2605.03562, May 2026). I need to understand specifically:

1. What is the null-space intervention experiment in Section 5.2?
2. Does it demonstrate within-scheme failure modes (where storage-space MSE in the attention-inert subspace converts to score damage after quantization)?
3. How does the Fisher-information weighting work for PCA components?
4. Is the argument that "within the same quantization scheme, embedding-space error ranking correlates with score-space ranking" valid, or does HeadQ's evidence refute it?

Use WebSearch and WebFetch to read the actual paper content. Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d61aec02-1791-4578-9945-5769da9d7a59",
  "agentId": "a1274b1642de5ffda",
  "type": "user",
  "uuid": "90a89b43-90ab-4ac4-bdbd-86b9625cd474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:20:25.016Z_

```json
{
  "parentUuid": "90a89b43-90ab-4ac4-bdbd-86b9625cd474",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
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
  "uuid": "02a82dda-6d11-41dc-86e4-8bf2069d726b",
  "timestamp": "2026-05-12T00:20:25.016Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:20:28.328Z_



I'll search for this paper and fetch its content. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02a82dda-6d11-41dc-86e4-8bf2069d726b",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011CawiaQgCqxUvMfxAi11rX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d16a3ac9-a3d6-4cc0-bb97-c0680d35d10d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJES9jVSdqyCTf1436tfiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T00:20:28.626Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017qhfifYJy3EifUfTmiFZen`</summary>

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
  "parentUuid": "d16a3ac9-a3d6-4cc0-bb97-c0680d35d10d",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011CawiaQgCqxUvMfxAi11rX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ea55515-fe9b-480b-a881-c59365e19f26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJES9jVSdqyCTf1436tfiv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 8223,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 728
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 728,
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

_source line 5 · 2026-05-12T00:20:28.633Z_

<details><summary>↩ Tool result · `toolu_017qhfifYJy3EifUfTmiFZen`</summary>

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
  "parentUuid": "0ea55515-fe9b-480b-a881-c59365e19f26",
  "isSidechain": true,
  "promptId": "d61aec02-1791-4578-9945-5769da9d7a59",
  "agentId": "a1274b1642de5ffda",
  "type": "user",
  "uuid": "11e715c4-9dbf-43e6-9936-2a18ff12cd1d",
  "sourceToolAssistantUUID": "0ea55515-fe9b-480b-a881-c59365e19f26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:20:31.904Z_



Now let me search for the paper and try to access it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11e715c4-9dbf-43e6-9936-2a18ff12cd1d",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011Cawiah2iG6YXJsyK1hQTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66d2afd5-f9b2-4c25-9ac3-8f42174ce595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017S1YZKZb56qiX5NtxMp85x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-12T00:20:33.392Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YLrrreKX49V1DosFBFzeAk`</summary>

```json
{
  "query": "HeadQ arXiv 2605.03562 KV-cache quantization score-space correction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66d2afd5-f9b2-4c25-9ac3-8f42174ce595",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011Cawiah2iG6YXJsyK1hQTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4d9f1a2-f636-481d-aa09-fbdaf8791f93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017S1YZKZb56qiX5NtxMp85x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-12T00:20:33.780Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012XY34bZhj489siqaBNydU8`</summary>

```json
{
  "query": "HeadQ model-visible distortion score-space correction KV cache quantization paper 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4d9f1a2-f636-481d-aa09-fbdaf8791f93",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011Cawiah2iG6YXJsyK1hQTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84ba1fff-faac-4600-b64c-b005a558c9dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017S1YZKZb56qiX5NtxMp85x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8951,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 147,
          "cache_read_input_tokens": 8951,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-12T00:20:40.776Z_

<details><summary>↩ Tool result · `toolu_01YLrrreKX49V1DosFBFzeAk`</summary>

```text
Web search results for query: "HeadQ arXiv 2605.03562 KV-cache quantization score-space correction 2026"

Links: [{"title":"[2605.03562] HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization","url":"https://arxiv.org/abs/2605.03562"},{"title":"HeadQ: Model-Visible Distortion and a Prototype KV Quantizer-Corrector Codec","url":"https://arxiv.org/html/2605.03562"},{"title":"HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization","url":"https://arxiv.org/html/2605.03562v1"},{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"KVLinC: KV Cache Quantization with Hadamard Rotation and Linear Correction","url":"https://arxiv.org/html/2510.05373v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"[2510.05373v1] KVLinC : KV Cache Quantization with Hadamard Rotation and Linear Correction","url":"https://arxiv.org/abs/2510.05373v1"},{"title":"Accurate KV Cache Quantization with Outlier Tokens Tracing","url":"https://aclanthology.org/2025.acl-long.631.pdf"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"}]

I found the paper! Here's what I discovered about HeadQ (arXiv 2605.03562):

## Overview

The paper is titled "HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization" and was submitted on May 5, 2026, with a revised version (v2) on May 7, 2026. It's authored by Jorge L. Ruiz Williams.

## Key Contribution

The paper argues that KV-cache quantizers usually optimize storage-space reconstruction, even though attention reads keys through logits and values through attention-weighted readout, and proposes that persistent cache error should be measured in model-visible coordinates.

## Technical Approach

For keys, the visible object is score error modulo constant shifts; this yields HeadQ, a key-side method that stores a low-rank residual side code in a calibration-learned query basis and applies it as an additive logit correction. For values, fixed-attention readout gives an A²-weighted token-distortion surrogate.

## Results

Across six models, Fisher/score-space error predicts attention KL far better than raw key MSE; same-budget counterexamples, null-space interventions, query-PCA controls, and wrong-sign HeadQ falsify storage-MSE alternatives.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4d9f1a2-f636-481d-aa09-fbdaf8791f93",
  "isSidechain": true,
  "promptId": "d61aec02-1791-4578-9945-5769da9d7a59",
  "agentId": "a1274b1642de5ffda",
  "type": "user",
  "uuid": "5fa52b12-5d8b-420d-8cb4-782318d0ce85",
  "sourceToolAssistantUUID": "c4d9f1a2-f636-481d-aa09-fbdaf8791f93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T00:20:41.289Z_

<details><summary>↩ Tool result · `toolu_012XY34bZhj489siqaBNydU8`</summary>

```text
Web search results for query: "HeadQ model-visible distortion score-space correction KV cache quantization paper 2026"

Links: [{"title":"[2605.03562] HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization","url":"https://arxiv.org/abs/2605.03562"},{"title":"HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization","url":"https://arxiv.org/html/2605.03562v1"},{"title":"HeadQ: Model-Visible Distortion and a Prototype KV Quantizer-Corrector Codec","url":"https://arxiv.org/html/2605.03562"},{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"},{"title":"[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/abs/2605.06675"},{"title":"GitHub - RecursiveIntell/turbo-quant: Rust implementation of TurboQuant, PolarQuant, and QJL — zero-overhead vector quantization for semantic search and KV cache compression (ICLR 2026)","url":"https://github.com/RecursiveIntell/turbo-quant"},{"title":"[2605.02905] eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/abs/2605.02905"}]

I found the paper you're looking for! Here's what the search revealed:

## HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization

The paper "HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization" was published on arXiv in May 2026 by Jorge L. Ruiz Williams.

### Key Contributions

KV-cache quantizers usually optimize storage-space reconstruction, even though attention reads keys through logits and values through attention-weighted readout. The authors argue that persistent cache error should be measured in model-visible coordinates.

For keys, the visible object is score error modulo constant shifts; this yields HeadQ, a key-side method that stores a low-rank residual side code in a calibration-learned query basis and applies it as an additive logit correction.

### Evaluation Results

Across six models, Fisher/score-space error predicts attention KL far better than raw key MSE; same-budget counterexamples, null-space interventions, query-PCA controls, and wrong-sign HeadQ falsify storage-MSE alternatives.

The paper is available on arXiv at: https://arxiv.org/abs/2605.03562


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84ba1fff-faac-4600-b64c-b005a558c9dc",
  "isSidechain": true,
  "promptId": "d61aec02-1791-4578-9945-5769da9d7a59",
  "agentId": "a1274b1642de5ffda",
  "type": "user",
  "uuid": "232f0d69-f8c4-44b5-b12a-8d51062c0788",
  "sourceToolAssistantUUID": "84ba1fff-faac-4600-b64c-b005a558c9dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-12T00:20:45.658Z_

Good, I found the paper. Now let me fetch the full HTML version to get the detailed content about the specific sections you asked about.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "232f0d69-f8c4-44b5-b12a-8d51062c0788",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011CawibcGVJkzyAT8tHcxsn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f62660f4-8de1-4926-ad62-d190f99fcb60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JffuEtwEP73Ua3XtxxBmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1979,
      "cache_read_input_tokens": 10861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1979,
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

_source line 12 · 2026-05-12T00:20:50.054Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VkNyBGWatXH1zqbpEYof6R`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.03562",
  "prompt": "Extract the full content of Section 5.2 (null-space intervention experiment). I need: (1) the exact experimental setup - what is the null-space intervention, how is it constructed, what subspace is targeted; (2) the results - does MSE in the attention-inert subspace convert to score damage after quantization; (3) any tables or figures referenced. Also extract all content about Fisher-information weighting for PCA components. Also find any discussion about whether embedding-space error ranking correlates with score-space ranking within the same quantization scheme."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f62660f4-8de1-4926-ad62-d190f99fcb60",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011CawibcGVJkzyAT8tHcxsn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41d87b29-1482-44cb-9ab4-6c5655ad5bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JffuEtwEP73Ua3XtxxBmV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1979,
      "cache_read_input_tokens": 10861,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 10861,
          "cache_creation_input_tokens": 1979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1979,
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

_source line 13 · 2026-05-12T00:20:59.082Z_

<details><summary>↩ Tool result · `toolu_01VkNyBGWatXH1zqbpEYof6R`</summary>

```text
# Section 5.2 Analysis: Null-Space Intervention Experiment

## Experimental Setup

The null-space intervention, called the **α intervention**, is constructed as:

**K_α = ΔK + α·𝟏k̄ᵀ**

This formula holds the residual ΔK fixed while restoring the token-shared mean component k̄. The authors note that "exact attention is unchanged for every α, but fixed-grid and group quantizers are not translation-equivariant."

The targeted subspace is the **softmax-null direction**: perturbations that affect storage coordinates but produce no change in the attention distribution for dense computation.

## Results

The intervention demonstrates a critical failure mode: non-equivariant quantizers convert attention-inert storage energy into active score damage. As the paper states, restoring "an attention-inert common key component sharply increases Fisher damage for non-equivariant fixed-grid K quantizers."

**Figure 3** presents the quantitative results at α=1, showing that:
- Block FP4 experiences significant Fisher damage (Pythia shows the sharpest effect)
- Group absmax-4 similarly increases damage
- Per-channel affine remains "invariant" to this manipulation

Across models tested (GPT-2, Pythia, Qwen2, Qwen2.5, TinyLlama), centered and affine quantizers preserved translation equivariance.

## Fisher-Information Weighting

The paper provides Equation 6 showing the Fisher object as:

**ℐ_q,K = Σⱼ pⱼ(δsⱼ - Σᵢ pᵢδsᵢ)²**

This represents the "pp-weighted centered variance of score error." The weight pⱼ derives from softmax attention probabilities—tokens with higher attention weight contribute proportionally more to the Fisher penalty.

## Score vs. Embedding Correlation

**Table 2** directly addresses embedding-space versus score-space ranking within the same quantization scheme. The "Ctrd. TurboQuant-MSE baseline subtracts the token-axis mean and applies a rotated MSE-oriented 3-bit quantizer." Results show: lower key MSE (0.081915 for Qwen2) correlates with *worse* Fisher error (0.46641) and *worse* attention KL (0.40414) compared to the Fisher-pullback method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41d87b29-1482-44cb-9ab4-6c5655ad5bc2",
  "isSidechain": true,
  "promptId": "d61aec02-1791-4578-9945-5769da9d7a59",
  "agentId": "a1274b1642de5ffda",
  "type": "user",
  "uuid": "fb3ded4b-ff76-41f1-87dd-012edb7733d4",
  "sourceToolAssistantUUID": "41d87b29-1482-44cb-9ab4-6c5655ad5bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-12T00:21:03.043Z_

Good, but I need more detail. Let me fetch additional sections of the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb3ded4b-ff76-41f1-87dd-012edb7733d4",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011CawicvLTz9nM89MZ8z11j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f922ba5-43e0-4873-95fe-e402f59a6672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBnBy4RtZSWYcn9mMrtsY1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 12840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 816,
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

_source line 15 · 2026-05-12T00:21:06.316Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019nGKopwosGp5mnkkRoewmN`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.03562",
  "prompt": "Extract all content from Section 5 (all subsections 5.1 through 5.4 or whatever exists). I need: (1) the full null-space intervention details from 5.2 including exact numbers from Figure 3 or Table results; (2) the \"same-budget counterexamples\" from Section 5.1; (3) what \"wrong-sign HeadQ\" experiments show; (4) any query-PCA control experiments. Also extract the abstract and introduction's core argument about why storage-space MSE is wrong and score-space metrics are needed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f922ba5-43e0-4873-95fe-e402f59a6672",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011CawicvLTz9nM89MZ8z11j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2e5d1dc-2e42-4e3d-bcb6-991a7e0d791a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBnBy4RtZSWYcn9mMrtsY1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 12840,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 816
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 12840,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 816,
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

_source line 16 · 2026-05-12T00:21:20.101Z_

<details><summary>↩ Tool result · `toolu_019nGKopwosGp5mnkkRoewmN`</summary>

```text
# HeadQ: Core Arguments and Empirical Results

## Abstract & Introduction: Why Storage MSE Fails

The paper's central claim: "persistent cache error should be measured in model-visible coordinates" rather than storage reconstruction metrics. Keys affect attention only through query-key logits, and values only through attention-weighted readout—yet "the dominant optimization targets are still mostly storage-centered: mean-squared error, distortion, outlier suppression."

Storage MSE wastes resolution on components invisible to attention. A key perturbation can have "arbitrarily large storage error and exactly unchanged attention," while smaller perturbations in score-visible directions cause sharp behavioral changes.

## Section 5.1: Score-Visible Error Predicts Attention Damage

**Fisher vs. MSE Ranking:**
Fisher geometry beats raw key MSE on every model tested, with Spearman correlation gains of roughly 0.62–0.69 points. For example, on GPT-2: Fisher achieved 0.995 while MSE scored 0.329—a +0.666 gain.

**Same-Budget Counterexample:**
A centered TurboQuant-MSE baseline achieved *lower* raw key MSE than Fisher-pullback FPQ on both Qwen2-0.5B and GPT-2, yet showed *worse* Fisher error, attention KL, and output MSE. "Euclidean reconstruction improves while behavior gets worse." This directly falsifies storage-MSE as a behavioral proxy.

## Section 5.2: Centering-Sensitive Quantizer Failure

**Null-Space Intervention (α=1):**
The researchers added token-shared key components—invisible to exact attention—and measured quantizer response. Results from Figure 3 show added Fisher damage for non-equivariant quantizers:
- Pythia-160M: Block FP4 suffered ~19.6 Fisher damage; per-channel affine remained invariant (~-0.0009)
- Qwen2-0.5B: Block FP4 added ~0.64 damage; affine stayed at ~0.0000

"Restoring an attention-inert common key component sharply increases Fisher damage for non-equivariant fixed-grid K quantizers."

## Section 5.3: Calibration-Learned Query Bases

Query-PCA control experiments showed learned per-head bases recover oracle benefits without future queries. At rank-4 (default setting), query-PCA achieved Fisher/Base ratio of 0.1727 and KL/Base of 0.1920, capturing ~0.872 of query axis variance. Equal-overhead random bases failed catastrophically, with ratios >1.0, confirming the structure is learnable and specific.

## Section 5.4: Cache-Only Same-MSE Causal Checks

**Matched-MSE Controls:**
For GPT-2 across 48 test sites, decomposing cached key errors into score-active, softmax-null, and random matched-MSE perturbations showed consistent ordering: active >> null (100% of sites) and active >> random (100%). Mean active next-token KL was 2.79×10⁻³ versus ≤4.2×10⁻⁵ for matched random controls.

Pythia-160M remained positive for centered quantizers but showed boundary failure with plain block-FP4 in route-flip regimes.

## Wrong-Sign Control

Reversing the HeadQ logit correction eliminated most 3-bit Qwen2 gains and became "catastrophically bad on Pythia-160M," confirming the benefit depends on applying the correction in the correct direction and to the correct score-visible object.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2e5d1dc-2e42-4e3d-bcb6-991a7e0d791a",
  "isSidechain": true,
  "promptId": "d61aec02-1791-4578-9945-5769da9d7a59",
  "agentId": "a1274b1642de5ffda",
  "type": "user",
  "uuid": "54a9ede7-0964-4484-a490-b4d66b5bccff",
  "sourceToolAssistantUUID": "b2e5d1dc-2e42-4e3d-bcb6-991a7e0d791a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T00:21:27.914Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018EKveonx11q7FBRm6JJiG9`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.03562",
  "prompt": "Extract the details about Fisher-information weighting for PCA components. Specifically: (1) How are PCA directions of the query distribution weighted by Fisher information? (2) What is the mathematical formulation - equations for how Fisher weights are applied to principal components? (3) How does this connect to the score-space metric vs storage-space metric? (4) Is there a discussion of which PCA components matter most and why? Also extract Section 3 (theoretical framework) if it discusses the Fisher metric derivation and how it differs from Euclidean MSE in the key embedding space."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54a9ede7-0964-4484-a490-b4d66b5bccff",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011CawieVVXniN63J9tDtbWf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdd33c01-8410-4544-8948-1f11a79d298a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Db8TSvRMmxcg3Pc6k1qMHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1092,
      "cache_read_input_tokens": 13656,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1092
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 13656,
          "cache_creation_input_tokens": 1092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1092,
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

_source line 18 · 2026-05-12T00:21:35.556Z_

<details><summary>↩ Tool result · `toolu_018EKveonx11q7FBRm6JJiG9`</summary>

```text
# Fisher Information and PCA in HeadQ

## Fisher Weighting of PCA Components

The paper does **not** weight PCA directions by Fisher information directly. Instead, it uses Fisher information as a diagnostic metric to validate that query-PCA bases capture the relevant score-visible components.

## Mathematical Formulation

The Fisher information matrix for softmax perturbations is:

**"ℐq,K(δK) = δs⊤(diag(p) - pp⊤)δs"** (Equation 4)

This can be rewritten as:

**"∑j=1^n pj(δsj - ∑i=1^n piδsi)²"** (Equation 6)

The key insight is that this Fisher quadratic measures score-error variance **weighted by attention probabilities p**, not Fisher-weighted PCA components.

## Connection to Score vs. Storage Metrics

The fundamental distinction emerges from fixed-query geometry. A key perturbation δK induces score perturbation δsj = q⊤δkj/√d. Unlike Euclidean MSE (which tracks all components of δK), Fisher focuses only on the **centered active coefficients** that affect softmax outputs.

Theorem 1 decomposes any key perturbation as:
- Token-shared component δ̄ (softmax-null)
- Query-aligned component ajq̂ (score-visible)
- Orthogonal component νj (invisible to current query)

Dense attention depends only on centered active coefficients, while storage MSE pays for all three pieces.

## PCA Component Importance

The paper trains query-PCA bases on calibration data without explicit Fisher weighting. The bases are chosen simply as the **top-r principal components** of the post-RoPE query distribution. The validation comes through empirical testing: Table 3 shows that learned query-PCA bases recover 87-90% query-axis capture, while equal-overhead random bases fail completely.

The paper states: **"Query-PCA makes the useful residual deployable"** by demonstrating that low-rank projections of the key residual into this basis effectively approximate the score-visible quotient space, without requiring online Fisher optimization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdd33c01-8410-4544-8948-1f11a79d298a",
  "isSidechain": true,
  "promptId": "d61aec02-1791-4578-9945-5769da9d7a59",
  "agentId": "a1274b1642de5ffda",
  "type": "user",
  "uuid": "aade07ad-1480-4b0d-9cd8-258acf53f370",
  "sourceToolAssistantUUID": "fdd33c01-8410-4544-8948-1f11a79d298a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-12T00:21:42.853Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fxui3T3EehQRzibJL8BLqw`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.03562",
  "prompt": "Find and extract: (1) Table 2 in full detail - what are all the columns and rows, what quantization schemes are compared, and what are the exact numbers showing that lower MSE can correlate with worse score-space metrics? (2) Any explicit discussion of whether within a SINGLE quantization scheme (not across schemes), embedding-space MSE ranking of different configurations correlates with score-space ranking. (3) The paper's explicit claims about when storage MSE does vs does not predict behavioral damage. (4) Section 6 or Discussion/Limitations if they exist - does the paper acknowledge cases where MSE might still be a valid proxy?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aade07ad-1480-4b0d-9cd8-258acf53f370",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011CawifcH6bxjTMG2bxz3Uj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38561915-4bd0-44d6-9480-ef4ec90a35f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa15MuPWTQxWjfJieuTivS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 14748,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 831
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 14748,
          "cache_creation_input_tokens": 831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 831,
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

_source line 20 · 2026-05-12T00:21:49.683Z_

<details><summary>↩ Tool result · `toolu_01Fxui3T3EehQRzibJL8BLqw`</summary>

```text
# Analysis of HeadQ Paper's MSE Claims

## (1) Table 2 Details

**Columns:** Model, Method, Key MSE, Fisher RMSE, Attention KL, Output MSE

**Rows & Quantization Schemes:**
- Qwen2-0.5B: FPQ vs. Centered TurboQuant-MSE
- GPT-2 124M: FPQ vs. Centered TurboQuant-MSE

**Key Finding:** The centered TurboQuant-MSE baseline achieves *lower* raw key MSE (0.082 vs 0.137 on Qwen2) yet exhibits *worse* Fisher error (0.466 vs 0.205), attention KL (0.404 vs 0.052), and output MSE (0.006 vs 0.002).

---

## (2) Within-Scheme MSE vs. Score-Space Ranking

The paper does **not** explicitly discuss whether different configurations of a *single* quantization scheme show correlated MSE and score-space rankings. The evidence provided compares *across* different schemes (FPQ vs. TurboQuant), not calibration variants within one approach.

---

## (3) Explicit Claims on MSE Predictiveness

The paper states: "storage MSE, by contrast, pays for all three pieces: the active coefficients, the token-shared shift, and the per-token orthogonal components. Therefore there exist key perturbations with arbitrarily large storage MSE and exactly unchanged attention."

The core claim is that MSE "cannot rank behavioral damage in general" because a large null-space perturbation can have zero attention impact while requiring high storage error.

---

## (4) Discussion/Limitations on MSE Validity

**Section 8 (Limitations)** acknowledges constraints but does not argue MSE regains validity in specific contexts. The paper treats score-visible geometry as the correct proxy across its test cases, without carving out domains where traditional MSE ranking might remain reliable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38561915-4bd0-44d6-9480-ef4ec90a35f1",
  "isSidechain": true,
  "promptId": "d61aec02-1791-4578-9945-5769da9d7a59",
  "agentId": "a1274b1642de5ffda",
  "type": "user",
  "uuid": "ef2fc684-ef6c-47da-9e26-f07b62c9c802",
  "sourceToolAssistantUUID": "38561915-4bd0-44d6-9480-ef4ec90a35f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-12T00:22:28.095Z_

Now I have comprehensive information. Here are my findings:

---

## Findings on HeadQ (arXiv:2605.03562)

### 1. The Null-Space Intervention Experiment (Section 5.2)

The experiment constructs an **alpha intervention** on cached keys:

**K_alpha = DeltaK + alpha * 1 * k_bar^T**

This restores a token-shared mean component k_bar to the quantized keys. The critical insight: this component lies in the **softmax-null direction** -- it shifts all logits by the same constant, so exact (dense) attention is completely unchanged for any value of alpha. The experiment then measures what happens when non-equivariant quantizers must re-quantize keys that include this attention-inert energy.

**Results at alpha=1:** Non-equivariant fixed-grid quantizers convert this attention-inert storage energy into real score damage. Pythia-160M with Block FP4 suffered roughly 19.6 added Fisher damage, while per-channel affine quantizers remained invariant (~-0.0009). Qwen2-0.5B with Block FP4 added ~0.64 Fisher damage; affine stayed at ~0.0000. The conclusion: quantizers that lack translation equivariance will convert invisible storage-space energy into visible score-space harm.

### 2. Does It Demonstrate Within-Scheme Failure Modes?

**Yes, precisely.** The alpha intervention holds the quantization scheme fixed (e.g., Block FP4 throughout) and only varies the input distribution by adding an attention-inert component. Within the same Block FP4 scheme, keys with higher storage-space MSE in the attention-inert subspace produce worse score-space damage -- but this MSE increase is entirely in the softmax-null direction, meaning storage MSE would wrongly flag it as damaging even before quantization, while the real damage comes only because the quantizer is not translation-equivariant. This is a within-scheme failure mode: the storage-space MSE in the inert subspace genuinely converts to score damage after quantization, but only for non-equivariant quantizers.

### 3. Fisher-Information Weighting for PCA Components

The paper does **not** apply Fisher weights to PCA components directly. The two concepts are related but separate:

- **Fisher information** is used as a diagnostic/evaluation metric. The Fisher quadratic is: I_{q,K}(deltaK) = delta_s^T (diag(p) - p*p^T) delta_s, which equals the p-weighted centered variance of score error. It measures how much a key perturbation disturbs attention, weighted by the attention distribution itself (tokens receiving higher attention weight contribute more).

- **Query-PCA bases** are computed as the top-r principal components of the post-RoPE query distribution from calibration data. These are used to define the subspace for the low-rank residual side-code. They are chosen by standard PCA (variance-maximizing), not by Fisher weighting. The validation is empirical: rank-4 query-PCA captures ~87% of query-axis variance and achieves Fisher/Base ratio of 0.1727, while random bases of equal overhead fail catastrophically (ratios >1.0).

The connection is that query-PCA identifies the directions in key-space that are score-visible (because score = q^T k / sqrt(d)), and Fisher information then validates that corrections along those directions actually reduce behavioral damage.

### 4. Does Embedding-Space Error Ranking Correlate with Score-Space Ranking Within a Scheme?

The paper's evidence on this point is **across schemes, not within a single scheme's hyperparameter sweep.** The key counterexample (Table 2) compares FPQ vs. Centered TurboQuant-MSE -- two different methods. TurboQuant achieves lower key MSE (0.082 vs 0.137 on Qwen2) but worse Fisher error (0.466 vs 0.205), attention KL (0.404 vs 0.052), and output MSE (0.006 vs 0.002).

The paper's explicit claim is that MSE "cannot rank behavioral damage in general" because perturbations in the softmax-null and query-orthogonal subspaces inflate MSE without affecting attention. However, the paper does not directly test whether, within a single quantization scheme (e.g., varying only bit-width or group size of the same quantizer), MSE ranking still tracks score-space ranking. The null-space intervention (Section 5.2) is the closest to a within-scheme test, and it shows that within Block FP4, adding inert storage energy does cause score damage -- but this is a specific pathology of non-equivariant quantizers, not a general MSE-vs-score correlation test.

**Bottom line:** The claim that "within the same quantization scheme, embedding-space error ranking correlates with score-space ranking" is neither directly validated nor directly refuted by HeadQ's evidence. The paper demonstrates that across schemes, MSE ranking can be entirely wrong. Within a single non-equivariant scheme, the null-space experiment shows MSE can be misleading. But the paper does not systematically sweep configurations within one scheme to test whether MSE remains a reliable ordinal proxy in that restricted setting. The paper's Section 8 (Limitations) does not carve out a domain where MSE might remain valid either.

Sources:
- [HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization (Abstract)](https://arxiv.org/abs/2605.03562)
- [HeadQ Full Paper (HTML)](https://arxiv.org/html/2605.03562)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef2fc684-ef6c-47da-9e26-f07b62c9c802",
  "isSidechain": true,
  "agentId": "a1274b1642de5ffda",
  "requestId": "req_011CawigegjaAeNuyrPbXv2P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ea95249-6df6-4886-8b02-8030d1e53b7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "44ee0f81-bd3c-4c23-9dc2-b38e1b0369cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDHqCWXg8zNDwLSySL1wAH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 15579,
      "output_tokens": 1339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 697
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1339,
          "cache_read_input_tokens": 15579,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 697,
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
