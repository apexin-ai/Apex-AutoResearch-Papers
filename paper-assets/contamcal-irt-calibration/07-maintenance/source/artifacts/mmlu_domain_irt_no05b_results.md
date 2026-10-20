# J=13 MMLU Domain IRT Final Results (D127)

**Date**: 2026-05-17
**Status**: All 9 domains complete (8 MMLU domains + pooled)
**Model**: 2PL+γ, CmdStan 4 chains × 1000 warmup + 1000 sampling
**Respondents (J=13)**: 8 × Qwen2.5-1.5B + 5 × Qwen2.5-3B (no 0.5B)

## Model Whitelist

| # | Model | Scale | Dosage |
|---|-------|-------|--------|
| 1 | Qwen2.5-1.5B_d000_s123 | 1.5B | 0% |
| 2 | Qwen2.5-1.5B_d000_s42 | 1.5B | 0% |
| 3 | Qwen2.5-1.5B_d005_s123 | 1.5B | 5% |
| 4 | Qwen2.5-1.5B_d005_s42 | 1.5B | 5% |
| 5 | Qwen2.5-1.5B_d025_s123 | 1.5B | 25% |
| 6 | Qwen2.5-1.5B_d025_s42 | 1.5B | 25% |
| 7 | Qwen2.5-1.5B_d100_s123 | 1.5B | 100% |
| 8 | Qwen2.5-1.5B_d100_s42 | 1.5B | 100% |
| 9 | Qwen2.5-3B_d005_s123 | 3B | 5% |
| 10 | Qwen2.5-3B_d025_s123 | 3B | 25% |
| 11 | Qwen2.5-3B_d025_v3_s42 | 3B | 25% |
| 12 | Qwen2.5-3B_d100_a32_s123 | 3B | 100% |
| 13 | Qwen2.5-3B_d100_a32_s42 | 3B | 100% |

Note: No d000 (clean) models for 3B in this pool.

## Per-Domain Gamma (8 domains)

| Domain | N_items | γ_mean | 95% CI | CI excludes 0? | PPP | N=23 γ_mean | Δ(J13−N23) |
|--------|---------|--------|--------|----------------|-----|-------------|------------|
| STEM_Math | 1190 | 0.499 | [−0.213, 1.203] | No | 0.206 | 0.97 | −0.47 |
| STEM_Science | 1397 | 0.504 | [−0.189, 1.202] | No | 0.149 | 0.84 | −0.34 |
| STEM_CS_Eng | 557 | 0.497 | [−0.425, 1.397] | No | 0.392 | 0.29 | +0.21 |
| Medical | 1640 | 0.235 | [−0.421, 0.879] | No | 0.124 | 0.27 | −0.04 |
| Humanities | 2000* | −0.309 | [−0.852, 0.257] | No | 0.530 | 0.47 | −0.78 |
| Social_Sciences | 2000* | −0.571 | [−1.054, −0.103] | **YES** | 0.570 | 0.28 | −0.85 |
| Business_Law | 2000* | 0.044 | [−0.497, 0.579] | No | 0.299 | 0.61 | −0.57 |
| Other | 883 | 0.127 | [−0.612, 0.885] | No† | 0.096 | 1.34 | −1.21 |

*subsampled from larger item pools (Humanities: 2816, Social_Sciences: 3077, Business_Law: 2482)
†Other domain: max Rhat=1.01, convergence marginal (rhat_ok=false)

## Pooled Gamma

| γ_mean | 95% CI | CI excludes 0? | PPP |
|--------|--------|----------------|-----|
| 0.107 | [−0.401, 0.625] | No | 0.208 |

## Ability Difference (θ)

**Not available.** Stan output CSV files were not retained in the result directories (only `irt_results.json` saved per domain). Cannot extract posterior θ estimates without re-running or modifying the pipeline to preserve CSV outputs.

## Diagnostics Summary

| Domain | n_items | fit_time (s) | max_rhat | convergence_ok |
|--------|---------|--------------|----------|----------------|
| STEM_Math | 1190 | 279 | 1.007 | Yes |
| STEM_Science | 1397 | 333 | — | Yes |
| STEM_CS_Eng | 557 | 81 | — | Yes |
| Medical | 1640 | 395 | — | Yes |
| Humanities | 2000 | 491 | — | Yes |
| Social_Sciences | 2000 | 484 | — | Yes |
| Business_Law | 2000 | 505 | — | Yes |
| Other | 883 | 183 | 1.010 | No |
| Pooled | 2000 | 487 | — | Yes |

## Key Findings

1. **Social Sciences is the only domain with CI excluding 0**, but γ is *negative* (−0.571), meaning 3B models underperform relative to IRT expectation. This is the opposite direction from contamination inflation.

2. **Removing 0.5B models collapses contamination signal.** In N=23, STEM_Math (0.97) and Other (1.34) had strong positive γ. With J=13, no domain shows significant positive γ. The 0.5B models were providing the low-ability anchor that made 3B overperformance detectable.

3. **STEM domains still show positive γ (~0.5)** but CIs are too wide to reach significance with only 13 respondents.

4. **Systematic downward shift**: 7/8 domains have lower γ in J=13 vs N=23. The largest drops are Other (−1.21), Social_Sciences (−0.85), and Humanities (−0.78).

5. **Model fit acceptable**: PPP values 0.10–0.57, residual MAE uniformly low (0.005–0.017).

## Summary Table for Paper

| Domain | J=13 γ | J=13 sig? | N=23 γ | N=23 sig? | Interpretation |
|--------|--------|-----------|--------|-----------|----------------|
| STEM_Math | 0.50 | No | 0.97 | Yes | Signal halved without 0.5B anchor |
| STEM_Science | 0.50 | No | 0.84 | Yes | Signal halved without 0.5B anchor |
| STEM_CS_Eng | 0.50 | No | 0.29 | No | Slight increase, both non-significant |
| Medical | 0.24 | No | 0.27 | No | Stable, weak in both |
| Humanities | −0.31 | No | 0.47 | No | Sign flip |
| Social_Sciences | −0.57 | **Yes** | 0.28 | No | Sign flip, now significant negative |
| Business_Law | 0.04 | No | 0.61 | No | Large drop |
| Other | 0.13 | No | 1.34 | Yes | Largest drop, lost significance |
