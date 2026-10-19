# monitor hsweep h2 seed2 completion

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_hsweep_h2_seed2_completion_20260518T011331_result.json`
- **Structured JSON:** [`c465a772e0c17809ddf5.json`](../../sessions/c4/c465a772e0c17809ddf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### bjb1-17606: hsweep_h2_seed2 — 仍在运行

| 指标 | 值 |
|------|-----|
| PID | 945877, 运行 11h03m |
| 当前进度 | step 12/15 已完成，正在跑 step 13 |
| ADV log | 2600 行 |
| train success | 8.59% (step 12) |
| pass@8 | 31.25% |
| action_valid | 97.7% |
| entropy | 0.307 |
| kl_loss | 0.110 |
| 每步耗时 | ~2700-3000s (~45-50min) |
| **预计完成** | **~1.5-2h（剩余 step 13-15）** |

### westd-47453: gsweep watchdog + g050

| 指标 | 值 |
|------|-----|
| Watchdog PID | 259808, 运行 8h21m, **存活** |
| g050 PID | 85798, 运行 10h42m, **存活** |
| 最新 checkpoint | global_step_10 (07:19) |
| 当前进度 | step 10/15 刚完成（含 eval），正在跑 step 11 |
| **train success** | **0%（全程）** |
| action_valid | 21.5%（训练中），96.4%（eval 中） |
| manager_invalid_action | 78.3%（训练中） |
| val reward | 全部 0.0 |
| 每步耗时 | ~2300-6100s（eval 步更久） |
| **预计完成** | **~3-5h（剩余 step 11-15）** |

**g050 警告**：训练 success 全程 0%，manager_invalid_action 高达 78%，gamma=0.50 配置下模型似乎没有学到有效行为。eval 中 action_valid 恢复到 96% 但 reward 仍为 0，说明 eval 时行为格式正确但策略无效。g080 链式启动就绪（watchdog 存活），但 g050 结果本身可能没有分析价值。

---

两个实验均在运行中，hsweep_h2_seed2 后续任务（ADV 分析 + exp029 reeval）需等其完成后执行。

---
