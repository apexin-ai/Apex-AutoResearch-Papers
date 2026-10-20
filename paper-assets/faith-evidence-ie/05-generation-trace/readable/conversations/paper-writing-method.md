# paper writing method

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 107
- **Recorded user turns:** 0
- **Tool calls:** 53
- **Original source:** `logs/chats/worker_paper_writing_method_20260517T162426.jsonl`
- **Structured JSON:** [`7e0bc3d52079dd7c80ef.json`](../../sessions/7e/7e0bc3d52079dd7c80ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

107 recorded events

### Tool call

_source line 1 · 2026-05-17T16:29:59.470709+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T16:29:59.471158+00:00_

docs/paper/acl-style/acl_lualatex.tex
docs/paper/acl-style/acl_latex.tex
docs/paper/main.tex
docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T16:29:59.471504+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/**/*.bib"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T16:29:59.471659+00:00_

docs/paper/acl-style/custom.bib
docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T16:29:59.471785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T16:29:59.472033+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Dataset.}
8	We conduct experiments on DocRED~\citep{yao2019docred}, a large-scale document-level relation extraction benchmark containing 3,053 training and 998 development documents spanning 96 relation types. Each document requires identifying relational triples across multiple sentences and grounding each triple with supporting evidence sentences. We use Re-DocRED~\citep{tan2022redocred} for cross-dataset generalization evaluation.
9	
10	\paragraph{Models.}
11	Our primary model is Qwen3-4B. To study scale effects, we additionally train Qwen3-1.7B and Qwen3-8B under identical configurations. We include LLaMA-3.1-8B as a cross-family validation point.
12	
13	\paragraph{Training.}
14	All models use LoRA~\citep{hu2022lora} with rank $r{=}64$ and $\alpha{=}128$ over a structured output format that jointly produces relation triples and evidence sentences. For RSFT, we sample $N{=}8$ candidate outputs per document and select the top-$k{=}1$ response ranked by CED scoring (\S\ref{sec:ced}), which combines NLI-based evidence faithfulness with extraction accuracy. GRPO experiments use group sizes $G{=}4$ (QLoRA, 4-bit) and $G{=}8$ (bf16 full-precision LoRA). DPO constructs preference pairs from CED-ranked outputs.
15	
16	\paragraph{Metrics.}
17	We report five metrics. \textbf{Ign-F1} is the primary DocRED metric that ignores triples appearing in the training set, matching the official leaderboard protocol. \textbf{Rel-F1} measures relation extraction F1 on all triples. \textbf{Evi-F1 (TP-only)} measures evidence sentence F1 conditioned on correctly predicted triples, reflecting evidence quality independent of extraction errors. \textbf{Evi-F1 (joint)} includes false-positive and false-negative triples in the denominator following the DREEAM protocol~\citep{ma2023dreeam}, enabling cross-method evidence comparison. \textbf{EDCR} (Evidence-Decoupling Rati
…[truncated 13562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T16:29:59.472205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T16:29:59.472368+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{xcolor}
16	\usepackage{multirow}
17	\usepackage{subcaption}
18	
19	\graphicspath{{../../figures/paper/}}
20	
21	\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/analysis}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	\bibliographystyle{acl_natbib}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T16:29:59.472514+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T16:29:59.472635+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T16:29:59.472810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T16:29:59.472940+00:00_

File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T16:29:59.473064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/custom.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/custom.bib"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T16:29:59.473209+00:00_

1	% Use this file for citations not found in the ACL Anthology (contained in "anthology.bib").
2	
3	@book{Aho:72,
4	    author  = {Alfred V. Aho and Jeffrey D. Ullman},
5	    title   = {The Theory of Parsing, Translation and Compiling},
6	    year    = "1972",
7	    volume  = "1",
8	    publisher = {Prentice-Hall},
9	    address = {Englewood Cliffs, NJ}
10	}
11	
12	@book{APA:83,
13	    author  = {{American Psychological Association}},
14	    title   = {Publications Manual},
15	    year    = "1983",
16	    publisher = {American Psychological Association},
17	    address = {Washington, DC}
18	}
19	
20	@article{Chandra:81,
21		author = {Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer},
22		year = "1981",
23		title = {Alternation},
24		journal = {Journal of the Association for Computing Machinery},
25		volume = "28",
26		number = "1",
27		pages = "114--133",
28		doi = "10.1145/322234.322243",
29	}
30	
31	@inproceedings{andrew2007scalable,
32	  title={Scalable training of {L1}-regularized log-linear models},
33	  author={Andrew, Galen and Gao, Jianfeng},
34	  booktitle={Proceedings of the 24th International Conference on Machine Learning},
35	  pages={33--40},
36	  year={2007},
37	}
38	
39	@book{Gusfield:97,
40	    author  = {Dan Gusfield},
41	    title   = {Algorithms on Strings, Trees and Sequences},
42	    year    = "1997",
43	    publisher = {Cambridge University Press},
44	    address = {Cambridge, UK}
45	}
46	
47	@article{rasooli-tetrault-2015,
48	    author    = {Mohammad Sadegh Rasooli and Joel R. Tetreault},
49	    title     = {Yara Parser: {A} Fast and Accurate Dependency Parser},
50	    journal   = {Computing Research Repository},
51	    volume    = {arXiv:1503.06733},
52	    year      = {2015},
53	    url       = {http://arxiv.org/abs/1503.06733},
54	    note    = {version 2}
55	}
56	
57	@article{Ando2005,
58		Acmid = {1194905},
59		Author = {Ando, Rie Kubota and Zhang, Tong},
60		Issn = {1532-4435},
61		Issue_Date = {12/1/2005},
62		Journal = {J
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T16:29:59.473424+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find citation keys and project context",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/, I need to find:\n\n1. Any literature_map.yaml or similar file that contains citation keys (bibtex keys) for papers like DeepSeekMath/GRPO, DPO (Rafailov), STaR (Zelikman), SAIS, DREEAM, LoRA, DocRED, etc.\n2. Any existing method.tex file\n3. Any ideas.md, report.md, or ROADMAP.md that might describe the method in more detail\n\nSearch broadly - check docs/, artifacts/, knowledge/, and any other directories. Report what you find, including the actual citation keys if they exist in any bib or yaml file."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find citation keys and project context",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/, I need to find:\n\n1. Any literature_map.yaml or similar file that contains citation keys (bibtex keys) for papers like DeepSeekMath/GRPO, DPO (Rafailov), STaR (Zelikman), SAIS, DREEAM, LoRA, DocRED, etc.\n2. Any existing method.tex file\n3. Any ideas.md, report.md, or ROADMAP.md that might describe the method in more detail\n\nSearch broadly - check docs/, artifacts/, knowledge/, and any other directories. Report what you find, including the actual citation keys if they exist in any bib or yaml file."
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T16:29:59.473582+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T16:29:59.473716+00:00_

artifacts/freige/configs/accelerate_4gpu.yaml
artifacts/dream_reports/dream_20260515T120227/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T120227/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T120227/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T120227/best/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/median/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/meta.yaml
artifacts/dream_reports/dream_20260515T132059/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T132059/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T132059/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T132059/best/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/median/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/meta.yaml
literature_map.yaml
constraints.yaml
artifacts/dream_reports/dream_20260516T105318/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T105318/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T105318/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T105318/best/review_context.yaml
artifacts/dream_reports/dream_20260516T105318/median/review_context.yaml
artifacts/dream_reports/dream_20260516T105318/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T105318/meta.yaml
artifacts/dream_reports/dream_20260516T155803/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T155803/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T155803/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T155803/best/review_context.yaml
artifacts/dream_reports/dream_20260516T155803/median/review_context.yaml
artifacts/dream_repor
…[truncated 254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T16:29:59.473865+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T16:29:59.474000+00:00_

task_context/history/director/loop_1.md
task_context/history/reviewer/loop_1.md
task_context/history/agent/loop_1.md
artifacts/_project/report/trl_grpo_stability_research.md
artifacts/trl_grpo_stability_research.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_1_1778770242.md
artifacts/kl_analysis_report.md
task_context/history/agent/loop_2.md
task_context/history/agent/loop_2_1778771560.md
artifacts/training_health_check.md
artifacts/eval_script_audit.md
task_context/history/reviewer/loop_2.md
task_context/history/agent/loop_2_1778772389.md
artifacts/diag_mvp2_grpo_flatnli_r3.md
task_context/history/agent/loop_2_1778773789.md
task_context/history/agent/loop_2_1778778064.md
task_context/history/agent/loop_2_1778781516.md
task_context/history/agent/loop_3.md
task_context/history/agent/loop_3_1778782483.md
task_context/history/agent/loop_3_1778782514.md
task_context/history/agent/loop_3_1778783774.md
task_context/history/agent/loop_3_1778783775.md
task_context/history/agent/loop_3_1778784175.md
task_context/history/agent/loop_3_1778785006.md
artifacts/_project/report/d024_literature_survey.md
artifacts/d024_literature_survey.md
artifacts/ced_stabilizer_literature_survey.md
task_context/history/agent/loop_3_1778785949.md
artifacts/eval_status_check.md
task_context/history/agent/loop_3_1778787924.md
task_context/history/reviewer/loop_3.md
task_context/history/agent/loop_3_1778793698.md
task_context/history/agent/loop_4.md
task_context/history/agent/loop_4_1778794020.md
task_context/history/agent/loop_4_1778794030.md
task_context/history/agent/loop_4_1778794301.md
task_context/history/agent/loop_4_1778794857.md
task_context/history/agent/loop_4_1778795427.md
task_context/history/agent/loop_4_1778795976.md
task_context/history/agent/loop_4_1778796493.md
task_context/history/agent/loop_4_1778797169.md
task_context/history/agent/loop_4_1778798567.md
task_context/history/agent/loop_4_1778799368.md
task_context/history/agent/loop_4_1778799743.md
task
…[truncated 2491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T16:29:59.474142+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T16:29:59.474289+00:00_

artifacts/dream_reports/dream_20260515T120227/best/paper.tex
artifacts/dream_reports/dream_20260515T120227/median/paper.tex
artifacts/dream_reports/dream_20260515T120227/worst/paper.tex
artifacts/dream_reports/dream_20260515T132059/best/paper.tex
artifacts/dream_reports/dream_20260515T132059/median/paper.tex
artifacts/dream_reports/dream_20260515T132059/worst/paper.tex
artifacts/dream_reports/dream_20260516T105318/best/paper.tex
artifacts/dream_reports/dream_20260516T105318/median/paper.tex
artifacts/dream_reports/dream_20260516T105318/worst/paper.tex
artifacts/dream_reports/dream_20260516T155803/best/paper.tex
artifacts/dream_reports/dream_20260516T155803/median/paper.tex
artifacts/dream_reports/dream_20260516T155803/worst/paper.tex
docs/paper/acl-style/acl_lualatex.tex
docs/paper/acl-style/acl_latex.tex
docs/paper/main.tex
artifacts/_project/paper/experiments.tex
docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T16:29:59.474426+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T16:29:59.474545+00:00_

docs/paper/acl-style/custom.bib
docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T16:29:59.474665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T16:29:59.474785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T16:29:59.474897+00:00_

File content (48306 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T16:29:59.475011+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{xcolor}
16	\usepackage{multirow}
17	\usepackage{subcaption}
18	
19	\graphicspath{{../../figures/paper/}}
20	
21	\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/analysis}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	\bibliographystyle{acl_natbib}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T16:29:59.475150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T16:29:59.475281+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-17T16:29:59.475404+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-17T16:29:59.475512+00:00_

docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-17T16:29:59.475627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "limit": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "limit": "10000"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T16:29:59.475752+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper -name \"*.bib\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper -name \"*.bib\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T16:29:59.475868+00:00_

File content (48306 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T16:29:59.475989+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T16:29:59.476101+00:00_

total 80
drwxr-xr-x 4 ubuntu ubuntu  4096 May 17 16:23 .
drwxr-xr-x 4 ubuntu ubuntu  4096 May 15 05:28 ..
drwxr-xr-x 3 ubuntu ubuntu  4096 May 17 13:51 acl-style
-rw-r--r-- 1 ubuntu ubuntu 11615 May 17 16:04 acl.sty
-rw-r--r-- 1 ubuntu ubuntu 45186 May 17 16:04 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu   870 May 17 16:04 main.tex
-rw-r--r-- 1 ubuntu ubuntu     0 May 17 16:04 references.bib
drwxr-xr-x 2 ubuntu ubuntu  4096 May 17 16:22 sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-17T16:29:59.476210+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/custom.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T16:29:59.476352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T16:29:59.476463+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-17T16:29:59.476578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/custom.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/custom.bib"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-17T16:29:59.476725+00:00_

1	% Use this file for citations not found in the ACL Anthology (contained in "anthology.bib").
2	
3	@book{Aho:72,
4	    author  = {Alfred V. Aho and Jeffrey D. Ullman},
5	    title   = {The Theory of Parsing, Translation and Compiling},
6	    year    = "1972",
7	    volume  = "1",
8	    publisher = {Prentice-Hall},
9	    address = {Englewood Cliffs, NJ}
10	}
11	
12	@book{APA:83,
13	    author  = {{American Psychological Association}},
14	    title   = {Publications Manual},
15	    year    = "1983",
16	    publisher = {American Psychological Association},
17	    address = {Washington, DC}
18	}
19	
20	@article{Chandra:81,
21		author = {Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer},
22		year = "1981",
23		title = {Alternation},
24		journal = {Journal of the Association for Computing Machinery},
25		volume = "28",
26		number = "1",
27		pages = "114--133",
28		doi = "10.1145/322234.322243",
29	}
30	
31	@inproceedings{andrew2007scalable,
32	  title={Scalable training of {L1}-regularized log-linear models},
33	  author={Andrew, Galen and Gao, Jianfeng},
34	  booktitle={Proceedings of the 24th International Conference on Machine Learning},
35	  pages={33--40},
36	  year={2007},
37	}
38	
39	@book{Gusfield:97,
40	    author  = {Dan Gusfield},
41	    title   = {Algorithms on Strings, Trees and Sequences},
42	    year    = "1997",
43	    publisher = {Cambridge University Press},
44	    address = {Cambridge, UK}
45	}
46	
47	@article{rasooli-tetrault-2015,
48	    author    = {Mohammad Sadegh Rasooli and Joel R. Tetreault},
49	    title     = {Yara Parser: {A} Fast and Accurate Dependency Parser},
50	    journal   = {Computing Research Repository},
51	    volume    = {arXiv:1503.06733},
52	    year      = {2015},
53	    url       = {http://arxiv.org/abs/1503.06733},
54	    note    = {version 2}
55	}
56	
57	@article{Ando2005,
58		Acmid = {1194905},
59		Author = {Ando, Rie Kubota and Zhang, Tong},
60		Issn = {1532-4435},
61		Issue_Date = {12/1/2005},
62		Journal = {J
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-17T16:29:59.476922+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-17T16:29:59.477076+00:00_

# Literature Map for faith-evidence-ie (FREIGE)
# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE
# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan; +15 papers from 2026-05-16 incremental scan; +9 papers from Related Work targeted expansion; +6 papers from evidence cost literature scan; +11 papers from related work foundational survey)

papers:

  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===

  - title: "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
    authors: NVIDIA Labs
    year: 2025
    venue: ICML 2026
    url: https://arxiv.org/abs/2601.05242
    category: reward_diversity
    role: closest_prior_work
    key_finding: >
      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，
      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，
      保留多 reward 的相对差异，显著提升训练稳定性。
    relevance_to_ced_stabilizer: >
      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），
      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。
      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。

  - title: "DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs"
    authors: Xiwen Chen et al.
    year: 2025
    venue: arXiv 2505.09655
    url: https://arxiv.org/abs/2505.09655
    category: reward_diversity
    role: related_method
    key_finding: >
      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。
      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，
      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。
    relevance_to_ced_stabilizer: >
      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。
      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。

  - title: "Shrinking the Variance:
…[truncated 6751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-17T16:29:59.477257+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"deepseekmatch\\|GRPO\\|DPO\\|Rafailov\\|STaR\\|Zelikman\\|SAIS\\|DREEAM\\|LoRA\\|DocRED\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"deepseekmatch\\|GRPO\\|DPO\\|Rafailov\\|STaR\\|Zelikman\\|SAIS\\|DREEAM\\|LoRA\\|DocRED\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -50"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-17T16:29:59.477404+00:00_

  - title: "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，
      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，
      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。
      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。
  - title: "DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs"
      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。
  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===
      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。
  - title: "Dr. GRPO: Removing Optimization Bias in GRPO"
      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组
      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。
      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，
      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。
      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。
  - title: "DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO"
      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）
      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——
  - title: "Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients"
      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，
      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；
      有效稳定训练并促进更多样的 policy exploration。
      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。
      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。
      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，
      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，
      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；
      避免了显式 GRPO 在 structured output 上的不稳定性。
      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。
      未报告 catastrophic for
…[truncated 946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-17T16:29:59.477560+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"^\\s+key:|bibtex|citation\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"^\\s+key:|bibtex|citation\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -30"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-17T16:29:59.477677+00:00_

      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-17T16:29:59.477810+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ | grep -E \"\\.md|\\.yaml|README\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ | grep -E \"\\.md|\\.yaml|README\""
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-17T16:29:59.477930+00:00_

-rw-r--r--  1 ubuntu ubuntu  16396 May 17 16:21 AGENTS.md
-rw-------  1 ubuntu ubuntu   4092 May 17 15:29 ROADMAP.md
-rw-------  1 ubuntu ubuntu   1891 May 16 11:15 constraints.yaml
-rw-------  1 ubuntu ubuntu  95895 May 17 15:29 decisions.yaml
-rw-------  1 ubuntu ubuntu   3135 May 16 16:31 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu   3140 May 16 16:31 dream_registry.yaml.bak
-rw-------  1 ubuntu ubuntu   7644 May 17 01:06 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu    960 May 15 19:11 ideas.md
-rw-r--r--  1 ubuntu ubuntu 137218 May 16 06:11 literature_map.yaml
-rw-r--r--  1 ubuntu ubuntu   8315 May 17 15:46 memory.md
-rw-------  1 ubuntu ubuntu   1869 May 17 15:08 mistakes.yaml
-rw-r--r--  1 ubuntu ubuntu  22573 May 17 15:06 paper_framing.md
-rw-------  1 ubuntu ubuntu   1404 May 17 16:23 paper_provenance.yaml
-rw-------  1 ubuntu ubuntu 359132 May 17 16:03 registry.yaml
-rw-r--r--  1 ubuntu ubuntu   6033 May 17 16:00 report.md
-rw-r--r--  1 ubuntu ubuntu  22562 May 17 15:28 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-17T16:29:59.478063+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-17T16:29:59.478176+00:00_

total 24
drwxr-xr-x 2 ubuntu ubuntu  4096 May 17 16:22 .
drwxr-xr-x 4 ubuntu ubuntu  4096 May 17 16:23 ..
-rw-r--r-- 1 ubuntu ubuntu 14994 May 17 16:22 experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-17T16:29:59.478319+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie -name \"method.tex\" -o -name \"methods.tex\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie -name \"method.tex\" -o -name \"methods.tex\""
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-17T16:29:59.478432+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-17T16:29:59.478550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-17T16:29:59.478725+00:00_

1	# Paper Framing — FREIGE
2	
3	> **状态**: POST-MVP + D078-D094 complete; Scaling Study 4/4 done (D094); P0 gaps filled; Paper writing in progress (Step 2→3)
4	> **最后更新**: 2026-05-17
5	> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成
6	> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3
7	
8	## Target Venue
9	
10	- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)
11	- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)
12	
13	## Core Insight
14	
15	LLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。
16	
17	我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。
18	
19	**Evidence tax 是 scale-dependent 的（non-monotonic pattern, D079/D082/D083）**：1.7B 模型中 evidence generation 反而带来 +6.2pp 收益（隐式正则化），4B 模型付出 -7.5pp 代价，8B Qwen 模型容量足够 absorb（≈0），8B LLaMA 跨家族确认（-0.7pp）。这推翻了"evidence 总有代价"的简单叙事。
20	
21	CED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 和 flat-NLI 作为 RSFT scoring functions 统计不可区分（D078 paired t-test p=0.44），但均显著优于 random/no scoring。CED 因可解释性优势作为默认推荐方案。
22	
23	## Story Arc
24	
25	1. **Problem**: LLM DocRE 无证据 → 部署障碍
26	2. **New task**: evidence-grounded DocRE — 同时生成关系和证据
27	3. **Cost of faithfulness**: evidence generation 代价是 **scale-dependent** 的——4B 模型付出 -7.5pp 代价，但 1.7B 反而获益 +6.2pp，8B 趋近于零。这不是固定成本，而是与模型容量的非线性交互（D079/D082/D083）
28	4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)
29	5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity
…[truncated 16406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-17T16:29:59.478893+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"key:|citation key|bibtex_key|citekey\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"key:|citation key|bibtex_key|citekey\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -40"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-17T16:29:59.479013+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-17T16:29:59.479138+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"STaR\\|Zelikman\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"STaR\\|Zelikman\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-17T16:29:59.479277+00:00_

      两阶段训练：SFT cold-start + GRPO RL。
  - title: "AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners"
      AdaSTaR 引入两个自适应采样原则：(1) diversity sampling 促进均衡，
      AdaSTaR 的 curriculum 策略可优化采样——先训简单 relation pair，再逐步引入困难的多跳关系。
  - title: "STaR: Bootstrapping Reasoning With Reasoning"
    authors: Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman
      STaR 的 iterative bootstrapping 是 FREIGE RSFT 的理论先驱——
      RSFT 本质上是 STaR 的一个 iteration（生成、筛选正确输出、fine-tune）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-17T16:29:59.479416+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "tail -500 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "tail -500 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -200"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-17T16:29:59.479564+00:00_

  - title: "RL-Struct: A Lightweight Reinforcement Learning Framework for Reliable Structured Output in LLMs"
    authors: Unknown
    year: 2025
    venue: arXiv 2512.00319
    url: https://arxiv.org/abs/2512.00319
    category: rl_for_ie
    role: method_component
    key_finding: >
      轻量级 RL 框架用于提升 LLM structured output 的可靠性。
      用 rule-based reward functions 提升结构合规性、数据有效性和整体准确性。
    relevance_to_freige: >
      与 FREIGE 共享 "RL for structured IE output" 的范式。RL-Struct 关注 structural reliability，
      FREIGE 进一步关注 evidence grounding。可作为 FREIGE 方法论的基础参考。

  # === Category 31: Reward Hacking Diagnostics (NEW - 2026-05-16 scan) ===

  - title: "The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking"
    authors: Yuchun Miao et al.
    year: 2025
    venue: ICML 2025
    url: https://arxiv.org/abs/2501.19358
    category: reward_hacking_diagnostics
    role: related_method
    key_finding: >
      发现 Energy Loss Phenomenon：LLM 最后一层的 energy loss（L1 norm 差值）在 RL 训练中
      持续增加，过度增加标志 reward hacking。理论证明 energy loss 增加降低 contextual relevance 上界。
      提出 EPPO（Energy loss-aware PPO）在 reward 计算中惩罚 energy loss 增加。
      EPPO 可解释为 entropy-regularized RL。
    relevance_to_freige: >
      与 FREIGE Claim 4（EDCR 双层诊断工具）直接相关：energy loss 是另一种 representation-level
      diagnostic for reward hacking。EDCR 从 evidence-relation consistency 角度诊断，
      EPPO 从 hidden state energy 角度诊断——互补的诊断信号。
      FREIGE 可引用 EPPO 作为 "diagnostic signals for RL training health" 的同类工作。

  - title: "Reward Hacking Mitigation using Verifiable Composite Rewards"
    authors: Unknown
    year: 2025
    venue: arXiv 2509.15557
    url: https://arxiv.org/abs/2509.15557
    category: reward_hacking_diagnostics
    role: related_method
    key_finding: >
      识别两种 reward hacking 行为：(1) 无推理直接给答案；(2) 非标准推理格式绕过 reward 机制。
      composite reward function 结合 correctness incentives + 结构性 penalties 缓解 hacking。
      二值 reward（非连续）更稳定——连续 reward 的 smooth gradients 被 exploit。
      augmen
…[truncated 7858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-17T16:29:59.479722+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -300 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "head -300 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/writing_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-17T16:29:59.479885+00:00_

meta:
  venue: emnlp-2026
  submission_type: long
  review_system: arr_july
  deadline: "2026-07-15"
  template:
    source: "github.com/acl-org/acl-style-files (official)"
    local_path: "projects/faith-evidence-ie/docs/paper/acl-style/"
    documentclass: "\\documentclass[11pt]{article}"
    options: "\\usepackage[review]{acl}"
    template_note: "Official ACL style files cloned 2026-05-17. EMNLP uses identical template."
  page_limits:
    main_text: 8
    references: unlimited
    appendix: unlimited
  title_candidates:
    - "Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction"
    - "The Cost of Faithfulness: Evidence-Extraction Trade-offs in Generative Document Relation Extraction"
    - "FREIGE: Faithful Evidence-Grounded Document-Level Relation Extraction via Rejection Sampling Fine-Tuning"
  preferred_title: 1
  visualization:
    preferred_tool: matplotlib

# ============================================================
# PAPER OUTLINE
# ============================================================
paper_outline:
  abstract:
    word_budget: 220
    key_message: >
      Evidence-grounded DocRE 新任务；系统比较 GRPO/DPO/RSFT 三范式；
      发现 decoupling spectrum（RL pressure 与 decoupling severity 正相关）；
      evidence tax 是 scale-dependent 的（1.7B +6.2pp benefit, 4B -7.0pp cost, 8B ≈0）；
      RSFT+NLI scoring 是唯一有效路线；EDCR 双层诊断
    must_include:
      - task definition (evidence-grounded DocRE, generative LLM qualifier)
      - three paradigms compared
      - decoupling spectrum core finding
      - scale-dependent evidence tax with concrete numbers
      - RSFT effectiveness delta vs SFT
      - EDCR diagnostic mention
    dependencies: [introduction, experiments, method]

  introduction:
    word_budget: 1200
    structure: five_paragraph
    paragraphs:
      - topic: "LLM DocRE progress but no evidence"
        word_budget: 200
      - topic: "Why verifiable evidence matters for deployment"
        word_budget: 150
      - topic: "E
…[truncated 10582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-17T16:29:59.480040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-17T16:29:59.480191+00:00_

1	# RSFT Scoring Commands
2	
3	## 验证结果
4	
5	- **脚本路径**: `/root/autodl-tmp/freige/training/rsft_score_filter.py`
6	- **模块导入**: `from freige.training.rsft_score_filter import main` ✅ OK
7	- **NLI 模型**: `/root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7`
8	
9	## Argparse 参数列表
10	
11	| 参数 | 必填 | 默认值 | 说明 |
12	|------|------|--------|------|
13	| `--input_dir` | ✅ | - | rsft_generate 输出目录（含 generations.jsonl） |
14	| `--output_path` | ✅ | - | 筛选结果输出目录 |
15	| `--nli_model_path` | ❌ | (内置默认) | NLI 模型路径 |
16	| `--nli_device` | ❌ | auto | NLI 模型运行设备 |
17	| `--tau` | ❌ | 0.5 | CED tau 阈值 |
18	| `--scoring_mode` | ❌ | ced | {ced, flat_nli} |
19	| `--format_weight` | ❌ | 0.2 | combined_score 中 format_reward 权重 |
20	| `--f1_weight` | ❌ | 0.4 | combined_score 中 f1_reward 权重 |
21	| `--ced_weight` | ❌ | 0.4 | combined_score 中 ced_reward 权重 |
22	| `--format_threshold` | ❌ | 0.5 | format_reward 最低阈值 |
23	| `--f1_threshold` | ❌ | 0.1 | f1_reward 最低阈值 |
24	| `--ced_threshold` | ❌ | 0.0 | ced_reward 最低阈值 |
25	| `--selection_strategy` | ❌ | top_pct | {threshold, top_k, top_pct} |
26	| `--top_k` | ❌ | 2 | top_k 策略: 每个文档取 top-K |
27	| `--top_pct` | ❌ | 25 | top_pct 策略: 每个文档取 top N% |
28	
29	## Candidate Generation 进度 (更新: 2026-05-17 ~00:00)
30	
31	| 模型 | lines | docs | 进度 | GPU | 输出路径 | 预计完成 |
32	|------|-------|------|------|-----|----------|----------|
33	| Qwen3-1.7B | 8616 | ~1077 | 35.6% | 0 | `freige/outputs/rsft_candidates_1_7b` | ~May 17 08:00 |
34	| Qwen3-8B | 6952 | ~869 | 28.7% | 3 | `freige/outputs/rsft_candidates_8b` | ~May 17 11:00 |
35	| LLaMA-3.1-8B | ~4456 | ~557 | 18.4% | 1→2(r3) | `/root/autodl-tmp/rsft_candidates_llama_3_1_8b` | ~May 17 15:00 |
36	
37	总目标: 3027 docs × 8 candidates each = 24216 lines
38	
39	## CED Scoring 命令模板
40	
41	基于 4B 历史参数（rsft_filtered_topk3: top_k=3, tau=0.5, weights 0.2/0.4/0.4）
42	
43	### 1.7B CED Scoring
44	
45	```bash
46	source /root/miniconda3/etc/profile.d/conda.sh && cond
…[truncated 5716 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-17T16:29:59.480370+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 3 \"title.*STaR\\|title.*DPO\\|title.*DeepSeekMath\\|title.*LoRA\\|title.*DocRED\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 3 \"title.*STaR\\|title.*DPO\\|title.*DeepSeekMath\\|title.*LoRA\\|title.*DocRED\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -80"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-17T16:29:59.480518+00:00_

  - title: "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
    authors: NVIDIA Labs
    year: 2025
    venue: ICML 2026
--
  - title: "LoRA vs Full Fine-tuning: An Illusion of Equivalence"
    authors: Reece Shuttleworth, Jacob Andreas, Antonio Torralba, Pratyusha Sharma
    year: 2024
    venue: arXiv 2410.21228
--
  - title: "The Impact of LoRA on the Emergence of Clusters in Transformers"
    authors: Hugo Koubbi, Louis Hernandez, Matthieu Boussard
    year: 2024
    venue: arXiv 2402.15415
--
  - title: "RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models"
    authors: Anonymous
    year: 2024
    venue: NAACL 2024 Findings
--
  - title: "How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness"
    authors: Darshita Rathore et al.
    year: 2025
    venue: IJCNLP-AACL 2025
--
  - title: "RandLoRA: Full-rank Parameter-Efficient Fine-tuning of Large Models"
    authors: Paul Albert et al.
    year: 2025
    venue: ICLR 2025
--
  - title: "C-LoRAE: Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for Unified Multimodal Information Extraction"
    authors: Unknown
    year: 2025
    venue: arXiv 2505.06303
--
  - title: "Ortho-LoRA: Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection"
    authors: Ziyu Yang et al.
    year: 2026
    venue: arXiv 2601.09684
--
  - title: "AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners"
    authors: Hyung Won Chung et al.
    year: 2025
    venue: NeurIPS 2025
--
  - title: "CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization"
    authors: Unknown
    year: 2025
    venue: arXiv 2501.18475
--
  - title: "FlyLoRA: Boosting Task Decoupling and Parameter Efficiency via Implicit Rank-Wise Mixture-of-Experts"
    authors: Heming Zou, Yunliang Zang, Wutong Xu, Yao Zhu, Xiangyang Ji
 
…[truncated 813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-17T16:29:59.480764+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"url:|arXiv|arxiv\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | grep -E \"STaR|DPO|DeepSeekMath|Rafailov|Zelikman|SAIS|DREEAM|LoRA|DocRED\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"url:|arXiv|arxiv\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | grep -E \"STaR|DPO|DeepSeekMath|Rafailov|Zelikman|SAIS|DREEAM|LoRA|DocRED\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-17T16:29:59.480926+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-17T16:29:59.481059+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B 5 -A 2 \"Zelikman\\|Rafailov\\|Shao.*GRPO\\|Hu.*LoRA\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B 5 -A 2 \"Zelikman\\|Rafailov\\|Shao.*GRPO\\|Hu.*LoRA\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -100"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-17T16:29:59.481180+00:00_

      但 FREIGE 的 re-DocRED evaluation 已有较完善的标签，影响可能较小。

  # === Category 41: Self-Training / Bootstrapping for LLM Reasoning ===

  - title: "STaR: Bootstrapping Reasoning With Reasoning"
    authors: Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman
    year: 2022
    venue: NeurIPS 2022

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-17T16:29:59.481358+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-17T16:29:59.481573+00:00_

1	# faith-evidence-ie — Research Dashboard
2	
3	> 最后更新: 2026-05-17 15:04 UTC | 更新原因: D094 Scaling Study 4/4 完成，8B RSFT +3.4pp
4	
5	## 核心方向
6	FREIGE: LLM-based evidence-grounded DocRE 系统性研究。核心发现：(1) Evidence tax 非单调；(2) QLoRA GRPO catastrophic decoupling（跨家族验证）；(3) CED-RSFT 跨规模+跨架构一致正向（+1.6 to +5.5pp）；(4) EDCR 双层诊断（ρ=-0.96）；(5) Joint generation 优于 post-hoc retrieval。详见 paper_framing.md。
7	
8	## 当前进展
9	- **阶段**: Research 近完成 + Paper Writing (Step 2→3) + 审稿同步
10	- **Scaling Study (D094)**: ✅ 4/4 完成。Qwen3-1.7B +2.7pp, 4B +5.5pp, 8B +3.4pp, LLaMA-8B +1.6pp
11	- **Post-hoc baseline (D091)**: ✅ BM25 k=2 evi_f1_joint=0.347 < RSFT 0.361
12	- **Lead 1 CED filter (D090)**: ✅ Negative
13	- **DREEAM Evi-F1 (D093)**: ✅ 协议对齐确认
14	- **Seed replication**: 1.7B seed43 eval running (20%), LLaMA seed43 training (62%)
15	- **Paper Agent**: Step 2 figures patching → Step 3 draft writing
16	
17	## 投稿目标
18	- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, ~59 days)
19	
20	## 运行中实验
21	| GPU | 任务 | 预计完成 |
22	|-----|------|---------|
23	| cuda:0 | plan_006_llama_rsft_seed43 训练 (62%) | ~1h |
24	| cuda:1 | lead2_ckpt20_eval | 进行中 |
25	| cuda:2 | plan_006_qwen3_1_7b_rsft_seed43_eval (20%) | ~1.5h |
26	| cuda:3 | **空闲** — 8B eval 已完成 (D094) | — |
27	
28	## 近期任务
29	- [x] Scaling Study 4/4 闭合 (D094)
30	- [x] Post-hoc BM25 baseline (D091)
31	- [x] Lead 1 CED filter (D090, negative)
32	- [x] DREEAM protocol alignment (D093)
33	- [ ] Lead 2 ckpt-20 eval → RSFT→GRPO 可行性
34	- [ ] 1.7B + LLaMA seed 43 eval → seed 方差验证
35	- [ ] CodaLab test 手动提交
36	- [ ] Paper Agent Step 3: Draft writing (experiments → method → intro → ...)
37	- [ ] 8B RSFT evi_f1_joint 计算（for evidence strategy table）
38	
39	## GPU 预算
40	- 硬件: 4× RTX 5090 32GB (rtx5090-4x)
41	- 当前 3/4 运行中，cuda:3 空闲
42	- 剩余任务: lead2 eval ~1h + seed43 训练/eval ~3h ≈ 5h
43	- Paper writing 不需要 GPU
44	
45	## 风险监控
46	- **Lead 2 结果**: 如果 RSFT→GRPO ckpt-20 表现好，可能改变 decoupling narrative
47	- **Seed variance**: 如果 seed 43 结果偏离 seed 42 > 2pp，需增加 seed 数量
48
…[truncated 1602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-17T16:29:59.481745+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B 3 -A 5 \"DPO\\|Direct Preference\\|Rafailov\" /home/ubuntu/.agent-ml-research-ie/literature_map.yaml | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B 3 -A 5 \"DPO\\|Direct Preference\\|Rafailov\" /home/ubuntu/.agent-ml-research-ie/literature_map.yaml | head -50"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-17T16:29:59.481866+00:00_

grep: /home/ubuntu/.agent-ml-research-ie/literature_map.yaml: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-17T16:29:59.481992+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B 3 -A 5 \"DPO\\|Direct Preference\\|Rafailov\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B 3 -A 5 \"DPO\\|Direct Preference\\|Rafailov\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -80"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-17T16:29:59.482126+00:00_

  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===

  - title: "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
    authors: NVIDIA Labs
    year: 2025
    venue: ICML 2026
    url: https://arxiv.org/abs/2601.05242
    category: reward_diversity
    role: closest_prior_work
    key_finding: >
      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，
      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，
      保留多 reward 的相对差异，显著提升训练稳定性。
    relevance_to_ced_stabilizer: >
      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），
      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。
      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。

  - title: "DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs"
    authors: Xiwen Chen et al.
    year: 2025
    venue: arXiv 2505.09655
--
    role: related_method
    key_finding: >
      GRPO 聚合 mixed-reward 时直接求和再归一化会淹没弱信号 reward 维度。
      RDPO 用 Magnitude-Aware Quantile normalization + Mahalanobis whitening
      去相关 reward 子空间，改善 LLM post-training 的多目标平衡。
    relevance_to_freige: >
      CED reward 的 evidence quality 维度与 extraction F1 天然低相关（r<0.3），
      RDPO 的理论预测这种低相关多维 reward 更易优化。
      为 CED 的 training-stabilizing 效果提供另一个理论解释角度。

  # === Category 15: GRPO Theory (NEW - 2026-05-15 scan) ===

  - title: "GRPO is Secretly a Process Reward Model"
--
    category: llm_ie_alignment
    role: key_baseline
    key_finding: >
      构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE。
      支持 closed/open/on-demand IE 三种模式。
      基于 LLaMA-2-7B/LLaMA-3.2-3B/Qwen2.5-1.5B，在多个 held-out IE dataset 上达 SOTA。
    relevance_to_freige: >
      ADELIE 是 IE alignment 的代表性工作，用 SFT+DPO 替代 RSFT+GRPO。
      我们的工作与 ADELIE 在 training paradigm 上有可比性——
      ADELIE 用 DPO（offline preference optimization），我们用 RSFT（offline rejection sampling）。
  
…[truncated 1279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-17T16:29:59.482303+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"deepseek\\|GRPO\\|shao\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"deepseek\\|GRPO\\|shao\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -20"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-17T16:29:59.482439+00:00_

      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，
  - title: "DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs"
      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。
  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===
      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。
      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。
  - title: "Dr. GRPO: Removing Optimization Bias in GRPO"
      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组
      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。
      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，
      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。
  - title: "DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO"
      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）
      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——
  - title: "Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients"
      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，
      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；
      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。
      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。
      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-17T16:29:59.482592+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"2403\\.07708|2305\\.18290|2402\\.03300|2210\\.10760\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml -B 5 -A 3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"2403\\.07708|2305\\.18290|2402\\.03300|2210\\.10760\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml -B 5 -A 3"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-17T16:29:59.482712+00:00_

  # === Category 3: Contrastive Rewards in RL ===

  - title: "Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards"
    authors: Shen, Zhang et al.
    year: 2024
    venue: arXiv 2403.07708
    url: https://arxiv.org/abs/2403.07708
    category: contrastive_reward
    role: closest_contrastive_precedent
    key_finding: >

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-17T16:29:59.482840+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"SAIS\\|DREEAM\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml -B 3 -A 5 | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"SAIS\\|DREEAM\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml -B 3 -A 5 | head -100"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-17T16:29:59.482971+00:00_

  # === Category 21: Evidence-Based / Faithful DocRE (Direction 1) ===

  - title: "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction"
    authors: Youmi Ma, An Wang, Naoaki Okazaki
    year: 2023
    venue: EACL 2023
    url: https://arxiv.org/abs/2302.08675
    category: evidence_based_docre
--
      silver evidence 训练 ER。DocRED 上 RE 和 ER 均达 SOTA。
      解决了 evidence retrieval 的两大问题：高内存消耗和标注有限。
    relevance_to_freige: >
      最重要的 evidence-based DocRE 先驱工作。DREEAM 用 evidence 引导 attention（encoder-based），
      我们用 evidence 引导 RL reward（generative LLM）。关键代际差异：
      (1) DREEAM 是 encoder-based（BERT/RoBERTa），我们是 LLM generative；
      (2) DREEAM 的 evidence 用于注意力监督，我们的 evidence 用于 reward 设计和 CED reranking；
      (3) DREEAM 未量化 evidence 对 RE 的 performance cost。
      Related Work 必引：evidence-based DocRE 的代表性工作。

  - title: "DocGNRE: Semi-automatic Data Enhancement for Document-Level Relation Extraction with Distant Supervision from Large Language Models"
    authors: Junpeng Li, Zixia Jia, Zilong Zheng
    year: 2023
--
      直接引导 PLM encoder 最后一层的 top-k token attention 到 evidence sentences，
      不引入额外可训练参数。Axial attention 建模 relation triple 之间的全局相互依赖。
    relevance_to_freige: >
      与 DREEAM 属于同一 evidence-guided attention 范式。
      EAAGRE 的无参数 evidence attention 与我们 CED reranker 的 post-hoc 方式形成对比——
      前者在 encoder 内部注入 evidence signal，后者在 generation 后验证。
      证明 evidence 信号无论注入位置都能提升 DocRE 性能。

  - title: "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction"
--
      成为 DocRE 标准 baseline，后续几乎所有 encoder-based 方法都以此为起点。
    relevance_to_freige: >
      DocRE 领域最重要的 baseline 之一。FREIGE 的 LLM-based 方法需要与
      ATLOP 及其后续改进（DREEAM, SAIS 等）进行性能对比和定位。

  - title: "Document-level Relation Extraction as Semantic Segmentation"
    authors: Ningyu Zhang, Xiang Chen, Xin Xie, Shumin Deng, Chuanqi Tan, Mosha Chen, Fei Huang, Luo Si, Huajun Chen
    year: 2021
    venue: I
…[truncated 976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-17T16:29:59.483127+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"^\\s+url:|title.*DPO\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"^\\s+url:|title.*DPO\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -100"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-17T16:29:59.483279+00:00_

  - title: "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
    url: https://arxiv.org/abs/2601.05242
    url: https://arxiv.org/abs/2505.09655
    url: https://arxiv.org/abs/2511.03710
    url: https://arxiv.org/abs/2502.18770
    url: https://arxiv.org/abs/2503.14476
    url: https://arxiv.org/abs/2503.20783
    url: https://arxiv.org/abs/2504.19599
    url: https://arxiv.org/abs/2501.03262
    url: https://arxiv.org/abs/2512.21514
    url: https://arxiv.org/abs/2601.23135
    url: https://arxiv.org/abs/2403.07708
    url: https://aclanthology.org/2024.emnlp-main.852/
    url: https://openreview.net/forum?id=iX1RjVQODj
    url: https://aclanthology.org/2025.acl-long.340.pdf
    url: https://aclanthology.org/2024.eacl-long.102/
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/
    url: https://openreview.net/forum?id=gkfUvn0fLU
    url: https://arxiv.org/abs/2505.23585
    url: https://arxiv.org/abs/2504.11343
    url: https://arxiv.org/abs/2602.04391
    url: https://openreview.net/forum?id=yQ2UivKlir
    url: https://arxiv.org/abs/2507.04642
    url: https://arxiv.org/abs/2603.09478
    url: https://2025.emnlp.org/program/find_papers/
    url: https://arxiv.org/abs/2406.11455
    url: https://arxiv.org/abs/2507.21892
    url: https://arxiv.org/abs/2511.08143
    url: https://arxiv.org/abs/2408.13889
    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11
    url: https://arxiv.org/abs/2508.00757
    url: https://arxiv.org/abs/2403.14888
    url: https://arxiv.org/abs/2410.21333
    url: https://arxiv.org/abs/2106.08657
    url: https://arxiv.org/abs/2404.03098
    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532
    url: https://arxiv.org/abs/2301.12618
    url: https://arxiv.org/abs/2412.18004
    url: https://arxiv.org/abs/2307.16877
    url: https://aclanthology.org/2024.cl-2.6/
    url: https://arxiv.org/abs/2401.14367
    url: https://arxiv.org/abs/2603.19532
    url: 
…[truncated 2705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-17T16:29:59.483432+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "awk '/DPO/{p=1} p{print; if(/url:/) p=0}' /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "awk '/DPO/{p=1} p{print; if(/url:/) p=0}' /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | head -50"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-17T16:29:59.483564+00:00_

  - title: "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
    authors: NVIDIA Labs
    year: 2025
    venue: ICML 2026
    url: https://arxiv.org/abs/2601.05242
      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，
      保留多 reward 的相对差异，显著提升训练稳定性。
    relevance_to_ced_stabilizer: >
      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），
      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。
      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。

  - title: "DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs"
    authors: Xiwen Chen et al.
    year: 2025
    venue: arXiv 2505.09655
    url: https://arxiv.org/abs/2505.09655
      RDPO 用 Magnitude-Aware Quantile normalization + Mahalanobis whitening
      去相关 reward 子空间，改善 LLM post-training 的多目标平衡。
    relevance_to_freige: >
      CED reward 的 evidence quality 维度与 extraction F1 天然低相关（r<0.3），
      RDPO 的理论预测这种低相关多维 reward 更易优化。
      为 CED 的 training-stabilizing 效果提供另一个理论解释角度。

  # === Category 15: GRPO Theory (NEW - 2026-05-15 scan) ===

  - title: "GRPO is Secretly a Process Reward Model"
    authors: Sullivan, Koller
    year: 2025
    venue: under review at ICML 2026
    url: https://arxiv.org/abs/2509.21154
      构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE。
      支持 closed/open/on-demand IE 三种模式。
      基于 LLaMA-2-7B/LLaMA-3.2-3B/Qwen2.5-1.5B，在多个 held-out IE dataset 上达 SOTA。
    relevance_to_freige: >
      ADELIE 是 IE alignment 的代表性工作，用 SFT+DPO 替代 RSFT+GRPO。
      我们的工作与 ADELIE 在 training paradigm 上有可比性——
      ADELIE 用 DPO（offline preference optimization），我们用 RSFT（offline rejection sampling）。
      关键差异：ADELIE 覆盖通用 IE，不涉及 evidence generation 或 DocRE-specific challenges；
      我们专注于 DocRE + evidence grounding 的 trade-off。

  # === Category 19: Unfaithful Reasoning / Post-Rationalization (NEW - 2026-05-15 scan) ===

  - title: "Chain-of-Though
…[truncated 350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-17T16:29:59.483772+00:00_

Perfect! Now I have comprehensive information. Let me compile the final report:

## Summary of Findings

I have successfully searched the FREIGE (faith-evidence-ie) project and found all the resources you requested. Here's what exists:

### 1. **Literature Map File** ✅
**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml`

This is a comprehensive literature map (48,306 tokens) containing 70+ papers organized by category. It includes detailed annotations for each paper with:
- Paper titles, authors, venues, years
- Key findings and relevance statements
- arXiv IDs and URLs

### 2. **Citation Keys Found** ✅

The project uses **direct arXiv citations** rather than BibTeX keys. Here are the key papers mentioned:

| Paper | Authors | Year | Citation/arXiv ID |
|-------|---------|------|------------------|
| **STaR: Bootstrapping Reasoning With Reasoning** | Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman | 2022 | NeurIPS 2022 |
| **DPO (Direct Preference Optimization)** | Rafailov et al. | 2023 | NeurIPS 2023, arXiv 2305.18290 |
| **DeepSeekMath (GRPO)** | Shao et al. | 2024 | arXiv 2402.03300 |
| **Scaling Laws for Reward Overoptimization** | Gao et al. | 2023 | ICML 2023, arXiv 2210.10760 |
| **LoRA: Low-Rank Adaptation** | Hu et al. | 2021 | (multiple variants in literature_map) |
| **DREEAM** | Youmi Ma, An Wang, Naoaki Okazaki | 2023 | EACL 2023, arXiv 2302.08675 |
| **SAIS** | Ruoting Xie, Jingqi Wang, Wei Cai, Runxin Xu, Baobao Chang | 2022 | NAACL 2022 |
| **DocRED** | Yuan Yao et al. | 2019 | ACL 2019 |
| **Contrastive Rewards in RLHF** | Shen, Zhang et al. | 2024 | arXiv 2403.07708 |
| **RS-DPO** | Anonymous | 2024 | NAACL 2024 Findings, arXiv 2402.10038 |

### 3. **Method Documentation** ✅

**No dedicated method.tex file exists yet.** However, there is comprehensive method documentation in:

- **`writing_plan.yaml`**: Contains detailed method section structure including:
  - Task definition (Evidence
…[truncated 2365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Agent",
  "elapsed_ms": 10
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-17T16:29:59.484031+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/",
  "description": "Check existing section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/",
    "description": "Check existing section files"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-17T16:29:59.484168+00:00_

experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-17T16:29:59.484347+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}\n\\label{sec:task}\n\nGiven a document $D = \\{s_1, \\ldots, s_n\\}$ consisting of $n$ sentences and a set of entities $\\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \\in \\mathcal{E} \\times \\mathcal{E}$, a relation $r \\in \\mathcal{R} \\cup \\{\\texttt{NA}\\}$ together with a set of supporting evidence sentences $E \\subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation additionally requires $E$, which grounds each prediction in specific textual support.\n\nIn our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \\texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\\citep{xie2022sais} and DREEAM~\\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.\n\n\n\\subsection{Supervised Fine-Tuning Baseline}\n\\label{sec:sft}\n\nWe fine-tune all models with LoRA~\\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\\alpha{=}128$, applied to attention projection matrices. The training data consists of DocRED~\\citep{yao2019docred} training documents converted to the structured output format described above, where each example maps a document and its entity set to the complete set of relation triples with evidence annotations. We additionally train a \\emph{no-evidence} variant under identical configuration but with evidence references removed from the output format, producing only \\texttt{(head, relation, tail)}. This variant serves as an upper bound on extraction performance by eliminating the generation cost of evidence, and allows direct measurement of the evidence tax at each model scale. Detailed hyperparameters (learning rate, batch size, number of epochs) are reported in the Appendix.\n\n\n\\subsection{Optimization Paradigms}\n\\label{sec:paradigms}\n\nWe evaluate three post-SFT optimization paradigms that differ in how they incorporate quality signals from the CED scoring function (\\S\\ref{sec:ced}).\n\n\\paragraph{GRPO.}\nGroup Relative Policy Optimization~\\citep{shao2024deepseekmath} is an online RL method that eliminates the need for a separate value network by computing advantages within groups of sampled outputs. For each training document, the policy generates $G$ candidate responses, which are scored by CED. The advantage of each response is computed relative to the group mean, and the policy is updated to increase the probability of above-average outputs. We test two configurations: QLoRA with $G{=}4$ groups under 4-bit quantization, and bf16 full-precision LoRA with $G{=}8$. Because GRPO applies gradient updates that directly optimize the reward signal, evidence quality and extraction accuracy compete for gradient capacity. We analyze this multi-objective tension in Section~\\ref{sec:spectrum}.\n\n\\paragraph{DPO.}\nDirect Preference Optimization~\\citep{rafailov2023direct} reformulates RLHF as a classification problem over preference pairs, without explicit reward models. We construct preference data from the SFT model's sampled outputs: for each document, the response with the highest CED score is labeled as preferred and the lowest-scoring response as rejected. DPO then adjusts the policy to increase the log-probability ratio between preferred and rejected completions. We train for 1 and 3 epochs to observe the temporal dynamics of evidence-extraction trade-offs under implicit optimization.\n\n\\paragraph{RSFT.}\nRejection Sampling Fine-Tuning is a single-round variant of iterative self-improvement methods such as STaR~\\citep{zelikman2022star}. The procedure is straightforward: the SFT model generates $N{=}8$ candidate outputs per training document, each candidate is scored by CED, and only the top-$k{=}1$ response is retained as training data. From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3\\% acceptance rate). Unlike GRPO and DPO, RSFT does not apply gradient-based optimization pressure toward a reward signal. Instead, it improves training data quality through filtering: the model trains on its own best outputs rather than all outputs. This distinction is critical because discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods find. The contribution of RSFT in our setting is not the framework itself, which is well-established, but its application to evidence-grounded DocRE with CED as a domain-specific quality filter.\n\n\n\\subsection{Contrastive Evidence Discrimination}\n\\label{sec:ced}\n\nCED is a scoring function that evaluates the faithfulness of predicted evidence sentences to their associated relation triples. It builds on Natural Language Inference (NLI) to measure whether evidence actually entails the predicted relation, rather than merely co-occurring with the relevant entities.\n\nFor a predicted triple $(e_h, r, e_t)$ with evidence sentences $E$, CED constructs a positive NLI pair: the premise is the concatenation of sentences in $E$, and the hypothesis is a natural-language verbalization of the relation (e.g., ``$e_h$ has relation $r$ with $e_t$''). An NLI model (\\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair. The contrastive component introduces hard negatives drawn from the same document. For each triple, we collect sentences that mention $e_h$ or $e_t$ but are not in the predicted evidence set. These entity-sharing distractors serve as negative premises, and the NLI model scores each to obtain $p^-_1, \\ldots, p^-_m$. The CED score for a single triple is:\n\\begin{equation}\n\\text{CED}(e_h, r, e_t, E) = p^+ - \\max_j \\, p^-_j\n\\label{eq:ced}\n\\end{equation}\nThis formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities. A high CED score indicates that the evidence provides relation-specific support beyond entity co-occurrence.\n\nThe document-level CED score aggregates over all predicted triples, weighted by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit. This coupling ensures that CED rewards both faithful evidence and accurate extraction jointly.\n\nWe also evaluate a \\emph{flat-NLI} baseline that uses only the positive entailment score $p^+$ without the contrastive term. In our experiments (Section~\\ref{sec:spectrum}), CED and flat-NLI produce statistically indistinguishable RSFT outcomes (paired $t$-test, $p{=}0.44$), but both outperform random selection and no-scoring baselines. We adopt CED as the default because the contrastive formulation provides interpretable per-triple discrimination scores that flat-NLI lacks.\n\n\n\\subsection{Evidence-Decoupling Ratio}\n\\label{sec:edcr}\n\nWe introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric that quantifies the degree of misalignment between a model's extraction and evidence capabilities. EDCR is not a training component; it serves purely as an analytical tool for comparing optimization methods.\n\nEDCR is defined as:\n\\begin{equation}\n\\text{EDCR} = \\frac{\\text{Evi-Recall}_{\\text{TP}}}{\\text{Rel-Recall}}\n\\label{eq:edcr}\n\\end{equation}\nwhere $\\text{Evi-Recall}_{\\text{TP}}$ is evidence sentence recall computed only over correctly predicted triples (true positives), and $\\text{Rel-Recall}$ is overall relation extraction recall. The numerator captures evidence quality on the subset of triples the model gets right; the denominator captures how many triples the model identifies in total.\n\nThe intuition is as follows. A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high $\\text{Evi-Recall}_{\\text{TP}}$ and low $\\text{Rel-Recall}$, yielding a high EDCR. This pattern signals that evidence quality has decoupled from extraction capability: the model produces faithful evidence only within a narrow comfort zone.\n\nEDCR operates at two diagnostic levels. At the method level, comparing EDCR across optimization paradigms reveals a strong negative correlation with Rel-F1 (Spearman $\\rho{=}{-}0.965$): methods with higher EDCR produce worse extraction, confirming that elevated EDCR signals problematic decoupling. At the per-relation level, computing EDCR for individual relation types reveals variation that is independent of Evi-F1 ($\\rho{=}{-}0.064$, $p{=}0.58$). This independence means EDCR captures relation-specific extraction-evidence misalignment that aggregate evidence metrics miss. In practice, EDCR values above 0.70 indicate concerning decoupling, while values below 0.65 (e.g., RSFT at 0.6503) reflect healthy co-optimization of both capabilities.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}\n\\label{sec:task}\n\nGiven a document $D = \\{s_1, \\ldots, s_n\\}$ consisting of $n$ sentences and a set of entities $\\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \\in \\mathcal{E} \\times \\mathcal{E}$, a relation $r \\in \\mathcal{R} \\cup \\{\\texttt{NA}\\}$ together with a set of supporting evidence sentences $E \\subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation additionally requires $E$, which grounds each prediction in specific textual support.\n\nIn our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \\texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\\citep{xie2022sais} and DREEAM~\\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.\n\n\n\\subsection{Supervised Fine-Tuning Baseline}\n\\label{sec:sft}\n\nWe fine-tune all models with LoRA~\\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\\alpha{=}128$, applied to attention projection matrices. The training data consists of DocRED~\\citep{yao2019docred} training documents converted to the structured output format described above, where each example maps a document and its entity set to the complete set of relation triples with evidence annotations. We additionally train a \\emph{no-evidence} variant under identical configuration but with evidence references removed from the output format, producing only \\texttt{(head, relation, tail)}. This variant serves as an upper bound on extraction performance by eliminating the generation cost of evidence, and allows direct measurement of the evidence tax at each model scale. Detailed hyperparameters (learning rate, batch size, number of epochs) are reported in the Appendix.\n\n\n\\subsection{Optimization Paradigms}\n\\label{sec:paradigms}\n\nWe evaluate three post-SFT optimization paradigms that differ in how they incorporate quality signals from the CED scoring function (\\S\\ref{sec:ced}).\n\n\\paragraph{GRPO.}\nGroup Relative Policy Optimization~\\citep{shao2024deepseekmath} is an online RL method that eliminates the need for a separate value network by computing advantages within groups of sampled outputs. For each training document, the policy generates $G$ candidate responses, which are scored by CED. The advantage of each response is computed relative to the group mean, and the policy is updated to increase the probability of above-average outputs. We test two configurations: QLoRA with $G{=}4$ groups under 4-bit quantization, and bf16 full-precision LoRA with $G{=}8$. Because GRPO applies gradient updates that directly optimize the reward signal, evidence quality and extraction accuracy compete for gradient capacity. We analyze this multi-objective tension in Section~\\ref{sec:spectrum}.\n\n\\paragraph{DPO.}\nDirect Preference Optimization~\\citep{rafailov2023direct} reformulates RLHF as a classification problem over preference pairs, without explicit reward models. We construct preference data from the SFT model's sampled outputs: for each document, the response with the highest CED score is labeled as preferred and the lowest-scoring response as rejected. DPO then adjusts the policy to increase the log-probability ratio between preferred and rejected completions. We train for 1 and 3 epochs to observe the temporal dynamics of evidence-extraction trade-offs under implicit optimization.\n\n\\paragraph{RSFT.}\nRejection Sampling Fine-Tuning is a single-round variant of iterative self-improvement methods such as STaR~\\citep{zelikman2022star}. The procedure is straightforward: the SFT model generates $N{=}8$ candidate outputs per training document, each candidate is scored by CED, and only the top-$k{=}1$ response is retained as training data. From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3\\% acceptance rate). Unlike GRPO and DPO, RSFT does not apply gradient-based optimization pressure toward a reward signal. Instead, it improves training data quality through filtering: the model trains on its own best outputs rather than all outputs. This distinction is critical because discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods find. The contribution of RSFT in our setting is not the framework itself, which is well-established, but its application to evidence-grounded DocRE with CED as a domain-specific quality filter.\n\n\n\\subsection{Contrastive Evidence Discrimination}\n\\label{sec:ced}\n\nCED is a scoring function that evaluates the faithfulness of predicted evidence sentences to their associated relation triples. It builds on Natural Language Inference (NLI) to measure whether evidence actually entails the predicted relation, rather than merely co-occurring with the relevant entities.\n\nFor a predicted triple $(e_h, r, e_t)$ with evidence sentences $E$, CED constructs a positive NLI pair: the premise is the concatenation of sentences in $E$, and the hypothesis is a natural-language verbalization of the relation (e.g., ``$e_h$ has relation $r$ with $e_t$''). An NLI model (\\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair. The contrastive component introduces hard negatives drawn from the same document. For each triple, we collect sentences that mention $e_h$ or $e_t$ but are not in the predicted evidence set. These entity-sharing distractors serve as negative premises, and the NLI model scores each to obtain $p^-_1, \\ldots, p^-_m$. The CED score for a single triple is:\n\\begin{equation}\n\\text{CED}(e_h, r, e_t, E) = p^+ - \\max_j \\, p^-_j\n\\label{eq:ced}\n\\end{equation}\nThis formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities. A high CED score indicates that the evidence provides relation-specific support beyond entity co-occurrence.\n\nThe document-level CED score aggregates over all predicted triples, weighted by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit. This coupling ensures that CED rewards both faithful evidence and accurate extraction jointly.\n\nWe also evaluate a \\emph{flat-NLI} baseline that uses only the positive entailment score $p^+$ without the contrastive term. In our experiments (Section~\\ref{sec:spectrum}), CED and flat-NLI produce statistically indistinguishable RSFT outcomes (paired $t$-test, $p{=}0.44$), but both outperform random selection and no-scoring baselines. We adopt CED as the default because the contrastive formulation provides interpretable per-triple discrimination scores that flat-NLI lacks.\n\n\n\\subsection{Evidence-Decoupling Ratio}\n\\label{sec:edcr}\n\nWe introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric that quantifies the degree of misalignment between a model's extraction and evidence capabilities. EDCR is not a training component; it serves purely as an analytical tool for comparing optimization methods.\n\nEDCR is defined as:\n\\begin{equation}\n\\text{EDCR} = \\frac{\\text{Evi-Recall}_{\\text{TP}}}{\\text{Rel-Recall}}\n\\label{eq:edcr}\n\\end{equation}\nwhere $\\text{Evi-Recall}_{\\text{TP}}$ is evidence sentence recall computed only over correctly predicted triples (true positives), and $\\text{Rel-Recall}$ is overall relation extraction recall. The numerator captures evidence quality on the subset of triples the model gets right; the denominator captures how many triples the model identifies in total.\n\nThe intuition is as follows. A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high $\\text{Evi-Recall}_{\\text{TP}}$ and low $\\text{Rel-Recall}$, yielding a high EDCR. This pattern signals that evidence quality has decoupled from extraction capability: the model produces faithful evidence only within a narrow comfort zone.\n\nEDCR operates at two diagnostic levels. At the method level, comparing EDCR across optimization paradigms reveals a strong negative correlation with Rel-F1 (Spearman $\\rho{=}{-}0.965$): methods with higher EDCR produce worse extraction, confirming that elevated EDCR signals problematic decoupling. At the per-relation level, computing EDCR for individual relation types reveals variation that is independent of Evi-F1 ($\\rho{=}{-}0.064$, $p{=}0.58$). This independence means EDCR captures relation-specific extraction-evidence misalignment that aggregate evidence metrics miss. In practice, EDCR values above 0.70 indicate concerning decoupling, while values below 0.65 (e.g., RSFT at 0.6503) reflect healthy co-optimization of both capabilities.\n"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-17T16:29:59.484574+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-17T16:29:59.484751+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "file=\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex\" && echo \"=== em-dash ===\" && grep -n \"—\" \"$file\" || echo \"None\" && echo \"=== explanatory en-dash ===\" && grep -n \" – \" \"$file\" || echo \"None\" && echo \"=== -ing phrase endings ===\" && grep -n \"ing\\.\\$\\|ing,\\$\\|ing\\\\\\\\\\\\\\\\\\$\" \"$file\" || echo \"None\" && echo \"=== word count ===\" && wc -w \"$file\"",
  "description": "Check for style violations in method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "file=\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex\" && echo \"=== em-dash ===\" && grep -n \"—\" \"$file\" || echo \"None\" && echo \"=== explanatory en-dash ===\" && grep -n \" – \" \"$file\" || echo \"None\" && echo \"=== -ing phrase endings ===\" && grep -n \"ing\\.\\$\\|ing,\\$\\|ing\\\\\\\\\\\\\\\\\\$\" \"$file\" || echo \"None\" && echo \"=== word count ===\" && wc -w \"$file\"",
    "description": "Check for style violations in method.tex"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-17T16:29:59.484910+00:00_

=== em-dash ===
None
=== explanatory en-dash ===
None
=== -ing phrase endings ===
None
=== word count ===
1243 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-17T16:29:59.485036+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -in \"furthermore\\|moreover\\|additionally\\|delve\\|leverage\\|utilize\\|facilitate\\|a myriad\\|a plethora\\|in the realm\\|paradigm shift\\|\\\\\\\\begin{document}\\|\\\\\\\\end{document}\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex || echo \"No blacklisted terms found\"",
  "description": "Check for blacklisted words and patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -in \"furthermore\\|moreover\\|additionally\\|delve\\|leverage\\|utilize\\|facilitate\\|a myriad\\|a plethora\\|in the realm\\|paradigm shift\\|\\\\\\\\begin{document}\\|\\\\\\\\end{document}\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex || echo \"No blacklisted terms found\"",
    "description": "Check for blacklisted words and patterns"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-17T16:29:59.485192+00:00_

7:Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation additionally requires $E$, which grounds each prediction in specific textual support.
15:We fine-tune all models with LoRA~\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\alpha{=}128$, applied to attention projection matrices. The training data consists of DocRED~\citep{yao2019docred} training documents converted to the structured output format described above, where each example maps a document and its entity set to the complete set of relation triples with evidence annotations. We additionally train a \emph{no-evidence} variant under identical configuration but with evidence references removed from the output format, producing only \texttt{(head, relation, tail)}. This variant serves as an upper bound on extraction performance by eliminating the generation cost of evidence, and allows direct measurement of the evidence tax at each model scale. Detailed hyperparameters (learning rate, batch size, number of epochs) are reported in the Appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-17T16:29:59.485458+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
  "old_string": "the evidence-grounded formulation additionally requires $E$",
  "new_string": "the evidence-grounded formulation also requires $E$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
    "old_string": "the evidence-grounded formulation additionally requires $E$",
    "new_string": "the evidence-grounded formulation also requires $E$"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-17T16:29:59.485637+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-17T16:29:59.485767+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
  "old_string": "We additionally train a \\emph{no-evidence} variant",
  "new_string": "We also train a \\emph{no-evidence} variant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
    "old_string": "We additionally train a \\emph{no-evidence} variant",
    "new_string": "We also train a \\emph{no-evidence} variant"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-17T16:29:59.485922+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-17T16:29:59.486061+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo \"=== Method params ===\" && grep -oP '(r\\{=\\}64|alpha\\{=\\}128|N\\{=\\}8|k\\{=\\}1|G\\{=\\}4|G\\{=\\}8|9,042|24,216|37\\.3|0\\.6503|0\\.965|0\\.064|0\\.58|0\\.44|0\\.70|0\\.65|sec:ced)' /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex && echo \"=== Experiment refs ===\" && grep -oP '(r\\{=\\}64|alpha\\{=\\}128|N\\{=\\}8|k\\{=\\}1|G\\{=\\}4|G\\{=\\}8|sec:ced|0\\.70)' /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
  "description": "Verify parameter consistency between method and experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "tool_args": {
    "command": "echo \"=== Method params ===\" && grep -oP '(r\\{=\\}64|alpha\\{=\\}128|N\\{=\\}8|k\\{=\\}1|G\\{=\\}4|G\\{=\\}8|9,042|24,216|37\\.3|0\\.6503|0\\.965|0\\.064|0\\.58|0\\.44|0\\.70|0\\.65|sec:ced)' /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex && echo \"=== Experiment refs ===\" && grep -oP '(r\\{=\\}64|alpha\\{=\\}128|N\\{=\\}8|k\\{=\\}1|G\\{=\\}4|G\\{=\\}8|sec:ced|0\\.70)' /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
    "description": "Verify parameter consistency between method and experiments"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-17T16:29:59.486204+00:00_

=== Method params ===
r{=}64
alpha{=}128
sec:ced
G{=}4
G{=}8
N{=}8
k{=}1
24,216
9,042
37.3
sec:ced
0.44
0.965
0.064
0.58
0.70
0.65
0.6503
=== Experiment refs ===
r{=}64
alpha{=}128
N{=}8
k{=}1
sec:ced
G{=}4
G{=}8
0.70
G{=}4
G{=}8
G{=}4
G{=}8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-17T16:29:59.486386+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-17T16:29:59.486516+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-17T16:29:59.486634+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "method-section-tex",
  "type": "paper",
  "description": "Method section (Section 3) LaTeX for EMNLP 2026 paper. Covers task formulation, SFT baseline, three optimization paradigms (GRPO/DPO/RSFT), CED scoring, and EDCR diagnostic metric. ~1243 words.",
  "project": "faith-evidence-ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
  "tags": "['paper', 'method', 'latex']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "method-section-tex",
    "type": "paper",
    "description": "Method section (Section 3) LaTeX for EMNLP 2026 paper. Covers task formulation, SFT baseline, three optimization paradigms (GRPO/DPO/RSFT), CED scoring, and EDCR diagnostic metric. ~1243 words.",
    "project": "faith-evidence-ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
    "tags": "['paper', 'method', 'latex']"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-17T16:29:59.486776+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260517_bac823\", \"name\": \"method-section-tex\", \"type\": \"paper\", \"description\": \"Method section (Section 3) LaTeX for EMNLP 2026 paper. Covers task formulation, SFT baseline, three optimization paradigms (GRPO/DPO/RSFT), CED scoring, and EDCR diagnostic metric. ~1243 words.\", \"path\": \"projects/faith-evidence-ie/artifacts/_project/paper/method.tex\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-17T16:29:47.753824+00:00\", \"tags\": [\"paper\", \"method\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T162426",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 107 · 2026-05-17T16:29:59.486951+00:00_

Method section 写入 `docs/paper/sections/method.tex`，~1243 words，5 个子节：

- **3.1 Task** — 形式化定义 evidence-grounded DocRE，区分 encoder-based 方法（SAIS/DREEAM 无生成开销）与 LLM 生成式方法（scale-dependent cost）
- **3.2 SFT Baseline** — LoRA r=64/α=128，含 no-evidence upper bound 变体
- **3.3 Optimization Paradigms** — GRPO (QLoRA G=4, bf16 G=8)、DPO (1ep/3ep)、RSFT (N=8, top-k=1, 9042/24216=37.3%)
- **3.4 CED** — NLI entailment + entity-sharing hard negatives 对比评分，含 flat-NLI baseline 对比（p=0.44），`\label{sec:ced}` 已设置
- **3.5 EDCR** — 诊断指标定义 Evi-Recall\_TP / Rel-Recall，method-level ρ=-0.965，per-relation ρ=-0.064，阈值 0.70/0.65

所有参数与 experiments.tex 一致。无 em-dash、无 -ing 短语结尾、无黑名单词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_20260517T162426"
}
```

</details>

---
