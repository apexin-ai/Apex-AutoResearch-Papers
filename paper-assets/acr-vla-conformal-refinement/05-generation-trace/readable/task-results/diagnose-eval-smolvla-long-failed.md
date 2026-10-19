# diagnose eval smolvla long failed

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-smolvla-long-failed_20260522T151015_result.json`
- **Structured JSON:** [`cf96c32f3aae9995f65a.json`](../../sessions/cf/cf96c32f3aae9995f65a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断报告

### 根因

**eval-vla-only-long-seed{0,1,2} 进程被人为终止并替换。** 

时间线：
- **22:19** — 三个 eval-vla-only-long 进程启动（使用项目自带 `evaluate.py`，`model=smolvla, mode=vla_only`）
- **~23:00** — 三个进程的 tmux session 被销毁（运行 ~40 分钟，完成 2/10 tasks），无错误日志、无 sentinel、无 W&B
- **23:05** — 三个 **eval-lerobot-long-seed{0,1,2}** 替代进程启动（使用 LeRobot 框架 `lerobot.scripts.lerobot_eval`），分配到 GPU 0/1/2

### 当前状态

**替代的 lerobot eval 进程仍在运行**，已运行 ~5 小时，完成约 63/200 rollouts（~31%）。预计还需 ~10 小时完成。

### 为什么 cron 报告失败

监控系统跟踪的是原始实验名 "eval-smolvla-long-seed{0,1,2}"，对应 eval-vla-only-long tmux session。这些 session 已被销毁，进程不存在、无 sentinel 文件、无 W&B run → cron 正确检测为 "process dead"。替代的 lerobot 进程使用了不同的实验名，不在监控范围内。

### 影响

无数据丢失。等价的评估正在以不同框架运行中。

### 修复建议

1. **无需重跑** — 等 lerobot eval 完成即可（预计还需 ~10h）
2. 在监控系统中注册 eval-lerobot-long-seed{0,1,2}，或将 cron 中的失败状态标记为 "superseded"

---
