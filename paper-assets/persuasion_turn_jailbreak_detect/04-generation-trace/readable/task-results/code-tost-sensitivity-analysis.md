# code tost sensitivity analysis

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tost-sensitivity-analysis_20260520T060835_result.json`
- **Structured JSON:** [`1c901632664067ff2be6.json`](../../sessions/1c/1c901632664067ff2be6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
TOST Sensitivity Analysis (9class vs scrambled labels)
============================================================

Dataset: DD OOD Full
  9class F1s:    [1.0, 1.0, 0.9904]
  scrambled F1s: [0.9904, 1.0, 1.0]
  Per-seed diffs: [0.0096, 0.0, -0.0096]
  Mean difference: 0.000000
  SE: 0.005565

  δ=5pp (0.05) [original]:  p_tost = 0.0061  → EQUIVALENT
  δ=2pp (0.02):             p_tost = 0.0347  → EQUIVALENT
  δ=3pp (0.03):             p_tost = 0.0164  → EQUIVALENT

Dataset: ActorAttack Full
  9class F1s:    [0.9904, 0.935, 0.9904]
  scrambled F1s: [0.8913, 0.9904, 0.9715]
  Per-seed diffs: [0.0991, -0.0554, 0.0189]
  Mean difference: 0.020860
  SE: 0.044608

  δ=5pp (0.05) [original]:  p_tost = 0.2903  → NOT equivalent
  δ=2pp (0.02):             p_tost = 0.5068  → NOT equivalent
  δ=3pp (0.03):             p_tost = 0.4283  → NOT equivalent
```

**DD OOD Full**: 即使收紧到 δ=2pp，TOST 仍然显著 (p=0.035)，scrambled 与 correct 等价。这说明在 DD OOD 上，9-class label 的信息量有限——scrambled 后模型表现不变。不过 p=0.035 已接近 0.05 边界，比原始 δ=5pp 的 p=0.006 弱很多。

**ActorAttack Full**: 所有 δ 值下 TOST 均不显著（p 远大于 0.05），scrambled 与 correct 不等价。这支持 9-class label 在 ActorAttack 上提供了有意义的信息。高方差（SE=0.045）源于 seed 42 的差异极大（+9.9pp）。

---
