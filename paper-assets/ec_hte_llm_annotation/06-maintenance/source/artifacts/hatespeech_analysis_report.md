# Hate Speech (CivilComments) — Per-Subgroup Bias Amplification Analysis

## Dataset

- **Source**: Jigsaw Civil Comments dataset
- **Task**: Binary toxicity classification (toxic vs non-toxic)
- **Effect modifier (Z)**: Annotated by LLMs (GPT-4o, GPT-4o-mini, GPT-3.5-turbo)
- **Subgroups (K=4)**: text_length × has_question
  - S0: short, no question (n=1163)
  - S1: short, has question (n=341)
  - S2: long, no question (n=1012)
  - S3: long, has question (n=484)

## Per-LLM Global Confusion Matrix Metrics

| LLM | Global FPR | Global FNR | Δ_FPR | Δ_FNR | R² |
|-----|-----------|-----------|-------|-------|-----|
| gpt-4o | 0.2652 | 0.2311 | 0.0912 | 0.1472 | 0.9794 |
| gpt-4o-mini | 0.4981 | 0.0722 | 0.1220 | 0.0534 | 0.7563 |
| gpt-3.5-turbo | 0.4171 | 0.1433 | 0.0895 | 0.0964 | 0.9346 |

## Per-Subgroup Confusion Matrix Profiles

### gpt-4o

| Subgroup | Label | n | FPR | FNR | Accuracy | κ(C_s) | π_s | δ_s |
|----------|-------|---|-----|-----|----------|--------|-----|-----|
| S0 | short, no question | 1163 | 0.2633 | 0.1823 | 0.7627 | 1.80 | 0.4456 | -0.0519 |
| S1 | short, has question | 341 | 0.2411 | 0.1477 | 0.7830 | 1.64 | 0.3888 | -0.1087 |
| S2 | long, no question | 1012 | 0.2455 | 0.2862 | 0.7431 | 2.14 | 0.5317 | +0.0342 |
| S3 | long, has question | 484 | 0.3323 | 0.2949 | 0.6798 | 2.68 | 0.6272 | +0.1297 |

### gpt-4o-mini

| Subgroup | Label | n | FPR | FNR | Accuracy | κ(C_s) | π_s | δ_s |
|----------|-------|---|-----|-----|----------|--------|-----|-----|
| S0 | short, no question | 1163 | 0.4975 | 0.0563 | 0.6440 | 2.24 | 0.5538 | -0.0174 |
| S1 | short, has question | 341 | 0.5692 | 0.0455 | 0.5660 | 2.60 | 0.6147 | +0.0435 |
| S2 | long, no question | 1012 | 0.4472 | 0.0989 | 0.6502 | 2.20 | 0.5461 | -0.0251 |
| S3 | long, has question | 484 | 0.5579 | 0.0769 | 0.5971 | 2.74 | 0.6348 | +0.0636 |

### gpt-3.5-turbo

| Subgroup | Label | n | FPR | FNR | Accuracy | κ(C_s) | π_s | δ_s |
|----------|-------|---|-----|-----|----------|--------|-----|-----|
| S0 | short, no question | 1163 | 0.3848 | 0.1233 | 0.6991 | 2.03 | 0.5081 | -0.0513 |
| S1 | short, has question | 341 | 0.4743 | 0.1023 | 0.6217 | 2.36 | 0.5766 | +0.0172 |
| S2 | long, no question | 1012 | 0.4102 | 0.1519 | 0.6621 | 2.28 | 0.5621 | +0.0027 |
| S3 | long, has question | 484 | 0.4665 | 0.1987 | 0.6198 | 2.99 | 0.6652 | +0.1058 |

## Theorem 1 Validation: Predicted vs Observed Bias (Δτ = 0.3)

