# writing related work v1 reviewer2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_writing_related-work-v1-reviewer2_20260515T095827.jsonl`
- **Structured JSON:** [`27a869655e6b647fda79.json`](../../sessions/27/27a869655e6b647fda79.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-15T10:00:20.277480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T10:00:20.277890+00:00_

1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Contrastive learning has become a dominant paradigm for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-m
…[truncated 4087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T10:00:20.278091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T10:00:20.278267+00:00_

1	# 1. Introduction
2	
3	Resolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \cite{jimenez2024swebench}.
4	Dense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \cite{reddy2025swerank,xie2025swefixer}.
5	These approaches build on a rich lineage of pre-trained code representations---from CodeBERT \cite{feng2020codebert} and UniXcoder \cite{guo2022unixcoder} to decoder-only code models \cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.
6	Yet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.
7	Despite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.
8	
9	In open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.
10	DPR \cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.
11	These methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \cite{zhan2021star,zeng2022cldrd}.
12	In the code domain, however, the picture is less clear.
13	CoCoHaNeRe \cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-ba
…[truncated 3925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T10:00:20.278429+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T10:00:20.278559+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T10:00:20.278736+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GraphCoder ASE 2024 Liu data-flow intra-procedural inter-procedural code retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GraphCoder ASE 2024 Liu data-flow intra-procedural inter-procedural code retrieval"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T10:00:20.278862+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARISE arXiv 2605.03117 Seddik 2026 data-flow scope intra-procedural"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARISE arXiv 2605.03117 Seddik 2026 data-flow scope intra-procedural"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T10:00:20.279007+00:00_

Web search results for query: "ARISE arXiv 2605.03117 Seddik 2026 data-flow scope intra-procedural"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.06826] How Does Attention Help? Insights from Random Matrices on Signal Recovery from Sequence Models","url":"https://arxiv.org/abs/2605.06826"},{"title":"[2605.13681] Sampling from Flow Language Models via Marginal-Conditioned Bridges","url":"https://arxiv.org/abs/2605.13681"},{"title":"[2605.13509] Quantifying information flow along a stochastic trajectory","url":"https://arxiv.org/abs/2605.13509"},{"title":"[2605.10938] ELF: Embedded Language Flows","url":"https://arxiv.org/abs/2605.10938"},{"title":"[2605.12951] Coreset-Induced Conditional Velocity Flow Matching","url":"https://arxiv.org/abs/2605.12951"},{"title":"[2605.02287] Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading in Decentralized Prediction Markets","url":"https://arxiv.org/abs/2605.02287"},{"title":"[2605.14137] Flow Field Reconstruction with Sensor Placement Policy Learning","url":"https://arxiv.org/abs/2605.14137"},{"title":"[2605.08648] FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts","url":"https://arxiv.org/abs/2605.08648"}]

Based on the search results, I found the paper you're looking for:

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do n
…[truncated 624 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T10:00:20.279209+00:00_

Web search results for query: "GraphCoder ASE 2024 Liu data-flow intra-procedural inter-procedural code retrieval"

Links: [{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024","url":"https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"GitHub - oceaneLIU/GraphCoder","url":"https://github.com/oceaneLIU/GraphCoder"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF","url":"https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"},{"title":"39th ASE 2024: Sacramento, CA, USA","url":"https://dblp.org/db/conf/kbse/ase2024.html"},{"title":"2024 39th IEEE/ACM International Conference on ...","url":"https://www.computer.org/csdl/proceedings/ase/2024/22gEsOsLriM"},{"title
…[truncated 1760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T10:00:20.279395+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GraphCoder \"code context graph\" CCG \"intra-procedural\" OR \"within function\" OR \"single function\" scope ASE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GraphCoder \"code context graph\" CCG \"intra-procedural\" OR \"within function\" OR \"single function\" scope ASE 2024"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T10:00:20.279528+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARISE arXiv 2605.03117 \"intra-procedural\" \"definition-use\" \"inter-procedural\" repository-level graph"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARISE arXiv 2605.03117 \"intra-procedural\" \"definition-use\" \"inter-procedural\" repository-level graph"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T10:00:20.279762+00:00_

Web search results for query: "GraphCoder "code context graph" CCG "intra-procedural" OR "within function" OR "single function" scope ASE 2024"

Links: [{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024","url":"https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"GitHub - oceaneLIU/GraphCoder","url":"https://github.com/oceaneLIU/GraphCoder"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code","url":"https://openreview.net/pdf/7a92572e89daf427869cbb262f97920e5f6f35a3.pdf"},{"title":"GraphCoder | NL2Code","url":"https://nl2code.github.io/posts/GraphCoder/"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph - Consensus","url":"https://consensus.app/papers/graphcoder-enhancing-repositorylevel-code-completion-wang-jin/b4870512e370577aa2ee9b8b4aee9bfd/"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on
…[truncated 1830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T10:00:20.280004+00:00_

Web search results for query: "ARISE arXiv 2605.03117 "intra-procedural" "definition-use" "inter-procedural" repository-level graph"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"RepoAudit: An Autonomous LLM-Agent for Repository- ...","url":"https://arxiv.org/pdf/2501.18160"},{"title":"INTERPROCEDURAL ANALYSIS","url":"https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"},{"title":"[2605.00817] When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models","url":"https://arxiv.org/abs/2605.00817"},{"title":"Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural","url":"https://www.arxiv.org/pdf/2602.06751"},{"title":"Retrieval from Within: An Intrinsic Capability of Attention-Based Models","url":"https://arxiv.org/html/2605.05806"},{"title":"SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution","url":"https://arxiv.org/html/2605.10114"},{"title":"Beyond State Machines: Executing Network Procedures with Agentic Tool-Calling Sequences","url":"https://arxiv.org/html/2605.02584"},{"title":"Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection","url":"https://arxiv.org/html/2602.06751v1"}]

Based on the web search results, I found information about the arXiv paper 2605.03117:

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

Repository-level fault localization and automated program repair require an agent to identify the rele
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T10:00:20.280201+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GraphCoder arxiv 2406.07003 \"code context graph\" scope statement-level function-level \"control flow\" \"data dependence\" construction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GraphCoder arxiv 2406.07003 \"code context graph\" scope statement-level function-level \"control flow\" \"data dependence\" construction"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T10:00:20.280334+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARISE arxiv 2605.03117 \"inter-procedural\" OR \"cross-function\" OR \"call graph\" data-flow edges graph construction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARISE arxiv 2605.03117 \"inter-procedural\" OR \"cross-function\" OR \"call graph\" data-flow edges graph construction"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T10:00:20.280497+00:00_

Web search results for query: "ARISE arxiv 2605.03117 "inter-procedural" OR "cross-function" OR "call graph" data-flow edges graph construction"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"Interprocedural Dataflow Analysis in the Presence of Large Libraries | SpringerLink","url":"https://link.springer.com/chapter/10.1007/11688839_2"},{"title":"INTERPROCEDURAL ANALYSIS","url":"https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"},{"title":"GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub","url":"https://github.com/ChrisCummins/ProGraML"},{"title":"Precise interprocedural dataflow analysis with applications to constant propagation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/0304397596000722"},{"title":"[1304.6274] Interprocedural Data Flow Analysis in Soot using Value Contexts","url":"https://arxiv.org/abs/1304.6274"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"http://proceedings.mlr.press/v139/cummins21a/cummins21a.pdf"},{"title":"PROGRAML: A Graph-based Program Representation for ...","url":"https://www.research.ed.ac.uk/files/221627281/PROGRAML_CUMMINS_DOA08052021_AFV.pdf"},{"title":"PhASAR: An Inter-procedural Static Analysis Framework for C/C++ | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-17465-1_22"}]

Based on the search results, I found information about the ARISE paper (arxiv 2605.03117):

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relation
…[truncated 1000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T10:00:20.280795+00:00_

Web search results for query: "GraphCoder arxiv 2406.07003 "code context graph" scope statement-level function-level "control flow" "data dependence" construction"

Links: [{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"(PDF) GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://www.researchgate.net/publication/381318841_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Code_Context_Graph-based_Retrieval_and_Language_Model"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"},{"title":"Enhancing Domain-Specific Code Completion via Collaborative Inference with Large and Small Language Models | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3770748"},{"title":"GraphCoder: Enhancing Repository-Level Code ...","url":"https://arxiv.org/pdf/2406.07003"},{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://arxiv.org/html/2504.10046v1"},{"title":"Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases","url":"https://arxiv.org/html/2507.19942v1"},{"title":"[Literature Review] GraphCoder: Enhancing Repository-Level Code Comple
…[truncated 1882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T10:00:20.281035+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope.",
  "new_string": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "old_string": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope.",
    "new_string": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T10:00:20.281200+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T10:00:20.281327+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "Critically, all these methods construct and query graphs at inference time",
  "new_string": "Critically, these methods primarily leverage structural graphs at inference time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "old_string": "Critically, all these methods construct and query graphs at inference time",
    "new_string": "Critically, these methods primarily leverage structural graphs at inference time"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T10:00:20.281474+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T10:00:20.281616+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training.",
  "new_string": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "old_string": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training.",
    "new_string": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach."
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T10:00:20.281779+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T10:00:20.281903+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension:",
  "new_string": "These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "old_string": "These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension:",
    "new_string": "These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension:"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T10:00:20.282074+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T10:00:20.282218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T10:00:20.282372+00:00_

1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Contrastive learning has become a dominant paradigm for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-m
…[truncated 4437 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-15T10:00:20.282552+00:00_

四项修改完成，摘要如下：

**修正 1 (§2.4)** — GraphCoder/ARISE scope：WebSearch 确认两者的 data-flow 分析确实是 intra-procedural（GraphCoder 用 CFG/CDG/DDG，ARISE 明确描述为 "intra-procedural definition-use edges"）。保留 intra-procedural 断言，但改写为更精确的表述，区分了两者各自的 data-flow 类型（control/data dependence vs. definition-use chains），并明确是 "data-flow analysis" 而非整个系统受限于 intra-procedural。

**修正 2 (§2.4)** — "all these methods" → "these methods primarily leverage structural graphs at inference time"，软化了全称断言。

**修正 3 (§2.3)** — CoCoHaNeRe 句后新增一句，说明该工作同时评估了多种非梯度策略（BM25 和 embedding-based），消除与 Introduction（批评 embedding negatives）的表述不一致。

**修正 4 (§2.2)** — 在 StructFuse 定位句前插入半句 "While GraphCodeBERT uses structural edges as a pretraining objective"，明确区分 pretraining objective vs. training-time negative selection。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_related-work-v1-reviewer2_20260515T095827"
}
```

</details>

---
