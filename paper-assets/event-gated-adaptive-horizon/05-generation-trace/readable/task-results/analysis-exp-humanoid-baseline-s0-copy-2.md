# analysis exp humanoid baseline s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_humanoid_baseline_s0_20260529T043240_result.json`
- **Structured JSON:** [`da19fd64e21ec6d0049d.json`](../../sessions/da/da19fd64e21ec6d0049d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/negative。

## 结果摘要

**Conclusion: NEGATIVE** — 假设被证伪。

| 指标 | 值 |
|------|-----|
| eval_return (final) | 1.2 |
| NVE_105K | **13.0×** (阈值 2.0×) |
| NVE_peak | **13.0×** (at 105K) |
| NVE_final (205K) | **12.2×** |
| NVE_mean (≥35K) | **7.7×** |
| CIVO alerts | 3 次 (55K, 105K, 195K) |
| value_mean | 5.5 → 15.2 (持续膨胀) |

**关键发现**: Humanoid Walk 对 DreamerV3-S baseline 本身就是 CIVO-prone 环境，与 Walker/Cheetah baseline（NVE < 2.0×, 0 alerts）形成鲜明对比。21-DoF 高维动作空间在 eval_return 几乎无学习（~1.2）的情况下，value function 持续无界膨胀。这意味着 Humanoid 环境中即使 dt=1 也需要 CIVO 干预，使其成为验证 gating 机制的强压力测试环境。

---
