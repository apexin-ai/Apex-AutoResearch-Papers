# analysis grid b1 0 b1 5 seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b1_0_b1_5_seed456_20260515T005252_result.json`
- **Structured JSON:** [`b3568519b574144c022b.json`](../../sessions/b3/b3568519b574144c022b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验的 registry 已更新完成（都已是 DONE + success 状态）。汇总结果：

## 结果汇总

| 指标 | grid_b1_0_seed456 | grid_b1_5_seed456 |
|------|-------------------|-------------------|
| train_loss | 10.178 | 10.435 |
| train_runtime_s | 12963.87 | 12950.16 |
| total_steps | 6103 | 6103 |
| **eval_loss** | **2.8725** | **2.8741** |
| **eval_ppl_holdout** | **17.68** | **17.71** |
| eval_holdout_tokens | 4,077,068 | 4,077,068 |
| checkpoint_path | output/models/grid_b1_0_seed456/final | output/models/grid_b1_5_seed456/final |
| gpu_hours | 3.67 | 3.67 |

## 与 seed123 对比

| 实验 | seed123 ppl | seed456 ppl | 差异 |
|------|-------------|-------------|------|
| b=1.0 | 17.674 | 17.68 | +0.006 |
| b=1.5 | 17.701 | 17.71 | +0.009 |
| uniform | — | 17.70 | — |

seed456 的结果与 seed123 高度一致，跨 seed 可复现性好。b=1.0 仍然优于 b=1.5 和 uniform baseline。

---
