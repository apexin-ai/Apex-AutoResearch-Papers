# train exp3 probing

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_exp3-probing_20260518T104339_result.json`
- **Structured JSON:** [`2c08ebed5dc4e6fe48bd.json`](../../sessions/2c/2c08ebed5dc4e6fe48bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Results summary:

**Linear Probing (5-fold CV accuracy +/- population std):**

| Task | Vanilla | MLM | 9-class |
|---|---|---|---|
| Turn Position | 0.7867 +/- 0.0339 | 0.7915 +/- 0.0609 | **0.8280** +/- 0.0987 |
| Escalation Level | 0.7319 +/- 0.0226 | 0.7315 +/- 0.0262 | **0.7817** +/- 0.0267 |
| Persuasion Presence | 0.9377 +/- 0.0854 | 0.9429 +/- 0.0873 | **0.9494** +/- 0.0926 |

**CKA (last layer CLS):**

| Pair | IID | DD OOD |
|---|---|---|
| vanilla vs mlm | 1.0000 | 1.0000 |
| vanilla vs 9class | 0.3668 | 0.8849 |
| mlm vs 9class | 0.3684 | 0.8847 |

**Layer-wise CKA key pattern:** All pairs are CKA~1.0 through layers 0-10. Divergence appears only in layers 11-12, concentrated at the final layer. The 9-class finetuning dramatically reshapes layer 12 representations (IID CKA drops to 0.37), while MLM pretraining leaves the representation space virtually unchanged (CKA=1.0 at all layers).

Key takeaways:
- 9-class multitask finetuning creates meaningfully different representations that encode more task-relevant features (turn position, escalation, persuasion)
- MLM continued pretraining has negligible effect on representation geometry
- Representation changes from 9-class training are concentrated in the top 2 layers
- DD OOD representations are more similar across encoders (CKA 0.88) than IID (CKA 0.37), suggesting the IID data has more diverse signal that fine-tuning can exploit

---
