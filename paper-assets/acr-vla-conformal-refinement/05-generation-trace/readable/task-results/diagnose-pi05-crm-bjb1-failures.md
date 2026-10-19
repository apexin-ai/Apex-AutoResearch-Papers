# diagnose pi05 crm bjb1 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-crm-bjb1-failures_20260526T093242_result.json`
- **Structured JSON:** [`8b5d6f3868276fdc419f.json`](../../sessions/8b/8b5d6f3868276fdc419f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根因：监控误报（false positive）

实验**没有失败**。监控系统检测不到 sentinel 文件或 W&B 活动，5次探测后自动标记为 failed。但实际上：

### 3个 Goal 实验：已全部完成 ✅

| 实验 | 状态 | 结果 |
|------|------|------|
| goal-s42 | 完成 (17:24) | **83.5%** (167/200) |
| goal-s43 | 完成 (17:32) | JSON 已保存 |
| goal-s44 | 完成 (17:23) | JSON 已保存 |

### 3个 Object 实验：仍在运行中 🔄

| 实验 | PID | GPU | 进度 |
|------|-----|-----|------|
| object-s42 | 600978 | GPU 3 (10.4GB) | 正在跑 chocolate_pudding 任务 |
| object-s43 | 601242 | GPU 4 (10.4GB) | 正在跑 chocolate_pudding 任务 |
| object-s44 | 601320 | GPU 5 (10.4GB) | chocolate_pudding 已完成 (100%) |

Object suite 任务数比 Goal 多（包含多个 pick_up_X_and_place_it_in_the_basket），运行时间更长（从 13:46 开始已跑近 4 小时），接近尾声。

### 服务器状态

- **磁盘**：根分区 34%，充裕
- **GPU**：0-2 空闲，3-5 被 object 实验占用
- **无 OOM / 无崩溃**
- **sentinel 目录为空**——实验脚本没有写 sentinel 文件，这是监控误判的直接原因

### 结论

- 6个实验**全部正常**，3个已完成有结果，3个还在跑即将结束
- 失败原因统一：evaluate.py 不写 sentinel 也不发 W&B，监控系统超时判定为 dead
- 无需重跑，等 object 实验自然跑完即可
- 长期修复：在 evaluate.py 中加 sentinel 写入，或调整监控对 eval 任务的超时策略

---
