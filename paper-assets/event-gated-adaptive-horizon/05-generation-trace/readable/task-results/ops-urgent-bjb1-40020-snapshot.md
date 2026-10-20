# ops urgent bjb1 40020 snapshot

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_bjb1_40020_snapshot_20260520T165017_result.json`
- **Structured JSON:** [`477912f8a68f53901118.json`](../../sessions/47/477912f8a68f53901118.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== exp_029c (σ=0.1) ===
PID 59395: RUNNING (Ss+, elapsed 05:07:50)
当前 step: 145K
FPS: ~7.9

eval_return:
  5K:  35.6    45K: 160.9    85K: 220.8   125K: 232.3
  15K:  99.1    55K: 254.8    95K: 188.6   135K: 247.4
  25K: 140.7    65K: 268.7   105K: 204.7   145K: 323.1 ← new peak
  35K: 155.7    75K: 295.5   115K: 296.4

ve_ratio:
  15K: 0.0306   55K: 0.4368   95K: 1.0218  135K: 0.3995
  25K: 0.1606   65K: 0.5432  105K: 0.7610  145K: 0.2667
  35K: 0.3162   75K: 0.6211  115K: 0.4514
  45K: 0.4807   85K: 0.9533  125K: 0.4899

⚠️ gate_dt 锁死在 2（gate_dt_2_frac=1.0 全程，empirical_entropy=0.0）

=== exp_029a ===
PID 50924: EXITED confirmed

=== GPU ===
cuda:0: 21% util, 3043/24564 MiB (PID 59400 python 3025 MiB)
cuda:1:  0% util,    1/24564 MiB (idle)
```

趋势：eval_return 在 145K 达到新高 323.1，但 ve_ratio 从 95K 峰值 1.02 持续回落到 0.27，gate 完全没有探索（全程 dt=2）。

---
