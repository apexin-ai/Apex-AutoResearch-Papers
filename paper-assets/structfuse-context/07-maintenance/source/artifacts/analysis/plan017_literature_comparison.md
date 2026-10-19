# Inference-time vs Training-time Structural Information: CodexGraph, LocAgent, and Related Methods vs StructFuse

## 1. Method Summaries

### 1.1 CodexGraph (Liu et al., NAACL 2025; arXiv:2408.03910)

**Core idea.** CodexGraph bridges LLM agents and code repositories by materializing a code property graph in a Neo4j graph database, then exposing a Cypher query interface that the LLM agent uses to perform multi-hop, structure-aware code retrieval at inference time.

**Graph construction.** A two-stage static analysis pipeline: (1) shallow intra-file indexing extracts MODULE, CLASS, and FUNCTION nodes; (2) cross-file analysis resolves inter-file relationships (CONTAINS, INHERITS, USES edges). The schema is task-agnostic—the same graph supports debugging, navigation, comment generation, etc. Importantly, CodexGraph captures *symbol-level structural relations* (call graphs, inheritance hierarchies) but **does not model data-flow semantics** (no taint tracking, no def-use chains).

**Computational overhead.** Graph construction is a one-time per-repository cost (comparable to IDE indexing), but **at inference time**, each query triggers the LLM agent to formulate and execute Cypher queries against the graph DB, often requiring multiple rounds of query refinement. This incurs latency proportional to the complexity of the code navigation task.

**Evaluation.** CrossCodeEval (code completion), SWE-bench (issue resolution), EvoCodeBench (evolving code). Five real-world application scenarios demonstrated.

**Open source.** Demo available at `modelscope/modelscope-agent/apps/codexgraph_agent` on GitHub.

### 1.2 LocAgent (Chen et al., ACL 2025; arXiv:2503.09089)

**Core idea.** LocAgent parses codebases into directed heterogeneous graphs and equips LLM agents with graph traversal tools, enabling multi-hop dependency reasoning for fault localization. The agent autonomously navigates the graph to locate buggy code given an issue description.

**Graph construction.** A directed heterogeneous graph with four edge types: *contain*, *import*, *invoke*, and *inherit*. Nodes represent files, classes, and functions. Graph construction is done per-repository (batch mode via `batch_build_graph.py`). Like CodexGraph, LocAgent captures **structural dependencies but not data-flow**—edges represent syntactic relationships (who calls whom, who inherits from whom), not how values propagate.

**Computational overhead.** The key cost driver is the LLM backbone: LocAgent achieves SOTA with a fine-tuned Qwen-2.5-Coder-32B model, but also works (at higher cost) with proprietary models. The authors report **~86% cost reduction** compared to proprietary-model baselines by using the fine-tuned open model. However, each localization query still requires multiple LLM inference calls as the agent traverses the graph.

**Evaluation.** SWE-bench-Lite: 92.7% file-level localization accuracy. Downstream: +12% Pass@10 on issue resolution when using LocAgent's localization output.

**Open source.** Available at `gersteinlab/LocAgent` on GitHub.

### 1.3 Other Related Inference-time Graph Methods

#### 1.3.1 RepoGraph (Ouyang et al., ICLR 2025; arXiv:2410.14684)

A plug-in module that constructs a **line-level code graph** (nodes = code lines; edges = definition-reference dependencies, class hierarchy, call graph). Designed as a drop-in enhancement for existing SE agents. On SWE-bench, integrating RepoGraph yields +32.8% relative improvement. Open source: `ozyyshr/RepoGraph` on GitHub. **No data-flow analysis**—purely structural relations.

#### 1.3.2 GraphCoder (Liu et al., ASE 2024; arXiv:2406.07003)

Constructs a **Code Context Graph (CCG)** combining control-flow graph (CFG), control-dependence graph (CDG), and data-dependence graph (DDG) for repository-level code completion. Employs coarse-to-fine retrieval: first match graph structure, then rank by code similarity. **Closest to StructFuse in using data/control flow**, but analysis is **intra-procedural only**—no cross-function data-flow tracking. Open source: `oceaneLIU/GraphCoder` on GitHub.

#### 1.3.3 RANGER (Shah et al., 2025; arXiv:2509.25257)

Combines a knowledge graph with **MCTS-guided traversal** for repository-level code retrieval. Dual-stage: entity queries use fast Cypher lookups; NL queries trigger MCTS exploration where a bi-encoder expands graph paths and a cross-encoder scores high-value candidates. Evaluated on CodeSearchNet, RepoQA, RepoBench, CrossCodeEval. **Heavy inference cost** due to MCTS rollouts + cross-encoder scoring. No data-flow analysis.

