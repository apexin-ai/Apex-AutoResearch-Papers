# analyze grid b1 0 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_grid_b1_0_seed123_20260514T104716_result.json`
- **Structured JSON:** [`f39652b98a750894d381.json`](../../sessions/f3/f39652b98a750894d381.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。总结：

## grid_b1_0_seed123 结果

| 指标 | 值 |
|------|-----|
| eval_ppl_holdout | **17.674** |
| eval_loss | 2.8721 |
| train_loss | 10.218 |
| total_steps | 6103 |
| train_runtime | 13,878s (3.86h) |
| wall_clock | 13,950s (3.88 GPU-hours) |
| checkpoint | `/root/provenance_weight_training/output/models/grid_b1_0_seed123/final/` |

## 与 baseline 对比 (seed=123)

| 方法 | b | eval_ppl_holdout | Δ vs uniform |
|------|---|-----------------|--------------|
| uniform | — | 17.690 | — |
| **grid b=1.0** | **1.0** | **17.674** | **-0.016** |
| grid b=0.5 | 0.5 | 17.638 | -0.052 |
| adaptive | auto | 17.630 | -0.060 |

**结论**：grid b=1.0 比 uniform 有微弱改善（-0.016 PPL），但不如 b=0.5（-0.052）和 adaptive（-0.060）。在 seed=123 上的 grid-b 排序为 b=0.5 > b=1.0 > uniform，与 seed=42 的趋势一致（seed42: b=0.5 PPL=17.651, b=1.0 PPL=17.692）。b=1.0 的 weighting 效果偏弱，确认 b 值越小（更平缓的权重分布）在当前设置下更优。

---
