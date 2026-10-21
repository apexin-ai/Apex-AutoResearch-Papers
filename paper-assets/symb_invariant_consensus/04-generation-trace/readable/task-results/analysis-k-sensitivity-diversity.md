# analysis k sensitivity diversity

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k-sensitivity-diversity_20260519T010940_result.json`
- **Structured JSON:** [`62ded5bcea1a26d2fbcc.json`](../../sessions/62/62ded5bcea1a26d2fbcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Here's the analysis:

## K vs Diversity Metrics (FOLIO-204, Mistral-7B, T=0.7)

| K | n | SC% | SICA% | delta | Entropy | Uniq Constr | Jaccard | Eff Div | Contr% | Status |
|---|---|-----|-------|-------|---------|-------------|---------|---------|--------|--------|
| 4 | 204 | 54.41 | 52.94 | -1.47 | 0.6315 | 19.4 | 0.1169 | 0.2328 | 2.16 | complete |
| 8 | 204 | 57.35 | 56.37 | -0.98 | 0.7875 | 32.2 | 0.1348 | 0.2460 | 2.70 | complete |
| 12 | 204 | 54.41 | 59.31 | +4.90 | 0.8150 | 39.3 | N/A | 0.2485 | 3.50 | complete |
| 16 | 61 | 65.57 | 65.57 | +0.00 | 0.8021 | 53.9 | 0.1560 | 0.2311 | 3.64 | in-progress |

### Constraint Scaling (diminishing unique ratio)
| K | Total | Unique | Unique% | Per-problem total | Per-problem unique |
|---|-------|--------|---------|-------------------|-------------------|
| 4 | 4,813 | 3,565 | 74.1% | 23.6 | 17.5 |
| 8 | 9,287 | 5,811 | 62.6% | 45.5 | 28.5 |
| 12 | 14,042 | 8,021 | 57.1% | 68.8 | 39.3 |
| 16* | 5,585 | 2,856 | 51.1% | 91.6 | 46.8 |

### Why K=12 is the sweet spot

Three converging signals:

1. **SICA delta peaks at K=12 (+4.90pp)**. At K=4/8, SICA actually underperforms SC (negative delta). Only at K=12 does constraint-based consensus overtake majority vote. K=16 partial data shows delta=0.

2. **Diversity saturates around K=12**. Answer entropy rises 0.63→0.79→0.82, then plateaus at 0.80 for K=16. Effective diversity peaks at K=12 (0.249) and drops at K=16 (0.231). The incremental diversity from more traces has diminishing returns.

3. **Noise grows linearly while unique info decays**. Unique constraint ratio drops from 74%→63%→57%→51%. Contradiction rate rises 2.2%→2.7%→3.5%→3.6%. More traces = more redundant and conflicting constraints, diluting the MaxSAT signal.

### Exp-051 progress
- K=4: done
- K=8: done
- K=16: 61/204 (actively running, ~30% done)
- K=20: not started

Note: K=12 Jaccard is N/A because exp033 didn't store per-trace constraint breakdowns (only aggregate `constraints_stats`). K=16 metrics are preliminary (61 samples may be order-biased).

---
