---
round: 0
review_mode: 
overall_score: 2.0 Resubmit next cycle (worst) / 3.5 Borderline Conference (best) / 2.5 Borderline Findings (median)
timestamp: 2026-05-22T05:22:32.443400+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 2 Consolidated Review Report — Worst Scenario

**Project**: gated_mfrm_judge_bias
**Venue**: EMNLP 2026 (via ARR)
**Round**: 2 (worst scenario supplement)
**Dream**: 20260521T215715 / worst
**Paper**: "How Much Contamination Are We Actually Correcting? A Joint Psychometric Audit of LLM-as-a-Judge Evaluation"
**Date**: 2026-05-22

---

## Summary

G-MFRM 三阶段 pipeline 在真实数据上得到 **calibrated null finding**：当前 benchmark contamination 可忽略（median c_n ≈ 0.15-0.18），G-MFRM 与 MFRM/Sequential/CyclicJudge+Discard 表现相同（所有 τ = 0.85, Δτ < 0.02, p > 0.18），Stage 2 e_i pipeline 的消融显示其对排名质量零贡献（uniform e_i: τ = 0.84 vs full pipeline: τ = 0.85）。论文将结果重新定位为"当前 benchmark 值得信赖"+ G-MFRM 作为监控基础设施。合成实验确认方法在 c_n ≥ 0.7 时有效（38.2% RMSE degradation from OVB at ρ = 0.6）。

---

## Scores

| Reviewer | Focus | Soundness | Excitement | Overall | Confidence |
|----------|-------|-----------|------------|---------|------------|
| R1 | Methods & Experiments | 2/5 | 2/5 | 2.0 | 4/5 |
| R2 | Novelty & Related Work | 2.5/5 | 1.5/5 | 2.0 | 4/5 |
| **Consensus** | | **2/5** | **2/5** | **2.0 (Resubmit next cycle)** | |

---

## Strengths

1. **Intellectual honesty exemplary**: p = 0.073/0.23 直接报告，88%/78% CI coverage 坦承，null finding 不隐藏——R1: "this level of intellectual honesty is rare and commendable"。
2. **OVB theory correct and independent of data outcome**: FWL theorem 应用正确，500/300-configuration Monte Carlo 验证。理论贡献与实证结果独立。
3. **Comprehensive experimental battery**: 16 tables, 12 experiments（convergence diagnostics, 8 baselines, error propagation, exposure ablation, judge count sensitivity, cross-benchmark, adversarial, facet fit）。
4. **Graceful degradation verified**: G-MFRM θ̂ within 0.02 of MFRM θ̂ when c_n ≈ 0 (r = 0.987)。Model does no harm。
5. **Error propagation analysis**: breakeven σ ≈ 0.28-0.38 量化了 safety margin。

---

## Weaknesses — Critical (R1+R2 strong consensus)

### [C1] Underpowered null finding — the paper's most fundamental inferential problem
- Post-hoc power = **0.12** for Δτ = 0.02, N = 22 models
- 88% probability of missing a true effect → null finding is underdetermined
- No equivalence test (TOST) to formally bound contamination effect below practical significance
- R1: "the null finding could mean contamination is negligible, OR the study is too underpowered to detect it"
- R2: "formal power analysis is absent — readers cannot interpret the null"
- **Consensus action**: TOST with δ = 0.03 + report minimum detectable c_n + increase N ≥ 50 models if possible

### [C2] MCMC convergence failure for c_n — the paper's core novel parameter
- R̂ = 1.12 (> 1.10 threshold), ESS = 79 (< 400 recommended), 23 divergent transitions
- 68% of models have c_n posterior dominated by prior (Half-Cauchy), not data-informed
- R2 key insight: **prior-dominated c_n means "uninformative finding" not "null finding"** — the model didn't learn contamination information, it doesn't mean contamination is absent
- θ and d converge well (R̂ ≤ 1.04, ESS ≥ 240) — problem is specific to c_n
- This directly undermines the "monitoring infrastructure" claim: monitoring is built on the most unreliable parameter
- **Consensus action**: Reparameterize; try spike-and-slab or horseshoe prior; increase warmup/chains

### [C3] e_i pipeline demonstrably adds nothing
- Table 8 ablation: uniform e_i (no estimation) τ = 0.84, full pipeline τ = 0.85
- Δτ = 0.01 within noise — entire Stage 2 contributes zero to ranking quality
- R1 correction: breakpoint σ ≈ 0.28 (not 0.35 as initially cited by R2) — G-MFRM degrades even earlier than reported
- Real e_i quality: ρ = 0.47 with ground truth, only 43% items high-confidence → real noise likely near/above breakpoint
- R1+R2 consensus: reframe as **"currently dormant infrastructure"** not "essential component"

