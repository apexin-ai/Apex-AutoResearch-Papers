---
dream_id: dream_20260518T162745
tier: median
overall_score: 3.5/6 — Borderline Conference (Findings-appropriate)
timestamp: 2026-05-18T17:28:49.921118+00:00
---

# Dream Review Report: OntoCoDec

**Paper:** OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints
**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-18

---

## Reviewer Scores Summary

| Dimension | R1 (Methods+Experiments) | R2 (Novelty+Related Work) | Consensus |
|---|---|---|---|
| Methodology / Novelty | 4.0 | 3.5 | 3.5 |
| Experimental Rigor | 4.0 | — | 4.0 |
| Related Work Coverage | — | 4.5 | 4.5 |
| Clarity & Presentation | — | 4.0 | 4.0 |
| Significance & Impact | — | 3.5 | 3.5 |
| **Overall** | **3.5** | **3.5** | **3.5** |

**Overall Assessment: 3.5/6 — Borderline Conference (Findings-appropriate)**

---

## Consolidated Strengths

1. **Thorough and honest empirical evaluation.** The paper covers 3 models x 3 datasets x 4 configurations with bootstrap significance testing, per-relation breakdowns, and transparent reporting of negative results (CF trade-off, post-hoc filtering winning on F1 in 5/6 zero-shot settings, dual-factor fit with p=0.058). This level of intellectual honesty is rare and commendable.

2. **Clean ablation design validates the two-layer architecture.** The grammar-only ablation on EE is particularly effective: EV→0% but RoV persists at 64-77%, directly demonstrating that CFG alone cannot enforce context-dependent constraints. The latent violation surfacing pattern (AC rising from 0-0.3% to 8-14% under grammar-only) is a genuine and non-obvious finding that validates the enabling dependency.

3. **Cross-task generalization without architectural modification.** Extending from RE (domain/range) to EE (role-entity type restrictions) with zero code changes is a meaningful demonstration of framework generality. The EE results (EV/RoV elimination from 10-89% to 0%) are the paper's strongest empirical evidence.

4. **Practical composability demonstrated.** The framework composes with LoRA fine-tuning (residual violations near-zero, F1 gains modest but positive) and beam search (k=4 shows simultaneous DR+CF reduction). This addresses the practical concern of deployment beyond zero-shot settings.

5. **Violation landscape study provides useful empirical contribution.** The finding that violation rates correlate with constraint tightness rather than ontology scale is non-obvious. The cross-model analysis (Llama: low EV but highest RoV on EE) reveals orthogonal violation dimensions across constraint types.

6. **Comprehensive related work coverage.** The extended appendix survey is thorough, covering grammar-constrained decoding, code-generation type checking, vocabulary-constrained IE, training-based IE, and post-hoc validation.

---

## Consolidated Weaknesses

1. **CF trade-off fundamentally undermines the central claim (both reviewers).** The paper frames itself around "type-safety guarantees" and "formal guarantees during autoregressive generation," but constrained decoding *introduces* CF violations from 0% to 9.9% (SciERC RE) and 14.9-21.1% (WikiEvents EE) in zero-shot. The system shifts the violation distribution (eliminating DR/RV/EV, introducing CF) rather than solving type-validity. The "grammar-first fallback" that drops semantic constraints when M_grammar ∧ M_semantic = ∅ means the system does not provide formal guarantees in the strong sense implied by the framing. The paper is honest about this limitation, but the Abstract/Introduction oversell the contribution.

2. **Limited conceptual novelty (both reviewers).** The core contribution reduces to applying XGrammar for grammar constraints plus implementing a domain-specific logits processor (entity registry + lookup masking). The enabling dependency, while empirically validated, borders on obvious once the two-layer design is stated. The decidability taxonomy, the most intellectually interesting component, is presented in a single paragraph without formal definitions, proofs, or connections to automata/constraint satisfaction theory. A practitioner could implement the full system as a custom LogitsProcessor callback on top of XGrammar in moderate effort. The paper reads as a well-executed systems paper rather than a research paper with novel algorithmic insights.

3. **Primary evaluation in a low-F1 regime limits practical significance (both reviewers).** Zero-shot R-F1 of 2-8% on RE and near-zero argument F1 on EE means the vast majority of extractions are incorrect. Constraint enforcement on such noisy outputs has limited practical value. The Entity F1 recovery on EE (0%→11-17%) is primarily format compliance, not extraction quality improvement. The "F1-neutral" claim is trivially satisfiable when baseline F1 is near-zero. The fine-tuned results (R-F1 40-46% on SciERC, Arg F1 27.5% on WikiEvents) are much more compelling but receive less emphasis.

4. **70B results partially undermine motivation.** At 70B, unconstrained DR drops to 6.5% (SciERC) and 5.8% (DocRED), reducing the absolute improvement to a few percentage points. Reviewers will ask: "Is 6.5% DR worth the overhead of constrained decoding at 70B scale?" The compliance-critical framing is the correct response but needs stronger articulation. DocRED 70B results may be incomplete.

5. **Missing baselines and comparisons.** EnriCo (ASP-based type constraints during decoding) is the closest prior work and not compared against. IterGen (ICLR 2025, semantic constraints with backtracking) is in the bibliography but not cited or compared — its backtracking mechanism could potentially address the CF problem. GenIE (constrained trie decoding for IE) and InstructUIE (zero-shot IE) are also missing. Few-shot baselines are absent.

