---
dream_id: dream_20260514T140607
tier: median
overall_score: 3/5 — Findings
timestamp: 2026-05-14T14:57:00.615406+00:00
---

# Dream Review Report: Ordinal Depth Estimation of Recursive Generation

**Paper:** "Ordinal Depth Estimation of Recursive Generation: A Depth Degradation Atlas for Model Collapse Characterization"
**Venue:** EMNLP 2026 (ACL Rolling Review)
**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-14

---

## Reviewer Assignments
- **R1:** Methods & Experiments
- **R2:** Novelty & Related Work

---

## R1 Review: Methods & Experiments

### Summary
This paper formalizes ordinal generation depth estimation and proposes DCOL, a DeBERTa-v3-large method with contrastive ordinal loss, learnable non-uniform margins, surprisal-augmented anchors, and strategy conditioning. It also contributes a Depth Degradation Atlas characterizing recursive degradation across 3 models × 3 strategies × 6 depths. DCOL achieves 57.1% 6-class accuracy (chance 16.7%) and 82.3% 4-class accuracy, outperforming the best baseline (CORAL) by +3.3pp. Experimental coverage is exceptionally thorough with 11 subsections and 16 tables.

### Strengths (Methods)
- **Well-motivated design loop.** The Atlas documents non-uniform inter-depth geometry, which directly motivates the learnable non-uniform margins in DCOL. This observation→design→validation chain is methodologically clean.
- **Ordinal inductive bias is principled.** The ordinal regression head mapping to cumulative probabilities P(D>d) with threshold at 0.5 is well-established and appropriate.
- **Feature engineering is well-grounded.** The 19-dimensional statistical feature set is comprehensive. Identification of surprisal variance as the strongest depth signal (monotonicity 0.847) has standalone scientific value.
- **Strategy conditioning addresses a real problem.** Different strategies produce different EDD values (range 2–4), and the lightweight strategy embedding is an appropriate solution.

### Strengths (Experiments)
- **Exceptional experimental breadth.** 11 experiment subsections covering per-model benchmarks, full baseline comparison, ablation, EDD analysis, feature monotonicity, extended depth, granularity ablation, cross-model LOMO, cross-strategy LOSO, downstream curation, cross-scale 7B probe, and wild-data calibration. Unusually thorough for a 10-page paper.
- **Comprehensive and fair baselines.** 9 methods spanning feature-based (RF, DivEye, LOKI), ordinal regression (CORAL), standard classification (CE DeBERTa), cascade (binary ensemble), regression (PPL), end-to-end neural (DeBERTa E2E), and zero-shot (GPT-4o). Same-backbone CORAL isolates DCOL-specific contributions.
- **Generalization rigorously tested.** LOMO (47.0% ± 3.6%) and LOSO (52.0% ± 2.1%) directly address external validity. Finding that strategy transfer is easier than model transfer is informative.
- **Ablation cleanly decomposes contributions.** Each component has monotonically ordered contribution (0.9–2.4pp). Transparent reporting of mild positive interaction.

### Weaknesses (Methods)
- **(Major) Contrastive loss formulation appears incomplete.** Eq. 1 (L = Σ max(0, ||h_i − h_j||₂ − m(|d_i − d_j|))²) is a pull-only loss trivially minimized by embedding collapse to a single point. A correct contrastive ordinal loss requires both attractive and repulsive terms. If correctly implemented but incorrectly described, this is a major reproducibility concern.
- **(Major) Surprisal computation reference model creates potential circularity.** The paper does not specify which model computes token-level surprisal, whether the generating model serves as its own reference (tautological signal), or how the reference model is chosen at inference on wild data. Contributes 1.3pp in ablation.
- **(Major) Depth-0 confound inflates headline numbers.** Depth 0 is human-written; depths 1–5 are model-generated. The d0-vs-d1 AUC of 0.998 is essentially binary human-vs-machine detection. A 5-class (d1–d5 only) accuracy is needed to isolate genuine ordinal depth estimation from binary detection.
- **(Minor) Strategy conditioning at inference on unknown-strategy data is unclear.** For wild-data deployment, the decoding strategy is unknown. How is conditioning handled?
- **(Minor) Margin monotonicity constraint enforcement mechanism is unspecified.** Different implementations (projected gradient, softmax reparameterization, cumulative sum) could lead to different optimization behavior.

