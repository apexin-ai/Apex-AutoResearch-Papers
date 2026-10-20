# Reviewer 1 coordination — Part 2 of 2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Structured JSON](../../../sessions/44/4438b2647bdef2856ed1.json)

## Round 17

### Tool call

_source line 506 · 2026-05-25T21:16:40.596621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-25T21:16:41.102637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-25T21:16:42.332598+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2605
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-25T21:16:43.294009+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3058
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-25T21:16:44.755325+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4158
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-25T21:16:44.758552+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3655
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-25T21:16:50.949674+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-25T21:16:53.734895+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.2}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.3}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 399.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 21.3}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2785
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-25T21:16:56.595604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-25T21:16:57.098573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 516 · 2026-05-25T21:16:57.553569+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 517 · 2026-05-25T21:16:57.555104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 518 · 2026-05-25T21:16:58.459836+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-25T21:16:58.460590+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-25T21:16:58.511055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 521 · 2026-05-25T21:16:58.712604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 522 · 2026-05-25T21:16:59.677015+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1165
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-25T21:17:00.084035+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1371
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-25T21:17:05.508605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-25T21:17:05.963628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-25T21:17:06.466810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-25T21:17:06.820730+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1312
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-25T21:17:06.821176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-25T21:17:07.328989+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1365
}
```

</details>

---


### Tool result

_source line 530 · 2026-05-25T21:17:07.934683+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1113
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-25T21:17:08.136760+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1669
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-25T21:18:29.495579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-25T21:18:29.597176+00:00_

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
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{amsthm}
14	\usepackage{booktabs}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\newtheorem{observation}{Observation}
19	\newtheorem{proposition}{Proposition}
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}{Corollary}
22	
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model\\for Disentangling Judge Bias and Contamination in LLM Evaluation}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{method}
37	\input{experiments}
38	\input{conclusion}
39	
40	\section*{Limitations}
41	\input{limitations}
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-25T21:18:32.456584+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/",
  "description": "List paper source files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/",
    "description": "List paper source files"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-25T21:18:32.657715+00:00_

_figure_backups
_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
background.tex
conclusion.tex
experiments.tex
figures
fill_paper_n17.py
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex
sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-25T21:18:35.418309+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-25T21:18:35.819961+00:00_

1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{fig2_ovb_bias}
7	\caption{Sequential estimation bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.80$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
8	\label{fig:ovb_bias}
9	\end{figure}
10	
11	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
12	%
13	\begin{equation}
14	\label{eq:mfrm}
15	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \gamma_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \gamma_k)} = \theta_n - b_i - d_j - \gamma_k,
16	\end{equation}
17	%
18	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\gamma_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts and showed that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
19	
20	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr20
…[truncated 3804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-25T21:18:35.820556+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-25T21:18:36.122267+00:00_

1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\subsection{Model Specification}
7	\label{sec:model_spec}
8	
9	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
10	%
11	\begin{equation}
12	\label{eq:gmfrm}
13	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \gamma_k + c_n \cdot e_i,
14	\end{equation}
15	%
16	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates model-specific contamination susceptibility ($c_n \geq 0$) from item-specific exposure ($e_i \in [0,1]$). When $c_n = 0$ or $e_i = 0$, the gating term vanishes and Eq.~\ref{eq:gmfrm} reduces to the standard MFRM.
17	
18	We enforce non-negativity and sparsity through a hierarchical HalfNormal prior: $\sigma_c \sim \text{HalfNormal}(1.0)$, $c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0)$, $c_n = c^{\mathrm{raw}}_n \cdot \sigma_c$. The hierarchical structure provides adaptive shrinkage: when data support low contamination, $\sigma_c$ contracts toward zero. The remaining priors are $\theta_n \sim \mathcal{N}(0, 1)$, $b_i \sim \mathcal{N}(0, 1)$, $d_j \sim \mathcal{N}(0, 0.5)$, and uniform on $\gamma_k$.
19	
20	G-MFRM extends the Doubly-Gated IRT model of \citet{shu2013dgirt}
…[truncated 5934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-25T21:18:36.122696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-25T21:18:36.173111+00:00_

1	The evaluation uses a single benchmark (Arena-Hard) with an incomplete observation design (${\sim}$58\% fill rate); generalization to other benchmarks and larger model populations remains to be verified. Posterior credible intervals for contamination susceptibility $c_n$ exhibit systematic overconfidence (71\% coverage at nominal 95\%; Appendix~\ref{app:ci_coverage}), a structural issue from the multiplicative coupling and HalfNormal boundary at $c_n = 0$ that warrants simulation-based recalibration. The rank-1 contamination structure assumes a single $c_n$ per model, whereas contamination may be domain-specific (e.g., coding vs.\ reasoning), motivating higher-rank decompositions in future work. The judge panel comprises six models from four provider families; generalization to more homogeneous panels is untested.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-25T21:18:39.787310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-25T21:18:40.089510+00:00_

1	\section{Proofs of Propositions~\ref{prop:no_new} and~\ref{prop:exposure_variation}}
2	\label{app:prop_proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:no_new}]
5	Suppose $c_n' = c_n + \delta$ preserves all response probabilities. Then $\delta \cdot e_i = 0$ for all items. Since $e_i \neq 0$ for at least one item by assumption, $\delta = 0$. Fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \cdot e_i = (\lambda c_n)(\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.
6	\end{proof}
7	
8	\begin{proof}[Proof of Proposition~\ref{prop:exposure_variation}]
9	When exposure is constant, the linear predictor becomes $(\theta_n + c_n \cdot e) - b_i - d_j - \gamma_k$, equivalent to a standard MFRM with reparameterized ability $\theta^*_n = \theta_n + c_n \cdot e$. No configuration of response data can distinguish $(\theta_n, c_n)$ from $(\theta_n + \epsilon, c_n - \epsilon/e)$ for any $\epsilon$.
10	\end{proof}
11	
12	
13	\section{Proof of Theorem~\ref{thm:sufficient}}
14	\label{app:proof}
15	
16	We prove that the G-MFRM is locally identifiable under the conditions of Theorem~\ref{thm:sufficient}. Following \citet{rothenberg1971}, a parametric model is locally identifiable at the true parameter vector $\boldsymbol{\psi}_0$ if and only if the Fisher information matrix $\mathbf{F}(\boldsymbol{\psi}_0)$ is non-singular.
17	
18	\paragraph{Setup.} The G-MFRM parameter vector is $\boldsymbol{\psi} = (\boldsymbol{\theta}, \mathbf{c}, \mathbf{b}, \mathbf{d}, \boldsymbol{\gamma})$, where $\boldsymbol{\theta} \in \mathbb{R}^{N-1}$ (after the location constraint $\sum_n \theta_n = 0$), $\mathbf{c} \in \mathbb{R}_{\geq 0}^N$, $\mathbf{b} \in \mathbb{R}^I$, $\mathbf{d} \in \mathbb{R}^J$, and $\boldsymbol{\gamma} \in \mathbb{R}^{K-1}$. The exposure vector $\mathbf{e} = (e_1, \ldots, e_I)$ is fixed externally and treated as known. The linear predictor is $\eta_{nijk} = \theta_n - b_i - d_j - \gamma_k + c_n \cdot e_i$, with partial derivatives:
…[truncated 35726 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-25T21:18:44.958584+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-25T21:18:45.009372+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig5_6_combined}
7	\caption{Contamination diagnostics ($N = 8$ pilot, 9 judges). (a)~Contamination susceptibility $\hat{c}_n$ (posterior mean $\pm$ 95\% CI), ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\times$ higher susceptibility than recent models (GPT-4o). (b)~Ability bias absorbed by MFRM-only estimation: $\Delta\theta = \hat{\theta}_{\mathrm{MFRM}} - \hat{\theta}_{\mathrm{G\text{-}MFRM}}$. The monotonic relationship (Spearman $\rho = 1.0$; $N = 8$, interpret with caution) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models, as predicted by the OVB analysis (Section~\ref{sec:confounding}).}
8	\label{fig:contamination_and_bias}
9	\end{figure*}
10	
11	\subsection{Setup}
12	\label{sec:setup}
13	
14	Our main experiment uses $N = 17$ target models evaluated by 6 LLM judges; a smaller $N = 8$ pilot with 9 judges validates sample-size effects. Table~\ref{tab:main_results} reports both configurations as part of the coverage analysis.
15	
16	\paragraph{Data and models.} We evaluate on Arena-Hard \citep{li2024arenahard}, a benchmark of 500 multi-turn conversational items selected for high separability among frontier models. The evaluation uses all 500 items in a connected incomplete design (${\sim}$58\% fill rate of the $N \times I \times J$ tensor). Seventeen target models spanning proprietary and open-source families are evaluated: GPT-4o, GPT-4o-mini, Qwen2.5-72B, LLaMA-3.3-70B, Qwen3-8B, Gemma-2-9B, GPT-4-0613, GPT-3.5-Turbo, Claude-3.5-Sonnet, GPT-4-Turbo, LLaMA-3.1-70B, Gemma-2-27B, Claude-3-Opus, LLaMA-3-70B, Mixtral-8x22B, Claude-3-Haiku, and LLaMA-3-8B. Ground-truth rankings are derived from Chatbot Arena human preference data \citep{zheng2023mtbench}.
17	
18	\paragraph{Judges.} Six LLM judges score responses in position-swapped pairwise mode: Claude Sonnet 4.6, DeepSeek-V4-Pro, Gem
…[truncated 8253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-25T21:22:30.480045+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告（方法严谨性审查）\n\n### 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4/5 (Quite sure)\n\n**一句话总结**: 理论框架（OVB 形式化 + identifiability 证明）扎实，但核心实验（N=17）中 G-MFRM 排名准确度反而低于 raw average，且 c_n 置信区间覆盖率仅 68–71%，削弱了作为实用校准工具的说服力。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 理论证明正确但 OVB 近似质量不足（r=0.80）；主实验排名负向；CI 系统性过窄 |\n| Excitement | 3.5/5 | 将 OVB 引入 LLM 评测的视角新颖，但实证改进不显著 |\n| Reproducibility | 4/5 | 代码数据已提供，合成实验可复现；Arena-Hard 公开可用；Stage 2 依赖 gpt-4-0314 锚点可能不可获取 |\n| Overall Assessment | 3.5 | Borderline Conference — 理论贡献达 Findings 水平，若解决主实验排名退化和 CI 覆盖问题可达 Conference |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 主实验（N=17）排名准确度系统性低于 baseline，正向结果仅来自统计不显著的小样本 pilot\n\n- 具体位置：Table 1 (Section 5.2)\n- 问题：N=17 主实验中，G-MFRM 在三个 item subset 上的 Kendall τ 分别为 0.794 / 0.809 / 0.779，均 ≤ raw average（0.838 / 0.824 / 0.779），Δτ = −0.044 / −0.015 / 0.000。即使在 100% exposure coverage 下，G-MFRM 也仅与 raw average 持平，未实现改进。唯一正向结果 Δτ = +0.071 来自 N=8 pilot，但 bootstrap CI 包含零（Table 1 脚注 †）。\n- 为什么影响接收：论文标题声称 \"Fair Scores via Joint Calibration\"，但主实验表明该方法在实际排名任务中无改进甚至有害。将正面叙事建立在非显著的 pilot 结果上，主实验负向结果放在 \"exposure coverage\" 解释下弱化处理，存在选择性报告的风险。\n- 建议修改方向：(1) 重新定位论文核心贡献为诊断工具（contamination profiling）而非排名校准方法；(2) 在 N=17 设置下验证 exposure 估计质量是否为根本瓶颈；(3) 或在 N≥17 规模上用完整 exposure 数据重新验证。\n\n**N2** [critical] c_n 置信区间覆盖率仅 67.9–71%（名义 95%），Murphy-Topel 修正未有效解决\n\n- 具体位置：Appendix R (CI Coverage Analysis)；Limitations；Table M caption\n- 问题：在合成数据上（N=8, 49 seeds），c_n 95% credible interval 的实际覆盖率仅为 67.9%；N=50 时改善至 71.3%。Murphy-Topel correction（Appendix D, Eq. 15）在理论上增大方差，但实际覆盖率仍远低于名义水平。同时 Table M 仍以 \"95% CI\" 标注 c_n 区间用于实质性解读。\n- 为什么影响接收：对于测量模型论文，不确定性量化的可靠性是核心质量指标。系统性 miscalibrated CI 会导致实践中对 c_n 的过度自信解读。\n- 建议修改方向：(1) 实现 simulation-based calibration (SBC)；(2) 报告 c_n 时使用实际覆盖率对应的区间；(3) 量化 Murphy-Topel 修正前后的覆盖率变化。\n\n**N3** [critical] OVB 线性近似应用于非线性 MFRM，近似质量不充分论证（r=0.80）\n\n- 具体位置：Observation 1 (Section 3, Eq. 3)；Figure 2；Appendix C (Eq. 10)\n- 问题：Observation 1 的核心公式 plim(θ̃_n − θ_n) = δ_n · c_n 仅对线性模型精确成立。一阶 Taylor 展开推广到 ordinal logit 后验证为 r = 0.80，r² = 0.64 意味着 36% 方差未被捕获。论文承认 \"the linear approximation serves only as directional motivation\"，但 Observation 1 的形式化陈述无近似误差界，且 OVB 叙事贯穿全文。\n- 为什么影响接收：论文理论新颖性主要来自将 OVB 引入 MFRM。若近似仅为 \"directional\"，Observation 1 应降级为启发式动机而非形式化结果。\n- 建议修改方向：(1) 提供近似误差的 formal bound；(2) 或在 Observation 1 中明确标注 \"approximate\" 并给出适用条件；(3) 补充大 c_n 下近似失效分析。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] MCMC 收敛阈值与引用标准不一致\n\n- 具体位置：Section 4.2；Section 5.1\n- 问题：论文设定 R̂ < 1.05, ESS_bulk > 100 并引用 Vehtari et al. (2021)。但该文推荐 R̂ < 1.01, ESS ≥ 400。实际结果（R̂ ≤ 1.003, ESS ≥ 1,240）满足更严格标准，但声明阈值与引用不符。\n- 建议：更新阈值为 R̂ < 1.01, ESS > 400，或将 R̂ < 1.05 引用改为 Gelman et al. (2013)。\n\n**W2** [warning] 42% items underfit（74/176 MNSQ < 0.5），模型拟合质量存疑\n\n- 具体位置：Appendix Q (Table 11)\n- 问题：176 个 items 中 92 个 misfitting（52%），其中 74 个 underfit。未量化这些 items 在总观测中占比，未做排除后 sensitivity analysis。\n- 建议：报告 misfitting items 观测覆盖率，做排除后 sensitivity analysis。\n\n**W3** [warning] Rank-1 contamination 结构（单一 c_n/model）限制性强\n\n- 具体位置：Section 4.1 (Eq. 4)；Limitations\n- 问题：假设每个模型有单一 c_n，不随 item 类型变化。未在当前数据上做 domain-specific residual analysis 检验此假设。\n- 建议：按 item category 做残差分析。\n\n**W4** [warning] Murphy-Topel correction 在 N=8 下渐近有效性未验证\n\n- 具体位置：Section 4.4；Appendix D\n- 问题：大样本修正在 N=8 下可能失效。未对比有/无 correction 的覆盖率。\n- 建议：量化 correction 前后覆盖率变化。\n\n**W5** [warning] σ_crit ≈ 0.2 阈值推导的 i.i.d. Gaussian 假设\n\n- 具体位置：Section 4.4\n- 问题：实际 exposure 估计误差可能跨 items 相关、非 Gaussian、heteroscedastic。\n- 建议：讨论假设局限性；测试 correlated noise。\n\n---\n\n### 小问题\n\n- Proposition 1 证明假设 \"e_i ≠ 0 for at least one item\"，但命题陈述中未包含此条件。\n- Figure 2 caption \"r = 0.80 confirms systematic overestimation\"——N=50 下 p < 0.001 门槛很低，\"confirms\" 措辞过强。\n- 合成实验规模（N=50）与真实实验（N=8/17）差异大，效果量直接对比需谨慎。\n- Section 5.2 的 Spearman ρ = 1.0 (N=8) 不具统计意义，论文已注释但可考虑删除。\n\n---\n\n### Questions for Authors\n\n1. N=17 的 100% exposure coverage 下（Exposed-only, 231 items），G-MFRM 与 raw average 的 τ 完全相同（0.779）。这是否意味着在充分 exposure 信息下，joint calibration 对排名没有增量价值？\n2. Murphy-Topel correction 后 c_n 覆盖率具体是多少？报告的 67.9–71% 是修正前还是修正后？\n3. Stage 2 的 gpt-4-0314 锚点若本身存在 contamination，exposure 估计是否会系统性偏倚？\n\n---\n\n### Missing References\n\n- SBC 文献（Talts et al., 2018）已在参考文献中但未用于 CI coverage 分析。\n- 无明显遗漏的关键 related work。\n\n---\n\n### 主要优势\n\n- 将 OVB 框架引入 MFRM 的 LLM 评测语境是新颖且有洞察力的视角。\n- Propositions 1–2 和 Theorem 1 的证明正确，Cauchy-Schwarz + Schur complement 路线简洁优雅。\n- 主实验负向结果的完整报告体现良好学术诚信。\n- Contamination susceptibility profile 与模型年龄的清晰梯度关系提供有实际意义的诊断信息。\n- 消融实验充分覆盖主要设计选择。",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告（方法严谨性审查）\n\n### 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4/5 (Quite sure)\n\n**一句话总结**: 理论框架（OVB 形式化 + identifiability 证明）扎实，但核心实验（N=17）中 G-MFRM 排名准确度反而低于 raw average，且 c_n 置信区间覆盖率仅 68–71%，削弱了作为实用校准工具的说服力。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 理论证明正确但 OVB 近似质量不足（r=0.80）；主实验排名负向；CI 系统性过窄 |\n| Excitement | 3.5/5 | 将 OVB 引入 LLM 评测的视角新颖，但实证改进不显著 |\n| Reproducibility | 4/5 | 代码数据已提供，合成实验可复现；Arena-Hard 公开可用；Stage 2 依赖 gpt-4-0314 锚点可能不可获取 |\n| Overall Assessment | 3.5 | Borderline Conference — 理论贡献达 Findings 水平，若解决主实验排名退化和 CI 覆盖问题可达 Conference |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 主实验（N=17）排名准确度系统性低于 baseline，正向结果仅来自统计不显著的小样本 pilot\n\n- 具体位置：Table 1 (Section 5.2)\n- 问题：N=17 主实验中，G-MFRM 在三个 item subset 上的 Kendall τ 分别为 0.794 / 0.809 / 0.779，均 ≤ raw average（0.838 / 0.824 / 0.779），Δτ = −0.044 / −0.015 / 0.000。即使在 100% exposure coverage 下，G-MFRM 也仅与 raw average 持平，未实现改进。唯一正向结果 Δτ = +0.071 来自 N=8 pilot，但 bootstrap CI 包含零（Table 1 脚注 †）。\n- 为什么影响接收：论文标题声称 \"Fair Scores via Joint Calibration\"，但主实验表明该方法在实际排名任务中无改进甚至有害。将正面叙事建立在非显著的 pilot 结果上，主实验负向结果放在 \"exposure coverage\" 解释下弱化处理，存在选择性报告的风险。\n- 建议修改方向：(1) 重新定位论文核心贡献为诊断工具（contamination profiling）而非排名校准方法；(2) 在 N=17 设置下验证 exposure 估计质量是否为根本瓶颈；(3) 或在 N≥17 规模上用完整 exposure 数据重新验证。\n\n**N2** [critical] c_n 置信区间覆盖率仅 67.9–71%（名义 95%），Murphy-Topel 修正未有效解决\n\n- 具体位置：Appendix R (CI Coverage Analysis)；Limitations；Table M caption\n- 问题：在合成数据上（N=8, 49 seeds），c_n 95% credible interval 的实际覆盖率仅为 67.9%；N=50 时改善至 71.3%。Murphy-Topel correction（Appendix D, Eq. 15）在理论上增大方差，但实际覆盖率仍远低于名义水平。同时 Table M 仍以 \"95% CI\" 标注 c_n 区间用于实质性解读。\n- 为什么影响接收：对于测量模型论文，不确定性量化的可靠性是核心质量指标。系统性 miscalibrated CI 会导致实践中对 c_n 的过度自信解读。\n- 建议修改方向：(1) 实现 simulation-based calibration (SBC)；(2) 报告 c_n 时使用实际覆盖率对应的区间；(3) 量化 Murphy-Topel 修正前后的覆盖率变化。\n\n**N3** [critical] OVB 线性近似应用于非线性 MFRM，近似质量不充分论证（r=0.80）\n\n- 具体位置：Observation 1 (Section 3, Eq. 3)；Figure 2；Appendix C (Eq. 10)\n- 问题：Observation 1 的核心公式 plim(θ̃_n − θ_n) = δ_n · c_n 仅对线性模型精确成立。一阶 Taylor 展开推广到 ordinal logit 后验证为 r = 0.80，r² = 0.64 意味着 36% 方差未被捕获。论文承认 \"the linear approximation serves only as directional motivation\"，但 Observation 1 的形式化陈述无近似误差界，且 OVB 叙事贯穿全文。\n- 为什么影响接收：论文理论新颖性主要来自将 OVB 引入 MFRM。若近似仅为 \"directional\"，Observation 1 应降级为启发式动机而非形式化结果。\n- 建议修改方向：(1) 提供近似误差的 formal bound；(2) 或在 Observation 1 中明确标注 \"approximate\" 并给出适用条件；(3) 补充大 c_n 下近似失效分析。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] MCMC 收敛阈值与引用标准不一致\n\n- 具体位置：Section 4.2；Section 5.1\n- 问题：论文设定 R̂ < 1.05, ESS_bulk > 100 并引用 Vehtari et al. (2021)。但该文推荐 R̂ < 1.01, ESS ≥ 400。实际结果（R̂ ≤ 1.003, ESS ≥ 1,240）满足更严格标准，但声明阈值与引用不符。\n- 建议：更新阈值为 R̂ < 1.01, ESS > 400，或将 R̂ < 1.05 引用改为 Gelman et al. (2013)。\n\n**W2** [warning] 42% items underfit（74/176 MNSQ < 0.5），模型拟合质量存疑\n\n- 具体位置：Appendix Q (Table 11)\n- 问题：176 个 items 中 92 个 misfitting（52%），其中 74 个 underfit。未量化这些 items 在总观测中占比，未做排除后 sensitivity analysis。\n- 建议：报告 misfitting items 观测覆盖率，做排除后 sensitivity analysis。\n\n**W3** [warning] Rank-1 contamination 结构（单一 c_n/model）限制性强\n\n- 具体位置：Section 4.1 (Eq. 4)；Limitations\n- 问题：假设每个模型有单一 c_n，不随 item 类型变化。未在当前数据上做 domain-specific residual analysis 检验此假设。\n- 建议：按 item category 做残差分析。\n\n**W4** [warning] Murphy-Topel correction 在 N=8 下渐近有效性未验证\n\n- 具体位置：Section 4.4；Appendix D\n- 问题：大样本修正在 N=8 下可能失效。未对比有/无 correction 的覆盖率。\n- 建议：量化 correction 前后覆盖率变化。\n\n**W5** [warning] σ_crit ≈ 0.2 阈值推导的 i.i.d. Gaussian 假设\n\n- 具体位置：Section 4.4\n- 问题：实际 exposure 估计误差可能跨 items 相关、非 Gaussian、heteroscedastic。\n- 建议：讨论假设局限性；测试 correlated noise。\n\n---\n\n### 小问题\n\n- Proposition 1 证明假设 \"e_i ≠ 0 for at least one item\"，但命题陈述中未包含此条件。\n- Figure 2 caption \"r = 0.80 confirms systematic overestimation\"——N=50 下 p < 0.001 门槛很低，\"confirms\" 措辞过强。\n- 合成实验规模（N=50）与真实实验（N=8/17）差异大，效果量直接对比需谨慎。\n- Section 5.2 的 Spearman ρ = 1.0 (N=8) 不具统计意义，论文已注释但可考虑删除。\n\n---\n\n### Questions for Authors\n\n1. N=17 的 100% exposure coverage 下（Exposed-only, 231 items），G-MFRM 与 raw average 的 τ 完全相同（0.779）。这是否意味着在充分 exposure 信息下，joint calibration 对排名没有增量价值？\n2. Murphy-Topel correction 后 c_n 覆盖率具体是多少？报告的 67.9–71% 是修正前还是修正后？\n3. Stage 2 的 gpt-4-0314 锚点若本身存在 contamination，exposure 估计是否会系统性偏倚？\n\n---\n\n### Missing References\n\n- SBC 文献（Talts et al., 2018）已在参考文献中但未用于 CI coverage 分析。\n- 无明显遗漏的关键 related work。\n\n---\n\n### 主要优势\n\n- 将 OVB 框架引入 MFRM 的 LLM 评测语境是新颖且有洞察力的视角。\n- Propositions 1–2 和 Theorem 1 的证明正确，Cauchy-Schwarz + Schur complement 路线简洁优雅。\n- 主实验负向结果的完整报告体现良好学术诚信。\n- Contamination susceptibility profile 与模型年龄的清晰梯度关系提供有实际意义的诊断信息。\n- 消融实验充分覆盖主要设计选择。",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-25T21:22:41.078470+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 10598
}
```

