# code find predictor wrapper

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_find_predictor_wrapper_20260521T020004_result.json`
- **Structured JSON:** [`6f781202c8b206ae5566.json`](../../sessions/6f/6f781202c8b206ae5566.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

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

---
