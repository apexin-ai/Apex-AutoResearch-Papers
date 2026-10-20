---
dream_id: dream_20260515T071730
tier: median
overall_score: weak reject
timestamp: 2026-05-15T08:01:15.732587+00:00
---

# Dream Review Report: Cross-Representation Disagreement for Diagnosis and Characterization of LLM Formalization Errors

**Dream ID**: 20260515T071730
**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)
**Date**: 2026-05-15

---

## Roundtable Summary

Two independent reviewers (R1: Methods+Experiments; R2: Novelty+Related Work) converged on **3/6 (Weak Reject)** with high confidence (4/5). The paper presents a thorough empirical analysis with some genuinely novel findings (domain-dependent asymmetry reversal, GT-label-dependent repair effect, formalization bottleneck gradient), but the methodological novelty is incremental, the strongest claims require oracle ground-truth labels unavailable at deployment, the error taxonomy lacks non-LLM validation, and CRD underperforms self-consistency on 2 of 3 benchmarks. Findings track would be appropriate with targeted revisions.

---

## Consolidated Scores

| Criterion | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3/4 | 3/4 | 3/4 |
| Presentation | 3/4 | 3/4 | 3/4 |
| Contribution | 2/4 | 2/4 | 2/4 |
| Overall | 3/6 | 3/6 | **3/6 (Weak Reject)** |
| Confidence | 4/5 | 4/5 | 4/5 |

---

## Strengths (Consensus)

1. **Rigorous and transparent statistical reporting.** Bootstrap CIs, Fisher exact tests, McNemar tests, and Bonferroni correction across 12 tests. Dual reporting of C5-committed (94.6%) vs. C5-coverage (53%) is exemplary. Confidence intervals for C4 explicitly include zero and this is stated rather than hidden.

2. **Domain-dependent asymmetry reversal is a genuinely novel empirical finding.** FOL-favored 5.6:1 on FOLIO vs. near-parity 1.8:1 on MATH demonstrates that representation advantage is task-dependent, not a fixed verifier hierarchy. No prior work has shown this.

3. **GT-label-dependent three-way split transforms a null result into an informative finding.** Unknown (+14.7pp), False (+6.7pp), True (-13.6pp) — each individually informative. The mechanistic explanation via Code overclaiming on three-valued logic is convincing.

4. **Unusually honest boundary characterization.** ProofWriter pilot failure (6.7%), GPQA degradation (C2=58%), "more disagreement ≠ better diagnosis" on 8B model, aggregate C4 non-significance — all transparently reported. The domain gradient (FOLIO > LogiQA > MATH > GPQA) mapping when CRD works vs. doesn't is a genuine contribution.

5. **Well-supported cost-efficiency argument.** 2 LLM calls vs. 5 for SC5, with qualitative advantages (error type classification, localization, paradigm characterization) that SC5 fundamentally cannot provide. The 0.40× cost ratio is consistent across benchmarks.

6. **Comprehensive experimental coverage.** 13 experiments across 4 benchmarks, 3 model conditions, 2 model scales, selection vs. repair, taxonomy ablation, multi-round repair, and correlated failure analysis. The design space is well-explored.

---

## Weaknesses (Consensus, by severity)

### Major

**W1. Aggregate C4 is non-significant on every benchmark; the actionable stratified analysis requires ground-truth labels unavailable at deployment.** The paper's most analytically interesting finding (GT-label-dependent repair effect) cannot be operationalized without oracle GT access. The paper suggests "skip repair for high-confidence True predictions" but never evaluates whether CRD's own signals (stability score, error type, asymmetry) can predict GT-label category. Without a GT-free deployment evaluation, Claim 3 is a retrospective insight, not an actionable method. Selection (82.8%) is barely above blind baseline (81.4%), a +1.4pp gain that is unlikely to be significant.

**W2. Incremental novelty over Liang et al. (2024).** The core observation that cross-representation disagreement is informative was established by Liang et al. (2024) for CoT-PoT pairs. This paper extends from binary filtering to diagnosis + taxonomy + localization + repair, but each component individually uses known techniques: rule-based error classification (standard in SE), perturbation-based fault localization (metamorphic testing), and diagnosis-informed re-prompting (Self-Debug, Self-Refine). The paper's own data shows selection captures most of the benefit at zero additional cost, suggesting the diagnostic machinery adds modest marginal value over the basic disagreement signal.

