# research prophetkv survey v2

**distill kv rag cache** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_research_prophetkv-survey-v2_20260514T045403.jsonl`
- **Structured JSON:** [`bd3a6b37ac0311a8a801.json`](../../sessions/bd/bd3a6b37ac0311a8a801.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-14T04:59:55.485476+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch,WebSearch,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch,WebSearch,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T04:59:55.485863+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T04:59:55.486139+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.02579",
  "prompt": "Extract all technical details about ProphetKV: 1) Which layers' attention scores are used for prediction? 2) How is \"Expected Attention\" computed mathematically? 3) The full algorithm/procedure. 4) Any formulas for score computation. 5) Computational overhead analysis. 6) How token importance scores are generated."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2602.02579",
    "prompt": "Extract all technical details about ProphetKV: 1) Which layers' attention scores are used for prediction? 2) How is \"Expected Attention\" computed mathematically? 3) The full algorithm/procedure. 4) Any formulas for score computation. 5) Computational overhead analysis. 6) How token importance scores are generated."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T04:59:55.486286+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/FasterDecoding/SnapKV",
  "prompt": "Extract: 1) Repository structure and main files. 2) Core algorithm description. 3) How attention scores are collected and aggregated. 4) What is the \"observation window\" mechanism? 5) How it integrates with HuggingFace transformers. 6) Key code files to look at."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/FasterDecoding/SnapKV",
    "prompt": "Extract: 1) Repository structure and main files. 2) Core algorithm description. 3) How attention scores are collected and aggregated. 4) What is the \"observation window\" mechanism? 5) How it integrates with HuggingFace transformers. 6) Key code files to look at."
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T04:59:55.486622+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "kvpress NVIDIA KV cache compression library GitHub Python"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebSearch",
  "tool_args": {
    "query": "kvpress NVIDIA KV cache compression library GitHub Python"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T04:59:55.486788+00:00_

# ProphetKV Technical Details

Based on the provided arXiv page content, I cannot provide the specific technical details you requested. The webpage only contains metadata and an abstract for the paper arXiv:2602.02579.

## What's Available

The abstract mentions that ProphetKV:
- Uses "a dual-stage recomputation pipeline to fuse layer-wise attention metrics into a high-utility set"
- "Dynamically prioritizes tokens based on their semantic relevance to the user query"
- Achieves "96%-101% of full-prefill accuracy with only a 20% recomputation ratio"

## What's Missing

The webpage does not include:
1. Which specific layers' attention scores are used
2. Mathematical formulas for "Expected Attention" computation
3. The complete algorithm or procedure
4. Detailed score computation formulas
5. Computational overhead analysis details
6. Specific token importance score generation methods

To access these technical details, you would need to review the full paper PDF or HTML version available at the arxiv.org links provided on the page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T04:59:55.486944+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_kv_rag_cache",
  "file": "ARCHITECTURE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_kv_rag_cache",
    "file": "ARCHITECTURE.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T04:59:55.487080+00:00_

# SnapKV Repository Analysis

## 1) Repository Structure and Main Files
The repository contains:
- `snapkv/monkeypatch/` - Integration modules for different model architectures
- `experiments/LongBench/` - Benchmark testing directory
- `notebooks/` - Example usage notebooks
- `snapkv_utils.py` - Core algorithm implementation
- Support for Llama, Mistral, and Mixtral model families

## 2) Core Algorithm Description
SnapKV is described as an "innovative and out-of-box KV cache compression method." The project implements techniques to compress key-value caches in large language models, enabling more efficient long-context processing without requiring model retraining.

## 3) Attention Score Collection and Aggregation
The page references that "the detailed algorithm of SnapKV is in `snapkv_utils.py`" but doesn't provide specific details about score collection mechanisms in the visible content.

## 4) Observation Window Mechanism
No explicit information about an "observation window" mechanism appears in the provided webpage content.

## 5) HuggingFace Transformers Integration
SnapKV integrates via monkey-patching. Users call functions like `replace_mistral()` to enable compression. The implementation requires "transformers>=4.36" and "flash-attn==2.4.0" for compatibility.

## 6) Key Code Files
- `snapkv/monkeypatch/snapkv_utils.py` - Algorithm implementation
- `snapkv/monkeypatch/llama_hijack_4_37.py`, `mistral_hijack_4_37.py`, `mixtral_hijack_4_37.py` - Model-specific integration
- `notebooks/example.ipynb` - Practical usage examples

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T04:59:55.487278+00:00_

Web search results for query: "kvpress NVIDIA KV cache compression library GitHub Python"

Links: [{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"kvpress/kvpress/presses/composed_press.py at main · NVIDIA/kvpress","url":"https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/composed_press.py"},{"title":"GitHub - lloydchang/NVIDIA-kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/lloydchang/NVIDIA-kvpress"},{"title":"kvpress/kvpress/presses/expected_attention_press.py at main · NVIDIA/kvpress","url":"https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/expected_attention_press.py"},{"title":"GitHub - alessiodevoto/l2compress: Code for the EMNLP24 paper \"A simple and effective L2 norm based method for KV Cache compression.\"","url":"https://github.com/alessiodevoto/l2compress"},{"title":"GitHub - snu-mllab/KVzip: [NeurIPS'25 Oral] Query-agnostic KV cache eviction: 3–4× reduction in memory and 2× decrease in latency (Qwen3/2.5, Gemma3, LLaMA3)","url":"https://github.com/snu-mllab/KVzip"},{"title":"kvpress/kvpress/presses/base_press.py at main · NVIDIA/kvpress","url":"https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/base_press.py"},{"title":"[Feature] Integrate KVPress in order to try more KV cache optimization heuristics easily · Issue #10585 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/10585"},{"title":"kvpress/kvpress/presses/per_layer_compression_press.py at main · NVIDIA/kvpress","url":"https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/per_layer_compression_press.py"},{"title":"GitHub - Janghyun1230/FastKVzip: Accurate and fast KV cache compression with a gating mechanism · GitHub","url":"https://github.com/Janghyun1230/FastKVzip"}]

Based on the search results, I found comprehensive information about the KVPress library:

## KVPress Overview

KVPress is an NVIDIA library that addresses t
…[truncated 1380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T04:59:55.487460+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ARCHITECTURE.md found for 'distill_kv_rag_cache'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T04:59:55.487624+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2602.02579",
  "prompt": "Extract ALL technical details from this paper: 1) The exact mathematical formula for Expected Attention (EA). 2) Which layers are used for prediction (early layers vs later layers). 3) The dual-stage recomputation pipeline algorithm. 4) How token importance scores are computed - step by step. 5) The recomputation ratio and how it works. 6) Any pseudocode or algorithm listings. 7) How attention patterns from early layers predict later layer importance. 8) The computational cost analysis. 9) How the method selects which tokens to keep/evict."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2602.02579",
    "prompt": "Extract ALL technical details from this paper: 1) The exact mathematical formula for Expected Attention (EA). 2) Which layers are used for prediction (early layers vs later layers). 3) The dual-stage recomputation pipeline algorithm. 4) How token importance scores are computed - step by step. 5) The recomputation ratio and how it works. 6) Any pseudocode or algorithm listings. 7) How attention patterns from early layers predict later layer importance. 8) The computational cost analysis. 9) How the method selects which tokens to keep/evict."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T04:59:55.488656+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/FasterDecoding/SnapKV/main/snapkv/monkeypatch/snapkv_utils.py",
  "prompt": "Extract the complete code. Show: 1) How attention scores are collected. 2) The observation window implementation. 3) How scores are aggregated across heads. 4) The token selection/eviction logic. 5) Any pooling or kernel operations on attention weights. 6) The main function signatures and their parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/FasterDecoding/SnapKV/main/snapkv/monkeypatch/snapkv_utils.py",
    "prompt": "Extract the complete code. Show: 1) How attention scores are collected. 2) The observation window implementation. 3) How scores are aggregated across heads. 4) The token selection/eviction logic. 5) Any pooling or kernel operations on attention weights. 6) The main function signatures and their parameters."
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T04:59:55.489041+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/NVIDIA/kvpress/main/kvpress/presses/base_press.py",
  "prompt": "Extract the complete code. Show: 1) The BasePress class interface. 2) The hook mechanism - how it attaches to HuggingFace modules. 3) The score_to_mask or compression logic. 4) All abstract methods that subclasses must implement. 5) How compression_ratio is used. 6) The forward hook signature and flow."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/NVIDIA/kvpress/main/kvpress/presses/base_press.py",
    "prompt": "Extract the complete code. Show: 1) The BasePress class interface. 2) The hook mechanism - how it attaches to HuggingFace modules. 3) The score_to_mask or compression logic. 4) All abstract methods that subclasses must implement. 5) How compression_ratio is used. 6) The forward hook signature and flow."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T04:59:55.489209+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/NVIDIA/kvpress/main/kvpress/presses/expected_attention_press.py",
  "prompt": "Extract the complete code. Show: 1) How Expected Attention scores are computed. 2) The mathematical formula used. 3) How it extends BasePress. 4) Any attention weight processing. 5) How scores map to compression decisions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/NVIDIA/kvpress/main/kvpress/presses/expected_attention_press.py",
    "prompt": "Extract the complete code. Show: 1) How Expected Attention scores are computed. 2) The mathematical formula used. 3) How it extends BasePress. 4) Any attention weight processing. 5) How scores map to compression decisions."
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T04:59:55.489342+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_kv_rag_cache",
  "file": "ROADMAP.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_kv_rag_cache",
    "file": "ROADMAP.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T04:59:55.489623+00:00_

# SnapKV Attention Management: Code Analysis

## 1) Attention Score Collection
Attention scores are computed using query-key multiplication:
```python
attn_weights = torch.matmul(query_states[..., -self.window_size:, :], 
                             key_states.transpose(2, 3)) / math.sqrt(head_dim)
