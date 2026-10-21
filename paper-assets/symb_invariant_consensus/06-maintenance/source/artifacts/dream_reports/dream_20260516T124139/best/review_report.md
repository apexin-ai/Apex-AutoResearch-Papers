---
dream_id: dream_20260516T124139
tier: best
overall_score: Weak Reject (3/6)
timestamp: 2026-05-16T13:15:14.578699+00:00
---

# Dream Review Report — SICA Paper (dream_20260516T124139)

**Paper:** "When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation"
**Venue standard:** Top ML venue (EMNLP-level, ~25% acceptance, 6-point scale)
**Review mode:** simple (1 reviewer, full coverage)

---

## Summary

The paper proposes SICA, a post-hoc aggregation method that extracts first-order logic (FOL) constraints from LLM reasoning traces and uses weighted partial MAX-SAT to resolve Self-Consistency (SC) voting ties. The central contribution is the C0 regime characterization: SICA helps when trace diversity C0 > 20% (instruction-tuned models on hard tasks) but degenerates to SC when C0 < 5% (reasoning models or easy tasks). Evaluated across 7 model configurations, 2 logic benchmarks, and a GSM8K pilot, reporting +6.9pp on FOLIO with Qwen2.5-14B (p=0.023) and C0-gap Pearson r=0.91 across 14 configurations.

---

## Strengths

- **S1. Well-motivated regime characterization.** The question "when does symbolic consensus help?" is more interesting than "symbolic consensus helps." Framing negative results (QwQ-32B, DeepSeek-R1 showing zero gain) as operating regime boundaries rather than hiding them is scientifically honest and adds genuine insight. The LLaMA-3.1-8B-Instruct vs. DeepSeek-R1-Distill-LLaMA-8B controlled comparison (same architecture, different training → C0 collapses from 0.40 to 0.033) is a particularly clean demonstration.

- **S2. C0 as zero-cost diagnostic is practically actionable.** Practitioners can compute C0 from an existing SC run with no additional inference to decide whether SICA deployment is worthwhile. The C0=20% threshold with 100% binary classification accuracy on the 14 evaluated configurations is a crisp, memorable result.

- **S3. Principled tiebreaking is well-validated.** The 77% tiebreak accuracy on 129 tied instances (vs. 50% random) is a substantial margin. The ablation hierarchy (MAX-SAT 77% > count-only 60% > random-weight 52% ≈ SC 50%) cleanly demonstrates that satisfiability checking adds value beyond simple constraint counting and that gains come from meaningful constraint weighting, not merely multi-signal aggregation (Table 4).

- **S4. Appropriate experimental controls.** K sensitivity (Table 3), constraint aggregation ablation (Table 4), overhead analysis (Table 5), multiple tiebreak baselines (Table 2), cross-family validation (Mistral, LLaMA), and qualitative failure analysis (1/8 negation scope case) are all included. The design space is well-explored.

- **S5. Low overhead and honest cost accounting.** The 1.38× multiplier over SC is modest. Showing MAX-SAT solving at only 1.4% of total time directly rebuts the "over-engineering" concern. The per-stage breakdown (Table 5) is transparent.

- **S6. Comprehensive model coverage for the C0 story.** 3 model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), within-family scaling (7B/14B/72B), and a cross-domain pilot (GSM8K) collectively paint a coherent picture. All 14 planned experiments are reflected in the paper.

---

## Weaknesses

- **W1 (Major). SICA's actual mechanism is narrower than framed.** Table 2 shows SICA's gains come entirely from the 129 tied instances out of 804. On non-tied questions where SC has a clear majority, SICA apparently produces identical output (the paper never reports SICA flipping a clear majority). The abstract and method section frame SICA as "constraint-based reasoning aggregation" with a general argmax formulation (Equation 1), but in practice it reduces to "a better-than-random tiebreaker for exact vote splits." This is a real but substantially narrower contribution than the framing suggests. The paper should transparently acknowledge this and discuss whether SICA ever disagrees with SC on non-tied instances.

