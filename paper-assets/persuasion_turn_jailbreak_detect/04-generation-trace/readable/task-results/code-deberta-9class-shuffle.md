# code deberta 9class shuffle

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deberta-9class-shuffle_20260520T092737_result.json`
- **Structured JSON:** [`411f494460f99effdff8.json`](../../sessions/41/411f494460f99effdff8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

```
DeBERTa-v3-base (exp1) 9-class Turn-Shuffle Results:

=== IID Test (76 samples) ===
  Original:  F1 = 1.0000±0.0000
  Shuffled:  F1 = 1.0000±0.0000 (9 runs)
  Δ = +0.0000

=== DD OOD (118 samples) ===
  Original:  F1 = 0.9936±0.0045
  Shuffled:  F1 = 0.9936±0.0045 (9 runs)
  Δ = +0.0000

=== AA OOD (118 samples) ===
  Original:  F1 = 0.9391±0.0465
  Shuffled:  F1 = 0.9306±0.0562 (9 runs)
  Δ = -0.0085
```

**验证通过**: Original DD OOD F1=0.9936，与已知值 0.994 一致（seed42=1.0, seed123=0.9904, seed456=0.9904）。

**结论**: DD OOD shuffle Δ=0.0000，IID shuffle Δ=0.0000，AA OOD shuffle Δ=-0.0085（微小）。跨 encoder 确认了 order-invariance——与 RoBERTa-large (exp15) 的结论一致，turn 顺序对检测性能几乎无影响。

---
