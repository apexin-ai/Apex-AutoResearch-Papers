# analysis bjb1 18228 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bjb1-18228-batch_20260520T124445_result.json`
- **Structured JSON:** [`adfe4e8732324dfeb080.json`](../../sessions/ad/adfe4e8732324dfeb080.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果

### 实验 1: eval-random-selection-spatial-seed43

| 指标 | 值 |
|------|-----|
| **exp_id** | eval-random-selection-spatial-seed43 |
| **overall_sr** | **26.0%** (26/100) |
| **conclusion** | **SUCCESS** — 假设确认 |

**Per-task SR:**

| Task (简称) | SR |
|---|---|
| between_plate_and_ramekin | 70.0% |
| next_to_ramekin | 90.0% |
| from_table_center | 0.0% |
| on_cookie_box | 10.0% |
| in_top_drawer | 0.0% |
| on_ramekin | 0.0% |
| next_to_cookie_box | 70.0% |
| on_stove | 0.0% |
| next_to_plate | 20.0% |
| on_wooden_cabinet | 0.0% |

**分析**: Random selection 26.0% ≈ VLA-only baseline (~29.6%)，与 Object benchmark 上的结论一致（Object: random 11.3% ≈ VLA-only 10.9%）。确认 CRM 的改善来自 guidance quality 而非 sampling diversity。

---

### 实验 2: eval-adaptive-k-spatial-p90-seed43

| 指标 | 值 |
|------|-----|
| **exp_id** | eval-adaptive-k-spatial-p90-seed43 |
| **overall_sr** | **32.0%** (32/100) |
| **avg_K** | 3.59 |
| **fast_path_pct** | 80.2% |
| **mean_l2** | 0.0905 |
| **threshold** | 0.12587 (P90) |
| **total_steps** | 23,797 (fast: 19,079 / full: 4,718) |
| **conclusion** | **SUCCESS** — cross-benchmark validation 通过 |

**Per-task SR:**

| Task (简称) | SR |
|---|---|
| between_plate_and_ramekin | 70.0% |
| next_to_ramekin | 100.0% |
| from_table_center | 10.0% |
| on_cookie_box | 30.0% |
| in_top_drawer | 0.0% |
| on_ramekin | 10.0% |
| next_to_cookie_box | 80.0% |
| on_stove | 0.0% |
| next_to_plate | 20.0% |
| on_wooden_cabinet | 0.0% |

**Cross-benchmark 对比 (P90 regime):**

| 指标 | Object | Spatial |
|------|--------|---------|
| SR | 13.3% | 32.0% |
| avg_K | ~2.6 | 3.59 |
| fast_path | ~93% | 80.2% |

**分析**: Spatial 上 CRM 触发 full refinement 更频繁（19.8% vs ~7%），avg_K 更高，说明 spatial tasks 中 CRM 检测到更多不确定性。尽管如此，80% 步骤仍走 fast path (K=2)，计算节省显著。SR 32.0% 高于 VLA-only 29.6%，adaptive-k P90 在保持大幅计算节省的同时仍有正向增益。无异常或错误。

---
