# analyze adaptive fix seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_adaptive_fix_seed123_20260514T204328_result.json`
- **Structured JSON:** [`481f1d0df2de58d888e3.json`](../../sessions/48/481f1d0df2de58d888e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，conclusion=success，status=DONE。

## adaptive_fix_seed123 结果汇总

| 指标 | 值 |
|------|-----|
| **eval_ppl_holdout** | **17.643** |
| eval_loss | 2.8704 |
| eval_tokens | 4,077,068 |
| train_loss (weighted) | 7.517 |
| train_runtime | 10,347s (~2.9h) |
| total_steps | 6,103 |

### 基准对比

| 实验 | eval_ppl | vs adaptive_fix |
|------|----------|-----------------|
| uniform_seed123 | 17.69 | +0.047 (worse) |
| adaptive_seed123 (n_min=3) | 17.63 | -0.013 (better) |
| grid_b0_5_seed123 | 17.638 | -0.005 (better) |
| **adaptive_fix_seed123 (n_min=2)** | **17.643** | — |

### b* 轨迹

b* 范围 [0, 20]，均值 0.72，中位数 0.0。59.9% 的 batch b*<0.5（接近 uniform），18% 在 [0.5,1.0)，仅 2% 超过 5。

**结论：success** — n_min=2 修复版优于 uniform 基线 (17.643 < 17.69)，但略逊于原版 adaptive (17.63) 和 grid_b0.5 (17.638)，差距在噪声范围内。

---
