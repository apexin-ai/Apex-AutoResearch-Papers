---
dream_id: dream_20260525T050917
tier: best
overall_score: 5.5/10 — Borderline (Weak Reject)
timestamp: 2026-05-25T06:28:19.874825+00:00
---

# Area Chair Consolidated Review Report

**Paper**: "Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"
**Venue**: CoRL 2026
**Roundtable Steps**: 2 (Cross-Share) + 3 (Convergence) + 4 (Final Report)

---

## 1. Paper Summary

This paper presents the first systematic cross-architecture study of vision token pruning in VLA models, evaluating 6 architectures (450M–7B) across 4 connector families (linear, MLP, BART encoder, pixel-shuffle) on 4 LIBERO task suites with 3 pruning strategies (L2-norm, random, attention-based) at multiple keep ratios. The central finding is a 2-axis framework: pruning robustness is jointly determined by (1) connector-imposed token coupling (independent vs. entangling) and (2) task complexity, which amplifies damage on entangling connectors. A coefficient of variation (CV) diagnostic predicts both pruning tolerance and optimal strategy, and a Vision Token Re-encoder (VTR) recovers pixel-shuffle architectures from 0% to near-baseline performance.

---

## 2. Agreed Strengths

Both reviewers affirm:

1. **Unprecedented cross-architecture breadth.** 6 models, 4 connector families, 4 LIBERO suites, 3 pruning methods, 6+ retention ratios. No concurrent work (SP-VLA, VLA-IAP, LightVLA, EfficientVLA, Compressor-VLA) covers more than 1–2 architectures. This is the paper's primary differentiator.

2. **Pixel-shuffle catastrophic cliff is definitive.** SmolVLA collapses to 0% SR at k=0.95 (removing just 5% of tokens), verified on official HuggingFace checkpoint, dual seeds, multiple methods (L2, random, attention, ToMe), and all 4 LIBERO suites. A clear, mechanistically interpretable, and practically important negative result.

3. **Double dissociation between scoring method and connector type.** Attention-based scoring achieves 99.2% on X-VLA at k=0.5 where L2-norm achieves only 42.6% (+56.6pp). L2-norm is better on OpenVLA. This structural interaction is genuinely novel, non-obvious, well-validated across suites, and has immediate practical implications.

4. **Intellectual honesty.** Both reviewers commend the transparent reporting of framework limitations, VTR failure on MLP projectors, and the confounder discussion. This level of candor is unusual and scientifically valuable.

5. **Thorough multi-seed validation for key claims.** The SmolVLA cliff, pi0.5 cliff zone, and X-VLA crossover are validated with 2–3 seeds with sub-1pp standard deviations.

---

## 3. Agreed Weaknesses (After Correcting Reviewer Errors)

Both reviewers identify these weaknesses, which withstand cross-examination:

1. **CV diagnostic is statistically underpowered.** The "continuous spectrum" and "scaling law" rest on 3 closed-loop data points (pi0.5, X-VLA, OpenVLA) for the strategy-prediction claim. SmolVLA is excluded (both methods = 0%). A perfect Spearman rho with n=3 is trivially achievable. The paper's framing as a "scaling law" overstates what 3 data points can support. OFT and pi0 are offline-only, padding the model count without adding closed-loop validation.

2. **Incomplete data matrix.** Multiple "--" entries in cross-suite tables. OpenVLA lacks multi-suite coverage in the main results (Object-only for many conditions). The paper claims "first comprehensive study" but the actual data matrix has structural gaps, with some experiments still running at submission time.

3. **LIBERO-only evaluation.** All results are from a single simulator on one robot. The abandoned SimplerEnv attempt (0% baseline) and weak MetaWorld results (26.4% SmolVLA baseline, all pruned conditions collapsed) suggest transferability is uncertain. For CoRL, the absence of any real-robot or multi-simulator validation is a meaningful gap.

4. **Confounded cross-model comparisons.** The 6 models differ simultaneously in backbone, encoder, scale, training data, and connector. Only OFT vs. OpenVLA provides a semi-controlled comparison (same connector, different action head), and OFT has no closed-loop evaluation. The paper's language often implies connector is causally isolated when the evidence is correlational.

5. **VTR contribution is narrow and architecturally derivative.** VTR is structurally identical to Perceiver Resampler / Q-Former. It works on SmolVLA only; it fails on OpenVLA (0% SR). Trained at batch size 4 vs. official batch size 512, producing a weakened baseline (44.8% reproduced vs. 59.2% official). The paper reframes around the official baseline, but the VTR training protocol mismatch is a concern.

