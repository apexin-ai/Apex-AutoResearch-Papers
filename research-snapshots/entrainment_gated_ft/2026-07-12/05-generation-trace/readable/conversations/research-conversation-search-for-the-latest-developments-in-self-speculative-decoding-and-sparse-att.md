# Research conversation: Search for the latest developments in self-speculative decoding and sparse attention from March-May 2026. I need to: 1. 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 1
- **Tool calls:** 30
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a25188ca95bace647.jsonl`
- **Structured JSON:** [`add28d5b20489dc36c82.json`](../../sessions/ad/add28d5b20489dc36c82.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

70 recorded events

### User

_source line 1 · 2026-05-10T20:34:35.041Z_

Search for the latest developments in self-speculative decoding and sparse attention from March-May 2026. I need to:

1. **Find any new concurrent work**: Search arXiv for papers from April-May 2026 on "self-speculative decoding", "sparse attention decoding", "head-adaptive attention", "attention prediction decoding". Are there any new methods that might overlap with or supersede the DecompSpec idea (variance-bounded head-adaptive decomposition for self-speculative decoding)?

2. **Component-Aware Self-Speculative Decoding (arXiv:2605.01106, May 2026)**: Fetch and read this paper. It exploits SSM/attention heterogeneity at component level - how does it differ from head-level decomposition?

3. **SpecKV (arXiv:2605.02888, May 2026)**: Fetch and read this paper about adaptive speculative decoding with compression-aware gamma selection. Does it address the staleness problem?

4. **SparseSpec codebase**: Search GitHub for "SparseSpec" or "sspec-project" to check if the codebase is available and what models it supports. Can it scale to Qwen3-32B?

5. **SpecAttn codebase**: Search GitHub for SpecAttn code availability.

6. **Timeline benchmarks**: Search for recent papers that report GPU hours for experiments on Qwen3-32B or similar 30B+ models. What's realistic for 200 GPU-hours?

Use WebSearch and WebFetch. Report all findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "43771b1d-f57b-4b5c-97f2-c3720f0842d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:34:35.043Z_

```json
{
  "parentUuid": "43771b1d-f57b-4b5c-97f2-c3720f0842d5",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
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
  "uuid": "b3b6ab2b-e114-4adc-95e8-9151225d2450",
  "timestamp": "2026-05-10T20:34:35.043Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T20:34:38.892Z_



I'll conduct a comprehensive search across all six areas. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3b6ab2b-e114-4adc-95e8-9151225d2450",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXYfdXk3bb7HUSrsUkG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a44928a0-5cce-4ab6-9b19-ca06db86b175",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wwMefQpjyYWw65ExLckkb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 913,
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

_source line 4 · 2026-05-10T20:34:39.127Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SaXJ8SqkkP8hQEa7Xz3EaX`</summary>

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
  "parentUuid": "a44928a0-5cce-4ab6-9b19-ca06db86b175",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXYfdXk3bb7HUSrsUkG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "899697b8-ce3f-4c7d-955f-2adf28361d4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wwMefQpjyYWw65ExLckkb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 8223,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 913,
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

_source line 5 · 2026-05-10T20:34:39.129Z_

<details><summary>↩ Tool result · `toolu_01SaXJ8SqkkP8hQEa7Xz3EaX`</summary>

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
  "parentUuid": "899697b8-ce3f-4c7d-955f-2adf28361d4e",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "21c90023-c69e-4de9-a079-02b08a5a57e8",
  "sourceToolAssistantUUID": "899697b8-ce3f-4c7d-955f-2adf28361d4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T20:34:41.814Z_



Now let me launch all the searches in parallel across all six areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21c90023-c69e-4de9-a079-02b08a5a57e8",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXYyFvgRExzeBxYr2Pa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46a3b950-c34a-44d8-ad02-dbe11c58a6fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tgUJmeRG9qwdc5P4JUAHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9136,
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

_source line 7 · 2026-05-10T20:34:42.764Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016jnrL3EryPKqbbBkgarL41`</summary>

```json
{
  "query": "self-speculative decoding 2026 arXiv new methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46a3b950-c34a-44d8-ad02-dbe11c58a6fc",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXYyFvgRExzeBxYr2Pa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6122fa3a-c45c-46d2-9b0f-8d215b86f2fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tgUJmeRG9qwdc5P4JUAHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9136,
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

_source line 8 · 2026-05-10T20:34:43.725Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01399nvYoPGijrBK9y3euy1s`</summary>

```json
{
  "query": "sparse attention decoding head-adaptive attention prediction 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6122fa3a-c45c-46d2-9b0f-8d215b86f2fb",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXYyFvgRExzeBxYr2Pa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a759d13-1c5e-4399-9682-7c514796f811",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tgUJmeRG9qwdc5P4JUAHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9136,
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

_source line 9 · 2026-05-10T20:34:44.247Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fw2WzG5MWrpDypRVaAfcvW`</summary>

```json
{
  "query": "arXiv 2605.01106 Component-Aware Self-Speculative Decoding 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a759d13-1c5e-4399-9682-7c514796f811",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXYyFvgRExzeBxYr2Pa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e242266-8393-4b13-a90a-3e2abf0aee66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tgUJmeRG9qwdc5P4JUAHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9136,
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

_source line 10 · 2026-05-10T20:34:45.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CrnjRTyWAzqVycAGm4SL2k`</summary>

```json
{
  "query": "arXiv 2605.02888 SpecKV adaptive speculative decoding compression-aware gamma 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e242266-8393-4b13-a90a-3e2abf0aee66",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXYyFvgRExzeBxYr2Pa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3d4cdcf-bc20-4b50-bb27-111753daa9e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tgUJmeRG9qwdc5P4JUAHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9136,
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

_source line 11 · 2026-05-10T20:34:46.591Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VLgjpCMmfC3ViswaX7kgfW`</summary>

```json
{
  "query": "GitHub SparseSpec sspec-project sparse speculative decoding codebase"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3d4cdcf-bc20-4b50-bb27-111753daa9e9",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXYyFvgRExzeBxYr2Pa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "495a2ef4-04b9-44ca-9513-29d6f1002430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tgUJmeRG9qwdc5P4JUAHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9136,
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

_source line 12 · 2026-05-10T20:34:46.773Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017m4ezuAUpuU3SMXM8LZVkw`</summary>

```json
{
  "query": "GitHub SpecAttn speculative attention code repository"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "495a2ef4-04b9-44ca-9513-29d6f1002430",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXYyFvgRExzeBxYr2Pa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72234fbe-0c1d-435a-84c0-efc7ba7972f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tgUJmeRG9qwdc5P4JUAHG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9136,
      "output_tokens": 346,
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
          "output_tokens": 346,
          "cache_read_input_tokens": 9136,
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

_source line 13 · 2026-05-10T20:34:49.974Z_

<details><summary>↩ Tool result · `toolu_01399nvYoPGijrBK9y3euy1s`</summary>

```text
Web search results for query: "sparse attention decoding head-adaptive attention prediction 2026 arXiv"

Links: [{"title":"Efficient Sparse Attention needs Adaptive Token Release","url":"https://arxiv.org/html/2407.02328"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"Adaptive Sparse and Monotonic Attention for Transformer- ...","url":"https://arxiv.org/pdf/2209.15176"},{"title":"vAttention: Verified Sparse Attention","url":"https://arxiv.org/html/2510.05688v1"},{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641v1"},{"title":"Sparse Attention Post-Training for Mechanistic Interpretability","url":"https://arxiv.org/html/2512.05865v1"},{"title":"SpargeAttn: Accurate Sparse Attention Accelerating Any Model Inference","url":"https://arxiv.org/html/2502.18137v1"},{"title":"SeerAttention-R: Sparse Attention Adaptation for Long ...","url":"https://arxiv.org/pdf/2506.08889"},{"title":"SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference","url":"https://arxiv.org/html/2502.18137v4"},{"title":"FASA: Frequency-aware Sparse Attention","url":"https://arxiv.org/pdf/2602.03152"}]

I found several relevant arXiv papers on sparse attention, decoding, and head-adaptive mechanisms. Here are the key results:

## Recent Sparse Attention and Adaptive Methods (2025-2026)

Recent work on head-adaptive sparse attention includes methods that predict token importance for decoding and incorporate dynamic token budget allocation per head.

SpecAttn is a novel training-free approach that integrates with speculative decoding techniques to enable efficient sparse attention, exploiting attention weights computed by draft models during speculative decoding to identify important tokens for the target model.

SpargeAttn proposes a universal sparse and quantized attention using a two-stage online filter that rapidly and accurately predicts the attention map, enabling the skip of some matrix multiplications.

vAttention adapts the sparsity in each layer for each head and for each specific query.

FASA is rooted on the observation that differential frequencies within RoPE induce functional sparsity among frequency chunks, with only sparse subsets contributing significantly to act as a high-fidelity computational filter, restricting full-precision attention to the most salient tokens.

These papers represent cutting-edge research on combining sparse attention mechanisms with head-adaptive and prediction-based approaches for efficient LLM inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a759d13-1c5e-4399-9682-7c514796f811",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "8e660b18-fcf8-4dc5-8ad7-b79871e14b3a",
  "sourceToolAssistantUUID": "9a759d13-1c5e-4399-9682-7c514796f811",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T20:34:50.431Z_

<details><summary>↩ Tool result · `toolu_016jnrL3EryPKqbbBkgarL41`</summary>

```text
Web search results for query: "self-speculative decoding 2026 arXiv new methods"

Links: [{"title":"[2605.01106] Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/abs/2605.01106"},{"title":"[2603.03251] Speculative Speculative Decoding","url":"https://arxiv.org/abs/2603.03251"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"},{"title":"Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/html/2605.01106"},{"title":"[2510.04147] Self Speculative Decoding for Diffusion Large Language Models","url":"https://arxiv.org/abs/2510.04147"},{"title":"Speculative Speculative Decoding","url":"https://arxiv.org/html/2603.03251"},{"title":"Speculative Speculative Decoding Tanishq Kumar1,* Tri Dao2,3 Avner May3","url":"https://arxiv.org/pdf/2603.03251"},{"title":"LogitSpec: Accelerating Retrieval-based Speculative Decoding via Next Next Token Speculation","url":"https://arxiv.org/html/2507.01449"},{"title":"SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection","url":"https://arxiv.org/html/2605.02888"}]

Based on the search results, here are some recent self-speculative decoding methods from 2026 on arXiv:

## Recent Self-Speculative Decoding Methods (2026)

**Component-Aware Self-Speculative Decoding in Hybrid Language Models**
This method exploits the internal architectural heterogeneity of hybrid language models, isolating the SSM/linear-attention subgraph as a zero-cost internal draft. It evaluates two architecturally distinct hybrid families: Falcon-H1 (parallel: Mamba-2 + attention per layer) and Qwen3.5 (sequential: interleaved linear and attention layers), with parallel hybrids achieving acceptance rates of alpha = 0.68 at draft length k=2 under greedy decoding, while sequential hybrids yield only alpha = 0.038.

**Speculative Speculative Decoding (SSD)**
This method introduces speculative speculative decoding to parallelize drafting and verification operations, where while a verification is ongoing, the draft model predicts likely verification outcomes and prepares speculations pre-emptively for them, and if the actual verification outcome is then in the predicted set, a speculation can be returned immediately, eliminating drafting overhead entirely. The result is Saguaro, an optimized SSD algorithm that achieves 30% faster performance than optimized speculative decoding baselines and up to 5x faster than autoregressive decoding with open source inference engines.

**SpecKV: Adaptive Speculative Decoding**
SpecKV presents a lightweight adaptive controller that selects the speculation length per speculation step using signals extracted from the draft model itself. SpecKV achieves a 56.0% improvement in expected tokens per speculation step over the fixed gamma=4 default.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6122fa3a-c45c-46d2-9b0f-8d215b86f2fb",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "0b53a89c-38b2-4afa-b2f6-925deeab8455",
  "sourceToolAssistantUUID": "6122fa3a-c45c-46d2-9b0f-8d215b86f2fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T20:34:51.117Z_

<details><summary>↩ Tool result · `toolu_01Fw2WzG5MWrpDypRVaAfcvW`</summary>

```text
Web search results for query: "arXiv 2605.01106 Component-Aware Self-Speculative Decoding 2026"

Links: [{"title":"[2605.01106] Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/abs/2605.01106"},{"title":"Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/html/2605.01106"},{"title":"SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection","url":"https://arxiv.org/html/2605.02888"},{"title":"[2605.02888] SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection","url":"https://arxiv.org/abs/2605.02888"},{"title":"SpecMemo: Speculative Decoding is in Your Pocket","url":"https://arxiv.org/html/2506.01986v1"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"},{"title":"Speculative Speculative Decoding","url":"https://arxiv.org/html/2603.03251"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification","url":"https://arxiv.org/html/2512.02337v1"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"}]

I found the paper you're looking for! Here's information about arXiv 2605.01106:

**Paper Title:** Component-Aware Self-Speculative Decoding in Hybrid Language Models

**Authors:** Hector Borobia, Elies Seguí-Mas, and Guillermina Tormo-Carbó

**Submission Date:** Submitted on 1 May 2026

**Key Contribution:** The paper introduces component-aware self-speculative decoding, the first method to exploit the internal architectural heterogeneity of hybrid language models, isolating the SSM/linear-attention subgraph as a zero-cost internal draft.

**Main Findings:** Parallel hybrids achieve acceptance rates of alpha = 0.68 at draft length k=2 under greedy decoding, while sequential hybrids yield only alpha = 0.038 -- an 18x gap attributable to how each architecture integrates its components.

**Evaluation:** The paper evaluates this on two architecturally distinct hybrid families: Falcon-H1 (parallel: Mamba-2 + attention per layer) and Qwen3.5 (sequential: interleaved linear and attention layers)

**Key Insight:** The composition pattern of hybrid models -- not merely the presence of alternative components -- determines whether component-level self-speculation is viable.

You can access the paper directly at: https://arxiv.org/abs/2605.01106


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e242266-8393-4b13-a90a-3e2abf0aee66",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "0bc2d54b-3c66-4075-ba79-ca79507173bc",
  "sourceToolAssistantUUID": "1e242266-8393-4b13-a90a-3e2abf0aee66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T20:34:52.789Z_

<details><summary>↩ Tool result · `toolu_017m4ezuAUpuU3SMXM8LZVkw`</summary>

```text
Web search results for query: "GitHub SpecAttn speculative attention code repository"

Links: [{"title":"GitHub - hemingkx/SpecDec: Codes for our paper \"Speculative Decoding: Exploiting Speculative Execution for Accelerating Seq2seq Generation\" (EMNLP 2023 Findings) · GitHub","url":"https://github.com/hemingkx/SpecDec"},{"title":"GitHub - lucidrains/speculative-decoding: Explorations into some recent techniques surrounding speculative decoding · GitHub","url":"https://github.com/lucidrains/speculative-decoding"},{"title":"blog/whisper-speculative-decoding.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/whisper-speculative-decoding.md"},{"title":"GitHub - romsto/Speculative-Decoding: Implementation of the paper Fast Inference from Transformers via Speculative Decoding, Leviathan et al. 2023. · GitHub","url":"https://github.com/romsto/Speculative-Decoding"},{"title":"GitHub - thu-ml/SpargeAttn: [ICML2025] SpargeAttention: A training-free sparse attention that accelerates any model inference. · GitHub","url":"https://github.com/thu-ml/SpargeAttn"},{"title":"GitHub - thu-ml/SageAttention: [ICLR2025, ICML2025, NeurIPS2025 Spotlight] Quantized Attention achieves speedup of 2-5x compared to FlashAttention, without losing end-to-end metrics across language, image, and video models. · GitHub","url":"https://github.com/thu-ml/SageAttention"},{"title":"speculative-execution · GitHub Topics · GitHub","url":"https://github.com/topics/speculative-execution"},{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641"},{"title":"GitHub - dilab-zju/self-speculative-decoding: Code associated with the paper **Draft & Verify: Lossless Large Language Model Acceleration via Self-Speculative Decoding**","url":"https://github.com/dilab-zju/self-speculative-decoding"},{"title":"Spectector","url":"https://spectector.github.io/"}]

Based on the search results, I found information about SpecAttn, which is a speculative attention research work. Here's what I found:

## SpecAttn Overview

SpecAttn is a training-free framework that fuses speculative decoding with dynamic sparse attention to drastically reduce the key-value (KV) cache usage in LLM inference. By mapping layers using KL divergence similarity and employing a sorting-free top-p token selection mechanism at each decoding step, SpecAttn achieves significant KV cache reductions and maintains competitive perplexity compared to existing sparse attention methods.

## Performance

SpecAttn can reduce KV cache access by up to 78% while maintaining reasonable perplexity degradation (15.29% relative increase for p=0.95). More than 4x speedup is achieved for prompt length 2048.

## Technical Approach

SpecAttn unites speculative decoding's training-free paradigm with fully dynamic, content-aware sparse attention by exploiting the attention weights already computed by the draft model to score and select the most informative tokens at each generation step.

Note: While the search results show SpecAttn described in an arXiv paper, I did not find a specific GitHub repository URL for the SpecAttn code in the search results. The work appears to be a recent academic contribution rather than an established public GitHub repository at this time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72234fbe-0c1d-435a-84c0-efc7ba7972f3",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "8e69930d-2835-40e0-8b2b-0132123f24b0",
  "sourceToolAssistantUUID": "72234fbe-0c1d-435a-84c0-efc7ba7972f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T20:34:53.002Z_

<details><summary>↩ Tool result · `toolu_01CrnjRTyWAzqVycAGm4SL2k`</summary>

```text
Web search results for query: "arXiv 2605.02888 SpecKV adaptive speculative decoding compression-aware gamma 2026"

Links: [{"title":"[2605.02888] SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection","url":"https://arxiv.org/abs/2605.02888"},{"title":"SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection","url":"https://arxiv.org/html/2605.02888"},{"title":"Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/html/2605.01106"},{"title":"SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification","url":"https://arxiv.org/html/2512.02337v1"},{"title":"SpecDec++: Boosting Speculative Decoding via Adaptive Candidate Lengths","url":"https://arxiv.org/html/2405.19715v1"},{"title":"Utility-Driven Speculative Decoding for Mixture-of-Experts","url":"https://arxiv.org/html/2506.20675v1"},{"title":"SpecMemo: Speculative Decoding is in Your Pocket","url":"https://arxiv.org/html/2506.01986v1"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://arxiv.org/html/2507.22424v1"},{"title":"SpecVLM: Fast Speculative Decoding in Vision-Language Models","url":"https://arxiv.org/html/2509.11815v1"},{"title":"[2605.00342] Making Every Verified Token Count: Adaptive Verification for MoE Speculative Decoding","url":"https://arxiv.org/abs/2605.00342"}]

I found the paper! Here's information about arXiv 2605.02888:

## SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection

SpecKV addresses speculative decoding, which accelerates LLM inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length γ, which determines how many tokens the draft model proposes per step.

### Key Problem

Nearly all existing systems use a fixed γ (typically 4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model.

### The Solution

SpecKV is a lightweight adaptive controller that selects γ per speculation step using signals extracted from the draft model itself. The authors profile speculative decoding across 4 task categories, 4 speculation lengths, and 3 compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence.

### Results

SpecKV-fast achieves 5.82 expected tokens per step overall, a 56.0% improvement over Fixed-4 (3.73 tokens/step). The SpecKV-fast controller (MLP-16) adds 0.34 ms per speculation step.

The paper was submitted on May 5, 2026, by Shikhar Shukla from the University of Kentucky.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3d4cdcf-bc20-4b50-bb27-111753daa9e9",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "43375485-5246-44e6-967c-9a7b3c51086a",
  "sourceToolAssistantUUID": "b3d4cdcf-bc20-4b50-bb27-111753daa9e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T20:34:54.864Z_

<details><summary>↩ Tool result · `toolu_01VLgjpCMmfC3ViswaX7kgfW`</summary>

```text
Web search results for query: "GitHub SparseSpec sspec-project sparse speculative decoding codebase"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2512.01278"},{"title":"Accelerating Large-Scale Reasoning Model Inference with ...","url":"https://arxiv.org/pdf/2512.01278"},{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2512.01278"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.01278v1"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding – Own Your AI","url":"https://ownyourai.com/accelerating-large-scale-reasoning-model-inference-with-sparse-self-speculative-decoding/"},{"title":"GitHub - hemingkx/Spec-Bench: Spec-Bench: A Comprehensive Benchmark and Unified Evaluation Platform for Speculative Decoding (ACL 2024 Findings) · GitHub","url":"https://github.com/hemingkx/Spec-Bench"},{"title":"SpecDec++: Boosting Speculative Decoding via Adaptive Candidate Lengths | OpenReview","url":"https://openreview.net/forum?id=Y131N9fUbU"},{"title":"GitHub - romsto/Speculative-Decoding: Implementation of the paper Fast Inference from Transformers via Speculative Decoding, Leviathan et al. 2023. · GitHub","url":"https://github.com/romsto/Speculative-Decoding"}]

Based on the search results, I found information about SparseSpec:

## SparseSpec Overview

SparseSpec is a speculative decoding framework that reuses the same model as both the draft and target models (i.e., self-speculation). The code is open-sourced at github.com/sspec-project/SparseSpec.

## Key Features

SparseSpec features a novel sparse attention mechanism, PillarAttn, as the draft model. PillarAttn selectively loads and computes only the critical tokens—those with the highest attention scores during inference—thereby significantly reducing memory bandwidth usage.

## System Innovations

SparseSpec co-designs self-speculation with three system innovations: (1) a unified scheduler to batch token drafting and verification, (2) delayed verification for CPU/GPU overlap, and (3) dynamic KV-Cache management to maximize memory utilization.

## Performance

Across various models and datasets, SparseSpec outperforms state-of-the-art solutions, with an up to 2.13x throughput speedup. SparseSpec's PillarAttn dynamically selects critical tokens, reducing KV-Cache memory access by up to 95%.

The framework is designed to address the memory bandwidth bottleneck in reasoning language models that generate lengthy outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "495a2ef4-04b9-44ca-9513-29d6f1002430",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "d00a6d91-b4d5-4c61-9d7b-6041f7c74dee",
  "sourceToolAssistantUUID": "495a2ef4-04b9-44ca-9513-29d6f1002430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T20:34:58.533Z_

Good, I have initial results. Now let me fetch the actual papers and do deeper searches on the remaining topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d00a6d91-b4d5-4c61-9d7b-6041f7c74dee",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXa8JffSDfyGdt9rZJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65db6672-ab5e-465c-813c-4347a0180901",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dwzQLEqHdBsrEd262nMBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 11046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4596,
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

_source line 20 · 2026-05-10T20:35:01.427Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019E7nWWNHvM5YueAtUjS4Gr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.01106",
  "prompt": "Extract the full abstract, key methodology details, which models are evaluated, acceptance rates, speedup results, and how this method differs from head-level decomposition approaches. What specific components are used as the draft vs target? How does it handle hybrid architectures?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65db6672-ab5e-465c-813c-4347a0180901",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXa8JffSDfyGdt9rZJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "264504d8-5511-42df-96c4-24ce090e422c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dwzQLEqHdBsrEd262nMBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 11046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4596,
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

_source line 21 · 2026-05-10T20:35:03.311Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GsvuxnU26AyEtx4MngoHdK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.02888",
  "prompt": "Extract the full abstract, methodology details, how gamma is selected adaptively, what signals are used from the draft model, whether it addresses KV cache staleness or stale attention problems, compression levels tested, and detailed results. Does it address the staleness problem in speculative decoding?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "264504d8-5511-42df-96c4-24ce090e422c",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXa8JffSDfyGdt9rZJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba220ba5-4621-4561-b891-0ca6e7f6e2a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dwzQLEqHdBsrEd262nMBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 11046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4596,
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

_source line 22 · 2026-05-10T20:35:05.026Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H3DtrvDn7urJfryHeroGbN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.03251",
  "prompt": "Extract the full abstract, key methodology, how speculative speculative decoding works, what is the Saguaro algorithm, performance results, and how it relates to self-speculative decoding approaches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba220ba5-4621-4561-b891-0ca6e7f6e2a3",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXa8JffSDfyGdt9rZJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5be0df2-9e1e-454e-9c69-3987499e8642",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dwzQLEqHdBsrEd262nMBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 11046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4596,
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

_source line 23 · 2026-05-10T20:35:06.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DCqMYfH4tycPmJNaVJReB8`</summary>

```json
{
  "query": "SparseSpec PillarAttn github.com/sspec-project models supported Qwen3 scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5be0df2-9e1e-454e-9c69-3987499e8642",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXa8JffSDfyGdt9rZJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f68104ac-3356-4446-bea0-74471fb94019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dwzQLEqHdBsrEd262nMBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 11046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4596,
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

_source line 24 · 2026-05-10T20:35:07.217Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012xVq7zNkfN25fpck8hJ6PE`</summary>

```json
{
  "query": "SpecAttn speculating sparse attention code release github 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f68104ac-3356-4446-bea0-74471fb94019",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXa8JffSDfyGdt9rZJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54cfa4ae-aa44-4dfd-8573-7e054542362d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dwzQLEqHdBsrEd262nMBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 11046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4596,
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

_source line 25 · 2026-05-10T20:35:07.699Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wr2BdhnFVHLR5qtbS5G3k1`</summary>

```json
{
  "query": "Qwen3-32B GPU hours training inference benchmark experiments 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54cfa4ae-aa44-4dfd-8573-7e054542362d",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXa8JffSDfyGdt9rZJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07826bd4-778e-4dc6-83d6-90ca62c6172f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dwzQLEqHdBsrEd262nMBt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 11046,
      "output_tokens": 549,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4596
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 950,
          "output_tokens": 549,
          "cache_read_input_tokens": 11046,
          "cache_creation_input_tokens": 4596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4596,
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

_source line 26 · 2026-05-10T20:35:07.800Z_

<details><summary>↩ Tool result · `toolu_019E7nWWNHvM5YueAtUjS4Gr`</summary>

```text
# Component-Aware Self-Speculative Decoding in Hybrid Language Models

## Full Abstract
"Speculative decoding accelerates autoregressive inference by drafting candidate tokens with a fast model and verifying them in parallel with the target. Self-speculative methods avoid the need for an external drafter but have been studied exclusively in homogeneous Transformer architectures. We introduce component-aware self-speculative decoding, the first method to exploit the internal architectural heterogeneity of hybrid language models, isolating the SSM/linear-attention subgraph as a zero-cost internal draft."

## Key Methodology
The approach leverages **internal architectural components** rather than separate models. The SSM (State Space Model) or linear-attention layers serve as the draft mechanism, while the full model performs verification—incurring minimal computational overhead since these components already exist within the hybrid architecture.

## Models Evaluated
- **Falcon-H1** (parallel architecture: Mamba-2 + attention per layer) at 0.5B and 3B scales
- **Qwen3.5** (sequential: interleaved linear and attention layers)
- **Qwen2.5** (pure Transformer control)

## Performance Results
- **Parallel hybrids** (Falcon-H1): α = 0.68 at draft length k=2 under greedy decoding
- **Sequential hybrids** (Qwen3.5): α = 0.038—an **18x acceptance rate gap** versus parallel models
- Perplexity ratios predict viability without running speculation itself

## Distinction from Head-Level Approaches
This method differs fundamentally by operating at the **component level** rather than layer-head decomposition, recognizing that hybrid architecture *composition patterns*—specifically whether components are parallel or sequential—determine speculation viability, not merely their presence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "264504d8-5511-42df-96c4-24ce090e422c",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "806cfb5d-bf90-4bf7-93ca-cc842e0e18bc",
  "sourceToolAssistantUUID": "264504d8-5511-42df-96c4-24ce090e422c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T20:35:10.127Z_

<details><summary>↩ Tool result · `toolu_01H3DtrvDn7urJfryHeroGbN`</summary>

```text
# Speculative Speculative Decoding: Summary

## Full Abstract
"Autoregressive decoding is bottlenecked by its sequential nature. Speculative decoding has become a standard way to accelerate inference by using a fast draft model to predict upcoming tokens from a slower target model, and then verifying them in parallel with a single target model forward pass. However, speculative decoding itself relies on a sequential dependence between speculation and verification."

The paper proposes eliminating this remaining sequential bottleneck through parallelization.

## Core Methodology
The technique works by having the draft model predict likely verification outcomes while verification is still occurring. These speculations are prepared proactively. If actual verification results match the predicted set, a speculation returns immediately, removing drafting overhead entirely.

## How SSD Works
The approach identifies and addresses three key challenges in parallelizing speculation and verification stages. Rather than waiting sequentially for draft → verify → draft cycles, both operations overlap when possible.

## Saguaro Algorithm
Saguaro represents the optimized implementation of speculative speculative decoding that solves the three identified challenges through principled methods.

## Performance Results
According to the abstract, Saguaro achieves "30% faster" performance versus optimized speculative decoding and "up to 5x faster" than standard autoregressive decoding using open source inference engines.

## Relationship to Self-Speculative Approaches
The page content provided does not contain information comparing this work to self-speculative decoding approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5be0df2-9e1e-454e-9c69-3987499e8642",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "9a298d31-e617-40e6-8bb2-3ec9e110ecbd",
  "sourceToolAssistantUUID": "e5be0df2-9e1e-454e-9c69-3987499e8642",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T20:35:10.154Z_

<details><summary>↩ Tool result · `toolu_01GsvuxnU26AyEtx4MngoHdK`</summary>

```text
# SpecKV: Adaptive Speculative Decoding Analysis

## Full Abstract
"Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length γ, which determines how many tokens the draft model proposes per step."

The paper demonstrates that optimal γ values vary across task types and compression levels, proposing an adaptive controller instead of fixed approaches.

## Adaptive Gamma Selection Mechanism
SpecKV employs a lightweight machine learning model (small MLP) that dynamically selects γ per speculation step. The controller makes real-time decisions rather than using a static configuration throughout inference.

## Signals from Draft Model
The system extracts two primary signals:
- **Draft model confidence** (correlation ≈ 0.56 with acceptance rates)
- **Draft model entropy** (also strongly predictive of acceptance)

These signals serve as input features for the MLP to predict optimal speculation length.

## Compression Levels Evaluated
Testing covered three quantization schemes:
- FP16
- INT8
- NF4

The research revealed that "the optimal γ shifts across compression regimes," indicating compression significantly impacts speculation behavior.

## Performance Results
SpecKV achieved "56.0% improvement over the fixed-γ=4 baseline with only 0.34 ms overhead per decision." Statistical significance was confirmed (p < 0.001).

## KV Cache/Staleness Issues
**The content does not address KV cache staleness or stale attention problems.** The focus remains exclusively on speculation length optimization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba220ba5-4621-4561-b891-0ca6e7f6e2a3",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "6a51287d-2023-4f00-9cb8-e0f374a36aaf",
  "sourceToolAssistantUUID": "ba220ba5-4621-4561-b891-0ca6e7f6e2a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T20:35:12.577Z_

<details><summary>↩ Tool result · `toolu_01DCqMYfH4tycPmJNaVJReB8`</summary>

```text
Web search results for query: "SparseSpec PillarAttn github.com/sspec-project models supported Qwen3 scale"

Links: [{"title":"SparseSpec: Sparse Computation Innovations","url":"https://www.emergentmind.com/topics/sparsespec"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"[Bug] Qwen3.6-27B-FP8 (dense): FP8 weight_scale_inv silently dropped → garbage output (gate_gate_up_proj loop bug in qwen3_5.py) · Issue #23687 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/23687"},{"title":"GitHub - QwenLM/Qwen3-VL: Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3-VL"},{"title":"[Feature]: Qwen3 Models GGUF Support · Issue #21511 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/21511"},{"title":"Qwen/Qwen3-ASR-0.6B · Improve model card: add Arxiv ID, library name, and language tags","url":"https://huggingface.co/Qwen/Qwen3-ASR-0.6B/discussions/2/files"},{"title":"GitHub - QwenLM/Qwen3-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-Embedding"},{"title":"Break Free from GitHub Copilot: Deploy Your Own Qwen2.5-Coder Assistant | by Wltsankalpa | Medium","url":"https://medium.com/@wltsankalpa/break-free-from-github-copilot-deploy-your-own-qwen2-5-coder-assistant-9c94153cc235"}]

Based on the search results, here's what I found about SparseSpec, PillarAttn, and their support for Qwen3 models:

## SparseSpec and PillarAttn

SparseSpec is a comprehensive framework that applies dynamic sparsification in large language model inference, achieving up to 2.13× throughput gains via its PillarAttn mechanism. The core innovation in SparseSpec is its PillarAttn mechanism, a dynamic sparse attention kernel that selects a small, adaptive subset of preceding tokens to attend to during drafting, leveraging verification-phase attention data and eliminating auxiliary forward passes and redundant KV-cache access.

## Qwen3 Model Support

On Qwen3-8B, end-to-end throughput is increased from 690 tokens/sec (baseline) to 1460 tokens/sec, and across Qwen3-1.7B, 8B, and 14B on AIME, OlympiadBench-Text, and LiveCodeBench, measured speedups are consistently in the... This indicates that SparseSpec has been tested on multiple Qwen3 model scales including 1.7B, 8B, and 14B variants.

However, the search results did not return specific information from the github.com/sspec-project repository itself, so I cannot provide details about the exact models currently supported there or their specific scale configurations. For the most up-to-date information about supported models, I recommend visiting the SparseSpec project repository directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f68104ac-3356-4446-bea0-74471fb94019",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "3d6984e8-1436-4edf-82e0-032339d8334a",
  "sourceToolAssistantUUID": "f68104ac-3356-4446-bea0-74471fb94019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T20:35:14.943Z_

<details><summary>↩ Tool result · `toolu_01Wr2BdhnFVHLR5qtbS5G3k1`</summary>

```text
Web search results for query: "Qwen3-32B GPU hours training inference benchmark experiments 2026"

Links: [{"title":"Speed Benchmark - Qwen","url":"https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3"},{"title":"Benchmarking Qwen Models Across NVIDIA GPUs (T4, L4, H100) Architectures: Inference Performance & Code Quality Analysis | by Wltsankalpa | Medium","url":"https://medium.com/@wltsankalpa/benchmarking-qwen-models-across-nvidia-gpus-t4-l4-h100-architectures-finding-your-sweet-spot-a59a0adf9043"},{"title":"Qwen/Qwen3.6-35B-A3B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-35B-A3B"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen/Qwen3-32B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-32B"},{"title":"GPU Benchmark Results | haimaker.ai","url":"https://haimaker.ai/benchmarks"}]

Based on the web search results, I found relevant information about Qwen3-32B GPU performance and benchmarks for 2026:

## Qwen3-32B Overview

Qwen3-32B-Base is the largest dense model among the Qwen3 series, and Qwen3-32B-Base performs as well as Qwen2.5-72B-Base.

## Inference Performance Benchmarks

The speed performance of bfloat16 models and quantized models (including FP8, GPTQ, AWQ) of the Qwen3 series are reported, specifically including inference speed (tokens/s) as well as memory footprint (GB) under different context lengths. Speed and memory usage are tested when generating 2048 tokens, with input lengths of 1, 6144, 14336, 30720, 63488, and 129024 tokens.

Recent 2026 benchmarking data shows the general-purpose Qwen3–32B achieved 21.7 tokens/second performance on H100 hardware.

## Training & Efficiency

Qwen3-32B-Base achieves comparable performance to Qwen2.5-72B-Base, which represents significant efficiency gains. Due to advancements in model architecture, increase in training data, and more effective training methods, the overall performance of Qwen3 dense base models matches that of Qwen2.5 base models with more parameters.

For detailed speed benchmarks and memory footprint data, the official Qwen documentation includes comprehensive results across different inference frameworks (Transformers and SGLang).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07826bd4-778e-4dc6-83d6-90ca62c6172f",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "1c33e7ab-cdfc-463f-8f8a-cccfa094fe83",
  "sourceToolAssistantUUID": "07826bd4-778e-4dc6-83d6-90ca62c6172f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T20:35:21.132Z_

<details><summary>↩ Tool result · `toolu_012xVq7zNkfN25fpck8hJ6PE`</summary>

```text
Web search results for query: "SpecAttn speculating sparse attention code release github 2025 2026"

Links: [{"title":"GitHub - thu-ml/SpargeAttn: [ICML2025] SpargeAttention: A training-free sparse attention that accelerates any model inference. · GitHub","url":"https://github.com/thu-ml/SpargeAttn"},{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641"},{"title":"[2510.27641] SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/abs/2510.27641"},{"title":"SpecAttn: Speculating Sparse Attention Harsh Shah Machine Learning Department","url":"https://openreview.net/pdf?id=5HgJc8B3j5"},{"title":"GitHub - YannX1e/Sparse-Feature-Attention: Official implement of ICLR 2026 paper \"Scaling Attention via Feature Sparsity\". · GitHub","url":"https://github.com/YannX1e/Sparse-Feature-Attention"},{"title":"SpecAttn: Speculating Sparse Attention Harsh Shah Machine Learning Department","url":"https://arxiv.org/pdf/2510.27641"},{"title":"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://www.arxiv.org/pdf/2602.07223"},{"title":"[2602.07223] SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/abs/2602.07223"},{"title":"GitHub - mit-han-lab/x-attention: [ICML 2025] XAttention: Block Sparse Attention with Antidiagonal Scoring · GitHub","url":"https://github.com/mit-han-lab/x-attention"},{"title":"GitHub - thu-ml/SageAttention: [ICLR2025, ICML2025, NeurIPS2025 Spotlight] Quantized Attention achieves speedup of 2-5x compared to FlashAttention, without losing end-to-end metrics across language, image, and video models. · GitHub","url":"https://github.com/thu-ml/SageAttention"}]

Based on the search results, here's what I found about SpecAttn and sparse attention:

## SpecAttn: Speculating Sparse Attention

SpecAttn is a novel training-free approach that seamlessly integrates with existing speculative decoding techniques to enable efficient sparse attention in pre-trained transformers. The key insight is to exploit the attention weights already computed by the draft model during speculative decoding to identify important tokens for the target model, eliminating redundant computation while maintaining output quality.

### Performance Results

SpecAttn achieves over 75% reduction in key-value cache accesses with a mere 15.29% increase in perplexity on the PG-19 dataset, significantly outperforming existing sparse attention methods. Additionally, the speedup increases as prompt length increases, with more than 4x speedup for prompt length 2048.

### Research Timeline

The original SpecAttn paper was published on arXiv on October 31, 2025. However, I also found a more recent paper titled "SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding" from February 6, 2026, which achieves 2.81x higher throughput over vanilla auto-regressive decoding and 1.29x improvement over state-of-the-art sparsity-based self-speculative decoding methods.

### Code Release

While the papers are available on arXiv, I did not find a specific GitHub repository for SpecAttn code release in these search results. The search results show other sparse attention implementations like SpargeAttn and XAttention on GitHub, but no official SpecAttn code release repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54cfa4ae-aa44-4dfd-8573-7e054542362d",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "884d5f6f-f5bd-4eb4-8651-126013b03ad6",
  "sourceToolAssistantUUID": "54cfa4ae-aa44-4dfd-8573-7e054542362d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-10T20:35:24.423Z_

Let me now fetch more detailed information on the remaining topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "884d5f6f-f5bd-4eb4-8651-126013b03ad6",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXc4byrrC7NamjwCKD5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88c0e6d6-5618-49b2-bf2b-5cd9b8b80532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HA9m9g5Vwcu3etHcTqTUu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 949,
      "cache_creation_input_tokens": 4866,
      "cache_read_input_tokens": 15642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4866,
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

_source line 33 · 2026-05-10T20:35:28.875Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K91suMBLei9abzaTzWANNq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.07223",
  "prompt": "Extract the full abstract, methodology, key results, and whether code is publicly available. How does SpecAttn co-design sparse attention with self-speculative decoding? What models and scales were tested?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88c0e6d6-5618-49b2-bf2b-5cd9b8b80532",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXc4byrrC7NamjwCKD5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64e55149-c4c8-403c-bc44-bc79a290ca9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HA9m9g5Vwcu3etHcTqTUu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 949,
      "cache_creation_input_tokens": 4866,
      "cache_read_input_tokens": 15642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4866,
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

_source line 34 · 2026-05-10T20:35:29.629Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HqZv4BCtfRewYdAxpRHDrY`</summary>

```json
{
  "url": "https://github.com/sspec-project/SparseSpec",
  "prompt": "What models does SparseSpec support? Is Qwen3-32B supported? What are the installation requirements? What is the latest commit date? Is the repository actively maintained? List all supported model architectures and sizes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64e55149-c4c8-403c-bc44-bc79a290ca9b",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXc4byrrC7NamjwCKD5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4f7fc62-a586-4050-a893-31608f064670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HA9m9g5Vwcu3etHcTqTUu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 949,
      "cache_creation_input_tokens": 4866,
      "cache_read_input_tokens": 15642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4866,
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

_source line 35 · 2026-05-10T20:35:29.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MSa1Dk3W5FvosN2sPWHzdF`</summary>

```json
{
  "query": "\"variance-bounded\" \"head-adaptive\" OR \"head-level decomposition\" speculative decoding attention 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4f7fc62-a586-4050-a893-31608f064670",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXc4byrrC7NamjwCKD5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c3ae142-1278-40c8-9fb6-eacac9bce42a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HA9m9g5Vwcu3etHcTqTUu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 949,
      "cache_creation_input_tokens": 4866,
      "cache_read_input_tokens": 15642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4866,
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

_source line 36 · 2026-05-10T20:35:30.425Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015r4WWXKC36A4vE8yF7CWKq`</summary>

```json
{
  "query": "speculative decoding 30B model GPU hours experiment cost research 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c3ae142-1278-40c8-9fb6-eacac9bce42a",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXc4byrrC7NamjwCKD5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1f83ccb-0ef7-446b-8566-55aba2886907",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HA9m9g5Vwcu3etHcTqTUu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 949,
      "cache_creation_input_tokens": 4866,
      "cache_read_input_tokens": 15642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4866,
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

_source line 37 · 2026-05-10T20:35:31.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P5N1vV9xdzYKMr1kNwZqJh`</summary>

```json
{
  "query": "attention prediction decoding self-speculative 2026 arXiv new paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1f83ccb-0ef7-446b-8566-55aba2886907",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXc4byrrC7NamjwCKD5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e87abac-252b-4d2d-ad5f-2dcd56df94ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HA9m9g5Vwcu3etHcTqTUu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 949,
      "cache_creation_input_tokens": 4866,
      "cache_read_input_tokens": 15642,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4866
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 949,
          "output_tokens": 411,
          "cache_read_input_tokens": 15642,
          "cache_creation_input_tokens": 4866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4866,
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

_source line 38 · 2026-05-10T20:35:33.870Z_

<details><summary>↩ Tool result · `toolu_01K91suMBLei9abzaTzWANNq`</summary>

```text
# SpecAttn: Analysis Based on Available Content

## Full Abstract
"Long-context large language model (LLM) inference has become the norm for today's AI applications. However, it is severely bottlenecked by the increasing memory demands of its KV cache." The paper proposes SpecAttn, which "identifies critical KV entries as a byproduct of verification and only loads these entries when drafting subsequent tokens."

## Co-Design Approach
SpecAttn integrates sparse attention with self-speculative decoding by leveraging verification as a signal for future drafting. Rather than using standalone algorithms to select key-value cache entries, the method identifies which entries matter during the verification phase and reuses this information when generating draft tokens subsequently. This creates a feedback loop where verification results guide subsequent attention patterns.

## Key Results
The method achieves:
- **2.81× throughput improvement** over standard autoregressive decoding
- **1.29× improvement** over existing sparsity-based self-speculative methods

The improvements stem from enhanced draft token acceptance rates combined with minimal overhead from KV selection.

## Models and Scales Tested
The webpage content does not specify which models, parameter sizes, or datasets were evaluated in the experiments.

## Code Availability
No information about public code release appears in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64e55149-c4c8-403c-bc44-bc79a290ca9b",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "6a4c072c-ea9a-45a0-82e1-ec4581db977a",
  "sourceToolAssistantUUID": "64e55149-c4c8-403c-bc44-bc79a290ca9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T20:35:34.399Z_

<details><summary>↩ Tool result · `toolu_01HqZv4BCtfRewYdAxpRHDrY`</summary>

```text
# SparseSpec Model and Repository Information

## Supported Models

Based on the documentation provided, SparseSpec has been evaluated on **Qwen3-1.7B, 8B, and 14B** models. The page does not mention support for Qwen3-32B or provide a comprehensive list of all supported model architectures and sizes.

## Installation Requirements

The framework requires:
- **Python 3.12** (via conda)
- **CMake 3.30.4 or higher**
- **CUDA and PyTorch** (tested with CUDA 12.9 and PyTorch 2.8.0)
- **NVIDIA H100-SXM5 GPUs** (testing environment)

Installation involves building from source with custom dependencies including FlashInfer, vLLM fork, and RAFT libraries.

## Repository Maintenance Status

The repository shows **3 total commits** and includes a disclaimer: "This repo is the proof-of-concept of our research project, which is not yet ready for production use." The latest commit date is not explicitly stated in the provided content.

## Summary

SparseSpec is a research prototype focused on reasoning model inference optimization, tested specifically on smaller Qwen3 variants. The project appears to be in active research phase rather than stable production release.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4f7fc62-a586-4050-a893-31608f064670",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "241af8f3-a992-4b70-8708-a14ed8f082a6",
  "sourceToolAssistantUUID": "e4f7fc62-a586-4050-a893-31608f064670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T20:35:37.247Z_

<details><summary>↩ Tool result · `toolu_01MSa1Dk3W5FvosN2sPWHzdF`</summary>

```text
Web search results for query: ""variance-bounded" "head-adaptive" OR "head-level decomposition" speculative decoding attention 2026"

Links: [{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"Towards Efficient LLM Inference via Collective and Adaptive Speculative Decoding | Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis","url":"https://dl.acm.org/doi/10.1145/3712285.3759834"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"},{"title":"Entropy-Driven Adaptive Decomposition and Linear-Complexity Score Attention: An AI-Powered Framework for Crude Oil Financial Market Forecasting","url":"https://www.mdpi.com/1099-4300/28/4/392"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"[2604.12247] SpecBound: Adaptive Bounded Self-Speculation with Layer-wise Confidence Calibration","url":"https://arxiv.org/abs/2604.12247"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.06932v2"},{"title":"Efficient and Scalable Speculative Decoding with Multi- ...","url":"https://aclanthology.org/2025.emnlp-main.986.pdf"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"}]

I found several relevant papers on speculative decoding and related techniques from 2026. Here are the key results:

## Recent Speculative Decoding Research (2026)

One notable paper on variational speculative decoding derives an Evidence Lower Bound (ELBO) training objective with two terms: one encouraging high-quality acceptable latent proposals and another acting as a regularizer to keep the draft policy aligned with the target distribution.

To address optimization challenges, researchers have adopted a variance-reduced gradient estimator along with Adaptive Rejection Weighting (ARW) and Confidence-Aware Regularization (CAR) mechanisms.

Another important work is SpecBound, which addresses self-draft methods in speculative decoding by proposing a framework that suppresses spurious confidence via layer-wise temperature annealing in early-exit decision and adaptively bounds speculation length based on token-wise decoding difficulty.

Additionally, Smurfs is an LLM inference system designed to accelerate LLM inference through collective and adaptive speculative decoding that adopts a majority-voted mechanism harnessing multiple SSMs to collaboratively predict LLM outputs in multi-task scenarios.

Aurora presents a unified training-serving system that reformulates speculative decoding as a joint learning-and-serving problem by connecting an SGLang-based inference server with an asynchronous training server via GPU-aware RPC to enable continuous on-policy adaptation of the draft model under live traffic.

These papers represent the cutting-edge of speculative decoding research in 2026, focusing on variance reduction, adaptive bounds, multi-model approaches, and continuous adaptation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c3ae142-1278-40c8-9fb6-eacac9bce42a",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "ced80902-976e-4845-a17c-56b67e52b7e2",
  "sourceToolAssistantUUID": "4c3ae142-1278-40c8-9fb6-eacac9bce42a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T20:35:37.268Z_

<details><summary>↩ Tool result · `toolu_015r4WWXKC36A4vE8yF7CWKq`</summary>

```text
Web search results for query: "speculative decoding 30B model GPU hours experiment cost research 2026"

Links: [{"title":"DFlash on GPU Cloud: 6x Faster LLM Inference with Block Diffusion Speculative Decoding (2026) | Spheron Blog","url":"https://www.spheron.network/blog/dflash-block-diffusion-speculative-decoding-gpu-cloud/"},{"title":"What to Buy for Local LLMs (April 2026) | by Julien Simon | Apr, 2026 | Medium","url":"https://julsimon.medium.com/what-to-buy-for-local-llms-april-2026-a4946a381a6a"},{"title":"Impact of decoding strategies on GPU energy usage in large language model text generation | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-31896-0"},{"title":"Cost Per Token Analysis: Optimizing GPU Infrastructure ... - Introl","url":"https://introl.com/blog/cost-per-token-llm-inference-optimization"},{"title":"Speculative Decoding: 2-3x Faster LLM Inference (2026)","url":"https://blog.premai.io/speculative-decoding-2-3x-faster-llm-inference-2026/"},{"title":"Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/mirror"},{"title":"SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding | Research","url":"https://research.nvidia.com/publication/2026-02_speed-bench-unified-and-diverse-benchmark-speculative-decoding"},{"title":"Looking back at speculative decoding","url":"https://research.google/blog/looking-back-at-speculative-decoding/"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"},{"title":"Performance improvements with speculative decoding in vLLM for gpt-oss | Red Hat Developer","url":"https://developers.redhat.com/articles/2026/04/16/performance-improvements-speculative-decoding-vllm-gpt-oss"}]

Based on the search results, I found relevant information about speculative decoding research and GPU costs in 2026:

## Key Findings:

**GPU Costs for 30B Model Training/Inference (2026):**

H100 at $2.50 to $3.00 per GPU-hour is adequate for 8B to 30B SFT and RL, according to an April 2026 guide on local LLM infrastructure.

**Speculative Decoding Performance & Cost Improvements:**

Standard speculative decoding with EAGLE-3 delivers 3-4x LLM throughput improvement, while DFlash gets to 6x, and does it without any quality tradeoff. The performance improvements are significant enough that speculative decoding in vLLM can significantly increase throughput without altering a model's output quality, resulting in 19% cost savings at scale for enterprise AI.

**Research Status (2025-2026):**

In 2025 and 2026, the technique went from research experiment to production standard, now built into vLLM, SGLang, TensorRT-LLM, and most serious serving frameworks. Additionally, Speculative Decoding has emerged as a critical technique for accelerating Large Language Model inference, with SD performance being inherently data-dependent, meaning diverse and representative workloads are essential for accurately measuring its effectiveness.

The search results show active research and benchmarking efforts in 2026, including NVIDIA's SPEED-Bench and various production deployments demonstrating the technique's maturity and widespread adoption.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1f83ccb-0ef7-446b-8566-55aba2886907",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "86965174-0f7f-42fb-95bd-e584262d936f",
  "sourceToolAssistantUUID": "c1f83ccb-0ef7-446b-8566-55aba2886907",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T20:35:40.206Z_

<details><summary>↩ Tool result · `toolu_01P5N1vV9xdzYKMr1kNwZqJh`</summary>

```text
Web search results for query: "attention prediction decoding self-speculative 2026 arXiv new paper"

Links: [{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"Cross-Attention Speculative Decoding Wei Zhong wei.zhong@lge.com","url":"https://www.arxiv.org/pdf/2505.24544"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"Scaling LLM Speculative Decoding: Non-Autoregressive Forecasting in Large-Batch Scenarios","url":"https://arxiv.org/html/2511.20340"},{"title":"Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/html/2605.01106"},{"title":"Cross-Attention Speculative Decoding","url":"https://arxiv.org/html/2505.24544v3"},{"title":"[2602.15318] Sparrow: Text-Anchored Window Attention with Visual-Semantic Glimpsing for Speculative Decoding in Video LLMs","url":"https://arxiv.org/abs/2602.15318"},{"title":"Speculative Speculative Decoding","url":"https://arxiv.org/html/2603.03251v2"},{"title":"Fast Inference from Transformers via Speculative Decoding","url":"https://arxiv.org/pdf/2211.17192"}]

I found several recent papers on attention prediction, decoding, and self-speculative methods from 2026. Here are the key papers:

## Recent 2026 arXiv Papers on Self-Speculative Decoding:

**1. Component-Aware Self-Speculative Decoding in Hybrid Language Models (2026)**

This paper introduces component-aware self-speculative decoding, the first method to exploit the internal architectural heterogeneity of hybrid language models, isolating the SSM/linear-attention subgraph as a zero-cost internal draft.

**2. Sparrow: Text-Anchored Window Attention for Video LLMs (February 2026)**

Sparrow proposes a framework that utilizes visually-aware text-anchored window attention via hidden state reuse to fully offload visual computation to the target model, and leverages intermediate-layer visual state bridging to train the draft model with semantic-rich intermediate states. Experiments show that Sparrow achieves an average speedup of 2.82x even with 25k visual tokens.

**3. Speculative Speculative Decoding (March 2026)**

This paper introduces speculative speculative decoding (SSD) to parallelize speculative decoding operations. While a verification is ongoing, the draft model predicts likely verification outcomes and prepares speculations pre-emptively for them.

## Earlier 2025 Papers:

**4. SparseSpec: Accelerating Large-Scale Reasoning Model Inference (December 2025)**

SparseSpec introduces a speculative decoding framework that reuses the same model as the draft and target models (i.e., self-speculation). It features a novel sparse attention mechanism, PillarAttn, as the draft model, which accurately selects critical tokens.

**5. Cross-Attention Speculative Decoding / Budget EAGLE (September 2025)**

Budget EAGLE (Beagle) is a speculative decoding method which does more accurate autoregressive predictions at inference time but utilizes multi-token parallel predictions during training to improve training efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e87abac-252b-4d2d-ad5f-2dcd56df94ae",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "22ab1693-d699-4651-8615-c6b8aca75bd6",
  "sourceToolAssistantUUID": "2e87abac-252b-4d2d-ad5f-2dcd56df94ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-10T20:35:43.874Z_

Let me now fetch additional details on SpecBound and do a few more targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22ab1693-d699-4651-8615-c6b8aca75bd6",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXdUonusZZBfdgkFToT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed03dab1-9801-422e-ae7b-9c9ac60bc6c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168bczbB8ffUKY6amZZsnQV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4882,
      "cache_read_input_tokens": 20508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4882,
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

_source line 44 · 2026-05-10T20:35:46.410Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013b6LukEpeUwkYHAB43AvBf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.12247",
  "prompt": "Extract the full abstract, methodology, and results of SpecBound. How does it use layer-wise confidence calibration? Does it do head-level or layer-level decomposition? How does it relate to variance-bounded approaches? What models were tested?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed03dab1-9801-422e-ae7b-9c9ac60bc6c4",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXdUonusZZBfdgkFToT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "156f7bbb-9622-4fdd-9f7a-70b3ebeb796b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168bczbB8ffUKY6amZZsnQV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4882,
      "cache_read_input_tokens": 20508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4882,
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

_source line 45 · 2026-05-10T20:35:51.048Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GdobNYex9SDZiR1Ju1k1CQ`</summary>

```json
{
  "query": "\"DecompSpec\" OR \"head decomposition\" self-speculative decoding variance 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "156f7bbb-9622-4fdd-9f7a-70b3ebeb796b",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXdUonusZZBfdgkFToT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "098d6514-0195-490b-b1da-3ebaeb6b6ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168bczbB8ffUKY6amZZsnQV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4882,
      "cache_read_input_tokens": 20508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4882,
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

_source line 46 · 2026-05-10T20:35:51.496Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ey47s45A1rS1Ha8TVFEUuo`</summary>

```json
{
  "query": "200 GPU hours A100 H100 speculative decoding experiments what is achievable 30B parameter model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "098d6514-0195-490b-b1da-3ebaeb6b6ff4",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXdUonusZZBfdgkFToT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13e994cb-810e-4daf-a450-c1ffe4e5aca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168bczbB8ffUKY6amZZsnQV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4882,
      "cache_read_input_tokens": 20508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4882,
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

_source line 47 · 2026-05-10T20:35:51.720Z_

<details><summary>↩ Tool result · `toolu_013b6LukEpeUwkYHAB43AvBf`</summary>

```text
# SpecBound Analysis

## Abstract
The paper proposes a self-draft framework for speculative decoding that "suppresses spurious confidence via layer-wise temperature annealing in early-exit decision and adaptively bounds speculation length based on token-wise decoding difficulty."

## Methodology

**Layer-wise Confidence Calibration:**
The approach uses temperature annealing across layers to address the problem where "shallow layers often produce overconfident yet incorrect token predictions." This mechanism helps calibrate confidence scores during early-exit decisions.

**Adaptive Bounding:**
The method "adaptively bounds speculation length based on token-wise decoding difficulty," preventing situations where difficult tokens force "redundant computation through deeper layers."

**Processing Approach:**
The technique "reprocess[es] the hidden states of draft tokens in a unified parallel pass through deep layers," maintaining exact equivalence with the original model.

## Decomposition Level
The document specifies **layer-level** calibration (not head-level). The abstract explicitly mentions "layer-wise" temperature annealing as the core mechanism.

## Results
The method achieved "up to 2.33x wall-time speedup over standard autoregressive decoding across diverse long-form generation tasks and multiple model architectures."

## Additional Details
- **No model modifications required:** The approach needs "no modifications to the base LLM parameters"
- **Variance-bounded relationships:** The abstract does not explicitly discuss variance-bounded approaches
- **Models tested:** The paper tested "multiple model architectures" but specific model names aren't detailed in this excerpt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "156f7bbb-9622-4fdd-9f7a-70b3ebeb796b",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "e7885267-832c-4777-bcac-6f5572fd0b57",
  "sourceToolAssistantUUID": "156f7bbb-9622-4fdd-9f7a-70b3ebeb796b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-10T20:35:52.268Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M4b64sb4TqkqC3GzTSidDf`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.02888",
  "prompt": "Extract all details about the staleness problem in speculative decoding. Does SpecKV address KV cache staleness, attention weight staleness, or draft-target distribution mismatch? What are the limitations discussed? What future work is proposed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7885267-832c-4777-bcac-6f5572fd0b57",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXdUonusZZBfdgkFToT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00456830-e851-4e1f-b9ce-702c8651d353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168bczbB8ffUKY6amZZsnQV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4882,
      "cache_read_input_tokens": 20508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4882,
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

_source line 49 · 2026-05-10T20:35:57.502Z_

<details><summary>↩ Tool result · `toolu_01M4b64sb4TqkqC3GzTSidDf`</summary>

```text
# SpecKV and the Staleness Problem in Speculative Decoding

Based on the paper content provided, **SpecKV does not address KV cache staleness, attention weight staleness, or draft-target distribution mismatch**. These fundamental staleness issues are not discussed in this work.

## What SpecKV Actually Addresses

SpecKV focuses exclusively on selecting the speculation length (γ) adaptively. The paper identifies that "the optimal γ varies across task types and...depends on the compression level applied to the target model." The system uses draft model signals—entropy and confidence—to predict acceptance rates and choose γ dynamically.

## Limitations Explicitly Acknowledged

The authors identify four key limitations:

1. **Model scale**: Testing limited to 1B/3B pairs; larger models (8B/70B) not evaluated
2. **Prompt diversity**: Only 20 prompts across 4 categories versus established benchmarks with hundreds
3. **Evaluation methodology**: Predictor-based simulation rather than live inference measurements
4. **Compression scope**: Weight quantization only; KV cache eviction and attention sparsification excluded

## Future Work Proposed

The paper outlines five research directions:

- Scaling to larger model pairs and comprehensive benchmarks
- End-to-end integration into HuggingFace generation pipelines
- **Extending to KV cache compression** techniques explicitly
- Online adaptation via Thompson Sampling and contextual bandits
- Production integration with vLLM/SGLang

The staleness problem remains an open research frontier not addressed by SpecKV's current scope.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00456830-e851-4e1f-b9ce-702c8651d353",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "dcd5d8e7-30d8-40fc-9b1a-0c66add72735",
  "sourceToolAssistantUUID": "00456830-e851-4e1f-b9ce-702c8651d353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T20:35:59.597Z_

<details><summary>↩ Tool result · `toolu_01GdobNYex9SDZiR1Ju1k1CQ`</summary>

```text
Web search results for query: ""DecompSpec" OR "head decomposition" self-speculative decoding variance 2026"

Links: [{"title":"Speculative Decoding Explained | Data Processing Club","url":"https://data-processing.club/speculative/"},{"title":"SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification","url":"https://arxiv.org/html/2512.02337v1"},{"title":"SpecPV: Improving Self-Speculative Decoding for Long- ...","url":"https://www.arxiv.org/pdf/2512.02337"},{"title":"DSDE: Dynamic Speculative Decoding with KLD Stability for Real-World Serving","url":"https://arxiv.org/html/2509.01083v1"},{"title":"A Hitchhiker’s Guide to Speculative Decoding – PyTorch","url":"https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/"},{"title":"Dynamic Speculation Lookahead Accelerates Speculative Decoding of Large Language Models","url":"https://arxiv.org/html/2405.04304v5"},{"title":"Visual Decoding Operators: Towards a Compositional Theory of Visualization Perception","url":"https://arxiv.org/html/2604.02220"},{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"},{"title":"[2510.04147] Self Speculative Decoding for Diffusion Large Language Models","url":"https://arxiv.org/abs/2510.04147"},{"title":"GitHub - dilab-zju/self-speculative-decoding: Code associated with the paper **Draft & Verify: Lossless Large Language Model Acceleration via Self-Speculative Decoding**","url":"https://github.com/dilab-zju/self-speculative-decoding"}]

Based on the search results, I found relevant information about self-speculative decoding and variance-related techniques, though I didn't find a specific paper titled "DecompSpec." Here's what I discovered:

## Self-Speculative Decoding and Variance

SpecPV is a self-speculative decoding approach that performs fast verification using partial key–value states (KV) and periodically applies full verification to eliminate accumulated errors. This addresses variance issues in long-context generation.

## Head Decomposition in Speculative Decoding

Multi-head designs assign each head to a specific future position, whereas single-head approaches repeatedly apply one prediction head in an autoregressive manner. Medusa adds additional heads to the final hidden layer of a pre-trained language model: one head predicts the token two steps ahead, another predicts three steps ahead, and so on, up to a head predicting the token K steps ahead. These heads are trained via self-distillation so that they predict the outputs of the base model.

## Variance in Speculation Length

Research has found that variance is a significant issue in speculative decoding. High variance of oracle speculation length (SL) values has been observed. Additionally, the variance of KLD (Kullback-Leibler divergence) reflects regional stability and provides guidance for speculation length adaptation, indicating whether the current generation phase is predictable or difficult.

If you're looking for a specific paper on "DecompSpec," it may be a very recent preprint or may be known by a different title. Would you like me to search with different keywords?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "098d6514-0195-490b-b1da-3ebaeb6b6ff4",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "bad8a135-bff0-457a-a81b-9431f43104ac",
  "sourceToolAssistantUUID": "098d6514-0195-490b-b1da-3ebaeb6b6ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-10T20:36:00.404Z_

<details><summary>↩ Tool result · `toolu_01Ey47s45A1rS1Ha8TVFEUuo`</summary>

```text
Web search results for query: "200 GPU hours A100 H100 speculative decoding experiments what is achievable 30B parameter model"

Links: [{"title":"NVIDIA A100 vs H100 vs H200: GPU Comparison for AI | E2E Networks","url":"https://www.e2enetworks.com/blog/nvidia-a100-vs-h100-vs-h200-gpu-comparison"},{"title":"Speculative decoding |","url":"https://scale-ml.org/posts/speculative-decoding.html"},{"title":"Nvidia H100 GPU: Specs, VRAM, Price, and AI Performance","url":"https://www.runpod.io/articles/guides/nvidia-h100"},{"title":"DFlash on GPU Cloud: 6x Faster LLM Inference with Block Diffusion Speculative Decoding (2026) | Spheron Blog","url":"https://www.spheron.network/blog/dflash-block-diffusion-speculative-decoding-gpu-cloud/"},{"title":"NVIDIA H100 Price Guide 2026: GPU Costs, Cloud Pricing & Buy vs Rent | Jarvis Labs Blog | Jarvis Labs","url":"https://jarvislabs.ai/blog/h100-price"},{"title":"GPU Cloud Pricing: A100 vs H100 vs H200 Compared","url":"https://www.gmicloud.ai/en/blog/gpu-cloud-pricing-a100-h100-h200"},{"title":"NVIDIA A100 TENSOR CORE GPU | DATA SHEET | Jun21 | 1","url":"https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf"},{"title":"LLM Inference Optimization: Cut Costs & Boost Speed","url":"https://www.gmicloud.ai/en/blog/how-to-scale-llm-inference-without-breaking-your-budget"},{"title":"NVIDIA Data Center GPUs Explained: From A100 to B200 and Beyond","url":"https://www.bentoml.com/blog/nvidia-data-center-gpus-explained-a100-h200-b200-and-beyond"},{"title":"Benchmarking Large Language Models on NVIDIA H100 GPUs with CoreWeave (Part 1) | Databricks Blog","url":"https://www.databricks.com/blog/coreweave-nvidia-h100-part-1"}]

Based on the search results, I found relevant information about what's achievable with speculative decoding experiments on A100/H100 GPUs with 30B parameter models:

## Key Findings:

**GPU Capability for 30B Models:**
For small models under 30B parameters, H100 delivers excellent performance at a reasonable price. H100 is suitable if your model fits comfortably in 80GB with room for KV cache, which covers most models under 30B parameters and many 30-70B models with FP8 quantization.

**Speculative Decoding Performance:**
Speculative decoding accelerates token generation by 2-2.5x without sacrificing output quality, with effectiveness determined by acceptance rate: at α ≥ 0.6 with 5 speculative tokens, you'll see 2-3x speedups over baseline. Additionally, DFlash (an advanced speculative decoding technique) turns a single H100 rental hour into the equivalent of six hours of standard inference throughput.

**Training Cost Context:**
For reference on what 200 GPU hours might accomplish, medium models (13-30B parameters) typically cost $500-$3,000 using 4 H100s for 50-200 hours.

**H100 vs A100:**
The H100 delivers roughly 3-4x better performance on transformer workloads via FP8 and the Transformer Engine. This means A100s would require more time for equivalent results.

The search results focus primarily on inference optimization and general GPU capabilities rather than specific experimental results on training speculative decoding models, so I wasn't able to find detailed benchmarks of what's specifically achievable with 200 GPU hours of experimentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13e994cb-810e-4daf-a450-c1ffe4e5aca8",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "07a14f69-d520-4ee1-8223-35edc13d214c",
  "sourceToolAssistantUUID": "13e994cb-810e-4daf-a450-c1ffe4e5aca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-10T20:36:05.583Z_

Let me get a few more pieces of information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07a14f69-d520-4ee1-8223-35edc13d214c",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXexZgHRLUQKKAZ1uUf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24f983b9-dec6-4fa5-9469-45d3fd888100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186BmhXbC7kccYssSBTpbf6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 392,
      "cache_creation_input_tokens": 2806,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2806,
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

_source line 53 · 2026-05-10T20:36:06.563Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NkNyoWXtTypFH4XJnRaVsL`</summary>

```json
{
  "query": "SPEED-Bench NVIDIA speculative decoding benchmark 2026 GPU hours experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24f983b9-dec6-4fa5-9469-45d3fd888100",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXexZgHRLUQKKAZ1uUf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69848119-70ca-4877-8606-bcdfe1c15bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186BmhXbC7kccYssSBTpbf6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 392,
      "cache_creation_input_tokens": 2806,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2806,
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

_source line 54 · 2026-05-10T20:36:07.162Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TzAHpKbFfNRUx5iu2UtK2n`</summary>

```json
{
  "query": "speculative decoding head-level attention sparsity per-head adaptive draft 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69848119-70ca-4877-8606-bcdfe1c15bae",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXexZgHRLUQKKAZ1uUf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69a68186-316d-419d-a9a4-bba904828ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186BmhXbC7kccYssSBTpbf6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 392,
      "cache_creation_input_tokens": 2806,
      "cache_read_input_tokens": 25390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2806,
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

_source line 55 · 2026-05-10T20:36:09.904Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YaTWbnBGsGPLD3gDUqYbLF`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.01106",
  "prompt": "Explain in detail: How does component-aware self-speculative decoding differ from head-level decomposition? Does it discuss attention head importance, head pruning, or per-head sparsity? What is the relationship between component-level and head-level granularity? Does it cite or discuss any head-adaptive or head-level methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69a68186-316d-419d-a9a4-bba904828ea3",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXexZgHRLUQKKAZ1uUf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2c0e5e0-50c6-4997-83eb-b039822924d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186BmhXbC7kccYssSBTpbf6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 392,
      "cache_creation_input_tokens": 2806,
      "cache_read_input_tokens": 25390,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2806
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 392,
          "output_tokens": 273,
          "cache_read_input_tokens": 25390,
          "cache_creation_input_tokens": 2806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2806,
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

_source line 56 · 2026-05-10T20:36:12.590Z_

<details><summary>↩ Tool result · `toolu_01NkNyoWXtTypFH4XJnRaVsL`</summary>

```text
Web search results for query: "SPEED-Bench NVIDIA speculative decoding benchmark 2026 GPU hours experiments"

Links: [{"title":"SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding | Research","url":"https://research.nvidia.com/publication/2026-02_speed-bench-unified-and-diverse-benchmark-speculative-decoding"},{"title":"Introducing SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding","url":"https://huggingface.co/blog/nvidia/speed-bench"},{"title":"Speculative Decoding: Performance or Illusion? | SpecDecode-Bench","url":"https://specdecode-bench.github.io/"},{"title":"Benchmarking LLM Performance on Different GPUs in 2026 · Technical news about AI, coding and all","url":"https://dasroot.net/posts/2026/04/benchmarking-llm-performance-gpus-2026/"},{"title":"[2604.09557] SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding","url":"https://arxiv.org/abs/2604.09557"},{"title":"NVIDIA Blackwell Raises Bar in New InferenceMAX Benchmarks, Delivering Unmatched Performance and Lowest Cost Per Token","url":"https://blogs.nvidia.com/blog/blackwell-inferencemax-benchmark-results/"},{"title":"Spec-Bench","url":"https://sites.google.com/view/spec-bench"},{"title":"Tokens Per Second: LLM Speed Benchmark Guide (2026) | Morph","url":"https://www.morphllm.com/tokens-per-second"},{"title":"Scaling Up, Speeding Up: A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling | OpenReview","url":"https://openreview.net/forum?id=DjOmnwX4wJ"},{"title":"SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding","url":"https://arxiv.org/html/2604.09557"}]

Based on my search results, here's what I found about SPEED-Bench, the NVIDIA speculative decoding benchmark:

## Overview

SPEED-Bench is a comprehensive suite designed to standardize speculative decoding (SD) evaluation across diverse semantic domains and realistic serving regimes. The paper was submitted on February 10, 2026, and was published as a community article on March 19, 2026.

## Benchmark Structure

SPEED-Bench offers a carefully curated qualitative data split, selected by prioritizing semantic diversity across the data samples. The Throughput Split includes data aggregated and processed into fixed Input Sequence Length (ISL) buckets (1k-32k) across three domain difficulties, supporting large batch sizes (up to 512 per ISL and difficulty).

## GPU Experiments

All experiments used a single NVIDIA B200 GPU, except for DeepSeek and Qwen models inference and GPT-OSS EAGLE3 training, which used eight.

## Models Tested

The experiments target large, modern open models: Llama 3.3 70B, GPT-OSS 120B, Qwen3 235B, Qwen3-Next, and DeepSeek R1.

## Integration with Production Systems

By integrating with production engines like vLLM and TensorRT-LLM, SPEED-Bench allows practitioners to analyze system behaviors often masked by other benchmarks.

The benchmark addresses key gaps in existing speculative decoding evaluations, particularly regarding realistic batch sizes and long context lengths.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69848119-70ca-4877-8606-bcdfe1c15bae",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "26641c1c-6804-4460-ba23-fad47d262ebb",
  "sourceToolAssistantUUID": "69848119-70ca-4877-8606-bcdfe1c15bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-10T20:36:14.268Z_

<details><summary>↩ Tool result · `toolu_01TzAHpKbFfNRUx5iu2UtK2n`</summary>

```text
Web search results for query: "speculative decoding head-level attention sparsity per-head adaptive draft 2026"

Links: [{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"Make Every Draft Count: Hidden State based Speculative Decoding","url":"https://arxiv.org/html/2602.21224v1"},{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00735/128189/OPT-Tree-Speculative-Decoding-with-Adaptive-Draft"},{"title":"Acceptance Dynamics Across Cognitive Domains in Speculative Decoding","url":"https://arxiv.org/html/2604.14682"},{"title":"Efficient and Scalable Speculative Decoding with Multi- ...","url":"https://aclanthology.org/2025.emnlp-main.986.pdf"},{"title":"Speculative Decoding with CTC-based Draft Model for LLM Inference Acceleration","url":"https://arxiv.org/html/2412.00061v1"},{"title":"GitHub - smart-lty/ParallelSpeculativeDecoding: [ICLR 2025] PEARL: Parallel Speculative Decoding with Adaptive Draft Length · GitHub","url":"https://github.com/smart-lty/parallelspeculativedecoding"}]

I found several relevant results about speculative decoding and related optimization techniques from 2025-2026. Here's what the search revealed:

## Key Recent Research (2026)

Variational Speculative Decoding (VSD) includes components like adaptive rejection weighting and confidence-aware regularization, with methods like GRIFFIN+VSD and HASS+VSD achieving consistent performance gains.

Recent work on hidden state-based speculative decoding (Lyanna) proposes draft model adaptation through next hidden state prediction, token-info injected sampling, and techniques for efficient token information integration.

## Attention Sparsity and Speculative Decoding

SpecAttn is a training-free approach that integrates with existing speculative decoding techniques to enable efficient sparse attention in pre-trained transformers. The approach leverages attention patterns computed by draft models during speculative execution for dynamic, content-aware key-value cache pruning.

## Adaptive Draft Mechanisms

EAGLE-3 attaches a lightweight drafting component called an "EAGLE head" to the internal layers of the target model, and this process is instance-adaptive where the head evaluates its own confidence and stops drafting if confidence drops below a threshold.

PEARL (Parallel Speculative Decoding with Adaptive Draft Length) was published at ICLR 2025, suggesting adaptive draft mechanisms remain an active area of research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69a68186-316d-419d-a9a4-bba904828ea3",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "bc14d2ed-d821-49c8-8181-680095c8b5da",
  "sourceToolAssistantUUID": "69a68186-316d-419d-a9a4-bba904828ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T20:36:14.985Z_

<details><summary>↩ Tool result · `toolu_01YaTWbnBGsGPLD3gDUqYbLF`</summary>

```text
# Component-Aware vs. Head-Level Decomposition

## Key Distinction

Component-aware self-speculative decoding operates at the **architectural pathway level**, not the head level. The paper isolates entire SSM or linear-attention components—processing whole pathways through the network—rather than examining individual attention heads.

## What the Paper Actually Addresses

The method works with two integration patterns:

**Parallel hybrids**: "both components process the same input and their outputs are summed" across complete layers, not individual heads.

**Sequential hybrids**: entire layers alternate between component types, creating "disjoint sets" of linear and attention layers across the network.

## No Head-Level Analysis

The paper contains **no discussion of**:
- Attention head importance or ranking
- Head pruning or removal strategies
- Per-head sparsity patterns
- Head-adaptive methods

## Granularity Difference

The distinction is fundamental:
- **Component-level**: removes entire attention pathways (which contain multiple heads)
- **Head-level**: would remove individual attention mechanisms within a layer

The paper's finding that sequential hybrids fail (α=0.038) stems from breaking the **layer-interleaving pattern**, not from head-level redundancy. This architectural mismatch differs entirely from head pruning approaches, which typically assume heads within a layer can be evaluated independently.

No prior head-focused methods are cited or compared.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2c0e5e0-50c6-4997-83eb-b039822924d9",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "447e9d7b-c6eb-47ef-a63f-18b4b0c813a4",
  "sourceToolAssistantUUID": "e2c0e5e0-50c6-4997-83eb-b039822924d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-10T20:36:18.325Z_

Now let me get a final set of targeted searches for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "447e9d7b-c6eb-47ef-a63f-18b4b0c813a4",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXg2utvVPktD9TcN8Mr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51dd8b37-d980-4f77-9b71-0d5d8275c93a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDfFNtALhc5ZR9YCUDHZDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2822,
      "cache_read_input_tokens": 28196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2822,
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

_source line 60 · 2026-05-10T20:36:19.314Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LmayftDpFYk6c75ES9qper`</summary>

```json
{
  "query": "SpecAttn arxiv 2602.07223 code github release models tested Llama Qwen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51dd8b37-d980-4f77-9b71-0d5d8275c93a",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXg2utvVPktD9TcN8Mr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b428401-b10b-4b17-b83a-b09bb9eeea1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDfFNtALhc5ZR9YCUDHZDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2822,
      "cache_read_input_tokens": 28196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2822,
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

_source line 61 · 2026-05-10T20:36:20.467Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ULfzKFNstnPSqg9Fec6m7J`</summary>

```json
{
  "query": "speculative decoding research 200 GPU hours budget feasibility ablation experiments academic 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b428401-b10b-4b17-b83a-b09bb9eeea1d",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXg2utvVPktD9TcN8Mr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae5104c2-ec8c-49ad-b8d7-164d69f6ae3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDfFNtALhc5ZR9YCUDHZDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2822,
      "cache_read_input_tokens": 28196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2822,
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

_source line 62 · 2026-05-10T20:36:22.594Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015xPjvr9ZvqH8Kt4cASav9H`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.09557",
  "prompt": "Extract details about GPU hours used for experiments, computational budget, how many GPU hours are needed for speculative decoding experiments on 30B+ models. What models were tested and how long did experiments take?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae5104c2-ec8c-49ad-b8d7-164d69f6ae3a",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXg2utvVPktD9TcN8Mr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8def3ea-653e-4694-a37d-54684dbfffed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDfFNtALhc5ZR9YCUDHZDi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2822,
      "cache_read_input_tokens": 28196,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2822
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 28196,
          "cache_creation_input_tokens": 2822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2822,
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

_source line 63 · 2026-05-10T20:36:25.365Z_

<details><summary>↩ Tool result · `toolu_015xPjvr9ZvqH8Kt4cASav9H`</summary>

```text
Based on the provided webpage content, I cannot extract specific details about GPU hours, computational budget, or experiment duration.

The abstract mentions that SPEED-Bench "integrates with production engines like vLLM and TensorRT-LLM" and discusses evaluating speculative decoding across various scenarios, but it does not disclose:

- Exact GPU hours consumed
- Computational budget information
- Duration of experiments
- Specific models tested (beyond the general reference to "30B+ models")
- Time requirements for running experiments

The webpage is an arXiv abstract page that provides only a high-level overview. These computational details would typically be found in the full paper itself, which is not included in the content provided. To obtain this information, you would need to access the complete PDF or HTML version of the paper linked on this page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8def3ea-653e-4694-a37d-54684dbfffed",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "659abb49-0219-4a69-9f31-615f6c928cd1",
  "sourceToolAssistantUUID": "f8def3ea-653e-4694-a37d-54684dbfffed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-10T20:36:27.114Z_

<details><summary>↩ Tool result · `toolu_01ULfzKFNstnPSqg9Fec6m7J`</summary>

```text
Web search results for query: "speculative decoding research 200 GPU hours budget feasibility ablation experiments academic 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"A CPU/GPU Heterogeneous Speculative Decoding for LLM ...","url":"https://aclanthology.org/2025.emnlp-main.879.pdf"},{"title":"BATCH SPECULATIVE DECODING DONE RIGHT","url":"https://openreview.net/pdf/c146854abff466edc531f707b9f9fd646814e687.pdf"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"Efficient LLM System with Speculative Decoding | EECS at UC Berkeley","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-224.html"},{"title":"SEQUOIA: Scalable and Robust Speculative Decoding Zhuoming Chen1∗Avner May2∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/ea1f5f0878d43ff4fb8bf64ef4a2326c-Paper-Conference.pdf"},{"title":"SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding | Research","url":"https://research.nvidia.com/publication/2026-02_speed-bench-unified-and-diverse-benchmark-speculative-decoding"},{"title":"Performance improvements with speculative decoding in vLLM for gpt-oss | Red Hat Developer","url":"https://developers.redhat.com/articles/2026/04/16/performance-improvements-speculative-decoding-vllm-gpt-oss"},{"title":"Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/mirror"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"}]

I've completed the web search for speculative decoding research with considerations around GPU hours budget, feasibility, and ablation experiments from 2025-2026. Here are the key findings:

## Recent Speculative Decoding Research (2025-2026)

The search results reveal active research in speculative decoding with recent academic work:

**Published Conference Papers:**
- A paper published at ICLR 2026 on speculative decoding techniques that references low-latency speculators and critical batch size analysis
- Research on batch speculative decoding that examines both sequence verification and tree verification paradigms

**System Design and Ablation Studies:**
- Extensive end-to-end experiments and ablation studies demonstrating effectiveness of SEQUOIA, a scalable speculative decoding approach
- Ablation studies showing that tree structures can generate up to 33% more tokens per decoding step compared to independent sequences

**Feasibility and Performance:**
- Research spanning algorithmic design, empirical characterization, and production-grade control mechanisms, noting that speculative decoding exhibits variable performance depending sensitively on workload characteristics, batch sizes, model configurations, and system conditions
- Implementations achieving speedups such as up to 4.04× for Llama2-7B on a single A100 GPU

**Practical Implementation:**
- Benchmarks demonstrating consistent throughput and latency improvements across varying concurrency levels, datasets, tensor-parallelism settings, and draft-token budgets

The research suggests that while speculative decoding is feasible with modern GPU resources, performance optimization requires careful consideration of multiple system parameters and extensive empirical validation through ablation studies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae5104c2-ec8c-49ad-b8d7-164d69f6ae3a",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "7150d14f-0f0f-47a5-96e7-661599f6ebec",
  "sourceToolAssistantUUID": "ae5104c2-ec8c-49ad-b8d7-164d69f6ae3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-10T20:36:34.441Z_

<details><summary>↩ Tool result · `toolu_01LmayftDpFYk6c75ES9qper`</summary>

```text
Web search results for query: "SpecAttn arxiv 2602.07223 code github release models tested Llama Qwen"

Links: [{"title":"[2602.07223] SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/abs/2602.07223"},{"title":"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/html/2602.07223"},{"title":"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://www.arxiv.org/pdf/2602.07223"},{"title":"GitHub - YuzeHao2023/daily-arxiv-ai4math: 🎓Automatically Update AI4math Papers Daily using Github Actions","url":"https://github.com/YuzeHao2023/daily-arxiv-ai4math"},{"title":"GitHub - UltraClr/agent-arxiv-daily: 🎓Automatically Update Agents Papers Daily using Github Actions","url":"https://github.com/UltraClr/agent-arxiv-daily"},{"title":"[2602.09185] AIDev: Studying AI Coding Agents on GitHub","url":"https://arxiv.org/abs/2602.09185"},{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641v1"},{"title":"[2602.00180] Spec-Driven Development:From Code to Contract in the Age of AI Coding Assistants","url":"https://arxiv.org/abs/2602.00180"},{"title":"[2510.27641] SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/abs/2510.27641"},{"title":"[2602.09892v1] Immersion in the GitHub Universe: Scaling Coding Agents to Mastery","url":"https://arxiv.org/abs/2602.09892v1"}]

Now let me search more specifically for information about the GitHub repository and models tested:

Links: [{"title":"Qwen3.5 & Qwen3.6 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html"},{"title":"Supported Models - vLLM","url":"https://docs.vllm.ai/en/latest/models/supported_models/"},{"title":"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/html/2602.07223"},{"title":"vLLM - Qwen","url":"https://qwen.readthedocs.io/en/latest/deployment/vllm.html"},{"title":"Supported Models — vLLM","url":"https://docs.vllm.ai/en/v0.6.2/models/supported_models.html"},{"title":"List of Supported Models — vLLM","url":"https://docs.vllm.ai/en/v0.7.0/models/supported_models.html"},{"title":"GitHub - hiyouga/LlamaFactory: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) · GitHub","url":"https://github.com/hiyouga/LlamaFactory"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen2.5: A Party of Foundation Models! | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5/"},{"title":"Model Providers | Qwen Code Docs","url":"https://qwenlm.github.io/qwen-code-docs/en/users/configuration/model-providers/"}]

Let me search specifically for the GitHub repository of SpecAttn:

Links: [{"title":"[2602.07223] SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/abs/2602.07223"},{"title":"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/html/2602.07223"},{"title":"Releases · github/spec-kit","url":"https://github.com/github/spec-kit/releases"},{"title":"Releases · panaversity/spec-kit-plus","url":"https://github.com/panaversity/spec-kit-plus/releases"},{"title":"Issues · github/spec-kit","url":"https://github.com/github/spec-kit/issues"},{"title":"Installation Guide | Spec Kit Documentation","url":"https://github.github.com/spec-kit/installation.html"},{"title":"Releases · anomalyco/opencode","url":"https://github.com/anomalyco/opencode/releases"},{"title":"spec-kit/spec-driven.md at main · github/spec-kit","url":"https://github.com/github/spec-kit/blob/main/spec-driven.md"},{"title":"The ONLY guide you'll need for GitHub Spec Kit - YouTube","url":"https://www.youtube.com/watch?v=a9eR1xsfvHg"},{"title":"What's The Deal With GitHub Spec Kit · Den Delimarsky","url":"https://den.dev/blog/github-spec-kit/"}]

Let me search with a different approach to find the SpecAttn code repository:

No links found.

Let me try another search approach:

Links: [{"title":"GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub","url":"https://github.com/vllm-project/vllm"},{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"vLLM · GitHub","url":"https://github.com/vllm-project"},{"title":"GitHub - vllm-project/speculators: A unified library for building, evaluating, and storing speculative decoding algorithms for LLM inference in vLLM · GitHub","url":"https://github.com/vllm-project/speculators"},{"title":"GitHub - Wenyueh/MinivLLM: Based on Nano-vLLM, a simple replication of vLLM with self-contained paged attention and flash attention implementation · GitHub","url":"https://github.com/Wenyueh/MinivLLM"},{"title":"GitHub - vllm-project/vllm-omni: A framework for efficient model inference with omni-modality models · GitHub","url":"https://github.com/vllm-project/vllm-omni"},{"title":"[New Model]: YuE · Issue #12658 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/12658"},{"title":"GitHub - vllm-project/vllm-ascend: Community maintained hardware plugin for vLLM on Ascend · GitHub","url":"https://github.com/vllm-project/vllm-ascend"},{"title":"[RFC]: Automate Speculative Decoding · Issue #4565 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/4565"},{"title":"vLLM Docs · GitHub","url":"https://gist.github.com/rbiswasfc/678e4c78258480dcb6214efeedbe5af8"}]

Based on my search results, I can provide you with the information found about SpecAttn arxiv 2602.07223:

## SpecAttn Paper Information (arxiv 2602.07223)

SpecAttn is a paper titled "Co-Designing Sparse Attention with Self-Speculative Decoding" submitted on February 6, 2026, authored by Yikang Yue, Yuqi Xue, and Jian Huang.

### What SpecAttn Does

SpecAttn is a self-speculative decoding method with verification-guided sparse attention that identifies critical KV entries as a byproduct of verification and only loads these entries when drafting subsequent tokens, improving draft token acceptance rate while incurring low KV selection overhead, thereby improving decoding throughput.

### Implementation and Models Tested

SpecAttn is implemented within vLLM as a training-free, plug-and-play solution, and evaluated using diverse LLMs including Qwen3 families and gpt-oss-20b with different content lengths.

### Performance Results

SpecAttn achieves 2.81× higher throughput over vanilla auto-regressive decoding and 1.29× improvement over state-of-the-art sparsity-based self-speculative decoding methods.

### GitHub Code Repository

Unfortunately, based on my search results, I could not find a specific public GitHub repository for the SpecAttn implementation. While the paper states that SpecAttn is implemented within vLLM using custom hooks that dynamically dispatch the correct attention kernel, a standalone release repository does not appear in the search results. You may need to contact the authors directly or check the paper's supplementary materials for access to the code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b428401-b10b-4b17-b83a-b09bb9eeea1d",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "287eca58-d76e-4dcf-9b14-02e82259278f",
  "sourceToolAssistantUUID": "4b428401-b10b-4b17-b83a-b09bb9eeea1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-10T20:36:39.765Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DpAa2HjghTzufG7rDZDuEd`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.07223",
  "prompt": "Extract: 1) Which specific models are tested (exact model names and sizes)? 2) Is code publicly available or planned for release? 3) How does SpecAttn select which attention heads or KV entries to keep? 4) What GPU resources were used for experiments? 5) Does it discuss head-level adaptive sparsity?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "287eca58-d76e-4dcf-9b14-02e82259278f",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXhU4WYCJUKgW6FRANR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0fabf6b-e608-4c53-877c-3fe2cfd7eedb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQPTyYddGSKRxSj5gVgJcX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1230,
      "cache_creation_input_tokens": 2639,
      "cache_read_input_tokens": 31018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-10T20:36:41.396Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K1ixuSShPViVqAtcEG3Kap`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.09557",
  "prompt": "Extract: 1) What GPU hours were used for the experiments? 2) What models were benchmarked (names, sizes)? 3) How many GPUs and for how long were experiments run? 4) What is the computational cost of running speculative decoding experiments on 30B+ models?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0fabf6b-e608-4c53-877c-3fe2cfd7eedb",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXhU4WYCJUKgW6FRANR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f342616e-e631-4e77-8a8b-c3568c2ea742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQPTyYddGSKRxSj5gVgJcX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1230,
      "cache_creation_input_tokens": 2639,
      "cache_read_input_tokens": 31018,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2639
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1230,
          "output_tokens": 288,
          "cache_read_input_tokens": 31018,
          "cache_creation_input_tokens": 2639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2639,
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

_source line 68 · 2026-05-10T20:36:44.980Z_

<details><summary>↩ Tool result · `toolu_01DpAa2HjghTzufG7rDZDuEd`</summary>

```text
# SpecAttn Research Paper - Key Findings

## 1. Models Tested
The paper evaluates four specific models: **Qwen3-4B, Qwen3-8B, Qwen3-30B-A3B-Thinking-2507-FP8, and gpt-oss-20b**. For the latter, "MXFP4 quantization" was applied to mixture-of-expert weights.

## 2. Code Availability
The authors commit to open-sourcing their work: "We will open-source SpecAttn as a drop-in patch to vLLM."

## 3. KV Entry Selection Mechanism
SpecAttn employs a sophisticated aggregation approach. Rather than selecting based on individual tokens, it identifies critical KV entries by "maximizing the coverage of attention weights across all draft tokens." Specifically, the method collects attention logits from the first and last draft tokens, then "select[s] the k tokens with the highest scores" based on averaged criticality metrics across attention heads.

## 4. Hardware Configuration
Experiments utilized "two NVIDIA H100 NVL GPUs (94 GB)" for all testing.

## 5. Head-Level Adaptive Sparsity
The paper does not discuss head-level adaptive sparsity. Selection occurs uniformly across all attention heads through averaging: "average this result across all query heads (h) to obtain a criticality score for each prefix token."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0fabf6b-e608-4c53-877c-3fe2cfd7eedb",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "7482dc60-1e45-40e7-a3fd-7eefe283099c",
  "sourceToolAssistantUUID": "e0fabf6b-e608-4c53-877c-3fe2cfd7eedb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-10T20:36:46.652Z_

<details><summary>↩ Tool result · `toolu_01K1ixuSShPViVqAtcEG3Kap`</summary>

```text
# GPU Hours and Computational Costs in SPEED-Bench

## Hardware Used

The paper documents experiments conducted on **NVIDIA B200 GPUs**. Most evaluations used a single B200, though "DeepSeek and Qwen models inference and GPT-OSS EAGLE3 training, which used eight" GPUs.

## Benchmarked Models

The study evaluated multiple large language models:

- **Llama 3.3 70B**
- **GPT-OSS 120B**
- **Qwen3 235B**
- **Qwen3-Next 80B**
- **DeepSeek R1**

For drafting, smaller models were paired with targets (e.g., Llama 3.2 1B with Llama 3.3 70B).

## Training Configuration Details

For EAGLE3 model training, researchers "sample 500k training samples" and "train on 8xB200 GPUs with an effective training batch size of 128," running for 3 epochs. However, the document does not provide explicit total GPU-hours calculations.

## Computational Cost Limitations

The paper lacks comprehensive disclosure of aggregate GPU hours or precise cost estimates. While detailing individual experimental setups, it does not quantify the total computational expense for benchmarking 30B+ models across diverse scenarios—a notable gap for reproducibility and accessibility assessment in the benchmarking literature.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f342616e-e631-4e77-8a8b-c3568c2ea742",
  "isSidechain": true,
  "promptId": "4832393a-ca5c-48ea-93ec-515ca9501e3d",
  "agentId": "a25188ca95bace647",
  "type": "user",
  "uuid": "2cbd6138-ed55-4964-8d61-4447d2353c5a",
  "sourceToolAssistantUUID": "f342616e-e631-4e77-8a8b-c3568c2ea742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-10T20:38:03.385Z_

I now have comprehensive data across all six areas. Here is the full report.

---

## Comprehensive Report: Self-Speculative Decoding & Sparse Attention Landscape (March-May 2026)

---

### 1. New Concurrent Work (April-May 2026)

I found several papers from this window that could overlap with or inform the DecompSpec idea (variance-bounded head-adaptive decomposition for self-speculative decoding):

**Directly relevant / potentially overlapping:**

- **Component-Aware Self-Speculative Decoding** (arXiv:2605.01106, May 2026) -- exploits SSM/attention heterogeneity in hybrid models. Operates at the *component level* (entire SSM vs. attention pathways), **not** head level. Does not discuss head importance, head pruning, or per-head sparsity at all. This is orthogonal to DecompSpec: it requires hybrid architectures (Falcon-H1, Qwen3.5) while DecompSpec targets standard Transformers via head-level decomposition.

- **SpecBound: Adaptive Bounded Self-Speculation with Layer-wise Confidence Calibration** (arXiv:2604.12247, April 2026) -- uses layer-wise temperature annealing for early-exit calibration and adaptively bounds speculation length per token difficulty. Achieves 2.33x speedup. This is *layer-level*, not head-level, so it doesn't directly compete with head-adaptive decomposition, but the adaptive bounding of speculation length based on difficulty is conceptually related to variance-bounded approaches.

- **SpecAttn v2: Co-Designing Sparse Attention with Self-Speculative Decoding** (arXiv:2602.07223, February 2026) -- the most relevant competitor. Integrates sparse attention directly into self-speculative decoding by using verification-phase attention weights to guide KV entry selection during drafting. Achieves 2.81x throughput over autoregressive and 1.29x over SOTA sparse self-speculation. Crucially, it averages attention scores **across all heads** (uniform treatment), and does **not** do per-head adaptive sparsity. This leaves a clear gap for DecompSpec's head-adaptive approach.

- **Speculative Speculative Decoding / Saguaro** (arXiv:2603.03251, March 2026, ICLR 2026) -- parallelizes draft and verification stages. 30% faster than optimized speculative decoding, up to 5x vs. autoregressive. Orthogonal to DecompSpec (focuses on pipeline parallelism, not attention decomposition).

**No paper found matching "DecompSpec" or "variance-bounded head-adaptive decomposition"** -- this specific idea appears to have no direct competitor as of May 2026. The niche of per-head variance-bounded attention decomposition for self-speculation remains open.

---

### 2. Component-Aware Self-Speculative Decoding (arXiv:2605.01106)

**How it works:** Isolates the SSM/linear-attention subgraph within hybrid LMs as a "zero-cost internal draft." The full model (with attention layers) serves as verifier.

**Key results:**
- Parallel hybrids (Falcon-H1: Mamba-2 + attention per layer): acceptance rate alpha=0.68 at k=2
- Sequential hybrids (Qwen3.5: interleaved linear/attention layers): alpha=0.038 -- an 18x gap
- Tested on Falcon-H1 0.5B/3B and Qwen3.5

**How it differs from head-level decomposition:**
- Operates at the **architectural pathway level** -- removes entire attention pathways (containing all heads), not individual heads
- Contains **zero discussion** of attention head importance, head pruning, or per-head sparsity
- Requires hybrid architectures; inapplicable to standard dense Transformers
- The failure of sequential hybrids stems from breaking layer interleaving, not head-level redundancy

**Implication for DecompSpec:** Non-overlapping. Component-aware decomposition is restricted to hybrid models. DecompSpec's head-level approach applies to standard Transformer architectures (Llama, Qwen dense models), which is a much larger model family.

---

### 3. SpecKV (arXiv:2605.02888)

**What it does:** A lightweight MLP controller that adaptively selects speculation length (gamma) per step using draft model entropy and confidence as signals. Achieves 56% improvement in expected tokens/step over fixed gamma=4 with only 0.34ms overhead.

**Does it address the staleness problem?** **No.** The paper explicitly does not address KV cache staleness, attention weight staleness, or draft-target distribution mismatch. It focuses solely on speculation length optimization.

**Limitations acknowledged:**
1. Tested only on 1B/3B model pairs (no large models)
2. Only 20 prompts across 4 categories
3. Predictor-based simulation, not live inference
4. Only weight quantization tested; KV cache eviction and attention sparsification excluded

**Future work:** Extending to KV cache compression techniques is listed as explicit future work, suggesting staleness-aware approaches remain an open direction.

---

### 4. SparseSpec Codebase

**Repository:** `github.com/sspec-project/SparseSpec`

**Status:** Research prototype. Only 3 total commits. The repo explicitly states: "This repo is the proof-of-concept of our research project, which is not yet ready for production use."

**Supported models:** Tested on **Qwen3-1.7B, 8B, and 14B** only. On Qwen3-8B, throughput increased from 690 to 1460 tokens/sec.

**Can it scale to Qwen3-32B?** Not currently. The largest tested model is Qwen3-14B. The codebase is a proof-of-concept built on a custom vLLM fork requiring:
- Python 3.12, CUDA 12.9, PyTorch 2.8.0
- NVIDIA H100-SXM5 GPUs
- Custom FlashInfer and RAFT library builds

Scaling to 32B would require: (a) multi-GPU support validation, (b) memory management for the larger KV cache, and (c) PillarAttn tuning for the 32B architecture. Given the prototype nature (3 commits), significant engineering effort would be needed.

---

### 5. SpecAttn Codebase

**Two versions exist:**
1. **SpecAttn v1** (arXiv:2510.27641, October 2025) -- training-free sparse attention via draft model attention reuse. No public code repository found.
2. **SpecAttn v2** (arXiv:2602.07223, February 2026) -- co-designs sparse attention with self-speculative decoding. Implemented as custom hooks within vLLM. Authors state: **"We will open-source SpecAttn as a drop-in patch to vLLM."** No public repo is available yet.

**Models tested (v2):** Qwen3-4B, Qwen3-8B, Qwen3-30B-A3B-Thinking-2507-FP8, and gpt-oss-20b.

**Hardware:** Two NVIDIA H100 NVL GPUs (94 GB each).

**Key technical detail:** SpecAttn selects KV entries by averaging attention scores **uniformly across all heads** -- it does not do per-head adaptive sparsity. This is a clear differentiation point for DecompSpec.

---

### 6. Timeline Benchmarks: What's Realistic for 200 GPU-Hours?

**Reference points from recent papers:**

| Paper/System | Hardware | Models | Experiment Scale |
|---|---|---|---|
| SPEED-Bench (NVIDIA) | 1-8x B200 | Llama 3.3 70B, GPT-OSS 120B, Qwen3 235B | EAGLE3 training: 500k samples, 3 epochs, 8xB200 |
| SpecAttn v2 | 2x H100 NVL | Up to Qwen3-30B-A3B | Full evaluation suite |
| SparseSpec | H100-SXM5 | Up to Qwen3-14B | Proof-of-concept |
| SpecKV | Not specified | 1B/3B pairs | 5,112 step-level records |

**Cost context (2026 rates):**
- H100: ~$2.50-$3.00/GPU-hour
- 200 GPU-hours = ~$500-$600
- This is described as adequate for "8B to 30B SFT and RL" experiments

**What 200 H100 GPU-hours can realistically cover for Qwen3-32B:**
- **Inference-only experiments** (speculative decoding evaluation across benchmarks): Comfortably feasible. SpecAttn evaluated Qwen3-30B-A3B on 2 H100s -- 200 GPU-hours provides ~100 hours of wall-clock on 2 GPUs, ample for comprehensive benchmark sweeps.
- **Lightweight training** (e.g., training an EAGLE head or small predictor MLP): Feasible. EAGLE3 training used 500k samples on 8xB200 for 3 epochs -- this is likely under 50 GPU-hours.
- **Full ablation study** (multiple attention configurations, multiple datasets, multiple gamma settings): Tight but feasible if experiments are well-designed. Budget for ~25 H100-hours per major ablation axis, giving ~8 major experimental conditions.
- **Full model fine-tuning at 32B scale:** Not feasible within 200 GPU-hours. SFT of a 32B model typically requires 500+ GPU-hours for meaningful training.

**Bottom line:** 200 GPU-hours is sufficient for a research paper's worth of *inference experiments and lightweight component training* on Qwen3-32B, but not for full model fine-tuning.

---

### Summary of Key Findings for DecompSpec Positioning

1. **No direct competitor exists** for variance-bounded head-adaptive decomposition as of May 2026
2. Component-Aware (2605.01106) works at pathway level in hybrid models -- orthogonal to head-level work
3. SpecAttn v2 is the closest competitor but explicitly uses **uniform** head averaging, leaving the per-head adaptive niche open
4. SpecBound does layer-wise adaptive bounding but not head-level
5. The staleness problem remains **unaddressed** by SpecKV and other recent work
6. SparseSpec cannot currently scale to Qwen3-32B (max tested: 14B, only 3 commits)
7. SpecAttn code is not yet released but is promised as a vLLM patch
8. 200 GPU-hours on H100 is realistic for inference experiments and lightweight predictor training on Qwen3-32B, but not for full fine-tuning

Sources:
- [Component-Aware Self-Speculative Decoding (2605.01106)](https://arxiv.org/abs/2605.01106)
- [SpecKV: Adaptive Speculative Decoding (2605.02888)](https://arxiv.org/abs/2605.02888)
- [Speculative Speculative Decoding / Saguaro (2603.03251)](https://arxiv.org/abs/2603.03251)
- [SpecBound (2604.12247)](https://arxiv.org/abs/2604.12247)
- [SpecAttn v1 (2510.27641)](https://arxiv.org/abs/2510.27641)
- [SpecAttn v2: Co-Designing Sparse Attention (2602.07223)](https://arxiv.org/abs/2602.07223)
- [SparseSpec / PillarAttn (2512.01278)](https://arxiv.org/abs/2512.01278)
- [SPEED-Bench (2604.09557)](https://arxiv.org/abs/2604.09557)
- [SparseSpec GitHub Repository](https://github.com/sspec-project/SparseSpec)
- [Speculative Decoding Papers Collection](https://github.com/hemingkx/SpeculativeDecodingPapers)
- [SPEED-Bench NVIDIA Research Page](https://research.nvidia.com/publication/2026-02_speed-bench-unified-and-diverse-benchmark-speculative-decoding)
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)
- [SpargeAttn GitHub](https://github.com/thu-ml/SpargeAttn)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cbd6138-ed55-4964-8d61-4447d2353c5a",
  "isSidechain": true,
  "agentId": "a25188ca95bace647",
  "requestId": "req_011CauXiNLVdj1nymEL88sF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c59b31cd-a057-4b96-8eb8-c0104a1e9dd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "86b75a6b-0ce3-4d89-8017-2931beba1ea5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjhVcHZz3WfgcCgoPhaSkm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2336,
      "cache_read_input_tokens": 33657,
      "output_tokens": 3124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2336
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3124,
          "cache_read_input_tokens": 33657,
          "cache_creation_input_tokens": 2336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2336,
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
