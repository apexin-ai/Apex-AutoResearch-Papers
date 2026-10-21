# ops harvest scan bjb2 28827 full

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-scan-bjb2-28827-full_20260519T011016_result.json`
- **Structured JSON:** [`309aa148589dd3894202.json`](../../sessions/30/309aa148589dd3894202.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-28827 扫描报告

### GPU 状态
| GPU | Util% | VRAM (used/total) | 进程数 |
|-----|-------|-------------------|--------|
| 0 | 99% | 8038/24564 MiB | 2 |
| 1 | 81% | 5749/24564 MiB | 2 |
| 2 | 18% | 4736/24564 MiB | 1 |
| 3 | 99% | 5749/24564 MiB | 2 |
| 4 | 99% | 7607/24564 MiB | 2 |
| 5 | 99% | 8074/24564 MiB | 2 |

**6/6 GPU 满载，0 空闲 slot。** 每张卡跑 1-2 个 eval 进程（共 11 个 eval 分布在 6 卡上）。

### 11 个 Tmux Session — 全部存活

| Session | 状态 | 进度 |
|---------|------|------|
| eval-obs-only-norm003-seed44-t16 | 运行中 | rollout 4/10 |
| eval-obs-only-object-default-seed45-r2 | 运行中 | 输出重定向到 log |
| eval-obs-only-object-default-seed48 | 运行中 | rollout 6/10 |
| eval-obs-only-object-norm005-seed47 | 运行中 | rollout 8/10 |
| eval-obs-only-object-norm01-seed45-r2 | 运行中 | 输出重定向到 log |
| eval-perdof-norm005-seed45-t16 | 运行中 | rollout 1/10 (刚启动) |
| eval-perdof-norm03-seed43-t16 | 运行中 | rollout 5/10 |
| eval-perdof-object-default-seed47 | 运行中 | rollout 3/10 |
| eval-perdof-object-norm003-seed46 | 运行中 | rollout 7/10 |
| eval-perdof-object-norm03-seed47 | 运行中 | rollout 5/10 |
| eval-random-selection-object-seed45 | 运行中 | rollout 5/10 |

**已死未清理的 session：0**

### 已完成实验（最近 12h）

| 实验 | SR |
|------|-----|
| eval_object_obs_only_norm01_seed42 | **19%** |
| eval_object_obs_only_norm02_k5_seed44 | 17% |
| eval_object_obs_only_norm02_k5_seed45 | 15% |
| eval_object_obs_only_default_seed45 | 12% |
| eval_object_random_selection_seed44 | 13% |
| eval_object_perdof_norm01_seed42 | 11% |
| eval_object_random_selection_seed43 | 9% |
| eval_object_perdof_norm02_seed48 | 7% |

### Orphan 进程
无 orphan。所有 python 进程都归属于 tmux session。另有 tensorboard (PID 960) 和 jupyter-lab (PID 964) 常驻服务。

### 小结
机器满载运转，无浪费。obs_only_norm01 目前是最优配置 (SR 19%)，perdof 和 random_selection 整体弱于 obs_only。

---
