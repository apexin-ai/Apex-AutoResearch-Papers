# analysis freeform 3seed integration

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_freeform_3seed_integration_20260515T184905_result.json`
- **Structured JSON:** [`6128b2d8efb4232a3c9e.json`](../../sessions/61/6128b2d8efb4232a3c9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the 3-seed freeform ablation summary:

### Freeform QE Signals (mean±σ across seeds 123/456/789)

**NER (n=529)**
| Signal | ρ | AUROC |
|--------|---|-------|
| VC | 0.415±0.007 | 0.775±0.022 |
| SJ | 0.386±0.008 | 0.730±0.021 |
| EM | 0.322±0.004 | 0.510±0.028 |
| FK | 0.307±0.019 | 0.772±0.020 |
| LP | 0.230±0.015 | 0.684±0.016 |

**RE (n=397)**
| Signal | ρ | AUROC |
|--------|---|-------|
| VC | 0.308±0.008 | 0.640±0.010 |
| LP | 0.304±0.007 | 0.698±0.009 |
| FK | 0.265±0.047 | 0.655±0.023 |
| SJ | 0.229±0.039 | 0.587±0.024 |
| EM | 0.115±0.019 | 0.475±0.013 |

### LP Compression
- Freeform tied_pct = **58.37±0.65%** vs constrained **59.7%**
- Variance ratio = **0.92±0.04x** (freeform slightly *less* compressed)
- Tied reduction = **1.33±0.65pp** (minimal)

### Selection Gap (freeform)
- NER: **+0.21±0.12pp** (consistently positive)
- RE: **+1.89±0.12pp** (stronger, very stable)

### Conclusion
LP compression persists in freeform decoding (58.4% tied vs 59.7% constrained), confirming it is **model/task intrinsic**, not a constrained decoding artifact. LP is notably the most stable RE signal across seeds (σ=0.007) while being weakest for NER — this task-dependent pattern is preserved in freeform. Parse rate 99.98±0.03% shows grammar constraints aren't needed for structural output fidelity.

Artifact registered: `freeform_3seed_summary.json` (art_20260515_74add7).

---
