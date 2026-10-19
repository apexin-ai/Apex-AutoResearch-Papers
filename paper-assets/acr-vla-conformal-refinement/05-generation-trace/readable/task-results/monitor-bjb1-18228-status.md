# monitor bjb1 18228 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb1-18228-status_20260515T044904_result.json`
- **Structured JSON:** [`6490580149be309b5ff9.json`](../../sessions/64/6490580149be309b5ff9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 Spatial Eval Status

| Experiment | Mode | PID | Tasks Done | Current SR | Status |
|---|---|---|---|---|---|
| reconvla | reconvla, K=10 | 231426 | 9/10 | 36.7% (33/90) | running T10 |
| acr_vla (perdof) | acr_vla, norm=0.1 | 253085 | 7/10 | 42.9% (30/70) | running T8 |
| obs_only | crm_obs_only, norm=0.1 | 270097 | 6/10 | 40.0% (24/60) | running T7 |
| scalar | crm_scalar, norm=0.1 | 288939 | 3/10 | 56.7% (17/30) | running T4 |

GPU: 4x RTX 4090, all occupied by these 4 experiments. No JSON output files yet.

### Per-task breakdown (short task names)

| Task | reconvla | acr_vla | obs_only | scalar |
|---|---|---|---|---|
| T0 between_plate_ramekin | 60% (6/10) | 60% (6/10) | **90%** (9/10) | 60% (6/10) |
| T1 next_to_ramekin | **100%** (10/10) | **100%** (10/10) | **100%** (10/10) | **100%** (10/10) |
| T2 table_center | 0% (0/10) | 10% (1/10) | 0% (0/10) | 10% (1/10) |
| T3 on_cookie_box | 30% (3/10) | 40% (4/10) | 40% (4/10) | *running* |
| T4 top_drawer | 10% (1/10) | 0% (0/10) | 10% (1/10) | — |
| T5 on_ramekin | 10% (1/10) | 0% (0/10) | 0% (0/10) | — |
| T6 next_to_cookie_box | **90%** (9/10) | **90%** (9/10) | *running* (5/5@r5) | — |
| T7 on_stove | 0% (0/10) | — | — | — |
| T8 next_to_plate | 30% (3/10) | — | — | — |
| T9 on_wooden_cabinet | *running* (0/5@r5) | — | — | — |

### 关键观察

- **T1 (next_to_ramekin)** 所有方法都 100%，是最简单的任务
- **T2 (table_center)** 所有方法都接近 0%，是最难的任务
- **obs_only 在 T0 上显著高** (90% vs 60%)，但在 T5 上也是 0%
- **scalar 目前只完成 3 个 task**，进度最慢，当前 SR 偏高是因为还没遇到难任务
- reconvla 接近完成（9/10），预估最终 SR ~33-37%（T9 on_wooden_cabinet 当前 0/5）

---
