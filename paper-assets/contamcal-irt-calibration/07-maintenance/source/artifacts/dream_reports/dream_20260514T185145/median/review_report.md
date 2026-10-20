---
dream_id: dream_20260514T185145
tier: median
overall_score: 3/6 — Weak Reject
timestamp: 2026-05-14T20:06:41.824701+00:00
---

# Dream Review Report — CONTAMCAL: Understanding and Calibrating Benchmark Contamination in LLMs

**Dream ID:** 20260514T185145  
**Review Mode:** Full (2-Reviewer Roundtable)  
**Date:** 2026-05-14

---

## Paper Summary

This paper presents CONTAMCAL, a two-stage framework for understanding and calibrating LLM benchmark scores under training data contamination. Stage 1 computes per-item exposure scores via four detection signals (embedding retrieval, Min-K++, ConStat, Self-Critique) aggregated through Reciprocal Rank Fusion (RRF). Stage 2 fits a contamination-augmented 4PL IRT model with per-benchmark susceptibility parameters (γ_k) via Bayesian MCMC (Stan NUTS), producing calibrated scores with credible intervals. The paper claims three contributions ordered by empirical strength: (C1) signal characterization revealing only embedding retrieval is effective while Min-K++ exhibits directional reversal, (C2) Fisher Information identifiability bounds with a practitioner-facing "phase diagram," and (C3) proof-of-concept calibration at 4.2pp MAE with 85% CI coverage.

Experiments use controlled SFT injection on Qwen2.5 (0.5B–7B) across five dosage levels, with N=26 pooled models, 7 baselines, cross-family validation on Llama-3.2-1B, and an RL observational study on 8 Instruct/R1-Distill models.

---

## Reviewer Assignments

- **R1** — Methods & Experiments  
- **R2** — Novelty & Related Work

---

## Consolidated Strengths

**S1. Well-motivated problem with principled framing (R1, R2).** The post-hoc statistical calibration framing — "when mitigation fails, adjust statistically" — is a genuine conceptual advance. The causal inference analogy (adjusting for confounders rather than eliminating them) is apt. The connection to Zhang et al. (2025) showing 20 mitigation strategies fail systematically provides strong motivation.

**S2. Min-K++ directional reversal is a genuinely novel and important finding (R1, R2).** Cohen's d = −1.2 to −2.7 consistently across all three scales and three benchmarks. This warns the community that a widely-used detection method can actively mislead under SFT contamination — not just fail, but point in the wrong direction. This is the paper's most citation-worthy result.

**S3. Fisher Information identifiability analysis is mathematically rigorous and practically useful (R1, R2).** The structural (AUC≥0.55) vs. practical (AUC≥0.70, N≥50) identifiability distinction, validated by the 120-condition simulation sweep (theory/empirical ratio = 0.998), provides actionable guidance via the "phase diagram." The measurement error attenuation formula (Eq. 6) is a clean theoretical result.

**S4. Transparent reporting of failures and limitations (R1, R2).** The paper does not hide that 3/4 signals fail, RRF degrades versus S1-only, γ mostly does not exclude zero, or that coverage is 10pp below nominal. This scientific honesty is rare and valuable. The 0.5B catastrophic forgetting, 3B GSM8K eval artifact, and dose-response monotonicity violations are all openly discussed.

**S5. Controlled experimental design with ground truth (R1).** SFT injection with known contamination labels at 5 dosage levels across 4 scales, with seed replication, provides strong internal validity. The 7 baselines including the direct predecessor DCR provide adequate comparison context.

**S6. Comprehensive simulation validation (R1).** The 120-condition sweep (1,200 runs, 800 CPU-hours) covering AUC × N_models with CI width scaling as O(1/√N) matching theory within 4% deviation provides credible evidence for identifiability claims.

---

## Consolidated Weaknesses

### Major