</details>

---


### Assistant

_source line 548 · 2026-05-25T21:22:49.510917+00:00_

审稿报告已提交给 Review Director。

总结：评分 **3.5 (Borderline Conference)**。三个 Must-Fix 问题：(1) N=17 主实验排名 Δτ 为负，唯一正向结果来自非显著的 N=8 pilot；(2) c_n 置信区间覆盖率仅 68–71%，Murphy-Topel 修正未解决；(3) OVB 线性近似 r=0.80，36% 方差未解释但以形式化结果呈现。理论贡献（identifiability 证明、OVB 视角）扎实，诊断功能有价值，但作为排名校准工具的实证支撑不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

4 recorded events


### User

_source line 549 · 2026-05-25T21:25:07.505122+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应，对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 或 [REBUT]，并提供理由（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 — 新颖性与完整性审查

### Overall: 3.0 / 5（Findings）

### Must-Fix 问题

**N1** [critical] 单一 benchmark 无法支撑标题和 abstract 中的通用性声明
- 全部真实数据实验仅使用 Arena-Hard（500 条多轮对话 item）。标题和 abstract 使用 "LLM Evaluation" 泛化表述。不同 benchmark 的 contamination 模式差异巨大（选择题 vs 开放生成 vs 代码），e_i 估计 pipeline 在非对话式 benchmark 上的行为未知。
- 建议：至少增加 1-2 个不同类型 benchmark，或将 claims 限定为 "conversational/open-ended evaluation"。