**W3. The error taxonomy lacks non-LLM validation.** Cross-model κ=0.54 (3-type merged) is only "moderate agreement." The most theoretically interesting category (quantifier_error, n=4, κ=0.22) is essentially noise. No human expert annotation is provided on any subsample. Two LLMs agreeing on error labels could reflect shared superficial heuristics. The taxonomy ablation (McNemar p=0.68) confirms the taxonomy is descriptive not prescriptive — but then its contribution reduces to descriptive analysis with unvalidated categories.

**W4. CRD loses to self-consistency on 2 of 3 benchmarks.** On LogiQA, SC5-Best outperforms CRD by 4.0pp; on MATH, by 9.0pp. CRD's precision advantage is limited to FOLIO (+2.2pp), the benchmark most favorable to FOL+Z3. The cost argument (0.40×) partially compensates, but a method that is less accurate on 2/3 benchmarks needs stronger justification.

**W5. Significant related work gaps.** Critical omissions:
- N-version programming (Avizienis & Chen, 1977; Avizienis, 1985) — the foundational paradigm for using implementation diversity to detect faults. CRD is essentially N-version programming for LLM formalizations. The "paradigm distance modulates effectiveness" finding directly parallels the "design diversity" literature.
- PAL (Gao et al., 2023) — the canonical reference for LLM-generated Python program solving, direct lineage of the Code pathway.
- Metamorphic testing (Chen et al., 1998) — stability-based localization is essentially a metamorphic relation.
- DIVERSE (Li et al., 2023) and Universal Self-Consistency (Chen et al., 2024) — closer baselines than vanilla SC5.
- Debate-based verification (Irving et al., 2018) — cross-representation disagreement as restricted debate.

### Moderate

**W6. The MATH instantiation conflates "cross-paradigm" with "cross-library."** SymPy symbolic vs. Python numerical are both imperative Python with no formal verification guarantees. This is categorically different from FOL+Z3 vs. Python. The paper's own data confirms the problem: CRD advantage evaporates on MATH (-9pp vs SC5). The framework's conceptual unity is weakened without a principled criterion for "sufficient representation diversity."

**W7. C5 coverage of 53% means the localization module provides no actionable signal on nearly half of diagnostic cases.** The 47% ambiguous rate is driven by GT=Unknown (61% ambiguous) — precisely where repair delta is largest. This creates a paradox: the subgroup where CRD is most useful is the subgroup where localization is least reliable.

**W8. Sample sizes are thin for the extensive stratification.** With n=204 on FOLIO and stratification by GT-label (3), error type (4), cross-model conditions (3), and repair rounds (3), many subgroup analyses rest on n<20. Quantifier_error (n=4) appears in multiple tables as if carrying analytical weight. The reported Bonferroni correction covers 12 tests, but actual comparisons across 11+ tables likely exceed 50.

### Minor

**W9. False agreement rate of 26.1% on GT=Unknown is high and underexplored.** One in four Unknown samples produces false agreement. CRD provides no signal for these and may increase confidence in incorrect answers.

**W10. "Paradigm distance modulates effectiveness" is post-hoc and circular.** The gradient could reflect benchmark difficulty, formalization quality, or evaluation protocol differences. No independent measure of paradigm distance is provided.

**W11. Incomplete bibliography entries.** Several references (HybridMind, VeriCoT, Roundtrip) lack full author lists. For a top-venue submission, every citation needs complete bibliographic information.

---

## Questions for Authors (Priority-ordered)

1. **GT-free deployment evaluation**: Have you evaluated a pipeline where repair/selection decisions use only CRD's own signals (stability score, error type, asymmetry direction) rather than oracle GT labels? What accuracy does this achieve? This is critical for Claim 3's practical relevance.

2. **N-version programming connection**: How does CRD relate to N-version programming (Avizienis, 1985)? The conceptual parallel — generating diverse implementations and comparing outputs to detect faults — is striking. The "design diversity" finding directly parallels your "paradigm distance" observation. Why is this connection not discussed?

