# exp_arXiv_qwen1b5_crossscorer: Cross-Scorer Validation Report

**Date**: 2026-05-18
**Experiment**: arXiv domain cross-scorer validation
**Generator**: Qwen2.5-1.5B | **Scorer**: Pythia-1.4B (cross-family)
**Baseline**: exp_024_arxiv (Qwen2.5-1.5B as both generator and scorer)

## 1. Core Finding

**K\*=3 is scorer-independent for arXiv domain.** Replacing Qwen-1.5B scorer with Pythia-1.4B preserves the saturation boundary at depth 3, confirming the generative depth signal in arXiv is genuine and not an artifact of same-family scoring bias.

This contrasts sharply with Wikipedia, where K\* dropped from 2 to 1 under the same cross-scorer protocol, revealing family bias.

## 2. Pairwise AUC Comparison: Cross-Scorer vs Original

| Boundary | Original (Qwen scorer) | Cross (Pythia scorer) | Delta | Interpretation |
|----------|----------------------|---------------------|-------|---------------|
| 0 vs 1   | 0.9948 +/- 0.0009   | 0.9748 +/- 0.0031  | -0.0200 | Near-perfect in both; small drop from cross-family tokenizer mismatch |
| 1 vs 2   | 0.8581 +/- 0.0119   | 0.8105 +/- 0.0083  | -0.0476 | Largest absolute drop; Pythia less sensitive to Qwen depth-1/2 features |
| 2 vs 3   | 0.6436 +/- 0.0221   | 0.6317 +/- 0.0124  | -0.0119 | Critical boundary: still above threshold (0.6317 > 0.60) |
| 3 vs 4   | 0.5440 +/- 0.0166   | 0.5437 +/- 0.0118  | -0.0003 | Effectively identical; both near chance |
| 4 vs 5   | 0.5299 +/- 0.0231   | 0.5294 +/- 0.0250  | -0.0005 | Effectively identical; both near chance |

**Pattern**: AUC drops monotonically with cross-scorer, with largest degradation at shallow depths (0v1, 1v2) and negligible change at deep boundaries (3v4, 4v5). The discriminability profile shape is fully preserved.

## 3. JSD Comparison

| Boundary | Original (Qwen) | Cross (Pythia) | Delta |
|----------|-----------------|----------------|-------|
| 0 vs 1   | 0.2030          | 0.1543         | -0.0487 |
| 1 vs 2   | 0.0773          | 0.0668         | -0.0105 |
| 2 vs 3   | 0.0198          | 0.0193         | -0.0006 |
| 3 vs 4   | 0.0083          | 0.0089         | +0.0006 |
| 4 vs 5   | 0.0077          | 0.0070         | -0.0007 |

JSD mirrors the AUC pattern: significant distributional divergence at shallow depths narrows under cross-scorer, but deep-boundary JSD is stable to within noise. The cross-family scorer measures essentially the same distributional structure at depth >= 2.

## 4. Wikipedia vs arXiv: Scorer Confound Comparison

| Metric | Wikipedia (Qwen) | Wikipedia (Pythia) | arXiv (Qwen) | arXiv (Pythia) |
|--------|------------------|--------------------|--------------|----------------|
| K\*     | 2                | 1                  | 3            | 3              |
| AUC(0v1) | 0.9961         | 0.9404             | 0.9948       | 0.9748         |
| AUC(1v2) | 0.6193         | 0.5870             | 0.8581       | 0.8105         |
| AUC(2v3) | 0.5498         | 0.5456             | 0.6436       | 0.6317         |
| Ordinal MAE | 1.1805      | 1.3559             | 0.8256       | 0.9017         |
| Ordinal Acc | 0.3768      | 0.3310             | 0.4767       | 0.4402         |

**Interpretation**:

- **Wikipedia K\*=2 was partially artifactual.** AUC(1v2) = 0.6193 under Qwen scorer is borderline above theta=0.60. With Pythia scorer, it drops to 0.5870 (below theta), confirming the depth-2 boundary was inflated by same-family bias. True Wikipedia K\*=1.
- **arXiv K\*=3 is genuine.** AUC(2v3) = 0.6317 under Pythia scorer remains comfortably above theta=0.60, with margin of +0.0317. All 5 folds individually exceed 0.60 (see below). The signal is real and not scorer-dependent.

This domain asymmetry makes sense: arXiv text has richer structural complexity (mathematical notation, technical vocabulary, multi-step arguments) that produces more distinguishable generative degradation patterns across families.

## 5. Critical Boundary Analysis: AUC(2v3) = 0.6317

Per-fold breakdown:

