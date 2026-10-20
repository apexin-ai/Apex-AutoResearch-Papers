# Research conversation: You are analyzing an ML paper for a distillation task. Fetch and deeply analyze this paper, then write a structured YAML

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a5012f467ffebcff9.jsonl`
- **Structured JSON:** [`fdbcc47264bfaa2a4369.json`](../../sessions/fd/fdbcc47264bfaa2a4369.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-20T04:44:02.838Z_

You are analyzing an ML paper for a distillation task. Fetch and deeply analyze this paper, then write a structured YAML file.

**Paper**: "Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity" (NeurIPS 2025, arXiv:2505.14884)
**paper_key**: `Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity`

**Steps**:
1. Use WebFetch to get the full paper from `https://arxiv.org/html/2505.14884v1` with prompt: "Extract the complete paper text including: abstract, introduction (full text), method section, experiment section (all tables and figures with captions), contribution statements, limitations, conclusion. Preserve all numerical results, table data, and figure descriptions."
2. Use WebFetch on `https://arxiv.org/abs/2505.14884` with prompt: "Extract the abstract, authors, and any metadata."
3. Analyze deeply:
   - Research: baselines, metrics, datasets, ablation dimensions, training recipe, method family
   - Positioning: core claim, key results, limitations, relation_to_us = "competitor" (we distill sparse SwiGLU patterns; Polar Sparsity does scalable contextual sparsity for batched inference - direct competitor)
   - Narrative: story type, hook, tension, key insight, argument chain, contribution framing, intro structure
   - Figures & Tables: full analysis per schema

4. Write YAML to `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/distill_tmp/polar_sparsity.yaml`

Use full YAML schema with research, positioning, narrative, figures, tables sections. Be thorough with numerical results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6c554a50-fdc1-49d2-883c-154465fd97fb",
  "agentId": "a5012f467ffebcff9",
  "type": "user",
  "uuid": "1d2cf0a9-0144-4132-ac63-2a514b4f8f5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T04:44:02.840Z_

```json
{
  "parentUuid": "1d2cf0a9-0144-4132-ac63-2a514b4f8f5c",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "6b525755-a83d-4e0d-8ece-cf2343322fb2",
  "timestamp": "2026-05-20T04:44:02.840Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-20T04:44:05.526Z_



I'll fetch the paper from both sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b525755-a83d-4e0d-8ece-cf2343322fb2",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDD9jY1TqNkfRpqD6x5M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e72422e6-10de-4ee6-a6cd-c7dce40b7609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMGWFrm3r2fzUyTD6FsCNM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9335,
      "cache_read_input_tokens": 8146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9335,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T04:44:05.603Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GUrHAMCdz1zhacnXmAj7YQ`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e72422e6-10de-4ee6-a6cd-c7dce40b7609",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDD9jY1TqNkfRpqD6x5M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed8d23b2-a3c6-473d-a247-cd1c74c35e6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMGWFrm3r2fzUyTD6FsCNM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9335,
      "cache_read_input_tokens": 8146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9335,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T04:44:05.606Z_

<details><summary>↩ Tool result · `toolu_01GUrHAMCdz1zhacnXmAj7YQ`</summary>

````text
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
  "parentUuid": "ed8d23b2-a3c6-473d-a247-cd1c74c35e6b",
  "isSidechain": true,
  "promptId": "6c554a50-fdc1-49d2-883c-154465fd97fb",
  "agentId": "a5012f467ffebcff9",
  "type": "user",
  "uuid": "0cd051fb-d7ed-4934-801d-9507519cca25",
  "sourceToolAssistantUUID": "ed8d23b2-a3c6-473d-a247-cd1c74c35e6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T04:44:10.236Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PL4fNvs8J91XExK6EbN9gE`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.14884v1",
  "prompt": "Extract the complete paper text including: abstract, introduction (full text), method section, experiment section (all tables and figures with captions), contribution statements, limitations, conclusion. Preserve all numerical results, table data, and figure descriptions. Include all section headings and subsection headings. Pay special attention to: 1) All baseline methods compared against, 2) All metrics used, 3) All datasets/benchmarks, 4) Hardware details, 5) Specific speedup numbers and accuracy numbers, 6) Figure and table captions with descriptions of what they show."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cd051fb-d7ed-4934-801d-9507519cca25",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDD9wb42P12kLeLC5wGQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0560ceb1-9927-4941-9997-d60271d90ada",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH2S2YjRNZef2hvRyYj9vt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 17481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T04:44:10.966Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013gMcfSmY3AfoSouvhVB1W4`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.14884",
  "prompt": "Extract the abstract, authors, title, submission date, and any metadata including subject categories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0560ceb1-9927-4941-9997-d60271d90ada",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDD9wb42P12kLeLC5wGQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c59905f5-c7d0-416d-a77c-0b410c52b085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH2S2YjRNZef2hvRyYj9vt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 17481,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1445
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 17481,
          "cache_creation_input_tokens": 1445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1445,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T04:44:15.577Z_

<details><summary>↩ Tool result · `toolu_013gMcfSmY3AfoSouvhVB1W4`</summary>

```text
# Paper Extraction Summary

**Title:** Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity

**Authors:** Susav Shrestha, Brad Settlemyer, Nikoli Dryden, Narasimha Reddy

**Submission Date:** May 20, 2025 (v1); Last revised November 11, 2025 (v3)

**Subject Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

**Abstract Summary:**
The paper addresses LLM inference acceleration through contextual sparsity. The key finding reveals a shift in sparsity importance from MLP to attention layers as batch sizes increase. The authors introduce "Selective Head Attention" with custom GPU kernels, achieving "up to 2.2× end-to-end speedups" on models including OPT, LLaMA variants, Qwen, and Mistral. They claim this represents the first successful application of contextual sparsity to large batch inference scenarios.

