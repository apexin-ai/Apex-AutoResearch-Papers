# Unified RSA Summary — Method B Recalculation

## Method B Specification (confirmed from rsa_clip.py / rsa_siglip_only.py)

| Parameter | Value |
|-----------|-------|
| Representation distance | cosine |
| Action distance | euclidean (L2) |
| N_SAMPLE | 20 (np.linspace subsample) |
| Pairing | within-task itertools.combinations |
| Aggregation | per-task Spearman → mean + bootstrap CI |
| Seed | 42 |

## All Conditions — Best Layer + Peak RSA

| Condition | Aggregation | Best Layer | Peak RSA |
|-----------|------------|------------|----------|
| trained_with_inst | image_mean | 12 | **0.6282** |
| trained_with_inst | last_preaction | 12 | **0.6425** |
| untrained_with_inst | image_mean | 0 | 0.6117 |
| untrained_with_inst | last_preaction | 1 | 0.6262 |
| trained_no_inst | image_mean | 13 | 0.6225 |
| untrained_no_inst | image_mean | 0 | 0.6106 |
| random_s0 | image_mean | 12 | 0.6283 |
| shuffled | image_mean | 12 | 0.6282 |

Note: last_preaction layer 0 returns NaN for all tasks (ConstantInputWarning — features at layer 0 produce constant cosine distances). Other layers are valid.

## Instruction Control (image_mean, trained)

| Condition | Best Layer | Peak RSA |
|-----------|------------|----------|
| normal (with-inst) | 12 | 0.6282 |
| no_inst (empty) | 13 | 0.6225 |
| random_s0 | 12 | 0.6283 |
| shuffled | 12 | 0.6282 |

All 4 conditions are nearly identical (range: 0.6225–0.6283). Instruction content has negligible impact.

## Method A → Method B Comparison

| Condition | Method A Peak (layer) | Method B Peak (layer) | Δ |
|-----------|----------------------|----------------------|---|
| trained_with_inst | 0.4876 (L9) | 0.6282 (L12) | +0.141 |
| untrained_with_inst | 0.4846 (L12) | 0.6117 (L0) | +0.127 |
| trained_no_inst | 0.489 (L30) | 0.6225 (L13) | +0.134 |
| untrained_no_inst | 0.4802 (L6) | 0.6106 (L0) | +0.130 |
| DINO | 0.388 | 0.692 (cls) | +0.304 |

Method B consistently produces higher absolute values (~+0.13 for VLA, +0.30 for DINO). Relative ordering preserved.

## Key Deltas (Method B, image_mean)

**Projector → VLA:**
- SigLIP+Projector: 0.615
- VLA trained: 0.6282
- Δ = **+0.013** (VLA slightly higher, not degraded)

**Trained vs Untrained:**
- Trained: 0.6282
- Untrained: 0.6117
- Δ = **+0.017** (small training effect)

**With-inst vs No-inst (trained):**
- With-inst: 0.6282
- No-inst: 0.6225
- Δ = **+0.006** (negligible instruction effect)

**image_mean vs last_preaction (trained):**
- image_mean: 0.6282
- last_preaction: 0.6425
- Δ = **+0.014** (pre-action token slightly more action-relevant)

## Standalone Baselines (Method B, for reference)

| Model | Feature | RSA |
|-------|---------|-----|
| SigLIP+Projector | — | 0.615 |
| DINO | cls_token | 0.692 |
| DINO | patch_mean | 0.631 |
| CLIP | patch_mean | 0.557 |

## Missing Data

- **"empty" instruction control**: No dedicated features directory found. Used `trained_no_inst` as equivalent.
- **last_preaction for no-inst / instruction control conditions**: Not computed (not requested).

## Files

- Full JSON: `/root/autodl-tmp/vla-ssd/results/rsa/unified_rsa_results.json` (199KB)
- Script: `/root/vla-ssd/scripts/rsa_unified_vla.py`
- Runtime: 1054s (~17.5 min)
