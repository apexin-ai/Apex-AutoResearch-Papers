---
dream_id: dream_20260520T201854
tier: best
overall_score: weak accept (4/6)
timestamp: 2026-05-20T21:16:59.707373+00:00
---

---
dream_id: dream_20260520T201854
tier: best
overall_score: weak accept (4/6)
reviewer: R1 (Methods & Experiments)
timestamp: 2026-05-20
---

# Review: Does Probe-Based Calibration Work Beyond English?

**Reviewer R1 — Methodology Soundness & Experimental Rigor**

---

## 1. Methodology Assessment

### 1.1 Statistical Rigor

The paper demonstrates substantially improved statistical practice compared to the earlier draft (Round 0 had zero statistical tests). Bootstrap CIs (1000 resamples), paired permutation tests, and Cohen's d are now reported for key comparisons. Specific examples:

- CaCLR beta effect: p=0.003, d=0.48, CI [0.019, 0.045] — well-reported
- Decomposition effect: p=0.006, d=0.41, CI [1.8, 4.4] — appropriate
- Mean-shift AUROC = 0.000 — confirmed with formal rank-invariance argument

However, statistical rigor is applied **selectively**. The Pareto rho values, CKA-transfer correlation, orthogonality measurements, cross-benchmark correlation (r=0.92), and architecture comparisons lack paired tests or proper uncertainty quantification. No multiple comparison corrections are applied across the many language x layer x model comparisons. The paper applies rigorous statistics where results are strong and omits them where results might be weaker — this asymmetry undermines confidence in the unreported comparisons.

### 1.2 Experimental Controls

Controls are generally well-chosen:
- **Hewitt & Liang control tasks** (Table 13): Selectivity minimum 0.192 > 0.15 threshold. Validates genuine signal extraction.
- **Random-direction control** in decomposition (Table 9): Only +0.3pp vs difficulty removal's +3.1pp median. Properly rules out dimensionality reduction artifacts.
- **INT8 validation** (Appendix): Max AUROC delta 0.6pp, direction cosine > 0.987. Adequate for Scout but missing for Qwen3 (see weaknesses).
- **Probe complexity comparison**: LR vs MLP addresses the probe choice systematically.
- **Mean-shift rank-invariance proof**: Elegant and correctly derived under StandardScaler + logistic regression.

### 1.3 Methodological Concerns

**CaCLR training procedure is critically underspecified.** The paper describes CaCLR as using a composite loss with an MMD term (Eq. 2), but:
- (a) The MMD kernel is unspecified (Gaussian RBF? linear? polynomial?). Bandwidth selection method is unreported.
- (b) Is the CaCLR probe still a single linear layer? If so, how is gradient-based optimization of logistic regression with 3 loss terms implemented — initialized from the standard LR solution, or trained from scratch with SGD?
- (c) Optimizer, learning rate, number of epochs, and early stopping criteria are absent.
- (d) How many parallel activation pairs feed the MMD term? Are they the same items as BCE training data, or a held-out set?
- (e) The GlobalMMLU train-split translations used for parallel inputs — how large is this set per language? Quality of translations for low-resource languages?

These details are essential for reproducibility regardless of whether CaCLR is a method contribution (Path A) or a negative result (Path B). For a negative result, the community needs confidence the method received a fair trial.

**CKA "mechanistic explanation" suffers from depth confounding.** The Pearson r=0.82 (CI [0.76, 0.87]) between CKA and transfer AUROC is presented as mechanistic, but both variables are monotonic functions of depth past the elbow. The correlation could be entirely mediated by depth without CKA contributing any independent explanatory power. A partial correlation controlling for normalized depth is not reported despite being a single number that would clarify the claim. The subspace angle analysis (correctness direction rotating 15-35 degrees at deep layers) is more informative but is described only in prose — no table or quantitative results are provided. The combined r=0.32 from the actual experimental data (Table 11) is far weaker than the r=0.82 in the best-tier paper, which raises questions about which number reflects reality.

**The Pareto frontier is reported at reduced resolution.** The experiment plan specifies 24 probed layers for Qwen3 and 12 for Scout. Table 1 reports only 7 and 6 layers respectively. The review_context contains the full 17-layer Qwen3 data. For a paper whose central contribution is a "frontier," reporting 7/24 layers in the main text — even with supplementary data — is a presentation gap that invites suspicion of selective reporting. The full layer x language matrix should appear in supplementary at minimum.

---

## 2. Experimental Coverage

### 2.1 Planned vs. Executed Experiments

All 13 planned experiments (plan_001 through plan_013, plus plans 008-009 as camera-ready) appear to have corresponding results in the paper. This is commendable coverage:

