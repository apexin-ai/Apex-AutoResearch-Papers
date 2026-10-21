# review caption consistency

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_review_caption_consistency_20260523T173725.jsonl`
- **Structured JSON:** [`82bcaea2d8fc110c9243.json`](../../sessions/82/82bcaea2d8fc110c9243.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-23T17:44:08.585015+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T17:44:08.585323+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T17:44:08.585514+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root/nlp_variance_gtheory -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root/nlp_variance_gtheory -name \"*.tex\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T17:44:08.585655+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.04}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T17:44:08.585805+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls -la /root/nlp_variance_gtheory/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls -la /root/nlp_variance_gtheory/"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T17:44:08.585954+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1432\\ndrwxr-xr-x 10 root root   4096 May 24 00:12 .\\ndrwx------  1 root root   4096 May 23 23:26 ..\\ndrwxr-xr-x  3 root root     30 May 21 12:21 artifacts\\ndrwxr-xr-x  3 root root   4096 May 23 22:50 data\\n-rw-r--r--  1 root root  10283 May 21 02:38 design_matrix.csv\\n-rw-r--r--  1 root root 291866 May 21 07:01 design_matrix_exp001.csv\\n-rw-r--r--  1 root root 291866 May 21 08:56 design_matrix_exp001_full.csv\\n-rw-r--r--  1 root root  79781 May 21 06:09 design_matrix_exp001_llama.csv\\n-rw-r--r--  1 root root 126437 May 21 06:13 design_matrix_exp001_llama_local.csv\\n-rw-r--r--  1 root root 413327 May 21 16:37 design_matrix_exp002.csv\\n-rw-r--r--  1 root root  24662 May 22 12:27 design_matrix_exp003_3b.csv\\n-rw-r--r--  1 root root  25058 May 22 13:12 design_matrix_exp003_72b.csv\\n-rw-r--r--  1 root root  24662 May 22 12:47 design_matrix_exp003_7b.csv\\n-rw-r--r--  1 root root  49622 May 22 12:26 design_matrix_exp003_scale.csv\\ndrwxr-xr-x  3 root root     27 May 22 20:17 figures\\ndrwxr-xr-x  2 root root     31 May 21 03:57 models\\n-rw-r--r--  1 root root  16155 May 23 17:09 partial_credit_multimodel.py\\n-rw-r--r--  1 root root    321 May 20 23:03 pyproject.toml\\n-rw-r--r--  1 root root    252 May 21 06:05 requirements.txt\\ndrwxr-xr-x 17 root root   4096 May 23 17:09 results\\n-rw-r--r--  1 root root   4306 May 21 03:11 run_bf16_eager.py\\n-rwxr-xr-x  1 root root   1442 May 21 02:44 run_float32_only.sh\\n-rwxr-xr-x  1 root root   1408 May 21 02:45 run_float32_v0.sh\\n-rwxr-xr-x  1 root root   1198 May 21 02:37 run_full_mvp.sh\\n-rwxr-xr-x  1 root root    363 May 24 00:12 run_mmlu_after.sh\\n-rwxr-xr-x  1 root root   1504 May 20 23:04 run_mvp.sh\\n-rw-r--r--  1 root root    798 May 21 14:10 run_reml_500.py\\n-rwxr-xr-x  1 root root    289 May 21 14:13 run_reml_500.sh\\n-rw-r--r--  1 root root   1225 May 21 14:16 run_reml_500_v2.py\\n-rw-r--r--  1 root root   1300 May 21 14:20 run_reml_500_v3
…[truncated 402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T17:44:08.586125+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root -name \"*.tex\" -type f -maxdepth 5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root -name \"*.tex\" -type f -maxdepth 5"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T17:44:08.586259+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T17:44:08.586379+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T17:44:08.586528+00:00_

artifacts/dream_reports/dream_20260520T190053/best/paper.tex
artifacts/dream_reports/dream_20260520T190053/median/paper.tex
artifacts/dream_reports/dream_20260520T190053/worst/paper.tex
artifacts/dream_reports/dream_20260520T222113/best/paper.tex
artifacts/dream_reports/dream_20260520T222113/median/paper.tex
artifacts/dream_reports/dream_20260520T222113/worst/paper.tex
artifacts/dream_reports/dream_20260521T032813/best/paper.tex
artifacts/dream_reports/dream_20260521T032813/median/paper.tex
artifacts/dream_reports/dream_20260521T032813/worst/paper.tex
artifacts/dream_reports/dream_20260521T044739/best/paper.tex
artifacts/dream_reports/dream_20260521T044739/median/paper.tex
artifacts/dream_reports/dream_20260521T044739/worst/paper.tex
artifacts/dream_reports/dream_20260521T075006/best/paper.tex
artifacts/dream_reports/dream_20260521T075006/median/paper.tex
artifacts/dream_reports/dream_20260521T075006/worst/paper.tex
artifacts/dream_reports/dream_20260521T122449/best/paper.tex
artifacts/dream_reports/dream_20260521T122449/median/paper.tex
artifacts/dream_reports/dream_20260521T122449/worst/paper.tex
artifacts/_project/paper/experiments.tex
docs/paper/sections/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/limitations.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/conclusion.tex
docs/paper/abstract.tex
docs/paper/limitations.tex
docs/paper/experiments.tex
docs/paper/method.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T17:44:08.586683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T17:44:08.586813+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	
11	\usepackage{graphicx}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Study of 7--9B Instruction-Tuned Models}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\input{conclusion}
44	
45	% === LIMITATIONS ===
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	% === APPENDIX ===
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T17:44:08.586943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T17:44:08.587123+00:00_

1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 58.4\% of total variance, with the residual term contributing 23.1\%. All main facet effects are negligible ($<$1\% each): precision 0.9\%, prompt template, temperature, seed, and ordering each $<$0.5\%. The interesting structure appears in item-conditional interactions: prompt$\times$item is the largest at 5.5\%, followed by seed$\times$item (4.7\%), precision$\times$item (3.3\%), temperature$\times$item (2.9\%), and ordering$\times$item (0.8\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.936$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 55 items in this multi-facet design.
14	
15	For text-exact-match scoring (requiring verbatim string matches), the variance structure shifts dramatically: te
…[truncated 9407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T17:44:08.587266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T17:44:08.587481+00:00_

1	\section{Method and Experimental Design}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \cite{efron1993bootstrap} (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel} = \sum_i \sigma^2_{p \times f_i} / n_{f_i} + \sigma^2_\text{residual} / \prod_i n_{f_i}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. A D-study projects 
…[truncated 11788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T17:44:08.587644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T17:44:08.587791+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	In our analysis of five benchmarks, item selection drives 34--38\% of evaluation variance on multiple-choice tasks while prompt wording is negligible ($<$3\%). On the free-form reasoning task GSM8K, the structure shifts: model$\times$prompt interaction alone accounts for approximately 9\%, while item selection drops to 17\%. These numbers, drawn from a factorial analysis of approximately 2.3 million evaluation records, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \citep{rodriguez2021leaderboards, dehghani2021benchmark}. No study has simultaneously crossed infrastructure and methodology facets in a unified factorial design across benchmarks to decompose these sources, quantify their interactions, and compare the resulting variance structure.
5	
6	Existing studies examine individual variance sources in isolation. \citet{sclar2024formatting} and BrittleBench \citep{brittlebench2026} documented 50--76\% accuracy swings from prompt formatting; \citet{yuan2025layercast} showed up to 9\% variation from numerical precision; \citet{pezeshkpour2024ordering}, \citet{dodge2020finetuning}, and \citet{henderson2018deep} documented ordering and hyperparameter sensitivity---each holding other factors fixed. \citet{messing2026hidden} applied G-theory to LLM evaluation across five methodology facets on a single benchmark (j
…[truncated 2900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T17:44:08.587951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T17:44:08.588100+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Variance Decomposition in ML/NLP Evaluation.}
5	Factorial decomposition of evaluation variance has roots in the ML reproducibility literature. \citet{bouthillier2021accounting} introduced an ANOVA-based template that decomposes benchmark variance across implementation details, hyperparameters, and data splits, establishing that design choices account for a substantial share of reproducibility failures. Subsequent studies applied similar decomposition to specific evaluation facets \citep{dodge2020finetuning, henderson2018deep, magnusson2023reproducibility}. \citet{messing2026hidden} brought Generalizability theory into LLM evaluation, decomposing variance across five methodology facets on a single benchmark (judge identity: 43.8\%; see Positioning below for detailed comparison). \citet{madaan2024quantifying} proposed per-factor variance metrics for LLM evaluation benchmarks but did not cross factors simultaneously. Holistic evaluation frameworks \citep{liang2023helm, kiela2021dynabench} standardize multi-scenario comparison but do not decompose variance sources. \citet{blackwell2024towards} quantified uncertainty in benchmark scores, and \citet{qian2026benchmark} conducted systematic meta-evaluation of LLM benchmarks; \citet{burnell2023rethink} called for rethinking evaluation reporting standards; \citet{saxon2024metrology} advocated model metrology as a framework for rigorous benchmark design. Recently, G-theory has been applied to LLM-based writing assessment \citep{wei2025gtheory} and annotation reliability \citep{varannot2025gtheory}, but these studies address scoring consistency rather than benchmark evaluation variance. \citet{kunievsky2025intent} proposed an alternative decomposition that separates intent uncertainty, articulation variance, and model uncertainty, but this framework does not cross infrastructure and methodology facets in a factorial design. Our work extends these approaches by cross
…[truncated 4652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T17:44:08.588242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T17:44:08.588365+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	A recommended 3-prompt $\times$ 3-seed design reduces item requirements from 552 to 178 for $G \geq 0.80$, confirmed across five benchmarks under binary scoring; multi-facet designs minimize items when item construction is costly, while single-condition designs suit compute-constrained settings. $G_\text{item}$ and $G_\text{model}$ have different bottlenecks---item count for the former, prompt standardization for the latter---providing orthogonal optimization paths: adding items improves item reliability, while controlling prompt and seed conditions improves model discriminability. All budgets assume binary scoring; extending to other model scales and continuous metrics is a priority. We recommend that benchmark designers adopt multi-facet validation (at minimum 3 prompts $\times$ 3 seeds) as standard practice when sizing pilot studies, and that leaderboard operators average over prompt and seed conditions to improve ranking stability. Code, data, and a D-study calculator will be released upon publication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T17:44:08.588508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T17:44:08.588628+00:00_

1	Large Language Model (LLM) evaluation results vary across reproductions, but variance sources interact, and their relative importance shifts with the benchmark format. We apply Generalizability theory (G-theory) in a fully crossed design with up to seven facets across eight open-weight instruction-tuned models (7--9B parameters) and five benchmarks, totaling approximately 2.3 million evaluation records. D-study projections show that, under binary correctness scoring, a recommended multi-condition design achieves $G \geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\times$ item reduction over single-condition designs (552 items, 552 evaluations)---trading approximately 3$\times$ more total evaluations for 3$\times$ fewer items, a tradeoff that favors multi-condition designs when item construction is costly. Model$\times$item interaction (up to 36\%) indicates that models differ primarily in which items they find difficult, not in overall ability. Preliminary validation across a 3B--72B parameter range confirms stable variance structure within one architecture family. We release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T17:44:08.588754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T17:44:08.588878+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Our eight models share the 2024--2025 instruction-tuning paradigm; temporal correlation may limit exchangeability, and results do not generalize to API-based or base models. Preliminary within-family 72B validation (\S4.6) suggests stable variance structure across scales, but is limited to a single architecture (Qwen2.5); the Qwen2.5 family shares training recipes and tokenizer, so validating with architecturally distinct families (e.g., Llama-3 70B, Mistral-Large) is necessary before extrapolating budget recommendations to arbitrary model families.
5	
6	The benchmark sample ($n = 5$) limits statistical power for format-associated observations ($p = 0.10$); other formats (code generation, multi-turn dialogue) may differ. All D-study budgets reported in this paper are strictly valid only under binary correctness scoring. Our partial-credit analysis (GSM8K, 8 models) shows $G$ drops from 0.86 to 0.77 (crossed design) with all models showing $G_\text{partial} < G_\text{binary}$, suggesting limited transferability to finer-grained scoring rubrics; the analysis is limited to a single benchmark, and its generalizability to other tasks is unknown. Our temperature range (0.0--0.7) does not cover high-temperature regimes ($\tau > 1.0$) sometimes used in generation tasks. Our design varies few-shot example ordering but not example identity, a known variance source. Results depend on vLLM~0.9.2; different inference engines or vLLM versions may alter CUDA-level nondeterminism patterns.
7	
8	All eight models may have encountered benchmark items during pre-training; differential contamination across architectures could inflate model$\times$item interaction \citep{golchin2023contamination, oren2024proving}, though consistent variance structures across three independently constructed MC benchmarks provide indirect evidence against contamination as the sole driver. Contamination affects absolute budget estimates but has limited 
…[truncated 130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T17:44:08.589009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T17:44:08.589279+00:00_

1	\appendix
2	\section{Additional Robustness Analyses}
3	\label{app:robustness}
4	
5	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
6	
7	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
8	
9	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
10	
11	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
12	
13	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings, excluding residual; \texttt{item\_id} dominant in all 100 replications; top-5 ordering correct in 79\% of replications). Bias analysis by difficulty stratum shows $|\text{bias}| = 0.28$--$0.37$ for items with $p \in [0.5, 0.8]$, where the Bernoulli variance ceiling $p(1{-}p)$ is largest. This an
…[truncated 26927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T17:44:08.589584+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/figures/paper/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/figures/paper/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T17:44:08.589726+00:00_

figures/paper/gen_fig2_design_diagram.py
figures/paper/fig2_design_diagram.pdf
figures/paper/fig2_design_diagram.png
figures/paper/fig1_cross_benchmark.pdf.bak
figures/paper/gen_fig3_dstudy_curves.py
figures/paper/fig3_dstudy_curves.pdf
figures/paper/fig3_dstudy_curves.png
figures/paper/fig4_difficulty_scatter.pdf
figures/paper/gen_fig1_cross_benchmark.py
figures/paper/fig1_cross_benchmark.png
figures/paper/fig1_cross_benchmark.pdf.bak2
figures/paper/fig1_cross_benchmark.pdf
figures/paper/plot_teaser_dstudy.py
figures/paper/fig0_teaser_dstudy.pdf
figures/paper/fig0_teaser_dstudy.png
figures/paper/budget_sensitivity_band.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T17:44:08.589850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/sections/experiments.tex",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/sections/experiments.tex",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T17:44:08.589982+00:00_

1	\section{Experiments}
2	
3	We apply the G-theory framework from Section~3 to a fully crossed evaluation design spanning multiple models, benchmarks, and methodological facets. All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on NVIDIA RTX PRO 6000 GPUs (96GB). Binary correctness (1/0) serves as the primary outcome measure throughout; generation-based scoring avoids the log-likelihood artifacts identified by \citet{hua2025flaw}.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 239,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 61.1\% of total variance, with the residual term contributing 19.5\%. All main facet effects are negligible ($<$1\% each): prompt template 0.3\%, temperature 0.2\%, precision 0.1\%, seed $<$0.1\%, ordering $<$0.1\%. The interesting structure appears in item-conditional interactions: precision$\times$item contributes 7.2\%, temperature$\times$item 6.9\%, and prompt$\times$item 5.7\%. This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.918$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 72 items in thi
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T17:44:08.590123+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\S\\d",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\S\\d",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T17:44:08.590239+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T17:44:08.590381+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "§\\d|\\\\S\\d",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Grep",
  "tool_args": {
    "pattern": "§\\d|\\\\S\\d",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T17:44:08.590536+00:00_

docs/paper/experiments.tex:80:Under binary scoring, BF16 and FP16 are functionally interchangeable ($<$0.1\% interaction \cite{yuan2025layercast}); under text-exact-match, a precision$\times$temperature interaction emerges at 1.3\%, consistent with \S4.1. Precision need not be controlled for binary evaluation at BF16/FP16 \cite{shanmugavelu2024floating}.
docs/paper/experiments.tex:113:\paragraph{Projection assumptions.} Cross-model budgets increase to 93 items because model$\times$item interaction enters relative error variance. Bootstrap CIs (71--162 items) and LOMO analysis (Appendix~\ref{app:robustness}) assess stability; $G_\text{item}$ is stable across benchmarks (0.863--0.896, CV = 1.4\%; Appendix~\ref{app:cross_benchmark_transfer}). All projections assume the 2024--2025 model generation; the 72B extension (\S4.6) provides preliminary support.
docs/paper/sections/experiments.tex:144:% [PLACEHOLDER: §4.7 Extended Results — 8-model × 5-benchmark expansion]
docs/paper/method.tex:27:[Omitted long matching line]
docs/paper/method.tex:79:[Omitted long matching line]
docs/paper/method.tex:83:[Omitted long matching line]
docs/paper/limitations.tex:4:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_caption_consistency_20260523T173725",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-23T17:44:08.590761+00:00_

Analysis complete. Here's the full consistency check report.

---

## Figure/Table Caption 一致性检查报告

### 1. 所有 Figure/Table 列表

**Figures（按编译顺序）：**

| 编号 | Label | 文件 | Caption 简述 |
|------|-------|------|-------------|
| Fig 1 | `fig:teaser` | introduction.tex:13 | D-study projections for MMLU (single-model baseline) |
| Fig 2 | `fig:design_diagram` | method.tex:58 | Fully crossed G-theory design (7 facets) |
| Fig 3 | `fig:cross_benchmark` | experiments.tex:75 | Variance decomposition across 5 benchmarks and 8 models |
| Fig 4 | `fig:budget_sensitivity` | appendix.tex:137 | Budget sensitivity to estimation error |
| Fig 5 | `fig:difficulty_scatter` | appendix.tex:189 | Item difficulty heterogeneity vs item variance share |

**Tables（按编译顺序）：**

| 编号 | Label | 文件 | Caption 简述 |
|------|-------|------|-------------|
| Tab 1 | `tab:design_matrix` | method.tex:34 | Fully crossed G-theory design matrix |
| Tab 2 | `tab:cross_model` | experiments.tex:23 | Cross-model MMLU variance decomposition |
| Tab 3 | `tab:cross_benchmark` | experiments.tex:52 | Format-associated variance across 5 benchmarks |
| Tab 4 | `tab:dstudy` | experiments.tex:91 | D-study reproducibility budgets (single-model) |
| Tab 5 | `tab:lomo_full` | appendix.tex:25 | LOMO stability across 5 benchmarks |
| Tab 6 | `tab:fixed_vs_random` | appendix.tex:51 | Random vs fixed model G coefficients |
| Tab 7 | `tab:dstudy_cross` | appendix.tex:79 | Cross-model D-study budgets with CIs |
| Tab 8 | `tab:forward_pred` | appendix.tex:108 | Four-model vs eight-model consistency |
| Tab 9 | `tab:intermediate_dstudy` | appendix.tex:151 | Intermediate D-study designs |
| Tab 10 | `tab:subject_gstudy` | appendix.tex:201 | MMLU subject-level variance |
| Tab 11 | `tab:ff_residual` | appendix.tex:236 | FF residual variance regression |
| Tab 12 | `tab:model_ids` | appendix.tex:260 | Model HuggingFace identifiers |

---

### 2. Figure 1 caption vs Table 3 数字对比

**Figure 1 caption 中的数字**：552 items, 178 items, 55 items (MMLU single-model D-study budgets)
**Table 3 中的数字**：per-benchmark variance percentages (cross-model, 8 models)

这两者是**不同分析**（single-model D-study vs. cross-benchmark variance decomposition），不存在直接对应关系。Figure 1 的数字与 **Table 4**（`tab:dstudy`）对应，经核验全部一致：
- Multi-facet: 55 items, G_200 = .936 ✓
- Single-condition: 552 items, G_200 = .592 ✓
- 3p×3s moderate: 178 items (from Table 9) ✓

---

### 3. 正文数字 vs 表格数字一致性

**已验证一致的数字（✓）：**
- item_id 58.4% → 37.9% cross-model (experiments.tex:19 vs Tab 2) ✓
- model×item 30.2% (experiments.tex:19 vs Tab 2) ✓
- model×item up to 36% (HellaSwag, Tab 3) ✓
- MC item-related variance 68–72% (Tab 3 计算：68.1%, 71.6%, 70.3%) ✓
- FF item-related variance 31–41% (Tab 3 计算：31.5%, 41.3%) ✓
- HellaSwag exception 36.0% > 34.3% (Fig 3 caption vs Tab 3) ✓
- 552/55 = 10.0× budget ratio (experiments.tex:86 vs Tab 4) ✓
- IRT 116 items: G=0.457 single, G=0.895 multi (experiments.tex:109 vs Tab 4) ✓
- |ΔG| ≤ 0.029 MC, ≤ 0.065 FF (experiments.tex:109 vs Tab 8) ✓
- G_item 0.863–0.896 range (experiments.tex:113 vs Tab 5) ✓
- Fixed vs random ΔG 0.077–0.113 (experiments.tex:119 vs Tab 6) ✓
- Total records 460,800 and 2,304,000 (math verified) ✓
- 1,296 conditions per item (math verified) ✓
- 178 × 9 = 1,602 evaluations (math verified) ✓
- 55 × 1,296 = 71,280 evaluations (Tab 4) ✓
- ARC model×prompt 8.0%, GSM8K model×prompt 8.5% (method.tex:85 vs Tab 3) ✓

---

### 4. 发现的不一致/问题

#### 问题 A：Model main effect 范围不精确（experiments.tex:19）

正文：`model main effect is 3--5\% (MC) and 9--11\% (FF)`

Table 3 实际值：
- MC: MMLU **2.8%**, ARC 3.1%, HellaSwag 5.4% → 实际范围 **2.8–5.4%**，不是 3–5%
- FF: MATH **8.5%**, GSM8K 10.7% → 实际范围 **8.5–10.7%**，不是 9–11%

MMLU 的 2.8% 和 MATH 的 8.5% 都低于正文声称的下限。

#### 问题 B：Introduction 中 model×prompt "approximately 9%" 偏高（introduction.tex:4）

正文：`model×prompt interaction alone accounts for approximately 9%`（指 GSM8K）
Table 3：GSM8K model×prompt = **8.5%**

8.5% 说成 "approximately 9%" 是可以接受的近似，但作为 Introduction 中的关键数字，建议精确为 "approximately 8.5%" 或 "nearly 9%"。

#### 问题 C：Multi-facet budget "71 to 162 items" 混淆点估计与 CI（experiments.tex:111）

正文：`multi-facet budgets ranging from 71 to 162 items (Table~\ref{tab:dstudy_cross})`

Table 7 实际值：
- **点估计**范围：93–128 items
- **95% CI** 全范围：71（ARC 下限）– 162（GSM8K 上限）

正文的 71–162 是 CI 的极端边界，但写法 "budgets ranging from 71 to 162" 读起来像点估计范围。建议明确标注为 CI 范围。

#### 问题 D：三处硬编码章节号（应使用 `\ref{}`）

| 位置 | 硬编码 | 应引用的 subsection |
|------|--------|-------------------|
| experiments.tex:80 | `\S4.1` | Single-Model Baseline（无 label） |
| experiments.tex:113 | `\S4.6` | Preliminary Scale Validation（无 label） |
| limitations.tex:4 | `\S4.6` | 同上 |

这两个 subsection 缺少 `\label{}`，若章节重排，引用会错乱。

#### 问题 E：`\label{sec:partial_credit}` 定义但未引用

appendix.tex:42 定义了 `\label{sec:partial_credit}`，但全文无 `\ref{sec:partial_credit}`。

#### 问题 F：`docs/paper/sections/experiments.tex` 是过期版本

该文件包含旧数据（4 models, 239,200 records, item_id=61.1%, G=0.918），与当前 `docs/paper/experiments.tex`（8 models, 259,200 records, item_id=58.4%, G=0.936）严重不一致。`main.tex` 引用的是后者，但旧文件的存在可能造成混淆。

#### 问题 G：`fig3_dstudy_curves.pdf` 为孤立图片

`figures/paper/` 中存在 `fig3_dstudy_curves.pdf`，但无 tex 文件引用它。

---

### 5. Label 一致性

**所有 `\ref{}` 均指向已定义的 `\label{}`**，无悬空引用。✓

**未引用的 labels**（不影响编译，但可考虑清理）：
`sec:introduction`, `sec:related`, `sec:method`, `sec:gtheory`, `sec:exp001`, `sec:protocol`, `sec:conclusion`, `sec:partial_credit`, `app:ai-assistants`, `app:budget_sensitivity`

---

### 总结

- **严重问题**：0 个（无悬空引用、无数字矛盾到影响结论的程度）
- **需修正**：问题 A（model main effect 范围偏差）、问题 D（硬编码章节号）
- **建议改进**：问题 B（近似精度）、问题 C（CI 标注）、问题 F（删除旧文件）
- **低优先级**：问题 E（unused label）、问题 G（orphan figure）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_caption_consistency_20260523T173725"
}
```

</details>

---
