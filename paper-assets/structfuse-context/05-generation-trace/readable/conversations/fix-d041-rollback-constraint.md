# fix d041 rollback constraint

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_fix_d041-rollback-constraint_20260515T022107.jsonl`
- **Structured JSON:** [`316ccf00e39a6af75207.json`](../../sessions/31/316ccf00e39a6af75207.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-15T02:22:39.782060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T02:22:39.782466+00:00_

1	# §3 Method
2	
3	## §3.1 Problem Formulation
4	
5	We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\mathcal{F} = \{f_1, f_2, \ldots, f_N\}$. The gold set $\mathcal{F}^+_q \subset \mathcal{F}$ denotes the files modified in the ground-truth patch.
6	
7	We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:
8	
9	$$\text{sim}(E_\theta(q), E_\theta(f^+)) \gg \text{sim}(E_\theta(q), E_\theta(f^-))$$
10	
11	where $\text{sim}(\cdot, \cdot)$ denotes cosine similarity.
12	
13	The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.
14	
15	## §3.2 Structural Information Extraction
16	
17	### CodeQL Bounded Data-Flow Analysis
18	
19	We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:
20	
21	- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.
22	- **Data-flow graph**: inter-procedural data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across 
…[truncated 9625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T02:22:39.782686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T02:22:39.782866+00:00_

1	# 1. Introduction
2	
3	Code retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \cite{liu2024repobench}, fault localization \cite{chen2025locagent}, and automated program repair \cite{jimenez2024swebench}.
4	Contrastive learning has become the dominant paradigm for training dense code retrievers \cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \cite{chen2020simclr,xiong2021ance}.
5	Despite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.
6	As retrieval scales to repository-level settings with hundreds of candidate files \cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.
7	
8	Existing negative selection approaches span a broad spectrum but leave a critical gap.
9	Random negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \cite{karpukhin2020dpr}.
10	Embedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.
11	CoCoHaNeRe \cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.
12	Meanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that 
…[truncated 3707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T02:22:39.783026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T02:22:39.783243+00:00_

1	# §4 Experiments
2	
3	## §4.1 Experimental Setup
4	
5	**Dataset.** We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \placeholder{34.3%} [pending recalc]. The remaining \placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.
6	
7	For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.
8	
9	**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \in \{1, 5, 10\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the c
…[truncated 14761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T02:22:39.783443+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "old_string": "$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.",
  "new_string": "$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "old_string": "$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.",
    "new_string": "$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T02:22:39.783654+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T02:22:39.783800+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "old_string": "Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query.",
  "new_string": "Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "old_string": "Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query.",
    "new_string": "Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T02:22:39.783965+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T02:22:39.784093+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "old_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
  "new_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "old_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "new_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T02:22:39.784253+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T02:22:39.784378+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "old_string": "dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.",
  "new_string": "dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
    "old_string": "dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.",
    "new_string": "dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T02:22:39.784518+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T02:22:39.784713+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "old_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
  "new_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
    "old_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "new_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T02:22:39.784872+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T02:22:39.784997+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4).",
  "new_string": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "old_string": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4).",
    "new_string": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4)."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T02:22:39.785173+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T02:22:39.785306+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
  "new_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "old_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "new_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T02:22:39.785478+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T02:22:39.785635+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "f ∈ R_G|f \\\\in \\\\mathcal\\{R\\}_G|structurally connected.*files.*ranked|structurally connected non-gold",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Grep",
  "tool_args": {
    "pattern": "f ∈ R_G|f \\\\in \\\\mathcal\\{R\\}_G|structurally connected.*files.*ranked|structurally connected non-gold",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T02:22:39.785774+00:00_

artifacts/paper_drafts/introduction_v1.md:30:3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.
artifacts/paper_drafts/introduction_v2.md:23:Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\% timeout rate and [TBD]\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T02:22:39.785908+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "f \\\\notin \\\\mathcal\\{R\\}_G|structurally disconnected|structurally \\*\\*disconnected\\*\\*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Grep",
  "tool_args": {
    "pattern": "f \\\\notin \\\\mathcal\\{R\\}_G|structurally disconnected|structurally \\*\\*disconnected\\*\\*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T02:22:39.786086+00:00_

artifacts/paper_drafts/method_v1.md:77:$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{BM25}(q, f)$$
artifacts/paper_drafts/method_v1.md:79:These files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.
artifacts/paper_drafts/method_v1.md:85:[Omitted long matching line]
artifacts/paper_drafts/experiments_v1.md:21:[Omitted long matching line]
artifacts/paper_drafts/introduction_v2.md:17:We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.
artifacts/paper_drafts/figure_design_v1.md:49:**Purpose**: Make the 3 strategies intuitive. Directly supports §3.4 and helps readers understand what "structurally disconnected but textually similar" means concretely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T02:22:39.786277+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "sim\\(E_\\\\theta_?0|embedding distance.*排序|argtop.*sim\\(E",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Grep",
  "tool_args": {
    "pattern": "sim\\(E_\\\\theta_?0|embedding distance.*排序|argtop.*sim\\(E",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T02:22:39.786407+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T02:22:39.786564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "offset": "69",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "offset": "69",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T02:22:39.786751+00:00_

69	### Dataflow-Aware Negatives
70	
71	This strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\mathcal{F}^+_q$, define the reachability set:
72	
73	$$\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$$
74	
75	where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:
76	
77	$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{BM25}(q, f)$$
78	
79	These files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.
80	
81	For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).
82	
83	### Difficulty Gradient
84	
85	The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).
86	
87	### Relationship to BM25 Baselines
88	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T02:22:39.786902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "offset": "14",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
    "offset": "14",
    "limit": "6"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T02:22:39.787030+00:00_

14	
15	We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.
16	Using CodeQL \cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.
17	We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.
18	All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T02:22:39.787154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "offset": "19",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "offset": "19",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T02:22:39.787281+00:00_

19	For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).
20	
21	**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.
22	
23	**Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-15T02:22:39.787455+00:00_

修改完成，验证结果：

| 检查项 | 状态 |
|--------|------|
| `f ∈ R_G` 作为 negative 选择约束 | 已消除（改为 `f \notin R_G(q)`） |
| "structurally connected" 作为 negative 描述 | 已改为 "structurally disconnected"（3个文件共5处） |
| BM25 排序 | 保留不变（无 `sim(E_θ0)` 回退） |
| D041 标记追加 | 3个文件均已追加 `回滚约束方向 2026-05-15` |

注：`introduction_v2.md:23` 中 "structurally connected non-gold rate" 是 Z% 统计指标（描述 connected 文件中 non-gold 的比例），不是 negative 选择方向，无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_d041-rollback-constraint_20260515T022107"
}
```

</details>

---
