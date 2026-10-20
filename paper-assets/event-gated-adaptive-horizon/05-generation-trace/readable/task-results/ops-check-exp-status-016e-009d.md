# ops check exp status 016e 009d

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp-status-016e-009d_20260515T221455_result.json`
- **Structured JSON:** [`9d8088b52b7ed4163f46.json`](../../sessions/9d/9d8088b52b7ed4163f46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_016e_sgs_walker_s1 (PID 527392)
- 进程状态: **ALIVE** (运行 9498s ≈ 2.6h)
- 当前 step: **92000** / 105000 (87.6%)，train_return = 75.1
- eval_return:
  - step 5000: 31.0
  - step 15000: 140.3
  - step 25000: 141.8
  - step 35000: 173.0
  - step 45000: 184.0
  - step 55000: 153.8
  - step 65000: 324.3
  - step 75000: 326.7
  - step 85000: 256.2
- GPU 显存: 3259 MiB

## exp_009d_baseline_walker_s0 (PID 149708)
- 进程状态: **ALIVE** (运行 35417s ≈ 9.8h)
- 当前 step: **224000** / 500000 (44.8%)，train_return = 658.4
- eval_return (最近 20):
  - step 5000: 35.0 → step 38000: 264.0 → step 68000: 402.2 → step 88000: 440.3 → step 118000: 480.6 → step 138000: 495.5 → step 148000: 504.3 → step 178000: 511.6 → step 198000: 558.7 → step 208000: 591.3 → **step 218000: 638.2**
- GPU 显存: 4156 MiB

## GPU 状态
- GPU 0: 4165 MiB, utilization 31% (009d)
- GPU 1: 3278 MiB, utilization 24% (016e)

**结论：两个实验都在正常运行，不是 cron 回调丢失——实验尚未完成。** 016e 预计还需 ~30min 完成剩余 13000 steps；009d 还剩 276000 steps，预计还需 ~10h。

---
