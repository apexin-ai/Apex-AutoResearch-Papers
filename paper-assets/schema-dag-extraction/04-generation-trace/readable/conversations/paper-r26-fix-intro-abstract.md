# paper r26 fix intro abstract

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_paper_r26_fix_intro_abstract_20260522T043723.jsonl`
- **Structured JSON:** [`e67490849831b0acf6bb.json`](../../sessions/e6/e67490849831b0acf6bb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-22T04:39:13.913609+00:00_

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
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
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

_source line 2 · 2026-05-22T04:39:13.914156+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T04:39:13.914342+00:00_

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
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
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

_source line 4 · 2026-05-22T04:39:13.914486+00:00_

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
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T04:39:13.914636+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T04:39:13.914767+00:00_

1	\begin{abstract}
2	Schema complexity affects training-free LLM information extraction through two independent dimensions: type count drives recall decline, while inter-type confusability drives type substitution errors. We present what is, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across NER, RE, and event detection on four datasets. Using embedding-based confusability metrics (SCS/BCS) with controlled batch design, we find:
3	(1)~count degradation spans all three tasks (up to $-$49\,pp); confusability-driven substitution is documented primarily in RE, with bounded interaction;
4	(2)~BCS explains ${\sim}$22\% of cross-batch RE accuracy variance on FewRel (ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;
5	(3)~schema decomposition fails due to merge amplification and routing failure, though oracle routing confirms the two dimensions are independently addressable.
6	\end{abstract}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T04:39:13.915086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T04:39:13.915265+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1
5	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
6	
7	\looseness=-1
8	What explains this degradation? Prior decomposition strategies \citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
9	
10	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
11	
12	We ask three questions. \textbf{RQ1}: Does type
…[truncated 3215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T04:39:13.915415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T04:39:13.915913+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	All experiments use Qwen3-32B and the v1 prompt (\S\ref{sec:model}; Appendix~\ref{sec:appendix_prompts}) unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model.
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where eliminating type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count decline replicates on LLaMA-70B with comparable magnitude and on Gemini Flash (Appendix~\ref{sec:appendix_cross_model_gemini}). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
10	
11	\subsection{Pairwise Confusability and Type Confusion}
12	\label{sec:pairwise}
13	
14	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\
…[truncated 12725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T04:39:13.916134+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T04:39:13.916284+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions and mechanisms.}
5	\looseness=-1
6	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). RE effects replicate across three open-weight models (8B--70B), two formats, five prompts, and two datasets; no NER BCS effect detected across three models (8B--70B). At the type-pair level, confusability explains ${\sim}$1.3\% of variance---individually modest---but practitioners deploy full schemas as batches, where correlated pairwise effects compound. Batch-level $R^2 {\approx}\, 22\%$ on FewRel corresponds to a ${\sim}$31\,pp gap between extreme batches, the relevant practical construct for real-world zero-shot IE. The NER--RE asymmetry reflects different error-mode structures (\S\ref{sec:multi_channel}) and compressed BCS variance (Appendix~\ref{sec:appendix_ner_power}).
7	
8	\paragraph{Practical implications and conclusion.}
9	\label{sec:conclusion}
10	\looseness=-1
11	For NER, reducing candidate types is the primary lever. For RE, BCS enables pre-hoc diagnostics (flag SCS${}\,>\,0.85$ pairs; $R^2 {\approx}\, 0.22$ on FewRel); high-SCS pairs dominate type substitution errors (Appendix~\ref{app:error-analysis}). Practitioners can pre-compute SCS to identify high-risk type pairs before deployment, enabling schema-aware pool selection as a preprocessing step. Decompose-then-merge fails (\S\ref{sec:sdgd}), but oracle routing recovers accuracy (72.4\% vs.\ 50.4\%), confirming that count and confusability are independently addressable.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T04:39:13.916450+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "drives",
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
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Grep",
  "tool_args": {
    "pattern": "drives",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T04:39:13.916576+00:00_

docs/paper/abstract.tex:2:Schema complexity affects training-free LLM information extraction through two independent dimensions: type count drives recall decline, while inter-type confusability drives type substitution errors. We present what is, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across NER, RE, and event detection on four datasets. Using embedding-based confusability metrics (SCS/BCS) with controlled batch design, we find:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T04:39:13.916705+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "first controlled study",
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
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Grep",
  "tool_args": {
    "pattern": "first controlled study",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T04:39:13.916827+00:00_

docs/paper/abstract.tex:2:Schema complexity affects training-free LLM information extraction through two independent dimensions: type count drives recall decline, while inter-type confusability drives type substitution errors. We present what is, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across NER, RE, and event detection on four datasets. Using embedding-based confusability metrics (SCS/BCS) with controlled batch design, we find:
docs/paper/introduction.tex:15:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T04:39:13.917075+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "drives",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Grep",
  "tool_args": {
    "pattern": "drives",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T04:39:13.917209+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T04:39:13.917326+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "drives",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Grep",
  "tool_args": {
    "pattern": "drives",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T04:39:13.917443+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T04:39:13.917554+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "drives",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Grep",
  "tool_args": {
    "pattern": "drives",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T04:39:13.917665+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T04:39:13.917787+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "old_string": "while inter-type confusability drives type substitution errors.",
  "new_string": "while inter-type confusability predicts type substitution errors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "old_string": "while inter-type confusability drives type substitution errors.",
    "new_string": "while inter-type confusability predicts type substitution errors."
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T04:39:13.918041+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T04:39:13.918634+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "old_string": "confusability-driven substitution is documented primarily in RE, with bounded interaction;",
  "new_string": "inter-type confusability (measured by BCS) predicts type substitution errors in RE ($R^2 \\approx 0.22$ on FewRel, VIF${}\\,=\\,1.18$); the batch-level BCS signal is not detected in NER at current statistical power;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "old_string": "confusability-driven substitution is documented primarily in RE, with bounded interaction;",
    "new_string": "inter-type confusability (measured by BCS) predicts type substitution errors in RE ($R^2 \\approx 0.22$ on FewRel, VIF${}\\,=\\,1.18$); the batch-level BCS signal is not detected in NER at current statistical power;"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T04:39:13.918927+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T04:39:13.919095+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "independently predicts type substitution errors in RE, explaining",
  "new_string": "independently predicts type substitution errors in RE (on FewRel where confusability is not confounded with centrality, VIF${}\\,=\\,1.18$), explaining"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "old_string": "independently predicts type substitution errors in RE, explaining",
    "new_string": "independently predicts type substitution errors in RE (on FewRel where confusability is not confounded with centrality, VIF${}\\,=\\,1.18$), explaining"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T04:39:13.919247+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T04:39:13.919375+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE",
  "new_string": "the first controlled study simultaneously isolating type count and inter-type confusability as independent dimensions via embedding-based metrics and stratified batch design in zero-shot LLM IE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "old_string": "the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE",
    "new_string": "the first controlled study simultaneously isolating type count and inter-type confusability as independent dimensions via embedding-based metrics and stratified batch design in zero-shot LLM IE"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T04:39:13.919564+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T04:39:13.919730+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T04:39:13.920142+00:00_

1	\begin{abstract}
2	Schema complexity affects training-free LLM information extraction through two independent dimensions: type count drives recall decline, while inter-type confusability predicts type substitution errors. We present what is, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across NER, RE, and event detection on four datasets. Using embedding-based confusability metrics (SCS/BCS) with controlled batch design, we find:
3	(1)~count degradation spans all three tasks (up to $-$49\,pp); inter-type confusability (measured by BCS) predicts type substitution errors in RE ($R^2 \approx 0.22$ on FewRel, VIF${}\,=\,1.18$); the batch-level BCS signal is not detected in NER at current statistical power;
4	(2)~BCS explains ${\sim}$22\% of cross-batch RE accuracy variance on FewRel (ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;
5	(3)~schema decomposition fails due to merge amplification and routing failure, though oracle routing confirms the two dimensions are independently addressable.
6	\end{abstract}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T04:39:13.920340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "offset": "14",
  "limit": "14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "offset": "14",
    "limit": "14"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T04:39:13.920494+00:00_

14	\looseness=-1
15	To our knowledge, we present the first controlled study simultaneously isolating type count and inter-type confusability as independent dimensions via embedding-based metrics and stratified batch design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We quantify confusability using pairwise embedding similarity, the \emph{Schema Confusability Score} (SCS), and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, and MAVEN \citep{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}).
16	
17	Our experiments yield four findings:
18	(1)~Degradation operates along two dimensions with bounded interaction: count-related recall decline (up to $-$49\,pp) and confusability-related type substitution, confirmed on sentence- and document-level RE (\S\ref{sec:count_curves}, \S\ref{sec:multi_channel}).
19	(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\S\ref{sec:pairwise}); at batch level, BCS predicts RE accuracy independent of output format (\S\ref{sec:bcs_controlled}) but not NER accuracy at current statistical power; per-type aggregation is confounded by centrality on homogeneous schemas (\S\ref{sec:centrality_confound}).
20	(3)~RE effects are consistent across schema sizes, prompt designs, and three open-weight model families (8B--70B); Gemini Flash provides partial but fragile corroboration. The NER null is not detected on three models (8B--70B; \S\ref{sec:bcs_controlled}).
21	(4)~Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), despite oracle routing recovering substantial accuracy (\S\ref{sec:sdgd}).
22	Our contributions are:
23	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
24	    \item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \citealt{llm-pee-2025}), independently predicts type substitutio
…[truncated 1109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-22T04:39:13.920678+00:00_

All edits applied successfully. Here's the modification summary:

| # | 文件 | 行号 | 修改前 | 修改后 | Task |
|---|------|------|--------|--------|------|
| 1 | `abstract.tex` | 2 | `while inter-type confusability drives type substitution errors.` | `while inter-type confusability predicts type substitution errors.` | T1 |
| 2 | `abstract.tex` | 3 | `confusability-driven substitution is documented primarily in RE, with bounded interaction;` | `inter-type confusability (measured by BCS) predicts type substitution errors in RE ($R^2 \approx 0.22$ on FewRel, VIF${}\,=\,1.18$); the batch-level BCS signal is not detected in NER at current statistical power;` | T2 |
| 3 | `introduction.tex` | 24 | `independently predicts type substitution errors in RE, explaining` | `independently predicts type substitution errors in RE (on FewRel where confusability is not confounded with centrality, VIF${}\,=\,1.18$), explaining` | T2 |
| 4 | `introduction.tex` | 15 | `the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE` | `the first controlled study simultaneously isolating type count and inter-type confusability as independent dimensions via embedding-based metrics and stratified batch design in zero-shot LLM IE` | T6 |

说明：
- Task 1 仅有 1 处 confusability 相关 "drives"（abstract.tex:2）。`related_work.tex`、`results.tex`、`discussion.tex`、`sdgd_negative.tex`、`supplementary.tex` 中无 "drives"。Abstract 中 "type count drives recall decline" 保留未动（count 有更强因果支持）。
- Task 2 Abstract (1) 项重写为带 R²/VIF 数值的精确限定；Introduction Contribution #1 加括号限定 FewRel+VIF。
- Task 6 Introduction "first controlled study" 扩展为完整限定语。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_r26_fix_intro_abstract_20260522T043723"
}
```

</details>

---