#### 1.3.4 ARISE (Seddik & Fard, 2026; arXiv:2605.03117)

Augments SWE-agent with a **multi-granularity program graph** extending down to statement-level nodes with **intra-procedural def-use edges**. Exposes a three-tier tool API including data-flow slicing as a first-class agent primitive. On SWE-bench Lite: +17.0 Function Recall@1, +15.0 Line Recall@1, 22.0% Pass@1. **Most similar to StructFuse in leveraging data-flow**, but limited to intra-procedural scope and used at inference time.

#### 1.3.5 CodeGRAG (2024; arXiv:2405.02355)

Bridges NL and PL via composed syntax graphs (AST + DFG + CFG). Unique in having **both training-time and inference-time graph components**: trains GNN-based soft prompts on graph structure, and uses graph prompts at inference. Data-flow extraction is function-level only. Evaluated on cross-lingual code generation.

#### 1.3.6 CodeRAG (2025; arXiv:2504.10046)

Constructs a **bigraph** (requirement graph + DS-code graph with dependency and semantic edges) for real-world code generation. Agentic reasoning allows LLMs to navigate the bigraph during generation. +40.90 Pass@1 with GPT-4o on DevEval. High inference overhead due to iterative graph reasoning.

### 1.4 StructFuse (Ours)

**Core idea.** StructFuse leverages CodeQL's bounded inter-procedural data-flow analysis (2-hop call-graph scope) to extract data-flow graphs **offline**, then uses these graphs to construct structure-grounded hard negatives for contrastive training of a cross-encoder. The key insight: code snippets that are structurally related via data-flow paths (e.g., a function that sanitizes input passed from a source to a sink) are semantically similar yet distinct—making them maximally informative hard negatives.

**Graph construction.** CodeQL static analysis with data-flow queries. This captures **bounded inter-procedural data-flow**: source→sink paths that cross function boundaries within a 2-hop call-graph scope, including through sanitizers, wrappers, and intermediate transformations. Average extraction time: **~8.9 seconds per instance**, with total extraction cost of **~110 hours for 44K training instances** (one-time, offline).

**Computational overhead at inference.** **Zero.** Once the cross-encoder is trained with structural negatives, inference is standard model forward pass—no graph construction, no graph traversal, no additional LLM calls. The structural knowledge is distilled into the model's parameters.

**Evaluation.** Code retrieval benchmarks with contrastive learning evaluation.

---

## 2. Comparative Analysis

### 2.1 Methodological Differences

The fundamental distinction is **when and how** structural information enters the pipeline:

| Dimension | Inference-time methods | StructFuse (training-time) |
|-----------|----------------------|---------------------------|
| **Graph usage** | Constructed per-repo; queried per-request | Constructed per-repo; consumed during training only |
| **Information flow** | Graph → agent reasoning → output | Graph → hard negatives → encoder parameters → output |
| **Data-flow depth** | Mostly structural (call/import/inherit); GraphCoder & ARISE have intra-proc data-flow | **Bounded inter-procedural** data-flow analysis (2-hop) via CodeQL |
| **LLM dependency at inference** | Requires LLM agent for graph navigation | No LLM needed; single encoder forward pass |
| **Adaptability to new repos** | Immediate (build graph + query) | Requires retraining or transfer from existing training |

**Training-time approach (StructFuse):** The graph is a *training signal generator*, not a runtime component. By mining hard negatives from data-flow relationships, the model learns to distinguish semantically subtle code differences that surface-level features miss. This is analogous to how knowledge distillation compresses a teacher's knowledge into a student—except here, the "teacher" is the CodeQL data-flow analysis.
<!-- 中文注释：StructFuse 的核心创新在于将图信息"蒸馏"到模型参数中，而非在推理时依赖图 -->

**Inference-time approach (CodexGraph, LocAgent, etc.):** The graph is a *runtime navigation aid*. The LLM agent explicitly traverses the graph to gather context. This provides maximum flexibility (any query can explore any graph path) but ties inference cost to graph complexity and query difficulty.

### 2.2 Computational Cost Comparison

#### StructFuse: Front-loaded, amortized cost

- **CodeQL extraction:** ~8.9s per instance average; ~110 hours total for 44K instances (one-time)
- **Training cost:** Standard contrastive learning with hard negatives (no additional cost beyond baseline training)
- **Inference cost:** Single cross-encoder forward pass. **No graph overhead whatsoever.**
- **Scaling model:** Cost is O(training data size), independent of query volume. For a service handling 1M queries/day, the per-query marginal cost of structural knowledge is effectively zero.

