# Min Phase Length Sensitivity Analysis

D = II(low sparsity phase) - II(high sparsity phase)
mpl values: [5, 10, 20]
Bootstrap B=10000, seed=42
Bonferroni k=4 (family-wise within model)

**Method**: Per-token sparsity data re-segmented under each mpl threshold to determine phase validity. II values from original mpl=10 profiling used for D computation. This tests whether conclusions are robust to the segmentation granularity parameter.

## Deepseek

| Strategy | Sparsity | mpl | n_eff | mid_null | median_D | 95% CI | p_wilcoxon | p_bonf | Sig |
|----------|----------|-----|-------|----------|----------|--------|------------|--------|-----|
| importance | s015 | 5 | 496 | 0.0% | +0.3907 | [0.3496, 0.4431] | 1.27e-70 | 5.08e-70 | YES |
| importance | s015 | 10 | 496 | 10.2% | +0.3907 | [0.3496, 0.4431] | 1.27e-70 | 5.08e-70 | YES |
| importance | s015 | 20 | 433 | 71.2% | +0.3925 | [0.3520, 0.4458] | 3.83e-66 | 1.53e-65 | YES |
| importance | s020 | 5 | 496 | 0.0% | +1.2149 | [1.1072, 1.3365] | 3.98e-75 | 1.59e-74 | YES |
| importance | s020 | 10 | 496 | 10.2% | +1.2149 | [1.1072, 1.3365] | 3.98e-75 | 1.59e-74 | YES |
| importance | s020 | 20 | 433 | 71.2% | +1.2345 | [1.1143, 1.3478] | 8.69e-69 | 3.48e-68 | YES |
| importance | s025 | 5 | 496 | 0.0% | +3.9857 | [3.5272, 4.3588] | 1.99e-78 | 7.98e-78 | YES |
| importance | s025 | 10 | 496 | 10.2% | +3.9857 | [3.5272, 4.3588] | 1.99e-78 | 7.98e-78 | YES |
| importance | s025 | 20 | 433 | 71.2% | +4.0174 | [3.5645, 4.4392] | 4.51e-71 | 1.80e-70 | YES |
| importance | s030 | 5 | 496 | 0.0% | +8.4813 | [7.7543, 9.6919] | 1.09e-79 | 4.35e-79 | YES |
| importance | s030 | 10 | 496 | 10.2% | +8.4813 | [7.7543, 9.6919] | 1.09e-79 | 4.35e-79 | YES |
| importance | s030 | 20 | 433 | 71.2% | +8.4204 | [7.4777, 9.6919] | 2.82e-70 | 1.13e-69 | YES |
| random | s015 | 5 | 496 | 0.0% | +0.0139 | [-0.0167, 0.0389] | 8.63e-01 | 1.00e+00 | no |
| random | s015 | 10 | 496 | 10.2% | +0.0139 | [-0.0167, 0.0389] | 8.63e-01 | 1.00e+00 | no |
| random | s015 | 20 | 433 | 71.2% | +0.0120 | [-0.0187, 0.0343] | 4.89e-01 | 1.00e+00 | no |
| random | s020 | 5 | 496 | 0.0% | +0.0315 | [-0.0112, 0.0767] | 2.80e-01 | 1.00e+00 | no |
| random | s020 | 10 | 496 | 10.2% | +0.0315 | [-0.0112, 0.0767] | 2.80e-01 | 1.00e+00 | no |
| random | s020 | 20 | 433 | 71.2% | +0.0227 | [-0.0252, 0.0618] | 8.25e-01 | 1.00e+00 | no |
| random | s025 | 5 | 496 | 0.0% | +0.2574 | [0.1265, 0.3498] | 1.46e-03 | 5.84e-03 | YES |
| random | s025 | 10 | 496 | 10.2% | +0.2574 | [0.1265, 0.3498] | 1.46e-03 | 5.84e-03 | YES |
| random | s025 | 20 | 433 | 71.2% | +0.1897 | [0.0805, 0.3132] | 7.88e-03 | 3.15e-02 | YES |
| random | s030 | 5 | 496 | 0.0% | +0.5096 | [0.2601, 0.8909] | 1.48e-03 | 5.90e-03 | YES |
| random | s030 | 10 | 496 | 10.2% | +0.5096 | [0.2601, 0.8909] | 1.48e-03 | 5.90e-03 | YES |
| random | s030 | 20 | 433 | 71.2% | +0.4100 | [0.1429, 0.7687] | 1.45e-02 | 5.79e-02 | no |

## Qwen