### Weaknesses (Experiments)
- **(Major) DCOL improvement over baselines is modest.** DCOL 57.1% vs CORAL 53.8% (+3.3pp) and vs DeBERTa E2E 55.3% (+1.8pp). A straightforward DeBERTa fine-tuning already achieves 55.3% with no ordinal or contrastive structure. The ablation confirms: all three modifications together contribute only 4.0pp over vanilla contrastive.
- **(Major) Cross-model generalization shows concerning failure.** OLMo held-out fails the 0.45 gate at 42.1%. The 10pp gap between in-distribution (57.1%) and cross-model mean (47.0%) suggests the model captures substantial model-specific signal.
- **(Minor) Cross-scale evaluation is too limited.** Only one larger model tested, only 4-class granularity. "Depth signals transfer across scales" rests on a single data point.
- **(Minor) Downstream curation experiment lacks task-based evaluation.** 3.1% PPL reduction (p=0.038) is marginal in both statistical significance and practical magnitude. No evaluation on downstream NLP tasks (MMLU, reasoning, etc.).
- **(Minor) No confusion matrix or error analysis.** Understanding failure modes is important for a new task definition.
- **(Minor) No figures in an empirical Atlas paper.** 16 tables and zero figures is a missed opportunity for visualization of feature evolution, embedding structure, AUC decay curves.

### Questions for Authors
1. Provide the complete training objective including the repulsive term. As written, Eq. 1 is trivially minimized by embedding collapse.
2. Which reference model computes token-level surprisal? Is it the same as the generating model?
3. What is the 5-class (d1–d5) accuracy for DCOL and baselines?
4. How is strategy conditioning handled at inference when the strategy is unknown?
5. How does the monotonicity constraint on margins get enforced during training?
6. Has depth-0 been tested with non-Wikipedia seed corpora to verify the signal is not a domain artifact?
7. Can you provide error bars or bootstrap CIs for the 3-fold LOMO experiment?

### R1 Preliminary Scores
- Soundness: 3/5
- Excitement: 3.5/5
- Overall: 3/5
- Confidence: 4/5

---

## R2 Review: Novelty & Related Work

### Summary
This paper proposes ordinal generation depth estimation as a new task (beyond binary synthetic detection), introduces DCOL as a contrastive ordinal method, and contributes a Depth Degradation Atlas documenting an Effective Discriminable Depth (EDD ≈ 3). The task formulation is genuinely novel and timely given increasing concerns about recursive synthetic contamination. However, DCOL is an incremental adaptation of existing contrastive ordinal methods (CLOC), the bibliography is critically sparse (only 3 references), and the modest DCOL improvement (+3.3pp) suggests the primary value lies in the task definition and Atlas rather than the method.

### Strengths (Novelty)
- **Task formulation is genuinely new.** Moving from binary (real vs. synthetic) to ordinal (depth 0–K) is a meaningful conceptual advance. No prior work has formalized recursive depth estimation as a standalone task.
- **EDD is a useful quantitative concept.** Defining the Effective Discriminable Depth as the maximum depth where adjacent-pair AUC ≥ 0.72 gives the model collapse community a concrete, measurable boundary. The finding that EDD ≈ 3 across conditions answers a previously open question.
- **Atlas extends prior characterization work.** Shumailov et al. (2024) documented that collapse happens; this paper documents where the information boundary lies and how it varies across conditions (model × strategy). The "feature handoff" finding (surprisal variance → Zipf α beyond EDD) is a novel observation about degradation phases.
- **Cross-model and cross-strategy generalization studies** are a meaningful contribution — prior model collapse work rarely examines whether degradation characterization transfers.

### Strengths (Presentation & Framing)
- **Honest, well-calibrated limitations.** The paper explicitly acknowledges: OLMo rotation failure, effective granularity limited to 4 classes, scale transfer gap, controlled-vs-wild gap, and moderate DCOL advantage. This is unusually transparent.
- **Appropriate scoping of downstream curation.** Framed as "proof-of-concept" with explicit limitations rather than a strong practical contribution.
- **Logical experimental progression.** Per-model → pooled → ablation → Atlas → generalization → application follows a natural arc.

### Weaknesses (Novelty)
- **(Major) DCOL is an incremental adaptation of CLOC.** The three modifications (learnable margins, surprisal anchors, strategy conditioning) are standard engineering choices. Learnable margins: standard in metric learning. Surprisal anchors: a feature-based hard negative mining variant. Strategy conditioning: a standard conditioning mechanism. The vanilla contrastive framework without modifications (53.1%) underperforms CORAL (53.8%), meaning the +3.3pp gain is entirely from engineering choices, not fundamental methodological advance.
- **(Minor) EDD threshold (0.72) is arbitrary.** The choice of AUC ≥ 0.72 as the EDD boundary is not motivated. Different thresholds (0.70, 0.75, 0.80) would yield different EDD values. A sensitivity analysis is needed.
- **(Minor) The benchmark construction follows a standard synthetic-data pipeline.** Generating recursive chains by prompting models with prior outputs is a straightforward setup. The novelty is in framing it as an ordinal estimation benchmark, not in the data construction itself.

