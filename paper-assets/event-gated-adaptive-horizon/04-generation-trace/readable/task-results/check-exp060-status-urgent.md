# check exp060 status urgent

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp060-status-urgent_20260525T012253_result.json`
- **Structured JSON:** [`4c28469d496e9e5b2f32.json`](../../sessions/4c/4c28469d496e9e5b2f32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### exp_060 (Cartpole baseline) — **已完成** ✓
- bjb1-45299 cuda:0 已空闲（0% util, 526 MiB, 无进程）
- 日志以 `=== seed 2 done === EXIT_CODE=0` 结束
- 3 seeds 全部跑完 112K steps：

| seed | step | train_return | 最后 eval_return (105K) |
|------|------|-------------|----------------------|
| 0 | 112000 | 809.4 | — |
| 1 | 112000 | 684.4 | — |
| 2 | 112000 | 526.1 | 557.0 (log) |

### exp_061 (Cartpole CIVO trigger) — **运行中, seed 2**
- bjb1-45299 cuda:1, 31% util, 2751 MiB, PID 243208
- seed 0/1 已完成 (112K)，seed 2 在跑

| seed | step | train_return | 状态 |
|------|------|-------------|------|
| 0 | 112000 | 199.2 | done |
| 1 | 112000 | 188.7 | done |
| 2 | 88000 | 222.7 | **running (78%)** |

- 最后 eval (85K): eval_return=216.5
- fps≈11, 剩余 24K steps → **预计 ~36 分钟完成**

### exp_062 (Cartpole control) — **运行中, seed 2**
- bjb1-40020 cuda:0, PID 491125, 3023 MiB

| seed | step | train_return | 状态 |
|------|------|-------------|------|
| 0 | 112000 | 224.0 | done |
| 1 | 112000 | 251.8 | done |
| 2 | 55000 | (55K metrics) | **running (49%)** |

- 最后 eval (55K): eval_return=217.4
- fps≈8, 剩余 57K steps → **预计 ~2 小时完成**

### exp_066 (timeseries RSSM fidelity) — **运行中**
- bjb1-40020 cuda:1, PID 490622, 2514 MiB
- 当前 step 55K, 正在执行 evaluation
- 日志末尾 train_return: 143~246 (52K)

**关键发现**: exp_060 已正常完成，cuda:0 on bjb1-45299 可用于新任务。exp_061/062 的 gate 全锁在 dt=2（gate_dt_2_frac=1.0），gate 没有学到变化。

---