**N2** [critical] c_n 验证存在循环性，缺乏独立外部验证
- c_n 验证逻辑："older models have higher c_n → aligns with expectations → therefore c_n captures contamination" 仅为 face validity。
  (1) model age 与多种因素共变（架构复杂度、训练数据量、RLHF 质量）；
  (2) Stage 2 用 gpt-4-0314（老模型）作 anchor 可能引入系统性偏差；
  (3) N=8 Spearman ρ = 1.0 被论文自身承认 "not statistically remarkable"；
  (4) 没有对比独立 contamination indicator（membership inference、n-gram overlap、memorization probe）。
- 建议：使用已知 contaminated item subset 验证，或对比 Min-K% 等独立指标。

**N3** [critical] 主实验排名准确度低于所有 baseline，解释虽合理但替代假说未被排除
- N=17 Δτ = −0.044，全部 7 baseline 在 raw average ±0.015 内。Coverage ablation（Δτ: −0.044 → −0.015 → 0.000）兼容两种解释：修正越来越准确 OR 限制到高信噪比 item 后噪声被抑制。
- 建议：增加 random e_i placebo test；展示 synthetic data 在 coverage < 50% 时行为。

### Should-Fix 问题

**W1** [warning] OVB 形式化是教科书应用而非原创贡献
- Observation 1 直接将 Angrist & Pischke OVB 公式应用到 MFRM 线性预测器，是标准计量经济学工具的领域应用。

