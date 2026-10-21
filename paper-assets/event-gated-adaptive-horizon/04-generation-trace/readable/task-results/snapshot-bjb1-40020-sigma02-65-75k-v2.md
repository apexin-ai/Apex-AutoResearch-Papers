# snapshot bjb1 40020 sigma02 65 75K v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_snapshot_bjb1_40020_sigma02_65_75K_v2_20260520T082644_result.json`
- **Structured JSON:** [`f9b842ee25970229e0bc.json`](../../sessions/f9/f9b842ee25970229e0bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整。两块 4090 均在跑（GPU 0: 19%, 3.6GB; GPU 1: 16%, 2.5GB），进程存活。

---

## exp_027_tcn_walker_s0_sigma02

当前步数：**135K**（仍在训练，fps=7.6）

| Step | eval_return | ve_ratio (NVE) |
|-----:|------------:|---------------:|
| 5K   | 35.6        | —              |
| 15K  | 150.6       | 0.0            |
| 25K  | 199.4       | 0.1            |
| 35K  | 278.2       | 0.2            |
| 45K  | 315.6       | 0.3            |
| 55K  | 278.6       | 0.5            |
| 65K  | 331.0       | 0.6            |
| 75K  | 293.1       | 0.6            |
| 85K  | 363.9       | 0.5            |
| 95K  | 171.4       | 0.9            |
| 105K | 236.4       | 0.6            |
| 115K | **543.8**   | 0.2            |
| 125K | 458.4       | 0.2            |
| 135K | 496.7       | 0.2            |

---

## exp_028_rave_walker_s0_ceil15

当前步数：**~132K**（仍在训练，fps=7.8，最新 eval 在 125K）

| Step | eval_return | ve_ratio (NVE) |
|-----:|------------:|---------------:|
| 5K   | 31.6        | —              |
| 15K  | 99.4        | 0.0            |
| 25K  | 155.3       | 0.1            |
| 35K  | **180.1**   | 0.2            |
| 45K  | 166.9       | 0.4            |
| 55K  | 131.0       | 0.7            |
| 65K  | 91.5        | 1.3            |
| 75K  | 120.9       | 0.9            |
| 85K  | 137.3       | 0.7            |
| 95K  | 70.2        | 1.3            |
| 105K | 76.2        | 1.0            |
| 115K | 41.2        | 1.5            |
| 125K | 36.6        | 1.5            |

---

**关键发现：**
- **exp_027 (TCN)** 表现良好，115K 处 eval_return 达峰 543.8，之后稳定在 ~460-500 区间。ve_ratio 从 0.9 降回 0.2 并稳定。
- **exp_028 (RAVE)** 明显发散——eval_return 从 35K 峰值 180.1 持续下滑到 125K 的 36.6，ve_ratio 持续攀升到 1.5。
- 两个实验的 **gate_dt 完全锁死在 2.0**（dt_2_frac=100%），gate 机制未生效。

---
