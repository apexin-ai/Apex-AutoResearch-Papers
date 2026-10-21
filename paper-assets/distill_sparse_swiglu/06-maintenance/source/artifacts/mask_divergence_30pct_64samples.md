# Mask Divergence Analysis: 30% Sparsity (64 samples)

**Server**: westd-41718 | **Date**: 2026-05-19 | **Tokens**: 131,072 (64 samples x 2048 seq_len)
**Predictor**: `checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt`
**Model**: LLaMA-3.1-8B (32 layers, hidden=4096, intermediate=14336)

## Summary

| Metric | 30% Sparsity | 50% Sparsity |
|--------|-------------|-------------|
| Mean Jaccard Distance | **46.26%** | **68.24%** |
| Min Layer Distance | 36.14% (Layer 31) | — |
| Max Layer Distance | 60.01% (Layer 27) | — |
| Neuron Disagree % (L16) | 8.71% | — |

30% sparsity shows substantially lower mask divergence than 50% (46.26% vs 68.24%), consistent with the expectation that sparser masks have less room for alternative configurations.

## Per-Layer Jaccard Distance

| Layer | Jaccard Sim | Jaccard Dist | KL Sparsity |
|-------|------------|-------------|-------------|
| 0 | 0.5905 | 0.4095 | 0.2041 |
| 1 | 0.5685 | 0.4315 | 0.2490 |
| 2 | 0.5398 | 0.4602 | 0.3140 |
| 3 | 0.5650 | 0.4350 | 0.2648 |
| 4 | 0.5619 | 0.4381 | 0.2737 |
| 5 | 0.5591 | 0.4409 | 0.2750 |
| 6 | 0.5651 | 0.4349 | 0.2621 |
| 7 | 0.5304 | 0.4696 | 0.3203 |
| 8 | 0.5142 | 0.4858 | 0.3555 |
| 9 | 0.5237 | 0.4763 | 0.3388 |
| 10 | 0.5144 | 0.4856 | 0.3537 |
| 11 | 0.5119 | 0.4881 | 0.3576 |
| 12 | 0.5425 | 0.4575 | 0.3183 |
| 13 | 0.5595 | 0.4405 | 0.2902 |
| 14 | 0.5810 | 0.4190 | 0.2489 |
| 15 | 0.6118 | 0.3882 | 0.1840 |
| 16 | 0.6311 | 0.3689 | 0.1390 |
| 17 | 0.6158 | 0.3842 | 0.1628 |
| 18 | 0.6215 | 0.3785 | 0.1456 |
| 19 | 0.5833 | 0.4167 | 0.2115 |
| 20 | 0.5670 | 0.4330 | 0.2342 |
| 21 | 0.5520 | 0.4480 | 0.2640 |
| 22 | 0.5107 | 0.4893 | 0.3193 |
| 23 | 0.4909 | 0.5091 | 0.3481 |
| 24 | 0.4461 | 0.5539 | 0.4134 |
| 25 | 0.4270 | 0.5730 | 0.4490 |
| 26 | 0.4070 | 0.5930 | 0.4905 |
| 27 | 0.3999 | 0.6001 | 0.5093 |
| 28 | 0.4038 | 0.5962 | 0.5167 |
| 29 | 0.4617 | 0.5383 | 0.4449 |
| 30 | 0.6010 | 0.3990 | 0.2282 |
| 31 | 0.6386 | 0.3614 | 0.1727 |

## Layer Pattern

- **Most stable (lowest divergence)**: Layers 15-18 (mid-network) and Layer 31 (final), Jaccard dist 36-39%
- **Most divergent**: Layers 25-29 (late-network), Jaccard dist 54-60%
- KL sparsity correlates strongly with Jaccard distance (high KL = high divergence)

## Generated Figures (on server)

- `figures/mask_divergence_heatmap_30pct_64samples.{pdf,png}`
- `figures/mask_comparison_30pct_64samples.{pdf,png}`
- `results/mask_divergence_30pct_64samples/fig1_mask_heatmap.{pdf,png}`
- `results/mask_divergence_30pct_64samples/fig2_token_dynamics.{pdf,png}`
- `results/mask_divergence_30pct_64samples/fig3_jaccard_divergence.{pdf,png}`

## Data Sources

- Primary: `figures/mask_stats_30pct_64samples.json` (visualization pipeline output)
- Secondary: `results/mask_divergence_30pct_64samples/stats.json` (analysis script output)
