# ops fix data path bjb1 40020

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_data_path_bjb1_40020_20260520T082801_result.json`
- **Structured JSON:** [`e023b30cccf058a56799.json`](../../sessions/e0/e023b30cccf058a56799.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据拿到了。

## Metrics 文件正确路径

| 实验 | 路径 |
|------|------|
| exp_027 (TCN σ=0.2) | `/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/metrics.jsonl` |
| exp_028 (RAVE ceil15) | `/root/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/metrics.jsonl` |

之前找不到是因为实际 logdir 在 `/root/runs/event-gated-adaptive-horizon/`，不是 `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/`。

## exp_027 — TCN σ=0.2 Walker（当前 135K 步）

| Step | eval_return | ve_ratio (NVE) |
|------|-------------|----------------|
| 5K   | 35.6        | —              |
| 15K  | 150.6       | 0.0192         |
| 25K  | 199.4       | 0.0961         |
| 35K  | 278.2       | 0.1875         |
| 45K  | 315.6       | 0.3009         |
| 55K  | 278.6       | 0.5231         |
| 65K  | 331.0       | 0.5654         |
| 75K  | 293.1       | 0.6110         |
| 85K  | 363.9       | 0.4665         |
| 95K  | 171.4       | 0.9081         |
| 105K | 236.4       | 0.5625         |
| 115K | **543.8**   | 0.2105         |
| 125K | 458.4       | 0.2182         |
| 135K | 496.7       | 0.1764         |

## exp_028 — RAVE ceil15 Walker（当前 135K 步）

| Step | eval_return | ve_ratio (NVE) |
|------|-------------|----------------|
| 5K   | 31.6        | —              |
| 15K  | 99.4        | 0.0300         |
| 25K  | 155.3       | 0.1278         |
| 35K  | **180.1**   | 0.2465         |
| 45K  | 166.9       | 0.4280         |
| 55K  | 131.0       | 0.7369         |
| 65K  | 91.5        | 1.2943         |
| 75K  | 120.9       | 0.9371         |
| 85K  | 137.3       | 0.7267         |
| 95K  | 70.2        | 1.2799         |
| 105K | 76.2        | 0.9841         |
| 115K | 41.2        | 1.5129         |
| 125K | 36.6        | 1.4624         |
| 135K | 39.1        | 1.1708         |

**关键观察：**
- **TCN σ=0.2** 表现良好：eval_return 在 115K 后突破 ~500，ve_ratio 从高点 0.91 回落到 0.18，gate 完全锁在 dt=2（无自适应）
- **RAVE ceil15** 严重崩溃：eval_return 从 35K 峰值 180 持续下降到 135K 的 39，ve_ratio 飙升到 1.5+，训练已发散

---
