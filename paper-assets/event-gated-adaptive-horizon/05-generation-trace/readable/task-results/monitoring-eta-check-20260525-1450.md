# monitoring eta check 20260525 1450

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_eta_check_20260525_1450_20260525T145511_result.json`
- **Structured JSON:** [`06fcfba240e49c478cb7.json`](../../sessions/06/06fcfba240e49c478cb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验进程存活。

| exp_id | step | target | progress | FPS | eval_return | 剩余时间 |
|--------|------|--------|----------|-----|-------------|----------|
| exp_080 (walker_s1) | 92K | 105K | 87.6% | 7.0 | 803.8 @85K | ~31 min |
| exp_081 (walker_s2) | 92K | 105K | 87.6% | 9.0 | 449.0 @85K | ~24 min |
| exp_082 (cheetah_no_dt_emb_s0) | 40K | 105K | 38.1% | 14.4 | 119.4 @35K | ~75 min |
| exp_083 (cheetah_baseline_s1) | 28K | 105K | 26.7% | 15.9 | 300.2 @25K | ~81 min |

进度对比上次（~15 min 前）：exp_080 84K→92K (+8K), exp_081 80K→92K (+12K), exp_082 25K→40K (+15K), exp_083 8K→28K (+20K)。

bjb1 上两个 walker 实验约半小时内完成；westd 上两个 cheetah 实验还需 ~1.5 小时。

---
