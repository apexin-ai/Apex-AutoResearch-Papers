---
dream_id: dream_20260516T155754
tier: worst
overall_score: 3 — Reject
timestamp: 2026-05-16T16:32:22.935643+00:00
---

# Review Report: "When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation"

## Summary

The paper proposes SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic constraints from LLM reasoning traces and uses weighted partial MAX-SAT to resolve voting ties in Self-Consistency (SC). Through evaluation across 7 models, 3 families, 2 reasoning architectures, and 804 logic questions, the authors find that SICA does not yield statistically significant accuracy gains over SC (+0.3pp, p=0.38). The paper pivots to characterizing the "operating regime" for symbolic consensus, identifying trace diversity (C0) as a necessary-but-not-sufficient condition and constraint extraction quality (~62%) as the bottleneck.

---

## Overall Assessment

**Score: 3 / 6 (Reject)**

The paper reports a comprehensive negative result with commendable honesty, but the analytical contributions presented as a pivot are largely tautological or insufficiently supported. The core method fails, and the post-hoc analysis—while sensible—does not rise to the level of a standalone contribution for a top ML venue. The constraint quality analysis, central to the "dual-condition" claim, rests on only 8 manually inspected examples.

---

## Strengths

### S1: Honest and Systematic Negative Result
The paper commendably reports a null result rather than cherry-picking favorable subsets. The progression from a +6.7pp pilot artifact to +0.3pp at scale is a useful cautionary tale about small-sample variance in LLM evaluation. This kind of transparency is valuable.

### S2: Broad Model Coverage
Evaluating 7 models across 3 families (Qwen, Mistral, LLaMA) and 2 training paradigms (instruction vs. reasoning) is thorough. The DeepSeek-R1 vs. LLaMA-3.1-8B minimal pair (same architecture, different training → dramatically different C0) is the cleanest experimental finding in the paper and convincingly isolates training methodology as the driver of output convergence.

### S3: Comprehensive Ablation Suite
The K sensitivity study (Table 6), constraint aggregation ablation (Table 7), overhead analysis (Table 9), and cross-domain C0 validation (GSM8K, Table 8) together provide a thorough dissection of where and why SICA fails. The K ablation cleanly shows SICA operates exclusively through tiebreaking.

### S4: Clear Writing
The paper is well-structured and readable. The framing is upfront about negative results rather than burying them. Tables and analysis are presented logically.

---

## Weaknesses

### W1: Core Contributions Are Near-Tautological (Major)
The paper's central analytical claim—that C0 < 5% means SICA ≡ SC—is definitionally obvious. If all K traces produce the same answer, *any* post-hoc aggregation method is redundant. This is not a "finding" but a logical consequence of the method's design (SICA only intervenes on ties). Framing this as an "operating regime characterization" overstates its intellectual contribution. The "diverse regime" finding (C0 > 20% → mean gap +0.7pp with 57% positive rate) is barely better than a coin flip for predicting actual gains, which the authors acknowledge but still present as a contribution.

### W2: Constraint Quality Analysis Is Severely Underpowered (Major)
The dual-condition claim—that constraint extraction quality (~62% semantic correctness) is the bottleneck—is the paper's most interesting potential contribution. However, it rests on manual analysis of only 8 questions (Section 4.8). This is far too small to support the central explanatory claim of the paper. The error taxonomy (hallucinated predicates 15%, wrong quantifier scope 10%, missing negation 8%) cannot be reliably estimated from 8 examples. An automated quality assessment (e.g., checking constraint consistency, back-translation verification, or correlation between per-question extraction quality and SICA correctness) over the full 804 questions would be needed to make this claim credible.

### W3: No Attempt to Address the Identified Bottleneck (Major)
The paper identifies constraint extraction quality as the key bottleneck but makes no attempt to improve it—not even a simple ablation with oracle constraints or a fine-tuned extractor. An experiment showing that SICA *does* improve significantly when given higher-quality constraints (e.g., gold FOL on a subset, or constraints verified by a second LLM pass) would transform this from "method doesn't work, here's why" into "method works under identifiable conditions, here's the path forward." Without this, the paper diagnoses but does not treat.

### W4: Unbalanced Evaluation Design (Moderate)
The primary model (Qwen2.5-14B) is evaluated on 804 questions, but all other models use only 60 questions (or 48 for QwQ-32B). At N=60, the statistical power to detect even a 5pp difference is low. The cross-family "validation" (Table 4) with p-values of 0.42–0.48 is essentially noise. Claims about cross-family consistency of the C0 pattern are confounded by insufficient sample size—we cannot distinguish "consistent null effect" from "underpowered to detect anything."

### W5: The "Interpretable Tiebreaking" Contribution Is Overstated (Moderate)
SICA's 57.8% tiebreak accuracy vs. 50% random is based on 45 ties. A two-sided binomial test for 26/45 vs. 50% gives p≈0.35—not significant. Claiming this as a contribution ("auditable, constraint-based justifications") when the accuracy advantage itself is indistinguishable from chance is misleading. The interpretability argument would need user studies or qualitative evidence that the audit trails are actually useful in practice.

