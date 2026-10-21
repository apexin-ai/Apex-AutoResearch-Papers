# analysis exp 066 timeseries rssm fidelity

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_066_timeseries_rssm_fidelity_20260525T023004_result.json`
- **Structured JSON:** [`6a01a9089ca9f1883862.json`](../../sessions/6a/6a01a9089ca9f1883862.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_066 分析结果

**结论: SUCCESS** — 假设成立。

### 关键发现

| 指标 | 早期 (10K) | 中期 (30K) | 末期 (65K) |
|------|-----------|-----------|-----------|
| SS fidelity ratio (dt2/dt1) | 1.05 | 1.25 | **1.68** |
| OL fidelity ratio | 0.94 | 1.45 | 1.38 |
| VE ratio | 0.005 | 0.22 | **1.40** |

### 时序因果链

- **Fidelity gap onset**: step 20K（SS ratio > 1.1）
- **VE onset**: step 30K（VE ratio > 0.2）
- → Fidelity gap **领先** VE ~10K steps

### 机制

dt=1 MAE 持续改善（0.090→0.050），而 dt=2 MAE 平台化（0.094→0.084）。差距来源于 dt=1 的 RSSM 持续学习进步，但 dt=2 由于 trained dt_embedding 引入的表征偏差无法同步改善。这个 fidelity gap 通过 imagination rollout 累积，导致 value estimate 系统性偏高。

### 统计

- Pearson(SS_ratio, VE_ratio) = **0.807** (p=0.0015)
- SS_ratio 单调性: 73%（8/11 递增）
- 交叉相关峰值 lag=0（同步或 SS 略领先）

图表和详细数据已保存到服务器 `logdir/exp_066_timeseries_rssm_fidelity_s0/exp_066_timeseries_fidelity_causal.png` 和 registry artifacts。

---
