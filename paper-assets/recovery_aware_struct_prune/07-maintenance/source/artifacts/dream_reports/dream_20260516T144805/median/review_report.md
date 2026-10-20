---
dream_id: dream_20260516T144805
tier: median
overall_score: Weak Reject (3/6)
timestamp: 2026-05-16T15:40:35.192879+00:00
---

# Dream Review Report

**Paper:** "GRPO Alignment Fails on Structurally Pruned Reasoning Models: Reward Hacking, Training Collapse, and the Redundancy-Stability Tradeoff"

**Review Mode:** Full (2-Reviewer Roundtable)

---

## Roundtable Summary

### Step 1: Independent Reviews

**R1 (Methods + Experiments) — Score: 4/6 (Weak Accept)**
- Methodological Soundness: 6/10
- Experimental Rigor: 6/10
- Reproducibility: 7/10
- Claim-Evidence Alignment: 5/10

**R2 (Novelty + Related Work) — Score: 3/6 (Weak Reject)**
- Novelty: 5/10
- Significance/Impact: 5/10
- Related Work Completeness: 6/10
- Positioning and Framing: 5/10
- Writing Quality: 7/10

### Step 2: Cross-Sharing — Areas of Agreement

Both reviewers converge on the following assessments:

1. **Finding 2 (collapse severity gradient) is the paper's most novel and strongest contribution.** The four-method ordering (RASP step ~10, GRASPrune ~18, Bonsai ~28, Standard ~60) plus the unstructured control (no collapse) is a clean result that has not appeared in prior work.

2. **Greedy-only evaluation is a critical gap.** GRPO optimizes sampling diversity, not the greedy mode. The "reward-accuracy decoupling" (Finding 1) could simply reflect that greedy accuracy was already at its ceiling while GRPO improved pass@k. Without pass@k evaluation (k=8, 64), the paper's strongest claim — that GRPO "universally fails" — is not adequately supported. Both reviewers flag this as the single largest threat to validity.

3. **Cross-model replication is weak.** On Qwen2.5-Math-7B, the RASP/Standard collapse ratio is 1.5–1.75× with 95% CIs [0.8, 2.8] and [0.9, 3.1], both including 1. The severity gradient — the paper's most novel finding — does not significantly replicate on the second model. The paper acknowledges this honestly ("diagnostic tendency ... not statistically significant replication"), which both reviewers appreciate.

4. **The SFT gap is not statistically significant at the primary sparsity level.** At 20%, RASP vs Standard is +2.2pp (p = 0.25). At 25% it is +3.2pp (p = 0.089). Neither reaches conventional significance. Finding 3 (Redundancy-Stability Tradeoff) rests on this SFT advantage as one side of the tradeoff, making the evidence asymmetric: the GRPO collapse side is strong, the SFT side is marginal.

5. **The structured vs. unstructured contrast is excellent.** At matched 20% sparsity, structured pruning collapses (step ~10–60) while unstructured pruning trains stably for 100 steps. This cleanly isolates structural integrity as the mechanism and is the paper's most convincing control experiment.

6. **RASP is technically simple but well-motivated as a diagnostic tool.** S(h) = I(h) × (1−F(h))^α is a straightforward weighted product of importance and CKA-based redundancy. The U-shaped alpha ablation (Table 4) confirms the parameter is meaningful. Both reviewers agree RASP's value is primarily diagnostic rather than as a superior pruning method.

### Step 3: Cross-Sharing — Areas of Divergence

1. **Publishability threshold.** R1 views the negative result (GRPO collapse) and diagnostic framework as sufficient for a venue like EMNLP with claim downscoping. R2 considers the greedy-only eval gap and single GRPO configuration as potentially fatal weaknesses that could invalidate the central claim.

2. **Severity of the "universal" overclaim.** R1 flags that "universal" is tested on one task (GSM8K), one eval protocol (greedy), and 100 GRPO steps, but considers this addressable by narrowing the claim language. R2 argues more strongly that without pass@k, the decoupling claim may be an artifact rather than a finding, which would undermine the paper's raison d'être.

3. **GRPO configuration concern.** R2 raises that only one GRPO configuration is tested (KL coefficient 0.04, lr 5e-7, 100 steps) and that Self-Healing uses different hyperparameters. R1 notes the issue but is less concerned since the collapse pattern holds across multiple pruning methods.

