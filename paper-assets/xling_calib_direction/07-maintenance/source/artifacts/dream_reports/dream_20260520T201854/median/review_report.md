---
dream_id: dream_20260520T201854
tier: median
overall_score: 3 - Weak Reject
timestamp: 2026-05-20T21:16:43.573906+00:00
---

# Reviewer 2 (R2): Novelty, Significance, Related Work, Writing

## Paper: "Cross-Lingual Correctness Probes Reveal a Depth--Transferability Pareto Frontier: Distributional Matching Fails Where Linear Projection Succeeds"

**Tier: MEDIAN (CaCLR fails — principled negative result + linear projection as constructive alternative)**

---

## 1. Novelty Assessment

### Contribution 1: Pareto Frontier
**Verdict: Low-to-moderate novelty.**

Same assessment as the best-tier version. The depth-transferability tradeoff is documented in prior work (Civelli et al. 2026, LACE 2025). The median version's numbers are weaker: rho ranges from -0.51 to -0.58, with substantial per-language variance (sigma_rho 0.12-0.16). On Llama 4 Scout, Table 2 shows the per-language rho range spans [-0.82, -0.21] — meaning some languages show strong negative correlation while others show almost none. This weakens the "Pareto frontier" framing considerably: it is not a universal phenomenon but a language-and-architecture-dependent tendency.

The framing as a "Pareto frontier" is arguably misleading when the median rho is only -0.52. A Pareto frontier implies a clean tradeoff; what the data shows is a noisy negative tendency that is sometimes absent. The paper would be more honest to call it a "depth-transfer tradeoff tendency."

### Contribution 2: CKA Mechanistic Explanation
**Verdict: Moderate novelty, but r=0.58 is not compelling.**

CKA explaining 34% of transfer variance is meaningful but leaves 66% unexplained. The comparison with MMD (6% variance explained) is the strongest point — it demonstrates that misalignment is geometric rather than distributional. However, CKA is a coarse measure (it compares entire representation matrices, not correctness-specific subspaces), and r=0.58 is a moderate correlation that many reviewers would not consider "mechanistic explanation."

The qualitative insight (geometric rotation vs distributional shift) is valuable and well-argued. But the paper oversells this as a "mechanistic explanation" when it is more accurately a "suggestive correlational analysis."

### Contribution 3: CaCLR Negative Result
**Verdict: The paper's central contribution, but faces the "is it surprising?" test.**

CaCLR's consistency loss being inert (d=0.08, p=0.42) is a clean negative result. The paper frames this as principled because it is predicted by the CKA geometric analysis. This is the strongest contribution of the median version.

However: Is this surprising? MMD-based domain adaptation is known to fail when the source and target domains have different geometric structure (not just distributional shift). The domain adaptation community has known since Ganin et al. (2016) and subsequent work that marginal distribution matching is insufficient when conditional distributions differ. Framing this as a novel finding requires the reader to not be familiar with the domain adaptation literature.

The constructive alternative (linear projection with 50-100 pairs) is useful but is essentially VecMap/MUSE applied to sentence-level correctness representations. The sample efficiency finding (~70 pairs to saturation) is consistent with existing cross-lingual alignment literature.

### Contribution 4: Cross-Lingual Orthogonality
**Verdict: Same as best tier — confirmatory extension.**

Max cosine rises to 0.10 in this version (vs 0.062 in best), with sw reaching 0.098. The resource-tier gradient is more pronounced. The finding remains confirmatory.

---

## 2. Significance

**Reduced compared to best tier.** Without CaCLR as a working method, the paper's contributions are:
- A systematic evaluation showing cross-lingual probe transfer works for high-resource but not low-resource languages (somewhat expected)
- A principled negative result about distributional matching (valuable but narrow)
- A recommendation to use linear projection (useful but not novel — this is what VecMap/MUSE already do)

The paper's significance rests on whether the community considers "MMD-based distributional matching doesn't work for correctness probe transfer, here's why, and use linear projection instead" to be a sufficient contribution. For a top venue, I would argue this is below the bar — the negative result, while clean, is not deeply surprising, and the constructive alternative is borrowed from existing methods.

---

## 3. Related Work Positioning

Mostly the same issues as the best tier, with one important addition:

- **The negative result needs stronger positioning against domain adaptation theory.** The paper invokes Ben-David et al. (2010) H-divergence framework, but the failure of marginal distribution matching when conditional distributions differ is better explained by more recent theoretical work (Zhao et al. 2019 "On learning invariant representations for domain adaptation"). The paper should engage with this literature to strengthen the theoretical grounding of the negative result.

- The bibliography is more complete in this version (21 entries vs 12), which is a significant improvement. Hewitt & Liang, Voita & Titov, and several additional references are properly cited.

- The DALI paper (Ravisankar et al. 2026) is still missing.

---

## 4. Writing Quality

