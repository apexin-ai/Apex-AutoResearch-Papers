# analysis exp 030c

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_030c_20260520T223021_result.json`
- **Structured JSON:** [`1baa474359e882fb8503.json`](../../sessions/1b/1baa474359e882fb8503.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部到手。以下是汇总报告。

---

## exp_030c 最终结果

- **最终 step**: 224K (train) / 215K (eval)，EXIT_CODE=0 正常退出
- **最终 eval_return**: **47.2** @215K
- **最终 NVE (ve_ratio)**: **0.3** @215K
- **eval_peak**: **371.7** @35K
- **NVE_max**: **0.4** @45K/75K/85K/95K

### eval_return 完整轨迹

| Step | eval_return | ve_ratio |
|------|------------|----------|
| 5K | 8.3 | — |
| 15K | 87.5 | 0.0 |
| 25K | 166.3 | 0.1 |
| 35K | **371.7** | 0.1 |
| 45K | 144.0 | 0.4 |
| 55K | 266.0 | 0.2 |
| 65K | 197.0 | 0.2 |
| 75K | 107.8 | 0.4 |
| 85K | 95.8 | 0.4 |
| 95K | 72.8 | 0.4 |
| 105K | 122.5 | 0.2 |
| 115K | 162.2 | 0.1 |
| 125K | 148.5 | 0.1 |
| 135K | 138.4 | 0.1 |
| 145K | 100.4 | 0.2 |
| 155K | 144.3 | 0.1 |
| 165K | 130.9 | 0.1 |
| 175K | 66.4 | 0.2 |
| 185K | 47.2 | 0.3 |
| 195K | 56.5 | 0.2 |
| 205K | 49.7 | 0.3 |
| 215K | 47.2 | 0.3 |

### Gate 状态
- gate_dt_mean=**2.0** 全程不变，gate_dt_2_frac=**1.0**，gate_entropy=**0.0**
- Gate 完全坍缩在 dt=2，TCN 从未激活 horizon 调整

### Cheetah 基线对比
- **Baseline eval (多 seed 平均)**: ~548 (last-5 mean), peak ~624-686
- exp_030c peak 371.7 = baseline 的 **67.8%**
- exp_030c final 47.2 = baseline 的 **8.6%**

### 结论: **negative**

σ=1.0 的高噪声完全抑制了 NVE 飙升（max 仅 0.4，远低于 CIVO 阈值），但代价是性能持续崩坏。35K 之后 eval 单调下行，175K 后跌至 ~50 区间再未恢复。Gate 全程锁死 dt=2，TCN 机制完全无效。

---

## Cheetah TCN 全系列对比 (exp_030a/b/c)

| 实验 | σ | eval_peak | peak_step | eval_final | NVE_max | NVE_max_step | 结论 |
|------|---|-----------|-----------|------------|---------|--------------|------|
| **030a** | 0.2 | 299.5 | 35K | ~32 (stopped@64K) | **1.90** | 55K | negative — NVE 突破致 crash |
| **030b** | 0.5 | 296.5 | 35K | 77.6 @195K | **10.67** | 55K | negative — 极端 NVE spike |
| **030c** | 1.0 | 371.7 | 35K | 47.2 @215K | **0.4** | 45K | negative — NVE 低但性能崩坏 |
| **Baseline** | — | 624-686 | 172-205K | ~548 avg | ~0.7-0.9 | — | success |

**规律**: 三个 σ 全部 negative。σ 越小 NVE 越容易爆（0.2→1.9, 0.5→10.7），σ 越大 NVE 被压平但 eval 也被压死。没有一个 σ 能同时抑制 CIVO 且保持性能。TCN 在 Cheetah 上全面失败，gate 始终锁 dt=2 从不自适应。

---
