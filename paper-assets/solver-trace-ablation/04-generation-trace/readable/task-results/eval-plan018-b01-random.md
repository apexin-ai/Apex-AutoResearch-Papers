# eval plan018 b01 random

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan018-b01-random_20260514T081242_result.json`
- **Structured JSON:** [`277bf21e2b837980ac09.json`](../../sessions/27/277bf21e2b837980ac09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。

## 结果总结

### plan018-additive-random-b01-s42 eval 结果

| 指标 | plan018 (random β=0.1) | plan002-b01 (ISR β=0.1) | 差异 |
|------|----------------------|------------------------|------|
| **eval PR** | 0.79 | 0.81 | ≈持平 (Δ=0.02) |
| **eval Mean ISR** | 0.104 | 0.337 | **ISR 3.2x higher** |
| **eval Proved-only ISR** | 0.131 | 0.415 | **ISR 3.2x higher** |
| **eval Median ISR** | 0.036 | — | — |
| **Component count** | 8.46 | 5.58 | random组更冗余 |
| **ISR=0 占比 (proved)** | 36.7% | — | random组大量无结构proof |
| **Tautological collapse** | 无 | 无 | — |

### Conclusion: **negative**

PR 几乎相同说明 β=0.1 random 噪声不影响证明能力。但 ISR 差 3.2 倍，**强力支持 Claim 2**：ISR reward 在低剂量下提供 genuine structural guidance，而非仅 variance regularization。

---
