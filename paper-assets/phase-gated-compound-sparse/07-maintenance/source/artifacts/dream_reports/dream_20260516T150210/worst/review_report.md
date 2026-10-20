---
dream_id: dream_20260516T150210
tier: worst
overall_score: borderline reject (2.5/5)
timestamp: 2026-05-16T16:04:00.643948+00:00
---

# Dream Review Report: "Phase-Dependent Compound Sparsity Severity in Reasoning LLMs"

**Venue:** EMNLP 2026 (via ACL Rolling Review)
**Review mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-16

---

## Venue Calibration

EMNLP 2026 uses ACL Rolling Review with three scoring dimensions:
- **Soundness** (1–5): methodological rigor and validity of claims
- **Excitement** (1–5): subjective impact and novelty
- **Overall Assessment** (1–5, half-point increments): 5 = award-worthy (top 2.5%), 4–4.5 = strong accept, 3–3.5 = accept/borderline accept, 2–2.5 = borderline reject, 1–1.5 = reject
- **Confidence** (1–5)
- Acceptance rate: ~22%

Guidelines sourced from [ARR Review Form](http://aclrollingreview.org/reviewform) and [ARR Reviewer Guidelines](http://aclrollingreview.org/reviewerguidelines).

---

## Paper Summary

The paper investigates compound sparsity — the simultaneous application of attention head pruning and KV cache eviction — in reasoning LLMs. The core finding is that compound interaction severity is **phase-modulated**: it increases monotonically from high-sparsity to low-sparsity reasoning phases, with paired median difference growing from 0.39 to 8.48 on MATH-500 (Spearman ρ = 1.0, n = 500, two Qwen2 models). This phase gradient replicates across 3 models, 2 architectures (Qwen2, LlamaForCausalLM), and 2 mathematical reasoning benchmarks (MATH-500, GSM8K). Strategy modulation (importance vs. random eviction) is architecture-dependent: 16.6× gradient ratio on Qwen2 vs. 2.4× on LLaMA. Discrimination collapse (Gini/CV decline of importance scores under pruning) is identified as a correlational mechanism. GPQA experiments (Appendix A) show 0/10 significant conditions, establishing a scope boundary at mathematical reasoning.

**Three claimed contributions:**
1. Phase gradient universality (dz ≈ 1.0–1.2, ρ = 1.0 across all models/benchmarks)
2. Architecture-dependent strategy modulation (Qwen2 strong, LLaMA attenuated)
3. Discrimination collapse mechanism (Gini/CV decline, cross-model consistent)

---

## Experiment Coverage Assessment

The review context specifies 5 planned experiments:

| # | Experiment | Status in Paper |
|---|-----------|-----------------|
| 1 | LLaMA n=250 cross-architecture (8 conditions) | **Covered** — Table 2, Table 4 (n=244 valid) |
| 2 | GPQA DeepSeek importance sweep (4 levels) | **Covered** — Appendix A, Table 6 |
| 3 | GPQA Qwen importance sweep (4 levels) | **Covered** — Appendix A, Table 6 |
| 4 | GPQA random masking controls (DS s025/s030) | **Covered** — Appendix A, Table 6 |
| 5 | GPQA cross-task synthesis | **Covered** — Table 5, Section 4.5 |

All 5 planned experiments are represented. Coverage is complete relative to the experiment design.

---

## Reviewer 1 (R1): Methods + Experiments

### Strengths

1. **Rigorous paired statistical design.** Wilcoxon signed-rank tests, Bonferroni correction (k=4), bootstrap CIs (B=10,000), Cohen's dz for effect sizes, and Spearman ρ for dose-response — all appropriate for non-normal, heavy-tailed data. The per-problem paired design controls for problem-level confounds (difficulty, length, topic).

2. **Transparent reporting of negative results.** GPQA failure (0/10 significant, direction reversals), Qwen entropy reversal (inconsistent across models), mitigation pilot below pre-registered gate (18% < 30%), LLaMA weak strategy interaction — the paper does not overstate its claims. This honesty is commendable and rare.

3. **Comprehensive multi-dimensional analysis.** Systematic variation across model (3), strategy (2), sparsity (4), benchmark (3), and architecture (2) provides a clear map of where the finding holds and where it breaks down.

### Weaknesses

1. **Head pruning ratio `p` is never explicitly specified.** Section 3.1 introduces `p` as a parameter ("attention head pruning at ratio p") but never states its value. The paper varies KV eviction sparsity s ∈ {0.15, 0.20, 0.25, 0.30} and reports results across these levels, but whether `p` is fixed, co-varies with `s`, or takes some other value is unclear. This is a critical experimental parameter that must be specified for reproducibility.

2. **Circular dependency confound.** Head pruning alters the attention distribution from which KV importance scores are computed. The observed "compound interaction" may substantially reflect scoring degradation rather than an intrinsic property of compound sparsity. Without a scoring-independent eviction baseline (e.g., recency-based), this confound cannot be disentangled. The paper acknowledges this in Limitations but does not test alternatives.

3. **Phase segmentation validated on only one model/benchmark.** The kappa=0.88 agreement with `<think>` markers is reported for DeepSeek on a limited sample. Qwen2.5-7B lacks `<think>` delimiters, so there is no direct validation that quantile-based segmentation captures meaningful reasoning stages for that model. The segmentation is also performed on the dense model's attention patterns — whether these assignments remain valid under sparsity is untested.

4. **Discrimination collapse mechanism is correlational and explanatorily incomplete.** Gini/CV decline is consistent across models, but both strategies show near-identical Gini drops while severity diverges by 15–17×. The mechanism identifies a correlate but cannot explain the magnitude of the effect. No causal intervention (e.g., artificially restoring discriminability) is attempted.

5. **Spearman ρ = 1.0 on 4 data points is misleading.** With only 4 sparsity levels, any monotone ordering achieves ρ = 1.0 (permutation p ≈ 0.042, barely significant). The abstract and introduction headline this statistic, which overstates its informativeness. The Jonckheere-Terpstra test is more appropriate but less prominently reported.

6. **Generation-time confound.** It is unclear whether the Interaction Index is computed on teacher-forced perplexity from dense-model generations or on autoregressive generations under the sparse model. If the latter, phase assignments from dense attention patterns may be misaligned with the sparse model's actual reasoning trajectory.

### Questions for Authors (R1)

1. What is the head pruning ratio `p`? Is it fixed across all conditions, or does it co-vary with the KV eviction sparsity `s`?
2. Is II computed on dense-model-generated token sequences (teacher-forced) or sparse-model autoregressive generations?
3. Have you considered testing recency-based or random-fixed-pattern eviction to isolate the circular scoring confound?
4. What fraction of the severity divergence does discrimination collapse quantitatively account for?
5. Can you validate the phase segmentation on Qwen2.5-7B using an independent criterion (e.g., reasoning structure annotation)?

### R1 Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 3.5 | Core methodology adequate; paired design and nonparametric stats appropriate. Deducted for: unspecified `p`, circular dependency confound, limited segmentation validation, correlational mechanism. |
| Excitement | 3.0 | Useful empirical observation for compression community, but practical implications unrealized (mitigation failed), generalization narrow (math only, 7B only), and finding somewhat expected given prior phase-dependent pruning work. |
| Overall | 3.0 | Solid empirical work within a narrow scope. Honest about limitations. But: unspecified critical parameter, unresolved confounds, no actionable outcome, limited domain. |
| Confidence | 4 | Familiar with KV cache compression, head pruning, and statistical methodology. |

---

## Reviewer 2 (R2): Novelty + Related Work

### Strengths

1. **Genuinely new empirical finding in the compound setting.** No prior work has explicitly measured how the interaction between head pruning and KV cache eviction is modulated by reasoning phase. The connection of phase-dependent sensitivity (ThinKV), compound super-additivity (SparK), and score instability (HIES) into one unified characterization is a legitimate scientific contribution.

2. **Exceptional statistical rigor as a standard-setter.** Pre-registered gates, Bonferroni + BH-FDR, Jonckheere-Terpstra for ordered alternatives, honest CI reporting, transparent negative results — this paper could serve as a template for empirical ML methodology.

3. **Clear positioning against prior work.** The differentiation from ThinKV (single-axis phase-aware), SparK (compound but phase-agnostic), and HIES (single-axis collapse) is cleanly stated and legitimate.

### Weaknesses

1. **Title overclaims scope.** "Reasoning LLMs" implies generality across reasoning tasks, but the phenomenon is demonstrated only on mathematical reasoning (MATH-500, GSM8K). GPQA (science reasoning) yields 0/10 significant conditions with direction reversals (Appendix A). Even GSM8K shows attenuated strategy specificity (2.3–3.8× vs. 15–36× on MATH-500). The title should be qualified to "Mathematical Reasoning LLMs" or the abstract must clearly scope the claim upfront.

2. **Novelty is moderate — connecting known dots.** The conceptual ingredients are all established: (a) phase-dependent compression tolerance (ThinKV), (b) compound super-additivity (SparK), (c) importance score collapse (HIES). The contribution is empirically combining and quantifying these in a unified framework. This is legitimate but sits at the intersection of existing ideas rather than opening a fundamentally new direction.

3. **Extremely sparse bibliography.** Only 9 references is far below the norm for an EMNLP main submission (typically 30–50). Major missing lines of work include:
   - Broader structured pruning literature (layer pruning, lottery ticket hypothesis for compound effects)
   - Chain-of-thought analysis literature (reasoning phase dynamics, information flow in CoT)
   - Rate-distortion / information-theoretic compression framing
   - Other compound compression works (EvicPress, PM-KVQ)
   - "Thinking Tokens are Information Peaks" (NeurIPS 2025) — directly relevant to phase-dependent behavior but uncited

4. **No actionable outcome.** The pilot mitigation achieved 18% recovery (below 30% pre-registered gate, CI spanning zero). The paper's practical message reduces to "compound sparsity is worse in some phases, but we don't yet know how to exploit this." The "phase-gated analysis framework" is a diagnostic contribution but without demonstrated utility.

5. **Positioning against SparK is slightly straw-man.** The paper claims SparK assumes "interaction magnitude is constant across generation." More accurately, SparK does not analyze temporal variation — it would be more precise to say SparK "does not study temporal dynamics" rather than implying it actively "assumes" uniformity.

6. **Discrimination collapse adds limited novelty over HIES.** HIES (2025) already reports importance score collapse under pruning. The extension to compound settings and phase-modulation is incremental. The paper acknowledges the mechanism is correlational and cannot explain the magnitude gap (identical Gini drops, 15–17× severity divergence).

### Questions for Authors (R2)

1. Given the GPQA null results, would you consider changing the title to "Phase-Dependent Compound Sparsity Severity in Mathematical Reasoning LLMs"?
2. How does the phase segmentation compare to ThinKV's semantic phase boundaries? Have you tested ThinKV-style segmentation as an alternative?
3. The bibliography has only 9 entries. Are you aware of the missing lines of work identified above? A revision should substantially expand the related work.
4. How sensitive are results to the choice of importance metric (cumulative attention scores vs. recency-weighted, SnapKV-style, or learned scores)?
5. Could you provide a theoretical grounding for why compound interaction should be phase-dependent, perhaps via information-theoretic arguments?

### R2 Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 3.5 | Methodology rigorous. Deducted for: circular dependency confound, correlational mechanism, and extremely sparse bibliography suggesting incomplete literature coverage. |
| Excitement | 2.5 | Moderate novelty (connecting known components). Limited domain (math reasoning only). No practical method emerges. Mitigation failed. Not likely to change how compression systems are built. |
| Overall | 2.5 | Well-executed empirical finding with moderate novelty. Domain limitation, thin bibliography, no actionable outcome, and incremental mechanism lower the contribution below the main conference bar. Suitable for Findings. |
| Confidence | 4 | Familiar with KV cache compression, pruning, and reasoning model literature. |

---

## Roundtable: Cross-Review Synthesis

### Step 2: Cross-Sharing — Convergences and Divergences

**Convergences (both reviewers agree):**
1. The core finding (phase-dependent compound severity with monotonic gradient) is valid and well-demonstrated within its scope
2. Statistical methodology is rigorous and sets a high standard
3. Transparent negative result reporting is a significant strength
4. Circular dependency confound (head pruning → degraded importance scores → degraded eviction) is a fundamental limitation
5. Discrimination collapse is correlational and explanatorily incomplete (identical Gini drops, 15–17× severity gap)
6. Title overclaims "Reasoning LLMs" when evidence supports only mathematical reasoning
7. No actionable practical outcome (mitigation failed pre-registered gate)
8. Head pruning ratio `p` is underspecified

**Divergences:**
1. R1 (Soundness 3.5, Overall 3.0) vs. R2 (Soundness 3.5, Overall 2.5) — R2 is more critical of novelty and excitement
2. R1 focuses on generation-time confound; R2 focuses on missing literature
3. R2 identifies the 9-reference bibliography as a major weakness; R1 does not flag this
4. R2 more strongly argues for Findings over main conference

### Step 3: Convergence Discussion

After cross-examination, the reviewers converge on the following positions:

- **Soundness: 3.5/5.** Both agree. Core methodology is adequate but limited by the circular dependency confound, unspecified `p`, correlational mechanism, and limited segmentation validation.

- **Excitement: 3.0/5.** R1 at 3.0, R2 at 2.5, converging to 3.0 (lower half). The finding is useful but not surprising given existing ingredients. Domain limitation and lack of actionable outcome dampen excitement. R2's concern about thin novelty is valid but the systematic cross-model/cross-architecture quantification does add value.

- **Overall: 2.5–3.0/5.** Converge at **2.5** (borderline reject / resubmit). The paper is a careful empirical study with a valid finding, but multiple issues collectively push it below the acceptance threshold for main conference: (1) title overclaims scope, (2) extremely sparse bibliography (9 refs), (3) critical experimental parameter unspecified, (4) no practical outcome, (5) mechanism incomplete and correlational, (6) novelty is moderate (connecting known dots). Could be suitable for Findings with revisions.

### Step 4: Final Consolidated Assessment

---

## Consolidated Scores

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Soundness** | **3.5** | Adequate methodology with notable gaps |
| **Excitement** | **3.0** | Useful characterization, limited impact |
| **Overall Assessment** | **2.5** | Borderline reject — resubmit with revisions |
| **Confidence** | **4** | High confidence in assessment |

---

## Top-Level Strengths

1. **Rigorous statistical framework.** Per-problem paired design, Wilcoxon signed-rank with Bonferroni correction, bootstrap CIs (B=10,000), Cohen's dz effect sizes, Jonckheere-Terpstra dose-response test. This is among the most statistically rigorous empirical ML papers we have reviewed.

2. **Transparent reporting of negative and boundary results.** GPQA failure (0/10 significant, direction reversals), LLaMA weak strategy interaction, Qwen entropy reversal, mitigation pilot below pre-registered gate — the paper consistently reports what did not work alongside what did. This intellectual honesty strengthens credibility.

3. **Systematic cross-model/cross-architecture replication.** The phase gradient is demonstrated across 3 models, 2 architectures, and 2 mathematical benchmarks, with quantitative characterization of where generalization holds (phase gradient direction) vs. where it breaks down (strategy specificity magnitude, domain boundary).

## Top-Level Weaknesses

1. **Critical experimental parameter unspecified.** The head pruning ratio `p` is introduced in §3.1 but its value is never stated. This makes the experiments unreproducible and prevents readers from understanding the actual compression operating point.

2. **Title and framing overclaim scope.** "Reasoning LLMs" implies generality across reasoning tasks, but evidence supports only mathematical reasoning. GPQA (science/graduate-level reasoning) yields 0/10 significant conditions with direction reversals. Even within math, GSM8K shows attenuated effects compared to MATH-500.

3. **Extremely sparse bibliography (9 references).** This is far below EMNLP norms. Major missing areas: structured pruning literature, chain-of-thought analysis (reasoning phase dynamics, information flow), rate-distortion framing, "Thinking Tokens are Information Peaks" (NeurIPS 2025), and additional compound compression works (EvicPress, PM-KVQ).

4. **Unresolved circular dependency confound.** Head pruning degrades the attention scores used for importance-based KV eviction. The compound "interaction" may substantially reflect this circular scoring failure rather than an intrinsic property of compound sparsity. No scoring-independent eviction strategy (recency-based, learned) is tested.

5. **Incomplete and correlational mechanism.** Discrimination collapse (Gini/CV decline) occurs nearly identically under both importance and random strategies, yet severity diverges 15–17×. The mechanism cannot explain the magnitude of the observed effect. No causal intervention is attempted.

6. **No actionable practical outcome.** The pilot mitigation achieved only 18% recovery (below the pre-registered 30% gate, CI spanning zero). The paper cannot recommend concrete deployment strategies.

## Detailed Issues

### Methodology
- **Phase segmentation validation is limited.** Kappa=0.88 agreement with `<think>` markers is shown for one model (DeepSeek) on limited samples. Qwen2.5-7B lacks `<think>` markers, so segmentation validity is unverified. Dense-model phase assignments may not be valid under sparsity.
- **Spearman ρ = 1.0 on 4 points is misleading.** Any monotone ordering of 4 items achieves ρ = 1.0 (permutation p ≈ 0.042). This statistic is prominently featured in the abstract and introduction but has minimal informativeness.
- **Generation-time confound.** It is unclear whether II is computed on dense-model or sparse-model token sequences. This affects whether phase assignments are aligned with the model's actual computational state.

### Novelty
- **Moderate novelty level.** The conceptual ingredients are all from existing work: phase-dependent tolerance (ThinKV), compound super-additivity (SparK), score collapse (HIES). The contribution is empirically connecting these in a quantitative framework — legitimate but incremental.
- **Discrimination collapse adds limited novelty over HIES.** The extension from single-axis to compound settings and phase-modulation is incremental, especially given the correlational nature and unexplained magnitude gap.

### Scope
- **Task scope boundary is severe.** The MATH-500 > GSM8K ≫ GPQA gradient suggests the finding may require long (>2000 token), highly structured reasoning chains. This is a narrow regime.
- **Scale limitation (7B/8B only).** Whether the phenomenon persists at 70B+ is untested. The paper acknowledges this.

## Questions for Authors

1. What is the head pruning ratio `p`? Does it co-vary with `s` or is it fixed?
2. Is II computed on dense-model-generated or sparse-model-generated token sequences?
3. Have you considered recency-based eviction as a control for the circular scoring confound?
4. What quantitative fraction of the severity divergence does discrimination collapse explain?
5. Can you validate phase segmentation on Qwen2.5-7B via an independent criterion?
6. Would you consider narrowing the title to "Mathematical Reasoning LLMs"?
7. Can you expand the bibliography to cover structured pruning, CoT analysis, and information-theoretic compression?

## Recommendations for Revision

1. **Specify `p` explicitly** and, ideally, test at least one additional pruning ratio to show robustness.
2. **Narrow title and framing** to mathematical reasoning; position GPQA as a scope boundary finding.
3. **Expand bibliography** from 9 to 30+ references covering the missing lines of work.
4. **Test one scoring-independent eviction strategy** (recency-based) to address the circular confound.
5. **Validate phase segmentation** on Qwen2.5-7B using an independent approach.
6. **De-emphasize ρ = 1.0** in abstract/introduction; foreground Jonckheere-Terpstra results instead.
7. **Provide causal evidence for discrimination collapse** or downgrade it from "mechanism" to "correlational observation."

## Verdict

**Overall: 2.5/5 — Borderline Reject**

The paper presents a valid empirical finding (phase-dependent compound sparsity severity) demonstrated with commendable statistical rigor and honest reporting. However, the combination of: (a) an unspecified critical parameter (`p`), (b) overclaimed scope ("Reasoning LLMs" vs. math-only evidence), (c) an extremely thin bibliography, (d) an unresolved fundamental confound, (e) a correlational and incomplete mechanism, and (f) no practical actionable outcome collectively places this below the EMNLP 2026 main conference acceptance threshold (~22%). With the revisions outlined above — particularly specifying `p`, narrowing scope, expanding the bibliography, and testing a scoring-independent eviction baseline — this could become a solid Findings paper or a competitive main conference submission in a future cycle.
