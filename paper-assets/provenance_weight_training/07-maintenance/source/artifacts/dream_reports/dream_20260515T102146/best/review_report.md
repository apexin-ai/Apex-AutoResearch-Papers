---
dream_id: dream_20260515T102146
tier: best
overall_score: Weak Reject (3/6)
timestamp: 2026-05-15T11:16:34.382275+00:00
---

### R1 Assessment: Methods & Experiments

**Summary**

The paper proposes dual-constrained adaptive b* for contamination-aware pretraining reweighting, positing a "minimum intervention principle" via alpha_eff quality floor + ESS stability ceiling. However, the actual experimental results contradict the paper's core narrative: ESS-only (max-intervention) achieves 17.635 PPL, outperforming both dual-constrained (17.650) and grid-best (17.651). This means the alpha_eff constraint -- framed as the paper's primary methodological contribution -- is empirically harmful, not load-bearing. The paper's framing needs fundamental revision. Effect sizes remain small (0.04 PPL at rho=0.4, seed variance ~0.005-0.009), and critical experiments lack multi-seed validation.

**Strengths**

- S1: The formulation is mathematically clean. The monotonicity proof for alpha_eff(b) is correct (Chebyshev covariance inequality), and the dual-constraint framework (alpha_eff lower bound on b, ESS upper bound) is well-defined with clear existence/uniqueness guarantees for b*.
- S2: Comprehensive ablation design. The n_min sweep (1-5) with batch_size interaction (4/8/16) is well-conceived and reveals meaningful structure (phase transition at n_min=batch_size, knife-edge at small batch). The tau sweep across 6 values is thorough.
- S3: Good baseline coverage. Seven baselines including Golden Ratio oracle, detect-and-remove, random reweight, and ESS-only provide meaningful comparisons. The random reweight baseline confirming detector signal is necessary is a clean control.
- S4: The detector quality ablation (TF-IDF AUC=0.939 vs ModernBERT AUC=0.986) with the finding that the gap shrinks from 0.015 to 0.002 under strong detection is an interesting interaction result.
- S5: Code-level reproducibility appears high -- the alpha_eff.py implementation uses numerically stable log-space computation, and the bisection search is well-implemented with appropriate clamping.

**Weaknesses**

- W1 (Major): **Core claim is contradicted by results.** The paper frames alpha_eff as "load-bearing" and ESS-only as degenerating to near-uniform. But Table 1 shows ESS-only (17.635) outperforms dual-constrained (17.650) by 0.015 PPL and outperforms grid-best (17.651) by 0.016 PPL. The n_min=1 variant (17.632) is best of all. This directly falsifies the minimum intervention principle -- maximum intervention wins. The entire narrative structure collapses.

- W2 (Major): **Selective multi-seed reporting.** The primary claim (adaptive matches grid-best) has 3-seed validation, but the most important comparison -- ESS-only vs dual-constrained -- is single-seed (seed42 only). Given seed variance of 0.005-0.009, the 0.015 PPL gap between ESS-only and dual could flip with different seeds. Multi-seed ESS-only is the single most critical missing experiment. Similarly, rho=0.6 results lack ESS-only comparison entirely.

- W3 (Major): **Effect sizes are at the noise floor.** The primary improvement is 0.040 PPL (0.23% relative) at rho=0.4. Seed variance is 0.005-0.009 (std). The "recovery ratio" metric (88.6%) is computed from differences of 0.039-0.052 PPL, where a 0.005 shift in any seed changes the ratio by ~10 percentage points. The 3B scaling claim (4x amplification) rests on single-seed comparison where downstream metrics (MMLU +0.7%, HellaSwag +1.1%) are within typical evaluation noise for these benchmarks.

- W4 (Moderate): **The tau sweep contradicts the tau-insensitivity claim.** Table 6 in the paper summary shows PPL monotonically increasing from 17.640 (tau=0.5) to 17.800 (tau=0.95) -- a range of 0.160 PPL, which is 4x the primary effect size. This is not insensitivity; this is a hyperparameter that matters. The paper's tau sweep table in the tex shows a much narrower range (0.023), suggesting either the imagined results and actual results diverge, or different versions of the table exist.