```
This calculates the "dot product between recent queries and all keys, normalized by head dimension."

## 2) Observation Window Implementation
The recent token window is preserved through slicing: `query_states[..., -self.window_size:, :]`. A causal mask ensures tokens only attend to previous positions:
```python
mask_cond = torch.arange(mask.size(-1), device=attn_weights.device)
mask.masked_fill_(mask_cond < (mask_cond + 1).view(mask.size(-1), 1), 0)
```

## 3) Score Aggregation Across Heads
Attention weights are summed over the query dimension for non-window tokens:
```python
attn_weights_sum = attn_weights[:, :, -self.window_size:, : -self.window_size].sum(dim=-2)
```
This "collapses attention patterns across all query positions within the recent window."

## 4) Token Selection/Eviction Logic
Top-k selection identifies important historical tokens:
```python
indices = attn_cache.topk(self.max_capacity_prompt - self.window_size, dim=-1).indices
```
Selected tokens are gathered while older tokens are discarded, maintaining a fixed cache size.

## 5) Pooling Operations
Two pooling methods aggregate scores:
```python
attn_cache = F.avg_pool1d(attn_weights_sum, kernel_size=self.kernel_size, 
                          padding=self.kernel_size//2, stride=1)
# or F.max_pool1d for max pooling
```

## 6) Function Signatures

**`update_kv(key_states, query_states, value_states, attention_mask, num_key_value_groups)`** — Main compression function triggered when sequence length exceeds `max_capacity_prompt`.

**`__init__(window_size=64, max_capacity_prompt=320, kernel_size=5, pooling='avgpool')`** — Initializes clustering with configurable cache constraints and pooling strategy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T04:59:55.489840+00:00_

# KVPress BasePress Class Analysis

## 1) BasePress Class Interface

The `BasePress` dataclass serves as the foundation for KV cache compression. Key methods include:

- `post_init_from_model(model)` - Optional initialization hook
- `compress(module, hidden_states, keys, values, attentions, kwargs)` - Abstract core logic
- `forward_hook(module, input, kwargs, output)` - Automatic compression application
- `__call__(model)` - Context manager for hook registration

## 2) Hook Mechanism

The system attaches to HuggingFace attention layers through PyTorch's forward hook registration:

```
for layer in language_model.layers:
    hooks.append(layer.self_attn.register_forward_hook(
        self.forward_hook, with_kwargs=True))
```

Hooks are automatically removed in a finally block when exiting the context manager, ensuring cleanup.

## 3) Compression Logic Flow

The `forward_hook` executes these steps:

- Checks if still in pre-filling phase: `if cache_position[-1] > q_len: return output`
- Extracts keys/values from cache using `extract_keys_and_values()`
- Calls `self.compress()` to reduce sequence length
- Updates cache in-place (handling both quantized and standard caches)

## 4) Abstract Methods for Subclasses

Only one method requires implementation:

- **`compress()`** - Must reduce cache tensors and "return a tuple containing the compressed keys and values tensors"

## 5) Compression Ratio Usage

**Not shown in this code**. The `compression_ratio` parameter appears in the docstring example (`KnormPress(compression_ratio=0.5)`) but is not implemented in `BasePress` itself—subclasses must define this.

## 6) Forward Hook Signature & Flow

**Signature**: `forward_hook(module, input, kwargs, output)`

**Flow**:
1. Extract hidden states and cache from kwargs
2. Validate pre-filling phase via cache_position
3. Extract keys/values from current layer cache
4. Invoke compress method with attention weights
5. Update cache_layer with compressed tensors
6. Return modified outp
…[truncated 2 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T04:59:55.490307+00:00_

# Expected Attention Press: KV Cache Compression Analysis

## 1) Expected Attention Score Computation

The `score()` method computes importance scores through these steps:

- Extracts query statistics (mean and covariance) from hidden states
- Applies averaged RoPE transformations to query distributions
- Calculates attention scores between mean queries and key vectors
- Optionally incorporates covariance information for variance-aware scoring
- Applies softmax normalization across key positions
- Rescales by value vector L2 norms to account for information magnitude
- Preserves sink tokens with maximum scores to prevent pruning

## 2) Mathematical Formula

The implementation follows this formula progression:

```
A = exp(Q @ K^T / √d)  [base attention]
E(A) = exp(K @ μ^T / √d + ½K @ Σ @ K^T / d)  [expected attention]
Final_scores = softmax(E(A)) × (ε + ||V||₂)  [rescaled]
```

Where μ represents the query mean, Σ is the query covariance matrix, and the average RoPE matrix R transforms these distributions across future positions.

## 3) Inheritance Structure

The class declaration shows: `class ExpectedAttentionPress(ScorerPress)` indicating inheritance from `ScorerPress`. This base class likely provides the compression framework that this implementation extends with statistical query modeling.

## 4) Attention Weight Processing

Processing includes:
- Softmax normalization: `scores = F.softmax(scores, dim=-1)`
- Averaging across attention head groups for dimensionality alignment
- Value norm rescaling: `(scores + epsilon) * values.norm(dim=-1)`
- Sink token preservation with padded maximum values

## 5) Score-to-Compression Mapping

Higher scores indicate tokens to preserve; lower scores identify compression targets. The `compression_ratio` parameter determines what percentage of non-sink tokens get removed, with scores directly determining the removal ranking.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T04:59:55.490864+00:00_

# ProphetKV Technical Details Extraction

## 1) Expected Attention (EA) / Query Attention Formula

The method doesn't use "Expected Attention" terminology. Instead, it uses **average query attention weights**:

$$\hat{\Phi}_{Q_s,t} = \frac{1}{|Q_s|}\sum_{q \in Q_s}\Phi_{q,t}$$

This represents "the average attention weights of query tokens to the t-th context token."

## 2) Layer Usage for Prediction

ProphetKV uses **all layers**, not early layers for prediction. The paper explicitly states: "our selection criterion Φ̂'_{Q_s,t} represents the attention weights from the query tokens to the document KV caches across all layers, which provides token importance in all layers without needing a full prefilling."

The method then fuses these with: $$\bar{\alpha}(t) = \frac{1}{L}\sum_{l=1}^{L}\alpha_l(t)$$

This contrasts with prior work that relied on early-layer approximations.

## 3) Dual-Stage Recomputation Pipeline

**Stage I (Lightweight Pass):**
- Compute query-to-context attention weights across all layers
- Calculate per-layer value function αₗ(t) = Φ̂'_{Q_s,t}(l)

**Stage II (Token Selection & Recomputation):**
- Fuse layer-wise scores into ᾱ(t)
- Select top-p tokens based on fused scores
- Perform complete KV cache recomputation for selected tokens only

Algorithm 1 in the appendix provides pseudocode showing concatenation of chunks, attention computation, fusion, and selective recomputation steps.

## 4) Token Importance Score Computation (Step-by-Step)

**Step 1:** Define semantic loss from imprecise KV caches:
$$\mathcal{L}_{semantic} = \left\|\sum_{1 \leq t \leq s}\hat{\Phi}_{Q_s,t}V_t - \sum_{1 \leq t \leq s}\hat{\Phi}_{Q_s,t}'V_t'\right\|_2$$

**Step 2:** Derive tractable upper bound via triangle inequality:
$$\mathcal{L} = \sum_{1 \leq t \leq s}\left\|\hat{\Phi}_{Q_s,t}'V_t' - \hat{\Phi}_{Q_s,t}V_t\right\|_2$$

**Step 3:** Decompose ideal value function into factors (Eq. 6), then empirically identify most influential factor

**Step 4:** Select practical 
…[truncated 2244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T04:59:55.491269+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/ROADMAP.md\", \"content\": \"# distill_kv_rag_cache — Research Dashboard\\n\\n> 最后更新: 2026-05-14 04:25 UTC | 更新原因: Reviewer 复核：pass #3 从\\\"所有方法 vs E < 5%\\\"改为\\\"D vs E < 5%\\\"，避免误杀正面结果\\n\\n## 核心方向\\nCompressLink: 在 position-independent KV cache serving 场景下，联合优化压缩 bit 分配（RABA）与恢复 token 选择（CEGR），打破压缩和恢复作为独立阶段的范式。基于 MEPIC 和 KVTC 共享的 NoPE 表示。\\n\\n## 当前进展\\n- **阶段**: MVP 验证（刚启动）\\n- 无服务器 / 无 GPU 配置\\n- Agent 已接到代码调研任务（OnlyTerp/kvtc + MEPIC + ProphetKV），等待回复中\\n\\n## MVP 验证方案\\n**核心假设**: 联合优化压缩-恢复接口（RABA+CEGR）优于独立处理。\\n\\n**实验设计**:\\n- 模型: Llama-3.1-8B-Instruct\\n- 数据: NaturalQuestions 子集（~500 queries）\\n- 压缩比: **6x + 8x**（双压缩比消除\\\"压缩太激进\\\"歧义）\\n- Recomputation budget: 20%\\n- 对比 4 组 × 2 压缩比 = 8 runs:\\n  - (A) Independent: standard KVTC + ProphetKV restoration\\n  - (B) RABA only: restoration-weighted allocation + ProphetKV restoration\\n  - (C) CEGR-MSE only: standard allocation + compression-error-guided restoration\\n  - (D) Joint: RABA + CEGR-MSE\\n- 额外 baseline: (E) Uncompressed MEPIC（无压缩，20% boundary recomputation）\\n\\n**Pass 标准**（全部满足）:\\n1. D > max(B, C) — 联合优化有协同效应\\n2. D vs A > 1% EM absolute — 联合优化有实际价值\\n3. **D vs E 退化 < 5%** — 方法本身质量有保证（A 退化大反而是 motivation 证据）\\n4. 上述 pattern 在 6x 和 8x 均成立 — 非压缩比 artifact\\n\\n**Kill 标准**:\\n- **杀死项目**: D ≤ A 在 6x 和 8x 均成立（联合优化无效或有害）\\n- **杀死项目**: D vs E 在 6x 退化 > 10%（即使联合优化+低压缩也无法保质）\\n- **Pivot**: D > A 但 D ≤ max(B, C)（无协同 → 评估单组件论文）\\n- **Pivot**: 仅一个组件有效 → 聚焦有效组件 + 深度分析\\n\\n## 实现依赖\\n1. Functional MEPIC (NoPE KV storage + RoPE-on-query attention + boundary recomputation)\\n2. OnlyTerp/kvtc 集成 (PCA + DP quantization + entropy coding)\\n3. RABA: 修改 DP solver error function（加权 (1-p_r(t))）\\n4. CEGR-MSE: 从 decompression metadata 解析 per-token 压缩误差，与 query relevance 联合评分\\n5. ProphetKV-style query relevance probe\\n\\n## 近期任务\\n- [ ] 用户配置 GPU 服务器（H100 80GB × 1-2 张）— **critical path**\\n-
…[truncated 836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T04:59:55.491653+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/NVIDIA/kvpress/main/kvpress/presses/scorer_press.py",
  "prompt": "Extract the complete code. Show: 1) ScorerPress class definition and how it extends BasePress. 2) The score() abstract method signature. 3) How scores are converted to compression decisions (mask/selection). 4) The compress() implementation that calls score(). 5) Any per-layer or per-head logic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/NVIDIA/kvpress/main/kvpress/presses/scorer_press.py",
    "prompt": "Extract the complete code. Show: 1) ScorerPress class definition and how it extends BasePress. 2) The score() abstract method signature. 3) How scores are converted to compression decisions (mask/selection). 4) The compress() implementation that calls score(). 5) Any per-layer or per-head logic."
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T04:59:55.491797+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/NVIDIA/kvpress/main/kvpress/presses/snapkv_press.py",
  "prompt": "Extract the complete code. Show: 1) How SnapKV is implemented as a kvpress Press. 2) The score computation method. 3) Window size and kernel size parameters. 4) How it differs from the original SnapKV implementation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/NVIDIA/kvpress/main/kvpress/presses/snapkv_press.py",
    "prompt": "Extract the complete code. Show: 1) How SnapKV is implemented as a kvpress Press. 2) The score computation method. 3) Window size and kernel size parameters. 4) How it differs from the original SnapKV implementation."
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T04:59:55.492000+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2602.02579",
  "prompt": "Focus on extracting: 1) Algorithm 1 pseudocode from the appendix - every line. 2) The exact formula for the value function α_l(t). 3) How chunked prefilling interacts with token selection. 4) Figure descriptions showing attention pattern differences across layers. 5) The relationship between recomputation ratio p and accuracy. 6) Any discussion of per-head vs per-layer score granularity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2602.02579",
    "prompt": "Focus on extracting: 1) Algorithm 1 pseudocode from the appendix - every line. 2) The exact formula for the value function α_l(t). 3) How chunked prefilling interacts with token selection. 4) Figure descriptions showing attention pattern differences across layers. 5) The relationship between recomputation ratio p and accuracy. 6) Any discussion of per-head vs per-layer score granularity."
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T04:59:55.492177+00:00_

# ScorerPress KV Cache Compression Architecture

## 1) Class Definition and Inheritance

`ScorerPress` extends `BasePress` as a dataclass-based implementation for score-based KV compression:

```python
@dataclass
class ScorerPress(BasePress):
    compression_ratio: float = 0.0
    
    def __post_init__(self):
        assert 0 <= self.compression_ratio < 1
```

The class validates that "compression ratio must be between 0 and 1" during initialization.

## 2) Abstract Score Method Signature

The `score()` method defines the interface subclasses must implement:

```python
def score(
    self,
    module: nn.Module,
    hidden_states: torch.Tensor,      # (batch, seq_len, hidden_dim)
    keys: torch.Tensor,                # (batch, num_kv_heads, seq_len, head_dim)
    values: torch.Tensor,              # (batch, num_kv_heads, seq_len, head_dim)
    attentions: torch.Tensor,          # (batch, num_heads, seq_len, seq_len)
    kwargs: dict
) -> torch.Tensor:                     # (batch, num_kv_heads, seq_len)
```

Returns importance scores where "higher scores indicate more important tokens that should be kept during compression."

## 3) Score-to-Compression Conversion

Conversion uses **top-k selection** rather than masking:

- Calculate retention count: `n_kept = int(k_len * (1 - compression_ratio))`
- Select indices: `indices = scores.topk(n_kept, dim=-1).indices`
- Expand for gathering: `indices.unsqueeze(-1).expand(..., module.head_dim)`

## 4) Compress Method Implementation

The `compress()` method orchestrates the pipeline:

```python
def compress(self, module, hidden_states, keys, values, attentions, kwargs):
    if self.compression_ratio == 0:
        return keys, values
    
    scores = self.score(...)  # Call subclass implementation
    indices = scores.topk(n_kept, dim=-1).indices
    keys = keys.gather(2, indices).contiguous()
    values = values.gather(2, indices).contiguous()
    return keys, values
```

## 5) Per-Layer/Per-Head Logic

- **Per-head granu
…[truncated 278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T04:59:55.492345+00:00_

# SnapKV Implementation Analysis

## 1) Implementation as a kvpress Press

SnapKV extends `ScorerPress`, inheriting the base framework for KV cache compression. It's a dataclass that implements attention-based scoring to identify and preserve important key-value pairs while removing less critical ones.

## 2) Score Computation Method

The `score()` method:
- Extracts attention weights from the last `window_size` queries focused on earlier tokens
- Computes these weights via `compute_window_attention()` if not already available
- Averages attention across query positions: `scores = attn_weights.mean(dim=-2)`
- Applies smoothing using "avg_pool1d with configurable kernel size for noise reduction"
- Groups scores across attention heads and averages them
- Pads scores with maximum values to protect the observation window from pruning

## 3) Key Parameters

- **compression_ratio** (0.0 default): fraction of KV pairs to remove
- **window_size** (64 default): "number of recent tokens to use for computing attention-based importance scores"
- **kernel_size** (5 default): "size of the pooling kernel applied to attention weights"

## 4) Differences from Original SnapKV

The implementation includes a specific adjustment noted in the code: "Average per group," with reference to a GitHub issue. This handles multi-query attention scenarios by reshaping scores across attention head groups before averaging, which standardizes behavior across different LLM architectures not explicitly detailed in the research paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T04:59:55.492604+00:00_

# ProphetKV: Key Technical Components

## Algorithm 1 Overview

The pseudocode implements a dual-stage pipeline. **Stage I** computes user-query attention weights across all layers to generate per-layer importance scores. **Stage II** fuses these scores and selects top-p tokens for recomputation, then recomputes their KV caches independently at each layer while reusing others.

## Value Function Formula

The practical selection criterion is:
**α(t) = Φ̂_Qs,t'** 

This represents "the attention weights from query tokens to document KV caches" computed without full context. The paper derives this as a computationally tractable proxy through sensitivity analysis, finding it outperforms alternatives like |ΔΦ̂| despite requiring only O(|Qs|×s) rather than O(s²) computation.

## Chunked Prefilling & Token Selection Interaction

Documents are precomputed independently in chunks. ProphetKV concatenates these imprecise KV caches, then selectively recomputes chosen tokens to restore cross-chunk attention. Critically, the selection mechanism operates on imprecise caches (V't, Φ̂'_Qs,t) rather than requiring full prefill—avoiding the "computational deadlock" that forces prior methods to approximate with early-layer information.

## Layer-Wise Attention Variation

Figure 11 demonstrates "lower layers focus primarily on nearby tokens, whereas higher layers attend to distant tokens." The fusion strategy (Equation 7) averages per-layer scores: **ᾱ(t) = (1/L)∑α_l(t)**, achieving significantly higher overlap with layer-wise optimal selections than single-layer approaches.

## Recomputation Ratio & Accuracy Relationship

At 20% recomputation, ProphetKV achieves "8.8%-24.9% improvement on RULER and 18.6%-50.9% on LongBench" over baselines. Figure 8 shows ProphetKV exhibits "significantly steeper accuracy recovery curves," requiring only 10-30% recomputation for <5% accuracy drop versus 40-80% for competitors.

## Granularity: Per-Head vs Per-Layer

The paper operates at **per-layer gra
…[truncated 218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T04:59:55.492914+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
  "content": "# ProphetKV 及 Query-Aware KV Cache 方法调研报告\n\n> 更新: 2026-05-14 | 项目: CompressLink (distill_kv_rag_cache)\n\n---\n\n## 1. 方法对比总览\n\n| 维度 | ProphetKV | SnapKV | kvpress (ExpectedAttention) |\n|------|-----------|--------|----------------------------|\n| 核心思想 | 用 query attention 跨所有层选 token，选择性 recompute | 用 observation window 内 recent query 的 attention 选 token，evict 剩余 | 用 query 统计量 (μ, Σ) 的期望注意力评分 |\n| 场景 | Chunked prefill 后的 KV cache 修复 | Prefill 阶段 KV cache 压缩 | Prefill 阶段 KV cache 压缩 |\n| Score 粒度 | per-layer → fuse to global | per-head per-layer | per-head per-layer |\n| 计算复杂度 | O(\\|Q_s\\| × s) per layer | O(window × s) per layer | O(s) per layer (统计量预计算) |\n| 开源代码 | ❌ 无 | ✅ FasterDecoding/SnapKV | ✅ NVIDIA/kvpress |\n| 与 HF 集成 | — | Monkey-patch | Forward hook (context manager) |\n\n---\n\n## 2. ProphetKV 方法细节 (arXiv 2602.02579)\n\n### 2.1 核心公式\n\n**平均 query attention weight:**\n\n$$\\hat{\\Phi}_{Q_s,t} = \\frac{1}{|Q_s|}\\sum_{q \\in Q_s}\\Phi_{q,t}$$\n\n其中 $Q_s$ 是 user query tokens，$\\Phi_{q,t}$ 是 query token $q$ 对 context token $t$ 的 attention weight。\n\n**实用选择准则 (value function):**\n\n$$\\alpha_l(t) = \\hat{\\Phi}'_{Q_s,t}(l)$$\n\n即第 $l$ 层用 imprecise KV cache 计算的 query-to-context attention weight。注意这里用的是 imprecise cache（chunked prefill 产生的），**不需要 full prefill**。\n\n**跨层融合:**\n\n$$\\bar{\\alpha}(t) = \\frac{1}{L}\\sum_{l=1}^{L}\\alpha_l(t)$$\n\n简单均值融合所有层的 per-layer score。\n\n**Top-p token 选择:**\n\n$$T_p = \\text{Top-}p_{t \\leq C}\\bar{\\alpha}(t)$$\n\n选 recomputation ratio $p$ 比例的 token 进行 recompute。\n\n### 2.2 Dual-Stage Pipeline\n\n**Stage I — Lightweight Query Pass:**\n1. 输入: chunked prefill 产生的 imprecise KV cache + user query tokens\n2. 在**所有层**计算 query tokens 对 context tokens 的 attention weights\n3. 输出: per-layer value function $\\alpha_l(t)$\n\n**Stage II — Selective Recomputation:**\n1. 融合 per-layer scores: $\\bar{\\alpha}(t) = \\frac{1}{L}\\sum\\alpha_l(t)$\n2. 选 top-p tokens $T_p$\n3. **仅对选中 token 重新计算 KV cache**（每层独立）\n4. 未选中 token 保留 imprecise cache\n\n### 2.3 关键设计选择\n\n- **拒绝 early-layer prediction**: 论文明确反对用前几层 attention 预测后续层。Figure 11 展示低层关注 nearby tokens、高层关注 distant tokens，pattern 差异很大\n- **Per-layer 粒度**: score 在每层独立计算，融合用简单均值。无 per-head 差异化\n- **Imprecise cache 上计算**: 不需要 full prefill 即可获得 importance score，打破 \"需要 full prefill 才能知道哪些 token 重要\" 的鸡蛋问题\n\n### 2.4 性能\n\n- 20% recomputation ratio 达到 full prefill 96-101% 准确率\n- 比 full recompute 加速 5×\n- Stage I 的 O(|Q_s|×s) 远低于 CacheBlend 的 O(s²)\n\n### 2.5 语义损失推导\n\n$$\\mathcal{L}_{semantic} = \\left\\|\\sum_t \\hat{\\Phi}_{Q_s,t}V_t - \\sum_t \\hat{\\Phi}'_{Q_s,t}V'_t\\right\\|_2$$\n\n通过三角不等式拆解为 per-token 上界，再通过因子分解实验确定 $\\alpha(t) = \\hat{\\Phi}'_{Q_s,t}$ 为最有效的实用代理。\n\n---\n\n## 3. SnapKV 代码分析 (FasterDecoding/SnapKV)\n\n### 3.1 代码结构\n\n```\nsnapkv/\n├── monkeypatch/\n│   ├── snapkv_utils.py          # 核心算法\n│   ├── llama_hijack_4_37.py     # Llama monkey-patch\n│   ├── mistral_hijack_4_37.py   # Mistral monkey-patch\n│   └── mixtral_hijack_4_37.py   # Mixtral monkey-patch\n├── experiments/LongBench/\n└── notebooks/example.ipynb\n```\n\n### 3.2 核心算法 (`snapkv_utils.py`)\n\n**主函数签名:**\n```python\ndef update_kv(key_states, query_states, value_states, attention_mask, num_key_value_groups):\n    # 触发条件: seq_len > max_capacity_prompt\n```\n\n**初始化参数:**\n```python\n__init__(window_size=64, max_capacity_prompt=320, kernel_size=5, pooling='avgpool')\n```\n\n**Attention 收集:**\n```python\n# 用 observation window 内的 recent queries 计算 attention\nattn_weights = torch.matmul(\n    query_states[..., -window_size:, :],   # recent queries only\n    key_states.transpose(2, 3)\n) / math.sqrt(head_dim)\n```\n\n**Score 聚合:**\n```python\n# 对 window 内所有 query 的 attention 求和（排除 window 内 token）\nattn_weights_sum = attn_weights[:, :, -window_size:, :-window_size].sum(dim=-2)\n```\n\n**Pooling 平滑:**\n```python\nattn_cache = F.avg_pool1d(attn_weights_sum, kernel_size=kernel_size,\n                          padding=kernel_size//2, stride=1)\n```\n\n**Token 选择:**\n```python\n# Top-k 选择重要的 historical tokens\nindices = attn_cache.topk(max_capacity_prompt - window_size, dim=-1).indices\n# Gather 选中的 KV\nkeys = keys.gather(2, indices)\nvalues = values.gather(2, indices)\n```\n\n### 3.3 Observation Window 机制\n\n- Window = 最近 `window_size` (默认64) 个 tokens\n- **始终保留**: window 内 token 不参与 eviction\n- **评估对象**: window 之前的所有 historical tokens\n- **评估方式**: window 内 queries 对 historical tokens 的 attention 作为 importance proxy\n- 直觉: 最近的 queries 的 attention pattern 能近似未来 queries 的需求\n\n### 3.4 与 HF 集成方式\n\n- **Monkey-patching**: 替换 `modeling_llama.py` 等文件中的 `forward` 方法\n- 需 `transformers>=4.36`, `flash-attn==2.4.0`\n- 侵入性强，版本绑定紧\n\n---\n\n## 4. kvpress 库分析 (NVIDIA/kvpress)\n\n### 4.1 架构层次\n\n```\nBasePress (dataclass)\n  └── ScorerPress (compression_ratio + score→topk)\n        ├── SnapKVPress (window_size, kernel_size)\n        ├── ExpectedAttentionPress (query 统计量)\n        ├── KnormPress (key norm)\n        └── ... 其他 Press\n```\n\n### 4.2 BasePress — Hook 机制\n\n```python\nclass BasePress:\n    def __call__(self, model):\n        \"\"\"Context manager: 注册 hook 到所有 attention 层\"\"\"\n        hooks = []\n        for layer in model.model.layers:\n            hooks.append(\n                layer.self_attn.register_forward_hook(\n                    self.forward_hook, with_kwargs=True\n                )\n            )\n        # finally: remove all hooks\n\n    def forward_hook(self, module, input, kwargs, output):\n        \"\"\"在每层 attention forward 后执行压缩\"\"\"\n        # 1. 检查是否在 prefill 阶段\n        if cache_position[-1] > q_len: return output\n        # 2. 从 cache 提取 keys, values\n        keys, values = extract_keys_and_values(...)\n        # 3. 调用 compress() — 子类实现\n        keys, values = self.compress(module, hidden_states, keys, values, attentions, kwargs)\n        # 4. 更新 cache in-place\n\n    def compress(self, module, hidden_states, keys, values, attentions, kwargs):\n        \"\"\"抽象方法 — 子类必须实现\"\"\"\n        raise NotImplementedError\n```\n\n### 4.3 ScorerPress — Score→Compression 桥梁\n\n```python\nclass ScorerPress(BasePress):\n    compression_ratio: float = 0.0  # [0, 1)\n\n    def score(self, module, hidden_states, keys, values, attentions, kwargs) -> Tensor:\n        \"\"\"返回 (batch, num_kv_heads, seq_len) 的 importance scores\"\"\"\n        raise NotImplementedError\n\n    def compress(self, module, hidden_states, keys, values, attentions, kwargs):\n        if self.compression_ratio == 0: return keys, values\n        scores = self.score(...)\n        n_kept = int(seq_len * (1 - self.compression_ratio))\n        indices = scores.topk(n_kept, dim=-1).indices\n        keys = keys.gather(2, indices).contiguous()\n        values = values.gather(2, indices).contiguous()\n        return keys, values\n```\n\n**关键**: score 输出 shape 为 `(batch, num_kv_heads, seq_len)` — **per-head 粒度**，每个 KV head 独立选择保留的 token。\n\n### 4.4 ExpectedAttentionPress\n\n```python\nclass ExpectedAttentionPress(ScorerPress):\n    def score(self, module, hidden_states, keys, values, attentions, kwargs):\n        # 1. 从 hidden_states 提取 query 统计量 (μ, Σ)\n        # 2. 应用 averaged RoPE 变换\n        # 3. 计算期望注意力:\n        #    E(A) = exp(K @ μᵀ / √d + ½K @ Σ @ Kᵀ / d)\n        # 4. Softmax 归一化\n        # 5. Value norm 加权: scores = softmax(E(A)) × (ε + ||V||₂)\n        # 6. Sink token 保护 (padding max values)\n        return scores  # (batch, num_kv_heads, seq_len)\n```\n\n### 4.5 SnapKVPress (kvpress 版)\n\n```python\nclass SnapKVPress(ScorerPress):\n    window_size: int = 64\n    kernel_size: int = 5\n\n    def score(self, module, hidden_states, keys, values, attentions, kwargs):\n        # 1. 提取 window 内 attention: attn[:, :, -window:, :]\n        # 2. 对 query 维度均值: scores = attn.mean(dim=-2)\n        # 3. Avg pooling 平滑: F.avg_pool1d(scores, kernel_size)\n        # 4. GQA 分组均值\n        # 5. Window token 保护 (padding max values)\n        return scores\n```\n\n### 4.6 可复用组件\n\n| 组件 | 说明 | CompressLink 可复用 |\n|------|------|---------------------|\n| Forward hook 注册/清理 | Context manager + register_forward_hook | ✅ 直接用 |\n| score→topk→gather pipeline | ScorerPress.compress() | ✅ 改造为 score→p_r |\n| Per-head score 机制 | (batch, num_kv_heads, seq_len) | ✅ 粒度合适 |\n| Attention 提取 | output_attentions=True | ⚠️ 需确认与 MEPIC NoPE 兼容 |\n| Cache in-place 更新 | 支持 quantized cache | ❌ 我们不 evict，而是 score |\n\n---\n\n## 5. CompressLink Query Relevance Probe 设计方案\n\n### 5.1 目标\n\n生成 per-token query relevance probability $p_r(t) \\in [0,1]$，用于:\n- **RABA**: $\\text{error\\_weight}(t) = 1 - p_r(t)$ — 高 $p_r$ token 分配更少 compression bits\n- **CEGR**: $\\text{restore\\_score}(t) = p_r(t) \\cdot \\text{compression\\_error}(t)$ — 联合评分选 token\n\n### 5.2 方案选择\n\n#### 方案 A: ProphetKV-Style 全层 Query Attention (推荐 MVP)\n\n```python\ndef compute_query_relevance(model, kv_cache, query_ids):\n    \"\"\"\n    在 KVTC 解压后的 (imprecise) KV cache 上运行 query tokens，\n    收集所有层的 attention weights，融合为 global p_r(t)。\n    \"\"\"\n    # Stage 1: 轻量 query forward pass\n    per_layer_scores = []  # List[(batch, num_kv_heads, context_len)]\n    with torch.no_grad():\n        for layer_idx in range(num_layers):\n            # query tokens attend to decompressed KV cache\n            attn_weights = compute_attention(\n                query_states=query_hidden[layer_idx],  # (batch, |Q|, head_dim)\n                key_states=kv_cache[layer_idx].keys,    # (batch, heads, context_len, head_dim)\n            )  # → (batch, heads, |Q|, context_len)\n\n            # 对 query 维度均值 → per-token score\n            alpha_l = attn_weights.mean(dim=-2)  # (batch, heads, context_len)\n            per_layer_scores.append(alpha_l)\n\n    # Stage 2: 跨层融合\n    stacked = torch.stack(per_layer_scores)  # (L, batch, heads, context_len)\n    alpha_bar = stacked.mean(dim=0)  # (batch, heads, context_len)\n\n    # Stage 3: Score → probability\n    # 方案 1 (简单): per-head softmax → 值域自然在 [0,1] 且 sum=1\n    p_r = F.softmax(alpha_bar / temperature, dim=-1)\n    # 方案 2 (rank-based): 按 score 排序，线性映射到 [0,1]\n    # 方案 3 (sigmoid): p_r = sigmoid((alpha_bar - mean) / std)\n\n    return p_r  # (batch, heads, context_len) 或 aggregate to (batch, context_len)\n```\n\n**优势**: \n- 与 ProphetKV 设计一致，理论基础扎实\n- 直接利用 imprecise KV cache，不需 full prefill\n- O(|Q|×s) per layer，query 通常很短\n\n**劣势**: \n- 需要额外 forward pass（但 query 短，开销小）\n\n#### 方案 B: SnapKV-Style Observation Window (简化替代)\n\n```python\ndef compute_query_relevance_snapkv(attn_weights, window_size=64, kernel_size=5):\n    \"\"\"\n    用最后 window_size 个 token 的 attention pattern 作为 query proxy。\n    不需要额外 forward pass，直接用 prefill 阶段的 attention。\n    \"\"\"\n    # 取 window 内 attention\n    scores = attn_weights[:, :, -window_size:, :-window_size].mean(dim=-2)\n    # Avg pooling 平滑\n    scores = F.avg_pool1d(scores, kernel_size=kernel_size, padding=kernel_size//2, stride=1)\n    # Normalize to [0,1]\n    p_r = scores / scores.sum(dim=-1, keepdim=True)\n    return p_r\n```\n\n**优势**: 零额外开销\n**劣势**: 只用 prefill 阶段信息，不含 actual query，与 \"query-aware\" 目标不一致\n\n#### 方案 C: MVP 纯位置先验 (最简)\n\n```python\ndef compute_query_relevance_positional(chunk_boundaries, context_len):\n    \"\"\"\n    MEPIC boundary tokens 的 p_r = 1.0，其余 = base_prob。\n    \"\"\"\n    p_r = torch.full((context_len,), fill_value=base_prob)\n    for b in chunk_boundaries:\n        p_r[b:b+block_size] = 1.0\n    return p_r\n```\n\n**用于 MVP baseline**: 验证 RABA/CEGR pipeline 是否工作，再插入真正的 query probe。\n\n### 5.3 推荐实现路径\n\n```\nPhase 1 (MVP): 方案 C — 位置先验\n  ├── 验证 RABA DP solver 能接受 per-token weight\n  ├── 验证 CEGR scoring pipeline 端到端\n  └── 代码量: ~50 行\n\nPhase 2: 方案 A — ProphetKV-style query attention\n  ├── Hook 到 HF attention layers (参考 kvpress 机制)\n  ├── 收集 per-layer attention\n  ├── Score fusion + probability conversion\n  └── 代码量: ~200 行\n\nPhase 3 (可选): 方案 A + per-head 差异化\n  ├── 不同 head 用不同 temperature\n  ├── 学习 per-layer fusion weight (替代均值)\n  └── 代码量: +100 行\n```\n\n### 5.4 需要 Hook 的 HF 模块\n\n```python\n# 参考 kvpress 的 hook 注册方式\nfor layer in model.model.layers:\n    # Hook 到 self_attn 模块\n    layer.self_attn.register_forward_hook(\n        collect_attention_hook, with_kwargs=True\n    )\n```\n\n**关键修改点 (MEPIC NoPE 兼容)**:\n- MEPIC 存储 NoPE KV cache (不含 RoPE)\n- Query relevance 计算需要用 **RoPE-on-query + NoPE-key** 的 attention\n- 这与标准 HF attention 不同，需要 custom attention computation\n- 不能直接用 `output_attentions=True`，需要在 hook 内手动计算\n\n### 5.5 Score → p_r(t) 转换\n\n| 方法 | 公式 | 值域 | 适用场景 |\n|------|------|------|----------|\n| Softmax | $p_r(t) = \\text{softmax}(\\bar{\\alpha}/\\tau)$ | [0,1], sum=1 | CEGR (相对排序) |\n| Sigmoid | $p_r(t) = \\sigma((\\bar{\\alpha}-\\mu)/\\sigma)$ | [0,1] | RABA (绝对概率) |\n| Rank-linear | $p_r(t) = \\text{rank}(t) / N$ | [0,1] | 均匀分布 |\n| Top-p threshold | $p_r(t) = 1$ if $t \\in T_p$ else $0$ | {0,1} | ProphetKV 原始 |\n\n**推荐**: RABA 用 sigmoid (需要绝对概率), CEGR 用 softmax (需要相对排序)。或统一用 sigmoid，因为 CEGR 本身会与 compression error 相乘。\n\n### 5.6 p_r(t) 粒度选择\n\n| 粒度 | 维度 | 优势 | 劣势 |\n|------|------|------|------|\n| Global | (batch, context_len) | 简单，RABA 直接用 | 忽略 head 差异 |\n| Per-head | (batch, num_kv_heads, context_len) | 精细 | RABA 需要 per-head DP solver |\n| Per-layer | (batch, num_layers, context_len) | 每层不同 restoration | 复杂度爆炸 |\n\n**推荐 MVP**: Global 粒度。per-layer scores 融合为 global score 后，再 per-head 均值得到 (batch, context_len)。RABA 和 CEGR 都在 token 级别操作。\n\n### 5.7 推理时 p_r(t) 获取时机\n\n```\nTimeline:\n  1. Chunked prefill → imprecise NoPE KV cache\n  2. User query arrives\n  3. ★ Query relevance computation (Stage I) ← 在此获取 p_r(t)\n  4. RABA: 用 p_r(t) 重新分配 compression bits (需要 re-compress?)\n     → 或者: p_r(t) 在压缩前预计算 (如果 query 已知)\n  5. CEGR: 用 p_r(t) × compression_error(t) 选 restoration tokens\n  6. Selective recomputation (Stage II)\n  7. Generation\n```\n\n**关键时序问题**:\n- 如果 query 在压缩前已知 → p_r(t) 直接用于 RABA 的 DP solver\n- 如果 query 在压缩后到达 → RABA 需要用 prior (如均匀分布)，CEGR 仍可用 p_r(t)\n- **MVP 假设**: query 在 generation 前已知，两个组件都能用 p_r(t)\n\n---\n\n## 6. 与 MEPIC Boundary Recomputation 的关系\n\n### 6.1 Boundary Token 的特殊性\n\nMEPIC 的 NoPE KV cache 在 chunk 边界处 attention 不连续（因为 chunked prefill 时每个 chunk 独立计算）。Boundary tokens (每个 chunk 的首 block) 必须 recompute 以恢复跨 chunk attention。\n\n**设计原则**:\n- Boundary tokens: $p_r(t) = 1.0$ (硬约束)\n- 这些 token 无论 query 是什么都必须 restore\n- ProphetKV 的 recomputation budget 应排除 boundary tokens（它们已经确定要 recompute）\n\n### 6.2 Budget 分配\n\n```\nTotal recomputation budget: 20% of context tokens\n  ├── Mandatory: boundary tokens (MEPIC 要求) — 约 5-10%\n  └── Discretionary: query-relevant tokens (ProphetKV/CEGR 选择) — 约 10-15%\n```\n\nCEGR 只在 discretionary budget 内操作，boundary tokens 不参与 scoring。\n\n### 6.3 与 RABA 的交互\n\nBoundary tokens 的 $p_r = 1.0$ 意味着:\n- RABA 给这些 token 的 compression weight = $1 - p_r = 0$\n- 即 boundary tokens 不分配 compression bits（反正要 recompute）\n- 这释放 bit budget 给其他 token\n\n---\n\n## 7. 代码量估计\n\n| 组件 | 估计行数 | 依赖 |\n|------|----------|------|\n| 位置先验 p_r (MVP) | ~50 | MEPIC chunk boundaries |\n| ProphetKV-style query probe | ~200 | HF attention hook, MEPIC NoPE KV cache |\n| RABA DP solver 修改 | ~100 | KVTC DP solver, p_r(t) |\n| CEGR scoring | ~80 | Decompression metadata, p_r(t) |\n| 端到端 pipeline | ~150 | 上述所有 |\n| **总计 MVP** | **~580** | |\n\n---\n\n## 8. 核心风险与开放问题\n\n1. **NoPE 兼容性**: ProphetKV 假设标准 RoPE attention，MEPIC 的 NoPE KV + RoPE query 需要 custom attention computation。kvpress 的 hook 不能直接用，需改造。\n\n2. **Softmax temperature**: score → p_r 的 temperature 选择影响 RABA/CEGR 的效果，需要 tuning。\n\n3. **Query 已知时机**: 如果 KV cache 在 query 到达前已经压缩好（serving 场景），RABA 无法用 query-specific p_r。可能需要 query-agnostic prior + query-aware CEGR 的分离设计。\n\n4. **Per-head 均值是否损失信息**: 不同 head 可能对不同 token pattern 敏感，global mean 可能模糊信号。但 MVP 先验证 global 有效性。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
    "content": "# ProphetKV 及 Query-Aware KV Cache 方法调研报告\n\n> 更新: 2026-05-14 | 项目: CompressLink (distill_kv_rag_cache)\n\n---\n\n## 1. 方法对比总览\n\n| 维度 | ProphetKV | SnapKV | kvpress (ExpectedAttention) |\n|------|-----------|--------|----------------------------|\n| 核心思想 | 用 query attention 跨所有层选 token，选择性 recompute | 用 observation window 内 recent query 的 attention 选 token，evict 剩余 | 用 query 统计量 (μ, Σ) 的期望注意力评分 |\n| 场景 | Chunked prefill 后的 KV cache 修复 | Prefill 阶段 KV cache 压缩 | Prefill 阶段 KV cache 压缩 |\n| Score 粒度 | per-layer → fuse to global | per-head per-layer | per-head per-layer |\n| 计算复杂度 | O(\\|Q_s\\| × s) per layer | O(window × s) per layer | O(s) per layer (统计量预计算) |\n| 开源代码 | ❌ 无 | ✅ FasterDecoding/SnapKV | ✅ NVIDIA/kvpress |\n| 与 HF 集成 | — | Monkey-patch | Forward hook (context manager) |\n\n---\n\n## 2. ProphetKV 方法细节 (arXiv 2602.02579)\n\n### 2.1 核心公式\n\n**平均 query attention weight:**\n\n$$\\hat{\\Phi}_{Q_s,t} = \\frac{1}{|Q_s|}\\sum_{q \\in Q_s}\\Phi_{q,t}$$\n\n其中 $Q_s$ 是 user query tokens，$\\Phi_{q,t}$ 是 query token $q$ 对 context token $t$ 的 attention weight。\n\n**实用选择准则 (value function):**\n\n$$\\alpha_l(t) = \\hat{\\Phi}'_{Q_s,t}(l)$$\n\n即第 $l$ 层用 imprecise KV cache 计算的 query-to-context attention weight。注意这里用的是 imprecise cache（chunked prefill 产生的），**不需要 full prefill**。\n\n**跨层融合:**\n\n$$\\bar{\\alpha}(t) = \\frac{1}{L}\\sum_{l=1}^{L}\\alpha_l(t)$$\n\n简单均值融合所有层的 per-layer score。\n\n**Top-p token 选择:**\n\n$$T_p = \\text{Top-}p_{t \\leq C}\\bar{\\alpha}(t)$$\n\n选 recomputation ratio $p$ 比例的 token 进行 recompute。\n\n### 2.2 Dual-Stage Pipeline\n\n**Stage I — Lightweight Query Pass:**\n1. 输入: chunked prefill 产生的 imprecise KV cache + user query tokens\n2. 在**所有层**计算 query tokens 对 context tokens 的 attention weights\n3. 输出: per-layer value function $\\alpha_l(t)$\n\n**Stage II — Selective Recomputation:**\n1. 融合 per-layer scores: $\\bar{\\alpha}(t) = \\frac{1}{L}\\sum\\alpha_l(t)$\n2. 选 top-p tokens $T_p$\n3. **仅对选中 token 重新计算 KV cache**（每层独立）\n4. 未选中 token 保留 imprecise cache\n\n### 2.3 关键设计选择\n\n- **拒绝 early-layer prediction**: 论文明确反对用前几层 attention 预测后续层。Figure 11 展示低层关注 nearby tokens、高层关注 distant tokens，pattern 差异很大\n- **Per-layer 粒度**: score 在每层独立计算，融合用简单均值。无 per-head 差异化\n- **Imprecise cache 上计算**: 不需要 full prefill 即可获得 importance score，打破 \"需要 full prefill 才能知道哪些 token 重要\" 的鸡蛋问题\n\n### 2.4 性能\n\n- 20% recomputation ratio 达到 full prefill 96-101% 准确率\n- 比 full recompute 加速 5×\n- Stage I 的 O(|Q_s|×s) 远低于 CacheBlend 的 O(s²)\n\n### 2.5 语义损失推导\n\n$$\\mathcal{L}_{semantic} = \\left\\|\\sum_t \\hat{\\Phi}_{Q_s,t}V_t - \\sum_t \\hat{\\Phi}'_{Q_s,t}V'_t\\right\\|_2$$\n\n通过三角不等式拆解为 per-token 上界，再通过因子分解实验确定 $\\alpha(t) = \\hat{\\Phi}'_{Q_s,t}$ 为最有效的实用代理。\n\n---\n\n## 3. SnapKV 代码分析 (FasterDecoding/SnapKV)\n\n### 3.1 代码结构\n\n```\nsnapkv/\n├── monkeypatch/\n│   ├── snapkv_utils.py          # 核心算法\n│   ├── llama_hijack_4_37.py     # Llama monkey-patch\n│   ├── mistral_hijack_4_37.py   # Mistral monkey-patch\n│   └── mixtral_hijack_4_37.py   # Mixtral monkey-patch\n├── experiments/LongBench/\n└── notebooks/example.ipynb\n```\n\n### 3.2 核心算法 (`snapkv_utils.py`)\n\n**主函数签名:**\n```python\ndef update_kv(key_states, query_states, value_states, attention_mask, num_key_value_groups):\n    # 触发条件: seq_len > max_capacity_prompt\n```\n\n**初始化参数:**\n```python\n__init__(window_size=64, max_capacity_prompt=320, kernel_size=5, pooling='avgpool')\n```\n\n**Attention 收集:**\n```python\n# 用 observation window 内的 recent queries 计算 attention\nattn_weights = torch.matmul(\n    query_states[..., -window_size:, :],   # recent queries only\n    key_states.transpose(2, 3)\n) / math.sqrt(head_dim)\n```\n\n**Score 聚合:**\n```python\n# 对 window 内所有 query 的 attention 求和（排除 window 内 token）\nattn_weights_sum = attn_weights[:, :, -window_size:, :-window_size].sum(dim=-2)\n```\n\n**Pooling 平滑:**\n```python\nattn_cache = F.avg_pool1d(attn_weights_sum, kernel_size=kernel_size,\n                          padding=kernel_size//2, stride=1)\n```\n\n**Token 选择:**\n```python\n# Top-k 选择重要的 historical tokens\nindices = attn_cache.topk(max_capacity_prompt - window_size, dim=-1).indices\n# Gather 选中的 KV\nkeys = keys.gather(2, indices)\nvalues = values.gather(2, indices)\n```\n\n### 3.3 Observation Window 机制\n\n- Window = 最近 `window_size` (默认64) 个 tokens\n- **始终保留**: window 内 token 不参与 eviction\n- **评估对象**: window 之前的所有 historical tokens\n- **评估方式**: window 内 queries 对 historical tokens 的 attention 作为 importance proxy\n- 直觉: 最近的 queries 的 attention pattern 能近似未来 queries 的需求\n\n### 3.4 与 HF 集成方式\n\n- **Monkey-patching**: 替换 `modeling_llama.py` 等文件中的 `forward` 方法\n- 需 `transformers>=4.36`, `flash-attn==2.4.0`\n- 侵入性强，版本绑定紧\n\n---\n\n## 4. kvpress 库分析 (NVIDIA/kvpress)\n\n### 4.1 架构层次\n\n```\nBasePress (dataclass)\n  └── ScorerPress (compression_ratio + score→topk)\n        ├── SnapKVPress (window_size, kernel_size)\n        ├── ExpectedAttentionPress (query 统计量)\n        ├── KnormPress (key norm)\n        └── ... 其他 Press\n```\n\n### 4.2 BasePress — Hook 机制\n\n```python\nclass BasePress:\n    def __call__(self, model):\n        \"\"\"Context manager: 注册 hook 到所有 attention 层\"\"\"\n        hooks = []\n        for layer in model.model.layers:\n            hooks.append(\n                layer.self_attn.register_forward_hook(\n                    self.forward_hook, with_kwargs=True\n                )\n            )\n        # finally: remove all hooks\n\n    def forward_hook(self, module, input, kwargs, output):\n        \"\"\"在每层 attention forward 后执行压缩\"\"\"\n        # 1. 检查是否在 prefill 阶段\n        if cache_position[-1] > q_len: return output\n        # 2. 从 cache 提取 keys, values\n        keys, values = extract_keys_and_values(...)\n        # 3. 调用 compress() — 子类实现\n        keys, values = self.compress(module, hidden_states, keys, values, attentions, kwargs)\n        # 4. 更新 cache in-place\n\n    def compress(self, module, hidden_states, keys, values, attentions, kwargs):\n        \"\"\"抽象方法 — 子类必须实现\"\"\"\n        raise NotImplementedError\n```\n\n### 4.3 ScorerPress — Score→Compression 桥梁\n\n```python\nclass ScorerPress(BasePress):\n    compression_ratio: float = 0.0  # [0, 1)\n\n    def score(self, module, hidden_states, keys, values, attentions, kwargs) -> Tensor:\n        \"\"\"返回 (batch, num_kv_heads, seq_len) 的 importance scores\"\"\"\n        raise NotImplementedError\n\n    def compress(self, module, hidden_states, keys, values, attentions, kwargs):\n        if self.compression_ratio == 0: return keys, values\n        scores = self.score(...)\n        n_kept = int(seq_len * (1 - self.compression_ratio))\n        indices = scores.topk(n_kept, dim=-1).indices\n        keys = keys.gather(2, indices).contiguous()\n        values = values.gather(2, indices).contiguous()\n        return keys, values\n```\n\n**关键**: score 输出 shape 为 `(batch, num_kv_heads, seq_len)` — **per-head 粒度**，每个 KV head 独立选择保留的 token。\n\n### 4.4 ExpectedAttentionPress\n\n```python\nclass ExpectedAttentionPress(ScorerPress):\n    def score(self, module, hidden_states, keys, values, attentions, kwargs):\n        # 1. 从 hidden_states 提取 query 统计量 (μ, Σ)\n        # 2. 应用 averaged RoPE 变换\n        # 3. 计算期望注意力:\n        #    E(A) = exp(K @ μᵀ / √d + ½K @ Σ @ Kᵀ / d)\n        # 4. Softmax 归一化\n        # 5. Value norm 加权: scores = softmax(E(A)) × (ε + ||V||₂)\n        # 6. Sink token 保护 (padding max values)\n        return scores  # (batch, num_kv_heads, seq_len)\n```\n\n### 4.5 SnapKVPress (kvpress 版)\n\n```python\nclass SnapKVPress(ScorerPress):\n    window_size: int = 64\n    kernel_size: int = 5\n\n    def score(self, module, hidden_states, keys, values, attentions, kwargs):\n        # 1. 提取 window 内 attention: attn[:, :, -window:, :]\n        # 2. 对 query 维度均值: scores = attn.mean(dim=-2)\n        # 3. Avg pooling 平滑: F.avg_pool1d(scores, kernel_size)\n        # 4. GQA 分组均值\n        # 5. Window token 保护 (padding max values)\n        return scores\n```\n\n### 4.6 可复用组件\n\n| 组件 | 说明 | CompressLink 可复用 |\n|------|------|---------------------|\n| Forward hook 注册/清理 | Context manager + register_forward_hook | ✅ 直接用 |\n| score→topk→gather pipeline | ScorerPress.compress() | ✅ 改造为 score→p_r |\n| Per-head score 机制 | (batch, num_kv_heads, seq_len) | ✅ 粒度合适 |\n| Attention 提取 | output_attentions=True | ⚠️ 需确认与 MEPIC NoPE 兼容 |\n| Cache in-place 更新 | 支持 quantized cache | ❌ 我们不 evict，而是 score |\n\n---\n\n## 5. CompressLink Query Relevance Probe 设计方案\n\n### 5.1 目标\n\n生成 per-token query relevance probability $p_r(t) \\in [0,1]$，用于:\n- **RABA**: $\\text{error\\_weight}(t) = 1 - p_r(t)$ — 高 $p_r$ token 分配更少 compression bits\n- **CEGR**: $\\text{restore\\_score}(t) = p_r(t) \\cdot \\text{compression\\_error}(t)$ — 联合评分选 token\n\n### 5.2 方案选择\n\n#### 方案 A: ProphetKV-Style 全层 Query Attention (推荐 MVP)\n\n```python\ndef compute_query_relevance(model, kv_cache, query_ids):\n    \"\"\"\n    在 KVTC 解压后的 (imprecise) KV cache 上运行 query tokens，\n    收集所有层的 attention weights，融合为 global p_r(t)。\n    \"\"\"\n    # Stage 1: 轻量 query forward pass\n    per_layer_scores = []  # List[(batch, num_kv_heads, context_len)]\n    with torch.no_grad():\n        for layer_idx in range(num_layers):\n            # query tokens attend to decompressed KV cache\n            attn_weights = compute_attention(\n                query_states=query_hidden[layer_idx],  # (batch, |Q|, head_dim)\n                key_states=kv_cache[layer_idx].keys,    # (batch, heads, context_len, head_dim)\n            )  # → (batch, heads, |Q|, context_len)\n\n            # 对 query 维度均值 → per-token score\n            alpha_l = attn_weights.mean(dim=-2)  # (batch, heads, context_len)\n            per_layer_scores.append(alpha_l)\n\n    # Stage 2: 跨层融合\n    stacked = torch.stack(per_layer_scores)  # (L, batch, heads, context_len)\n    alpha_bar = stacked.mean(dim=0)  # (batch, heads, context_len)\n\n    # Stage 3: Score → probability\n    # 方案 1 (简单): per-head softmax → 值域自然在 [0,1] 且 sum=1\n    p_r = F.softmax(alpha_bar / temperature, dim=-1)\n    # 方案 2 (rank-based): 按 score 排序，线性映射到 [0,1]\n    # 方案 3 (sigmoid): p_r = sigmoid((alpha_bar - mean) / std)\n\n    return p_r  # (batch, heads, context_len) 或 aggregate to (batch, context_len)\n```\n\n**优势**: \n- 与 ProphetKV 设计一致，理论基础扎实\n- 直接利用 imprecise KV cache，不需 full prefill\n- O(|Q|×s) per layer，query 通常很短\n\n**劣势**: \n- 需要额外 forward pass（但 query 短，开销小）\n\n#### 方案 B: SnapKV-Style Observation Window (简化替代)\n\n```python\ndef compute_query_relevance_snapkv(attn_weights, window_size=64, kernel_size=5):\n    \"\"\"\n    用最后 window_size 个 token 的 attention pattern 作为 query proxy。\n    不需要额外 forward pass，直接用 prefill 阶段的 attention。\n    \"\"\"\n    # 取 window 内 attention\n    scores = attn_weights[:, :, -window_size:, :-window_size].mean(dim=-2)\n    # Avg pooling 平滑\n    scores = F.avg_pool1d(scores, kernel_size=kernel_size, padding=kernel_size//2, stride=1)\n    # Normalize to [0,1]\n    p_r = scores / scores.sum(dim=-1, keepdim=True)\n    return p_r\n```\n\n**优势**: 零额外开销\n**劣势**: 只用 prefill 阶段信息，不含 actual query，与 \"query-aware\" 目标不一致\n\n#### 方案 C: MVP 纯位置先验 (最简)\n\n```python\ndef compute_query_relevance_positional(chunk_boundaries, context_len):\n    \"\"\"\n    MEPIC boundary tokens 的 p_r = 1.0，其余 = base_prob。\n    \"\"\"\n    p_r = torch.full((context_len,), fill_value=base_prob)\n    for b in chunk_boundaries:\n        p_r[b:b+block_size] = 1.0\n    return p_r\n```\n\n**用于 MVP baseline**: 验证 RABA/CEGR pipeline 是否工作，再插入真正的 query probe。\n\n### 5.3 推荐实现路径\n\n```\nPhase 1 (MVP): 方案 C — 位置先验\n  ├── 验证 RABA DP solver 能接受 per-token weight\n  ├── 验证 CEGR scoring pipeline 端到端\n  └── 代码量: ~50 行\n\nPhase 2: 方案 A — ProphetKV-style query attention\n  ├── Hook 到 HF attention layers (参考 kvpress 机制)\n  ├── 收集 per-layer attention\n  ├── Score fusion + probability conversion\n  └── 代码量: ~200 行\n\nPhase 3 (可选): 方案 A + per-head 差异化\n  ├── 不同 head 用不同 temperature\n  ├── 学习 per-layer fusion weight (替代均值)\n  └── 代码量: +100 行\n```\n\n### 5.4 需要 Hook 的 HF 模块\n\n```python\n# 参考 kvpress 的 hook 注册方式\nfor layer in model.model.layers:\n    # Hook 到 self_attn 模块\n    layer.self_attn.register_forward_hook(\n        collect_attention_hook, with_kwargs=True\n    )\n```\n\n**关键修改点 (MEPIC NoPE 兼容)**:\n- MEPIC 存储 NoPE KV cache (不含 RoPE)\n- Query relevance 计算需要用 **RoPE-on-query + NoPE-key** 的 attention\n- 这与标准 HF attention 不同，需要 custom attention computation\n- 不能直接用 `output_attentions=True`，需要在 hook 内手动计算\n\n### 5.5 Score → p_r(t) 转换\n\n| 方法 | 公式 | 值域 | 适用场景 |\n|------|------|------|----------|\n| Softmax | $p_r(t) = \\text{softmax}(\\bar{\\alpha}/\\tau)$ | [0,1], sum=1 | CEGR (相对排序) |\n| Sigmoid | $p_r(t) = \\sigma((\\bar{\\alpha}-\\mu)/\\sigma)$ | [0,1] | RABA (绝对概率) |\n| Rank-linear | $p_r(t) = \\text{rank}(t) / N$ | [0,1] | 均匀分布 |\n| Top-p threshold | $p_r(t) = 1$ if $t \\in T_p$ else $0$ | {0,1} | ProphetKV 原始 |\n\n**推荐**: RABA 用 sigmoid (需要绝对概率), CEGR 用 softmax (需要相对排序)。或统一用 sigmoid，因为 CEGR 本身会与 compression error 相乘。\n\n### 5.6 p_r(t) 粒度选择\n\n| 粒度 | 维度 | 优势 | 劣势 |\n|------|------|------|------|\n| Global | (batch, context_len) | 简单，RABA 直接用 | 忽略 head 差异 |\n| Per-head | (batch, num_kv_heads, context_len) | 精细 | RABA 需要 per-head DP solver |\n| Per-layer | (batch, num_layers, context_len) | 每层不同 restoration | 复杂度爆炸 |\n\n**推荐 MVP**: Global 粒度。per-layer scores 融合为 global score 后，再 per-head 均值得到 (batch, context_len)。RABA 和 CEGR 都在 token 级别操作。\n\n### 5.7 推理时 p_r(t) 获取时机\n\n```\nTimeline:\n  1. Chunked prefill → imprecise NoPE KV cache\n  2. User query arrives\n  3. ★ Query relevance computation (Stage I) ← 在此获取 p_r(t)\n  4. RABA: 用 p_r(t) 重新分配 compression bits (需要 re-compress?)\n     → 或者: p_r(t) 在压缩前预计算 (如果 query 已知)\n  5. CEGR: 用 p_r(t) × compression_error(t) 选 restoration tokens\n  6. Selective recomputation (Stage II)\n  7. Generation\n```\n\n**关键时序问题**:\n- 如果 query 在压缩前已知 → p_r(t) 直接用于 RABA 的 DP solver\n- 如果 query 在压缩后到达 → RABA 需要用 prior (如均匀分布)，CEGR 仍可用 p_r(t)\n- **MVP 假设**: query 在 generation 前已知，两个组件都能用 p_r(t)\n\n---\n\n## 6. 与 MEPIC Boundary Recomputation 的关系\n\n### 6.1 Boundary Token 的特殊性\n\nMEPIC 的 NoPE KV cache 在 chunk 边界处 attention 不连续（因为 chunked prefill 时每个 chunk 独立计算）。Boundary tokens (每个 chunk 的首 block) 必须 recompute 以恢复跨 chunk attention。\n\n**设计原则**:\n- Boundary tokens: $p_r(t) = 1.0$ (硬约束)\n- 这些 token 无论 query 是什么都必须 restore\n- ProphetKV 的 recomputation budget 应排除 boundary tokens（它们已经确定要 recompute）\n\n### 6.2 Budget 分配\n\n```\nTotal recomputation budget: 20% of context tokens\n  ├── Mandatory: boundary tokens (MEPIC 要求) — 约 5-10%\n  └── Discretionary: query-relevant tokens (ProphetKV/CEGR 选择) — 约 10-15%\n```\n\nCEGR 只在 discretionary budget 内操作，boundary tokens 不参与 scoring。\n\n### 6.3 与 RABA 的交互\n\nBoundary tokens 的 $p_r = 1.0$ 意味着:\n- RABA 给这些 token 的 compression weight = $1 - p_r = 0$\n- 即 boundary tokens 不分配 compression bits（反正要 recompute）\n- 这释放 bit budget 给其他 token\n\n---\n\n## 7. 代码量估计\n\n| 组件 | 估计行数 | 依赖 |\n|------|----------|------|\n| 位置先验 p_r (MVP) | ~50 | MEPIC chunk boundaries |\n| ProphetKV-style query probe | ~200 | HF attention hook, MEPIC NoPE KV cache |\n| RABA DP solver 修改 | ~100 | KVTC DP solver, p_r(t) |\n| CEGR scoring | ~80 | Decompression metadata, p_r(t) |\n| 端到端 pipeline | ~150 | 上述所有 |\n| **总计 MVP** | **~580** | |\n\n---\n\n## 8. 核心风险与开放问题\n\n1. **NoPE 兼容性**: ProphetKV 假设标准 RoPE attention，MEPIC 的 NoPE KV + RoPE query 需要 custom attention computation。kvpress 的 hook 不能直接用，需改造。\n\n2. **Softmax temperature**: score → p_r 的 temperature 选择影响 RABA/CEGR 的效果，需要 tuning。\n\n3. **Query 已知时机**: 如果 KV cache 在 query 到达前已经压缩好（serving 场景），RABA 无法用 query-specific p_r。可能需要 query-agnostic prior + query-aware CEGR 的分离设计。\n\n4. **Per-head 均值是否损失信息**: 不同 head 可能对不同 token pattern 敏感，global mean 可能模糊信号。但 MVP 先验证 global 有效性。\n"
  }
}
````

