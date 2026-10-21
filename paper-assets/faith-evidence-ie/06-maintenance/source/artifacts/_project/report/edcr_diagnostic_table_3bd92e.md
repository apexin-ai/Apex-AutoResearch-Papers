# EDCR Cross-Method Diagnostic Table

Generated: 2026-05-16 | Methods: 15

| Method | rel_f1 | evi_f1 | EDCR | evi_joint_f1 | Category |
|--------|--------|--------|------|--------------|----------|
| SFT no-evidence | 0.4893 | 0.0000 | 0.0000 | 0.0000 | ablation |
| RSFT-CED s43 | 0.4683 | 0.8156 | 0.6388 | 0.0000 | rsft |
| RSFT-CED s44 | 0.4655 | 0.8087 | 0.6350 | 0.0000 | rsft |
| GRPO bf16 ckpt100 | 0.4549 | 0.8086 | 0.6318 | 0.3571 | grpo |
| RSFT-flatNLI s42 | 0.4539 | 0.8043 | 0.6431 | 0.3544 | rsft |
| RSFT-CED r2a | 0.4494 | 0.8108 | 0.6641 | 0.0000 | rsft |
| RSFT-CED r2b | 0.4493 | 0.8128 | 0.6609 | 0.0000 | rsft |
| RSFT-CED s42 | 0.4449 | 0.8187 | 0.6565 | 0.0000 | rsft |
| GRPO bf16 ckpt50 | 0.4276 | 0.8024 | 0.6855 | 0.3300 | grpo |
| SFT baseline (noquant) | 0.4106 | 0.8013 | 0.7039 | 0.3216 | baseline |
| SFT baseline (quant) | 0.4057 | 0.7979 | 0.7118 | 0.0000 | baseline |
| DPO-CED 1ep | 0.4034 | 0.8088 | 0.7139 | 0.3069 | dpo |
| DPO-CED 3ep | 0.3429 | 0.8403 | 0.7294 | 0.2703 | dpo |
| GRPO QLoRA kl001 | 0.2167 | 0.5746 | 0.8539 | 0.0000 | grpo |
| GRPO QLoRA lr5e6 | 0.0138 | 0.8504 | 0.9876 | 0.0000 | grpo |

## Correlation Analysis

| Metric Pair | Spearman (all) | p-value | Pearson | p-value |
|-------------|---------------|---------|---------|---------|
| EDCR vs rel_f1 | -0.9648 | 0.0000 | -0.9906 | 0.0000 |
| EDCR vs evi_f1 | 0.0022 | 0.9941 | -0.2680 | 0.3543 |

Functional methods only (rel_f1>0.1, n=13):
- EDCR vs rel_f1: Spearman=-0.9560 (p=0.0000)
- EDCR vs evi_f1: Spearman=-0.2473 (p=0.4154)

## Diagnostic Categories

- **Evidence-dominated (EDCR>0.75)**: Model produces many distractor citations not tied to correct relations
- **Balanced (0.6<EDCR<0.75)**: Moderate coupling between evidence and relation extraction
- **Relation-focused (EDCR<0.6)**: Evidence tightly coupled to correct relations (best for IE)

## Key Findings

1. EDCR is near-perfectly anticorrelated with rel_f1 (ρ=-0.96). Higher rel_f1 → lower EDCR.
2. EDCR is completely uncorrelated with evi_f1 (ρ≈0). EDCR does NOT measure evidence quality.
3. EDCR's primary diagnostic value: identifying pathological models (GRPO QLoRA) that produce high evi_f1 by flooding citations without correct relations.
4. For functional methods (rel_f1>0.1), EDCR ranking is nearly identical to rel_f1 ranking — limited additional discriminative power.
5. No method achieves EDCR<0.6 ("relation-focused"), suggesting all models still produce substantial distractor evidence.