- **W2 (Major). C0-gap correlation with n=14 has severe non-independence.** The r=0.91 claim uses 14 data points, but 5 come from varying K on the same model/dataset (K=6,8,12,16,20 for Qwen2.5-14B on D012), introducing strong autocorrelation. The remaining 9 include 3 Qwen variants (correlated by family), 2 reasoning models trivially at the origin (C0≈0, gap=0), and only 2 truly independent non-Qwen models (Mistral, LLaMA). Effective independent sample size is closer to 6–7. No confidence intervals are reported on the correlation or regression coefficients. The C0-gap relationship also breaks at K=20: C0 continues to increase (0.58) but gap narrows to +1.7pp, contradicting the simple monotonic narrative. This is acknowledged in the K-sensitivity discussion but not reconciled with the r=0.91 claim.

- **W3 (Major). Combined statistical significance is marginal.** The combined 804-question result has p=0.072, which does not meet alpha=0.05. Only the FOLIO subset reaches significance (p=0.023). The abstract and introduction lead with FOLIO numbers (+6.9pp, p=0.023) while the combined significance is mentioned in passing (Section 5.1). This selective emphasis on the per-domain subset where significance is achieved is a form of cherry-picking. ProofWriter shows only +1.2pp, making the combined improvement fragile.

- **W4 (Major). Cross-family evaluations are severely underpowered.** Mistral-7B and LLaMA-8B are each evaluated on only 60 questions (D012). A +5.0pp gap on 60 questions corresponds to ~3 questions. Bootstrap p-values would be well above 0.05 (the paper reports p=0.17 and p=0.19 from the context). These results cannot individually achieve significance. Their claimed value is in the aggregate pattern, which has the non-independence issues of W2.

- **W5 (Major). Missing comparisons to neuro-symbolic baselines.** The related work discusses Logic-LM [3] and LINC [4], both of which have published FOLIO/ProofWriter results and represent the most directly comparable methods. No head-to-head experimental comparison is provided. The argument that "they replace LLM reasoning while SICA aggregates" is a framing distinction, not an empirical justification for omitting comparisons on the same benchmarks. This is a significant gap for an EMNLP submission.

- **W6 (Moderate). Domain coverage is narrow and favorable.** Both primary benchmarks (FOLIO: FOL NLI; ProofWriter: formal logic) are tasks where FOL constraint extraction is naturally well-suited. The GSM8K pilot (30 questions, C0=0.10, gap=0) is too small to constitute cross-domain evidence and shows no gain. Commonsense reasoning (e.g., StrategyQA, ARC), reading comprehension, or other NLU tasks where constraint extraction quality is unknown are absent. The evaluation is domain-favorable for SICA.

- **W7 (Moderate). Missing comparison against trivial odd-K baseline.** If SICA's entire contribution is tiebreaking on even-K settings, using K=13 instead of K=12 (odd K eliminates ties at zero overhead) is a cheaper alternative. The paper does not discuss or compare against this trivial baseline, which is a significant oversight for the practical deployment narrative.

- **W8 (Moderate). Broken figure reference undermines central claim.** Section 5.3 references "Figure ?? (described textually; see Appendix for data)" — the hero scatter plot that is supposed to visually anchor the C0 diagnostic claim is missing. For a paper whose central contribution is the C0-gap relationship, not having this figure is a serious presentation failure.

- **W9 (Minor). Thin bibliography.** Only 9 references for a paper positioned at the intersection of SC, neuro-symbolic reasoning, and uncertainty quantification. Key recent works (Taubenfeld et al. 2025 on self-consistency improvements, DyLoS, FoVer, LogicAgent, Aristotle, DeepSeek-R1 technical report) are absent. The related work section is thin for a top venue submission.

---

## Detailed Dimension Scores

### Novelty & Significance: 4/6

