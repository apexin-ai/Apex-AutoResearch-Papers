# analysis exp 070 008e v3 walker s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_070_008e_v3_walker_s0_20260525T085136_result.json`
- **Structured JSON:** [`cfc8ee5300c3e1d1ca38.json`](../../sessions/cf/cfc8ee5300c3e1d1ca38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

**exp_070_008e_v3_walker_s0: NEGATIVE（非 CIVO 学习失败）**

- eval_return = 148 @105K（峰值 232.5 @55K），远低于 baseline ~500+
- ve_ratio = 0.8，全程 < 1.5x，**无 CIVO**
- 这是第三种失败模式：agent 从未学会走路，但 value function 没有过估——与 s2/s3 的 CIVO 崩塌（NVE >3.7x, eval 先到 500-700+ 再崩）完全不同

**008e_v3 跨 seed 汇总（5 completed / 1 running）：**

| 类别 | Seeds | 比例 |
|------|-------|------|
| Success | s1 (870), s4 (899) | 2/5 = 40% |
| CIVO collapse | s2 (137, NVE=3.78), s3 (93, NVE=4.02) | 2/5 = 40% |
| Non-CIVO failure | **s0 (148, NVE=0.8)** | 1/5 = 20% |

- CIVO collapse rate: 50% → **40%**（加入 s0 后下降）
- Overall failure rate: 50% → **60%**（加入 s0 后上升）
- s5 (exp_072) 仍在 running，完成后更新至 n=6

---
