---
dream_id: dream_20260516T155754
tier: best
overall_score: 3/6 Weak Reject
timestamp: 2026-05-16T16:27:36.089247+00:00
---

# Review Report: "When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation"

## Summary

The paper proposes SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic (FOL) constraints from LLM reasoning traces and uses weighted partial MAX-SAT to select the most globally consistent answer, improving over Self-Consistency (SC) majority voting. The core contribution is the multi-candidate rate C0 as a zero-cost diagnostic that predicts when SICA helps: high C0 (instruction-tuned models on hard tasks) → positive gains; low C0 (reasoning models or easy tasks) → zero gain. Evaluated on FOLIO + ProofWriter with 7 models across 3 families.

---

## Strengths

**S1. Clean problem framing and well-told story.** The paper identifies a genuine weakness of SC (arbitrary tiebreaking), proposes a principled solution, and then honestly characterizes when it works and when it doesn't. The "when does it help?" framing is more valuable than presenting SICA as a universal improvement. This intellectual honesty is refreshing.

**S2. The C0 diagnostic is a genuinely useful practical contribution.** C0 is computable at zero additional cost from existing SC samples, achieves strong predictive power (r=0.89, AUC=0.96), and provides a clean deployment decision rule. This is actionable for practitioners regardless of whether they adopt SICA itself.

**S3. Strong negative controls.** The QwQ-32B and DeepSeek-R1-LLaMA-8B results are not treated as failures but as informative negative controls. The LLaMA-8B-Instruct vs. DeepSeek-R1-Distill-LLaMA-8B comparison (same base architecture, C0=52% vs. 5%) is particularly elegant and cleanly isolates training regime as the driver of trace diversity.

**S4. Tiebreak analysis is convincing.** 78% accuracy on 68 tied problems vs. 50% random (p=0.003) isolates SICA's contribution cleanly. The comparison against multiple tiebreak strategies (alphabetical, longest-chain, first-seen) is thorough.

**S5. The constraint ablation validates the method's machinery.** MAX-SAT outperforming count-only by 2.6pp (and 16pp on tiebreak accuracy) demonstrates that satisfiability checking is load-bearing, not just constraint counting. This is the right experiment to run.

**S6. Reasonable model coverage.** 7 models spanning 3 families (Qwen, Mistral, LLaMA) and 2 training regimes (instruction-tuned, reasoning-distilled). The within-Qwen scaling gradient (7B→14B→72B) and cross-family convergence at 7-8B scale add credibility.

---

## Weaknesses

**W1. Narrow domain — only logic reasoning where FOL extraction is natural (Major).**
FOLIO and ProofWriter are essentially the best-case benchmarks for a method that extracts FOL constraints, since FOLIO premises are near-FOL by design and ProofWriter is fully formal. The paper's claim that SICA provides "principled tiebreaking" is only demonstrated in this favorable domain. The GSM8K pilot (30 questions, C0=10%, gap=0) shows C0 transfers but says nothing about whether SICA works on domains with high C0 but where constraint extraction is less faithful (e.g., commonsense reasoning, science QA, code generation). The authors acknowledge this limitation, but it substantially reduces the paper's scope and impact.

**W2. Most cross-model results rest on 60-question evaluations with non-significant p-values (Major).**
Only the 14B full-scale experiment (804q, p=0.018) achieves statistical significance. The individual 60-question experiments yield p-values of 0.14 (7B), 0.19 (Mistral), 0.21 (LLaMA), and 0.38 (72B). On 30-question subsets, +3.3pp corresponds to exactly 1 question. The cross-family and scaling claims are built on individually underpowered experiments. While the consistent direction across models is suggestive, reviewers at a top venue will (rightly) question whether 5 instruction models each showing +1 to +3 correct questions on 60 items constitutes robust evidence.

**W3. Suspiciously uniform results across models (Moderate).**
Mistral-7B and LLaMA-8B both show exactly +3.3pp on FOLIO and +3.3pp on ProofWriter. On 30-question subsets, this is exactly 1 additional correct answer in each case. The uniformity is suspicious and raises the question of whether these are genuine, replicable effects or within-noise fluctuations that happen to align.

**W4. Missing important baselines (Major).**
The paper only compares SICA against vanilla SC. Key missing baselines:
- **Weighted SC** (weight votes by generation log-probability or confidence calibration) — this is the most obvious extension of SC and a natural comparison
- **Verifier-based approaches** (ORM/PRM-style reranking) — these also exploit trace content for answer selection
- **Universal Self-Consistency** (Chen et al., 2023) — mentioned in related work but not compared experimentally
- **Best-of-N with reward model** — another structured selection method

Without these, it's unclear whether SICA's gains come from the specific FOL+MAX-SAT machinery or simply from using any signal beyond raw vote count.

**W5. No figures in the paper (Moderate).**
The experiment plan envisions several figures (C0 vs. gap scatter plot as "hero figure," K vs. accuracy curves, operating regime heatmap, overhead stacked bar). The submitted paper contains only tables. The C0 scatter plot in particular would make the paper's central claim far more compelling than the current text-only description of correlations in Section 5.4. This is a significant presentation gap.

