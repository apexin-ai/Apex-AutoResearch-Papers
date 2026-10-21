---
dream_id: dream_20260515T140651
tier: median
overall_score: 3/6 Weak Reject
timestamp: 2026-05-15T15:04:40.597737+00:00
---

# Consolidated Review Report

**Paper:** Recovery-Aware Structured Pruning: How Pruning Method and Recovery Paradigm Interact in Reasoning Language Models
**Review Mode:** Full (2 Reviewers + Roundtable)
**Consensus Score:** 3/6 (Weak Reject)
**Confidence:** 4/5 (High)

---

## Summary

The paper introduces RASP, which augments standard importance-based structured pruning with a CKA functional overlap term: S(h) = I(h) × (1−F(h))^α. Applied to DeepSeek-R1-Distill-Qwen-7B at 20% structured sparsity, the central finding is a pruning×recovery interaction: GRPO recovery favors RASP (+5pp), SFT recovery favors standard pruning (+7pp), yielding a 12pp crossover (2×2 ANOVA interaction p=0.008, η²=0.12). Secondary contributions include a mixed-effects regression showing CKA as a complementary recoverability predictor (incremental R²=8%), an α ablation showing monotonic improvement up to α=4, and OOD evaluation showing the advantage is specific to mathematical reasoning.

Both reviewers agreed this paper tackles a genuinely novel research question — the coupling between pruning structure selection and recovery paradigm — but found the evidence base insufficient for a top ML venue. The roundtable converged on a score of 3/6 (Weak Reject) with actionable paths to improvement.

---

## Strengths (Consensus)

- **Novel research question.** The observation that the "best" pruning strategy depends on the intended recovery method (SFT vs. GRPO) is a genuinely new finding. No prior work explicitly studies this coupling. The 2×2 factorial design is methodologically appropriate for testing this interaction.

- **Honest, calibrated reporting.** The paper reports the SFT reversal (Standard > RASP by 7pp) rather than cherry-picking only the GRPO-favorable results. Claims are appropriately scoped: Claim 1 uses "moderate advantage," Claim 2 says "additional predictive signal" rather than "superior predictor." The limitations section is unusually thorough (5 explicit limitations).

- **Comprehensive experimental coverage.** The paper covers 13 tables spanning the full pipeline (post-prune, post-SFT, post-GRPO), multi-seed validation, scoring ablation, mixed-effects regression, α sensitivity, sparsity scaling (20/25/30%), OOD evaluation (4 benchmarks), CKA reliability, inference efficiency, and baseline comparisons (GRASPrune, Bonsai, unstructured). This is ambitious scope.

- **Practical relevance.** The α ablation provides actionable guidance (α∈[2,4] recommended), CKA reliability analysis shows 256 samples suffice (8 min compute), and the structured pruning achieves real 1.20× speedup with RASP+GRPO slightly exceeding unstructured+GRPO (64% vs 62%).

- **Mechanistic framing.** Connecting the pruning×recovery interaction to the "RL Squeezes, SFT Expands" framework provides an interpretable mechanism: SFT benefits from high-importance structures for gradient flow, GRPO benefits from functionally unique structures for exploration diversity.

---

## Weaknesses

### Major

**W1. No multi-seed recovery validation (both reviewers).** The headline claims — 5pp GRPO advantage, 12pp interaction — rest on a single GRPO training run per pruning method. GRPO is known to have high variance. The 2×2 ANOVA reports F=8.4, p=0.008, but each cell contains one training run. The denominator degrees of freedom for the F-test must come from test-set bootstrap or similar, which does not account for training variance. If the GRPO run for Standard happened to underperform by 3pp due to training noise, the interaction would collapse. Multi-seed post-prune evaluation (Table 2) is commendable, but it validates only the pruning stage, not the full pipeline. The paper's own limitations acknowledge this (#3), but this is not just a limitation — it undermines the central claim.

**W2. Single model, no architectural validation (both reviewers).** All experiments use DeepSeek-R1-Distill-Qwen-7B. For a claim about the fundamental coupling between pruning and recovery, single-model evidence is insufficient. Distilled reasoning models may have specific redundancy patterns (from the distillation process) that do not generalize to natively-trained models (e.g., QwQ, DeepSeek-R1 full). At minimum, a second model at similar scale (Qwen2.5-7B-Instruct, Llama-3.1-8B) would strengthen the contribution.

