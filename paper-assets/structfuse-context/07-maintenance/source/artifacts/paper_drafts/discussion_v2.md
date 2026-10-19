# 5. Discussion

## 5.1 Relationship to Inference-Time Graph Methods

A growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.
CodexGraph (Liu et al., NAACL 2025) materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides line-level code graph navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) and ARISE (Seddik & Fard, 2026) come closest to our work in incorporating data-flow information, but both are limited to intra-procedural scope.

Table 5 summarizes the key dimensions of comparison. We highlight two axes along which StructFuse occupies a distinct position:

**When structural information enters the pipeline.** Inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity and—for agent-based systems—requiring multiple LLM calls per query. StructFuse amortizes all graph computation to training time: CodeQL extraction costs approximately 8.9 seconds per instance (~110 CPU-hours for 44K instances; Table 4), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead. For latency-sensitive, high-throughput retrieval scenarios, this cost model is substantially more favorable.

**Depth of data-flow analysis.** Most inference-time graph methods use structural relations (call graphs, class hierarchies, import dependencies). GraphCoder incorporates control-flow and data-dependence graphs, and ARISE exposes statement-level def-use edges, but both operate within single procedures. StructFuse leverages CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths—e.g., a sanitizer that transforms data between a source and sink across call boundaries. This deeper semantic signal generates harder, more informative negatives than structural proximity alone.

**Complementarity.** We emphasize that StructFuse and inference-time graph methods address different stages of the retrieval pipeline and are composable rather than competing. A StructFuse-trained encoder can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. Conversely, systems like CodexGraph or LocAgent can refine StructFuse retrieval results through explicit graph navigation when maximum precision is required. The two paradigms are complementary: StructFuse internalizes general structural patterns during training, while inference-time methods provide case-specific structural reasoning during deployment.

## 5.2 Representation Geometry and Strategy Effectiveness: An Exploratory Analysis

We present the following analysis as an exploratory observation derived from two encoders, not a validated mechanism.

Our negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining. Importantly, the three strategies differ in *selection method*—random sampling, cosine-similarity ranking in the pretrained embedding space (embedding-distance), and BM25 lexical ranking within CodeQL-identified structurally connected files (dataflow-aware)—while the analysis *evaluates* the resulting negatives' difficulty uniformly via pretrained encoder cosine similarity as a common metric.

When the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This is consistent with the [TBD: +X.Xpp] R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).

When the representation space has healthy separation—as observed for StarCoder2-3B (pos\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement ([TBD: +X.Xpp] for embedding vs.\ random, but [TBD: X.Xpp] for dataflow vs.\ random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance.

This interaction between representation geometry and strategy effectiveness has a practical implication: practitioners can compute pos\_sim on a held-out sample with their pretrained encoder (a single forward pass, requiring no training) to predict whether structure-grounded negatives are worth the extraction cost. We observe that pos\_sim > 0.98 serves as an approximate threshold above which structural negatives provide conditional benefit, though we note this threshold is derived from two encoder observations and should be validated more broadly.

## 5.3 Limitations

We identify several limitations of the current study that contextualize our findings:

**Encoder scope.** Our experiments use two decoder-only 3B-parameter encoders (Qwen2.5-Coder-3B and StarCoder2-3B). While these models differ meaningfully in pretraining corpus and representation geometry—enabling our interaction analysis—generalizing to encoder-only architectures (e.g., CodeBERT), larger scales, or non-code domains requires further investigation.

**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.

**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).

**Static mining.** Our negative mining is performed once before training and remains fixed throughout. Dynamic re-mining—where negatives are refreshed each epoch using the current encoder's embeddings—could yield progressively harder negatives as the model improves. We do not evaluate this variant in the current work and acknowledge the static-vs.-dynamic mining confound as a limitation. We plan to address this in future revisions.

**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.

## 5.4 Future Work

We identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:

**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.

**Representation-guided strategy selection.** Our observation that pos\_sim appears to correlate with strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.

**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.

