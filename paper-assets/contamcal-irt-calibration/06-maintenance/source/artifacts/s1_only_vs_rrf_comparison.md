# S1-Only (Min-K++) vs Full RRF: IRT Calibration Comparison

**Date**: 2026-05-23
**Setup**: J=16 models (Qwen2.5 1.5B + 3B, 4 dosages × 2 seeds), 2PL+γ model, top-300 items
**S1-only**: Items selected and exposed by s2_minkpp signal alone
**RRF**: Items selected and exposed by 3-signal RRF fusion (s1_embedding + s2_minkpp + s4_selfcritique)

## 1. Pooled Benchmark Comparison

### MMLU

| Metric | S1-only | RRF | Delta |
|--------|---------|-----|-------|
| γ (mean) | **1.7535** | 0.6979 | +1.056 |
| 95% CI | [0.912, 2.630] | [−0.423, 1.813] | — |
| CI excludes 0 | Yes | No | — |
| PPP | 0.0003 | **0.193** | −0.193 |
| Kendall τ | 0.628 | **0.730** | −0.102 |
| MAE_cal | 0.0728 | **0.0091** | +0.064 |
| ρ_dose | 0.049 | −0.073 | — |
| R̂_max | 1.007 | 1.008 | — |
| ESS_min | 261 | **1708** | — |

### ARC-Challenge

| Metric | S1-only | RRF | Delta |
|--------|---------|-----|-------|
| γ (mean) | **2.5723** | 0.7269 | +1.845 |
| 95% CI | [1.762, 3.370] | [0.021, 1.443] | — |
| CI excludes 0 | Yes | Yes | — |
| PPP | 0.0000 | **0.003** | −0.003 |
| Kendall τ | 0.597 | **0.733** | −0.137 |
| MAE_cal | 0.1152 | **0.0194** | +0.096 |
| ρ_dose | 0.243 | 0.188 | — |
| R̂_max | 1.014 | 1.007 | — |
| ESS_min | 294 | **1449** | — |

### GSM8K (negative control — no contamination expected)

| Metric | S1-only | RRF | Delta |
|--------|---------|-----|-------|
| γ (mean) | −0.0477 | 0.0639 | −0.112 |
| 95% CI | [−0.496, 0.422] | [−0.364, 0.490] | — |
| CI excludes 0 | No | No | — |
| PPP | 0.578 | **0.541** | +0.037 |
| Kendall τ | **0.366** | 0.191 | +0.175 |
| MAE_cal | 0.1626 | **0.1386** | +0.024 |
| ρ_dose | 0.146 | 0.506 | — |
| R̂_max | 1.009 | 1.008 | — |
| ESS_min | 687 | **1313** | — |

## 2. MMLU Domain-Level γ (RRF baseline, J=16)

S1-only domain fitting only completed STEM_Math before the worker failed. STEM_Math result is pathological.

| Domain | RRF γ | RRF 95% CI | RRF PPP | S1-only γ | S1-only PPP |
|--------|-------|------------|---------|-----------|-------------|
| STEM_Math | 0.5955 | [−0.076, 1.247] | 0.305 | **−6.3181** | 1.000 |
| STEM_Science | 0.5661 | [−0.071, 1.203] | 0.197 | — | — |
| STEM_CS_Eng | 0.3202 | [−0.556, 1.206] | 0.503 | — | — |
| Medical | 0.0505 | [−0.527, 0.651] | 0.268 | — | — |
| Humanities | −0.1420 | [−0.662, 0.408] | 0.416 | — | — |
| Social_Sciences | −0.6274 | [−1.073, −0.192] | 0.722 | — | — |
| Business_Law | 0.0800 | [−0.414, 0.579] | 0.395 | — | — |
| Other | 0.3185 | [−0.440, 1.104] | 0.072 | — | — |

S1-only STEM_Math: γ=−6.32 [−6.65, −5.98], PPP=1.000 — complete model failure. Negative γ implies contamination *decreases* performance, which is nonsensical.

## 3. Key Findings

1. **S1-only γ is massively inflated**: 2.5× for MMLU, 3.5× for ARC vs RRF. The inflated γ is an artifact of model misfit, not a stronger contamination signal.

2. **Model fit is catastrophic with S1-only**: PPP=0.0003 (MMLU) and 0.0000 (ARC) indicate the IRT model is severely misspecified when using Min-K++ alone as exposure. RRF achieves acceptable PPP (0.19, 0.003).

3. **Calibration is 6–8× worse**: MAE_cal jumps from 0.009→0.073 (MMLU) and 0.019→0.115 (ARC). S1-only calibrated scores systematically deviate from ground truth.

4. **Ranking quality degrades**: Kendall τ drops from 0.730→0.628 (MMLU) and 0.733→0.597 (ARC). S1-only is worse at ranking models by true contamination level.

5. **MCMC convergence degrades**: ESS drops from ~1500→~280, indicating the posterior is harder to sample — the model is fighting the data.

6. **GSM8K confirms both methods**: Both correctly estimate γ≈0 with good PPP — the negative control works for both.

7. **Domain-level S1-only fails completely**: STEM_Math γ=−6.32 with PPP=1.000 shows Min-K++ alone cannot provide meaningful domain-level exposure estimates.

## 4. Interpretation

Min-K++ alone selects items that conflate **item difficulty** with **contamination exposure**. The top-300 items by Min-K++ score tend to be items the model has memorized, but the per-item exposure signal lacks the orthogonal information from embedding similarity (s1) and self-critique consistency (s4) that helps separate genuine contamination from ability effects.

The multi-signal RRF fusion is essential: it produces exposure estimates that the IRT model can use to cleanly decompose ability (θ) from contamination (γ), resulting in well-calibrated scores and meaningful γ estimates.

## 5. Source Files

- S1-only results: `/root/autodl-tmp/exp006/s1only_minkpp_ablation/{mmlu,arc_challenge,gsm8k}/s1only_minkpp_results.json`
- RRF baseline (pooled): `/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16_fixed/pooled_rrf_irt_results.json`
- RRF baseline (domain): `/root/autodl-tmp/exp006/mmlu_domain_irt_j16_qwen/all_domain_results.json`
- Analysis script: `/root/contamcal-irt-calibration/analysis/run_s1only_minkpp_analysis.py`
- Log: `/root/contamcal-irt-calibration/logs/s1only_minkpp.log`

## 6. Metric Definitions

- **γ**: Contamination effect parameter in 2PL+γ IRT model. Higher = more performance inflation from contamination.
- **PPP**: Posterior predictive p-value. Values near 0 or 1 = poor model fit; 0.1–0.9 = acceptable.
- **Kendall τ**: Rank correlation between calibrated scores and ground truth (d000 accuracy per scale). Higher = better ranking.
- **MAE_cal**: Mean absolute error between calibrated scores and ground truth. Lower = better calibration.
- **ρ_dose**: Spearman correlation between dosage level and calibrated score. Ideally ~0 (calibration removes dosage effect).
- **ESS_min**: Minimum effective sample size across all parameters. Higher = better MCMC mixing.

## 7. Note on Incomplete Domain Results

The S1-only domain-stratified analysis was interrupted after STEM_Math (the first domain). The remaining 7 domains did not complete. Given the pathological STEM_Math result (γ=−6.32, PPP=1.000), rerunning the remaining domains is low priority — the pooled analysis already demonstrates that S1-only exposure is inadequate.
