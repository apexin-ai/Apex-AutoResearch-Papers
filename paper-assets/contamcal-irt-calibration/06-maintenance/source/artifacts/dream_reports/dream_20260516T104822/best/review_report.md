---
dream_id: dream_20260516T104822
tier: best
overall_score: borderline reject
timestamp: 2026-05-16T11:28:09.472039+00:00
---

# Review Report: ContamCal — Characterizing and Calibrating Benchmark Contamination via Item Response Theory

**Review mode**: Simple (single reviewer, full coverage)
**Venue standard**: Top ML venue, ~25% acceptance rate, 6-point scale

---

## Summary

The paper introduces ContamCal, a two-stage framework that bridges contamination detection signals with Item Response Theory (IRT) to characterize and calibrate benchmark contamination effects. Stage 1 constructs per-item exposure scores via Reciprocal Rank Fusion (RRF) of four detection signals (embedding similarity, Min-K++, ConStat, Self-Critique). Stage 2 fits a contamination-augmented 4PL IRT model with per-benchmark γ_k parameters. Through controlled SFT injection on N=24 models (Qwen2.5 0.5B–7B + Llama-3.2-3B) at varying dosage levels, the paper establishes four claims: (1) contamination is benchmark-dependent (ARC forgetting vs GSM8K inflation), (2) scale-modulated (catastrophic at 0.5B, negligible at 7B), (3) detectable only via specific signals (Min-K++ exhibits directional reversal), and (4) conditionally calibratable (ARC MAE=0.030 vs linear baseline MAE=0.052).

---

## Overall Assessment

**Score: 4 — Borderline Reject**

The paper tackles an important and timely problem with a principled approach grounded in psychometric theory. The experimental design is thorough and the Min-K++ reversal finding is genuinely valuable to the community. However, there is a fundamental tension between the paper's title/framing (calibration) and what it actually delivers (characterization with limited calibration). Only one benchmark (ARC) passes the gating criterion for calibration, coverage at 95% CI is 63% (well below nominal), and the practical impact remains modest. The characterization insights, while valuable, are somewhat expected at the coarse level (larger models are more robust) and need stronger theoretical grounding to justify a top-venue contribution.

---

## Strengths

### S1. Novel and principled problem formulation
Bridging IRT with contamination detection is a creative contribution. The item-compromise IRT literature (Eckerly 2017, Sinharay 2017) is an apt foundation, and the three structural modifications (joint item distribution, continuous exposure, regime-conditional ability) are well-motivated. This is the kind of cross-disciplinary transfer that opens new research directions.

### S2. Comprehensive and honest experimental design
N=24 models across 4 scales (0.5B–7B), 2 model families (Qwen, Llama), 5 dosage levels, and 4 benchmarks is substantial. The paper demonstrates intellectual honesty throughout: excluding 0.5B from MC pooling due to position bias, gating out GSM8K when the signal is insufficient, and attributing the coverage gap to local independence violations rather than hand-waving. This kind of transparent scientific reasoning is commendable.

