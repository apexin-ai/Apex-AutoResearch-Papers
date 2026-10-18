# paper bibliography terminology

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_paper_bibliography-terminology_20260515T155105.jsonl`
- **Structured JSON:** [`4f9ef4c2361b18bedc62.json`](../../sessions/4f/4f9ef4c2361b18bedc62.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-15T15:53:06.216819+00:00_

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
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T15:53:06.217483+00:00_

1	@article{shumailov2024_nature,
2	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
3	  title     = {{AI models collapse when trained on recursively generated data}},
4	  journal   = {Nature},
5	  year      = {2024},
6	  doi       = {10.1038/s41586-024-07566-y},
7	}
8	
9	@inproceedings{marchi2024_heat_death,
10	  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},
11	  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},
12	  booktitle = {Proceedings of ICASSP},
13	  year      = {2024},
14	  note      = {arXiv:2404.02325},
15	  url       = {https://arxiv.org/abs/2404.02325},
16	}
17	
18	@inproceedings{dohmatob2024_tale_of_tails,
19	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
20	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
21	  booktitle = {Proceedings of ICML},
22	  year      = {2024},
23	  note      = {arXiv:2402.07043},
24	  url       = {https://arxiv.org/abs/2402.07043},
25	}
26	
27	@inproceedings{dohmatob2024_strong_collapse,
28	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
29	  title     = {{Strong Model Collapse}},
30	  booktitle = {Proceedings of ICLR},
31	  year      = {2024},
32	  note      = {arXiv:2410.04840},
33	  url       = {https://arxiv.org/abs/2410.04840},
34	}
35	
36	@inproceedings{dohmatob2024_demystified,
37	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
38	  title     = {{Model Collapse Demystified: The Case of Regression}},
39	  booktitle = {Proceedings of NeurIPS},
40	  year      = {2024},
41	  note      = {arXiv:2402.07712},
42	  url       = {https://arxiv.org/abs/2402.07712},
43	}
44	
45	@inproceedings{mohamed2025_broken_telephone,
46	  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
47	  title     = {{LLM a
…[truncated 12027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T15:53:06.217824+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T15:53:06.218108+00:00_

docs/paper/main.tex
docs/paper/abstract.tex
docs/paper/section_appendix.tex
docs/paper/conclusion.tex
docs/paper/related_work.tex
docs/paper/discussion.tex
docs/paper/generalization.tex
docs/paper/method.tex
docs/paper/atlas.tex
docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T15:53:06.218402+00:00_

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
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T15:53:06.218643+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	
18	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{atlas}
34	
35	\input{generalization}
36	
37	\input{discussion}
38	
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{section_appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T15:53:06.218915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T15:53:06.219158+00:00_

1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises---yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	From each passage we extract 19 statistical features---perplexity percentiles, surprisal moments, and lexical diversity measures---computed against a fixed reference model (GPT-2 base, 124M).
5	A Random Forest classifier achieves 70--85\% four-class accuracy (chance = 25\%; a zero-shot LLM baseline reaches only 40\%), with 90th-percentile perplexity and surprisal variance emerging as universal depth markers (top-2 importance in 9/9 and 7/9 model--strategy cells, respectively; mean Spearman $\rho{=}0.868$).
6	Our \emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for extended recursion chains.
7	Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%, though temperature sampling induces a d1/d2 AUC inversion that z-score normalization cannot resolve.
8	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T15:53:06.219391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T15:53:06.219655+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical---it is already occurring in the wild---yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive depth of a text passage from its content alone.
13	
14	Our key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints exhibit universal stability across model families and decoding strategies.
15	Specifically, perplexity tail statistics---the 90th-percentile perplexity (\textsc{p90\_ppl}) and surprisal variance (\textsc{var\_surprisal})---emerge as dominant depth indicators, rank
…[truncated 2942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T15:53:06.219947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T15:53:06.220228+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursively training language models on their own outputs erodes distributional tails, eventually collapsing the output distribution to a narrow mode.
6	\citet{dohmatob2024_tale_of_tails} formalize this phenomenon through scaling laws that distinguish tail \emph{narrowing} (reduced variance) from tail \emph{cutting} (lost support), showing both accelerate with generation depth; \citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \citet{dohmatob2024_demystified} analyze the regression case.
7	The MAD framework \cite{alemohammad2024_mad} extends this analysis to self-consuming generative models and quantifies the precision--recall tradeoff as synthetic data accumulates across generations.
8	Mitigation strategies include retaining real data \cite{gerstgrasser2024_accumulate} and filtering synthetic samples via detection \cite{drayson2025_detection_prevents_collapse}.
9	Recent work identifies non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, fixed-point convergence \cite{marchi2024_heat_death}, contamination bounds \cite{wang2026_contamination}, curated pipelines \cite{falahati2026_curated}, knowledge collapse \cite{knowledge_collapse2025}, spectral signatures \cite{sigma2026_spectral}, and self-improving loops \cite{synthetic_eggs2026}.
10	These works characterize degradation patterns but assume the generation depth is known a priori; our work addresses the inverse problem of estimating depth from text alone.
11	
12	\paragraph{AI Text Detection.}
13	DetectGPT \cite{mitchell2023_detectgpt} introduced probability curvature---the tendency of model-generated text to occupy local maxima of the log-probability surface---as a zero-shot detection signal.
14	\citet{fast_detectgpt2024} improve computational efficiency by replacing random perturbations with conditional probability curvature from a surrogate 
…[truncated 3207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T15:53:06.220487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T15:53:06.220792+00:00_

1	\section{Task Formulation}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	
27	\paragraph{Depth and scale.}
28	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
29	For depth ex
…[truncated 5766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T15:53:06.221088+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T15:53:06.221436+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\times$ 3 decoding strategies $\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.
5	For each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \S\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.
6	
7	\subsection{In-Distribution Performance}
8	\label{sec:atlas:indist}
9	
10	Table~\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.
11	All 9 cells exceed chance (25\%) by a wide margin, with accuracy ranging from 69.6\% to 85.4\%.
12	Both model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.
13	Top-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{In-distribution 4-class depth estimation accuracy (\%) across 3 model families $\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\%.}
19	\label{tab:main_matrix}
20	\begin{tabular}{lccc}
21	\toprule
22	Model & Nucleus & Temp & Top-$k$ \\
23	 & $p{=}0.95$ & $\tau{=}0.9$ & $k{=}50$ \\
24	\midrule
25	Pythia-1.4B & 78.2 & 76.3 & 69.6 \\
26	OLMo-1B & 78.8 & 82.0 & 74.2 \\
27	GPT-2 XL & 83.3 & \textbf{85.4} & 76.6 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	Because the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accurac
…[truncated 9164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T15:53:06.221709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T15:53:06.222039+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether the atlas results (69.6--85.4\%) reflect genuine statistical regularities or training artifacts, evaluating four axes: classifier choice (\S\ref{sec:gen:baselines}), cross-model transfer (\S\ref{sec:gen:crossmodel}), cross-strategy transfer (\S\ref{sec:gen:crossstrategy}), and end-to-end learning (\S\ref{sec:gen:dcol}).
5	
6	\subsection{Baseline Comparison}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.
10	Three feature-based methods---Random Forest (RF), CORAL ordinal regression \cite{coral2020}, and DivEye \cite{diveye2026}---all operate on the same 19 statistical features and achieve statistically indistinguishable accuracy (78.1--78.2\%; pairwise bootstrap $p>0.05$ after Bonferroni correction, 95\% CI within $\pm$1.1pp).
11	These three significantly outperform CE-MLP ($p<0.001$, $+$3.8pp), which in turn trails logistic regression by $\sim$0.1pp.
12	Single-feature regression on mean perplexity performs at chance (25.1\%), confirming that depth estimation requires the multi-dimensional feature representation defined in \S\ref{sec:method}.
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\caption{Comparison of classification methods on Pythia-1.4B nucleus. RF, CORAL, and DivEye use the same 19 statistical features and are statistically indistinguishable (bootstrap $p>0.05$, Bonferroni-corrected). Chance = 25\%. 5-fold CV std: 0.2--0.9pp across all methods.}
18	\label{tab:baselines}
19	\begin{tabular}{lc}
20	\toprule
21	Method & 4-class Acc (\%) \\
22	\midrule
23	RF (19 features) & 78.2 \\
24	CORAL & 78.1 \\
25	DivEye & 78.2 \\
26	CE-MLP & 74.9 \\
27	LR & 75.0 \\
28	DeepSeek V3.2 (zero-shot)\footnotemark & 40.0 \\
29	ppl-regression (single feature) & 25.1 \\
30	\bottomrule
31	\end{tabular}
32	\footnotetext{Evaluated on 200 samples (approximately 50 per class) from the Pythia-1.4B nucleus cell on
…[truncated 5299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T15:53:06.222301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T15:53:06.222523+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Depth-graduated data curation.}
5	Predicted depth can serve as a continuous quality proxy for importance weighting in curation pipelines \cite{dsir2023,qurating2024}, retaining shallow-generation text while down-weighting deeply recursive samples that binary filters \cite{drayson2025_detection_prevents_collapse} would indiscriminately discard.
6	
7	\paragraph{Deployment considerations.}
8	The temperature-induced d1/d2 AUC inversion (\S\ref{sec:gen:crossstrategy}) means deploying without knowing the target decoding strategy risks systematic prediction reversals; strategy-conditioned classifiers or automatic strategy identification are needed.
9	
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T15:53:06.222753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T15:53:06.223028+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced recursive generation depth estimation and showed that 19 lightweight statistical features---with p90 perplexity and surprisal variance as universal markers---achieve 70--85\% four-class accuracy (chance = 25\%) with $\mathrm{EDD}_{0.75}{=}4$.
5	Cross-model transfer reaches 66.4\% and cross-strategy 59.1\%, though the temperature-induced d1/d2 inversion and PLMs' ${\sim}$59\% ceiling underscore remaining challenges; future work should address wild-data transfer, larger scales, and strategy-conditioned classifiers.
6	Code and data will be released upon acceptance.
7	
8	\section*{Limitations}
9	\label{sec:limitations}
10	
11	\paragraph{Cross-strategy deployment constraint.}
12	Deploying depth estimators across decoding strategies requires knowing the target strategy type a priori.
13	Without this knowledge, d1/d2 predictions may systematically invert: cross-strategy holdout d1v2 AUC drops to 0.129 (GPT-2~XL) and 0.253 (OLMo) when temperature-sampled text is classified by a model trained on nucleus and top-$k$ (\S\ref{sec:gen:crossstrategy}).
14	Strategy-conditioned classifiers or automatic strategy identification are needed before deployment.
15	
16	\paragraph{d0 inflation of headline metrics.}
17	Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all settings), inflating headline accuracy.
18	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
19	
20	\paragraph{Controlled vs.\ ecological setting.}
21	All experiments use Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models).
22	Transfer to mixed-domain corpora, instruction-tuned models, and larger scales (7B+) remains open.
23	Wild-data calibration is probed only indirectly; ecological transfer is future work.
24	
25	\paragraph{EDD threshold sensitivity.}
26	The Effective Discriminable Depth depend
…[truncated 1107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T15:53:06.223281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T15:53:06.223542+00:00_

1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:trajectories}.
9	Concretely, the d0$\to$d1 drop in \textsc{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	Results are highly consistent: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both measures, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$).
17	The mean Spearman rank correlation between Gini and permutation importance vectors across all 9 cells is $\rho{=}0.94$, confirming that the reported feature universality is robust to the choice of importance measure.
18	
19	\subsection{DCOL Iteration Details}
20	\label{app:dcol_iterations}
21	
22	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
23	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
24	
25	\begin{table}[h]
26	\centering
27	\small
28	\caption{DCOL iteration summary. All experim
…[truncated 1689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T15:53:06.223864+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "recursive depth|iteration depth",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Grep",
  "tool_args": {
    "pattern": "recursive depth|iteration depth",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T15:53:06.224103+00:00_

docs/paper/introduction.tex:12:No existing method estimates the ordinal recursive depth of a text passage from its content alone.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T15:53:06.224315+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "quality degradation|hand-crafted|perplexity features",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Grep",
  "tool_args": {
    "pattern": "quality degradation|hand-crafted|perplexity features",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T15:53:06.224528+00:00_

docs/paper/method.tex:75:While correlated with perplexity features, surprisal variance captures second-order structure---the variability of token predictability---that is not redundant with perplexity moments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T15:53:06.224739+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "recursive collapse",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Grep",
  "tool_args": {
    "pattern": "recursive collapse",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T15:53:06.224965+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T15:53:06.225174+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T15:53:06.225448+00:00_

docs/paper/generalization.tex:10:Three feature-based methods---Random Forest (RF), CORAL ordinal regression \cite{coral2020}, and DivEye \cite{diveye2026}---all operate on the same 19 statistical features and achieve statistically indistinguishable accuracy (78.1--78.2\%; pairwise bootstrap $p>0.05$ after Bonferroni correction, 95\% CI within $\pm$1.1pp).
docs/paper/generalization.tex:98:Z-score normalization \cite{sugiyama2007_importance_weighting} improves logistic regression cross-strategy accuracy (25\%$\to$61\%) but does not recover the inversion---all three models worsen (GPT-2~XL 0.50$\to$0.24, OLMo 0.50$\to$0.19, Pythia 0.63$\to$0.52)---confirming a genuine geometry-level shift rather than a correctable scale difference.
docs/paper/generalization.tex:108:DCOL \cite{cloc2025}, which adds a contrastive ordinal loss, fared worse: across six iterations with two backbones (Appendix~\ref{app:dcol_iterations}), the best run (RoBERTa-large) reached only 64.5\% with severe overfitting, 13.7pp below RF.
docs/paper/introduction.tex:5:As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
docs/paper/introduction.tex:6:This model$\to$data$\to$model cycle is no longer hypothetical---it is already occurring in the wild---yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
docs/paper/introduction.tex:9:Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing al
…[truncated 4334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T15:53:06.225810+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\citet\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\citet\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T15:53:06.226094+00:00_

docs/paper/introduction.tex:11:The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
docs/paper/method.tex:35:We adopt standard LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout$\,{=}\,0.05$) following \citet{hu2022lora}, applied uniformly across all models.
docs/paper/conclusion.tex:35:\citet{bakshi2026_collapse_improvement} find that early recursion can temporarily \emph{improve} model quality, potentially violating the monotonicity assumption, and \citet{falahati2026_curated} show that curated synthetic data need not trigger collapse, attenuating the fingerprints we exploit.
docs/paper/atlas.tex:127:Temperature sampling ($\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \citet{marchi2024_heat_death}.
docs/paper/related_work.tex:5:\citet{shumailov2024_nature} demonstrate that recursively training language models on their own outputs erodes distributional tails, eventually collapsing the output distribution to a narrow mode.
docs/paper/related_work.tex:6:\citet{dohmatob2024_tale_of_tails} formalize this phenomenon through scaling laws that distinguish tail \emph{narrowing} (reduced variance) from tail \emph{cutting} (lost support), showing both accelerate with generation depth; \citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \citet{dohmatob2024_demystified} analyze the regression case.
docs/paper/related_work.tex:14:\citet{fast_detectgpt2024} improve computational efficiency by replacing random perturbations with conditional probability curvature from a surrogate model.
docs/paper/related_work.tex:17:\citet{sadasivan2023_paraphrase} expose fundamental limits: paraphrasing attacks reduce detection accuracy to near chance, and
…[truncated 1669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T15:53:06.226423+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
  "old_string": "No existing method estimates the ordinal recursive depth of a text passage from its content alone.",
  "new_string": "No existing method estimates the ordinal recursive generation depth of a text passage from its content alone."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
    "old_string": "No existing method estimates the ordinal recursive depth of a text passage from its content alone.",
    "new_string": "No existing method estimates the ordinal recursive generation depth of a text passage from its content alone."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T15:53:06.226685+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_bibliography-terminology_20260515T155105",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T15:53:06.226977+00:00_

## 结果

### Task 1: Bibliography — 已满足
38 条 bib 条目，≥ 25。任务要求的所有引用均已存在：Kirchenbauer, Alemohammad, Dohmatob (tale of tails + strong + demystified), Gerstgrasser, Shumailov, DSIR, QuRating, Uchendu, Binoculars, Fast-DetectGPT, DivEye, Garces Arias, Holtzman, Sadasivan, CORAL, CLOC, Drayson, EditLens, Bakshi, Marchi, Pudasaini, Falahati, Sugiyama, Hu (LoRA)。无需新增。

### Task 2: 术语一致性 — 1 处修正
- `introduction.tex:12` "ordinal recursive depth" → "ordinal recursive generation depth"
- 其余术语一致：首次出现均用 "recursive generation depth"，后续缩写 "generation depth"；"model collapse" 统一使用文献标准用法；"statistical features" 全文一致；EDD 在 abstract 首次出现时已定义。

### Task 3: Orphan bib — 无 orphan
38/38 条 bib 条目均在 .tex 文件中被引用，无需标记。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_bibliography-terminology_20260515T155105"
}
```

</details>

---