- W5 (Moderate): **alpha_eff definition inconsistency.** The paper's Eq. 2 defines alpha_eff as weighted proportion of samples with q <= 0.5 (indicator function), but the code (alpha_eff.py line 29-53) computes it as weighted mean of (1-q) without any threshold -- a continuous quantity. These are different functions with different monotonicity properties. The paper's theoretical claims (monotonicity via Chebyshev) apply to the code version, not the paper version.

- W6 (Moderate): **Contamination setup is unrealistically clean.** Same-model generation (Qwen3-0.6B generates contamination for Qwen3-0.6B training) creates a detection task that is artificially easy even for TF-IDF (AUC=0.939). Real web contamination involves diverse generators, paraphrasing, and distribution shift. The cross-generator experiment (Section 6.4) is text-only with no table, making it unverifiable.

- W7 (Minor): **n_min=2 is the only working value at batch_size=4.** The paper acknowledges this but frames it as "clear physical meaning." In reality, with batch_size=4, the ESS dynamic range is [2, 4], meaning ~75% of batches hit the ESS floor. The method is operating at its constraint boundary almost always. The batch_size=16 ablation alleviates this but introduces a confound (different effective batch statistics).

- W8 (Minor): **200M tokens is far below practical pretraining scale.** The method's per-batch b* adaptation depends on micro-batch q-score statistics. Whether these statistics remain meaningful at 1B+ token scale with different data compositions is untested.

**Questions for Authors**

- Q1: Table 1 shows ESS-only (17.635) and n_min=1 (17.632) both outperform dual-constrained (17.650). How do you reconcile this with the "minimum intervention principle" narrative? Does this not show that maximum intervention is strictly better?
- Q2: Why is multi-seed validation missing for ESS-only? This is the single most important ablation for the paper's core claim. Can you provide 3-seed ESS-only results?
- Q3: The alpha_eff formula in the paper (Eq. 2, indicator-based) differs from the code (continuous weighted mean). Which was used in experiments? The monotonicity proof applies to the continuous version but the paper presents the indicator version.
- Q4: The tau sweep in the paper summary (Table 6) shows PPL range 17.640-17.800 (range=0.160), but the paper's tau table shows range 17.645-17.668 (range=0.023). Which is correct? If the former, the tau-insensitivity claim is invalid.
- Q5: At rho=0.6, dual-constrained (18.550) underperforms grid-best b=0.5 (18.500) by 0.050 PPL (Table 9). This means the adaptive method is worse than the fixed baseline it claims to replace. Can you explain?
- Q6: The 3B downstream metrics (MMLU +0.7%, HellaSwag +1.1%) -- are these statistically significant? What is the evaluation variance from different prompt templates or few-shot selections?

**Missing Experiments**

- ESS-only adaptive b* with 3 seeds (the most critical gap -- the paper's entire framing depends on dual > ESS-only, but only seed42 is reported)
- ESS-only at rho=0.6 (Table 9 omits this, yet the rho=0.6 scaling claim needs it)
- Grid-b sweep for low b values (b=0.1/0.2/0.3) with multiple seeds (only seed42 partially reported)
- Statistical significance tests for the primary comparison (adaptive vs grid-best, paired across seeds)
- Adaptive dual-constrained at rho=0.6 with multiple seeds
- Clean baseline (rho=0, no contamination) to establish the ceiling and quantify how much of the gap is closed
- Larger batch size (32, 64) to test whether the method's benefit persists when micro-batch statistics are more reliable
- Wall-clock overhead measurement of bisection search at scale

**Preliminary Score**: 3/6 (Weak Reject)

**Confidence**: 4/5

The fundamental problem is that the experimental results contradict the paper's core narrative. ESS-only outperforms dual-constrained, meaning the alpha_eff quality floor -- the paper's primary methodological contribution -- actively hurts performance. The paper could potentially be reframed as "ESS-only adaptive b* as a tuning-free practical heuristic," but that would require dropping the dual-constraint framing, the minimum intervention principle, and the alpha_eff theoretical apparatus -- essentially a different paper. Additionally, effect sizes are marginal and the most critical comparisons lack multi-seed validation. The experimental coverage is broad but shallow where it matters most.