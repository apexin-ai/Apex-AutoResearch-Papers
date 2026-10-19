---
dream_id: dream_20260518T173518
tier: best
overall_score: borderline conference (3.5/6)
timestamp: 2026-05-18T18:29:13.678750+00:00
---

# Dream Review Report: "Output-Distribution Distillation Discovers Hidden Neuron Importance in SwiGLU Activation Sparsity"

**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-18
**Venue Standard:** Top ML venue, ~25% acceptance, 6-point scale

---

## Panel

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Methods + Experiments | 4.0 (Weak Accept) | 4/5 |
| R2 | Novelty + Related Work | 3.5 (Borderline) | 4/5 |
| **Consensus** | | **3.5 (Borderline Conference)** | **4/5** |

---

## Paper Summary

The paper proposes replacing BCE loss with KL-divergence distillation for training SwiGLU sparsity predictors. The core finding is that KL-trained predictors discover neuron importance masks that diverge 53% from magnitude-based oracles, and a causal ablation (training BCE on KL-derived targets) confirms that the mask patterns themselves, not the gradient coupling during training, are the sole driver of KL's quality advantage. A 6-point regime curve identifies three sparsity operating regimes, and evaluations span PPL, downstream tasks, LongBench, MT-Bench, and RULER. Experiments are primarily on Llama 3.1 8B with limited cross-scale validation on Qwen-2.5-14B.

---

## Consensus Strengths

### S1. Clean causal ablation design (both reviewers)
The C1 ablation (BCE trained on KL-derived hard masks) is well-conceived and provides a genuine mechanistic insight. The null result (PPL delta ≤ 0.03, max downstream delta < 1pp across two seeds) cleanly disentangles target quality from gradient coupling. This is the paper's strongest scientific contribution and elevates it above a simple "loss function swap" paper.

### S2. Thorough and honest experimental reporting (both reviewers)
The paper systematically ablates each design choice (Gumbel vs. STE, forward vs. reverse KL, loss isolation, compensation redundancy). Negative results are reported transparently: the 14B MMLU failure, downstream collapse at 50% sparsity, and the non-monotonic allocation preference. The Limitations section is substantive, not perfunctory.

### S3. Useful practical insights (R1)
The 6-point regime curve with three qualitatively distinct regimes provides actionable deployment guidance. The finding that uniform allocation gives 7.5x smaller cross-seed MMLU variance at 30% is practically valuable. The recommended 30% operating point is well-justified.

### S4. Well-structured related work and positioning (R2)
The 2D taxonomy (training-free vs. learned, per-neuron vs. coupled) identifies a genuine gap that the paper fills. Related work sections cover the relevant 2024 literature adequately. The distinction from SPON (static bias correction, cosine similarity 0.196) is quantitatively supported.

---

## Consensus Weaknesses

