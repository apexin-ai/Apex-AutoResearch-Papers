---
dream_id: dream_20260518T162745
tier: best
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-18T17:26:08.434425+00:00
---

# Reviewer 1 (R1): Methods Soundness and Experimental Rigor

**Paper:** OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints

---

## 1. Methodology Soundness (Score: 4/6)

### Two-Layer Architecture

The two-layer architecture (grammar + semantic) is well-motivated and cleanly designed. The separation of concerns is principled: CFGs handle structural validity (JSON well-formedness, vocabulary membership), while the stateful semantic layer handles cross-field constraints (domain/range type pairs). The authors correctly identify that domain/range enforcement is context-sensitive but prefix-decidable, which justifies their approach of sequential masking within the autoregressive framework.

The entity registry mechanism (Section 3.3.1) is a sound design choice. Building a name-to-type mapping incrementally during generation and consulting it at relation-generation time is the natural way to maintain state in a left-to-right decoder. The fixed field ordering (head, tail, relation, head_type, tail_type) ensuring that relation type is known before entity types are generated is a critical design decision that is well-explained.

### Enabling Dependency

The enabling dependency is clearly demonstrated both formally (Section 4, Eq. 1) and empirically. The semantic-only ablation on SciERC achieves only 24% DR reduction vs. 94% for the full system, directly because OOV relation types have no domain/range rules to look up. This is a genuine architectural insight, not merely a synergy claim. The asymmetry is well-characterized.

### Decidability Taxonomy

The decidability taxonomy (local / prefix-decidable / non-local) is stated in a single paragraph in Section 4 and feels underdeveloped. It is conceptually useful for understanding the design space but is not rigorously formalized. The classification of CF violations as "non-local" is correct but the paper does not explore this deeply enough. The taxonomy would benefit from formal definitions and a proof sketch that domain/range constraints are indeed prefix-decidable under the fixed field ordering assumption. As stated, it is more of a descriptive label than a rigorous contribution.

### Graceful Degradation

The grammar-first fallback mechanism is sound in principle: when semantic and grammar masks conflict (empty intersection), structural integrity is preserved by dropping semantic constraints. The priority ordering (structural > type) is well-justified since malformed JSON is catastrophically worse than a type violation.

However, the fallback has a significant side effect: it is the primary mechanism by which CF violations are introduced (Section App B). The CF-DR tradeoff ablation (Table in Appendix B) is honest and informative, showing that swapping to CF-priority fallback increases total violations (DR+CF from 10.83% to 14.82%). This confirms the current design sits near a Pareto frontier, but the paper should be clearer that the fallback is not just a safety valve but an active source of a new violation type.

### Gaps in Method Description

- The continuation masking mechanism (Section 3.3.3) for multi-token type names is described at a high level but lacks implementation detail. The claim of tokenizer-agnostic handling across byte-level BPE and SentencePiece is validated empirically (3 tokenizer families) but the compile-time prefix map construction algorithm is not specified precisely enough for reproducibility.
- The interaction between the entity registry and entities that appear in relations but NOT in the entity list is not fully specified. What happens when the model generates a relation with a head entity name not in the registry? The paper mentions fallback to "all domain-valid types" but this scenario deserves more attention.
- The S2 two-pass strategy is described briefly but the paper does not discuss its computational overhead or failure modes in detail. Given that it is presented as an alternative, this is a minor gap.

**Methodology Soundness Score: 4/6** -- The core architecture is well-designed and well-motivated. The enabling dependency is a genuine contribution. The decidability taxonomy is underdeveloped. The CF tradeoff is honestly characterized but represents a real limitation of the per-slot enforcement design.

---

## 2. Experimental Rigor (Score: 4/6)

### Baselines

The baseline set is adequate for the claims:
- **Unconstrained**: proper zero-shot baseline establishing violation rates
- **Grammar-only**: isolates structural from semantic contributions
- **Semantic-only**: demonstrates the enabling dependency
- **Post-hoc filtering**: the natural alternative approach, well-characterized including rejection rates and TP loss
- **Schema-informed prompting**: shown to be per-relation unreliable (Evaluate-for regression)

Missing baselines that would strengthen the paper:
- No comparison with EnriCo (ASP-based constraints), which is the most directly comparable decoding-time constraint method cited in Related Work. Even a qualitative comparison of constraint expressiveness would help.
- No comparison with DORE or GenIE's trie-based constraints, which enforce entity-level constraints during decoding.
- No few-shot baselines (e.g., 3-5 shot in-context learning), which is the standard comparison point for zero-shot IE papers.