**Additional Metadata:**
- **Venue:** NeurIPS 2025
- **Paper Length:** 10 pages, 7 figures
- **License:** CC BY 4.0
- **Availability:** Code repository referenced; PDF and HTML versions available on arXiv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c59905f5-c7d0-416d-a77c-0b410c52b085",
  "isSidechain": true,
  "promptId": "6c554a50-fdc1-49d2-883c-154465fd97fb",
  "agentId": "a5012f467ffebcff9",
  "type": "user",
  "uuid": "d725f197-e87a-42b8-9be0-33cf1cc7b13d",
  "sourceToolAssistantUUID": "c59905f5-c7d0-416d-a77c-0b410c52b085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T04:44:41.858Z_

<details><summary>↩ Tool result · `toolu_01PL4fNvs8J91XExK6EbN9gE`</summary>

```text
# Polar Sparsity: High Throughput Batched LLM Inferencing - Complete Summary

## Abstract

The paper introduces "Polar Sparsity," a technique for accelerating large language model inference during batched decoding. The authors identify a critical insight: as batch sizes and sequence lengths increase, the computational bottleneck shifts from MLP layers to attention layers. While MLP sparsity diminishes under batching due to union activation effects, attention head sparsity remains stable and batch-invariant. The method delivers "up to 2.2× end-to-end speedups" across OPT, LLaMA-2, and LLaMA-3 models without sacrificing accuracy.

## Key Contributions

1. **Observation on Sparsity Scaling**: Demonstrates that MLP activation sparsity degrades with batch size due to union activations, while attention head sparsity remains stable and batch-invariant.

2. **Custom GPU Kernels**: Develops Selective GEMM kernels with layer-wise top-k optimization achieving "up to 5.5× speedup" for dynamic MLP activations, and Selective FlashAttention kernels supporting head/group sparsity with "up to 2.8× speedup."

3. **Scalable to Large Batches**: First work demonstrating contextual sparsity effectiveness at large batch sizes, delivering substantial gains in high-throughput scenarios.

4. **Minimal Model Changes**: Integrates into existing LLMs without retraining, including models using non-ReLU activations.

## Introduction

Modern LLMs require efficient inference for real-world deployment. While sparsity and pruning are extensively studied, production use remains limited due to irregular memory access and poor hardware utilization. Recent contextual activation sparsity research shows promise—where input tokens dynamically activate only small neuron subsets—but prior work focused on single-query scenarios.

### Problem Analysis

The authors analyze inference in two stages: prefill (processing prompt) and decode (autoregressive generation). Decode dominates latency in practice. Their analysis of OPT-66b shows a critical shift: at small batch sizes, linear layers dominate; at scale, attention becomes the bottleneck. Figure 1 reveals that union neuron sparsity in MLPs diminishes with batching while attention computation grows linearly with batch size and sequence length.

## Method: Polar Sparsity

### 3.1 Accelerating MLP Layers

In decode, MLP input is a 3D tensor x ∈ ℝ^(B×1×d), where B is batch size and d is model dimension. Under contextual sparsity, only a subset S ⊆ [D] of D neurons activate per token.

The challenge: under batching, the union S_B (active neurons across all batch sequences) grows, reducing effective sparsity. Early layers maintain sparsity even at large batch sizes because per-token activation averages under 1%.

**Solution**: Use layer-wise top-k optimization with a lightweight two-layer router that predicts neuron activations. A dynamic top-k mechanism adapts the number of active neurons per layer to maintain 99% recall while minimizing computation.

### 3.2 Accelerating Attention Layers

During decode, attention input is x ∈ ℝ^(B×1×d). After QKV projections: Q ∈ ℝ^(B×H×1×d_h), K,V ∈ ℝ^(B×H_kv×N×d_h), where H is head count and N is sequence length.

**Key insight**: Unlike MLP sparsity, attention head sparsity is batch-invariant. Each sequence independently computes attention, so per-head sparsity remains consistent regardless of batch size.

The authors empirically validate this: activating only top-k heads by output L2 norm shows perplexity increases gradually. At 30% head activation, OPT-66b shows only 5% perplexity increase; at 50%, it increases by approximately 1%.

**Additional finding**: Layer 0 consistently exhibits highest importance; subsequent layers can apply uniform head sparsity.

## 4. Implementation: Polar Sparsity System

### 4.1 MLP Kernels

A custom GPU kernel fuses indexing and matrix multiplication (Algorithm 3), avoiding separate gather-scatter overhead. The kernel supports batched GEMM (not just GEMV like prior work) and achieves near-linear speedups: "up to 5.5× over dense baseline" at higher sparsity levels (Figure 3a shows approximately 4× speedup at 70% sparsity).

### 4.2 Attention Kernels

**Selective Head FlashAttention (SHA)**: Modifies FlashAttention to incorporate head sparsity by indexing into relevant heads during kernel initialization using a batch head index tensor. All memory access updated accordingly to read/write only active head data.

Algorithm 1 shows the decode process: for each batch b and top-k index k, retrieve actual head index from batch_head_index, load corresponding Q vector, iterate through K,V cache blocks, compute attention scores, accumulate results, and write to output using only activated head indices.

Results: "up to 2.8× improvement at 30% sparsity" over dense (Figure 3b shows approximately 2.5× at 70% sparsity).

**GQA Support**: For group query attention (as in LLaMA-3), applies group sparsity where query heads within a group share KV cache.

## 5. Evaluation

### 5.1 Benchmark Results

**Models Tested**: OPT (6.7B, 30B, 66B), LLaMA-2 (7B, 13B), LLaMA-3.1 (70B)

**Tasks**: Nine downstream tasks including COPA, OpenBookQA, PIQA, RTE, Winogrande, HellaSwag, MMLU, ARC-easy, ARC-challenging

**Training Data**: 400,000 token samples from WikiText-2 training dataset for router training

**Hardware**: NVIDIA DGX A100 80GB GPU nodes

**Sparsity Applied**:
- OPT models: Both MLP and attention sparsity
- LLaMA models: Attention sparsity only (Appendix B shows MLP benefits are limited)

**Critical Thresholds** (attention density where accuracy remains within ~1% of dense):
- OPT-66b: 30%
- OPT-6.7b, LLaMA-2 7B/13B: 50%
- LLaMA-3.1 70B: 62.5% (GQA has less diversity)

Table 1 shows accuracy at critical thresholds:
- OPT-66B maintains average accuracy within 1% at 30% density (0.560 vs 0.570)
- LLaMA-2 7B maintains accuracy within ~1.4% at 50% density (0.594 vs 0.608)
- LLaMA-3.1 70B shows 1.2% drop at 62.5% density (0.712 vs 0.724)

**Comparison with Prior Work** (Table 2, LLaMA-2-7B):
- Polar Sparsity competitive or superior to ProbePruning, ReLUfication, ProSparse, CATS, TEAL, GRIFFIN, R-Sparse
- Example: MMLU 5-shot shows 0.381 (Polar) vs 0.405 (TEAL) and 0.455 (ProSparse)

### 5.2 Throughput Results

**OPT-6.7B** (Figure 5a, seq_len=1920, critical threshold 50%):
- Batch 1: Similar to conventional sparsity
- Batch 64: 2× speedup over DejaVu, 1.83× over dense
- Demonstrates improved scaling compared to activation-only sparsity

**OPT-66B** (Figure 5b, seq_len=1920, critical threshold 30%):
- Batch 1: 1.66× speedup over dense
- Batch 64: 2.2× speedup over dense, 2× over DejaVu
- Shows significant advantage of attention sparsity at scale

**LLaMA-2 7B** (Figure 6a, seq_len=3968, critical threshold 50%):
- Attention-only sparsity
- Speedups increase with batch size, reaching 1.85× at larger batches

**LLaMA-3.1 70B** (Figure 6b, seq_len=8192, critical threshold 62.5%):
- Despite higher attention density requirement
- Achieves 1.51× speedup at large batch sizes

**Latency Analysis** (Appendix E.2):
- OPT models with batch 16, varying sequence length: "up to 2× speedup over dense, 1.52× over DejaVu"
- LLaMA models with batch 16: "up to 1.77× over dense"

**Tensor Parallel Results** (Appendix E.1.1, OPT-66B):
- TP degree 2: 1.8× speedup at larger batch sizes
- TP degree 4: Diminishing returns at small batches, 1.8× at large batches (due to workload division reducing per-GPU work)

## Architectural Differences and Design Choices

**Why Dense Attention at Layer 0**: Figure 2b shows layer 0 has consistently highest importance across models (OPT-6.7b, OPT-66b, LLaMA variants).

**Router Architecture**:
- MLP routers: Two-layer feedforward with 1024 hidden dimension
- Attention routers: Single-layer feedforward
- MLP router trained to predict neuron activations; attention router trained on binary classification of head importance
- Binary cross-entropy loss, AdamW optimizer, learning rate 1e-4

**Dynamic Top-k for MLPs**: Algorithm 2 shows greedy adjustment to meet 99% target recall, calibrated offline per model variant. Standard static top-k proved suboptimal for batched inference.

## Limitations and Future Work

1. **Diminishing Returns at Small Scale**: Benefits limited for small models or small-batch inference due to reduced GPU workload and parallelism.

2. **Fixed Head Selection**: Currently uses fixed top-k per layer; dynamic input or layer-adaptive strategies could improve efficiency.

3. **Minor Accuracy Drop**: Average 1% accuracy loss at critical thresholds; could potentially recover through fine-tuning.

4. **GQA Challenge**: Models with group query attention require higher density (62.5% for LLaMA-3.1) compared to full multi-head attention, limiting sparsity gains.

5. **Future Opportunities**:
   - Combine with token sparsity for multiplicative gains
   - Task-aware activation: allocate more heads to harder queries
   - Per-token difficulty: apply higher sparsity to easily-predicted tokens
   - Training models to induce inherent head sparsity

## Conclusion

The paper establishes that contextual sparsity scales effectively to large batches when properly targeted. By shifting focus from MLP sparsity (which degrades with batching) to attention head sparsity (which remains stable), Polar Sparsity delivers "2.2× end-to-end speedups" at scale with minimal accuracy impact. The work is the first to demonstrate contextual sparsity effectiveness at large batch sizes with custom GPU kernels enabling practical wall-clock improvements.

## Code and Reproducibility

Authors commit to releasing code and custom kernels at: https://github.com/susavlsh10/Polar-Sparsity

---

**Hardware Context**: All experiments on NVIDIA A100 GPUs; results scale to batch sizes up to 512 until GPU memory limits reached; pipeline parallelism used (most common for production inference).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0560ceb1-9927-4941-9997-d60271d90ada",
  "isSidechain": true,
  "promptId": "6c554a50-fdc1-49d2-883c-154465fd97fb",
  "agentId": "a5012f467ffebcff9",
  "type": "user",
  "uuid": "59a9442b-e3f5-4dbe-907b-78471089508b",
  "sourceToolAssistantUUID": "0560ceb1-9927-4941-9997-d60271d90ada",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-20T04:44:48.589Z_

Now let me fetch the figures for visual analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59a9442b-e3f5-4dbe-907b-78471089508b",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDDCcQUQXQcpa5oeA7vQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5095b4c1-6ad2-4bd1-9a97-9eb3bb3e6d02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMECX9Pom2bLYwG9zCVXra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 340,
      "cache_creation_input_tokens": 3170,
      "cache_read_input_tokens": 18926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3170,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T04:44:50.602Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LouSr5UUrKTuWNnwhAof2x`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.14884v1",
  "prompt": "List ALL figures and tables in the paper with their exact captions, figure/table numbers, and describe what each figure visually shows (chart type, axes, data series, visual layout). Also extract: 1) The exact contribution statements (usually bullet points in the intro), 2) The exact structure of the introduction (what each paragraph covers), 3) How many paragraphs in the intro, 4) The opening sentence of the paper, 5) Any related work section structure, 6) The exact numbers from Table 1 and Table 2 if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5095b4c1-6ad2-4bd1-9a97-9eb3bb3e6d02",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDDCcQUQXQcpa5oeA7vQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41b1c362-b71e-47f6-9623-628f97b465d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMECX9Pom2bLYwG9zCVXra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 340,
      "cache_creation_input_tokens": 3170,
      "cache_read_input_tokens": 18926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3170,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T04:45:16.621Z_

