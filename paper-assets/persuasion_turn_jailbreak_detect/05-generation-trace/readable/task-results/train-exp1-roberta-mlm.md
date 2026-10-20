# train exp1 roberta mlm

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_exp1-roberta-mlm_20260518T102224_result.json`
- **Structured JSON:** [`457d84e2af558393c892.json`](../../sessions/45/457d84e2af558393c892.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Results summary:

**RoBERTa MLM-only (continued pretraining + BiGRU):**

| Metric | Mean | Std |
|---|---|---|
| DD OOD K=1 | 0.9428 | 0.0184 |
| DD OOD K=2 | 0.9747 | 0.0232 |
| DD OOD K=3 | 0.9747 | 0.0232 |
| DD OOD K=5 | 0.9841 | 0.0160 |
| DD OOD Full | 0.9874 | 0.0178 |

**RoBERTa Vanilla (no pretraining + BiGRU):**

| Metric | Mean | Std |
|---|---|---|
| DD OOD K=1 | 0.9127 | 0.1028 |
| DD OOD K=2 | 0.9003 | 0.1342 |
| DD OOD K=3 | 0.8976 | 0.1381 |
| DD OOD K=5 | 0.9442 | 0.0789 |
| DD OOD Full | 0.9813 | 0.0264 |

MLM pretraining shows slightly higher mean F1 and substantially lower variance across seeds compared to vanilla. The vanilla baseline has high variance driven by seed=42 underperforming (K=1 F1=0.77 vs 0.98-0.99 for other seeds).

Artifacts saved to:
- `artifacts/exp1_roberta_mlm_results.json`
- `artifacts/exp1_roberta_vanilla_results.json`

Server-side results at:
- `results/exp1_roberta_mlm.json`
- `results/exp1_roberta_vanilla.json`

Script: `src/exp1_roberta_mlm_pipeline.py`

---
