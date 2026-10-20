# Research conversation: Search for concrete throughput benchmarks for ModernBERT-large on H100 GPUs. I need to find: 1. The ModernBERT paper (ar

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ab57b4cc9d1dfc52e.jsonl`
- **Structured JSON:** [`95367ccdbccf219a1bc0.json`](../../sessions/95/95367ccdbccf219a1bc0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-09T20:43:30.335Z_

Search for concrete throughput benchmarks for ModernBERT-large on H100 GPUs. I need to find:

1. The ModernBERT paper (arXiv:2412.13663) - look for any throughput numbers on H100 specifically, or benchmark tables
2. Any Hugging Face blog posts or documentation about ModernBERT performance
3. Any community benchmarks comparing ModernBERT-large encoding speed on different GPUs

Search queries to try:
- "ModernBERT H100 throughput tokens per second"
- "ModernBERT-large inference speed benchmark GPU"
- "arXiv:2412.13663 ModernBERT benchmark"

I need to know: Is 100-150K tokens/sec on H100 a documented figure, or is it unverified? What hardware were the official benchmarks run on? What's the actual throughput range?

Use WebSearch and WebFetch to find actual numbers. Read the actual paper abstract/benchmark section if accessible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "c68a044d-efb5-4029-b672-f06f1b35f874",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-09T20:43:31.851Z_

I'll help you search for concrete throughput benchmarks for ModernBERT-large on H100 GPUs. Let me start with several search queries and then fetch the paper if available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c68a044d-efb5-4029-b672-f06f1b35f874",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseRDCAYv6khaViBuL1M",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0f34479a-7272-43e4-83e7-89d6f81a92b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CRXfvG4JaRUyVkFJFuc2M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14448,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-09T20:43:31.996Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F3ZYEwdXRmBJkKpkJVMjra`</summary>

```json
{
  "query": "ModernBERT H100 throughput tokens per second"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f34479a-7272-43e4-83e7-89d6f81a92b0",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseRDCAYv6khaViBuL1M",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9ac99da1-7714-4bd3-8b9b-679288a71b4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CRXfvG4JaRUyVkFJFuc2M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14448,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-09T20:43:32.230Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016rK5WwNzx9d18ABM3oN8BB`</summary>

```json
{
  "query": "ModernBERT-large inference speed benchmark GPU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ac99da1-7714-4bd3-8b9b-679288a71b4d",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseRDCAYv6khaViBuL1M",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd51604f-b5d9-4dd9-9ab0-411d78ae410c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CRXfvG4JaRUyVkFJFuc2M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14448,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-09T20:43:32.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D77xheFziCqWTFVe1skJKn`</summary>

```json
{
  "query": "arXiv:2412.13663 ModernBERT benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd51604f-b5d9-4dd9-9ab0-411d78ae410c",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseRDCAYv6khaViBuL1M",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c2dbb5c-52c5-400a-a0fa-e577a6b43d12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CRXfvG4JaRUyVkFJFuc2M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14448,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-09T20:43:32.409Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P8Y3nSt3oaqBvQpm8abdTU`</summary>

```json
{
  "query": "ModernBERT paper benchmarks throughput"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c2dbb5c-52c5-400a-a0fa-e577a6b43d12",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseRDCAYv6khaViBuL1M",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b46f4973-afd5-4503-a502-a41c29993b52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CRXfvG4JaRUyVkFJFuc2M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 0,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 245,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 14448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14448,
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

_source line 7 · 2026-05-09T20:43:37.801Z_

<details><summary>↩ Tool result · `toolu_01F3ZYEwdXRmBJkKpkJVMjra`</summary>

```text
Web search results for query: "ModernBERT H100 throughput tokens per second"

Links: [{"title":"BioClinical ModernBERT: A State-of-the-Art Long-Context Encoder for Biomedical and Clinical NLP","url":"https://arxiv.org/html/2506.10896v1"},{"title":"Nvidia H100 vLLM Benchmark Results: Reasoning LLMs on Hugging Face","url":"https://www.databasemart.com/blog/vllm-gpu-benchmark-h100"},{"title":"Finally, a Replacement for BERT: Introducing ModernBERT","url":"https://huggingface.co/blog/modernbert"},{"title":"H100 has 4.6x A100 Performance in TensorRT LLM, achieving 10,000 tok/s at 100ms to first token — TensorRT LLM","url":"https://nvidia.github.io/TensorRT-LLM/blogs/H100vsA100.html"},{"title":"Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT","url":"https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/"},{"title":"LLM Inference Performance Engineering: Best Practices | Databricks Blog","url":"https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices"},{"title":"Achieving High Mixtral 8x7B Performance with NVIDIA H100 Tensor Core GPUs and NVIDIA TensorRT-LLM | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/achieving-high-mixtral-8x7b-performance-with-nvidia-h100-tensor-core-gpus-and-tensorrt-llm/"},{"title":"Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference","url":"https://arxiv.org/html/2412.13663v2"},{"title":"Breaking MLPerf Training Records with NVIDIA H100 GPUs | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/breaking-mlperf-training-records-with-nvidia-h100-gpus/"},{"title":"Comparing NVIDIA H100 vs A100 GPUs for AI Workloads | OpenMetal IaaS","url":"https://openmetal.io/resources/blog/nvidia-h100-vs-a100-gpu-comparison/"}]

Based on the search results, I found information about ModernBERT throughput, though the H100-specific data requires some context:

ModernBERT delivers competitive throughput at 76.2 kTok/s (76,200 tokens per second), though it's important to note that this inference speed evaluation was conducted on a machine with a single A100 40GB GPU, not an H100.

The search results also show that ModernBERT maintains relatively stable processing speed across all input lengths: 76.2 kTok/s at 512 tokens, 73.8 kTok/s at 4096 tokens, and 71.1 kTok/s at 8192 tokens for fixed datasets.

While the search results don't contain specific H100 benchmarks for ModernBERT, they do indicate that H100 GPUs generally deliver significantly higher throughput than A100s for inference tasks. For context, H100 GPUs are capable of 250 to 300 tokens per second for similar models, depending on optimization strategies and batch size, which represents nearly double the performance of A100 GPUs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ac99da1-7714-4bd3-8b9b-679288a71b4d",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "ea18333b-ec50-4db8-8ece-6bca082e7595",
  "sourceToolAssistantUUID": "9ac99da1-7714-4bd3-8b9b-679288a71b4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-09T20:43:39.129Z_

<details><summary>↩ Tool result · `toolu_016rK5WwNzx9d18ABM3oN8BB`</summary>

