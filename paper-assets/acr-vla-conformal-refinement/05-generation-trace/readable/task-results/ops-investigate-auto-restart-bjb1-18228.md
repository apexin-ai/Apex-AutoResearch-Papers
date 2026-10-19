# ops investigate auto restart bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-auto-restart-bjb1-18228_20260517T223720_result.json`
- **Structured JSON:** [`b8396487d768c83b8909.json`](../../sessions/b8/b8396487d768c83b8909.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键证据已收集完毕。

## 排查结论

### SIGHUP 事件
从 sentinel 文件确认：**2026-05-17T18:30:58Z (北京时间 05-18 02:30:58)** 所有运行中的进程同时收到 SIGHUP (exit code 129)：
- `eval-obs-only-object-norm02-k5-seed42.exit`: 129
- `eval-obs-only-object-norm02-k20-seed42.exit`: 129  
- `eval-obs-only-object-norm005-seed43-r3.exit`: 129
- `eval-perdof-object-norm02-seed45-r2.exit`: 129 (7秒更早)

这是一次**批量 SIGHUP 事件**——所有 tmux session 内的进程同时被 kill，最可能原因是 tmux server 进程本身崩溃或被重启（容器层面事件）。

### 重启机制

**不是**系统级自动重启（tmux respawn / supervisord / systemd / crontab 都不是）。

**实际机制**：Agent-driven retry
1. `submit_training_job` 启动任务时在 bash wrapper 中注册了 EXIT trap，进程死亡时写入 sentinel 文件 (`/tmp/agent-ml-exit/&lt;exp_id>.exit`)
2. `core/tools/cron.py` 的 cron_poller (每 30-120s 轮询) 通过 sentinel 检测到进程死亡 + exit_code=129
3. Cron 系统将实验状态从 RUNNING → DONE(failed)
4. Worker agent 被调度，检测到 failed 状态后通过 `submit_training_job` 重新提交
5. `core/tools/registry.py` 中 `retry_count` 从 0 → 1

从时间线看：SIGHUP 发生在 02:30，新 tmux session `eval-obs-k5` 创建于 02:54——间隔约 24 分钟（包括 cron 检测 + Worker 调度 + 提交）。

### 是否需要禁用

不需要禁用——这个 retry 是 Agent 系统的正常行为（Worker 主动决策重提交，不是盲目的自动重启）。`max_retries` 默认为 3，超限后会拒绝重试。

如果需要防止特定实验被重试，可以在 registry 中设置 `max_retries=0`。

---