**The median version is better written than the best version.** Specific improvements:
- More honest framing: "principled negative result" rather than overselling CaCLR
- Better organized: the CKA analysis precedes the CaCLR results, making the prediction-then-test structure clearer
- The discussion section properly explains "Why Does Distributional Matching Fail?" — this is the paper's strongest prose
- Statistical reporting is more consistent (bootstrap CIs, permutation tests, Cohen's d throughout)

**Issues:**
- The title is long and awkward: "Cross-Lingual Correctness Probes Reveal a Depth--Transferability Pareto Frontier: Distributional Matching Fails Where Linear Projection Succeeds" — this reads as two papers forced into one title
- The abstract is still too dense but better organized than the best version
- Some results are only in appendices that should be in the main text (cross-benchmark generalization, control task selectivity)

---

## 5. Strengths

1. **Clean negative result with mechanistic explanation.** The CaCLR beta inertness is demonstrated rigorously (3 OOM sweep, d=0.08, p=0.42) and the CKA-based geometric explanation is coherent. This is how negative results should be reported.

2. **Honest framing.** The paper does not oversell. The limitations section acknowledges weak selectivity for low-resource languages. The discussion explains rather than speculates.

3. **Strong statistical methodology.** Same as best tier — above field median.

4. **Constructive alternative.** Rather than stopping at "CaCLR doesn't work," the paper identifies linear projection as the practical solution and characterizes its sample efficiency.

---

## 6. Weaknesses

1. **(Major) Insufficient novelty for a top venue.** The negative result (distributional matching fails for cross-lingual correctness probe transfer) is clean but unsurprising given the domain adaptation literature. The positive finding (linear projection works) is borrowed from existing methods. The Pareto frontier extends known findings. For ~25% acceptance rate, I expect the paper to teach the community something it could not have predicted.

2. **(Moderate) The "Pareto frontier" framing overstates the finding.** Median rho of -0.52 with sigma_rho 0.12-0.16 and per-language range [-0.82, -0.21] does not constitute a "frontier" — it is a noisy tendency. On Llama 4 Scout, the rho median is only -0.54, meaning roughly half the per-language correlations are weaker than -0.54 and some are near zero or positive. The paper should reframe this as a "depth-transfer tradeoff" rather than a "Pareto frontier."

3. **(Moderate) CKA analysis is correlational, not mechanistic.** r=0.58, explaining 34% of variance, is presented as a "mechanistic explanation" throughout the paper. This is a correlation. A mechanistic explanation would identify the specific geometric transformation (rotation, scaling) at each layer and show that correcting it restores transfer performance. The paper gestures at this (subspace angle analysis showing 15-35 degree rotation) but does not follow through with a controlled experiment.

4. **(Minor) Limited practical impact of the negative result.** Who was planning to use MMD-based consistency loss for cross-lingual probe transfer? The paper addresses a method (CaCLR) that the authors themselves proposed. Showing that your own proposed method doesn't work is less impactful than showing that a widely-used method doesn't work.

5. **(Minor) Gemma 4 results are thin.** The dense architecture is relegated to a summary table and brief paragraph. For the MoE-vs-dense contrast to be compelling, the dense model needs the same full treatment (per-language results, CKA analysis, all transfer conditions).

---

## 7. Questions for Authors

**Q1:** The domain adaptation community has known since at least Zhao et al. (2019) that marginal distribution matching fails when conditional distributions differ across domains. How is CaCLR's failure a novel finding rather than a specific instance of a known general principle? What does this paper add to the theoretical understanding beyond confirming the prediction?

**Q2:** The CKA-transfer correlation is r=0.58, explaining 34% of variance. The paper calls this a "mechanistic explanation." Would you accept r=0.58 as a "mechanistic explanation" if it appeared in a paper you were reviewing? What fraction of transfer variance would need to be explained to justify the "mechanistic" label?

**Q3:** Linear projection with 50-100 pairs is your recommended solution. How does this differ from applying VecMap/MUSE at the sentence level? Is there any technical novelty in the projection method itself, or is the contribution purely that "existing alignment methods work for this new task"?

---

## 8. Score

**3 / 6 — Weak Reject**

The paper is methodologically rigorous and honestly framed. The negative result is clean. However, for a top venue at ~25% acceptance, I need novelty that teaches the community something non-obvious. The negative result (distributional matching fails) is predictable from domain adaptation theory. The positive result (linear projection works) is borrowed from existing methods. The Pareto frontier finding extends known cross-lingual probing results without a surprising twist. The comprehensive evaluation is valuable but insufficient to compensate for limited novelty.

The paper would be better suited for a workshop, findings track, or a venue that specifically values systematic empirical evaluation and negative results (e.g., NeurIPS Datasets and Benchmarks track, or a ReScience-style venue).

## 9. Confidence

**4 / 5 — High confidence.** Same basis as best-tier review. The novelty assessment is where I am most confident — I can trace each contribution to its antecedents in the literature.
