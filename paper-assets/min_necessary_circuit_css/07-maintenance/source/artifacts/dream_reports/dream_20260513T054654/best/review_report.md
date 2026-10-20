---
dream_id: dream_20260513T054654
tier: best
overall_score: 2/6 Reject
timestamp: 2026-05-13T06:26:41.432657+00:00
---

# Dream Review Report: Circuit Structural Similarity (CSS)

**Dream ID**: 20260513T054654
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-13

---

## Roundtable Process

- **R1** (Methods + Experiments): Focused on methodological soundness, experimental rigor, implementation correctness, and missing controls.
- **R2** (Novelty + Related Work): Focused on conceptual novelty, positioning against prior work, reference completeness, and significance.
- **Step 1**: Independent reviews completed.
- **Step 2**: Cross-sharing — reviewers exchanged findings.
- **Step 3**: Convergence — strong agreement on all critical issues; minor differences in emphasis.
- **Step 4**: This synthesis.

---

## Paper Summary

The paper proposes Circuit Structural Similarity (CSS), a binary consensus score computed by intersecting binarized edge sets from K≥3 circuit discovery methods drawn from distinct algorithmic families. On four tasks (IOI, SVA, Factual Recall, Arithmetic) spanning the localized-to-distributed circuit spectrum and four models (GPT-2 Small 117M, Qwen-2.5 0.5B, Gemma-2 2B, Llama-3.1 8B), the paper claims that (1) CSS=1.0 circuits are 3–7× smaller yet achieve higher CPR than any single method when methods genuinely disagree (Jmax < 0.55), and (2) CSS utility is predicted by inter-method correlation (Spearman ρ=0.94, p=0.005). A fourth method family (IFR) is introduced to increase diversity. A fitted Jaccard threshold (~0.53) is proposed as a practitioner meta-diagnostic.

---

## Consolidated Strengths

1. **Well-motivated research question.** The observation that different circuit discovery methods produce strikingly different circuits is well-documented but underexploited. Framing cross-method consensus as a quality filter (rather than treating disagreement as noise) is a clean, useful conceptual contribution. (R1, R2 agree)

2. **Honest treatment of negative results.** Arithmetic as a principled negative case — where CSS fails because task structure forces method convergence — is more scientifically interesting than a universal superiority claim. The conditional framing ("CSS helps when methods disagree") is intellectually honest and strengthens the paper. (R1, R2 agree)

3. **Actionable meta-diagnostic.** The Jaccard threshold (~0.53) as a decision rule ("compute Jmax first, then decide whether to invest in consensus") is the most practically valuable contribution. If validated at scale, this would be immediately useful to practitioners. (R1, R2 agree)

4. **Methodological simplicity.** CSS is trivial to implement (set intersection), avoids the score calibration problem of continuous averaging (cf. Mondorf et al.), and is paradigm-agnostic. This is a feature, not a weakness. (R1)

5. **CIRCUS differentiation.** The contrast between within-method threshold stability (CIRCUS, negative CPR) and cross-method consensus (CSS, positive CPR) is conceptually compelling, even though the current implementation has issues (see weaknesses). (R1, R2 agree)

6. **Ablation coverage.** Top-k sensitivity (k=50–150), ablation method robustness (zero/mean/resample), and the CIRCUS comparison collectively demonstrate awareness of the right robustness questions. (R1)

7. **Complete experiment design.** All 10 planned experiments from the design are represented in the paper, covering 4 tasks × 4 models, sensitivity sweeps, ablation protocol robustness, and a competitor comparison. The experimental *design* is thorough and well-structured. (R1, R2 agree)

---

## Consolidated Weaknesses

### Critical

**W1. The majority of reported results are simulated/projected, not from actual experimental runs.**
The paper's own Limitations section acknowledges: "The 'best tier' experiments use simulated evaluation numbers; full replication on the actual models is needed for camera-ready." This means Tables 2 (SVA), 4 (Factual Recall), 5 (cross-model scaling), and 6 (Jaccard–utility correlation) contain projected numbers rather than measured results. The cross-model results (Qwen, Gemma-2, Llama-3.1) and at least 2 of the 4 GPT-2 tasks appear simulated. The Spearman ρ=0.94 (p=0.005) — the paper's central statistical claim — is computed over a mixture of real and projected data points, rendering the p-value meaningless. This is the single most damaging issue. **(R1, R2 unanimous)**

**W2. The central correlation claim rests on insufficient real data.**
Even setting aside the simulation issue, n=6 data points for a Spearman correlation yields an extremely wide confidence interval on ρ. The 6 points cluster into two groups (3 low-Jaccard/positive-Δ, 3 high-Jaccard/negative-Δ), meaning a step function at Jaccard~0.5 would fit equally well. The fitted threshold CI of [0.48, 0.58] implies precision that 6 points cannot support. **(R1, R2 agree)**

