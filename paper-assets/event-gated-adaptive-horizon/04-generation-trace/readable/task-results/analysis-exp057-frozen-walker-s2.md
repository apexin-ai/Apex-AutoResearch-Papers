# analysis exp057 frozen walker s2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp057-frozen-walker-s2_20260524T164639_result.json`
- **Structured JSON:** [`8daebe6bfbd714f90817.json`](../../sessions/8d/8daebe6bfbd714f90817.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

```
exp_057 (s2): conclusion=success, eval_reward_peak=221.7 @195k, eval_reward_final=123.9 @215k, nve_peak=1.3 @115k
```

**3-seed 汇总:**

| Seed | Exp | NVE peak | CIVO | eval peak | 状态 |
|------|-----|----------|------|-----------|------|
| s0 | exp_042 | 0.19 | 无 | - | success |
| s1 | exp_047 | 1.71 | transient, 自愈 | - | success |
| s2 | exp_057 | 1.3 | transient (115k-145k), 自愈至0.2 | 221.7 | success |

**Frozen Walker 总结论: 稳健。** 0/3 持续 CIVO。2/3 有 transient NVE spike (>1.0) 但均自愈，无 civo_alert 触发。Frozen dt_emb 在 Walker 上不会导致持续性 value overestimation。

---
