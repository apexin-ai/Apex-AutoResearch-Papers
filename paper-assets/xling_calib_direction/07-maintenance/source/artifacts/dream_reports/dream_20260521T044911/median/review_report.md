---
dream_id: dream_20260521T044911
tier: median
overall_score: Findings (Overall 3/5)
timestamp: 2026-05-21T06:05:50.784279+00:00
---

# Dream Review Report — "When Does Cross-Lingual Calibration Transfer Work?"

**Review Mode**: Full (2 Reviewers + Roundtable)
**Venue Standard**: ACL ARR 1–5 scale
**Date**: 2026-05-21

---

## Reviewer Assignment

| Reviewer | Focus | Confidence |
|----------|-------|------------|
| R1 | Methods + Experiments | 4/5 |
| R2 | Novelty + Related Work | 4/5 |

---

## 1. Paper Summary

This paper presents the first large-scale study of cross-lingual correctness probe transfer. English logistic regression probes are trained on hidden-state activations from two MoE architectures (Qwen3-235B-A22B, Llama 4 Scout 17B-16E) and evaluated on zero-shot transfer to 20 languages across three resource tiers (HIGH/MID/LOW) using five transfer strategies: zero-shot, mean-shift, CaCLR (MMD consistency loss), linear projection (Procrustes), and few-shot fine-tuning. Camera-ready extensions add Gemma 4 31B Dense and 52 languages.

Three practical findings and one systematic negative result emerge: (1) linear projection with ~70 parallel pairs reaches 95% of max transfer improvement; (2) Procrustes alignment reverses its effect at a ZS AUROC threshold of ~0.55; (3) ~30% of low-resource language–layer probing results are capacity artifacts; (4) CaCLR's MMD consistency loss is inert (ΔAUROC = +0.002, p = 0.42), with a geometric explanation via CKA subspace analysis. Supporting analyses include an architecture-dependent depth–transferability Pareto frontier, a Simpson's Paradox in the CKA–transfer correlation, cross-lingual orthogonality replication, and cross-benchmark generalization.

---

## 2. Consolidated Strengths

**S1. Comprehensive experimental design with strong statistical practices** [R1, R2 agree].
The 13-experiment plan covers core claims, robustness checks (quantization validation, probe complexity comparison), generalization (3 benchmarks, 52 languages), and controls (Hewitt & Liang selectivity). Bootstrap 95% CIs (1,000 resamples), paired permutation tests, and Cohen's d effect sizes are reported throughout — exceeding the field norm where most comparable papers report point estimates without CIs. The progression from pilot validation to full-scale execution is methodologically sound.

**S2. Simpson's Paradox analysis is the methodological highlight** [R1, R2 agree].
The sign reversal from raw negative Spearman correlation (Qwen3: ρ = −0.22, p < 0.001; Llama4: ρ = −0.28, p < 0.001) to positive partial correlation after controlling for depth (Llama4: ρ = +0.29, p = 0.018; Qwen3: ρ = +0.16, p = 0.072) is correctly executed and provides genuine explanatory value. The per-layer within-depth-bin analysis provides independent non-parametric corroboration. This directly addresses the "CKA is just a depth proxy" concern that would otherwise undermine the geometric narrative.

**S3. Probing control tasks are a field-level methodological contribution** [R1, R2 agree].
First application of Hewitt & Liang (2019) selectivity analysis to cross-lingual probing. The finding that ~30% of LOW-resource and ~28% of MID-resource language–layer combinations fall below the 0.05 selectivity threshold (Table 14) is directly useful. The paper identifies yo (selectivity = 0.032) and am (selectivity = 0.018) as artifacts at L80 (Table 15), cross-validates with the orthogonality outliers, and re-verifies main results after filtering. This should influence methodological standards for all cross-lingual probing work.

**S4. CaCLR negative result is systematic and well-explained** [R1].
The β sweep across three orders of magnitude (0.001–1.0), component ablation (Table 8), and CKA subspace analysis (Table 9 showing MMD reduces marginal distance but leaves subspace angles unchanged) constitute a thorough closure of the 1-D distributional matching path. The connection to Zhao et al. (2019) conditional-marginal mismatch theory is well-articulated.

