# analysis mse training config

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mse_training_config_20260520T061551_result.json`
- **Structured JSON:** [`e249ab5dab376f39ee7f.json`](../../sessions/e2/e249ab5dab376f39ee7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取完整信息。以下是提取的 MSE baseline 训练配置：

---

## MSE Baseline 训练配置

### 1. Mask 生成方式

**Gumbel-Sigmoid relaxation**，与 KL 训练完全相同。

`train_perlayer_mse.py` L105-107:
```python
logits = wrapper.predictors[layer_idx](inp)
mask = wrapper.gumbel_mask(logits)
```

`predictor.py` GumbelSigmoidMask:
```python
u = torch.rand_like(logits).clamp(1e-6, 1 - 1e-6)
gumbel_noise = -torch.log(-torch.log(u))
y_soft = torch.sigmoid((logits + gumbel_noise) / self.tau)
```

温度线性退火 (L103): `tau = tau_start + (tau_end - tau_start) * (step / num_steps)`，从 1.0 → 0.1。

### 2. 稀疏度控制

**Adaptive Lagrangian penalty controller**，与 KL 训练机制相同。

L97-99 初始化:
```python
lambda_sparse = 1.0
target_sparsity = args.sparsity_target
margin = 0.02
```

L150-155 约束 loss + 自适应更新:
```python
sparsity_error = torch.abs(actual_sparsity - target_sparsity)
constraint_loss = lambda_sparse * torch.clamp(sparsity_error - margin, min=0.0) ** 2

# Adaptive: push lambda up when too dense, down when too sparse
if last_sparsity < target_sparsity - margin:
    lambda_sparse *= 2.0
elif last_sparsity > target_sparsity + margin:
    lambda_sparse *= 0.5
lambda_sparse = max(0.01, min(lambda_sparse, args.lambda_max))  # cap=1000
```

与 KL 训练(`train.py`)的 Lagrangian 完全一致。

### 3. 超参数

实际启动命令（registry.yaml L709-714, L856-861）：

| 超参 | MSE 30% | MSE 50% | KL（对照） |
|------|---------|---------|-----------|
| LR | 1e-3 | 1e-3 | 1e-3 |
| Optimizer | AdamW (weight_decay=0.01) | 同左 | 同左 |
| Batch size | 4 | 4 | 4 |
| Steps | 1000 | 1000 | 1000 |
| Seq len | 2048 | 2048 | 2048 |
| Warmup | 100 | 100 | 100 |
| Scheduler | cosine w/ warmup | 同左 | 同左 |
| tau | 1.0 → 0.1 (linear) | 同左 | 同左 |
| Grad clip | 1.0 | 1.0 | 1.0 |
| Gradient checkpointing | **No** | **No** | **Yes** (auto for KL) |
| Gradient accumulation | 1 | 1 | 1 |
| Dataset | wikitext-103 | wikitext-103 | wikitext-103 |
| Seed | 42 | 42 | 42 |
| bottleneck_dim | 128 | 128 | 128 |
| lambda_max | 1000 | 1000 | 1000 |

### 4. 与 KL/BCE 的关键差异

**Loss 函数**:
- MSE: `||down_proj(act * mask) - down_proj(act)||² / num_layers`，per-layer 独立计算，梯度不穿过整个 model（L109-115）
- KL: `KL(P_dense || P_sparse)` 在 output logit 空间，梯度需 backprop 穿过所有后续层
- BCE: `BCE(predictor_logits, top-k_binary_target)`，无需 forward pass 生成 sparse output

**梯度流差异**:
- MSE: `mse → sparse_out → down_proj (frozen) → mask → predictor`。只穿过单层的 down_proj，**不需要 gradient checkpointing**。
- KL: `kl → all subsequent layers → mask → predictor`。需穿过整个模型，**需要 gradient checkpointing**。

**Predictor 架构**: 完全相同 — `SparsityPredictor(hidden_size, intermediate_size, bottleneck_size=128)`，GELU 激活。

**数据 pipeline**: 完全相同 — `get_calibration_loader(tokenizer, batch_size=4, seq_len=2048, seed=42, "wikitext-103")`。

**训练结果**:
- MSE 30%: final_mse=0.0057, sparsity=0.277, lambda 到顶 1000（未收敛到目标 0.3）
- MSE 50%: final_loss=0.0083, sparsity=0.539

---
