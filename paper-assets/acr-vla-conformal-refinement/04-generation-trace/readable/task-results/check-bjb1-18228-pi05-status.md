# check bjb1 18228 pi05 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-18228-pi05-status_20260525T070438_result.json`
- **Structured JSON:** [`c37f91a7ab328df06088.json`](../../sessions/c3/c37f91a7ab328df06088.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | 显存 | 实验 | 状态 | 进度/结果 |
|-----|------|------|------|----------|
| 0 | 0 MiB | π0.5 Adaptive Spatial s42 | **CRASHED** | state_dict size mismatch (checkpoint=2118, model=990) |
| 1 | 0 MiB | π0.5 VLA-only Spatial s42 paired | **COMPLETED** (12:57) | SR=**0.98** (10 tasks × 20 rollouts) |
| 2 | 0 MiB | π0.5 VLA-only Goal s42 paired | **COMPLETED** (12:55) | SR=**0.98** (10 tasks × 20 rollouts) |
| 3 | 9883 MiB / 22% | precompute pi05 long 2048 r2 (PID 114507) | **RUNNING** | 108300/136090 ≈ **79.6%**, ETA ~15h (54186s) |

## 已完成实验

**eval_spatial_vla_only_pi05_seed42_paired** (mode=vla_only, single, spatial, n=20)
- Overall SR = **0.98** (196/200)
- 7 任务 100%；on_ramekin=0.85，on_wooden_cabinet=0.95

**eval_goal_vla_only_pi05_seed42_paired** (mode=vla_only, single, goal, n=20)
- Overall SR = **0.98** (196/200)
- 8 任务 100%；middle_drawer=0.95, wine_bottle_cabinet=0.95, push_plate=0.90

## 失败实验

**eval_spatial_adaptive_pi05_seed42** (13:26 crash, log: `/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_pi05_seed42.log`)
```
RuntimeError: size mismatch for input_mean: checkpoint=[2118], model=[990]
```
checkpoint 是用更大 input dim (2118) 训练的，eval 脚本用默认 (990) 构造 ConformalRefinementModule。需对齐 `--input_dim 2118` 或换匹配的 checkpoint，然后重跑。

## 仍在运行

**precompute-pi05-long-2048-r2**（GPU 3, PID 114507, 已运行 2d10h44m）
- 进度：108300 / 136090（79.6%）
- 速率：1.95 s/sample
- 剩余约 **15 小时**（~54186s）
- 输出：`/root/autodl-tmp/crm_cache_pi05_2048/long/`（partial_s0_*.pt 持续写入）
- 日志：`/root/autodl-tmp/logs/precompute_pi05_long_2048.log`（非 `/tmp/precompute-pi05-long-2048-r2.log`）

---