**W3. Missing critical related work (R2, confirmed by R1).** Several highly relevant works are absent:
- **FANG (Dec 2025):** Function-aware neuron grouping for structured pruning — the closest conceptual parallel to CKA-based functional identification.
- **PAT (AAAI 2025):** Joint pruning-tuning framework that explicitly co-optimizes pruning and recovery, directly challenging the claim that "no prior work studies pruning-recovery interaction."
- **Davari et al. (ICLR 2023):** CKA reliability limitations — any paper building on CKA should acknowledge its sensitivity to outliers and potential manipulation.
- **RestoreLCC (NeurIPS 2025 Spotlight):** Alternative recovery via activation compensation.
- **Boiling Frog (Feb 2026), P2 Law (ACL 2025):** Directly relevant prune-then-recover and pruning scaling works.

The related work section (4 paragraphs, 10 references) is too thin for a top venue. The claim "no prior work studies pruning-recovery interaction" needs qualification given PAT.

**W4. Scoring formula lacks theoretical justification (both reviewers).** S(h) = I(h) × (1−F(h))^α is a multiplicative heuristic. No argument connects this functional form to any optimization objective or recoverability criterion. The paper does not compare against alternatives: additive (I(h) + β(1−F(h))), other similarity metrics (SVCCA, CCA, mutual information), or weight-norm-based overlap (which outperforms CKA in the regression with 14% vs 8% incremental R²). The lack of ablation over the functional form (only α is swept, not the formula structure) weakens the methodological contribution.

### Moderate

**W5. CKA is the weakest predictor in its own regression (both reviewers).** Table 5 shows weight norm (β=0.31, incr. R²=14%) and gradient importance (β=0.22, incr. R²=11%) both individually outperform CKA F(h) (β=0.18, incr. R²=8%). The paper honestly positions CKA as "complementary," but this raises a natural question: would S(h) = I(h) × (1−WeightNormOverlap)^α outperform the CKA-based version? If so, the CKA contribution is marginal. If not, why not, given the regression suggests weight norm is more predictive?

**W6. α=1 default is suboptimal by the paper's own data (both reviewers).** The α ablation shows monotonic improvement from 27% (α=0) to 40% (α=4), a 13pp range. The main results use α=1 (30%), leaving a 10pp gap to the apparent optimum — larger than the claimed 5pp GRPO advantage. The "conservative default" argument is unsatisfying: if α=4 is better, report main results at α=4 (or α=2 as the recommended default). The seed sensitivity at α=4 (±3pp) is acknowledged but not disqualifying.

**W7. CKA computed on mean-pooled activations (R1).** Computing CKA on mean-pooled activations across 512 calibration samples collapses positional and sequential structure. For reasoning models where chain-of-thought unfolds over hundreds of tokens, temporal dynamics are arguably the most informative signal for functional similarity. No justification is provided for mean-pooling, and no comparison to token-level CKA is offered.

**W8. Near-circularity in Claim 2 (R1).** The mixed-effects regression predicts "per-structure recoverability" from CKA overlap. But structures with high F(h) are by definition those whose function is replicated elsewhere — of course their removal is more recoverable. This is closer to validating the CKA definition than providing a genuinely predictive finding. A stronger test would predict recovery outcomes for held-out structures or novel sparsity levels.

**W9. OOD advantage limited to mathematical reasoning (R2).** RASP advantage is +5pp on GSM8K and MATH-500 but only +1pp on HumanEval and MMLU. The CKA signal appears to capture math-reasoning-specific redundancy patterns, not general functional overlap. This limits the practical scope considerably and should be more prominently discussed.

**W10. Only MLP channel groups pruned (R2).** At 20-25% sparsity, 0/112 attention GQA groups are pruned. The CKA functional overlap signal is validated exclusively on MLP structures. Whether CKA captures meaningful redundancy in attention mechanisms (which operate differently from MLPs) is untested. The generality of the "functional overlap" concept beyond MLP groups is undemonstrated.

### Minor

**W11. "Redundancy Paradox" is standard intuition (R2).** That redundant structures are safer to remove than unique ones is the standard justification for redundancy-based pruning. Calling this a "paradox" is rhetorical inflation. The genuinely novel insight — that the value of redundancy depends on the recovery method — is already captured by the interaction finding.

**W12. F(h) definition inconsistency.** The method section (Eq. 3) defines F(h) as max CKA with any other same-layer structure, but this could be confused with mean pairwise CKA depending on implementation. The paper should clarify unambiguously.

