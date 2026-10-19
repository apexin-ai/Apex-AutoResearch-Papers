We thank Reviewer K2pz for the thorough review and constructive suggestions. We address the concerns below, grouping related issues.

**W1 and W8: Scope and generalization.**

Our intention was not to present the four datasets as independent confirmations of the same effect. Rather, we evaluate four datasets spanning RE, NER, and ED to examine where the effect does and does not emerge. FewRel provides the cleanest batch-level identification, DocRED provides directional evidence under collinearity, and MAVEN and Few-NERD help characterize boundary conditions.

We will replace phrases such as "across four datasets" with "evaluated on four datasets" and explicitly attribute the 27% result to FewRel. We also acknowledge that all four datasets are English and primarily Wikipedia/Wikidata-derived. Cross-model validation provides complementary evidence but does not eliminate this limitation. We will therefore temper our claims regarding domain, linguistic, and training-regime generalization.

**W2 and W3: Interpretation and scope of SCS/BCS.**

We will clarify that, on FewRel, BCS accounts for 27% of cross-batch accuracy variance, not individual type-pair confusion, and report the practical slope of a 1.9 percentage-point accuracy decrease per 0.1 increase in BCS. The pairwise and batch-level R² measure different outcomes and are not directly comparable.

We also acknowledge that SCS captures type-name semantic overlap but not co-occurrence or context-dependent ambiguity, as illustrated by the instance_of/taxon_rank pair. We therefore narrow our claim: SCS is a low-cost, pre-hoc indicator of name-based confusion risk, not a comprehensive confusion predictor. We will state this limitation in both the main text and Limitations, and clarify that Appendix N provides only a possible aggregation mechanism.

**W4 and W5: Alternative explanations and robustness.**

We agree that our existing controls reduce but do not eliminate the possibility of domain confounding. Adding domain entropy leaves the BCS coefficient unchanged, and BCS has low collinearity with centrality on FewRel. However, these analyses cannot rule out all domain- or label-specific effects. We will therefore present the mediator interpretation as a hypothesis rather than an established conclusion and identify within-domain analysis as an important direction for future work.

We also acknowledge that several secondary analyses are borderline or inconclusive, including the logit-scale interaction, the 2×2 factorial TOST, one within-pool confidence interval, and the leverage-sensitive Gemini result. We will state these limitations explicitly and no longer present these analyses as independent confirmation. The core conclusions rely on the full-range FewRel analysis and the primary pre-specified TOST.

**W6: Practical implications.**

We agree that the paper is diagnostic and does not introduce a new extraction algorithm. We will make its practical guidance explicit: prioritize candidate-count reduction for NER, use SCS/BCS to identify RE schemas vulnerable to name-based confusion, and avoid the tested decomposition strategies when routing overlap or merge-induced false positives are high. The oracle-routing gap further identifies routing and merging as the main targets for future decomposition methods.

**W7: Single-seed greedy decoding.**

Temperature-0 greedy decoding is deterministic for a fixed input, so the relevant randomness comes from batch construction rather than decoding. Our 25 independently sampled batches per condition and bootstrap confidence intervals quantify this variation. We will clarify this distinction and, where feasible, report an additional batch-sampling seed check for the main FewRel regression.

**Suggestions adopted in revision:**
- Figure 2 caption: added "FewRel RE" scope note
- Table 5 v1/v2 mixing: made the note more prominent
- Practical slope reported near the 27% finding in §4.3
