---
dream_id: dream_20260518T162745
tier: worst
overall_score: 3.0 — Findings (Borderline)
timestamp: 2026-05-18T17:37:04.590533+00:00
---

# Dream Review Report

**Paper:** "How and When Do LLMs Violate Ontology Constraints? An Empirical Study with Decoding-Time Enforcement"
**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-18

---

## Roundtable Summary

R1 (Method + Experiments) and R2 (Novelty + Related Work) independently scored the paper at **3.5 / 6 (Borderline Conference)**. Cross-sharing in Step 2 revealed no significant disagreements. Both reviewers converged on the same core assessment: the empirical study is thorough and honestly reported, but limited methodological novelty, a serious CF trade-off, and incomplete evaluation elements prevent a confident accept. The consensus score is **3.0 (Findings)**.

The 0.5-point downward adjustment from individual scores reflects the roundtable's assessment that the weaknesses compound: the method is incremental (R2) AND introduces a trade-off that undermines its value (R1+R2) AND lacks direct baselines to demonstrate improvement over prior art (R1) AND the strongest results occur in a regime (zero-shot) where F1 is too low to be practically useful (R1+R2). Individually these are manageable; together they fall below the conference threshold.

---

## R1: Method and Experimental Rigor

### Score: 3.5 / 6 | Confidence: 4/5

### Strengths

- **Well-defined problem with first systematic quantification.** The paper identifies a real and under-studied problem (ontology constraint violations in LLM-based IE) and provides the first comprehensive measurement across tasks, models, and ontology configurations. The constraint tightness analysis is a genuine empirical insight.
- **Clean architectural decomposition.** The grammar/semantic two-layer design with enabling dependency (grammar must run first so semantic layer encounters valid type names) is elegant, well-motivated, and empirically validated through thorough ablation.
- **Honest reporting of limitations.** The CF trade-off is discussed in depth with a convincing ablation showing it is structural. Residual DR on DocRED is not hidden. The paper acknowledges that Entity F1 gains are format compliance, not semantic improvement.
- **Broad experimental coverage.** Three model families, two RE datasets, one EE dataset, zero-shot + fine-tuned regimes. Prompt sensitivity analysis, document length analysis, and bootstrap CIs are useful robustness checks.
- **Strong fine-tuning composability.** DR ≤0.20% with <0.6pp F1 cost across model-dataset configurations. This is the most practically compelling result.
- **Cross-task generalization to EE.** Demonstrating the framework on WikiEvents without architectural modification strengthens the contribution.

### Weaknesses

- **Overclaimed guarantees.** The abstract references "formal guarantees" but the grammar-first fallback means type validity is NOT guaranteed (residual DR ranges from 0.08% to 10.21% across configurations). The paper should not claim formal guarantees without precise qualification of what is and is not guaranteed.
- **CF trade-off undermines practical value in zero-shot.** CF of 9.90–21.1% in zero-shot means the method introduces a new class of violations while reducing another. On WikiEvents EE, CF (14.9–21.1%) is arguably worse than the DR it replaces. This fundamentally limits the zero-shot use case.
- **Incomplete 70B evaluation.** The paper presents 70B SciERC and 70B DocRED results in Tables 1–3, but these appear to be the only 70B data points. The claim that "violation severity is determined by constraint tightness × task complexity, not model scale alone" would be stronger with 70B EE data. No 70B fine-tuning results are included.
- **No direct baseline comparison.** No head-to-head comparison with EnriCo, GCD, GenIE, or other constrained decoding systems for IE. Post-hoc filtering is compared but is a weak baseline for the constrained decoding approach. Without direct baselines, relative improvement over prior art cannot be assessed.
- **Zero-shot F1 is very low (~4–8% R-F1).** The paper correctly frames F1 as a control variable, but at this quality level, most triples are incorrect. The practical value of ensuring (mostly wrong) triples have valid types is limited. The fine-tuned regime is more convincing but receives less experimental focus.
- **DocRED Qwen residual DR of 10.21% is high.** For the larger, more realistic ontology, constraint enforcement leaves substantial residual violations for Qwen. The Llama result (2.55%) is better, raising the question of whether effectiveness is model-dependent in hard-to-predict ways.
- **WikiEvents EE evaluation lacks depth.** No bootstrap CIs for EE results. Entity F1 from 0% is purely format compliance. Trigger F1 improvements (+1.5–1.8pp) are not statistically significant.

### Questions for Authors