**W13. Narrow operational range.** 20-25% sparsity is the only viable range; 30% approaches collapse for both methods. Practical deployment often targets higher compression (50%+). The method's applicability is bounded.

---

## Questions for Authors

1. **Multi-seed recovery:** What are the exact degrees of freedom in the 2×2 ANOVA (Table 3)? If each cell has one GRPO training run, how is the p=0.008 computed — bootstrap over test instances, permutation test, or something else? Have you estimated GRPO training variance from any preliminary runs?

2. **Weight norm as alternative to CKA:** Given that weight norm has higher incremental R² (14% vs 8%) in Table 5, have you tested S(h) = I(h) × (1−WeightNormOverlap)^α? What is the correlation between weight-norm-based overlap and CKA F(h)?

3. **α default:** Why report main results at α=1 when your own ablation shows α=2–4 is strictly better? Have you validated whether the α ranking transfers from post-prune to post-recovery accuracy?

4. **Token-level CKA:** Have you compared mean-pooled CKA to token-level CKA (e.g., CKA computed on individual token positions or sliding windows)? Given that reasoning traces can be hundreds of tokens, temporal structure seems critical.

5. **Interaction generality:** The interaction is demonstrated for SFT vs. GRPO on one model. Can you predict which pruning method wins for a different recovery paradigm (DPO, KTO, PPO) before running the experiment? This would elevate the contribution from observation to predictive framework.

6. **FANG and PAT comparison:** How does RASP's CKA-based overlap differ from FANG's activation-based functional grouping? PAT (AAAI 2025) jointly optimizes pruning and tuning — how does RASP's sequential approach compare?

7. **Circularity in Claim 2:** The regression predicts recoverability from CKA overlap, but high-overlap structures are definitionally those with redundant function. Is this finding informative beyond validating the CKA definition itself?

---

## Experiment Coverage Assessment

Comparing against the full experimental design (18 planned experiments):
- **Fully covered (16/18):** Post-prune full eval, post-recovery full eval, GRASPrune baseline, multi-seed post-prune, scoring ablation, CKA regression, SFT-only comparison, 25% sparsity pipeline, 30% sparsity probe, OOD evaluation, Bonsai baseline, CKA reliability, α ablation, inference speedup, unstructured baseline, SFT OOD eval.
- **Not covered (0/18):** All planned experiments appear in the paper.
- **Coverage is comprehensive.** The paper executes all designed experiments, which is commendable scope.

---

## Verdict and Actionable Recommendations

The paper addresses a genuinely novel research question — the interaction between pruning strategy and recovery paradigm — and executes a comprehensive experimental program. The central finding (12pp crossover, p=0.008) is interesting and potentially impactful. However, the evidence base is too thin for confident acceptance at a top ML venue:

**Must-haves for resubmission:**
1. Multi-seed GRPO recovery (3+ seeds per condition) to establish training variance and validate the interaction p-value with proper denominator df.
2. Validation on at least one additional model architecture.
3. Comprehensive related work section addressing FANG, PAT, Davari et al., and other missing works.

**Strong improvements:**
4. Ablate the scoring formula itself (not just α): compare multiplicative vs. additive, CKA vs. weight-norm overlap, CKA vs. SVCCA.
5. Report main results at α=2 (recommended default) rather than α=1, or provide post-recovery validation for optimal α.
6. Address CKA mean-pooling limitation with at least a discussion or preliminary token-level comparison.

**If all three must-haves are addressed**, the paper would likely reach Weak Accept (4/6) or higher, depending on whether the interaction replicates across seeds and models. The research direction is promising and the question is timely.

---

## Scoring Breakdown

| Criterion | Score | Notes |
|-----------|-------|-------|
| Novelty | 4/6 | Interaction question novel; CKA scoring incremental over MPruner |
| Soundness | 3/6 | Single-seed recovery, ANOVA df concern, formula unjustified |
| Significance | 3/6 | Modest effect sizes, CKA weakest predictor, single model |
| Clarity | 4/6 | Well-written, honest reporting, but too-thin related work |
| **Overall** | **3/6 (Weak Reject)** | Novel question, insufficient evidence |

**R1 Score:** 3/6 (Weak Reject), Confidence 4/5
**R2 Score:** 3/6 (Weak Reject), Confidence 4/5
**Consensus:** 3/6 (Weak Reject), Confidence 4/5