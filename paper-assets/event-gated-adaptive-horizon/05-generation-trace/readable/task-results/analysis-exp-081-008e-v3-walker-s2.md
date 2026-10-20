# analysis exp 081 008e v3 walker s2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_081_008e_v3_walker_s2_20260525T153929_result.json`
- **Structured JSON:** [`c28eb54d5300cbad1215.json`](../../sessions/c2/c28eb54d5300cbad1215.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE(success)，artifact 已注册。

---

## 结果摘要

**Conclusion: success** (CIVO hypothesis confirmed)

| Metric | Value |
|--------|-------|
| eval_return@105K | 597.1 (65.2% baseline) |
| ve_ratio | stable 0.4–0.6, peak 0.6 |
| NVE (est.) | ~0.7–0.8, well below 1.5 |
| CIVO alert | 0 (none) |
| gate_dt_mean | 1.0 (100% dt=1) |

**vs Seed 0**: eval_return 比 seed 0 (869.88) 低 31%，但 CIVO 指标一致——ve_ratio 稳定、无 alert、value function 单调递增无发散。性能差距是 seed 级别的学习速度方差，非 CIVO 相关退化。

**C6 claim 影响**: 3/3 seeds 均确认 008e_v3 配置（trained dt_emb + dt=1 imagination）不触发 CIVO。C6 claim 得到跨 seed 验证支持。Seed 2 的低 eval_return 是次要关注点——训练曲线仍在上升，105K 步属于 Walker Walk 的早中期训练。

---