**Resolution:** Both reviewers agree that the structural damage finding (Finding 2) and the structured-vs-unstructured control are genuine contributions regardless of the greedy/pass@k question. The disagreement centers on whether Finding 1 (universal decoupling) is real or an evaluation artifact. This is resolvable: pass@k evaluation would either confirm or refute it.

### Step 4: Consolidated Assessment

---

## Strengths

**S1 (Major): Novel identification of GRPO training collapse on structurally pruned models.**
No prior work has documented this phenomenon. The collapse definition (frac_zero_std > 0.85, grad_norm < 0.01, persisting ≥5 steps) is crisp and the severity gradient across four structured pruning methods is clean. This is a genuine contribution to the pruning-alignment interaction literature.

**S2 (Major): The structured vs. unstructured control experiment.**
At identical 20% sparsity, structured pruning (RASP: 29.8% post-prune) collapses at step ~10 while unstructured pruning (68.2% post-prune) trains stably for 100 steps with reward reaching 0.548. The qualitative difference (collapse vs. stability) cannot be fully explained by the accuracy gap alone and points to structural integrity as a mechanism. This is the paper's most convincing result.

**S3 (Major): Comprehensive experimental matrix.**
The paper evaluates 5 pruning methods (RASP, Standard, GRASPrune, Bonsai, Unstructured) × 3 recovery paradigms (post-prune, SFT, GRPO) × 2–3 sparsity levels, with cross-model validation, OOD evaluation (MATH-500, HumanEval, MMLU), scoring ablation, alpha sensitivity, CKA reliability analysis, and inference speedup benchmarks. For a 9-page paper, the experimental breadth is impressive.

**S4 (Moderate): Honest and calibrated claim language.**
The Discussion section transparently acknowledges: (i) cross-model replication is weak, (ii) the SFT gap is not significant at 20%, (iii) the Redundancy-Stability Tradeoff is an "empirical observation on the DeepSeek-R1 family," not a universal law. This self-awareness is commendable and appropriate.

**S5 (Moderate): The U-shaped alpha ablation (Table 4).**
The minimum at α = 0.5 and optimum at α = 2.0 for both post-prune and post-SFT accuracy confirms the CKA penalty is a meaningful (not arbitrary) parameter and reveals the "noise injection" regime where weak CKA signal disrupts importance ranking.

**S6 (Minor): Practical recommendations are clearly stated.**
The paper offers actionable advice: (1) SFT-only recovery is currently the safe path, (2) structured pruning beyond 25% is impractical for 7B reasoning models, (3) if RLVR is required downstream, unstructured pruning preserves structural integrity.

---

## Weaknesses

**W1 (Critical): Greedy-only evaluation may invalidate Finding 1.**
The paper evaluates exclusively with greedy decoding. GRPO is designed to improve the distribution of outputs, not the mode. The identical 1072/1319 correct answers before and after GRPO on the unpruned model could simply mean the greedy mode was already optimal while GRPO improved sampling diversity (pass@k). If pass@8 or pass@64 shows improvement, the "reward-accuracy decoupling is universal" claim collapses. This is acknowledged nowhere in the paper. **The paper must either report pass@k or explicitly scope the claim to greedy evaluation.**

**W2 (Major): Single GRPO configuration tested.**
The paper uses one GRPO setup: lr 5e-7, KL coefficient 0.04, group size 8, 100 steps. Self-Healing (Chen et al. 2025) uses different hyperparameters. The paper does not show that collapse persists across varying learning rates, KL penalties (especially β > 0), temperature, or training duration. Standard pruning shows transient collapse at step ~60 with "partial recovery" (Table 3 footnote) — does collapse persist to step 200? 500? This undermines the "fundamental" framing of the collapse phenomenon.

**W3 (Major): Cross-model replication does not reach significance.**
On Qwen2.5-Math-7B, the RASP/Standard collapse ratio is 1.5–1.75× with 95% CIs including 1 (Table 5). Both models collapse (supporting Finding 1), but the severity gradient (Finding 2) does not replicate. The paper correctly acknowledges this as a "diagnostic tendency" rather than a universal law, but the abstract and introduction still use "universal" language ("universally fails").