### Datasets and Models

Three datasets (SciERC, DocRED, WikiEvents) spanning RE and EE with different ontology sizes (7, 96, 56 event types) is reasonable coverage. The choice to include WikiEvents demonstrates cross-task generalization without code modification, which is a strong validation.

Three 7-8B models (Qwen3-8B, Llama-3.1-8B, Mistral-7B) provide adequate cross-family validation. The 70B experiment (SciERC only fully reported, DocRED was running) addresses the scale question partially.

Concern: All primary experiments operate in the zero-shot regime where R-F1 is approximately 2-8%. This is a problematic evaluation regime because:
1. Most predicted triples are wrong (>90% are false positives), making violation rate measurements less meaningful in practice.
2. The "F1-neutral" claim is trivially easy to satisfy when F1 is near zero.
3. The practical utility of guaranteeing type-valid triples when the vast majority are semantically incorrect is questionable.

The LoRA composability experiments partially address this (R-F1 of 40-46% under fine-tuning), but these are presented as supplementary rather than primary results. The paper would be significantly stronger if fine-tuned models were the primary evaluation and zero-shot was the ablation.

### Statistical Testing

Bootstrap CI with 10,000 iterations is appropriate. The paper reports p-values honestly:
- SciERC R-F1: p=0.58 (correctly stated as not significant)
- DocRED R-F1: p<0.001 (significant, attributed to OOV elimination)
- EE metrics: entity F1 p<0.001 (trivial: 0% to 12-18%), trigger F1 borderline (p=0.015-0.05)

The dual-factor regression ($R^2=0.886$, n=4, p~0.058) is honestly reported as descriptive rather than confirmatory. With only 4 data points and df=2, no strong statistical claim can be made, and the authors correctly acknowledge this.

### Coverage of Planned Experiments

From the review context:
- P001-P019: All completed and present in the paper
- P021-P028: WikiEvents baselines and ablations all completed
- P029: 70B SciERC completed and reported
- P030: 70B DocRED was RUNNING; the paper has a commented-out placeholder in section5_runtime.tex. The review context imagines DR~11%/constrained~1.2%, but the paper does not report these numbers. This is a gap.
- P031: Case studies present (4 cases in Appendix)
- P032: EE FT composability mentioned in the review context as "Priority 2" but NOT present in the paper. The paper only reports RE FT composability.
- P033: Grammar-only cross-model for EE is present (Table 6 in the paper shows all 3 models)
- P034: Bootstrap CI for EE reported
- P035: Latency SciERC completed (13.1%), DocRED was running

The 70B DocRED results being absent is a notable gap for the "scale" narrative. The paper's title section on runtime has the 70B paragraph entirely commented out.

### Honest Reporting

The paper is commendably honest about several aspects:
- CF tradeoff is disclosed proactively with quantitative analysis
- Post-hoc filtering is acknowledged to achieve higher F1 in 5/6 zero-shot settings
- The low zero-shot F1 regime is discussed explicitly (Appendix B)
- Residual DR on DocRED (10.21%) is framed through the dual-factor lens rather than hidden
- Mistral's boundary-condition behavior is characterized separately from calibrated models

The CF tradeoff (0% to 9.9-21.1%) is the paper's most significant honest disclosure. The paper's treatment is thorough: dual-mechanism analysis, fallback ablation, concentration in Generic-type ambiguity, resolution through fine-tuning (to 1.18%) and beam search (to 0.53%). However, the fact that the method *introduces* a new violation type at rates up to 21% while claiming to enforce type validity is a tension that the paper does not fully resolve.

**Experimental Rigor Score: 4/6** -- Comprehensive experiment matrix with honest reporting and appropriate statistical testing. Weakened by the zero-shot-primary evaluation regime, missing 70B DocRED results, absence of few-shot baselines, and no comparison with the most directly comparable prior method (EnriCo).

---

## 3. Strengths

- **Clean architectural decomposition.** The grammar/semantic separation with enabling dependency is a principled design that yields clear ablation insights. The fact that semantic-only achieves only 24% DR reduction while the full system achieves 94% is a compelling demonstration that the layers are not merely additive.

- **Cross-task generalization without code modification.** Applying the same framework to both RE (SciERC, DocRED) and EE (WikiEvents) with zero architectural changes is a genuine strength. The WikiEvents results (EV/RoV elimination across 3 models) validate the framework's generality.

