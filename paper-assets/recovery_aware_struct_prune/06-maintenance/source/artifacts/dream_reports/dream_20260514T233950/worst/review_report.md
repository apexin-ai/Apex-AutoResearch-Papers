---
dream_id: dream_20260514T233950
tier: worst
overall_score: weak reject
timestamp: 2026-05-15T00:30:16.139415+00:00
---

# Dream Review Report: "When Does Structured Pruning Kill Reasoning?"

**Dream ID:** 20260514T233950
**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-15

---

## Reviewer Assignments

- **R1 (Methods + Experiments):** Score 3/6 (Weak Reject), Confidence 4/5
- **R2 (Novelty + Related Work):** Score 2/6 (Reject), Confidence 4/5

---

## R1 Review: Methods & Experiments

### Summary
The paper conducts a systematic empirical study of structured pruning on DeepSeek-R1-Distill-Qwen-7B, comparing four pruning methods across three sparsity levels with SFT and SFT+GRPO recovery. All proposed hypotheses (CKA predicts recoverability, RASP enables superior recovery, GRPO differentially benefits CKA-pruned models) are falsified. The paper pivots to a negative-result framing, reporting that structured pruning catastrophically damages reasoning and that CKA overlap is a reliable but non-predictive metric.

### Strengths
- **Comprehensive experimental design.** 14 planned experiments covering post-prune eval, multi-seed robustness, recovery pipeline, scoring ablation, CKA regression, interaction tests, multi-sparsity, and cross-benchmark evaluation. This is thorough for an empirical study.
- **Rigorous statistical methodology.** Mixed-effects regression with proper covariates and random effects (ICC=0.73), McNemar's test for pairwise significance, 2×2 ANOVA for interaction testing, 95% CIs on primary results. Above average for ML papers.
- **Honest reporting of negative results.** CKA non-predictivity (β=0.08, p=0.12), GRPO marginality (~5pp uniform), and no pruning×recovery interaction (p=0.54) are all transparently reported rather than suppressed.
- **Cross-benchmark dissociation is informative.** MMLU 76.8% retention vs MATH-500 30% retention provides a concrete, actionable insight about what structured pruning destroys.
- **Full evaluation on GSM8K** (1319 samples with CIs) rather than relying on subsampled pilot results.

### Weaknesses
- **The proposed method (RASP) is outperformed by an external baseline (GRASPrune).** GRASPrune achieves 0.477 recovery ratio vs RASP's 0.406. The paper's own contribution is not the best performer on its own benchmark, which is unusual for a methods paper and awkward even for a negative-result paper.
- **Multi-seed variance (SD=6.2pp) undermines most pairwise method comparisons.** With only 3 seeds and a 12.3pp range, the RASP–Standard gap at the worst seed (8.2pp) is comparable to the RASP–Bonsai gap (2.9pp) and RASP–Gradient-only gap (2.3pp). Many comparisons in Table 1 are not statistically robust against seed variation. Only Table 1 entries for Standard, RASP, and Baseline have CIs reported; the others (Magnitude, Gradient, Bonsai, GRASPrune) lack uncertainty estimates.
- **Missing unstructured pruning baseline.** The paper's headline claim contrasts with Self-Healing's 95% recovery at 25% unstructured sparsity, but never directly runs unstructured pruning on the same model. This makes the comparison indirect and potentially confounded by model-specific factors.
- **No inference speedup measurements.** Structured pruning's primary practical advantage is hardware speedup. The paper never measures actual wall-clock improvement, making the practical motivation hollow.
- **Single recovery hyperparameter configuration.** SFT lr=2e-5, 3 epochs; GRPO 2000 steps, group size 8, KL=0.04. No exploration of whether different hyperparameters (especially more aggressive SFT or longer GRPO) could improve recovery. The paper acknowledges this but it limits the strength of the "GRPO is marginal" conclusion.
- **No α sensitivity analysis for RASP.** The compound scoring S(h)=I(h)×(1-F(h))^α uses an α parameter that is never ablated. If α is poorly tuned, the CKA null result may reflect suboptimal use of the CKA signal rather than its inherent non-predictivity.
- **CKA calibration set is small (256 samples).** While CKA split-half reliability is high (ρ=0.92), the 256-sample calibration may still introduce systematic bias. The paper shows rank correlation with 512 and 1024 samples (0.89, 0.95) but does not test whether using 1024 samples for actual pruning changes outcomes.

