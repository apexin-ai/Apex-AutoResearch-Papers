# D111 Direction Check — Full Sweep (9 α values)

**Date**: 2026-05-19
**Rule**: naive_xcorr and diff_xcorr require `peak_lag > 0` for forward direction (D111).
**Scope**: 9 WikiText α values: 0.00, 0.05, 0.10, 0.25, 0.35, 0.50, 0.60, 0.75, 1.00

## Per-α Summary

| α | naive (old→new) | diff (old→new) | K≥3 (old→new) | K≥4 (old→new) | need_update? |
|---|-----------------|----------------|----------------|----------------|-------------|
| 0.00 | 1.000→0.750 | 0.500→0.000 | 0.375→0.125 | 0.000→0.000 | Y |
| 0.05 | 0.875→0.375 | 0.375→0.000 | 0.375→0.000 | 0.000→0.000 | Y |
| 0.10 | 0.875→0.500 | 0.750→0.125 | 0.500→0.250 | 0.250→0.000 | Y |
| 0.25 | 1.000→0.625 | 0.375→0.250 | 0.500→0.250 | 0.000→0.000 | Y |
| 0.35 | 1.000→1.000 | 0.500→0.000 | 0.750→0.500 | 0.250→0.000 | Y |
| 0.50 | 1.000→0.625 | 0.875→0.125 | 0.875→0.625 | 0.750→0.250 | Y |
| 0.60 | 0.875→0.500 | 1.000→0.000 | 1.000→0.750 | 0.875→0.125 | Y |
| 0.75 | 0.875→0.000 | 0.750→0.000 | 0.875→0.750 | 0.750→0.000 | Y |
| 1.00 | 1.000→0.000 | 0.750→0.000 | 0.750→0.750 | 0.750→0.000 | Y |

**Note**: "old" = CSV values before this audit (sig-only, no direction check). "new" = D111-corrected (sig AND peak_lag > 0).

### Key observations

1. **diff_fwd is 0.000 for 7/9 α values** — almost all significant diff_xcorr peaks occur at negative lags (reverse direction).
2. **α=0.75 and α=1.00: naive_fwd = 0.000** — all significant naive peaks also at negative lags. At high contamination, cross-correlation consistently peaks in the reverse direction.
3. **α=0.35 is the only α where naive_fwd = 1.000** — all 8 naive peaks at positive lags.
4. **K≥4 drops to 0.000 for 7/9 α values** — only α=0.50 (0.250) and α=0.60 (0.125) retain K≥4 evidence after direction correction.
5. **K≥3 remains ≥ 0.625 for α≥0.50** — threshold/permG/TY sustain consensus even without naive/diff forward evidence.

### Discrepancy note (α=0.00)

The α=0.00 analysis file (`a000_s42/analysis/5method_leadlag.json`) yields threshold_rate=0.375 and TY_rate=0.125, which differ from the CSV's 0.500 and 0.250. The CSV may have been generated from a different analysis version. K values for α=0.00 in this audit are computed from the `analysis/5method_leadlag.json` data.

---

## Per-α Detail

### α=0.00 (results/alpha_sweep/a000_s42, westd-19828)

Source: `analysis/5method_leadlag.json`

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K_new |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|-------|
| te→d1 | -5 | T | **F** | -1 | T | **F** | F | F | F | 0 |
| te→d2 | 2 | T | T | -4 | T | **F** | F | F | F | 1 |
| te→d3 | 2 | T | T | -4 | T | **F** | F | F | F | 1 |
| te→mauve | 2 | T | T | 5 | F | F | F | F | F | 1 |
| ece→d1 | -4 | T | **F** | 2 | F | F | T | F | F | 1 |
| ece→d2 | 4 | T | T | 2 | F | F | T | F | F | 2 |
| ece→d3 | 4 | T | T | -3 | F | F | T | F | T | 3 |
| ece→mauve | 4 | T | T | -3 | T | **F** | F | F | F | 1 |

**naive_fwd**: 6/8=0.750 (was 1.000). **diff_fwd**: 0/8=0.000 (was 0.500). **K≥3**: 1/8=0.125. **K≥4**: 0/8=0.000.

### α=0.05 (results/alpha_sweep/a005_s42_fp32_v3_d080, westd-17855)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K_new |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|-------|
| te→d1 | -1 | T | **F** | -2 | T | **F** | T | F | F | 1 |
| te→d2 | -2 | T | **F** | -2 | T | **F** | T | F | F | 1 |
| te→d3 | -2 | T | **F** | -2 | T | **F** | T | F | F | 1 |
| te→mauve | 5 | T | T | -2 | F | F | T | F | F | 2 |
| ece→d1 | 1 | T | T | 5 | F | F | F | F | F | 1 |
| ece→d2 | -4 | T | **F** | -4 | F | F | F | F | T | 1 |
| ece→d3 | 1 | T | T | -4 | F | F | F | F | T | 2 |
| ece→mauve | 4 | F | F | -2 | F | F | T | F | T | 2 |