```text
Web search results for query: "ModernBERT-large inference speed benchmark GPU"

Links: [{"title":"Finally, a Replacement for BERT: Introducing ModernBERT","url":"https://huggingface.co/blog/modernbert"},{"title":"Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference","url":"https://arxiv.org/html/2412.13663v2"},{"title":"[Literature Review] BioClinical ModernBERT: A State-of-the-Art Long-Context Encoder for Biomedical and Clinical NLP","url":"https://www.themoonlight.io/en/review/bioclinical-modernbert-a-state-of-the-art-long-context-encoder-for-biomedical-and-clinical-nlp"},{"title":"ModernBERT or DeBERTaV3? Examining Architecture and Data Influence on Transformer Encoder Models Performance","url":"https://arxiv.org/html/2504.08716v1"},{"title":"ModernBERT vs LLMs for Detecting Adverse Drug Reactions – Paul Simmering","url":"https://simmering.dev/blog/modernbert-vs-llm/"},{"title":"GitHub - XiongjieDai/GPU-Benchmarks-on-LLM-Inference: Multiple NVIDIA GPUs or Apple Silicon for Large Language Model Inference? · GitHub","url":"https://github.com/XiongjieDai/GPU-Benchmarks-on-LLM-Inference"},{"title":"ModernBERT - MattWeekend","url":"https://www.mattweekend.com/modern"},{"title":"BERT inference cost/performance analysis CPU vs GPU | by Vincent Teyssier | Medium","url":"https://vincentteyssier.medium.com/bert-inference-cost-performance-analysis-cpu-vs-gpu-b58a2420b2c8"},{"title":"Fine-tune classifier with ModernBERT in 2025","url":"https://www.philschmid.de/fine-tune-modern-bert-in-2025"},{"title":"Large Language Model Inference Acceleration: A Comprehensive Hardware Perspective","url":"https://arxiv.org/html/2410.04466v3"}]

Based on the search results, here's what I found about ModernBERT-large inference speed benchmarks on GPUs:

## Inference Speed Performance

Memory and inference efficiency results on an NVIDIA RTX 4090 are measured in thousands of tokens per second, averaged over 10 runs. Inference efficiency benchmarks are presented on an NVIDIA RTX 4090 for ModernBERT and other decoder models.

For variable length inputs, ModernBERT is much faster than all other models. More specifically, ModernBERT is twice as fast as DeBERTa – in fact, up to 4x faster in the more common situation where inputs are mixed length. Its long context inference is nearly 3 times faster than other high-quality models such as NomicBERT and GTE-en-MLM.

## Memory Efficiency

ModernBERT-large is slightly less memory efficient than the original BERT-large on short-context inputs, but can process batches at least 60 percent bigger than every other large model.

## Comparison with Other Models

ModernBERT-large is the second-best large encoder on GLUE, almost matching DeBERTaV3-large with one-tenth fewer parameters while processing tokens in half the time.

The model was specifically designed with efficiency in mind, incorporating optimization techniques like FlashAttention and hardware-aware design choices to maximize inference performance on consumer-grade GPUs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd51604f-b5d9-4dd9-9ab0-411d78ae410c",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "8e90ceaa-9526-413c-869d-ed65145114fa",
  "sourceToolAssistantUUID": "dd51604f-b5d9-4dd9-9ab0-411d78ae410c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-09T20:43:40.458Z_

<details><summary>↩ Tool result · `toolu_01D77xheFziCqWTFVe1skJKn`</summary>

```text
Web search results for query: "arXiv:2412.13663 ModernBERT benchmark"

Links: [{"title":"[2412.13663] Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference","url":"https://arxiv.org/abs/2412.13663"},{"title":"arXiv:2412.13663v2 [cs.CL] 19 Dec 2024","url":"https://arxiv.org/pdf/2412.13663"},{"title":"Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference","url":"https://arxiv.org/html/2412.13663v2"},{"title":"Paper page - Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference","url":"https://huggingface.co/papers/2412.13663"},{"title":"Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference - Summary","url":"https://portkey.ai/blog/smarter-better-faster-longer-a-modern-bidirectional-encoder-for-fast-memory-efficient-and-long-context-finetuning-and-inference-summary-2/"},{"title":"[2412.13663] Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference","url":"http://export.arxiv.org/abs/2412.13663"},{"title":"ModernBERT is More Efficient than Conventional BERT for ...","url":"https://arxiv.org/pdf/2503.05060"},{"title":"GitHub - AnswerDotAI/ModernBERT: Bringing BERT into modernity via both architecture changes and scaling · GitHub","url":"https://github.com/AnswerDotAI/ModernBERT"},{"title":"ModernBERT or DeBERTaV3? Examining Architecture and Data Influence on Transformer Encoder Models Performance","url":"https://arxiv.org/html/2504.08716v1"},{"title":"answerdotai/ModernBERT-base · Speed Benchmarks with MPS Backend","url":"https://huggingface.co/answerdotai/ModernBERT-base/discussions/47"}]

I found detailed information about arXiv:2412.13663. Here's a summary of the paper and its benchmarking results:

## Paper Overview

The paper is titled "Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference". ModernBERT brings modern model optimizations to encoder-only models and represents a major Pareto improvement over older encoders, trained on 2 trillion tokens with a native 8192 sequence length.

## Benchmark Performance

ModernBERT models exhibit state-of-the-art results on a large pool of evaluations encompassing diverse classification tasks and both single and multi-vector retrieval on different domains (including code). ModernBERT outperforms other leading models on benchmarks like GLUE, and on long-context retrieval tasks like MLDR, shows significant improvements.

## Efficiency Advantages

In addition to strong downstream performance, ModernBERT is also the most speed and memory efficient encoder and is designed for inference on common GPUs. ModernBERT processes sequences of 8192 tokens almost two times faster than previous models.

## Key Technical Innovations

Attention layers in ModernBERT alternate between global attention and local attention, with every third layer employing global attention and the remaining layers using a 128 token local sliding window attention. ModernBERT unpads inputs before the token embedding layer and optionally repads model outputs leading to a 10-to-20 percent performance improvement over other unpadding methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c2dbb5c-52c5-400a-a0fa-e577a6b43d12",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "736b0fd0-c8c6-4f74-89e3-900a72cf0ff7",
  "sourceToolAssistantUUID": "4c2dbb5c-52c5-400a-a0fa-e577a6b43d12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-09T20:43:47.481Z_

<details><summary>↩ Tool result · `toolu_01P8Y3nSt3oaqBvQpm8abdTU`</summary>

