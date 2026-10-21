# debug v7 1 spectral norm

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_v7_1-spectral-norm_20260515T191109_result.json`
- **Structured JSON:** [`17de625d3d75ec660db9.json`](../../sessions/17/17de625d3d75ec660db9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

step 2000 数据还没出。确认了训练循环结构——现在出报告。

---

## 排查报告：v7.1 Spectral Norm 异常

### 1. LIP_MONITOR 数据

| Step | empirical_L | spectral_norm | 状态 |
|------|------------|---------------|------|
| 500  | 0.0432     | 1.0143        | OK |
| 1000 | 0.1212     | 2.4852        | **WARNING: SN > 2** |
| 1500 | 0.2940     | 4.6170        | **WARNING: SN > 3** |
| 2000 | 尚无数据（训练可能还没到） | — | — |

step 2000 尚未产出。L_emp 也在快速增长（0.29 逼近 0.3 阈值）。

### 2. 根因：`compute_empirical_lipschitz` 泄漏 eval mode

**`imm/metrics.py:87`**：
```python
acis_module.eval()   # ← 设了 eval，从未恢复 train
```

调用链：
1. `train.py:463` — 训练循环前 `model.train()`，此后循环体内**再无** `model.train()` 调用
2. `train.py:646` — step 500 触发 LIP_MONITOR
3. `train.py:660` → `compute_empirical_lipschitz(model.acis, ...)` → **`model.acis.eval()`**
4. 函数返回后，`model.acis` 永久停在 eval mode
5. `evaluate()` 的 `model.train()`（line 539）不会触发，因为 `eval_every=999999`

**PyTorch 旧式 `spectral_norm` 在 eval mode 下跳过 power iteration**（`if module.training:` 才更新 u/v 向量）。结果：
- step 500 后，u/v 向量冻结
- 每次 forward 仍做 `weight = weight_orig / sigma`，但 sigma 用的是**过时的** u/v → 越来越不准
- `weight_orig` 被 optimizer 持续更新，实际 spectral norm 不受控增长

对比 v7：**无 LIP_MONITOR 代码** → ACIS 始终 train mode → power iteration 正常更新 → SN 恒定 1.067。

### 3. 影响

不仅是测量偏差——**实际训练中 spectral normalization 也坏了**：
- ACIS Lipschitz 常数不再受约束
- certified bound `k·ε·L/Δ` 失效
- margin loss 在不正确的 importance scores 上学习

### 4. 修复

**`imm/metrics.py`**，`compute_empirical_lipschitz` 需保存和恢复 training mode：

```python
@torch.no_grad()
def compute_empirical_lipschitz(
    acis_module: nn.Module,
    visual_tokens: Tensor,
    a_query: Tensor,
    num_samples: int = 100,
    epsilon: float = 0.001,
) -> float:
    was_training = acis_module.training
    acis_module.eval()
    s_clean = acis_module(a_query, visual_tokens)

    max_ratio = 0.0
    for _ in range(num_samples):
        delta = torch.randn_like(visual_tokens)
        delta = delta / delta.norm(dim=-1, keepdim=True).clamp(min=1e-8) * epsilon
        s_pert = acis_module(a_query, visual_tokens + delta)

        score_diff = (s_pert - s_clean).norm(dim=-1)
        input_diff = delta.flatten(1).norm(dim=-1)
        ratio = (score_diff / input_diff.clamp(min=1e-8)).max().item()
        max_ratio = max(max_ratio, ratio)

    if was_training:
        acis_module.train()
    return max_ratio
```

只需改 metrics.py 第 87 行区域，加 `was_training` 保存 + 末尾恢复。v7.1 训练需要用修复后的代码重跑。

---
