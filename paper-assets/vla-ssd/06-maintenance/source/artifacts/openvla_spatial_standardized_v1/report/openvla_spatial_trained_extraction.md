# OpenVLA Spatial Trained — Data Extraction

> Source: `westd-19183:/root/autodl-tmp/vla-ssd/results/libero_spatial/`
> Pipeline: openvla_spatial_standardized_v1 (crashed at CF phase, 4/5 phases complete)
> Extracted: 2026-05-22

## R² Probing (last_preaction)

Peak: **L14 = 0.845**
Exit (L31): **0.735**
Δ = **0.110**
Exit collapse: **YES** (Δ > 0.05)

| Layer | last_preaction | image_mean |
|-------|---------------|------------|
| L0  | 0.677 | 0.844 |
| L1  | 0.759 | 0.847 |
| L2  | 0.779 | 0.849 |
| L3  | 0.795 | 0.854 |
| L4  | 0.816 | 0.859 |
| L5  | 0.826 | 0.859 |
| L6  | 0.829 | 0.860 |
| L7  | 0.824 | 0.862 |
| L8  | 0.825 | 0.866 |
| L9  | 0.831 | 0.866 |
| L10 | 0.827 | 0.862 |
| L11 | 0.829 | 0.864 |
| L12 | 0.836 | 0.864 |
| L13 | 0.842 | 0.866 |
| L14 | **0.845** | 0.866 |
| L15 | 0.843 | 0.869 |
| L16 | 0.837 | 0.871 |
| L17 | 0.828 | 0.872 |
| L18 | 0.835 | 0.872 |
| L19 | 0.836 | 0.871 |
| L20 | 0.840 | 0.870 |
| L21 | 0.841 | 0.869 |
| L22 | 0.839 | 0.864 |
| L23 | 0.837 | 0.859 |
| L24 | 0.840 | 0.859 |
| L25 | 0.839 | 0.862 |
| L26 | 0.832 | 0.864 |
| L27 | 0.821 | 0.862 |
| L28 | 0.792 | 0.862 |
| L29 | 0.767 | 0.857 |
| L30 | 0.737 | 0.851 |
| L31 | **0.735** | 0.856 |

Profile: gradual rise L0-L14, plateau L14-L25, then steep drop L26-L31.

## L1 Attention

| Metric | Value |
|--------|-------|
| Instruction-dominant | **24/32** |
| Image-dominant | 0/32 |
| Mixed | **8/32** |

Mixed heads: h3, h6, h9, h13, h16, h21, h24, h28

Top instruction-ratio heads: h0 (0.850), h22 (0.809), h14 (0.754), h10 (0.743), h25 (0.735)

## Cross-Instruction Classification

Chance level: 0.1 (10 tasks)

| Layer | last_preaction | image_mean |
|-------|---------------|------------|
| L0  | 0.991 | 0.998 |
| L1  | **1.000** | 0.998 |
| L2-L31 | 1.000 | 1.000 |

Perfect classification from L1 onward on last_preaction. Near-perfect even at L0 (0.991).

## RSA (last_preaction)

| Layer | mean ρ | 95% CI |
|-------|--------|--------|
| L0  | **0.579** | [0.506, 0.658] |
| L4  | 0.573 | [0.464, 0.678] |
| L8  | 0.470 | [0.356, 0.601] |
| L12 | 0.530 | [0.445, 0.637] |
| L16 | 0.537 | [0.414, 0.645] |
| L20 | 0.547 | [0.437, 0.639] |
| L24 | 0.497 | [0.417, 0.581] |
| L28 | 0.530 | [0.408, 0.657] |
| L31 | 0.491 | [0.388, 0.584] |

Best last_preaction: L0 (ρ=0.579). No clear mid-layer peak; RSA is relatively flat with a slight early-layer advantage. Best overall (image_mean): L31 (ρ=0.635).

## Comparison with Legacy Data

Old (pre-standardized): R² peak 0.696 at L13 using image_mean representation.
New (standardized): R² peak 0.845 at L14 using last_preaction representation.

The ~0.15 difference is due to representation choice (last_preaction vs image_mean for R² action probing). The new standardized pipeline correctly uses last_preaction for action probing.