**W4 (Major): SFT advantage underlying Finding 3 is not significant.**
The RASP vs. Standard SFT gap is +2.2pp (p = 0.25) at 20% and +3.2pp (p = 0.089) at 25%. Neither reaches conventional significance. The Redundancy-Stability Tradeoff concept requires both sides to hold: RASP advantages under SFT AND RASP disadvantages under GRPO. The GRPO side is well-supported; the SFT side is a consistent trend that does not reach significance in the primary evaluation.

**W5 (Major): Confound between accuracy level and structural integrity.**
The unstructured control starts at 68.2% post-prune vs. 29.8% (RASP) or 26.1% (Standard) for structured methods. The paper argues the qualitative collapse-vs-stability difference points to structural integrity, not accuracy level, as the mechanism. But this is not cleanly disentangled. A stronger control would be structured pruning at a lower sparsity that matches unstructured's starting accuracy, or unstructured pruning at a higher sparsity that matches structured's starting accuracy.

**W6 (Moderate): Single seed for most experiments.**
Multi-seed results appear only for post-prune evaluation (5 seeds, Appendix A). All SFT, GRPO, cross-model, and OOD experiments are single-seed. For stochastic training processes like GRPO, single-seed collapse step estimates may not be reliable. The collapse step ~10 vs ~60 difference is large enough that it is unlikely a seed artifact, but the GRASPrune (~18) and Bonsai (~28) positions in the gradient are less certain without replication.

**W7 (Moderate): No mechanistic explanation for collapse.**
The paper observes that redundancy removal correlates with collapse speed but does not explain the mechanism. Why does removing entire attention heads or MLP groups eliminate exploration capacity while zeroing individual weights does not? The "exploration topology" hypothesis is stated but not validated through, e.g., representation geometry analysis, gradient flow decomposition, or policy entropy dynamics during training.

**W8 (Minor): Limited reference list.**
13 references is thin for a paper making broad claims about pruning-alignment interaction at a top venue. Notable omissions: Davari et al. (ICLR 2023) on CKA reliability/limitations (directly relevant to the core technical component), plasticity loss literature in RL (Dohare, Nature 2024; Lyle et al., ICML 2024), and the "From LLMs to LRMs" line of work on width vs. depth pruning for reasoning models.

**W9 (Minor): Bonsai and GRASPrune results appear in a limited capacity.**
Bonsai appears only in the main tables and a brief appendix paragraph. GRASPrune has limited pipeline coverage. For these to serve as convincing data points in the severity gradient, more detail (training curves, multi-seed, hyperparameter choices) would strengthen the claim.

---

## Questions for Authors

**Q1:** Have you evaluated pass@k (k = 8, 64) for the unpruned model before and after GRPO? If GRPO improves pass@8 from, say, 85% to 92% while greedy stays at 81.27%, the "reward-accuracy decoupling" claim needs fundamental revision.

**Q2:** What happens if you run GRPO for 200–500 steps on Standard-pruned models? Table 3 notes "partial recovery" at step ~60. Does this recovery stabilize, or does the model re-collapse?

**Q3:** Have you tested GRPO with different KL coefficients (β ∈ {0.01, 0.1, 0.5})? A stronger KL anchor to the SFT reference policy might prevent collapse while still providing alignment benefits.

**Q4:** To disentangle accuracy level from structural integrity: what happens if you run unstructured pruning at 40–50% sparsity to match the ~30% post-prune accuracy of structured pruning? Does GRPO still train stably?

**Q5:** The CKA-recoverability analysis (Table 10) shows within-layer variance explained is only 8% (ICC = 0.71, layer dominates). Given that RASP and Standard make similar layer-level allocation decisions, is RASP's differentiation from Standard almost entirely driven by within-layer structure selection? If so, the 8% explanatory power suggests RASP's CKA signal is near-negligible at the relevant granularity.

**Q6:** For the Qwen-Math cross-model experiments: the collapse ratios are 1.5–1.75× with CIs including 1. Do you view Finding 2 as model-specific to DeepSeek-R1-Distill, or do you maintain it generalizes?

---

## Experiment Coverage Assessment

Comparing against the review_context.yaml (18 imagined experiments):

