# analysis adaptive seed234 seed789

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_adaptive_seed234_seed789_20260524T083348_result.json`
- **Structured JSON:** [`72a779698e7d5986ced6.json`](../../sessions/72/72a779698e7d5986ced6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 最终 Metrics

| 实验 | holdout_ppl | holdout_loss | train_loss | train_duration |
|------|------------|-------------|-----------|---------------|
| adaptive_seed234 | 17.6782 | 2.8723 | 9.695 | 13540s (3h46m) |
| adaptive_seed789 | 17.6684 | 2.8718 | 9.650 | 13570s (3h46m) |

### N=5 Paired t-test (adaptive vs uniform)

| Seed | Adaptive PPL | Uniform PPL | Δ |
|------|-------------|------------|-------|
| 42 | 17.6440 | 17.6939 | -0.0499 |
| 123 | 17.6308 | 17.6861 | -0.0553 |
| 456 | 17.6419 | 17.7015 | -0.0596 |
| 789 | 17.6684 | 17.6954 | -0.0270 |
| 234 | 17.6782 | 17.7082 | -0.0300 |

**Mean Δ = -0.0444 ± 0.0149 (SD)**

- paired t(4) = -6.65, **p = 0.00266**
- BH-adjusted p (rank 1/9) = **0.0239 < 0.05** → 显著

### Metric 一致性说明

所有 5 个 adaptive 实验均使用 post-hoc eval（`eval_results/ppl_holdout.json`）。uniform 实验使用 inline holdout eval。两者都是对同一 holdout set 计算 PPL，只是 eval 时机不同（final checkpoint 相同），结果可比。

---
