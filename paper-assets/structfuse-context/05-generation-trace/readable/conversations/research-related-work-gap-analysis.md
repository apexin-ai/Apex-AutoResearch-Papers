# research related work gap analysis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 0
- **Tool calls:** 35
- **Original source:** `logs/chats/worker_research_related-work-gap-analysis_20260515T041514.jsonl`
- **Structured JSON:** [`82673cf7d6969034c3bb.json`](../../sessions/82/82673cf7d6969034c3bb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

71 recorded events

### Tool call

_source line 1 · 2026-05-15T04:20:41.397901+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T04:20:41.398261+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T04:20:41.398451+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T04:20:41.398846+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 39 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n     
…[truncated 15730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T04:20:41.399047+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "artifacts/paper_drafts/discussion_v2.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "artifacts/paper_drafts/discussion_v2.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T04:20:41.399191+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/paper_drafts/discussion_v2.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T04:20:41.399331+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T04:20:41.399566+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo
…[truncated 11498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T04:20:41.399859+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search gap area papers",
  "prompt": "I need to find real, verified academic papers to fill citation gaps for a paper about using code structure (call graph / data-flow) for contrastive learning hard negative mining in code retrieval. The paper already has 39 citations but needs better coverage in certain areas.\n\nSearch for the following papers using WebSearch. For each paper, confirm: title, authors, venue, year. Only return papers you can verify exist.\n\n**Area 1: Contrastive Learning for Code (need 2-3 more)**\n- Search: \"contrastive learning code representation 2022 2023 2024 ACL EMNLP ICLR NeurIPS\"\n- Look for: SynCoBERT, DISCO, or other contrastive code learning papers\n- Search: \"self-supervised code understanding contrastive pre-training\"\n\n**Area 2: Hard Negative Mining in Dense Retrieval (need 1-2 more)**\n- Search: \"RocketQA hard negative mining dense retrieval 2021\"\n- Search: \"hard negative mining contrastive learning survey 2023 2024\"\n- Search: \"debiased contrastive learning hard negatives retrieval\"\n\n**Area 3: Code Search / Dense Retrieval for Code (need 1-2)**\n- Search: \"dense code retrieval neural code search 2023 2024 ICSE FSE\"\n- Search: \"CoSQA code search question answering benchmark\"\n\n**Area 4: Repository-level Code Understanding (need 1-2)**\n- Search: \"repository level code understanding cross-file context 2024\"\n- Search: \"CrossCodeEval benchmark cross-file code completion\"\n\n**Area 5: Program Analysis meets Deep Learning (need 1)**\n- Search: \"ProGraML program graph machine learning 2021\"\n- Search: \"learning program semantics graph neural network ICML NeurIPS\"\n\n**Area 6: Training Data Quality / Curriculum for Retrieval (need 1)**\n- Search: \"data quality curriculum learning dense retrieval 2023 2024\"\n\nFor each paper found, provide:\n- Exact title\n- Authors (first 3 + et al.)\n- Venue and year\n- One sentence on why it's relevant to a paper about structure-grounded hard negative mining for code retrieval\n\nReturn a clean list grouped by area. Only include papers you verified via web search.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "Agent",
  "tool_args": {
    "description": "Search gap area papers",
    "prompt": "I need to find real, verified academic papers to fill citation gaps for a paper about using code structure (call graph / data-flow) for contrastive learning hard negative mining in code retrieval. The paper already has 39 citations but needs better coverage in certain areas.\n\nSearch for the following papers using WebSearch. For each paper, confirm: title, authors, venue, year. Only return papers you can verify exist.\n\n**Area 1: Contrastive Learning for Code (need 2-3 more)**\n- Search: \"contrastive learning code representation 2022 2023 2024 ACL EMNLP ICLR NeurIPS\"\n- Look for: SynCoBERT, DISCO, or other contrastive code learning papers\n- Search: \"self-supervised code understanding contrastive pre-training\"\n\n**Area 2: Hard Negative Mining in Dense Retrieval (need 1-2 more)**\n- Search: \"RocketQA hard negative mining dense retrieval 2021\"\n- Search: \"hard negative mining contrastive learning survey 2023 2024\"\n- Search: \"debiased contrastive learning hard negatives retrieval\"\n\n**Area 3: Code Search / Dense Retrieval for Code (need 1-2)**\n- Search: \"dense code retrieval neural code search 2023 2024 ICSE FSE\"\n- Search: \"CoSQA code search question answering benchmark\"\n\n**Area 4: Repository-level Code Understanding (need 1-2)**\n- Search: \"repository level code understanding cross-file context 2024\"\n- Search: \"CrossCodeEval benchmark cross-file code completion\"\n\n**Area 5: Program Analysis meets Deep Learning (need 1)**\n- Search: \"ProGraML program graph machine learning 2021\"\n- Search: \"learning program semantics graph neural network ICML NeurIPS\"\n\n**Area 6: Training Data Quality / Curriculum for Retrieval (need 1)**\n- Search: \"data quality curriculum learning dense retrieval 2023 2024\"\n\nFor each paper found, provide:\n- Exact title\n- Authors (first 3 + et al.)\n- Venue and year\n- One sentence on why it's relevant to a paper about structure-grounded hard negative mining for code retrieval\n\nReturn a clean list grouped by area. Only include papers you verified via web search.",
    "model": "sonnet"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T04:20:41.400064+00:00_

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
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
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

_source line 11 · 2026-05-15T04:20:41.400196+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T04:20:41.400326+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SynCoBERT contrastive learning code representation 2022 ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SynCoBERT contrastive learning code representation 2022 ACL EMNLP"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T04:20:41.400456+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DISCO contrastive learning code understanding pre-training 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DISCO contrastive learning code understanding pre-training 2023"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T04:20:41.400631+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RocketQA hard negative mining dense retrieval 2021 NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RocketQA hard negative mining dense retrieval 2021 NAACL"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T04:20:41.400798+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoSQA code search question answering benchmark 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoSQA code search question answering benchmark 2021"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T04:20:41.400931+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CrossCodeEval benchmark cross-file code completion 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CrossCodeEval benchmark cross-file code completion 2024"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T04:20:41.401053+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProGraML program graph machine learning ICML 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProGraML program graph machine learning ICML 2021"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T04:20:41.401185+00:00_

Web search results for query: "SynCoBERT contrastive learning code representation 2022 ACL EMNLP"

Links: [{"title":"[2108.04556] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://arxiv.org/abs/2108.04556"},{"title":"[2108.04556] SynCoBERT: Syntax-Enhanced Contrastive Pre-Training for Code Representation","url":"https://ar5iv.labs.arxiv.org/html/2108.04556"},{"title":"[PDF] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SynCoBERT:-Syntax-Guided-Multi-Modal-Contrastive-Wang-Wang/14b104d1a1c0b784e4e74454d809455cc47d0093"},{"title":"[2108.04556v3] SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://arxiv.org/abs/2108.04556v3"},{"title":"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/wang2021syncobert/"},{"title":"(PDF) SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation","url":"https://www.academia.edu/73281297/SynCoBERT_Syntax_Guided_Multi_Modal_Contrastive_Pre_Training_for_Code_Representation"},{"title":"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210804556W/abstract"},{"title":"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation | DeepAI","url":"https://deepai.org/publication/syncobert-syntax-guided-multi-modal-contrastive-pre-training-for-code-representation"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070/36225"},{"title":"SYNCOBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for","url":"https://arxiv.org/pdf/2108.04556"}]

Based on the search results, here's what
…[truncated 1284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T04:20:41.401345+00:00_

Web search results for query: "ProGraML program graph machine learning ICML 2021"

Links: [{"title":"GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub","url":"https://github.com/ChrisCummins/ProGraML"},{"title":"ICML 2021 ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations Spotlight","url":"https://icml.cc/virtual/2021/spotlight/8886"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"https://chriscummins.cc/pub/2021-icml.pdf"},{"title":"Downloads 2021","url":"https://icml.cc/Downloads/2021"},{"title":"ICML 2021 Schedule","url":"https://icml.cc/virtual/2021/calendar"},{"title":"Machine Learning for Software Engineering papers at ICML 2021 · GitHub","url":"https://gist.github.com/bzz/38cfef2e735393a5ccf59f70ddff77d0"},{"title":"ProGraML: Graph-based Deep Learning for Program Optimization and Analysis.","url":"https://spcl.inf.ethz.ch/Publications/.pdf/programl-icml21-slides.pdf"},{"title":"[2003.10536] ProGraML: Graph-based Deep Learning for Program Optimization and Analysis","url":"https://arxiv.org/abs/2003.10536"},{"title":"PROGRAML: GRAPH-BASED DEEP LEARNING FOR PROGRAM OPTIMIZATION AND ANALYSIS","url":"https://arxiv.org/pdf/2003.10536"},{"title":"ICML: International Conference on Machine Learning 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1421"}]

I've found comprehensive information about ProGraML from ICML 2021. Here are the key findings:

## Overview

ProGraML - Program Graphs for Machine Learning - is a language-independent, portable representation of program semantics. ProGraML is a representation for programs as input to a machine learning model.

## Key Features

The system supports several programming languages (C, C++, LLVM-IR, XLA) and several graph formats (NetworkX, DGL, Graphviz, JSON) out of the box. It captures every control, data, and call relation across entire prog
…[truncated 876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T04:20:41.401500+00:00_

Web search results for query: "DISCO contrastive learning code understanding pre-training 2023"

Links: [{"title":"DisCo: Graph-Based Disentangled Contrastive Learning for Cold-Start Cross-Domain Recommendation","url":"https://arxiv.org/html/2412.15005v1"},{"title":"GitHub - xrenaa/DisCo: [ICLR2022] Code for \"Learning Disentangled Representation by Exploiting Pretrained Generative Models: A Contrastive Learning View\"","url":"https://github.com/xrenaa/DisCo"},{"title":"DisCo: Graph-Based Disentangled Contrastive Learning for Cold-Start","url":"https://arxiv.org/pdf/2412.15005"},{"title":"GitHub - KingGugu/DA-CL-4Rec: The latest research progress of Contrastive Learning(CL), Data Augmentation(DA) and Self-Supervised Learning(SSL) in Recommender Systems · GitHub","url":"https://github.com/KingGugu/DA-CL-4Rec"},{"title":"Contrastive Representation Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2021-05-31-contrastive/"},{"title":"[2412.15005] DisCo: Graph-Based Disentangled Contrastive Learning for Cold-Start Cross-Domain Recommendation","url":"https://ar5iv.labs.arxiv.org/html/2412.15005"},{"title":"CONTRASTIVE CODE REPRESENTATION LEARNING","url":"https://openreview.net/pdf?id=uV7hcsjqM-"},{"title":"GitHub - YuanchenBei/Awesome-Cold-Start-Recommendation: [Up-to-date] A curated list of resources on cold-start recommendations. · GitHub","url":"https://github.com/YuanchenBei/Awesome-Cold-Start-Recommendation"},{"title":"Advanced code time complexity prediction approach using contrastive learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197625006311"},{"title":"DiSCo: Disrupting Semantic Consistency for Transferable Cross-Modal Adversarial Attacks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-6957-1_2"}]

Based on the search results, I found relevant information about code-related contrastive learning research. Here are the key findings:

## ContraCode: Contrastive Code Represen
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T04:20:41.401678+00:00_

Web search results for query: "CoSQA code search question answering benchmark 2021"

Links: [{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210513239H/abstract"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.442/"},{"title":"GitHub - Jun-jie-Huang/CoCLR: Source Code for ACL-21 main conference paper \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\".","url":"https://github.com/Jun-jie-Huang/CoCLR"},{"title":"[2105.13239] CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://arxiv.org/abs/2105.13239"},{"title":"[2105.13239v1] CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://arxiv.org/abs/2105.13239v1"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/cosqa-20-000-web-queries-for-code-search-and-question-answering/"},{"title":"CoSQA+: Pioneering the Multi-Choice Code Search Benchmark with Test-Driven Agents","url":"https://arxiv.org/html/2406.11589v4"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://arxiv.org/pdf/2105.13239"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://gengo.sotaro.io/2021.acl-long.442"},{"title":"CoSQA+: Enhancing Code Search Evaluation with a Multi-Choice Benchmark and Test-Driven Agents","url":"https://arxiv.org/html/2406.11589"}]

I found comprehensive information about the CoSQA benchmark. Here are the key details:

## CoSQA: Code Search and Question Answering Benchmark (2021)

CoSQA is titled "20,000+ Web Queries for Code Search and Question Answering" and was published in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T04:20:41.401839+00:00_

Web search results for query: "CrossCodeEval benchmark cross-file code completion 2024"

Links: [{"title":"[2310.11248] CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://arxiv.org/abs/2310.11248"},{"title":"CrossCodeEval","url":"https://crosscodeeval.github.io/"},{"title":"GitHub - amazon-science/cceval: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion (NeurIPS 2023)","url":"https://github.com/amazon-science/cceval"},{"title":"NeurIPS Poster CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://neurips.cc/virtual/2023/poster/73423"},{"title":"A Diverse and Multilingual Benchmark for Cross-File Code ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/920f2dced7d32ab2ba2f1970bc306af6-Paper-Datasets_and_Benchmarks.pdf"},{"title":"STALL+: Boosting LLM-based Repository-level Code Completion","url":"https://mingwei-liu.github.io/assets/pdf/arxiv2024STALL.pdf"},{"title":"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion | OpenReview","url":"https://openreview.net/forum?id=wgDcbBMSfh"},{"title":"[PDF] CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CrossCodeEval:-A-Diverse-and-Multilingual-Benchmark-Ding-Wang/f1bd7ea3a63b78a60b5d90d91fdb4a1d7ac0de8e"},{"title":"RepoMasterEval: Evaluating Code Completion via Real-World Repositories","url":"https://arxiv.org/pdf/2408.03519"},{"title":"dblp: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion.","url":"https://dblp.org/rec/journals/corr/abs-2310-11248.html"}]

Based on the search results, here's what I found about CrossCodeEval:

## Overview

CrossCodeEval is a diverse and multilingual code completion benchmark that necessitates an in-depth cross-file contextual understanding to complete the code accurately.

## Purpose an
…[truncated 1576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T04:20:41.402001+00:00_

Web search results for query: "RocketQA hard negative mining dense retrieval 2021 NAACL"

Links: [{"title":"Research/NLP/NAACL2021-RocketQA at master · PaddlePaddle/Research","url":"https://github.com/PaddlePaddle/Research/tree/master/NLP/NAACL2021-RocketQA"},{"title":"RocketQA/research/RocketQA_NAACL2021 at main · PaddlePaddle/RocketQA","url":"https://github.com/PaddlePaddle/RocketQA/tree/main/research/RocketQA_NAACL2021"},{"title":"RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.466/"},{"title":"(PDF) RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering","url":"https://www.academia.edu/75599741/RocketQA_An_Optimized_Training_Approach_to_Dense_Passage_Retrieval_for_Open_Domain_Question_Answering"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"RocketQA: An Optimized Training Approach to Dense ...","url":"https://aclanthology.org/2021.naacl-main.466.pdf"},{"title":"RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering | Request PDF","url":"https://www.researchgate.net/publication/352364344_RocketQA_An_Optimized_Training_Approach_to_Dense_Passage_Retrieval_for_Open-Domain_Question_Answering"},{"title":"RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv201008191Q/abstract"},{"title":"GitHub - PaddlePaddle/RocketQA: 🚀 RocketQA, dense retrieval for information retrieval and question answering, including both Chinese and English state-of-the-art models.","url":"https://github.com/PaddlePaddle/RocketQA"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://aclanthology.org/2025.acl-industry.72.pdf"}]

Based on the search results, here's what I fo
…[truncated 1207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T04:20:41.402168+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ContraCode contrastive learning code representation self-supervised 2022 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ContraCode contrastive learning code representation self-supervised 2022 ICLR"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T04:20:41.402305+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hard negative mining contrastive learning survey dense retrieval 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hard negative mining contrastive learning survey dense retrieval 2023 2024"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T04:20:41.402434+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "repository level code understanding cross-file context LLM 2024 ICSE FSE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "repository level code understanding cross-file context LLM 2024 ICSE FSE"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T04:20:41.402563+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "curriculum learning data quality dense retrieval training 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "curriculum learning data quality dense retrieval training 2023 2024"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T04:20:41.402720+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "dense neural code search retrieval 2023 2024 ICSE FSE ASE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "dense neural code search retrieval 2023 2024 ICSE FSE ASE"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T04:20:41.402856+00:00_

Web search results for query: "ContraCode contrastive learning code representation self-supervised 2022 ICLR"

Links: [{"title":"Contrastive Code Representation Learning | OpenReview","url":"https://openreview.net/forum?id=uV7hcsjqM-"},{"title":"CONTRASTIVE CODE REPRESENTATION LEARNING","url":"https://openreview.net/pdf?id=uV7hcsjqM-"},{"title":"GitHub - parasj/contracode: Contrastive Code Representation Learning: functionality-based JavaScript embeddings through self-supervised learning","url":"https://github.com/parasj/contracode"},{"title":"Contrastive Code Representation Learning","url":"https://parasj.github.io/contracode/"},{"title":"(PDF) Contrastive Code Representation Learning","url":"https://www.researchgate.net/publication/342829858_Contrastive_Code_Representation_Learning"},{"title":"[PDF] Contrastive Code Representation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Contrastive-Code-Representation-Learning-Jain-Jain/021bbcefc993c389bad6c1daefd8ff92d0fc2441"},{"title":"Contrastive Code Representation Learning · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/jain2020contrastive/"},{"title":"Contrastive Code Representation Learning","url":"https://aclanthology.org/2021.emnlp-main.482.pdf"},{"title":"Contrastive Code Representation Learning","url":"https://arxiv.org/pdf/2007.04973v3"},{"title":"CONTRASTIVE CODE REPRESENTATION LEARNING","url":"https://www.arxiv.org/pdf/2007.04973v2"}]

Based on the search results, here's what I found about ContraCode:

## ContraCode: Contrastive Code Representation Learning

ContraCode is a self-supervised algorithm for learning task-agnostic semantic representations of programs via contrastive learning. The approach learns to represent programs in a self-supervised manner by using compiler transformations as data augmentations.

### Key Methodology

ContraCode optimizes for a representation that is invariant to semantic-preserving code transformations,
…[truncated 905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T04:20:41.403011+00:00_

Web search results for query: "curriculum learning data quality dense retrieval training 2023 2024"

Links: [{"title":"[PDF] Curriculum Learning for Dense Retrieval Distillation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Curriculum-Learning-for-Dense-Retrieval-Zeng-Zamani/58aa3467505e900f76fb2295f2f94d60c70a65e2"},{"title":"Curriculum Learning with Quality-Driven Data Selection","url":"https://arxiv.org/pdf/2407.00102"},{"title":"Curriculum Learning with Quality-Driven Data Selection","url":"https://www.researchgate.net/publication/381882368_Curriculum_Learning_with_Quality-Driven_Data_Selection"},{"title":"[2204.13679] Curriculum Learning for Dense Retrieval Distillation","url":"https://arxiv.org/abs/2204.13679"},{"title":"[2204.13679v1] Curriculum Learning for Dense Retrieval Distillation","url":"https://arxiv.org/abs/2204.13679v1"},{"title":"Learning More Effective Representations for Dense Retrieval through Deliberate Thinking Before Search","url":"https://arxiv.org/html/2502.12974v1"},{"title":"Dense Retrieval: Principles & Applications","url":"https://www.emergentmind.com/topics/dense-retrieval-dr"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.651/"},{"title":"[2407.00102] Curriculum Learning with Quality-Driven Data Selection","url":"https://arxiv.org/abs/2407.00102"},{"title":"Curriculum Learning for Dense Retrieval Distillation Hansi Zeng","url":"https://arxiv.org/pdf/2204.13679"}]

Based on the search results, here are the key findings on curriculum learning, data quality, and dense retrieval training from 2023-2024:

## Curriculum Learning for Dense Retrieval

A curriculum learning framework called CL-DRD controls the difficulty level of training data by iteratively optimizing the dense retrieval (student) model by increasing the difficulty of knowledge distillation data made available to it. The approach initially provides the stu
…[truncated 1236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T04:20:41.403168+00:00_

Web search results for query: "hard negative mining contrastive learning survey dense retrieval 2023 2024"

Links: [{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3695994"},{"title":"Negative Sampling Techniques in Information Retrieval: A Survey","url":"https://arxiv.org/html/2603.18005"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Negative Sampling Techniques for Dense Passage Retrieval ...","url":"https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/rajapakse-2024-study.pdf"},{"title":"NV-Retriever: Improving text embedding models with effective","url":"https://arxiv.org/pdf/2407.15831"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems","url":"https://arxiv.org/html/2505.18366v1"},{"title":"Positive and Negative Sampling Strategies for Representation Learning in Semantic Search - Sumit's Diary","url":"https://blog.reachsumit.com/posts/2023/03/pairing-for-representation/"},{"title":"A Hard Negatives Mining and Enhancing Method for Multi-Modal Contrastive Learning","url":"https://www.mdpi.com/2079-9292/14/4/767"},{"title":"Towards Expansive and Adaptive Hard Negative Mining: Graph Contrastive Learning via Subspace Preserving | Proceedings of the ACM Web Conference 2024","url":"https://dl.acm.org/doi/10.1145/3589334.3645327"}]

I found several relevant resources on hard negative mining for contrastive learning and dense retrieval from 2023-2024. Here's a summary of what the search revealed:

## Survey and Overview Papers

A recent survey on negative sampling techniques provides systematic analysis of negative sampling for contrastive learning, examining the critical false
…[truncated 1405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T04:20:41.403325+00:00_

Web search results for query: "dense neural code search retrieval 2023 2024 ICSE FSE ASE"

Links: [{"title":"ESEC/FSE 2023 - Research Papers - ESEC/FSE 2023","url":"https://2023.esec-fse.org/track/fse-2023-research-papers"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"A Systematic Literature Review on Large Language Models","url":"https://arxiv.org/pdf/2405.01466"},{"title":"A Survey of Model Architectures in Information Retrieval","url":"https://arxiv.org/html/2502.14822v2"},{"title":"FSE 2024 - Research Papers - FSE 2024","url":"https://2024.esec-fse.org/track/fse-2024-research-papers"},{"title":"ICSE Home Page","url":"https://www.icse-conferences.org/"},{"title":"1 Large Language Models for Software Engineering:","url":"https://nzjohng.github.io/publications/papers/tosem2024_5.pdf"},{"title":"Retrieval-based Neural Source Code Summarization (ICSE 2020 - Technical Papers) - ICSE 2020","url":"https://conf.researchr.org/details/icse-2020/icse-2020-papers/90/Retrieval-based-Neural-Source-Code-Summarization"},{"title":"FSE 2025 - Research Papers - FSE 2025 - conf.researchr.org","url":"https://conf.researchr.org/track/fse-2025/fse-2025-research-papers"}]

Based on the web search results, here are relevant papers on dense neural code search and retrieval from 2023-2024 published at ICSE, FSE, and ASE conferences:

## Code Search and Retrieval Papers (2023-2024)

**Efficient Text-to-Code Retrieval with Cascaded Fast and Slow Transformer Models** (2023), FSE'23, by Gotmare, A., et al.

**GraphSearchNet: Enhancing GNNs via capturing global dependencies for semantic code search** (2023), TSE, by Liu, Shangqing, et al.

**K
…[truncated 973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T04:20:41.403486+00:00_

Web search results for query: "repository level code understanding cross-file context LLM 2024 ICSE FSE"

Links: [{"title":"GitHub - allanj/repo-level-codegen-papers: Repo-Level Code generation papers · GitHub","url":"https://github.com/allanj/repo-level-codegen-papers"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"CodePlan: Repository-level Coding using LLMs and Planning (FSE 2024 - Posters) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-posters/43/CodePlan-Repository-level-Coding-using-LLMs-and-Planning"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"CodePlan: Repository-level Coding using LLMs and Planning (FSE 2024 - Research Papers) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-research-papers/66/CodePlan-Repository-level-Coding-using-LLMs-and-Planning"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf"},{"title":"In Line with Context: Repository-Level Code Generation via Context Inlining","url":"https://arxiv.org/html/2601.00376v1"},{"title":"Repository-level code completion with adaptive segmentation and fused retrieval | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10762-7"},{"title":"CodePlan: Repository-Level Coding using LLMs and ...","url":"https://dl.acm.org/doi/pdf/10.1145/3643757"},{"title":"On Improving Repository-Level Code QA for Large ...","url":"https://aclanthology.org/2024.acl-srw.28.pdf"}]

Based on the search results, here's what I found regarding repository-level code understanding with cross-file context and 
…[truncated 1623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T04:20:41.403675+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ContraBERT contrastive learning code pre-trained models ICSE 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ContraBERT contrastive learning code pre-trained models ICSE 2023"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T04:20:41.403817+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CAPSTONE curriculum sampling dense retrieval EMNLP 2023 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CAPSTONE curriculum sampling dense retrieval EMNLP 2023 authors"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T04:20:41.403946+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RepoFusion repository level code completion cross-file 2024 NeurIPS ICSE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RepoFusion repository level code completion cross-file 2024 NeurIPS ICSE"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T04:20:41.404074+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"effective hard negative mining\" code search TOSEM 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"effective hard negative mining\" code search TOSEM 2024"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T04:20:41.404199+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SynCoBERT authors Wang 2022 venue published journal conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SynCoBERT authors Wang 2022 venue published journal conference"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T04:20:41.404330+00:00_

Web search results for query: "CAPSTONE curriculum sampling dense retrieval EMNLP 2023 authors"

Links: [{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.651/"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion | OpenReview","url":"https://openreview.net/forum?id=Mefvmgkb9G&noteId=TlRvoprgev"},{"title":"[2212.09114] CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://arxiv.org/abs/2212.09114"},{"title":"Curriculum Sampling for Dense Retrieval with Document ...","url":"https://aclanthology.org/2023.emnlp-main.651.pdf"},{"title":"GitHub - microsoft/SimXNS: SimXNS is a research project for information retrieval. This repo contains official implementations by MSRA NLC team.","url":"https://github.com/microsoft/SimXNS"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://openreview.net/pdf?id=Mefvmgkb9G"},{"title":"Main Conference - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_main_conference/"},{"title":"Curriculum Sampling for Dense Retrieval with Document Expansion | Request PDF","url":"https://www.researchgate.net/publication/366423521_Curriculum_Sampling_for_Dense_Retrieval_with_Document_Expansion"},{"title":"Curriculum Sampling For Dense Retrieval With Document ...","url":"https://www.scribd.com/document/835721616/CurriculumSamplingForDenseRetrievalWithDocumentExpansion"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, I found the information about the CAPSTONE paper from EMNLP 2023.

The authors of CAPSTONE are Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, and Nan Duan. The paper is titled "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion" and was publis
…[truncated 231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T04:20:41.404493+00:00_

Web search results for query: "ContraBERT contrastive learning code pre-trained models ICSE 2023"

Links: [{"title":"ContraBERT: Enhancing Code Pre-trained Models via ...","url":"https://www.computer.org/csdl/proceedings-article/icse/2023/570100c476/1OM4OrPPiNy"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning - Singapore Management University","url":"https://smusg.elsevierpure.com/en/publications/contrabert-enhancing-code-pre-trained-models-via-contrastive-lear"},{"title":"[2301.09072] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/abs/2301.09072"},{"title":"ContraBERT: Enhancing Code Pre-Trained Models via Contrastive Learning | Proceedings of the 45th International Conference on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00207"},{"title":"[PDF] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f6572fccea70e5023cc38cb33ebd0f520d7b22e2"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/pdf/2301.09072"},{"title":"About me - Shangqing Liu’s Homepage","url":"https://shangqing-liu.github.io/"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Request PDF","url":"https://www.researchgate.net/publication/372385658_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"},{"title":"Enhancing Code Search Fine-Tuning with Momentum Contrastive Learning and Cross-Modal Matching | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-0014-7_42"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10172726/"}]

Based on the search results, here's what I found about ContraBERT:

## ContraBERT Overview

ContraBERT: Enhancing Code Pr
…[truncated 1494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T04:20:41.404713+00:00_

Web search results for query: ""effective hard negative mining" code search TOSEM 2024"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"Effective Hard Negative Mining for Contrastive Learning-based Code Search | CoLab","url":"https://colab.ws/articles/10.1145/3695994"},{"title":"NV-Retriever: Improving text embedding models with effective","url":"https://arxiv.org/pdf/2407.15831"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems","url":"https://arxiv.org/html/2505.18366v1"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://aclanthology.org/2025.acl-industry.72.pdf"},{"title":"A Novel Refactoring and Semantic Aware Abstract Syntax Tree Differencing Tool","url":"https://users.encs.concordia.ca/~nikolaos/publications/TOSEM_2024.pdf"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Hard Negative Sample Mining for Whole Slide Image Classification | MICCAI 2024 - Open Access","url":"https://papers.miccai.org/miccai-2024/372-Paper3822.html"}]

I found relevant results for your search. The top result is the exact paper you're looking for:

The paper "Effective Hard Negative Mining for Contrastive Learning-Based Code Search" addresses code search, which aims to find the most relevant code snippet in a large codebase based on a given natural language query. An accurate code search engine can increase cod
…[truncated 594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T04:20:41.404949+00:00_

Web search results for query: "SynCoBERT authors Wang 2022 venue published journal conference"

Links: [{"title":"The 2nd Workshop on Recommendation with Generative Models","url":"https://arxiv.org/pdf/2403.04399"},{"title":"Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies - ACL Anthology","url":"https://aclanthology.org/volumes/2022.naacl-main/"},{"title":"Wang research group to present at The ACM Web Conference 2022","url":"https://ischool.illinois.edu/news-events/news/2022/04/wang-research-group-present-acm-web-conference-2022"},{"title":"Yao Wan@Huazhong University of Science and Technology","url":"http://wanyao.me/publication.html"},{"title":"YUYAN WANG (Last updated: Mar 2024)","url":"https://yuyanwang.people.stanford.edu/sites/g/files/sbiybj30946/files/media/file/cv_yuyan_wang_website_0.pdf"},{"title":"Publication | Wayne Wu","url":"https://wywu.github.io/publication/"},{"title":"Jianzong Wang | LLAM | Lab of Large Audio Model","url":"https://largeaudiomodel.com/author/jianzong-wang/"},{"title":"Ge Wang - CSCW '22 - Conference Programs","url":"https://programs.sigchi.org/cscw/2022/authors/86551"},{"title":"Tong Wang","url":"https://scholar.google.com/citations?user=KB6A0esAAAAJ&hl=en"},{"title":"Yin Wang - Conferences","url":"https://sites.google.com/view/yin-wang/conferences"}]

Based on the search results, I found information about SynCoBERT:

SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation was authored by Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, and Xin Jiang, and was published on arXiv in 2021.

The paper appears to have been posted to arXiv rather than published in a traditional conference or journal venue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T04:20:41.405200+00:00_

Web search results for query: "RepoFusion repository level code completion cross-file 2024 NeurIPS ICSE"

Links: [{"title":"Repository-level code completion with adaptive segmentation and fused retrieval | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10762-7"},{"title":"REPOFUSE: Repository-Level Code Completion with Fused Dual Context","url":"https://arxiv.org/pdf/2402.14323"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"GitHub - allanj/repo-level-codegen-papers: Repo-Level Code generation papers · GitHub","url":"https://github.com/allanj/repo-level-codegen-papers"},{"title":"REPOFUSION: TRAINING CODE MODELS TO ...","url":"https://openreview.net/pdf?id=2drC319yHQ"},{"title":"RepoFusion: Training Code Models to Understand Your Repository | OpenReview","url":"https://openreview.net/forum?id=2drC319yHQ"},{"title":"Repoformer: Selective Retrieval for Repository-Level Code Completion","url":"https://arxiv.org/html/2403.10059v2"},{"title":"RepoFusion: Training Code Models to Understand Your Repository | alphaXiv","url":"https://www.alphaxiv.org/abs/2306.10998"},{"title":"RepoFusion: Training Code Models to Understand Your Repository | Request PDF","url":"https://www.researchgate.net/publication/371727808_RepoFusion_Training_Code_Models_to_Understand_Your_Repository"}]

Based on the search results, I found information about RepoFusion and related work on repository-level code completion:

## RepoFusion: Training Code Models to Understand Your Repository

RepoFusion is a framework to train models to incorporate rele
…[truncated 1705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T04:20:41.405451+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SynCoBERT \"ACL 2022\" OR \"EMNLP 2022\" OR \"NAACL 2022\" published proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SynCoBERT \"ACL 2022\" OR \"EMNLP 2022\" OR \"NAACL 2022\" published proceedings"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T04:20:41.405686+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"effective hard negative mining\" code search TOSEM 2024 authors title full"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"effective hard negative mining\" code search TOSEM 2024 authors title full"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T04:20:41.405898+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CrossCodeEval NeurIPS 2023 authors Ding Wang title full"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CrossCodeEval NeurIPS 2023 authors Ding Wang title full"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T04:20:41.406090+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ContraBERT ICSE 2023 Shangqing Liu authors full title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ContraBERT ICSE 2023 Shangqing Liu authors full title"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T04:20:41.406283+00:00_

Web search results for query: ""effective hard negative mining" code search TOSEM 2024 authors title full"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"Effective Hard Negative Mining for Contrastive Learning-based Code Search | CoLab","url":"https://colab.ws/articles/10.1145/3695994"},{"title":"NV-Retriever: Improving text embedding models with effective","url":"https://arxiv.org/pdf/2407.15831"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems","url":"https://arxiv.org/html/2505.18366v1"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://aclanthology.org/2025.acl-industry.72.pdf"},{"title":"A Novel Refactoring and Semantic Aware Abstract Syntax Tree Differencing Tool","url":"https://users.encs.concordia.ca/~nikolaos/publications/TOSEM_2024.pdf"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Hard Negative Sample Mining for Whole Slide Image Classification | MICCAI 2024 - Open Access","url":"https://papers.miccai.org/miccai-2024/372-Paper3822.html"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Effective Hard Negative Mining for Contrastive Learning-Based Code Search"

**Publication:** ACM Transactions on Software Engineering and Methodology (TOSEM)

**Year:** 2024

The paper was published in ACM TOSEM in 2024 (with a metadata date of October 11, 2024). T
…[truncated 531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T04:20:41.406521+00:00_

Web search results for query: "SynCoBERT "ACL 2022" OR "EMNLP 2022" OR "NAACL 2022" published proceedings"

Links: [{"title":"ACL 2022 | 60th Annual Meeting of the Association for Computational Linguistics | Ireland","url":"https://www.2022.aclweb.org/papers"},{"title":"The 2022 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2022/"},{"title":"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing: System Demonstrations - ACL Anthology","url":"https://aclanthology.org/volumes/2022.emnlp-demos/"},{"title":"Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/venues/emnlp/"},{"title":"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing: Industry Track - ACL Anthology","url":"https://aclanthology.org/volumes/2022.emnlp-industry/"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2022 - ACL Anthology","url":"https://aclanthology.org/volumes/2022.findings-emnlp/"},{"title":"EMNLP 2022 The 2022 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2022.emnlp-tutorials.pdf"},{"title":"2022 Annual Conference of the North American Chapter of the Association for Computational Linguistics - NAACL-HLT 2022","url":"https://2022.naacl.org/"},{"title":"Findings of the Association for Computational Linguistics - ACL Anthology","url":"https://aclanthology.org/venues/findings/"},{"title":"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/volumes/2022.emnlp-main/"}]

The search results show links to the ACL Anthology pages for EMNLP 2022 and NAACL 2022 proceedings, but do not contain any specific information about SynCoBERT in these proceedings. The results provide general information about the available proceedings from these conferences but don't menti
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T04:20:41.406777+00:00_

Web search results for query: "CrossCodeEval NeurIPS 2023 authors Ding Wang title full"

Links: [{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Yangruibo+Ding%2C+Zijian+Wang%2C+Wasi+Ahmad%2C+Hantian+Ding%2C+Ming+Tan%2C+Nihal+Jain%2C+Murali+Krishna+Ramanathan%2C+Ramesh+Nallapati%2C+Parminder+Bhatia%2C+Dan+Roth%2C+and+Bing+Xiang.+2023.+CrossCodeEval%3A+A+Diverse+and+Multilingual+Benchmark+for+Cross-File+Code+Completion.+Advances+in+Neural+Information+Processing+Systems+36+%28Dec.+2023%29%2C+46701--46723."},{"title":"GitHub - amazon-science/cceval: CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion (NeurIPS 2023)","url":"https://github.com/amazon-science/cceval"},{"title":"© 2023, Amazon Web Services, Inc. or its affiliates. All rights reserved.","url":"https://neurips.cc/media/neurips-2023/Slides/73423.pdf"},{"title":"CROSSCODEEVAL: A Diverse and Multilingual","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/920f2dced7d32ab2ba2f1970bc306af6-Paper-Datasets_and_Benchmarks.pdf"},{"title":"cceval/README.md at a11b8a6c71cf1fe99881dd22d14871c6f01bd30f · amazon-science/cceval","url":"https://github.com/amazon-science/cceval/blob/a11b8a6c71cf1fe99881dd22d14871c6f01bd30f/README.md"},{"title":"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/920f2dced7d32ab2ba2f1970bc306af6-Abstract-Datasets_and_Benchmarks.html"},{"title":"cceval/README.md at main · amazon-science/cceval","url":"https://github.com/amazon-science/cceval/blob/main/README.md"},{"title":"[Quick Review] CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion","url":"https://liner.com/review/crosscodeeval-a-diverse-and-multilingual-benchmark-for-crossfile-code-completion"},{"title":"CROSSCODEEVAL: A Diverse and Multilingual","url":"https://zijianwang.me/data/NeurIPS_2023__CrossCodeEval.pdf"},{"title":"NeurIPS Poster Cros
…[truncated 709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T04:20:41.407006+00:00_

Web search results for query: "ContraBERT ICSE 2023 Shangqing Liu authors full title"

Links: [{"title":"About me - Shangqing Liu’s Homepage","url":"https://shangqing-liu.github.io/"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning - Singapore Management University","url":"https://smusg.elsevierpure.com/en/publications/contrabert-enhancing-code-pre-trained-models-via-contrastive-lear"},{"title":"[PDF] ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ContraBERT:-Enhancing-Code-Pre-trained-Models-via-Liu-Wu/f6572fccea70e5023cc38cb33ebd0f520d7b22e2"},{"title":"Publications - Shangqing Liu’s Homepage","url":"https://shangqing-liu.github.io/publications/"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | Request PDF","url":"https://www.researchgate.net/publication/372385658_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"},{"title":"shangqing-liu (ShangqingLiu) · GitHub","url":"https://github.com/shangqing-liu"},{"title":"Exploring the Potential of ChatGPT in Automated Code Refinement: An Empirical Study | Proceedings of the IEEE/ACM 46th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3597503.3623306"},{"title":"GitHub - xinyi-hou/LLM4SE_SLR: Large Language Models for Software Engineering: A Systematic Literature Review · GitHub","url":"https://github.com/xinyi-hou/LLM4SE_SLR"},{"title":"(PDF) ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://www.researchgate.net/publication/367359448_ContraBERT_Enhancing_Code_Pre-trained_Models_via_Contrastive_Learning"},{"title":"Shangqing Liu","url":"https://scholar.google.com/citations?hl=en&user=Rl0-phkAAAAJ"}]

Based on the search results, here is the information about the ContraBERT paper:

**Full Title:** ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning

**Au
…[truncated 304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T04:20:41.407235+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"effective hard negative mining\" \"contrastive learning\" code search 2024 authors arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"effective hard negative mining\" \"contrastive learning\" code search 2024 authors arXiv"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T04:20:41.407436+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProGraML ICML 2021 Cummins authors full title \"data flow analysis\" \"compiler optimizations\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProGraML ICML 2021 Cummins authors full title \"data flow analysis\" \"compiler optimizations\""
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-15T04:20:41.407666+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ContraCode \"contrastive code representation learning\" EMNLP 2021 Jain authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ContraCode \"contrastive code representation learning\" EMNLP 2021 Jain authors"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-15T04:20:41.407881+00:00_

Web search results for query: ""effective hard negative mining" "contrastive learning" code search 2024 authors arXiv"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-based Code Search | CoLab","url":"https://colab.ws/articles/10.1145/3695994"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Towards Expansive and Adaptive Hard Negative Mining: Graph Contrastive Learning via Subspace Preserving | Proceedings of the ACM Web Conference 2024","url":"https://dl.acm.org/doi/10.1145/3589334.3645327"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"GitHub - mala-lab/AUGCL: Official code for TNNLS paper \"Affinity Uncertainty-based Hard Negative Mining in Graph Contrastive Learning\"","url":"https://github.com/mala-lab/AUGCL"},{"title":"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning","url":"https://proceedings.mlr.press/v162/xia22b.html"},{"title":"Mining negative samples on contrastive learning via curricular weighting strategy - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S002002552400447X"},{"title":"Dynamic Asymmetric Contrastive Learning with Adaptive Hard Negative Mining for Resume-Job Matching | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3055-7_26"},{"title":"A Hard Negatives Mining and Enhancing Method for Multi-Modal Contrastive Learning","url":"https://www.mdpi.com/2079-9292/14/4/767"}]

Based on the web search results, I found relevant information about the 
…[truncated 1161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T04:20:41.408083+00:00_

Web search results for query: "ProGraML ICML 2021 Cummins authors full title "data flow analysis" "compiler optimizations""

Links: [{"title":"GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub","url":"https://github.com/ChrisCummins/ProGraML"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/programl-a-graph-based-program-representation-for-data-flow-analy"},{"title":"[PDF] ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProGraML:-A-Graph-based-Program-Representation-for-Cummins-Fisches/7843876d45f4c6ac751039b198aade0ee9f94342"},{"title":"dblp: ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations.","url":"https://dblp.org/rec/conf/icml/CumminsFBHOL21.html"},{"title":"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations","url":"https://proceedings.mlr.press/v139/cummins21a.html"},{"title":"ICML 2021 ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations Spotlight","url":"https://icml.cc/virtual/2021/spotlight/8886"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"http://proceedings.mlr.press/v139/cummins21a/cummins21a.pdf"},{"title":"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations - YouTube","url":"https://www.youtube.com/watch?v=cHElgMSOPFs"},{"title":"The Next 700 ML-Enabled Compiler Optimizations | Proceedings of the 33rd ACM SIGPLAN International Conference on Compiler Construction","url":"https://dl.acm.org/doi/10.1145/3640537.3641580"},{"title":"ProGraML: Graph-based Deep Learning for Program Optimization
…[truncated 969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T04:20:41.408247+00:00_

Web search results for query: "ContraCode "contrastive code representation learning" EMNLP 2021 Jain authors"

Links: [{"title":"Contrastive Code Representation Learning - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.482/"},{"title":"[PDF] Contrastive Code Representation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Contrastive-Code-Representation-Learning-Jain-Jain/021bbcefc993c389bad6c1daefd8ff92d0fc2441"},{"title":"Contrastive Code Representation Learning","url":"https://aclanthology.org/2021.emnlp-main.482.pdf"},{"title":"dblp: Contrastive Code Representation Learning.","url":"https://dblp.org/rec/conf/emnlp/0001JZA0S21.html"},{"title":"[2007.04973] Contrastive Code Representation Learning","url":"https://arxiv.org/abs/2007.04973"},{"title":"GitHub - parasj/contracode: Contrastive Code Representation Learning: functionality-based JavaScript embeddings through self-supervised learning","url":"https://github.com/parasj/contracode"},{"title":"[EMNLP 2021] Contrastive Code Representation Learning - YouTube","url":"https://www.youtube.com/watch?v=0deUDO6BqYY"},{"title":"(PDF) Contrastive Code Representation Learning","url":"https://www.academia.edu/87692509/Contrastive_Code_Representation_Learning"},{"title":"Contrastive Code Representation Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200704973J/abstract"},{"title":"Contrastive Code Representation Learning","url":"https://parasj.github.io/contracode/"}]

Based on the search results, here's what I found about ContraCode:

## Paper Details

ContraCode is authored by Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, and Ion Stoica, and was published in the Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP).

## Overview

ContraCode is a contrastive pre-training task that learns code functionality, not form. ContraCode pre-trains a neural network to identify functionally similar variants of a
…[truncated 589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T04:20:41.408401+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoSQA authors Junjie Huang Duyu Tang ACL 2021 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoSQA authors Junjie Huang Duyu Tang ACL 2021 full author list"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T04:20:41.408552+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RocketQA authors Yingqi Qu NAACL 2021 full citation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RocketQA authors Yingqi Qu NAACL 2021 full citation"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-15T04:20:41.408763+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CAPSTONE \"curriculum sampling\" \"dense retrieval\" EMNLP 2023 Xingwei He full authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CAPSTONE \"curriculum sampling\" \"dense retrieval\" EMNLP 2023 Xingwei He full authors"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-15T04:20:41.408906+00:00_

Web search results for query: "CoSQA authors Junjie Huang Duyu Tang ACL 2021 full author list"

Links: [{"title":"GitHub - Jun-jie-Huang/CoCLR: Source Code for ACL-21 main conference paper \"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\".","url":"https://github.com/Jun-jie-Huang/CoCLR"},{"title":"Junjie Huang - Homepage","url":"https://jun-jie-huang.github.io/"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.442/"},{"title":"[PDF] CoSQA: 20,000+ Web Queries for Code Search and Question Answering | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoSQA:-20,000+-Web-Queries-for-Code-Search-and-Huang-Tang/0c21334be0228431d619a180c809b43be0065bdd"},{"title":"ACL-IJCNLP 2021","url":"https://2021.aclweb.org/registration/accept/"},{"title":"Junjie Huang - ACL Anthology","url":"https://aclanthology.org/people/j/junjie-huang/"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/cosqa-20-000-web-queries-for-code-search-and-question-answering/"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering","url":"https://gengo.sotaro.io/2021.acl-long.442"},{"title":"CoSQA: 20,000+ Web Queries for Code Search and Question Answering | Request PDF","url":"https://www.researchgate.net/publication/351926082_CoSQA_20000_Web_Queries_for_Code_Search_and_Question_Answering"},{"title":"WhiteningBERT: An Easy Unsupervised Sentence Embedding Approach - ACL Anthology","url":"https://aclanthology.org/2021.findings-emnlp.23/"}]

Based on the search results, the full author list for the CoSQA paper published at ACL 2021 is: Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, and Nan Duan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T04:20:41.409052+00:00_

Web search results for query: "CAPSTONE "curriculum sampling" "dense retrieval" EMNLP 2023 Xingwei He full authors"

Links: [{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.651/"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion | OpenReview","url":"https://openreview.net/forum?id=Mefvmgkb9G&noteId=TlRvoprgev"},{"title":"[2212.09114] CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://arxiv.org/abs/2212.09114"},{"title":"GitHub - microsoft/SimXNS: SimXNS is a research project for information retrieval. This repo contains official implementations by MSRA NLC team.","url":"https://github.com/microsoft/SimXNS"},{"title":"dblp: Anlei Dong","url":"https://dblp.org/pid/28/6385.html"},{"title":"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion","url":"https://openreview.net/pdf?id=Mefvmgkb9G"},{"title":"Curriculum Sampling for Dense Retrieval with Document ...","url":"https://aclanthology.org/2023.emnlp-main.651.pdf"},{"title":"Paper Digest: EMNLP-2023 Highlights (Full List)","url":"https://www.paperdigest.org/data/emnlp-2023-full.html"},{"title":"dblp: Jian Jiao 0007","url":"https://dblp.org/pid/29/265-7.html"},{"title":"Main Conference - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_main_conference/"}]

Based on the search results, I found the full author information for the CAPSTONE paper at EMNLP 2023:

The full authors are: Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Yiu, and Nan Duan.

The paper is titled "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion" and was published in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 10531–10541, Singapore.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-15T04:20:41.409221+00:00_

Web search results for query: "RocketQA authors Yingqi Qu NAACL 2021 full citation"

Links: [{"title":"RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.466/"},{"title":"RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering | Request PDF","url":"https://www.researchgate.net/publication/352364344_RocketQA_An_Optimized_Training_Approach_to_Dense_Passage_Retrieval_for_Open-Domain_Question_Answering"},{"title":"dblp: RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering.","url":"https://dblp.org/rec/conf/naacl/QuDLLRZDWW21.html"},{"title":"GitHub - PaddlePaddle/RocketQA: 🚀 RocketQA, dense retrieval for information retrieval and question answering, including both Chinese and English state-of-the-art models.","url":"https://github.com/PaddlePaddle/RocketQA"},{"title":"RocketQA/research/RocketQA_NAACL2021 at main · PaddlePaddle/RocketQA","url":"https://github.com/PaddlePaddle/RocketQA/tree/main/research/RocketQA_NAACL2021"},{"title":"Research/NLP/NAACL2021-RocketQA at master · PaddlePaddle/Research","url":"https://github.com/PaddlePaddle/Research/tree/master/NLP/NAACL2021-RocketQA"},{"title":"[PDF] RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RocketQA:-An-Optimized-Training-Approach-to-Dense-Qu-Ding/f2c1ab4e850ad89bd6b6b9908e12a4151d152070"},{"title":"Google znalac","url":"https://scholar.google.com/scholar?q=Yingqi+Qu%2C+Yuchen+Ding%2C+Jing+Liu%2C+Kai+Liu%2C+Ruiyang+Ren%2C+Xin+Zhao%2C+Daxiang+Dong%2C+Hua+Wu%2C+and+Haifeng+Wang.+2021.+RocketQA%3A+An+Optimized+Training+Approach+to+Dense+Passage+Retrieval+for+Open-Domain+Question+Answering.+NAACL."},{"title":"DL-NLP-Readings/Bibtex/RocketQA - An Optimized Training Approach to Dense Passage Re
…[truncated 1746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T04:20:41.409449+00:00_

Here is the verified list, grouped by area. All papers were confirmed via web search with ACL Anthology, DBLP, proceedings pages, or arXiv records.

---

**Area 1: Contrastive Learning for Code**

**1. ContraCode: Contrastive Code Representation Learning**
- Authors: Paras Jain, Ajay Jain, Tianjun Zhang, et al. (Pieter Abbeel, Joseph Gonzalez, Ion Stoica)
- Venue/Year: EMNLP 2021
- Relevance: Directly precedent work using compiler-based semantic-preserving augmentations for contrastive code pre-training; contrasting functionally equivalent programs is the code-specific analog of structure-guided hard negative construction.

**2. SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation**
- Authors: Xin Wang, Yasheng Wang, Fei Mi, et al.
- Venue/Year: arXiv 2021 (widely cited preprint; no confirmed top-venue proceedings publication found — treat as arXiv cite)
- Relevance: Uses AST edges and multi-modal contrastive objectives over code/comment/AST triples, making it the closest prior work to structure-aware contrastive learning for code retrieval.

**3. ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning**
- Authors: Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu
- Venue/Year: ICSE 2023
- Relevance: Applies contrastive learning with nine program-level augmentation operators to improve code pre-trained model robustness; directly related to contrastive objectives for code representation.

---

**Area 2: Hard Negative Mining in Dense Retrieval**

**4. RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering**
- Authors: Yingqi Qu, Yuchen Ding, Jing Liu, et al. (Kai Liu, Ruiyang Ren, Wayne Xin Zhao, Daxiang Dong, Hua Wu, Haifeng Wang)
- Venue/Year: NAACL 2021
- Relevance: Introduces denoised hard negative sampling (using a cross-encoder to filter false negatives) as a core training technique for dense retrieval; the structural-denoising intuition transfers directly t
…[truncated 4058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "Agent",
  "elapsed_ms": 9
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T04:20:41.409686+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "max_chars": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "memory.md",
    "max_chars": "500"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T04:20:41.409852+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | \\n\\n... [截断: 省略 12463 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 12963, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-15T04:20:41.410000+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T04:20:41.410232+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo
…[truncated 11498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-15T04:20:41.410472+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "content": "# Inference-Time Graph Methods 文献对比\n\n## 对比表\n\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\n\n## Discussion 要点\n\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\n\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\n\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\n\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\n\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\n\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\n\n## Related Work 段落草稿 (~200 words)\n\n**Graph-Based Methods for Code Understanding.**\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\n\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\n\n---\n\n## 参考文献（全部已验证 2026-05-14）\n\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\n- CodeRAG: arXiv:2504.10046, 2025\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\")\n- CodeGRAG: arXiv:2405.02355, 2024\n\n---\n\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\n\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\n\n**分歧 pattern**：\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\n\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\n\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) hard_negative_ratio=0.5 平衡设计。K 敏感性列为 limitation/future work。\n\n---\n\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\n\n**两层重叠率数据（注意区分）**：\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\n\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\n|------|-------------------|----------------|------------------|\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\n\n**核心修正**：之前基于 87% 预测\"Phase 2 中 BM25 R@1 很可能接近 embedding\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\n\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\n\n---\n\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\n\n**发现者**：Reviewer\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\n\n**差异**：\n\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\n三步法：\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\n\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\n两步法：\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\n\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\n\n### 差异总结\n\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\n|------|------------------------|--------------------------|\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\n\n### 对齐建议\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\n\n---\n\n## 运维经验 (2026-05-14)\n\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\n\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\n\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\n\n---\n\n## 关键决策记录\n\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\n\n---\n\n## Related Work Gap Analysis (2026-05-15)\n\n### 当前 Citation 统计 (literature_map.yaml)\n\n| Category | Count | 代表论文 |\n|----------|-------|---------|\n| code_retrieval_bug_fixing | 8 | SWE-bench, SWE-agent, AutoCodeRover, Agentless, SWE-smith, RepoBench, SweRank, SWE-Fixer |\n| hard_negative_mining | 6 | DPR, ANCE, SimCLR, SBERT, CL-DRD, CoCoHaNeRe |\n| contrastive_code_learning | 3 | ContraCode, CodeRetriever, Ding et al. (ACL 2022) |\n| program_analysis_for_ml | 6 | CodeQL (tool), code2vec, code2seq, FA-AST, GraphCodeBERT, ARISE |\n| code_embeddings_search | 9 | CodeSearchNet, CodeBERT, UniXcoder, StarCoder, Code Llama, Qwen2.5-Coder, DeepSeek-Coder, RepoFusion, BM25 |\n| graph_guided_inference | 5 | LocAgent, CodexGraph, RANGER, RepoGraph, GraphCoder |\n| infrastructure | 2 | FAISS, Tree-sitter |\n| **Total (literature_map)** | **39** | 含 2 个软件工具引用 |\n\n另有 memory.md 中 2 篇未入 literature_map：CodeRAG (arXiv 2025), CodeGRAG (arXiv 2024)。\n\n**已超过 25+ 目标**（39-41 篇），核心问题是覆盖均匀性。\n\n### 缺口识别 + 推荐论文\n\n#### Gap 1: Contrastive Learning for Code（当前仅 3 篇，最薄弱）\n\n**推荐添加：**\n\n1. **ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning**\n   - Authors: Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\n   - Venue: ICSE 2023\n   - 为什么引：用 9 种程序级变换做对比学习增强代码预训练模型鲁棒性，是 code contrastive learning 的直接前序工作。StructFuse 的结构信号与其 augmentation 策略形成方法论对比。\n   - ✅ WebSearch 确认: ACM DL https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00207\n\n2. **SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation**\n   - Authors: Xin Wang, Yasheng Wang, Fei Mi, et al.\n   - Venue: arXiv 2021 (arXiv:2108.04556, 广泛引用)\n   - 为什么引：用 AST 边 + 多模态（code/comment/AST）对比目标，是最接近\"结构感知对比学习\"的前序工作。与 StructFuse 用 data-flow 做负样本挖掘形成直接技术路线对比。\n   - ✅ WebSearch 确认: arXiv https://arxiv.org/abs/2108.04556\n\n#### Gap 2: Hard Negative Mining — 通用 ML 方法论（需补充 dense retrieval 经典方法）\n\n**推荐添加：**\n\n3. **RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering**\n   - Authors: Yingqi Qu, Yuchen Ding, Jing Liu, et al.\n   - Venue: NAACL 2021\n   - 为什么引：提出 denoised hard negative sampling（用 cross-encoder 过滤 false negatives），其\"去噪\"直觉与 StructFuse 用 data-flow 结构过滤假阴性负样本的思路高度对应。\n   - ✅ WebSearch 确认: ACL Anthology https://aclanthology.org/2021.naacl-main.466/\n\n4. **CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion**\n   - Authors: Xingwei He, Yeyun Gong, A-Long Jin, et al.\n   - Venue: EMNLP 2023\n   - 为什么引：渐进难度调度训练样本用于密集检索，支持 StructFuse 中 hard_negative_ratio 从简到难的课程学习式解读。与已有的 CL-DRD (SIGIR 2022) 互补。\n   - ✅ WebSearch 确认: ACL Anthology https://aclanthology.org/2023.emnlp-main.651/\n\n#### Gap 3: Code Search Benchmarks（缺标准评测集引用）\n\n**推荐添加：**\n\n5. **CoSQA: 20,000+ Web Queries for Code Search and Question Answering**\n   - Authors: Junjie Huang, Duyu Tang, Linjun Shou, et al.\n   - Venue: ACL 2021\n   - 为什么引：标准代码搜索 benchmark + CoCLR 对比学习方法，是 code retrieval problem formulation 的重要引用。\n   - ✅ WebSearch 确认: ACL Anthology https://aclanthology.org/2021.acl-long.442/\n\n#### Gap 4: Repository-level Code Understanding（当前无专门的 cross-file benchmark 引用）\n\n**推荐添加：**\n\n6. **CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion**\n   - Authors: Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, et al.\n   - Venue: NeurIPS 2023 (Datasets & Benchmarks)\n   - 为什么引：建立了 cross-file 结构理解的必要性，直接论证 call-graph 级别上下文对 repo-scale 代码检索的重要性。\n   - ✅ WebSearch 确认: NeurIPS Proceedings 2023\n\n#### Gap 5: Program Analysis + Deep Learning（缺程序图 ML 奠基工作）\n\n**推荐添加：**\n\n7. **ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations**\n   - Authors: Chris Cummins, Zacharias Fisches, Tal Ben-Nun, et al.\n   - Venue: ICML 2021\n   - 为什么引：将程序表示为 control/data/call-flow 三合一图用于 ML，是\"data-flow 信号用于机器学习\"的奠基性正当化引用。与 GraphCodeBERT (ICLR 2021) 互补——GraphCodeBERT 在 NLP 预训练中用 data-flow，ProGraML 在编译优化中用。\n   - ✅ WebSearch 确认: ICML 2021 Proceedings https://proceedings.mlr.press/v139/cummins21a.html\n\n### 已充分覆盖的领域\n\n- **SWE-bench 生态** (8 篇)：SWE-bench, SWE-agent, Agentless, AutoCodeRover, SWE-smith, RepoBench, SweRank, SWE-Fixer — 覆盖 benchmark + 主流 agent/retrieval 方法 ✓\n- **Code embeddings / LLM** (9 篇)：CodeBERT → UniXcoder → StarCoder/Qwen2.5-Coder/DeepSeek-Coder 演进链完整 ✓\n- **Inference-time graph methods** (5+3=8 篇)：覆盖所有主要 2024-2026 graph-guided code 方法 ✓\n- **Infrastructure** (2)：FAISS, Tree-sitter — 作为工具引用足够 ✓\n\n### 达到目标的路径\n\n| 状态 | Count |\n|------|-------|\n| literature_map.yaml 当前 | 39 |\n| memory.md 额外 (CodeRAG, CodeGRAG) | +2 |\n| Gap 1: contrastive_code_learning (+ContraBERT, +SynCoBERT) | +2 |\n| Gap 2: hard_negative_mining (+RocketQA, +CAPSTONE) | +2 |\n| Gap 3: code_search_benchmarks (+CoSQA) | +1 |\n| Gap 4: repo-level understanding (+CrossCodeEval) | +1 |\n| Gap 5: program_analysis_for_ml (+ProGraML) | +1 |\n| **添加后总计** | **48** |\n\n添加 7 篇后达到 48 篇，远超 25+ 目标。每个核心领域至少 5 篇，覆盖均匀。\n\n### 优先级\n\n1. **必须加** (reviewer 会注意到缺失): RocketQA, ContraBERT, ProGraML, CrossCodeEval\n2. **强烈建议** (加厚薄弱领域): SynCoBERT, CAPSTONE\n3. **可选** (锦上添花): CoSQA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "memory.md",
    "content": "# Inference-Time Graph Methods 文献对比\n\n## 对比表\n\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\n\n## Discussion 要点\n\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\n\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\n\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\n\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\n\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\n\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\n\n## Related Work 段落草稿 (~200 words)\n\n**Graph-Based Methods for Code Understanding.**\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\n\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\n\n---\n\n## 参考文献（全部已验证 2026-05-14）\n\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\n- CodeRAG: arXiv:2504.10046, 2025\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\")\n- CodeGRAG: arXiv:2405.02355, 2024\n\n---\n\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\n\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\n\n**分歧 pattern**：\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\n\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\n\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) hard_negative_ratio=0.5 平衡设计。K 敏感性列为 limitation/future work。\n\n---\n\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\n\n**两层重叠率数据（注意区分）**：\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\n\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\n|------|-------------------|----------------|------------------|\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\n\n**核心修正**：之前基于 87% 预测\"Phase 2 中 BM25 R@1 很可能接近 embedding\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\n\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\n\n---\n\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\n\n**发现者**：Reviewer\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\n\n**差异**：\n\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\n三步法：\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\n\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\n两步法：\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\n\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\n\n### 差异总结\n\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\n|------|------------------------|--------------------------|\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\n\n### 对齐建议\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\n\n---\n\n## 运维经验 (2026-05-14)\n\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\n\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\n\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\n\n---\n\n## 关键决策记录\n\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\n\n---\n\n## Related Work Gap Analysis (2026-05-15)\n\n### 当前 Citation 统计 (literature_map.yaml)\n\n| Category | Count | 代表论文 |\n|----------|-------|---------|\n| code_retrieval_bug_fixing | 8 | SWE-bench, SWE-agent, AutoCodeRover, Agentless, SWE-smith, RepoBench, SweRank, SWE-Fixer |\n| hard_negative_mining | 6 | DPR, ANCE, SimCLR, SBERT, CL-DRD, CoCoHaNeRe |\n| contrastive_code_learning | 3 | ContraCode, CodeRetriever, Ding et al. (ACL 2022) |\n| program_analysis_for_ml | 6 | CodeQL (tool), code2vec, code2seq, FA-AST, GraphCodeBERT, ARISE |\n| code_embeddings_search | 9 | CodeSearchNet, CodeBERT, UniXcoder, StarCoder, Code Llama, Qwen2.5-Coder, DeepSeek-Coder, RepoFusion, BM25 |\n| graph_guided_inference | 5 | LocAgent, CodexGraph, RANGER, RepoGraph, GraphCoder |\n| infrastructure | 2 | FAISS, Tree-sitter |\n| **Total (literature_map)** | **39** | 含 2 个软件工具引用 |\n\n另有 memory.md 中 2 篇未入 literature_map：CodeRAG (arXiv 2025), CodeGRAG (arXiv 2024)。\n\n**已超过 25+ 目标**（39-41 篇），核心问题是覆盖均匀性。\n\n### 缺口识别 + 推荐论文\n\n#### Gap 1: Contrastive Learning for Code（当前仅 3 篇，最薄弱）\n\n**推荐添加：**\n\n1. **ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning**\n   - Authors: Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\n   - Venue: ICSE 2023\n   - 为什么引：用 9 种程序级变换做对比学习增强代码预训练模型鲁棒性，是 code contrastive learning 的直接前序工作。StructFuse 的结构信号与其 augmentation 策略形成方法论对比。\n   - ✅ WebSearch 确认: ACM DL https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00207\n\n2. **SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation**\n   - Authors: Xin Wang, Yasheng Wang, Fei Mi, et al.\n   - Venue: arXiv 2021 (arXiv:2108.04556, 广泛引用)\n   - 为什么引：用 AST 边 + 多模态（code/comment/AST）对比目标，是最接近\"结构感知对比学习\"的前序工作。与 StructFuse 用 data-flow 做负样本挖掘形成直接技术路线对比。\n   - ✅ WebSearch 确认: arXiv https://arxiv.org/abs/2108.04556\n\n#### Gap 2: Hard Negative Mining — 通用 ML 方法论（需补充 dense retrieval 经典方法）\n\n**推荐添加：**\n\n3. **RocketQA: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering**\n   - Authors: Yingqi Qu, Yuchen Ding, Jing Liu, et al.\n   - Venue: NAACL 2021\n   - 为什么引：提出 denoised hard negative sampling（用 cross-encoder 过滤 false negatives），其\"去噪\"直觉与 StructFuse 用 data-flow 结构过滤假阴性负样本的思路高度对应。\n   - ✅ WebSearch 确认: ACL Anthology https://aclanthology.org/2021.naacl-main.466/\n\n4. **CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion**\n   - Authors: Xingwei He, Yeyun Gong, A-Long Jin, et al.\n   - Venue: EMNLP 2023\n   - 为什么引：渐进难度调度训练样本用于密集检索，支持 StructFuse 中 hard_negative_ratio 从简到难的课程学习式解读。与已有的 CL-DRD (SIGIR 2022) 互补。\n   - ✅ WebSearch 确认: ACL Anthology https://aclanthology.org/2023.emnlp-main.651/\n\n#### Gap 3: Code Search Benchmarks（缺标准评测集引用）\n\n**推荐添加：**\n\n5. **CoSQA: 20,000+ Web Queries for Code Search and Question Answering**\n   - Authors: Junjie Huang, Duyu Tang, Linjun Shou, et al.\n   - Venue: ACL 2021\n   - 为什么引：标准代码搜索 benchmark + CoCLR 对比学习方法，是 code retrieval problem formulation 的重要引用。\n   - ✅ WebSearch 确认: ACL Anthology https://aclanthology.org/2021.acl-long.442/\n\n#### Gap 4: Repository-level Code Understanding（当前无专门的 cross-file benchmark 引用）\n\n**推荐添加：**\n\n6. **CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion**\n   - Authors: Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, et al.\n   - Venue: NeurIPS 2023 (Datasets & Benchmarks)\n   - 为什么引：建立了 cross-file 结构理解的必要性，直接论证 call-graph 级别上下文对 repo-scale 代码检索的重要性。\n   - ✅ WebSearch 确认: NeurIPS Proceedings 2023\n\n#### Gap 5: Program Analysis + Deep Learning（缺程序图 ML 奠基工作）\n\n**推荐添加：**\n\n7. **ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations**\n   - Authors: Chris Cummins, Zacharias Fisches, Tal Ben-Nun, et al.\n   - Venue: ICML 2021\n   - 为什么引：将程序表示为 control/data/call-flow 三合一图用于 ML，是\"data-flow 信号用于机器学习\"的奠基性正当化引用。与 GraphCodeBERT (ICLR 2021) 互补——GraphCodeBERT 在 NLP 预训练中用 data-flow，ProGraML 在编译优化中用。\n   - ✅ WebSearch 确认: ICML 2021 Proceedings https://proceedings.mlr.press/v139/cummins21a.html\n\n### 已充分覆盖的领域\n\n- **SWE-bench 生态** (8 篇)：SWE-bench, SWE-agent, Agentless, AutoCodeRover, SWE-smith, RepoBench, SweRank, SWE-Fixer — 覆盖 benchmark + 主流 agent/retrieval 方法 ✓\n- **Code embeddings / LLM** (9 篇)：CodeBERT → UniXcoder → StarCoder/Qwen2.5-Coder/DeepSeek-Coder 演进链完整 ✓\n- **Inference-time graph methods** (5+3=8 篇)：覆盖所有主要 2024-2026 graph-guided code 方法 ✓\n- **Infrastructure** (2)：FAISS, Tree-sitter — 作为工具引用足够 ✓\n\n### 达到目标的路径\n\n| 状态 | Count |\n|------|-------|\n| literature_map.yaml 当前 | 39 |\n| memory.md 额外 (CodeRAG, CodeGRAG) | +2 |\n| Gap 1: contrastive_code_learning (+ContraBERT, +SynCoBERT) | +2 |\n| Gap 2: hard_negative_mining (+RocketQA, +CAPSTONE) | +2 |\n| Gap 3: code_search_benchmarks (+CoSQA) | +1 |\n| Gap 4: repo-level understanding (+CrossCodeEval) | +1 |\n| Gap 5: program_analysis_for_ml (+ProGraML) | +1 |\n| **添加后总计** | **48** |\n\n添加 7 篇后达到 48 篇，远超 25+ 目标。每个核心领域至少 5 篇，覆盖均匀。\n\n### 优先级\n\n1. **必须加** (reviewer 会注意到缺失): RocketQA, ContraBERT, ProGraML, CrossCodeEval\n2. **强烈建议** (加厚薄弱领域): SynCoBERT, CAPSTONE\n3. **可选** (锦上添花): CoSQA"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T04:20:41.410839+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-gap-analysis_20260515T041514",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-15T04:20:41.411017+00:00_

Gap 分析已写入 memory.md。

**摘要**：

- 当前 literature_map.yaml 39 篇，已超 25+ 目标，但覆盖不均
- 最薄弱：contrastive learning for code（仅 3 篇）、通用 hard negative mining 方法论
- 推荐添加 7 篇（全部 WebSearch 验证真实存在）：
  - **必须加**：RocketQA (NAACL 2021)、ContraBERT (ICSE 2023)、ProGraML (ICML 2021)、CrossCodeEval (NeurIPS 2023)
  - **强烈建议**：SynCoBERT (arXiv 2021)、CAPSTONE (EMNLP 2023)
  - **可选**：CoSQA (ACL 2021)
- 添加后总计 48 篇，各领域均 ≥5 篇

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_related-work-gap-analysis_20260515T041514"
}
```

</details>

---