| Experiment | Status | Notes |
|---|---|---|
| plan_001 (Post-prune N=1319) | ✅ Covered | Table 1 |
| plan_004 (All recovered models) | ✅ Covered | Table 2 |
| plan_005 (GRASPrune pipeline) | ✅ Covered | Tables 2, 3 |
| plan_006 (Multi-seed 5 seeds) | ✅ Covered | Table 1, Appendix A |
| plan_007 (Scoring ablation) | ✅ Covered | Table 6 |
| plan_008 (CKA-recoverability) | ✅ Covered | Table 10 |
| plan_009 (SFT-only recovery) | ✅ Covered | Table 2 |
| plan_010 (25% sparsity) | ✅ Covered | Tables 1–3 |
| plan_011 (30% probe) | ✅ Covered | Table 1 |
| plan_012 (Extended eval) | ✅ Covered | Table 8 |
| plan_013 (Bonsai baseline) | ✅ Covered | Tables 2, 3, Appendix B |
| plan_014 (CKA reliability) | ✅ Covered | Table 9 |
| plan_015 (Alpha ablation) | ✅ Covered | Table 4 |
| plan_016 (Inference speedup) | ✅ Covered | Table 7 |
| plan_017 (Unstructured baseline) | ✅ Covered | Tables 2, 3 |
| plan_018 (SFT OOD) | ✅ Covered | Table 8 |
| scope_qwen_math_grpo_20 | ✅ Covered | Table 5 |
| scope_qwen_math_grpo_25 | ✅ Covered | Table 5 |

**Coverage: 18/18 (100%).** All imagined experiments are reflected in the paper. The experimental breadth is commendable.

---

## Consolidated Scores

| Dimension | R1 | R2 | Consolidated |
|---|---|---|---|
| Methodological Soundness | 6/10 | — | 6/10 |
| Experimental Rigor | 6/10 | — | 6/10 |
| Reproducibility | 7/10 | — | 7/10 |
| Claim-Evidence Alignment | 5/10 | — | 5/10 |
| Novelty | — | 5/10 | 5/10 |
| Significance/Impact | — | 5/10 | 5/10 |
| Related Work | — | 6/10 | 6/10 |
| Positioning/Framing | — | 5/10 | 6/10 |
| Writing Quality | — | 7/10 | 7/10 |

---

## Overall Score: 3 — Weak Reject

**Confidence: 4/5 (high)**

### Justification

The paper identifies a genuinely interesting and previously undocumented phenomenon: GRPO training collapse on structurally pruned reasoning models. The severity gradient across four pruning methods and the structured-vs-unstructured control constitute a real empirical contribution. The Redundancy-Stability Tradeoff is a useful conceptual frame. The experimental matrix is impressively comprehensive for a 9-page paper (5 methods × 3 recovery paths × 2–3 sparsity levels, plus cross-model, OOD, and ablation studies).

However, three critical issues prevent acceptance:

1. **The "universal failure" claim (Finding 1) rests on greedy-only evaluation.** GRPO is designed to improve sampling diversity, and the paper does not test pass@k. The identical 1072/1319 correct answers could reflect greedy-mode saturation rather than alignment failure. This is the paper's headline claim and its evidence base has a fundamental gap.

2. **The cross-model evidence undermines generalization.** The severity gradient — the most novel finding — does not significantly replicate on Qwen-Math-7B (CIs include 1). The paper honestly acknowledges this, but the abstract and title still use language ("universally fails") that overpromises relative to the evidence.

3. **The SFT side of the Redundancy-Stability Tradeoff is not significant.** At the primary sparsity (20%), p = 0.25. Finding 3 is therefore asymmetric: the collapse side is strong, the SFT advantage side is a directional trend.

### Path to Acceptance

This paper could reach acceptance at a top venue (EMNLP Main, NeurIPS) with:
- **pass@k evaluation** for the unpruned and key pruned configurations (resolves W1)
- **GRPO hyperparameter sensitivity** (at minimum, varying KL coefficient and training length) (resolves W2)
- Narrowing "universal" to "observed across all tested structured pruning methods on GSM8K with greedy evaluation" (resolves W3)
- Ideally, one additional model family (e.g., Llama-based) for cross-model evidence
- Multi-seed replication of at least the primary GRPO collapse results

The core finding — that structural pruning causes GRPO collapse while unstructured pruning does not — is valuable and, if confirmed with pass@k, would represent an important warning for the pruning-alignment community.