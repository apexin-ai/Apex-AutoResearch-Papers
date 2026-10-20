# train plan003 scrambled retrain perturbation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan003-scrambled-retrain-perturbation_20260518T070024_result.json`
- **Structured JSON:** [`6c2f71a02f58470a6c24.json`](../../sessions/6c/6c2f71a02f58470a6c24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**DeBERTa 训练 (Stage 1):**
- 4 epochs, best_epoch=4, val_persuasion_acc=0.613 (vs plan_002 原始 0.829), val_intent_acc=0.967
- Persuasion acc 下降符合预期（scrambled labels 无法学到真实 label 对应关系）

**GRU 训练 (Stage 2):**
- IID test F1=1.0 (full turns), k=2 时 0.986

**Perturbation Eval (Stage 3):**
| Model | Clean F1 | Perturbed F1 | Delta |
|---|---|---|---|
| 9-class persuasion | 1.000 | 1.000 | 0.000 |
| **Scrambled** | **0.333** | **0.333** | **0.000** |
| Jailbreak MLM | - | - | -0.026 |
| Vanilla baseline | 1.000 | 0.882 | -0.118 |

**关键发现:** Scrambled delta=0 但本质不同于 9-class persuasion 的 delta=0。9-class 模型在 OOD perturbed data 上 clean 和 perturbed 都达到 F1=1.0（真正 robust），而 scrambled 模型在 OOD 数据上完全崩溃（F1=0.333，预测全部为 benign）。这说明 random labels + classification structure **不足以**提供泛化能力，正确的 persuasion label 内容对 OOD robustness 至关重要。

Checkpoints: `checkpoints/plan_003_scrambled_retrain/`
Results: `results/plan_003_scrambled_perturbation.json`
Registry: `plan_003_scrambled_perturbation` (DONE, negative)

---