```text
Web search results for query: "ModernBERT paper benchmarks throughput"

Links: [{"title":"Finally, a Replacement for BERT: Introducing ModernBERT","url":"https://huggingface.co/blog/modernbert"},{"title":"[2412.13663] Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference","url":"https://arxiv.org/abs/2412.13663"},{"title":"Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference - Summary","url":"https://portkey.ai/blog/smarter-better-faster-longer-a-modern-bidirectional-encoder-for-fast-memory-efficient-and-long-context-finetuning-and-inference-summary-2/"},{"title":"A Quick Review of ModernBERT: Finally, a Replacement for BERT | by Shirley Li | Medium","url":"https://medium.com/@lixue421/a-quick-review-of-modernbert-finally-a-replacement-for-bert-120f9e44cf90"},{"title":"ModernBERT or DeBERTaV3? Examining Architecture and Data Influence on Transformer Encoder Models Performance","url":"https://arxiv.org/html/2504.08716v1"},{"title":"[2504.08716] ModernBERT or DeBERTaV3? Examining Architecture and Data Influence on Transformer Encoder Models Performance","url":"https://arxiv.org/abs/2504.08716"},{"title":"Paper Review: Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference – Andrey Lukyanenko","url":"https://andlukyane.com/blog/paper-review-modernbert"},{"title":"Papers Explained 277: ModernBERT. ModernBERT is a state-of-the-art… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-277-modernbert-59f25989f685"},{"title":"ModernBERT/benchmark.py at main · AnswerDotAI/ModernBERT","url":"https://github.com/AnswerDotAI/ModernBERT/blob/main/benchmark.py"},{"title":"Fine-tune classifier with ModernBERT in 2025","url":"https://www.philschmid.de/fine-tune-modern-bert-in-2025"}]

Based on the search results, here are the key throughput benchmarks from the ModernBERT paper:

## Speed Performance

ModernBERT is twice as fast as DeBERTa, and up to 4x faster in situations where inputs are mixed length. Its long context inference is nearly 3 times faster than other high-quality models such as NomicBERT and GTE-en-MLM.

## Inference Efficiency Metrics

The paper measures memory in terms of max batch size and inference speed in terms of thousands of tokens per second. Four synthetic datasets of documents are created with fixed and varying lengths (512, 8192 tokens) to measure and compare inference efficiency across various sequence lengths.

## Architecture Optimizations for Throughput

The paper introduces full unpadding, significantly enhancing processing efficiency and throughput. PyTorch's built-in compiling is leveraged to improve training efficiency by compiling all compatible modules, yielding a 10 percent improvement in throughput with negligible compilation overhead.

Additionally, ModernBERT is 2-4x faster than previous encoder models while achieving state-of-the-art performance across classification, retrieval and code understanding tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b46f4973-afd5-4503-a502-a41c29993b52",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "aa69d30c-a5c4-4701-bb04-29c0002f353c",
  "sourceToolAssistantUUID": "b46f4973-afd5-4503-a502-a41c29993b52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-09T20:43:51.851Z_

Excellent! I found references to the paper. Now let me fetch the actual paper and the Hugging Face blog post to get the specific benchmark numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa69d30c-a5c4-4701-bb04-29c0002f353c",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseSUQEXxjMF9xHEsBvq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a849943c-5f54-47b7-9720-d3b7ee652a75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ENMQ1jryyuCvGY6L97uNUk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4896,
      "cache_read_input_tokens": 14448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4896,
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

_source line 12 · 2026-05-09T20:43:53.062Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FgQFTD7cfouZY1J7KeJq8q`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.13663v2",
  "prompt": "What are the specific throughput numbers in tokens per second? What GPU was used for benchmarking? Is there an H100 benchmark? What are the exact throughput figures for ModernBERT-large?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a849943c-5f54-47b7-9720-d3b7ee652a75",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseSUQEXxjMF9xHEsBvq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "79619114-c032-4ee7-b0bf-eef5f6a38cda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ENMQ1jryyuCvGY6L97uNUk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4896,
      "cache_read_input_tokens": 14448,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4896
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 260,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 4896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4896,
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

