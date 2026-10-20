---
dream_id: dream_20260515T140651
tier: worst
overall_score: weak reject (3/6)
timestamp: 2026-05-15T15:11:55.919613+00:00
---

# Dream Review Report: "Do Reasoning LLMs Need Recovery-Aware Pruning?"

**Dream ID:** 20260515T140651
**Review Mode:** Full (2 Reviewers + Roundtable)
**Consensus Score:** 3/6 (Weak Reject)

---

## Reviewer Assignments

- **R1 (Methods + Experiments):** Score 4/6 (Weak Accept), Confidence 4/5
- **R2 (Novelty + Related Work):** Score 3/6 (Weak Reject), Confidence 4/5
- **Post-Roundtable Consensus:** 3/6 (Weak Reject)

---

## Paper Summary

The paper proposes Recovery-Aware Structured Pruning (RASP), scoring structures as S(h) = I(h) × (1−F(h))^α where F(h) is CKA-based functional overlap. It tests this hypothesis on DeepSeek-R1-Distill-Qwen-7B across 3 sparsity levels, 4 pruning methods, and 2 recovery paradigms (SFT, SFT→GRPO). Core findings are negative: CKA does not predict recoverability (β=0.08, p=0.12, R²=1.8%), Standard+SFT beats RASP+SFT (63.5% vs 55.3%), GRPO adds nothing over SFT (p=0.62). One positive finding: α-scaling improves post-prune accuracy by +12pp at α=4, but this vanishes after SFT recovery.

---

## Experiment Coverage Assessment

All 18 planned experiments from the design document are represented in the paper:

| # | Experiment | Paper Location | Status |
|---|-----------|---------------|--------|
| 1 | Full GSM8K Eval N=1319 (Post-Prune) | Table 1 | ✓ |
| 2 | SFT Warmup Recovery | Table 3 | ✓ |
| 3 | GRPO Stage-2 Recovery | Table 4 | ✓ |
| 4 | Full GSM8K Eval (All Recovered) | Table 5 | ✓ |
| 5 | GRASPrune Baseline 20% | Table 7 | ✓ |
| 6 | Multi-Seed Post-Prune (5 Seeds) | Table 2 | ✓ |
| 7 | Scoring Ablation 20% | Table 8 | ✓ |
| 8 | CKA-Recoverability Correlation | Table 10 | ✓ |
| 9 | SFT-Only Recovery / 2×2 ANOVA | Table 6 | ✓ |
| 10 | 25% Sparsity | Table 11 | ✓ |
| 11 | 30% Sparsity Probe | Table 11 | ✓ |
| 12 | OOD Evaluation (MATH-500, HumanEval) | Table 12 | ✓ |
| 13 | Bonsai Baseline 20% | Table 7 | ✓ |
| 14 | CKA Reliability Analysis | Section 5.8 text | ✓ |
| 15 | α Sensitivity Ablation | Table 9 | ✓ |
| 16 | Inference Speedup Benchmark | Table 14 | ✓ |
| 17 | Unstructured Pruning Baseline 20% | Table 13 | ✓ |
| 18 | SFT OOD Eval Contingency | Merged into Table 12 | ✓ |

Coverage: **18/18 (100%)**. The experimental program is fully represented.

---

## Consolidated Strengths

