# check bjb1 32546 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-32546-status_20260525T174354_result.json`
- **Structured JSON:** [`0587bbcd320ed7666a59.json`](../../sessions/05/0587bbcd320ed7666a59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546 进程状态

**实际运行的实验与 registry 记录不一致。** Registry 中的 9 个实验（eval-smolvla-crm-goal-seed44 等）均已不存在（PID 70782 已死），服务器上跑的是另一批新实验。

### 当前活跃进程（6个）

| 实验 | GPU | PID | 状态 | 进度 |
|------|-----|-----|------|------|
| smolvla crm_obs_only, long benchmark, seed44 | 3 | 185264 | RUNNING | 正在跑 KITCHEN_SCENE6 |
| smolvla adaptive_conformal_crm, long benchmark, seed43 | 4 | 185266 | RUNNING | 正在跑 KITCHEN_SCENE8 |
| **pi05** crm_obs_only, spatial benchmark, seed44 | 5 | 194257 | RUNNING | 接近完成 (95% SR on last task) |
| **pi05** crm_obs_only, object benchmark, seed42 | 0 | 269240 | RUNNING | 刚启动(01:42) |
| **pi05** crm_obs_only, object benchmark, seed43 | 1 | 269242 | RUNNING | 刚启动(01:42) |
| **pi05** crm_obs_only, object benchmark, seed44 | 2 | 269244 | RUNNING | 刚启动(01:42) |

### GPU 使用

| GPU | 状态 | 占用 |
|-----|------|------|
| 0 | 忙 | pi05 object s42 (刚启动，模型加载中) |
| 1 | 忙 | pi05 object s43 (同上) |
| 2 | 忙 | pi05 object s44 (同上) |
| 3 | 忙 | smolvla long crm s44 (1950 MiB) |
| 4 | 忙 | smolvla long adaptive s43 (1702 MiB) |
| 5 | 忙 | pi05 spatial crm s44 (12565 MiB) |

**所有 6 GPU 满载，无空闲。**

### 已完成结果（未收录，共 9 个文件）

| 文件 | 模型 | Benchmark | Mode | Seed | SR |
|------|------|-----------|------|------|----|
| eval_goal_crm_obs_only_norm0.05_seed42.json | smolvla | goal | crm_obs_only | 42 | **0.82** |
| eval_goal_crm_seed43.json | smolvla | goal | crm_obs_only | 43 | **0.82** |
| eval_goal_crm_seed44.json | smolvla | goal | crm_obs_only | 44 | **0.82** |
| eval_object_crm_seed42.json | smolvla | object | crm_obs_only | 42 | **0.77** |
| eval_object_crm_seed43.json | smolvla | object | crm_obs_only | 43 | **0.785** |
| eval_object_crm_seed44.json | smolvla | object | crm_obs_only | 44 | **0.74** |
| eval_spatial_crm_seed48.json | smolvla | spatial | crm_obs_only | 48 | **0.805** |
| eval_spatial_crm_obs_only_norm0.05_seed47.json | smolvla | spatial | crm_obs_only | 47 | **0.815** |
| eval_spatial_crm_obs_only_norm0.05_seed49.json | smolvla | spatial | crm_obs_only | 49 | **0.79** |

### 结论

- Registry 中标记为 RUNNING 的 9 个实验（eval-smolvla-crm-goal-seed44, eval-k2-spatial-* 系列等）**全部已死/不存在**，需要标记为 DEAD
- 服务器上实际在跑 **6 个新实验**（2个 smolvla long horizon + 4个 pi05），这些可能未注册
- 有 **9 个已完成的 JSON 结果**等待收录

---
