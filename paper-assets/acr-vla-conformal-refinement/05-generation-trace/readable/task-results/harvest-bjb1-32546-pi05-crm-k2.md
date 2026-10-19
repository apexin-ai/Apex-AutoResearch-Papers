# harvest bjb1 32546 pi05 crm k2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546-pi05-crm-k2_20260526T084700_result.json`
- **Structured JSON:** [`552be475421eabbaee12.json`](../../sessions/55/552be475421eabbaee12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：cron 误报，6 个实验均未完成，仍在运行

**关键证据：**
- `ps -ef` 显示 6 个 `python -u src/evaluate.py` 进程全部活跃，CPU 时间 7+ 小时
- `tmux ls` 列出全部 6 个 session（名称无 `-bjb1` 后缀 — 这是 cron 检测失败的原因）
- 6 个 GPU 显存 10-11GB 占用，利用率 21-43%
- JSON 输出文件均不存在（eval 脚本仅在最后写入）

**当前任务进度（LIBERO 每 suite 10 个任务 × 20 rollouts）：**

| exp_id | tasks done | 当前任务进度 | status |
|--------|-----------|--------------|--------|
| pi05-crm-k2-goal-s42-bjb1 | 8/10 | put_the_bowl_on_the_plate 10/20 | RUNNING |
| pi05-crm-k2-goal-s43-bjb1 | 8/10 | put_the_bowl_on_the_plate 5/20 | RUNNING |
| pi05-crm-k2-goal-s44-bjb1 | 8/10 | put_the_bowl_on_the_plate 10/20 | RUNNING |
| pi05-crm-k2-object-s42-bjb1 | 7/10 | butter task 完成 | RUNNING |
| pi05-crm-k2-object-s43-bjb1 | 6/10 | butter 10/20 | RUNNING |
| pi05-crm-k2-object-s44-bjb1 | 7/10 | butter 15/20 | RUNNING |

**建议处置：**
- **不要 kill，不要改 registry**。所有实验都还在跑，预计还需 1-2 小时（每个任务约 30-50 分钟）。
- cron 监控规则需修复：当前应在搜索 `pi05-crm-k2-*-bjb1` 但实际 tmux session 名是 `pi05-crm-k2-*`（无 `-bjb1` 后缀）。
- 等待 JSON 文件生成后再 harvest。

---
