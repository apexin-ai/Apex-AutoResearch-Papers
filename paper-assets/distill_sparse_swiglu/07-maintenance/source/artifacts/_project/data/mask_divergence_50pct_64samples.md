# Mask Divergence Analysis: 50% Sparsity, 64 Samples

## Summary
- **Sparsity**: 50%
- **Samples**: 64 (seq_len=2048, total tokens=131,072)
- **Checkpoint**: `mvp_kl_norm_v2_s42/predictor_kl_normalized.pt`
- **Model**: LLaMA-3.1-8B

## Aggregate Statistics
| Metric | Value |
|--------|-------|
| Mean Jaccard Similarity | 0.3176 |
| **Mean Jaccard Distance** | **0.6824** |
| Min Jaccard Distance | 0.5234 (layer 31) |
| Max Jaccard Distance | 0.7517 (layer 26) |
| Neuron Scatter Disagree (L16) | 40.6% |

## Per-Layer Jaccard Distance

| Layer | Jaccard Dist | Layer | Jaccard Dist |
|-------|-------------|-------|-------------|
| 0 | 0.6270 | 16 | 0.6112 |
| 1 | 0.7411 | 17 | 0.6154 |
| 2 | 0.7193 | 18 | 0.6371 |
| 3 | 0.6907 | 19 | 0.6582 |
| 4 | 0.6739 | 20 | 0.6693 |
| 5 | 0.6776 | 21 | 0.6746 |
| 6 | 0.6799 | 22 | 0.6998 |
| 7 | 0.7112 | 23 | 0.7188 |
| 8 | 0.7088 | 24 | 0.7338 |
| 9 | 0.7271 | 25 | 0.7471 |
| 10 | 0.7173 | 26 | 0.7517 |
| 11 | 0.6950 | 27 | 0.7437 |
| 12 | 0.6921 | 28 | 0.7290 |
| 13 | 0.6988 | 29 | 0.6998 |
| 14 | 0.6460 | 30 | 0.6079 |
| 15 | 0.6100 | 31 | 0.5234 |

## Key Observations
- Mean Jaccard distance 68.24% confirms the paper's claim (~68%)
- Divergence is highest in layers 24-28 (>0.73), indicating KL predictor discovers substantially different importance patterns from magnitude in deeper layers
- Layers 15-17 and 30-31 show lowest divergence (~0.52-0.61), suggesting magnitude and KL agree more in early attention layers and the final layer
- Range: 0.5234 to 0.7517 (spread of 0.2283)

## Data Source
- JSON: `/root/distill_sparse_swiglu/figures/mask_stats_50pct_64samples.json`
- Figures: `/root/distill_sparse_swiglu/figures/mask_divergence_heatmap_50pct_64samples.{pdf,png}`
- Log: `/root/distill_sparse_swiglu/logs/vis_mask_50pct_64s.log`
