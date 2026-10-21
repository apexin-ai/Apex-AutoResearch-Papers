---
dream_id: dream_20260514T094226
tier: best
overall_score: Weak Reject (3)
timestamp: 2026-05-14T11:02:35.235800+00:00
---

# Reviewer R2 — Novelty, Significance, Related Work, Writing Quality

## Paper: "How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation" / "OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints"

**Note**: The "best" and "median" tier drafts differ in title and some numerical details. This review covers both, noting discrepancies where material.

---

## 1. Novelty Assessment

### 1.1 Violation Landscape Study (Contribution 1)
**Moderate novelty.** The systematic measurement of ontology constraint violations in LLM-based IE is, to my knowledge, genuinely new — no prior work has characterized the per-relation distribution of type constraint violations in LLM-generated IE outputs. The finding that constraint tightness predicts violation rate is a useful empirical insight.

However, measuring error rates of LLM outputs against a known schema is conceptually straightforward. The landscape study is descriptive rather than explanatory: the tightness-violation correlation is intuitive (tighter constraints leave less room for valid outputs, so violations are more likely) and does not reveal deeper mechanisms about *why* LLMs produce these violations (e.g., distributional prior conflicts, attention patterns, or training data biases). The "prior-constraint conflict" analysis for Evaluate-for is suggestive but underdeveloped.

The landscape study spans only 2 datasets and 1-2 models, which limits its generality as a standalone empirical contribution. A landscape study claiming to characterize "how LLMs violate ontology constraints" should ideally include more diverse ontologies, model families, and scales.

### 1.2 Grammar-Constrained Decoding for IE (Contribution 2)
**Low novelty.** Applying XGrammar to enforce JSON structure and vocabulary compliance is a straightforward engineering application of an existing tool. The paper itself acknowledges that grammar-constrained decoding is the "de facto standard for structured output" from LLMs. Compiling an IE ontology's entity types and relation names into a CFG and feeding it to XGrammar is exactly what the tool was designed for.

The result (ET→0%, RV→0%) is expected by construction — this is the definition of grammar-constrained decoding. Reporting that it works is necessary for completeness but does not constitute a research contribution. The latency overhead measurement (13-14%) has some practical value.

### 1.3 Semantic Constraint Layer (Contribution 3)
**Moderate novelty with significant caveats.** The stateful entity registry + dynamic logit masking for cross-field domain/range enforcement during autoregressive generation is the most novel component. The key idea — maintaining state across generation positions to enforce constraints beyond CFG expressiveness — is technically sound and fills a genuine gap.

