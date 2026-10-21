# Feasibility Report: Re-fitting IRT Parameters from v1 Open LLM Leaderboard Data

**Experiment**: exp-v1-irt-refit-pilot  
**Date**: 2026-05-20  
**Parent**: exp-item-alignment-check (Claim 3)

## Executive Summary

Re-fitting IRT parameters from v1 Open LLM Leaderboard response data is **not feasible** with the available sample size. With only 63 downloadable models (examinees) and 14,042 MMLU items, the examinee-to-item ratio (N:J ≈ 0.0045) is far below the minimum required for stable MML-EM estimation. Discrimination parameters are essentially unidentifiable, difficulty parameters show only moderate correlation (r=0.63) with PSN-IRT on a different scale, and the resulting lz* statistics are completely miscalibrated (mean=11.7 instead of ~0).

## Phase 1: Feasibility Research

### IRT Fitting Tools Evaluated

| Tool | Models | Issue |
|------|--------|-------|
| girth (PyPI) | 1PL, 2PL, 3PL | 3PL crashes with scipy ≥1.17 (array-vs-scalar bug in fminbound) |
| py-irt 0.1.1 | 1PL, 2PL only | PyPI release lacks 4PL despite documentation claims |
| Custom MML-EM | 2PL, 3PL | Implemented with vectorized Newton-Raphson M-step |

**Decision**: Implemented custom MML-EM with Gauss-Hermite quadrature (Q=31) and vectorized Newton-Raphson. Fitting 14,042 items across 63 models takes ~9s (2PL) and ~12s (3PL).

### Data Availability

- 101 model identifiers compiled from v1 leaderboard
- 63 models (62.4%) had downloadable MMLU evaluation details on HuggingFace
- 38 failures: repos don't exist (chat/instruct variants, newer models like Yi, Gemma, DeepSeek, SOLAR, OLMo, etc.)
- Data format: per-item binary accuracy (`acc` field) across 57 MMLU subjects, 14,042 items total

### Compute Estimation

Vectorized MML-EM achieved ~70x speedup over per-item scipy optimization:
- 2PL fitting (50 iterations, 14042 items, 63 models): **8.9 seconds**
- 3PL fitting (50 iterations, c fixed at 0.25): **12.1 seconds**

## Phase 2: Pilot Results

### Response Matrix

- Shape: 63 models × 14,042 items
- Overall accuracy: 0.426 (range: 0.241 to 0.712)
- Zero-variance items removed: 38
- Items with valid PSN-IRT mapping: 12,441

### Parameter Comparison: v1-Refitted (3PL) vs PSN-IRT

| Parameter | Pearson r | Spearman r | v1 Mean (SD) | PSN-IRT Mean (SD) |
|-----------|-----------|------------|--------------|-------------------|
| a (discrimination) | 0.111 | 0.111 | 2.97 (1.92) | 1.21 (0.52) |
| b (difficulty) | 0.626 | 0.656 | 2.07 (2.67) | -0.83 (0.74) |
| c (guessing) | — | — | 0.25 (fixed) | 0.23 (0.18) |

### Parameter Comparison: v1-Refitted (2PL) vs PSN-IRT

| Parameter | Pearson r | Spearman r | v1 Mean (SD) | PSN-IRT Mean (SD) |
|-----------|-----------|------------|--------------|-------------------|
| a (discrimination) | -0.084 | -0.052 | 1.43 (1.42) | 1.21 (0.52) |
| b (difficulty) | 0.572 | 0.630 | 1.66 (2.88) | -0.83 (0.74) |

### lz* Statistics (using v1-refitted 3PL parameters)

| Metric | Value |
|--------|-------|
| Mean | 11.69 |
| SD | 6.68 |
| Min | -5.88 |
| Max | 23.37 |
| Flagged (z < -1.96) | 1/63 (1.6%) |

The lz* distribution is severely right-shifted (should be approximately N(0,1) under correct model fit). This indicates the refitted model is miscalibrated — models systematically perform better than the model predicts.

## Diagnosis: Why Re-fitting Failed

### 1. Catastrophically Low N:J Ratio

The fundamental problem is **63 examinees for 14,042 items** (N:J = 0.0045). Classical MML-EM typically requires:
- N > 500 for stable 2PL estimation
- N > 1,000 for stable 3PL estimation
- N:J > 5 as a rough guideline

With N:J < 0.005, item parameters are severely under-determined. The E-step posterior over θ is informed by very few response patterns, and the M-step must estimate 14,042 × 2 parameters from only 63 × 14,042 = 884,646 observations — most items have near-identical response patterns across the small examinee pool.

### 2. Discrimination Parameters Hit Bounds

The scatter plot shows many v1-fitted discrimination values clustered at the upper bound (a = 5.0) or near the lower bound (a ≈ 0.01). With so few examinees, the likelihood surface for discrimination is flat — small perturbations in θ estimates cause large swings in a estimates. PSN-IRT's neural approach, trained on hundreds of models, avoids this by learning smooth parameter mappings.

### 3. Difficulty Scale Shift

The v1-refitted difficulty parameters have mean 2.07 (vs PSN-IRT mean -0.83). This ~3-unit shift reflects different θ distributions: PSN-IRT was trained with a standard normal θ prior, while our 63-model sample is skewed toward lower-performing models (overall accuracy 0.43). The rank correlation (Spearman r=0.66) is somewhat better than Pearson (r=0.63), suggesting the relative ordering is partially preserved despite the scale mismatch.

### 4. lz* Miscalibration

lz* assumes the item parameters define the true generative model. When parameters are poorly estimated, the expected log-likelihood and its variance (used in the lz* correction) are wrong, producing systematically biased scores. The mean of 11.7 (vs expected ~0) confirms the refitted model does not describe the data-generating process.

## Implications for the Project

1. **PSN-IRT parameters cannot be replaced** by classical re-fitting from v1 data alone — the sample size is insufficient.

2. **PSN-IRT parameters remain the best available option** for computing person-fit on v1 leaderboard models, despite the ~12% item alignment noise identified in exp-item-alignment-check. The alignment issue introduces noise but doesn't systematically bias the person-fit statistics.

3. **Possible improvements** (not pursued in this pilot):
   - Bayesian IRT with informative priors on a, b (e.g., from PSN-IRT as priors)
   - Regularized MML-EM (penalized likelihood)
   - Downloading more models from v1 leaderboard (full scrape could yield 200-400 models)
   - Using PSN-IRT parameters as initialization for fine-tuning on v1 data

4. **Recommendation**: Proceed with PSN-IRT parameters directly for person-fit analysis, accepting the alignment noise as a known limitation. The moderate difficulty correlation (r=0.63) from re-fitting provides partial validation that PSN-IRT's item parameters capture real difficulty variation in MMLU.

## Artifacts

| File | Description |
|------|-------------|
| `pilot_irt_refit.py` | Full pipeline script |
| `pilot_results.json` | Detailed results with per-model statistics |
| `pilot_response_matrix.npz` | 63×14042 binary response matrix |
| `v1_fitted_params.csv` | Refitted 2PL and 3PL parameters for 14042 items |
| `parameter_comparison.png` | Scatter plots of v1 vs PSN-IRT parameters |
| `lz_star_distribution.png` | lz* histogram and per-model bar chart |
| `feasibility_report.md` | This report |
