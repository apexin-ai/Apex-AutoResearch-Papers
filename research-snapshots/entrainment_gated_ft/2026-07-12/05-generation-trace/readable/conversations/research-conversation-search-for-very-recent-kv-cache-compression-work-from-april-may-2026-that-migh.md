# Research conversation: Search for very recent KV cache compression work from April-May 2026 that might be missing from the CompressLink proposa

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-acff6feaecf4f7787.jsonl`
- **Structured JSON:** [`9d2437f8ca14901bee09.json`](../../sessions/9d/9d2437f8ca14901bee09.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-11T23:35:48.937Z_

Search for very recent KV cache compression work from April-May 2026 that might be missing from the CompressLink proposal. Specifically:

1. "RateQuant" arXiv:2605.06675 - rate-distortion-optimal mixed-precision KV quantization
2. "CommVQ" ICML 2025 from Apple - RoPE-commutative vector quantization for KV cache
3. Any other KV cache compression papers from March-May 2026 that combine compression with chunk-level or document-level caching
4. Search: "KV cache compression 2026 RAG" site:arxiv.org
5. Search: "position independent" "compressed" "KV cache" 2026

Report what you find. Under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "acff6feaecf4f7787",
  "type": "user",
  "uuid": "bb33a087-2ee4-425f-8f63-b2fb8400feee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:35:48.938Z_

```json
{
  "parentUuid": "bb33a087-2ee4-425f-8f63-b2fb8400feee",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
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
  "uuid": "4e8c96e4-2b43-4fe6-821f-ba955a52e32e",
  "timestamp": "2026-05-11T23:35:48.938Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:35:51.511Z_



I'll search for these recent papers and topics across multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e8c96e4-2b43-4fe6-821f-ba955a52e32e",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfB9WeP3u7raab6rRqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8eaab530-c60d-4baa-afbf-65cf118ba6db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xw3ntR1SbbLDQXpefJf9Zs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 730,
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

_source line 4 · 2026-05-11T23:35:51.846Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AWE6dxg17dZKBi5GvWkSAa`</summary>

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
  "parentUuid": "8eaab530-c60d-4baa-afbf-65cf118ba6db",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfB9WeP3u7raab6rRqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efbb6d1a-cdb9-463e-a970-cd216163fb5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xw3ntR1SbbLDQXpefJf9Zs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 8223,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 730
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 730,
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

_source line 5 · 2026-05-11T23:35:51.851Z_

<details><summary>↩ Tool result · `toolu_01AWE6dxg17dZKBi5GvWkSAa`</summary>

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
  "parentUuid": "efbb6d1a-cdb9-463e-a970-cd216163fb5b",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "acff6feaecf4f7787",
  "type": "user",
  "uuid": "1df7217c-1eb8-4df0-8a24-94f6a9d62f9e",
  "sourceToolAssistantUUID": "efbb6d1a-cdb9-463e-a970-cd216163fb5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:35:54.450Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1df7217c-1eb8-4df0-8a24-94f6a9d62f9e",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfBMxkKmLsHHGEZjj5d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38fddbba-acd9-4798-b552-8efe19173177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7RynodSWiAWdukyYoLMWp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 7 · 2026-05-11T23:35:55.399Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GGBxJ8dKk3h3feVjAgLEuu`</summary>

```json
{
  "query": "RateQuant arXiv 2605.06675 rate-distortion mixed-precision KV quantization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38fddbba-acd9-4798-b552-8efe19173177",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfBMxkKmLsHHGEZjj5d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba8e4871-b958-4d0e-b958-8a0706a5653c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7RynodSWiAWdukyYoLMWp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 8 · 2026-05-11T23:35:56.867Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015X2tmvNDnnBbKatMMWFDs2`</summary>

```json
{
  "query": "CommVQ ICML 2025 Apple RoPE-commutative vector quantization KV cache"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba8e4871-b958-4d0e-b958-8a0706a5653c",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfBMxkKmLsHHGEZjj5d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ba59760-c860-4c27-8583-73f77865d11b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7RynodSWiAWdukyYoLMWp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 9 · 2026-05-11T23:35:57.402Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SfBeViEqgetem7igR6gnEm`</summary>

```json
{
  "query": "KV cache compression 2026 RAG",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ba59760-c860-4c27-8583-73f77865d11b",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfBMxkKmLsHHGEZjj5d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0607ab1d-1e68-47ef-b3f6-30e1a191d319",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7RynodSWiAWdukyYoLMWp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 10 · 2026-05-11T23:35:58.349Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0177vudkg6qD2cUYyf8GJsxu`</summary>

```json
{
  "query": "\"position independent\" \"compressed\" \"KV cache\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0607ab1d-1e68-47ef-b3f6-30e1a191d319",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfBMxkKmLsHHGEZjj5d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a0af676-2057-41cd-ab62-267644fe81e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7RynodSWiAWdukyYoLMWp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 11 · 2026-05-11T23:35:58.900Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J6tnLqed6xcGPUAuMwEj3D`</summary>

```json
{
  "query": "KV cache compression chunk-level document-level caching 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a0af676-2057-41cd-ab62-267644fe81e3",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfBMxkKmLsHHGEZjj5d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "780b75fd-8e46-43a1-9015-966eb42678c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7RynodSWiAWdukyYoLMWp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8953,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1409
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 315,
          "cache_read_input_tokens": 8953,
          "cache_creation_input_tokens": 1409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1409,
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

_source line 12 · 2026-05-11T23:36:00.224Z_

<details><summary>↩ Tool result · `toolu_01GGBxJ8dKk3h3feVjAgLEuu`</summary>

```text
Web search results for query: "RateQuant arXiv 2605.06675 rate-distortion mixed-precision KV quantization"

Links: [{"title":"[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/abs/2605.06675"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/new"},{"title":"Flexible Mixed Precision Quantization for Learned Image Compression","url":"https://arxiv.org/html/2506.01221"},{"title":"AlignedKV: Reducing Memory Access of KV-Cache with Precision-Aligned Quantization","url":"https://arxiv.org/html/2409.16546v2"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"},{"title":"HeadQ: Model-Visible Distortion and a Prototype KV Quantizer-Corrector Codec","url":"https://arxiv.org/html/2605.03562"},{"title":"WindowQuant: Mixed-Precision KV Cache Quantization based on Window-Level Similarity for VLMs Inference Optimization","url":"https://arxiv.org/html/2605.02262"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.18643"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new"}]

I found the paper you're looking for! Here's what the search results reveal about RateQuant (arXiv 2605.06675):

## Overview

RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory addresses how large language models cache key-value (KV) pairs during generation, with the KV cache growing linearly with sequence length and becoming a primary memory bottleneck.

## Key Problem Addressed

Current quantizers assign the same bit-width to every attention head, ignoring large variation in head importance, so a natural idea is to allocate more bits to important heads and fewer to the rest. However, each quantizer follows a different distortion curve D(b)=alpha*beta^{-b} with decay rate beta varying from 3.6 to 5.3 across quantizer designs, and applying one quantizer's distortion model to another inverts the allocation order and makes performance worse than uniform quantization.

## Solution

RateQuant fits a per-quantizer distortion model from a small calibration set, then solves the resulting bit-allocation problem in closed form via reverse waterfilling from rate-distortion theory.

## Results

On Qwen3-8B at 2.5 average bits, calibrated RateQuant reduces KIVI's perplexity from 49.3 to 14.9 (70% reduction) and improves QuaRot by 6.6 PPL, with the entire calibration taking 1.6 s on a single GPU and adding zero overhead at inference time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba8e4871-b958-4d0e-b958-8a0706a5653c",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "acff6feaecf4f7787",
  "type": "user",
  "uuid": "4d3c9ff6-0089-4af0-bf51-1932517d820e",
  "sourceToolAssistantUUID": "ba8e4871-b958-4d0e-b958-8a0706a5653c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-11T23:36:02.771Z_

<details><summary>↩ Tool result · `toolu_015X2tmvNDnnBbKatMMWFDs2`</summary>

```text
Web search results for query: "CommVQ ICML 2025 Apple RoPE-commutative vector quantization KV cache"

Links: [{"title":"CommVQ: Commutative Vector Quantization for KV Cache Compression - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/commutative-vector-quantization"},{"title":"CommVQ: Commutative Vector Quantization for KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=sbbyCB39HN"},{"title":"CommVQ: Commutative Vector Quantization for KV Cache Compression","url":"https://arxiv.org/html/2506.18879v1"},{"title":"ICML Poster CommVQ: Commutative Vector Quantization for KV Cache Compression","url":"https://icml.cc/virtual/2025/poster/43828"},{"title":"GitHub - UMass-Embodied-AGI/CommVQ: [ICML 2025] CommVQ: Commutative Vector Quantization for KV Cache Compression","url":"https://github.com/UMass-Embodied-AGI/CommVQ"},{"title":"[2506.18879] CommVQ: Commutative Vector Quantization for KV Cache Compression","url":"https://arxiv.org/abs/2506.18879"},{"title":"CommVQ: Commutative Vector Quantization for KV Cache ...","url":"https://www.arxiv.org/pdf/2506.18879"},{"title":"CommVQ: Commutative Vector Quantization for KV Cache Compression","url":"https://proceedings.mlr.press/v267/li25du.html"},{"title":"[PDF] CommVQ: Commutative Vector Quantization for KV Cache Compression | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CommVQ:-Commutative-Vector-Quantization-for-KV-Li-Zhang/cadb8aa5ee529a865cdc90c22cddb2bcf6895217"},{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/quantspec"}]

Based on the search results, here's what I found about CommVQ:

## Overview
CommVQ is a novel KV cache quantization method that reduces FP16 KV cache size by 87.5% while maintaining high accuracy through additive quantization and a RoPE-commutative codebook.

## Technical Approach
The method leverages additive quantization by introducing a lightweight encoder and codebook to compress the KV cache, which can then be decoded with a simple matrix multiplication. To tackle high computational costs during decoding, the codebook is designed to be commutative with Rotary Position Embedding (RoPE), and an Expectation-Maximization (EM) algorithm is utilized to learn the codebook.

## Performance Results
Experiments on long-context benchmarks and GSM8K show that the method reduces FP16 KV cache size by 87.5% with 2-bit quantization, while outperforming state-of-the-art KV cache quantization methods. It enables 1-bit KV cache quantization with minimal accuracy loss, allowing a LLaMA-3.1 8B model to run with a 128K context length on a single RTX 4090 GPU.

## Publication
CommVQ was presented as an ICML 2025 poster, and the source code is available at: https://github.com/UMass-Embodied-AGI/CommVQ.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ba59760-c860-4c27-8583-73f77865d11b",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "acff6feaecf4f7787",
  "type": "user",
  "uuid": "80afd19a-ae0a-4694-87f3-c2f808ee9453",
  "sourceToolAssistantUUID": "2ba59760-c860-4c27-8583-73f77865d11b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T23:36:06.110Z_

<details><summary>↩ Tool result · `toolu_01J6tnLqed6xcGPUAuMwEj3D`</summary>

```text
Web search results for query: "KV cache compression chunk-level document-level caching 2026 arxiv"

Links: [{"title":"[2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://arxiv.org/abs/2502.00299"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://arxiv.org/html/2502.00299v5"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"CacheGen: KV Cache Compression and Streaming for Fast Large","url":"https://arxiv.org/pdf/2310.07240"},{"title":"Published as a conference paper at ICLR 2026 ADAPTIVE KV-CACHE COMPRESSION","url":"https://www.arxiv.org/pdf/2509.03136"},{"title":"[2603.20218] An experimental study of KV cache reuse strategies in chunk-level caching systems","url":"https://arxiv.org/abs/2603.20218"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"KV Cache Offloading for Context-Intensive Tasks","url":"https://arxiv.org/html/2604.08426"},{"title":"1 Introduction","url":"https://arxiv.org/html/2510.09665v1"},{"title":"[2510.00231] The Pitfalls of KV Cache Compression","url":"https://arxiv.org/abs/2510.00231"}]

I found several relevant research papers on KV cache compression with chunk-level and document-level caching approaches. Here are the key findings:

## ChunkKV: Semantic-Preserving KV Cache Compression

ChunkKV fundamentally reimagines KV cache compression by treating semantic chunks rather than isolated tokens as basic compression units, preserving complete linguistic structures and contextual integrity. Large Language Models require significant GPU memory when processing long texts, with the KV cache consuming up to 70% of total memory during inference.

The method includes a novel layer-wise index reuse technique that exploits the higher cross-layer similarity of preserved indices in ChunkKV, reducing computational overhead and improving throughput by 26.5%.

## Chunk-Level Caching Systems

Chunk level caching accelerates inference by precomputing KV caches for retrieved chunks and reusing them, though these caches miss cross-attention dependencies between chunks, which can reduce output quality.

## Document-Level and Cross-Query Caching

Cross-query caching avoids redundant compute by persisting the KV cache of a prefix beyond the lifecycle of a query and reusing it when subsequent queries reuse the prefix (such as the same prompt template or retrieved document chunk), significantly lowering both time-to-first-token and overall GPU resource consumption during the prefill phase.

These papers demonstrate emerging approaches to optimize KV cache management at multiple granularities, from token-level to document-level caching strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "780b75fd-8e46-43a1-9015-966eb42678c3",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "acff6feaecf4f7787",
  "type": "user",
  "uuid": "a8ca6916-4917-4b93-9f29-914d58a7dac3",
  "sourceToolAssistantUUID": "780b75fd-8e46-43a1-9015-966eb42678c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T23:36:06.140Z_

<details><summary>↩ Tool result · `toolu_0177vudkg6qD2cUYyf8GJsxu`</summary>

```text
Web search results for query: ""position independent" "compressed" "KV cache" 2026"

Links: [{"title":"LMCache + Redis: Distributed KV Cache for Enterprise LLM Inference - barrahome.org","url":"https://barrahome.org/2026/02/08/lmcache-redis-distributed-kv-cache.md"},{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Google’s TurboQuant Compression May Support Faster Inference, Same Accuracy on Less Capable Hardware - InfoQ","url":"https://www.infoq.com/news/2026/04/turboquant-compression-kv-cache/"},{"title":"CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving | USENIX","url":"https://www.usenix.org/conference/fast26/presentation/liu-yang"},{"title":"CacheGen: KV Cache Compression and Streaming for Fast Large","url":"https://cs.stanford.edu/~keithw/sigcomm2024/sigcomm24-final1571-acmpaginated.pdf"},{"title":"EPIC: Efficient Position-Independent Caching for Serving Large Language Models | OpenReview","url":"https://openreview.net/forum?id=qjd3ZUiHRT&noteId=nEjRCvdG9t"},{"title":"EPIC: Efficient Position-Independent Caching for Serving Large Language Models","url":"https://arxiv.org/pdf/2410.15332"},{"title":"Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries","url":"https://arxiv.org/html/2603.11564"},{"title":"New KV cache compaction technique cuts LLM memory 50x without accuracy loss | VentureBeat","url":"https://venturebeat.com/orchestration/new-kv-cache-compaction-technique-cuts-llm-memory-50x-without-accuracy-loss"}]

Based on the search results, here are the key findings related to position-independent, compressed KV cache techniques in 2026:

## Position-Independent Caching

Position-Independent Caching (PIC) enables modular reuse of the KV vectors regardless of prefixes. Existing context caching requires exact prefix matches across requests, limiting reuse cases in settings such as few-shot learning and retrieval-augmented generation, where immutable content remains unchanged across requests but is preceded by varying prefixes.

In EPIC's compile step, individual immutable chunks are submitted to the LLM to generate and store their respective KV vectors, with each chunk encoded with position IDs starting from zero.

## KV Cache Compression Techniques

LMCache stores KV cache chunks in Redis with chunk-level reuse that is position-independent, combining distributed caching with compression capabilities.

Several compression approaches are being researched:

- TurboQuant can compress the KV cache down to 3.5 bits per value with near-zero accuracy loss and no retraining needed
- eOptShrinkQ applies compression chunk-by-chunk during prefill, where each chunk of 128 tokens passes through all layers, then the KV cache for that chunk is compressed in-place
- Attention Matching manages to compact the context by up to 50x with very little loss in quality

These techniques represent the 2026 frontier in making LLM inference more efficient by combining position-aware caching strategies with advanced compression methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a0af676-2057-41cd-ab62-267644fe81e3",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "acff6feaecf4f7787",
  "type": "user",
  "uuid": "da11aae9-a61c-4371-8fd9-e3ce528d7451",
  "sourceToolAssistantUUID": "9a0af676-2057-41cd-ab62-267644fe81e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T23:36:07.030Z_

<details><summary>↩ Tool result · `toolu_01SfBeViEqgetem7igR6gnEm`</summary>

```text
Web search results for query: "KV cache compression 2026 RAG"

Links: [{"title":"Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning","url":"https://arxiv.org/html/2503.04973v1"},{"title":"[2503.04973] Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning","url":"https://arxiv.org/abs/2503.04973"},{"title":"Published as a conference paper at ICLR 2026 ADAPTIVE KV-CACHE COMPRESSION","url":"https://www.arxiv.org/pdf/2509.03136"},{"title":"KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs","url":"https://arxiv.org/html/2604.13226"},{"title":"[2510.10129] CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/abs/2510.10129"},{"title":"CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/html/2510.10129v1"},{"title":"[2603.27819] KVSculpt: KV Cache Compression as Distillation","url":"https://arxiv.org/abs/2603.27819"},{"title":"Forget, Then Recall: Learnable Compression and Selective Unfolding via Gist Sparse Attention","url":"https://arxiv.org/html/2604.20920"},{"title":"[2602.02579] ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2602.02579"},{"title":"[2412.14838] DynamicKV: Task-Aware Adaptive KV Cache Compression for Long Context LLMs","url":"https://arxiv.org/abs/2412.14838"}]

Based on the search results, here's what I found about KV cache compression and RAG in 2026:

## Recent Developments in KV Cache Compression for RAG

Several significant advances in KV cache compression techniques have emerged recently:

### Task-Aware Compression
A task-aware key-value (KV) cache compression approach compresses external knowledge in a zero- or few-shot setup, enabling LLMs to reason efficiently over a compacted representation of all relevant information. This method improves accuracy by up to 7 absolute points over RAG with a 30× compression rate, while reducing inference latency from 0.43s to 0.16s.

### Adaptive Compression Methods
GVote is a novel adaptive compression algorithm that automatically computes optimal cache budgets through query sampling and voting mechanisms, demonstrating substantial empirical improvements across multiple benchmarks and eliminating manual tuning requirements.

### RAG-Specific Solutions
CacheClip achieves both fast time-to-first-token and high generation quality, accelerating LLM inference by up to 1.92x in prefill time, providing a practical solution to the efficiency-quality trade-off in RAG systems.

ProphetKV is a user-query-driven KV Cache reuse method that dynamically prioritizes tokens based on their semantic relevance to the user query and employs a dual-stage recomputation pipeline to fuse layer-wise attention metrics.

### Advanced Distillation-Based Approaches
KVSculpt optimizes a smaller set of unconstrained KV pairs in continuous embedding space to preserve each layer's attention behavior, instead of selecting or combining original pairs.

These methods represent the cutting edge of KV cache compression research for RAG systems in 2026, with various approaches focusing on efficiency, quality preservation, and task-awareness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0607ab1d-1e68-47ef-b3f6-30e1a191d319",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "acff6feaecf4f7787",
  "type": "user",
  "uuid": "e2c68eed-9af8-49c5-9cdb-549d1d022b2f",
  "sourceToolAssistantUUID": "0607ab1d-1e68-47ef-b3f6-30e1a191d319",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-11T23:36:11.576Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lb1trYBr6KtVSGL8RCaXw6`</summary>

```json
{
  "query": "KV Packet arXiv 2604.13226 recomputation-free context-independent KV caching"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2c68eed-9af8-49c5-9cdb-549d1d022b2f",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfCUatYnpm9nYJNPuEj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80bd76f4-445b-4a24-a239-a9e917087103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrJweg7R7fX7Ey17yqWBMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1867,
      "cache_creation_input_tokens": 3046,
      "cache_read_input_tokens": 10362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3046,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-11T23:36:12.001Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MAFw18NM61JrnXK4WYUmH4`</summary>

```json
{
  "query": "CacheSlide cross position-aware KV cache reuse FAST 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80bd76f4-445b-4a24-a239-a9e917087103",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfCUatYnpm9nYJNPuEj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "369c7999-0170-4ee7-9b8b-54147d0965e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrJweg7R7fX7Ey17yqWBMH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1867,
      "cache_creation_input_tokens": 3046,
      "cache_read_input_tokens": 10362,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3046
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1867,
          "output_tokens": 129,
          "cache_read_input_tokens": 10362,
          "cache_creation_input_tokens": 3046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3046,
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

_source line 19 · 2026-05-11T23:36:19.194Z_

<details><summary>↩ Tool result · `toolu_01MAFw18NM61JrnXK4WYUmH4`</summary>

```text
Web search results for query: "CacheSlide cross position-aware KV cache reuse FAST 2026"

Links: [{"title":"CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving | USENIX","url":"https://www.usenix.org/conference/fast26/presentation/liu-yang"},{"title":"CacheSlide: Unlocking Cross Position-Aware KV Cache ...","url":"https://www.usenix.org/system/files/fast26-liu-yang.pdf"},{"title":"Fused KV Caching","url":"https://www.aussieai.com/research/fused-kv-caching"},{"title":"Architecting for Reuse: A Deep Journey into the Heart of KV Caching","url":"https://blog.everpuredata.com/purely-technical/cut-llm-inference-costs-with-kv-caching/"},{"title":"LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference","url":"https://arxiv.org/html/2510.09665v2"},{"title":"GitHub - jjiantong/Awesome-KV-Cache-Optimization: [ACL 2026] Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization · GitHub","url":"https://github.com/jjiantong/Awesome-KV-Cache-Optimization"},{"title":"KV Cache TTL for Multi-Turn Agent Scheduling — AI Post Transformers","url":"https://podcast.do-not-panic.com/episodes/kv-cache-ttl-for-multi-turn-agent-scheduling/"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"1 Introduction","url":"https://arxiv.org/html/2510.09665v1"},{"title":"Crusoe MemoryAlloy technology: Reinventing KV caching for cluster-scale inference","url":"https://www.crusoe.ai/resources/blog/crusoe-memoryalloy-reinventing-kv-caching-for-cluster-scale-inference"}]

Based on the search results, here's what I found about CacheSlide:

## CacheSlide Overview

CacheSlide is a novel KV cache management system that enhances positional-encoding similarity for fixed segments, computes attention for only a minimal subset of tokens, combines new and cached KVs using learned weights, and implements layer-wise and spill-aware KV-cache optimizations.

## The Problem It Addresses

Large Language Models (LLMs) are increasingly deployed in agent-based applications with complex prompt structures comprising both invariant and dynamic segments. Existing KV cache reuse strategies—PositionDependent Caching (PDC) and Position-Independent Caching (PIC)—inadequately address these scenarios, imposing either strict positional constraints or introducing significant computational overhead due to Positionally Misaligned KV Drift (PMKD) and window padding problems.

## Key Innovation

CacheSlide identifies a distinct pattern in agent workflows termed Relative-Position-Dependent Caching (RPDC), where reusable segments maintain consistent relative ordering despite absolute position shifts.

## Performance Results

CacheSlide significantly outperforms state-of-the-art baselines, achieving 3.11-4.3× reduction in latency and 3.5-5.8× improvement in throughput.

## Publication

CacheSlide was presented at the 24th USENIX Conference on File and Storage Technologies (FAST 26) in February 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "369c7999-0170-4ee7-9b8b-54147d0965e1",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "acff6feaecf4f7787",
  "type": "user",
  "uuid": "bad66288-c396-42dc-a893-6ae4066504e7",
  "sourceToolAssistantUUID": "369c7999-0170-4ee7-9b8b-54147d0965e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-11T23:36:19.478Z_

<details><summary>↩ Tool result · `toolu_01Lb1trYBr6KtVSGL8RCaXw6`</summary>

```text
Web search results for query: "KV Packet arXiv 2604.13226 recomputation-free context-independent KV caching"

Links: [{"title":"[2604.13226] KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs","url":"https://arxiv.org/abs/2604.13226"},{"title":"KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs","url":"https://arxiv.org/html/2604.13226"},{"title":"Paper page - KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs","url":"https://huggingface.co/papers/2604.13226"},{"title":"FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference","url":"https://arxiv.org/html/2505.13109"},{"title":"TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference","url":"https://arxiv.org/html/2604.19769"},{"title":"ShadowServe: Interference-Free KV Cache Fetching for Distributed Prefix Caching","url":"https://arxiv.org/html/2509.16857v1"},{"title":"PackKV: Reducing KV Cache Memory Footprint through LLM-Aware Lossy Compression","url":"https://arxiv.org/html/2512.24449"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"KVCompose: Efficient Structured KV Cache Compression with Composite Tokens","url":"https://arxiv.org/pdf/2509.05165"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722"}]

Based on the search results, here's information about the KV Packet paper (arXiv 2604.13226):

## Overview

KV Packet is a recomputation-free cache reuse framework that treats cached documents as immutable "packets" wrapped in light-weight trainable soft-token adapters, which are trained via self-supervised distillation to bridge context discontinuities.

## Problem It Addresses

Large Language Models (LLMs) rely heavily on Key-Value (KV) caching to minimize inference latency. However, standard KV caches are context-dependent: reusing a cached document in a new context requires recomputing KV states to account for shifts in attention distribution.

Existing solutions such as CacheBlend, EPIC, and SAM-KV mitigate this issue by selectively recomputing a subset of tokens; however, they still incur non-negligible computational overhead (FLOPs) and increased Time-to-First-Token (TTFT) latency.

## Key Benefits

KV Packet enables context-independent KV caching without model fine-tuning or inference-time recomputation. By wrapping document blocks with learned universal adapters, KV Packet ensures that precomputed caches are intrinsically compatible for direct concatenation. This decoupling enables seamless composition of retrieved documents at serving time with zero additional computational overhead.

## Experimental Results

Experiments on Llama-3.1 and Qwen2.5 demonstrate that the proposed KV Packet method achieves near-zero FLOPs and lower TTFT than recomputation-based baselines, while retaining F1 scores comparable to those of the full recomputation baseline.

The paper was submitted on April 14, 2026, and code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80bd76f4-445b-4a24-a239-a9e917087103",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "acff6feaecf4f7787",
  "type": "user",
  "uuid": "6e53a983-4504-428c-b811-553a0680e044",
  "sourceToolAssistantUUID": "80bd76f4-445b-4a24-a239-a9e917087103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-11T23:36:48.043Z_

Here is what I found across all five searches:

---

**1. RateQuant (arXiv:2605.06675)** -- Confirmed. Fits a per-quantizer distortion model from a small calibration set, then solves bit-allocation in closed form via reverse waterfilling. On Qwen3-8B at 2.5 avg bits it cuts KIVI perplexity from 49.3 to 14.9 (70% drop), with calibration taking 1.6 s and zero inference overhead. Directly relevant to any mixed-precision KV quantization section.

**2. CommVQ (ICML 2025, Apple/UMass)** -- Confirmed. Uses additive quantization with a RoPE-commutative codebook learned via EM. Achieves 87.5% KV size reduction at 2-bit and enables 1-bit quantization with minimal loss (LLaMA-3.1 8B at 128K context on a single RTX 4090). The RoPE-commutativity property is important for any position-independent caching scheme.

**3. Papers combining compression with chunk/document-level caching (Mar-May 2026):**
- **KV Packet** (arXiv:2604.13226) -- wraps cached documents in trainable soft-token adapters for recomputation-free, context-independent KV reuse. Near-zero extra FLOPs and lower TTFT than recomputation baselines.
- **CacheSlide** (FAST '26) -- introduces Relative-Position-Dependent Caching (RPDC) for agent workflows, achieving 3-4x latency reduction and 4-6x throughput improvement over PDC/PIC baselines.
- **KVSculpt** (arXiv:2603.27819) -- distillation-based: optimizes a smaller set of unconstrained KV pairs in continuous space to preserve attention behavior.
- **ChunkKV** (arXiv:2502.00299) -- treats semantic chunks as compression units with layer-wise index reuse, 26.5% throughput gain.

**4-5. RAG and position-independent compressed KV cache:**
- **CacheClip** (arXiv:2510.10129) -- up to 1.92x prefill speedup for RAG via KV cache reuse.
- **ProphetKV** (arXiv:2602.02579) -- query-driven selective recomputation for RAG.
- **EPIC** (arXiv:2410.15332) -- position-independent caching that encodes chunks starting from position zero; directly composable at serving time.
- **GVote** (ICLR 2026, arXiv:2509.03136) -- adaptive KV compression with automatic budget tuning via voting.

**Key gaps for CompressLink:** RateQuant's calibrated mixed-precision allocation, CommVQ's RoPE-commutative codebook, and KV Packet's zero-recomputation adapter framework are the most likely missing pieces. CacheSlide's RPDC paradigm is also relevant if CompressLink targets agentic or multi-turn RAG settings.

Sources:
- [RateQuant](https://arxiv.org/abs/2605.06675)
- [CommVQ (Apple ML Research)](https://machinelearning.apple.com/research/commutative-vector-quantization)
- [CommVQ (OpenReview)](https://openreview.net/forum?id=sbbyCB39HN)
- [KV Packet](https://arxiv.org/abs/2604.13226)
- [CacheSlide (FAST '26)](https://www.usenix.org/conference/fast26/presentation/liu-yang)
- [KVSculpt](https://arxiv.org/abs/2603.27819)
- [ChunkKV](https://arxiv.org/abs/2502.00299)
- [CacheClip](https://arxiv.org/abs/2510.10129)
- [ProphetKV](https://arxiv.org/abs/2602.02579)
- [EPIC](https://arxiv.org/pdf/2410.15332)
- [GVote / Adaptive KV-Cache Compression (ICLR 2026)](https://www.arxiv.org/pdf/2509.03136)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e53a983-4504-428c-b811-553a0680e044",
  "isSidechain": true,
  "agentId": "acff6feaecf4f7787",
  "requestId": "req_011CawfDPu8oFMeJE4YJ9hRq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1aacc5e-f06b-4cb2-91fa-06ac221eefd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhNbabDSSn5QdZA3R86rpi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 939,
      "cache_creation_input_tokens": 3048,
      "cache_read_input_tokens": 13408,
      "output_tokens": 1060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 939,
          "output_tokens": 1060,
          "cache_read_input_tokens": 13408,
          "cache_creation_input_tokens": 3048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3048,
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
