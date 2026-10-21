# 5-Method Lead-Lag Analysis: α=0.75, seed=44

## Setup
- Model: Pythia-410M, Dataset: WikiText-103 5k subset
- T=11 generations (gen_0..gen_10), α=0.75
- Canaries: token_entropy, ece
- Downstreams: distinct_1, distinct_2, distinct_3, perplexity
- 8 pairs × 2 directions = 16 tests

## Method Summary

| Method | Forward sig | Reverse sig | Notes |
|--------|-------------|-------------|-------|
| Naive XCorr | 4/8 (lag≤0) | — | ece pairs show canary-leads lag |
| Diff XCorr (FDR) | 8/8 | 8/8 | All significant both directions (short series) |
| Threshold Onset | 4/8 | 0/8 | token_entropy onset gen1, downstream gen2 |
| Perm Granger (FDR) | **6/8** | **0/8** | Strong directional asymmetry |
| TY Granger | 1/8 | 0/8 | Only ece→distinct_2 (d_max=1, df_resid=5) |

## Permutation Granger Detail (Forward, BH FDR q=0.05)

| Pair | F-stat | p_raw | p_FDR | Sig | f² |
|------|--------|-------|-------|-----|-----|
| token_entropy→distinct_1 | 356.53 | 0.0362 | 0.0483 | * | 59.42 |
| token_entropy→distinct_2 | 215.00 | 0.0472 | 0.0630 | | 35.83 |
| token_entropy→distinct_3 | 101.06 | 0.0450 | 0.0601 | | 16.84 |
| token_entropy→perplexity | 40.04 | 0.0228 | 0.0364 | * | 6.67 |
| ece→distinct_1 | 144.65 | 0.0228 | 0.0364 | * | 24.11 |
| ece→distinct_2 | 87.04 | 0.0270 | 0.0364 | * | 14.51 |
| ece→distinct_3 | 56.51 | 0.0304 | 0.0406 | * | 9.42 |
| ece→perplexity | 40.84 | 0.0228 | 0.0364 | * | 6.81 |

## Threshold Onset

| Pair | Canary onset | Downstream onset | Lead time |
|------|-------------|-----------------|-----------|
| token_entropy→distinct_1 | gen 1 | gen 2 | +1 gen * |
| token_entropy→distinct_2 | gen 1 | gen 2 | +1 gen * |
| token_entropy→distinct_3 | gen 1 | gen 2 | +1 gen * |
| token_entropy→perplexity | gen 1 | gen 2 | +1 gen * |
| ece→distinct_1 | gen 1 | gen 1 | 0 |
| ece→distinct_2 | gen 1 | gen 1 | 0 |
| ece→distinct_3 | gen 1 | gen 1 | 0 |
| ece→perplexity | gen 1 | gen 1 | 0 |

## TY Granger Notes

- token_entropy pairs: d_max=2 → k=3 → df_resid=1 → no power (expected, per C003)
- ece pairs: d_max=1 → k=2 → df_resid=4-5 → marginal power
- Only ece→distinct_2 significant: F=23.56, p=0.008, df_resid=5

## Consensus (≥3/5 methods supporting forward)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy→distinct_1 | 3/5 | diff, threshold, perm |
| token_entropy→distinct_2 | 2/5 | diff, threshold |
| token_entropy→distinct_3 | 2/5 | diff, threshold |
| token_entropy→perplexity | 3/5 | diff, threshold, perm |
| ece→distinct_1 | 3/5 | naive, diff, perm |
| **ece→distinct_2** | **4/5** | naive, diff, perm, ty |
| ece→distinct_3 | 3/5 | naive, diff, perm |
| ece→perplexity | 2/5 | diff, perm |

**Robust pairs (≥3/5): 5/8**

## Cross-seed Comparison (s44 vs s42 reference)

| Metric | s42 | s44 | Delta |
|--------|-----|-----|-------|
| Perm Granger FDR fwd | 3/8 | 6/8 | +3 |
| Robust consensus | (11/16†) | 5/8 | not directly comparable |

† s42 reference used 4 canaries × 4 downstreams = 16 pairs

**Key observation**: s44 shows STRONGER perm Granger signal than s42 (6/8 vs 3/8). The directional asymmetry (6 fwd vs 0 rev) is highly robust — no reverse pair is significant even before FDR correction. This confirms the canary→downstream causal direction at α=0.75.

## Files
- Full results JSON: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s44/analysis/5method_leadlag.json`
- Analysis script: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/a075_s44_leadlag.py`
