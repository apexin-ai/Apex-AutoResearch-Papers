# paper fig2 integration

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_paper_fig2-integration_20260517T010117.jsonl`
- **Structured JSON:** [`0f24d98c1422aab01f79.json`](../../sessions/0f/0f24d98c1422aab01f79.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-17T01:04:22.336424+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T01:04:22.336940+00:00_

docs/paper/_corl_template/corl_2026_template_submission/example.tex
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/dream_reports/dream_20260514T062606/best/paper.tex
artifacts/dream_reports/dream_20260514T062606/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/best/paper.tex
artifacts/dream_reports/dream_20260515T004704/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/worst/paper.tex
artifacts/figures/archive/tab_rssm_fidelity.tex
artifacts/_project/paper/nve_sensitivity_table_37b680.tex
artifacts/_project/paper/nve_sensitivity_table.tex
paper/tables/nve_sensitivity_table.tex
artifacts/dream_reports/dream_20260514T062606/worst/paper.tex
artifacts/dream_reports/dream_20260516T115400/best/paper.tex
artifacts/dream_reports/dream_20260516T115400/median/paper.tex
artifacts/dream_reports/dream_20260516T115400/worst/paper.tex
docs/paper/sections/abstract.tex
artifacts/dream_reports/dream_20260516T133210/best/paper.tex
artifacts/dream_reports/dream_20260516T133210/median/paper.tex
artifacts/dream_reports/dream_20260516T133210/worst/paper.tex
artifacts/dream_reports/dream_20260516T172011/best/paper.tex
artifacts/dream_reports/dream_20260516T172011/median/paper.tex
artifacts/dream_reports/dream_20260516T172011/worst/paper.tex
docs/paper/sections/related_work.tex
docs/paper/sections/methodology.tex
docs/paper/main.tex
docs/paper/sections/abstract_body.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/analysis.tex
docs/paper/sections/appendix.tex
docs/paper/sections/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T01:04:22.337229+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T01:04:22.337497+00:00_

docs/paper/_corl_template/corl_2026_template_submission/corlabbrvnat.bst
docs/paper/_corl_template/corl_2026_template_submission/example.bib
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._corlabbrvnat.bst
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.bib
docs/paper/_corl_template/corl_2026_template_submission/.DS_Store
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._.DS_Store
docs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._corl_2026.sty
docs/paper/_corl_template/__MACOSX/._corl_2026_template_submission
docs/paper/_corl_template/corl_2026_template_submission/example.tex
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/_project/paper/narrative_frameworks_95c2c8.md
artifacts/_project/paper/narrative_frameworks.md
artifacts/_project/paper/related_work_section_6c6fde.md
artifacts/_project/paper/related_work_section.md
artifacts/_project/paper/experimental_setup_c0856a.md
artifacts/_project/paper/experimental_setup.md
artifacts/_project/paper/reference_audit_report.md
artifacts/_project/paper/method.md
artifacts/_project/paper/method_90ca4b.md
artifacts/_project/paper/related_work_draft_0456d1.md
artifacts/_project/paper/related_work_draft.md
artifacts/figures/paper/fig_style.py
artifacts/figures/paper/fig1_learning_curves.py
artifacts/figures/paper/fig4_mechanism_diagram.py
artifacts/figures/paper/fig5_dt_amplification.py
artifacts/figures/paper/__pycache__/fig_style.cpython-314.pyc
artifacts/figures/paper/fig1_learning_curves.pdf
artifacts/figures/paper/fig1_learning_curves.png
artifacts/figures/paper/fig4_mechanism_diagram.pdf
artifacts/figures/paper/fig4_mechanism_diagram.png
artifacts/figures/paper/fig5_dt_amplification.pdf
artifacts/figures/paper/fig5_dt_amplification.png
artifacts/figures/paper/fig3_factorial_grid.py
artifacts/figures/paper/fig3_factorial_grid.pdf
artifac
…[truncated 2604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T01:04:22.337767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T01:04:22.338119+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{All configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	\rowcolor{gray!15}
22	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
23	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
24	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
25	\midrule
26	\rowcolor{gray!15}
27	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
28	\rowcolor{gray!15}
29	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
30	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
31	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
32	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\times$ & Grad.\ starvation \\
33	\midrule
34	018 s1 & Full-SGS
…[truncated 7412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T01:04:22.338407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T01:04:22.338604+00:00_

1	\documentclass{article}
2	
3	% Load xcolor before corl_2026 (which loads color internally)
4	\usepackage[table]{xcolor}
5	\usepackage{corl_2026}
6	
7	\usepackage[utf8]{inputenc}
8	\usepackage[T1]{fontenc}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{graphicx}
13	\graphicspath{{../../artifacts/}}
14	\usepackage{colortbl}
15	\usepackage{caption}
16	\usepackage{subcaption}
17	\usepackage{array}
18	\usepackage{enumitem}
19	\usepackage{wrapfig}
20	
21	% Custom commands
22	\newcommand{\dt}{\mathrm{dt}}
23	\newcommand{\nve}{\mathrm{nve}}
24	% SGS result values (018 seed 1 only; seed 2 collapsed — 50% prevention rate)
25	\newcommand{\sgseval}{448.3}
26	\newcommand{\sgsnve}{1.66}
27	\newcommand{\sgsclaim}{prevented collapse in one of two seeds}
28	\newcommand{\ie}{\textit{i.e.}}
29	\newcommand{\eg}{\textit{e.g.}}
30	\newcommand{\cf}{\textit{cf.}}
31	\newcommand{\etal}{\textit{et al.}}
32	
33	\title{Why Temporal Abstraction Fails in Imagination-Based RL:\\
34	A Diagnostic Analysis of Variable-Rate DreamerV3}
35	
36	\author{
37	  Anonymous Authors
38	}
39	
40	\begin{document}
41	\maketitle
42	
43	\begin{abstract}
44	\input{sections/abstract_body}
45	\end{abstract}
46	
47	\keywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}
48	
49	% --- INTRODUCTION ---
50	\input{sections/introduction}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T01:04:22.338763+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "offset": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "offset": "50"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T01:04:22.338969+00:00_

50	\input{sections/introduction}
51	
52	% --- RELATED WORK ---
53	\input{sections/related_work}
54	
55	% --- METHODOLOGY ---
56	\input{sections/methodology}
57	
58	% --- RESULTS ---
59	\input{sections/results}
60	
61	% --- ANALYSIS ---
62	\input{sections/analysis}
63	
64	% --- CONCLUSION ---
65	\input{sections/conclusion}
66	
67	% no \bibliographystyle needed — corl_2026.sty sets it automatically
68	\bibliography{references}
69	
70	% --- APPENDIX ---
71	\appendix
72	\input{sections/appendix}
73	
74	\end{document}
75	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T01:04:22.339205+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/fig2_civo_decomposition.pdf",
  "description": "Verify figure file exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/fig2_civo_decomposition.pdf",
    "description": "Verify figure file exists"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T01:04:22.339371+00:00_

-rw-r--r-- 1 ubuntu ubuntu 21131 May 17 00:00 /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/fig2_civo_decomposition.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T01:04:22.339510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": "98"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "offset": "98"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T01:04:22.339658+00:00_

98	%% ============================================================
99	%% F6--F7: Interventions and cross-environment
100	%% ============================================================
101	
102	\subsection{F6--F7: Interventions and Multiple Pathways}
103	\label{sec:f6}
104	
105	\paragraph{F6: $\dt{=}1$ imagination does not prevent all collapse.}
106	Exp\_008e\_v3 restricts imagination to $\dt{=}1$ while retaining the trained embedding. Seed~1 is healthy (eval 869.9, $\nve = 0.80\times$); seed~2 collapses (eval $715 \rightarrow 137$, $\nve = 3.78\times$)---but via a qualitatively distinct mechanism (Figure~\ref{fig:multiple_pathways}). Classic CIVO (008d, Pathway~A) shows value explosion followed by evaluation decline with decreasing entropy; 008e\_v3\_s2 (Pathway~B) shows evaluation crash with \emph{increasing} entropy ($-5.21 \rightarrow -3.83$) while values remain stable. This produces the sole false positive in the NVE classification.
107	
108	\begin{figure}[t]
109	\centering
110	\includegraphics[width=0.65\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}
111	\caption{Contrasting collapse dynamics. \textbf{Left:} 008d (CIVO)---value explosion, entropy decreases. \textbf{Right:} 008e\_v3 s2 (non-CIVO)---evaluation crashes, entropy increases.}
112	\label{fig:multiple_pathways}
113	\end{figure}
114	
115	\paragraph{F7: Full-pathway gradient stopping shows mixed results.}
116	Exp\_018 detaches all non-KL gradients from $e_{\dt}$. This intervention yields seed-dependent outcomes: seed~1 avoids collapse (eval \sgseval{}, peak NVE $\sgsnve{}\times$) while seed~2 collapses (eval 40.8), indicating that cutting the observation decoder gradient pathway is necessary but not sufficient (50\% prevention rate). Reward-only SGS (016e) fails entirely (NVE $10.42\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\%$); peak NVE $14.59\times$.
117	
118	%% ===========================
…[truncated 1255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T01:04:22.339932+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 detaches all non-KL gradients from $e_{\\dt}$. This intervention yields seed-dependent outcomes: seed~1 avoids collapse (eval \\sgseval{}, peak NVE $\\sgsnve{}\\times$) while seed~2 collapses (eval 40.8), indicating that cutting the observation decoder gradient pathway is necessary but not sufficient (50\\% prevention rate). Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.",
  "new_string": "\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}\n\\label{fig:civo_decomposition}\n\\end{figure}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "old_string": "\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 detaches all non-KL gradients from $e_{\\dt}$. This intervention yields seed-dependent outcomes: seed~1 avoids collapse (eval \\sgseval{}, peak NVE $\\sgsnve{}\\times$) while seed~2 collapses (eval 40.8), indicating that cutting the observation decoder gradient pathway is necessary but not sufficient (50\\% prevention rate). Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.",
    "new_string": "\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}\n\\label{fig:civo_decomposition}\n\\end{figure}"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T01:04:22.340216+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T01:04:22.340371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": "114",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "offset": "114",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T01:04:22.340519+00:00_

114	
115	\paragraph{F7: Full-pathway gradient stopping shows mixed results.}
116	Exp\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\dt$-embedding alone produces $-73\%$ peak and $-86\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \sgseval{}, $-51\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\%$), yielding a 50\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\%$); peak NVE $14.59\times$.
117	
118	\begin{figure}[t]
119	\centering
120	\includegraphics[width=0.75\columnwidth]{figures/fig2_civo_decomposition.pdf}
121	\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\dt}$, two seeds. Trained $\dt$-embedding degrades peak eval by $73\%$ and final eval by $86\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\%$ final, no collapse) but seed~2 collapses ($-96\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\%$). All percentages relative to Baseline 001.}
122	\label{fig:civo_decomposition}
123	\end{figure}
124	
125
…[truncated 991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T01:04:22.340702+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fig:civo_decomposition|Fig\\.?\\s*2|Figure\\s*2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fig:civo_decomposition|Fig\\.?\\s*2|Figure\\s*2",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T01:04:22.340854+00:00_

docs/paper/sections/results.tex:116:[Omitted long matching line]
docs/paper/sections/results.tex:122:\label{fig:civo_decomposition}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T01:04:22.341046+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "SGS|Full-SGS|018|gradient stopping",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Grep",
  "tool_args": {
    "pattern": "SGS|Full-SGS|018|gradient stopping",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T01:04:22.341207+00:00_

docs/paper/sections/introduction.tex:6:[Omitted long matching line]
docs/paper/sections/results.tex:34:018 s1 & Full-SGS & trn$^\ddagger$ & ON & 8 & \sgseval{} @105K & \sgsnve{}$\times$$^*$ & No collapse \\
docs/paper/sections/results.tex:36:018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
docs/paper/sections/results.tex:48:trn$^\ddagger$ = full-pathway SGS (all non-KL gradients detached);
docs/paper/sections/results.tex:115:\paragraph{F7: Full-pathway gradient stopping shows mixed results.}
docs/paper/sections/results.tex:116:[Omitted long matching line]
docs/paper/sections/results.tex:121:[Omitted long matching line]
docs/paper/sections/methodology.tex:56:018 & Full-SGS & trn$^\ddagger$ & on & 8 & 2 \\
docs/paper/sections/methodology.tex:102:To identify which gradient pathway through $e_{\Delta t}$ drives CIVO, we introduce \textit{selective gradient stopping} (SGS): during the backward pass, $e_{\Delta t}$ is detached before entering selected prediction heads via the stop-gradient operator $\operatorname{sg}(\cdot)$, preventing those loss gradients from updating $e_{\Delta t}$'s parameters while preserving its forward-pass contribution.
docs/paper/sections/methodology.tex:104:[Omitted long matching line]
docs/paper/sections/methodology.tex:109:[Omitted long matching line]
docs/paper/sections/abstract.tex:2:[Omitted long matching line]
docs/paper/sections/appendix.tex:183:This mechanism is analogous to delusional bias \citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced---the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.
docs/paper/sections/appendix.tex:194:\caption{Gradient contribution to $e_{\Delta t}$ by loss component at two training checkpoints. The reward head contri
…[truncated 2175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T01:04:22.341352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
  "offset": "1",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
    "offset": "1",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T01:04:22.341564+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\dt{=}2$ collapses to $14\%$ of baseline, fixed $\dt{=}4$ never exceeds $19\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\%$. Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the causal factor within the factorial design tested. This trained-and-exposed embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates---a failure mode we term \emph{conditioning-induced value overestimation} (CIVO). A $\nve \geq 1.5\times$ threshold (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, single environment), with one non-CIVO false positive---a failure mode analogous to delusional bias \citep{lu2018nondelusional} but arising from model imprecision amplified by learned temporal conditioning. Gradient decomposition reveals a non-obvious mechanism: the reward head contributes the largest gradient share (38--49\%) but does not encode $\dt$-specific structural information, while the observation decoder channel (16--22\%) carries the critical spatial predictions that drive the RSSM fidelity gap. Reward-only gradient stopping fails (NVE $10.42\times$) despite targeting the largest pathway; full-pathway SGS that removes observation decoder gradients from the temporal embedding \sgsclaim{} (eval \sgseval
…[truncated 863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig2-integration_20260517T010117",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-17T01:04:22.342160+00:00_

Integration complete. The figure is placed in the F7 section (`\label{fig:civo_decomposition}`) with:

- **Updated F7 paragraph**: references `Figure~\ref{fig:civo_decomposition}`, reports the key percentages (-73% peak, -86% final for trained dt-emb; -51% and -96% for Full-SGS s1/s2), and frames SGS as "reduces but does not eliminate CIVO risk."
- **Self-contained caption**: defines all four conditions (Baseline, Trained dt-emb, Full-SGS s1/s2), reports quantitative findings, and explicitly notes the 50% prevention rate without overclaiming.
- **Figure path**: `figures/fig2_civo_decomposition.pdf` resolves correctly via the existing `\graphicspath{{../../artifacts/}}`.
- **Style compliance**: no em-dashes, no -ing phrase endings, no transition-word stacking.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_fig2-integration_20260517T010117"
}
```

</details>

---
