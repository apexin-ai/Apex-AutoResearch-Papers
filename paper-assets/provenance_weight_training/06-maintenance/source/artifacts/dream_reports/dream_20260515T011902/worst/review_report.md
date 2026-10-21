---
dream_id: dream_20260515T011902
tier: worst
overall_score: weak reject
timestamp: 2026-05-15T02:26:07.965746+00:00
---

# Dream Review Report: Adaptive Provenance Weighting for Contaminated Pretraining Corpora

**Dream ID:** 20260515T011902 | **Review Mode:** full | **Reviewers:** R1 (Methods+Experiments), R2 (Novelty+Related Work)

---

## Roundtable Summary

Both reviewers converge on **Weak Reject (3/6)**. The paper addresses a real problem (automated b selection for provenance-weighted pretraining) but the proposed solution has fundamental methodological and empirical shortcomings that place it below the acceptance threshold for a top ML venue.

---

## Reviewer R1: Methods and Experiments

**Score: 3 (Weak Reject) | Confidence: 4/5**

### Strengths

- **S1: Well-motivated problem.** The observation that Drayson et al.'s b requires per-model validation-based grid search, impractical for web-scale pretraining, is a genuine pain point.
- **S2: Honest self-assessment.** The paper's characterization of adaptive b* as a "contamination thermometer, not an optimizer" that "overshoots by ~4×" and serves as a "reasonable default recovering ~70%" is refreshingly candid. The identification of failure modes (cross-gen, domain-skew) strengthens credibility.
- **S3: Lightweight detector finding is practically valuable.** TF-IDF+LR achieving near-equivalent training outcomes to ModernBERT-150M (0.003 PPL difference) is genuinely useful for practitioners, if confirmed with more seeds.
- **S4: Thorough ablation coverage.** The n_min sweep, detector quality comparison, contamination rate variation, cross-generator test, domain-skew test, and baseline comparisons represent a comprehensive ablation suite.

### Weaknesses

- **W1: The α̂_eff "theoretical framework" adds no value to b* selection.** Since α̂_eff(b) is monotonically non-decreasing in b, maximizing α̂_eff subject to ESS ≥ n_min always selects the largest feasible b. The entire theoretical apparatus reduces to "pick the largest b such that ESS(b) ≥ n_min." The α̂_eff framework contributes nothing beyond the ESS constraint — it is a complex way to state a simple threshold rule.

- **W2: Effect sizes are at or below the noise floor.** The core improvement is 0.040 PPL (0.23% relative) on a base of ~17.69. Cross-seed variance in uniform baselines spans 0.010 PPL. The adaptive-vs-grid-best gap (0.013 PPL, 0.07% relative) is within seed variance (~0.007 std). No confidence intervals or significance tests are reported for the primary claim.

- **W3: n_min is a fragile hyperparameter with an extremely narrow sweet spot.** With batch_size=4, only n_min=2 works. n_min=1 over-downweights (PPL worse than uniform), n_min ≥ 3 degenerates to uniform. The "hyperparameter-free" framing is undermined: one difficult continuous hyperparameter (b ∈ [0.1, 10]) is replaced by another with a single effective integer value.

- **W4: Single-seed results dominate critical experiments.** The ρ=0.6 comparison, cross-model scaling (3B), cross-generator, domain-skew, and downstream evaluations all use a single seed. For effect sizes this small, single-seed results are scientifically uninformative.

- **W5: Evaluation scale is insufficient for claims.** 200M tokens / 0.6B parameters is a toy setting for pretraining research. The 3B experiments at 200M tokens (63 tokens/parameter, vs ~1200× Chinchilla-optimal) are so severely undertrained that downstream metrics are at chance level (MMLU 25.8% ≈ random 25%).

### Questions for Authors

1. Given that α̂_eff(b) is monotonically non-decreasing, why frame b* selection as "maximizing α̂_eff"? The ESS constraint alone determines b*. What does the α̂_eff framework contribute beyond the ESS constraint?
2. With batch_size=4 and n_min=2, ESS touches 2.0 for the majority of batches. Have you run experiments with larger batch sizes (e.g., 16, 64) where the ESS dynamic range would be wider and the n_min sweet spot potentially broader?
3. The loss reweighting vs. SIR comparison is listed as a contribution, but the paper states "a full gradient variance analysis under both implementations remains future work." Can you provide an empirical comparison, or should this claim be removed?
4. How was the grid {0.1, 0.2, ..., 5.0} chosen? Was the low-b range (0.1–0.3) included from the start or added after initial results with b ≥ 0.5?