**S5. Practical guidance is specific and actionable** [R1, R2 agree].
The paper provides concrete, deployable recommendations: test ZS AUROC first; below 0.55, use linear projection with ~70 pairs; above 0.62, use zero-shot directly. Resource-tier stratified saturation curves (Table 11: HIGH saturates at ~35 pairs, LOW at ~75) add granularity. The Procrustes reversal threshold with 95% CI ([0.46, 0.63]) allows practitioners to assess uncertainty.

**S6. Paper fills a genuine gap** [R2].
The entire probe-based calibration literature (CORAL, Miao & Ungar steering, Confidence Manifold) is English-only. The distinction from Xiao et al.'s knowledge-boundary probes (input-level answerability vs. output-dependent correctness) is clearly articulated. The scale advantage (20 languages, 2–3 architectures, 5 methods vs. Xiao et al.'s 8 languages, 1 method) is substantial.

**S7. Mean-shift invariance proof is clean** [R1].
The mathematical argument that StandardScaler + logistic regression makes mean-shift ΔAUROC ≡ 0 is correct and clearly differentiates from Xiao et al.'s pipeline. Verified empirically.

---

## 3. Consolidated Weaknesses

### Major

**W1. CaCLR negative result should be scoped more precisely to 1-D marginal matching** [R1].
CaCLR's MMD operates on scalar probe logits (z ∈ ℝ¹). In 1-D, Gaussian RBF MMD essentially matches a single scalar's marginal distribution. The paper draws the strong conclusion that "distributional matching fails for correctness probe transfer" and uses this to validate Zhao et al.'s theory. However, this conclusion is specific to 1-D marginal matching — MMD on the full hidden-state space or on a low-rank projection could yield different results. The negative result should be explicitly scoped: "1-D logit-level distributional matching fails" rather than implying distributional matching as a class is ineffective. This affects the abstract, §4.4, and the Discussion.

**W2. Procrustes train/eval contamination risk** [R1].
The linear projection evaluation appears to sample parallel pairs from the same pool used for AUROC evaluation. With 200 pairs out of ~4,200 eval samples (~5%), bias may be small, but it is methodologically incorrect. Tables 11 and 12 are both potentially affected. The paper should either restrict Procrustes pairs to the train split exclusively or quantify contamination bias via leave-pair-out analysis.

**W3. Architecture-dependent conclusions are underpowered** [R2].
The claim that the Pareto frontier is "architecture-dependent" (Contribution 1 in abstract and introduction) rests on n = 2 core architectures (n = 3 with camera-ready Gemma 4) that differ simultaneously in type (MoE vs. dense), scale, layer count, quantization, and training data. No specific architectural feature can be isolated. The paper acknowledges this in Limitations but presents architecture dependence as a headline finding. The framing should be more cautious: "we observe architecture-correlated differences" rather than implying a general architectural principle.

**W4. Single random seed throughout** [R1].
All experiments use seed = 42. Given modest effect sizes (CaCLR: +0.002; linear projection at 50 pairs: +0.027; few-shot 25: +0.018), variance across seeds could be comparable to reported effects. Few-shot evaluation with k = 25 is particularly sensitive to the specific sample drawn. Multi-seed variance estimates (3–5 seeds) are needed for key results, especially few-shot and low-pair-count Procrustes.

**W5. CaCLR hyperparameter selection criterion is English-only** [R1].
The β sweep selects the best configuration by English validation performance. If the consistency loss improves cross-lingual transfer at the expense of English performance, the English-only criterion would systematically select against it. This structural bias toward low β values potentially undermines the negative result claim. A mixed criterion incorporating at least one validation language would strengthen the conclusion.

### Minor–Moderate

