---
dream_id: dream_20260515T071730
tier: worst
overall_score: Weak Reject (3/6)
timestamp: 2026-05-15T08:07:16.085811+00:00
---

# Dream Review Report

**Paper:** "When Do Two Formalizations Know More Than One? An Empirical Study of Cross-Representation Disagreement in LLM Reasoning"
**Review Mode:** Full (2 Reviewers + Roundtable)
**Target Venue Standard:** Top ML venue (~25% acceptance rate, 6-point scale)

---

## Roundtable Summary

Both reviewers independently scored the paper **3/6 (Weak Reject)** with **4/5 confidence**. After cross-sharing reviews, all major assessments converged with no score changes. The reviewers agree that the paper demonstrates commendable statistical honesty and provides genuinely novel empirical observations (asymmetry reversal, GT-label-dependent repair boundaries), but the aggregate contribution falls below the bar for a top venue main track due to non-significant core results, oracle-dependent actionability, and incremental methodological novelty.

---

## R1 Review: Methods and Experiments (Score: 3/6, Confidence: 4/5)

### Strengths
- **S1: Rigorous and transparent statistical methodology.** Bootstrap 95% CIs for all primary metrics, Fisher exact tests, McNemar tests, dual reporting of C5-committed (94.6%) vs. C5-coverage (53.0%). The paper is upfront that aggregate C4 is non-significant on every benchmark (FOLIO p=0.626, LogiQA p=0.71, MATH p=0.82). This level of statistical honesty is rare and commendable.
- **S2: Well-defined 4-stage pipeline with clear evaluation criteria.** The CRD pipeline is precisely specified and the 5 evaluation criteria (C1-C5) provide a comprehensive framework that cleanly separates signal detection, signal quality, error characterization, downstream utility, and localization precision.
- **S3: Comprehensive experimental coverage.** All planned experiments appear executed: core FOLIO analysis, cross-model ablation, ProofWriter pilot/LogiQA fallback, MATH extension, multi-round repair, correlated failure analysis, selection vs repair, taxonomy ablation, statistical significance tests, self-consistency baseline, and taxonomy cross-validation.
- **S4: GT-label-stratified analysis transforms a null result into an informative finding.** The three-way split (Unknown +14.7pp, False +6.7pp, True −13.6pp) is more scientifically valuable than a marginal aggregate positive. The mechanistic explanation via Code overclaiming (73.9% on GT=Unknown) is convincing and testable.
- **S5: Domain-dependent asymmetry reversal is genuinely novel.** FOL>Code 5.6:1 on FOLIO vs. Code>FOL 1.8:1 for DeepSeek. No prior work has documented this model-dependent reversal of representation advantage.

### Weaknesses
- **W1: Aggregate C4 is non-significant on every benchmark, and the actionable stratified analysis requires oracle GT labels.** The GT-label-stratified repair effect requires knowing ground truth to decide whether to apply repair. The paper never evaluates whether CRD's own signals (stability score, error type) can predict GT-label category or repair benefit. Without a GT-free deployment evaluation, the stratified findings are retrospective analytical insights, not actionable methods. Meta-analytic C4 of +2.9pp (CI [−2.1%, +7.9%]) confirms the aggregate effect is negligible.
- **W2: No human annotation baseline for taxonomy validation.** Cross-model κ=0.33 (4-type) is "fair agreement," well below the 0.60 threshold for reliable classification. Two LLMs may agree on superficial patterns rather than genuine error categories. Without human expert annotation on even 30–50 samples, the taxonomy's validity is ungrounded.
- **W3: Sample sizes are marginal for the extensive stratification performed.** FOLIO n=204 with stratification by GT-label (3), error type (4), cross-model conditions (3), repair rounds (3) yields many subgroups with dangerously small n. Quantifier_error (n=4) appears in multiple tables as if carrying analytical weight. The Bonferroni correction covers 12 tests, but actual comparisons across 16+ tables likely exceed 50, creating substantial false discovery risk.
- **W4: The MATH extension (SymPy vs. Python numerical) is categorically different from FOL+Z3 vs. Python.** Both MATH representations are imperative Python code with no formal verification guarantee—this is "cross-library" not "cross-paradigm." The paper's own data confirms this: C2 drops to 51.5% (coin-flip accuracy), and 48.5% of disagreements are noise. Including MATH under the unified "CRD" framework weakens conceptual coherence.
- **W5: Self-consistency comparison may understate SC5's advantage.** SC5-FOL achieves 84.8% end-to-end accuracy at 5× cost vs. CRD's 69.1% at 5.76× cost—a 15.7pp gap. Even SC3-FOL (83.3% at 3× cost) surpasses CRD. CRD is Pareto-dominated on cost-accuracy across all three benchmarks (cost ratios 0.38–0.42). The cost analysis also omits CRD infrastructure requirements (Z3 solver, Python sandbox, stability test with k=3 additional calls per disagreement).
- **W6: C5 coverage of 53% means localization is uninformative on nearly half of diagnostic cases.** The 47% ambiguous rate is highest on GT=Unknown (61%)—the exact subgroup where repair delta is largest. This creates a paradox: where CRD is most useful, localization least often provides definitive signal.

