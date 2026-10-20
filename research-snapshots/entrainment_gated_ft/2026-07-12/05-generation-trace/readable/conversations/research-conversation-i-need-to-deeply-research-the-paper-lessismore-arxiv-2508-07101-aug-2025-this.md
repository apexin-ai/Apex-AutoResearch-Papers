# Research conversation: I need to deeply research the paper "LessIsMore" (arXiv:2508.07101, Aug 2025). This paper argues that per-head token sel

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ab24a9630119d9066.jsonl`
- **Structured JSON:** [`be4c392b0affda151152.json`](../../sessions/be/be4c392b0affda151152.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-10T20:58:38.365Z_

I need to deeply research the paper "LessIsMore" (arXiv:2508.07101, Aug 2025). This paper argues that per-head token selection is suboptimal during reasoning because token importance is "global and stable across attention heads," and proposes a unified cross-head approach.

Please do the following:
1. Use WebFetch to read the paper at https://arxiv.org/abs/2508.07101 — get the abstract and key claims
2. Use WebFetch to read the PDF at https://arxiv.org/pdf/2508.07101 if possible, focusing on:
   - Their main argument for why unified cross-head selection works
   - What models they evaluate on
   - What benchmarks they use
   - Their speedup numbers
   - Any caveats or limitations they mention about their unified approach
3. Search for any follow-up work that cites or responds to LessIsMore

The context: I'm working on a method (DecompSpec) that does per-head adaptive temporal prediction for self-speculative decoding. The reviewer says LessIsMore is the strongest counterargument to per-head adaptive strategies during reasoning. I need to understand exactly what they claim so I can position my work appropriately.

Key distinction I need to verify: Does LessIsMore address *which tokens* to attend to (token importance rankings), or does it also address *how to predict attention scores* across draft steps? My method operates at the temporal prediction mechanism level (how scores evolve across draft steps), not the token selection level.

Report your findings in detail — include exact quotes from the abstract if possible, their main theorem/result, evaluation setup, and any limitations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "8f05b497-ea69-4242-b03b-8459e367a587",
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

_source line 2 · 2026-05-10T20:58:38.368Z_

```json
{
  "parentUuid": "8f05b497-ea69-4242-b03b-8459e367a587",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
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
  "uuid": "d5d1a2d7-2497-4496-ab36-e2e81d7b1108",
  "timestamp": "2026-05-10T20:58:38.368Z",
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

_source line 3 · 2026-05-10T20:58:40.629Z_



I'll start by loading the WebFetch and WebSearch tool schemas, then fetch the paper and search for follow-up work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5d1a2d7-2497-4496-ab36-e2e81d7b1108",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZP4RS4yF15GcHtdi8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef9d66b2-d705-49a3-bbbd-0a07332eb9ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhsnnG8wPNJu2YHZFEV6Um",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 924,
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

_source line 4 · 2026-05-10T20:58:41.100Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RdyJKbgmHEPi5EJxmXNGPQ`</summary>

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
  "parentUuid": "ef9d66b2-d705-49a3-bbbd-0a07332eb9ff",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZP4RS4yF15GcHtdi8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8273a900-404c-4a44-bb03-d18f967e2cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhsnnG8wPNJu2YHZFEV6Um",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 8223,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 924
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 924,
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

_source line 5 · 2026-05-10T20:58:41.109Z_

<details><summary>↩ Tool result · `toolu_01RdyJKbgmHEPi5EJxmXNGPQ`</summary>

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
  "parentUuid": "8273a900-404c-4a44-bb03-d18f967e2cb0",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "6202f4a8-f765-4768-a589-1daaf736c8ef",
  "sourceToolAssistantUUID": "8273a900-404c-4a44-bb03-d18f967e2cb0",
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

_source line 6 · 2026-05-10T20:58:44.082Z_



Now let me fetch the paper abstract page and PDF, and search for follow-up work, all in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6202f4a8-f765-4768-a589-1daaf736c8ef",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZPGUENVhrU63PQCgwD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0b71b36-7401-4653-b3f2-263fc28b4510",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H23Ww2U4svU82Y3eRK5sAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 7 · 2026-05-10T20:58:46.442Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014Ae9y2AwrNH9vYJCKqMuvw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.07101",
  "prompt": "Extract the full abstract, author names, title, submission date, and any other metadata about this paper. Include the complete abstract text verbatim. Also extract any information about the paper's main contributions or claims mentioned on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0b71b36-7401-4653-b3f2-263fc28b4510",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZPGUENVhrU63PQCgwD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f68763b0-426a-44fc-b4c5-3b2aa9523f1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H23Ww2U4svU82Y3eRK5sAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 8 · 2026-05-10T20:58:51.834Z_

<details><summary>↩ Tool result · `toolu_014Ae9y2AwrNH9vYJCKqMuvw`</summary>

```text
# Paper Metadata Extract

**Title:** Less Is More: Fast and Accurate Reasoning with Cross-Head Unified Sparse Attention

**Authors:** Lijie Yang, Zhihao Zhang, Arti Jain, Shijie Cao, Baihong Yuan, Yiwei Chen, Zhihao Jia, Ravi Netravali

**arXiv Identifier:** 2508.07101

**Submission Date:** August 9, 2025 (v1); Last revised April 27, 2026 (v2)

**Subject Classification:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI)

## Abstract

The researchers present a training-free sparse attention mechanism designed for reasoning models. Their method, called LessIsMore, operates on the principle that "token importance in reasoning is global and stable: critical tokens are largely shared across attention heads." The approach unifies token selection across attention heads and maintains a stable recency window to preserve recent context.

## Key Claims & Contributions

- Achieves performance matching or exceeding baseline accuracy while attending to substantially fewer tokens
- Demonstrates "up to 1.6× end-to-end decoding speedup" and "up to 1.72× faster sparse attention computation"
- Works across multiple model families and challenging reasoning benchmarks
- Requires no retraining
- Shows generality across long-context scenarios
- Code is publicly available on GitHub
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f68763b0-426a-44fc-b4c5-3b2aa9523f1b",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "16906fb8-b4c2-41f8-be71-973e1fd17a13",
  "sourceToolAssistantUUID": "f68763b0-426a-44fc-b4c5-3b2aa9523f1b",
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

_source line 9 · 2026-05-10T20:58:55.001Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RtS8bjzMeDWNuJH6mFzvKu`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2508.07101",
  "prompt": "Extract as much detail as possible from this paper, focusing on:\n1. The full abstract\n2. The main argument/theorem for why unified cross-head token selection works better than per-head selection\n3. What specific models they evaluate on (model names and sizes)\n4. What benchmarks they use for evaluation\n5. Their reported speedup numbers and accuracy/quality metrics\n6. Any caveats, limitations, or failure cases they mention about their unified approach\n7. Whether they address token importance rankings (which tokens to attend to) vs how to predict attention scores across draft steps\n8. Their method description - what exactly does \"unified cross-head\" mean in their approach\n9. Any theoretical results or proofs\n10. The difference between their work and self-speculative decoding approaches\nInclude exact quotes where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16906fb8-b4c2-41f8-be71-973e1fd17a13",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZPGUENVhrU63PQCgwD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53134a05-e69e-4cc1-99f4-e35f4552484b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H23Ww2U4svU82Y3eRK5sAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 10 · 2026-05-10T20:58:55.271Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BjPCHYyaWa75G1LY4631kf`</summary>

```json
{
  "query": "LessIsMore arXiv 2508.07101 unified cross-head token selection attention reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53134a05-e69e-4cc1-99f4-e35f4552484b",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZPGUENVhrU63PQCgwD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd0d8b92-8b61-4c28-902c-59e66e2290df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H23Ww2U4svU82Y3eRK5sAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 11 · 2026-05-10T20:58:55.293Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WS8122HZa3NhscayZgifub`</summary>

```json
{
  "query": "\"LessIsMore\" cross-head attention token selection per-head reasoning LLM citation follow-up 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd0d8b92-8b61-4c28-902c-59e66e2290df",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZPGUENVhrU63PQCgwD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afd8ce8b-5f22-481d-b181-c2e912838232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H23Ww2U4svU82Y3eRK5sAK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9147,
      "output_tokens": 518,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 518,
          "cache_read_input_tokens": 9147,
          "cache_creation_input_tokens": 1917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1917,
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

_source line 12 · 2026-05-10T20:59:02.630Z_

<details><summary>↩ Tool result · `toolu_01BjPCHYyaWa75G1LY4631kf`</summary>

```text
Web search results for query: "LessIsMore arXiv 2508.07101 unified cross-head token selection attention reasoning 2025 2026"

