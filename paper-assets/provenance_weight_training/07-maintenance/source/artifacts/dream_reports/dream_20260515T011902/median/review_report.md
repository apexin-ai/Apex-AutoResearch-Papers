---
dream_id: dream_20260515T011902
tier: median
overall_score: Weak Reject
timestamp: 2026-05-15T02:24:06.958600+00:00
---

# Review Report — Reviewer R2 (Novelty and Related Work)

**Paper**: Adaptive Contamination-Aware Reweighting for Pretraining on Mixed Real-Synthetic Corpora

**Tier**: Median

---

## 1. Novelty Assessment

The core technical contribution — adaptive b* via ESS-constrained maximization of alpha_eff(b) — is **limited in novelty**. I identify three layers of concern:

**a) The weighting formula is not new.** The authors forthrightly acknowledge that w_i = (1-q_i)^b comes from Drayson et al. (EMNLP 2025). The paper's novelty rests entirely on the *selection mechanism* for b.

**b) ESS constraints are a textbook technique.** Effective sample size thresholding is standard practice in importance sampling (see Vehtari et al., JMLR 2024 on PSIS, which the authors cite in their literature map but omit from the paper). The idea of "pick the most aggressive weighting that doesn't collapse your effective sample size below a threshold" is not new — it is essentially the operating principle behind Pareto-smoothed importance sampling diagnostics. Applying this to a specific b parameter in a specific weighting formula constitutes an application, not a methodological advance.

**c) The "principled derivation" framing is overstated.** The paper claims a "theoretical framework" but alpha_eff(b) is defined as a weighted average of (1-q_i), which is simply the normalized first moment of the weight distribution. The connection to the convergence bound d(P_t, P_0) <= t^{-min{p,alpha}} from arXiv 2602.16065 is stated as motivation but never formalized — the paper explicitly says "motivation not contribution." This means the "principled" in "principled b* derivation" reduces to "pick b to maximize a weighted mean subject to an ESS floor," which is a reasonable heuristic but not a theoretical contribution.

**d) Advancement beyond Drayson et al. is marginal.** The paper replaces Drayson's per-model validation-based b selection with per-batch ESS-constrained selection. But the empirical evidence shows this replacement captures only ~86% of grid-best improvement, fails under cross-generator and domain-skewed settings, and the b* distribution is insensitive to model scale (identical at 0.6B and 3B). The "zero tuning cost" advantage is real but modest — Drayson's grid search is not computationally prohibitive for the model scales studied.

**Verdict**: The novelty is below the threshold for a top venue. The contribution is an application of standard importance sampling diagnostics to a specific hyperparameter selection problem, not a new method.

---

## 2. Related Work Completeness

The related work section is **adequate but has notable gaps**:

**Missing references:**
- **Vehtari et al. (JMLR 2024), "Pareto Smoothed Importance Sampling"**: The paper uses ESS as its core constraint but does not cite the most relevant work on ESS diagnostics for importance weighting. This omission is significant because PSIS provides exactly the kind of principled importance weight management that the paper claims to introduce.
- **Kimura & Hino (TMLR 2024), importance weighting survey**: Provides the theoretical backbone for the approach but is uncited.
- **Alemohammad et al. (ICLR 2024), "Self-Consuming Generative Models Go MAD"**: Relevant background on model autophagy that strengthens the motivation.
- **Feng et al. (2024), "Beyond Model Collapse"**: Uses verifiers for synthetic data filtering — the hard-filtering counterpart to this paper's soft reweighting.
- **Nait Saada et al. (2025), "The Data-Quality Illusion"**: Directly relevant cautionary work on classifier-based quality scores, which applies to the q-scores used here.

**Positioning concerns:**
- The paper positions itself as "complementary" to Drayson et al. by distinguishing recursive training vs. one-pass pretraining. But the weighting formula works identically in both settings — the distinction is about experimental setup, not methodology. A reviewer familiar with both papers would see this as the same method with a different b-selection subroutine.
- The comparison to Golden Ratio Weighting (He et al. 2025) is fair but could note that Golden Ratio provides actual theoretical optimality guarantees, whereas adaptive b* provides a heuristic with no optimality proof.
- The SIR vs. loss reweighting distinction is listed as a differentiator but the paper admits "a full gradient variance analysis under both implementations remains future work." Without this analysis, the distinction is implementation-level, not conceptual.

---

## 3. Contribution Calibration

The paper's three claimed contributions need recalibration:

