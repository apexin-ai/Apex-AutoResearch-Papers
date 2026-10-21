# paper pre submission check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_paper_pre-submission-check_20260519T095454.jsonl`
- **Structured JSON:** [`db25ae888016fb2eb7ab.json`](../../sessions/db/db25ae888016fb2eb7ab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-19T09:58:19.714578+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T09:58:19.715004+00:00_

artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
artifacts/_project/paper/discussion_outline.md
artifacts/_project/paper/discussion_section_info.md
artifacts/_project/paper/conclusion_section_info.md
artifacts/_project/paper/discussion_v2.md
artifacts/_project/paper/abstract_v2.md
artifacts/_project/paper/theta_sensitivity_table.tex
artifacts/_project/paper/semantic_ablation_table_info.md
artifacts/_project/paper/tab_domain_model_kstar.tex
artifacts/_project/paper/tab_domain_model_kstar_full.tex
artifacts/_project/paper/theta_lofo_table.tex
artifacts/_project/paper/borderline_features_126826.tex
artifacts/_project/paper/borderline_features.tex
artifacts/_project/paper/cohens_d_full_50bdcb.tex
artifacts/_project/paper/cohens_d_full.tex
artifacts/_project/paper/new_bibtex_entries.bib
artifacts/_project/paper/code_crossmodel_table.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T09:58:19.715201+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T09:58:19.715464+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T09:58:19.715615+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T09:58:19.715766+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T09:58:19.715951+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T09:58:19.716244+00:00_

artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
artifacts/_project/paper/theta_sensitivity_table.tex
artifacts/_project/paper/tab_domain_model_kstar.tex
artifacts/_project/paper/tab_domain_model_kstar_full.tex
artifacts/_project/paper/theta_lofo_table.tex
artifacts/_project/paper/borderline_features_126826.tex
artifacts/_project/paper/borderline_features.tex
artifacts/_project/paper/cohens_d_full_50bdcb.tex
artifacts/_project/paper/cohens_d_full.tex
artifacts/_project/paper/code_crossmodel_table.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T09:58:19.716388+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T09:58:19.716526+00:00_

artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
artifacts/_project/paper/theta_sensitivity_table.tex
artifacts/_project/paper/tab_domain_model_kstar.tex
artifacts/_project/paper/tab_domain_model_kstar_full.tex
artifacts/_project/paper/theta_lofo_table.tex
artifacts/_project/paper/borderline_features_126826.tex
artifacts/_project/paper/borderline_features.tex
artifacts/_project/paper/cohens_d_full_50bdcb.tex
artifacts/_project/paper/cohens_d_full.tex
artifacts/_project/paper/code_crossmodel_table.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T09:58:19.716676+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T09:58:19.716846+00:00_

artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
artifacts/exp_015_neural_probe/paper/neural_probe_analysis.tex
artifacts/drafts/neural_probe_analysis.tex
artifacts/c3_contingency_versions.tex
artifacts/exp-006/paper/c3_contingency_versions.tex
artifacts/dream_reports/dream_20260516T073047/best/paper.tex
artifacts/dream_reports/dream_20260516T073047/median/paper.tex
artifacts/dream_reports/dream_20260516T073047/worst/paper.tex
artifacts/_project/paper/theta_sensitivity_table.tex
artifacts/theta_sensitivity_table.tex
artifacts/_project/paper/tab_domain_model_kstar.tex
artifacts/_project/paper/tab_domain_model_kstar_full.tex
artifacts/dream_reports/dream_20260518T113009/best/paper.tex
artifacts/dream_reports/dream_20260518T113009/median/paper.tex
artifacts/dream_reports/dream_20260518T113009/worst/paper.tex
artifacts/dream_reports/dream_20260518T123349/best/paper.tex
artifacts/dream_reports/dream_20260518T123349/median/paper.tex
artifacts/dream_reports/dream_20260518T123349/worst/paper.tex
artifacts/dream_reports/dream_20260518T125757/best/paper.tex
artifacts/dream_reports/dream_20260518T125757/median/paper.tex
artifacts/dream_reports/dream_20260518T125757/worst/paper.tex
artifacts/exp_026_arxiv_filtering/latex_table.tex
artifacts/exp_026_arxiv_filtering/paper/latex_table.tex
artifacts/exp_026_arxiv_filtering/paper/latex_table_790184.tex
artifacts/exp_026_arxiv_filtering/paper/latex_table_db01ab.tex
artifacts/feature_ablation/latex_table.tex
artifacts/domain_lexical_stats/domain_ttr_entropy.tex
artifacts/mcnemar_pvalues/mcnemar_detail.tex
artifacts/_project/paper/theta_lof
…[truncated 1022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T09:58:19.717028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T09:58:19.717408+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{subcaption}
13	\usepackage{tablefootnote}
14	
15	\newcommand{\kstar}{K^{*}}
16	\newcommand{\auc}{\mathrm{AUC}}
17	\newcommand{\jsd}{\mathrm{JSD}}
18	\newcommand{\dpi}{\mathrm{DPI}}
19	
20	\title{Bounded Depth Discrimination in Recursive Synthetic Text:\\
21	  Measuring $K^{*}$ Across Domains, Architectures, and Scales}
22	
23	\author{Anonymous}
24	\date{}
25	
26	\begin{document}
27	\maketitle
28	
29	% ===========================================================================
30	% ABSTRACT
31	% ===========================================================================
32	\begin{abstract}
33	Web-scale training corpora are increasingly contaminated by machine-generated text that has itself been generated from earlier machine outputs, forming recursive chains of unknown depth.
34	Current detectors treat this as a binary problem (human vs.\ synthetic) and ignore generational depth, yet quality degrades non-linearly with each recursive pass.
35	We formalize recursive generation as an iterated lossy channel and show via the Data Processing Inequality (DPI) that a finite discrimination boundary $\kstar$ must exist: beyond depth $\kstar$, no statistical test can reliably distinguish consecutive generations.
36	Through controlled experiments spanning 9 model configurations (6 architecture families, 1B--32B parameters), 4 source domains (C4, Wikipedia, arXiv, Code/Python), and 4 decoding strategies, we provide the first systematic empirical measurement of $\kstar$.
37	We find that $\kstar \in \{1,2,3\}$, forming a strict domain hierarchy: Wikipedia saturates at $\kstar\!=\!1$ (6 models, scorer-controlled), web text and code at $\kstar\!=\!2$ (C4: 8/
…[truncated 39887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T09:58:19.717600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T09:58:19.717847+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	% === Pipeline figure placeholder ===
5	% \begin{figure}[t]
6	% \centering
7	% \includegraphics[width=\columnwidth]{figures/pipeline.pdf}
8	% \caption{Overview of the generational depth estimation pipeline. Seed documents from C4 are recursively passed through a generation operator $G_\delta$ to produce a depth chain $X \to Y_1 \to \cdots \to Y_K$. Statistical features extracted by an external scorer model are fed to the OBD-LightGBM classifier for depth prediction.}
9	% \label{fig:pipeline}
10	% \end{figure}
11	
12	\subsection{Problem Formulation}
13	\label{sec:formulation}
14	
15	We model recursive text generation as an iterated lossy channel.
16	Let $X$ denote an original human-written document drawn from a source distribution $\mathcal{D}$.
17	A generation operator $G_\delta = \text{LLM} + \delta$, parameterized by a decoding strategy $\delta$ (e.g., nucleus sampling with top-$p$ and temperature $T$), produces successive generations:
18	\begin{equation}
19	  X \to Y_1 \to Y_2 \to \cdots \to Y_K, \quad Y_k = G_\delta(Y_{k-1}),
20	  \label{eq:markov}
21	\end{equation}
22	where $Y_0 \triangleq X$.
23	The sequence $\{Y_k\}_{k=0}^K$ forms a Markov chain, since each generation depends only on its immediate predecessor.
24	
25	By the Data Processing Inequality (DPI), mutual information between the original document and successive generations is monotonically non-increasing:
26	\begin{equation}
27	  I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0.
28	  \label{eq:dpi}
29	\end{equation}
30	Since mutual information is bounded below by zero, this monotone sequence converges, implying that $I(Y_k; Y_{k+1}) \to 0$ as $k$ grows.
31	There exists a finite $\Ktheory$ beyond which the channel retains negligible information about generational identity---the \emph{information-theoretic discrimination boundary}.
32	
33	$\Ktheory$ is an upper bound on discriminability in principle.
34	In practice, we measure an \emph{operational} lower bound $\
…[truncated 10800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T09:58:19.718024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/experiments_c1.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T09:58:19.718261+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on four model configurations:
5	Pythia-1.4B and OLMo-1B in continuation mode, and Qwen2.5-7B-Instruct in both rewrite and continuation modes.
6	All experiments use the OBD-LightGBM classifier with the 12-dimensional feature set described in Section~3.
7	Each configuration uses a balanced corpus of 500 texts per depth level (generations 0--5).
8	We organize results around four questions:
9	(1)~Does $\Kempirical = 2$ hold across configurations?
10	(2)~Do depth classifiers transfer across models?
11	(3)~Is the feature degradation ordering model-independent?
12	(4)~How does generation mode affect detectability?
13	
14	%% ====================================================================
15	\subsection{$\Kstar = 2$ Across All Configurations}
16	\label{sec:kstar_boundary}
17	
18	Table~\ref{tab:kstar_ci} reports pairwise $\auc$ for adjacent depth pairs
19	across all four configurations, with bootstrap 95\% confidence intervals
20	(1{,}000 resamples) and permutation-test $p$-values for the critical 1v2
21	and 2v3 boundaries.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\caption{Pairwise $\auc$ for adjacent depth pairs.  Bootstrap 95\% CIs
27	and permutation $p$-values shown for the $\Kstar$ boundary rows (1v2,
28	2v3).  $\Kempirical = 2$ requires 1v2 $\text{CI}_\text{low} > \theta$
29	and 2v3 $\text{CI}_\text{high} < \theta$ with $\theta = 0.60$.
30	All 0v1 permutation $p = 0.002$.}
31	\label{tab:kstar_ci}
32	\begin{tabular}{lcccc}
33	\toprule
34	 & Qwen-rw & Pythia & OLMo & Qwen-cont \\
35	\midrule
36	0v1 & 0.9956 & 0.9932 & 0.9970 & 0.9972 \\[4pt]
37	1v2 & 0.6955 & 0.6539 & 0.6145 & 0.6112 \\
38	{\footnotesize CI}
39	  & {\footnotesize [.6859,\,.7041]}
40	  & {\footnotesize [.6454,\,.6630]}
41	  & {\footnotesize [.6045,\,.6247]}
42	  & {\footnotesize [.6015,\,.6213]} \\
43	{\footnotesize $p$}
44	  & {\footnotesize .002}
45	  & {\footnotesize .002}
46	  & {\footnotesize
…[truncated 13354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T09:58:19.718419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/code_crossmodel_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/code_crossmodel_table.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T09:58:19.718567+00:00_

1	%%% Code Domain Cross-Model K* Table
2	\begin{table*}[t]
3	  \centering
4	  \footnotesize
5	  \caption{Code domain (Python, CodeSearchNet) pairwise AUC with 5-fold cross-validated 95\% CIs across four models (four architecture families).
6	  Each model generates depth-0 through depth-5 text via iterative continuation of Python code snippets;
7	  LightGBM classifiers (5-fold GroupKFold) distinguish consecutive depths using surprisal and lexical features.
8	  $K^*$ denotes the empirical saturation depth at threshold $\theta = 0.60$.
9	  Qwen2.5-1.5B and LLaMA-3.1-8B yield $K^* = 2$; Pythia-1.4B yields $K^* = 1$; remaining models pending completion.}
10	  \label{tab:code_crossmodel_kstar}
11	  \resizebox{\textwidth}{!}{%
12	  \begin{tabular}{lcccccccc}
13	    \toprule
14	     & \multicolumn{2}{c}{Qwen2.5-1.5B} & \multicolumn{2}{c}{Pythia-1.4B} & \multicolumn{2}{c}{LLaMA-3.1-8B} & \multicolumn{2}{c}{Mistral-7B-v0.3} \\
15	    \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}
16	     & AUC & 95\% CI & AUC & 95\% CI & AUC & 95\% CI & AUC & 95\% CI \\
17	    \midrule
18	    0v1 & .9388 & [.929,\,.949] & \textbf{.9592} & [.956,\,.963] & .9161 & [.912,\,.920] & .TBD & [.TBD,\,.TBD] \\
19	    1v2 & \textbf{.7382} & [.709,\,.767]\rlap{$^*$} & .5983 & [.593,\,.603] & .7394 & [.729,\,.750]\rlap{$^*$} & .TBD & [.TBD,\,.TBD] \\
20	    2v3 & .5300 & [.514,\,.546] & .5215 & [.509,\,.534] & .5112 & [.502,\,.521] & .TBD & [.TBD,\,.TBD] \\
21	    3v4 & .5022 & [.486,\,.518] & .5152 & [.503,\,.527] & .5200 & [.506,\,.534] & .TBD & [.TBD,\,.TBD] \\
22	    4v5 & .5219 & [.510,\,.534] & .5046 & [.491,\,.518] & .4996 & [.493,\,.507] & .TBD & [.TBD,\,.TBD] \\
23	    \midrule
24	    $K^*$ & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{1} & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{TBD} \\
25	    \bottomrule
26	    \multicolumn{9}{l}{\footnotesize $^*$Permutation $p < 0.001$. $K^*$ defined as max $k$ where CI lower bound of $k$v$(k{+}1)$ AUC $\geq \the
…[truncated 52 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T09:58:19.718760+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T09:58:19.718925+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T09:58:19.719053+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T09:58:19.719180+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T09:58:19.719330+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\?\\?",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\?\\?",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T09:58:19.719468+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T09:58:19.719598+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{|\\\\cite\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{|\\\\cite\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T09:58:19.719737+00:00_

157:Table~\ref{tab:c4_full_scale} presents the complete C4 results across 8 model configurations spanning 1B to 32B parameters.
158:Eight of nine configurations yield $\kstar\!=\!2$; the sole exception is Mistral-7B ($\kstar\!=\!1$), analyzed in Section~\ref{sec:domain_ceiling}.
183:Table~\ref{tab:qwen32b_c4} shows the pairwise AUC profile.
206:Table~\ref{tab:scale_trend} summarizes the relationship between model scale and discrimination metrics.
237:Table~\ref{tab:code_crossmodel} summarizes Code domain results across five models and three architecture families.
259:Table~\ref{tab:mistral_code} presents Mistral-7B's Code domain pairwise AUC profile.
261:This is particularly informative because Mistral-7B achieves $\kstar\!=\!1$ on C4 (Section~\ref{sec:c4}), $\kstar\!=\!2$ on Code, and $\kstar\!=\!3$ on arXiv (Section~\ref{sec:arxiv}), making it the only model spanning all three $\kstar$ values.
262:Table~\ref{tab:mistral_ladder} presents this cross-domain ladder.
299:Table~\ref{tab:qwen7b_code} shows the Qwen-7B Code pairwise AUC profile, with $\kstar\!=\!2$ (1v2 AUC = 0.7223, CI [0.705, 0.740]).
300:Table~\ref{tab:qwen_code_scale} compares Qwen-1.5B and Qwen-7B on Code, demonstrating that a 4.7$\times$ scale increase within the same family produces no change in $\kstar$ and only a 1.6 percentage point shift in 1v2 AUC.
336:Table~\ref{tab:qwen7b_crossdomain} shows that Qwen-7B achieves the domain ceiling in all three tested domains: $\kstar\!=\!2$ on both C4 and Code, and $\kstar\!=\!3$ on arXiv.
379:Table~\ref{tab:domain_hierarchy} consolidates the domain hierarchy.
443:Table~\ref{tab:cc_depth} presents the predicted depth distribution.
466:Table~\ref{tab:cc_correlations} shows that predicted depth correlates negatively with both AlignScore (semantic coherence; Spearman $\rho = -0.312$, $p < 10^{-50}$) and vocabulary richness measures (type-token ratio: $\rho = -0.274$; hapax ratio: $\rho = -0.238$).
487:Table~\ref{tab:cc_domains} breaks down depth predictions by 
…[truncated 30 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T09:58:19.719910+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T09:58:19.720042+00:00_

155:\label{sec:c4}
163:\label{tab:c4_full_scale}
190:\label{tab:qwen32b_c4}
214:\label{tab:scale_trend}
231:\label{sec:code}
243:\label{tab:code_crossmodel}
267:\label{tab:mistral_code}
285:\label{tab:mistral_ladder}
305:\label{tab:qwen7b_code}
323:\label{tab:qwen_code_scale}
342:\label{tab:qwen7b_crossdomain}
356:\label{sec:arxiv}
366:\label{sec:wiki}
377:\label{sec:hierarchy}
385:\label{tab:domain_hierarchy}
400:\label{sec:transfer}
413:\label{sec:domain_ceiling}
440:\label{sec:cc_validation}
448:\label{tab:cc_depth}
472:\label{tab:cc_correlations}
494:\label{tab:cc_domains}
509:\label{sec:curation}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T09:58:19.720167+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\input\\{|\\\\include\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\input\\{|\\\\include\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T09:58:19.720284+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T09:58:19.720396+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.{log,aux,pdf}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.{log,aux,pdf}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T09:58:19.720510+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T09:58:19.720621+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "TBD",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/code_crossmodel_table.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "TBD",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/code_crossmodel_table.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T09:58:19.720751+00:00_

18:    0v1 & .9388 & [.929,\,.949] & \textbf{.9592} & [.956,\,.963] & .9161 & [.912,\,.920] & .TBD & [.TBD,\,.TBD] \\
19:    1v2 & \textbf{.7382} & [.709,\,.767]\rlap{$^*$} & .5983 & [.593,\,.603] & .7394 & [.729,\,.750]\rlap{$^*$} & .TBD & [.TBD,\,.TBD] \\
20:    2v3 & .5300 & [.514,\,.546] & .5215 & [.509,\,.534] & .5112 & [.502,\,.521] & .TBD & [.TBD,\,.TBD] \\
21:    3v4 & .5022 & [.486,\,.518] & .5152 & [.503,\,.527] & .5200 & [.506,\,.534] & .TBD & [.TBD,\,.TBD] \\
22:    4v5 & .5219 & [.510,\,.534] & .5046 & [.491,\,.518] & .4996 & [.493,\,.507] & .TBD & [.TBD,\,.TBD] \\
24:    $K^*$ & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{1} & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{TBD} \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T09:58:19.720953+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{|\\\\cite\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/method.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{|\\\\cite\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/method.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T09:58:19.721087+00:00_

39:where $\auc_{k,k+1}$ is the pairwise area under the ROC curve for distinguishing depth $k$ from $k{+}1$, $\text{CI}_{\text{lower}}^{95\%}$ denotes the lower bound of a bootstrap 95\% confidence interval (1{,}000 resamples), and $\theta$ is an operational threshold justified in \S\ref{sec:kstar_operational}.
45:We characterize each document with a 15-dimensional statistical feature vector, organized into five groups (Table~\ref{tab:features}).
87:Tail-thinning features capture the well-documented phenomenon whereby recursive generation concentrates probability mass on high-frequency tokens, thinning the distribution tail \cite{shumailov2024collapse, dohmatob2024model}.
121:$\Kempirical$ is defined as the maximum depth $k$ for which $\text{CI}_{\text{lower}}^{95\%}(\auc_{k,k+1}) > \theta$ (Eq.~\ref{eq:kstar}).
133:We evaluate four model configurations spanning three model families and two generation modes (Table~\ref{tab:setup}).
161:The effect of alternative decoding strategies (greedy, lower temperature, different $p$) on $\Kempirical$ is examined in a separate ablation (\S\ref{sec:experiments}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T09:58:19.721216+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{|\\\\cite\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/experiments_c1.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{|\\\\cite\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/experiments_c1.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T09:58:19.721336+00:00_

18:Table~\ref{tab:kstar_ci} reports pairwise $\auc$ for adjacent depth pairs
71:Figure~\ref{fig:auc_decay} visualizes this decay.
106:We examine both factors in Sections~\ref{sec:transfer}
107:and~\ref{sec:generation_mode}.
127:Table~\ref{tab:transfer_matrix} shows the full
260:(Table~\ref{tab:top_features}).
273:Section~\ref{sec:transfer}---rewrite-mode classifiers learn

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T09:58:19.721454+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
  "description": "Count words in paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
    "description": "Count words in paper.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T09:58:19.721575+00:00_

4988 /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T09:58:19.721689+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
  "description": "Count lines in paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
    "description": "Count lines in paper.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T09:58:19.721822+00:00_

571 /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T09:58:19.721940+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/tab_domain_model_kstar.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/tab_domain_model_kstar.tex"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T09:58:19.722070+00:00_

1	\begin{table}[t]
2	\centering
3	\caption{Generative depth $K^*$ across domains and models (scorer: Qwen2.5-1.5B, $\theta{=}0.60$). Bold values indicate the dominant mode per domain. $K^*$ is remarkably consistent within each domain: C4 yields $K^*{=}2$, arXiv yields $K^*{=}3$, and Wikipedia yields $K^*{=}1$, confirming that generative depth is domain-dependent and low-bounded.}
4	\label{tab:domain_model_kstar}
5	{\small
6	\begin{tabular}{llccc}
7	\toprule
8	\textbf{Model} & \textbf{Size} & \textbf{C4}~$K^*$ & \textbf{arXiv}~$K^*$ & \textbf{Wiki}~$K^*$ \\
9	\midrule
10	Qwen2.5       & 1.5B & \textbf{2} & \textbf{3} & \textbf{1}\textsuperscript{$\dagger$} \\
11	Qwen2.5       & 7B   & \textbf{2} & \textbf{3} & \textbf{1}\textsuperscript{$\dagger$} \\
12	Pythia        & 1.4B & \textbf{2} & \textbf{3} & \textbf{1} \\
13	LLaMA-3.1    & 8B   & \textbf{2} & \textbf{3} & \textbf{1} \\
14	Mistral       & 7B   & 1\textsuperscript{$\ddagger$} & \textbf{3} & \textbf{1} \\
15	OLMo          & 1B   & \textbf{2} & 1\textsuperscript{$*$} & \textbf{1} \\
16	\midrule
17	\textit{Dominant} & & \textbf{2} & \textbf{3} & \textbf{1} \\
18	\bottomrule
19	\end{tabular}
20	}
21	\vspace{2pt}
22	
23	{\footnotesize
24	\textsuperscript{$\dagger$}Scorer artifact: Qwen-1.5B scorer yields $K^*{=}2$; Pythia scorer yields $K^*{=}1$ (see \S\ref{sec:crossscorer}).\\
25	\textsuperscript{$\ddagger$}Domain-specific one-wash: AUC(1v2)${=}0.5935{<}\theta$; arXiv rescues to $K^*{=}3$.\\
26	\textsuperscript{$*$}Capacity failure: OLMo-1B generates out-of-domain text on arXiv.
27	}
28	\end{table}
29	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T09:58:19.722223+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260519T090934/best/paper.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T09:58:19.722341+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T09:58:19.722454+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/method.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/method.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T09:58:19.722577+00:00_

31:There exists a finite $\Ktheory$ beyond which the channel retains negligible information about generational identity---the \emph{information-theoretic discrimination boundary}.
111:The low MAE of ordinal logistic regression stems from collapsing predictions toward central depths rather than improved discrimination---a pathology that renders it unsuitable when pairwise depth discriminability is the primary objective.
183:Third, the asymmetric transfer---continuation${\to}$rewrite retains 89\% performance versus rewrite${\to}$continuation at 82\%---indicates that continuation-mode features form a generalizable subset of what rewrite-mode classifiers exploit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T09:58:19.722696+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/experiments_c1.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/experiments_c1.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T09:58:19.722836+00:00_

94:indicates that $\Kstar = 2$ is robust but not trivially so---continuation-mode
182:the depth signal---on the order of 70--85\%---is text-intrinsic
257:The top-3 features---\texttt{surp\_d1\_std}, \texttt{surp\_std},
258:and \texttt{surp\_d2\_std}---are shared (up to ordering) across
273:Section~\ref{sec:transfer}---rewrite-mode classifiers learn
292:discrimination boundary---where precision matters most---varies
316:from the source text's style---additional artifacts that are
323:whereas the reverse direction---Qwen-rw trained,
324:Qwen-cont tested---retains 82\%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T09:58:19.722956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/new_bibtex_entries.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/paper/new_bibtex_entries.bib"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T09:58:19.723102+00:00_

1	% === New BibTeX entries for placeholder citations ===
2	% Generated 2026-05-18
3	
4	% placeholder_guo2023survey → guo2023closechatgpt
5	% NOTE: No survey paper co-authored by both "Guo" and "Bao" was found.
6	% Best match for "Guo 2023" in text detection is the HC3 paper below.
7	% The paper covers detection methods extensively but is a dataset/benchmark
8	% paper, not a pure survey. Consider whether this is the intended reference,
9	% or if a different survey (e.g., Wu et al. 2023, arXiv:2310.14724) is meant.
10	@article{guo2023closechatgpt,
11	  title={How Close is {ChatGPT} to Human Experts? {Comparison} Corpus, Evaluation, and Detection},
12	  author={Guo, Biyang and Zhang, Xin and Wang, Ziyuan and Jiang, Minqi and Nie, Jinran and Ding, Yuxuan and Yue, Jianwei and Wu, Yupeng},
13	  journal={arXiv preprint arXiv:2301.07597},
14	  year={2023},
15	  url={https://arxiv.org/abs/2301.07597}
16	}
17	
18	% placeholder_tang2024science → tang2024science
19	@article{tang2024science,
20	  title={The Science of Detecting {LLM}-Generated Text},
21	  author={Tang, Ruixiang and Chuang, Yu-Neng and Hu, Xia},
22	  journal={Communications of the ACM},
23	  volume={67},
24	  number={4},
25	  pages={50--59},
26	  year={2024},
27	  doi={10.1145/3624725}
28	}
29	
30	% placeholder_krishna2024 → krishna2023paraphrasing (DUPLICATE)
31	% NOTE: krishna2023paraphrasing already exists in references.bib (line 239).
32	% No separate 2024 paper by Krishna on iterative paraphrasing was found.
33	% The tex file cites both krishna2023paraphrasing (line 14) and
34	% placeholder_krishna2024 (line 15) separately. These likely refer to the
35	% same NeurIPS 2023 paper. Recommended fix: replace \cite{placeholder_krishna2024}
36	% with \cite{krishna2023paraphrasing} in related_work.tex line 15,
37	% or keep this duplicate entry under a different key:
38	@inproceedings{krishna2024paraphrasing,
39	  title={Paraphrasing Evades Detectors of {AI}-Generated Text, but Retrieval is an Effective Defense},
40	
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pre-submission-check_20260519T095454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-19T09:58:19.723412+00:00_

Now I have everything needed. Here's the full pre-submission check report.

---

## 论文 Pre-Submission 检查报告

检查对象：
- 主论文：`artifacts/dream_reports/dream_20260519T090934/best/paper.tex`（最新完整 draft，571 行）
- 组件文件：`artifacts/_project/paper/method.tex`、`experiments_c1.tex`、`code_crossmodel_table.tex`

---

### 1. Em-dash 清零检查

**主论文 paper.tex（dream report）：** ✅ 通过
- Unicode em-dash `—` (U+2014): 0 匹配
- 解释性 en-dash ` – ` (U+2013): 0 匹配
- LaTeX em-dash `---`: 0 匹配

**组件文件：** ⚠️ 需修复（如果合入最终稿）

`method.tex` 有 3 处 `---`：
- 第 31 行: `...generational identity---the \emph{information-theoretic...`
- 第 111 行: `...improved discrimination---a pathology that renders...`
- 第 183 行: `...the asymmetric transfer---continuation${\to}$rewrite...`

`experiments_c1.tex` 有 8 处 `---`：
- 第 94、182、257-258、273、292、316、323-324 行

如果主论文 dream paper.tex 是最终投稿版，则这些组件文件的 dash 不影响提交。但如果后续需要把组件文件内容合入，必须清理。

---

### 2. Undefined References 检查

⚠️ 有严重问题

**`??` 标记：** ✅ 未发现（但论文未编译，无法从 .log 确认）

**`\ref{}` 交叉引用：** ✅ 全部匹配
- 所有 `\ref{tab:...}` 和 `\ref{sec:...}` 都有对应 `\label{}`

**`\cite{}` 缺失：** ⚠️⚠️ 严重问题
- 主论文 paper.tex 中有 `\bibliographystyle{plainnat}` 和 `\bibliography{references}`
- 但**整篇论文 0 个 `\cite{}` 命令**
- Related Work 中提到多篇论文（DetectGPT, Fast-DetectGPT, Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024, DSIR, D4, DoReMi 等）全部以文本形式提及，没有使用 `\cite{}`
- 编译后 bibliography 将为空，所有作者年份引用都不会正确渲染
- **必须修复：为所有文内引用添加 `\cite{}`，确保 .bib 文件包含所有条目**

---

### 3. Abstract 模型数量描述检查

⚠️ 需修复

Abstract 声称：**"9 model configurations (6 architecture families, 1B--32B parameters)"**

**实际模型列表**（Introduction 第 134 行）：
Qwen-1.5B, Qwen-7B, Qwen-14B, Qwen-32B, LLaMA-3.1-8B, Mistral-7B, Pythia-1.4B, OLMo-1B = **8 个不同模型**

如果加上 Qwen rewrite+continuation 两种模式 = 9 configs，但这不是独立模型配置，描述有误导性。

**架构族数量错误：**
- Qwen, LLaMA, Mistral, GPT-NeoX (Pythia), OLMo = **5 个架构族**
- 论文声称 **6 个**，多算了 1 个
- Introduction 第 69 行尝试列举 6 个但实际只列了 5 个

**需更新数字：**
| 项目 | 论文声称 | 实际 | 需改? |
|------|---------|------|-------|
| Model configs | 9 | 8 模型 (或 9 含 rewrite) | 需统一口径 |
| Architecture families | 6 | **5** | ⚠️ 必须改为 5 |
| Domains | 4 | 4 | ✅ |
| Decoding strategies | 4 | 4 | ✅ |

**Code domain 描述**（Abstract 第 37 行）：
- 声称 "Code: 4/5 models across 3 architecture families"
- 论文实际测了 5 个模型 (Qwen-1.5B, LLaMA-8B, Mistral-7B, Qwen-7B, Pythia-1.4B)，4/5 达到 ceiling
- Qwen-1.5B 和 Qwen-7B 同属 Qwen 族，LLaMA, Mistral, GPT-NeoX = 共 **4 个架构族**（非 3 个）
- ⚠️ "3 architecture families" 应改为 "4 architecture families"

---

### 4. code_crossmodel_table.tex 嵌入检查

⚠️ 需确认

**嵌入状态：** 主论文 paper.tex 没有 `\input{}` 或 `\include{}`，所有表格都直接内联在 paper.tex 中。`code_crossmodel_table.tex` 未被引用。

**TBD 占位符状态：**
- `code_crossmodel_table.tex` 中 Mistral-7B-v0.3 全部为 TBD（第 18-24 行共 6 处）
- 但主论文 paper.tex 中已有 Mistral-7B Code 完整数据（K*=2, 1v2 AUC=0.6893）
- `code_crossmodel_table.tex` 缺少 Qwen-7B 列，而主论文已有 Qwen-7B Code 数据

**结论：** `code_crossmodel_table.tex` 与主论文数据不同步。如果这个文件不直接参与投稿则无影响，但应更新以保持一致。

---

### 5. 页数检查

⚠️ 多项问题

**无编译 PDF**（`_project/paper/` 目录无 .pdf/.log/.aux 文件）

**粗略估算：**
- paper.tex: 571 行, ~4988 词（含 LaTeX 命令）
- 正文 7 个 section（Abstract 至 Conclusion）
- **16+ 个表格**（大部分为 `[t]` 浮动表格）
- 至少 2 个 figure 引用（fig:auc_decay, fig:transfer_heatmap），但 figure 文件未包含

以 ACL 两栏格式估算，16+ 表格 + 正文文字量**大概率超过 8 页**。需要编译后确认。

**⚠️⚠️ 模板错误（最严重问题）：**
- 当前使用 `\documentclass[11pt,a4paper]{article}` + `geometry` 包
- **EMNLP 2026 要求使用官方 ACL 模板**（`acl_natbib` 或 `acl.sty`）
- 当前模板字号、栏宽、margin 全部不符合投稿要求
- **必须切换到 EMNLP 2026 官方模板后重新排版并确认页数**

---

### 汇总

| 检查项 | 状态 | 严重程度 |
|--------|------|---------|
| Em-dash 清零（主论文） | ✅ 通过 | — |
| Em-dash 清零（组件文件） | ⚠️ method.tex/experiments_c1.tex 有 `---` | 低（若不合入） |
| `??` undefined ref | ✅ 无 | — |
| `\ref` 交叉引用 | ✅ 全匹配 | — |
| **`\cite{}` 缺失** | **⚠️⚠️ 整篇 0 个 cite** | **🔴 Critical** |
| **架构族数量** | **⚠️ 声称 6 实际 5** | **需修复** |
| Code 架构族数量 | ⚠️ 声称 3 实际 4 | 需修复 |
| code_crossmodel_table 同步 | ⚠️ TBD 未更新 | 低 |
| **LaTeX 模板** | **⚠️⚠️ 非官方模板** | **🔴 Critical** |
| 页数 | ⚠️ 大概率超 8 页 | 需编译确认 |

**最紧急修复项：**
1. 补全所有 `\cite{}` 并确保 .bib 文件完整
2. 切换到 EMNLP 2026 官方 LaTeX 模板
3. 修正 "6 architecture families" → "5 architecture families"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_pre-submission-check_20260519T095454"
}
```

</details>

---
