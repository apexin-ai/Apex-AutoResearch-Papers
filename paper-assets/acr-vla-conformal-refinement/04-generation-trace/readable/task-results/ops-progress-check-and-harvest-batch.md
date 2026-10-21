# ops progress check and harvest batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-and-harvest-batch_20260518T112416_result.json`
- **Structured JSON:** [`6de60685ed07273ba3ff.json`](../../sessions/6d/6de60685ed07273ba3ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 实验 1：K=5 seed43（bjb2-28827, cuda:2）
- **状态**: RUNNING
- **进度**: Task 9/10（chocolate_pudding），rollout 5/10
- 可见部分结果：bbq_sauce=30%, ketchup=10%, tomato_sauce=20%, butter=10%, milk=10%
- 预计还需 ~15 个 rollout（task 9 剩 5 个 + task 10 全部 10 个）

### 实验 2：random_selection seed42（bjb2-40593, cuda:0）
- **状态**: RUNNING
- **进度**: Task 10/10（orange_juice），rollout 5/10
- 只剩 5 个 rollout，马上完成
- 已完成 9 个 task：0%, 10%, 10%, 40%, 0%, 20%, 0%, 10%, 20%

### 实验 3：perdof default seed43（bjb1-18228, cuda:3）
- **状态**: RUNNING
- **进度**: Task 1/10（alphabet_soup），rollout 6/10
- 刚启动不久

### 实验 4：perdof default seed45（bjb1-32546, cuda:4）
- **状态**: RUNNING
- **进度**: Task 5/10（ketchup），rollout 5/10
- 前 4 个 task 全部 0% SR（符合 perdof default 预期）

### GPU 释放
- **bjb2-28827**: 6 个 PID 全部存活，0 GPU 释放
- **bjb2-40593**: PID 395256 存活，0 GPU 释放
- **bjb1-18228**: 4 个 PID 全部存活，0 GPU 释放
- **bjb1-32546**: 6 个 PID 全部存活，0 GPU 释放

**无任何 GPU 释放。** 实验 1 和 2 预计 10-20 分钟内完成，可以稍后再收割结果。

---
