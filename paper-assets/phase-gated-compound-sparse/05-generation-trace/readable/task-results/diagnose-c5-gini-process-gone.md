# diagnose c5 gini process gone

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_c5_gini_process_gone_20260516T035154_result.json`
- **Structured JSON:** [`681b88225acd65b725fc.json`](../../sessions/68/681b88225acd65b725fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## c5_per_phase_gini DS 状态报告

**进程状态**：已正常退出。GPU 0 空闲（0MiB）。结果文件 `results_c5_gini_ds.json` 写入于 11:49，366KB。

**完成度**：30/30 problems，全部完成。

### DS Per-Phase Gini Delta 数据

| Sparsity | Method | Global Δ | Low Δ | Mid Δ | High Δ |
|----------|--------|----------|-------|-------|--------|
| 15% | importance | -0.0301 | -0.0163 | -0.0073 | -0.0152 |
| 15% | random | -0.0309 | -0.0102 | -0.0006 | -0.0062 |
| 20% | importance | -0.0404 | -0.0209 | -0.0092 | -0.0200 |
| 20% | random | -0.0403 | -0.0120 | -0.0007 | -0.0085 |
| 25% | importance | -0.0647 | -0.0313 | -0.0133 | -0.0267 |
| 25% | random | -0.0620 | -0.0150 | -0.0096 | -0.0112 |
| 30% | importance | -0.0806 | -0.0373 | -0.0183 | -0.0314 |
| 30% | random | -0.0732 | -0.0183 | -0.0093 | -0.0138 |

**关键观察**：
- Importance pruning 在所有 sparsity level 的 low/high phase delta 均大于 random，说明 importance-based 剪枝在 low-sparsity 和 high-sparsity phase 产生更大的 Gini 变化
- Mid-sparsity phase delta 在两种方法间差距最小（random 在 15%/20% 几乎为 0）
- 随 sparsity 增加，所有 delta 单调增大（绝对值）

---
