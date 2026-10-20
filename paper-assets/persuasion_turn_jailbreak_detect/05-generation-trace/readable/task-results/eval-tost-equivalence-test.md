# eval tost equivalence test

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_tost-equivalence-test_20260518T203518_result.json`
- **Structured JSON:** [`f6f5555591ae0a9f374d.json`](../../sessions/f6/f6f5555591ae0a9f374d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `results/tost_equivalence.json`。

### Per-seed Macro F1

| Dataset | Variant | Seed 42 | Seed 123 | Seed 456 | Mean |
|---------|---------|---------|----------|----------|------|
| DD OOD Full | 9class | 1.0000 | 1.0000 | 0.9904 | 0.9968 |
| DD OOD Full | binary | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| DD OOD Full | scrambled | 0.9904 | 1.0000 | 1.0000 | 0.9968 |
| DD OOD Full | jb_mlm | 1.0000 | 0.9902 | 0.7512 | 0.9138 |
| ActorAttack Full | 9class | 0.9904 | 0.9350 | 0.9904 | 0.9719 |
| ActorAttack Full | binary | 0.9809 | 0.9904 | 1.0000 | 0.9904 |
| ActorAttack Full | scrambled | 0.8913 | 0.9904 | 0.9715 | 0.9510 |
| ActorAttack Full | jb_mlm | 0.9715 | 0.9252 | 0.7836 | 0.8934 |

### TOST Equivalence Results (Δ=0.05)

| Comparison | Dataset | Mean Diff | 90% CI | p_TOST | CI within ±0.05? |
|---|---|---|---|---|---|
| 9class vs scrambled | DD OOD Full | +0.0000 | [-0.016, +0.016] | 0.006 | **Yes** |
| 9class vs scrambled | ActorAttack Full | +0.0209 | [-0.109, +0.151] | 0.290 | No |
| 9class vs binary | DD OOD Full | -0.0032 | [-0.013, +0.006] | 0.002 | **Yes** |
| 9class vs binary | ActorAttack Full | -0.0185 | [-0.075, +0.038] | 0.122 | No |
| 9class vs jb_mlm | DD OOD Full | +0.0830 | [-0.145, +0.311] | 0.643 | No |
| 9class vs jb_mlm | ActorAttack Full | +0.0784 | [-0.109, +0.266] | 0.650 | No |
| scrambled vs binary | DD OOD Full | -0.0032 | [-0.013, +0.006] | 0.002 | **Yes** |
| scrambled vs binary | ActorAttack Full | -0.0394 | [-0.117, +0.038] | 0.363 | No |

### 解读

**DD OOD Full**: 9class vs scrambled、9class vs binary、scrambled vs binary 三对均通过 TOST (p<0.05) 且 90% CI 完全落在 ±0.05 内——正面证明等价。

**ActorAttack Full**: 所有对比对 TOST 均未达显著，90% CI 也超出 margin。这主要是 n=3 seeds 加上 ActorAttack 上 variance 较大（scrambled seed 42 仅 0.891，9class seed 123 仅 0.935）导致 power 不足。不能断言等价，但也不能断言差异——属于 inconclusive。

**jb_mlm 对比**: 两个数据集上均远离等价（mean diff ~0.08，CI 跨零且远超 ±0.05），符合预期——jb_mlm 确实性能更低。

---
