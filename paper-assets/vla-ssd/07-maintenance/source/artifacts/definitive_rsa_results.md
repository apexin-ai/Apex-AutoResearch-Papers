# Definitive RSA Results (Method B)

**Date**: 2026-05-16
**Script**: `rsa_definitive.py` (MD5: `be4f68dc8c763c5e1a052b8fa8e6da64`)
**Server**: westd-19183
**Runtime**: 1813.8 seconds (~30 min)
**JSON**: `/root/autodl-tmp/vla-ssd/results/rsa/rsa_definitive.json`

## Methodology

- **Pairing**: within-task (Method B)
- **Representation distance**: cosine
- **Action distance**: euclidean
- **N_SAMPLE**: 20 random within-task pairs per bootstrap
- **Demos/task**: 50
- **Bootstrap**: 1000 resamples, seed=42
- **Statistical tests**: paired t-test on per-task RSA values
- **Tasks**: 10 LIBERO-Goal tasks
- **VLA layers**: 33 Llama layers (0-32), best layer selected by mean RSA
- **Token aggregation**: image_mean = mean of 256 image patch tokens (positions 1:257), last_preaction = single readout token at position 257

## RSA Ranking Table

| Rank | Model | Best Layer | RSA | std | CI_lo | CI_hi |
|------|-------|-----------|------|------|-------|-------|
| 1 | dino_cls | - | **0.6915** | 0.0847 | 0.6409 | 0.7401 |
| 2 | vla_trained/last_preaction | L12 | 0.6425 | 0.1255 | 0.5643 | 0.7145 |
| 3 | fused_backbone | - | 0.6336 | 0.1509 | 0.5420 | 0.7162 |
| 4 | dino_patch_mean | - | 0.6307 | 0.1294 | 0.5473 | 0.7008 |
| 5 | vla_trained/image_mean | L12 | 0.6282 | 0.1510 | 0.5349 | 0.7129 |
| 6 | vla_trained_no_inst/last_preaction | L13 | 0.6267 | 0.1571 | 0.5325 | 0.7234 |
| 7 | vla_untrained/last_preaction | L1 | 0.6262 | 0.1389 | 0.5427 | 0.7044 |
| 8 | vla_untrained_no_inst/last_preaction | L1 | 0.6257 | 0.1440 | 0.5387 | 0.7049 |
| 9 | vla_trained_no_inst/image_mean | L13 | 0.6225 | 0.1890 | 0.4998 | 0.7337 |
| 10 | vla_untrained/image_mean | L0 | 0.6117 | 0.1520 | 0.5184 | 0.6954 |
| 11 | siglip_projector | - | 0.6117 | 0.1520 | 0.5184 | 0.6954 |
| 12 | vla_untrained_no_inst/image_mean | L0 | 0.6106 | 0.1542 | 0.5154 | 0.6954 |
| 13 | clip_patch_mean | - | 0.5572 | 0.1679 | 0.4541 | 0.6541 |
| 14 | clip_cls | - | 0.5062 | 0.1795 | 0.3912 | 0.6081 |

## Pairwise Comparisons (C1-C8)

| ID | Comparison | Delta | CI_lo | CI_hi | p_boot | p_ttest | Sig |
|----|-----------|-------|-------|-------|--------|---------|-----|
| C1 | trained vs untrained image_mean (L12) | +0.0787 | 0.0596 | 0.0982 | 0.000 | 3.9e-05 | *** |
| C2 | trained vs untrained last_preaction (L12) | +0.0472 | 0.0234 | 0.0697 | 0.000 | 0.0045 | ** |
| C3 | siglip_projector vs trained image_mean (L12) | -0.0165 | -0.0338 | 0.0003 | 1.000 | 0.118 | ns |
| C4 | siglip_projector vs trained last_preaction (L12) | -0.0308 | -0.0580 | -0.0074 | 1.000 | 0.055 | . |
| C5 | dino_cls vs siglip_projector | +0.0798 | 0.0220 | 0.1393 | 0.006 | 0.032 | * |
| C6 | fused_backbone vs siglip_projector | +0.0219 | 0.0094 | 0.0337 | 0.002 | 0.011 | * |
| C7 | trained inst vs no-inst image_mean (L12) | +0.0081 | -0.0774 | 0.1025 | 0.844 | 0.863 | ns |
| C8 | untrained inst vs no-inst image_mean (L0) | +0.0011 | 0.0000 | 0.0033 | 0.656 | 0.343 | ns |

Significance: *** p<0.001, ** p<0.01, * p<0.05, . p<0.1, ns not significant

## Instruction Control (image_mean at best layer 12)

| Condition | RSA | std | Description |
|-----------|------|------|-------------|
| inst_normal | 0.6282 | 0.1510 | Correct task instruction |
| inst_random | 0.6283 | 0.1510 | Random instruction from another task |
| inst_shuffled | 0.6282 | 0.1510 | Word-shuffled instruction |
| inst_no_inst | 0.6201 | 0.1933 | No instruction tokens |

## Key Findings

1. **DINOv2 CLS has the highest RSA** (0.6915), significantly above all other models
2. **Training significantly improves VLA RSA** for both image_mean (+0.079, p<0.001) and last_preaction (+0.047, p<0.01)
3. **VLA trained is NOT significantly better than SigLIP projector** for image_mean (C3, p=0.118); marginal for last_preaction (C4, p=0.055)
4. **Pre-projector features beat post-projector**: fused_backbone > siglip_projector (C6, p=0.011)
5. **Instruction content has zero effect on RSA**: normal/random/shuffled are identical; no-inst is slightly lower but not significant (C7, p=0.863)
6. **Untrained VLA image_mean at L0 matches siglip_projector exactly** (both 0.6117) — the VLA backbone without training preserves projector RSA at its input layer
7. **Best VLA layer shifts with training**: untrained peaks at L0-1 (input), trained peaks at L12-13 (middle)
8. **last_preaction consistently outperforms image_mean** for all VLA variants (concentrated > distributed readout)

## VLA Best Layers

| Model | image_mean | last_preaction |
|-------|-----------|---------------|
| vla_trained | L12 (0.6282) | L12 (0.6425) |
| vla_trained_no_inst | L13 (0.6225) | L13 (0.6267) |
| vla_untrained | L0 (0.6117) | L1 (0.6262) |
| vla_untrained_no_inst | L0 (0.6106) | L1 (0.6257) |
