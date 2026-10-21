---
dream_id: dream_20260514T205155
tier: best
overall_score: borderline accept / findings
timestamp: 2026-05-14T21:38:43.771935+00:00
---

## Summary of the Paper

This paper identifies that LLM-based zero-shot information extraction produces systematic ontology constraint violations (15-19% of triples violate domain/range rules on SciERC and DocRED), conducts a per-relation violation landscape study showing that violation rates correlate with constraint tightness rather than ontology size, and proposes OntoCoDec -- a two-layer constrained decoding framework that compiles IE ontology schemas into a grammar layer (XGrammar CFG for structural/vocabulary validity) and a semantic layer (stateful entity registry + dynamic logit masking for domain/range enforcement). On SciERC the system achieves 94% DR reduction at zero F1 cost; on DocRED, 45-90% DR reduction depending on the model, with cross-model validation on Qwen3-8B and Llama-3.1-8B.

## Summary of Strengths

- S1: **The violation landscape study is a genuine empirical contribution.** No prior work has systematically measured per-relation ontology constraint violation distributions in LLM-based IE. The finding that comparable DR rates emerge across ontologies differing 14x in size (SciERC 15.4% vs DocRED 18.5%), with the key predictor being constraint tightness rather than ontology scale, is non-obvious and practically useful. The Evaluate-for regression (+5.8pp under schema-informed prompting) provides concrete evidence that prompt-level intervention is not merely insufficient but can be counterproductive.

- S2: **Thorough and honestly reported experimental design.** The 4/5-way ablation cleanly isolates each layer's contribution, with cross-model (2x2 matrix), post-hoc filtering baseline, bootstrap CIs (10,000 iterations), and per-relation breakdowns. Negative results are transparently disclosed: CF elevation to 9.90%, grammar-only DR *increase* on DocRED, S2 null result, post-hoc filtering achieving higher F1. This level of honesty strengthens the paper's credibility.

- S3: **The related work section is substantially more thorough than the original brief submission context suggested.** Six organized paradigms with ~42 references. The PICARD/Synchromesh/PLDI'25 differentiation is technically precise, and the paper correctly identifies the key IE-specific challenge (entity registry populated during generation from free text, vs. fixed schema in SQL/code). The concurrent work coverage (OntoLogX, Zhou et al. 2026 ontology-to-tools) is commendable.

- S4: **The dual-factor model (tightness x model RV baseline) for DR reduction is analytically stronger than a naive single-factor story.** Qwen's 29.66% RV baseline causing grammar enforcement to surface latent DR violations, yielding only 45% DR reduction on the same ontology where Llama (RV 16.03%) achieves 90.2%, is a genuine insight about model-constraint interaction.

- S5: **Post-hoc filtering comparison is well-framed.** Rather than competing on F1 (where post-hoc wins by removing FPs in a low-F1 regime), the paper correctly argues along multiple dimensions: recall preservation, TP retention (127 lost on DocRED), entity-type violation persistence (post-hoc ET=2.47% vs OntoCoDec ET=0%), and streaming compatibility.

## Summary of Weaknesses

- W1: [Major] **Core technical contribution has limited novelty.** The paper's central technical mechanism -- compiling ontological type constraints into token-level logit masks applied during autoregressive decoding -- is a domain transfer of techniques well-established in the code generation literature to a *structurally simpler* constraint system. PICARD (EMNLP 2021) maintains incremental parsing state for SQL type checking. Synchromesh (ICLR 2022) enforces type and scope constraints via dynamic token masks. The PLDI 2025 work compiles full type systems (with subtyping and parametric polymorphism) into prefix automata for logit masking. IE ontology constraints -- flat domain/range sets over 6 entity types -- are dramatically simpler than these systems. The entity registry is a dictionary lookup; the composition mechanism is standard bitwise AND. The paper acknowledges the code-gen parallel but does not convincingly articulate what IE-specific technical challenge required a solution *beyond* what these systems already provide. The free-text entity span argument (entities discovered during generation, not declared upfront) is valid but the actual implementation (building a dict as entities are parsed) is straightforward.

- W2: [Major] **The decidability taxonomy is not a meaningful contribution.** The local / prefix-decidable / non-local classification follows directly from basic properties of left-to-right autoregressive generation. That entity-type membership is locally decidable, domain/range constraints are prefix-decidable once the registry is built, and forward coreference is non-local -- these are obvious consequences of the generation order. Similar (and more rigorous) taxonomies appear implicitly in Synchromesh, MGD, and the PLDI 2025 work. Presenting this as a contribution (it appears in the abstract and is repeated in multiple sections) inflates the paper's novelty claims. It would be better positioned as design rationale or organizational framework.