### [C4] 78% CI coverage — systematic overconfidence
- Bayesian credible intervals 17% overcoverage gap (78% vs 95% nominal)
- Low c_n models have worst coverage (unreported but inferred from convergence pattern)
- Per-model diagnostic claims ("Model X has c_n = 0.72 [0.38, 1.12]") cannot be trusted at face value
- Combined with prior-dominated posteriors: **c_n estimates are both poorly explored AND overconfident**

### [C5] 36.4% c_n misfit rate
- 8/22 models with outfit > 1.3 — rank-1 assumption c_n·e_i violated for >1/3 of parameters
- Section 5.10 adversarial analysis admits item-specific contamination "is not well-approximated by a single c_n per model"
- Paper's own evidence contradicts its modeling assumption

### [C6] Weak construct validity
- ConStat ρ = 0.32 [0.04, 0.54] — CI includes near-zero, explains only ~10% variance
- Cross-benchmark c_n ρ = 0.28-0.42 — too low for "stable model-level trait" (should > 0.7)
- c_n likely reflects noise or benchmark-specific artifact rather than true contamination susceptibility

### [C7] "Monitoring infrastructure" reframing lacks novelty and validation
- (a) No comparison to simpler monitors (ConStat-as-monitor, LogProber-as-monitor)
- (b) "Contamination will grow → G-MFRM value increases" is unfalsifiable speculation
- (c) "Monitoring infrastructure" is application direction, not EMNLP research contribution
- (d) Adversarial detection: 35% rate for subtle attacks, 14% FPR — not compelling

### [C8] No positive-control benchmark
- Only evaluates on MT-Bench/Arena-Hard/WildBench where contamination is apparently low
- No known-contaminated benchmark (MMLU, GSM8K) as positive control
- Without positive control, null finding could reflect measurement insensitivity rather than true absence
- R1+R2 consensus: **most high-leverage single fix** — could simultaneously validate method sensitivity AND current-benchmark cleanliness

---

## Weaknesses — Should-Fix

**[S1]** Missing contamination avoidance literature (LiveBench, SEAL, private benchmarks, Arena dynamic prompts) — avoidance strategies may explain why current contamination is low, further weakening G-MFRM's value proposition

**[S2]** Missing null-result methodology references (Dodge et al. 2019, Rogers et al. 2020) — if null finding is contribution, it needs methodological anchoring in the null-results tradition

**[S3]** Narrative reads as post-hoc reframing (propose method → null result → reframe as monitoring) — if monitoring is primary contribution, title/Introduction must establish it upfront

**[S4]** Reproducibility concerns: reference variant generation method unspecified, spline correction details missing, MCMC hyperpriors incomplete, code/data release aspirational not committed

**[S5]** Page count likely exceeds 8-page limit (~9.5-10 pages main text)

**[S6]** 16 tables excessive density — Tables 3 (synthetic) and 7 (error propagation) could move to appendix

---

## Reviewer Consensus (Cross-Sharing)

### R2 → R1 Cross-Response
All 6 R1 weaknesses: **[AGREE]**
- Supplemented W1 with spike-and-slab/horseshoe prior suggestion
- Supplemented W2 with "currently dormant infrastructure" framing
- Supplemented W3 with TOST as more direct solution than power analysis alone
- Corrected R1 on WildBench judge count ([REBUT] minor — worst uses 8 judges not 6)
- Identified causal chain: weak contamination → flat likelihood → convergence failure → prior-dominated → poor coverage → weak validation → no improvement → forced reframe

### R1 → R2 Cross-Response
All 5 R2 weaknesses: **[AGREE]**
- Corrected R2-M1 RMSE (0.42 not 0.55) — strengthens R2's point
- Corrected R2-M2 breakpoint (σ≈0.28 not 0.35) — makes problem more severe
- Supplemented R2-M2 with CyclicJudge+Discard Occam's razor argument (same τ=0.85, no MCMC)
- Supplemented R2-M3 with Section 5.10 self-contradiction (adversarial admits rank-1 inadequacy)
- R1 adds: θ convergence is fine (R̂≤1.04) → rankings reliable → but this means c_n (monitoring core) is specifically unreliable

### Consensus Summary
**Perfect agreement**: R1 and R2 independently give 2.0, identify same 6-8 interrelated problems, agree on all cross-response items. Zero substantive divergence.

**Causal chain (R2 formulation, R1 endorsed)**:
```
Weak real contamination (c_n ~0.18)
  → flat likelihood for c_n
    → MCMC convergence failure (R̂=1.12, 23 divergent)
      → prior-dominated posteriors (68% models)
        → poor CI coverage (78%)
          → weak external validation (ρ=0.32)
            → no ranking improvement
              → forced "monitoring" reframe
                → speculative/unvalidated contribution
```