---

## Reviewer R2: Novelty and Related Work

**Score: 3 (Weak Reject) | Confidence: 4/5**

### Strengths

- **S1: Honest presentation of negative results.** The paper forthrightly reports that adaptive b* overshoots by 4×, fails in cross-gen and domain-skew settings, and doesn't adapt to model scale. This is more valuable to the community than inflated claims.
- **S2: Detector sufficiency finding.** The demonstration that AUC 0.939→0.986 (+5% relative) yields only 0.003 PPL improvement is a clean, actionable result. The argument that w=(1−q)^b's monotonicity makes ranking more important than calibration is theoretically sound.
- **S3: Clean positioning against Drayson et al.** The paper clearly identifies the gap it targets (validation-based grid search over b) and is transparent about how far it closes that gap (~70%).
- **S4: Failure mode analysis adds value.** Cross-generator degradation (AUC 0.939→0.891 causing adaptive to lose to uniform) and domain-skew amplification are important boundary conditions that future work can build on.

### Weaknesses

- **W1: The core method underperforms its own baseline and fails in realistic conditions.** Adaptive b* recovers only 70% of grid-best improvement in the favorable setting, and actively *hurts* in cross-generator (Table 7: +0.02 PPL vs uniform) and domain-skewed (Table 8: +0.03 PPL vs uniform) scenarios. Cross-generator contamination and domain-skewed injection are the *norm* in real web corpora, not edge cases. The method works only in the easiest setting (single known generator, uniform injection).