- W3: [Major] **DocRED results are weak and strain the "near-complete" framing.** For Qwen3-8B on DocRED, DR drops only from 18.46% to 10.21% -- a 45% reduction, leaving more than 1 in 10 triples with domain/range violations. One of four cells in the 2x2 evaluation matrix retains >10% violation rate. The title "Near-Complete Type-Valid Information Extraction" is defensible for SciERC (0.93%) and Llama-DocRED (2.55%) but misleading for Qwen-DocRED. The paper should either qualify "near-complete" more carefully or acknowledge that the system's effectiveness is highly dependent on the interaction between model RV baseline and ontology tightness.

- W4: [Moderate] **CF trade-off is substantial and the severity distinction is asserted, not validated.** CF rises from 0.08% to 9.90% on SciERC (Qwen) and to 12.02% on DocRED (Llama). The paper frames DR as "hard" and CF as "soft" violations, arguing that individual triples remain type-valid under CF. This distinction is plausible but entirely unvalidated: no downstream evaluation shows that CF violations are indeed less harmful. The dominant conflict pattern (Generic <-> OtherScientificTerm) is attributed to type system ambiguity, which risks dismissing a method limitation as a dataset artifact. Ablation evidence cleanly attributes CF to the semantic layer (grammar-only CF=0.08%), which is informative but does not reduce the practical impact.

- W5: [Moderate] **Evaluation scope is narrow for the generality of claims.** Two 8B-class models, two datasets, zero-shot only, R-F1 of 2-8%. No fine-tuned model, no larger model, no domain beyond scientific/Wikipedia text. The claim "model-agnostic generalization" in the introduction and cross-model section overreaches from a 2-model sample. More critically, the practical motivation for constraint enforcement is arguably strongest in the fine-tuned regime where F1 is meaningful and residual violations matter for downstream applications -- yet this regime is entirely unexamined.

- W6: [Minor] **"First systematic study" claim should be scoped.** The paper claims "the first systematic study of ontological constraint violations in LLM-based IE." This should be qualified to zero-shot LLM-based IE. Knowledge graph embedding literature (e.g., TransE, RotatE) has long examined type constraint violations in learned representations, and supervised IE systems like SpERT implicitly enforce type consistency through architecture. The claim as stated may be technically correct but is stronger than warranted without acknowledging these adjacent literatures.

- W7: [Minor] **The "enabling dependency" is architecturally self-evident.** The finding that semantic constraints need grammar to validate relation names before domain/range lookup can work is a direct consequence of the system design (the semantic layer looks up rules by relation name). The 24% vs 94% gap is empirically informative, but framing this as a key finding rather than a design requirement inflates its significance.

- W8: [Minor] **Tightness-violation correlation on SciERC (7 data points) is statistically weak.** Even if r=0.87 (mentioned in project context), 7 points are too few for robust correlation analysis and could be confounded by relation frequency. DocRED with 96 relations would provide much stronger evidence, but per-relation DR under constrained decoding is not reported for DocRED at the same granularity.

## Questions for Authors

- Q1: What specific IE technical challenge does OntoCoDec solve that the PLDI'25 type-constrained code generation system (or a straightforward adaptation of it) cannot? Beyond the entity registry being populated during generation -- which is a dict lookup -- what is the algorithmic innovation?

- Q2: The fallback rate on DocRED (10.2%, 1770/17341 triples) and residual DR (10.21%) are nearly identical. Is this a mathematical tautology (every fallback = one DR violation by definition) or an empirical finding? If the former, the "tightness predicts DR" chain is partially circular -- tightness causes fallback, fallback *is* residual DR, therefore tightness "predicts" DR.

- Q3: Have you measured or estimated violation rates in a fine-tuned IE system? If fine-tuned models on SciERC already achieve <2% DR, the practical motivation for decoding-time enforcement narrows substantially. Conversely, if fine-tuned models retain non-trivial DR, that would greatly strengthen the paper.

- Q4: The semantic-only configuration on DocRED *increases* ET violations (2.48% -> 4.22%). This negative interaction effect -- partial constraint application worsening a different violation category -- seems concerning and underexplored. What is the mechanism, and does it carry implications for deploying individual constraint layers?

- Q5: How does the system handle entities that appear in relations but were not present in the entity list? The registry lookup would fail. What fraction of triples contain entities absent from the entity list, and how does this affect DR enforcement?

## Missing References

The related work is substantially more complete than initially apparent (~42 references across 6 paradigms). However, several notable gaps remain:

