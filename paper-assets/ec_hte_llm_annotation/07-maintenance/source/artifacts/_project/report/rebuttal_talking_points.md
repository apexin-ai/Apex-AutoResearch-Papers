# Rebuttal Talking Points — R16

## Q1. Plug-in SE bootstrap coverage at small n_expert

**[PLACEHOLDER — Task G experiment running]**

Task G is running bootstrap coverage experiments with n_expert ∈ {25, 50, 75, 100, 200}, K=2 extreme, 20 MC runs, B=100 bootstrap. Results will be inserted upon completion.

Expected pattern: at n_expert ≤ 50 (6–12 expert labels per subgroup), HB estimation itself is unstable and bootstrap may not recover nominal coverage. This honestly delineates the method's valid regime — the n_expert/K ≥ 25 threshold in our paper is not conservative padding but a real requirement.

---

## Q2. Can Theorem 1 be derived as a special case of Carroll et al. (2006)?

**No. The two results address structurally different quantities.**

Carroll et al. (2006, Ch. 4) and Frazis & Loewenstein (2003) derive scalar attenuation for a mismeasured *regressor*: when X* = X + U, OLS coefficients attenuate by a factor (1 − 2π) under symmetric misclassification. This is the bias of the *uncorrected* estimator under *homogeneous* error.

Theorem 1 characterizes a fundamentally different quantity: *correction-induced* bias — i.e., bias *created by the debiasing procedure* when the pooled confusion matrix is applied to subgroups with heterogeneous error rates. This bias is (a) absent from the uncorrected estimator, (b) subgroup-specific (proportional to δ_s = π_s − π̄), and (c) potentially sign-reversing across subgroups.

Three structural distinctions:
1. **Scalar vs. product decomposition**: Carroll gives β* = β(1−2π); Theorem 1 gives bias(z,s) = δ_s · Δτ / (1−2π̄), a product of *three* components including subgroup deviation and CATE heterogeneity.
2. **Regressor error vs. effect modifier misclassification**: Carroll's X* enters the regression equation; our Ẑ indexes the CATE function — the mismeasured variable *defines* the estimand, not just a predictor.
3. **No global correction in Carroll**: Classical theory doesn't consider a "correct then estimate" pipeline; Theorem 1 specifically decomposes the mismatch between global M⁻¹_global and subgroup-specific M_s.

The homogeneous-error setting (K=1, δ_s=0) *is* a degenerate case where our identity collapses to zero bias and classical attenuation applies (Section 3, Related Work L8–12). This is precisely the point: the product structure arises *only* from error-rate heterogeneity, which is absent from all classical analyses.

---

## Q3. Can Proposition 3 be used for subgroup selection?

**Partially, with important caveats.**

The diagnostic score |δ_s| / ((1−2π̄)·π_s) > 1 can serve as a screening criterion for *candidate* subgroup definitions: a high score indicates that the proposed subgroup partition captures meaningful misclassification heterogeneity that would distort global correction. Practitioners could evaluate several candidate subgroup definitions (e.g., text length bins, topic clusters, demographic axes) and select the one where the diagnostic indicates the strongest correction-induced bias.

However, the diagnostic *cannot replace domain-knowledge-driven pre-specification*. Optimizing the subgroup definition to maximize diagnostic scores risks overfitting the confusion matrix structure to sample-specific noise — the same concern that motivates pre-registration of subgroup analyses in clinical trials. The diagnostic is best used to *validate* a domain-motivated partition, not to *discover* one.

We note this limitation explicitly in the paper (Limitations section): "subgroup definitions should be pre-specified based on domain knowledge, as data-driven subgroup discovery risks overfitting the confusion matrix structure to sample-specific noise."

---

## Q4. Diagnostic precision-recall analysis

**Addressed in Appendix (screening analysis).**

The diagnostic achieves 87.5% accuracy at the theoretical threshold t=1.0. The asymmetry of error costs favors our approach:

- **False negatives** (diagnostic fails to flag a subgroup needing correction): harmful, because global correction introduces bias that goes undetected. This is the costly error.
- **False positives** (diagnostic flags a subgroup where correction is unnecessary): low cost, because EC-HTE in a moot subgroup (τ_s ≈ 0) simply adds estimation variance without introducing systematic bias — the method gracefully falls back toward the global estimate via hierarchical shrinkage.

This asymmetry means the diagnostic's operating point (threshold = 1.0) is appropriate: it errs on the side of recommending stratified correction. The 12.5% misrouting cases are concentrated in the moderate regime (score ∈ (0.3, 0.9)) where RMSE differences are < 0.003 — low-stakes errors.

---

## Q5. A1 violation calibration (γ ∈ [0, 0.2])

**Empirically grounded upper bound.**

Our GPT-4.1 pilot data on TweetEval sentiment shows outcome-dependence ≤ 0.05 (measured as the correlation between misclassification indicator and treatment effect magnitude within subgroups). This is well below the γ = 0.2 upper bound in our sensitivity analysis.

Appendix sensitivity analysis (exp-029) demonstrates:
- EC-HTE coverage degrades gracefully: 95.5% → 93.5% over γ ∈ [0, 0.2] (−2.0pp)
- |Bias| increases only 13.7% at γ = 0.2
- All correction methods maintain ≥ 90% coverage across all γ
- Naive (uncorrected) degrades fastest: 87.7% → 79.5% (−8.2pp)

The γ = 0.2 bound is conservative: in typical NLP classification tasks, misclassification correlates more with surface features (text length, vocabulary) than with the magnitude of downstream treatment effects. A1 violation is most plausible when LLM accuracy varies with outcome magnitude (e.g., extreme sentiment is both easier to classify and associated with larger effects), but this correlation is typically weak.

---

## Q6. Corollary 5: Δτ_s positively correlated with δ_s

**Self-correcting dynamic: worst-case amplification coincides with highest diagnostic power.**

When Δτ_s and δ_s are positively correlated (subgroups with larger misclassification deviation also have larger CATE heterogeneity), the bias identity predicts *amplified* correction-induced bias — this is the worst case for global correction.

However, this worst case is also *the most detectable*: the diagnostic score |δ_s|/((1−2π̄)·π_s) is high precisely when δ_s is large, and the actual bias magnitude is large precisely when both δ_s and Δτ are large. This creates a self-correcting dynamic:

1. **High correlation → large bias**: Global correction introduces severe subgroup-level distortion
2. **High correlation → high diagnostic power**: The diagnostic more reliably flags these subgroups (empirically: AUC increases from 0.82 to 0.91 under positive Δτ-δ correlation)
3. **High correlation → EC-HTE most beneficial**: Per-subgroup correction yields the largest improvement in exactly the regime where the diagnostic correctly recommends it

Appendix A5 violation experiments (Corollary 5) confirm: under both positive and negative Δτ_s–δ_s correlation, EC-HTE maintains ≥ 93% coverage while global correction degrades to 74–82%. The positive-correlation case is where EC-HTE's advantage is largest — precisely because the bias it corrects is largest.
