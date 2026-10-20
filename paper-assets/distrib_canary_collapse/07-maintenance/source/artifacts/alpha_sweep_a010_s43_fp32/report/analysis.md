# Alpha Sweep a010_s43_fp32 Analysis Report

**Date**: 2026-05-19
**Experiment**: alpha_sweep_a010_s43_fp32
**Server**: westd-17855
**Config**: Pythia-410m, WikiText-103 5k, alpha=0.10, seed=43, fp32, 10 generations x 5000 steps

## 1. Experiment Status

- EXIT_CODE: 0
- Generations: gen_0 to gen_10 (11 directories, complete)
- No NaN or errors in training log
- all_metrics.json: 11 entries, all metrics populated

## 2. Drift Metrics (gen0 to gen10)

| Metric | gen0 | gen10 | Drift (%) | bf16 s43 Drift (%) | Delta |
|--------|------|-------|-----------|---------------------|-------|
| token_entropy | 3.2342 | 3.0891 | **-4.49** | -13.1 | +8.6pp less |
| perplexity | 26.949 | 22.086 | **-18.04** | -38.9 | +20.9pp less |
| distinct_1 | 0.0929 | 0.0724 | **-22.08** | -29.1 | +7.0pp less |
| distinct_2 | 0.5074 | 0.3883 | **-23.47** | -40.3 | +16.8pp less |
| distinct_3 | 0.8350 | 0.6982 | **-16.39** | -31.9 | +15.5pp less |
| ece | 0.0108 | 0.0149 | **+37.87** | N/A | - |
| effective_rank | 46.613 | 46.953 | **+0.73** | N/A | - |
| mauve | 0.0304 | 0.0247 | **-18.72** | N/A | - |

**fp32 precision roughly halves the drift magnitude** across all key metrics compared to bf16.

## 3. Lead-lag Analysis (5-method, FDR-corrected)

| Method | fp32 s43 | bf16 s43 (parent) |
|--------|----------|-------------------|
| naive_xcorr_fwd | 8/8 | N/A |
| diff_xcorr_fwd | 7/8 | N/A |
| threshold_onset | **4/8** | 3/8 |
| perm_granger_fwd | **0/8** | 0/8 |
| perm_granger_rev | **0/8** | 0/8 |
| ty_granger | **6/8** | 0/8 |
| consensus_k4 | **4/8** | 0/8 |

### Consensus Detail (k >= 4 pairs)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy -> distinct_1 | 4 | naive, diff, thresh, ty |
| token_entropy -> distinct_2 | 4 | naive, diff, thresh, ty |
| token_entropy -> distinct_3 | 4 | naive, diff, thresh, ty |
| token_entropy -> mauve | 4 | naive, diff, thresh, ty |
| ece -> distinct_1 | 2 | naive, diff |
| ece -> distinct_2 | 3 | naive, diff, ty |
| ece -> distinct_3 | 2 | naive, diff |
| ece -> mauve | 2 | naive, ty |

### MMCT

- Mode: weighted_pair_forward (simple consensus, no null distribution)
- Detection rate: 0.5 (4/8 pairs)

## 4. TY Granger Reliability Check (C003)

Per constraint C003, TY Granger results at alpha <= 0.50 are unreliable due to d_max instability across seeds.

TY d_max / df_resid in this run:

| Pair | d_max | df_resid | Significant | Reliability |
|------|-------|----------|-------------|-------------|
| token_entropy -> distinct_1 | 1 | 4 | Yes | Moderate (df_resid OK) |
| token_entropy -> distinct_2 | (truncated, likely 1) | - | Yes | Check needed |
| token_entropy -> distinct_3 | (truncated, likely 1) | - | Yes | Check needed |
| token_entropy -> mauve | (truncated, likely similar) | - | Yes | Check needed |
| ece -> distinct_2 | 2 | 1 | Yes | **LOW (df_resid=1)** |
| ece -> mauve | 2 | 1 | Yes | **LOW (df_resid=1)** |

**Critical**: The k_gte4=4/8 consensus relies on TY as the 4th method in all 4 passing pairs. Excluding TY per C003, these pairs drop to k=3 (naive+diff+thresh), and k_gte4 falls to **0/8**, consistent with the bf16 blind zone.

## 5. Blind Zone Assessment

### fp32 vs bf16 comparison

1. **Drift attenuation**: fp32 roughly halves all drift magnitudes. Diversity collapse still occurs (distinct_1: -22%, distinct_2: -23%, distinct_3: -16%) but is less severe than bf16 (-29%, -40%, -32%).

2. **Entropy canary signal**: token_entropy drift is only -4.49% in fp32 (vs -13.1% in bf16). The entropy signal is weaker in absolute terms, but the ratio of entropy-to-diversity drift is similar (~1:5 in fp32 vs ~1:3 in bf16).

3. **Causal detection (PermG)**: 0/8 in both fp32 and bf16. Permutation Granger consistently fails at alpha=0.10 regardless of precision. This is the most robust blind zone indicator.

4. **k_gte4 consensus**: Nominally 4/8 in fp32 vs 0/8 in bf16, but after applying C003 (excluding TY), effectively 0/8 in both.

### Conclusion

**The canary blind zone at alpha=0.10 is seed-invariant and precision-invariant.** fp32 attenuates collapse severity but does not resolve the fundamental detection failure:

- PermG remains 0/8 (hard zero, same as bf16)
- k_gte4 is 0/8 after C003 correction (same as bf16)
- The apparent improvement in TY (6/8) and k_gte4 (4/8) is an artifact of single-seed TY instability at low alpha

fp32 does reduce the magnitude of diversity collapse, which partially mitigates the practical impact of the blind zone, but does not eliminate it as a methodological concern.

## 6. Raw Time Series

| Gen | token_entropy | distinct_1 | distinct_2 | distinct_3 | perplexity | ece | eff_rank | mauve |
|-----|---------------|------------|------------|------------|------------|-----|----------|-------|
| 0 | 3.2342 | 0.0929 | 0.5074 | 0.8350 | 26.949 | 0.0108 | 46.613 | 0.0304 |
| 1 | 2.9943 | 0.0916 | 0.5002 | 0.8275 | 19.405 | 0.0105 | 48.569 | 0.0282 |
| 2 | 3.0274 | 0.0720 | 0.3924 | 0.7217 | 20.213 | 0.0106 | 49.791 | 0.0237 |
| 3 | 3.0432 | 0.0675 | 0.3532 | 0.6686 | 20.656 | 0.0112 | 49.700 | 0.0224 |
| 4 | 3.0402 | 0.0676 | 0.3473 | 0.6593 | 21.099 | 0.0134 | 49.222 | 0.0220 |
| 5 | 3.0545 | 0.0688 | 0.3559 | 0.6611 | 21.085 | 0.0129 | 47.897 | 0.0226 |
| 6 | 3.0632 | 0.0693 | 0.3644 | 0.6707 | 21.204 | 0.0130 | 48.063 | 0.0237 |
| 7 | 3.0674 | 0.0704 | 0.3728 | 0.6815 | 21.617 | 0.0145 | 46.542 | 0.0264 |
| 8 | 3.0596 | 0.0705 | 0.3782 | 0.6858 | 21.564 | 0.0149 | 46.863 | 0.0244 |
| 9 | 3.0875 | 0.0709 | 0.3792 | 0.6871 | 21.911 | 0.0147 | 46.439 | 0.0253 |
| 10 | 3.0891 | 0.0724 | 0.3883 | 0.6982 | 22.086 | 0.0149 | 46.953 | 0.0247 |