**W6. Missing related work** [R2].
Several relevant papers are absent from the bibliography:
- Burns et al. (2023) CCS: trains probes via consistency constraints across contrasting inputs without supervision — structurally analogous to CaCLR's consistency regularization idea.
- Kadavath et al. (2022): foundational work on model self-knowledge and calibration, directly motivating correctness probing.
- Wendler et al. (2024): studies language-specific vs. shared processing in multilingual LLMs, directly relevant to the claim that correctness occupies a language-agnostic subspace.
The bibliography has only 15 entries for a paper of this scope, which is thin for a *CL venue.

**W7. Correctness vs. knowledge-boundary distinction is not empirically validated** [R2].
The distinction between correctness probing (output-dependent) and knowledge-boundary probing (input-level answerability, Xiao et al.) is central to the novelty claim but purely definitional. The paper never demonstrates that these signals behave differently — e.g., different Pareto shapes or CKA relationships. An empirical comparison would make the distinction load-bearing.

**W8. Difficulty decomposition is methodologically weak** [R1].
The difficulty probe R² = 0.35 means 65% of difficulty variance is unexplained, so "projecting out difficulty" leaves substantial difficulty signal in the residual. Prescriptive accuracy of 58% is barely above chance (50%), undermining practical value. The random-direction control shows ~40% of the effect comes from pure dimensionality reduction. The IRT difficulty score source is unspecified — if from model accuracy, circularity arises. This section should be further weakened or its limitations more explicitly acknowledged.

**W9. Potential CKA–transfer tautology** [R1, R2].
Both linear CKA and linear probe AUROC measure linear alignment between English and target representations. A positive partial correlation between them may partly reflect measurement overlap rather than genuinely independent geometric structure. The subspace angle analysis partially addresses this, but the point deserves more than a single sentence.

**W10. Simpson's Paradox label may overclaim** [R2].
Simpson's Paradox typically involves subgroup reversal with causal implications. The finding here is a confounded correlation that reverses sign under depth control — real and valuable, but more accurately described as "confound-reversal." The branded label (used in abstract, introduction, 3+ section headings, conclusion) creates tension with the paper's own caveat that the analysis is "geometric and correlational, not mechanistic."

---

## 4. Questions for Authors

1. **Procrustes contamination**: Can you confirm that Tables 11–12 use Procrustes pairs exclusively from the train split, with evaluation only on the held-out eval split?

2. **CaCLR in higher dimensions**: Have you tried MMD on hidden-state activations directly (before the probe) or on a PCA-reduced intermediate space? The 1-D logit constraint seems artificially restrictive for the distributional matching hypothesis.

3. **Multi-seed variance**: What is the standard deviation of CaCLR AUROC and linear projection AUROC across 3–5 random seeds? Is the +0.002 CaCLR effect within seed-to-seed noise?

4. **IRT difficulty source**: Where do the item-level difficulty scores for the decomposition (Table 13) come from? If estimated from model accuracy, how is circularity addressed?

5. **Correctness vs. answerability**: Have you measured whether Xiao et al.'s knowledge-boundary probes show the same Pareto frontier and Simpson's Paradox? An empirical comparison would substantially strengthen the claimed distinction.

6. **CKA tautology**: If you compute CKA on a held-out subset of examples disjoint from the AUROC evaluation set, does the partial correlation hold? This would address the measurement overlap concern.

7. **Selectivity threshold sensitivity**: How sensitive are the artifact rates (Table 14) to the selectivity threshold? What are the rates at 0.03 and 0.10?

---

## 5. Experiment Coverage Assessment

All 13 planned experiments from the design document are covered in the paper:

| Plan | Description | Coverage |
|------|-------------|----------|
| 001 | Full Pareto — Qwen3-235B | §4.2 ✓ |
| 002 | Full Pareto — Llama 4 Scout | §4.2 ✓ |
| 003 | CaCLR + Negative Result | §4.4 ✓ |
| 004 | Difficulty Decomposition | §4.7 ✓ |
| 005 | Cross-Lingual Orthogonality | §4.9.1 ✓ |
| 006 | LR vs MLP | §4.9.2 ✓ |
| 007 | Belebele + MMLU-ProX | §4.9.3 ✓ |
| 008 | Gemma 4 31B Dense | §4.10 ✓ (camera-ready) |
| 009 | 52 Languages | §4.10 ✓ (camera-ready) |
| 010 | Quantization Validation | §4.9.4 ✓ |
| 011 | CKA + Simpson's Paradox | §4.3 ✓ |
| 012 | Linear Projection Sensitivity | §4.6 ✓ |
| 013 | Probing Control Tasks | §4.8 ✓ |

