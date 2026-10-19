# Related Work Supplement: Contrastive Learning for Code & Adjacent Areas

> **Purpose**: Supplementary paragraphs and citations to strengthen weak areas in Related Work v1.
> Six new papers added; RocketQA already cited in v1.
> Generated: 2026-05-15

---

## Supplement A: Contrastive Learning for Code (insert into Section 2.2, after the ContraCode/CodeRetriever paragraph)

Beyond learning invariance to syntactic variation, contrastive pre-training has been applied to inject structural and robustness priors into code representations. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pre-training that aligns code, natural language, and abstract syntax tree (AST) modalities through identifier prediction and AST edge prediction objectives, demonstrating that explicitly encoding syntactic structure during contrastive pre-training improves downstream code intelligence tasks. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing nine data augmentation operators that generate adversarial code and comment variants---including identifier renaming, dead code insertion, and operand swapping---and further trains existing code models with contrastive objectives on these augmented pairs. ContraBERT shows that contrastive pre-training with targeted perturbations substantially improves model robustness against adversarial attacks while maintaining strong performance on standard benchmarks. These methods enrich the positive pair construction space for code contrastive learning, yet they focus on augmenting the pre-training signal rather than improving the selection of negative examples during fine-tuning. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, it improves which negatives the model trains against by grounding negative selection in inter-procedural data-flow structure.

## Supplement B: Hard Negative Mining in Dense Retrieval (insert into Section 2.3, after the CL-DRD sentence)

The curriculum learning paradigm for negative sampling has been further developed by CAPSTONE \cite{he2023capstone}, which addresses the training-inference discrepancy in dual-encoder dense retrieval. CAPSTONE expands documents with pseudo-queries during training and employs a curriculum sampling strategy that progressively improves the relevance between generated and real queries, effectively controlling negative difficulty through the query generation quality. This approach achieves strong results on both in-domain and out-of-domain retrieval benchmarks, reinforcing the finding that curriculum-based difficulty scheduling benefits dense retrieval training. While CAPSTONE focuses on bridging the training-inference gap through document expansion, our structure-grounded negatives provide an orthogonal form of curriculum: negatives that are hard because they do *not* share data-flow context with the positive (¬reachable_G(x,q)), not because of embedding proximity alone.

## Supplement C: Cross-File Code Understanding and Evaluation (insert into Section 2.4, before the closing paragraph, or as a new subsection bridge)

The importance of cross-file context for code understanding has been empirically validated by dedicated benchmarks. CrossCodeEval \cite{ding2023crosscodeeval} constructs a diverse, multilingual benchmark for cross-file code completion across Python, Java, TypeScript, and C\#, using static analysis to identify completion targets that strictly require cross-file dependencies. Experiments show that even state-of-the-art code LLMs struggle without cross-file context, and that retrieval-augmented approaches yield clear improvements---yet performance remains far below the ceiling, indicating substantial room for better cross-file retrieval. ProGraML \cite{cummins2021programl} provides a language-independent, graph-based program representation that captures control-flow, data-flow, and call relations across entire programs, achieving strong results on data-flow analysis tasks. ProGraML demonstrates that whole-program structural representations are learnable and informative, providing conceptual grounding for StructFuse's use of inter-procedural data-flow graphs as a training signal. CoSQA \cite{huang2021cosqa} contributes a large-scale dataset of 20,000+ real web queries paired with Python code, bridging the gap between synthetic code search benchmarks and real-world developer information needs; it also introduces a contrastive learning method (CoCLR) for data augmentation in code search training. Together, these resources underscore that cross-file structural dependencies and realistic query distributions are critical dimensions for advancing code retrieval---precisely the dimensions that StructFuse's structure-grounded training targets.

---

## Summary of New Citations

| Paper | Venue | Year | Area | Relation to StructFuse |
|-------|-------|------|------|----------------------|
| SynCoBERT | arXiv | 2021 | Contrastive code pre-training | Syntax-guided contrastive pre-training; StructFuse uses structure for negatives, not positives |
| ContraBERT | ICSE | 2023 | Contrastive code pre-training | Robustness-oriented augmentation; complementary to StructFuse's negative mining |
| CAPSTONE | EMNLP | 2023 | Dense retrieval | Curriculum sampling for retrieval; StructFuse provides structure-based curriculum |
| CrossCodeEval | NeurIPS | 2023 | Benchmark | Validates importance of cross-file context for code tasks |
| ProGraML | ICML | 2021 | Program graphs for ML | Whole-program graph representation; conceptual grounding for StructFuse's data-flow use |
| CoSQA | ACL | 2021 | Code search dataset | Real-world query benchmark with contrastive learning augmentation |
