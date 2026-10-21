---
dream_id: dream_20260516T124139
tier: median
overall_score: 3 — Weak Reject
timestamp: 2026-05-16T13:17:46.217753+00:00
---


# Review Report: "When Does Symbolic Consensus Help?"

## Paper Summary

This paper proposes SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic constraints from LLM reasoning traces and resolves disagreements via weighted partial MAX-SAT. Rather than claiming uniform accuracy gains, the paper characterizes *when* SICA helps through the multi-candidate rate C0 — the fraction of questions producing multiple distinct answers across K sampled traces. Experiments span 3 instruction-model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and 2 formal-logic benchmarks (FOLIO, ProofWriter). The paper claims: (1) SICA provides principled tiebreaking (64.7% win rate on ties, p=0.035); (2) C0 governs SICA effectiveness (instruction models C0>20% benefit, reasoning models C0<5% see no gain); (3) C0 functions as a binary deployment diagnostic (AUC=0.82).

---

## Strengths

### S1: Honest and well-calibrated framing
The paper resists the temptation to overclaim. Framing the contribution as "when does this help?" rather than "this always helps" is intellectually honest and more useful than inflated accuracy claims. The paper explicitly acknowledges borderline significance (p=0.08 on FOLIO, p=0.19 combined) and decomposes the overall accuracy gain into a modest ~0.8pp over fair random tiebreaking. This calibration is refreshing and builds trust.

### S2: Clean instruction-vs-reasoning contrast
The C0 dichotomy between instruction models (C0=35–55%) and reasoning models (C0<5%) is the paper's strongest empirical finding. The LLaMA-8B-Instruct vs DeepSeek-R1-LLaMA-8B comparison is particularly compelling: same base architecture, different training paradigm, opposite SICA behavior. This cleanly isolates training paradigm as the governing variable.

### S3: Thorough experimental coverage
Seven model configurations spanning 3 families and 2 reasoning architectures, plus K-sensitivity ablation, constraint ablation, overhead analysis, cross-domain validation (GSM8K), and qualitative constraint quality analysis. For a short paper (10 pages), the breadth of experiments is commendable. All 14 planned experiments from the design are represented.

### S4: Per-tie statistical result is clean
The tiebreak analysis (44/68, p=0.035 vs random) is the paper's most statistically rigorous result. Isolating the mechanism to tie cases and demonstrating significant advantage there is methodologically sound.

### S5: Practical overhead is reasonable
22.4% overhead with 81.7% shared generation cost is defensible. The breakdown showing MAX-SAT solving is negligible (4.1%) and extraction dominates the overhead is useful for practitioners considering deployment.

---

## Weaknesses

### W1 (Major): Primary accuracy claims lack statistical significance
The headline accuracy improvement — +1.5pp combined (p=0.19), +3.9pp FOLIO (p=0.08) — is not statistically significant at conventional thresholds. The paper's main quantitative contribution thus rests on a *trending* result, not a confirmed one. While the per-tie result (p=0.035) is clean, that is a much narrower claim: SICA is a better-than-random tiebreaker, contributing ~0.8pp overall. For a top venue, this weakness is hard to overlook. The paper acknowledges this honestly, but honest framing doesn't change the evidential status.

### W2 (Major): Severely underpowered cross-model evaluations
Five of seven model configurations are evaluated on only 60 questions (30 FOLIO + 30 ProofWriter). Only Qwen-14B gets the full 804-question evaluation. With N=60, bootstrap power to detect a 3pp difference is extremely low. The reported per-model gaps (e.g., LLaMA +3.4pp, Mistral +1.6pp) all have p>0.14 — they are consistent with noise. The cross-family validation claim ("all three families confirm C0>20%") is actually a claim about C0, not about SICA's benefit, since none of the 60-question experiments achieves significance for the accuracy gap. The paper should either expand evaluations to ≥200 questions per model or explicitly caveat that individual cross-model accuracy gaps are not reliably estimated.

