# eval v8 step2k read results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v8-step2k-read-results_20260516T001442_result.json`
- **Structured JSON:** [`94abf41470ad4a1966f6.json`](../../sessions/94/94abf41470ad4a1966f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v8 (Gradient Isolation) Step 2K Early Eval 结果

### Bypass Eval (bypass-ACIS, 纯模型质量)

| 条件 | action_loss |
|------|------------|
| **eps0.0_pruneFalse (clean)** | **0.05790** |
| eps0.0_pruneTrue | 0.04700 |
| eps0.01_pruneFalse | 0.05165 |
| eps0.02_pruneFalse | 0.05505 |
| eps0.05_pruneFalse | 0.06057 |

### Standard Eval (含 ACIS)

| 条件 | action_loss | margin_median | preservation | LED_median |
|------|------------|---------------|-------------|------------|
| **eps0.0 clean** | **0.04036** | 0.166 | 1.000 | 0.281 |
| eps0.0 prune | 0.04502 | 0.172 | 1.000 | 0.273 |
| eps0.01 | 0.03525 | 0.166 | 0.921 | 0.282 |
| eps0.02 | 0.04545 | 0.166 | 0.828 | 0.564 |
| eps0.05 | 0.04321 | 0.172 | 0.644 | 1.359 |

### Gate 评估

| Gate | 值 | 阈值 | 结果 |
|------|-----|------|------|
| **G1** margin ratio | **15.83x** | ≥ 2.0 | **PASS** |
| **G2** preservation diff | **+0.461** | ≥ 0.10 | **PASS** |
| **G3** clean loss ratio | **9.90x** | ≤ 1.10 | **FAIL** |
| **G4** LED median | **0.564** | < 1.0 | **PASS** |

### G3 指标计算

- **G3a** (bypass clean / baseline final) = 0.05790 / 0.00408 = **14.19x**
- **G3b** (standard clean / baseline final) = 0.04036 / 0.00408 = **9.89x**

### 总结

**OVERALL: FAIL** — G1/G2/G4 全过，但 G3 严重不达标。

Step 2K 时 clean action_loss 0.04036 (standard) / 0.05790 (bypass)，远高于 baseline final 0.00408。这是预期中的——step 2K 仅训练了 6.7%，模型还远未收敛。参考 baseline 自身 step 2K 时大约在 ~0.04-0.05 范围（step 5K 为 0.01891），所以 v8 step 2K 的 loss 水平与 baseline 同期基本一致，并无异常退化。

**与 v7/v7.2 对比建议**: v7/v7.2 只有 final (30K) 数据，无法直接对比 step 2K。但 v8 的 margin (15.8x) 和 preservation (+0.461) 显著优于 v7 final 的水平，gradient isolation 的 ACIS 学习效率明显更高。关键问题是 v8 能否在继续训练后让 clean loss 收敛到 baseline 水平——需要等更多 checkpoint 评估。

---