1. **SynCode (Ugare et al., 2024)** -- Grammar-constrained decoding with semantic validation for Python/Go, directly relevant to the grammar+semantic layering.
2. **TANL (Paolini et al., ICLR 2021)** -- Translation-based IE that frames extraction as augmented natural language generation; relevant as a training-based structured generation baseline.
3. **REBEL (Cabot & Navigli, EMNLP 2021)** -- Autoregressive relation extraction with constrained beam search over relation triples.
4. **Neuro-symbolic constraint literature** -- DeepProbLog (Manhaeve et al., NeurIPS 2018), Semantic Loss (Xu et al., ICML 2018), posterior regularization (Ganchev et al., JMLR 2010). OntoCoDec's approach of compiling declarative constraints into procedural enforcement is a specific instance of this broader research direction. This connection is entirely absent.
5. **KG embedding type constraints** -- TransR (Lin et al., AAAI 2015), type-constrained negative sampling (Krompass et al., 2015). These enforce type constraints in representation learning and motivate why type validity matters for KG applications.
6. **Schema-guided dialogue** -- SGD (Rastogi et al., AAAI 2020) and related work on schema-following constrained generation in task-oriented dialogue, which shares the "compile schema into generation constraints" paradigm.
7. **InstructUIE (Wang et al., 2023)** -- Mentioned in the summary context but not cited in the actual paper; zero-shot IE with instruction tuning.

## Detailed Comments

**Novelty positioning is the paper's greatest vulnerability.** The related work section correctly identifies the code-generation constrained decoding lineage (PICARD, Synchromesh, MGD, PLDI'25) and articulates the key difference (free-text entity discovery vs. fixed schemas). However, the paper does not sufficiently grapple with the implication that IE ontology constraints are *dramatically simpler* than the constraint systems these prior works already handle. Programming-language type systems feature subtyping hierarchies, generic types, parametric polymorphism, and scope rules; IE ontologies have flat domain/range sets over 6 entity types. The entity registry -- the main IE-specific innovation -- is a dictionary populated during generation. Reviewers familiar with the code-gen literature will perceive this as competent engineering rather than algorithmic innovation. The paper should either (a) argue convincingly why the IE domain introduces challenges absent in code generation that require novel solutions, or (b) reframe the contribution as primarily empirical (the violation landscape study) with the system as enabling infrastructure.

**The violation landscape study (Section 3) is the paper's strongest and most original contribution.** I would recommend elevating it: dedicate more space to per-relation analysis on both datasets, report the tightness-violation correlation with proper statistical tests on DocRED (96 relations provide much stronger evidence than SciERC's 7), and consider it as the primary contribution rather than sharing emphasis equally with the framework. The finding that constraint tightness, not ontology size, predicts violations is genuinely useful for the IE community.

**Low F1 complicates interpretation.** At 8% R-F1, approximately 92% of extracted triples are incorrect. Enforcing type constraints on this distribution means the system is primarily constraining the types of *incorrect* triples. While the paper correctly frames F1 as a control variable and the zero-shot setting as isolating the constraint effect, the practical question remains: does constraining a mostly-wrong distribution teach us something transferable to the regime where IE systems are actually deployed? The dual-factor model (tightness x RV baseline) is dataset/model-specific and may not hold when the base model is substantially more accurate.

**Title and abstract overstate the DocRED results.** The abstract states "18.46% -> 10.21%" for Qwen-DocRED, which is correct, but the title "Near-Complete Type-Valid" and the emphasis on 94% reduction (SciERC) creates an impression that does not survive contact with the DocRED numbers. I recommend the abstract lead with the range (45-94% on SciERC, 45-90% on DocRED) and the title be revised to something like "Substantial" or "High-Coverage" rather than "Near-Complete."

**The paper is well-written and honestly reported.** Despite the novelty concerns, the experimental rigor, transparent disclosure of limitations (CF trade-off, S2 null result, grammar DR increase on DocRED, post-hoc F1 advantage), and careful claim calibration are commendable. This is a paper that does not oversell its contributions, which is appreciated.

## Scores
- Soundness: 3.5/5
- Excitement: 2.5/5
- Overall: 3/5
- Confidence: 4/5

**Rationale for scores:**

*Soundness (3.5):* Experimental methodology is strong -- clean ablation design, cross-model validation, bootstrap CIs for F1, honest negative result reporting. Deductions: violation rate metrics lack uncertainty quantification (the headline 94% has no CI); the tightness-DR correlation rests on 7 SciERC points; the fallback-rate/residual-DR near-identity may be tautological; CF severity distinction is asserted without validation.

*Excitement (2.5):* The violation landscape study is genuinely novel and the dual-factor model is insightful. However, the core technical framework is domain transfer of established code-generation constrained decoding techniques to a simpler constraint domain. The decidability taxonomy restates known properties. The entity registry is a dictionary lookup. The composition is standard bitwise AND. The IE community would benefit from the empirical findings; the systems contribution is competent but incremental.

*Overall (3.0):* The paper fills a real gap -- no prior work compiles IE ontology constraints into decoding-time masks -- and does so with commendable experimental thoroughness and honesty. The violation landscape study alone is a publishable contribution. The framework works as described. However, limited technical novelty beyond domain transfer, narrow evaluation scope (2x2, zero-shot, ~8% F1), substantial CF trade-off without downstream validation, and one matrix cell retaining >10% DR place this at borderline. Suitable for Findings; borderline for main conference. Strengthening the novelty argument and adding a fine-tuned baseline would significantly improve the paper's positioning.