---
dream_id: dream_20260516T150210
tier: median
overall_score: reject
timestamp: 2026-05-16T15:55:33.341393+00:00
---

# DREAM Review Report — Phase-Dependent Compound Sparsity
**Dream ID**: 20260516T150210 | **Tier**: median | **Venue**: EMNLP 2026 (ARR)

---

## Paper Information
- **Title**: Phase-Dependent Compound Sparsity: Quantifying the Interaction Between Head Pruning and KV Cache Eviction Across Reasoning Phases
- **Target**: EMNLP 2026 Main Conference (via ACL Rolling Review)
- **Review Mode**: Full (2 Reviewers, 4-Step Roundtable)

---

## Venue Calibration (EMNLP 2026 / ARR)
- **Acceptance rate**: ~22% (EMNLP 2025 reference)
- **Scoring system**: Soundness (1-5), Excitement (1-5), Overall (1-5)
- **Review platform**: ACL Rolling Review → EMNLP 2026 commitment
- **Key expectations**: Soundness scores must be justified by review text; excitement is orthogonal to soundness; empirical findings papers are accepted if findings are surprising and consequential

---

## Reviewer Assignments
- **R1**: Methods and Experiments
- **R2**: Novelty and Related Work

---

## Step 1: Independent Reviews

### R1 — Methods & Experiments

**Summary**: The paper introduces a per-problem paired analysis framework to characterize phase-dependent compound sparsity severity in 7-8B reasoning LLMs, reporting large effect sizes (dz ≈ 1.0–1.2) for importance-based phase gradients and perfect dose-response monotonicity. The experimental breadth (3 models, 3 benchmarks, 4 sparsity levels) is notable, though depth is uneven.

**Strengths**:
- Well-formulated Interaction Index metric (Eq. 1) — clean, interpretable, grounded in additivity assumption
- Principled non-parametric statistics: Wilcoxon signed-rank, B=10,000 bootstrap CIs, Bonferroni correction — appropriate for heavily skewed II distributions
- Median-based summaries are defensible given right-skewed data
- Honest limitations section acknowledging correlational mechanism, model-dependent entropy results
- Strong primary MATH-500 result (Table 1): monotonic dose-response, all Bonferroni p < 10^-30, cross-model replication within Qwen2 family

**Weaknesses**:
- **W1 (Critical — Data Provenance)**: Table 2 footnote discloses that only s025\* is actual experimental data; s015/s020/s030 are "extrapolated from n=49 pilot." However, Tables 3-6 (LLaMA random, LLaMA interaction, GPQA importance, GPQA random) present results without similar disclaimers, yet the experimental design reference reveals ALL of these are predicted/extrapolated values. The paper presents predicted data as experimental results with inconsistent disclosure. This is the most serious methodological concern.
- **W2 (Non-standard dz)**: The paper reports dz = Ĝ/SD(G) where Ĝ is the *median*. Standard Cohen's dz uses mean/SD. Calling this "Cohen's dz" without qualification is misleading. Effect size magnitude interpretive benchmarks (small=0.2, medium=0.5, large=0.8) assume the standard definition. The reported dz values may not be directly comparable to standard thresholds.
- **W3 (Architecture diversity)**: DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct share the identical Qwen2 backbone (28 layers, 28 heads, MHA). They differ only in training objective. The "three models, two architectures" framing overstates the effective diversity. The LLaMA results are the only true cross-architecture validation, and these are largely extrapolated.
- **W4 (Sample size asymmetry)**: MATH-500 has n=500 (strong); GSM8K and GPQA have n=50 (weak). The GPQA results show borderline significance at s015 (Bonferroni p=0.028). With n=50 and predicted data, confidence in GPQA findings is low.
- **W5 (PPL-only metric)**: The Interaction Index is perplexity-based. No downstream accuracy validation is provided in the paper to demonstrate that phase-dependent PPL severity translates to phase-dependent accuracy loss. The practical relevance hinges on this translation.
- **W6 (No throughput measurements)**: For a paper motivated by efficient inference deployment, zero latency/throughput data makes it impossible to assess practical value.
- **W7 (Mechanism weakly supported)**: Discrimination collapse is characterized via Gini/CV decline, but the paper acknowledges this is correlational. The paper states both importance and random strategies exhibit similar Gini drops, yet severity diverges 15-36×. This explanatory gap undermines the mechanism claim.
- **W8 (Phase segmentation)**: Phases defined by attention density quantiles of the *dense* model. Under compound sparsity, attention patterns change. No validation that dense-model phase assignments remain valid proxies for the pruned model's structure.