Full coverage. No planned experiments are missing from the paper.

---

## 6. Roundtable Consensus

### Step 2 — Cross-Sharing Summary

R1 raised precise methodological concerns: Procrustes train/eval contamination, CaCLR English-only selection bias, 1-D MMD scope limitation, single-seed variance, and difficulty decomposition weakness. R2 raised positioning concerns: missing citations (Burns CCS, Kadavath, Wendler), unvalidated correctness vs. answerability distinction, overclaimed architecture dependence, and the Simpson's Paradox naming issue.

### Step 3 — Convergence

Both reviewers independently converged on identical scores (Soundness 3.5, Excitement 3, Overall 3) and agreed on the same core assessment: the paper fills a genuine gap with thorough experimentation and strong statistical practices, but limited method novelty, underpowered architectural claims, and several addressable methodological concerns place it at the Findings level. The Simpson's Paradox analysis and control-task artifact warning are the strongest contributions; the difficulty decomposition is the weakest.

R1's concern about 1-D MMD scope (W1) and R2's concern about CaCLR novelty are complementary — together they suggest the CaCLR contribution is correctly framed as a negative result but needs tighter scoping. R1's Procrustes contamination concern (W2) was not raised by R2 but is accepted as valid. R2's missing related work concern (W6) was not raised by R1 but is accepted as valid. No disagreements required resolution.

---

## 7. Final Scores

| Dimension | R1 | R2 | Final | Justification |
|-----------|----|----|-------|---------------|
| **Soundness** | 3.5 | 3.5 | **3.5** | Comprehensive design, rigorous statistics. Procrustes contamination, single seed, CaCLR selection bias, and difficulty decomposition weakness prevent a 4. All addressable in revision. |
| **Excitement** | 3 | 3 | **3** | Simpson's Paradox and control-task findings are interesting. Pareto frontier is largely predicted by domain adaptation theory. Limited method novelty (CaCLR is a negative result, Procrustes is adapted from MUSE/VecMap). Solid empirical characterization, not a source of surprising insights beyond the Simpson's reversal. |
| **Overall** | 3 | 3 | **3** | **Findings-level paper.** Fills a genuine gap, experimental scale is impressive, statistical practices exceed field norms. Core limitations (CaCLR scope, architecture underpowered, missing citations, single seed) are all addressable. With revisions, could reach 3.5 (strong Findings / borderline Conference). |

**Confidence**: 4/5 (both reviewers)

---

## 8. Revision Recommendations (Priority-Ordered)

1. **Scope the CaCLR negative result to 1-D MMD** (W1). Revise abstract, §4.4, and Discussion to state "1-D logit-level distributional matching" rather than implying distributional matching as a class fails. Optionally, run MMD on PCA-reduced activations to test the broader claim.

2. **Fix Procrustes train/eval separation** (W2). Ensure Procrustes pairs are drawn exclusively from the train split. Re-run Tables 11–12 with clean separation.

3. **Add multi-seed variance** (W4). Report standard deviations across 3–5 seeds for CaCLR, linear projection (especially low pair counts), and few-shot 25.

4. **Temper architecture-dependence framing** (W3). Change from "architecture-dependent" to "architecture-correlated" in abstract and introduction. Emphasize observational nature more prominently.

5. **Add missing citations** (W6). Burns et al. (CCS), Kadavath et al., Wendler et al. at minimum. Expand bibliography from 15 to ~20+ entries.

6. **Address CKA tautology** (W9). Add a paragraph in Discussion or §4.3 discussing measurement overlap and why the sign reversal itself is informative beyond it.

7. **Specify IRT difficulty source and acknowledge decomposition limits** (W8). State where difficulty scores come from. Further weaken prescriptive claims given 58% accuracy.
