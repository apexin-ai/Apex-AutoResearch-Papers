# §6 Conclusion

We presented a systematic comparison of hard negative mining strategies for contrastive code retrieval, evaluating random sampling, static embedding-distance mining, and dataflow-aware mining across two decoder-only encoders with three seeds each.

Our primary finding is that simple static embedding-distance mining provides a reliable retrieval improvement over random baselines ([TBD: +X.X pp R@1, 95\% CI] averaged across encoders and seeds) at zero additional computational cost beyond the pretrained encoder already available. This establishes embedding-distance mining as a strong, zero-cost baseline for future work on negative selection strategies, and challenges the assumption that gradient-based methods are necessary for effective hard negative mining in code retrieval.

As a secondary, exploratory observation, we found that dataflow-aware negatives---selected via inter-procedural data-flow filtering and BM25 ranking---exhibit an encoder-dependent interaction pattern. Negative difficulty margin analysis suggests that encoder representation geometry, specifically the degree of embedding space saturation, may mediate strategy effectiveness. This preliminary finding, derived from two encoders, offers a candidate heuristic for strategy selection that warrants broader validation.

To enable this study, we developed a CodeQL-based extraction pipeline that computes inter-procedural data-flow connectivity across 123 repositories with 0\% analysis timeout, demonstrating the practical feasibility of structure-grounded negative mining at scale.

[TBD: 1--2 sentences on downstream SWE-bench validation, pending plan\_003 completion.]

All improvements are training-time interventions with zero inference overhead, making them directly applicable to existing contrastive retrieval pipelines. We hope this work encourages systematic investigation of the interaction between negative mining strategies and encoder properties---not only for code retrieval, but for contrastive learning broadly.
