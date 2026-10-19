# monitor exp027 step3 check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp027_step3_check_20260515T184556_result.json`
- **Structured JSON:** [`4ac5043434a452e74ab5.json`](../../sessions/4a/4ac5043434a452e74ab5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp027 训练进度报告

### 进程状态
- **PID 789790** 存活，运行 **4h13m**
- 命令：`python train.py --config-name _alfworld_exp027_stable_grpo`

### 已完成 Steps

| 指标 | Step 0 (eval baseline) | Step 1 (train) | Step 2 (train) |
|------|----------------------|----------------|----------------|
| **success** | 6.25% | **35.94%** | 10.16% |
| **kl_loss** | — | 0.0576 | **0.4134** |
| **entropy** | — | 0.2753 | 0.3603 |
| **grad_norm** | — | 19.44 | 19.31 |
| **reward_mean** | — | 1.997 | 0.594 |
| **pass@16** | pass@1=6.25% | **100%** | 62.5% |
| batch_size | — | 5152 | 6144 |
| step耗时 | — | 72min | 98min |

### 当前状态
- **最新已完成 step：2**（train_total = 10229s ≈ 2h50m）
- Log 末尾停在 step 2 输出后，**step 3 正在进行中**（rollout 阶段）
- 按 step 耗时 72-98min 估算，step 3 预计 **~1-1.5h 后完成**

### Checkpoint
- `/root/autodl-tmp/checkpoints/exp027/` 目录为空 — save_freq=5，第一个 checkpoint 在 step 5

### 磁盘
- `/root/autodl-tmp`：250G 总量，108G 可用（57% 已用）

### 警告信号
**Step 2 指标显著恶化**：success 从 35.9% 骤降至 10.2%，KL loss 从 0.058 飙升至 0.413（7倍），reward_mean 从 2.0 降至 0.59，pass@16 从 100% 降至 62.5%。这可能预示策略不稳定，建议持续关注 step 3 指标是否回升。

---
