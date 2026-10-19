We thank Reviewer YZ47 for the constructive review. We address each concern below.

**W1: Strongest evidence concentrated in FewRel RE.**

We agree that FewRel provides the clearest identification result (VIF = 1.18). We would like to clarify that our abstract already states that the paper focuses on relation extraction (RE) as the primary testbed, with named entity recognition (NER) and event detection (ED) serving as boundary conditions. The title poses a research question rather than making a universal claim, and the answer is task-dependent. In the revision, we add an explicit scope statement at the beginning of Section 6 (Discussion): "The primary quantitative evidence for confusability as an independent predictor comes from FewRel, while NER and ED serve as boundary conditions that characterize where the effect does and does not manifest."

**W2: RE task is relation classification with marked entities, not full end-to-end IE.**

We agree this distinction is important. Section 3.1 already states "Each instance provides a sentence with marked head and tail entities; the task is to classify the relation," but we did not foreground this distinction at the framing level. In the revision, we add to §3.1: "This formulation—relation classification with given entity mentions—is the standard evaluation protocol in FewRel and DocRED. Our findings characterize label-selection behavior under schema complexity; whether the same patterns hold under end-to-end entity-and-relation extraction (where entity detection errors may dominate) remains an open question."

We note that this setting is common in the IE literature (FewRel, DocRED, TACRED all provide marked entities) and that confusability-driven type substitution is specifically a label-selection phenomenon—the entity spans are given, so the model's errors are purely in type discrimination, which is precisely what BCS measures.

**W3: BCS may absorb broader effects (domain, label properties).**

Three controls help address this concern:
1. Adding domain entropy as a covariate leaves the BCS coefficient unchanged, while domain entropy is not significant (p = 0.97; §4.3).
2. BCS and degree centrality exhibit low collinearity on FewRel (VIF = 1.18; Table 8, Appendix E.3).
3. FewRel's balanced design, with 700 instances per type, controls for frequency differences.

Additionally, the within-pool analysis (§4.3) constructs low-BCS and high-BCS batches from the same 16-relation subsets, reducing the influence of relation composition. The permutation test finds no significant evidence that the BCS slope differs across pools (p ≈ 0.60).

We acknowledge that these controls cannot rule out all domain-specific or label-specific effects. A hierarchical model with relation-type random effects would provide stronger evidence and remains an important direction for future work. We therefore interpret BCS as an independent predictor conditional on the measured controls.

**W4: NER v1/v2 prompt distinction.**

We clarify: all main-text results (count curves in §4.1, BCS-null in §4.3–4.4) use the v1 prompt unless explicitly noted. The v2 prompt appears only in (a) cross-model Table 5 for fair comparison (noted in the table caption), and (b) format-independence analysis (Appendix). The NER U-shaped count curve and BCS-null are v1 results. In the revision, we add a clarifying sentence to §4.1: "The NER count curve and all BCS analyses use the v1 prompt; v2 appears only in cross-model comparisons (Table 5, noted in caption)."

**Suggestions adopted:**
- §5: revised to "the tested decompose-then-merge/routing strategies fail" rather than implying all possible decomposition approaches fail
- §3.1: added explicit relation-classification distinction
- §4.3: added domain-entropy interpretation sentence
