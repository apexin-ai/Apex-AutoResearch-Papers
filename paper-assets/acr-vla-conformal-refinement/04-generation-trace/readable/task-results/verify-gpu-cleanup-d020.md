# verify gpu cleanup d020

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_gpu-cleanup-d020_20260514T223850_result.json`
- **Structured JSON:** [`c4fadb536ec9f1c8bdc9.json`](../../sessions/c4/c4fadb536ec9f1c8bdc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-40593
- PID 199257: **DEAD** (confirmed killed)
- PID 203222: **DEAD** (confirmed killed)
- PID 201029 (vla-mean-t10): **ALIVE** — `evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --start_task 9`
- GPU 0 状态: 占用 by PID 201029, 1915MiB/24564MiB, 12% util

## bjb1-18228
- GPU 0: PID 270097 (crm_obs_only, obs-only-r2) — 6221MiB 主进程 + PID 231426/232820/253085 各占 ~2655-3714MiB 共享显存 = **15293MiB/24564MiB**
- GPU 1: PID 231426 (eval-argmin-only-spatial, `crm_v2/perdof`) — 1414MiB
- GPU 2: PID 232820 (eval-tiny-correction-spatial, `crm_v2/perdof`, max_correction_norm=0.05) — 1450MiB
- GPU 3: PID 253085 (eval_acr_spatial_v4_small, `crm_v3_norm/perdof`, max_correction_norm=0.1) — 1450MiB
- PID 270097 (obs-only-r2): **ALIVE**
- 是否有 scalar eval 进程: **NO** — 没有 scalar 相关进程，四个 GPU 上跑的都是之前的 eval 任务

---