### W6: Missing Baselines and Comparisons (Moderate)
The paper compares SICA only to vanilla SC variants (random, deterministic). Several relevant alternatives are absent:
- **Confidence-weighted SC** (using log-probabilities or calibrated confidence)
- **Debate/refinement approaches** where traces are iteratively improved
- **Verifier-based methods** (e.g., using a separate verifier model to score candidates)
- **Logic-LM** (Pan et al., 2023), cited but not compared against experimentally

Without these, we cannot assess whether SICA's failure is specific to its FOL+MAX-SAT approach or reflects a general limitation of post-hoc consensus enhancement.

### W7: C0 Correlation Analysis Is Underpowered (Minor)
The Pearson correlation of r=0.28 (p=0.43) between C0 and accuracy gap is computed over only 10 data points (Section 4.2). With N=10, even strong correlations (|r|>0.6) would struggle for significance. The paper correctly notes this is non-significant but still uses it as evidence for "C0 does not predict gain magnitude." A non-significant result with N=10 is absence of evidence, not evidence of absence.

### W8: Domain Coverage Is Narrow (Minor)
All substantive evaluation is on two logic NLI benchmarks (FOLIO, ProofWriter) with a 30-question GSM8K pilot. Logic reasoning is arguably the most favorable domain for FOL constraint extraction. If SICA fails here, there is little reason to expect success elsewhere—but the paper cannot claim generality of its findings beyond logic tasks. Commonsense reasoning, code generation, and scientific reasoning are all mentioned only in limitations.

---

## Detailed Questions for Authors

1. **Oracle constraint experiment**: Have you evaluated SICA with ground-truth or manually verified constraints on a subset? This would directly test whether the method *could* work with better extraction, separating method soundness from extraction quality.

2. **Per-question analysis**: For the 804 expanded questions, can you correlate per-question constraint extraction quality (even a proxy like extraction rate or constraint count) with SICA correctness? This would provide quantitative support for the dual-condition claim beyond 8 case studies.

3. **Why not improve extraction?** Multi-round extraction, self-verification, or a fine-tuned extractor are mentioned as future work but are feasible within the current setup. Even a simple "extract twice and keep consensus constraints" could test whether extraction quality improvements translate to SICA gains.

4. **FOLIO vs. ProofWriter divergence**: FOLIO consistently shows positive trends while PW is negative. Is this solely about extraction quality, or does PW's synthetic structure introduce systematic biases in FOL extraction? A per-dataset constraint quality comparison would clarify.

5. **Temperature sensitivity**: All experiments use T=0.7. C0 is directly affected by temperature. Have you explored the C0-gap relationship at different temperatures (e.g., T=1.0, T=0.5)?

---

## Experiment Coverage Assessment

Comparing against the full experiment design:
- **14 planned experiments**: All 14 are covered in the paper (expanded evaluation, K ablation, tiebreak analysis, 7B/72B/Mistral/LLaMA scaling, QwQ/DeepSeek-R1 regime, C0 diagnostic, constraint quality, overhead, GSM8K pilot, constraint ablation).
- **Coverage is complete** in breadth. The main gap is depth: the constraint quality analysis (exp-008) is central to the narrative but uses only 8 examples, far fewer than would be needed to support the claims built upon it.

---

## Minor Issues

- Table 1: QwQ-32B rows show "—" for SC and SICA accuracy. If accuracy was computed, it should be reported; if not, explain why.
- Section 4.4: The cross-family results paragraph references "consistent C0 patterns" but the actual C0 values vary substantially (0.30–0.65), which is a 2× range. "Consistent" is misleading; "all above 20%" would be more accurate.
- The 72B model uses 4-bit AWQ quantization. Quantization can affect output diversity (and thus C0). This confound is not discussed.
- Reference [3] is cited twice (Pan et al., 2023) for both a survey and Logic-LM. These appear to be different papers that should have separate entries.
- The paper claims "zero-cost diagnostic" for C0, but computing C0 requires running K traces, which is the same cost as SC. C0 is zero *marginal* cost over SC, not zero cost.

---

## Verdict

This paper presents a thorough negative result with good experimental coverage, but the analytical contributions offered as a pivot are insufficient for a top venue. The operating regime characterization is near-tautological (no disagreement → no improvement), the constraint quality bottleneck claim rests on 8 examples, and no attempt is made to validate the diagnosis by improving extraction quality. The paper would be significantly strengthened by: (1) an oracle constraint experiment proving SICA works in principle, (2) a scaled-up automated constraint quality assessment, and (3) at least one extraction improvement attempt showing the dual-condition theory has predictive power. In its current form, the paper reads as a well-executed postmortem of a failed method rather than a paper with actionable new knowledge for the community.

**Recommendation: Reject (3/6)** — Below the acceptance threshold for a top ML venue. The negative result is valuable but the analytical pivot does not constitute sufficient contribution. Resubmission with oracle experiments and improved extraction validation could elevate the work to borderline-accept territory.