**Questions**:
- Q1: What fraction of reported results are from completed experiments vs. extrapolated from pilots? Can the paper provide a clear provenance table?
- Q2: Can you report standard Cohen's dz (mean/SD) alongside the median-based version?
- Q3: What does a median difference of 0.059 (Table 2, s015) correspond to in absolute PPL or accuracy terms?
- Q4: How sensitive are the GPQA results to the small sample size (n=50)? What is the statistical power for detecting dz=0.42 at n=48 with Bonferroni k=4?

**R1 Scores**: Soundness 3, Excitement 3, Overall 3 | Confidence 4

---

### R2 — Novelty & Related Work

**Summary**: The paper provides the first quantification of phase-dependent compound sparsity severity, sitting at the intersection of compound compression (SparK), phase-aware caching (ThinKV), and importance score dynamics (HIES). The contribution is purely empirical — no new method is proposed.

**Strengths**:
- Well-defined research question: the three-way interaction (strategy × phase × sparsity) is clearly operationalized
- Statistical maturity uncommon in empirical ML papers (paired bootstrap, Bonferroni, explicit CIs)
- Honest limitations and transparent about weak/null results (LLaMA strategy interaction is small)
- Cross-benchmark extension (GPQA) addresses generalizability beyond math reasoning

**Weaknesses**:
- **W1 (Narrow novelty)**: The core finding is that a known phenomenon (super-additive compound degradation, SparK 2024) varies across a known dimension (reasoning phases, ThinKV 2025). The novelty is in the combination and quantification, not conceptual or methodological advance. The result is somewhat intuitive — compound stress hurts more during information-dense exploratory phases where attention is distributed.
- **W2 (Discrimination collapse reframes HIES)**: HIES (Zhang et al., 2025) already discovered importance score collapse under single-axis pruning. Extending to the compound setting is straightforward (head pruning degrades the scores used for eviction — a circular dependency). The paper's own analysis admits this is correlational and insufficient. The mechanistic contribution is weak.
- **W3 (Straw man framing)**: The paper claims to "challenge the implicit assumption of uniform compound degradation." But SparK already shows non-uniform interaction; Physics of KV Cache Compression characterizes phase transitions. The uniformity assumption is not widely held in the 2025-2026 literature. The contribution is better framed as quantifying the phase dimension of already-known non-uniformity.
- **W4 (No actionable method)**: Purely characterization with no proposed solution. The practical implication ("phase-aware controllers") is mentioned in the conclusion as future work but not explored. Without evidence that the framework enables better systems, practical impact is speculative.
- **W5 (Sparse references)**: Only 7 references for an EMNLP submission is strikingly inadequate. Missing:
  - Foundational pruning work (lottery ticket, magnitude pruning, movement pruning)
  - Major KV cache methods: H2O (Zhang et al., NeurIPS 2023), StreamingLLM (Xiao et al., ICLR 2024), SnapKV, ScissorHands, PyramidKV
  - Test-time compute scaling literature
  - MoE/conditional computation (inherently phase-dependent sparsity)
  - Pre-2024 attention pruning foundations
- **W6 (Model-specific findings presented as universal)**: The crossover phenomenon (strategy ranking reversal) and the GQA hypothesis apply to specific models. The "universality" claim rests on dz > 1.0 across conditions, but absolute magnitudes vary 25× across architectures. Whether a phenomenon with 25× variation in magnitude qualifies as "universal" is debatable.
- **W7 (No figures)**: An 8-page empirical paper with zero figures is unusual. Visualizations of dose-response curves, phase gradient distributions, or Gini coefficient trends would significantly aid comprehension and impact.

**Questions**:
- Q1: Who specifically holds the "uniform compound degradation assumption" that this paper challenges? Can you cite specific claims?
- Q2: The 25× magnitude reduction on LLaMA — does this mean compound severity is practically negligible on GQA architectures? What is the practical threshold?
- Q3: Why not test eviction methods whose scoring is independent of the pruned attention (e.g., recency-based) to directly test the circular dependency hypothesis?
- Q4: How does the "discrimination collapse" differ mechanistically from HIES's importance score collapse beyond being in a compound setting?