| Strategy | Sparsity | mpl | n_eff | mid_null | median_D | 95% CI | p_wilcoxon | p_bonf | Sig |
|----------|----------|-----|-------|----------|----------|--------|------------|--------|-----|
| importance | s015 | 5 | 475 | 0.4% | +0.0659 | [0.0492, 0.0925] | 8.66e-15 | 3.46e-14 | YES |
| importance | s015 | 10 | 475 | 45.2% | +0.0659 | [0.0492, 0.0925] | 8.66e-15 | 3.46e-14 | YES |
| importance | s015 | 20 | 289 | 84.6% | +0.0659 | [0.0455, 0.1010] | 2.30e-11 | 9.20e-11 | YES |
| importance | s020 | 5 | 475 | 0.4% | +0.3073 | [0.2612, 0.3564] | 6.84e-42 | 2.74e-41 | YES |
| importance | s020 | 10 | 475 | 45.2% | +0.3073 | [0.2612, 0.3564] | 6.84e-42 | 2.74e-41 | YES |
| importance | s020 | 20 | 289 | 84.6% | +0.3245 | [0.2715, 0.3982] | 6.60e-30 | 2.64e-29 | YES |
| importance | s025 | 5 | 475 | 0.4% | +1.0745 | [0.9766, 1.1787] | 1.06e-68 | 4.25e-68 | YES |
| importance | s025 | 10 | 475 | 45.2% | +1.0745 | [0.9766, 1.1787] | 1.06e-68 | 4.25e-68 | YES |
| importance | s025 | 20 | 289 | 84.6% | +1.1062 | [1.0133, 1.3572] | 1.84e-44 | 7.35e-44 | YES |
| importance | s030 | 5 | 475 | 0.4% | +3.1550 | [2.7986, 3.5582] | 9.21e-74 | 3.69e-73 | YES |
| importance | s030 | 10 | 475 | 45.2% | +3.1550 | [2.7986, 3.5582] | 9.21e-74 | 3.69e-73 | YES |
| importance | s030 | 20 | 289 | 84.6% | +3.5805 | [2.9342, 4.1340] | 1.22e-47 | 4.88e-47 | YES |
| random | s015 | 5 | 475 | 0.4% | -0.0111 | [-0.0390, 0.0124] | 1.72e-01 | 6.87e-01 | no |
| random | s015 | 10 | 475 | 45.2% | -0.0111 | [-0.0390, 0.0124] | 1.72e-01 | 6.87e-01 | no |
| random | s015 | 20 | 289 | 84.6% | -0.0111 | [-0.0433, 0.0169] | 2.32e-01 | 9.28e-01 | no |
| random | s020 | 5 | 475 | 0.4% | +0.0153 | [-0.0145, 0.0684] | 2.00e-01 | 8.00e-01 | no |
| random | s020 | 10 | 475 | 45.2% | +0.0153 | [-0.0145, 0.0684] | 2.00e-01 | 8.00e-01 | no |
| random | s020 | 20 | 289 | 84.6% | +0.0153 | [-0.0273, 0.0788] | 3.49e-01 | 1.00e+00 | no |
| random | s025 | 5 | 475 | 0.4% | +0.3931 | [0.2360, 0.5529] | 1.59e-11 | 6.37e-11 | YES |
| random | s025 | 10 | 475 | 45.2% | +0.3931 | [0.2360, 0.5529] | 1.59e-11 | 6.37e-11 | YES |
| random | s025 | 20 | 289 | 84.6% | +0.2658 | [0.1173, 0.4718] | 2.93e-06 | 1.17e-05 | YES |
| random | s030 | 5 | 475 | 0.4% | +0.9127 | [0.6134, 1.2584] | 2.92e-15 | 1.17e-14 | YES |
| random | s030 | 10 | 475 | 45.2% | +0.9127 | [0.6134, 1.2584] | 2.92e-15 | 1.17e-14 | YES |
| random | s030 | 20 | 289 | 84.6% | +0.7876 | [0.3948, 1.1481] | 1.15e-08 | 4.61e-08 | YES |

## Key Findings

### Deepseek
- **mpl=5**: imp 4/4 sig, rand 2/4 sig, avg n_effective=496
- **mpl=10**: imp 4/4 sig, rand 2/4 sig, avg n_effective=496
- **mpl=20**: imp 4/4 sig, rand 1/4 sig, avg n_effective=433

### Qwen
- **mpl=5**: imp 4/4 sig, rand 2/4 sig, avg n_effective=475
- **mpl=10**: imp 4/4 sig, rand 2/4 sig, avg n_effective=475
- **mpl=20**: imp 4/4 sig, rand 2/4 sig, avg n_effective=289

### Robustness: Sign Consistency

- mpl=10 vs mpl=5 (importance): 8/8 same sign
- mpl=10 vs mpl=20 (importance): 8/8 same sign

### n_effective by mpl

| Model | Strategy | Sparsity | mpl=5 | mpl=10 | mpl=20 |
|-------|----------|----------|-------|--------|--------|
| deepseek | importance | s015 | 496 | 496 | 433 |
| deepseek | importance | s020 | 496 | 496 | 433 |
| deepseek | importance | s025 | 496 | 496 | 433 |
| deepseek | importance | s030 | 496 | 496 | 433 |
| deepseek | random | s015 | 496 | 496 | 433 |
| deepseek | random | s020 | 496 | 496 | 433 |
| deepseek | random | s025 | 496 | 496 | 433 |
| deepseek | random | s030 | 496 | 496 | 433 |
| qwen | importance | s015 | 475 | 475 | 289 |
| qwen | importance | s020 | 475 | 475 | 289 |
| qwen | importance | s025 | 475 | 475 | 289 |
| qwen | importance | s030 | 475 | 475 | 289 |
| qwen | random | s015 | 475 | 475 | 289 |
| qwen | random | s020 | 475 | 475 | 289 |
| qwen | random | s025 | 475 | 475 | 289 |
| qwen | random | s030 | 475 | 475 | 289 |

### Interpretation

1. **All 8 importance conditions remain significant (p < 0.05, Bonferroni-corrected) across all three mpl values.** The phase-dependent interaction effect is robust to segmentation granularity.

2. **Sign consistency is perfect (8/8)**: the direction of the effect (II_low > II_high) never flips regardless of mpl.

3. **mpl=20 drops n_effective substantially** (deepseek: 496→433, qwen: 475→289) because stricter merging eliminates short phases, yet all importance conditions remain highly significant.

4. **Random masking**: at low sparsity (s015, s020), D is near zero and non-significant across all mpl — confirming that the interaction effect requires structured (importance-based) masking. At higher sparsity (s025, s030), random also shows significance, consistent with the dose-response pattern.

5. **One marginal change**: ds_rand_s030 loses significance at mpl=20 (bonf_p=0.058), consistent with reduced power from smaller n_effective rather than a genuine change in the effect.
