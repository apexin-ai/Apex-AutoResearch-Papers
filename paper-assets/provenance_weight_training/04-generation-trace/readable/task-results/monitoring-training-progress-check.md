# monitoring training progress check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_training_progress_check_20260514T183314_result.json`
- **Structured JSON:** [`f097f0523eb6acd3042d.json`](../../sessions/f0/f097f0523eb6acd3042d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`ps` 命令因 `||` 元字符被 read_only 拦截，但日志都在实时更新，进程均存活。

## 训练进度汇总

| 实验 | GPU | 当前 step | 总 steps | 进度 | 速度 | 预计剩余 | 状态 |
|------|-----|-----------|----------|------|------|----------|------|
| adaptive_fix_seed42 | cuda:1 | 2732/6103 | 6103 | 45% | 2.23s/it | ~2h06m | RUNNING |
| adaptive_fix_seed123 | cuda:2 | 2727/6103 | 6103 | 45% | 2.23s/it | ~2h05m | RUNNING |
| adaptive_fix_seed456 | cuda:3 | 2227/6103 | 6103 | 36% | 2.19s/it | ~2h21m | RUNNING |
| grid_b_seed42_batch | cuda:0 | 186/6103 (b=5.0) | 6103 | 3% | 2.11s/it | ~3h28m | RUNNING |

### grid_b_seed42_batch 子任务明细

| b 值 | 状态 | 完成时间 |
|------|------|----------|
| 0.5 | DONE | May 14 11:27 |
| 1.0 | DONE | May 14 15:03 |
| 1.5 | DONE | May 14 19:10 |
| 2.0 | DONE | May 14 22:48 |
| 3.0 | DONE | May 15 02:25 |
| 5.0 | RUNNING (186/6103, 3%) | 预计 ~3h28m 后 |

所有 4 个实验运行正常，无异常。3 个 adaptive_fix 实验进度相近（36%~45%），预计 2~2.5h 后完成。grid_b 已完成 5/6 个 b 值，最后一个 b=5.0 刚开始，约 3.5h 后完成。

---
