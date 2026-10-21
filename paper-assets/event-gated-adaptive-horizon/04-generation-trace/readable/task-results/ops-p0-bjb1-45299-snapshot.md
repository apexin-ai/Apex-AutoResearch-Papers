# ops p0 bjb1 45299 snapshot

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0_bjb1_45299_snapshot_20260520T114438_result.json`
- **Structured JSON:** [`1d9aebab718f3dca04ae.json`](../../sessions/1d/1d9aebab718f3dca04ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== exp_027_tcn_walker_s1 (σ=0.5 s1) ===
PID: 888926, 状态: running (cuda:1)
当前 step: ~195K / 210K

eval_return 完整轨迹:
  5K=31.0, 15K=140.5, 25K=163.6, 35K=153.0, 45K=136.8, 55K=158.3,
  65K=298.5, 75K=364.9, 85K=134.0, 95K=94.6, 105K=216.7, 115K=318.9,
  125K=309.1, 135K=216.1, 145K=175.4, 155K=171.0, 165K=209.5, 175K=120.4,
  185K=355.4, 195K=183.3

ve_ratio 完整轨迹:
  15K=0.025, 25K=0.142, 35K=0.359, 45K=0.610, 55K=0.709, 65K=0.488,
  75K=0.490, 85K=1.410, 95K=1.637, 105K=0.644, 115K=0.402, 125K=0.380,
  135K=0.508, 145K=0.847, 155K=0.857, 165K=0.539, 175K=0.735, 185K=0.211,
  195K=0.351

汇总: eval_peak=364.9@75K, ve_ratio_max=1.637@95K
注意: gate_dt 全程锁定在 2.0 (dt_2_frac=100%, entropy=0.0)

=== exp_030b_tcn_cheetah_s0_sigma05 (Cheetah σ=0.5) ===
PID: 903247, 状态: running (cuda:0)
当前 step: ~15K / 210K (刚启动不久)

eval_return: 5K=8.3, 15K=78.3
ve_ratio: 15K=0.020
gate_dt: 锁定 2.0 (dt_2_frac=100%)

=== GPU ===
cuda:0: 21% util, 3801 / 97887 MiB  ← PID 903247 (exp_030b, 3257 MiB)
cuda:1: 23% util, 2753 / 97887 MiB  ← PID 888926 (exp_027, 2744 MiB)
```

---
