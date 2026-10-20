# Research conversation: I need to deeply research the paper "TAPPA" (arXiv:2601.21709, ICLR 2026). This paper is from the same group as Attentio

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a32e859e0d4ccdd85.jsonl`
- **Structured JSON:** [`cdaa44a9052d39cce766.json`](../../sessions/cd/cdaa44a9052d39cce766.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-10T21:01:55.727Z_

I need to deeply research the paper "TAPPA" (arXiv:2601.21709, ICLR 2026). This paper is from the same group as AttentionPredictor and provides a theoretical framework classifying attention patterns as "predictable" vs "unpredictable" based on query self-similarity along the temporal dimension.

Please do the following:
1. Use WebFetch to read the paper at https://arxiv.org/abs/2601.21709 — get the abstract and key claims
2. Use WebFetch to read the full paper at https://arxiv.org/html/2601.21709 or https://arxiv.org/pdf/2601.21709 focusing on:
   - Their definition of "predictable" vs "unpredictable" attention patterns
   - The query self-similarity metric they use
   - Their theoretical framework / theorems
   - How they classify heads
   - What models and benchmarks they evaluate on
   - Their relationship to AttentionPredictor
   - Any connection to MRL (mean resultant length) or directional statistics
3. Search for "TAPPA attention prediction ICLR 2026" and "TAPPA temporal attention pattern" to find any additional context

The context: I'm working on DecompSpec, which classifies attention heads as "structural" (high MRL, analytically predictable via trigonometric rotation) vs "content-dependent" (low MRL, needs explicit residual tracking). TAPPA's predictable/unpredictable classification may be directly related to my structural/content-dependent classification. I need to understand:
- Is TAPPA's "predictable" the same concept as my "structural"?
- Does TAPPA provide error bounds similar to my MSE bound?
- How should I position DecompSpec relative to TAPPA?

Report findings in detail with exact quotes from the abstract and key results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "291c0c26-92d0-489d-996f-3b77581c0bda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T21:01:55.732Z_

```json
{
  "parentUuid": "291c0c26-92d0-489d-996f-3b77581c0bda",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
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
  "uuid": "9e1bc8b2-dbdf-4f72-94b1-8a8c89687d64",
  "timestamp": "2026-05-10T21:01:55.732Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T21:01:58.827Z_



I'll start by loading the WebFetch and WebSearch tool schemas, then fetch the paper and search for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e1bc8b2-dbdf-4f72-94b1-8a8c89687d64",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZdcFW5YqGW6ypjuANN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a57522f-5912-4986-8aa4-47e82790fcf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8Q7nHXycdyrfzZzgXN9c9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 981,
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

_source line 4 · 2026-05-10T21:01:58.937Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AMtfb8dM5ZiuYjhb4FSoz9`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a57522f-5912-4986-8aa4-47e82790fcf1",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZdcFW5YqGW6ypjuANN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e28bc56-6df4-4552-8c9f-0856751e759a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8Q7nHXycdyrfzZzgXN9c9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 8223,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 981
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 981,
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

_source line 5 · 2026-05-10T21:01:58.941Z_

<details><summary>↩ Tool result · `toolu_01AMtfb8dM5ZiuYjhb4FSoz9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "1e28bc56-6df4-4552-8c9f-0856751e759a",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "8b452541-bfe9-42ee-8cec-7545e1939ba7",
  "sourceToolAssistantUUID": "1e28bc56-6df4-4552-8c9f-0856751e759a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T21:02:01.325Z_



Now let me fetch the paper and run searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b452541-bfe9-42ee-8cec-7545e1939ba7",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZdrAAbEqKqgaC6w7u8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbd126b7-b206-4c3e-aa57-4bab6dbd977d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Nab1cSXK8Keg3UTVbiW8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 7 · 2026-05-10T21:02:03.215Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016Q1oA88597KvKw7vmSWAjt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.21709",
  "prompt": "Extract the complete abstract, title, authors, and any key claims or contributions listed on this page. Include all text verbatim from the abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbd126b7-b206-4c3e-aa57-4bab6dbd977d",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZdrAAbEqKqgaC6w7u8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "919d114c-96c5-4e26-8c39-3c6cd5642690",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Nab1cSXK8Keg3UTVbiW8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 8 · 2026-05-10T21:02:07.516Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AvePxnavBsoMwtm6e2LNdc`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.21709",
  "prompt": "Extract ALL detailed content from this paper, focusing especially on:\n1. The complete abstract\n2. Their definition of \"predictable\" vs \"unpredictable\" attention patterns\n3. The query self-similarity metric they use (exact mathematical definition)\n4. Their theoretical framework, theorems, and proofs (include theorem statements verbatim)\n5. How they classify attention heads\n6. What models and benchmarks they evaluate on\n7. Their relationship to AttentionPredictor\n8. Any connection to MRL (mean resultant length) or directional statistics\n9. Error bounds they provide\n10. Key results and tables\nInclude exact quotes wherever possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "919d114c-96c5-4e26-8c39-3c6cd5642690",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZdrAAbEqKqgaC6w7u8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da1d4ed2-9c5d-4833-9fa7-ab9eb0c5e2e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Nab1cSXK8Keg3UTVbiW8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 9 · 2026-05-10T21:02:08.038Z_

<details><summary>↩ Tool result · `toolu_016Q1oA88597KvKw7vmSWAjt`</summary>

```text
# Paper Summary

**Title:** Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis

**Authors:** Qingyue Yang, Jie Wang, Xing Li, Yinqi Bai, Xialiang Tong, Huiling Zhen, Jianye Hao, Mingxuan Yuan, Bin Li

**Abstract:**
The researchers introduce TAPPA (Temporal Attention Pattern Predictability Analysis), a framework explaining diverse attention patterns through temporally continuous mathematical analysis. They categorize patterns as either "predictable patterns with clear regularities" or those appearing "effectively random," attributing this distinction to query self-similarity along the temporal dimension. The work provides detailed mathematical analysis of three representative cases involving queries, keys, and Rotary Positional Embeddings. 

**Key Contributions:**
- A unifying theoretical framework for understanding attention behavior in large language models
- Distinction between predictable and unpredictable attention patterns based on query self-similarity
- Mathematical analysis of representative attention pattern cases
- Practical applications demonstrating improved performance in KV cache compression and LLM pruning tasks
- Open-source code availability

**Venue:** ICLR 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "919d114c-96c5-4e26-8c39-3c6cd5642690",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "f9027095-5735-472f-8fd9-8521f9b4a807",
  "sourceToolAssistantUUID": "919d114c-96c5-4e26-8c39-3c6cd5642690",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T21:02:08.513Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JZ4CNDEzVXSwtAETmG6cj5`</summary>

```json
{
  "query": "TAPPA attention prediction ICLR 2026 arxiv 2601.21709"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9027095-5735-472f-8fd9-8521f9b4a807",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZdrAAbEqKqgaC6w7u8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12a88170-7d4f-4b6a-80ec-2ecfe534a4da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Nab1cSXK8Keg3UTVbiW8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 11 · 2026-05-10T21:02:08.725Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019wojVpeiaV3mfcmSiZBpm6`</summary>

```json
{
  "query": "TAPPA temporal attention pattern predictable unpredictable transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12a88170-7d4f-4b6a-80ec-2ecfe534a4da",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZdrAAbEqKqgaC6w7u8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e52db1c8-abee-4d01-a0f2-aa1f790223b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7Nab1cSXK8Keg3UTVbiW8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9204,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 435,
          "cache_read_input_tokens": 9204,
          "cache_creation_input_tokens": 1915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1915,
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

_source line 12 · 2026-05-10T21:02:14.179Z_

<details><summary>↩ Tool result · `toolu_01JZ4CNDEzVXSwtAETmG6cj5`</summary>

```text
Web search results for query: "TAPPA attention prediction ICLR 2026 arxiv 2601.21709"

Links: [{"title":"[2601.21709] Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis","url":"https://arxiv.org/abs/2601.21709"},{"title":"Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis","url":"https://arxiv.org/html/2601.21709"},{"title":"Published as a conference paper at ICLR 2026 WHY ATTENTION PATTERNS EXIST:","url":"https://arxiv.org/pdf/2601.21709"},{"title":"[2601.00919] Attention Needs to Focus: A Unified Perspective on Attention Allocation","url":"https://arxiv.org/abs/2601.00919"},{"title":"PAtt: A Pattern Attention Network for ETA Prediction Using Historical Speed Profiles","url":"https://arxiv.org/html/2601.13793"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"[2601.01818] Robust Egocentric Visual Attention Prediction Through Language-guided Scene Context-aware Learning","url":"https://arxiv.org/abs/2601.01818"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"2026 Conference","url":"https://iclr.cc/"}]

Based on the search results, here's what I found about TAPPA:

TAPPA (Temporal Attention Pattern Predictability Analysis) is a unifying framework that explains diverse attention patterns by analyzing their underlying mathematical formulations from a temporally continuous perspective.

**Key Findings:**

TAPPA characterizes attention patterns as predictable patterns with clear regularities and unpredictable patterns that appear effectively random, with this distinction explained by the degree of query self-similarity along the temporal dimension.

The theoretical analysis reveals that stable, predictable patterns arise from the combined effects of query-key continuity and Rotary Positional Embeddings (RoPE), providing a clear explanation for phenomena like periodic sequential diagonals.

**Applications:**

The practical value of TAPPA is confirmed by applying its insights to downstream tasks, with a simple metric inspired by TAPPA successfully improving performance in both KV cache compression and LLM pruning.

The paper (arxiv 2601.21709) was published as a conference paper at ICLR 2026 and is authored by Qingyue Yang and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12a88170-7d4f-4b6a-80ec-2ecfe534a4da",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "5126377f-5074-4186-9d0c-97ed218311d3",
  "sourceToolAssistantUUID": "12a88170-7d4f-4b6a-80ec-2ecfe534a4da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T21:02:15.959Z_

<details><summary>↩ Tool result · `toolu_019wojVpeiaV3mfcmSiZBpm6`</summary>

```text
Web search results for query: "TAPPA temporal attention pattern predictable unpredictable transformer"

Links: [{"title":"Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis","url":"https://arxiv.org/html/2601.21709"},{"title":"Published as a conference paper at ICLR 2026 WHY ATTENTION PATTERNS EXIST:","url":"https://arxiv.org/pdf/2601.21709"},{"title":"[2601.21709] Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis","url":"https://arxiv.org/abs/2601.21709"},{"title":"Easy attention: A simple attention mechanism for temporal predictions with transformers","url":"https://arxiv.org/html/2308.12874v3"},{"title":"GitHub - MIRALab-USTC/LLM-TAPPA: The code for \"Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis\", Qingyue Yang, Jie Wang, Xing Li, Yinqi Bai, Xialiang Tong, Huiling Zhen, Jianye HAO, Mingxuan Yuan, Bin Li. · GitHub","url":"https://github.com/MIRALab-USTC/LLM-TAPPA"},{"title":"TAPformer : A transformer with adaptive attention and temporal projection encoding for long-term electricity load forecasting in IoT systems - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S2542660526000259"},{"title":"Easy attention: A simple attention mechanism for temporal predictions with transformers | APL Computational Physics | AIP Publishing","url":"https://pubs.aip.org/aip/aco/article/1/1/016104/3362108/Easy-attention-A-simple-attention-mechanism-for"},{"title":"Paper page - TAPTR: Tracking Any Point with Transformers as Detection","url":"https://huggingface.co/papers/2403.13042"},{"title":"[2310.18698] Triplet Attention Transformer for Spatiotemporal Predictive Learning","url":"https://arxiv.org/abs/2310.18698"},{"title":"[2202.02093] Temporal Attention for Language Models","url":"https://arxiv.org/abs/2202.02093"}]

Based on the search results, here's what I found about TAPPA:

## TAPPA: Temporal Attention Pattern Predictability Analysis

TAPPA is a unified framework that interprets attention patterns through the temporal behavior of queries and the response of the RoPE channels.

### Core Concept

TAPPA characterizes attention patterns as predictable patterns with clear regularities and unpredictable patterns that appear effectively random. This distinction can be explained by the degree of query self-similarity along the temporal dimension.

### Key Characteristics

Predictable patterns exhibit temporal continuity across decoding steps or along the temporal dimension, where the indices of high attention scores evolve smoothly over time. In contrast, unpredictable patterns display irregular jumps with little temporal consistency.

### Pattern Types

TAPPA provides the first systematic analysis of the shapes of attention patterns from a unifying temporal perspective, analyzing unpredictable patterns alongside three predictable types: re-access, sequential, and seasonal.

### Practical Applications

Temporal stability enables inference optimization: stable patterns can be anticipated and efficiently compressed in the KV cache, while unpredictable ones resist such treatment. The practical value of TAPPA is confirmed by applying its insights to downstream tasks. A simple metric inspired by TAPPA successfully improved performance in both KV cache compression and LLM pruning.

The framework was published as a conference paper at ICLR 2026 and provides valuable insights into understanding and optimizing transformer attention mechanisms in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e52db1c8-abee-4d01-a0f2-aa1f790223b7",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "d07a6617-a995-40ba-8288-d732b9498b04",
  "sourceToolAssistantUUID": "e52db1c8-abee-4d01-a0f2-aa1f790223b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T21:02:26.138Z_

<details><summary>↩ Tool result · `toolu_01AvePxnavBsoMwtm6e2LNdc`</summary>

```text
# TAPPA: Temporal Attention Pattern Predictability Analysis - Key Findings

## Abstract Summary
The paper introduces TAPPA, a framework explaining diverse attention patterns in LLMs through temporal continuity analysis. It identifies that query self-similarity distinguishes predictable patterns (with clear regularities) from unpredictable ones (appearing random), providing mathematical analysis of three representative predictable patterns through interactions between queries, keys, and Rotary Positional Embeddings (RoPE).

## Predictable vs. Unpredictable Patterns

The authors define these categories temporally:

**Predictable patterns:** "exhibit temporal continuity across decoding steps or along the temporal dimension, where the indices of high attention scores evolve smoothly over time."

**Unpredictable patterns:** "display irregular jumps with little temporal consistency."

Empirically, retrieval heads exemplify unpredictable behavior, while re-access and sequential patterns are predictable.

## Query Self-Similarity Metric (q-similarity)

The paper does not provide an explicit closed-form equation for q-similarity in the main text. Instead, they reference it qualitatively as a "quantitative measure of query continuity" based on "similarity between queries at different time indices." The authors state: "When successive queries remain close in representation space, attention indices change smoothly and produce predictable attention maps."

In Appendix F.3, they study "Q-similarity distribution" but the exact mathematical formulation isn't detailed in the provided excerpt.

## Core Theoretical Framework

### Proposition 4.1 (Unpredictable Pattern Condition)

"If qt+1−qt has a large norm and is not orthogonal to all rotated keys {Rt+1−j kj}, then the difference between the logit vectors at and at+1 is necessarily large."

Mathematical bound: ‖at+1−at‖∞ ≥ c₁‖qt+1−qt‖ − c₂ for constants c₁,c₂ > 0

### Theorem 5.1 (Vertical Stability - Re-access Patterns)

Conditions: (1) "queries evolve continuously in the sense that ‖qt+1−qt‖ ≤ ε"; (2) "existence of a dominant low-frequency channel m⋆ whose weight wm⋆ dominates the other channels, and whose RoPE frequency θm⋆ is small."

**Result:** "the per-key differences at+1,i−at,i are uniformly small, and the attention logits are vertically stable."

### Theorem 5.2 (Sequential Patterns)

Conditions: "queries and keys both exhibit high self-similarity, in the sense that ‖qt+1−qt‖ ≤ ε, ‖ki+1−ki‖ ≤ ε for sufficiently small ε > 0"

**Result:** "|at+1,i+1 − at,i| ≤ Cε, for some constant C > 0. Consequently, the attention logits exhibit approximate shift-invariance along the (+1,+1) diagonal, giving rise to sequential patterns."

### Theorem 5.3 (Periodic Sequential Patterns)

"If a sequential pattern arises and the corresponding key exhibits a massive channel at index m⋆, then the spacing between adjacent diagonals is determined by the rotation frequency of that channel: T = 2π/θm⋆ = 2π c^(2m⋆/d)"

### Theorem 5.4 (Seasonal Patterns)

Conditions: Input periodicity with "‖qt+L−qt‖ ≤ εq, ‖ki+L−ki‖ ≤ εk" and resonance condition "|Lθm⋆ − 2kπ| ≤ δ"

**Result:** "|at+L,i − at,i| ≤ C₁(εq + εk) + C₂δ" demonstrating periodic attention behavior.

## Attention Pattern Classification

The framework categorizes heads into:
1. **Re-access/Sink patterns** - repeated focus on small token sets (vertical lines)
2. **Sequential patterns** - diagonal progression through tokens
3. **Periodic sequential patterns** - multiple parallel diagonals
4. **Seasonal patterns** - repeating attention blocks
5. **Retrieval patterns** - semantically-driven random access (unpredictable)

## Models and Benchmarks Evaluated

**Models:** Llama-3.1-8B, Llama-2-7B, Qwen-2.5-7B

**Datasets:** 
- GSM8K and AIGC (for attention pattern analysis)
- LongBench (KV cache compression evaluation - 16 benchmark tasks)
- PIQA, HellaSwag, WinoGrande, ARC-Easy (layer pruning evaluation)

## Relationship to AttentionPredictor

The paper acknowledges: "AttentionPredictor proposed that the temporal continuity of queries is a key driver for pattern formation, though it did not provide a deep mathematical analysis or consider the interplay with RoPE."

TAPPA extends this by providing formal theorems and analyzing RoPE's joint effects.

## Directional Statistics Connection

No explicit mention of Mean Resultant Length (MRL) or directional statistics appears in the provided content. The framework uses angle differences (ϕt,i^(m)) between query and key vectors but doesn't invoke circular statistics terminology.

## Key Results: KV Cache Compression (Table 1)

TAPPA consistently outperformed baselines across budget settings (512-2048 tokens). Example results for Llama-3.1-8B at 1024-token budget:
- TAPPA average: 48.43
- CAKE: 48.43
- SnapKV: 48.32
- H2O: 47.30

## Key Results: LLM Pruning (Table 2)

At 28% pruning (Llama-3.1-8B):
- TAPPA: 59.11% average accuracy
- ShortGPT: 53.51% average accuracy

The pruning strategy leverages q-similarity inversely: "layers with higher query similarity can be pruned with less impact on model performance, while low similarity layers, which are more likely to host retrieval-oriented and task-critical behaviors, are preserved."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da1d4ed2-9c5d-4833-9fa7-ab9eb0c5e2e7",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "c45d6b99-73c9-4302-b4c4-4b85f865fcd2",
  "sourceToolAssistantUUID": "da1d4ed2-9c5d-4833-9fa7-ab9eb0c5e2e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T21:02:29.094Z_

Now let me fetch more details from the PDF and the GitHub repository, and search for the AttentionPredictor connection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c45d6b99-73c9-4302-b4c4-4b85f865fcd2",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZfrHf7kiPPLyfc2Bct",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ae75a3b-0e8a-467c-88fb-90f610bcf312",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StrxfKYcKCKco4YUZqAAmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1672,
      "cache_creation_input_tokens": 2283,
      "cache_read_input_tokens": 11119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2283,
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

_source line 16 · 2026-05-10T21:02:35.348Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Euug5g7MFRqesm3CbWd8dL`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2601.21709",
  "prompt": "Extract ALL mathematical details from this paper. I need:\n1. The exact definition of q-similarity (query self-similarity metric) - the mathematical formula\n2. Full statement of Proposition 4.1 with all mathematical notation\n3. Full statements of Theorems 5.1, 5.2, 5.3, 5.4 with all conditions and bounds\n4. How they define the attention logit decomposition (equation for a_{t,i})\n5. The role of RoPE frequencies theta_m and channel weights w_m\n6. Their connection to or citation of AttentionPredictor\n7. Any error bounds or MSE-type bounds\n8. The q-similarity formula used in their practical applications (KV cache compression and pruning)\n9. Any mention of cosine similarity, angular distance, or circular/directional statistics\n10. Their pruning criterion formula\nInclude ALL equations and mathematical notation verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ae75a3b-0e8a-467c-88fb-90f610bcf312",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZfrHf7kiPPLyfc2Bct",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcb97dcf-175b-430c-b1e2-78ea8e7eb42a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StrxfKYcKCKco4YUZqAAmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1672,
      "cache_creation_input_tokens": 2283,
      "cache_read_input_tokens": 11119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2283,
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

_source line 17 · 2026-05-10T21:02:37.691Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HtwPm2MdNupfLLwv9Mdt3D`</summary>

```json
{
  "url": "https://github.com/MIRALab-USTC/LLM-TAPPA",
  "prompt": "Extract all information about this repository: README content, code structure, implementation details of q-similarity metric, how they classify heads as predictable/unpredictable, any configuration files showing which heads are classified as what."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcb97dcf-175b-430c-b1e2-78ea8e7eb42a",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZfrHf7kiPPLyfc2Bct",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "737a58b4-0953-4914-b4c3-2ace667c6b52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StrxfKYcKCKco4YUZqAAmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1672,
      "cache_creation_input_tokens": 2283,
      "cache_read_input_tokens": 11119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2283,
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

_source line 18 · 2026-05-10T21:02:37.901Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018vQnT5YLfbi8Xv4MCkY4GH`</summary>

```json
{
  "query": "AttentionPredictor temporal continuity query similarity attention prediction transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "737a58b4-0953-4914-b4c3-2ace667c6b52",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZfrHf7kiPPLyfc2Bct",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bd187c9-5e78-49df-85d1-3e52b32fd42e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StrxfKYcKCKco4YUZqAAmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1672,
      "cache_creation_input_tokens": 2283,
      "cache_read_input_tokens": 11119,
      "output_tokens": 484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2283
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1672,
          "output_tokens": 484,
          "cache_read_input_tokens": 11119,
          "cache_creation_input_tokens": 2283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2283,
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

_source line 19 · 2026-05-10T21:02:44.171Z_

<details><summary>↩ Tool result · `toolu_01HtwPm2MdNupfLLwv9Mdt3D`</summary>

```text
# LLM-TAPPA Repository Analysis

## Overview
This GitHub repository contains implementation code for "Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis," published at ICLR 2026. The project introduces TAPPA (Temporal Attention Pattern Predictability Analysis).

## Core Concept
The research explains attention patterns through a temporal lens. The key finding is that "query self-similarity along the temporal dimension (q-similarity)" determines whether attention behaves predictably or irregularly. High q-similarity indicates stable query evolution with clear regularities, while low q-similarity suggests noisy, irregular patterns.

## Repository Structure
Currently, only one module is available:

- **KVCache/** (✅ Available) - Contains KV cache compression methods using q-similarity guided budget allocation
- **Prune/** (⏳ TODO) - Planned structural pruning code
- **Visualization/** (⏳ TODO) - Planned attention pattern visualization tools

## Implementation Details Available
The README provides theoretical framing but **does not include**:
- Specific q-similarity metric calculations
- Code showing head classification as predictable/unpredictable
- Configuration files specifying individual head classifications
- Mathematical formulas for the metric

## Practical Applications
The q-similarity signal guides two downstream tasks:
1. **KV cache compression** - Lower q-similarity receives more budget for token retention (+11.34 average gain over baseline)
2. **Structural pruning** - Higher q-similarity correlates with higher pruning probability (+5.60 average gain)

## Repository Stats
- **7 stars**, **1 fork**, **2 commits**
- **99.8% Python**, **0.2% Shell**
- **MIT License**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "737a58b4-0953-4914-b4c3-2ace667c6b52",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "0dc8c95d-566d-48ab-bad6-b42572735fc0",
  "sourceToolAssistantUUID": "737a58b4-0953-4914-b4c3-2ace667c6b52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T21:02:45.286Z_

<details><summary>↩ Tool result · `toolu_018vQnT5YLfbi8Xv4MCkY4GH`</summary>

```text
Web search results for query: "AttentionPredictor temporal continuity query similarity attention prediction transformer"

Links: [{"title":"AttentionPredictor: Temporal Patterns Matter for KV Cache Compression","url":"https://arxiv.org/pdf/2502.04077"},{"title":"AttentionPredictor: Temporal Pattern Matters for Efficient LLM Inference","url":"https://arxiv.org/html/2502.04077v1"},{"title":"Learning Temporal Features With Alternated Similarity and Proximity Attention for Time-Series Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025ITNNL..3616339C/abstract"},{"title":"Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis","url":"https://arxiv.org/html/2601.21709"},{"title":"[2502.04077] AttentionPredictor: Temporal Patterns Matter for KV Cache Compression","url":"https://arxiv.org/abs/2502.04077"},{"title":"Learning Temporal Features With Alternated Similarity and Proximity Attention for Time-Series Prediction | IEEE Journals & Magazine | IEEE Xplore","url":"https://xplorestaging.ieee.org/document/10981478"},{"title":"[2308.12874] Easy attention: A simple attention mechanism for temporal predictions with transformers","url":"https://arxiv.org/abs/2308.12874"},{"title":"Easy attention: A simple attention mechanism for temporal predictions with transformers","url":"https://arxiv.org/html/2308.12874v3"},{"title":"PeriodNet: Boosting the Potential of Attention Mechanism for Time Series Forecasting","url":"https://arxiv.org/html/2511.19497"},{"title":"Easy attention: A simple attention mechanism for temporal predictions with transformers | APL Computational Physics | AIP Publishing","url":"https://pubs.aip.org/aip/aco/article/1/1/016104/3362108/Easy-attention-A-simple-attention-mechanism-for"}]

Based on the search results, here's what I found about AttentionPredictor and related concepts:

## AttentionPredictor Overview

AttentionPredictor is the first learning-based method to directly predict attention patterns for KV cache compression and critical token identification. It learns a lightweight, unified convolution model to dynamically capture spatiotemporal patterns and predict the next-token attention scores.

## Temporal Continuity and Query Similarity

The core concept behind AttentionPredictor is temporal continuity. Since the temporal dimension corresponds to the query sequence (one query per step), the similarity between adjacent queries (qt and qt+1) is the most critical factor for demonstrating step-by-step temporal continuity. The one-step cosine autocorrelation is 0.87, indicating a high degree of alignment between queries.

Temporal continuity of queries, measured by their self-similarity, is the key factor distinguishing predictable patterns, characterized by clear regularities, and unpredictable patterns that lack stable regularities.

## Applications and Performance

AttentionPredictor achieves 13× KV cache compression and 5.6× speedup in a cache offloading scenario with comparable LLM performance. This frames attention prediction as a time series forecasting task, leveraging temporal prediction techniques to forecast the next-step attention.

The research demonstrates that attention patterns in transformers follow predictable temporal structures, enabling efficient compression of key-value caches for faster inference in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bd187c9-5e78-49df-85d1-3e52b32fd42e",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "77ce6372-c80b-4d01-86ca-eb20ecf0df07",
  "sourceToolAssistantUUID": "5bd187c9-5e78-49df-85d1-3e52b32fd42e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T21:02:45.537Z_

<details><summary>↩ Tool result · `toolu_01Euug5g7MFRqesm3CbWd8dL`</summary>

```text
# Mathematical Details from "Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis"

## 1. Query Self-Similarity (q-similarity) Definition

The paper defines q-similarity as a metric measuring how similar a query at position t is to itself across the sequence. The core formula involves:

**s_q(t) = ||q_t||²** (query norm squared)

This serves as a foundation for their temporal perspective analysis, representing query self-correlation that drives attention patterns.

## 2. Proposition 4.1

The proposition establishes that attention patterns emerge from temporal dynamics. While the exact statement isn't fully visible in the provided PDF content, it relates to how query similarity properties propagate through attention computation.

## 3. Theorems 5.1-5.4

The theorems establish theoretical bounds on attention behavior:

- **Theorem 5.1**: Characterizes conditions under which attention concentrates on recent tokens
- **Theorem 5.2**: Provides bounds on attention mass distribution
- **Theorem 5.3**: Establishes error bounds for approximating attention
- **Theorem 5.4**: Bounds for attention pattern prediction

These theorems use notation like: attention weight bounds, temporal distance measures, and concentration inequalities.

## 4. Attention Logit Decomposition

The attention logit for position (t,i) decomposes as:
**a_{t,i} = q_t^T k_i / √d**

This is the standard dot-product attention scaled by dimension.

## 5. RoPE Frequencies and Channel Weights

The paper references RoPE (Rotary Position Embeddings) with frequency parameters **θ_m** controlling positional encoding. Channel-specific weights **w_m** modulate importance across dimensions, connecting to their temporal analysis framework.

## 6. AttentionPredictor Connection

The paper cites "AttentionPredictor" work (Yang et al. 2025) as predicting attention patterns—their q-similarity framework extends this by providing theoretical grounding for pattern prediction.

## 7. Error Bounds

The paper establishes MSE-type bounds on attention approximation errors of the form:
**E[||ã_t - a_t||²] ≤ bound(q-similarity, temporal-distance)**

Exact constants appear in the theorem statements.

## 8. q-Similarity in KV Cache Compression

For practical compression, they define retention criterion:
**Keep token i if sim(q_t, k_i) > threshold or recency(i,t) < window**

This prioritizes tokens with high query-key similarity or recent positions.

## 9. Directional/Angular Metrics

The framework implicitly uses angular distance through normalized dot products, treating attention as a directional similarity measure on the query-key manifold rather than purely Euclidean distance.

## 10. Pruning Criterion

Tokens are pruned when:
**score_i = w_recent · recency_i + w_sim · similarity_i < threshold**

This weighted combination of temporal and similarity factors determines token retention in compressed KV caches.

**Note**: The provided PDF extract contains structural data rather than fully readable mathematical content. Specific equation numbers and complete bounds would require access to readable equation environments in the full document.

[Binary content (application/pdf, 2.8MB) also saved to /home/ubuntu/.claude-account-1/projects/-/a323c789-4aa2-416f-8bdf-eb4dc8663029/tool-results/webfetch-1778446955381-uuccx7.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcb97dcf-175b-430c-b1e2-78ea8e7eb42a",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "73011f9a-7607-41c7-8477-8d0491be45b4",
  "sourceToolAssistantUUID": "bcb97dcf-175b-430c-b1e2-78ea8e7eb42a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T21:02:48.068Z_

Let me get more details from the HTML version of the paper and the AttentionPredictor paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73011f9a-7607-41c7-8477-8d0491be45b4",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZhHBQ7EJxQ3W1hdnxr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31af09d0-53e6-49d5-9e88-20fbe45c5935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139RertGTxHa6mSEjx5X98Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1299,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 13402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3121,
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

_source line 23 · 2026-05-10T21:02:54.503Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RNsaqxBcRQfWc6pY9cpuEs`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.21709",
  "prompt": "I need the EXACT mathematical details. Please extract:\n1. The EXACT formula for q-similarity - look for any equation defining q-similarity, query self-similarity, or cosine similarity between consecutive queries\n2. The EXACT statement of Proposition 4.1 including the mathematical bound\n3. The attention logit decomposition - how a_{t,i} is broken down into channel contributions with RoPE\n4. Definition of channel weight w_m and massive channel\n5. How they define the per-channel phase angle phi_{t,i}^{(m)}\n6. The EXACT pruning score formula\n7. The EXACT KV cache budget allocation formula\n8. Any equation involving cosine similarity between q_t and q_{t+1}\n9. Their Section 4 on unpredictable patterns - what makes a pattern unpredictable\n10. Their conclusion about which fraction of heads are predictable vs unpredictable\nInclude equation numbers if visible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31af09d0-53e6-49d5-9e88-20fbe45c5935",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZhHBQ7EJxQ3W1hdnxr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7799f9e-a4b9-48f5-a2d7-bf6824419a7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139RertGTxHa6mSEjx5X98Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1299,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 13402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3121,
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

_source line 24 · 2026-05-10T21:02:55.791Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xj1yh2Unf12ChhJRjkwAo7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.04077",
  "prompt": "Extract the abstract and key claims of AttentionPredictor. What is their relationship to TAPPA? What is their query similarity metric? How do they define temporal continuity?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7799f9e-a4b9-48f5-a2d7-bf6824419a7b",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZhHBQ7EJxQ3W1hdnxr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18f5be59-f861-4386-9642-55ab419a21bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139RertGTxHa6mSEjx5X98Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1299,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 13402,
      "output_tokens": 423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1299,
          "output_tokens": 423,
          "cache_read_input_tokens": 13402,
          "cache_creation_input_tokens": 3121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3121,
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

_source line 25 · 2026-05-10T21:03:00.168Z_

<details><summary>↩ Tool result · `toolu_01Xj1yh2Unf12ChhJRjkwAo7`</summary>

```text
# AttentionPredictor: Summary and Analysis

## Abstract & Key Claims

The paper presents **AttentionPredictor**, described as "the first learning-based method to directly predict attention patterns for KV cache compression." Key achievements include:

- A lightweight convolution model that captures spatiotemporal patterns in attention scores
- Achievement of "13× KV cache compression and 5.6× speedup" in cache offloading scenarios
- A unified prediction model shared across transformer layers with negligible memory overhead

## TAPPA Relationship

The provided webpage content does not contain any mention of TAPPA or discuss its relationship to AttentionPredictor. I cannot address this aspect based on the available information.

## Query Similarity Metric

The webpage does not define or describe any query similarity metric used by AttentionPredictor.

## Temporal Continuity Definition

The abstract does not explicitly define "temporal continuity." The paper notes that prior methods "neglect the temporal patterns in attention scores," and proposes learning to "dynamically capture spatiotemporal patterns," but the specific mathematical or operational definition of temporal continuity is not provided in this excerpt.

**Note:** For complete technical details on these metrics and definitions, consulting the full paper would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18f5be59-f861-4386-9642-55ab419a21bf",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "7ab8ec99-53c8-4f1e-a20f-6e5f6cc5cc9a",
  "sourceToolAssistantUUID": "18f5be59-f861-4386-9642-55ab419a21bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T21:03:06.204Z_

<details><summary>↩ Tool result · `toolu_01RNsaqxBcRQfWc6pY9cpuEs`</summary>

```text
# Exact Mathematical Details from TAPPA

## 1. Query Self-Similarity (q-similarity) Definition

The paper does **not provide an explicit mathematical formula** for q-similarity in the main text. Instead, they define it conceptually as temporal continuity of queries: "‖qt+1−qt‖≤ε" indicating successive queries remain close in representation space.

The metric appears computed empirically but the exact formulation is relegated to downstream task sections without a standalone equation.

## 2. Proposition 4.1 (Unpredictable Patterns)

**Exact statement:**
"If qt+1−qt has a large norm and is not orthogonal to all rotated keys {Rt+1−j·kj}, then the difference between the logit vectors at and at+1 is necessarily large. In particular, there exist constants c₁,c₂>0 such that ‖at+1−at‖∞≥c₁‖qt+1−qt‖−c₂."

This demonstrates that large query changes force large attention logit changes, making patterns unpredictable.

## 3. Attention Logit Decomposition (Equation 5)

**Exact decomposition:**
"at,i = Σₘ₌₁ᴹ ‖qt⁽ᵐ⁾‖ ‖ki⁽ᵐ⁾‖ cos(ϕt,i⁽ᵐ⁾+(i−t)θₘ)"

where ϕt,i⁽ᵐ⁾ denotes the angle between qt⁽ᵐ⁾ and ki⁽ᵐ⁾.

## 4. Channel Weight Definition

**Exact definition (Appendix B):**
"wₘ := ‖qt⁽ᵐ⁾‖ ‖ki⁽ᵐ⁾‖"

A "massive channel" or "dominant channel m⋆" is one whose weight wₘ⋆ dominates other channels in the sum.

## 5. Per-Channel Phase Angle

**Exact definition:**
"ψₘ := ϕt,i⁽ᵐ⁾+(i−t)θₘ"

where ϕt,i⁽ᵐ⁾ is the angle between two-dimensional channel pairs qt⁽ᵐ⁾ and ki⁽ᵐ⁾, and θₘ = c⁻²ᵐ/ᵈ is the RoPE frequency.

## 6. Pruning Score Formula

**Not explicitly stated.** The paper uses "q-similarity" combined with "Block Influence" metric but provides no single equation. Section 6.2 states: "layers with higher query similarity can be pruned...layers with low similarity...are preserved."

## 7. KV Cache Budget Allocation

**Not explicitly stated as single formula.** Section 6.1 describes: "we leverage q-similarity as a proxy signal to dynamically guide the per-layer cache budget allocation."

Appendix G.1 provides implementation details but no master equation appears in provided text.

## 8. Cosine Similarity Between Consecutive Queries

**Not explicitly defined.** The paper uses continuity condition ‖qt+1−qt‖≤ε throughout rather than explicit cosine similarity. Empirical q-similarity appears computed but the exact cosine formula is not shown.

## 9. Section 4: Unpredictable Patterns Characteristics

Key finding: **"Unpredictable patterns display irregular jumps with little temporal consistency."** Retrieval heads exemplify this—"their attention often jumps across the entire context in a seemingly random fashion." 

The distinction hinges on whether successive queries satisfy the low-norm condition; large ‖qt+1−qt‖ violates structure.

## 10. Fraction of Predictable vs Unpredictable Heads

**The paper does NOT quantify overall fractions.** It states: "High q-similarity correlates with stable, predictable heads, while low q-similarity leads to retrieval-like, unpredictable behavior" and references Appendix F.3 for distribution analysis across layers, but provides no aggregate percentages in the provided text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7799f9e-a4b9-48f5-a2d7-bf6824419a7b",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "34f50d5d-227c-4deb-b512-fe33a7c0e520",
  "sourceToolAssistantUUID": "a7799f9e-a4b9-48f5-a2d7-bf6824419a7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T21:03:12.519Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B9DH8aUfBLRyP2ez4AFu47`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.04077v1",
  "prompt": "Extract all details about:\n1. Their definition of temporal continuity of queries\n2. The one-step cosine autocorrelation of 0.87 - what is the exact formula?\n3. How they measure query self-similarity\n4. Their relationship to TAPPA or later theoretical work\n5. Author list - are any authors shared with TAPPA?\n6. Their observation about which heads are predictable vs unpredictable\n7. Any classification of attention heads\nInclude exact quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34f50d5d-227c-4deb-b512-fe33a7c0e520",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZioWZF97g7hsK4T2kj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "512147c8-188b-4ce7-8796-7e4a0eb2c51b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiLuzmnvuaYQd1kpxfjBAS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 304,
      "cache_creation_input_tokens": 2800,
      "cache_read_input_tokens": 16523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2800,
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

_source line 28 · 2026-05-10T21:03:16.680Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KA826ttu1yKFfjUiR4iaPF`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.21709",
  "prompt": "I need details from the APPENDIX sections, particularly:\n1. Appendix F.3 - Q-similarity distribution analysis. What does it show? How is q-similarity computed?\n2. Appendix G.1 - KV cache implementation details. What is the exact budget allocation formula?\n3. Section 6 - Applications. What is the exact q-similarity metric used in practice?\n4. Any figures showing the distribution of q-similarity across layers/heads\n5. How many heads fall into predictable vs unpredictable categories empirically\n6. The connection between q-similarity and the theorems - how do they bridge theory and practice?\nAlso extract: Do they mention cosine similarity of consecutive queries? Do they define q-similarity as cos(q_t, q_{t+1})?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "512147c8-188b-4ce7-8796-7e4a0eb2c51b",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZioWZF97g7hsK4T2kj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee3f6d8e-bced-409d-a2a8-102a0d367b0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiLuzmnvuaYQd1kpxfjBAS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 304,
      "cache_creation_input_tokens": 2800,
      "cache_read_input_tokens": 16523,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 304,
          "output_tokens": 435,
          "cache_read_input_tokens": 16523,
          "cache_creation_input_tokens": 2800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2800,
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

_source line 29 · 2026-05-10T21:03:19.608Z_

<details><summary>↩ Tool result · `toolu_01B9DH8aUfBLRyP2ez4AFu47`</summary>

```text
# Analysis of AttentionPredictor's Query Continuity Framework

## 1. Temporal Continuity Definition
The paper defines temporal continuity through query similarity across decoding steps. They state: *"the query sequence exhibits a cosine autocorrelation of 87% at a one-step lag"* and establish that *"High query autocorrelation...is also reported in Lee et al. (2024)."*

## 2. One-Step Cosine Autocorrelation Formula
The exact measurement involves computing similarity between consecutive query vectors. Appendix A specifies: *"we extract query data from LLaMA-3.1-8B using LongBench and compute the cosine autocorrelation of adjacent queries with a lag of 1."* The resulting values are 86% (LongChat) and 87% (LLaMA-3.1), but the document provides no explicit mathematical formula—only the computational procedure.

## 3. Query Self-Similarity Measurement
They employ standard cosine similarity on query embeddings. The paper notes: *"the average similarity is 86% for Longchat and 87% for LLaMA-3.1, indicating strong continuity."* Figure 6 visualizes this across layers and attention heads.

## 4. TAPPA or Later Theoretical Work
The document contains no references to TAPPA or citations to subsequent theoretical frameworks building on this query continuity observation.

## 5. Author Overlap with TAPPA
No author comparison is possible, as TAPPA is not mentioned in this paper.

## 6. Predictable vs. Unpredictable Head Classification
The paper does not classify specific attention heads as predictable or unpredictable. It only observes: *"the similarity in LLaMA is more consistent across layers, while Longchat shows higher similarity in the shallower layers."*

## 7. Attention Head Classification System
No systematic classification of attention heads appears in this work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "512147c8-188b-4ce7-8796-7e4a0eb2c51b",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "c5d55970-a27b-4749-8c2e-95ab18a2e9c3",
  "sourceToolAssistantUUID": "512147c8-188b-4ce7-8796-7e4a0eb2c51b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T21:03:22.943Z_

<details><summary>↩ Tool result · `toolu_01KA826ttu1yKFfjUiR4iaPF`</summary>

```text
# TAPPA Framework: Query Self-Similarity Analysis

## Q-Similarity Definition and Computation

The paper introduces **q-similarity** as a quantitative measure of query continuity, but the exact computational formula is not explicitly stated in the provided sections. However, based on context clues:

- Q-similarity measures "the similarity between queries at different time indices"
- It captures temporal continuity: "When successive queries remain close in representation space, attention indices change smoothly"
- The paper references "Appendix F.3" for "Q-similarity distribution," indicating this metric is computed across layers and heads

The specific formula appears to involve **cosine similarity of consecutive queries**, though the exact form isn't provided in the excerpted content.

## Empirical Distribution Findings

According to Section 4:

> "High q-similarity correlates with stable, predictable heads, while low q-similarity leads to retrieval-like, unpredictable behavior."

Figure 3 demonstrates this empirically, showing that:
- **High q-similarity patterns** exhibit stable, vertical or diagonal structures
- **Low q-similarity patterns** display random attention distributions with scattered focus points

## Theory-to-Practice Bridge

The connection works through **Proposition 4.1**, which establishes that large query changes (low q-similarity) necessarily produce large logit differences. This mathematical result justifies using q-similarity as a practical metric for:

1. **KV Cache Compression** (Section 6.1): Allocating larger cache budgets to low q-similarity layers with unpredictable retrieval patterns
2. **LLM Pruning** (Section 6.2): Identifying high q-similarity layers as redundant candidates for removal

## Key Empirical Results

The paper demonstrates that q-similarity-guided approaches **consistently outperform baselines** across multiple datasets and compression ratios, validating the theoretical predictions about pattern predictability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee3f6d8e-bced-409d-a2a8-102a0d367b0f",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "9103dbf3-3df0-4275-a01e-a8830a273723",
  "sourceToolAssistantUUID": "ee3f6d8e-bced-409d-a2a8-102a0d367b0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T21:03:25.729Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BHNWS2WRtDP6Qbix2PsFHm`</summary>

```json
{
  "query": "\"TAPPA\" \"AttentionPredictor\" same authors query self-similarity USTC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9103dbf3-3df0-4275-a01e-a8830a273723",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZk36eXU5534eCvHyiu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acb48d5c-a564-4a3d-a311-1f88ba6aac3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNTQyjcGzN3EsVhV3amBc4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1670,
      "cache_read_input_tokens": 19323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1670,
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

_source line 32 · 2026-05-10T21:03:26.910Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DWqjKeQHYDbj4P4xaReUyF`</summary>

```json
{
  "query": "AttentionPredictor arxiv 2502.04077 authors Qingyue Yang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acb48d5c-a564-4a3d-a311-1f88ba6aac3f",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZk36eXU5534eCvHyiu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "179ee5ae-9eec-42c5-a994-1720fb0b8eed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNTQyjcGzN3EsVhV3amBc4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1670,
      "cache_read_input_tokens": 19323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1670,
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

### Tool result

_source line 33 · 2026-05-10T21:03:33.279Z_

<details><summary>↩ Tool result · `toolu_01DWqjKeQHYDbj4P4xaReUyF`</summary>

```text
Web search results for query: "AttentionPredictor arxiv 2502.04077 authors Qingyue Yang"

Links: [{"title":"[2502.04077] AttentionPredictor: Temporal Patterns Matter for KV Cache Compression","url":"https://arxiv.org/abs/2502.04077"},{"title":"AttentionPredictor: Temporal Patterns Matter for KV Cache Compression","url":"https://arxiv.org/pdf/2502.04077"},{"title":"AttentionPredictor: Temporal Pattern Matters for Efficient LLM Inference","url":"https://arxiv.org/html/2502.04077v1"},{"title":"AttentionPredictor: Temporal Pattern Matters for Efficient LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AttentionPredictor:-Temporal-Pattern-Matters-for-Yang-Wang/53e17a360183f33c2efd8c79eb76976a60163e0c"},{"title":"GitHub - MIRALab-USTC/LLM-AttentionPredictor: The code for \"AttentionPredictor: Temporal Pattern Matters for Efficient LLM Inference\", Qingyue Yang, Jie Wang, Xing Li, Zhihai Wang, Chen Chen, Lei Chen, Xianzhi Yu, Wulong Liu, Jianye HAO, Mingxuan Yuan, Bin Li.","url":"https://github.com/MIRALab-USTC/LLM-AttentionPredictor"},{"title":"AttentionPredictor: Temporal Pattern Matters for Efficient LLM Inference | Request PDF","url":"https://www.researchgate.net/publication/388792054_AttentionPredictor_Temporal_Pattern_Matters_for_Efficient_LLM_Inference"},{"title":"AttentionPredictor: Temporal Patterns Matter for KV Cache Compression - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250204077Y/abstract"},{"title":"[PDF] AttentionPredictor: Temporal Patterns Matter for KV Cache Compression | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AttentionPredictor:-Temporal-Patterns-Matter-for-KV-Yang-Wang/239a5644c64520f22b6e2073677aeeef96b62f07"},{"title":"GitHub - MIRALab-USTC/LLM-TAPPA: The code for \"Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis\", Qingyue Yang, Jie Wang, Xing Li, Yinqi Bai, Xialiang Tong, Huiling Zhen, Jianye HAO, Mingxuan Yuan, Bin Li. · GitHub","url":"https://github.com/MIRALab-USTC/LLM-TAPPA"},{"title":"Computation and Language Feb 2025","url":"http://www.arxiv.org/list/cs.CL/2025-02?skip=225&show=1000"}]

I found the paper! Here are the key details about AttentionPredictor (arXiv 2502.04077):

## Paper Overview

The paper is authored by Qingyue Yang, Jie Wang, Xing Li, Zhihai Wang, Chen Chen, Lei Chen, Xianzhi Yu, Wulong Liu, Jianye Hao, Mingxuan Yuan, and Bin Li.

## Main Contribution

AttentionPredictor is the first learning-based method to directly predict attention patterns for KV cache compression and critical token identification.

## Technical Approach

AttentionPredictor learns a lightweight, unified convolution model to dynamically capture spatiotemporal patterns and predict the next-token attention scores. The method addresses the limitation that prior methods often struggle to accurately determine critical tokens as they neglect the temporal patterns in attention scores, resulting in degradation in LLM performance.

## Performance

AttentionPredictor achieves 13× KV cache compression and 5.6× speedup in a cache offloading scenario with comparable LLM performance.

## Additional Framework

The authors propose a cross-token critical cache prefetching framework that hides the token estimation time overhead to accelerate the decoding stage.

The code is available on GitHub at https://github.com/MIRALab-USTC/LLM-AttentionPredictor.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "179ee5ae-9eec-42c5-a994-1720fb0b8eed",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "e2503c91-41f7-4c2e-966b-b9209ba33030",
  "sourceToolAssistantUUID": "179ee5ae-9eec-42c5-a994-1720fb0b8eed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T21:03:34.751Z_

<details><summary>↩ Tool result · `toolu_01BHNWS2WRtDP6Qbix2PsFHm`</summary>

```text
Web search results for query: ""TAPPA" "AttentionPredictor" same authors query self-similarity USTC"

Links: [{"title":"GitHub - MIRALab-USTC/LLM-TAPPA: The code for \"Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis\", Qingyue Yang, Jie Wang, Xing Li, Yinqi Bai, Xialiang Tong, Huiling Zhen, Jianye HAO, Mingxuan Yuan, Bin Li. · GitHub","url":"https://github.com/MIRALab-USTC/LLM-TAPPA"},{"title":"Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis","url":"https://arxiv.org/html/2601.21709"},{"title":"GitHub - MIRALab-USTC/LLM-AttentionPredictor: The code for \"AttentionPredictor: Temporal Pattern Matters for Efficient LLM Inference\", Qingyue Yang, Jie Wang, Xing Li, Zhihai Wang, Chen Chen, Lei Chen, Xianzhi Yu, Wulong Liu, Jianye HAO, Mingxuan Yuan, Bin Li.","url":"https://github.com/MIRALab-USTC/LLM-AttentionPredictor"},{"title":"Published as a conference paper at ICLR 2026 WHY ATTENTION PATTERNS EXIST:","url":"https://arxiv.org/pdf/2601.21709"},{"title":"[2601.21709] Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis","url":"https://arxiv.org/abs/2601.21709"},{"title":"AttentionPredictor: Temporal Patterns Matter for KV Cache Compression","url":"https://openreview.net/attachment?id=Guar1tumDr&name=pdf"},{"title":"AttentionPredictor: Temporal Patterns Matter for KV Cache Compression","url":"https://arxiv.org/pdf/2502.04077"},{"title":"AttentionPredictor: Temporal Pattern Matters for Efficient LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AttentionPredictor:-Temporal-Pattern-Matters-for-Yang-Wang/53e17a360183f33c2efd8c79eb76976a60163e0c"},{"title":"[PDF] AttentionPredictor: Temporal Patterns Matter for KV Cache Compression | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AttentionPredictor:-Temporal-Patterns-Matter-for-KV-Yang-Wang/239a5644c64520f22b6e2073677aeeef96b62f07"},{"title":"Lightweight Causal Transformer with Local Self-Attention for Real-Time","url":"http://staff.ustc.edu.cn/~jundu/Publications/publications/oostermeijer21_interspeech.pdf"}]

Based on the search results, I found information about TAPPA and AttentionPredictor that share the same authors and are both affiliated with USTC:

## Shared Authors and Connection

TAPPA and AttentionPredictor are related works by the same research team from USTC (MIRALab-USTC), with authors including Qingyue Yang, Jie Wang, Xing Li, Yinqi Bai, Xialiang Tong, Huiling Zhen, Jianye Hao, Mingxuan Yuan, and Bin Li. TAPPA is closely related to the earlier work AttentionPredictor (NeurIPS 2025), which learns a lightweight convolution model to capture spatiotemporal patterns and predict the next-token attention score.

## Query Self-Similarity Focus

Both papers emphasize query self-similarity:

- TAPPA reveals that the distinction between predictable and unpredictable attention patterns can be explained by the degree of query self-similarity along the temporal dimension, mathematically showing that temporal continuity of queries, measured by their self-similarity, is the key factor distinguishing predictable patterns from unpredictable ones.

- AttentionPredictor observes that the query embedding sequence exhibits high temporal self-similarity with a one-step cosine autocorrelation of 0.87, indicating a high degree of alignment between queries, and high query self-similarity indicates high stability of the attention score over consecutive time steps, which is highly predictable.

TAPPA was published as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acb48d5c-a564-4a3d-a311-1f88ba6aac3f",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "29c750e5-5c29-4a56-a891-ec87ad2e615e",
  "sourceToolAssistantUUID": "acb48d5c-a564-4a3d-a311-1f88ba6aac3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-10T21:03:38.756Z_

Now let me get the final pieces -- the exact q-similarity computation from the code, and look for any connection to MRL or directional statistics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29c750e5-5c29-4a56-a891-ec87ad2e615e",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZkucitQSsu3uxdUM5T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94dae1c0-870a-4071-9ae3-af1e710f4165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8jqpoDKpRGD48MkHKbdRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1154,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 20993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1298,
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

_source line 36 · 2026-05-10T21:03:40.184Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fqghy4wjVZb2AqQjFkGuSL`</summary>

```json
{
  "url": "https://github.com/MIRALab-USTC/LLM-TAPPA/tree/main/KVCache",
  "prompt": "Show the repository structure and any Python files that compute q-similarity. I need to find the exact implementation of how q-similarity is calculated."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94dae1c0-870a-4071-9ae3-af1e710f4165",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZkucitQSsu3uxdUM5T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b95a90bf-f942-4347-a880-edcb1eb7b3d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8jqpoDKpRGD48MkHKbdRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1154,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 20993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1298,
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

_source line 37 · 2026-05-10T21:03:40.637Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WpmxxWUqh912wthmBK1L3s`</summary>

```json
{
  "query": "TAPPA q-similarity cosine query consecutive tokens formula definition attention head classification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b95a90bf-f942-4347-a880-edcb1eb7b3d3",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZkucitQSsu3uxdUM5T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2e7b39a-4a2c-4fb5-ba65-9bc9458ca453",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8jqpoDKpRGD48MkHKbdRz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1154,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 20993,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1298
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1154,
          "output_tokens": 209,
          "cache_read_input_tokens": 20993,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1298,
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

_source line 38 · 2026-05-10T21:03:46.149Z_

<details><summary>↩ Tool result · `toolu_01Fqghy4wjVZb2AqQjFkGuSL`</summary>

```text
# Repository Structure & Q-Similarity Implementation

## Directory Layout

Based on the GitHub page, the KVCache folder contains:

- **`tappa/`**: TAPPA-specific code, including `tappa_qsim.py` for "q-similarity utilities"
- **`tappa/model/`**: Forward implementations for different models (llama, qwen2)
- **`tappa/patch.py`**: Monkeypatch for attention mechanisms
- **`cake/`, `pyramidkv/`**: Baseline method implementations
- **`config/`**: Configuration mappings
- **`pred_kvcache.py`**: Main entry script
- **`eval.py`, `metrics.py`**: Evaluation utilities

## Q-Similarity Location

The document explicitly identifies **`tappa/tappa_qsim.py`** as containing "q-similarity utilities," but the actual source code for these utilities is not displayed in the provided content.

## Next Steps

To access the exact q-similarity calculation implementation, you would need to:
1. Navigate to the `KVCache/tappa/tappa_qsim.py` file in the GitHub repository
2. Review the actual Python code in that module
3. Cross-reference with `tappa/patch.py` to see how it integrates with the attention forward pass

The documentation confirms this module exists but doesn't provide the implementation details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b95a90bf-f942-4347-a880-edcb1eb7b3d3",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "81d83631-5128-4cb3-85bc-672a11af7968",
  "sourceToolAssistantUUID": "b95a90bf-f942-4347-a880-edcb1eb7b3d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T21:03:47.157Z_

<details><summary>↩ Tool result · `toolu_01WpmxxWUqh912wthmBK1L3s`</summary>

```text
Web search results for query: "TAPPA q-similarity cosine query consecutive tokens formula definition attention head classification"

Links: [{"title":"Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis","url":"https://arxiv.org/html/2601.21709"},{"title":"Deep Dive into Self-Attention by Hand✍︎ | Towards Data Science","url":"https://towardsdatascience.com/deep-dive-into-self-attention-by-hand-%EF%B8%8E-f02876e49857/"},{"title":"The Detailed Explanation of Self-Attention in Simple Words | by Maninder Singh | Medium","url":"https://medium.com/@manindersingh120996/the-detailed-explanation-of-self-attention-in-simple-words-dec917f83ef3"},{"title":"Attention (machine learning) - Wikipedia","url":"https://en.wikipedia.org/wiki/Attention_(machine_learning)"},{"title":"11.2. Attention Pooling by Similarity — Dive into Deep Learning 1.0.3 documentation","url":"https://d2l.ai/chapter_attention-mechanisms-and-transformers/attention-pooling.html"},{"title":"What is grouped query attention? | IBM","url":"https://www.ibm.com/think/topics/grouped-query-attention"},{"title":"Query, Key, Value: The Foundation of Transformer Attention - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/query-key-value-attention-mechanism"},{"title":"COTTENTION: LINEAR TRANSFORMERS WITH COSINE ATTENTION Gabriel Mongaras","url":"https://arxiv.org/pdf/2409.18747"},{"title":"Attention? Attention! | Lil'Log","url":"https://lilianweng.github.io/posts/2018-06-24-attention/"},{"title":"What is an attention mechanism? | IBM","url":"https://www.ibm.com/think/topics/attention-mechanism"}]

Based on the search results, I found relevant information about TAPPA and q-similarity:

## TAPPA and Q-Similarity

TAPPA (Temporal Attention Pattern Predictability Analysis) is a unified framework that interprets attention patterns through the temporal behavior of queries and the response of the RoPE channels.

### Q-Similarity Definition

Q-similarity refers to the cosine similarity between consecutive queries, with values around 0.99 indicating very high similarity. Temporal continuity of queries, measured by their self-similarity, is the key factor distinguishing predictable patterns, characterized by clear regularities, and unpredictable patterns that lack stable regularities.

### Key Insights on Query Consecutive Tokens

High q-similarity without RoPE yields a coarse, locally diagonal pattern, whereas only when smooth q-dynamics and RoPE are both present do we obtain clean, stable sequential patterns in the attention map.

### Application to Attention Head Classification

Q-similarity is a metric derived from TAPPA that has been applied to the KV cache compression task, which aims to reduce the memory footprint of key-value caches during large language model inference while maintaining model accuracy.

The framework helps explain why certain attention patterns emerge by analyzing how consecutive query vectors maintain high similarity and how this interacts with positional encoding (RoPE) to produce predictable attention behaviors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2e7b39a-4a2c-4fb5-ba65-9bc9458ca453",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "78f82abb-3071-4fe5-aabb-a88d1eb4d253",
  "sourceToolAssistantUUID": "e2e7b39a-4a2c-4fb5-ba65-9bc9458ca453",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-10T21:03:51.162Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HsfYuUXn7yij8pjsQMntnE`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/MIRALab-USTC/LLM-TAPPA/main/KVCache/tappa/tappa_qsim.py",
  "prompt": "Show the COMPLETE source code of this file. I need to see the exact implementation of q-similarity computation - every function, every line of code."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78f82abb-3071-4fe5-aabb-a88d1eb4d253",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZmpdcXRBFkJ82dYk21",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fe65c45-c187-471e-920f-e514dc5dee46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWoTzUgYb7GdiWvWhQpouc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2660,
      "cache_read_input_tokens": 22291,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2660
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 22291,
          "cache_creation_input_tokens": 2660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2660,
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

_source line 41 · 2026-05-10T21:03:55.311Z_

<details><summary>↩ Tool result · `toolu_01HsfYuUXn7yij8pjsQMntnE`</summary>

```text
# Complete Source Code for Q-Similarity Computation

The file provided contains the **complete implementation** of a single function: `compute_q_sim_torch()`. There are no additional functions or hidden code sections.

## Summary of Implementation

The function computes "TAPPA q_sim from a query time series" using multiple similarity metrics. Here's what's included:

**Main Function:**
- `compute_q_sim_torch()` - accepts query tensor with shape `[T, D]` or `[H, T, D]`

**Supported Metrics (9 total):**
1. **cosine** - normalized dot product similarity
2. **dot** - raw dot product
3. **euclidean** - L2 distance between vectors
4. **rbf** - Gaussian kernel with configurable sigma
5. **l1** - Manhattan distance
6. **pearson** - normalized correlation coefficient
7. **angular** - arc-cosine based angular distance
8. **kl** - symmetric Kullback-Leibler divergence (treats vectors as probability distributions)

**Helper Function:**
- `avg_offdiag()` - computes average of off-diagonal elements in similarity matrices

The implementation uses PyTorch tensor operations and returns a scalar float value representing the average q_sim score across all off-diagonal element pairs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fe65c45-c187-471e-920f-e514dc5dee46",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "8f0e4c1c-510e-41c7-bf65-8e365dd13127",
  "sourceToolAssistantUUID": "4fe65c45-c187-471e-920f-e514dc5dee46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-10T21:04:06.094Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SkVn2eqk35y3PE9hWJpEQd`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/MIRALab-USTC/LLM-TAPPA/main/KVCache/tappa/tappa_qsim.py",
  "prompt": "Show the EXACT Python code verbatim. I need to see the exact implementation including the default metric used, the cosine similarity computation, the angular distance computation, and how q-similarity is computed between consecutive queries vs all pairs. Include every line of code."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f0e4c1c-510e-41c7-bf65-8e365dd13127",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZnRUbqxx5fxvGcCtir",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6ac493c-15a4-4f50-a336-bb78ddf0454a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1tDKAVEWj6vAgn1jKxX3J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 24951,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 24951,
          "cache_creation_input_tokens": 452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 452,
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

_source line 43 · 2026-05-10T21:04:12.983Z_

<details><summary>↩ Tool result · `toolu_01SkVn2eqk35y3PE9hWJpEQd`</summary>

````text
# TAPPA q_sim Implementation

## Default Metric
The default similarity metric is **"cosine"** (average cosine similarity).

## Exact Code Structure

The implementation computes similarity across **all pairs** of timesteps, not just consecutive ones. Here's the key logic:

**Cosine similarity computation:**
```python
norm = q.norm(dim=-1, keepdim=True).clamp_min(eps)
qn = q / norm
sim = torch.matmul(qn, qn.transpose(-1, -2))
```

**Angular distance computation:**
```python
cos_sim = torch.matmul(qn, qn.transpose(-1, -2)).clamp(-1.0, 1.0)
ang = torch.acos(cos_sim) / math.pi
```

**Average off-diagonal calculation:**
The function uses `avg_offdiag()` which computes the mean of all non-diagonal elements:
```python
total = mat.sum(dim=(-1, -2))
diag = mat.diagonal(dim1=-2, dim2=-1).sum(dim=-1)
return (total - diag) / (T * (T - 1))
```

This averages similarities/distances between all distinct timestep pairs, then takes the mean across heads. The final result is `float(q_sim.item())`.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6ac493c-15a4-4f50-a336-bb78ddf0454a",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "a02ae1c1-6777-4c5e-a38e-c28b3dae22b1",
  "sourceToolAssistantUUID": "e6ac493c-15a4-4f50-a336-bb78ddf0454a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-10T21:04:17.106Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015YobtHLiMRKKoqx5HDB9sn`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/MIRALab-USTC/LLM-TAPPA/main/KVCache/tappa/patch.py",
  "prompt": "Show the complete code. I need to see how q-similarity is integrated into the attention forward pass and how it's used for KV cache budget allocation. How does the per-layer budget get computed from q-similarity scores?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a02ae1c1-6777-4c5e-a38e-c28b3dae22b1",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZoj25SAigxCZB54s4f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e79ec3c-23fc-43fb-8b1c-ada92d3a080c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RDsu6jNJCworgCjQv3wJZt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 25403,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 496
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 25403,
          "cache_creation_input_tokens": 496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 496,
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

_source line 45 · 2026-05-10T21:04:21.660Z_

<details><summary>↩ Tool result · `toolu_015YobtHLiMRKKoqx5HDB9sn`</summary>

```text
# Analysis of the Provided Code

Based on the content shown, this is a **patching module** that monkey-patches HuggingFace transformer models, but it **does not contain the actual implementation details** you're asking about.

## What's Missing

The code you've shared only shows the patching interface. To understand how q-similarity is integrated into the attention forward pass and budget allocation, you would need to examine these modules:

- `cake.model.modify_llama` and `cake.model.modify_qwen2` (model forward implementations)
- `tappa.model.llama_forward` and `tappa.model.qwen2_forward` (attention mechanisms)

## What This Code Does

The patching functions replace standard model components with custom versions: "Patch HuggingFace Llama FlashAttention2 to use TAPPA attention forward" and similarly for Qwen2.

## To Answer Your Questions

You'll need to inspect the actual implementation files in the `cake/` and `tappa/` directories, particularly the attention forward functions (`llama_attn_forward_tappa`, `qwen2_attn_forward_tappa`), which would contain the q-similarity scoring logic and KV cache budget computation per layer.

The current snippet only provides the **interface** for applying these patches, not the **mechanisms** behind q-similarity integration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e79ec3c-23fc-43fb-8b1c-ada92d3a080c",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "1c52b878-8f34-4199-8c79-6d04af90b786",
  "sourceToolAssistantUUID": "4e79ec3c-23fc-43fb-8b1c-ada92d3a080c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-10T21:04:25.624Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VPvgGBaa1yzWiMbfozoz7e`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/MIRALab-USTC/LLM-TAPPA/main/KVCache/pred_kvcache.py",
  "prompt": "Show the complete code. I need to see how q-similarity scores are computed per layer, how they are converted to per-layer KV cache budgets, and the budget allocation formula."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c52b878-8f34-4199-8c79-6d04af90b786",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZpNGSBLW3PaqYSWqPT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a989aba-a981-4399-a46c-5e857caa7a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cn4TTJ7phssatAWjxBV4yg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 25899,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 474
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 25899,
          "cache_creation_input_tokens": 474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 474,
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

_source line 47 · 2026-05-10T21:04:30.250Z_

<details><summary>↩ Tool result · `toolu_01VPvgGBaa1yzWiMbfozoz7e`</summary>

```text
# Analysis of Q-Similarity and Budget Allocation

Based on the provided code, I cannot show you the complete implementation you're requesting because **this script does not contain the q-similarity computation or budget allocation logic**.

## What This Script Shows

This is an **evaluation/inference script** that:
- Loads pre-trained models with different KV cache compression methods
- Applies monkeypatches to enable methods like CAKE, TAPPA, PyramidKV, etc.
- Runs generation tasks and evaluates results

## What's Missing

The actual q-similarity calculations and budget allocation formulas are located in **separate imported modules**:

1. `"from cake.cake_cache import CakeprefillKVCache"` — contains CAKE's logic
2. `"from cake.monkeypatch import replace_flashllama_attn_with_cakeattn"` — patches attention layers
3. `"from tappa.patch import apply_tappa_patch"` — implements TAPPA's approach
4. `"from pyramidkv.monkeypatch import replace_llama"` — handles PyramidKV logic

The script only **configures hyperparameters** like `tau1`, `tau2`, `gamma`, and `window_size`, but the actual per-layer q-similarity scoring and budget allocation happens inside those imported modules.

**To find the algorithms you need, examine the source code in the `cake/`, `tappa/`, and `pyramidkv/` package directories.**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a989aba-a981-4399-a46c-5e857caa7a54",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "57cf3db3-f267-44f3-8590-77c5657fe64c",
  "sourceToolAssistantUUID": "6a989aba-a981-4399-a46c-5e857caa7a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-10T21:04:33.249Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0198kYVJqaRdV6UpRCCDABNs`</summary>

```json
{
  "url": "https://github.com/MIRALab-USTC/LLM-TAPPA/tree/main/KVCache/tappa/model",
  "prompt": "List all files in this directory and show their contents or descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57cf3db3-f267-44f3-8590-77c5657fe64c",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZpzt68hRRxaE6SDdAb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81181f28-66dd-4294-ae1b-945ba78c7d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxXiKGUZjvW1oW9e5c66fu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 26373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 500,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-10T21:04:35.125Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015NuvMpGs2mer6SdphL8gdp`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/MIRALab-USTC/LLM-TAPPA/main/KVCache/tappa/model/llama_forward.py",
  "prompt": "Show the complete code. Focus on: how q-similarity is computed during the forward pass, how it determines which tokens to keep in the KV cache, and the budget allocation per layer based on q-similarity. Include all relevant code verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81181f28-66dd-4294-ae1b-945ba78c7d75",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZpzt68hRRxaE6SDdAb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8646bdde-93ab-4525-99b9-ec9ff1f4ed1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxXiKGUZjvW1oW9e5c66fu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 26373,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 500
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 26373,
          "cache_creation_input_tokens": 500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 500,
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

_source line 50 · 2026-05-10T21:04:36.367Z_

<details><summary>↩ Tool result · `toolu_0198kYVJqaRdV6UpRCCDABNs`</summary>

```text
# Files in KVCache/tappa/model Directory

Based on the GitHub page, this directory contains the following files:

1. **llama_forward.py** - Implementation file for LLaMA model forward pass logic
2. **qwen2_forward.py** - Implementation file for Qwen2 model forward pass logic

## Summary

The model directory houses forward pass implementations for two large language models. These files likely contain the core neural network computations and attention mechanisms specific to each model architecture within the LLM-TAPPA project, which appears to focus on KV cache optimization techniques for efficient LLM inference.

The page doesn't provide detailed file descriptions, but the filenames indicate architecture-specific forward propagation code for both LLaMA and Qwen2 models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81181f28-66dd-4294-ae1b-945ba78c7d75",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "4cfa725f-5058-491a-9d28-c4236037207d",
  "sourceToolAssistantUUID": "81181f28-66dd-4294-ae1b-945ba78c7d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-10T21:04:39.906Z_

<details><summary>↩ Tool result · `toolu_015NuvMpGs2mer6SdphL8gdp`</summary>

````text
# Q-Similarity Computation in TAPPA Forward Pass

## Q-Similarity Calculation

The code computes q-similarity during prefill using:

```python
q = query_states[0, :, -T:, :]
mode = "cosine"
q_sim = compute_q_sim_torch(q, mode=mode)
```

Here, `T` represents the window size for the layer. The function `compute_q_sim_torch` (from `tappa.tappa_qsim`) calculates similarity between query tokens using cosine distance as the distance metric.

## Preference Score Computation

The preference score—which determines token importance for cache eviction—combines two scoring approaches:

**When alpha is infinite:**
```python
pref_score = 1 - q_sim
```

**Otherwise (hybrid scoring):**
```python
disp = calculate_entropy(tmp_attn_weights[:, :, -T:, :-T])
var = torch.var(tmp_attn_weights[:, :, -T:, :-T], dim=-2).sum(0).sum(0).sum(0)
cake_score = (disp ** (1 / self.config.tau1) * var ** (1 / self.config.tau2)).cpu().numpy()
pref_score = cake_score + self.config.alpha * (1 - q_sim)
```

This linearly combines entropy-variance metrics with inverse q-similarity, weighted by hyperparameter `alpha`.

## Cache Eviction Integration

The computed `pref_score` is passed to the cache for token selection:

```python
past_key_value.update_score(pref_score, hh_score)
```

The actual eviction mechanism resides in the `CakeDecodingKVCache_LayerWise` class (initialized per layer), which uses these preference scores to determine which tokens remain within allocated budgets across layers.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8646bdde-93ab-4525-99b9-ec9ff1f4ed1f",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "a32e859e0d4ccdd85",
  "type": "user",
  "uuid": "04306888-27f6-44a2-9852-7acbd4fa315e",
  "sourceToolAssistantUUID": "8646bdde-93ab-4525-99b9-ec9ff1f4ed1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-10T21:06:01.461Z_

Now I have comprehensive information. Let me compile the detailed research report.

---

## TAPPA Research Report: Detailed Findings

### Paper Identity

**Title:** "Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis"
**Authors:** Qingyue Yang, Jie Wang, Xing Li, Yinqi Bai, Xialiang Tong, Huiling Zhen, Jianye Hao, Mingxuan Yuan, Bin Li (MIRALab-USTC)
**Venue:** ICLR 2026
**arXiv:** 2601.21709
**Code:** https://github.com/MIRALab-USTC/LLM-TAPPA

### Relationship to AttentionPredictor

TAPPA is the **theoretical follow-up** to AttentionPredictor (arXiv:2502.04077, NeurIPS 2025) by the **same group** (shared first authors: Qingyue Yang, Jie Wang, Xing Li; same lab MIRALab-USTC). The paper explicitly states: "AttentionPredictor proposed that the temporal continuity of queries is a key driver for pattern formation, though it did not provide a deep mathematical analysis or consider the interplay with RoPE." TAPPA provides the formal theorems that AttentionPredictor lacked.

AttentionPredictor empirically observed that consecutive queries have cosine autocorrelation ~0.87 (one-step lag), making attention scores temporally predictable. TAPPA formalizes *why* this happens and what happens when it does not.

---

### Core Framework: Predictable vs. Unpredictable Patterns

**Predictable patterns:** "exhibit temporal continuity across decoding steps or along the temporal dimension, where the indices of high attention scores evolve smoothly over time."

**Unpredictable patterns:** "display irregular jumps with little temporal consistency." Retrieval heads are the canonical example.

The distinction is driven by **query self-similarity (q-similarity)**: when consecutive queries are close in representation space, attention patterns are stable and predictable. When they are not, patterns become erratic.

---

### The q-Similarity Metric

The paper defines q-similarity conceptually via the continuity condition `||q_{t+1} - q_t|| <= epsilon` in the theorems. In practice, the implementation (`tappa_qsim.py`) computes it as the **average pairwise cosine similarity** across all pairs of query vectors within a window:

```python
norm = q.norm(dim=-1, keepdim=True).clamp_min(eps)
qn = q / norm
sim = torch.matmul(qn, qn.transpose(-1, -2))  # [H, T, T] cosine sim matrix
# Then average off-diagonal elements:
q_sim = (total - diag) / (T * (T - 1))  # average over all distinct pairs
```

Default metric is **cosine similarity**. The code also supports angular distance (`arccos(cos_sim) / pi`), Pearson correlation, Euclidean, RBF, L1, KL divergence, and raw dot product. The result is a **scalar per head** (or per layer when averaged across heads).

---

### Key Theoretical Results

#### Attention Logit Decomposition (Equation 5)

The critical mathematical insight is the channel-wise decomposition of the attention logit:

**a_{t,i} = sum_{m=1}^{M} ||q_t^{(m)}|| ||k_i^{(m)}|| cos(phi_{t,i}^{(m)} + (i-t) theta_m)**

where:
- `q_t^{(m)}`, `k_i^{(m)}` are the 2D channel-pair vectors for channel m
- `phi_{t,i}^{(m)}` is the angle between q_t^{(m)} and k_i^{(m)} (before RoPE rotation)
- `theta_m = c^{-2m/d}` is the RoPE frequency for channel m
- `w_m := ||q_t^{(m)}|| ||k_i^{(m)}||` is the channel weight
- A **"massive channel"** m* is one where w_{m*} dominates all other channels

#### Proposition 4.1 (Unpredictable Pattern Condition)

"If q_{t+1} - q_t has a large norm and is not orthogonal to all rotated keys {R_{t+1-j} k_j}, then the difference between the logit vectors a_t and a_{t+1} is necessarily large. In particular, there exist constants c_1, c_2 > 0 such that **||a_{t+1} - a_t||_inf >= c_1 ||q_{t+1} - q_t|| - c_2**."

This is the key negative result: low q-similarity *forces* unpredictable attention.

#### Theorem 5.1 (Vertical Stability / Re-access Patterns)

Conditions: (1) `||q_{t+1} - q_t|| <= epsilon`; (2) existence of a dominant low-frequency channel m* whose weight w_{m*} dominates other channels and whose RoPE frequency theta_{m*} is small.

Result: "the per-key differences a_{t+1,i} - a_{t,i} are uniformly small, and the attention logits are vertically stable."

This explains sink tokens and re-access heads -- they attend to the same positions repeatedly because queries barely change and the dominant channel has low RoPE frequency.

#### Theorem 5.2 (Sequential Patterns)

Conditions: queries and keys both exhibit high self-similarity: `||q_{t+1} - q_t|| <= epsilon`, `||k_{i+1} - k_i|| <= epsilon`

Result: **"|a_{t+1,i+1} - a_{t,i}| <= C*epsilon"** for some constant C > 0. "Consequently, the attention logits exhibit approximate shift-invariance along the (+1,+1) diagonal, giving rise to sequential patterns."

#### Theorem 5.3 (Periodic Sequential Patterns)

If a sequential pattern arises and the corresponding key exhibits a massive channel at index m*, then the spacing between adjacent diagonals is:

**T = 2*pi / theta_{m*} = 2*pi * c^{2m*/d}**

This directly connects the observed periodicity to RoPE frequencies.

#### Theorem 5.4 (Seasonal Patterns)

Conditions: input periodicity `||q_{t+L} - q_t|| <= epsilon_q`, `||k_{i+L} - k_i|| <= epsilon_k`, and resonance condition `|L*theta_{m*} - 2k*pi| <= delta`

Result: **"|a_{t+L,i} - a_{t,i}| <= C_1*(epsilon_q + epsilon_k) + C_2*delta"**

---

### Pattern Classification (5 Types)

1. **Re-access / Sink patterns** -- vertical lines in the attention map (Theorem 5.1)
2. **Sequential patterns** -- diagonal progression (Theorem 5.2)
3. **Periodic sequential patterns** -- multiple parallel diagonals (Theorem 5.3)
4. **Seasonal patterns** -- repeating attention blocks (Theorem 5.4)
5. **Retrieval patterns** -- semantically-driven random access (Proposition 4.1 -- unpredictable)

The paper does **not** provide aggregate statistics on what fraction of heads are predictable vs. unpredictable. It states qualitatively that "High q-similarity correlates with stable, predictable heads, while low q-similarity leads to retrieval-like, unpredictable behavior."

---

### Models and Benchmarks

**Models:** Llama-3.1-8B, Llama-2-7B, Qwen-2.5-7B

**Evaluation:**
- KV cache compression: LongBench (16 tasks), budgets 512-2048 tokens
- LLM pruning: PIQA, HellaSwag, WinoGrande, ARC-Easy
- Pattern analysis: GSM8K, AIGC datasets

**Key results:** TAPPA matches or exceeds baselines (CAKE, SnapKV, H2O) for cache compression; for pruning at 28% on Llama-3.1-8B, TAPPA achieves 59.11% vs ShortGPT's 53.51%.

---

### Practical Application of q-Similarity

In the KV cache code, the preference score for cache eviction is:

- **Simple mode (alpha=inf):** `pref_score = 1 - q_sim` (lower q-similarity = higher priority to keep tokens)
- **Hybrid mode:** `pref_score = cake_score + alpha * (1 - q_sim)` where cake_score combines entropy and variance of attention weights

The pruning strategy is inverted: "layers with higher query similarity can be pruned with less impact on model performance, while low similarity layers, which are more likely to host retrieval-oriented and task-critical behaviors, are preserved."

---

### Connection to MRL / Directional Statistics

**No explicit mention of Mean Resultant Length (MRL) or directional statistics.** The framework uses angle differences (phi_{t,i}^{(m)}) between query and key vectors within the RoPE decomposition, but does not invoke circular statistics terminology. The cosine similarity in their q-similarity metric is standard Euclidean-normalized cosine, not circular MRL.

---

### Critical Analysis for DecompSpec Positioning

**Is TAPPA's "predictable" the same as your "structural"?**

There is strong conceptual overlap but they are **not identical**:

- TAPPA's "predictable" = high q-similarity (consecutive queries are similar) => attention evolves smoothly over time. This is an *empirical/temporal* criterion.
- Your "structural" = high MRL (query directions are concentrated on the circle) => attention is analytically predictable via trigonometric rotation formulas. This is a *geometric/directional statistics* criterion.

The connection: TAPPA's Theorem 5.1-5.4 all assume `||q_{t+1} - q_t|| <= epsilon`, which implies queries change slowly. If queries change slowly *and* have a dominant channel, the attention becomes a near-periodic function of position -- which is exactly what your trigonometric rotation model captures. High MRL would correspond to the case where the dominant channel m* has a weight w_{m*} that overwhelms all others, making the attention logit approximately `w_{m*} * cos(phi + (i-t)*theta_{m*})` -- a single sinusoid, which would have MRL close to 1.

However, TAPPA's classification is **coarser**: a head can be "predictable" (high q-similarity) but still have multiple competing channels (moderate MRL), meaning it's predictable-by-continuity but not analytically decomposable into a single rotation. Your structural/content-dependent split is a **finer-grained** version of their predictable/unpredictable split.

**Does TAPPA provide error bounds similar to your MSE bound?**

Yes, but in a different form. Their bounds are **pointwise logit-difference bounds** (L-infinity norm), not MSE bounds:
- `||a_{t+1} - a_t||_inf >= c_1 ||q_{t+1} - q_t|| - c_2` (Prop 4.1, lower bound for unpredictable)
- `|a_{t+1,i+1} - a_{t,i}| <= C*epsilon` (Theorem 5.2, upper bound for sequential)
- `|a_{t+L,i} - a_{t,i}| <= C_1*(epsilon_q + epsilon_k) + C_2*delta` (Theorem 5.4)

These bound the **temporal stability** of attention logits, not reconstruction error from an analytical approximation. Your MSE bound is about how well a closed-form rotation formula approximates the true attention, which is a different (and arguably more useful for inference) quantity.

**How to position DecompSpec relative to TAPPA:**

1. TAPPA provides the *theoretical justification* for why some heads are analytically tractable (their theorems show that smooth query evolution + dominant RoPE channel = predictable patterns). DecompSpec provides the *operational mechanism* for exploiting this (closed-form rotation formulas with MRL-based head selection).

2. TAPPA's q-similarity is a **temporal continuity measure** (are queries similar over time?). Your MRL is a **directional concentration measure** (are query directions concentrated?). These are related but not the same -- MRL captures the *geometric structure* that makes analytical prediction possible, while q-similarity captures the *temporal smoothness* that makes empirical prediction possible.

3. TAPPA classifies heads into 5 pattern types but does not provide closed-form prediction formulas for any of them. DecompSpec provides exact trigonometric formulas for structural heads. This is a clear differentiation: TAPPA explains *why* patterns exist; DecompSpec shows *how to compute them analytically*.

4. You should cite TAPPA as providing complementary theoretical foundations: "TAPPA (Yang et al., ICLR 2026) establishes that query self-similarity drives pattern predictability, identifying conditions under which attention logits are temporally stable. Our work goes further by showing that for heads with high directional concentration (MRL), the attention can be computed in closed form via trigonometric rotation, eliminating the need for explicit key-value storage entirely."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04306888-27f6-44a2-9852-7acbd4fa315e",
  "isSidechain": true,
  "agentId": "a32e859e0d4ccdd85",
  "requestId": "req_011CauZqiCGcXyP4TZEqZv1J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84eb2d5f-6224-4d44-95e5-70687b6bb1ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mj2tYvk1jZpbc1HgbTi8Gs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 26873,
      "output_tokens": 3305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 943
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3305,
          "cache_read_input_tokens": 26873,
          "cache_creation_input_tokens": 943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 943,
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
