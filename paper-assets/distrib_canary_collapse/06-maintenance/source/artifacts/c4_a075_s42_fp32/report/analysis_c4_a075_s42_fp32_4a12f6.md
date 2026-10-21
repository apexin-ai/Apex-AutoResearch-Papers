# Analysis Report: c4_a075_s42_fp32

**Experiment**: C4 5k, Pythia-410m, α=0.75, seed=42, fp32
**Hypothesis**: Claim 2 cross-domain validation — C4 dataset α=0.75 regime boundary fp32
**Parent**: alpha_sweep_a075_s42_fp32 (WikiText α=0.75)
**Date**: 2026-05-19

## 1. Metric Drift (Gen0 → Gen10)

| Metric | Gen0 | Gen10 | Drift% |
|--------|------|-------|--------|
| token_entropy | 3.1094 | 2.0110 | **-35.32%** |
| ece | 0.0122 | 0.3545 | **+2809.23%** |
| perplexity | 24.01 | 540.90 | **+2152.60%** |
| distinct_1 | 0.1149 | 0.1007 | -12.40% |
| distinct_2 | 0.5570 | 0.4712 | -15.41% |
| distinct_3 | 0.8388 | 0.7164 | -14.59% |
| effective_rank | 68.75 | 144.59 | +110.31% |
| mauve | 0.8286 | 0.4785 | **-42.26%** |

## 2. Per-Method Significance Rates (8 pairs, BH FDR q=0.05)

| Method | Sig/Total | Notes |
|--------|-----------|-------|
| naive_xcorr | **8/8** | All peak_lag = -1 (canary leads) |
| diff_xcorr | **8/8** | FDR-corrected |
| threshold_onset (3σ) | **8/8** | Canary onset gen 1, downstream gen 2-4 |
| perm_granger_fwd | **8/8** | FDR-corrected, n_perm=5000 |
| perm_granger_rev | **0/8** | Perfect asymmetry |
| ty_granger | **6/8** | Non-sig: *→distinct_1 pairs (d_max=1, df_resid=4) |

## 3. Per-Pair Consensus (5 methods: naive, diff, threshold, pg_fwd, TY)

| Pair | K | Methods Significant |
|------|---|---------------------|
| token_entropy → distinct_1 | 4 | naive, diff, thresh, pg_fwd |
| token_entropy → distinct_2 | 5 | naive, diff, thresh, pg_fwd, ty |
| token_entropy → distinct_3 | 5 | naive, diff, thresh, pg_fwd, ty |
| token_entropy → mauve | 5 | naive, diff, thresh, pg_fwd, ty |
| ece → distinct_1 | 4 | naive, diff, thresh, pg_fwd |
| ece → distinct_2 | 5 | naive, diff, thresh, pg_fwd, ty |
| ece → distinct_3 | 5 | naive, diff, thresh, pg_fwd, ty |
| ece → mauve | 5 | naive, diff, thresh, pg_fwd, ty |

**K≥3 (3σ): 8/8** | **K≥4 (3σ): 8/8**

## 4. Parent Comparison (WikiText α=0.75 vs C4 α=0.75)

| Metric | WikiText (parent) | C4 (this) | Delta |
|--------|-------------------|-----------|-------|
| PermG_fwd | 6/8 | **8/8** | +2 |
| PermG_rev | 0/8 | 0/8 | = |
| K≥4 (3σ) | 6/8 | **8/8** | +2 |
| threshold_onset (3σ) | 8/8 | 8/8 | = |
| TY_granger | 8/8 | 6/8 | -2 |
| entropy drift | -29.41% | **-35.32%** | stronger |
| d1 drift | -25.38% | -12.40% | weaker |
| ppl drift | +188.31% | **+2152.60%** | much stronger |

## 5. Key Observations

1. **Stronger signal on C4**: PermG_fwd improves from 6/8 (WikiText) to 8/8 (C4), K≥4 also 6/8→8/8. Cross-domain generalization confirmed with amplification.

2. **Perfect directional asymmetry**: PermG_fwd=8/8, Rev=0/8. Canary→downstream causality is strictly unidirectional on C4, consistent with WikiText.

3. **Extreme calibration/perplexity drift**: ECE drift +2809% and perplexity +2152% on C4 vs +188% ppl on WikiText. C4's larger vocabulary and domain diversity amplifies model collapse effects.

4. **Weaker diversity drift**: distinct_1 drops only 12.4% on C4 vs 25.4% on WikiText, yet lead-lag signal is stronger. This suggests the canary lead-lag mechanism is robust even when downstream degradation magnitude varies.

5. **TY Granger miss on distinct_1**: Both canary→distinct_1 pairs have TY non-significant (d_max=1, df_resid=4). Known limitation per C003 — T=11 gives minimal degrees of freedom when d_max>0.

6. **threshold_onset 3σ at 8/8**: Unlike many experiments where 3σ threshold_onset has low power, C4 α=0.75 achieves full detection. Canary onset consistently at gen 1, downstream onset at gen 2-4.

## 6. Conclusion

**SUCCESS**. C4 α=0.75 fp32 validates cross-domain generalization of canary lead-lag at the regime boundary. Signal is stronger than the WikiText parent on the primary metric (PermG_fwd 8/8 vs 6/8). All 8 pairs achieve K≥4 consensus under true 3σ threshold.

## Parameters

- n_perm: 5000
- xcorr_lag: 5
- granger_lag: 1
- threshold: 3σ (D105)
- FDR: per-method BH q=0.05 (D086)
- Server: westd-17855
- Analysis script: batch_analysis.py
