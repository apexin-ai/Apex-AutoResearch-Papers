# Research conversation: I need to verify the paper "Quantization Dominates Rank Reduction for KV-Cache Compression" (arXiv:2604.11501, April 202

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6c887de685b0dd66.jsonl`
- **Structured JSON:** [`87f8f2c8457d1cd1cfc1.json`](../../sessions/87/87f8f2c8457d1cd1cfc1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-11T23:31:27.994Z_

I need to verify the paper "Quantization Dominates Rank Reduction for KV-Cache Compression" (arXiv:2604.11501, April 2026).

Specifically:
1. Does this paper exist on arXiv?
2. Does it show that quantization outperforms PCA-based rank reduction at matched storage budgets?
3. Does it test dimension-discarding projection (not decorrelation-before-quantization as KVTC uses)?
4. What are the specific findings about hybrid baselines (e.g., Rank-64 + INT8)?
5. Does it address transform coding approaches like KVTC, or only rank-reducing projection?

Also search for any other recent work (2025-2026) that challenges or validates PCA-based KV cache compression approaches. 

Use WebSearch for "Quantization Dominates Rank Reduction KV Cache arXiv 2604.11501" and fetch the paper. Under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "a6c887de685b0dd66",
  "type": "user",
  "uuid": "a80dcc9f-b5d2-4dfb-a367-e173e2ac3ae1",
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

_source line 2 · 2026-05-11T23:31:27.996Z_

```json
{
  "parentUuid": "a80dcc9f-b5d2-4dfb-a367-e173e2ac3ae1",
  "isSidechain": true,
  "agentId": "a6c887de685b0dd66",
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
  "uuid": "2dcb2894-df65-481e-be63-1dcbf67b059c",
  "timestamp": "2026-05-11T23:31:27.996Z",
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

_source line 3 · 2026-05-11T23:31:36.014Z_



I'll search for this paper and related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dcb2894-df65-481e-be63-1dcbf67b059c",
  "isSidechain": true,
  "agentId": "a6c887de685b0dd66",
  "requestId": "req_011CawequfvWUX6BzD784uUT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88aa0b24-1848-4bcc-bba8-bbdc0edd86e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019h3YctEc4Xbk39SxLKN3LN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 775,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:31:36.462Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Mhr7cGMBAZKWohi3RYE1kG`</summary>

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
  "parentUuid": "88aa0b24-1848-4bcc-bba8-bbdc0edd86e7",
  "isSidechain": true,
  "agentId": "a6c887de685b0dd66",
  "requestId": "req_011CawequfvWUX6BzD784uUT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa85f9b8-60d7-4381-803f-974469d16a90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019h3YctEc4Xbk39SxLKN3LN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 775,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-11T23:31:36.466Z_

<details><summary>↩ Tool result · `toolu_01Mhr7cGMBAZKWohi3RYE1kG`</summary>

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
  "parentUuid": "aa85f9b8-60d7-4381-803f-974469d16a90",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "a6c887de685b0dd66",
  "type": "user",
  "uuid": "2cccb696-eede-4f50-b2ae-f60b62791f8b",
  "sourceToolAssistantUUID": "aa85f9b8-60d7-4381-803f-974469d16a90",
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

_source line 6 · 2026-05-11T23:31:41.638Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E4Gfn67VRtkE8vfR51bWhx`</summary>

```json
{
  "query": "Quantization Dominates Rank Reduction KV Cache arXiv 2604.11501"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cccb696-eede-4f50-b2ae-f60b62791f8b",
  "isSidechain": true,
  "agentId": "a6c887de685b0dd66",
  "requestId": "req_011CawerYdR8UFJejxhVmajC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a531f5a3-e116-417f-8991-9860f2fcbc20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExQPZn3pSMGnw8QuJmJkMV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8998,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 8998,
          "cache_creation_input_tokens": 1900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1900,
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

_source line 7 · 2026-05-11T23:31:41.647Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012GxXLPprWtt5EQiSkFw95B`</summary>

```json
{
  "query": "PCA KV cache compression quantization 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a531f5a3-e116-417f-8991-9860f2fcbc20",
  "isSidechain": true,
  "agentId": "a6c887de685b0dd66",
  "requestId": "req_011CawerYdR8UFJejxhVmajC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d636e3b-dca1-4e97-8dae-6e27ce0388fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExQPZn3pSMGnw8QuJmJkMV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8998,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 8998,
          "cache_creation_input_tokens": 1900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1900,
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

_source line 8 · 2026-05-11T23:31:49.639Z_

<details><summary>↩ Tool result · `toolu_01E4Gfn67VRtkE8vfR51bWhx`</summary>

```text
Web search results for query: "Quantization Dominates Rank Reduction KV Cache arXiv 2604.11501"

Links: [{"title":"[2604.11501] Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/abs/2604.11501"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"},{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722"},{"title":"KVLinC: KV Cache Quantization with Hadamard Rotation and Linear Correction","url":"https://arxiv.org/html/2510.05373v1"},{"title":"XQuant: Breaking the Memory Wall for LLM Inference with KV Cache Rematerialization","url":"https://arxiv.org/html/2508.10395v1"},{"title":"KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study","url":"https://arxiv.org/html/2603.27469v1"},{"title":"[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/abs/2605.06675"},{"title":"WindowQuant: Mixed-Precision KV Cache Quantization based on Window-Level Similarity for VLMs Inference Optimization","url":"https://arxiv.org/html/2605.02262v1"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Quantization Dominates Rank Reduction for KV-Cache Compression"

**arXiv ID:** 2604.11501

**Key Findings:**

The paper compares two strategies for compressing the KV cache in transformer inference: rank reduction (discard dimensions) and quantization (keep all dimensions, reduce precision). At matched storage budgets across five models (124M–14B, MHA and GQA), they find that quantization consistently outperforms rank reduction—by 4–364 PPL depending on model and compression level.

The gap traces to a structural asymmetry: under softmax attention routing, removing a dimension can flip which token is attended (a discrete failure), while quantization noise is bounded and typically preserves score ordering.

**Performance Results:**

Joint K+V INT4 quantization achieves 75% total KV reduction at only +0.18 PPL on Mistral 7B. On LAMBADA, INT4 matches FP16 accuracy (+0.23 PPL on Mistral 7B, +0.58 on GPT-2) while rank-32 at identical storage collapses to 0.4%.

The paper was published on April 13, 2026, by Samuel M.A. Salfati from fraQtl AI Research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a531f5a3-e116-417f-8991-9860f2fcbc20",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "a6c887de685b0dd66",
  "type": "user",
  "uuid": "50c5c438-acec-473a-a944-997dc6cfbdde",
  "sourceToolAssistantUUID": "a531f5a3-e116-417f-8991-9860f2fcbc20",
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

_source line 9 · 2026-05-11T23:31:50.877Z_

<details><summary>↩ Tool result · `toolu_012GxXLPprWtt5EQiSkFw95B`</summary>

```text
Web search results for query: "PCA KV cache compression quantization 2025 2026 arXiv"

Links: [{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"},{"title":"GitHub - OnlyTerp/kvtc: First open-source KVTC implementation (NVIDIA, ICLR 2026) -- 8-32x KV cache compression via PCA + adaptive quantization + entropy coding · GitHub","url":"https://github.com/OnlyTerp/kvtc"},{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"},{"title":"KV Cache Transform Coding for Compact Storage in LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251101815S/abstract"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"},{"title":"[2511.01815] KV Cache Transform Coding for Compact Storage in LLM Inference","url":"https://arxiv.org/abs/2511.01815"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"Mixed-Dimension Budget Allocation for Efficient KV Cache ...","url":"https://arxiv.org/pdf/2603.20616"},{"title":"KV Cache Transform Coding for Compact Storage in LLM Inference","url":"https://arxiv.org/pdf/2511.01815"},{"title":"KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study","url":"https://arxiv.org/html/2603.27469v1"}]

Based on the search results, here are the recent papers on PCA KV cache compression and quantization from 2025-2026:

## Key Recent Papers:

### 1. **KVTC: KV Cache Transform Coding** (NVIDIA, Accepted to ICLR 2026)
KVTC combines PCA-based feature decorrelation, adaptive quantization, and entropy coding. KVTC achieves up to 20× compression while maintaining reasoning and long-context accuracy, and 40× or higher for specific use cases. The paper was published to arXiv in November 2025 (arXiv:2511.01815) and accepted to ICLR 2026.

### 2. **Quantization Dominates Rank Reduction for KV-Cache Compression**
In every setting tested, quantization outperforms rank reduction at matched storage, with INT4 achieving near-lossless compression (+0.23 PPL on Mistral 7B at 75% reduction), while rank-32 at identical storage loses 34.77 PPL.

### 3. **eOptShrinkQ: Near-Lossless KV Cache Compression**
eOptShrinkQ combines optimal singular value shrinkage (eOptShrink) to automatically extract shared structure, and the residual is quantized by TurboQuant, a per-vector scalar quantizer with near-optimal distortion guarantees.

### 4. **Don't Waste Bits! Adaptive KV-Cache Quantization** 
This work proposes adaptive KV-cache quantization, a learned policy that assigns bit-width proportional to token importance, minimizing expected memory and latency without sacrificing competitive accuracy.

These papers represent the current frontier of research combining PCA-based feature extraction with quantization techniques for efficient KV cache compression in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d636e3b-dca1-4e97-8dae-6e27ce0388fb",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "a6c887de685b0dd66",
  "type": "user",
  "uuid": "b48dff6d-c707-495f-8a8e-05f2434d72d3",
  "sourceToolAssistantUUID": "3d636e3b-dca1-4e97-8dae-6e27ce0388fb",
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

_source line 10 · 2026-05-11T23:31:58.156Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M3Qnuar1fKfeTFiFzvmXYb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.11501",
  "prompt": "Extract: (1) Does it test dimension-discarding projection specifically, or decorrelation-before-quantization like KVTC? (2) What are the exact findings about hybrid baselines like Rank-64 + INT8? (3) Does it address transform coding approaches like KVTC, or only rank-reducing projection? (4) List the exact models and datasets tested. (5) Who are the authors?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b48dff6d-c707-495f-8a8e-05f2434d72d3",
  "isSidechain": true,
  "agentId": "a6c887de685b0dd66",
  "requestId": "req_011CawesbV6AZP6GCZwD2FS3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b9ea6ed-48bb-48f6-8854-ad11b8e0f755",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrbq9bBnPYEkCxK5CAAaeJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1993,
      "cache_read_input_tokens": 10898,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1993
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 10898,
          "cache_creation_input_tokens": 1993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1993,
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

_source line 11 · 2026-05-11T23:32:02.505Z_

<details><summary>↩ Tool result · `toolu_01M3Qnuar1fKfeTFiFzvmXYb`</summary>

```text
# Findings from "Quantization Dominates Rank Reduction for KV-Cache Compression"

**(1) Dimension-discarding projection vs. decorrelation:**
The paper focuses on "rank reduction (discard dimensions)" versus quantization approaches. The abstract does not mention KVTC or decorrelation-before-quantization strategies specifically.

**(2) Hybrid baseline findings:**
The research shows that "the gap persists even when rank reduction is combined with quantization in hybrid baselines." However, specific INT8+Rank-64 results are not detailed in this excerpt.

**(3) Transform coding approaches:**
The abstract does not address KVTC or other transform coding methods. The comparison centers narrowly on dimension-reduction versus precision-reduction techniques.

**(4) Models and datasets tested:**
- **Models:** Five models ranging from 124M-14B parameters, including both Multi-Head Attention (MHA) and Grouped Query Attention (GQA) variants, with specific mentions of Mistral 7B and GPT-2
- **Datasets:** LAMBADA is explicitly referenced for evaluation

**(5) Author:**
Samuel Salfati is the sole author listed for this submission (arXiv:2604.11501, submitted April 13, 2026).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b9ea6ed-48bb-48f6-8854-ad11b8e0f755",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "a6c887de685b0dd66",
  "type": "user",
  "uuid": "ffec1048-051b-4aad-8670-a710d6f03453",
  "sourceToolAssistantUUID": "3b9ea6ed-48bb-48f6-8854-ad11b8e0f755",
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

_source line 12 · 2026-05-11T23:32:07.049Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JdJmamCadNuDHpZMjXSqaa`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.11501",
  "prompt": "Extract the following specific details: (1) The exact hybrid baseline results, especially Rank-64 + INT8 numbers. (2) Does the paper discuss or cite KVTC (KV Cache Transform Coding) or decorrelation-based approaches? (3) What exactly is the rank reduction method used -- is it PCA projection that discards dimensions, or something else? (4) Any limitations the authors acknowledge about their comparison scope."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffec1048-051b-4aad-8670-a710d6f03453",
  "isSidechain": true,
  "agentId": "a6c887de685b0dd66",
  "requestId": "req_011CawetTD3a85P26eSER5Uw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09a3279b-3ac2-4eb3-931a-cdc48eadffb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QePx272QsMQwGMHDu5MfAT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 12891,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 12891,
          "cache_creation_input_tokens": 479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 479,
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

_source line 13 · 2026-05-11T23:32:13.837Z_

<details><summary>↩ Tool result · `toolu_01JdJmamCadNuDHpZMjXSqaa`</summary>

```text
# Analysis of Paper Details

## (1) Hybrid Baseline Results

The paper presents hybrid baseline results in **Table 2**. At matched 512-bit budget on Mistral 7B:

- Full INT4 (128 dims): **9.42 PPL**
- Rank-64 INT8: **13.06 PPL**
- Rank-32 FP16: **44.19 PPL**

The authors conclude: "Even Rank-64 INT8 fails to match full INT4 at the same budget." On Qwen 14B at identical storage, the pattern holds (INT4: 7.23 vs Rank-64 INT8: 13.90).

## (2) KVTC or Decorrelation-Based Methods

The paper does **not mention KVTC** or other decorrelation-based compression approaches. The related work section (Section 2) covers KV-cache quantization, low-rank compression, sensitivity-weighted methods, and token eviction, but makes no reference to transform coding methods.

## (3) Rank Reduction Method

The rank reduction approach used is **standard projection-based dimensionality reduction**. The paper states: "Projection V^=V P P^⊤ where P = top-r eigenvectors." This involves computing eigenbasis vectors and discarding lower-ranked directions, effectively reducing the dimension space while keeping precision at FP16.

## (4) Acknowledged Limitations

The authors explicitly list scope limitations:

- "Five models up to 14B; larger models untested"
- "LAMBADA on two models only"
- "No wall-clock latency" measurements (acknowledging that rank reduction saves attention compute while quantization saves bandwidth)
- Testing restricted to INT8/INT4 quantization levels
- Results specific to KV-cache compression during inference
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09a3279b-3ac2-4eb3-931a-cdc48eadffb0",
  "isSidechain": true,
  "promptId": "41385595-bf7a-4f64-9964-72fa610f10c5",
  "agentId": "a6c887de685b0dd66",
  "type": "user",
  "uuid": "612f81e1-a421-4748-9ab1-feecb45c875e",
  "sourceToolAssistantUUID": "09a3279b-3ac2-4eb3-931a-cdc48eadffb0",
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

_source line 14 · 2026-05-11T23:32:33.227Z_

Here are the findings:

**1. Existence:** Yes, arXiv:2604.11501 exists. Published April 13, 2026, sole author Samuel Salfati (fraQtl AI Research).

**2. Quantization vs. PCA rank reduction:** Yes. At matched storage budgets across five models (124M--14B), quantization consistently wins by 4--364 PPL. On Mistral 7B, INT4 (75% reduction) costs only +0.18 PPL; rank-32 at identical storage collapses (+34.77 PPL).

**3. Dimension-discarding projection only:** Yes. The paper tests standard eigenbasis projection that discards low-ranked dimensions (V_hat = V P P^T, P = top-r eigenvectors). It does **not** test decorrelation-before-quantization as KVTC uses -- the comparison is narrower than it may appear.

**4. Hybrid baselines (Table 2, Mistral 7B, 512-bit budget):**
- Full INT4 (128 dims): **9.42 PPL**
- Rank-64 + INT8: **13.06 PPL**
- Rank-32 FP16: **44.19 PPL**

The gap persists on Qwen 14B (INT4: 7.23 vs Rank-64+INT8: 13.90). Hybrids help over pure rank reduction but never match pure quantization.

**5. KVTC / transform coding:** **Not addressed.** The paper cites quantization, low-rank, sensitivity-weighted, and token eviction work, but makes no reference to KVTC or any decorrelation+quantization pipeline. Its conclusions apply to naive dimension-discarding projection, not to the decorrelate-then-quantize paradigm.

**Related recent work (2025--2026):**
- **KVTC** (NVIDIA, ICLR 2026, arXiv:2511.01815): PCA decorrelation + adaptive quantization + entropy coding; 20--40x compression with maintained accuracy -- a fundamentally different approach than what 2604.11501 tests against.
- **eOptShrinkQ** (arXiv:2605.02905): Optimal spectral denoising + per-vector quantization.
- **RateQuant** (arXiv:2605.06675): Rate-distortion-optimal mixed-precision KV quantization.

**Bottom line:** The paper's core claim (quantization beats rank reduction) is well-supported for the narrow comparison it makes, but it does not test or refute transform-coding approaches like KVTC that decorrelate before quantizing.

Sources:
- [Quantization Dominates Rank Reduction for KV-Cache Compression (abstract)](https://arxiv.org/abs/2604.11501)
- [Quantization Dominates Rank Reduction for KV-Cache Compression (HTML)](https://arxiv.org/html/2604.11501)
- [KVTC: KV Cache Transform Coding (arXiv:2511.01815)](https://arxiv.org/abs/2511.01815)
- [eOptShrinkQ (arXiv:2605.02905)](https://arxiv.org/html/2605.02905)
- [RateQuant (arXiv:2605.06675)](https://arxiv.org/abs/2605.06675)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "612f81e1-a421-4748-9ab1-feecb45c875e",
  "isSidechain": true,
  "agentId": "a6c887de685b0dd66",
  "requestId": "req_011CaweuHequdE6B1AVqpUEu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "796d5716-6735-418d-b16f-c3e9450d8ee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8991f2e9-0486-40fc-bb52-57bc0fc68af2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SaYpBjtQwdETckZ2KCVbMG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 611,
      "cache_read_input_tokens": 13370,
      "output_tokens": 829,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 611
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 829,
          "cache_read_input_tokens": 13370,
          "cache_creation_input_tokens": 611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 611,
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