### Questions for Authors
- Q1: Have you evaluated a GT-free deployment pipeline where repair/selection decisions use only CRD's own signals?
- Q2: What is CRD's end-to-end accuracy (including non-disagreement samples) vs. SC5 on each benchmark?
- Q3: Why does repair help on GT=Unknown (+14.7pp) when localization is ambiguous 61% of the time?
- Q4: Could you provide human expert annotations on 30–50 diagnostic cases to validate the taxonomy?
- Q5: How many total statistical tests were performed across all tables? The Bonferroni correction over 12 tests likely understates the multiple comparison burden.

---

## R2 Review: Novelty, Positioning, and Related Work (Score: 3/6, Confidence: 4/5)

### Strengths
- **S1: The domain-dependent asymmetry reversal is novel and non-obvious.** The gradient from FOLIO (5.6:1 FOL-favored) through LogiQA (2.1:1) to MATH (1.4:1 Python-favored) demonstrates task-dependent representation advantage. The cross-model ablation (DeepSeek reversing to Code>FOL 1.8:1) further separates model-level from representation-level effects. No prior work has characterized this.
- **S2: Unusually honest statistical reporting.** The paper does not hide negative results. Aggregate C4 non-significance is stated plainly, ProofWriter pilot failure (4.0%) is transparently reported, and the dual C5 reporting (committed vs. coverage) is exemplary.
- **S3: The GT-label-dependent three-way split is an informative boundary characterization.** Unknown +14.7pp / False +6.7pp / True −13.6pp with mechanistic Code-overclaiming explanation is more valuable than the non-significant aggregate alone.
- **S4: Cost-efficiency argument and qualitative advantages are clearly articulated.** "SC reveals that something may be wrong; CRD reveals why" is a crisp distinction, though the paper's own data shows the "why" does not translate to better repair.