### Major

**W3. EAP-IG and Edge Pruning are not fully independent algorithmic families.**
The paper claims K=3 methods from "3 different algorithmic families," but EP uses mask gradients, making it gradient-adjacent to EAP-IG. The Arithmetic Jaccard of EAP-IG×EP = 0.695 empirically confirms high correlation. The "3 independent families" framing is overstated. **(R1)**

**W4. IFR is underspecified and overclaimed as a contribution.**
IFR is described in one sentence with no pseudocode, no algorithmic analysis, and no standalone evaluation. The method has a known granularity mismatch: it assigns identical scores to all head×QKV edges within a (src, dst_layer) pair, making it effectively layer-level while other methods operate at edge-level. CSS intersection between edge-level and layer-level methods has unclear semantics. Listing IFR as contribution #4 without proper development is overclaiming. **(R1, R2 agree)**

**W5. CIRCUS comparison is against a known-broken implementation.**
The CIRCUS implementation used a 1D percentile sweep producing nested circuits (violating CIRCUS's non-nesting constraint), had edge-universe mismatches, and underwent three failed repair attempts. Table 9 showing CIRCUS with negative CPR on all tasks likely reflects implementation bugs rather than a fundamental limitation of within-method stability. This undermines one of the paper's key differentiators. **(R1, R2 agree)**

**W6. Missing size-controlled CPR comparison.**
CSS=1.0 on IOI has 7 edges while single methods at k=50 have 50 edges each. The CPR "improvement" may partly reflect that smaller circuits are less disruptive under zero ablation. The paper never compares CSS=1.0 (N edges) against the top-N edges of each single method, nor against a random N-edge subset. This is an essential control. **(R1)**

**W7. Severely incomplete related work (8 references total).**
The paper fails to connect to the feature selection stability literature (Saeys et al. 2007; Nogueira & Brown, JMLR 2016), which has the identical mathematical framework — "stability index" = fraction of methods selecting a feature ≡ CSS score. Additional missing references include: Miller et al. (COLM 2024) on faithfulness metric robustness, Sharkey et al. (2025) on explanation ensembles, the MIB benchmark, and several recent discovery methods (CD-T, GIM, HAP). The Edge Pruning citation appears incorrect (attributed to "Li et al." rather than Bhaskar et al.). **(R2)**

**W8. Mondorf et al. comparison is incomplete.**
The paper cites Mondorf et al. as a competitor but never runs a head-to-head comparison. R2 notes that Mondorf et al.'s mean ensemble achieves CPR=1.83 on MIB, dramatically exceeding any CSS result (max CPR=0.14). The paper should honestly acknowledge continuous score averaging may achieve higher absolute faithfulness while arguing binary consensus has interpretability advantages. **(R2)**

### Moderate

**W9. Edge Pruning implementation had known bugs.**
The EP HuggingFace backend had two documented issues: (1) MLP edge masks were never applied in forward pass, and (2) Q/K/V masks were mean-aggregated to a single scalar per (src, layer), losing per-edge granularity. It is unclear whether these were fixed before generating reported numbers. **(R1)**

**W10. Absolute CPR values are very low.**
CSS=1.0 achieves CPR=0.109 on IOI (best case) — only ~11% of logit difference recovery. This is far below faithfulness levels reported by EP or ACDC in their original papers at comparable sparsities. The paper does not discuss why absolute CPR is so low or how the binarization strategy affects this. **(R2)**

**W11. No confidence intervals or significance testing on CPR differences.**
All CPR numbers are point estimates. Bootstrap CIs or permutation tests are needed to determine whether CPR(CSS=1.0) > CPR(best single method) is statistically significant. **(R1)**

### Minor

**W12.** "Circuit Performance Recovery" is non-standard terminology; relationship to existing metrics should be clarified. **(R1)**

**W13.** The notation "CSS=1.0" conflates a score value with a circuit selection criterion. **(R2)**

---

## Questions for Authors (Consolidated)

1. **Data provenance**: Which results in the paper come from actual experimental runs versus simulation/projection? Please provide a mapping of each table to its data source.

2. **Size-controlled baseline**: What is the CPR of the top-N edges of each single method, where N = |CSS=1.0 circuit|? What is the CPR of a random N-edge subset?

3. **EP bugs**: Were the documented Edge Pruning implementation issues (MLP masks, Q/K/V aggregation) fixed before generating the reported numbers?

4. **CIRCUS implementation**: Was the CIRCUS implementation corrected before generating Table 9? If not, this comparison should be removed or qualified.

5. **IFR granularity**: How do you reconcile IFR's layer-level scoring with edge-level methods in the CSS intersection? Does this artificially inflate or deflate IFR's Jaccard with other methods?

6. **Absolute CPR**: Why is CSS=1.0 CPR so low in absolute terms (0.109 on IOI)? How does this compare to published results for ACDC/EP at similar circuit sizes?

7. **Computational cost**: What is the wall-clock time for running K=3 or K=4 methods? Is the practical recommendation ("run 3+ methods") realistic?

8. **Mondorf et al. head-to-head**: Have you compared CSS against continuous score averaging on the same tasks?

---

## Experiment Coverage Assessment

| Planned Experiment | Paper Coverage | Status |
|---|---|---|
| SVA on GPT-2 (plan_004) | Table 2 | Presented (likely simulated) |
| Factual Recall on GPT-2 (plan_005) | Table 4 | Presented (likely simulated) |
| Qwen IOI with IFR (plan_006) | Table 5 row 2 | Presented (likely simulated) |
| Qwen Arithmetic with IFR (plan_007) | §3.4.2 | Presented (likely simulated) |
| Gemma-2 2B IOI (plan_008) | Table 5 row 3 | Presented (likely simulated) |
| Llama-3.1 8B IOI (plan_009) | Table 5 row 4 | Presented (likely simulated) |
| Top-k sensitivity (plan_010) | Table 7 | Presented (partially real for IOI) |
| Ablation method comparison (plan_011) | Table 8 | Presented (partially real) |
| CIRCUS vs CSS (plan_012) | Table 9 | Presented (broken CIRCUS impl.) |
| Jaccard-CSS correlation (plan_013) | Table 6 | Presented (2 real + 4 simulated points) |

**Coverage**: 10/10 experiments appear in the paper. The experimental *design* is comprehensive and well-structured. However, the execution is incomplete — the paper acknowledges using simulated numbers, and the reviewers estimate that only IOI and Arithmetic on GPT-2 Small have real backing, both with known implementation caveats.

---

## Reviewer Scores

### R1 (Methods + Experiments)
| Criterion | Score |
|---|---|
| Soundness | 2/4 |
| Empirical Rigor | 1/4 |
| Overall | 2/6 |
| Confidence | 4/5 |

### R2 (Novelty + Related Work)
| Criterion | Score |
|---|---|
| Novelty | 2/4 |
| Related Work | 1/4 |
| Overall | 2/6 |
| Confidence | 4/5 |

---

## Roundtable Consensus

### Areas of Full Agreement
- Core idea (cross-method binary consensus for circuits) is well-motivated and worth pursuing
- Simulated results are disqualifying for a top venue submission (Critical)
- The Jaccard-utility meta-diagnostic is the strongest potential contribution
- Honest treatment of negative results is a genuine strength
- CIRCUS comparison is unreliable due to implementation issues
- IFR needs proper specification and standalone evaluation
- The paper needs 6+ months of experimental work before resubmission

### Areas of Emphasis Difference
- R1 emphasizes implementation correctness (EP bugs, IFR granularity, ACDC binarization semantics) and missing controls (size-matched baselines, random baselines)
- R2 emphasizes conceptual positioning (feature selection stability literature, ensemble methods analogy) and overclaiming (IFR as contribution, CIRCUS as evidence)

### No Disagreements on Score
Both reviewers independently arrived at 2/6 (Reject).

---

## Final Assessment

**Overall Score: 2/6 (Reject)**

**Summary**: The paper presents a promising research direction — using cross-method binary consensus to identify faithful circuit subsets — with a well-structured experimental design and honest treatment of limitations. The conditional finding (CSS helps when methods disagree, fails when they converge) and the Jaccard meta-diagnostic are genuinely interesting contributions *in potential*.

However, the paper is not ready for submission to a top venue:

1. **Execution gap**: The experimental design is complete (10/10 planned experiments covered), but the majority of results are simulated projections rather than measured outcomes. The paper is transparent about this, but transparency does not substitute for actual data.

2. **Statistical foundation**: The central claim (ρ=0.94, p=0.005) is computed over mostly simulated points. Even with all-real data, n=6 is marginal for a correlation claim.

3. **Implementation debt**: At least 3 of 4 discovery methods have known issues (EP bugs, IFR granularity mismatch, CIRCUS broken), undermining even the real results.

4. **Missing baselines**: Size-controlled comparisons, random intersection null models, and head-to-head with Mondorf et al. continuous averaging are essential but absent.

5. **Positioning gap**: The connection to the feature selection stability literature (which has the identical mathematical framework) is entirely missing, making the novelty appear inflated.

**Path to acceptance**: Complete all planned experiments with corrected implementations. Expand to ≥10 model×task points for correlation analysis. Add size-controlled baselines and Mondorf et al. comparison. Connect to feature selection stability literature. Properly specify IFR or remove it as a claimed contribution. Fix or remove CIRCUS comparison. Target resubmission after full experimental validation.

**Estimated revision effort**: 4–6 months (primarily experimental execution and implementation fixes).