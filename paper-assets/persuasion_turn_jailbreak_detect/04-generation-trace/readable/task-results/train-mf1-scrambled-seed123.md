# train mf1 scrambled seed123

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_mf1-scrambled-seed123_20260518T091249_result.json`
- **Structured JSON:** [`22a99d66f9325fe80865.json`](../../sessions/22/22a99d66f9325fe80865.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MF1 pipeline complete. Summary:

**MF1 Scrambled Labels seed=123 — Results**

| Stage | Metric | Value |
|-------|--------|-------|
| DeBERTa | val_persuasion_acc | 0.6724 |
| DeBERTa | val_intent_acc | 1.0 |
| DeBERTa | val_loss | 0.7906 |
| DD OOD | F1 @ K=1 | 1.0 |
| DD OOD | F1 @ K=2 | 1.0 |
| DD OOD | F1 @ K=3 | 1.0 |
| DD OOD | F1 @ K=5 | 1.0 |
| DD OOD | F1 Full | 1.0 |

**Artifacts on server:**
- Scrambled data: `data/plan_002_splits/train_scrambled_seed123.jsonl`
- DeBERTa checkpoint: `checkpoints/mf1_scrambled_seed123/deberta_multitask/best/`
- GRU checkpoint: `checkpoints/mf1_scrambled_seed123/gru/best.pt`
- Results JSON: `results/mf1_scrambled_seed123.json`

**Comparison with seed=42:** DeBERTa persuasion acc similar (0.6724 vs 0.6792). DD OOD F1 slightly higher (1.0 vs 0.9904 for seed=42). Both seeds show that the scrambled model retains strong jailbreak detection because the intent classification head (val_intent_acc=1.0) provides sufficient signal for the GRU classifier.

---
