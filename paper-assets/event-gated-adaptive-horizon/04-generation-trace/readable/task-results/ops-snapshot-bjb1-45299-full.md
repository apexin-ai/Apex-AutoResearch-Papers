# ops snapshot bjb1 45299 full

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_snapshot_bjb1_45299_full_20260520T161741_result.json`
- **Structured JSON:** [`d0938c72ad5e1e569840.json`](../../sessions/d0/d0938c72ad5e1e569840.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== exp_030b (Cheetah σ=0.5) ===
PID 903247: running (5h06m47s)
当前 step: 195K / 210K

eval_return 完整:
  5K=8.3, 15K=78.3, 25K=219.3, 35K=296.5, 45K=32.8, 55K=6.0,
  65K=71.2, 75K=23.3, 85K=34.0, 95K=143.6, 105K=104.4, 115K=137.7,
  125K=211.7, 135K=97.2, 145K=79.4, 155K=76.8, 165K=77.5, 175K=85.7,
  185K=68.7, 195K=77.6
  峰值 35K=296.5，之后崩塌，95K-125K 短暂回升，后期稳定在 ~77

ve_ratio 完整:
  15K=0.0202, 25K=0.0636, 35K=0.1238, 45K=1.9141, 55K=10.6657,
  65K=0.8371, 75K=1.9823, 85K=1.0946, 95K=0.2253, 105K=0.2686,
  115K=0.1789, 125K=0.1037, 135K=0.2153, 145K=0.2478, 155K=0.2392,
  165K=0.2020, 175K=0.1591, 185K=0.1834, 195K=0.1534
  45K-85K 有剧烈波动（与 eval_return 崩塌对应），后期稳定在 ~0.15-0.25

=== exp_031 (PickCube σ=0.2) ===
PID 908459: running (3h35m16s)
当前 step: 62.5K / 200K

eval_return 完整:
  2.5K=2.4, 12.5K=19.2, 22.5K=17.7, 32.5K=11.5, 42.5K=7.8,
  52.5K=4.8, 62.5K=10.4
  12.5K 峰值 19.2，之后持续下降，62.5K 微回升

ve_ratio 完整:
  12.5K=0.1989, 22.5K=1.0128, 32.5K=2.2946, 42.5K=3.0555,
  52.5K=3.7109, 62.5K=1.1999
  ve_ratio 持续上升至 52.5K=3.71 后回落，与 eval_return 下降趋势对应

=== GPU ===
cuda:0: 23% util, 3952/97887 MiB — PID 903247 (python, 3257 MiB)
cuda:1: 19% util, 2767/97887 MiB — PID 908464 (python, 2758+643+643 MiB)
```

---