Links: [{"title":"[2508.07101] Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/abs/2508.07101"},{"title":"Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/html/2508.07101"},{"title":"Paper page - Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://huggingface.co/papers/2508.07101"},{"title":"Less Is More: Fast and Accurate Reasoning with Cross-Head Unified Sparse Attention | OpenReview","url":"https://openreview.net/forum?id=3iwDzfIk60"},{"title":"[2508.08961] DualSpeechLM: Towards Unified Speech Understanding and Generation via Dual Speech Token Modeling with Large Language Models","url":"https://arxiv.org/abs/2508.08961"},{"title":"Learning Unified User Quantized Tokenizers for User Representation","url":"https://arxiv.org/html/2508.00956v2"},{"title":"FLUID: Flow-Latent Unified Integration via Token Distillation for Expert Specialization in Multimodal Learning","url":"https://arxiv.org/html/2508.07264"},{"title":"Cross-Tokenizer LLM Distillation through a Byte-Level Interface","url":"https://arxiv.org/html/2604.07466"},{"title":"[2508.07264] FLUID: Flow-Latent Unified Integration via Token Distillation for Expert Specialization in Multimodal Learning","url":"https://arxiv.org/abs/2508.07264"},{"title":"Cubit: Token Mixer with Kernel Ridge Regression","url":"https://arxiv.org/html/2605.06501v1"}]

I found the paper you're looking for. Here's what I found:

## LessIsMore: Training-Free Sparse Attention with Global Locality for Efficient Reasoning

LessIsMore is a training-free sparse attention mechanism for reasoning tasks that leverages global attention patterns and aggregates token selections from local attention heads with recent contextual information, enabling unified cross-head token ranking for future decoding layers.

**Key Features:**
- This unified selection improves generalization and efficiency by avoiding the need to maintain separate token subsets per head.
- LessIsMore reserves a fixed proportion for a stable recency window, ensuring that recently generated tokens—critical for step-by-step reasoning—are consistently attended to.

**Performance Results:**
- LessIsMore preserves—and in some cases improves—accuracy while achieving a 1.1× average decoding speed-up compared to full attention.
- LessIsMore attends to 2× fewer tokens without accuracy loss, achieving a 1.13× end-to-end speed-up compared to existing sparse attention methods.
- Evaluation on Qwen3-8B and Qwen3-4B across diverse reasoning tasks demonstrates that LessIsMore consistently outperforms existing sparse attention baselines, achieving up to 87.5% sparsity and 1.1× end-to-end inference speed-up on AIME-24 with lossless accuracy.

**Paper Details:**
The paper was submitted to arXiv on August 9, 2025 (arxiv.org/abs/2508.07101), and code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd0d8b92-8b61-4c28-902c-59e66e2290df",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "75ab9439-a419-4581-beaa-11b14f54835d",
  "sourceToolAssistantUUID": "bd0d8b92-8b61-4c28-902c-59e66e2290df",
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

_source line 13 · 2026-05-10T20:59:02.724Z_

<details><summary>↩ Tool result · `toolu_01RtS8bjzMeDWNuJH6mFzvKu`</summary>

```text
# Analysis of "Less Is More: Fast and Accurate Reasoning with Cross-Head Unified Sparse Attention"

## 1. Abstract
The document title indicates this work focuses on achieving "Fast and Accurate Reasoning with Cross-Head Unified Sparse Attention," suggesting an approach to optimize attention mechanisms during LLM inference.

## 2. Main Argument
The paper proposes unified cross-head token selection rather than per-head selection. This means determining which tokens to attend to based on a single unified decision across all attention heads, rather than making independent selections for each head. The key insight appears to be that this unified approach reduces redundancy and computational overhead while maintaining reasoning accuracy.

## 3. Models Evaluated
The evaluation includes:
- Llama 3-8B (Instruct variant with 1M context)
- DeepSeek-R1
- Qwen 3
- Claude 4
- GPT-O-SS (OpenAI)
- GPT-5 (referenced as upcoming)

## 4. Benchmarks
The evaluation uses reasoning-focused benchmarks:
- AIME (American Invitational Mathematics Examination)
- GPQA (Graduate-level Google Proof QA)
- General chain-of-thought reasoning tasks
- LongBench for long-context evaluation

## 5. Speedup and Metrics
The document references performance improvements but specific numerical speedup percentages are embedded in compressed PDF streams and cannot be reliably extracted from the provided format.

## 6. Caveats and Limitations
The paper discusses tradeoffs between inference speed and reasoning quality. One limitation mentioned involves "Recency Locality in Reasoning Process," suggesting that maintaining access to recent reasoning steps is critical—a constraint that unified selection must respect.

## 7. Token Importance vs. Attention Score Prediction
The work addresses token importance ranking—determining which tokens deserve attention—rather than predicting raw attention scores across speculative decoding steps.

## 8. Method Description
"Unified cross-head" means applying a single sparsity pattern across all attention heads simultaneously, eliminating per-head redundancy. This contrasts with traditional approaches where each head independently selects attended tokens.

## 9. Theoretical Results
No explicit proofs are evident in the extractable portions, though the framing suggests theoretical grounding in attention mechanism analysis.

## 10. Difference from Self-Speculative Decoding
Self-speculative decoding involves draft step prediction and verification. This work focuses on static attention optimization during reasoning, not speculative draft generation.

[Binary content (application/pdf, 8.2MB) also saved to /home/ubuntu/.claude-account-1/projects/-/a323c789-4aa2-416f-8bdf-eb4dc8663029/tool-results/webfetch-1778446735077-ujzg8b.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53134a05-e69e-4cc1-99f4-e35f4552484b",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "a0ed0c9c-7ff2-42c5-9283-5b68298267ef",
  "sourceToolAssistantUUID": "53134a05-e69e-4cc1-99f4-e35f4552484b",
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

_source line 14 · 2026-05-10T20:59:03.669Z_

<details><summary>↩ Tool result · `toolu_01WS8122HZa3NhscayZgifub`</summary>

```text
Web search results for query: ""LessIsMore" cross-head attention token selection per-head reasoning LLM citation follow-up 2025 2026"

