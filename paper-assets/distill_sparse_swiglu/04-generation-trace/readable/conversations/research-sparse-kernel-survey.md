# research sparse kernel survey

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 255
- **Recorded user turns:** 0
- **Tool calls:** 127
- **Original source:** `logs/chats/worker_research_sparse-kernel-survey_20260519T025318.jsonl`
- **Structured JSON:** [`b4a19203046e1d664c6f.json`](../../sessions/b4/b4a19203046e1d664c6f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

255 recorded events

### Tool call

_source line 1 · 2026-05-19T02:57:42.208346+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Triton sparse kernel research",
  "subagent_type": "Explore",
  "prompt": "Research Triton-based sparse matmul kernels for LLM activation sparsity inference. I need to find:\n\n1. Open-source Triton kernels for sparse matrix multiplication (especially activation sparsity, not weight pruning)\n2. Specifically search for:\n   - CATS paper implementation: https://github.com/ScalingIntelligence/CATS — look for their Triton kernels for sparse FFN\n   - Deja Vu sparse inference implementation on GitHub\n   - Any Triton kernel that does masked GEMM or sparse activation forwarding\n   - PowerInfer's sparse GPU kernel code\n   - triton-lang examples for sparse ops\n\n3. Search GitHub and the web for:\n   - \"triton sparse matmul\" implementations\n   - \"triton activation sparsity kernel\" \n   - \"triton masked gemm\"\n   - \"triton sparse ffn\"\n   - CATS activation sparsity kernel code\n   - Deja Vu sparse inference code\n\n4. For each implementation found, note:\n   - GitHub URL\n   - What kind of sparsity it supports (structured 2:4 vs unstructured)\n   - Whether it handles activation sparsity (dynamic, per-token masks) vs static weight sparsity\n   - Reported speedups\n   - How complex the kernel code is\n\nReport all findings with URLs and technical details. Be thorough — check multiple search terms."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Agent",
  "tool_args": {
    "description": "Triton sparse kernel research",
    "subagent_type": "Explore",
    "prompt": "Research Triton-based sparse matmul kernels for LLM activation sparsity inference. I need to find:\n\n1. Open-source Triton kernels for sparse matrix multiplication (especially activation sparsity, not weight pruning)\n2. Specifically search for:\n   - CATS paper implementation: https://github.com/ScalingIntelligence/CATS — look for their Triton kernels for sparse FFN\n   - Deja Vu sparse inference implementation on GitHub\n   - Any Triton kernel that does masked GEMM or sparse activation forwarding\n   - PowerInfer's sparse GPU kernel code\n   - triton-lang examples for sparse ops\n\n3. Search GitHub and the web for:\n   - \"triton sparse matmul\" implementations\n   - \"triton activation sparsity kernel\" \n   - \"triton masked gemm\"\n   - \"triton sparse ffn\"\n   - CATS activation sparsity kernel code\n   - Deja Vu sparse inference code\n\n4. For each implementation found, note:\n   - GitHub URL\n   - What kind of sparsity it supports (structured 2:4 vs unstructured)\n   - Whether it handles activation sparsity (dynamic, per-token masks) vs static weight sparsity\n   - Reported speedups\n   - How complex the kernel code is\n\nReport all findings with URLs and technical details. Be thorough — check multiple search terms."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-19T02:57:42.208789+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CATS paper Triton kernels sparse FFN GitHub ScalingIntelligence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CATS paper Triton kernels sparse FFN GitHub ScalingIntelligence"
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T02:57:42.208986+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Deja Vu sparse inference Triton GPU kernel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Deja Vu sparse inference Triton GPU kernel"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T02:57:42.209208+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PowerInfer sparse GPU kernel code Triton"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PowerInfer sparse GPU kernel code Triton"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T02:57:42.209373+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "triton sparse matmul activation sparsity kernel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "triton sparse matmul activation sparsity kernel"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T02:57:42.209502+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "triton masked GEMM sparse FFN implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "triton masked GEMM sparse FFN implementation"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T02:57:42.209622+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"triton\" \"sparse activation\" kernel LLM inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"triton\" \"sparse activation\" kernel LLM inference"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T02:57:42.209760+00:00_

Web search results for query: "triton sparse matmul activation sparsity kernel"

Links: [{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/html/2603.25011"},{"title":"triton-index/kernels/0013_Sparse_Matmul.md at main · gpu-mode/triton-index","url":"https://github.com/gpu-mode/triton-index/blob/main/kernels/0013_Sparse_Matmul.md"},{"title":"Implementing block-sparse matrix multiplication kernels using Triton","url":"https://openreview.net/pdf?id=doa11nN5vG"},{"title":"Supercharging JAX with Triton Kernels on AMD GPUs — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/jax-triton/README.html"},{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/pdf/2603.25011"},{"title":"From 11% to 88% Peak Bandwidth: Writing Custom Triton Kernels for LLM Inference | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2025/triton-kernels-llm-inference/"}]

Based on the search results, here's what I found about Triton sparse matmul activation sparsity kernels:

## Sparton: Sparse Matmul with Activation Sparsity

Sparton is an optimized Triton kernel that leverages tiled matrix multiplication, operator re-ordering, and sparse activation to alleviate memory bottlenecks and accelerate the LM head in LSR models. Sparton utilizes a fused approach that integrates the tiled matrix multiplication, ReLU, log1p, and max-reduction into a single GPU kernel.

By performing an early online reduction directly on raw logit tiles, Sparton avoids materializing the full logit matrix in memory. Experiments demonstrate that the Sparton kernel achieves up to a 4.8× speedup and an order-of-magnitude reduction in peak memory usage compared to PyTorch baselines.

## Block-Sparse Matrix Multiplication Kernels

Microsoft DeepSpeed provides Triton kernels for block-sparse matrix multiplication with code for sdd (sparse = dense x dense), dsd (dense = sparse x dense),
…[truncated 321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T02:57:42.209930+00:00_

Web search results for query: "CATS paper Triton kernels sparse FFN GitHub ScalingIntelligence"

Links: [{"title":"GitHub - ScalingIntelligence/CATS","url":"https://github.com/ScalingIntelligence/CATS"},{"title":"GitHub - bassrehab/triton-kernels: High-performance GPU kernels for LLM inference in OpenAI Triton. Fused RMSNorm, SwiGLU, INT8 GEMM with benchmarks and roofline analysis. · GitHub","url":"https://github.com/bassrehab/triton-kernels"},{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/pdf/2603.25011"},{"title":"GitHub - corl-team/flexsae: Official Triton kernels for TopK and HierarchicalTopK Sparse Autoencoder decoders. · GitHub","url":"https://github.com/corl-team/flexsae"},{"title":"GitHub - rkinas/triton-resources: A curated list of resources for learning and exploring Triton, OpenAI's programming language for writing efficient GPU code. · GitHub","url":"https://github.com/rkinas/triton-resources"},{"title":"Beating CUDA with Triton: A Fused MoE Dispatch Kernel for Mixtral and DeepSeek | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/fused-moe-dispatch-triton/"},{"title":"Scaling Intelligence Lab · GitHub","url":"https://github.com/ScalingIntelligence"}]

Based on the search results, here's what I found:

## CATS Paper Overview

The CATS paper, titled "Contextually-Aware Thresholding for Sparsity in Large Language Models," introduces a new method aimed at reducing the computational demands of deploying LLMs without sacrificing their performance on downstream tasks.

## Key Features

The method centers around a novel activation function that enhances activation sparsity effectively and efficiently. The CATS approach can be applied to various base models such as Mistral-7B and Llama2-7B, demonstrating a minimal performance drop (within 1-2% of the base models) even at 50% activation sparsity levels.

## GPU Kernel and Performance

CATS not only accelerates convergence but also integ
…[truncated 388 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T02:57:42.210127+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "PyTorch sparse + cuSPARSE research",
  "subagent_type": "Explore",
  "prompt": "Research PyTorch native sparse support and NVIDIA cuSPARSE/cuBLAS for LLM activation sparsity inference. I need:\n\n1. **PyTorch semi-structured sparsity**:\n   - `torch.sparse.to_sparse_semi_structured` — what does it support? Only 2:4 structured?\n   - Can it handle arbitrary unstructured sparsity (e.g., 30-50% of neurons zeroed per token)?\n   - Any PyTorch native way to do sparse matmul with dynamic masks efficiently?\n   - Search for torch.sparse APIs that could work for activation sparsity\n\n2. **cuSPARSE**:\n   - `cusparseSpMM` — can it do sparse activation × dense weight efficiently?\n   - What formats does it support (CSR, COO, etc.)?\n   - Is there overhead for converting dense activations to sparse format on-the-fly?\n   - Performance characteristics for 30-50% sparsity on modern GPUs\n   - Any benchmarks for cuSPARSE sparse GEMM vs dense GEMM at various sparsity levels?\n\n3. **cuBLAS**:\n   - Does cuBLAS have any sparse-aware GEMM?\n   - cuBLAS with structured sparsity (2:4) on Ampere+ GPUs\n\n4. **Key question**: For unstructured activation sparsity where the mask changes per token, what's the most efficient NVIDIA-native approach?\n\nSearch the web for benchmarks, documentation, and real-world usage reports. Report findings with links and performance numbers where available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Agent",
  "tool_args": {
    "description": "PyTorch sparse + cuSPARSE research",
    "subagent_type": "Explore",
    "prompt": "Research PyTorch native sparse support and NVIDIA cuSPARSE/cuBLAS for LLM activation sparsity inference. I need:\n\n1. **PyTorch semi-structured sparsity**:\n   - `torch.sparse.to_sparse_semi_structured` — what does it support? Only 2:4 structured?\n   - Can it handle arbitrary unstructured sparsity (e.g., 30-50% of neurons zeroed per token)?\n   - Any PyTorch native way to do sparse matmul with dynamic masks efficiently?\n   - Search for torch.sparse APIs that could work for activation sparsity\n\n2. **cuSPARSE**:\n   - `cusparseSpMM` — can it do sparse activation × dense weight efficiently?\n   - What formats does it support (CSR, COO, etc.)?\n   - Is there overhead for converting dense activations to sparse format on-the-fly?\n   - Performance characteristics for 30-50% sparsity on modern GPUs\n   - Any benchmarks for cuSPARSE sparse GEMM vs dense GEMM at various sparsity levels?\n\n3. **cuBLAS**:\n   - Does cuBLAS have any sparse-aware GEMM?\n   - cuBLAS with structured sparsity (2:4) on Ampere+ GPUs\n\n4. **Key question**: For unstructured activation sparsity where the mask changes per token, what's the most efficient NVIDIA-native approach?\n\nSearch the web for benchmarks, documentation, and real-world usage reports. Report findings with links and performance numbers where available."
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T02:57:42.210325+00:00_

Web search results for query: "PowerInfer sparse GPU kernel code Triton"

Links: [{"title":"Introducing Triton: Open-source GPU programming for neural networks | OpenAI","url":"https://openai.com/index/triton/"},{"title":"Triton — GPU Programming for Neural Networks | by Dhananjay Kumar | Medium","url":"https://dhnanjay.medium.com/triton-gpu-programming-for-neural-networks-16271d729f78"},{"title":"GitHub - rkinas/triton-resources: A curated list of resources for learning and exploring Triton, OpenAI's programming language for writing efficient GPU code. · GitHub","url":"https://github.com/rkinas/triton-resources"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/pdf/2312.12456"},{"title":"Triton Kernel Implementation","url":"https://www.emergentmind.com/topics/triton-kernel-implementation"},{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/pdf/2603.25011"},{"title":"Triton GPU Kernel Programming Guide: CUDA Alternative | RightNow AI | RightNow AI","url":"https://www.rightnowai.co/guides/frameworks/triton"},{"title":"Unlock Peak Performance on AMD GPUs with Triton Kernel Optimizations — ROCm Blogs","url":"https://rocm.blogs.amd.com/software-tools-optimization/kernel-development-optimizations-with-triton-on-/README.html"}]

Based on the search results, I found relevant information about PowerInfer and sparse GPU kernels with Triton:

## PowerInfer Sparse GPU Kernels

PowerInfer designs neuron-aware sparse operators that directly interact with individual neurons, bypassing operations on entire matrices. This approach enables efficient matrix-vector multiplication at the neuron level and removes the need for specific sparse format conversions.

Conventional libraries like cuSPARSE are not optimal due to their general-purpose design, which includes tracking each non-zero element and converting dense matrices into sparse formats.

## Triton's Capabili
…[truncated 824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T02:57:42.210533+00:00_

Web search results for query: "Deja Vu sparse inference Triton GPU kernel"

Links: [{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/html/2603.25011"},{"title":"Triton — GPU Programming for Neural Networks | by Dhananjay Kumar | Medium","url":"https://dhnanjay.medium.com/triton-gpu-programming-for-neural-networks-16271d729f78"},{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/pdf/2603.25011"},{"title":"GitHub - bassrehab/triton-kernels: High-performance GPU kernels for LLM inference in OpenAI Triton. Fused RMSNorm, SwiGLU, INT8 GEMM with benchmarks and roofline analysis. · GitHub","url":"https://github.com/bassrehab/triton-kernels"},{"title":"Insum: Sparse GPU Kernels Simplified and Optimized with Indirect Einsums","url":"https://spice.cs.umd.edu/proceedings/5_Insum.pdf"},{"title":"The Anatomy of a Triton Attention Kernel","url":"https://arxiv.org/html/2511.11581v1"}]

Based on the search results, I found relevant information about sparse inference and Triton GPU kernels, though the specific project "Deja Vu" wasn't prominently featured in the results. Here's what I found:

## Sparse Inference with Triton Kernels

Triton enables easy implementation of custom operations with irregular memory access patterns like sparse kernels, which are challenging for other systems.

### Sparton: A Key Example

One notable project related to sparse inference is Sparton. Sparton is a fast, memory-efficient Triton kernel tailored for the LM head in learned sparse retrieval (LSR) models, utilizing a fused approach that integrates tiled matrix multiplication, ReLU, log1p, and max-reduction into a single GPU kernel. The Sparton kernel achieves up to 4.8× speedup and an order-of-magnitude reduction in peak memory usage compared to PyTorch baselines.

### Other Sparse Inference Approaches

Triton kernels can fuse gather, matmul, and scatter operations into a si
…[truncated 468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T02:57:42.210703+00:00_

Web search results for query: "triton masked GEMM sparse FFN implementation"

Links: [{"title":"GitHub - ChangLiuCat/FlexGEMM-arch: A Cross-Platform Backend for High-Performance Sparse Convolutions · GitHub","url":"https://github.com/ChangLiuCat/FlexGEMM-arch"},{"title":"GitHub - JeffreyXiang/FlexGEMM: A Cross-Platform Backend for High-Performance Sparse Convolutions · GitHub","url":"https://github.com/JeffreyXiang/FlexGEMM"},{"title":"Beating CUDA with Triton: A Fused MoE Dispatch Kernel for Mixtral and DeepSeek | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/fused-moe-dispatch-triton/"},{"title":"Jianfeng Xiang | Blogs | FlexGEMM: A Cross-Platform Backend for High-Performance Sparse Convolutions","url":"https://jeffreyxiang.github.io/en/blogs/flexgemm"},{"title":"Deploying DeepSeek with PD Disaggregation and Large-Scale Expert Parallelism on 96 H100 GPUs - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2025-05-05-large-scale-ep/"},{"title":"Accelerating a Triton Fused Kernel for W4A16 Quantized Inference with   SplitK work decomposition","url":"https://arxiv.org/pdf/2402.00025"},{"title":"tritonBLAS: Triton-based Analytical Approach for GEMM Kernel Parameter Selection","url":"https://arxiv.org/pdf/2512.04226"},{"title":"Triton Tutorial #2 | by Sherlock | Medium","url":"https://medium.com/@sherlockliao01/triton-tutorial-2-5de66cd2170d"},{"title":"tritonBLAS: Triton-based Analytical Approach for GEMM Kernel Parameter Selection","url":"https://arxiv.org/html/2512.04226v1"}]

Based on the search results, here are the key findings related to your query about Triton masked GEMM sparse FFN implementation:

## Triton-Powered Sparse GEMM Implementations

FlexGEMM is a high-performance, Triton-powered GEMM backend designed for 3D sparse convolutions that implements Explicit, Implicit, and Masked Implicit algorithm variants, featuring optional Split-K parallelism for sparse GEMM.

## Masked Implicit GEMM Performance

Masked Implicit GEMM often improve
…[truncated 1170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T02:57:42.210858+00:00_

Web search results for query: ""triton" "sparse activation" kernel LLM inference"

Links: [{"title":"Mixture-of-Channels: Exploiting Sparse FFNs for Efficient LLMs Pre-Training and Inference","url":"https://arxiv.org/html/2511.09323"},{"title":"GitHub - bassrehab/triton-kernels: High-performance GPU kernels for LLM inference in OpenAI Triton. Fused RMSNorm, SwiGLU, INT8 GEMM with benchmarks and roofline analysis. · GitHub","url":"https://github.com/bassrehab/triton-kernels"},{"title":"From 11% to 88% Peak Bandwidth: Writing Custom Triton Kernels for LLM Inference | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2025/triton-kernels-llm-inference/"},{"title":"Liger Kernel: Efficient Triton Kernels for LLM Training","url":"https://arxiv.org/pdf/2410.10989"},{"title":"Triton Kernel Implementation","url":"https://www.emergentmind.com/topics/triton-kernel-implementation"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"}]

I've found several relevant results about Triton kernels and sparse activation for LLM inference. Here's what the search uncovered:

## Sparse Activation with Triton Kernels

Custom forward and backward kernels for sparse architectures can be designed using Triton, as demonstrated in the Mixture-of-Channels (MoC) research. Fused Triton kernels can accelerate intermediate computations in sparse models, and sparse architectures like MoC achieve around 1.13× speedup in end-to-end decoding latency.

## General Triton Optimization for LLM Inference

Most LLM inference operations are memory-bound, which is why optimizations focus on reducing memory traffic rather than raw FLOPS. Triton can fuse operations into one kernel, achieving up to 8x speedup compared to PyTorch's multiple small kernels.

Fused Triton kernels with SplitK work decomposition for W4A16 quantized inference achieve average speedups of 65% on NVIDIA A100 and 124% on H100.

## Sparse Activation Pred
…[truncated 306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T02:57:42.211008+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PyTorch torch.sparse.to_sparse_semi_structured 2:4 structured sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PyTorch torch.sparse.to_sparse_semi_structured 2:4 structured sparsity"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T02:57:42.211161+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PyTorch sparse matmul activation sparsity unstructured dynamic masks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PyTorch sparse matmul activation sparsity unstructured dynamic masks"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T02:57:42.211280+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NVIDIA cuSPARSE cusparseSpMM sparse activation dense weight performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NVIDIA cuSPARSE cusparseSpMM sparse activation dense weight performance"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T02:57:42.211395+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cuSPARSE CSR COO format sparse GEMM overhead benchmark sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cuSPARSE CSR COO format sparse GEMM overhead benchmark sparsity"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T02:57:42.211511+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cuBLAS sparse GEMM Ampere structured sparsity 2:4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cuBLAS sparse GEMM Ampere structured sparsity 2:4"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T02:57:42.211623+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM unstructured activation sparsity NVIDIA CUDA sparse inference benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM unstructured activation sparsity NVIDIA CUDA sparse inference benchmark"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T02:57:42.211734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PyTorch torch.sparse API sparse matmul COO CSR dense"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PyTorch torch.sparse API sparse matmul COO CSR dense"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T02:57:42.211843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "sparse neural network activation sparsity per-token mask dynamic inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "sparse neural network activation sparsity per-token mask dynamic inference"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T02:57:42.211977+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "DeepSparse + vLLM sparse research",
  "subagent_type": "Explore",
  "prompt": "Research Neural Magic / DeepSparse and vLLM sparse inference capabilities for LLM activation sparsity. I need:\n\n1. **Neural Magic / DeepSparse / nm-vllm**:\n   - Does DeepSparse support activation sparsity (dynamic, per-token) or only weight sparsity?\n   - What sparse formats does it use?\n   - Is it GPU-accelerated or CPU-only?\n   - Search: \"deepsparse activation sparsity\", \"neural magic sparse llm inference\", \"nm-vllm sparse\"\n   - Any support for SwiGLU/GatedMLP sparse inference?\n\n2. **vLLM sparse support**:\n   - Does vLLM have any sparse kernel integration?\n   - Search: \"vllm sparse inference\", \"vllm activation sparsity\"\n   - Any plugins or extensions for sparse inference in vLLM?\n\n3. **PowerInfer**:\n   - PowerInfer uses activation sparsity for inference — how does their sparse kernel work?\n   - Search GitHub: \"powerinfer\" sparse GPU kernel source code\n   - Is their sparse kernel reusable independently?\n   - What speedups do they report?\n   - Search: \"powerinfer sparse kernel\", \"powerinfer gpu sparse matmul\"\n\n4. **RelayAttention / other frameworks**:\n   - Any other inference frameworks that support dynamic activation sparsity?\n\nSearch the web and GitHub thoroughly. Report URLs, supported sparsity types, and performance data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Agent",
  "tool_args": {
    "description": "DeepSparse + vLLM sparse research",
    "subagent_type": "Explore",
    "prompt": "Research Neural Magic / DeepSparse and vLLM sparse inference capabilities for LLM activation sparsity. I need:\n\n1. **Neural Magic / DeepSparse / nm-vllm**:\n   - Does DeepSparse support activation sparsity (dynamic, per-token) or only weight sparsity?\n   - What sparse formats does it use?\n   - Is it GPU-accelerated or CPU-only?\n   - Search: \"deepsparse activation sparsity\", \"neural magic sparse llm inference\", \"nm-vllm sparse\"\n   - Any support for SwiGLU/GatedMLP sparse inference?\n\n2. **vLLM sparse support**:\n   - Does vLLM have any sparse kernel integration?\n   - Search: \"vllm sparse inference\", \"vllm activation sparsity\"\n   - Any plugins or extensions for sparse inference in vLLM?\n\n3. **PowerInfer**:\n   - PowerInfer uses activation sparsity for inference — how does their sparse kernel work?\n   - Search GitHub: \"powerinfer\" sparse GPU kernel source code\n   - Is their sparse kernel reusable independently?\n   - What speedups do they report?\n   - Search: \"powerinfer sparse kernel\", \"powerinfer gpu sparse matmul\"\n\n4. **RelayAttention / other frameworks**:\n   - Any other inference frameworks that support dynamic activation sparsity?\n\nSearch the web and GitHub thoroughly. Report URLs, supported sparsity types, and performance data."
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T02:57:42.212248+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com CATS sparse FFN activation kernel ScalingIntelligence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com CATS sparse FFN activation kernel ScalingIntelligence"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T02:57:42.212380+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DejaVu\" sparse inference LLM GitHub implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DejaVu\" sparse inference LLM GitHub implementation"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T02:57:42.212501+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com triton sparse FFN activation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com triton sparse FFN activation"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T02:57:42.212615+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mixture-of-Channels MoC sparse FFN Triton kernel GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mixture-of-Channels MoC sparse FFN Triton kernel GitHub"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T02:57:42.212728+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparseInfer activation sparsity fast inference code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparseInfer activation sparsity fast inference code"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T02:57:42.212838+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com sparse activation mask matmul CUDA Triton"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com sparse activation mask matmul CUDA Triton"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T02:57:42.212998+00:00_

Web search results for query: ""DejaVu" sparse inference LLM GitHub implementation"

Links: [{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://proceedings.mlr.press/v202/liu23am.html"},{"title":"GitHub - FMInference/DejaVu · GitHub","url":"https://github.com/FMInference/DejaVu"},{"title":"Paper page - Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://huggingface.co/papers/2310.17157"},{"title":"Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://www.emergentmind.com/papers/2310.17157"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time | OpenReview","url":"https://openreview.net/forum?id=wIPIhHd00i"},{"title":"ICML 2023 Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time Oral","url":"https://icml.cc/virtual/2023/oral/25453"},{"title":"Deja Vu: contextual sparsity for efficient LLMs at inference ...","url":"https://dl.acm.org/doi/10.5555/3618408.3619327"},{"title":"[PDF] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deja-Vu:-Contextual-Sparsity-for-Efficient-LLMs-at-Liu-Wang/95240dda409e28acccdc5cf619ad0c036cf4292d"}]

Based on the search results, here's what I found about DejaVu:

## Overview

DejaVu is a system that uses a low-cost algorithm to predict contextual sparsity on the fly given inputs to each layer, along with an asynchronous and hardware-aware implementation that speeds up LLM inference.

## How It Works

Contextual sparsity consists of small, input-dependent sets of attention heads and MLP parameters that yield approximately the same output as the dense model for a given input. The system uses an asynchronous look-ahead mechanism that exploits the properties of residual connections in LLMs, noting that token embeddings c
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T02:57:42.213199+00:00_

Web search results for query: "site:github.com triton sparse FFN activation"

Links: [{"title":"Spark Transformer: Reactivating Sparsity in FFN and Attention","url":"https://arxiv.org/pdf/2506.06644"},{"title":"The triton operators performed worse after fusion · Issue #135994 · pytorch/pytorch","url":"https://github.com/pytorch/pytorch/issues/135994"},{"title":"GitHub - Doraemonzzz/Awesome-Triton-Resources: Awesome Triton Resources","url":"https://github.com/Doraemonzzz/Awesome-Triton-Resources"},{"title":"GitHub - Raincleared-Song/sparse_gpu_operator: GPU operators for sparse tensor operations","url":"https://github.com/Raincleared-Song/sparse_gpu_operator"},{"title":"GitHub - XunhaoLai/native-sparse-attention-triton: Efficient triton implementation of Native Sparse Attention. · GitHub","url":"https://github.com/XunhaoLai/native-sparse-attention-triton"},{"title":"Accelerating Transformer Inference and Training with 2:4 Activation   Sparsity","url":"https://arxiv.org/pdf/2503.16672"},{"title":"GitHub - rkinas/triton-resources: A curated list of resources for learning and exploring Triton, OpenAI's programming language for writing efficient GPU code. · GitHub","url":"https://github.com/rkinas/triton-resources"}]

I found several relevant results related to Triton, sparse operations, and FFN activations. Here are the key findings:

## GitHub Resources

1. **sparse_gpu_operator** - This repository contains GPU operators tailored for the ReLU-activated FFNs in LLM, from the paper "ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models".

2. **native-sparse-attention-triton** - This repository implements the sparse attention mechanism introduced in the paper "Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention" and provides an efficient training implementation based on Triton.

3. **Awesome-Triton-Resources** - This curated collection includes triton-activations (a collection of neural network activa
…[truncated 704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T02:57:42.213362+00:00_

Web search results for query: "site:github.com sparse activation mask matmul CUDA Triton"

Links: [{"title":"Segfault when using blocksparse matmul in attention · Issue #237 · triton-lang/triton","url":"https://github.com/triton-lang/triton/issues/237"},{"title":"CUDA errors on kernels after block sparse Triton ops · Issue #882 · triton-lang/triton","url":"https://github.com/triton-lang/triton/issues/882"},{"title":"triton-index/kernels/0013_Sparse_Matmul.md at main · gpu-mode/triton-index","url":"https://github.com/gpu-mode/triton-index/blob/main/kernels/0013_Sparse_Matmul.md"},{"title":"GitHub - dropbox/gemlite: Fast low-bit matmul kernels in Triton · GitHub","url":"https://github.com/mobiusml/gemlite"},{"title":"GitHub - rkinas/triton-resources: A curated list of resources for learning and exploring Triton, OpenAI's programming language for writing efficient GPU code. · GitHub","url":"https://github.com/rkinas/triton-resources"},{"title":"Is there a triton implementation of block sparse flash attention? · Issue #2012 · triton-lang/triton","url":"https://github.com/triton-lang/triton/issues/2012"},{"title":"GitHub - zhengqigao/hbsattn: a high-performance Block Sparse Attention kernel in Triton","url":"https://github.com/zhengqigao/hbsattn"}]

The search results show several GitHub repositories and issues related to sparse activation masks, matmul operations, CUDA, and Triton:

1. **Triton block-sparse matmul issues**: The Triton library provides block-sparse matmul operations for attention mechanisms with different configurations like "sdd" and "dsd" formats.

2. **Block-sparse linear layers**: There are implementations of block-sparse linear layers using Triton's block-sparse matmul operations with sparsity masks.

3. **Sparse matmul resources**: Collections of Triton kernels for block-sparse matrix multiplication exist in projects like DeepSpeed.

4. **GemLite**: GemLite is a collection of Triton kernels designed for efficient low-bit matrix multiplication, whic
…[truncated 585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T02:57:42.213517+00:00_

Web search results for query: "Mixture-of-Channels MoC sparse FFN Triton kernel GitHub"

Links: [{"title":"Mixture-of-Channels: Exploiting Sparse FFNs for Efficient LLMs Pre-Training and Inference","url":"https://arxiv.org/html/2511.09323v1"},{"title":"Mixture-of-Channels: Exploiting Sparse FFNs for","url":"https://arxiv.org/pdf/2511.09323"},{"title":"MIXTURE-OF-CHANNELS: EXPLOITING SPARSE FFNS","url":"https://openreview.net/pdf/38a07407d0c06c24ef08347e72aee697cd35a93a.pdf"},{"title":"[2511.09323] Mixture-of-Channels: Exploiting Sparse FFNs for Efficient LLMs Pre-Training and Inference","url":"https://arxiv.org/abs/2511.09323"},{"title":"GitHub - rkinas/triton-resources: A curated list of resources for learning and exploring Triton, OpenAI's programming language for writing efficient GPU code. · GitHub","url":"https://github.com/rkinas/triton-resources"},{"title":"GitHub - shawntan/scattermoe: Triton-based implementation of Sparse Mixture of Experts.","url":"https://github.com/shawntan/scattermoe"}]

Based on the search results, I found information about Mixture-of-Channels (MoC):

Mixture-of-Channels (MoC) is a novel FFN architecture that selectively activates only the Top-K most relevant channels per token determined by SwiGLU's native gating mechanism.

Regarding the Triton kernel implementation: Custom forward and backward kernels for the MoC architecture were designed using Triton, delivering comparable training throughput and approximately a 1.4× decoding speedup in the FFN compared to standard LLaMA-style Transformer implementations.

The research comes from a paper titled "Mixture-of-Channels: Exploiting Sparse FFNs for Efficient LLMs Pre-Training and Inference" published on arXiv. The paper describes how MoC demonstrates substantial memory savings while outperforming existing memory-efficient methods in performance, and during inference, MoC achieves a 1.13× speedup in end-to-end decoding latency.

However, the search results do not show a direct link to a 
…[truncated 260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T02:57:42.213666+00:00_

Web search results for query: "PyTorch torch.sparse.to_sparse_semi_structured 2:4 structured sparsity"

Links: [{"title":"(beta) Accelerating BERT with semi-structured (2:4) sparsity — PyTorch Tutorials 2.11.0+cu130 documentation","url":"https://docs.pytorch.org/tutorials/advanced/semi_structured_sparse.html"},{"title":"(prototype) Accelerating BERT with semi-structured (2:4) sparsity — PyTorch Tutorials 2.6.0+cu124 documentation","url":"https://pytorch.org/tutorials/prototype/semi_structured_sparse.html?highlight=transformer"},{"title":"(prototype) Accelerating BERT with semi-structured (2:4) sparsity — PyTorch Tutorials 2.8.0+cu128 documentation","url":"https://docs.pytorch.org/tutorials/unstable/semi_structured_sparse.html"},{"title":"2:4 semi structured sparsity matmul not supported on hopper · Issue #132009 · pytorch/pytorch","url":"https://github.com/pytorch/pytorch/issues/132009"},{"title":"'torch.sparse.to_sparse_semi_structured' significantly worsens performance on H100 GPUs · Issue #153825 · pytorch/pytorch","url":"https://github.com/pytorch/pytorch/issues/153825"},{"title":"Accelerating Neural Network Training with Semi-Structured (2:4) Sparsity – PyTorch","url":"https://pytorch.org/blog/accelerating-neural-network-training/"},{"title":"CoCalc -- semi_structured_sparse.py","url":"https://cocalc.com/github/pytorch/tutorials/blob/main/advanced_source/semi_structured_sparse.py"},{"title":"PyTorch: torch/sparse/semi_structured.py | Fossies","url":"https://fossies.org/linux/pytorch/torch/sparse/semi_structured.py"}]

Based on the search results, here's information about PyTorch's `torch.sparse.to_sparse_semi_structured` and 2:4 structured sparsity:

## Overview

A 2:4-sparse matrix is a matrix where at most 2 elements are non-zero for every 4 elements. For users with existing 2:4 sparse models, accelerating nn.Linear layers for inference with to_sparse_semi_structured is quite straightforward.

## Key Benefits

Unlike previous sparse formats, semi-structured s
…[truncated 827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T02:57:42.213821+00:00_

Web search results for query: "NVIDIA cuSPARSE cusparseSpMM sparse activation dense weight performance"

Links: [{"title":"cuSPARSE | NVIDIA Developer","url":"https://developer.nvidia.com/cusparse"},{"title":"Accelerating Matrix Multiplication with Block Sparse Format and NVIDIA Tensor Cores | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/accelerating-matrix-multiplication-with-block-sparse-format-and-nvidia-tensor-cores/"},{"title":"High-Performance Sparse Linear Algebra on NVIDIA GPUs ...","url":"https://graphblas.org/GraphBLAS-Pointers/Slides/SIAMCSE21-Nvidia-cuSPARSE.pdf"},{"title":"Exploiting NVIDIA Ampere Structured Sparsity with cuSPARSELt | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/exploiting-ampere-structured-sparsity-with-cusparselt/"},{"title":"CUDALibrarySamples/cuSPARSE at master · NVIDIA/CUDALibrarySamples","url":"https://github.com/NVIDIA/CUDALibrarySamples/tree/master/cuSPARSE"},{"title":"cuSPARSE SpMV/SpMM performance and upperbound: Nvidia Pascal P100 GPU... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/cuSPARSE-SpMV-SpMM-performance-and-upperbound-Nvidia-Pascal-P100-GPU-Fig-1-displays_fig1_325706323"},{"title":"Acc-SpMM: Accelerating General-purpose Sparse Matrix-Matrix   Multiplication with GPU Tensor Cores","url":"https://arxiv.org/pdf/2501.09251"},{"title":"High Performance Unstructured SpMM Computation Using Tensor Cores","url":"https://arxiv.org/pdf/2408.11551"}]

Based on the search results, here's what I found about NVIDIA cuSPARSE cusparseSpMM sparse activation dense weight performance:

## Overview

The cuSPARSE library provides cusparseSpMM routine for SpMM operations (sparse-matrix dense-matrix multiplication). The cuSPARSE library is highly optimized for performance on NVIDIA GPUs, with SpMM performance 30-150X faster than CPU-only alternatives.

## Performance Characteristics

When the block size is 32, the kernel is faster than cuBLAS if the density is less than 40% 
…[truncated 899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T02:57:42.213974+00:00_

Web search results for query: "PyTorch torch.sparse API sparse matmul COO CSR dense"

Links: [{"title":"Sparse Tensors in PyTorch","url":"https://runebook.dev/en/articles/pytorch/sparse"},{"title":"torch_geometric.utils._spmm — pytorch_geometric documentation","url":"https://pytorch-geometric.readthedocs.io/en/latest/_modules/torch_geometric/utils/_spmm.html"},{"title":"torch.sparse — PyTorch master documentation","url":"https://glaringlee.github.io/sparse.html"},{"title":"Memory-Efficient Aggregations — pytorch_geometric documentation","url":"https://pytorch-geometric.readthedocs.io/en/2.5.1/advanced/sparse_tensor.html"},{"title":"Mastering PyTorch's torch.sparse: A Friendly Guide to Common Issues and Fixes","url":"https://runebook.dev/en/docs/pytorch/sparse"},{"title":"GitHub - rusty1s/pytorch_sparse: PyTorch Extension Library of Optimized Autograd Sparse Matrix Operations · GitHub","url":"https://github.com/rusty1s/pytorch_sparse"},{"title":"torch.sparse_csr_tensor — PyTorch 2.10 documentation","url":"https://docs.pytorch.org/docs/stable/generated/torch.sparse_csr_tensor.html"}]

Based on the search results, here's information about PyTorch's sparse tensor API for matrix multiplication with COO, CSR, and dense formats:

## Sparse Tensor Formats

PyTorch supports sparse tensors in COO(rdinate) format, which can efficiently store and process tensors for which the majority of elements are zeros. Additionally, PyTorch provides conversion functions like torch.sparse.csr_tensor() to convert sparse tensors to Compressed Sparse Row (CSR) format.

## Sparse-Dense Matrix Multiplication

The function torch.sparse.mm() performs matrix multiplication between a sparse matrix and a dense matrix. torch.matmul() has a special implementation for sparse-dense matrix multiplication.

## Format Optimization

COO format can be converted to CSR format for more efficient processing, and documentation warns about converting sparse tensors to CSR format beforehand to avoid repeated conver
…[truncated 570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T02:57:42.214145+00:00_

Web search results for query: "PyTorch sparse matmul activation sparsity unstructured dynamic masks"

Links: [{"title":"Accelerating Neural Network Training with Semi-Structured (2:4) Sparsity – PyTorch","url":"https://pytorch.org/blog/accelerating-neural-network-training/"},{"title":"[RFC] Plans for sparsity · Issue #143 · pytorch/ao","url":"https://github.com/pytorch/ao/issues/143"},{"title":"Sparsity Made Easy – Introducing the Cerebras PyTorch Sparsity Library - Cerebras","url":"https://www.cerebras.ai/blog/sparsity-made-easy-introducing-the-cerebras-pytorch-sparsity-library"},{"title":"ao/torchao/sparsity/README.md at main · pytorch/ao","url":"https://github.com/pytorch/ao/blob/main/torchao/sparsity/README.md"},{"title":"pytorch masked matmul with sparse mask · GitHub","url":"https://gist.github.com/persiyanov/9454dc94a08b64337fcc1629d316e87e"},{"title":"Accelerating Deep Neural Networks via Semi-Structured Activation   Sparsity","url":"https://arxiv.org/pdf/2309.06626"},{"title":"Efficient Dynamic Structured Sparse Training with Learned Shuffles","url":"https://arxiv.org/pdf/2510.14812"},{"title":"Masked Matrix Multiplication for Emergent Sparsity","url":"https://arxiv.org/pdf/2402.14118"}]

I found several relevant results about PyTorch sparse matrix multiplication and activation sparsity. Here's a summary of the key findings:

## Semi-Structured Sparsity and Dynamic Masks

PyTorch supports dynamic sparsity masks that are recomputed at every training step as weights are continuously updated during optimization. During sparse training with 2:4 sparsity, the sparsity mask on weights is dynamically recomputed at every step.

## Unstructured Sparsity Challenges

Unstructured pruning allows every parameter to have its own mask, giving the most flexibility but requiring very high sparsity (>98%) in order to provide performance benefits. The parallel nature of GPU backends makes accelerating unstructured sparsity difficult.

## Activation Sparsity

One approach invo
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T02:57:42.214300+00:00_

Web search results for query: "cuSPARSE CSR COO format sparse GEMM overhead benchmark sparsity"

Links: [{"title":"A Framework for General Sparse Matrix-Matrix Multiplication on GPUs and Heterogeneous Processors | Request PDF","url":"https://www.researchgate.net/publication/275280146_A_Framework_for_General_Sparse_Matrix-Matrix_Multiplication_on_GPUs_and_Heterogeneous_Processors"},{"title":"Sparse GEMM and Tensor Core’s Structured Sparsity | by Huan Xu | Medium","url":"https://medium.com/@hxu296/exploring-spgemm-and-nvidias-leap-in-deep-neural-network-efficiency-d367adc68791"},{"title":"SparseRT: Accelerating Unstructured Sparsity on GPUs for Deep","url":"https://arxiv.org/pdf/2008.11849"},{"title":"1. Introduction — cuSPARSE 13.2 documentation","url":"https://docs.nvidia.com/cuda/cusparse/index.html"},{"title":"cuSPARSE Storage Formats — cuSPARSE 12.6 documentation","url":"https://docs.nvidia.com/cuda/cusparse/storage-formats.html"},{"title":"cuSPARSE | NVIDIA Developer","url":"https://developer.nvidia.com/cusparse"},{"title":"CUSPARSE: CSR GEMM should dispatch to mm!/cusparseSpGEMM · Issue #1511 · JuliaGPU/CUDA.jl","url":"https://github.com/JuliaGPU/CUDA.jl/issues/1511"},{"title":"cuSPARSE Release 13.2 NVIDIA Corporation Apr 02, 2026","url":"https://docs.nvidia.com/cuda/pdf/CUSPARSE_Library.pdf"},{"title":"cuSPARSE — Pyculib 1.0.1 documentation","url":"https://pyculib.readthedocs.io/en/latest/cusparse.html"}]

I've completed the web search with your query. Here are the key findings:

## Search Results Summary

The search returned information about sparse matrix formats and operations in the context of GPU computing. Here are the relevant insights:

**Sparse Matrix Formats:**
Storage of sparse matrices involves three primary compressed formats — Coordinate (COO), Compressed Sparse Row (CSR), and Compressed Sparse Column (CSC). COO records non-zeros with their values and positional information in three arrays, providing an intuitive but space-inefficient method. CSR
…[truncated 1193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T02:57:42.214446+00:00_

Web search results for query: "LLM unstructured activation sparsity NVIDIA CUDA sparse inference benchmark"

Links: [{"title":"Sakana AI and NVIDIA Introduce TwELL: 20.5% Faster LLM Inference via Unstructured Sparsity • Dev|Journal","url":"https://earezki.com/ai-news/2026-05-11-sakana-ai-and-nvidia-introduce-twell-with-cuda-kernels-for-205-inference-and-219-training-speedup-in-llms/"},{"title":"Sakana AI and NVIDIA Introduce TwELL with CUDA Kernels for 20.5% Inference and 21.9% Training Speedup in LLMs - MarkTechPost","url":"https://www.marktechpost.com/2026/05/11/sakana-ai-and-nvidia-introduce-twell-with-cuda-kernels-for-20-5-inference-and-21-9-training-speedup-in-llms/"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://pub.sakana.ai/sparser-faster-llms/"},{"title":"GitHub - SakanaAI/sparser-faster-llms: Cuda kernels for leveraging LLM sparsity to improve throughput and decrease the memory requirements during inference and training. · GitHub","url":"https://github.com/SakanaAI/sparser-faster-llms"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/pdf/2603.23198"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation","url":"https://arxiv.org/pdf/2507.01299"}]

Based on the web search results, here's what I found about LLM unstructured activation sparsity with NVIDIA CUDA sparse inference:

## Key Recent Development

Sakana AI and NVIDIA introduced TwELL and custom CUDA kernels, achieving 20.5% inference and 21.9% training speedups in LLMs by exploiting activation sparsity.

## Technical Approach

Sakana AI and NVIDIA researchers have developed TwELL, a new sparse data format and custom CUDA kernels for gated feedforward l
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T02:57:42.214589+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSparse activation sparsity dynamic per-token LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSparse activation sparsity dynamic per-token LLM"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T02:57:42.214709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Neural Magic sparse LLM inference weight activation sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Neural Magic sparse LLM inference weight activation sparsity"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T02:57:42.214824+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "nm-vllm sparse inference vLLM integration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "nm-vllm sparse inference vLLM integration"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T02:57:42.214936+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "vLLM sparse kernel inference activation sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "vLLM sparse kernel inference activation sparsity"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T02:57:42.215066+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PowerInfer sparse GPU kernel activation sparsity LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PowerInfer sparse GPU kernel activation sparsity LLM"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T02:57:42.215183+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PowerInfer sparse matmul kernel source code GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PowerInfer sparse matmul kernel source code GitHub"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-19T02:57:42.215292+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSparse SwiGLU GatedMLP sparse inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSparse SwiGLU GatedMLP sparse inference"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T02:57:42.215399+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "vLLM sparse inference plugins extensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "vLLM sparse inference plugins extensions"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T02:57:42.215519+00:00_

Web search results for query: "PowerInfer sparse matmul kernel source code GitHub"

Links: [{"title":"GitHub - mstnegate/int4matmul_kernels","url":"https://github.com/mstnegate/int4matmul_kernels"},{"title":"tensorflow/tensorflow/core/kernels/sparse_matmul_op_test.cc at master · tensorflow/tensorflow","url":"https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/kernels/sparse_matmul_op_test.cc"},{"title":"GitHub - openai/blocksparse: Efficient GPU kernels for block-sparse matrix multiplication and convolution","url":"https://github.com/openai/blocksparse"},{"title":"tensorflow_makefile/tensorflow/python/kernel_tests/sparse_matmul_op_test.py at master · petewarden/tensorflow_makefile","url":"https://github.com/petewarden/tensorflow_makefile/blob/master/tensorflow/python/kernel_tests/sparse_matmul_op_test.py"},{"title":"tensorflow/tensorflow/core/kernels/sparse_tensor_dense_matmul_op.cc at master · tensorflow/tensorflow","url":"https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/kernels/sparse_tensor_dense_matmul_op.cc"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/pdf/2312.12456"},{"title":"GitHub - CMU-SAFARI/SparseP: SparseP is the first open-source Sparse Matrix Vector Multiplication (SpMV) software package for real-world Processing-In-Memory (PIM) architectures. SparseP is developed to evaluate and characterize the first publicly-available real-world PIM architecture, the UPMEM PIM architecture. Described by C. Giannoula et al. [https://arxiv.org/abs/2201.05072] · GitHub","url":"https://github.com/CMU-SAFARI/SparseP"},{"title":"tensorflow/tensorflow/core/kernels/sparse_tensor_dense_matmul_op_gpu.cu.cc at master · tensorflow/tensorflow","url":"https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/kernels/sparse_tensor_dense_matmul_op_gpu.cu.cc"},{"title":"[FEATURE] PowerInfer Kernels with Sparse Transformers · Issue #54 · NimbleEdge/sparse_transformers","u
…[truncated 756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T02:57:42.215673+00:00_

Web search results for query: "Neural Magic sparse LLM inference weight activation sparsity"

Links: [{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity","url":"https://arxiv.org/pdf/2602.14452"},{"title":"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2512.12744"},{"title":"Sparsity in Large Language Models (LLMs) - Data Magic AI Blog","url":"https://datamagiclab.com/sparsity-in-large-language-models-llms/"},{"title":"Introducing Sparse Llama: 70% Smaller, 3x Faster, Full Accuracy - Cerebras","url":"https://www.cerebras.ai/blog/introducing-sparse-llama-70-smaller-3x-faster-full-accuracy"},{"title":"2:4 Sparse Llama: Smaller models for efficient GPU inference | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/02/28/24-sparse-llama-smaller-models-efficient-gpu-inference"},{"title":"WINA: Weight Informed Neuron Activation for Accelerating Large Language Model Inference","url":"https://arxiv.org/pdf/2505.19427"}]

Based on the web search results, here's information about Neural Magic's work on sparse LLM inference with weight and activation sparsity:

## Neural Magic's Sparse LLM Approach

Neural Magic is working on sparse LLMs—reducing the model size by removing unneeded connections while retaining accuracy. Their efforts focus on both weight and activation sparsity for efficient inference.

### DeepSparse Engine

Neural Magic's DeepSparse engine delivers exceptional inference performance on CPUs by leveraging advanced techniques such as Just-In-Time (JIT) compilation, kernel fusion, and vectorized instructions to optimize sparse operations. By exploiting sparsity patterns in LLMs, DeepSparse minimizes memory accesses and computational overhead, resulting in up to 3x faster inference compared 
…[truncated 673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T02:57:42.215817+00:00_

Web search results for query: "nm-vllm sparse inference vLLM integration"

Links: [{"title":"nm-vllm · PyPI","url":"https://pypi.org/project/nm-vllm/0.4.0/"},{"title":"Offline Inference Sparse — vLLM","url":"https://nm-vllm.readthedocs.io/en/0.4.0/getting_started/examples/offline_inference_sparse.html"},{"title":"Offline Inference Sparse - vLLM - Read the Docs","url":"https://nm-vllm.readthedocs.io/en/0.5.0/getting_started/examples/offline_inference_sparse.html"},{"title":"GitHub - neuralmagic/nm-vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub","url":"https://github.com/neuralmagic/nm-vllm"},{"title":"Enabling High-Sparsity Foundational Llama Models with Efficient   Pretraining and Deployment","url":"https://arxiv.org/pdf/2405.03594"},{"title":"[Feature]: Is it possible for VLLM to support inference with dynamic activation sparsity? · Issue #10259 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/10259"},{"title":"[RFC]: KVComp Sparse Attention for Long-Context Inference · Issue #5507 · vllm-project/vllm-ascend","url":"https://github.com/vllm-project/vllm-ascend/issues/5507"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"}]

Based on the search results, here's what I found about nm-vllm sparse inference and vLLM integration:

## Overview

nm-vllm is Neural Magic's opinionated focus on incorporating the latest LLM optimizations like quantization and sparsity for enhanced performance. vLLM is a fast and easy-to-use library for LLM inference that Neural Magic regularly contributes upstream improvements to.

## Sparse Inference Support

nm-vllm includes support for newly-developed sparse inference kernels, which provides both memory reduction and acceleration of sparse models leveraging sparsity. SparseGPT and Sparse Fine-tuning are the leading algorithms for pruning LLMs, which enables removing at least half of model weights with lim
…[truncated 586 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-19T02:57:42.215966+00:00_

Web search results for query: "DeepSparse activation sparsity dynamic per-token LLM"

Links: [{"title":"Activation Sparsity","url":"https://www.aussieai.com/research/activation-sparsity"},{"title":"Sparsity Optimizations in LLMs","url":"https://www.aussieai.com/research/sparse"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/html/2411.12692v1"},{"title":"Sparse Brains are Also Adaptive Brains: Cognitive-Load-Aware Dynamic   Activation for LLMs","url":"https://arxiv.org/pdf/2502.19078"},{"title":"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware   Masking","url":"https://arxiv.org/pdf/2412.01380"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"ENABLING HIGH-SPARSITY FOUNDATIONAL LLAMA MODELS","url":"https://openreview.net/pdf?id=MuRhZtBw0N"},{"title":"Enabling Dynamic Sparsity in Quantized LLM Inference","url":"https://arxiv.org/pdf/2511.04477"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated   Parameters","url":"https://arxiv.org/pdf/2406.05955"}]

Based on the search results, here's what I found about DeepSparse and activation sparsity for dynamic per-token LLM inference:

## DeepSparse Overview

DeepSparse is a sparsity-aware deep learning inference runtime for CPUs, developed by Neural Magic. The INT8 format for weights and activations is crucial for achieving maximal speedups with the DeepSparse engine, both for time-to-first token and time-per-output token.

## Activation Sparsity Concept

Activation sparsity is an LLM speed optimization based on setting low-value signals to zero during inference, so that they can be skipped. If an activation has a low magnitude value, whether positive or negative, then it has only a limited effect on the final result.

## Dynamic Per-Token Application

Activation sparsity refers to dynamic analysis of the "a
…[truncated 653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T02:57:42.216140+00:00_

Web search results for query: "vLLM sparse kernel inference activation sparsity"

Links: [{"title":"[Feature]: Is it possible for VLLM to support inference with dynamic activation sparsity? · Issue #10259 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/10259"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"[Kernel] Add CUTLASS sparse support, heuristics, and torch operators by Faraz9877 · Pull Request #10340 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/10340"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/pdf/2504.19449"},{"title":"2:4 Sparse Llama: Smaller models for efficient GPU inference | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/02/28/24-sparse-llama-smaller-models-efficient-gpu-inference"},{"title":"GitHub - CURRENTF/Sparse-vLLM: A sparse-first inference engine (sparsevllm). It also contains DeltaKV compressor training + evaluation tooling (deltakv). · GitHub","url":"https://github.com/CURRENTF/Sparse-vLLM"},{"title":"int4 Weight Quantization of a 2:4 Sparse Model - vLLM","url":"https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_2of4_sparse_w4a16/"}]

Based on the web search results, here's what I found about vLLM sparse kernel inference and activation sparsity:

## Activation Sparsity in vLLM

Language models exhibit activation sparsity during inference, meaning that they can perform lossless inference even when only a portion of the activation values are activated. By applying this process to inference, one can record the activated neurons during the prefill stage and then compute only the selected neurons during the decode stage, thereby accelerating inference.

## Sparse Kernel Support

vLLM implements NVIDIA CUTLASS 2:4 structured sparsity support for LLM inference, where this sparsification pat
…[truncated 778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T02:57:42.216292+00:00_

Web search results for query: "vLLM sparse inference plugins extensions"

Links: [{"title":"vLLM · GitHub","url":"https://github.com/vllm-project"},{"title":"Building Clean, Maintainable vLLM Modifications Using the Plugin System | vLLM Blog","url":"https://blog.vllm.ai/2025/11/20/vllm-plugin-system.html"},{"title":"GitHub - CURRENTF/Sparse-vLLM: A sparse-first inference engine (sparsevllm). It also contains DeltaKV compressor training + evaluation tooling (deltakv). · GitHub","url":"https://github.com/CURRENTF/Sparse-vLLM"},{"title":"[RFC]: Add SpargeAttn Sparse Attention Backend · Issue #765 · vllm-project/vllm-omni","url":"https://github.com/vllm-project/vllm-omni/issues/765"},{"title":"Welcome to vLLM — vLLM","url":"https://docs.vllm.ai/en/v0.7.3/index.html"},{"title":"DeepSeek-V3.2-Exp on vLLM, Day 0: Sparse Attention for long-context inference, ready for experimentation today with Red Hat AI | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/10/03/deepseek-v32-exp-vllm-day-0-sparse-attention-long-context-inference"},{"title":"vLLM Hook v0: A Plug-in for Programming Model Internals on vLLM","url":"https://arxiv.org/pdf/2603.06588"}]

Based on the search results, here's what I found about vLLM sparse inference plugins and extensions:

## vLLM Plugin System

vLLM has an official general_plugins entry point system that serves as a supported extension mechanism. The general plugin system can be leveraged for custom behavior as an alternative to forking or monkey-patching strategies.

## Sparse Inference Support

vLLM includes support for Sparse Attention, a two-stage process ("lightning indexer" + "fine-grained token selection") that enables efficient long-context inference. vLLM delivered Day 0 support for DeepSeek-V3.2-Exp, making it runnable on NVIDIA Hopper and Blackwell architectures.

## Related Tools and Extensions

The compressed-tensors project is a safetensors extension to efficiently store sparse quantized tensors on disk.

Additiona
…[truncated 474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T02:57:42.216447+00:00_

Web search results for query: "PowerInfer sparse GPU kernel activation sparsity LLM"

Links: [{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/html/2312.12456v2"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/pdf/2312.12456"},{"title":"[2312.12456] PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://ar5iv.labs.arxiv.org/html/2312.12456"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://arxiv.org/pdf/2505.14884"},{"title":"GitHub - Tiiny-AI/PowerInfer: High-speed Large Language Model Serving for Local Deployment · GitHub","url":"https://github.com/Tiiny-AI/PowerInfer"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models","url":"https://arxiv.org/html/2402.13516v1"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU | Proceedings of the ACM SIGOPS 30th Symposium on Operating Systems Principles","url":"https://dl.acm.org/doi/10.1145/3694715.3695964"},{"title":"GitHub - SJTU-IPADS/PowerInfer: High-speed Large Language Model Serving for Local Deployment","url":"https://github.com/SJTU-IPADS/PowerInfer"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/html/2411.12692v1"}]

Based on the search results, here's what I found about PowerInfer, sparse GPU kernels, activation sparsity, and LLMs:

## PowerInfer Overview

PowerInfer is a high-speed Large Language Model (LLM) inference engine on a personal computer (PC) equipped with a single consumer-grade GPU. The key principle underlying the design of PowerInfer is exploiting the high locality inherent in LLM inference, characterized by a power-law distribution in neuron activation, where a small subset of neurons, termed hot neurons, are consistently activated across inputs, while th
…[truncated 1235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T02:57:42.216600+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "CATS + Deja Vu + academic implementations",
  "subagent_type": "Explore",
  "prompt": "Research academic paper implementations for activation sparsity speedup in LLMs. Focus on these papers and their code:\n\n1. **CATS (Context-Aware Token Sparsity)**:\n   - GitHub: https://github.com/ScalingIntelligence/CATS\n   - How do they achieve wall-clock speedup from activation sparsity?\n   - What kernel do they use? Triton? Custom CUDA?\n   - What sparsity patterns does their code support?\n   - What speedups do they report?\n\n2. **Deja Vu** (Liu et al., \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\"):\n   - Search GitHub for their implementation\n   - How do they implement sparse FFN forward pass?\n   - What kernel technology do they use?\n\n3. **TEAL** (Training-free Efficient Activation pruning for LLMs):\n   - Search for their implementation\n   - How do they get speedup numbers?\n\n4. **Mixture-of-Depths / early-exit methods**:\n   - Any reusable sparse inference kernels from these?\n\n5. **Turbo Sparse** and similar recent papers:\n   - Search: \"turbo sparse llm\", \"sparse activation inference kernel\"\n   - Any 2024-2025 papers with good open-source sparse kernels?\n\n6. **Griffin / Sparse-Finetuned LLMs**:\n   - Search: \"griffin sparse llm kernel\", \"sparse finetuned llm inference\"\n\nFor each, report:\n- GitHub URL if available\n- Kernel technology (Triton/CUDA/cuSPARSE)\n- Sparsity type supported (unstructured activation sparsity?)\n- Reported speedups and at what sparsity levels\n- Code quality/reusability assessment\n\nBe very thorough — these are the most directly relevant to our use case."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Agent",
  "tool_args": {
    "description": "CATS + Deja Vu + academic implementations",
    "subagent_type": "Explore",
    "prompt": "Research academic paper implementations for activation sparsity speedup in LLMs. Focus on these papers and their code:\n\n1. **CATS (Context-Aware Token Sparsity)**:\n   - GitHub: https://github.com/ScalingIntelligence/CATS\n   - How do they achieve wall-clock speedup from activation sparsity?\n   - What kernel do they use? Triton? Custom CUDA?\n   - What sparsity patterns does their code support?\n   - What speedups do they report?\n\n2. **Deja Vu** (Liu et al., \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\"):\n   - Search GitHub for their implementation\n   - How do they implement sparse FFN forward pass?\n   - What kernel technology do they use?\n\n3. **TEAL** (Training-free Efficient Activation pruning for LLMs):\n   - Search for their implementation\n   - How do they get speedup numbers?\n\n4. **Mixture-of-Depths / early-exit methods**:\n   - Any reusable sparse inference kernels from these?\n\n5. **Turbo Sparse** and similar recent papers:\n   - Search: \"turbo sparse llm\", \"sparse activation inference kernel\"\n   - Any 2024-2025 papers with good open-source sparse kernels?\n\n6. **Griffin / Sparse-Finetuned LLMs**:\n   - Search: \"griffin sparse llm kernel\", \"sparse finetuned llm inference\"\n\nFor each, report:\n- GitHub URL if available\n- Kernel technology (Triton/CUDA/cuSPARSE)\n- Sparsity type supported (unstructured activation sparsity?)\n- Reported speedups and at what sparsity levels\n- Code quality/reusability assessment\n\nBe very thorough — these are the most directly relevant to our use case."
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T02:57:42.216786+00:00_

Web search results for query: "sparse neural network activation sparsity per-token mask dynamic inference"

Links: [{"title":"Activation Sparsity: Concepts, Methods, and Applications | by Ali Borji | Medium","url":"https://medium.com/@aliborji/activation-sparsity-concepts-methods-and-applications-b9b371588daa"},{"title":"Learning Neural Networks with Sparse Activations","url":"https://arxiv.org/html/2406.17989v1"},{"title":"Dynamic Regularization on Activation Sparsity for Neural Network Efficiency Improvement","url":"https://dl.acm.org/doi/fullHtml/10.1145/3447776"},{"title":"Sparse Weight Activation Training Md Aamir Raihan, Tor M. Aamodt","url":"https://proceedings.neurips.cc/paper/2020/file/b44182379bf9fae976e6ae5996e13cd8-Paper.pdf"},{"title":"Exploiting Activation Sparsity with Dense to Dynamic-k ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Learning Neural Networks with Sparse Activations","url":"https://arxiv.org/pdf/2406.17989"},{"title":"Inducing and Exploiting Activation Sparsity for Fast Neural Network Inference","url":"http://proceedings.mlr.press/v119/kurtz20a/kurtz20a.pdf"},{"title":"Dynamic Sparse Graph for Efficient Deep Learning","url":"https://arxiv.org/pdf/1810.00859"}]

I've completed the web search for your query. Here are the key findings:

## Overview of Sparse Neural Networks and Per-Token Activation Sparsity

Activation sparsity is dynamic — it varies per input, per layer, and per forward pass. The idea is that if most activations in a network are zero at any given time, we can skip the corresponding computations entirely, yielding significant speedups and memory savings without sacrificing accuracy.

## Per-Token Activation Sparsity in Language Models

Large language models exhibit substantial activation sparsity 
…[truncated 1078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-19T02:57:42.216960+00:00_

Web search results for query: "site:github.com CATS sparse FFN activation kernel ScalingIntelligence"

Links: [{"title":"GitHub - ScalingIntelligence/CATS","url":"https://github.com/ScalingIntelligence/CATS"},{"title":"GitHub - IntelLabs/SCAP: Statistical Calibrated Activation Pruning","url":"https://github.com/IntelLabs/SCAP"},{"title":"CATS: Contextually-Aware Thresholding for Sparsity in Large Language   Models","url":"https://arxiv.org/pdf/2404.08763"},{"title":"Spark Transformer: Reactivating Sparsity in FFN and Attention","url":"https://arxiv.org/pdf/2506.06644"},{"title":"To 2:4 Sparsity and Beyond: Neuron-level Activation Function to Accelerate LLM Pre-Training","url":"https://arxiv.org/pdf/2602.06183"},{"title":"Accelerating Transformer Inference and Training with 2:4 Activation   Sparsity","url":"https://arxiv.org/pdf/2503.16672"},{"title":"Universal Properties of Activation Sparsity in Modern Large Language Models","url":"https://arxiv.org/pdf/2509.00454"},{"title":"CHESS: Optimizing LLM Inference via Channel-Wise Thresholding and   Selective Sparsification","url":"https://arxiv.org/pdf/2409.01366"},{"title":"GitHub - wh-xu/sparse-ffn-llm: A sparse and retraining-free FFN/MoE inference algorithm for large language model (LLM)","url":"https://github.com/wh-xu/sparse-ffn-llm"}]

The search results returned information about CATS and related sparse FFN activation work. Here are the key findings:

## CATS Repository

The official implementation of CATS is for "Contextually-Aware Thresholding for Sparsity in Large Language Models." The paper has been accepted for presentation at COLM 2024.

## Key Features

The CATS approach can be applied to various base models such as Mistral-7B and Llama2-7B, demonstrating a minimal performance drop (within 1-2% of the base models) even at 50% activation sparsity levels.

CATS integrates a custom GPU kernel that enhances inference speeds by approximately 15%. The custom GPU kernel for efficient implementation of CATS transl
…[truncated 381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-19T02:57:42.217160+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "git log --oneline -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "git log --oneline -20"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-19T02:57:42.217292+00:00_

49bef00 [paper] Remove enlargethispage (P0 desk-reject fix) + sharpen abstract C1 delta
406f40a [paper] Fill C1 ablation downstream numbers: all 5 metrics match (max Δ=0.79pp)
13418e6 [paper] Upgrade C1 ablation to full-spectrum evidence (PPL + 4 downstream tasks)
b66e8c3 [paper] Fix C1 ablation numbers: use controlled eval (TEAL 50% uniform) not training eval
6abafc3 [paper] Reframe narrative: gradient coupling → mask pattern discovery with C1 causal ablation
01a67df [paper] Add MoE/GLU related work paragraph + mask pattern analysis framework
3c352a5 [paper] Round 8: cross-arch table to appendix, 14B scope fix, regime weakening, PPL/format fixes
ab23ee2 [paper] Upgrade 30% KL uniform row to 3-seed mean±std in Tables 2+5
86bf43a [paper] Compress content for 8-page compliance: regime details to appendix refs, Conclusion 3 sentences
25dc25f [paper] Expand Conclusion to 4 sentences, add 14B knowledge density discussion, simplify Limitations
180b1e4 [paper] Fix comp convergence appendix: replace inaccurate <5% with absolute loss units
0898abc [paper] Restore comp claim to both 30%+50%, 2-seed for 30%, add convergence appendix
8f3db37 [paper] Downgrade comp claim: 30%-only 2-seed, suspend 50% pending predictor verification
1910c3b [paper] D057 compensation redundancy upgrade: both 30% and 50% identical to KL-only
7231663 [paper] C1 compensation redundancy: KL+Comp no benefit at 30%, page budget fix
d123181 [paper] Update C4 OOD 30% to 2-seed mean±std (16.03±0.01), responding to W4
e8388f6 [paper] Fix 3 reviewer-audit issues: 14B +8.1pp→+5.0pp, intro sparsity context, SNR display precision
71aa753 [paper] Revert σ ratio to 7.5× + add TEAL determinism framing for 9.5pp variance
2e03aa8 [paper] Fix cross-seed σ ratio: 7.5× → 7.3× (9.5/1.3=7.31)
e7e8fc4 [paper] D055 checkpoint consistency: revert MMLU std to 9.5pp (westd-34887 source)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T02:57:42.217436+00:00_

Web search results for query: "SparseInfer activation sparsity fast inference code"

Links: [{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10992997/"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/html/2411.12692v2"},{"title":"[Literature Review] SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://www.themoonlight.io/en/review/sparseinfer-training-free-prediction-of-activation-sparsity-for-fast-llm-inference"},{"title":"(PDF) SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://www.researchgate.net/publication/385944711_SparseInfer_Training-free_Prediction_of_Activation_Sparsity_for_Fast_LLM_Inference"},{"title":"[2411.12692] SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/abs/2411.12692"}]

Based on the search results, here's what I found about SparseInfer:

## Overview

SparseInfer is a simple, lightweight, and training-free predictor for activation sparsity of ReLU-fied LLMs, in which activation sparsity is predicted by comparing only the sign bits of inputs and weights.

## Problem It Addresses

Modern LLMs employing SiLU as their activation function exhibit minimal activation sparsity, but recent research has proposed replacing SiLU with ReLU to induce significant activation sparsity with no downstream task accuracy degradation through fine-tuning.

## Key Technical Details

The method employs a comparison of the sign bits of the model's weights and the input vector during the forward pass. The prediction method requires only sign-bit information of the weight mat
…[truncated 627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T02:57:42.217591+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/ScalingIntelligence/CATS",
  "prompt": "Find GPU kernel code for sparse activation in Triton or CUDA, sparse FFN implementation, reported speedups"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/ScalingIntelligence/CATS",
    "prompt": "Find GPU kernel code for sparse activation in Triton or CUDA, sparse FFN implementation, reported speedups"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-19T02:57:42.217779+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/FMInference/DejaVu",
  "prompt": "Find Triton or CUDA sparse kernel implementation for activation sparsity, GPU acceleration code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/FMInference/DejaVu",
    "prompt": "Find Triton or CUDA sparse kernel implementation for activation sparsity, GPU acceleration code"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T02:57:42.217972+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/gpu-mode/triton-index/blob/main/kernels/0013_Sparse_Matmul.md",
  "prompt": "Sparse matmul Triton kernel implementation details, code snippets, types of sparsity supported"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/gpu-mode/triton-index/blob/main/kernels/0013_Sparse_Matmul.md",
    "prompt": "Sparse matmul Triton kernel implementation details, code snippets, types of sparsity supported"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-19T02:57:42.218151+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Raincleared-Song/sparse_gpu_operator",
  "prompt": "GPU operators for sparse tensor operations, ReLU-activated FFN code, kernel implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Raincleared-Song/sparse_gpu_operator",
    "prompt": "GPU operators for sparse tensor operations, ReLU-activated FFN code, kernel implementation"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T02:57:42.218288+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com PowerInfer sparse GPU kernel CUDA implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com PowerInfer sparse GPU kernel CUDA implementation"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T02:57:42.218423+00:00_

Web search results for query: "cuBLAS sparse GEMM Ampere structured sparsity 2:4"

Links: [{"title":"Accelerating Transformer Pre-training with 2:4 Sparsity","url":"https://arxiv.org/html/2404.01847v3"},{"title":"Exploiting NVIDIA Ampere Structured Sparsity with cuSPARSELt | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/exploiting-ampere-structured-sparsity-with-cusparselt/"},{"title":"cuSPARSE | NVIDIA Developer","url":"https://developer.nvidia.com/cusparse"},{"title":"Accelerating Sparse DNNs Based on Tiled GEMM","url":"https://arxiv.org/pdf/2402.10876"},{"title":"Sparse GEMM and Tensor Core’s Structured Sparsity | by Huan Xu | Medium","url":"https://medium.com/@hxu296/exploring-spgemm-and-nvidias-leap-in-deep-neural-network-efficiency-d367adc68791"},{"title":"Accelerating Matrix Multiplication with Block Sparse Format and NVIDIA Tensor Cores | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/accelerating-matrix-multiplication-with-block-sparse-format-and-nvidia-tensor-cores/"},{"title":"Hardware-Aware Sparse Pruning. some well-known hardware-supported… | by sandeep chowdhury | Medium","url":"https://medium.com/@sandeepiit.ism/accelerating-ai-with-pattern-based-pruning-understanding-n-m-sparsity-d696dddbdd66"},{"title":"Bridging the Gap between Unstructured SpMM and Structured Sparse Tensor Cores | Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis","url":"https://dl.acm.org/doi/10.1145/3712285.3759849"},{"title":"Accelerating Sparse Deep Neural Networks","url":"https://arxiv.org/pdf/2104.08378"},{"title":"Structured Sparsity in the NVIDIA Ampere Architecture and Applications in Search Engines | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/"}]

Based on the search results, here's what I found about cuBLAS sparse GEMM, Ampere, and 2:4 structured sparsity:

## 2:4 Struct
…[truncated 1168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-19T02:57:42.218578+00:00_

Web search results for query: "DeepSparse SwiGLU GatedMLP sparse inference"

Links: [{"title":"What is SwiGLU, and why is it common in modern LLM feed-forward layers? | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/faq/docs/swiglu-modern-llms.html"},{"title":"Dependency-Aware Semi-Structured Sparsity: Declining Roles of Outliers in Pruning GLU-based LLMs","url":"https://arxiv.org/html/2405.01943v2"},{"title":"Gated Multi-Layer Perceptron (Gated-MLP)","url":"https://www.intel.com/content/www/us/en/docs/onednn/developer-guide-reference/2025-1/gated-multi-layer-perceptron-gated-mlp.html"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/html/2406.05955"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"DeepSparse Inference Runtime | DigitalOcean Marketplace 1-Click App","url":"https://marketplace.digitalocean.com/apps/deepsparse-inference-runtime"},{"title":"Deep reinforcement learning with significant multiplications inference","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10682459/"},{"title":"Sparse Computations in Deep Learning Inference","url":"https://arxiv.org/html/2512.02550v1"},{"title":"Deep Kernel Fusion for Transformers","url":"https://arxiv.org/pdf/2602.11808"}]

Based on the search results, here's what I found about DeepSparse, SwiGLU, GatedMLP, and sparse inference:

## SwiGLU and GatedMLP Overview

SwiGLU is a gated feed-forward layer used in many modern LLMs. Swish activation is further adopted to replace Sigmoid in the GLU to form SwiGLU, and the Gated-MLP based on SwiGLU is also adopted in LLMs like LLaMA and Qwen.

## Sparse Inference Applications

Research has demonstrated the use of the DeepSparse inference engine for testing sparse model speedup, showing significant reductions in end-to-end decode latency for models like LLaMA2-7B. The speed was tested on an Intel
…[truncated 595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-19T02:57:42.218728+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CATS Context-Aware Token Sparsity GitHub ScalingIntelligence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CATS Context-Aware Token Sparsity GitHub ScalingIntelligence"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-19T02:57:42.218856+00:00_

# Block-Sparse Matrix Multiplication in Triton

This resource documents a Triton kernel implementation for sparse matrix operations. According to the GitHub page, it's "A collection of Triton kernels for block-sparse matrix multiplication."

## Key Details

**Source:** The implementation originates from Microsoft DeepSpeed's sparse attention module, adapted from Philippe Tillet's torch-blocksparse repository.

**Sparsity Patterns Supported:** The kernel handles three multiplication scenarios:
- **SDD**: Sparse result from dense × dense inputs
- **DSD**: Dense result from sparse × dense inputs  
- **DDS**: Dense result from dense × sparse inputs

**Requirements:** This implementation requires Triton v2.1.0 or later.

**Classification:** The kernel is tagged with sparsity and matrix multiplication operations, making it relevant for optimizing attention mechanisms and other sparse computational workloads common in deep learning.

This approach allows developers to leverage hardware acceleration for sparse operations while maintaining compatibility with dense tensor workflows.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-19T02:57:42.218996+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PowerInfer speedup performance benchmark activation sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PowerInfer speedup performance benchmark activation sparsity"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T02:57:42.219150+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Deja Vu contextual sparsity efficient LLMs inference GitHub Liu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Deja Vu contextual sparsity efficient LLMs inference GitHub Liu"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-19T02:57:42.219279+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TEAL training-free efficient activation pruning LLMs GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TEAL training-free efficient activation pruning LLMs GitHub"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T02:57:42.219400+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cuSPARSELt SpMM performance benchmark 30% 50% sparsity speedup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cuSPARSELt SpMM performance benchmark 30% 50% sparsity speedup"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-19T02:57:42.219521+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RelayAttention dynamic sparsity inference framework"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RelayAttention dynamic sparsity inference framework"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-19T02:57:42.219642+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PyTorch sparse matmul backward gradient activation sparsity training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PyTorch sparse matmul backward gradient activation sparsity training"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-19T02:57:42.219764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Turbo Sparse\" LLM sparse activation inference kernel 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Turbo Sparse\" LLM sparse activation inference kernel 2024"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T02:57:42.219884+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NVIDIA sparse tensor operations dense to sparse conversion overhead latency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NVIDIA sparse tensor operations dense to sparse conversion overhead latency"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-19T02:57:42.220004+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSparse CPU GPU weight sparsity format structured unstructured"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSparse CPU GPU weight sparsity format structured unstructured"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-19T02:57:42.220148+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"vLLM\" \"sparse kernel\" GPU inference implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"vLLM\" \"sparse kernel\" GPU inference implementation"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T02:57:42.220269+00:00_

# CATS: GPU Kernel and Sparse Implementation Analysis

Based on the GitHub repository content, here's what I found regarding your specific queries:

## GPU Kernel Code Location

The repository contains a **`flash_gemv` folder** that likely houses custom GPU kernel implementations. The documentation mentions: "CATS...integrates a custom GPU kernel that enhances inference speeds by approximately 15%."

However, the provided content doesn't reveal the specific kernel language (Triton vs. CUDA) or implementation details within that directory.

## Sparse FFN Implementation

The codebase includes several relevant files:
- `inference.py` - likely contains inference logic with sparse operations
- `create_models.py` - model creation infrastructure
- `experiments/` folder - experimental implementations

## Reported Performance Improvements

According to the README, the framework achieves:
- **~15% inference speedup** from the custom GPU kernel
- **50% activation sparsity** with only 1-2% performance degradation compared to baseline models (Mistral-7B, Llama2-7B)

## Repository Status

The project notes they are "currently developing a framework that will enable CATS to be easily integrated with any model from the HuggingFace library," suggesting the codebase is still evolving.

To access the actual kernel code and sparse FFN details, you would need to examine the `flash_gemv/` directory and related source files directly in the repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-19T02:57:42.220404+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"TwELL\" \"sparser faster llms\" activation sparsity CUDA kernel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"TwELL\" \"sparser faster llms\" activation sparsity CUDA kernel"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-19T02:57:42.220525+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "sparse activation inference dynamic mask per-token feedforward MLP optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "sparse activation inference dynamic mask per-token feedforward MLP optimization"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-19T02:57:42.220638+00:00_

# DejaVu Repository Analysis

Based on the GitHub page content provided, I cannot find any explicit mentions of **Triton or CUDA sparse kernel implementations** for activation sparsity or GPU acceleration code within this repository.

## What the Repository Actually Contains

DejaVu focuses on contextual sparsity for efficient LLM inference. The project includes:

1. **Sparsity Predictor Training** - Uses "low-cost algorithm to predict contextual sparsity on the fly" but implementation details aren't visible in this summary

2. **Accuracy Benchmarking** - Built on Decentralized_FM_alpha framework

3. **Generation Latency** - Described as a "pytorch based implementation that exploits cuda graph"

## GPU Implementation Details

The repository mentions using PyTorch with CUDA 11.3 and NCCL library support, but the specific sparse kernel implementations aren't documented in the README excerpt provided.

## Recommendation

To find the actual Triton or CUDA sparse kernel code, you would need to:
- Examine the `/Dejavu/benchmarks/` directory contents
- Review the sparse computation files in the repository
- Check the Dockerfile for build details that might reveal optimization libraries used

The page content doesn't provide sufficient detail about which sparse computation backend is actually implemented.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-19T02:57:42.220759+00:00_

# Summary of sparse_gpu_operator Repository

This GitHub project implements efficient GPU operators for sparse tensor operations, specifically designed for ReLU-activated feed-forward networks (FFNs) in large language models.

## Key Features

The repository contains two main operators:
- **ffn_23**: Handles step (2) - a fused ReLU operation with output-side sparsity
- **ffn_4**: Handles step (3) - sparse matrix-vector multiplication with input-side sparsity

## Performance Results

According to the documentation, the operators achieve notable speedups:
- "Step (2) speedup up to 2.00-2.44x and Step (3) speedup up to 1.49-1.70x" depending on model size and sparsity levels
- Better acceleration effects demonstrated on larger models (13B vs 7B)

## Technical Implementation

The code uses CUDA kernels with system-level optimizations including operator fusion, coalesced memory access, and vectorization. The default data type is bfloat16, though other types are supported.

## Installation & Configuration

Installation uses standard Python setup: `python setup.py install` or `pip install .`

The operators support configurable dimensions via macro variables in `kernel/formula_4_kernel.cu`, with preset values for LLaMA models.

## Related Research

This work is based on the paper "ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models" with trained model checkpoints available on Hugging Face.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-19T02:57:42.220893+00:00_

Web search results for query: "site:github.com PowerInfer sparse GPU kernel CUDA implementation"

Links: [{"title":"GitHub - Tiiny-AI/PowerInfer: High-speed Large Language Model Serving for Local Deployment · GitHub","url":"https://github.com/Tiiny-AI/PowerInfer"},{"title":"Sparse GPU Kernels for Deep Learning Trevor Gale Stanford University","url":"https://arxiv.org/pdf/2006.10901"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/pdf/2312.12456"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU | Proceedings of the ACM SIGOPS 30th Symposium on Operating Systems Principles","url":"https://dl.acm.org/doi/10.1145/3694715.3695964"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU + CPU · Issue #1802 · nomic-ai/gpt4all","url":"https://github.com/nomic-ai/gpt4all/issues/1802"},{"title":"GitHub - a-hamdi/GPU: 100 days of building GPU kernels! · GitHub","url":"https://github.com/a-hamdi/GPU"},{"title":"Fast Sparse Matrix-Vector Multiplication on GPUs: Implications for Graph   Mining","url":"https://arxiv.org/pdf/1103.2405"},{"title":"GitHub - google-research/sputnik: A library of GPU kernels for sparse matrix operations. · GitHub","url":"https://github.com/google-research/sputnik"},{"title":"GitHub - openai/blocksparse: Efficient GPU kernels for block-sparse matrix multiplication and convolution","url":"https://github.com/openai/blocksparse"}]

Based on the search results, here's what I found about PowerInfer's sparse GPU kernel and CUDA implementation:

## PowerInfer Overview

PowerInfer is a high-speed and easy-to-use inference engine for deploying LLMs locally. It utilizes sparse activation and 'hot'/'cold' neuron concept for efficient LLM inference, ensuring high speed with lower resource demands.

## Neuron-Aware Sparse Operators

Rather than using traditional sparse libraries, PowerInfer designs neuron-aware sparse operators that directly inte
…[truncated 948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-19T02:57:42.221098+00:00_

Web search results for query: "CATS Context-Aware Token Sparsity GitHub ScalingIntelligence"

Links: [{"title":"CATS: Context-Aware Thresholding for Sparsity in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=v3w2a7EInO"},{"title":"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models","url":"https://arxiv.org/html/2404.08763v3"},{"title":"CATS: Contextually-Aware Thresholding for Sparsity in ...","url":"https://zhang677.github.io/publications/cats2024.pdf"},{"title":"GitHub - ScalingIntelligence/CATS","url":"https://github.com/ScalingIntelligence/CATS"},{"title":"CATS: Context-Aware Thresholding for LLM Sparsity","url":"https://www.emergentmind.com/papers/2404.08763"},{"title":"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models | Scaling Intelligence Lab at Stanford University","url":"https://scalingintelligence.stanford.edu/blogs/cats/"},{"title":"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/cats-contextually-aware-thresholding-sparsity-large-language"},{"title":"Published as a conference paper at COLM 2024","url":"https://arxiv.org/pdf/2404.08763"},{"title":"[2404.08763] CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models","url":"https://arxiv.org/abs/2404.08763"}]

Based on the search results, here's what I found about CATS (Context-Aware Token Sparsity):

## Overview

CATS is the official implementation of Contextually-Aware Thresholding for Sparsity in Large Language Models. It's a framework for sparsifying the activations of base LLMs and reducing inference costs.

## Key Features

This method centers around a novel activation function that enhances activation sparsity effectively and efficiently. The CATS approach can be applied to various base models such as Mistral-7B and Llama2-7B, demonstrating a minimal performance drop (within 1-2% of the base models) e
…[truncated 641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-19T02:57:42.221258+00:00_

Web search results for query: "TEAL training-free efficient activation pruning LLMs GitHub"

Links: [{"title":"TEAL: Training-Free Activation Sparsity in Large Language Models","url":"https://www.together.ai/blog/teal-training-free-activation-sparsity-in-large-language-models"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2408.14690v1"},{"title":"GitHub - FasterDecoding/TEAL","url":"https://github.com/FasterDecoding/TEAL"},{"title":"SEAP: Training-free Sparse Expert Activation Pruning Unlock the Brainpower of Large Language Models","url":"https://arxiv.org/html/2503.07605v1"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/pdf/2408.14690"},{"title":"Training-Free Activation Sparsity in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=dGVZwyq5tV"},{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"},{"title":"DuoGPT: Training-free Dual Sparsity through Activation-aware Pruning in LLMs","url":"https://arxiv.org/html/2506.20194"}]

Based on the search results, here's what I found about TEAL:

## Overview

TEAL (Training-Free Activation Sparsity in LLMs) is a simple training-free method that applies magnitude-based activation sparsity to hidden states throughout the entire model.

## Key Performance Results

TEAL achieves 40-50% model-wide sparsity with minimal performance degradation across Llama-2, Llama-3, and Mistral families, with sizes varying from 7B to 70B. The method demonstrates wall-clock decoding speed-ups of up to 1.53× and 1.8× at 40% and 50% model-wide sparsity. Additionally, TEAL is compatible with weight quantization, enabling further efficiency gains.

## How It Works

During decoding, TEAL thresholds low-magnitude activation entries to zero, which obviates the need to move the associated weight channels 
…[truncated 421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-19T02:57:42.221409+00:00_

Web search results for query: "PowerInfer speedup performance benchmark activation sparsity"

Links: [{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU∗","url":"https://ipads.se.sjtu.edu.cn/_media/publications/powerinfer-20231219.pdf"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU | Request PDF","url":"https://www.researchgate.net/publication/385860215_PowerInfer_Fast_Large_Language_Model_Serving_with_a_Consumer-grade_GPU"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://ipads.se.sjtu.edu.cn/_media/publications/song-sosp24.pdf"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/html/2312.12456"},{"title":"Performance Evaluation of PowerInfer‑2: Offloading, Prefill, and In‑Memory Efficiency | MEXC News","url":"https://www.mexc.com/news/153016"},{"title":"GitHub - amir2pl/PowerInfer2: High-speed Large Language Model Serving on PCs with Consumer-grade GPUs · GitHub","url":"https://github.com/amir2pl/PowerInfer2"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/pdf/2406.05955"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/pdf/2312.12456"}]

Based on the search results, here's what I found about PowerInfer's speedup performance and its relationship with activation sparsity:

## Performance Benchmarks

PowerInfer attains an average token generation rate of 13.20 tokens/s, with a peak of 29.08 tokens/s, across various LLMs (including OPT-175B) on a single NVIDIA RTX 4090 GPU. This significantly outperforms llama.cpp by up to 11.69×. Additionally, PowerInfer-2 achieves up to 29× speedups over llama.cpp and 13× over LLMFlash.

For longer input sequences, PowerInfer still achieves a 3.47× to 5.69× speedup.

## Activation Sparsity's Role

The performance benefits are directly 
…[truncated 1019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-19T02:57:42.221556+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Tiiny-AI/PowerInfer",
  "prompt": "Find CUDA or Triton GPU kernel code for sparse operators, neuron-aware sparse activation kernels, kernel source files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Tiiny-AI/PowerInfer",
    "prompt": "Find CUDA or Triton GPU kernel code for sparse operators, neuron-aware sparse activation kernels, kernel source files"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-19T02:57:42.221688+00:00_

Web search results for query: "Deja Vu contextual sparsity efficient LLMs inference GitHub Liu"

Links: [{"title":"[2310.17157v1] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/abs/2310.17157v1"},{"title":"[2310.17157] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/abs/2310.17157"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://proceedings.mlr.press/v202/liu23am.html"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time | OpenReview","url":"https://openreview.net/forum?id=wIPIhHd00i"},{"title":"Papers with Code - Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://paperswithcode.com/paper/deja-vu-contextual-sparsity-for-efficient"},{"title":"GitHub - FMInference/DejaVu · GitHub","url":"https://github.com/FMInference/DejaVu"},{"title":"[PDF] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deja-Vu:-Contextual-Sparsity-for-Efficient-LLMs-at-Liu-Wang/95240dda409e28acccdc5cf619ad0c036cf4292d"},{"title":"Deja Vu: contextual sparsity for efficient LLMs at inference ...","url":"https://dl.acm.org/doi/10.5555/3618408.3619327"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMS at Inference Time","url":"https://minjiazhang.github.io/courses/sp24-resource/DejaVu-pre.pdf"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"}]

Based on the search results, I found comprehensive information about the "Deja Vu" paper on contextual sparsity for efficient LLM inference:

## Overview

"Deja Vu" demonstrates that contextual sparsity exists, that it can be accurately predicted, and that it can be exploited to speed up LLM inference in wall-clock time without compromising LLM's quality or in-context learning ability.

## The Approach

DejaVu is a s
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-19T02:57:42.221842+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/XunhaoLai/native-sparse-attention-triton",
  "prompt": "Triton sparse attention kernel implementation, code snippets, sparsity patterns supported"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/XunhaoLai/native-sparse-attention-triton",
    "prompt": "Triton sparse attention kernel implementation, code snippets, sparsity patterns supported"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-19T02:57:42.221982+00:00_

Web search results for query: "DeepSparse CPU GPU weight sparsity format structured unstructured"

Links: [{"title":"SparseRT: Accelerating Unstructured Sparsity on GPUs for Deep Learning Inference","url":"https://dspace.mit.edu/handle/1721.1/146100"},{"title":"SparseRT: Accelerating Unstructured Sparsity on GPUs for Deep Learning Inference | DeepAI","url":"https://deepai.org/publication/sparsert-accelerating-unstructured-sparsity-on-gpus-for-deep-learning-inference"},{"title":"SparseRT: Accelerating Unstructured Sparsity on GPUs for Deep Learning Inference","url":"https://www.researchgate.net/publication/343931705_SparseRT_Accelerating_Unstructured_Sparsity_on_GPUs_for_Deep_Learning_Inference"},{"title":"When deep learning models on GPU can be accelerated by taking advantage   of unstructured sparsity","url":"https://arxiv.org/pdf/2011.06295"},{"title":"Speeding up deep learning inference via unstructured sparsity | Towards Data Science","url":"https://towardsdatascience.com/speeding-up-deep-learning-inference-via-unstructured-sparsity-c87e3137cebc/"},{"title":"Enabling Unstructured Sparse Acceleration on Structured Sparse Accelerators","url":"https://arxiv.org/pdf/2403.07953"},{"title":"Accelerating Sparse Deep Neural Networks","url":"https://arxiv.org/pdf/2104.08378"},{"title":"Accelerating Inference with Sparsity Using the NVIDIA Ampere Architecture and NVIDIA TensorRT | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/"}]

Based on the search results, I found relevant information about weight sparsity formats (structured and unstructured) in deep learning acceleration on CPUs and GPUs, though the results focus more broadly on sparsity acceleration rather than specifically on "DeepSparse" as a product.

## Key Findings:

**Structured vs. Unstructured Sparsity:**

There are two main types of pruning: structural (based on removing whole weight kernels) and non-structural (removing indivi
…[truncated 1261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-19T02:57:42.222155+00:00_

Web search results for query: ""vLLM" "sparse kernel" GPU inference implementation"

Links: [{"title":"How to Choose the Right GPU for vLLM Inference | DigitalOcean","url":"https://www.digitalocean.com/community/conceptual-articles/vllm-gpu-sizing-configuration-guide"},{"title":"GitHub - CURRENTF/Sparse-vLLM: A sparse-first inference engine (sparsevllm). It also contains DeltaKV compressor training + evaluation tooling (deltakv). · GitHub","url":"https://github.com/CURRENTF/Sparse-vLLM"},{"title":"GitHub - vllm-project/vllm-xpu-kernels: The vLLM XPU kernels for Intel GPU · GitHub","url":"https://github.com/vllm-project/vllm-xpu-kernels"},{"title":"[RFC]: Sparse attention KV cache offloading to support longer sequence length · Issue #33980 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/33980"},{"title":"2:4 Sparse Llama: Smaller models for efficient GPU inference | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/02/28/24-sparse-llama-smaller-models-efficient-gpu-inference"},{"title":"Profiling vLLM Inference Server with GPU acceleration on RHEL | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/10/16/profiling-vllm-inference-server-gpu-acceleration-rhel"},{"title":"DeepSeek-V3.2-Exp on vLLM, Day 0: Sparse Attention for long-context inference, ready for experimentation today with Red Hat AI | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/10/03/deepseek-v32-exp-vllm-day-0-sparse-attention-long-context-inference"},{"title":"vTensor: Flexible Virtual Tensor Management for Efficient LLM Serving","url":"https://arxiv.org/pdf/2407.15309"}]

Based on the search results, here's what I found about vLLM and sparse kernel GPU inference implementation:

## Sparse Attention and KV Cache Optimization

In long sequence inference scenarios, KV cache size has become one of the inference bottlenecks. vLLM has been developing approaches to address this, including a layerwise KV cache offloading a
…[truncated 984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-19T02:57:42.222370+00:00_

Web search results for query: "PyTorch sparse matmul backward gradient activation sparsity training"

Links: [{"title":"Accelerate activation sparsity with activation compression · Issue #1920 · pytorch/ao","url":"https://github.com/pytorch/ao/issues/1920"},{"title":"`out = gather(x @ x, sparse_grad=True); out.sum().backward()` fails as `matmul` does not work with sparse gradients for dense inputs. · Issue #77532 · pytorch/pytorch","url":"https://github.com/pytorch/pytorch/issues/77532"},{"title":"torchsparsegradutils · PyPI","url":"https://pypi.org/project/torchsparsegradutils/"},{"title":"Sparse tensor use cases · Issue #10043 · pytorch/pytorch","url":"https://github.com/pytorch/pytorch/issues/10043"},{"title":"Exploiting Activation based Gradient Output Sparsity to Accelerate   Backpropagation in CNNs","url":"https://arxiv.org/pdf/2109.07710"},{"title":"SparseTrain: Exploiting Dataflow Sparsity for Efficient Convolutional   Neural Networks Training","url":"https://arxiv.org/pdf/2007.13595"},{"title":"Structurally Sparsified Backward Propagation for Faster Long Short-Term   Memory Training","url":"https://arxiv.org/pdf/1806.00512"}]

Based on the search results, here's what I found regarding PyTorch sparse matmul, backward gradients, activation sparsity, and training:

## Key Findings

**Sparse Matrix Multiplication in PyTorch:**
PyTorch has limitations with sparse gradients, as matmul does not work with sparse gradients for dense inputs, which is a known issue in the PyTorch autograd system.

**Activation Sparsity and Training:**
PyTorch accelerates sparse activation x dense weight matmul with 2:4 sparsity, but the backwards pass requires special handling to maintain accuracy. A training recipe for 2:4 activation sparsity achieves high levels of activation sparsity (>85%) during training.

**Backward Pass Sparsity:**
Neuron gradients can be sparse, and several prior works have sought to exploit gradient sparsity in the backward pass of training. Stochastic prunin
…[truncated 692 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-19T02:57:42.222541+00:00_

Web search results for query: ""Turbo Sparse" LLM sparse activation inference kernel 2024"

Links: [{"title":"[2406.05955v2] Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/abs/2406.05955v2"},{"title":"[2406.05955] Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/abs/2406.05955"},{"title":"(PDF) Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://www.researchgate.net/publication/381307349_Turbo_Sparse_Achieving_LLM_SOTA_Performance_with_Minimal_Activated_Parameters"},{"title":"Accelerating LLM Inference Using Sparsity Kira Selby, Varun Khare NimbleEdge","url":"https://www.nimbleedge.com/sparsity-white-paper.pdf"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://bestofai.com/article/turbo-sparse-achieving-llm-sota-performance-with-minimal-activated-parameters"},{"title":"[Literature Review] Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://www.themoonlight.io/en/review/turbo-sparse-achieving-llm-sota-performance-with-minimal-activated-parameters"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/html/2406.05955v1"}]

Based on the search results, here's what I found about Turbo Sparse:

## Overview

Turbo Sparse is a method for exploiting activation sparsity to significantly accelerate the inference process of large language models (LLMs) without compromising performance.

## Key Technical Approach

The method proposes a novel dReLU function designed to improve LLM activation sparsity, along with a high-quality training data mixture ratio to facilitate effective sparsification. Additionally, the researchers leverage sparse activation patterns within the Feed-Forward Network (FFN) experts of Mixture-of-Experts (MoE) models to further boost efficiency.

…[truncated 906 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-19T02:57:42.222696+00:00_

Web search results for query: "NVIDIA sparse tensor operations dense to sparse conversion overhead latency"

Links: [{"title":"Accelerating Neural Network Training with Semi-Structured (2:4) Sparsity – PyTorch","url":"https://pytorch.org/blog/accelerating-neural-network-training/"},{"title":"Simplify Sparse Deep Learning with Universal Sparse Tensor in nvmath-python | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/simplify-sparse-deep-learning-with-universal-sparse-tensor-in-nvmath-python/"},{"title":"Sparse GEMM and Tensor Core’s Structured Sparsity | by Huan Xu | Medium","url":"https://medium.com/@hxu296/exploring-spgemm-and-nvidias-leap-in-deep-neural-network-efficiency-d367adc68791"},{"title":"Accelerating Inference with Sparsity Using the NVIDIA Ampere Architecture and NVIDIA TensorRT | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/"},{"title":"Sparsity in INT8: Training Workflow and Best Practices for NVIDIA TensorRT Acceleration | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/sparsity-in-int8-training-workflow-and-best-practices-for-tensorrt-acceleration/"},{"title":"A Unified Optimization Approach for Sparse Tensor Operations on GPUs","url":"https://arxiv.org/pdf/1705.09905"},{"title":"Efficient Quantized Sparse Matrix Operations on Tensor Cores","url":"https://arxiv.org/pdf/2209.06979"},{"title":"Fused3S: Fast Sparse Attention on Tensor Cores Zitong Li","url":"https://hpcrl.github.io/ICS2025-webpage/program/Proceedings_ICS25/ics25-70.pdf"}]

Based on the search results, here's what I found about NVIDIA sparse tensor operations and dense-to-sparse conversion:

## Key Findings

**Conversion Overhead Challenges:**
Simply setting weights to zero isn't enough, as the dense tensor still contains these pruned elements and dense matrix multiplication kernels will continue to process them, incurring the same latency and memory overhead.

**Addressing t
…[truncated 1318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-19T02:57:42.222871+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/zhengqigao/hbsattn",
  "prompt": "High-performance block sparse attention Triton kernel, implementation details, speedups"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/zhengqigao/hbsattn",
    "prompt": "High-performance block sparse attention Triton kernel, implementation details, speedups"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-19T02:57:42.223090+00:00_

Web search results for query: ""TwELL" "sparser faster llms" activation sparsity CUDA kernel"

Links: [{"title":"Faster LLMs by Reshaping Sparsity | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/technology/2026/faster-llms-by-reshaping-sparsity"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://pub.sakana.ai/sparser-faster-llms/"},{"title":"Sakana AI and NVIDIA Introduce TwELL: 20.5% Faster LLM Inference via Unstructured Sparsity • Dev|Journal","url":"https://earezki.com/ai-news/2026-05-11-sakana-ai-and-nvidia-introduce-twell-with-cuda-kernels-for-205-inference-and-219-training-speedup-in-llms/"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/html/2603.23198"},{"title":"GitHub - SakanaAI/sparser-faster-llms: Cuda kernels for leveraging LLM sparsity to improve throughput and decrease the memory requirements during inference and training. · GitHub","url":"https://github.com/SakanaAI/sparser-faster-llms"},{"title":"Sakana AI and NVIDIA Introduce TwELL with CUDA Kernels for 20.5% Inference and 21.9% Training Speedup in LLMs - MarkTechPost","url":"https://www.marktechpost.com/2026/05/11/sakana-ai-and-nvidia-introduce-twell-with-cuda-kernels-for-20-5-inference-and-21-9-training-speedup-in-llms/"},{"title":"Sakana AI and NVIDIA Introduce TwELL with CUDA Kernels for 20.5% Inference and 21.9% Training Speedup in LLMs - Cryptopond","url":"https://cryptopond.com/sakana-ai-and-nvidia-introduce-twell-with-cuda-kernels-for-20-5-inference-and-21-9-training-speedup-in-llms/"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://sakana.ai/twell/"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/html/2411.12692v1"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/pdf/2603.23198"}]

Based on the search results, I found comprehensive information about TwELL and the rela
…[truncated 1557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-19T02:57:42.223266+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com \"block sparse\" OR \"sparse matmul\" triton inference activation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com \"block sparse\" OR \"sparse matmul\" triton inference activation"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-19T02:57:42.223408+00:00_

Web search results for query: "cuSPARSELt SpMM performance benchmark 30% 50% sparsity speedup"

Links: [{"title":"cuSPARSE | NVIDIA Developer","url":"https://developer.nvidia.com/cusparse"},{"title":"EFFICIENT GPU KERNELS FOR N:M-SPARSE WEIGHTS IN DEEP LEARNING","url":"https://proceedings.mlsys.org/paper_files/paper/2023/file/a10deb4d5227a8ea307ea8ff3cb712f4-Paper-mlsys2023.pdf"},{"title":"Accelerating Matrix Multiplication with Block Sparse Format and NVIDIA Tensor Cores | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/accelerating-matrix-multiplication-with-block-sparse-format-and-nvidia-tensor-cores/"},{"title":"GitHub - bcacdwk/vllmbench: End to end benchmark using Slidesparse GEMM kernels · GitHub","url":"https://github.com/bcacdwk/vllmbench"},{"title":"Exploiting NVIDIA Ampere Structured Sparsity with cuSPARSELt | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/exploiting-ampere-structured-sparsity-with-cusparselt/"},{"title":"cuSPARSELt: A High-Performance CUDA Library for Sparse Matrix-Matrix Multiplication — NVIDIA cuSPARSELt","url":"https://docs.nvidia.com/cuda/cusparselt/index.html"},{"title":"cuSPARSE SpMV/SpMM performance and upperbound: Nvidia Pascal P100 GPU... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/cuSPARSE-SpMV-SpMM-performance-and-upperbound-Nvidia-Pascal-P100-GPU-Fig-1-displays_fig1_325706323"},{"title":"Acc-SpMM: Accelerating General-purpose Sparse Matrix-Matrix Multiplication with GPU Tensor Cores","url":"https://arxiv.org/html/2501.09251v1"},{"title":"High Performance Unstructured SpMM Computation Using Tensor Cores","url":"https://arxiv.org/pdf/2408.11551"},{"title":"[2501.09251] Acc-SpMM: Accelerating General-purpose Sparse Matrix-Matrix Multiplication with GPU Tensor Cores","url":"https://arxiv.org/abs/2501.09251"}]

Based on the search results, here's what I found regarding cuSPARSELt SpMM performance benchmarks:

## Key Performance Findings

cuSPARSELt is a high-performanc
…[truncated 1089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-19T02:57:42.223567+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "triton-lang examples sparse operations matrix multiplication tutorials"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "triton-lang examples sparse operations matrix multiplication tutorials"
  }
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-19T02:57:42.223696+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Griffin sparse LLM kernel inference GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Griffin sparse LLM kernel inference GitHub"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-19T02:57:42.223822+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mixture-of-Depths early exit sparse inference kernel GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mixture-of-Depths early exit sparse inference kernel GitHub"
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-19T02:57:42.223946+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "sparse activation inference kernel LLM CUDA Triton 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "sparse activation inference kernel LLM CUDA Triton 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-19T02:57:42.224091+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"activation sparsity\" LLM kernel implementation cuSPARSE unstructured"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"activation sparsity\" LLM kernel implementation cuSPARSE unstructured"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-19T02:57:42.224226+00:00_

Web search results for query: "RelayAttention dynamic sparsity inference framework"

Links: [{"title":"RelayAttention for Efficient Large Language Model Serving with Long System Prompts | Request PDF","url":"https://www.researchgate.net/publication/384215185_RelayAttention_for_Efficient_Large_Language_Model_Serving_with_Long_System_Prompts"},{"title":"Sparsity Forcing: Reinforcing Token Sparsity of MLLMs","url":"https://arxiv.org/html/2504.18579"},{"title":"RRAttention: Dynamic Block Sparse Attention via Per-Head Round-Robin Shifts for Long-Context Inference","url":"https://arxiv.org/pdf/2602.05853"},{"title":"Dynamic Convolutions: Exploiting Spatial Sparsity for Faster Inference","url":"https://arxiv.org/pdf/1912.03203"},{"title":"SparseTrain:Leveraging Dynamic Sparsity in Training DNNs on   General-Purpose SIMD Processors","url":"https://arxiv.org/pdf/1911.10175"}]

Based on the search results, I found some relevant information, though the results primarily show related work on dynamic sparsity for attention mechanisms rather than specific details about "RelayAttention" as a distinct framework.

From the search results, I can see that there are several dynamic sparsity inference frameworks for large language models mentioned:

1. Twilight, a framework to bring adaptive sparsity to any existing sparse attention algorithm without sacrificing their accuracy, which can adaptively prune at most 98% of redundant tokens.

2. Dynamic methods that adaptively determine sparse patterns based on input characteristics, such as Minference and MMinference which determined the optimal pattern for each attention head and dynamically built sparse indices based on the assigned pattern during inference.

3. RRAttention, which maintains query independence while enabling efficient global pattern discovery with stride-level aggregation, reducing complexity from O(L²) to O(L²/S²) and employing adaptive Top-τ selection for optimal sparsity.

However, the search results don't contain speci
…[truncated 378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-19T02:57:42.224373+00:00_

# PowerInfer: GPU Kernel Code Analysis

Based on the GitHub repository documentation, PowerInfer contains **CUDA kernel implementations** for sparse operators, though the specific source files aren't extensively detailed in this README.

## Key Kernel-Related Files:

**CUDA Implementation:**
- `ggml-cuda.cu` - Main CUDA backend implementation
- `ggml-cuda.h` - CUDA header definitions

**Supporting Infrastructure:**
- `ggml-backend.c/h` - Backend abstraction layer
- `ggml-quants.c/h` - Quantization operations

## Sparse Operator Support:

The system implements "neuron-aware sparse operators" as part of its core design. According to the documentation, PowerInfer exploits "high locality inherent in LLM inference, characterized by a power-law distribution in neuron activation."

The architecture distinguishes between:
- **Hot neurons** (preloaded on GPU for fast access)
- **Cold neurons** (computed on CPU)

## Build Configuration:

To access CUDA kernels, users compile with:
```
cmake -S . -B build -DLLAMA_CUBLAS=ON
```

**Note:** The repository primarily focuses on the inference engine's overall architecture rather than exposing detailed kernel documentation. For specific sparse kernel implementations, examining `ggml-cuda.cu` directly in the source code would be necessary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-19T02:57:42.224512+00:00_

Web search results for query: "sparse activation inference dynamic mask per-token feedforward MLP optimization"

Links: [{"title":"Exploiting Activation Sparsity with Dense to Dynamic-k   Mixture-of-Experts Conversion","url":"https://arxiv.org/pdf/2310.04361"},{"title":"Accelerating LLM Inference Using Sparsity Kira Selby, Varun Khare NimbleEdge","url":"https://www.nimbleedge.com/sparsity-white-paper.pdf"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"CoreInfer: Accelerating Large Language Model Inference with   Semantics-Inspired Adaptive Sparse Activation","url":"https://arxiv.org/pdf/2410.18311"},{"title":"Token-Sparsification Strategy","url":"https://www.emergentmind.com/topics/token-sparsification-strategy"},{"title":"Trainable Dynamic Mask Sparse Attention","url":"https://arxiv.org/html/2508.02124v1"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated   Parameters","url":"https://arxiv.org/pdf/2406.05955"}]

I found several relevant research papers and resources on sparse activation inference with dynamic masking for feedforward networks. Here are the key findings:

## Dynamic Sparse Activation Methods

Dynamic activation sparse inference is based on the observation that activation of individual tokens in large language models is often highly sparse, and during the decoding stage, it activates only a small number of neurons for each token, effectively accelerating model inference.

CoreInfer introduces an MLP-free adaptive sparse activation inference method based on sentence-level prediction, proposing the concept of sentence-wise core neurons which refers to the subset of neurons most critical for a given sentence.

## Per-Token Feedforward Network Optimization

One approach is to exploit variation in activations through a dynamic-k routing procedure that adapts the number of experts allocated to a sample. Existing methods predict 
…[truncated 887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-19T02:57:42.224657+00:00_

# Native Sparse Attention Triton Implementation

This GitHub repository provides an efficient implementation of Native Sparse Attention using Triton, based on the research paper "Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention."

## Key Features

The project supports both training and inference for variable-length Native Sparse Attention, including prefilling, decoding, and KV cache management. A toy LLaMA model (`ToyNSALlama`) is provided with both forward and generate functions.

## Core Components

**Operations available include:**
- `linear_compress`: Key-value compression using learnable projections
- `compressed_attention`: Attention over compressed representations
- `topk_sparse_attention`: Top-k sparse attention mechanism

**The implementation provides:**
- PyTorch reference implementations for debugging
- Optimized Triton kernels for production use
- Module-level abstractions for easy model integration
- Simplified LLaMA model variants featuring self-attention and sparse attention

## Performance

Benchmarks on NVIDIA A100/H100 GPUs show significant speedups. For example, with 131K sequence length and block size 64, the Triton top-8 sparse attention achieves approximately **37x faster forward pass** compared to standard Flash Attention on A100 GPUs.

## Technical Requirements

- PyTorch ≥ 2.1.0
- Triton ≥ 3.0.0
- Attention head dimension < 128
- CUDA-capable GPU

The project uses the varlen approach similar to Flash Attention, requiring concatenated batch inputs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-19T02:57:42.224801+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSparse inference engine sparsity format support CPU optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSparse inference engine sparsity format support CPU optimization"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-19T02:57:42.224940+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"PowerInfer\" sparse operator implementation GPU kernel source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"PowerInfer\" sparse operator implementation GPU kernel source"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-19T02:57:42.225088+00:00_

# HBSAttention: High-Performance Block Sparse Attention Kernel

## Overview
This GitHub repository provides a "high-performance **Block Sparse Attention** kernel for PyTorch, implemented with **Triton**" for GPU acceleration. The kernel enables efficient processing of long sequences by restricting attention computation to user-specified query and key blocks.

## Key Features

**Flexibility and Compatibility:**
- Supports heterogeneous block sizes (allowing `q_block_size != k_block_size`)
- Handles variable-length inputs with differing sequence lengths
- Compatible with group query attention where `nhead_q % nhead_k == 0`
- Supports both causal and non-causal attention modes

**Current Limitations:**
- Forward pass only (no backward/gradient support yet)
- Block sizes must be integer multiples of 16

## Performance Benchmarks

Testing on an Nvidia H200 shows the Triton implementation performs comparably to existing CUDA implementations. The repository includes comparisons against:
- FlashAttention v2.7.4
- PyTorch's FlexAttention
- Han Lab's block sparse attention (CUDA)

Results demonstrate competitive performance across varying sparsity ratios (0.7-0.9) and sequence lengths (128 to ~64K tokens).

## Installation & Usage

Installation requires PyTorch and Triton, followed by cloning and installing the repository as an editable package. The API is straightforward—users provide query, key, value tensors along with a custom `block_mask` parameter defining sparse attention patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-19T02:57:42.225241+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "sparse LLM inference frameworks comparison 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "sparse LLM inference frameworks comparison 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-19T02:57:42.225373+00:00_

Web search results for query: "triton-lang examples sparse operations matrix multiplication tutorials"

Links: [{"title":"How to implement SDD Sparse Matrix Multiplication with high sparsity (96% ) but low block-level sparsity 13% · triton-lang/triton · Discussion #1766","url":"https://github.com/triton-lang/triton/discussions/1766"},{"title":"Tutorials — Triton documentation","url":"https://triton-lang.org/main/getting-started/tutorials/index.html"},{"title":"triton/python/tutorials/03-matrix-multiplication.py at main · triton-lang/triton","url":"https://github.com/triton-lang/triton/blob/main/python/tutorials/03-matrix-multiplication.py"},{"title":"Matrix Multiplication — Triton documentation","url":"https://triton-lang.org/main/getting-started/tutorials/03-matrix-multiplication.html"},{"title":"CoCalc -- 03-matrix-multiplication.py","url":"https://cocalc.com/github/Shrek/triton/blob/master/python/tutorials/03-matrix-multiplication.py"},{"title":"Triton Tutorial #2 | by Sherlock | Medium","url":"https://medium.com/@sherlockliao01/triton-tutorial-2-5de66cd2170d"},{"title":"Triton Tutorial #2 - sherlock","url":"https://sherlock.micro.blog/2024/04/17/triton-tutorial.html"},{"title":"Sparse matrix multiplication in associative memory device","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10489480"},{"title":"Sparse matrix multiplication in hardware","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12189710"},{"title":"Techniques for accelerating matrix multiplication computations using hierarchical representations of sparse matrices","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12141229"}]

Based on the search results, here's what I found about Triton language examples for sparse operations and matrix multiplication tutorials:

## Official Tutorials

Triton offers a gallery of tutorials for writing various basic operations, and it is recommended that you read through the tutorials in order, sta
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-19T02:57:42.225520+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://docs.pytorch.org/tutorials/advanced/semi_structured_sparse.html",
  "prompt": "What does torch.sparse.to_sparse_semi_structured support? What are the limitations and capabilities?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://docs.pytorch.org/tutorials/advanced/semi_structured_sparse.html",
    "prompt": "What does torch.sparse.to_sparse_semi_structured support? What are the limitations and capabilities?"
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-19T02:57:42.225651+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://developer.nvidia.com/blog/exploiting-ampere-structured-sparsity-with-cusparselt/",
  "prompt": "cuSPARSELt performance characteristics and structured sparsity support details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://developer.nvidia.com/blog/exploiting-ampere-structured-sparsity-with-cusparselt/",
    "prompt": "cuSPARSELt performance characteristics and structured sparsity support details"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-19T02:57:42.225780+00:00_

Web search results for query: "site:github.com "block sparse" OR "sparse matmul" triton inference activation"

Links: [{"title":"Segfault when using blocksparse matmul in attention · Issue #237 · triton-lang/triton","url":"https://github.com/openai/triton/issues/237"},{"title":"CUDA errors on kernels after block sparse Triton ops · Issue #882 · triton-lang/triton","url":"https://github.com/triton-lang/triton/issues/882"},{"title":"GitHub - facebookresearch/spartan: Spartan is an algorithm for training sparse neural network models. This repository accompanies the paper \"Spartan Differentiable Sparsity via Regularized Transportation\" (NeurIPS 2022).","url":"https://github.com/facebookresearch/spartan"},{"title":"GitHub - yaozhewei/MLPruning: MLPruning, PyTorch, NLP, BERT, Structured Pruning","url":"https://github.com/yaozhewei/MLPruning"},{"title":"GitHub - zhengqigao/hbsattn: a high-performance Block Sparse Attention kernel in Triton","url":"https://github.com/zhengqigao/hbsattn"},{"title":"Q-Sparse: All Large Language Models can be Fully Sparsely-Activated","url":"https://arxiv.org/pdf/2407.10969"},{"title":"Is there a triton implementation of block sparse flash attention? · Issue #2012 · triton-lang/triton","url":"https://github.com/triton-lang/triton/issues/2012"},{"title":"GitHub - mit-han-lab/x-attention: [ICML 2025] XAttention: Block Sparse Attention with Antidiagonal Scoring · GitHub","url":"https://github.com/mit-han-lab/x-attention"}]

I found several relevant results related to block sparse operations and Triton inference. Here's what the search returned:

**Key Findings:**

1. **Triton Block Sparse Operations**: Triton provides block sparse matmul operations that can be used for attention mechanisms with different modes like "sdd" and "dsd".

2. **Known Issues**: Block sparse linear layers have been associated with CUDA errors when using Triton ops, including RuntimeError related to CUBLAS initialization.

3. **Research Libraries**: 
   - MLPruning incor
…[truncated 812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-19T02:57:42.225931+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/SakanaAI/sparser-faster-llms",
  "prompt": "TwELL sparse format and CUDA kernel implementation for activation sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/SakanaAI/sparser-faster-llms",
    "prompt": "TwELL sparse format and CUDA kernel implementation for activation sparsity"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-19T02:57:42.226079+00:00_

Web search results for query: "Mixture-of-Depths early exit sparse inference kernel GitHub"

Links: [{"title":"GitHub - koayon/awesome-adaptive-computation: A curated reading list of research in Adaptive Computation, Inference-Time Computation & Mixture of Experts (MoE). · GitHub","url":"https://github.com/koayon/awesome-adaptive-computation"},{"title":"GitHub - raymin0223/mixture_of_recursions: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation (NeurIPS 2025) · GitHub","url":"https://github.com/raymin0223/mixture_of_recursions"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models","url":"https://arxiv.org/html/2404.02258v1"},{"title":"GitHub - paulilioaica/Mixture-Of-Depths","url":"https://github.com/paulilioaica/Mixture-Of-Depths"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models - Graphcore Research Blog","url":"https://graphcore-research.github.io/mixture-of-depths/"},{"title":"GitHub - falcon-xu/early-exit-papers: A curated list of early exiting (LLM, CV, NLP, etc) · GitHub","url":"https://github.com/falcon-xu/early-exit-papers"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive","url":"https://arxiv.org/pdf/2507.10524"}]

I found several relevant resources related to Mixture-of-Depths and sparse inference:

## Key GitHub Resources

The paulilioaica/Mixture-Of-Depths repository explores how transformer-based language models can dynamically allocate computation to specific positions in a sequence, optimizing allocation across layers in the model depth. The proposed method enforces a fixed compute budget by capping the number of tokens that participate in self-attention and MLP computations at each layer, with tokens routed to either full computation or a residual connection.

## Overview of Mixture-of-Depths

MoD sets a static compute budget which limits the number of tokens that can participate in a transformer layer'
…[truncated 661 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-19T02:57:42.226237+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/pdf/2603.23198",
  "prompt": "Sparser Faster Lighter Transformer - activation sparsity approach and performance results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/pdf/2603.23198",
    "prompt": "Sparser Faster Lighter Transformer - activation sparsity approach and performance results"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-19T02:57:42.226368+00:00_

Web search results for query: ""activation sparsity" LLM kernel implementation cuSPARSE unstructured"

Links: [{"title":"cuSPARSE | NVIDIA Developer","url":"https://developer.nvidia.com/cusparse"},{"title":"Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative Model Inference With Unstructured Sparsity | by FSA Lab | Medium","url":"https://medium.com/@fsalab/flash-llm-enabling-cost-effective-and-highly-efficient-large-generative-model-inference-with-06ef6c586734"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/pdf/2603.23198"},{"title":"Published as a conference paper at ICLR 2024 RELU STRIKES BACK:","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6cf669c222ad13f60d503736fb2bd15b-Paper-Conference.pdf"},{"title":"Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large","url":"https://jamesthez.github.io/files/flashllm-vldb24.pdf"},{"title":"SpInfer: Leveraging Low-Level Sparsity for Efficient Large ...","url":"https://www.cse.ust.hk/~weiwa/papers/eurosys25-fall-spinfer.pdf"},{"title":"Coruscant: Co-Designing GPU Kernel and Sparse Tensor Core to Advocate Unstructured Sparsity in Efficient LLM Inference | Proceedings of the 58th IEEE/ACM International Symposium on Microarchitecture","url":"https://dl.acm.org/doi/full/10.1145/3725843.3756065"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/pdf/2408.14690"}]

Based on the search results, here's what I found about activation sparsity, LLM kernel implementation, cuSPARSE, and unstructured sparsity:

## Key Findings

**cuSPARSE Overview:**
The cuSPARSE APIs provides GPU-accelerated basic linear algebra subroutines for sparse matrix computations for unstructured sparsity. cuSPARSE is widely used by engineers and scientists working on applications in machine learning, AI, computational fluid dynamics, seismic exploration, and computational sciences.

**Limitations of cuSPARSE for LLM Inference:**
F
…[truncated 1131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-19T02:57:42.226517+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"sparse FFN\" OR \"activation sparsity\" Triton kernel GitHub open source code 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"sparse FFN\" OR \"activation sparsity\" Triton kernel GitHub open source code 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-19T02:57:42.226646+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com wh-xu sparse-ffn-llm implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com wh-xu sparse-ffn-llm implementation"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-19T02:57:42.226778+00:00_

Web search results for query: "sparse activation inference kernel LLM CUDA Triton 2024 2025"

Links: [{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"From 11% to 88% Peak Bandwidth: Writing Custom Triton Kernels for LLM Inference | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2025/triton-kernels-llm-inference/"},{"title":"Triton Kernel Implementation","url":"https://www.emergentmind.com/topics/triton-kernel-implementation"},{"title":"CHESS: Optimizing LLM Inference via Channel-Wise Thresholding and   Selective Sparsification","url":"https://arxiv.org/pdf/2409.01366"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/pdf/2504.19449"},{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity","url":"https://arxiv.org/pdf/2602.14452"},{"title":"CUDA-Free Inference for LLMs – PyTorch","url":"https://pytorch.org/blog/cuda-free-inference-for-llms/"},{"title":"ReLU$^2$ Wins: Discovering Efficient Activation Functions for Sparse   LLMs","url":"https://arxiv.org/pdf/2402.03804"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"}]

Based on the search results, here's what I found regarding sparse activation inference kernels for LLMs with CUDA and Triton in 2024-2025:

## Recent Developments in Sparse Activation Inference

**Sparse Activation Optimization Approaches:**

Activation sparsity has emerged as a promising solution that dynamically loads only the active channels and their corresponding weight rows or columns from off-chip HBM to on-chip SRAM, significantly alleviating latency and memory cost when equipped with optimized system implementations.

**Key Projects and Methods:**

1. **SparseInfer**: Uses a CUDA kernel for XOR-based activation sparsity prediction with GPU parallel processing, and applies kernel 
…[truncated 1146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-19T02:57:42.226930+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com scattermoe sparse mixture experts Triton"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com scattermoe sparse mixture experts Triton"
  }
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-19T02:57:42.227078+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Q-Sparse activation sparsity GitHub implementation code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Q-Sparse activation sparsity GitHub implementation code"
  }
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-19T02:57:42.227211+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com \"sparse activation\" matmul CUDA kernel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com \"sparse activation\" matmul CUDA kernel"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-19T02:57:42.227341+00:00_

Web search results for query: "Griffin sparse LLM kernel inference GitHub"

Links: [{"title":"Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://arxiv.org/html/2402.19427v1"},{"title":"GitHub - hdong920/GRIFFIN · GitHub","url":"https://github.com/hdong920/GRIFFIN"},{"title":"Prompt-prompted Adaptive Structured Pruning for Efficient LLM Generation","url":"https://arxiv.org/pdf/2404.01365"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/pdf/2603.23198"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"GitHub - SakanaAI/sparser-faster-llms: Cuda kernels for leveraging LLM sparsity to improve throughput and decrease the memory requirements during inference and training. · GitHub","url":"https://github.com/SakanaAI/sparser-faster-llms"},{"title":"Self-Selected Attention Span for Accelerating Large Language Model   Inference","url":"https://arxiv.org/pdf/2404.09336"},{"title":"GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library for LLM Serving · GitHub","url":"https://github.com/flashinfer-ai/flashinfer"}]

Based on the search results, here are the key findings related to Griffin sparse LLM kernel inference:

## Griffin: Mixing Gated Linear Recurrences with Local Attention

Griffin uses a kernel for the RG-LRU layer, implemented in Pallas, that minimizes memory transfers. During inference, Griffin achieves significantly higher throughput than MQA Transformers and achieves lower latency when sampling long sequences.

## GRIFFIN: Gating by Repetition In Feedforward Intermediate Neurons

A separate project with the same acronym exists on GitHub: GRIFFIN (Gating by Repetition In Feedforward Intermediate Neurons) is an efficient method to adaptively and instantan
…[truncated 646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-19T02:57:42.227492+00:00_

# torch.sparse.to_sparse_semi_structured Support & Limitations

## Supported Capabilities

Based on the tutorial, `to_sparse_semi_structured` enables acceleration of **2:4 semi-structured sparse models** for inference. Specifically:

- **Converts dense, zeroed-out weights** into a compressed sparse format that GPUs can efficiently process
- **Works with nn.Linear layers** that follow the 2:4 sparsity pattern (2 zeros per every 4 elements)
- **Achieves measurable speedups**: The tutorial demonstrates "1.3x speedup over the fp16 baseline, and up to 2x with torch.compile"
- **Compatible with torch.compile** for additional performance gains
- **Preserves numerical accuracy**: The tutorial confirms "sparse and dense matmul are numerically equivalent"

## Key Limitations

- **Hardware requirements**: Requires "A NVIDIA GPU with semi-structured sparsity support (Compute Capability 8.0+)"
- **Data type**: Requires FP16 precision; "2:4 sparsity require fp16"
- **Sparsity pattern constraints**: Only works with properly formatted 2:4 sparse weights; doesn't automatically create sparsity
- **Shape dependencies**: Performance gains vary significantly by batch size—"When batch sizes are small and limited time is spent in compute sparse kernels may be slower than their dense counterparts"
- **Pre-sparsified models only**: Requires weights already in 2:4 sparse format; the function compresses but doesn't prune

The function serves as the **inference acceleration layer** after separate magnitude pruning and fine-tuning steps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-19T02:57:42.227637+00:00_

Web search results for query: ""PowerInfer" sparse operator implementation GPU kernel source"

Links: [{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU∗","url":"https://ipads.se.sjtu.edu.cn/_media/publications/powerinfer-20231219.pdf"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/pdf/2312.12456"},{"title":"[2312.12456] PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU","url":"https://arxiv.org/abs/2312.12456"},{"title":"GitHub - Raincleared-Song/sparse_gpu_operator: GPU operators for sparse tensor operations","url":"https://github.com/Raincleared-Song/sparse_gpu_operator"},{"title":"PowerInfer: Fast Large Language Model Serving with a ...","url":"https://www.emergentmind.com/papers/2312.12456"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU | Proceedings of the ACM SIGOPS 30th Symposium on Operating Systems Principles","url":"https://dl.acm.org/doi/10.1145/3694715.3695964"},{"title":"About | PowerInfer","url":"https://powerinfer.ai/about/"},{"title":"GitHub - Tiiny-AI/PowerInfer: High-speed Large Language Model Serving for Local Deployment · GitHub","url":"https://github.com/Tiiny-AI/PowerInfer"},{"title":"Sparse GPU Kernels for Deep Learning Trevor Gale Stanford University","url":"https://arxiv.org/pdf/2006.10901"}]

Based on the web search results, here's what I found about PowerInfer's sparse operator implementation and GPU kernel source:

## Overview

PowerInfer integrates adaptive predictors and neuron-aware sparse operators, optimizing the efficiency of neuron activation and computational sparsity. The implementation combines both CPU and GPU components.

## GPU Kernel Source and Implementation

The online inference engine is realized by extending existing LLM frameworks with additional implementations in C++ and CUDA, while the offline component utilizes a Python-based profiler and solver to categorize neuron
…[truncated 888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-19T02:57:42.227792+00:00_

Web search results for query: "DeepSparse inference engine sparsity format support CPU optimization"

Links: [{"title":"What is DeepSparse in AI Inference?","url":"https://www.thelasttech.com/ai/what-is-deepsparse-in-ai-inference"},{"title":"Deepsparse - Crazytools.ai","url":"https://crazytools.ai/tool/deepsparse/"},{"title":"deepsparse · PyPI","url":"https://pypi.org/project/deepsparse/1.8.0/"},{"title":"DeepSparse download | SourceForge.net","url":"https://sourceforge.net/projects/deepsparse.mirror/"},{"title":"Optimizing YOLO26 Inferences with Neural Magic's DeepSparse Engine | Ultralytics Docs","url":"https://docs.ultralytics.com/integrations/neural-magic"},{"title":"GitHub - williamsnick606/deepsparse_fork: Neural network inference engine that delivers GPU-class performance for sparsified models on CPUs","url":"https://github.com/williamsnick606/deepsparse_fork"},{"title":"deepsparse/src/deepsparse/yolo/README.md at main · neuralmagic/deepsparse","url":"https://github.com/neuralmagic/deepsparse/blob/main/src/deepsparse/yolo/README.md"},{"title":"GitHub - neuralmagic/deepsparse: Sparsity-aware deep learning inference runtime for CPUs · GitHub","url":"https://github.com/neuralmagic/deepsparse"},{"title":"Sparse fine-tuning for accelerating large language models with DeepSparse | Red Hat Developer","url":"https://developers.redhat.com/articles/2023/10/12/sparse-fine-tuning-accelerating-llms-with-deepsparse"},{"title":"SparseDNN: Fast Sparse Deep Learning Inference on CPUs Ziheng Wang","url":"https://arxiv.org/pdf/2101.07948"}]

Based on the search results, here's what I found about DeepSparse inference engine:

## Overview
DeepSparse is an inference runtime from Neural Magic that delivers GPU-class performance on CPUs for deep learning models. It is a CPU inference runtime that takes advantage of sparsity to accelerate neural network inference.

## Sparsity Format Support
DeepSparse uses advanced algorithms to identify and exploit sparsity in neural networks, redu
…[truncated 985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-19T02:57:42.227933+00:00_

# Summary of "Sparser, Faster, Lighter Transformer Language Models"

This GitHub repository by SakanaAI contains implementation code for a research paper focused on optimizing transformer language models through sparsity techniques.

## Key Features

**Core Technology**: The project provides "Cuda kernels for leveraging LLM sparsity to improve throughput and decrease" memory requirements during inference and training. The implementation uses the TwELL packing format optimized for H100 GPUs.

**Available Resources**:
- Pretrained sparse checkpoints ranging from 0.5B to 2B parameters available on Hugging Face Hub
- Custom CUDA kernels with two variants: standard `twell` and `twell-flex` for non-uniform sparsity patterns
- Inference benchmarking tools and training code using PyTorch

**Repository Structure**: The codebase includes sparse model definitions, dataset utilities, Hydra configuration files, and specialized CUDA modules. The project is written primarily in CUDA (49.6%), Python (40.5%), and C++ (9.4%).

## Getting Started

Installation requires CUDA 12.8+ and can be completed via a provided installation script. Training supports multi-GPU setups with DeepSpeed integration, while inference benchmarking allows comparison between PyTorch and TwELL implementations.

The work is published under an MIT license and cites authors from both Sakana AI and Nvidia.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-19T02:57:42.228095+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FlashInfer sparse activation LLM kernel GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FlashInfer sparse activation LLM kernel GitHub"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-19T02:57:42.228232+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SparseInfer\" activation sparsity LLM kernel implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SparseInfer\" activation sparsity LLM kernel implementation"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-19T02:57:42.228352+00:00_

# Sparser, Faster, Lighter Transformer Language Models

This research paper presents methods to reduce transformer model size and computational requirements through activation sparsity techniques.

## Key Approach

The authors develop techniques to identify and eliminate redundant computations in transformer networks. Rather than processing all tokens equally, their method recognizes that "many tokens do not require the full capacity of the model" and can be computed with reduced computational overhead.

## Performance Characteristics

The sparsity-based approach achieves notable efficiency gains:

- **Computational reduction**: Models process a subset of tokens through lighter computation paths
- **Memory efficiency**: Reduced model footprint without substantial accuracy loss
- **Inference speed**: Faster execution times compared to dense baseline models

## Technical Implementation

The methodology integrates activation patterns analysis to determine which computations contribute meaningfully to output quality. This selective processing strategy preserves model capability while diminishing resource consumption.

## Significance

This work addresses a critical challenge in deploying large language models: the computational and environmental costs associated with inference. By demonstrating that transformer efficiency can improve through intelligent sparsity patterns, the research enables more accessible model deployment across resource-constrained environments.

The research team includes contributors from Sakana AI and Google DeepMind, indicating collaboration between industry and research institutions on practical efficiency improvements for modern language models.

[Binary content (application/pdf, 1.6MB) also saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/7d58e080-b37e-425d-823d-30d547736bee/tool-results/webfetch-1779159267222-ht7eov.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-19T02:57:42.228491+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "R-Sparse rank-aware activation sparsity GitHub 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "R-Sparse rank-aware activation sparsity GitHub 2025"
  }
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-19T02:57:42.228615+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"WiSparse\" weight-aware mixed activation sparsity GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"WiSparse\" weight-aware mixed activation sparsity GitHub"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-19T02:57:42.228737+00:00_

Web search results for query: "site:github.com wh-xu sparse-ffn-llm implementation"

Links: [{"title":"GitHub - wh-xu/sparse-ffn-llm: A sparse and retraining-free FFN/MoE inference algorithm for large language model (LLM)","url":"https://github.com/wh-xu/sparse-ffn-llm"},{"title":"sparse-ffn-llm/eval_long_ppl.py at main · wh-xu/sparse-ffn-llm","url":"https://github.com/wh-xu/sparse-ffn-llm/blob/main/eval_long_ppl.py"},{"title":"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity","url":"https://arxiv.org/pdf/2602.00397"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/pdf/2603.23198"},{"title":"FAST-Prefill: FPGA Accelerated Sparse Attention for Long Context LLM Prefill","url":"https://arxiv.org/pdf/2602.20515"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"}]

Based on the search results, I found the GitHub repository you're looking for:

The sparse-ffn-llm repository by wh-xu is "A sparse and retraining-free FFN/MoE inference algorithm for large language model (LLM)".

The repository is located at: https://github.com/wh-xu/sparse-ffn-llm

The implementation includes evaluation code that works with models like Facebook's OPT-1.3B and datasets like Wikitext, with features such as sparse FFN activation that can be enabled during inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-19T02:57:42.228875+00:00_

# cuSPARSELt Performance and Structured Sparsity Support

## Performance Characteristics

**Speedup Metrics:**
The library demonstrates significant acceleration over dense operations. For instance, a BERT-Large model showed performance gains ranging from 1.3x to 1.6x speedup across different layers. The QKV layer achieved 1.4x speedup (188 to 263 TFLOPs), while the FC2 layer reached 1.6x (211 to 339 TFLOPs).

Performance varies based on matrix dimensions and data types. According to the blog, "the larger the workload is, the more that sparsity can help."

## Structured Sparsity Support

**2:4 Sparsity Pattern:**
The NVIDIA Ampere architecture implements a "2:4 pattern: out of every four elements, at least two must be zero." This constraint enables the hardware to skip zero computations while maintaining accuracy.

**Data Type Support:**
The library provides "mixed-precision support" including FP16, BFLOAT16, and INT8 inputs/outputs with corresponding accumulation types.

**Key Capability:**
cuSPARSELt leverages Sparse Tensor Cores to "double throughput by skipping the computation of the zero values," effectively doubling math efficiency compared to regular Tensor Core operations on the same pruned matrices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-19T02:57:42.229033+00:00_

Web search results for query: "site:github.com scattermoe sparse mixture experts Triton"

Links: [{"title":"GitHub - shawntan/scattermoe: Triton-based implementation of Sparse Mixture of Experts.","url":"https://github.com/shawntan/scattermoe"},{"title":"Scattered Mixture-of-Experts Implementation","url":"https://arxiv.org/pdf/2403.08245"},{"title":"GitHub - rkinas/triton-resources: A curated list of resources for learning and exploring Triton, OpenAI's programming language for writing efficient GPU code. · GitHub","url":"https://github.com/rkinas/triton-resources"},{"title":"GitHub - lucidrains/mixture-of-experts: A Pytorch implementation of Sparsely-Gated Mixture of Experts, for massively increasing the parameter count of language models · GitHub","url":"https://github.com/lucidrains/mixture-of-experts"},{"title":"PuzzleMoE: Efficient Compression of Large Mixture-of-Experts Models via Sparse Expert Merging and Bit-packed inference","url":"https://arxiv.org/pdf/2511.04805"}]

Based on the search results, here's what I found:

ScatterMoE is a Triton-based implementation of Sparse Mixture-of-Experts (SMoE) on GPUs. The repository is located at https://github.com/shawntan/scattermoe.

ScatterMoE builds upon existing implementations and overcomes some limitations to improve inference, training speed, and memory footprint by avoiding padding and making excessive copies of the input. The implementation fuses expert linear transforms and reordering operations with ParallelLinear, a module that can be used to extend the concept of SMoEs.

This implementation is lightweight (~700 lines) and will work within an FSDP or pipeline parallel framework, but does not include any additional multi-node training infrastructure code.

Additionally, the implementation has been benchmarked against Megablocks, showing higher throughput and lower memory footprint.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-19T02:57:42.229194+00:00_

Web search results for query: ""sparse FFN" OR "activation sparsity" Triton kernel GitHub open source code 2024 2025"

Links: [{"title":"GitHub - fla-org/native-sparse-attention: 🐳 Efficient Triton implementations for \"Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention\"","url":"https://github.com/fla-org/native-sparse-attention"},{"title":"GitHub - Raincleared-Song/sparse_gpu_operator: GPU operators for sparse tensor operations","url":"https://github.com/Raincleared-Song/sparse_gpu_operator"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=iOy2pITOoH"},{"title":"Spark Transformer: Reactivating Sparsity in FFN and Attention","url":"https://arxiv.org/pdf/2506.06644"},{"title":"Accelerating Transformer Inference and Training with 2:4 Activation   Sparsity","url":"https://arxiv.org/pdf/2503.16672"},{"title":"GitHub - corl-team/flexsae: Official Triton kernels for TopK and HierarchicalTopK Sparse Autoencoder decoders. · GitHub","url":"https://github.com/corl-team/flexsae"}]

Based on the web search results, here are several relevant open-source projects with Triton kernels for sparse FFN and activation sparsity from 2024-2025:

## Key Projects Found:

### 1. **Native Sparse Attention (fla-org)**
Recent updates in 2025 include full support for NSA training with flame, an online top-k selection kernel that avoids materializing the attention matrix, and a fused Triton kernel combining selected attention with sliding attention. The project is available at: https://github.com/fla-org/native-sparse-attention

### 2. **Sparse GPU Operator (ProSparse)**
This repository contains source code for sparse GPU operators mentioned in the ProSparse paper, tailored for ReLU-activated FFNs in LLMs. The operators include a fused ReLU operator and sparse matrix-vector multiplication with input-side sparsity, with code in kernel/formula_23_kernel.cu and kernel/formula_4_kernel.cu.
…[truncated 942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-19T02:57:42.229354+00:00_

Web search results for query: "sparse LLM inference frameworks comparison 2024 2025"

Links: [{"title":"GitHub - xlite-dev/Awesome-LLM-Inference: 📚A curated list of Awesome LLM/VLM Inference Papers with Codes: Flash-Attention, Paged-Attention, WINT8/4, Parallelism, etc.🎉","url":"https://github.com/xlite-dev/Awesome-LLM-Inference"},{"title":"A Survey of Efficient LLM Inference Serving","url":"https://aclanthology.org/2025.inlg-main.32.pdf"},{"title":"LLM Inference Frameworks 2025: Complete Guide | Medium","url":"https://medium.com/@michael.hannecke/choosing-the-right-llm-inference-framework-a-practical-guide-acb3d1c40a5b"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity","url":"https://arxiv.org/pdf/2602.14452"},{"title":"2026 Ultimate LLM Inference Framework Guide: 7 Frameworks Compared - No More Confusion • StableLearn | Make AI Your Superpower","url":"https://stable-learn.com/en/llm-inference-framework-guide-2026/"},{"title":"ReLU$^2$ Wins: Discovering Efficient Activation Functions for Sparse   LLMs","url":"https://arxiv.org/pdf/2402.03804"}]

Based on the search results, here's what I found about sparse LLM inference frameworks in 2024-2025:

## Recent Sparse LLM Inference Techniques

SparseInfer, released in November 2024, is a training-free approach for predicting activation sparsity for fast LLM inference from the University of Seoul. SparseInfer proposes a calibrated solution for ReLU-fied LLMs using sign-bit comparisons.

Experiments on sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8× reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores.

## Key Sparse Activation Approaches

Several methods have emerged for leveraging sparse activations:

- GRIFFIN selects active "expert" neurons using prefill activation
…[truncated 887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-19T02:57:42.229516+00:00_

Web search results for query: "Q-Sparse activation sparsity GitHub implementation code"

Links: [{"title":"GitHub - nanowell/Q-Sparse-LLM: My Implementation of Q-Sparse: All Large Language Models can be Fully Sparsely-Activated","url":"https://github.com/nanowell/Q-Sparse-LLM"},{"title":"GitHub - ostix360/Q-sparse: Unofficial implementation of Q-sparse: All Large Language Models can be Fully Sparsely-Activated https://arxiv.org/abs/2407.10969","url":"https://github.com/ostix360/Q-sparse"},{"title":"Q-Sparse: Activating Full Sparsity in Large Language Models - A Revolution","url":"https://www.visive.ai/news/q-sparse-activating-full-sparsity-in-large-language-models-a-revolution"},{"title":"Q-Sparse: All Large Language Models can be Fully Sparsely-Activated","url":"https://arxiv.org/pdf/2407.10969"},{"title":"Q-Sparse: All Large Language Models can be Fully Sparsely-Activated | OpenReview","url":"https://openreview.net/forum?id=cit3SNnZ6Q"},{"title":"[2407.10969] Q-Sparse: All Large Language Models can be Fully Sparsely-Activated","url":"https://arxiv.org/abs/2407.10969"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Exploiting activation sparsity in deep neural networks","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12131130"},{"title":"GitHub - mit-han-lab/sparsevit: [CVPR'23] SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer · GitHub","url":"https://github.com/mit-han-lab/sparsevit"}]

I found several GitHub implementations of Q-Sparse activation sparsity for you:

## Primary GitHub Implementations

1. **nanowell/Q-Sparse-LLM** (https://github.com/nanowell/Q-Sparse-LLM)
   - This implementation applies a mask to keep only the top K% of activations by magnitude and rescales the output by its L2 norm. It provides a QSparseModel initialization with configurable parameters like vocab_size, d_model, nhe
…[truncated 937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-19T02:57:42.229666+00:00_

Web search results for query: "site:github.com "sparse activation" matmul CUDA kernel"

Links: [{"title":"Accelerate activation sparsity with activation compression · Issue #1920 · pytorch/ao","url":"https://github.com/pytorch/ao/issues/1920"},{"title":"Block-Based Compression and Corresponding Hardware Circuits for Sparse Activations","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8622461/"},{"title":"ReLU$^2$ Wins: Discovering Efficient Activation Functions for Sparse   LLMs","url":"https://arxiv.org/pdf/2402.03804"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/pdf/2504.19449"},{"title":"Accelerating Transformer Inference and Training with 2:4 Activation   Sparsity","url":"https://arxiv.org/pdf/2503.16672"}]

I found search results related to sparse activation and CUDA kernels. Here are the key findings:

The PyTorch AO project accelerates sparse activation x dense weight matmul with 2:4 sparsity, which you can find in their GitHub issue tracker.

Two new CUDA kernels were implemented so that the entire FFN forward pass can be implemented with only 3 kernels: the existing FP8 matmul for the first linear layer, a new kernel that applies the activation, the sparsification, and FP8 quantization, and another new 2:4 GEMM kernel that supports FP8 rowwise scaling.

The R-Sparse project with code available at https://github.com/VITA-Group/R-Sparse demonstrates rank-aware activation sparsity for efficient LLM inference with customized kernels.

The most relevant GitHub resource appears to be the PyTorch AO repository (https://github.com/pytorch/ao) which contains discussions and implementations of sparse activation matmul CUDA kernels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-19T02:57:42.229807+00:00_

Web search results for query: ""WiSparse" weight-aware mixed activation sparsity GitHub"

Links: [{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-aware Mixed Activation Sparsity","url":"https://arxiv.org/html/2602.14452"},{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity","url":"https://arxiv.org/pdf/2602.14452"},{"title":"[2602.14452] WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity","url":"https://arxiv.org/abs/2602.14452"},{"title":"Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.57/"},{"title":"RANK-AWARE ACTIVATION SPARSITY FOR EFFICIENT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf"}]

Based on the search results, here's what I found about WiSparse:

## WiSparse Overview

WiSparse is a Weight-aware Mixed-Granularity Training-free Activation Sparsity method that leverages both activation and weight information and enables adaptive sparsity allocation across different granularities.

## Key Features

The method introduces a weight-aware activation sparsification mechanism that integrates activation magnitudes with precomputed weight norms to more accurately identify salient channels. This is combined with a mixed-granularity sparsity allocation scheme featuring a coarse-to-fine strategy: a global sparsity budget is first distributed across blocks via evolutionary search to protect sensitive regions, and subsequently refined at finer granularities within each block to minimize reconstruction error.

## Performance

At 50% sparsity, WiSparse preserves 97% of Llama3.1's dense model performance, surpassing the strongest baseline by 2.23 percentage points while achieving a 21.4% acceleration in end-to-end inference speed.

## Paper Details

The research was conducte
…[truncated 336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-19T02:57:42.229955+00:00_

Web search results for query: ""SparseInfer" activation sparsity LLM kernel implementation"

Links: [{"title":"[Literature Review] SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://www.themoonlight.io/en/review/sparseinfer-training-free-prediction-of-activation-sparsity-for-fast-llm-inference"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10992997/"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/html/2411.12692v1"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"(PDF) SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://www.researchgate.net/publication/385944711_SparseInfer_Training-free_Prediction_of_Activation_Sparsity_for_Fast_LLM_Inference"},{"title":"[2411.12692] SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/abs/2411.12692"},{"title":"Efficient Activation Functions for Sparse LLMs","url":"https://www.emergentmind.com/topics/efficient-activation-functions-for-sparse-llms"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/pdf/2504.19449"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/html/2504.19449v1"}]

Based on the search results, here's what I found about SparseInfer:

## Overview

SparseInfer is a method designed to enhance the inference efficiency of large language models (LLMs) through the exploitation of activation sparsity, particularly in models that utilize the ReLU activation function.

## Core Approach

SparseInfer is a simple, lightweight, and training-free predictor for 
…[truncated 1277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-19T02:57:42.230150+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/corl-team/flexsae",
  "prompt": "Triton kernels TopK sparse autoencoder implementation, kernel code, sparsity patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/corl-team/flexsae",
    "prompt": "Triton kernels TopK sparse autoencoder implementation, kernel code, sparsity patterns"
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-19T02:57:42.230291+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/wh-xu/sparse-ffn-llm",
  "prompt": "Sparse FFN inference algorithm, CUDA or Triton kernels, GPU acceleration implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/wh-xu/sparse-ffn-llm",
    "prompt": "Sparse FFN inference algorithm, CUDA or Triton kernels, GPU acceleration implementation"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-19T02:57:42.230419+00:00_

Web search results for query: "R-Sparse rank-aware activation sparsity GitHub 2025"

Links: [{"title":"GitHub - VITA-Group/R-Sparse: [ICLR'25] R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://github.com/VITA-Group/R-Sparse"},{"title":"[2504.19449] R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/abs/2504.19449"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/pdf/2504.19449"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=9VMW4iXfKt"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/html/2504.19449v1"},{"title":"RANK-AWARE ACTIVATION SPARSITY FOR EFFICIENT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf"},{"title":"DuoGPT: Training-free Dual Sparsity through Activation-aware Pruning in LLMs","url":"https://arxiv.org/html/2506.20194v1"}]

I found information about R-Sparse. Here are the search results:

## R-Sparse: Rank-Aware Activation Sparsity

R-Sparse is a training-free activation sparsity approach capable of achieving high sparsity levels in advanced LLMs.

**Key Technical Approach:**
The method replaces linear layers in LLMs with a rank-aware sparse inference method that leverages the sparsity of input channels and singular value components, eliminating the need for active channel prediction like output sparsity based approaches.

**Performance:**
Experiments on Llama-2/3 and Mistral models across ten diverse tasks demonstrate that R-Sparse achieves comparable performance at 50% model-level sparsity, resulting in a significant 43% end-to-end efficient improvements with customized kernels.

**GitHub Repository:**
The code is available at https://github.com/VITA-Group/R-Sparse.

**Publication:**
The paper "[ICLR'25
…[truncated 202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-19T02:57:42.230569+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/shawntan/scattermoe",
  "prompt": "Triton sparse mixture of experts implementation, kernel code, performance benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/shawntan/scattermoe",
    "prompt": "Triton sparse mixture of experts implementation, kernel code, performance benchmarks"
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-19T02:57:42.230701+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com \"sparse\" \"inference\" Triton kernel cuBLAS CUDA benchmark speedup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com \"sparse\" \"inference\" Triton kernel cuBLAS CUDA benchmark speedup"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-19T02:57:42.230831+00:00_

Web search results for query: "FlashInfer sparse activation LLM kernel GitHub"

Links: [{"title":"GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library for LLM Serving","url":"https://github.com/flashinfer-ai/flashinfer/tree/main"},{"title":"GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library for LLM Serving · GitHub","url":"https://github.com/flashinfer-ai/flashinfer"},{"title":"GitHub - happierpig/flashinfer-ai: FlashInfer: Kernel Library for LLM Serving","url":"https://github.com/happierpig/flashinfer-ai"},{"title":"GitHub - kvcache-ai/custom_flashinfer: FlashInfer: Kernel Library for LLM Serving · GitHub","url":"https://github.com/kvcache-ai/custom_flashinfer"},{"title":"GitHub - zlyuan9/my-flashinfer: FlashInfer: Kernel Library for LLM Serving","url":"https://github.com/zlyuan9/my-flashinfer"},{"title":"GitHub - dongshijiang/custom_flashinfer: FlashInfer: Kernel Library for LLM Serving","url":"https://github.com/dongshijiang/custom_flashinfer"},{"title":"GitHub - SystemPanic/flashinfer-windows: FlashInfer: Kernel Library for LLM Serving (Windows build & kernels)","url":"https://github.com/SystemPanic/flashinfer-windows"},{"title":"GitHub - yzh119/flashinfer-dev: FlashInfer: Kernel Library for LLM Serving","url":"https://github.com/yzh119/flashinfer-dev"},{"title":"GitHub - flashinfer-ai/flashinfer-bench-starter-kit: FlashInfer Bench @ MLSys 2026: Building AI agents to write high performance GPU kernels · GitHub","url":"https://github.com/flashinfer-ai/flashinfer-bench-starter-kit"}]

Based on the search results, here's what I found about FlashInfer sparse activation LLM kernel on GitHub:

## Overview

FlashInfer is a library and kernel generator for Large Language Models that provides high-performance implementation of LLM GPU kernels such as FlashAttention, SparseAttention, PageAttention, Sampling, and more.

## Key Features

FlashInfer provides efficient sparse/dense attention kernels with efficient single/batch attention for sparse(paged)/d
…[truncated 849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-19T02:57:42.230987+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp && git clone --depth 1 https://github.com/ScalingIntelligence/CATS.git 2>&1 | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp && git clone --depth 1 https://github.com/ScalingIntelligence/CATS.git 2>&1 | head -20"
  }
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-19T02:57:42.231144+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp && git clone --depth 1 https://github.com/FMInference/DejaVu.git 2>&1 | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp && git clone --depth 1 https://github.com/FMInference/DejaVu.git 2>&1 | head -20"
  }
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-19T02:57:42.231273+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp && git clone --depth 1 https://github.com/FasterDecoding/TEAL.git 2>&1 | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp && git clone --depth 1 https://github.com/FasterDecoding/TEAL.git 2>&1 | head -20"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-19T02:57:42.231391+00:00_

# Sparse FFN LLM Repository Overview

This GitHub repository contains "A sparse and retraining-free FFN/MoE inference algorithm for large language model (LLM)." The project focuses on memory-efficient inference optimization.

## Key Details

**Project Focus:** The repository implements optimization techniques for Feed-Forward Network (FFN) and Mixture of Experts (MoE) layers in large language models through approximation methods that don't require model retraining.

**Technical Stack:** The project requires PyTorch 2.2.1, Transformers 4.38.2, Datasets 2.18.0, lm_eval 0.4.0, and CUDA 12.2 GPU support.

**Repository Status:** The project contains 7 commits across multiple directories including `scripts` and `sparse_llm`, with Python representing 97.5% of the codebase and Shell scripts making up 2.5%.

**Licensing:** The project is released under an MIT license, making it open for academic and commercial use with proper attribution.

The repository includes evaluation scripts for perplexity assessment, benchmarking utilities, and training functionality, though usage documentation remains marked as "TODO."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-19T02:57:42.231510+00:00_

Cloning into 'CATS'...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-19T02:57:42.231624+00:00_

# FlexSAE: Triton Kernels for Sparse Autoencoders

## Overview

FlexSAE provides optimized Triton kernel implementations for TopK and HierarchicalTopK sparse autoencoder (SAE) decoders. The project stems from research accepted to EMNLP 2025 on "Train One Sparse Autoencoder Across Multiple Sparsity Budgets to Preserve Interpretability and Accuracy."

## Key Components

The repository includes:

- **TopK kernel**: A slightly modified version from xformers (`topk_kernels.py`)
- **HierarchicalTopK kernels**: Custom implementations (`hierarchical_kernels.py`)
- **Test suite**: CUDA-backed property tests ensuring numerical consistency across data types

## Performance Gains

The benchmarks demonstrate substantial improvements. On dictionary size F=65,536 with embedding dimension D=2,304:

- HierarchicalTopK achieves approximately "6.696 / 2.92" milliseconds/GiB at K=32, compared to "12.824 / 6.29" with pure torch compilation
- Memory usage remains flat at ~2.93 GiB across sparsity levels, versus 19.80 GiB for reference implementations

## Usage

Kernels load via: `flex = get_kernel('t-tech/flex-sae')` and support both `triton_topk_sae_loss` and `triton_hierarchical_sae_loss` functions operating on batch, sparse indices, and decoder weights.

## Licensing

Most code uses Apache License 2.0; the TopK kernel component adapted from Facebook Research remains restricted to non-commercial use.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-19T02:57:42.231752+00:00_

# ScatterMoE: Triton-Based Sparse Mixture of Experts

ScatterMoE is a GPU-optimized implementation of Sparse Mixture-of-Experts (SMoE) architecture. According to the repository, it's "Triton-based implementation of Sparse Mixture-of-Experts (SMoE) on GPUs."

## Key Features

The implementation aims to improve upon existing approaches by:
- Avoiding padding and excessive input copying
- Fusing expert linear transforms with reordering operations through a `ParallelLinear` module
- Maintaining a lightweight codebase (~700 lines)

## Technical Details

The project works within FSDP or pipeline parallel frameworks without requiring additional multi-node training infrastructure. It's written entirely in Python and includes testing utilities.

## Installation & Usage

Installation is straightforward via pip with `-e` flag for development. The module provides an `MLP` class that accepts input tensors along with top-k weights and indices from a router.

## Academic Backing

The work is documented in a research paper (arXiv:2403.08245) authored by Tan, Shen, Panda, and Courville (2024).

## Community Adoption

The repository has garnered 273 stars and 28 forks on GitHub, indicating moderate community interest in this specialized deep learning optimization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-19T02:57:42.231872+00:00_

Cloning into 'DejaVu'...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-19T02:57:42.231996+00:00_

Web search results for query: "site:github.com "sparse" "inference" Triton kernel cuBLAS CUDA benchmark speedup"

Links: [{"title":"GitHub - coderonion/awesome-cuda-and-hpc: 🚀🚀🚀 This repository lists some awesome public CUDA, cuda-python, cuBLAS, cuDNN, CUTLASS, TensorRT, TensorRT-LLM, Triton, TVM, MLIR, PTX and High Performance Computing (HPC) projects.","url":"https://github.com/coderonion/awesome-cuda-and-hpc"},{"title":"GitHub - HankWang-WL/CUDA-AI-inference-acceleration: CUDA batched matmul and PyTorch baseline, benchmark for AI acceleration","url":"https://github.com/HankWang-WL/CUDA-AI-inference-acceleration"},{"title":"GitHub - fpgaminer/GPTQ-triton: GPTQ inference Triton kernel","url":"https://github.com/fpgaminer/GPTQ-triton"},{"title":"GitHub - RightNow-AI/qwen3.5-triton: Pure Triton kernels for Qwen3.5-27B inference on NVIDIA B200 · GitHub","url":"https://github.com/RightNow-AI/qwen3.5-triton"},{"title":"GitHub - flagos-ai/awesome-LLM-driven-kernel-generation: Review automated kernel generation in the era of LLMs · GitHub","url":"https://github.com/flagos-ai/awesome-LLM-driven-kernel-generation"},{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/pdf/2603.25011"},{"title":"GitHub - hofong428/Optimizing-GPU-Kernels: LLM Serving & Inference Optimization · GitHub","url":"https://github.com/hofong428/Optimizing-GPU-Kernels"},{"title":"GitHub - bassrehab/triton-kernels: High-performance GPU kernels for LLM inference in OpenAI Triton. Fused RMSNorm, SwiGLU, INT8 GEMM with benchmarks and roofline analysis. · GitHub","url":"https://github.com/bassrehab/triton-kernels"}]

I found several relevant GitHub repositories related to sparse inference, Triton kernels, and CUDA benchmarks. Here are the results:

## Key Findings:

1. **Sparse Attention with Triton**: A repository contains customized CUDA kernels written in OpenAI Triton, including sparse attention kernels used in phi-3-small models.

2. **Qwen3
…[truncated 1015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-19T02:57:42.232178+00:00_

Cloning into 'TEAL'...
Updating files:  94% (1005/1060)Updating files:  95% (1007/1060)Updating files:  96% (1018/1060)Updating files:  97% (1029/1060)Updating files:  98% (1039/1060)Updating files:  99% (1050/1060)Updating files: 100% (1060/1060)Updating files: 100% (1060/1060), done.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-19T02:57:42.232308+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/native-sparse-attention",
  "prompt": "Triton kernel implementation for sparse attention, sparsity type, speedup benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/native-sparse-attention",
    "prompt": "Triton kernel implementation for sparse attention, sparsity type, speedup benchmarks"
  }
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-19T02:57:42.232446+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/bassrehab/triton-kernels",
  "prompt": "Triton kernels for LLM inference, SwiGLU sparse FFN implementation, benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/bassrehab/triton-kernels",
    "prompt": "Triton kernels for LLM inference, SwiGLU sparse FFN implementation, benchmarks"
  }
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-19T02:57:42.232613+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "R-Sparse rank-aware activation sparsity GitHub VITA-Group sparse inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "R-Sparse rank-aware activation sparsity GitHub VITA-Group sparse inference"
  }
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-19T02:57:42.232744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Spark Transformer\" sparse FFN attention GitHub implementation code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Spark Transformer\" sparse FFN attention GitHub implementation code"
  }
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-19T02:57:42.232869+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/CATS -name \"*.py\" -o -name \"*.cu\" -o -name \"*.cpp\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/CATS -name \"*.py\" -o -name \"*.cu\" -o -name \"*.cpp\" | head -30"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-19T02:57:42.233045+00:00_

/tmp/CATS/utils/utils.py
/tmp/CATS/utils/parse_args.py
/tmp/CATS/utils/mistral_utils.py
/tmp/CATS/utils/constants.py
/tmp/CATS/setup.py
/tmp/CATS/inference.py
/tmp/CATS/flash_gemv/test/test_fuse_gemv_cmp.py
/tmp/CATS/flash_gemv/setup.py
/tmp/CATS/flash_gemv/flash_gemv/kernels.py
/tmp/CATS/flash_gemv/flash_gemv/flash_gemv.py
/tmp/CATS/flash_gemv/flash_gemv/__init__.py
/tmp/CATS/flash_gemv/csrc/fuse_gemv_cmp.cpp
/tmp/CATS/flash_gemv/csrc/cuda/fuse_gemv_cmp_cuda.cu
/tmp/CATS/flash_gemv/bench/utils.py
/tmp/CATS/flash_gemv/bench/profile_mistral7B.py
/tmp/CATS/flash_gemv/bench/profile_llama7B.py
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py
/tmp/CATS/flash_gemv/bench/plot_latency.py
/tmp/CATS/flash_gemv/bench/__init__.py
/tmp/CATS/flash_gemv/artifact/mlp/plot_latency.py
/tmp/CATS/flash_gemv/artifact/e2e/plot_bar.py
/tmp/CATS/flash_gemv/artifact/e2e/geom_e2e.py
/tmp/CATS/flash_gemv/artifact/e2e/calculate_speedup.py
/tmp/CATS/flash_gemv/artifact/ablation/plot_ablation.py
/tmp/CATS/experiments/trainer.py
/tmp/CATS/experiments/time_util_nofile.py
/tmp/CATS/experiments/sparse_finetune.py
/tmp/CATS/experiments/replace_util.py
/tmp/CATS/experiments/pretrain_sparse_model.py
/tmp/CATS/experiments/plot_zero_shot.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-19T02:57:42.233210+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/DejaVu -name \"*.py\" -o -name \"*.cu\" -o -name \"*.cpp\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/DejaVu -name \"*.py\" -o -name \"*.cu\" -o -name \"*.cpp\" | head -30"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-19T02:57:42.233334+00:00_

/tmp/DejaVu/sparse_predictor/trainer_mlp.py
/tmp/DejaVu/sparse_predictor/trainer_att.py
/tmp/DejaVu/sparse_predictor/main_mlp.py
/tmp/DejaVu/sparse_predictor/main_att.py
/tmp/DejaVu/lm-eval-harness-adapter/tasks/util.py
/tmp/DejaVu/lm-eval-harness-adapter/tasks/eval_harness.py
/tmp/DejaVu/lm-eval-harness-adapter/tasks/__init__.py
/tmp/DejaVu/lm-eval-harness-adapter/generate_task_data.py
/tmp/DejaVu/lm-eval-harness-adapter/evaluate_task_result.py
/tmp/DejaVu/Dejavu/src/utils/dejavu_util.py
/tmp/DejaVu/Dejavu/src/utils/__init__.py
/tmp/DejaVu/Dejavu/src/ops/triton/k_activations.py
/tmp/DejaVu/Dejavu/src/ops/triton/gather_gemv.py
/tmp/DejaVu/Dejavu/src/ops/triton/attention_proj_sparse.py
/tmp/DejaVu/Dejavu/src/ops/triton/att_out_gemv.py
/tmp/DejaVu/Dejavu/src/ops/fused_dropout_add.py
/tmp/DejaVu/Dejavu/src/ops/fused_dense_sparse_dejavu.py
/tmp/DejaVu/Dejavu/src/models/modules/mha_dejavu.py
/tmp/DejaVu/Dejavu/src/models/modules/block_dejavu.py
/tmp/DejaVu/Dejavu/src/models/modules/__init__.py
/tmp/DejaVu/Dejavu/src/models/gpt_mlp_sparse.py
/tmp/DejaVu/Dejavu/src/models/gpt_dense.py
/tmp/DejaVu/Dejavu/src/models/gpt_dejavu.py
/tmp/DejaVu/Dejavu/src/models/__init__.py
/tmp/DejaVu/Dejavu/src/__init__.py
/tmp/DejaVu/Dejavu/benchmarks/benchmark_generation_opt_mlp_sparse.py
/tmp/DejaVu/Dejavu/benchmarks/benchmark_generation_opt_dejavu.py
/tmp/DejaVu/Dejavu/benchmarks/benchmark_generation_opt.py
/tmp/DejaVu/Dejavu/benchmarks/__init__.py
/tmp/DejaVu/Dejavu/benchmarks/.ipynb_checkpoints/benchmark_generation_opt_175b_dejavu-checkpoint.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-19T02:57:42.233476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/TEAL -name \"*.py\" -o -name \"*.cu\" -o -name \"*.cpp\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/TEAL -name \"*.py\" -o -name \"*.cu\" -o -name \"*.cpp\" | head -30"
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-19T02:57:42.233596+00:00_

/tmp/TEAL/utils/utils.py
/tmp/TEAL/utils/eval_ppl.py
/tmp/TEAL/utils/data.py
/tmp/TEAL/utils/__init__.py
/tmp/TEAL/teal/self_attn.py
/tmp/TEAL/teal/ppl_test.py
/tmp/TEAL/teal/model.py
/tmp/TEAL/teal/mlp.py
/tmp/TEAL/teal/greedyopt.py
/tmp/TEAL/teal/grab_acts.py
/tmp/TEAL/scripts/benchmark_gemv.py
/tmp/TEAL/kernels/sparse_gemv.py
/tmp/TEAL/kernels/kernel_utils.py
/tmp/TEAL/kernels/compile_wrapper.py
/tmp/TEAL/kernels/__init__.py
/tmp/TEAL/gpt-fast/tp.py
/tmp/TEAL/gpt-fast/tokenizer.py
/tmp/TEAL/gpt-fast/setup.py
/tmp/TEAL/gpt-fast/scripts/download.py
/tmp/TEAL/gpt-fast/scripts/convert_hf_checkpoint.py
/tmp/TEAL/gpt-fast/quantize.py
/tmp/TEAL/gpt-fast/model.py
/tmp/TEAL/gpt-fast/mixtral-moe/tp.py
/tmp/TEAL/gpt-fast/mixtral-moe/scripts/download.py
/tmp/TEAL/gpt-fast/mixtral-moe/scripts/convert_hf_checkpoint.py
/tmp/TEAL/gpt-fast/mixtral-moe/quantize.py
/tmp/TEAL/gpt-fast/mixtral-moe/model.py
/tmp/TEAL/gpt-fast/mixtral-moe/generate.py
/tmp/TEAL/gpt-fast/generate.py
/tmp/TEAL/gpt-fast/eval.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-19T02:57:42.233723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/CATS/flash_gemv/csrc/cuda/fuse_gemv_cmp_cuda.cu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/CATS/flash_gemv/csrc/cuda/fuse_gemv_cmp_cuda.cu"
  }
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-19T02:57:42.233846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/DejaVu/Dejavu/src/ops/triton/gather_gemv.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/DejaVu/Dejavu/src/ops/triton/gather_gemv.py"
  }
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-19T02:57:42.233958+00:00_

File content (42901 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-19T02:57:42.234178+00:00_

1	from typing import Optional
2	
3	import torch
4	import triton
5	import triton.language as tl
6	
7	from src.ops.triton.k_activations import relu, gelu, gelu_approx, squared_relu
8	
9	
10	@triton.jit
11	def apply_activation(x, ACTIVATION: tl.constexpr):
12	    if ACTIVATION == "relu":
13	        x = relu(x)
14	    elif ACTIVATION == "gelu":
15	        x = gelu(x)
16	    elif ACTIVATION == "gelu_approx":
17	        x = gelu_approx(x)
18	    elif ACTIVATION == "squared_relu":
19	        x = squared_relu(x)
20	    return x
21	
22	
23	@triton.autotune(
24	    configs=[
25	        triton.Config({"BLOCK_M": 4, "BLOCK_N": 256}, num_warps=4),
26	        triton.Config({"BLOCK_M": 4, "BLOCK_N": 512}, num_warps=4),
27	        triton.Config({"BLOCK_M": 4, "BLOCK_N": 1024}, num_warps=4),
28	        triton.Config({"BLOCK_M": 8, "BLOCK_N": 256}, num_warps=4),
29	        triton.Config({"BLOCK_M": 8, "BLOCK_N": 512}, num_warps=4),
30	        triton.Config({"BLOCK_M": 8, "BLOCK_N": 1024}, num_warps=4),
31	        triton.Config({"BLOCK_M": 16, "BLOCK_N": 256}, num_warps=4),
32	        triton.Config({"BLOCK_M": 16, "BLOCK_N": 512}, num_warps=4),
33	        triton.Config({"BLOCK_M": 16, "BLOCK_N": 1024}, num_warps=4),
34	    ],
35	    key=["CACHE_KEY_M", "CACHE_KEY_N", "BATCHSIZE"],
36	)
37	@triton.heuristics(
38	    {
39	        "EVEN_N": lambda args: args["N"] % args["BLOCK_N"] == 0,
40	    }
41	)
42	@triton.jit
43	def gather_gemv_kernel(
44	    Y,  # Pointers to matrices
45	    A,
46	    X,
47	    IDX,
48	    BIAS,
49	    # Matrix dimensions
50	    M,
51	    N,
52	    CACHE_KEY_M,
53	    CACHE_KEY_N,
54	    # The stride variables represent how much to increase the ptr by when moving by 1
55	    # element in a particular dimension. E.g. stride_am is how much to increase a_ptr
56	    # by to get the element one row down (A has M rows)
57	    stride_am,
58	    # Meta-parameters
59	    BATCHSIZE: tl.constexpr,
60	    HAS_BIAS: tl.constexpr,
61	    ACTIVATION: tl.constexpr,
62	    BLOCK_M
…[truncated 24717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-19T02:57:42.234353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/TEAL/kernels/sparse_gemv.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/TEAL/kernels/sparse_gemv.py"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-19T02:57:42.234521+00:00_

1	# adapted from deja vu
2	
3	from typing import Optional
4	
5	import torch
6	import triton
7	import triton.language as tl
8	def init_to_zero(*names):
9	    def init_func(nargs):
10	        for name in names:
11	            nargs[name].zero_()
12	    return init_func
13	
14	# NOTE: will need to warm up kernels each time, triton autotune caching isn't a thing right now
15	
16	configs=[
17	    triton.Config({"BLOCK_M": 64, "BLOCK_N": 128}, num_warps=2, pre_hook=init_to_zero("Y")), 
18	
19	    triton.Config({"BLOCK_M": 64, "BLOCK_N": 64}, num_warps=4, pre_hook=init_to_zero("Y")),
20	    triton.Config({"BLOCK_M": 8, "BLOCK_N": 128}, num_warps=2, pre_hook=init_to_zero("Y")),
21	    triton.Config({"BLOCK_M": 16, "BLOCK_N": 256}, num_warps=4, pre_hook=init_to_zero("Y")),
22	    triton.Config({"BLOCK_M": 16, "BLOCK_N": 256}, num_warps=4, pre_hook=init_to_zero("Y")),
23	    triton.Config({"BLOCK_M": 32, "BLOCK_N": 256}, num_warps=4, pre_hook=init_to_zero("Y")),
24	    triton.Config({"BLOCK_M": 64, "BLOCK_N": 256}, num_warps=4, pre_hook=init_to_zero("Y")),
25	    triton.Config({"BLOCK_M": 128, "BLOCK_N": 16}, num_warps=4, pre_hook=init_to_zero("Y")),
26	    triton.Config({"BLOCK_M": 128, "BLOCK_N": 32}, num_warps=4, pre_hook=init_to_zero("Y")),
27	    triton.Config({"BLOCK_M": 128, "BLOCK_N": 64}, num_warps=4, pre_hook=init_to_zero("Y")),
28	    triton.Config({"BLOCK_M": 128, "BLOCK_N": 128}, num_warps=4, pre_hook=init_to_zero("Y")),
29	    triton.Config({"BLOCK_M": 128, "BLOCK_N": 256}, num_warps=4, pre_hook=init_to_zero("Y")),
30	
31	    triton.Config({"BLOCK_M": 128, "BLOCK_N": 512}, num_warps=4, pre_hook=init_to_zero("Y")),
32	    triton.Config({"BLOCK_M": 64, "BLOCK_N": 512}, num_warps=4, pre_hook=init_to_zero("Y")),
33	    triton.Config({"BLOCK_M": 32, "BLOCK_N": 512}, num_warps=4, pre_hook=init_to_zero("Y")),
34	    triton.Config({"BLOCK_M": 16, "BLOCK_N": 512}, num_warps=4, pre_hook=init_to_zero("Y")),
35	
36	
37	    # Llama 3 variants can use BLOCK_N >= 1024
38	    #
…[truncated 9277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-19T02:57:42.234676+00:00_

# Native Sparse Attention: Efficient Triton Implementation

## Overview
This GitHub repository contains optimized Triton kernel implementations for Native Sparse Attention (NSA), a hardware-aligned sparse attention mechanism described in a 2025 research paper.

## Key Features

**Sparsity Type:** NSA combines two attention patterns:
- Selected attention (top-k block selection)
- Sliding window attention

The implementation includes "an online top‑k selection kernel that avoids materializing the attention matrix during selection."

## Performance Highlights

The benchmarks demonstrate significant efficiency gains. For a sequence length of 2048 tokens:
- NSA forward pass: 2.3ms
- Flash Attention forward: 0.97ms
- NSA backward: 11.1ms
- Flash Attention backward: 4.1ms

The repository includes visualization charts comparing performance across varying sequence lengths (128 to 16,384 tokens).

## Technical Implementation

The library supports:
- Variable-length inputs via sequence offsets
- Gradient computation (forward and backward passes)
- Dynamic block count handling across queries
- Integration with training frameworks via `flame`

## Installation & Usage

The package installs via standard Python tooling. Users can directly call the `parallel_nsa()` kernel with query, key, and value tensors, along with block indices and gate parameters controlling sparse selection and sliding attention.

The repository maintains 1,000+ stars and includes comprehensive testing utilities for validation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-19T02:57:42.234824+00:00_

Web search results for query: "R-Sparse rank-aware activation sparsity GitHub VITA-Group sparse inference"

Links: [{"title":"GitHub - VITA-Group/R-Sparse: [ICLR'25] R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://github.com/VITA-Group/R-Sparse"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/html/2504.19449v1"},{"title":"RANK-AWARE ACTIVATION SPARSITY FOR EFFICIENT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/pdf/2504.19449"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference | alphaXiv","url":"https://www.alphaxiv.org/resources/2504.19449v1"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=9VMW4iXfKt"},{"title":"VITA","url":"https://vita-group.github.io/publication.html"},{"title":"[2504.19449] R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/abs/2504.19449"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250419449Z/abstract"}]

Based on the search results, I found comprehensive information about R-Sparse:

## R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference

R-Sparse is a training-free activation sparsity approach capable of achieving high sparsity levels in advanced LLMs.

### Key Innovation

The method replaces the linear layers in LLMs with a rank-aware sparse inference method that leverages the sparsity of input channels and singular value components, eliminating the need for active channel prediction like the output sparsity based approaches.

### Performance Results

Experiments on Llama-2/3 and Mistral models across ten 
…[truncated 583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-19T02:57:42.234984+00:00_

Web search results for query: ""Spark Transformer" sparse FFN attention GitHub implementation code"

Links: [{"title":"Spark Transformer: Reactivating Sparsity in Transformer FFN and Attention","url":"https://openreview.net/pdf/83a01256d6f2b9860a6ad66ea9ffdc712111468f.pdf"},{"title":"[2506.06644] Spark Transformer: Reactivating Sparsity in FFN and Attention","url":"https://arxiv.org/abs/2506.06644"},{"title":"Spark Transformer: Reactivating Sparsity in FFN and Attention","url":"https://arxiv.org/pdf/2506.06644"},{"title":"Spark Transformer: Reactivating Sparsity in FFN and Attention","url":"https://arxiv.org/html/2506.06644v1"},{"title":"SPARK TRANSFORMER: HOW MANY FLOPS IS A TO","url":"https://openreview.net/pdf?id=iOy2pITOoH"},{"title":"GitHub - kyegomez/SparseAttention: Pytorch Implementation of the sparse attention from the paper: \"Generating Long Sequences with Sparse Transformers\" · GitHub","url":"https://github.com/kyegomez/SparseAttention"},{"title":"GitHub - lucidrains/sinkhorn-transformer: Sinkhorn Transformer - Practical implementation of Sparse Sinkhorn Attention · GitHub","url":"https://github.com/lucidrains/sinkhorn-transformer"}]

Based on the search results, here's what I found about Spark Transformer:

## Overview

The Spark Transformer is a novel architecture that achieves a high level of activation sparsity in both FFN and the attention mechanism while maintaining model quality, parameter count, and standard training procedures.

## Key Features

The method realizes sparsity via top-k masking for explicit control over sparsity level, and introduces statistical top-k, a hardware-accelerator-friendly, linear-time approximate algorithm that avoids costly sorting.

Spark Transformer reallocates existing FFN parameters and attention key embeddings to form a low-cost predictor for identifying activated entries.

## Performance Results

Pretrained with the Gemma-2 recipe, Spark Transformer demonstrates competitive performance while exhibiting significa
…[truncated 718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-19T02:57:42.235233+00:00_

Excellent! Now I have comprehensive information. Let me compile the final research report with all the findings:

## Comprehensive Research Report: LLM Sparse Inference Frameworks

Based on thorough web research, here's a detailed breakdown of sparse inference capabilities across major frameworks:

---

### 1. NEURAL MAGIC / DEEPSPARSE / NM-VLLM

#### DeepSparse Capabilities:

**Sparsity Support:**
- **Weight Sparsity: YES** (primary focus)
- **Activation Sparsity: LIMITED** — DeepSparse is primarily CPU-based and focuses on exploiting structured weight sparsity rather than dynamic activation sparsity
- **Format:** Supports unstructured and structured sparsity patterns; works with ONNX models
- **CPU-Only:** DeepSparse is a CPU inference runtime with support for AVX2, AVX-512, and VNNI instruction sets (x86 Intel Haswell+ and AMD)

**Important Status:**
⚠️ **As of June 2, 2025, Neural Magic ceased development and deprecated the community versions of DeepSparse** — tools no longer receive updates or support.

#### nm-vllm (Neural Magic's vLLM Fork):

**Features:**
- GPU-accelerated sparse inference kernels for LLMs
- **Supports structured weight sparsity** (2:4 sparsity patterns)
- **Activation sparsity partial support** through recent kernel implementations
- **Performance:** Up to **1.7x speedup on GPUs** through sparsity; sparse-quantized LLaMA on CPUs achieves **8.6x speedup**

**Sparse Models:**
- SparseGPT and Sparse Fine-tuning for weight pruning (≥50% weight removal)
- Newly-developed sparse inference kernels for acceleration

**SwiGLU/GatedMLP Support:**
- Research shows that models using dReLU (ReLU activation) can achieve ~90% sparsity while matching SwiGLU performance
- DeepSparse has tested sparse inference on models like LLaMA2-7B

#### GitHub & Documentation:
- [nm-vllm on PyPI](https://pypi.org/project/nm-vllm/)
- [nm-vllm GitHub](https://github.com/neuralmagic/nm-vllm)
- [nm-vllm Sparse Inference Examples](https://nm-vllm.readthedocs.io/en/0.5.0/gett
…[truncated 6868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Agent",
  "elapsed_ms": 23
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-19T02:57:42.235397+00:00_

# Triton Kernels Repository Summary

This GitHub repository provides optimized GPU kernels for large language model inference, implemented in OpenAI's Triton programming language.

## Key Offerings

The project includes several specialized kernels with impressive performance gains:

- **RMSNorm**: Achieves "8.1x" speedup through operation fusion
- **SwiGLU**: Fused gated linear unit with "1.6x" improvement
- **INT8 GEMM**: Quantized matrix multiplication enabling 2x memory savings
- **MoE Dispatch**: Mixture-of-Experts routing reaching "up to 9.1x" speedup

## Core Philosophy

The repository emphasizes that "LLM inference is memory-bandwidth bound," meaning data movement—not computation—limits performance. The kernels address this through fusion strategies that minimize intermediate tensor materialization and memory round-trips.

## Technical Foundation

Each implementation includes roofline analysis showing how kernels approach hardware limits. The project demonstrates that many LLM operations achieve only 10-20% bandwidth utilization with standard PyTorch, while these Triton implementations reach 80-88% of peak bandwidth.

## Accessibility

Drop-in module replacements allow integration into existing PyTorch models. The codebase provides comprehensive benchmarking tools and validation across NVIDIA and AMD platforms, though the author explicitly notes these are "educational implementations" rather than production-ready solutions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-19T02:57:42.235614+00:00_

Perfect! Now I have comprehensive information. Let me compile the research findings.

---

## COMPREHENSIVE RESEARCH ON PYTORCH SPARSE SUPPORT & NVIDIA SPARSE LIBRARIES FOR LLM ACTIVATION SPARSITY

### 1. PYTORCH SEMI-STRUCTURED SPARSITY

#### `torch.sparse.to_sparse_semi_structured` Capabilities & Limitations

**What it supports:**
- **2:4 structured sparsity only** — exactly 2 zeros per every 4 elements (50% sparsity ratio)
- Works with pre-sparsified weight tensors in `nn.Linear` layers
- FP16 precision required
- Hardware-accelerated on Ampere+ GPUs (Compute Capability 8.0+)
- Up to 2x speedup with `torch.compile`, typical 1.3-1.6x in practice

**Critical limitations:**
- **Cannot handle arbitrary unstructured sparsity** (e.g., 30-50% random neuron zeroing per token)
- Only compresses already-sparse weights; doesn't induce sparsity
- Requires static, pattern-conforming sparse weights
- Performance degrades significantly at small batch sizes (may be slower than dense)
- **No support for dynamic per-token activation masks**

**PyTorch native sparse matmul APIs:**
PyTorch provides `torch.sparse.mm()` for sparse-dense operations with COO/CSR formats, but these have fundamental limitations:
- No backwards pass support for sparse gradients on dense inputs
- Significantly higher overhead than dense operations for unstructured sparsity
- Not practical for dynamic token-by-token activation sparsity
- CSR format can use 2-3x more memory during backward passes vs COO

**Verdict:** PyTorch's sparse infrastructure is **limited to structured 2:4 patterns with static masks**. It cannot efficiently handle dynamic per-token activation sparsity without external solutions.

**Reference:** [PyTorch 2:4 Semi-Structured Sparsity Tutorial](https://docs.pytorch.org/tutorials/advanced/semi_structured_sparse.html)

---

### 2. NVIDIA cuSPARSE & cuSPARSELt PERFORMANCE

#### `cusparseSpMM` For Sparse Activation × Dense Weight

**Format support:**
- COO (Coordinate), CSR (Compressed Sparse 
…[truncated 9232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Agent",
  "elapsed_ms": 25
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-19T02:57:42.235782+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/VITA-Group/R-Sparse",
  "prompt": "Rank-aware activation sparsity kernel implementation, CUDA Triton code, customized kernels for sparse inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/VITA-Group/R-Sparse",
    "prompt": "Rank-aware activation sparsity kernel implementation, CUDA Triton code, customized kernels for sparse inference"
  }
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-19T02:57:42.235923+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com sparse autoencoder Triton decoder kernel topk"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com sparse autoencoder Triton decoder kernel topk"
  }
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-19T02:57:42.236125+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"sparse activation\" \"token-wise\" OR \"per-token\" mask LLM kernel GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"sparse activation\" \"token-wise\" OR \"per-token\" mask LLM kernel GitHub"
  }
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-19T02:57:42.236270+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Triton GEMM sparse pattern block structured 2:4 sparsity kernel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Triton GEMM sparse pattern block structured 2:4 sparsity kernel"
  }
}
```

</details>

---

### Tool call

_source line 189 · 2026-05-19T02:57:42.236399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/CATS/flash_gemv/csrc/cuda/fuse_gemv_cmp_cuda.cu",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/CATS/flash_gemv/csrc/cuda/fuse_gemv_cmp_cuda.cu",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 190 · 2026-05-19T02:57:42.236545+00:00_

1	#include "fuse_gemv_cmp_cuda.h"
2	#include "reduce_kernel_utils.cuh"
3	#include &lt;cuda_fp16.h>
4	#include &lt;cooperative_groups.h>
5	#include &lt;cuda.h>
6	#include &lt;cuda_runtime.h>
7	#include &lt;cuda_runtime_api.h>
8	
9	#include &lt;torch/torch.h>
10	#include &lt;ATen/Dispatch.h>
11	#include &lt;ATen/cuda/CUDAContext.h>
12	#include &lt;ATen/cuda/detail/IndexUtils.cuh>
13	#include &lt;ATen/cuda/detail/TensorInfo.cuh>
14	
15	
16	
17	#define N 4096
18	#define M 14336
19	
20	using namespace at::native;
21	using namespace cooperative_groups;
22	
23	constexpr float log2e = 1.44269504088896340736f;
24	
25	#define gpuErrchk(ans) { gpuAssert((ans), __FILE__, __LINE__); }
26	inline void gpuAssert(cudaError_t code, const char *file, int line, bool abort=true)
27	{
28	  if (code != cudaSuccess)
29	  {
30	    fprintf(stderr,"GPUassert: %s %s %d\n", cudaGetErrorString(code), file, line);
31	    if (abort) exit(code);
32	  }
33	}
34	
35	__forceinline__ __device__ float ptx_exp2(float x) {
36	    float y;
37	    asm volatile("ex2.approx.ftz.f32 %0, %1;" : "=f"(y) : "f"(x));
38	    return y;
39	  }
40	
41	__device__ __managed__ int length = 0;
42	
43	__global__ void fuse_gemv_cmp_kernel(half* input, half* weight, half* output, int64_t* idx, float threshold) {
44	    int m = blockIdx.x;
45	    int warp_id = threadIdx.y;
46	    int lane_id = threadIdx.x;
47	    __shared__ half2 temp_result[64];
48	    half2 w_0 = make_half2(weight[m * N + warp_id * 128 + lane_id], weight[m * N + warp_id * 128 + lane_id + 32]);
49	    half2 w_1 = make_half2(weight[m * N + warp_id * 128 + lane_id + 64], weight[m * N + warp_id * 128 + lane_id + 96]);
50	    half2 x_0 = make_half2(input[warp_id * 128 + lane_id], input[warp_id * 128 + lane_id + 32]);
51	    half2 x_1 = make_half2(input[warp_id * 128 + lane_id + 64], input[warp_id * 128 + lane_id + 96]);
52	
53	
54	    thread_block_tile<32, thread_block> group = tiled_partition<32>(this_thread_block());
55	    // Accumulate to local (first land)
56	    // First lane stores the
…[truncated 6071 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-19T02:57:42.236709+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"speedup\\|throughput\\|latency\" /tmp/CATS --include=\"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"speedup\\|throughput\\|latency\" /tmp/CATS --include=\"*.py\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-19T02:57:42.236838+00:00_

/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:    dense_latency_list = []
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:    baseline_latency_list = []
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:    ours_latency_list = []
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:    optimal_latency_list = []
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:                    dense_latency_list.append(float(row[2]))
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:                    baseline_latency_list.append(float(row[3]))
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:                    ours_latency_list.append(float(row[-2]))
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:                    optimal_latency_list.append(float(row[-1]))
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:    print(ours_latency_list, baseline_latency_list)
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:        "Dense Latency": dense_latency_list,
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:        "Ours Latency": ours_latency_list,
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:        "Baseline Latency": baseline_latency_list,
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:        "Optimal Latency": optimal_latency_list,
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:    save_dir = os.path.join(os.getenv("CATS_RESPATH", ""), "speedup", "figures")
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:    plt.savefig(save_dir + f"/fig4: {models[idx]}_mlp_latency.png")
/tmp/CATS/flash_gemv/bench/plot_latency_sub.py:    plt.savefig(save_dir + f"/fig6: {models[idx]}_mlp_ablation_latency.png")
/tmp/CATS/flash_gemv/bench/plot_latency.py:df = pd.read_excel('mlp-latency.xlsx')
/tmp/CATS/flash_gemv/bench/plot_latency.py:plt.savefig('latency.pdf')
/tmp/CATS/flash_gemv/bench/plot_latency.py:plt.savefig('latency.svg')
/tmp/CATS/flash_gemv/artifact/mlp/plot_latency.py:# plt.savefig('llama7B-latency-l40s-fp16.pdf')

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 193 · 2026-05-19T02:57:42.237012+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"speedup\\|throughput\\|latency\" /tmp/TEAL --include=\"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"speedup\\|throughput\\|latency\" /tmp/TEAL --include=\"*.py\" | head -20"
  }
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-19T02:57:42.237219+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"speedup\\|throughput\\|latency\" /tmp/DejaVu --include=\"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"speedup\\|throughput\\|latency\" /tmp/DejaVu --include=\"*.py\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-19T02:57:42.237346+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-19T02:57:42.237469+00:00_

/tmp/DejaVu/Decentralized_FM_alpha/unit_tests/io_test.py:    task_latency_sec = max([sec for _, sec, _ in pool_results])
/tmp/DejaVu/Decentralized_FM_alpha/unit_tests/io_test.py:    task_speed_GB = total_bytes / task_latency_sec / BYTES_PER_GB
/tmp/DejaVu/Decentralized_FM_alpha/unit_tests/io_test.py:    print(f'Task {io_string} Latency = {task_latency_sec} sec')
/tmp/DejaVu/Decentralized_FM_alpha/unit_tests/io_test.py:    e2e_latency_sec = max([sec for sec, _, _ in pool_results])
/tmp/DejaVu/Decentralized_FM_alpha/unit_tests/io_test.py:    e2e_speed_GB = total_bytes / e2e_latency_sec / BYTES_PER_GB
/tmp/DejaVu/Decentralized_FM_alpha/unit_tests/io_test.py:    print(f'E2E {io_string} Latency = {e2e_latency_sec} sec')
/tmp/DejaVu/Decentralized_FM_alpha/unit_tests/API_tests/performance_test.py:                      f"latency: {returned_payload['raw_compute_time']}")
/tmp/DejaVu/Decentralized_FM_alpha/unit_tests/API_tests/performance_test.py:                      f"latency: {returned_payload['raw_compute_time']} s, "
/tmp/DejaVu/Decentralized_FM_alpha/unit_tests/API_tests/performance_test.py:                      f"throughput: {args.max_tokens*args.prompt_num/returned_payload['raw_compute_time']} token/s")
/tmp/DejaVu/Decentralized_FM_alpha/pipeline_parallel/dist_hybrid_inference_greedy_token_async_deprecated.py:            print("Estimated token throughput for myself: {:3.2f} token/second".format(token_tp))
/tmp/DejaVu/Decentralized_FM_alpha/local_latency_inference_nlp_w_httpclient.py:        print('Exception in latency inference:', e)
/tmp/DejaVu/Decentralized_FM_alpha/dist_latency_parallelformers_w_httpclient.py:        print('Exception in latency inference:', e)
/tmp/DejaVu/Decentralized_FM_alpha/dist_latency_glm_inference_w_httpclient.py:        print('Exception in latency inference:', e)
/tmp/DejaVu/Decentralized_FM_alpha/dist_latency_auto_batch_inference_w_httpclient.py:    n_pads = 0  # in latency inference, #pad should be 0
/tmp/DejaVu/Decentralized_FM_alpha/dis
…[truncated 755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-19T02:57:42.237623+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/CATS /tmp/TEAL /tmp/DejaVu -name \"README*\" -o -name \"*.md\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/CATS /tmp/TEAL /tmp/DejaVu -name \"README*\" -o -name \"*.md\" | head -10"
  }
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-19T02:57:42.237752+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/CATS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/CATS"
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-19T02:57:42.237868+00:00_

EISDIR: illegal operation on a directory, read '/tmp/CATS'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-19T02:57:42.237979+00:00_

/tmp/CATS/flash_gemv/README.md
/tmp/CATS/README.md
/tmp/TEAL/gpt-fast/mixtral-moe/README.md
/tmp/TEAL/gpt-fast/README.md
/tmp/TEAL/gpt-fast/CONTRIBUTING.md
/tmp/TEAL/gpt-fast/CODE_OF_CONDUCT.md
/tmp/TEAL/README.md
/tmp/DejaVu/sparse_predictor/README.md
/tmp/DejaVu/lm-eval-harness-adapter/README.md
/tmp/DejaVu/README.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-19T02:57:42.238140+00:00_

# R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference

## Project Summary

R-Sparse is a training-free activation sparsity method designed to optimize Large Language Model inference. According to the repository, the approach "achieves comparable performance at 50% model-level sparsity, resulting in a significant 43% end-to-end efficient improvements with customized kernels."

## Key Innovation

The method makes two core observations about linear layer computations:

1. Non-sparse input components can be approximated as bias terms
2. Full computation can be effectively approximated "by an appropriate combination of input channels and weight singular values"

This enables sparsity without requiring active channel prediction, addressing limitations of previous output-sparsity approaches that struggle with non-ReLU activation functions common in modern LLMs.

## Technical Implementation

The repository includes:
- **Language**: Primarily Python (85%) with CUDA components (13.8%)
- **Tested Models**: Llama-2/3 and Mistral architectures
- **Evaluation**: Ten diverse benchmark tasks
- **Infrastructure**: Triton kernel implementations and customized inference kernels

## Getting Started

Environment setup uses conda, with example benchmarking available via provided scripts targeting Llama3-8b.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-19T02:57:42.238284+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/CATS/README.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/CATS/README.md"
  }
}
```

</details>

---

### Tool call

_source line 203 · 2026-05-19T02:57:42.238409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/TEAL/README.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/TEAL/README.md"
  }
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-19T02:57:42.238538+00:00_

1	# CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models
2	
3	Welcome to the official implementation of [CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models](https://arxiv.org/pdf/2404.08763). We are thrilled to announce that our paper has been accepted for presentation at [COLM 2024](https://colmweb.org/index.html)!
4	
5	If you find our work useful in your research, please consider citing our paper:
6	
7	```
8	@article{lee2024cats,
9	  title={CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},
10	  author={Lee, Je-Yong and Lee, Donghyun and Zhang, Genghan and Tiwari, Mo and Mirhoseini, Azalia},
11	  journal={arXiv preprint arXiv:2404.08763},
12	  year={2024}
13	}
14	```
15	
16	## Overview
17	
18	Our paper, "CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models," introduces CATS—a new method aimed at reducing the computational demands of deploying LLMs without sacrificing their performance on downstream tasks. This method centers around a novel activation function that enhances activation sparsity effectively and efficiently.
19	
20	The CATS approach can be applied to various base models such as Mistral-7B and Llama2-7B, demonstrating a minimal performance drop (within 1-2% of the base models) even at 50% activation sparsity levels. Importantly, CATS not only accelerates convergence but also integrates a custom GPU kernel that enhances inference speeds by approximately 15%.
21	
22	## Reproducing Results
23	
24	To reproduce the experimental results and figures presented in our work, please follow the steps outlined below. The process has been simplified into a single script to ensure ease of use and to maintain consistency across different environments.
25	
26	### Prerequisites
27	
28	Ensure you have the following prerequisites installed:
29	
30	- Bash shell (Unix/Linux/Mac)
31	- Required Python packages (listed in `requirements.txt`)
32	- Set an `accelerate` configuration 
…[truncated 610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-19T02:57:42.238707+00:00_

1	# Training-Free Acivation Sparsity in Large Language Models
2	
3	[[Paper](https://www.arxiv.org/abs/2408.14690)][[Blog](https://www.together.ai/blog/teal-training-free-activation-sparsity-in-large-language-models)]
4	
5	
6	TEAL induces up to 40-50% model-wide activation sparsity in modern LLMs with minimal degradation, resulting in an up to 1.53-1.8x speedup in single-batch decoding.
7	
8	&lt;div align="center">
9	    &lt;img src="figures/clickbait.png" width="500" height="auto"/>
10	  &lt;/a>
11	&lt;/div>
12	
13	The current release supports:
14	- FP16 inference for Llama-2/3 models using uniform sparsities
15	- Accuracy evaluation for Llama-2/3 and Mistral models using uniform and block-wise greedy sparsities
16	
17	
18	## News
19	
20	- [01/2025] 🔥 TEAL is accepted to ICLR 2025 as a Spotlight!
21	- [08/2024] 🔥 Arxiv release!
22	
23	## Abstract
24	
25	Activation sparsity can enable practical inference speedups in large language models (LLMs) by reducing the compute and memory-movement required for matrix
26	multiplications during the forward pass. However, existing methods face limitations that inhibit widespread adoption. Some approaches are tailored towards
27	older models with ReLU-based sparsity, while others require extensive continued
28	pre-training on up to hundreds of billions of tokens. This paper describes TEAL
29	(**T**raining-Fre**e** **A**ctivation Sparsity in **L**LMs), a simple training-free method that
30	applies magnitude-based activation sparsity to hidden states throughout the entire
31	model. TEAL achieves 40-50% model-wide sparsity with minimal performance
32	degradation across Llama-2, Llama-3, and Mistral families, with sizes varying
33	from 7B to 70B. We improve existing sparse kernels and demonstrate wall-clock
34	decoding speed-ups of up to 1.53× and 1.8× at 40% and 50% model-wide sparsity.
35	TEAL is compatible with weight quantization, enabling further efficiency gains.
36	
37	
38	
39	## Contents
40	
41	- [Install](#Install)
42	- [Demo](#Demo)
43	
…[truncated 3784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-19T02:57:42.238872+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/DejaVu/README.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/DejaVu/README.md"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-19T02:57:42.239034+00:00_

1	# Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time
2	
3	Large language models (LLMs) with hundreds of billions of parameters have sparked a new wave of exciting AI applications. However, they are computationally expensive at inference time. Sparsity is a natural approach to reduce this cost, but existing methods either require costly retraining, have to forgo LLM’s in-context learning ability, or do not yield wall-clock time speedup on modern hardware. We hypothesize that contextual sparsity, which are small, input-dependent sets of attention heads and MLP parameters that yield approximately the same output as the dense model for a given input, can address these issues. We show that contextual sparsity exists, that it can be accurately predicted, and that we can exploit it to speed up LLM inference in wall-clock time without compromising LLM’s quality or in-context learning ability. Based on these insights, we propose DejaVu, a system that uses a low-cost algorithm to predict contextual sparsity on the fly given inputs to each layer, along with an asynchronous and hardware-aware implementation that speeds up LLM inference. We validate that DejaVu can reduce the inference latency of OPT-175B by over 2×
4	 compared to the state-of-the-art FasterTransformer, and over 6×
5	 compared to the widely used Hugging Face implementation, without compromising model quality. The code is available at https://github.com/FMInference/DejaVu.
6	
7	Paper Link: https://proceedings.mlr.press/v202/liu23am.html
8	
9	
10	This repo is consisting of three parts: (1) Training sparsity predictor (2) End-to-End Accuracy Benchmark (3) Generation Latency Benchmark.
11	
12	## Training sparsity predictor
13	We collect training data by running model inference using Decentralized_FM_alpha. 
14	
15	**Requirements**
16	
17	
18	```
19	    pip3 install --pre torch==1.12.0+cu113 -f https://download.pytorch.org/whl/torch_stable.html
20	    pip3 install cupy-cuda11x==11.0.0
21	    python3 
…[truncated 5745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 208 · 2026-05-19T02:57:42.239195+00:00_

Web search results for query: "site:github.com sparse autoencoder Triton decoder kernel topk"

Links: [{"title":"GitHub - corl-team/flexsae: Official Triton kernels for TopK and HierarchicalTopK Sparse Autoencoder decoders. · GitHub","url":"https://github.com/corl-team/flexsae"},{"title":"sparse-autoencoder · GitHub Topics · GitHub","url":"https://github.com/topics/sparse-autoencoder?o=desc&s=updated"},{"title":"sparse_autoencoder/sparse_autoencoder/train.py at main · openai/sparse_autoencoder","url":"https://github.com/openai/sparse_autoencoder/blob/main/sparse_autoencoder/train.py"},{"title":"sparse_autoencoder/sparse_autoencoder/kernels.py at main · openai/sparse_autoencoder","url":"https://github.com/openai/sparse_autoencoder/blob/main/sparse_autoencoder/kernels.py"},{"title":"corl-team · GitHub","url":"https://github.com/corl-team"},{"title":"GitHub - koayon/awesome-sparse-autoencoders: A curated reading list of research in Sparse Autoencoders, Feature Extraction and related topics in Mechanistic Interpretability","url":"https://github.com/koayon/awesome-sparse-autoencoders"},{"title":"GitHub - snooky23/K-Sparse-AutoEncoder: Sparse Auto Encoder and regular MNIST classification with mini batch's · GitHub","url":"https://github.com/snooky23/K-Sparse-AutoEncoder"},{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/pdf/2603.25011"},{"title":"BatchTopK Sparse Autoencoders","url":"https://arxiv.org/pdf/2412.06410"}]

Based on the search results, I found several relevant GitHub repositories related to your query:

## Primary Result

The main result is flexsae, which contains fused Triton implementations of the TopK and HierarchicalTopK sparse autoencoder (SAE) decoder losses from the corl-team. This work has been accepted to EMNLP 2025.

The repository includes a fast TopK kernel for SAE (slightly modified version from xformers) and fast HierarchicalTopK kernels, which can be found in the torch-ext/flex_sa
…[truncated 760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 209 · 2026-05-19T02:57:42.239355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ProSparse\" activation sparsity LLM GitHub 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ProSparse\" activation sparsity LLM GitHub 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-19T02:57:42.239490+00:00_

Web search results for query: "Triton GEMM sparse pattern block structured 2:4 sparsity kernel"

Links: [{"title":"Accelerating Sparse DNNs Based on Tiled GEMM","url":"https://arxiv.org/pdf/2402.10876"},{"title":"Accelerating Neural Network Training with Semi-Structured (2:4) Sparsity – PyTorch","url":"https://pytorch.org/blog/accelerating-neural-network-training/"},{"title":"Accelerating Transformer Pre-training with 2:4 Sparsity","url":"https://arxiv.org/html/2404.01847v3"},{"title":"An Efficient Sparse Inference Software Accelerator for ...","url":"https://arxiv.org/pdf/2306.16601"},{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/html/2603.25011"},{"title":"Accelerating Matrix Multiplication with Block Sparse Format and NVIDIA Tensor Cores | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/accelerating-matrix-multiplication-with-block-sparse-format-and-nvidia-tensor-cores/"},{"title":"Exploiting NVIDIA Ampere Structured Sparsity with cuSPARSELt | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/exploiting-ampere-structured-sparsity-with-cusparselt/"},{"title":"SparStencil: Retargeting Sparse Tensor Cores to Scientific Stencil Computations via Structured Sparsity Transformation","url":"https://arxiv.org/pdf/2506.22969"}]

Based on the search results, here's what I found about Triton GEMM sparse pattern block structured 2:4 sparsity kernels:

## Overview of 2:4 Sparsity

2:4 sparsity is a semi-structured sparsity pattern supported on NVIDIA Ampere architectures where a 2:4 sparse matrix partitions its elements into groups of four numbers, with each group having exactly two zeros.

## Performance Benefits

On the NVIDIA A100 GPU, the 2:4 pattern means out of every four elements, at least two must be zero, which reduces the data footprint and bandwidth of one matrix multiply (GEMM) operand by 2x and doubles throughput by skipping the computation of the zero values using ne
…[truncated 1043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-19T02:57:42.239643+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Q-Sparse\" quantized sparse LLM kernel GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Q-Sparse\" quantized sparse LLM kernel GitHub"
  }
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-19T02:57:42.239775+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CHESS channel-wise thresholding sparse LLM kernel GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CHESS channel-wise thresholding sparse LLM kernel GitHub"
  }
}
```

</details>

---

### Tool call

_source line 213 · 2026-05-19T02:57:42.239902+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Flash-LLM\" unstructured sparsity tensor cores GPU kernel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Flash-LLM\" unstructured sparsity tensor cores GPU kernel"
  }
}
```

</details>

---

### Tool result

_source line 214 · 2026-05-19T02:57:42.240050+00:00_

Web search results for query: ""sparse activation" "token-wise" OR "per-token" mask LLM kernel GitHub"

Links: [{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/pdf/2505.14884"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/html/2411.12692v1"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/pdf/2408.14690"},{"title":"GitHub - mit-han-lab/Block-Sparse-Attention: A sparse attention kernel supporting mix sparse patterns · GitHub","url":"https://github.com/mit-han-lab/Block-Sparse-Attention"},{"title":"CHESS: Optimizing LLM Inference via Channel-Wise Thresholding and   Selective Sparsification","url":"https://arxiv.org/pdf/2409.01366"},{"title":"Sparser Block-Sparse Attention via Token Permutation","url":"https://arxiv.org/html/2510.21270v1"}]

Here are the search results for "sparse activation" "token-wise" OR "per-token" mask LLM kernel GitHub:

## Key Findings:

**Sparse Activation and Attention Methods:**

1. **Polar Sparsity** - For a given input, only a small fraction of neurons contribute meaningfully at each decoding step. Several works explore token sparsity in attention, leveraging the fact that many tokens contribute little to model output.

2. **SparseInfer** - The XOR-based activation sparsity prediction method was implemented as a CUDA kernel to enable parallel processing on the GPU. SparseInfer was implemented on an open source LLM inference engine, llama.cpp.

3. **Block-Sparse Attention (GitHub)** - A library of sparse attention kernels that supports various sparse patterns, including streaming attention with token granularity, streaming attention with block granularity, and block-sparse attention. Available at: https://gi
…[truncated 818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 215 · 2026-05-19T02:57:42.240210+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/mit-han-lab/Block-Sparse-Attention",
  "prompt": "Block sparse attention kernel implementation, Triton CUDA, sparse patterns supported, speedups"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/mit-han-lab/Block-Sparse-Attention",
    "prompt": "Block sparse attention kernel implementation, Triton CUDA, sparse patterns supported, speedups"
  }
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-19T02:57:42.240343+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com \"Polar Sparsity\" OR \"TEAL sparse\" activation LLM inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com \"Polar Sparsity\" OR \"TEAL sparse\" activation LLM inference"
  }
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-19T02:57:42.240480+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com \"Flash-LLM\" OR \"TurboAttention\" OR \"PBSAttn\" sparse attention kernel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com \"Flash-LLM\" OR \"TurboAttention\" OR \"PBSAttn\" sparse attention kernel"
  }
}
```

</details>

---

### Tool result

_source line 218 · 2026-05-19T02:57:42.240619+00:00_

Web search results for query: "CHESS channel-wise thresholding sparse LLM kernel GitHub"

Links: [{"title":"CHESS: Optimizing LLM Inference via Channel-Wise Thresholding and Selective Sparsification | OpenReview","url":"https://openreview.net/forum?id=QeZwkjuq4J"},{"title":"CHESS : Optimizing LLM Inference via Channel-Wise Thresholding and Selective Sparsification","url":"https://arxiv.org/html/2409.01366v2"},{"title":"[2409.01366] CHESS: Optimizing LLM Inference via Channel-Wise Thresholding and Selective Sparsification","url":"https://arxiv.org/abs/2409.01366"},{"title":"CHESS: Optimizing LLM Inference via Channel-Wise Thresholding and   Selective Sparsification","url":"https://arxiv.org/pdf/2409.01366"},{"title":"[2409.01366v1] CHESS: Optimizing LLM Inference via Channel-Wise Thresholding and Selective Sparsification","url":"https://arxiv.org/abs/2409.01366v1"},{"title":"CHESS: Optimizing LLM Inference via Channel-Wise Thresholding and Selective Sparsification - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1038/"},{"title":"CHESS Optimizing LLM Inference via Channel-Wise Thresholding ...","url":"https://scholars.cityu.edu.hk/ws/portalfiles/portal/278715776/273194576.pdf"}]

Based on the search results, here's what I found about CHESS:

## Overview

CHESS is a general activation sparsification approach via CHannel-wise thrEsholding and Selective Sparsification.

## Key Components

The approach proposes channel-wise thresholding for FFN modules in LLMs, which determines a unique threshold for each activation channel. Furthermore, it proposes selective sparsification, which applies thresholding-based activation sparsification to the target layers in the attention module. Finally, it presents the implementations of sparse kernels to accelerate the inference based on the sparse activations.

## Performance

Experimental results demonstrate that CHESS can achieve lower performance degradation with better end-to-end inference speedup, with results show
…[truncated 244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-19T02:57:42.240847+00:00_

Web search results for query: ""Q-Sparse" quantized sparse LLM kernel GitHub"

Links: [{"title":"GitHub - nanowell/Q-Sparse-LLM: My Implementation of Q-Sparse: All Large Language Models can be Fully Sparsely-Activated","url":"https://github.com/nanowell/Q-Sparse-LLM"},{"title":"Q-Sparse: All Large Language Models can be Fully Sparsely-Activated","url":"https://arxiv.org/pdf/2407.10969"},{"title":"GitHub - pprp/Awesome-LLM-Quantization: Awesome list for LLM quantization · GitHub","url":"https://github.com/pprp/Awesome-LLM-Quantization"},{"title":"Sparse, Quantize and Serving LLMs with NeuralMagic, AutoGPTQ and vLLM | by Vilson Rodrigues | Medium","url":"https://vilsonrodrigues.medium.com/sparse-quantize-and-serving-llms-with-neuralmagic-autogptq-and-vllm-03961b72ec3a"},{"title":"GitHub - Vahe1994/SpQR · GitHub","url":"https://github.com/Vahe1994/SpQR"},{"title":"SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression | OpenReview","url":"https://openreview.net/forum?id=Q1u25ahSuy"},{"title":"SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight   Compression","url":"https://arxiv.org/pdf/2306.03078"}]

Based on the web search results, here's what I found:

## Q-Sparse

Q-Sparse-LLM is an implementation of a sparse transformer architecture designed for efficient and high-performance language modeling. The main GitHub repository is located at: **https://github.com/nanowell/Q-Sparse-LLM**

Q-Sparse is a simple yet effective approach to enable full sparsity of activations in LLMs. For each linear projection, it has a top-K sparsification function that selects the top-K activations in the input tensor.

Key features include:
- Q-Sparse can be used with both full-precision and quantized LLMs.
- It introduces a quantized version of the top-K sparsity function that quantizes the input tensor to an 8-bit representation.
- It also introduces a squared ReLU function for the feed-forward layers to further improve the sparsity of the activa
…[truncated 247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-19T02:57:42.241082+00:00_

Web search results for query: ""ProSparse" activation sparsity LLM GitHub 2024 2025"

Links: [{"title":"[2402.13516] ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models","url":"https://arxiv.org/abs/2402.13516"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.180/"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models","url":"https://arxiv.org/html/2402.13516v1"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/prosparse-introducing-enhancing-intrinsic-activation-sparsity-within"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity","url":"https://arxiv.org/pdf/2402.13516"},{"title":"SparseLLM/prosparse-llama-2-7b · Hugging Face","url":"https://huggingface.co/SparseLLM/prosparse-llama-2-7b"},{"title":"GitHub - Raincleared-Song/sparse_gpu_operator: GPU operators for sparse tensor operations","url":"https://github.com/Raincleared-Song/sparse_gpu_operator"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation ...","url":"https://aclanthology.org/2025.coling-main.180.pdf"}]

Based on the search results, here's what I found about ProSparse:

## Overview

ProSparse is a sparsification method designed to push LLMs for higher activation sparsity while maintaining comparable performance. After substituting the activation function of LLMs with ReLU, ProSparse adopts progressive sparsity regularization with a factor smoothly increasing across multiple stages.

## Key Results

ProSparse achieved high sparsity of 89.32% for LLaMA2-7B, 88.80% for LLaMA2-13B, and 87.89% for MiniCPM-1B. These represent the most sparsely activated models among open-source LLaMA versions and competitive end-size mod
…[truncated 658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-19T02:57:42.241276+00:00_

Web search results for query: ""Flash-LLM" unstructured sparsity tensor cores GPU kernel"

Links: [{"title":"Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative   Model Inference with Unstructured Sparsity","url":"https://arxiv.org/pdf/2309.10285"},{"title":"Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative Model Inference with Unstructured Sparsity","url":"https://arxiv.org/html/2309.10285"},{"title":"[2309.10285] Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative Model Inference with Unstructured Sparsity","url":"https://ar5iv.labs.arxiv.org/html/2309.10285"},{"title":"Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative Model Inference With Unstructured Sparsity | by FSA Lab | Medium","url":"https://medium.com/@fsalab/flash-llm-enabling-cost-effective-and-highly-efficient-large-generative-model-inference-with-06ef6c586734"},{"title":"Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative Model Inference with Unstructured Sparsity","url":"https://www.researchgate.net/publication/376428517_Flash-LLM_Enabling_Cost-Effective_and_Highly-Efficient_Large_Generative_Model_Inference_with_Unstructured_Sparsity"},{"title":"[2309.10285] Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative Model Inference with Unstructured Sparsity","url":"https://arxiv.org/abs/2309.10285"},{"title":"Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative Model Inference with Unstructured Sparsity | Proceedings of the VLDB Endowment","url":"https://dl.acm.org/doi/abs/10.14778/3626292.3626303"},{"title":"Coruscant: Co-Designing GPU Kernel and Sparse Tensor Core to Advocate Unstructured Sparsity in Efficient LLM Inference | Proceedings of the 58th IEEE/ACM International Symposium on Microarchitecture","url":"https://dl.acm.org/doi/full/10.1145/3725843.3756065"}]

Based on the search results, here's what I found about Flash-LLM:

## Overview

Flash-LLM enab
…[truncated 1302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-19T02:57:42.241450+00:00_

Web search results for query: "site:github.com "Polar Sparsity" OR "TEAL sparse" activation LLM inference"

Links: [{"title":"[PDF] Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Polar-Sparsity:-High-Throughput-Batched-LLM-with-Shrestha-Settlemyer/328fcf757fa9647ea5eb96d37ee735e52a43df43"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2408.14690v1"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/pdf/2408.14690"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with ...","url":"https://susavlsh10.github.io/files/Polar_Sparsity_NeurIPS_2025_CameraReady.pdf"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://arxiv.org/pdf/2505.14884"},{"title":"La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation","url":"https://arxiv.org/html/2507.01299"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884v2"},{"title":"Polar Sparsity: High Throughput Batched LLM","url":"https://openreview.net/pdf?id=cg2S1qqNSq"},{"title":"training-free activation sparsity in large language models","url":"https://www.arxiv.org/pdf/2408.14690"}]

Based on the search results, I found information about both Polar Sparsity and TEAL sparse activation methods for LLM inference:

## TEAL (Training-Free Activation Sparsity in LLMs)

TEAL is a simple training-free method that applies magnitude-based activation sparsity to hidden states throughout the entire model. TEAL achieves 40-50% model-wide sparsity with minimal performance degradation across Llama-2, Llama-3, and Mistral families, with sizes varying from 7B to 70B. It demonstrates wall-clock decoding speed-ups of up to 1.53× and 1.8× at 40% and 50% model-wide sparsity.

## Polar Sparsity
…[truncated 755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 223 · 2026-05-19T02:57:42.241610+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sparser faster lighter transformer LLM sparse kernel 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sparser faster lighter transformer LLM sparse kernel 2025"
  }
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-19T02:57:42.241747+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SpInfer\" sparse inference kernel LLM unstructured GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SpInfer\" sparse inference kernel LLM unstructured GitHub"
  }
}
```

</details>

---

### Tool call

_source line 225 · 2026-05-19T02:57:42.241882+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Coruscant\" sparse tensor core LLM kernel GPU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Coruscant\" sparse tensor core LLM kernel GPU"
  }
}
```

</details>

---

### Tool result

_source line 226 · 2026-05-19T02:57:42.242005+00:00_

# Block Sparse Attention Overview

**Block Sparse Attention** is a library from MIT-HAN-Lab that provides optimized sparse attention kernels for large language models. The project addresses computational efficiency challenges in LLMs by leveraging sparsity patterns in attention mechanisms.

## Key Features

The library supports four attention patterns, with the ability to mix patterns across different heads:

1. **Dense attention** - Standard full attention matrix calculation
2. **Token-level streaming** - Fixed sink and local tokens (inspired by StreamingLLM)
3. **Block-level streaming** - Fixed sink and local blocks (128-token blocks)
4. **Block-sparse attention** - Custom block masks for sparse patterns

As the developers note, "by fully leveraging the inherent sparsity in attention patterns, we can optimize the model's performance, effectively reducing inference costs."

## Performance

The implementation demonstrates significant speedups over FlashAttention 2.4.2 on A100 GPUs. For hybrid scenarios combining dense and streaming masks across heads, the approach achieves substantial performance improvements for long-context inference.

## Technical Specifications

- **Requirements**: CUDA 11.6+, PyTorch 1.12+, Linux
- **Supported data types**: FP16, BF16 (Ampere+ GPUs)
- **Head dimensions**: 32, 64, 128
- **Latest updates**: Support for Hopper (H100) and Blackwell (B200) GPUs added in 2025

The codebase builds upon FlashAttention 2.4.2 and includes both forward and backward pass implementations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-19T02:57:42.242180+00:00_

Web search results for query: "site:github.com "Flash-LLM" OR "TurboAttention" OR "PBSAttn" sparse attention kernel"

Links: [{"title":"Sparser Block-Sparse Attention via Token Permutation","url":"https://arxiv.org/pdf/2510.21270"},{"title":"GitHub - xinghaow99/pbs-attn: Sparser Block-Sparse Attention via Token Permutation","url":"https://github.com/xinghaow99/pbs-attn"},{"title":"TurboAttention: Efficient Attention Approximation For High Throughputs   LLMs","url":"https://arxiv.org/pdf/2412.08585"},{"title":"GitHub - HKUSTDial/flash-sparse-attention: Trainable fast and memory-efficient sparse attention · GitHub","url":"https://github.com/flash-algo/flash-sparse-attention"},{"title":"GitHub - mit-han-lab/Block-Sparse-Attention: A sparse attention kernel supporting mix sparse patterns · GitHub","url":"https://github.com/mit-han-lab/Block-Sparse-Attention"},{"title":"GitHub - xlite-dev/Awesome-LLM-Inference: 📚A curated list of Awesome LLM/VLM Inference Papers with Codes: Flash-Attention, Paged-Attention, WINT8/4, Parallelism, etc.🎉","url":"https://github.com/xlite-dev/Awesome-LLM-Inference"},{"title":"GitHub - Relaxed-System-Lab/Flash-Sparse-Attention: 🚀🚀 Efficient implementations of Native Sparse Attention","url":"https://github.com/Relaxed-System-Lab/Flash-Sparse-Attention"},{"title":"FSA: An Alternative Efficient Implementation of Native Sparse Attention Kernel","url":"https://arxiv.org/pdf/2508.18224"},{"title":"Block Sparse Flash Attention","url":"https://arxiv.org/pdf/2512.07011"}]

Based on the search results, I found relevant information about these sparse attention methods:

## PBS-Attn (Permuted Block-Sparse Attention)

PBS-Attn is a plug-and-play method that leverages the permutation properties of attention to increase block-level sparsity and boost efficiency of LLM prefilling. The code is available at https://github.com/xinghaow99/pbs-attn. PBS-Attn achieves an end-to-end speedup of up to 2.75× in long-context prefilling.

## TurboAttention

TurboAttentio
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-19T02:57:42.242348+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/xinghaow99/pbs-attn",
  "prompt": "Permuted block sparse attention kernel implementation, Triton CUDA, sparse pattern, speedup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/xinghaow99/pbs-attn",
    "prompt": "Permuted block sparse attention kernel implementation, Triton CUDA, sparse pattern, speedup"
  }
}
```

</details>

---

### Tool call

_source line 229 · 2026-05-19T02:57:42.242484+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Relaxed-System-Lab/Flash-Sparse-Attention",
  "prompt": "Native sparse attention kernel Triton implementation, sparsity patterns, performance benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Relaxed-System-Lab/Flash-Sparse-Attention",
    "prompt": "Native sparse attention kernel Triton implementation, sparsity patterns, performance benchmarks"
  }
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-19T02:57:42.242613+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com openai sparse-autoencoder Triton kernel sparse matmul"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com openai sparse-autoencoder Triton kernel sparse matmul"
  }
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-19T02:57:42.242742+00:00_

Web search results for query: ""Coruscant" sparse tensor core LLM kernel GPU"

Links: [{"title":"Coruscant: Co-Designing GPU Kernel and Sparse Tensor Core to Advocate Unstructured Sparsity in Efficient LLM Inference | Proceedings of the 58th IEEE/ACM International Symposium on Microarchitecture","url":"https://dl.acm.org/doi/full/10.1145/3725843.3756065"},{"title":"GitHub - dhjoo98/coruscant: codebase for Coruscant: Co-Designing GPU Kernel and Sparse Tensor Core to Advocate Unstructured Sparsity in Efficient LLM Inference","url":"https://github.com/dhjoo98/coruscant"},{"title":"dhjoo98 (Joo Donghyeon) · GitHub","url":"https://github.com/dhjoo98"},{"title":"From Sparse Patterns to Smart Acceleration","url":"https://www.cs.umd.edu/class/fall2025/cmsc416/slides/Asgari-slides.pdf"},{"title":"Coruscant: Co-Designing GPU Kernel and Sparse Tensor ...","url":"https://dl.acm.org/doi/pdf/10.1145/3725843.3756065"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://openreview.net/pdf/3f12569e75bc44a8825d64bce1b98b485b326f52.pdf"},{"title":"Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative   Model Inference with Unstructured Sparsity","url":"https://arxiv.org/pdf/2309.10285"},{"title":"SlideSparse: Fast and Flexible (2N-2):2N Structured Sparsity","url":"https://arxiv.org/pdf/2603.05232"},{"title":"LUT Tensor Core: A Software-Hardware Co-Design for LUT-Based Low-Bit LLM Inference","url":"https://arxiv.org/pdf/2408.06003"}]

Based on the search results, here's what I found about Coruscant:

Coruscant is a system that co-designs GPU kernel and sparse tensor core to advocate unstructured sparsity in efficient LLM inference. 

**Key Features:**

Coruscant uses a bitmap-based sparse format and builds a GPU kernel upon it to unleash the benefits of unstructured sparsity across a wide range of sparsity levels on GPUs.

**Performance Benefits:**

The system helps harness unstructured sparsity in pruned LLMs to 
…[truncated 794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 232 · 2026-05-19T02:57:42.242889+00:00_

Web search results for query: "Sparser faster lighter transformer LLM sparse kernel 2025"

Links: [{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/html/2603.23198v1"},{"title":"GitHub - SakanaAI/sparser-faster-llms: Cuda kernels for leveraging LLM sparsity to improve throughput and decrease the memory requirements during inference and training. · GitHub","url":"https://github.com/SakanaAI/sparser-faster-llms"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/pdf/2603.23198"},{"title":"[2603.23198] Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/abs/2603.23198"},{"title":"[2603.23198v1] Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/abs/2603.23198v1"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://pub.sakana.ai/sparser-faster-llms/"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://sakana.ai/twell/"}]

Based on the search results, here's what I found about this topic:

This research tackles the vast computational costs of scaling large language models by leveraging unstructured sparsity within an LLM's feedforward layers, the components accounting for most of the model parameters and execution FLOPs.

The work introduces new kernels designed for modern NVIDIA GPUs to bridge this gap and leverage unstructured sparsity to deliver substantial speedups while reducing memory requirements and energy consumption during both LLM inference and training.

The research, titled "Sparser, Faster, Lighter Transformer Language Models," includes sparse training code and custom CUDA kernels designed for H100 GPUs for sparse models, leveraging the TwELL packing format.

Key results include:

- Simple L1 regularization can induce over 99% sparsity with negligible impact on downstream performance.
- Significant speedups ranging up to 30% are observed during batched inference across al
…[truncated 393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-19T02:57:42.243064+00:00_

Web search results for query: ""SpInfer" sparse inference kernel LLM unstructured GitHub"

Links: [{"title":"SpInfer: Leveraging Low-Level Sparsity for Efficient Large ...","url":"https://www.cse.ust.hk/~weiwa/papers/eurosys25-fall-spinfer.pdf"},{"title":"SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs - Consensus","url":"https://consensus.app/papers/spinfer-leveraging-lowlevel-sparsity-for-efficient-large-dong-fan/a5f33a6f14a256d2a1f4de05ae038d26/"},{"title":"SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs | Request PDF","url":"https://www.researchgate.net/publication/390315327_SpInfer_Leveraging_Low-Level_Sparsity_for_Efficient_Large_Language_Model_Inference_on_GPUs"},{"title":"SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs | Proceedings of the Twentieth European Conference on Computer Systems","url":"https://dl.acm.org/doi/10.1145/3689031.3717481"},{"title":"GitHub - chenhongyu2048/LLM-inference-optimization-paper: Summary of some awesome work for optimizing LLM inference · GitHub","url":"https://github.com/chenhongyu2048/LLM-inference-optimization-paper"},{"title":"GitHub - AlibabaResearch/flash-llm: Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative Model Inference with Unstructured Sparsity · GitHub","url":"https://github.com/AlibabaResearch/flash-llm"},{"title":"Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative   Model Inference with Unstructured Sparsity","url":"https://arxiv.org/pdf/2309.10285"}]

Based on the search results, here's what I found about SpInfer:

## Overview

SpInfer is a high-performance framework specifically designed to accelerate LLM inference by leveraging low-level unstructured sparsity on GPUs.

## Key Challenge

The primary challenge addressed is the storage overhead of indexing non-zero elements and the inefficiency of sparse matrix multiplication (SpMM) kern
…[truncated 899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-19T02:57:42.243219+00:00_

# Permuted Block-Sparse Attention (PBS-Attn)

## Overview

PBS-Attn is a research project introducing an efficient attention mechanism for large language models. According to the repository, it's "a plug-and-play method that leverages the permutation properties of attention to increase block-level sparsity and boost efficiency of LLM prefilling."

## Key Innovation

The approach uses token permutation within segments to reduce the number of blocks needed while maintaining important key token coverage, without breaking causal structure required for language models.

## Technical Details

The implementation is written primarily in Python (98.2%) with shell scripts for evaluation. It provides:

- A permuted block-sparse attention forward function compatible with HuggingFace models
- Integration with popular LLMs like Llama 3.1
- Evaluation frameworks for benchmarks including LongBench and efficiency testing
- Comparison baselines against Flash Attention, Minference, and other sparse attention methods

## Installation & Usage

The package supports one-line installation via pip, with optional dependencies for specific baselines. The README includes code examples showing how to patch transformer models for efficient prefilling.

## Status

The project cites an ICML 2026 publication, contains 29 stars on GitHub, and includes evaluation scripts for reproducibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-19T02:57:42.243357+00:00_

# Flash Sparse Attention Overview

**Flash Sparse Attention (FSA)** is an optimized implementation of Native Sparse Attention that improves efficiency on modern GPUs. The project is hosted at the Relaxed-System-Lab on GitHub.

## Key Innovation

FSA addresses a critical bottleneck in NSA by reversing the kernel loop order. Rather than looping over queries externally and KV blocks internally, FSA "loops over KV blocks in the outer loop and loops over query tokens in the inner loop." This architectural change significantly reduces unnecessary memory access and padding computations.

## Performance Advantages

The optimization proves particularly effective for smaller Grouped Query Attention (GQA) group sizes (under 8), which are common in state-of-the-art language models. Testing demonstrates FSA delivers meaningful speedups across varied configurations, though it falls back to NSA for larger group sizes where NSA performs better.

## Technical Scope

- **Supported Hardware**: NVIDIA Ampere and Hopper GPUs
- **Data Types**: fp16 and bf16
- **Head Dimensions**: Up to 256
- **GQA Group Sizes**: 1-16
- **Use Cases**: Training and inference (prefill)

## Code Structure

The implementation centers on the `FlashSparseAttention` class and underlying `FSATopkSparseAttention` operations, utilizing Triton for kernel development. The repository includes benchmarking tools and integration examples for LLM training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-19T02:57:42.243497+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "git clone --depth 1 https://github.com/VITA-Group/R-Sparse.git 2>&1 | head -10 && find /tmp -name \"R-Sparse\" -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "git clone --depth 1 https://github.com/VITA-Group/R-Sparse.git 2>&1 | head -10 && find /tmp -name \"R-Sparse\" -type d"
  }
}
```

</details>

---

### Tool call

_source line 237 · 2026-05-19T02:57:42.243625+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "git clone --depth 1 https://github.com/flashinfer-ai/flashinfer.git 2>&1 | tail -5 && ls -la /tmp/flashinfer 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "git clone --depth 1 https://github.com/flashinfer-ai/flashinfer.git 2>&1 | tail -5 && ls -la /tmp/flashinfer 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 238 · 2026-05-19T02:57:42.243742+00:00_

Cloning into 'R-Sparse'...
find: ‘/tmp/systemd-private-a8c3b138ffeb4fa28f9ef65cbc474bf3-fwupd.service-YaJbXY’: Permission denied
find: ‘/tmp/systemd-private-a8c3b138ffeb4fa28f9ef65cbc474bf3-ModemManager.service-fVA58V’: Permission denied
find: ‘/tmp/systemd-private-a8c3b138ffeb4fa28f9ef65cbc474bf3-systemd-logind.service-OPcjeE’: Permission denied
find: ‘/tmp/systemd-private-a8c3b138ffeb4fa28f9ef65cbc474bf3-polkit.service-oHyaiN’: Permission denied
find: ‘/tmp/systemd-private-a8c3b138ffeb4fa28f9ef65cbc474bf3-irqbalance.service-OmfTqI’: Permission denied
find: ‘/tmp/systemd-private-a8c3b138ffeb4fa28f9ef65cbc474bf3-chrony.service-WJe0JW’: Permission denied
find: ‘/tmp/snap-private-tmp’: Permission denied

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-19T02:57:42.243866+00:00_

Cloning into 'flashinfer'...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-19T02:57:42.243993+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/R-Sparse -name \"*.py\" -o -name \"*.cu\" -o -name \"*.cpp\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/R-Sparse -name \"*.py\" -o -name \"*.cu\" -o -name \"*.cpp\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool call

_source line 241 · 2026-05-19T02:57:42.244145+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/flashinfer -name \"*.py\" -type f 2>/dev/null | head -15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/flashinfer -name \"*.py\" -type f 2>/dev/null | head -15"
  }
}
```

</details>

---

### Tool result

_source line 242 · 2026-05-19T02:57:42.244260+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 243 · 2026-05-19T02:57:42.244367+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-19T02:57:42.244485+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "activation sparsity LLM inference kernel comparison survey 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "activation sparsity LLM inference kernel comparison survey 2025"
  }
}
```

</details>

---

### Tool call

_source line 245 · 2026-05-19T02:57:42.244605+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /tmp/CATS/flash_gemv/flash_gemv/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /tmp/CATS/flash_gemv/flash_gemv/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 246 · 2026-05-19T02:57:42.244713+00:00_

total 56
drwxr-xr-x 2 ubuntu ubuntu   100 May 19 02:54 .
drwxr-xr-x 7 ubuntu ubuntu   180 May 19 02:54 ..
-rw-r--r-- 1 ubuntu ubuntu  2582 May 19 02:54 __init__.py
-rw-r--r-- 1 ubuntu ubuntu  2219 May 19 02:54 flash_gemv.py
-rw-r--r-- 1 ubuntu ubuntu 47778 May 19 02:54 kernels.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-19T02:57:42.244844+00:00_

Web search results for query: "site:github.com openai sparse-autoencoder Triton kernel sparse matmul"

Links: [{"title":"sparse_autoencoder/sparse_autoencoder/kernels.py at main · openai/sparse_autoencoder","url":"https://github.com/openai/sparse_autoencoder/blob/main/sparse_autoencoder/kernels.py"},{"title":"sparse_autoencoder/sparse_autoencoder/train.py at main · openai/sparse_autoencoder","url":"https://github.com/openai/sparse_autoencoder/blob/main/sparse_autoencoder/train.py"},{"title":"GitHub - koayon/awesome-sparse-autoencoders: A curated reading list of research in Sparse Autoencoders, Feature Extraction and related topics in Mechanistic Interpretability","url":"https://github.com/koayon/awesome-sparse-autoencoders"},{"title":"sparse-autoencoder · GitHub Topics · GitHub","url":"https://github.com/topics/sparse-autoencoder"},{"title":"GitHub - rkinas/triton-resources: A curated list of resources for learning and exploring Triton, OpenAI's programming language for writing efficient GPU code. · GitHub","url":"https://github.com/rkinas/triton-resources"},{"title":"GitHub - openai/sparse_autoencoder · GitHub","url":"https://github.com/openai/sparse_autoencoder"},{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/pdf/2603.25011"},{"title":"sparse_autoencoder/README.md at main · openai/sparse_autoencoder","url":"https://github.com/openai/sparse_autoencoder/blob/main/README.md"}]

I found relevant results for your search about OpenAI's sparse autoencoder Triton kernels for sparse matrix multiplication.

The search returned several key findings:

1. **OpenAI's Sparse Autoencoder Repository**: The kernels.py file in the openai/sparse_autoencoder GitHub repository contains a `triton_sparse_transpose_dense_matmul` function that calculates sparse.T @ dense matrix multiplication.

2. **Kernel Implementation Details**: The kernel performs sparse matrix multiplication in COO-format (Coordinate format) with suppo
…[truncated 710 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-19T02:57:42.245050+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"activation sparsity\" OR \"sparse activation\" inference GPU kernel 2025 2024 GitHub open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"activation sparsity\" OR \"sparse activation\" inference GPU kernel 2025 2024 GitHub open source"
  }
}
```

</details>

---

### Tool call

_source line 249 · 2026-05-19T02:57:42.245200+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProSparse ProX inference sparse activation GPU kernel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProSparse ProX inference sparse activation GPU kernel"
  }
}
```

</details>

---

### Tool result

_source line 250 · 2026-05-19T02:57:42.245336+00:00_

Web search results for query: "activation sparsity LLM inference kernel comparison survey 2025"

Links: [{"title":"ENABLING DYNAMIC SPARSITY IN QUANTIZED LLM INFERENCE","url":"https://arxiv.org/pdf/2511.04477"},{"title":"Activation Sparsity","url":"https://www.aussieai.com/research/activation-sparsity"},{"title":"Weight-Aware Activation Sparsity with Constrained ...","url":"https://aclanthology.org/2025.emnlp-main.57.pdf"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/html/2411.12692v1"},{"title":"Accelerating LLM Inference Using Sparsity Kira Selby, Varun Khare NimbleEdge","url":"https://www.nimbleedge.com/sparsity-white-paper.pdf"},{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity","url":"https://arxiv.org/pdf/2602.14452"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/pdf/2504.19449"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"}]

Based on the web search results, here's what I found on activation sparsity for LLM inference with kernel comparisons and surveys from 2025:

## Key Research Areas

Network sparsification is primarily categorized into weight sparsity and activation sparsity, with recent research increasingly focused on data-dependent activation sparsity, which has shown superior performance and better scalability across diverse tasks.

## Recent Approaches and Comparisons

Several recent papers focus on activation sparsity optimization:

- **WiSparse**: At 50% sparsity, WiSparse preserves 97% of Llama3.1's dense model performance while achieving a 21.4% acceleration in end-to-end inference speed.

- **R-Sparse**: R-Sparse achieves comparable performance at 50% model-level sparsity, resulting in a 43% end-to-end efficient improvements with customized kernels on Llama-2/3 and Mistral mo
…[truncated 836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-19T02:57:42.245482+00:00_

Web search results for query: "ProSparse ProX inference sparse activation GPU kernel"

Links: [{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models","url":"https://arxiv.org/html/2402.13516v7"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/html/2411.12692v2"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity","url":"https://arxiv.org/pdf/2402.13516"},{"title":"SparseLLM/prosparse-llama-2-7b · Hugging Face","url":"https://huggingface.co/SparseLLM/prosparse-llama-2-7b"},{"title":"GitHub - Raincleared-Song/sparse_gpu_operator: GPU operators for sparse tensor operations","url":"https://github.com/Raincleared-Song/sparse_gpu_operator"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation ...","url":"https://aclanthology.org/2025.coling-main.180.pdf"},{"title":"ProSparse: Introducing and Enhancing Intrinsic","url":"https://arxiv.org/pdf/2402.13516v4"}]

Based on the search results, here's what I found about ProSparse ProX inference sparse activation GPU kernel:

## Overview

ProSparse is a sparsification method designed to push LLMs for higher activation sparsity while maintaining comparable performance. By applying ProSparse to Swish-activated LLaMA2-7B, LLaMA2-13B, and MiniCPM-1B, ReLU-activated models are obtained with high sparsity of 89.32%, 88.80%, and 87.89%, respectively.

## GPU Kernels

Two hardware-efficient sparse GPU operators were implemented with system-level optimizations, such as operator fusion, coalesced memory access, and vectorization, thereby exploiting input-side and output-side sparsity. These GPU operators are tailored for ReLU-activated FFNs in LLMs.

Codes for Operator Step (2) and Operator Step (3) are included in kernel/formula_23_kernel.cu and kernel/formula_4_kernel.cu respectively.

## Accuracy Advantage

The sparse GPU operators provide faster accurate inference utilizing a
…[truncated 443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 252 · 2026-05-19T02:57:42.245633+00:00_

Web search results for query: ""activation sparsity" OR "sparse activation" inference GPU kernel 2025 2024 GitHub open source"

Links: [{"title":"GitHub - Raincleared-Song/sparse_gpu_operator: GPU operators for sparse tensor operations","url":"https://github.com/Raincleared-Song/sparse_gpu_operator"},{"title":"SNICIT: Accelerating Sparse Neural Network Inference via ...","url":"https://tsung-wei-huang.github.io/papers/2023-icpp.pdf"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"GitHub - SakanaAI/sparser-faster-llms: Cuda kernels for leveraging LLM sparsity to improve throughput and decrease the memory requirements during inference and training. · GitHub","url":"https://github.com/SakanaAI/sparser-faster-llms"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/pdf/2504.19449"},{"title":"GitHub - chenhongyu2048/LLM-inference-optimization-paper: Summary of some awesome work for optimizing LLM inference · GitHub","url":"https://github.com/chenhongyu2048/LLM-inference-optimization-paper"},{"title":"Enabling Dynamic Sparsity in Quantized LLM Inference","url":"https://arxiv.org/pdf/2511.04477"}]

Great! I found several relevant open-source projects and research work on activation sparsity for GPU inference. Here are the key findings:

## Open Source GPU Kernel Projects

**ProSparse/sparse_gpu_operator** - This repository contains GPU operators for sparse tensor operations that utilize activation sparsity for LLM inference acceleration, specifically tailored for ReLU-activated FFNs in LLMs.

**SakanaAI/sparser-faster-llms** - Provides CUDA kernels for leveraging LLM sparsity, including TwELL kernel implementations and a flex variant for non-uniform sparsity patterns.

**R-Sparse** - Achieves rank-aware activation sparsity for efficient LLM inference with 43% end-to-end efficiency improvements on Llama-2/3 and Mistral 
…[truncated 810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-19T02:57:42.245885+00:00_

Perfect! Now let me create a comprehensive report with all the findings. Let me compile the information:

Based on my thorough research of academic paper implementations for activation sparsity speedup in LLMs, here's a comprehensive analysis:

## COMPREHENSIVE RESEARCH REPORT: Activation Sparsity Kernels for LLM Inference

---

### 1. CATS (Context-Aware Token Sparsity)

**GitHub:** https://github.com/ScalingIntelligence/CATS

**Kernel Technology:**
- Custom CUDA kernels (not Triton)
- Implemented in `/flash_gemv/csrc/cuda/fuse_gemv_cmp_cuda.cu`
- Uses cooperative groups and warp-level reductions for efficient computation
- FP16-optimized with `half2` vector operations

**Sparsity Type Supported:**
- Magnitude-based activation sparsity on FFN layers
- Context-aware thresholding approach (input-dependent)
- Works with standard transformer architectures (Llama2, Mistral)

**Reported Speedups:**
- Approximately 15% inference speedup with custom GPU kernel
- Maintains performance within 1-2% of base models at 50% activation sparsity
- Compatible with fine-tuning (targets 1% of parameters for quick convergence)

**Code Quality Assessment:**
- Production-ready implementation
- Custom CUDA kernel is well-structured with thread-block tiling
- Includes benchmarking suite (`flash_gemv/bench/` directory)
- Paper accepted at COLM 2024, indicating peer-reviewed quality

---

### 2. Deja Vu (Contextual Sparsity for Efficient LLMs)

**GitHub:** https://github.com/FMInference/DejaVu

**Kernel Technology:**
- Triton kernels for sparse operations
- Key files: `/Dejavu/src/ops/triton/gather_gemv.py` and `att_out_gemv.py`
- Uses Triton autotune with multiple BLOCK_M/BLOCK_N configurations
- Supports batched and unbatched operations

**Sparsity Type Supported:**
- Context-aware structured sparsity (sparse attention heads and MLP parameters)
- Predicts sparse patterns per-input dynamically
- Combines both attention and FFN sparsity

**Reported Speedups:**
- 2x speedup vs. FasterTransfor
…[truncated 8269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Agent",
  "elapsed_ms": 29
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-19T02:57:42.246230+00:00_

Excellent! Now I have comprehensive data. Let me compile the final report.

## Comprehensive Research Report: Triton-Based Sparse Matmul Kernels for LLM Activation Sparsity

I've completed a thorough search for open-source Triton kernels and GPU implementations for sparse matrix multiplication focused on activation sparsity inference. Here are all the findings organized by category:

---

### ACTIVATION SPARSITY FOCUSED IMPLEMENTATIONS

#### 1. **CATS (Contextually-Aware Thresholding for Sparsity)**
- **GitHub**: https://github.com/ScalingIntelligence/CATS
- **Sparsity Type**: Activation sparsity with contextual thresholding
- **Kernel Type**: Custom GPU kernel (language not explicitly specified in repo)
- **Reported Speedup**: ~15% inference speedup on token generation
- **Performance**: 50% activation sparsity with only 1-2% performance degradation
- **Models**: Mistral-7B, Llama2-7B
- **Publication**: COLM 2024
- **Note**: Kernel details in `flash_gemv/` folder; needs direct repo inspection for implementation language

#### 2. **Deja Vu (Contextual Sparsity for Inference)**
- **GitHub**: https://github.com/FMInference/DejaVu
- **Sparsity Type**: Contextual sparsity (input-dependent attention heads and MLP parameters)
- **Implementation**: PyTorch with CUDA 11.3 and CUDA graph optimization
- **Reported Speedup**: 2x vs FasterTransformer, 6x vs Hugging Face (OPT-175B)
- **Publication**: ICML 2023 (oral presentation)
- **Note**: Uses asynchronous look-ahead mechanism exploiting residual connections

#### 3. **ProSparse (Intrinsic Activation Sparsity)**
- **GitHub**: https://github.com/Raincleared-Song/sparse_gpu_operator
- **Sparsity Type**: Unstructured activation sparsity in ReLU-activated FFNs
- **Kernel Type**: CUDA kernels with operator fusion
- **Kernel Files**:
  - `kernel/formula_23_kernel.cu` - Fused ReLU with output-side sparsity
  - `kernel/formula_4_kernel.cu` - Sparse matrix-vector multiplication (input-side)
- **Reported Speedup**: Step (2) up to 2.00-
…[truncated 14034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_sparse-kernel-survey_20260519T025318",
  "tool": "Agent",
  "elapsed_ms": 37
}
```

</details>

---

### Assistant

_source line 255 · 2026-05-19T02:57:42.246502+00:00_

调研完成，综合四路结果。以下是完整评估。

---

## Sparse Inference Kernel 方案评估

### 场景约束
- Unstructured activation sparsity, 30-50%, per-token dynamic mask
- SwiGLU FFN (非 ReLU)
- 模型: LLaMA-3.1-8B / Mistral-7B / Qwen-2.5-14B
- GPU: RTX PRO 6000 Blackwell
- DDL: 6 天

---

### 方案总览

| 方案 | 可行性 | 实现难度 | 预期 Speedup | 硬件兼容 | 时间估计 | GitHub |
|------|--------|---------|-------------|---------|---------|--------|
| **TEAL (Triton GEMV)** | **直接可用** | 低 (有现成 kernel) | 1.5x@40%, 1.8x@50% | Triton 通用 | **2-3 天** | [FasterDecoding/TEAL](https://github.com/FasterDecoding/TEAL) |
| R-Sparse | 可用 | 中 | 1.43x@50% | CUDA/Triton | 3-4 天 | [VITA-Group/R-Sparse](https://github.com/VITA-Group/R-Sparse) |
| ProSparse CUDA | 部分 (针对 ReLU) | 中 | 2-2.4x/step | CUDA | 4-5 天 | [Raincleared-Song/sparse_gpu_operator](https://github.com/Raincleared-Song/sparse_gpu_operator) |
| TwELL (SakanaAI) | 可用 | 中-高 | 1.2x (batch) | H100 优化 | 4-5 天 | [SakanaAI/sparser-faster-llms](https://github.com/SakanaAI/sparser-faster-llms) |
| CATS CUDA | 可用 | 中 | 1.15x | CUDA | 3-4 天 | [ScalingIntelligence/CATS](https://github.com/ScalingIntelligence/CATS) |
| Deja Vu (Triton) | 可用 | 中 | 2x (大模型) | Triton | 3-4 天 | [FMInference/DejaVu](https://github.com/FMInference/DejaVu) |
| PyTorch 2:4 | **不可用** | — | — | — | — | — |
| cuSPARSE | 不推荐 | 高 | 动态 mask 转换开销抵消收益 | — | — | — |
| DeepSparse | **已废弃** | — | — | — | — | — |
| PowerInfer | 不独立可用 | 高 (GPU-CPU 混合架构) | 大但不可移植 | — | — | — |

---

### 排除项说明

1. **PyTorch 2:4 semi-structured**: 仅支持静态 2:4 weight sparsity，不支持 unstructured dynamic activation sparsity
2. **cuSPARSE**: 每 token 需做 dense→sparse 格式转换，overhead 抵消 sparsity 收益
3. **cuBLAS**: 无 sparse GEMM，需走 cuSPARSELt（仅 2:4）
4. **DeepSparse**: Neural Magic 2025-06 停止维护，CPU-only
5. **PowerInfer**: 架构绑定（GPU-CPU hybrid + llama.cpp），kernel 不可独立提取

---

### 推荐方案：TEAL Triton Kernel

**理由：**
1. 我们的论文已经在用 "TEAL-style inference" 框架（predictor → mask → sparse FFN）
2. TEAL 的 Triton sparse GEMV kernel 直接支持 unstructured activation sparsity + dynamic per-token mask
3. ICLR 2025 Spotlight，代码质量高，有完整 benchmark
4. Triton kernel 跨 GPU 架构兼容（Blackwell 支持 Triton）
5. 实现路径最短：clone kernel → 接入我们的 predictor mask → benchmark

**关键文件：**
- `kernels/sparse_gemv.py` — Triton sparse GEMV kernel
- 支持 deterministic 和 atomic-add 两种变体
- FP16 精度（Triton BF16 atomic_add 有限制）

**预期数据：**
- 40% sparsity → ~1.5x wall-clock speedup
- 50% sparsity → ~1.8x wall-clock speedup
- 单 batch decoding 场景最优

---

### 实现步骤（6 天计划）

**Day 1-2: 集成 TEAL kernel**
1. Clone TEAL repo，提取 `kernels/sparse_gemv.py`
2. 适配我们的 predictor output（binary mask）→ TEAL sparse format
3. 替换 SwiGLU FFN forward 中的 dense matmul 为 sparse GEMV
4. 单层验证：sparse FFN output 与 dense FFN output 对齐（numerical check）

**Day 3-4: Benchmark**
5. Wall-clock latency benchmark：dense vs sparse，逐层 + 端到端
6. 扫 sparsity level: 30%, 40%, 50%
7. 扫模型: LLaMA-3.1-8B, Mistral-7B, Qwen-2.5-14B
8. 记录 throughput (tokens/s) 和 per-layer latency breakdown

**Day 5: 论文数据整合**
9. 制作 speedup table/figure
10. 写 experiments section 的 efficiency 段落

**Day 6: Buffer + 备选**
11. 如果 TEAL kernel 在 Blackwell 上有兼容问题，fallback 到手写简化版 Triton kernel（gather-based sparse matmul，~200 行）
12. 或参考 Deja Vu 的 `gather_gemv.py` 作为替代

---

### 备选方案优先级

如果 TEAL 遇阻：
1. **Deja Vu Triton kernel** (`gather_gemv.py`) — 同样是 Triton，gather-based sparse GEMV
2. **自写 Triton kernel** — 基于 scatter/gather pattern，核心逻辑 ~200 行
3. **R-Sparse** — ICLR 2025，有 CUDA kernel，但适配成本更高

### 论文可引用的 speedup 参考值

即使我们自己的 kernel 实测数据还没出，论文中可以引用同类工作的数据作为 "activation sparsity speedup 是 well-established" 的论据：
- TEAL: 1.53-1.8x (ICLR 2025)
- R-Sparse: 1.43x (ICLR 2025)
- ProSparse: 2-4.5x (COLING 2025, ReLU models)
- TwELL: 1.2x batch / 1.2x e2e (ICML 2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_sparse-kernel-survey_20260519T025318"
}
```

</details>

---
