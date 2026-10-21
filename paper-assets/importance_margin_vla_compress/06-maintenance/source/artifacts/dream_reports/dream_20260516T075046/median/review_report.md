---
dream_id: dream_20260516T075046
tier: median
overall_score: 5 - Marginally Below Acceptance Threshold
timestamp: 2026-05-16T08:41:50.613888+00:00
---

# Dream Review Report — Importance Margin Maximization (IMM)

**Paper:** Importance Margin Maximization: A Robustness-Aware Framework for Vision-Language-Action Token Compression
**Venue:** CoRL 2026
**Review Mode:** Full (2 Reviewers + Roundtable)
**Dream ID:** 20260516T075046

---

## Reviewer Assignments
- **R1:** Methods and Experiments
- **R2:** Novelty and Related Work

---

## R1 Review: Methods and Experiments

### Summary
IMM proposes a margin-maximization training framework for robust VLA token compression with a certified stability bound and two-stage training protocol. The two-stage design is well-motivated by a clear ablation trajectory showing co-adaptation is destructive. The experimental breadth is impressive (12 experiments across models, benchmarks, compression methods, and defenses), but statistical rigor is insufficient for the claims made.

### Strengths
1. **Well-motivated two-stage design with mechanistic ablation (Table 7).** G3 progression from joint (3.29) → gradient-isolated (1.34) → two-stage (0.87) provides a clear causal story with each step isolating one variable.
2. **ACIS is lightweight and practical (Table 12).** 2.3M params (0.46% overhead), +0.6ms latency offset by 37% net latency reduction. The cost-benefit ratio makes deployment plausible.
3. **Compression-agnostic cross-method validation (Table 5).** +52–56pp preservation uplift on three independent compression methods (FastV, VLA-IAP, VLA-Cache) with consistent G3 near 1.0. This elevates IMM from ACIS-specific trick to general training framework.
4. **Formal connection between margin and stability (Proposition 1).** While elementary, it provides an actionable deployment criterion.
5. **Multi-angle denoising evidence.** Token analysis (Table 11) + U-shaped G3 curve (Table 8) provide complementary support.

### Weaknesses

**Major:**

1. **Non-significant headline results undermine core claims.** Table 2: ACIS prune 84% vs baseline 82%, p=0.38. Table 3: −0.7pp average, p=0.31. The central "near-lossless" claim rests on results indistinguishable from noise at the reported sample sizes. The paper cannot claim "near-lossless" with p>0.3.

2. **Single-seed evaluation throughout.** No multi-seed results are reported for any experiment. CoRL expects variance estimates, especially when effect sizes are small. 60-episode evaluations lack power to detect the claimed 2pp differences (would need ~2000 episodes).

3. **Formal bound is ~6.2x loose (Table 10).** The bound is conservative — never violated, but the average tightness ratio of 6.2x means the certified region is 6x smaller than what empirical stability actually supports. At ε=0.1 the bound saturates to 1.0 (trivial). This severely limits practical utility as a runtime certificate.

4. **Bypass degradation undermines "lossless" framing.** Table 7 shows bypass loss (0.0187) is far above ACIS+prune loss (0.0035) for two-stage, meaning the backbone has become functionally dependent on ACIS routing despite the two-stage design's intent to prevent this. G3=0.87 means the *compressed* model is better than baseline, but removing ACIS is not graceful.

5. **Lambda confound in training ablation (Table 7).** Joint and grad-isolated use λ=0.5 while two-stage Stage 1 uses λ=1.0. This conflates training strategy differences with hyperparameter tuning, weakening the ablation's interpretability.

**Minor:**

6. **LIBERO-Plus perturbation magnitudes unspecified.** The paper tests 7 perturbation dimensions (Table 1) without specifying their strengths, making results non-reproducible.

