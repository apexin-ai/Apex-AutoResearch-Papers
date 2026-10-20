# analyze cwm seed0

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cwm-seed0_20260512T135307_result.json`
- **Structured JSON:** [`96f1173b3e25a1e557a1.json`](../../sessions/96/96f1173b3e25a1e557a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总如下：

## cwm-seed0 结果

| 指标 | 值 |
|------|-----|
| overall_accuracy | **87.57** |
| fail_f1 | 87.93 |
| fail_precision / recall | 82.71 / 93.86 |
| pass_f1 | 87.18 |
| pass_precision / recall | 93.45 / 81.70 |
| exact_match_rate | 84.29 |
| eval_loss | 0.0665 |
| train_loss | 0.2554 |
| 训练时间 | ~60 min (1.05 GPU-hr) |

## 4B CWM Seeds 对比

| Seed | overall_acc | fail_f1 | pass_f1 |
|------|-------------|---------|---------|
| **seed0** | **87.57** | **87.93** | **87.18** |
| seed123 | 87.32 | 87.92 | 86.69 |
| seed42 (baseline) | 86.93 | 87.51 | 86.33 |
| seed456 | 86.59 | 87.23 | 85.92 |
| seed789 | 运行中 | — | — |

seed0 是目前 4 个已完成 seed 中**最优的**——overall_acc 87.57 领先 seed123 0.25pp，pass_f1 87.18 领先 seed123 0.49pp，fail_f1 与 seed123 基本持平（87.93 vs 87.92）。

4 个 seed 的方差很小：overall_acc 范围 86.59–87.57（极差 0.98pp），说明 CWM 方法对 seed 不敏感，结果稳定。等 seed789 完成后可做完整 5-seed paired 统计分析。

---
