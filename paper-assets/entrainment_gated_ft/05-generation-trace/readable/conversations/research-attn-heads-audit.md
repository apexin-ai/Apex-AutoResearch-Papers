# research attn heads audit

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_research_attn-heads-audit_20260518T055457.jsonl`
- **Structured JSON:** [`be969fc972160b3eb2dd.json`](../../sessions/be/be969fc972160b3eb2dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-18T05:55:46.361350+00:00_

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
  "session": "worker_research_attn-heads-audit_20260518T055457",
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

_source line 2 · 2026-05-18T05:55:46.361675+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T05:55:46.361878+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-HGRN2-pure-baseline/raw/main/config.json",
  "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-HGRN2-pure-baseline/raw/main/config.json",
    "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T05:55:46.362010+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-HGRN2-hybrid-24-1/raw/main/config.json",
  "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-HGRN2-hybrid-24-1/raw/main/config.json",
    "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T05:55:46.362132+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-HGRN2-hybrid-12-1/raw/main/config.json",
  "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-HGRN2-hybrid-12-1/raw/main/config.json",
    "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T05:55:46.362249+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-HGRN2-hybrid-6-1/raw/main/config.json",
  "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-HGRN2-hybrid-6-1/raw/main/config.json",
    "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T05:55:46.362401+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/HGRN2/hgrn2_340M_hybrid_24.json",
  "architectures": [
    "HGRN2ForCausalLM"
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
  "elementwise_affine": true,
  "eos_token_id": 2,
  "expand_ratio": 128,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "hgrn2",
  "norm_eps": 1e-06,
  "num_heads": 8,
  "num_hidden_layers": 24,
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_cache": true,
  "use_lower_bound": true,
  "use_short_conv": false,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T05:55:46.362602+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-HGRN2-hybrid-3-1/raw/main/config.json",
  "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-HGRN2-hybrid-3-1/raw/main/config.json",
    "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T05:55:46.362790+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/HGRN2/hgrn2_340M.json",
  "architectures": [
    "HGRN2ForCausalLM"
  ],
  "attn": null,
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "elementwise_affine": true,
  "eos_token_id": 2,
  "expand_ratio": 128,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "hgrn2",
  "norm_eps": 1e-06,
  "num_heads": 8,
  "num_hidden_layers": 24,
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_cache": true,
  "use_lower_bound": true,
  "use_short_conv": false,
  "vocab_size": 32000
}
```

