# UCB Hate Speech — Annotator Demographic Δπ Summary

## Approach

Unit of analysis: (comment, annotator) pair.
- Z_true = annotator's individual dehumanize label (≥2 → 1, else 0)
- Z_hat = GPT-4.1 LLM label (binary, at comment level)
- Subgroup = annotator demographic attribute
- N = 5,865 annotator-level observations (2,496 comments × ~2.3 annotators each)

## Global confusion matrix

|          | Z_hat=0 | Z_hat=1 |
|----------|---------|---------|
| Z_true=0 | 2,347   | 519     |
| Z_true=1 | 1,641   | 1,358   |

- FPR = 0.181, FNR = 0.547, π = 0.364
- Overall accuracy = 63.2%
- Key pattern: **highly asymmetric CM** — LLM misses >50% of hate speech (high FNR)

## Δπ by demographic feature (min group N ≥ 50)

| Feature | # Groups | min π | max π | Δπ | ΔFPR | ΔFNR | Highest π group | Lowest π group |
|---------|----------|-------|-------|----|------|------|-----------------|----------------|
| race × ideology | 12 | 0.289 | 0.405 | **0.117** | 0.131 | 0.161 | latinx_conservative | asian_conservative |
| gender × ideology¹ | 6 | 0.314 | 0.406 | **0.092** | 0.088 | 0.096 | female_conservative | male_neutral |
| education | 7 | 0.307 | 0.391 | **0.084** | 0.096 | 0.135 | professional_degree | phd |
| race | 5 | 0.294 | 0.374 | **0.080** | 0.123 | 0.058 | latinx | native_american |
| ideology (fine) | 8 | 0.319 | 0.396 | **0.077** | 0.078 | 0.098 | slightly_conservative | no_opinion |
| ideology (grouped) | 3 | 0.340 | 0.389 | **0.049** | 0.044 | 0.055 | conservative | neutral |
| income | 5 | 0.331 | 0.376 | **0.045** | 0.034 | 0.064 | 100k-200k | <10k |
| age_group | 5 | 0.347 | 0.387 | **0.040** | 0.021 | 0.090 | 56+ | 36-45 |
| gender | 2 | 0.353 | 0.370 | **0.017** | 0.029 | 0.006 | female | male |

¹ Excluding non-binary_liberal (N=36), which had anomalously low π=0.176.

## Key finding

**Max Δπ = 0.117** (race × ideology interaction), **below the 0.15 EC-HTE threshold**.

No single demographic feature or two-way interaction produces sufficient misclassification heterogeneity for EC-HTE correction to work on this data.

## Interpretation

1. **Moderate ideology effect**: Conservatives have π ≈ 0.39, liberals π ≈ 0.36, neutrals π ≈ 0.34.
   The LLM aligns better with moderate/neutral annotators and worse with conservative annotators (higher FNR).

2. **Moderate race effect**: Latinx (π=0.374) and Black (π=0.372) annotators show higher
   disagreement with the LLM than Asian (π=0.341) or Native American (π=0.294) annotators.

3. **FNR dominates**: The LLM's main error is under-detection of hate speech (FNR ≈ 0.55).
   ΔFNR is the primary driver of Δπ for most features.

4. **Interaction effects are additive, not multiplicative**: The race×ideology interaction
   Δπ (0.117) is roughly the sum of individual Δπ values, not larger than expected.

## Why EC-HTE is unlikely to help here

1. **Δπ < 0.15**: Insufficient misclassification heterogeneity across subgroups
2. **Asymmetric CM**: FPR ≈ 0.17, FNR ≈ 0.55 → denominator (1-FPR-FNR) ≈ 0.28 is small,
   making any correction amplify estimation noise
3. **Annotator-level subgroups ≠ comment-level subgroups**: In a real application, each comment
   doesn't have a fixed annotator demographic — the subgroup structure is at the annotator level,
   not the observation level

## Semi-synthetic validation (gender × ideology, including N=36 outlier)

A semi-synthetic run was performed using the gender×ideology grouping (including the
non-binary_liberal outlier, giving inflated Δπ=0.23). Results confirmed that correction
methods perform *worse* than naive, primarily due to the asymmetric CM:

| Method | n=100 RMSE | n=250 RMSE | n=500 RMSE |
|--------|------------|------------|------------|
| Oracle | 0.047 | 0.047 | 0.047 |
| Naive | **0.104** | **0.104** | **0.104** |
| HB EC-HTE | 0.212 | 0.208 | 0.174 |
| Global corrected | 0.664 | 0.510 | 0.412 |
| Stratified MLE | 0.829 | 0.786 | 0.618 |

Even with (artificially) large Δπ, the correction amplifies errors because the small
denominator (1-FPR-FNR ≈ 0.28) makes the estimator unstable.

## Per-subgroup detail: Top features

### race × ideology (Δπ = 0.117)
| Subgroup | N | FPR | FNR | π |
|----------|---|-----|-----|---|
| latinx_conservative | 77 | 0.250 | 0.561 | 0.405 |
| white_conservative | 1281 | 0.192 | 0.597 | 0.394 |
| black_liberal | 376 | 0.232 | 0.556 | 0.394 |
| black_conservative | 71 | 0.200 | 0.583 | 0.392 |
| latinx_liberal | 209 | 0.193 | 0.570 | 0.381 |
| asian_liberal | 265 | 0.162 | 0.547 | 0.355 |
| white_liberal | 2220 | 0.157 | 0.539 | 0.348 |
| white_neutral | 801 | 0.136 | 0.548 | 0.342 |
| asian_neutral | 94 | 0.178 | 0.490 | 0.334 |
| latinx_neutral | 90 | 0.143 | 0.521 | 0.332 |
| black_neutral | 155 | 0.172 | 0.435 | 0.304 |
| asian_conservative | 66 | 0.119 | 0.458 | 0.289 |

### ideology (Δπ = 0.077)
| Subgroup | N | FPR | FNR | π |
|----------|---|-----|-----|---|
| slightly_conservative | 623 | 0.188 | 0.603 | 0.396 |
| extremely_conservative | 192 | 0.210 | 0.565 | 0.388 |
| conservative | 712 | 0.187 | 0.581 | 0.384 |
| liberal | 1435 | 0.164 | 0.567 | 0.366 |
| slightly_liberal | 981 | 0.184 | 0.525 | 0.355 |
| extremely_liberal | 726 | 0.151 | 0.538 | 0.344 |
| neutral | 1007 | 0.149 | 0.539 | 0.344 |
| no_opinion | 188 | 0.132 | 0.505 | 0.319 |

### education (Δπ = 0.084)
| Subgroup | N | FPR | FNR | π |
|----------|---|-----|-----|---|
| professional_degree | 128 | 0.230 | 0.552 | 0.391 |
| college_grad_aa | 821 | 0.189 | 0.562 | 0.375 |
| college_grad_ba | 2172 | 0.176 | 0.557 | 0.367 |
| some_college | 1485 | 0.169 | 0.553 | 0.361 |
| high_school_grad | 568 | 0.133 | 0.582 | 0.358 |
| masters | 571 | 0.141 | 0.528 | 0.334 |
| phd | 77 | 0.167 | 0.447 | 0.307 |