### Weaknesses (Related Work)
- **(Major) Only 3 references is critically inadequate for EMNLP.** The bibliography is missing entire subfields:
  - **Watermarking literature** (Kirchenbauer et al. 2023, "A Watermark for LLMs") — relevant because watermarking provides an alternative approach to tracking generation provenance.
  - **Data curation** (DSIR, QuRating, FineWeb) — directly relevant to the downstream curation motivation.
  - **Multi-class/multi-source attribution** (Uchendu et al. 2020, "Authorship Attribution for Neural Text Generation") — prior work on distinguishing among multiple generators, adjacent to ordinal depth.
  - **Model collapse theory** (Alemohammad et al. 2023, "Self-Consuming Generative Models") — foundational theoretical work on recursive generation.
  - **Binoculars** (Hans et al. 2024), **Fast-DetectGPT** (Bao et al. 2024) — mentioned in passing but not cited.
  - **CLOC** (CVPR 2025) — the method DCOL is most closely adapted from, mentioned but not fully cited.
  - **Data contamination detection** (Shi et al. 2023, "Detecting Pretraining Data") — related task of detecting training data artifacts.
  - A venue like EMNLP typically expects 30+ references. Three references makes it impossible to properly position the work.

- **(Major) Related work section is too brief (~0.5 page).** Three paragraphs covering model collapse, synthetic detection, and ordinal classification cannot adequately survey the relevant literature. Missing discussions of: (a) the relationship between depth estimation and authorship attribution, (b) connections to data quality scoring, (c) how watermarking interacts with depth estimation, (d) connections to distribution shift detection.

- **(Minor) Binary detectors (LOKI, DivEye, Binoculars) are mentioned but not cited.** These appear as baselines in experiments but lack proper citations in the text.

### Weaknesses (Claims & Framing)
- **(Major) Depth-0 confound in headline metrics.** The 82.3% 4-class accuracy and 57.1% 6-class accuracy include the near-perfect d0 classification (AUC 0.998), which is essentially binary human-vs-machine detection — a near-solved problem. The genuine ordinal contribution (distinguishing d1 from d2 from d3) is obscured. Reporting d1–d5 accuracy as a companion metric is essential.
- **(Minor) "First systematic empirical map" claim may be overstated.** Shumailov et al. (2024) and Drayson et al. (2025) provide systematic characterizations of recursive degradation. The novelty is in the ordinal estimation lens and the EDD formalization, not in being the first to empirically characterize degradation.
- **(Minor) Framing prioritizes DCOL over Atlas.** The Abstract and Introduction lead with DCOL, but the Atlas and EDD concept appear to be the more durable contributions. The framing should be rebalanced.

### Questions for Authors
1. Why does the bibliography contain only 3 references? Were additional references omitted for anonymity or page limits?
2. How does DCOL compare to a simple recalibration of CLOC for text? What is the specific architectural novelty beyond known techniques?
3. What is the sensitivity of EDD to the threshold choice? Report EDD at 0.70, 0.75, and 0.80.
4. How do you position this work relative to multi-source attribution (Uchendu et al.)? Is ordinal depth estimation a special case of attribution?
5. Could watermarking-based approaches solve this problem more directly? Why is statistical detection preferred?

### R2 Preliminary Scores
- Soundness: 3/5
- Excitement: 3/5
- Overall: 2.5/5
- Confidence: 4/5

---

## Roundtable Discussion

### Step 2: Cross-Sharing

R1 shared with R2: The loss formulation (Eq. 1) appears to be missing a repulsive term, which is a fundamental technical concern. The experimental breadth is exceptional (11 subsections, 16 tables), but DCOL's advantage is narrow (+1.8pp over vanilla DeBERTa E2E). The Atlas and EDD are the strongest contributions.

R2 shared with R1: The bibliography (3 references) is critically inadequate for EMNLP — missing entire subfields including watermarking, data curation, multi-source attribution, and model collapse theory. DCOL is an incremental adaptation of CLOC with engineering-level modifications. The framing oversells the method and undersells the Atlas.

### Step 3: Convergence

**Points of agreement (both reviewers):**
1. Task formulation (ordinal depth estimation) is genuinely novel and timely — this is a real contribution.
2. The Depth Degradation Atlas and EDD (≈3) concept are the paper's primary and most durable contributions.
3. Eq. 1 loss formulation is incomplete as written — missing repulsive term is a critical reproducibility concern.
4. Depth-0 confound inflates headline metrics. A d1–d5 accuracy is essential as a companion metric.
5. DCOL improvement is modest (+3.3pp over CORAL, +1.8pp over E2E); the paper should rebalance framing from method to Atlas.
6. Experimental coverage is exceptionally thorough, which partially compensates for method weakness.
7. Limitations are honestly reported — an unusual and commendable feature.