#### CodexGraph: Per-repo setup + per-query agent cost

- **Graph construction:** One-time per repository (comparable to IDE indexing). For large repos, the two-stage static analysis (intra-file + cross-file) can take minutes to hours.
- **Inference cost:** Each query triggers Cypher query formulation + execution + result interpretation by the LLM. Multiple rounds of query refinement are common. Cost scales with query complexity and repository size.
- **LLM cost:** Requires a capable LLM (GPT-4 class) as the agent backbone.

#### LocAgent: Graph setup + LLM agent inference

- **Graph construction:** Batch mode available (`batch_build_graph.py`); four edge types to resolve per repository.
- **Inference cost:** Multiple LLM calls per localization query as the agent traverses the graph. With Qwen-2.5-Coder-32B: ~86% cheaper than GPT-4-based approaches, but still requires multi-turn LLM inference.
- **Fine-tuning cost:** Training a 32B model for graph-guided localization is a significant one-time investment.

#### RANGER: Heaviest inference cost

- **MCTS rollouts + cross-encoder scoring at inference time.** Each query potentially explores many graph paths before converging.
- **Dual model cost:** bi-encoder for expansion + cross-encoder for reward evaluation.

**Summary:** StructFuse pays upfront (~110h CodeQL extraction) and gets free inference forever. Inference-time methods pay per-query, with costs ranging from moderate (LocAgent with fine-tuned model) to heavy (RANGER with MCTS). For high-throughput code search services, StructFuse's cost model is dramatically more favorable.
<!-- 中文注释：对于高 QPS 场景（如企业代码搜索），StructFuse 的成本优势是压倒性的 -->

### 2.3 Complementarity

StructFuse and inference-time graph methods are **orthogonal and composable**. They operate at different stages of the retrieval pipeline and address different aspects of the problem:

**StructFuse as first-stage retriever + inference-time graph as reranker/navigator:**
- A StructFuse-trained encoder provides fast, structure-aware initial retrieval (top-k candidates in milliseconds).
- An inference-time graph method (CodexGraph, LocAgent) then navigates the code graph to refine, verify, or expand the retrieved context.
- This combination leverages StructFuse's efficiency for broad retrieval and inference-time methods' precision for targeted reasoning.

**Concrete example:** For a code search query, StructFuse retrieves the top-50 candidates using embeddings that already encode data-flow semantics. RANGER or CodexGraph then performs graph-guided reranking on this small candidate set, achieving high precision without the cost of searching the entire repository graph.

**Why they don't conflict:**
- StructFuse's hard negatives teach the model *what structural relationships matter* (offline learning).
- Inference-time methods provide *explicit structural reasoning* for specific queries (online reasoning).
- These are complementary: the encoder has internalized general structural patterns, while the graph agent handles case-specific navigation.

**Limitation of combination:** The main cost is engineering complexity—maintaining both a trained encoder and a runtime graph infrastructure. Whether this is worthwhile depends on the precision requirements and query volume of the target application.

### 2.4 Applicable Scenarios

| Scenario | Best approach | Rationale |
|----------|--------------|-----------|
| **High-QPS code search service** (e.g., enterprise search with millions of daily queries) | StructFuse | Zero per-query graph cost; latency-sensitive; structural knowledge baked into embeddings |
| **Interactive debugging / issue resolution** (developer exploring unfamiliar codebase) | Inference-time (CodexGraph, LocAgent) | Requires flexible, open-ended graph exploration; query volume is low; precision matters more than latency |
| **Fault localization in CI/CD pipeline** | LocAgent / ARISE | Specific task with well-defined graph traversal patterns; benefits from multi-hop reasoning |
| **Repository-level code completion** | GraphCoder + StructFuse backbone | GraphCoder's CCG provides local context; StructFuse encoder provides cross-file retrieval |
| **Maximum precision, cost is secondary** | RANGER or StructFuse + inference-time reranker | MCTS exploration maximizes recall; StructFuse narrows search space |
| **New repository with no training data** | Inference-time methods | StructFuse requires training data with structural negatives; inference-time methods work immediately on any repo with a parseable graph |
| **Cross-repository transfer** | StructFuse (if domain-similar) | Trained encoder generalizes across repos with similar structural patterns; inference-time methods must rebuild graphs per repo |

<!-- 中文注释：关键判断——StructFuse 在"离线可准备、在线要快"的场景占优；inference-time methods 在"灵活探索、精度优先"的场景占优 -->

---

## 3. Implications for Paper

### Related Work paragraph (suggested wording)

