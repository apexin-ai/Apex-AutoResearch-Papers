# 5-Method Lead-Lag Analysis: Intervention Experiments

## Configuration
- Methods: naive_xcorr, diff_xcorr, threshold_onset, perm_granger (n_perm=5000, FDR-corrected), ty_granger
- 8 pairs: {token_entropy, ece} x {distinct_1, distinct_2, distinct_3, perplexity}
- xcorr_lag=5, granger_lag=1, FDR alpha=0.05 (Benjamini-Hochberg)
- All experiments: Pythia-410M, alpha=1.0, 11 generations

## Summary Table

| Experiment | Seed | Prec | Trigger | Naive | Diff (FDR) | Threshold | PermG (FDR) | TY | K>=3/5 | K>=4/5 |
|------------|------|------|---------|-------|------------|-----------|-------------|-----|--------|--------|
| Predictive s42 | 42 | fp32 | gen 1 | 0/8 | 8/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |
| Reactive s42 | 42 | fp32 | gen 2 | 8/8 | 8/8 | 0/8 | 8/8 | 8/8 | 8/8 | 4/8 |
| Predictive s43 | 43 | bf16 | gen 1 | 8/8 | 7/8 | 0/8 | 8/8 | 6/8 | 8/8 | 6/8 |
| Reactive s43 | 43 | bf16 | gen 2 | 7/8 | 8/8 | 4/8 | 5/8 | 3/8 | 8/8 | 3/8 |

Values show forward significance count (canary leads downstream) out of 8 pairs.

## Per-Pair Consensus Detail

### Predictive s42 (fp32, trigger gen 1)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy -> distinct_1 | 1/5 | diff |
| token_entropy -> distinct_2 | 1/5 | diff |
| token_entropy -> distinct_3 | 1/5 | diff |
| token_entropy -> perplexity | 1/5 | diff |
| ece -> distinct_1 | 1/5 | diff |
| ece -> distinct_2 | 1/5 | diff |
| ece -> distinct_3 | 2/5 | naive, diff |
| ece -> perplexity | 1/5 | diff |

Interpretation: The V-shaped trajectory (collapse gen 0-1, recovery gen 2+) weakens correlation-based methods. Only diff_xcorr captures the co-movement in first differences. Perm Granger and TY Granger are non-significant after FDR correction, likely because the early intervention (gen 1) truncates the monotonic collapse trajectory that these tests require.

### Reactive s42 (fp32, trigger gen 2)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy -> distinct_1 | 4/5 | naive, diff, perm, ty |
| token_entropy -> distinct_2 | 3/5 | diff, perm, ty |
| token_entropy -> distinct_3 | 3/5 | diff, perm, ty |
| token_entropy -> perplexity | 3/5 | diff, perm, ty |
| ece -> distinct_1 | 4/5 | naive, diff, perm, ty |
| ece -> distinct_2 | 3/5 | diff, perm, ty |
| ece -> distinct_3 | 3/5 | diff, perm, ty |
| ece -> perplexity | 3/5 | diff, perm, ty |

Interpretation: Strong canary-leads-downstream signal across all pairs. The 2-gen monotonic collapse (gen 0-2) before intervention gives sufficient trajectory for Granger methods to detect lead. All 8/8 pairs have PermG FDR-significant forward, 0/8 reverse, confirming directional causality.

### Predictive s43 (bf16, trigger gen 1)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy -> distinct_1 | 4/5 | naive, diff, pg, ty |
| token_entropy -> distinct_2 | 4/5 | naive, diff, pg, ty |
| token_entropy -> distinct_3 | 4/5 | naive, diff, pg, ty |
| token_entropy -> perplexity | 3/5 | naive, diff, pg |
| ece -> distinct_1 | 4/5 | naive, diff, pg, ty |
| ece -> distinct_2 | 4/5 | naive, diff, pg, ty |
| ece -> distinct_3 | 4/5 | naive, diff, pg, ty |
| ece -> perplexity | 2/5 | naive, pg |

Interpretation: Stronger signal than s42 predictive despite also triggering at gen 1. The bf16 precision and different seed produce a V-shape where the canary-downstream co-movement is more pronounced. 8/8 PermG FDR-significant forward vs 0/8 reverse.

### Reactive s43 (bf16, trigger gen 2)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy -> distinct_1 | 4/5 | naive, diff, thresh, pg |
| token_entropy -> distinct_2 | 4/5 | naive, diff, thresh, pg |
| token_entropy -> distinct_3 | 3/5 | naive, diff, thresh |
| token_entropy -> perplexity | 3/5 | diff, thresh, ty |
| ece -> distinct_1 | 4/5 | naive, diff, pg, ty |
| ece -> distinct_2 | 3/5 | naive, diff, pg |
| ece -> distinct_3 | 3/5 | naive, diff, pg |
| ece -> perplexity | 3/5 | naive, diff, ty |

Interpretation: All 8/8 pairs reach K>=3 consensus. Threshold_onset contributes in 4 pairs (only reactive s43 produces this). PermG FDR-significant in 5/8 forward, 0/8 reverse.

## Cross-Experiment Patterns

1. **Threshold onset never fires in predictive experiments** (0/8 across both seeds): intervention at gen 1 prevents the canary from crossing the 3-sigma drift threshold.

2. **Reactive experiments show stronger forward-only directionality**: PermG forward >> reverse in all cases, consistent with the canary-leads-downstream causal structure of model collapse.

3. **Seed/precision affects lead-lag detectability**: s43 bf16 predictive shows much stronger signal than s42 fp32 predictive (6/8 vs 0/8 K>=4). The shallower V-shape in bf16 may produce a more detectable co-movement pattern.

4. **Diff xcorr is the most robust single method**: 31/32 pair-experiments significant (only missing 1 pair in s43 predictive). Its first-differencing makes it well-suited for non-monotonic (V-shaped) trajectories.

## Data Sources
- predictive_te_s42: westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/intervention/predictive_te_s42/analysis/5method_leadlag.json
- reactive_d1_s42: westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/intervention/reactive_d1_s42/analysis/5method_leadlag.json
- predictive_te_s43_bf16: westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/intervention/predictive_te_s43_bf16/analysis/5method_leadlag.json
- reactive_d1_s43_bf16: westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/intervention/reactive_d1_s43_bf16/analysis/5method_leadlag.json