### Weaknesses
- **W1: Incremental novelty over Liang et al. (2024).** The core observation—cross-representation disagreement is diagnostically informative—was established by Liang et al. for CoT-PoT pairs. This paper extends from binary filtering to diagnosis + taxonomy + localization + repair, but each component employs known techniques: rule-based error classification, perturbation-based fault localization, and diagnosis-informed re-prompting (Self-Debug, Self-Refine). The paper's own data shows selection (zero additional cost) outperforms repair by 6.1pp, suggesting the diagnostic machinery beyond basic disagreement detection adds modest marginal value.
- **W2: Significant related work gaps.** Missing connections: (a) N-version programming (Avizienis 1985)—CRD is essentially N-version programming for LLM formalizations, and the "paradigm distance" finding parallels "design diversity" literature. (b) PAL (Gao et al. 2023)—canonical reference for the Code pathway. (c) Universal Self-Consistency (Chen et al. 2024) and DIVERSE (Li et al. 2023)—closer baselines than vanilla SC5. (d) Metamorphic testing—the stability-based localization is essentially a metamorphic relation. With ~14 references, the bibliography is thin for EMNLP.
- **W3: Error taxonomy lacks non-LLM validation and has no prescriptive value.** κ=0.33 (4-type cross-model) is below "moderate agreement." Taxonomy-guided vs. fixed repair: +0.8pp (p=0.91)—taxonomy adds zero value for repair. If the taxonomy is neither stable nor prescriptive, its contribution reduces to descriptive analysis with unvalidated categories.
- **W4: The MATH extension weakens conceptual unity.** SymPy vs. Python numerical are both imperative code—no formal verification guarantee. C2=51.5% is coin-flip. Including this under "cross-representation" without defining what constitutes sufficient representation diversity weakens the framework.
- **W5: The reframing from "CRD as a better tool" to "empirical anatomy" feels post-hoc.** The method-heavy Section 3 describes a 5-stage pipeline, reading like a methods paper whose method did not work. A genuine analysis paper would foreground research questions and hypotheses rather than pipeline description. The narrative tension between "here is our pipeline" and "the pipeline doesn't work" is noticeable.
- **W6: "Paradigm distance modulates effectiveness" is post-hoc and circular.** The effectiveness gradient (FOLIO > LogiQA > MATH) could equally reflect benchmark difficulty, formalization quality, or statistical power differences. No independent measure of paradigm distance is provided; it is inferred from CRD's own effectiveness.

### Questions for Authors
- Q1: How does CRD compare head-to-head with Roundtrip Verification on the same benchmark?
- Q2: At what k does single-representation self-consistency match CRD's detection precision?
- Q3: How much of the 5.6:1 FOL-over-Code asymmetry is driven by exec_crash? If excluded, does asymmetry attenuate substantially?
- Q4: How do you respond to the N-version programming connection? The "design diversity" literature has decades of findings on when implementation diversity works.

### Minor Issues
- 16 tables across 12 pages is dense; consider consolidating and moving supporting analyses to appendix.
- Abstract mentions "94.6% localization accuracy" without noting 53% coverage limitation—somewhat misleading.
- Several references listed as "Anonymous" need complete bibliographic information for venue submission.
- Section 5 has 8 subsections, fragmenting the narrative. Consider consolidating to 3–4 main findings.

---

## Roundtable Convergence

### Areas of Full Agreement (Both Reviewers)

1. **Score: 3/6 (Weak Reject).** The paper is below the acceptance threshold for a top ML venue main track.
2. **Statistical honesty is a genuine strength.** The transparent reporting of non-significant results, dual C5 metrics, and abandoned ProofWriter pilot is commendable and rare.
3. **Aggregate C4 non-significance is the central weakness.** The paper's core pipeline (diagnosis-guided repair) does not produce statistically significant accuracy improvement on any benchmark. The meta-analytic effect (+2.9pp, CI includes zero) confirms this is not a power issue.
4. **GT-label dependency renders stratified findings non-deployable.** The most interesting finding (repair helps on Unknown, hurts on True) requires oracle ground-truth labels unavailable in practice. Neither reviewer found evidence that CRD's own signals can predict GT category.
5. **Taxonomy lacks validation and prescriptive value.** κ=0.33 cross-model, no human annotation, taxonomy-guided repair indistinguishable from generic repair (p=0.91).
6. **Self-consistency dominates CRD.** SC5 achieves higher accuracy at equal or lower cost on all benchmarks. CRD is Pareto-dominated.
7. **MATH extension weakens conceptual coherence.** Both code-based representations lack the paradigmatic difference that makes FOLIO results interesting.
8. **Missing related work.** N-version programming, PAL, Universal Self-Consistency, metamorphic testing are all relevant and uncited.
9. **Sample sizes marginal for stratification depth.** Multiple subgroups with n < 10 appear in tables.

### Areas of Partial Disagreement