<details><summary>↩ Tool result · `toolu_01LouSr5UUrKTuWNnwhAof2x`</summary>

```text
# Polar Sparsity: Comprehensive Document Analysis

## OPENING SENTENCE
"Modern LLMs have emerged as powerful tools capable of excelling at diverse tasks, leading to their widespread adoption in modern systems."

## FIGURES AND TABLES

### Figure 1: OPT 66b Analysis
- **1(a) Decode Latency Breakdown**: Bar chart showing latency distribution across model components (Attention, MLP, QKV projection, output projection, others) on A100 GPUs with sequence length 1920
- **1(b) Batch Neuron Activations**: Line graph depicting union neuron sparsity decline as batch size increases with random sequences

### Figure 2: Head Sparsity Analysis
- **2(a) Head Sparsity vs Perplexity**: Line plots showing perplexity increases across multiple models (OPT variants, LLaMA) as attention density decreases
- **2(b) Attention Layer Importance**: Bar chart displaying per-layer importance scores across model families, highlighting layer 0's consistency

### Figure 3: Polar Sparsity Kernels
- **3(a) Select GEMM Kernel**: Line graph showing speedup vs sparsity percentage on A100, demonstrating near-linear scaling
- **3(b) Select FlashAttention Kernel**: Similar performance visualization for attention kernels at batch size 64, sequence length 1920

### Figure 4: Accuracy vs Attention Density
- Three subplots showing zero-shot accuracy across downstream tasks for OPT-66b, LLaMA-2-7b, and LLaMA-3.1-70b as attention density varies from 0-100%

### Figure 5: OPT Models Sparse Decoding Throughput
- **5(a) OPT-6.7b**: Throughput comparison (dense, DejaVu, Polar Sparsity) across batch sizes (1-256) at sequence length 1920
- **5(b) OPT-66b**: Similar throughput analysis showing up to 2.2× improvements at larger batch sizes

### Figure 6: LLaMA Models Sparse Decoding Throughput
- **6(a) LLaMA-2-7b**: Throughput vs batch size at sequence length 3968, critical threshold 50%
- **6(b) LLaMA-3.1-70b**: Throughput results at sequence length 8192, critical threshold 62.5%

### Figure 7: OPT Family Neuron Batch Activations (Appendix B)
- **7(a) OPT-6.7b**: Union neuron activation heatmap across layers and batch sizes
- **7(b) OPT-30b**: Similar activation pattern visualization

### Figure 8: LLaMA-2-7b Sparsified Models Neuron Batch Activations
- **8(a) ReLU LLaMA-2-7b**: Activation patterns after ReLU modification
- **8(b) ProSparse LLaMA-2-7b**: Activation patterns with ProSparse technique

### Figure 9: Head Activation Heat Maps (Appendix B)
- **9(a) OPT-6.7b**: Head usage distribution across layers (100,000 samples)
- **9(b) LLaMA-2-7b**: Comparable head activation patterns

### Figure 10: Router Ablation Study (Appendix C)
- Bar chart showing decode latency for MLP and Attention blocks with routers at different sparsity levels (batch 64, sequence 1920)

### Figure 11: Additional Throughput Results (Appendix E)
- **11(a) OPT-30b**: Throughput across batch sizes, critical density 40%
- **11(b) LLaMA-2-13b**: Performance metrics at 50% attention density

### Figure 12: Tensor Parallel Execution (Appendix E)
- **12(a) TP world size = 2**: OPT-66b throughput with tensor parallelism
- **12(b) TP world size = 4**: Similar analysis with increased tensor parallelism

### Figure 13: OPT Models Inter-Token Latency (Appendix E)
- **13(a) OPT-6.7b**: Inter-token latency vs sequence length (batch 16)
- **13(b) OPT-66b**: Similar latency analysis across sequence lengths

### Figure 14: LLaMA Models Inter-Token Latency (Appendix E)
- **14(a) LLaMA-2-7b**: Latency comparison across sequence lengths
- **14(b) LLaMA-3-70b**: Inter-token latency metrics

### TABLE 1: LLM Zero-Shot Evaluation at Critical Thresholds
Rows: OPT-6.7B, OPT-6.7B+PolarSparse-0.5, OPT-66B, OPT-66B+PolarSparse-0.3, LLaMA-2-7B, LLaMA-2-7B+PolarSparse-0.5, LLaMA-2-13B, LLaMA-2-13B+PolarSparse-0.5, LLaMA-3.1-70B, LLaMA-3.1-70B+PolarSparse-0.625

Columns: COPA, OpenBookQA, PIQA, RTE, Winogrande, HellaSwag, MMLU, ARC-E, ARC-C, Average

**Selected Data:**
- OPT-66B: Average 0.570; OPT-66B+PolarSparse: Average 0.560
- LLaMA-2-7B: Average 0.608; +PolarSparse: Average 0.594
- LLaMA-3.1-70B: Average 0.724; +PolarSparse: Average 0.712

### TABLE 2: Benchmark Results on LLaMA-2-7b
Rows: Dense baseline, ProbePruning-40%, ReLUfication, ProSparse, CATS-50%, TEAL-50%, GRIFFIN-50%, R-Sparse-50%, PolarSparse-50%

Columns: COPA, PIQA, Winogrande, HellaSwag, MMLU (5-shot), ARC-e, ARC-c

**Key Metrics:**
- Dense baseline: MMLU 0.458, Average across tasks competitive
- PolarSparse-50%: COPA 0.89, PIQA 0.779, MMLU 0.381

---

## EXACT CONTRIBUTION STATEMENTS

The paper presents four primary contributions:

1. "We show that activation sparsity in the MLP layers degrades with batch size due to union activations, while attention head sparsity remains stable and batch-invariant."

2. "We design Selective GEMM kernels with a layer-wise top-k optimization strategy for dynamic MLP activations, achieving up to 5.5× speedup."

3. "We introduce Selective FlashAttention kernels that support Head/Group sparsity with per-query activation, reducing memory I/O and compute, achieving up to 2.8× speedup."

4. "Polar Sparsity delivers up to 2.2× improvement in batched decoding throughput with negligible accuracy loss, and can be seamlessly integrated into a wide range of LLMs..."

---

## INTRODUCTION STRUCTURE

The introduction spans approximately **9 paragraphs**:

1. **Paragraph 1**: Opens with motivation about LLM deployment costs and computational expense
2. **Paragraph 2**: Discusses sparsity and pruning limitations in production, introducing contextual activation sparsity
3. **Paragraph 3**: States research gap—activation sparsity limited to single-query workloads despite modern systems depending on batching
4. **Paragraph 4**: Presents the key observation from Figure 1—attention dominates at scale while MLP sparsity diminishes with batching
5. **Paragraph 5**: Defines "Polar Sparsity" concept and explains the shift in optimization targets
6. **Paragraph 6**: Details the observation about stable attention head sparsity versus degrading MLP sparsity
7. **Paragraph 7**: Describes hardware-efficient kernel development
8. **Paragraph 8**: Claims about reproducibility and first demonstration of scalable contextual sparsity with batch size
9. **Paragraph 9**: Lists the four main contributions

---

## RELATED WORK SECTION STRUCTURE

**Section 2: Background and Related Works** (~2 pages)

- Overview of contextual sparsity in routers/MoE
- Early ReLU-based sparsity observations
- Recent activation function modifications (SwiGLU to ReLU returns)
- Token sparsity in attention mechanisms
- Comparison with prior head sparsity work (DejaVu, TEAL, MoA, MoH)
- Discussion of batch efficiency limitations in existing methods

**Appendix A: Extended Related Works** includes:
- A.1 Contextual Activation Sparsity
- A.2 Attention Head Sparsity and Token Sparsity

---

## ALGORITHMS PRESENTED

**Algorithm 1**: Selective Head FlashAttention (Decode)—modified FlashAttention incorporating head sparsity via batch_head_index tensor, 13 steps

**Algorithm 2**: Greedy Top-k Selection to Meet Target Recall—iterative k adjustment for MLP layers to achieve 99% recall, 9 steps

**Algorithm 3**: Sparse Fused GEMM Kernel—fused indexing and matrix multiplication for batched operations, 7 steps
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41b1c362-b71e-47f6-9623-628f97b465d1",
  "isSidechain": true,
  "promptId": "6c554a50-fdc1-49d2-883c-154465fd97fb",
  "agentId": "a5012f467ffebcff9",
  "type": "user",
  "uuid": "ee09b6e8-59f8-4e99-960f-04350b9c8ddc",
  "sourceToolAssistantUUID": "41b1c362-b71e-47f6-9623-628f97b465d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T04:45:27.760Z_

Now let me check if the distill_tmp directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee09b6e8-59f8-4e99-960f-04350b9c8ddc",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDDFAzb9MzqymTTiSaNR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f3a5ae0-0037-4626-a310-332878385cb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01842u7KuZzKy9MtDYZyhAuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2902,
      "cache_read_input_tokens": 22096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2902,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T04:45:29.728Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T4ZzNDag75qbhezcgkkJFQ`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/distill_tmp/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if distill_tmp directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f3a5ae0-0037-4626-a310-332878385cb9",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDDFAzb9MzqymTTiSaNR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "536b7f01-07f8-491a-99e5-215ba088bc3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01842u7KuZzKy9MtDYZyhAuu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2902,
      "cache_read_input_tokens": 22096,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 22096,
          "cache_creation_input_tokens": 2902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2902,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T04:45:29.777Z_

