# code find predictor wrapper

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_code_find_predictor_wrapper_20260521T020004.jsonl`
- **Structured JSON:** [`3870e5b6778d457eb199.json`](../../sessions/38/3870e5b6778d457eb199.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Assistant

_source line 1 · 2026-05-21T02:00:14.799615+00:00_

You've hit your limit · resets May 22, 6pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_find_predictor_wrapper_20260521T020004"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T02:00:22.695542+00:00_

You've hit your limit · resets May 22, 5am (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_find_predictor_wrapper_20260521T020004"
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T02:01:21.018766+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_find_predictor_wrapper_20260521T020004",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T02:01:21.019156+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_find_predictor_wrapper_20260521T020004",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T02:01:21.019414+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "ls /root/distill_sparse_swiglu/src/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_find_predictor_wrapper_20260521T020004",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "ls /root/distill_sparse_swiglu/src/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T02:01:21.019610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -rln \"class PredictorWrapper\" /root/distill_sparse_swiglu/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_find_predictor_wrapper_20260521T020004",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "grep -rln \"class PredictorWrapper\" /root/distill_sparse_swiglu/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T02:01:21.019783+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_mask_divergence.py\\nanalyze_natural_sparsity.py\\nanalyze_perlayer_sparsity.py\\nbaselines.py\\nbatch_eval.py\\nbenchmark_eval.py\\nbenchmark_flashinfer.py\\nbenchmark_latency.py\\ncompensation.py\\ndata_utils.py\\ndebug_mask_v2.py\\ndebug_mask_verify.py\\ndiag_hflm.py\\ndiag_hflm_direct.py\\ndiag_mask.py\\ndiag_mmlu.py\\neval_bce_comp.py\\neval_benchmark.py\\neval_c4_ood.py\\neval_c4_predictor.py\\neval_spon.py\\neval_spon_supplementary.py\\nevaluate.py\\nevaluate.py.bak\\nevaluate.py.v2_bak\\ngsm8k_gen_compare.py\\nlatency_benchmark.py\\nlm_eval_sparse.py\\nlm_eval_sparse_uniform.py\\nlm_eval_teal.py\\nlosses.py\\nlosses.py.bak\\npatch_vanilla_teal.py\\npredictor.py\\npredictor.py.bak\\nquick_eval.py\\nquick_eval2.py\\nquick_sp70.py\\nrun_baselines_sweep.py\\nrun_db_sweep.sh\\nspon.py\\nsubsumption_test.py\\ntest_greedy_dryrun.py\\ntrain.py\\ntrain.py.bak\\ntrain.py.v1_bak\\ntrain.py.v2_bak\\ntrain_bce_comp.py\\ntrain_bce_gumbel.py\\ntrain_bce_gumbel_no_penalty.py\\ntrain_bce_kl_targets.py\\ntrain_compensation.py\\ntrain_perlayer_kl.py\\ntrain_perlayer_mse.py\\ntrain_spon.py\\nvisualize_mask_patterns.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_find_predictor_wrapper_20260521T020004",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T02:01:21.019927+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/src/predictor.py\\n/root/distill_sparse_swiglu/src/predictor.py.bak\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_find_predictor_wrapper_20260521T020004",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T02:01:21.020091+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "wc -l /root/distill_sparse_swiglu/src/predictor.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_find_predictor_wrapper_20260521T020004",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "wc -l /root/distill_sparse_swiglu/src/predictor.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:01:21.020613+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"199 /root/distill_sparse_swiglu/src/predictor.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_find_predictor_wrapper_20260521T020004",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T02:01:21.020806+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/src/predictor.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_find_predictor_wrapper_20260521T020004",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/distill_sparse_swiglu/src/predictor.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:01:21.021115+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Sparsity predictor architecture: bottleneck MLP + Gumbel-sigmoid/STE mask + model wrapper.\\n# Compensation network: per-layer MLP correcting sparse MLP output errors (FastForward-style).\\n# Input: hidden_states (batch, seq, hidden_size) -> Output: mask logits (batch, seq, intermediate_size)\\n\\nimport torch\\nimport torch.nn as nn\\n\\n\\nclass SparsityPredictor(nn.Module):\\n    \\\"\\\"\\\"Rank-bottleneck MLP predicting SwiGLU sparsity masks.\\\"\\\"\\\"\\n\\n    def __init__(self, hidden_size: int, intermediate_size: int, bottleneck_size: int = 128):\\n        super().__init__()\\n        self.down = nn.Linear(hidden_size, bottleneck_size)\\n        self.act = nn.GELU()\\n        self.up = nn.Linear(bottleneck_size, intermediate_size)\\n\\n    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:\\n        return self.up(self.act(self.down(hidden_states)))\\n\\n\\nclass CompensationHead(nn.Module):\\n    \\\"\\\"\\\"Per-layer MLP predicting the output error introduced by sparsification.\\n\\n    Takes MLP input hidden state, outputs correction added to sparse MLP output.\\n    \\\"\\\"\\\"\\n\\n    def __init__(self, hidden_size: int, bottleneck_size: int = 256):\\n        super().__init__()\\n        self.net = nn.Sequential(\\n            nn.Linear(hidden_size, bottleneck_size),\\n            nn.GELU(),\\n            nn.Linear(bottleneck_size, hidden_size),\\n        )\\n\\n    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:\\n        return self.net(hidden_states)\\n\\n\\nclass CompensationNetwork(nn.Module):\\n    \\\"\\\"\\\"Per-layer compensation heads correcting sparse MLP output errors.\\\"\\\"\\\"\\n\\n    def __init__(self, num_layers: int, hidden_size: int, bottleneck_size: int = 256):\\n        super().__init__()\\n        self.heads = nn.ModuleList([\\n            CompensationHead(hidden_size, bottleneck_size)\\n            for _ in range(num_layers)\\n        ])\\
…[truncated 5774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_find_predictor_wrapper_20260521T020004",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T02:01:21.021379+00:00_

文件路径：`/root/distill_sparse_swiglu/src/predictor.py`（199 行）

## 完整源代码（关键部分）

### `PredictorWrapper` 类（line 94-199）

**初始化**：
- 接受 `model` + `bottleneck_size=128`（默认）
- 冻结 base model 所有参数
- 创建 `num_layers` 个 `SparsityPredictor`（每层独立）
- 共享一个 `GumbelSigmoidMask`（无可学习参数）
- 默认 `sparse_mode=True`
- `comp_network=None`, `use_compensation=False`

**Monkey-patch 机制（`_patch_single_mlp`）**：每层 MLP 的 `forward` 被替换为 `patched_forward`。

### `forward_sparse` 实现细节

```python
def patched_forward(x):
    gate = act_fn(gate_proj(x))      # SwiGLU gate
    up = up_proj(x)
    intermediate = gate * up         # SwiGLU intermediate

    if wrapper.sparse_mode:
        logits = predictor(x)                              # per-layer predictor: hidden -> intermediate
        mask = wrapper.gumbel_mask(logits)                 # Gumbel-sigmoid (train) / hard threshold (eval)
        wrapper._layer_masks[layer_idx] = mask             # 缓存 mask
        result = down_proj(intermediate * mask)            # 应用 mask 后 down_proj
        if wrapper.use_compensation and wrapper.comp_network is not None:
            result = result + wrapper.comp_network.forward_layer(layer_idx, x)  # 补偿
        return result
    elif wrapper.capture_intermediates:
        wrapper._layer_intermediates[layer_idx] = intermediate.detach()
        wrapper._layer_inputs[layer_idx] = x.detach()

    return down_proj(intermediate)   # dense path