- **Honest and thorough treatment of the CF tradeoff.** Rather than hiding the 0% to 9.9-21.1% CF increase, the paper provides: (a) dual-mechanism analysis (registry override vs. grammar-first fallback), (b) fallback priority ablation showing the Pareto nature of the tradeoff, (c) concentration analysis (63% involving Generic type), and (d) two resolution paths (fine-tuning to 1.18%, beam search to 0.53%).

- **Practical viability demonstrated through latency analysis.** 13.1% overhead (zero-shot) and 2.3% (fine-tuned) on SciERC with one-time 44ms grammar compilation cost shows the method is deployment-ready.

- **Killer comparison against post-hoc filtering for EE.** The 99.6-100% argument discard rate for post-hoc filtering on WikiEvents is a single data point that decisively eliminates "just filter afterwards" as a viable alternative for EE.

- **Comprehensive appendix.** The paper includes prompt sensitivity analysis, document length analysis, beam search compatibility, sampling robustness, per-relation breakdowns, and fine-tuned ablations. This level of thoroughness demonstrates experimental maturity.

---

## 4. Weaknesses

- **Zero-shot evaluation regime undermines practical significance.** The primary results operate at R-F1 of 2-8%, where >90% of predictions are incorrect. Guaranteeing type validity on triples that are overwhelmingly wrong has limited practical value. The fine-tuned composability results (R-F1 40-46%) are more convincing but are relegated to a secondary role. The paper's own framing that "F1 serves as a control variable" is an acknowledgment that the extraction quality is too low to be useful, which raises the question of why anyone would deploy this system in zero-shot mode.

- **CF violations introduced by the method are substantial.** While honestly disclosed, the fact that OntoCoDec introduces 0% to 9.9% (SciERC), 12.0% (Llama DocRED), and 14.9-21.1% (WikiEvents) CF violations is a significant limitation. The method trades one class of type violations for another. The paper's argument that CF is "resolved by fine-tuning" only holds for the RE setting (verified on SciERC/DocRED); EE fine-tuning composability is not evaluated. The beam search resolution (CF to 0.53%) is compelling but only demonstrated on SciERC with greedy/beam comparison, not systematically across all settings.

- **70B results partially undermine the motivation.** On SciERC, the 70B model reduces unconstrained DR from ~13-15% (8B) to 6.5%, and OntoCoDec brings it to 0%. But the diminishing returns pattern (fewer violations to fix at scale) and the missing DocRED 70B results leave the "violations persist at scale" argument incomplete. The paper would benefit from completing the 70B DocRED experiment and discussing whether the motivation weakens as models improve.

- **No comparison with directly comparable methods.** EnriCo applies ASP-based decoding-time constraints for joint entity-relation extraction. GenIE uses trie-based entity constraints during decoding. DORE uses generate-then-select. The paper cites these but does not empirically compare with any of them. Even a qualitative comparison showing which constraint types each method can/cannot enforce would help position the contribution.

- **The decidability taxonomy is not a real contribution.** Classifying constraints as local/prefix-decidable/non-local is a single paragraph that restates well-known concepts from formal language theory. It is presented as if it were a contribution but lacks formal definitions, proofs, or novel insights. Either develop this into a proper formal framework or reduce it to a design motivation.

- **DocRED residual DR of 10.21% for Qwen is high.** While explained through the dual-factor analysis (high tightness x high baseline RV), from a practical standpoint, retaining 10% DR violations means the system does not deliver on the type-safety guarantee that motivates the paper. The paper's framing through "effective semantic coverage" is sophisticated but cannot fully mask the fact that the method is substantially less effective on the harder dataset.

---

## 5. Questions for Authors

1. **On the CF-DR Pareto frontier:** You show that the grammar-first fallback sits near the Pareto frontier. Have you explored intermediate fallback strategies (e.g., probabilistic fallback based on model confidence, or fallback only when the logit gap exceeds a threshold)? The current design is binary (all-or-nothing semantic mask), but a softer approach might find better tradeoff points.

2. **On zero-shot vs. fine-tuned evaluation:** Given that fine-tuned results (R-F1 40-46%) are far more practically relevant, why not structure the paper with fine-tuning as the primary evaluation? The zero-shot setting isolates constraint effects but at the cost of practical relevance. What is the violation rate for state-of-the-art fine-tuned IE systems (e.g., GoLLIE, KnowCoder) on SciERC/DocRED, and would OntoCoDec provide meaningful violation reduction on top of those systems?

