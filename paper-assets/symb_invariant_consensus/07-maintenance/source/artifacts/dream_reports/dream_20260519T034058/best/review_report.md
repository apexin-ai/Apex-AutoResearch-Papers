---
dream_id: dream_20260519T034058
tier: best
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-19T04:40:32.277363+00:00
---

# Dream Review Report: "Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning"

**dream_id**: 20260519T034058 | **review_mode**: full | **reviewers**: R1 (Methods+Experiments), R2 (Novelty+Related Work)

---

## Consolidated Assessment

**Overall Score: 3.5 / 6 (Borderline Conference)**

Both reviewers independently scored 3.5 with confidence 4/5, converging on the assessment that this is a well-executed negative-result paper with genuine analytical contributions, but with insufficient novelty and empirical foundation for a confident accept at a top ML venue.

---

## Paper Summary

The paper evaluates Symbolic Invariant Consensus Aggregation (SICA), a pipeline that extracts FOL constraints from LLM reasoning traces and aggregates them via weighted MAX-SAT, as an augmentation of self-consistency (SC). The dominant finding is negative: SICA produces statistically significant gains (+4.9pp, p=0.013) only under narrow conditions (Mistral-7B, FOLIO, T=0.7, K=12), while all other configurations (5 model families, 6 datasets, 12+ conditions) yield zero or negative gains. The paper explains this through a Condorcet Jury Theorem lens, quantifying trace correlation via Fleiss' kappa and Effective-K, and proposes a "dual bottleneck" framework requiring both sufficient trace independence (Eff-K > 1.5) and base accuracy in a Goldilocks zone (45% < SC < 60%). An oracle control (+14.2pp with gold FOL) localizes the bottleneck to self-extraction quality. Nine remediation strategies all fail.

---

## Agreed Strengths (both reviewers)

1. **Oracle control design is methodologically exemplary.** The causal intervention replacing self-extracted constraints with gold FOL while holding aggregation fixed is clean and decisive. The large oracle gains (+14.2pp FOLIO, p = 2.0e-7) prove the aggregation mechanism is sound and isolate the bottleneck to extraction. This is the paper's strongest contribution.

2. **Comprehensive experimental coverage with honest reporting.** Seven models across four families, six benchmarks, and systematic ablations across K, T, seeds, and aggregation mechanisms. The inclusion of reasoning models (QwQ-32B, DeepSeek-R1) as negative controls is well-motivated. The transparent reporting of seed fragility (2/3 significant) and eleven explicit limitations demonstrates scientific integrity.

3. **Nine failed remediations strengthen the structural bottleneck thesis.** Covering prompting, architecture, capability, verification, diversity, and filtering dimensions makes a convincing case that the limitation is structural to same-model self-extraction, not addressable by engineering tweaks. The multi-temperature experiment is particularly informative.

4. **Effective regime characterization.** The Type A/B/C failure taxonomy is intuitive, well-supported by data, and provides actionable guidance. The Goldilocks zone concept is communicated clearly.

5. **Appropriate statistical methodology.** McNemar exact tests for paired binary outcomes, bootstrap confidence intervals, power analysis for minimum detectable effects, and discordant pair reporting. Above field standard.

6. **Practical utility of C0+SC diagnostic.** A zero-cost deployment screening tool that can predict whether SICA will help before incurring the ~2x overhead of constraint extraction. This has genuine practical value.

---

## Agreed Weaknesses (both reviewers)

1. **The Condorcet/Effective-K framework is the weakest contribution despite being foregrounded.** Both reviewers identified the same critical flaw: Effective-K is not a reliable predictor within the paper's own data. Seed s42 has the *lowest* Eff-K (1.85) yet the *highest* delta (+4.9pp), while seed s456 has *higher* Eff-K (2.22) yet negative delta. The framework discriminates across model families (Qwen vs. Mistral) but fails within the condition that matters most. The Eff-K formula is a direct application of Ladha (1992) and Fleiss (1971), not a novel derivation. The paper would be more honest framing this as quantifying a known phenomenon rather than proposing a new theoretical lens.

2. **The positive result rests on a single model-dataset pair with fragile replication.** The entire "Goldilocks zone" concept is supported by Mistral-7B on FOLIO (n=204) with 2/3 seeds significant and a mean cross-seed effect of +2.6pp. No other condition naturally falls in the Goldilocks range. LLaMA-8B shows directional support (+6.7pp D012, +2.0pp PW-600) but neither reaches significance. This is a slender empirical foundation for the paper's central positive claim.

3. **Constraint quality analysis is missing for the key condition.** The detailed extraction taxonomy (discriminative rate, variable naming inconsistency, trivially satisfied constraints) is computed only on Qwen-14B (Type A regime), where constraints are expected to fail. The paper does not report these metrics for Mistral-7B in the Goldilocks zone, where SICA actually works. This is the most critical analytical gap: we do not know whether Mistral's success comes from higher constraint quality, lower confirmation bias, or a different mechanism entirely.

4. **Variable naming canonicalization is the obvious untested fix.** The finding that 56.4% of cross-answer constraint pairs share zero Z3 variables, making logical comparison vacuous, is arguably the most mechanistically informative finding. A simple variable standardization step (mapping entity references to a canonical namespace) would be a straightforward intervention. Its absence from the nine remediation strategies weakens the "structural bottleneck" claim, since this failure mode appears to be an engineering limitation of the extraction prompt rather than a fundamental theoretical barrier.