### W1. [Major] Single-model primary evaluation; 14B result undermines generality
**Both reviewers flagged this independently.** All core results and the causal ablation are on Llama 3.1 8B only. The sole cross-scale validation (Qwen-2.5-14B) shows PPL advantage preserved but MMLU 8pp below TEAL (63.7% vs. 71.8%), actively undermining the central claims. The causal ablation (the paper's strongest contribution) has zero cross-model validation. A paper claiming to "discover hidden neuron importance structure" needs to demonstrate this structure exists beyond one model.

**Recommendation:** Run C1 ablation on at least one additional model (e.g., Mistral-7B) and provide a mechanistic explanation for the 14B MMLU failure.

### W2. [Major] Novelty concerns: assembly of known components
**R2 primary, R1 concurred during roundtable.** The method combines KL distillation + Gumbel-Sigmoid relaxation + Lagrangian sparsity control, all individually well-established. MaskLLM (Fang et al., 2024) already uses frozen weights + learnable masks + KL + Gumbel for a closely related mask-learning problem (semi-structured N:M sparsity). The paper's contribution is primarily empirical (the causal ablation finding), not methodological. While empirical discoveries are valuable, the "hidden neuron importance" framing suggests a deeper contribution than what is delivered.

**Recommendation:** Tone down the discovery framing. Strengthen the mechanistic characterization of what the 53% divergent neurons actually represent (layer distribution, functional role, activation statistics beyond mean gate probability 0.614).

### W3. [Major] No wall-clock speedup; practical impact unclear
**Both reviewers flagged this.** The latency table shows the method adds 6.4% overhead with no actual speedup because masks are unstructured. The 1.36x FLOPs saving at 30% is purely theoretical. Without sparse kernel support, N:M structuring, or at minimum a concrete path to hardware exploitation, the practical value proposition is speculative. This is particularly concerning for a paper positioned around deployment guidelines and "recommended operating points."

### W4. [Major] Causal ablation conducted only at 50% sparsity where downstream metrics are at floor
**Both reviewers flagged this.** The C1 ablation runs at 50% uniform sparsity, where MMLU collapses to ~28% (near random) for all methods. "Matching within 0.79pp" at near-random performance is not informative for downstream quality. The ablation would be substantially more convincing at 30% sparsity where downstream metrics are still meaningful and the method is actually recommended for use.

**Recommendation:** Replicate C1 at 30% sparsity. If the null result holds there too, the claim is much stronger.

### W5. [Minor] Statistical rigor at the recommended 30% operating point
KL uniform MMLU at 30% is 44.8 (from regime curve) or 40.7 ± 1.3 (from 3-seed evaluation), while TEAL is 38.61 (single seed). The ~2pp improvement is not tested for statistical significance, and TEAL is not evaluated with multiple seeds. The headline PPL improvement (8.82 vs. 10.97) is more robust but downstream is where practitioners care.

### W6. [Minor] Gradient analysis section (~1 page) is rendered moot by the paper's own ablation
**R2 primary.** Section 3.5 develops the gradient coupling analysis in detail, but Section 4.3 then demonstrates that gradient coupling contributes zero measurable effect. The gradient analysis provides mathematical intuition for why KL *could* work, but the causal ablation shows the actual mechanism is different. This creates a narrative tension and the gradient analysis section consumes space that could be used for the missing mechanistic characterization of divergent neurons (W2).

### W7. [Minor] Training/evaluation data proximity
Training on WikiText-103 and evaluating PPL on WikiText-2 (same Wikipedia source). C4 OOD evaluation exists in appendix but shows noticeably larger degradation ratio (1.74x dense vs. 1.44x on WikiText-2), which deserves main-text discussion.

### W8. [Minor] Incomplete MT-Bench reporting
Table 5 shows per-category scores only for KL 30%; Dense and TEAL 30% per-category scores are missing, preventing category-level comparison. Only average scores are reported for all three conditions.

### W9. [Minor] Missing references
Several relevant works are absent: SliceGPT (structured pruning via rotation), Fisher-information-based importance methods, SparseGPT, and Wanda (magnitude + input-aware pruning). With only 11 references total, the bibliography appears thin for a venue-ready submission.

---

## Questions for Authors (Priority-Ordered)

1. **Can you run C1 at 30% sparsity?** This would directly address W4 and substantially strengthen the core claim.
2. **Why does KL hurt MMLU at 14B while helping PPL?** Without a mechanistic explanation, this failure mode raises concerns about generalizability. Does KL systematically deprioritize neurons important for factual recall at larger scales?
3. **What is the per-layer mask divergence distribution?** The 53% average masks a potentially informative distribution. Do early/late layers diverge more? Does divergence correlate with layer importance?
4. **Can you provide multi-seed TEAL baselines at 30%?** Needed for fair statistical comparison.
5. **What do the KL-important, magnitude-unimportant neurons actually compute?** Beyond mean gate probability (0.614), can you characterize their functional role (e.g., which token types or syntactic structures activate them)?
6. **Is there a path to structured (N:M) sparsity from KL masks?** This would address the wall-clock speedup gap.

---

## Experiment Coverage Assessment

| Planned Experiment | In Paper? | Completeness |
|---|---|---|
| C1 Causal Ablation (2 seeds) | Yes (Table 2) | Full |
| 6-Point Regime Curve | Yes (Table 3) | Full |
| BCE 30% Forced Top-k | Yes (Table 1) | Full |
| LongBench (4K-32K) | Yes (Table 4) | Full |
| MT-Bench | Yes (Table 5) | Partial (missing per-category Dense/TEAL) |
| RULER (4K/16K) | Yes (Table 6) | Full |

All planned experiments are reflected. MT-Bench reporting is incomplete but the experiment was conducted.

---

## Consolidated Assessment

**Score: 3.5 / 6 (Borderline Conference)**

The paper asks a good research question ("what makes KL better for sparsity prediction?") and provides a clean answer via the causal ablation ("the masks, not the gradients"). This is a genuine scientific contribution. The experimental suite is thorough and honestly reported.

However, the paper faces a convergence of limitations that collectively bring it to borderline: (1) single-model primary evaluation with a cross-scale result that actively undermines generality claims; (2) the method is an assembly of known components, with MaskLLM as close prior art; (3) no wall-clock speedup despite deployment-oriented framing; (4) the causal ablation is conducted at a sparsity level where downstream metrics are uninformative; (5) downstream improvements at the recommended operating point are modest and not clearly statistically significant.

The paper would benefit most from: running C1 at 30% sparsity, replicating C1 on a second model, providing mechanistic characterization of divergent neurons, and either demonstrating wall-clock speedup or reframing away from deployment.

**Actionable path to acceptance:** Address W1 (cross-model C1) and W4 (C1 at 30%), tone down discovery framing (W2), and either demonstrate speedup or explicitly reposition as an analysis/understanding paper. These changes would likely move the score to 4.0-4.5.
