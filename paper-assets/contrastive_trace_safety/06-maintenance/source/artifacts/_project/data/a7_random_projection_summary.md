# A7: Random Projection to 384d Baseline

## Results

| Model | RP-384d Prec | Text Prec | ΔPrec | RP-384d BA | Text BA | ΔBA | RP-384d FPR | Text FPR | ΔFPR | RP-384d AUC | Text AUC | ΔAUC |
|-------|-------------|-----------|-------|-----------|---------|-----|------------|----------|------|------------|----------|------|
| R1-8B | 0.621±0.009 | 0.416 | +0.205 | 0.787±0.004 | 0.647 | +0.140 | 0.147±0.005 | 0.258 | -0.111 | 0.871±0.003 | 0.705 | +0.166 |
| OT-7B | 0.371±0.001 | 0.244 | +0.127 | 0.708±0.004 | 0.580 | +0.128 | 0.249±0.007 | 0.348 | -0.099 | 0.779±0.008 | 0.597 | +0.182 |
| R1-32B | 0.524±0.017 | 0.441 | +0.083 | 0.686±0.010 | 0.601 | +0.085 | 0.330±0.034 | 0.382 | -0.052 | 0.738±0.014 | 0.637 | +0.101 |
| QwQ-32B | 0.563±0.003 | 0.391 | +0.172 | 0.724±0.009 | 0.591 | +0.132 | 0.197±0.005 | 0.291 | -0.094 | 0.800±0.005 | 0.624 | +0.176 |

## Bootstrap (1000 resamples, RP-Text)

All models: p(RP > Text) = 1.000 for Prec/BA/AUROC.

## Conclusion

HS advantage does NOT depend on PCA variance-preserving property. Random projection to 384d still significantly outperforms text embeddings at the same dimensionality.

## Config

60/20/20 split seed=42, 3 RP seeds (42/123/456), LR(lbfgs, C=1.0, balanced), text=all-MiniLM-L6-v2
Remote: /root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a7_random_projection/a7_results.json