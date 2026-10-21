# analyze rho02 adaptive tau09 r5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_rho02_adaptive_tau09_r5_20260517T175617_result.json`
- **Structured JSON:** [`e24f9eb15464a3f02ea1.json`](../../sessions/e2/e24f9eb15464a3f02ea1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

## rho02_adaptive_tau09_r5 结果

| 指标 | 值 |
|---|---|
| **eval PPL** | **17.45** |
| eval loss | 2.8593 |
| train_loss | 11.864 |
| epoch | 0.47 |
| checkpoint | `/root/autodl-tmp/output/models/rho02_adaptive_tau09_seed42/final` |

### b* 统计
| 指标 | 值 |
|---|---|
| mean | 4.35 |
| median | 2.96 |
| std | 4.40 |
| min/max | 0 / 20 |
| pct_zero | 2.65% |
| alpha_eff mean | 0.83 |
| alpha_eff pct_at_max(0.9) | 42.95% |
| ESS mean | 2.38 |

### 结论：**negative**

- PPL 17.45 > rho02_uniform baseline 17.336，adaptive 在 ρ=0.2 低 contamination 下未能超越 uniform
- 虽然 b* 非 trivial（mean=4.35, 仅 2.65% 为零），说明 adaptive 确实找到了有意义的 reweighting boundary，但这些 reweighting 反而损害了模型质量
- 在低 contamination 场景下，数据本身已足够干净，aggressive reweighting（τ=0.9 导致 42.95% batch 命中上限）可能过度惩罚了有用样本
- train_loss 异常高（11.864），可能是 weighted loss 放大效应导致的报告值偏差

---
