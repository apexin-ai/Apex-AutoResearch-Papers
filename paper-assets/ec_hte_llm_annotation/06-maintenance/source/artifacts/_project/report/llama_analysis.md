# EC-HTE Misclassification Analysis: Llama-3.1-8B

## Data Overview

- **N**: 500
- **P(Z=1)** (ground truth): 0.652
- **P(Z_hat=1)** (LLM): 0.570
- **Overall accuracy** (Z vs Z_hat): 0.754
- **Balanced Z definition**: Z=1 if true_label >= 1 (neutral + positive)
- **Subgroups**: has_hashtag × text_length_bin (K=4)
- **HB EB hyperparameters**: α₀(z=0) = 2.95, α₀(z=1) = 3.66

## Subgroup Sizes

| Subgroup | n | n(Z=0) | n(Z=1) | P(Z=1) |
|----------|---|--------|--------|--------|
| False_medium | 193 | 102 | 91 | 0.472 |
| False_short | 109 | 29 | 80 | 0.734 |
| True_medium | 129 | 32 | 97 | 0.752 |
| True_short | 69 | 11 | 58 | 0.841 |

## Per-Subgroup Confusion Matrix (MLE)

| Subgroup | n | Accuracy | FPR | FNR | π_s | κ(M̂_s) |
|----------|---|----------|-----|-----|-----|---------|
| False_medium | 193 | 0.725 | 0.235 | 0.319 | 0.277 | 2.26 |
| False_short | 109 | 0.761 | 0.310 | 0.212 | 0.261 | 2.12 |
| True_medium | 129 | 0.752 | 0.219 | 0.258 | 0.238 | 1.91 |
| True_short | 69 | 0.826 | 0.091 | 0.190 | 0.140 | 1.42 |

## Per-Subgroup Confusion Matrix (HB Empirical Bayes)

| Subgroup | P(Z_hat=0|Z=0) | P(Z_hat=1|Z=0) [FPR] | P(Z_hat=0|Z=1) [FNR] | P(Z_hat=1|Z=1) | π_s (HB) | κ (HB) |
|----------|----------------|----------------------|----------------------|----------------|----------|--------|
| False_medium | 0.757 | 0.243 | 0.326 | 0.674 | 0.284 | 2.34 |
| False_short | 0.672 | 0.328 | 0.225 | 0.775 | 0.276 | 2.27 |
| True_medium | 0.758 | 0.242 | 0.267 | 0.733 | 0.255 | 2.04 |
| True_short | 0.823 | 0.177 | 0.208 | 0.792 | 0.193 | 1.63 |

## Misclassification Heterogeneity (Δπ)

- **Δπ = max(π_s) - min(π_s) = 0.277 - 0.140 = 0.137**
- **Threshold**: Δπ > 0.05 → **YES** (heterogeneous misclassification confirmed)
- **max κ(M̂_s)**: 2.26

## Proposition 2 Diagnostic

Condition: |δ_s| / ((1 - 2π̄) · π_s) > 1 implies CATE bias from misclassification.

- **π̄** (mean symmetric misclass rate): 0.229
- **1 - 2π̄**: 0.542

| Subgroup | δ_s (FPR-FNR) | π_s | Prop2 ratio | Triggered? |
|----------|---------------|-----|-------------|------------|
| False_medium | -0.083 | 0.277 | 0.556 | no |
| False_short | +0.098 | 0.261 | 0.691 | no |
| True_medium | -0.039 | 0.238 | 0.302 | no |
| True_short | -0.099 | 0.140 | 1.300 | **YES** |

## Asymmetry Analysis (FPR vs FNR)

- **False_medium**: FPR=0.235, FNR=0.319 → FNR > FPR (|δ|=0.083)
- **False_short**: FPR=0.310, FNR=0.212 → FPR > FNR (|δ|=0.098)
- **True_medium**: FPR=0.219, FNR=0.258 → FNR > FPR (|δ|=0.039)
- **True_short**: FPR=0.091, FNR=0.190 → FNR > FPR (|δ|=0.099)

## Conclusion

**Llama-3.1-8B exhibits subgroup-heterogeneous misclassification** (Δπ = 0.137 > 0.05).

This confirms Claim C1: real LLM annotators produce misclassification rates that vary across subgroups defined by text features (hashtag presence × text length).

Proposition 2 diagnostic triggered in 1/4 subgroups, indicating that the asymmetric misclassification pattern would bias CATE estimates if this annotation were used as a treatment/outcome proxy in a causal study.