6. **Dual-factor analysis is statistically unconvincing.** The dual-factor linear fit (tightness x baseline RV predicting residual DR) has n=4 data points and p≈0.058. Presenting this as a "strong fit" or validated model is not appropriate with four observations and a non-significant p-value. It is a descriptive observation at best.

---

## Key Questions for Authors

1. **CF downstream impact.** You acknowledge CF violations "may propagate to downstream tasks." Have you measured the actual downstream impact? If an entity is assigned type A in one relation and type B in another, a KG consumer must choose. Is the DR-to-CF shift net positive for downstream applications? Without this analysis, the value proposition is incomplete.

2. **Why not global type consensus?** A post-decoding majority-vote or MAP estimate over per-entity type assignments seems implementable within the current framework without abandoning forward-only decoding. Why was this not attempted as a simple CF mitigation?

3. **IterGen comparison.** IterGen (Ugare et al., ICLR 2025) supports semantic constraints with backtracking during decoding and is in your bibliography. Have you considered whether backtracking could resolve CF? If excluded for principled reasons, state them.

4. **70B DocRED completeness.** Are the 70B DocRED results (DR 5.8→1.1%) based on completed experiments or projections? The review context suggests this was still running.

5. **Scaling to production ontologies.** DocRED (96 relations) and WikiEvents (56 event types x 80 roles) are moderate-scale ontologies. How does the continuation masking approach scale to Wikidata-scale ontologies (10K+ properties)?

6. **Post-hoc + schema-informed prompting.** Have you evaluated combining schema-informed prompting with post-hoc filtering? This compound baseline could be stronger than either alone and would better calibrate the marginal value of constrained decoding.

---

## Minor Issues

- The Abstract is dense with numbers (approximately 200 words of specific percentages). Consider moving some to the body.
- The title uses "Type-Valid" but the system does not achieve full type validity (residual DR 0.93-10.2%, CF 0-21%). "Type-Constrained" is more accurate.
- Continuation masking implementation details are insufficient for reproducibility. The prefix map construction, exact matching criteria, and handling of tokenizer-specific edge cases need more specification.
- Several EE-relevant baselines (DEGREE, Text2Event, CEDAR) are mentioned in passing but not formally cited.
- The dual-factor scatter plot with 4 points and a regression line is not visually convincing and may draw reviewer criticism.
- Bootstrap CI for Entity F1 on EE should explicitly note "format compliance recovery, not extraction quality" to avoid misleading interpretation.

---

## Missing References

- **IterGen** (Ugare et al., ICLR 2025) — in bib, not cited; directly relevant for semantic constraints with backtracking
- **InstructUIE** (Wang et al., 2023) — prominent zero-shot IE baseline
- **DEGREE** (Hsu et al., 2022) — WikiEvents EE baseline
- **Text2Event** (Lu et al., 2021) — end-to-end EE baseline
- **Rush & Collins (2012)** — dual decomposition for global constraints in NLP (relevant to CF discussion)
- **EnriCo** — ASP-based type constraints during decoding (closest prior work, needs explicit comparison)

---

## Experiment Coverage Assessment

Based on the experiment design reference:

| Experiment | Status in Paper | Assessment |
|---|---|---|
| P021-P025: EE unconstrained baselines (3 models) | Complete | Adequate |
| P027: Mistral grammar-only ablation | Complete | Strong |
| P028: Post-hoc filtering for EE | Complete | Strong |
| P029: 70B SciERC | Complete | Adequate |
| P030: 70B DocRED | Reported (may be incomplete) | Needs verification |
| P031: Error analysis (15 cases) | Complete (qualitative) | Adequate for appendix |
| P032: EE FT composability (Qwen) | Complete | Adequate |
| P033: Grammar-only cross-model (Qwen/Llama EE) | Complete (Table 6) | Good — strengthens ablation |
| P034: Bootstrap CI for EE | Complete | Methodologically sound |
| P035: Latency overhead | SciERC complete, DocRED reported | Adequate |

Overall experiment coverage is good. The main gap is the potentially incomplete 70B DocRED results and the absence of few-shot/EnriCo baselines.

---

## Recommendation

**Score: 3.5/6 — Borderline Conference / Findings-appropriate**

The paper addresses a real practical problem with a clean engineering solution, supported by thorough and honest evaluation. The violation landscape study and cross-task generalization provide useful empirical contributions. However, the conceptual novelty is thin (XGrammar + custom logits processor), the CF trade-off partially undermines the central narrative, and the primary evaluation in a low-F1 regime limits demonstrated practical impact.

**For Findings acceptance:** The paper is likely acceptable as-is, with the caveats that the "formal guarantees" framing should be softened and the decidability taxonomy should either be expanded or de-emphasized as a contribution.

**For main conference acceptance:** The paper would need (a) a deeper treatment of the decidability taxonomy with formal results, (b) resolution or meaningful mitigation of the CF problem (e.g., post-decoding consensus), (c) primary evaluation on fine-tuned models rather than zero-shot, and (d) comparison with EnriCo/IterGen.

**Predicted reviewer score range: 3.25-3.75** (consistent with Findings-level work at a top ML/NLP venue).