This is the configuration file for the **HGRN2 340M** model, a causal language model with:
- **24 layers** with **8 attention heads**
- **1024 hidden dimensions** with **4x hidden ratio**
- **2048 max position embeddings** (context length)
- **32,000 vocabulary size**
- Optimizations: fused cross-entropy, norm, and SwiGLU operations
- Chunk-based attention mode with 4-sized convolutions
- Compatible with Hugging Face Transformers 4.49.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T05:55:46.362940+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-RetNet-pure/raw/main/config.json",
  "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-RetNet-pure/raw/main/config.json",
    "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T05:55:46.363080+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/HGRN2/hgrn2_340M_hybrid_12.json",
  "architectures": [
    "HGRN2ForCausalLM"
  ],
  "attn": {
    "layers": [
      11,
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
  "elementwise_affine": true,
  "eos_token_id": 2,
  "expand_ratio": 128,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "hgrn2",
  "norm_eps": 1e-06,
  "num_heads": 8,
  "num_hidden_layers": 24,
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_cache": true,
  "use_lower_bound": true,
  "use_short_conv": false,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T05:55:46.363205+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-RetNet-hybrid-24-1/raw/main/config.json",
  "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-RetNet-hybrid-24-1/raw/main/config.json",
    "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T05:55:46.363337+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/HGRN2/hgrn2_340M_hybrid_6.json",
  "architectures": [
    "HGRN2ForCausalLM"
  ],
  "attn": {
    "layers": [
      5,
      11,
      17,
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
  "elementwise_affine": true,
  "eos_token_id": 2,
  "expand_ratio": 128,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "hgrn2",
  "norm_eps": 1e-06,
  "num_heads": 8,
  "num_hidden_layers": 24,
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_cache": true,
  "use_lower_bound": true,
  "use_short_conv": false,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T05:55:46.363505+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-RetNet-hybrid-12-1/raw/main/config.json",
  "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-RetNet-hybrid-12-1/raw/main/config.json",
    "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T05:55:46.363659+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/HGRN2/hgrn2_340M_hybrid_3.json",
  "architectures": [
    "HGRN2ForCausalLM"
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
  "elementwise_affine": true,
  "eos_token_id": 2,
  "expand_ratio": 128,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "hgrn2",
  "norm_eps": 1e-06,
  "num_heads": 8,
  "num_hidden_layers": 24,
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_cache": true,
  "use_lower_bound": true,
  "use_short_conv": false,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T05:55:46.363791+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-RetNet-hybrid-6-1/raw/main/config.json",
  "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-RetNet-hybrid-6-1/raw/main/config.json",
    "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T05:55:46.363920+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/RetNet/retnet_340M.json",
  "architectures": [
    "RetNetForCausalLM"
  ],
  "attn": null,
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "clamp_min": null,
  "conv_size": 4,
  "elementwise_affine": true,
  "eos_token_id": 2,
  "expand_k": 0.5,
  "expand_v": 1,
  "feature_map": null,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "retnet",
  "norm_eps": 1e-06,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "num_kv_heads": null,
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_cache": true,
  "use_output_gate": true,
  "use_short_conv": false,
  "vocab_size": 32000
}
```

This is a configuration file for a **RetNet 340M** causal language model with 24 layers, 1024 hidden dimensions, 4 attention heads, and a 32k token vocabulary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T05:55:46.364041+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-RetNet-hybrid-3-1/raw/main/config.json",
  "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-RetNet-hybrid-3-1/raw/main/config.json",
    "prompt": "Return the FULL JSON content exactly as-is, no summarization. I need every field."
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T05:55:46.364173+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/RetNet/retnet_340M_hybrid_24.json",
  "architectures": [
    "RetNetForCausalLM"
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
  "clamp_min": null,
  "conv_size": 4,
  "elementwise_affine": true,
  "eos_token_id": 2,
  "expand_k": 0.5,
  "expand_v": 1,
  "feature_map": null,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "retnet",
  "norm_eps": 1e-06,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "num_kv_heads": null,
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_cache": true,
  "use_output_gate": true,
  "use_short_conv": false,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T05:55:46.364315+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/RetNet/retnet_340M_hybrid_12.json",
  "architectures": [
    "RetNetForCausalLM"
  ],
  "attn": {
    "layers": [
      11,
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
  "clamp_min": null,
  "conv_size": 4,
  "elementwise_affine": true,
  "eos_token_id": 2,
  "expand_k": 0.5,
  "expand_v": 1,
  "feature_map": null,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "retnet",
  "norm_eps": 1e-06,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "num_kv_heads": null,
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_cache": true,
  "use_output_gate": true,
  "use_short_conv": false,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T05:55:46.364454+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/RetNet/retnet_340M_hybrid_3.json",
  "architectures": [
    "RetNetForCausalLM"
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
  "clamp_min": null,
  "conv_size": 4,
  "elementwise_affine": true,
  "eos_token_id": 2,
  "expand_k": 0.5,
  "expand_v": 1,
  "feature_map": null,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "retnet",
  "norm_eps": 1e-06,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "num_kv_heads": null,
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_cache": true,
  "use_output_gate": true,
  "use_short_conv": false,
  "vocab_size": 32000
}
```

This is a RetNet 340M hybrid model configuration with 24 hidden layers, 1024 hidden dimensions, and 32K vocabulary size. Attention is applied selectively to 8 specific layers using chunked attention mode with RoPE positional embeddings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T05:55:46.364596+00:00_

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/RetNet/retnet_340M_hybrid_6.json",
  "architectures": [
    "RetNetForCausalLM"
  ],
  "attn": {
    "layers": [
      5,
      11,
      17,
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
  "clamp_min": null,
  "conv_size": 4,
  "elementwise_affine": true,
  "eos_token_id": 2,
  "expand_k": 0.5,
  "expand_v": 1,
  "feature_map": null,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "retnet",
  "norm_eps": 1e-06,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "num_kv_heads": null,
  "tie_word_embeddings": true,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_cache": true,
  "use_output_gate": true,
  "use_short_conv": false,
  "vocab_size": 32000
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_attn-heads-audit_20260518T055457",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-18T05:55:46.364817+00:00_

全部数据已获取。

## 对比表

### HGRN2

| Ratio | attn.num_heads | attn.num_kv_heads | head_dim | attn.layers | 其他 attn 参数 |
|-------|---------------|-------------------|----------|-------------|---------------|
| pure  | N/A (attn=null) | N/A | N/A | N/A | recurrent num_heads=8 |
| 24:1  | **16** | **8** | 64 | [23] | qkv_bias=false, rope_theta=10000, window_size=null |
| 12:1  | **16** | **8** | 64 | [11, 23] | 同上 |
| 6:1   | **16** | **8** | 64 | [5, 11, 17, 23] | 同上 |
| 3:1   | **16** | **8** | 64 | [2, 5, 8, 11, 14, 17, 20, 23] | 同上 |

### RetNet

| Ratio | attn.num_heads | attn.num_kv_heads | head_dim | attn.layers | 其他 attn 参数 |
|-------|---------------|-------------------|----------|-------------|---------------|
| pure  | N/A (attn=null) | N/A | N/A | N/A | recurrent num_heads=4 |
| 24:1  | **16** | **8** | 64 | [23] | qkv_bias=false, rope_theta=10000, window_size=null |
| 12:1  | **16** | **8** | 64 | [11, 23] | 同上 |
| 6:1   | **16** | **8** | 64 | [5, 11, 17, 23] | 同上 |
| 3:1   | **16** | **8** | 64 | [2, 5, 8, 11, 14, 17, 20, 23] | 同上 |

## 结论

1. **HGRN2 各 ratio 之间完全一致。** 所有 hybrid 变体的 full attention 层配置完全相同：num_heads=16, num_kv_heads=8, head_dim=64。唯一区别是 attention 层的数量和位置（均匀分布在 24 层中）。

2. **RetNet 各 ratio 之间完全一致。** 与 HGRN2 完全相同的 attention 配置。

3. **HGRN2 和 RetNet 之间也完全一致。** 两者的 hybrid attention 层使用了完全相同的 num_heads/num_kv_heads 配置。

4. **与 GatedDeltaNet 的对比：GatedDeltaNet 是唯一存在 cross-ratio 不一致的架构。** GatedDeltaNet 的 3:1 ratio 使用 num_heads=16，而 6:1/12:1/24:1 使用 num_heads=32。HGRN2 和 RetNet 不存在这个问题。

### 影响评估

HGRN2 和 RetNet 的 cross-ratio 实验可比性没有问题。GatedDeltaNet 3:1 的 num_heads 差异（16 vs 32）是该架构独有的配置异常，意味着 GatedDeltaNet 3:1 的 attention 层 head_dim=64，而其他 ratio 的 head_dim=32。这可能混淆 ratio 效果和 head 配置效果的归因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_attn-heads-audit_20260518T055457"
}
```

</details>

---
