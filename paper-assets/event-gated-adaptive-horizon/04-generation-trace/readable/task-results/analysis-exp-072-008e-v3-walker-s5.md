# analysis exp 072 008e v3 walker s5

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_072_008e_v3_walker_s5_20260525T095006_result.json`
- **Structured JSON:** [`19fd84c0a0fc098ef01d.json`](../../sessions/19/19fd84c0a0fc098ef01d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_072_008e_v3_walker_s5 分析完成

**结论：SUCCESS**

| 指标 | 值 |
|------|-----|
| final eval_return | **853.1** @ 105K (93.2% of baseline) |
| peak eval | 853.1 @ 105K (仍在上升) |
| final NVE | 0.61x (远低于 1.5x CIVO 阈值) |
| civo/alert | 0.0 全程 |
| gate_dt_1_frac | 1.0 |
| actor_entropy | -5.1 |

eval 轨迹单调上升（仅 85K 微幅回落 710→728 后恢复），NVE 从 0→0.61x 平稳增长，无任何 collapse 迹象。表现与 s1 (869.9) 接近，且 NVE 更健康（0.61x vs 0.80x）。

**008e_v3 collapse rate 更新：2/5 = 40%**（s1=SUCCESS, s5=SUCCESS, s2=NEGATIVE/CIVO, s0=NEGATIVE/non-CIVO）

---