**W1. N_models = 26 is critically insufficient for the calibration claims (R1-W1, R2-W4). [Consensus]**  
The paper's own simulation sweep shows practical identifiability requires N≥50. At N=20–26, the 95% CI coverage is systematically below nominal (80–86% in simulations). The paper's own Fisher Information analysis establishes thresholds the experiments fail to meet. This is not merely a limitation — it undermines the validity of the reported γ posteriors (Table 8) and the coverage diagnostics (85% vs 95%). The disconnect between the theoretical contribution (C2: "you need N≥50") and the empirical validation (C3: "we used N=26") weakens both claims.

**W2. The 85% vs. 95% CI coverage gap undermines the UQ contribution (R1-W2, R2-W7). [Consensus]**  
A 10pp coverage gap is severe for a framework whose central value proposition over baselines (DCR, Emperor) is formal Bayesian uncertainty quantification. The SBC diagnostic (p=0.04) suggests systematic miscalibration. The paper attributes this to local independence violations but does not formally test this hypothesis or quantify its contribution relative to the sample size effect identified in W1. Without resolving whether this is a model misspecification problem or a sample size artifact, the UQ advantage over baselines is more theoretical than practical.

**W3. Multi-signal framework collapses to single-signal at all tested scales (R1-W3, R2-W3). [Consensus]**  
S1 (embedding retrieval) alone achieves AUC = 0.979, while RRF 4-signal degrades to 0.932 (−4.7pp). S2, S3, and S4 remain near chance (AUC 0.43–0.68) across all three scales (0.5B, 1.5B, 3B). This is not a scale-dependent failure; it is method-specific. The "extensible architecture" framing (RRF benefits when future signals improve) is speculative — at present, the framework is empirically S1 + IRT. The elaborate signal fusion machinery adds complexity without benefit.

**W4. Calibration improvement over baselines is not statistically meaningful (R1-W4, R2-W4). [Consensus]**  
The 4PL+γ model achieves 4.2pp MAE, identical to Emperor mitigation (4.2pp) and only 0.5pp better than DCR (4.7pp). Raw scores achieve 4.4pp MAE. No bootstrap confidence intervals on MAE differences are reported. A 0.2pp improvement over raw scores is within noise. The paper honestly frames this as "proof-of-concept" where the value is UQ not point estimates, but the UQ itself is compromised (W2).

**W5. γ_k posteriors mostly include zero (R1-W5, R2-W4). [Consensus]**  
Only GSM8K (γ = 0.45 ± 0.11) reliably excludes zero. MMLU is marginal (CI: [−0.01, 0.56]). ARC and HumanEval CIs comfortably include zero. This means the framework cannot statistically confirm contamination effects on 3/4 benchmarks. The 62.5% rate of γ excluding zero (concentrated in high-dosage GSM8K conditions) does not constitute strong evidence for the contamination susceptibility parameter.

### Moderate

**W6. SFT injection is a weak proxy for real-world contamination (R2-W5).**  
Real contamination occurs during pre-training, involves orders of magnitude more data, and produces qualitatively different memorization. The RL observational results (S1 AUC drops to 0.58–0.62 on Instruct models) demonstrate that the signal pipeline may be inapplicable to the models people actually evaluate. The paper acknowledges this limitation but the practical utility gap is larger than discussed.

**W7. Dose-response monotonicity violations are concerning (R1-W6).**  
0.5B shows catastrophic forgetting (MMLU −16.5pp at d100 vs d000), opposite to contamination inflation. 3B GSM8K has a +57.7pp artifact from eval format issues. Only 7B shows clean monotonic dose-response. The paper relies on a single scale (7B) for the "contamination → inflation" narrative, while the confounded data from 0.5B (included in the N=26 pool) may bias γ estimates.

**W8. Single model family limits generalizability (R1-W7, R2-W6). [Consensus]**  
All controlled experiments use Qwen2.5. The Llama-3.2-1B cross-family validation (6 runs, 3 dosages) is too small to support generalization claims. The per-benchmark γ_k directional consistency (r = 0.72) is encouraging but the quantitative gap (MAE 5.8pp vs 4.2pp for Qwen) and Llama's CI not excluding zero preclude formal cross-family claims.