| LLM | Subgroup | z | Predicted Bias | Observed Bias | SE | |Pred-Obs|/SE |
|-----|----------|---|---------------|--------------|-----|------------|
| gpt-3.5-turbo | S0 | 0 | -0.007927 | -0.008912 | 0.002774 | 0.36 |
| gpt-3.5-turbo | S0 | 1 | +0.024766 | +0.024608 | 0.005017 | 0.03 |
| gpt-3.5-turbo | S1 | 0 | -0.005203 | -0.000056 | 0.005700 | 0.90 |
| gpt-3.5-turbo | S1 | 1 | -0.007829 | -0.028770 | 0.010277 | 2.04 |
| gpt-3.5-turbo | S2 | 0 | +0.001562 | +0.005420 | 0.002673 | 1.44 |
| gpt-3.5-turbo | S2 | 1 | -0.001456 | -0.005562 | 0.005788 | 0.71 |
| gpt-3.5-turbo | S3 | 0 | +0.019447 | +0.023767 | 0.004359 | 0.99 |
| gpt-3.5-turbo | S3 | 1 | -0.050948 | -0.066753 | 0.008721 | 1.81 |
| gpt-4o | S0 | 0 | -0.010148 | -0.010490 | 0.002698 | 0.13 |
| gpt-4o | S0 | 1 | +0.017484 | +0.013618 | 0.004704 | 0.82 |
| gpt-4o | S1 | 0 | -0.019935 | -0.019927 | 0.004919 | 0.00 |
| gpt-4o | S1 | 1 | +0.042376 | +0.036435 | 0.009069 | 0.66 |
| gpt-4o | S2 | 0 | +0.007965 | +0.005949 | 0.002700 | 0.75 |
| gpt-4o | S2 | 1 | -0.005892 | -0.006940 | 0.005176 | 0.20 |
| gpt-4o | S3 | 0 | +0.021775 | +0.020824 | 0.003634 | 0.26 |
| gpt-4o | S3 | 1 | -0.059548 | -0.054137 | 0.006914 | 0.78 |
| gpt-4o-mini | S0 | 0 | -0.004338 | -0.002559 | 0.002378 | 0.75 |
| gpt-4o-mini | S0 | 1 | +0.007977 | +0.002249 | 0.005481 | 1.04 |
| gpt-4o-mini | S1 | 0 | -0.003845 | +0.004297 | 0.005007 | 1.63 |
| gpt-4o-mini | S1 | 1 | -0.013052 | -0.023604 | 0.009515 | 1.11 |
| gpt-4o-mini | S2 | 0 | +0.003749 | +0.004441 | 0.002942 | 0.23 |
| gpt-4o-mini | S2 | 1 | +0.007983 | +0.002409 | 0.006924 | 0.81 |
| gpt-4o-mini | S3 | 0 | +0.005293 | +0.000103 | 0.004425 | 1.17 |
| gpt-4o-mini | S3 | 1 | -0.026664 | -0.029089 | 0.008013 | 0.30 |

## R² Summary

### CivilComments

| LLM | R² | Max |B| | Diagnostic AUC |
|-----|-----|---------|----------------|
| gpt-4o | 0.9794 | 0.1985 | 0.3005 |
| gpt-4o-mini | 0.7563 | 0.0889 | 0.3081 |
| gpt-3.5-turbo | 0.9346 | 0.1698 | 0.2342 |

**Pooled R² (all LLMs combined)**: 0.9440

### Comparison with TweetEval

| LLM | CivilComments R² | TweetEval R² |
|-----|-----------------|-------------|
| gpt-4o | 0.9794 | 0.9752 |
| gpt-4o-mini | 0.7563 | 0.9293 |
| gpt-3.5-turbo | 0.9346 | 0.9478 |

## Debiasing Hurts Analysis

- **Total LLM × subgroup × z × Δτ combinations**: 120
- **Cases where |observed bias| > 2 SE**: 66 (55.0%)
- This means global debiasing introduces statistically significant residual bias in 55.0% of subgroup-level estimates.

### Most Extreme Bias Amplification Cases (max |bias| > 0.05)

| LLM | Subgroup | Label | κ(C_s) | δ_s | Max |Bias| |
|-----|----------|-------|--------|-----|-----------|
| gpt-4o | S3 | long, has question | 2.68 | +0.1297 | 0.0992 |
| gpt-3.5-turbo | S3 | long, has question | 2.99 | +0.1058 | 0.0906 |
| gpt-4o | S1 | short, has question | 1.64 | -0.1087 | 0.0667 |

## Key Takeaways

1. **Theorem 1 accuracy**: Average R² = 0.890 across 3 LLMs on CivilComments, confirming the analytic bias formula accurately predicts residual subgroup-level bias from global debiasing.
   - Comparable to TweetEval average R² = 0.951 (across overlapping LLMs).
2. **Misclassification heterogeneity**: Subgroup FPR ranges span 0.241–0.569, FNR ranges span 0.045–0.295.
3. **Most ill-conditioned subgroup**: gpt-3.5-turbo × S3 (long, has question) with κ = 2.99.
4. **Best-conditioned subgroup**: gpt-4o × S1 (short, has question) with κ = 1.64.
5. **Debiasing hurts prevalence**: 55.0% of subgroup-level estimates show statistically significant residual bias after global correction.
6. **Practical implication**: In hate speech detection, text-feature-based misclassification heterogeneity (driven by text length and question presence) produces systematic bias in subgroup-level treatment effect estimates even after global debiasing correction.