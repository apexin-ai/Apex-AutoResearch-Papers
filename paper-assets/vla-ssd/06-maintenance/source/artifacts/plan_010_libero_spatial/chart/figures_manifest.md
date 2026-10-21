# LIBERO-Spatial Figures

Server path: `/root/autodl-tmp/vla-ssd/results/figures/`

## Files
- `libero_spatial_rsa_perlayer.pdf` / `.png` — 4 curves (trained/untrained × imgmean/lastpre) with 95% CI shading + peak annotations
- `libero_spatial_r2_perlayer.pdf` / `.png` — 4 R² curves with peak annotations
- `cross_benchmark_comparison.pdf` / `.png` — 1×2 subplot: Goal (thin/transparent) vs Spatial (bold), Left=RSA Right=R²

## Script
`/root/vla-ssd/scripts/plot_spatial_results.py`

## Style
- Trained: blue tones, Untrained: red/orange tones
- image_mean: solid lines, last_preaction: dashed lines
- Goal: thin/transparent, Spatial: bold/opaque (in comparison figure)
- 300 DPI, academic style (no top/right spines)