### Questions to Authors
1. What is the α value used in RASP, and how sensitive are results to it? An α ablation (e.g., 0.5, 1.0, 2.0) would clarify whether CKA non-predictivity is inherent or an artifact of α choice.
2. Can you run unstructured pruning at 20% and 25% on the same model to directly calibrate the structured-unstructured gap?
3. Why are CIs missing for Magnitude-only, Gradient-only, Bonsai, and GRASPrune in Table 1? Were these single-seed results?
4. What happens if the per-layer 40% floor is removed from RASP? The ablation should isolate whether RASP's advantage is from the CKA signal or the floor constraint.
5. What are the actual inference speedups (latency, throughput) at 20% structured sparsity?
6. The mixed-effects regression (Table 5) uses N=224 heads — are these all from a single pruning run (seed 42)? If so, how robust is the ICC=0.73 across seeds?

### Missing Experiments
- Unstructured pruning baseline on the same model (critical for the Self-Healing comparison)
- α sensitivity ablation for RASP
- Per-layer 40% floor ablation (RASP without floor vs with floor)
- Sub-20% sparsity exploration (10%, 15%) to find the transition boundary
- Multi-seed evaluation for all methods (not just RASP)
- Inference speedup benchmarking
- At least one additional model (non-distilled reasoning model)

### Score: 3/6 (Weak Reject) | Confidence: 4/5

---

## R2 Review: Novelty & Related Work

### Summary
The paper reports that structured pruning at 20% sparsity causes catastrophic reasoning collapse on a distilled reasoning model, that CKA functional overlap does not predict per-structure recoverability, and that GRPO adds only marginal benefit over SFT for recovery. It frames these as negative results that "correct" the optimistic narrative from Self-Healing (2025) on unstructured pruning recovery.

### Strengths
- **Addresses a timely practical question.** Understanding whether structured pruning preserves reasoning in deployed models like DeepSeek-R1-Distill is directly useful.
- **Cross-benchmark dissociation is genuinely informative.** MMLU 76.8% retention vs MATH-500 30% retention provides a concrete insight about the selective vulnerability of reasoning chains.
- **Honest null results.** CKA non-predictivity and GRPO marginality are reported transparently.
- **Multi-method comparison.** Four pruning methods prevent single-method bias.
- **Statistical methodology is above average.** Mixed-effects regression, ICC, McNemar's test, interaction analysis.

### Weaknesses
- **The core finding ("structured pruning is harder than unstructured") confirms conventional understanding.** The pruning community has long known that removing entire structural units is far more destructive than removing individual weights. The paper does not adequately argue why this expected finding constitutes a sufficient contribution.
- **No surviving positive contribution.** Every proposed hypothesis was falsified: CKA non-predictive, RASP not best, GRPO marginal, no pruning×recovery interaction. A negative-result paper must compensate with deep mechanistic insight, which is lacking here.
- **Insufficient mechanistic analysis.** ICC=0.73 for layer-level effects is the most interesting finding but is not explored: which layers? What properties distinguish sensitive from robust layers? This is where the "functional analysis" title promises content the paper does not deliver.
- **Single distilled model severely limits generalizability.** Distilled models have compressed redundancy, making them inherently more pruning-sensitive. Claims about "structured pruning killing reasoning" cannot generalize from one distilled model.
- **Self-Healing comparison is not apples-to-apples.** Structured vs unstructured pruning are fundamentally different operations; showing they have different outcomes does not "contradict" Self-Healing — it confirms a known distinction. The framing overstates the comparison.
- **GRASPrune advantage is underexplored.** GRASPrune's 47.7% recovery (vs RASP 40.6%) is an interesting positive finding buried inside the negative framing. Why does it work better? Rescale compensation? Learned gates? Per-channel granularity?
- **Reference list is inadequate.** 12 citations is far too thin for a paper at the intersection of structured pruning, reasoning models, and recovery. A thorough survey requires 25-35 references.