1. Can you precisely state what is guaranteed vs. not, given the grammar-first fallback? "Formal guarantees" in the abstract is misleading when residual DR can reach 10%.
2. Have you considered alternative fallback strategies (e.g., selecting the grammar-valid token that minimizes semantic distance to the valid type set) instead of binary grammar-first?
3. Why was no comparison made with EnriCo, GCD, or GenIE on the same datasets?
4. The entity registry is populated from the model's own entity list. What happens with a gold or external NER source? This would isolate the semantic layer's contribution.
5. CF on WikiEvents reaches 21.1%. Since fine-tuning resolves CF on SciERC RE, why was the EE fine-tuning composability experiment not extended to demonstrate CF resolution on EE?

---

## R2: Novelty and Related Work

### Score: 3.5 / 6 | Confidence: 4/5

### Strengths

- **Exemplary experimental design.** 3 models × 3 datasets, 5-way ablation, cross-model validation, composability with fine-tuning, beam search, prompt sensitivity, latency profiling. This is unusually comprehensive and above average for the field.
- **Transparent limitation disclosure.** CF trade-off proactively disclosed with detailed analysis. Post-hoc filtering shown to achieve higher F1 in 5/6 zero-shot settings. This honesty is commendable and rare.
- **Cross-task generalization.** Same framework on WikiEvents EE without modification. Grammar-only ablation clearly demonstrates layer complementarity (grammar eliminates EV but not RoV; semantic eliminates RoV).
- **Bootstrap confidence intervals.** 10,000-iteration bootstrap CIs for all F1 comparisons with p-values. Above average statistical rigor.
- **Composability with fine-tuning is practically important.** DR drops to 0.01–0.20% with LoRA + S1 and R-F1 within ±0.6pp. This is the strongest argument for practical deployment.

### Weaknesses

