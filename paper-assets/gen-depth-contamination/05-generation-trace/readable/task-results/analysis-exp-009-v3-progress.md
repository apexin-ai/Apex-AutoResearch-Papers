# analysis exp 009 v3 progress

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_009_v3_progress_20260517T081806_result.json`
- **Structured JSON:** [`555ced127f559985d09f.json`](../../sessions/55/555ced127f559985d09f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-009 v3 Dose-Response 进度汇报

| Ratio | PID | 状态 | 已完成 | 当前任务 | 预计剩余 |
|-------|-----|------|--------|----------|----------|
| **10%** | 4187 | **存活** (1h12m) | **13/15** | seed=4, binary_ours — eval 68% (65949/96336) | **~30 min** |
| **30%** | 4327 | **存活** (1h12m) | **13/15** | seed=4, binary_ours — eval 46% (43841/96336) | **~35 min** |
| **50%** | 4404 | **存活** (1h12m) | **12/15** | seed=4, no_filter — eval 35% (33855/96336) | **~55 min** |

### 结果文件统计
路径: `results/exp_009_dose_response/ratio_XX/`

- **ratio_10**: 13 个 eval.json (seed 0-3 全部完成 + seed4 no_filter)
- **ratio_30**: 13 个 eval.json (seed 0-3 全部完成 + seed4 no_filter)
- **ratio_50**: 12 个 eval.json (seed 0-3 全部完成)

### 剩余工作
- **10%**: binary_ours_seed4 (当前 68%) → graduated_seed4 = 2 cycles
- **30%**: binary_ours_seed4 (当前 46%) → graduated_seed4 = 2 cycles
- **50%**: no_filter_seed4 (当前 35%) → binary_ours_seed4 → graduated_seed4 = 3 cycles

Seeds 0-3 全部从之前 run 恢复跳过。每个 cycle 约 20-25 min (train ~3min + eval ~18min)。预计 10%/30% 约 30-35 min 内完成，50% 约 55 min 内完成。

---
