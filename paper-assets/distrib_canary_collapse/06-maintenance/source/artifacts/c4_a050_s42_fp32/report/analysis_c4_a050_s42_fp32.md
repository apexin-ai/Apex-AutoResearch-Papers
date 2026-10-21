# Analysis: c4_a050_s42_fp32

**Date**: 2026-05-19
**Server**: westd-17855
**Precision**: fp32
**Parent (bf16)**: alpha_sweep_c4_a050_s42_bf16

## Purpose

Determine whether the bf16 parent's PermG fwd=0/8 at C4 α=0.50 is a precision artifact or a true blind zone.

## Result Summary

**Conclusion: bf16 precision artifact confirmed.** fp32 rerun yields PermG fwd=8/8, K≥4=8/8. C4 α=0.50 has strong causal lead-lag signal; bf16 completely masked it.

## Training Completion

- EXIT_CODE=0 (normal exit)
- 11 generations (gen 0–10)
- All metrics computed, sentinel written

## Per-Generation Metrics

| Gen | token_entropy | distinct_1 | distinct_2 | distinct_3 | perplexity | mauve | ece |
|-----|--------------|------------|------------|------------|------------|-------|-----|
| 0 | 3.109 | 0.1149 | 0.5570 | 0.8388 | 24.01 | 0.829 | 0.012 |
| 1 | 2.327 | 0.1162 | 0.5571 | 0.8363 | 53.65 | 0.876 | 0.166 |
| 2 | 2.024 | 0.0987 | 0.4830 | 0.7562 | 112.74 | 0.494 | 0.260 |
| 3 | 1.831 | 0.0955 | 0.4583 | 0.7134 | 188.29 | 0.450 | 0.311 |
| 4 | 1.725 | 0.0951 | 0.4460 | 0.6873 | 260.55 | 0.367 | 0.339 |
| 5 | 1.679 | 0.0971 | 0.4469 | 0.6781 | 331.59 | 0.382 | 0.353 |
| 6 | 1.650 | 0.0990 | 0.4511 | 0.6785 | 407.93 | 0.420 | 0.364 |
| 7 | 1.626 | 0.1007 | 0.4579 | 0.6801 | 480.53 | 0.393 | 0.375 |
| 8 | 1.617 | 0.1020 | 0.4634 | 0.6858 | 559.26 | 0.402 | 0.383 |
| 9 | 1.610 | 0.1035 | 0.4698 | 0.6934 | 637.24 | 0.377 | 0.387 |
| 10 | 1.617 | 0.1037 | 0.4695 | 0.6899 | 727.95 | 0.379 | 0.390 |

## Drift (gen 0 → gen 10)

| Metric | gen 0 | gen 10 | Δ% |
|--------|-------|--------|-----|
| token_entropy | 3.109 | 1.617 | -48.0% |
| distinct_1 | 0.115 | 0.104 | -9.8% |
| distinct_2 | 0.557 | 0.469 | -15.7% |
| distinct_3 | 0.839 | 0.690 | -17.8% |
| perplexity | 24.01 | 727.95 | +2932% |
| mauve | 0.829 | 0.379 | -54.3% |
| ece | 0.012 | 0.390 | +3104% |
| effective_rank | 68.75 | 145.79 | +112.1% |

## Lead-Lag Analysis (D102: 8-pair, D105: 3σ, D106: PermG fwd)

### Method Summary

| Method | Sig/Total |
|--------|-----------|
| naive_xcorr | 8/8 |
| diff_xcorr (FDR) | 8/8 |
| threshold_onset (3σ) | 8/8 |
| **perm_granger_fwd (FDR)** | **8/8** |
| perm_granger_rev (FDR) | 7/8 |
| ty_granger | 4/8 |
| **consensus K≥4** | **8/8** |
| consensus K≥3 | 8/8 |

### Per-Pair Consensus

| Pair | K | Methods |
|------|---|---------|
| token_entropy→distinct_1 | 4 | naive, diff, thresh, pg_fwd |
| token_entropy→distinct_2 | 4 | naive, diff, thresh, pg_fwd |
| token_entropy→distinct_3 | 5 | naive, diff, thresh, pg_fwd, ty |
| token_entropy→mauve | 5 | naive, diff, thresh, pg_fwd, ty |
| ece→distinct_1 | 4 | naive, diff, thresh, pg_fwd |
| ece→distinct_2 | 4 | naive, diff, thresh, pg_fwd |
| ece→distinct_3 | 5 | naive, diff, thresh, pg_fwd, ty |
| ece→mauve | 5 | naive, diff, thresh, pg_fwd, ty |

### Threshold Onset (3σ)

All 8 pairs: canary onset at gen 1, downstream onset at gen 2–3 (lead time 1–2 gens).

### PermG Forward (FDR-corrected)

| Pair | F-stat | p_fdr |
|------|--------|-------|
| token_entropy→distinct_1 | 157.41 | 0.0036 |
| ece→distinct_3 | 229.43 | 0.0028 |
| ece→mauve | 153.78 | 0.0029 |
| (all 8 pairs significant) | | |

## bf16 vs fp32 Comparison

| Metric | bf16 parent | fp32 (this) |
|--------|-------------|-------------|
| token_entropy (gen 0) | 3.136 | 3.109 |
| token_entropy (final) | 1.94 | 1.617 |
| token_entropy Δ% | -38.2% | -48.0% |
| distinct_1 Δ% | -20.3% | -9.8% |
| perplexity (final) | 122.8 | 727.95 |
| mauve (final) | 0.078 | 0.379 |
| ece (final) | 0.259 | 0.390 |
| **PermG fwd** | **0/8** | **8/8** |
| **PermG rev** | **0/8** | **7/8** |
| **K≥4** | **0/8** | **8/8** |

## Interpretation

1. **bf16 precision artifact confirmed**: The complete flip from 0/8 to 8/8 on PermG fwd (D106 primary metric) demonstrates that bf16 numerical precision destroyed the causal signal at C4 α=0.50. This validates D079 (fp32 mandatory for ≤3B models).

2. **C4 α=0.50 is NOT a blind zone**: Strong causal lead-lag exists across all 8 canary-diversity pairs. Canaries (token_entropy, ece) lead downstream diversity metrics (d1–d3, mauve) by 1–2 generations at the 3σ threshold.

3. **Dynamics differ in fp32**: fp32 shows deeper collapse (entropy -48% vs -38%, ppl +2932% vs +402%) but paradoxically higher remaining mauve (0.379 vs 0.078). This suggests bf16 introduced different collapse dynamics, not just masking the signal.

4. **Dose-response regime map update**: C4 α=0.50 should be reclassified from "blind zone / no signal" to "active signal with strong causal structure." Any other bf16-only 0/8 results at moderate α values are candidates for fp32 reruns.

## Files

- Results: `westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32/`
- Analysis: `westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32/analysis_results.json`
- Log: `westd-17855:/root/runs/distrib_canary_collapse/c4_a050_s42_fp32.log`
