# analysis t20 predictions locked

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t20_predictions_locked_20260520T104710_result.json`
- **Structured JSON:** [`a3bcfc06136848044891.json`](../../sessions/a3/a3bcfc06136848044891.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered: `art_20260520_aa9d51`.

## T=20 Locked Predictions Summary

**Sigmoid fit** (T=10, excl. α=0.60 sync dip): step-function at α_c = 0.4755, y_max = 0.752 (k=200, essentially binary transition).

| α | T=10 actual | T=20 predicted | Confidence |
|------|-------------|----------------|------------|
| 0.45 | 0/8 | **0/8** | medium — key falsifiable test |
| 0.50 | 6/8 | **7/8** | high |
| 0.60 | 3/8 | **3/8** | low — sync dip |
| 0.75 | 6/8 | **7/8** | high |
| 1.00 | 6/8 | **7/8** | high |

**Interpretation**: The T=10 transition is so sharp (0/8 → 6/8 between α=0.45 and α=0.50) that the sigmoid is effectively a step function. Power theory predicts α≥0.50 should gain ~1 pair (6→7/8) at T=20, while α=0.45 stays at 0/8. If T=20 observation shows α=0.45 > 0/8, that falsifies the step-function model and confirms left-shift of the phase boundary with increasing T.

---
