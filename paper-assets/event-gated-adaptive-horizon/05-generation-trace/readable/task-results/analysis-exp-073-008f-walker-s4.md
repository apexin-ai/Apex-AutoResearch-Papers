# analysis exp 073 008f walker s4

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_073_008f_walker_s4_20260525T094942_result.json`
- **Structured JSON:** [`d39748cb60297efb7bfb.json`](../../sessions/d3/d39748cb60297efb7bfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

**exp_073_008f_walker_s4 → success（无 CIVO）**

| 指标 | 值 |
|------|-----|
| 最终 eval_return | 289.3 (step 105k) |
| 峰值 eval_return | **486.5** (step 75k) |
| 最大 ve_ratio | **0.5** (远低于 1.5x 阈值) |
| civo/alert | 0.0 (全程) |
| gate_dt_2_frac | 1.0 (固定 dt=2，符合预期) |
| 训练步数 | 112k env steps, 25k updates |

**CIVO 判定：No onset。** ve_ratio 始终 < 0.5，远低于 1.5x 阈值。符合 control 预期——移除 dt_embedding 后不触发 CIVO。

**008f 跨 seed 汇总：** s1=success (503), s2=negative (148), s4=success (peak 486.5)。2/3 seeds 验证了 control 假设。

Registry 已更新为 DONE/success，报告已注册为 artifact。

---