5. **Dual bottleneck thresholds are post-hoc.** The Eff-K > 1.5 and 45% < SC < 60% boundaries appear fitted to the observed data with no held-out validation. The R-squared of 0.72 for joint prediction (mentioned in planning documents) does not appear in the paper. Formalizing the dual condition as a testable prediction with validation would strengthen the theoretical contribution.

---

## R1-Specific Concerns (Methods + Experiments)

- **Scoring function circularity:** The source-trace attribution in the MAX-SAT scoring (constraints attributed to their source trace's answer) may amplify confirmation bias. Not discussed.
- **Penalty weight alpha=0.5 fixed with no sensitivity analysis.** Given that the penalty term drives the only mechanism by which SICA can differ from SC, this deserves ablation.
- **Extraction temperature T_ext=0.3 not ablated.** Given extraction quality is the identified bottleneck, this is a notable gap.
- **Small-n probes overrepresented:** GSM8K (n=30), ARC (n=60), StrategyQA (n=60) appear in Table 1 contributing an impression of breadth the statistical power does not support.
- **Entropy-conditioned analysis is underexploited.** The finding that SICA achieves +9.6pp in high-entropy problems even for Qwen is a genuine mechanistic insight that deserves more prominence.

## R2-Specific Concerns (Novelty + Related Work)

- **Missing citation: Lefort et al. (2024)** appears in the bibliography but is not cited in the paper body. This is the closest prior work applying CJT to LLM ensembles and its omission is a significant gap.
- **FOL vs. propositional mismatch:** Constraints are acknowledged as "predominantly ground propositional clauses without quantifiers" but the paper consistently claims "FOL constraints" in the title, abstract, and introduction. This is potentially misleading.
- **SICA provenance is ambiguous.** The paper does not clarify whether SICA is novel or a formalization of ideas implicit in Logic-LM/LINC. This matters for contribution assessment.
- **Six vs. nine remediation strategies:** The abstract/conclusion claim six strategies while Section 6.5 describes nine. This inconsistency must be resolved.
- **Fundamental framing tension:** The title promises a trace-independence story, but the actual mechanistic finding is about extraction quality (variable naming, confirmation bias, propositional constraints). The theoretical framing (Condorcet) and empirical findings (extraction engineering) pull in different directions.

---

## Questions for Authors (consolidated, prioritized)

1. **Why is constraint quality analysis absent for Mistral-7B on FOLIO?** This is the only condition where SICA works. Without knowing the discriminative rate, variable naming consistency, and constraint-model agreement in this condition, the mechanistic explanation for the Goldilocks zone remains speculative.

2. **Has variable naming canonicalization been tested?** The 56.4% zero-shared-variable finding suggests this intervention could substantially change results. If tested and failed, it would strongly support the structural bottleneck claim. If untested, it is the most obvious gap in the remediation analysis.

3. **How do you reconcile the Eff-K non-monotonicity across seeds?** Seed s42 (Eff-K=1.85, delta=+4.9pp) vs. s456 (Eff-K=2.22, delta=-0.5pp) contradicts the framework's core prediction. The Unknown-proportion explanation is acknowledged but suggests Eff-K alone is insufficient, undermining its role as a central explanatory variable.

4. **What is SICA's provenance?** Is this a method you introduce, or a formalization of prior work? The answer affects contribution assessment.

5. **What is the sensitivity to penalty weight alpha and extraction temperature T_ext?** Both are fixed hyperparameters for the mechanism identified as the bottleneck.

---

## Numerical Inconsistencies Flagged

- Abstract/Conclusion cite different delta values than Table 1 for some conditions (e.g., PW-D5 delta)
- Six vs. nine remediation strategies count discrepancy between abstract and Section 6.5

---

## Recommendations for Revision

**To reach 4.0 (Borderline Accept):**
1. Add constraint quality analysis for Mistral-7B FOLIO (discriminative rate, variable naming consistency, confirmation bias metrics)
2. Test variable naming canonicalization as a tenth remediation strategy
3. Properly cite and distinguish from Lefort et al. (2024) in the paper body
4. Fix numerical inconsistencies and the six/nine remediation count
5. De-emphasize Condorcet/Eff-K in the title and framing, or provide held-out validation of the dual bottleneck thresholds
6. Clarify SICA provenance
7. Reconcile FOL vs. propositional framing

**To reach 4.5+ (Accept):**
- All of the above, plus:
- At least one additional model-dataset condition in the Goldilocks range (e.g., a weaker model on FOLIO or a harder dataset with Mistral)
- Formal dual bottleneck prediction with held-out validation
- Alpha and T_ext sensitivity analysis

---

## Final Verdict

A competent negative-result paper with a well-designed oracle control, thorough ablations, and practical diagnostic utility. The nine failed remediations convincingly demonstrate a structural bottleneck in same-model self-extraction. However, the Condorcet/Eff-K framing (which the title foregrounds) is undermined by the paper's own data, the positive result is narrow and fragile, the constraint quality analysis is missing for the key condition, and the most obvious remediation (variable naming canonicalization) was not tested. The paper's empirical contributions exceed its theoretical contributions. At current state, this is a borderline paper that would benefit from targeted revisions to align its framing with its actual findings and fill the identified analytical gaps.

**Consensus Score: 3.5 / 6 (Borderline Conference)**
**Confidence: 4 / 5**