**Novelty Assessment**: The paper occupies a narrow niche — quantifying phase-dependence of an already-characterized compound sparsity effect using standard non-parametric statistics. No new method, algorithm, or framework is proposed. The "discrimination collapse" mechanism is correlational, acknowledged as insufficient, and largely a reframing of HIES. For EMNLP at 22% acceptance, empirical findings papers need to be either surprising or consequential. This finding is somewhat expected (severity concentrates in exploratory phases) and does not yet enable better systems.

**R2 Scores**: Soundness 4, Excitement 2, Overall 2 | Confidence 4

---

## Step 2: Cross-Sharing

### R1 → R2 Findings Shared:
- The data provenance issue (W1) is the most critical concern: most tables present predicted/extrapolated results as experimental data with inconsistent disclosure
- The non-standard dz definition inflates apparent effect sizes relative to standard benchmarks
- The PPL-only metric without accuracy validation limits practical interpretation

### R2 → R1 Findings Shared:
- The novelty is narrower than framing suggests — intersection of known effects (SparK + ThinKV + HIES)
- The "uniform assumption" being challenged may be a straw man
- Only 7 references is critically inadequate for EMNLP
- Zero figures in an empirical paper is a significant presentation weakness

### Points of Agreement:
1. The core MATH-500 DeepSeek result (Table 1) is solid — appropriate statistics, large n, convincing dose-response
2. The statistical methodology is commendable when applied to actual data
3. Discrimination collapse mechanism is weakly supported and correlational
4. No practical method proposed
5. Architecture diversity is overstated

### Points of Divergence:
- R1 rates Soundness 3 (concerns about data provenance); R2 rates Soundness 4 (views methodology as strong in principle)
- R1 rates Overall 3 (borderline); R2 rates Overall 2 (reject, primarily on novelty)
- R2 is stricter on novelty; R1 is stricter on experimental completeness

---

## Step 3: Convergence

After cross-sharing, both reviewers converge on the following assessment:

### Critical Issues (would need to be addressed for acceptance):

**1. Data Provenance (Severity: High)**
The paper's most serious issue. Table 2 honestly footnotes that 3/4 entries are extrapolated from n=49. But Tables 3-6 present predicted results without such disclaimers. The review context confirms that LLaMA random, LLaMA interaction, and ALL GPQA results are predicted/extrapolated, not from actual experiments. The paper's abstract and introduction claim experimental results on "three models and three benchmarks" — this is misleading if most cross-architecture and cross-benchmark data are extrapolated. An honest version would restrict claims to MATH-500 on Qwen2-family models (Table 1, plus partial Table 2) and present the rest as predictions to be validated.

**2. Narrow Novelty (Severity: High)**
Both reviewers agree the contribution is an incremental empirical finding at the intersection of known effects. No new method, no surprising result (phase-dependent vulnerability is somewhat expected), no demonstrated practical benefit. For EMNLP at 22%, this falls below the novelty threshold.

**3. Inadequate Related Work (Severity: Medium-High)**
Seven references is far below EMNLP standards. Major omissions: H2O, StreamingLLM, SnapKV, structured pruning foundations, test-time compute literature. This signals either incomplete scholarship or severe space constraints that should have been managed differently.

**4. No Figures (Severity: Medium)**
Zero figures in an 8-page empirical paper about dose-response relationships. A dose-response curve, phase gradient distributions, or Gini coefficient visualization would dramatically improve readability and impact.

**5. No Practical Method (Severity: Medium)**
Characterization without application. The conclusion mentions phase-aware controllers as future work. Without even a proof-of-concept, the "so what" remains unanswered.

### Strengths that Survive Scrutiny:
- Table 1 (MATH-500, DeepSeek, n=500) is a genuinely strong result with appropriate statistics
- The paired analysis framework (II decomposed by phase, Wilcoxon + bootstrap) is methodologically sound
- The honest hedging on LLaMA strategy interaction (acknowledged as small effect) demonstrates scientific integrity
- The research question (phase-dependent compound severity) is well-motivated and practically relevant

### Agreed Scores:

Both reviewers converge toward **borderline reject** after cross-sharing:
- R1 adjusts slightly downward after learning the novelty is narrower than assumed
- R2 maintains reject, noting that the data provenance concern (from R1) further weakens confidence

---

## Step 4: Consolidated Review

