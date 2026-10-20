# D120 5-Method Lead-Lag Analysis: α=0.60 s42 fp32 v4

## Experiment
- **exp_id**: alpha_sweep_a060_s42_fp32_v4
- **Model**: Pythia-410M, seed=42, α=0.60, T=10 (11 gens), fp32
- **Server**: westd-17855
- **Data**: results/alpha_sweep/a060_s42_fp32_v4
- **Script**: run_5method_analysis_d102.py (n_perm=5000, threshold=true_3sigma_d105)

## Results Summary

| Method | Forward | Reverse |
|--------|---------|---------|
| PermG (FDR) | 0/8 | 0/8 |
| TY Granger | 0/8 | — |
| diff_xcorr (FDR) | 6/8 | 6/8 |
| naive_xcorr | 2/8 | — |
| threshold_onset_3sigma | 0/8 | — |

**K≥3: 0/8 | K≥4: 0/8 | Robust pairs: 0/8**

## Per-Pair Consensus

| Pair | K | Methods |
|------|---|---------|
| token_entropy→distinct_1 | 1/5 | diff |
| token_entropy→distinct_2 | 1/5 | diff |
| token_entropy→distinct_3 | 1/5 | diff |
| token_entropy→mauve | 1/5 | naive |
| ece→distinct_1 | 1/5 | diff |
| ece→distinct_2 | 1/5 | diff |
| ece→distinct_3 | 1/5 | diff |
| ece→mauve | 1/5 | naive |

## Interpretation

**Negative result.** α=0.60 at T=10 shows no robust multi-method lead-lag signal. PermG—the primary causal method—finds 0/8 significant pairs in both directions. diff_xcorr detects 6/8 forward correlations but this is not confirmed by any other method, yielding K=1 for all pairs.

This confirms the **non-monotonic sync dip** at α=0.60: despite being above the onset threshold [0.45, 0.50], the lead-lag signal collapses before recovering at α=0.75. Key comparison points:
- α=0.50 s42 fp32: PermG typically ≥5/8, K≥3 robust
- α=0.60 s42 fp32 v4: PermG 0/8, K≥3 = 0/8 ← **this experiment**
- α=0.75 s42 fp32: PermG recovers

This v4 result (clean fp32 standard params) replaces the v3_d080 variant (excluded per D125 for non-traceability) and will serve as the T=10 baseline for T=20 comparison at α=0.60.

## Conclusion
**negative** — No robust lead-lag at α=0.60 T=10.
