---
dream_id: dream_20260515T071730
tier: best
overall_score: 3/6 Weak Reject
timestamp: 2026-05-15T07:54:32.797062+00:00
---

# Dream Review Report: Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors

**Dream ID:** 20260515T071730
**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-15

---

## Consolidated Score: 3/6 (Weak Reject)

Both reviewers independently scored 3/6. After cross-sharing and roundtable discussion, the panel converges on **Weak Reject** with recognition that the analytical contributions are solid but insufficient to overcome methodological and novelty concerns at a top ML venue (~25% acceptance rate).

---

## Panel Summary

The paper presents Cross-Representation Disagreement Diagnosis (CRD), extending cross-representation disagreement from binary filtering to structured error diagnosis. Given a reasoning problem, CRD generates dual executable formalizations (FOL+Z3 and Python), detects disagreements, classifies errors into a 4-type taxonomy, localizes the faulty side via stability testing, and optionally performs diagnosis-guided repair. Evaluated on 3 primary benchmarks (FOLIO, LogiQA, MATH Level 5) plus GPQA Diamond, with 2 primary models (Qwen3-32B, DeepSeek V4 Pro) and 1 ablation model (Qwen3-8B).

The paper's strongest contribution is empirical characterization: the asymmetry reversal across domains (FOL-favored 5.6:1 in logic vs. Code-favored 1.8:1 in math) is a genuinely novel finding, and the GT-label-dependent repair effect with honest boundary reporting (True overcorrection at −11.2pp) demonstrates intellectual rigor. However, the aggregate repair improvement (C4) is non-significant on every benchmark, the core stratified analysis requires oracle GT labels unavailable at inference, and the novelty over Liang et al. (2024) is incremental.

---

## R1 Review: Methods & Experiments

**Score:** 3/6 | **Confidence:** 4/5

### Strengths

- **S1: Well-characterized diagnostic signal with honest statistical reporting.** Bootstrap CIs, Fisher exact tests, and McNemar tests are applied throughout. The paper is upfront that aggregate C4 is non-significant (p=0.626). The GT-stratified three-way split (Unknown +14.7pp → +22.1pp, False +6.7pp → +10.4pp, True −13.6pp → −11.2pp) transforms a negative result into an informative boundary. Dual reporting of C5-committed (94.6%) and C5-coverage (53.0%) is transparent.

- **S2: Multi-benchmark generalization with meaningful effectiveness gradient.** The C2 trajectory (FOLIO 87.2% → LogiQA 81.5% → MATH 76.0% → GPQA 72.7%) traces a clear boundary: CRD is most effective when errors arise from formalization rather than domain knowledge gaps. The ProofWriter pilot failure (6.7% disagreement) and its honest reporting strengthens the boundary characterization. The asymmetry reversal on MATH is a substantive cross-domain finding.

- **S3: Cost-efficiency framing is compelling.** CRD achieves 2 calls vs. 5 for self-consistency at 40% token cost, with qualitative advantages (error type, localization, paradigm characterization) over SC5's binary majority vote signal.

### Weaknesses