**Contribution 1 ("Theoretical framework")**: Overclaimed. There is no theorem, no proof, no formal guarantee. alpha_eff(b) is a diagnostic statistic, and the ESS constraint is borrowed from importance sampling. Calling this a "theoretical framework" risks reviewer backlash at a top venue. More honest framing: "a practical heuristic for automated b selection motivated by importance sampling principles."

**Contribution 2 ("Practical result")**: The strongest contribution, but the headline number (85.8% of grid-best) is not compelling. At a top venue, reviewers expect methods to match or exceed baselines, not recover 86% of them. The "zero tuning cost" angle is legitimate but the savings are modest — 9 training runs is not prohibitive at the 200M-token scale, and the paper does not demonstrate settings where grid search is genuinely infeasible.

**Contribution 3 ("Problem setting")**: This is not a contribution — it is a statement of the experimental conditions. "We address the unknown contamination proportion setting" is a problem setup, not a methodological contribution. Drayson et al. also do not assume known proportions; they use a validation set to select b, which is a different (and arguably more principled) approach to handling unknown proportions.

**The "diagnostic framework" reframing** (visible in the worst-case paper variant) feels like a retreat. The original claim was that adaptive b* provides a principled alternative to grid search. When the method systematically overshoots by 4x and recovers only 70% of grid-best, relabeling it as a "diagnostic tool" does not rescue the contribution — it replaces a falsified strong claim with an unfalsifiable weak claim.

---

## 4. Significance

**Problem importance**: High. Contaminated pretraining corpora are a genuine and growing concern. The problem is timely and practically relevant.

**Solution sufficiency**: Low. The proposed method:
- Recovers only 86% of grid-best improvement in the best case
- Fails (performs worse than uniform) under cross-generator contamination
- Fails under domain-skewed contamination
- Produces b* distributions insensitive to model scale, suggesting it does not actually adapt to the problem structure
- Shows no statistically significant downstream task improvement
- Has a critical hyperparameter (n_min) with an extremely narrow working range (only n_min=2 works at batch_size=4)

The paper's strongest empirical finding — that TF-IDF+LR is within 0.005 PPL of ModernBERT — is genuinely useful but is an observation, not a method. It could be a paragraph in a systems paper, not the centerpiece of a methods paper.

**Practitioner impact**: Low. A practitioner reading this paper would conclude: (a) use any detector with AUC > 0.9; (b) set b=0.3 and don't bother with adaptive selection; (c) the effect is 0.04 PPL at 200M tokens, which may or may not matter at scale.

---

## 5. Presentation

**Strengths**: The paper (median variant) is clearly written. The experimental setup is well-described. Tables are clean and informative. The limitations section is unusually honest.

**Weaknesses**:
- The abstract claims "matches grid-search-optimal performance within seed variance" but the aggregate ratio is 85.8%, which is not "within seed variance" by any standard statistical definition. The per-seed ratios (95.2%, 87.0%, 78.4%) show the gap is systematic, not noise.
- Algorithm 1 is underspecified. The paper says "Search b in [0, b_max] for b* maximizing alpha_eff(b)" but the actual implementation (visible in the code) uses a 1000-point grid search + bisection refinement. This is a grid search to replace a grid search — the overhead is per-batch rather than per-experiment, but the framing obscures this.
- The paper does not report computational overhead of the per-batch b* computation. How much wall-clock time does the 1000-point grid + bisection add per training step?
- The "effect amplification" sections (higher contamination, larger model) report projected numbers that appear to be from the "dream" simulation rather than actual experiments. The distinction between real and projected results is unclear.

---

## 6. Top Weaknesses

**W1: The method underperforms its own baseline.** Adaptive b* recovers 85.8% of grid-best at rho=0.4, drops to 75% cross-generator, and to ~50% domain-skewed. A method paper whose main method is consistently inferior to a simple grid search over 9 values faces a fundamental viability question. The "zero tuning cost" argument does not overcome this when the grid search is cheap.

**W2: Failure modes are not edge cases.** Cross-generator contamination (the norm in web data) and domain-skewed contamination (the norm in real corpora) are the standard conditions, not adversarial stress tests. The method works only in the easiest setting (single known generator, uniform injection) — the one setting where you'd have the most information to just set b manually.

**W3: n_min sensitivity reveals fragility.** At batch_size=4, only n_min=2 works. n_min=1 leads to extremes, n_min=3 collapses to uniform. This is not a "robust default" — it is a knife-edge that happens to work at one batch size. The paper does not test whether n_min=2 remains optimal at batch_size=16 or 64. The internal project notes reveal that 75%+ of batches have ESS hitting the floor at 2.0, meaning the method operates at its constraint boundary almost always. This is a sign of a poorly conditioned optimization, not a well-designed algorithm.

