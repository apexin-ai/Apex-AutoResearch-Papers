# Paper Framing — cross_representation_disagreement_diagno

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026 (10 days)
- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage

## Core Insight
When the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This "disagreement as diagnostic" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.

## Core Claims (3 条)

### Claim 1: Disagreement as High-Precision Diagnostic Signal
When the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.

**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).

### Claim 2: Error Classification and Conditional Localization
Disagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is 94.6%. The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.

**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return "ambiguous" (especially Unknown: 61%). C3=4 error types.

**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.

**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled "the error."

### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral
Diagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:

| GT Label | n | Targeted | Blind | Delta | Interpretation |
|----------|---|----------|-------|-------|----------------|
| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |
| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |
| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |

This is NOT simply "conditional advantage" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal ("Code disagrees with FOL") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.

**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.

**Presentation strategy**: 
1. Report C4 stratified by GT label as the PRIMARY result (table above)
2. Aggregate C4 only as context, with explicit caveat about non-significance
3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness
4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)

## Story Spine

- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.

- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.

- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).

- **Headline result template**: "On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation."

## Venue Fit

- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.
- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.
- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.

## Anticipated Reviewer Concerns & Responses

| # | Concern | Response Strategy | Required Experiment |
|---|---------|-------------------|---------------------|
| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |
| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |
| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |
| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |
| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |
| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |
| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |
| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |
| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |
| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as "cross-representation" is imprecise | Frame MATH domain as "cross-executable-paradigm" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |
| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |
