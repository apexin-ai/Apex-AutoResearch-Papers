# train plan003 scrambled fix data

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan003-scrambled-fix-data_20260518T073310_result.json`
- **Structured JSON:** [`d11990c5d0fc03afcf62.json`](../../sessions/d1/d11990c5d0fc03afcf62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 实验结果总结

**plan_003_scrambled_fix** 全部完成，使用正确数据源 `data/plan_002_splits/`。

| 指标 | 值 |
|---|---|
| **DeBERTa** val_persuasion_acc | 0.679 (scrambled 导致下降) |
| **DeBERTa** val_intent_acc | 1.0 (未受影响) |
| **IID Test F1 (full)** | 1.0000 |
| **DD OOD F1 (full)** | 0.9904 |
| **DD OOD F1 (k=2)** | 0.9439 |
| **DD OOD F1 (k=3)** | 0.9350 |
| **Perturbation delta (full)** | 0.0000 |
| **Perturbation delta (k=1)** | +0.0527 |

**结论 (negative)**: DD OOD F1 = 0.9904，远非预期的 0.333（全预测 benign）。Scrambled persuasion labels 未显著降低检测性能。原因：intent classification head（binary jailbreak/benign）的标签未被打乱，DeBERTa 微调通过 intent 信号即可学到足够的 jailbreak 表征。正确的 persuasion strategy 标签不是检测的核心机制。

产出：
- 结果 JSON: `results/plan_003_scrambled_fix.json`
- DeBERTa checkpoint: `checkpoints/plan_003_scrambled_fix/deberta_multitask/best/`
- GRU checkpoint: `checkpoints/plan_003_scrambled_fix/gru/best.pt`
- 训练日志: `results/plan_003_scrambled_fix_stage1.log`, `results/plan_003_scrambled_fix_stage2.log`

---
