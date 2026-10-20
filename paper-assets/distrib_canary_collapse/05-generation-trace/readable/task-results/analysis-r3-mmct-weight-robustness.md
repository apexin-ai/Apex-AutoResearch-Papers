# analysis r3 mmct weight robustness

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r3_mmct_weight_robustness_20260520T153326_result.json`
- **Structured JSON:** [`afac7ad0c5f77db67d3c.json`](../../sessions/af/afac7ad0c5f77db67d3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

| Scheme | PermG Rank | PermG Combined | 2nd Place | Gap |
|--------|-----------|----------------|-----------|-----|
| **Equal (w=1)** | **#1** | -0.1516 | NaiveXCorr (-0.1373) | 0.014 |
| **Cap-5** | **#1** | -0.1653 | NaiveXCorr (-0.1227) | 0.043 |
| **Cap-10** | **#1** | -0.4257 | TYGranger (-0.0667) | 0.359 |
| **Cap-100 (original)** | **#1** | -0.4257 | TYGranger (-0.0667) | 0.359 |

**PermG ranks #1 under ALL 4 weighting schemes**, including equal-weighting where every method has w=1 (no FPR-based advantage at all). The circularity concern is fully resolved.

Key points:
- **Equal-weight** is the strongest test: PermG's advantage comes purely from zero FPR + strong FNR reduction, not from weight design
- Cap-10 and Cap-100 are degenerate (identical results) because the 3-smallest-weight threshold is the same (7.76) and both PermG/TY individually exceed it
- FPR/FNR rates verified against Shapley v3 reference (exact match)

Output: `artifacts/mmct_weight_robustness.json`

---
