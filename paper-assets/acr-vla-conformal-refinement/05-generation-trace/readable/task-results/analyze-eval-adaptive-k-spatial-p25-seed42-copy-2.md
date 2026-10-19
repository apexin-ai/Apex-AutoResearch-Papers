# analyze eval adaptive k spatial p25 seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-adaptive-k-spatial-p25-seed42_20260520T105122_result.json`
- **Structured JSON:** [`90700270e393cfa120d5.json`](../../sessions/90/90700270e393cfa120d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

## eval-adaptive-k-spatial-p25-seed42 — **DONE (negative)**

| Metric | Value |
|--------|-------|
| **Overall SR** | **33.0%** (vs ~34% Spatial K=10 baseline) |
| **Avg K** | 7.65 (vs 4.8 on Object) |
| **Fast path %** | 29.4% (vs 65% on Object) |
| **Mean L2** | 0.0892 |
| **Threshold (τ)** | 0.054959 |

### Per-task breakdown

| Task | SR |
|------|----|
| next_to_ramekin | 100% |
| next_to_cookie_box | 90% |
| between_plate_and_ramekin | 70% |
| on_cookie_box | 30% |
| next_to_plate | 30% |
| in_top_drawer | 10% |
| from_table_center | 0% |
| on_ramekin | 0% |
| on_stove | 0% |
| on_wooden_cabinet | 0% |

### Analysis

P25 threshold (0.054959) calibrated on Object does **not** transfer to Spatial: fast path drops from 65% → 29.4%, avg K rises from 4.8 → 7.65. The CRM's L2 distances on Spatial are systematically higher, so the Object-calibrated threshold is too tight — almost always triggers full K=10. SR is preserved (33% ≈ baseline) precisely because there's minimal fast-path usage. The threshold needs per-benchmark calibration to be useful.

---
