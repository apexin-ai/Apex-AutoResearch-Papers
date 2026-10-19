# write related work expand

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 85
- **Recorded user turns:** 0
- **Tool calls:** 42
- **Original source:** `logs/chats/worker_write_related-work-expand_20260515T031325.jsonl`
- **Structured JSON:** [`a5c5ba1e427f60e91689.json`](../../sessions/a5/a5c5ba1e427f60e91689.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

85 recorded events

### Tool call

_source line 1 · 2026-05-15T03:22:30.705931+00:00_

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
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T03:22:30.706342+00:00_

1	# 2. Related Work
2	
3	## 2.1 Code Retrieval Methods
4	
5	Repo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.
6	
7	A parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization—though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they 
…[truncated 5473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T03:22:30.706538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T03:22:30.706752+00:00_

1	# 5. Discussion
2	
3	## 5.1 Relationship to Inference-Time Graph Methods
4	
5	A growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.
6	CodexGraph (Liu et al., NAACL 2025) materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides line-level code graph navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) and ARISE (Seddik & Fard, 2026) come closest to our work in incorporating data-flow information, but both are limited to intra-procedural scope.
7	
8	Table 5 summarizes the key dimensions of comparison. We highlight two axes along which StructFuse occupies a distinct position:
9	
10	**When structural information enters the pipeline.** Inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity and—for agent-based systems—requiring multiple LLM calls per query. StructFuse amortizes all graph computation to training time: CodeQL extraction costs approximately 8.9 seconds per instance (~110 CPU-hours for 44K instances; Table 4), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead. For latency-sensitive, high-throughput retrieval scenarios, this cost model is substantially more favorable.
11	
12	**Depth of data-flow analysis.** Most inference-time graph methods use structural relations (call graphs, class hierarchies, import dependencies). GraphCoder incorporates control-flow and data-dependence graphs, and ARISE exposes statement-level def-use edges, but both operate within single procedures. StructFuse leverages CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths—e.g., a 
…[truncated 7259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T03:22:30.706922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T03:22:30.707047+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T03:22:30.707178+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T03:22:30.707294+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T03:22:30.707405+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T03:22:30.707516+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T03:22:30.707686+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify CodeBERT, UniXcoder, CodeSage papers",
  "prompt": "I need to verify the exact publication details of several papers for a bibliography. Use WebSearch to find the correct arXiv IDs, conference venues, and author lists for each. Report the full citation info (authors, title, venue, year, arXiv ID if available).\n\n1. CodeBERT (Feng et al., 2020) — code-NL pre-training with contrastive learning\n2. UniXcoder (Guo et al., 2022) — unified cross-modal code representation\n3. CodeSage (Zhang et al., 2024) — code representation learning (likely from Salesforce)\n4. SCodeR or CodeContrastNet — recent contrastive learning for code search (2023-2024)\n5. StarCoder2 (Lozhkov et al., 2024) — the model we use as encoder\n\nFor each, I need: full author list (at least first 3 + et al.), exact title, venue (conference/journal or arXiv), year, and arXiv ID.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify CodeBERT, UniXcoder, CodeSage papers",
    "prompt": "I need to verify the exact publication details of several papers for a bibliography. Use WebSearch to find the correct arXiv IDs, conference venues, and author lists for each. Report the full citation info (authors, title, venue, year, arXiv ID if available).\n\n1. CodeBERT (Feng et al., 2020) — code-NL pre-training with contrastive learning\n2. UniXcoder (Guo et al., 2022) — unified cross-modal code representation\n3. CodeSage (Zhang et al., 2024) — code representation learning (likely from Salesforce)\n4. SCodeR or CodeContrastNet — recent contrastive learning for code search (2023-2024)\n5. StarCoder2 (Lozhkov et al., 2024) — the model we use as encoder\n\nFor each, I need: full author list (at least first 3 + et al.), exact title, venue (conference/journal or arXiv), year, and arXiv ID.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T03:22:30.707845+00:00_

Async agent launched successfully.
agentId: a25497bf4e929bce1 (internal ID - do not mention to user. Use SendMessage with to: 'a25497bf4e929bce1' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/8c3dfb9b-6330-40ad-a7df-88d6f823d16e/tasks/a25497bf4e929bce1.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T03:22:30.707996+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify hard negative mining papers",
  "prompt": "I need to verify the exact publication details of several papers on hard negative mining for a bibliography. Use WebSearch to find the correct arXiv IDs, conference venues, and author lists for each. Report the full citation info.\n\n1. STAR (Zhan et al., 2021) — hard negative mining for dense retrieval, \"Learning to Retrieve: How to Train a Dense Retrieval Model Effectively and Efficiently\"\n2. RocketQA (Qu et al., 2021) — hard negative mining with cross-encoder for dense passage retrieval\n3. Qwen2.5-Coder (Hui et al., 2024) — the code LLM model, need correct citation\n\nFor each, I need: full author list (at least first 3 + et al.), exact title, venue (conference/journal or arXiv), year, and arXiv ID.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify hard negative mining papers",
    "prompt": "I need to verify the exact publication details of several papers on hard negative mining for a bibliography. Use WebSearch to find the correct arXiv IDs, conference venues, and author lists for each. Report the full citation info.\n\n1. STAR (Zhan et al., 2021) — hard negative mining for dense retrieval, \"Learning to Retrieve: How to Train a Dense Retrieval Model Effectively and Efficiently\"\n2. RocketQA (Qu et al., 2021) — hard negative mining with cross-encoder for dense passage retrieval\n3. Qwen2.5-Coder (Hui et al., 2024) — the code LLM model, need correct citation\n\nFor each, I need: full author list (at least first 3 + et al.), exact title, venue (conference/journal or arXiv), year, and arXiv ID.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T03:22:30.708144+00:00_

Async agent launched successfully.
agentId: aa2482f77491fcc56 (internal ID - do not mention to user. Use SendMessage with to: 'aa2482f77491fcc56' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/8c3dfb9b-6330-40ad-a7df-88d6f823d16e/tasks/aa2482f77491fcc56.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T03:22:30.708324+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify code structure analysis papers",
  "prompt": "I need to verify the exact publication details of several papers related to code structure analysis for a bibliography. Use WebSearch to find the correct details.\n\n1. CodeQL — find the canonical academic paper or reference for CodeQL (GitHub's static analysis engine). It may be published under the name \"QL\" or \"Semmle QL\" by Pavel Avgustinov et al., or there may be a more recent reference.\n2. Tree-sitter — find if there is an academic paper about tree-sitter for code parsing, or identify the best academic work that uses tree-sitter for code structure in ML/NLP context\n3. Program dependence graph — find the classic paper by Ferrante, Ottenstein, Warren (1987) on \"The program dependence graph and its use in optimization\"\n4. Joern — the open source code analysis tool, find its academic paper (Yamaguchi et al.)\n5. InferCode (Bui et al., 2021) — learning code representations from AST subtrees\n\nFor each, I need: full author list, exact title, venue, year, and any identifier (arXiv, DOI).",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify code structure analysis papers",
    "prompt": "I need to verify the exact publication details of several papers related to code structure analysis for a bibliography. Use WebSearch to find the correct details.\n\n1. CodeQL — find the canonical academic paper or reference for CodeQL (GitHub's static analysis engine). It may be published under the name \"QL\" or \"Semmle QL\" by Pavel Avgustinov et al., or there may be a more recent reference.\n2. Tree-sitter — find if there is an academic paper about tree-sitter for code parsing, or identify the best academic work that uses tree-sitter for code structure in ML/NLP context\n3. Program dependence graph — find the classic paper by Ferrante, Ottenstein, Warren (1987) on \"The program dependence graph and its use in optimization\"\n4. Joern — the open source code analysis tool, find its academic paper (Yamaguchi et al.)\n5. InferCode (Bui et al., 2021) — learning code representations from AST subtrees\n\nFor each, I need: full author list, exact title, venue, year, and any identifier (arXiv, DOI).",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T03:22:30.708477+00:00_

Async agent launched successfully.
agentId: a6f54155fec009ea1 (internal ID - do not mention to user. Use SendMessage with to: 'a6f54155fec009ea1' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/8c3dfb9b-6330-40ad-a7df-88d6f823d16e/tasks/a6f54155fec009ea1.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T03:22:30.708654+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T03:22:30.708782+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T03:22:30.708913+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read existing files and catalog current citations', 'status': 'completed', 'activeForm': 'Reading existing files and cataloging current citations'}, {'content': 'Verify new paper citations via WebSearch (3 agents running)', 'status': 'in_progress', 'activeForm': 'Verifying new paper citations via WebSearch'}, {'content': 'Write expanded related_work_v1.md with 25+ citations', 'status': 'pending', 'activeForm': 'Writing expanded related_work_v1.md'}, {'content': 'Create references.bib with all citations', 'status': 'pending', 'activeForm': 'Creating references.bib'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read existing files and catalog current citations', 'status': 'completed', 'activeForm': 'Reading existing files and cataloging current citations'}, {'content': 'Verify new paper citations via WebSearch (3 agents running)', 'status': 'in_progress', 'activeForm': 'Verifying new paper citations via WebSearch'}, {'content': 'Write expanded related_work_v1.md with 25+ citations', 'status': 'pending', 'activeForm': 'Writing expanded related_work_v1.md'}, {'content': 'Create references.bib with all citations', 'status': 'pending', 'activeForm': 'Creating references.bib'}]"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T03:22:30.709049+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T03:22:30.709482+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read existing files and catalog current citations', 'status': 'completed', 'activeForm': 'Reading existing files and cataloging current citations'}, {'content': 'Verify new paper citations via WebSearch (3 agents running)', 'status': 'completed', 'activeForm': 'Verifying new paper citations via WebSearch'}, {'content': 'Verify remaining existing citations', 'status': 'in_progress', 'activeForm': 'Verifying remaining existing citations'}, {'content': 'Write expanded related_work_v1.md with 25+ citations', 'status': 'pending', 'activeForm': 'Writing expanded related_work_v1.md'}, {'content': 'Create references.bib with all citations', 'status': 'pending', 'activeForm': 'Creating references.bib'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read existing files and catalog current citations', 'status': 'completed', 'activeForm': 'Reading existing files and cataloging current citations'}, {'content': 'Verify new paper citations via WebSearch (3 agents running)', 'status': 'completed', 'activeForm': 'Verifying new paper citations via WebSearch'}, {'content': 'Verify remaining existing citations', 'status': 'in_progress', 'activeForm': 'Verifying remaining existing citations'}, {'content': 'Write expanded related_work_v1.md with 25+ citations', 'status': 'pending', 'activeForm': 'Writing expanded related_work_v1.md'}, {'content': 'Create references.bib with all citations', 'status': 'pending', 'activeForm': 'Creating references.bib'}]"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T03:22:30.709667+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T03:22:30.709808+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify remaining paper citations",
  "prompt": "I need to verify the exact publication details for several papers. Use WebSearch for each. Report: authors, title, venue, year, arXiv ID.\n\n1. SweRank (Reddy et al., 2025) — retrieve-and-rerank pipeline for software issue localization, SWE-Bench-Lite\n2. SWE-Fixer (Xie et al., 2025) — BM25 + learned retriever for file retrieval in SWE tasks\n3. LocAgent (Chen et al., 2025) — LLM agent with directed heterogeneous graphs for fault localization, supposedly ACL 2025\n4. RANGER (Shah et al., 2025) — repository knowledge graphs with MCTS for code retrieval\n5. CodexGraph (Liu et al., 2025) — code graph database queried via Cypher, supposedly NAACL 2025\n6. RepoGraph (Ouyang et al., 2025) — line-level code graph navigation for SE agents, supposedly ICLR 2025\n7. ARISE (Seddik & Fard, 2026) — statement-level def-use edges for agentic fault localization\n8. CL-DRD (Zeng et al., 2022) — curriculum learning for dense retrieval with knowledge distillation\n9. CoCoHaNeRe (Fan et al., 2025) — differentiable hard negative for code search contrastive learning\n\nFor each, give me: full author list (first 3+), exact title, venue, year, arXiv ID if any.",
  "run_in_background": "False"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify remaining paper citations",
    "prompt": "I need to verify the exact publication details for several papers. Use WebSearch for each. Report: authors, title, venue, year, arXiv ID.\n\n1. SweRank (Reddy et al., 2025) — retrieve-and-rerank pipeline for software issue localization, SWE-Bench-Lite\n2. SWE-Fixer (Xie et al., 2025) — BM25 + learned retriever for file retrieval in SWE tasks\n3. LocAgent (Chen et al., 2025) — LLM agent with directed heterogeneous graphs for fault localization, supposedly ACL 2025\n4. RANGER (Shah et al., 2025) — repository knowledge graphs with MCTS for code retrieval\n5. CodexGraph (Liu et al., 2025) — code graph database queried via Cypher, supposedly NAACL 2025\n6. RepoGraph (Ouyang et al., 2025) — line-level code graph navigation for SE agents, supposedly ICLR 2025\n7. ARISE (Seddik & Fard, 2026) — statement-level def-use edges for agentic fault localization\n8. CL-DRD (Zeng et al., 2022) — curriculum learning for dense retrieval with knowledge distillation\n9. CoCoHaNeRe (Fan et al., 2025) — differentiable hard negative for code search contrastive learning\n\nFor each, give me: full author list (first 3+), exact title, venue, year, arXiv ID if any.",
    "run_in_background": "False"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T03:22:30.709982+00:00_

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
  "session": "worker_write_related-work-expand_20260515T031325",
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

_source line 25 · 2026-05-15T03:22:30.710103+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T03:22:30.710226+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SweRank Reddy 2025 retrieve rerank software issue localization SWE-Bench arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SweRank Reddy 2025 retrieve rerank software issue localization SWE-Bench arXiv"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T03:22:30.710352+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SWE-Fixer Xie 2025 BM25 learned retriever file retrieval SWE tasks arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SWE-Fixer Xie 2025 BM25 learned retriever file retrieval SWE tasks arXiv"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T03:22:30.710689+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LocAgent Chen 2025 LLM agent directed heterogeneous graphs fault localization ACL arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LocAgent Chen 2025 LLM agent directed heterogeneous graphs fault localization ACL arXiv"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T03:22:30.710851+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RANGER Shah 2025 repository knowledge graphs MCTS code retrieval arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RANGER Shah 2025 repository knowledge graphs MCTS code retrieval arXiv"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T03:22:30.710980+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CodexGraph Liu 2025 code graph database Cypher NAACL arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CodexGraph Liu 2025 code graph database Cypher NAACL arXiv"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T03:22:30.711104+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RepoGraph Ouyang 2025 line-level code graph navigation SE agents ICLR arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RepoGraph Ouyang 2025 line-level code graph navigation SE agents ICLR arXiv"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T03:22:30.711225+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARISE Seddik Fard 2026 statement-level def-use edges agentic fault localization arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARISE Seddik Fard 2026 statement-level def-use edges agentic fault localization arXiv"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T03:22:30.711346+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CL-DRD Zeng 2022 curriculum learning dense retrieval knowledge distillation arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CL-DRD Zeng 2022 curriculum learning dense retrieval knowledge distillation arXiv"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T03:22:30.711465+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoCoHaNeRe Fan 2025 differentiable hard negative code search contrastive learning arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoCoHaNeRe Fan 2025 differentiable hard negative code search contrastive learning arXiv"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T03:22:30.711592+00:00_

Web search results for query: "SweRank Reddy 2025 retrieve rerank software issue localization SWE-Bench arXiv"

Links: [{"title":"[2505.07849] SweRank: Software Issue Localization with Code Ranking","url":"https://arxiv.org/abs/2505.07849"},{"title":"SWERANK+: Multilingual, Multi-Turn Code Ranking for Software Issue Localization","url":"https://arxiv.org/pdf/2512.20482"},{"title":"SweRank: Software Issue Localization with Code Ranking","url":"https://arxiv.org/pdf/2505.07849"},{"title":"GitHub - SalesforceAIResearch/SweRank","url":"https://github.com/SalesforceAIResearch/SweRank"},{"title":"SweRank: How AI is Revolutionizing Software Issue Localization","url":"https://www.salesforce.com/blog/swerank-software-issue-localization/?bc=OTH"},{"title":"SweRank: Software Issue Localization with Code Ranking - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250507849G/abstract"},{"title":"[2512.20482] SweRank+: Multilingual, Multi-Turn Code Ranking for Software Issue Localization","url":"https://arxiv.org/abs/2512.20482"},{"title":"SWERANK: SOFTWARE ISSUE LOCALIZATION","url":"https://openreview.net/pdf/e70b6b05efcf9186c40a441e74e6722123168739.pdf"},{"title":"Paper page - SweRank: Software Issue Localization with Code Ranking","url":"https://huggingface.co/papers/2505.07849"},{"title":"(PDF) SweRank: Software Issue Localization with Code Ranking","url":"https://www.researchgate.net/publication/391706826_SweRank_Software_Issue_Localization_with_Code_Ranking"}]

Based on the search results, I found detailed information about SweRank by Revanth Gangi Reddy and colleagues from 2025.

## Overview

SweRank is an efficient and effective retrieve-and-rerank framework for software issue localization. Software issue localization is the task of identifying the precise code locations (files, classes, or functions) relevant to a natural language issue description (e.g., bug report, feature request).

## Motivation

While recent LLM-based agentic approaches demonstrate promise, the
…[truncated 1239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T03:22:30.711774+00:00_

Web search results for query: "SWE-Fixer Xie 2025 BM25 learned retriever file retrieval SWE tasks arXiv"

Links: [{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution","url":"https://arxiv.org/html/2501.05040v2"},{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and ...","url":"https://aclanthology.org/2025.findings-acl.62.pdf"},{"title":"GitHub - InternLM/SWE-Fixer · GitHub","url":"https://github.com/InternLM/SWE-Fixer"},{"title":"Published as a conference paper at ICLR 2024 SWE-BENCH:","url":"https://arxiv.org/pdf/2310.06770"},{"title":"Deep Retrieval at CheckThat! 2025: Identifying Scientific Papers from Implicit Social Media Mentions via Hybrid Retrieval and Re-Ranking","url":"https://arxiv.org/html/2505.23250v1"},{"title":"Visual Words Meet BM25: Sparse Auto-Encoder Visual Word Scoring for Image Retrieval","url":"https://arxiv.org/html/2603.05781"},{"title":"From BM25 to Corrective RAG: Benchmarking Retrieval Strategies for Text-and-Table Documents","url":"https://arxiv.org/html/2604.01733v1"},{"title":"Blended RAG: Improving RAG (Retriever-Augmented Generation) Accuracy with Semantic Search and Hybrid Query-Based Retrievers","url":"https://arxiv.org/html/2404.07220"},{"title":"From BM25 to Corrective RAG: Benchmarking Retrieval ...","url":"https://arxiv.org/pdf/2604.01733"},{"title":"Evaluating the Effectiveness and Efficiency of ...","url":"https://arxiv.org/pdf/2410.09662"}]

I found relevant information about SWE-Fixer! Here are the search results:

## SWE-Fixer: Overview

SWE-Fixer is a simple yet effective pipeline-based approach for training open-source models to resolve Github issues.

## Retrieval Approach

The retrieval module employs BM25 along with a lightweight model to achieve coarse-to-fine file retrieval. More specifically, the retrieval task uses a coarse-to-fine strategy combining BM25 for initial file retrieval and a model to identify the defective files from the BM25 results.

## Archi
…[truncated 913 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T03:22:30.711932+00:00_

Web search results for query: "LocAgent Chen 2025 LLM agent directed heterogeneous graphs fault localization ACL arXiv"

Links: [{"title":"GitHub - gersteinlab/LocAgent: [ACL 2025] Graph-guided agentic framework for code localization https://arxiv.org/abs/2503.09089 · GitHub","url":"https://github.com/gersteinlab/LocAgent"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.426/"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://arxiv.org/html/2503.09089v1"},{"title":"(PDF) LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://www.researchgate.net/publication/389786036_LocAgent_Graph-Guided_LLM_Agents_for_Code_Localization"},{"title":"[2503.09089] LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://arxiv.org/abs/2503.09089"},{"title":"Paper page - LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://huggingface.co/papers/2503.09089"},{"title":"Meet LocAgent: Graph-Based AI Agents Transforming Code Localization for Scalable Software Maintenance - MarkTechPost","url":"https://www.marktechpost.com/2025/03/23/meet-locagent-graph-based-ai-agents-transforming-code-localization-for-scalable-software-maintenance/"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://aclanthology.org/2025.acl-long.426.pdf"},{"title":"IMPROVING CODE LOCALIZATION WITH REPOSITORY ...","url":"https://openreview.net/pdf/16c6927ff5b16b02a05c38612a8573a76a2c4fb9.pdf"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/locagent-graph-guided-llm-agents-code-localization"}]

Based on the web search results, I found comprehensive information about LocAgent. Here's what the research presents:

## Overview

LocAgent is a framework that addresses code localization through graph-based representation by parsing codebases into
…[truncated 1543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T03:22:30.712082+00:00_

Web search results for query: "CL-DRD Zeng 2022 curriculum learning dense retrieval knowledge distillation arXiv"

Links: [{"title":"[2204.13679] Curriculum Learning for Dense Retrieval Distillation","url":"https://arxiv.org/abs/2204.13679"},{"title":"Curriculum Learning for Dense Retrieval Distillation Hansi Zeng","url":"https://arxiv.org/pdf/2204.13679"},{"title":"[2204.13679v1] Curriculum Learning for Dense Retrieval Distillation","url":"https://arxiv.org/abs/2204.13679v1"},{"title":"GitHub - HansiZeng/CL-DRD: [SIGIR 2022] The official repo for the paper \"Curriculum Learning for Dense Retrieval Distillation\".","url":"https://github.com/HansiZeng/CL-DRD"},{"title":"[PDF] Curriculum Learning for Dense Retrieval Distillation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Curriculum-Learning-for-Dense-Retrieval-Zeng-Zamani/58aa3467505e900f76fb2295f2f94d60c70a65e2"},{"title":"Curriculum Learning for Dense Retrieval Distillation Hansi Zeng","url":"https://ciir-publications.cs.umass.edu/getpdf.php?id=1456"},{"title":"Curriculum Learning for Dense Retrieval Distillation | Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3477495.3531791"},{"title":"Translate-Distill: Learning Cross-Language Dense Retrieval by Translation and Distillation","url":"https://arxiv.org/html/2401.04810"},{"title":"LEAD: Liberal Feature-based Distillation for Dense Retrieval","url":"https://arxiv.org/html/2212.05225"},{"title":"Adam: Dense Retrieval Distillation with Adaptive Dark Examples","url":"https://arxiv.org/html/2212.10192"}]

I found the paper you were looking for. CL-DRD is a generic curriculum learning based optimization framework that controls the difficulty level of training data produced by the re-ranking (teacher) model. CL-DRD iteratively optimizes the dense retrieval (student) model by increasing the difficulty of the knowledge distillation data made available
…[truncated 850 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T03:22:30.712232+00:00_

Web search results for query: "CodexGraph Liu 2025 code graph database Cypher NAACL arXiv"

Links: [{"title":"[2408.03910] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.7/"},{"title":"CODEXGRAPH: Bridging Large Language Models and ...","url":"https://aclanthology.org/2025.naacl-long.7.pdf"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/html/2408.03910v2"},{"title":"CodexGraph","url":"https://laptype.github.io/CodexGraph-page/"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://www.researchgate.net/publication/392505894_CodexGraph_Bridging_Large_Language_Models_and_Code_Repositories_via_Code_Graph_Databases"},{"title":"CODEXGRAPH: Bridging Large Language Models","url":"https://arxiv.org/pdf/2408.03910v2"},{"title":"[2408.03910v2] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910v2"},{"title":"[2408.03910v1] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910v1"},{"title":"CodexGraph: LLM-Driven Code Graphs","url":"https://www.emergentmind.com/topics/codexgraph"}]

Based on the search results, I found comprehensive information about CodexGraph. Here's what the research reveals:

## Overview

CodexGraph is a system that integrates LLM agents with graph database interfaces extracted from code repositories. The paper was published in the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2025).

## Core Technology

CodexGraph enables th
…[truncated 1203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T03:22:30.712386+00:00_

Web search results for query: "RANGER Shah 2025 repository knowledge graphs MCTS code retrieval arXiv"

Links: [{"title":"[2509.25257] RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval","url":"https://arxiv.org/abs/2509.25257"},{"title":"Preprint. Under Review. RANGER: REPOSITORY-LEVEL AGENT FOR","url":"https://arxiv.org/pdf/2509.25257"},{"title":"RANGER: Repository‑level Agent for Graph‑Enhanced Retrieval","url":"https://arxiv.org/html/2509.25257v1"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Software Engineering on X: \"RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval. https://t.co/wXCWqY3iyI\" / X","url":"https://x.com/ComputerPapers/status/1973474396628029697"},{"title":"GitHub - DavidZWZ/Awesome-RAG-Reasoning: [EMNLP 2025] Awesome RAG Reasoning Resources · GitHub","url":"https://github.com/DavidZWZ/Awesome-RAG-Reasoning"},{"title":"REKG-MCTS: Reinforcing LLM Reasoning on Knowledge ...","url":"https://aclanthology.org/2025.findings-acl.484.pdf"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"Knowledge Graph Based Repository-Level Code Generation","url":"https://arxiv.org/html/2505.14394v1"},{"title":"[2501.00309] Retrieval-Augmented Generation with Graphs (GraphRAG)","url":"https://arxiv.org/abs/2501.00309"}]

Based on the search results, I found detailed information about RANGER, a recent research paper from 2025:

## RANGER: Repository-Level Agent for Graph-Enhanced Retrieval

RANGER is a repository-level code retrieval agent designed to address both code-entity queries and natural language queries. The paper was authored by Pratik Shah and colleagues and was submitted to arXiv on September 27, 2025.

### Key Components

The system presents a tool that c
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T03:22:30.712560+00:00_

Web search results for query: "RepoGraph Ouyang 2025 line-level code graph navigation SE agents ICLR arXiv"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf"},{"title":"Enhancing AI Software Engineering with Repository-level Code Graph RepoGraph:","url":"https://iclr.cc/media/iclr-2025/Slides/28957.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.14684"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/html/2410.14684v1"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2410.14684] RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/abs/2410.14684"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | OpenReview","url":"https://openreview.net/forum?id=dw9VUsSHGB"},{"title":"REPOGRAPH: ENHANCING AI SOFTWARE ENGINEERING WITH REPOSITORY-LEVEL CODE GRAPH - Illinois Experts","url":"https://experts.illinois.edu/en/publications/repograph-enhancing-ai-software-engineering-with-repository-level/"},{"title":"(PDF) RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://www.researchgate.net/publication/385108343_RepoGraph_Enhancing_AI_Software_Engineering_with_Repository-level_Code_Graph"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/4a4a3c197deac042461c677219efd36c-Abstract-Conference.html"}]

Based on the search results, I found relevant information about RepoGraph by Ouyang et al. Here's what I found:

## RepoGraph Overview

RepoGraph is a plug-in module that manages a repository-l
…[truncated 1500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T03:22:30.712761+00:00_

Web search results for query: "CoCoHaNeRe Fan 2025 differentiable hard negative code search contrastive learning arXiv"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval","url":"https://www.researchgate.net/publication/342655592_Approximate_Nearest_Neighbor_Negative_Contrastive_Learning_for_Dense_Text_Retrieval"},{"title":"CoCoSoDa: Effective Contrastive Learning for Code Search","url":"https://arxiv.org/pdf/2204.03293"},{"title":"Contrastive learning with hard negative samples","url":"https://arxiv.org/pdf/2010.04592"},{"title":"[2010.04592] Contrastive Learning with Hard Negative Samples","url":"https://arxiv.org/abs/2010.04592"},{"title":"Hard Negative Mixing for Contrastive Learning Yannis Kalantidis","url":"https://arxiv.org/pdf/2010.01028"},{"title":"GitHub - ryanzhumich/Contrastive-Learning-NLP-Papers: Paper List for Contrastive Learning for Natural Language Processing · GitHub","url":"https://github.com/ryanzhumich/Contrastive-Learning-NLP-Papers"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://csse.szu.edu.cn/attachment/cglr/1749432531_AAAI-2025%E8%AE%BA%E6%96%87-%E5%88%98%E6%B6%B5.pdf"},{"title":"Contrastive Representation Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2021-05-31-contrastive/"},{"title":"SynCo: Synthetic Hard Negatives in Contrastive Learning for Better Unsupervised Visual Representations","url":"https://arxiv.org/html/2410.02401v3"}]

Based on the search results, I found relevant information about CoCoHaNeRe. Here's what I found:

## CoCoHaNeRe Overview

CoCoHaNeRe is a Code search framework augmented by Contrastive learning with differentiable Hard Negative samples Retrieval.

## Key Technical Contributions

The framework design
…[truncated 1347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T03:22:30.712914+00:00_

Web search results for query: "ARISE Seddik Fard 2026 statement-level def-use edges agentic fault localization arXiv"

Links: [{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: Agentic Rubric-Guided Iterative Survey Engine for Automated Scholarly Paper Generation","url":"https://arxiv.org/html/2511.17689v1"},{"title":"Agentic Code Reasoning","url":"https://arxiv.org/html/2603.01896v1"},{"title":"A Survey of Agentic AI and Cybersecurity: Challenges, Opportunities and Use-case Prototypes","url":"https://arxiv.org/html/2601.05293v1"},{"title":"[2403.16362] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/abs/2403.16362"},{"title":"An Empirical Study on LLM-based Agents for Automated Bug Fixing","url":"https://arxiv.org/html/2411.10213v1"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=1450&show=2000"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"},{"title":"[2601.20810] Context-Augmented Code Generation Using Programming Knowledge Graphs","url":"https://arxiv.org/abs/2601.20810"}]

I found the paper you're looking for! Here are the key details about ARISE:

## ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair

The paper is authored by Shahd Seddik and Fatemeh Fard from the University of British Columbia.

### Overview
ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

### Key Innovat
…[truncated 1057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T03:22:30.713069+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.07849 SweRank authors full list Gangi Reddy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.07849 SweRank authors full list Gangi Reddy"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T03:22:30.713198+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2501.05040 SWE-Fixer authors full list Xie venue ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2501.05040 SWE-Fixer authors full list Xie venue ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T03:22:30.713321+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2509.25257 RANGER authors full list Pratik Shah 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2509.25257 RANGER authors full list Pratik Shah 2025"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T03:22:30.713443+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2410.14684 RepoGraph authors full list Ouyang ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2410.14684 RepoGraph authors full list Ouyang ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T03:22:30.713561+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.03117 ARISE authors Seddik Fard full details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.03117 ARISE authors Seddik Fard full details"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T03:22:30.713705+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CoCoHaNeRe\" Fan 2025 code search hard negative arXiv paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CoCoHaNeRe\" Fan 2025 code search hard negative arXiv paper"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T03:22:30.713827+00:00_

Web search results for query: "arxiv 2505.07849 SweRank authors full list Gangi Reddy"

Links: [{"title":"[2505.07849] SweRank: Software Issue Localization with Code Ranking","url":"https://arxiv.org/abs/2505.07849"},{"title":"SweRank: Software Issue Localization with Code Ranking","url":"https://arxiv.org/html/2505.07849"},{"title":"GitHub - SalesforceAIResearch/SweRank","url":"https://github.com/SalesforceAIResearch/SweRank"},{"title":"Paper page - SweRank: Software Issue Localization with Code Ranking","url":"https://huggingface.co/papers/2505.07849"},{"title":"arXiv:2505.07849v1 [cs.SE] 7 May 2025","url":"https://arxiv.org/pdf/2505.07849"},{"title":"SweRank+: Multilingual, Multi-Turn Code Ranking for Software Issue Localization","url":"https://arxiv.org/html/2512.20482v1"},{"title":"dblp: SweRank: Software Issue Localization with Code Ranking.","url":"https://dblp.org/rec/journals/corr/abs-2505-07849.html"},{"title":"Revanth Gangi Reddy's Post","url":"https://www.linkedin.com/posts/revanth-gangi-reddy-5b7257ba_swerank-now-accepted-at-iclr-2026-paper-activity-7421644822752542720-nr31"},{"title":"SweRank: How AI is Revolutionizing Software Issue Localization","url":"https://www.salesforce.com/blog/swerank-software-issue-localization/?bc=OTH"},{"title":"Revanth Gangi Reddy - Research Scientist @ DeepMind","url":"https://www.linkedin.com/in/revanth-gangi-reddy-5b7257ba/"}]

Based on the search results, here is the full list of authors for arXiv paper 2505.07849 "SweRank: Software Issue Localization with Code Ranking":

1. Revanth Gangi Reddy
2. Tarun Suresh
3. JaeHyeok Doo
4. Ye Liu
5. Xuan Phi Nguyen
6. Yingbo Zhou
7. Semih Yavuz
8. Caiming Xiong
9. Heng Ji
10. Shafiq Joty


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T03:22:30.713962+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2408.03910 CodexGraph authors full list Liu 2024 NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2408.03910 CodexGraph authors full list Liu 2024 NAACL 2025"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T03:22:30.714102+00:00_

Web search results for query: "arxiv 2410.14684 RepoGraph authors full list Ouyang ICLR 2025"

Links: [{"title":"[2410.14684] RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/abs/2410.14684"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/html/2410.14684"},{"title":"Enhancing AI Software Engineering with Repository-level Code Graph RepoGraph:","url":"https://iclr.cc/media/iclr-2025/Slides/28957.pdf"},{"title":"Paper page - RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://huggingface.co/papers/2410.14684"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | alphaXiv","url":"https://www.alphaxiv.org/en/overview/2410.14684"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/?searchtype=author&query=ZIlin+Ma"},{"title":"Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/html/2503.21710v1"},{"title":"(PDF) RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://www.researchgate.net/publication/385108343_RepoGraph_Enhancing_AI_Software_Engineering_with_Repository-level_Code_Graph"},{"title":"MrZilinXiao/RepoGraph · Datasets at Hugging Face","url":"https://huggingface.co/datasets/MrZilinXiao/RepoGraph"},{"title":"Hunyuan on X: \"Last week, we hosted a live session to dive into Tencent Hunyuan's ICLR 2025 papers with the authors，presented six of these papers, which had covered multiple areas including large model algorithms, speech technologies, life sciences, and data science and so on. We are excited https://t.co/YEmDXXDzGx\" / X","url":"https://x.com/TencentHunyuan/status/1930467525030228033"}]

Based on the search results, I found the information about the RepoGraph paper:

The full list of authors for the RepoGraph paper (arxiv 2410.14684) is: Siru 
…[truncated 337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T03:22:30.714255+00:00_

Web search results for query: "arxiv 2501.05040 SWE-Fixer authors full list Xie venue ACL 2025"

Links: [{"title":"[2501.05040] SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution","url":"https://arxiv.org/abs/2501.05040"},{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution","url":"https://arxiv.org/html/2501.05040"},{"title":"GitHub - InternLM/SWE-Fixer · GitHub","url":"https://github.com/InternLM/SWE-Fixer"},{"title":"internlm/SWE-Fixer-Editor-72B · Hugging Face","url":"https://huggingface.co/internlm/SWE-Fixer-Editor-72B"},{"title":"SWE-Fixer/README.md at main · InternLM/SWE-Fixer","url":"https://github.com/InternLM/SWE-Fixer/blob/main/README.md"},{"title":"Paper page - SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution","url":"https://huggingface.co/papers/2501.05040"},{"title":"SWE-Fixer: Training LLMs for Real World Github Issue Resolving","url":"https://arxiv.org/html/2501.05040v1"},{"title":"internlm/SWE-Fixer-Retriever-7B · Hugging Face","url":"https://huggingface.co/internlm/SWE-Fixer-Retriever-7B"},{"title":"internlm/SWE-Fixer-Train-110K · Datasets at Hugging Face","url":"https://huggingface.co/datasets/internlm/SWE-Fixer-Train-110K"},{"title":"BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills","url":"https://arxiv.org/html/2510.19898v1"}]

Based on the search results, here's what I found about the SWE-Fixer paper (arXiv 2501.05040):

**Full Author List:**
Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, and Kai Chen

**Venue:**
The search results do not contain information confirming that this paper has been accepted to ACL 2025. The paper appears to currently be an arXiv preprint from January 2025, but there is no evidence in the search results that it has been published at or accepted to ACL 2025 or any other conference venue.

**Note:** While you mentioned "ACL 2025" in your query, this information
…[truncated 336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T03:22:30.714401+00:00_

Web search results for query: "arxiv 2509.25257 RANGER authors full list Pratik Shah 2025"

Links: [{"title":"[2509.25257] RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval","url":"https://arxiv.org/abs/2509.25257"},{"title":"RANGER: Repository‑level Agent for Graph‑Enhanced Retrieval","url":"https://arxiv.org/html/2509.25257"},{"title":"Preprint. Under Review. RANGER: REPOSITORY-LEVEL AGENT FOR","url":"https://arxiv.org/pdf/2509.25257"},{"title":"[1012.3359] Curve Reconstruction in Riemannian Manifolds: Ordering Motion Frames","url":"https://arxiv.org/abs/1012.3359"},{"title":"[1810.10664] Automated Process Incorporating Machine Learning Segmentation and Correlation of Oral Diseases with Systemic Health","url":"https://arxiv.org/abs/1810.10664"},{"title":"All Publications | Pratik Shah","url":"https://www.pratiks.info/publications/all/"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=474&show=500"},{"title":"Machine Learning Publications | Pratik Shah","url":"https://www.pratiks.info/publications/machine-learning/"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=3125&show=2000"},{"title":"[2509.15295] Living on the edge: a non-perturbative resolution to the negativity of bulk entropies","url":"https://arxiv.org/abs/2509.15295"}]

Based on the search results, here is the complete list of authors for the RANGER paper (arxiv 2509.25257):

The authors are: Pratik Shah (Georgia Institute of Technology and Nutanix), Rajat Ghosh (Nutanix), Aryan Singhal (Nutanix), and Debojyoti Dutta (Nutanix). The paper notes that the work was done during Pratik's internship at Nutanix.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-15T03:22:30.714540+00:00_

Web search results for query: ""CoCoHaNeRe" Fan 2025 code search hard negative arXiv paper"

Links: [{"title":"Improving Code Search with Hard Negative Sampling Based on Fine-tuning","url":"https://arxiv.org/html/2305.04508"},{"title":"[2305.04508] Improving Code Search with Hard Negative Sampling Based on Fine-tuning","url":"https://arxiv.org/abs/2305.04508"},{"title":"Exploration and Exploitation of Hard Negative Samples for Cross-Domain Sequential Recommendation | Proceedings of the Eighteenth ACM International Conference on Web Search and Data Mining","url":"https://dl.acm.org/doi/10.1145/3701551.3703535"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=6625&show=2000"},{"title":"[2010.04592] Contrastive Learning with Hard Negative Samples","url":"https://arxiv.org/abs/2010.04592"},{"title":"Artificial Intelligence Jan 2025","url":"https://arxiv.org/list/cs.AI/2025-01?skip=1575&show=2000"},{"title":"Computer Science Aug 2024","url":"https://arxiv.org/list/cs/2024-08?skip=375&show=2000"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=3075&show=1000"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=2425&show=2000"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=550&show=2000"}]

I found a relevant arXiv paper on code search with hard negative sampling. The search returned "Improving Code Search with Hard Negative Sampling Based on Fine-tuning" (arXiv paper 2305.04508).

However, I didn't find a paper specifically titled "CoCoHaNeRe" in the search results. The query you provided appears to combine multiple concepts. The closest match I found addresses:

- Pre-trained code models for code search tasks using fine-tuning on the search-relevant task
- A cross-encoder architecture for code search that jointly encodes query and code, with a Retriever-Ranker framework that cascades the dual-encoder and cross-enco
…[truncated 386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T03:22:30.714703+00:00_

Web search results for query: "arxiv 2408.03910 CodexGraph authors full list Liu 2024 NAACL 2025"

Links: [{"title":"[2408.03910] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/html/arXiv:2408.03910"},{"title":"[2408.03910v2] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910v2"},{"title":"[2408.03910v1] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910v1"},{"title":"Paper page - CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://huggingface.co/papers/2408.03910"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.7/"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2408.03910"},{"title":"[PDF] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases | Semantic Scholar","url":"https://api.semanticscholar.org/arXiv:2408.03910"},{"title":"CodexGraph","url":"https://laptype.github.io/CodexGraph-page/"},{"title":"CODEXGRAPH: Bridging Large Language Models","url":"https://arxiv.org/pdf/2408.03910v2"}]

Based on the search results, I found the complete author list for the CodexGraph paper (arXiv 2408.03910):

The authors are: Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, and Wenmeng Zhou.

The paper was published in 2025 as part of the NAACL (North American Chapter of the Association for Computational Linguistics) 2025 conference proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T03:22:30.714843+00:00_

Web search results for query: "arxiv 2605.03117 ARISE authors Seddik Fard full details"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[1506.03117] Untitled Document","url":"https://ar5iv.labs.arxiv.org/html/1506.03117"},{"title":"[2605.06826] How Does Attention Help? Insights from Random Matrices on Signal Recovery from Sequence Models","url":"https://arxiv.org/abs/2605.06826"},{"title":"[2605.05417] Signature structure of quadratic response under Zeno-Schur coarse graining in open quantum systems","url":"https://arxiv.org/abs/2605.05417"},{"title":"[2605.03140] Evaluating Retrieval-Augmented Generation for Explainable Malware Analysis","url":"https://arxiv.org/abs/2605.03140"},{"title":"[2511.02869] Analysis of AdvFusion: Adapter-based Multilingual Learning for Code Large Language Models","url":"https://arxiv.org/abs/2511.02869"},{"title":"[2605.13710] Pattern-based tests for two-dimensional copulas","url":"https://arxiv.org/abs/2605.13710"},{"title":"[2605.12605] Stability of localized solutions to lattice dynamical systems","url":"https://arxiv.org/abs/2605.12605"},{"title":"[2605.08644] On Codes with Support-Constrained Parity Checks","url":"https://arxiv.org/abs/2605.08644"}]

Based on the search results, here are the full details for arxiv paper 2605.03117:

## Paper Details

**Title:** ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair

**Authors:** Shahd Seddik and Fatemeh Fard, both from University of British Columbia in Kelowna, Canada

**Submission Date:** Submitted on 4 May 2026

## Abstract Summary

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a mult
…[truncated 1133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T03:22:30.714994+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SWE-Fixer Xie 2025 ACL findings accepted venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SWE-Fixer Xie 2025 ACL findings accepted venue conference"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T03:22:30.715121+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoCoHaNeRe code contrastive hard negative retrieval Fan Shi 2024 2025 TOSEM ACM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoCoHaNeRe code contrastive hard negative retrieval Fan Shi 2024 2025 TOSEM ACM"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-15T03:22:30.715244+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SweRank ICLR 2026 accepted Gangi Reddy venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SweRank ICLR 2026 accepted Gangi Reddy venue"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T03:22:30.715364+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RANGER Shah Ghosh Singhal Dutta 2025 arxiv 2509.25257 venue under review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RANGER Shah Ghosh Singhal Dutta 2025 arxiv 2509.25257 venue under review"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T03:22:30.715489+00:00_

Web search results for query: "SWE-Fixer Xie 2025 ACL findings accepted venue conference"

Links: [{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.62/"},{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and ...","url":"https://aclanthology.org/2025.findings-acl.62.pdf"},{"title":"Paper Digest: ACL 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/07/acl-2025-papers-highlights/"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"Three papers accepted in ACL 2025 by our group","url":"https://www.linkedin.com/posts/sriparna-saha-1a1338161_acl2025-activity-7329101872303104001-bxta"},{"title":"ACL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FConference"},{"title":"Conference acceptance rates - ACL Wiki","url":"https://www.aclweb.org/aclwiki/Conference_acceptance_rates"},{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution","url":"https://www.researchgate.net/publication/394273882_SWE-Fixer_Training_Open-Source_LLMs_for_Effective_and_Efficient_GitHub_Issue_Resolution"},{"title":"Paper Accepted at Findings of ACL 2025","url":"https://michelepapucci.github.io/blog/paper-accepted-at-findings-of-acl-2025/"}]

Based on the search results, here are the findings about the SWE-Fixer paper:

SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution, authored by Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, and Kai Chen, was accepted to the Findings of the Association for Computational Linguistics: ACL 2025, pages 1123–1139, Vienna, Austria.

The paper focuses on resolving real-world tasks on GitHu
…[truncated 400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-15T03:22:30.715684+00:00_

Web search results for query: "CoCoHaNeRe code contrastive hard negative retrieval Fan Shi 2024 2025 TOSEM ACM"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Visual perturbation and adaptive hard negative contrastive ...","url":"https://dl.acm.org/doi/10.24963/ijcai.2025/605"},{"title":"ACM Transactions on Software Engineering and Methodology","url":"https://ftp.math.utah.edu/pub/tex/bib/toc/tosem.html"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b010241b9f1cdfc7d4c392db899cef86-Paper-Conference.pdf"},{"title":"TOSEM: Just Accepted","url":"https://dl.acm.org/toc/tosem/justaccepted"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"Exploration and Exploitation of Hard Negative Samples for Cross-Domain Sequential Recommendation | Proceedings of the Eighteenth ACM International Conference on Web Search and Data Mining","url":"https://dl.acm.org/doi/10.1145/3701551.3703535"},{"title":"SC-HNM: Filtering False Negatives for Network Service Embeddings | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-6209-1_21"},{"title":"Knowledge-guided prompt-based continual learning: : Aligning task-prompts through contrastive hard negatives: Knowledge-Based Systems: Vol 310, No C","url":"https://dl.acm.org/doi/10.1016/j.knosys.2025.113009"},{"title":"Generalized Contrastive Learning for Multi-Modal Retrieval and Ranking | Companion Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3701716.3715227"}]

Based on the search results, I found relevant information about CoCoHaNeRe:

CoCoHaNeRe is a Code sea
…[truncated 968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T03:22:30.715880+00:00_

Web search results for query: "SweRank ICLR 2026 accepted Gangi Reddy venue"

Links: [{"title":"Salesforce AI Research at ICLR 2026 - Salesforce","url":"https://www.salesforce.com/blog/salesforce-iclr-2026/"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"SweRank: How AI is Revolutionizing Software Issue Localization","url":"https://www.salesforce.com/blog/swerank-software-issue-localization/?bc=OTH"},{"title":"ICLR 2026 in Brazil– Deadlines, Venue, Dates, and Call for Papers","url":"https://conferenceinc.net/post/iclr-2026-conference/"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"ICLR 2026 Accepted Papers: Oral Papers, Research Trends & Top Highlights","url":"https://www.bohrium.com/en/blog/research-notes/iclr-2026-accepted-papers-highlights/"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"},{"title":"ICLR.2026 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026"},{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"}]

Based on the search results, I found the information you're looking for:

SweRank is an efficient retrieve-and-rerank framework for software issue localization, trained on the SweLoc dataset, that achieves state-of-the-art performance on SWE-Bench-Lite and LocBench while outperforming costly agent-based systems that rely on closed-source LLMs.

The paper was authored by Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, and Shafiq Joty.

The conference runs April 23–27 at the Riocentro Convention and Event Center in Rio de Janeiro, Brazil.


REMINDER: You MUST include the sources above in your re
…[truncated 45 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-15T03:22:30.716036+00:00_

Web search results for query: "RANGER Shah Ghosh Singhal Dutta 2025 arxiv 2509.25257 venue under review"

Links: [{"title":"[2509.25257] RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval","url":"https://arxiv.org/abs/2509.25257"},{"title":"RANGER: Repository‑level Agent for Graph‑Enhanced Retrieval","url":"https://arxiv.org/html/2509.25257"},{"title":"[2509.21148] Scalaron dark matter dynamics: effects of Higgs non-minimal coupling to gravity","url":"https://arxiv.org/abs/2509.21148"},{"title":"Google Scholar","url":"https://scholar.google.com/citations?user=nVo0WNYAAAAJ&hl=en"},{"title":"Paramita Dutta's articles on arXiv","url":"https://arxiv.org/a/dutta_p_1.html"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=33375&show=1000"},{"title":"[2509.20324v1] RAG Security and Privacy: Formalizing the Threat Model and Attack Surface","url":"https://arxiv.org/abs/2509.20324v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=OwNoTs2r8e"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=250&show=2000"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=885&show=1000"}]

Based on the search results, I found information about the paper you're looking for:

The paper is titled "RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval" by Pratik Shah, Rajat Ghosh, Aryan Singhal, and Debojyoti Dutta, with arxiv ID 2509.25257.

RANGER is a repository-level code retrieval agent designed to address both code-entity queries and natural language queries, filling a gap in recent works that have focused primarily on code-entity queries.

Regarding the venue, the search results show that the paper was submitted to arXiv on September 27, 2025, but the specific publication venue information (whether it's under review for a conference or journal) is not explicitly stated in the search results provided. The paper is currently avai
…[truncated 132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-15T03:22:30.716188+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoCoHaNeRe TOSEM 2025 authors Fan Shi code search contrastive hard negative mining full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoCoHaNeRe TOSEM 2025 authors Fan Shi code search contrastive hard negative mining full author list"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-15T03:22:30.716318+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:dl.acm.org \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\" authors TOSEM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:dl.acm.org \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\" authors TOSEM"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T03:22:30.716436+00:00_

Web search results for query: "site:dl.acm.org "Effective Hard Negative Mining for Contrastive Learning-Based Code Search" authors TOSEM"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"}]

I found the paper! The paper "Effective Hard Negative Mining for Contrastive Learning-Based Code Search" proposes CoCoHaNeRe, a contrastive learning code search model that introduces hard negative examples into contrastive training, which are negative examples in the codebase that are most similar to positive examples.

The paper is published in ACM Transactions on Software Engineering and Methodology (TOSEM) and is available at: https://dl.acm.org/doi/full/10.1145/3695994


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-15T03:22:30.716683+00:00_

Web search results for query: "CoCoHaNeRe TOSEM 2025 authors Fan Shi code search contrastive hard negative mining full author list"

Links: [{"title":"[PDF] CoCoSoDa: Effective Contrastive Learning for Code Search | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoCoSoDa:-Effective-Contrastive-Learning-for-Code-Shi-Wang/ae52599f2d2731f68c567b6726a5185c06cb9a41"},{"title":"[2204.03293] CoCoSoDa: Effective Contrastive Learning for Code Search","url":"https://arxiv.org/abs/2204.03293"},{"title":"HedgeCode: A Multi-Task Hedging Contrastive Learning Framework for Code Search | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00008"},{"title":"CoCoSoDa: Effective Contrastive Learning for Code Search","url":"https://arxiv.org/pdf/2204.03293"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://csse.szu.edu.cn/attachment/cglr/1749432531_AAAI-2025%E8%AE%BA%E6%96%87-%E5%88%98%E6%B6%B5.pdf"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"CoCoSoDa: Effective Contrastive Learning for Code Search | Proceedings of the 45th International Conference on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/ICSE48619.2023.00185"},{"title":"TOSEM: Just Accepted","url":"https://dl.acm.org/toc/tosem/justaccepted"},{"title":"dblp: ACM Transactions on Software Engineering and Methodology, Volume 34","url":"https://dblp.org/db/journals/tosem/tosem34.html"},{"title":"[2204.03293v3] CoCoSoDa: Effective Contrastive Learning for Code Search","url":"https://arxiv.org/abs/2204.03293v3"}]

Based on the search results, I found information about a related paper. The paper "Effective Hard Negative Mining for Contrastive Learning-Based Code Search" by Ye Fan, Chuanyi L
…[truncated 1055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-15T03:22:30.716859+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\" CoCoHaNeRe authors \"Ye Fan\" \"Chuanyi Li\" TOSEM 2025 volume issue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\" CoCoHaNeRe authors \"Ye Fan\" \"Chuanyi Li\" TOSEM 2025 volume issue"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T03:22:30.716993+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CodexGraph NAACL 2025 authors \"Xiangyan Liu\" \"Bo Lan\" \"Zhiyuan Hu\" full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CodexGraph NAACL 2025 authors \"Xiangyan Liu\" \"Bo Lan\" \"Zhiyuan Hu\" full list"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T03:22:30.717123+00:00_

Web search results for query: "CodexGraph NAACL 2025 authors "Xiangyan Liu" "Bo Lan" "Zhiyuan Hu" full list"

Links: [{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.7/"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://www.researchgate.net/publication/392505894_CodexGraph_Bridging_Large_Language_Models_and_Code_Repositories_via_Code_Graph_Databases"},{"title":"dblp: NAACL-HLT 2025 - Volume 1: Long Papers","url":"https://dblp.org/db/conf/naacl/naacl2025-1.html"},{"title":"NAACL 2025 Annual Conference of the Nations of the Americas Chapter of","url":"https://aclanthology.org/2025.naacl-long.0.pdf"},{"title":"Zhiyuan Hu - Homepage","url":"https://zhiyuanhubj.github.io/"},{"title":"[2408.03910] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910"},{"title":"CodexGraph","url":"https://laptype.github.io/CodexGraph-page/"},{"title":"Xiangyan Liu","url":"https://xyliugo.github.io/"},{"title":"[2408.03910v2] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910v2"}]

Based on the search results, here is the full list of authors for the CodexGraph paper presented at NAACL 2025:

The authors are: Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, and Wenmeng Zhou.

The paper was published in the Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 142–160, in Albuquerque, New Mexico.


REMINDER: You MUST include the sources above in your response to the user using markdown hyp
…[truncated 8 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-15T03:22:30.717327+00:00_

Web search results for query: ""Effective Hard Negative Mining for Contrastive Learning-Based Code Search" CoCoHaNeRe authors "Ye Fan" "Chuanyi Li" TOSEM 2025 volume issue"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-based Code Search | CoLab","url":"https://colab.ws/articles/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"A Hard Negatives Mining and Enhancing Method for Multi-Modal Contrastive Learning","url":"https://www.mdpi.com/2079-9292/14/4/767"},{"title":"Mining negative samples on contrastive learning via curricular weighting strategy - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S002002552400447X"},{"title":"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning","url":"https://proceedings.mlr.press/v162/xia22b.html"},{"title":"Affinity Uncertainty-Based Hard Negative Mining in Graph Contrastive Learning | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10382709/"},{"title":"Affinity Uncertainty-based Hard Negative Mining in Graph Contrastive Learning","url":"https://arxiv.org/html/2301.13340v2"},{"title":"Hard negative mixing for contrastive learning | Proceedings of the 34th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3495724.3497553"}]

Based on the search results, I found the information about the paper:

The paper "Effective Hard Negative
…[truncated 608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T03:22:30.717627+00:00_

Here are the verified publication details for all 9 papers.

---

**1. SweRank**
- **Title:** SweRank: Software Issue Localization with Code Ranking
- **Authors:** Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty
- **Venue:** ICLR 2026 (accepted; originally arXiv May 2025)
- **Year:** 2025 (preprint) / 2026 (conference)
- **arXiv ID:** 2505.07849
- **Note:** Your citation says "Reddy et al., 2025" -- the first author is Revanth Gangi Reddy. The paper was accepted at ICLR 2026, not a 2025 venue.

---

**2. SWE-Fixer**
- **Title:** SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution
- **Authors:** Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen
- **Venue:** Findings of ACL 2025 (pages 1123--1139, Vienna, Austria)
- **Year:** 2025
- **arXiv ID:** 2501.05040

---

**3. LocAgent**
- **Title:** LocAgent: Graph-Guided LLM Agents for Code Localization
- **Authors:** Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang
- **Venue:** ACL 2025 (Long Papers, pages 8697--8727, Vienna, Austria) -- confirmed
- **Year:** 2025
- **arXiv ID:** 2503.09089

---

**4. RANGER**
- **Title:** RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval
- **Authors:** Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta
- **Venue:** arXiv preprint, marked "Under Review" (no confirmed conference venue yet)
- **Year:** 2025 (submitted September 2025)
- **arXiv ID:** 2509.25257
- **Note:** The arXiv PDF header says "Preprint. Under Review." No published venue confirmed as of now.

---

**5. CodexGraph**
- **Title:** CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases
- **Authors:** Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou
- **Venue:** NAACL 2025 (Long Papers, pages 142--160, Albuq
…[truncated 2314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Agent",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-15T03:22:30.717953+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read existing files and catalog current citations', 'status': 'completed', 'activeForm': 'Reading existing files and cataloging current citations'}, {'content': 'Verify new paper citations via WebSearch (3 agents running)', 'status': 'completed', 'activeForm': 'Verifying new paper citations via WebSearch'}, {'content': 'Verify remaining existing citations', 'status': 'completed', 'activeForm': 'Verifying remaining existing citations'}, {'content': 'Write expanded related_work_v1.md with 25+ citations', 'status': 'in_progress', 'activeForm': 'Writing expanded related_work_v1.md'}, {'content': 'Create references.bib with all citations', 'status': 'pending', 'activeForm': 'Creating references.bib'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read existing files and catalog current citations', 'status': 'completed', 'activeForm': 'Reading existing files and cataloging current citations'}, {'content': 'Verify new paper citations via WebSearch (3 agents running)', 'status': 'completed', 'activeForm': 'Verifying new paper citations via WebSearch'}, {'content': 'Verify remaining existing citations', 'status': 'completed', 'activeForm': 'Verifying remaining existing citations'}, {'content': 'Write expanded related_work_v1.md with 25+ citations', 'status': 'in_progress', 'activeForm': 'Writing expanded related_work_v1.md'}, {'content': 'Create references.bib with all citations', 'status': 'pending', 'activeForm': 'Creating references.bib'}]"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-15T03:22:30.718119+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-15T03:22:30.718265+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "content": "# 2. Related Work\n\n## 2.1 Code Retrieval Methods\n\nRepo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \\cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \\cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \\cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \\cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.\n\nA parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \\cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \\cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \\cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \\cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \\cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \\cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization---though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they incur per-query computational costs and, for agent-based systems, require multiple LLM calls per retrieval step.\n\nCritically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.\n\n## 2.2 Pre-trained Code Representations and Contrastive Learning\n\nPre-trained code models have evolved rapidly in both architecture and training objectives. CodeBERT \\cite{feng2020codebert} introduced bimodal pre-training on natural language--programming language pairs using masked language modeling and replaced token detection, establishing that cross-modal pre-training improves downstream code search and documentation generation. GraphCodeBERT \\cite{guo2021graphcodebert} extended this by incorporating data-flow edges into pre-training, showing that intra-procedural data-flow information improves code understanding tasks. UniXcoder \\cite{guo2022unixcoder} unified encoder-only, decoder-only, and encoder-decoder modes in a single framework with cross-modal pre-training, achieving strong results across code understanding and generation benchmarks. code2vec \\cite{alon2019code2vec} demonstrated that AST path-based representations capture meaningful program properties at scale, complementing token-level approaches. More recently, CodeSage \\cite{zhang2024codesage} scaled bidirectional code encoders with a two-stage pipeline combining identifier deobfuscation and bimodal contrastive learning, achieving state-of-the-art code retrieval performance. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning---a fundamentally different application of structural information that operates at the repository level rather than the function level.\n\nBuilding on the success of Sentence-BERT \\cite{reimers2019sentencebert} in learning dense representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns. ContraCode \\cite{jain2021contracode} applies compiler-driven transformations to generate functionally equivalent program variants as positive pairs, training the encoder to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal (code-code) and bimodal (code-text) contrastive objectives, achieving strong results across code search benchmarks. SCodeR \\cite{li2022scoder} introduces soft-labeled contrastive pre-training that uses a teacher model to assign continuous similarity scores rather than binary labels, capturing graded code similarity. \\citet{ding2022programcontrasts} leverage program structure and functional attributes to construct contrastive pairs for learning code (dis)similarity representations. InferCode \\cite{bui2021infercode} takes a complementary self-supervised approach, learning code representations by predicting AST subtrees without requiring labeled pairs.\n\nThe recent shift toward decoder-only architectures has produced models such as StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, which achieve strong performance across code generation and understanding tasks. These models are increasingly adopted as backbone encoders for contrastive fine-tuning in code retrieval, though their pretrained representation geometries differ substantially from encoder-only predecessors---a factor that, as we show, interacts with negative mining strategy effectiveness.\n\nDespite the progress in pre-trained code representations and contrastive learning, these methods share a common dependency on negative sampling strategy yet few systematically investigate which negatives yield the best representations for code retrieval. Most approaches rely on in-batch negatives \\cite{karpukhin2020dpr} or random sampling, leaving the interaction between negative selection strategy and encoder representation geometry unexplored. Our work addresses this gap with a controlled comparison across negative mining strategies on modern decoder-only code encoders.\n\n## 2.3 Hard Negative Mining\n\nHard negative mining---selecting negative examples that are challenging for the current model---is well established for improving contrastive learning. In visual representation learning, SimCLR \\cite{chen2020simclr} demonstrates the importance of large batch sizes and hard negatives for learning discriminative features. In dense text retrieval, DPR \\cite{karpukhin2020dpr} shows that BM25-retrieved passages serve as effective hard negatives beyond in-batch sampling. ANCE \\cite{xiong2021ance} advances this by mining negatives from the model's own embedding space via approximate nearest neighbor search, achieving substantial gains over static BM25 negatives. STAR \\cite{zhan2021star} addresses the training instability of dynamic mining by jointly training the retriever with periodically refreshed hard negatives and a random negative stabilization mechanism. RocketQA \\cite{qu2021rocketqa} introduces a cross-encoder as a denoiser to filter false negatives from hard negative candidates, demonstrating that the quality of hard negatives matters as much as their difficulty. Curriculum-based approaches such as CL-DRD \\cite{zeng2022cldrd} progressively increase negative difficulty during training through knowledge distillation.\n\nIn the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \\cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining in structural code retrieval settings.\n\nOur work provides a systematic comparison that challenges the assumption that expensive gradient-based or dynamic hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation or periodic re-mining. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and observe that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry---an interaction that existing work does not examine.\n\n## 2.4 Code Structure Analysis\n\nOur structure-grounded negative mining pipeline builds upon established foundations in program analysis. The program dependence graph \\cite{ferrante1987pdg}, representing both control and data dependencies between program statements, provides the theoretical basis for inter-procedural data-flow analysis. Yamaguchi et al.\\ \\cite{yamaguchi2014cpg} introduced the code property graph, merging ASTs, control-flow graphs, and program dependence graphs into a unified queryable representation implemented in the Joern platform, primarily for vulnerability detection. Our pipeline leverages CodeQL \\cite{avgustinov2016ql}, which models codebases as relational databases queryable via a declarative object-oriented language, enabling scalable inter-procedural taint tracking across repository-scale codebases. While these tools have been primarily applied to vulnerability detection and program optimization, we repurpose inter-procedural data-flow analysis for a novel application: constructing structure-grounded hard negatives for contrastive code retrieval training.\n\nTogether, these four lines of work---code retrieval, contrastive code representation learning, hard negative mining, and code structure analysis---converge in our approach, which uses structural signals from program analysis to improve contrastive training for code retrieval, distinct from methods that apply structure at inference time or during pre-training.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "content": "# 2. Related Work\n\n## 2.1 Code Retrieval Methods\n\nRepo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \\cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \\cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \\cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \\cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.\n\nA parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \\cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \\cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \\cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \\cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \\cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \\cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization---though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they incur per-query computational costs and, for agent-based systems, require multiple LLM calls per retrieval step.\n\nCritically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.\n\n## 2.2 Pre-trained Code Representations and Contrastive Learning\n\nPre-trained code models have evolved rapidly in both architecture and training objectives. CodeBERT \\cite{feng2020codebert} introduced bimodal pre-training on natural language--programming language pairs using masked language modeling and replaced token detection, establishing that cross-modal pre-training improves downstream code search and documentation generation. GraphCodeBERT \\cite{guo2021graphcodebert} extended this by incorporating data-flow edges into pre-training, showing that intra-procedural data-flow information improves code understanding tasks. UniXcoder \\cite{guo2022unixcoder} unified encoder-only, decoder-only, and encoder-decoder modes in a single framework with cross-modal pre-training, achieving strong results across code understanding and generation benchmarks. code2vec \\cite{alon2019code2vec} demonstrated that AST path-based representations capture meaningful program properties at scale, complementing token-level approaches. More recently, CodeSage \\cite{zhang2024codesage} scaled bidirectional code encoders with a two-stage pipeline combining identifier deobfuscation and bimodal contrastive learning, achieving state-of-the-art code retrieval performance. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning---a fundamentally different application of structural information that operates at the repository level rather than the function level.\n\nBuilding on the success of Sentence-BERT \\cite{reimers2019sentencebert} in learning dense representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns. ContraCode \\cite{jain2021contracode} applies compiler-driven transformations to generate functionally equivalent program variants as positive pairs, training the encoder to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal (code-code) and bimodal (code-text) contrastive objectives, achieving strong results across code search benchmarks. SCodeR \\cite{li2022scoder} introduces soft-labeled contrastive pre-training that uses a teacher model to assign continuous similarity scores rather than binary labels, capturing graded code similarity. \\citet{ding2022programcontrasts} leverage program structure and functional attributes to construct contrastive pairs for learning code (dis)similarity representations. InferCode \\cite{bui2021infercode} takes a complementary self-supervised approach, learning code representations by predicting AST subtrees without requiring labeled pairs.\n\nThe recent shift toward decoder-only architectures has produced models such as StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, which achieve strong performance across code generation and understanding tasks. These models are increasingly adopted as backbone encoders for contrastive fine-tuning in code retrieval, though their pretrained representation geometries differ substantially from encoder-only predecessors---a factor that, as we show, interacts with negative mining strategy effectiveness.\n\nDespite the progress in pre-trained code representations and contrastive learning, these methods share a common dependency on negative sampling strategy yet few systematically investigate which negatives yield the best representations for code retrieval. Most approaches rely on in-batch negatives \\cite{karpukhin2020dpr} or random sampling, leaving the interaction between negative selection strategy and encoder representation geometry unexplored. Our work addresses this gap with a controlled comparison across negative mining strategies on modern decoder-only code encoders.\n\n## 2.3 Hard Negative Mining\n\nHard negative mining---selecting negative examples that are challenging for the current model---is well established for improving contrastive learning. In visual representation learning, SimCLR \\cite{chen2020simclr} demonstrates the importance of large batch sizes and hard negatives for learning discriminative features. In dense text retrieval, DPR \\cite{karpukhin2020dpr} shows that BM25-retrieved passages serve as effective hard negatives beyond in-batch sampling. ANCE \\cite{xiong2021ance} advances this by mining negatives from the model's own embedding space via approximate nearest neighbor search, achieving substantial gains over static BM25 negatives. STAR \\cite{zhan2021star} addresses the training instability of dynamic mining by jointly training the retriever with periodically refreshed hard negatives and a random negative stabilization mechanism. RocketQA \\cite{qu2021rocketqa} introduces a cross-encoder as a denoiser to filter false negatives from hard negative candidates, demonstrating that the quality of hard negatives matters as much as their difficulty. Curriculum-based approaches such as CL-DRD \\cite{zeng2022cldrd} progressively increase negative difficulty during training through knowledge distillation.\n\nIn the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \\cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining in structural code retrieval settings.\n\nOur work provides a systematic comparison that challenges the assumption that expensive gradient-based or dynamic hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation or periodic re-mining. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and observe that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry---an interaction that existing work does not examine.\n\n## 2.4 Code Structure Analysis\n\nOur structure-grounded negative mining pipeline builds upon established foundations in program analysis. The program dependence graph \\cite{ferrante1987pdg}, representing both control and data dependencies between program statements, provides the theoretical basis for inter-procedural data-flow analysis. Yamaguchi et al.\\ \\cite{yamaguchi2014cpg} introduced the code property graph, merging ASTs, control-flow graphs, and program dependence graphs into a unified queryable representation implemented in the Joern platform, primarily for vulnerability detection. Our pipeline leverages CodeQL \\cite{avgustinov2016ql}, which models codebases as relational databases queryable via a declarative object-oriented language, enabling scalable inter-procedural taint tracking across repository-scale codebases. While these tools have been primarily applied to vulnerability detection and program optimization, we repurpose inter-procedural data-flow analysis for a novel application: constructing structure-grounded hard negatives for contrastive code retrieval training.\n\nTogether, these four lines of work---code retrieval, contrastive code representation learning, hard negative mining, and code structure analysis---converge in our approach, which uses structural signals from program analysis to improve contrastive training for code retrieval, distinct from methods that apply structure at inference time or during pre-training.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-15T03:22:30.718571+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-15T03:22:30.718742+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read existing files and catalog current citations', 'status': 'completed', 'activeForm': 'Reading existing files and cataloging current citations'}, {'content': 'Verify new paper citations via WebSearch (3 agents running)', 'status': 'completed', 'activeForm': 'Verifying new paper citations via WebSearch'}, {'content': 'Verify remaining existing citations', 'status': 'completed', 'activeForm': 'Verifying remaining existing citations'}, {'content': 'Write expanded related_work_v1.md with 25+ citations', 'status': 'completed', 'activeForm': 'Writing expanded related_work_v1.md'}, {'content': 'Create references.bib with all citations', 'status': 'in_progress', 'activeForm': 'Creating references.bib'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read existing files and catalog current citations', 'status': 'completed', 'activeForm': 'Reading existing files and cataloging current citations'}, {'content': 'Verify new paper citations via WebSearch (3 agents running)', 'status': 'completed', 'activeForm': 'Verifying new paper citations via WebSearch'}, {'content': 'Verify remaining existing citations', 'status': 'completed', 'activeForm': 'Verifying remaining existing citations'}, {'content': 'Write expanded related_work_v1.md with 25+ citations', 'status': 'completed', 'activeForm': 'Writing expanded related_work_v1.md'}, {'content': 'Create references.bib with all citations', 'status': 'in_progress', 'activeForm': 'Creating references.bib'}]"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T03:22:30.718890+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T03:22:30.719040+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
  "content": "% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================\n\n@article{robertson2009bm25,\n  title={The Probabilistic Relevance Framework: {BM25} and Beyond},\n  author={Robertson, Stephen and Zaragoza, Hugo},\n  journal={Foundations and Trends in Information Retrieval},\n  volume={3},\n  number={4},\n  pages={333--389},\n  year={2009},\n  publisher={Now Publishers}\n}\n\n@inproceedings{karpukhin2020dpr,\n  title={Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Karpukhin, Vladimir and O{\\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={6769--6781},\n  year={2020}\n}\n\n@article{reddy2025swerank,\n  title={{SweRank}: Software Issue Localization with Code Ranking},\n  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},\n  journal={arXiv preprint arXiv:2505.07849},\n  year={2025}\n}\n\n@inproceedings{xie2025swefixer,\n  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},\n  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},\n  pages={1123--1139},\n  year={2025}\n}\n\n@inproceedings{chen2025locagent,\n  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},\n  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={8697--8727},\n  year={2025}\n}\n\n@article{shah2025ranger,\n  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},\n  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},\n  journal={arXiv preprint arXiv:2509.25257},\n  year={2025}\n}\n\n@inproceedings{liu2025codexgraph,\n  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},\n  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},\n  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages={142--160},\n  year={2025}\n}\n\n@inproceedings{ouyang2025repograph,\n  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},\n  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},\n  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@inproceedings{liu2024graphcoder,\n  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},\n  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},\n  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\n  year={2024}\n}\n\n@article{seddik2026arise,\n  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},\n  author={Seddik, Shahd and Fard, Fatemeh},\n  journal={arXiv preprint arXiv:2605.03117},\n  year={2026}\n}\n\n% =============================================================================\n% Section 2.2: Pre-trained Code Representations and Contrastive Learning\n% =============================================================================\n\n@inproceedings{feng2020codebert,\n  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n\n@inproceedings{guo2021graphcodebert,\n  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{guo2022unixcoder,\n  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={7212--7225},\n  year={2022}\n}\n\n@inproceedings{alon2019code2vec,\n  title={code2vec: Learning Distributed Representations of Code},\n  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},\n  booktitle={Proceedings of the ACM on Programming Languages (POPL)},\n  volume={3},\n  pages={1--29},\n  year={2019}\n}\n\n@inproceedings{zhang2024codesage,\n  title={Code Representation Learning At Scale},\n  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@inproceedings{reimers2019sentencebert,\n  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n  author={Reimers, Nils and Gurevych, Iryna},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={3982--3992},\n  year={2019}\n}\n\n@inproceedings{jain2021contracode,\n  title={Contrastive Code Representation Learning},\n  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={5954--5971},\n  year={2021}\n}\n\n@inproceedings{li2022coderetriever,\n  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={2898--2910},\n  year={2022}\n}\n\n@inproceedings{li2022scoder,\n  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},\n  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year={2022}\n}\n\n@inproceedings{ding2022programcontrasts,\n  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},\n  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={6300--6312},\n  year={2022}\n}\n\n@inproceedings{bui2021infercode,\n  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},\n  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},\n  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={1186--1197},\n  year={2021}\n}\n\n@article{lozhkov2024starcoder2,\n  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},\n  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},\n  journal={arXiv preprint arXiv:2402.19173},\n  year={2024}\n}\n\n@article{hui2024qwen25coder,\n  title={{Qwen2.5-Coder} Technical Report},\n  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},\n  journal={arXiv preprint arXiv:2409.12186},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.3: Hard Negative Mining\n% =============================================================================\n\n@inproceedings{chen2020simclr,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},\n  pages={1597--1607},\n  year={2020}\n}\n\n@inproceedings{xiong2021ance,\n  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},\n  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{zhan2021star,\n  title={Optimizing Dense Retrieval Model Training with Hard Negatives},\n  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},\n  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1503--1512},\n  year={2021}\n}\n\n@inproceedings{qu2021rocketqa,\n  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},\n  pages={5835--5847},\n  year={2021}\n}\n\n@inproceedings{zeng2022cldrd,\n  title={Curriculum Learning for Dense Retrieval Distillation},\n  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},\n  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1979--1983},\n  year={2022}\n}\n\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  year={2025},\n  publisher={ACM}\n}\n\n% =============================================================================\n% Section 2.4: Code Structure Analysis\n% =============================================================================\n\n@article{ferrante1987pdg,\n  title={The Program Dependence Graph and Its Use in Optimization},\n  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},\n  journal={ACM Transactions on Programming Languages and Systems},\n  volume={9},\n  number={3},\n  pages={319--349},\n  year={1987},\n  publisher={ACM}\n}\n\n@inproceedings{yamaguchi2014cpg,\n  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},\n  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},\n  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\\&P)},\n  pages={590--604},\n  year={2014},\n  publisher={IEEE}\n}\n\n@inproceedings{avgustinov2016ql,\n  title={{QL}: Object-oriented Queries on Relational Data},\n  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\\\"a}fer, Max},\n  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},\n  series={LIPIcs},\n  volume={56},\n  pages={2:1--2:25},\n  year={2016}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
    "content": "% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================\n\n@article{robertson2009bm25,\n  title={The Probabilistic Relevance Framework: {BM25} and Beyond},\n  author={Robertson, Stephen and Zaragoza, Hugo},\n  journal={Foundations and Trends in Information Retrieval},\n  volume={3},\n  number={4},\n  pages={333--389},\n  year={2009},\n  publisher={Now Publishers}\n}\n\n@inproceedings{karpukhin2020dpr,\n  title={Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Karpukhin, Vladimir and O{\\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={6769--6781},\n  year={2020}\n}\n\n@article{reddy2025swerank,\n  title={{SweRank}: Software Issue Localization with Code Ranking},\n  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},\n  journal={arXiv preprint arXiv:2505.07849},\n  year={2025}\n}\n\n@inproceedings{xie2025swefixer,\n  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},\n  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},\n  pages={1123--1139},\n  year={2025}\n}\n\n@inproceedings{chen2025locagent,\n  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},\n  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={8697--8727},\n  year={2025}\n}\n\n@article{shah2025ranger,\n  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},\n  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},\n  journal={arXiv preprint arXiv:2509.25257},\n  year={2025}\n}\n\n@inproceedings{liu2025codexgraph,\n  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},\n  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},\n  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages={142--160},\n  year={2025}\n}\n\n@inproceedings{ouyang2025repograph,\n  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},\n  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},\n  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@inproceedings{liu2024graphcoder,\n  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},\n  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},\n  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\n  year={2024}\n}\n\n@article{seddik2026arise,\n  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},\n  author={Seddik, Shahd and Fard, Fatemeh},\n  journal={arXiv preprint arXiv:2605.03117},\n  year={2026}\n}\n\n% =============================================================================\n% Section 2.2: Pre-trained Code Representations and Contrastive Learning\n% =============================================================================\n\n@inproceedings{feng2020codebert,\n  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n\n@inproceedings{guo2021graphcodebert,\n  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{guo2022unixcoder,\n  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={7212--7225},\n  year={2022}\n}\n\n@inproceedings{alon2019code2vec,\n  title={code2vec: Learning Distributed Representations of Code},\n  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},\n  booktitle={Proceedings of the ACM on Programming Languages (POPL)},\n  volume={3},\n  pages={1--29},\n  year={2019}\n}\n\n@inproceedings{zhang2024codesage,\n  title={Code Representation Learning At Scale},\n  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@inproceedings{reimers2019sentencebert,\n  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n  author={Reimers, Nils and Gurevych, Iryna},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={3982--3992},\n  year={2019}\n}\n\n@inproceedings{jain2021contracode,\n  title={Contrastive Code Representation Learning},\n  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={5954--5971},\n  year={2021}\n}\n\n@inproceedings{li2022coderetriever,\n  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={2898--2910},\n  year={2022}\n}\n\n@inproceedings{li2022scoder,\n  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},\n  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year={2022}\n}\n\n@inproceedings{ding2022programcontrasts,\n  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},\n  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={6300--6312},\n  year={2022}\n}\n\n@inproceedings{bui2021infercode,\n  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},\n  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},\n  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={1186--1197},\n  year={2021}\n}\n\n@article{lozhkov2024starcoder2,\n  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},\n  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},\n  journal={arXiv preprint arXiv:2402.19173},\n  year={2024}\n}\n\n@article{hui2024qwen25coder,\n  title={{Qwen2.5-Coder} Technical Report},\n  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},\n  journal={arXiv preprint arXiv:2409.12186},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.3: Hard Negative Mining\n% =============================================================================\n\n@inproceedings{chen2020simclr,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},\n  pages={1597--1607},\n  year={2020}\n}\n\n@inproceedings{xiong2021ance,\n  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},\n  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{zhan2021star,\n  title={Optimizing Dense Retrieval Model Training with Hard Negatives},\n  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},\n  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1503--1512},\n  year={2021}\n}\n\n@inproceedings{qu2021rocketqa,\n  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},\n  pages={5835--5847},\n  year={2021}\n}\n\n@inproceedings{zeng2022cldrd,\n  title={Curriculum Learning for Dense Retrieval Distillation},\n  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},\n  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1979--1983},\n  year={2022}\n}\n\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  year={2025},\n  publisher={ACM}\n}\n\n% =============================================================================\n% Section 2.4: Code Structure Analysis\n% =============================================================================\n\n@article{ferrante1987pdg,\n  title={The Program Dependence Graph and Its Use in Optimization},\n  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},\n  journal={ACM Transactions on Programming Languages and Systems},\n  volume={9},\n  number={3},\n  pages={319--349},\n  year={1987},\n  publisher={ACM}\n}\n\n@inproceedings{yamaguchi2014cpg,\n  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},\n  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},\n  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\\&P)},\n  pages={590--604},\n  year={2014},\n  publisher={IEEE}\n}\n\n@inproceedings{avgustinov2016ql,\n  title={{QL}: Object-oriented Queries on Relational Data},\n  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\\\"a}fer, Max},\n  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},\n  series={LIPIcs},\n  volume={56},\n  pages={2:1--2:25},\n  year={2016}\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T03:22:30.719291+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-15T03:22:30.719421+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read existing files and catalog current citations', 'status': 'completed', 'activeForm': 'Reading existing files and cataloging current citations'}, {'content': 'Verify new paper citations via WebSearch (3 agents running)', 'status': 'completed', 'activeForm': 'Verifying new paper citations via WebSearch'}, {'content': 'Verify remaining existing citations', 'status': 'completed', 'activeForm': 'Verifying remaining existing citations'}, {'content': 'Write expanded related_work_v1.md with 25+ citations', 'status': 'completed', 'activeForm': 'Writing expanded related_work_v1.md'}, {'content': 'Create references.bib with all citations', 'status': 'completed', 'activeForm': 'Creating references.bib'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read existing files and catalog current citations', 'status': 'completed', 'activeForm': 'Reading existing files and cataloging current citations'}, {'content': 'Verify new paper citations via WebSearch (3 agents running)', 'status': 'completed', 'activeForm': 'Verifying new paper citations via WebSearch'}, {'content': 'Verify remaining existing citations', 'status': 'completed', 'activeForm': 'Verifying remaining existing citations'}, {'content': 'Write expanded related_work_v1.md with 25+ citations', 'status': 'completed', 'activeForm': 'Writing expanded related_work_v1.md'}, {'content': 'Create references.bib with all citations', 'status': 'completed', 'activeForm': 'Creating references.bib'}]"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T03:22:30.719560+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_related-work-expand_20260515T031325",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-15T03:22:30.719741+00:00_

完成。

**扩展结果：20 → 32 独立引用**，分 4 个子节：

| 子节 | 引用数 | 新增 |
|------|--------|------|
| 2.1 Code Retrieval Methods | 10 | — (原有) |
| 2.2 Pre-trained Code Representations and Contrastive Learning | 14 | +7: CodeBERT, UniXcoder, CodeSage, SCodeR, InferCode, StarCoder2, Qwen2.5-Coder |
| 2.3 Hard Negative Mining | 7 | +2: STAR, RocketQA |
| 2.4 Code Structure Analysis (新) | 3 | +3: PDG, Joern/CPG, CodeQL |

新增子节 2.4 将 CodeQL、program dependence graph、code property graph 作为 StructFuse pipeline 的理论基础。Section 2.2 拆分为两部分：pre-trained code models 演进 + contrastive learning methods，并新增 decoder-only 模型段落（StarCoder2/Qwen2.5-Coder）呼应实验设置。Discussion 中的 6 个 inference-time graph methods 全部已在 2.1 中引用。

所有引用均经 WebSearch 验证 arXiv ID / 会议出处。`references.bib` 已创建，包含全部 32 条 bib 条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_write_related-work-expand_20260515T031325"
}
```

</details>

---