However:
- The mechanism (bitwise AND of two mask vectors) is elementary.
- The concept of type-constrained decoding with stateful monitors already exists in the code generation domain (Synchromesh ICLR'22, MGD NeurIPS'23, PLDI'25). The paper's own related work section acknowledges this. The transfer from code generation to IE is the claimed novelty, but the technical delta is modest — IE ontologies have flat domain/range sets (simpler than programming language type systems), and the main new challenge (inferring entity types from free text) is handled by simply recording types from the entity list, not by a novel inference mechanism.
- Effectiveness degrades substantially on DocRED (only 46% DR reduction vs 94% on SciERC), and the paper introduces a new class of violations (CF: 9.9% on SciERC) that did not exist in the unconstrained baseline. This trade-off weakens the practical value proposition.

### 1.4 Overall Novelty Verdict
The paper's novelty is spread thin across three contributions, none of which is individually strong enough for a top venue. The landscape study is useful but shallow; the grammar layer is engineering; the semantic layer is the most novel but has limited effectiveness and introduces side effects. The "decidability taxonomy" (local / prefix-decidable / non-local) is a reasonable framing but not a deep theoretical contribution — it is a restatement of well-known properties of autoregressive generation.

---

## 2. Significance and Impact

### 2.1 Who would use these findings?
Practitioners building LLM-based IE pipelines who need ontology compliance. The grammar layer is immediately deployable. The semantic layer requires implementing the TypeConstraintProcessor per ontology.

### 2.2 Is the grammar layer finding actionable enough to justify publication?
No. "Use XGrammar to enforce JSON schema" is good engineering advice, not a research contribution. This belongs in a technical blog post or toolkit documentation, not a top-venue paper.

### 2.3 Does the violation landscape data have reuse value?
Moderate. The per-relation violation data for SciERC and DocRED could inform future work on targeted constraint enforcement. However, the landscape is model-specific (Qwen3-8B) and setting-specific (zero-shot). Different models, prompt strategies, or fine-tuning would produce different violation landscapes.

### 2.4 Is the positioning effective?
The paper tries to be both an empirical study and a method paper, but this dual positioning weakens both aspects. As an empirical study, it lacks breadth (2 datasets, 1-2 models). As a method paper, the method's effectiveness is partial (46% on DocRED) and introduces a new failure mode (CF violations). The paper would be stronger if it committed fully to one identity.

### 2.5 Practical Significance Concern
The absolute R-F1 is ~8% across all configurations. The paper correctly notes this is a zero-shot setting and F1 is a control variable. However, this means the constraint enforcement is being evaluated on a system whose extraction quality is far below practical utility. It is unclear whether constrained decoding would provide the same benefits (or introduce the same CF trade-offs) on a fine-tuned model with R-F1 in the 40-50% range where the outputs actually matter. This limits the practical significance of the findings.

---

## 3. Related Work Coverage

### 3.1 Reference Count
The "median" tier paper cites ~13 references; the extended related work section (section6_related_work.tex) cites ~25. The extended version is adequate; the short versions are insufficient. A paper making claims about being "the first" to do something must demonstrate thorough coverage of prior art.

### 3.2 Missing or Underrepresented Areas

**Structured prediction for IE (critical gap):**
- Roth & Yih (2004) is cited in the extended version but absent from the main drafts. This is the foundational work on enforcing type constraints in IE via ILP — the paper should explicitly position against it.
- Joint entity-relation extraction models (e.g., SpERT, PURE, PFN, UniRel) that implicitly enforce type constraints through shared representations are entirely absent.
- CasRel, TPLinker, and other structured prediction approaches for RE that handle type constraints architecturally.

**Other constrained decoding methods:**
- PICARD (Scholak et al., 2021) is cited in the median bib but not discussed. PICARD does incremental parsing for SQL — a highly relevant constrained decoding approach.
- Guidance (Microsoft) and Instructor — practical tools for structured LLM output that compete with the grammar layer.
- JSON mode / structured output features built into commercial APIs (OpenAI, Anthropic) that solve the grammar-layer problem out of the box.

**Schema-guided generation:**
- SGD (Schema-Guided Dialogue) and schema-guided approaches in dialogue systems.
- TANL (Paolini et al., 2021) — structured generation for IE.

**KG completion with type constraints:**
- TransE/TransR/RotatE with type constraints are not discussed. Type-constrained KG completion (Krompass et al., 2015, mentioned in the task description but absent from the paper) is a relevant precedent.

**Error analysis in IE:**
- Prior work on error analysis of IE systems (e.g., detailed error taxonomies for RE, NER error analysis) is not cited. The violation taxonomy presented is novel in the specific context of ontology constraints but should be positioned against existing error analysis frameworks.

### 3.3 Is the positioning fair?
The claim "first systematic study of ontology constraint violations in LLM-based IE" appears defensible based on my knowledge. However, the claim "first to migrate type-constrained decoding from code generation to IE" (from the extended related work) may be overly strong — EnriCo (Zaratiana et al., AAAI 2024) applies ASP constraints during decoding for joint entity-relation extraction, which is a form of semantic-constrained decoding for IE, even if it uses different formalism.

---

## 4. Writing Quality

### 4.1 Clarity of Exposition
Generally clear. The violation taxonomy (ET/RV/DR/CF) is well-defined. The enabling dependency between grammar and semantic layers is explained well. The constraint tightness definition is intuitive.

### 4.2 Organization and Flow
The paper is well-organized with a logical progression from landscape study to method to experiments. The "best" tier draft has better flow than the "median" tier, with section numbering and cross-references more consistently applied.

### 4.3 Negative Results Presentation
**A strength of this paper.** The honest presentation of:
- DocRED's attenuated results (46% vs 94%)
- CF violation trade-off (9.9% on SciERC)
- S2 offering no improvement over S1
- Evaluate-for regression under schema-informed prompting

...is commendable and reflects scientific integrity. The paper does not oversell its findings.

### 4.4 Title/Abstract Alignment
The "best" tier title ("Near-Complete Type-Valid IE via Compiled Ontology Constraints") overpromises slightly — "near-complete" applies to SciERC but not DocRED where 10.19% DR remains. The "median" tier title ("Type-Valid IE via Compiled Ontology Constraints") is more appropriate.

The landscape study title variant ("How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation") better reflects the paper's actual balance of contributions but undersells the semantic layer.

### 4.5 Specific Writing Issues
- The paper inconsistently uses "14%" and "62%" for latency overhead across drafts (the "best" tier says 37%, the "median" says 62% for full S1). These numbers need reconciliation.
- Some tables present "---" for values that should be reported (e.g., grammar-only DR on DocRED in Table 5 of the median draft).
- The "enabling ratio" metric (full DR reduction / semantic-only DR reduction) is introduced without adequate motivation for why this specific ratio is informative.

---

## 5. Weaknesses (Numbered)

**W1 (Major): Limited experimental scope undermines generality claims.** Two datasets, one primary model (Qwen3-8B), zero-shot only. The cross-model validation with Llama-3.1-8B is SciERC-only and appears incomplete in the current drafts. For a paper claiming to present a general framework, this is insufficient. Critical missing experiments: (a) a fine-tuned model where F1 is practically meaningful; (b) at least one additional ontology domain (biomedical, financial); (c) larger models (70B+) where violation patterns may differ.

**W2 (Major): The CF violation trade-off is inadequately addressed.** The semantic layer eliminates 94% of DR violations on SciERC but introduces 9.9% CF violations that did not exist before. The paper argues CF violations are "softer" than DR violations, but this is assertion rather than demonstrated. In a knowledge graph, an entity with inconsistent types across relations creates downstream inference failures. The net benefit calculation (DR reduction per CF increase) is not grounded in any downstream task evaluation.

**W3 (Major): DocRED results are weak and inconsistent across drafts.** The "best" tier claims 46% DR reduction; the paper_framing.md mentions 35.5%. The grammar-only DR on DocRED *increases* from 18.7% to 26.17%, which the paper explains as a "denominator effect" — but this explanation itself reveals that the violation measurement is confounded by the constraint intervention. The tightness-violation correlation on DocRED is weak (rho=0.37 in one draft, 0.52 in another, 0.14 in the task description). These inconsistencies across drafts suggest the results are still in flux.

**W4 (Moderate): No downstream task evaluation.** All evaluation is intrinsic (violation rates, F1 against gold labels). There is no evaluation of whether reduced violations actually improve downstream KG quality, question answering, or reasoning. The motivation section argues violations matter for "downstream knowledge graph population, reasoning engines, and regulatory compliance systems" — but this claim is never empirically validated.

**W5 (Moderate): The decidability taxonomy is underexploited.** The three-level taxonomy (local / prefix-decidable / non-local) is presented as a contribution but only Type (a) and Type (b) constraints are addressed. Type (c) — forward coreference — is acknowledged as out of scope. The taxonomy itself is a straightforward observation about autoregressive generation and does not offer deep insight.

**W6 (Moderate): Insufficient comparison with simpler baselines.** The paper compares against unconstrained generation and schema-informed prompting. Missing baselines: (a) post-hoc filtering (reject + regenerate invalid triples); (b) self-consistency voting across multiple samples; (c) few-shot prompting with constraint examples; (d) simple regex-based type checking during generation (without the full semantic layer machinery).

**W7 (Minor): The paper conflates two different papers.** The "best" and "median" tier drafts present materially different numbers, framings, and even titles. The Spearman rho for tightness-DR on DocRED varies from 0.14 to 0.52 across documents. This suggests the experimental results are not yet settled, which is concerning for review.

---

## 6. Questions for Authors (Numbered)

**Q1.** The DocRED Spearman rho for tightness-DR correlation is reported as 0.14 (p=0.18) in one place and 0.52 (p<0.001) in another. Which is correct? Is the discrepancy due to measuring unconstrained vs. constrained (full_s1) DR? If so, why does the correlation change so dramatically?

**Q2.** Have you measured whether CF violations actually harm downstream tasks? The severity distinction (DR = hard, CF = soft) is intuitive but unvalidated. In what downstream application would CF violations be acceptable?

**Q3.** What happens when this framework is applied to a fine-tuned IE model with R-F1 in the 40-50% range? Does the violation rate decrease (making constraints less necessary) or does the constraint framework still provide meaningful benefit?

**Q4.** The grammar-only DR on DocRED *increases* (18.7% → 26.17%). You explain this as a denominator effect. But could it also reflect that grammar constraints force the model into generation patterns that produce more DR violations? Have you analyzed whether the set of DR-violating triples under grammar-only overlaps with the unconstrained set?

**Q5.** Why is no post-hoc filtering baseline reported? The paper argues against post-hoc filtering in the introduction but never empirically compares against it. A reject-and-regenerate baseline would clarify whether the decoding-time approach offers genuine advantages beyond computational efficiency.

**Q6.** The CF analysis attributes 85% of SciERC CF violations to "type system ambiguity." How do you distinguish genuine ambiguity from method-induced errors? Is there human annotation to validate this claim?

**Q7.** How sensitive are the results to the output JSON format? If the entity list were generated *after* relations (or interleaved), would the semantic layer's entity registry mechanism still work?

---

## 7. Minor Issues

- M1: The latency overhead numbers are inconsistent across drafts (14% vs 23% vs 37% vs 62% for various configurations). These need to be reconciled into a single coherent set.
- M2: Table 4 in paper_tables_draft.tex has "TBD" entries for DocRED S1, suggesting the paper is not yet complete.
- M3: The bib file has cite key naming issues (e.g., `synchromesh_neurips2022` is actually ICLR 2022; `roth_yih_2004` suggests AAAI but is CoNLL at HLT-NAACL).
- M4: The `zhou2026snowballing` reference has a "PENDING AUDIT" comment in the extended related work, suggesting unverified citations.
- M5: The "Conjunction" relation in SciERC has 0% DR both before and after constraints — including it in the ablation table adds noise without information.
- M6: No confidence intervals, bootstrap estimates, or significance tests are reported for the main DR reduction numbers. The paper correctly notes F1 differences are not significant but does not apply the same rigor to violation rate differences.
- M7: The paper should report wall-clock times for the full pipeline (compilation + inference), not just per-token overhead, since compilation cost matters for deployment.

---

## 8. Score and Justification

**Score: 3 (Weak Reject)**

**Justification:**

The paper addresses a real and practical problem — LLM-based IE systems do produce ontology violations, and constrained decoding is a reasonable approach. The honest presentation of negative results (DocRED degradation, CF trade-off) is commendable.

However, the paper falls short of the acceptance bar for a top ML venue for several reasons:

1. **Novelty is insufficient.** The grammar layer is engineering; the semantic layer transfers an existing idea (type-constrained decoding) from code generation to IE with modest technical delta; the landscape study is descriptive but shallow.

2. **Experimental scope is narrow.** Two datasets, one primary model, zero-shot only. The DocRED results are weak and internally inconsistent across drafts.

3. **The CF trade-off undermines the core value proposition.** Eliminating one violation type while introducing another is a net unclear benefit without downstream evaluation.

4. **Related work coverage is thin** in the main paper drafts (7-13 references), missing important prior work on structured prediction for IE, joint extraction models, and alternative constrained decoding methods.

5. **No downstream evaluation.** The practical motivation (KG quality, reasoning, compliance) is never empirically validated.

The paper could be strengthened by: (a) committing to either a thorough empirical study (more models, datasets, settings) OR a method paper with downstream evaluation; (b) addressing CF violations with a concrete solution rather than just analysis; (c) including post-hoc filtering and few-shot baselines; (d) expanding related work significantly.

As currently positioned, the paper is a competent technical report that would be appropriate for a workshop or a systems/demo track, but does not meet the novelty and significance bar for a main conference paper at a top ML/NLP venue.
