# D141 Conditional Success Decomposition — Span Matching (Fixed)

**Date**: 2026-05-18
**Fix**: Restored `entity_f1` to span matching `(start, end, type)` — previously incorrectly changed to text matching `(text, type)`.

## Methodology

For each test instance with N=8 samples:
- **Condition 1 (Non-degenerate)**: at least 2 samples have different entity-level F1
- **Condition 2 (LP discriminative)**: within-instance LP range > median LP range

Four buckets: Favorable (C1+C2), Cond1-only (C1 only), Cond2-only (C2 only), Unfavorable (neither).

All F1 values are macro-averaged (mean of per-instance F1). Delta = LP_sel - Greedy.

Evaluation: **strict span matching** `(start, end, type)` — consistent with main table and entity_merge analysis.

## SciERC (N=529, median LP range=0.040121)

| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |
|--------|--------|---|-----------|-------|-------|--------|
| Favorable | 227 | 42.9 | 0.6333 | 0.6585 | +0.0252 | [0.0034, 0.0476] |
| Cond1-only | 208 | 39.3 | 0.6632 | 0.6546 | -0.0086 | [-0.0330, 0.0162] |
| Cond2-only | 37 | 7.0 | 0.4434 | 0.4254 | -0.0180 | [-0.0541, 0.0000] |
| Unfavorable | 57 | 10.8 | 0.7461 | 0.7461 | +0.0000 | [0.0000, 0.0000] |

## CoNLL (N=2756, median LP range=0.062012)

| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |
|--------|--------|---|-----------|-------|-------|--------|
| Favorable | 841 | 30.5 | 0.8679 | 0.8491 | -0.0188 | [-0.0293, -0.0085] |
| Cond1-only | 318 | 11.5 | 0.8441 | 0.8239 | -0.0202 | [-0.0431, 0.0017] |
| Cond2-only | 537 | 19.5 | 0.8887 | 0.8887 | +0.0000 | [0.0000, 0.0000] |
| Unfavorable | 1060 | 38.5 | 0.9661 | 0.9661 | +0.0000 | [0.0000, 0.0000] |

## FewNERD (N=4351, median LP range=0.066996)

| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |
|--------|--------|---|-----------|-------|-------|--------|
| Favorable | 2064 | 47.4 | 0.7829 | 0.7898 | +0.0069 | [0.0005, 0.0135] |
| Cond1-only | 1659 | 38.1 | 0.7548 | 0.7821 | +0.0274 | [0.0182, 0.0371] |
| Cond2-only | 111 | 2.5 | 0.1171 | 0.1141 | -0.0030 | [-0.0090, 0.0000] |
| Unfavorable | 517 | 11.9 | 0.7206 | 0.7171 | -0.0035 | [-0.0089, 0.0000] |

## Summary

**SciERC**:
- Favorable: Delta=+0.0252 CI=[0.0034, 0.0476] (42.9%) — significant positive gain
- Cond1-only: Delta=-0.0086 (39.3%)
- Cond2-only: Delta=-0.0180 (7.0%)
- Unfavorable: Delta=+0.0000 (10.8%)

**CoNLL**:
- Favorable: Delta=-0.0188 CI=[-0.0293, -0.0085] (30.5%) — LP selection hurts
- Cond1-only: Delta=-0.0202 (11.5%)
- Cond2-only: Delta=+0.0000 (19.5%)
- Unfavorable: Delta=+0.0000 (38.5%)

**FewNERD**:
- Favorable: Delta=+0.0069 CI=[0.0005, 0.0135] (47.4%) — significant positive gain
- Cond1-only: Delta=+0.0274 CI=[0.0182, 0.0371] (38.1%) — strong gain even without LP discriminativeness
- Cond2-only: Delta=-0.0030 (2.5%)
- Unfavorable: Delta=-0.0035 (11.9%)
