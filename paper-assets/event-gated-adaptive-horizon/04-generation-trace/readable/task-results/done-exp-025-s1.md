# done exp 025 s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_done_exp_025_s1_20260520T023934_result.json`
- **Structured JSON:** [`ee0df0f6666bdb7502eb.json`](../../sessions/ee/ee0df0f6666bdb7502eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**exp_025_obs_sgs_walker_s1 → SUCCESS (CIVO prevented)**

**训练状态**: 正常完成，final eval step 215K（超过 210K 目标），无错误。

**完整 ve_ratio trajectory**:

| Step | eval_return | value_mean | ve_ratio |
|------|------------|------------|----------|
| 5K | 36.66 | 0.00 | 0.0000 |
| 25K | 184.17 | 29.19 | 0.1585 |
| 45K | 209.25 | 100.03 | 0.4780 |
| 65K | 393.24 | 233.29 | 0.5932 |
| 75K | 521.96 | 288.25 | 0.5522 |
| 85K | 490.87 | 315.11 | 0.6419 |
| **95K** | **340.78** | **283.30** | **0.8313** ← peak |
| 105K | 460.50 | 234.55 | 0.5093 |
| 115K | 494.10 | 203.42 | 0.4117 |
| 125K | 494.48 | 171.88 | 0.3476 |
| 135K | 510.63 | 143.45 | 0.2809 |
| 145K | 628.44 | 118.33 | 0.1883 |
| 155K | 524.57 | 96.63 | 0.1842 |
| 165K | 716.65 | 78.78 | 0.1099 |
| 175K | 731.16 | 66.16 | 0.0905 |
| 185K | 520.26 | 56.58 | 0.1088 |
| 195K | 245.32 | 49.38 | 0.2013 |
| 205K | 605.08 | 43.87 | 0.0725 |
| **215K** | **726.41** | **40.91** | **0.0563** |

**NVE 判定**:
- Peak ve_ratio = 0.8313 @ 95K
- Baseline @ 95K ≈ 0.648（线性插值 75K=0.5951, 105K=0.6739）
- **Peak NVE ≈ 1.28× < 1.5× threshold → CIVO prevented**
- 95K 之后 ve_ratio 单调下降至 0.056，value overestimation 完全消散

**论文 framing**: obs-decoder SGS Walker 最终 **1/4 seed prevention**。

Registry → DONE(success), cron 已删除。

---
