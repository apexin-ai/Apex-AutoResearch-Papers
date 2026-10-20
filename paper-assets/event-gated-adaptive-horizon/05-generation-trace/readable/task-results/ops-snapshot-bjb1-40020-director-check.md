# ops snapshot bjb1 40020 director check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_snapshot_bjb1_40020_director_check_20260520T204413_result.json`
- **Structured JSON:** [`252b151f2159100004b2.json`](../../sessions/25/252b151f2159100004b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_029b: step=108K (eval@105K), eval=32.0, NVE=2.765@105K, value_mean=88.4, 进程=alive
  eval轨迹: 5K=30.5, 15K=168.4, 25K=159.6, 35K=168.1, 45K=171.5, 55K=177.7(peak), 65K=106.6, 75K=64.0, 85K=62.8, 95K=44.7, 105K=32.0
  NVE轨迹:  15K=0.030, 25K=0.174, 35K=0.335, 45K=0.477, 55K=0.583, 65K=1.014, 75K=1.650, 85K=1.623, 95K=2.109, 105K=2.765
  ⚠️ 持续崩溃: eval从55K的177.7单调下降到105K的32.0, NVE从65K突破1.0后持续飙升至2.765

exp_029d: step=36K (eval@35K), eval=190.8, NVE=0.312@35K, value_mean=59.6, 进程=alive
  eval轨迹: 5K=31.7, 15K=159.1, 25K=155.7, 35K=190.8
  NVE轨迹:  15K=0.021, 25K=0.171, 35K=0.312
  ✅ 健康上升中，NVE远低于危险阈值

GPU: cuda:0=13% (029d, 3043/24564 MiB), cuda:1=25% (029b, 3043/24564 MiB)
```

**关键发现**: exp_029b 情况恶化严重——eval从上次快照的64.0@75K进一步跌到32.0@105K，NVE从1.65飙到2.765，value_mean=88.4 远超实际 eval=32.0（value overestimation 严重）。该实验基本不可挽救，接近随机策略水平。exp_029d 进展正常，35K的190.8已超过029b的peak。

---
