# ssh scan bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scan-bjb2-28827_20260520T024054_result.json`
- **Structured JSON:** [`552b47f3ec2f8c0e72b3.json`](../../sessions/55/552b47f3ec2f8c0e72b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-28827 全面状态扫描

### GPU 状态 (6× 24GB)

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| 0 | 0% | 1 MiB | **空闲** |
| 1 | 0% | 1 MiB | **空闲** |
| 2 | 25% | 1961 MiB | **运行中** — PID 85772 |
| 3 | 0% | 1 MiB | **空闲** |
| 4 | 0% | 1 MiB | **空闲** |
| 5 | 0% | 1 MiB | **空闲** |

### 唯一在跑的进程

**PID 85772** (cuda:2) — `eval-adaptive-k-p25-seed43`
- `--adaptive_threshold 0.054959 --k_full 10 --benchmark object --seed 43`
- 日志进度：正在跑 `pick_up_the_milk_and_place_it_in_the_basket` (2/10 success)

### 已完成的已知部署

| 任务 | Exit | 完成时间 | JSON |
|------|------|----------|------|
| eval-vla-only-goal-seed44-r2 | 0 | 05-19 18:20 | eval_goal_vla_only_seed44_r2.json (1.3KB) |
| eval-argmin-object-k5-seed44-r2 | 0 | 05-19 19:14 | eval_object_argmin_k5_seed44_r2.json (1.5KB) |
| eval-obs-only-spatial-norm02-seed46-r2 | 0 | 05-19 18:50 | eval_spatial_obs_only_norm02_seed46_r2.json (1.7KB) |
| eval-openvla-object-baseline-seed42 | **1 (失败)** | 05-19 23:07 | **无 JSON** |
| eval-perdof-object-norm02-seed48 | 0 | 05-18 14:34 | eval_object_perdof_norm02_seed48.json |
| eval-adaptive-k-p90-seed43 | 0 | 05-20 02:25 | eval_adaptive_k_p90_seed43.json |
| eval-adaptive-k-p75-seed42 | 0 | 05-20 02:29 | eval_adaptive_k_p75_seed42.json |
| eval-adaptive-k-p75-seed43 | 0 | 05-20 02:30 | eval_adaptive_k_p75_seed43.json |
| eval-adaptive-k-p50-seed42 | 0 | 05-20 02:34 | eval_adaptive_k_p50_seed42.json |
| eval-adaptive-k-p90-seed44 | 0 | 05-20 02:36 | eval_adaptive_k_p90_seed44.json |

- **eval-obs-only-object-norm005-seed43**: 无 exit 文件、无 JSON — 可能未在此服务器启动
- **eval-openvla-object-baseline-seed42**: exit code 1，失败，未产出 JSON

### Adaptive-K JSON 结果汇总

| 配置 | overall_SR | avg_actual_k | fast_path_ratio |
|------|-----------|--------------|-----------------|
| **p50_seed42** | **0.16** | 3.72 | 78.5% |
| **p75_seed42** | 0.12 | 3.07 | 86.6% |
| **p75_seed43** | 0.13 | 3.15 | 85.6% |
| **p90_seed43** | 0.14 | 2.61 | 92.3% |
| **p90_seed44** | 0.14 | 2.58 | 92.8% |
| **p25_seed43** | 运行中 | — | — |

趋势：更高 percentile 阈值 → 更高 fast_path_ratio（更多跳过 refinement）、更低 avg_k，但 SR 差异不大（0.12-0.16）。p50 反而 SR 最高（0.16）。

### 需关注

1. **eval-openvla-object-baseline-seed42** exit code 1，需要查日志排查失败原因
2. **5 张 GPU 空闲**（0/1/3/4/5），可以部署新任务
3. **eval-adaptive-k-p25-seed43** 是唯一在跑的，预计还需一段时间

---
