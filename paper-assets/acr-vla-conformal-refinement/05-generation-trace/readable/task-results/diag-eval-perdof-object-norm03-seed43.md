# diag eval perdof object norm03 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-perdof-object-norm03-seed43_20260518T212146_result.json`
- **Structured JSON:** [`2e46e60df88c5bd7a193.json`](../../sessions/2e/2e46e60df88c5bd7a193.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

---

## 诊断汇总

### 1. 日志最后在做什么
- **Task 4/10**: `pick_up_the_bbq_sauce_and_place_it_in_the_basket`，rollout 5/10
- 已完成 3 个完整 task（每个 10 rollouts）+ task 4 的 5 个 rollout = 共 35/100 rollouts

### 2. 部分结果
- JSON 文件 **不存在**。脚本只在全部完成后才写 JSON，超时即丢失全部数据。

### 3. Stuck/hang 迹象
- **无 hang 迹象**。Rollouts 逐步推进，没有重复错误、没有卡死。单纯是跑太慢。

### 4. 同类实验运行时间对比

| 实验 | 时长 | 完成度 | 状态 |
|---|---|---|---|
| norm02-seed48 | **~15h 29m** | 10/10 tasks (100 rollouts) | 成功 (EXIT_CODE=0) |
| norm02-seed44 | **~16h 12m** | 10/10 tasks (100 rollouts) | 成功 |
| **norm03-seed43** | **~6h 00m** | 3.5/10 tasks (~35 rollouts) | **超时 (EXIT_CODE=124)** |
| norm005-seed45 | **~5h 25m** | ~3.4/10 tasks (~34 rollouts) | 同样超时（无 EXIT_CODE 记录） |
| norm01-seed47 | **~25 秒** | 0/10 tasks (仅初始化) | 异常：只有 13 行日志，启动后即终止 |

### 5. 根因分析
**Timeout 设置过短。** 成功的 perdof eval（同一台机器，同配置 10 tasks × 10 rollouts × 300 max_steps）需要 **15-16 小时**，但 timeout 只给了 6 小时。6 小时只能跑完约 35% 的 rollouts，然后被 `timeout` 命令 kill。

每个 rollout 平均耗时约 10 分钟，符合预期（300 steps × 需要 VLA + CRM 推理）。

### 6. 建议

1. **将 perdof eval 的 timeout 增加到 18-20 小时**（成功实验约 16h，留 margin）
2. **在 eval 脚本中加入增量保存**：每完成一个 task 就追加写入 JSON，避免超时后数据全丢。当前 seed43 跑了 6 小时的结果完全浪费了
3. **排查 norm01-seed47**：仅运行 25 秒即终止，只有初始化日志，可能是被其他实验挤占或 GPU 问题，需单独诊断

---
