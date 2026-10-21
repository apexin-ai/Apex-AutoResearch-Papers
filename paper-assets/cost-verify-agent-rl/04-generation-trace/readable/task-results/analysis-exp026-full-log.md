# analysis exp026 full log

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp026_full_log_20260515T125106_result.json`
- **Structured JSON:** [`41de5e851bb2fd79bdfa.json`](../../sessions/41/41de5e851bb2fd79bdfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整分析报告：

---

## exp026_step_independent_grpo 训练日志分析

### 进程状态：**仍在运行**（未崩溃）

PID 778562（启动脚本）和 781795（Ray TaskRunner）均存活。cron 检测到的"进程死亡"可能是监控了错误的 PID 或 shell wrapper 退出。

### 训练完成步数：2 步（正在执行 step 3）

| Step | 类型 | success | action_is_valid | entropy | pg_loss | kl_loss | ppo_kl | grad_norm | pass@16 |
|------|------|---------|-----------------|---------|---------|---------|--------|-----------|---------|
| 0 | val | 6.25% | 63.13% | - | - | - | - | - | - |
| 1 | train | 21.88% | 68.65% | 0.267 | 0.00732 | 0.180 | 0.0670 | 14.43 | 100% |
| 2 | train | 32.81% | 60.35% | 0.317 | 0.00571 | 0.0974 | 0.0267 | 15.62 | 100% |

### 关键指标趋势
- **success_rate**: 6.25% → 21.88% → 32.81%（强劲上升）
- **entropy**: 0.267 → 0.317（略增，健康）
- **kl_loss**: 0.180 → 0.0974（下降，策略在收敛）
- **grad_norm**: 14.43 → 15.62（稳定）
- **pass@16**: 训练集达到 100%

### Step timing
- Step 1: 2278s（~38min）
- Step 2: 2561s（~42.7min）
- 预估 150 steps 完成时间: ~100 小时

### 配置关键参数
- `test_freq: 5` — 下次 val eval 在 step 5
- `save_freq: 25` — 首个 checkpoint 在 step 25
- `total_training_steps: 150`
- `val_before_train: true`

### Checkpoint
- `/root/autodl-tmp/checkpoints/exp026/` — **空目录**（save_freq=25，未到保存点）

### W&B
- 配置了 `logger: ['console', 'wandb']`，但日志中**未找到 wandb run URL**，wandb 目录不存在。可能初始化静默失败。

### 崩溃原因
- **没有崩溃。** 进程仍在运行，无 Traceback、无 OOM、无 Error。
- 磁盘正常：`/root/autodl-tmp/` 114GB 可用 (55%)，根分区 16GB 可用 (50%)

### 日志文件
- 启动脚本日志: `/root/runs/cost-verify-agent-rl/exp026_step_independent_grpo.log`（9746 行，最后修改 20:21:39）
- **Ray worker 日志（主要指标来源）**: `/root/autodl-tmp/tmp/ray/session_2026-05-15_18-38-45_487055_778562/logs/worker-f5a9c771de63c207b8db019edc7dedd89a425c2fe97314a2669cdd43-01000000-781795.out`（1496 行，最后修改 20:32:20）

### 注意事项
1. cron 应监控 PID 781795（TaskRunner）而非 778562（shell wrapper）
2. 启动脚本日志 80% 是 `anchor_obs` 警告，真正的 step 指标只在 Ray worker 日志
3. 每步 ~40min，预计 step 5 的首次 val eval 还需约 2 小时

---