**W9. Limited novelty of the 4PL+γ formulation (R2-W1).**  
The core model is a direct application of explanatory IRT (De Boeck & Wilson 2004) with a single added covariate. The three "structural adaptations" (continuous covariates, per-benchmark fitting, regime-conditional signals) are either standard in psychometrics or constitute empirical observations rather than modeling innovations. The differentiation from Eckerly (2017) and Sinharay (2017) is primarily in the application domain. This is competent cross-disciplinary transfer, not a methodological advance.

### Minor

**W10.** MMLU subsampling from 14K to 1K items for NUTS feasibility is a significant unvalidated compromise (R1-W9). Stability across subsamples should be demonstrated.

**W11.** The 2-signal closed-weight mode (AUC = 0.568, MAE = 7.2pp) is below the practical identifiability threshold. Presenting this as a "mode" rather than an acknowledged failure case overstates applicability to closed-weight models (R1-W8).

**W12.** The paper uses "calibration" in a non-standard sense for ML (decontamination, not probability calibration). The disambiguation paragraph exists but the potential for confusion is real.

---

## Questions for Authors

**Q1.** Can you provide simulation results at exactly N=26 and AUC=0.97 (your operating point) to quantify the expected coverage gap from sample size alone, separate from model misspecification?

**Q2.** Have you computed downstream calibration MAE using S1-only exposure scores instead of RRF? If S1-only also yields equal or lower MAE, the multi-signal framework provides no benefit at any stage of the pipeline.

**Q3.** For the 0.5B d100 condition showing catastrophic forgetting: what happens to γ estimates when you exclude 0.5B d100 from the pooled analysis? Does the coverage gap narrow?

**Q4.** The SBC diagnostic p=0.04 — can you report the full SBC rank histogram and identify whether miscalibration concentrates in γ, θ, or item parameters?

**Q5.** GSM8K shows the strongest γ (CI excludes zero) but also the highest MAE among MMLU/ARC/GSM8K. How should a practitioner decide when to apply ContamCal versus trusting raw scores, given they don't know the ground truth?

**Q6.** The Fisher Information analysis assumes known item parameters (conditional information). The observed CI widths are substantially wider than the conditional lower bound. Can you provide marginal Fisher Information (integrated over item parameter uncertainty)?

**Q7.** How sensitive are γ estimates to the Stan prior specification (γ ~ N(0,1))? What happens with γ ~ N(0,5)?

**Q8.** For the Min-K++ reversal: can you provide a more precise mechanistic explanation? Does SFT on contaminated items elevate probabilities on all tokens globally, or specifically on non-contaminated items through knowledge transfer?

---

## Experiment Coverage Assessment

Comparing the paper against the experimental design (review_context.yaml):

| Imagined Experiment | Covered? | Notes |
|---|---|---|
| stage1_signal_pipeline (exp-002) | ✅ Full | Tables 1–2, all 3 scales |
| rrf_aggregation_ablation (exp-003) | ✅ Full | Table 3, including FP robustness |
| irt_calibration_and_baselines (exp-006) | ✅ Full | Tables 7–8, 7 baselines |
| scale_bridging_7b (exp-007) | ✅ Full | Tables 9–10 |
| signal_survival_analysis (exp-008) | ✅ Partial | Instruct degradation in §5.3 but no dedicated table |
| multi_family_validation (exp-014) | ✅ Partial | Table 13 (Llama), §8.2, but minimal (6 runs) |
| rl_observational_case_study (exp-009) | ✅ Full | Table 11, expected regret |
| observational_72b (exp-012) | ✅ Partial | §8.3, one paragraph, no ground truth |
| closed_weight_2signal_mode (exp-013) | ✅ Full | Table 12 |
| simulation_identifiability_sweep (exp-004) | ✅ Full | Tables 4–5, Appendix D |
| noise_propagation_analysis (exp-005) | ✅ Full | Table 6, §6.2 |

