# paper ref audit B

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 126
- **Recorded user turns:** 0
- **Tool calls:** 62
- **Original source:** `logs/chats/worker_paper_ref-audit-B_20260526T104639.jsonl`
- **Structured JSON:** [`3e9c53733f8f7c4fcb23.json`](../../sessions/3e/3e9c53733f8f7c4fcb23.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

126 recorded events

### Assistant

_source line 1 · 2026-05-26T10:46:47.835551+00:00_

You've hit your limit · resets May 28, 1pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_ref-audit-B_20260526T104639"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-26T10:56:42.704040+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-26T10:56:42.704450+00:00_

_figure_backups
abstract.tex
acl.sty
acl_natbib.bst
atlas.tex
conclusion.tex
discussion.tex
drafts
figures
generalization.tex
introduction.tex
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
section_appendix.tex
theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T10:56:42.704684+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/ 2>/dev/null",
  "description": "List drafts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/ 2>/dev/null",
    "description": "List drafts directory"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-26T10:56:42.704909+00:00_

14b_scenarios.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T10:56:42.705114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T10:56:42.705396+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026
3	\documentclass[11pt]{article}
4	
5	% Change "review" to "final" to generate the camera-ready version.
6	\usepackage[review]{acl}
7	
8	% Standard package includes (per official ACL template)
9	\usepackage{times}
10	\usepackage{latexsym}
11	\usepackage[T1]{fontenc}
12	\usepackage[utf8]{inputenc}
13	\usepackage{microtype}
14	% \usepackage{inconsolata}  % not available in this TeX installation
15	\usepackage{graphicx}
16	
17	% Additional packages for this paper
18	\usepackage{booktabs}
19	\usepackage{amsmath}
20	\usepackage{amssymb}
21	\usepackage{multirow}
22	\usepackage{subcaption}
23	\usepackage{enumitem}
24	\usepackage{amsthm}
25	
26	\theoremstyle{definition}
27	\newtheorem{definition}{Definition}
28	
29	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
30	
31	\author{Anonymous}
32	
33	\begin{document}
34	\maketitle
35	
36	\input{abstract}
37	
38	\input{introduction}
39	
40	\input{related_work}
41	
42	\input{method}
43	
44	\input{theory}
45	
46	\input{atlas}
47	
48	\input{generalization}
49	
50	\input{discussion}
51	
52	\input{conclusion}
53	
54	\bibliography{references}
55	
56	\appendix
57	\input{section_appendix}
58	
59	\end{document}
60	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:56:42.705634+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[tp]?\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T10:56:42.705984+00:00_

docs/paper/related_work.tex:5:Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad} and Markovian generation chains \cite{geng2026_markovian}.
docs/paper/related_work.tex:6:\citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (grounding our EDD ceiling, \S\ref{sec:method:theory}); refinements address generalization-to-memorization transitions \cite{shi2025_closer_look} and broader model classes \cite{dohmatob2025_strong_collapse}.
docs/paper/related_work.tex:7:\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena; we respond by operationalizing tail-erosion into a deployable ordinal classifier that reveals strategy-dependent trajectories the theory does not predict.
docs/paper/related_work.tex:11:The detection literature \cite{wu2025_detection_survey} spans statistical \cite{mitchell2023_detectgpt,fast_detectgpt2024,binoculars2024,gehrmann2019_gltr,verma2024_ghostbuster}, geometric \cite{tulchinskii2023_intrinsic_dim}, and watermarking \cite{kirchenbauer2023_watermark} methods, with known limits \cite{sadasivan2023_paraphrase,pudasaini2026_detection_fails}.
docs/paper/related_work.tex:12:\citet{bevendorff2025_two_paradigms} distinguish attribution from verification; all remain binary, whereas our approach outputs ordinal depth labels along a third axis, recursive iteration.
docs/paper/related_work.tex:15:Training data extraction \cite{carlini2021_extracting} motivates provenance pipelines; Min-K\% Prob \cite{shi2024_minkprob}, Datamodels \cite{ilyas2022datamodels}, watermarks \cite{christ2024_undetectable}, and TROVE \cite{zhu2025_trove} address membership inference or source attribution but remain binary or cooperation-dependent.
docs/paper/related_wo
…[truncated 9391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:56:42.706256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T10:56:42.706785+00:00_

1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},