### W3 (Major): C0 diagnostic is partially circular
The C0 metric measures "how often does the model disagree with itself." The finding that a disagreement-resolving method helps when there is disagreement is near-tautological. The paper's actual contribution is formalizing this into a threshold-based diagnostic, but the intellectual novelty is limited. Moreover, with only 14 data points for the diagnostic analysis (Table 3), the AUC=0.82 and accuracy=85.7% are computed on an extremely small sample where leave-one-out variance is high. The diagnostic's reliability is not established.

### W4 (Major): Extremely narrow domain scope
Both benchmarks (FOLIO, ProofWriter) are formal logic tasks. The only non-logic evaluation is 30 GSM8K questions showing zero benefit. The paper provides no evidence that SICA helps on commonsense reasoning, multi-hop QA, code generation, or any domain beyond formal NLI/deduction. The title "When Does Symbolic Consensus Help?" implies generality that the experiments do not support — the answer might more accurately be "only on formal logic tasks where instruction models disagree, and even then marginally."

### W5 (Moderate): MAX-SAT solver adds negligible value over count-only
Table 6 shows MAX-SAT adds only +0.7pp over count-only aggregation (71.8% vs 71.1%). Count-only already captures +0.8pp over SC. The sophisticated symbolic solver — the titular "symbolic" contribution — provides marginal additional value. The paper appropriately frames MAX-SAT's primary contribution as interpretability, but this undermines the technical novelty of the constraint-satisfaction approach. If counting constraints suffices for accuracy, the MAX-SAT machinery is largely ornamental from a performance standpoint.

### W6 (Moderate): No figures in the paper
The experiment design references several key figures — a C0-vs-gap scatter plot (F2, described as the "hero figure"), a heatmap (F3), a K-sensitivity curve (F4), tiebreak comparison bar charts, and overhead stacked bars — but the submitted paper contains zero figures. For a paper whose core contribution is characterizing an operating regime, the absence of the scatter plot showing C0 vs gap across all configurations is a major presentation gap. Figures would substantially aid comprehension and make the operating-regime story visually compelling.

### W7 (Moderate): Thin related work
Only 7 references total. Missing important related work: (a) verifier/outcome-based reward models for reasoning (Cobbe et al., 2021; Lightman et al., 2023); (b) debate-based aggregation (Du et al., 2023); (c) structured/constrained decoding (Poesia et al., 2022); (d) LLM calibration and uncertainty quantification literature; (e) more recent SC variants and improvements. The positioning against Logic-LM and Faithful CoT is appropriate but insufficient for a venue submission.

### W8 (Minor): No error analysis on SICA failures
Of 68 tie cases, SICA loses 24. What characterizes these failures? Are they systematic (certain question types, certain constraint patterns) or random? An error analysis would strengthen the mechanistic understanding and help practitioners know when to trust SICA's tiebreaking.

### W9 (Minor): QwQ-32B data is heterogeneous
QwQ-32B is evaluated on 48 questions mixing AIME (22), ProofWriter (16), and FOLIO (10) — a different composition than all other models. AIME is a math competition benchmark not used elsewhere in the paper. The dashes in Table 1 for QwQ's per-benchmark scores make the comparison less clean. While the C0=3.6% finding is robust to composition, the inconsistency is a minor methodological blemish.

---

## Experiment Coverage vs Design

All 14 planned experiments are represented in the paper:
- **exp-001** (expanded 804q): Section 5.3, Table 1 ✓
- **exp-002** (K ablation): Table 4 ✓
- **exp-003** (tiebreak baselines): Table 2 ✓
- **exp-004** (7B scaling): Table 1 ✓
- **exp-005** (QwQ-32B): Table 1 ✓
- **exp-006** (C0 diagnostic): Table 3 ✓
- **exp-007** (72B AWQ): Table 1 ✓
- **exp-008** (constraint quality): Section 5.8 ✓
- **exp-009** (overhead): Table 5 ✓
- **exp-010** (Mistral-7B): Table 1 ✓
- **exp-011** (LLaMA-8B): Table 1 ✓
- **exp-012** (GSM8K pilot): Section 5.9, Table 8 ✓
- **exp-013** (constraint ablation): Table 6 ✓
- **exp-014** (DeepSeek-R1): Table 1 ✓

