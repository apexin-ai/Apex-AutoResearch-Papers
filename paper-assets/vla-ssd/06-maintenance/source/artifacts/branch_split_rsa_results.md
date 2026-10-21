# Branch-Split RSA Results

## Method
- Prismatic fused backbone (2176d projector input) split into DINOv2 branch (first 1024d) and SigLIP branch (last 1152d)
- Method B: within-task pairing, cosine representation distance, euclidean action distance, full trajectory subsampled to N=20, Spearman rank correlation, mean across 10 LIBERO-Goal tasks
- Concat order confirmed from source: `torch.cat([DINOv2_patches, SigLIP_patches], dim=2)`
- Features extracted from second-to-last transformer block of each backbone (Prismatic convention), NOT `last_hidden_state`

## Results

| Representation | RSA (mean) | std | 95% CI |
|---|---|---|---|
| **DINOv2 branch** (1024d, patch_mean) | 0.619 | 0.158 | [0.522, 0.705] |
| **SigLIP branch** (1152d, patch_mean) | 0.621 | 0.143 | [0.520, 0.701] |
| **Fused** (2176d, patch_mean) | 0.634 | 0.151 | [0.537, 0.722] |

## Comparison with Prior Results

| Representation | RSA |
|---|---|
| Standalone DINO cls_token | 0.692 |
| Fused 2176d (pre-projector) | **0.634** |
| Standalone DINO patch_mean | 0.631 |
| SigLIP branch (in-backbone) | 0.621 |
| DINOv2 branch (in-backbone) | 0.619 |
| Fused+Projector 4096d | 0.615 |
| Standalone CLIP patch_mean | 0.557 |

## Key Observations

1. **DINOv2 and SigLIP branches have nearly identical RSA** (0.619 vs 0.621, delta < 0.002). Neither branch dominates action-relevant information in the fused backbone.

2. **Fused 2176d > both individual branches** (0.634 vs 0.619/0.621). Concatenation provides mild complementary benefit, consistent with the Prismatic design rationale.

3. **Fused pre-projector (0.634) > post-projector (0.615)**. The projector MLP slightly reduces action-alignment, suggesting it compresses some action-relevant spatial structure while adapting features for the LLM.

4. **Standalone DINO (0.692 cls, 0.631 patch_mean) > in-backbone DINOv2 branch (0.619)**. The in-backbone branch uses the second-to-last transformer block rather than the last (Prismatic convention), which may explain the gap. The standalone DINO cls_token also benefits from the [CLS] token's global aggregation vs patch_mean.

5. **SigLIP branch (0.621) >> standalone CLIP (0.557)**. SigLIP-SO400M produces substantially more action-aligned features than OpenAI CLIP ViT-L/14, validating Prismatic's choice of SigLIP over CLIP.

## Files
- JSON: `/root/autodl-tmp/vla-ssd/results/rsa/rsa_branch_split.json`
- Features: `/root/autodl-tmp/vla-ssd/features/fused_backbone_libero_goal/` (10 tasks, 50 demos each, 2176d patch_mean)
- Scripts: `/root/vla-ssd/scripts/rsa_branch_split.py`, `/root/vla-ssd/scripts/extract_fused_backbone.py`