**Points of divergence (resolved):**
- R2 initially scored lower (2.5) due to bibliography concerns. After discussion, panel agrees the bibliography sparsity is a serious but fixable issue — the experimental substance warrants Findings-level acceptance even with this gap. R2 adjusts to 3.0.
- R1 gave higher Excitement (3.5) based on experimental depth. R2 converges to 3.0 Excitement, noting that the Atlas concept is exciting but the execution (no figures for an "Atlas" paper) dampens impact. Panel settles on 3.0 Excitement.

### Step 4: Consolidated Assessment

**Consensus Scores (ARR/EMNLP 2026 scale):**
- **Soundness:** 3/5 — The task formulation and Atlas are sound. The loss formulation (Eq. 1) has a critical presentation/reproducibility issue. Experiments are thorough but DCOL's technical contribution is incremental.
- **Excitement:** 3/5 — The EDD concept and ordinal depth estimation task are genuinely interesting to the model collapse community. But the moderate improvements and execution gaps (no figures, sparse bibliography) limit excitement.
- **Overall Assessment:** 3/5 (Findings) — The paper introduces a novel and timely task (ordinal depth estimation), provides a valuable empirical characterization (Depth Degradation Atlas, EDD ≈ 3), and demonstrates thorough experimental methodology. However, the method contribution (DCOL) is incremental (+3.3pp over CORAL, +1.8pp over E2E), the loss formulation has a critical presentation error, the bibliography is critically sparse (3 references for EMNLP), and headline metrics are inflated by the depth-0 confound. The Atlas and EDD are the primary contributions and would be well-suited for Findings. Main conference acceptance would require: fixing the loss formulation, expanding the bibliography substantially, reporting d1–d5 metrics, and rebalancing framing toward Atlas.
- **Confidence:** 4/5

---

## Summary of Required Revisions for Acceptance

### Must-Fix (for Findings)
1. **Fix Eq. 1:** Provide the complete contrastive loss with both attractive and repulsive terms. Current formulation is trivially minimizable.
2. **Expand bibliography** to ≥25 references covering watermarking, data curation, multi-source attribution, model collapse theory, and properly cite all baselines mentioned.
3. **Report d1–d5 (synthetic-only) accuracy** as a companion metric to isolate ordinal depth estimation from binary detection.
4. **Specify the surprisal reference model** and address potential circularity.

### Should-Fix (for Main Conference)
5. Add figures: confusion matrices, AUC decay curves, feature evolution trajectories, embedding visualizations. An "Atlas" paper with zero figures is incongruous.
6. Rebalance framing: lead with Atlas/EDD as primary contribution, position DCOL as one strong implementation within the framework.
7. EDD threshold sensitivity analysis (at 0.70, 0.75, 0.80).
8. Clarify strategy conditioning at inference when strategy is unknown.
9. Add task-based downstream evaluation (beyond PPL) for the curation experiment.

### Nice-to-Have
10. Error analysis / confusion matrix to characterize failure modes.
11. Volume-matched curation comparison.
12. Reference model sensitivity analysis for surprisal features.

---

## Experiment Coverage Assessment

All 13-14 experiments from the design document are covered in the paper:
| Experiment | Paper Section | Status |
|---|---|---|
| OLMo-1B benchmark | §4.1, Table 1-2 | ✓ Covered |
| GPT-2 XL benchmark | §4.1, Table 1,3 | ✓ Covered |
| DCOL training | §4.2, Table 4-5 | ✓ Covered |
| Leave-one-model-out | §4.7, Table 11 | ✓ Covered |
| Depth Degradation Atlas | §4.4, Table 7-8 | ✓ Covered |
| Leave-one-strategy-out | §4.8, Table 12 | ✓ Covered |
| DeBERTa E2E | §4.2, Table 5 | ✓ Covered |
| Baseline battery | §4.2, Table 4 | ✓ Covered |
| DCOL ablation | §4.3, Table 6 | ✓ Covered |
| Depth extension | §4.5, Table 9 | ✓ Covered |
| Granularity ablation | §4.6, Table 10 | ✓ Covered |
| Downstream curation | §4.9, Table 13 | ✓ Covered |
| 7B cross-scale probe | §4.10, Table 14 | ✓ Covered |
| Wild-data calibration | §4.11, Table 15-16 | ✓ Covered |

Experiment coverage is 100%. The paper faithfully represents all planned experiments.

---

## Final Verdict

**Overall: 3/5 — Findings**

The paper's strongest asset is the Depth Degradation Atlas and EDD concept, which provides genuine scientific value to the model collapse community. The task formulation is novel. Experimental thoroughness is exceptional. However, the method (DCOL) is incremental, the loss formulation has a critical error, the bibliography is inadequate for a top venue, and headline metrics are inflated by the depth-0 confound. Suitable for Findings with revisions; main conference would require substantial reworking of framing, bibliography, and loss presentation.