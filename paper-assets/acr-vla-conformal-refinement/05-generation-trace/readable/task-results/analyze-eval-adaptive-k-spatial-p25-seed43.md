# analyze eval adaptive k spatial p25 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-adaptive-k-spatial-p25-seed43_20260520T105000_result.json`
- **Structured JSON:** [`bdc0c8576a0189e1a766.json`](../../sessions/bd/bdc0c8576a0189e1a766.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 实验结果摘要：eval-adaptive-k-spatial-p25-seed43

| 指标 | 值 |
|------|-----|
| **Overall SR** | **30.0%** (30/100) |
| **Avg K** | 7.6 |
| **Fast path (K=1)** | 29.5% |
| **Mean L2** | 0.089 |
| **Rollouts** | 100 (10 tasks × 10), 无错误/crash |
| W&B | 日志中无 run ID |

### Per-task SR

| Task | SR |
|------|-----|
| next_to_ramekin | **100%** |
| next_to_cookie_box | 80% |
| between_plate_and_ramekin | 60% |
| on_cookie_box | 30% |
| next_to_plate | 20% |
| in_top_drawer | 10% |
| from_table_center | 0% |
| on_ramekin | 0% |
| on_stove | 0% |
| on_wooden_cabinet | 0% |

### 与 Object P25 对比

| | Spatial P25 (seed43) | Object P25 |
|---|---|---|
| SR | **30.0%** | 14.3% |
| Avg K | 7.6 | ~4.8 |
| Fast path | 29.5% | ~65% |

### 分析

Spatial 上 P25 阈值的表现比 Object 好很多（SR 30% vs 14.3%），但代价是计算量大幅增加——avg_k=7.6（接近满 K=10），fast_path 仅 29.5%。这说明模型在 Spatial 任务上不确定性更高，P25 阈值几乎无法过滤掉不必要的推理步骤，adaptive 机制退化为接近 K=10 的行为。任务成功率两极分化严重：3 个 task ≥60%，4 个 task 为 0%。

---
