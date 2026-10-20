# Research conversation: Search for the paper "Q-Infer" which is described as a GPU-CPU collaborative LLM inference system that coordinates both 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac2d475fdb055a07a.jsonl`
- **Structured JSON:** [`246a2a36bc85df5727d8.json`](../../sessions/24/246a2a36bc85df5727d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-10T18:21:32.528Z_

Search for the paper "Q-Infer" which is described as a GPU-CPU collaborative LLM inference system that coordinates both MLP neuron sparsity and KV cache compression, published in ACM TACO 2025. Verify it exists and understand its approach.

Also search for any papers from 2025-2026 that specifically propose using a SINGLE signal to drive BOTH MLP sparsity and KV cache decisions:
1. "Q-Infer GPU CPU MLP sparsity KV cache ACM TACO"
2. "unified signal MLP KV cache coordination LLM inference 2025 2026"  
3. "single metric MLP sparsity KV eviction transformer"
4. "cross-axis optimization MLP attention LLM inference"
5. "joint compute memory optimization LLM decoding"

Report what you find — especially whether Q-Infer or any other paper uses a unified redundancy signal across both axes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "0ee99967-acef-4672-8d5a-03e4157396d9",
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

_source line 2 · 2026-05-10T18:21:32.530Z_

```json
{
  "parentUuid": "0ee99967-acef-4672-8d5a-03e4157396d9",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
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
  "uuid": "cb84de5b-5086-4fa7-9494-59354ac80958",
  "timestamp": "2026-05-10T18:21:32.530Z",
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

_source line 3 · 2026-05-10T18:21:34.952Z_



I'll search for the Q-Infer paper and related work on unified MLP sparsity and KV cache coordination. Let me run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb84de5b-5086-4fa7-9494-59354ac80958",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMQEsceedbpv89E3rLg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab79988c-2de0-4ced-8e98-3841b03d3580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01755uefkr4hnQCgYW7g1Q36",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 769,
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

_source line 4 · 2026-05-10T18:21:35.768Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GrzgxGDiUbAWDc4XBW4pB3`</summary>

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
  "parentUuid": "ab79988c-2de0-4ced-8e98-3841b03d3580",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMQEsceedbpv89E3rLg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b803c81-3ca5-4537-8200-62eba5c24694",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01755uefkr4hnQCgYW7g1Q36",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 8223,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 769
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 769,
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

_source line 5 · 2026-05-10T18:21:35.770Z_

<details><summary>↩ Tool result · `toolu_01GrzgxGDiUbAWDc4XBW4pB3`</summary>

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
  "parentUuid": "7b803c81-3ca5-4537-8200-62eba5c24694",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "50ea00cf-8612-41b5-acd7-0979859057f0",
  "sourceToolAssistantUUID": "7b803c81-3ca5-4537-8200-62eba5c24694",
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

_source line 6 · 2026-05-10T18:21:38.783Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50ea00cf-8612-41b5-acd7-0979859057f0",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMQUzvjSaG7SAPLV9Pq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54d00970-113b-4a66-8c73-9532ad1b17d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EUsUd8cuY5oMN5QKjGNPRM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 8992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1429,
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

_source line 7 · 2026-05-10T18:21:39.419Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WbRnVfWu3b3n7UxPes85Lu`</summary>

```json
{
  "query": "Q-Infer GPU CPU MLP sparsity KV cache ACM TACO 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54d00970-113b-4a66-8c73-9532ad1b17d1",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMQUzvjSaG7SAPLV9Pq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce2cc8d8-5d6e-4cbb-b22a-f23c5cd13b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EUsUd8cuY5oMN5QKjGNPRM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 8992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1429,
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

_source line 8 · 2026-05-10T18:21:45.944Z_

<details><summary>↩ Tool result · `toolu_01WbRnVfWu3b3n7UxPes85Lu`</summary>

```text
Web search results for query: "Q-Infer GPU CPU MLP sparsity KV cache ACM TACO 2025"

Links: [{"title":"Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling | ACM Transactions on Architecture and Code Optimization","url":"https://dl.acm.org/doi/full/10.1145/3764589"},{"title":"Q-Infer: Towards Eficient GPU-CPU Collaborative LLM Inference via","url":"https://dl.acm.org/doi/pdf/10.1145/3764589"},{"title":"Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling","url":"https://www.researchgate.net/publication/395071810_Q-Infer_Towards_Efficient_GPU-CPU_Collaborative_LLM_Inference_via_Sparsity-Aware_Dynamic_Scheduling"},{"title":"An I/O Characterizing Study of Offloading LLM Models and KV Caches to NVMe SSD","url":"https://atlarge-research.com/pdfs/2025-cheops-llm.pdf"},{"title":"KVPR: Efficient LLM Inference with I/O-Aware KV Cache ...","url":"https://aclanthology.org/2025.findings-acl.997.pdf"},{"title":"Breaking the Boundaries of Long-Context LLM Inference: Adaptive KV Management on a Single Commodity GPU","url":"https://arxiv.org/html/2506.20187v1"},{"title":"Activation Sequence Caching: High-Throughput and ...","url":"https://dl.acm.org/doi/pdf/10.1145/3656019.3676945"},{"title":"HGCA: Hybrid GPU-CPU Attention for Long Context LLM Inference","url":"https://arxiv.org/html/2507.03153v1"},{"title":"GPU-Accelerated INT8 Quantization for KV Cache Compression in Large Language Models","url":"https://arxiv.org/html/2601.04719v1"},{"title":"Scalable Processing-Near-Memory for 1M-Token LLM Inference: CXL-Enabled KV-Cache Management Beyond GPU Limits","url":"https://arxiv.org/html/2511.00321v1"}]

The search has found detailed information about Q-Infer. Here are the key findings:

## Q-Infer Overview

Q-Infer is an efficient GPU-CPU collaborative inference system featured with sparsity-aware cache management and dynamic compute scheduling.

## Key Features

**Sparsity and KV Cache Management:**
By reducing the batch sizes of inputs in the GPU, the KV cache size can be reduced, and sparsity can be enhanced. Q-Infer dynamically selects a small number of key tokens from the entire Token Window via a multi-window mechanism, which quantifies the KV cache of unimportant tokens instead of discarding them directly.

**MLP Sparsity Exploitation:**
In the MLP blocks, since Q-Infer only calculates the activated neurons, Q-Infer prefetches only the most activated neurons (Top-K) to the GPU, leaving the remainder on the CPU. Q-Infer employs an online MLP predictor to predict the activated neurons in each Transformer layer.

## Performance

Q-Infer significantly outperforms state-of-the-art inference systems in terms of inference throughput, latency and accuracy.

## Publication

The research appears in ACM Transactions on Architecture and Code Optimization (ACM Trans. Arch. Code Optim.), which suggests it may be related to the ACM TACO 2025 conference/journal you mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce2cc8d8-5d6e-4cbb-b22a-f23c5cd13b45",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "7bc2ce64-f668-4969-923b-84dc1aaa4e32",
  "sourceToolAssistantUUID": "ce2cc8d8-5d6e-4cbb-b22a-f23c5cd13b45",
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

### Tool call

_source line 9 · 2026-05-10T18:21:49.481Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AHQn7W74aGFPndmwum8HSE`</summary>

```json
{
  "query": "unified signal MLP KV cache coordination LLM inference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bc2ce64-f668-4969-923b-84dc1aaa4e32",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMREJAguuWBEV6R25ec",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ec3097a-fab3-410b-97ba-cde41e6d5ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmfZmL4C2S8aAj6arQQ8G6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 10421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1043,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T18:21:50.057Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018vGkLLbc5PzWSHZ88wQHCP`</summary>

```json
{
  "query": "single metric MLP sparsity KV eviction transformer 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ec3097a-fab3-410b-97ba-cde41e6d5ec4",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMREJAguuWBEV6R25ec",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "680b201f-8643-4436-b5ac-5c046c922e89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmfZmL4C2S8aAj6arQQ8G6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 10421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1043,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T18:21:50.529Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XeSFPo8ezm6uzm3YHmWfSr`</summary>

```json
{
  "query": "cross-axis optimization MLP attention LLM inference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "680b201f-8643-4436-b5ac-5c046c922e89",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMREJAguuWBEV6R25ec",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca413cc1-6571-4079-9275-4da99d1d47b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmfZmL4C2S8aAj6arQQ8G6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 10421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1043,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T18:21:50.952Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EgD8i43JipyY7dnBcKnBny`</summary>

```json
{
  "query": "joint compute memory optimization MLP KV cache LLM decoding 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca413cc1-6571-4079-9275-4da99d1d47b9",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMREJAguuWBEV6R25ec",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40a158b2-20cd-4414-8215-859277182e66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmfZmL4C2S8aAj6arQQ8G6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 10421,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1043
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 10421,
          "cache_creation_input_tokens": 1043,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1043,
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

_source line 13 · 2026-05-10T18:21:58.141Z_

<details><summary>↩ Tool result · `toolu_01AHQn7W74aGFPndmwum8HSE`</summary>

```text
Web search results for query: "unified signal MLP KV cache coordination LLM inference 2025 2026"

Links: [{"title":"Multi-tier dynamic storage of KV cache for LLM inference under resource-constrained conditions | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02200-4"},{"title":"LMCACHE: AN EFFICIENT KV CACHE LAYER FOR ENTERPRISE-SCALE LLM INFERENCE","url":"https://lmcache.ai/tech_report.pdf"},{"title":"Master KV cache aware routing with llm-d for efficient AI inference | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/10/07/master-kv-cache-aware-routing-llm-d-efficient-ai-inference"},{"title":"LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference","url":"https://arxiv.org/pdf/2510.09665"},{"title":"LLM Inference Optimization: Quantization, KV Cache, and Serving at Scale - Perivitta Rajendran","url":"https://pr-peri.github.io/blogpost/2026/03/25/blogpost-llm-quantization-kv-cache.html"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"How to Cut LLM Inference Costs with KV Caching | Everpure Blog","url":"https://blog.everpuredata.com/purely-technical/cut-llm-inference-costs-with-kv-caching/"},{"title":"BanaServe: Unified KV Cache and Dynamic Module Migration for Balancing Disaggregated LLM Serving in AI Infrastructure - He - 2026 - Software: Practice and Experience - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/spe.70054?af=R"},{"title":"Customizing LLMs for Efficient Latency-Aware Inference at ...","url":"https://www.usenix.org/system/files/atc25-tian.pdf"}]

Based on the web search results, I found several relevant papers and resources about KV cache coordination and LLM inference optimization in 2025-2026:

## Key Research Findings

**QKVShare Framework**: QKVShare introduces a framework for quantized KV-cache handoff between LLM agents on edge devices that utilizes a topology-aware controller and a compact CacheCard representation to minimize re-prefill latency, employing a 2-layer MLP controller to assign per-token bit-widths based on local importance and cross-agent downstream demand signals.

**Adaptive KV-Cache Quantization**: A compact MLP controller for real-time quantization leverages readily available token-level features, including token frequency or rarity, quality score, attention variance, and entropy-based uncertainty, to select KV precision under strict memory and latency constraints. The method extracts lightweight token-level signals (e.g., token frequency, attention variance, and entropy-based uncertainty) and uses a learned MLP controller to assign per-token KV precision (2/4/8-bit or FP16) during decoding.

**BanaServe System**: BanaServe demonstrates that dynamic, multi-granularity resource rebalancing and cache-decoupled routing are essential for efficient disaggregated LLM serving, jointly addressing resource elasticity, stage imbalance, and cache-induced load skew.

**KV Cache Routing Coordination**: Cache routing requires coordination between your orchestration layer (whether that's vLLM, TensorRT-LLM, or a custom scheduler) and your cache storage backend to ensure that cache lookups account for both the content hash and the TP degree used to generate that cache.

These recent developments show active research in unified signal processing, MLP-based controllers, and coordinated KV cache management for efficient LLM inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ec3097a-fab3-410b-97ba-cde41e6d5ec4",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "75f1e31e-2ed0-4d07-9e3e-68641886190c",
  "sourceToolAssistantUUID": "6ec3097a-fab3-410b-97ba-cde41e6d5ec4",
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

_source line 14 · 2026-05-10T18:21:58.439Z_

<details><summary>↩ Tool result · `toolu_01XeSFPo8ezm6uzm3YHmWfSr`</summary>

```text
Web search results for query: "cross-axis optimization MLP attention LLM inference 2025"

Links: [{"title":"LLM Inference Optimization:. Breakthrough Techniques Reducing… | by Inference Weekly | Medium","url":"https://medium.com/@harshit.sinha0910/llm-inference-optimization-f720e71f5da0"},{"title":"Scaling LLM Inference: Innovations in Tensor Parallelism, Context Parallelism, and Expert Parallelism - Engineering at Meta","url":"https://engineering.fb.com/2025/10/17/ai-research/scaling-llm-inference-innovations-tensor-parallelism-context-parallelism-expert-parallelism/"},{"title":"Mastering LLM Techniques: Inference Optimization | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"GitHub - amitshekhariitbhu/llm-internals: Learn LLM internals step by step - from tokenization to attention to inference optimization. · GitHub","url":"https://github.com/amitshekhariitbhu/llm-internals"},{"title":"Rethinking LLM Inference Bottlenecks: Insights from Latent Attention and Mixture-of-Experts","url":"https://arxiv.org/html/2507.15465v3"},{"title":"A Survey of LLM Inference Systems","url":"https://arxiv.org/html/2506.21901v1"},{"title":"GitHub - xlite-dev/Awesome-LLM-Inference: 📚A curated list of Awesome LLM/VLM Inference Papers with Codes: Flash-Attention, Paged-Attention, WINT8/4, Parallelism, etc.🎉","url":"https://github.com/xlite-dev/Awesome-LLM-Inference"},{"title":"FastMTP: Accelerating LLM Inference with Enhanced Multi-Token Prediction","url":"https://arxiv.org/html/2509.18362v1"},{"title":"Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/html/2507.19595v1"}]

I've completed a web search for "cross-axis optimization MLP attention LLM inference 2025". Here are the key findings from recent research and technical articles:

## LLM Inference Optimization Overview

The search results reveal several major areas of recent optimization work in LLM inference:

### Attention and MLP Optimization Techniques

Multi-Head Attention (MHA) and Grouped-Query Attention are memory-bound due to low arithmetic intensity, while FeedForward Networks are compute-bound. Recent architectural advances in transformer models—Multi-head Latent Attention (MLA) and Mixture of Experts (MoE)—introduce new dominant bottlenecks.

The arithmetic intensity of MLA is over two orders of magnitude higher than that of MHA, moving it toward a compute-bound regime well-matched to modern accelerators such as GPUs.

### Specific Optimization Approaches

**Tensor and Context Parallelism:** Tensor parallelism involves sharding individual layers of the model, such as attention blocks and multi-layer perceptron (MLP) layers, into smaller, independent blocks that can be executed on different devices.

**Multi-Token Prediction:** Medusa employs extra MLP heads that reuse the last hidden states from the target model to predict the next few tokens in parallel. EAGLE incorporates both the last hidden state and preceding tokens to draft in an autoregressive way, establishing it as the current state-of-the-art approach.

**Speculative Decoding:** Recent breakthroughs in inference optimization are slashing latency by 40% or more — often achieving 2x speedups — without sacrificing output quality.

The results show that 2025 research is shifting focus from attention acceleration to broader system-level optimizations, including communication efficiency and load balancing across distributed inference systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca413cc1-6571-4079-9275-4da99d1d47b9",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "9cf7ecec-c504-4150-a51a-5abc42a7c2d0",
  "sourceToolAssistantUUID": "ca413cc1-6571-4079-9275-4da99d1d47b9",
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

_source line 15 · 2026-05-10T18:21:58.539Z_

<details><summary>↩ Tool result · `toolu_01EgD8i43JipyY7dnBcKnBny`</summary>

```text
Web search results for query: "joint compute memory optimization MLP KV cache LLM decoding 2025 2026"

Links: [{"title":"Joint Encoding of KV-Cache Blocks for Scalable LLM Serving | OpenReview","url":"https://openreview.net/forum?id=M9SgtgvF7l"},{"title":"Joint Encoding of KV-Cache Blocks for Scalable LLM Serving","url":"https://arxiv.org/html/2601.03067v1"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"LLM Inference Optimization Techniques | Clarifai Guide","url":"https://www.clarifai.com/blog/llm-inference-optimization/"},{"title":"LLM Inference Optimization: Quantization, KV Cache, and Serving at Scale - Perivitta Rajendran","url":"https://pr-peri.github.io/blogpost/2026/03/25/blogpost-llm-quantization-kv-cache.html"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"EvicPress: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/html/2512.14946"},{"title":"LMCACHE: AN EFFICIENT KV CACHE LAYER FOR ENTERPRISE-SCALE LLM INFERENCE","url":"https://lmcache.ai/tech_report.pdf"},{"title":"Making sense of KV Cache optimizations, Ep. 1: An overview · Sara Zan","url":"https://www.zansara.dev/posts/2025-10-26-kv-caching-optimizations-intro/"},{"title":"[2601.03067] Joint Encoding of KV-Cache Blocks for Scalable LLM Serving","url":"https://arxiv.org/abs/2601.03067"}]

I found several relevant research papers and resources on joint compute-memory optimization, KV cache optimization, and LLM decoding from 2025-2026. Here are the key findings:

## Joint KV-Cache Optimization

A recent approach proposes joint encoding of KV-cache blocks, which fuses similar blocks across requests and input chunks into shared representations while preserving standard cache structure, alleviating the KV-cache memory bottleneck and supporting high-concurrency serving without specialized hardware. This method achieves up to 4.38× KV-cache compression with negligible accuracy loss across diverse LLMs and benchmarks.

## LLM Decoding Architecture

LLM services face distinct challenges across two stages: the prefill stage where the model processes the input sequence (compute-bound but executed only once per request), and the decode stage which generates subsequent output tokens, is repeated for every token, and is primarily constrained by memory bandwidth.

## Hardware-Software Co-Design Approaches

Recent approaches like INF2 enable the GPU to concurrently process remaining computation like MLP while accelerators perform attention computation near storage.

## Adaptive KV-Cache Techniques

A lightweight data-driven approach designs a compact MLP controller for real-time quantization that leverages token-level features including token frequency, quality score, attention variance, and entropy-based uncertainty to select KV precision under strict memory and latency constraints.

## Broader Optimization Landscape

Current optimization techniques include KV cache selection (prioritizing relevant tokens), budget allocation (distributing memory resources across tokens), KV cache merging (reducing redundancy), and KV cache quantization (reducing precision).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40a158b2-20cd-4414-8215-859277182e66",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "536f0111-d8b9-46b2-9c4e-ffd500c5fff5",
  "sourceToolAssistantUUID": "40a158b2-20cd-4414-8215-859277182e66",
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

_source line 16 · 2026-05-10T18:22:01.239Z_

<details><summary>↩ Tool result · `toolu_018vGkLLbc5PzWSHZ88wQHCP`</summary>

```text
Web search results for query: "single metric MLP sparsity KV eviction transformer 2025"

Links: [{"title":"ICLR 2025 Workshop on Sparsity in LLMs (SLLM) LLMS KNOW WHAT TO DROP:","url":"https://openreview.net/pdf?id=qg9dlCcNzr"},{"title":"Hierarchical Adaptive Eviction for KV Cache Management in Multimodal Language Models","url":"https://arxiv.org/html/2602.02197v1"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity","url":"https://arxiv.org/html/2602.08005v1"},{"title":"MadaKV: Adaptive Modality-Perception KV Cache Eviction ...","url":"https://aclanthology.org/2025.acl-long.652.pdf"},{"title":"FIER: Fine-Grained and Efficient KV Cache Retrieval for ...","url":"https://aclanthology.org/2025.findings-emnlp.515.pdf"},{"title":"KV Cache Eviction in Transformer LLMs","url":"https://www.emergentmind.com/topics/kv-cache-eviction"},{"title":"Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://www.arxiv.org/pdf/2601.17668"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"NVIDIA Researchers Introduce Dynamic Memory Sparsification (DMS) for 8× KV Cache Compression in Transformer LLMs - MarkTechPost","url":"https://www.marktechpost.com/2025/06/11/nvidia-researchers-introduce-dynamic-memory-sparsification-dms-for-8x-kv-cache-compression-in-transformer-llms/"}]

Based on the search results, here's what I found related to your query about single metric MLP sparsity and KV eviction in transformers from 2025:

## Key Findings on KV Cache Eviction and Sparsity (2025)

**Recent Methods Using Single Metrics:**

One notable approach reuses a small part of the attention mechanism (a single neuron) to predict eviction, demonstrating efficient single-metric approaches for KV cache management.

**MLP and Attention Sparsity Research:**

Gating mechanisms that enable sparse and selective computation have been introduced in Transformers, including approaches that demonstrate effective exploitation of sparsity in MLP and attention modules to improve computational efficiency.

**Attention-Based KV Eviction:**

SAGE-KV compresses the KV cache after prefilling for direct use in generation by exploiting attention sparsity. Analysis of attention score sparsity shows that attention heads selectively highlight important tokens, motivating optimization of KV cache compression at the head level.

**Dynamic Memory Sparsification (DMS):**

With as few as 1K training steps, DMS can achieve 8× KV cache compression, preserving or even improving model performance across reasoning tasks.

The 2025 research landscape shows significant progress in developing efficient single-metric and attention-based approaches for KV cache eviction and sparsity in transformer models, balancing computational efficiency with model performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "680b201f-8643-4436-b5ac-5c046c922e89",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "2bd74496-378a-45d4-b3de-c2227d2f2b1a",
  "sourceToolAssistantUUID": "680b201f-8643-4436-b5ac-5c046c922e89",
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

_source line 17 · 2026-05-10T18:22:04.989Z_

Now let me do a few more targeted searches to specifically look for Q-Infer's mechanism and whether any paper proposes a truly unified/single signal for both MLP sparsity and KV cache decisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bd74496-378a-45d4-b3de-c2227d2f2b1a",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMSMgCeWHzPvTT6oeMv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a92d8e3-e95e-4aed-b93e-ddb280078786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StVGYNnqx25ZfuUj1faSEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1991,
      "cache_creation_input_tokens": 2249,
      "cache_read_input_tokens": 11464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2249,
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

_source line 18 · 2026-05-10T18:22:06.127Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01923F7ReFk4AvM4k3cFgWuU`</summary>

```json
{
  "query": "Q-Infer ACM TACO sparsity-aware dynamic scheduling GPU CPU collaborative mechanism details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a92d8e3-e95e-4aed-b93e-ddb280078786",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMSMgCeWHzPvTT6oeMv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0c7b2fe-a8de-43e5-a410-22d06d75491e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StVGYNnqx25ZfuUj1faSEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1991,
      "cache_creation_input_tokens": 2249,
      "cache_read_input_tokens": 11464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2249,
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

_source line 19 · 2026-05-10T18:22:07.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01USatRDLzdCrrtVoMrYR6xi`</summary>

```json
{
  "query": "\"unified redundancy signal\" OR \"single signal\" MLP sparsity \"KV cache\" eviction compression LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0c7b2fe-a8de-43e5-a410-22d06d75491e",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMSMgCeWHzPvTT6oeMv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e001166-168f-4c28-bff4-f555c8db91f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StVGYNnqx25ZfuUj1faSEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1991,
      "cache_creation_input_tokens": 2249,
      "cache_read_input_tokens": 11464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2249,
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

_source line 20 · 2026-05-10T18:22:07.904Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015FSVZkWk1r4vcUfq5YPMtN`</summary>

```json
{
  "query": "ICLR 2025 ICML 2025 NeurIPS 2025 paper joint MLP neuron pruning KV cache compression single metric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e001166-168f-4c28-bff4-f555c8db91f1",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMSMgCeWHzPvTT6oeMv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "610ca0d1-f6ab-47b7-8d33-d9860f4a62b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StVGYNnqx25ZfuUj1faSEC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1991,
      "cache_creation_input_tokens": 2249,
      "cache_read_input_tokens": 11464,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2249
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1991,
          "output_tokens": 251,
          "cache_read_input_tokens": 11464,
          "cache_creation_input_tokens": 2249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2249,
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

_source line 21 · 2026-05-10T18:22:13.043Z_

<details><summary>↩ Tool result · `toolu_01923F7ReFk4AvM4k3cFgWuU`</summary>

```text
Web search results for query: "Q-Infer ACM TACO sparsity-aware dynamic scheduling GPU CPU collaborative mechanism details"

Links: [{"title":"Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling | ACM Transactions on Architecture and Code Optimization","url":"https://dl.acm.org/doi/10.1145/3764589"},{"title":"Q-Infer: Towards Eficient GPU-CPU Collaborative LLM Inference via","url":"https://dl.acm.org/doi/pdf/10.1145/3764589"},{"title":"Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling","url":"https://www.researchgate.net/publication/395071810_Q-Infer_Towards_Efficient_GPU-CPU_Collaborative_LLM_Inference_via_Sparsity-Aware_Dynamic_Scheduling"},{"title":"Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Q-Infer:-Towards-Efficient-GPU-CPU-Collaborative-Lu-Wei/6d2fee68aef566c75bf4678c2f7ae176d5314a44"},{"title":"GitHub - PDS-Lab/Q-Infer · GitHub","url":"https://github.com/PDS-Lab/Q-Infer"},{"title":"GitHub - chenhongyu2048/LLM-inference-optimization-paper: Summary of some awesome work for optimizing LLM inference · GitHub","url":"https://github.com/chenhongyu2048/LLM-inference-optimization-paper"},{"title":"[PDF] Improving Throughput-Oriented LLM Inference with CPU Computations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/09410cd732c26668fe232cc065f2e380fdf9495b"},{"title":"HGCA: Hybrid GPU-CPU Attention for Long Context LLM Inference","url":"https://arxiv.org/html/2507.03153v1"},{"title":"GitHub - byungsoo-oh/ml-systems-papers: Curated collection of papers in machine learning systems · GitHub","url":"https://github.com/byungsoo-oh/ml-systems-papers"},{"title":"Parallel CPU-GPU Execution for LLM Inference on Constrained GPUs","url":"https://gptshop.ai/paper/Apex.pdf"}]

Based on the search results, here are the key details about Q-Infer's sparsity-aware dynamic scheduling and GPU-CPU collaborative mechanism:

## Core Design Principles

Q-Infer is an efficient GPU-CPU collaborative inference system, featured with sparsity-aware cache management and dynamic compute scheduling.

## Key Mechanisms

### 1. Sparsity-Aware Dynamic Cache Strategy

Q-Infer employs a token-level dynamic neuron caching mechanism to effectively mitigate performance degradation due to the weak power-law distribution of neuron activations. Furthermore, it decreases I/O latency by predicting and pre-loading cross-layer activated neurons. To prevent accuracy loss from critical token selection, Q-Infer also introduces a quantization window mechanism.

### 2. GPU-CPU Collaborative Inference and Dynamic Scheduling

Q-Infer employs a hybrid GPU-CPU heterogeneous parallel inference that maximizes CPU computational resources to reduce transmission overhead. Q-Infer balances CPU and GPU processing latency, as well as IO latency, through its dynamic caching policy and scheduling mechanism.

### 3. KV Cache Optimization

Q-Infer proposes a multi-window-based approach for selecting important tokens, which reduces the KV cache while maintaining high accuracy.

## Performance Advantages

Q-Infer's throughput is approximately 1.4×, 2×, and 10× higher than that of PowerInfer, llama.cpp, and FlexGen, respectively. The results demonstrate Q-Infer's superior inference performance while retaining model accuracy compared with state-of-the-art GPU-CPU systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0c7b2fe-a8de-43e5-a410-22d06d75491e",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "d0c7527e-f458-4395-a1a5-b590e66079cd",
  "sourceToolAssistantUUID": "e0c7b2fe-a8de-43e5-a410-22d06d75491e",
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

_source line 22 · 2026-05-10T18:22:13.204Z_

<details><summary>↩ Tool result · `toolu_015FSVZkWk1r4vcUfq5YPMtN`</summary>

```text
Web search results for query: "ICLR 2025 ICML 2025 NeurIPS 2025 paper joint MLP neuron pruning KV cache compression single metric"

Links: [{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/855fc19219017d00abd33ccdc6379a94-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025 FORGET THE DATA AND FINE-TUNING!","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f102c495b31bcc7b2a11c27de75475fc-Paper-Conference.pdf"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"ICML.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025"},{"title":"Published as a conference paper at ICLR 2025 SVD-LLM: TRUNCATION-AWARE SINGULAR","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"GitHub - yinizhilian/ICLR2025-Papers-with-Code: 历年ICLR论文和开源项目合集，包含ICLR2021、ICLR2022、ICLR2023、ICLR2024、ICLR2025.","url":"https://github.com/yinizhilian/ICLR2025-Papers-with-Code"},{"title":"Published as a conference paper at ICLR 2025 DYNAMIC DIFFUSION TRANSFORMER","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a44a70acd5d0abc1a252ada9719dd06d-Paper-Conference.pdf"},{"title":"NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://neurips.cc/public/JournalToConference"}]

I found several papers from ICLR 2025 related to model compression, pruning, and KV cache compression. The search results show papers on model compression techniques, but the specific query about a paper addressing joint MLP neuron pruning and KV cache compression with a single metric didn't return a direct match. 

The search results show:
- Papers discussing MLP pruning and attention layer pruning for models like Llama 3.2, where pruning ratios were set to 0.5 for both MLP and attention layers
- A paper (SVD-LLM) that reduces runtime KV cache memory without additional accuracy drop
- A model compression technique involving neuron clustering and merging

However, I didn't locate the specific paper you're asking about that combines joint MLP neuron pruning and KV cache compression using a single metric across ICLR 2025, ICML 2025, or NeurIPS 2025. The search results indicate these conferences have many papers on related compression techniques, but would need more specific details (such as author names or the exact paper title) to pinpoint the exact paper you're referring to.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "610ca0d1-f6ab-47b7-8d33-d9860f4a62b5",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "48d24fb6-3d62-47a3-abdc-90cdf6fbef5d",
  "sourceToolAssistantUUID": "610ca0d1-f6ab-47b7-8d33-d9860f4a62b5",
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

_source line 23 · 2026-05-10T18:22:14.765Z_

<details><summary>↩ Tool result · `toolu_01USatRDLzdCrrtVoMrYR6xi`</summary>

```text
Web search results for query: ""unified redundancy signal" OR "single signal" MLP sparsity "KV cache" eviction compression LLM"

Links: [{"title":"DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity","url":"https://arxiv.org/html/2602.08005v1"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html"},{"title":"Efficient LLMs at Scale: My NeurIPS Week in KV Caches, Spec Decoding, and FP4","url":"https://kaitchup.substack.com/p/efficient-llms-at-scale-my-neurips"},{"title":"SmallKV: Small Model Assisted Compensation of KV ...","url":"https://openreview.net/pdf?id=0BVrpXMr5Y"},{"title":"Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://www.arxiv.org/pdf/2601.17668"},{"title":"SELF-ATTENTION GUIDED KV CACHE EVICTION FOR ...","url":"https://openreview.net/pdf?id=qg9dlCcNzr"},{"title":"Q-Hitter: A Better Token Oracle for Efficient LLM Inference ...","url":"https://proceedings.mlsys.org/paper_files/paper/2024/file/bbb7506579431a85861a05fff048d3e1-Paper-Conference.pdf"},{"title":"Awesome-LLM-Compression/README.md at main · HuangOwen/Awesome-LLM-Compression","url":"https://github.com/HuangOwen/Awesome-LLM-Compression/blob/main/README.md"}]

Based on the search results, I found several relevant works on KV cache compression and LLM efficiency, though the search didn't return papers specifically using all those exact terms together. Here are the key findings:

## Recent Research on KV Cache Compression and Sparsity

R-KV focuses on extremely long chain-of-thought traces from reasoning models where much of the KV cache is redundant self-reflection, starting from attention signals and adding a redundancy score based on similarity between key vectors to penalize tokens that look like near-duplicates of later ones.

SparK (Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning) targets channel-level redundancy, based on the insight that channel saliency varies dramatically across both queries and positions, with certain feature channels carrying near-zero information while others spike in relevance for a given query.

SparK identifies and prunes KV entries at the channel level that are deemed irrelevant for the current query, and dynamically restores the pruned entries during attention score computation through a "prune-and-recover" mechanism.

Beyond empirical gains, research highlights that KV caches exhibit substantial global redundancy beyond local similarity, and suggests KV optimization should move beyond eviction and low-rank projection toward similarity-aware representations.

The search results also reveal numerous other approaches to KV cache optimization including eviction strategies, quantization methods, and low-rank projection techniques, though I did not find papers using the exact phrase "unified redundancy signal" or "single signal" in combination with the other terms you specified.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e001166-168f-4c28-bff4-f555c8db91f1",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "4a86d66b-24d2-429d-8b2e-0c96b7c26b60",
  "sourceToolAssistantUUID": "6e001166-168f-4c28-bff4-f555c8db91f1",
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

_source line 24 · 2026-05-10T18:22:19.741Z_

Let me do a few final targeted searches to look for any paper that uses a truly unified signal across both MLP and KV cache axes, and to get more detail on Q-Infer's internal mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a86d66b-24d2-429d-8b2e-0c96b7c26b60",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMTMjww18GWEaCJeEvh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "defcf159-b3dc-467a-bc1d-5df0e0b071e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxiAojRuqmNqGVrCgonEiB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 4472,
      "cache_read_input_tokens": 13713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4472,
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

_source line 25 · 2026-05-10T18:22:20.713Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HVNFfAXJmrdkWt8uF2aX8a`</summary>

```json
{
  "query": "Q-Infer paper token importance MLP predictor KV cache quantization window mechanism details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "defcf159-b3dc-467a-bc1d-5df0e0b071e9",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMTMjww18GWEaCJeEvh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8356d86-69a9-4bad-9255-b0afba25a18b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxiAojRuqmNqGVrCgonEiB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 4472,
      "cache_read_input_tokens": 13713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4472,
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

_source line 26 · 2026-05-10T18:22:21.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N5vhVU6yu6giBoo1vV93sc`</summary>

```json
{
  "query": "\"token redundancy\" OR \"activation importance\" drives both MLP sparsity KV cache pruning single shared signal LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8356d86-69a9-4bad-9255-b0afba25a18b",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMTMjww18GWEaCJeEvh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed4be20b-7b3c-4314-900e-bc3e73c7e727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxiAojRuqmNqGVrCgonEiB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 4472,
      "cache_read_input_tokens": 13713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4472,
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

_source line 27 · 2026-05-10T18:22:22.506Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01McHaBQL1Wt4UkvNr9SdLZk`</summary>

```json
{
  "query": "PowerInfer DejaVu \"MLP sparsity\" \"KV cache\" unified combined single approach 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed4be20b-7b3c-4314-900e-bc3e73c7e727",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMTMjww18GWEaCJeEvh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74c4c01b-5d52-454b-aff6-413c97df0b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxiAojRuqmNqGVrCgonEiB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 4472,
      "cache_read_input_tokens": 13713,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4472
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 959,
          "output_tokens": 244,
          "cache_read_input_tokens": 13713,
          "cache_creation_input_tokens": 4472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4472,
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

_source line 28 · 2026-05-10T18:22:27.839Z_

<details><summary>↩ Tool result · `toolu_01HVNFfAXJmrdkWt8uF2aX8a`</summary>

```text
Web search results for query: "Q-Infer paper token importance MLP predictor KV cache quantization window mechanism details"

Links: [{"title":"Q-Hitter: A Better Token Oracle for Efficient LLM Inference ...","url":"https://proceedings.mlsys.org/paper_files/paper/2024/file/bbb7506579431a85861a05fff048d3e1-Paper-Conference.pdf"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"More Tokens, Lower Precision: Towards the Optimal Token-Precision Trade-off in KV Cache Compression","url":"https://arxiv.org/html/2412.12706v1"},{"title":"Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling | ACM Transactions on Architecture and Code Optimization","url":"https://dl.acm.org/doi/10.1145/3764589"},{"title":"GitHub - SqueezeAILab/KVQuant: [NeurIPS 2024] KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization · GitHub","url":"https://github.com/SqueezeAILab/KVQuant"},{"title":"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization","url":"https://arxiv.org/html/2401.18079v3"},{"title":"Towards 10 Million Context Length LLM Inference with KV ...","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf"},{"title":"KVQuant: Towards 10 Million Context Length LLM Inference ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/028fcbcf85435d39a40c4d61b42c99a4-Paper-Conference.pdf"},{"title":"NeurIPS Poster KV Cache is 1 Bit Per Channel: Efficient Large Language Model Inference with Coupled Quantization","url":"https://neurips.cc/virtual/2024/poster/93558"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397"}]

Based on the search results, I found information about **Q-Infer**, which is an efficient GPU-CPU collaborative LLM inference system. Here are the key details:

## Q-Infer: Token Importance and Multi-Window Mechanism

**Token Importance & MLP Predictor:**
Q-Infer employs an online MLP predictor to predict the activated neurons in each Transformer layer. Based on the results of the predictor, Q-Infer prefetches only the most activated neurons (Top-K) to the GPU, leaving the remainder on the CPU.

**KV Cache Quantization & Window Mechanism:**
Q-Infer dynamically selects a small number of key tokens from the entire Token Window via a multi-window mechanism, which quantifies the KV cache of unimportant tokens instead of discarding them directly.

**Multi-Window Structure:**
Q-Infer divides the KV cache according to the token window. The corresponding KV cache is distributed to the GPU in the order of the recent window, the key tokens window, and the quantization window. Most quantized KV caches are computed by the CPU, and Modern CPUs (e.g., AVX-512 instruction set) are specifically optimized for low-precision calculations.

The system uses three distinct windows: a recent window (storing recent tokens in full precision), a key tokens window (storing important tokens selected dynamically), and a quantization window (storing less important tokens in quantized form) to balance memory efficiency and inference accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8356d86-69a9-4bad-9255-b0afba25a18b",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "408a9b3c-96eb-4fef-8c4e-9b07ca6521b3",
  "sourceToolAssistantUUID": "e8356d86-69a9-4bad-9255-b0afba25a18b",
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

_source line 29 · 2026-05-10T18:22:29.548Z_

<details><summary>↩ Tool result · `toolu_01McHaBQL1Wt4UkvNr9SdLZk`</summary>

```text
Web search results for query: "PowerInfer DejaVu "MLP sparsity" "KV cache" unified combined single approach 2025 arxiv"

Links: [{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/html/2312.12456v1"},{"title":"[2312.12456] PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://ar5iv.labs.arxiv.org/html/2312.12456"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU∗","url":"https://ipads.se.sjtu.edu.cn/_media/publications/powerinfer-20231219.pdf"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"},{"title":"[2310.17157] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://ar5iv.labs.arxiv.org/html/2310.17157"},{"title":"[2507.20613] Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression","url":"https://arxiv.org/abs/2507.20613"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling | ACM Transactions on Architecture and Code Optimization","url":"https://dl.acm.org/doi/full/10.1145/3764589"},{"title":"A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/html/2412.19442v3"}]

Based on the search results, I found relevant information about PowerInfer, DejaVu, MLP sparsity, and KV cache approaches. Here's what the search reveals:

## PowerInfer and DejaVu Context

DejaVu accelerates LLM inference by using activation sparsity, selectively processing only those neurons that are predicted to be activated while bypassing the inactivated ones. PowerInfer reduces computational loads by only processing those neurons that are predicted to be activated, using a method also employed in DejaVu which advocates for training a set of fixed-size MLP predictors.

## MLP Sparsity and KV Cache Approaches

The search results show that approaches that sparsify only the MLP block show decreased speedup with larger batch sizes. More recent work addresses both sparsity dimensions: Activation sparsity has been shown to be effective in reducing inference latency, but its application has been largely limited to single-query workloads like DejaVu, PowerInfer, and LLMInAFlash.

## Unified Approaches

For combined approaches, one proposal includes an adaptive search algorithm that optimizes sparsity and KV cache compression to enhance efficiency, uniquely combining pruning with key-value cache quantization. Additionally, sparse attention mechanisms could be combined with KV cache merging to achieve greater efficiency, exploring how merging complements sparsity-based approaches.

The search results indicate this is an active research area with various systems exploring combined sparsity and KV cache optimization approaches, though the specific 2025 arxiv paper matching all your exact search terms wasn't directly returned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74c4c01b-5d52-454b-aff6-413c97df0b5e",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "2575c98e-7b21-4177-a4a6-d6de3198e6bc",
  "sourceToolAssistantUUID": "74c4c01b-5d52-454b-aff6-413c97df0b5e",
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

_source line 30 · 2026-05-10T18:22:29.673Z_

<details><summary>↩ Tool result · `toolu_01N5vhVU6yu6giBoo1vV93sc`</summary>

```text
Web search results for query: ""token redundancy" OR "activation importance" drives both MLP sparsity KV cache pruning single shared signal LLM 2025"

Links: [{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://www.arxiv.org/pdf/2512.07090"},{"title":"SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling","url":"https://arxiv.org/html/2506.04179v1"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html"},{"title":"ICLR 2025 Workshop on Sparsity in LLMs (SLLM) LLMS KNOW WHAT TO DROP:","url":"https://openreview.net/pdf?id=qg9dlCcNzr"},{"title":"Think Clearly: Improving Reasoning via Redundant Token Pruning","url":"https://assets.amazon.science/b5/2e/9db326c7421b967fe0903d6307b9/think-clearly-improving-reasoning-via-redundant-token-pruning.pdf"},{"title":"LLM Inference Optimization Techniques | Redwerk","url":"https://redwerk.com/blog/llm-inference-optimization-techniques/"},{"title":". . Latest updates: hps://dl.acm.org/doi/10.1145/3706418 . . SURVEY","url":"https://dl.acm.org/doi/pdf/10.1145/3706418"}]

Based on the search results, I found several relevant papers from 2025 that address token redundancy, activation importance, MLP sparsity, and KV cache pruning in large language models. Here are the key findings:

## Token Redundancy and Activation Importance

Token redundancy is exploited in training-free KV cache compression methods, recognizing that not all tokens equally influence future predictions, and many provide negligible information once their contextual role is fulfilled.

## KV Cache Pruning Methods

KeyDiff (2025) demonstrated a correlation between cosine similarity among keys and their attention scores, where keys with high cosine similarity to an anchor key (the mean of all previous keys) are considered redundant and less important, allowing them to be evicted from the KV cache.

KeyDiff emphasizes key vector diversity by evicting tokens whose keys are redundant, i.e., highly similar to others, thereby preserving a more diverse compression.

## MLP vs Attention Sparsity

As context grows, later tokens require more attention computation but less MLP computation. Additionally, the MLP module has higher redundancy during the decoding phase compared to the pre-filling phase, while attention redundancy remains nearly the same in both phases.

## Query-Aware Sparsity Approaches

SparK's core insight is that channel saliency varies dramatically across both queries and positions, where for a given query, certain feature channels carry near-zero information, while others spike in relevance, identifying and pruning KV entries at the channel level that are deemed irrelevant for the current query.

These approaches demonstrate unified frameworks that identify redundant information across both MLP sparsity and KV cache management in LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed4be20b-7b3c-4314-900e-bc3e73c7e727",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "1ada800a-29a0-4cf8-a46c-c495934bca48",
  "sourceToolAssistantUUID": "ed4be20b-7b3c-4314-900e-bc3e73c7e727",
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

_source line 31 · 2026-05-10T18:22:32.783Z_

Let me check that last interesting result about "Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression" more closely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ada800a-29a0-4cf8-a46c-c495934bca48",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMUTE8TiTQKRAnfPyDP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f3838e7-5056-40a3-a69d-bee0eaff8fae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMWWJ8YZSi3AanAj13SWwr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 3177,
      "cache_read_input_tokens": 18185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3177,
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

_source line 32 · 2026-05-10T18:22:33.264Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DxQ3B7mf3j3RPJovxrsect`</summary>

```json
{
  "query": "arxiv 2507.20613 \"Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression\" details approach"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f3838e7-5056-40a3-a69d-bee0eaff8fae",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMUTE8TiTQKRAnfPyDP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1b34dd5-ccc9-47eb-8dce-89b2ba385d36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMWWJ8YZSi3AanAj13SWwr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 3177,
      "cache_read_input_tokens": 18185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3177,
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

_source line 33 · 2026-05-10T18:22:34.421Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012UyQ5bcMVsvYPTM4q6U28W`</summary>

```json
{
  "query": "SkipGPT \"module decoupling\" MLP attention token awareness layer pruning joint signal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1b34dd5-ccc9-47eb-8dce-89b2ba385d36",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMUTE8TiTQKRAnfPyDP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "768ab269-f4d6-4383-9bac-4f5dae5e5720",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMWWJ8YZSi3AanAj13SWwr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 3177,
      "cache_read_input_tokens": 18185,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3177
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 946,
          "output_tokens": 178,
          "cache_read_input_tokens": 18185,
          "cache_creation_input_tokens": 3177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3177,
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

_source line 34 · 2026-05-10T18:22:40.490Z_

<details><summary>↩ Tool result · `toolu_01DxQ3B7mf3j3RPJovxrsect`</summary>

```text
Web search results for query: "arxiv 2507.20613 "Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression" details approach"

Links: [{"title":"[2507.20613] Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression","url":"https://arxiv.org/abs/2507.20613"},{"title":"Enhancing Large Multimodal Models with Adaptive ...","url":"https://arxiv.org/pdf/2507.20613"},{"title":"[2507.20613v1] Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression","url":"https://arxiv.org/abs/2507.20613v1"},{"title":"Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression - haebom","url":"https://slashpage.com/haebom/daily_arxiv?lang=en&tl=en&post=ywk9j7298ppydmgpqvnd"},{"title":"Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression - Consensus","url":"https://consensus.app/papers/enhancing-large-multimodal-models-with-adaptive-sparsity-zhang-li/fc4b71264f0f5afeb6d85ec189385eb8/"},{"title":"Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression","url":"https://powerdrill.ai/discover/summary-enhancing-large-multimodal-models-with-adaptive-cmdp0vdq9a5ml07nq067fxtqj"},{"title":"VL-Cache: Sparsity and modality-aware KV cache compression for vision-language model inference acceleration - Amazon Science","url":"https://www.amazon.science/publications/vl-cache-sparsity-and-modality-aware-kv-cache-compression-for-vision-language-model-inference-acceleration"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"Large Multimodal Models (LMMs) Overview","url":"https://www.emergentmind.com/topics/large-multimodal-models-lmms"},{"title":"A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/html/2412.19442v3"}]

Based on the search results, here are the details of the approach presented in arxiv paper 2507.20613:

## Paper Overview

The paper addresses large multimodal models (LMMs) that integrate visual encoders with extensive language models, and proposes an adaptive search algorithm that optimizes sparsity and KV cache compression to enhance LMM efficiency.

## Key Approach

The method employs two main compression techniques:

1. **Adaptive Sparsity Optimization**: The method dynamically adjusts pruning ratios across different LMM layers, using model performance as the optimization objective. The approach introduces an advanced pruning metric that captures weights and activations in both row and column dimensions, enabling accurate ranking of unit importance.

2. **KV Cache Compression**: Uniform asymmetric quantization compresses the Key-Value (KV) Cache in LLMs by mapping high-precision values to lower-precision formats, reducing memory usage during inference.

## Optimization Method

The approach utilizes the Tree-structured Parzen Estimator and dynamically adjusts pruning ratios and KV cache quantization bandwidth across different LMM layers.

## Key Advantage

This approach uniquely combines pruning with key-value cache quantization and incorporates a fast pruning technique that eliminates the need for additional fine-tuning or weight adjustments.

## Evaluation

The paper conducted extensive experiments on benchmarks like VQAv2, SQA, POPE, TextVQA, and Wikitext perplexity, with pruning and quantization methods demonstrating superior performance in maintaining model quality under various sparsity ratios and quantization bandwidths.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1b34dd5-ccc9-47eb-8dce-89b2ba385d36",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "dc641edd-afbb-47dd-9236-a24a5ebc3f16",
  "sourceToolAssistantUUID": "e1b34dd5-ccc9-47eb-8dce-89b2ba385d36",
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

_source line 35 · 2026-05-10T18:22:41.911Z_

<details><summary>↩ Tool result · `toolu_012UyQ5bcMVsvYPTM4q6U28W`</summary>

```text
Web search results for query: "SkipGPT "module decoupling" MLP attention token awareness layer pruning joint signal"

Links: [{"title":"SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling","url":"https://arxiv.org/html/2506.04179v1"},{"title":"SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and","url":"https://arxiv.org/pdf/2506.04179"},{"title":"[2506.04179] SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling","url":"https://arxiv.org/abs/2506.04179"},{"title":"GitHub - EIT-NLP/SkipGPT: [ICML 2025] Official implementation of the paper \"SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling\". (By Anhao Zhao)","url":"https://github.com/EIT-NLP/SkipGPT"},{"title":"(PDF) SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling","url":"https://www.researchgate.net/publication/392406297_SkipGPT_Dynamic_Layer_Pruning_Reinvented_with_Token_Awareness_and_Module_Decoupling"},{"title":"SkipGPT: Each Token is One of a Kind | OpenReview","url":"https://openreview.net/forum?id=d7v2iUSa9s"},{"title":"FROM LLMS TO LRMS: RETHINKING PRUNING FOR ...","url":"https://openreview.net/pdf/22e86f83f92e7bde9a53913afbf933b2a230853c.pdf"},{"title":"SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling","url":"https://paperreading.club/page?id=313575"},{"title":"STREAMINGTHINKER: LARGE LANGUAGE MODELS CAN THINK WHILE READING Junlong Tong1,2","url":"https://www.arxiv.org/pdf/2510.17238"},{"title":"TokenSkip: Efficient Token and Module Skipping","url":"https://www.emergentmind.com/topics/tokenskip"}]

Based on the search results, I found comprehensive information about SkipGPT. Here's what I found:

## SkipGPT Overview

SkipGPT is a dynamic layer pruning framework designed to optimize computational resource allocation through two core innovations: (1) global token-aware routing to prioritize critical tokens, and (2) decoupled pruning policies for MLP and self-attention components.

## Key Technical Features

**Module Decoupling**: SkipGPT decouples the MLP and self-attention components within each layer, enabling more granular control over which parts of the model are pruned. Research suggests that MLPs function like localized neural processes, capturing task-specific interactions, whereas attention mechanisms resemble higher-level cognitive functions, managing contextual relevance and information flow. Inspired by how the human brain activates different regions for different tasks, SkipGPT decouples the pruning of MLP and self-attention, enabling more targeted and efficient computation reduction.

**Token Awareness**: SkipGPT dynamically prunes layers on a per-token basis, adapting the pruning process to the complexity of each token.

## Training Approach

SkipGPT uses a two-stage training paradigm: First, in Router Tuning, the model parameters are frozen and only the router is optimized, allowing it to identify the most critical computations without disrupting the model's pretrained knowledge. Second, in LoRA Fine-Tuning, the router is frozen and the model is fine-tuned using LoRA to compensate for any performance degradation caused by pruning.

## Performance

SkipGPT reduces up to 40% of parameters without compromising—and sometimes even improving—performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "768ab269-f4d6-4383-9bac-4f5dae5e5720",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "ac2d475fdb055a07a",
  "type": "user",
  "uuid": "72edd0ae-a2c6-429a-b43a-a79632086d1d",
  "sourceToolAssistantUUID": "768ab269-f4d6-4383-9bac-4f5dae5e5720",
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

_source line 36 · 2026-05-10T18:23:24.667Z_

Now I have a comprehensive picture. Here is my report:

---

## Findings

### Q-Infer: Verified and Characterized

**Q-Infer** is a real, published paper. Its full title is "Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling," published in **ACM Transactions on Architecture and Code Optimization (TACO)**, 2025. It is available at:

- [ACM Digital Library](https://dl.acm.org/doi/full/10.1145/3764589)
- [ResearchGate](https://www.researchgate.net/publication/395071810_Q-Infer_Towards_Efficient_GPU-CPU_Collaborative_LLM_Inference_via_Sparsity-Aware_Dynamic_Scheduling)
- [GitHub (PDS-Lab/Q-Infer)](https://github.com/PDS-Lab/Q-Infer)

**Q-Infer's approach** addresses both MLP neuron sparsity and KV cache compression, but it treats them as **two separate optimization mechanisms coordinated at the system/scheduling level**, not as a single unified signal:

1. **MLP Sparsity**: Q-Infer uses an online MLP predictor to predict which neurons will be activated in each Transformer layer. Only the Top-K activated neurons are prefetched to the GPU; the rest remain on the CPU. This exploits contextual sparsity in the MLP blocks.

2. **KV Cache Compression**: Independently, Q-Infer uses a **multi-window mechanism** that divides the KV cache into three windows:
   - A **recent window** (full-precision recent tokens)
   - A **key tokens window** (dynamically selected important tokens)
   - A **quantization window** (less important tokens stored in quantized form on the CPU, computed via AVX-512 instructions)

3. **Coordination**: These two mechanisms are coordinated through a **sparsity-aware dynamic scheduling** layer that balances GPU-CPU workloads and I/O latency. The MLP predictor and the token importance selection for KV cache are **separate predictors/signals** -- they are orchestrated together in a system-level scheduler, but they do not share a single redundancy metric.

**Performance**: Q-Infer achieves approximately 1.4x, 2x, and 10x higher throughput compared to PowerInfer, llama.cpp, and FlexGen respectively.

---

### Does Any Paper Use a Single Unified Signal for Both MLP Sparsity and KV Cache Decisions?

After extensive searching across five different query formulations, **I did not find any published paper (2025-2026) that proposes using a single, shared redundancy signal to simultaneously drive both MLP neuron sparsity decisions and KV cache eviction/compression decisions.** Here is what the landscape looks like:

**Papers that address both axes but with separate mechanisms:**

- **Q-Infer** (ACM TACO 2025): As described above -- separate MLP predictor and KV cache window mechanism, coordinated at the scheduling level.
- **[Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression](https://arxiv.org/abs/2507.20613)** (Zhang et al., 2025): Combines weight pruning with KV cache quantization using a Tree-structured Parzen Estimator to search for optimal per-layer configurations. But pruning and quantization use separate metrics (weight/activation importance for pruning, uniform asymmetric quantization for KV cache). These are jointly *optimized* but driven by *different signals*.
- **SkipGPT** (ICML 2025): Decouples MLP and self-attention pruning decisions, using a learned router to make per-token, per-module skip decisions. This is arguably the closest to a unified framework, as a single router makes decisions about both MLP and attention modules. However, it operates at the **layer-skipping** level (deciding whether to skip an MLP or attention sub-layer entirely), not at the neuron-sparsity / KV-eviction level. And the router produces separate skip signals for MLP vs. attention rather than one shared redundancy score.

**Papers that address KV cache only (with relevant techniques):**
- **SparK** (AMD, 2025): Query-aware channel-level KV cache pruning.
- **R-KV**: Redundancy scoring based on key-vector similarity for KV eviction.
- **DeltaKV**: Residual-based KV cache compression via long-range similarity.

**Papers that address MLP sparsity only:**
- **Polar Sparsity** (2025): Batched LLM inference with scalable contextual sparsity.
- **DejaVu / PowerInfer**: Foundational MLP contextual sparsity work (2023-2024).

---

### Summary

- **Q-Infer is real and verified** -- published in ACM TACO 2025, with code on GitHub. It addresses both MLP sparsity and KV cache compression, but uses **separate mechanisms** (MLP activation predictor + multi-window KV cache management) coordinated through a system-level dynamic scheduler.

- **No paper found that uses a single unified redundancy signal across both axes.** The closest works either (a) jointly optimize both but with separate metrics (Q-Infer, the multimodal sparsity+quantization paper), or (b) use a single router that makes separate decisions per module type (SkipGPT). The idea of a single scalar or vector "redundancy signal" that simultaneously determines which MLP neurons to skip and which KV cache entries to evict appears to be an **open research gap** as of the searches conducted.

Sources:
- [Q-Infer (ACM TACO)](https://dl.acm.org/doi/full/10.1145/3764589)
- [Q-Infer PDF](https://dl.acm.org/doi/pdf/10.1145/3764589)
- [Q-Infer on ResearchGate](https://www.researchgate.net/publication/395071810_Q-Infer_Towards_Efficient_GPU-CPU_Collaborative_LLM_Inference_via_Sparsity-Aware_Dynamic_Scheduling)
- [Q-Infer on Semantic Scholar](https://www.semanticscholar.org/paper/Q-Infer:-Towards-Efficient-GPU-CPU-Collaborative-Lu-Wei/6d2fee68aef566c75bf4678c2f7ae176d5314a44)
- [Q-Infer GitHub](https://github.com/PDS-Lab/Q-Infer)
- [Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression](https://arxiv.org/abs/2507.20613)
- [SkipGPT (ICML 2025)](https://arxiv.org/abs/2506.04179)
- [SkipGPT GitHub](https://github.com/EIT-NLP/SkipGPT)
- [SparK (AMD ROCm Blog)](https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html)
- [Polar Sparsity](https://arxiv.org/html/2505.14884)
- [KV Cache Optimization Strategies Survey](https://arxiv.org/html/2603.20397v1)
- [ICLR 2025 Workshop: LLMs Know What to Drop](https://openreview.net/pdf?id=qg9dlCcNzr)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72edd0ae-a2c6-429a-b43a-a79632086d1d",
  "isSidechain": true,
  "agentId": "ac2d475fdb055a07a",
  "requestId": "req_011CauMVMY6t853vfgeQnyGY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "436f442c-4317-478e-be33-94d8b13b8899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EUpWebzHPqxxbGjR1ooiaj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3229,
      "cache_read_input_tokens": 21362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3229,
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
