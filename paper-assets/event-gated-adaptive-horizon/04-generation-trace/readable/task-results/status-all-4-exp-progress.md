# status all 4 exp progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_all-4-exp-progress_20260522T054357_result.json`
- **Structured JSON:** [`4baa7e80cbc0656a87f5.json`](../../sessions/4b/4baa7e80cbc0656a87f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 服务器 1: bjb1-45299

```
=== PID CHECK ===
 52397    02:43:18 1167 3315512
PID_52397_ALIVE
 51103    03:06:06 1204 3450184
PID_51103_ALIVE
=== GPU ===
0, 29 %, 4067 MiB
1, 21 %, 3017 MiB
=== EXP_040 ===
step: 95000 (最新训练指标), step: 96000 (train_return: 85.29, 53.58, 86.65, 65.71)
=== EXP_040 EVAL ===
step 75000: eval_return=40.08
step 85000: eval_return=68.08
step 95000: eval_return=149.89
=== EXP_040 NVE ===
step 75000: ve_ratio=0.468
step 85000: ve_ratio=0.107 (输出被截断)
step 95000: ve_ratio=0.107
=== EXP_041 ===
step: 95000 (训练指标), step: 105000 (ve_ratio=0.265)
=== EXP_041 EVAL ===
step 85000: eval_return=254.73
step 95000: eval_return=266.05
step 105000: (被截断)
=== EXP_041 NVE ===
step 95000: ve_ratio=0.564
step 105000: ve_ratio=0.265
```

### 服务器 2: bjb1-40020

```
=== PID CHECK ===
251336    03:05:59  608 2944580
PID_251336_ALIVE
250627    03:08:06  616 2824508
PID_250627_ALIVE
=== GPU ===
0, 11 %, 3564 MiB
1, 17 %, 2523 MiB
=== EXP_042 ===
step: 85000 (ve_ratio=0.112), step: 88000 (train_return: 334.33, 438.32, 420.76, 327.28)
=== EXP_042 EVAL ===
step 65000: eval_return=413.47
step 75000: eval_return=453.54
step 85000: eval_return=378.30
=== EXP_042 NVE ===
step 65000: ve_ratio=0.100
step 75000: ve_ratio=0.112 (被截断)
step 85000: ve_ratio=0.112
=== EXP_043 ===
step: 85000, step: 88000 (train_return 被截断)
=== EXP_043 EVAL ===
step 65000: eval_return=143.79
step 75000: eval_return=175.11 (被截断)
step 85000: (被截断)
=== EXP_043 NVE ===
step 65000: ve_ratio=0.258
step 75000: ve_ratio=0.235
step 85000: ve_ratio=0.308
```

4 个进程全部存活，GPU 正常使用中。输出因长度被截断了部分内容——如需完整数据可单独查询某个实验。

---