</details>

---

### Tool result

_source line 28 · 2026-05-14T04:59:55.493644+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T04:59:55.493820+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
    "description": "Check artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T04:59:55.493994+00:00_

_project
kvtc_survey.md
manifest.yaml
mepic_survey.md
prophetkv_survey.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T04:59:55.494208+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T04:59:55.494508+00:00_

1	# ProphetKV 及 Query-Aware KV Cache 方法调研报告
2	
3	> 论文: arXiv 2602.02579 (Feb 2026)  
4	> 作者: Shihao Wang, Jiahao Chen et al. (HIT Shenzhen, Yanrong Technology)  
5	> 代码: **无公开代码仓库**  
6	> 调研日期: 2026-05-14  
7	> 目的: 为 CompressLink 的 query relevance probe (p_r(t)) 提供方法论依据和实现方案
8	
9	---
10	
11	## 1. ProphetKV 核心方法
12	
13	### 1.1 问题场景
14	
15	ProphetKV 针对 RAG 场景中的 **position-independent KV cache reuse**。典型流程:
16	1. 多个 RAG 文档各自独立预计算 KV cache（chunk-wise precomputation）
17	2. 用户请求时，拼接各 chunk 的 KV cache → **缺失 cross-chunk attention**
18	3. 需要选择性 recompute 部分 token 来恢复关键的 cross-attention
19	
20	**核心洞察**: 现有方法（CacheBlend、EPIC、KVShare）使用全局 saliency 指标选 token，导致 **crowding-out effect** — 全局显著但与用户查询无关的 token 占满 recomputation budget，挤走真正关键的 token。
21	
22	### 1.2 "User Query as a Prophet" — 核心假设
23	
24	**实验发现**: 用户查询 attention 到的 token 子集，与 decoding 阶段被 attend 到的 token 子集有 **高度重叠**（overlap ratio 在 top-p=0.2 时已达 80%+，跨 Llama3-8B、Qwen2.5-14B、Qwen3-14B 均稳健）。
25	
26	→ 用户查询的 attention pattern 可作为 decoding 阶段 token 重要性的 **先知 (prophet)**。
27	
28	### 1.3 数学推导
29	
30	#### 1.3.1 Attention 输出分解
31	
32	对于生成 token n > s（s 为输入长度），attention 输出可分解为:
33	
34	```
35	AttnOut_n = Σ_{1≤t≤s} Φ_{n,t} V_t + Σ_{s&lt;t≤n} Φ_{n,t} V_t
36	            ├── 输入 token 贡献 ──┘   └── 生成 token 贡献 ──┘
37	```
38	
39	#### 1.3.2 Query Attention 作为代理
40	
41	定义 **query token 对 context token t 的平均 attention**:
42	
43	```
44	Φ̂_{Q_s,t} = (1/|Q_s|) Σ_{q∈Q_s} Φ_{q,t}
45	```
46	
47	其中 Q_s 是用户查询 token 集合。核心近似:
48	
49	```
50	Φ_{n,t} ≈ Φ̂_{Q_s,t}   (for n > s)
51	```
52	
53	#### 1.3.3 Semantic Loss 定义
54	
55	Precise KV cache (有 cross-attention) vs Imprecise KV cache (无 cross-attention) 的差距:
56	
57	```
58	L_semantic = ||Σ_{1≤t≤s} Φ̂_{Q_s,t} V_t - Σ_{1≤t≤s} Φ̂'_{Q_s,t} V'_t||_2   ... (Eq. 2)
59	```
60	
61	其中 V'_t 和 Φ̂'_{Q_s,t} 是 imprecise 版本（chunk 独立计算、无 cross-attention）。
62	
63	上界（三角不等式）:
64	
65	```
66	L_semantic ≤ L = Σ_{1≤t≤s} ||Φ̂'_{Q_s,t} V'_t - Φ̂_{Q_s,t} V_t||_2   ... (Eq. 3)
67	```
68	
69	#### 1.3.4 Token 选择的 Value Function
70	
7
…[truncated 23343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T04:59:55.495259+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

````json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
  "old_string": "> 论文: arXiv 2602.02579 (Feb 2026)  \n> 作者: Shihao Wang, Jiahao Chen et al. (HIT Shenzhen, Yanrong Technology)  \n> 代码: **无公开代码仓库**  \n> 调研日期: 2026-05-14  \n> 目的: 为 CompressLink 的 query relevance probe (p_r(t)) 提供方法论依据和实现方案",
  "new_string": "> 论文: arXiv 2602.02579 (Feb 2026)  \n> 作者: Shihao Wang, Jiahao Chen et al. (HIT Shenzhen, Yanrong Technology)  \n> 代码: **无公开代码仓库**  \n> 调研日期: 2026-05-14 (v2 更新)  \n> 目的: 为 CompressLink 的 query relevance probe (p_r(t)) 提供方法论依据和实现方案\n\n---\n\n## 快速参考\n\n### 方法对比表\n\n| 维度 | ProphetKV | SnapKV | kvpress ExpectedAttn |\n|------|-----------|--------|---------------------|\n| 核心信号 | query attn column sum, 跨所有层 | observation window attn, per-layer | Gaussian E[attn], per-layer |\n| 场景 | Chunked prefill 后 KV 修复 | Prefill KV eviction | Prefill KV eviction |\n| 需要 query? | ✅ | ❌ (用 window proxy) | ❌ (统计预测) |\n| Score 粒度 | per-layer → fuse to global per-token | per-head per-layer | per-head per-layer |\n| 计算开销 | O(\\|Q\\|×s) per layer | O(window×s) per layer | O(s×d) per layer |\n| 开源代码 | ❌ | ✅ FasterDecoding/SnapKV | ✅ NVIDIA/kvpress |\n| HF 集成 | — | Monkey-patch | Forward hook (context mgr) |\n\n### 核心公式速查\n\n```\nProphetKV:  α_l(t) = Φ̂'_{Q_s,t}^(l) = (1/|Q|) Σ_q softmax(q·K'/√d)_t\n            ᾱ(t) = (1/L) Σ_l α_l(t)\n            T_p = Top-p(ᾱ(t))\n\nSnapKV:     scores = AvgPool1d(attn[:,:,-W:,:-W].mean(dim=-2), kernel=5)\n            keep = TopK(scores, capacity - window)\n\nExpAttn:    E(A)_i = exp(μ_q^T k_i/√d + k_i^T Σ_q k_i/(2d))\n            score_i = softmax(E(A))_i · (ε + ||v_i||₂)\n```\n\n### 代码量估计\n\n| 组件 | 行数 | 依赖 |\n|------|------|------|\n| 位置先验 p_r (MVP Phase 0) | ~50 | MEPIC chunk boundaries |\n| ProphetKV-style query probe (Phase 1) | ~200 | HF attn hook, NoPE KV cache |\n| RABA DP solver 修改 | ~100 | KVTC DP solver |\n| CEGR scoring | ~80 | Decompression metadata |\n| 端到端 pipeline glue | ~150 | 以上全部 |\n| **总计** | **~580** | |"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
    "old_string": "> 论文: arXiv 2602.02579 (Feb 2026)  \n> 作者: Shihao Wang, Jiahao Chen et al. (HIT Shenzhen, Yanrong Technology)  \n> 代码: **无公开代码仓库**  \n> 调研日期: 2026-05-14  \n> 目的: 为 CompressLink 的 query relevance probe (p_r(t)) 提供方法论依据和实现方案",
    "new_string": "> 论文: arXiv 2602.02579 (Feb 2026)  \n> 作者: Shihao Wang, Jiahao Chen et al. (HIT Shenzhen, Yanrong Technology)  \n> 代码: **无公开代码仓库**  \n> 调研日期: 2026-05-14 (v2 更新)  \n> 目的: 为 CompressLink 的 query relevance probe (p_r(t)) 提供方法论依据和实现方案\n\n---\n\n## 快速参考\n\n### 方法对比表\n\n| 维度 | ProphetKV | SnapKV | kvpress ExpectedAttn |\n|------|-----------|--------|---------------------|\n| 核心信号 | query attn column sum, 跨所有层 | observation window attn, per-layer | Gaussian E[attn], per-layer |\n| 场景 | Chunked prefill 后 KV 修复 | Prefill KV eviction | Prefill KV eviction |\n| 需要 query? | ✅ | ❌ (用 window proxy) | ❌ (统计预测) |\n| Score 粒度 | per-layer → fuse to global per-token | per-head per-layer | per-head per-layer |\n| 计算开销 | O(\\|Q\\|×s) per layer | O(window×s) per layer | O(s×d) per layer |\n| 开源代码 | ❌ | ✅ FasterDecoding/SnapKV | ✅ NVIDIA/kvpress |\n| HF 集成 | — | Monkey-patch | Forward hook (context mgr) |\n\n### 核心公式速查\n\n```\nProphetKV:  α_l(t) = Φ̂'_{Q_s,t}^(l) = (1/|Q|) Σ_q softmax(q·K'/√d)_t\n            ᾱ(t) = (1/L) Σ_l α_l(t)\n            T_p = Top-p(ᾱ(t))\n\nSnapKV:     scores = AvgPool1d(attn[:,:,-W:,:-W].mean(dim=-2), kernel=5)\n            keep = TopK(scores, capacity - window)\n\nExpAttn:    E(A)_i = exp(μ_q^T k_i/√d + k_i^T Σ_q k_i/(2d))\n            score_i = softmax(E(A))_i · (ε + ||v_i||₂)\n```\n\n### 代码量估计\n\n| 组件 | 行数 | 依赖 |\n|------|------|------|\n| 位置先验 p_r (MVP Phase 0) | ~50 | MEPIC chunk boundaries |\n| ProphetKV-style query probe (Phase 1) | ~200 | HF attn hook, NoPE KV cache |\n| RABA DP solver 修改 | ~100 | KVTC DP solver |\n| CEGR scoring | ~80 | Decompression metadata |\n| 端到端 pipeline glue | ~150 | 以上全部 |\n| **总计** | **~580** | |"
  }
}
````