**naive_fwd**: 3/8=0.375 (was 0.875). **diff_fwd**: 0/8=0.000 (was 0.375). **K≥3**: 0/8=0.000. **K≥4**: 0/8=0.000.

### α=0.10 (results/alpha_sweep/a010_s42_fp32, westd-17855)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K_new |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|-------|
| te→d1 | -2 | T | **F** | -1 | T | **F** | T | F | F | 1 |
| te→d2 | -2 | T | **F** | -1 | T | **F** | T | F | T | 2 |
| te→d3 | 4 | T | T | -3 | T | **F** | T | F | T | 3 |
| te→mauve | 4 | F | F | 5 | T | T | T | F | T | 3 |
| ece→d1 | 3 | T | T | -4 | T | **F** | F | F | F | 1 |
| ece→d2 | 3 | T | T | -3 | T | **F** | F | F | F | 1 |
| ece→d3 | 2 | T | T | 5 | F | F | F | F | F | 1 |
| ece→mauve | -3 | T | **F** | 2 | F | F | T | F | F | 1 |

**naive_fwd**: 4/8=0.500 (was 0.875). **diff_fwd**: 1/8=0.125 (was 0.750). **K≥3**: 2/8=0.250. **K≥4**: 0/8=0.000.

### α=0.25 (results/alpha_sweep/a025_s42_fp32, westd-17855)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K_new |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|-------|
| te→d1 | 1 | T | T | -1 | T | **F** | T | F | F | 2 |
| te→d2 | 1 | T | T | -3 | F | F | T | F | T | 3 |
| te→d3 | 1 | T | T | -3 | F | F | T | F | F | 2 |
| te→mauve | 2 | T | T | 5 | F | F | T | F | T | 3 |
| ece→d1 | 1 | T | T | 4 | F | F | F | F | F | 1 |
| ece→d2 | 0 | T | **F** | 4 | T | T | F | F | F | 1 |
| ece→d3 | 0 | T | **F** | 4 | T | T | F | F | F | 1 |
| ece→mauve | -2 | T | **F** | -4 | F | F | T | F | T | 2 |

**naive_fwd**: 5/8=0.625 (was 1.000). **diff_fwd**: 2/8=0.250 (was 0.375). **K≥3**: 2/8=0.250. **K≥4**: 0/8=0.000.

### α=0.35 (results/alpha_sweep/a035_s42_fp32, westd-17855)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K_new |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|-------|
| te→d1 | 1 | T | T | -1 | T | **F** | T | F | T | 3 |
| te→d2 | 1 | T | T | -1 | T | **F** | T | F | F | 2 |
| te→d3 | 5 | T | T | 5 | F | F | T | F | F | 2 |
| te→mauve | 1 | T | T | 4 | F | F | T | F | T | 3 |
| ece→d1 | 3 | T | T | -1 | T | **F** | T | F | T | 3 |
| ece→d2 | 3 | T | T | -1 | T | **F** | T | F | F | 2 |
| ece→d3 | 3 | T | T | -3 | F | F | T | F | F | 2 |
| ece→mauve | 2 | T | T | 5 | F | F | T | F | T | 3 |

**naive_fwd**: 8/8=1.000 (unchanged). **diff_fwd**: 0/8=0.000 (was 0.500). **K≥3**: 4/8=0.500. **K≥4**: 0/8=0.000.

### α=0.50 (results/alpha_sweep/a050_s42_fp32, westd-17855)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K_new |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|-------|
| te→d1 | 5 | T | T | -2 | T | **F** | T | T | F | 3 |
| te→d2 | 5 | T | T | -2 | T | **F** | T | T | T | 4 |
| te→d3 | 4 | T | T | -2 | T | **F** | T | T | T | 4 |
| te→mauve | 4 | T | T | 4 | T | T | T | F | F | 3 |
| ece→d1 | -1 | T | **F** | -1 | T | **F** | T | T | F | 2 |
| ece→d2 | -1 | T | **F** | -2 | T | **F** | T | T | T | 3 |
| ece→d3 | -1 | T | **F** | -2 | T | **F** | T | T | T | 3 |
| ece→mauve | 2 | T | T | 5 | F | F | T | F | F | 2 |

**naive_fwd**: 5/8=0.625 (was 1.000). **diff_fwd**: 1/8=0.125 (was 0.875). **K≥3**: 5/8=0.625. **K≥4**: 2/8=0.250.