Links: [{"title":"Less Is More: Fast and Accurate Reasoning with Cross-Head Unified Sparse Attention | OpenReview","url":"https://openreview.net/forum?id=3iwDzfIk60"},{"title":"[2508.07101] Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/abs/2508.07101"},{"title":"Less Is More: Fast and Accurate Reasoning with Cross-Head Unified Sparse Attention","url":"https://arxiv.org/html/2508.07101v2"},{"title":"Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/html/2508.07101v1"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Attention Mechanism in LLMs Explained (2026)","url":"https://www.buildfastwithai.com/blogs/attention-mechanism-llm-explained"},{"title":"understanding and steering the cognitive be","url":"https://www.arxiv.org/pdf/2512.24574"},{"title":"State of Reasoning LLMs: The New Era of “Thinking” Machines | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/state-of-reasoning-llms-the-new-era-of-thinking-machines-f241b1a3096d"},{"title":"M-A-P A Survey on Latent Reasoning","url":"https://www.nju-link.com/zh/publication/zhu-2025-surveylatentreasoning/zhu-2025-surveylatentreasoning.pdf"},{"title":"GitHub - amitshekhariitbhu/llm-internals: Learn LLM internals step by step - from tokenization to attention to inference optimization. · GitHub","url":"https://github.com/amitshekhariitbhu/llm-internals"}]

Based on the web search results, I found comprehensive information about LessIsMore, a recent research paper on cross-head attention token selection for reasoning LLMs. Here's what I found:

## Overview

LessIsMore is a training-free sparse attention mechanism for reasoning tasks, which leverages global attention patterns rather than relying on traditional head-specific local optimizations.

## Key Mechanism

LessIsMore aggregates token selections from local attention heads with recent contextual information, enabling unified cross-head token ranking for future decoding layers, which improves generalization and efficiency by avoiding the need to maintain separate token subsets per head.

## Performance Results

Evaluation across diverse reasoning tasks and benchmarks shows that LessIsMore preserves -- and in some cases improves -- accuracy while achieving a 1.1× average decoding speed-up compared to full attention. Additionally, LessIsMore attends to 2× fewer tokens without accuracy loss, achieving a 1.13× end-to-end speed-up compared to existing sparse attention methods.

LessIsMore achieves up to 87.5% sparsity on AIME-24 with no accuracy loss and avoids the generation length inflation observed in prior sparse attention methods.

## Evaluation Details

The research evaluated four reasoning models: Qwen3-4B, Qwen3-8B, Qwen3-14B, and DeepSeek-R1-Distill-Llama-8B on multiple mainstream reasoning tasks, including AIME-24, AIME-25, GPQA-Diamond, and MATH500.

The paper appears to have been released in August 2025 and was presented at OpenReview in October 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afd8ce8b-5f22-481d-b181-c2e912838232",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "f806364c-592a-43ae-80b0-e157149e0cce",
  "sourceToolAssistantUUID": "afd8ce8b-5f22-481d-b181-c2e912838232",
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

_source line 15 · 2026-05-10T20:59:07.557Z_

Good, I have solid initial information. Now let me get more details from the HTML version of the paper (which is more parseable than the PDF), check the OpenReview page for reviews, and search for citations/responses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f806364c-592a-43ae-80b0-e157149e0cce",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZQvm83VQB9g2fdVECk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c97120c-401a-4b2a-8f0b-940d6be304ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EhE3MyMdethgvFEXB79Bo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3438,
      "cache_read_input_tokens": 11064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3438,
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

_source line 16 · 2026-05-10T20:59:15.545Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PSZCis2WuGcuZmZjtp6QrW`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.07101v2",
  "prompt": "Extract detailed information about:\n1. The EXACT abstract text, verbatim\n2. Their key observation about token importance being \"global and stable across attention heads\" - what evidence do they provide? What figures or analysis support this?\n3. The method description: How does unified cross-head selection work exactly? What is the algorithm?\n4. The \"recency window\" component - what is it and why is it needed?\n5. Their definition of \"global locality\" \n6. Any theoretical claims or formal results\n7. Their comparison against per-head selection methods - which specific methods do they compare against?\n8. The exact models evaluated: Qwen3-4B, Qwen3-8B, Qwen3-14B, DeepSeek-R1-Distill-Llama-8B - any others?\n9. Benchmarks: AIME-24, AIME-25, GPQA-Diamond, MATH500 - any others?\n10. Exact speedup numbers with context\n11. Limitations section - what do they say about when their approach might NOT work?\n12. Any mention of speculative decoding, draft models, or temporal prediction\n13. The difference between their \"token selection\" approach and attention score prediction\n14. Section headings and structure of the paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c97120c-401a-4b2a-8f0b-940d6be304ab",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZQvm83VQB9g2fdVECk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4322bad-2807-47d7-a1e5-6d1239065f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EhE3MyMdethgvFEXB79Bo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3438,
      "cache_read_input_tokens": 11064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3438,
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

_source line 17 · 2026-05-10T20:59:18.145Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RQGe4Yk87C3rF61gt7S9pF`</summary>

```json
{
  "url": "https://openreview.net/forum?id=3iwDzfIk60",
  "prompt": "Extract all reviewer comments, scores, and any discussion about this paper. Include:\n1. What venue is this submitted to?\n2. Reviewer scores and summaries\n3. Any reviewer criticisms about the per-head vs unified approach\n4. Any discussion about limitations of the unified approach\n5. Any mention of speculative decoding or comparison to per-head methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4322bad-2807-47d7-a1e5-6d1239065f66",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZQvm83VQB9g2fdVECk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da1e165a-8dd9-44f2-a650-2f4214041724",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EhE3MyMdethgvFEXB79Bo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3438,
      "cache_read_input_tokens": 11064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3438,
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

_source line 18 · 2026-05-10T20:59:18.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EXY3W46S9u7FJK6ugjcxUb`</summary>

```json
{
  "query": "cite:2508.07101 OR \"Less Is More\" \"cross-head\" sparse attention reasoning follow-up work response 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da1e165a-8dd9-44f2-a650-2f4214041724",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZQvm83VQB9g2fdVECk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8297d3a2-5339-4348-98bd-ae59275b00b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EhE3MyMdethgvFEXB79Bo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3438,
      "cache_read_input_tokens": 11064,
      "output_tokens": 636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3438
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 636,
          "cache_read_input_tokens": 11064,
          "cache_creation_input_tokens": 3438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3438,
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

_source line 19 · 2026-05-10T20:59:21.955Z_

<details><summary>↩ Tool result · `toolu_01RQGe4Yk87C3rF61gt7S9pF`</summary>

```text
# Paper Review Summary

## Venue
This paper is submitted to **ICLR 2026 Conference**.

## Reviewer Information
Based on the provided web page content, **no reviewer comments, scores, or discussion are included**. The page displays only:
- Paper title and author information
- Submission date (September 13, 2025; modified February 11, 2026)
- Abstract and keywords
- Publication status indicators

## What's Missing
The extracted content does not contain:
1. Reviewer scores or evaluations
2. Reviewer summaries or criticisms
3. Discussion about per-head versus unified approaches
4. Analysis of unified approach limitations
5. Any mentions of speculative decoding or method comparisons
6. Review discussion threads

## Note
To access this information, you would need to visit the full OpenReview page and check the "Revisions" section or review timeline, which typically displays reviewer feedback, scores, and author responses once the review period concludes and results are published.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da1e165a-8dd9-44f2-a650-2f4214041724",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "d37b0dec-1fcb-495c-a416-b2c20aab4bc2",
  "sourceToolAssistantUUID": "da1e165a-8dd9-44f2-a650-2f4214041724",
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

_source line 20 · 2026-05-10T20:59:22.892Z_

<details><summary>↩ Tool result · `toolu_01EXY3W46S9u7FJK6ugjcxUb`</summary>

```text
Web search results for query: "cite:2508.07101 OR "Less Is More" "cross-head" sparse attention reasoning follow-up work response 2026"

Links: [{"title":"[2508.07101] Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/abs/2508.07101"},{"title":"Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/html/2508.07101"}]

The web search found the original paper (arXiv:2508.07101) titled "Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning." This paper introduces LessIsMore, a training-free sparse attention mechanism for reasoning tasks that leverages global attention patterns and aggregates token selections from local attention heads with recent contextual information, enabling unified cross-head token ranking for future decoding layers.

However, the search results don't show any follow-up work or responses to this paper from 2026. Since this paper was published in August 2025 and today's date is May 10, 2026, there may be follow-up work available, but it's not appearing in these search results. The query syntax you used (with "cite:" operator) is specific to Google Scholar, which may not be fully indexed in standard web search results. If you're looking for citations or follow-up responses to this paper, you might have better success searching directly on arXiv.org or Google Scholar.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8297d3a2-5339-4348-98bd-ae59275b00b3",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "8c9f2b68-e4aa-4880-9dc7-2c71c58caa67",
  "sourceToolAssistantUUID": "8297d3a2-5339-4348-98bd-ae59275b00b3",
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

_source line 21 · 2026-05-10T20:59:38.941Z_

<details><summary>↩ Tool result · `toolu_01PSZCis2WuGcuZmZjtp6QrW`</summary>

```text
# LessIsMore: Detailed Analysis

## 1. Abstract (Verbatim)

"Large reasoning models achieve strong performance through test-time scaling, but this incurs substantial computational overhead due to long decoding from short prompts. While sparse attention can reduce latency and memory usage, existing methods often degrade reasoning accuracy because selection errors accumulate over long generation horizons, or require costly retraining. We introduce LessIsMore, a training-free sparse attention mechanism for long-horizon reasoning. Our key insight is that token importance in reasoning is global and stable: critical tokens are largely shared across attention heads and remain stable over decoding steps."

## 2. Key Observation: Global & Stable Token Importance

**Evidence provided:**

- **Figure 2**: Visualizes ground-truth top-4K attended tokens across 32 attention heads in Qwen3-8B at decoding step 20K. Shows "substantial overlap in token importance rankings both within key-value groups (yellow regions) and across all heads (red regions)."

- **Attention Recall Analysis (Figure 1a)**: Demonstrates TidalDecode achieves only ~75% recall on AIME-24, while their method maintains higher recall throughout generation.

- **Cross-Head Spatial Locality (Section 2.3)**: Claims overlaps "persist across layers and decoding steps" per appendix sections A.6 and references to Figures 9-10.

- **Temporal Recency Locality (Section 2.4)**: "Recently generated tokens consistently receive high attention scores across all heads" and "the ratio between recent tokens and total critical tokens remains approximately constant."

## 3. Method: Unified Cross-Head Selection

**Algorithm structure (Algorithm 1):**

The approach operates through three layer types:
- **Full Attention Layers**: Early layers (first 2) use standard attention
- **Token Selection Layers** (CUSA): Compute globally consistent indices
- **Sparse Attention Layers**: Reuse computed indices

**Exact mechanism (lines 10-13):**

Each head independently proposes top-k candidates: `ρ_head = TopKIndices(P[:,:-Kr], k=K(1-r))`

These proposals are aggregated via `UnionFlatten()` into single ranked set, retaining top K(1-r) tokens globally.

Final selection: `ρ = ρ_unified[:K(1-r)] ∪ ρ_recent`

## 4. Recency Window Component

**Purpose**: Preserve step-by-step reasoning coherence by explicitly allocating fixed proportion r of token budget to recent tokens.

**Implementation**: Reserve K·r most recent tokens, union them with historically selected K(1-r) tokens.

**Why needed**: Section 2.4 observes recent tokens receive "consistently high attention scores" and this proportion "remains approximately constant throughout decoding."

**Default setting**: r = 0.25 (25% budget reserved for recent context)

## 5. Definition of "Global Locality"

The paper uses "global" in two senses:

1. **Spatial globality**: Token importance "is a global property, not a head-local one" (p. 5). Important tokens overlap substantially across all attention heads rather than being head-specific.

2. **Temporal globality**: Token importance remains stable across decoding steps, enabling "infrequent re-selection" with index reuse across multiple layers.

The authors explicitly state: "token importance in reasoning is a global and slowly evolving property."

## 6. Theoretical Claims & Formal Results

**No formal theorems presented.** The paper is empirically motivated.

**Key structural claims:**
- "Even small selection errors compound across thousands of decoding steps, leading to attention recall degradation" (informal complexity argument)
- Attention recall (Equation 3) as diagnostic metric: `R_i = Σ(softmax(W_i)[ρ]) / Σ(softmax(W_i))`

## 7. Per-Head Selection Comparison

**Methods compared against per-head approaches:**

- **TidalDecode** (Yang et al., 2024): Uses "per-head top-k selection"
- **Quest** (Tang et al., 2024): Head-specific selections
- **Randomized Top-k** (Appendix A.1.1): "Random application of one query head's top-k tokens"
- **Head-to-Head** (Appendix A.1.1): "Direct utilization of top-k tokens for each individual head"

Figure 4 shows LessIsMore maintains 85%+ recall when selection occurs infrequently (Layer 2 only), while Head-to-Head drops significantly.

## 8. Models Evaluated

**Exact models:**
- Qwen3-4B
- Qwen3-8B  
- Qwen3-14B
- DeepSeek-R1-Distill-Llama-8B

**Additional models in appendices:**
- LongChat-7B-v1.5-32k (MHA architecture, Table 8)
- Llama-3-8B-Instruct-Gradient-1048k (Table 7)
- Llama-3.1-8B-Instruct (Table 7)

## 9. Benchmarks

**Primary reasoning benchmarks:**
- AIME-24, AIME-25
- GPQA-Diamond
- MATH500

**Additional benchmarks (appendices):**
- Needle-in-the-Haystack (10K, 32K, 100K contexts)
- LongBench (5 datasets: MFQA, Qasper, HotpotQA, TriviaQA, PassageRetrieval-en)

## 10. Exact Speedup Numbers

**End-to-end decoding (Figure 6a, DeepSeek-R1-8B):**
- 16K context: 1.1× speedup
- 32K context: 1.3× speedup
- 64K context: 1.6× speedup

**Kernel-level sparse attention (Figure 6b):**
- Consistent 1.3×–1.72× speedup vs TidalDecode across token budgets

**SGLang serving (Table 3):**
- Up to 1.51× TBT speedup at 64K context

**Sparsity achieved:** "87.5% sparsity on AIME-24 with no accuracy loss"

## 11. Limitations Section

**Notable absence**: The paper contains NO explicit "Limitations" section.

**Implicit limitations evident:**

- Only tested on GQA-based models primarily (MHA generalization relegated to appendix)
- Requires full attention layers early in model (first 2 layers)
- Fixed recency ratio r=0.25 (though ablations in A.1.2 explore alternatives)
- "Infrequent re-selection works" validated empirically (Figure 4) but lacks theoretical guarantees

## 12. Speculative Decoding / Draft Models

**No mention** of speculative decoding, draft models, or temporal prediction anywhere in the paper.

## 13. Token Selection vs. Attention Score Prediction

The paper **does not discuss** this distinction explicitly.

**Method is explicitly "token selection"**: They select concrete token indices based on query-key products P=q·C.K^T, not predictive models.

Selection is **not** attention score prediction—it uses exact attention scores from the current query to rank tokens.

## 14. Paper Structure & Section Headings

1. Introduction
2. Observation: Attention Pattern in Long-Horizon Reasoning
   - 2.1 Background: Attention Recall as Diagnostic Metric
   - 2.2 Failure of Existing Sparse Attention in Reasoning
   - 2.3 Spatial Locality Across Attention Heads
   - 2.4 Temporal Recency Locality
3. LessIsMore
   - 3.1 Cross-Head Unified Sparse Attention (CUSA)
   - 3.2 Cross-Head Unified Token Selection
   - 3.3 Stable Recency Preservation
   - 3.4 Why Infrequent Re-Selection Works
4. Experiments
5. Related Work
6. Conclusion
Appendix A (extensive ablations and supplementary results)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4322bad-2807-47d7-a1e5-6d1239065f66",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "af260041-6aad-4439-84ad-a317e96b4b32",
  "sourceToolAssistantUUID": "e4322bad-2807-47d7-a1e5-6d1239065f66",
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

_source line 22 · 2026-05-10T20:59:41.703Z_

Let me search for citations and related work more specifically, and also try to access the Semantic Scholar and Google Scholar pages for this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af260041-6aad-4439-84ad-a317e96b4b32",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZTXRkkNFkWfdUTbb4Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df91d64a-bb39-4b2c-b351-83629724cef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GQUAabjnafYN5p67oV3PZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 653,
      "cache_creation_input_tokens": 2748,
      "cache_read_input_tokens": 14502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2748,
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

_source line 23 · 2026-05-10T20:59:42.649Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CSidd8quSwkLsN2ASM6VfT`</summary>

```json
{
  "query": "\"2508.07101\" cited by papers 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df91d64a-bb39-4b2c-b351-83629724cef3",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZTXRkkNFkWfdUTbb4Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "981496ae-ee30-4514-95f2-3c25d2998035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GQUAabjnafYN5p67oV3PZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 653,
      "cache_creation_input_tokens": 2748,
      "cache_read_input_tokens": 14502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2748,
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

_source line 24 · 2026-05-10T20:59:43.600Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sgmt5JbwAmmjULJ7ZFrnKE`</summary>

```json
{
  "query": "per-head vs unified attention sparse token selection reasoning counterargument adaptive 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "981496ae-ee30-4514-95f2-3c25d2998035",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZTXRkkNFkWfdUTbb4Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5836bf0a-ab5a-4008-a0a0-36de94936a65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GQUAabjnafYN5p67oV3PZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 653,
      "cache_creation_input_tokens": 2748,
      "cache_read_input_tokens": 14502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2748,
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

_source line 25 · 2026-05-10T20:59:49.196Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014vM49LysCjABkDmRnd9d58`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.07101v2",
  "prompt": "Focus specifically on:\n1. Section 2.3 \"Spatial Locality Across Attention Heads\" - extract the exact claims and evidence about cross-head overlap. What specific overlap percentages or metrics do they report?\n2. Section 3.4 \"Why Infrequent Re-Selection Works\" - what is their argument here?\n3. Any discussion of WHERE their method applies: is it only during the generation/decoding phase? Does it apply to speculative decoding setups?\n4. The exact definition of their \"attention recall\" metric (Equation 3)\n5. Any claims about per-head adaptive methods being suboptimal - exact quotes if possible\n6. What do they say about GQA (Grouped Query Attention) vs MHA (Multi-Head Attention)?\n7. The Related Work section - do they mention speculative decoding at all?\n8. Their conclusion - what future directions do they suggest?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5836bf0a-ab5a-4008-a0a0-36de94936a65",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZTXRkkNFkWfdUTbb4Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58a18062-71b5-4dff-bf52-527540502f58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GQUAabjnafYN5p67oV3PZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 653,
      "cache_creation_input_tokens": 2748,
      "cache_read_input_tokens": 14502,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2748
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 653,
          "output_tokens": 425,
          "cache_read_input_tokens": 14502,
          "cache_creation_input_tokens": 2748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2748,
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

_source line 26 · 2026-05-10T20:59:50.187Z_

<details><summary>↩ Tool result · `toolu_01Sgmt5JbwAmmjULJ7ZFrnKE`</summary>

```text
Web search results for query: "per-head vs unified attention sparse token selection reasoning counterargument adaptive 2025 2026"

Links: [{"title":"Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection","url":"https://arxiv.org/html/2602.03216v1"},{"title":"Paper page - Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection","url":"https://huggingface.co/papers/2602.03216"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://aclanthology.org/2025.acl-long.1126.pdf"},{"title":"TokenSelect: Efficient Long-Context Inference and Length ...","url":"https://aclanthology.org/2025.emnlp-main.1079.pdf"},{"title":"Token Sparse Attention: Efficient Long-Context Inference ...","url":"https://www.arxiv.org/pdf/2602.03216"},{"title":"Long-Context Generalization with Sparse Attention | OpenReview","url":"https://openreview.net/forum?id=PsB6Lynznk"},{"title":"[2602.03216] Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection","url":"https://arxiv.org/abs/2602.03216"},{"title":"[2502.11089] Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://arxiv.org/abs/2502.11089"},{"title":"[2506.16640] Long-Context Generalization with Sparse Attention","url":"https://arxiv.org/abs/2506.16640"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://arxiv.org/pdf/2502.11089"}]

Based on the search results, I found relevant recent research (2025-2026) on per-head versus unified attention approaches in sparse token selection for long-context LLMs:

## Key Findings

**Per-Head vs. Unified Attention:**

Head-wise selection enables fine-grained, head-specific token sets, avoiding the rigid unified token constraint of eviction-based methods. This is a central argument in favor of per-head approaches.

However, there are important counterarguments from a modern architecture perspective. Methods that fail to adapt to modern decoding efficient architectures like Multiple-Query Attention (MQA) and Grouped-Query Attention (GQA), where each attention head independently selects its KV-cache subset, face a different scenario in GQA models where the memory access volume of KV-cache corresponds to the union of selections from all query heads within the same GQA group, meaning that while these methods can reduce computation operations, the required KV-cache memory access remains relatively high.

**Adaptive Token Selection:**

Recent methods like Token Sparse Attention propose a middle ground: Token Sparse Attention compresses per-head Q,K,V to a reduced token set during attention and then decompresses the output back to the original sequence, enabling token information to be reconsidered. This advantage is attributed to layer-wise dynamic budget allocation and reversible interleaving, where tokens skipped in one attention operation remain available via the residual path.

The research from 2025-2026 suggests that while per-head selection offers fine-grained control, practical implementations must account for modern attention architectures (GQA/MQA) where unified or hierarchical approaches may be more efficient for memory access patterns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5836bf0a-ab5a-4008-a0a0-36de94936a65",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "b62ea9fb-3139-42a4-bc41-04a1ab7199a6",
  "sourceToolAssistantUUID": "5836bf0a-ab5a-4008-a0a0-36de94936a65",
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

_source line 27 · 2026-05-10T20:59:56.165Z_

<details><summary>↩ Tool result · `toolu_01CSidd8quSwkLsN2ASM6VfT`</summary>

```text
Web search results for query: ""2508.07101" cited by papers 2025 2026"

Links: [{"title":"Notice to Legal Services Corporation Grantees of Application Process for Making 2025 Mid-Year and 2026 Basic Field Fund Subgrants, 17470-17471 [2025-07101] :: Legal Services Corporation :: Agencies And Commissions :: Regulation Tracker :: Justia","url":"https://regulations.justia.com/regulations/fedreg/2025/04/25/2025-07101.html"},{"title":"2025 Author Guidelines - CVPR 2026","url":"https://cvpr.thecvf.com/Conferences/2025/AuthorGuidelines"},{"title":"World University Rankings 2026 methodology | Times Higher Education (THE) 1","url":"https://www.timeshighereducation.com/sites/default/files/breaking_news_files/the_world_university_rankings_2026_methodology.pdf"},{"title":"Google Scholar names its most influential papers for 2025 | News | Nature Index","url":"https://www.nature.com/nature-index/news/google-scholar-reveals-most-influential-research-papers-citations-twenty-twenty-five"},{"title":"Papers - ACM CHI 2026","url":"https://chi2026.acm.org/authors/papers/"},{"title":"2024–2025 Reviewer Thank You - 2026 - PM&R - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/pmrj.70111"},{"title":"Papers - CHI 2025 - ACM","url":"https://chi2025.acm.org/for-authors/papers/"},{"title":"Journal Citation Reports 2025 Statistics | Clarivate","url":"https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/infographic/"},{"title":"Looking at the 2026 EDUCAUSE Top 10 through a library ...","url":"https://www.tandfonline.com/doi/pdf/10.1080/07317131.2025.2599621"},{"title":"1 United Nations Commission on Science and Technology for Development","url":"https://unctad.org/system/files/information-document/cstd2025-2026_issues_ai_en.pdf"}]

The search results don't contain specific information about the paper "2508.07101" or citations to it. The results appear to be about federal regulations, conference guidelines, and general information about papers and citations in 2025-2026, but nothing specifically about the arxiv paper ID "2508.07101" that you're looking for.

Let me try a more specific search:

Links: [{"title":"[2508.07101] Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/abs/2508.07101"},{"title":"Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/html/2508.07101"},{"title":"Paper page - Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://huggingface.co/papers/2508.07101"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=1191&show=1000"},{"title":"Computer Science Aug 2025","url":"https://www.arxiv.org/list/cs/2025-08?skip=3825&show=25"},{"title":"[2604.07101] SurFITR: A Dataset for Surveillance Image Forgery Detection and Localisation","url":"https://arxiv.org/abs/2604.07101"},{"title":"[2512.07101] Wigner's Frame - Quantum Physics","url":"https://arxiv.org/abs/2512.07101"},{"title":"Inverse problems for history-enriched linear model reduction","url":"https://arxiv.org/html/2601.07101"},{"title":"[2508.07871] CATP: Contextually Adaptive Token Pruning for Efficient and Enhanced Multimodal In-Context Learning","url":"https://arxiv.org/abs/2508.07871"},{"title":"Contents","url":"https://arxiv.org/html/2508.12818"}]

Great! I found the paper. Now let me search for citations to this paper in 2025 and 2026:

Links: [{"title":"[2508.07101] Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/abs/2508.07101"}]

Based on my web search, I found that the paper 2508.07101 is titled "Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning" by authors Lijie Yang, Zhihao Zhang, Arti Jain, Shijie Cao, Baihong Yuan, Yiwei Chen, Zhihao Jia, and Ravi Netravali, submitted on August 9, 2025.

The paper addresses the problem of large reasoning models incurring substantial computational overhead from excessive token generation. While sparse attention mechanisms can reduce latency and memory usage, existing approaches suffer from significant accuracy degradation, and these methods generally require either high token retention rates or expensive retraining.

Unfortunately, the search results did not return specific information about papers that have cited 2508.07101 in 2025 and 2026. Since this paper was only submitted in August 2025, it may not have accumulated many citations yet, or citation databases may not yet have indexed all the citing papers. For a more comprehensive list of citations, you might want to check:

- ArXiv's citation network directly
- Google Scholar citations page for this paper
- Semantic Scholar or other academic citation tracking services


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "981496ae-ee30-4514-95f2-3c25d2998035",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "7d7f6af3-501d-439a-9a00-8afe989047b3",
  "sourceToolAssistantUUID": "981496ae-ee30-4514-95f2-3c25d2998035",
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

_source line 28 · 2026-05-10T21:00:00.133Z_

<details><summary>↩ Tool result · `toolu_014vM49LysCjABkDmRnd9d58`</summary>

```text
# Analysis of "Less Is More: Fast and Accurate Reasoning with Cross-Head Unified Sparse Attention"

## 1. Spatial Locality Claims (Section 2.3)

The paper identifies "substantial overlap in token importance rankings across heads" but does not provide specific quantitative percentages. Instead, they rely on Figure 2's visualization showing "dark blue positions indicate tokens included in the ground-truth top-4K budget" with overlapping regions marked by different colors to represent shared attention patterns across the 32 attention heads in Qwen3-8B.

## 2. Infrequent Re-Selection Argument (Section 3.4)

Their core claim: "because CUSA produces globally consistent and temporally stable token indices, the selected set ρ remains valid across multiple subsequent layers" without requiring frequent recalculation. Figure 4 empirically demonstrates that locally-optimized per-head strategies degrade rapidly with infrequent selection, whereas LessIsMore "maintains high attention recall even when selection is applied only once early in Layer 2."

## 3. Application Scope

The method applies specifically to the **decoding/generation phase** of inference. The paper states: "LessIsMore is a training-free sparse attention mechanism for long-horizon reasoning" focused on reducing "latency and memory usage" during "long decoding from short prompts." No discussion of speculative decoding appears in the provided content.

## 4. Attention Recall Definition (Equation 3)

> "Ri=∑(softmax(Wi)[ρ])/∑(softmax(Wi))" - the "fraction of attention mass retained by the selected tokens."

This measures what proportion of the full attention distribution is captured by the sparse token subset ρ.

## 5. Critique of Per-Head Methods

They explicitly state: "per-head top-k selection yields only a local optimum, overfitting to head-specific noise while failing to capture globally salient tokens that remain important in future layers."

## 6. GQA vs MHA Discussion

LessIsMore is evaluated on **GQA-based models** (DeepSeek-R1-Distill-Llama-8B, Qwen3 family). For MHA, they test on LongChat-7B-v1.5-32k (Table 8), demonstrating generalization "beyond GQA-based architectures." Both perform well, though kernel-level optimizations specifically benefit GQA's grouped structure.

## 7. Related Work & Speculative Decoding

The Related Work section (Section 5) contains **no mention of speculative decoding**. It covers sparse attention, KV cache compression, and reasoning-specific methods, but does not address speculative generation or draft-model approaches.

## 8. Conclusion & Future Directions

Their conclusion emphasizes: "explicitly exploiting global attention structure is critical for efficient and accurate sparse attention in reasoning workloads, and suggest a promising direction for scaling reasoning models without sacrificing performance." They do not articulate specific future research directions beyond this directional statement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58a18062-71b5-4dff-bf52-527540502f58",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "ef6f824f-ac06-4870-89c8-3c1afd537f09",
  "sourceToolAssistantUUID": "58a18062-71b5-4dff-bf52-527540502f58",
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

_source line 29 · 2026-05-10T21:00:03.295Z_

Let me do one more targeted search for Semantic Scholar citations and for any work that specifically responds to LessIsMore's claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef6f824f-ac06-4870-89c8-3c1afd537f09",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZV5zcRFSMVjJgsh9RV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9d3fe5b-3f44-4a85-84d8-dd768e5c391b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5eLwgWRKLsedJA2Si5d6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4160,
      "cache_read_input_tokens": 17250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4160,
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

_source line 30 · 2026-05-10T21:00:05.248Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VEwB7wW6Qi5pP6MYrfPa1K`</summary>

```json
{
  "url": "https://api.semanticscholar.org/graph/v1/paper/ArXiv:2508.07101?fields=title,citationCount,citations.title,citations.externalIds,citations.year",
  "prompt": "Extract the citation count and list all papers that cite this work. Include their titles, years, and arXiv IDs if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9d3fe5b-3f44-4a85-84d8-dd768e5c391b",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZV5zcRFSMVjJgsh9RV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "243ea105-2338-4d43-b6ae-5a12b8ed87ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5eLwgWRKLsedJA2Si5d6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4160,
      "cache_read_input_tokens": 17250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4160,
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

_source line 31 · 2026-05-10T21:00:05.655Z_

<details><summary>↩ Tool result · reported error · `toolu_01VEwB7wW6Qi5pP6MYrfPa1K`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "243ea105-2338-4d43-b6ae-5a12b8ed87ad",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "62d1700c-24ff-4467-8e14-235b0bc9910b",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "243ea105-2338-4d43-b6ae-5a12b8ed87ad",
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

_source line 32 · 2026-05-10T21:00:05.932Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019g6ZCoTNJcBF16sHfA6kHo`</summary>

```json
{
  "query": "self-speculative decoding per-head adaptive attention sparse token importance global vs local 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62d1700c-24ff-4467-8e14-235b0bc9910b",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZV5zcRFSMVjJgsh9RV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1ca3f33-e439-4f79-9190-7db9e1e83852",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5eLwgWRKLsedJA2Si5d6p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4160,
      "cache_read_input_tokens": 17250,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4160
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 17250,
          "cache_creation_input_tokens": 4160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4160,
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

_source line 33 · 2026-05-10T21:00:14.137Z_

<details><summary>↩ Tool result · `toolu_019g6ZCoTNJcBF16sHfA6kHo`</summary>

```text
Web search results for query: "self-speculative decoding per-head adaptive attention sparse token importance global vs local 2025 2026"

Links: [{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641"},{"title":"Accelerating Large-Scale Reasoning Model Inference with ...","url":"https://arxiv.org/pdf/2512.01278"},{"title":"Accelerate Speculative Decoding with Sparse Computation in Verification","url":"https://arxiv.org/html/2512.21911"},{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"Tactic: Adaptive Sparse Attention with Clustering and Distribution Fitting for Long-Context LLMs","url":"https://arxiv.org/html/2502.12216v1"},{"title":"Efficient Sparse Attention needs Adaptive Token Release","url":"https://arxiv.org/html/2407.02328"},{"title":"Speculative Sampling — TensorRT-LLM","url":"https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html"},{"title":"MIXTURE OF ATTENTIONS FOR SPECULATIVE DECODING","url":"https://discovery.ucl.ac.uk/id/eprint/10212512/1/11328_Mixture_of_Attentions_Fo.pdf"},{"title":"SparseSpec: Sparse Computation Innovations","url":"https://www.emergentmind.com/topics/sparsespec"}]

I found relevant research on the topics you're interested in. Here's a summary of recent work combining self-speculative decoding with sparse attention mechanisms:

## Key Recent Papers (2025-2026)

### SpecAttn: Speculating Sparse Attention
SpecAttn is a training-free approach that integrates with speculative decoding to enable efficient sparse attention in pre-trained transformers, exploiting attention weights from the draft model to identify important tokens for the target model. The method employs KL divergence-based layer alignment, a GPU-optimized sorting-free algorithm for top-p token selection, and dynamic key-value cache pruning.

### SparseSpec: Self-Speculative Decoding with Sparse Attention
SparseSpec introduces sparse self-speculation where the same model serves as both draft and target, featuring PillarAttn that selects critical tokens by reusing verification-phase information. It co-designs three system innovations: a unified scheduler for batching, delayed verification for CPU/GPU overlap, and dynamic KV-cache management, achieving up to 2.13x throughput speedup.

### Sparse Verification in Speculative Decoding
Recent work proposes applying sparsification to attention, feed-forward networks, and MoE layers jointly, introducing importance-based sparse attention for multi-token verification with piecewise budget control, inter-layer retrieval reuse, and sparse MoE strategies.

### Tactic: Adaptive Sparse Attention
Tactic dynamically selects tokens based on cumulative attention scores rather than fixed budgets, ensuring token selection adapts to variations in attention sparsity across heads, layers, and contexts.

These approaches represent the state-of-the-art in combining per-head adaptive attention with sparse token selection in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1ca3f33-e439-4f79-9190-7db9e1e83852",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "add273fe-b616-4bfc-b5c4-173d657526a2",
  "sourceToolAssistantUUID": "a1ca3f33-e439-4f79-9190-7db9e1e83852",
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

_source line 34 · 2026-05-10T21:00:16.785Z_

Let me get more detail on the SpecAttn paper since it seems directly relevant to the intersection of speculative decoding and sparse attention.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "add273fe-b616-4bfc-b5c4-173d657526a2",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZW7s15eQivJVjttWg2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dd9df19-77c5-4a75-9edf-25feb5b4f4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwMyGcnGtqk7LFh3bj7Qts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 21410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1170,
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

_source line 35 · 2026-05-10T21:00:19.221Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BGqQyU2uMRruiwFJee9dGJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.27641",
  "prompt": "Extract the full abstract, authors, and key claims. Does this paper cite or respond to LessIsMore (2508.07101)? Does it argue for per-head or unified token selection? What is its relationship to speculative decoding?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dd9df19-77c5-4a75-9edf-25feb5b4f4c9",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZW7s15eQivJVjttWg2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78502646-0969-4dd2-a37c-f2813f32dd62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwMyGcnGtqk7LFh3bj7Qts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 21410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1170,
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

_source line 36 · 2026-05-10T21:00:20.089Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019YdgZbBKVma33BptoZ4DMC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.01278",
  "prompt": "Extract the full abstract, authors, and key claims. Does this paper cite or respond to LessIsMore (2508.07101)? Does it use per-head adaptive attention? What is its approach to self-speculative decoding with sparse attention?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78502646-0969-4dd2-a37c-f2813f32dd62",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZW7s15eQivJVjttWg2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74482aa7-3cf8-40c8-964d-b92c4cf10866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwMyGcnGtqk7LFh3bj7Qts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 21410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1170,
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

_source line 37 · 2026-05-10T21:00:21.114Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SgxH9rDdbRnukJK3x4qeRo`</summary>

```json
{
  "query": "\"LessIsMore\" OR \"Less Is More\" \"global locality\" sparse attention criticism limitation rebuttal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74482aa7-3cf8-40c8-964d-b92c4cf10866",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZW7s15eQivJVjttWg2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e2f9033-4e32-450a-a603-95ef4444b15e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwMyGcnGtqk7LFh3bj7Qts",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 21410,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1170
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 343,
          "cache_read_input_tokens": 21410,
          "cache_creation_input_tokens": 1170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1170,
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

_source line 38 · 2026-05-10T21:00:25.033Z_

<details><summary>↩ Tool result · `toolu_01BGqQyU2uMRruiwFJee9dGJ`</summary>

```text
# SpecAttn Paper Analysis

## Full Abstract
"Large Language Models (LLMs) face significant computational bottlenecks during inference due to the quadratic complexity of self-attention mechanisms, particularly as context lengths increase. We introduce SpecAttn, a novel training-free approach that seamlessly integrates with existing speculative decoding techniques to enable efficient sparse attention in pre-trained transformers. Our key insight is to exploit the attention weights already computed by the draft model during speculative decoding to identify important tokens for the target model, eliminating redundant computation while maintaining output quality. SpecAttn employs three core techniques: KL divergence-based layer alignment between draft and target models, a GPU-optimized sorting-free algorithm for top-p token selection from draft attention patterns, and dynamic key-value cache pruning guided by these predictions. By leveraging the computational work already performed in standard speculative decoding pipelines, SpecAttn achieves over 75% reduction in key-value cache accesses with a mere 15.29% increase in perplexity on the PG-19 dataset, significantly outperforming existing sparse attention methods."

## Author
**Harsh Shah**

## Key Claims
- Achieves "over 75% reduction in key-value cache accesses" with minimal quality loss
- "Training-free approach" requiring no model modification
- Outperforms existing sparse attention baselines significantly

## Citation Questions
**LessIsMore (2508.07101)**: The provided content does not reference this paper.

**Per-head vs. unified selection**: The abstract mentions "top-p token selection from draft attention patterns" but doesn't explicitly specify granularity level.

## Relationship to Speculative Decoding
SpecAttn is fundamentally parasitic on speculative decoding—it "seamlessly integrates with existing speculative decoding techniques," reusing computation from draft models to guide target model token selection rather than performing redundant attention calculations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78502646-0969-4dd2-a37c-f2813f32dd62",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "507c880e-99f0-4149-98b2-94e744a3844f",
  "sourceToolAssistantUUID": "78502646-0969-4dd2-a37c-f2813f32dd62",
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

_source line 39 · 2026-05-10T21:00:26.923Z_

<details><summary>↩ Tool result · `toolu_019YdgZbBKVma33BptoZ4DMC`</summary>

```text
# Analysis of arXiv:2512.01278

## Full Abstract
"Reasoning language models have demonstrated remarkable capabilities on challenging tasks by generating elaborate chain-of-thought (CoT) solutions. However, such lengthy generation shifts the inference bottleneck from compute-bound to memory-bound. To generate each token, the model applies full attention to all previously generated tokens, requiring memory access to an increasingly large KV-Cache. Consequently, longer generations demand more memory access for every step, leading to substantial pressure on memory bandwidth. To address this, we introduce SparseSpec, a speculative decoding framework that reuses the same model as the draft and target models (i.e., self-speculation). SparseSpec features a novel sparse attention mechanism, PillarAttn, as the draft model, which accurately selects critical tokens via elegantly reusing information from the verification stage. Furthermore, SparseSpec co-designs self-speculation with three system innovations: (1) a unified scheduler to batch token drafting and verification, (2) delayed verification for CPU/GPU overlap, and (3) dynamic KV-Cache management to maximize memory utilization."

## Authors
Yilong Zhao, Jiaming Tang, Kan Zhu, Zihao Ye, Chi-Chih Chang, Chaofan Lin, Jongseok Park, Guangxuan Xiao, Mohamed S. Abdelfattah, Mingyu Gao, Baris Kasikci, Song Han, Ion Stoica

## Citation Information
The provided page content does not include references or bibliography sections, so I cannot confirm whether it cites LessIsMore (2508.07101).

## Key Technical Approach
- **Self-Speculative Mechanism**: Uses the same model for both draft and target roles
- **Sparse Attention (PillarAttn)**: Selectively identifies important tokens by reusing verification-stage information
- **System Co-Design**: Integrates unified scheduling, delayed verification, and adaptive KV-Cache management
- **Performance**: Achieves up to 2.13x throughput speedup

## Per-Head Adaptive Attention
The page content does not mention per-head adaptive attention mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74482aa7-3cf8-40c8-964d-b92c4cf10866",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "9fc1b215-8516-4e1d-9c37-8f87c926554d",
  "sourceToolAssistantUUID": "74482aa7-3cf8-40c8-964d-b92c4cf10866",
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

_source line 40 · 2026-05-10T21:00:27.961Z_

<details><summary>↩ Tool result · `toolu_01SgxH9rDdbRnukJK3x4qeRo`</summary>

```text
Web search results for query: ""LessIsMore" OR "Less Is More" "global locality" sparse attention criticism limitation rebuttal 2026"

Links: [{"title":"[2508.07101] Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/abs/2508.07101"},{"title":"Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://arxiv.org/html/2508.07101v1"},{"title":"Paper page - Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://huggingface.co/papers/2508.07101"},{"title":"Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning - haebom","url":"https://slashpage.com/haebom/4z7pvx2k1vjey2ek8653"},{"title":"GitHub - DerrickYLJ/LessIsMore: Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning","url":"https://github.com/DerrickYLJ/LessIsMore"},{"title":"Sparse Attention","url":"https://www.aussieai.com/research/sparse-attention"},{"title":"fly51fly on X: \"[CL] Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning L Yang, Z Zhang, A Jain, S Cao... [Princeton University &amp; CMU] (2025) https://t.co/slnA2lZaef https://t.co/HGGShJhuF3\" / X","url":"https://x.com/fly51fly/status/1955397036414734753"},{"title":"Less is More: Fewer Interpretable Region via Submodular Subset Selection | OpenReview","url":"https://openreview.net/forum?id=jKTUlxo5zy"},{"title":"VIDEONSA: NATIVE SPARSE ATTENTION SCALES ...","url":"https://openreview.net/pdf/05943dbd6b808ccbffb5488718a1c9f50bcc7069.pdf"},{"title":"Less is more: A closer look at semantic-based few-shot learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1566253524004500"}]

Based on the search results, I found information about the "Less Is More" paper and LessIsMore method. Here's what I found:

## LessIsMore Overview

LessIsMore is a training-free sparse attention mechanism for reasoning tasks, which leverages global attention patterns rather than relying on traditional head-specific local optimizations.

## Key Innovation with Global Locality

The method leverages two key observations: (1) attention heads in reasoning tasks show significant overlap in which tokens they find important (spatial locality), and (2) recently generated tokens consistently receive high attention across multiple future steps (recency locality).

## Performance Results

Evaluation across diverse reasoning tasks and benchmarks shows that LessIsMore preserves -- and in some cases improves -- accuracy while achieving a 1.1× average decoding speed-up compared to full attention. Moreover, LessIsMore attends to 2× fewer tokens without accuracy loss, achieving a 1.13× end-to-end speed-up compared to existing sparse attention methods.

## Addressing Limitations

The key insight is that existing sparse attention methods fail on reasoning tasks because they make localized token selection decisions for each attention head separately, leading to accumulated errors over long reasoning sequences. LessIsMore addresses this by aggregating decisions globally across heads.

However, the search results did not contain specific criticisms, limitations, or rebuttals of the LessIsMore approach from other researchers in 2026. The results mainly present the method's own contributions and claims.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e2f9033-4e32-450a-a603-95ef4444b15e",
  "isSidechain": true,
  "promptId": "c480a951-78b1-4276-a180-d052549dd2ba",
  "agentId": "ab24a9630119d9066",
  "type": "user",
  "uuid": "5375fa3b-2d98-4687-9b28-28abe8400ab1",
  "sourceToolAssistantUUID": "5e2f9033-4e32-450a-a603-95ef4444b15e",
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

_source line 41 · 2026-05-10T21:01:41.694Z_

I now have comprehensive information. Here is my detailed report.

---

## Deep Research Report: LessIsMore (arXiv:2508.07101)

### Paper Identity

- **Title**: "Less Is More: Training-Free Sparse Attention with Global Locality for Efficient Reasoning"
- **Authors**: Lijie Yang, Zhihao Zhang, Arti Jain, Shijie Cao, Baihong Yuan, Yiwei Chen, Zhihao Jia, Ravi Netravali (Princeton University & CMU)
- **Submitted**: August 9, 2025 (v1); revised April 27, 2026 (v2)
- **Venue**: Submitted to ICLR 2026 (OpenReview ID: 3iwDzfIk60)
- **Code**: https://github.com/DerrickYLJ/LessIsMore

---

### Verbatim Abstract (from the HTML version)

> "Large reasoning models achieve strong performance through test-time scaling, but this incurs substantial computational overhead due to long decoding from short prompts. While sparse attention can reduce latency and memory usage, existing methods often degrade reasoning accuracy because selection errors accumulate over long generation horizons, or require costly retraining. We introduce LessIsMore, a training-free sparse attention mechanism for long-horizon reasoning. Our key insight is that token importance in reasoning is global and stable: critical tokens are largely shared across attention heads and remain stable over decoding steps."

---

### Core Claim and Evidence

**Central thesis**: Token importance during reasoning is a *global* property, not a *head-local* one. Important tokens overlap substantially across all attention heads and remain stable over time.

**Evidence they provide**:

1. **Figure 2**: Visualizes ground-truth top-4K attended tokens across 32 attention heads in Qwen3-8B at decoding step 20K. They show "substantial overlap in token importance rankings both within key-value groups (yellow regions) and across all heads (red regions)."

2. **Attention Recall metric** (Equation 3): R_i = sum(softmax(W_i)[rho]) / sum(softmax(W_i)) -- measures the fraction of total attention mass captured by the selected sparse token subset. They show TidalDecode (per-head) achieves only ~75% recall on AIME-24, while LessIsMore maintains higher recall.

3. **Section 2.3 (Spatial Locality Across Attention Heads)**: Claims overlaps "persist across layers and decoding steps" with supporting figures in appendices.

4. **Section 2.4 (Temporal Recency Locality)**: "Recently generated tokens consistently receive high attention scores across all heads" and "the ratio between recent tokens and total critical tokens remains approximately constant."

**Explicit critique of per-head methods** (exact quote): "per-head top-k selection yields only a local optimum, overfitting to head-specific noise while failing to capture globally salient tokens that remain important in future layers."

---

### Method: How Unified Cross-Head Selection Works

The algorithm (Algorithm 1, Section 3) operates as follows:

1. **Full Attention Layers**: First 2 layers use standard dense attention
2. **Token Selection Layers (CUSA)**: Each head independently proposes top-k candidates. These proposals are aggregated via `UnionFlatten()` into a single ranked set, retaining top K(1-r) tokens globally.
3. **Stable Recency Window**: Reserve K*r most recent tokens (default r=0.25, so 25% of budget). The final selection is: `rho = rho_unified[:K(1-r)] UNION rho_recent`
4. **Sparse Attention Layers**: Reuse the computed indices from the selection layer across multiple subsequent layers (infrequent re-selection)

**Section 3.4 ("Why Infrequent Re-Selection Works")**: Because CUSA produces globally consistent and temporally stable token indices, the selected set remains valid across multiple subsequent layers without requiring frequent recalculation. Figure 4 shows locally-optimized per-head strategies degrade rapidly with infrequent selection, whereas LessIsMore "maintains high attention recall even when selection is applied only once early in Layer 2."

---

### Evaluation Setup

**Models evaluated**:
- Qwen3-4B, Qwen3-8B, Qwen3-14B (GQA architecture)
- DeepSeek-R1-Distill-Llama-8B (GQA architecture)
- LongChat-7B-v1.5-32k (MHA architecture, in appendix)
- Llama-3-8B-Instruct-Gradient-1048k, Llama-3.1-8B-Instruct (appendix)

**Benchmarks**:
- Primary reasoning: AIME-24, AIME-25, GPQA-Diamond, MATH500
- Long-context: Needle-in-the-Haystack (10K, 32K, 100K), LongBench (MFQA, Qasper, HotpotQA, TriviaQA, PassageRetrieval-en)

**Baselines compared against**:
- TidalDecode (per-head top-k selection)
- Quest (head-specific selections)
- Randomized Top-k, Head-to-Head (ablations in appendix)

---

### Speedup Numbers

- **End-to-end decoding** (DeepSeek-R1-8B): 1.1x at 16K context, 1.3x at 32K, up to **1.6x at 64K** context
- **Kernel-level sparse attention**: 1.3x-1.72x speedup vs TidalDecode
- **SGLang serving** (Table 3): Up to 1.51x TBT speedup at 64K context
- **Sparsity**: Up to 87.5% on AIME-24 with no accuracy loss
- **Accuracy**: Matches or exceeds full attention; avoids generation length inflation observed in prior sparse methods

---

### Limitations and Caveats

**The paper has NO explicit "Limitations" section.** This is notable. Implicit limitations:

1. **Only tested on GQA-based models primarily** -- MHA generalization is relegated to appendix
2. **Requires full attention on early layers** (first 2 layers always dense)
3. **Fixed recency ratio** r=0.25 (ablations explore alternatives but no adaptive mechanism)
4. **Empirically motivated only** -- no formal theorems or proofs, no theoretical guarantees for when infrequent re-selection is valid
5. **Modest speedups** -- the 1.1x average end-to-end speedup is relatively small; the headline 1.6x requires 64K+ contexts
6. **No evaluation on models larger than 14B parameters**
7. **Reasoning-specific** -- the "global and stable" property may not hold for non-reasoning tasks (they only claim it for reasoning)

---

### CRITICAL FINDING FOR YOUR WORK: What LessIsMore Does and Does NOT Address

**What LessIsMore addresses**: *Which tokens to attend to* -- i.e., token importance rankings / token selection for sparse attention during standard autoregressive decoding.

**What LessIsMore does NOT address**:
- **Speculative decoding** -- not mentioned anywhere in the paper, not in the method, not in related work
- **Attention score prediction** -- they use exact attention scores from the current query to rank tokens, not a predictive model
- **Draft models or draft steps** -- entirely outside their scope
- **Temporal prediction of how attention patterns evolve** -- their "temporal stability" observation is used only to justify *infrequent re-selection of the same indices*, not to predict future attention scores

**The fundamental distinction**: LessIsMore operates at the **token selection level** during standard (non-speculative) decoding. It asks "given a query, which KV cache entries should I attend to?" and answers "use a unified cross-head ranking instead of per-head rankings."

Your DecompSpec method operates at the **temporal prediction mechanism level** -- "how do attention scores evolve across speculative draft steps, and can we predict them per-head adaptively?" These are orthogonal axes:

| Dimension | LessIsMore | DecompSpec (yours) |
|-----------|-----------|-------------------|
| Task | Token selection for sparse attention | Attention score prediction for draft steps |
| Setting | Standard autoregressive decoding | Self-speculative decoding |
| What varies | Which tokens to attend to | How to predict attention across draft steps |
| Per-head vs unified | Unified (cross-head) | Per-head adaptive |
| Training | Training-free | (your approach) |

---

### Follow-up Work and Citations

I was unable to find papers that directly cite or respond to LessIsMore. The paper is relatively recent (Aug 2025), submitted to ICLR 2026, and citation databases have not yet indexed significant follow-up work.

However, two highly relevant contemporaneous papers at the intersection of sparse attention and speculative decoding exist:

1. **SpecAttn** (arXiv:2510.27641) -- exploits draft model attention weights to identify important tokens for the target model during speculative decoding. This is closer to your problem space.

2. **SparseSpec** (arXiv:2512.01278) -- a self-speculative decoding framework with PillarAttn that selects critical tokens by reusing verification-stage information. Achieves 2.13x throughput speedup. This is the most directly relevant comparison to your work.

---

### Positioning Advice for Your DecompSpec Paper

The reviewer's concern can be addressed on two levels:

1. **Scope mismatch**: LessIsMore addresses token *selection* (which KV entries to attend to) during standard decoding. Your work addresses attention score *prediction* during speculative draft steps. Their "global and stable" finding is about which tokens matter, not about how attention scores should be predicted across draft steps. These are different mechanisms solving different problems.

2. **Even if the analogy held**: LessIsMore's "global and stable" observation is specifically about *token importance rankings being shared across heads at the same decoding step*. It says nothing about whether the *temporal dynamics* of how attention patterns evolve across multiple draft steps are head-uniform or head-specific. Per-head adaptive temporal prediction could be necessary even if the static token importance ranking is globally shared -- because different heads may evolve at different rates across draft steps.

3. **Their own evidence suggests head-level differences exist**: They use `UnionFlatten()` to aggregate per-head proposals precisely because heads do propose *different* candidates -- the overlap is substantial but not total. The "noise" they dismiss as head-specific may contain exactly the temporal dynamics your method captures.

Sources:
- [LessIsMore arXiv page](https://arxiv.org/abs/2508.07101)
- [LessIsMore HTML full paper](https://arxiv.org/html/2508.07101v2)
- [LessIsMore OpenReview (ICLR 2026)](https://openreview.net/forum?id=3iwDzfIk60)
- [LessIsMore GitHub](https://github.com/DerrickYLJ/LessIsMore)
- [HuggingFace paper page](https://huggingface.co/papers/2508.07101)
- [SpecAttn](https://arxiv.org/abs/2510.27641)
- [SparseSpec](https://arxiv.org/abs/2512.01278)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5375fa3b-2d98-4687-9b28-28abe8400ab1",
  "isSidechain": true,
  "agentId": "ab24a9630119d9066",
  "requestId": "req_011CauZX92yWLQrsUXmCkzLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8280f58c-013b-410d-b921-581810349dab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a323c789-4aa2-416f-8bdf-eb4dc8663029",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKH85rTMEmzPboLLaieD3E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2395,
      "cache_read_input_tokens": 22580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2395,
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
