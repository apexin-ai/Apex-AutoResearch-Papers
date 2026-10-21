# D102 5-Method Analysis: t10_a075_s43_fp32

| Field | Value |
|-------|-------|
| α | 0.75 |
| seed | 43 |
| T | 10 |
| n_gens | 11 (gen_0–gen_10) |
| threshold | true_3sigma_d105 |
| server | westd-17855 |

## Summary

| Method | Forward | Reverse |
|--------|---------|---------|
| PermG FDR | **6/8** | 0/8 |
| Diff xcorr FDR | 7/8 | 7/8 |
| Threshold onset | 0/8 | — |
| TY Granger | 0/8 | — |
| Robust (≥3/5) | **4/8** | — |

## Consensus (forward direction)

| Pair | K | Methods |
|------|---|---------|
| token_entropy→distinct_1 | 3/5 | naive, diff, perm |
| token_entropy→distinct_2 | 2/5 | diff, perm |
| token_entropy→distinct_3 | 2/5 | diff, perm |
| token_entropy→mauve | 1/5 | diff |
| ece→distinct_1 | 3/5 | naive, diff, perm |
| ece→distinct_2 | 3/5 | naive, diff, perm |
| ece→distinct_3 | 3/5 | naive, diff, perm |
| ece→mauve | 0/5 | — |

## Cross-Seed Comparison

| Seed | PermG fwd | PermG rev | Robust ≥3 |
|------|-----------|-----------|-----------|
| s42 | 6/8 | 0/8 | — |
| s43 | 6/8 | 0/8 | 4/8 |

**Cross-seed robust**: s43 PermG=6/8 matches s42 exactly. Strong asymmetry (fwd≫rev) preserved.

## Key Observations
- PermG detects 6/8 forward pairs (all except mauve pairs), 0/8 reverse → strong directional asymmetry
- mauve pairs resist detection (PermG p_fdr > 0.47 for both canaries)
- 6/8 ceiling consistent with all α=0.75 experiments across T=10/15/20/25
- Threshold onset = 0/8 because 3sigma onsets not reached in T=10 window
- TY Granger = 0/8 (expected for T=10, short series)
