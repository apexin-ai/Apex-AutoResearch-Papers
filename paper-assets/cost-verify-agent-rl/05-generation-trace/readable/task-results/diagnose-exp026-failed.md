# diagnose exp026 failed

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp026_failed_20260515T110843_result.json`
- **Structured JSON:** [`c7a0f3a2d7b551c8bd27.json`](../../sessions/c7/c7a0f3a2d7b551c8bd27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整信息已收集。以下是诊断报告：

---

## exp026_step_independent_grpo 诊断报告

### 结论：进程未退出，CRON 报告为误报

**进程仍在运行。** nvidia-smi 确认 PID 782015 (cuda:0) 和 782016 (cuda:1) 活跃，GPU 利用率 100%，各占用 ~42.7GB/97.9GB 显存。

### CRON 误报原因

WANDB_MODE=disabled，所以不存在远程 W&B metrics。CRON 检查 W&B metrics 未找到，误判为 "Process exited without valid W&B metrics"。

### 训练进度

| 项目 | 状态 |
|------|------|
| 启动时间 | 2026-05-15 18:28（约 50 分钟前，非 21 小时） |
| 当前阶段 | Step 1 进行中（初始 validation 已完成，policy update 已触发） |
| 已完成 steps | 0/150（正在执行 step 1） |
| 日志最后更新 | 19:06:55（FutureWarning from compute_policy_loss） |
| 日志静默原因 | 正在执行 rollout，rollout 期间无 log 输出（stdout buffering） |

### 初始 Validation 指标（Step 0, 16 episodes）

| 指标 | 值 |
|------|------|
| success | 6.25% (1/16) |
| action_is_valid | 63.1% |
| action_is_effective | 87.9% |
| num_actions | 42.4 (接近 max 50) |
| validation time | 505.7s (~8.4 min) |

### Checkpoint

- `/root/autodl-tmp/checkpoints/exp026/` — **空目录**，尚未保存任何 checkpoint（step 1 还未完成）
- `/root/autodl-tmp/checkpoints/exp026_dryrun/` — dry run 的 checkpoint

### 服务器资源

| 资源 | 状态 |
|------|------|
| GPU 0 | 42720MiB/97887MiB, 100% util, 76°C |
| GPU 1 | 42680MiB/97887MiB, 100% util, 76°C |
| 磁盘 | 119GB 可用 (53%) |

### 速度估算

初始 validation（16 episodes）耗时 ~505s。训练 rollout 每 step 需处理 64 trajectories（4 groups × 16 size），每 trajectory 最多 50 turns，加上 step-independent 模式下每 turn 独立推理——预估每 step 需要 **30-60 分钟**。150 steps 总训练时间约 **75-150 小时**。

### 关注点

1. **训练速度极慢**：按当前速度，150 steps 需要 3-6 天。需要确认这个速度是否可接受。
2. **日志无训练指标**：step 1 尚未完成，无法判断 loss/gradient 趋势。建议等 step 1 完成后再评估。
3. **initial success 6.25%**：SFT 模型起点偏低，与 exp021 的 SFT 结果一致（此前 eval 也是 6.25%）。

### 建议

**继续等待**，不需要干预。进程正常运行中。建议 20-30 分钟后再检查日志是否有 step 1 的训练指标输出。如果 1 小时后日志仍无更新且 GPU 仍满载，可能需要排查是否 hang 在某处。

---