- **Novelty assessment:** R2 views the contribution as more incremental ("composition of known techniques") while R1 gives slightly more credit to the empirical findings (asymmetry reversal, GT-dependent boundaries). After discussion, both agree the empirical findings are novel but the methodological contribution is incremental—consistent with 3/6.
- **Reframing concern:** R2 flags the methods-paper-turned-analysis-paper tension more strongly. R1 acknowledges this but views the transparent negative reporting as partially redeeming. Both agree the framing is imperfect but not dishonest.

---

## Consolidated Assessment

### Overall Score: 3/6 (Weak Reject)

### Recommendation: **Reject for main track; encourage resubmission to Findings track with revisions.**

### Key Reasons for Rejection

1. **The core proposed method (CRD repair pipeline) does not work.** Aggregate repair improvement is non-significant on all three benchmarks, with CIs uniformly including zero. The meta-analytic effect is +2.9pp—too small to be practically meaningful even if it reached significance with larger samples.

2. **The most actionable finding requires oracle information.** The GT-label-dependent repair pattern is genuinely informative for understanding CRD, but it cannot be operationalized without ground-truth labels. No GT-free proxy evaluation is provided.

3. **CRD is Pareto-dominated by self-consistency.** SC5 achieves 84.8% vs. CRD's 69.1% on FOLIO at comparable cost. Even SC3 (3× cost) beats CRD (5.76× cost). This holds across all benchmarks.

4. **Incremental novelty.** The extension from binary filtering (Liang et al. 2024) to structured diagnosis uses established techniques. The paper's own evidence shows the additional diagnostic machinery adds minimal value over simple selection.

5. **Insufficient validation of the error taxonomy.** κ=0.33 cross-model agreement, no human annotation, and zero prescriptive value (p=0.91 for taxonomy-guided vs. generic repair).

### What Would Strengthen the Paper

1. **GT-free deployment evaluation:** Demonstrate that CRD's own features (stability scores, error types, asymmetry patterns) can predict when repair will help vs. hurt, enabling a practical decision policy.
2. **Human taxonomy annotation:** Validate error categories on 50+ samples with human experts to ground the taxonomy beyond LLM-to-LLM agreement.
3. **Head-to-head comparison with Roundtrip Verification:** Clarify the value of cross-representation vs. within-representation diagnosis.
4. **Scope MATH honestly:** Either provide an independent paradigm-distance metric or reframe MATH as a boundary test showing where CRD breaks down, not as evidence of generality.
5. **Expand related work:** Add N-version programming, PAL, Universal Self-Consistency, DIVERSE, and metamorphic testing connections.
6. **Tighten presentation:** 16 tables → consolidate to ~8 in main paper, move supporting analyses to appendix. Reduce Section 5 from 8 to 4 subsections.

### Positive Aspects Worth Preserving

- The asymmetry reversal across models (Qwen FOL>Code vs. DeepSeek Code>FOL) is a genuinely novel empirical finding with practical implications for representation selection.
- The GT-label-dependent repair boundary and Code-overclaiming mechanism provide real insight into why cross-representation approaches fail.
- The statistical transparency sets a positive example for the field—negative results reported with full CIs and p-values.
- The "formalization bottleneck" hypothesis (CRD requires sufficient interpretation space in NL-to-formal translation) is a useful conceptual contribution, even if not rigorously tested.

### Experiment Coverage Assessment

Comparing against the full experiment plan (11 planned experiments):
- **Covered in paper:** exp-001 (FOLIO core), exp-002 (cross-model ablation), exp-003 (ProofWriter/LogiQA), exp-004 (MATH), exp-005 (multi-round repair), exp-006 (correlated failures), exp-007 (selection vs repair), exp-008 (taxonomy ablation), exp-009 (statistical significance), exp-012 (SC5 baseline), exp-013 (taxonomy cross-validation). All 11 experiments appear represented.
- **Coverage quality:** FOLIO analysis is thorough. Cross-benchmark experiments (LogiQA, MATH) have adequate sample sizes but thin stratified subgroups. The taxonomy ablation is well-designed but yields a null result. The SC5 comparison is comprehensive and appropriately damaging to the CRD narrative.
- **Missing from plan:** No experiment tests GT-free deployment, which both reviewers identified as the most critical gap.