| Fold | AUC(2v3) | Above theta? |
|------|----------|--------------|
| 0    | 0.6533   | Yes (+0.053) |
| 1    | 0.6260   | Yes (+0.026) |
| 2    | 0.6296   | Yes (+0.030) |
| 3    | 0.6157   | Yes (+0.016) |
| 4    | 0.6340   | Yes (+0.034) |

All 5 folds exceed theta=0.60. The minimum fold (fold 3, AUC=0.6157) still clears by +0.016, and the standard deviation is 0.0124. This is a robust, stable boundary.

The 95% confidence interval lower bound is approximately 0.6317 - 1.96 * 0.0124/sqrt(5) = 0.6208, still above 0.60.

## 6. Per-Fold Data (All Boundaries)

### AUC Per-Fold

| Boundary | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Std |
|----------|--------|--------|--------|--------|--------|------|-----|
| 0 vs 1   | 0.9723 | 0.9715 | 0.9796 | 0.9732 | 0.9774 | 0.9748 | 0.0031 |
| 1 vs 2   | 0.8070 | 0.8248 | 0.8138 | 0.8006 | 0.8063 | 0.8105 | 0.0083 |
| 2 vs 3   | 0.6533 | 0.6260 | 0.6296 | 0.6157 | 0.6340 | 0.6317 | 0.0124 |
| 3 vs 4   | 0.5577 | 0.5480 | 0.5228 | 0.5499 | 0.5403 | 0.5437 | 0.0118 |
| 4 vs 5   | 0.5197 | 0.5551 | 0.5102 | 0.5625 | 0.4994 | 0.5294 | 0.0250 |

### Ordinal Classification
- MAE = 0.9017 (vs 0.8256 original; +0.076 degradation)
- Accuracy = 0.4402 (vs 0.4767 original; -0.037 degradation)

Moderate ordinal degradation under cross-scorer, consistent with the shallow-boundary AUC drops.

## 7. Feature Importance (Top 10)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | freq_entropy | 9540.4 |
| 2 | surp_std | 8015.4 |
| 3 | surp_d1_skew | 7848.6 |
| 4 | surp_d1_mean | 7427.4 |
| 5 | surp_mean | 7402.2 |
| 6 | surp_d2_mean | 7324.8 |
| 7 | freq_kurtosis | 6931.2 |
| 8 | surp_kurt | 6623.8 |
| 9 | surp_d1_std | 6006.8 |
| 10 | hapax_ratio | 5892.6 |

Frequency entropy and surprisal statistics dominate, as expected. The cross-scorer feature ranking likely differs from the original since Pythia's tokenizer produces different surprisal distributions, but the overall reliance on distributional shape features (entropy, kurtosis, derivatives) is consistent.

## 8. Predictions for Remaining Cross-Scorer Experiments

Based on the arXiv cross-scorer result showing domain-genuine K\*=3:

| Experiment | Scorer | Expected K\* | Rationale |
|-----------|--------|-------------|-----------|
| exp_arXiv_qwen7b_crossscorer | Pythia-1.4B on Qwen-7B gen | 3 | If Qwen-1.5B signal is genuine, larger Qwen-7B should also hold |
| exp_arXiv_llama8b_crossscorer | Pythia-1.4B on LLaMA-8B gen | 2-3 | LLaMA-8B may have different saturation depth; cross-scorer should preserve it |
| exp_arXiv_mistral7b_crossscorer | Pythia-1.4B on Mistral-7B gen | 2-3 | Similar to LLaMA; cross-scorer confirms genuine depth |

The key prediction: no arXiv cross-scorer experiment should show K\* collapse (K\* dropping by >= 2), unlike Wikipedia where cross-scoring exposed the scorer artifact. If any arXiv experiment does show K\* collapse, it would indicate a generator-specific artifact rather than a domain-level property.

## 9. Summary

1. **K\*=3 confirmed scorer-independent for arXiv domain.** The generative saturation boundary is a genuine text-distributional property, not a same-family scoring artifact.
2. **Domain asymmetry validated.** Wikipedia K\*=2 was partially artifactual (drops to K\*=1 under cross-scorer). arXiv K\*=3 is genuine (holds under cross-scorer). This supports the hypothesis that structurally complex domains sustain deeper distinguishable generative depth.
3. **AUC degradation is concentrated at shallow boundaries** (0v1: -0.02, 1v2: -0.05), consistent with cross-family tokenizer mismatch affecting absolute sensitivity but not the structural pattern.
4. **The critical AUC(2v3) = 0.6317 is robust**: all 5 folds above theta, 95% CI lower bound > 0.60.