### Related Work Gaps
- No citation of function-aware pruning methods (FANG, FuncNet) directly relevant to the "functional analysis" framing
- No citation of alternative recovery paradigms for reasoning (RAC — chain-of-thought reconstruction)
- Missing pruning-aware tuning methods (PAT, RestoreLCC) relevant to the recovery analysis
- No reference to structured pruning's effect on test-time scaling ("Doing More With Less")
- No reference to width vs depth pruning for reasoning ("From LLMs to LRMs")
- Missing pruning recovery scaling laws (P-squared Law)
- The reference list should be expanded significantly to meet venue standards

### Novelty Assessment
**Insufficient for a top venue in current form.** The delta over prior work reduces to: (a) structured is harder than unstructured for reasoning (expected), (b) CKA doesn't predict recoverability (null result without compensating insight), (c) GRPO adds little over SFT at this sparsity (narrow). The cross-benchmark dissociation is the most novel element but receives insufficient analytical depth.

For a negative-result paper to succeed at a top venue, it must either overturn a widely-held belief (this does not), provide deep mechanistic understanding (insufficiently developed), or offer novel practical guidance (recommendations are generic).

### Questions to Authors
1. Can you provide results on at least one non-distilled reasoning model? The distillation confound is severe.
2. What is the effective capacity reduction (FLOPs, parameter count in reasoning-critical components) for 25% unstructured vs 20% structured? Without this, the Self-Healing contrast is misleading.
3. Why does GRASPrune recover better? An ablation isolating rescale compensation, learned gates, and granularity would add significant value.
4. Can you provide a per-layer sensitivity breakdown? Which layers are most critical and why? This would fulfill the "functional analysis" promise.
5. Have you tested below 20% sparsity (10%, 15%)? The transition boundary is far more informative than the 20-30% collapse range.
6. The paper describes "four pruning methods" but lists six (Standard, Magnitude, Gradient, RASP, GRASPrune, Bonsai). Resolve this inconsistency.
7. The title asks "When does structured pruning kill reasoning?" but the answer is "always, at ≥20% on this one model." Can you deliver on the conditional analysis the title promises?

### Score: 2/6 (Reject) | Confidence: 4/5

---

## Roundtable Discussion

### Step 1: Independent Positions
- **R1 (3, Weak Reject):** Acknowledges experimental rigor and comprehensive design, but concerned about statistical reliability (seed variance), missing baselines (unstructured pruning), and the proposed method being outperformed by GRASPrune.
- **R2 (2, Reject):** Focuses on insufficient novelty — the core finding confirms conventional understanding, all hypotheses are falsified with no compensating insight, related work coverage is inadequate, single distilled model limits generalizability.

### Step 2: Cross-Sharing
R1 acknowledges R2's novelty concern: the "structured is harder" finding is indeed expected. R2 acknowledges R1's point about experimental rigor: the statistical methodology is genuinely above average for the field. Both agree the cross-benchmark dissociation (MMLU vs MATH-500) is the most publishable finding but is underdeveloped.

### Step 3: Convergence
Both reviewers converge on the following assessment:

**Points of agreement:**
1. **Single model is a critical limitation** — especially for a negative-result paper making broad claims. A distilled model's pruning sensitivity may not represent reasoning models generally.
2. **Cross-benchmark dissociation is the strongest finding** — but needs much deeper analysis (per-layer breakdown, mechanistic explanation, additional models) to stand as a primary contribution.
3. **CKA null result is clean but mechanistically shallow** — "CKA is reliable but non-predictive" is well-demonstrated but the paper does not sufficiently explore WHY (layer-level ICC=0.73 is noted but not analyzed).
4. **Missing unstructured baseline is a significant gap** — the headline comparison to Self-Healing is indirect and potentially misleading without running unstructured pruning on the same model.
5. **RASP being outperformed by GRASPrune** weakens the paper's contribution regardless of framing.
6. **Practical recommendations are generic** — "don't prune beyond 20%", "use SFT", "evaluate on reasoning benchmarks" are not insights that require this paper to establish.
7. **Related work coverage is inadequate** — 12 citations is far below venue standards.

