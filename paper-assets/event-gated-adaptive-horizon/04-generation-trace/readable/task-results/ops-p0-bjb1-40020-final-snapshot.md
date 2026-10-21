# ops p0 bjb1 40020 final snapshot

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0_bjb1_40020_final_snapshot_20260520T114428_result.json`
- **Structured JSON:** [`131196c8e44bd2b697cd.json`](../../sessions/13/131196c8e44bd2b697cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. exp_029c 刚启动，还没有 ve_ratio 数据。

```
=== exp_027_tcn_walker_s0_sigma02 (FINAL) ===
进程状态: EXITED (PID 37863)
总步数: 215,000

eval_return 完整轨迹 (22 points):
  5K=35.6, 15K=150.6, 25K=199.4, 35K=278.2, 45K=315.6, 55K=278.6,
  65K=331.0, 75K=293.1, 85K=363.9, 95K=171.4, 105K=236.4, 115K=543.8,
  125K=458.4, 135K=496.7, 145K=542.7, 155K=660.5, 165K=653.3, 175K=821.1,
  185K=560.5, 195K=567.9, 205K=558.7, 215K=551.0

ve_ratio 完整轨迹 (21 points):
  15K=0.0192, 25K=0.0961, 35K=0.1875, 45K=0.3009, 55K=0.5231,
  65K=0.5654, 75K=0.6110, 85K=0.4665, 95K=0.9081, 105K=0.5625,
  115K=0.2105, 125K=0.2182, 135K=0.1764, 145K=0.1430, 155K=0.1060,
  165K=0.0979, 175K=0.0729, 185K=0.1048, 195K=0.1026, 205K=0.0995,
  215K=0.0955

汇总:
  eval_peak     = 821.1 @ 175K
  eval_last10_mean = 587.1 (steps 125K–215K)
  nve_max       = 0.9081 @ 95K
  nve_final     = 0.0955
  total_steps   = 215,000

checkpoint_path: /root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt
log_path: /root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log

=== exp_029c (Walker σ=0.1) ===
PID: 59395, 状态: RUNNING (elapsed 00:01:52)
GPU 0 占用: PID 59400, 3023 MiB
当前进度: step=5K, eval_return=35.6 (刚启动，尚无 ve_ratio)

=== exp_029a (σ=0.2 s1) ===
PID: 50924, 状态: RUNNING (elapsed 03:12:05)
最新 step: 85K

eval_return 最新 5 点:
  45K=124.2, 55K=133.9, 65K=169.7, 75K=171.2, 85K=151.8

ve_ratio 最新 5 点:
  45K=0.5147, 55K=0.6428, 65K=0.4777, 75K=0.3980, 85K=0.4033

全部 eval_return (9 points):
  5K=36.7, 15K=137.7, 25K=180.9, 35K=124.0, 45K=124.2,
  55K=133.9, 65K=169.7, 75K=171.2, 85K=151.8
```

---
