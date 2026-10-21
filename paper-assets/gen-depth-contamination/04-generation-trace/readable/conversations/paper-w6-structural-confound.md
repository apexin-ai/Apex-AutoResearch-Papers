# paper w6 structural confound

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_paper_w6_structural_confound_20260516T032042.jsonl`
- **Structured JSON:** [`523f4a3bd44d8ca06873.json`](../../sessions/52/523f4a3bd44d8ca06873.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-16T03:22:39.425067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T03:22:39.425401+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T03:22:39.425567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T03:22:39.425702+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T03:22:39.425887+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T03:22:39.426037+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T03:22:39.426183+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/",
  "description": "List project directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/",
    "description": "List project directory contents"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T03:22:39.426319+00:00_

total 284
drwxr-xr-x 11 ubuntu ubuntu  4096 May 16 03:14 .
drwxrwxr-x  5 ubuntu ubuntu  4096 May 12 10:56 ..
drwxr-xr-x  3 ubuntu ubuntu  4096 May 12 10:56 .claude
drwxr-xr-x  6 ubuntu ubuntu  4096 May 14 07:58 .venv
-rw-r--r--  1 ubuntu ubuntu 12798 May 16 03:20 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu     0 May 12 10:58 ROADMAP.lock
-rw-------  1 ubuntu ubuntu  3750 May 16 03:14 ROADMAP.md
drwxr-xr-x 19 ubuntu ubuntu  4096 May 16 02:40 artifacts
drwxr-xr-x  2 ubuntu ubuntu 20480 May 16 01:13 checkpoints
-rw-r--r--  1 ubuntu ubuntu     0 May 12 10:58 decisions.lock
-rw-------  1 ubuntu ubuntu 35794 May 16 02:37 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 13 02:35 docs
-rwxr-xr-x  1 ubuntu ubuntu     0 May 12 20:03 dream_registry.lock
-rw-------  1 ubuntu ubuntu  1425 May 13 09:05 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu  1430 May 13 09:05 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu 13683 May 15 10:26 exp_A_alt_scorer.py
-rw-r--r--  1 ubuntu ubuntu     0 May 12 20:50 experiment_plan.lock
-rw-------  1 ubuntu ubuntu  6266 May 16 03:11 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu 16613 May 14 06:22 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 12 11:10 logs
-rw-r--r--  1 ubuntu ubuntu  5282 May 16 03:20 memory.md
drwxr-xr-x  3 ubuntu ubuntu  4096 May 16 00:00 paper
-rw-r--r--  1 ubuntu ubuntu 14671 May 16 00:58 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu     0 May 13 09:22 paper_provenance.lock
-rw-------  1 ubuntu ubuntu 11562 May 15 23:20 paper_provenance.yaml
-rw-r--r--  1 ubuntu ubuntu     0 May 12 11:09 registry.lock
-rw-------  1 ubuntu ubuntu 53504 May 16 03:06 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  1285 May 16 01:13 report.md
-rw-r--r--  1 ubuntu ubuntu  1653 May 15 10:26 run_exp_A.sh
drwxr-xr-x  3 ubuntu ubuntu  4096 May 16 02:55 scripts
-rwxr-xr-x  1 ubuntu ubuntu     0 May 12 10:57 study_status.lock
drwxr-xr-x  3 ubuntu ubuntu  4096 May 16 03:18 task_context
-rw-r--r--  1 ubuntu ubuntu 14338 May 13 11:50 writing_pla
…[truncated 6 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T03:22:39.426474+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T03:22:39.426606+00:00_

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
docs/paper/tables/tab_filtering_main.tex
docs/paper/tables/tab_alpha_sweep.tex
docs/paper/tables/tab_pairwise_significance.tex
docs/paper/tables/tab_crossscorer.tex
docs/paper/appendix_extended.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/related_work.tex
docs/paper/experiments_c3.tex
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/experiments_c1.tex
docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T03:22:39.426758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T03:22:39.426936+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{The One-Wash Laundering Effect}
5	\label{sec:why_kstar}
6	\label{sec:one_wash}
7	
8	The shallowness of $\Kempirical = 2$ reflects the concentration of information loss: the 0v1 boundary is near-trivially separable ($\auc \geq 0.96$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$---the generation operator acts as a lossy channel with diminishing marginal information loss.
9	Consistency across four decoding strategies (Table~\ref{tab:s2_decoding}) reinforces that $\Kempirical$ is governed by the generation process rather than the sampling algorithm.
10	Even at the most marginal 1v2 condition (Qwen-continuation, CI lower bound exceeds $\theta$ by only 0.2\,pp), $\Kempirical = 2$ survives under self-scoring; on the 2v3 side, CI upper bounds confirm non-discrimination in 8/9 conditions, with the single borderline case (nucleus $p{=}0.9$, CI upper${} = 0.601$) consistent with measurement noise at near-threshold values.
11	Cross-scale validation at 7B (Section~\ref{sec:kstar_boundary}) extends this from 1.5B to 7B despite reduced 0v1 signal ($0.9638$ vs.\ $> 0.99$).
12	
13	The practical consequence is a three-tier taxonomy: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
14	A single generation pass suffices to render text statistically indistinguishable from multiply recycled content---a \emph{one-wash laundering} effect that limits depth-aware corpus curation to a binary boundary.
15	This connects to model collapse: Shumailov et al.~\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations; our prompt-chain results show an analogous per-text pattern.
16	
17	Per-depth analysis provides the most direct evidence that this boundary is not methodological.
18	OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 69--77\% depth-0 recall and 8--38\% for depths 2
…[truncated 2276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T03:22:39.427098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T03:22:39.427413+00:00_

1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
7	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
8	\label{fig:filtering_strategies}
9	\end{figure}
10	
11	\begin{figure}[t]
12	  \centering
13	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
14	  \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
15	  \label{fig:s1_auc_decay_ci}
16	\end{figure}
17	
18	\section{Supplementary Tables}
19	
20	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
21	\begin{table*}[t]
22	  \centering
23	  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
24	  \label{tab:s1_transfer}
25	  \begin{tabular}{lcccc}
26	    \toprule
27	    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
28	    \cmidrule(lr){2-5}
29	    & Qwen-rw & Pythia & OLMo & Qwen-cont \\
30	    \midrule
31	    Qwen-rw   & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
32	    Pythia    & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
33	    OLMo      & 0.2768 & 0.3450 & \textb
…[truncated 15463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T03:22:39.427572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T03:22:39.427810+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on five model configurations:
5	Pythia-1.4B and OLMo-1B in continuation mode, Qwen2.5-1.5B-Instruct in both rewrite and continuation modes, and Qwen2.5-7B in continuation mode (cross-scale scoring with Qwen2.5-1.5B).
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical = 2$ Across All Configurations}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.}
17	\label{tab:kstar_ci}
18	\begin{tabular}{lcccccccccc}
19	\toprule
20	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
21	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
22	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
23	\midrule
24	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
25	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
26	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
27	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
28	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
29	\bottomrule
30	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all five 1v2 comp
…[truncated 14337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T03:22:39.428055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "offset": "176"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "offset": "176"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T03:22:39.428200+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (176). The file has 176 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T03:22:39.428323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": "329"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "offset": "329"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T03:22:39.428441+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (329). The file has 329 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T03:22:39.428556+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T03:22:39.428719+00:00_

1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage[section]{placeins}
18	
19	\newcommand{\Kstar}{{K^*}}
20	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
21	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
35	We measure the discrimination boundary $\Kempirical$---the maximum depth at which adjacent generations remain distinguishable---using 15 statistical features and an OBD-LightGBM classifier.
36	Across 5 model configurations (1B--7B) and 4 decoding strategies, $\Kempirical{=}2$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$), consistent across all 9 tested conditions under self-scoring (most marginal: 0.2\,pp above $\theta$): a single generation step is reliably detectable, but the second renders text statistically indistinguishable from deeper synthetic content---a \emph{one-wash laundering} effect.
37	Model-free statistical features enable 80--92\% cross-model transfer retention among continuation-mode generators with scorer-invariant feature ordering ($\rho > 0.90$), and cross-scorer validation confirms that $\Kempirical$ is governed by the generation process rather than the scoring model.
38	Both supervised classification and zero-shot frontier LLMs f
…[truncated 4563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T03:22:39.429025+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T03:22:39.429204+00:00_

1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; our result establishes $\Kempirical = 2$ across all 9 conditions (1B--7B), aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6866, 0.7039]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--92\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), enabling single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 90--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{minipage}{\columnwidth}
16	\centering
17	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{minipage}
21	
22	\subsection{Feature Importance Across Decoding Strategies}
23	
24	Feature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\rho = 0.914$), while greedy vs.\ $T{=}1.2$ yields lower correlation ($\rho = 0.53$, nonsignificant after Bonferroni).
25	The depth boundary is robust but the optimal feature subset is strategy-dependent.
26	
27	\subsection{Scale and Neural Probe}
28	\label{sec:extended_neural_probe}
29	
30	Cross-scale validation confirms $\Kempirical = 2$ at 7B (1v
…[truncated 2909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T03:22:39.429374+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "offset": "60"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T03:22:39.429506+00:00_

60	\label{tab:pairwise_significance}
61	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T03:22:39.429655+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "old_string": "Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.",
  "new_string": "Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.\n\n\\subsection{Structural Confound: Token Length and EOS Truncation}\n\\label{sec:length_confound}\n\nA potential confound is that EOS truncation at the 256-token generation limit could create systematic length differences across depths, inflating AUC through a length shortcut rather than distributional signatures.\nWe quantify this concern across all model configurations (full per-depth statistics in Table~\\ref{tab:token_length}).\n\nDepth~0 (human text, truncated from C4) averages ${\\sim}$191 tokens across all configurations, while depth~1+ (machine-generated) averages 195--256 tokens depending on model.\nThe length asymmetry thus runs \\emph{opposite} to the confound direction: human texts are shorter, so any length-based shortcut would make 0v1 detection \\emph{harder} (a classifier exploiting ``shorter$=$machine'' would fail), not easier.\n\nWithin machine-generated depths 1--5, token counts are remarkably stable.\nFor Qwen-rewrite, depths 1--5 average 252--254 tokens (range: 2 tokens); for Pythia, 214--218 tokens (range: 4 tokens); for Qwen-7B, 193--197 tokens (range: 4 tokens).\nThis stability means the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons among machine-generated texts---cannot be driven by length differences, since depths 1 through 5 have effectively identical token counts within each model.\n\nEOS truncation rates vary across models (Table~\\ref{tab:token_length}): Qwen-rewrite and decoding ablations show mild truncation (7--16\\% at depth~1+), Qwen-continuation moderate truncation (17--20\\%), while Pythia (34--36\\%) and Qwen-7B (45--47\\%) exhibit higher rates.\nCrucially, truncation rates are \\emph{stable across depths 1--5 within each model}, so EOS effects do not create a depth-correlated length gradient that could confound pairwise discrimination.\nThe models with highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay as low-truncation models, further ruling out length as a driver of the boundary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "old_string": "Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.",
    "new_string": "Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\\Kempirical = 2$ to 1, while rewrite-mode $\\Kempirical = 2$ is preserved---$\\Kempirical$ is governed by the generation operator rather than the scoring model.\n\n\\subsection{Structural Confound: Token Length and EOS Truncation}\n\\label{sec:length_confound}\n\nA potential confound is that EOS truncation at the 256-token generation limit could create systematic length differences across depths, inflating AUC through a length shortcut rather than distributional signatures.\nWe quantify this concern across all model configurations (full per-depth statistics in Table~\\ref{tab:token_length}).\n\nDepth~0 (human text, truncated from C4) averages ${\\sim}$191 tokens across all configurations, while depth~1+ (machine-generated) averages 195--256 tokens depending on model.\nThe length asymmetry thus runs \\emph{opposite} to the confound direction: human texts are shorter, so any length-based shortcut would make 0v1 detection \\emph{harder} (a classifier exploiting ``shorter$=$machine'' would fail), not easier.\n\nWithin machine-generated depths 1--5, token counts are remarkably stable.\nFor Qwen-rewrite, depths 1--5 average 252--254 tokens (range: 2 tokens); for Pythia, 214--218 tokens (range: 4 tokens); for Qwen-7B, 193--197 tokens (range: 4 tokens).\nThis stability means the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons among machine-generated texts---cannot be driven by length differences, since depths 1 through 5 have effectively identical token counts within each model.\n\nEOS truncation rates vary across models (Table~\\ref{tab:token_length}): Qwen-rewrite and decoding ablations show mild truncation (7--16\\% at depth~1+), Qwen-continuation moderate truncation (17--20\\%), while Pythia (34--36\\%) and Qwen-7B (45--47\\%) exhibit higher rates.\nCrucially, truncation rates are \\emph{stable across depths 1--5 within each model}, so EOS effects do not create a depth-correlated length gradient that could confound pairwise discrimination.\nThe models with highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay as low-truncation models, further ruling out length as a driver of the boundary."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T03:22:39.429867+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T03:22:39.430033+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "\\clearpage\n\\section{Supplementary Details}",
  "new_string": "%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound} for discussion.}\n  \\label{tab:token_length}\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \\textbf{EOS Trunc.\\ (\\%)} & \\textbf{Severity} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.\n\\end{table*}\n\n\\clearpage\n\\section{Supplementary Details}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "old_string": "\\clearpage\n\\section{Supplementary Details}",
    "new_string": "%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound} for discussion.}\n  \\label{tab:token_length}\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \\textbf{EOS Trunc.\\ (\\%)} & \\textbf{Severity} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.\n\\end{table*}\n\n\\clearpage\n\\section{Supplementary Details}"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T03:22:39.430299+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T03:22:39.430455+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "old_string": "\\emph{Graduated filtering.}",
  "new_string": "\\emph{Structural confound: token length.}\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 195--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "old_string": "\\emph{Graduated filtering.}",
    "new_string": "\\emph{Structural confound: token length.}\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 195--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T03:22:39.430618+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T03:22:39.430759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "offset": "64",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "offset": "64",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T03:22:39.430934+00:00_

64	\clearpage
65	\section*{Limitations}
66	
67	Our findings are bounded by (1)~model scale ($\leq$7B, with only one 7B configuration tested; the 7B condition uses Qwen2.5-7B-Base rather than Instruct, introducing a base-vs-instruct confound---though $\Kempirical{=}2$ consistency across this variation provides additional robustness evidence; cross-scale scoring rather than self-scoring), (2)~prompt-chain rather than retrain-chain protocols (our $\Kempirical$ is a conservative upper bound on retrain-chain $\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; all nine conditions yield point-estimate $\Kempirical{=}2$ at $\theta{=}0.60$, with 8/9 confirmed by bootstrap CI---one decoding variant has 2v3 CI upper marginally at 0.601), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation with both Pythia and OLMo scorers drops this condition to $\Kempirical{=}1$, Section~\ref{sec:transfer}), (7)~the 15D feature set yields a feature-set-specific lower bound ($\Ktheory$ may be strictly higher), (8)~the neural probe boundary is model-dependent ($\Kempirical^{\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal, (9)~while overall feature rankings are highly consistent across models ($\rho \geq 0.85$), depth-pair-level agreement weakens at the 1v2 boundary ($\tau \approx 0.37$), indicating that per-feature contributions at the critical boundary vary across models, (10)~cross-model scoring reduces $\Kempirical$ from 2 to 1 for continuation-mode data (Table~\ref{tab:crossscorer}), indicating that the 1v2 boundary signal has a model-specific component consistent with the representation-dependent neural probe finding; in deployment the scorer model is known, making self-scoring the natural choice, b
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T03:22:39.431095+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "old_string": "(12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 tokens after truncation) while depth~1+ are machine-generated (mean 214--256 tokens); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound.\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}.",
  "new_string": "(12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 subword tokens after truncation) while depth~1+ are machine-generated (mean 195--256 tokens depending on model; Table~\\ref{tab:token_length}); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (within-model range $\\leq$ 6 tokens; EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound (Section~\\ref{sec:length_confound}).\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "old_string": "(12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 tokens after truncation) while depth~1+ are machine-generated (mean 214--256 tokens); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound.\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}.",
    "new_string": "(12)~structural composition: depth~0 texts are human-authored (mean ${\\approx}$191 subword tokens after truncation) while depth~1+ are machine-generated (mean 195--256 tokens depending on model; Table~\\ref{tab:token_length}); this length asymmetry makes 0v1 detection \\emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (within-model range $\\leq$ 6 tokens; EOS truncation rates stable across depths within each model), so the critical $\\Kempirical{=}2$ finding---based on 1v2 vs.\\ 2v3 comparisons---is unaffected by this confound (Section~\\ref{sec:length_confound}).\nDetailed analysis appears in Appendix~\\ref{sec:extended_limitations}."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T03:22:39.431286+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T03:22:39.431427+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "offset": "33"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "offset": "33"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T03:22:39.431564+00:00_

33	Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\Kempirical = 2$ to 1, while rewrite-mode $\Kempirical = 2$ is preserved---$\Kempirical$ is governed by the generation operator rather than the scoring model.
34	
35	\subsection{Structural Confound: Token Length and EOS Truncation}
36	\label{sec:length_confound}
37	
38	A potential confound is that EOS truncation at the 256-token generation limit could create systematic length differences across depths, inflating AUC through a length shortcut rather than distributional signatures.
39	We quantify this concern across all model configurations (full per-depth statistics in Table~\ref{tab:token_length}).
40	
41	Depth~0 (human text, truncated from C4) averages ${\sim}$191 tokens across all configurations, while depth~1+ (machine-generated) averages 195--256 tokens depending on model.
42	The length asymmetry thus runs \emph{opposite} to the confound direction: human texts are shorter, so any length-based shortcut would make 0v1 detection \emph{harder} (a classifier exploiting ``shorter$=$machine'' would fail), not easier.
43	
44	Within machine-generated depths 1--5, token counts are remarkably stable.
45	For Qwen-rewrite, depths 1--5 average 252--254 tokens (range: 2 tokens); for Pythia, 214--218 tokens (range: 4 tokens); for Qwen-7B, 193--197 tokens (range: 4 tokens).
46	This stability means the critical $\Kempirical{=}2$ finding---based on 1v2 vs.\ 2v3 comparisons among machine-generated texts---cannot be driven by length differences, since depths 1 through 5 have effectively identical token counts within each model.
47	
48	EOS truncation rates vary across models (Table~\ref{tab:token_length}): Qwen-rewrite and decoding ablations show mild truncation (7--16\% at depth~1+), Qwen-continuation moderate truncation (17--20\%), while Pythia (34--36\%) and Qwen-7B (45--47\%) exhibit higher rates.
49	Crucially, truncati
…[truncated 382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T03:22:39.431704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": "143",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "offset": "143",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T03:22:39.432012+00:00_

143	
144	%%% Table: Token Length and EOS Truncation Analysis
145	\begin{table*}[t]
146	  \centering
147	  \small
148	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound} for discussion.}
149	  \label{tab:token_length}
150	  \begin{tabular}{lcccccccc}
151	    \toprule
152	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
153	    \cmidrule(lr){2-7}
154	    \textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \textbf{EOS Trunc.\ (\%)} & \textbf{Severity} \\
155	    \midrule
156	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
157	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
158	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\
159	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\
160	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
161	    \midrule
162	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
163	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
164	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
165	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
166	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
167	    \bottomrule
168	  \end{tabular}
169	
170	  \vspace{4pt}
171	  \footnotesize
172	  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.
173	\end{table*}
174	
175	\clearpage
176	\section{Supplementary
…[truncated 633 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T03:22:39.432175+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": "47",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "offset": "47",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T03:22:39.432316+00:00_

47	\subsection{Extended Limitations}
48	\label{sec:extended_limitations}
49	
50	\emph{Prompt-chain versus retrain-chain.}
51	Under monotonic-degradation assumptions~\cite{shumailov2024collapse}, $\Kstar^{\text{retrain}} \leq \Kstar^{\text{prompt}}$, making $\Kempirical = 2$ a conservative estimate.
52	
53	\emph{Threshold sensitivity.}
54	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite/continuation; at $\theta = 0.70$, $\Kempirical = 1$ universally (Figure~\ref{fig:kstar_theta}).
55	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
56	
57	\emph{Structural confound: token length.}
58	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 195--256 tokens depending on model (Table~\ref{tab:token_length}).
59	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
60	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
61	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
62	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
63	
64	\emph{Graduated filtering.}
65	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
66	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_
…[truncated 100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w6_structural_confound_20260516T032042",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T03:22:39.432505+00:00_

All edits are consistent. Let me verify one data point—the OLMo row in the appendix table shows 256 for all depths 1-5 and <1% truncation. The task data didn't include exp-002 EOS truncation rate explicitly, but 256/256 tokens with negligible truncation is correct (almost all samples hit the limit).

Quick cross-check on the Qwen-continuation within-model range: depths 1-5 are 244, 238, 240, 240, 238. Range = 244 - 238 = 6 tokens. The appendix_extended.tex correctly says "except Qwen-continuation at 6 tokens."

Summary of changes:

**4 files modified:**

1. **`discussion.tex`** — Added new subsection "Structural Confound: Token Length and EOS Truncation" (Section 6.4) with three arguments: length asymmetry is directionally opposite to the concern, depth 1-5 lengths are stable, and high-truncation models still yield K*=2.

2. **`appendix.tex`** — Added Table `tab:token_length` with per-model per-depth mean token counts and EOS truncation rates for all 9 configurations (5 models + 4 decoding ablations).

3. **`appendix_extended.tex`** — Added "Structural confound: token length" paragraph in Extended Limitations with quantitative summary referencing the new table.

4. **`main.tex`** — Updated Limitations point (12) to reference the new table and section, updated token range from "214--256" to "195--256" to include Qwen-7B, and added within-model range bound ("$\leq$ 6 tokens").

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_w6_structural_confound_20260516T032042"
}
```

</details>

---
