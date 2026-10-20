# Demo-Standardized RSA Results (10 demos, Method B)

**Date**: 2026-05-16
**Script**: `/root/vla-ssd/scripts/rsa_demo_standardized.py`
**Output**: `/root/autodl-tmp/vla-ssd/results/rsa/rsa_demo_standardized.json`

## Method
- Within-task pairs (itertools.combinations)
- Representation distance: cosine
- Action distance: euclidean
- Temporal subsampling: 20 timesteps (linspace)
- Per-task Spearman → mean across 10 tasks
- Bootstrap CI: 1000 resamples, seed=42

## Standardization
All models use **demo_0 through demo_9** (10 demos per task, identical across all models).

## Token Info
- **VLA image_mean**: mean of 256 image patch tokens (positions 1:257), excludes BOS and text tokens
- **VLA last_preaction**: hidden state at last sequence position
- **SigLIP projector**: SigLIP features projected to 4096-dim LLM space (`siglip_only_libero_goal/last_preaction`)
- **DINO/CLIP**: DINOv2/CLIP ViT-L cls_token or patch_mean (1024-dim)

## Results

| Model | RSA | 95% CI |
|-------|-----|--------|
| **DINO cls** | **0.6412** | [0.4949, 0.7747] |
| DINO patch_mean | 0.5675 | [0.3919, 0.7338] |
| CLIP cls | 0.4818 | [0.2923, 0.6591] |
| CLIP patch_mean | 0.5408 | [0.3617, 0.7103] |
| SigLIP projector | 0.5645 | [0.4268, 0.7008] |
| VLA trained L9 lastpre | 0.4990 | [0.3427, 0.6354] |
| VLA untrained L9 lastpre | 0.5767 | [0.4368, 0.7111] |
| VLA trained L9 imgmean | 0.5706 | [0.4317, 0.7092] |
| VLA untrained L9 imgmean | 0.5143 | [0.3666, 0.6735] |

## Pairwise Δ Bootstrap CIs

| Comparison | Δ | 95% CI | Significant? |
|-----------|---|--------|-------------|
| trained vs untrained (lastpre) | -0.0777 | [-0.1369, -0.0157] | **YES** (untrained > trained) |
| trained vs untrained (imgmean) | +0.0562 | [+0.0258, +0.0895] | **YES** (trained > untrained) |
| SigLIP proj vs VLA trained (lastpre) | +0.0654 | [-0.0001, +0.1309] | No (borderline) |
| DINO cls vs SigLIP proj | +0.0768 | [+0.0031, +0.1556] | **YES** |

## Key Observations

1. **DINO cls is the top performer** at 0.641, significantly above SigLIP projector.
2. **Trained vs untrained direction reverses by feature type**: lastpre shows untrained > trained (Δ=-0.078, sig), while image_mean shows trained > untrained (Δ=+0.056, sig). This suggests training reshapes action information across token positions.
3. **All CIs are wide** due to only 10 tasks — high per-task variance (e.g., `cream_cheese_in_bowl` consistently low, `wine_bottle_on_rack` consistently high).
4. Numbers match prior audit within noise: DINO cls 0.641 (was 0.641), SigLIP 0.565 (was 0.565), VLA trained L9 lastpre 0.499 (was 0.499).

## Note on Feature Directories
Actual paths differ from task context:
- `trained` → `trained_libero_goal/` (50 demos available, 10 used)
- `untrained` → `untrained_libero_goal/`
- `siglip_projector` → `siglip_only_libero_goal/`
- `dino` → `dinov2_libero_goal/`
- `clip` → `clip_libero_goal/`
- `fused_backbone_libero_goal/` also exists (SigLIP+DINOv2 concat, 2176-dim, only 2 tasks)
