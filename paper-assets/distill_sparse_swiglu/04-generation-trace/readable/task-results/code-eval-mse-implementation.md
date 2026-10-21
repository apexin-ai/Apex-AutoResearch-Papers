# code eval mse implementation

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_mse_implementation_20260520T020807_result.json`
- **Structured JSON:** [`37a80b45709c9cea1880.json`](../../sessions/37/37a80b45709c9cea1880.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have enough information. Here's the complete assessment.

---

## Per-Layer MSE Loss 实现评估

### 现有架构概要

核心模块在远程服务器 `/root/distill_sparse_swiglu/src/`:
- **predictor.py**: `SparsityPredictor`（per-layer, GELU, d_b=128）、`PredictorWrapper`（hook 式 wrapper）、`CompensationNetwork`
- **losses.py**: `BCESparsityLoss`, `CompensationLoss`, `SparsityRegularizer`
- **data_utils.py**: 数据加载

训练脚本每个变体独立一个文件（`train_bce_comp.py`, `train_bce_kl_targets.py` 等）。

---

### Q1: 现有 forward pass 能否访问每层 hidden states？

**Dense**: 部分可以。`wrapper.forward_dense(input_ids, capture_intermediates=True)` 通过 hook 捕获：
- `get_layer_inputs()` → `{layer_idx: [B, S, hidden_size]}` — 每层 MLP 输入
- `get_intermediates()` → `{layer_idx: [B, S, intermediate_size]}` — SwiGLU 激活 (`act(gate) * up`)

**不直接提供的**: FFN 输出（post `down_proj`）和完整 layer output。但现有 compensation loss 已演示如何手动计算：`down_proj(dense_act)` 和 `down_proj(dense_act * mask)` — 见 `train_bce_comp.py:168-171`。

**Sparse**: 没有完整的 sparse forward pass。现有代码逐层独立计算 sparse FFN output。

### Q2: 是否需要新 hooks？

**不需要**（如果做 per-layer 独立 MSE）。现有 hook 已捕获所需的 `dense_act` 和 `layer_input`，可直接计算：
```python
dense_out = down_proj(dense_act)                    # [B, S, hidden_size]
sparse_out = down_proj(dense_act * diff_mask)       # differentiable mask
mse = F.mse_loss(sparse_out, dense_out.detach())
```

如果要做 **propagated MSE**（跨层累积稀疏效应），则需要完整 sparse forward pass + 每层 output hook，复杂度显著增加。

### Q3: 现有 loss 计算位置

`train_bce_comp.py:147-186` — per-layer loop inside gradient accumulation loop。新 loss 遵循同样模式插入。

### Q4: Compensation loss 作为参考

直接参考 `train_bce_comp.py:167-173`:
```python
down_proj = wrapper.model.model.layers[layer_idx].mlp.down_proj
with torch.no_grad():                          # ← 关键差异点
    dense_out = down_proj(dense_act)
    sparse_out = down_proj(dense_act * mask)
comp = comp_net.forward_layer(layer_idx, inp)
total_comp += comp_loss_fn(comp, sparse_out, dense_out)
```

Compensation loss 的 mask 是 **detached** 的（`with torch.no_grad()`），只训练 compensation network。Per-layer MSE 需要 **differentiable mask** 来训练 predictor — 这是核心区别。

### Q5: 文件改动清单

| 文件 | 改动 |
|------|------|
| `src/losses.py` | 新增 `PerLayerMSELoss` 类（简单封装，~15 行） |
| `src/train_perlayer_mse.py` **(新建)** | 独立训练脚本，仿照 `train_bce_comp.py` 结构 |
| `src/predictor.py` | **无需改动** — `gumbel_mask` 已支持可微分 mask |

### Q6: 实现方案（伪代码）

```python
# 在 per-layer loop 内（类似 train_bce_comp.py 的结构）:

for layer_idx in range(num_layers):
    dense_act = intermediates[layer_idx]        # [B, S, inter_size]
    inp = layer_inputs[layer_idx]               # [B, S, hidden_size]
    
    pred_logits = wrapper.predictors[layer_idx](inp)
    
    # 可微分 mask（STE 或 Gumbel-Sigmoid）
    soft_mask = torch.sigmoid(pred_logits / tau)
    hard_mask = (pred_logits > 0).float()
    diff_mask = hard_mask - soft_mask.detach() + soft_mask  # STE
    
    down_proj = wrapper.model.model.layers[layer_idx].mlp.down_proj
    dense_out = down_proj(dense_act).detach()    # target, no grad
    sparse_out = down_proj(dense_act.detach() * diff_mask)  # grad flows through mask only
    
    total_mse += F.mse_loss(sparse_out, dense_out)

# 总 loss: bce_weight * bce + mse_weight * mse + reg
```

### Q7: 新训练参数

- `--mse_weight` (float, default=1.0): per-layer MSE 权重
- `--bce_weight` (float, default=1.0): 可选，BCE 权重（如果混合训练）
- `--mse_only` (flag): 是否仅用 MSE 不加 BCE
- `tau_start/tau_end`: 已存在于 codebase，Gumbel 温度退火

---

### 预估复杂度: **中等偏简单**

核心改动是 ~100 行新训练脚本（在现有 `train_bce_comp.py` 基础上改），losses.py 加 ~15 行。

### 潜在风险

1. **显存压力**: `down_proj(dense_act * diff_mask)` 需要保留 diff_mask 的计算图。每层 `dense_act` shape = `[4, 2048, 14336]`，bf16 下 ~235MB/层 × 32 层 = ~7.5GB。A6000 48GB 应该够，但 margin 不大。**缓解**: 可逐层计算并立即 backward（gradient checkpointing 式），或 detach `dense_act` 只让梯度流过 mask。
2. **梯度尺度**: MSE 和 BCE 的梯度量级可能差几个数量级，需要调 `mse_weight`。建议先跑一个 step 看 loss scale。
3. **STE bias**: STE 在 mask 接近 0.5 时 gradient 最准确，但实际训练中 mask 很快极化到 0/1。Gumbel-Sigmoid 可能更稳定（codebase 已有 `gumbel_mask` 基础设施）。
4. **dense_act detach 问题**: `dense_act` 来自 frozen model 的 forward hook，应该已经是 detached 的。需要确认 `capture_intermediates` 的实现是否自动 detach。

---
