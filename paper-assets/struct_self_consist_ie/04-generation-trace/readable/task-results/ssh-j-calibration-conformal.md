# ssh j calibration conformal

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_j-calibration-conformal_20260520T101503_result.json`
- **Structured JSON:** [`93861c79254e6cfefb30.json`](../../sessions/93/93861c79254e6cfefb30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifacts registered. Results summary:

## Calibration (ECE)

| Dataset | ECE | Interpretation |
|---------|-----|----------------|
| **SciERC** | 0.098 | Overconfident — entities with 8/8 agreement are only 82% correct |
| **CoNLL** | 0.037 | Well-calibrated — 8/8 agreement entities are 97% correct |
| **FewNERD** | 0.035 | Well-calibrated — monotonic confidence→accuracy relationship |

SciERC's higher ECE is driven by the high-confidence bins (0.75–1.0) where accuracy lags 15–25pp behind confidence.

## Conformal Prediction (α=0.1, target: coverage ≥ 0.9)

| Dataset | Coverage | Threshold | Avg Set Size | Passes? |
|---------|----------|-----------|-------------|---------|
| **CoNLL** | 0.925 | 0.125 | 2.8 | ✓ |
| **FewNERD** | 0.789 | 0.000 | 5.3 | ✗ |
| **SciERC** | 0.566 | 0.000 | 5.4 | ✗ |

For SciERC and FewNERD, the threshold drops to 0.0 (include everything) yet coverage still fails — this means ~21% (FewNERD) and ~43% (SciERC) of instances have gold entities that never appear in any of the N=8 samples. This is a fundamental recall ceiling, not a thresholding issue. CoNLL passes comfortably because its entity types (PER/LOC/ORG) are more consistently generated.

---
