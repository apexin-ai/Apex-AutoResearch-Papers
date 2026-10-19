---
dream_id: dream_20260518T173518
tier: median
overall_score: Findings (3.0/6.0)
timestamp: 2026-05-18T18:36:43.544284+00:00
---

# Dream Review Report — Full Roundtable

**Paper**: "What Does KL Distillation Learn for SwiGLU Sparsity Prediction? Mask Pattern Discovery Beyond Magnitude Oracles"

**Review mode**: full (2 Reviewers, 4-step roundtable)
**Scoring scale**: 6-point (1=Strong Reject … 6=Strong Accept), top ML venue, ~25% acceptance

---

## Roundtable Summary

| Reviewer | Focus | Initial Score | Post-Crossshare Score |
|----------|-------|--------------|----------------------|
| R1 | Methods + Experiments | 3.5 | 3.0 |
| R2 | Novelty + Related Work | 3.0 | 3.0 |
| **Consensus** | | | **3.0 (Findings)** |

Both reviewers converged to 3.0 after cross-share. R1 moved down 0.5 points after accepting R2's argument that the core method (KL + Gumbel-Sigmoid for mask training) is substantially anticipated by MaskLLM (Fang et al., NeurIPS 2024). R2 considered moving to 2.5 based on R1's wall-clock speedup and downstream collapse arguments, but held at 3.0 given the causal ablation's genuine analytical value.

---

## Consensus Strengths

**S1. Clean causal ablation (C1) is the paper's strongest and most original contribution.** Both reviewers independently identified this as the standout experiment. BCE trained on KL-derived oracle masks recovers >95% of KL's advantage (PPL delta 0.15–0.28), cleanly proving target quality, not gradient coupling, drives KL's gains. The two-seed verification and five-metric coverage (PPL + 4 downstream) add credibility. This is a genuinely informative experiment rare in the activation sparsity literature.

**S2. Honest and transparent reporting of failures.** Both reviewers commended the paper's candor: downstream collapse at 50% sparsity (MMLU near random), no wall-clock speedup (0.94×), 14B MMLU disconnect (63.7% vs TEAL 71.8%), long-context degradation (72%→41% at 4K→32K), and single-seed noise at 35%. This level of transparency is unusual and builds trust.

**S3. Comprehensive ablation coverage.** The paper includes ablations for divergence direction (forward KL vs JSD vs reverse KL), relaxation method (STE vs Gumbel), loss isolation, compensation redundancy, iso-compute BCE, and SPON orthogonality. The hyperparameter sensitivity analysis shows <3% variation across configurations.

**S4. Useful conceptual taxonomy.** The correction-granularity × training-signal-coupling framing places prior work (DejaVu, FastForward, ShadowLLM, SPON, D2DMoE) in a clear space and identifies the paper's contribution as filling the per-token × coupled cell.

**S5. Cross-architecture validation.** KL/TEAL PPL ratio is remarkably consistent across Llama (1.24×/1.98×/5.59×) and Mistral (1.24×/2.12×/4.63×), supporting generality of the finding within the 7-8B range.

---

## Consensus Weaknesses

**W1 [Major]. No wall-clock speedup — the method is slower than dense inference.** Table 6 shows 0.94× actual throughput at 30% sparsity (+3.17ms predictor overhead on 119.1ms dense baseline). The paper's fundamental motivation is inference acceleration, yet the method adds latency. Theoretical FLOPs reductions (1.36× at 30%) are meaningless without sparse kernel realization. DejaVu and PowerInfer demonstrated actual speedups; this paper does not. There is no analysis of whether the unstructured element-wise masks are even compatible with existing sparse libraries (Triton, cuSPARSE). Both reviewers flagged this; R2 considered it sufficient to lower the score further.

**W2 [Major]. Core methodological contribution is thin and anticipated by MaskLLM.** The method combines a standard two-layer MLP predictor, Gumbel-Sigmoid relaxation (Jang et al. 2017), forward KL divergence (Hinton et al. 2015), and adaptive penalty for sparsity control. None is novel individually, and the combination is the natural first thing to try. MaskLLM (Fang et al., NeurIPS 2024) already demonstrated "frozen weights + learnable masks + KL training" via Gumbel relaxation for N:M weight sparsity. The paper dismisses MaskLLM based on weight-vs-activation sparsity differences, but the core intellectual move is the same. R1 initially underweighted this but agreed after cross-share.

**W3 [Major]. Downstream collapse at 50% sparsity undermines the headline PPL result.** The paper's most dramatic PPL improvement (11.78 vs 23.31) occurs at 50%, where MMLU drops to ~28% (near 25% random), GSM8K to ~2%, and ARC-c to ~34% (vs 58.3% dense). The model is functionally broken for knowledge-intensive tasks at this regime. At the recommended 30% operating point, gains are more modest (PPL 8.82 vs 10.97, 18% improvement). The disconnect between PPL and downstream quality is itself an underexplored finding.

**W4 [Moderate]. 53% mask divergence lacks mechanistic analysis.** This is presented as a primary finding (abstract, introduction, conclusion) but analysis stops at the aggregate Jaccard number. No per-layer distribution, no characterization of which neurons KL prefers over magnitude (e.g., low-magnitude but high downstream Jacobian?), no correlation with token difficulty or domain. "Fundamentally different neuron importance landscape" is unsupported beyond one number.

**W5 [Moderate]. Missing baselines — both WINA and predictor-based methods.** WINA is listed as a baseline in Section 4.1 but never appears in any results table. ShadowLLM and original FastForward numbers are absent; the BCE predictor is the authors' own reimplementation. Without these, the claim of superiority over prior predictor-based methods rests only on comparison against the authors' own BCE baseline.

