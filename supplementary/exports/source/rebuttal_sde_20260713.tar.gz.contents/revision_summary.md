## Summary of Revisions

We thank all reviewers for their constructive feedback. The main changes in the revised manuscript are:

1. **Scope clarification**: Replaced "across four datasets" with "evaluated on four datasets" throughout. Added explicit scope statement in §6 (Discussion) attributing the primary quantitative evidence to FewRel RE, with NER and ED as boundary conditions. Added "at the batch level" qualifier to abstract finding (2). Reported practical slope (~1.9 pp per 0.1 BCS) alongside the semipartial R².

2. **Task formulation distinction**: Added a sentence in §3.1 explicitly noting that our RE evaluation uses relation classification with given entity mentions (the standard FewRel/DocRED protocol), and that end-to-end extraction remains an open question.

3. **Statistical interpretation tightened**: Revised mediator interpretation in §4.3 to a hypothesis rather than an established conclusion. Explicitly enumerated borderline secondary analyses (logit-scale interaction p = 0.047, inconclusive 2×2 factorial TOST, within-pool CI crossing zero, leverage-sensitive Gemini result) and stated they are not presented as independent confirmation.

4. **Section 5 narrowed**: "Schema decomposition fails" revised to "the tested decompose-then-merge/routing strategies fail."

5. **NER U-shape hypotheses**: Added to Discussion—coarse-category disambiguation, task recognition, and reduced omission under complete schemas—explicitly labeled as hypotheses requiring future verification.

6. **Type definition sourcing**: Clarified in §3.2 and Appendix C.3 how type definitions are obtained per dataset (Few-NERD ontology descriptions, MAVEN FrameNet definitions, FewRel/DocRED Wikidata property labels).

7. **SCS/BCS clarifications**: Added explicit statement in §3.2 that SCS operates on type-name strings for pre-hoc computation. Narrowed claim: SCS is a low-cost indicator of name-based confusion risk, not a comprehensive confusion predictor. Moved the SCS-misses-co-occurrence discussion to Limitations.

8. **Figure 2 caption**: Added "FewRel RE" scope note.

9. **Table 5 mixing note**: Made the v1/v2 prompt version note more prominent.

10. **Writing clarity**: Inline definitions of BCS/SCS at first use in introduction; clearer separation of metrics and interpretation in §4.

All changes are highlighted in blue in the revised manuscript.