_source line 13 · 2026-05-09T20:43:53.381Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018LqxVhcCRhkpKjJg58rSM2`</summary>

```json
{
  "url": "https://huggingface.co/blog/modernbert",
  "prompt": "What are the specific throughput benchmarks for ModernBERT-large on H100 or other GPUs? What are the tokens per second numbers mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79619114-c032-4ee7-b0bf-eef5f6a38cda",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseSUQEXxjMF9xHEsBvq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0cc38f3f-d21a-4f3a-96f4-7833fe284894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ENMQ1jryyuCvGY6L97uNUk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4896,
      "cache_read_input_tokens": 14448,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4896
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 260,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 4896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4896,
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

_source line 14 · 2026-05-09T20:43:57.201Z_

<details><summary>↩ Tool result · `toolu_01FgQFTD7cfouZY1J7KeJq8q`</summary>

```text
# ModernBERT Throughput Benchmarks

## GPU and Benchmarking Setup
The paper evaluated efficiency on an **NVIDIA RTX 4090**, which was one of ModernBERT's target GPUs. No H100 benchmarks are provided in the efficiency evaluation section.

## Throughput Numbers (Tokens per Second)

**ModernBERT-large on RTX 4090:**
- Fixed short-context (512 tokens): **52,300 tokens/sec**
- Fixed long-context (8192 tokens): **46,800 tokens/sec**
- Variable-length short (centered at 256): **52,900 tokens/sec**
- Variable-length long (centered at 4096): **49,800 tokens/sec**

**ModernBERT-base on RTX 4090:**
- Fixed short-context: **148,100 tokens/sec**
- Fixed long-context: **123,700 tokens/sec**
- Variable-length short: **147,300 tokens/sec**
- Variable-length long: **133,800 tokens/sec**

The paper notes that on long-context tasks, "ModernBERT is faster than all competing encoders, processing documents 2.65 and 3 times faster than the next-fastest encoder" for base and large variants respectively.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79619114-c032-4ee7-b0bf-eef5f6a38cda",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "32e45d5d-7b5d-41ea-907e-aaa045016e28",
  "sourceToolAssistantUUID": "79619114-c032-4ee7-b0bf-eef5f6a38cda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-09T20:43:59.872Z_

<details><summary>↩ Tool result · `toolu_018LqxVhcCRhkpKjJg58rSM2`</summary>

```text
# ModernBERT Throughput Benchmarks

The blog post does **not provide specific throughput numbers (tokens per second) for ModernBERT-large on H100 GPUs**. 

## What Benchmarks Are Provided

The efficiency results shown are for **NVIDIA RTX 4090** only, presented in a table with two scenarios:

1. **Fixed length inputs** (at maximum 8,192 token context)
2. **Variable length inputs** (more realistic real-world scenario)

## Key Performance Claims

The post makes these efficiency-related statements:

- ModernBERT is **2x faster than DeBERTa**
- Up to **4x faster in variable-length input scenarios**
- Nearly **3x faster than NomicBERT and GTE-en-MLM** on long context inference
- **2-3x faster** than the next fastest model for long context inputs

## Why RTX 4090 Was Chosen

The authors explicitly state their focus on practicality:

> "The first thing you might notice is that we're analysing the efficiency on an affordable consumer GPU, rather than the latest unobtainable hyped hardware. **First and foremost, ModernBERT is focused on practicality, not hype.**"

## For Specific H100 Numbers

The blog post does not include H100 benchmarks. For actual throughput metrics on enterprise GPUs, you would need to:
- Check the [arXiv paper](https://arxiv.org/abs/2412.13663)
- Test on your own infrastructure
- Check the [GitHub repository](https://github.com/huggingface/blog/blob/main/modernbert.md)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cc38f3f-d21a-4f3a-96f4-7833fe284894",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "bdc67403-fddf-4125-9ec1-621d15b37dbd",
  "sourceToolAssistantUUID": "0cc38f3f-d21a-4f3a-96f4-7833fe284894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-09T20:44:01.280Z_

Let me also check the GitHub repository and look for any community benchmarks with H100 data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdc67403-fddf-4125-9ec1-621d15b37dbd",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseTPQsw8xDXC3R3YqCo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86737b91-6f0c-4c88-86bc-55a19c5b470b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YTAzKNQJqjALn2cmHGf9eo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 19344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1020,
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

_source line 17 · 2026-05-09T20:44:01.509Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LjvuHWYmC3geqxnCAM1yUf`</summary>

```json
{
  "query": "ModernBERT A100 H100 benchmark comparison tokens per second"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86737b91-6f0c-4c88-86bc-55a19c5b470b",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseTPQsw8xDXC3R3YqCo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e940e899-ae92-4709-aab6-e638ec6a0b9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YTAzKNQJqjALn2cmHGf9eo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 19344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1020,
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

_source line 18 · 2026-05-09T20:44:01.721Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RCbugFAdmqzBr1ufMsK4bc`</summary>

```json
{
  "query": "\"ModernBERT\" \"100k tokens\" OR \"150k tokens\" H100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e940e899-ae92-4709-aab6-e638ec6a0b9a",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseTPQsw8xDXC3R3YqCo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5a45c87e-395e-4d66-97b7-9addb0ea0466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YTAzKNQJqjALn2cmHGf9eo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 19344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1020,
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

_source line 19 · 2026-05-09T20:44:02.140Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VAJWedZe9RjVBnUoECDdMk`</summary>

```json
{
  "url": "https://github.com/AnswerDotAI/ModernBERT",
  "prompt": "Are there any benchmark results with H100 GPUs? What throughput benchmarks are documented?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a45c87e-395e-4d66-97b7-9addb0ea0466",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseTPQsw8xDXC3R3YqCo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a8552419-3892-43ab-97e3-6e9e26c7d081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YTAzKNQJqjALn2cmHGf9eo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 19344,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 232,
          "cache_read_input_tokens": 19344,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1020,
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

_source line 20 · 2026-05-09T20:44:05.928Z_

<details><summary>↩ Tool result · `toolu_01VAJWedZe9RjVBnUoECDdMk`</summary>

```text
Based on the provided content, there is no information about H100 GPU benchmark results or throughput benchmarks documented in this GitHub repository page.

The only reference to H100s appears in the setup instructions: "if using H100s clone and build flash attention 3" - this merely indicates that H100 support exists but doesn't provide any performance metrics.

The repository does mention a `benchmark.py` file exists, which suggests benchmarking capabilities are available, but no actual benchmark results or throughput documentation is included in the content shown here. For specific performance metrics, you would need to consult the arXiv preprint or the referenced blog post on HuggingFace.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8552419-3892-43ab-97e3-6e9e26c7d081",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "79086de6-fcfa-4424-a648-8601111c845c",
  "sourceToolAssistantUUID": "a8552419-3892-43ab-97e3-6e9e26c7d081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-09T20:44:06.964Z_

<details><summary>↩ Tool result · `toolu_01RCbugFAdmqzBr1ufMsK4bc`</summary>

```text
Web search results for query: ""ModernBERT" "100k tokens" OR "150k tokens" H100"

Links: [{"title":"BioClinical ModernBERT: A State-of-the-Art Long-Context Encoder for Biomedical and Clinical NLP","url":"https://arxiv.org/html/2506.10896v1"},{"title":"Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference","url":"https://arxiv.org/html/2412.13663v2"},{"title":"Finally, a Replacement for BERT: Introducing ModernBERT","url":"https://huggingface.co/blog/modernbert"},{"title":"pre-training speed, data loader and gpu utilization · Issue #236 · AnswerDotAI/ModernBERT","url":"https://github.com/AnswerDotAI/ModernBERT/issues/236"},{"title":"lucataco/modernbert-large | Run with an API on Replicate","url":"https://replicate.com/lucataco/modernbert-large"},{"title":"H100 has 4.6x A100 Performance in TensorRT LLM, achieving 10,000 tok/s at 100ms to first token — TensorRT LLM","url":"https://nvidia.github.io/TensorRT-LLM/blogs/H100vsA100.html"},{"title":"Nvidia H100 vLLM Benchmark Results: Reasoning LLMs on Hugging Face","url":"https://www.databasemart.com/blog/vllm-gpu-benchmark-h100"},{"title":"Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT","url":"https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/"},{"title":"Finetuning time for 1 billion tokens on H100 - cuDNN - NVIDIA Developer Forums","url":"https://forums.developer.nvidia.com/t/finetuning-time-for-1-billion-tokens-on-h100/296075"},{"title":"Optimizing vLLM Performance on A100 80GB: GPU Benchmark Insights","url":"https://www.databasemart.com/blog/vllm-gpu-benchmark-a100-80gb"}]

Based on the search results, here's what I found regarding ModernBERT with 100k/150k tokens and H100:

## ModernBERT Context Length

ModernBERT was trained on 2 trillion tokens with a native 8192 sequence length. The search results do not contain specific information about ModernBERT supporting 100k or 150k token context lengths. 

ModernBERT enables the processing of entire clinical notes and documents in a single pass with a context window of up to 8,192 tokens, extendable via rotary positional embeddings (RoPE), but the results don't mention extensions to 100k or 150k tokens.

## H100 Training

Regarding H100 GPUs, ModernBERT was trained on 8x H100 GPUs. However, the search results discuss ModernBERT's native 8k token context, not 100k or 150k token variants.

If you're looking for information about ModernBERT variants with extended context lengths of 100k-150k tokens, that information was not found in these search results. You may want to check the official ModernBERT repository or more recent papers for updates on context extension capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a45c87e-395e-4d66-97b7-9addb0ea0466",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "9fcc49b7-c50c-4065-a826-faf5deddb989",
  "sourceToolAssistantUUID": "5a45c87e-395e-4d66-97b7-9addb0ea0466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-09T20:44:08.438Z_

<details><summary>↩ Tool result · `toolu_01LjvuHWYmC3geqxnCAM1yUf`</summary>

```text
Web search results for query: "ModernBERT A100 H100 benchmark comparison tokens per second"

Links: [{"title":"NVIDIA GPU benchmark: H100 vs A100 vs L40S","url":"https://www.cudocompute.com/blog/real-world-gpu-benchmarks"},{"title":"A100 vs H100 for LLM Inference: Performance Guide | Lyceum Technology","url":"https://lyceum.technology/magazine/a100-vs-h100-for-llm-inference/"},{"title":"NVIDIA A100 vs H100 vs H200: GPU Comparison for AI | E2E Networks","url":"https://www.e2enetworks.com/blog/nvidia-a100-vs-h100-vs-h200-gpu-comparison"},{"title":"NVIDIA A100 vs H100: Specs, Benchmarks, and Cloud Pricing Guide (2026) | Spheron Blog","url":"https://www.spheron.network/blog/nvidia-a100-vs-h100/"},{"title":"NVIDIA A100 vs. H100: Choosing the Right GPU for Your AI Workloads","url":"https://www.clarifai.com/blog/nvidia-a100-vs.-h100-choosing-the-right-gpu-for-your-ai-workloads"},{"title":"Benchmark H100 vs A100 Deep Learning Speed Guide | Ventus Servers","url":"https://ventusserver.com/a100-deep-learning-speed/"},{"title":"H100 vs A100 Cloud Performance Benchmarks Guide | Ventus Servers","url":"https://ventusserver.com/a100-cloud-performance-benchmarks/"},{"title":"Comparing NVIDIA H100 vs A100 GPUs for AI Workloads | OpenMetal IaaS","url":"https://openmetal.io/resources/blog/nvidia-h100-vs-a100-gpu-comparison/"},{"title":"H100 vs A100: GPU Benchmarks, Specs & Cloud Pricing Compared (2026) | Jarvis Labs Blog | Jarvis Labs","url":"https://jarvislabs.ai/blog/h100-vs-a100"},{"title":"Optimizing vLLM Performance on A100 80GB: GPU Benchmark Insights","url":"https://www.databasemart.com/blog/vllm-gpu-benchmark-a100-80gb"}]

Based on the search results, here's what I found about ModernBERT A100 and H100 benchmark comparisons in terms of tokens per second:

## Key Benchmark Results

Industry testing on Llama-70B shows H100 achieving 250-300 tokens/second with TensorRT-LLM optimization, compared to A100's ~130 tokens/second.

For BERT-specific workloads, one H100 streams 24,000 tokens/second on BERT, scaling to 250-300 on Llama-70B versus A100's 130.

## Performance Ratios

The roughly 2× gap observed in BERT inference tests aligns with industry testing on larger models. More specifically, the H100 W4A8 advantage at high concurrency is significant: 2.6x the output tokens/sec of A100 INT4 at batch 16 for 70B models.

## Overall Context

A controlled, apples-to-apples benchmark on CUDO Compute compared three NVIDIA GPUs—H100 SXM, A100, and L40S—under identical software stacks and single-GPU VM configurations, using an end-to-end BERT-base masked-LM fine-tune as the workload.

The results consistently show that H100 delivers approximately 2-3x better throughput than A100 for transformer-based models like BERT and Llama across different optimization strategies and batch sizes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e940e899-ae92-4709-aab6-e638ec6a0b9a",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "34ea2aec-1042-429f-8b1d-aa462f651cd8",
  "sourceToolAssistantUUID": "e940e899-ae92-4709-aab6-e638ec6a0b9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-09T20:44:09.598Z_

Let me check if there are any community discussions or Hugging Face model card benchmarks for ModernBERT.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34ea2aec-1042-429f-8b1d-aa462f651cd8",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseU27k1FKkuuZCNpGQB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fc2719a3-9873-4de3-93b7-e1896d514efc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4pbWmeNBu1K8oM3x6gATG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1097,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 20364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1193,
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

_source line 24 · 2026-05-09T20:44:09.823Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018LFERJA8YaJkbhLqBhNtMD`</summary>

```json
{
  "query": "site:huggingface.co ModernBERT-large benchmark throughput"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc2719a3-9873-4de3-93b7-e1896d514efc",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseU27k1FKkuuZCNpGQB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "29ef5b61-bfcd-442b-a57d-a736d463509f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4pbWmeNBu1K8oM3x6gATG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1097,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 20364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1193,
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

_source line 25 · 2026-05-09T20:44:09.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Po4cSkNfkoCjbL4QF14LAH`</summary>

```json
{
  "query": "ModernBERT H100 community benchmark reddit github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29ef5b61-bfcd-442b-a57d-a736d463509f",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseU27k1FKkuuZCNpGQB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f3411cd4-dd17-4c8b-a8e7-a7af453a1f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4pbWmeNBu1K8oM3x6gATG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1097,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 20364,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1193
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1097,
          "output_tokens": 141,
          "cache_read_input_tokens": 20364,
          "cache_creation_input_tokens": 1193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1193,
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

_source line 26 · 2026-05-09T20:44:14.519Z_

<details><summary>↩ Tool result · `toolu_018LFERJA8YaJkbhLqBhNtMD`</summary>

```text
Web search results for query: "site:huggingface.co ModernBERT-large benchmark throughput"

Links: [{"title":"Fine-tune classifier with ModernBERT in 2025","url":"https://www.philschmid.de/fine-tune-modern-bert-in-2025"},{"title":"Finally, a Replacement for BERT: Introducing ModernBERT","url":"https://huggingface.co/blog/modernbert"},{"title":"answerdotai/ModernBERT-large · Hugging Face","url":"https://huggingface.co/answerdotai/ModernBERT-large"},{"title":"mmBERT: ModernBERT goes Multilingual","url":"https://huggingface.co/blog/mmbert"},{"title":"transformers/docs/source/en/model_doc/modernbert.md at main · huggingface/transformers","url":"https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/modernbert.md"},{"title":"answerdotai/ModernBERT-Large-Instruct · Hugging Face","url":"https://huggingface.co/answerdotai/ModernBERT-Large-Instruct"},{"title":"ModernBERT · Hugging Face","url":"https://huggingface.co/docs/transformers/v4.49.0/model_doc/modernbert"},{"title":"answerdotai/ModernBERT-base · Hugging Face","url":"https://huggingface.co/answerdotai/ModernBERT-base"},{"title":"blog/modernbert.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/modernbert.md"},{"title":"GitHub - AnswerDotAI/ModernBERT: Bringing BERT into modernity via both architecture changes and scaling · GitHub","url":"https://github.com/answerdotai/modernbert"}]

Based on the search results, here's what I found about ModernBERT-large benchmark throughput:

ModernBERT is twice as fast as DeBERTa – in fact, up to 4x faster in the more common situation where inputs are mixed length. Additionally, its long context inference is nearly 3 times faster than other high-quality models such as NomicBERT and GTE-en-MLM.

ModernBERT achieves state-of-the-art performance across classification, retrieval and code understanding tasks while being 2-4x faster than previous encoder models.

The search results indicate that ModernBERT-large offers significant throughput improvements, particularly for variable-length inputs and long context processing, but specific detailed throughput benchmark numbers (like tokens/second) are not provided in the search results from the Hugging Face documentation and blog posts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29ef5b61-bfcd-442b-a57d-a736d463509f",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "39e463d7-25e4-44e9-b6bf-1965ef7f2c1b",
  "sourceToolAssistantUUID": "29ef5b61-bfcd-442b-a57d-a736d463509f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-09T20:44:17.995Z_

<details><summary>↩ Tool result · `toolu_01Po4cSkNfkoCjbL4QF14LAH`</summary>

```text
Web search results for query: "ModernBERT H100 community benchmark reddit github"

Links: [{"title":"blog/modernbert.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/modernbert.md"},{"title":"ModernBERT/benchmark.py at main · AnswerDotAI/ModernBERT","url":"https://github.com/AnswerDotAI/ModernBERT/blob/main/benchmark.py"},{"title":"GitHub - AnswerDotAI/ModernBERT: Bringing BERT into modernity via both architecture changes and scaling · GitHub","url":"https://github.com/answerdotai/modernbert"},{"title":"Finally, a Replacement for BERT: Introducing ModernBERT","url":"https://huggingface.co/blog/modernbert"},{"title":"GitHub - Meeex2/ModernBert_Benchmark: Exploring the code capabilities of ModernBert in comparision with the former BERT model.","url":"https://github.com/Meeex2/ModernBert_Benchmark"},{"title":"GitHub - lindvalllab/BioClinical-ModernBERT · GitHub","url":"https://github.com/lindvalllab/BioClinical-ModernBERT"},{"title":"Encoder-only ModernBERT Model | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/encoder-only-modernbert-model/4361559"},{"title":"answerdotai/ModernBERT-base · Hugging Face","url":"https://huggingface.co/answerdotai/ModernBERT-base"},{"title":"Hashcat v6.2.6 benchmark on the Nvidia H100 PCIe · GitHub","url":"https://gist.github.com/Chick3nman/e1417339accfbb0b040bcd0a0a9c6d54"},{"title":"Nvidia H100 vLLM Benchmark Results: Reasoning LLMs on Hugging Face","url":"https://www.databasemart.com/blog/vllm-gpu-benchmark-h100"}]

Based on the search results, here's what I found about ModernBERT, H100 benchmarks, and community resources:

## ModernBERT Overview

ModernBERT is a modernized bidirectional encoder-only Transformer model pre-trained on 2 trillion tokens of English and code data with a native context length of up to 8,192 tokens. ModernBERT is a new Encoder Model developed by Answer.AI and LightOn.

## H100 Resources

The FineWeb-Edu filtering effort took 6,000 H100 hours. Additionally, the environment documentation includes instructions for H100 GPU setup with Flash Attention 3.

## Community Benchmarks & GitHub Resources

The main GitHub repositories include:

1. **Official ModernBERT Repository**: The AnswerDotAI/ModernBERT repository contains the experiments to bring BERT into modernity via both architecture changes and scaling.

2. **Community Benchmark Projects**: The Meeex2/ModernBert_Benchmark project explores the capabilities of ModernBERT and the former bert model by analyzing their tokenization processes and evaluating their performance on various text inputs.

3. **BioClinical ModernBERT**: The multiprocess_bench.py script is used to measure inference speed of each model, and is a modified version of ModernBERT's inference speed script.

## Performance Benchmarks

For variable length inputs, ModernBERT is much faster than all other models, and for long context inputs, ModernBERT is 2-3x faster than the next fastest model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3411cd4-dd17-4c8b-a8e7-a7af453a1f20",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "590bb6eb-96b0-4950-bfc3-eb11d4b6a397",
  "sourceToolAssistantUUID": "f3411cd4-dd17-4c8b-a8e7-a7af453a1f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-09T20:44:19.331Z_

Perfect! I found a benchmark.py file. Let me fetch that to see what benchmarks are actually documented.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "590bb6eb-96b0-4950-bfc3-eb11d4b6a397",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseUisC1eQPwz9Z1p2sx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "093315f9-a498-4c24-8c2c-d2f31631b8cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XNndKfQJMpUbjmaLxqgC1v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2928,
      "cache_read_input_tokens": 21557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2928,
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

_source line 29 · 2026-05-09T20:44:19.989Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CXa19iAyrEZxvFksYELuqw`</summary>

```json
{
  "url": "https://github.com/AnswerDotAI/ModernBERT/blob/main/benchmark.py",
  "prompt": "What benchmarking methodology is used? What GPU targets are there? What throughput metrics does this benchmark measure?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "093315f9-a498-4c24-8c2c-d2f31631b8cf",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseUisC1eQPwz9Z1p2sx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fcc2bc1f-d87c-4952-a178-c8d74144cd07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XNndKfQJMpUbjmaLxqgC1v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2928,
      "cache_read_input_tokens": 21557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2928,
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

_source line 30 · 2026-05-09T20:44:20.360Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DMKA5uX7XuBveJ13taXJtg`</summary>

```json
{
  "url": "https://github.com/huggingface/blog/blob/main/modernbert.md",
  "prompt": "What are the specific throughput numbers in tokens per second? Is there an H100 benchmark? What GPU was used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc2bc1f-d87c-4952-a178-c8d74144cd07",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseUisC1eQPwz9Z1p2sx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5bd40942-29e1-4938-b711-221e5b47103f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XNndKfQJMpUbjmaLxqgC1v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2928,
      "cache_read_input_tokens": 21557,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2928
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 239,
          "cache_read_input_tokens": 21557,
          "cache_creation_input_tokens": 2928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2928,
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

_source line 31 · 2026-05-09T20:44:24.381Z_

<details><summary>↩ Tool result · `toolu_01CXa19iAyrEZxvFksYELuqw`</summary>

```text
# Benchmarking Methodology Analysis

## Methodology
The benchmark uses a training and inference testing approach with warmup phases. It executes "warmup batches" before measurement to stabilize performance, then measures actual runs while tracking power consumption at intervals.

## GPU Targets
The code supports flexible GPU selection via the `gpu_idx` parameter (defaults to 0). No specific GPU model is hardcoded; the benchmark adapts to "cuda if torch.cuda.is_available() else cpu."

## Throughput Metrics
The benchmark measures:

- **Tokens per second**: Calculated as "(num_samples × seq_length) / run_time"
- **Normalized throughput**: "tokens_per_second_per_million_params" normalizes results across model sizes
- Both training and inference throughput are tracked separately

Additional metrics include power consumption (average/max watts), memory usage (GiB), and final loss values during training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcc2bc1f-d87c-4952-a178-c8d74144cd07",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "d79edf4a-9b4d-4c1b-82ad-1bc61cf7648a",
  "sourceToolAssistantUUID": "fcc2bc1f-d87c-4952-a178-c8d74144cd07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-09T20:44:25.017Z_

<details><summary>↩ Tool result · `toolu_01DMKA5uX7XuBveJ13taXJtg`</summary>

```text
# ModernBERT Throughput Benchmarks

Based on the provided content, the specific throughput metrics mentioned are:

**Tokens per second:** The blog states that ModernBERT achieves inference "in thousands of tokens per second" but does not provide exact numerical values for throughput rates.

**GPU used:** The efficiency benchmarks were conducted on an "NVIDIA RTX 4090" - notably a consumer-grade GPU rather than enterprise hardware.

**H100 benchmark:** There is no H100 benchmark included in this documentation. The authors explicitly emphasize practicality over hype: "First and foremost, ModernBERT is focused on practicality, not hype." They deliberately chose to test on "an affordable consumer GPU, rather than the latest unobtainable hyped hardware."

The blog does provide comparative speed claims (such as being "twice as fast as DeBERTa" and "4x faster" for mixed-length inputs), but actual throughput numbers in tokens/second are not quantified in the source material.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bd40942-29e1-4938-b711-221e5b47103f",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "05ac88a8-3e03-4a5e-9ab8-362edf43a7d7",
  "sourceToolAssistantUUID": "5bd40942-29e1-4938-b711-221e5b47103f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-09T20:44:26.293Z_

Now let me check the actual Hugging Face model card for ModernBERT-large to see if there are any additional benchmarks documented there.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05ac88a8-3e03-4a5e-9ab8-362edf43a7d7",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseVEtU8aGemz4rfKCCx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "39660f0f-441a-43d9-b566-d2e378c401c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JKMpnM5pyiqqfYEicpXj4j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 738,
      "cache_read_input_tokens": 24485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 738,
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

_source line 34 · 2026-05-09T20:44:26.647Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QvQYGZHwJG6xYh7QRFs7NS`</summary>

```json
{
  "url": "https://huggingface.co/answerdotai/ModernBERT-large",
  "prompt": "Are there any benchmark results or throughput metrics documented? What hardware specifications are mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39660f0f-441a-43d9-b566-d2e378c401c9",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseVEtU8aGemz4rfKCCx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e2b1c5e3-8c68-4705-8fa9-ad0af270061e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JKMpnM5pyiqqfYEicpXj4j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 738,
      "cache_read_input_tokens": 24485,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 738
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 139,
          "cache_read_input_tokens": 24485,
          "cache_creation_input_tokens": 738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 738,
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

_source line 35 · 2026-05-09T20:44:32.764Z_

<details><summary>↩ Tool result · `toolu_01QvQYGZHwJG6xYh7QRFs7NS`</summary>

````text
# Benchmark Results and Hardware Specifications

## Benchmark Results

Yes, ModernBERT includes comprehensive evaluation across multiple tasks:

### Key Performance Highlights:
- **GLUE (NLU)**: ModernBERT-base achieves **88.4**, surpassing similarly-sized encoder models. ModernBERT-large reaches **90.4**, second only to DeBERTa-v3-large (**91.4**)
- **Code Retrieval**: State-of-the-art results on CodeSearchNet (**56.4** base, **59.5** large) and StackQA (**73.6** base, **83.9** large)
- **Long-context Retrieval (MLDR)**: ModernBERT-large achieves **80.4** on MLDR_OOD, significantly outperforming competitors
- **General Retrieval (BEIR)**: Strong performance in both DPR-style (**44.0** large) and ColBERT-style (**52.4** large) settings

### Evaluation Categories:
- Natural language understanding (GLUE)
- General retrieval (BEIR)
- Long-context retrieval (MLDR)
- Code retrieval (CodeSearchNet and StackQA)

## Hardware Specifications

**Training Infrastructure:**
- **GPU**: 8x H100 GPUs
- **Data**: 2 trillion tokens of English text and code
- **Sequence Length**: Pre-trained up to 1,024 tokens, then extended to 8,192 tokens

## Performance Optimization

**For inference efficiency**, the documentation recommends:
> "⚠️ If your GPU supports it, we recommend using ModernBERT with Flash Attention 2 to reach the highest efficiency."

Installation:
```bash
pip install flash-attn
```

**Note**: No specific throughput metrics (tokens/second, latency) are documented on this page.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2b1c5e3-8c68-4705-8fa9-ad0af270061e",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "0d0320bb-e747-4340-a987-d52e3168d739",
  "sourceToolAssistantUUID": "e2b1c5e3-8c68-4705-8fa9-ad0af270061e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-09T20:44:33.974Z_

Excellent. Let me do one more search to see if there are any external community benchmarks or technical blogs that have run ModernBERT on H100.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d0320bb-e747-4340-a987-d52e3168d739",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseVp51CtEwPnZAb7PDv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce94b8bb-782d-4ad5-8dad-bda8944f5e02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CoedX23PYSAnKo6g42KLTK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 25223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 607,
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

_source line 37 · 2026-05-09T20:44:34.609Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kk79xXgC1PjGUM547y9Li8`</summary>

```json
{
  "query": "\"ModernBERT\" inference benchmark GPU performance comparison 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce94b8bb-782d-4ad5-8dad-bda8944f5e02",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseVp51CtEwPnZAb7PDv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9f267da7-2f24-452e-8558-9678c74f3dfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CoedX23PYSAnKo6g42KLTK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 25223,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 157,
          "cache_read_input_tokens": 25223,
          "cache_creation_input_tokens": 607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 607,
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

_source line 38 · 2026-05-09T20:44:34.615Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EC1dg7hgkvCo2sGYBF5NqW`</summary>

```json
{
  "query": "ModernBERT latency throughput RTX 4090 A100 benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f267da7-2f24-452e-8558-9678c74f3dfa",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseVp51CtEwPnZAb7PDv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e9614cfe-ab6c-46cf-85ee-2e2162a7376d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CoedX23PYSAnKo6g42KLTK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 25223,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 157,
          "cache_read_input_tokens": 25223,
          "cache_creation_input_tokens": 607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 607,
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

_source line 39 · 2026-05-09T20:44:40.531Z_

<details><summary>↩ Tool result · `toolu_01EC1dg7hgkvCo2sGYBF5NqW`</summary>

```text
Web search results for query: "ModernBERT latency throughput RTX 4090 A100 benchmark"

Links: [{"title":"RTX 4090 & 5090 vs A100: Consumer GPUs Outperform Datacenter Cards | Hivenet","url":"https://www.hivenet.com/post/rtx-4090-and-5090s---up-to-2-3x-faster-than-an-a100"},{"title":"Why A100/H100 Beat RTX 4090 for Large-Model Training","url":"https://www.allpcb.com/allelectrohub/why-a100h100-beat-rtx-4090-for-large-model-training"},{"title":"GPU Benchmarks of H100/H200/A100/RTX 4090 and WhaleFlux Resource Management Solution","url":"https://www.whaleflux.com/blog/gpu-benchmarks-of-h100-h200-a100-rtx-4090-and-whaleflux-resource-management-solution/"},{"title":"Nvidia RTX 4090 - GPU benchmark - UserBenchmark","url":"https://gpu.userbenchmark.com/Nvidia-RTX-4090/Rating/4136"},{"title":"RTX4090 vLLM Benchmark: Best GPU for LLMs Below 8B on Hugging Face","url":"https://www.databasemart.com/blog/vllm-gpu-benchmark-rtx4090"},{"title":"NVIDIA A100 40 GB (PCIe) vs. NVIDIA RTX 4090| GPU Benchmarks for AI/ML, local LLM, deep learning in %current_year% | BIZON","url":"https://bizon-tech.com/gpu-benchmarks/NVIDIA-A100-40-GB-(PCIe)-vs-NVIDIA-RTX-4090/592vs637"},{"title":"Unveiling the Titans: Nvidia GeForce RTX 4090 vs. Nvidia A100 for Ultimate Performance - fibermall.com","url":"https://www.fibermall.com/blog/nvidia-a100-vs-4090.htm"},{"title":"NVIDIA A100 80 GB (PCIe) vs. NVIDIA RTX 4090| GPU Benchmarks for AI/ML, local LLM, deep learning in %current_year% | BIZON","url":"https://bizon-tech.com/gpu-benchmarks/NVIDIA-A100-80-GB-(PCIe)-vs-NVIDIA-RTX-4090/624vs637"},{"title":"NVIDIA RTX 4090 vs. A100: Two Powerhouses, Two Purposes","url":"https://vast.ai/article/nvidia-rtx-4090-vs-a100-two-powerhouses-two-purposes"},{"title":"RTX 4090 vs A100 PCIe | Runpod GPU Benchmarks","url":"https://www.runpod.io/gpu-compare/rtx-4090-vs-a100-pcie"}]

I've performed a web search for benchmark information on ModernBERT latency and throughput across RTX 4090 and A100 GPUs. However, the search results I found don't contain specific benchmark data for ModernBERT. Instead, the results focus on general comparisons of RTX 4090 and A100 performance for LLMs and other AI workloads.

The search did return some relevant general information:

**RTX 4090 vs A100 Performance Overview:**
- Under moderate load (1 req/s), the RTX 4090 offers latencies close to the A100 performances
- RTX 4090 trailed the A100 on both latency and throughput for 8B LLaMA 3.1 Instruct model, though it's strong for its class
- The A100 delivers around 2 TB/s of bandwidth – double the RTX 4090

**VRAM Considerations:**
- The RTX 4090's 24GB VRAM is suitable for small-to-medium models
- The A100's 80GB version is suitable for models with tens of billions of parameters

Unfortunately, I couldn't find specific ModernBERT benchmark results in these search results. You may need to check the official ModernBERT repository, documentation, or relevant AI benchmarking sites like HELM, MLPerf, or the authors' publications for specific latency and throughput metrics on these GPUs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9614cfe-ab6c-46cf-85ee-2e2162a7376d",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "cd18e809-d432-40ee-af99-b9c0ce463e03",
  "sourceToolAssistantUUID": "e9614cfe-ab6c-46cf-85ee-2e2162a7376d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-09T20:44:41.591Z_

<details><summary>↩ Tool result · `toolu_01Kk79xXgC1PjGUM547y9Li8`</summary>

```text
Web search results for query: ""ModernBERT" inference benchmark GPU performance comparison 2024 2025"

Links: [{"title":"NVIDIA: MLPerf AI Benchmarks","url":"https://www.nvidia.com/en-us/data-center/resources/mlperf-benchmarks/"},{"title":"AMD Delivers Breakthrough MLPerf Inference 6.0 Results","url":"https://www.amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-inference-6-0-results.html"},{"title":"The Best GPUs for Local LLM Inference in 2025 | LocalLLM.in","url":"https://localllm.in/blog/best-gpus-llm-inference-2025"},{"title":"Open Source AI Inference Benchmark | InferenceX by SemiAnalysis","url":"https://inferencex.semianalysis.com/"},{"title":"GPU Cluster Benchmarking | Introl Blog","url":"https://introl.com/blog/gpu-cluster-benchmarking-mlperf-testing-performance-validation"},{"title":"MLPerf Inference v5.1 Results Land With New Benchmarks and Record Participation - HPCwire","url":"https://www.hpcwire.com/2025/09/10/mlperf-inference-v5-1-results-land-with-new-benchmarks-and-record-participation/"},{"title":"GPU LLM Performance Benchmarks | Koyeb","url":"https://www.koyeb.com/docs/hardware/gpu-benchmarks"},{"title":"GitHub - XiongjieDai/GPU-Benchmarks-on-LLM-Inference: Multiple NVIDIA GPUs or Apple Silicon for Large Language Model Inference? · GitHub","url":"https://github.com/XiongjieDai/GPU-Benchmarks-on-LLM-Inference"},{"title":"LLM Performance and AI Hardware: 2023–2025 Breakthroughs | by Oleksandr Kucherenko | Medium","url":"https://medium.com/@olku/llm-performance-and-ai-hardware-2023-2025-breakthroughs-fa3a1f8dc505"},{"title":"Choosing the right GPU | LLM Inference Handbook","url":"https://bentoml.com/llm/getting-started/choosing-the-right-gpu"}]

Based on the web search results, here's what I found regarding GPU inference performance benchmarks for 2024-2025:

## General GPU Inference Performance Trends

NVIDIA's Blackwell architecture now delivers over 1,000 tokens per second per user — a 15x improvement over previous generation hardware — while inference costs have plummeted 280-fold since late 2022.

## Consumer GPU Performance

For consumer-grade hardware, the NVIDIA RTX 5090 emerges as the new consumer champion for LLM inference, delivering up to 213 tokens/second on 8B models with its 32GB VRAM capacity. Additionally, the RTX 5090 leads consumer GPUs with 213 tokens/second, representing a 67% improvement over the RTX 4090, with this performance gain coming from both architectural improvements and increased memory bandwidth.

## Enterprise-Scale Benchmarks

NVIDIA Blackwell Ultra GPUs powered the highest-performing submissions across the broadest range of models and scenarios in MLPerf Inference v6.0, and only the NVIDIA platform submitted on every newly added benchmark.

In 2025, the AMD instinct MI350 Series, including the MI355X GPU, pushed the platform forward again with new AI data types, larger-model capacity and the inference gains shown throughout this submission.

## Benchmark Evolution

Llama 2/3 becoming standard LLM benchmark alongside BERT.

Note: The search results don't contain specific benchmarks focused on ModernBERT model inference. The results primarily cover general LLM inference benchmarks and broader GPU performance comparisons for 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f267da7-2f24-452e-8558-9678c74f3dfa",
  "isSidechain": true,
  "promptId": "1a22e9ee-ee99-4b4e-b0ca-b2e4481662f5",
  "agentId": "ab57b4cc9d1dfc52e",
  "type": "user",
  "uuid": "6de897a6-aed6-4560-aee0-19c1a41a8609",
  "sourceToolAssistantUUID": "9f267da7-2f24-452e-8558-9678c74f3dfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-09T20:44:51.617Z_

Based on my comprehensive search, here's what I found about ModernBERT throughput benchmarks:

## Summary of Findings

### Official Benchmarks (From arXiv:2412.13663)

**No H100 benchmarks exist in the official paper.** The authors explicitly chose to benchmark on an **NVIDIA RTX 4090** (consumer GPU) rather than enterprise hardware. As stated in their Hugging Face blog: *"First and foremost, ModernBERT is focused on practicality, not hype."*

**Documented throughput on RTX 4090:**
- **ModernBERT-large, fixed short-context (512 tokens):** 52,300 tokens/sec
- **ModernBERT-large, fixed long-context (8192 tokens):** 46,800 tokens/sec
- **ModernBERT-large, variable-length short:** 52,900 tokens/sec
- **ModernBERT-large, variable-length long:** 49,800 tokens/sec

For comparison, ModernBERT-base on RTX 4090 achieves 148,100 tokens/sec (fixed short-context).

### H100 Throughput (Estimated, Not Official)

**The 100-150K tokens/sec figure on H100 is UNVERIFIED.** Here's why:

1. **No official H100 benchmarks** - The ModernBERT paper and Hugging Face blog contain zero H100 performance data
2. **GPU scaling estimates** - Industry benchmarks show H100 delivers roughly **2-2.6x** the throughput of RTX 4090 for encoder models
3. **Rough extrapolation** - If you multiply RTX 4090's ~50-52K tokens/sec by 2-2.6x, you get approximately 100-135K tokens/sec—which aligns with the 100-150K range you mentioned, but this is **not an official figure**

### Hardware Used for Training

The Hugging Face model card confirms:
- **Training:** 8x H100 GPUs
- **Training data:** 2 trillion tokens
- **Recommended inference:** Flash Attention 2 for optimal efficiency

### Official Documentation Status

- **Paper:** No H100 inference benchmarks provided
- **Hugging Face blog:** RTX 4090 only
- **Model card:** No throughput metrics listed
- **GitHub repository:** Contains `benchmark.py` script but no published H100 results

## Answer to Your Questions

**Is 100-150K tokens/sec on H100 documented?** No, it is **unverified and not official**. It's a reasonable extrapolation based on H100/RTX-4090 performance scaling factors (2-2.6x), but the authors did not publish this figure.

**What hardware were the official benchmarks run on?** RTX 4090 (consumer GPU).

**What's the actual throughput range?** 
- **Verified (RTX 4090):** 46.8K - 52.9K tokens/sec for ModernBERT-large
- **Estimated (H100):** ~100-135K tokens/sec (unverified extrapolation)

## Sources

- [arXiv:2412.13663 - ModernBERT Paper](https://arxiv.org/html/2412.13663v2)
- [Hugging Face Blog - Finally, a Replacement for BERT: Introducing ModernBERT](https://huggingface.co/blog/modernbert)
- [ModernBERT-large Model Card](https://huggingface.co/answerdotai/ModernBERT-large)
- [NVIDIA GPU Benchmarks Documentation](https://www.cudocompute.com/blog/real-world-gpu-benchmarks)
- [H100 vs A100 GPU Comparisons](https://lyceum.technology/magazine/a100-vs-h100-for-llm-inference/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6de897a6-aed6-4560-aee0-19c1a41a8609",
  "isSidechain": true,
  "agentId": "ab57b4cc9d1dfc52e",
  "requestId": "req_011CaseWTjAU7NH795vk5sAL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1fec4752-29c8-44e0-940a-a8fff28c1248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3c884850-9858-4096-a616-f8f43a461503",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Df6BNXjdtdCQ1avCTfbet9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1117,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 25830,
      "output_tokens": 944,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1158
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1117,
          "output_tokens": 944,
          "cache_read_input_tokens": 25830,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1158,
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