**W6 [Moderate]. Gradient analysis narrative contradicts the ablation.** Section 3.3 builds intuition around coupled vs factorized gradients as KL's advantage mechanism. Section 4.4 then shows gradient coupling contributes only 1–3%. This creates narrative tension: substantial space is devoted to a motivation that the paper's own experiments largely dismiss. The gradient analysis should be shortened and explicitly framed as "mechanism of target discovery, not driver of quality advantage."

**W7 [Moderate]. Near-domain training/evaluation inflates results.** Training on WikiText-103 and evaluating on WikiText-2 (same domain) creates an optimistic picture. C4 OOD PPL ratio is 1.74× vs in-domain 1.46× at 30%, showing significant domain sensitivity. C4 results should be in main tables, not appendix.

**W8 [Minor-Moderate]. Adaptive penalty deviation at recommended operating point.** At 30% target, the controller achieves only 28.5% actual sparsity (λ saturates at cap). Comparing KL at 28.5% against TEAL at 30% introduces a systematic advantage for KL.

**W9 [Minor-Moderate]. Scale limitations undermine generality.** Validated only at 7-8B. At 14B (Qwen-2.5-14B), MMLU drops 8pp below TEAL despite better PPL. No models above 14B tested. The practical value proposition is narrow.

**W10 [Minor]. Missing citations.** Polar Sparsity (Shrestha et al., NeurIPS 2025) — challenges scalability of MLP contextual sparsity to batched inference. DistiLLM (Ko et al., ICML 2024) — relevant to KL direction choice. Instruction-Following Pruning (Hou et al., ICML 2025) — architecturally similar sparse mask predictor.

---

## Key Questions for Authors

**Q1.** WINA is listed as a baseline but absent from all tables. What are its numbers at 30% and 50%?

**Q2.** What is the per-layer distribution of the 53% mask divergence? Is it concentrated in specific layers? What characterizes the neurons KL prefers over magnitude?

**Q3.** MaskLLM uses the same core approach (KL + Gumbel for mask learning) in weight sparsity. Beyond the application domain, what is the intellectual contribution over MaskLLM?

**Q4.** At 14B, KL achieves better PPL but worse MMLU (63.7% vs 71.8%). Can you provide per-subtask or per-layer analysis?

**Q5.** Have you evaluated at batch sizes relevant to serving (e.g., 8, 32)? Polar Sparsity shows MLP contextual sparsity benefits vanish with batched inference.

**Q6.** The adaptive penalty achieves only 28.5% sparsity at 30% target. Have you compared TEAL at matched actual sparsity (28.5%)?

**Q7.** Could a cheaper two-stage pipeline work: KL for 100 steps to extract targets, then BCE for 900 steps?

---

## Experiment Coverage Assessment

Comparing against the imagined experiment list in review_context.yaml:

| Experiment | Covered? | Notes |
|-----------|----------|-------|
| Four-condition ablation (plan_001) | ✅ | Table 1 |
| STE baseline (plan_002) | ✅ | Table 8 |
| Iso-compute BCE (plan_003) | ✅ | Section 5.2 |
| SPON reimplementation (plan_004) | ✅ | Table 7 |
| SPON subsumption (plan_005) | ✅ | Table 7 |
| Training-free baselines (plan_006) | ⚠️ | TEAL/R-Sparse in Table 1, but WINA missing from tables |
| Full benchmark + Pareto (plan_007) | ✅ | Table 2, Table 6 |
| Sparsity regime (plan_008) | ✅ | Table 4 |
| Mistral cross-arch (plan_009) | ✅ | Table 5, but downstream sparse at 30% |
| LongBench (plan_010) | ✅ | Table 9 |
| MT-Bench (plan_011) | ✅ | Table 10 |
| RULER (plan_012) | ✅ | Table 11 |
| C1 causal ablation | ✅ | Table 3 |
| Dense sparsity sweep (6pt) | ✅ | Table 4 |
| BCE 30% forced top-k | ✅ | Table 2 |

Coverage: 14/15 experiments represented. WINA numbers are the main gap.

---

## Minor Issues

1. References show [??] placeholders in the introduction (broken \cite commands).
2. Weight decay inconsistency: 0.05 in paper vs 0.01 in ablation code.
3. "Unified benchmark protocol" in Table 3 caption never defined.
4. Some table entries lack seed annotations (e.g., KL global at 50% in Table 1).
5. R-Sparse and DIP listed in Related Work but absent from experimental comparison.
6. The paper title may differ between the PDF and the submission metadata.

---

## Final Verdict

**Consensus Score: 3.0 — Findings**
**Confidence: 4/5**

The paper presents a well-executed empirical study with one genuinely valuable analytical contribution (the C1 causal ablation proving target quality > gradient coupling). The experimental methodology is thorough, the ablation coverage is above average, and the honest reporting of failures is commendable. These qualities make it a solid Findings paper.

However, it falls short of a main conference contribution for several reinforcing reasons: (1) the core method (KL + Gumbel for mask training) combines standard components and is anticipated by MaskLLM; (2) the central empirical finding (53% mask divergence) lacks the mechanistic depth to stand as a primary contribution; (3) no wall-clock speedup is demonstrated, undermining the practical motivation; (4) downstream tasks collapse at the regime where PPL gains are largest; and (5) scale validation is limited to 7-8B with known failures at 14B. The C1 ablation and regime analysis provide genuine value to the activation sparsity community, but the novelty and practical impact do not clear the ~25% acceptance bar for a main conference track.