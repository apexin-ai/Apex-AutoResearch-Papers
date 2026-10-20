# code ifr perhead diagnostic

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_code_ifr-perhead-diagnostic_20260513T073307.jsonl`
- **Structured JSON:** [`00f8186980d3046c28ea.json`](../../sessions/00/00f8186980d3046c28ea.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-13T07:37:22.482943+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T07:37:22.483263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T07:37:22.483430+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "cat /root/structfuse-context/ifr_scoring.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "cat /root/structfuse-context/ifr_scoring.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T07:37:22.483561+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "ls -la /root/structfuse-context/results/Qwen_Qwen2.5_0.5B_ioi/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "ls -la /root/structfuse-context/results/Qwen_Qwen2.5_0.5B_ioi/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-13T07:37:22.483861+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"from __future__ import annotations\\n\\nimport os\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"0\\\")\\n\\n\\\"\\\"\\\"IFR (Information Flow Routes) edge-level scoring for HuggingFace models.\\n\\nImplements ALTI-based proximity attribution from:\\n  Ferrando & Voita, \\\"Information Flow Routes: Automatically Interpreting\\n  Language Models at Scale\\\", EMNLP 2024.\\n\\nScores each edge (u->v) by how much source u's output is \\\"present\\\" in the\\nresidual stream that destination v reads from:\\n\\n    score(u->v) = max(||x_v||_1 - ||y_u - x_v||_1, 0)\\n\\nwhere y_u = component u's output, x_v = residual stream input to component v.\\n\\nInput:\\n  - model: HuggingFace CausalLM (Llama, Qwen2, Gemma2, Mistral, GPT2)\\n  - dataset: tokenized examples (list[dict], dict with input_ids, or Tensor)\\n  - metric_fn: unused — kept for interface parity with EAP-IG / Edge Pruning\\n\\nOutput:\\n  - Dict[str, float] mapping canonical edge names to proximity scores (>=0).\\n    Format: \\\"{src}->{dst}\\\"\\n    Nodes: input, a{L}.h{H}, m{L}\\n    Attention destinations carry .q/.k/.v suffix: a{L}.h{H}.q\\n\\nDependencies: torch, transformers\\n\\\"\\\"\\\"\\n\\n\\nimport torch\\nimport torch.nn as nn\\nfrom typing import Dict, Callable, Union\\n\\n\\n# -----------------------------------------------------------------------------\\n# Core proximity metric (ALTI)\\n# -----------------------------------------------------------------------------\\n\\ndef _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:\\n    \\\"\\\"\\\"max(||x_v||_1 - ||y_u - x_v||_1, 0), averaged over batch & sequence.\\\"\\\"\\\"\\n    diff_norm = (y_u - x_v).abs().sum(dim=-1)\\n    base_norm = x_v.abs().sum(dim=-1)\\n    return (base_norm - diff_norm).clamp(min=0).mean().item()\\n\\n\\n# -----------------------------------------------------------------------------\\n# Architecture detection\\n# --------------------------------
…[truncated 7026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T07:37:22.484051+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x 2 root root   51 May 13 15:25 .\\ndrwxr-xr-x 3 root root   43 May 13 15:25 ..\\n-rw-r--r-- 1 root root 1754 May 13 15:25 Qwen_Qwen2.5_0.5B_ioi_K3.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T07:37:22.484221+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "cat /root/structfuse-context/results/Qwen_Qwen2.5_0.5B_ioi/Qwen_Qwen2.5_0.5B_ioi_K3.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "cat /root/structfuse-context/results/Qwen_Qwen2.5_0.5B_ioi/Qwen_Qwen2.5_0.5B_ioi_K3.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T07:37:22.484402+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment_id\\\": \\\"phase2_qwen05b_ioi_k3\\\",\\n  \\\"model\\\": \\\"Qwen/Qwen2.5-0.5B\\\",\\n  \\\"task\\\": \\\"ioi\\\",\\n  \\\"K\\\": 3,\\n  \\\"num_samples\\\": 100,\\n  \\\"seed\\\": 42,\\n  \\\"binarize\\\": {\\n    \\\"strategy\\\": \\\"topn\\\",\\n    \\\"n\\\": 100\\n  },\\n  \\\"baseline_io_s_diff\\\": 7.0764,\\n  \\\"method_edge_counts\\\": {\\n    \\\"eap_ig\\\": 179388,\\n    \\\"edge_pruning\\\": 179388,\\n    \\\"ifr\\\": 141384\\n  },\\n  \\\"binarized_counts\\\": {\\n    \\\"eap_ig\\\": 100,\\n    \\\"edge_pruning\\\": 100,\\n    \\\"ifr\\\": 100\\n  },\\n  \\\"css_distribution\\\": {\\n    \\\"1/3\\\": 160,\\n    \\\"2/3\\\": 70\\n  },\\n  \\\"css_core_count\\\": 0,\\n  \\\"css_core_edges\\\": [],\\n  \\\"off_diagonal_pct\\\": 1.0,\\n  \\\"pairwise_jaccard\\\": {\\n    \\\"eap_ig_vs_edge_pruning\\\": 0.5385,\\n    \\\"eap_ig_vs_ifr\\\": 0.0,\\n    \\\"edge_pruning_vs_ifr\\\": 0.0\\n  },\\n  \\\"faithfulness\\\": {\\n    \\\"css_core\\\": {\\n      \\\"zero\\\": {\\n        \\\"full_metric\\\": 7.0764,\\n        \\\"circuit_metric\\\": -0.0044,\\n        \\\"cpr\\\": -0.0006\\n      },\\n      \\\"mean\\\": {\\n        \\\"full_metric\\\": 7.0764,\\n        \\\"circuit_metric\\\": -0.1083,\\n        \\\"cpr\\\": -0.0153\\n      }\\n    },\\n    \\\"eap_ig\\\": {\\n      \\\"zero\\\": {\\n        \\\"full_metric\\\": 7.0764,\\n        \\\"circuit_metric\\\": 0.0467,\\n        \\\"cpr\\\": 0.0066\\n      },\\n      \\\"mean\\\": {\\n        \\\"full_metric\\\": 7.0764,\\n        \\\"circuit_metric\\\": -0.1148,\\n        \\\"cpr\\\": -0.0162\\n      }\\n    },\\n    \\\"edge_pruning\\\": {\\n      \\\"zero\\\": {\\n        \\\"full_metric\\\": 7.0764,\\n        \\\"circuit_metric\\\": 0.0706,\\n        \\\"cpr\\\": 0.01\\n      },\\n      \\\"mean\\\": {\\n        \\\"full_metric\\\": 7.0764,\\n        \\\"circuit_metric\\\": 0.1379,\\n        \\\"cpr\\\": 0.0195\\n      }\\n    },
…[truncated 518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T07:37:22.484552+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "grep -n \"_decompose_per_head\\|_src_label\\|def \" /root/structfuse-context/ifr_scoring.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "grep -n \"_decompose_per_head\\|_src_label\\|def \" /root/structfuse-context/ifr_scoring.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T07:37:22.484674+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T07:37:22.484863+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "grep -n \"def \" /root/structfuse-context/ifr_scoring.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "grep -n \"def \" /root/structfuse-context/ifr_scoring.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T07:37:22.484988+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "cat /root/structfuse-context/css.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "cat /root/structfuse-context/css.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T07:37:22.485113+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"43:def _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:\\n59:def _get_model_info(model) -> dict:\\n92:def _before_attn(kind: str, src_layer: int, dst_layer: int) -> bool:\\n98:def _before_mlp(kind: str, src_layer: int, dst_layer: int) -> bool:\\n110:def _prepare_tokens(\\n142:def _decompose_per_head(\\n174:def _src_label(kind: str, layer: int, head: int) -> str:\\n186:def compute_ifr_edges(\\n220:        def _pre(mod, inp, *, _l=l_idx):\\n232:        def _oproj(mod, inp, out, *, _l=l_idx):\\n240:        def _mlp(mod, inp, out, *, _l=l_idx):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T07:37:22.485314+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"0\\\")\\n\\n\\\"\\\"\\\"\\nCSS (Cross-method Stability Scoring) binarization and consensus module.\\n\\nProvides multiple binarization strategies for converting continuous edge scores\\nto binary circuit membership, then computes cross-method consensus.\\n\\nD010: IFR proximity scores are identical for all heads in the same (src, dst_layer).\\nTop-N binarization causes block-voting. Use percentile_threshold or unique_score_rank\\nto handle tied scores fairly.\\n\\\"\\\"\\\"\\n\\nfrom typing import Dict, List, Literal, Tuple\\nimport numpy as np\\n\\nBinarizeStrategy = Literal[\\\"topn\\\", \\\"threshold\\\", \\\"percentile_threshold\\\", \\\"unique_score_rank\\\"]\\n\\n\\ndef generate_nonnested_configs(\\n    node_thresholds: List[float],\\n    edge_thresholds: List[float],\\n    B: int = 9,\\n    seed: int = 42,\\n) -> List[Tuple[float, float]]:\\n    \\\"\\\"\\\"Generate B non-nested (anti-chain) configurations from 2D threshold space.\\n\\n    Anti-chain constraint: for any (n_i, e_i), (n_j, e_j),\\n    NOT (n_i <= n_j AND e_i <= e_j) — no dominance relation.\\n\\n    Method: interpolate B values per axis within the provided ranges,\\n    then select the anti-diagonal (node ascending, edge descending).\\n    This guarantees pairwise incomparability.\\n    \\\"\\\"\\\"\\n    n_lo, n_hi = min(node_thresholds), max(node_thresholds)\\n    e_lo, e_hi = min(edge_thresholds), max(edge_thresholds)\\n\\n    n_vals = np.linspace(n_lo, n_hi, B)\\n    e_vals = np.linspace(e_lo, e_hi, B)\\n\\n    return [(float(n_vals[i]), float(e_vals[B - 1 - i])) for i in range(B)]\\n\\n\\ndef binarize_scores(\\n    scores: Dict[str, float],\\n    strategy: BinarizeStrategy,\\n    *,\\n    n: int = 200,\\n    threshold: float = 0.01,\\n    percentile: float = 95.0,\\n) -> set[str]:\\n    \\\"\\\"\\\"Convert continuous edge scores to binary set of 'active' edges.\\n\\n 
…[truncated 4095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T07:37:22.485512+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "head -185 /root/structfuse-context/ifr_scoring.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "head -185 /root/structfuse-context/ifr_scoring.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T07:37:22.485752+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"from __future__ import annotations\\n\\nimport os\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"0\\\")\\n\\n\\\"\\\"\\\"IFR (Information Flow Routes) edge-level scoring for HuggingFace models.\\n\\nImplements ALTI-based proximity attribution from:\\n  Ferrando & Voita, \\\"Information Flow Routes: Automatically Interpreting\\n  Language Models at Scale\\\", EMNLP 2024.\\n\\nScores each edge (u->v) by how much source u's output is \\\"present\\\" in the\\nresidual stream that destination v reads from:\\n\\n    score(u->v) = max(||x_v||_1 - ||y_u - x_v||_1, 0)\\n\\nwhere y_u = component u's output, x_v = residual stream input to component v.\\n\\nInput:\\n  - model: HuggingFace CausalLM (Llama, Qwen2, Gemma2, Mistral, GPT2)\\n  - dataset: tokenized examples (list[dict], dict with input_ids, or Tensor)\\n  - metric_fn: unused — kept for interface parity with EAP-IG / Edge Pruning\\n\\nOutput:\\n  - Dict[str, float] mapping canonical edge names to proximity scores (>=0).\\n    Format: \\\"{src}->{dst}\\\"\\n    Nodes: input, a{L}.h{H}, m{L}\\n    Attention destinations carry .q/.k/.v suffix: a{L}.h{H}.q\\n\\nDependencies: torch, transformers\\n\\\"\\\"\\\"\\n\\n\\nimport torch\\nimport torch.nn as nn\\nfrom typing import Dict, Callable, Union\\n\\n\\n# -----------------------------------------------------------------------------\\n# Core proximity metric (ALTI)\\n# -----------------------------------------------------------------------------\\n\\ndef _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:\\n    \\\"\\\"\\\"max(||x_v||_1 - ||y_u - x_v||_1, 0), averaged over batch & sequence.\\\"\\\"\\\"\\n    diff_norm = (y_u - x_v).abs().sum(dim=-1)\\n    base_norm = x_v.abs().sum(dim=-1)\\n    return (base_norm - diff_norm).clamp(min=0).mean().item()\\n\\n\\n# -----------------------------------------------------------------------------\\n# Architecture detection\\n# --------------------------------
…[truncated 5026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T07:37:22.485957+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "tail -80 /root/structfuse-context/ifr_scoring.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "tail -80 /root/structfuse-context/ifr_scoring.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T07:37:22.486086+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "find /root/structfuse-context/results/ -type f -name \"*.pt\" -o -name \"*.pkl\" -o -name \"*scores*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "find /root/structfuse-context/results/ -type f -name \"*.pt\" -o -name \"*.pkl\" -o -name \"*scores*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T07:37:22.486204+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "ls -la /root/structfuse-context/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "ls -la /root/structfuse-context/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T07:37:22.486368+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        o_proj = (\\n            layer.self_attn.o_proj if arch == \\\"llama_like\\\"\\n            else layer.attn.c_proj\\n        )\\n\\n        def _oproj(mod, inp, out, *, _l=l_idx):\\n            cache[\\\"attn_out\\\"][_l] = out.detach()\\n            cache[\\\"head_out\\\"][_l] = _decompose_per_head(\\n                inp[0].detach(), mod, n_heads, head_dim,\\n            )\\n        hooks.append(o_proj.register_forward_hook(_oproj))\\n\\n        # 3) MLP output\\n        def _mlp(mod, inp, out, *, _l=l_idx):\\n            cache[\\\"mlp_out\\\"][_l] = (\\n                out.detach() if isinstance(out, torch.Tensor)\\n                else out[0].detach()\\n            )\\n        hooks.append(layer.mlp.register_forward_hook(_mlp))\\n\\n    # ---- single forward pass ----\\n    model.eval()\\n    try:\\n        with torch.no_grad():\\n            model(tokens)\\n    finally:\\n        for h in hooks:\\n            h.remove()\\n\\n    # ---- build source activation table: (kind, layer, head) -> [B, S, D] ----\\n    src_act: Dict[tuple, torch.Tensor] = {}\\n    src_act[(\\\"input\\\", -1, -1)] = cache[\\\"resid_pre\\\"][0]\\n\\n    for l in range(n_layers):\\n        if l in cache[\\\"head_out\\\"]:\\n            for h in range(n_heads):\\n                src_act[(\\\"attn\\\", l, h)] = cache[\\\"head_out\\\"][l][h]\\n        if l in cache[\\\"mlp_out\\\"]:\\n            src_act[(\\\"mlp\\\", l, -1)] = cache[\\\"mlp_out\\\"][l]\\n\\n    # resid_mid[L] = resid_pre[L] + attn_out[L]\\n    # (exact for Llama/Qwen2/Mistral; slight approximation for Gemma2\\n    #  which applies an extra LN on attn output before residual addition)\\n    resid_mid: Dict[int, torch.Tensor] = {}\\n    for l in range(n_layers):\\n        if l in cache[\\\"resid_pre\\\"] and l in cache[\\\"attn_out\\\"]:\\n            resid_mid[l] = cache[\\\"resid_pre\\\"][l] + cache[\\\"attn_out\\\"][l]\\n\\n    # ---- proximity scoring ----\\n    
…[truncated 1292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T07:37:22.486514+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T07:37:22.486652+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 2992\\ndrwxr-xr-x 6 root root    4096 May 13 15:25 .\\ndrwx------ 1 root root    4096 May 13 15:18 ..\\ndrwxr-xr-x 2 root root    4096 May 13 15:25 __pycache__\\n-rw-r--r-- 1 root root    5822 May 13 14:28 acdc_topk_sweep.py\\n-rw-r--r-- 1 root root   12959 May 13 14:28 analysis_fix_v3.py\\ndrwxr-xr-x 3 root root      39 May 13 15:24 cache\\n-rw-r--r-- 1 root root 1368547 May 13 15:23 cache_eap_ig_sva.json\\n-rw-r--r-- 1 root root 1352131 May 13 15:25 cache_ep_sva.json\\n-rw-r--r-- 1 root root    6533 May 13 14:28 circuit_discovery.py\\n-rw-r--r-- 1 root root    6001 May 13 14:28 circus.py\\n-rw-r--r-- 1 root root     868 May 13 14:28 config.py\\n-rw-r--r-- 1 root root    4091 May 13 14:28 cross_tabulate.py\\n-rw-r--r-- 1 root root    5443 May 13 14:28 css.py\\n-rw-r--r-- 1 root root    8146 May 13 15:16 e2e_validate.py\\n-rw-r--r-- 1 root root    9819 May 13 14:28 edge_pruning_l0.py\\n-rw-r--r-- 1 root root    5787 May 13 14:28 eval_faithfulness.py\\n-rw-r--r-- 1 root root   15176 May 13 14:28 eval_mean_ablation.py\\n-rw-r--r-- 1 root root   17573 May 13 14:28 eval_topk_faithfulness.py\\n-rw-r--r-- 1 root root    4295 May 13 14:28 evaluation.py\\n-rw-r--r-- 1 root root    5467 May 13 14:28 ifr_discovery.py\\n-rw-r--r-- 1 root root   10413 May 13 14:28 ifr_scoring.py\\ndrwxr-xr-x 2 root root      46 May 13 15:11 logs\\n-rw-r--r-- 1 root root    8956 May 13 14:28 phase2_configs.yaml\\ndrwxr-xr-x 3 root root      43 May 13 15:25 results\\n-rw-r--r-- 1 root root   15953 May 13 14:28 run_arithmetic.py\\n-rw-r--r-- 1 root root   10187 May 13 14:28 run_circus.py\\n-rw-r--r-- 1 root root    9726 May 13 14:28 run_circus_fix.py\\n-rw-r--r-- 1 root root   12870 May 13 14:28 run_mvp.py\\n-rw-r--r-- 1 root root   17344 May 13 14:28 run_phase2_experiment.py\\n-rw-r--r-- 1 root root    7277 May 13 14:28 run_phase_d_only.py\\n-rw-r--r-- 1 root root   22038 May 13 15:24 run_qwen_ioi.py\\n-rw-r--r-- 1 root root   21684 Ma
…[truncated 191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T07:37:22.486865+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "ls -la /root/structfuse-context/cache/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "ls -la /root/structfuse-context/cache/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T07:37:22.487001+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x 3 root root   39 May 13 15:24 .\\ndrwxr-xr-x 6 root root 4096 May 13 15:25 ..\\ndrwxr-xr-x 3 root root   25 May 13 15:24 Qwen_Qwen2.5_0.5B\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T07:37:22.487119+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "head -100 /root/structfuse-context/run_qwen_ioi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "head -100 /root/structfuse-context/run_qwen_ioi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T07:37:22.487304+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Phase 2: Qwen-2.5 0.5B IOI K=3 experiment.\\n\\nMethods: EAP-IG + Edge Pruning (L0) + IFR — all HuggingFace-native.\\nBinarization: top-100 for all methods.\\nEvaluation: zero + mean ablation faithfulness.\\n\\\"\\\"\\\"\\nimport os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"0\\\"\\n\\nimport sys, json, random, time, gc, math, re, logging\\nfrom pathlib import Path\\nfrom typing import Dict, Set, List, Optional\\n\\nsys.path.insert(0, \\\"/root/structfuse-context\\\")\\n\\nimport torch\\nimport torch.nn as nn\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\", datefmt=\\\"%H:%M:%S\\\")\\nlog = logging.getLogger(\\\"qwen_ioi\\\")\\n\\n# ============================================================\\n# Config\\n# ============================================================\\nMODEL_PATH = \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\\\"\\nNUM_SAMPLES = 100\\nSEED = 42\\nK = 3\\nBINARIZE_N = 100\\nEAP_IG_STEPS = 5\\nEP_EPOCHS = 100\\nEP_LAMBDA = 1e-2\\nEP_LR = 0.05\\nIFR_THRESHOLD = 0.05\\nOUTPUT_DIR = Path(\\\"results/Qwen_Qwen2.5_0.5B_ioi\\\")\\nCACHE_DIR = Path(\\\"cache/Qwen_Qwen2.5_0.5B/ioi\\\")\\nEXP_ID = \\\"phase2_qwen05b_ioi_k3\\\"\\nDEVICE = \\\"cuda\\\"\\n\\nNAMES = [\\\"John\\\",\\\"Mary\\\",\\\"Alice\\\",\\\"Bob\\\",\\\"Charlie\\\",\\\"David\\\",\\\"Emma\\\",\\\"Frank\\\",\\n         \\\"Grace\\\",\\\"Henry\\\",\\\"Jack\\\",\\\"Kate\\\",\\\"Leo\\\",\\\"Mia\\\",\\\"Noah\\\",\\\"Tom\\\"]\\nTEMPLATES = [\\n    \\\"When {io} and {s} went to the {place}, {s} gave a {obj} to\\\",\\n    \\\"After {io} and {s} arrived at the {place}, {s} handed a {obj} to\\\",\\n    \\\"{io} and {s} were at the {place}. {s} gave a {obj} to\\\",\\n    \\\"Then, {io} and {s} had a meeting at the {place}, {s} passed a {obj} to\\\",\\n]\\nPLACES = [\\\"store\\\",\\\"park\\\",\\\"library\\\",\\\"school\\\",\\\"hospital\\\",\\\"restaurant\\\",\\\"office\\\"]\\nOB
…[truncated 2244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T07:37:22.487454+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "find /root/structfuse-context/cache/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "find /root/structfuse-context/cache/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T07:37:22.487586+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse-context/cache/Qwen_Qwen2.5_0.5B/ioi/cache_eap_ig.json\\n/root/structfuse-context/cache/Qwen_Qwen2.5_0.5B/ioi/cache_edge_pruning.json\\n/root/structfuse-context/cache/Qwen_Qwen2.5_0.5B/ioi/cache_ifr.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T07:37:22.487750+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "head -30 /root/structfuse-context/cache/Qwen_Qwen2.5_0.5B/ioi/cache_ifr.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "head -30 /root/structfuse-context/cache/Qwen_Qwen2.5_0.5B/ioi/cache_ifr.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-13T07:37:22.487877+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "head -30 /root/structfuse-context/cache/Qwen_Qwen2.5_0.5B/ioi/cache_eap_ig.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "head -30 /root/structfuse-context/cache/Qwen_Qwen2.5_0.5B/ioi/cache_eap_ig.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T07:37:22.488132+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"input->a0.h0.q\\\": 10.774487495422363, \\\"input->a0.h0.k\\\": 10.774487495422363, \\\"input->a0.h0.v\\\": 10.774487495422363, \\\"input->a0.h1.q\\\": 10.774487495422363, \\\"input->a0.h1.k\\\": 10.774487495422363, \\\"input->a0.h1.v\\\": 10.774487495422363, \\\"input->a0.h2.q\\\": 10.774487495422363, \\\"input->a0.h2.k\\\": 10.774487495422363, \\\"input->a0.h2.v\\\": 10.774487495422363, \\\"input->a0.h3.q\\\": 10.774487495422363, \\\"input->a0.h3.k\\\": 10.774487495422363, \\\"input->a0.h3.v\\\": 10.774487495422363, \\\"input->a0.h4.q\\\": 10.774487495422363, \\\"input->a0.h4.k\\\": 10.774487495422363, \\\"input->a0.h4.v\\\": 10.774487495422363, \\\"input->a0.h5.q\\\": 10.774487495422363, \\\"input->a0.h5.k\\\": 10.774487495422363, \\\"input->a0.h5.v\\\": 10.774487495422363, \\\"input->a0.h6.q\\\": 10.774487495422363, \\\"input->a0.h6.k\\\": 10.774487495422363, \\\"input->a0.h6.v\\\": 10.774487495422363, \\\"input->a0.h7.q\\\": 10.774487495422363, \\\"input->a0.h7.k\\\": 10.774487495422363, \\\"input->a0.h7.v\\\": 10.774487495422363, \\\"input->a0.h8.q\\\": 10.774487495422363, \\\"input->a0.h8.k\\\": 10.774487495422363, \\\"input->a0.h8.v\\\": 10.774487495422363, \\\"input->a0.h9.q\\\": 10.774487495422363, \\\"input->a0.h9.k\\\": 10.774487495422363, \\\"input->a0.h9.v\\\": 10.774487495422363, \\\"input->a0.h10.q\\\": 10.774487495422363, \\\"input->a0.h10.k\\\": 10.774487495422363, \\\"input->a0.h10.v\\\": 10.774487495422363, \\\"input->a0.h11.q\\\": 10.774487495422363, \\\"input->a0.h11.k\\\": 10.774487495422363, \\\"input->a0.h11.v\\\": 10.774487495422363, \\\"input->a0.h12.q\\\": 10.774487495422363, \\\"input->a0.h12.k\\\": 10.774487495422363, \\\"input->a0.h12.v\\\": 10.774487495422363, \\\"input->a0.h13.q\\\": 10.774487495422363, \\\"input->a0.h13.k\\\": 10.774487495422363, \\\"input->a0.h13.v\\\": 10.774487495422363, \\\"input->m0\\\": 5.232016086578369, \\\"a0.h0->m0\\\": 0.07678630948066711, \\\"a
…[truncated 7515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T07:37:22.488462+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"input->a0.h0.q\\\": -0.0004028638650197536, \\\"input->a0.h0.k\\\": -0.0004028638650197536, \\\"input->a0.h0.v\\\": -0.0004028638650197536, \\\"input->a0.h1.q\\\": -0.0004028638650197536, \\\"input->a0.h1.k\\\": -0.0004028638650197536, \\\"input->a0.h1.v\\\": -0.0004028638650197536, \\\"input->a0.h2.q\\\": -0.0004028638650197536, \\\"input->a0.h2.k\\\": -0.0004028638650197536, \\\"input->a0.h2.v\\\": -0.0004028638650197536, \\\"input->a0.h3.q\\\": -0.0004028638650197536, \\\"input->a0.h3.k\\\": -0.0004028638650197536, \\\"input->a0.h3.v\\\": -0.0004028638650197536, \\\"input->a0.h4.q\\\": -0.0004028638650197536, \\\"input->a0.h4.k\\\": -0.0004028638650197536, \\\"input->a0.h4.v\\\": -0.0004028638650197536, \\\"input->a0.h5.q\\\": -0.0004028638650197536, \\\"input->a0.h5.k\\\": -0.0004028638650197536, \\\"input->a0.h5.v\\\": -0.0004028638650197536, \\\"input->a0.h6.q\\\": -0.0004028638650197536, \\\"input->a0.h6.k\\\": -0.0004028638650197536, \\\"input->a0.h6.v\\\": -0.0004028638650197536, \\\"input->a0.h7.q\\\": -0.0004028638650197536, \\\"input->a0.h7.k\\\": -0.0004028638650197536, \\\"input->a0.h7.v\\\": -0.0004028638650197536, \\\"input->a0.h8.q\\\": -0.0004028638650197536, \\\"input->a0.h8.k\\\": -0.0004028638650197536, \\\"input->a0.h8.v\\\": -0.0004028638650197536, \\\"input->a0.h9.q\\\": -0.0004028638650197536, \\\"input->a0.h9.k\\\": -0.0004028638650197536, \\\"input->a0.h9.v\\\": -0.0004028638650197536, \\\"input->a0.h10.q\\\": -0.0004028638650197536, \\\"input->a0.h10.k\\\": -0.0004028638650197536, \\\"input->a0.h10.v\\\": -0.0004028638650197536, \\\"input->a0.h11.q\\\": -0.0004028638650197536, \\\"input->a0.h11.k\\\": -0.0004028638650197536, \\\"input->a0.h11.v\\\": -0.0004028638650197536, \\\"input->a0.h12.q\\\": -0.0004028638650197536, \\\"input->a0.h12.k\\\": -0.0004028638650197536, \\\"input->a0.h12.v\\\": -0.0004028638650197536, \\\"input->a0.h13.q\\\": -0.0004028638650197536, \\\"input->a0
…[truncated 7364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-13T07:37:22.488782+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-pro6000",
  "command": "cat > /root/structfuse-context/diagnose_ifr_perhead.py << 'PYEOF'\n\"\"\"Diagnose IFR per-head score degeneracy and test alternative binarizations.\"\"\"\nimport json\nimport re\nfrom collections import defaultdict\nfrom pathlib import Path\n\nCACHE = Path(\"/root/structfuse-context/cache/Qwen_Qwen2.5_0.5B/ioi\")\n\ndef load_scores(name):\n    with open(CACHE / f\"cache_{name}.json\") as f:\n        return json.load(f)\n\ndef jaccard(a: set, b: set) -> float:\n    if not a and not b:\n        return 0.0\n    return len(a & b) / len(a | b)\n\ndef topn(scores, n=100):\n    sorted_edges = sorted(scores.items(), key=lambda x: abs(x[1]), reverse=True)\n    return {e for e, _ in sorted_edges[:n]}\n\ndef topn_positive(scores, n=100):\n    sorted_edges = sorted(scores.items(), key=lambda x: x[1], reverse=True)\n    return {e for e, _ in sorted_edges[:n]}\n\ndef unique_score_rank(scores, n=100):\n    unique_vals = sorted(set(abs(v) for v in scores.values()), reverse=True)\n    top_vals = set(unique_vals[:n])\n    return {e for e, v in scores.items() if abs(v) in top_vals}\n\n# Load all scores\nifr = load_scores(\"ifr\")\neap = load_scores(\"eap_ig\")\nep  = load_scores(\"edge_pruning\")\n\nprint(f\"Total edges: IFR={len(ifr)}, EAP-IG={len(eap)}, EP={len(ep)}\")\n\n# --- 1. IFR score degeneracy analysis ---\nprint(\"\\n=== IFR Score Degeneracy ===\")\nunique_ifr = set(ifr.values())\nprint(f\"Total IFR edges: {len(ifr)}\")\nprint(f\"Unique IFR scores: {len(unique_ifr)}\")\nprint(f\"Degeneracy ratio: {len(ifr)/len(unique_ifr):.1f}x\")\n\n# Group attention edges by (src, dst_layer) to show block structure\nattn_pattern = re.compile(r\"(.+)->a(\\d+)\\.h(\\d+)\\.(q|k|v)\")\ngroups = defaultdict(set)\nfor edge, score in ifr.items():\n    m = attn_pattern.match(edge)\n    if m:\n        src, layer = m.group(1), m.group(2)\n        groups[(src, layer)].add(score)\n\nn_degenerate = sum(1 for v in groups.values() if len(v) == 1)\nprint(f\"\\nAttention edge groups (src, dst_layer): {len(groups)}\")\nprint(f\"Groups with ALL heads having same score: {n_degenerate} ({n_degenerate/len(groups)*100:.0f}%)\")\n\n# MLP edges: per-head variance\nmlp_pattern = re.compile(r\"a(\\d+)\\.h(\\d+)->m(\\d+)\")\nmlp_groups = defaultdict(list)\nfor edge, score in ifr.items():\n    m = mlp_pattern.match(edge)\n    if m:\n        src_layer, dst_layer = m.group(1), m.group(3)\n        mlp_groups[(src_layer, dst_layer)].append(score)\n\nprint(f\"\\nMLP edge groups (attn_head->mlp): {len(mlp_groups)}\")\nif mlp_groups:\n    variances = []\n    for k, scores_list in mlp_groups.items():\n        if len(scores_list) > 1:\n            mean = sum(scores_list) / len(scores_list)\n            var = sum((s - mean)**2 for s in scores_list) / len(scores_list)\n            variances.append(var)\n    print(f\"Groups with >1 head: {len(variances)}\")\n    if variances:\n        print(f\"Score variance: mean={sum(variances)/len(variances):.6f}, max={max(variances):.6f}\")\n\n# Also check EAP-IG degeneracy\nunique_eap = set(eap.values())\nprint(f\"\\n=== EAP-IG Score Degeneracy ===\")\nprint(f\"Total EAP-IG edges: {len(eap)}\")\nprint(f\"Unique EAP-IG scores: {len(unique_eap)}\")\nprint(f\"Degeneracy ratio: {len(eap)/len(unique_eap):.1f}x\")\n\neap_groups = defaultdict(set)\nfor edge, score in eap.items():\n    m = attn_pattern.match(edge)\n    if m:\n        src, layer = m.group(1), m.group(2)\n        eap_groups[(src, layer)].add(score)\nn_deg_eap = sum(1 for v in eap_groups.values() if len(v) == 1)\nprint(f\"Attn groups with ALL heads same score: {n_deg_eap} ({n_deg_eap/len(eap_groups)*100:.0f}%)\")\n\n# --- 2. Binarization comparison ---\nprint(\"\\n=== Binarization: top-100 (abs value) ===\")\nifr_top = topn(ifr, 100)\neap_top = topn(eap, 100)\nep_top  = topn(ep, 100)\nprint(f\"Jaccard IFR vs EAP-IG: {jaccard(ifr_top, eap_top):.4f}\")\nprint(f\"Jaccard IFR vs EP:     {jaccard(ifr_top, ep_top):.4f}\")\nprint(f\"Jaccard EAP-IG vs EP:  {jaccard(eap_top, ep_top):.4f}\")\n\nprint(\"\\n=== Binarization: top-100 (positive only, for EAP-IG/EP) ===\")\neap_top_pos = topn_positive(eap, 100)\nep_top_pos  = topn_positive(ep, 100)\nprint(f\"Jaccard IFR vs EAP-IG: {jaccard(ifr_top, eap_top_pos):.4f}\")\nprint(f\"Jaccard IFR vs EP:     {jaccard(ifr_top, ep_top_pos):.4f}\")\nprint(f\"Jaccard EAP-IG vs EP:  {jaccard(eap_top_pos, ep_top_pos):.4f}\")\n\nprint(\"\\n=== Binarization: unique_score_rank top-100 unique values ===\")\nifr_usr = unique_score_rank(ifr, 100)\neap_usr = unique_score_rank(eap, 100)\nep_usr  = unique_score_rank(ep, 100)\nprint(f\"|IFR|={len(ifr_usr)}, |EAP|={len(eap_usr)}, |EP|={len(ep_usr)}\")\nprint(f\"Jaccard IFR vs EAP-IG: {jaccard(ifr_usr, eap_usr):.4f}\")\nprint(f\"Jaccard IFR vs EP:     {jaccard(ifr_usr, ep_usr):.4f}\")\nprint(f\"Jaccard EAP-IG vs EP:  {jaccard(eap_usr, ep_usr):.4f}\")\n\n# --- 3. What's in each top-100? ---\nprint(\"\\n=== IFR top-10 edges (by score) ===\")\nfor edge, score in sorted(ifr.items(), key=lambda x: x[1], reverse=True)[:10]:\n    print(f\"  {score:12.4f}  {edge}\")\n\nprint(\"\\n=== EAP-IG top-10 edges (by abs score) ===\")\nfor edge, score in sorted(eap.items(), key=lambda x: abs(x[1]), reverse=True)[:10]:\n    print(f\"  {score:12.8f}  {edge}\")\n\nprint(\"\\n=== EP top-10 edges (by abs score) ===\")\nfor edge, score in sorted(ep.items(), key=lambda x: abs(x[1]), reverse=True)[:10]:\n    print(f\"  {score:12.8f}  {edge}\")\n\n# --- 4. Check: where do IFR top-100 edges land? ---\nprint(\"\\n=== IFR top-100 structure ===\")\nifr_top_layers = defaultdict(int)\nfor e in ifr_top:\n    m = re.match(r\".*->(?:a|m)(\\d+)\", e)\n    if m:\n        ifr_top_layers[int(m.group(1))] += 1\nprint(\"Destination layer distribution:\")\nfor layer in sorted(ifr_top_layers):\n    print(f\"  layer {layer}: {ifr_top_layers[layer]} edges\")\n\nprint(\"\\n=== EAP-IG top-100 structure ===\")\neap_top_layers = defaultdict(int)\nfor e in eap_top:\n    m = re.match(r\".*->(?:a|m)(\\d+)\", e)\n    if m:\n        eap_top_layers[int(m.group(1))] += 1\nprint(\"Destination layer distribution:\")\nfor layer in sorted(eap_top_layers):\n    print(f\"  layer {layer}: {eap_top_layers[layer]} edges\")\n\n# --- 5. Collapse to (src_node, dst_node_type_layer) and compare ---\nprint(\"\\n=== Collapse to (src, dst_layer) level ===\")\ndef collapse(edges):\n    \"\"\"Collapse head-level edges to (src, dst_layer) level.\"\"\"\n    collapsed = set()\n    for e in edges:\n        m = attn_pattern.match(e)\n        if m:\n            collapsed.add(f\"{m.group(1)}->a{m.group(2)}\")\n        else:\n            collapsed.add(e)\n    return collapsed\n\nifr_c = collapse(ifr_top)\neap_c = collapse(eap_top)\nep_c  = collapse(ep_top)\nprint(f\"|IFR|={len(ifr_c)}, |EAP|={len(eap_c)}, |EP|={len(ep_c)}\")\nprint(f\"Jaccard IFR vs EAP-IG: {jaccard(ifr_c, eap_c):.4f}\")\nprint(f\"Jaccard IFR vs EP:     {jaccard(ifr_c, ep_c):.4f}\")\nprint(f\"Jaccard EAP-IG vs EP:  {jaccard(eap_c, ep_c):.4f}\")\n\nprint(\"\\nIFR collapsed:\", sorted(ifr_c))\nprint(\"\\nEAP collapsed:\", sorted(eap_c))\nPYEOF\necho \"Script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "cat > /root/structfuse-context/diagnose_ifr_perhead.py << 'PYEOF'\n\"\"\"Diagnose IFR per-head score degeneracy and test alternative binarizations.\"\"\"\nimport json\nimport re\nfrom collections import defaultdict\nfrom pathlib import Path\n\nCACHE = Path(\"/root/structfuse-context/cache/Qwen_Qwen2.5_0.5B/ioi\")\n\ndef load_scores(name):\n    with open(CACHE / f\"cache_{name}.json\") as f:\n        return json.load(f)\n\ndef jaccard(a: set, b: set) -> float:\n    if not a and not b:\n        return 0.0\n    return len(a & b) / len(a | b)\n\ndef topn(scores, n=100):\n    sorted_edges = sorted(scores.items(), key=lambda x: abs(x[1]), reverse=True)\n    return {e for e, _ in sorted_edges[:n]}\n\ndef topn_positive(scores, n=100):\n    sorted_edges = sorted(scores.items(), key=lambda x: x[1], reverse=True)\n    return {e for e, _ in sorted_edges[:n]}\n\ndef unique_score_rank(scores, n=100):\n    unique_vals = sorted(set(abs(v) for v in scores.values()), reverse=True)\n    top_vals = set(unique_vals[:n])\n    return {e for e, v in scores.items() if abs(v) in top_vals}\n\n# Load all scores\nifr = load_scores(\"ifr\")\neap = load_scores(\"eap_ig\")\nep  = load_scores(\"edge_pruning\")\n\nprint(f\"Total edges: IFR={len(ifr)}, EAP-IG={len(eap)}, EP={len(ep)}\")\n\n# --- 1. IFR score degeneracy analysis ---\nprint(\"\\n=== IFR Score Degeneracy ===\")\nunique_ifr = set(ifr.values())\nprint(f\"Total IFR edges: {len(ifr)}\")\nprint(f\"Unique IFR scores: {len(unique_ifr)}\")\nprint(f\"Degeneracy ratio: {len(ifr)/len(unique_ifr):.1f}x\")\n\n# Group attention edges by (src, dst_layer) to show block structure\nattn_pattern = re.compile(r\"(.+)->a(\\d+)\\.h(\\d+)\\.(q|k|v)\")\ngroups = defaultdict(set)\nfor edge, score in ifr.items():\n    m = attn_pattern.match(edge)\n    if m:\n        src, layer = m.group(1), m.group(2)\n        groups[(src, layer)].add(score)\n\nn_degenerate = sum(1 for v in groups.values() if len(v) == 1)\nprint(f\"\\nAttention edge groups (src, dst_layer): {len(groups)}\")\nprint(f\"Groups with ALL heads having same score: {n_degenerate} ({n_degenerate/len(groups)*100:.0f}%)\")\n\n# MLP edges: per-head variance\nmlp_pattern = re.compile(r\"a(\\d+)\\.h(\\d+)->m(\\d+)\")\nmlp_groups = defaultdict(list)\nfor edge, score in ifr.items():\n    m = mlp_pattern.match(edge)\n    if m:\n        src_layer, dst_layer = m.group(1), m.group(3)\n        mlp_groups[(src_layer, dst_layer)].append(score)\n\nprint(f\"\\nMLP edge groups (attn_head->mlp): {len(mlp_groups)}\")\nif mlp_groups:\n    variances = []\n    for k, scores_list in mlp_groups.items():\n        if len(scores_list) > 1:\n            mean = sum(scores_list) / len(scores_list)\n            var = sum((s - mean)**2 for s in scores_list) / len(scores_list)\n            variances.append(var)\n    print(f\"Groups with >1 head: {len(variances)}\")\n    if variances:\n        print(f\"Score variance: mean={sum(variances)/len(variances):.6f}, max={max(variances):.6f}\")\n\n# Also check EAP-IG degeneracy\nunique_eap = set(eap.values())\nprint(f\"\\n=== EAP-IG Score Degeneracy ===\")\nprint(f\"Total EAP-IG edges: {len(eap)}\")\nprint(f\"Unique EAP-IG scores: {len(unique_eap)}\")\nprint(f\"Degeneracy ratio: {len(eap)/len(unique_eap):.1f}x\")\n\neap_groups = defaultdict(set)\nfor edge, score in eap.items():\n    m = attn_pattern.match(edge)\n    if m:\n        src, layer = m.group(1), m.group(2)\n        eap_groups[(src, layer)].add(score)\nn_deg_eap = sum(1 for v in eap_groups.values() if len(v) == 1)\nprint(f\"Attn groups with ALL heads same score: {n_deg_eap} ({n_deg_eap/len(eap_groups)*100:.0f}%)\")\n\n# --- 2. Binarization comparison ---\nprint(\"\\n=== Binarization: top-100 (abs value) ===\")\nifr_top = topn(ifr, 100)\neap_top = topn(eap, 100)\nep_top  = topn(ep, 100)\nprint(f\"Jaccard IFR vs EAP-IG: {jaccard(ifr_top, eap_top):.4f}\")\nprint(f\"Jaccard IFR vs EP:     {jaccard(ifr_top, ep_top):.4f}\")\nprint(f\"Jaccard EAP-IG vs EP:  {jaccard(eap_top, ep_top):.4f}\")\n\nprint(\"\\n=== Binarization: top-100 (positive only, for EAP-IG/EP) ===\")\neap_top_pos = topn_positive(eap, 100)\nep_top_pos  = topn_positive(ep, 100)\nprint(f\"Jaccard IFR vs EAP-IG: {jaccard(ifr_top, eap_top_pos):.4f}\")\nprint(f\"Jaccard IFR vs EP:     {jaccard(ifr_top, ep_top_pos):.4f}\")\nprint(f\"Jaccard EAP-IG vs EP:  {jaccard(eap_top_pos, ep_top_pos):.4f}\")\n\nprint(\"\\n=== Binarization: unique_score_rank top-100 unique values ===\")\nifr_usr = unique_score_rank(ifr, 100)\neap_usr = unique_score_rank(eap, 100)\nep_usr  = unique_score_rank(ep, 100)\nprint(f\"|IFR|={len(ifr_usr)}, |EAP|={len(eap_usr)}, |EP|={len(ep_usr)}\")\nprint(f\"Jaccard IFR vs EAP-IG: {jaccard(ifr_usr, eap_usr):.4f}\")\nprint(f\"Jaccard IFR vs EP:     {jaccard(ifr_usr, ep_usr):.4f}\")\nprint(f\"Jaccard EAP-IG vs EP:  {jaccard(eap_usr, ep_usr):.4f}\")\n\n# --- 3. What's in each top-100? ---\nprint(\"\\n=== IFR top-10 edges (by score) ===\")\nfor edge, score in sorted(ifr.items(), key=lambda x: x[1], reverse=True)[:10]:\n    print(f\"  {score:12.4f}  {edge}\")\n\nprint(\"\\n=== EAP-IG top-10 edges (by abs score) ===\")\nfor edge, score in sorted(eap.items(), key=lambda x: abs(x[1]), reverse=True)[:10]:\n    print(f\"  {score:12.8f}  {edge}\")\n\nprint(\"\\n=== EP top-10 edges (by abs score) ===\")\nfor edge, score in sorted(ep.items(), key=lambda x: abs(x[1]), reverse=True)[:10]:\n    print(f\"  {score:12.8f}  {edge}\")\n\n# --- 4. Check: where do IFR top-100 edges land? ---\nprint(\"\\n=== IFR top-100 structure ===\")\nifr_top_layers = defaultdict(int)\nfor e in ifr_top:\n    m = re.match(r\".*->(?:a|m)(\\d+)\", e)\n    if m:\n        ifr_top_layers[int(m.group(1))] += 1\nprint(\"Destination layer distribution:\")\nfor layer in sorted(ifr_top_layers):\n    print(f\"  layer {layer}: {ifr_top_layers[layer]} edges\")\n\nprint(\"\\n=== EAP-IG top-100 structure ===\")\neap_top_layers = defaultdict(int)\nfor e in eap_top:\n    m = re.match(r\".*->(?:a|m)(\\d+)\", e)\n    if m:\n        eap_top_layers[int(m.group(1))] += 1\nprint(\"Destination layer distribution:\")\nfor layer in sorted(eap_top_layers):\n    print(f\"  layer {layer}: {eap_top_layers[layer]} edges\")\n\n# --- 5. Collapse to (src_node, dst_node_type_layer) and compare ---\nprint(\"\\n=== Collapse to (src, dst_layer) level ===\")\ndef collapse(edges):\n    \"\"\"Collapse head-level edges to (src, dst_layer) level.\"\"\"\n    collapsed = set()\n    for e in edges:\n        m = attn_pattern.match(e)\n        if m:\n            collapsed.add(f\"{m.group(1)}->a{m.group(2)}\")\n        else:\n            collapsed.add(e)\n    return collapsed\n\nifr_c = collapse(ifr_top)\neap_c = collapse(eap_top)\nep_c  = collapse(ep_top)\nprint(f\"|IFR|={len(ifr_c)}, |EAP|={len(eap_c)}, |EP|={len(ep_c)}\")\nprint(f\"Jaccard IFR vs EAP-IG: {jaccard(ifr_c, eap_c):.4f}\")\nprint(f\"Jaccard IFR vs EP:     {jaccard(ifr_c, ep_c):.4f}\")\nprint(f\"Jaccard EAP-IG vs EP:  {jaccard(eap_c, ep_c):.4f}\")\n\nprint(\"\\nIFR collapsed:\", sorted(ifr_c))\nprint(\"\\nEAP collapsed:\", sorted(eap_c))\nPYEOF\necho \"Script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T07:37:22.489004+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T07:37:22.489135+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-pro6000",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse-context && python diagnose_ifr_perhead.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse-context && python diagnose_ifr_perhead.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T07:37:22.489311+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total edges: IFR=141384, EAP-IG=179388, EP=179388\\n\\n=== IFR Score Degeneracy ===\\nTotal IFR edges: 141384\\nUnique IFR scores: 6863\\nDegeneracy ratio: 20.6x\\n\\nAttention edge groups (src, dst_layer): 3281\\nGroups with ALL heads having same score: 3281 (100%)\\n\\nMLP edge groups (attn_head->mlp): 300\\nGroups with >1 head: 283\\nScore variance: mean=0.374098, max=6.706000\\n\\n=== EAP-IG Score Degeneracy ===\\nTotal EAP-IG edges: 179388\\nUnique EAP-IG scores: 8664\\nDegeneracy ratio: 20.7x\\nAttn groups with ALL heads same score: 4164 (100%)\\n\\n=== Binarization: top-100 (abs value) ===\\nJaccard IFR vs EAP-IG: 0.0000\\nJaccard IFR vs EP:     0.0000\\nJaccard EAP-IG vs EP:  0.5385\\n\\n=== Binarization: top-100 (positive only, for EAP-IG/EP) ===\\nJaccard IFR vs EAP-IG: 0.0000\\nJaccard IFR vs EP:     0.0000\\nJaccard EAP-IG vs EP:  0.5385\\n\\n=== Binarization: unique_score_rank top-100 unique values ===\\n|IFR|=2191, |EAP|=2027, |EP|=49714\\nJaccard IFR vs EAP-IG: 0.0649\\nJaccard IFR vs EP:     0.0186\\nJaccard EAP-IG vs EP:  0.0145\\n\\n=== IFR top-10 edges (by score) ===\\n      206.3023  m2->a3.h0.q\\n      206.3023  m2->a3.h0.k\\n      206.3023  m2->a3.h0.v\\n      206.3023  m2->a3.h1.q\\n      206.3023  m2->a3.h1.k\\n      206.3023  m2->a3.h1.v\\n      206.3023  m2->a3.h2.q\\n      206.3023  m2->a3.h2.k\\n      206.3023  m2->a3.h2.v\\n      206.3023  m2->a3.h3.q\\n\\n=== EAP-IG top-10 edges (by abs score) ===\\n    0.00238087  a20.h9->m23\\n    0.00231672  a20.h9->m22\\n    0.00202737  a20.h9->a23.h0.q\\n    0.00202737  a20.h9->a23.h0.k\\n    0.00202737  a20.h9->a23.h0.v\\n    0.00202737  a20.h9->a23.h1.q\\n    0.00202737  a20.h9->a23.h1.k\\n    0.00202737  a20.h9->a23.h1.v\\n    0.00202737  a20.h9->a23.h2.q\\n    0.00202737  a20.h9->a23.h2.k\\n\\n=== EP top-10 edges (by abs score) ===\\n    0.98762071  a20.h9->m20\\n    0.98762071  a20.h9->a21.h0.q\\n    0.98762071  a20.h9->a21.h0.k\\n    0.9
…[truncated 963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T07:37:22.489539+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-pro6000",
  "command": "cat >> /root/structfuse-context/diagnose_ifr_perhead.py << 'PYEOF'\n\n# --- 6. Sweep topN to find if overlap appears at any N ---\nprint(\"\\n=== Jaccard sweep over topN ===\")\nprint(f\"{'N':>6} {'IFR-EAP':>10} {'IFR-EP':>10} {'EAP-EP':>10}\")\nfor n in [50, 100, 200, 500, 1000, 2000, 5000]:\n    i = topn(ifr, n)\n    e = topn(eap, n)\n    p = topn(ep, n)\n    print(f\"{n:>6} {jaccard(i, e):>10.4f} {jaccard(i, p):>10.4f} {jaccard(e, p):>10.4f}\")\n\n# --- 7. Source node overlap ---\nprint(\"\\n=== Source node overlap in top-100 ===\")\ndef src_nodes(edges):\n    return {e.split(\"->\")[0] for e in edges}\nifr_src = src_nodes(ifr_top)\neap_src = src_nodes(eap_top)\nep_src  = src_nodes(ep_top)\nprint(f\"IFR sources:    {sorted(ifr_src)}\")\nprint(f\"EAP-IG sources: {sorted(eap_src)}\")\nprint(f\"EP sources:     {sorted(ep_src)}\")\nprint(f\"Jaccard(IFR src, EAP src): {jaccard(ifr_src, eap_src):.4f}\")\nprint(f\"Jaccard(IFR src, EP src):  {jaccard(ifr_src, ep_src):.4f}\")\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse-context && python diagnose_ifr_perhead.py 2>&1 | tail -30",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "cat >> /root/structfuse-context/diagnose_ifr_perhead.py << 'PYEOF'\n\n# --- 6. Sweep topN to find if overlap appears at any N ---\nprint(\"\\n=== Jaccard sweep over topN ===\")\nprint(f\"{'N':>6} {'IFR-EAP':>10} {'IFR-EP':>10} {'EAP-EP':>10}\")\nfor n in [50, 100, 200, 500, 1000, 2000, 5000]:\n    i = topn(ifr, n)\n    e = topn(eap, n)\n    p = topn(ep, n)\n    print(f\"{n:>6} {jaccard(i, e):>10.4f} {jaccard(i, p):>10.4f} {jaccard(e, p):>10.4f}\")\n\n# --- 7. Source node overlap ---\nprint(\"\\n=== Source node overlap in top-100 ===\")\ndef src_nodes(edges):\n    return {e.split(\"->\")[0] for e in edges}\nifr_src = src_nodes(ifr_top)\neap_src = src_nodes(eap_top)\nep_src  = src_nodes(ep_top)\nprint(f\"IFR sources:    {sorted(ifr_src)}\")\nprint(f\"EAP-IG sources: {sorted(eap_src)}\")\nprint(f\"EP sources:     {sorted(ep_src)}\")\nprint(f\"Jaccard(IFR src, EAP src): {jaccard(ifr_src, eap_src):.4f}\")\nprint(f\"Jaccard(IFR src, EP src):  {jaccard(ifr_src, ep_src):.4f}\")\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse-context && python diagnose_ifr_perhead.py 2>&1 | tail -30",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T07:37:22.489713+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  layer 21: 14 edges\\n  layer 22: 43 edges\\n  layer 23: 43 edges\\n\\n=== Collapse to (src, dst_layer) level ===\\n|IFR|=5, |EAP|=5, |EP|=6\\nJaccard IFR vs EAP-IG: 0.0000\\nJaccard IFR vs EP:     0.0000\\nJaccard EAP-IG vs EP:  0.5714\\n\\nIFR collapsed: ['m2->a3', 'm2->m3', 'm20->a21', 'm22->a23', 'm22->m23']\\n\\nEAP collapsed: ['a20.h9->a21', 'a20.h9->a22', 'a20.h9->a23', 'a20.h9->m22', 'a20.h9->m23']\\n\\n=== Jaccard sweep over topN ===\\n     N    IFR-EAP     IFR-EP     EAP-EP\\n    50     0.0000     0.0000     0.0638\\n   100     0.0000     0.0000     0.5385\\n   200     0.0000     0.0000     0.4815\\n   500     0.0449     0.0000     0.1820\\n  1000     0.0220     0.0000     0.1507\\n  2000     0.0395     0.0000     0.1220\\n  5000     0.1818     0.0001     0.0897\\n\\n=== Source node overlap in top-100 ===\\nIFR sources:    ['m2', 'm20', 'm22']\\nEAP-IG sources: ['a20.h9']\\nEP sources:     ['a20.h9']\\nJaccard(IFR src, EAP src): 0.0000\\nJaccard(IFR src, EP src):  0.0000\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T07:37:22.489873+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T07:37:22.489994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T07:37:22.490110+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "IFR per-head degeneracy diagnosis",
  "type": "report",
  "description": "Diagnosis of IFR per-head score degeneracy and Jaccard overlap with gradient methods on Qwen-2.5-0.5B IOI",
  "project": "structfuse-context",
  "exp_id": "phase2_qwen05b_ioi_k3",
  "source_path": "/root/structfuse-context/diagnose_ifr_perhead.py",
  "tags": "['ifr', 'degeneracy', 'jaccard', 'diagnosis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "IFR per-head degeneracy diagnosis",
    "type": "report",
    "description": "Diagnosis of IFR per-head score degeneracy and Jaccard overlap with gradient methods on Qwen-2.5-0.5B IOI",
    "project": "structfuse-context",
    "exp_id": "phase2_qwen05b_ioi_k3",
    "source_path": "/root/structfuse-context/diagnose_ifr_perhead.py",
    "tags": "['ifr', 'degeneracy', 'jaccard', 'diagnosis']"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T07:37:22.490241+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/structfuse-context/diagnose_ifr_perhead.py\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T07:37:22.490369+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "IFR per-head degeneracy diagnosis",
  "type": "report",
  "description": "Diagnosis of IFR per-head score degeneracy and Jaccard overlap with gradient methods on Qwen-2.5-0.5B IOI",
  "project": "structfuse-context",
  "exp_id": "phase2_qwen05b_ioi_k3",
  "content_filename": "ifr_perhead_diagnosis.md",
  "tags": "['ifr', 'degeneracy', 'jaccard', 'diagnosis']",
  "content": "# IFR Per-Head Degeneracy Diagnosis\n\n## Question\nCan per-head IFR decomposition fix zero Jaccard overlap with gradient methods (EAP-IG, EP)?\n\n## Answer: No. Per-head decomposition is already enabled; the disagreement is structural.\n\n## Evidence\n\n### 1. Per-head decomposition is already running\n`_decompose_per_head()` is called in every `o_proj` hook. Source-side attention heads get distinct scores (visible in `a{L}.h{H}->m{L'}` edges with head-level variance mean=0.374).\n\n### 2. Destination-side degeneracy is 100%\nAll 3281 IFR attention edge groups `(src, dst_layer)` assign identical scores to all 14 destination heads × 3 qkv = 42 edges. EAP-IG has the exact same degeneracy (4164/4164 = 100%). This is architectural — all heads in a layer read the same residual stream.\n\n- IFR: 141,384 edges → 6,863 unique scores (20.6x degeneracy)\n- EAP-IG: 179,388 edges → 8,664 unique scores (20.7x degeneracy)\n\n### 3. Zero overlap is at (src, dst_layer) level, not head level\nCollapsed top-100 edges to (src, dst_layer) granularity:\n- **IFR**: `m2→a3, m2→m3, m20→a21, m22→a23, m22→m23` (MLP outputs dominate)\n- **EAP-IG**: `a20.h9→a21, a20.h9→a22, a20.h9→a23, a20.h9→m22, a20.h9→m23` (single attn head)\n- **Jaccard at collapsed level: 0.0000**\n\nSource nodes: IFR selects `{m2, m20, m22}`, gradient methods select `{a20.h9}`. Zero overlap.\n\n### 4. Jaccard sweep over topN\n| N | IFR-EAP | IFR-EP | EAP-EP |\n|---|---------|--------|--------|\n| 50 | 0.0000 | 0.0000 | 0.0638 |\n| 100 | 0.0000 | 0.0000 | 0.5385 |\n| 500 | 0.0449 | 0.0000 | 0.1820 |\n| 1000 | 0.0220 | 0.0000 | 0.1507 |\n| 5000 | 0.1818 | 0.0001 | 0.0897 |\n\nFirst non-zero IFR-EAP Jaccard at N=500 (0.045). IFR-EP stays ~0 until N=5000.\n\n### 5. unique_score_rank binarization\nExpanding to 100 unique score values: |IFR|=2191, |EAP|=2027 → Jaccard=0.065. Marginal.\n\n## Root Cause\nIFR proximity (L1 activation norm) measures \"how much of source's output is present in the residual stream\" — biased toward high-magnitude MLP outputs (m2, m22). Gradient methods measure \"which edges causally affect the metric\" — finds specific task-relevant heads (a20.h9). These are fundamentally different quantities. Per-head decomposition cannot bridge this gap because the disagreement is at the source-node level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "IFR per-head degeneracy diagnosis",
    "type": "report",
    "description": "Diagnosis of IFR per-head score degeneracy and Jaccard overlap with gradient methods on Qwen-2.5-0.5B IOI",
    "project": "structfuse-context",
    "exp_id": "phase2_qwen05b_ioi_k3",
    "content_filename": "ifr_perhead_diagnosis.md",
    "tags": "['ifr', 'degeneracy', 'jaccard', 'diagnosis']",
    "content": "# IFR Per-Head Degeneracy Diagnosis\n\n## Question\nCan per-head IFR decomposition fix zero Jaccard overlap with gradient methods (EAP-IG, EP)?\n\n## Answer: No. Per-head decomposition is already enabled; the disagreement is structural.\n\n## Evidence\n\n### 1. Per-head decomposition is already running\n`_decompose_per_head()` is called in every `o_proj` hook. Source-side attention heads get distinct scores (visible in `a{L}.h{H}->m{L'}` edges with head-level variance mean=0.374).\n\n### 2. Destination-side degeneracy is 100%\nAll 3281 IFR attention edge groups `(src, dst_layer)` assign identical scores to all 14 destination heads × 3 qkv = 42 edges. EAP-IG has the exact same degeneracy (4164/4164 = 100%). This is architectural — all heads in a layer read the same residual stream.\n\n- IFR: 141,384 edges → 6,863 unique scores (20.6x degeneracy)\n- EAP-IG: 179,388 edges → 8,664 unique scores (20.7x degeneracy)\n\n### 3. Zero overlap is at (src, dst_layer) level, not head level\nCollapsed top-100 edges to (src, dst_layer) granularity:\n- **IFR**: `m2→a3, m2→m3, m20→a21, m22→a23, m22→m23` (MLP outputs dominate)\n- **EAP-IG**: `a20.h9→a21, a20.h9→a22, a20.h9→a23, a20.h9→m22, a20.h9→m23` (single attn head)\n- **Jaccard at collapsed level: 0.0000**\n\nSource nodes: IFR selects `{m2, m20, m22}`, gradient methods select `{a20.h9}`. Zero overlap.\n\n### 4. Jaccard sweep over topN\n| N | IFR-EAP | IFR-EP | EAP-EP |\n|---|---------|--------|--------|\n| 50 | 0.0000 | 0.0000 | 0.0638 |\n| 100 | 0.0000 | 0.0000 | 0.5385 |\n| 500 | 0.0449 | 0.0000 | 0.1820 |\n| 1000 | 0.0220 | 0.0000 | 0.1507 |\n| 5000 | 0.1818 | 0.0001 | 0.0897 |\n\nFirst non-zero IFR-EAP Jaccard at N=500 (0.045). IFR-EP stays ~0 until N=5000.\n\n### 5. unique_score_rank binarization\nExpanding to 100 unique score values: |IFR|=2191, |EAP|=2027 → Jaccard=0.065. Marginal.\n\n## Root Cause\nIFR proximity (L1 activation norm) measures \"how much of source's output is present in the residual stream\" — biased toward high-magnitude MLP outputs (m2, m22). Gradient methods measure \"which edges causally affect the metric\" — finds specific task-relevant heads (a20.h9). These are fundamentally different quantities. Per-head decomposition cannot bridge this gap because the disagreement is at the source-node level."
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-13T07:37:22.490536+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_586184\", \"name\": \"IFR per-head degeneracy diagnosis\", \"type\": \"report\", \"description\": \"Diagnosis of IFR per-head score degeneracy and Jaccard overlap with gradient methods on Qwen-2.5-0.5B IOI\", \"path\": \"projects/structfuse-context/artifacts/phase2_qwen05b_ioi_k3/report/ifr_perhead_diagnosis.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": \"phase2_qwen05b_ioi_k3\", \"skill\": \"\", \"created_at\": \"2026-05-13T07:37:09.832747+00:00\", \"tags\": [\"ifr\", \"degeneracy\", \"jaccard\", \"diagnosis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-13T07:37:22.490717+00:00_

## 结论

**Per-head IFR 分解已经在运行，无法修复零重叠。** 根因不在 head 粒度。

### 核心发现

| 维度 | IFR | EAP-IG / EP |
|------|-----|-------------|
| Source 节点偏好 | MLP 输出 (`m2, m20, m22`) | 特定注意力头 (`a20.h9`) |
| 度量本质 | activation 幅度（"残差流中存在多少"） | 梯度因果性（"对 metric 影响多大"） |

**关键数据：**

1. **Destination-side 退化是 100%** — IFR 和 EAP-IG 都有同样问题（3281/3281 和 4164/4164 组全退化），这是架构性的（同层头共享 residual stream）

2. **即使 collapse 到 (src, dst_layer) 粒度，Jaccard 仍为 0.0000** — IFR 选的 source 节点和梯度方法完全不同

3. **Jaccard sweep**: 首次非零出现在 N=500（IFR-EAP=0.045），说明需要扩到前 500 条边才开始有微弱交集

4. **`unique_score_rank` 策略**: 把 100 unique scores 展开后 |IFR|=2191 条边，Jaccard 也仅 0.065

**结论**: IFR proximity 本质上度量的是 activation magnitude，天然偏向高幅度 MLP 输出；梯度方法度量的是 causal influence，找到任务相关的特定注意力头。这两者在 Qwen-0.5B IOI 上对信息流的理解根本不同。Per-head 分解不是修复方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_ifr-perhead-diagnostic_20260513T073307"
}
```

</details>

---