### α=0.60 (results/alpha_sweep/a060_s42_fp32_v3_d080, westd-17855)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K_new |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|-------|
| te→d1 | 5 | T | T | -1 | T | **F** | T | T | T | 4 |
| te→d2 | 5 | T | T | -2 | T | **F** | T | F | T | 3 |
| te→d3 | 5 | T | T | -3 | T | **F** | T | F | T | 3 |
| te→mauve | 5 | T | T | -5 | T | **F** | T | F | T | 3 |
| ece→d1 | -1 | T | **F** | -1 | T | **F** | T | T | T | 3 |
| ece→d2 | -1 | T | **F** | -2 | T | **F** | T | T | T | 3 |
| ece→d3 | -5 | F | F | -3 | T | **F** | T | F | T | 2 |
| ece→mauve | -1 | T | **F** | -5 | T | **F** | T | F | T | 2 |

**naive_fwd**: 4/8=0.500 (was 0.875). **diff_fwd**: 0/8=0.000 (was 1.000). **K≥3**: 6/8=0.750. **K≥4**: 1/8=0.125.

### α=0.75 (results/alpha_sweep/a075_s42_fp32, westd-17855)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K_new |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|-------|
| te→d1 | -5 | T | **F** | -5 | T | **F** | T | T | T | 3 |
| te→d2 | -5 | T | **F** | -5 | T | **F** | T | T | T | 3 |
| te→d3 | -5 | T | **F** | -5 | T | **F** | T | T | T | 3 |
| te→mauve | -5 | F | F | -4 | F | F | T | F | T | 2 |
| ece→d1 | -3 | T | **F** | -1 | T | **F** | T | T | T | 3 |
| ece→d2 | -4 | T | **F** | -4 | T | **F** | T | T | T | 3 |
| ece→d3 | -4 | T | **F** | -4 | T | **F** | T | T | T | 3 |
| ece→mauve | -5 | T | **F** | -4 | F | F | T | F | T | 2 |

**naive_fwd**: 0/8=0.000 (was 0.875). **diff_fwd**: 0/8=0.000 (was 0.750). **K≥3**: 6/8=0.750. **K≥4**: 0/8=0.000.

### α=1.00 (results/padding_robustness/a100_s42_fp32, westd-17855)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh | permG | TY | K_new |
|------|-----------|-----------|-----------|----------|--------------|----------|--------|-------|----|-------|
| te→d1 | -1 | T | **F** | -1 | T | **F** | T | T | T | 3 |
| te→d2 | -1 | T | **F** | -1 | T | **F** | T | T | T | 3 |
| te→d3 | -2 | T | **F** | -2 | T | **F** | T | T | T | 3 |
| te→mauve | -4 | F | F | -5 | F | F | T | F | F | 1 |
| ece→d1 | -2 | T | **F** | -2 | T | **F** | T | T | T | 3 |
| ece→d2 | -3 | T | **F** | -1 | T | **F** | T | T | T | 3 |
| ece→d3 | -3 | T | **F** | -1 | T | **F** | T | T | T | 3 |
| ece→mauve | -4 | F | F | -5 | F | F | T | F | F | 1 |

**naive_fwd**: 0/8=0.000 (was 1.000). **diff_fwd**: 0/8=0.000 (was 0.750). **K≥3**: 6/8=0.750 (unchanged). **K≥4**: 0/8=0.000 (was 0.750).

---

## Impact on dose-response narrative

After D111 correction:
- **Null regime (α=0.00-0.25)**: naive_fwd drops to 0.375-0.625, diff_fwd drops to 0.000-0.250. K≥3 = 0.000-0.250. Cross-correlation evidence is largely direction-inconsistent.
- **Transition (α=0.35)**: naive_fwd=1.000 (all positive lags), diff_fwd=0.000. K≥3=0.500 sustained by threshold+TY.
- **Onset (α=0.50)**: K≥3=0.625, K≥4=0.250. PermG+threshold+TY carry the consensus; naive contributes, diff does not.
- **Sync-collapse (α=0.60)**: K≥3=0.750, K≥4=0.125. Same pattern.
- **Detection (α=0.75, 1.00)**: naive_fwd=0.000, diff_fwd=0.000. ALL cross-correlation peaks at negative lags. K≥3=0.750 sustained entirely by threshold+permG+TY.

The direction check reveals that cross-correlation (both naive and diff) systematically peaks at negative lags for high α — the downstream metric change appears to precede the canary metric change in the cross-correlation function. Forward causal evidence at high α comes exclusively from threshold onset, permutation Granger, and Toda-Yamamoto.
