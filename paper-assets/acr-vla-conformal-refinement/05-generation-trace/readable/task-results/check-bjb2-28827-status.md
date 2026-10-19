# check bjb2 28827 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb2-28827-status_20260525T174403_result.json`
- **Structured JSON:** [`7a5f7aa9ba64aa9eee1e.json`](../../sessions/7a/7a5f7aa9ba64aa9eee1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-28827 进程状态

### Registry 7 个实验状态

| # | exp_id | 状态 | 结果 |
|---|--------|------|------|
| 1 | eval-adaptive-long-s44-d149 | **DONE** | SR=54.0%, trigger=4.5%, benchmark=long |
| 2 | eval-adaptive-long-s42-d149 | **DONE** | SR=58.0%, trigger=4.3%, benchmark=long |
| 3 | eval-pi05-vla-only-object-s43 | **DONE** (PID 732901 已退出) | SR=98.5%, benchmark=object, model=pi05 |
| 4 | eval-pi05-vla-only-goal-s44 | **DONE** (PID 733782 已退出) | SR=97.5%, benchmark=goal, model=pi05 |
| 5 | eval-pi05-adaptive-object-s43 | **DEAD** (PID 733341 不存在) | nohup log 停在 task 2/10，无 json 输出 |
| 6 | eval-pi05-adaptive-object-s42 | **DEAD** (PID 732464 不存在) | nohup log 停在 task 2/10，无 json 输出 |
| 7 | eval-pi05-adaptive-goal-s43 | **DEAD** (PID 732018 不存在) | nohup log 停在 ~task 6/10，无 json 输出 |

#5/#6/#7 被后提交的实验抢占 GPU 后中断，未产出结果。

### GPU 使用情况

| GPU | 显存 | 利用率 | 当前进程 |
|-----|------|--------|---------|
| 0 | 4 MiB | 0% | pi05 crm_obs_only long s42 (加载模型中) |
| 1 | 4 MiB | 0% | pi05 crm_obs_only long s43 (加载模型中) |
| 2 | 2422 MiB | 24% | **SmolVLA crm_obs_only long s44** (task 9/10) |
| 3 | 3 MiB | 0% | pi05 crm_obs_only spatial s42 (加载模型中) |
| 4 | 3 MiB | 0% | pi05 crm_obs_only spatial s43 (加载模型中) |
| 5 | 2328 MiB | 19% | **SmolVLA adaptive long s43** (task 9/10) |

### 当前实际运行的实验（非 registry 中的）

- **GPU 2**: SmolVLA `crm_obs_only --benchmark long --seed 44` (PID 857632, 运行~24h, 即将完成)
- **GPU 5**: SmolVLA `adaptive_conformal_crm --benchmark long --seed 43` (PID 857635, 运行~24h, 即将完成)
- **GPU 0/1/3/4**: 4 个 Pi0.5 `crm_obs_only` 实验刚启动 (01:42)，正在加载模型，尚未占 GPU 显存

### 已完成但需确认是否收录的结果

- `eval_goal_adaptive_seed42.json` — SmolVLA adaptive goal s42, SR=83.5%, trigger=8.3% (tmux session 已完成)
- `eval_long_adaptive_seed44.json` — SR=54.0% (registry #1)
- `eval_long_adaptive_seed42.json` — SR=58.0% (registry #2)
- `eval_object_vla_only_pi05_seed43.json` — SR=98.5% (registry #3)
- `eval_goal_vla_only_pi05_seed44.json` — SR=97.5% (registry #4)

---