<details><summary>↩ Tool result · `toolu_01T4ZzNDag75qbhezcgkkJFQ`</summary>

```text
total 8
drwxr-xr-x  2 ubuntu ubuntu 4096 May 20 04:42 .
drwxr-xr-x 17 ubuntu ubuntu 4096 May 20 04:42 ..
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "536b7f01-07f8-491a-99e5-215ba088bc3f",
  "isSidechain": true,
  "promptId": "6c554a50-fdc1-49d2-883c-154465fd97fb",
  "agentId": "a5012f467ffebcff9",
  "type": "user",
  "uuid": "13890689-4614-46d6-9023-62e6b686964c",
  "sourceToolAssistantUUID": "536b7f01-07f8-491a-99e5-215ba088bc3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-20T04:45:33.258Z_

Good, the directory exists. Now I have all the information needed. Let me write the comprehensive YAML file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13890689-4614-46d6-9023-62e6b686964c",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDDG9P8jJYt5vMP7Cuog",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd1aabf2-64b2-474a-b986-d644a62502cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eu5sEhrraJZvdyW53ujL1h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 215,
      "cache_read_input_tokens": 24998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 215,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T04:46:50.961Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Y5NDHM3evCaafnPZzP9Wd9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/distill_tmp/polar_sparsity.yaml",
  "content": "paper_key: \"polar_sparsity\"\ntitle: \"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity\"\nvenue: \"NeurIPS 2025\"\nauthors: \"Susav Shrestha, Brad Settlemyer, Nikoli Dryden, Narasimha Reddy\"\narxiv_id: \"2505.14884\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - Dense (full model)\n    - DejaVu\n    - ProbePruning (40%)\n    - ReLUfication\n    - ProSparse\n    - CATS (50%)\n    - TEAL (50%)\n    - GRIFFIN (50%)\n    - R-Sparse (50%)\n  metrics:\n    - {name: \"Zero-shot accuracy (COPA, OpenBookQA, PIQA, RTE, Winogrande, HellaSwag, ARC-e, ARC-c)\", direction: \"higher_better\"}\n    - {name: \"MMLU 5-shot accuracy\", direction: \"higher_better\"}\n    - {name: \"Perplexity (WikiText-2)\", direction: \"lower_better\"}\n    - {name: \"Decoding throughput (tokens/sec)\", direction: \"higher_better\"}\n    - {name: \"Inter-token latency\", direction: \"lower_better\"}\n    - {name: \"End-to-end speedup vs dense\", direction: \"higher_better\"}\n    - {name: \"Kernel speedup vs dense GEMM/FlashAttention\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"WikiText-2\", size: \"400K token samples for router training\"}\n    - {name: \"COPA\", size: \"standard\"}\n    - {name: \"OpenBookQA\", size: \"standard\"}\n    - {name: \"PIQA\", size: \"standard\"}\n    - {name: \"RTE\", size: \"standard\"}\n    - {name: \"Winogrande\", size: \"standard\"}\n    - {name: \"HellaSwag\", size: \"standard\"}\n    - {name: \"MMLU\", size: \"standard, 5-shot\"}\n    - {name: \"ARC-easy\", size: \"standard\"}\n    - {name: \"ARC-challenge\", size: \"standard\"}\n  ablation_dimensions:\n    - \"Attention density threshold (30%-100%)\"\n    - \"MLP sparsity level\"\n    - \"Batch size scaling (1-512)\"\n    - \"Sequence length scaling\"\n    - \"Per-layer head importance (layer 0 dense vs uniform sparsity)\"\n    - \"Router overhead analysis\"\n    - \"Tensor parallel degree (1, 2, 4)\"\n    - \"Model family (OPT vs LLaMA-2 vs LLaMA-3.1)\"\n    - \"Attention type: MHA vs GQA impact on achievable sparsity\"\n  training_recipe:\n    router_architecture: \"MLP router: two-layer feedforward, 1024 hidden dim; Attention router: single-layer feedforward\"\n    router_training_data: \"400K token samples from WikiText-2 training set\"\n    router_loss: \"Binary cross-entropy\"\n    router_optimizer: \"AdamW, lr=1e-4\"\n    dynamic_topk_target: \"99% recall for MLP neurons\"\n    hardware: \"NVIDIA DGX A100 80GB GPUs\"\n    no_model_retraining: true\n  method_family: \"Contextual sparsity for inference acceleration (activation sparsity + attention head sparsity)\"\n\npositioning:\n  core_claim: \"MLP contextual sparsity degrades with batch size due to union activations, but attention head sparsity is batch-invariant; shifting optimization focus to attention heads enables the first scalable contextual sparsity system for high-throughput batched LLM inference.\"\n  key_results: |\n    End-to-end speedup: up to 2.2x over dense (OPT-66B, batch 64)\n    Selective GEMM kernel: up to 5.5x speedup for dynamic MLP activations\n    Selective FlashAttention kernel: up to 2.8x speedup for head-sparse attention\n    OPT-66B at 30% attention density: avg accuracy 0.560 vs 0.570 dense (-1.0%)\n    LLaMA-2-7B at 50% attention density: avg accuracy 0.594 vs 0.608 dense (-1.4%)\n    LLaMA-3.1-70B at 62.5% attention density: avg accuracy 0.712 vs 0.724 dense (-1.2%)\n    Throughput at batch 64: 2x over DejaVu, 1.83x over dense (OPT-6.7B)\n    LLaMA-3.1-70B: 1.51x speedup at large batch sizes despite higher density requirement\n  limitations:\n    - \"Diminishing returns at small model scale or small-batch inference due to reduced GPU workload\"\n    - \"Fixed top-k head selection per layer; dynamic input-adaptive strategies could improve efficiency\"\n    - \"Average ~1% accuracy loss at critical thresholds; could potentially recover with fine-tuning\"\n    - \"GQA models (LLaMA-3.1) require higher density (62.5%) than MHA models (30% for OPT-66B), limiting sparsity gains\"\n    - \"MLP sparsity benefits limited for non-ReLU models (LLaMA family); attention-only sparsity applied\"\n    - \"Router overhead not negligible at small batch sizes (Figure 10 shows latency contribution)\"\n  relation_to_us: \"competitor\"\n  # We distill sparse SwiGLU activation patterns into static masks; Polar Sparsity uses dynamic contextual\n  # sparsity with routers. Key difference: they show MLP sparsity degrades under batching (union activation\n  # problem), which is exactly the problem our static mask approach can address differently. Their attention\n  # head sparsity insight is orthogonal/complementary to our MLP-focused work. Their Table 2 directly\n  # compares against TEAL and R-Sparse which are also in our competitor set. Their finding that GQA limits\n  # sparsity gains is relevant to our work on modern architectures.\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Contextual sparsity is promising but fails to scale beyond single-query inference; real-world LLM serving requires batched decoding.\"\n  tension: |\n    Prior contextual sparsity work (DejaVu, CATS, TEAL, etc.) only demonstrated gains on single-query\n    inference. In production settings with batching, the union of activated MLP neurons across batch\n    elements erases sparsity gains. This creates a fundamental gap: the technique that works beautifully\n    at batch=1 becomes useless at production batch sizes.\n  key_insight: |\n    The paper reveals a \"polarity\" in sparsity behavior: MLP sparsity degrades with batch size (union\n    activation effect), while attention head sparsity remains stable and batch-invariant. This is because\n    each sequence computes attention independently, so per-head importance doesn't suffer from the union\n    problem. The insight is revealed through Figure 1 (latency breakdown showing attention dominance at\n    scale) and the batch neuron activation analysis. The name \"Polar\" captures this dichotomy.\n  argument_chain: |\n    1. LLM inference is expensive, sparsity is a promising acceleration path\n    2. Existing contextual sparsity only works at batch=1\n    3. Analysis reveals WHY: MLP union activations grow with batch size (Figure 1b)\n    4. But attention computation grows linearly AND head sparsity is batch-invariant\n    5. Therefore: shift optimization focus from MLP to attention heads\n    6. Design custom GPU kernels (Selective GEMM + Selective FlashAttention)\n    7. Validate across OPT, LLaMA-2, LLaMA-3.1 with minimal accuracy loss\n    8. Demonstrate first scalable contextual sparsity at large batch sizes (up to 2.2x)\n  contribution_framing: \"Four contributions listed as enumerated items: (1) empirical observation, (2) MLP kernel, (3) attention kernel, (4) end-to-end system with speedup claims\"\n  intro_structure: |\n    9 paragraphs:\n    P1: LLM deployment costs motivation\n    P2: Sparsity/pruning limitations, introduce contextual activation sparsity\n    P3: Research gap - activation sparsity limited to single-query\n    P4: Key observation from Figure 1 - attention dominates at scale\n    P5: Define \"Polar Sparsity\" concept\n    P6: Detail stable attention head sparsity vs degrading MLP sparsity\n    P7: Hardware-efficient kernel development\n    P8: Claims about first demonstration of scalable contextual sparsity\n    P9: Four contribution bullet points\n  notable_technique: |\n    The \"polarity\" framing is the strongest narrative device: by naming the paper after the observed\n    dichotomy (MLP sparsity degrades vs attention sparsity stable), they create a memorable conceptual\n    handle. The intro builds tension through a gap analysis (existing sparsity fails at scale) before\n    revealing the solution through empirical analysis rather than top-down design. Figure 1 is placed\n    very early (paragraph 4) to ground the argument in data immediately.\n\nfigures:\n  figure_count: 14  # including appendix figures\n  figure1:\n    type: \"motivation\"\n    description: |\n      Two-panel figure for OPT-66B. (a) Decode latency breakdown bar chart across batch sizes showing\n      component contributions (Attention, MLP, QKV projection, output projection, others) on A100 with\n      seq_len=1920. Shows attention dominating at larger batch sizes. (b) Line graph showing union neuron\n      sparsity decline as batch size increases with random sequences - demonstrates MLP sparsity erosion.\n    narrative_role: \"Establishes the core problem: MLP sparsity degrades with batching while attention becomes the bottleneck. This is THE motivating evidence for the entire paper.\"\n    design_elements:\n      - \"Side-by-side panels contrasting latency breakdown (a) with sparsity degradation (b)\"\n      - \"Stacked bar chart for component decomposition\"\n      - \"Line plot showing monotonic degradation trend\"\n      - \"Batch size as shared x-axis creating visual linkage\"\n    visual_style: \"Clean two-panel layout, standard academic colors, shared x-axis (batch size), clear axis labels\"\n\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Kernel speedup vs sparsity level for (a) Selective GEMM and (b) Selective FlashAttention\"\n      how_gain_highlighted: \"Shows near-linear speedup scaling with sparsity, demonstrating kernel efficiency\"\n      design_note: \"Separate panels for MLP and attention kernels; uses batch=64, seq=1920 as realistic production config\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Zero-shot accuracy across downstream tasks vs attention density for OPT-66B, LLaMA-2-7B, LLaMA-3.1-70B\"\n      how_gain_highlighted: \"Shows accuracy plateau before sharp degradation, identifying 'critical threshold' visually\"\n      design_note: \"Three subplots for different model families; multiple task lines allow readers to see variance across tasks\"\n    - figure_id: \"Figure 5\"\n      viz_type: \"line_plot\"\n      what_compared: \"Throughput (tokens/sec) vs batch size for dense, DejaVu, and Polar Sparsity on OPT-6.7B and OPT-66B\"\n      how_gain_highlighted: \"Polar Sparsity line diverges upward from baselines at larger batch sizes, visually emphasizing the scaling advantage\"\n      design_note: \"Two panels (6.7B and 66B) showing consistent pattern; DejaVu included as strongest prior baseline\"\n    - figure_id: \"Figure 6\"\n      viz_type: \"line_plot\"\n      what_compared: \"Throughput vs batch size for dense vs Polar Sparsity on LLaMA-2-7B and LLaMA-3.1-70B\"\n      how_gain_highlighted: \"Growing gap between dense and sparse lines at larger batch sizes\"\n      design_note: \"Demonstrates generalization to non-OPT architectures and GQA; no DejaVu baseline (doesn't apply to attention-only sparsity)\"\n\n  ablation_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"line_plot + bar_chart\"\n      dimensions_varied: [\"Head sparsity level vs perplexity across models\", \"Per-layer attention importance\"]\n      design_note: \"Two-panel: (a) perplexity degradation curves across models establish safe sparsity ranges; (b) bar chart of per-layer importance justifies dense layer-0 design choice\"\n    - figure_id: \"Figure 10 (Appendix C)\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"Router overhead at different sparsity levels for MLP and Attention blocks\"]\n      design_note: \"Stacked bars showing router latency as fraction of total; justifies router design is practical\"\n\n  figure_narrative_role: |\n    Figure 1 (motivation: MLP sparsity degrades, attention dominates)\n    -> Figure 2 (analysis: head sparsity is viable, layer-0 is special)\n    -> Figure 3 (kernel performance: custom kernels achieve near-linear speedup)\n    -> Figure 4 (accuracy: critical thresholds identified per model)\n    -> Figure 5-6 (throughput results: end-to-end speedup across models and batch sizes)\n    Flow: problem observation -> feasibility analysis -> implementation validation -> accuracy validation -> throughput validation\n\ntables:\n  table_count: 2  # main paper; additional in appendix\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"models (Dense vs PolarSparse at critical threshold)\"\n    col_axis: \"9 downstream tasks + average\"\n    row_organization: \"by_model_family\"\n    col_organization: \"flat (individual tasks + average)\"\n    highlight_strategy: \"Paired rows (dense/sparse) per model for direct comparison\"\n    statistical_reporting: \"Single-run numbers, no variance reported\"\n    num_baselines: 5  # 5 model variants, each with dense baseline\n    design_note: |\n      Clean paired-row design: each model has dense row immediately followed by PolarSparse row,\n      making accuracy drop instantly visible. Critical threshold noted in row label\n      (e.g., PolarSparse-0.3 for 30% density). Average column on far right for quick summary.\n      10 tasks is comprehensive but pushes table width.\n\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"Sparsity method (8 competitors + dense baseline)\"]\n      variation_style: \"full_numbers\"\n      design_note: |\n        Comparison table on LLaMA-2-7B specifically. All methods at 50% sparsity level\n        (where applicable). 7 tasks shown. Directly compares against TEAL, R-Sparse, CATS,\n        ProSparse, GRIFFIN, ReLUfication, ProbePruning. PolarSparse competitive but MMLU shows\n        weakness (0.381 vs 0.458 dense). Honest reporting of mixed results.\n\n  supplementary_tables:\n    in_appendix: true\n    content: \"Extended throughput results, tensor parallel results, latency breakdowns across sequence lengths\"\n    reason: \"Main paper focused on accuracy (Table 1) and method comparison (Table 2); throughput presented as figures rather than tables for visual impact\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd1aabf2-64b2-474a-b986-d644a62502cb",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDDG9P8jJYt5vMP7Cuog",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "267d51fe-c8f1-48c1-b050-35096f35793f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eu5sEhrraJZvdyW53ujL1h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 215,
      "cache_read_input_tokens": 24998,
      "output_tokens": 4101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 215
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4101,
          "cache_read_input_tokens": 24998,
          "cache_creation_input_tokens": 215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 215,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T04:46:50.972Z_

<details><summary>↩ Tool result · `toolu_01Y5NDHM3evCaafnPZzP9Wd9`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/distill_tmp/polar_sparsity.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "267d51fe-c8f1-48c1-b050-35096f35793f",
  "isSidechain": true,
  "promptId": "60b585a6-d8cb-4604-9cdc-913e61ff6276",
  "agentId": "a5012f467ffebcff9",
  "type": "user",
  "uuid": "e9031b81-eadd-40c1-b291-55f1321a1dfa",
  "sourceToolAssistantUUID": "267d51fe-c8f1-48c1-b050-35096f35793f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-20T04:47:00.354Z_

YAML written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/distill_tmp/polar_sparsity.yaml`.

