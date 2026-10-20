# code verify adaptive code

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-adaptive-code_20260513T234937_result.json`
- **Structured JSON:** [`0ac4d37621bade32f38b.json`](../../sessions/0a/0ac4d37621bade32f38b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过，汇报如下：

### 1. alpha_eff.py 函数完整性 ✓

6 个函数全部存在且实现正确：
- `compute_alpha_eff(q_scores, b)` — log-space 数值稳定实现
- `compute_ess(q_scores, b)` — Kish's ESS
- `find_optimal_b(q_scores, tau, n_min)` — grid search + bisection 两阶段优化
- `compute_sample_weights(q_scores, b)` — 归一化权重 (sum=N)
- `compute_concentration_bound(q_scores, b, delta)` — 置信区间上界（额外实现）
- `__main__` 自测代码

### 2. Smoke Test 结果 ✓

```
q = [0.1, 0.3, 0.5, 0.7, 0.9]
b*=3.311, alpha_eff=0.800, ess=2.1
weights=[3.116, 1.356, 0.445, 0.082, 0.002]
```
- b* 使 α_eff 恰好达到 τ=0.8 阈值
- ESS=2.1 ≥ n_min=2，约束满足
- 权重单调递减（q 越高权重越低），符合预期

### 3. pretrain_weighted.py 集成 ✓

- `WeightedTrainer.compute_loss()` (L143-149) 正确实现 adaptive 分支：调用 `find_optimal_b` → `compute_sample_weights` → 加权 loss
- 三种模式 (uniform/grid/adaptive) 完整，每步记录 b, α_eff, ESS 指标

### 4. contamination_ratio 参数传递 ✓

- `--contamination_ratio` 默认 0.2 (L213)
- `--tau` 默认 `None`，未指定时自动计算 `tau = 1.0 - contamination_ratio * 0.5` (L272-273)
- D004 设 contamination_ratio=0.4 → tau=0.8，逻辑正确

**无缺失或需要修复的问题。**

---
