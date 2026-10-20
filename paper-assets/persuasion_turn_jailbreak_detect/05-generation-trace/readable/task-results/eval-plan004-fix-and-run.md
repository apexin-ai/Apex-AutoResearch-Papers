# eval plan004 fix and run

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan004-fix-and-run_20260517T234937_result.json`
- **Structured JSON:** [`39d613f1edb2393d25e9.json`](../../sessions/39/39d613f1edb2393d25e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 修复内容

1. **adversarial_perturbation.py L416**: `num_persuasion_classes=8` → `9`（与 checkpoint 和模型默认值一致）

2. **eval_early_detection.py L205-216**: 硬编码的 stage1 metrics 替换为从 `training_metrics.json` 动态读取，fallback 值也更新为实际训练日志的正确数据（best_epoch=2, persuasion_acc=0.8285, intent_acc=1.0, val_loss=0.4759）

### 三路对比结果 (K=full)

| Model | Original F1 | Perturbed F1 | Delta | Robustness |
|-------|------------|-------------|-------|-----------|
| TF-IDF | 1.0000 | 0.9867 | -0.0133 | HIGH |
| Vanilla DeBERTa (Baseline) | 1.0000 | 0.8824 | **-0.1176** | LOW |
| Persuasion DeBERTa (Treatment) | 1.0000 | **1.0000** | **+0.0000** | HIGH |

Treatment 在所有 K≥2 上 perturbed F1 均为 1.0，无下降。Baseline 在所有 K 上 drop 12-15%。结果保存至 `results/plan_004_perturbation_eval.json`。

---
