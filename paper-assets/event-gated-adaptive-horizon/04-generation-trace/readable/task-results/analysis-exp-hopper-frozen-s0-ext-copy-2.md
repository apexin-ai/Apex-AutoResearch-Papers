# analysis exp hopper frozen s0 ext

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_hopper_frozen_s0_ext_20260527T104437_result.json`
- **Structured JSON:** [`9fe18814905da5aba741.json`](../../sessions/9f/9fe18814905da5aba741.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 结论：NEGATIVE（hypothesis 被证伪）

**exp_hopper_frozen_s0_ext** 延长训练至 160K 步，eval_return 始终未恢复：

| 对比 | eval_return_final | ve_ratio_final | 恢复? |
|------|-------------------|----------------|-------|
| **frozen_s0_ext** (this) | **0.56** | **15.08** | **否** |
| trained_s0_ext | 81.58 | — | 是 |
| baseline | 96.43 | 0.559 | — |

**核心发现**：
- Frozen dt_embedding 导致 gate 永久锁死在 dt=2（entropy=0），无任何自适应 horizon 行为
- value_mean 从 0.001 膨胀至 8.5，而实际 eval_return ≈ 0 — 典型的 value overestimation 无纠正
- ve_ratio 经历两次灾难性爆发（65K: 820K, 105K: 4.3M），延长后降至 ~15 但不回归正常值 0.5
- 与 trained_s0_ext 形成鲜明对比：可学习的 dt_embedding 是 CIVO 自纠正机制运转的必要条件

**诊断**：frozen_s0 的"degenerate CIVO"不是 transient instability，而是因 frozen embedding 锁死 gate 导致的**结构性不可恢复故障**。

---
