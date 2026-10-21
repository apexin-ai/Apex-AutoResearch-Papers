# alpha_sweep_a050_s42 Final Analysis

## Gen10 Final Metrics
- token_entropy: 2.6318
- ece: 0.1019
- perplexity: 32.644
- distinct_1: 0.0616
- distinct_2: 0.2513
- distinct_3: 0.3873
- effective_rank: 59.333
- mauve: 0.0210

## Gen0→Gen10 Drift
- token_entropy: -18.63%
- ece: +842.8%
- perplexity: +21.14%
- distinct_1: -37.28%
- distinct_2: -51.47%
- distinct_3: -52.36%
- mauve: -38.48%

## Granger Causality (diff-permutation, n_perm=5000, max_lag=1)
| Pair | diff_p | diff_sig | undiff_p | undiff_sig |
|------|--------|----------|----------|------------|
| entropy→d1 | 0.095 | No | 0.042 | Yes |
| entropy→d2 | 0.097 | No | 0.034 | Yes |
| ece→d1 | 0.019 | Yes | 0.010 | Yes |
| ece→d2 | 0.039 | Yes | 0.014 | Yes |

Diff-sig: 2/4 (ece channel sig, entropy channel n.s.)

## Cross-Alpha Comparison
| α | d1_drift | d2_drift | entropy_drift | ece_drift | Granger diff-sig |
|---|---------|---------|--------------|----------|-----------------|
| 0.00 | -13.8% | -9.8% | -5.1% | +51.7% | N/A (baseline) |
| 0.25 | -40.3% | -57.1% | -4.1% | +79.7% | TY 3/8 marginal |
| 0.50 | -37.3% | -51.5% | -18.6% | +842.8% | 2/4 (ece sig, entropy n.s.) |
| 1.00 | -25.6% | N/A | ~-60% | ~+3700% | 24/24 all sig |

## Key Finding
alpha=0.50 is NOT a uniform detectability boundary. It is the boundary specifically for token_entropy as canary (p~0.095). ECE remains strong at alpha=0.50 (p=0.019-0.039). Refines D025: detectability threshold is canary-dependent.

## α=0.75 Predictions
- entropy_drift: ~-35% to -45%
- ece_drift: ~+1500% to +2500%
- Granger: likely 3/4 or 4/4 diff-sig

## Checkpoint
/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_10/checkpoint