**W6. Thin related work (Moderate).**
Only 3 references. Missing important lines of work:
- Verifier/reranking approaches (Cobbe et al., 2021; Li et al., 2023)
- Other symbolic reasoning integration (SatLM, LINC, etc.)
- Debate/discussion-based aggregation methods
- Ensemble methods beyond SC (mixture-of-agents, etc.)
- Prior work on MAX-SAT for belief aggregation/merging

**W7. FOL extraction quality lacks rigorous evaluation (Moderate).**
The qualitative analysis covers only 8 problems and reports summary statistics (85% semantically meaningful, 75% excluded constraints correspond to errors) without systematic evaluation. There is no inter-annotator agreement, no evaluation on a held-out set, and no analysis of failure modes in extraction. Given that extraction quality is the foundation of the entire method, this deserves more rigorous treatment.

**W8. C0 as predictor is partially tautological (Minor).**
C0 measures trace diversity → higher C0 means more ties → more ties means more tiebreaking opportunities → more opportunities means larger SICA-SC gap. The correlation is mechanistic, not surprising. The paper calls this "causal" (Section 5.4), but it's closer to definitional. The more interesting (and untested) question is: given a fixed C0, does SICA's gain vary with constraint extraction quality, domain, or model family?

**W9. No analysis of SICA's failure cases (Minor).**
The paper mentions 6 unique losses (problems where SICA is wrong but random tiebreak would be correct) but doesn't analyze them. Understanding when MAX-SAT resolution fails is important for practitioners.

---

## Experiment Coverage Assessment

Comparing against the full experiment design (14 planned experiments):

| Experiment | Status | Notes |
|---|---|---|
| exp-001: 14B full-scale (804q) | Fully covered | Table 1, primary evidence |
| exp-002: K ablation | Fully covered | Table 3 |
| exp-003: Tiebreak baselines | Fully covered | Table 2 |
| exp-004: 7B scaling | Covered | Table 1 (60q) |
| exp-005: QwQ-32B regime | Covered | Table 7 |
| exp-006: C0 diagnostic scatter | Partially | Correlations in text, no figure |
| exp-007: 72B AWQ | Covered | Table 1 (60q) |
| exp-008: Constraint case studies | Thin | Section 5.8, no figures |
| exp-009: Overhead analysis | Fully covered | Table 4 |
| exp-010: Mistral-7B | Covered | Table 1 (60q) |
| exp-011: LLaMA-8B | Covered | Table 1 (60q) |
| exp-012: GSM8K pilot | Covered | Table 6 |
| exp-013: Constraint ablation | Fully covered | Table 5 |
| exp-014: DeepSeek-R1-8B | Covered | Table 1 (60q) |

All 14 experiments are represented. The main gap is the absence of planned figures, particularly the hero C0-vs-gap scatter plot. The constraint quality case studies (exp-008) are thinner than planned.

---

## Questions for Authors

1. How does SICA compare against weighted SC (votes weighted by generation log-probability)? This is the minimal baseline that uses trace content.
2. What happens on a high-C0 domain where FOL extraction is less natural (e.g., commonsense NLI, science QA)?
3. The 60-question experiments are individually non-significant. Have you considered a formal meta-analysis or mixed-effects model across all experiments to pool statistical power?
4. Can you characterize the 6 unique loss cases? Are they systematic (e.g., extraction errors on a specific pattern) or random?
5. Is the constraint extraction prompt fixed across all models and benchmarks, or was it tuned?

---

## Minor Issues

- Table 1: QwQ-32B row shows "—" for absolute accuracy values. These should be reported.
- Section 3.2: The C0 formula uses set notation {a_i^(j)} which may count duplicates differently depending on interpretation. Clarify whether this is the set of distinct answers.
- The paper uses "principally" (Section 1, paragraph 2) where "principled" is intended (a recurring typo in multiple places — check).
- Table 7 uses a different question set (48q including AIME) vs. other models (60q FOLIO+PW). This inconsistency should be explained.

---

## Overall Assessment

**Score: 3 / 6 (Weak Reject)**

The paper presents a clean idea (FOL constraint extraction + MAX-SAT for principled tiebreaking) with an intellectually honest framing (characterizing when it works rather than claiming universal gains). The C0 diagnostic is a genuine contribution. However, the paper has significant experimental limitations that fall below the bar for a top ML venue:

1. **Domain narrowness**: Only demonstrated on benchmarks where FOL extraction is trivially well-suited. Generalizability is unknown.
2. **Statistical power**: 5 of 7 model evaluations use 60 questions with non-significant p-values. The cross-model claims outrun the evidence.
3. **Missing baselines**: No comparison against weighted SC, verifier-based reranking, or other structured aggregation methods. Without these, the value of the specific FOL+MAX-SAT machinery over simpler alternatives is unestablished.
4. **Presentation gaps**: No figures despite the analysis being inherently visual (scatter plots, heatmaps).

The core idea deserves development. To reach acceptance at a top venue, the paper needs: (a) evaluation on at least one non-logic domain with high C0, (b) weighted-SC and verifier baselines, (c) full-scale evaluations for at least 2-3 more models (not just 14B), and (d) the planned figures. The current version reads as a solid workshop paper or work-in-progress rather than a complete top-venue submission.

**Confidence: 4/5** — I am confident in this assessment. The strengths are genuine and the weaknesses are identifiable from the paper itself without requiring external verification.
