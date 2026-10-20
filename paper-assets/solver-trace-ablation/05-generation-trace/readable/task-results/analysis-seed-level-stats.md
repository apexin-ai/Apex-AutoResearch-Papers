# analysis seed level stats

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed-level-stats_20260517T114905_result.json`
- **Structured JSON:** [`c304373d99eb8b7cdc32.json`](../../sessions/c3/c304373d99eb8b7cdc32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Script ran successfully. Here are the complete results:

---

## Results

### 2a. CMH Test (seed-stratified, sample-level)

| Comparison | Pooled OR | 95% CI | CMH chi2 | p-value |
|---|---|---|---|---|
| H7 rate | 2.460 | [1.852, 3.268] | 65.63 | 5.55e-16 |
| Genuine rate | 3.366 | [2.210, 5.126] | 38.88 | 4.51e-10 |

Both significant even after accounting for seed clustering.

### 2b. Permutation Test (seed as unit, n=5 per group)

| Comparison | ISR mean | Random mean | Δ | p-value |
|---|---|---|---|---|
| H7 rate | 0.530 | 0.260 | +0.271 | 0.281 |
| Genuine rate | 0.260 | 0.083 | +0.177 | 0.262 |
| H7+H8 hacking | 0.575 | 0.316 | +0.259 | 0.242 |

None significant at seed level (n=5 per group is underpowered; min possible p = 0.0079).

### 2c. Wilson 95% CI per seed

Key observations: ISR seeds 45/46 have 55% genuine (CI: [40-69%]), while ISR seeds 43/44 have ~0% genuine (100% H7 collapse). Massive inter-seed variance.

### 2d. Pooled 5-seed summary

| | ISR β=0.1 | Random β=0.1 |
|---|---|---|
| Proved | 350 | 414 |
| H7 | 188 (53.7%) | 122 (29.5%) |
| Genuine | 81 (23.1%) | 32 (7.7%) |
| Pooled Fisher: H7 | OR=2.778, p=1.32e-11 | |
| Pooled Fisher: Genuine | OR=3.595, p=2.78e-9 | |

### Key takeaway

CMH (sample-level, seed-stratified) confirms both effects are significant (p<1e-9). Permutation tests (seed as unit) are non-significant due to n=5 power limitation combined with extreme bimodality (collapsed vs non-collapsed seeds). This is the expected pattern: the effect is real at the sample level even accounting for clustering, but per-seed variance is too high relative to group size for seed-level tests to reach significance.

---
