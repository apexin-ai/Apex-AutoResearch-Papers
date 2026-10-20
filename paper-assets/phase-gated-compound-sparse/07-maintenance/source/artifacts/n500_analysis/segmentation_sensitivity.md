# Segmentation Sensitivity Analysis

## Overview

Tests whether the Phase-Gated Compound Sparsity II (Interaction Index) difference between low-sparsity and high-sparsity phases is robust across different segmentation granularities (tercile/quartile/quintile).

- **Models**: DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both bf16)
- **Strategy**: importance masking
- **D** = II(lowest_phase) - II(highest_phase) per problem
- **Statistical test**: Wilcoxon signed-rank (two-sided), Bonferroni k=4
- **Bootstrap**: B=10000, seed=42, median CI (alpha=0.05)

## Results Summary

All 24 conditions (2 models x 4 sparsity x 3 segmentations) show **significant positive D** after Bonferroni correction, confirming that low-sparsity phases consistently have higher II than high-sparsity phases regardless of model or segmentation granularity.

### DeepSeek — Tercile (n=500, n_eff=496, 3 phases)

| Sparsity | median_D | 95% CI | Bonf p | Sig |
|----------|----------|--------|--------|-----|
| s015 | +0.391 | [0.350, 0.443] | 5.08e-70 | yes |
| s020 | +1.215 | [1.109, 1.339] | 1.59e-74 | yes |
| s025 | +3.986 | [3.534, 4.356] | 7.98e-78 | yes |
| s030 | +8.481 | [7.754, 9.685] | 4.35e-79 | yes |

### DeepSeek — Quartile (n=50, 4 phases)

| Sparsity | median_D | 95% CI | Bonf p | Sig |
|----------|----------|--------|--------|-----|
| s015 | +0.491 | [0.444, 0.696] | 1.47e-12 | yes |
| s020 | +1.388 | [1.053, 1.786] | 3.06e-13 | yes |
| s025 | +4.322 | [3.617, 8.064] | 2.34e-13 | yes |
| s030 | +12.930 | [9.828, 19.101] | 1.78e-13 | yes |

### DeepSeek — Quintile (n=50, 5 phases)

| Sparsity | median_D | 95% CI | Bonf p | Sig |
|----------|----------|--------|--------|-----|
| s015 | +0.505 | [0.331, 0.705] | 3.54e-11 | yes |
| s020 | +1.197 | [1.019, 1.755] | 1.42e-14 | yes |
| s025 | +4.960 | [3.801, 9.019] | 1.20e-12 | yes |
| s030 | +11.548 | [10.055, 18.506] | 3.06e-13 | yes |

### Qwen — Tercile (n=500, n_eff=475, 3 phases)

| Sparsity | median_D | 95% CI | Bonf p | Sig |
|----------|----------|--------|--------|-----|
| s015 | +0.066 | [0.049, 0.092] | 3.46e-14 | yes |
| s020 | +0.307 | [0.261, 0.356] | 2.74e-41 | yes |
| s025 | +1.074 | [0.977, 1.179] | 4.25e-68 | yes |
| s030 | +3.155 | [2.783, 3.558] | 3.69e-73 | yes |

### Qwen — Quartile (n=50, 4 phases)

| Sparsity | median_D | 95% CI | Bonf p | Sig |
|----------|----------|--------|--------|-----|
| s015 | +0.226 | [0.143, 0.267] | 4.20e-07 | yes |
| s020 | +0.561 | [0.351, 0.769] | 1.45e-07 | yes |
| s025 | +1.870 | [1.055, 2.435] | 2.86e-10 | yes |
| s030 | +4.097 | [2.911, 4.943] | 4.97e-14 | yes |

### Qwen — Quintile (n=50, 5 phases)

| Sparsity | median_D | 95% CI | Bonf p | Sig |
|----------|----------|--------|--------|-----|
| s015 | +0.203 | [0.134, 0.261] | 2.89e-07 | yes |
| s020 | +0.517 | [0.292, 0.751] | 2.53e-08 | yes |
| s025 | +1.801 | [1.131, 2.378] | 4.77e-09 | yes |
| s030 | +4.009 | [3.279, 5.339] | 1.35e-13 | yes |

## Key Observations

1. **Cross-model consistency**: Both DeepSeek and Qwen show significant positive D across all 12 conditions each, confirming the PACS effect generalizes beyond a single architecture.
2. **Direction consistency**: All segmentations show positive D (low phase > high phase) across all sparsity levels for both models.
3. **Magnitude scaling**: DeepSeek D values are systematically ~2-3x larger than Qwen at matched sparsity, consistent with main profiling results.
4. **Dose-response preserved**: D increases monotonically with sparsity across all segmentations for both models (s015 < s020 < s025 < s030).
5. **Robustness**: The effect is not an artifact of the 3-way tercile split; finer-grained segmentations (4-way, 5-way) reproduce the same pattern.
6. **Effective n**: DeepSeek tercile n_eff=496/500, Qwen tercile n_eff=475/500 (25 problems with insufficient token count for 3-phase split).

## Files

- `segmentation_sensitivity.csv` — 24-row unified CSV (12 DeepSeek + 12 Qwen)
- Server: `/root/autodl-tmp/pacs/analysis_output/segmentation_sensitivity.csv` (DeepSeek), `/root/autodl-tmp/pacs/analysis_output/qwen_segmentation_sensitivity.csv` (Qwen)
