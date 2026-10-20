# diagnose grpo v2 trainer state

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo-v2-trainer-state_20260514T122645_result.json`
- **Structured JSON:** [`c8469eb6e9a3cd7320f6.json`](../../sessions/c8/c8469eb6e9a3cd7320f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete picture:

## GRPO v2 训练状态

**进程**: PID 30171, 运行中 (state R), 已运行 1h29m, RSS 2.6GB

**进度**: Step 8/73, 平均 ~10.75 min/step

**GPU**: cuda:0 — 38% utilization, 28.7GB/95.6GB | cuda:1 — idle

## Reward Metrics: 当前不可读

从启动命令确认的参数:
- `--save-steps 50` — 首次 checkpoint 在 step 50
- `--logging-steps 5` — 每 5 步记录 metrics
- 未传 `--wandb-run-name` → `report_to="none"`, 无 wandb
- 无 tensorboard events

**grpo_v2 checkpoint 目录为空** — step 50 才会写 trainer_state.json。

Metrics 存在于进程内存的 `trainer.state.log_history` 和 stdout buffer 中，但因 nohup 全缓冲，stdout 未刷到日志文件。grep 在日志中找不到任何 reward/loss 字样。

## 时间估算

| 里程碑 | 预计时间 (May 15) |
|--------|-------------------|
| Step 50 (首次 checkpoint) | ~03:55 |
| Step 73 (训练完成) | ~08:03 |

距首次 checkpoint 约 **7.5 小时**。

## 建议

当前没有途径读取 reward metrics。可选方案：
1. **等 step 50 checkpoint** (~7.5h 后读 trainer_state.json)
2. **提前终止并重启，加 `--save-steps 10`**（能更早看到 metrics，但丢失当前 8 步进度）
3. **重启时加 `--wandb-run-name grpo-v2`**（实时 metrics，但同样需要重启）

---
