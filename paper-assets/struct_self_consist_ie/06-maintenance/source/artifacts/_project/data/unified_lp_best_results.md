## Unified Instance Set LP-best F1 Results (2026-05-22)

### SciERC (529 unified instances, greedy=0.6683)

| N | LP-best F1 | LP Δ(pp) |
|---|-----------|----------|
| 8 | 0.6651 | -0.32 |
| 16 | 0.6635 | -0.48 |
| 32 | 0.6708 | +0.25 |
| 64 | 0.6712 | +0.29 |

### CoNLL (2756 unified instances, greedy=0.9123)

| N | LP-best F1 | LP Δ(pp) |
|---|-----------|----------|
| 8 | 0.8961 | -1.62 |
| 16 | 0.8887 | -2.36 |
| 32 | 0.8923 | -2.00 |
| 64 | 0.8889 | -2.34 |

### Key Insight
LP-best (select sample with highest mean log-prob) is strictly worse than greedy.
MV strict crosses greedy at N≈24 (SciERC) and is positive from N=8 (CoNLL).
This contrasts confidence-based selection (fails) vs agreement-based aggregation (succeeds at scale).