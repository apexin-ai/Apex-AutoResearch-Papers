# Research conversation: Search for and read the paper "DeltaAttention" (arXiv 2505.11254). I need to understand: 1. What is the core idea of dis

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5d5e8078d2e31eff.jsonl`
- **Structured JSON:** [`9794c94532b5f1c74bb8.json`](../../sessions/97/9794c94532b5f1c74bb8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-10T20:10:44.722Z_

Search for and read the paper "DeltaAttention" (arXiv 2505.11254). I need to understand:
1. What is the core idea of distributional correction for sparse attention?
2. How does it correct distributional shift from Top-K truncation?
3. What is the overhead (~1.5% of full attention cost)?
4. Is it NeurIPS 2025 as claimed?

Use WebSearch to find it, then use WebFetch to read the abstract and method from the arXiv page. Report the key findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a5d5e8078d2e31eff",
  "type": "user",
  "uuid": "3f02b423-9827-4001-84c6-cc8adba81d5e",
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

_source line 2 · 2026-05-10T20:10:44.724Z_

```json
{
  "parentUuid": "3f02b423-9827-4001-84c6-cc8adba81d5e",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
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
  "uuid": "e13453bf-e798-4602-8ad3-18f7e62c3c1e",
  "timestamp": "2026-05-10T20:10:44.724Z",
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

_source line 3 · 2026-05-10T20:10:49.102Z_



I'll search for the paper and read it from arXiv. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e13453bf-e798-4602-8ad3-18f7e62c3c1e",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
  "requestId": "req_011CauVjEM5LmBiqnNWYo61C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba4c35d7-bdd8-4929-9af5-9fbed707b12c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014begJtYL1BbKVpdLPUsPoA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 677,
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

_source line 4 · 2026-05-10T20:10:49.375Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VQ5J8et3ghWVM4mdU4nmtg`</summary>

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
  "parentUuid": "ba4c35d7-bdd8-4929-9af5-9fbed707b12c",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
  "requestId": "req_011CauVjEM5LmBiqnNWYo61C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7572e55c-fbba-4a63-a017-7f5bcd25f56d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014begJtYL1BbKVpdLPUsPoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 8223,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 677
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 677,
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

_source line 5 · 2026-05-10T20:10:49.377Z_

<details><summary>↩ Tool result · `toolu_01VQ5J8et3ghWVM4mdU4nmtg`</summary>

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
  "parentUuid": "7572e55c-fbba-4a63-a017-7f5bcd25f56d",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a5d5e8078d2e31eff",
  "type": "user",
  "uuid": "8effa402-1e7c-4e00-8588-cd5867220856",
  "sourceToolAssistantUUID": "7572e55c-fbba-4a63-a017-7f5bcd25f56d",
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

_source line 6 · 2026-05-10T20:10:52.763Z_



Now let me search for the paper and fetch its arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8effa402-1e7c-4e00-8588-cd5867220856",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
  "requestId": "req_011CauVjaUYaM2bzUE2F6yoZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bb5dd39-dae1-4345-8270-cad359b986ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bwLa4NWR9XCW7S9ihQKdQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 7 · 2026-05-10T20:10:53.802Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019BWY7Cq9vpNRgn1oerAgBy`</summary>

```json
{
  "query": "DeltaAttention arXiv 2505.11254 distributional correction sparse attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bb5dd39-dae1-4345-8270-cad359b986ee",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
  "requestId": "req_011CauVjaUYaM2bzUE2F6yoZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6b5fa86-895c-412a-a986-5a5e37e635fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bwLa4NWR9XCW7S9ihQKdQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 8 · 2026-05-10T20:10:56.609Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SKKz875J6NGmZ6ugmANCf8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.11254",
  "prompt": "Extract the full abstract, the list of authors, the paper title, the submission date, and any mention of conference acceptance (e.g. NeurIPS 2025). Also extract the key method description if visible on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6b5fa86-895c-412a-a986-5a5e37e635fa",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
  "requestId": "req_011CauVjaUYaM2bzUE2F6yoZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9afaa97-4737-447f-b11a-f4bd03bb256f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bwLa4NWR9XCW7S9ihQKdQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8900,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 8900,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 9 · 2026-05-10T20:11:00.934Z_

<details><summary>↩ Tool result · `toolu_019BWY7Cq9vpNRgn1oerAgBy`</summary>

```text
Web search results for query: "DeltaAttention arXiv 2505.11254 distributional correction sparse attention"

Links: [{"title":"[2505.11254] Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction","url":"https://arxiv.org/abs/2505.11254"},{"title":"𝚫 Attention: Fast and Accurate Sparse Attention Inference by Delta Correction","url":"https://arxiv.org/html/2505.11254"},{"title":"Paper page - Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction","url":"https://huggingface.co/papers/2505.11254"},{"title":"arXiv:2505.11254v1 [cs.LG] 16 May 2025","url":"https://www.arxiv.org/pdf/2505.11254"},{"title":"Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.11254v1"},{"title":"∆Attention: Fast and Accurate Sparse Attention Inference by Delta Correction","url":"https://openreview.net/pdf/6fbc5290ef9f74929813563e512225b32f29ffe5.pdf"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=950&show=1000"},{"title":"NeurIPS Poster Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction","url":"https://neurips.cc/virtual/2025/poster/118545"},{"title":"(PDF) Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction","url":"https://www.researchgate.net/publication/391857051_Delta_Attention_Fast_and_Accurate_Sparse_Attention_Inference_by_Delta_Correction"},{"title":"Sparse Attention","url":"https://www.aussieai.com/research/sparse-attention"}]

Based on the search results, here's what I found about DeltaAttention (arXiv 2505.11254):

## Overview

Delta Attention is a paper by Jeffrey Willette, Heejun Lee, and Sung Ju Hwang, addressing a fundamental problem in sparse attention mechanisms.

## The Problem

Sparse attention inference methods aim to reduce computational burden, but they come with a troublesome performance degradation that arises from a distributional shift in the attention outputs. The distributional shift causes decoding-time queries to fail to align well with the appropriate keys from the prefill stage, leading to a drop in performance.

## The Solution

The paper proposes a simple, novel, and effective procedure for correcting this distributional shift, bringing the distribution of sparse attention outputs closer to that of quadratic attention. ΔAttention is a sparse post-processing correction that realigns sparse outputs with full quadratic attention.

## Key Results

The method can be applied on top of any sparse attention method, and results in an average 36 percentage point performance increase, recovering 88% of quadratic attention accuracy on the 131K RULER benchmark when applied on top of sliding window attention with sink tokens while only adding a small overhead. The method can maintain approximately 98.5% sparsity over full quadratic attention, making the model 32 times faster than Flash Attention 2 when processing 1M token prefills.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6b5fa86-895c-412a-a986-5a5e37e635fa",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a5d5e8078d2e31eff",
  "type": "user",
  "uuid": "47ef413d-e11c-473b-bb98-03882aaa4fa2",
  "sourceToolAssistantUUID": "e6b5fa86-895c-412a-a986-5a5e37e635fa",
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

_source line 10 · 2026-05-10T20:11:01.178Z_

<details><summary>↩ Tool result · `toolu_01SKKz875J6NGmZ6ugmANCf8`</summary>

```text
# Paper Summary: Delta Attention

**Title:** Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction

**Authors:** Jeffrey Willette, Heejun Lee, Sung Ju Hwang

**Submission Date:** Submitted May 16, 2025 (revised November 22, 2025)

**Conference Acceptance:** No conference acceptance mentioned on this page.

## Abstract
The paper addresses computational efficiency in transformer attention mechanisms. The researchers identify that sparse attention induces "a distributional shift in the attention outputs," causing performance degradation. Their proposed solution applies a correction procedure to align sparse attention distributions with standard quadratic attention. On the RULER benchmark (131K tokens), their approach achieves "an average 36%pt performance increase" while maintaining approximately 98.5% sparsity, resulting in "32 times faster" performance than Flash Attention 2 on 1M token prefills.

## Key Method
Delta Attention corrects distributional misalignment between sparse and dense attention computations, enabling the method to work as a plug-in improvement over existing sparse attention techniques like sliding window attention with sink tokens.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9afaa97-4737-447f-b11a-f4bd03bb256f",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a5d5e8078d2e31eff",
  "type": "user",
  "uuid": "8cd7c9a7-5317-4cf0-b5c0-07c3c5030067",
  "sourceToolAssistantUUID": "b9afaa97-4737-447f-b11a-f4bd03bb256f",
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

_source line 11 · 2026-05-10T20:11:04.381Z_

Good, I have the overview. Now let me fetch the HTML version for more detailed method description.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cd7c9a7-5317-4cf0-b5c0-07c3c5030067",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
  "requestId": "req_011CauVkSgGC84UsQt3oEHMa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2c13239-a4d2-4a58-ae1c-75e6a69242cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKzRFLpmvFTEGhbGAqTLV9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 10813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1359,
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

_source line 12 · 2026-05-10T20:11:08.596Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019g4egp235fK8wV88N2M3bq`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.11254",
  "prompt": "Extract the detailed method/approach section. Specifically I need:\n1. How does the distributional shift from Top-K truncation occur? What is the mathematical explanation?\n2. What exactly is the 'delta correction' - how does it work step by step?\n3. What is the overhead cost (~1.5% of full attention cost) - how is this computed and what operations contribute to it?\n4. Any mention of NeurIPS 2025 acceptance.\n5. The core formula or algorithm for Delta Attention.\nPlease be thorough and extract the technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2c13239-a4d2-4a58-ae1c-75e6a69242cd",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
  "requestId": "req_011CauVkSgGC84UsQt3oEHMa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15664958-f619-4e19-a45a-884e7aef5851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKzRFLpmvFTEGhbGAqTLV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 10813,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1359
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 10813,
          "cache_creation_input_tokens": 1359,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1359,
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

_source line 13 · 2026-05-10T20:11:20.351Z_

<details><summary>↩ Tool result · `toolu_019g4egp235fK8wV88N2M3bq`</summary>

````text
# Delta Attention: Technical Method Analysis

## 1. Distributional Shift from Sparse Attention

The paper identifies that sparse attention methods cause a **distributional shift in attention outputs**. The mathematical explanation centers on softmax normalization differences:

When sparse attention computes only a subset of attention scores, the softmax normalization constant differs from full attention. As stated: *"the softmax normalization of sparse attention methods generally only computes the normalization constant over the nonzero values"* (Equation 3).

Specifically, if full attention has normalization constant Z = H + T (head-sum plus tail-sum), sparse attention uses only T (tail-sum), ignoring the H (head-sum) from pruned entries. This causes sparse and dense attention to have different output distributions, misaligning queries with keys during decoding.

## 2. Delta Correction: Step-by-Step Process

The delta correction works through four key steps (Algorithm 1, Equation 6-7):

**Step 1:** Compute full sparse attention for all queries: **A\*V**

**Step 2:** Select every γth query (e.g., γ=64) and compute dense attention for this subset: **Ã V**

**Step 3:** Calculate the difference (delta term): *"Δ correction term = [ÃV - (A*V)floor(i/γ)γ]"*

**Step 4:** Broadcast this delta across the γ-sized window: *"(ÂV)ᵢ = (A*V)ᵢ + (AᐃV)floor(i/γ)γ"*

The intuition: *"the difference of attention outputs approximates the missing attention contribution"* from sparsified regions.

## 3. Overhead Cost Calculation (~1.5%)

The overhead derives from computing every γth row densely:

- Standard setting: γ = 64
- Per-row computation: window size (2048) + C/(2γ)
- For 131K context: 2048 + 2¹⁷/(2×2⁶) = 2048 + 1024 = 3072 tokens
- Overhead ratio: 1024/65536 ≈ **1.5% of full quadratic attention**

Operations contributing to overhead:
- Query subset selection (negligible)
- Dense attention recomputation for query subset (1.5% of full computation)
- Delta difference calculation (minimal)
- Broadcasting across windows (trivial scatter operation)

## 4. NeurIPS 2025 Status

**No explicit mention of acceptance appears in this content.** The paper is formatted as an arXiv submission (arxiv.org/html/2505.11254v2) and includes a NeurIPS checklist, suggesting submission intent, but acceptance status is not stated.

## 5. Core Algorithm and Formula

**Primary Formula (Equation 6-7):**

```
(ÂV)ᵢ = (A*V)ᵢ + [ÃV⌊i/γ⌋ - (A*V)⌊i/γ⌋γ]
```

Where:
- A*V = sparse attention output
- ÃV = dense attention for sampled queries
- The bracketed term = delta correction broadcast to γ neighbors

**Key Theoretical Result (Lemma 1):**

For top-k sparse attention: *"|Δ - Σᵢ₌₁ᴺ⁻ᵏ aᵢvᵢ| ≤ [H/(H+T)] × max|vᵢ|"*

This bounds the approximation error, showing tighter bounds when T ≫ H (good sparsity).
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15664958-f619-4e19-a45a-884e7aef5851",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a5d5e8078d2e31eff",
  "type": "user",
  "uuid": "fe20ad37-67b7-4f76-8230-d7c130e6de8b",
  "sourceToolAssistantUUID": "15664958-f619-4e19-a45a-884e7aef5851",
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

_source line 14 · 2026-05-10T20:11:22.770Z_

Now let me check the NeurIPS page directly to confirm the conference status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe20ad37-67b7-4f76-8230-d7c130e6de8b",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
  "requestId": "req_011CauVmreC8ywqqT36Kjcae",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8986cd47-b713-4f44-8a6a-c95abeda4ccf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9sWy948JZg69x2wHaRjtb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 12172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
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

_source line 15 · 2026-05-10T20:11:24.392Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0171q5mVNdNVKKunwTNQVuGK`</summary>

```json
{
  "url": "https://neurips.cc/virtual/2025/poster/118545",
  "prompt": "Confirm whether this paper (Delta Attention) was accepted at NeurIPS 2025. Extract any details about its presentation format (poster, oral, spotlight) and the conference year."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8986cd47-b713-4f44-8a6a-c95abeda4ccf",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
  "requestId": "req_011CauVmreC8ywqqT36Kjcae",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65845f25-f5b5-4e3e-ad14-12bb847aea55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9sWy948JZg69x2wHaRjtb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 12172,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1136
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 12172,
          "cache_creation_input_tokens": 1136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1136,
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

_source line 16 · 2026-05-10T20:11:27.608Z_

<details><summary>↩ Tool result · `toolu_0171q5mVNdNVKKunwTNQVuGK`</summary>

```text
# Delta Attention Paper Confirmation

**Acceptance Status:** Yes, the paper was accepted at NeurIPS 2025.

**Presentation Format:** Poster presentation

**Conference Year:** 2025

**Details:** The paper, titled "Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction," is authored by Jeffrey Willette, Heejun Lee, and Sung Ju Hwang. According to the page, it was scheduled as a "Poster Thu, Dec 4, 2025 • 11:00 AM – 2:00 PM PST" at the San Diego location of the conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65845f25-f5b5-4e3e-ad14-12bb847aea55",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a5d5e8078d2e31eff",
  "type": "user",
  "uuid": "4224b008-6bc4-447b-b9e7-4c452eb72406",
  "sourceToolAssistantUUID": "65845f25-f5b5-4e3e-ad14-12bb847aea55",
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

_source line 17 · 2026-05-10T20:11:53.596Z_

Here are the key findings from the paper.

---

**Paper:** *Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction* (arXiv 2505.11254)
**Authors:** Jeffrey Willette, Heejun Lee, Sung Ju Hwang

---

### 1. Core Idea of Distributional Correction for Sparse Attention

Sparse attention methods (Top-K, sliding window, etc.) prune away most attention scores to save computation. However, this pruning changes the softmax normalization constant. Full attention normalizes over all N keys (Z = H + T, where H is the sum over pruned/"head" entries and T is the sum over kept/"tail" entries), but sparse attention normalizes only over the kept entries (using T alone). This mismatch means the sparse attention output distribution diverges from that of full quadratic attention, causing decoding-time queries to misalign with the appropriate keys from prefill. Delta Attention corrects this by computing a cheap correction term that brings the sparse output distribution back toward the full-attention distribution.

### 2. How the Delta Correction Works (Step by Step)

The method is elegantly simple:

1. **Compute sparse attention** for all queries as usual: A*V (the standard sparse output).
2. **Sample every gamma-th query** (default gamma = 64) and compute **full dense attention** for just those sampled queries: tilde{A}V.
3. **Compute the delta** = (dense output - sparse output) for each sampled query. This difference captures the contribution of the pruned attention entries.
4. **Broadcast the delta** to all gamma neighbors: for query i, the corrected output is:

   `(corrected output)_i = (A*V)_i + [dense_output_{floor(i/gamma)} - sparse_output_{floor(i/gamma)}]`

The key insight is that the difference between dense and sparse outputs at a sampled query approximates the missing attention contribution from pruned regions, and this difference varies slowly across nearby queries, so broadcasting it across a window of gamma queries is a good approximation.

The approximation error is bounded (Lemma 1): `|delta - sum of pruned contributions| <= [H/(H+T)] * max|v_i|`, which is tight when sparsity is good (T >> H).

### 3. The ~1.5% Overhead

The overhead comes from recomputing dense attention for every 64th query (gamma = 64). At 131K context length:

- Each sampled query attends to the full context (rather than just the sparse window of ~2048 tokens).
- The additional cost per sampled row is roughly C/(2*gamma) = 131072 / 128 = 1024 extra tokens of attention.
- As a fraction of full quadratic attention: 1024 / 65536 ~ **1.5%**.

The operations contributing: (a) selecting the query subset (negligible), (b) dense attention for those queries (the 1.5%), (c) computing the difference and broadcasting (trivial). So the method maintains ~98.5% sparsity over full quadratic attention.

### 4. NeurIPS 2025 Status: Confirmed

Yes, the paper was **accepted at NeurIPS 2025** as a **poster presentation** (Thursday, December 4, 2025, San Diego). This is confirmed by the NeurIPS virtual site listing (poster #118545).

---

### Bottom Line

Delta Attention is a plug-in post-processing correction applicable to any sparse attention method. On the 131K RULER benchmark, it recovers an average of 36 percentage points of performance (reaching 88% of full quadratic attention accuracy) when applied on top of sliding window + sink tokens, at only ~1.5% additional cost. At 1M token prefills, this yields a 32x speedup over FlashAttention-2.

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2505.11254)
- [arXiv HTML Full Paper](https://arxiv.org/html/2505.11254)
- [NeurIPS 2025 Poster Page](https://neurips.cc/virtual/2025/poster/118545)
- [HuggingFace Paper Page](https://huggingface.co/papers/2505.11254)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4224b008-6bc4-447b-b9e7-4c452eb72406",
  "isSidechain": true,
  "agentId": "a5d5e8078d2e31eff",
  "requestId": "req_011CauVnPfk3SgLxfELVp1V9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cb6fe29-05fe-441d-8110-34fdb924fa8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P241nyBtqbmBbjhLAZowau",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 296,
      "cache_read_input_tokens": 13308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 296,
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