3. **On scalability of the prefix map:** You note (Limitations) that the continuation masking approach has been tested with 6-27 entity types. For ontologies with hundreds of types (e.g., Wikidata's full entity type hierarchy, UMLS semantic types), how does the prefix map size scale? Is there a risk of the semantic mask computation becoming the bottleneck?

4. **On the WikiEvents CF rate of 15-21%:** This is substantially higher than RE (2-12%). Is this because EE has more complex argument sharing across events? Have you analyzed whether the CF violations in EE affect downstream task performance differently from RE CF violations?

5. **On the 70B DocRED gap:** The 70B DocRED experiment was running at submission time. Can you report these results? The dual-factor model predicts DR~11% unconstrained and ~1.2% constrained. If the actual results deviate significantly, how does this affect the dual-factor characterization?

---

## 6. Minor Issues

- **Title inconsistency:** The main.tex title says "Type-Constrained" but the task summary says "Type-Valid." Pick one.
- **Abstract length:** At ~220 words, the abstract is within bounds but dense. The beam search sentence (starting "With beam search ($k=4$)") adds complexity without proportional clarity. Consider cutting it to tighten the abstract.
- **Table 4 (SciERC ablation):** CF is excluded from "best per column" bolding, but no rationale is given in the caption for why. State explicitly that CF has no monotonic "better" direction.
- **Eq. 1 (output schema):** The resizebox makes the equation hard to read on screen. Consider splitting it across two lines.
- **Section numbering in main.tex:** Section 3 (Method) contains the method, but Section 5 (Experiments) includes a subsection called "Violation Landscape" that is conceptually part of the motivation/background (Section 3 violation landscape study). This organizational choice is confusing.
- **Appendix B (Extended Discussion):** This appendix is extremely long and contains material that reads like main-text analysis moved to the appendix for space. Some of this (CF dual mechanism, CF-DR tradeoff) is essential for understanding the paper's limitations and should arguably be in the main text, even at the cost of other content.
- **DocRED dev set evaluation:** The paper evaluates on DocRED's development set because test annotations are unavailable. This is standard practice but should be noted more prominently, as it means the numbers are not directly comparable to published DocRED leaderboard results.
- **Mistral CF anomaly:** In Table 5 (cross-model), Mistral SciERC unconstrained CF=56.87% is extremely high and flagged with a dagger, but the text explanation ("poor zero-shot calibration") is vague. A few sentences explaining what "poor calibration" means concretely (e.g., Mistral assigns random types to entities) would help.

---

## 7. Overall Assessment

**Score: 3.5 (Borderline Conference)**

This paper presents a well-engineered system for enforcing ontology constraints during LLM-based information extraction. The two-layer architecture is principled, the enabling dependency is a genuine insight, and the experimental coverage is thorough across models, datasets, and tasks. The honest treatment of the CF tradeoff and the comprehensive appendix demonstrate experimental maturity.

However, several factors prevent a clear accept recommendation:

(1) The primary evaluation in the zero-shot regime (R-F1 2-8%) limits practical significance. The method's value proposition is strongest when extraction quality is already reasonable, but the fine-tuned results are secondary.

(2) The method introduces substantial CF violations (up to 21% in EE) while claiming to enforce type validity, creating a tension between the promise and delivery.

(3) The lack of comparison with directly comparable methods (EnriCo, GenIE's constraints) makes it difficult to assess the incremental contribution over existing decoding-time constraint approaches.

(4) The decidability taxonomy is too shallow to serve as a standalone contribution, and the violation landscape study (Section 3 of experiments) is useful motivation but not a methodological contribution.

The paper is above average in execution quality but the contribution sits at the boundary: it is a strong engineering contribution with some analytical insights (enabling dependency, dual-factor characterization, CF-DR Pareto analysis), but it does not clearly advance the state of the art in IE performance or introduce fundamentally new algorithmic ideas. The constrained decoding machinery is largely assembled from existing components (XGrammar, logit masking, entity registry) in a competent but not surprising way.

For acceptance, I would want to see: (a) fine-tuned models as the primary evaluation, (b) at least one empirical comparison with EnriCo or a similar constraint-based baseline, and (c) either a deeper formalization of the decidability taxonomy or its removal as a claimed contribution.
