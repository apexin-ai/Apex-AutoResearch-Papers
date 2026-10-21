# paper r26 fix related work

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_r26_fix_related_work_20260522T043743.jsonl`
- **Structured JSON:** [`4db5a0483fccfd0d3ef7.json`](../../sessions/4d/4db5a0483fccfd0d3ef7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-22T04:39:34.722325+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T04:39:34.722747+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T04:39:34.723022+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T04:39:34.723315+00:00_

artifacts/dream_reports/dream_20260515T053106/best/paper.tex
artifacts/dream_reports/dream_20260515T053106/median/paper.tex
artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
artifacts/dream_reports/dream_20260515T113743/best/paper.tex
artifacts/dream_reports/dream_20260515T113743/median/paper.tex
artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
artifacts/dream_reports/dream_20260515T140829/best/paper.tex
artifacts/dream_reports/dream_20260515T140829/median/paper.tex
artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
artifacts/_project/paper/dataset_stats.tex
artifacts/paper/tables/dataset_stats.tex
artifacts/_project/paper/sdgd_negative.tex
artifacts/_project/paper/experimental_setup.tex
docs/paper/conclusion.tex
artifacts/_project/paper/results.tex
artifacts/dream_reports/dream_20260516T073533/best/paper.tex
artifacts/dream_reports/dream_20260516T073533/median/paper.tex
artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
docs/paper/supplementary.tex
artifacts/acknowledgements_draft.tex
docs/paper/prompt_appendix.tex
docs/paper/checklist.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/experimental_setup.tex
artifacts/error_taxonomy_cross_model_table.tex
artifacts/permutation_equivalence_latex.tex
docs/paper/sdgd_negative.tex
docs/paper/related_work.tex
docs/paper/results.tex
docs/paper/discussion.tex
docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T04:39:34.723477+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T04:39:34.723630+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	\looseness=-1
6	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, and bidirectional encoders \citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \citep{relationprompt-2022}, constrained generation \citep{josifoski-2022-genie}, and shared embedding spaces \citep{boylan-2025-glirel,wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.
7	
8	\paragraph{Schema complexity in IE.}
9	\looseness=-1
10	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21; \S\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches address schema complexity via hard negative mining \citep{iepile-2024}, schema definition optimization \citep{parse-2025}, multi-agent debate \citep{crossagentie-2025,cma
…[truncated 2068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T04:39:34.723923+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T04:39:34.724067+00:00_

File content (26055 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T04:39:34.724218+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\subsection|\\\\paragraph.*SCS|\\\\paragraph.*BCS|\\\\paragraph.*Confus|Schema Confusability|Batch Confusability",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\subsection|\\\\paragraph.*SCS|\\\\paragraph.*BCS|\\\\paragraph.*Confus|Schema Confusability|Batch Confusability",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T04:39:34.724374+00:00_

docs/paper/related_work.tex:16:\paragraph{SCS novelty.}
docs/paper/acl.sty:236:\def\subsection{\@startsection{subsection}{2}{\z@}{-1.8ex plus
docs/paper/main.tex:199:\subsection{Practical Routing Strategies on RE}
docs/paper/main.tex:308:\subsection{Partial Correlation: Controlling for Degree Centrality}
docs/paper/main.tex:330:\subsection{NER BCS-Null Power Analysis}
docs/paper/main.tex:373:\subsection{Cross-Prompt-Variant BCS Correlation}
docs/paper/main.tex:404:We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\ref{tab:bcs_aggregation}).
docs/paper/main.tex:583:[Omitted long matching line]
docs/paper/main.tex:639:\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\beta_{\text{BCS}} = -0.416$, $p < 0.001$ (vs.\ $\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\beta_{\text{origin}} = -0.057$, $p = 0.245$), and $\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.
docs/paper/main.tex:739:\paragraph{Dimension~2: BCS-controlled confusability.}
docs/paper/main.tex:797:[Omitted long matching line]
docs/paper/main.tex:820:[Omitted long matching line]
docs/paper/checklist.tex:5:\subsection*{A \quad For Every Submission}
docs/paper/checklist.tex:27:\subsection*{B \quad Scientific Artifacts}
docs/paper/checklist.tex:57:\subsection*{C \quad Computational Experiments}
docs/paper/checklist.tex:79:\subsection*{D \quad Human Annotators or Crowdworkers}
docs/paper/checklist.tex:105:\subsection*{E \quad AI-Assisted Research}
docs/paper/prompt_appendix.tex:22:\subsection{Named Entit
…[truncated 2366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T04:39:34.724525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "offset": "41",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "offset": "41",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T04:39:34.724677+00:00_

41	\subsection{Schema Confusability Score (SCS)}
42	\label{sec:scs}
43	
44	\looseness=-1
45	We define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
46	{\small
47	\[
48	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
49	\]
50	}
51	
52	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
53	\[
54	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
55	\]
56	
57	We use two embeddings to provide complementary perspectives: Qwen3 captures the extraction model's own type representations (self-similarity), while MiniLM provides an independent general-purpose baseline. Cross-embedding consistency holds on all datasets (Appendix~\ref{sec:appendix_bcs_sensitivity}); MiniLM consistently yields equal or stronger correlations, which confirms that Qwen3-based estimates are conservative. We compute SCS with: (1)~Qwen3-32B \citep{qwen3-2025} hidden-state representations (5{,}120-d) and (2)~all-MiniLM-L6-v2 \citep{minilm-2020,sentence-bert-2019}, a 384-d sentence encoder. Few-NERD uses Qwen3 because its fine-grained same-category pairs (e.g., ``person-artist'' vs.\ ``person-actor'') require the higher-dimensional space. MiniLM is the primary BCS embedding because sentence-transformers are trained for semantic similarity \citep{sentence-bert-2019}; Qwen3 causal-LM states show compressed BCS range (std${}\,=\,0.034$ vs.\ MiniLM std${}\,=\,0.081$), consistent with autoregressive anisotropy \citep{ethayarajh-contextual-2019}. Name-only SCS yields equivalent predictive accuracy to name+definition ($\Delta r$: $-0.023$ to $+0.035$; Appendix~\ref{app:scs-ablation}).
58	
59	\
…[truncated 1424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T04:39:34.725248+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "old_string": "SCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. The metric is a means; the empirical findings are the contribution",
  "new_string": "SCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "old_string": "SCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. The metric is a means; the empirical findings are the contribution",
    "new_string": "SCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T04:39:34.725470+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T04:39:34.725756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "offset": "16",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "offset": "16",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T04:39:34.725959+00:00_

16	\paragraph{SCS novelty.}
17	\looseness=-1
18	SCS inherits the embedding-similarity criterion from LLM-PEE \citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \citep{snell2017prototypical} and zero-shot classification \citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\%) compounds at the ecological batch level to explain ${\sim}$22\% of cross-batch RE variance on FewRel (\S\ref{sec:bcs_controlled}).
19	
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_related_work_20260522T043743",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-22T04:39:34.726158+00:00_

修改完成。

**文件**: `docs/paper/related_work.tex:18`

**插入位置**: "SCS novelty" 段落第一句之后，第二句（"The metric is a means..."）之前。

**新增内容**（1 句）:
> Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy.

覆盖了三个要点：
1. LLM-PEE 用 similarity 做 partition engineering vs. 我们做 prediction/analysis
2. BCS = MEAN（averages all pairwise SCS）
3. 与后续已有文字（"The metric is a means; the empirical findings are the contribution, enabled by ... BCS-controlled batches that isolate confusability from count"）衔接，共同强调贡献是 controlled experimental design 而非 metric 本身

未添加第二句"The contribution is not the metric itself but the controlled batch design..."，因为紧跟的已有文字已表达相同含义，避免冗余。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_r26_fix_related_work_20260522T043743"
}
```

</details>

---