- **W1: Aggregate C4 is non-significant on every benchmark, and the stratified analysis relies on GT labels unavailable at inference.** The method provides no statistically significant overall accuracy improvement. The GT-label-stratified analysis (Claim 3's core) requires knowing ground truth to decide whether to apply repair. The paper suggests "skip repair for high-confidence True predictions" but never evaluates whether CRD's own signals can predict GT-label category, nor demonstrates a realistic GT-free deployment pipeline.

- **W2: No human annotation baseline for taxonomy validation.** Cross-model κ=0.67 uses LLM-to-LLM agreement, which is circular — two LLMs may agree on superficial patterns rather than genuine error categories. The most theoretically interesting category (quantifier_error, n=4, κ=0.45) is essentially unvalidated. Without human expert annotation on even a subsample, there is no ground truth for whether the taxonomy is meaningful.

- **W3: The self-consistency comparison has inconsistencies across benchmarks.** CRD outperforms SC5 by +7.9pp on FOLIO but only +1.2pp on MATH. An equally valid reading is that CRD works well specifically on benchmarks designed for FOL translation (FOLIO) and degrades when paradigm distance shrinks. The cost argument also omits CRD's infrastructure requirements (Z3 solver, Python sandbox, diagnosis pipeline).

- **W4: Sample sizes are marginal for the many stratified analyses performed.** n=204/200/200/150 is reasonable for primary metrics but thin for the extensive stratification: quantifier_error has n=4, cross-model ablation has 3 conditions, several Fisher exact tests on small subgroups. Multiple comparisons inflate false discovery risk despite the claimed corrections.

- **W5: The MATH extension (SymPy vs. Python numerical) is a fundamentally different instantiation.** Neither representation has a formal verification guarantee, unlike FOL+Z3. Grouping them under "CRD" without adequately discussing whether the framework genuinely applies when both sides are imperative Python variants weakens the conceptual unity.

### Questions for Authors

- Q1: Have you evaluated a realistic deployment scenario where repair/select decisions use CRD's own signals (stability test, error type, asymmetry) rather than GT labels? What accuracy does GT-free selection achieve?

- Q2: Could you provide human expert annotations on a subsample (e.g., 50 diagnostic cases) to validate the taxonomy against a non-LLM ground truth?

---

## R2 Review: Novelty & Related Work

**Score:** 3/6 | **Confidence:** 4/5

### Strengths

- **S1: The asymmetry reversal is a genuinely novel empirical finding.** No prior work has demonstrated that cross-representation disagreement direction reverses across domains (FOL-favored in logic, Code-favored in math), revealing domain-specific representation strengths rather than a fixed verifier hierarchy. This finding alone has conceptual value beyond the CRD framework.

- **S2: Honest boundary characterization elevates the paper's intellectual contribution.** The GT=True overcorrection (−11.2pp), ProofWriter's 6.7% failure, GPQA's C2=72.7% boundary, and the C1↑C2↓ tradeoff on Qwen3-8B are all reported transparently. This gives the reader a nuanced understanding of when CRD works and when it doesn't — more valuable than presenting only favorable conditions.

- **S3: Comprehensive experimental coverage.** 18 tables across 13 experiments spanning 4 benchmarks, 3 models, and multiple ablation axes. The paper addresses correlated failures (phi=0.189, false agreement 12.3%), selection vs. repair decomposition, taxonomy-guided vs. fixed-strategy, model scale effects, and cross-domain boundaries.

### Weaknesses

- **W1: Incremental novelty over Liang et al. (2024).** The "filtering to diagnosis" extension combines individually known techniques: rule-based error classification (standard in software engineering), perturbation-based localization (established in program debugging), and diagnosis-informed prompting (common in self-refinement literature). The paper's contribution is their composition, not a conceptual advance. The key differentiator — that disagreement patterns are diagnostically rich — is stated as a finding but the taxonomy itself is ad hoc (rule-based, 4 categories, no formal derivation).

- **W2: Significant related work gaps.** Missing comparisons: (a) PAL (Gao et al., 2023) and Program-of-Thought (Chen et al., 2023) — the direct lineage of the Code representation path; (b) Universal Self-Consistency (Chen et al., 2024) — extends self-consistency to free-form answers, directly relevant to the SC5 comparison; (c) DIVERSE (Li et al., 2023) — diverse verifier with voting, a closer baseline than vanilla SC5; (d) inadequate discussion of Roundtrip Verification (Zhong et al., 2025), which performs diagnosis-guided repair within a single representation on traffic rules — the paper cites it but doesn't explain why cross-representation is fundamentally better than within-representation roundtrip for general domains.

- **W3: Incomplete bibliography entries.** PROVE, VERGE, VeriCoT, HybridMind, Adaptive Representation Selection, and Roundtrip Verification references all lack full author lists (listed as "Author et al." or "Anonymous"). For a venue submission, these need complete citation information or should be removed.

- **W4: MATH domain conflation weakens the conceptual framing.** SymPy symbolic vs. Python numerical is "cross-library" not "cross-paradigm" in the same sense as FOL+Z3 vs. Python. Both are imperative Python code; the paradigm gap is much smaller. The paper's own data confirms this: CRD advantage over SC5 is only +1.2pp on MATH vs. +7.9pp on FOLIO. This undermines the generality claim — CRD may be primarily a FOL-vs-Code diagnostic tool rather than a general cross-representation framework.

- **W5: Taxonomy coverage is unvalidated and has mixed granularity.** No analysis of out-of-taxonomy errors (what fraction of disagreements don't fit any of the 4 types?). negation_error is arguably a subtype of logic_error; exec_crash is operational rather than reasoning-related. The taxonomy mixes abstraction levels without justification. The paper claims "rule-based for interpretability" but provides no inter-annotator study of the rules themselves.

- **W6: The "paradigm distance modulates CRD effectiveness" discussion point is post-hoc.** The gradient (FOLIO > LogiQA > MATH) could equally reflect benchmark difficulty, formalization quality, or evaluation protocol differences rather than paradigm distance per se. No independent measure of paradigm distance is provided; it is inferred circularly from CRD's own effectiveness.

### Questions for Authors

- Q1: How does CRD compare to Roundtrip Verification (Zhong et al., 2025) when both are applied to the same benchmark? Is cross-representation diagnosis fundamentally more informative than within-representation roundtrip, or just differently scoped?

- Q2: What fraction of FOLIO disagreement samples fall outside the 4-type taxonomy? If the taxonomy has ≥90% coverage, what is the evidence? If <90%, the uncovered cases may contain systematic patterns worth characterizing.

---

## Roundtable Synthesis

### Areas of Agreement (Both Reviewers)

1. **The asymmetry reversal and GT-label-dependent effect are genuine contributions.** These empirical findings are novel, non-obvious, and would be of interest to the neurosymbolic reasoning community regardless of CRD's practical utility.

2. **The GT-oracle problem is a critical limitation.** Both reviewers flag that Claim 3's core finding requires ground-truth labels for stratification, making the most interesting results practically unactionable without additional work on GT-free deployment.

3. **Aggregate repair improvement is non-significant everywhere.** This fundamentally limits the paper's practical contribution — CRD is characterized as a diagnostic/analytical tool, not a method that reliably improves accuracy.

4. **The MATH extension weakens the paradigm-distance narrative.** SymPy vs. Python numerical is a much smaller paradigm gap than FOL+Z3 vs. Python, and the CRD advantage shrinks correspondingly (+1.2pp). This is consistent but also reveals that CRD's value proposition depends heavily on having maximally different representation paradigms.

5. **Honest, thorough reporting is a significant positive.** The paper does not hide negative results (C4 non-significance, GT=True overcorrection, ProofWriter failure, GPQA boundary). This intellectual honesty is appreciated and elevates the analytical contribution.

### Areas of Disagreement

- **Severity of novelty concern:** R2 views the contribution as incremental over Liang et al. (2024) (composition of known techniques), while R1 is more sympathetic to the diagnostic signal characterization as a standalone contribution. After discussion, both agree that the empirical findings (asymmetry reversal, GT-dependent effect) are more novel than the framework itself.

- **Taxonomy validation sufficiency:** R1 emphasizes the need for human annotation; R2 focuses on taxonomy coverage and granularity. Both agree the current validation (κ=0.67 LLM-to-LLM) is insufficient for a top venue.

### Verdict

The paper presents a thorough empirical study with some genuinely interesting findings (asymmetry reversal, GT-dependent repair boundary). However, at a top ML venue with ~25% acceptance:

- The framework novelty is incremental (composition of known techniques applied to cross-representation disagreement)
- The practical utility is limited (no significant aggregate improvement; stratified improvements require oracle GT labels)
- The taxonomy lacks rigorous validation (no human annotation, mixed granularity, tiny n for key categories)
- The generalization argument weakens outside the FOL+Z3 vs. Python paradigm gap
- Related work coverage has notable gaps

**Recommendation:** Weak Reject. The analytical findings deserve publication but the paper needs: (1) a GT-free deployment evaluation, (2) human annotation for taxonomy validation, (3) complete related work coverage including PAL/PoT and DIVERSE, and (4) clearer scoping of claims to the FOL-vs-Code setting where the paradigm gap is genuinely large.

---

## Actionable Revision Suggestions (Priority-Ordered)

1. **[Critical] Evaluate GT-free repair selection.** Train a simple classifier or heuristic on CRD signals (error type, stability score, asymmetry direction) to predict repair benefit without GT labels. Report accuracy on held-out FOLIO samples. This directly addresses the oracle problem and could salvage Claim 3's practical relevance.

2. **[Critical] Add human expert annotation on ≥50 diagnostic samples.** Compute human-LLM κ and human-human κ on the 4-type taxonomy. This is the minimum bar for claiming the taxonomy is meaningful rather than an LLM artifact.

3. **[Important] Close related work gaps.** Add PAL, Program-of-Thought, Universal Self-Consistency, and DIVERSE. Provide a substantive comparison with Roundtrip Verification explaining why cross-representation diagnosis adds value over within-representation roundtrip.

4. **[Important] Scope MATH claims more carefully.** Either demonstrate that SymPy vs. Python numerical qualifies as "cross-paradigm" by some independent measure, or explicitly position MATH as a "reduced paradigm gap" condition that tests CRD's limits rather than its generality.

5. **[Moderate] Fix incomplete references.** Provide full author lists for all citations. Remove or replace any that cannot be properly cited.

6. **[Moderate] Report taxonomy coverage.** State what fraction of disagreement samples are classified into the 4 types vs. falling outside the taxonomy. If there is a residual "other" category, characterize it.

7. **[Minor] Discuss multiple comparison correction.** With 18 tables and many stratified tests, explicitly state the family-wise error control strategy (Bonferroni, Holm, or FDR).
