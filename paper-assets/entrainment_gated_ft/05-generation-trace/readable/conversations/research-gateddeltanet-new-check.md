# research gateddeltanet new check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_research_gateddeltanet-new-check_20260518T051249.jsonl`
- **Structured JSON:** [`1b6a8794a0b10af8e0d3.json`](../../sessions/1b/1b6a8794a0b10af8e0d3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-18T05:14:33.658772+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T05:14:33.659097+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T05:14:33.659270+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-hybrid-3-1/raw/main/config.json",
  "prompt": "Return the complete JSON content exactly as-is, no modifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-hybrid-3-1/raw/main/config.json",
    "prompt": "Return the complete JSON content exactly as-is, no modifications."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T05:14:33.659432+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1/raw/main/config.json",
  "prompt": "Return the complete JSON content exactly as-is, no modifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1/raw/main/config.json",
    "prompt": "Return the complete JSON content exactly as-is, no modifications."
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T05:14:33.659561+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1/raw/main/config.json",
  "prompt": "Return the complete JSON content exactly as-is, no modifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1/raw/main/config.json",
    "prompt": "Return the complete JSON content exactly as-is, no modifications."
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T05:14:33.659741+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/DeltaNet/deltanet_340M_24.json",
  "architectures": [
    "DeltaNetForCausalLM"
  ],
  "attn": {
    "layers": [
      23
    ],
    "num_heads": 16,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "rope_theta": 10000.0,
    "window_size": null
  },
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "delta_net",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 8,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_beta": true,
  "use_cache": true,
  "use_gate": false,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T05:14:33.659902+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/GatedDeltaNet/gated_deltanet_340M_24.json",
  "architectures": [
    "GatedDeltaNetForCausalLM"
  ],
  "attn": {
    "layers": [
      23
    ],
    "num_heads": 32,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "rope_theta": 10000.0,
    "window_size": null
  },
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "gated_deltanet",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": false,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_beta": true,
  "use_cache": true,
  "use_gate": true,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T05:14:33.660060+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/GatedDeltaNet/gated_deltanet_340M_3.json",
  "architectures": [
    "GatedDeltaNetForCausalLM"
  ],
  "attn": {
    "layers": [
      2,
      5,
      8,
      11,
      14,
      17,
      20,
      23
    ],
    "num_heads": 16,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "rope_theta": 10000.0,
    "window_size": null
  },
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "gated_deltanet",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": false,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_beta": true,
  "use_cache": true,
  "use_gate": true,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

This is a configuration file for a **GatedDeltaNet** model (340M parameters) with causal language modeling capabilities. Key specifications include:

- **Architecture**: 24 hidden layers with attention at specific positions (2, 5, 8, 11, 14, 17, 20, 23)
- **Model Dimensions**: 1024 hidden size, 256 head dimension
- **Attention**: 4 heads (main), 16 heads + 8 KV heads in attention layers, chunked attention mode
- **Context Length**: 2048 maximum position embeddings
- **Vocabulary**: 32,000 tokens
- **Optimizations**: Fused operations (norm, cross-entropy, SwiGLU), short convolution, gating mechanism

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T05:14:33.660250+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-hybrid-6-1/raw/main/config.json",
  "prompt": "Return the complete JSON content exactly as-is, no modifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-hybrid-6-1/raw/main/config.json",
    "prompt": "Return the complete JSON content exactly as-is, no modifications."
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T05:14:33.660377+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-hybrid-12-1/raw/main/config.json",
  "prompt": "Return the complete JSON content exactly as-is, no modifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-hybrid-12-1/raw/main/config.json",
    "prompt": "Return the complete JSON content exactly as-is, no modifications."
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T05:14:33.660512+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/GatedDeltaNet/gated_deltanet_340M_6.json",
  "architectures": [
    "GatedDeltaNetForCausalLM"
  ],
  "attn": {
    "layers": [
      6,
      11,
      17,
      23
    ],
    "num_heads": 32,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "rope_theta": 10000.0,
    "window_size": null
  },
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "gated_deltanet",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": false,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_beta": true,
  "use_cache": true,
  "use_gate": true,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T05:14:33.660693+00:00_

```json
{
  "architectures": [
    "GatedDeltaNetForCausalLM"
  ],
  "attn": {
    "layers": [
      11,
      23
    ],
    "num_heads": 32,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "rope_theta": 10000.0,
    "window_size": null
  },
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "gated_deltanet",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": false,
  "torch_dtype": "float32",
  "transformers_version": "4.51.3",
  "use_beta": true,
  "use_cache": true,
  "use_gate": true,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T05:14:33.660887+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-pure-baseline/raw/main/config.json",
  "prompt": "Return the complete JSON content exactly as-is, no modifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-pure-baseline/raw/main/config.json",
    "prompt": "Return the complete JSON content exactly as-is, no modifications."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T05:14:33.661029+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/GatedDeltaNet/gated_deltanet_340M.json",
  "architectures": [
    "GatedDeltaNetForCausalLM"
  ],
  "attn": null,
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "gated_deltanet",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": false,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_beta": true,
  "use_cache": true,
  "use_gate": true,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T05:14:33.661221+00:00_

## 结论：GatedDeltaNet-New 24:1 与标准 GatedDeltaNet 架构完全一致

"New" 仅是命名差异，不代表架构变化。可以直接作为 GatedDeltaNet 系列的 24:1 使用。

### 全系列 config 关键字段对比

| 字段 | pure | 3:1 | 6:1 | 12:1 | **24:1 (New)** |
|------|------|-----|-----|------|----------------|
| `model_type` | `gated_deltanet` | `gated_deltanet` | `gated_deltanet` | `gated_deltanet` | `gated_deltanet` |
| `architectures` | `GatedDeltaNetForCausalLM` | 同左 | 同左 | 同左 | 同左 |
| `hidden_size` | 1024 | 1024 | 1024 | 1024 | 1024 |
| `num_hidden_layers` | 24 | 24 | 24 | 24 | 24 |
| `num_heads` (linear attn) | 4 | 4 | 4 | 4 | 4 |
| `head_dim` | 256 | 256 | 256 | 256 | 256 |
| `hidden_ratio` | 4 | 4 | 4 | 4 | 4 |
| `attn.layers` | null | 8层 | 4层 | 2层 | **1层 [23]** |
| `attn.num_heads` | - | **16** | 32 | 32 | 32 |
| `attn.num_kv_heads` | - | 8 | 8 | 8 | 8 |
| `use_gate` | true | true | true | true | true |
| `use_beta` | true | true | true | true | true |
| `tie_word_embeddings` | false | false | false | false | false |
| `qk_activation` | silu | silu | silu | silu | silu |
| `qk_norm` | l2 | l2 | l2 | l2 | l2 |

### 分析

1. **架构完全一致**：`model_type`、`architectures`、所有核心超参（hidden_size, num_hidden_layers, num_heads, head_dim 等）在 New 24:1 和标准版之间完全相同。

2. **唯一变化是 ratio 本身**：`attn.layers` 从 8 层（3:1）递减到 1 层（24:1），符合 ratio 定义。

3. **`attn.num_heads` 差异不是 New 的问题**：3:1 用 16，而 6:1、12:1、24:1 统一用 32。3:1 才是异类，24:1 (New) 反而与 6:1 和 12:1 一致。这个差异仅影响 softmax attention 层的 head 数，不影响 linear attention 层。

4. **DeltaNet 24:1 不可替代**：它是完全不同的架构（`model_type=delta_net`，`use_gate=false`，`num_heads=8`，`tie_word_embeddings=true`，无 `head_dim` 字段）。

### 结论

**直接使用 `m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1` 作为 GatedDeltaNet 系列的 24:1 变体**，无需任何额外处理。不要用 DeltaNet 24:1 替代。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_gateddeltanet-new-check_20260518T051249"
}
```

</details>

---