</details>

---

### Tool result

_source line 34 · 2026-05-14T04:59:55.495549+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T04:59:55.495709+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
  "old_string": "**核心**: **累积 attention score** — 每个 token 在所有之前的 attention 计算中被 attend 到的总量。",
  "new_string": "**核心**: **累积 attention score** — 每个 token 在所有之前的 attention 计算中被 attend 到的总量。ProphetKV **明确反对** early-layer prediction（论文 Figure 11 展示低层关注 nearby tokens、高层关注 distant tokens，pattern 差异显著），因此跨所有层计算后融合。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
    "old_string": "**核心**: **累积 attention score** — 每个 token 在所有之前的 attention 计算中被 attend 到的总量。",
    "new_string": "**核心**: **累积 attention score** — 每个 token 在所有之前的 attention 计算中被 attend 到的总量。ProphetKV **明确反对** early-layer prediction（论文 Figure 11 展示低层关注 nearby tokens、高层关注 distant tokens，pattern 差异显著），因此跨所有层计算后融合。"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T04:59:55.496049+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T04:59:55.496518+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

````json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
  "old_string": "### 3.2 核心接口\n\n```python\n# 使用方式 (context manager)\nwith press(model):\n    outputs = model.generate(...)\n\n# ScorerPress 子类需实现:\ndef score(self, module, hidden_states, keys, values, attentions, kwargs):\n    \"\"\"\n    返回 shape: [batch_size, num_kv_heads, seq_len]\n    分数越高 = token 越重要 = 越不会被剪\n    \"\"\"\n    ...\n\n# 基类自动处理:\n# 1. 注册 forward hook 到每个 attention layer\n# 2. 调用 score() 获取分数\n# 3. topk 保留 n_kept = int(seq_len * (1 - compression_ratio)) 个 token\n# 4. gather key/value tensors\n```",
  "new_string": "### 3.2 核心接口\n\n```python\n# 使用方式 (context manager)\nwith press(model):\n    outputs = model.generate(...)\n\n# ScorerPress 子类需实现:\ndef score(self, module: nn.Module, hidden_states: torch.Tensor,\n          keys: torch.Tensor,       # (batch, num_kv_heads, seq_len, head_dim)\n          values: torch.Tensor,     # (batch, num_kv_heads, seq_len, head_dim)\n          attentions: torch.Tensor, # (batch, num_heads, seq_len, seq_len)\n          kwargs: dict\n    ) -> torch.Tensor:              # (batch, num_kv_heads, seq_len) ← per-head 粒度\n    \"\"\"分数越高 = token 越重要 = 越不会被剪\"\"\"\n    ...\n\n# ScorerPress.compress() 的实际实现:\ndef compress(self, module, hidden_states, keys, values, attentions, kwargs):\n    if self.compression_ratio == 0: return keys, values\n    scores = self.score(module, hidden_states, keys, values, attentions, kwargs)\n    n_kept = int(seq_len * (1 - self.compression_ratio))\n    indices = scores.topk(n_kept, dim=-1).indices          # (batch, heads, n_kept)\n    indices_exp = indices.unsqueeze(-1).expand(-1,-1,-1, head_dim)\n    keys = keys.gather(2, indices_exp).contiguous()        # (batch, heads, n_kept, dim)\n    values = values.gather(2, indices_exp).contiguous()\n    return keys, values\n\n# 关键: score 返回 per-head 粒度 → 每个 KV head 独立决定保留哪些 token\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
    "old_string": "### 3.2 核心接口\n\n```python\n# 使用方式 (context manager)\nwith press(model):\n    outputs = model.generate(...)\n\n# ScorerPress 子类需实现:\ndef score(self, module, hidden_states, keys, values, attentions, kwargs):\n    \"\"\"\n    返回 shape: [batch_size, num_kv_heads, seq_len]\n    分数越高 = token 越重要 = 越不会被剪\n    \"\"\"\n    ...\n\n# 基类自动处理:\n# 1. 注册 forward hook 到每个 attention layer\n# 2. 调用 score() 获取分数\n# 3. topk 保留 n_kept = int(seq_len * (1 - compression_ratio)) 个 token\n# 4. gather key/value tensors\n```",
    "new_string": "### 3.2 核心接口\n\n```python\n# 使用方式 (context manager)\nwith press(model):\n    outputs = model.generate(...)\n\n# ScorerPress 子类需实现:\ndef score(self, module: nn.Module, hidden_states: torch.Tensor,\n          keys: torch.Tensor,       # (batch, num_kv_heads, seq_len, head_dim)\n          values: torch.Tensor,     # (batch, num_kv_heads, seq_len, head_dim)\n          attentions: torch.Tensor, # (batch, num_heads, seq_len, seq_len)\n          kwargs: dict\n    ) -> torch.Tensor:              # (batch, num_kv_heads, seq_len) ← per-head 粒度\n    \"\"\"分数越高 = token 越重要 = 越不会被剪\"\"\"\n    ...\n\n# ScorerPress.compress() 的实际实现:\ndef compress(self, module, hidden_states, keys, values, attentions, kwargs):\n    if self.compression_ratio == 0: return keys, values\n    scores = self.score(module, hidden_states, keys, values, attentions, kwargs)\n    n_kept = int(seq_len * (1 - self.compression_ratio))\n    indices = scores.topk(n_kept, dim=-1).indices          # (batch, heads, n_kept)\n    indices_exp = indices.unsqueeze(-1).expand(-1,-1,-1, head_dim)\n    keys = keys.gather(2, indices_exp).contiguous()        # (batch, heads, n_kept, dim)\n    values = values.gather(2, indices_exp).contiguous()\n    return keys, values\n\n# 关键: score 返回 per-head 粒度 → 每个 KV head 独立决定保留哪些 token\n```"
  }
}
````

