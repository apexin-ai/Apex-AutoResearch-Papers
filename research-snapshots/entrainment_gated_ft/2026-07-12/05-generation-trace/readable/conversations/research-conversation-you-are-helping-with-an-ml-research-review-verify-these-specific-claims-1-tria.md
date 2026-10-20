# Research conversation: You are helping with an ML research review. Verify these specific claims: 1. **TriAttention (April 2026)**: The proposal

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a05adfcf7f25b2d24.jsonl`
- **Structured JSON:** [`ef7a756f4faaa4f5e1fc.json`](../../sessions/ef/ef7a756f4faaa4f5e1fc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-10T19:35:50.017Z_

You are helping with an ML research review. Verify these specific claims:

1. **TriAttention (April 2026)**: The proposal claims it achieves "10.7x memory reduction, 6.3x throughput on MATH-500 (1,405 vs 223 tokens/s), and 2.5x throughput at matched accuracy on AIME25 with a vLLM plugin." Previous review rounds flagged that the 6.3x MATH-500 number couldn't be verified. Search for:
   - "TriAttention trigonometric KV compression reasoning 2026"
   - "TriAttention pre-RoPE concentration KV cache"
   - Try to find the actual paper and verify these specific numbers

2. **Polar Sparsity (NeurIPS 2025)**: The proposal says it "reveals that MLP contextual sparsity diminishes with batch size as active neuron sets converge toward dense, and pivots to attention head sparsity which remains stable and batch-invariant; custom Triton kernels for selective head attention achieve 2.2x end-to-end speedup." Verify:
   - Is it NeurIPS 2025?
   - Does it have open-source Triton kernels at github.com/susavlsh10/Polar-Sparsity?
   - Does it achieve 2.2x speedup?
   - Does it show MLP sparsity diminishes with batch size?

3. **AMP (IJCNN 2025)**: Claims "distributing pruning across head+MLP jointly outperforms single-axis pruning (61.02% vs 37.63% attention-only or 56.93% MLP-only at 30% compression)." Verify these specific numbers.

4. **R-KV**: Claims open-source code at github.com/Zefan-Cai/R-KV. Verify the repo exists and what it does.

Use WebSearch and WebFetch as needed. Report exactly what you find for each claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "2d539f78-55f1-4b69-b8a7-dee28fa61363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:35:50.021Z_

```json
{
  "parentUuid": "2d539f78-55f1-4b69-b8a7-dee28fa61363",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "0a95819d-8d11-4b31-9671-16ac86fe4904",
  "timestamp": "2026-05-10T19:35:50.021Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:35:52.362Z_



I'll systematically verify each claim. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a95819d-8d11-4b31-9671-16ac86fe4904",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT4phVMupxTdcCqUxFN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7478c523-b5b6-4b6d-8754-5d5e413c4865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LamYKUxfzpskjZ8W1BYyrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1004,
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

_source line 4 · 2026-05-10T19:35:52.477Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RsqZLh1CFXVbZzbqXeCd1p`</summary>

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
  "parentUuid": "7478c523-b5b6-4b6d-8754-5d5e413c4865",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT4phVMupxTdcCqUxFN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19da7a9a-9ef5-4fac-b02f-963a705d20c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LamYKUxfzpskjZ8W1BYyrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 7304,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 1004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1004,
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

_source line 5 · 2026-05-10T19:35:52.480Z_

<details><summary>↩ Tool result · `toolu_01RsqZLh1CFXVbZzbqXeCd1p`</summary>

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
  "parentUuid": "19da7a9a-9ef5-4fac-b02f-963a705d20c9",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "874fad2c-0f77-4bd9-8fdd-a402fab10302",
  "sourceToolAssistantUUID": "19da7a9a-9ef5-4fac-b02f-963a705d20c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:35:55.149Z_



Now let me search for all four claims in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "874fad2c-0f77-4bd9-8fdd-a402fab10302",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT51MCHybXX2xQLdkR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7e89fdb-e962-40ed-897f-d8dcb7d389a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJ4KAeZPyLNoCbDbKeAQaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 7 · 2026-05-10T19:35:59.970Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H5rhxD4jZxPHJEsrsaKXSr`</summary>

```json
{
  "query": "TriAttention trigonometric KV compression reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7e89fdb-e962-40ed-897f-d8dcb7d389a9",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT51MCHybXX2xQLdkR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80e9c26d-7ed7-4017-a1a8-826b814ce358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJ4KAeZPyLNoCbDbKeAQaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 8 · 2026-05-10T19:36:00.213Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N6q3LfrMbHCMB1neQj1XM1`</summary>

```json
{
  "query": "Polar Sparsity NeurIPS 2025 attention head sparsity batch invariant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80e9c26d-7ed7-4017-a1a8-826b814ce358",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT51MCHybXX2xQLdkR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d69cfb79-d613-404a-9f03-28fb635cc3c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJ4KAeZPyLNoCbDbKeAQaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 9 · 2026-05-10T19:36:00.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DanKq4pJmnPi68Q4iwfANc`</summary>

```json
{
  "query": "AMP IJCNN 2025 pruning head MLP jointly 61.02%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d69cfb79-d613-404a-9f03-28fb635cc3c5",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT51MCHybXX2xQLdkR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10737f67-2717-485d-82bf-b715d7fc459c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJ4KAeZPyLNoCbDbKeAQaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 10 · 2026-05-10T19:36:00.607Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019AK45d4xrEBptBYkmskzNb`</summary>

```json
{
  "query": "R-KV Zefan Cai KV cache github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10737f67-2717-485d-82bf-b715d7fc459c",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT51MCHybXX2xQLdkR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75ec3735-6717-48f0-9223-6db8687ebcc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJ4KAeZPyLNoCbDbKeAQaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 11 · 2026-05-10T19:36:05.272Z_

<details><summary>↩ Tool result · `toolu_01DanKq4pJmnPi68Q4iwfANc`</summary>

```text
Web search results for query: "AMP IJCNN 2025 pruning head MLP jointly 61.02%"

Links: [{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250421174G/abstract"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/html/2504.21174v1"},{"title":"IJCNN 2025","url":"https://2025.ijcnn.org/"},{"title":"[2504.21174] Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/abs/2504.21174"},{"title":"IJCNN: International Joint Conference on Neural Network 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1573"},{"title":"Call for Papers | IJCNN 2025","url":"https://2025.ijcnn.org/authors/call-for-papers"},{"title":"Program at a Glance | IJCNN 2025","url":"https://2025.ijcnn.org/program/program-at-a-glance"},{"title":"IJCNN Home","url":"https://www.inns.org/ijcnn-home"},{"title":"Registration | IJCNN 2025","url":"https://2025.ijcnn.org/registration"},{"title":"Program | IJCNN 2025","url":"https://2025.ijcnn.org/program/program"}]

I found the research paper you're looking for. AMP (Attention Heads and MLP Pruning) is a novel structured pruning method that efficiently compresses LLMs by removing less critical structures within Multi-Head Attention (MHA) and Multilayer Perceptron (MLP). 

The paper is to be published in the International Joint Conference on Neural Networks (IJCNN) 2025. 

Regarding the 61.02% metric in your query: For a compression ratio of 30.03%, the results are 60.72%, 61.02%, 60.10% and 59.18%, which appears to be the performance metric you were referencing. This represents the average accuracy results across tasks at different epochs of fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10737f67-2717-485d-82bf-b715d7fc459c",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "80cecde0-5fe5-44f3-a1c9-9e7f98c6568f",
  "sourceToolAssistantUUID": "10737f67-2717-485d-82bf-b715d7fc459c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:36:05.819Z_

<details><summary>↩ Tool result · `toolu_01H5rhxD4jZxPHJEsrsaKXSr`</summary>

```text
Web search results for query: "TriAttention trigonometric KV compression reasoning 2026"

Links: [{"title":"GitHub - WeianMao/triattention: TriAttention — Efficient long reasoning with trigonometric KV cache compression. Enables OpenClaw local deployment on memory-constrained GPUs.","url":"https://github.com/WeianMao/triattention"},{"title":"Paper page - TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://huggingface.co/papers/2604.04921"},{"title":"[2604.04921] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921"},{"title":"Researchers from MIT, NVIDIA, and Zhejiang University Propose TriAttention: A KV Cache Compression Method That Matches Full Attention at 2.5× Higher Throughput - MarkTechPost","url":"https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/"},{"title":"TriAttention | Efficient KV Cache Compression for Long-Context Reasoning","url":"https://weianmao.github.io/tri-attention-project-page/"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV","url":"https://www.opentrain.ai/papers/triattention-efficient-long-reasoning-with-trigonometric-kv-compression--arxiv-2604.04921/"},{"title":"[2604.04921v1] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921v1"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/html/2604.04921v1"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression | alphaXiv","url":"https://www.alphaxiv.org/overview/2604.04921"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://papers.fzhiy.net/papers/2604-04921.html"}]

Based on the search results, here's what I found about TriAttention:

## Overview

TriAttention is a method for efficient long reasoning with trigonometric KV compression, proposed by researchers from MIT, NVIDIA, and Zhejiang University. The research addresses the problem that extended reasoning in large language models (LLMs) creates severe KV cache memory bottlenecks.

## Key Innovation

The method observes that Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions in the pre-RoPE space. This concentration causes queries to preferentially attend to keys at specific distances (e.g., nearest keys), with the centers determining which distances are preferred via a trigonometric series.

## Performance Results

On AIME25 with 32K-token generation, TriAttention matches Full Attention reasoning accuracy while achieving 2.5× higher throughput or 10.7× KV memory reduction, whereas leading baselines achieve only about half the accuracy at the same efficiency.

## Practical Applications

TriAttention is OpenClaw compatible and enables local deployment on 24GB RTX 4090. As of April 2026, TriAttention now supports AR video generation with KV cache compression.

The paper was published on arXiv in 2026 with identifier 2604.04921, and the project is licensed under Apache License 2.0.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80e9c26d-7ed7-4017-a1a8-826b814ce358",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "531fb40d-3abd-43cc-b079-d7eff4f14235",
  "sourceToolAssistantUUID": "80e9c26d-7ed7-4017-a1a8-826b814ce358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:36:07.852Z_

<details><summary>↩ Tool result · `toolu_01N6q3LfrMbHCMB1neQj1XM1`</summary>

```text
Web search results for query: "Polar Sparsity NeurIPS 2025 attention head sparsity batch invariant"

Links: [{"title":"NeurIPS Poster Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117070"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with ...","url":"https://susavlsh10.github.io/files/Polar_Sparsity_NeurIPS_2025_CameraReady.pdf"},{"title":"Polar Sparsity: High Throughput Batched LLM","url":"https://openreview.net/pdf?id=cg2S1qqNSq"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity | OpenReview","url":"https://openreview.net/forum?id=cg2S1qqNSq"},{"title":"[2505.14884] Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/abs/2505.14884"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://arxiv.org/pdf/2505.14884"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://openreview.net/pdf/43bf702e03ce0cb3a890cf8a35f3ded98d30b94d.pdf"},{"title":"[NeurIPS 2025] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiviq.substack.com/p/neurips-2025-gated-attention-for"},{"title":"GitHub - qiuzh20/gated_attention: The official implementation for [NeurIPS2025 Oral] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free · GitHub","url":"https://github.com/qiuzh20/gated_attention"}]

Based on the search results, I found detailed information about Polar Sparsity at NeurIPS 2025:

## Overview

Polar Sparsity highlights a key shift in sparsity importance from MLP to Attention layers as batch size and sequence length scale, where attention head sparsity remains stable and batch-invariant.

## Key Insight on Batch-Invariant Head Sparsity

While MLP layers become more compute-efficient under batching with their sparsity vanishing, attention becomes increasingly more expensive at scale, while their head sparsity remains stable and batch-invariant. Unlike MLP sparsity, this form of sparsity is invariant to batching, as each sequence computes attention independently.

## Selective Head Attention Approach

The work develops Selective Head Attention with hardware-efficient, sparsity-aware GPU kernels, delivering up to 2.2× end-to-end speedups for models like OPT, LLaMA-2 & 3, Qwen, Mistral across various batch sizes and sequence lengths without compromising accuracy.

## Technical Implementation

At each transformer layer, only the top-k attention heads, ranked by output L2 norm, are activated, while the outputs of non-activated heads are masked to zero. This is the first work to demonstrate that contextual sparsity can scale effectively to large batch sizes, delivering substantial inference acceleration with minimal changes, making Polar Sparsity practical for large-scale, high-throughput LLM deployment systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d69cfb79-d613-404a-9f03-28fb635cc3c5",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "73ade140-0d56-4d12-b861-8ee0d73f0d8a",
  "sourceToolAssistantUUID": "d69cfb79-d613-404a-9f03-28fb635cc3c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:36:08.963Z_

<details><summary>↩ Tool result · `toolu_019AK45d4xrEBptBYkmskzNb`</summary>

```text
Web search results for query: "R-KV Zefan Cai KV cache github"

Links: [{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://zefan-cai.github.io/R-KV.page/"},{"title":"GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub","url":"https://github.com/Zefan-Cai/KVCache-Factory"},{"title":"Releases · Zefan-Cai/R-KV","url":"https://github.com/Zefan-Cai/R-KV/releases"},{"title":"GitHub - Zefan-Cai/Awesome-LLM-KV-Cache: Awesome-LLM-KV-Cache: A curated list of 📙Awesome LLM KV Cache Papers with Codes.","url":"https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache"},{"title":"KVCache-Factory/README.md at main · Zefan-Cai/KVCache-Factory","url":"https://github.com/Zefan-Cai/KVCache-Factory/blob/main/README.md"},{"title":"Awesome-LLM-KV-Cache/README.md at main · Zefan-Cai/Awesome-LLM-KV-Cache","url":"https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache/blob/main/README.md"},{"title":"Zefan-Cai (Zefan Cai) · GitHub","url":"https://github.com/Zefan-Cai"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"Zefan Cai on X: \"🚀 Introducing R-KV: Redundancy-aware KV-cache compression for reasoning LLMs. Shrink the cache, keep the brains —10 % cache → ≈100 % accuracy, 90 % memory saved, 6.6× throughput. 🌏 Page 🔗 https://t.co/viGvxJtcsh 📖 Paper 🔗 https://t.co/Tzm2f0gEkG\" / X","url":"https://x.com/Zefan_Cai/status/1929729587225022632"}]

Here are the search results for R-KV by Zefan Cai:

## Main Project: R-KV

R-KV is a NeurIPS 2025 paper on Redundancy-aware KV Cache Compression for Reasoning Models. The GitHub repository is located at: **https://github.com/Zefan-Cai/R-KV**

### What R-KV Does

R-KV solves the KV cache bloat problem by ranking tokens on-the-fly for both importance and non-redundancy, retaining only the informative, diverse ones. It addresses the challenge that large language models relying on chain-of-thought or self-reflection produce very long outputs that bloat the key–value cache during inference.

### Key Features

- Up to 90% KV-cache memory savings with zero—sometimes negative—accuracy loss
- Plug-and-play: a lightweight wrapper for any autoregressive LLM
- Training-free: drop straight into inference or RL roll-outs—no finetuning required

### Performance Results

R-KV attains parity with 10–34% cache and even beats the FullKV baseline at 10%. At 16% (Llama-8B) or 33% (Qwen-14B) cache, R-KV reaches 105% of FullKV accuracy—evidence that trimming redundant tokens can improve reasoning quality.

## Related Projects by Zefan Cai

- **KVCache-Factory**: https://github.com/Zefan-Cai/KVCache-Factory - Unified KV Cache Compression Methods for Auto-Regressive Models
- **Awesome-LLM-KV-Cache**: https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache - A curated list of Awesome LLM KV Cache Papers with Codes


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75ec3735-6717-48f0-9223-6db8687ebcc1",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "a621bef4-a93c-4e8a-87eb-0e557f700829",
  "sourceToolAssistantUUID": "75ec3735-6717-48f0-9223-6db8687ebcc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T19:36:13.310Z_

Good, I have initial results. Now let me dig deeper into each claim to verify the specific numbers. Let me fetch the actual paper/pages for TriAttention (MATH-500 throughput numbers), Polar Sparsity (GitHub repo and speedup), and AMP (specific accuracy numbers).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a621bef4-a93c-4e8a-87eb-0e557f700829",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT6DftEGWAeFFfCKLF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e8378c5-9bea-4fad-b988-05c62925811b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Pp2JV8eTVLJn1qnDUDA4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4083,
      "cache_read_input_tokens": 10220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4083,
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

_source line 16 · 2026-05-10T19:36:16.750Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y6AKdZvTcdjTeW1m6ofM7v`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.04921",
  "prompt": "Extract all specific performance numbers mentioned in this paper abstract/summary. Specifically look for: MATH-500 throughput numbers (tokens/s), 6.3x throughput claim, 1405 vs 223 tokens/s, 10.7x memory reduction, 2.5x throughput on AIME25, and any mention of a vLLM plugin."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e8378c5-9bea-4fad-b988-05c62925811b",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT6DftEGWAeFFfCKLF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c97d12f-99b9-4b12-ad8a-77b260806e36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Pp2JV8eTVLJn1qnDUDA4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4083,
      "cache_read_input_tokens": 10220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4083,
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

_source line 17 · 2026-05-10T19:36:18.685Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JHyvXL9hbKdH5zjdKkebaU`</summary>

```json
{
  "url": "https://github.com/susavlsh10/Polar-Sparsity",
  "prompt": "Does this repository exist? What does it contain? Does it have Triton kernels? What speedup numbers are claimed? Look for 2.2x end-to-end speedup claim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c97d12f-99b9-4b12-ad8a-77b260806e36",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT6DftEGWAeFFfCKLF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1aee271e-e3e3-4bde-a760-7f16ac802509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Pp2JV8eTVLJn1qnDUDA4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4083,
      "cache_read_input_tokens": 10220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4083,
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

_source line 18 · 2026-05-10T19:36:20.488Z_

<details><summary>↩ Tool result · `toolu_01Y6AKdZvTcdjTeW1m6ofM7v`</summary>

```text
# Performance Numbers from TriAttention Paper

Based on the abstract provided, here are the specific performance metrics mentioned:

**AIME25 Results (32K-token generation):**
- "2.5x higher throughput or 10.7x KV memory reduction" compared to Full Attention while matching accuracy
- Leading baselines achieve only about half the accuracy at the same efficiency levels

**Not Found in This Content:**
The following metrics you requested are **not mentioned** in the provided abstract/summary:
- MATH-500 throughput numbers (tokens/s)
- 6.3x throughput claim
- 1405 vs 223 tokens/s comparison
- Any vLLM plugin reference

The document confirms TriAttention enables model deployment on consumer GPUs by reducing KV memory requirements substantially, but the specific throughput measurements in tokens/second that you referenced do not appear in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c97d12f-99b9-4b12-ad8a-77b260806e36",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "0880c5b2-6d6e-4764-8a60-d73c9d913256",
  "sourceToolAssistantUUID": "8c97d12f-99b9-4b12-ad8a-77b260806e36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T19:36:21.567Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YMzuPuAsaYr7X2d9aWyS8H`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.21174",
  "prompt": "Extract all specific accuracy numbers from this paper. Specifically look for: 61.02% vs 37.63% attention-only or 56.93% MLP-only at 30% compression. What are the exact numbers for joint pruning vs single-axis pruning? Is this an IJCNN 2025 paper?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0880c5b2-6d6e-4764-8a60-d73c9d913256",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT6DftEGWAeFFfCKLF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b25c2eb4-f522-4364-921a-357bfa25cc6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Pp2JV8eTVLJn1qnDUDA4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4083,
      "cache_read_input_tokens": 10220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4083,
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

_source line 20 · 2026-05-10T19:36:22.666Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UwSMDFJ5JtMDFGNW6MwP9p`</summary>

```json
{
  "url": "https://github.com/Zefan-Cai/R-KV",
  "prompt": "Does this repository exist? What does R-KV do? What is the description? Is it NeurIPS 2025? What code/tools does it provide?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b25c2eb4-f522-4364-921a-357bfa25cc6d",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT6DftEGWAeFFfCKLF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54ede71b-0964-4022-99ae-188609591c38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Pp2JV8eTVLJn1qnDUDA4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4083,
      "cache_read_input_tokens": 10220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4083,
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

_source line 21 · 2026-05-10T19:36:23.630Z_

<details><summary>↩ Tool result · `toolu_01JHyvXL9hbKdH5zjdKkebaU`</summary>

```text
# Polar Sparsity Repository Analysis

**Repository Existence:** Yes, this repository exists at `susavlsh10/Polar-Sparsity` on GitHub.

**Contents:** The repository contains a framework for efficient sparse inference in large language models. Key components include:

- Router data collection and training modules (MLP and attention routers)
- Custom Triton kernel implementations for selective computation
- Benchmarking and evaluation tools
- End-to-end sparse generation capabilities

**Triton Kernels:** Yes, the repository includes custom Triton kernels located in `HybridTensor/triton/`. These implement selective GEMM operations for sparse MLPs and sparse multi-head attention layers.

**Speedup Claims:** The provided content does not explicitly mention a "2.2x end-to-end speedup" claim. The README describes benchmarking scripts for measuring kernel speedups but does not state specific speedup numbers in the excerpt provided. To find such claims, you would need to consult the actual paper (referenced as arXiv:2505.14884) or additional documentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1aee271e-e3e3-4bde-a760-7f16ac802509",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "9772e50b-faec-49ec-b950-c0303c92615e",
  "sourceToolAssistantUUID": "1aee271e-e3e3-4bde-a760-7f16ac802509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:36:24.918Z_

<details><summary>↩ Tool result · `toolu_01YMzuPuAsaYr7X2d9aWyS8H`</summary>

```text
# Response Based on Available Content

I cannot extract the specific accuracy numbers you're requesting (61.02% vs 37.63%, 56.93%, etc.) because **they do not appear in the webpage content provided**.

The page contains only the abstract and metadata for arXiv paper 2504.21174. The abstract mentions that "AMP surpasses the current state-of-the-art on commonsense reasoning tasks by up to 1.49 percentage points, achieving a 30% pruning ratio with minimal impact," but does not provide the granular comparisons between joint pruning versus single-axis pruning approaches.

**Regarding publication venue:** Yes, the paper is confirmed as an IJCNN 2025 paper. The submission information states: "To be published in International Joint Conference on Neural Networks (IJCNN), 2025"

To obtain the specific numerical comparisons you're seeking, you would need to review the full paper PDF or HTML version, which would contain the detailed results tables comparing different pruning strategies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b25c2eb4-f522-4364-921a-357bfa25cc6d",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "d1c9759b-bbf1-4b0d-a9d5-b10af9ba487c",
  "sourceToolAssistantUUID": "b25c2eb4-f522-4364-921a-357bfa25cc6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T19:36:28.528Z_

<details><summary>↩ Tool result · `toolu_01UwSMDFJ5JtMDFGNW6MwP9p`</summary>

```text
# R-KV Repository Analysis

**Does it exist?** Yes, this is an active GitHub repository by Zefan-Cai with 1.2k stars and 192 forks.

**What is R-KV?** R-KV is a method for compressing the key-value (KV) cache during inference in large language models, particularly those using chain-of-thought reasoning. The project tagline states: "Shrink the cache, keep the brains."

**Description:** The tool addresses memory bloat from lengthy reasoning outputs in models like DeepSeek-R1. Rather than keeping all generated tokens in the KV cache, R-KV intelligently discards redundant tokens while maintaining accuracy. According to the repository, it achieves approximately "100% accuracy with only 10% of the cache" and provides "90% memory savings."

**NeurIPS 2025 Status?** Yes, the title explicitly indicates "[NeurIPS 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models."

**Code/Tools Provided:**
- Core rkv Python package (installable via `pip install -e .`)
- Integration implementations for HuggingFace, vLLM, SGLang, and FlashInfer
- Evaluation toolkit with math benchmark support (MATH-500, AIME 2024)
- Visualization scripts in Jupyter notebooks
- Bash scripts for running inference and evaluation

The method operates training-free during decoding by scoring tokens for both importance and redundancy, then retaining only the most valuable ones.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54ede71b-0964-4022-99ae-188609591c38",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "3d94295b-b16f-4e86-82f1-7123d68c4886",
  "sourceToolAssistantUUID": "54ede71b-0964-4022-99ae-188609591c38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T19:36:34.839Z_

Good progress. Now I need to dig deeper for the specific numbers that weren't in the abstracts. Let me fetch the full HTML paper for TriAttention (for MATH-500 numbers) and the AMP full paper (for the specific accuracy comparison numbers).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d94295b-b16f-4e86-82f1-7123d68c4886",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT7fF3aSL9UHNsGWcKY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fb08af1-c826-460e-9daf-b002c4373816",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmGCHjMEvMHePeFWSx79UG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1830,
      "cache_read_input_tokens": 14303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1830,
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

_source line 25 · 2026-05-10T19:36:36.929Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TAoVHdnN3uGjyoYLAyc7yG`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.04921v1",
  "prompt": "Search for all mentions of MATH-500, tokens/s, throughput numbers, 6.3x, 1405, 223, and vLLM. Extract exact numbers for MATH-500 throughput and any vLLM plugin mentions. Also look for any throughput comparison tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fb08af1-c826-460e-9daf-b002c4373816",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT7fF3aSL9UHNsGWcKY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14c3e925-fcaa-4c1b-815b-e76bf343a14e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmGCHjMEvMHePeFWSx79UG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1830,
      "cache_read_input_tokens": 14303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1830,
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

_source line 26 · 2026-05-10T19:36:39.808Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Pf1YhYypuhHthQU1bFP4uh`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.21174v1",
  "prompt": "Find the specific numbers comparing joint pruning vs single-axis pruning. Look for: 61.02%, 37.63% (attention-only), 56.93% (MLP-only) at 30% compression. Search for any tables comparing AMP (joint head+MLP pruning) versus attention-only pruning versus MLP-only pruning. Extract the exact accuracy numbers from any such comparison tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14c3e925-fcaa-4c1b-815b-e76bf343a14e",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT7fF3aSL9UHNsGWcKY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52539696-21a3-4432-a3ac-642f0ac30643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmGCHjMEvMHePeFWSx79UG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1830,
      "cache_read_input_tokens": 14303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1830,
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

_source line 27 · 2026-05-10T19:36:40.473Z_

<details><summary>↩ Tool result · `toolu_01TAoVHdnN3uGjyoYLAyc7yG`</summary>

```text
# TriAttention Performance Analysis

## MATH-500 Throughput Numbers

The paper reports specific throughput metrics for MATH-500 evaluation:

- **Full Attention**: 222.8 tokens/second
- **TriAttention**: 1,405.2 tokens/second
- **Speedup**: **6.3×** higher throughput

This comparison appears in Table 4 of the document, where "TriAttention achieves 6.3× higher throughput while maintaining comparable accuracy (68.4% vs. 69.6%)."

## Additional Context

The evaluation used a KV budget of 1,024 tokens for TriAttention versus no compression for Full Attention baseline. Both were tested on NVIDIA A100 80GB GPUs with bfloat16 precision and FlashAttention-2.

The paper does **not mention vLLM** or any vLLM plugin integration in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14c3e925-fcaa-4c1b-815b-e76bf343a14e",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "cf35ecbe-0619-4d3a-9205-23c1da305f62",
  "sourceToolAssistantUUID": "14c3e925-fcaa-4c1b-815b-e76bf343a14e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-10T19:36:41.155Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LzLtEKbUT5nn5MjBrqyJys`</summary>

```json
{
  "url": "https://weianmao.github.io/tri-attention-project-page/",
  "prompt": "Look for any mentions of MATH-500 throughput, 6.3x speedup, 1405 tokens/s, 223 tokens/s, vLLM plugin, or any throughput comparison tables. Extract all specific performance numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf35ecbe-0619-4d3a-9205-23c1da305f62",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT7fF3aSL9UHNsGWcKY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a982fc93-84e9-46ed-b1ad-e02bb0b68e89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmGCHjMEvMHePeFWSx79UG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1830,
      "cache_read_input_tokens": 14303,
      "output_tokens": 487,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1830
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 487,
          "cache_read_input_tokens": 14303,
          "cache_creation_input_tokens": 1830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1830,
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

_source line 29 · 2026-05-10T19:36:43.013Z_

<details><summary>↩ Tool result · `toolu_01Pf1YhYypuhHthQU1bFP4uh`</summary>

```text
# Joint vs. Single-Axis Pruning Comparison

Based on Table III in the document, here are the exact accuracy comparisons at 30% compression on LLaMA-2 7B:

**Joint Pruning (AMP with both components):** 61.02% average accuracy

**Single-Axis Pruning:**
- MLP component only: 56.93% average accuracy
- MHA (attention heads) component only: 37.63% average accuracy

The results demonstrate that "removing all components together, AMP ensures that no component is removed prematurely, allowing higher compression rates while maintaining predictive ability." The joint approach outperforms MLP-only pruning by approximately 4.09 percentage points and attention-only pruning by roughly 23.39 percentage points at the same compression ratio.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52539696-21a3-4432-a3ac-642f0ac30643",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "cf9af524-852b-4ca0-bc4d-915cd98d83ab",
  "sourceToolAssistantUUID": "52539696-21a3-4432-a3ac-642f0ac30643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T19:36:44.638Z_

<details><summary>↩ Tool result · `toolu_01LzLtEKbUT5nn5MjBrqyJys`</summary>

```text
# TriAttention Performance Metrics

Based on the webpage content, here are the specific performance numbers mentioned:

**MATH 500 Throughput:**
- TriAttention: 1,405 tokens/s at 68.4% accuracy
- Full Attention: 223 tokens/s at 69.6% accuracy
- **6.3× peak speedup achieved**

**AIME25 Performance (at matched 40.8% accuracy):**
- "TriAttention delivers 2.5× higher throughput than Full Attention"
- "10.7× KV cache memory reduction while matching Full Attention reasoning accuracy"

**Real-World Deployment:**
The page demonstrates running a 32B model on a 24GB GPU where "Full Attention hits out-of-memory before the agent can even start," while TriAttention "compresses KV cache on the fly, letting the agent run to completion."

**Note:** The search did not reveal any mentions of a vLLM plugin or throughput comparison tables beyond what is cited above.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a982fc93-84e9-46ed-b1ad-e02bb0b68e89",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "fffe74d9-3cb6-4685-81b0-bd5ad2dd282d",
  "sourceToolAssistantUUID": "a982fc93-84e9-46ed-b1ad-e02bb0b68e89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T19:36:47.745Z_

Now let me verify the Polar Sparsity 2.2x speedup claim by checking the paper itself, and also verify whether TriAttention has a vLLM plugin by checking the GitHub repo.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fffe74d9-3cb6-4685-81b0-bd5ad2dd282d",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT8rLKjt3Z4QmaS3Rrh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1656fadf-65f9-4339-97f1-d6904715026e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HL4GWUT9CGch7mKceQTJqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 16133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1208,
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

_source line 32 · 2026-05-10T19:36:50.179Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017LtxaiT6KjjmfQVsF1BYaW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.14884",
  "prompt": "Look for the specific speedup numbers claimed. Does it say 2.2x end-to-end speedup? What exact speedup numbers are reported? Also confirm it discusses MLP sparsity diminishing with batch size."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1656fadf-65f9-4339-97f1-d6904715026e",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT8rLKjt3Z4QmaS3Rrh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cef6eb70-ac21-4779-bec5-a0bbd636bddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HL4GWUT9CGch7mKceQTJqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 16133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1208,
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

_source line 33 · 2026-05-10T19:36:51.323Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y8bQzsBzjwLgoZSy3c2CP6`</summary>

```json
{
  "url": "https://github.com/WeianMao/triattention",
  "prompt": "Does this repository mention a vLLM plugin or vLLM integration? Look for any mentions of vLLM, plugin, or inference serving integration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cef6eb70-ac21-4779-bec5-a0bbd636bddd",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT8rLKjt3Z4QmaS3Rrh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b43dda10-a3fd-41d5-b8dd-52d325ba664a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HL4GWUT9CGch7mKceQTJqW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 16133,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1208
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 274,
          "cache_read_input_tokens": 16133,
          "cache_creation_input_tokens": 1208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1208,
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

_source line 34 · 2026-05-10T19:36:53.791Z_

<details><summary>↩ Tool result · `toolu_017LtxaiT6KjjmfQVsF1BYaW`</summary>

```text
# Polar Sparsity: Key Claims Analysis

## Speedup Numbers

The paper claims **up to 2.2× end-to-end speedups**, as stated in the abstract:

> "delivering up to 2.2× end-to-end speedups for models like OPT, LLaMA-2 & 3, Qwen, Mistral across various batch sizes"

This represents the maximum improvement observed across the tested model architectures.

## MLP Sparsity at Scale

The document confirms the diminishing returns of MLP sparsity under batching:

> "While MLP layers become more compute-efficient under batching, their sparsity vanishes."

The key insight is that as batch sizes increase, the union of active neurons in MLP layers approaches dense computation, making their sparsity benefits negligible. In contrast, attention layer head sparsity remains "stable and batch-invariant," which is why the authors shift focus to optimizing attention mechanisms through their Selective Head Attention approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cef6eb70-ac21-4779-bec5-a0bbd636bddd",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "7d3efdba-6a6e-4bc2-add2-14affe64b1ff",
  "sourceToolAssistantUUID": "cef6eb70-ac21-4779-bec5-a0bbd636bddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T19:36:55.905Z_

<details><summary>↩ Tool result · `toolu_01Y8bQzsBzjwLgoZSy3c2CP6`</summary>

```text
# TriAttention vLLM Integration

Yes, this repository extensively documents vLLM integration. The project includes:

**vLLM Plugin**: "TriAttention includes a vLLM plugin that enables transparent KV cache compression for production deployment. After installation, vLLM automatically discovers and activates the plugin."

**Key Features**:
- OpenAI-compatible API server mode
- Python API for direct integration
- Automatic activation upon installation
- Configuration via environment variables including `TRIATTN_RUNTIME_KV_BUDGET` and `TRIATTN_RUNTIME_SPARSE_STATS_PATH`

**Hardware Support**: Specific guidance is provided for DGX Spark/GB10 deployment, indicating the integration supports multiple hardware platforms.

**Additional Backend**: The documentation also mentions SGLang backend support was added separately, expanding beyond vLLM alone.

The entire "vLLM Integration" section details server configuration, Python API usage, and environment variable reference for controlling the compression behavior.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b43dda10-a3fd-41d5-b8dd-52d325ba664a",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "a05adfcf7f25b2d24",
  "type": "user",
  "uuid": "3be5e647-6459-4dcc-94dd-7d20a0fa1d34",
  "sourceToolAssistantUUID": "b43dda10-a3fd-41d5-b8dd-52d325ba664a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-10T19:37:42.002Z_

Excellent. Now I have all the information needed. Let me compile the verification report.

---

## Verification Report

### 1. TriAttention (April 2026)

**Paper confirmed**: [arXiv:2604.04921](https://arxiv.org/abs/2604.04921), "TriAttention: Efficient Long Reasoning with Trigonometric KV Compression," from MIT, NVIDIA, and Zhejiang University.

**Claim-by-claim verification:**

- **"10.7x memory reduction"** -- **VERIFIED.** The paper and project page both state 10.7x KV cache memory reduction while matching Full Attention reasoning accuracy on AIME25 with 32K-token generation.

- **"6.3x throughput on MATH-500 (1,405 vs 223 tokens/s)"** -- **VERIFIED.** Table 4 of the paper reports Full Attention at 222.8 tokens/s and TriAttention at 1,405.2 tokens/s on MATH-500, which is a 6.3x speedup. The project page confirms these same numbers. The accuracy trade-off is 68.4% (TriAttention) vs 69.6% (Full Attention) -- so there is a slight accuracy drop. Previous review rounds flagging this as unverifiable were incorrect; the numbers are in the paper.

- **"2.5x throughput at matched accuracy on AIME25"** -- **VERIFIED.** Both the abstract and project page confirm 2.5x higher throughput at matched accuracy (40.8%) on AIME25.

- **"vLLM plugin"** -- **VERIFIED.** The [GitHub repository](https://github.com/WeianMao/triattention) documents a vLLM plugin that enables transparent KV cache compression, with automatic discovery/activation upon installation and OpenAI-compatible API server mode. SGLang support is also available.

- **"pre-RoPE concentration"** -- **VERIFIED.** The paper's key observation is that Q and K vectors are highly concentrated around fixed non-zero centers in the pre-RoPE space, stable across positions. This concentration causes queries to attend preferentially to keys at specific distances via a trigonometric series.

**Verdict: All specific claims about TriAttention are accurate and verifiable.**

---

### 2. Polar Sparsity (NeurIPS 2025)

**Paper confirmed**: [arXiv:2505.14884](https://arxiv.org/abs/2505.14884), "Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity." NeurIPS 2025 poster confirmed at [NeurIPS virtual site](https://neurips.cc/virtual/2025/loc/san-diego/poster/117070) and [OpenReview](https://openreview.net/forum?id=cg2S1qqNSq).

**Claim-by-claim verification:**

- **"NeurIPS 2025"** -- **VERIFIED.** Confirmed via NeurIPS virtual poster page and OpenReview.

- **"Open-source Triton kernels at github.com/susavlsh10/Polar-Sparsity"** -- **VERIFIED.** The [repository](https://github.com/susavlsh10/Polar-Sparsity) exists and contains custom Triton kernels in `HybridTensor/triton/` implementing selective GEMM operations for sparse MLPs and sparse multi-head attention.

- **"2.2x end-to-end speedup"** -- **VERIFIED.** The abstract explicitly states "delivering up to 2.2x end-to-end speedups for models like OPT, LLaMA-2 & 3, Qwen, Mistral across various batch sizes."

- **"MLP sparsity diminishes with batch size"** -- **VERIFIED.** The paper states: "While MLP layers become more compute-efficient under batching, their sparsity vanishes." As batch sizes increase, the union of active neurons approaches dense computation. The paper pivots to attention head sparsity which remains "stable and batch-invariant."

- **"custom Triton kernels for selective head attention"** -- **VERIFIED.** The approach uses Selective Head Attention, ranking heads by output L2 norm and activating only top-k heads per layer.

**Verdict: All specific claims about Polar Sparsity are accurate and verifiable.**

---

### 3. AMP (IJCNN 2025)

**Paper confirmed**: [arXiv:2504.21174](https://arxiv.org/abs/2504.21174), "Efficient LLMs with AMP: Attention Heads and MLP Pruning." Confirmed as IJCNN 2025 publication.

**Claim-by-claim verification:**

- **"IJCNN 2025"** -- **VERIFIED.** The submission states: "To be published in International Joint Conference on Neural Networks (IJCNN), 2025."

- **"61.02% vs 37.63% attention-only or 56.93% MLP-only at 30% compression"** -- **VERIFIED.** Table III in the paper (LLaMA-2 7B at ~30% compression) shows:
  - AMP (joint head+MLP): **61.02%** average accuracy
  - MLP-only pruning: **56.93%** average accuracy
  - MHA (attention-only) pruning: **37.63%** average accuracy

  These numbers exactly match the proposal's claims. Joint pruning outperforms MLP-only by ~4.09 pp and attention-only by ~23.39 pp.

**Verdict: All specific claims about AMP are accurate and verifiable.**

---

### 4. R-KV

**Claim-by-claim verification:**

- **"Open-source code at github.com/Zefan-Cai/R-KV"** -- **VERIFIED.** The [repository](https://github.com/Zefan-Cai/R-KV) exists with 1.2k stars and 192 forks. It is tagged as "[NeurIPS 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models."

- **What it does**: R-KV compresses the KV cache during inference for reasoning LLMs by scoring tokens for both importance and redundancy, retaining only the most valuable ones. It is training-free and plug-and-play. The repo provides:
  - Core `rkv` Python package
  - Integrations for HuggingFace, vLLM, SGLang, and FlashInfer
  - Evaluation toolkits for MATH-500, AIME 2024
  - Visualization notebooks
  - Claims ~100% accuracy with only 10% cache, 90% memory savings, 6.6x throughput

**Verdict: The repo exists and is exactly what was claimed.**

---

### Summary

All four claims in the proposal are **verified as accurate**:

| Paper | Venue | Key Numbers | Status |
|-------|-------|-------------|--------|
| TriAttention | arXiv April 2026 | 10.7x mem, 6.3x throughput (1,405 vs 223 tok/s), 2.5x AIME25, vLLM plugin | All verified |
| Polar Sparsity | NeurIPS 2025 | 2.2x speedup, Triton kernels, MLP sparsity diminishes | All verified |
| AMP | IJCNN 2025 | 61.02% joint vs 37.63% attn-only vs 56.93% MLP-only @ 30% | All verified |
| R-KV | NeurIPS 2025 | GitHub repo exists, KV cache compression for reasoning | Verified |

The previous review round's flag that the 6.3x MATH-500 number "couldn't be verified" is incorrect -- the number appears explicitly in Table 4 of the TriAttention paper and on the project page.

Sources:
- [TriAttention arXiv](https://arxiv.org/abs/2604.04921)
- [TriAttention HTML paper](https://arxiv.org/html/2604.04921v1)
- [TriAttention project page](https://weianmao.github.io/tri-attention-project-page/)
- [TriAttention GitHub](https://github.com/WeianMao/triattention)
- [TriAttention MarkTechPost](https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/)
- [Polar Sparsity arXiv](https://arxiv.org/abs/2505.14884)
- [Polar Sparsity NeurIPS poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/117070)
- [Polar Sparsity OpenReview](https://openreview.net/forum?id=cg2S1qqNSq)
- [Polar Sparsity GitHub](https://github.com/susavlsh10/Polar-Sparsity)
- [AMP arXiv](https://arxiv.org/abs/2504.21174)
- [AMP HTML paper](https://arxiv.org/html/2504.21174v1)
- [R-KV GitHub](https://github.com/Zefan-Cai/R-KV)
- [R-KV project page](https://zefan-cai.github.io/R-KV.page/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3be5e647-6459-4dcc-94dd-7d20a0fa1d34",
  "isSidechain": true,
  "agentId": "a05adfcf7f25b2d24",
  "requestId": "req_011CauT9gKqnu7CkRGZxEaKY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8de6879-1d53-4724-9148-cd528f70437f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1kA4Vhz1ZARmU3MoF6ydu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 17341,
      "output_tokens": 2394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 789
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2394,
          "cache_read_input_tokens": 17341,
          "cache_creation_input_tokens": 789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 789,
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
