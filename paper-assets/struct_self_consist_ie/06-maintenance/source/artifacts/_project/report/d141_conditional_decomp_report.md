# D141 Task 2: Conditional Success Decomposition

## Methodology

For each test instance with N samples:
- **Condition 1 (Non-degenerate)**: at least 2 samples have different entity-level F1
- **Condition 2 (LP discriminative)**: within-instance LP range > median LP range

Four buckets: Favorable (C1+C2), Cond1-only (C1 only), Cond2-only (C2 only), Unfavorable (neither)

All F1 values are macro-averaged (mean of per-instance F1). Delta = LP_sel - Greedy.

## SciERC (N=529, median LP range=0.040121)

| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |
|--------|--------|---|-----------|-------|-------|--------|
| Favorable | 227 | 42.9 | 0.6333 | 0.6585 | +0.0252 | [0.0034, 0.0476] |
| Cond1-only | 208 | 39.3 | 0.6632 | 0.6546 | -0.0086 | [-0.0330, 0.0162] |
| Cond2-only | 37 | 7.0 | 0.4434 | 0.4254 | -0.0180 | [-0.0541, 0.0000] |
| Unfavorable | 57 | 10.8 | 0.7461 | 0.7461 | +0.0000 | [0.0000, 0.0000] |

## CoNLL (N=2756, median LP range=0.090754)

| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |
|--------|--------|---|-----------|-------|-------|--------|
| Favorable | 955 | 34.6 | 0.8566 | 0.8341 | -0.0224 | [-0.0326, -0.0129] |
| Cond1-only | 466 | 16.9 | 0.8998 | 0.8807 | -0.0191 | [-0.0314, -0.0076] |
| Cond2-only | 423 | 15.3 | 0.9050 | 0.9050 | +0.0000 | [0.0000, 0.0000] |
| Unfavorable | 912 | 33.1 | 0.9643 | 0.9643 | +0.0000 | [0.0000, 0.0000] |

## FewNERD (N=32565, median LP range=0.066227)

| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |
|--------|--------|---|-----------|-------|-------|--------|
| Favorable | 15532 | 47.7 | 0.7830 | 0.7877 | +0.0047 | [0.0026, 0.0069] |
| Cond1-only | 12554 | 38.5 | 0.7469 | 0.7772 | +0.0303 | [0.0268, 0.0338] |
| Cond2-only | 750 | 2.3 | 0.1192 | 0.1098 | -0.0093 | [-0.0160, -0.0038] |
| Unfavorable | 3729 | 11.4 | 0.7312 | 0.7296 | -0.0015 | [-0.0031, -0.0000] |