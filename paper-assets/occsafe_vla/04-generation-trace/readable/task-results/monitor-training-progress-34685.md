# monitor training progress 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-34685_20260527T022000_result.json`
- **Structured JSON:** [`7aac7f5fb30df7bbd982.json`](../../sessions/7a/7aac7f5fb30df7bbd982.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

## 训练进度汇总 (westd-34685)

| exp_id | 当前 step | max_steps | 进度% | 最新 loss (action / occ) | 速度 | 预计完成 (UTC) |
|--------|-----------|-----------|-------|--------------------------|------|---------------|
| detach_ln_v2_s1_35 | ~10400 | 50005 | 20.8% | 0.1338 / 0.0126 | 1.07 it/s | May 27 ~12:50 |
| detach_ln_s4 | ~10441 | 50005 | 20.9% | 0.1621 / 0.0109 | 1.08 it/s | May 27 ~12:50 |
| ablation_occ_detach_s4 | ~7630 | 50005 | 15.3% | 0.1455 / 0.0101 | 1.08 it/s | May 27 ~13:40 |
| mvp_occ_s4 | ~7610 | 50005 | 15.2% | 0.1514 / 0.0138 | 1.07 it/s | May 27 ~13:40 |

## Checkpoint 情况

| exp_id | 已保存 checkpoint |
|--------|-------------------|
| detach_ln_v2_s1_35 | 10000_chkpt (May 27 10:14) |
| detach_ln_s4 | 10000_chkpt (May 27 10:12) |
| ablation_occ_detach_s4 | 无（尚未到 10k） |
| mvp_occ_s4 | 无（尚未到 10k） |

## 进程状态

4 个进程均存活。PID 681204 (detach_ln_v2_s1) CPU 592%，正常。其余 3 个 PID 瞬时 CPU 0.0%（GPU-bound 训练的正常快照现象，日志持续推进，无异常）。

## 异常检查

- **Loss 收敛正常**：所有实验 action_loss 从 ~0.65 降至 0.13-0.16，occ_loss 从 ~0.19 降至 0.01，趋势健康
- **无磁盘问题**：checkpoint 正常保存
- **DDL 风险**：4 个实验预计 May 27 13:00-14:00 UTC 完成，距 May 28 12:00 UTC 截止还有 ~22h 余量，**无风险**

---