```

`forward_sparse(input_ids, ...)`（line 184-187）：设置 `sparse_mode=True` → 调 `self.forward` → 走 patched MLP 路径，每层都用 `predictor[layer_idx]` 产生 logits → `gumbel_mask` 二值化 → mask 乘到 intermediate。

### `forward_dense`（line 172-182）

设置 `sparse_mode=False`，在 `torch.no_grad()` 下跑 base model；`capture_intermediates=True` 时缓存每层 `intermediate`（gate*up）和 `x`（MLP 输入）；返回后复位 `sparse_mode=True`。

### `get_masks`（line 189-190）

`return dict(self._layer_masks)` — 返回上一次 forward 各层缓存的 mask 字典 `{layer_idx: mask_tensor}`。Mask 是在 `patched_forward` 里写入的，没有"批量收集"步骤。

### `GumbelSigmoidMask` 的 per-layer 工作方式（line 54-72）

**不是 per-layer**：`PredictorWrapper` 只持有**一个共享** `self.gumbel_mask`（无参数）。Per-layer 差异来自 **`predictors[layer_idx]`** 产生的不同 logits，`gumbel_mask` 只是把 logits 二值化：
- **训练 (`self.training and not self.hard`)**: 加 Gumbel 噪声，sigmoid + 温度 `tau=1.0`（默认），返回 soft mask（梯度可传）
- **推理或 `hard=True`**: `(logits > 0).to(dtype)` 硬阈值

### 关键超参（与 C003 对照）
- `SparsityPredictor`: GELU 激活 ✓, `bottleneck_size=128` ✓, structure = `Linear(hidden, 128) → GELU → Linear(128, intermediate)`
- `CompensationHead`: GELU, `bottleneck_size=256`（默认，与 predictor 不同）
- `GumbelSigmoidMask`: `tau=1.0`, `hard=False` (默认)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_find_predictor_wrapper_20260521T020004"
}
```

</details>

---