Coverage is complete. However, all planned figures (F2 scatter, F3 heatmap, F4 K-curve, tiebreak bars, overhead stacked bars, appendix case-study figures) are missing from the PDF.

---

## Questions for Authors

1. **Statistical power**: Given p=0.19 on the combined 804-question evaluation, what sample size would be needed to achieve significance at α=0.05 for a true effect of +1.5pp? Have you considered running the expanded evaluation on additional models?

2. **Domain generality**: Can you provide evidence (even preliminary) on any non-logic reasoning task where C0>20% AND SICA shows a positive gap? Without this, the paper's applicability claim is restricted to formal-logic NLI.

3. **Constraint extraction circularity**: The same LLM generates reasoning traces AND extracts constraints. Have you experimented with cross-model extraction (e.g., a stronger model extracting constraints from a weaker model's traces) to decouple generation quality from extraction quality?

4. **C0 diagnostic validation**: With only 14 data points, how robust is the AUC=0.82? What is the leave-one-out variance? Could you provide confidence intervals?

5. **Missing figures**: Are the scatter plot (C0 vs gap) and other referenced figures available? Their absence significantly weakens the presentation.

---

## Minor Issues

- Table 1 footnote says "Others: 60 questions" — should explicitly note this is 30 FOLIO + 30 ProofWriter for clarity
- The constraint extraction prompt (Step 1 in Section 3.2) is not provided; reproducibility would benefit from including it in the appendix
- Section 5.5 mentions "even values create more exact ties" — this mechanistic claim about even-K could be supported with data (e.g., comparing K=11 vs K=12)
- The paper uses both "C0" and "multi-candidate rate" — standardizing to one term would improve readability
- No mention of random seeds or variance across runs; are the 60-question results from a single run?

---

## Scoring

| Dimension | Score (1–6) | Notes |
|-----------|-------------|-------|
| Novelty | 3 | C0 diagnostic is useful but near-tautological; MAX-SAT adds marginal value over counting |
| Soundness | 3 | Core accuracy claims not significant; cross-model evals underpowered (N=60); diagnostic validated on 14 points |
| Significance | 3 | Narrow domain (formal logic only); marginal improvements (~0.8pp over fair baseline); limited practical impact |
| Clarity | 4 | Well-written, honest framing, good structure; severely hampered by missing all figures |
| Reproducibility | 3 | Model configs specified; extraction prompt missing; no random seeds; code not referenced |
| Overall | 3 | Weak Reject |

**Overall Score: 3 (Weak Reject)**

**Confidence: 4/5** — I have carefully read the paper and cross-referenced all experiments against the design document. The statistical and scope limitations are clear.

---

## Summary Assessment

The paper asks a good question ("when does symbolic consensus help?") and provides an honest, well-structured answer. The C0 operating regime characterization and the instruction-vs-reasoning contrast are genuine contributions. However, the work is undermined by three compounding issues: (1) the primary accuracy improvement is not statistically significant, even on the largest evaluation; (2) cross-model experiments are severely underpowered at N=60; (3) the domain is limited to two formal-logic benchmarks. The MAX-SAT solver — the paper's technical centerpiece — adds negligible accuracy over simple constraint counting. The missing figures further weaken the presentation.

For EMNLP Findings, the honest framing and operating-regime analysis are in the right spirit, but the current evidence base is too thin. The paper would benefit from: (a) expanding evaluations to ≥200 questions for at least 2–3 additional models to achieve statistical power; (b) testing on at least one non-logic domain where C0>20% and SICA shows benefit; (c) including the planned figures; (d) expanding the related work. With these additions, the "when does it help" framing could support a solid Findings-track contribution.