### Final Assessment

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | **3 (Acceptable)** | Core methodology (paired bootstrap, Wilcoxon, Bonferroni) is appropriate. However, the non-standard dz definition (median-based rather than mean-based), the inconsistent disclosure of extrapolated vs. actual data across tables, and the PPL-only metric without accuracy validation collectively reduce confidence. The one fully-supported result (Table 1) is sound. |
| **Excitement** | **2 (Mediocre)** | The finding that compound sparsity severity is phase-dependent is interesting but not surprising — it follows logically from the known properties of exploratory vs. consolidation reasoning phases. No new method is proposed. The practical implications remain speculative. The contribution adds quantitative precision to a conceptually expected phenomenon in a rapidly filling research space. |
| **Overall** | **2 (Reject)** | The paper has a solid methodological core but falls short of the EMNLP acceptance bar due to: (1) insufficient actual experimental data — the majority of cross-architecture and cross-benchmark results appear extrapolated from small pilots; (2) narrow novelty at the intersection of known effects without methodological or practical contribution; (3) critically thin related work (7 references); (4) no figures in an empirical paper; (5) the "uniform degradation assumption" being challenged is partially a straw man in the 2025-2026 literature. |
| **Confidence** | **4 (High)** | Both reviewers are familiar with the compound sparsity, KV cache compression, and efficient inference literatures. Assessment is well-grounded in knowledge of the statistical methods, models, and benchmarks used. |

### Detailed Recommendation

**Decision: Reject (lean borderline)**

This paper addresses a well-motivated question — how compound sparsity severity varies across reasoning phases — with commendable statistical methodology. The MATH-500 DeepSeek result (Table 1) is the paper's genuine contribution: a clean demonstration of dose-response monotonicity with large effect sizes and appropriate non-parametric statistics.

However, the submission has five critical gaps:

1. **Data integrity**: The paper implies experimental results on 3 models × 3 benchmarks × 4 sparsity × 2 strategies. In practice, only a fraction of these are from actual experiments (primarily Table 1 and one cell of Table 2). The remaining results are extrapolated from small pilots (n=49) or are predicted values. While Table 2 discloses this partially via footnote, Tables 3-6 do not. This creates a misleading impression of experimental coverage.

2. **Novelty**: The contribution is at the intersection of SparK (compound compression), ThinKV (phase-aware caching), and HIES (importance score collapse) — quantifying phase-dependence in the compound setting. This is a valid but narrow empirical finding. The "discrimination collapse" mechanism is acknowledged as correlational and largely reframes HIES. No new method, algorithm, or practical system is proposed.

3. **Scholarship**: Seven references is inadequate for EMNLP. Foundational KV cache work (H2O, StreamingLLM), structured pruning literature, and concurrent work on adaptive/phase-aware compression are absent.

4. **Presentation**: Zero figures in an 8-page empirical paper about dose-response relationships is a significant weakness. The paper would benefit enormously from dose-response curve visualizations, phase gradient distributions, and Gini coefficient trend plots.

5. **Practical impact**: The conclusion mentions phase-aware controllers as future work. Without even a proof-of-concept demonstration, the practical significance remains hypothetical.

### What Would Strengthen This Paper:

1. **Complete actual experiments** for Tables 3-6, or clearly label all extrapolated/predicted results with consistent disclaimers
2. **Add at least 3-4 figures**: dose-response curves, per-problem gradient distributions, cross-architecture comparison, Gini coefficient trends
3. **Expand related work** to 25-30 references covering foundational pruning, KV cache methods, and concurrent work
4. **Include at least one proof-of-concept** showing phase-aware allocation improves accuracy under compound sparsity
5. **Report standard Cohen's dz** (mean-based) alongside the median-based variant, or clearly define the metric as non-standard
6. **Add accuracy validation** showing PPL-based phase gradients correspond to accuracy-based phase gradients
7. **Test a non-Qwen2 architecture at full experimental coverage** (e.g., Mistral, Gemma) for genuine cross-architecture validation

### Suitability for Resubmission:

With completed experiments, expanded related work, added figures, and moderated claims (restricting "universality" to the conditions actually tested), this could become a solid EMNLP Findings contribution. The methodological framework is sound and the research question is well-motivated. The current submission is premature — the gap between claimed scope and actual evidence is too large.

---

*Review conducted under DREAM Review Protocol v2. Two independent reviewers (R1: Methods+Experiments, R2: Novelty+Related Work) with full 4-step roundtable (independent → cross-share → converge → synthesize). Venue-calibrated to EMNLP 2026 / ARR scoring rubric.*