- **W2: No genuine theoretical contribution.** α̂_eff(b) is a weighted mean of sample weights — a standard quantity in importance sampling literature. The ESS constraint is textbook importance sampling diagnostics (Kish's ESS). The convergence bound from prior work is explicitly disclaimed as a contribution. The paper assembles standard components without producing novel theoretical insight.

- **W3: The "diagnostic framework" framing is a retreat, not a contribution.** The paper reframes adaptive b* from "replaces grid search" to "diagnostic tool whose b* trajectory reveals contamination structure." But the diagnostic claim is supported only by the observation that b* shifts from 0.87 to 1.08 when ρ changes from 0.4 to 0.6 — a single directional check. No systematic validation of diagnostic accuracy is provided. Any monotone statistic of q-scores would shift with contamination level.

- **W4: Loss reweighting vs. SIR comparison is unsubstantiated.** Listed as contribution #3, but the paper provides only conceptual bullet points (granularity, gradient variance, adaptivity) with no experiments. The paper itself acknowledges "a full gradient variance analysis under both implementations remains future work." This should not be listed as a contribution.

- **W5: Missing related work on importance weighting.** The ESS-constrained importance weighting approach has extensive precedent in the survey sampling, Bayesian inference (Pareto-smoothed importance sampling, Vehtari et al. 2024), and off-policy RL (per-decision importance sampling with ESS truncation) literatures. The paper cites none of these, positioning the ESS constraint as if it were novel to this domain.

### Contribution Calibration

The three claimed contributions are:
1. **Lightweight detector sufficiency** — This is an empirical observation, not a methodological contribution. It is valid and useful but could be a workshop paper finding or a section within a larger study.
2. **α̂_eff(b) as diagnostic framework** — This is the weakest claim. α̂_eff is a weighted mean; claiming it as a "framework" overstates its conceptual depth. The diagnostic value is demonstrated with a single contamination-level comparison.
3. **Loss reweighting vs. SIR** — Not delivered. No experiments, acknowledged as future work.

The most honest and defensible contribution is: "We ran comprehensive experiments on provenance weighting across multiple axes (detector quality, contamination ratio, model scale, n_min sensitivity, cross-generator, domain-skew) and provide practical guidelines." This is a valuable empirical contribution but framed as a methods paper, it falls short.

### Questions for Authors

1. Can you provide any formal connection between α̂_eff(b) and the convergence bound d(P̂_t, P_0) ≲ t^{−min{p,α}} beyond "motivation"? Without this, the theoretical framing is decorative.
2. The paper claims adaptive b* "adapts" per-batch, but with n_min=2 and batch_size=4, how much does b* actually vary across batches? What is the coefficient of variation of b* across batches within a single training run?
3. How would you position this work against standard ESS-truncated importance weighting from the survey sampling / Bayesian inference literature (e.g., Vehtari et al.'s Pareto-smoothed IS)?
4. What is the minimum detector AUC needed for adaptive b* to be beneficial rather than harmful? The paper shows AUC=0.939 works and AUC=0.891 fails — is there a threshold?

---

## Roundtable: Cross-Review Convergence

### Points of Agreement (Both Reviewers)

1. **The paper is honest and well-structured.** Both reviewers commend the candid reporting of negative results, failure modes, and limitations. This is genuinely valuable.
2. **Effect sizes are at the noise floor.** 0.040 PPL (0.23% relative) is marginal. No downstream transfer is demonstrated.
3. **n_min fragility is a serious concern.** The single-point sweet spot (n_min=2 at batch_size=4) undermines the "hyperparameter-free" value proposition.
4. **The α̂_eff framework is theoretically thin.** R1 identifies that it reduces to ESS thresholding; R2 identifies it as standard importance sampling diagnostics. Both agree the "theoretical contribution" framing is overstated.
5. **Lightweight detector sufficiency is the strongest finding.** Both reviewers agree this is actionable and practically valuable, though it is an empirical observation rather than a methodological advance.
6. **Loss reweighting vs. SIR comparison is undelivered.** Both flag this as a claimed contribution with no supporting experiments.
7. **The method fails in realistic conditions.** Cross-generator and domain-skewed results show adaptive b* losing to uniform — the method is most fragile precisely where it would be most needed (diverse web corpora).

### Areas of Emphasis Difference

- R1 focuses more on **statistical rigor**: missing confidence intervals, single-seed limitations, fragility of recovery ratio arithmetic.
- R2 focuses more on **novelty assessment**: ESS-constrained importance weighting as a known technique, missing related work from survey sampling / Bayesian inference, contribution calibration.

Both perspectives reinforce the same conclusion: the paper does not clear the bar for a top ML venue.

---

## Consolidated Assessment

### Overall Score: 3 (Weak Reject)

### Key Reasons for Rejection

1. **Methodological contribution is thin.** The adaptive b* derivation reduces to "pick the largest b satisfying ESS ≥ n_min" — a direct application of textbook importance sampling diagnostics, not a new technique. The α̂_eff framework adds no information beyond the ESS constraint.

2. **The method fails where it matters most.** Adaptive b* loses to uniform training under cross-generator contamination and domain-skewed injection — the default conditions in real web corpora. A method that only works with single-source, uniformly-distributed synthetic contamination has narrow applicability.

3. **Effect sizes are marginal throughout.** The best improvement is 0.040 PPL (0.23% relative) in a toy 200M-token setting, with no downstream transfer. Even this improvement drops to ~70% of grid-best when the grid is properly extended to low-b values. Statistical significance is not established.

4. **Undelivered contributions.** The loss reweighting vs. SIR comparison is listed as a contribution but acknowledged as future work. The "diagnostic framework" claim rests on a single directional contamination-level check.

### What Would Strengthen the Paper

- **Scale up**: 1B+ tokens, Chinchilla-adequate training for the 3B model, to establish whether effect sizes grow or remain negligible.
- **Address n_min fragility**: Test with batch_size ∈ {16, 32, 64} to see if the sweet spot broadens.
- **Deliver the SIR comparison**: Run matched experiments with SIR resampling vs. loss reweighting.
- **Strengthen the diagnostic claim**: Validate α̂_eff as a contamination estimator across multiple contamination rates with calibration curves.
- **Position as an empirical study**: Reframe from "methods paper with α̂_eff framework" to "comprehensive empirical investigation of provenance weighting design choices," with detector sufficiency and failure mode analysis as primary contributions. This framing better matches the actual evidence.

### Verdict for Authors

The paper's greatest strength is its honesty. The comprehensive experimental coverage, candid reporting of failure modes, and the detector sufficiency finding are all valuable. However, the methodological contribution (adaptive b*) does not work well enough to anchor a top-venue paper: it overshoots by 4×, has a fragile hyperparameter, and fails in realistic contamination scenarios. We recommend either (a) substantially improving the method to close the overshoot gap, or (b) repositioning as a primarily empirical contribution focused on detector sufficiency and practical guidelines for provenance weighting, dropping the α̂_eff framework as a claimed theoretical contribution.