The regime characterization (C0 as a diagnostic for when symbolic aggregation helps) is a genuinely novel and useful conceptual contribution. The specific combination of FOL extraction + MAX-SAT + SC sampling is new, though individual components are well-established. The tiebreaking-only nature of the improvement limits significance: the practical impact is bounded by the tie rate, which depends on K, answer space cardinality, and model confidence. For binary tasks (ProofWriter), ties are rare and gains approach zero. The contribution would be more significant if SICA could override clear SC majorities.

### Technical Soundness: 4/6

The MAX-SAT formulation (Equation 1) is properly specified. Z3 PB-MaxSAT usage is appropriate. The constraint weighting by "occurrence frequency across traces" could be more formally defined (raw count? normalized? TF-IDF-style?). The C0 analysis conflates model capability with the C0 metric itself — C0 is simultaneously correlated with model strength, task difficulty, and training paradigm, and the paper cannot disentangle these. The K=20 anomaly (C0 up, gap down) contradicts the monotonic C0→gap story. The ablation design is sound (MAX-SAT vs count-only vs random-weight is the right comparison). Statistical testing uses bootstrap but doesn't report effect sizes or CIs on the correlation.

### Experimental Rigor: 3/6

The 804-question FOLIO+PW evaluation for the main model (14B) is adequate for the per-domain significance on FOLIO (p=0.023), but the combined p=0.072 is marginal. The D012 (60 questions) evaluations for all other models are severely underpowered for individual claims. The n=14 correlation with ~7 effectively independent points is fragile. The K-ablation and constraint ablation are well-designed but both use the limited D012/804 data. The GSM8K pilot (30 questions) is too small to be meaningful. No held-out test set or cross-validation. No correction for multiple comparisons across 7 model configurations.

### Clarity & Presentation: 4/6

The paper is generally well-written with clear method description, intuitive C0 definition, and informative tables. The 4-stage pipeline is easy to follow. The "When Does Symbolic Consensus Help?" framing is compelling. Weaknesses: the broken "Figure ??" reference is a serious omission for the paper's central visual claim; the abstract/introduction frame the contribution more broadly than the actual mechanism warrants; the paper could be more upfront about the tiebreaking-only nature of improvements.

### Completeness & Coverage: 3/6

All 14 planned experiments are reflected, which is good internal completeness. However, the absence of comparisons to Logic-LM, LINC, or other neuro-symbolic methods on FOLIO/ProofWriter is a significant external gap. The bibliography is thin (9 refs). No odd-K baseline comparison. No analysis of SICA behavior on non-tied instances. No per-question constraint quality metrics against FOLIO's gold FOL annotations.

### Limitations & Honesty: 5/6

The limitations section is commendably honest: it acknowledges narrow domain coverage, D012 power limitations, constraint extraction bias, and that SICA targets instruction-tuned models (not reasoning models). The QwQ/DeepSeek-R1 negative results are presented as scientific findings. The 1/8 failure case is included. The paper could go further by acknowledging: (a) SICA's improvement is exclusively on tied instances; (b) the C0-gap correlation may be an artifact of the instruction-vs-reasoning dichotomy rather than a continuous relationship.

### Practical Impact: 3/6

The deployment protocol ("run SC → compute C0 → deploy SICA if C0>20%") is clear and actionable. The 1.38× overhead is reasonable. However, impact is limited by: (a) tiebreaking-only mechanism bounds gains by tie rate; (b) gains are concentrated on FOL-aligned tasks; (c) the trivial alternative of using odd K (K=11 or K=13) to eliminate ties entirely is not discussed; (d) the combined accuracy gain of +2.6pp at p=0.072 may not justify the engineering complexity of deploying FOL extraction + MAX-SAT in production.

---

## Missing Experiments / Key Gaps