> **Graph-Based Methods for Code Understanding.** Recent work has explored leveraging code structure graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code property graph database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level line-granularity navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) incorporates intra-procedural control-flow and data-dependence for code completion, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. These methods achieve strong task-specific results but impose per-query inference costs—graph construction, traversal, and often multiple LLM calls—and their data-flow analysis remains intra-procedural at most. StructFuse takes a fundamentally different approach: we leverage CodeQL's bounded inter-procedural data-flow analysis (2-hop call-graph scope) to extract data-flow graphs *offline* and generate structure-grounded hard negatives for contrastive encoder training. This distills cross-function data-flow semantics into model parameters, yielding zero-overhead inference while capturing deeper structural relationships than existing graph-based methods.

### Discussion paragraph (suggested wording)

> **Training-time vs Inference-time Structural Information.** Our approach is complementary to inference-time graph methods rather than competing with them. While systems like CodexGraph and LocAgent provide flexible, query-adaptive graph navigation at runtime, they incur per-query costs that scale with graph complexity and require capable LLM backends. StructFuse amortizes all structural computation to training time: our CodeQL extraction costs approximately 8.9 seconds per instance (~110 GPU-free hours for 44K instances), after which the trained encoder operates at standard inference speed with no graph overhead. This makes StructFuse particularly suited for latency-sensitive, high-throughput retrieval scenarios. Moreover, the two paradigms are composable: a StructFuse-trained encoder can serve as an efficient first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. A promising direction for future work is evaluating such hybrid pipelines, as well as extending StructFuse's bounded inter-procedural analysis beyond the current 2-hop scope or to the inference-time setting where it could further benefit graph-guided agents.

### Reviewer question strategy: "Why not compare directly with inference-time graph methods?"

**Key arguments:**

1. **Different computational paradigms, not directly comparable.** StructFuse is a *training method* that improves encoder quality; CodexGraph/LocAgent are *inference systems* that augment LLM agents with runtime graph access. Comparing them is like comparing data augmentation vs. test-time augmentation—they operate at different stages and can be combined.

2. **Different task interfaces.** Most inference-time graph methods are designed for agentic tasks (issue resolution, fault localization) where the LLM agent interacts with the graph over multiple turns. StructFuse targets embedding-based code retrieval where the output is a ranked list, not a multi-turn interaction.

3. **Complementary, not competing.** We can acknowledge this gap and frame it constructively: "StructFuse's trained encoder could serve as the retrieval backbone within these systems, replacing their default embedding models. Evaluating such integration is a natural and valuable direction for future work."

4. **Empirical grounding.** If pressed, note that inference-time methods have been evaluated on different benchmarks (SWE-bench for LocAgent, CrossCodeEval for CodexGraph) with different metrics, making direct numerical comparison methodologically questionable without a unified evaluation setup.

<!-- 中文注释：核心策略——承认对比的价值，但指出"不同范式"+"不同任务接口"使直接对比不恰当，同时提出组合使用作为 future work -->

---

## References

- **CodexGraph:** Liu et al., "CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases," NAACL 2025. arXiv:2408.03910. [Paper](https://arxiv.org/abs/2408.03910)
- **LocAgent:** Chen et al., "LocAgent: Graph-Guided LLM Agents for Code Localization," ACL 2025. arXiv:2503.09089. [Paper](https://arxiv.org/abs/2503.09089) | [Code](https://github.com/gersteinlab/LocAgent)
- **RepoGraph:** Ouyang et al., "Enhancing AI Software Engineering with Repository-level Code Graph," ICLR 2025. arXiv:2410.14684. [Paper](https://arxiv.org/abs/2410.14684) | [Code](https://github.com/ozyyshr/RepoGraph)
- **GraphCoder:** Liu et al., "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model," ASE 2024. arXiv:2406.07003. [Paper](https://arxiv.org/abs/2406.07003) | [Code](https://github.com/oceaneLIU/GraphCoder)
- **RANGER:** Shah et al., "RANGER: Repository-Level Agent for Graph-Enhanced Retrieval," 2025. arXiv:2509.25257. [Paper](https://arxiv.org/abs/2509.25257)
- **ARISE:** Seddik & Fard, "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair," 2026. arXiv:2605.03117. [Paper](https://arxiv.org/abs/2605.03117)
- **CodeGRAG:** "CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation," 2024. arXiv:2405.02355. [Paper](https://arxiv.org/abs/2405.02355)
- **CodeRAG:** "CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation," 2025. arXiv:2504.10046. [Paper](https://arxiv.org/abs/2504.10046)