6. **No efficiency measurements.** For a paper motivating token pruning by inference cost, there are no latency, throughput, or memory benchmarks beyond a single 6% latency improvement figure for VTR. The absence of wall-clock measurements is notable.

---

## 4. Contested Points (AC Resolution)

**Contribution novelty (R1: 3/4 vs. R2: 2/4).**
R1 values the practical, actionable contribution (cross-architecture comparison fills a genuine gap; findings are directly useful for practitioners). R2 emphasizes that the individual components (CV, attention scoring, VTR) lack methodological novelty and the 2-axis framework is descriptive rather than predictive.

**AC Resolution**: The cross-architecture breadth and double dissociation are genuine contributions that exceed "just running existing methods on more models." However, the 2-axis framework is indeed more descriptive than predictive — it organizes observations but does not predict cliff locations, amplification magnitudes, or thresholds. The "Diagnose-then-Compress" framework is essentially a decision tree (if CV < X, do Y), not a learned or validated predictor. **Consolidated Contribution: 2.5/4** — acknowledging real empirical novelty but limited methodological and theoretical advance.

**Paper framing of 2-axis framework failure.**
The task description notes that "the 2-axis framework is NOT the central contribution" and that both reviewers "treat the failed framework as if the paper is claiming it works." After reading the actual paper, I find the paper does NOT explicitly report the framework as failed with a 62% accuracy figure in the submitted text. The paper presents the 2-axis framework as a positive contribution (listed as Contribution #1) with no Table 10 or Table 11 in the actual paper.tex. The honest limitations are in the appendix and paper_framing.md (project internals), not the submitted paper. **Both reviewers are justified in engaging with the framework as presented — as a positive claim.**

**"Single pruning ratio" criticism.**
Both reviewers were briefed that this is a factual error. Confirmed: the paper evaluates k in {0.3, 0.5, 0.7, 0.85, 0.9, 0.95} and additional values (0.925, 0.8, 0.2, 0.1) for specific models. Multiple tables show full degradation curves. This criticism is invalid and should not affect scoring.

---

## 5. Factual Corrections

1. **"Single pruning ratio" (both R1 and R2)**: Incorrect. The paper evaluates 6+ keep ratios per model, with degradation curves, cliff zone characterization, and method preference reversals across k. Tables 3, 4, 5, 6, 7 all show multiple k values.

2. **"No figures" (R2)**: Accurate for the submitted PDF (11 tables, 0 figures). This is a legitimate presentation concern — the paper is extremely table-dense with no visual summary of degradation curves, no architecture diagram, and no heatmap visualization. Adding 2–3 figures would significantly improve readability.

3. **Neither reviewer's factual errors are severe enough to change scores by more than ~0.5 points.** The pruning ratio error, if corrected, addresses one listed weakness per reviewer but does not change the core concerns about CV validation, sim-only evaluation, or novelty.

---

## 6. Key Questions for Rebuttal

1. **CV beyond connector type**: Can you demonstrate that CV is predictive beyond what connector family membership already tells us? Within the MLP family (OpenVLA CV=0.215 vs. OFT CV=0.219), is there measurable pruning robustness difference consistent with the 0.004 CV gap? Without this, CV is a proxy for connector type, not an independent predictor.

2. **Attention-based scoring on additional models**: The double dissociation is the paper's strongest finding, but attention-based pruning is only tested on X-VLA. Does attention scoring help or hurt on pi0.5 (low CV, linear) and OpenVLA (high CV, MLP)? Completing this table would make the dissociation considerably more compelling.

3. **Efficiency measurements**: Can you provide wall-clock latency and peak memory measurements for at least 2 models at 2 keep ratios? A paper motivating inference efficiency must quantify the efficiency gains.

4. **VTR batch size confound**: The VTR baseline (44.8% at batch 4) is 14.4pp below official (59.2% at batch 512). How confident are you that VTR's recovery to ~60% is genuine rather than an artifact of the weakened training protocol? Would VTR at batch 512 exceed baseline?

5. **Position re-indexing confound**: After token pruning, remaining tokens receive new position indices. Have you tested masking tokens to zero while preserving original positions, to isolate information loss from positional disruption?

---

## 7. Missing Elements

Ranked by impact on the paper's strength:

1. **Complete data matrix** — Fill all "--" entries, especially OpenVLA cross-suite and attention-based pruning on additional models.
2. **Efficiency benchmarks** — Latency, throughput, memory at representative k values for 2+ models.
3. **Head-to-head comparison with one concurrent method** — Running VLA-IAP or SP-VLA on the same setup would demonstrate the diagnostic framework's explanatory power.
4. **Figures** — Degradation curve plots, architecture diagram, and/or CV-vs-strategy scatter plot would transform readability.
5. **Position-preserving ablation** — Zero-mask control to isolate positional vs. information loss.
6. **Additional benchmark** — Even one non-LIBERO benchmark with reasonable baselines would strengthen generalizability.

---

## 8. Limitations Assessment

The paper reports limitations honestly in the Discussion section: sim-only evaluation, VTR parameter/latency overhead, and single-model Perceiver Resampler validation. The internal project documents (paper_framing.md, memory.md) reveal even more honest self-assessment — abandoned SimplerEnv, failed MetaWorld transfers, framework breakage under cross-suite data — but this candor does not fully surface in the submitted paper. The Appendix includes confounder analysis and acknowledges that "the six architectures differ in backbone, encoder, and scale beyond the connector, preventing causal isolation."

**Assessment**: Limitations reporting is above average for the field. The paper could be more explicit in the main text about the CV diagnostic's statistical limitations (n=3) and the data matrix gaps.

---

## 9. CoRL Relevance

Token pruning for VLA efficiency is directly relevant to robot learning — it addresses a real deployment bottleneck. The question (why does pruning work on some VLAs but not others?) is important and timely, given the proliferation of concurrent VLA compression works. LIBERO is a respected benchmark in the CoRL community. The practical recommendations (measure CV, choose strategy accordingly) are immediately useful.

**However**, CoRL increasingly expects real-robot validation or at least multi-simulator evaluation. A pure LIBERO study, even a thorough one, may be seen as better suited to an ML venue (NeurIPS, ICML) where empirical analysis contributions are more valued. The paper's strongest claim — that connector architecture determines pruning robustness — has clear implications for VLA design, which is squarely CoRL territory.

**Verdict**: Appropriate for CoRL, though the sim-only limitation is a more significant gap at CoRL than it would be at NeurIPS.

---

## 10. Final Scores

| Dimension | R1 | R2 | AC Consolidated | Justification |
|-----------|----|----|-----------------|---------------|
| **Soundness** | 2/4 | 2/4 | **3/4** | Experiments are thorough where data exists, with multi-seed validation and appropriate controls. AC upgrades from R1/R2 because the "single pruning ratio" criticism was factual error. Main soundness gap: causal claims exceed correlational evidence, and CV has n=3 closed-loop validation. |
| **Presentation** | 3/4 | 2/4 | **2.5/4** | Well-organized paper with clear methodology, but 11 tables with zero figures creates extreme density. Multiple "--" entries in key tables. Abstract claims "6 models" but only 4 have closed-loop evaluation. Some overclaiming ("scaling law" for 3 data points). |
| **Contribution** | 3/4 | 2/4 | **2.5/4** | Cross-architecture breadth is genuine first-of-its-kind value. Double dissociation and pixel-shuffle cliff are novel findings. But: CV is undertested, VTR is derivative and narrow, 2-axis framework is descriptive. Contribution is empirical synthesis, not methodological advance. |
| **Overall** | 6/10 | 5/10 | **5.5/10** | See justification below. |
| **Confidence** | 4/5 | 4/5 | **4/5** | Thorough review of paper, supplementary materials, and project context. Familiar with VLA pruning literature and LIBERO benchmark. |

**Overall justification (5.5/10)**: The paper addresses a timely and important question with the most comprehensive cross-architecture VLA pruning evaluation to date. The double dissociation finding and pixel-shuffle cliff are genuinely novel and practically valuable. However, the paper falls short of CoRL acceptance (~25–33% rate) on several axes: the CV "scaling law" is a 3-point correlation, the data matrix has structural gaps, there are no efficiency measurements for an efficiency-motivated paper, VTR is narrowly validated and architecturally derivative, and the evaluation is simulation-only. The theoretical contribution (2-axis framework) is descriptive rather than predictive. The paper is a strong workshop paper or a borderline conference paper — it needs either deeper mechanistic insight, broader validation (more models for CV, real robot, second benchmark), or completed data matrix to cross the acceptance threshold.

---

## 11. Recommendation

**Borderline — Weak Reject.**

The paper provides useful empirical knowledge and the cross-architecture breadth is a genuine differentiator from concurrent VLA pruning works. The double dissociation and pixel-shuffle cliff are findings the community needs. However, the theoretical contribution is limited (descriptive framework, not predictive), the key diagnostic (CV) is validated on too few models (n=3 closed-loop), VTR is narrow, and the absence of efficiency benchmarks and real-robot validation weakens the CoRL fit. A revision addressing data completeness, CV validation on additional models, and efficiency measurements could move this to a solid accept.