Key findings from the deep analysis:

**Core relevance to our project**: Polar Sparsity is a direct competitor. Their central finding -- MLP contextual sparsity degrades with batch size due to union activations, while attention head sparsity remains batch-invariant -- is directly relevant to our distilled sparse SwiGLU work. They show the union activation problem is fundamental to dynamic MLP sparsity under batching, which is the exact problem our static mask approach addresses from a different angle.

**Competitive landscape**: Table 2 compares against TEAL, R-Sparse, CATS, ProSparse, GRIFFIN -- overlapping with our competitor set. Their solution shifts focus from MLP to attention heads, achieving 2.2x end-to-end speedup on OPT-66B at batch 64.

**Weaknesses we can exploit**: (1) GQA models require much higher density (62.5% for LLaMA-3.1 vs 30% for OPT-66B), limiting gains on modern architectures. (2) MMLU accuracy drops notably (0.381 vs 0.458 dense on LLaMA-2-7B). (3) No model retraining means no opportunity to recover accuracy. (4) MLP sparsity largely abandoned for non-ReLU models (LLaMA family uses attention-only).

**Narrative technique**: The "polarity" framing (MLP sparsity bad at scale, attention sparsity good) is memorable. Figure 1 placed in paragraph 4 of intro to ground the argument empirically before proposing the solution. 9-paragraph intro follows: motivation -> gap -> observation -> concept -> detail -> implementation -> claims -> contributions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9031b81-eadd-40c1-b291-55f1321a1dfa",
  "isSidechain": true,
  "agentId": "a5012f467ffebcff9",
  "requestId": "req_011CbDDN8KJf84Vy9vPNByzD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "635e860c-99d4-4433-bbd4-754c30be6210",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/distiller_ff4d142d",
  "sessionId": "b20cea17-0528-4150-82d3-639a719a1660",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5kQFYjnkdMdPjhozN62ax",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4161,
      "cache_read_input_tokens": 25213,
      "output_tokens": 445,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4161
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 445,
          "cache_read_input_tokens": 25213,
          "cache_creation_input_tokens": 4161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4161,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
