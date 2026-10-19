# analyze eval adaptive k spatial p25 seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-adaptive-k-spatial-p25-seed42_20260520T103941_result.json`
- **Structured JSON:** [`488c4c6870863dbbb3e9.json`](../../sessions/48/488c4c6870863dbbb3e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval-adaptive-k-spatial-p25-seed42 结果

### 核心指标
- **SR: 33%** (33/100)
- **avg_K: 7.65**
- **fast_path_ratio: 29.4%** (6,873 / 23,410 steps)
- mean_l2_distance: 0.0892
- threshold (τ): 0.054959 (Object-calibrated P25)
- total_steps: 23,410

### Per-task breakdown

| Task (简写) | SR |
|---|---|
| between_plate_and_ramekin | 70% (7/10) |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 30% (3/10) |
| in_top_drawer_wooden_cabinet | 10% (1/10) |
| on_ramekin | 0% (0/10) |
| next_to_cookie_box | **90%** (9/10) |
| on_stove | 0% (0/10) |
| next_to_plate | 30% (3/10) |
| on_wooden_cabinet | 0% (0/10) |

4个任务0%，2个任务≥90%，分化严重。

### 对比

| 方法 | SR | avg_K | fast_path |
|---|---|---|---|
| **Adaptive P25 (本次)** | **33%** | 7.65 | 29.4% |
| Adaptive P75 (seed42) | 31% | 5.02 | 62.2% |
| VLA-only baseline (4 seeds avg) | ~29.5% | 1 | 100% |
| CRM K=10 obs-only (2 seeds avg) | ~34% | 10 | 0% |
| ReconVLA spatial | 10% | — | — |

- **vs VLA-only**: P25 +3.5pp (33% vs 29.5%)，但代价是 avg_K=7.65（接近满 K=10）
- **vs CRM K=10**: P25 几乎持平（33% vs 34%），节省 ~23.5% 计算量（avg_K 7.65 vs 10）
- **vs P75**: P25 SR 略高 +2pp（33% vs 31%），但 fast_path 远低（29.4% vs 62.2%）。P75 用一半的计算量几乎达到相同 SR。
- P25 阈值（Object 上 calibrated）迁移到 Spatial 后 fast_path 只有 29.4%（vs Object 上预期的 ~65%），说明 **跨 benchmark 阈值迁移效果不佳**——Spatial 的 CRM 预测 L2 分布与 Object 差异较大。

### 日志状态
正常完成，EXIT_CODE=0，无 error/traceback。

---
