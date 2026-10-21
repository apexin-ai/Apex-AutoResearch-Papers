# paper d044 section4 fixes

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_paper_d044_section4_fixes_20260516T101314.jsonl`
- **Structured JSON:** [`6d22e62ddcf5e75e53c9.json`](../../sessions/6d/6d22e62ddcf5e75e53c9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-16T10:14:58.215684+00:00_

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
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T10:14:58.216483+00:00_

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
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T10:14:58.216728+00:00_

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
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T10:14:58.217274+00:00_

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
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T10:14:58.217648+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "quasi-experimental",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Grep",
  "tool_args": {
    "pattern": "quasi-experimental",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T10:14:58.218004+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T10:14:58.218451+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "amplification|practical magnitude|r.*1\\.5",
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
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Grep",
  "tool_args": {
    "pattern": "amplification|practical magnitude|r.*1\\.5",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T10:14:58.218676+00:00_

docs/paper/related_work.tex:8:[Omitted long matching line]
docs/paper/acl.sty:239:\def\subsubsection{\@startsection{subsubsection}{3}{\z@}{-1.5ex plus
docs/paper/acl.sty:241:\def\paragraph{\@startsection{paragraph}{4}{\z@}{1.5ex plus
docs/paper/acl.sty:243:\def\subparagraph{\@startsection{subparagraph}{5}{\parindent}{1.5ex plus
docs/paper/acl.sty:260:\leftmarginiii 1.5em \leftmarginiv 1.0em \leftmarginv .5em \leftmarginvi .5em
docs/paper/acl.sty:287:% The choices were between 1-pt and 1.5-pt leading
docs/paper/main.tex:239:[Omitted long matching line]
docs/paper/main.tex:245:[Omitted long matching line]
docs/paper/main.log:150:Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
docs/paper/discussion.tex:8:For NER, merge amplification blocks naive decomposition (\S\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this. For RE, extending confusability-aware batching to broader benchmarks is a natural next step.
docs/paper/discussion.tex:13:[Omitted long matching line]
docs/paper/introduction.tex:12:[Omitted long matching line]
docs/paper/introduction.tex:19:    \item \textbf{Diagnosis to mitigation.} A diagnosis of schema decomposition feasibility: oracle routing recovers count-based degradation in RE (+29.8\,pp); confusability-aware grouping is inconclusive (+1.4\,pp, $p\approx 0.19$); NER decomposition fails due to merge amplification (\S\ref{sec:sdgd}).
docs/paper/results.tex:94:[Omitted long matching line]
docs/paper/main.aux:628:\@writefile{toc}{\contentsline {paragraph}{Merge amplification as the bottleneck.}{7}{section*.26}\protected@file@percent }
docs/paper/sdgd_negative.tex:6:\paragraph{Merge amplification as the bottleneck.}
docs/paper/sdgd_negative.tex:7:[Omitted long matching line]
docs/paper/sdgd_negative.tex:10:Merge amplification is specific to span-level tasks: each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assign
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T10:14:58.219077+00:00_

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
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T10:14:58.219257+00:00_

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
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T10:14:58.219407+00:00_

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
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T10:14:58.219557+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies implicitly assume different answers: \citet{uniner-2024} extract each type independently; \citet{llm-pee-2025} partition schemas by type embedding similarity; \citet{parse-2025} optimize schema definitions. None isolates \emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusabil
…[truncated 2905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T10:14:58.220169+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "We fix the type count and vary BCS to obtain controlled stratified comparison evidence. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for residual confounds from pool composition.",
  "new_string": "We fix the type count and vary BCS to obtain controlled stratified comparison evidence. Our design controls for count and pool composition. However, BCS-defined strata may differ in type frequency, definition quality, or prompt position---confounds we cannot fully rule out. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for residual confounds from pool composition."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "We fix the type count and vary BCS to obtain controlled stratified comparison evidence. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for residual confounds from pool composition.",
    "new_string": "We fix the type count and vary BCS to obtain controlled stratified comparison evidence. Our design controls for count and pool composition. However, BCS-defined strata may differ in type frequency, definition quality, or prompt position---confounds we cannot fully rule out. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for residual confounds from pool composition."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T10:14:58.220388+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T10:14:58.220524+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "likely reflecting DocRED's wider confusability range.",
  "new_string": "possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "likely reflecting DocRED's wider confusability range.",
    "new_string": "possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T10:14:58.220701+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T10:14:58.220830+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "Error taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 10^{-6}$) for RE. In RE, 100\\% of confusion errors are intra-batch and missed-entity rates remain flat (10--16\\%); in NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.",
  "new_string": "Error taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 10^{-6}$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "Error taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 10^{-6}$) for RE. In RE, 100\\% of confusion errors are intra-batch and missed-entity rates remain flat (10--16\\%); in NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.",
    "new_string": "Error taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy} in Appendix~\\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 10^{-6}$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T10:14:58.221054+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T10:14:58.221189+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the 31.2\\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience.",
  "new_string": "For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the 31.2\\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $r^2{=}1.5\\%$ aggregates to batch-level $R^2{=}22$--$53\\%$ across datasets, a 14--35$\\times$ amplification consistent with averaging over $\\sim\\binom{k}{2}$ correlated pair effects per batch."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the 31.2\\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience.",
    "new_string": "For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the 31.2\\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $r^2{=}1.5\\%$ aggregates to batch-level $R^2{=}22$--$53\\%$ across datasets, a 14--35$\\times$ amplification consistent with averaging over $\\sim\\binom{k}{2}$ correlated pair effects per batch."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T10:14:58.221375+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T10:14:58.221503+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\item \\textbf{Causal mechanism.} The study establishes correlational evidence; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway.",
  "new_string": "\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "old_string": "\\item \\textbf{Causal mechanism.} The study establishes correlational evidence; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway.",
    "new_string": "\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T10:14:58.221690+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T10:14:58.221835+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "69",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "69",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T10:14:58.221995+00:00_

69	\subsection{BCS-Controlled Experiments}
70	\label{sec:bcs_controlled}
71	
72	We fix the type count and vary BCS to obtain controlled stratified comparison evidence. Our design controls for count and pool composition. However, BCS-defined strata may differ in type frequency, definition quality, or prompt position---confounds we cannot fully rule out. Table~\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches; the within-pool analysis (\S\ref{sec:within_pool}) controls for residual confounds from pool composition.
73	
74	\begin{table}[t]
75	\centering
76	\small
77	\resizebox{\columnwidth}{!}{%
78	\begin{tabular}{lcrrrr}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T10:14:58.222117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "93",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "93",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T10:14:58.222237+00:00_

93	\paragraph{Document-level RE (DocRED).}
94	The effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\,pp at count 16 (slope $= -0.713$, $\rho = -0.661$, $p = 1.5 \times 10^{-5}$) and $-$17.6\,pp at count 32 (slope $= -0.690$, $\rho = -0.509$, $p = 0.002$). BCS explains 44--53\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.
95	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T10:14:58.222354+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "128",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "128",
    "limit": "6"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T10:14:58.222481+00:00_

128	\paragraph{Practical magnitude.}
129	\label{sec:practical_magnitude}
130	For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0])---roughly 7\% of the 31.2\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). The 31.2\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $r^2{=}1.5\%$ aggregates to batch-level $R^2{=}22$--$53\%$ across datasets, a 14--35$\times$ amplification consistent with averaging over $\sim\binom{k}{2}$ correlated pair effects per batch.
131	
132	\paragraph{Cross-model validation.}
133	The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap. Both models converge to $\approx$51\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\ref{tab:cross_model_bcs}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T10:14:58.223165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "139",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "139",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T10:14:58.223635+00:00_

139	\label{sec:multi_channel}
140	
141	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy} in Appendix~\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\rho = 1.0$ ($p < 0.001$) for NER and $\rho = 0.954$ ($p < 10^{-6}$) for RE. Under closed-set classification, non-\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches.
142	
143	These results establish two channels: \textbf{Channel~1} (count $\to$ recall decline) and \textbf{Channel~2} (confusability $\to$ type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T10:14:58.223799+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "47",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "47",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T10:14:58.224009+00:00_

47	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.
48	
49	\item \textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_section4_fixes_20260516T101314",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-16T10:14:58.224191+00:00_

所有修改完成。总结：

**修改文件和位置：**

| 文件 | 行号 | 修改内容 |
|------|------|----------|
| `results.tex` | 72 | **C1**: 添加 confound disclosure（BCS strata 可能因 type frequency/definition quality/prompt position 差异） |
| `results.tex` | 94 | **S8**: DocRED R² 归因从单一解释改为两个并列解释（wider confusability range + document-level context） |
| `results.tex` | 130 | **C2**: 在 Practical magnitude 段末加入 pair→batch 14–35× amplification 论证 |
| `results.tex` | 141 | **S10**: RE 100% intra-batch 降级为 tautology 说明 + 重新聚焦 IntraSub-SCS 相关性 |
| `main.tex` | 49 | **C1**: Limitations 第6条 "correlational" → "correlational with controlled stratification" |

**无需修改的项：**
- "quasi-experimental" 全文不存在，无需替换
- C3 的 80-rel null result 段落已在 results.tex:126 存在，无需新增

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_d044_section4_fixes_20260516T101314"
}
```

</details>

---