7. **Token importance analysis lacks causal direction (Table 11).** Pruned tokens having lower attention (ratio 0.44) could mean ACIS learned from attention patterns rather than independently discovering importance. Moderate effect sizes (Cohen's d = 0.42–0.51) indicate substantial distribution overlap.

8. **OpenVLA G3=1.09 (Table 4) shows compression is not near-lossless on larger models.** The paper acknowledges this but the Discussion section treatment is brief.

### Questions for Authors
1. Can you provide multi-seed results (≥3 seeds) for Tables 1-3 with standard deviations?
2. What is the actual success rate with ACIS removed post-deployment (bypass scenario)?
3. Were λ values matched across training ablation conditions? If not, can you rerun with matched values?
4. How many episodes would be needed to achieve statistical significance for the observed 2pp differences?
5. What is the Lipschitz constant estimation procedure (spectral norm? power iteration? how many iterations)?
6. Can you report wall-clock training time for the complete two-stage pipeline?

### Scores
- Originality: 6/10
- Quality: 5/10
- Clarity: 6/10
- Significance: 6/10
- Relevance: 8/10
- Overall: 5/10
- Confidence: 4/5

### Summary Assessment
Marginally below acceptance. The two-stage training and compression-agnostic design are genuine contributions, but non-significant headline results (p>0.3), single-seed evaluation, and the ~6x loose bound substantially weaken the paper's evidence base relative to its claims.

---

## R2 Review: Novelty and Related Work

### Summary
IMM connects margin-based robustness to token selection stability — a clean formulation. The compression-agnostic plugin framing is the strongest novelty claim. However, the theoretical contribution is shallow (Proposition 1 is a direct Lipschitz + union bound application), the related work is severely incomplete (missing entire literatures in ViT token pruning and margin-based robustness), and differentiation from the closest work (CAGE) is unclear.

### Strengths
1. **Clean problem formulation.** "Importance margin collapse" as root cause of compression brittleness is intuitive and operationalizable.
2. **Compression-agnostic positioning.** Demonstrating +53pp preservation on three external methods is the paper's strongest novelty — IMM is a *training strategy*, not another compression method.
3. **Two-stage training insight.** G3 3.29→0.87 progression is a compelling engineering contribution with clear mechanistic explanation.
4. **Good experimental breadth for 6 pages.** Cross-model, cross-benchmark, cross-compression, multi-perturbation coverage.
5. **Denoising effect is surprising and interesting.** G3 < 1.0 is counterintuitive and supported by multiple analyses.

### Weaknesses

**Major:**

1. **Proposition 1 is theoretically trivial.** P(top-k flip) ≤ k·ε·L/Δ_k is a direct union bound over k positions + Lipschitz continuity of pairwise score differences. This is not a "certified robustness guarantee" in the sense of Cohen et al. or IBP-style methods. The probabilistic framing is also questionable — for a deterministic Lipschitz scorer, the top-k set either changes or doesn't. The bound should be stated as a sufficient condition (Δ_k > k·ε·L ⟹ no flip), not a probability.

2. **Massive gap in ViT token pruning literature.** Zero citations from: ToMe (Bolya et al., ICLR 2023), DynamicViT (Rao et al., NeurIPS 2021), EViT (Liang et al., ICLR 2022), ATS (Fayyaz et al., NeurIPS 2022), A-ViT (Yin et al., 2022). DynamicViT in particular learns token importance scores via a prediction module — architecturally very similar to ACIS. Not engaging with this literature is a serious omission.

3. **Margin-based robustness has deep unacknowledged history.** SVMs, large-margin classifiers (Elsayed et al., NeurIPS 2018), MMA Training (Ding et al., NeurIPS 2020) directly maximize margins for robustness. The paper does not discuss how IMM's margin concept relates to these conceptual ancestors. The "first to maximize margins for robustness" framing is untenable without this context.

4. **Unclear differentiation from CAGE [7].** The paper states CAGE "formalizes the attack surface but offers no defense." But CAGE also provides certified guarantees (hence "Certified" in its name). The paper must explain precisely how IMM's guarantee differs — tighter? Different threat model? Different assumptions?

5. **"First robustness-aware framework" claim is overstated.** RobustVLA, adversarial training, and CAGE all address robustness of VLAs or VLA compression. The novelty wedge ("first *certified* + *token compression*") is very narrow and contested by CAGE.

**Minor:**

6. **Only ~10 references.** Even for a 6-page paper, CoRL submissions typically have 25–40 references. This signals either incomplete literature review or rushed preparation.

7. **No comparison with token merging.** ToMe-style methods that merge rather than prune tokens may be inherently more robust (merged tokens retain information). This alternative is never discussed.

8. **Lipschitz constant estimation method undescribed.** L=1.07 is reported without explaining the computation method or tightness of the estimate.

### Missing Related Work
1. **ViT token pruning/merging:** ToMe, DynamicViT, EViT, ATS, A-ViT, SPViT, AdaViT
2. **Large-margin deep learning:** Elsayed et al. (2018), Ding et al. (2020, MMA), Sun et al. (2015, LMCL)
3. **Certified robustness beyond RS:** IBP (Gowal et al., 2018), CROWN (Zhang et al., 2018), Lipschitz certificates (Tsuzuku et al., 2018)
4. **Robust attention:** Zhai et al. (2020), adversarially robust ViTs (Bai et al., 2021; Mo et al., 2022)
5. **LLM token importance:** H2O (Zhang et al., 2023), StreamingLLM (Xiao et al., 2023), ScissorHands (Liu et al., 2023)
6. **Compression + robustness interaction:** Ye et al. (2019), Gui et al. (2019)

### Questions for Authors
1. How does Proposition 1 differ from the sufficient condition Δ_k > k·ε·L ⟹ no flip? Why the probabilistic framing?
2. How does IMM's bound compare to CAGE's certified guarantee — tighter, weaker, or different scope?
3. How does ACIS differ from DynamicViT's prediction module beyond the margin training objective?
4. Have you compared against ToMe-style token merging for inherent robustness?
5. Could the "denoising effect" (G3 < 1.0) be achieved by any competent importance scorer (e.g., attention-threshold pruning) without margin training?
6. What is the computational cost of estimating L at deployment?

### Scores
- Originality: 5/10
- Quality: 6/10
- Clarity: 7/10
- Significance: 5/10
- Relevance: 8/10
- Overall: 5/10
- Confidence: 4/5

### Summary Assessment
Marginally below acceptance. The core idea is sensible and the compression-agnostic plugin framing is novel, but the theoretical contribution is trivially derived, the related work has critical gaps (ViT pruning, margin-based robustness), and differentiation from CAGE is insufficient. A revision with honest theoretical positioning and comprehensive literature engagement could reach acceptance.

---

## Roundtable Discussion

### Step 2: Cross-Sharing

**R1 → R2:** "My main concern is statistical rigor — the headline results (Tables 2-3) are not significant (p>0.3), and there are no multi-seed evaluations. The bound's 6.2x looseness also undermines the 'certified' framing. The training ablation has a lambda confound."

**R2 → R1:** "My main concern is novelty positioning — Proposition 1 is a textbook Lipschitz bound, the ViT pruning literature is entirely missing, and CAGE already provides certified guarantees for VLA compression. The reference list is far too short for a venue submission."

### Step 3: Convergence

**Points of agreement:**
1. **Two-stage training is the strongest contribution.** Both reviewers identify the co-adaptation ablation (Table 7) as mechanistically clear and practically useful. This is the paper's most defensible novelty.
2. **Compression-agnostic plugin (Table 5) is compelling.** +53pp across three external methods elevates IMM beyond a single compression approach.
3. **Formal bound is oversold.** R1 notes ~6.2x looseness; R2 notes trivial derivation. Both agree the bound should be positioned as a "principled design criterion" (which the paper partly does) rather than a "certified guarantee" (which the abstract and introduction still claim).
4. **Claims need tempering.** "Near-lossless" requires statistical significance (R1). "First robustness-aware" requires engaging with CAGE and RobustVLA (R2). "Certified" requires tighter bounds or honest acknowledgment (both).
5. **Experimental coverage is good; statistical rigor is not.** 12 experiments across models/benchmarks/methods is impressive scope. But single-seed, non-significant p-values, and unspecified perturbation magnitudes weaken all results.

**Points of disagreement:**
- R1 is slightly harsher on experimental methodology (non-significance, bypass degradation); R2 is harsher on positioning (missing literature, trivial theory). Both arrive at the same overall score (5/10).
- R1 sees the bypass degradation as a fundamental problem; R2 does not raise it but would likely acknowledge it as a valid concern after cross-sharing.

**Consensus overall: 5/10 — Marginally Below Acceptance Threshold**

### Step 4: Consolidated Assessment

## Final Scores

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Originality | 6 | 5 | 5 |
| Quality | 5 | 6 | 5 |
| Clarity | 6 | 7 | 7 |
| Significance | 6 | 5 | 5 |
| Relevance | 8 | 8 | 8 |
| **Overall** | **5** | **5** | **5** |
| Confidence | 4 | 4 | 4 |

**Overall Recommendation: 5/10 — Marginally Below Acceptance Threshold**

## Key Strengths (Consensus)
1. **Two-stage training protocol with mechanistic ablation** — the G3 3.29→1.34→0.87 progression is the paper's most convincing contribution
2. **Compression-agnostic plugin** — +53pp preservation on FastV/VLA-IAP/VLA-Cache demonstrates IMM is a general training strategy, not just another compression method
3. **Strong experimental breadth** — 12 experiments across 2 models, 4 benchmarks, 4 compression methods, 4 defense baselines, and 7 perturbation types in 6 pages
4. **Practical impact** — negligible ACIS overhead (+0.46% params) with 1.62x inference speedup; clear deployment path
5. **Timely problem** — VLA compression robustness is a real and growing concern for robot deployment

## Key Weaknesses (Consensus)

### Critical
1. **Non-significant headline results.** Success rate differences (Tables 2-3) have p>0.3. No multi-seed results reported. The "near-lossless" claim requires statistical evidence that currently does not exist.
2. **Theoretical contribution is oversold.** Proposition 1 is a textbook Lipschitz + union bound, not a novel "certified robustness guarantee." The 6.2x tightness ratio makes it impractical as a runtime certificate. Should be honestly positioned as a design criterion.
3. **Severely incomplete related work.** Missing entire literatures: ViT token pruning (ToMe, DynamicViT, EViT — architecturally related to ACIS), margin-based robustness (SVMs, large-margin classifiers), certified robustness beyond RS. Only ~10 references is far below venue standards.
4. **Unclear differentiation from CAGE [7].** CAGE also provides certified guarantees for VLA compression. The novelty gap must be explicitly addressed.

### Major
5. **"First robustness-aware framework" claim is contested** by RobustVLA, adversarial training, and CAGE. The narrow novelty wedge must be clearly defined and defended.
6. **OpenVLA G3=1.09** shows compression is not near-lossless on larger models. The paper's scope of applicability is narrower than claimed.
7. **Lambda confound in training ablation** (Table 7) weakens the two-stage justification.

### Minor
8. LIBERO-Plus perturbation magnitudes unspecified
9. Token analysis (Table 11) correlation ≠ causation, moderate effect sizes
10. No comparison with token merging (ToMe-style) approaches

## Actionable Recommendations for Revision
1. **Add multi-seed results** (≥3 seeds) for all headline experiments with reported standard deviations
2. **Reposition Proposition 1** as "principled design criterion" throughout — remove "certified" language from abstract/intro unless bound is tightened
3. **Expand related work** to cite ViT pruning, margin-based robustness, and LLM token importance literatures (add 15-25 references)
4. **Add explicit CAGE comparison** — table showing threat model, assumptions, bound tightness, training cost differences
5. **Match hyperparameters** in training ablation or report sensitivity to λ
6. **Discuss limitations more prominently** — OpenVLA G3>1.0, statistical non-significance, bound looseness
7. **Report perturbation specifications** for LIBERO-Plus reproducibility

## Experiment Coverage Assessment
All 12 planned experiments from the experiment design are present in the paper. Coverage is complete. The paper's experimental breadth is a notable strength — the weakness lies in depth (single-seed, non-significant effects) rather than coverage.

## Venue Fit
The paper is well-suited for CoRL in topic (VLA compression for robot deployment). The relevance score (8/10) reflects this. However, CoRL increasingly expects real-robot validation or at minimum high-fidelity simulation with clear sim-to-real transfer arguments, neither of which is present. All evaluations are in simulation (aloha_sim_insertion, LIBERO).

## Meta-Assessment
This is a paper with a **good idea, adequate breadth, but insufficient depth** for acceptance at a ~30% acceptance rate venue. The core insight (margin maximization for robust compression) and the engineering contribution (two-stage training) are sound and practically useful. However, the theoretical overselling, incomplete literature engagement, and statistical gaps in the experimental evidence collectively place it below the acceptance threshold. A focused revision addressing the 7 recommendations above — particularly multi-seed results, honest theoretical positioning, and literature coverage — has a realistic path to acceptance at CoRL or a similar venue.
