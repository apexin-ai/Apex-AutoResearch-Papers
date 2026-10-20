# check exp progress 071 072 073

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp-progress-071-072-073_20260525T090824_result.json`
- **Structured JSON:** [`52481bf500ace043146b.json`](../../sessions/52/52481bf500ace043146b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前时间 17:08，三个实验均存活：

| exp_id | PID alive | current_step/105000 | GPU util% | 预计完成时间 |
|--------|-----------|--------------------:|----------:|-------------|
| exp_071_008f_walker_s3 (bjb1, cuda:1) | Yes (2h04m) | 80000/105000 (76%) | 23% | ~17:47 (~39min) |
| exp_072_008e_v3_walker_s5 (westd, cuda:1) | Yes (1h44m) | 85000/105000 (81%) | 44% | ~17:33 (~25min) |
| exp_073_008f_walker_s4 (westd, cuda:0) | Yes (1h37m) | 84000/105000 (80%) | 29% | ~17:33 (~25min) |

**估算方法**：elapsed time / current_step × remaining_steps。

exp_071 速度较慢（GPU 利用率低），约 645 steps/min；westd 两个实验约 820-860 steps/min。三个实验预计均在 30-40 分钟内完成。

---