**W4: No genuine theoretical contribution.** The alpha_eff(b) "framework" is a weighted mean. The ESS constraint is textbook. The convergence bound is motivation, not contribution. The paper has no theorem, no proof, and no formal guarantee about b*'s behavior. The concentration bound in the code (compute_concentration_bound) is not mentioned in the paper at all.

**W5: Effect size is negligible and does not transfer downstream.** 0.04 PPL improvement at 200M tokens, with no statistically significant downstream task improvement. The "effect amplification" argument (2x at higher contamination, 2x at larger scale) is speculative extrapolation from limited data points, and even the projected best case (1.24% relative PPL at 3B, rho=0.4) is modest.

---

## 7. Strengths

**S1: Honest reporting.** The paper does not hide its negative results. The cross-generator degradation, domain-skewed failure, and downstream non-significance are all reported transparently. This is commendable and relatively rare.

**S2: Controlled experimental design.** The use of 3 seeds, multiple contamination ratios, cross-generator testing, and domain-skewed injection represents a thorough experimental protocol. The extended grid search to b < 0.5 to verify the grid-best location shows diligence.

**S3: Detector sufficiency finding.** The empirical observation that TF-IDF+LR (AUC=0.939) is within 0.005 PPL of ModernBERT (AUC=0.986) is practically useful. If validated at scale, this would save significant compute in production pipelines.

**S4: Clean comparison with Drayson et al.** The paper clearly delineates what is shared (the weighting formula) and what is new (the b-selection mechanism). The comparison table in the paper framing is well-structured.

**S5: Graceful degradation.** The property that n_min >= |B| recovers uniform training (never worse than baseline) is a nice safety property, even if the effective operating range is narrow.

---

## 8. Questions for Authors

**Q1**: The paper claims adaptive b* "eliminates grid search" but Algorithm 1 performs a 1000-point grid search over b *per batch*. Over 6100 training steps, this is 6.1M evaluations of alpha_eff and ESS, versus 9 evaluations in Drayson's approach (9 values of b, each evaluated once on a validation set). Can you clarify the computational overhead and justify the claim that this is "zero cost"?

**Q2**: The b* distribution is nearly identical across 0.6B and 3B models (median 0.88 vs. 0.85). If b* does not adapt to model capacity, what exactly is it adapting to? Drayson et al. find that optimal b varies dramatically with model size (b=10 for small models, b=1 for 1.7B). Your method's insensitivity to model scale could be either a feature (model-agnostic) or a bug (failure to capture model-dependent dynamics). Which interpretation do you support, and what evidence distinguishes them?

**Q3**: At batch_size=4, 75%+ of batches have ESS=2.0 (hitting the n_min floor). This means the adaptive algorithm is effectively just picking the largest b such that ESS=2 for most batches — a simple threshold rule, not a nuanced adaptation. Would you agree that at practical batch sizes (32, 64, 128), the method might behave very differently? If so, have you tested this?

**Q4**: The cross-generator experiment shows adaptive b* achieves only 75% ratio and the domain-skewed experiment shows ~50%. In production web pretraining, contamination is always multi-generator and non-uniformly distributed. What is the practical deployment scenario where the in-distribution, uniform-injection assumption holds?

**Q5**: The concentration bound function in your code (compute_concentration_bound) provides a formal error bound on alpha_eff estimation. Why is this not included in the paper? It seems like the closest thing to a genuine theoretical contribution.

---

## 9. Score

**3 — Weak Reject**

The paper addresses a relevant problem and is honestly written, but the core methodological contribution (adaptive b* via ESS-constrained alpha_eff maximization) is an application of standard importance sampling diagnostics rather than a novel technique. The method consistently underperforms grid search, fails in realistic contamination scenarios (cross-generator, domain-skewed), and has a narrow hyperparameter working range. The strongest finding (detector sufficiency) is an empirical observation that does not require the proposed framework. The "theoretical framework" claim is not supported by any formal result. For a top venue at 25% acceptance, the novelty and result strength are insufficient.

---

## 10. Confidence

**4 — High confidence.** I am familiar with importance sampling, ESS diagnostics, data reweighting for LLM pretraining, and the Drayson et al. baseline. I have read the paper, the codebase (alpha_eff.py), the internal decision log, and the project memory. My concerns about novelty and method effectiveness are grounded in both the reported results and the internal development history (e.g., n_min=3 failure requiring D012 fix, MVP passing at 88.6% under a relaxed threshold via D019).