…[truncated 31307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:56:42.707110+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T10:56:42.707320+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:56:42.707513+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T10:56:42.707701+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T10:56:42.707906+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T10:56:42.708103+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:56:42.708291+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T10:56:42.708524+00:00_

59:We compute conditional permutation importance (CPI) \citep{strobl2008_conditional}, which permutes each feature \emph{within strata defined by its correlated partners}, isolating the unique contribution after controlling for multicollinearity.
336:DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.7\%) by 20.4pp and 19.2pp.
363:DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
513:We extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct \cite{qwen2.5}, Llama-3.1-8B-Instruct \cite{llama3}) and one 14B model (Qwen2.5-14B).
658:To isolate the scale effect from these artifacts, we run the full recursive generation pipeline on Qwen2.5-7B \cite{qwen2.5} (base model, not instruction-tuned) using FP16 LoRA fine-tuning and self-reference feature extraction (the same model serves as both generator and reference).
796:Table~\ref{tab:learned_estimator} evaluates three learned classifiers (XGBoost, ordinal MLP with CORAL loss \cite{coral2020}, prototypical networks) under the same leave-one-model-out protocol as Table~\ref{tab:cross_model}.
797:The ordinal MLP follows the nested binary reduction framework \cite{mccullagh1980_ordinal,frank2001} with the loss function of \citet{rennie2005}.
939:Binoculars~\cite{binoculars2024} and Fast-DetectGPT~\cite{fast_detectgpt2024} scores are computed on the Pythia-1.4B nucleus ($p{=}0.95$) subset and fed to: (a)~a log-likelihood rank classifier (Log-Rank, 64.0\%), (b)~a combined RF trained on both detector scores (Combined, 74.2\%), and (c)~the standard 19-feature RF (78.7\%).
945:DetectGPT~\cite{mitchell2023_detectgpt} (gpt2-large scoring model, t5-larg
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T10:56:42.708840+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T10:56:42.709072+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:56:42.709297+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Markovian Generation Chains\" Geng Mohamed Shang Vazirgiannis 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Markovian Generation Chains\" Geng Mohamed Shang Vazirgiannis 2026 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T10:56:42.709492+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LLM as a Broken Telephone\" Mohamed Geng iterative generation arxiv 2502.20258"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LLM as a Broken Telephone\" Mohamed Geng iterative generation arxiv 2502.20258"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T10:56:42.709702+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Closer Look at Model Collapse\" Shi Wu Zhang generalization memorization NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Closer Look at Model Collapse\" Shi Wu Zhang generalization memorization NeurIPS 2025"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T10:56:42.709918+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Strong Model Collapse\" Dohmatob Feng Subramonian Kempe ICLR 2025 arxiv 2410.04840"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Strong Model Collapse\" Dohmatob Feng Subramonian Kempe ICLR 2025 arxiv 2410.04840"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T10:56:42.710173+00:00_

Web search results for query: ""Strong Model Collapse" Dohmatob Feng Subramonian Kempe ICLR 2025 arxiv 2410.04840"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=MQXrTMonT1"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534888-tale-tails-model-collapse-change-scaling-laws"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective | Request PDF","url":"https://www.researchgate.net/publication/395724450_A_Closer_Look_at_Model_Collapse_From_a_Generalization-to-Memorization_Perspective"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"}]

I found the paper! Here's information about "Strong Model Collapse":

#
…[truncated 1200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:56:42.710546+00:00_

Web search results for query: ""Markovian Generation Chains" Geng Mohamed Shang Vazirgiannis 2026 arxiv"

Links: [{"title":"[2603.11228] Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/abs/2603.11228"},{"title":"Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/html/2603.11228"},{"title":"[2502.20258] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/abs/2502.20258"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | Request PDF","url":"https://www.researchgate.net/publication/394300051_LLM_as_a_Broken_Telephone_Iterative_Generation_Distorts_Information"},{"title":"Markovian Generation Chains in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nTDn4OMiym"},{"title":"From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers","url":"https://arxiv.org/html/2402.13512v1"},{"title":"Large Language Models as Markov Chains","url":"https://arxiv.org/html/2410.02724v1"},{"title":"From Self-Attention to Markov Models:","url":"https://arxiv.org/pdf/2402.13512"}]

I found the paper you're looking for! Here are the details:

**Markovian Generation Chains in Large Language Models**

Submitted on 11 Mar 2026 by authors: Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, and Thierry Poibeau

**Overview:**
The paper addresses the question: how do texts evolve when they are repeatedly processed by LLMs? The iterative inference process is defined as Markovian generation chains, where each step takes a specific prompt template and the previous output as input, without including any prior memory.

**Key Findings:**
In iterative rephrasing and round-trip translation experiments, the output either converges to a small recurrent set or continues to produce novel sentences over a finite horizon. Through sentence-level Markov chain modeling and analysis of simulated data, they show that the
…[truncated 307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T10:56:42.710756+00:00_

Web search results for query: ""A Closer Look at Model Collapse" Shi Wu Zhang generalization memorization NeurIPS 2025"

Links: [{"title":"NeurIPS Poster A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://neurips.cc/virtual/2025/poster/119754"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://shilianghe007.github.io/model-collapse/index.html"},{"title":"[2509.16499] A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/abs/2509.16499"},{"title":"Fifteen papers by ECE researchers at NeurIPS 2025","url":"https://ece.engin.umich.edu/stories/fifteen-papers-by-ece-researchers-at-neurips-2025"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective | Request PDF","url":"https://www.researchgate.net/publication/395724450_A_Closer_Look_at_Model_Collapse_From_a_Generalization-to-Memorization_Perspective"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=1225&show=100"}]

I found the paper! Here are the results for your search:

**"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"**

**Authors:** Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, and Qing Qu

**Venue:** NeurIPS 2025 Spotlight Poster

**Key Findings:**

The paper identifies a transition from generalization to memorization during model collapse in diffusion models, where models increasingly replicate training data instead of generating novel content during iterative training on synthetic samples.

This transition is directly driven by the declining entropy of the synthetic training data produced in each training cycle, which serves as a clear indicator of model degradation.

**Proposed Solution:**


…[truncated 620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T10:56:42.711008+00:00_

Web search results for query: ""LLM as a Broken Telephone" Mohamed Geng iterative generation arxiv 2502.20258"

Links: [{"title":"[2502.20258] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/abs/2502.20258"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/html/2502.20258"},{"title":"Paper page - LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://huggingface.co/papers/2502.20258"},{"title":"dblp: LLM as a Broken Telephone: Iterative Generation Distorts Information.","url":"https://dblp.org/rec/journals/corr/abs-2502-20258.html"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.20258v1"},{"title":"GitHub - amr-mohamedd/LLM-as-a-Broken-Telephone: [ACL 2025] Code implementation for the \"LLM as a Broken Telephone: Iterative Generation Distorts Information\" paper.","url":"https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.371/"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | Request PDF","url":"https://www.researchgate.net/publication/394300051_LLM_as_a_Broken_Telephone_Iterative_Generation_Distorts_Information"},{"title":"Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/html/2603.11228"}]

I found the paper! Here's information about "LLM as a Broken Telephone: Iterative Generation Distorts Information" (arXiv:2502.20258):

## Overview

Inspired by the "broken telephone" effect in chained human communication, this study investigates whether LLMs similarly distort information through iterative generation.

## Key Findings

Through translation-based experiments, the researchers find that distortion accumulates over time, influenced by lang
…[truncated 835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T10:56:42.711290+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Position: Model Collapse Does Not Mean What You Think\" Schaeffer Kazdan arxiv 2503.03150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Position: Model Collapse Does Not Mean What You Think\" Schaeffer Kazdan arxiv 2503.03150"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T10:56:42.711491+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Machine-generated text detection prevents language model collapse\" Drayson Yilmaz Lampos EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Machine-generated text detection prevents language model collapse\" Drayson Yilmaz Lampos EMNLP 2025"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:56:42.711682+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen TMLR arxiv 2509.18880"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen TMLR arxiv 2509.18880"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T10:56:42.711891+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Why AI-Generated Text Detection Fails\" Pudasaini Lillis arxiv 2603.23146"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Why AI-Generated Text Detection Fails\" Pudasaini Lillis arxiv 2603.23146"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-26T10:56:42.712152+00:00_

Web search results for query: ""Position: Model Collapse Does Not Mean What You Think" Schaeffer Kazdan arxiv 2503.03150"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v1"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model TrainingAuthors ordered alphabetically. Author contributions are listed at the end.","url":"https://arxiv.org/html/2502.08924v2"},{"title":"Computers and Society Mar 2025","url":"https://arxiv.org/list/cs.CY/2025-03?skip=300&show=25"},{"title":"Recursive Training Loops in LLMs: How training data properties modulate distribution shift in generated data?","url":"https://arxiv.org/html/2504.03814v4"},{"title":"Position: Machine Learning Conferences Should Establish a “Refutations and Critiques” Track","url":"https://arxiv.org/html/2506.19882"}]

I found the paper! Here's what I can tell you about it:

## "Position: Model Collapse Does Not Mean What You Think"

**Authors:** Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo

**arxiv ID:** 2503.03150 (submitted March 5, 2025, last revised March 18, 2025)

### Main Arguments

The paper addresses concerns over model collapse, which is a degradation in future generative models' performance when trained on synthetic data generated by earlier models.

The authors contend that the widespread narrative fundamentally misunderstands the scientific evidence, and highlight that research on 
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T10:56:42.712452+00:00_

Web search results for query: ""Why AI-Generated Text Detection Fails" Pudasaini Lillis arxiv 2603.23146"

Links: [{"title":"[2603.23146] Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy","url":"https://arxiv.org/abs/2603.23146"},{"title":"[2603.23146v1] Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy","url":"https://arxiv.org/abs/2603.23146v1"},{"title":"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy","url":"https://arxiv.org/html/2603.23146v2"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"PADBen: A Comprehensive Benchmark for Evaluating AI Text Detectors Against Paraphrase Attacks","url":"https://arxiv.org/html/2511.00416v1"},{"title":"Detecting AI-Generated Text: Factors Influencing Detectability with Current Methods","url":"https://arxiv.org/html/2406.15583v1"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Uncertainty in Authorship: Why Perfect AI Detection Is Mathematically Impossible","url":"https://arxiv.org/html/2509.11915v1"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"}]

I found the paper you're looking for! Here's what the research shows:

## Paper Overview

The widespread adoption of Large Language Models (LLMs) has made the detection of AI-generated text a pressing challenge, and although many detection systems report high benchmark accuracy, their reliability in real-world settings remains uncertain, and their interpretability is often unexplored.

## Key Findings

The researchers investigated whether contemporary detectors genuinely identify machine authorship or merely exploit dataset-specific artifacts. They proposed an interpretable detection framework that integrates
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T10:56:42.712738+00:00_

Web search results for query: ""Machine-generated text detection prevents language model collapse" Drayson Yilmaz Lampos EMNLP 2025"

Links: [{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654v6"},{"title":"Machine-generated text detection prevents language model ...","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/1/2025.emnlp-main.1506.pdf"},{"title":"Machine-generated text detection prevents language model collapse - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/"},{"title":"Machine-generated text detection prevents language ...","url":"https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"},{"title":"GitHub - GeorgeDrayson/model_collapse","url":"https://github.com/GeorgeDrayson/model_collapse"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341v3"}]

I found the paper you were looking for! Here's what I found:

## Paper Details

The paper "Machine-generated text detection prevents language model collapse" was authored by George Drayson, Emine Yilmaz, and Vasileios Lampos and was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing. The conference took place November 4-9, 2025.

## Research Overview

The research addresses how machine-generated content is proliferating across the web, risking a future where it dilutes human-authored text. Since online data is the primary resource for LLM pre-training, subsequent models could be trained on an unknown portion of synthetic samples, whic
…[truncated 645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T10:56:42.713035+00:00_

Web search results for query: ""Diversity Boosts AI-Generated Text Detection" Basani Chen TMLR arxiv 2509.18880"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.researchgate.net/publication/395771470_Diversity_Boosts_AI-Generated_Text_Detection"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=12550&show=25"},{"title":"When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection","url":"https://arxiv.org/html/2601.04833v1"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=3550&show=50"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"}]

I found the paper you're looking for. Here's the information about it:

## "Diversity Boosts AI-Generated Text Detection"

**Authors:** Advik Raj Basani and Pin-Yu Chen

**Paper ID:** arXiv:2509.18880

**Publication:** Accepted to Transactions on Machine Learning Research (TMLR '26)

**Overview:**
The paper proposes DivEye, a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features. It is motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs.

**Key Results:**
The method outperforms existing zero-shot detectors by up to 33.2% and achi
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T10:56:42.713282+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EditLens\" \"Quantifying the Extent of AI Editing\" Thai Emi Iyyer arxiv 2510.03154"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EditLens\" \"Quantifying the Extent of AI Editing\" Thai Emi Iyyer arxiv 2510.03154"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T10:56:42.713485+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"TROVE\" Zhu fine-grained text provenance source sentence tracing ACL 2025 arxiv 2503.15289"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"TROVE\" Zhu fine-grained text provenance source sentence tracing ACL 2025 arxiv 2503.15289"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-26T10:56:42.713686+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Two Paradigms of LLM Detection\" Bevendorff Wiegmann authorship attribution verification Findings ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Two Paradigms of LLM Detection\" Bevendorff Wiegmann authorship attribution verification Findings ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:56:42.713926+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CLOC\" Contrastive Learning Ordinal Classification Pitawela Carneiro CVPR 2025 arxiv 2504.17813"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CLOC\" Contrastive Learning Ordinal Classification Pitawela Carneiro CVPR 2025 arxiv 2504.17813"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-26T10:56:42.714170+00:00_

Web search results for query: ""TROVE" Zhu fine-grained text provenance source sentence tracing ACL 2025 arxiv 2503.15289"

Links: [{"title":"TROVE: A Challenge for Fine-Grained Text Provenance via Source Sentence Tracing and Relationship Classification - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.577/"},{"title":"TROVE: A Challenge for Fine-Grained Text Provenance via ...","url":"https://aclanthology.org/2025.acl-long.577.pdf"},{"title":"[2503.15289] TROVE: A Challenge for Fine-Grained Text Provenance via Source Sentence Tracing and Relationship Classification","url":"https://arxiv.org/abs/2503.15289"},{"title":"[Quick Review] TROVE: A Challenge for Fine-Grained Text Provenance via Source Sentence Tracing and Relationship Classification","url":"https://liner.com/review/trove-challenge-for-finegrained-text-provenance-via-source-sentence-tracing"},{"title":"TROVE: A Challenge for Fine-Grained Text Provenance via ...","url":"https://www.nlpr.ia.ac.cn/cip/ZongPublications/2025/2025-ZhuJunnan-ACL.pdf"},{"title":"TROVE: A Challenge for Fine-Grained Text Provenance via Source Sentence Tracing and Relationship Classification","url":"https://arxiv.org/html/2503.15289v3"},{"title":"Computation and Language Mar 2025","url":"https://www.arxiv.org/list/cs.CL/2025-03?skip=900&show=100"},{"title":"Computation and Language 2025","url":"https://www.arxiv.org/list/cs.CL/2025?skip=3650&show=2000"}]

I found the paper you're looking for! Here's what I discovered:

TROVE: A Challenge for Fine-Grained Text Provenance via Source Sentence Tracing and Relationship Classification was published by Zhu et al. at ACL 2025.

The TROVE challenge is designed to trace each sentence of a target text back to specific source sentences within potentially lengthy or multi-document inputs, and annotates fine-grained relationships (quotation, compression, inference, and others) to provide a deep understanding of how each target sentence is formed.

The dataset was constructed by leverag
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-26T10:56:42.714464+00:00_

Web search results for query: ""EditLens" "Quantifying the Extent of AI Editing" Thai Emi Iyyer arxiv 2510.03154"

Links: [{"title":"[2510.03154] EditLens: Quantifying the Extent of AI Editing in Text","url":"https://arxiv.org/abs/2510.03154"},{"title":"EditLens: Quantifying the Extent of AI Editing in Text","url":"https://arxiv.org/pdf/2510.03154"},{"title":"(PDF) EditLens: Quantifying the Extent of AI Editing in Text","url":"https://www.researchgate.net/publication/396223292_EditLens_Quantifying_the_Extent_of_AI_Editing_in_Text"},{"title":"Paper page - EditLens: Quantifying the Extent of AI Editing in Text","url":"https://huggingface.co/papers/2510.03154"},{"title":"EditLens: Quantifying the Extent of AI Editing in Text","url":"https://chatpaper.com/paper/195828"},{"title":"[Paper Note] EditLens: Quantifying the Extent of AI Editing in Text, Katherine Thai+, arXiv'25, 2025.10 · Issue #3696 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3696"},{"title":"[PDF] EditLens: Quantifying the Extent of AI Editing in Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/EditLens:-Quantifying-the-Extent-of-AI-Editing-in-Thai-Emi/5e7890592dea915fb5b61be51030add4bf384787"},{"title":"GitHub - pangramlabs/EditLens · GitHub","url":"https://github.com/pangramlabs/EditLens"},{"title":"dblp: EditLens: Quantifying the Extent of AI Editing in Text.","url":"https://dblp.org/rec/journals/corr/abs-2510-03154.html"}]

I found the paper! Here are the search results for "EditLens: Quantifying the Extent of AI Editing in Text":

## Overview

A significant proportion of queries to large language models ask them to edit user-provided text, rather than generate new text from scratch.

## Main Contribution

AI-edited text is distinguishable from human-written and AI-generated text. The researchers propose using lightweight similarity metrics to quantify the magnitude of AI editing present in a text given the original human-written text
…[truncated 874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-26T10:56:42.714764+00:00_

Web search results for query: ""CLOC" Contrastive Learning Ordinal Classification Pitawela Carneiro CVPR 2025 arxiv 2504.17813"

Links: [{"title":"CLOC: Contrastive Learning for Ordinal Classification with ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Pitawela_CLOC_Contrastive_Learning_for_Ordinal_Classification_with_Multi-Margin_N-pair_Loss_CVPR_2025_paper.pdf"},{"title":"[2504.17813] CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss","url":"https://arxiv.org/abs/2504.17813"},{"title":"GitHub - dpitawela/CLOC · GitHub","url":"https://github.com/dpitawela/CLOC"},{"title":"CVPR Poster CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss","url":"https://cvpr.thecvf.com/virtual/2025/poster/32653"},{"title":"[PDF] CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CLOC:-Contrastive-Learning-for-Ordinal-with-N-pair-Pitawela-Carneiro/7700b46ac3e76407652c19707bb612adf959dbe7"},{"title":"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss | CoLab","url":"https://colab.ws/articles/10.1109/cvpr52734.2025.01448"},{"title":"250417813 — Grokipedia","url":"https://grokipedia.com/page/250417813"},{"title":"(PDF) CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss","url":"https://www.researchgate.net/publication/391220117_CLOC_Contrastive_Learning_for_Ordinal_Classification_with_Multi-Margin_N-pair_Loss"},{"title":"dblp: Dileepa Pitawela","url":"https://dblp.org/pid/239/2550.html"}]

I found comprehensive information about the CLOC paper. Here's what I found:

## CLOC: Contrastive Learning for Ordinal Classification

CLOC is a margin-based contrastive learning method for ordinal classification that learns an ordered representation based on the optimization of multiple margins with a novel multi-margin n-pair loss (MMNP).

**Problem Address
…[truncated 1450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-26T10:56:42.715071+00:00_

Web search results for query: ""The Two Paradigms of LLM Detection" Bevendorff Wiegmann authorship attribution verification Findings ACL 2025"

Links: [{"title":"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.194/"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"The Two Paradigms of LLM Detection: Authorship ...","url":"https://aclanthology.org/2025.findings-acl.194.pdf"},{"title":"dblp: The Two Paradigms of LLM Detection: Authorship Attribution vs Authorship Verification.","url":"https://dblp.org/rec/conf/acl/BevendorffWRP025.html"},{"title":"Overview of the “Voight-Kampff” Generative AI Authorship ...","url":"https://ceur-ws.org/Vol-4038/paper_277.pdf"},{"title":"Exploring Concept Depth: How Large Language Models ...","url":"https://aclanthology.org/2025.coling-main.37.pdf"}]

I found the paper you're looking for! "The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification" is by Janek Bevendorff, Matti Wiegmann, Emmelie Richter, Martin Potthast, and Benno Stein, published in the Findings of ACL 2025.

The paper appears in the Findings of the Association for Computational Linguistics: ACL 2025, pages 3762–3787, Vienna, Austria.

The paper addresses an important research gap in LLM detection, examining how different paradigms (authorship attribution vs. authorship verification) approach the problem of detecting LLM-generated text. You can access the full paper through the ACL Anthology at https://aclanthology.org/2025.findings-acl.194/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:56:42.715337+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"How Bad is Training on Synthetic Data\" Seddik Chen Hayou Debbah arxiv 2404.05090"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"How Bad is Training on Synthetic Data\" Seddik Chen Hayou Debbah arxiv 2404.05090"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T10:56:42.715536+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Tale of Tails\" Dohmatob Feng Yang Charton Kempe ICML 2024 arxiv 2402.07043"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Tale of Tails\" Dohmatob Feng Yang Charton Kempe ICML 2024 arxiv 2402.07043"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-26T10:56:42.715730+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Self-Consuming Generative Models Go MAD\" Alemohammad Casco-Rodriguez ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Self-Consuming Generative Models Go MAD\" Alemohammad Casco-Rodriguez ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T10:56:42.715941+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Survey on LLM-Generated Text Detection\" Wu Yang Zhan Yuan Chao Wong Computational Linguistics 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Survey on LLM-Generated Text Detection\" Wu Yang Zhan Yuan Chao Wong Computational Linguistics 2025"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:56:42.716193+00:00_

Web search results for query: ""A Tale of Tails" Dohmatob Feng Yang Charton Kempe ICML 2024 arxiv 2402.07043"

Links: [{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"},{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"ICML Poster A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://icml.cc/virtual/2024/poster/34339"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10535859"},{"title":"A tale of tails | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692515"},{"title":"CDS at ICLR 2024: A Showcase of Cutting-Edge Research | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/cds-at-iclr-2024-a-showcase-of-cutting-edge-research-aece9a6b7551"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"[Quick Review] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://liner.com/review/tale-tails-model-collapse-as-change-scaling-laws"}]

I found the paper you're looking for! Here are the details:

"A Tale of Tails: Model Collapse as a Change of Scaling Laws" is a paper by Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, and Julia Kempe, published in the Proceedings of the 41st International Conference on Machine 
…[truncated 987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:56:42.716482+00:00_

Web search results for query: ""How Bad is Training on Synthetic Data" Seddik Chen Hayou Debbah arxiv 2404.05090"

Links: [{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis","url":"https://arxiv.org/pdf/2404.05090"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | alphaXiv","url":"https://www.alphaxiv.org/resources/2404.05090v1"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240405090E/abstract"},{"title":"[PDF] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/how-bad-is-training-synthetic-data-statistical"},{"title":"How Bad is Training on Synthetic Data? A Statistical ...","url":"https://openreview.net/pdf/4b55130ce33429ab600e5cde927dfe10a36328ba.pdf"},{"title":"Real vs Synthetic Data: Is Generative Content in Need of Human Touch - Khalifa University","url":"https://www.ku.ac.ae/real-vs-synthetic-data-is-generative-content-in-need-of-human-touch"},{"title":"arXiv:2410.04840v2 [cs.LG] 8 Oct 2024","url":"https://arxiv.org/pdf/2410.04840"}]

I found the paper! Here's what I can tell you about it:

**Title:** How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse

**Authors:** Moham
…[truncated 1016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:56:42.716761+00:00_

Web search results for query: ""Self-Consuming Generative Models Go MAD" Alemohammad Casco-Rodriguez ICLR 2024"

Links: [{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"Self-Consuming Generative Models Go MAD | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10570494"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"Self-Consuming Generative Models Go MAD | Montreal AI Ethics Institute","url":"https://montrealethics.ai/self-consuming-generative-models-go-mad/"},{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"ICLR Poster Self-Consuming Generative Models Go MAD","url":"https://iclr.cc/virtual/2024/poster/18592"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"(PDF) Self-Consuming Generative Models Go MAD","url":"https://www.researchgate.net/publication/372136378_Self-Consuming_Generative_Models_Go_MAD"}]

I found the paper! Here's what I found about "Self-Consuming Generative Models Go MAD":

## Overview

The paper is by Sina Alemohammad, Josue Casco-Rodriguez, and co-authors, and was presented at the 12th International Conference on Learning Representations (ICLR 2024) in Vienna, Austria.

## Main Topic

The research addresses how advances in generative AI have led to using AI-synthesized data to train next-generation models, crea
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-26T10:56:42.717071+00:00_

Web search results for query: ""A Survey on LLM-Generated Text Detection" Wu Yang Zhan Yuan Chao Wong Computational Linguistics 2025"

Links: [{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/article/view/2687"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://aclanthology.org/2025.cl-1.8.pdf"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/html/2310.14724v3"},{"title":"[PDF] A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-LLM-generated-Text-Detection:-Methods,-Wu-Yang/a09d3686285f609b60b18b5935da64b29a5cce0f"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://ouci.dntb.gov.ua/en/works/420xKD38/"},{"title":"Overview of the NLPCC 2025 Shared Task 1: LLM-Generated Text Detection | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3352-7_21"}]

I found the paper! Here are the search results for "A Survey on LLM-Generated Text Detection" by Wu, Yang, Zhan, Yuan, Chao, 
…[truncated 1028 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T10:56:42.717340+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclanthology.org/2025.cl-1.8/",
  "prompt": "What are the page numbers and exact venue/volume/issue for \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\" by Wu et al.? Report start page and end page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclanthology.org/2025.cl-1.8/",
    "prompt": "What are the page numbers and exact venue/volume/issue for \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\" by Wu et al.? Report start page and end page."
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T10:56:42.717539+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Spotting LLMs With Binoculars\" Hans Schwarzschild Cherepanova ICML 2024 arxiv 2401.12070"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Spotting LLMs With Binoculars\" Hans Schwarzschild Cherepanova ICML 2024 arxiv 2401.12070"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:56:42.717740+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"On the Stability of Iterative Retraining of Generative Models\" Bertrand Bose Duplessis Gidel ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"On the Stability of Iterative Retraining of Generative Models\" Bertrand Bose Duplessis Gidel ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:56:42.717949+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Detecting Pretraining Data from Large Language Models\" Shi Ajith Xia ICLR 2024 Min-K%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Detecting Pretraining Data from Large Language Models\" Shi Ajith Xia ICLR 2024 Min-K%"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-26T10:56:42.718149+00:00_

# Publication Details for Wu et al. Survey

**Page Numbers:** 275–338

**Venue/Volume/Issue:** Computational Linguistics, Volume 51, Issue 1 (March 2025)

The paper spans 64 pages and was published by MIT Press in Cambridge, MA. The DOI is 10.1162/coli_a_00549.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-26T10:56:42.718396+00:00_

Web search results for query: ""On the Stability of Iterative Retraining of Generative Models" Bertrand Bose Duplessis Gidel ICLR 2024"

Links: [{"title":"[2310.00429] On the Stability of Iterative Retraining of Generative Models on their own Data","url":"https://arxiv.org/abs/2310.00429"},{"title":"ON THE STABILITY OF ITERATIVE RETRAINING ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/339cab2a98edcba2d4ac42e5f8b64218-Paper-Conference.pdf"},{"title":"On the Stability of Iterative Retraining of Generative Models on their own Data","url":"https://iclr.cc/media/iclr-2024/Slides/18942.pdf"},{"title":"[2310.00429v3] On the Stability of Iterative Retraining of Generative Models on their own Data","url":"https://arxiv.org/abs/2310.00429v3"},{"title":"Could we see the collapse of generative AI? | Inria","url":"https://www.inria.fr/en/collapse-ia-generatives"},{"title":"On the Stability of Iterative Retraining of Generative Models on their own Data","url":"https://arxiv.org/html/2310.00429v3"},{"title":"On the Stability of Iterative Retraining of Generative Models ...","url":"https://arxiv.org/pdf/2310.00429"},{"title":"[2310.00429v5] On the Stability of Iterative Retraining of Generative Models on their own Data","url":"https://arxiv.org/abs/2310.00429v5"},{"title":"On the Stability of Iterative Retraining of Generative Models on their own Data | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/stability-iterative-retraining-generative-models-their-own"}]

I found the paper you're looking for! Here are the key details:

"On the Stability of Iterative Retraining of Generative Models on their own Data" was presented at the 2024 ICLR conference by Quentin Bertrand, Joey Bose, Alexandre Duplessis, Marco Jiralerspong, and Gauthier Gidel.

**Main Topic:**
The paper addresses what happens when a generative artificial intelligence model is trained using an increasing proportion of self-generated images.

**Key Findings:**
Iterative retrai
…[truncated 648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T10:56:42.718684+00:00_

Web search results for query: ""Spotting LLMs With Binoculars" Hans Schwarzschild Cherepanova ICML 2024 arxiv 2401.12070"

Links: [{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"Spotting LLMs with binoculars | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692768"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | OpenReview","url":"https://openreview.net/forum?id=iARAKITHTH"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | MPI-IS","url":"https://is.mpg.de/en/publications/hans_spotting_2024"},{"title":"Binoculars/README.md at main · ahans30/Binoculars","url":"https://github.com/ahans30/Binoculars/blob/main/README.md"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Safety- and Efficiency- aligned Learning – MPI-IS","url":"https://is.mpg.de/seal/publications/hans_spotting_2024"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://proceedings.mlr.press/v235/hans24a.html"},{"title":"[PDF] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Spotting-LLMs-With-Binoculars:-Zero-Shot-Detection-Hans-Schwarzschild/8dafb105a0cec1956443003eeea9fcf13c0ffa99"}]

I found relevant information about the paper you're searching for. Here's what I found:

## Paper Summary

"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" is authored by Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldste
…[truncated 1008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:56:42.718991+00:00_

Web search results for query: ""Detecting Pretraining Data from Large Language Models" Shi Ajith Xia ICLR 2024 Min-K%"

Links: [{"title":"[2310.16789] Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/abs/2310.16789"},{"title":"DETECTING PRETRAINING DATA FROM LARGE LANGUAGE MODELS - Princeton University","url":"https://collaborate.princeton.edu/en/publications/detecting-pretraining-data-from-large-language-models/"},{"title":"Detecting Pretraining Data from Large Language Models | OpenReview","url":"https://openreview.net/forum?id=zWqr3MQuNs"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/html/2310.16789v3"},{"title":"DETECTING PRETRAINING DATA FROM LARGE LAN","url":"https://openreview.net/pdf?id=zWqr3MQuNs"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://swj0419.github.io/detect-pretrain.github.io/"},{"title":"ICLR Poster Detecting Pretraining Data from Large Language Models","url":"https://iclr.cc/virtual/2024/poster/17381"},{"title":"GitHub - swj0419/detect-pretrain-code: This repository provides an original implementation of Detecting Pretraining Data from Large Language Models by *Weijia Shi, *Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu , Terra Blevins , Danqi Chen , Luke Zettlemoyer. · GitHub","url":"https://github.com/swj0419/detect-pretrain-code"},{"title":"Detecting Pretraining Data from Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231016789S/abstract"},{"title":"[PDF] Detecting Pretraining Data from Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Detecting-Pretraining-Data-from-Large-Language-Shi-Ajith/3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a"}]

I found the research paper you're looking for! Here are the key details:

**"Detecting Pretraining Data from Large Language Models"** is a paper by Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Bl
…[truncated 1469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T10:56:42.719262+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"GLTR\" Gehrmann Strobelt Rush ACL 2019 statistical detection generated text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"GLTR\" Gehrmann Strobelt Rush ACL 2019 statistical detection generated text"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T10:56:42.719463+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DetectGPT\" Mitchell Lee Khazatsky Manning Finn ICML 2023 zero-shot probability curvature"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DetectGPT\" Mitchell Lee Khazatsky Manning Finn ICML 2023 zero-shot probability curvature"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-26T10:56:42.719646+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Fast-DetectGPT\" Bao Zhao Teng Yang Zhang ICLR 2024 efficient zero-shot conditional probability curvature"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Fast-DetectGPT\" Bao Zhao Teng Yang Zhang ICLR 2024 efficient zero-shot conditional probability curvature"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T10:56:42.719818+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Intrinsic Dimension Estimation for Robust Detection\" Tulchinskii Kuznetsov Kushnareva NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Intrinsic Dimension Estimation for Robust Detection\" Tulchinskii Kuznetsov Kushnareva NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T10:56:42.720047+00:00_

Web search results for query: ""GLTR" Gehrmann Strobelt Rush ACL 2019 statistical detection generated text"

Links: [{"title":"GLTR: Statistical Detection and Visualization of Generated Text - ACL Anthology","url":"https://aclanthology.org/P19-3019/"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text | Sebastian Gehrmann","url":"https://scholar.harvard.edu/gehrmann/publications/gltr-statistical-detection-and-visualization-generated-text"},{"title":"[1906.04043] GLTR: Statistical Detection and Visualization of Generated Text","url":"https://arxiv.org/abs/1906.04043"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text","url":"https://scholar.harvard.edu/files/gehrmann/files/acl_demo_2019_gltr_statistical_detection_of_fake_text_5.pdf"},{"title":"GLTR: Statistical detection and visualization of generated text for ACL 2019 - IBM Research","url":"https://research.ibm.com/publications/gltr-statistical-detection-and-visualization-of-generated-text"},{"title":"[PDF] GLTR: Statistical Detection and Visualization of Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLTR:-Statistical-Detection-and-Visualization-of-Gehrmann-Strobelt/867db5097ad6aaef098c60b0845785b440eca49a"},{"title":"dblp: ACL 2019","url":"https://dblp.org/db/conf/acl/acl2019-3.html"},{"title":"GLTR: Statistical Detection and Visualization of Generated ...","url":"https://aclanthology.org/P19-3019.pdf"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190604043G/abstract"}]

I've found comprehensive information about GLTR. Here are the key details:

## Overview
GLTR: Statistical Detection and Visualization of Generated Text was presented by Sebastian Gehrmann, Hendrik Strobelt, and Alexander Rush at ACL 2019.

## Purpose and Function
GLTR is a tool to support humans in detecting whether a text was generated by a model. GLTR applies a suite of baseline sta
…[truncated 704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:56:42.720301+00:00_

Web search results for query: ""Fast-DetectGPT" Bao Zhao Teng Yang Zhang ICLR 2024 efficient zero-shot conditional probability curvature"

Links: [{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=Bpcgcr8E8Z"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text   via Conditional Probability Curvature","url":"https://arxiv.org/pdf/2310.05130"},{"title":"Guangsheng Bao","url":"https://baoguangsheng.github.io/"},{"title":"ICLR Poster Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://iclr.cc/virtual/2024/poster/19201"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/html/2310.05130v3"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Guangsheng+Bao,+Yanbin+Zhao,+Zhiyang+Teng,+Linyi+Yang,+and+Yue+Zhang.+2024.+Fast-DetectGPT:+Efficient+Zero-Shot+Detection+of+Machine-Generated+Text+via+Conditional+Probability+Curvature.+In+The+Twelfth+International+Conference+on+Learning+Representations.+https://openreview.net/forum?id%3DBpcgcr8E8Z"},{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"}]

I found the research for you! Here are the key details about the Fast-DetectGPT paper:

## Paper Overview

This is an ICLR 2024 paper titled "Fast-DetectGPT: Efficient Zero-Shot Det
…[truncated 1139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:56:42.720538+00:00_

Web search results for query: ""Intrinsic Dimension Estimation for Robust Detection" Tulchinskii Kuznetsov Kushnareva NeurIPS 2023"

Links: [{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/7baa48bc166aa2013d78cbdc15010530-Abstract-Conference.html"},{"title":"NeurIPS Poster Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://neurips.cc/virtual/2023/poster/72624"},{"title":"Intrinsic dimension estimation for robust detection of AI-generated texts | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667828"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/pdf/2306.04723"},{"title":"[2306.04723] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/abs/2306.04723"},{"title":"[PDF] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Intrinsic-Dimension-Estimation-for-Robust-Detection-Tulchinskii-Kuznetsov/a5fab19553e623e8787383cb3da76b8a3c42a8f4"},{"title":"(PDF) Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://www.researchgate.net/publication/371414255_Intrinsic_Dimension_Estimation_for_Robust_Detection_of_AI-Generated_Texts"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts - Archive ouverte HAL","url":"https://hal.science/hal-04306453v1"}]

Based on the web search results, I found information about the paper you're looking for:

## Paper Details

"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" by Eduard Tulchinskii, Kristian Kuznetsov, Laida Kushnareva, Daniil Cherniavskii, Sergey Nikolenko, Evgeny Burnaev, Serguei Barannikov, and Irina Piontkovskaya 
…[truncated 1001 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-26T10:56:42.720802+00:00_

Web search results for query: ""DetectGPT" Mitchell Lee Khazatsky Manning Finn ICML 2023 zero-shot probability curvature"

Links: [{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"GitHub - eric-mitchell/detect-gpt: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature · GitHub","url":"https://github.com/eric-mitchell/detect-gpt"},{"title":"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn · DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://slideslive.com/39004346/detectgpt-zeroshot-machinegenerated-text-detection-using-probability-curvature"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"},{"title":"Google Académico","url":"https://scholar.google.com/scholar?q=Eric+Mitchell,+Yoonho+Lee,+Alexander+Khazatsky,+Christopher+D+Manning,+and+Chelsea+Finn.+2023.+DetectGPT:+Zero-Shot+Machine-Generated+Text+Detection+using+Probability+Curvature.+arXiv+preprint+arXiv:2301.11305+(2023)."},{"title":"ICML Oral DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://icml.cc/virtual/2023/oral/25525"},{"title":"[PDF] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature | Semantic Scholar","url":"https://www.semanticscholar.org/paper/9a7ac45eafe11ca003db3a300505f3b5c3f9009a"},{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"Googl
…[truncated 1629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T10:56:42.721063+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Watermark for Large Language Models\" Kirchenbauer Geiping Wen Katz Miers Goldstein ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Watermark for Large Language Models\" Kirchenbauer Geiping Wen Katz Miers Goldstein ICML 2023"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-26T10:56:42.721263+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan Kumar Balasubramanian Feizi arxiv 2303.11156"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan Kumar Balasubramanian Feizi arxiv 2303.11156"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T10:56:42.721456+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Authorship Attribution for Neural Text Generation\" Uchendu Le Shu Lee EMNLP 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Authorship Attribution for Neural Text Generation\" Uchendu Le Shu Lee EMNLP 2020"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-26T10:56:42.721710+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Ghostbuster\" Verma Fleisig Tomlin Klein NAACL 2024 detecting ghostwritten"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Ghostbuster\" Verma Fleisig Tomlin Klein NAACL 2024 detecting ghostwritten"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T10:56:42.722087+00:00_

Web search results for query: ""Can AI-Generated Text be Reliably Detected" Sadasivan Kumar Balasubramanian Feizi arxiv 2303.11156"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Paper page - Can AI-Generated Text be Reliably Detected?","url":"https://huggingface.co/papers/2303.11156"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://ar5iv.labs.arxiv.org/html/2303.11156"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[2303.11156v1] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v1"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2023"}]

I found the paper for you! Here are the key details about the research:

**Paper Title:** Can AI-Generated Text be Reliably Detected?

**Authors:** Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi

**Publication:** arXiv:2303.11156, submitted on March 17, 2023 (with the latest version updated January 17, 2025)

**Key Findings:** The paper shows that these detectors are not reliable in practical scenarios. More specifically, the paper introduces a recursive paraphrasing attack to stress test the robustness of AI text detectors in the presence of an attacker, and provides a theoretical framework connecting the AUROC of the best pos
…[truncated 478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T10:56:42.722394+00:00_

Web search results for query: ""Authorship Attribution for Neural Text Generation" Uchendu Le Shu Lee EMNLP 2020"

Links: [{"title":"Authorship Attribution for Neural Text Generation - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.673/"},{"title":"Authorship Attribution for Neural Text Generation | Request PDF","url":"https://www.researchgate.net/publication/347235360_Authorship_Attribution_for_Neural_Text_Generation"},{"title":"Authorship attribution for neural text generation - Penn State","url":"https://pure.psu.edu/en/publications/authorship-attribution-for-neural-text-generation"},{"title":"Authorship Attribution for Neural Text Generation.","url":"https://dblp.org/rec/conf/emnlp/UchenduLSL20.xml"},{"title":"[PDF] Authorship Attribution for Neural Text Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Authorship-Attribution-for-Neural-Text-Generation-Uchendu-Le/9da9cab545bd1534a8c953bb66e611243dcee24d"},{"title":"GitHub - AdaUchendu/Authorship-Attribution-for-Neural-Text-Generation · GitHub","url":"https://github.com/AdaUchendu/Authorship-Attribution-for-Neural-Text-Generation"},{"title":"Authorship Attribution for Neural Text Generation - researchr publication","url":"https://researchr.org/publication/UchenduLSL20"},{"title":"Papers with Code - Authorship Attribution for Neural Text Generation","url":"https://paperswithcode.com/paper/authorship-attribution-for-neural-text"}]

I found the paper you were looking for! Here are the search results:

"Authorship Attribution for Neural Text Generation" was published by Adaku Uchendu, Thai Le, Kai Shu, and Dongwon Lee at EMNLP 2020. It was published in the Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 8384–8395.

The work investigates the authorship attribution problem in three versions, and finds that most generators still generate texts significantly different from human-written ones, thereby making three problems easi
…[truncated 582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T10:56:42.722687+00:00_

Web search results for query: ""Ghostbuster" Verma Fleisig Tomlin Klein NAACL 2024 detecting ghostwritten"

Links: [{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.95/"},{"title":"[2305.15047] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047"},{"title":"Detecting Text Ghostwritten by Large Language Models","url":"https://aclanthology.org/2024.naacl-long.95.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma","url":"https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/html/2305.15047v3"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631441_Ghostbuster_Detecting_Text_Ghostwritten_by_Large_Language_Models"},{"title":"[2305.15047v1] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047v1"},{"title":"[PDF] Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Ghostbuster:-Detecting-Text-Ghostwritten-by-Large-Verma-Fleisig/fb467f368b9e196b32c90e3da7ae0986d59cd66f"},{"title":"Accepted Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/program/accepted_papers/"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230515047V/abstract"}]

I found the paper! Here are the key details about "Ghostbuster: Detecting Text Ghostwritten by Large Language Models":

**Authors and Publication:**
The paper was authored by Vivek Verma, Eve Fleisig, Nicholas Tomlin, and Dan Klein and was published at NAACL 2024.

**Core Method:**
The method works by passing do
…[truncated 967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-26T10:56:42.723007+00:00_

Web search results for query: ""A Watermark for Large Language Models" Kirchenbauer Geiping Wen Katz Miers Goldstein ICML 2023"

Links: [{"title":"A Watermark for Large Language Models","url":"https://proceedings.mlr.press/v202/kirchenbauer23a.html"},{"title":"[2301.10226] A Watermark for Large Language Models","url":"https://arxiv.org/abs/2301.10226"},{"title":"A Watermark for Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230110226K/abstract"},{"title":"[PDF] A Watermark for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Watermark-for-Large-Language-Models-Kirchenbauer-Geiping/cb5b71a622aff47014d4f28a958679629a8b6363"},{"title":"A Watermark for Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10522346-watermark-large-language-models"},{"title":"ICML Poster A Watermark for Large Language Models","url":"https://icml.cc/virtual/2023/poster/24544"},{"title":"A Watermark for Large Language Models","url":"https://arxiv.org/pdf/2301.10226"},{"title":"GitHub - jwkirchenbauer/lm-watermarking · GitHub","url":"https://github.com/jwkirchenbauer/lm-watermarking"},{"title":"dblp: A Watermark for Large Language Models.","url":"https://dblp.org/rec/conf/icml/KirchenbauerGWK23.html"},{"title":"A Watermark for Large Language Models","url":"https://bibbase.org/network/publication/kirchenbauer-geiping-wen-katz-miers-goldstein-awatermarkforlargelanguagemodels-2023"}]

I found the paper! Here's what I can tell you about it:

"A Watermark for Large Language Models" was authored by John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein and published in the Proceedings of the 40th International Conference on Machine Learning (ICML 2023), pages 17061-17084.

**Main Contribution:**
The paper proposes watermarking model output, which embeds signals into generated text that are invisible to humans but algorithmically detectable from a short span of
…[truncated 856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-26T10:56:42.723266+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Curious Case of Neural Text Degeneration\" Holtzman Buys Du Forbes Choi ICLR 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Curious Case of Neural Text Degeneration\" Holtzman Buys Du Forbes Choi ICLR 2020"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T10:56:42.723470+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Closing the Curious Case of Neural Text Degeneration\" Finlayson Hewitt Koller Swayamdipta Sabharwal ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Closing the Curious Case of Neural Text Degeneration\" Finlayson Hewitt Koller Swayamdipta Sabharwal ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-26T10:56:42.723667+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Decoding Decoded\" Garces Arias Li Heumann Assenmacher COLING 2025 hyperparameter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Decoding Decoded\" Garces Arias Li Heumann Assenmacher COLING 2025 hyperparameter"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-26T10:56:42.723860+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"On Decoding Strategies for Neural Text Generators\" Wiher Meister Cotterell TACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"On Decoding Strategies for Neural Text Generators\" Wiher Meister Cotterell TACL 2022"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T10:56:42.724144+00:00_

Web search results for query: ""Curious Case of Neural Text Degeneration" Holtzman Buys Du Forbes Choi ICLR 2020"

Links: [{"title":"[1904.09751] The Curious Case of Neural Text Degeneration","url":"https://arxiv.org/abs/1904.09751"},{"title":"The Curious Case of Neural Text Degeneration - UCT Computer Science Research Document Archive","url":"https://pubs.cs.uct.ac.za/id/eprint/1407/"},{"title":"[Paper Note] The Curious Case of Neural Text Degeneration, Ari Holtzman+, ICLR'20 · Issue #1889 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1889"},{"title":"CLOSING THE CURIOUS CASE OF NEURAL TEXT DEGENERATION Matthew Finlayson∗","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf"},{"title":"dblp: The Curious Case of Neural Text Degeneration.","url":"https://dblp.org/rec/conf/iclr/HoltzmanBDFC20.html"},{"title":"THE CURIOUS CASE OF NEURAL TEXT DeGENERATION","url":"https://openreview.net/pdf?id=rygGQyrFvH"},{"title":"The Curious Case of Neural Text Degeneration. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/229fdab5aeb4deb740ceb07a72a6e9058/albinzehe"},{"title":"[PDF] The Curious Case of Neural Text Degeneration | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Case-of-Neural-Text-Degeneration-Holtzman-Buys/cf4aa38ae31b43fd07abe13b4ffdb265babb7be1"},{"title":"The Curious Case of Neural Text Degeneration | ML Anthology","url":"https://mlanthology.org/iclr/2020/holtzman2020iclr-curious/"}]

I found the paper you were searching for! Here are the key findings:

**Paper Information:**
"The Curious Case of Neural Text Degeneration" was published by Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi at the International Conference on Learning Representations (ICLR) on April 26 - May 1, 2020.

**Main Contribution:**
The paper reveals that even though likelihood as a training objective leads to high-quality models for language 
…[truncated 737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T10:56:42.724450+00:00_

Web search results for query: ""Closing the Curious Case of Neural Text Degeneration" Finlayson Hewitt Koller Swayamdipta Sabharwal ICLR 2024"

Links: [{"title":"Closing the Curious Case of Neural Text Degeneration","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/34899013589ef41aea4d7b2f0ef310c1-Abstract-Conference.html"},{"title":"[2310.01693] Closing the Curious Case of Neural Text Degeneration","url":"https://arxiv.org/abs/2310.01693"},{"title":"Closing the Curious Case of Neural Text Degeneration | OpenReview","url":"https://openreview.net/forum?id=dONpC9GL1o"},{"title":"CLOSING THE CURIOUS CASE OF NEURAL TEXT DEGENERATION Matthew Finlayson∗","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf"},{"title":"[PDF] Closing the Curious Case of Neural Text Degeneration | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Closing-the-Curious-Case-of-Neural-Text-Finlayson-Hewitt/678a3cc761024b6daaf41ac4333f695358447a2f"},{"title":"ICLR Poster Closing the Curious Case of Neural Text Degeneration","url":"https://iclr.cc/virtual/2024/poster/18260"},{"title":"Closing the Curious Case of Neural Text Degeneration (ICLR 2024) [PAPER EXPLAINED] - YouTube","url":"https://www.youtube.com/watch?v=cUXrlXwxCUg"},{"title":"[PDF] The Curious Case of Neural Text Degeneration | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Case-of-Neural-Text-Degeneration-Holtzman-Buys/cf4aa38ae31b43fd07abe13b4ffdb265babb7be1"},{"title":"Closing the Curious Case of Neural Text Degeneration - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231001693F/abstract"},{"title":"Paper page - Closing the Curious Case of Neural Text Degeneration","url":"https://paperswithcode.com/paper/closing-the-curious-case-of-neural-text"}]

I found the paper! Here's what the search results show about "Closing the Curious Case of Neural Text Degeneration":

**Publication Details:**
The paper is part o
…[truncated 1329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T10:56:42.724748+00:00_

Web search results for query: ""Decoding Decoded" Garces Arias Li Heumann Assenmacher COLING 2025 hyperparameter"

Links: [{"title":"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.668/"},{"title":"GitHub - YecanLee/Decoding-Decoded: [COLING 2025] Official PyTorch Implementation of \"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\" · GitHub","url":"https://github.com/YecanLee/Decoding-Decoded"},{"title":"Understanding Hyperparameter Effects in Open-Ended ...","url":"https://aclanthology.org/2025.coling-main.668.pdf"},{"title":"[2410.06097v2] Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation","url":"https://arxiv.org/abs/2410.06097v2"},{"title":"[2410.06097] Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation","url":"https://arxiv.org/abs/2410.06097"},{"title":"dblp: Christian Heumann","url":"https://dblp.org/pid/10/8427.html"},{"title":"The Truncation Blind Spot: How Decoding Strategies Systematically Exclude Human-Like Token Choices","url":"https://arxiv.org/html/2603.18482"},{"title":"(PDF) Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation","url":"https://www.researchgate.net/publication/389215115_Decoding_Decoded_Understanding_Hyperparameter_Effects_in_Open-Ended_Text_Generation"},{"title":"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation","url":"https://arxiv.org/html/2410.06097v2"},{"title":"Decoding Decoded:","url":"https://arxiv.org/pdf/2410.06097"}]

I found the research paper you were looking for! Here's the information:

"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation" is a paper by Esteban Garces Arias, Meimingwei Li, Christian Heumann, and Matthias Assenmacher presented at COLING 2025.

The paper appears in the Proceedings of the 31st Interna
…[truncated 842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-26T10:56:42.725081+00:00_

Web search results for query: ""On Decoding Strategies for Neural Text Generators" Wiher Meister Cotterell TACL 2022"

Links: [{"title":"On Decoding Strategies for Neural Text Generators - ACL Anthology","url":"https://aclanthology.org/2022.tacl-1.58/"},{"title":"On Decoding Strategies for Neural Text Generators | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00502/113024/On-Decoding-Strategies-for-Neural-Text-Generators"},{"title":"On Decoding Strategies for Neural Text Generators | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/ojs/index.php/tacl/article/view/3807"},{"title":"On Decoding Strategies for Neural Text Generators","url":"https://direct.mit.edu/tacl/article-abstract/doi/10.1162/tacl_a_00502/113024"},{"title":"On Decoding Strategies for Neural Text Generators - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220315721W/abstract"},{"title":"(PDF) On Decoding Strategies for Neural Text Generators","url":"https://www.researchgate.net/publication/363744968_On_Decoding_Strategies_for_Neural_Text_Generators"},{"title":"On Decoding Strategies for Neural Text Generators","url":"https://www.mendeley.com/catalogue/6d004644-be9b-3691-98d6-c75ad76d6177/"},{"title":"@article{wiher-etal-2022-decoding,","url":"https://aclanthology.org/2022.tacl-1.58.bib"},{"title":"On Decoding Strategies for Neural Text Generators | Rycolab","url":"https://rycolab.io/publication/wiheral-tacl-22/"},{"title":"On Decoding Strategies for Neural Text Generators | Clara Meister","url":"https://cimeister.github.io/publication/wiheral-tacl-22/"}]

I found the paper! Here's the information about "On Decoding Strategies for Neural Text Generators":

**Citation Details:**
Gian Wiher, Clara Meister, and Ryan Cotterell published "On Decoding Strategies for Neural Text Generators" in Transactions of the Association for Computational Linguistics, Volume 10, pag
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T10:56:42.725351+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mirostat\" Basu Ramachandran Keskar Varshney ICLR 2021 neural text decoding perplexity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mirostat\" Basu Ramachandran Keskar Varshney ICLR 2021 neural text decoding perplexity"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T10:56:42.725551+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Rank Consistent Ordinal Regression for Neural Networks\" Cao Mirjalili Raschka Pattern Recognition Letters 2020 CORAL age estimation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Rank Consistent Ordinal Regression for Neural Networks\" Cao Mirjalili Raschka Pattern Recognition Letters 2020 CORAL age estimation"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-26T10:56:42.725763+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LoRA\" \"Low-Rank Adaptation of Large Language Models\" Hu Shen Wallis ICLR 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LoRA\" \"Low-Rank Adaptation of Large Language Models\" Hu Shen Wallis ICLR 2022"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-26T10:56:42.725987+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DeBERTaV3\" He Gao Chen ELECTRA gradient-disentangled ICLR 2023 arxiv 2111.09543"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DeBERTaV3\" He Gao Chen ELECTRA gradient-disentangled ICLR 2023 arxiv 2111.09543"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-26T10:56:42.726236+00:00_

Web search results for query: ""Rank Consistent Ordinal Regression for Neural Networks" Cao Mirjalili Raschka Pattern Recognition Letters 2020 CORAL age estimation"

Links: [{"title":"[1901.07884] Rank consistent ordinal regression for neural networks with application to age estimation","url":"https://arxiv.org/abs/1901.07884"},{"title":"Rank consistent ordinal regression for neural networks with application to age estimation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S016786552030413X"},{"title":"Deep neural networks for rank-consistent ordinal regression based on conditional probabilities | Pattern Analysis and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10044-023-01181-9"},{"title":"(PDF) Rank consistent ordinal regression for neural networks with application to age estimation","url":"https://www.researchgate.net/publication/347503290_Rank_consistent_ordinal_regression_for_neural_networks_with_application_to_age_estimation"},{"title":"Deep Neural Networks for Rank-Consistent Ordinal ...","url":"https://arxiv.org/pdf/2111.08851"},{"title":"Rank consistent ordinal regression for neural networks with ...","url":"https://sebastianraschka.com/pdf/papers/2020-coral.pdf"},{"title":"GitHub - Raschka-research-group/coral-cnn: Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation · GitHub","url":"https://github.com/Raschka-research-group/coral-cnn"},{"title":"Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities","url":"https://arxiv.org/html/2111.08851v5"},{"title":"GitHub - Raschka-research-group/coral-pytorch: CORAL and CORN implementations for ordinal regression with deep neural networks. · GitHub","url":"https://github.com/Raschka-research-group/coral-pytorch"}]

I found the research paper you're looking for! Here are the key details:

The paper "Rank Consistent Ordinal Regression for Neural Networks with Application to
…[truncated 1023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-26T10:56:42.726523+00:00_

Web search results for query: ""Mirostat" Basu Ramachandran Keskar Varshney ICLR 2021 neural text decoding perplexity"

Links: [{"title":"GitHub - basusourya/mirostat: Code for the paper-\"Mirostat: A Perplexity-Controlled Neural Text Decoding Algorithm\" (https://arxiv.org/abs/2007.14966). · GitHub","url":"https://github.com/basusourya/mirostat"},{"title":"MIROSTAT: A NEURAL TEXT DECODING ALGORITHM THAT DIRECTLY CONTROLS PERPLEXITY - Illinois Experts","url":"https://experts.illinois.edu/en/publications/mirostat-a-neural-text-decoding-algorithm-that-directly-controls-/"},{"title":"mirostat/README.md at master · basusourya/mirostat","url":"https://github.com/basusourya/mirostat/blob/master/README.md"},{"title":"Mirostat: A Neural Text Decoding Algorithm That Directly Controls Perplexity (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10276288"},{"title":"Published as a conference paper at ICLR 2021","url":"https://openreview.net/pdf?id=W1G1JZEIy5_"},{"title":"Salesforce Research at ICLR 2021 - Salesforce","url":"https://www.salesforce.com/blog/salesforce-research-at-iclr-2021/"},{"title":"ICLR Poster Mirostat: A Neural Text Decoding Algorithm That Directly Controls Perplexity","url":"https://iclr.cc/virtual/2021/poster/2700"},{"title":"Sourya Basu University of Illinois at Urbana-Champaign Mirostat:","url":"https://iclr.cc/media/Slides/iclr/2021/virtual(05-00-00)-05-00-00UTC-2700-mirostat_a_neu.pdf"},{"title":"Papers with Code - Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity","url":"https://paperswithcode.com/paper/mirostat-a-perplexity-controlled-neural-text"},{"title":"MIROSTAT: A NEURAL TEXT DECODING ALGORITHM THAT DIRECTLY CONTROLS PERPLEXITY | Request PDF","url":"https://www.researchgate.net/publication/352560296_MIROSTAT_A_NEURAL_TEXT_DECODING_ALGORITHM_THAT_DIRECTLY_CONTROLS_PERPLEXITY"}]

Based on the search results, here's what I found about Mirostat:

## Overview

Mirostat is a perplexity-controlled neural tex
…[truncated 1209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-26T10:56:42.726824+00:00_

Web search results for query: ""LoRA" "Low-Rank Adaptation of Large Language Models" Hu Shen Wallis ICLR 2022"

Links: [{"title":"LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/pdf/2106.09685"},{"title":"ICLR Poster LoRA: Low-Rank Adaptation of Large Language Models","url":"https://iclr.cc/virtual/2022/poster/6319"},{"title":"ICLR LoRAM: Low-Rank Adaptation of Large Language Models on Manifold","url":"https://iclr.cc/virtual/2025/33548"},{"title":"MiLoRA: Efficient Mixture of Low-Rank Adaptation for Large Language   Models Fine-tuning","url":"https://arxiv.org/pdf/2410.18035"},{"title":"OLoRA: Orthonormal Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/pdf/2406.01775"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/lora-low-rank-adaptation-of-large-language-models/"},{"title":"LoRA-FA: Memory-efficient Low-rank Adaptation for Large Language Models   Fine-tuning","url":"https://arxiv.org/pdf/2308.03303"},{"title":"Expressive and Generalizable Low-rank Adaptation for Large Models via   Slow Cascaded Learning","url":"https://arxiv.org/pdf/2407.01491"},{"title":"Brief Review — LoRA: Low-Rank Adaptation of Large Language Models | by Sik-Ho Tsang | Medium","url":"https://sh-tsang.medium.com/brief-review-lora-low-rank-adaptation-of-large-language-models-faf5ddd5802f"}]

Based on the search results, here's what I found about LoRA:

## LoRA: Low-Rank Adaptation of Large Language Models

LoRA freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks.

The paper was published at ICLR 2022 in April 2022. The research was conducted by researchers at Microsoft (as referenced in multiple sources mentioning "Hu et al.").

### Key Results

Compared to GPT-3 175B fine-tuned with Adam, LoR
…[truncated 739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-26T10:56:42.727141+00:00_

Web search results for query: ""DeBERTaV3" He Gao Chen ELECTRA gradient-disentangled ICLR 2023 arxiv 2111.09543"

Links: [{"title":"[2111.09543] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543"},{"title":"[2111.09543v4] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543v4"},{"title":"[2111.09543v1] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543v1"},{"title":"[2111.09543v2] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543v2"},{"title":"[2111.09543] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://ar5iv.labs.arxiv.org/html/2111.09543"},{"title":"[PDF] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeBERTaV3:-Improving-DeBERTa-using-ELECTRA-Style-He-Gao/972706306f85b1bfb40c7d35c796ad5174eb0c9c"},{"title":"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv211109543H/abstract"},{"title":"GitHub - microsoft/DeBERTa: The implementation of DeBERTa · GitHub","url":"https://github.com/microsoft/DeBERTa"}]

I found the paper! Here's what I can tell you about it:

DeBERTaV3 improves the original DeBERTa model by replacing mask language modeling (MLM) with replaced token detection (RTD), a more sample-efficient pre-training task.

The key innovation addresses a problem with vanilla embedding sharing in ELECTRA-style pre-training: vanilla embedding sharing in ELECTRA hurts training e
…[truncated 715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-26T10:56:42.727414+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"RoBERTa: A Robustly Optimized BERT Pretraining\" Liu Ott Goyal arxiv 1907.11692"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"RoBERTa: A Robustly Optimized BERT Pretraining\" Liu Ott Goyal arxiv 1907.11692"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-26T10:56:42.727614+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Qwen2.5 Technical Report\" Qwen Team arxiv 2412.15115"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Qwen2.5 Technical Report\" Qwen Team arxiv 2412.15115"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-26T10:56:42.727807+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Llama 3 Herd of Models\" Grattafiori 2024 arxiv 2407.21783"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Llama 3 Herd of Models\" Grattafiori 2024 arxiv 2407.21783"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-26T10:56:42.728018+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Extracting Training Data from Large Language Models\" Carlini Tramer Wallace USENIX Security 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Extracting Training Data from Large Language Models\" Carlini Tramer Wallace USENIX Security 2021"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-26T10:56:42.728277+00:00_

Web search results for query: ""RoBERTa: A Robustly Optimized BERT Pretraining" Liu Ott Goyal arxiv 1907.11692"

Links: [{"title":"[1907.11692] RoBERTa: A Robustly Optimized BERT Pretraining Approach","url":"https://arxiv.org/abs/1907.11692"},{"title":"arXiv:1907.11692v1 [cs.CL] 26 Jul 2019","url":"https://arxiv.org/pdf/1907.11692"},{"title":"RoBERTa: A Robustly Optimized BERT Pretraining Approach | OpenReview","url":"https://openreview.net/forum?id=SyxS0T4tvS"},{"title":"RoBERTa: A Robustly Optimized BERT Pretraining Approach","url":"https://www.researchgate.net/publication/334735779_RoBERTa_A_Robustly_Optimized_BERT_Pretraining_Approach"},{"title":"Paper page - RoBERTa: A Robustly Optimized BERT Pretraining Approach","url":"https://huggingface.co/papers/1907.11692"},{"title":"[1907.11692v1] RoBERTa: A Robustly Optimized BERT Pretraining Approach","url":"https://arxiv.org/abs/1907.11692v1"},{"title":"[PDF] RoBERTa: A Robustly Optimized BERT Pretraining Approach | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RoBERTa:-A-Robustly-Optimized-BERT-Pretraining-Liu-Ott/077f8329a7b6fa3b7c877a57b81eb6c18b5f87de"},{"title":"dblp: RoBERTa: A Robustly Optimized BERT Pretraining Approach.","url":"https://dblp.org/rec/journals/corr/abs-1907-11692.html"},{"title":"RoBERTa: A Robustly Optimized BERT Pretraining Approach","url":"https://oa.mg/work/10.48550/arxiv.1907.11692"},{"title":"RoBERTa: A Robustly Optimized BERT Pretraining Approach | Paper2Cod…","url":"https://www.opentrain.ai/papers/roberta-a-robustly-optimized-bert-pretraining-approach--arxiv-1907.11692/"}]

I found the paper you were searching for. Here are the key details:

**Title:** RoBERTa: A Robustly Optimized BERT Pretraining Approach

**Authors:** Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov

**ArXiv ID:** 1907.11692

**Published:** July 26, 2019

**Summary:** The paper presents a replication study of BERT pr
…[truncated 557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-26T10:56:42.728576+00:00_

Web search results for query: ""Qwen2.5 Technical Report" Qwen Team arxiv 2412.15115"

Links: [{"title":"[2412.15115] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Paper page - Qwen2.5 Technical Report","url":"https://huggingface.co/papers/2412.15115"},{"title":"Qwen2.5 Technical Report","url":"https://bibbase.org/network/publication/qwen-yang-yang-zhang-hui-zheng-yu-li-etal-qwen25technicalreport-2025"},{"title":"[PDF] Qwen2.5 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Qwen2.5-Technical-Report-Yang-Yang/88aa6b1f37d1fd8e0a40499ce9bb87873f03aaa8"},{"title":"[2412.15115v1] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115v1"},{"title":"2024-12-20 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115v1"},{"title":"Qwen2.5-Max: Exploring the Intelligence of Large-scale MoE Model | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-max/"},{"title":"dblp: Qwen2.5 Technical Report.","url":"https://dblp.org/rec/journals/corr/abs-2412-15115.html"}]

I found the paper! Here's what the search results show about the Qwen2.5 Technical Report (arxiv 2412.15115):

**Overview:**
Qwen2.5 is a comprehensive series of large language models (LLMs) designed to meet diverse needs, authored by Qwen team with An Yang as the first listed author and 41 other contributors.

**Key Details:**

- **Model Sizes:** The open-weight release includes pre-trained and instruction-tuned models of 7 sizes: 0.5B, 1.5B, 3B, 7B, 14B, 32B, and 72B, available in bfloat16 precision and quantized versions in different precisions.

- **Pre-training Scale:** High-quality pre-training datasets have been scaled from the previous 7 trillion tokens to 18 trillion tokens.

- **Publication:** The paper was submitted on December 19, 2024, and last revised on Jan
…[truncated 411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T10:56:42.728869+00:00_

Web search results for query: ""Extracting Training Data from Large Language Models" Carlini Tramer Wallace USENIX Security 2021"

Links: [{"title":"Extracting Training Data from Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting"},{"title":"Extracting Training Data from Large Language Models","url":"https://www.usenix.org/system/files/sec21-carlini-extracting.pdf"},{"title":"Extracting Training Data from Large Language Models - researchr publication","url":"https://researchr.org/publication/CarliniTWJHLRBS21"},{"title":"Extracting Training Data from Large Language Models","url":"https://ryanzhumich.github.io/cse587/slides_extract_data.pdf"},{"title":"Papers | Nicholas Carlini","url":"https://nicholas.carlini.com/papers"},{"title":"Extracting training data from diffusion models | Proceedings of the 32nd USENIX Conference on Security Symposium","url":"https://dl.acm.org/doi/10.5555/3620237.3620531"},{"title":"Extracting Training Data from Large Language Models | by Soumyendra Shrivastava | Medium","url":"https://medium.com/@shrivastavasoumyendra/extracting-training-data-from-large-language-models-18604e6e41a2"},{"title":"2021-09-21: Nicholas Carlini - Extracting Training Data from Large Language Models: Institut: ITS","url":"https://www.its.uni-luebeck.de/forschung/forschungsseminar/2021-09-21-nicholas-carlini-extracting-training-data-from-large-language-models"},{"title":"GitHub - ftramer/LM_Memorization: Training data extraction on GPT-2 · GitHub","url":"https://github.com/ftramer/LM_Memorization"},{"title":"[2012.07805] Extracting Training Data from Large Language Models","url":"https://arxiv.org/abs/2012.07805"}]

I found comprehensive information about the paper you're looking for. Here's what I discovered:

## Paper Details

The paper "Extracting Training Data from Large Language Models" was authored by Nicholas Carlini (Google), Florian Tramèr (Stanford University), Eric Wallace (UC Berkele
…[truncated 1301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-26T10:56:42.729177+00:00_

Web search results for query: ""Llama 3 Herd of Models" Grattafiori 2024 arxiv 2407.21783"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"},{"title":"The Llama 3 Herd of Models. Paper Review | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/the-llama-3-herd-of-models-2f62252ce1c8"}]

I found the paper you're looking for! Here are the key details about "The Llama 3 Herd of Models":

**Paper Information:**
- ArXiv ID: 2407.21783, submitted on July 31, 2024, with the latest version (v3) revised on November 23, 2024
- Lead author: Aaron Grattafiori (with 558 other authors)

**Paper Summary:**
The paper presents Llama 3, a new set of foundation models consisting of a herd of language models that natively support multilinguality, coding, reasoning, and tool usage.

**Key Technical Details:**
- The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.
- Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks.
- Meta publicly released Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and Llama Guard 3 model for input and output safety.
- The paper also presents experiments integrating image, video, and speech capabilities into Llama 
…[truncated 201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-26T10:56:42.729415+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Datamodels\" Ilyas Park Engstrom Leclerc Madry ICML 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Datamodels\" Ilyas Park Engstrom Leclerc Madry ICML 2022"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-26T10:56:42.729613+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Undetectable Watermarks for Language Models\" Christ Gunn Zamir COLT 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Undetectable Watermarks for Language Models\" Christ Gunn Zamir COLT 2024"
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-26T10:56:42.729829+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Simple Approach to Ordinal Classification\" Frank Hall ECML 2001"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Simple Approach to Ordinal Classification\" Frank Hall ECML 2001"
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T10:56:42.730055+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Loss Functions for Preference Levels\" Rennie Srebro IJCAI 2005 ordered labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Loss Functions for Preference Levels\" Rennie Srebro IJCAI 2005 ordered labels"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-26T10:56:42.730307+00:00_

Web search results for query: ""Undetectable Watermarks for Language Models" Christ Gunn Zamir COLT 2024"

Links: [{"title":"Undetectable Watermarks for Language Models","url":"https://proceedings.mlr.press/v247/christ24a.html"},{"title":"COLT 2024: Undetectable Watermarks for Language Models","url":"https://learningtheory.org/colt2024/schedule/poster_156.html"},{"title":"[CGZ24] Undetectable watermarks for language models [ ...","url":"https://people.eecs.berkeley.edu/~gunn/images/water-summaries.pdf"},{"title":"[2306.09194] Undetectable Watermarks for Language Models","url":"https://arxiv.org/abs/2306.09194"},{"title":"[PDF] Undetectable Watermarks for Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Undetectable-Watermarks-for-Language-Models-Christ-Gunn/7baae1691bc8c4012f2193e174de94c228afa8f8"},{"title":"Undetectable Watermarks for Language Models","url":"https://www.cs.columbia.edu/~mchrist/Watermarks-with-comp.pdf"},{"title":"Two Halves Make a Whole: How to Reconcile Soundness and ...","url":"https://eprint.iacr.org/2024/2062.pdf"},{"title":"(PDF) Undetectable Watermarks for Language Models","url":"https://www.researchgate.net/publication/371605498_Undetectable_Watermarks_for_Language_Models"},{"title":"Undetectable Watermarks for Language Models Miranda Christ∗","url":"https://eprint.iacr.org/2023/763.pdf"}]

I found the research paper you're looking for! Here are the key details:

**Paper Title:** Undetectable Watermarks for Language Models

**Authors:** Miranda Christ, Sam Gunn, Or Zamir

**Publication:** Proceedings of Thirty Seventh Conference on Learning Theory, PMLR 247:1125-1139, 2024

**Main Contribution:** The paper introduces a cryptographically-inspired notion of undetectable watermarks for language models—asking whether it's possible to introduce a watermark without incurring any detectable change to the output distribution.

**Key Concept:** Watermarks can be detected only with the knowledge of a secret key; witho
…[truncated 457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-26T10:56:42.730600+00:00_

Web search results for query: ""Datamodels" Ilyas Park Engstrom Leclerc Madry ICML 2022"

Links: [{"title":"GitHub - MadryLab/datamodels","url":"https://github.com/MadryLab/datamodels"},{"title":"[2202.00622] Datamodels: Predicting Predictions from Training Data","url":"https://arxiv.org/abs/2202.00622"},{"title":"Datamodels: Predicting Predictions from Training Data","url":"https://proceedings.mlr.press/v162/ilyas22a/ilyas22a.pdf"},{"title":"Datamodels Predicting Predictions with Training Data @andrew_ilyas","url":"https://icml.cc/media/icml-2022/Slides/16972.pdf"},{"title":"ICML Poster Datamodels: Understanding Predictions with Data and Data with Predictions","url":"https://icml.cc/virtual/2022/poster/16971"},{"title":"datamodels/README.md at main · MadryLab/datamodels","url":"https://github.com/MadryLab/datamodels/blob/main/README.md"},{"title":"Datamodels: Understanding Predictions with Data and Data with Predictions","url":"https://proceedings.mlr.press/v162/ilyas22a.html"},{"title":"ICML 2022","url":"https://icml.cc/Conferences/2022/ScheduleMultitrack?event=17124"},{"title":"GitHub - MadryLab/datamodels-data: Data for \"Datamodels: Predicting Predictions with Training Data\"","url":"https://github.com/MadryLab/datamodels-data"},{"title":"Track: Deep Learning/Optimization","url":"https://icml.cc/virtual/2022/session/20101"}]

I found comprehensive information about the "Datamodels" paper from ICML 2022. Here's what I found:

## Paper Overview

The paper "Datamodels: Predicting Predictions from Training Data" was authored by Andrew Ilyas, Sung Min Park, Logan Engstrom, Guillaume Leclerc, and Aleksander Madry and published at ICML 2022.

## Core Concept

The paper presents a conceptual framework called datamodeling for analyzing the behavior of a model class in terms of the training data. A datamodel is a parameterized function that, for any subset of training data—using only information about which examples are contained in that subset—predicts the outcome of tr
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-26T10:56:42.730920+00:00_

Web search results for query: ""Simple Approach to Ordinal Classification" Frank Hall ECML 2001"

Links: [{"title":"A Simple Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/3-540-44795-4_13"},{"title":"A Simple Approach to Ordinal Classiﬁcation Eibe Frank and Mark Hall","url":"https://link.springer.com/content/pdf/10.1007/3-540-44795-4_13.pdf"},{"title":"[PDF] A Simple Approach to Ordinal Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Simple-Approach-to-Ordinal-Classification-Frank-Hall/76fc26939d73c565431e1f38107a4245e739284e"},{"title":"(PDF) A Simple Approach to Ordinal Classification","url":"https://www.researchgate.net/publication/226877154_A_Simple_Approach_to_Ordinal_Classification"},{"title":"(PDF) A Simple Approach to Ordinal Classification (2001) | Eibe Frank | 655 Citations","url":"https://scispace.com/papers/a-simple-approach-to-ordinal-classification-2mjbzk39ox"},{"title":"A simple approach to ordinal classification.","url":"https://researchcommons.waikato.ac.nz/items/ce0009f5-92fa-4113-b8b2-7ac929cfd32c"},{"title":"A simple approach to ordinal classification | Proceedings of the 12th European Conference on Machine Learning","url":"https://dl.acm.org/doi/10.1007/3-540-44795-4_13"},{"title":"Classification of Ordinal Data Using Neural Networks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/11564096_70"},{"title":"An Improved Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-662-45652-1_4"}]

I found the paper you're looking for! Here are the details:

**"A Simple Approach to Ordinal Classification"** by Frank, E., and Hall, M. (2001), published in Machine Learning: ECML 2001.

**About the paper:**

The paper addresses a key problem in machine learning: while classification methods commonly assume unordered class values, many practical applications have class values that ex
…[truncated 620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-26T10:56:42.731224+00:00_

Web search results for query: ""Loss Functions for Preference Levels" Rennie Srebro IJCAI 2005 ordered labels"

Links: [{"title":"Loss Functions for Preference Levels: Regression with Discrete Ordered Labels","url":"https://bibbase.org/network/publication/rennie-srebro-lossfunctionsforpreferencelevelsregressionwithdiscreteorderedlabels-2005"},{"title":"(PDF) Loss functions for preference levels: Regression with discrete ordered labels","url":"https://www.researchgate.net/publication/228633527_Loss_functions_for_preference_levels_Regression_with_discrete_ordered_labels"},{"title":"Loss Functions for Preference Levels: Regression with Discrete Ordered Labels","url":"https://home.ttic.edu/~nati/Publications/IJCAI05slides"},{"title":"Loss Functions for Preference Levels: Regression with Discrete Ordered Labels","url":"https://www.linkedin.com/pulse/loss-functions-preference-levels-regression-discrete-diego"},{"title":"API reference — mord 0.3 documentation","url":"https://pythonhosted.org/mord/reference.html"},{"title":"Jason Rennie's publications page","url":"http://qwone.com/~jason/papers/"},{"title":"Loss Function (All-Threshold Loss) for ordinal response variables HistGradientBoosting · Issue #16694 · scikit-learn/scikit-learn","url":"https://github.com/scikit-learn/scikit-learn/issues/16694"},{"title":"Beyond Binary Preferences: A Principled Framework for Reward Modeling with Ordinal Feedback","url":"https://arxiv.org/html/2603.02232"},{"title":"Jason Rennie's Resume - People - MIT","url":"https://people.csail.mit.edu/jrennie/cv.html"}]

Based on the search results, I found detailed information about the paper you're looking for:

## Publication Details

"Loss Functions for Preference Levels: Regression with Discrete Ordered Labels" by Rennie and Srebro was published in the Proceedings of the IJCAI Multidisciplinary Workshop on Advances in Preference Handling, 2005.

## Overview

The work casts the problem as a regression problem with discrete ordered labels and mo
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-26T10:56:42.731468+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Regression Models for Ordinal Data\" McCullagh 1980 JRSS Series B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Regression Models for Ordinal Data\" McCullagh 1980 JRSS Series B"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-26T10:56:42.731672+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Conditional variable importance for random forests\" Strobl Boulesteix Kneib Augustin Zeileis BMC Bioinformatics 2008"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Conditional variable importance for random forests\" Strobl Boulesteix Kneib Augustin Zeileis BMC Bioinformatics 2008"
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-26T10:56:42.731861+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Unrestricted Permutation forces Extrapolation\" Hooker Mentch Zhou Statistics Computing 2021 variable importance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Unrestricted Permutation forces Extrapolation\" Hooker Mentch Zhou Statistics Computing 2021 variable importance"
  }
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-26T10:56:42.732086+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Applied Logistic Regression\" Hosmer Lemeshow Wiley book second edition 2000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Applied Logistic Regression\" Hosmer Lemeshow Wiley book second edition 2000"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-26T10:56:42.732344+00:00_

Web search results for query: ""Regression Models for Ordinal Data" McCullagh 1980 JRSS Series B"

Links: [{"title":"Regression Models for Ordinal Data - McCullagh - 1980 - Journal of the Royal Statistical Society: Series B (Methodological) - Wiley Online Library","url":"https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1980.tb01109.x"},{"title":"Regression Models for Ordinal Data | Journal of the Royal Statistical Society Series B: Statistical Methodology | Oxford Academic","url":"https://academic.oup.com/jrsssb/article/42/2/109/7027621"},{"title":"McCullagh, P. (1980) Regression Models for Ordinal Data (with Discussion). Journal of the Royal Statistical Society Series B, 42, 109-142. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/ReferencesPapers?ReferenceID=2153795"},{"title":"McCullagh, P. (1980) Regression Models for Ordinal Data. Journal of the Royal Statistical Society. Series B (Methodological), 42, 109-142. - References - Scientific Research Publishing","url":"https://www.scirp.org/(S(i43dyn45teexjx-455qlt3d2q))/reference/referencespapers?referenceid=2361645"},{"title":"Regression Models for Ordinal Data","url":"https://cran.r-project.org/web/packages/ordinal/ordinal.pdf"},{"title":"Tests of significance using regression models for ordered categorical data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/3567291/"},{"title":"Regression Models for Ordinal Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Regression-Models-for-Ordinal-Data-McCullagh/0c86d2393b781941d178bf2bc2709ff4b3db90dd"},{"title":"A constrained regression model for an ordinal response with ordinal   predictors","url":"https://arxiv.org/pdf/1804.08715"},{"title":"McCullagh, P. (1980) Regression Models for Ordinal Data. ...","url":"https://www.scirp.org/reference/referencespapers"},{"title":"A new specification of generalized linear models for categorical data","url":"https://arxiv.org/pdf/1404.7331"}]

I found the paper y
…[truncated 1018 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-26T10:56:42.732646+00:00_

Web search results for query: ""Conditional variable importance for random forests" Strobl Boulesteix Kneib Augustin Zeileis BMC Bioinformatics 2008"

Links: [{"title":"Conditional variable importance for random forests | BMC Bioinformatics | Springer Nature Link","url":"https://link.springer.com/article/10.1186/1471-2105-9-307"},{"title":"Conditional variable importance for random forests - PMC - NIH","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC2491635/"},{"title":"(PDF) Conditional Variable Importance for Random Forests","url":"https://www.researchgate.net/publication/5231126_Conditional_Variable_Importance_for_Random_Forests"},{"title":"Conditional Variable Importance for Random Forests - WU Vienna University of Economics and Business","url":"https://research.wu.ac.at/en/publications/conditional-variable-importance-for-random-forests-3/"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Conditional+variable+importance+for+random+forests&amp=&author=C.+Strobl&amp=&author=A.-L.+Boulesteix&amp=&author=T.+Kneib&amp=&author=T.+Augustin&amp=&author=A.+Zeileis&amp=&publication_year=2008&amp=&journal=BMC+Bioinformatics&amp=&volume=9&amp=&pages=307"},{"title":"C. Strobl, A. L. Boulesteix, T. Kneib, T. Augustin and A. Zeileis, “Conditional Variable Importance for Random Forests,” BMC Bioinformatics, Vol. 9, Article 307, 2008. doi10.1186/1471-2105-9-307 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=244582"},{"title":"Strobl, C., Boulesteix, A.L., Kneib, T., Augustin, T. and Zeileis, A. (2008) Conditional Variable Importance for Random Forests. BMC Bioinformatics, 9, 307. - References - Scientific Research Publishing","url":"https://www.scirp.org/(S(351jmbntvnsjt1aadkposzje))/reference/ReferencesPapers.aspx?ReferenceID=1904998"},{"title":"Conditional variable importance for random forests - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/18620558/?dopt=Abstract"}]

I found
…[truncated 1064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-26T10:56:42.732961+00:00_

Web search results for query: ""Applied Logistic Regression" Hosmer Lemeshow Wiley book second edition 2000"

Links: [{"title":"Hosmer D.W. and Lemeshow, S. (2000) Applied Logistic Regression. 2nd Edition, Wiley, New York. https//doi.org/10.1002/0471722146 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2603462"},{"title":"3. Applied Logistic Regression. 2nd edn. David W. Hosmer and Stanley Lemeshow. Wiley, New York, 2000. No. of pages: xii+373. Price: �60.95. ISBN 0-471-35632-8 | Request PDF","url":"https://www.researchgate.net/publication/246197970_3_Applied_Logistic_Regression_2nd_edn_David_W_Hosmer_and_Stanley_Lemeshow_Wiley_New_York_2000_No_of_pages_xii373_Price_6095_ISBN_0-471-35632-8"},{"title":"Hosmer Jr., D.W and Lemeshow, S. (2000) Applied logistic regression. 2nd Edition, John Wiley & Sons, Inc., New York. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=959519"},{"title":"3. Applied Logistic Regression. 2nd edn. David W. Hosmer and Stanley Lemeshow. Wiley, New York, 2000. No. of pages: xii+373. Price: £60.95. ISBN 0‐471‐35632‐8 - Andersen - 2002 - Statistics in Medicine - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/sim.1236"},{"title":"Applied Logistic Regression - David W. Hosmer, Jr., Stanley Lemeshow - Google Books","url":"https://books.google.com/books/about/Applied_Logistic_Regression.html?id=Po0RLQ7USIMC"},{"title":"Hosmer. D.W. and Lemeshow, S. (2000) Applied Logistic Regression. 2nd Edition, John Wiley and Sons, New York, Chapter 5, 160-164. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2312845"},{"title":"Applied Logistic Regression","url":"https://onlinelibrary.wiley.com/doi/chapter-epub/10.1002/9781118548387.fmatter"},{"title":"Applied Logistic Regression","url":"https://ndl.ethernet.edu.et/bitstream/123456789/28462/
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-26T10:56:42.733276+00:00_

Web search results for query: ""Unrestricted Permutation forces Extrapolation" Hooker Mentch Zhou Statistics Computing 2021 variable importance"

Links: [{"title":"[1905.03151] Unrestricted Permutation forces Extrapolation: Variable Importance Requires at least One More Model, or There Is No Free Variable Importance","url":"https://arxiv.org/abs/1905.03151"},{"title":"Unrestricted permutation forces extrapolation: variable importance requires at least one more model, or there is no free variable importance - The Australian National University","url":"https://researchportalplus.anu.edu.au/en/publications/unrestricted-permutation-forces-extrapolation-variable-importance/"},{"title":"(PDF) Unrestricted permutation forces extrapolation: variable importance requires at least one more model, or there is no free variable importance","url":"https://www.researchgate.net/publication/355755411_Unrestricted_permutation_forces_extrapolation_variable_importance_requires_at_least_one_more_model_or_there_is_no_free_variable_importance"},{"title":"Unrestricted permutation forces extrapolation: variable importance requires at least one more model, or there is no free variable importance | Statistics and Computing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11222-021-10057-z"},{"title":"Unrestricted permutation forces extrapolation: variable importance requires at least one more model, or there is no free variable importance","url":"https://www.mendeley.com/catalogue/add75fb7-c217-3d2c-ae41-bc7b85d5545c/"},{"title":"Unrestricted Permutation forces Extrapolation: Variable Importance Requires at least One More Model, or There Is No Free Variable Importance - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190503151H/abstract"},{"title":"[1905.03151v2] Unrestricted Permutation forces Extrapolation: Variable Importance Requires at least One More Model, or There Is No Free Variable Importance","url":"https://arxiv.org/abs/1905.03151v2"},{"title":"Statis
…[truncated 2381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-26T10:56:42.733545+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"AI models collapse when trained on recursively generated data\" Shumailov Nature 2024 631 pages 755"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"AI models collapse when trained on recursively generated data\" Shumailov Nature 2024 631 pages 755"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-26T10:56:42.733764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "McCullagh \"Regression Models for Ordinal Data\" 1980 pages 109 142 discussion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "McCullagh \"Regression Models for Ordinal Data\" 1980 pages 109 142 discussion"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-26T10:56:42.733982+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Bertrand\" \"Iterative Retraining\" \"Spotlight\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Bertrand\" \"Iterative Retraining\" \"Spotlight\" ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-26T10:56:42.734250+00:00_

Web search results for query: "McCullagh "Regression Models for Ordinal Data" 1980 pages 109 142 discussion"

Links: [{"title":"Regression Models for Ordinal Data - Peter McCullagh","url":"https://www.stat.uchicago.edu/~pmcc/pubs/paper2.pdf"},{"title":"Regression Models for Ordinal Data","url":"https://cran.r-project.org/web/packages/ordinal/ordinal.pdf"},{"title":"Regression Models for Ordinal Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Regression-Models-for-Ordinal-Data-McCullagh/0c86d2393b781941d178bf2bc2709ff4b3db90dd"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Regression+models+for+ordinal+data&amp=&author=P.+McCullagh&amp=&publication_year=1980&amp=&journal=Journal+of+the+Royal+Statistical+Society,+Series+B+(Methodological)&amp=&pages=109-142&amp=&doi=10.1111/j.2517-6161.1980.tb01109.x"},{"title":"Regression Models for Ordinal Data - McCullagh - 1980 - Journal of the Royal Statistical Society: Series B (Methodological) - Wiley Online Library","url":"https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1980.tb01109.x"},{"title":"McCullagh, P. (1980) Regression Models for Ordinal Data. Journal of the Royal Statistical Society. Series B (Methodological), 42, 109-142. - References - Scientific Research Publishing","url":"https://www.scirp.org/(S(i43dyn45teexjx-455qlt3d2q))/reference/referencespapers?referenceid=2361645"},{"title":"Tests of significance using regression models for ordered categorical data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/3567291/"},{"title":"P. McCullagh, “Regression Models for Ordinal Data,” Journal of Royal Statistical Society, Vol. 42, No. 2, 1980, pp. 109-142. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=357234"},{"title":"Regression Models for Ordinal Data | Journal of the Royal Statistical Society Series B: Statistical Methodology | Oxford Academic","url":"https://academic.oup.com/jrsssb
…[truncated 1236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-26T10:56:42.734540+00:00_

Web search results for query: ""AI models collapse when trained on recursively generated data" Shumailov Nature 2024 631 pages 755"

Links: [{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"},{"title":"[PDF] AI models collapse when trained on recursively generated data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AI-models-collapse-when-trained-on-recursively-data-Shumailov-Shumaylov/603d3f90fc40f79ff51258f0295de3ec5107f73e"},{"title":"A note on “AI models collapse when trained on recursively generated data” | by Ali Borji | Medium","url":"https://medium.com/@aliborji/a-note-on-ai-models-collapse-when-trained-on-recursively-generated-data-5bee1de1ab87"},{"title":"AI models collapse when trained on recursively generated data","url":"https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/pdf/2410.12954"},{"title":"(PDF) AI models collapse when trained on recursively generated data","url":"https://www.researchgate.net/publication/382526401_AI_models_collapse_when_trained_on_recursively_generated_data"}]

I found the paper you're looking for. Here's what the search results show:

The paper "AI models collapse when trained on recursively generated data" by Shumailov et al. was published in Nature, volume 631, pages 755-759 (2024).

The research shows that indiscriminately 
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-26T10:56:42.734836+00:00_

Web search results for query: ""Bertrand" "Iterative Retraining" "Spotlight" ICLR 2024"

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=JORAfH2xFd"},{"title":"On the Stability of Iterative Retraining of Generative Models on their own Data","url":"https://iclr.cc/media/iclr-2024/Slides/18942.pdf"},{"title":"Quentin BERTRAND - Home","url":"https://qb3.github.io/index.html"},{"title":"On the Stability of Iterative Retraining of Generative Models ...","url":"https://arxiv.org/pdf/2310.00429"},{"title":"GitHub - QB3/gen_models_dont_go_mad: Code to reproduce the experiments of the ICLR 2024 (spotlight) paper \"On the Stability of Iterative Retraining of Generative Models on their Own Data\" https://arxiv.org/abs/2310.00429","url":"https://github.com/qb3/gen_models_dont_go_mad"},{"title":"QB3 (Quentin Bertrand) · GitHub","url":"https://github.com/QB3"},{"title":"Downloads 2024","url":"https://iclr.cc/Downloads/2024"},{"title":"ICLR 2024 Spotlights","url":"https://iclr.cc/virtual/2024/events/Spotlight"},{"title":"GitHub - ANLGBOY/ICLR-2024-OpenReview-Ratings · GitHub","url":"https://github.com/ANLGBOY/ICLR-2024-OpenReview-Ratings"},{"title":"ICLR 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?page=210&venue=ICLR.cc/2024/Conference"}]

Based on the search results, I found the paper you're looking for:

The paper "On the Stability of Iterative Retraining of Generative Models on their own Data" by Bertrand and colleagues was accepted to ICLR 2024 with a spotlight presentation.

The paper is authored by Quentin Bertrand (Université de Montréal and Mila), Avishek (Joey) Bose (McGill and Mila), Alexandre Duplessis (ENS, PSL), Marco Jiralerspong (Université de Montréal and Mila), and Gauthier Gidel (Université de Montréal and Mila).

The work studies the iterative retraining of deep generative models on mixed datasets composed of clean real data and synthetic data generated from the current 
…[truncated 382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-26T10:56:42.735173+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "DCOL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "tool_args": {
    "pattern": "DCOL",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-26T10:56:42.735390+00:00_

docs/paper/generalization.tex:13:DeBERTa-v3-base (LoRA, 53--61\%) and RoBERTa-DCOL (ordinal contrastive, 64.5\%) lag RF by 14--33\,pp; note that RF features access reference-model log-probabilities unavailable to end-to-end pretrained language model (PLM) baselines (\S\ref{sec:discussion}).
docs/paper/generalization.tex:36:RoBERTa-DCOL (ordinal) & contrastive & 64.5 & --- \\
docs/paper/section_appendix.tex:223:\subsection{DCOL Iteration Details}
docs/paper/section_appendix.tex:226:Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
docs/paper/section_appendix.tex:232:\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.7\%.}
docs/paper/section_appendix.tex:363:DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-B_20260526T104639",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 126 · 2026-05-26T10:56:42.735791+00:00_

I have enough verification data now. Let me produce the final report.

---

# 引用核查报告（Worker B：从正文 cite 出发）

## 1. 全部正文引用逐条核查

格式：`[状态] cite_key | authors | year | title_first_5_words | venue | 问题描述`

```
[✓] shumailov2024_nature | Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal | 2024 | AI models collapse when trained | Nature 631:755-759 | —
[✓] dohmatob2024_tale_of_tails | Dohmatob, Feng, Yang, Charton, Kempe | 2024 | A Tale of Tails: Model | ICML 2024 / arXiv:2402.07043 | —
[✓] seddik2024synthetic | Seddik, Chen, Hayou, Youssef, Debbah | 2024 | How Bad is Training on | arXiv:2404.05090 | —
[✓] alemohammad2024_mad | Alemohammad, Casco-Rodriguez, Luzi, ... | 2024 | Self-Consuming Generative Models Go MAD | ICLR 2024 / arXiv:2307.01850 | —
[✓] geng2026_markovian | Geng, Mohamed, Shang, Vazirgiannis, Poibeau | 2026 | Markovian Generation Chains in Large | arXiv:2603.11228 | —
[✓] bertrand2024_stability | Bertrand, Bose, Duplessis, Jiralerspong, Gidel | 2024 | On the Stability of Iterative | ICLR 2024 Spotlight / arXiv:2310.00429 | —
[✗] shi2025_closer_look | Shi, Wu, Zhang, Zhang, Tao, Qu | 2025 | A Closer Look at Model | NeurIPS 2025 Spotlight | Bib 缺 arXiv 编号 (2509.16499)；且该论文主要研究 diffusion models，论文 §related_work 描述"refinements address generalization-to-memorization transitions"对 LLM 语境而言略 stretch（但 cite key OK）
[✓] dohmatob2025_strong_collapse | Dohmatob, Feng, Subramonian, Kempe | 2025 | Strong Model Collapse | ICLR 2025 Spotlight / arXiv:2410.04840 | —
[✓] schaeffer2025 | Schaeffer, Kazdan, Arulandu, Koyejo | 2025 | Position: Model Collapse Does Not | arXiv:2503.03150 | —
[✗] wu2025_detection_survey | Wu, Yang, Zhan, Yuan, Chao, Wong | 2025 | A Survey on LLM-Generated | Computational Linguistics 51(1):275-338 | Bib 写 pages={275--354}，实际为 275-338（页码错误）
[✓] mitchell2023_detectgpt | Mitchell, Lee, Khazatsky, Manning, Finn | 2023 | DetectGPT: Zero-Shot Machine-Generated Text | ICML 2023 (Oral) / arXiv:2301.11305 | —
[✓] fast_detectgpt2024 | Bao, Zhao, Teng, Yang, Zhang | 2024 | Fast-DetectGPT: Efficient Zero-Shot Detection | ICLR 2024 / arXiv:2310.05130 | —
[✓] binoculars2024 | Hans, Schwarzschild, Cherepanova, Kazemi, ... | 2024 | Spotting LLMs With Binoculars: | ICML 2024 / arXiv:2401.12070 | —
[✓] gehrmann2019_gltr | Gehrmann, Strobelt, Rush | 2019 | GLTR: Statistical Detection and | ACL 2019 System Demo / arXiv:1906.04043 | —
[✓] verma2024_ghostbuster | Verma, Fleisig, Tomlin, Klein | 2024 | Ghostbuster: Detecting Text Ghostwritten | NAACL 2024 / arXiv:2305.15047 | —
[✓] tulchinskii2023_intrinsic_dim | Tulchinskii, Kuznetsov, Kushnareva, ... | 2023 | Intrinsic Dimension Estimation for Robust | NeurIPS 2023 / arXiv:2306.04723 | —
[✓] kirchenbauer2023_watermark | Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein | 2023 | A Watermark for Large | ICML 2023 / arXiv:2301.10226 | —
[✓] sadasivan2023_paraphrase | Sadasivan, Kumar, Balasubramanian, Wang, Feizi | 2023 | Can AI-Generated Text be | arXiv:2303.11156 | —
[✓] pudasaini2026_detection_fails | Pudasaini, Miralles-Pechuán, Lillis, Salvador | 2026 | Why AI-Generated Text Detection | arXiv:2603.23146 | —
[✓] bevendorff2025_two_paradigms | Bevendorff, Wiegmann, Richter, Potthast, Stein | 2025 | The Two Paradigms of LLM | Findings of ACL 2025 (pp. 3762-3787) | —
[✓] carlini2021_extracting | Carlini, Tramer, Wallace, Jagielski, ... | 2021 | Extracting Training Data from | USENIX Security 2021 / arXiv:2012.07805 | —
[✓] shi2024_minkprob | Shi, Ajith, Xia, Huang, Liu, Blevins, Chen, Zettlemoyer | 2024 | Detecting Pretraining Data from | ICLR 2024 / arXiv:2310.16789 | —
[✓] ilyas2022datamodels | Ilyas, Park, Engstrom, Leclerc, Madry | 2022 | Datamodels: Understanding Predictions with | ICML 2022 (arXiv:2202.00622) | Bib 标题用 proceedings 版（"Understanding..."），arXiv 题为 "Predicting Predictions from Training Data"——两者皆为同一篇论文官方版本，OK
[✓] christ2024_undetectable | Christ, Gunn, Zamir | 2024 | Undetectable Watermarks for Language | COLT 2024 PMLR 247:1125-1139 / arXiv:2306.09194 | —
[✓] zhu2025_trove | Zhu, Xiao, Wang, Zhai, Zhou, Zong | 2025 | TROVE: A Challenge for | ACL 2025 / arXiv:2503.15289 | —
[✓] editlens2026 | Thai, Emi, Masrour, Iyyer | 2026 | EditLens: Quantifying the Extent | ICLR 2026 / arXiv:2510.03154 | —
[✓] uchendu2020_attribution | Uchendu, Le, Shu, Lee | 2020 | Authorship Attribution for Neural | EMNLP 2020 (pp. 8384-8395) | —
[✓] mohamed2025_broken_telephone | Mohamed, Geng, Vazirgiannis, Shang | 2025 | LLM as a Broken Telephone: | ACL 2025 Long / arXiv:2502.20258 | —
[✓] coral2020 | Cao, Mirjalili, Raschka | 2020 | Rank Consistent Ordinal Regression | Pattern Recognition Letters 140:325-331 / arXiv:1901.07884 | —
[✓] cloc2025 | Pitawela, Carneiro, Chen | 2025 | CLOC: Contrastive Learning for | CVPR 2025 / arXiv:2504.17813 | —
[✓] holtzman2020_nucleus | Holtzman, Buys, Du, Forbes, Choi | 2020 | The Curious Case of | ICLR 2020 / arXiv:1904.09751 | —
[✓] finlayson2024_closing | Finlayson, Hewitt, Koller, Swayamdipta, Sabharwal | 2024 | Closing the Curious Case | ICLR 2024 / arXiv:2310.01693 | —
[✓] garces_arias2025_decoding_decoded | Garcés Arias, Li, Heumann, Assenmacher | 2025 | Decoding Decoded: Understanding Hyperparameter | COLING 2025 / arXiv:2410.06097 | —
[✓] wiher2022_decoding | Wiher, Meister, Cotterell | 2022 | On Decoding Strategies for | TACL 2022 vol.10 pp.997-1012 | —
[✓] basu2021_mirostat | Basu, Ramachandran, Keskar, Varshney | 2021 | Mirostat: A Neural Text | ICLR 2021 / arXiv:2007.14966 | —
[✓] strobl2008_conditional | Strobl, Boulesteix, Kneib, Augustin, Zeileis | 2008 | Conditional variable importance for | BMC Bioinformatics 9:307 | —
[✓] hooker2021_permutation | Hooker, Mentch, Zhou | 2021 | Unrestricted Permutation forces Extrapolation: | Statistics and Computing 31:82 | —
[✓] hosmer2000 | Hosmer, Lemeshow | 2000 | Applied Logistic Regression | Wiley 2nd Edition | —
[✗] he2021_deberta_v3 | He, Gao, Chen | 2021 | DeBERTaV3: Improving DeBERTa using | ICLR 2023 / arXiv:2111.09543 | Bib year 写 2021 且 booktitle=ICLR，实际 ICLR 2023 接收（2021 是 arXiv 上线时间）。应改为 year={2023}
[✓] liu2019_roberta | Liu, Ott, Goyal, Du, Joshi, Chen, Levy, Lewis, Zettlemoyer, Stoyanov | 2019 | RoBERTa: A Robustly Optimized | arXiv:1907.11692 | —
[✓] qwen2.5 | Qwen Team | 2024 | Qwen2.5 Technical Report | arXiv:2412.15115 | —
[✓] llama3 | Grattafiori et al. | 2024 | The Llama 3 Herd | arXiv:2407.21783 | —
[✓] mccullagh1980_ordinal | McCullagh | 1980 | Regression Models for Ordinal | JRSS Series B 42(2):109-142 (with discussion) | —
[✓] frank2001 | Frank, Hall | 2001 | A Simple Approach to | ECML 2001 LNCS 2167 pp.145-156 | —
[✓] rennie2005 | Rennie, Srebro | 2005 | Loss Functions for Preference | IJCAI 2005 Workshop on Advances in Preference Handling | —
[✓] hu2022lora | Hu, Shen, Wallis, Allen-Zhu, Li, Wang, Wang, Chen | 2022 | LoRA: Low-Rank Adaptation of | ICLR 2022 / arXiv:2106.09685 | —
[✓] diveye2026 | Basani, Chen | 2026 | Diversity Boosts AI-Generated Text | TMLR 2026 / arXiv:2509.18880 | —
[✓] drayson2025_detection_prevents_collapse | Drayson, Yilmaz, Lampos | 2025 | Machine-generated text detection prevents | EMNLP 2025 (pp. 29657-29673) | —
```

## 2. 引用上下文匹配问题

| cite_key | 上下文 | 匹配评估 |
|---|---|---|
| `shi2025_closer_look` | "refinements address generalization-to-memorization transitions" | 该论文主要研究 diffusion models 的 generalization→memorization，并非 LLM 模型崩塌。论文 related work 上下文在讨论 LLM/text 的 model collapse；cite 在 NeurIPS 2025 主题上是 valid，但读者可能误以为该论文研究 LLM。建议在句中显式标注"diffusion models" 或换 cite 为更直接相关的 LLM 工作。 |
| `ilyas2022datamodels` | "Datamodels \cite{ilyas2022datamodels}, watermarks ..., TROVE ... address membership inference or source attribution but remain binary or cooperation-dependent." | Datamodels 严格说是预测训练样本对模型行为的影响（influence/attribution-of-training-points），不是传统意义的 membership inference。语义略有 stretch，但 attribution 类比可接受。 |
| `cloc2025` | section_appendix.tex 中 "DCOL \cite{cloc2025}" | 文中"DCOL"是作者自定义的命名（基于 CLOC 方法的变体），cite 指向 CLOC 原论文是合理的（说明方法来源）。 |

未发现 cite A 描述了 B 的明确错误，但 `shi2025_closer_look` 在域上是 diffusion → LLM 的跨域引用，建议复核。

## 3. Orphan References（bib 中未被正文引用的条目）

共 **29 条** orphan：

```
dohmatob2024_demystified
gerstgrasser2024_accumulate
marchi2024_heat_death
knowledge_collapse2025
sigma2026_spectral
synthetic_eggs2026
yi2026_escaping_collapse
muennighoff2023scaling
bakshi2026_collapse_improvement
wang2026_contamination
falahati2026_curated
pu2026_generator_barrier
wang2023_seqxgpt
bevendorff2026_pan
wang2024_m4_semeval
li2024_mage
yang2024_dnagpt
kazdan2025_collapse_or_thrive
suresh2025_rate_collapse
wenzek2020_ccnet
dugan2024_raid
guo2024curious
padmakumar2024diversity
briesch2024selfconsuming
janitza2016_ordinal_rf
guo2024_biscope
kasa2024_ordinality
zhang2024_minkpp
lakens2017
```

由于 ACL/EMNLP 模板下 `\bibliography` 只输出实际被引用的 entry，这些条目不会出现在最终 PDF 中——不算硬错误，但 bib 文件冗余较多，建议清理或在草稿阶段标注。

注：`drafts/14b_scenarios.tex` 不在 `main.tex` 的 `\input` 链中，其中的 `\cite{llama3}` / `\cite{qwen2.5}` 不进入编译。

## 4. 统计汇总

- 总计正文实际使用 cite keys：**48** 个 unique 条目
- ✓ 通过：**46**
- ✗ 有问题：**2**
- Orphan references in .bib (未被正文引用)：**29** 个

## 5. 具体错误及建议修复

### ✗ 错误 1：`wu2025_detection_survey` 页码错误
- **文件**：`references.bib:171`
- **当前**：`pages = {275--354}`
- **实际**：`pages = {275--338}`（来源：MIT Press / ACL Anthology 官方页面，DOI 10.1162/coli_a_00549）
- **修复**：将 `pages = {275--354}` 改为 `pages = {275--338}`

### ✗ 错误 2：`he2021_deberta_v3` 年份错误
- **文件**：`references.bib:437-444`
- **当前**：`year = {2021}`, `booktitle = {Proceedings of ICLR}`
- **实际**：ICLR 2023 接收（arXiv 上线时间 2021-11，但会议接收在 2023）
- **修复**：将 `year = {2021}` 改为 `year = {2023}`（cite key 名称为 `he2021_*` 保留即可，但 entry 内 year 字段应反映会议年份；或将 cite key 重命名为 `he2023_deberta_v3`，但会需要在所有 .tex 中替换调用）

## 6. 次要建议

- `shi2025_closer_look` 域差异（diffusion vs LLM）：若审稿人挑刺，可在 `related_work.tex:6` 引文处补一句限定语，或换为更直接的 LLM model-collapse refinement 工作。
- `ilyas2022datamodels` 在 "membership inference or source attribution" 描述下略 stretch；可考虑改写为 "training-data influence attribution"。
- Bib 中 29 个 orphan entries 建议在投稿前清理（虽不影响最终 PDF，但暴露给共作者/reviewer 时显得草率）。

Sources:
- [Wu et al. survey - ACL Anthology](https://aclanthology.org/2025.cl-1.8/)
- [DeBERTaV3 - arXiv 2111.09543](https://arxiv.org/abs/2111.09543)
- [Shi et al. A Closer Look - NeurIPS 2025](https://neurips.cc/virtual/2025/poster/119754)
- [Bertrand et al. ICLR 2024 Spotlight](https://github.com/qb3/gen_models_dont_go_mad)
- [Shumailov et al. Nature 2024](https://www.nature.com/articles/s41586-024-07566-y)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_ref-audit-B_20260526T104639"
}
```

</details>

---