3. **SC5 comparison at k<5**: At what k does self-consistency match CRD's diagnostic precision? If k=3 suffices, the cost argument weakens substantially.

4. **Human taxonomy validation**: Could you provide human expert annotations on 30-50 diagnostic cases? Cross-model κ=0.54 with two LLMs is suggestive but insufficient.

5. **Asymmetry without exec_crash**: What happens to the 5.6:1 asymmetry ratio if exec_crash errors are excluded? Are logic_error and negation_error individually asymmetric in the same direction?

6. **C2 inflation by asymmetry**: If FOL is correct 5.6× more often than Code among disagreements, a trivial "always trust FOL" baseline achieves high C2 by construction. What is C2 when conditioning on Code-correct-FOL-wrong cases only?

7. **Stability test calibration**: Is there a threshold of perturbation agreement above which localization is near-perfect, enabling higher-coverage deployment at a controlled precision level?

---

## Experiment Coverage Assessment

All 13 imagined experiments from the review context are covered in the paper:

| Experiment | Coverage | Section |
|-----------|----------|---------|
| exp-002 Cross-Model Ablation | ✓ Full | §5.6 |
| exp-003 ProofWriter→LogiQA | ✓ Full | §5.7 |
| exp-004 MATH Level 5 | ✓ Full | §5.7 |
| exp-005 Multi-round Repair | ✓ Full | §5.4 |
| exp-006 Unknown Analysis | ✓ Full | §5.5 |
| exp-007 Selection vs Repair | ✓ Full | §5.3 |
| exp-008 Taxonomy Ablation | ✓ Full | §5.4 |
| exp-009 Statistical Significance | ✓ Full | §5.9 |
| exp-010 Scale Ablation (8B) | ✓ Full | §5.10 |
| exp-011 GPQA Diamond | ✓ Full | §5.7 |
| exp-012 SC5 Comparison | ✓ Full | §5.2 |
| exp-013 Taxonomy Validation | ✓ Full | §5.8 |

Experiment coverage is complete. No imagined experiments are missing from the paper.

---

## Missing Experiments / Suggested Additions

1. **GT-free deployment evaluation** (Critical): Train a lightweight classifier on CRD features to predict repair benefit. Evaluate on held-out data. This would make Claim 3 actionable.

2. **Human expert annotation** (Critical for taxonomy): ≥50 samples annotated by domain experts. Compute human-LLM κ for the taxonomy to validate it captures genuine error categories.

3. **Roundtrip Verification comparison**: Empirical head-to-head on an overlapping benchmark to demonstrate cross-representation advantage over within-representation roundtrip.

4. **SC5 at k=3**: If k=3 SC achieves comparable precision to CRD, the 0.40× cost advantage shrinks to ~0.67×, weakening a core argument.

5. **C2 decomposition by asymmetry direction**: Report C2 separately for FOL-correct-Code-wrong vs. Code-correct-FOL-wrong to address the "always trust FOL" inflation concern.

---

## Recommendation

**Overall: 3/6 (Weak Reject) for top ML venue main track.**

The paper's strongest contributions are empirical findings (asymmetry reversal, GT-dependent effect, formalization bottleneck gradient) rather than methodological advances. The framework is a competent composition of known techniques with incremental novelty over Liang et al. (2024). The most actionable claim (Claim 3) requires oracle labels; the taxonomy (Claim 2) lacks non-LLM validation; and CRD underperforms SC5 on 2/3 benchmarks (undermining Claim 1's generality).

**Path to acceptance**: (1) Add GT-free deployment evaluation to make Claim 3 actionable; (2) Provide human annotation for taxonomy validation; (3) Complete the related work (N-version programming, PAL, metamorphic testing); (4) Reframe the MATH results honestly as a reduced-paradigm-gap condition. With these revisions, the paper would be competitive for **Findings track** (EMNLP Findings) or a **neurosymbolic reasoning workshop**.

The paper's transparency about limitations and honest reporting of negative findings (non-significant C4, ProofWriter failure, GPQA boundary) is commendable and should be preserved in revision.
