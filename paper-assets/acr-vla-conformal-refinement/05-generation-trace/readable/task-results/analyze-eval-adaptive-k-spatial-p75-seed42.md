# analyze eval adaptive k spatial p75 seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-adaptive-k-spatial-p75-seed42_20260520T103231_result.json`
- **Structured JSON:** [`e2b177ed7118c2706785.json`](../../sessions/e2/e2b177ed7118c2706785.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。最终报告：

## eval-adaptive-k-spatial-p75-seed42 结果

| 指标 | 值 |
|------|-----|
| **SR** | **31.0%** (31/100) |
| **avg_K** | 5.02 |
| **fast_path_ratio** | 62.2% |
| **mean_l2** | 0.0909 |

**Per-task SR:**

| Task | SR |
|------|-----|
| next_to_ramekin | 100% |
| next_to_cookie_box | 80% |
| between_plate_and_ramekin | 60% |
| on_cookie_box | 40% |
| next_to_plate | 20% |
| in_top_drawer | 10% |
| from_table_center | 0% |
| on_ramekin | 0% |
| on_stove | 0% |
| on_wooden_cabinet | 0% |

**对比分析：**

| 配置 | SR | avg_K | fast_path |
|------|-----|-------|-----------|
| Spatial P75 (本实验) | 31.0% | 5.02 | 62.2% |
| Spatial K=10 baseline | 34.4% | 10.0 | 0% |
| VLA-only baseline | ~28% | 1 | 100% |
| Object P75 (参考) | 13.7% | 3.1 | 87% |

**Conclusion: success.** Object-calibrated P75 阈值 (τ=0.098735) 跨 benchmark 迁移到 Spatial 有效——SR 31% 达到 K=10 baseline 的 90%，但平均 K 仅 5.0（节省 50% 推理计算）。Spatial 更难导致 fast_path 从 87%→62.2%，触发更多全量 refinement，这是合理的自适应行为。

---
