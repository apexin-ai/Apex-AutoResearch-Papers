---
dream_id: dream_20260514T171536
tier: worst
overall_score: 3/6 Weak Reject
timestamp: 2026-05-14T18:43:40.345037+00:00
---

# Dream Review Report — Full Roundtable

**Paper:** "When Contamination Signals Fail: An Empirical Anatomy of Detection Reliability and Identifiability Boundaries for Contamination-Aware LLM Evaluation"

**Review Mode:** Full (2 Reviewers + Roundtable)
**Venue Standard:** Top ML venue, ~25% acceptance, 6-point scale

---

## Panel Summary

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Methods + Experiments | 2 (Reject) | 4/5 |
| R2 | Novelty + Related Work | 3 (Weak Reject) | 4/5 |
| **Consensus** | — | **3 (Weak Reject)** | **4/5** |

---

## 1. Paper Summary

The paper studies the reliability of four contamination detection signals (embedding similarity, Min-K++, ConStat, Self-Critique) across model scales (0.5B–7B Qwen2.5, Llama-3.2-1B cross-family), four dosage levels (0%–100%), and four benchmarks under controlled SFT paraphrase injection. It proposes ContamCal, a contamination-augmented 4PL IRT model with Bayesian uncertainty quantification, positioned as a proof-of-concept diagnostic framework. Three main findings: (1) Min-K++ exhibits directional reversal under paraphrased contamination (Cohen's d from −1.98 to −2.7); (2) identifiability boundaries at AUC ≥ 0.80 for calibration feasibility; (3) GSM8K accuracy gains are confounded with format learning. ContamCal honestly underperforms raw scores (MAE 8.7 vs 4.2 pp).

---

## 2. Strengths

### S1. Min-K++ Directional Reversal (R1+R2 agree: strongest contribution)
The finding that Min-K++ not only fails but *reverses direction* under SFT paraphrased contamination (Cohen's d from −1.98 at 0.5B to −2.7 at 3B) is **genuinely novel and practically significant**. This is confirmed across model families (Llama d = −1.2) and worsens with scale. Any study using Min-K++ to detect paraphrased contamination in SFT-trained models risks systematic false positives on clean items. This finding alone has immediate implications for the contamination detection community and could anchor a focused empirical paper.

### S2. Comprehensive Controlled Experimental Design (R1+R2)
The factorial design (4 signals × 3+ scales × 4 dosages × 4 benchmarks × 2 families) is more thorough than any prior contamination signal study. The controlled SFT injection provides ground truth that observational studies lack. Coverage of all planned experiments (9 experiments from the design document) is complete.

### S3. Commendable Honesty About Negative Results (R1+R2)
The paper does not hide that ContamCal underperforms raw scores. Tables 3 and 8 clearly show calibration introducing more noise than it removes. The "proof-of-concept that exposes failure modes" framing is refreshingly transparent compared to papers that cherry-pick favorable metrics.

### S4. Fisher Information Identifiability Analysis (R1)
The derivation connecting exposure signal quality (AUC) to γ identifiability via I(γ_k) ∝ Σ τ²·a²·P(1−P) is technically sound. The simulation sweep (144 conditions) establishing AUC ≥ 0.80 as a practical threshold provides actionable guidance. The measurement error attenuation result (reliability ratio) offers genuine theoretical insight.

### S5. Signal Landscape Characterization (R1+R2)
The systematic mapping of which signals work under which conditions — method-specific rather than scale-dependent — is a useful empirical contribution. The finding that RRF degrades below S1-only (AUC 0.979 → 0.83) when most constituent signals are noise is an important cautionary result for fusion-based detection.

### S6. Format Learning Confound Documentation (R2)
The observation that GSM8K's 12%→70% accuracy jump under 100% dosage SFT at 0.5B reflects chain-of-thought format learning rather than content memorization is well-argued, with three lines of evidence presented (equal original/paraphrase gains, γ confounding, 7B dosage sensitivity).

---

## 3. Weaknesses

### W1 [Critical, R1+R2]: ContamCal Calibration Fails — Not Just Underperforms, but Actively Hurts
The central negative result is severe: ContamCal (MAE 8.7 ± 3.0 pp) is **more than twice as bad as raw scores** (MAE 4.2 ± 1.8 pp). This is not a marginal shortfall — it means using the proposed method makes evaluation *less accurate* than doing nothing. Kendall's τ drops from 0.72 (raw) to 0.65 (ContamCal), and 95% CI coverage is only 0.72 (vs nominal 0.95) with intervals averaging 18.5 pp wide. The expected regret analysis in the RL case study confirms this: calibration *increases* model selection regret (0.11 vs 0.08). Even the linear regression baseline (MAE 8.1) fails, suggesting the fundamental issue is signal quality, not model choice — but this means the paper's IRT-specific contributions add nothing beyond what a linear model provides.

### W2 [Critical, R1]: Insufficient N_models for IRT Model Identifiability
The paper's own simulation study identifies N ≥ 50 models as necessary for reliable γ recovery, yet the actual experimental design has only ~4 models per scale (d000/d005/d025/d100) and ~15 when pooled. The 4PL model has 4J + N + 1 parameters; with J = 1319 (GSM8K items) and N = 4, that is ~5300 parameters for ~5300 observations — the model is fundamentally unidentifiable. This is not a minor technical issue but a structural flaw in the experimental design that undermines all IRT-specific claims.

### W3 [Critical, R1]: MCMC Diagnostics Indicate Serious Model Misfit
The reported diagnostics collectively disqualify the posterior inference:
- Divergent transitions at 2.5% (standard threshold: < 0.1%)
- Posterior predictive check p = 0.03 (indicates systematic misfit)
- Residual correlation 0.18 (substantial local independence violation)
- ESS_min = 380 (marginal for a model with this many parameters)

The paper acknowledges these issues but proceeds to draw conclusions from the posteriors anyway. Divergent transitions at 25× the acceptable threshold mean the sampler is not reliably exploring the posterior geometry. Results derived from these MCMC chains should be treated with extreme caution.

### W4 [Major, R1+R2]: SFT Paraphrase Injection Is a Poor Proxy for Real Contamination
The LoRA SFT injection protocol produces qualitatively different contamination dynamics from real-world pre-training contamination:
- Contamination effects are tiny (≤ 6 pp at 7B, ≤ 2 pp MMLU) vs. literature reports of 8–15 pp under verbatim contamination
- At 0.5B, contamination causes *negative* net effects (catastrophic forgetting dominates)
- The dose-response relationship is non-monotonic (violating IRT model assumptions)
- Format confounds (CoT learning) dominate content memorization effects

This severely limits external validity. The paper's findings may be specific to "SFT paraphrase contamination at small scale" — a regime that may not represent the contamination practitioners actually care about.

### W5 [Major, R2]: Multi-Signal Framing Masks Single-Signal Reality
The paper's architecture assumes four informative signals aggregated via RRF, but the empirical reality is that only S1 (embedding similarity) works at any scale. S2–S4 are random noise (AUC 0.45–0.55). RRF actively *dilutes* S1 (Table 5: AUC drops from 0.979 to 0.83). The 2-signal closed-weight mode is completely untenable (MAE 12.0 pp, 3× worse than no adjustment). The multi-signal framework is an architectural choice without empirical justification in this setting.

### W6 [Major, R2]: Limited Novelty in the IRT Framework
ContamCal's 4PL+γ model is a direct application of explanatory IRT (De Boeck & Wilson, 2004) with a contamination covariate — adding a linear term γ·τ to the ability parameter is precisely what this literature prescribes. The measurement error model is standard. The three "structural adaptations" (continuous exposure, measurement error, per-benchmark γ) are either standard IRT techniques or, in the case of the measurement error model, shown to underperform the simpler variant in finite samples.

### W7 [Moderate, R2]: GSM8K Confound Undermines the Only Significant γ
Table 4 shows only GSM8K's γ CI excludes zero (γ = 0.45, CI [0.08, 0.82]). But the paper itself demonstrates this estimate captures format learning rather than contamination. This means *none* of the four benchmarks produce a reliable, interpretable contamination effect estimate — the IRT model's distinctive output (per-benchmark γ) is uninformative across the board.

### W8 [Moderate, R1+R2]: Cross-Family Validation Reveals Non-Transferability
Table 7 shows γ estimates are family-specific (cross-family correlation r = 0.15), GSM8K dosage response differs dramatically (+13 pp Llama vs 0 pp Qwen at d100), and the γ_MMLU sign flips between families. This means any calibration would need to be fit per-family, further limiting practical applicability.

### W9 [Minor, R2]: Missing Related Work
- Membership inference foundations (Shokri et al. 2017, Carlini et al. 2022) — Min-K++ is a MIA method; the reversal finding should be contextualized against this literature
- Alternative evaluation paradigms that bypass contamination (Chatbot Arena, HELM)
- Burnell et al. 2023 on multidimensional IRT for LLMs (relevant to the unidimensional θ limitation)
- Deeper engagement with DCR (Oren et al. 2024) as a structural comparison

---

## 4. Questions for Authors

1. **Practical utility:** Given MAE 8.7 vs 4.2 pp, under what concrete scenario would a practitioner use ContamCal over raw scores? The paper argues for "honest uncertainty quantification," but the CIs are miscalibrated (72% coverage at nominal 95%) — in what sense is this uncertainty "honest"?

2. **N_models gap:** The simulation requires N ≥ 50 for identifiability, but the experiment uses N ≈ 4–15. Did you attempt to pool models across families/scales to increase N? If so, what prevented it? If not, why was this discrepancy not addressed in the experimental design?

3. **MCMC reliability:** With 2.5% divergent transitions (25× threshold), how do you justify drawing conclusions from these posteriors? Have you tried reparameterization, tighter priors, or simpler models (2PL+γ) to achieve reliable inference?

4. **Verbatim contamination:** Your protocol only tests paraphrased SFT contamination. Given that signal reliability may differ fundamentally under verbatim contamination (where Min-K++ is designed to work), do you plan experiments under verbatim regimes? Without these, the paper's scope claims about "contamination signals" in general are overstated.

5. **Why not just S1?** Given that only S1 works, have you evaluated a simplified pipeline using S1 alone with a simple threshold or regression? The full IRT machinery adds complexity without apparent benefit in this signal regime.

6. **Format confound resolution:** The paper identifies the GSM8K confound but proposes no solution. Have you considered controlling for format by evaluating on a reformatted test set, or using a format-invariant evaluation metric?

---

## 5. Experiment Coverage Assessment

Comparing against the full experiment design (review_context.yaml, 9 planned experiments):

| Experiment | Covered? | Comment |
|-----------|----------|---------|
| exp-002: Signal pipeline | ✓ | Table 1, comprehensive |
| exp-003: RRF ablation | ✓ | Table 5 |
| exp-006: IRT calibration | ✓ | Tables 3–4, but N_models issue undermines results |
| exp-007: 7B bridging | ✓ | Table 6 |
| exp-008: Signal survival | ✓ | Tables 1–2 |
| exp-009: RL observational | ✓ | Section 11.2, appropriately scoped as limited |
| exp-012: 72B observational | ✓ | Section 11.3, brief |
| exp-013: Closed-weight 2-signal | ✓ | Table 8 |
| exp-014: Cross-family | ✓ | Table 7 |
| exp-015: QC ablation | ✓ | Table 9 |

All planned experiments are reflected in the paper. The experiment plan itself anticipated the negative results, so coverage is consistent. The key issue is not missing experiments but that the experimental design's structural limitations (N_models, SFT proxy, signal landscape) prevent the IRT framework from demonstrating its value.

---

## 6. Roundtable Convergence

### Points of Agreement (R1+R2)
- Min-K++ directional reversal is the paper's genuine and strongest contribution
- ContamCal calibration fails in practice — this is not just a marginal negative result but a fundamental one
- N_models is structurally insufficient for IRT identifiability
- The paper should be reframed as an empirical anatomy paper with Min-K++ reversal and signal landscape mapping as primary contributions, rather than a calibration framework paper
- The honest reporting of negative results is commendable but insufficient to reach the acceptance bar

### Points of Disagreement
- R1 emphasizes MCMC reliability as disqualifying (leans Reject); R2 gives partial credit for diagnostic framing (leans Weak Reject)
- R2 finds the identifiability boundary analysis more novel than R1 (who views it as routine psychometric theory)
- Resolution: The MCMC issues are real but the paper doesn't rely solely on the MCMC posteriors — the signal landscape and reversal findings stand independently. This tips the consensus toward Weak Reject rather than Reject.

### Consensus Score Rationale
**Score: 3 (Weak Reject)**. The paper contains one genuinely novel empirical finding (Min-K++ reversal, potentially publishable on its own) and useful signal landscape characterization, but the central IRT calibration framework adds complexity without demonstrated value over simpler alternatives. The N_models insufficiency, MCMC misfit, limited external validity of SFT paraphrase injection, and the fact that calibration is worse than no adjustment collectively prevent acceptance. A significantly revised version focusing on the empirical anatomy (signal reliability, Min-K++ reversal, identifiability boundaries) without the IRT calibration claims — or with a substantially strengthened calibration evaluation (N ≥ 50 models, verbatim contamination, reliable MCMC) — could be competitive.

---

## 7. Actionable Recommendations for Revision

1. **Reframe as empirical anatomy paper.** Lead with Min-K++ reversal and signal landscape mapping. Demote ContamCal to a brief section or appendix.

2. **Increase N_models dramatically.** Pool across seeds, scales, families, and training checkpoints to reach N ≥ 50. Without this, IRT-specific claims are unsupported.

3. **Add verbatim contamination experiments.** The current findings are specific to paraphrased SFT contamination. Verbatim experiments would test whether signals (especially Min-K++) behave differently and whether calibration succeeds in a higher-effect-size regime.

4. **Fix MCMC or switch to simpler models.** Either resolve the divergent transitions and misfit (reparameterization, 2PL, informative priors) or acknowledge that the Bayesian IRT approach is infeasible at current sample sizes and present the linear regression baseline as primary.

5. **Contextualize Min-K++ reversal in MIA literature.** Connect the finding to membership inference attack literature (Shokri et al. 2017, Carlini et al. 2022) to broaden the paper's impact.

6. **Address the "why not just S1?" question.** If only one signal works, the multi-signal architecture needs stronger motivation or should be dropped.

---

## 8. Overall Assessment

**Overall Score: 3 / 6 (Weak Reject)**
**Confidence: 4 / 5 (High)**

The paper tackles an important and timely problem with a thorough experimental design and commendable honesty. The Min-K++ directional reversal is a genuinely novel finding with immediate community implications. However, the core IRT calibration framework — the paper's primary technical contribution — fails to demonstrate value over raw scores or even a simple linear baseline, is undermined by insufficient sample sizes for the model's parameterization, and produces unreliable MCMC inference. The honest negative-result framing partially mitigates these issues but cannot substitute for a working method or a clean reframing that matches the paper's actual contributions to its claims. With significant revision (reframing, more models, verbatim experiments), the empirical anatomy components could form a strong submission.