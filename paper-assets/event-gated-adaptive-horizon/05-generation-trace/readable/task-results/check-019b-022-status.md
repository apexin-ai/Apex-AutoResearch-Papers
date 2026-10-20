# check 019b 022 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_019b-022-status_20260517T103915_result.json`
- **Structured JSON:** [`d96d90c30f557ebe3758.json`](../../sessions/d9/d96d90c30f557ebe3758.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== exp_019b ==
Current step: ~135600/200000 (67.8%)
Latest eval checkpoint: step 132500

New checkpoints since 72.5K:
  step=82500   eval=5.713   value=8.590   ve=1.503   NVE=0.779 (baseline_ve=1.929)
  step=92500   eval=4.973   value=6.572   ve=1.322   NVE=0.677 (baseline_ve=1.953)
  step=102500  eval=8.362   value=5.539   ve=0.662   NVE=0.186 (baseline_ve=3.556)
  step=112500  eval=9.031   value=4.976   ve=0.551   (no baseline)
  step=122500  eval=13.571  value=4.953   ve=0.365   (no baseline)
  step=132500  eval=26.873  value=4.355   ve=0.162   (no baseline)

趋势: eval_return 在 102.5K 后持续上升（8.4→9.0→13.6→26.9），132.5K 创新高。
V/E ratio 持续下降（value_mean 稳定在 4-5 区间，eval 快速增长），value function 严重低估实际回报。
Gate 始终锁定 dt=2（gate_dt_2_frac=1.0, entropy=0）。

== exp_022 ==
Current step: ~108000/105000 (已超过预设终点，仍在运行)
Latest eval: step 105000, eval_return=189.109
Gate status: gate_dt_1_frac=1.0, gate_entropy=0.0, gate_dt_mean=1.0
Gate active: NO — 完全锁死在 dt=1，entropy=0，gate_scale 刚开始升到 0.00626

eval_return 趋势: 75K=573.8 → 85K=176.2 → 95K=195.4 → 105K=189.1
从 75K 的峰值 573.8 大幅跌落后在 ~190 附近企稳，gate 未起任何作用。

== GPU status ==
GPU 0: RTX PRO 6000, 37°C, 132W/600W, 3435MiB/97887MiB, 28% util
  - PID 649577 (exp_019b): 2849MiB
GPU 1: RTX PRO 6000, 42°C, 119W/600W, 3284MiB/97887MiB, 20% util
  - PID 661600 (exp_022): 3265MiB
两个实验均正常运行。
```

---