Coverage is comprehensive — all imagined experiments appear in the paper, though some (signal survival, multi-family, 72B) receive abbreviated treatment.

---

## Roundtable Convergence

### Areas of Agreement (R1 + R2)
Both reviewers agree on:
1. The Min-K++ directional reversal is the paper's strongest and most novel empirical finding
2. The Fisher Information identifiability analysis is mathematically correct and practically useful
3. N=26 models is below the paper's own recommended practical threshold (N≥50)
4. The coverage gap (85% vs 95%) undermines the central UQ value proposition
5. The multi-signal narrative collapses to single-signal at all tested scales
6. The calibration improvement over baselines is within noise
7. Single model family is a meaningful limitation
8. The paper demonstrates unusual intellectual honesty about its limitations

### Areas of Partial Disagreement
- **Novelty**: R2 rates the IRT formulation as incremental over educational measurement literature; R1 finds the cross-disciplinary transfer more compelling. Resolution: the novelty is moderate — competent transfer of established psychometric methods, with the Fisher Info identifiability analysis as the primary theoretical contribution.
- **Completeness**: R2 initially flagged placeholder tables, but this appears to stem from accessing internal project source files rather than the submitted PDF, which contains complete numerical results. This concern is withdrawn.

---

## Overall Assessment

### Score: 3/6 — Weak Reject

### Justification

The paper addresses an important problem (quantifying rather than eliminating contamination effects) with a principled approach (explanatory IRT with contamination covariates). Two components are solid contributions:

1. **The Min-K++ directional reversal finding** (Cohen's d = −1.2 to −2.7 across all scales) is a genuinely cautionary result for the contamination detection community, worth publishing independently.

2. **The Fisher Information identifiability analysis** provides actionable thresholds (AUC≥0.70, N≥50) backed by a thorough simulation sweep (1,200 runs, 800 CPU-hours, theory/empirical ratio = 0.998).

However, the core calibration contribution (C3) is fatally underpowered:
- N=26 is below the paper's own practical identifiability threshold of N≥50
- The 10pp coverage gap undermines the Bayesian UQ value proposition
- Calibration MAE improvement (0.2–0.7pp over baselines) is not statistically established
- γ excludes zero on only 1/4 benchmarks
- The multi-signal architecture adds complexity while degrading performance vs. S1-only
- Validation is limited to a single model family under idealized SFT contamination

The paper's honest reframing from "calibration framework" to "signal characterization + identifiability + proof-of-concept" is partly justified by the results, but at a top venue (25% acceptance), "proof-of-concept with known underpowering" does not clear the bar. The negative findings (3/4 signals fail, RRF degrades, coverage gap, single-family) outweigh the positive ones in both number and severity.

### Recommendation for Strengthening
To reach acceptance at a top venue, the paper would need:
1. **Increase N_models to ≥50** (complete multi-seed strategy or add more model scales/families)
2. **Diagnose and close the coverage gap** via formal SBC analysis and potential model fixes
3. **Provide bootstrap CIs on baseline MAE differences** to establish statistical significance
4. **Present the framework as S1-driven** (honest current state) with RRF as extensible architecture (future state)
5. **Multi-family validation at ≥3B scale** (e.g., Llama-3-8B or Mistral-7B with controlled SFT)

### Venue Fit
The signal characterization (C1) and identifiability analysis (C2) could form a strong workshop paper or a focused contribution to a dataset & benchmarks track. The full framework with calibration claims would need the experimental improvements above for a main conference paper.

### Confidence: 4/5 (High)
Both reviewers have carefully examined the paper's mathematical formulations, experimental setup, statistical claims, and results tables. The concerns about sample size insufficiency are directly supported by the authors' own simulation sweep. The coverage gap and signal effectiveness issues are quantitatively documented in the reported results.
