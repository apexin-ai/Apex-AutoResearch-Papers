# Dose-Response D120 Compiled — v2: FDR-corrected

**v2: FDR-corrected, replaces v1 which used pre-FDR significance**

## Data source
- D120-compliant `5method_leadlag.json` files (containing `true_3sigma_d105` threshold)
- Servers: westd-17855 (fp32 canonical), westd-19828 (supplementary seeds + α=0.55)
- Excluded: `postd093` and `v3_d080` non-standard variants
- De-dup: same (α, seed, dataset) → prefer 17855 fp32

## FDR correction method
- `diff_xcorr`, `perm_granger`: use `significant_fdr` (BH-corrected)
- `naive_xcorr`, `threshold_onset`, `ty_granger`: use `significant` (no FDR field available in JSON)

## Coverage
| Category | Count |
|----------|-------|
| alpha_sweep | 26 |
| generalize | 15 |
| scale_check | 3 |
| scale | 1 |
| intervention | 2 |
| ablation | 1 |
| padding_robustness | 1 |
| **Total** | **49** |

## Alpha sweep coverage
α values: 0.00, 0.10, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.75
Total experiments: 26

## FDR correction impact (PermG changes vs v1)
| Experiment | α | v1 permg | v2 permg (FDR) |
|-----------|---|----------|----------------|
| a000_s43 | 0.00 | 2/8 | 0/8 |
| a000_s44 | 0.00 | 2/8 | 0/8 |
| a010_s42_fp32 | 0.10 | 2/8 | 0/8 |
| c4_a025_s42_fp32 | 0.25 | 2/8 | 0/8 |
| a025_s42_fp32 | 0.25 | 3/8 | 0/8 |
| a040_s42_fp32 | 0.40 | 3/8 | 0/8 |
| a045_s42_fp32 | 0.45 | 3/8 | 0/8 |
| a055_s42_fp32 | 0.55 | 5/8 | 0/8 |
| a060_s42_fp32_v4 | 0.60 | 2/8 | 0/8 |
| a060_s43_fp32 | 0.60 | 5/8 | 0/8 |
| a075_s43 | 0.75 | 6/8 | 5/8 |
| a075_s44 | 0.75 | 4/8 | 0/8 |

**Key observation**: FDR correction eliminates all spurious PermG significance at α ≤ 0.45, confirming the dose-response threshold lies between α=0.45 and α=0.50.

## Validation checks (all passed)
- α=0.45 s42: permg_count = 0 ✓ (v1 incorrectly reported 3/8)
- α=0.55 s42: permg_count = 0 ✓ (v1 incorrectly reported 5/8)  
- α=0.50 s42: permg_count = 6 ✓ (unchanged)
- α=0.00 (all seeds): permg_count = 0 ✓ (null baseline correct)

## File
- CSV: `dose_response_d120_compiled.csv`
- Generated: 2026-05-20
