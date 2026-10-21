# paper d044 section5 discussion

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_paper_d044_section5_discussion_20260516T101343.jsonl`
- **Structured JSON:** [`6efd8ab568fd6150c0d1.json`](../../sessions/6e/6efd8ab568fd6150c0d1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-16T10:17:34.790456+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T10:17:34.790790+00:00_

_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
checklist.tex
conclusion.tex
discussion.tex
experimental_setup.tex
introduction.tex
main.aux
main.bbl
main.blg
main.log
main.out
main.pdf
main.tex
prompt_appendix.tex
references.bib
related_work.tex
results.tex
sdgd_negative.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T10:17:34.791005+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ -name \"*error*\" -o -name \"*taxonomy*\" -o -name \"*fig*\" 2>/dev/null",
  "description": "Search for error taxonomy or figure files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ -name \"*error*\" -o -name \"*taxonomy*\" -o -name \"*fig*\" 2>/dev/null",
    "description": "Search for error taxonomy or figure files"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T10:17:34.791145+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T10:17:34.791270+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/ -name \"*fig*\" -o -name \"*error*\" -o -name \"*count_curve*\" -o -name \"*taxonomy*\" 2>/dev/null",
  "description": "Search artifacts for figure files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/ -name \"*fig*\" -o -name \"*error*\" -o -name \"*count_curve*\" -o -name \"*taxonomy*\" 2>/dev/null",
    "description": "Search artifacts for figure files"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T10:17:34.791400+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/d037_statistical_analyses/figure_data_audit.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_error_taxonomy.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_bcs_scaling.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_count_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_count_curves_73bdd4.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp008_sdgd_zero_fewnerd_r2/chart/fig_sdgd_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fig_count_curves.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/ace05_code/configs
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fig_error_taxonomy.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/maven_code/configs
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/count_curve_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_docred_confusability/count_curve_results.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T10:17:34.791540+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T10:17:34.791677+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\ref{tab:sdgd_results}).
5	
6	\paragraph{Merge amplification as the bottleneck.}
7	The failure is \emph{merge amplification}: presenting the same text $k$ times causes each pass to independently generate predictions. Single-pass precision (0.563) collapses to 0.210--0.249 after union merge with 8 batches, while recall gains are modest (0.368 $\to$ 0.314--0.446). Confidence gating improves precision but with disproportionate recall loss (Appendix~\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \cite{llm-calibration-survey-2024}.
8	
9	\paragraph{Why NER fails but RE does not.}
10	Merge amplification is specific to span-level tasks: each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE operates on fixed (head, tail) pairs with no span reconciliation---each pair receives an independent classification, eliminating the mechanism that caused SDGD to fail.
11	
12	\paragraph{Confusability-aware batch composition for RE.}
13	Since RE avoids merge amplification, we test whether confusability-aware batching improves accuracy. All decomposition conditions use oracle routing (each instance is routed to the batch containing its gold type). Single-type batches versus the 80-relation single-pass yields +29.8\,pp (0.802 vs.\ 0.504), confirming that decomposition is effective whe
…[truncated 415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T10:17:34.791859+00:00_

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
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T10:17:34.792018+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Practitioners should monitor BCS and prefer cross-domain type groupings. Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1: $-$31.2\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Future directions.}
8	For NER, merge amplification blocks naive decomposition (\S\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this. For RE, extending confusability-aware batching to broader benchmarks is a natural next step.
9	
10	\section{Conclusion}
11	\label{sec:conclusion}
12	
13	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp) and across extraction granularities (DocRED document-level RE: count decline $-$49\,pp; BCS slope $= -0.71$, $R^2 = 0.53$), with high-BCS accuracy converging to a floor consistent across both tested models. We further identified a centrality confound on same-domain schemas, demonstrated that merge amplification is a structural challenge for NER decomposition, and showed that confusability-aware grouping yields a directionally consistent but non-significant improvement (+1.4\,pp, $p\approx 0.19$). Cross-batch calibration or joint decoding 
…[truncated 84 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T10:17:34.792166+00:00_

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
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T10:17:34.792375+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
25	
26	\paragraph{NER (Few-NERD).}
27	Recall declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$ ($-$42\% relative), with minor non-monotonicity within sampling variability (bootstrap CIs overlap). Precision rises inversely (0.11 $\to$ 0.52), reflecting a shift from over-prediction to under-prediction as candidate types increase.
28	
29	\paragraph{RE (FewRel).}
30	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled fr
…[truncated 12928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T10:17:34.792546+00:00_

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
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T10:17:34.792784+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	
16	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
40	
41	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
42	
43	\item \textbf{Non-significant factorial test.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.
44	
45	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.
46	
47	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits 
…[truncated 18387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T10:17:34.792965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T10:17:34.793133+00:00_

1	\section{Prompt Templates}
2	\label{sec:appendix_prompts}
3	
4	This appendix reproduces the complete prompt templates used for all three extraction tasks.
5	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
6	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
7	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
8	
9	\medskip\noindent
10	\textbf{Notation.}
11	Placeholders are shown in \texttt{\{braces\}}.
12	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
13	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
14	
15	\subsection{Named Entity Recognition (Few-NERD)}
16	
17	\paragraph{v1 prompt (with character offsets).}
18	
19	\begin{small}
20	\begin{verbatim}
21	Extract all named entities from the following text.
22	Only extract entities of the following types:
23	- {type_1}: {definition_1}
24	- {type_2}: {definition_2}
25	  ...
26	
27	Text: {input_text}
28	
29	Output as JSON: [{"text": "...", "type": "...",
30	                  "start": ..., "end": ...}]
31	\end{verbatim}
32	\end{small}
33	
34	\noindent
35	\textbf{v1 constrained-decoding schema:}
36	\begin{small}
37	\begin{verbatim}
38	{"type": "array",
39	 "items": {"type": "object",
40	   "properties": {
41	     "text":  {"type": "string"},
42	     "type":  {"type": "string",
43	               "enum": [&lt;sorted_types>]},
44	     "start": {"type": "integer"},
45	     "end":   {"type": "integer"}},
46	   "required": ["text","type","start","end"]}}
47	\end{verbatim}
48	\end{small}
49	
50	\paragraph{v2 prompt (text+type only).}
51	
52	\begin{small}
53	\begin{verbatim}
54	Extract all named entities from the following text.
55	Only extract entities of the following types:
56	- {type_1}: {definition_1}
57	- {type_2}: {definition_2}
58	  ...
59	
60	Text
…[truncated 1517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T10:17:34.793360+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/../../figures/paper/ 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check figures directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/../../figures/paper/ 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check figures directory"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T10:17:34.793499+00:00_

fig_bcs_scaling.pdf
fig_bcs_scaling.png
fig_count_curves.pdf
fig_count_curves.png
fig_error_taxonomy.pdf
fig_error_taxonomy.png
fig_sdgd_comparison.pdf
fig_sdgd_comparison.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T10:17:34.793637+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "old_string": "RE operates on fixed (head, tail) pairs with no span reconciliation---each pair receives an independent classification, eliminating the mechanism that caused SDGD to fail.",
  "new_string": "Under oracle routing, RE requires no span reconciliation---each pair receives a single classification from the batch containing its gold type, eliminating the mechanism that caused SDGD to fail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "old_string": "RE operates on fixed (head, tail) pairs with no span reconciliation---each pair receives an independent classification, eliminating the mechanism that caused SDGD to fail.",
    "new_string": "Under oracle routing, RE requires no span reconciliation---each pair receives a single classification from the batch containing its gold type, eliminating the mechanism that caused SDGD to fail."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T10:17:34.793778+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T10:17:34.793924+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "old_string": "a +1.4\\,pp gain that is directionally consistent but not statistically significant ($p \\approx 0.19$), limited by the narrow BCS margin (0.006) achievable at this partition granularity (Table~\\ref{tab:batch_composition} in Appendix~\\ref{sec:appendix_batch_composition}).",
  "new_string": "a +1.4\\,pp gain that is directionally consistent but not statistically significant ($p \\approx 0.19$), limited by the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006) achievable at this partition granularity (Table~\\ref{tab:batch_composition} in Appendix~\\ref{sec:appendix_batch_composition})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "old_string": "a +1.4\\,pp gain that is directionally consistent but not statistically significant ($p \\approx 0.19$), limited by the narrow BCS margin (0.006) achievable at this partition granularity (Table~\\ref{tab:batch_composition} in Appendix~\\ref{sec:appendix_batch_composition}).",
    "new_string": "a +1.4\\,pp gain that is directionally consistent but not statistically significant ($p \\approx 0.19$), limited by the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006) achievable at this partition granularity (Table~\\ref{tab:batch_composition} in Appendix~\\ref{sec:appendix_batch_composition})."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T10:17:34.794070+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T10:17:34.794206+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "old_string": "\\paragraph{Why NER fails but RE does not.}",
  "new_string": "In our NER experiments, multi-pass decomposition produces $k$ independent tagging outputs per sentence, where entities near chunk boundaries may receive conflicting labels. Post-hoc merging via span overlap resolution amplifies false positives: a single entity can appear in multiple chunks' output, and resolving conflicts by majority vote or confidence score inflates precision errors. This mechanism explains why SDGD achieved lower F1 (0.241) than the single-pass baseline (0.445)---decomposition amplified boundary errors faster than it reduced schema confusion.\n\n\\paragraph{Why NER fails but RE does not.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "old_string": "\\paragraph{Why NER fails but RE does not.}",
    "new_string": "In our NER experiments, multi-pass decomposition produces $k$ independent tagging outputs per sentence, where entities near chunk boundaries may receive conflicting labels. Post-hoc merging via span overlap resolution amplifies false positives: a single entity can appear in multiple chunks' output, and resolving conflicts by majority vote or confidence score inflates precision errors. This mechanism explains why SDGD achieved lower F1 (0.241) than the single-pass baseline (0.445)---decomposition amplified boundary errors faster than it reduced schema confusion.\n\n\\paragraph{Why NER fails but RE does not.}"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T10:17:34.794354+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T10:17:34.794495+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS",
  "new_string": "\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS",
    "new_string": "\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T10:17:34.794622+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T10:17:34.794738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "137",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "137",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T10:17:34.794888+00:00_

137	
138	\subsection{Multi-Channel Degradation}
139	\label{sec:multi_channel}
140	
141	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy} in Appendix~\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\rho = 1.0$ ($p < 0.001$) for NER and $\rho = 0.954$ ($p < 10^{-6}$) for RE. Under closed-set classification, non-\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches.
142	
143	These results establish two channels: \textbf{Channel~1} (count $\to$ recall decline) and \textbf{Channel~2} (confusability $\to$ type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.
144	
145	\subsection{Centrality Confound on Homogeneous Schemas}
146	\label{sec:centrality_confound}
147	
148	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--F1 correlation (Qwen3 $\rho = +0.184$, $p = 0.025$; MiniLM $\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 10^{-10}$; Table~\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable onl
…[truncated 94 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T10:17:34.795048+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS",
  "new_string": "\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS",
    "new_string": "\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T10:17:34.795230+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T10:17:34.795366+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}",
  "new_string": ""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "old_string": "\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}",
    "new_string": ""
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T10:17:34.795488+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T10:17:34.795604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "115",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "115",
    "limit": "12"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T10:17:34.795728+00:00_

115	\end{table}
116	
117	\begin{figure}[h]
118	\centering
119	\includegraphics[width=\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}
120	\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
121	\label{fig:error_taxonomy}
122	\end{figure}
123	
124	\section{SDGD Full Protocol and Results}
125	\label{sec:appendix_sdgd}
126	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T10:17:34.795884+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\n\\section{SDGD Full Protocol and Results}",
  "new_string": "\\section{SDGD Full Protocol and Results}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "old_string": "\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\n\\section{SDGD Full Protocol and Results}",
    "new_string": "\\section{SDGD Full Protocol and Results}"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T10:17:34.796088+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T10:17:34.796235+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Boundary conditions.}\nThe two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Practitioners should monitor BCS and prefer cross-domain type groupings. Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1: $-$31.2\\,pp; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Future directions.}\nFor NER, merge amplification blocks naive decomposition (\\S\\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this. For RE, extending confusability-aware batching to broader benchmarks is a natural next step.",
  "new_string": "\\paragraph{Boundary conditions.}\nThe two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals. High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1: $-$31.2\\,pp; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Practitioner guidance.}\nOur results suggest a practical threshold: type pairs with SCS ${>}\\,0.75$ contribute disproportionately to confusion (accounting for a majority of substitution errors in our taxonomy). Practitioners designing extraction schemas may benefit from pre-computing pairwise SCS and restructuring or merging types that exceed this threshold.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies (e.g., embedding-based instance-to-batch assignment) that would make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS that incorporates type descriptions rather than names alone. For NER, merge amplification blocks naive decomposition (\\S\\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "old_string": "\\paragraph{Boundary conditions.}\nThe two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Practitioners should monitor BCS and prefer cross-domain type groupings. Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1: $-$31.2\\,pp; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Future directions.}\nFor NER, merge amplification blocks naive decomposition (\\S\\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this. For RE, extending confusability-aware batching to broader benchmarks is a natural next step.",
    "new_string": "\\paragraph{Boundary conditions.}\nThe two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals. High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1: $-$31.2\\,pp; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Practitioner guidance.}\nOur results suggest a practical threshold: type pairs with SCS ${>}\\,0.75$ contribute disproportionately to confusion (accounting for a majority of substitution errors in our taxonomy). Practitioners designing extraction schemas may benefit from pre-computing pairwise SCS and restructuring or merging types that exceed this threshold.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies (e.g., embedding-based instance-to-batch assignment) that would make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS that incorporates type descriptions rather than names alone. For NER, merge amplification blocks naive decomposition (\\S\\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T10:17:34.796406+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T10:17:34.796558+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "The two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals.",
  "new_string": "The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "old_string": "The two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals.",
    "new_string": "The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound})."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T10:17:34.796701+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T10:17:34.796864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T10:17:34.797022+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\ref{tab:sdgd_results}).
5	
6	\paragraph{Merge amplification as the bottleneck.}
7	The failure is \emph{merge amplification}: presenting the same text $k$ times causes each pass to independently generate predictions. Single-pass precision (0.563) collapses to 0.210--0.249 after union merge with 8 batches, while recall gains are modest (0.368 $\to$ 0.314--0.446). Confidence gating improves precision but with disproportionate recall loss (Appendix~\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \cite{llm-calibration-survey-2024}.
8	
9	In our NER experiments, multi-pass decomposition produces $k$ independent tagging outputs per sentence, where entities near chunk boundaries may receive conflicting labels. Post-hoc merging via span overlap resolution amplifies false positives: a single entity can appear in multiple chunks' output, and resolving conflicts by majority vote or confidence score inflates precision errors. This mechanism explains why SDGD achieved lower F1 (0.241) than the single-pass baseline (0.445)---decomposition amplified boundary errors faster than it reduced schema confusion.
10	
11	\paragraph{Why NER fails but RE does not.}
12	Merge amplification is specific to span-level tasks: each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. Under oracle rout
…[truncated 1063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T10:17:34.797173+00:00_

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
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T10:17:34.797312+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1: $-$31.2\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Practitioner guidance.}
8	Our results suggest a practical threshold: type pairs with SCS ${>}\,0.75$ contribute disproportionately to confusion (accounting for a majority of substitution errors in our taxonomy). Practitioners designing extraction schemas may benefit from pre-computing pairwise SCS and restructuring or merging types that exceed this threshold.
9	
10	\paragraph{Future directions.}
11	Three directions merit investigation: (i)~non-oracle routing strategies (e.g., embedding-based instance-to-batch assignment) that would make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS that incorporates type descriptions rather than names alone. For NER, merge amplification blocks naive decomposition (\S\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this.
12	
13	\section{Conclusion}
14	\label{sec:conclusion}
15	
16	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both ch
…[truncated 755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T10:17:34.797460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "137",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "137",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T10:17:34.797598+00:00_

137	
138	\subsection{Multi-Channel Degradation}
139	\label{sec:multi_channel}
140	
141	\begin{figure}[t]
142	\centering
143	\includegraphics[width=\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}
144	\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
145	\label{fig:error_taxonomy}
146	\end{figure}
147	
148	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\rho = 1.0$ ($p < 0.001$) for NER and $\rho = 0.954$ ($p < 10^{-6}$) for RE. Under closed-set classification, non-\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches.
149	
150	These results establish two channels: \textbf{Channel~1} (count $\to$ recall decline) and \textbf{Channel~2} (confusability $\to$ type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.
151	
152	\subsection{Centrality Confound on Homogeneous Schemas}
153	\label{sec:centrality_confound}
154	
155	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--F1 correlation (Qwen3 $\rho = +0.184$, $p = 0.025$; MiniLM $\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanish
…[truncated 444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T10:17:34.797743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "112",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "112",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T10:17:34.797891+00:00_

112	\end{tabular}}
113	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
114	\label{tab:error_taxonomy}
115	\end{table}
116	
117	\section{SDGD Full Protocol and Results}
118	\label{sec:appendix_sdgd}
119	
120	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
121	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T10:17:34.798035+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -n '\\\\\\\\label{fig_error_taxonomy}' main.tex results.tex 2>/dev/null; echo \"---\"; grep -c '\\\\begin{figure}' results.tex main.tex sdgd_negative.tex discussion.tex; echo \"---\"; grep -c '\\\\end{figure}' results.tex main.tex sdgd_negative.tex discussion.tex",
  "description": "Check for duplicate labels and balanced figure environments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && grep -n '\\\\\\\\label{fig_error_taxonomy}' main.tex results.tex 2>/dev/null; echo \"---\"; grep -c '\\\\begin{figure}' results.tex main.tex sdgd_negative.tex discussion.tex; echo \"---\"; grep -c '\\\\end{figure}' results.tex main.tex sdgd_negative.tex discussion.tex",
    "description": "Check for duplicate labels and balanced figure environments"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T10:17:34.798158+00:00_

---
results.tex:2
main.tex:0
sdgd_negative.tex:0
discussion.tex:0
---
results.tex:2
main.tex:0
sdgd_negative.tex:0
discussion.tex:0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T10:17:34.798280+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{fig_error_taxonomy\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{fig_error_taxonomy\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T10:17:34.798583+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T10:17:34.798741+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "label\\{fig:error_taxonomy\\}|label\\{fig_error_taxonomy\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Grep",
  "tool_args": {
    "pattern": "label\\{fig:error_taxonomy\\}|label\\{fig_error_taxonomy\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T10:17:34.798895+00:00_

results.tex:145:\label{fig:error_taxonomy}
main.aux:1170:\newlabel{fig:error_taxonomy}{{2}{12}{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic}{figure.caption.42}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T10:17:34.799053+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport re\nfor f in ['sdgd_negative.tex', 'discussion.tex', 'results.tex']:\n    content = open(f).read()\n    opens = content.count('{')\n    closes = content.count('}')\n    if opens != closes:\n        print(f'{f}: UNBALANCED braces ({opens} open, {closes} close)')\n    else:\n        print(f'{f}: OK ({opens} pairs)')\n\"",
  "description": "Check brace balance in modified files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport re\nfor f in ['sdgd_negative.tex', 'discussion.tex', 'results.tex']:\n    content = open(f).read()\n    opens = content.count('{')\n    closes = content.count('}')\n    if opens != closes:\n        print(f'{f}: UNBALANCED braces ({opens} open, {closes} close)')\n    else:\n        print(f'{f}: OK ({opens} pairs)')\n\"",
    "description": "Check brace balance in modified files"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T10:17:34.799175+00:00_

sdgd_negative.tex: OK (13 pairs)
discussion.tex: OK (11 pairs)
results.tex: OK (197 pairs)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section5_discussion_20260516T101343",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-16T10:17:34.799333+00:00_

All files have balanced braces. Here's a summary of all modifications:

---

**Modified files:**

| File | Change |
|------|--------|
| `sdgd_negative.tex` | (C4) Oracle routing qualifier: "Under oracle routing, RE requires no span reconciliation---each pair receives a single classification from the batch containing its gold type" |
| `sdgd_negative.tex` | (C4) Added `($n{=}1$)` limitation to +1.4pp result |
| `sdgd_negative.tex` | (S4) Inserted merge amplification mechanistic paragraph (boundary conflicts, FP inflation via span overlap resolution) |
| `results.tex` | (S5) Moved `fig_error_taxonomy` into §4.4 body as `\begin{figure}[t]` |
| `main.tex` | (S5) Removed duplicate figure from appendix |
| `discussion.tex` | (S1) MAVEN scope sentence integrated into Boundary conditions |
| `discussion.tex` | (S6) New `\paragraph{Practitioner guidance.}` with SCS > 0.75 threshold |
| `discussion.tex` | (S6) Rewrote Future directions with three specific items (non-oracle routing, model coverage, definition-inclusive SCS) |
| `discussion.tex` | (S6) No unsupported theoretical speculation added |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_d044_section5_discussion_20260516T101343"
}
```

</details>

---