- **Limited methodological novelty.** OntoCoDec is a composition of XGrammar (existing) + lookup-table logit masking (straightforward). The entity registry is a dictionary. Continuation masking is a prefix tree. None are individually novel. The enabling dependency (grammar before semantic) is a natural design decision, not a deep insight. The "type checking for neural generation" framing has been explored in code generation (the paper's own cited DOMINO reference).
- **Prefix-decidability taxonomy is not deeply novel.** The three-way classification (local / prefix-decidable / non-local) is standard in compiler theory and incremental parsing (cf. attribute grammars). PICARD (Scholak et al., 2021) implements essentially the same insight for SQL. The taxonomy is a useful organizational device but does not constitute a standalone intellectual contribution. It would need formal decidability results or complexity analysis to be more than a classification convenience.
- **"Constraint tightness determines violation severity" is somewhat expected.** Tighter constraints are harder to satisfy, so violations are more frequent. The dual-factor pattern (tightness × baseline RV) is more interesting but characterized on only 4 data points with p=0.058, which the authors correctly note is descriptive.
- **CF trade-off undermines the value proposition.** The method claims "type-safety" but introduces 2.57–21.1% CF violations in zero-shot. CF means the same entity gets different types across triples, which is equally problematic for KG construction. The paper asserts DR is "harder" than CF without downstream validation.
- **Zero-shot F1 too low to demonstrate practical value.** At 4–8% R-F1, the constrained outputs are not useful for any downstream application. The fine-tuned results are convincing but are a smaller fraction of the experimental narrative.
- **Related work gaps.** Pre-neural constrained inference for IE (ILP-based joint inference, Li & Roth 2002, Punyakanok et al. 2004/2008) is underrepresented. The paper positions constraint enforcement as novel for IE, but it was standard in pre-neural NLP. Knowledge graph completion with type constraints (TKRL, TypeComplex, TypeDistMult) is conceptually related but not discussed. Neuro-symbolic IE (DeepProbLog, NeurASP) is not engaged with.
- **Entity F1 improvement from 0% is misleading if not immediately qualified.** The abstract highlights this without immediate context that it is format compliance, not extraction quality.

### Questions for Authors

1. Have you evaluated whether CF violations actually cause problems downstream (KG construction, QA)? The DR-harder-than-CF claim needs empirical support.
2. The grammar-first fallback triggers ~57 times per document on DocRED for 8B models. What fraction of type tokens are actually semantically constrained vs. falling back to grammar-only?
3. Why not a two-pass approach for global type consensus (pass 1: entity extraction with type voting; pass 2: relation extraction with fixed types)? How would this compare to the current approach?
4. How does OntoCoDec compare with EnriCo in constraint expressiveness and enforcement effectiveness?
5. The dual-factor pattern (tightness × RV baseline) is characterized on 4 data points. Do you plan to validate on additional ontologies?

---

## Roundtable Convergence

### Points of Agreement (R1 + R2)

1. **The empirical study is the primary contribution and is well-executed.** Both reviewers recognize the breadth and honesty of the experimental evaluation as above average for the field.
2. **Methodological novelty is limited.** The system is a composition of known techniques (CFG masking + lookup-table logit masking). The prefix-decidability taxonomy, while useful, formalizes known distinctions from compiler theory.
3. **CF trade-off is a serious limitation.** CF of up to 21.1% in zero-shot undermines the "type safety" framing. The method trades one violation class for another without demonstrated net benefit on downstream tasks.
4. **Zero-shot F1 is too low for practical relevance.** At 4–8% R-F1, the practical value of constraint enforcement is questionable. The fine-tuned regime is more convincing but less emphasized.
5. **Missing direct baselines.** No comparison with EnriCo, GCD, GenIE, or other constrained decoding systems for IE. This is a significant gap.
6. **70B evaluation is present but limited.** 70B results appear only for RE (SciERC and DocRED). No 70B EE, no 70B fine-tuning.
7. **Fine-tuning composability is the strongest practical result.** Both reviewers view this as the most compelling evidence for the method's utility.
8. **Honest reporting is commendable.** The paper's transparency about limitations, CF trade-offs, and format-compliance-vs-semantic-improvement distinctions is praised by both reviewers.

### Points of Minor Disagreement

- R1 places more weight on the incomplete 70B evaluation and the overclaimed "formal guarantees." R2 places more weight on the limited methodological novelty and the taxonomy's lack of depth. These are complementary concerns, not contradictions.

### Consensus Assessment

The paper sits at the boundary between a solid Findings contribution and a main conference paper. The empirical thoroughness and honest reporting push it toward acceptance; the limited novelty, CF trade-off, low zero-shot F1, and missing baselines pull it back. The consensus is that the paper does not meet the bar for the main conference but has sufficient merit for Findings-level acceptance if the authors address the overclaiming (formal guarantees) and provide at least one direct baseline comparison.

---

## Experiment Coverage Assessment

Comparing against the full experiment plan:

| Experiment | Status in Paper | Assessment |
|---|---|---|
| P029: 70B SciERC | Present (Table 1) | Complete |
| P030: 70B DocRED | Present (Tables 2–3) | Complete |
| P031: Error analysis (15 cases) | Present (Section 4.6) | Adequate but small sample |
| P032: EE FT composability | Present (Table 5) | Complete |
| P033: Grammar-only cross-model EE | Present (Table 4) | Complete |
| P034: Bootstrap CI | Present (Table 6) | Complete |
| P035: Latency overhead | Partially present (Table 7) | WikiEvents estimated, not measured |

Coverage is high (~90%). The main gap is WikiEvents latency being estimated rather than measured, and the absence of 70B EE experiments.

---

## Consolidated Score

| | R1 | R2 | Consensus |
|---|---|---|---|
| Score | 3.5 | 3.5 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

**Overall: 3.0 / 6 — Findings**

### Justification

The paper presents a thorough empirical study of ontology constraint violations in LLM-based IE with an engineering system (OntoCoDec) that is practical and composable. The experimental design is exemplary in breadth and the reporting is commendably honest. However:

1. **Novelty is incremental.** The method composes existing techniques (CFG masking + lookup tables) without algorithmic innovation. The prefix-decidability taxonomy formalizes known compiler-theory distinctions.
2. **The CF trade-off (up to 21.1%) partially negates the contribution.** The method solves one violation class while introducing another, with no downstream evaluation to demonstrate net benefit.
3. **The strongest regime (zero-shot) produces unusably low F1 (4–8%).** The fine-tuned regime where results are compelling receives less focus.
4. **No direct baselines.** Without comparison to EnriCo, GCD, or GenIE, the relative contribution cannot be assessed.
5. **Overclaiming.** "Formal guarantees" language is not supported by the grammar-first fallback mechanism that permits residual violations up to 10%.

The work would benefit from: (a) removing the "formal guarantee" claim or precisely qualifying it, (b) adding at least one direct baseline comparison, (c) a small downstream evaluation demonstrating DR reduction matters more than CF introduction, and (d) rebalancing the narrative toward the fine-tuned regime where results are most compelling.

---

## Key Revision Recommendations

1. **Remove or qualify "formal guarantee" claims.** State precisely: grammar layer guarantees vocabulary membership and JSON validity; semantic layer provides best-effort domain/range enforcement with graceful degradation.
2. **Add direct baseline comparison.** Even on a single dataset, compare with EnriCo or another constrained decoding system for IE.
3. **Downstream evaluation for CF vs DR.** A small experiment showing the impact of DR violations vs CF violations on KG quality or downstream QA would substantially strengthen the paper.
4. **Rebalance toward fine-tuned regime.** The FT composability results are the most practically compelling. Consider making this the primary evaluation, with zero-shot as a stress test.
5. **Deepen the taxonomy.** Add formal decidability results or complexity analysis to make the prefix-decidability taxonomy a standalone contribution rather than a classification convenience.
6. **Fill related work gaps.** Discuss pre-neural constrained inference (ILP-based joint inference), KGC type constraints, and neuro-symbolic IE to properly situate the contribution historically.