### S1. Exceptional Experimental Thoroughness (R1+R2 consensus)
The combination of 5-seed evaluation, 2×2 factorial ANOVA, mixed-effects regression with layer random effects, scoring ablations, α sweep, sparsity scaling, OOD evaluation, 4 external baselines, and inference benchmarks sets a high bar for empirical pruning research. The statistical methodology (paired t-tests, Wilcoxon, Cohen's d, bootstrap CIs, effect sizes) is more sophisticated than the vast majority of pruning papers. This is a genuine strength.

### S2. Honest Reporting of Negative Results (R1+R2 consensus)
The paper proposes a hypothesis, tests it rigorously, and honestly reports its falsification. The narrative structure (hypothesis → test → falsify → extract lessons) is scientifically sound. The paper does not bury the failure or oversell marginal findings.

### S3. Well-Controlled Comparison (R1)
Standard and RASP share identical infrastructure, calibration data, per-layer floors, and parameter budgets. The only difference is structure selection via CKA weighting. This level of experimental control is essential for isolating the CKA contribution and is executed well.

### S4. Actionable Practical Takeaways (R1+R2 consensus)
"Use Standard+SFT, skip GRPO, focus on sparsity ratio" is clear, useful guidance. The finding that the simplest pipeline is Pareto-optimal saves practitioners from pursuing complex alternatives.

### S5. The α-Scaling Proxy-vs-Target Insight (R1+R2 consensus)
The decoupling between post-prune and post-recovery accuracy (α=4 helps pre-recovery but vanishes after SFT) is a genuinely useful methodological insight: optimizing a proxy metric does not optimize the true target. This cautionary finding has broad applicability beyond this specific method.

---

## Consolidated Weaknesses

### W1. [CRITICAL] Negative Claim Overclaimed Relative to Scope (R2, endorsed by R1 post-roundtable)
The paper concludes that "functional overlap does not predict recoverability" and that "recovery-aware pruning yields negligible benefit." However, the evidence supports only a narrower claim: **mean intra-layer linear CKA, in this specific multiplicative formulation, on MLP groups at 20–30% sparsity, on one distilled model, does not predict recoverability.** Crucially:

- **Only one similarity metric tested.** SVCCA, OPD, RSA, mutual information, or RBF-kernel CKA are not compared. Davari et al. (ICLR 2023) documented CKA failure modes (sensitivity to outliers, manipulability) that are directly relevant but unmentioned.
- **CKA overlap range is extremely narrow** ([0.879, 0.997] for MLP groups), severely limiting discriminative power. At α=1, the overlap penalty varies by ~10× across groups; at α=0.25, barely 2×. The null result for CKA predictiveness may simply reflect insufficient variance in the predictor.
- **Mean pooling over sequence length** discards temporal reasoning structure. Two MLP groups with different activation patterns across reasoning steps (early vs. final) would appear identical.
- **CKA computed on gate_proj only**, not the full gated MLP output (gate × up → down). This may not capture true functional similarity.

The paper should either test alternatives or explicitly scope its negative claim to "CKA-based overlap in this formulation."

### W2. [MAJOR] Self-Healing (2025) Contradiction Unresolved (R2)
Self-Healing Authors (2025) showed RLVR recovers standard-pruned models to 95%+ at 25% compression, significantly outperforming SFT (~80%). This paper finds GRPO adds nothing over SFT (p=0.62). This is a **direct contradiction** that demands explanation. Possible confounds (structured vs. unstructured pruning, different GRPO compute budgets, different base models, GRPO hyperparameter sensitivity) are not systematically discussed. Without reconciliation, the reader cannot assess whether the GRPO-adds-nothing finding is robust or an artifact.

### W3. [MAJOR] Single GRPO Training Run (R1+R2 consensus)
The GRPO null result (p=0.62) rests on a single training run per condition. The project history documents 8 GRPO versions (v1–v7 failures, v8 success), indicating high training instability. Without even 2–3 GRPO seeds, "GRPO adds nothing" is indistinguishable from "our single GRPO run was unlucky or suboptimally configured." The conclusion should be hedged to "we could not demonstrate a GRPO benefit under these conditions."

### W4. [MAJOR] α=4 Confound Unresolved (R1+R2 consensus)
The only positive finding (+12pp post-prune at α=4) has an untested alternative explanation. At α=4, (1−F(h))^4 creates extreme nonlinear compression of scores, effectively reshaping the importance distribution. The critical missing control experiment is **I(h)^β without CKA** (or any monotone reshaping of importance scores). If I(h)^4 achieves similar gains, the 12pp improvement has nothing to do with CKA. Without this ablation, the positive finding cannot be attributed to functional overlap.

### W5. [MAJOR] Single Model Limits Generalizability (R1+R2 consensus)
DeepSeek-R1-Distill-Qwen-7B is a distilled model whose internal redundancy patterns may differ from natively-trained reasoning models. Generalization to other architectures (LLaMA, Mistral), scales (1B–70B), attention configurations (MHA, MQA), and training regimes is entirely unknown. For a negative result paper, single-model evidence limits conclusions to "does not work here" rather than "does not work in general."

### W6. [MODERATE] Missing Related Work (R2)
Several relevant works are missing:
- **"Free Lunch in LLM Retraining"** (Wagner et al., 2025): Shows recovery dominates pruning method — directly supports the paper's finding but provides prior evidence that weakens the novelty claim.
- **PAT (AAAI 2025):** Joint pruning-tuning optimization — challenges the "unexplored" claim.
- **Davari et al. (ICLR 2023):** CKA failure modes — directly relevant to explaining the negative CKA finding.
- **"Boiling Frog" (Zhao et al., 2026):** Iterative prune-tune loops showing SFT sufficiency.

The claim "interaction between pruning structure and recovery method remains unexplored" is overclaimed.

### W7. [MODERATE] Scoring Ablation at N=100 (R1)
Table 8 uses N=100 (95% CI ≈ ±9pp). Differences between Standard (28%), RASP α=1 (30%), Magnitude (27%), and Gradient (26%) are within noise. Only the α=4 (40%) comparison exceeds CI width. Full N=1319 evaluation or explicit CI reporting needed.

### W8. [MODERATE] 14 Tables May Be Excessive (R2)
For a paper whose core message is "this doesn't work," the sheer volume of tables risks diluting the key findings. A tighter presentation focusing on the 4–5 most impactful results would be more compelling.

### W9. [MINOR] "Redundancy Paradox" Is Rhetorical Inflation (R1)
The idea that redundant structures are safer to remove is standard pruning intuition, not a paradox.

---

## Key Questions for Authors

1. **Have you tested I(h)^β (without CKA) as a scoring function?** If I(h)^4 achieves similar post-prune gains to RASP α=4, the CKA contribution is illusory. This is the single most important missing experiment.

2. **Why does your GRPO-adds-nothing finding contradict Self-Healing (2025)?** Self-Healing showed RLVR dramatically outperforms SFT. What explains the discrepancy — structured vs. unstructured pruning, compute budget, hyperparameters, or model differences?

3. **Did you test any alternative similarity metrics beyond linear CKA?** Given the narrow CKA overlap range [0.879, 0.997], a different metric with more discriminative power might yield different results.

4. **What is the pruning mask overlap between Standard and RASP?** If >80% of the 200 pruned MLP groups are identical, the small performance difference is expected regardless of CKA's validity.

5. **What happens at ≥40% sparsity where attention groups enter the pruning range?** The CKA signal for attention GQA groups (only 4 per layer, potentially more heterogeneous overlap) is never empirically tested.

---

## Reviewer Detailed Scores

### R1 (Methods + Experiments): 4/6 (Weak Accept)
**Rationale:** The experimental design is commendable — 18 experiments, 5-seed validation, factorial ANOVA, mixed-effects regression, and controlled comparison. The negative result is well-supported by the evidence within its scope. The honest reporting and practical takeaways constitute a contribution. Concerns about single GRPO run, α=4 confound, and N=100 ablation are real but do not invalidate the core findings. Acceptance contingent on: (a) acknowledging α confound explicitly, (b) reporting GRPO variance, (c) reframing scope of negative claim.

### R2 (Novelty + Related Work): 3/6 (Weak Reject)
**Rationale:** The research question is excellent and the methodology commendable, but the paper's contribution is structurally weak. The negative result is overclaimed relative to scope (one model, one CKA variant, narrow overlap range). The RASP formulation risks being seen as a strawman — testing one simple heuristic and concluding that the entire class of functional-overlap-aware pruning is ineffective. The Self-Healing contradiction is unresolved. Missing related work weakens the "unexplored" positioning. The paper lacks a strong positive contribution — α-scaling gains vanish after recovery, so even the positive finding is another negative result. Better suited for a Findings track or workshop.

---

## Roundtable Consensus: 3/6 (Weak Reject)

### Consensus Rationale
Both reviewers agree the experimental thoroughness is exceptional and the honest reporting of negative results is laudable. However, after cross-sharing, R1 concurred with R2's central concern: **the breadth of the negative claim exceeds the evidence base.** The paper tests one specific CKA formulation on one model in a narrow sparsity regime and concludes broadly that "functional overlap does not predict recoverability" and "recovery-aware pruning yields negligible benefit." This overclaim is the primary reason for the weak reject.

The unresolved Self-Healing contradiction (W2) is the second deciding factor: the paper's most practically consequential finding (GRPO adds nothing) directly contradicts established literature, and a single-run result with documented instability cannot overturn a prior published finding without explanation.

### What Would Change the Score
- **To 4/6 (Weak Accept):** (a) Test 2+ alternative similarity metrics, (b) resolve Self-Healing contradiction, (c) add I(h)^β ablation, (d) scope negative claims narrowly.
- **To 5/6 (Accept):** All of the above plus (e) second model family, (f) multi-seed GRPO, (g) higher sparsity regime where attention groups are pruned.

### Verdict
The paper asks an important question and provides a well-executed but inconclusive answer. The experimental infrastructure and methodology are publication-quality, but the negative conclusions need either narrower scoping or broader evidence to be convincing at a top venue. Recommended path: scope claims to "CKA-based RASP on this model/regime," add the I(h)^β control, reconcile with Self-Healing, and resubmit.