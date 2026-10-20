# Research conversation: Search for "Qwen3-Embedding-0.6B" to verify this model exists on HuggingFace. The proposal plans to use it as a frozen e

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2f012828444862c9.jsonl`
- **Structured JSON:** [`8756b5612ca98d6299b3.json`](../../sessions/87/8756b5612ca98d6299b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-11T23:36:03.366Z_

Search for "Qwen3-Embedding-0.6B" to verify this model exists on HuggingFace. The proposal plans to use it as a frozen embedding model for trajectory step encoding.

1. Search "Qwen3-Embedding-0.6B huggingface"
2. Search "Qwen3 embedding model 2025 2026"
3. If it exists, what is its embedding dimension, max sequence length, and performance on standard benchmarks?
4. Is there also a "Qwen3-Embedding-4B" variant (mentioned as an ablation)?

Use WebSearch and report findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "73a8f41f-e7fa-4202-b55c-022bdc924b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:36:03.367Z_

```json
{
  "parentUuid": "73a8f41f-e7fa-4202-b55c-022bdc924b12",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
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
  "uuid": "ffa7eaaf-c165-46ad-8cb2-5bf35017ce61",
  "timestamp": "2026-05-11T23:36:03.367Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:36:05.115Z_



I'll search for information about these models using WebSearch.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffa7eaaf-c165-46ad-8cb2-5bf35017ce61",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfCCz2vWD1STKz2fmPF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "faeaaac3-d9d4-4ef8-ba51-930518cc60d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJnZtprJpGqzjSrtnoxQKi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 692,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:36:05.567Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EtFFrGb52SYrj9NLgwjiQM`</summary>

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
  "parentUuid": "faeaaac3-d9d4-4ef8-ba51-930518cc60d2",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfCCz2vWD1STKz2fmPF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a006828e-84de-4077-b7b2-79c830aa2622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJnZtprJpGqzjSrtnoxQKi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 692,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-11T23:36:05.571Z_

<details><summary>↩ Tool result · `toolu_01EtFFrGb52SYrj9NLgwjiQM`</summary>

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
  "parentUuid": "a006828e-84de-4077-b7b2-79c830aa2622",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "46831322-c1f2-4704-9dfc-532c27629720",
  "sourceToolAssistantUUID": "a006828e-84de-4077-b7b2-79c830aa2622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:36:07.946Z_



Now let me run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46831322-c1f2-4704-9dfc-532c27629720",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfCPJeRQdpkvfKfRWbu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61ed6936-f161-465d-b1cd-b782a48f2717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQ9eDRJhCP7nTrdJQwfwRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 7 · 2026-05-11T23:36:08.529Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0188qcMMCCR7cc4b9YkRsJoc`</summary>

```json
{
  "query": "Qwen3-Embedding-0.6B huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61ed6936-f161-465d-b1cd-b782a48f2717",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfCPJeRQdpkvfKfRWbu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d9b6ef5-fc6f-41e2-a343-67de231252e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQ9eDRJhCP7nTrdJQwfwRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 8 · 2026-05-11T23:36:09.358Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013x4zNftffmfGnXmGdPLskh`</summary>

```json
{
  "query": "Qwen3 embedding model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d9b6ef5-fc6f-41e2-a343-67de231252e0",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfCPJeRQdpkvfKfRWbu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f202be0a-34eb-4382-af21-abcc7b40c392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQ9eDRJhCP7nTrdJQwfwRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 9 · 2026-05-11T23:36:09.421Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mpbfhp29rVkmd3psuFUtXR`</summary>

```json
{
  "query": "Qwen3-Embedding-4B huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f202be0a-34eb-4382-af21-abcc7b40c392",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfCPJeRQdpkvfKfRWbu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1f94a39-adbe-4659-b765-7ce3b1857d5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQ9eDRJhCP7nTrdJQwfwRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 10 · 2026-05-11T23:36:15.213Z_

<details><summary>↩ Tool result · `toolu_01Mpbfhp29rVkmd3psuFUtXR`</summary>

````text
Web search results for query: "Qwen3-Embedding-4B huggingface"

Links: [{"title":"Qwen/Qwen3-Embedding-4B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-4B"},{"title":"Qwen/Qwen3-Embedding-4B-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-4B-GGUF"},{"title":"Qwen/Qwen3-Embedding-4B at main","url":"https://huggingface.co/Qwen/Qwen3-Embedding-4B/tree/main"},{"title":"Mungert/Qwen3-Embedding-4B-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/Qwen3-Embedding-4B-GGUF"},{"title":"Qwen/Qwen3-Embedding-4B · Discussions","url":"https://huggingface.co/Qwen/Qwen3-Embedding-4B/discussions"},{"title":"Qwen (Qwen)","url":"https://huggingface.co/Qwen/collections"},{"title":"README.md · Qwen/Qwen3-Embedding-4B at main","url":"https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/README.md"},{"title":"Qwen/Qwen3-Reranker-4B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Reranker-4B"},{"title":"GitHub - QwenLM/Qwen3-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-Embedding"},{"title":"Qwen3-Embedding - a Qwen Collection","url":"https://huggingface.co/collections/Qwen/qwen3-embedding"}]

Based on the search results, here's what I found about Qwen3-Embedding-4B on Hugging Face:

## Overview

Qwen3-Embedding-4B is a text embedding and ranking model from the Qwen family, part of a comprehensive range available in various sizes (0.6B, 4B, and 8B).

## Capabilities

The Qwen3 Embedding series represents significant advancements in multiple text embedding and ranking tasks, including text retrieval, code retrieval, text classification, text clustering, and bitext mining.

The model supports over 100 languages and includes various programming languages, providing robust multilingual, cross-lingual, and code retrieval capabilities.

## Key Features

The model allows for flexible vector definitions across all dimensions and supports user-defined instructions to enhance performance for specific tasks, languages, or scenarios.

The series inherits exceptional multilingual capabilities, long-text understanding, and reasoning skills from its foundational model.

## Usage

You can load the model using the Sentence Transformers library with the code:
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-Embedding-4B")
```

The model is available on the Hugging Face Hub at: https://huggingface.co/Qwen/Qwen3-Embedding-4B


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1f94a39-adbe-4659-b765-7ce3b1857d5a",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "4f40d024-da0e-47d1-9842-07a8e67e93d8",
  "sourceToolAssistantUUID": "f1f94a39-adbe-4659-b765-7ce3b1857d5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-11T23:36:15.346Z_

<details><summary>↩ Tool result · `toolu_0188qcMMCCR7cc4b9YkRsJoc`</summary>

```text
Web search results for query: "Qwen3-Embedding-0.6B huggingface"

Links: [{"title":"Qwen/Qwen3-Embedding-0.6B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B"},{"title":"Qwen/Qwen3-Embedding-0.6B-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B-GGUF"},{"title":"Qwen/Qwen3-0.6B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-0.6B"},{"title":"Mungert/Qwen3-Embedding-0.6B-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/Qwen3-Embedding-0.6B-GGUF"},{"title":"Qwen/Qwen3-Embedding-0.6B · Discussions","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/discussions"},{"title":"Qwen/Qwen3-Reranker-0.6B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Reranker-0.6B"},{"title":"Qwen/Qwen3-Embedding-0.6B at main","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/tree/main"},{"title":"zhiqing/Qwen3-Embedding-0.6B-ONNX · Hugging Face","url":"https://huggingface.co/zhiqing/Qwen3-Embedding-0.6B-ONNX"},{"title":"Qwen3-Embedding - a Qwen Collection","url":"https://huggingface.co/collections/Qwen/qwen3-embedding"},{"title":"mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ · Hugging Face","url":"https://huggingface.co/mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ"}]

Based on the search results, here's information about **Qwen3-Embedding-0.6B** on Hugging Face:

## Overview
The Qwen3 Embedding model series is the latest proprietary model of the Qwen family, specifically designed for text embedding and ranking tasks.

## Model Specifications
The model provides a comprehensive range of text embeddings and reranking models in various sizes (0.6B, 4B, and 8B). This series inherits the exceptional multilingual capabilities, long-text understanding, and reasoning skills of its foundational model.

## Capabilities
The Qwen3 Embedding series represents significant advancements in multiple text embedding and ranking tasks, including text retrieval, code retrieval, text classification, text clustering, and bitext mining.

## Key Features
- The Qwen3 Embedding series offer support for over 100 languages
- The embedding model allows for flexible vector definitions across all dimensions, and both embedding and reranking models support user-defined instructions to enhance performance for specific tasks, languages, or scenarios.

## Available Variants
The model is available in different formats on Hugging Face, including:
- Standard PyTorch format (Qwen/Qwen3-Embedding-0.6B)
- GGUF format (Qwen/Qwen3-Embedding-0.6B-GGUF)
- ONNX format
- MLX-optimized versions

You can find the official model page at https://huggingface.co/Qwen/Qwen3-Embedding-0.6B


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d9b6ef5-fc6f-41e2-a343-67de231252e0",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "6dc0dbc1-45af-42e8-ab75-2493cedb01c2",
  "sourceToolAssistantUUID": "2d9b6ef5-fc6f-41e2-a343-67de231252e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:36:15.738Z_

<details><summary>↩ Tool result · `toolu_013x4zNftffmfGnXmGdPLskh`</summary>

```text
Web search results for query: "Qwen3 embedding model 2025 2026"

Links: [{"title":"Qwen/Qwen3-Embedding-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-8B"},{"title":"GitHub - QwenLM/Qwen3-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-Embedding"},{"title":"qwen3-embedding","url":"https://ollama.com/library/qwen3-embedding"},{"title":"[2506.05176] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models","url":"https://arxiv.org/abs/2506.05176"},{"title":"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen","url":"https://qwenlm.github.io/blog/qwen3-embedding/"},{"title":"Ultimate Guide - The Best Qwen3 Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-qwen3-models-in-2025"},{"title":"[2601.04720] Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking","url":"https://arxiv.org/abs/2601.04720"},{"title":"GitHub - QwenLM/Qwen3-VL-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-VL-Embedding"},{"title":"Qwen3-VL-Embedding","url":"https://qwen.ai/blog?id=qwen3-vl-embedding"},{"title":"Qwen3 Embedding: Advancing Text ...","url":"https://arxiv.org/pdf/2506.05176"}]

Based on the search results, here's what I found about Qwen3 embedding models in 2025-2026:

## Qwen3 Text Embedding Models

The Qwen3 Embedding model series is specifically designed for text embedding and ranking tasks. It provides a comprehensive range of text embeddings and reranking models in various sizes (0.6B, 4B, and 8B).

### Key Features and Performance

The 8B size embedding model ranks No.1 in the MTEB multilingual leaderboard (as of June 5, 2025, score 70.58). The Qwen3 Embedding series offer support for over 100 languages.

The Qwen3 Embedding series represents significant advancements in multiple text embedding and ranking tasks, including text retrieval, code retrieval, text classification, text clustering, and bitext mining.

## Qwen3-VL Multimodal Embedding Models (2026)

More recently, Qwen3-VL-Embedding and Qwen3-VL-Reranker model series were introduced, built on the Qwen3-VL foundation model, providing an end-to-end pipeline for high-precision multimodal search by mapping diverse modalities, including text, images, document images, and video, into a unified representation space.

Qwen3-VL-Embedding-8B attains an overall score of 77.8 on MMEB-V2, ranking first among all models (as of January 8, 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f202be0a-34eb-4382-af21-abcc7b40c392",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "94be4455-1d66-4975-94cf-149aa95c02f6",
  "sourceToolAssistantUUID": "f202be0a-34eb-4382-af21-abcc7b40c392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-11T23:36:18.569Z_

Good, both models exist. Now let me get the specific technical details -- embedding dimension, max sequence length, and benchmark scores.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94be4455-1d66-4975-94cf-149aa95c02f6",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfD7sj3EzTjDgSfYM4s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "711cc24e-4895-4e0a-a69a-77a4e5054ce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGRhG9auw6fkoo52JhFXpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 887,
      "cache_creation_input_tokens": 2069,
      "cache_read_input_tokens": 10321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2069,
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

_source line 14 · 2026-05-11T23:36:19.155Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PaT17Ndw2Hk9kaqtP7D1ni`</summary>

```json
{
  "query": "Qwen3-Embedding-0.6B embedding dimension hidden size max sequence length specifications"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "711cc24e-4895-4e0a-a69a-77a4e5054ce7",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfD7sj3EzTjDgSfYM4s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baef633c-c761-422a-8509-cf4e1e1ecae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGRhG9auw6fkoo52JhFXpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 887,
      "cache_creation_input_tokens": 2069,
      "cache_read_input_tokens": 10321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2069,
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

_source line 15 · 2026-05-11T23:36:19.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018rR9kcBj3DyRfeGupvKsdY`</summary>

```json
{
  "query": "Qwen3-Embedding-0.6B MTEB benchmark results performance scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baef633c-c761-422a-8509-cf4e1e1ecae9",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfD7sj3EzTjDgSfYM4s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "047f2e65-1dd6-44d5-9ff3-a7e7898307e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGRhG9auw6fkoo52JhFXpK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 887,
      "cache_creation_input_tokens": 2069,
      "cache_read_input_tokens": 10321,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2069
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 887,
          "output_tokens": 151,
          "cache_read_input_tokens": 10321,
          "cache_creation_input_tokens": 2069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2069,
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

_source line 16 · 2026-05-11T23:36:23.719Z_

<details><summary>↩ Tool result · `toolu_01PaT17Ndw2Hk9kaqtP7D1ni`</summary>

```text
Web search results for query: "Qwen3-Embedding-0.6B embedding dimension hidden size max sequence length specifications"

Links: [{"title":"Qwen/Qwen3-Embedding-0.6B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B"},{"title":"GitHub - QwenLM/Qwen3-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-Embedding"},{"title":"qwen3-embedding:0.6b","url":"https://ollama.com/library/qwen3-embedding:0.6b"},{"title":"Qwen3 Embedding: Advancing Text ...","url":"https://arxiv.org/pdf/2506.05176"},{"title":"Qwen/Qwen3-Embedding-0.6B-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B-GGUF"},{"title":"Qwen3-Embedding-0.6B - Accenture AI Refinery SDK","url":"https://sdk.airefinery.accenture.com/distiller/model_catalog/Embedding/Qwen/Qwen3-Embedding-0.6B/"},{"title":"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen","url":"https://qwenlm.github.io/blog/qwen3-embedding/"},{"title":"README.md · Qwen/Qwen3-Embedding-0.6B at main","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md"},{"title":"Qwen3-0.6B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen3-0-6b"},{"title":"Mastering Text Embedding and Reranker with Qwen3 - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/mastering-text-embedding-and-reranker-with-qwen3_602308"}]

Based on the search results, here are the specifications for Qwen3-Embedding-0.6B:

**Max Sequence Length:** The maximum sequence length is 8192 tokens.

**Embedding Dimension:** The default vector length for Qwen3-Embedding-0.6B is 1024D. However, the embedding model allows for flexible vector definitions across all dimensions, meaning you can customize the output dimension based on your needs.

**General Architecture:** The model is built on the Qwen3 foundation architecture, which follows a dense Transformer decoder design optimized for embedding tasks.

The specific hidden size of the underlying 0.6B base model is not explicitly mentioned in the available documentation, though the model inherits architectural components from the Qwen3-0.6B foundation model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baef633c-c761-422a-8509-cf4e1e1ecae9",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "83ada3e3-da9a-4b2d-9cb2-cbfdb2558fad",
  "sourceToolAssistantUUID": "baef633c-c761-422a-8509-cf4e1e1ecae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T23:36:24.617Z_

<details><summary>↩ Tool result · `toolu_018rR9kcBj3DyRfeGupvKsdY`</summary>

```text
Web search results for query: "Qwen3-Embedding-0.6B MTEB benchmark results performance scores"

Links: [{"title":"Qwen3 Embedding: Advancing Text ...","url":"https://arxiv.org/pdf/2506.05176"},{"title":"GitHub - QwenLM/Qwen3-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-Embedding"},{"title":"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen","url":"https://qwenlm.github.io/blog/qwen3-embedding/"},{"title":"Qwen/Qwen3-Embedding-0.6B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B"},{"title":"Top embedding models on the MTEB leaderboard","url":"https://modal.com/blog/mteb-leaderboard-article"},{"title":"Qwen/Qwen3-Embedding-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-8B"},{"title":"qwen3-embedding","url":"https://ollama.com/library/qwen3-embedding"},{"title":"Qwen3-Embedding-0.6B - Model Info, Parameters, Benchmarks - SiliconFlow\"","url":"https://www.siliconflow.com/models/qwen3-embedding-0-6b"},{"title":"Qwen/Qwen3-Reranker-0.6B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Reranker-0.6B"},{"title":"MTEB Leaderboard - a Hugging Face Space by mteb","url":"https://huggingface.co/spaces/mteb/leaderboard"}]

Based on the search results, here's what I found about the Qwen3-Embedding-0.6B's MTEB benchmark performance:

## MTEB Benchmark Results for Qwen3-Embedding-0.6B

Qwen3-Embedding-0.6B achieves a strong performance on the MTEB multilingual leaderboard with a score of 64.33 and demonstrates excellent results across various tasks including text retrieval, code retrieval, text classification, clustering, and bitext mining.

### Context on the Qwen3 Embedding Series

The Qwen3-Embedding-0.6B is part of a broader embedding model series. The Qwen3 Embedding models are available in three sizes: 0.6B, 4B, and 8B parameters. For comparison, the 8B size embedding model ranks No.1 in the MTEB multilingual leaderboard (as of June 5, 2025, score 70.58).

The 0.6B model serves as the lightweight option in the series, with all reranking evaluation scores based on the top-100 candidates retrieved by the dense embedding model Qwen3-Embedding-0.6B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "047f2e65-1dd6-44d5-9ff3-a7e7898307e5",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "8c70072d-211b-4b1a-81e5-f92c751d7bf8",
  "sourceToolAssistantUUID": "047f2e65-1dd6-44d5-9ff3-a7e7898307e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-11T23:36:28.386Z_

Let me get a few more details to be thorough -- the Qwen3-Embedding-4B specs for comparison, and the exact hidden size of the 0.6B model.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c70072d-211b-4b1a-81e5-f92c751d7bf8",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfDmtE9MhUukCw8Kdcs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfd09af8-4827-41e7-b03b-4802f787c025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4jL57zC8EoFhHpDCF9d6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 12390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2620,
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

_source line 19 · 2026-05-11T23:36:29.869Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XoLY2aKPG9jgAvvkq9fxUN`</summary>

```json
{
  "query": "Qwen3-Embedding-0.6B config.json hidden_size \"hidden_size\" site:huggingface.co"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfd09af8-4827-41e7-b03b-4802f787c025",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfDmtE9MhUukCw8Kdcs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d7c0792-338a-4ae0-8c35-7be5a9ea4ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4jL57zC8EoFhHpDCF9d6k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 12390,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2620
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 12390,
          "cache_creation_input_tokens": 2620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2620,
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

_source line 20 · 2026-05-11T23:36:29.926Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bjh6YxkqtsabPVzScH141C`</summary>

```json
{
  "query": "Qwen3-Embedding-4B embedding dimension MTEB benchmark score specifications"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d7c0792-338a-4ae0-8c35-7be5a9ea4ad9",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfDmtE9MhUukCw8Kdcs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18c162a1-8da3-4b5b-a1b6-fa9ec53c300a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4jL57zC8EoFhHpDCF9d6k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 12390,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2620
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 12390,
          "cache_creation_input_tokens": 2620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2620,
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

_source line 21 · 2026-05-11T23:36:35.514Z_

<details><summary>↩ Tool result · `toolu_01Bjh6YxkqtsabPVzScH141C`</summary>

```text
Web search results for query: "Qwen3-Embedding-4B embedding dimension MTEB benchmark score specifications"

Links: [{"title":"GitHub - QwenLM/Qwen3-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-Embedding"},{"title":"Qwen/Qwen3-Embedding-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-8B"},{"title":"qwen3-embedding","url":"https://ollama.com/library/qwen3-embedding"},{"title":"Qwen/Qwen3-Embedding-4B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-4B"},{"title":"Qwen3 Embedding: Advancing Text ...","url":"https://arxiv.org/pdf/2506.05176"},{"title":"Qwen3-Embedding-4B - Model Info, Parameters, Benchmarks - SiliconFlow\"","url":"https://www.siliconflow.com/models/qwen3-embedding-4b"},{"title":"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen","url":"https://qwenlm.github.io/blog/qwen3-embedding/"},{"title":"Comparative Analysis of Qwen-3 and BGE-M3 Embedding Models for Multilingual Information Retrieval | by Aryan Kumar | Medium","url":"https://medium.com/@mrAryanKumar/comparative-analysis-of-qwen-3-and-bge-m3-embedding-models-for-multilingual-information-retrieval-72c0e6895413"},{"title":"README.md · Qwen/Qwen3-Embedding-4B at main","url":"https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/README.md"},{"title":"Mungert/Qwen3-Embedding-4B-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/Qwen3-Embedding-4B-GGUF"}]

Based on the search results, here are the specifications for Qwen3-Embedding-4B:

## Embedding Dimension

The Qwen3-Embedding-4B model supports context lengths up to 32K and can generate embeddings with dimensions up to 2560. More specifically, the model has embedding dimensions of 2560, and it offers flexible vector dimensions ranging from 32 to 2560.

## MTEB Benchmark Score

The model achieves excellent performance on the MTEB multilingual leaderboard with a score of 69.45.

## Additional Specifications

- **Model Size**: 4B parameters
- **Multilingual Support**: The model supports over 100 languages, along with long-text understanding and reasoning skills
- **Task Coverage**: The model demonstrates outstanding results across various tasks including text retrieval, code retrieval, text classification, clustering, and bitext mining


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18c162a1-8da3-4b5b-a1b6-fa9ec53c300a",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "b5f99ce6-21aa-43b2-ab24-383bc3ae95b7",
  "sourceToolAssistantUUID": "18c162a1-8da3-4b5b-a1b6-fa9ec53c300a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-11T23:36:40.688Z_

<details><summary>↩ Tool result · `toolu_01XoLY2aKPG9jgAvvkq9fxUN`</summary>

```text
Web search results for query: "Qwen3-Embedding-0.6B config.json hidden_size "hidden_size" site:huggingface.co"

Links: [{"title":"Qwen/Qwen3-Embedding-0.6B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B"},{"title":"config.json · Qwen/Qwen3-Embedding-0.6B at d43997c8a1046d1734f8d519effbb424a832a0a2","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/d43997c8a1046d1734f8d519effbb424a832a0a2/config.json"},{"title":"config.json · Qwen/Qwen3-Embedding-0.6B at 6d728645432c51ecc9e94990d9b7be391eaa6579","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/6d728645432c51ecc9e94990d9b7be391eaa6579/config.json"},{"title":"config.json · tomaarsen/Qwen3-Embedding-0.6B-18-layers at main","url":"https://huggingface.co/tomaarsen/Qwen3-Embedding-0.6B-18-layers/blob/main/config.json"},{"title":"Qwen/Qwen3-Embedding-0.6B · Adding ONNX file of this model","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/discussions/31/files"},{"title":"README.md · Qwen/Qwen3-Embedding-0.6B at main","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md"},{"title":"config.json · Qwen/Qwen3-8B at main","url":"https://huggingface.co/Qwen/Qwen3-8B/blob/main/config.json"},{"title":"Qwen/Qwen3-Embedding-0.6B-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B-GGUF"},{"title":"config.json · Qwen/Qwen3-0.6B at main","url":"https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json"},{"title":"Qwen3 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/qwen3"}]

I found search results for the Qwen3-Embedding-0.6B model on Hugging Face. The search returned links to the config.json file, but the actual content of the JSON file itself wasn't displayed in the search results. 

Based on the search results, I can see that:

1. The config.json file for Qwen3-Embedding-0.6B exists at: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/config.json

2. While the search results don't show the full config.json content with the hidden_size value, I can reference related information: For the base Qwen3-0.6B model (which the embedding model is built upon), the hidden_size is 4096.

To view the specific `hidden_size` value in the Qwen3-Embedding-0.6B config.json file, you would need to visit the direct link to the config.json file on Hugging Face. The embedding variant may use a different hidden_size than the base model, so I'd recommend checking the file directly for the accurate value specific to the embedding model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d7c0792-338a-4ae0-8c35-7be5a9ea4ad9",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "0d219bc7-05d8-415f-a403-0fa40fdf5be3",
  "sourceToolAssistantUUID": "6d7c0792-338a-4ae0-8c35-7be5a9ea4ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-11T23:36:43.021Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G85YgEkNcePXq4jgDzEmSD`</summary>

```json
{
  "query": "Qwen3-Embedding-0.6B hidden_size 1024 architecture config parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d219bc7-05d8-415f-a403-0fa40fdf5be3",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfExXTecW91Q1WtE41Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe51a85e-40b7-4ec0-8b49-3452fcb2aae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjqGYhPZtjX6DFwp7CgEHJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 801,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 15010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1318,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-11T23:36:43.473Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019K4QdyGQ3NiA8fiZMsW42E`</summary>

```json
{
  "query": "Qwen3 Embedding model comparison 0.6B 4B 8B MTEB scores table blog"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe51a85e-40b7-4ec0-8b49-3452fcb2aae0",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfExXTecW91Q1WtE41Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ea3f75f-daec-42a7-a9d5-0b62debfa7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjqGYhPZtjX6DFwp7CgEHJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 801,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 15010,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1318
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 801,
          "output_tokens": 133,
          "cache_read_input_tokens": 15010,
          "cache_creation_input_tokens": 1318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1318,
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

_source line 25 · 2026-05-11T23:36:48.501Z_

<details><summary>↩ Tool result · `toolu_01G85YgEkNcePXq4jgDzEmSD`</summary>

```text
Web search results for query: "Qwen3-Embedding-0.6B hidden_size 1024 architecture config parameters"

Links: [{"title":"Qwen/Qwen3-Embedding-0.6B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B"},{"title":"GitHub - QwenLM/Qwen3-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-Embedding"},{"title":"Qwen3-0.6B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen3-0-6b"},{"title":"Qwen3-Embedding-0.6B - Accenture AI Refinery SDK","url":"https://sdk.airefinery.accenture.com/distiller/model_catalog/Embedding/Qwen/Qwen3-Embedding-0.6B/"},{"title":"Qwen3-embedding-0.6B 的embedding输出维度如何配置成512？ · Issue #177 · QwenLM/Qwen3-Embedding","url":"https://github.com/QwenLM/Qwen3-Embedding/issues/177"},{"title":"Qwen/Qwen3-Embedding-0.6B-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B-GGUF"},{"title":"Qwen3 Embedding: Advancing Text ...","url":"https://arxiv.org/pdf/2506.05176"},{"title":"qwen3-embedding:0.6b","url":"https://ollama.com/library/qwen3-embedding:0.6b"},{"title":"Qwen3 Embedding","url":"https://simonwillison.net/2025/Jun/8/qwen3-embedding/"},{"title":"Qwen3-TTS-12Hz-0.6B-Base fine-tuning fails due to embedding dimension mismatch (2048 vs 1024) · Issue #198 · QwenLM/Qwen3-TTS","url":"https://github.com/QwenLM/Qwen3-TTS/issues/198"}]

Based on the search results, here is the information about Qwen3-Embedding-0.6B architecture configuration parameters:

## Model Architecture

Qwen3-Embedding-0.6B model is built on the Qwen3 foundation architecture, which follows a dense Transformer decoder design optimized for embedding tasks.

## Key Configuration Parameters

**Hidden Size:** The model has an embedding dimension of up to 1024, supporting user-defined output dimensions ranging from 32 to 1024. Qwen3 0.6B produces 1024 length embedding vectors.

## Model Specifications

- **Model Type:** Text Embedding
- **Parameters:** 0.6B
- **Context Length:** 32k
- **Supported Languages:** 100+ Languages

## Special Features

The model is instruction aware and supports MRL (Matryoshka Representation Learning) for flexible embedding vector dimensions, which allows users to configure custom output dimensions between 32 and 1024.

For more detailed architecture specifications (such as the exact number of layers and attention mechanisms), you may want to refer to the official Hugging Face model card or the arXiv paper referenced in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe51a85e-40b7-4ec0-8b49-3452fcb2aae0",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "3d1ca398-9436-4c2c-9f9e-272ec3aec1bd",
  "sourceToolAssistantUUID": "fe51a85e-40b7-4ec0-8b49-3452fcb2aae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T23:36:49.324Z_

<details><summary>↩ Tool result · `toolu_019K4QdyGQ3NiA8fiZMsW42E`</summary>

```text
Web search results for query: "Qwen3 Embedding model comparison 0.6B 4B 8B MTEB scores table blog"

Links: [{"title":"Qwen/Qwen3-Embedding-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-8B"},{"title":"qwen3-embedding","url":"https://ollama.com/library/qwen3-embedding"},{"title":"Qwen/Qwen3-Embedding-0.6B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B"},{"title":"GitHub - QwenLM/Qwen3-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-Embedding"},{"title":"Qwen/Qwen3-Embedding-4B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-4B"},{"title":"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models","url":"https://arxiv.org/html/2506.05176v1"},{"title":"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen","url":"https://qwenlm.github.io/blog/qwen3-embedding/"},{"title":"Comparative Analysis of Qwen-3 and BGE-M3 Embedding Models for Multilingual Information Retrieval | by Aryan Kumar | Medium","url":"https://medium.com/@mrAryanKumar/comparative-analysis-of-qwen-3-and-bge-m3-embedding-models-for-multilingual-information-retrieval-72c0e6895413"},{"title":"Qwen/Qwen3-Embedding-0.6B-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-0.6B-GGUF"},{"title":"Qwen3-Embedding-4B: Text-to-Text model — overview, use cases, alternatives","url":"https://www.aimodels.fyi/models/huggingFace/qwen3-embedding-4b-qwen"}]

Based on the search results, I found information about the Qwen3 Embedding model comparison with MTEB scores. Here's what I found:

## Qwen3 Embedding Model Comparison

The Qwen3 Embedding model series provides a comprehensive range of text embeddings models in various sizes (0.6B, 4B, and 8B).

### MTEB Scores

Qwen3-Embedding-8B scores 70.58 on MTEB versus 69.45 for the 4B model, and Qwen3-Embedding-0.6B scores 64.33 on MTEB with only 1024-dimensional embeddings.

The 8B size embedding model ranks No.1 in the MTEB multilingual leaderboard (as of June 5, 2025, score 70.58).

### Model Characteristics

Models are available at 0.6B, 4B, and 8B parameters to balance performance and computational cost with embedding dimensions of 1024, 2560, and 4096 respectively.

### Performance Comparison

The Qwen3-Embedding-4B/8B models achieve the best performance, and the smallest model, Qwen3-Embedding-0.6B, only lags behind the best-performing baseline method (Gemini-Embedding), despite having only 0.6B parameters.

For more detailed benchmark evaluation and comparison tables, you can refer to the official blog and GitHub for comprehensive information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ea3f75f-daec-42a7-a9d5-0b62debfa7a3",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "a2f012828444862c9",
  "type": "user",
  "uuid": "5f7a058f-d625-4a27-9764-7547876c13a4",
  "sourceToolAssistantUUID": "2ea3f75f-daec-42a7-a9d5-0b62debfa7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-11T23:37:09.582Z_

I now have comprehensive information. Here is the full report.

---

## Findings: Qwen3-Embedding-0.6B and Qwen3-Embedding-4B

### 1. Qwen3-Embedding-0.6B -- Confirmed to Exist

The model is real and publicly available on HuggingFace at `Qwen/Qwen3-Embedding-0.6B`. It was released by the Qwen team (Alibaba) and is part of the Qwen3-Embedding series introduced around June 2025, with an accompanying paper on arXiv (2506.05176).

### 2. Technical Specifications (Qwen3-Embedding-0.6B)

| Property | Value |
|---|---|
| **Parameters** | 0.6B |
| **Embedding Dimension** | **1024** (default/max); supports flexible dimensions from 32 to 1024 via Matryoshka Representation Learning (MRL) |
| **Max Sequence Length** | **32,768 tokens** (32k context window) |
| **Architecture** | Dense Transformer decoder (based on Qwen3-0.6B foundation model), adapted for embedding |
| **Languages** | 100+ languages |
| **Instruction-aware** | Yes -- supports user-defined task instructions to improve performance |

### 3. Benchmark Performance (MTEB Multilingual Leaderboard)

| Model | MTEB Score | Embedding Dim |
|---|---|---|
| **Qwen3-Embedding-0.6B** | **64.33** | 1024 |
| Qwen3-Embedding-4B | 69.45 | 2560 |
| Qwen3-Embedding-8B | 70.58 (ranked #1 as of June 2025) | 4096 |

The 0.6B variant, despite its small size, only lags behind the best-performing baseline (Gemini-Embedding) and covers tasks including text retrieval, code retrieval, text classification, text clustering, and bitext mining.

### 4. Qwen3-Embedding-4B -- Confirmed to Exist

Yes, `Qwen/Qwen3-Embedding-4B` also exists on HuggingFace. It serves as the mid-tier option in the series:

- **Parameters**: 4B
- **Embedding Dimension**: 2560 (flexible from 32 to 2560)
- **Max Sequence Length**: 32k
- **MTEB Score**: 69.45

Both models are suitable for use as frozen embedding backbones. For a proposal using Qwen3-Embedding-0.6B as a frozen encoder for trajectory step encoding, the key practical considerations are:

- The 1024-dimensional output is quite manageable for downstream projection layers
- At 0.6B parameters it is lightweight enough to keep frozen without excessive memory overhead
- The 32k context window provides ample room for encoding long trajectory steps
- The 4B variant is a reasonable ablation choice, offering +5 MTEB points at the cost of ~6.7x more parameters and 2560-dim embeddings

Sources:
- [Qwen3-Embedding-0.6B on HuggingFace](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)
- [Qwen3-Embedding-4B on HuggingFace](https://huggingface.co/Qwen/Qwen3-Embedding-4B)
- [Qwen3-Embedding-8B on HuggingFace](https://huggingface.co/Qwen/Qwen3-Embedding-8B)
- [Qwen3 Embedding arXiv Paper (2506.05176)](https://arxiv.org/abs/2506.05176)
- [Qwen3 Embedding Official Blog](https://qwenlm.github.io/blog/qwen3-embedding/)
- [QwenLM/Qwen3-Embedding GitHub](https://github.com/QwenLM/Qwen3-Embedding)
- [Qwen3-Embedding Collection on HuggingFace](https://huggingface.co/collections/Qwen/qwen3-embedding)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f7a058f-d625-4a27-9764-7547876c13a4",
  "isSidechain": true,
  "agentId": "a2f012828444862c9",
  "requestId": "req_011CawfFbXC5sbJGFQ6jAHVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "681f7a6f-5ceb-4874-8aba-714aefca2eac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe7Fkk5hUar5Z1BWjRN7bP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2790,
      "cache_read_input_tokens": 16328,
      "output_tokens": 1048,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2790
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1048,
          "cache_read_input_tokens": 16328,
          "cache_creation_input_tokens": 2790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2790,
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
