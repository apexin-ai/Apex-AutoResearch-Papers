# code add per episode data to eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add_per_episode_data_to_eval_20260520T182019_result.json`
- **Structured JSON:** [`b0180c393d385c649742.json`](../../sessions/b0/b0180c393d385c649742.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果

**两台服务器均已修改，语法验证通过，行数一致（454 → 476，+22行）。**

### 修改摘要（7处 patch）

| # | 位置 | 改动 |
|---|------|------|
| 1 | `run_episode` 函数体 | 新增 `step_count = 0` |
| 2 | episode 步进循环 | `step_count += 1`（在 `prepare_obs` 前，仅计实际步） |
| 3 | `run_episode` 返回值 | `return success, replay_images, step_count` |
| 4 | `main` 初始化 | 新增 `all_episodes = []` |
| 5 | `main` 调用处 | 解包 `success, replay, step_count = run_episode(...)` |
| 6 | `episodes.append` | 增加 `trajectory_length`；新增 `all_episodes.append(...)` 收集全局数据 |
| 7 | `results["summary"]` | 增加 `total_collisions` + `displacement_stats`(min/max/mean/median)；新增 `results["per_episode"]` |

### JSON 输出结构示例

```json
{
  "config": { "checkpoint": "...", "task_suite": "libero_spatial", ... },
  "tasks": {
    "pick up the black bowl...": {
      "task_id": 0, "n": 20, "tsr": 0.85, "car": 0.70,
      "episodes": [
        {"ep": 0, "success": true, "collision": false, "max_disp": 0.000312, "coll_step": -1, "trajectory_length": 145},
        ...
      ]
    }
  },
  "per_episode": [
    {"task_id": 0, "task_name": "pick up the black bowl...", "episode_idx": 0,
     "max_displacement": 0.000312, "collision_detected": false, "trajectory_length": 145, "task_success": true},
    ...
  ],
  "summary": {
    "total_episodes": 200, "tsr": 0.82, "car": 0.65,
    "total_collisions": 70,
    "displacement_stats": {"min": 0.0001, "max": 0.0523, "mean": 0.0089, "median": 0.0034}
  }
}
```

---