**Points of disagreement:**
- R1 gives more credit to experimental thoroughness and honest reporting (Score 3); R2 weighs novelty deficit more heavily (Score 2). After discussion, both agree the paper falls below the acceptance threshold but disagree on severity.

### Step 4: Consolidated Assessment

**Overall Score: 3/6 (Weak Reject)**

This paper presents a thorough empirical study with above-average statistical methodology, but falls short of the acceptance bar for a top ML venue on three grounds:

**1. Insufficient novelty.** The core finding — structured pruning is far more destructive than unstructured for reasoning — confirms the expected behavior rather than overturning a belief. Every proposed hypothesis (CKA predicts recoverability, RASP enables superior recovery, GRPO differentially benefits CKA-pruned models) was falsified, leaving no positive contribution. The paper would need substantially deeper mechanistic analysis of the layer-level sensitivity finding (ICC=0.73) or results on additional models to compensate.

**2. Key experimental gaps.** No direct unstructured pruning comparison on the same model (making the Self-Healing contrast indirect), no α sensitivity ablation for RASP (leaving open whether CKA non-predictivity is inherent vs. artifact), no inference speedup measurements (undermining practical motivation), CIs missing for 4 of 7 methods in Table 1, only 3 seeds for robustness analysis.

**3. Generalizability concerns.** Single distilled model (known to have compressed redundancy). Claims about "structured pruning killing reasoning" cannot generalize without testing non-distilled reasoning models. The paper acknowledges this limitation but does not address it.

**What would raise the score:**
- Add at least one non-distilled reasoning model (e.g., Qwen-2.5-7B-Instruct or a smaller non-distilled model)
- Run unstructured pruning at 20% and 25% on the same model for direct comparison
- Deep per-layer sensitivity analysis: identify which layers are critical, correlate with architectural properties, explain mechanistically why layer position dominates over head-level CKA
- Expand related work to 25+ references, engaging with function-aware pruning and alternative recovery methods
- α ablation for RASP and per-layer floor ablation
- Inference speedup benchmarking
- Sub-20% sparsity exploration to map the safe-to-catastrophic transition

**Strongest elements worth preserving:**
- Cross-benchmark dissociation (MMLU 76.8% vs MATH-500 30%) — this selective destruction finding is genuine and useful
- CKA reliability + non-predictivity combination — a clean negative result (reliable metric, no predictive power)
- Statistical methodology (mixed-effects regression, ICC, interaction testing) — a model for how empirical pruning studies should be conducted
- Sparsity cliff characterization (nonlinear degradation 20→25→30%) — practical value for practitioners

**Verdict:** The paper's experimental execution is solid, but the contribution — primarily confirming expected behavior with negative results on a single model — is insufficient for acceptance at a top venue. A major revision addressing the model diversity, mechanistic depth, and missing baselines could elevate this to borderline-accept territory, likely as a Findings paper rather than main conference.

---

## Experiment Coverage Check

All 14 planned experiments from the design document are represented in the paper:
- Plans 001-004 (GSM8K eval, SFT, GRPO, final eval): Tables 1, 3 ✓
- Plan 005 (GRASPrune): Tables 1, 3 ✓
- Plan 006 (Multi-seed): Table 2 ✓
- Plan 007 (Scoring ablation): Table 4 ✓
- Plan 008 (CKA regression): Table 5 ✓
- Plan 009 (Interaction test): Table 7 ✓
- Plan 010 (25% sparsity): Table 8 ✓
- Plan 011 (30% probe): Table 8 ✓
- Plan 012 (Extended eval): Table 9 ✓
- Plan 013 (Bonsai): Tables 1, 3 ✓
- Plan 014 (CKA reliability): Table 6 ✓

Coverage is complete. However, the paper could benefit from additional experiments not in the original design (unstructured baseline, α ablation, sub-20% sparsity, second model).