**W2** [warning] N=8 pilot 统计效力不足以支撑 contamination diagnostics 叙事权重
- N=8 posterior CI 很宽，N=17 vs N=8 的 c_n 不一致（GPT-3.5-Turbo: 5.60 vs 2.57）。

**W3** [warning] e_i 估计 pipeline 缺乏 ground truth 验证
- 权重 robustness（ρ≥0.998）只说明不同权重产生类似排序，不说明 e_i 准确。

**W4** [warning] Ground truth（Chatbot Arena 排名）本身存在偏差
- Kendall τ 衡量的是与另一个 biased ranking system 的一致性。

**W5** [warning] Table 1 caption "seven baselines" 列举不完整
- Caption 只列 5 个名称但声称 7 个；Table 本身无 per-baseline τ 值。

### Missing References
- Batsuren et al. 2024 "Evaluating LLMs with Item Response Theory"
- Stureborg et al. 2024 "Large Language Models are Inconsistent and Biased Evaluators"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-25T21:27:15.532931+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 单一 benchmark 无法支撑通用性声明**\n\n同意。标题/abstract 使用 \"LLM Evaluation\" 泛化表述，但实验仅基于 Arena-Hard。理论贡献是 benchmark-agnostic 的，但 Stage 2 exposure pipeline（Section 4.2）针对 pairwise comparison 设计，在选择题或代码生成 benchmark 上行为未知。Limitations 已承认此问题但标题/abstract 表述过宽。补充：建议将 claims 限定为 \"pairwise open-ended evaluation\" 或增加不同类型 benchmark。\n\n---\n\n**[AGREE] R2-N2: c_n 验证存在循环性**\n\n同意这是关键弱点。Model age 与 c_n 的相关性（Figure 5a）是 face validity，不构成 causal validation。论文提供的间接证据——LOO-ELPD（ΔELPD = −55.7, |Δ/SE| = 5.9; Appendix G）证明模型拟合优势而非 c_n 语义正确性；合成 recovery（r = 0.81）在已知 ground truth 下。缺乏独立外部指标（membership inference、Min-K%）的对比。\n\n---\n\n**[AGREE] R2-N3: 主实验排名低于 baseline，替代假说未被排除**\n\n与我的 N1 高度一致。R2 的替代假说 B（item filtering 移除高噪声 item，任何方法都会改善）未被排除。random e_i placebo test 是有效区分方法。补充：即使在 100% coverage 下（Exposed-only, 231 items），G-MFRM 仅与 raw average 持平（τ = 0.779, Table 1），未实现正向改进。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: OVB 形式化是教科书应用而非原创贡献**\n\n部分不同意。Observation 1 本身（Eq. 3）确实是标准 OVB 公式的领域应用，但 R2 忽略了论文在 OVB 之上的贡献链：(1) 识别 judge bias 与 contamination 在 MFRM 中的 confounding 结构——这个 problem formulation 是新的；(2) Identifiability 分析（Theorem 1, Appendix B）通过 Cauchy-Schwarz + Schur complement 建立 gated IRT 首个形式化条件，超越教科书 OVB；(3) G-MFRM 模型设计由 OVB motivate 但非直接推论。将整体贡献归为\"教科书应用\"低估了从 problem identification 到 identifiability proof 的完整理论链。但同意 Observation 1 本身新颖性有限，叙事应更清晰区分 motivation 和 contribution。\n\n---\n\n**[AGREE] R2-W2: N=8 pilot 统计效力不足**\n\n同意。Power analysis（Appendix J）承认 N=8 下 power ~50%。更关键的是 c_n 跨配置不一致：GPT-3.5-Turbo 在 N=8 中 c_n = 5.60，N=17 中降至 2.57（>2× 差异）。论文解释为 \"shrinkage from larger population\"（Section 5.2），但 hierarchical shrinkage 通常不产生如此剧烈变化。N=8 用 9 judges 而 N=17 用 6 judges，panel 完全不同也可能是原因。这强化了 c_n CI 覆盖率问题（我的 N2）。\n\n---\n\n**[AGREE] R2-W3: e_i pipeline 缺乏 ground truth 验证**\n\n同意。Appendix K 权重 robustness（ρ ≥ 0.998）证明内部一致性，不证明准确度。如果 e_i 的 ground truth bias 是系统性的，σ_crit 分析框架（假设 ε_i ~ N(0, σ²) i.i.d.）不适用。这是从合成到真实数据推广的核心薄弱环节。\n\n---\n\n**[REBUT] R2-W4: Chatbot Arena 排名本身存在偏差**\n\n部分不同意。Chatbot Arena 确有已知偏差，但：(1) 它是当前领域最广泛接受的 human preference ground truth；(2) Kendall τ 对 monotone transformation 不变，部分减轻 scale-level bias；(3) 系统性偏差同等影响所有方法，Δτ 相对比较仍有效。此批评适用于整个领域而非本文独有。但同意应在 Limitations 增加 ground truth 局限性讨论。\n\n---\n\n**[AGREE] R2-W5: Table 1 caption 列举不完整**\n\n同意。Caption 列举 5 个名称但声称 7 个 baseline（Section 5.2 列举完整：加 Raw Average 和 CyclicJudge+discard）。Table 1 未给出每个 baseline 独立 τ 值，仅用 \"within 0.015\" 概括，对完整性不足。\n\n---\n\n### Missing References 回应\n\n- Batsuren et al. 2024：与本文直接相关（IRT 用于 LLM 评测），应引用。\n- Stureborg et al. 2024：相关但非必须——论文已引用多篇 judge bias 文献（Section 2）。\n\n### 综合评估\n\nR2 和我的审稿在三个核心问题上高度一致：(1) 主实验排名退化（R2-N3 ≈ R1-N1）；(2) c_n 验证不足（R2-N2 补充了我未充分强调的循环性问题）；(3) 单一 benchmark 限制（R2-N1 比我更明确地指出标题/abstract 的过度泛化）。\n\nR2 提出的 random e_i placebo test（R2-N3）和独立 contamination indicator 对比（R2-N2）是具体可操作的改进建议。我对 R2-W1（OVB 非原创）和 R2-W4（ground truth 偏差）持部分不同意见——前者低估了完整理论链，后者是领域共性问题。\n\n维持我的评分：Overall 3.5 (Borderline Conference)。R2 的评分 3.0 (Findings) 也合理，两者差异主要在对理论贡献（identifiability proof）的权重不同。",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 单一 benchmark 无法支撑通用性声明**\n\n同意。标题/abstract 使用 \"LLM Evaluation\" 泛化表述，但实验仅基于 Arena-Hard。理论贡献是 benchmark-agnostic 的，但 Stage 2 exposure pipeline（Section 4.2）针对 pairwise comparison 设计，在选择题或代码生成 benchmark 上行为未知。Limitations 已承认此问题但标题/abstract 表述过宽。补充：建议将 claims 限定为 \"pairwise open-ended evaluation\" 或增加不同类型 benchmark。\n\n---\n\n**[AGREE] R2-N2: c_n 验证存在循环性**\n\n同意这是关键弱点。Model age 与 c_n 的相关性（Figure 5a）是 face validity，不构成 causal validation。论文提供的间接证据——LOO-ELPD（ΔELPD = −55.7, |Δ/SE| = 5.9; Appendix G）证明模型拟合优势而非 c_n 语义正确性；合成 recovery（r = 0.81）在已知 ground truth 下。缺乏独立外部指标（membership inference、Min-K%）的对比。\n\n---\n\n**[AGREE] R2-N3: 主实验排名低于 baseline，替代假说未被排除**\n\n与我的 N1 高度一致。R2 的替代假说 B（item filtering 移除高噪声 item，任何方法都会改善）未被排除。random e_i placebo test 是有效区分方法。补充：即使在 100% coverage 下（Exposed-only, 231 items），G-MFRM 仅与 raw average 持平（τ = 0.779, Table 1），未实现正向改进。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: OVB 形式化是教科书应用而非原创贡献**\n\n部分不同意。Observation 1 本身（Eq. 3）确实是标准 OVB 公式的领域应用，但 R2 忽略了论文在 OVB 之上的贡献链：(1) 识别 judge bias 与 contamination 在 MFRM 中的 confounding 结构——这个 problem formulation 是新的；(2) Identifiability 分析（Theorem 1, Appendix B）通过 Cauchy-Schwarz + Schur complement 建立 gated IRT 首个形式化条件，超越教科书 OVB；(3) G-MFRM 模型设计由 OVB motivate 但非直接推论。将整体贡献归为\"教科书应用\"低估了从 problem identification 到 identifiability proof 的完整理论链。但同意 Observation 1 本身新颖性有限，叙事应更清晰区分 motivation 和 contribution。\n\n---\n\n**[AGREE] R2-W2: N=8 pilot 统计效力不足**\n\n同意。Power analysis（Appendix J）承认 N=8 下 power ~50%。更关键的是 c_n 跨配置不一致：GPT-3.5-Turbo 在 N=8 中 c_n = 5.60，N=17 中降至 2.57（>2× 差异）。论文解释为 \"shrinkage from larger population\"（Section 5.2），但 hierarchical shrinkage 通常不产生如此剧烈变化。N=8 用 9 judges 而 N=17 用 6 judges，panel 完全不同也可能是原因。这强化了 c_n CI 覆盖率问题（我的 N2）。\n\n---\n\n**[AGREE] R2-W3: e_i pipeline 缺乏 ground truth 验证**\n\n同意。Appendix K 权重 robustness（ρ ≥ 0.998）证明内部一致性，不证明准确度。如果 e_i 的 ground truth bias 是系统性的，σ_crit 分析框架（假设 ε_i ~ N(0, σ²) i.i.d.）不适用。这是从合成到真实数据推广的核心薄弱环节。\n\n---\n\n**[REBUT] R2-W4: Chatbot Arena 排名本身存在偏差**\n\n部分不同意。Chatbot Arena 确有已知偏差，但：(1) 它是当前领域最广泛接受的 human preference ground truth；(2) Kendall τ 对 monotone transformation 不变，部分减轻 scale-level bias；(3) 系统性偏差同等影响所有方法，Δτ 相对比较仍有效。此批评适用于整个领域而非本文独有。但同意应在 Limitations 增加 ground truth 局限性讨论。\n\n---\n\n**[AGREE] R2-W5: Table 1 caption 列举不完整**\n\n同意。Caption 列举 5 个名称但声称 7 个 baseline（Section 5.2 列举完整：加 Raw Average 和 CyclicJudge+discard）。Table 1 未给出每个 baseline 独立 τ 值，仅用 \"within 0.015\" 概括，对完整性不足。\n\n---\n\n### Missing References 回应\n\n- Batsuren et al. 2024：与本文直接相关（IRT 用于 LLM 评测），应引用。\n- Stureborg et al. 2024：相关但非必须——论文已引用多篇 judge bias 文献（Section 2）。\n\n### 综合评估\n\nR2 和我的审稿在三个核心问题上高度一致：(1) 主实验排名退化（R2-N3 ≈ R1-N1）；(2) c_n 验证不足（R2-N2 补充了我未充分强调的循环性问题）；(3) 单一 benchmark 限制（R2-N1 比我更明确地指出标题/abstract 的过度泛化）。\n\nR2 提出的 random e_i placebo test（R2-N3）和独立 contamination indicator 对比（R2-N2）是具体可操作的改进建议。我对 R2-W1（OVB 非原创）和 R2-W4（ground truth 偏差）持部分不同意见——前者低估了完整理论链，后者是领域共性问题。\n\n维持我的评分：Overall 3.5 (Borderline Conference)。R2 的评分 3.0 (Findings) 也合理，两者差异主要在对理论贡献（identifiability proof）的权重不同。",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-25T21:27:19.717147+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4184
}
```

</details>

---


### Assistant

_source line 552 · 2026-05-25T21:27:25.667715+00:00_

交叉回应已提交。总结：

- **AGREE** 6 条（R2-N1, N2, N3, W2, W3, W5）——与我的审稿意见高度一致，特别是主实验排名退化、c_n 验证循环性、e_i 缺乏 ground truth 三个核心问题。
- **REBUT** 2 条（R2-W1, W4）——OVB 形式化虽非原创但完整理论链有增量贡献；Chatbot Arena 偏差是领域共性问题。
- 维持评分 3.5 (Borderline Conference)，与 R2 的 3.0 差异在于对 identifiability proof 理论贡献的权重不同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---