</details>

---

### Tool result

_source line 38 · 2026-05-14T04:59:55.496920+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T04:59:55.497105+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
  "old_string": "### 6.3 风险与未知\n\n1. **ProphetKV 假设 RAG 场景** — CompressLink 的 general compression 场景中 query 的预测力是否同样强需要验证\n2. **Expected Attention 的 Gaussian 假设** — 实际 hidden states 未必 Gaussian，需要验证误差\n3. **p_r 在 RABA 中的反向使用** — ProphetKV 用 p_r 选 token 做 recompute，RABA 用 p_r 决定 bit allocation，逻辑一致性需要理论分析\n4. **Per-layer vs Global p_r** — KVTC 是 per-layer 操作，但 ProphetKV 建议 fusion 效果更好，需要实验对比",
  "new_string": "### 6.3 风险与未知\n\n1. **ProphetKV 假设 RAG 场景** — CompressLink 的 general compression 场景中 query 的预测力是否同样强需要验证\n2. **Expected Attention 的 Gaussian 假设** — 实际 hidden states 未必 Gaussian，需要验证误差\n3. **p_r 在 RABA 中的反向使用** — ProphetKV 用 p_r 选 token 做 recompute，RABA 用 p_r 决定 bit allocation，逻辑一致性需要理论分析\n4. **Per-layer vs Global p_r** — KVTC 是 per-layer 操作，但 ProphetKV 建议 fusion 效果更好，需要实验对比\n5. **NoPE 兼容性** — ProphetKV 和 kvpress 都假设标准 RoPE attention。MEPIC 存储 NoPE KV cache (不含位置编码)，query 侧加 RoPE。计算 p_r 时需手动做 RoPE-query × NoPE-key attention，不能直接用 HF 的 output_attentions=True\n6. **Boundary tokens 硬约束** — MEPIC chunk 边界 token 的 p_r 必须 = 1.0（RABA 给 0 bits，反正要 recompute）。CEGR budget 应排除 boundary tokens（mandatory ~5-10%），discretionary budget 仅 ~10-15%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
    "old_string": "### 6.3 风险与未知\n\n1. **ProphetKV 假设 RAG 场景** — CompressLink 的 general compression 场景中 query 的预测力是否同样强需要验证\n2. **Expected Attention 的 Gaussian 假设** — 实际 hidden states 未必 Gaussian，需要验证误差\n3. **p_r 在 RABA 中的反向使用** — ProphetKV 用 p_r 选 token 做 recompute，RABA 用 p_r 决定 bit allocation，逻辑一致性需要理论分析\n4. **Per-layer vs Global p_r** — KVTC 是 per-layer 操作，但 ProphetKV 建议 fusion 效果更好，需要实验对比",
    "new_string": "### 6.3 风险与未知\n\n1. **ProphetKV 假设 RAG 场景** — CompressLink 的 general compression 场景中 query 的预测力是否同样强需要验证\n2. **Expected Attention 的 Gaussian 假设** — 实际 hidden states 未必 Gaussian，需要验证误差\n3. **p_r 在 RABA 中的反向使用** — ProphetKV 用 p_r 选 token 做 recompute，RABA 用 p_r 决定 bit allocation，逻辑一致性需要理论分析\n4. **Per-layer vs Global p_r** — KVTC 是 per-layer 操作，但 ProphetKV 建议 fusion 效果更好，需要实验对比\n5. **NoPE 兼容性** — ProphetKV 和 kvpress 都假设标准 RoPE attention。MEPIC 存储 NoPE KV cache (不含位置编码)，query 侧加 RoPE。计算 p_r 时需手动做 RoPE-query × NoPE-key attention，不能直接用 HF 的 output_attentions=True\n6. **Boundary tokens 硬约束** — MEPIC chunk 边界 token 的 p_r 必须 = 1.0（RABA 给 0 bits，反正要 recompute）。CEGR budget 应排除 boundary tokens（mandatory ~5-10%），discretionary budget 仅 ~10-15%"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T04:59:55.497359+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T04:59:55.497560+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "prophetkv_survey_v2",
  "type": "report",
  "description": "ProphetKV/SnapKV/kvpress 调研报告 v2：方法对比、核心公式、CompressLink query relevance probe 实现方案、代码量估计",
  "project": "distill_kv_rag_cache",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
  "tags": "['prophetkv', 'snapkv', 'kvpress', 'query-relevance', 'kv-cache', 'survey']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "prophetkv_survey_v2",
    "type": "report",
    "description": "ProphetKV/SnapKV/kvpress 调研报告 v2：方法对比、核心公式、CompressLink query relevance probe 实现方案、代码量估计",
    "project": "distill_kv_rag_cache",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md",
    "tags": "['prophetkv', 'snapkv', 'kvpress', 'query-relevance', 'kv-cache', 'survey']"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T04:59:55.497949+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_80c1f0\", \"name\": \"prophetkv_survey_v2\", \"type\": \"report\", \"description\": \"ProphetKV/SnapKV/kvpress 调研报告 v2：方法对比、核心公式、CompressLink query relevance probe 实现方案、代码量估计\", \"path\": \"projects/distill_kv_rag_cache/artifacts/_project/report/prophetkv_survey_80c1f0.md\", \"url\": null, \"project\": \"distill_kv_rag_cache\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T04:59:41.662534+00:00\", \"tags\": [\"prophetkv\", \"snapkv\", \"kvpress\", \"query-relevance\", \"kv-cache\", \"survey\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-14T04:59:55.498147+00:00_

报告已完成并注册。核心结论：

**ProphetKV 方法**: 用 query attention column sum 跨所有层融合（$\bar{\alpha}(t) = \frac{1}{L}\sum_l \alpha_l(t)$），20% recomputation 达 96-101% full prefill 精度。明确拒绝 early-layer prediction。无开源代码但公式简单可复现。

**推荐实现路径**:
1. **MVP Phase 0**: 位置先验 p_r（boundary=1.0, 其余 uniform），~50 行，验证 RABA/CEGR pipeline
2. **Phase 1**: ProphetKV-style query probe — hook 到 HF attention layers，收集 per-layer attention column sum，均值融合，~200 行
3. **RABA 集成**: p_r 高的 token 分配更少 compression bits (weight = 1-p_r)，~100 行修改 KVTC DP solver
4. **CEGR 集成**: restore_score = p_r × compression_error，topk 选择，~80 行

**关键风险**: MEPIC NoPE KV cache 与标准 RoPE attention 不兼容，需手动实现 RoPE-query × NoPE-key attention 计算 p_r。kvpress 的 hook 机制可复用但 attention 计算需定制。

**总代码量**: ~580 行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_prophetkv-survey-v2_20260514T045403"
}
```

</details>

---