1. **Head-to-head comparison with Logic-LM / LINC on FOLIO/ProofWriter** — the most directly comparable methods
2. **Odd-K baseline (K=11 or K=13)** — if SICA = tiebreaker, odd K eliminates ties at zero cost
3. **SICA behavior on non-tied instances** — does it EVER disagree with SC majority? If not, state explicitly
4. **Confidence intervals on C0-gap regression** — bootstrap CIs on slope, intercept, and r
5. **Larger non-logic domain evaluation** — 100+ questions on GSM8K, StrategyQA, or ARC
6. **Constraint extraction quality** — precision/recall against FOLIO gold FOL annotations
7. **The actual hero figure (C0 vs gap scatter plot)** — currently a broken reference

---

## Minor Issues

- Broken figure reference "Figure ??" in Section 5.3
- Table 1 GSM8K row uses "—" for FOLIO/PW but shows combined 90.0/90.0/0.0 — this "Combined" means something different than for other rows
- "SC-Random" is both the standard SC default and a tiebreak baseline in Table 2 — slightly confusing
- Section 3.3 says "weighted by occurrence frequency across traces" — needs formal definition
- AWQ quantization for 72B not discussed as a potential confound on C0
- Only 9 references is unusually thin

---

## Questions for Authors

1. **On non-tied instances:** What fraction of the 675 non-tied instances (out of 804) show any SICA–SC disagreement? If zero, this should be stated clearly and the contribution reframed as principled tiebreaking rather than general constraint-based aggregation.

2. **Odd-K baseline:** Have you tested K=11 or K=13? If SICA's gains are entirely from tiebreaking, odd K eliminates ties at zero cost — what is SC accuracy at K=13 vs SICA at K=12?

3. **K=20 anomaly:** C0 increases monotonically with K, but gap narrows at K=20. How do you reconcile this with the claimed C0-determines-gap relationship?

4. **Logic-LM comparison:** Logic-LM with GPT-4 achieves ~71% on FOLIO. Your SICA + 14B claims 82.4%. Can you provide a controlled comparison on the same data split?

5. **Constraint extraction quality:** What is the precision/recall of extracted FOL constraints against FOLIO's gold FOL annotations?

---

## Overall Assessment

| Dimension | Score |
|---|---|
| Novelty & Significance | 4/6 |
| Technical Soundness | 4/6 |
| Experimental Rigor | 3/6 |
| Clarity & Presentation | 4/6 |
| Completeness & Coverage | 3/6 |
| Limitations & Honesty | 5/6 |
| Practical Impact | 3/6 |

## Overall Score: 3/6 (Weak Reject)
## Confidence: 4/5
## Recommendation: Weak Reject

**Justification:** The paper asks an interesting and well-framed question ("when does symbolic consensus help?"). The C0 regime characterization is a genuinely useful conceptual contribution, the tiebreaking mechanism is real and well-ablated, and the honest inclusion of negative results (reasoning models) is commendable. However, the paper has several significant issues that place it below the acceptance bar for a top venue:

1. **The contribution is narrower than framed** — SICA is a tiebreaker, not a general aggregation mechanism, and this is not transparently acknowledged.
2. **Statistical evidence is marginal** — combined p=0.072, cross-family evaluations on only 60 questions, C0 correlation on n=14 with ~7 effectively independent points.
3. **Missing key comparisons** — no head-to-head with Logic-LM/LINC; no odd-K baseline; no non-logic domain at scale.
4. **Presentation gap** — the hero figure (C0-vs-gap scatter) is a broken reference.
5. **Narrow domain** — gains are concentrated on FOLIO (FOL-aligned task); ProofWriter shows minimal gain; no evidence beyond logic/math.

**Path to acceptance:** (a) Include the hero figure; (b) add Logic-LM/LINC comparison on FOLIO; (c) test odd-K baseline to establish SICA's advantage over the trivial alternative; (d) expand cross-family evaluations to 200+ questions for statistical power; (e) add a commonsense reasoning benchmark; (f) transparently frame the contribution as principled tiebreaking with a deployment diagnostic, not general constraint-based aggregation.