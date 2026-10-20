# train plan017 mlm control

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan017-mlm-control_20260518T052428_result.json`
- **Structured JSON:** [`9e1bcc4ec088cd2ee590.json`](../../sessions/9e/9e1bcc4ec088cd2ee590.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 017 complete. Here are the results:

## Plan 017: MLM Continued Pretraining Control — Results

### DD OOD (Deceptive Delight)

| K | MLM Control | Persuasion (006) | Vanilla Baseline (006) |
|---|---|---|---|
| 1 | **1.000** | 1.000 | 0.575 |
| 2 | **1.000** | 0.990 | 0.438 |
| 3 | **1.000** | 0.990 | N/A |
| 5 | **1.000** | 1.000 | N/A |
| full | **1.000** | 1.000 | 0.285 |

### IID (Crescendo test set)
| K | MLM Control |
|---|---|
| 1 | 0.960 |
| 2 | 0.974 |
| 3 | 0.987 |
| 5 | 1.000 |
| full | 1.000 |

### MLM Training Summary
- 4 epochs, val MLM loss: 6.50 → 3.77 → 2.91 → 2.47
- BiGRU converged to val loss 0.005, 100% val accuracy by epoch 15

### Interpretation

**Track B confirmed:** MLM control F1 = 1.0 across all K values on DD OOD, matching the persuasion treatment exactly. Pure text exposure (no classification labels) is sufficient for cross-attack generalization.

This means:
- **Classification supervision is NOT necessary** for the OOD generalization effect
- The critical factor is **domain-adaptive fine-tuning** on jailbreak conversation text, not the persuasion strategy labels
- Combined with plan_003 (scrambled labels ≈ proper labels), this consistently points to: **fine-tuning on the right text distribution is what matters, not what task you fine-tune on**
- The vanilla baseline fails because it has zero exposure to this text distribution, not because it lacks persuasion understanding

The paper framing needs adjustment. The value of persuasion supervision shifts from "necessary for OOD generalization" to "providing interpretability" (strategy trajectories, turn-level explanations).

---