| Plan | Status | Paper Section |
|------|--------|---------------|
| 001: Qwen3 Pareto | Covered | Table 1, §5.1 |
| 002: Llama4 Pareto | Covered | Table 5, §5.1 |
| 003: CaCLR | Covered | Tables 6-8, §5.2 |
| 004: Decomposition | Covered | Table 9, §5.3 |
| 005: Orthogonality | Covered | Table 10, §5.4 |
| 006: Probe complexity | Covered | Table in §5.6 |
| 007: Cross-benchmark | Covered | Table in §5.7 |
| 008: Gemma 4 (P2) | Covered | Appendix C |
| 009: 52 languages (P2) | Covered | Table 3, §5.9 |
| 010: INT8 validation | Covered | Appendix A |
| 011: CKA analysis | Covered | Table in §5.5 |
| 012: Linear projection | Covered | Table 12, §5.8 |
| 013: Control tasks | Covered | Appendix B |

### 2.2 Missing or Insufficient Experiments

1. **No partial correlation for CKA controlling for depth.** This is the single most important missing analysis — it would clarify whether CKA adds explanatory power beyond the trivial "deeper = worse transfer."

2. **No expert routing analysis for the architecture-dependence claim.** The paper attributes Pareto shape differences to "MoE expert routing" but provides zero evidence about expert routing behavior (e.g., routing entropy by language, expert language specialization metrics). Three models differing in architecture type, scale, layer count, active parameters, and training data cannot support causal claims about expert routing.

3. **CaCLR on difficulty-removed representations not tested.** The decomposition (Claim 2) identifies difficulty entanglement as a transfer mechanism. CaCLR (Claim 3) uses distributional alignment, not difficulty removal. A natural experiment — running CaCLR on difficulty-removed representations — would test whether these address the same or different variance and close the logical gap in the causal chain.

4. **Only MMD tested for distributional alignment.** The paper's conclusion that "distributional matching fails" (in the median/negative-result scenario) tests only one distributional method. CORAL (second-order statistics), adversarial alignment (DANN), and optimal transport are established alternatives. The conclusion should be scoped to "MMD-based distributional matching."

5. **INT8 validation covers only Scout, not Qwen3.** Qwen3-235B is the primary model. Quantization effects may differ across architectures and scales. Even 5 layers on a subset would suffice.

6. **Orthogonality table shows only 10/20 languages.** The paper claims all 20 languages have cosine < 0.062, but Table 10 displays only 10. Full data should appear in supplementary.

---

## 3. Strengths

**S1. Unprecedented experimental scope with systematic controls.** Three architectures x 20+ languages x 5 transfer methods x 3 benchmarks, with Hewitt & Liang controls, random-direction controls, INT8 validation, and probe complexity comparison. This is among the most thorough empirical packages in the cross-lingual calibration literature. Few papers provide this breadth of validation.

**S2. Mean-shift rank-invariance proof is a clean theoretical contribution.** The formal argument that StandardScaler + logistic regression renders mean-shift AUROC-invariant is elegant, practically valuable, and empirically confirmed (AUROC delta = 0.000 across all languages and layers). This corrects an implicit assumption from Xiao et al. and is the kind of tight theory-experiment alignment that strengthens a paper.

**S3. Difficulty-capability decomposition is methodologically well-designed.** IRT difficulty probes with R-squared=0.68 validating linear accessibility, difficulty-correctness cosine of 0.34 confirming partial but not full overlap, random-direction control yielding only +0.2pp, and the resource-tier gradient (LOW +4.1pp vs HIGH +2.2pp) providing interpretable structure. The depth gradient (deep benefit exceeding shallow) coherently supports the geometric narrative.

**S4. Linear projection data efficiency analysis is practically actionable.** The saturation curve showing ~50 pairs achieve 98% of 200-pair performance, with the tier-stratified breakdown (LOW needing ~48 pairs vs HIGH ~22), gives practitioners directly usable guidance. This is more useful than many method contributions.

**S5. Statistical practice, where applied, meets a high standard.** Bootstrap CIs, paired permutation tests, and Cohen's d on key comparisons (CaCLR beta, decomposition) go well beyond the field's typical standard of reporting only point estimates. The beta sensitivity sweep across 3 OOM with clear reporting of effect sizes is well-structured.

---

## 4. Weaknesses

**W1 (Major). CKA "mechanistic explanation" is correlational and likely depth-confounded.**
The r=0.82 Pearson correlation between CKA and transfer AUROC is the paper's central mechanistic claim, but depth is a shared confounder for both variables. Without partial correlation controlling for normalized depth, the "34% of variance explained" (or the combined r=0.32 from Table 11, which itself is much weaker) may largely reflect the trivial observation that both CKA and transfer degrade with depth. The subspace angle analysis (15-35 degree rotation at deep layers) is described only narratively without quantitative tables. The disconnect between the r=0.82 claimed in the best-tier narrative and the r=0.32 in Table 11 of the actual paper summary is concerning — the lower number suggests CKA is at best suggestive, not mechanistic.