### S3. Min-K++ reversal finding
The directional reversal of Min-K++ (Cohen's d ∈ [−1.98, −1.28] across 0.5B–3B, confirmed across both model families) is the paper's most citation-worthy empirical contribution. The mechanistic explanation (SFT shifts distribution toward paraphrases, making originals look *less* familiar) is clear and has direct implications for the contamination detection community. This finding alone justifies dissemination.

### S4. Calibration gating as a design principle
The gating criterion (γ CI excludes zero, PPP ∈ [0.1, 0.9], calibrated MAE < raw MAE) is a thoughtful mechanism that prevents the framework from producing overconfident corrections. The GSM8K case — where +43pp inflation is correctly attributed to genuine ability gain rather than contamination — demonstrates that the framework knows when *not* to calibrate.

### S5. Comprehensive experiment coverage
Comparing against the experimental design context, the paper covers all planned experiments: QC validation (exp-015), 7B scale bridging (exp-007), Llama cross-family (exp-014), observational case study (exp-009), 72B frontier (exp-012), and 2-signal degraded mode (exp-013). Nothing was cherry-picked or dropped.

### S6. Fisher Information identifiability analysis
Establishing that reliable γ recovery requires signal AUC ≥ 0.55 at N ≥ 50 is a useful theoretical contribution that sets expectations for practitioners and future work.

---

## Weaknesses

### W1. Title/framing mismatch — the paper undersells characterization and oversells calibration [Major]
The title promises "Calibrating Benchmark Contamination" but the conclusion acknowledges "the framework's primary value is not score correction but systematic characterization." Only ARC passes the calibration gating criterion. GSM8K is gated out. MMLU's aggregate γ ≈ 0 means no calibration applies at the benchmark level. The observational study shows a marginal 0.4pp regret improvement. A top-venue paper should have a clear, coherent identity — this paper is torn between two stories. **Recommendation**: Either reframe as primarily a characterization paper with calibration as a proof-of-concept, or substantially strengthen the calibration results.

### W2. Coverage at 63% is a fundamental limitation for a calibration framework [Major]
63% at nominal 95% CI means the uncertainty estimates are systematically miscalibrated. The paper attributes this to local independence violation (correlated item responses from shared model parameters), which is a well-known IRT issue. But this isn't just a limitation to acknowledge — it undermines the credibility of all reported confidence intervals, including the γ CIs that are central to the claims. The SBC diagnostic is mentioned but results are not shown. If the posterior is miscalibrated, how can we trust that γ = −1.2 with CI [−2.0, −0.4] truly excludes zero? **What's needed**: Full SBC rank histograms, or at minimum, a sensitivity analysis showing how coverage varies with N and model composition.

### W3. N=24 is fundamentally small for a 4PL IRT model [Major]
The 4PL model has 4 parameters per item (a, b, c, d) plus one γ per benchmark. With ~1,172 ARC items and 24 examinees, each item parameter is informed by at most 24 binary observations. Standard IRT practice recommends N ≥ 200–500 for stable 3PL estimation; 4PL+γ is strictly harder. The paper's own identifiability analysis says N ≥ 50 is needed — the experiments don't meet this threshold. The Bayesian framework with informative priors partially mitigates this, but raises the question: how much are the results driven by priors vs. data? **What's needed**: Prior sensitivity analysis (e.g., varying γ prior width, alternative c/d priors) and comparison with simpler models (2PL+γ, 3PL+γ) to assess whether the 4PL complexity is warranted at this sample size.

### W4. SFT injection is a poor proxy for real-world contamination [Moderate]
The paper acknowledges this limitation but doesn't adequately address it. Real contamination occurs through: (a) pre-training data overlap (verbatim or near-verbatim), (b) instruction tuning on benchmark-formatted data, (c) RLHF reward hacking on benchmark-style problems. SFT with paraphrased benchmark items at known dosages is a clean experimental setup but may produce systematically different contamination dynamics. The observational case study (Section 5.8) is intended to bridge this gap, but with mean exposure of 0.032 and all γ CIs including zero, it provides no evidence that ContamCal works on real contamination. **What's needed**: At minimum, a controlled experiment with verbatim (non-paraphrased) contamination to test whether the framework handles different contamination modalities.

### W5. RRF signal aggregation is ad-hoc [Moderate]
The choice of k=60 in RRF, equal weighting of all four signals, and the meta-circularity argument against learned aggregation are insufficiently justified. k=60 is the default from Cormack et al. (2009) for document retrieval — there's no reason to believe it's optimal for contamination detection. The paper shows S1 dominates (AUC ~0.98 vs. S3=0.62, S4=0.56), meaning the other signals contribute noise as much as information. An ablation showing RRF(S1 only) vs. RRF(all 4) would clarify whether the multi-signal approach actually helps or hurts. The 2-signal degraded mode (Section 5.7) partially addresses this but from the wrong direction (removing the *best* signal rather than the worst).

### W6. Statistical reporting gaps [Moderate]
- Bootstrap p=0.03 for MAE comparison is borderline significant — after any multiple comparison correction, this would not survive.
- No effect sizes reported for the calibration improvement (MAE 0.030 vs 0.052 — what is this in practical terms for model selection?).
- The paper reports Kendall τ = 0.87 for cross-family ranking but no confidence interval or significance test for this correlation.
- MMLU Simpson's paradox: "6/8 domains significant" but no correction for multiple comparisons across domains.
- Missing R-hat and ESS values for MCMC convergence diagnostics in the main paper.

### W7. Limited practical impact demonstration [Moderate]
The observational case study shows expected regret improving from 1.8pp to 1.4pp — a 0.4pp improvement. For a framework that requires training 24+ controlled models (hundreds of GPU-hours), running 4 detection signals per item, and fitting a Bayesian IRT model, this improvement is negligible. The paper should more clearly articulate the cost-benefit tradeoff. Under what conditions is ContamCal worth deploying?

---

## Minor Issues

- **M1**: Table 5 is incomplete — B0 Raw has no MAE/Coverage/τ values, and B4 has no Coverage/τ. This makes comparison difficult.
- **M2**: The paper mentions "SBC diagnostic" and "posterior predictive p-values" but doesn't show the actual diagnostic plots. These should be in the paper or supplementary material.
- **M3**: Section 3.4 gating criterion mentions "posterior predictive p-value ∈ [0.1, 0.9]" but Section 5.8 reports PPP values of 0.58–0.72. These seem to come from the observational study but it's unclear if the controlled experiments' PPP values are reported.
- **M4**: The 72B "extension" (Section 5.9) contributes no statistical analysis — it's purely narrative. Either cut it or add value (e.g., using it to validate exposure score calibration at frontier scale).
- **M5**: The paper uses "contamination" and "exposure" somewhat interchangeably. Exposure scores measure similarity to training corpus paraphrases; contamination is the causal effect on performance. The distinction matters.
- **M6**: Reference list has ~30 entries, which is adequate but on the low side for a paper touching IRT, contamination detection, MIA, calibration, and Bayesian inference. Key missing references include DIF (Differential Item Functioning) literature beyond Holland & Wainer, and recent work on benchmark difficulty estimation (e.g., BenchmarkCards, DataComp evaluation frameworks).
- **M7**: The paper doesn't discuss computational cost. How long does the full pipeline take? What are the hardware requirements?

---

## Questions for Authors

1. How sensitive are the γ estimates to the prior specification (γ ~ N(0, 2))? With N=24, the prior likely exerts substantial pull. What happens with γ ~ N(0, 5) or γ ~ N(0, 1)?
2. Have you tried a 2PL+γ or 3PL+γ model? The 4PL c and d parameters are notoriously hard to estimate even with large N — at N=24, are they identifiable?
3. Can you show the full SBC rank histograms? The 63% coverage claim needs this diagnostic to be interpretable.
4. The RRF k=60 constant: did you try other values? What about weighted RRF given S1's dominance?
5. For the observational case study, all exposure scores are 0.032 — identical across all 6 models. Is this a bug or a display artifact? If real, it implies exposure is model-independent, which seems implausible.
6. What is the computational budget for reproducing the full experimental pipeline?

---

## Experiment Coverage Assessment

Comparing the paper against the experimental design (review_context.yaml):

| Experiment | In Paper? | Section | Notes |
|---|---|---|---|
| sft_d100_qc_only (exp-015) | Yes | 5.1 | Fully covered |
| scale_bridging_7b (exp-007) | Yes | 5.2 | Fully covered |
| multi_family_validation (exp-014) | Yes | 5.3 | Fully covered |
| IRT characterization (core) | Yes | 5.4 | Fully covered |
| Calibration performance | Yes | 5.5 | Partially — missing some baselines |
| closed_weight_2signal_mode (exp-013) | Yes | 5.6, 5.7 | Split across two sections |
| rl_observational_case_study (exp-009) | Yes | 5.8 | Fully covered |
| observational_72b (exp-012) | Yes | 5.9 | Narrative only, minimal analysis |

All planned experiments are present. The coverage is good, though the 72B section is thin and some baselines from B0–B6 are not fully reported.

---

## Verdict

The paper addresses an important problem with a principled approach and delivers genuine empirical insights, particularly the Min-K++ reversal finding and the benchmark-dependent contamination taxonomy. However, the calibration claims — which the title foregrounds — are undersupported: only one benchmark is calibratable, coverage is 37% below nominal, and practical impact is marginal. The paper would benefit from (1) reframing as primarily a characterization contribution, (2) strengthening statistical rigor (prior sensitivity, SBC diagnostics, multiple comparison corrections), and (3) demonstrating practical value more convincingly. In its current form, the paper falls just below the acceptance threshold for a top ML venue, though the characterization components are strong enough that a revised version addressing these concerns could be competitive.

**Overall Score: 4 — Borderline Reject**

**Confidence: 4 — High** (familiar with IRT, contamination detection, and Bayesian inference; read full paper and experimental context carefully)