---

## Questions for Authors

1. **Minimum detectable c_n**: Given N=22 models, e_i noise, and current MCMC configuration, what is the minimum c_n G-MFRM can reliably detect (80% power, α=0.05)?
2. **TOST equivalence**: Can you run a TOST at δ=0.03 to formally establish ranking equivalence?
3. **Positive control**: Why not evaluate on MMLU/GSM8K where contamination is known to exist?
4. **Spike-and-slab prior**: Would a spike-and-slab prior for c_n improve convergence by explicitly modeling the zero-inflated structure?
5. **Monitoring comparison**: How does G-MFRM-as-monitor compare to ConStat-as-monitor in detection sensitivity and cost?
6. **Contamination avoidance**: Given LiveBench and private benchmarks, what is G-MFRM's value proposition for static public benchmarks?
7. **e_i breakpoint**: With real e_i noise likely near σ≈0.28 breakpoint, is Stage 2 already operating in the degradation regime?

## Missing References

- Dodge et al. (2019) — "Show Your Work" (negative results reporting)
- Rogers et al. (2020) — "Changing the World by Changing the Data"
- White et al. (2024) LiveBench
- Chiang et al. (2024) Chatbot Arena methodology
- SEAL / private held-out benchmarks
- Eckes (2011), Patz et al. (2002), Fox & Glas (2001) — MFRM+DIF
- Albert (1992), Fox (2010) — Bayesian IRT
- Li et al. (2024) Arena-Hard
- Polo et al. (2024) TinyBenchmarks
- Golchin & Surdeanu (2023), Shi et al. (2023) — known contamination evidence

## External Review
**Status**: Not requested (project not configured).

## Visual Layout Check
**Status**: Not started (`review_paper_pdf_path` not configured).

---

## Overall Assessment: 2.0 — Resubmit Next Cycle

论文包含正确的理论贡献（OVB observation）和有原则的方法论（G-MFRM），合成数据验证方法在强污染下有效。但真实数据执行有六个互相关联的问题，构成致命的 causal chain：(1) MCMC 收敛失败导致 c_n 估计不可靠，(2) e_i pipeline 零贡献，(3) null finding underpowered (power=0.12) 且无 equivalence test，(4) 36.4% c_n misfit，(5) 78% CI coverage，(6) ConStat ρ=0.32 + cross-benchmark ρ=0.28-0.42 的 weak construct validity。"Calibrated null finding" 叙事建立在一个缺乏灵敏度和可靠性的测量工具之上。

### Score Path (R1 formulated, R2 endorsed)

**→ 3.0 (Findings)** if authors:
1. Fix c_n convergence (spike-and-slab prior, reparameterize, longer chains)
2. Add TOST equivalence test to formally bound contamination effect
3. Add positive-control benchmark (MMLU/GSM8K) — **most high-leverage single fix**
4. Reframe e_i pipeline as future-proofing, not current contribution

**→ 1.5 (Resubmit after next cycle)** if:
- Convergence issues shown to invalidate c_n posteriors entirely
- Or positive control also fails to detect known contamination

---

## Cross-Scenario Summary (all three scenarios)

| Scenario | c_n median | Δτ vs best baseline | p-value | ConStat ρ | R1 | R2 | Consensus |
|----------|-----------|---------------------|---------|-----------|----|----|-----------|
| **Best** | ~0.95-1.18 | +0.04-0.05 | 0.003 | 0.78-0.82 | 3.5 | 3.5 | 3.5 Borderline Conference |
| **Median** | ~0.48 | +0.02 | 0.073 | 0.52 | 2.5 | 2.5 | 2.5 Borderline Findings |
| **Worst** | ~0.18 | -0.01-0.00 | 0.23 | 0.32 | 2.0 | 2.0 | 2.0 Resubmit |

**核心洞察**: 方法论一致，novelty 弱点一致，唯一变量是真实 contamination 量级。论文命运完全由数据决定。

**关键门槛**:
- c_n > 0.8 + p < 0.05 → 3.0-3.5 (Findings to Borderline Conference)
- c_n ≈ 0.3-0.5 + p < 0.10 → 2.5-3.0 (requires power analysis + positive control)
- c_n < 0.3 + p > 0.10 → 2.0 (resubmit with positive control + TOST)

**Confidence**: Very high — R1 and R2 independently converge to identical scores across all three scenarios with zero substantive divergence.

---

*Review Director, Round 2 worst-scenario supplement, 2026-05-22.*
*Reviewers: R1 (Methods, 4/5), R2 (Novelty, 4/5). Both cross-responses completed. Perfect consensus.*