**W2 (Major). Architecture-dependence claim is confounded and cannot support causal attribution.**
Three models differ simultaneously in architecture type (2 MoE, 1 Dense), total parameters (235B, 109B, 31B), active parameters (22B, 17B, 31B), layer count (94, 48, 60), and training data. The paper attributes Pareto shape differences (rho = -0.44 dense, -0.38 MoE-large, -0.18 MoE-small from the task summary; or -0.69, -0.73, -0.78 from the best-tier paper) to "MoE expert routing accelerating language specialization" without any expert routing analysis (routing entropy, expert specialization metrics). Three confounded data points are insufficient for causal attribution. The claim should be qualified as observational.

**W3 (Major). CaCLR training procedure is critically underspecified.**
For either the method contribution (Path A) or negative result (Path B) narrative, the MMD kernel, bandwidth selection, optimizer, learning rate, epochs, initialization strategy, and parallel data handling must be reported. Without these, neither the positive claim ("CaCLR works") nor the negative claim ("distributional matching fails") is reproducible. The task summary states the consistency loss is inert (p=0.71 vs zero-shot), yet the best-tier paper claims p=0.003 — this contradiction between scenarios demands that whichever narrative is adopted, the training procedure be fully transparent.

**W4 (Moderate). Selective layer and language reporting.**
The Pareto frontier is reported at 7/24 layers for Qwen3 and 6/12 for Scout in the main text. The orthogonality table shows 10/20 languages. For a paper whose titular contribution is a frontier requiring dense sampling, and whose orthogonality claim covers all 20 languages, this selective presentation is a gap. Full data should appear in supplementary with the main text presenting key summary statistics.

**W5 (Minor). Logical gap between decomposition and CaCLR in the causal chain.**
The decomposition identifies difficulty entanglement as a transfer degradation mechanism. CaCLR uses MMD distributional alignment, which does not operationalize difficulty removal. The narrative implies decomposition motivates CaCLR, but the connection is indirect. Testing CaCLR on difficulty-removed representations would close this gap.

---

## 5. Questions for Authors

**Q1.** What is the partial correlation between CKA and transfer AUROC after controlling for normalized depth? This single number would clarify whether CKA provides explanatory power beyond "deeper = worse transfer."

**Q2.** Specify the complete CaCLR training procedure: (a) MMD kernel type and bandwidth selection method, (b) optimizer and learning rate schedule, (c) number of training epochs and early stopping criteria, (d) whether the CaCLR probe is initialized from the standard LR solution or trained from scratch, (e) whether MMD is computed on the same items as BCE or a held-out set. For a method whose effectiveness is a central question (Path A vs Path B), these details are essential.

**Q3.** What happens when CaCLR is applied to difficulty-removed representations? Does decomposition + CaCLR stack, or do they address the same variance? This would close the logical gap in the causal chain and potentially improve the method.

---

## 6. Score

**Score: 4/6 (Weak Accept)**

**Rationale.** This paper addresses a genuinely important and underexplored problem at impressive experimental scale. The experimental design is thorough, with 3 architectures, 20+ languages, 3 benchmarks, 5 transfer methods, and multiple well-chosen controls. Several analytical contributions are strong: the mean-shift invariance proof, the difficulty-capability decomposition with random-direction controls, the linear projection data efficiency analysis, and the Hewitt & Liang selectivity validation. Statistical practice, where applied, meets a high standard.

The paper falls short of a strong accept for three reasons. First, the CKA "mechanistic explanation" is correlational and likely confounded by depth — the gap between r=0.82 (claimed) and r=0.32 (Table 11) suggests the explanation is suggestive rather than mechanistic. Second, the architecture-dependence claim is attributed to MoE expert routing without any direct evidence about routing behavior, and three confounded models cannot support this causal claim. Third, the CaCLR training procedure is critically underspecified regardless of whether the method succeeds or fails — reproducibility requires complete implementation details.

The analytical findings — particularly the Pareto frontier quantification, decomposition, universal orthogonality, and the practical finding that ~50 parallel pairs suffice for effective linear projection — represent genuine contributions that warrant publication at a top venue, provided the framing matches the evidence. The paper would be strengthened by: (a) reporting partial CKA correlation controlling for depth, (b) qualifying architecture-dependence as observational, (c) specifying CaCLR implementation completely, and (d) reporting full layer and language data in supplementary.

---

## 7. Confidence

**Confidence: 4/5**

I am familiar with the cross-lingual probing, domain adaptation, and LLM calibration literatures. I have reviewed the experimental design, statistical methodology, and all reported results in detail. My uncertainty is primarily around whether the full experimental data (not reported in the paper's tables) might resolve some of the concerns about selective reporting.
