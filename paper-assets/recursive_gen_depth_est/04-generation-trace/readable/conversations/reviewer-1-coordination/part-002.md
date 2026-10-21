# Reviewer 1 coordination — Part 2 of 3

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/b5/b5a69f660c93ec0a662f.json)

## Round 17

### Tool result

_source line 455 · 2026-05-18T14:10:15.100445+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-18T14:10:15.100791+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-18T14:10:15.151290+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-18T14:10:18.363826+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-18T14:10:18.816244+00:00_

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
17	\usepackage{amsthm}
18	
19	\theoremstyle{definition}
20	\newtheorem{definition}{Definition}
21	
22	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	
33	\input{related_work}
34	
35	\input{method}
36	
37	\input{atlas}
38	
39	\input{generalization}
40	
41	\input{discussion}
42	
43	\input{conclusion}
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{section_appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-18T14:10:18.866940+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-18T14:10:19.319151+00:00_

1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	A Random Forest over 19 perplexity-based features achieves $\approx$69--86\% four-class accuracy (chance = 25\%), with perplexity tail statistics emerging as consistent depth markers; a parsimonious subset of 5 features retains 97.6\% of full performance.
5	We define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for the best-characterized family, and show that cross-model transfer reaches 66.4\% (2.7$\times$ chance).
6	Systematic generalization across eight axes (e.g., cross-scale 7B at 70.2\%, prompted generation at 69.5\%, cross-model chains at 84.75\%, and cross-domain arXiv at 74.1\%) confirms that depth signal is robust across model families but strategy-dependent, residing in distributional statistics inaccessible from surface text (zero-shot LLMs: 30--36\%, 43\,pp below RF).
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-18T14:10:19.369756+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-18T14:10:19.772034+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	We find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.
15	Specifically, perplexity tail statistics (the 90th-percentile perplexity, \texttt{p90\_ppl}, and surprisal variance, \text
…[truncated 2702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-18T14:10:19.772415+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-18T14:10:19.822979+00:00_

1	\section{Method}
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
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 6862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-18T14:10:20.225045+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-18T14:10:21.129327+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.8\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.9--85.9\%), followed by OLMo (74.5--82.1\%) and Pythia (68.8--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.2~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; 10{,}000 resamples) across the $3 \times 3$ atlas; d1--d3 three-class accuracy in parentheses (chance = 25\% / 33\%). Depth-0 recall exceeds 98\% in all cells.}
22	\label{tab:main_matrix}
23	\begin{tabular}{@{}lccc@{}}
24	\toprule
25	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
26	\midrule
27	Pythia-1.4B  & 78.7{\scriptsize$\pm$0.5}\,(71.2) & 76.7{\scriptsize$\pm$0.5}\,(70.6) & 68.8{\scriptsize$\pm$0.6}\,(58.8) \\
28	OLMo-1B     & 78.9{\scriptsize$\pm$0.5}\,(75.0) & 82.1{\scriptsize$\pm$0.5}\,(76.3) & 74.5{\scriptsize$\pm$0.5}\,(66.1) \\
29	GPT-2~XL    & \textbf{84.1}{\scriptsize$\pm$0.5}\,(79.0) & \textbf{
…[truncated 12841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-18T14:10:21.129831+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-18T14:10:21.632106+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.8--85.9\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} evaluates bagging (RF) and gradient boosting (XGBoost, LightGBM) on the same 19 features; per-cell spread ($\leq$0.4pp) establishes a feature-determined ceiling.
10	On Pythia nucleus, CORAL \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match RF within 0.6\,pp ($p>0.05$); all feature-based methods outperform CE-MLP (74.9\%) and logistic regression (75.0\%).
11	Binary detectors repurposed for ordinal classification (Binoculars + Fast-DetectGPT combined: 74.2\%) fall 4\,pp below RF (Appendix~\ref{app:detector_baselines}).
12	
13	\paragraph{Surface-text ablation.}
14	Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (DeepSeek V3.2, 36.2\%; Qwen2.5-7B-Instruct, 30.4\%) also fail (43\,pp below RF; Appendix~\ref{app:zeroshot_prompt}); depth signal therefore resides in distributional statistics inaccessible from surface text.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\caption{Classifier convergence: 4-class accuracy (\%) across three atlas cells. RF (bagging), XGBoost and LightGBM (gradient boosting) operate on the same 19 features; $\Delta_{\max}$: largest per-cell spread. Chance = 25\%. RF values differ from Table~\ref{tab:main_matrix} by $\leq$0.2pp due to matched-fold evaluation. 5-fold cross-validation standard deviation $\leq$ 0.9\,pp across all settings.}
20	\label{tab:baselines}
21	\begin{tabular}{@{}lcccc@{}}
22	\toprule
23	Cell & RF & XGB & LGBM & $\Delta_{\max}$ \\
24	\midrule
25	Pythia, nuc. & 78.8 & 79.0 & 78.9 & 0.2 \\
26	GPT-2~XL, $\tau$ & 85.8 & 86.2 & 86.2 & 0.4 \\
27	Pythia, top-$k$ & 68.9 & 68.9 & 68.7 & 0.2 \\
28	\bottomrule
29	\end{tabular}
…[truncated 5015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-18T14:10:21.682729+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-18T14:10:22.084848+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \cite{seddik2024synthetic}, \citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \cite{alemohammad2024_mad} extends the analysis to self-consuming models.
6	Subsequent work addresses mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.
7	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, and call for operationally precise metrics.
8	Dohmatob et al.\ predict that recursive training erodes distributional tails as a theoretical scaling law \citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt2024}, Binoculars \cite{binoculars2024}, DivEye \cite{diveye2026}, GLTR \cite{gehrmann2019_gltr}, Ghostbuster \cite{verma2024_ghostbuster}, DNA-GPT \cite{yang2024_dnagpt}), geometric approaches based on intrinsic dimensionality \cite{tulchinskii2023_intrinsic_dim}, and watermarking 
…[truncated 2352 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-18T14:10:22.085382+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-18T14:10:22.135858+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation as ordinal classification and showed that perplexity tail statistics achieve 69--86\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance.
5	LoRA fine-tuning loss decreases monotonically with depth for all three families, a direct empirical validation of the tail erosion predicted by \citet{dohmatob2024_tale_of_tails}; instruction tuning regularizes this compression (\S\ref{sec:gen:crossscale}).
6	The non-uniform AUC contraction across adjacent pairs (ratio 0.69--0.80) is qualitatively consistent with exponential decay but deviates quantitatively.
7	RF-filtered subsets outperform random subsampling ($p{<}0.001$; Appendix~\ref{app:curation_poc}, \ref{app:downstream}), and cross-model chains (84.75\%; Appendix~\ref{app:cross_boundary}) confirm the signal is process-level; cross-strategy transfer and depth-quality entanglement remain open challenges (Limitations; Appendix~\ref{app:extended_discussion}).
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-18T14:10:22.588244+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-18T14:10:22.588675+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Cross-strategy deployment constraint.}
5	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
6	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random Forest classifier used throughout the main experiments ($\Delta < 0.02$\,pp), and even in the best case (logistic regression) leaves a residual gap relative to within-strategy performance (${\sim}0.83$); a two-stage pipeline (strategy identification + strategy-conditioned classification) is therefore needed for reliable cross-strategy deployment.
7	
8	\paragraph{Strategy-unknown deployment.}
9	In strategy-unknown settings, naive transfer on d1--d3 yields only 45.9\%, and d1/d2 predictions may invert.
10	A two-stage pipeline recovers 11.5\,pp over LOO, though per-model gains vary (GPT-2~XL $+$16.4\,pp vs.\ Pythia $+$8.0\,pp).
11	Practical deployment requires either strategy metadata or learned routing.
12	
13	\paragraph{d0 inflation of headline metrics.}
14	Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all nine model--strategy settings), inflating headline accuracy.
15	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
16	
17	\paragraph{Controlled vs.\ ecological setting.}
18	The primary benchmark uses Wikipedia seed text with controlled LoRA fine-tuning (1--1.5B models), a design that isolates the depth variable but diverges from wild contamination where models train on mixed corpora with prior-generation outputs at unknown proportions.
19	Domain bias controls confirm depth as the dominant factor: LOGO accuracy (72.1\%) matches standard CV (72.0\%), seed-group prediction is at chance (10.2\%; Appendix~\ref{app:domain_bias}).
20	Cross-scale experiments (7--8B, \S
…[truncated 5678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-18T14:10:22.940443+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-18T14:10:23.200484+00:00_

1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
9	Concretely, the d0$\to$d1 drop in \texttt{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	The top-2 features are stable across measures: \texttt{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \texttt{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \texttt{p75\_ppl} displaces \texttt{var\_surprisal} to rank 3).
17	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
18	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
19	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical; the top features are therefore robust to the choice of importance measure at the aggregate level, 
…[truncated 45789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 260
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-18T14:10:33.751999+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-18T14:10:33.904466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-18T14:10:36.866208+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"
  }
}
```

</details>

---


### Tool call

_source line 481 · 2026-05-18T14:10:37.268445+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR review form dimensions soundness excitement novelty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR review form dimensions soundness excitement novelty"
  }
}
```

</details>

---


### Tool result

_source line 482 · 2026-05-18T14:10:45.574571+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"}]

Based on the web search results, I found comprehensive information about ACL ARR (ACL Rolling Review) reviewer guidelines and scoring criteria for 2025-2026:

## Key Reviewer Scoring Updates (February 2025)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, an
…[truncated 1671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8708
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-18T14:10:52.405147+00:00_

Web search results for query: "EMNLP 2026 ARR review form dimensions soundness excitement novelty"

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, I found information about the ARR (ACL Rolling Review) review form dimensions that apply to EMNLP 2026 submissions:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

The three key dimensions of the ARR review form are:

1. **Soundness**: Reviewers assess whether papers are sufficiently sound and thorough, clearly state scientific claims and provide adequate support for them, and consider the depth and/or breadth of research questions investigated and technical soundness of experiments.

2. **Excitement**: Excitement is subjective and does not necessarily follow wha
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 15136
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-18T14:10:55.772111+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-18T14:10:55.822800+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-18T14:11:00.869386+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and the detailed description of each score level. Include soundness, excitement, overall assessment, reproducibility, and any other dimensions. List every score option with its label."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and the detailed description of each score level. Include soundness, excitement, overall assessment, reproducibility, and any other dimensions. List every score option with its label."
  }
}
```

</details>

---


### Tool call

_source line 487 · 2026-05-18T14:11:02.377815+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines. Include all criteria for evaluation, what reviewers should look for in soundness, excitement, novelty, reproducibility, and limitations. Include the scoring rubric details and any specific instructions about what constitutes a strong vs weak paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines. Include all criteria for evaluation, what reviewers should look for in soundness, excitement, novelty, reproducibility, and limitations. Include the scoring rubric details and any specific instructions about what constitutes a strong vs weak paper."
  }
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-18T14:11:07.864819+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with 0.5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with 0.5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment**
Scale: 1-5 (with 0.5 increments)
- **5**: "Consider for Award"
- **4**: "Conference acceptance"
- **3**: "Findings acceptance"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce with some difficulty."
- **2**: "They would be hard pressed to reproduce."
- **1**: "They would not be able to reproduce."

## 6. **Datasets**
Scale: 1-5
- **5**: "Enabling"
- **4**: "Useful"
- **3**: "Potentially useful"
- 
…[truncated 477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6995
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-18T14:11:13.443654+00:00_

# ARR Reviewer Guidelines: Complete Evaluation Framework

## Core Evaluation Dimensions

ARR reviewers assess papers using three primary scores:

**Soundness**: Technical validity and methodological rigor. Must be justified by review text—low scores require explicit explanation of identified flaws.

**Excitement**: Personal interest level, orthogonal to soundness. Reflects subjective preference rather than objective quality.

**Overall Recommendation**: Composite judgment considering soundness, excitement, novelty, and potential impact. Papers need sufficient soundness for acceptance regardless of excitement level.

## What Reviewers Should Assess

### Methodology Evaluation
- Reproducibility: sufficient detail for replication, hyperparameter clarity, code/data availability plans
- Statistical rigor: confidence intervals, significance testing, effect sizes, p-hacking detection
- Assumption clarity: all assumptions explicitly stated; formal proofs complete and correct
- Experimental design: appropriate model/benchmark selection with clear justification

### Paper Quality Standards
Reviewers verify papers include limitations sections and check for common NLP problems: LLM evaluation without validation, undisclosed data quality issues, unmotivated sample selection, inappropriate claim scope, overclaiming, and missing statistical assessment.

### Critical Reviewer Biases to Avoid

The guidelines identify 17 heuristics that mislead reviewers:

*"Results seem obvious in retrospect"* doesn't establish prior knowledge. *"Results contradict my expectations"* may reflect confirmation bias. Novelty requires documented precedent—not simply personal unfamiliarity. Negative results deserve publication. Simple solutions outperform complex ones. Non-English research matters equally.

Papers need "sufficient evidence for claims authors make"—not hypothetical additional experiments.

## Scoring Standards

**Soundness justification requirement**: Low soundness scores without identifie
…[truncated 1143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11065
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-18T14:12:48.760164+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-18T14:12:48.760629+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-18T14:12:51.673663+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-18T14:12:51.724630+00:00_

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

…[truncated 25205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-18T14:13:50.238016+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-18T14:13:50.339104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-18T14:16:14.613521+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — Round 1 审稿意见\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**审查侧重**: 方法严谨性 + 实验设计\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类问题，构建了包含 3 个模型族 × 3 种解码策略 × 4 个深度的 180K 样本基准，提出了 Effective Discriminable Depth (EDD) 指标。基于 19 个参考模型困惑度特征的 Random Forest 分类器达到 69-86% 四分类准确率，困惑度尾部统计量（p90_ppl, var_surprisal）被识别为一致的深度标记。论文在 8 个泛化轴上进行了系统测试。任务定义新颖且实际相关，实验设计系统性强，但若干统计和方法论问题影响核心声明的可信度。\n\n---\n\n## Strengths\n\n**S1. 新颖且重要的任务形式化。** 现有工作要么做二分类检测（human vs. machine），要么研究 model collapse 时假设深度已知。本文首次将序数深度估计作为独立任务提出（§1, §3.1），填补了一个真实的研究空白。EDD 指标（Definition 1）提供了量化相邻深度可区分性的操作性框架。\n\n**S2. 系统性的实验设计。** 3×3 Atlas 网格（§4）在模型族和解码策略两个维度上系统展开，且将模型规模控制在 1-1.5B 的窄区间内以隔离架构/数据差异（§3.2）。8 个泛化轴（§5）的覆盖面在同类工作中罕见。\n\n**S3. 特征分析深度。** 三种特征重要性度量（Gini, SHAP, permutation）的一致性检验（Kendall's W=0.90, p<0.005; Appendix B）是方法论上的亮点。特征层级在不同深度边界处的转移（§4.2: 浅层 var_surprisal 主导，深层 p90_ppl 接管）提供了连接 model collapse 理论（尾部侵蚀）与实证信号的机制性洞察。\n\n**S4. 透明的局限性报告。** 论文对多个不利结果（domain bias 实现 bug 的发现与修复、GPT-2 XL 跨种子 CI 不重叠、C4 上 20-22% FPR、跨策略 d1/d2 边界反转）的坦诚报告超出了大多数投稿的标准。\n\n**S5. 实用性考量。** GPU-free 推理（2 分钟/5K 样本）、5 特征精简模型保留 97.6% 性能（§4.2）、以及详细的计算资源报告（Appendix F.19）对实际部署有价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] EDD 指标的统计声明与证据不匹配**\n- 具体位置：§4.4, 第 129-131 行\n- 问题：论文声称\"all three models cross the T=0.75 threshold within the d3-d4 region\"并称之为\"a consistent depth-4 decay boundary\"，但 bootstrap 检验结果为：Pythia p=0.001（显著），OLMo p=0.091（边缘），GPT-2 XL p=0.505（完全不显著）。在常规 α=0.05 水平下，仅 1/3 模型统计显著支持 AUC>0.75。用\"graded confidence\"来描述这一结果虽然诚实，但主文声明（\"consistent depth-4 decay boundary\"）仍然过度。Abstract 和 Introduction 中 EDD_{0.75}=4 的报告（第 5 行、第 26 行）也未充分传达这一不确定性。\n- 为什么影响接收：EDD 是本文的核心贡献之一（Contribution 2），其统计基础必须经得起检验。如果 2/3 模型不支持该声明，则 EDD=4 不能作为一般性结论。\n- 建议修改方向：(1) Abstract/Introduction 中明确 EDD_{0.75}=4 仅对 Pythia 显著成立；(2) 报告所有 9 cells 的 bootstrap p 值，而非仅 3 个扩展实验；(3) 考虑在 T=0.70 处报告 EDD 作为更稳健的主指标（Table 6 显示 T=0.70 时 8/9 cells 达标）。\n\n**N2 [critical] 单 LoRA 种子构成系统性混淆因子，跨种子复制不足**\n- 具体位置：§3.2（pipeline 描述）、Appendix F.14（cross-seed replication）\n- 问题：Atlas 的每个 cell 使用单一 LoRA 种子。跨种子复制仅覆盖 2/9 cells（Pythia nucleus, GPT-2 XL nucleus）各 2 个种子。GPT-2 XL 的两个种子结果 CI 不重叠（[83.89, 84.77] vs [86.17, 86.49]），差异 2.04pp——这意味着报告的单种子准确率受 LoRA 初始化显著影响。论文报告的跨模型效应（7.2pp）和跨策略效应（9.2pp）可能部分被 LoRA 种子噪声污染，但无法从当前数据中分离。\n- 为什么影响接收：如果 LoRA 种子可以引起 2pp+ 的系统性偏移，那么 Atlas 中基于单种子比较得出的\"strategy effect > model effect\"等结论（§4.5）的可信度存疑。审稿人无法判断 Table 2 中的准确率差异有多少源自深度信号 vs LoRA 种子偶然性。\n- 建议修改方向：(1) 至少对 Atlas 中的关键 cells（如 accuracy 最高和最低的 cells）进行 3 种子复制，报告种子间方差；(2) 或者承认无法分离 LoRA 种子效应并在 Abstract/Introduction 降低对跨 cell 比较结论的置信度。\n\n**N3 [critical] 序数分类形式化与实际方法/指标不一致**\n- 具体位置：§3.1（problem definition）、§4.1-§5（所有结果表）\n- 问题：论文在 §3.1 明确将任务定义为 ordinal classification（\"depths carry a natural ordering, and d=1 is structurally closer to d=0 than d=3 is\"），但：(a) 主分类器 Random Forest 不利用序数结构；(b) CORAL（真正的序数方法）仅作为 baseline 出现，且与 RF 无显著差异（78.1% vs 78.7%, §5.1）；(c) 全文未报告任何序数评价指标（MAE, Quadratic Weighted Kappa, adjacent-class confusion rate vs non-adjacent rate）。如果序数方法不优于非序数方法，且不报告序数指标，那么序数形式化的动机何在？\n- 为什么影响接收：形式化与执行之间的不一致削弱了 Contribution 1（\"task formalization\"）的实质性。审稿人会质疑序数声明是否只是包装。\n- 建议修改方向：(1) 报告 MAE 和 QWK 作为补充指标；(2) 分析混淆矩阵中相邻 vs 非相邻类别的错误分布——如果错误确实集中在相邻类别，这将实证支持序数结构的存在；(3) 讨论为什么 CORAL 未能超越 RF——是因为 RF 隐式捕获了序数结构，还是因为序数结构在特征空间中不重要？\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] d0 膨胀对标题指标的系统性影响未在核心展示中充分处理**\n- 具体位置：Abstract（第 4 行）、Table 2（§4.1）、Table 4（§5.2）\n- 问题：d0 recall 在所有 9 cells 中超过 98%（§4.1），人类文本与任何生成文本几乎完美可分——这本质上是一个已解决的子问题（二分类检测）。将 d0 纳入四分类准确率系统性地膨胀了标题数字。例如，cross-model transfer 报告 66.4%，但 d1-d3 balanced accuracy 仅 55.4%（§5.2，仅略高于 33% chance）。Abstract 中的\"69-86% four-class accuracy\"和\"66.4% cross-model transfer\"是读者首先看到的数字，但最具挑战性的三分类性能被降格为括号注释。\n- 建议：在 Abstract 和 Introduction 中同时突出报告 d1-d3 accuracy（已在 Table 2 括号中给出，但被严重弱化）。考虑将 d1-d3 balanced accuracy 作为平行的主指标。\n\n**W2 [warning] 跨策略迁移失败是根本性实用限制，但未被充分强调**\n- 具体位置：§5.3, Table 5; Limitations 第 1-2 段\n- 问题：跨策略 d1-d3 accuracy 仅 45.9%（chance=33%），d1/d2 boundary inversion（AUC<0.5）意味着分类器做出系统性错误预测（不仅仅是随机错误）。在实际部署中，解码策略通常未知。论文提到 two-stage pipeline 恢复 11.5pp，但这个方案未被充分验证（未报告策略识别模块的独立准确率）。这一限制当前仅出现在 Limitations 段落和简短的主文讨论中，与其对实际应用的影响不成比例。\n- 建议：在 Discussion 中更显著地讨论这一限制对实际部署场景的影响；报告策略识别步骤的独立准确率。\n\n**W3 [warning] 跨规模实验的混淆因子未被充分隔离**\n- 具体位置：§5.4, Appendix F.9\n- 问题：7-8B 实验引入了四个同时变化的因子：(1) 4-bit NF4 QLoRA（1-1.5B 用 full-precision LoRA）；(2) 样本量 500 vs 5000；(3) 仅 nucleus 采样；(4) 参考模型-生成模型的 vocabulary mismatch 更大。论文在 Appendix 中逐一列出了这些 confounds，但主文 §5.4 和 Abstract 中的表述（\"cross-scale 7B at 70.2%\"）可能给读者留下深度信号在 7B 规模稳健存在的印象，而实际上无法归因。\n- 建议：主文中弱化跨规模声明的置信度（如\"preliminary evidence\"而非并列为主要贡献）；或设计一个控制实验隔离量化效应（如在 1.5B 模型上对比 full-precision LoRA vs QLoRA）。\n\n**W4 [warning] 参考模型选择的非对称性**\n- 具体位置：§3.2（reference model 段落）、Appendix F.8\n- 问题：Pythia-1.4B 同时作为生成器之一和所有实验的参考模型。论文论证\"no systematic self-model advantage\"（Pythia 78.7% < GPT-2 XL 85.9%），但 Appendix F.8 的 reference ablation 显示 self-reference（Pythia-as-ref 对 Pythia 数据: 78.6%）优于 cross-reference（OLMo-as-ref: 74.5%, GPT-2 XL-as-ref: 67.3%）。这意味着 Pythia 的结果可能受益于 self-measurement，而 GPT-2 XL 和 OLMo 的特征提取受限于 cross-model measurement。Table 2 中 GPT-2 XL 的最高准确率可能部分因为 GPT-2 XL 的输出在 Pythia 特征空间中恰好更可分——而非 GPT-2 XL 的深度信号真正更强。\n- 建议：在主文中用 each-model-as-its-own-reference 的结果补充 Table 2 的对比，以隔离参考模型效应。\n\n**W5 [warning] 下游 curation PoC 结论不足以支撑实用价值声明**\n- 具体位置：Appendix F.10 (Table 8, Table 9)\n- 问题：RF-filtered vs unfiltered 的 perplexity 差异不显著（rf_soft: p=0.407, rf_moderate: p=0.492, rf_strict: p=0.607）。仅 RF-filtered vs random subsampling 显著——但这只说明深度过滤好于随机丢弃，未证明深度估计好于更简单的质量过滤方法（如困惑度阈值过滤）。Discussion §6 中提到的\"depth-graduated curation\"场景缺乏实证支持。\n- 建议：增加与简单困惑度阈值过滤的对比；或降低对 curation 应用的声明力度。\n\n### Minor 问题（不影响接收）\n\n**M1.** Definition 1 (Eq. 1)：EDD binary classifiers 使用 500 trees（§3.4），而主实验使用 200 trees（§4.1）。这一不一致未被解释。不同树数量是否影响 EDD 值？\n\n**M2.** Table 2 caption 中的括号值\"d1-d3 three-class accuracy\"说明不够清晰——首次阅读时容易被忽略。建议在正文中明确解释。\n\n**M3.** 19 个特征的选择缺乏系统化论证（§3.3）。为什么不包括 entropy rate, mutual information, 或其他信息论量？Table 1 列举了特征但未解释为何这 19 个是最佳或充分的候选集。\n\n**M4.** §6 Discussion and Conclusion 仅一段，对一篇包含如此多实验的论文来说过于压缩。关键 takeaway（如\"strategy matters as much as model\"）值得更充分的讨论。\n\n**M5.** Prompted generation 验证（§5.3）仅覆盖一个 cell（GPT-2 XL nucleus）。鉴于 BOS-seeded 是实验的核心设置，且 prompted generation 更接近实际场景，至少应在另外 1-2 个 cells 上验证。\n\n**M6.** Appendix F.10 curation PoC 进行了多次配对比较但未做多重比较校正。rf_moderate vs random_moderate 的 p=0.020 在 Bonferroni 校正后可能不显著。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** 主实验和所有泛化实验的 MAE 和 Quadratic Weighted Kappa 是多少？混淆矩阵中相邻类别错误占总错误的比例是多少？\n\n**Q2.** 如果将 EDD 的默认阈值设为 T=0.70（8/9 cells 达标，统计基础更强），是否会改变论文的核心叙事？\n\n**Q3.** Cross-model chains 实验（Appendix F.12）为何只测试了一种链序（加反向控制）而非全部 6 种排列？更完整的设计能否进一步隔离架构混淆？\n\n**Q4.** 参考模型使用完全无关的架构（如 T5 或 encoder-only 模型）时，EDD 和特征排名会发生什么变化？\n\n**Q5.** C4 上 20-22% 的 FPR（Pythia/GPT-2 XL）在数据 curation 场景中意味着大量人类文本被错误标记为 d1+。论文是否有 FPR 在不同深度类别上的分布？（Appendix F.7 提到了 GPT-2 XL 和 OLMo 的分布，但 Pythia 缺失。）\n\n---\n\n## Missing References\n\n1. **Repeated self-distillation 文献**：Pareek et al. (2024) \"Understanding the Gains from Repeated Self-Distillation\" 已在 bib 中但未在正文中引用——该工作从理论角度分析了迭代蒸馏的增益/损失，与递归生成深度的概念直接相关。\n\n2. **Ordinal Random Forest**：Janitza et al. (2016) \"Random forest for ordinal responses: Prediction and variable selection\" 提出了专门处理序数响应的 RF 变体——鉴于论文的 ordinal classification 形式化，应作为 baseline 或至少在 Related Work §2 中讨论。\n\n3. **SemEval-2024 Task 8 的后续分析**：Wang et al. (2024) 已引用，但该 shared task 产生了多篇关于多类别检测粒度的系统论文，可能与本文的序数扩展动机相关。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要声明有支撑，但 EDD 统计显著性不足（N1）、单 LoRA 种子混淆（N2）、序数形式化与执行不一致（N3）削弱了部分核心声明 |\n| Excitement | 3.5/5 | 任务定义新颖，Atlas 和特征分析有洞察力，但实际限制（策略依赖、高 FPR、d1-d3 准确率有限）约束了影响力 |\n| Reproducibility | 4/5 | 超参数、硬件、软件版本详尽（Appendix F.19）；代码/数据承诺发布；唯一不足是单 LoRA 种子限制了结果的可复制性验证 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文含附录，熟悉 model collapse、AI text detection 和序数分类文献 |\n\n## Overall Assessment\n\n**Overall**: 3.5（Borderline Conference）\n**一句话总结**: 一篇定义新颖任务且实验系统性强的工作，但 EDD 核心指标的统计基础不均匀、单 LoRA 种子混淆效应未充分量化、以及序数形式化与实际方法/指标之间的不一致，使其处于 Conference 与 Findings 的边界。\n\n**理由**: 本文的主要优势在于任务新颖性（S1）和实验系统性（S2），这在 AI text detection 领域是突出的。但三个 Must-Fix 问题共同构成了方法论层面的担忧：(1) EDD=4 的核心声明在 2/3 模型上不显著，(2) 单种子 atlas 的 cell 间比较可能被 LoRA 初始化噪声污染，(3) 序数形式化缺乏对应的评价指标和方法论支撑。如果作者能在 rebuttal 中提供 ordinal metrics、补充关键 cells 的多种子结果、并在 EDD 声明中准确传达统计不确定性，论文有望上升至 Conference 水平。当前状态下，Findings 接收更有把握。\n\n**Confidence**: 4/5（Quite sure. I tried to check the important points carefully.）\n",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — Round 1 审稿意见\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**审查侧重**: 方法严谨性 + 实验设计\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类问题，构建了包含 3 个模型族 × 3 种解码策略 × 4 个深度的 180K 样本基准，提出了 Effective Discriminable Depth (EDD) 指标。基于 19 个参考模型困惑度特征的 Random Forest 分类器达到 69-86% 四分类准确率，困惑度尾部统计量（p90_ppl, var_surprisal）被识别为一致的深度标记。论文在 8 个泛化轴上进行了系统测试。任务定义新颖且实际相关，实验设计系统性强，但若干统计和方法论问题影响核心声明的可信度。\n\n---\n\n## Strengths\n\n**S1. 新颖且重要的任务形式化。** 现有工作要么做二分类检测（human vs. machine），要么研究 model collapse 时假设深度已知。本文首次将序数深度估计作为独立任务提出（§1, §3.1），填补了一个真实的研究空白。EDD 指标（Definition 1）提供了量化相邻深度可区分性的操作性框架。\n\n**S2. 系统性的实验设计。** 3×3 Atlas 网格（§4）在模型族和解码策略两个维度上系统展开，且将模型规模控制在 1-1.5B 的窄区间内以隔离架构/数据差异（§3.2）。8 个泛化轴（§5）的覆盖面在同类工作中罕见。\n\n**S3. 特征分析深度。** 三种特征重要性度量（Gini, SHAP, permutation）的一致性检验（Kendall's W=0.90, p<0.005; Appendix B）是方法论上的亮点。特征层级在不同深度边界处的转移（§4.2: 浅层 var_surprisal 主导，深层 p90_ppl 接管）提供了连接 model collapse 理论（尾部侵蚀）与实证信号的机制性洞察。\n\n**S4. 透明的局限性报告。** 论文对多个不利结果（domain bias 实现 bug 的发现与修复、GPT-2 XL 跨种子 CI 不重叠、C4 上 20-22% FPR、跨策略 d1/d2 边界反转）的坦诚报告超出了大多数投稿的标准。\n\n**S5. 实用性考量。** GPU-free 推理（2 分钟/5K 样本）、5 特征精简模型保留 97.6% 性能（§4.2）、以及详细的计算资源报告（Appendix F.19）对实际部署有价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] EDD 指标的统计声明与证据不匹配**\n- 具体位置：§4.4, 第 129-131 行\n- 问题：论文声称\"all three models cross the T=0.75 threshold within the d3-d4 region\"并称之为\"a consistent depth-4 decay boundary\"，但 bootstrap 检验结果为：Pythia p=0.001（显著），OLMo p=0.091（边缘），GPT-2 XL p=0.505（完全不显著）。在常规 α=0.05 水平下，仅 1/3 模型统计显著支持 AUC>0.75。用\"graded confidence\"来描述这一结果虽然诚实，但主文声明（\"consistent depth-4 decay boundary\"）仍然过度。Abstract 和 Introduction 中 EDD_{0.75}=4 的报告（第 5 行、第 26 行）也未充分传达这一不确定性。\n- 为什么影响接收：EDD 是本文的核心贡献之一（Contribution 2），其统计基础必须经得起检验。如果 2/3 模型不支持该声明，则 EDD=4 不能作为一般性结论。\n- 建议修改方向：(1) Abstract/Introduction 中明确 EDD_{0.75}=4 仅对 Pythia 显著成立；(2) 报告所有 9 cells 的 bootstrap p 值，而非仅 3 个扩展实验；(3) 考虑在 T=0.70 处报告 EDD 作为更稳健的主指标（Table 6 显示 T=0.70 时 8/9 cells 达标）。\n\n**N2 [critical] 单 LoRA 种子构成系统性混淆因子，跨种子复制不足**\n- 具体位置：§3.2（pipeline 描述）、Appendix F.14（cross-seed replication）\n- 问题：Atlas 的每个 cell 使用单一 LoRA 种子。跨种子复制仅覆盖 2/9 cells（Pythia nucleus, GPT-2 XL nucleus）各 2 个种子。GPT-2 XL 的两个种子结果 CI 不重叠（[83.89, 84.77] vs [86.17, 86.49]），差异 2.04pp——这意味着报告的单种子准确率受 LoRA 初始化显著影响。论文报告的跨模型效应（7.2pp）和跨策略效应（9.2pp）可能部分被 LoRA 种子噪声污染，但无法从当前数据中分离。\n- 为什么影响接收：如果 LoRA 种子可以引起 2pp+ 的系统性偏移，那么 Atlas 中基于单种子比较得出的\"strategy effect > model effect\"等结论（§4.5）的可信度存疑。审稿人无法判断 Table 2 中的准确率差异有多少源自深度信号 vs LoRA 种子偶然性。\n- 建议修改方向：(1) 至少对 Atlas 中的关键 cells（如 accuracy 最高和最低的 cells）进行 3 种子复制，报告种子间方差；(2) 或者承认无法分离 LoRA 种子效应并在 Abstract/Introduction 降低对跨 cell 比较结论的置信度。\n\n**N3 [critical] 序数分类形式化与实际方法/指标不一致**\n- 具体位置：§3.1（problem definition）、§4.1-§5（所有结果表）\n- 问题：论文在 §3.1 明确将任务定义为 ordinal classification（\"depths carry a natural ordering, and d=1 is structurally closer to d=0 than d=3 is\"），但：(a) 主分类器 Random Forest 不利用序数结构；(b) CORAL（真正的序数方法）仅作为 baseline 出现，且与 RF 无显著差异（78.1% vs 78.7%, §5.1）；(c) 全文未报告任何序数评价指标（MAE, Quadratic Weighted Kappa, adjacent-class confusion rate vs non-adjacent rate）。如果序数方法不优于非序数方法，且不报告序数指标，那么序数形式化的动机何在？\n- 为什么影响接收：形式化与执行之间的不一致削弱了 Contribution 1（\"task formalization\"）的实质性。审稿人会质疑序数声明是否只是包装。\n- 建议修改方向：(1) 报告 MAE 和 QWK 作为补充指标；(2) 分析混淆矩阵中相邻 vs 非相邻类别的错误分布——如果错误确实集中在相邻类别，这将实证支持序数结构的存在；(3) 讨论为什么 CORAL 未能超越 RF——是因为 RF 隐式捕获了序数结构，还是因为序数结构在特征空间中不重要？\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] d0 膨胀对标题指标的系统性影响未在核心展示中充分处理**\n- 具体位置：Abstract（第 4 行）、Table 2（§4.1）、Table 4（§5.2）\n- 问题：d0 recall 在所有 9 cells 中超过 98%（§4.1），人类文本与任何生成文本几乎完美可分——这本质上是一个已解决的子问题（二分类检测）。将 d0 纳入四分类准确率系统性地膨胀了标题数字。例如，cross-model transfer 报告 66.4%，但 d1-d3 balanced accuracy 仅 55.4%（§5.2，仅略高于 33% chance）。Abstract 中的\"69-86% four-class accuracy\"和\"66.4% cross-model transfer\"是读者首先看到的数字，但最具挑战性的三分类性能被降格为括号注释。\n- 建议：在 Abstract 和 Introduction 中同时突出报告 d1-d3 accuracy（已在 Table 2 括号中给出，但被严重弱化）。考虑将 d1-d3 balanced accuracy 作为平行的主指标。\n\n**W2 [warning] 跨策略迁移失败是根本性实用限制，但未被充分强调**\n- 具体位置：§5.3, Table 5; Limitations 第 1-2 段\n- 问题：跨策略 d1-d3 accuracy 仅 45.9%（chance=33%），d1/d2 boundary inversion（AUC<0.5）意味着分类器做出系统性错误预测（不仅仅是随机错误）。在实际部署中，解码策略通常未知。论文提到 two-stage pipeline 恢复 11.5pp，但这个方案未被充分验证（未报告策略识别模块的独立准确率）。这一限制当前仅出现在 Limitations 段落和简短的主文讨论中，与其对实际应用的影响不成比例。\n- 建议：在 Discussion 中更显著地讨论这一限制对实际部署场景的影响；报告策略识别步骤的独立准确率。\n\n**W3 [warning] 跨规模实验的混淆因子未被充分隔离**\n- 具体位置：§5.4, Appendix F.9\n- 问题：7-8B 实验引入了四个同时变化的因子：(1) 4-bit NF4 QLoRA（1-1.5B 用 full-precision LoRA）；(2) 样本量 500 vs 5000；(3) 仅 nucleus 采样；(4) 参考模型-生成模型的 vocabulary mismatch 更大。论文在 Appendix 中逐一列出了这些 confounds，但主文 §5.4 和 Abstract 中的表述（\"cross-scale 7B at 70.2%\"）可能给读者留下深度信号在 7B 规模稳健存在的印象，而实际上无法归因。\n- 建议：主文中弱化跨规模声明的置信度（如\"preliminary evidence\"而非并列为主要贡献）；或设计一个控制实验隔离量化效应（如在 1.5B 模型上对比 full-precision LoRA vs QLoRA）。\n\n**W4 [warning] 参考模型选择的非对称性**\n- 具体位置：§3.2（reference model 段落）、Appendix F.8\n- 问题：Pythia-1.4B 同时作为生成器之一和所有实验的参考模型。论文论证\"no systematic self-model advantage\"（Pythia 78.7% < GPT-2 XL 85.9%），但 Appendix F.8 的 reference ablation 显示 self-reference（Pythia-as-ref 对 Pythia 数据: 78.6%）优于 cross-reference（OLMo-as-ref: 74.5%, GPT-2 XL-as-ref: 67.3%）。这意味着 Pythia 的结果可能受益于 self-measurement，而 GPT-2 XL 和 OLMo 的特征提取受限于 cross-model measurement。Table 2 中 GPT-2 XL 的最高准确率可能部分因为 GPT-2 XL 的输出在 Pythia 特征空间中恰好更可分——而非 GPT-2 XL 的深度信号真正更强。\n- 建议：在主文中用 each-model-as-its-own-reference 的结果补充 Table 2 的对比，以隔离参考模型效应。\n\n**W5 [warning] 下游 curation PoC 结论不足以支撑实用价值声明**\n- 具体位置：Appendix F.10 (Table 8, Table 9)\n- 问题：RF-filtered vs unfiltered 的 perplexity 差异不显著（rf_soft: p=0.407, rf_moderate: p=0.492, rf_strict: p=0.607）。仅 RF-filtered vs random subsampling 显著——但这只说明深度过滤好于随机丢弃，未证明深度估计好于更简单的质量过滤方法（如困惑度阈值过滤）。Discussion §6 中提到的\"depth-graduated curation\"场景缺乏实证支持。\n- 建议：增加与简单困惑度阈值过滤的对比；或降低对 curation 应用的声明力度。\n\n### Minor 问题（不影响接收）\n\n**M1.** Definition 1 (Eq. 1)：EDD binary classifiers 使用 500 trees（§3.4），而主实验使用 200 trees（§4.1）。这一不一致未被解释。不同树数量是否影响 EDD 值？\n\n**M2.** Table 2 caption 中的括号值\"d1-d3 three-class accuracy\"说明不够清晰——首次阅读时容易被忽略。建议在正文中明确解释。\n\n**M3.** 19 个特征的选择缺乏系统化论证（§3.3）。为什么不包括 entropy rate, mutual information, 或其他信息论量？Table 1 列举了特征但未解释为何这 19 个是最佳或充分的候选集。\n\n**M4.** §6 Discussion and Conclusion 仅一段，对一篇包含如此多实验的论文来说过于压缩。关键 takeaway（如\"strategy matters as much as model\"）值得更充分的讨论。\n\n**M5.** Prompted generation 验证（§5.3）仅覆盖一个 cell（GPT-2 XL nucleus）。鉴于 BOS-seeded 是实验的核心设置，且 prompted generation 更接近实际场景，至少应在另外 1-2 个 cells 上验证。\n\n**M6.** Appendix F.10 curation PoC 进行了多次配对比较但未做多重比较校正。rf_moderate vs random_moderate 的 p=0.020 在 Bonferroni 校正后可能不显著。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** 主实验和所有泛化实验的 MAE 和 Quadratic Weighted Kappa 是多少？混淆矩阵中相邻类别错误占总错误的比例是多少？\n\n**Q2.** 如果将 EDD 的默认阈值设为 T=0.70（8/9 cells 达标，统计基础更强），是否会改变论文的核心叙事？\n\n**Q3.** Cross-model chains 实验（Appendix F.12）为何只测试了一种链序（加反向控制）而非全部 6 种排列？更完整的设计能否进一步隔离架构混淆？\n\n**Q4.** 参考模型使用完全无关的架构（如 T5 或 encoder-only 模型）时，EDD 和特征排名会发生什么变化？\n\n**Q5.** C4 上 20-22% 的 FPR（Pythia/GPT-2 XL）在数据 curation 场景中意味着大量人类文本被错误标记为 d1+。论文是否有 FPR 在不同深度类别上的分布？（Appendix F.7 提到了 GPT-2 XL 和 OLMo 的分布，但 Pythia 缺失。）\n\n---\n\n## Missing References\n\n1. **Repeated self-distillation 文献**：Pareek et al. (2024) \"Understanding the Gains from Repeated Self-Distillation\" 已在 bib 中但未在正文中引用——该工作从理论角度分析了迭代蒸馏的增益/损失，与递归生成深度的概念直接相关。\n\n2. **Ordinal Random Forest**：Janitza et al. (2016) \"Random forest for ordinal responses: Prediction and variable selection\" 提出了专门处理序数响应的 RF 变体——鉴于论文的 ordinal classification 形式化，应作为 baseline 或至少在 Related Work §2 中讨论。\n\n3. **SemEval-2024 Task 8 的后续分析**：Wang et al. (2024) 已引用，但该 shared task 产生了多篇关于多类别检测粒度的系统论文，可能与本文的序数扩展动机相关。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要声明有支撑，但 EDD 统计显著性不足（N1）、单 LoRA 种子混淆（N2）、序数形式化与执行不一致（N3）削弱了部分核心声明 |\n| Excitement | 3.5/5 | 任务定义新颖，Atlas 和特征分析有洞察力，但实际限制（策略依赖、高 FPR、d1-d3 准确率有限）约束了影响力 |\n| Reproducibility | 4/5 | 超参数、硬件、软件版本详尽（Appendix F.19）；代码/数据承诺发布；唯一不足是单 LoRA 种子限制了结果的可复制性验证 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文含附录，熟悉 model collapse、AI text detection 和序数分类文献 |\n\n## Overall Assessment\n\n**Overall**: 3.5（Borderline Conference）\n**一句话总结**: 一篇定义新颖任务且实验系统性强的工作，但 EDD 核心指标的统计基础不均匀、单 LoRA 种子混淆效应未充分量化、以及序数形式化与实际方法/指标之间的不一致，使其处于 Conference 与 Findings 的边界。\n\n**理由**: 本文的主要优势在于任务新颖性（S1）和实验系统性（S2），这在 AI text detection 领域是突出的。但三个 Must-Fix 问题共同构成了方法论层面的担忧：(1) EDD=4 的核心声明在 2/3 模型上不显著，(2) 单种子 atlas 的 cell 间比较可能被 LoRA 初始化噪声污染，(3) 序数形式化缺乏对应的评价指标和方法论支撑。如果作者能在 rebuttal 中提供 ordinal metrics、补充关键 cells 的多种子结果、并在 EDD 声明中准确传达统计不确定性，论文有望上升至 Conference 水平。当前状态下，Findings 接收更有把握。\n\n**Confidence**: 4/5（Quite sure. I tried to check the important points carefully.）\n",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-18T14:16:18.670843+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4057
}
```

</details>

---


### Assistant

_source line 498 · 2026-05-18T14:16:28.972430+00:00_

审稿意见已提交给 Review Director。

总结：

- **Overall 3.5 (Borderline Conference)**，Soundness 3.5，Excitement 3.5
- 提出 **3 个 Must-Fix 问题**：(1) EDD_{0.75}=4 的统计声明仅 1/3 模型显著支持，headline claim 过度；(2) 单 LoRA 种子构成系统混淆，跨种子复制仅覆盖 2/9 cells 且 GPT-2 XL CI 不重叠；(3) 序数分类形式化与实际方法（非序数 RF）和评价指标（无 MAE/QWK）不一致
- 提出 **5 个 Should-Fix 问题**：d0 膨胀标题指标、跨策略迁移失败被弱化、跨规模 confounds 未隔离、参考模型非对称性、下游 curation PoC 不具说服力
- 核心判断：任务新颖性和实验系统性是明确优势，但统计基础和方法论一致性需要加强后才能达到 Conference 水平

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

4 recorded events


### User

_source line 499 · 2026-05-18T14:17:13.611820+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见（侧重：新颖性 + 完整性 + 写作质量）。请逐条回应：
- **[AGREE]**：同意并说明理由
- **[REBUT]**：反驳并提供证据（引用具体 Section/Table/Figure）

---

**Reviewer 2 评分：Overall 3.0 (Findings)**，Soundness 3.5，Excitement 2.5

### Must-Fix 问题

**R2-N1 [critical] 方法论新颖性不足：RF + hand-crafted features 缺乏算法层面的贡献**
核心 pipeline 是"提取 19 个统计特征 → 喂给 Random Forest"，是标准 feature engineering + shallow ML。EDD 本质上是 pairwise AUC 序列上的阈值截断。Table 3（§5.1）确认 RF/XGBoost/LightGBM 几乎无差异（Δ_max ≤ 0.4pp），说明贡献完全在特征设计而非分类方法。19 特征中 14-16 个 VIF>10，有效维度仅 4-5，本质是低维问题。EMNLP 2026 期望方法论贡献或显著新洞见。

**R2-N2 [critical] Discussion 过于简略**
Discussion and Conclusion 合为一节，正文仅 1 段（约 7 行）。缺少：(a) depth signal 本质来源的深入讨论；(b) 与 Dohmatob 2024 理论的定量对比；(c) practical deployment 完整路径。Appendix Extended Discussion 有内容但未在正文展开。

**R2-N3 [critical] d0 inflation 严重扭曲 headline metrics**
d0 recall > 98% 在所有 9 cells 中近乎完美，本质是 binary detection。扣除 d0 后，cross-model d1-d3 balanced accuracy 仅 55.4%（chance=33%），within-distribution d2 recall 最低 45.6%。最弱配置下 d2 recall 低至 26.8%。Abstract 报告的 69-86% 和 66.4% cross-model 与实际 d1-d3 区分能力有显著落差。

### Should-Fix 问题

**R2-W1** Abstract 将全部 19 个特征称为 "perplexity-based" 不准确（7 个特征不依赖 reference model perplexity）。

**R2-W2** Cross-strategy transfer 近乎失败（d1-d3 仅 45.9%），two-stage pipeline 未在正文验证。

**R2-W3** 主实验仅 1-1.5B 模型，2026 年标准下偏小；7-8B 实验有 QLoRA confound。

**R2-W4** 与 Dohmatob et al. 2024 的关系定位不够诚实——核心发现本质上是理论的实验验证。

**R2-W5** Downstream curation PoC：RF-filtered vs unfiltered 不显著（p>0.4），仅 RF vs random 显著。

### Minor 问题
M1: "43pp below RF" 数值不精确。M2: 3 个 orphan bib entries。M3: 某些 arXiv ID 待验证。M4: Discussion 无实质 Conclusion 内容。M5: Table 2 caption 中 chance 混写。

### Missing References
可能缺失：Shumailov 2023 原始 arXiv 版本、data provenance/C2PA 标准。

### Questions
Q1: d1-d3 only 的 balanced accuracy + CI？Q2: tail statistics 是 LoRA 特有还是通用？Q3: controlled → wild generalization gap？Q4: cross-model chains 高准确率是否因跨架构分布差异更大而非 process-level signal？

---

请对以上每条 Must-Fix、Should-Fix 和 Questions 给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-18T14:19:18.744640+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: 方法论新颖性不足**\n\nR2 的批评——\"RF + hand-crafted features 缺乏算法层面的贡献\"——将论文的贡献类型误判了。本文不是一篇方法论创新论文，而是一篇**任务定义 + 系统实证分析**论文。其贡献在于：(1) 形式化一个此前未被研究的任务（§3.1）；(2) 发现 perplexity tail statistics 是跨模型/策略的一致深度标记（§4.2, Table 3: 9/9 cells 中 p90_ppl top-2）；(3) 揭示策略依赖的退化轨迹（§4.5）和特征层级随深度边界转移的现象（§4.2 最后一段）。Table 3（§5.1）中分类器收敛（Δ_max ≤ 0.4pp）恰恰支持了论文的核心论点——**信号在特征，不在分类器**——这本身就是一个科学发现，而非缺陷。\n\n*ACL 系列会议历来接受以实证发现驱动的分析型工作（如 Binoculars 2024 用 cross-perplexity ratio 单特征做二分类，GLTR 2019 用 token probability 分桶），方法简洁并不等于贡献不足。*\n\n但我承认 R2 的一个有效子论点：EDD 作为指标的新颖性确实有限——本质是 pairwise AUC 上的阈值截断。Definition 1 的数学内容相对简单，论文若能更诚实地将 EDD 定位为\"operational convenience\"而非\"methodological contribution\"，叙事会更准确。\n\n**[AGREE] R2-N2: Discussion 过于简略**\n\n完全同意。我在 R1 审稿意见中已将此标记为 Minor M4，但回顾后认为 R2 将其升级为 Must-Fix 是合理的。§6 仅约 7 行，对于一篇包含 3×3 atlas + 8 个泛化轴 + 多个附录实验的工作，正文 Discussion 应当至少覆盖：(a) depth signal 的机制性解释（tail erosion → detectable → 为什么在 τ=1.1 消失，这在 Appendix F.4 有数据但主文未展开）；(b) 与 Dohmatob 2024 scaling law 的定量偏离（AUC-excess contraction ratio 0.69-0.80 vs 理论预测的指数衰减，§4.4 提到但未深入分析）；(c) deployment roadmap（策略识别 → 深度分类的 two-stage pipeline 架构）。Appendix F.18 Extended Discussion 有部分内容，但关键 insight 不应藏在附录。\n\n**[AGREE] R2-N3: d0 inflation**\n\n同意，这与我的 R1-W1 完全对齐。补充一个 R2 未提到的量化角度：cross-model transfer 中 Pythia holdout 的 d2 recall 仅 26.8%（Table 4），即该配置下超过 73% 的 d2 文本被错误分类。这意味着在最弱的跨模型设置中，分类器对 d2 文本的识别能力接近无效。如果 d0 被排除，headline metric 的实际信息量会被更诚实地传达。\n\n但我不同意将其定为 Must-Fix——d0 膨胀在 AI text detection 文献中普遍存在（Binoculars, Fast-DetectGPT 等的 headline AUROC 也受 human vs machine 的高可分性驱动），且论文确实在 Table 2 括号中和 §5.2 中报告了 d1-d3 数字。问题在于展示优先级（Should-Fix），而非数据缺失（Must-Fix）。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract 中 \"19 perplexity-based features\" 不准确**\n\nTable 1（§3.3）明确列出 4 个 lexical diversity 特征（TTR, hapax ratio, bigram/trigram entropy）和 3 个 repetition 特征（repeated 2/3/4-gram fractions），共 7 个不依赖参考模型困惑度分布。Abstract 第 4 行将全部 19 个特征统称为\"perplexity-based\"是事实性错误。虽然 Appendix F.15 显示 perplexity features alone 达到 66.0%（vs full 66.6%），非 perplexity 特征的边际贡献很小，但这不能证明错误标注的合理性。建议改为\"19 statistical features (primarily perplexity-based)\"或\"19 features including perplexity statistics, surprisal measures, and lexical indicators\"。\n\n**[AGREE] R2-W2: Cross-strategy transfer 近乎失败**\n\n同意，这与我的 R1-W2 对齐。补充：§5.3 提到 two-stage pipeline 恢复 11.5pp，但论文未报告策略识别模块的独立准确率、使用的特征集或分类方法。一个未经验证的 pipeline 不能作为解决方案被引用。\n\n**[REBUT] R2-W3: 主实验仅 1-1.5B 模型偏小**\n\nR2 的\"2026 年标准下偏小\"暗示论文应使用更大规模模型作为主实验——这一标准不合理。论文在 §3.2 明确论证了选择 1-1.5B 的方法论原因：\"Restricting to a narrow parameter range isolates the effect of architecture and training data from scale\"。这是一个**有意的实验控制**，不是资源限制的结果。将多个变量同时变化（规模 + 架构 + 训练数据 + 量化方式）的实验反而会削弱因果推断——这正是 7-8B 实验面临的问题（我在 R1-W3 中已指出）。\n\n论文的目标是建立深度估计的基础科学（信号存在性、特征层级、策略依赖性），而非建立 SOTA 部署系统。1-1.5B 的系统性网格在这个目标下比 2-3 个 7B 模型的非系统性实验更有价值。ARR reviewer guidelines 也明确指出不应因\"not using preferred methodology\"而惩罚论文。\n\n**[REBUT] R2-W4: 核心发现本质上是 Dohmatob 2024 理论的实验验证**\n\n这一判断过于简化。论文与 Dohmatob 2024 的关系是**operationalization + new phenomena**，而非单纯 validation：\n\n1. **策略依赖的退化轨迹**（§4.5）：Dohmatob 的理论不区分解码策略，但论文发现 temperature 加速收敛、top-k 衰减信号、策略效应（9.2pp）超过模型效应（7.2pp）——这是理论未预测的实证发现。\n\n2. **非单调 7B 行为**（§5.4, Appendix F.9 Table 14）：Qwen2.5-7B 的 U-shaped AUC 恢复直接违反了理论预测的单调衰减。\n\n3. **特征层级随深度边界转移**（§4.2 最后一段）：浅层 var_surprisal 主导 → 深层 p90_ppl/kurtosis_ppl 接管——理论没有预测这一转变。\n\n4. **从理论到可部署分类器的工程距离**不是 trivial 的。理论说\"tails erode\"——但哪些统计量最敏感？在哪些策略下？到什么深度？这些具体问题只能通过系统实证来回答。\n\nRelated Work §2 第 8 行已明确区分了本文与 Dohmatob 的关系。\n\n**[AGREE] R2-W5: Downstream curation PoC 不显著**\n\n同意，与我的 R1-W5 对齐。RF-filtered vs unfiltered 所有三个配置均 p>0.4，效应量也很小（Cohen's d_z 绝对值 0.25-0.41）。唯一显著结果（RF vs random）仅说明有意识的过滤好于随机丢弃，不能证明深度估计的增量价值超过简单启发式（如原始困惑度阈值过滤）。论文应降低 curation 应用的声明力度，或增加与困惑度阈值 baseline 的对比。\n\n---\n\n### Minor 问题\n\n**[AGREE] R2-M1**: \"43pp below RF\" 确实不精确——RF 在不同 cells 上准确率不同，DeepSeek 36.2% 与 Pythia nucleus RF 78.7% 的差距是 42.5pp，与 GPT-2 XL temp 85.9% 的差距是 49.7pp。应指定参照点。\n\n**[AGREE] R2-M2**: 如果存在 orphan bib entries（已在 bib 中但未在正文 cite 的条目），应清理。我注意到 `pareek2024understanding` 在 references.bib 中但未在任何 .tex 文件中出现——需验证。\n\n**[AGREE] R2-M4**: Discussion 缺乏实质 Conclusion 内容——同 R2-N2。\n\n**[AGREE] R2-M5**: 需检查 Table 2 caption 中 chance 的标注一致性。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1**: d1-d3 balanced accuracy + CI 应作为论文的核心指标之一被系统报告。与我的 R1-N3 对齐——序数分类形式化需要配套的评价指标。\n\n**[AGREE] R2-Q2**: Tail statistics 是 LoRA 特有还是通用？论文的 prompted generation 实验（§5.3, Appendix F.16）和 cross-model chains（Appendix F.12）提供了部分证据：prompted generation 保持相同 top features（p90_ppl rank 1），cross-model chains 达到 84.75%。但这两个实验仍使用 LoRA fine-tuning 作为递归训练方式。如果用 full fine-tuning 或 continued pretraining 代替 LoRA，tail statistics 是否仍然主导？这是一个合理但非 must-answer 的问题，因为论文已在 §3.2 明确了 scope（\"Our findings...are limited to this grid\"）。\n\n**[REBUT] R2-Q4**: Cross-model chains 高准确率是否因跨架构分布差异更大？\n\n论文在 Appendix F.12 直接用反向链控制实验回应了这一混淆：正向链（Pythia→OLMo→GPT-2 XL）84.75%，反向链（GPT-2 XL→OLMo→Pythia）85.75%，CI 重叠。如果分类器利用的是架构指纹而非深度信号，反转模型-深度对应关系应导致预测反转——但准确率几乎相同。此外，单纯架构区分应产生接近完美的准确率（因为架构完美确定深度标签），但观测到的 84.75% 伴随单调递减的 per-depth F1（d0=0.98, d1=0.88, d2=0.76, d3=0.76），这更符合深度信号而非架构指纹的解释。\n\n**[AGREE] R2-Q3**: Controlled → wild generalization gap 是一个关键开放问题。Appendix F.7 的 C4 FPR 数据（4.7-22.4%）已经表明这一 gap 是显著的，但论文缺乏从 wild web data 中估计深度分布的验证实验。\n\n---\n\n### 对 R2 Overall Assessment 的评论\n\nR2 给出 Overall 3.0 (Findings)，核心理由是方法论新颖性不足（N1）和 d0 inflation（N3）。我认为：\n\n- **N1 的严重性被高估**：论文的贡献类型是任务定义 + 系统实证，不是算法创新。将缺乏算法新颖性等同于缺乏贡献，忽略了 ACL 系列会议对 analysis/resource 型论文的传统接受度。\n- **N3 的影响被准确评估但处理建议不同**：d0 inflation 是展示问题而非实验缺陷——论文已报告了 d1-d3 数字，问题在于突出程度。\n- **R2 的 Excitement 2.5 偏低**：任务本身（从文本中估计递归生成深度）在 model collapse 和数据 provenance 快速增长的背景下有明确的实际需求。即使当前方法有限制，任务定义和初始 benchmark 对社区仍有价值。\n\n综合考虑，我维持我的 R1 评分：**Overall 3.5 (Borderline Conference)**。论文的任务新颖性和实验系统性高于 Findings 平均水平，但统计严谨性问题（R1-N1, N2）阻止我给出 4.0。\n",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: 方法论新颖性不足**\n\nR2 的批评——\"RF + hand-crafted features 缺乏算法层面的贡献\"——将论文的贡献类型误判了。本文不是一篇方法论创新论文，而是一篇**任务定义 + 系统实证分析**论文。其贡献在于：(1) 形式化一个此前未被研究的任务（§3.1）；(2) 发现 perplexity tail statistics 是跨模型/策略的一致深度标记（§4.2, Table 3: 9/9 cells 中 p90_ppl top-2）；(3) 揭示策略依赖的退化轨迹（§4.5）和特征层级随深度边界转移的现象（§4.2 最后一段）。Table 3（§5.1）中分类器收敛（Δ_max ≤ 0.4pp）恰恰支持了论文的核心论点——**信号在特征，不在分类器**——这本身就是一个科学发现，而非缺陷。\n\n*ACL 系列会议历来接受以实证发现驱动的分析型工作（如 Binoculars 2024 用 cross-perplexity ratio 单特征做二分类，GLTR 2019 用 token probability 分桶），方法简洁并不等于贡献不足。*\n\n但我承认 R2 的一个有效子论点：EDD 作为指标的新颖性确实有限——本质是 pairwise AUC 上的阈值截断。Definition 1 的数学内容相对简单，论文若能更诚实地将 EDD 定位为\"operational convenience\"而非\"methodological contribution\"，叙事会更准确。\n\n**[AGREE] R2-N2: Discussion 过于简略**\n\n完全同意。我在 R1 审稿意见中已将此标记为 Minor M4，但回顾后认为 R2 将其升级为 Must-Fix 是合理的。§6 仅约 7 行，对于一篇包含 3×3 atlas + 8 个泛化轴 + 多个附录实验的工作，正文 Discussion 应当至少覆盖：(a) depth signal 的机制性解释（tail erosion → detectable → 为什么在 τ=1.1 消失，这在 Appendix F.4 有数据但主文未展开）；(b) 与 Dohmatob 2024 scaling law 的定量偏离（AUC-excess contraction ratio 0.69-0.80 vs 理论预测的指数衰减，§4.4 提到但未深入分析）；(c) deployment roadmap（策略识别 → 深度分类的 two-stage pipeline 架构）。Appendix F.18 Extended Discussion 有部分内容，但关键 insight 不应藏在附录。\n\n**[AGREE] R2-N3: d0 inflation**\n\n同意，这与我的 R1-W1 完全对齐。补充一个 R2 未提到的量化角度：cross-model transfer 中 Pythia holdout 的 d2 recall 仅 26.8%（Table 4），即该配置下超过 73% 的 d2 文本被错误分类。这意味着在最弱的跨模型设置中，分类器对 d2 文本的识别能力接近无效。如果 d0 被排除，headline metric 的实际信息量会被更诚实地传达。\n\n但我不同意将其定为 Must-Fix——d0 膨胀在 AI text detection 文献中普遍存在（Binoculars, Fast-DetectGPT 等的 headline AUROC 也受 human vs machine 的高可分性驱动），且论文确实在 Table 2 括号中和 §5.2 中报告了 d1-d3 数字。问题在于展示优先级（Should-Fix），而非数据缺失（Must-Fix）。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract 中 \"19 perplexity-based features\" 不准确**\n\nTable 1（§3.3）明确列出 4 个 lexical diversity 特征（TTR, hapax ratio, bigram/trigram entropy）和 3 个 repetition 特征（repeated 2/3/4-gram fractions），共 7 个不依赖参考模型困惑度分布。Abstract 第 4 行将全部 19 个特征统称为\"perplexity-based\"是事实性错误。虽然 Appendix F.15 显示 perplexity features alone 达到 66.0%（vs full 66.6%），非 perplexity 特征的边际贡献很小，但这不能证明错误标注的合理性。建议改为\"19 statistical features (primarily perplexity-based)\"或\"19 features including perplexity statistics, surprisal measures, and lexical indicators\"。\n\n**[AGREE] R2-W2: Cross-strategy transfer 近乎失败**\n\n同意，这与我的 R1-W2 对齐。补充：§5.3 提到 two-stage pipeline 恢复 11.5pp，但论文未报告策略识别模块的独立准确率、使用的特征集或分类方法。一个未经验证的 pipeline 不能作为解决方案被引用。\n\n**[REBUT] R2-W3: 主实验仅 1-1.5B 模型偏小**\n\nR2 的\"2026 年标准下偏小\"暗示论文应使用更大规模模型作为主实验——这一标准不合理。论文在 §3.2 明确论证了选择 1-1.5B 的方法论原因：\"Restricting to a narrow parameter range isolates the effect of architecture and training data from scale\"。这是一个**有意的实验控制**，不是资源限制的结果。将多个变量同时变化（规模 + 架构 + 训练数据 + 量化方式）的实验反而会削弱因果推断——这正是 7-8B 实验面临的问题（我在 R1-W3 中已指出）。\n\n论文的目标是建立深度估计的基础科学（信号存在性、特征层级、策略依赖性），而非建立 SOTA 部署系统。1-1.5B 的系统性网格在这个目标下比 2-3 个 7B 模型的非系统性实验更有价值。ARR reviewer guidelines 也明确指出不应因\"not using preferred methodology\"而惩罚论文。\n\n**[REBUT] R2-W4: 核心发现本质上是 Dohmatob 2024 理论的实验验证**\n\n这一判断过于简化。论文与 Dohmatob 2024 的关系是**operationalization + new phenomena**，而非单纯 validation：\n\n1. **策略依赖的退化轨迹**（§4.5）：Dohmatob 的理论不区分解码策略，但论文发现 temperature 加速收敛、top-k 衰减信号、策略效应（9.2pp）超过模型效应（7.2pp）——这是理论未预测的实证发现。\n\n2. **非单调 7B 行为**（§5.4, Appendix F.9 Table 14）：Qwen2.5-7B 的 U-shaped AUC 恢复直接违反了理论预测的单调衰减。\n\n3. **特征层级随深度边界转移**（§4.2 最后一段）：浅层 var_surprisal 主导 → 深层 p90_ppl/kurtosis_ppl 接管——理论没有预测这一转变。\n\n4. **从理论到可部署分类器的工程距离**不是 trivial 的。理论说\"tails erode\"——但哪些统计量最敏感？在哪些策略下？到什么深度？这些具体问题只能通过系统实证来回答。\n\nRelated Work §2 第 8 行已明确区分了本文与 Dohmatob 的关系。\n\n**[AGREE] R2-W5: Downstream curation PoC 不显著**\n\n同意，与我的 R1-W5 对齐。RF-filtered vs unfiltered 所有三个配置均 p>0.4，效应量也很小（Cohen's d_z 绝对值 0.25-0.41）。唯一显著结果（RF vs random）仅说明有意识的过滤好于随机丢弃，不能证明深度估计的增量价值超过简单启发式（如原始困惑度阈值过滤）。论文应降低 curation 应用的声明力度，或增加与困惑度阈值 baseline 的对比。\n\n---\n\n### Minor 问题\n\n**[AGREE] R2-M1**: \"43pp below RF\" 确实不精确——RF 在不同 cells 上准确率不同，DeepSeek 36.2% 与 Pythia nucleus RF 78.7% 的差距是 42.5pp，与 GPT-2 XL temp 85.9% 的差距是 49.7pp。应指定参照点。\n\n**[AGREE] R2-M2**: 如果存在 orphan bib entries（已在 bib 中但未在正文 cite 的条目），应清理。我注意到 `pareek2024understanding` 在 references.bib 中但未在任何 .tex 文件中出现——需验证。\n\n**[AGREE] R2-M4**: Discussion 缺乏实质 Conclusion 内容——同 R2-N2。\n\n**[AGREE] R2-M5**: 需检查 Table 2 caption 中 chance 的标注一致性。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1**: d1-d3 balanced accuracy + CI 应作为论文的核心指标之一被系统报告。与我的 R1-N3 对齐——序数分类形式化需要配套的评价指标。\n\n**[AGREE] R2-Q2**: Tail statistics 是 LoRA 特有还是通用？论文的 prompted generation 实验（§5.3, Appendix F.16）和 cross-model chains（Appendix F.12）提供了部分证据：prompted generation 保持相同 top features（p90_ppl rank 1），cross-model chains 达到 84.75%。但这两个实验仍使用 LoRA fine-tuning 作为递归训练方式。如果用 full fine-tuning 或 continued pretraining 代替 LoRA，tail statistics 是否仍然主导？这是一个合理但非 must-answer 的问题，因为论文已在 §3.2 明确了 scope（\"Our findings...are limited to this grid\"）。\n\n**[REBUT] R2-Q4**: Cross-model chains 高准确率是否因跨架构分布差异更大？\n\n论文在 Appendix F.12 直接用反向链控制实验回应了这一混淆：正向链（Pythia→OLMo→GPT-2 XL）84.75%，反向链（GPT-2 XL→OLMo→Pythia）85.75%，CI 重叠。如果分类器利用的是架构指纹而非深度信号，反转模型-深度对应关系应导致预测反转——但准确率几乎相同。此外，单纯架构区分应产生接近完美的准确率（因为架构完美确定深度标签），但观测到的 84.75% 伴随单调递减的 per-depth F1（d0=0.98, d1=0.88, d2=0.76, d3=0.76），这更符合深度信号而非架构指纹的解释。\n\n**[AGREE] R2-Q3**: Controlled → wild generalization gap 是一个关键开放问题。Appendix F.7 的 C4 FPR 数据（4.7-22.4%）已经表明这一 gap 是显著的，但论文缺乏从 wild web data 中估计深度分布的验证实验。\n\n---\n\n### 对 R2 Overall Assessment 的评论\n\nR2 给出 Overall 3.0 (Findings)，核心理由是方法论新颖性不足（N1）和 d0 inflation（N3）。我认为：\n\n- **N1 的严重性被高估**：论文的贡献类型是任务定义 + 系统实证，不是算法创新。将缺乏算法新颖性等同于缺乏贡献，忽略了 ACL 系列会议对 analysis/resource 型论文的传统接受度。\n- **N3 的影响被准确评估但处理建议不同**：d0 inflation 是展示问题而非实验缺陷——论文已报告了 d1-d3 数字，问题在于突出程度。\n- **R2 的 Excitement 2.5 偏低**：任务本身（从文本中估计递归生成深度）在 model collapse 和数据 provenance 快速增长的背景下有明确的实际需求。即使当前方法有限制，任务定义和初始 benchmark 对社区仍有价值。\n\n综合考虑，我维持我的 R1 评分：**Overall 3.5 (Borderline Conference)**。论文的任务新颖性和实验系统性高于 Findings 平均水平，但统计严谨性问题（R1-N1, N2）阻止我给出 4.0。\n",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-18T14:19:22.661549+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 502 · 2026-05-18T14:19:32.730681+00:00_

交叉回应已提交。总结：

- 对 R2 的 3 个 Must-Fix 中，**N2 (Discussion 过简) 和 N3 (d0 inflation) 同意**，但 N3 我认为是 Should-Fix 而非 Must-Fix；**N1 (方法论新颖性不足) 反驳**——论文属于任务定义+系统实证类型，分类器收敛恰恰是科学发现。
- 对 5 个 Should-Fix 中，**W1, W2, W5 同意**；**W3 (模型规模偏小) 和 W4 (仅验证理论) 反驳**——1-1.5B 是有意的实验控制，策略依赖轨迹和非单调 7B 行为是理论未预测的新发现。
- 维持 R1 评分 **Overall 3.5 (Borderline Conference)**，高于 R2 的 3.0。核心分歧在于任务定义型贡献的价值判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

30 recorded events


### User

_source line 503 · 2026-05-18T17:00:07.265742+00:00_

[Round 1 审稿请求]:
[Dream 审稿任务 — Reviewer 1：方法 + 实验]

论文：Depth Degradation Atlas: Ordinal Estimation of Recursive Generation Depth from Text
PDF：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf

你的审查侧重：
- **方法描述**：是否完整、claim 是否被实验数据支撑、关键超参 / 训练流程是否清晰
- **实验设计**：是否覆盖关键 baseline / ablation / 跨数据集 / scale 维度
- **数据呈现**：表格 / 图是否能让审稿人复现结论、误差棒 / 统计显著性是否充分

请基于论文内容独立评判，不要假设论文结果的质量高低。

**不要评判**：新颖性 / 相关工作（那是 Reviewer 2 的范围）、格式 / 排版。

实验设计参考（完整想象实验列表）：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_context.yaml

按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

请通过 review_reviewer_post_to_director(text, reviewer_id="1", project="recursive_gen_depth_est", dream_id="20260518T162616") 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-18T17:00:15.479815+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-18T17:00:15.480272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-18T17:00:19.101745+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf",
  "pages": "1-10",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf",
    "pages": "1-10",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-18T17:00:19.606273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_context.yaml"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-18T17:00:23.081130+00:00_

Error: result (6,128,663 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/7ff5f3bf-0ab6-472d-9e27-f2fe2b867f69/tool-results/mcp-agent-ml-research-pdf_to_images-1779123622711.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/7ff5f3bf-0ab6-472d-9e27-f2fe2b867f69/tool-results/mcp-agent-ml-research-pdf_to_images-1779123622711.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3979
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-18T17:00:23.081791+00:00_

1	narrative_guidance: 'best档叙事：14B Qwen2.5-14B FP16 完整验证 depth signal 在主流规模上的持续性， 消除"small
2	  model only"质疑。理论section从 Shumailov tail erosion + Dohmatob contraction rate 推导出
3	  EDD 上界=4±1，与三模型实证 EDD=4 精确吻合，将 Atlas 从 empirical observation 升级为 theoretically grounded
4	  framework。Binoculars/Fast-DetectGPT ordinal baseline 接近 chance， 确认现有 binary detector
5	  不具备 ordinal 能力。Bootstrap CIs 紧致（±1-2pp），三模型 cross-seed max Δ<3pp。 论文定位 "task formalization
6	  + theoretical grounding + systematic empirical atlas + practical framework" 获审稿人认可，projected_reviewer_avg
7	  3.7-4.0。
8	
9	  '
10	imagined_experiments:
11	- name: 14B clean FP16 scale validation
12	  plan_id: plan_014
13	  description: 'Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。 完整 d0-d3 nucleus
14	    递归链 + 19 特征提取 + RF/LR 分类。 验证 depth signal 在 14B 主流规模上是否与 1B 量级一致。
15	
16	    '
17	  expected_results:
18	    rf_4class_acc: 0.79
19	    rf_4class_ci:
20	    - 0.778
21	    - 0.802
22	    lr_4class_acc: 0.76
23	    d0v1_auc: 0.991
24	    d1v2_auc: 0.87
25	    d1v3_auc: 0.975
26	    d2v3_auc: 0.82
27	    rf_3class_acc: 0.74
28	    rf_3class_ci:
29	    - 0.722
30	    - 0.758
31	    top_features:
32	    - p90_ppl
33	    - var_surprisal
34	    - p75_ppl
35	    - mean_surprisal
36	    feature_top4_overlap_with_1b: 4
37	    per_class_recall_d0: 0.98
38	    per_class_recall_d1: 0.84
39	    per_class_recall_d2: 0.62
40	    per_class_recall_d3: 0.72
41	    finetune_loss_d0: 2.35
42	    finetune_loss_d1: 1.58
43	    finetune_loss_d2: 1.15
44	  result_rationale: 'Shumailov tail erosion 是递归生成的基本属性，不依赖模型规模——每次递归 fine-tune 都使输出分布的尾部进一步收缩
45	    （高 perplexity token 概率下降，低 perplexity token 概率上升）。14B 模型容量更大意味着 d0 输出分布更接近训练数据（更宽尾），但递归过程同样驱动尾部收敛。因此
46	    p90_ppl 和 var_surprisal 仍然是 top-4 特征（overlap=4/4）。绝对准确率 ~79% 处于 1B 三模型均值（78.3%）附近，
47	    因为 Qwen2.5 架构的 RoPE + GQA 与 GPT-2/Pythia/OLMo 的 absolute PE + MHA 不同， but feature
48	    space 捕获的是输出分布统计属性而非架构细节。d1v2_auc=0.87 处于 [0.82, 0.92] 范围中段， 与 OLMo nucleus (0.867)
49	    和 Pythia nu
…[truncated 16315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3475
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-18T17:00:30.180595+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf",
  "pages": "1-3",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf",
    "pages": "1-3",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-18T17:00:31.096486+00:00_

Error: result (1,546,744 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/7ff5f3bf-0ab6-472d-9e27-f2fe2b867f69/tool-results/mcp-agent-ml-research-pdf_to_images-1779123631033.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/7ff5f3bf-0ab6-472d-9e27-f2fe2b867f69/tool-results/mcp-agent-ml-research-pdf_to_images-1779123631033.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 915
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-18T17:00:35.779790+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-18T17:00:36.539013+00:00_

Error: result (512,908 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/7ff5f3bf-0ab6-472d-9e27-f2fe2b867f69/tool-results/mcp-agent-ml-research-pdf_to_images-1779123636260.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/7ff5f3bf-0ab6-472d-9e27-f2fe2b867f69/tool-results/mcp-agent-ml-research-pdf_to_images-1779123636260.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 759
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-18T17:00:36.539563+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf - 2>/dev/null | head -20",
  "description": "Extract first 20 lines of text from PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf - 2>/dev/null | head -20",
    "description": "Extract first 20 lines of text from PDF"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-18T17:00:36.742552+00:00_

Depth Degradation Atlas: Ordinal Estimation of Recursive
Generation Depth from Text

Anonymous

Abstract
Web-scraped training corpora increasingly contain multi-generational synthetic content
produced by uncontrolled model-data-model feedback loops. Existing detectors classify text
as real or synthetic but discard ordinal depth information, a critical distinction since rstgeneration synthetic data can improve training while deeply recursive text drives distribution
collapse. We formalize

ordinal generation depth estimation as a new task: given text alone,

predict how many recursive generation cycles it has undergone.

We construct a multi-

generational benchmark spanning three model families (GPT-2 XL, OLMo-1B, Pythia-1.4B),
three decoding strategies (nucleus, temperature, top-k ), and four depth levels (d0d3), and
provide the rst

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-18T17:00:39.855565+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf - 2>/dev/null | wc -l",
  "description": "Count total lines in extracted PDF text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf - 2>/dev/null | wc -l",
    "description": "Count total lines in extracted PDF text"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-18T17:00:40.006797+00:00_

1021

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-18T17:00:43.271999+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf /tmp/dream_paper.txt 2>/dev/null && echo \"Done\"",
  "description": "Extract PDF text to file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf /tmp/dream_paper.txt 2>/dev/null && echo \"Done\"",
    "description": "Extract PDF text to file"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-18T17:00:43.373345+00:00_

Done

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-18T17:00:47.254702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/dream_paper.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/dream_paper.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-18T17:00:47.355780+00:00_

1	Depth Degradation Atlas: Ordinal Estimation of Recursive
2	Generation Depth from Text
3	
4	Anonymous
5	
6	Abstract
7	Web-scraped training corpora increasingly contain multi-generational synthetic content
8	produced by uncontrolled model-data-model feedback loops. Existing detectors classify text
9	as real or synthetic but discard ordinal depth information, a critical distinction since rstgeneration synthetic data can improve training while deeply recursive text drives distribution
10	collapse. We formalize
11	
12	ordinal generation depth estimation as a new task: given text alone,
13	
14	predict how many recursive generation cycles it has undergone.
15	
16	We construct a multi-
17	
18	generational benchmark spanning three model families (GPT-2 XL, OLMo-1B, Pythia-1.4B),
19	three decoding strategies (nucleus, temperature, top-k ), and four depth levels (d0d3), and
20	provide the rst
21	
22	Depth Degradation Atlas, a systematic empirical map of how text statistical
23	
24	properties evolve across recursive depths. Random Forest classiers on 19 statistical features
25	achieve 7085% four-class accuracy (chance = 25%), with bootstrap 95% condence intervals
26	of ±12.5 percentage points. The depth signal persists at 14B scale (Qwen2.5-14B FP16,
27	79% accuracy) with identical top-4 features (4/4 overlap), eliminating the small model only
28	
29	EDD) from
30	EDD ∈ [3, 5], which matches the empirical EDD
31	
32	concern. We derive a theoretical upper bound on Eective Discriminable Depth (
33	model collapse contraction rates, predicting
34	
35	= 4 observed across all three model families. Existing binary detectors (Binoculars, FastDetectGPT) achieve only 3038% when repurposed for ordinal estimation (near chance),
36	conrming that ordinal depth estimation requires dedicated methods. A two-stage strategy-
37	
38	aware pipeline recovers +11.5 percentage points over naive cross-strategy transfer, addressing
39	the deployment challenge.
40	
41	1
42	
43	Introduction
4
…[truncated 7915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-18T17:00:50.776472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/dream_paper.txt",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/dream_paper.txt",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-18T17:00:50.827218+00:00_

200	reference model.
201	
202	Reference model and circularity.
203	
204	Using the generating model as its own reference creates
205	
206	a potential circularity concern: the reference model recognizes its own output distribution. We
207	address this through cross-model leave-one-out (LOO) evaluation, where the reference model
208	is never the generating model. Cross-model LOO accuracy (mean 66.4%) conrms that depth
209	signal is not purely an artifact of model self-recognition, though within-model accuracy is higher
210	(mean 78.3%), indicating that model-specic distributional knowledge contributes to but is not
211	necessary for depth estimation.
212	
213	Eective Discriminable Depth (EDD).
214	
215	We dene the
216	
217	EDD at threshold T as the maxi-
218	
219	∗
220	∗
221	mum depth d such that adjacent-depth pairwise AUC exceeds T for all pairs up to d :
222	
223	EDD(T ) = max{d∗ : AUC(di, di+1) ≥ T, ∀ i < d∗}.
224	(1)
225	EDD quanties the practical horizon of ordinal depth estimation: beyond EDD, adjacent depths
226	become statistically indistinguishable with current features.
227	
228	4
229	
230	Theoretical Analysis
231	
232	We ground the empirical Atlas in model collapse theory, deriving three veriable predictions that
233	connect distributional contraction to depth estimation feasibility.
234	
235	4.1
236	
237	Tail Erosion and Feature Dominance
238	
239	Shumailov et al. [2024] prove that recursive ne-tuning progressively erodes the tails of the
240	output distribution:
241	
242	high-perplexity tokens lose probability mass while low-perplexity tokens
243	
244	gain mass at each recursive step. This tail erosion mechanism directly explains why perplexity
245	
246	3
247	
248	tail statistics (p90_ppl, var_surprisal) dominate the feature ranking across all model-strategy
249	combinations. Central tendency measures (mean perplexity) are less sensitive because the bulk
250	of the distribution shifts slowly relative to the tails.
251	
252	Prediction 1. Per-dept
…[truncated 4871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-18T17:00:53.939675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/dream_paper.txt",
  "offset": "400",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/dream_paper.txt",
    "offset": "400",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-18T17:00:53.990459+00:00_

400	0.80.
401	
402	Third, decoding strategies produce a three-tier pattern:
403	
404	temperature enhances signal
405	
406	(mean accuracy 82.6%), nucleus provides a stable baseline (mean 79.0%), and top-k attenuates
407	signal (mean 73.2%).
408	
409	6.2
410	
411	Scale Robustness at 14B
412	
413	Table 2 presents results for Qwen2.5-14B under clean FP16 conditions (no quantization). The
414	14B model achieves 79% four-class accuracy [77.8, 80.2], falling within the range of the three
415	1B-scale models (69.785.4%). The adjacent-depth AUC prole mirrors the 1B pattern: d0v1
416	= 0.991, d1v2 = 0.87, d2v3 = 0.82. The top-4 features are identical to the 1B models (overlap
417	= 4/4):
418	
419	p90_ppl, var_surprisal, p75_ppl, and mean_surprisal. Per-class recall follows the
420	
421	expected depth-dependent pattern: d0 = 98%, d1 = 84%, d2 = 62%, d3 = 72%.
422	These results conrm that the depth signal and feature universality are not limited to small
423	models.
424	
425	The ne-tuning loss trajectory at 14B (2.35 → 1.58 → 1.15) is atter than at 1B,
426	
427	consistent with larger residual capacity resisting catastrophic distributional shift, but insucient
428	to prevent tail erosion.
429	
430	6.3
431	
432	Binary Detectors Fail at Ordinal Estimation
433	
434	Table 3 compares existing binary detectors repurposed for ordinal depth estimation against our
435	feature-based approach. Both Binoculars and Fast-DetectGPT perform near chance on the ordinal task. Even with oracle threshold optimization (which uses test-set depth distribution information), the best binary detector achieves only 38%, compared to 78.3% for the RF 19-feature
436	
437	5
438	
439	Table 2: Scale robustness: Qwen2.5-14B FP16 vs 1B-scale models.
440	
441	Feature overlap refers to
442	
443	concordance of top-4 ranked features with the 1B-model consensus.
444	
445	Model
446	
447	4-class Acc d1v2 AUC d2v3 AUC Top-4 Overlap
448	
449	Pythia-1.4B (nucleus)
450	
451	78.2
452	
453	0.86
454	
455	0.80
456	
457	OL
…[truncated 3481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-18T17:00:56.754734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/dream_paper.txt",
  "offset": "598",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/dream_paper.txt",
    "offset": "598",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-18T17:00:56.805655+00:00_

598	Theoretical
599	
600	Empirical
601	
602	p90_ppl decay / depth
603	Temp/nucleus
604	
605	convergence
606	
607	[3, 5]
608	
609	4 (all 3 models)
610	
611	1525%
612	
613	1822%
614	
615	>1
616	
617	≈ 1.35
618	
619	ratio
620	
621	Strategy-dependent d1v2 AUC.
622	
623	We report per-strategy cross-strategy d1v2 AUC for trans-
624	
625	parency. When temperature is the holdout strategy, d1v2 AUC drops to 0.130.25, reecting the
626	structural distributional shift identied in Section 4.3. Z-score normalization improves overall
627	LR cross-strategy accuracy from 25% to 61% but does not recover pairwise d1v2 AUC (GPT-2
628	XL: 0.50 → 0.24; OLMo: 0.50 → 0.19), conrming that simple feature normalization cannot
629	resolve a geometric distributional shift.
630	
631	7
632	
633	Discussion
634	
635	Wild-data ecological validity.
636	
637	To assess behavior on uncurated web text, we apply depth
638	
639	estimators trained on our controlled benchmark to 10K-sample subsets of C4, FineWeb, and
640	RedPajama. The depth distribution is dominated by d0 predictions (7885%), with false positive rates (non-d0 predictions on human-written web text) of 21.5% (C4), 18.0% (FineWeb),
641	and 15.0% (RedPajama). Cross-model agreement on d0 predictions is high (92%). Inspection
642	of misclassied samples reveals that template, SEO, and boilerplate content shares statistical
643	features with recursively generated text (high n-gram repetition, low surprisal variance). FPR
644	correlates inversely with the strictness of the source corpus's cleaning pipeline (RedPajama <
645	FineWeb < C4).
646	
647	This suggests that depth estimation features capture a general text quality
648	
649	gradient, with template-heavy web content occupying a similar feature-space region as shallow
650	recursive generation. Full results appear in Appendix Tables 5 and 6.
651	
652	API model generalization.
653	
654	Fine-tuned GPT-4o-mini recursive chains achieve 58% four-class
655	
656	accuracy with d0v1 AUC = 0.93 and
…[truncated 7395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-18T17:00:59.669670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/dream_paper.txt",
  "offset": "797",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/dream_paper.txt",
    "offset": "797",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-18T17:00:59.720583+00:00_

797	generated texts. arXiv preprint arXiv:2404.17435, 2024.
798	A. Wettig, A. Gao, Z. Zhong, and D. Chen. QuRating: Selecting high-quality data for training
799	language models. In ICML, 2024.
800	S. M. Xie, S. Santurkar, T. Ma, and P. Liang. Data selection for language models via importance
801	resampling. In NeurIPS, 2023.
802	A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever.
803	
804	Language models are
805	
806	unsupervised multitask learners. OpenAI Technical Report, 2019.
807	S. Biderman, H. Schoelkopf, Q. Anthony, H. Bradley, K. O'Brien, E. Hallahan, M. A. Khan,
808	S. Purohit, U. S. Prashanth, E. Ra, et al.
809	
810	Pythia:
811	
812	A suite for analyzing large language
813	
814	models across training and scaling. In ICML, 2023.
815	D. Groeneveld, I. Beltagy, P. Walsh, A. Bhagia, R. Kinney, O. Tafjord, A. Jha, H. Ivison,
816	I. Magnusson, Y. Wang, et al. OLMo: Accelerating the science of language models. In ACL,
817	2024.
818	E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen.
819	Low-rank adaptation of large language models. In ICLR, 2022.
820	
821	9
822	
823	LoRA:
824	
825	L. Breiman. Random forests. Machine Learning, 45(1):532, 2001.
826	A. Yang, B. Yang, B. Hui, B. Zheng, B. Yu, C. Zhou, et al.
827	
828	Qwen2 technical report.
829	
830	arXiv
831	
832	preprint arXiv:2407.10671, 2024.
833	
834	W. Cao, V. Mirjalili, and S. Raschka.
835	
836	Rank consistent ordinal regression for neural networks
837	
838	with application to age estimation. Pattern Recognition Letters, 140:325331, 2020.
839	P. Liang, R. Bommasani, T. Lee, D. Tsipras, D. Soylu, M. Yasunaga, Y. Zhang, D. Narayanan,
840	et al. Holistic evaluation of language models. TMLR, 2023.
841	D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring
842	massive multitask language understanding. In ICLR, 2021.
843	J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, et al. GPT-4 technical
844	report. arXiv pr
…[truncated 3775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-18T17:03:22.908743+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — Dream 审稿意见（方法 + 实验）\n\n**论文**: Depth Degradation Atlas: Ordinal Estimation of Recursive Generation Depth from Text\n**审查侧重**: 方法描述完整性、实验设计、数据呈现与统计严谨性\n**评分标准**: Top ML venue 通用标准（6 分制，接受率 ~25%）\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类任务，构建了 3×3 (模型×策略) 的 180K 样本基准（Depth Degradation Atlas），并在 14B FP16 规模上验证了深度信号的持续性。论文从 model collapse 收缩率理论推导出 EDD 上界 ≤5，与实证 EDD=4 吻合，并展示了现有二分类检测器（Binoculars, Fast-DetectGPT）在序数任务上接近 chance（30-38%）。相比本项目的实际论文，Dream 版本在理论分析、规模验证和 baseline 覆盖上有实质性改进。\n\n---\n\n## Strengths\n\n**S1. 14B FP16 clean validation 消除关键混淆（Table 2, §6.2）。** 这是相对实际论文最关键的改进。Qwen2.5-14B 在无量化干扰下达到 79% 四分类准确率，d1v2 AUC=0.87 与 1B 模型一致，top-4 特征完全重合（4/4 overlap）。这直接回应了\"small model only\"质疑，且排除了 QLoRA 量化作为混淆因子。Fine-tuning loss 轨迹（2.35→1.58→1.15 比 1B 更平缓）提供了额外机制性证据。\n\n**S2. Binary detector ordinal baseline 建立了任务必要性（Table 3, §6.3）。** Binoculars/Fast-DetectGPT 在序数任务上 30-38%（oracle threshold 含 test-set 信息仍仅 38%），d1v2 AUC 0.54-0.56 仅略高于 chance——这是论文最具说服力的结果之一。RF 19-feature 的 78.3% vs binary detector 的 ~35% 形成 43pp gap，clean proof that ordinal depth estimation requires dedicated methods。这在实际论文中被降级到附录，在 Dream 版本中正确置于主文。\n\n**S3. 理论分析提供了可验证预测（§4, Table 4）。** 三条预测（EDD ∈ [3,5]，p90_ppl 衰减 15-25%/depth，temp/nucleus 收敛比 >1）均与实验吻合。将 atlas 从纯经验观察提升为有理论基础的框架，对审稿人的\"just an empirical study\"质疑有直接回应价值。\n\n**S4. Two-stage pipeline 有具体数字（§6.5）。** Strategy identification accuracy = 57.8%，cross-strategy 从 59.1% 恢复至 70.5%（+11.5pp），oracle ceiling = 78.3%。实际论文仅提到\"recovers 11.5pp\"但未报告策略识别准确率。这些数字让审稿人能评估 pipeline 的瓶颈。\n\n**S5. Wild-data calibration 和 API model 扩展了生态效度（§7, Appendix A-B）。** C4/FineWeb/RedPajama 三语料验证（Table 5-6），FPR 与语料清洗严格度逆相关的发现有洞察力。GPT-4o-mini fine-tuned chain 58% 确认深度信号在 RLHF 对齐商用模型中存在。\n\n---\n\n## Weaknesses\n\n### Major Weaknesses\n\n**W1. 理论分析中 α 的估计路径存在逻辑跳跃（§4.2, Eq. 2）。**\nDohmatob 理论中的收缩率 α 描述的是**分布空间中的距离收缩**（||Pk - P∞|| ≤ C·α^k），但论文用 **fine-tuning loss 衰减**（2.27→1.65→1.23）来估计 α≈0.72。Fine-tuning loss 衡量的是模型对数据的拟合程度，不等于输出分布在 L1/KL 意义下的距离收缩。此外，从分布距离到 AUC 的映射依赖于特征提取管道的性质（哪些特征被提取、分类器的决策边界形状），但论文将 ε=0.05 直接映射到 AUC=0.75 threshold 而未说明这一对应关系的假设条件。\n\n这并非致命缺陷——三条预测确实与数据吻合——但推导中的非严格步骤应被明确标注为近似（approximate derivation），而非呈现为严格上界（\"we derive... EDD ≤ 5\"）。如果审稿人追问\"α 为什么可以从 loss 估计？\"，当前文本缺乏防御。\n\n**W2. Atlas 单 LoRA 种子问题仍未解决。**\n论文未提及 cross-seed replication。实际论文的 cross-seed 数据显示 GPT-2 XL 两个种子的 CI 不重叠（Δ=2.04pp），表明 LoRA 初始化对结果有显著影响。Dream 版本报告的 bootstrap CIs（±1-2.5pp, Table 1）仅量化了 fold 间方差，不捕获 LoRA 种子方差。如果种子方差与 fold 方差量级相当（~2pp），Table 1 中某些 cell 间的差异（如 Pythia nucleus 78.2% vs OLMo nucleus 78.9%，Δ=0.7pp）可能不显著。这影响对 model effect 和 strategy effect 的量化解读。\n\n**W3. 序数分类形式化仍缺乏对应指标。**\n§3 将任务定义为 ordinal classification，但全文评价指标仅有 accuracy 和 pairwise AUC。未报告 MAE（Mean Absolute Error）、QWK（Quadratic Weighted Kappa）、或相邻类 vs 非相邻类的混淆率分析。如果论文的核心论点是\"depths carry natural ordering\"（§3 暗示），则应展示分类错误是否确实集中在相邻深度——这既支持序数结构的存在，也为 EDD 的实用意义提供补充证据。RF 作为非序数分类器在此任务上与 CORAL（序数方法）持平这一事实（见实际论文 §5.1）在 dream 版本中未被讨论。\n\n### Minor Weaknesses\n\n**W4. d0 inflation 仍影响标题指标。**\nTable 1 报告 70-85% 四分类准确率，但 d0 recall 接近完美（98%+），实际的 d1-d3 区分能力显著低于标题数字。Abstract 中\"70-85% four-class accuracy\"是读者首先看到的数字。Dream 版本在 Table 2 中报告了 per-class recall 但在 Table 1 中缺失。建议 Table 1 增加括号注释 d1-d3 三分类准确率。\n\n**W5. 14B 验证仅覆盖 nucleus sampling（Table 2）。**\nStrategy effect 是论文的核心发现之一（9.2pp range > 7.2pp model effect），但 14B 验证仅测试了一种策略。如果 top-k 在 14B 下的行为与 1B 不同（如大模型的 top-k 截断行为可能因 vocabulary 利用率不同而改变），则\"scale robustness\"声明不完整。至少应讨论为什么只测试了 nucleus。\n\n**W6. API model 实验缺乏统计量（Appendix B, Table 7）。**\nGPT-4o-mini 结果无 CI、无 fold-level 方差、样本量未报告。Prompted chain 45% 仅比 chance（25%）高 20pp，信号较弱。在缺乏 CI 的情况下无法判断这 20pp 是否统计显著。\n\n**W7. Wild-data FPR 的正面框架值得商榷（§7）。**\n论文将 C4 的 21.5% FPR 解释为\"depth estimation features capture a general text quality gradient\"。但在数据 curation 应用中，21.5% FPR 意味着每 5 条人类撰写的 web 文本中约 1 条被错误标记——这对实际部署是严重问题。Discussion 应同时呈现这一实用限制。\n\n**W8. 理论预测的后验性质。**\nTable 4 的三条\"predictions\"的预测范围相当宽泛（EDD ∈ [3,5] 覆盖 3 个可能值；15-25%/depth 是 10pp 宽的范围）。审稿人可能质疑这些范围是否在看到数据之前就被确定——如果是在看到实验结果后调整参数（α, ε）使预测匹配数据，则不是真正的 prediction 而是 calibration。论文应明确 α 和 ε 的选择是独立于 Table 4 中的观测值的。\n\n---\n\n## Questions for Authors\n\n**Q1.** α≈0.72 是如何从 fine-tuning loss 衰减（2.27→1.65→1.23）计算的？请写出具体的数学步骤。Fine-tuning loss 和 Dohmatob 理论中的分布距离之间的关系是什么？\n\n**Q2.** Cross-seed replication 是否在 dream 版本中进行？如果是，Table 1 的 CIs 是否包含了 LoRA 种子方差？如果否，建议对 accuracy 差异最小的 cell 对（如 Pythia nucleus vs OLMo nucleus）进行种子敏感性分析。\n\n**Q3.** 14B 实验为何仅测试 nucleus sampling？是否有 GPU 资源约束以外的方法论原因？\n\n**Q4.** Table 4 中 α=0.72 和 ε=0.05 的选择是否独立于 EDD=4 的观测结果？如果 α 或 ε 变化 10%，预测范围如何变化？\n\n**Q5.** RF 分类器在此任务上的混淆矩阵中，相邻类错误（d1↔d2, d2↔d3）占总错误的比例是多少？这一比例是否显著高于非相邻类错误（d1↔d3）？\n\n---\n\n## Missing Experiments / Ablations\n\n1. **Cross-seed replication**: 至少 3 个种子 × 2-3 个关键 cells 的复制是必要的。\n2. **Ordinal evaluation metrics**: MAE, QWK 应与 accuracy 并列报告。\n3. **14B multi-strategy**: 至少应在 14B 上测试 top-k（信号最弱的策略）以验证 scale robustness 在极端条件下也成立。\n4. **α sensitivity analysis**: 在 α ∈ [0.6, 0.85] 和 ε ∈ [0.03, 0.10] 网格上报告 EDD 上界的变化。\n\n---\n\n## Overall Assessment\n\n**Score: 4 / 6 (Weak Accept)**\n\n**理由**: 论文定义了一个重要且新颖的任务，实验设计系统且覆盖面广（3×3 atlas, 14B scale, binary detector baselines, wild-data calibration, API models, negative results）。相比实际论文，Dream 版本的核心改进——14B FP16 验证（W1 of real paper 消除）、binary detector ordinal baseline（填补关键空白）、理论分析（提升贡献层次）——有效回应了审稿人的主要关切。\n\n阻止更高评分的因素：(1) 理论分析中 α 估计的逻辑跳跃削弱了\"theoretically grounded\"的声明力度；(2) 单 LoRA 种子 + 无序数指标是持续的方法论缺口；(3) d0 inflation 继续影响标题指标的信息量。如果作者能提供 α 的严格推导路径（或明确标注为近似）并补充 ordinal metrics，Score 可升至 5。\n\n**Confidence**: 4/5\n",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — Dream 审稿意见（方法 + 实验）\n\n**论文**: Depth Degradation Atlas: Ordinal Estimation of Recursive Generation Depth from Text\n**审查侧重**: 方法描述完整性、实验设计、数据呈现与统计严谨性\n**评分标准**: Top ML venue 通用标准（6 分制，接受率 ~25%）\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类任务，构建了 3×3 (模型×策略) 的 180K 样本基准（Depth Degradation Atlas），并在 14B FP16 规模上验证了深度信号的持续性。论文从 model collapse 收缩率理论推导出 EDD 上界 ≤5，与实证 EDD=4 吻合，并展示了现有二分类检测器（Binoculars, Fast-DetectGPT）在序数任务上接近 chance（30-38%）。相比本项目的实际论文，Dream 版本在理论分析、规模验证和 baseline 覆盖上有实质性改进。\n\n---\n\n## Strengths\n\n**S1. 14B FP16 clean validation 消除关键混淆（Table 2, §6.2）。** 这是相对实际论文最关键的改进。Qwen2.5-14B 在无量化干扰下达到 79% 四分类准确率，d1v2 AUC=0.87 与 1B 模型一致，top-4 特征完全重合（4/4 overlap）。这直接回应了\"small model only\"质疑，且排除了 QLoRA 量化作为混淆因子。Fine-tuning loss 轨迹（2.35→1.58→1.15 比 1B 更平缓）提供了额外机制性证据。\n\n**S2. Binary detector ordinal baseline 建立了任务必要性（Table 3, §6.3）。** Binoculars/Fast-DetectGPT 在序数任务上 30-38%（oracle threshold 含 test-set 信息仍仅 38%），d1v2 AUC 0.54-0.56 仅略高于 chance——这是论文最具说服力的结果之一。RF 19-feature 的 78.3% vs binary detector 的 ~35% 形成 43pp gap，clean proof that ordinal depth estimation requires dedicated methods。这在实际论文中被降级到附录，在 Dream 版本中正确置于主文。\n\n**S3. 理论分析提供了可验证预测（§4, Table 4）。** 三条预测（EDD ∈ [3,5]，p90_ppl 衰减 15-25%/depth，temp/nucleus 收敛比 >1）均与实验吻合。将 atlas 从纯经验观察提升为有理论基础的框架，对审稿人的\"just an empirical study\"质疑有直接回应价值。\n\n**S4. Two-stage pipeline 有具体数字（§6.5）。** Strategy identification accuracy = 57.8%，cross-strategy 从 59.1% 恢复至 70.5%（+11.5pp），oracle ceiling = 78.3%。实际论文仅提到\"recovers 11.5pp\"但未报告策略识别准确率。这些数字让审稿人能评估 pipeline 的瓶颈。\n\n**S5. Wild-data calibration 和 API model 扩展了生态效度（§7, Appendix A-B）。** C4/FineWeb/RedPajama 三语料验证（Table 5-6），FPR 与语料清洗严格度逆相关的发现有洞察力。GPT-4o-mini fine-tuned chain 58% 确认深度信号在 RLHF 对齐商用模型中存在。\n\n---\n\n## Weaknesses\n\n### Major Weaknesses\n\n**W1. 理论分析中 α 的估计路径存在逻辑跳跃（§4.2, Eq. 2）。**\nDohmatob 理论中的收缩率 α 描述的是**分布空间中的距离收缩**（||Pk - P∞|| ≤ C·α^k），但论文用 **fine-tuning loss 衰减**（2.27→1.65→1.23）来估计 α≈0.72。Fine-tuning loss 衡量的是模型对数据的拟合程度，不等于输出分布在 L1/KL 意义下的距离收缩。此外，从分布距离到 AUC 的映射依赖于特征提取管道的性质（哪些特征被提取、分类器的决策边界形状），但论文将 ε=0.05 直接映射到 AUC=0.75 threshold 而未说明这一对应关系的假设条件。\n\n这并非致命缺陷——三条预测确实与数据吻合——但推导中的非严格步骤应被明确标注为近似（approximate derivation），而非呈现为严格上界（\"we derive... EDD ≤ 5\"）。如果审稿人追问\"α 为什么可以从 loss 估计？\"，当前文本缺乏防御。\n\n**W2. Atlas 单 LoRA 种子问题仍未解决。**\n论文未提及 cross-seed replication。实际论文的 cross-seed 数据显示 GPT-2 XL 两个种子的 CI 不重叠（Δ=2.04pp），表明 LoRA 初始化对结果有显著影响。Dream 版本报告的 bootstrap CIs（±1-2.5pp, Table 1）仅量化了 fold 间方差，不捕获 LoRA 种子方差。如果种子方差与 fold 方差量级相当（~2pp），Table 1 中某些 cell 间的差异（如 Pythia nucleus 78.2% vs OLMo nucleus 78.9%，Δ=0.7pp）可能不显著。这影响对 model effect 和 strategy effect 的量化解读。\n\n**W3. 序数分类形式化仍缺乏对应指标。**\n§3 将任务定义为 ordinal classification，但全文评价指标仅有 accuracy 和 pairwise AUC。未报告 MAE（Mean Absolute Error）、QWK（Quadratic Weighted Kappa）、或相邻类 vs 非相邻类的混淆率分析。如果论文的核心论点是\"depths carry natural ordering\"（§3 暗示），则应展示分类错误是否确实集中在相邻深度——这既支持序数结构的存在，也为 EDD 的实用意义提供补充证据。RF 作为非序数分类器在此任务上与 CORAL（序数方法）持平这一事实（见实际论文 §5.1）在 dream 版本中未被讨论。\n\n### Minor Weaknesses\n\n**W4. d0 inflation 仍影响标题指标。**\nTable 1 报告 70-85% 四分类准确率，但 d0 recall 接近完美（98%+），实际的 d1-d3 区分能力显著低于标题数字。Abstract 中\"70-85% four-class accuracy\"是读者首先看到的数字。Dream 版本在 Table 2 中报告了 per-class recall 但在 Table 1 中缺失。建议 Table 1 增加括号注释 d1-d3 三分类准确率。\n\n**W5. 14B 验证仅覆盖 nucleus sampling（Table 2）。**\nStrategy effect 是论文的核心发现之一（9.2pp range > 7.2pp model effect），但 14B 验证仅测试了一种策略。如果 top-k 在 14B 下的行为与 1B 不同（如大模型的 top-k 截断行为可能因 vocabulary 利用率不同而改变），则\"scale robustness\"声明不完整。至少应讨论为什么只测试了 nucleus。\n\n**W6. API model 实验缺乏统计量（Appendix B, Table 7）。**\nGPT-4o-mini 结果无 CI、无 fold-level 方差、样本量未报告。Prompted chain 45% 仅比 chance（25%）高 20pp，信号较弱。在缺乏 CI 的情况下无法判断这 20pp 是否统计显著。\n\n**W7. Wild-data FPR 的正面框架值得商榷（§7）。**\n论文将 C4 的 21.5% FPR 解释为\"depth estimation features capture a general text quality gradient\"。但在数据 curation 应用中，21.5% FPR 意味着每 5 条人类撰写的 web 文本中约 1 条被错误标记——这对实际部署是严重问题。Discussion 应同时呈现这一实用限制。\n\n**W8. 理论预测的后验性质。**\nTable 4 的三条\"predictions\"的预测范围相当宽泛（EDD ∈ [3,5] 覆盖 3 个可能值；15-25%/depth 是 10pp 宽的范围）。审稿人可能质疑这些范围是否在看到数据之前就被确定——如果是在看到实验结果后调整参数（α, ε）使预测匹配数据，则不是真正的 prediction 而是 calibration。论文应明确 α 和 ε 的选择是独立于 Table 4 中的观测值的。\n\n---\n\n## Questions for Authors\n\n**Q1.** α≈0.72 是如何从 fine-tuning loss 衰减（2.27→1.65→1.23）计算的？请写出具体的数学步骤。Fine-tuning loss 和 Dohmatob 理论中的分布距离之间的关系是什么？\n\n**Q2.** Cross-seed replication 是否在 dream 版本中进行？如果是，Table 1 的 CIs 是否包含了 LoRA 种子方差？如果否，建议对 accuracy 差异最小的 cell 对（如 Pythia nucleus vs OLMo nucleus）进行种子敏感性分析。\n\n**Q3.** 14B 实验为何仅测试 nucleus sampling？是否有 GPU 资源约束以外的方法论原因？\n\n**Q4.** Table 4 中 α=0.72 和 ε=0.05 的选择是否独立于 EDD=4 的观测结果？如果 α 或 ε 变化 10%，预测范围如何变化？\n\n**Q5.** RF 分类器在此任务上的混淆矩阵中，相邻类错误（d1↔d2, d2↔d3）占总错误的比例是多少？这一比例是否显著高于非相邻类错误（d1↔d3）？\n\n---\n\n## Missing Experiments / Ablations\n\n1. **Cross-seed replication**: 至少 3 个种子 × 2-3 个关键 cells 的复制是必要的。\n2. **Ordinal evaluation metrics**: MAE, QWK 应与 accuracy 并列报告。\n3. **14B multi-strategy**: 至少应在 14B 上测试 top-k（信号最弱的策略）以验证 scale robustness 在极端条件下也成立。\n4. **α sensitivity analysis**: 在 α ∈ [0.6, 0.85] 和 ε ∈ [0.03, 0.10] 网格上报告 EDD 上界的变化。\n\n---\n\n## Overall Assessment\n\n**Score: 4 / 6 (Weak Accept)**\n\n**理由**: 论文定义了一个重要且新颖的任务，实验设计系统且覆盖面广（3×3 atlas, 14B scale, binary detector baselines, wild-data calibration, API models, negative results）。相比实际论文，Dream 版本的核心改进——14B FP16 验证（W1 of real paper 消除）、binary detector ordinal baseline（填补关键空白）、理论分析（提升贡献层次）——有效回应了审稿人的主要关切。\n\n阻止更高评分的因素：(1) 理论分析中 α 估计的逻辑跳跃削弱了\"theoretically grounded\"的声明力度；(2) 单 LoRA 种子 + 无序数指标是持续的方法论缺口；(3) d0 inflation 继续影响标题指标的信息量。如果作者能提供 α 的严格推导路径（或明确标注为近似）并补充 ordinal metrics，Score 可升至 5。\n\n**Confidence**: 4/5\n",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-18T17:03:26.627004+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3718
}
```

</details>

---


### Assistant

_source line 532 · 2026-05-18T17:03:30.855019+00:00_

Dream 审稿意见已提交。

核心判断：Dream 版本在 14B FP16 验证、binary detector baseline、理论分析三个维度上有实质改进，Score 4/6 (Weak Accept)。主要未解决问题是理论中 α 估计的逻辑跳跃、单 LoRA 种子、缺乏序数评价指标。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

16 recorded events


### User

_source line 533 · 2026-05-18T17:03:31.862239+00:00_

[Round 1 审稿请求]:
[Dream 审稿任务 — Reviewer 1：方法 + 实验]

论文标题：Ordinal Depth Estimation for Recursive Model-Generated Text: A Depth Degradation Atlas

PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/median/review_input_e90a5c14.pdf

实验设计参考（含想象实验列表）：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/median/review_context.yaml

审稿标准：top ML venue 通用标准（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

你的审查侧重：
- **方法描述**：是否完整、claim 是否被实验数据支撑、关键超参 / 训练流程是否清晰
- **实验设计**：是否覆盖关键 baseline / ablation / 跨数据集 / scale 维度
- **数据呈现**：表格 / 图是否能让审稿人复现结论、误差棒 / 统计显著性是否充分
- **实验覆盖度**：参考 review_context.yaml 中的想象实验列表，判断论文是否覆盖了关键实验

请基于论文内容独立评判，不要假设论文结果的质量高低。

**不要评判**：新颖性 / 相关工作（那是 Reviewer 2 的范围）、格式 / 排版。

**Dream 审稿边界**：
- 不需要评审：Reproducibility checklist、代码/数据可用性、具体数值精确性（数字是想象的，关注实验设计而非数值）、伦理/IRB、匿名性
- 需要评审但标注为 "presentation 层面"：Reference 真实性、论文完整度、引用数量
- 必须评审（idea/design 层面）：实验设计是否足以支撑 claims、叙事逻辑是否自洽、Claim 的 generality 是否被实验范围支撑

每条 weakness 必须标注属于 **idea 层面** 还是 **presentation 层面**。

**评分校准规则**：
- 3+ Major issues → 不高于 Borderline Reject
- 2 Major issues → 不高于 Weak Accept
- 1 Major issue → 不高于 Accept
- 0 Major issues → 可给 Strong Accept
Major issue 需有 explicit justification。

请输出结构化审稿报告，包含：Summary、Strengths、Weaknesses（标注 Major/Minor + idea/presentation）、Questions、Overall Score（1-6）、Confidence（1-5）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-18T17:03:39.105922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/median/review_context.yaml"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-18T17:03:39.157071+00:00_

1	narrative_guidance: 'Median档核心叙事：论文定位为 task formalization + systematic empirical study
2	  + bounded claims。 14B结果存在但减弱（68% vs 1B的78%），Claim 1必须从"robust across scales"降级为
3	  "feasible at 1B with preliminary evidence of scale persistence at 14B"。 Binoculars/Fast-DetectGPT
4	  ordinal baseline在45-60%的表现削弱方法独特性， 需将优势重新定位为"systematic multi-model multi-strategy
5	  coverage + ordinal-specific feature discovery"而非单一cell的accuracy优势。 理论section标注为"Theoretical
6	  Motivation"不列入contribution list。 Cross-strategy pipeline诚实报告strategy classifier瓶颈。
7	  论文需要champion reviewer认可problem formalization + Atlas/EDD的价值才能过线。 预期reviewer avg
8	  3.0-3.5，borderline accept需要rebuttal中补充14B多策略或调整claim强度。
9	
10	  '
11	imagined_experiments:
12	- name: 14B_scale_validation
13	  plan_id: plan_014
14	  description: 'Qwen2.5-14B FP16 + LoRA, nucleus p=0.95, d0-d3递归链。 19特征提取 + RF/LR分类。验证depth
15	    signal在14B主流规模下是否持续。
16	
17	    '
18	  expected_results:
19	    rf_4class_acc: 0.68
20	    rf_4class_ci:
21	    - 0.665
22	    - 0.695
23	    lr_4class_acc: 0.635
24	    rf_3class_acc: 0.575
25	    d0v1_auc: 0.972
26	    d1v2_auc: 0.76
27	    d2v3_auc: 0.67
28	    d1v3_auc: 0.92
29	    per_class_recall_d0: 0.97
30	    per_class_recall_d1: 0.72
31	    per_class_recall_d2: 0.46
32	    per_class_recall_d3: 0.58
33	    feature_top4_overlap_with_1b: 2
34	    top_features:
35	    - p90_ppl
36	    - mean_surprisal
37	    - type_token_ratio
38	    - var_surprisal
39	    finetune_loss_d0: 1.85
40	    finetune_loss_d1: 1.42
41	    finetune_loss_d2: 1.18
42	    delta_vs_1b_best_pp: -15.2
43	    delta_vs_1b_avg_pp: -11.5
44	  result_rationale: '14B模型容量远大于1B，LoRA fine-tune在每一代产生的分布偏移更小—— 模型能更好地在fit训练数据的同时保持生成多样性。具体机制：
45	    (1) 14B的attention head冗余度高，LoRA rank=16仅修改极小比例参数， 递归fine-tune对整体生成分布的扰动幅度约为1B的60-70%；
46	    (2) perplexity tail statistics (p90_ppl)仍为top feature，因为tail erosion 是recursive
47	    generation的universal现象（Shumailov机制与模型规模无关）， 但绝对差异缩小——14B d1的p90_ppl中位数可能在d0和d1之间的gap仅为1B的一半；
48	    (3) feature ran
…[truncated 18880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-18T17:03:50.539091+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/median/review_input_e90a5c14.pdf /tmp/dream_median_paper.txt 2>/dev/null && wc -l /tmp/dream_median_paper.txt",
  "description": "Extract median dream paper PDF text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/median/review_input_e90a5c14.pdf /tmp/dream_median_paper.txt 2>/dev/null && wc -l /tmp/dream_median_paper.txt",
    "description": "Extract median dream paper PDF text"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-18T17:03:50.847416+00:00_

997 /tmp/dream_median_paper.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 308
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-18T17:03:54.185618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/dream_median_paper.txt",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/dream_median_paper.txt",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-18T17:03:54.286798+00:00_

1	Ordinal Depth Estimation for Recursive Model-Generated Text:
2	A Depth Degradation Atlas
3	
4	Anonymous
5	
6	Abstract
7	Web-scraped training corpora increasingly contain multi-generational synthetic content
8	produced by uncontrolled model-data-model feedback loops. While binary detectors distinguish human from machine text, they discard ordinal depth information that is critical for
9	data curation: rst-generation synthetic data may improve training, whereas deeply recursive text drives distribution collapse. We formalize ordinal generation depth estimation as
10	a new task and construct a multi-generational benchmark spanning three model families
11	(1B1.5B), three decoding strategies, and four recursion depths. Feature-based classiers
12	on 19 statistical features achieve 7085% four-class accuracy (chance = 25%), with perplexity tail statistics consistently among the top-4 features across all settings. We provide a
13	Depth Degradation Atlas, the rst systematic empirical map of how text statistical properties evolve across recursive depths, revealing non-uniform inter-depth distances, an Eective
14	Discriminable Depth (EDD) boundary, and strategy-dependent feature trajectory reversal.
15	A two-stage strategy-aware pipeline improves cross-strategy accuracy by +11.5 percentage
16	points over naive transfer. Preliminary experiments on Qwen2.5-14B conrm depth signal persistence at mainstream model scale (68% accuracy, chance = 25%), with attenuated
17	inter-depth discrimination compared to 1B models. We release the benchmark and feature
18	extraction pipeline to support further research on recursive contamination in training data.
19	
20	1
21	
22	Introduction
23	
24	Large Language Models (LLMs) trained on web-crawled data increasingly face a recursive contamination problem: model-generated text enters training corpora, and models trained on this
25	data produce the next generation of synthetic text [Shumailov et al., 2024, Alemohammad et al.,
26	2024]. This 
…[truncated 10006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-18T17:03:57.208414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/dream_median_paper.txt",
  "offset": "250",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/dream_median_paper.txt",
    "offset": "250",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-18T17:03:57.260255+00:00_

250	4
251	4
252	3
253	3
254	4
255	3
256	3
257	3
258	3
259	
260	3
261	4
262	3
263	3
264	3
265	3
266	3
267	3
268	2
269	
270	3
271	3
272	3
273	3
274	3
275	2
276	3
277	3
278	2
279	
280	3
281	3
282	2
283	2
284	3
285	2
286	2
287	2
288	2
289	
290	GPT-2 XL / Nucleus
291	GPT-2 XL / Temp
292	GPT-2 XL / Top-k
293	OLMo / Nucleus
294	OLMo / Temp
295	OLMo / Top-k
296	Pythia / Nucleus
297	Pythia / Temp
298	Pythia / Top-k
299	
300	feature-based detection [He et al., 2024] adapted for ordinal classication. All results use 5-fold
301	cross-validation with bootstrap condence intervals (1,000 resamples).
302	
303	4
304	
305	Depth Degradation Atlas
306	
307	4.1 Within-Strategy Depth Estimation
308	Table 1 presents four-class depth estimation accuracy across all 9 model-strategy cells with 95%
309	bootstrap condence intervals. Random Forest achieves the highest accuracy in 8 of 9 settings,
310	ranging from 69.6% (Pythia, top-k ) to 85.4% (GPT-2 XL, temperature). All cells are well above
311	the 25% chance baseline, with the lowest condence interval lower bound at 68.1%.
312	Two patterns emerge. First,
313	
314	strategy eects are systematic: temperature consistently
315	
316	yields the highest or near-highest accuracy within each model, while top-k consistently yields the
317	lowest. This ordering reects how each strategy shapes the generation distribution (Section 8).
318	Second,
319	
320	model eects are secondary: GPT-2 XL achieves the highest accuracy across all
321	
322	strategies, but the strategy eect (up to 16pp between temperature and top-k ) exceeds the model
323	eect (up to 7pp between GPT-2 XL and Pythia at the same strategy).
324	
325	4.2 Eective Discriminable Depth
326	We dene the Eective Discriminable Depth (EDD) as the maximum depth d at which adjacent
327	depths d and d+1 can be reliably distinguished. Formally, EDD(T ) = max{d : AUC(d, d+1) ≥
328	
329	T }, where T is a discrimination threshold.
330	Table 2 reports EDD at four threshold levels. At the standard 
…[truncated 6963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-18T17:04:00.632405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/dream_median_paper.txt",
  "offset": "499",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/dream_median_paper.txt",
    "offset": "499",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-18T17:04:00.683349+00:00_

499	strategy-invariant core (approximately 60% accuracy oor) plus a strategy-specic component.
500	
501	Misrouted samples still benet from the invariant core, while correctly routed samples
502	
503	gain the full strategy-specic signal.
504	
505	7
506	
507	Extended Validation
508	
509	7.1 Scale Validation: 14B
510	To test whether depth signal persists at mainstream model scale, we replicate the recursive chain
511	with Qwen2.5-14B in FP16 (no quantization) using LoRA ne-tuning and nucleus sampling
512	(p=0.95).
513	Table 4 shows that depth signal persists at 14B (68% accuracy, chance = 25%) but with
514	attenuated inter-depth discrimination: d1 vd2 AUC drops from 0.91 to 0.76, and d2 vd3 from 0.82
515	to 0.67. The d0 vd1 boundary remains strong (AUC = 0.972). Per-class recall reveals that depth
516	2 is the hardest to classify (recall = 46%), consistent with 14B's larger capacity causing depth 1
517	
518	6
519	
520	Table 4: Scale comparison: Qwen2.5-14B vs 1B-scale models. 14B uses nucleus sampling; 1B
521	values are nucleus-strategy averages. ∆ columns show the 14B decrement.
522	
523	Model
524	
525	4-class Acc (%) d vd AUC d vd AUC
526	1
527	
528	2
529	
530	2
531	
532	3
533	
534	Top-4 Features
535	
536	GPT-2 XL (1.5B)
537	OLMo (1B)
538	Pythia (1.4B)
539	
540	83.9
541	78.9
542	78.1
543	
544	0.91
545	0.86
546	0.84
547	
548	0.82
549	0.79
550	0.77
551	
552	p90, var_s, mean_s, rep3
553	p90, var_s, prob_std, ttr
554	p90, var_s, rep3, mean_s
555	
556	Qwen2.5 (14B)
557	∆ vs 1B best
558	
559	68.0
560	−15.9
561	
562	0.76
563	−0.15
564	
565	0.67
566	−0.15
567	
568	p90, mean_s, ttr, var_s
569	2/4 overlap
570	
571	Table 5: Depth estimation across model types.
572	
573	Base 1B is the nucleus-strategy average over
574	
575	three 1B models. API models show attenuated but non-zero signal.
576	
577	Model Type
578	
579	4-class Acc (%) d vd AUC Top Feature
580	
581	Base 1B (avg)
582	Base 14B (Qwen)
583	API ne-tuned
584	API prompted
585	Chance
586	
587	1
588	
589	78.3
590	68.0

…[truncated 4891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-18T17:04:05.972133+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/dream_median_paper.txt",
  "offset": "748",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/dream_median_paper.txt",
    "offset": "748",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-18T17:04:06.023046+00:00_

748	
749	where τdisc is the minimum KL divergence required for statistical discrimination. For 1B models,
750	this bound gives EDD ≤ 6, while empirical EDD is 34. The bound is loose but directionally
751	correct, and the gap reects the violation of the i.i.d. assumption:
752	
753	our recursive chain uses
754	
755	dierent LoRA weights at each depth, creating a non-stationary contraction operator rather
756	than a xed one.
757	
758	Strategy-dependent convergence rates. Temperature scaling divides all logits by τ ,
759	
760	applying a uniform transformation that preserves distribution shape but rescales entropy.
761	
762	In
763	
764	contrast, nucleus and top-k sampling truncate the tail. Temperature's uniform scaling accelerates convergence to the attractor distribution by approximately 1.31.5× compared to truncation
765	methods, explaining why temperature-sampled text at depth N exhibits feature values similar
766	to nucleus/top-k text at depth N +1. This mechanistic dierence explains the feature trajectory
767	reversal observed in cross-strategy experiments (Section 6).
768	
769	8
770	
771	9
772	
773	Analysis: Contrastive Ordinal Learning
774	
775	We attempted to learn depth-discriminative text embeddings via contrastive ordinal learning,
776	training a RoBERTa-large encoder with an N-pair contrastive loss that attracts same-depth
777	embeddings and repels dierent-depth embeddings with margins proportional to depth distance.
778	Across six architecture and training variants (v1v6), all attempts failed: embedding collapse
779	(v1v2), out-of-memory errors (v3), catastrophic forgetting (v4), hyperparameter instability
780	(v5), and the nal RoBERTa-large variant (v6) achieved only 64.4% accuracy, 13.7pp below the
781	Random Forest baseline (78.2%).
782	This negative result is informative. Ordinal depth signal resides primarily in distributional
783	statistics (perplexity tails, surprisal variance) rather than in token-level semantic features that
784	RoBERTa-s
…[truncated 11010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-18T17:06:52.214532+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — Median Dream 审稿意见（方法 + 实验）\n\n**论文**: Ordinal Depth Estimation for Recursive Model-Generated Text: A Depth Degradation Atlas\n**审查侧重**: 方法描述、实验设计、数据呈现\n**评分标准**: Top ML venue 6 分制（接受率 ~25%）\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类任务，构建了 3 模型 × 3 策略 × 4 深度的 180K 样本基准和 Depth Degradation Atlas。RF 分类器在 19 统计特征上达到 70-85% 四分类准确率。论文还报告了 14B 规模初步验证（68%）、二分类检测器序数 baseline（48-54%）、wild-data 校准、API 模型实验、以及 contrastive ordinal learning 负面结果。整体实验覆盖面广，报告诚实，但两个关键实验缺口（跨模型迁移、跨种子复制）和一个设计不一致（序数形式化 vs 非序数指标）限制了 claims 的支撑强度。\n\n---\n\n## Strengths\n\n**S1. 系统性的 Atlas 设计和诚实的 claim 边界。** [idea] 3×3 网格在模型和策略两个维度上系统展开。论文自觉地将 14B 结果定位为\"preliminary evidence\"（§7.1, §10.1）、将理论部分标注为\"Theoretical Motivation\"（§8）而非贡献、并在 Limitations 中逐条列出关键约束。这种诚实的 claim 校准在投稿中少见且值得肯定。\n\n**S2. 二分类检测器序数 baseline 是关键实验。** [idea] Table 3 展示 Binoculars（48%）和 Fast-DetectGPT（54%）在序数任务上的表现，d1v2 AUC 仅 0.61-0.66——虽然高于 chance 但远低于 RF（0.861）。更有说服力的是排除 d0 后的 3-class accuracy（detectors ~41% vs RF 59-82%），证明 binary scores 在 d1+ 上确实饱和。这直接支撑了 \"ordinal estimation requires dedicated methods\" 的论点。不过，Fast-DetectGPT 在某些 cells 达到 60%（GPT-2 XL temp09），与 RF top-k cells（69.6%）的 gap 仅 ~10pp——论文在 §5 诚实报告了这一点。\n\n**S3. d0 排除指标作为 companion metric。** [presentation] §4.4 显式报告 3-class accuracy（59-82%），直接回应了 d0 inflation 的标准审稿批评。这比仅在括号中注明要清晰得多。\n\n**S4. Cross-strategy analysis 有机制性解释和实用方案。** [idea] §6.1 不仅报告 d1v2 AUC 反转（0.13-0.25），还提供了 temperature uniform scaling → accelerated convergence 的机制性解释。Two-stage pipeline 的呈现（strategy classifier 57.8%, +11.5pp recovery, oracle ceiling 78.3%）让审稿人能评估每个组件的瓶颈——这比仅报告\"+11.5pp\"信息量大得多。\n\n**S5. 负面结果的分析价值。** [idea] §9 的 DCOL v1-v6 失败模式分析（embedding collapse → OOM → catastrophic forgetting → gradient instability → overfitting）提供了系统性的 negative evidence。cosine similarity > 0.95 的发现为\"feature-based > end-to-end for this task\"提供了解释性证据。\n\n**S6. Wild-data calibration 提供生态效度。** [idea] Table 6 在 C4/FineWeb/RedPajama 上的部署验证，特别是 FPR 与语料清洗严格度的逆相关性发现，以及 WikiText 控制组 99% d0 的结果，为从 controlled 到 deployment 的路径提供了初步证据。\n\n---\n\n## Weaknesses\n\n### Major Weaknesses\n\n**W1 [Major, idea] 跨模型迁移实验缺失，但 claim 暗示跨模型泛化。**\n§3.3 提到 \"In cross-model leave-one-out experiments, we ensure the reference model is distinct from the generation model\"，但全文无表格报告 cross-model LOO transfer accuracy。这是一个关键遗漏：Atlas 的核心价值在于揭示\"跨模型/策略的统计规律性\"，但如果在 Pythia 上训练的分类器无法识别 OLMo 生成的文本的深度，Atlas 的实用价值大打折扣。对比 review_context.yaml：该实验不在 imagined experiments 列表中，但它是实证论文的标准泛化测试。\n\nContribution 2（Atlas）的措辞 \"perplexity tail statistics as universal depth markers\" 暗示了跨模型泛化，但没有跨模型实验支撑这一 claim。在缺乏 cross-model LOO 数据的情况下，\"universal\" 应限定为 \"consistent within each model-strategy cell\"。\n\n**W2 [Major, idea] 单 LoRA 种子 + 无跨种子复制，Atlas cell 间比较缺乏统计基础。**\nTable 1 的 bootstrap CIs（±1.2-2.8pp）仅量化 fold 间方差，不捕获 LoRA 初始化方差。如果 LoRA 种子方差与 fold 方差量级相当（实际论文的 cross-seed 数据显示 GPT-2 XL Δ=2.04pp 且 CI 不重叠），则：\n- §4.1 的 \"strategy effect up to 16pp exceeds model effect up to 7pp\" 可能部分是 LoRA 种子噪声的产物\n- Table 1 中 CI 重叠的 cell 对（review_context 估计约 3 对）的差异不能被解释为有意义\n- 14B 的 68% 与 1B 均值的 78.3% 之间的 10pp 差异可能部分归因于 14B 的特定种子\n\n论文未提及 cross-seed replication，也未在 Limitations 中讨论种子效应。至少需要对 2-3 个关键 cells 进行 3 种子复制，或在 Limitations 中显式承认这一限制。\n\n### Minor Weaknesses\n\n**W3 [Minor, idea] 14B 验证削弱 feature universality claim 但未在 Contribution 中限定。**\nTable 4 显示 14B 的 top-4 features 仅与 1B 重合 2/4（p90_ppl 和 var_surprisal 保留，但 type_token_ratio 替代了 repetition 类特征）。Contribution 2(a) 声称 \"perplexity tail statistics as universal depth markers\"——14B 结果实际上支持 \"p90_ppl is universal\" 但不支持 var_surprisal 的普遍性（在 14B 降至 top-4 但非 top-2）。论文应在 Contribution 中加入 scale 限定词：\"universal within the 1-1.5B range; partially preserved at 14B\"。\n\n**W4 [Minor, idea] 序数形式化与评价指标不一致。**\n§3.1 明确将任务定义为 ordinal classification 并给出三条理由（discrete, non-uniform distances, ordinal structure should be exploited）。但：\n- 主分类器 RF 不利用序数结构\n- CORAL（序数方法）在 Table 3 中低于 RF 4pp（74.1% vs 78.3%）\n- 全文无 MAE、QWK 或相邻 vs 非相邻错误分析\n如果 ordinal 方法不优于 non-ordinal 方法，且不报告 ordinal 指标，则 §3.1 的第三条理由（\"ordinal structure should be exploited\"）缺乏实证支撑。\n\n**W5 [Minor, idea] EDD 缺乏 bootstrap 显著性检验。**\nTable 2 报告了 EDD 在 4 个阈值下的值，但未报告 pairwise AUC 的置信区间或 bootstrap p 值。在 T=0.75 下 7/9 cells 达到 EDD≥3，但 d2v3 AUC 的不确定性未量化——如果某些 cells 的 d2v3 AUC CI 跨越 0.75，EDD 的报告值就不稳健。\n\n**W6 [Minor, presentation] API 实验缺乏统计量和样本量报告。**\nTable 5 中 API model 结果（42-45%）无 CI、无 fold 方差、无样本量。Prompted chain 42% 仅比 chance 高 17pp——在缺乏统计量的情况下无法判断是否显著。\n\n**W7 [Minor, idea] 256 token 的通道长度可能低估信号强度。**\n§3.2 使用 256 token passages。如果深度信号随长度增强（如实际论文显示 128→256→512 的 9.5pp 单调增长），则当前设置可能系统性低估准确率上限，也可能改变最优特征排名。论文未报告长度消融实验。\n\n**W8 [Minor, idea] Wild-data FPR 的实际部署影响被低估。**\nC4 上 32% FPR 意味着近 1/3 的人类文本被标记为 d1+。§10.1 承认\"too high for deployment without additional filtering\"，但 Discussion §10 第二段的 \"depth-graduated curation\" 建议（d0 full weight, d1 reduced, d2+ excluded）在 32% FPR 下会导致大量 d0 文本被错误降权。论文应量化这一实际影响。\n\n**W9 [Minor, presentation] EDD 定义缺少 contiguous 条件。**\n§4.2 的 EDD 定义为 `max{d : AUC(d, d+1) ≥ T}`，这是 non-contiguous 版本——允许中间某一对 AUC < T 但更深一对 AUC ≥ T 时报告较高的 EDD。对于非单调 AUC profile（如 14B 或 instruction-tuned 模型可能出现的 U-shaped pattern），这一定义可能过于乐观。应讨论 contiguous vs non-contiguous 的设计选择。\n\n---\n\n## Questions\n\n**Q1.** 是否进行了 cross-model leave-one-out transfer 实验？如果是，请报告结果；如果否，这一遗漏的原因是什么？\n\n**Q2.** Table 1 的 CIs 是否包含 LoRA 种子方差？如果仅基于 fold-level bootstrap，建议补充至少 2 个关键 cells 的 3 种子复制。\n\n**Q3.** RF 分类器的混淆矩阵中，相邻类错误（如 d1↔d2）占总错误的比例是多少？这一比例是否显著高于随机预期？\n\n**Q4.** 将通道长度从 256 增加到 512 tokens 对准确率的影响是多少？是否进行了长度消融？\n\n**Q5.** CORAL 低于 RF 4pp（Table 3），且论文声称 ordinal structure 应被利用（§3.1）——如何解释这一矛盾？\n\n---\n\n## Experiments Coverage Assessment (vs review_context.yaml)\n\n| 想象实验 | 论文是否覆盖 | 覆盖质量 |\n|----------|------------|---------|\n| 14B scale validation | ✓ (Table 4) | 仅 nucleus，单模型，无 multi-strategy |\n| Wild-data calibration | ✓ (Table 6) | 3 corpora + 1 control，合理 |\n| Detector ordinal baseline | ✓ (Table 3) | 全面，含 9-cell breakdown |\n| Bootstrap CIs | ✓ (Table 1) | 合理 |\n| Theoretical analysis | ✓ (§8) | 正确定位为 motivation，不 overclaim |\n| API model chains | ✓ (Table 5) | 缺 CIs 和样本量 |\n| DCOL negative results | ✓ (§9) | 有分析价值 |\n| **Cross-model LOO transfer** | ✗ 缺失 | 关键泛化轴 |\n| **Cross-seed replication** | ✗ 缺失 | 影响 cell 间比较 |\n| **Feature ablation (top-k vs full)** | ✗ 缺失 | 有助确认 5 特征是否足够 |\n| **Length ablation** | ✗ 缺失 | 影响部署建议 |\n\n---\n\n## Overall Assessment\n\n**Score: 3 / 6 (Borderline Reject)**\n\n**Major issues（2 个）**:\n1. 跨模型迁移实验缺失（W1），但 \"universal depth markers\" claim 暗示跨模型泛化 → claim 超出实验支撑范围\n2. 单 LoRA 种子无复制（W2）→ Atlas cell 间比较的统计基础不足\n\n**理由**: 论文在任务形式化、Atlas 设计和诚实报告方面有明确优势。Binary detector baseline（S2）和 companion metric excluding d0（S3）是有效的呈现决策。但两个 Major 缺口——跨模型迁移和跨种子复制——共同削弱了核心 claims 的泛化可信度。Feature universality claim 在缺乏跨模型和跨规模（14B only 2/4 overlap）证据的情况下需要显著限定。14B 结果的 68% 准确率和 2/4 feature overlap 实际上部分 *反驳* 了 universality claim 而非支持。\n\n如果作者在 rebuttal 中补充 cross-model LOO transfer 结果（即使准确率较低，诚实报告也有价值），并提供至少 2 个 cells 的 cross-seed 方差估计，Score 可升至 4（Weak Accept）。当前状态下，两个 Major issues 的共同影响使论文处于接受线以下。\n\n**Confidence: 4/5** (仔细阅读全文和 context，对方法和实验设计的评估有高置信度)\n",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — Median Dream 审稿意见（方法 + 实验）\n\n**论文**: Ordinal Depth Estimation for Recursive Model-Generated Text: A Depth Degradation Atlas\n**审查侧重**: 方法描述、实验设计、数据呈现\n**评分标准**: Top ML venue 6 分制（接受率 ~25%）\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类任务，构建了 3 模型 × 3 策略 × 4 深度的 180K 样本基准和 Depth Degradation Atlas。RF 分类器在 19 统计特征上达到 70-85% 四分类准确率。论文还报告了 14B 规模初步验证（68%）、二分类检测器序数 baseline（48-54%）、wild-data 校准、API 模型实验、以及 contrastive ordinal learning 负面结果。整体实验覆盖面广，报告诚实，但两个关键实验缺口（跨模型迁移、跨种子复制）和一个设计不一致（序数形式化 vs 非序数指标）限制了 claims 的支撑强度。\n\n---\n\n## Strengths\n\n**S1. 系统性的 Atlas 设计和诚实的 claim 边界。** [idea] 3×3 网格在模型和策略两个维度上系统展开。论文自觉地将 14B 结果定位为\"preliminary evidence\"（§7.1, §10.1）、将理论部分标注为\"Theoretical Motivation\"（§8）而非贡献、并在 Limitations 中逐条列出关键约束。这种诚实的 claim 校准在投稿中少见且值得肯定。\n\n**S2. 二分类检测器序数 baseline 是关键实验。** [idea] Table 3 展示 Binoculars（48%）和 Fast-DetectGPT（54%）在序数任务上的表现，d1v2 AUC 仅 0.61-0.66——虽然高于 chance 但远低于 RF（0.861）。更有说服力的是排除 d0 后的 3-class accuracy（detectors ~41% vs RF 59-82%），证明 binary scores 在 d1+ 上确实饱和。这直接支撑了 \"ordinal estimation requires dedicated methods\" 的论点。不过，Fast-DetectGPT 在某些 cells 达到 60%（GPT-2 XL temp09），与 RF top-k cells（69.6%）的 gap 仅 ~10pp——论文在 §5 诚实报告了这一点。\n\n**S3. d0 排除指标作为 companion metric。** [presentation] §4.4 显式报告 3-class accuracy（59-82%），直接回应了 d0 inflation 的标准审稿批评。这比仅在括号中注明要清晰得多。\n\n**S4. Cross-strategy analysis 有机制性解释和实用方案。** [idea] §6.1 不仅报告 d1v2 AUC 反转（0.13-0.25），还提供了 temperature uniform scaling → accelerated convergence 的机制性解释。Two-stage pipeline 的呈现（strategy classifier 57.8%, +11.5pp recovery, oracle ceiling 78.3%）让审稿人能评估每个组件的瓶颈——这比仅报告\"+11.5pp\"信息量大得多。\n\n**S5. 负面结果的分析价值。** [idea] §9 的 DCOL v1-v6 失败模式分析（embedding collapse → OOM → catastrophic forgetting → gradient instability → overfitting）提供了系统性的 negative evidence。cosine similarity > 0.95 的发现为\"feature-based > end-to-end for this task\"提供了解释性证据。\n\n**S6. Wild-data calibration 提供生态效度。** [idea] Table 6 在 C4/FineWeb/RedPajama 上的部署验证，特别是 FPR 与语料清洗严格度的逆相关性发现，以及 WikiText 控制组 99% d0 的结果，为从 controlled 到 deployment 的路径提供了初步证据。\n\n---\n\n## Weaknesses\n\n### Major Weaknesses\n\n**W1 [Major, idea] 跨模型迁移实验缺失，但 claim 暗示跨模型泛化。**\n§3.3 提到 \"In cross-model leave-one-out experiments, we ensure the reference model is distinct from the generation model\"，但全文无表格报告 cross-model LOO transfer accuracy。这是一个关键遗漏：Atlas 的核心价值在于揭示\"跨模型/策略的统计规律性\"，但如果在 Pythia 上训练的分类器无法识别 OLMo 生成的文本的深度，Atlas 的实用价值大打折扣。对比 review_context.yaml：该实验不在 imagined experiments 列表中，但它是实证论文的标准泛化测试。\n\nContribution 2（Atlas）的措辞 \"perplexity tail statistics as universal depth markers\" 暗示了跨模型泛化，但没有跨模型实验支撑这一 claim。在缺乏 cross-model LOO 数据的情况下，\"universal\" 应限定为 \"consistent within each model-strategy cell\"。\n\n**W2 [Major, idea] 单 LoRA 种子 + 无跨种子复制，Atlas cell 间比较缺乏统计基础。**\nTable 1 的 bootstrap CIs（±1.2-2.8pp）仅量化 fold 间方差，不捕获 LoRA 初始化方差。如果 LoRA 种子方差与 fold 方差量级相当（实际论文的 cross-seed 数据显示 GPT-2 XL Δ=2.04pp 且 CI 不重叠），则：\n- §4.1 的 \"strategy effect up to 16pp exceeds model effect up to 7pp\" 可能部分是 LoRA 种子噪声的产物\n- Table 1 中 CI 重叠的 cell 对（review_context 估计约 3 对）的差异不能被解释为有意义\n- 14B 的 68% 与 1B 均值的 78.3% 之间的 10pp 差异可能部分归因于 14B 的特定种子\n\n论文未提及 cross-seed replication，也未在 Limitations 中讨论种子效应。至少需要对 2-3 个关键 cells 进行 3 种子复制，或在 Limitations 中显式承认这一限制。\n\n### Minor Weaknesses\n\n**W3 [Minor, idea] 14B 验证削弱 feature universality claim 但未在 Contribution 中限定。**\nTable 4 显示 14B 的 top-4 features 仅与 1B 重合 2/4（p90_ppl 和 var_surprisal 保留，但 type_token_ratio 替代了 repetition 类特征）。Contribution 2(a) 声称 \"perplexity tail statistics as universal depth markers\"——14B 结果实际上支持 \"p90_ppl is universal\" 但不支持 var_surprisal 的普遍性（在 14B 降至 top-4 但非 top-2）。论文应在 Contribution 中加入 scale 限定词：\"universal within the 1-1.5B range; partially preserved at 14B\"。\n\n**W4 [Minor, idea] 序数形式化与评价指标不一致。**\n§3.1 明确将任务定义为 ordinal classification 并给出三条理由（discrete, non-uniform distances, ordinal structure should be exploited）。但：\n- 主分类器 RF 不利用序数结构\n- CORAL（序数方法）在 Table 3 中低于 RF 4pp（74.1% vs 78.3%）\n- 全文无 MAE、QWK 或相邻 vs 非相邻错误分析\n如果 ordinal 方法不优于 non-ordinal 方法，且不报告 ordinal 指标，则 §3.1 的第三条理由（\"ordinal structure should be exploited\"）缺乏实证支撑。\n\n**W5 [Minor, idea] EDD 缺乏 bootstrap 显著性检验。**\nTable 2 报告了 EDD 在 4 个阈值下的值，但未报告 pairwise AUC 的置信区间或 bootstrap p 值。在 T=0.75 下 7/9 cells 达到 EDD≥3，但 d2v3 AUC 的不确定性未量化——如果某些 cells 的 d2v3 AUC CI 跨越 0.75，EDD 的报告值就不稳健。\n\n**W6 [Minor, presentation] API 实验缺乏统计量和样本量报告。**\nTable 5 中 API model 结果（42-45%）无 CI、无 fold 方差、无样本量。Prompted chain 42% 仅比 chance 高 17pp——在缺乏统计量的情况下无法判断是否显著。\n\n**W7 [Minor, idea] 256 token 的通道长度可能低估信号强度。**\n§3.2 使用 256 token passages。如果深度信号随长度增强（如实际论文显示 128→256→512 的 9.5pp 单调增长），则当前设置可能系统性低估准确率上限，也可能改变最优特征排名。论文未报告长度消融实验。\n\n**W8 [Minor, idea] Wild-data FPR 的实际部署影响被低估。**\nC4 上 32% FPR 意味着近 1/3 的人类文本被标记为 d1+。§10.1 承认\"too high for deployment without additional filtering\"，但 Discussion §10 第二段的 \"depth-graduated curation\" 建议（d0 full weight, d1 reduced, d2+ excluded）在 32% FPR 下会导致大量 d0 文本被错误降权。论文应量化这一实际影响。\n\n**W9 [Minor, presentation] EDD 定义缺少 contiguous 条件。**\n§4.2 的 EDD 定义为 `max{d : AUC(d, d+1) ≥ T}`，这是 non-contiguous 版本——允许中间某一对 AUC < T 但更深一对 AUC ≥ T 时报告较高的 EDD。对于非单调 AUC profile（如 14B 或 instruction-tuned 模型可能出现的 U-shaped pattern），这一定义可能过于乐观。应讨论 contiguous vs non-contiguous 的设计选择。\n\n---\n\n## Questions\n\n**Q1.** 是否进行了 cross-model leave-one-out transfer 实验？如果是，请报告结果；如果否，这一遗漏的原因是什么？\n\n**Q2.** Table 1 的 CIs 是否包含 LoRA 种子方差？如果仅基于 fold-level bootstrap，建议补充至少 2 个关键 cells 的 3 种子复制。\n\n**Q3.** RF 分类器的混淆矩阵中，相邻类错误（如 d1↔d2）占总错误的比例是多少？这一比例是否显著高于随机预期？\n\n**Q4.** 将通道长度从 256 增加到 512 tokens 对准确率的影响是多少？是否进行了长度消融？\n\n**Q5.** CORAL 低于 RF 4pp（Table 3），且论文声称 ordinal structure 应被利用（§3.1）——如何解释这一矛盾？\n\n---\n\n## Experiments Coverage Assessment (vs review_context.yaml)\n\n| 想象实验 | 论文是否覆盖 | 覆盖质量 |\n|----------|------------|---------|\n| 14B scale validation | ✓ (Table 4) | 仅 nucleus，单模型，无 multi-strategy |\n| Wild-data calibration | ✓ (Table 6) | 3 corpora + 1 control，合理 |\n| Detector ordinal baseline | ✓ (Table 3) | 全面，含 9-cell breakdown |\n| Bootstrap CIs | ✓ (Table 1) | 合理 |\n| Theoretical analysis | ✓ (§8) | 正确定位为 motivation，不 overclaim |\n| API model chains | ✓ (Table 5) | 缺 CIs 和样本量 |\n| DCOL negative results | ✓ (§9) | 有分析价值 |\n| **Cross-model LOO transfer** | ✗ 缺失 | 关键泛化轴 |\n| **Cross-seed replication** | ✗ 缺失 | 影响 cell 间比较 |\n| **Feature ablation (top-k vs full)** | ✗ 缺失 | 有助确认 5 特征是否足够 |\n| **Length ablation** | ✗ 缺失 | 影响部署建议 |\n\n---\n\n## Overall Assessment\n\n**Score: 3 / 6 (Borderline Reject)**\n\n**Major issues（2 个）**:\n1. 跨模型迁移实验缺失（W1），但 \"universal depth markers\" claim 暗示跨模型泛化 → claim 超出实验支撑范围\n2. 单 LoRA 种子无复制（W2）→ Atlas cell 间比较的统计基础不足\n\n**理由**: 论文在任务形式化、Atlas 设计和诚实报告方面有明确优势。Binary detector baseline（S2）和 companion metric excluding d0（S3）是有效的呈现决策。但两个 Major 缺口——跨模型迁移和跨种子复制——共同削弱了核心 claims 的泛化可信度。Feature universality claim 在缺乏跨模型和跨规模（14B only 2/4 overlap）证据的情况下需要显著限定。14B 结果的 68% 准确率和 2/4 feature overlap 实际上部分 *反驳* 了 universality claim 而非支持。\n\n如果作者在 rebuttal 中补充 cross-model LOO transfer 结果（即使准确率较低，诚实报告也有价值），并提供至少 2 个 cells 的 cross-seed 方差估计，Score 可升至 4（Weak Accept）。当前状态下，两个 Major issues 的共同影响使论文处于接受线以下。\n\n**Confidence: 4/5** (仔细阅读全文和 context，对方法和实验设计的评估有高置信度)\n",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-18T17:06:56.358529+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4143
}
```

</details>

---


### Assistant

_source line 548 · 2026-05-18T17:07:02.782164+00:00_

Median Dream 审稿意见已提交。

核心判断：Score 3/6 (Borderline Reject)。两个 Major issues：(1) 跨模型迁移实验缺失但 "universal" claim 暗示跨模型泛化；(2) 单 LoRA 种子无复制使 Atlas cell 间比较缺乏统计基础。14B 结果（68%, 2/4 feature overlap）实际上部分反驳了 universality claim。补充 cross-model LOO 和 cross-seed 方差可升至 Weak Accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 21

## Round 21

4 recorded events


### User

_source line 549 · 2026-05-18T17:07:03.784222+00:00_

[Round 2 审稿请求]:
[Round 2 — Cross-Share]

Reviewer 2（新颖性 + 相关工作）的 Round 1 报告：

---
**R2 Score: 2.5/6 (Borderline Findings)**

**R2 Major Issues:**
1. **Missing adjacent literature undermines novelty claim**: Membership inference (Shi et al. 2024 Min-K% Prob, Maini 2023 TOFU, Min 2023 SiLo), corpus fingerprinting, and watermarking (Kirchenbauer 2023, Christ 2024) are unacknowledged. If membership inference methods adapted to ordinal depth achieve competitive accuracy, the novelty claim is weakened.
2. **Practical scope too constrained for real-world framing**: Works well only when source model is known, decoding strategy known, model is base (not instruct), and domain is clean. Instruct/API models (42-45%) represent most real-world AI text. 19-32% wild FPR is prohibitive. The paper's framing implies real-world applicability but experiments show a narrow lab setting.
3. **Atlas is primarily descriptive statistics**: The four Atlas findings are observational characterizations from 19 features. No mechanistic account of why findings hold, no test of predictive power on held-out models. Without mechanistic grounding or demonstrated generalization, the Atlas contribution is inflated.

**R2 Minor Issues:**
1. Binary baseline vs RF comparison conflates different evaluation regimes (oracle strategy vs unknown strategy).
2. Decoding strategy effects subsection only cites 2 papers despite feature trajectory reversal being a key finding.

**R2 Questions:**
1. How do membership inference methods perform on the ordinal depth task?
2. Does the Atlas predict anything testable on unseen models?
3. Is the system for real-world auditing or for studying model collapse in controlled settings?
---

请你（Reviewer 1）从方法 + 实验角度对 R2 的发现做补充：
- R2 提到的 missing literature（membership inference, watermarking）是否会影响方法层面的可比性？即这些方法如果适配到 ordinal depth task，实验设计上是否需要包含它们作为 baseline？
- R2 认为 Atlas 是 descriptive statistics——从实验设计角度看，Atlas findings 是否有 predictive value（如能否预测 14B 的 feature behavior）？
- R2 的 scope constraint 批评——从实验数据看，base model vs instruct model 的 feature regime 差异是否 fundamental 到 invalidate 整个 framework？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-18T17:08:12.508697+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — Round 2 Cross-Share 回应（方法 + 实验视角补充 R2 发现）\n\n---\n\n### 1. Missing Literature 对方法层面可比性的影响\n\n**R2-Major-1 提到的 membership inference 方法是否应作为 ordinal baseline？**\n\n[PARTIALLY AGREE] 但需区分两个层次：\n\n**概念层面**：membership inference（MI）和 ordinal depth estimation 解决的是不同问题。MI 回答\"这段文本是否在模型 X 的训练集中\"——这是一个 binary 问题，且依赖于特定模型的训练数据。Ordinal depth estimation 回答\"这段文本经历了多少轮递归生成\"——这是一个 ordinal 问题，且（理论上）不依赖于特定模型。两者的 threat model 不同。\n\n**实验层面**：然而，MI 方法（尤其是 Min-K% Prob）的核心机制——利用 token-level probability 分布的统计特性——与本文的 perplexity tail features 有实质性重叠。如果将 Min-K% Prob 的连续分数校准为 ordinal bins（类似论文对 Binoculars/Fast-DetectGPT 的处理），它可能构成一个有信息量的 baseline。具体原因：\n\n- Min-K% Prob 本质上关注 low-probability token 的行为——这与 p90_ppl（high perplexity = low probability tokens）捕获的信号相同\n- 递归生成的 tail erosion 会系统性地改变 low-probability token 的分布，因此 MI score 可能随 depth 单调变化\n- 如果 Min-K% Prob 的 ordinal calibration 达到与 Fast-DetectGPT（54%）相当或更好的表现，它将成为比 Binoculars 更强的 baseline\n\n**建议**：将 Min-K% Prob ordinal calibration 作为 Table 3 的补充 baseline 是合理的实验要求，且实现成本低（仅需在已有数据上计算 Min-K% scores + binning）。但我不同意 R2 将其上升为 Major issue 的判断——即使 Min-K% Prob 达到 55-60%，RF 19-feature 的 78.3% 仍有 18-23pp 优势，不改变论文的核心结论。\n\n**Watermarking（Kirchenbauer 2023, Christ 2024）**则不构成合理 baseline——watermarking 是 proactive 方法（需要生成时嵌入），与本文的 retroactive 分析方法在 threat model 上根本不同。论文应在 Related Work 中讨论但不需要作为实验 baseline。\n\n---\n\n### 2. Atlas 的 Predictive Value——从实验数据评估\n\n**R2-Major-3 认为 Atlas 是 descriptive statistics。从实验设计角度，Atlas findings 是否有 predictive value？**\n\n[PARTIALLY AGREE with R2] Atlas 确实主要是 descriptive，但有部分 predictive evidence——问题在于论文未显式测试 predictions。\n\n**Atlas 隐含的可检验预测**：\n1. \"p90_ppl 在所有 model-strategy cells 中 top-4\" → 预测 14B 也应如此\n2. \"strategy 三档排序：temp > nucleus > top-k\" → 预测 14B 也应如此\n3. \"d0v1 near-perfect, d2v3 是 bottleneck\" → 预测 14B 也应如此\n\n**14B 数据的检验结果（Table 4）**：\n- Prediction 1：**部分成立**。p90_ppl 在 14B 仍为 top-1，但 var_surprisal 降至 top-4（非 top-2），整体 overlap 仅 2/4。Atlas 预测了 p90_ppl 的稳健性但未预测 type_token_ratio 的崛起。\n- Prediction 2：**未测试**。14B 仅有 nucleus，无法验证 strategy 排序。\n- Prediction 3：**成立**。d0v1 AUC = 0.972（仍 near-perfect），d2v3 = 0.67（仍是 bottleneck）。\n\n**Cross-model chains（如果存在）**也是 prediction test：Atlas 基于 single-model chains 的发现是否 transfer 到 heterogeneous chains？但 median dream 论文未报告跨模型迁移。\n\n**结论**：Atlas 有一些 implicit predictive power，但论文未将其显式框架化为 \"predictions from 1B → test at 14B\"。如果 §7.1 的叙事改为 \"We use the 14B experiment to test three predictions derived from the 1B Atlas\"，则 Atlas 的贡献从 \"description\" 升级为 \"empirically testable characterization\"。当前的写法（§7.1 以验证 signal persistence 为目标，而非测试 Atlas predictions）错失了这一机会。\n\nR2 的批评在当前叙事下是成立的——Atlas findings 被呈现为 observations 而非 testable predictions。但 the underlying data actually supports partial predictive power，这是一个叙事问题而非实验缺陷。\n\n---\n\n### 3. Base Model vs Instruct/API 的 Feature Regime 差异是否 Fundamental\n\n**R2-Major-2 认为 practical scope 过窄。从实验数据看，instruct model 的 feature shift 是否 invalidate 整个 framework？**\n\n[REBUT — feature shift 不 invalidate framework，但确实 redefine scope]\n\n**实验证据分析**：\n\nTable 5 显示 API models 的 top feature 从 p90_ppl 转为 surprisal_range。这意味着：\n- RLHF/instruction tuning 预先压缩了 perplexity tail（alignment 本身执行了一种 tail regularization）\n- 递归生成在 aligned model 上仍然产生可检测的分布偏移，但偏移的 dominant dimension 不同（positional surprisal patterns 而非 tail erosion）\n\n**这是 scope boundary，不是 framework invalidation**。理由：\n\n1. **42-45% 仍显著高于 25% chance**。即使信号衰减，framework 的核心机制（递归生成 → 分布偏移 → 可检测特征）仍成立。accuracy 下降不等于 framework 失效——它等于 feature set 需要针对 aligned model 重新设计。\n\n2. **Feature shift 本身是有价值的科学发现**。\"Instruction tuning regularizes the perplexity tail, forcing depth signal into alternative distributional dimensions\" 这一发现实际上深化了对递归生成机制的理解。如果所有模型类型都产生相同的 feature profile，反而说明 feature 捕获的是 trivial 信号。\n\n3. **Primary use case 是 base model outputs in data feedback loops**。R2 说 \"instruct/API models represent most real-world AI text\" ——这是正确的，但论文的 target application 是 training data curation（检测训练语料中的递归污染），不是检测 ChatGPT 输出。Training data contamination 主要由 base model outputs 或 lightly fine-tuned outputs 构成，因为这些才是进入 web-crawl → training pipeline 的内容。Instruct model outputs 通常以对话形式存在，与 pretraining corpus 的格式不同。\n\n**但 R2 的批评在一个关键点上是成立的**：论文的 framing（Introduction, Abstract）暗示了比实验支撑更广的适用性。Median dream 的 Abstract 说 \"ordinal generation depth estimation as a new task\" 而非 \"ordinal depth estimation for base model recursive chains\"。如果 task formalization 声称的是一般性任务，但实验仅在特定 regime 下有效（base models, known strategy, clean domain），则 framing 与 evidence 之间存在 gap。\n\n**修正建议**：论文应在 Introduction 中明确 primary scope：\"We focus on base model recursive chains, the dominant mode of uncontrolled data contamination in web-crawled training corpora\"。将 instruct/API 实验定位为 scope boundary exploration 而非 limitation。\n\n---\n\n### 综合评估对 R2 Score 的影响\n\nR2 给出 2.5/6（Borderline Findings）。从方法 + 实验角度：\n\n- **R2-Major-1（missing MI baseline）**：有一定道理但不构成 Major——MI 方法如果适配后在 54-60% 范围，不改变论文结论。建议降级为 Minor。\n- **R2-Major-2（practical scope）**：部分成立——framing 与 evidence 之间确实有 gap，但 base model use case 合理。建议维持为 Major 但承认 target application 的合理性。\n- **R2-Major-3（Atlas descriptive）**：当前叙事下成立，但 underlying data 有部分 predictive power。建议维持为 Should-Fix（叙事调整可修复），不构成 fundamental weakness。\n\n综合看，R2 的 2.5 偏低——将 MI baseline 缺失升级为 Major 不合理，且 Atlas 的 predictive value 被低估。但 practical scope 的 framing gap 是实质性问题。我认为合理分数范围是 3.0-3.5，而非 2.5。\n\n**我维持 Median Dream 的 R1 评分 3/6（Borderline Reject）**，主要基于 cross-model transfer 缺失和 single-seed confound——这两个 idea-level 问题比 R2 关注的 novelty/scope 问题更直接影响实验 claims 的可信度。\n",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — Round 2 Cross-Share 回应（方法 + 实验视角补充 R2 发现）\n\n---\n\n### 1. Missing Literature 对方法层面可比性的影响\n\n**R2-Major-1 提到的 membership inference 方法是否应作为 ordinal baseline？**\n\n[PARTIALLY AGREE] 但需区分两个层次：\n\n**概念层面**：membership inference（MI）和 ordinal depth estimation 解决的是不同问题。MI 回答\"这段文本是否在模型 X 的训练集中\"——这是一个 binary 问题，且依赖于特定模型的训练数据。Ordinal depth estimation 回答\"这段文本经历了多少轮递归生成\"——这是一个 ordinal 问题，且（理论上）不依赖于特定模型。两者的 threat model 不同。\n\n**实验层面**：然而，MI 方法（尤其是 Min-K% Prob）的核心机制——利用 token-level probability 分布的统计特性——与本文的 perplexity tail features 有实质性重叠。如果将 Min-K% Prob 的连续分数校准为 ordinal bins（类似论文对 Binoculars/Fast-DetectGPT 的处理），它可能构成一个有信息量的 baseline。具体原因：\n\n- Min-K% Prob 本质上关注 low-probability token 的行为——这与 p90_ppl（high perplexity = low probability tokens）捕获的信号相同\n- 递归生成的 tail erosion 会系统性地改变 low-probability token 的分布，因此 MI score 可能随 depth 单调变化\n- 如果 Min-K% Prob 的 ordinal calibration 达到与 Fast-DetectGPT（54%）相当或更好的表现，它将成为比 Binoculars 更强的 baseline\n\n**建议**：将 Min-K% Prob ordinal calibration 作为 Table 3 的补充 baseline 是合理的实验要求，且实现成本低（仅需在已有数据上计算 Min-K% scores + binning）。但我不同意 R2 将其上升为 Major issue 的判断——即使 Min-K% Prob 达到 55-60%，RF 19-feature 的 78.3% 仍有 18-23pp 优势，不改变论文的核心结论。\n\n**Watermarking（Kirchenbauer 2023, Christ 2024）**则不构成合理 baseline——watermarking 是 proactive 方法（需要生成时嵌入），与本文的 retroactive 分析方法在 threat model 上根本不同。论文应在 Related Work 中讨论但不需要作为实验 baseline。\n\n---\n\n### 2. Atlas 的 Predictive Value——从实验数据评估\n\n**R2-Major-3 认为 Atlas 是 descriptive statistics。从实验设计角度，Atlas findings 是否有 predictive value？**\n\n[PARTIALLY AGREE with R2] Atlas 确实主要是 descriptive，但有部分 predictive evidence——问题在于论文未显式测试 predictions。\n\n**Atlas 隐含的可检验预测**：\n1. \"p90_ppl 在所有 model-strategy cells 中 top-4\" → 预测 14B 也应如此\n2. \"strategy 三档排序：temp > nucleus > top-k\" → 预测 14B 也应如此\n3. \"d0v1 near-perfect, d2v3 是 bottleneck\" → 预测 14B 也应如此\n\n**14B 数据的检验结果（Table 4）**：\n- Prediction 1：**部分成立**。p90_ppl 在 14B 仍为 top-1，但 var_surprisal 降至 top-4（非 top-2），整体 overlap 仅 2/4。Atlas 预测了 p90_ppl 的稳健性但未预测 type_token_ratio 的崛起。\n- Prediction 2：**未测试**。14B 仅有 nucleus，无法验证 strategy 排序。\n- Prediction 3：**成立**。d0v1 AUC = 0.972（仍 near-perfect），d2v3 = 0.67（仍是 bottleneck）。\n\n**Cross-model chains（如果存在）**也是 prediction test：Atlas 基于 single-model chains 的发现是否 transfer 到 heterogeneous chains？但 median dream 论文未报告跨模型迁移。\n\n**结论**：Atlas 有一些 implicit predictive power，但论文未将其显式框架化为 \"predictions from 1B → test at 14B\"。如果 §7.1 的叙事改为 \"We use the 14B experiment to test three predictions derived from the 1B Atlas\"，则 Atlas 的贡献从 \"description\" 升级为 \"empirically testable characterization\"。当前的写法（§7.1 以验证 signal persistence 为目标，而非测试 Atlas predictions）错失了这一机会。\n\nR2 的批评在当前叙事下是成立的——Atlas findings 被呈现为 observations 而非 testable predictions。但 the underlying data actually supports partial predictive power，这是一个叙事问题而非实验缺陷。\n\n---\n\n### 3. Base Model vs Instruct/API 的 Feature Regime 差异是否 Fundamental\n\n**R2-Major-2 认为 practical scope 过窄。从实验数据看，instruct model 的 feature shift 是否 invalidate 整个 framework？**\n\n[REBUT — feature shift 不 invalidate framework，但确实 redefine scope]\n\n**实验证据分析**：\n\nTable 5 显示 API models 的 top feature 从 p90_ppl 转为 surprisal_range。这意味着：\n- RLHF/instruction tuning 预先压缩了 perplexity tail（alignment 本身执行了一种 tail regularization）\n- 递归生成在 aligned model 上仍然产生可检测的分布偏移，但偏移的 dominant dimension 不同（positional surprisal patterns 而非 tail erosion）\n\n**这是 scope boundary，不是 framework invalidation**。理由：\n\n1. **42-45% 仍显著高于 25% chance**。即使信号衰减，framework 的核心机制（递归生成 → 分布偏移 → 可检测特征）仍成立。accuracy 下降不等于 framework 失效——它等于 feature set 需要针对 aligned model 重新设计。\n\n2. **Feature shift 本身是有价值的科学发现**。\"Instruction tuning regularizes the perplexity tail, forcing depth signal into alternative distributional dimensions\" 这一发现实际上深化了对递归生成机制的理解。如果所有模型类型都产生相同的 feature profile，反而说明 feature 捕获的是 trivial 信号。\n\n3. **Primary use case 是 base model outputs in data feedback loops**。R2 说 \"instruct/API models represent most real-world AI text\" ——这是正确的，但论文的 target application 是 training data curation（检测训练语料中的递归污染），不是检测 ChatGPT 输出。Training data contamination 主要由 base model outputs 或 lightly fine-tuned outputs 构成，因为这些才是进入 web-crawl → training pipeline 的内容。Instruct model outputs 通常以对话形式存在，与 pretraining corpus 的格式不同。\n\n**但 R2 的批评在一个关键点上是成立的**：论文的 framing（Introduction, Abstract）暗示了比实验支撑更广的适用性。Median dream 的 Abstract 说 \"ordinal generation depth estimation as a new task\" 而非 \"ordinal depth estimation for base model recursive chains\"。如果 task formalization 声称的是一般性任务，但实验仅在特定 regime 下有效（base models, known strategy, clean domain），则 framing 与 evidence 之间存在 gap。\n\n**修正建议**：论文应在 Introduction 中明确 primary scope：\"We focus on base model recursive chains, the dominant mode of uncontrolled data contamination in web-crawled training corpora\"。将 instruct/API 实验定位为 scope boundary exploration 而非 limitation。\n\n---\n\n### 综合评估对 R2 Score 的影响\n\nR2 给出 2.5/6（Borderline Findings）。从方法 + 实验角度：\n\n- **R2-Major-1（missing MI baseline）**：有一定道理但不构成 Major——MI 方法如果适配后在 54-60% 范围，不改变论文结论。建议降级为 Minor。\n- **R2-Major-2（practical scope）**：部分成立——framing 与 evidence 之间确实有 gap，但 base model use case 合理。建议维持为 Major 但承认 target application 的合理性。\n- **R2-Major-3（Atlas descriptive）**：当前叙事下成立，但 underlying data 有部分 predictive power。建议维持为 Should-Fix（叙事调整可修复），不构成 fundamental weakness。\n\n综合看，R2 的 2.5 偏低——将 MI baseline 缺失升级为 Major 不合理，且 Atlas 的 predictive value 被低估。但 practical scope 的 framing gap 是实质性问题。我认为合理分数范围是 3.0-3.5，而非 2.5。\n\n**我维持 Median Dream 的 R1 评分 3/6（Borderline Reject）**，主要基于 cross-model transfer 缺失和 single-seed confound——这两个 idea-level 问题比 R2 关注的 novelty/scope 问题更直接影响实验 claims 的可信度。\n",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-18T17:08:17.707353+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5198
}
```

</details>

---


### Assistant

_source line 552 · 2026-05-18T17:08:23.126102+00:00_

Round 2 Cross-Share 回应已提交。

三个核心判断：
1. MI baseline（Min-K% Prob）值得补充但不改变核心结论，R2 将其升级为 Major 不合理
2. Atlas 有部分 predictive value（14B 验证了 p90_ppl dominance 和 d2v3 bottleneck），但论文未显式测试——这是叙事问题，可修复
3. Base vs instruct 的 feature shift 是 scope boundary 而非 framework invalidation，但 Introduction 的 framing 确实过宽

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 22

## Round 22

58 recorded events


### User

_source line 553 · 2026-05-19T02:58:04.661208+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计 + 统计有效性 + 可复现性**

### Venue 信息
- **目标会议**：EMNLP 2026 Main Conference (通过 ARR 统一审稿)
- **截止日期**：2026-05-25
- **页数限制**：Long paper 8 pages content；Limitations 和 Ethics Statement 不计入页数
- **模板**：ACL style (`\usepackage[review]{acl}`)
- **匿名规则**：Double-blind
- **评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

### 论文文件
- 主文件：`projects/recursive_gen_depth_est/docs/paper/main.tex`
- 各章节：abstract.tex, introduction.tex, related_work.tex, method.tex, theory.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex

### 你的审查重点

1. **方法设计**：
   - 问题定义（ordinal classification formalization）是否严谨
   - EDD 定义（Definition 1, Eq. 1）是否数学上合理
   - 19 个统计特征的设计是否有理论依据和实验支撑
   - RF 分类器选择是否合理，序数结构是否被正确利用

2. **实验设计**：
   - Benchmark 构建（3×3 grid, 180K samples）是否可靠
   - 交叉验证方案是否正确（是否存在数据泄露风险）
   - Cross-model / Cross-strategy / Cross-scale 实验设计是否合理
   - Baseline 选择是否充分、对比是否公平
   - Confound 分析是否到位

3. **统计有效性**：
   - 报告的数字是否可信（CI, p-value, effect size）
   - d0 对 headline metrics 的膨胀效应是否被充分揭示
   - 多重比较是否需要校正
   - 样本量是否足够支撑 claims

4. **可复现性**：
   - 超参数是否完整列出
   - 计算资源是否报告
   - 数据/代码是否承诺公开

### 输出格式

请按以下结构输出审稿意见：
```
## Summary (2-3 句)
## Strengths (逐条)
## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])
## Questions (需要作者回答的问题)
## Missing References (遗漏的重要文献)
## Overall Assessment (评分 + 置信度)
## Detailed Comments (逐 section 的细节意见)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-19T02:58:10.744546+00:00_

called Skill

<details open><summary>🔧 Tool call — Skill</summary>

```json
{
  "skill": "review-reviewer-session-start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Skill",
  "tool_args": {
    "skill": "review-reviewer-session-start"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-19T02:58:10.744899+00:00_

&lt;tool_use_error>Unknown skill: review-reviewer-session-start&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Skill",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-19T02:58:16.719031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-19T02:58:16.920582+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-19T02:58:20.041231+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-19T02:58:20.092392+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-19T02:58:23.558525+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-19T02:58:23.760676+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-19T02:58:26.120573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-19T02:58:26.171641+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-19T02:58:32.599065+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-19T02:58:32.649857+00:00_

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
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{theory}
39	
40	\input{atlas}
41	
42	\input{generalization}
43	
44	\input{discussion}
45	
46	\input{conclusion}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{section_appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-19T02:58:43.614722+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 567 · 2026-05-19T02:58:43.665531+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-19T02:58:47.630143+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,TodoWrite,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,TodoWrite,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-19T02:58:47.680805+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-19T02:58:55.413576+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 ACL ARR reviewer guidelines 和评分标准', 'status': 'in_progress', 'activeForm': '搜索 ACL ARR reviewer guidelines'}, {'content': '通读论文全文（所有章节）', 'status': 'pending', 'activeForm': '通读论文全文'}, {'content': '验证引用完整性和真实性', 'status': 'pending', 'activeForm': '验证引用'}, {'content': '撰写审稿意见并汇报 Director', 'status': 'pending', 'activeForm': '撰写审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 ACL ARR reviewer guidelines 和评分标准', 'status': 'in_progress', 'activeForm': '搜索 ACL ARR reviewer guidelines'}, {'content': '通读论文全文（所有章节）', 'status': 'pending', 'activeForm': '通读论文全文'}, {'content': '验证引用完整性和真实性', 'status': 'pending', 'activeForm': '验证引用'}, {'content': '撰写审稿意见并汇报 Director', 'status': 'pending', 'activeForm': '撰写审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-19T02:58:55.464247+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-19T02:58:59.784029+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-19T02:59:00.286004+00:00_

1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	A Random Forest over 19 statistical features achieves $\approx$69--86\% four-class accuracy on 1--1.5B base models under matched decoding strategies (chance = 25\%; d1--d3 balanced accuracy: 71.6\% within-distribution, 55.4\% cross-model; chance = 33\%), with perplexity tail statistics as consistent depth markers; a parsimonious subset of 5 features retains 97.6\% of full performance.
5	We define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.70}{=}4$ for all three families at the primary scale (confirmed by 5-class d0--d4 extension on three families, 71--80\%), and show that cross-model transfer reaches 66.4\% (2.7$\times$ chance).
6	Systematic generalization across eight axes (e.g., cross-scale 7--14B (70\%$\to$54\%, attenuating with scale), prompted generation at 69.5\%, cross-model chains at 84.75\%, and cross-domain arXiv at 74.1\%) confirms that depth signal is robust across model families but scale- and strategy-dependent, residing in distributional statistics inaccessible from surface text or binary detection scores (zero-shot LLMs: 30--36\%; membership inference baselines: 30--33\%; both $>$43\,pp below RF).
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-19T02:59:00.286621+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-19T02:59:00.738553+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	We find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.
15	Specifically, perplexity tail statistics (the 90th-percentile perplexity, \texttt{p90\_ppl}, and su
…[truncated 2740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-19T02:59:00.739309+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-19T02:59:01.241712+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad}.
6	Subsequent work refines the conditions under which collapse occurs: \citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \S\ref{sec:method:theory}), \citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.
7	Mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence analysis \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026} are active areas.
8	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena and call for operationally precise metrics; we respond by operationalizing tail-erosion predictions into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt2024}, Binoculars \cite{binoculars2024}, DivEye \cite{diveye2
…[truncated 2753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-19T02:59:01.242122+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-19T02:59:01.694110+00:00_

1	\section{Method}
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
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 5853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-19T02:59:01.694592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-19T02:59:02.196776+00:00_

1	\subsection{Theoretical Grounding}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts \texttt{p90\_ppl} as a depth marker, confirmed by its top-2 ranking in all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--80\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), so EDD should decrease with scale.
15	Qwen2.5-14B confirms this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B), while d1--d3 AUCs remain above 0.70 (\S\ref{sec:gen:crossscale}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$(d{+}1)$ text in tail statistics.
20	GPT-2~XL confirms this: temperature d1 median \texttt{p90\_ppl} (92.2) matches the nu
…[truncated 264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-19T02:59:02.197290+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-19T02:59:03.151487+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}1{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: MAE\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$).}
22	\label{tab:main_matrix}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}lccc@{}}
25	\toprule
26	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
27	\midrule
28	Pythia-1.4B  & 78.7{\scriptsize$\pm$0.6}\,(71.8) & 76.8{\scriptsize$\pm$0.6
…[truncated 8333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-19T02:59:03.151851+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-19T02:59:03.604162+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares ordinal depth estimation methods across all 9 atlas cells.
10	RF, XGBoost, and LightGBM on the same 19 features converge within 0.4\,pp per cell, confirming a feature-determined ceiling; on Pythia nucleus, CORAL \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match RF within 0.6\,pp ($p>0.05$).
11	
12	\paragraph{Binary detectors and membership inference.}
13	Four methods designed for binary AI-text detection or membership inference, when calibrated for ordinal depth, all fall 43--48\,pp below RF (Table~\ref{tab:baselines}).
14	Min-K\% Prob \cite{shi2024_minkprob} (33.2\%) outperforms DetectGPT \cite{mitchell2023_detectgpt} (30.7\%) by 2.5\,pp, consistent with token-level log-probabilities encoding more depth information than perturbation-based curvature; both remain near chance.
15	CORAL ordinal calibration does not close the gap (Min-K\% CORAL d1--d3 BalAcc: 40.4\% vs.\ RF 71.6\%), confirming that the bottleneck is input signal, not calibration.
16	Binary detector scores (Binoculars, Fast-DetectGPT) repurposed as RF features reach 74.2\% on a single cell but average only 30--35\% across 9 cells (Appendix~\ref{app:detector_baselines}).
17	Adding Min-K\% probability as a 20th RF feature yields +0.48\,pp (78.4\%$\to$78.9\%); Min-K\% ranks \#3 by importance (0.095), below \texttt{p90\_ppl} (0.161) and \texttt{var\_surprisal} (0.126), while DetectGPT contributes negligibly (\#17, 0.026).
18	The gain is consistent across 8 of 9 cells but small, confirming that the 19 statistical features already capture the dominant ordinal signal.
19	
20	\paragraph{Surface-text ablation.}
21	Single-feature regress
…[truncated 6322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-19T02:59:03.604541+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-19T02:59:04.056715+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	This paper formalizes recursive generation depth estimation as ordinal classification.
5	Perplexity tail statistics (\texttt{p90\_ppl}, \texttt{var\_surprisal}) are consistent depth markers across all nine model--strategy cells; five features retain 97.6\% of full performance, and $\mathrm{EDD}_{0.70}{=}4$ for all three families (confirmed by 5-class extension, 71--80\%; Appendix~\ref{app:depth4_ext}).
6	Cross-model transfer reaches 66.4\% ($2.7\times$ chance), cross-model chains 84.75\%, and cross-domain arXiv 74.1\%; binary detectors and membership inference methods achieve only 30--35\%, confirming that depth-specific distributional features are necessary.
7	Cross-strategy transfer remains the primary bottleneck (d1--d3: 45.9\%); scale-dependent signal attenuation, depth-quality entanglement, and cross-strategy deployment are open challenges (Appendix~\ref{app:extended_discussion}).
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-19T02:59:04.057316+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-19T02:59:04.560969+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Cross-strategy deployment constraint.}
5	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
6	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random Forest classifier used throughout the main experiments ($\Delta < 0.02$\,pp), and even in the best case (logistic regression) leaves a residual gap relative to within-strategy performance (${\sim}0.83$); a two-stage pipeline (strategy identification + strategy-conditioned classification) is therefore needed for reliable cross-strategy deployment.
7	
8	\paragraph{Strategy-unknown deployment.}
9	In strategy-unknown settings, naive transfer on d1--d3 yields only 45.9\%, and d1/d2 predictions may invert.
10	A two-stage pipeline recovers 11.5\,pp over LOO, though per-model gains vary (GPT-2~XL $+$16.4\,pp vs.\ Pythia $+$8.0\,pp).
11	Practical deployment requires either strategy metadata or learned routing.
12	
13	\paragraph{d0 inflation of headline metrics.}
14	Depth~0 (human-written text) is near-perfectly separable (recall $>$97\% across all nine model--strategy settings), inflating headline accuracy.
15	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
16	
17	\paragraph{Controlled vs.\ ecological setting.}
18	The primary benchmark uses Wikipedia seed text with controlled LoRA fine-tuning (1--1.5B models), a design that isolates the depth variable but diverges from wild contamination where models train on mixed corpora with prior-generation outputs at unknown proportions.
19	Domain bias controls confirm depth as the dominant factor: LOGO accuracy (72.1\%) matches standard CV (72.0\%), seed-group prediction is at chance (10.2\%; Appendix~\ref{app:domain_bias}).
20	Cross-scale experiments (7--14B, \
…[truncated 6225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-19T02:59:04.561454+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-19T02:59:05.466098+00:00_

1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
43	Concretely, the d0$\t
…[truncated 57224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-19T02:59:05.466532+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 593 · 2026-05-19T02:59:06.018776+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 594 · 2026-05-19T02:59:23.956539+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, here is information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the pa
…[truncated 470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 18489
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-19T03:00:17.638483+00:00_

&lt;persisted-output>
Output too large (53.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/18e2781e-e5ad-47ad-895c-aafdbd2b04f0/tool-results/toolu_015jUowEUHRVxwKP1QHqw2hZ.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 68, \"total_citations\": 102, \"unique_cited_keys\": 67, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 7, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"c2pa2024\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemo
…[truncated 364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 71619
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-19T03:00:28.561915+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 ACL ARR reviewer guidelines 和评分标准', 'status': 'completed', 'activeForm': '搜索 ACL ARR reviewer guidelines'}, {'content': '通读论文全文（所有章节）', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '验证引用完整性和真实性', 'status': 'in_progress', 'activeForm': '验证引用完整性和真实性'}, {'content': '撰写审稿意见并汇报 Director', 'status': 'pending', 'activeForm': '撰写审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 ACL ARR reviewer guidelines 和评分标准', 'status': 'completed', 'activeForm': '搜索 ACL ARR reviewer guidelines'}, {'content': '通读论文全文（所有章节）', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '验证引用完整性和真实性', 'status': 'in_progress', 'activeForm': '验证引用完整性和真实性'}, {'content': '撰写审稿意见并汇报 Director', 'status': 'pending', 'activeForm': '撰写审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-19T03:00:28.563038+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-19T03:00:29.216378+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-19T03:00:29.267079+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-19T03:00:37.502548+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All scoring dimensions (soundness, excitement, overall assessment, etc.) and their scales (1-5? 1-6?). 2) What each score level means. 3) Any other required fields in the review form (confidence, reproducibility, etc.). 4) Guidelines on what constitutes a good vs bad review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All scoring dimensions (soundness, excitement, overall assessment, etc.) and their scales (1-5? 1-6?). 2) What each score level means. 3) Any other required fields in the review form (confidence, reproducibility, etc.). 4) Guidelines on what constitutes a good vs bad review."
  }
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-19T03:00:40.675607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/18e2781e-e5ad-47ad-895c-aafdbd2b04f0/tool-results/toolu_015jUowEUHRVxwKP1QHqw2hZ.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/18e2781e-e5ad-47ad-895c-aafdbd2b04f0/tool-results/toolu_015jUowEUHRVxwKP1QHqw2hZ.txt"
  }
}
```

</details>

---


### Tool result

_source line 602 · 2026-05-19T03:00:41.130797+00:00_

1	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 68, \"total_citations\": 102, \"unique_cited_keys\": 67, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 7, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"c2pa2024\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"type\": \"misc\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Ger
…[truncated 52390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-19T03:00:46.647225+00:00_

# ARR Review Form Criteria & Scoring

Based on the ARR Reviewer Guidelines, here's what I found regarding the review form:

## Scoring Dimensions

The document explicitly mentions **three scores** (as of February 2025):

1. **Soundness** - Technical validity and methodological rigor
2. **Excitement** - Personal interest level (described as "orthogonal to soundness")
3. **Overall Assessment** - Explicit recommendation for paper outcome

**Critical note:** The guidelines do not specify the numerical scales (1-5, 1-6, etc.) for these dimensions in the provided content.

## Score Interpretation Guidance

- **Soundness scores must be justified** by review text. Low soundness without documented faults indicates incomplete analysis.
- **Excitement reflects subjective taste** and doesn't require explicit reasoning.
- **Overall Assessment** is a "composite score" balancing soundness, excitement, novelty, and potential impact.

## Additional Required Fields

The guidelines reference a "Responsible NLP checklist" but don't detail other mandatory form fields beyond the three scoring dimensions.

## Good vs. Bad Review Standards

**Poor reviews exhibit:**
- Vague criticisms without specifics
- Reliance on common heuristics (H1-H17) without evidence
- Unprofessional or sarcastic tone

**Strong reviews feature:**
- "Specific and ideally understandable to chairs" without reading the full paper
- Clear justification linking scores to textual analysis
- Professional, constructive language

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9144
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-19T03:02:29.976446+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 ACL ARR reviewer guidelines 和评分标准', 'status': 'completed', 'activeForm': '搜索 ACL ARR reviewer guidelines'}, {'content': '通读论文全文（所有章节）', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '验证引用完整性和真实性', 'status': 'completed', 'activeForm': '验证引用完整性和真实性'}, {'content': '撰写审稿意见并汇报 Director', 'status': 'in_progress', 'activeForm': '撰写审稿意见并汇报 Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 ACL ARR reviewer guidelines 和评分标准', 'status': 'completed', 'activeForm': '搜索 ACL ARR reviewer guidelines'}, {'content': '通读论文全文（所有章节）', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '验证引用完整性和真实性', 'status': 'completed', 'activeForm': '验证引用完整性和真实性'}, {'content': '撰写审稿意见并汇报 Director', 'status': 'in_progress', 'activeForm': '撰写审稿意见并汇报 Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-19T03:02:29.977068+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-19T03:05:12.515365+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性\n\n---\n\n## Summary (2-3 句)\n\n本文提出将递归生成深度估计形式化为序数分类问题，构建了一个 180K 样本的基准（3 模型族×3 解码策略×4 深度），用 Random Forest 在 19 个统计特征上实现了 69-86% 的 4 类准确率。论文定义了 Effective Discriminable Depth (EDD) 度量，并在跨模型、跨策略、跨尺度等 8 个泛化维度上进行了系统评估。这是一项扎实的实证研究和问题形式化工作，透明地报告了大量局限性，但生态效度和实际部署可行性存在显著差距。\n\n---\n\n## Strengths (逐条)\n\n**S1. 新颖且有价值的问题定义。** 递归生成深度估计是一个未被研究过的问题，填补了模型坍塌理论（假设深度已知）和二分类检测（忽略深度信息）之间的空白。将其形式化为序数分类是自然且恰当的。Introduction §1 清楚地定位了这一空白。\n\n**S2. 系统的实验设计。** 3×3 网格（模型族×解码策略）在每个 cell 内有 5,000 样本/depth，总计 180K 样本。在多个泛化轴上的评估（跨模型 LOO、跨策略 LOO、跨尺度、prompted generation、跨域 arXiv、cross-model chains）是全面的。基线覆盖了四类方法（二分类检测器、成员推理、zero-shot LLM、序数回归），且对比公平。\n\n**S3. 统计实践透明。** Bootstrap 95% CI (B=1000) 贯穿主要结果（Table 1）；domain bias 分析的三个子实验（标准 CV、LOGO、负控制）设计严谨，且作者透明报告了初始 bug（全局计数器导致 seed-group 与 depth 混淆）及修复后的结果（Appendix §G）。这种透明度值得肯定。\n\n**S4. 诚实的局限性讨论。** d0 膨胀效应、cross-strategy 失败（d1/d2 boundary inversion）、cross-scale 实验的 5 个混杂因素、单 LoRA 种子的 1-3pp 不确定性——这些都在 Limitations 中明确讨论。这种诚实远超许多同类论文。\n\n**S5. 理论-实证对应关系。** §3.1 将 tail erosion 理论预测（p90_ppl 为深度标记物）与 9/9 cells 的实验结果对照验证；strategy-dependent convergence 的理论预测（temperature d1 ≈ nucleus d2）在 GPT-2 XL 数据中得到精确确认（92.2 vs 92.3, §3.3）。\n\n**S6. 特征重要性的三重验证。** Gini、SHAP、permutation importance 三种方法的一致性（Kendall's W=0.90, p<0.005; Appendix §B）增强了 p90_ppl 和 var_surprisal 作为核心深度标记物的可信度。\n\n---\n\n## Weaknesses (逐条)\n\n**W1 [Must-Fix]. 生态效度差距过大，需更清晰的 scope 声明。**\n- 具体位置：§2.2, Limitations \"Controlled vs. ecological setting\"\n- 问题：基准使用 Wikipedia 种子文本 + 可控 LoRA 微调（1-1.5B 模型），每深度独立训练新 adapter。真实世界的递归污染涉及全量微调或预训练、混合语料（不同深度文本混合）、未知比例的合成数据。论文的 pipeline（每步完全替换训练数据）是 model collapse 理论文献的标准 setup，但与实际发生的渐进污染（accumulation setting, cf. Gerstgrasser et al. 2024）存在结构性差异。\n- 为什么影响接收：审稿人和读者需要清楚理解该方法在什么条件下 works，当前 \"recursive generation depth estimation\" 的 framing 暗示了比实际验证范围更广的适用性。\n- 建议修改方向：(1) 在 Abstract 或 Introduction 中明确声明 \"full-replacement recursive chain\" 的 scope 限制；(2) 讨论 accumulation setting（混合真实+合成数据训练）下深度信号是否存在的理论预期；(3) 即使不做实验，也应在 Discussion 中正式讨论这一 gap 与实际部署的关系。\n\n**W2 [Must-Fix]. Cross-strategy 失败是实际部署的根本障碍，但论文 framing 不够突出。**\n- 具体位置：§5.3, Table 4\n- 问题：Cross-strategy transfer 的 d1-d3 balanced accuracy 仅 45.9%（chance=33%），且出现 d1/d2 boundary inversion（d1v2 AUC < 0.5）。在实际部署中，解码策略几乎总是未知的。Two-stage pipeline 恢复 11.5pp 但仍有大幅差距。这意味着在现实条件下（未知策略），深度估计的可靠性大幅下降。\n- 为什么影响接收：论文标题和 Abstract 以 \"estimating recursive generation depth\" 为核心 claim，但该 claim 在最常见的部署场景（未知策略）下实质上不成立——d1-d3 区分仅略高于 chance。\n- 建议修改方向：(1) 在 Abstract 中更明确地 qualify 结果——当前 Abstract 第 6 行的 \"cross-model transfer reaches 66.4% (2.7× chance)\" 是有 d0 膨胀的数字，应补充 d1-d3 的 45.9%；(2) 在 Contributions 列表中增加 \"identifying cross-strategy transfer as a fundamental bottleneck\" 作为独立贡献点，而非仅作为 limitation 处理。\n\n**W3 [Should-Fix]. d0 膨胀显著，Abstract 中的数字呈现具有误导性。**\n- 具体位置：Abstract, Table 2, Table 3\n- 问题：d0 recall > 97% 在所有 9 cells 中成立。4-class accuracy (69-86%) 包含了 d0 的近完美贡献。Abstract 第 4 行 \"69-86% four-class accuracy\" 是 headline，括号内的 \"d1-d3 balanced accuracy: 71.6% within-distribution, 55.4% cross-model\" 虽然提供了修正数字但被淹没在信息过载的长句中。Cross-model 的 66.4% 被 d0 从 55.4% 抬升了 11pp。\n- 建议：在所有 headline 数字旁系统性地并列报告 d1-d3 balanced accuracy，并在 Abstract 中将 d1-d3 数字提升到与 4-class accuracy 同等的显著位置。\n\n**W4 [Should-Fix]. Cross-scale 实验证据不足以支撑 \"scale-dependent attenuation\" 的结论。**\n- 具体位置：§5.4, Table (cross_scale), Appendix §K\n- 问题：仅有 2 个 7-8B 模型（Llama-3.1-8B, Qwen2.5-7B）和 1 个 14B 模型（Qwen2.5-14B）。这 3 个数据点存在 5 个明确列出的混杂因素（QLoRA 量化、样本量缩减至 500、仅 nucleus、vocabulary mismatch、14B 自参考模型）。更关键的是，两个 7-8B 模型的 AUC 轨迹完全不同（Llama 单调递减 vs Qwen U-shaped），无法确定哪种 pattern 是主流。\n- 建议：(1) 将 \"Preliminary Cross-Scale Observations\" 的 \"Preliminary\" 保留但在 Abstract/Contributions 中降调 cross-scale 的 claim 力度；(2) 明确声明 \"cross-scale results are confounded and should be interpreted as existence proofs rather than quantitative trends.\"\n\n**W5 [Should-Fix]. Curation PoC 的 primary comparison 不显著，削弱了实用动机。**\n- 具体位置：Appendix §H, Table 8\n- 问题：RF-filtered vs unfiltered 的比较 p=0.407，effect size d_z=0.41（small），完全不显著。显著的 RF vs random comparison（p<0.02）涉及多重比较且未校正（论文自己承认）。Downstream fine-tuning probe（Appendix §L）同样在 5 seeds、500 samples 下未达显著性。\n- 为什么影响评分：论文在 Extended Discussion（Appendix §P, \"Depth-graduated curation\"）中以此作为实用场景的证据，但统计证据不支持。\n- 建议：(1) 明确将 curation PoC 标记为 \"inconclusive\"，不在 Discussion 中以 \"feasible\" 描述 depth-graduated filtering；(2) 对 RF vs random 的 3 个 comparisons 应用 Bonferroni 或 Holm 校正并报告校正后 p 值。\n\n**W6 [Should-Fix]. 多重共线性下的特征重要性解读需更多 caveat。**\n- 具体位置：§4.2, Table 2\n- 问题：19 个特征中 14-16 个 VIF>10（§2.3），有效独立维度仅 ~4-5。在严重多重共线性下，Gini importance 不可靠（会在相关特征间分散重要性）。论文在 footnote 5 中提到了这一点（\"Individual feature rankings should be interpreted cautiously\"），但正文继续以单特征 rank 作为核心叙事（\"p90_ppl ranks top-2 in all 9 cells\"）。\n- 建议：(1) 主表格应以 feature group（perplexity tail, surprisal, lexical, repetition）而非 individual feature 为分析单位；(2) 考虑使用 grouped permutation importance 或 conditional permutation importance 作为多重共线性下的补充验证。\n\n**W7 [Minor]. EDD 定义中的 AUC threshold T=0.70 选择缺乏独立的理论/实证依据。**\n- 具体位置：Definition 1 (§2.4), §4.4\n- 问题：T=0.70 被选为 \"primary threshold\" 的唯一理由是 \"8/9 cells achieve EDD≥3\"（§2.4 最后一行）。这是循环论证：选择让结果看起来最好的 threshold。虽然敏感性分析（T ∈ {0.65, 0.70, 0.75, 0.80}）有助于缓解，但仍缺乏独立的 calibration。\n- 建议：讨论 T=0.70 在 AUC 文献中的含义（对应什么水平的实际分类性能），或通过 downstream task 的需求反向确定 threshold。\n\n**W8 [Minor]. RF 的 ordinal structure 利用 claim 缺乏严格支撑。**\n- 具体位置：§2.4\n- 问题：\"RF implicitly respects ordinal structure: 98.2% of errors fall on adjacent depths (|Δ|≤1), QWK=0.89\" (Table 1 caption)。但 adjacent-class error 集中可能仅仅反映 adjacent classes 更难区分（feature overlap），而非 RF \"respects\" ordinal structure。论文引用 Janitza et al. (2016) 说 RF \"implicitly respects ordinal structure when inter-class distances are monotonic\"，这一条件在论文中通过 §4.3 的 monotonicity 结果得到部分验证，但论文的表述过于强烈。\n- 建议：弱化表述为 \"RF produces ordinally consistent predictions, with 98.2% of errors at adjacent depths\"，避免暗示 RF 有内在的序数归纳偏置。\n\n**W9 [Minor]. Reference model 与 generator 的重叠未被充分控制。**\n- 具体位置：§2.2 最后一段, Limitations \"Reference model dependency\"\n- 问题：Pythia-1.4B 同时作为三个 generator 之一和唯一的 reference model。论文认为\"Pythia 78.7% vs GPT-2 XL 85.9%\" 说明自参考无系统优势，但这忽略了一种可能性：自参考可能在某些深度边界上具有优势而在其他边界上具有劣势，宏观指标上相互抵消。Appendix §J 的 reference ablation 仅在 Pythia 生成数据上测试（not GPT-2 XL or OLMo），无法排除这一假设。\n- 建议：在至少一个非 Pythia cell（e.g., GPT-2 XL nucleus）上补充 reference model ablation，以排除 generator-reference 交互效应。\n\n---\n\n## Questions (需要作者回答)\n\n**Q1.** 在 accumulation setting（每步保留部分真实数据 + 新生成的合成数据混合训练）下，你们预期深度信号会如何变化？是否有理论上的预期或初步实验？\n\n**Q2.** Cross-model chain 实验（Appendix §K, 84.75%）中，architecture identity 与 depth 完全共变（d1=Pythia, d2=OLMo, d3=GPT-2 XL）。虽然 reverse-chain control 提供了部分证据，但能否通过 same-model-at-all-depths 的结果（即主实验）对减去 architecture signal 做定量分析？例如，比较 cross-model chain 的 per-depth confusion 与 single-model chain 的 confusion 差异。\n\n**Q3.** Table 1 的 d2 recall 系统性最低（44-73%），论文解释为 \"d2 位于深度梯度中心\"。但 d3 recall (61-80%) 一致高于 d2。为什么 d3（更远离 d0）反而比 d2 更容易分类？是否因为 d3 有更多独特的退化信号（如高 repetition）？\n\n**Q4.** Feature extraction \"requires no GPU\" 且 \"2 minutes per 5,000 samples on a single CPU core\" (Appendix §Q)。但 reference model forward pass（Pythia-1.4B）是否确实在 CPU 上运行？如果是，这在大规模部署中是否可行？如果需要 GPU，请修正这一声明。\n\n**Q5.** 论文声称 \"no per-passage lineage exists across depths\" (§2.2)。能否更明确地解释：不同深度的 5,000 个样本是否有任何间接的数据依赖关系？例如，d1 数据是在 d0 上微调后生成的，d2 数据是在 d1 上微调后生成的——即使单个 passage 无对应关系，训练数据的统计特性是有传递性的，这对 CV split 的独立性假设有何影响？\n\n---\n\n## Missing References (遗漏的重要文献)\n\n1. **Shumailov et al. (2024) \"The Curse of Recursion\"** — 虽然 Nature 版本已引用，但 arXiv 预印本中有更多关于 tail erosion 的量化分析，与本文的 p90_ppl 发现直接相关。(注: 可能已覆盖，需确认 Nature 版本是否包含相同内容)\n\n2. 引用验证中 1 条孤立 bib entry (c2pa2024, C2PA Specification) 未在正文中引用——若不使用应删除。\n\n3. 引用验证中 5 条轻微 mismatch（多为第一作者名变体或年份差异）：alemohammad2024_mad, garces_arias2025_decoding_decoded, he2021_deberta_v3 (year: bib=2023 vs api=2021), llama3, guo2024_biscope。建议核实并修正。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5/5\n**Excitement**: 3.0/5\n**Confidence**: 4/5\n\n### 评分理由\n\n**Soundness (3.5)**: 问题定义清晰，实验方法论基本严谨，统计实践透明。主要扣分点：(1) cross-scale 实验的混杂因素使核心结论之一（scale-dependent attenuation）缺乏可靠支撑；(2) d0 膨胀虽被讨论但在 headline 数字呈现上仍有误导性；(3) curation PoC 不显著却作为动机之一。\n\n**Excitement (3.0)**: 问题定义新颖且 timely（递归污染是活跃研究领域），EDD 度量有概念贡献。但 (1) 核心发现（depth signal exists in tail statistics）在模型坍塌理论预测之下并不 surprising；(2) 方法（RF on hand-crafted features）缺乏算法创新；(3) cross-strategy 失败和 scale attenuation 大幅限制了实际影响力——该方法目前仅在\"已知策略 + 1-1.5B 模型\"条件下 reliably works，这一条件在实践中罕见。\n\n**一句话总结**: 一项定义新颖、执行严谨但实用性受限的实证研究——在可控条件下证明了递归深度信号的存在，但距离实际部署（未知策略、大模型）有显著差距，适合作为 Findings 论文发表。\n\n---\n\n## Detailed Comments (逐 section)\n\n### Abstract\n- 信息密度高但几乎不可能一次读懂。建议减少括号内的数字堆砌，将核心结果分为 2-3 个清晰的 claim 层级。\n- \"69-86% four-class accuracy\" 应伴随 \"d1-d3 balanced: 59-82%\" 作为等权的修正数字。\n- \"cross-model transfer reaches 66.4% (2.7× chance)\" 中的 d1-d3 数字 (55.4%) 应被提升到同等显著位置。\n\n### Introduction (§1)\n- 叙事线清晰：递归循环 → 现有工具的空白 → perplexity tail fingerprint 的发现 → 贡献总结。\n- 第 3 段 \"consistent in direction but scale-dependent in magnitude\" 是一个好的 qualifier。\n- Contribution 列表第 3 点过于冗长，应将数字细节移至正文。\n\n### Related Work (§2)\n- 覆盖全面：model collapse theory、AI text detection、membership inference、adjacent tasks、ordinal classification、decoding strategies。\n- 与 Mohamed et al. (2025, \"Broken Telephone\") 的区分清晰：\"characterize how text degrades\" vs \"classify which iteration\"。\n- 引用密度适当（67 unique cited keys）。\n\n### Method (§3)\n- Problem Definition (§2.1): 形式化清晰。建议增加一段讨论 full-replacement vs accumulation setting 的区别。\n- Benchmark (§2.2): \"BOS-seeded generation may amplify depth signal\" — 好的自我审视。但 prompted validation 仅在 1/9 cells 上做了 (GPT-2 XL nucleus)，推广性未确立。\n- Features (§2.3): 设计合理但应更突出 effective dimensionality ~4-5 的发现。\n- EDD (§2.4): 定义数学上自洽。Footnote 2 关于 non-monotonic AUC 的讨论是必要的。\n\n### Theory (§3.1)\n- \"Scale-dependent attenuation\" 的理论预测 (α closer to 1 for larger models) 是合理的。\n- Strategy-dependent convergence 的预测与 GPT-2 XL 数据精确匹配 (92.2 vs 92.3) — 但这是 cherry-picked 的单一比较，需注意不要过度泛化。\n\n### Atlas (§4)\n- §4.1: 结构清晰，交叉效应（strategy effect 9.3pp vs model effect 7.2pp）是有趣的发现。\n- §4.2: Feature importance analysis 的主要问题是 multicollinearity (W6)。\n- §4.4: AUC decay analysis 和 EDD threshold sensitivity 是论文最有价值的分析之一。d3-vs-d4 AUC 在三个模型间的 convergence (0.750-0.784) 特别有说服力。\n\n### Generalization (§5)\n- §5.1: Baseline comparison 全面且公平。RF/XGB/LightGBM convergence within 0.4pp 有力地证明了 feature-determined ceiling。\n- §5.2: Cross-model transfer 的 d2 recall (26.8-52.6%) 是最大的弱点，特别是 Pythia holdout 的 26.8%。\n- §5.3: Cross-strategy failure 是论文最重要的负面结果。Two-stage pipeline 的 11.5pp recovery 是有趣的工程方向。\n- §5.4: Cross-scale observations 标记为 \"Preliminary\" 是恰当的。\n\n### Discussion/Conclusion\n- Discussion 过于简短（单独成节只有一段），未充分讨论 open questions。\n- 建议扩展 Discussion 部分，特别是: (1) accumulation setting; (2) 与 model collapse mitigation 策略的交互; (3) 向实际部署的 roadmap。\n\n### Limitations\n- 覆盖广泛且诚实。特别值得肯定的是 domain-dependent FPR 分析（C4 上 22.4% FPR）和 adversarial robustness 的坦诚承认。\n- 建议增加：passage-level 假设（论文假设每个 passage 深度均匀）在真实 mixed-depth documents 中的限制。（实际上 Appendix §N 讨论了 mixed-depth，但 Limitations 中未提及 segment-level estimation。更新：重新检查发现 Limitations 倒数第二段确实提到了 \"Segment-level estimation in mixed-depth documents remains open\"，这一点已覆盖。）\n\n### Appendix\n- 信息量极大，覆盖了几乎所有可预见的 reviewer 问题。\n- Temperature robustness (Appendix §E) 中 \"memorization as prerequisite\" 的发现（τ=1.1 下信号消失）是一个重要的机制性洞察。\n- Domain bias analysis (Appendix §G) 是论文的一大亮点。\n\n### 格式合规\n- `\\documentclass[11pt]{article}` + `\\usepackage[review]{acl}` — 符合 ACL 2025 模板要求。\n- 匿名化：作者为 \"Anonymous\"，正文中无自引泄露。\n- bib 中 1 条孤立条目 (c2pa2024) 应清理。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性\n\n---\n\n## Summary (2-3 句)\n\n本文提出将递归生成深度估计形式化为序数分类问题，构建了一个 180K 样本的基准（3 模型族×3 解码策略×4 深度），用 Random Forest 在 19 个统计特征上实现了 69-86% 的 4 类准确率。论文定义了 Effective Discriminable Depth (EDD) 度量，并在跨模型、跨策略、跨尺度等 8 个泛化维度上进行了系统评估。这是一项扎实的实证研究和问题形式化工作，透明地报告了大量局限性，但生态效度和实际部署可行性存在显著差距。\n\n---\n\n## Strengths (逐条)\n\n**S1. 新颖且有价值的问题定义。** 递归生成深度估计是一个未被研究过的问题，填补了模型坍塌理论（假设深度已知）和二分类检测（忽略深度信息）之间的空白。将其形式化为序数分类是自然且恰当的。Introduction §1 清楚地定位了这一空白。\n\n**S2. 系统的实验设计。** 3×3 网格（模型族×解码策略）在每个 cell 内有 5,000 样本/depth，总计 180K 样本。在多个泛化轴上的评估（跨模型 LOO、跨策略 LOO、跨尺度、prompted generation、跨域 arXiv、cross-model chains）是全面的。基线覆盖了四类方法（二分类检测器、成员推理、zero-shot LLM、序数回归），且对比公平。\n\n**S3. 统计实践透明。** Bootstrap 95% CI (B=1000) 贯穿主要结果（Table 1）；domain bias 分析的三个子实验（标准 CV、LOGO、负控制）设计严谨，且作者透明报告了初始 bug（全局计数器导致 seed-group 与 depth 混淆）及修复后的结果（Appendix §G）。这种透明度值得肯定。\n\n**S4. 诚实的局限性讨论。** d0 膨胀效应、cross-strategy 失败（d1/d2 boundary inversion）、cross-scale 实验的 5 个混杂因素、单 LoRA 种子的 1-3pp 不确定性——这些都在 Limitations 中明确讨论。这种诚实远超许多同类论文。\n\n**S5. 理论-实证对应关系。** §3.1 将 tail erosion 理论预测（p90_ppl 为深度标记物）与 9/9 cells 的实验结果对照验证；strategy-dependent convergence 的理论预测（temperature d1 ≈ nucleus d2）在 GPT-2 XL 数据中得到精确确认（92.2 vs 92.3, §3.3）。\n\n**S6. 特征重要性的三重验证。** Gini、SHAP、permutation importance 三种方法的一致性（Kendall's W=0.90, p<0.005; Appendix §B）增强了 p90_ppl 和 var_surprisal 作为核心深度标记物的可信度。\n\n---\n\n## Weaknesses (逐条)\n\n**W1 [Must-Fix]. 生态效度差距过大，需更清晰的 scope 声明。**\n- 具体位置：§2.2, Limitations \"Controlled vs. ecological setting\"\n- 问题：基准使用 Wikipedia 种子文本 + 可控 LoRA 微调（1-1.5B 模型），每深度独立训练新 adapter。真实世界的递归污染涉及全量微调或预训练、混合语料（不同深度文本混合）、未知比例的合成数据。论文的 pipeline（每步完全替换训练数据）是 model collapse 理论文献的标准 setup，但与实际发生的渐进污染（accumulation setting, cf. Gerstgrasser et al. 2024）存在结构性差异。\n- 为什么影响接收：审稿人和读者需要清楚理解该方法在什么条件下 works，当前 \"recursive generation depth estimation\" 的 framing 暗示了比实际验证范围更广的适用性。\n- 建议修改方向：(1) 在 Abstract 或 Introduction 中明确声明 \"full-replacement recursive chain\" 的 scope 限制；(2) 讨论 accumulation setting（混合真实+合成数据训练）下深度信号是否存在的理论预期；(3) 即使不做实验，也应在 Discussion 中正式讨论这一 gap 与实际部署的关系。\n\n**W2 [Must-Fix]. Cross-strategy 失败是实际部署的根本障碍，但论文 framing 不够突出。**\n- 具体位置：§5.3, Table 4\n- 问题：Cross-strategy transfer 的 d1-d3 balanced accuracy 仅 45.9%（chance=33%），且出现 d1/d2 boundary inversion（d1v2 AUC < 0.5）。在实际部署中，解码策略几乎总是未知的。Two-stage pipeline 恢复 11.5pp 但仍有大幅差距。这意味着在现实条件下（未知策略），深度估计的可靠性大幅下降。\n- 为什么影响接收：论文标题和 Abstract 以 \"estimating recursive generation depth\" 为核心 claim，但该 claim 在最常见的部署场景（未知策略）下实质上不成立——d1-d3 区分仅略高于 chance。\n- 建议修改方向：(1) 在 Abstract 中更明确地 qualify 结果——当前 Abstract 第 6 行的 \"cross-model transfer reaches 66.4% (2.7× chance)\" 是有 d0 膨胀的数字，应补充 d1-d3 的 45.9%；(2) 在 Contributions 列表中增加 \"identifying cross-strategy transfer as a fundamental bottleneck\" 作为独立贡献点，而非仅作为 limitation 处理。\n\n**W3 [Should-Fix]. d0 膨胀显著，Abstract 中的数字呈现具有误导性。**\n- 具体位置：Abstract, Table 2, Table 3\n- 问题：d0 recall > 97% 在所有 9 cells 中成立。4-class accuracy (69-86%) 包含了 d0 的近完美贡献。Abstract 第 4 行 \"69-86% four-class accuracy\" 是 headline，括号内的 \"d1-d3 balanced accuracy: 71.6% within-distribution, 55.4% cross-model\" 虽然提供了修正数字但被淹没在信息过载的长句中。Cross-model 的 66.4% 被 d0 从 55.4% 抬升了 11pp。\n- 建议：在所有 headline 数字旁系统性地并列报告 d1-d3 balanced accuracy，并在 Abstract 中将 d1-d3 数字提升到与 4-class accuracy 同等的显著位置。\n\n**W4 [Should-Fix]. Cross-scale 实验证据不足以支撑 \"scale-dependent attenuation\" 的结论。**\n- 具体位置：§5.4, Table (cross_scale), Appendix §K\n- 问题：仅有 2 个 7-8B 模型（Llama-3.1-8B, Qwen2.5-7B）和 1 个 14B 模型（Qwen2.5-14B）。这 3 个数据点存在 5 个明确列出的混杂因素（QLoRA 量化、样本量缩减至 500、仅 nucleus、vocabulary mismatch、14B 自参考模型）。更关键的是，两个 7-8B 模型的 AUC 轨迹完全不同（Llama 单调递减 vs Qwen U-shaped），无法确定哪种 pattern 是主流。\n- 建议：(1) 将 \"Preliminary Cross-Scale Observations\" 的 \"Preliminary\" 保留但在 Abstract/Contributions 中降调 cross-scale 的 claim 力度；(2) 明确声明 \"cross-scale results are confounded and should be interpreted as existence proofs rather than quantitative trends.\"\n\n**W5 [Should-Fix]. Curation PoC 的 primary comparison 不显著，削弱了实用动机。**\n- 具体位置：Appendix §H, Table 8\n- 问题：RF-filtered vs unfiltered 的比较 p=0.407，effect size d_z=0.41（small），完全不显著。显著的 RF vs random comparison（p<0.02）涉及多重比较且未校正（论文自己承认）。Downstream fine-tuning probe（Appendix §L）同样在 5 seeds、500 samples 下未达显著性。\n- 为什么影响评分：论文在 Extended Discussion（Appendix §P, \"Depth-graduated curation\"）中以此作为实用场景的证据，但统计证据不支持。\n- 建议：(1) 明确将 curation PoC 标记为 \"inconclusive\"，不在 Discussion 中以 \"feasible\" 描述 depth-graduated filtering；(2) 对 RF vs random 的 3 个 comparisons 应用 Bonferroni 或 Holm 校正并报告校正后 p 值。\n\n**W6 [Should-Fix]. 多重共线性下的特征重要性解读需更多 caveat。**\n- 具体位置：§4.2, Table 2\n- 问题：19 个特征中 14-16 个 VIF>10（§2.3），有效独立维度仅 ~4-5。在严重多重共线性下，Gini importance 不可靠（会在相关特征间分散重要性）。论文在 footnote 5 中提到了这一点（\"Individual feature rankings should be interpreted cautiously\"），但正文继续以单特征 rank 作为核心叙事（\"p90_ppl ranks top-2 in all 9 cells\"）。\n- 建议：(1) 主表格应以 feature group（perplexity tail, surprisal, lexical, repetition）而非 individual feature 为分析单位；(2) 考虑使用 grouped permutation importance 或 conditional permutation importance 作为多重共线性下的补充验证。\n\n**W7 [Minor]. EDD 定义中的 AUC threshold T=0.70 选择缺乏独立的理论/实证依据。**\n- 具体位置：Definition 1 (§2.4), §4.4\n- 问题：T=0.70 被选为 \"primary threshold\" 的唯一理由是 \"8/9 cells achieve EDD≥3\"（§2.4 最后一行）。这是循环论证：选择让结果看起来最好的 threshold。虽然敏感性分析（T ∈ {0.65, 0.70, 0.75, 0.80}）有助于缓解，但仍缺乏独立的 calibration。\n- 建议：讨论 T=0.70 在 AUC 文献中的含义（对应什么水平的实际分类性能），或通过 downstream task 的需求反向确定 threshold。\n\n**W8 [Minor]. RF 的 ordinal structure 利用 claim 缺乏严格支撑。**\n- 具体位置：§2.4\n- 问题：\"RF implicitly respects ordinal structure: 98.2% of errors fall on adjacent depths (|Δ|≤1), QWK=0.89\" (Table 1 caption)。但 adjacent-class error 集中可能仅仅反映 adjacent classes 更难区分（feature overlap），而非 RF \"respects\" ordinal structure。论文引用 Janitza et al. (2016) 说 RF \"implicitly respects ordinal structure when inter-class distances are monotonic\"，这一条件在论文中通过 §4.3 的 monotonicity 结果得到部分验证，但论文的表述过于强烈。\n- 建议：弱化表述为 \"RF produces ordinally consistent predictions, with 98.2% of errors at adjacent depths\"，避免暗示 RF 有内在的序数归纳偏置。\n\n**W9 [Minor]. Reference model 与 generator 的重叠未被充分控制。**\n- 具体位置：§2.2 最后一段, Limitations \"Reference model dependency\"\n- 问题：Pythia-1.4B 同时作为三个 generator 之一和唯一的 reference model。论文认为\"Pythia 78.7% vs GPT-2 XL 85.9%\" 说明自参考无系统优势，但这忽略了一种可能性：自参考可能在某些深度边界上具有优势而在其他边界上具有劣势，宏观指标上相互抵消。Appendix §J 的 reference ablation 仅在 Pythia 生成数据上测试（not GPT-2 XL or OLMo），无法排除这一假设。\n- 建议：在至少一个非 Pythia cell（e.g., GPT-2 XL nucleus）上补充 reference model ablation，以排除 generator-reference 交互效应。\n\n---\n\n## Questions (需要作者回答)\n\n**Q1.** 在 accumulation setting（每步保留部分真实数据 + 新生成的合成数据混合训练）下，你们预期深度信号会如何变化？是否有理论上的预期或初步实验？\n\n**Q2.** Cross-model chain 实验（Appendix §K, 84.75%）中，architecture identity 与 depth 完全共变（d1=Pythia, d2=OLMo, d3=GPT-2 XL）。虽然 reverse-chain control 提供了部分证据，但能否通过 same-model-at-all-depths 的结果（即主实验）对减去 architecture signal 做定量分析？例如，比较 cross-model chain 的 per-depth confusion 与 single-model chain 的 confusion 差异。\n\n**Q3.** Table 1 的 d2 recall 系统性最低（44-73%），论文解释为 \"d2 位于深度梯度中心\"。但 d3 recall (61-80%) 一致高于 d2。为什么 d3（更远离 d0）反而比 d2 更容易分类？是否因为 d3 有更多独特的退化信号（如高 repetition）？\n\n**Q4.** Feature extraction \"requires no GPU\" 且 \"2 minutes per 5,000 samples on a single CPU core\" (Appendix §Q)。但 reference model forward pass（Pythia-1.4B）是否确实在 CPU 上运行？如果是，这在大规模部署中是否可行？如果需要 GPU，请修正这一声明。\n\n**Q5.** 论文声称 \"no per-passage lineage exists across depths\" (§2.2)。能否更明确地解释：不同深度的 5,000 个样本是否有任何间接的数据依赖关系？例如，d1 数据是在 d0 上微调后生成的，d2 数据是在 d1 上微调后生成的——即使单个 passage 无对应关系，训练数据的统计特性是有传递性的，这对 CV split 的独立性假设有何影响？\n\n---\n\n## Missing References (遗漏的重要文献)\n\n1. **Shumailov et al. (2024) \"The Curse of Recursion\"** — 虽然 Nature 版本已引用，但 arXiv 预印本中有更多关于 tail erosion 的量化分析，与本文的 p90_ppl 发现直接相关。(注: 可能已覆盖，需确认 Nature 版本是否包含相同内容)\n\n2. 引用验证中 1 条孤立 bib entry (c2pa2024, C2PA Specification) 未在正文中引用——若不使用应删除。\n\n3. 引用验证中 5 条轻微 mismatch（多为第一作者名变体或年份差异）：alemohammad2024_mad, garces_arias2025_decoding_decoded, he2021_deberta_v3 (year: bib=2023 vs api=2021), llama3, guo2024_biscope。建议核实并修正。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5/5\n**Excitement**: 3.0/5\n**Confidence**: 4/5\n\n### 评分理由\n\n**Soundness (3.5)**: 问题定义清晰，实验方法论基本严谨，统计实践透明。主要扣分点：(1) cross-scale 实验的混杂因素使核心结论之一（scale-dependent attenuation）缺乏可靠支撑；(2) d0 膨胀虽被讨论但在 headline 数字呈现上仍有误导性；(3) curation PoC 不显著却作为动机之一。\n\n**Excitement (3.0)**: 问题定义新颖且 timely（递归污染是活跃研究领域），EDD 度量有概念贡献。但 (1) 核心发现（depth signal exists in tail statistics）在模型坍塌理论预测之下并不 surprising；(2) 方法（RF on hand-crafted features）缺乏算法创新；(3) cross-strategy 失败和 scale attenuation 大幅限制了实际影响力——该方法目前仅在\"已知策略 + 1-1.5B 模型\"条件下 reliably works，这一条件在实践中罕见。\n\n**一句话总结**: 一项定义新颖、执行严谨但实用性受限的实证研究——在可控条件下证明了递归深度信号的存在，但距离实际部署（未知策略、大模型）有显著差距，适合作为 Findings 论文发表。\n\n---\n\n## Detailed Comments (逐 section)\n\n### Abstract\n- 信息密度高但几乎不可能一次读懂。建议减少括号内的数字堆砌，将核心结果分为 2-3 个清晰的 claim 层级。\n- \"69-86% four-class accuracy\" 应伴随 \"d1-d3 balanced: 59-82%\" 作为等权的修正数字。\n- \"cross-model transfer reaches 66.4% (2.7× chance)\" 中的 d1-d3 数字 (55.4%) 应被提升到同等显著位置。\n\n### Introduction (§1)\n- 叙事线清晰：递归循环 → 现有工具的空白 → perplexity tail fingerprint 的发现 → 贡献总结。\n- 第 3 段 \"consistent in direction but scale-dependent in magnitude\" 是一个好的 qualifier。\n- Contribution 列表第 3 点过于冗长，应将数字细节移至正文。\n\n### Related Work (§2)\n- 覆盖全面：model collapse theory、AI text detection、membership inference、adjacent tasks、ordinal classification、decoding strategies。\n- 与 Mohamed et al. (2025, \"Broken Telephone\") 的区分清晰：\"characterize how text degrades\" vs \"classify which iteration\"。\n- 引用密度适当（67 unique cited keys）。\n\n### Method (§3)\n- Problem Definition (§2.1): 形式化清晰。建议增加一段讨论 full-replacement vs accumulation setting 的区别。\n- Benchmark (§2.2): \"BOS-seeded generation may amplify depth signal\" — 好的自我审视。但 prompted validation 仅在 1/9 cells 上做了 (GPT-2 XL nucleus)，推广性未确立。\n- Features (§2.3): 设计合理但应更突出 effective dimensionality ~4-5 的发现。\n- EDD (§2.4): 定义数学上自洽。Footnote 2 关于 non-monotonic AUC 的讨论是必要的。\n\n### Theory (§3.1)\n- \"Scale-dependent attenuation\" 的理论预测 (α closer to 1 for larger models) 是合理的。\n- Strategy-dependent convergence 的预测与 GPT-2 XL 数据精确匹配 (92.2 vs 92.3) — 但这是 cherry-picked 的单一比较，需注意不要过度泛化。\n\n### Atlas (§4)\n- §4.1: 结构清晰，交叉效应（strategy effect 9.3pp vs model effect 7.2pp）是有趣的发现。\n- §4.2: Feature importance analysis 的主要问题是 multicollinearity (W6)。\n- §4.4: AUC decay analysis 和 EDD threshold sensitivity 是论文最有价值的分析之一。d3-vs-d4 AUC 在三个模型间的 convergence (0.750-0.784) 特别有说服力。\n\n### Generalization (§5)\n- §5.1: Baseline comparison 全面且公平。RF/XGB/LightGBM convergence within 0.4pp 有力地证明了 feature-determined ceiling。\n- §5.2: Cross-model transfer 的 d2 recall (26.8-52.6%) 是最大的弱点，特别是 Pythia holdout 的 26.8%。\n- §5.3: Cross-strategy failure 是论文最重要的负面结果。Two-stage pipeline 的 11.5pp recovery 是有趣的工程方向。\n- §5.4: Cross-scale observations 标记为 \"Preliminary\" 是恰当的。\n\n### Discussion/Conclusion\n- Discussion 过于简短（单独成节只有一段），未充分讨论 open questions。\n- 建议扩展 Discussion 部分，特别是: (1) accumulation setting; (2) 与 model collapse mitigation 策略的交互; (3) 向实际部署的 roadmap。\n\n### Limitations\n- 覆盖广泛且诚实。特别值得肯定的是 domain-dependent FPR 分析（C4 上 22.4% FPR）和 adversarial robustness 的坦诚承认。\n- 建议增加：passage-level 假设（论文假设每个 passage 深度均匀）在真实 mixed-depth documents 中的限制。（实际上 Appendix §N 讨论了 mixed-depth，但 Limitations 中未提及 segment-level estimation。更新：重新检查发现 Limitations 倒数第二段确实提到了 \"Segment-level estimation in mixed-depth documents remains open\"，这一点已覆盖。）\n\n### Appendix\n- 信息量极大，覆盖了几乎所有可预见的 reviewer 问题。\n- Temperature robustness (Appendix §E) 中 \"memorization as prerequisite\" 的发现（τ=1.1 下信号消失）是一个重要的机制性洞察。\n- Domain bias analysis (Appendix §G) 是论文的一大亮点。\n\n### 格式合规\n- `\\documentclass[11pt]{article}` + `\\usepackage[review]{acl}` — 符合 ACL 2025 模板要求。\n- 匿名化：作者为 \"Anonymous\"，正文中无自引泄露。\n- bib 中 1 条孤立条目 (c2pa2024) 应清理。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-19T03:05:17.087049+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4571
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-19T03:05:24.031489+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 ACL ARR reviewer guidelines 和评分标准', 'status': 'completed', 'activeForm': '搜索 ACL ARR reviewer guidelines'}, {'content': '通读论文全文（所有章节）', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '验证引用完整性和真实性', 'status': 'completed', 'activeForm': '验证引用完整性和真实性'}, {'content': '撰写审稿意见并汇报 Director', 'status': 'completed', 'activeForm': '撰写审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 ACL ARR reviewer guidelines 和评分标准', 'status': 'completed', 'activeForm': '搜索 ACL ARR reviewer guidelines'}, {'content': '通读论文全文（所有章节）', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '验证引用完整性和真实性', 'status': 'completed', 'activeForm': '验证引用完整性和真实性'}, {'content': '撰写审稿意见并汇报 Director', 'status': 'completed', 'activeForm': '撰写审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-19T03:05:24.132388+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 610 · 2026-05-19T03:05:32.899828+00:00_

Round 1 审稿意见已完成并提交给 Review Director。

**评分摘要**：Overall 3.0 (Findings)，Soundness 3.5/5，Excitement 3.0/5，Confidence 4/5。

**核心判断**：问题定义新颖、实验执行严谨、统计实践透明，但两个根本性限制压制了评分：(1) cross-strategy transfer 在 d1-d3 上仅 45.9%（部署场景下策略通常未知），(2) 生态效度差距大（可控 LoRA 微调 vs 真实递归污染）。方法无算法创新（RF on hand-crafted features），且 curation PoC 不显著。适合 Findings 发表。

提出了 2 个 Must-Fix（scope 声明 + cross-strategy framing）、4 个 Should-Fix（d0 膨胀呈现、cross-scale 证据不足、curation PoC、多重共线性）、3 个 Minor，以及 5 个需要作者回答的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 23

## Round 23

4 recorded events


### User

_source line 611 · 2026-05-19T03:06:53.686645+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每一条 Weakness 和 Question，标注：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注与你自己意见的**共识和分歧**。

---

以下是 Reviewer 2 的完整审稿原文：

## Reviewer 2 — Round 1 审稿意见

**审查侧重：新颖性 + 完整性 + 写作质量 + Related Work 覆盖度**

### Summary
本文提出将"递归生成深度估计"形式化为序数分类任务，构建了 180K 样本的基准测试，使用 19 个统计特征的 RF 在 1-1.5B 模型上达到 69-86% 的四分类精度。工作在任务定义和系统性实证分析上有真正的贡献，但在算法新颖性、规模可扩展性和生态效度方面存在显著局限。

### Strengths
S1. 任务定义的原创性。
S2. 系统性实验设计。
S3. 透明的局限性和诚实的报告。
S4. Feature analysis 的洞察。
S5. Related Work 覆盖充分（67 条引用）。

### Weaknesses
W1 [Must-Fix]. 规模可扩展性是致命瓶颈。14B 的 EDD_{0.70}=0，d0-vs-d1 AUC 降至 0.643。如果方法在 14B 已基本失效，70B+ 的可行性令人严重怀疑。

W2 [Must-Fix]. 生态效度差距过大。Benchmark 使用高度受控流程，真实世界涉及混合语料、未知比例、多模型、后处理等。

W3 [Must-Fix]. 算法贡献不足以支撑 EMNLP Main。分类器是标准 RF，特征是标准 perplexity 统计量。RF/XGBoost/LightGBM 在 0.4pp 内收敛说明方法论贡献几乎为零。

W4 [Should-Fix]. Abstract 信息过载（200 词中 20+ 数字）。

W5 [Should-Fix]. Discussion 实质缺失（Section 7 仅一段约 80 词）。

W6 [Should-Fix]. d0 通胀需要更突出处理。d1-d3 balanced accuracy 仅 55.4% (cross-model) 和 45.9% (cross-strategy)。

W7 [Should-Fix]. Downstream utility 证据不足。Curation PoC RF vs unfiltered p>0.4 不显著。

W8 [Minor]. 写作存在轻微 AI 痕迹。

W9 [Minor]. Feature trajectory 图被移入 Appendix，应保留正文。

### Questions
Q1. 14B EDD=0 是否意味着 perplexity-based features 路线在规模增长下注定失效？Higher-order moments 是否暗示 feature adaptation 策略？
Q2. Cross-model chains 高于部分 within-distribution cells，是否因为多模型 shift 更大更易检测？
Q3. Prompted generation 只验证 1/9 cells，13.8pp 下降是否被低估？
Q4. τ=1.1 时 depth signal 消失，是否意味着高 temperature 可规避 depth estimation？

### Missing References
1. Muennighoff et al. (2024) "Scaling Data-Constrained Language Models"
2. Self-play / iterative self-improvement 文献
3. Ilyas et al. (2022) "Datamodels"
4. 孤立 bib entry: c2pa2024

### Overall: 3.0 (Findings), Confidence 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-19T03:08:22.618131+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 规模可扩展性是致命瓶颈。**\n同意这是核心问题。14B 的 EDD_{0.70}=0（Table in §5.4 / Appendix §K）确实令人担忧。但我补充两点 nuance：\n1. 14B 的 d0v1 AUC=0.643 存在自参考混杂（Qwen2.5-14B 用自身做 reference model，与所有其他实验用 Pythia-1.4B 不同），论文在 Appendix §K Confounds 中明确列出了这一点。因此 14B 的数字不能直接与 1-1.5B 比较——信号衰减和参考模型变更的效应被混淆了。\n2. 但即便打折，d1-d3 balanced accuracy 57.4%（chance=33%）说明信号确实在衰减。R2 的推论（70B+ 可行性存疑）是合理的。\n建议作者：如果可能，用 Pythia-1.4B 作为 14B 的 reference model 补充一组实验，以分离 scale effect 和 reference model effect。\n\n**[AGREE] R2-W2: 生态效度差距过大。**\n与我的 W1 完全一致。我在自己的审稿中也将此列为 Must-Fix。论文的 full-replacement recursive chain 与真实世界的 accumulation setting 存在结构性差异。论文 Limitations 中的 \"Controlled vs. ecological setting\" 段承认了这一点，但 framing 不够突出。\n\n**[REBUT] R2-W3: 算法贡献不足以支撑 EMNLP Main。**\n部分不同意。R2 认为 \"方法论贡献几乎为零\"，但我认为这低估了以下贡献：\n1. **任务形式化本身就是贡献**——论文第 18 行明确声明 \"This paper is an empirical study and problem formalization rather than an algorithmic contribution\"（Introduction §1）。EMNLP/ACL 接收过大量以 benchmark + systematic analysis 为主的论文（如 RAID [Dugan et al. 2024, cited]、M4-SemEval [Wang et al. 2024, cited]），算法新颖性不是唯一接收标准。\n2. **EDD 度量**是一个有概念价值的新定义（Definition 1, §2.4），虽然数学上简单，但将 model collapse 的理论预测操作化为可测量的度量。\n3. **Depth Degradation Atlas** 的系统性分析揭示了非平凡的发现：strategy effect (9.3pp) > model effect (7.2pp)（§4.1）；feature hierarchy 随深度变化（shallow: var_surprisal dominates, deep: p90_ppl dominates, §4.2）；temperature d1 ≈ nucleus d2 的精确验证（§3.3）。\n4. RF/XGB/LightGBM 收敛恰恰证明了 **feature 的价值**而非方法论的无贡献——它意味着核心贡献在 feature design + task formalization，而非 classifier engineering。\n\n但我同意这更适合 Findings 而非 Main（与我的 Overall 3.0 一致），因为缺乏推动方法边界的算法创新。R2 将此定为 Must-Fix 似乎过强——这是 scope/positioning 问题而非缺陷。\n\n**[AGREE] R2-W4: Abstract 信息过载。**\n同意。Abstract 7 行中塞入了 20+ 数字和多层括号嵌套，一次阅读几乎无法消化。我在自己的 Detailed Comments 中也指出了这一点。建议作者将 Abstract 重构为 3 个清晰的 claim 层级，数字细节移至正文。\n\n**[AGREE] R2-W5: Discussion 实质缺失。**\n同意。Section 7 仅一段约 80 词，实质上是 Results 的摘要而非 Discussion。我在自己的 Detailed Comments 中也建议扩展 Discussion，特别是 (1) accumulation setting, (2) 与 model collapse mitigation 策略的交互, (3) 向实际部署的 roadmap。Appendix §P \"Extended Discussion\" 有更多内容，但核心 discussion 不应被放逐到附录。\n\n**[AGREE] R2-W6: d0 通胀需要更突出处理。**\n与我的 W3 完全一致。d1-d3 balanced accuracy 55.4% (cross-model) 和 45.9% (cross-strategy) 才是评估该方法实际能力的关键数字。Abstract 中这些数字被淹没在括号嵌套中。\n\n**[AGREE] R2-W7: Downstream utility 证据不足。**\n与我的 W5 完全一致。RF vs unfiltered p=0.407 是不显著的。RF vs random 的显著结果（p<0.02）未做多重比较校正。\n\n**[REBUT] R2-W8: 写作存在轻微 AI 痕迹。**\nR2 未给出具体例子，这一评价缺乏证据支撑。论文 Ethics Statement 最后一行坦诚声明 \"This research used AI coding assistants for experiment implementation and writing drafts. All scientific decisions, experimental design, and result interpretation were conducted by the authors.\"（Limitations/Ethics §末尾）。在当前学术环境下，使用 AI 辅助写作是常见做法，只要科学判断由作者做出。除非 R2 能指出具体的 AI 痕迹导致了理解障碍或质量下降，否则这不应作为评分依据。我自己通读全文，写作质量总体在 acceptable 范围内（信息密度过高是独立问题）。\n\n**[AGREE] R2-W9: Feature trajectory 图被移入 Appendix。**\n同意。Figure (fig_feature_trajectory, Appendix §C) 是理解 depth signal 的直觉关键图——展示了 p90_ppl、var_surprisal、rep_3gram 跨深度的单调变化轨迹。正文 §4.3 提到了 monotonicity 结果但读者看不到图，削弱了可读性。建议移回正文，可缩小尺寸。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: 14B EDD=0 是否意味着 perplexity-based features 路线注定失效？**\n好问题。论文 Appendix §K 段 (3) 确实观察到 14B 的 feature importance 发生结构性转变（higher-order moments 取代 first-order tail statistics），这暗示了一种可能的 feature adaptation 路线。但论文未探索这一方向。我认为这是 future work 而非当前论文的缺陷——论文明确将 cross-scale 标记为 \"Preliminary\"（§5.4 标题）。\n\n**[REBUT] R2-Q2: Cross-model chains 高于部分 within-distribution cells，是否因为多模型 shift 更大更易检测？**\nR2 的假设有一定道理，但论文提供了反证：reverse-chain control（GPT-2 XL→OLMo→Pythia）达到 85.75%，与 forward chain（84.75%）统计不可区分（Appendix §K \"Reverse-chain control\"）。如果高准确率仅因为 \"多模型 shift 更大\"，那么 reverse chain 应该产生不同的 per-depth accuracy pattern（因为 model-depth assignment 完全反转），但两者的准确率几乎相同。更可能的解释是：跨模型链中每步的分布 shift 是**累积的**（depth signal + architecture shift 叠加），而非单纯由 architecture fingerprint 驱动。不过我同意 confound 未被完全排除——84.75% 中有多少来自 depth signal vs architecture shift 的定量分解是缺失的。\n\n**[AGREE] R2-Q3: Prompted generation 只验证 1/9 cells，13.8pp 下降是否被低估？**\n与我在 W1 中的观点一致。论文 Limitations 倒数第 2 段承认 \"Prompted generation was validated on only 1 of 9 cells (GPT-2 XL nucleus); generalization to other model-strategy configurations under prompted conditions is not established.\" 但这一 caveat 在正文 §5.3 和 Abstract 中不够突出。如果其他 cells（特别是较弱的 Pythia top-k, 68.9%）下的 prompted-generation drop 更大，实际性能可能低于 55%。\n\n**[AGREE] R2-Q4: τ=1.1 时 depth signal 消失，是否意味着高 temperature 可规避？**\n是的，这是一个有意义的 adversarial 发现。Appendix §E 的 \"memorization as prerequisite\" 分析（τ=1.1 时训练 loss 几乎不下降，2.27→1.91→1.85）提供了机制解释：高 entropy 输出抵抗 memorization，因此 depth-dependent distributional shift 不会累积。但需要注意：τ=1.1 的文本质量可能已显著下降（higher entropy = more noise），所以 \"规避 depth estimation\" 的代价是生成质量损失。论文未讨论这一 trade-off。\n\n---\n\n### Missing References 回应\n\n**[AGREE] R2-MR1: Muennighoff et al. (2024) \"Scaling Data-Constrained Language Models\"。** 相关——讨论了数据量与模型规模的 scaling，与本文的 scale-dependent attenuation 有联系。应引用。\n\n**[REBUT] R2-MR2: Self-play / iterative self-improvement 文献。** 方向相关但不直接。Self-play 中的 iteration 是 policy optimization，不是 recursive generation chain。不是必须引用但可在 Related Work \"Adjacent Tasks\" 段提及。\n\n**[AGREE] R2-MR3: Ilyas et al. (2022) \"Datamodels\"。** 与 data provenance 和 data influence 相关，可在 Extended Discussion \"Toward a provenance toolkit\" 段引用。\n\n**[AGREE] R2-MR4: 孤立 bib entry c2pa2024。** 与我的引用验证结果一致——c2pa2024 在 bib 中但未被引用，应删除或在 Discussion 中引用。\n\n---\n\n### 共识与分歧总结\n\n**核心共识（R1 与 R2 一致的问题）：**\n1. 生态效度差距（R1-W1, R2-W2）\n2. d0 膨胀的 headline 误导性（R1-W3, R2-W6）\n3. Downstream utility 不显著（R1-W5, R2-W7）\n4. Abstract 信息过载（R1-Detailed, R2-W4）\n5. Discussion 缺失（R1-Detailed, R2-W5）\n6. Prompted generation 验证不足（R1-Q implicit, R2-Q3）\n7. 孤立 bib entry c2pa2024（R1-MR, R2-MR4）\n\n**主要分歧：**\n1. **算法贡献 (R2-W3)**：R2 认为 Must-Fix，我认为这是 scope/positioning 问题而非缺陷。论文明确自我定位为 empirical study + problem formalization。Benchmark + systematic analysis 类论文在 *ACL 有先例（RAID, M4-SemEval）。更适合 Findings 但不是 reject 理由。\n2. **AI 写作痕迹 (R2-W8)**：R2 未提供具体例子，我认为在作者已坦诚声明使用 AI 辅助的情况下，这不应作为评分依据。\n3. **Scale 问题的严重程度 (R2-W1 vs R1-W4)**：R2 将此列为 Must-Fix（\"致命瓶颈\"），我列为 Should-Fix。区别在于：我认为 14B 的自参考混杂使该数据点不可靠，因此 \"scale attenuation\" 的证据本身是 weak 的（既不能证明 works 也不能证明 fails）；R2 将 14B 结果视为 face value 并推断 70B+ 必然失效。在混杂未被分离之前，两种推断都缺乏充分依据。\n\n**评分一致：** 两位 Reviewer 均给出 Overall 3.0 (Findings), Confidence 4/5。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 规模可扩展性是致命瓶颈。**\n同意这是核心问题。14B 的 EDD_{0.70}=0（Table in §5.4 / Appendix §K）确实令人担忧。但我补充两点 nuance：\n1. 14B 的 d0v1 AUC=0.643 存在自参考混杂（Qwen2.5-14B 用自身做 reference model，与所有其他实验用 Pythia-1.4B 不同），论文在 Appendix §K Confounds 中明确列出了这一点。因此 14B 的数字不能直接与 1-1.5B 比较——信号衰减和参考模型变更的效应被混淆了。\n2. 但即便打折，d1-d3 balanced accuracy 57.4%（chance=33%）说明信号确实在衰减。R2 的推论（70B+ 可行性存疑）是合理的。\n建议作者：如果可能，用 Pythia-1.4B 作为 14B 的 reference model 补充一组实验，以分离 scale effect 和 reference model effect。\n\n**[AGREE] R2-W2: 生态效度差距过大。**\n与我的 W1 完全一致。我在自己的审稿中也将此列为 Must-Fix。论文的 full-replacement recursive chain 与真实世界的 accumulation setting 存在结构性差异。论文 Limitations 中的 \"Controlled vs. ecological setting\" 段承认了这一点，但 framing 不够突出。\n\n**[REBUT] R2-W3: 算法贡献不足以支撑 EMNLP Main。**\n部分不同意。R2 认为 \"方法论贡献几乎为零\"，但我认为这低估了以下贡献：\n1. **任务形式化本身就是贡献**——论文第 18 行明确声明 \"This paper is an empirical study and problem formalization rather than an algorithmic contribution\"（Introduction §1）。EMNLP/ACL 接收过大量以 benchmark + systematic analysis 为主的论文（如 RAID [Dugan et al. 2024, cited]、M4-SemEval [Wang et al. 2024, cited]），算法新颖性不是唯一接收标准。\n2. **EDD 度量**是一个有概念价值的新定义（Definition 1, §2.4），虽然数学上简单，但将 model collapse 的理论预测操作化为可测量的度量。\n3. **Depth Degradation Atlas** 的系统性分析揭示了非平凡的发现：strategy effect (9.3pp) > model effect (7.2pp)（§4.1）；feature hierarchy 随深度变化（shallow: var_surprisal dominates, deep: p90_ppl dominates, §4.2）；temperature d1 ≈ nucleus d2 的精确验证（§3.3）。\n4. RF/XGB/LightGBM 收敛恰恰证明了 **feature 的价值**而非方法论的无贡献——它意味着核心贡献在 feature design + task formalization，而非 classifier engineering。\n\n但我同意这更适合 Findings 而非 Main（与我的 Overall 3.0 一致），因为缺乏推动方法边界的算法创新。R2 将此定为 Must-Fix 似乎过强——这是 scope/positioning 问题而非缺陷。\n\n**[AGREE] R2-W4: Abstract 信息过载。**\n同意。Abstract 7 行中塞入了 20+ 数字和多层括号嵌套，一次阅读几乎无法消化。我在自己的 Detailed Comments 中也指出了这一点。建议作者将 Abstract 重构为 3 个清晰的 claim 层级，数字细节移至正文。\n\n**[AGREE] R2-W5: Discussion 实质缺失。**\n同意。Section 7 仅一段约 80 词，实质上是 Results 的摘要而非 Discussion。我在自己的 Detailed Comments 中也建议扩展 Discussion，特别是 (1) accumulation setting, (2) 与 model collapse mitigation 策略的交互, (3) 向实际部署的 roadmap。Appendix §P \"Extended Discussion\" 有更多内容，但核心 discussion 不应被放逐到附录。\n\n**[AGREE] R2-W6: d0 通胀需要更突出处理。**\n与我的 W3 完全一致。d1-d3 balanced accuracy 55.4% (cross-model) 和 45.9% (cross-strategy) 才是评估该方法实际能力的关键数字。Abstract 中这些数字被淹没在括号嵌套中。\n\n**[AGREE] R2-W7: Downstream utility 证据不足。**\n与我的 W5 完全一致。RF vs unfiltered p=0.407 是不显著的。RF vs random 的显著结果（p<0.02）未做多重比较校正。\n\n**[REBUT] R2-W8: 写作存在轻微 AI 痕迹。**\nR2 未给出具体例子，这一评价缺乏证据支撑。论文 Ethics Statement 最后一行坦诚声明 \"This research used AI coding assistants for experiment implementation and writing drafts. All scientific decisions, experimental design, and result interpretation were conducted by the authors.\"（Limitations/Ethics §末尾）。在当前学术环境下，使用 AI 辅助写作是常见做法，只要科学判断由作者做出。除非 R2 能指出具体的 AI 痕迹导致了理解障碍或质量下降，否则这不应作为评分依据。我自己通读全文，写作质量总体在 acceptable 范围内（信息密度过高是独立问题）。\n\n**[AGREE] R2-W9: Feature trajectory 图被移入 Appendix。**\n同意。Figure (fig_feature_trajectory, Appendix §C) 是理解 depth signal 的直觉关键图——展示了 p90_ppl、var_surprisal、rep_3gram 跨深度的单调变化轨迹。正文 §4.3 提到了 monotonicity 结果但读者看不到图，削弱了可读性。建议移回正文，可缩小尺寸。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: 14B EDD=0 是否意味着 perplexity-based features 路线注定失效？**\n好问题。论文 Appendix §K 段 (3) 确实观察到 14B 的 feature importance 发生结构性转变（higher-order moments 取代 first-order tail statistics），这暗示了一种可能的 feature adaptation 路线。但论文未探索这一方向。我认为这是 future work 而非当前论文的缺陷——论文明确将 cross-scale 标记为 \"Preliminary\"（§5.4 标题）。\n\n**[REBUT] R2-Q2: Cross-model chains 高于部分 within-distribution cells，是否因为多模型 shift 更大更易检测？**\nR2 的假设有一定道理，但论文提供了反证：reverse-chain control（GPT-2 XL→OLMo→Pythia）达到 85.75%，与 forward chain（84.75%）统计不可区分（Appendix §K \"Reverse-chain control\"）。如果高准确率仅因为 \"多模型 shift 更大\"，那么 reverse chain 应该产生不同的 per-depth accuracy pattern（因为 model-depth assignment 完全反转），但两者的准确率几乎相同。更可能的解释是：跨模型链中每步的分布 shift 是**累积的**（depth signal + architecture shift 叠加），而非单纯由 architecture fingerprint 驱动。不过我同意 confound 未被完全排除——84.75% 中有多少来自 depth signal vs architecture shift 的定量分解是缺失的。\n\n**[AGREE] R2-Q3: Prompted generation 只验证 1/9 cells，13.8pp 下降是否被低估？**\n与我在 W1 中的观点一致。论文 Limitations 倒数第 2 段承认 \"Prompted generation was validated on only 1 of 9 cells (GPT-2 XL nucleus); generalization to other model-strategy configurations under prompted conditions is not established.\" 但这一 caveat 在正文 §5.3 和 Abstract 中不够突出。如果其他 cells（特别是较弱的 Pythia top-k, 68.9%）下的 prompted-generation drop 更大，实际性能可能低于 55%。\n\n**[AGREE] R2-Q4: τ=1.1 时 depth signal 消失，是否意味着高 temperature 可规避？**\n是的，这是一个有意义的 adversarial 发现。Appendix §E 的 \"memorization as prerequisite\" 分析（τ=1.1 时训练 loss 几乎不下降，2.27→1.91→1.85）提供了机制解释：高 entropy 输出抵抗 memorization，因此 depth-dependent distributional shift 不会累积。但需要注意：τ=1.1 的文本质量可能已显著下降（higher entropy = more noise），所以 \"规避 depth estimation\" 的代价是生成质量损失。论文未讨论这一 trade-off。\n\n---\n\n### Missing References 回应\n\n**[AGREE] R2-MR1: Muennighoff et al. (2024) \"Scaling Data-Constrained Language Models\"。** 相关——讨论了数据量与模型规模的 scaling，与本文的 scale-dependent attenuation 有联系。应引用。\n\n**[REBUT] R2-MR2: Self-play / iterative self-improvement 文献。** 方向相关但不直接。Self-play 中的 iteration 是 policy optimization，不是 recursive generation chain。不是必须引用但可在 Related Work \"Adjacent Tasks\" 段提及。\n\n**[AGREE] R2-MR3: Ilyas et al. (2022) \"Datamodels\"。** 与 data provenance 和 data influence 相关，可在 Extended Discussion \"Toward a provenance toolkit\" 段引用。\n\n**[AGREE] R2-MR4: 孤立 bib entry c2pa2024。** 与我的引用验证结果一致——c2pa2024 在 bib 中但未被引用，应删除或在 Discussion 中引用。\n\n---\n\n### 共识与分歧总结\n\n**核心共识（R1 与 R2 一致的问题）：**\n1. 生态效度差距（R1-W1, R2-W2）\n2. d0 膨胀的 headline 误导性（R1-W3, R2-W6）\n3. Downstream utility 不显著（R1-W5, R2-W7）\n4. Abstract 信息过载（R1-Detailed, R2-W4）\n5. Discussion 缺失（R1-Detailed, R2-W5）\n6. Prompted generation 验证不足（R1-Q implicit, R2-Q3）\n7. 孤立 bib entry c2pa2024（R1-MR, R2-MR4）\n\n**主要分歧：**\n1. **算法贡献 (R2-W3)**：R2 认为 Must-Fix，我认为这是 scope/positioning 问题而非缺陷。论文明确自我定位为 empirical study + problem formalization。Benchmark + systematic analysis 类论文在 *ACL 有先例（RAID, M4-SemEval）。更适合 Findings 但不是 reject 理由。\n2. **AI 写作痕迹 (R2-W8)**：R2 未提供具体例子，我认为在作者已坦诚声明使用 AI 辅助的情况下，这不应作为评分依据。\n3. **Scale 问题的严重程度 (R2-W1 vs R1-W4)**：R2 将此列为 Must-Fix（\"致命瓶颈\"），我列为 Should-Fix。区别在于：我认为 14B 的自参考混杂使该数据点不可靠，因此 \"scale attenuation\" 的证据本身是 weak 的（既不能证明 works 也不能证明 fails）；R2 将 14B 结果视为 face value 并推断 70B+ 必然失效。在混杂未被分离之前，两种推断都缺乏充分依据。\n\n**评分一致：** 两位 Reviewer 均给出 Overall 3.0 (Findings), Confidence 4/5。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-19T03:08:26.785303+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4167
}
```

</details>

---


### Assistant

_source line 614 · 2026-05-19T03:08:33.959546+00:00_

交叉回应已提交给 Review Director。

总结：与 Reviewer 2 在 7 个核心问题上达成共识（生态效度、d0 膨胀、downstream PoC 不显著、Abstract 过载、Discussion 缺失、prompted validation 不足、孤立引用）。主要分歧在 3 点：(1) 算法贡献是否构成 Must-Fix（我认为是 positioning 问题而非缺陷），(2) AI 写作痕迹的指控缺乏具体证据，(3) 14B scale 问题的严重程度因自参考混杂而存在不确定性。两位 Reviewer 评分一致：Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 24

## Round 24

54 recorded events


### User

_source line 615 · 2026-05-19T06:34:31.217355+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计声明）

### Venue 信息
- **目标**: EMNLP 2026 (ARR May cycle)
- **截止日期**: 2026-05-25
- **页数**: Long paper, 8 页正文 + 无限引用/附录
- **模板**: ACL style template (review mode, double-blind)
- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

### 论文路径
`projects/recursive_gen_depth_est/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, theory.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）

### 你的审查侧重

**核心任务**：评估论文的方法严谨性、实验设计质量和统计声明的可靠性。

请重点审查以下方面：

1. **实验设计**
   - Benchmark 构建（180K 样本, 3×3 grid, d0-d3）是否存在数据泄露或系统性偏差
   - Full-replacement chain 的 scope 声明是否充分，与 accumulation setting 的差距讨论是否到位
   - Cross-validation 设计是否合理（5-fold stratified CV）
   - LoRA finetuning 配置的合理性（单一超参、fresh adapter）

2. **统计声明的可靠性**
   - 所有 accuracy/AUC 数字是否有充分的置信区间和统计检验
   - d0 recall >97% 对 headline metrics 的膨胀问题：d1-d3 balanced accuracy 是否被系统性地并列报告
   - Cross-scale 实验（7-14B）的 5 个混杂因素是否被充分讨论
   - Curation PoC（Appendix）主比较 p>0.4 不显著，多重比较是否校正
   - Cross-seed replication 仅覆盖 3/9 cells，single-seed uncertainty 估计

3. **方法**
   - EDD 定义的严谨性：contiguous prefix 要求在非单调情况下是否过于保守
   - Reference model (Pythia-1.4B) 与 generator 重叠的 circularity 风险
   - RF ordinal claim 的强度是否与 CORAL baseline 对比证据匹配
   - 19 features 中 14-16 个 VIF>10 高共线性下的 feature importance 解释

4. **可复现性**
   - 超参细节是否充足
   - 代码/数据承诺（upon acceptance）
   - 计算资源报告

### 输出格式

请按以下结构输出审稿意见：
- **Summary**: 2-3 句论文概述
- **Strengths**: 逐条列出（S1, S2, ...）
- **Weaknesses**: 逐条列出（W1, W2, ...），每条标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]
- **Questions**: 需要作者回答的问题
- **Missing References**: 遗漏的重要相关工作
- **Overall Assessment**: 评分 + 置信度 + 1-2 句总结
- **Detailed Comments**: 按 section 逐节详细评论

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-19T06:34:40.814437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-19T06:34:40.817112+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-19T06:34:40.867745+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-19T06:34:40.868306+00:00_

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
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{theory}
39	
40	\input{atlas}
41	
42	\input{generalization}
43	
44	\input{discussion}
45	
46	\input{conclusion}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{section_appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-19T06:34:43.982519+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-19T06:34:44.384987+00:00_

1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification, constructing a 180K-passage benchmark spanning 3 model families, 3 decoding strategies, and 4 depths under controlled full-replacement recursive chains at the 1--1.5B scale.
4	A Random Forest over 19 statistical features, dominated by the perplexity tail family (\texttt{p90\_ppl}, \texttt{var\_surprisal}), achieves 69--86\% four-class accuracy (d1--d3 balanced: 59--82\%; chance = 25\%/33\%); the convergence of RF, XGBoost, and LightGBM within 0.4\,pp confirms that discriminative signal resides in feature design, not classifier choice.
5	Cross-model transfer reaches 66.4\% four-class (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, and a single-cell prompted-generation test 69.5\%.
6	Cross-strategy transfer (59.1\%, d1--d3: 45.9\%) reveals that decoding strategies induce structurally distinct degradation trajectories, a finding we formalize via the \emph{Effective Discriminable Depth} (EDD) metric ($\mathrm{EDD}_{0.70}{=}4$ for all three families).
7	Preliminary cross-scale experiments (7--14B, 54--70\%) provide an existence proof that depth signal persists at larger scales, though confounded by five factors including quantization and vocabulary mismatch.
8	Binary detectors and membership inference baselines (30--35\%) fall ${>}$43\,pp below our pipeline, confirming that ordinal depth estimation requires distributional statistics inaccessible from surface text.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-19T06:34:44.385421+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-19T06:34:44.837625+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	We study this question under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination typically involves partial mixing (accumulation), where synthetic and human data co-exist at unknown proportions; the full-replacement setting provides an upper bound on depth signal strength, and we discuss implications for accumulation settings in \S\ref{sec:discussion}.
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
11	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
12	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
13	No exi
…[truncated 3395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-19T06:34:44.838140+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-19T06:34:45.340858+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad}.
6	Subsequent work refines the conditions under which collapse occurs: \citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \S\ref{sec:method:theory}), \citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.
7	Mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, data scaling under constraint \cite{muennighoff2023scaling}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence analysis \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026} are active areas.
8	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena and call for operationally precise metrics; we respond by operationalizing tail-erosion predictions into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt
…[truncated 2904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-19T06:34:45.341290+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-19T06:34:45.844831+00:00_

1	\section{Method}
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
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 5915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-19T06:34:45.845395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-19T06:34:46.750174+00:00_

1	\subsection{Theoretical Grounding}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed by its dominance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--80\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), so EDD should decrease with scale.
15	Qwen2.5-14B confirms this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B), while d1--d3 AUCs remain above 0.70 (\S\ref{sec:gen:crossscale}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$(d{+}1)$ text in tail statistics.
20	GPT-2~XL confirms this: temperature d1 median \texttt{p90\_ppl} (92.
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-19T06:34:46.750696+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-19T06:34:47.566706+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}1{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: MAE\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$).}
22	\label{tab:main_matrix}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}lccc@{}}
25	\toprule
26	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
27	\midrule
28	Pythia-1.4B  & 78.7{\scriptsize$\pm$0.6}\,(
…[truncated 8458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 816
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-19T06:34:47.617454+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-19T06:34:47.669214+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares ordinal depth estimation methods across all 9 atlas cells.
10	RF, XGBoost, and LightGBM on the same 19 features converge within 0.4\,pp per cell, confirming a feature-determined ceiling; on Pythia nucleus, CORAL \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match RF within 0.6\,pp ($p>0.05$).
11	
12	\paragraph{Binary detectors and membership inference.}
13	Four binary detection/membership inference methods, calibrated for ordinal depth, all fall 43--48\,pp below RF (Table~\ref{tab:baselines}).
14	Min-K\% Prob \cite{shi2024_minkprob} (33.2\%) outperforms DetectGPT \cite{mitchell2023_detectgpt} (30.7\%), but CORAL ordinal calibration does not close the gap (d1--d3: 40.4\% vs.\ RF 71.6\%), confirming the bottleneck is input signal, not calibration (Appendix~\ref{app:detector_baselines}).
15	Adding Min-K\% as a 20th RF feature yields only +0.48\,pp (78.4\%$\to$78.9\%); the 19 statistical features already capture the dominant ordinal signal.
16	
17	\paragraph{Surface-text ablation.}
18	Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (DeepSeek V3.2, 36.2\%; Qwen2.5-7B-Instruct, 30.4\%) also fail (43\,pp below the best RF cell; Appendix~\ref{app:zeroshot_prompt}); depth signal resides in distributional statistics inaccessible from surface text.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\caption{Ordinal depth estimation: method comparison (mean across 9 atlas cells; DetectGPT: 8 of 9, Pythia nucleus excluded due to scoring instability). Chance = 25\% (4-class) / 33.3\% (d1--d3). Min-K\%: $K{=}20$, CORAL calibration. D
…[truncated 5079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-19T06:34:47.669764+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-19T06:34:48.124225+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	This paper formalizes recursive generation depth estimation as ordinal classification under controlled full-replacement chains.
5	The perplexity tail feature family dominates depth discrimination across all nine cells, with $\mathrm{EDD}_{0.70}{=}4$ for all three families (confirmed by 5-class extension, 71--80\%; Appendix~\ref{app:depth4_ext}); cross-model transfer reaches 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, while binary detectors and membership inference methods achieve only 30--35\%.
6	
7	\paragraph{Accumulation settings.}
8	Our benchmark uses full-replacement chains; in practice, model training involves accumulation, mixing human data with synthetic outputs at unknown proportions \cite{gerstgrasser2024_accumulate}.
9	Under accumulation, depth signal should attenuate because each generation retains human-originated distributional properties, slowing tail erosion.
10	The 66.4\% cross-model and 59.1\% cross-strategy transfer should be interpreted as ceiling estimates for the mixed-data regime.
11	Extending the framework to accumulation, where depth becomes a continuous mixing parameter, is a priority for future work.
12	
13	\paragraph{Scale and deployment implications.}
14	The depth signal attenuates with model scale: at 14B, d0/d1 separability drops sharply ($\mathrm{EDD}_{0.70}{=}0$), though d1--d3 discrimination persists above chance.
15	This suggests that depth estimation complements rather than replaces binary detection for practical data auditing: binary detectors handle the human-vs-machine boundary where depth estimation is redundant ($>$97\% d0 recall), while depth estimation provides the finer ordinal resolution that binary methods cannot.
16	A practical deployment path proceeds from controlled settings, where model and strategy are known, to partially known settings via strategy-identification routing, to fully unknown settings requiring strategy-invariant features (Appen
…[truncated 365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-19T06:34:48.175063+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-19T06:34:48.477126+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	All experiments use full-replacement recursive chains, where each depth fully replaces the prior training corpus. Real-world contamination typically involves accumulation, where synthetic and human data co-exist at unknown proportions across iterations \cite{gerstgrasser2024_accumulate}. Under accumulation, depth signal should attenuate because each generation retains human-originated distributional properties. Our results therefore represent an upper bound on feature separability; extending the framework to accumulation settings, where depth becomes a continuous mixing parameter, is a priority for future work.
6	Segment-level estimation in mixed-depth documents remains open (Appendix~\ref{app:mixed_depth}), as our framework assumes uniform depth per passage.
7	
8	\paragraph{Controlled experimental setting.}
9	The primary benchmark uses Wikipedia seed text with controlled LoRA fine-tuning (1--1.5B models), a design that isolates the depth variable but diverges from wild contamination.
10	Domain bias controls confirm depth as the dominant factor: LOGO accuracy (72.1\%) matches standard CV (72.0\%), seed-group prediction is at chance (10.2\%; Appendix~\ref{app:domain_bias}).
11	Cross-scale experiments (7--14B, \S\ref{sec:gen:crossscale}) show signal that attenuates with scale; at 14B, d0/d1 separability nearly vanishes ($\mathrm{EDD}_{0.70}{=}0$) while d1--d3 discrimination persists; this constitutes a boundary condition for the current feature set (confounded by five factors; Appendix~\ref{app:cross_scale_confounds}).
12	
13	\paragraph{Cross-strategy deployment constraint.}
14	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
15	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random 
…[truncated 6195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-19T06:34:48.527775+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-19T06:34:48.782074+00:00_

1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
43	Concretely, the d0$\t
…[truncated 57037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 254
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-19T06:34:54.354426+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,TodoWrite",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,TodoWrite",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-19T06:34:54.455213+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-19T06:35:01.735736+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 ARR/EMNLP 2026 reviewer guidelines 和 review form', 'status': 'in_progress', 'activeForm': '搜索 ARR reviewer guidelines'}, {'content': '通读论文全文并记录关键发现', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '按官方维度逐项打分', 'status': 'pending', 'activeForm': '按官方维度逐项打分'}, {'content': '撰写完整审稿意见', 'status': 'pending', 'activeForm': '撰写完整审稿意见'}, {'content': '通过 review_reviewer_post_to_director 提交审稿意见', 'status': 'pending', 'activeForm': '提交审稿意见给 Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 ARR/EMNLP 2026 reviewer guidelines 和 review form', 'status': 'in_progress', 'activeForm': '搜索 ARR reviewer guidelines'}, {'content': '通读论文全文并记录关键发现', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '按官方维度逐项打分', 'status': 'pending', 'activeForm': '按官方维度逐项打分'}, {'content': '撰写完整审稿意见', 'status': 'pending', 'activeForm': '撰写完整审稿意见'}, {'content': '通过 review_reviewer_post_to_director 提交审稿意见', 'status': 'pending', 'activeForm': '提交审稿意见给 Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-19T06:35:01.736335+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-19T06:35:04.945571+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"
  }
}
```

</details>

---


### Tool call

_source line 645 · 2026-05-19T06:35:05.850039+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form soundness excitement reproducibility 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form soundness excitement reproducibility 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-19T06:35:06.303224+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-19T06:35:06.353844+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 648 · 2026-05-19T06:35:12.779985+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Author reviewing exemptions from July 2025 cycle – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/exemptions2025"},{"title":"Main Conference - ACL 2025","url":"https://2025.aclweb.org/calls/main_conference_papers/"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the web search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Key Reviewer Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

## Important Policies for 2025-2026

- **Highly Irresponsible Reviewers**: Starting in May 2025, ARR adopts a new policy on the 'highly irresponsi
…[truncated 895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7834
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-19T06:35:13.382626+00:00_

Web search results for query: "ACL Rolling Review reviewer form soundness excitement reproducibility 2025 2026"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, here's what I found about the ACL Rolling Review (ARR) reviewer form and the scoring criteria:

## Reviewer Form Updates (2025-2026)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
So
…[truncated 1071 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7532
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-19T06:35:17.098561+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-19T06:35:17.199632+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-19T06:35:22.069488+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract ALL scoring dimensions, their exact scales (1-5, 1-6, etc.), and the description of each score level. I need the complete review form criteria including: soundness, excitement, overall assessment, reproducibility, confidence, and any other dimensions. Give me the EXACT text for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract ALL scoring dimensions, their exact scales (1-5, 1-6, etc.), and the description of each score level. I need the complete review form criteria including: soundness, excitement, overall assessment, reproducibility, confidence, and any other dimensions. Give me the EXACT text for each score level."
  }
}
```

</details>

---


### Tool call

_source line 653 · 2026-05-19T06:35:23.426074+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines. I need: what reviewers should focus on, what constitutes a good review, scoring criteria details, and any specific instructions about soundness, excitement, novelty, reproducibility, and overall assessment. Give me the full text of the guidelines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines. I need: what reviewers should focus on, what constitutes a good review, scoring criteria details, and any specific instructions about soundness, excitement, novelty, reproducibility, and overall assessment. Give me the full text of the guidelines."
  }
}
```

</details>

---


### Tool result

_source line 654 · 2026-05-19T06:35:31.557627+00:00_

# ACL Rolling Review Form Scoring Dimensions

## 1. Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings."
- **3**: "Pretty sure, but there's a chance I missed something. Although I have a good feel for this area in general, I did not carefully check the paper's details."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details, didn't understand some central points."
- **1**: "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## 2. Soundness (1-5 scale with half-points)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement (1-5 scale with half-points)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points to others and/or attend if there's time."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. Overall Assessment (1-5 scale with half-points)
- **5**: "Consider for Award: paper could be considered for outstanding paper award (top 2.5%)."
- **4**: "Conference: paper could be accepted to an *ACL conference."
- **3**: "Fi
…[truncated 1888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9488
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-19T06:35:34.056031+00:00_

# ACL Rolling Review - Reviewer Guidelines Summary

## Core Focus Areas for Reviewers

Reviewers should concentrate on four main tasks:

1. **Time allocation** - Block calendar time for reading, reviewing, and participating in author discussions
2. **Assignment verification** - Confirm expertise match, check for conflicts of interest, and assess anonymity concerns
3. **Quality review writing** - Produce detailed, constructive feedback
4. **Post-response engagement** - Update assessments based on author responses and peer discussion

## What Constitutes a Good Review

Strong reviews demonstrate these characteristics:

- **Specificity**: Provide concrete examples rather than vague criticism. State "Paper misses references X, Y, Z" instead of "Missing relevant references"
- **Professionalism**: Maintain neutral, kind tone that respects authors' efforts and circumstances
- **Justified scoring**: Ensure review text substantiates all numerical scores
- **Balanced perspective**: Read papers twice (skim then in-depth) to avoid knee-jerk reactions

## Scoring Criteria (Three Scores Required)

**Soundness**: Technical validity and rigor
- Must be justified by review text
- Low scores require identified major faults
- Assess reproducibility separately when applicable

**Excitement**: Personal intellectual interest
- Orthogonal to soundness assessment
- Reflects subjective preferences, not objective merit
- Need not require explicit justification

**Overall Assessment**: Recommendation for acceptance
- Composite judgment combining soundness, excitement, novelty, and impact
- Main conference papers must be sound even if personally unexciting
- Findings papers have same soundness requirements as main track

## Critical Review Issues to Avoid

The guidelines identify 17 common problematic review patterns (H1-H17), including:

- Dismissing results as "unsurprising" despite lacking prior empirical validation
- Demanding state-of-the-art results when not claimed by authors
- Penalizi
…[truncated 1146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 10629
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-19T06:36:55.144082+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 ARR/EMNLP 2026 reviewer guidelines 和 review form', 'status': 'completed', 'activeForm': '搜索 ARR reviewer guidelines'}, {'content': '通读论文全文并记录关键发现', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '按官方维度逐项打分', 'status': 'completed', 'activeForm': '按官方维度逐项打分'}, {'content': '撰写完整审稿意见', 'status': 'in_progress', 'activeForm': '撰写完整审稿意见'}, {'content': '通过 review_reviewer_post_to_director 提交审稿意见', 'status': 'pending', 'activeForm': '提交审稿意见给 Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 ARR/EMNLP 2026 reviewer guidelines 和 review form', 'status': 'completed', 'activeForm': '搜索 ARR reviewer guidelines'}, {'content': '通读论文全文并记录关键发现', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '按官方维度逐项打分', 'status': 'completed', 'activeForm': '按官方维度逐项打分'}, {'content': '撰写完整审稿意见', 'status': 'in_progress', 'activeForm': '撰写完整审稿意见'}, {'content': '通过 review_reviewer_post_to_director 提交审稿意见', 'status': 'pending', 'activeForm': '提交审稿意见给 Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-19T06:36:55.144551+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-19T06:37:00.970222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": "354",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "offset": "354",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-19T06:37:01.022468+00:00_

354	\subsection{Reference Model Ablation}
355	\label{app:ref_ablation}
356	
357	\begin{table}[h]
358	\centering
359	\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}
360	\label{tab:ref_ablation}
361	\resizebox{\columnwidth}{!}{%
362	\begin{tabular}{@{}lcc@{}}
363	\toprule
364	Reference Model & Architecture & Accuracy (\%) \\
365	\midrule
366	Pythia-1.4B (self) & GPT-NeoX & 78.6 $\pm$ 0.6 \\
367	OLMo-1B (cross) & OLMo & 74.5 $\pm$ 0.7 \\
368	GPT-2~XL (cross) & GPT-2 & 67.3 $\pm$ 0.7 \\
369	\bottomrule
370	\end{tabular}}
371	\end{table}
372	
373	\subsection{Cross-Scale Full Results}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-19T06:37:15.171093+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 ARR/EMNLP 2026 reviewer guidelines 和 review form', 'status': 'completed', 'activeForm': '搜索 ARR reviewer guidelines'}, {'content': '通读论文全文并记录关键发现', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '按官方维度逐项打分', 'status': 'completed', 'activeForm': '按官方维度逐项打分'}, {'content': '撰写完整审稿意见', 'status': 'in_progress', 'activeForm': '撰写完整审稿意见'}, {'content': '通过 review_reviewer_post_to_director 提交审稿意见', 'status': 'pending', 'activeForm': '提交审稿意见给 Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 ARR/EMNLP 2026 reviewer guidelines 和 review form', 'status': 'completed', 'activeForm': '搜索 ARR reviewer guidelines'}, {'content': '通读论文全文并记录关键发现', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '按官方维度逐项打分', 'status': 'completed', 'activeForm': '按官方维度逐项打分'}, {'content': '撰写完整审稿意见', 'status': 'in_progress', 'activeForm': '撰写完整审稿意见'}, {'content': '通过 review_reviewer_post_to_director 提交审稿意见', 'status': 'pending', 'activeForm': '提交审稿意见给 Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-19T06:37:15.171621+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-19T06:37:21.448903+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 ARR/EMNLP 2026 reviewer guidelines 和 review form', 'status': 'completed', 'activeForm': '搜索 ARR reviewer guidelines'}, {'content': '通读论文全文并记录关键发现', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '按官方维度逐项打分', 'status': 'completed', 'activeForm': '按官方维度逐项打分'}, {'content': '撰写完整审稿意见', 'status': 'completed', 'activeForm': '撰写完整审稿意见'}, {'content': '通过 review_reviewer_post_to_director 提交审稿意见', 'status': 'in_progress', 'activeForm': '提交审稿意见给 Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 ARR/EMNLP 2026 reviewer guidelines 和 review form', 'status': 'completed', 'activeForm': '搜索 ARR reviewer guidelines'}, {'content': '通读论文全文并记录关键发现', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '按官方维度逐项打分', 'status': 'completed', 'activeForm': '按官方维度逐项打分'}, {'content': '撰写完整审稿意见', 'status': 'completed', 'activeForm': '撰写完整审稿意见'}, {'content': '通过 review_reviewer_post_to_director 提交审稿意见', 'status': 'in_progress', 'activeForm': '提交审稿意见给 Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-19T06:37:21.449412+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-19T06:40:02.300234+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见\n\n### Summary\n\n本文将递归生成深度估计（recursive generation depth estimation）形式化为序数分类任务，构建了一个 180K 样本的基准测试集（3 个模型族 × 3 种解码策略 × 4 个深度等级），并使用基于 19 个统计特征的 Random Forest 进行分类。论文提出了 Effective Discriminable Depth（EDD）指标来量化相邻深度的可区分性极限，并在多个泛化轴（跨模型、跨策略、跨域、跨尺度）上进行了系统实验。核心发现是困惑度尾部特征族（p90_ppl、var_surprisal）在所有 9 个 cell 中主导深度判别。\n\n---\n\n### Strengths\n\n**S1: 任务形式化填补了真实空白。** 在二元检测（human vs. machine）和模型坍塌理论（假定深度已知）之间，序数深度估计是一个未被研究的新维度。EDD 指标提供了一个有操作意义的量化手段来衡量递归链上的可区分极限。这一贡献在概念层面是扎实的。\n\n**S2: 基准设计系统且全面。** 3×3 grid（模型族 × 解码策略）覆盖了合理的变异来源，180K 样本规模充足。每个 cell 独立评估，避免了将异质信号混为一体。Depth extension 到 d5 的设计也合理。\n\n**S3: 控制实验设计良好。** Domain bias analysis（§App F）中的 LOGO 评估和 seed-group negative control 是方法论亮点——LOGO accuracy（72.1%）与标准 CV（72.0%）匹配，seed-group 预测在 chance level（10.2%），有效排除了 topic leakage。修正 bug 后如实报告修正前后的数据（64.0% → 72.1%），体现了研究诚信。\n\n**S4: 分类器收敛验证了特征为核心。** RF、XGBoost、LightGBM 在 0.4pp 内收敛（§5.1），加上 CORAL/DivEye 在 0.6pp 内匹配（p>0.05），有力地论证了分类信号来自特征设计而非分类器架构。\n\n**S5: Limitations 章节异常诚实。** 论文主动讨论了 full-replacement vs. accumulation、d0 inflation、cross-strategy boundary inversion、reference model dependency、single LoRA instance、adversarial robustness 等。这种透明度在提交稿中并不常见。\n\n**S6: 跨模型递归链实验（App J）是有价值的补充。** 异构链（Pythia→OLMo→GPT-2 XL）达到 84.75%，反向链（GPT-2 XL→OLMo→Pythia）达到 85.75%，有效排除了架构指纹假说。\n\n---\n\n### Weaknesses\n\n**W1 [Must-Fix]: Reference model circularity claim 与消融数据自相矛盾。**\n- 具体位置：§3.4（\"confers no systematic advantage\"）vs. Table 8 / Appendix H\n- 问题：§3.4 声称 Pythia-1.4B 同时作为 generator 和 reference model \"不带来系统性优势\"，论据是 Pythia 数据（78.7%）低于 GPT-2 XL 数据（85.9%）。但这是**跨 generator 的混淆比较**——GPT-2 XL 数据准确率更高可能是因为 GPT-2 XL 产生了更强的深度信号，而非 self-reference 不帮助 Pythia。Appendix H（Table 8）的**公平消融**显示：在 Pythia 生成的数据上，self-reference（78.6%）> OLMo 参考（74.5%）> GPT-2 XL 参考（67.3%），self-reference 带来 4.1-11.3pp 的优势。Limitations 中也承认 \"same-family references yield optimal performance\"。\n- 影响：这意味着 Pythia cell 的 78.7% 准确率可能部分来自 self-reference 的系统性优势，而非纯粹的深度信号。OLMo 和 GPT-2 XL cell 使用的是 cross-reference（Pythia-1.4B），其准确率反而可能被低估。这使得 9 个 cell 之间的横向比较不公平。\n- 建议：(1) 修正 §3.4 的 claim，承认 self-reference 带来可测量的优势；(2) 在 Table 2 的 Pythia 行旁注明 self-reference；(3) 讨论使用统一 cross-reference 时所有 cell 准确率的预期变化。\n\n**W2 [Must-Fix]: 跨尺度实验的 5 个混淆因素使其结论不可靠。**\n- 具体位置：§5.4, Appendix I\n- 问题：7-14B 实验引入了 5 个混淆因素（QLoRA 4-bit 量化 / 样本量 500 vs 5000 / 仅 nucleus 策略 / 词表不匹配 / 14B 使用 self-reference），且论文承认\"infeasible to attribute the observed accuracy gap to any single factor\"。在这种条件下：\n  - 仅 2 个 7-8B 模型（Llama-3.1-8B 和 Qwen2.5-7B）给出了方向相反的 AUC 轨迹（单调 vs U 型），无法判断哪种是主流模式\n  - 14B 的 EDD=0 可能完全是 self-reference + quantization 的产物，而非真正的 scale effect\n  - 500 samples/depth 的 CI 宽度为 ±2pp（Table 9），Cross-scale 的准确率差异（54-70%）可能部分在噪声范围内\n- 主文 §5.4 使用 \"existence proof\" 是恰当的，但 abstract 中 \"Preliminary cross-scale experiments (7-14B, 54-70%) provide an existence proof that depth signal persists at larger scales\" 的表述过于乐观——\"persists\" 对 14B（EDD=0, d0v1 AUC=0.643）来说言过其实\n- 建议：(1) 在 abstract 中将 14B 的结果明确标记为 boundary condition 而非 \"persists\"；(2) 讨论 QLoRA quantization 对 perplexity distribution 的独立影响——是否有消融可以分离量化效应？(3) 增加至少一个不使用量化的 7-8B 实验作为 control\n\n**W3 [Must-Fix]: d0 recall >97% 系统性膨胀 headline metrics，且 d1-d3 balanced accuracy 未被充分前置。**\n- 具体位置：Abstract, Table 2, §4.1, §5.1-5.3\n- 问题：Abstract 首句报告 \"69-86% four-class accuracy\"，括号内的 \"d1-d3 balanced: 59-82%\" 是补充说明。但 d0 recall >97% 本质上是二元检测的成功（已被 Binoculars 等工具解决），不是本文的核心贡献。核心贡献是区分 d1/d2/d3——而 d1-d3 balanced accuracy 在跨模型迁移中仅 55.4%（chance=33%），跨策略迁移中仅 45.9%。\n  - Cross-model transfer: 66.4% headline → 55.4% d1-d3（下降 11pp）\n  - Cross-strategy transfer: 59.1% headline → 45.9% d1-d3（下降 13.2pp）\n  - 更极端的是 Pythia holdout 的 d2 recall 仅 26.8%（Table 4）\n- 论文在 Limitations 中承认了 d0 inflation，但 abstract 和 contribution 列表中仍以四类准确率为主导叙事\n- 建议：(1) Abstract 和 Contribution 列表中应以 d1-d3 balanced accuracy 为主指标，四类准确率作为补充；(2) Table 2 增加一列专门报告 d1-d3 balanced accuracy 的 CI；(3) 明确讨论：在 d2 recall=26.8% 的 worst case 下，深度估计的实际部署意义\n\n**W4 [Should-Fix]: Curation PoC（Appendix K）的主要比较不显著，多重比较未充分校正。**\n- 具体位置：Table 13, Table 14, Appendix K, Extended Discussion（Appendix N）\n- 问题：\n  - 核心比较（RF-filtered vs unfiltered）：p=0.407（rf_soft）、p=0.492（rf_moderate）、p=0.607（rf_strict），全部不显著\n  - RF vs random 的 3 个 pairwise 比较（p=0.002, 0.020, <0.001）未进行 Bonferroni 校正；Appendix N 声称 \"2 of 3 comparisons surviving\" Bonferroni（α=0.05/3=0.017），但 rf_moderate vs random_moderate 的 p=0.020 不通过\n  - 效应量微小：rf_soft vs unfiltered 的 Δ=+0.043 PPL（<0.3% relative）\n  - 仅 5 seeds，power 极低\n- 论文诚实地报告了 p 值并承认 \"inconclusive\"，但 Appendix N 的 framing（\"2 of 3 surviving Bonferroni\"）给读者留下了部分显著的印象\n- 建议：(1) 统一使用 Bonferroni-corrected p 值，明确标注 rf_moderate vs random_moderate 不通过；(2) 在 Discussion 中将 curation 描述为 \"negative result\" 而非 \"inconclusive preliminary evidence\"；(3) 删除或大幅缩减 curation PoC 篇幅，避免读者产生误导性的实用价值预期\n\n**W5 [Should-Fix]: VIF>10 for 14-16/19 features 下的 feature importance 解释过度。**\n- 具体位置：§4.2, Table 3, footnote 3\n- 问题：当 VIF>10 时，Gini importance 在高共线性特征间分配不稳定。论文的脚注承认 \"individual rankings should be interpreted cautiously given high multicollinearity\"，但紧接着在 Table 3 中详细报告了每个 cell 的逐个特征排名和精确 importance 值（如 .17、.15、.11）。§4.2 声称 \"p90_ppl ranks top-2 by Gini importance in all 9 cells\" 和 \"var_surprisal in 8/9 under SHAP\"——在 effective dimensionality 仅 4-5 的情况下，这些个体排名的稳定性存疑。\n- group-level dominance 的 claim（perplexity tail family 主导）有 Kendall's W=0.90 支持，是可靠的\n- 但 Table 3 的呈现方式暗示了比数据支持的更高的特征级别精度\n- 建议：(1) 明确区分 group-level claim（可靠）和 individual feature claim（不可靠）；(2) 报告 bootstrap stability 的特征排名（重采样 1000 次后 p90_ppl 排名 top-2 的概率）；(3) 考虑使用 PCA 或 elastic net 来处理共线性后再解释 importance\n\n**W6 [Should-Fix]: EDD 定义的 contiguous prefix 要求在非单调场景下过于保守，且无替代方案。**\n- 具体位置：Definition 1（§3.5），Limitations\n- 问题：EDD 要求从 (0,1) 到 (d*,d*+1) 的所有 pairwise AUC 都超过阈值 T。当 AUC profile 非单调时（如 Qwen2.5-7B 的 U 型，Limitations 中提到的 cross-strategy inversion 导致 d1v2 AUC 低至 0.129），EDD 会大幅低估真实的可区分范围。\n- 对 1-1.5B 基模型，AUC 严格单调递减，EDD 表现良好。但论文将 EDD 作为通用指标推广，在 7B+ 和 cross-strategy 场景下它的保守性成为系统性偏差\n- 论文在 Limitations 中承认了这一点（\"extending EDD to handle non-contiguous discriminable regions is future work\"），但没有提供任何替代定义或敏感性分析\n- 建议：(1) 提供一个补充指标（如 \"Maximum Discriminable Depth\" = max{d : AUC(d,d+1) ≥ T}）来覆盖非单调场景；(2) 在 §3.5 中明确 EDD 的适用条件（monotonic AUC decay）而非仅在脚注中提及\n\n**W7 [Should-Fix]: Cross-seed replication 覆盖不足（3/9 cells），且方向一致的 seed=43 优势未被解释。**\n- 具体位置：Appendix M, Limitations\n- 问题：\n  - 仅 3 个 cell（Pythia/OLMo/GPT-2 XL nucleus）有 cross-seed replication；其余 6 个 cell（所有 temperature 和 top-k 配置）均为 single-seed\n  - seed=43 在所有 3 个 cell 中均优于 seed=42（+0.14 到 +3.17pp），且 2/3 差异统计显著（CI 不重叠）。方向一致的偏差暗示 seed=42 可能系统性偏低，而非 seed=43 偏高\n  - single-seed 不确定性为 ~1-3pp，这意味着 Table 2 中跨 cell 的许多差异（如 Pythia nucleus 78.7% vs OLMo nucleus 78.9% 仅差 0.2pp）可能完全在 seed noise 范围内\n- 建议：(1) 至少对 3 个 temperature cells 补充 seed=43 replication；(2) 讨论 seed=43 系统性偏高的可能原因；(3) 在 Table 2 的 caption 中注明 single-seed uncertainty ~1-3pp\n\n**W8 [Should-Fix]: Full-replacement scope 声明在 Introduction/Abstract 中不够前置。**\n- 具体位置：Abstract（第 2 句）、Introduction §1 段 2\n- 问题：Abstract 第 2 句提到 \"controlled full-replacement recursive chains\"，但对不熟悉模型坍塌文献的读者来说，\"full-replacement\" 的含义及其对实际场景的限制不明显。Introduction 在第 2 段才解释这一点，并指出 \"real-world contamination typically involves partial mixing (accumulation)\"。\n- 论文在 Discussion 中声称 cross-model/cross-strategy transfer 应被视为 \"ceiling estimates for the mixed-data regime\"，但这一 claim 未经任何实验验证——accumulation 设置下的特征行为可能完全不同（不仅仅是 \"attenuated\"）\n- \"upper bound on depth signal strength\" 的论证是直觉性的（full-replacement 最大化深度信号），但缺乏理论或实验支持\n- 建议：(1) 在 Abstract 中明确说明这是 full-replacement 的 upper bound 结果；(2) 至少做一个 toy-scale accumulation 实验来验证 \"upper bound\" 假设\n\n**W9 [Minor]: 单一 LoRA 超参数配置。**\n- 具体位置：§3.2, Table 5\n- 所有 9 个 cell 使用完全相同的 LoRA 配置（r=16, α=32, lr=2e-4, 3 epochs）。不同的 LoRA rank 或学习率可能改变递归链的衰退速度，从而影响深度信号强度。缺少对 rank r（如 r=4, 8, 32）或 learning rate 的敏感性分析。\n\n**W10 [Minor]: Prompted generation 验证仅覆盖 1/9 cell。**\n- 具体位置：§5.3, Appendix O\n- 仅 GPT-2 XL nucleus 一个 cell 验证了 prompted generation（69.5%，-13.8pp）。13.8pp 的下降幅度不小；在 top-k 或 temperature 配置下（本已准确率较低），prompted generation 可能将准确率推向 chance level。\n\n---\n\n### Questions\n\n**Q1:** Table 8（Appendix H）显示 self-reference 在 Pythia 数据上提供 4.1-11.3pp 优势。§3.4 如何将此与 \"no systematic advantage\" 的 claim 调和？\n\n**Q2:** Curation PoC 中 rf_moderate vs random_moderate 的 p=0.020 在 Bonferroni 校正（α=0.017）下不通过，但 Appendix N 声称 \"2 of 3 comparisons surviving\"。请澄清具体哪两个通过了？\n\n**Q3:** 论文声称 full-replacement 结果是 accumulation 设置的 \"upper bound\"。是否有任何实验或理论依据支持这一单调性假设？是否存在 accumulation 反而增强某些深度信号的可能？\n\n**Q4:** seed=43 在所有 3 个 cell 中系统性优于 seed=42。是否检查了 seed=42 的 LoRA 训练是否有异常（如训练不收敛、outlier 比例异常）？Appendix M 提到 seed=42 下 d3 outlier 比例为 0.56%，seed=43 为 12.8%——但 seed=43 反而准确率更高，这似乎矛盾。\n\n**Q5:** 对于 cross-strategy transfer 中 d1/d2 boundary inversion（d1v2 AUC < 0.5），两阶段 pipeline 仅恢复了 11.5pp。在策略未知的实际部署中（d1-d3: 45.9%），这一准确率是否足以支持 \"data auditing\" 的实用 claim？\n\n---\n\n### Missing References\n\n未发现重大遗漏。Related Work 覆盖了 model collapse theory、AI text detection、membership inference、ordinal classification 和 decoding strategy effects 的主要工作。建议补充：\n- 关于 synthetic data contamination in the wild 的实证研究（如果有 2025-2026 的新工作）\n- 关于 LoRA 微调与模型坍塌交互的工作（如果存在）\n\n---\n\n### 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 1-1.5B full-replacement 范围内的实验设计扎实（LOGO control、多 baseline、多泛化轴），但 reference model circularity claim 与消融数据矛盾（W1），cross-scale 结论受 5 个混淆因素限制（W2），curation PoC 主比较不显著且多重比较校正有误（W4）。Feature importance 在高共线性下的解释超出了数据支持的范围（W5）。 |\n| **Excitement** | 3.5/5 | 任务形式化是真正的新贡献，EDD 指标有操作价值。但 full-replacement 限制降低了生态效度；cross-strategy barrier（d1-d3: 45.9%）和 scale attenuation（14B EDD=0）使得从实验室到部署的路径不清晰。 |\n| **Reproducibility** | 3/5 | LoRA 超参（Table 5）、RF 配置、软件版本和硬件均已报告。但：(1) 代码/数据 \"upon acceptance\" 未提供匿名链接；(2) Wikipedia subset 的选择方法未说明；(3) 仅 3/9 cells 有 cross-seed replication。 |\n| **Confidence** | 4/5 | 我仔细阅读了论文全文和附录，熟悉 model collapse 和 AI text detection 文献。不太确定的点是 accumulation 设置下的理论预期。 |\n\n### Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n**一句话总结：** 任务形式化有价值且实验系统全面，但 reference model circularity 的误导性 claim、cross-scale 结论的不可靠性、以及 d0 inflation 对核心 d1-d3 性能的掩盖，使论文在方法严谨性上存在需要修复的问题。\n\n本文的核心贡献——将递归生成深度估计形式化为序数分类并构建系统性基准——是有意义的。在 1-1.5B full-replacement 范围内的实验设计是审慎的，控制实验（LOGO、negative control、reverse chain）是亮点。但论文在几个关键点上的 claim 强度超过了数据支持：(1) reference model \"no systematic advantage\" 与 Table 8 矛盾；(2) cross-scale \"depth signal persists\" 对 14B（EDD=0）不成立；(3) d1-d3 balanced accuracy（核心指标）在跨模型/跨策略迁移中仅 55.4%/45.9%，显著低于 headline 四类准确率。修复 W1-W3 后，论文有望达到 Conference 水准。\n\n---\n\n### Detailed Comments（按 Section）\n\n**Abstract:** \"69-86% four-class accuracy\" 应明确标注包含 d0 inflation。建议改为以 d1-d3 balanced accuracy 为主指标。\"depth signal persists at larger scales\" 对 14B（EDD=0）不准确。\n\n**§1 Introduction:** 第 2 段对 full-replacement scope 的说明是必要的，但应更前置（移到第 1 段末尾或与任务定义一起出现）。Contribution 列表中的 \"EDD_{0.70}=4 for all three families\" 需注明这是 1-1.5B 的结果。\n\n**§3.4 Reference model:** \"confers no systematic advantage\" 需要修正为 \"confers a measurable advantage on same-family data (4-11pp; Appendix H) but does not drive the cross-generator accuracy ranking\"。当前表述具有误导性。\n\n**§3.5 EDD:** Definition 1 的适用条件（monotonic AUC decay）应在定义而非脚注中明确。当前脚注提到 Qwen2.5-7B 的非单调性，但读者在阅读 Definition 1 时不一定注意到这个限制。\n\n**§4.1 In-Distribution Performance:** Table 2 的 caption 已提到 \"Depth-0 recall exceeds 97%\"，但建议增加 d1-d3 balanced accuracy 列以便读者直接比较。\n\n**§4.2 Feature Consistency:** 建议将 footnote 3（multicollinearity caveat）提升为正文段落，并在 Table 3 的 caption 中明确注明 \"individual feature rankings are unstable under VIF>10; group-level dominance is robust\"。\n\n**§5.1 Classifier Comparison:** \"within 0.4pp\" 的收敛 claim 是否经过等价性检验（如 TOST）？如果仅是 observed difference，应说明 \"observed difference ≤ 0.4pp\" 而非暗示统计等价。\n\n**§5.4 Cross-Scale:** 建议将 \"existence proof\" 的 claim 限制为 7-8B（signal above chance），14B 明确标记为 boundary condition。当前表述 \"depth signal persists at larger scales\" 对 14B 不成立。\n\n**Appendix K Curation PoC:** 建议大幅压缩或移至补充材料的 \"inconclusive results\" 部分。当前篇幅和位置可能给读者造成 \"curation 有效\" 的印象。\n\n**Limitations:** 质量很高，建议将 reference model circularity 的更诚实表述（self-reference 4-11pp advantage）从 Limitations 提前到 §3.4 正文。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见\n\n### Summary\n\n本文将递归生成深度估计（recursive generation depth estimation）形式化为序数分类任务，构建了一个 180K 样本的基准测试集（3 个模型族 × 3 种解码策略 × 4 个深度等级），并使用基于 19 个统计特征的 Random Forest 进行分类。论文提出了 Effective Discriminable Depth（EDD）指标来量化相邻深度的可区分性极限，并在多个泛化轴（跨模型、跨策略、跨域、跨尺度）上进行了系统实验。核心发现是困惑度尾部特征族（p90_ppl、var_surprisal）在所有 9 个 cell 中主导深度判别。\n\n---\n\n### Strengths\n\n**S1: 任务形式化填补了真实空白。** 在二元检测（human vs. machine）和模型坍塌理论（假定深度已知）之间，序数深度估计是一个未被研究的新维度。EDD 指标提供了一个有操作意义的量化手段来衡量递归链上的可区分极限。这一贡献在概念层面是扎实的。\n\n**S2: 基准设计系统且全面。** 3×3 grid（模型族 × 解码策略）覆盖了合理的变异来源，180K 样本规模充足。每个 cell 独立评估，避免了将异质信号混为一体。Depth extension 到 d5 的设计也合理。\n\n**S3: 控制实验设计良好。** Domain bias analysis（§App F）中的 LOGO 评估和 seed-group negative control 是方法论亮点——LOGO accuracy（72.1%）与标准 CV（72.0%）匹配，seed-group 预测在 chance level（10.2%），有效排除了 topic leakage。修正 bug 后如实报告修正前后的数据（64.0% → 72.1%），体现了研究诚信。\n\n**S4: 分类器收敛验证了特征为核心。** RF、XGBoost、LightGBM 在 0.4pp 内收敛（§5.1），加上 CORAL/DivEye 在 0.6pp 内匹配（p>0.05），有力地论证了分类信号来自特征设计而非分类器架构。\n\n**S5: Limitations 章节异常诚实。** 论文主动讨论了 full-replacement vs. accumulation、d0 inflation、cross-strategy boundary inversion、reference model dependency、single LoRA instance、adversarial robustness 等。这种透明度在提交稿中并不常见。\n\n**S6: 跨模型递归链实验（App J）是有价值的补充。** 异构链（Pythia→OLMo→GPT-2 XL）达到 84.75%，反向链（GPT-2 XL→OLMo→Pythia）达到 85.75%，有效排除了架构指纹假说。\n\n---\n\n### Weaknesses\n\n**W1 [Must-Fix]: Reference model circularity claim 与消融数据自相矛盾。**\n- 具体位置：§3.4（\"confers no systematic advantage\"）vs. Table 8 / Appendix H\n- 问题：§3.4 声称 Pythia-1.4B 同时作为 generator 和 reference model \"不带来系统性优势\"，论据是 Pythia 数据（78.7%）低于 GPT-2 XL 数据（85.9%）。但这是**跨 generator 的混淆比较**——GPT-2 XL 数据准确率更高可能是因为 GPT-2 XL 产生了更强的深度信号，而非 self-reference 不帮助 Pythia。Appendix H（Table 8）的**公平消融**显示：在 Pythia 生成的数据上，self-reference（78.6%）> OLMo 参考（74.5%）> GPT-2 XL 参考（67.3%），self-reference 带来 4.1-11.3pp 的优势。Limitations 中也承认 \"same-family references yield optimal performance\"。\n- 影响：这意味着 Pythia cell 的 78.7% 准确率可能部分来自 self-reference 的系统性优势，而非纯粹的深度信号。OLMo 和 GPT-2 XL cell 使用的是 cross-reference（Pythia-1.4B），其准确率反而可能被低估。这使得 9 个 cell 之间的横向比较不公平。\n- 建议：(1) 修正 §3.4 的 claim，承认 self-reference 带来可测量的优势；(2) 在 Table 2 的 Pythia 行旁注明 self-reference；(3) 讨论使用统一 cross-reference 时所有 cell 准确率的预期变化。\n\n**W2 [Must-Fix]: 跨尺度实验的 5 个混淆因素使其结论不可靠。**\n- 具体位置：§5.4, Appendix I\n- 问题：7-14B 实验引入了 5 个混淆因素（QLoRA 4-bit 量化 / 样本量 500 vs 5000 / 仅 nucleus 策略 / 词表不匹配 / 14B 使用 self-reference），且论文承认\"infeasible to attribute the observed accuracy gap to any single factor\"。在这种条件下：\n  - 仅 2 个 7-8B 模型（Llama-3.1-8B 和 Qwen2.5-7B）给出了方向相反的 AUC 轨迹（单调 vs U 型），无法判断哪种是主流模式\n  - 14B 的 EDD=0 可能完全是 self-reference + quantization 的产物，而非真正的 scale effect\n  - 500 samples/depth 的 CI 宽度为 ±2pp（Table 9），Cross-scale 的准确率差异（54-70%）可能部分在噪声范围内\n- 主文 §5.4 使用 \"existence proof\" 是恰当的，但 abstract 中 \"Preliminary cross-scale experiments (7-14B, 54-70%) provide an existence proof that depth signal persists at larger scales\" 的表述过于乐观——\"persists\" 对 14B（EDD=0, d0v1 AUC=0.643）来说言过其实\n- 建议：(1) 在 abstract 中将 14B 的结果明确标记为 boundary condition 而非 \"persists\"；(2) 讨论 QLoRA quantization 对 perplexity distribution 的独立影响——是否有消融可以分离量化效应？(3) 增加至少一个不使用量化的 7-8B 实验作为 control\n\n**W3 [Must-Fix]: d0 recall >97% 系统性膨胀 headline metrics，且 d1-d3 balanced accuracy 未被充分前置。**\n- 具体位置：Abstract, Table 2, §4.1, §5.1-5.3\n- 问题：Abstract 首句报告 \"69-86% four-class accuracy\"，括号内的 \"d1-d3 balanced: 59-82%\" 是补充说明。但 d0 recall >97% 本质上是二元检测的成功（已被 Binoculars 等工具解决），不是本文的核心贡献。核心贡献是区分 d1/d2/d3——而 d1-d3 balanced accuracy 在跨模型迁移中仅 55.4%（chance=33%），跨策略迁移中仅 45.9%。\n  - Cross-model transfer: 66.4% headline → 55.4% d1-d3（下降 11pp）\n  - Cross-strategy transfer: 59.1% headline → 45.9% d1-d3（下降 13.2pp）\n  - 更极端的是 Pythia holdout 的 d2 recall 仅 26.8%（Table 4）\n- 论文在 Limitations 中承认了 d0 inflation，但 abstract 和 contribution 列表中仍以四类准确率为主导叙事\n- 建议：(1) Abstract 和 Contribution 列表中应以 d1-d3 balanced accuracy 为主指标，四类准确率作为补充；(2) Table 2 增加一列专门报告 d1-d3 balanced accuracy 的 CI；(3) 明确讨论：在 d2 recall=26.8% 的 worst case 下，深度估计的实际部署意义\n\n**W4 [Should-Fix]: Curation PoC（Appendix K）的主要比较不显著，多重比较未充分校正。**\n- 具体位置：Table 13, Table 14, Appendix K, Extended Discussion（Appendix N）\n- 问题：\n  - 核心比较（RF-filtered vs unfiltered）：p=0.407（rf_soft）、p=0.492（rf_moderate）、p=0.607（rf_strict），全部不显著\n  - RF vs random 的 3 个 pairwise 比较（p=0.002, 0.020, <0.001）未进行 Bonferroni 校正；Appendix N 声称 \"2 of 3 comparisons surviving\" Bonferroni（α=0.05/3=0.017），但 rf_moderate vs random_moderate 的 p=0.020 不通过\n  - 效应量微小：rf_soft vs unfiltered 的 Δ=+0.043 PPL（<0.3% relative）\n  - 仅 5 seeds，power 极低\n- 论文诚实地报告了 p 值并承认 \"inconclusive\"，但 Appendix N 的 framing（\"2 of 3 surviving Bonferroni\"）给读者留下了部分显著的印象\n- 建议：(1) 统一使用 Bonferroni-corrected p 值，明确标注 rf_moderate vs random_moderate 不通过；(2) 在 Discussion 中将 curation 描述为 \"negative result\" 而非 \"inconclusive preliminary evidence\"；(3) 删除或大幅缩减 curation PoC 篇幅，避免读者产生误导性的实用价值预期\n\n**W5 [Should-Fix]: VIF>10 for 14-16/19 features 下的 feature importance 解释过度。**\n- 具体位置：§4.2, Table 3, footnote 3\n- 问题：当 VIF>10 时，Gini importance 在高共线性特征间分配不稳定。论文的脚注承认 \"individual rankings should be interpreted cautiously given high multicollinearity\"，但紧接着在 Table 3 中详细报告了每个 cell 的逐个特征排名和精确 importance 值（如 .17、.15、.11）。§4.2 声称 \"p90_ppl ranks top-2 by Gini importance in all 9 cells\" 和 \"var_surprisal in 8/9 under SHAP\"——在 effective dimensionality 仅 4-5 的情况下，这些个体排名的稳定性存疑。\n- group-level dominance 的 claim（perplexity tail family 主导）有 Kendall's W=0.90 支持，是可靠的\n- 但 Table 3 的呈现方式暗示了比数据支持的更高的特征级别精度\n- 建议：(1) 明确区分 group-level claim（可靠）和 individual feature claim（不可靠）；(2) 报告 bootstrap stability 的特征排名（重采样 1000 次后 p90_ppl 排名 top-2 的概率）；(3) 考虑使用 PCA 或 elastic net 来处理共线性后再解释 importance\n\n**W6 [Should-Fix]: EDD 定义的 contiguous prefix 要求在非单调场景下过于保守，且无替代方案。**\n- 具体位置：Definition 1（§3.5），Limitations\n- 问题：EDD 要求从 (0,1) 到 (d*,d*+1) 的所有 pairwise AUC 都超过阈值 T。当 AUC profile 非单调时（如 Qwen2.5-7B 的 U 型，Limitations 中提到的 cross-strategy inversion 导致 d1v2 AUC 低至 0.129），EDD 会大幅低估真实的可区分范围。\n- 对 1-1.5B 基模型，AUC 严格单调递减，EDD 表现良好。但论文将 EDD 作为通用指标推广，在 7B+ 和 cross-strategy 场景下它的保守性成为系统性偏差\n- 论文在 Limitations 中承认了这一点（\"extending EDD to handle non-contiguous discriminable regions is future work\"），但没有提供任何替代定义或敏感性分析\n- 建议：(1) 提供一个补充指标（如 \"Maximum Discriminable Depth\" = max{d : AUC(d,d+1) ≥ T}）来覆盖非单调场景；(2) 在 §3.5 中明确 EDD 的适用条件（monotonic AUC decay）而非仅在脚注中提及\n\n**W7 [Should-Fix]: Cross-seed replication 覆盖不足（3/9 cells），且方向一致的 seed=43 优势未被解释。**\n- 具体位置：Appendix M, Limitations\n- 问题：\n  - 仅 3 个 cell（Pythia/OLMo/GPT-2 XL nucleus）有 cross-seed replication；其余 6 个 cell（所有 temperature 和 top-k 配置）均为 single-seed\n  - seed=43 在所有 3 个 cell 中均优于 seed=42（+0.14 到 +3.17pp），且 2/3 差异统计显著（CI 不重叠）。方向一致的偏差暗示 seed=42 可能系统性偏低，而非 seed=43 偏高\n  - single-seed 不确定性为 ~1-3pp，这意味着 Table 2 中跨 cell 的许多差异（如 Pythia nucleus 78.7% vs OLMo nucleus 78.9% 仅差 0.2pp）可能完全在 seed noise 范围内\n- 建议：(1) 至少对 3 个 temperature cells 补充 seed=43 replication；(2) 讨论 seed=43 系统性偏高的可能原因；(3) 在 Table 2 的 caption 中注明 single-seed uncertainty ~1-3pp\n\n**W8 [Should-Fix]: Full-replacement scope 声明在 Introduction/Abstract 中不够前置。**\n- 具体位置：Abstract（第 2 句）、Introduction §1 段 2\n- 问题：Abstract 第 2 句提到 \"controlled full-replacement recursive chains\"，但对不熟悉模型坍塌文献的读者来说，\"full-replacement\" 的含义及其对实际场景的限制不明显。Introduction 在第 2 段才解释这一点，并指出 \"real-world contamination typically involves partial mixing (accumulation)\"。\n- 论文在 Discussion 中声称 cross-model/cross-strategy transfer 应被视为 \"ceiling estimates for the mixed-data regime\"，但这一 claim 未经任何实验验证——accumulation 设置下的特征行为可能完全不同（不仅仅是 \"attenuated\"）\n- \"upper bound on depth signal strength\" 的论证是直觉性的（full-replacement 最大化深度信号），但缺乏理论或实验支持\n- 建议：(1) 在 Abstract 中明确说明这是 full-replacement 的 upper bound 结果；(2) 至少做一个 toy-scale accumulation 实验来验证 \"upper bound\" 假设\n\n**W9 [Minor]: 单一 LoRA 超参数配置。**\n- 具体位置：§3.2, Table 5\n- 所有 9 个 cell 使用完全相同的 LoRA 配置（r=16, α=32, lr=2e-4, 3 epochs）。不同的 LoRA rank 或学习率可能改变递归链的衰退速度，从而影响深度信号强度。缺少对 rank r（如 r=4, 8, 32）或 learning rate 的敏感性分析。\n\n**W10 [Minor]: Prompted generation 验证仅覆盖 1/9 cell。**\n- 具体位置：§5.3, Appendix O\n- 仅 GPT-2 XL nucleus 一个 cell 验证了 prompted generation（69.5%，-13.8pp）。13.8pp 的下降幅度不小；在 top-k 或 temperature 配置下（本已准确率较低），prompted generation 可能将准确率推向 chance level。\n\n---\n\n### Questions\n\n**Q1:** Table 8（Appendix H）显示 self-reference 在 Pythia 数据上提供 4.1-11.3pp 优势。§3.4 如何将此与 \"no systematic advantage\" 的 claim 调和？\n\n**Q2:** Curation PoC 中 rf_moderate vs random_moderate 的 p=0.020 在 Bonferroni 校正（α=0.017）下不通过，但 Appendix N 声称 \"2 of 3 comparisons surviving\"。请澄清具体哪两个通过了？\n\n**Q3:** 论文声称 full-replacement 结果是 accumulation 设置的 \"upper bound\"。是否有任何实验或理论依据支持这一单调性假设？是否存在 accumulation 反而增强某些深度信号的可能？\n\n**Q4:** seed=43 在所有 3 个 cell 中系统性优于 seed=42。是否检查了 seed=42 的 LoRA 训练是否有异常（如训练不收敛、outlier 比例异常）？Appendix M 提到 seed=42 下 d3 outlier 比例为 0.56%，seed=43 为 12.8%——但 seed=43 反而准确率更高，这似乎矛盾。\n\n**Q5:** 对于 cross-strategy transfer 中 d1/d2 boundary inversion（d1v2 AUC < 0.5），两阶段 pipeline 仅恢复了 11.5pp。在策略未知的实际部署中（d1-d3: 45.9%），这一准确率是否足以支持 \"data auditing\" 的实用 claim？\n\n---\n\n### Missing References\n\n未发现重大遗漏。Related Work 覆盖了 model collapse theory、AI text detection、membership inference、ordinal classification 和 decoding strategy effects 的主要工作。建议补充：\n- 关于 synthetic data contamination in the wild 的实证研究（如果有 2025-2026 的新工作）\n- 关于 LoRA 微调与模型坍塌交互的工作（如果存在）\n\n---\n\n### 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 1-1.5B full-replacement 范围内的实验设计扎实（LOGO control、多 baseline、多泛化轴），但 reference model circularity claim 与消融数据矛盾（W1），cross-scale 结论受 5 个混淆因素限制（W2），curation PoC 主比较不显著且多重比较校正有误（W4）。Feature importance 在高共线性下的解释超出了数据支持的范围（W5）。 |\n| **Excitement** | 3.5/5 | 任务形式化是真正的新贡献，EDD 指标有操作价值。但 full-replacement 限制降低了生态效度；cross-strategy barrier（d1-d3: 45.9%）和 scale attenuation（14B EDD=0）使得从实验室到部署的路径不清晰。 |\n| **Reproducibility** | 3/5 | LoRA 超参（Table 5）、RF 配置、软件版本和硬件均已报告。但：(1) 代码/数据 \"upon acceptance\" 未提供匿名链接；(2) Wikipedia subset 的选择方法未说明；(3) 仅 3/9 cells 有 cross-seed replication。 |\n| **Confidence** | 4/5 | 我仔细阅读了论文全文和附录，熟悉 model collapse 和 AI text detection 文献。不太确定的点是 accumulation 设置下的理论预期。 |\n\n### Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n**一句话总结：** 任务形式化有价值且实验系统全面，但 reference model circularity 的误导性 claim、cross-scale 结论的不可靠性、以及 d0 inflation 对核心 d1-d3 性能的掩盖，使论文在方法严谨性上存在需要修复的问题。\n\n本文的核心贡献——将递归生成深度估计形式化为序数分类并构建系统性基准——是有意义的。在 1-1.5B full-replacement 范围内的实验设计是审慎的，控制实验（LOGO、negative control、reverse chain）是亮点。但论文在几个关键点上的 claim 强度超过了数据支持：(1) reference model \"no systematic advantage\" 与 Table 8 矛盾；(2) cross-scale \"depth signal persists\" 对 14B（EDD=0）不成立；(3) d1-d3 balanced accuracy（核心指标）在跨模型/跨策略迁移中仅 55.4%/45.9%，显著低于 headline 四类准确率。修复 W1-W3 后，论文有望达到 Conference 水准。\n\n---\n\n### Detailed Comments（按 Section）\n\n**Abstract:** \"69-86% four-class accuracy\" 应明确标注包含 d0 inflation。建议改为以 d1-d3 balanced accuracy 为主指标。\"depth signal persists at larger scales\" 对 14B（EDD=0）不准确。\n\n**§1 Introduction:** 第 2 段对 full-replacement scope 的说明是必要的，但应更前置（移到第 1 段末尾或与任务定义一起出现）。Contribution 列表中的 \"EDD_{0.70}=4 for all three families\" 需注明这是 1-1.5B 的结果。\n\n**§3.4 Reference model:** \"confers no systematic advantage\" 需要修正为 \"confers a measurable advantage on same-family data (4-11pp; Appendix H) but does not drive the cross-generator accuracy ranking\"。当前表述具有误导性。\n\n**§3.5 EDD:** Definition 1 的适用条件（monotonic AUC decay）应在定义而非脚注中明确。当前脚注提到 Qwen2.5-7B 的非单调性，但读者在阅读 Definition 1 时不一定注意到这个限制。\n\n**§4.1 In-Distribution Performance:** Table 2 的 caption 已提到 \"Depth-0 recall exceeds 97%\"，但建议增加 d1-d3 balanced accuracy 列以便读者直接比较。\n\n**§4.2 Feature Consistency:** 建议将 footnote 3（multicollinearity caveat）提升为正文段落，并在 Table 3 的 caption 中明确注明 \"individual feature rankings are unstable under VIF>10; group-level dominance is robust\"。\n\n**§5.1 Classifier Comparison:** \"within 0.4pp\" 的收敛 claim 是否经过等价性检验（如 TOST）？如果仅是 observed difference，应说明 \"observed difference ≤ 0.4pp\" 而非暗示统计等价。\n\n**§5.4 Cross-Scale:** 建议将 \"existence proof\" 的 claim 限制为 7-8B（signal above chance），14B 明确标记为 boundary condition。当前表述 \"depth signal persists at larger scales\" 对 14B 不成立。\n\n**Appendix K Curation PoC:** 建议大幅压缩或移至补充材料的 \"inconclusive results\" 部分。当前篇幅和位置可能给读者造成 \"curation 有效\" 的印象。\n\n**Limitations:** 质量很高，建议将 reference model circularity 的更诚实表述（self-reference 4-11pp advantage）从 Limitations 提前到 §3.4 正文。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-19T06:40:06.977508+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4677
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-19T06:40:17.225294+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 ARR/EMNLP 2026 reviewer guidelines 和 review form', 'status': 'completed', 'activeForm': '搜索 ARR reviewer guidelines'}, {'content': '通读论文全文并记录关键发现', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '按官方维度逐项打分', 'status': 'completed', 'activeForm': '按官方维度逐项打分'}, {'content': '撰写完整审稿意见', 'status': 'completed', 'activeForm': '撰写完整审稿意见'}, {'content': '通过 review_reviewer_post_to_director 提交审稿意见', 'status': 'completed', 'activeForm': '提交审稿意见给 Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 ARR/EMNLP 2026 reviewer guidelines 和 review form', 'status': 'completed', 'activeForm': '搜索 ARR reviewer guidelines'}, {'content': '通读论文全文并记录关键发现', 'status': 'completed', 'activeForm': '通读论文全文'}, {'content': '按官方维度逐项打分', 'status': 'completed', 'activeForm': '按官方维度逐项打分'}, {'content': '撰写完整审稿意见', 'status': 'completed', 'activeForm': '撰写完整审稿意见'}, {'content': '通过 review_reviewer_post_to_director 提交审稿意见', 'status': 'completed', 'activeForm': '提交审稿意见给 Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-19T06:40:17.276089+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 668 · 2026-05-19T06:40:25.756646+00:00_

Round 1 审稿意见已提交给 Review Director。

核心评分：**Overall 3.5（Borderline Conference）**，Soundness 3.5/5，Excitement 3.5/5，Reproducibility 3/5，Confidence 4/5。

主要发现：
- **3 个 Must-Fix**：reference model circularity claim 与 Appendix H 消融数据矛盾（self-reference 实际带来 4-11pp 优势）；cross-scale 的 5 个混淆因素使 14B 结论不可靠；d0 >97% recall 系统性膨胀 headline metrics
- **5 个 Should-Fix**：curation PoC 主比较不显著且多重比较校正有误；VIF>10 下 feature importance 解释过度；EDD contiguous prefix 在非单调场景下过于保守；cross-seed replication 仅覆盖 3/9 cells 且 seed=43 系统性偏高；full-replacement scope 在 abstract 中不够前置
- **2 个 Minor**：单一 LoRA 配置、prompted generation 仅验证 1/9 cell

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 25

## Round 25

24 recorded events


### User

_source line 669 · 2026-05-19T06:42:21.174678+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 2 完整审稿意见

**Overall Assessment: 3.0 (Findings), Confidence 4/5**

**一句话总结:** 论文提出了新颖且有价值的 recursive depth estimation 任务，实验全面且 reporting 诚实，但方法创新不足（标准 RF + 标准特征）、Discussion 过薄、full-replacement-only 设置限制实用性，达到 Findings 水平。

**Strengths:**
- S1: 新颖且及时的任务形式化，填补 data provenance 工具链空白
- S2: 3×3×4 atlas + 8 个泛化轴的系统实验设计
- S3: 高度诚实的 reporting（d1-d3 balanced acc alongside headline, 详尽 Limitations）
- S4: Feature consistency 发现有理论意义（验证 tail erosion 预测）
- S5: Related Work 覆盖全面，69 引用

**Must-Fix:**
- W1: Abstract 数字堆砌（20+ 数字），缺乏叙事吸引力和动机
- W2: Discussion 仅 ~200 words，无法承载 empirical study 的 insight 深度（应提升 Appendix A.17 的 provenance toolkit 讨论到正文，新增 cross-strategy barrier 和 collapse phase transition 分析）

**Should-Fix:**
- W3: 方法层面无算法贡献（RF + 已知特征），classifier convergence (0.4pp) 证明了 ceiling
- W4: Full-replacement only，缺乏 accumulation 实验（哪怕 pilot）
- W5: "confirming that..." -ing 短语模式全文出现 9+ 次，AI 写作痕迹明显
- W6: EDD 创新程度有限（本质是 pairwise AUC + threshold + contiguous prefix）
- W7: 14B 实验 5 个 confounds，Abstract 中的描述可能误导读者

**Minor:**
- W8: 3 条孤儿引用（llama3, qwen2.5, sugiyama2007）
- W9: Curation PoC 未做 multiple comparison correction

**Questions:**
- Q1: 与 Mohamed et al. (2025) "Broken Telephone" 的精确区分
- Q2: Cross-strategy d1/d2 inversion 是否质疑 depth 定义的 strategy-invariance
- Q3: GPT-2 XL 最高准确率是 architecture 还是 parameter count 效应
- Q4: EDD=4 跨三个 family 一致性有无理论基础

---

请对 R2 的每个 Weakness (W1-W9)、每个 Question (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。特别关注：你是否认同 R2 将 overall 降至 3.0 (Findings) 的判断？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-19T06:43:09.323064+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-19T06:43:09.674991+00:00_

1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification, constructing a 180K-passage benchmark spanning 3 model families, 3 decoding strategies, and 4 depths under controlled full-replacement recursive chains at the 1--1.5B scale.
4	A Random Forest over 19 statistical features, dominated by the perplexity tail family (\texttt{p90\_ppl}, \texttt{var\_surprisal}), achieves 69--86\% four-class accuracy (d1--d3 balanced: 59--82\%; chance = 25\%/33\%); the convergence of RF, XGBoost, and LightGBM within 0.4\,pp confirms that discriminative signal resides in feature design, not classifier choice.
5	Cross-model transfer reaches 66.4\% four-class (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, and a single-cell prompted-generation test 69.5\%.
6	Cross-strategy transfer (59.1\%, d1--d3: 45.9\%) reveals that decoding strategies induce structurally distinct degradation trajectories, a finding we formalize via the \emph{Effective Discriminable Depth} (EDD) metric ($\mathrm{EDD}_{0.70}{=}4$ for all three families).
7	Preliminary cross-scale experiments (7--14B, 54--70\%) provide an existence proof that depth signal persists at larger scales, though confounded by five factors including quantization and vocabulary mismatch.
8	Binary detectors and membership inference baselines (30--35\%) fall ${>}$43\,pp below our pipeline, confirming that ordinal depth estimation requires distributional statistics inaccessible from surface text.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-19T06:43:09.675350+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-19T06:43:10.127258+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	This paper formalizes recursive generation depth estimation as ordinal classification under controlled full-replacement chains.
5	The perplexity tail feature family dominates depth discrimination across all nine cells, with $\mathrm{EDD}_{0.70}{=}4$ for all three families (confirmed by 5-class extension, 71--80\%; Appendix~\ref{app:depth4_ext}); cross-model transfer reaches 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, while binary detectors and membership inference methods achieve only 30--35\%.
6	
7	\paragraph{Accumulation settings.}
8	Our benchmark uses full-replacement chains; in practice, model training involves accumulation, mixing human data with synthetic outputs at unknown proportions \cite{gerstgrasser2024_accumulate}.
9	Under accumulation, depth signal should attenuate because each generation retains human-originated distributional properties, slowing tail erosion.
10	The 66.4\% cross-model and 59.1\% cross-strategy transfer should be interpreted as ceiling estimates for the mixed-data regime.
11	Extending the framework to accumulation, where depth becomes a continuous mixing parameter, is a priority for future work.
12	
13	\paragraph{Scale and deployment implications.}
14	The depth signal attenuates with model scale: at 14B, d0/d1 separability drops sharply ($\mathrm{EDD}_{0.70}{=}0$), though d1--d3 discrimination persists above chance.
15	This suggests that depth estimation complements rather than replaces binary detection for practical data auditing: binary detectors handle the human-vs-machine boundary where depth estimation is redundant ($>$97\% d0 recall), while depth estimation provides the finer ordinal resolution that binary methods cannot.
16	A practical deployment path proceeds from controlled settings, where model and strategy are known, to partially known settings via strategy-identification routing, to fully unknown settings requiring strategy-invariant features (Appen
…[truncated 365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-19T06:43:10.228122+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
  "offset": "20",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
    "offset": "20",
    "limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-19T06:43:10.328996+00:00_

20	
21	\paragraph{Adjacent Tasks.}
22	EditLens \cite{editlens2026} estimates editing extent but does not model recursive chains; \citet{uchendu2020_attribution} classify \emph{which} model generated text; \citet{mohamed2025_broken_telephone} characterize \emph{how} text degrades under iterative generation without classifying which iteration a passage comes from.
23	Our task performs the inverse: ordinal depth estimation from text alone.
24	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-19T06:43:14.395687+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "confirming that",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "confirming that",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-19T06:43:15.350067+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.txt:300:354   p > 0.05; §5), confirming that the feature bottle- Appendix A.3.                                                                403
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.txt:1304:1400   tures (rep_3gram +37%, rep_4gram +75%                            depth passages, confirming that the multi-feature                                 1431
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.txt:1510:1619   confirming that the depth signal resides in the p90-          one-model-out, nucleus, 4-class). RF baseline from
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:537:Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:722:CORAL calibration improves ordinal structure (d1--d3 BalAcc 40.4\% vs.\ 33.3\% random) without closing the gap to RF (71.6\%), confirming that the bottleneck is the input signal rather than the calibration strategy.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:730:The top-2 features (\texttt{p90\_ppl} + \texttt{var\_surprisal}) retain combined importance of 28.7\%, confirming that perplexity tail statistics remain the dominant depth markers even after augmentation.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:771:Under correct strategy routing, four-class accuracy reaches 72.6\% vs.\ 68.0\% under misrouting ($N{=}103{,}498$ / $76{,}502$), a gap of 4.6\,pp; d0 accuracy remains near-ceiling (${\sim}99.6
…[truncated 1015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-19T06:43:15.551317+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", (confirming|demonstrating|highlighting|suggesting|indicating|revealing|establishing) ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", (confirming|demonstrating|highlighting|suggesting|indicating|revealing|establishing) ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "output_mode": "count"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-19T06:43:15.601975+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.txt:5
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:2
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:6
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:5

Found 20 total occurrences across 6 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-19T06:43:22.029417+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "llama3|qwen2\\.5|sugiyama2007|sugiyama",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "llama3|qwen2\\.5|sugiyama2007|sugiyama",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "output_mode": "content",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-19T06:43:22.130509+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:98:$\mathrm{EDD}_T$ reports the longest \emph{contiguous} discriminable prefix: the deepest $d$ such that every pair from $(0,1)$ through $(d{-}1, d)$ exceeds $T$.\footnote{AUC profiles decay monotonically for 1--1.5B models (\S\ref{sec:atlas}); Qwen2.5-7B shows non-monotonic patterns (\S\ref{sec:gen:crossscale}), where the contiguous formulation is more conservative (Limitations).}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex:15:Qwen2.5-14B confirms this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B), while d1--d3 AUCs remain above 0.70 (\S\ref{sec:gen:crossscale}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:18:Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (DeepSeek V3.2, 36.2\%; Qwen2.5-7B-Instruct, 30.4\%) also fail (43\,pp below the best RF cell; Appendix~\ref{app:zeroshot_prompt}); depth signal resides in distributional statistics inaccessible from surface text.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:110:Depth signal persists at larger scales: 7--8B models achieve 60--70\% and 14B (Qwen2.5-14B) reaches 54.1\% (d1--d3: 57.4\%, chance = 33\%), though confounded by five factors (quantization, sample size, single strategy, vocabulary mismatch, self-reference scoring; Appendix~\ref{app:cross_scale_confounds}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:123:Both DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:377:We extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct) and one 14B model (Qwen2.
…[truncated 7484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-19T06:43:28.858215+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*llama|\\\\cite\\{.*qwen|\\\\cite\\{.*sugiyama",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*llama|\\\\cite\\{.*qwen|\\\\cite\\{.*sugiyama",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "output_mode": "content",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-19T06:43:28.858821+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:15:At 7--8B (QLoRA), Llama-3.1-8B \cite{llama3} achieves 70.2\% ($\mathrm{EDD}_{0.70}{=}4$) and Qwen2.5-7B \cite{qwen2.5} 60.1\%.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:40:At 7--8B (QLoRA), Llama-3.1-8B \cite{llama3} achieves 70.2\% ($\mathrm{EDD}_{0.70}{=}4$) and Qwen2.5-7B \cite{qwen2.5} 60.1\%.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:62:At 7--8B (QLoRA), Llama-3.1-8B \cite{llama3} achieves 70.2\% ($\mathrm{EDD}_{0.70}{=}4$) and Qwen2.5-7B \cite{qwen2.5} 60.1\%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-19T06:43:33.333534+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-19T06:43:33.386080+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-19T06:43:36.602901+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "llama3|qwen2\\.5|sugiyama",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "llama3|qwen2\\.5|sugiyama",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-19T06:43:36.703759+00:00_

466:@article{sugiyama2007_importance_weighting,
467:  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\"u}ller, Klaus-Robert},
479:@misc{qwen2.5,
481:  title     = {{Qwen2.5: A Party of Foundation Models}},
487:@misc{llama3,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-19T06:43:43.182857+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{[^}]*llama3|\\\\cite[tp]?\\{[^}]*qwen2|\\\\cite[tp]?\\{[^}]*sugiyama",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[tp]?\\{[^}]*llama3|\\\\cite[tp]?\\{[^}]*qwen2|\\\\cite[tp]?\\{[^}]*sugiyama",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-19T06:43:43.233589+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:15:At 7--8B (QLoRA), Llama-3.1-8B \cite{llama3} achieves 70.2\% ($\mathrm{EDD}_{0.70}{=}4$) and Qwen2.5-7B \cite{qwen2.5} 60.1\%.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:40:At 7--8B (QLoRA), Llama-3.1-8B \cite{llama3} achieves 70.2\% ($\mathrm{EDD}_{0.70}{=}4$) and Qwen2.5-7B \cite{qwen2.5} 60.1\%.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:62:At 7--8B (QLoRA), Llama-3.1-8B \cite{llama3} achieves 70.2\% ($\mathrm{EDD}_{0.70}{=}4$) and Qwen2.5-7B \cite{qwen2.5} 60.1\%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-19T06:45:48.903162+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: Abstract 数字堆砌**\n同意。我逐一计数，abstract 9 句话中包含 20+ 个数值（180K、3×3、d0-d3、19、69-86%、59-82%、25%/33%、0.4pp、66.4%、55.4%、74.1%、69.5%、59.1%、45.9%、EDD_{0.70}=4、7-14B、54-70%、30-35%、43pp）。这确实读起来像 results summary 而非有吸引力的叙事。我的审稿（R1-W3）也指出 d0 inflation 的叙事问题，但未单独将 abstract 写作风格列为独立问题——R2 的诊断更精确。建议：减少到 8-10 个关键数字，将叙事主线放在 \"深度信号存在于困惑度尾部统计中\" 这一洞察上，而非罗列所有泛化实验。不过我认为这是 Should-Fix 而非 Must-Fix，因为 abstract 的信息完整性没有问题，只是叙事吸引力不足。\n\n**[AGREE] R2-W2: Discussion 过薄（~250 words）**\n同意 concern，但对严重程度的判断有分歧。Discussion+Conclusion（§6）约 250 words，3 个 paragraph，确实无法承载 9 个 cell + 8 个泛化轴的 insight 深度。Appendix N（Extended Discussion）的 provenance toolkit 讨论和 cross-strategy conditional decomposition 分析是有价值的材料，提升到正文会显著改善论文。然而，我认为这是 **Should-Fix** 而非 Must-Fix：Discussion 的薄弱影响的是论文的 impact/excitement 感知，而非 soundness 或核心 claims 的可靠性。正文 8 页的空间约束下，Discussion 被压缩是可以理解的。\n\n**[REBUT] R2-W3: 方法层面无算法贡献**\n不同意将此作为显著扣分项。理由：\n1. 论文在 §1 明确声明 \"our contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty\"——这是自觉的 empirical contribution 定位。\n2. ARR reviewer guidelines 列出了 17 个 common review issues，其中 H2 明确警告不要 \"demanding state-of-the-art results or novel algorithms when the paper's contribution is elsewhere\"。\n3. Classifier convergence（RF/XGBoost/LightGBM 在 0.4pp 内收敛，§5.1）本身是一个有价值的 empirical finding：它证明了信号瓶颈在特征设计而非分类器——这一结论指导了未来研究方向（改进特征而非改进分类器）。\n4. 类比：许多被广泛引用的 NLP benchmark 论文（如 GLUE、SuperGLUE、MMLU）的方法贡献也是 \"standard model + standard protocol\"，其价值在于 task formalization 和 systematic evaluation。\n5. R2 自己也在 S1 中认可了 \"novel and timely task formalization\"——如果任务形式化是核心贡献，那么用标准方法证明信号存在性正是合适的方法论选择。\n\n**[AGREE] R2-W4: Full-replacement only，缺乏 accumulation 实验**\n完全同意。我的审稿（R1-W8）也将此列为 Should-Fix。论文在 Discussion 中声称 full-replacement 结果是 accumulation 的 \"ceiling estimate\"（§6, para 2），但这一单调性假设缺乏理论或实验支持。即使是一个 toy-scale 实验（如 50% human + 50% synthetic 的 2-depth 混合链）也会大幅增强论文的生态效度。\n\n**[AGREE] R2-W5: -ing 短语 AI 写作痕迹**\n事实确认：我 grep 了全文，\", confirming/demonstrating/suggesting/indicating/revealing/establishing \" 模式在正文+附录中出现 **20 次**（仅 \"confirming that\" 就有 8 次），R2 的 \"9+ 次\" 是保守估计。这确实是显著的 AI 写作标志。但我将此列为 **Minor** 而非 Should-Fix：ARR guidelines 强调 \"assess substance over style\"，这些模式不影响论文的技术内容或可读性。修复也很简单（将 -ing 分词短语改写为独立句子）。\n\n**[REBUT] R2-W6: EDD 创新程度有限**\n部分不同意。R2 将 EDD 描述为 \"pairwise AUC + threshold + contiguous prefix\"，这在技术组件层面是准确的，但低估了其概念贡献：\n1. EDD 的价值不在于组件的技术新颖性，而在于**将 model collapse 理论的定性预测转化为可操作的定量指标**。这类 operationalization 在 NLP 中有悠久传统（BLEU = n-gram precision + brevity penalty；ROUGE = recall-based overlap；BERTScore = contextual embedding similarity——组件都不新，但组合后的 operationalization 有独立价值）。\n2. contiguous prefix 要求使 EDD 具有可解释的语义：\"前 d 个深度都可以可靠区分\"，比简单的 \"最大可区分对\" 更有实际部署意义。\n3. 不过，我在 R1-W6 中指出了 EDD 在非单调场景下的过度保守性（如 Qwen2.5-7B 的 U 型 AUC），论文没有提供替代指标。这是 EDD 定义的一个真实局限，但不等于 \"创新不足\"。\n\n**[AGREE] R2-W7: 14B 实验 5 个 confounds 在 Abstract 中的描述可能误导**\n强烈同意。我的审稿（R1-W2）将此列为 Must-Fix。Abstract 中 \"depth signal persists at larger scales\" 对 14B（EDD=0, d0v1 AUC=0.643）不成立。5 个混淆因素（QLoRA量化 / 500 samples / 单策略 / 词表不匹配 / self-reference）使 cross-scale 结论不可靠。R2 和我在这一点上完全一致。\n\n**[AGREE] R2-W8: 3 条孤儿引用**\n已验证：`llama3`、`qwen2.5`、`sugiyama2007_importance_weighting` 存在于 references.bib 中，但在实际提交的 tex 文件中**均未被 \\cite**（仅出现在 drafts/ 目录的未使用草稿中）。这是提交前清理的遗漏，属于 Minor 但应修复。\n\n**[AGREE] R2-W9: Curation PoC 未做 multiple comparison correction**\n同意，且我的审稿（R1-W4）对此有更详细的分析：rf_moderate vs random_moderate 的 p=0.020 在 Bonferroni 校正（α=0.017）下不通过，但 Appendix N 声称 \"2 of 3 surviving\"。R2 的 concern 与我一致。\n\n---\n\n### Questions 逐条回应\n\n**[REBUT] R2-Q1: 与 Mohamed et al. (2025) \"Broken Telephone\" 的区分**\nRelated Work §2（Adjacent Tasks 段）已明确区分：\"Mohamed et al. (2025) characterize *how* text degrades under iterative generation without classifying which iteration a passage comes from. Our task performs the inverse: ordinal depth estimation from text alone.\" 区分是清晰的：Mohamed et al. 分析退化现象（descriptive），本文估计迭代次数（predictive/classificatory）。不过，可以建议作者补充一句说明为什么 \"Broken Telephone\" 的 degradation characterization 不能直接用于深度分类（如：是否因为其特征不具有序数单调性？）。\n\n**[AGREE] R2-Q2: Cross-strategy d1/d2 inversion 是否质疑 depth 的 strategy-invariance**\n这是一个有深度的概念问题。我的回答是：它质疑的不是 **depth 定义的 strategy-invariance**（depth 是过程定义，策略无关），而是**基于当前特征集的 depth estimation 的 strategy-invariance**。温度采样加速收敛（§3.6），使得 temp d1 的统计特征类似于 nucleus d2——这是特征空间的对齐问题，不是深度定义的问题。但 R2 提出这个问题的价值在于：论文应更明确地区分 \"depth as a process property\"（strategy-invariant）和 \"depth estimation via perplexity features\"（strategy-dependent）。当前的 Discussion 没有充分展开这一区分，这也印证了 R2-W2（Discussion 过薄）的 concern。\n\n**[REBUT] R2-Q3: GPT-2 XL 最高准确率是 architecture 还是 parameter count**\n参数量不能解释准确率排序。OLMo-1B（1B 参数）在 temperature 策略下达到 82.3%，超过 Pythia-1.4B（1.4B）的 76.8%——如果参数量是主导因素，这一反转不应出现。更可能的解释是训练数据差异：GPT-2 XL（WebText）的训练数据与 Wikipedia seed 的分布差异可能产生了更强的深度信号（cross-distribution feature extraction）。这一点可以通过 Table 8（Appendix H）的 reference model ablation 间接验证：当 Pythia 数据使用 GPT-2 XL 作为参考模型时准确率**最低**（67.3%），而 GPT-2 XL 数据使用 Pythia 作为参考模型时准确率**最高**（85.9%）——这暗示 generator 与 reference 的分布差异本身可能放大了深度信号，值得进一步调查。\n\n**[AGREE] R2-Q4: EDD=4 跨三个 family 的一致性有无理论基础**\n§3.6 提供了部分理论基础（tail mass 以 α^k 收缩，α 为 contraction factor），如果三个模型的 α 在 1-1.5B 尺度下相近，EDD 收敛是可预期的。但仅 3 个模型族构不成统计意义上的 \"一致性\"——这可能是 scale 约束下的巧合。论文将 \"EDD_{0.70}=4 for all three families\" 写入 abstract 和 contribution 列表，但没有提供理论预测或 bootstrap 检验来支持这一一致性的显著性。R2 的质疑合理。\n\n---\n\n### 对 R2 Overall Assessment (3.0, Findings) 的评价\n\n**我不完全认同将 overall 降至 3.0。** 我的评分为 3.5（Borderline Conference），与 R2 的核心分歧在 W3（方法无算法贡献）和 W6（EDD 创新有限）：\n\n1. **W3 的权重分歧**：R2 将 \"RF + 已知特征\" 视为 Should-Fix 级别的弱点，但 ARR guidelines 明确警告不要惩罚 empirical contribution 论文缺乏算法创新。论文的价值在于：(a) 定义了一个被忽视但重要的新任务；(b) 通过系统实验证明了信号的存在性和特征结构；(c) 证明了分类器不是瓶颈。这种 \"task + benchmark + systematic empirical characterization\" 的贡献模式在 *ACL venues 中有清晰的先例。\n\n2. **W6 与 W3 的耦合**：如果因为 RF 不新（W3）又因为 EDD 不新（W6），论文的方法贡献就被双重折扣了。但 EDD 的贡献是 operationalization 而非 algorithmic novelty，与 W3 属于不同维度。\n\n3. **R2 与 R1 的共识区域**：我们在以下问题上完全一致——full-replacement scope limitation（R2-W4 / R1-W8）、cross-scale confounds（R2-W7 / R1-W2）、curation PoC 不显著（R2-W9 / R1-W4）、Abstract 需要改善（R2-W1 / R1-W3 部分重叠）。这些问题是 **可修复的**，不构成 fundamental flaw。\n\n4. **R2 比 R1 更敏感的区域**：Discussion 厚度（W2）和 AI 写作痕迹（W5）。这些是合理的关注，但它们的修复成本低（增写 Discussion + 改写 -ing 短语），不应将论文从 Conference 边缘推到 Findings。\n\n5. **R1 比 R2 更敏感的区域**：Reference model circularity（R1-W1）、feature importance 在高共线性下的过度解释（R1-W5）、cross-seed 覆盖不足（R1-W7）。这些是 R2 未覆盖的方法严谨性问题，但同样可修复。\n\n**综合判断**：论文的 Must-Fix 问题（reference model claim 矛盾、cross-scale claim 校准、d0 inflation 前置）是 claim-strength 校准问题，而非 fundamental methodological flaw。在 claim 校准后，任务形式化 + 系统实验 + EDD 指标 + 特征一致性发现的组合贡献足以支撑 Borderline Conference（3.5），前提是作者在 rebuttal 中充分回应 W1-W3 的修复方案。如果 rebuttal 不能令人信服地回应 reference model circularity 和 cross-scale confounds，我会降至 3.0。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: Abstract 数字堆砌**\n同意。我逐一计数，abstract 9 句话中包含 20+ 个数值（180K、3×3、d0-d3、19、69-86%、59-82%、25%/33%、0.4pp、66.4%、55.4%、74.1%、69.5%、59.1%、45.9%、EDD_{0.70}=4、7-14B、54-70%、30-35%、43pp）。这确实读起来像 results summary 而非有吸引力的叙事。我的审稿（R1-W3）也指出 d0 inflation 的叙事问题，但未单独将 abstract 写作风格列为独立问题——R2 的诊断更精确。建议：减少到 8-10 个关键数字，将叙事主线放在 \"深度信号存在于困惑度尾部统计中\" 这一洞察上，而非罗列所有泛化实验。不过我认为这是 Should-Fix 而非 Must-Fix，因为 abstract 的信息完整性没有问题，只是叙事吸引力不足。\n\n**[AGREE] R2-W2: Discussion 过薄（~250 words）**\n同意 concern，但对严重程度的判断有分歧。Discussion+Conclusion（§6）约 250 words，3 个 paragraph，确实无法承载 9 个 cell + 8 个泛化轴的 insight 深度。Appendix N（Extended Discussion）的 provenance toolkit 讨论和 cross-strategy conditional decomposition 分析是有价值的材料，提升到正文会显著改善论文。然而，我认为这是 **Should-Fix** 而非 Must-Fix：Discussion 的薄弱影响的是论文的 impact/excitement 感知，而非 soundness 或核心 claims 的可靠性。正文 8 页的空间约束下，Discussion 被压缩是可以理解的。\n\n**[REBUT] R2-W3: 方法层面无算法贡献**\n不同意将此作为显著扣分项。理由：\n1. 论文在 §1 明确声明 \"our contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty\"——这是自觉的 empirical contribution 定位。\n2. ARR reviewer guidelines 列出了 17 个 common review issues，其中 H2 明确警告不要 \"demanding state-of-the-art results or novel algorithms when the paper's contribution is elsewhere\"。\n3. Classifier convergence（RF/XGBoost/LightGBM 在 0.4pp 内收敛，§5.1）本身是一个有价值的 empirical finding：它证明了信号瓶颈在特征设计而非分类器——这一结论指导了未来研究方向（改进特征而非改进分类器）。\n4. 类比：许多被广泛引用的 NLP benchmark 论文（如 GLUE、SuperGLUE、MMLU）的方法贡献也是 \"standard model + standard protocol\"，其价值在于 task formalization 和 systematic evaluation。\n5. R2 自己也在 S1 中认可了 \"novel and timely task formalization\"——如果任务形式化是核心贡献，那么用标准方法证明信号存在性正是合适的方法论选择。\n\n**[AGREE] R2-W4: Full-replacement only，缺乏 accumulation 实验**\n完全同意。我的审稿（R1-W8）也将此列为 Should-Fix。论文在 Discussion 中声称 full-replacement 结果是 accumulation 的 \"ceiling estimate\"（§6, para 2），但这一单调性假设缺乏理论或实验支持。即使是一个 toy-scale 实验（如 50% human + 50% synthetic 的 2-depth 混合链）也会大幅增强论文的生态效度。\n\n**[AGREE] R2-W5: -ing 短语 AI 写作痕迹**\n事实确认：我 grep 了全文，\", confirming/demonstrating/suggesting/indicating/revealing/establishing \" 模式在正文+附录中出现 **20 次**（仅 \"confirming that\" 就有 8 次），R2 的 \"9+ 次\" 是保守估计。这确实是显著的 AI 写作标志。但我将此列为 **Minor** 而非 Should-Fix：ARR guidelines 强调 \"assess substance over style\"，这些模式不影响论文的技术内容或可读性。修复也很简单（将 -ing 分词短语改写为独立句子）。\n\n**[REBUT] R2-W6: EDD 创新程度有限**\n部分不同意。R2 将 EDD 描述为 \"pairwise AUC + threshold + contiguous prefix\"，这在技术组件层面是准确的，但低估了其概念贡献：\n1. EDD 的价值不在于组件的技术新颖性，而在于**将 model collapse 理论的定性预测转化为可操作的定量指标**。这类 operationalization 在 NLP 中有悠久传统（BLEU = n-gram precision + brevity penalty；ROUGE = recall-based overlap；BERTScore = contextual embedding similarity——组件都不新，但组合后的 operationalization 有独立价值）。\n2. contiguous prefix 要求使 EDD 具有可解释的语义：\"前 d 个深度都可以可靠区分\"，比简单的 \"最大可区分对\" 更有实际部署意义。\n3. 不过，我在 R1-W6 中指出了 EDD 在非单调场景下的过度保守性（如 Qwen2.5-7B 的 U 型 AUC），论文没有提供替代指标。这是 EDD 定义的一个真实局限，但不等于 \"创新不足\"。\n\n**[AGREE] R2-W7: 14B 实验 5 个 confounds 在 Abstract 中的描述可能误导**\n强烈同意。我的审稿（R1-W2）将此列为 Must-Fix。Abstract 中 \"depth signal persists at larger scales\" 对 14B（EDD=0, d0v1 AUC=0.643）不成立。5 个混淆因素（QLoRA量化 / 500 samples / 单策略 / 词表不匹配 / self-reference）使 cross-scale 结论不可靠。R2 和我在这一点上完全一致。\n\n**[AGREE] R2-W8: 3 条孤儿引用**\n已验证：`llama3`、`qwen2.5`、`sugiyama2007_importance_weighting` 存在于 references.bib 中，但在实际提交的 tex 文件中**均未被 \\cite**（仅出现在 drafts/ 目录的未使用草稿中）。这是提交前清理的遗漏，属于 Minor 但应修复。\n\n**[AGREE] R2-W9: Curation PoC 未做 multiple comparison correction**\n同意，且我的审稿（R1-W4）对此有更详细的分析：rf_moderate vs random_moderate 的 p=0.020 在 Bonferroni 校正（α=0.017）下不通过，但 Appendix N 声称 \"2 of 3 surviving\"。R2 的 concern 与我一致。\n\n---\n\n### Questions 逐条回应\n\n**[REBUT] R2-Q1: 与 Mohamed et al. (2025) \"Broken Telephone\" 的区分**\nRelated Work §2（Adjacent Tasks 段）已明确区分：\"Mohamed et al. (2025) characterize *how* text degrades under iterative generation without classifying which iteration a passage comes from. Our task performs the inverse: ordinal depth estimation from text alone.\" 区分是清晰的：Mohamed et al. 分析退化现象（descriptive），本文估计迭代次数（predictive/classificatory）。不过，可以建议作者补充一句说明为什么 \"Broken Telephone\" 的 degradation characterization 不能直接用于深度分类（如：是否因为其特征不具有序数单调性？）。\n\n**[AGREE] R2-Q2: Cross-strategy d1/d2 inversion 是否质疑 depth 的 strategy-invariance**\n这是一个有深度的概念问题。我的回答是：它质疑的不是 **depth 定义的 strategy-invariance**（depth 是过程定义，策略无关），而是**基于当前特征集的 depth estimation 的 strategy-invariance**。温度采样加速收敛（§3.6），使得 temp d1 的统计特征类似于 nucleus d2——这是特征空间的对齐问题，不是深度定义的问题。但 R2 提出这个问题的价值在于：论文应更明确地区分 \"depth as a process property\"（strategy-invariant）和 \"depth estimation via perplexity features\"（strategy-dependent）。当前的 Discussion 没有充分展开这一区分，这也印证了 R2-W2（Discussion 过薄）的 concern。\n\n**[REBUT] R2-Q3: GPT-2 XL 最高准确率是 architecture 还是 parameter count**\n参数量不能解释准确率排序。OLMo-1B（1B 参数）在 temperature 策略下达到 82.3%，超过 Pythia-1.4B（1.4B）的 76.8%——如果参数量是主导因素，这一反转不应出现。更可能的解释是训练数据差异：GPT-2 XL（WebText）的训练数据与 Wikipedia seed 的分布差异可能产生了更强的深度信号（cross-distribution feature extraction）。这一点可以通过 Table 8（Appendix H）的 reference model ablation 间接验证：当 Pythia 数据使用 GPT-2 XL 作为参考模型时准确率**最低**（67.3%），而 GPT-2 XL 数据使用 Pythia 作为参考模型时准确率**最高**（85.9%）——这暗示 generator 与 reference 的分布差异本身可能放大了深度信号，值得进一步调查。\n\n**[AGREE] R2-Q4: EDD=4 跨三个 family 的一致性有无理论基础**\n§3.6 提供了部分理论基础（tail mass 以 α^k 收缩，α 为 contraction factor），如果三个模型的 α 在 1-1.5B 尺度下相近，EDD 收敛是可预期的。但仅 3 个模型族构不成统计意义上的 \"一致性\"——这可能是 scale 约束下的巧合。论文将 \"EDD_{0.70}=4 for all three families\" 写入 abstract 和 contribution 列表，但没有提供理论预测或 bootstrap 检验来支持这一一致性的显著性。R2 的质疑合理。\n\n---\n\n### 对 R2 Overall Assessment (3.0, Findings) 的评价\n\n**我不完全认同将 overall 降至 3.0。** 我的评分为 3.5（Borderline Conference），与 R2 的核心分歧在 W3（方法无算法贡献）和 W6（EDD 创新有限）：\n\n1. **W3 的权重分歧**：R2 将 \"RF + 已知特征\" 视为 Should-Fix 级别的弱点，但 ARR guidelines 明确警告不要惩罚 empirical contribution 论文缺乏算法创新。论文的价值在于：(a) 定义了一个被忽视但重要的新任务；(b) 通过系统实验证明了信号的存在性和特征结构；(c) 证明了分类器不是瓶颈。这种 \"task + benchmark + systematic empirical characterization\" 的贡献模式在 *ACL venues 中有清晰的先例。\n\n2. **W6 与 W3 的耦合**：如果因为 RF 不新（W3）又因为 EDD 不新（W6），论文的方法贡献就被双重折扣了。但 EDD 的贡献是 operationalization 而非 algorithmic novelty，与 W3 属于不同维度。\n\n3. **R2 与 R1 的共识区域**：我们在以下问题上完全一致——full-replacement scope limitation（R2-W4 / R1-W8）、cross-scale confounds（R2-W7 / R1-W2）、curation PoC 不显著（R2-W9 / R1-W4）、Abstract 需要改善（R2-W1 / R1-W3 部分重叠）。这些问题是 **可修复的**，不构成 fundamental flaw。\n\n4. **R2 比 R1 更敏感的区域**：Discussion 厚度（W2）和 AI 写作痕迹（W5）。这些是合理的关注，但它们的修复成本低（增写 Discussion + 改写 -ing 短语），不应将论文从 Conference 边缘推到 Findings。\n\n5. **R1 比 R2 更敏感的区域**：Reference model circularity（R1-W1）、feature importance 在高共线性下的过度解释（R1-W5）、cross-seed 覆盖不足（R1-W7）。这些是 R2 未覆盖的方法严谨性问题，但同样可修复。\n\n**综合判断**：论文的 Must-Fix 问题（reference model claim 矛盾、cross-scale claim 校准、d0 inflation 前置）是 claim-strength 校准问题，而非 fundamental methodological flaw。在 claim 校准后，任务形式化 + 系统实验 + EDD 指标 + 特征一致性发现的组合贡献足以支撑 Borderline Conference（3.5），前提是作者在 rebuttal 中充分回应 W1-W3 的修复方案。如果 rebuttal 不能令人信服地回应 reference model circularity 和 cross-scale confounds，我会降至 3.0。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-19T06:45:52.969162+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4065
}
```

</details>

---


### Assistant

_source line 692 · 2026-05-19T06:46:05.798430+00:00_

交叉回应已提交。

要点总结：
- 与 R2 在 **7 个 Weakness 上一致**（W1/W2/W4/W5/W7/W8/W9），但对 W1 和 W2 的严重程度判断不同（我认为是 Should-Fix，R2 认为 Must-Fix）
- **反驳了 2 个 Weakness**：W3（方法无算法贡献——ARR guidelines 明确不应惩罚 empirical contribution 论文）和 W6（EDD 创新有限——operationalization 有独立价值）
- **不认同降至 3.0**：核心分歧在于 W3/W6 的权重。问题是 claim-strength 校准而非 fundamental flaw，修复后足以支撑 3.5（Borderline Conference）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 26

## Round 26

88 recorded events


### User

_source line 693 · 2026-05-20T06:27:03.576691+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性）

### Venue 信息
- **目标会议**: EMNLP 2026（通过 ACL Rolling Review）
- **ARR May cycle 截止**: 2026-05-25
- **EMNLP commitment deadline**: 2026-08-02
- **格式**: Long paper，正文 8 页限制，参考文献不限，ACL 模板，double-blind
- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）

### 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`
- main.tex 通过 \input 引入：abstract, introduction, related_work, method, theory, atlas, generalization, discussion, conclusion, section_appendix

### 你的审查侧重：方法严谨性

请重点审查以下维度，给出 Strengths / Weaknesses / Questions / Missing References：

1. **实验设计与统计分析**
   - 180K benchmark 构建是否合理？LoRA fine-tuning 链的 hyperparameter 选择（r=16, α=32）是否充分论证？
   - Random Forest 作为主分类器，与 CORAL / XGBoost 等的比较是否充分？
   - Cross-validation 设计是否有 data leakage 风险？
   - 统计检验（bootstrap CI, p-value）使用是否恰当？多重比较校正是否完整？

2. **Cross-transfer 有效性**
   - Cross-model transfer（66.4%）、cross-strategy（59.1%, d1-d3: 45.9%）、cross-domain（74.1%）的实验设计和结论是否匹配？
   - Cross-strategy d1/d2 boundary inversion 是否被充分分析和解释？
   - Two-stage pipeline 是否是合理的解决方案？

3. **EDD 指标**
   - Effective Discriminable Depth 的定义是否严谨？T=0.70 的阈值选择是否有充分依据？
   - 非单调 AUC 场景下 EDD 的适用性？
   - Contiguous prefix 要求是否过于保守？

4. **Baseline 比较**
   - Binoculars（78.1%）vs 本方法（78.4%）差异不显著，如何定位本方法的附加价值？
   - Perturbation-based baselines（DetectGPT 28.8%, Min-K% Prob 33.2%）是否为公平比较（binary → ordinal 适配）？
   - Zero-shot LLM baselines 的设计是否充分？

5. **Reference Model 自引用问题**
   - Pythia-1.4B 同时作为 reference model 和 generator，Table 中是否充分标注？
   - Self-reference 带来的 4-11pp 优势是否影响 cross-model 比较的公平性？

6. **Cross-scale 实验**
   - 7-8B 和 14B 实验的结论强度是否与证据匹配？
   - 14B EDD=0 但 claim "signal persists" 是否言过其实？
   - Mixed confounders（model family, tokenizer, training data 均不同）是否被充分讨论？

7. **Reproducibility**
   - Cross-seed replication 仅 3/9 cells，是否足够？
   - 单一 LoRA 超参配置是否影响结论普适性？

请以 EMNLP 2026 顶会标准严格审稿。每个 Weakness 标注 **[Must-Fix]** / **[Should-Fix]** / **[Minor]**。最后给出独立评分建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-20T06:27:15.648413+00:00_

called Skill

<details open><summary>🔧 Tool call — Skill</summary>

```json
{
  "skill": "review-reviewer-session-start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Skill",
  "tool_args": {
    "skill": "review-reviewer-session-start"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-20T06:27:15.648762+00:00_

&lt;tool_use_error>Unknown skill: review-reviewer-session-start&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Skill",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-20T06:27:20.036189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-20T06:27:20.036980+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-20T06:27:29.198241+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-20T06:27:29.198831+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-20T06:27:31.966044+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-20T06:27:32.118060+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-20T06:27:34.784129+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-20T06:27:34.834922+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-20T06:27:41.615582+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-20T06:27:41.667269+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-20T06:27:50.383666+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 707 · 2026-05-20T06:27:52.341273+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "project": "recursive_gen_depth_est",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "project": "recursive_gen_depth_est",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 708 · 2026-05-20T06:27:57.011847+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found relevant information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

Reviewers are asked to read the paper and get a first impression, search for related work, and state in the review if they did not check some major parts, such as proofs. Reviewers are provided with a checklist to flag problems that other people may have missed.

If a submission looks very close to the reviewer's own work about to be submitted, it is b
…[truncated 962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6628
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-20T06:27:58.621816+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_
…[truncated 289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6280
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-20T06:28:13.404613+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch,TodoWrite",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch,TodoWrite",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-20T06:28:13.455358+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-20T06:28:23.279277+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '获取 ACL ARR 官方 review form 评分维度', 'status': 'in_progress', 'activeForm': '获取 ACL ARR 官方 review form 评分维度'}, {'content': '通读论文 PDF 全文（正文 + appendix）', 'status': 'pending', 'activeForm': '通读论文 PDF 全文'}, {'content': '深度审查：实验设计与统计分析', 'status': 'pending', 'activeForm': '审查实验设计与统计分析'}, {'content': '深度审查：Cross-transfer 有效性', 'status': 'pending', 'activeForm': '审查 Cross-transfer 有效性'}, {'content': '深度审查：EDD 指标定义', 'status': 'pending', 'activeForm': '审查 EDD 指标定义'}, {'content': '深度审查：Baseline 比较公平性', 'status': 'pending', 'activeForm': '审查 Baseline 比较公平性'}, {'content': '深度审查：Reference Model 自引用问题', 'status': 'pending', 'activeForm': '审查 Reference Model 自引用'}, {'content': '深度审查：Cross-scale 实验', 'status': 'pending', 'activeForm': '审查 Cross-scale 实验'}, {'content': '深度审查：Reproducibility', 'status': 'pending', 'activeForm': '审查 Reproducibility'}, {'content': '引用验证', 'status': 'pending', 'activeForm': '验证引用'}, {'content': '撰写完整审稿意见并汇报', 'status': 'pending', 'activeForm': '撰写审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '获取 ACL ARR 官方 review form 评分维度', 'status': 'in_progress', 'activeForm': '获取 ACL ARR 官方 review form 评分维度'}, {'content': '通读论文 PDF 全文（正文 + appendix）', 'status': 'pending', 'activeForm': '通读论文 PDF 全文'}, {'content': '深度审查：实验设计与统计分析', 'status': 'pending', 'activeForm': '审查实验设计与统计分析'}, {'content': '深度审查：Cross-transfer 有效性', 'status': 'pending', 'activeForm': '审查 Cross-transfer 有效性'}, {'content': '深度审查：EDD 指标定义', 'status': 'pending', 'activeForm': '审查 EDD 指标定义'}, {'content': '深度审查：Baseline 比较公平性', 'status': 'pending', 'activeForm': '审查 Baseline 比较公平性'}, {'content': '深度审查：Reference Model 自引用问题', 'status': 'pending', 'activeForm': '审查 Reference Model 自引用'}, {'content': '深度审查：Cross-scale 实验', 'status': 'pending', 'activeForm': '审查 Cross-scale 实验'}, {'content': '深度审查：Reproducibility', 'status': 'pending', 'activeForm': '审查 Reproducibility'}, {'content': '引用验证', 'status': 'pending', 'activeForm': '验证引用'}, {'content': '撰写完整审稿意见并汇报', 'status': 'pending', 'activeForm': '撰写审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-20T06:28:23.279801+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-20T06:28:24.987127+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions/criteria names, their descriptions, and scoring scales (1-5 or whatever scale is used). List every field a reviewer must fill out."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all dimensions/criteria names, their descriptions, and scoring scales (1-5 or whatever scale is used). List every field a reviewer must fill out."
  }
}
```

</details>

---


### Tool call

_source line 715 · 2026-05-20T06:28:27.349066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 716 · 2026-05-20T06:28:27.952206+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-20T06:28:40.808375+00:00_

# ACL Rolling Review Form - Complete Structure

## Required Review Dimensions

### 1. **Paper Summary**
Description: Summarize the paper's topic to help editors and area chairs understand the work and catch misunderstandings.

### 2. **Summary of Strengths**
Description: Identify major publication reasons, including "novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature."

### 3. **Summary of Weaknesses**
Description: Document concerns about correctness, limited impact, clarity, or other factors favoring alternative papers. Numbered format required for author responses.

### 4. **Comments/Suggestions/Typos**
Description: Provide improvement suggestions beyond addressing main concerns.

### 5. **Reviewer Confidence**
Scale: 1-5
- 5 = Positive evaluation; very careful reading and familiarity with related work
- 4 = Quite sure; important points checked carefully
- 3 = Pretty sure; general area knowledge but limited detail verification
- 2 = Willing to defend evaluation; likely missed details or novelty assessment uncertain
- 1 = Not expert area; educated guess only

### 6. **Soundness**
Scale: 1-5 (with .5 increments: 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)
Evaluates scientific rigor, experimental validity, and adequacy of support for claims.

### 7. **Excitement**
Scale: 1-5 (with .5 increments)
Subjective assessment of innovation potential, community impact, and personal relevance.

### 8. **Overall Assessment**
Scale: 1-5 (with .5 increments)
Recommendation categories: Award consideration, Conference, Findings, Resubmit, or Reject.

### 9. **Best Paper Justification**
Description: Required only if rating is "Consider for Award" or "Borderline Award."

### 10. **Limitations and Societal Impact**
Description: Evaluate authors' discussion of work limitations and positive/negative societal consequences.

### 11. **Ethical Concerns**
Description: Review against "ACL code of ethics" and assess author acknow
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 15821
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-20T06:28:47.207335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-20T06:28:48.068592+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 861
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-20T06:28:48.221246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 721 · 2026-05-20T06:28:48.675447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-20T06:28:49.230966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-20T06:28:49.637697+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-20T06:28:49.638161+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-20T06:28:50.698774+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2023
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-20T06:28:50.699251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-20T06:28:51.052676+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1821
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-20T06:28:51.355601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-20T06:28:51.509706+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1871
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-20T06:28:51.510154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 731 · 2026-05-20T06:28:52.016423+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 732 · 2026-05-20T06:28:52.168056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1468
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-20T06:28:53.177691+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1822
}
```

</details>

---


### Tool result

_source line 734 · 2026-05-20T06:28:53.279349+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1769
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-20T06:28:53.481142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1464
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-20T06:29:15.880168+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '获取 ACL ARR 官方 review form 评分维度', 'status': 'completed', 'activeForm': '获取 ACL ARR 官方 review form 评分维度'}, {'content': '通读论文 PDF 全文（正文 + appendix）', 'status': 'in_progress', 'activeForm': '通读论文 PDF 全文'}, {'content': '深度审查：实验设计与统计分析', 'status': 'pending', 'activeForm': '审查实验设计与统计分析'}, {'content': '深度审查：Cross-transfer 有效性', 'status': 'pending', 'activeForm': '审查 Cross-transfer 有效性'}, {'content': '深度审查：EDD 指标定义', 'status': 'pending', 'activeForm': '审查 EDD 指标定义'}, {'content': '深度审查：Baseline 比较公平性', 'status': 'pending', 'activeForm': '审查 Baseline 比较公平性'}, {'content': '深度审查：Reference Model 自引用问题', 'status': 'pending', 'activeForm': '审查 Reference Model 自引用'}, {'content': '深度审查：Cross-scale 实验', 'status': 'pending', 'activeForm': '审查 Cross-scale 实验'}, {'content': '深度审查：Reproducibility', 'status': 'pending', 'activeForm': '审查 Reproducibility'}, {'content': '引用验证', 'status': 'pending', 'activeForm': '验证引用'}, {'content': '撰写完整审稿意见并汇报', 'status': 'pending', 'activeForm': '撰写审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '获取 ACL ARR 官方 review form 评分维度', 'status': 'completed', 'activeForm': '获取 ACL ARR 官方 review form 评分维度'}, {'content': '通读论文 PDF 全文（正文 + appendix）', 'status': 'in_progress', 'activeForm': '通读论文 PDF 全文'}, {'content': '深度审查：实验设计与统计分析', 'status': 'pending', 'activeForm': '审查实验设计与统计分析'}, {'content': '深度审查：Cross-transfer 有效性', 'status': 'pending', 'activeForm': '审查 Cross-transfer 有效性'}, {'content': '深度审查：EDD 指标定义', 'status': 'pending', 'activeForm': '审查 EDD 指标定义'}, {'content': '深度审查：Baseline 比较公平性', 'status': 'pending', 'activeForm': '审查 Baseline 比较公平性'}, {'content': '深度审查：Reference Model 自引用问题', 'status': 'pending', 'activeForm': '审查 Reference Model 自引用'}, {'content': '深度审查：Cross-scale 实验', 'status': 'pending', 'activeForm': '审查 Cross-scale 实验'}, {'content': '深度审查：Reproducibility', 'status': 'pending', 'activeForm': '审查 Reproducibility'}, {'content': '引用验证', 'status': 'pending', 'activeForm': '验证引用'}, {'content': '撰写完整审稿意见并汇报', 'status': 'pending', 'activeForm': '撰写审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-20T06:29:15.880623+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-20T06:29:18.178178+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "project": "recursive_gen_depth_est",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "project": "recursive_gen_depth_est",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 739 · 2026-05-20T06:29:18.579532+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 740 · 2026-05-20T06:29:19.432557+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 587.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 576.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 450.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.8}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.5}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 475.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.8}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper
…[truncated 307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1254
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-20T06:31:40.079516+00:00_

&lt;persisted-output>
Output too large (53.5KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/7e2550a3-60a5-4171-8040-cdc6d111e28f/tool-results/toolu_01EmKBpA9m8fpDMNXckNSMfD.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 68, \"total_citations\": 107, \"unique_cited_keys\": 68, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 57, \"online_not_found\": 7, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina
…[truncated 364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 141499
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-20T06:31:45.903963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/7e2550a3-60a5-4171-8040-cdc6d111e28f/tool-results/toolu_01EmKBpA9m8fpDMNXckNSMfD.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/7e2550a3-60a5-4171-8040-cdc6d111e28f/tool-results/toolu_01EmKBpA9m8fpDMNXckNSMfD.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-20T06:31:46.408089+00:00_

1	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 68, \"total_citations\": 107, \"unique_cited_keys\": 68, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 57, \"online_not_found\": 7, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"type\": \"misc\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, M
…[truncated 52809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-20T06:31:46.408552+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-20T06:31:47.362518+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-20T06:31:47.362949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-20T06:31:47.871340+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-20T06:31:47.871687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-20T06:31:48.323755+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-20T06:31:48.324171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-20T06:31:48.876701+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-20T06:31:48.927468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-20T06:31:48.978199+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-20T06:31:56.002348+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/_pdf_images/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/_pdf_images/*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-20T06:31:56.053068+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-20T06:32:00.738522+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-20T06:32:00.789109+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-20T06:32:03.953555+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 759 · 2026-05-20T06:32:04.305540+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 760 · 2026-05-20T06:32:04.759143+00:00_

1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
43	Concretely, the d0$\t
…[truncated 63837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-20T06:32:04.759587+00:00_

1	\section{Method}
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
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 6151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-20T06:32:04.759811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-20T06:32:05.212008+00:00_

1	\subsection{Theoretical Grounding}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed by its dominance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--80\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), so EDD should decrease with scale.
15	Qwen2.5-14B confirms this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B), while d1--d3 AUCs remain above 0.70 (\S\ref{sec:gen:crossscale}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$(d{+}1)$ text in tail statistics.
20	GPT-2~XL confirms this: temperature d1 median \texttt{p90\_ppl} (92.
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-20T06:32:05.212522+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-20T06:32:06.166942+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}1{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: MAE\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$). $^\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\,pp advantage over cross-model references (Appendix~\ref{app:ref_ablation}).}
22	\label{tab:main_matrix}
23	\resizebox
…[truncated 8856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-20T06:32:06.167352+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-20T06:32:06.268238+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares ordinal depth estimation methods across all 9 atlas cells.
10	RF, XGBoost, and LightGBM on the same 19 features converge within 0.4\,pp per cell (a feature-determined ceiling); on Pythia nucleus, CORAL \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match RF within 0.6\,pp ($p>0.05$).
11	
12	\paragraph{Neural end-to-end baselines.}
13	DeBERTa-v3-base (LoRA) trained end-to-end on raw text underperforms RF by 16--32\,pp across three cells (Table~\ref{tab:baselines}); the gap is largest on GPT-2~XL temp09 (53.1\% vs.\ 85.9\%), where RF signal is strongest.
14	Depth-2 recall collapses to 8.4\% under DeBERTa, indicating that intermediate-depth distributional shifts---captured by perplexity tail statistics---are invisible to token-level neural encoders without explicit feature engineering.
15	RoBERTa-DCOL (ordinal contrastive; 64.5\%) narrows the gap but remains 14\,pp below RF.
16	
17	\paragraph{Binary detectors and membership inference.}
18	Perturbation-based (DetectGPT, 28.8\%) and membership-inference (Min-K\% Prob, 33.2\%) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); CORAL calibration does not close the gap (d1--d3: 40.4\% vs.\ RF 71.6\%).
19	Binoculars \cite{binoculars2024}, calibrated with an 11-feature RF on per-token cross-perplexity scores, matches our pipeline within 0.3\,pp (78.1\% vs.\ 78.4\%, $p{>}0.05$); 6 of 11 Binoculars features overlap with 6 of our 19 (both capture mean-level perplexity displacement), and merging all 30 features yields 82.6\% (+4.2\,pp; Appendix~\ref{app:feature_ablation_bino}).
20	
21	\paragraph{
…[truncated 5787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-20T06:32:06.268736+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-20T06:32:06.319379+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	This paper formalizes recursive generation depth estimation as ordinal classification under controlled full-replacement chains.
5	The perplexity tail feature family dominates depth discrimination across all nine cells, with $\mathrm{EDD}_{0.70}{=}4$ for all three families; cross-model transfer reaches 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, while perturbation-based and membership-inference detectors achieve only 30--35\%.
6	Under accumulation (GPT-2~XL, nucleus), accuracy drops to ${\sim}$69--70\% ($-$15\,pp, $2.8{\times}$ chance); at 14B (mean 50.8\% across three strategies, $2{\times}$ chance), $\mathrm{EDD}_{0.70}{=}0$ but d1--d3 discrimination persists with strategy-specific AUC patterns (Appendix~\ref{app:cross_scale_full}).
7	
8	\paragraph{Multi-channel depth encoding.}
9	Feature ablation (Appendix~\ref{app:feature_ablation_bino}) decomposes the depth signal into perplexity displacement (6 core features, 75.9\%, 97\% of pipeline accuracy), distributional shape (+2.5\,pp), and cross-model divergence (+4.2\,pp, merged 82.6\%); the gain is strategy-dependent (nucleus/temperature +4.7\,pp vs.\ top-k +3.2\,pp).
10	That two independent pipelines converge to within 0.3\,pp validates depth as a genuine distributional property; at 14B, merging still yields +3.6--3.7\,pp despite a 10$\times$ observer--generator scale gap (Appendix~\ref{app:feature_ablation_bino}).
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-20T06:33:26.361459+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '获取 ACL ARR 官方 review form 评分维度', 'status': 'completed', 'activeForm': '获取 ACL ARR 官方 review form 评分维度'}, {'content': '通读论文 PDF 全文（正文 + appendix）', 'status': 'completed', 'activeForm': '通读论文 PDF 全文'}, {'content': '深度审查全部维度并撰写审稿意见', 'status': 'in_progress', 'activeForm': '深度审查并撰写审稿意见'}, {'content': '引用验证', 'status': 'completed', 'activeForm': '验证引用'}, {'content': '汇报审稿意见给 Director', 'status': 'pending', 'activeForm': '汇报审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '获取 ACL ARR 官方 review form 评分维度', 'status': 'completed', 'activeForm': '获取 ACL ARR 官方 review form 评分维度'}, {'content': '通读论文 PDF 全文（正文 + appendix）', 'status': 'completed', 'activeForm': '通读论文 PDF 全文'}, {'content': '深度审查全部维度并撰写审稿意见', 'status': 'in_progress', 'activeForm': '深度审查并撰写审稿意见'}, {'content': '引用验证', 'status': 'completed', 'activeForm': '验证引用'}, {'content': '汇报审稿意见给 Director', 'status': 'pending', 'activeForm': '汇报审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-20T06:33:26.412286+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-20T06:33:35.307610+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-20T06:33:35.358391+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	All experiments use full-replacement recursive chains, where each depth fully replaces the prior training corpus. Real-world contamination typically involves accumulation, where synthetic and human data co-exist at unknown proportions across iterations \cite{gerstgrasser2024_accumulate}. Under accumulation, depth signal should attenuate because each generation retains human-originated distributional properties. Our results therefore represent an upper bound on feature separability; extending the framework to accumulation settings, where depth becomes a continuous mixing parameter, is a priority for future work.
6	Segment-level estimation in mixed-depth documents remains open (Appendix~\ref{app:mixed_depth}), as our framework assumes uniform depth per passage.
7	
8	\paragraph{Controlled experimental setting.}
9	The primary benchmark uses Wikipedia seed text with controlled LoRA fine-tuning (1--1.5B models), a design that isolates the depth variable but diverges from wild contamination.
10	Domain bias controls confirm depth as the dominant factor: LOGO accuracy (72.1\%) matches standard CV (72.0\%), seed-group prediction is at chance (10.2\%; Appendix~\ref{app:domain_bias}).
11	Cross-scale experiments (7--14B, \S\ref{sec:gen:crossscale}) show signal that attenuates with scale; at 14B, d0/d1 separability nearly vanishes ($\mathrm{EDD}_{0.70}{=}0$) while d1--d3 discrimination persists; this constitutes a boundary condition for the current feature set (confounded by five factors; Appendix~\ref{app:cross_scale_confounds}).
12	
13	\paragraph{Cross-strategy deployment constraint.}
14	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
15	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random 
…[truncated 6238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-20T06:34:33.507389+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '获取 ACL ARR 官方 review form 评分维度', 'status': 'completed', 'activeForm': '获取 ACL ARR 官方 review form 评分维度'}, {'content': '通读论文 PDF 全文（正文 + appendix）', 'status': 'completed', 'activeForm': '通读论文 PDF 全文'}, {'content': '深度审查全部维度并撰写审稿意见', 'status': 'completed', 'activeForm': '深度审查并撰写审稿意见'}, {'content': '引用验证', 'status': 'completed', 'activeForm': '验证引用'}, {'content': '汇报审稿意见给 Director', 'status': 'in_progress', 'activeForm': '汇报审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '获取 ACL ARR 官方 review form 评分维度', 'status': 'completed', 'activeForm': '获取 ACL ARR 官方 review form 评分维度'}, {'content': '通读论文 PDF 全文（正文 + appendix）', 'status': 'completed', 'activeForm': '通读论文 PDF 全文'}, {'content': '深度审查全部维度并撰写审稿意见', 'status': 'completed', 'activeForm': '深度审查并撰写审稿意见'}, {'content': '引用验证', 'status': 'completed', 'activeForm': '验证引用'}, {'content': '汇报审稿意见给 Director', 'status': 'in_progress', 'activeForm': '汇报审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-20T06:34:33.558132+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 776 · 2026-05-20T06:37:07.063201+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 方法严谨性审查（Round 1）\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 问题定义新颖、benchmark 构建系统，但 headline metrics 被 d0 系统性膨胀、与 Binoculars 无显著差异、cross-transfer 实用性不足、14B 实验严重混淆，作为主会议论文方法严谨性未达标，作为 Findings 论文贡献足够。\n\n---\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心 in-distribution 实验严谨；cross-transfer 和 cross-scale 的 claim 超出证据支撑；自引用混淆未充分隔离 |\n| Excitement | 3.5/5 | 问题本身新颖有价值（递归生成深度估计是新方向）；EDD 指标有概念贡献；但方法简单（RF + 手工特征），增量性较强 |\n| Reproducibility | 4.0/5 | 超参详尽（Appendix A），代码承诺开源；但 cross-seed 仅覆盖 3/9 cells，单一 LoRA 配置 |\n| Overall Assessment | 3.0 | Findings 水平——贡献真实但主会议接收需解决 d0 膨胀表述、baseline 差距不显著、cross-scale 混淆等关键问题 |\n| Confidence | 4/5 | 仔细阅读了全文和全部 25 页附录，核验了统计检验和引用 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Headline metrics 被 d0 召回率系统性膨胀，误导读者对方法实用性的判断\n- 具体位置：Abstract（\"accuracy of 59–82%\"）, Section 4.1 Table 2, Section 5.2 Table 5（\"66.4%\"）, Section 6\n- 问题：d0（human-written）召回率 >97%（Table 2 脚注），four-class accuracy 被 d0 严重拉高。Cross-model transfer 的 66.4% 中 d0 贡献巨大，d1-d3 balanced accuracy 仅 55.4%（1.66× chance）。Pythia holdout d2 recall 仅 26.8%（Table 5）。Abstract 和 Introduction 始终以 four-class accuracy 作为主指标，d1-d3 balanced accuracy 虽有报告但始终处于括号内或脚注位置。这在实际应用中会误导用户：一个能以 97% 识别人类文本但只有 26.8% 识别 d2 的系统，其实用价值与 \"66.4% accuracy\" 给人的印象截然不同。\n- 为什么影响接收：ACL ARR soundness 要求 claims 与 evidence 匹配。当前表述方式让读者高估了方法在真正困难（d1-d3 discriminability）场景下的能力。\n- 建议修改方向：(1) Abstract 和 Introduction 同时并列报告 four-class accuracy 和 d1-d3 balanced accuracy；(2) 在 Section 6 Discussion 中明确承认 d0 膨胀效应并量化其影响；(3) 考虑以 d1-d3 balanced accuracy 作为主指标。\n\n**N2** [critical] 与 Binoculars baseline 无显著差异（78.4% vs 78.1%, p>0.05），论文未充分定位自身方法的附加价值\n- 具体位置：Section 5.1 Table 4, Section 5.1 正文第 3 段, Appendix B.17 Table B.17\n- 问题：论文 19-feature RF（78.4%）与 Binoculars 11-feature RF calibration（78.1%）在 9-cell mean 上无统计显著差异。Table 4 中 Binoculars 行列出的是 threshold（69.8%）和 RF (1 feat)（63.7%）两个较弱配置，78.1% 的完整 11-feature 配置仅在正文中一句话提及。这种呈现方式不透明。Merged 30-feature 达到 82.6%（+4.2pp），说明两个管线的信号部分互补——但互补性本身暗示 19-feature pipeline 并未完全覆盖 Binoculars 的信号，反之亦然。\n- 为什么影响接收：如果一个已有方法（Binoculars + RF calibration）已经达到相同性能，那么本文的方法论贡献（19-feature pipeline）需要通过其他维度（如 interpretability、deployment cost、无需 performer model）来论证，而非仅以 accuracy 定位。\n- 建议修改方向：(1) Table 4 中加入 Binoculars 11-feat RF 行并标注 p-value；(2) 明确论证本文管线相对 Binoculars 的优势（如单一 reference model 即可、无需 observer-performer pair、特征可解释性、merged system 的增益来源）；(3) 将 merged 82.6% 作为推荐配置而非附录内容。\n\n**N3** [critical] 14B 实验严重混淆，\"signal persists\" claim 言过其实\n- 具体位置：Section 5.4, Section 6 第 1 段, Appendix B.12 Table B.6 及 §Confounds\n- 问题：14B 实验（Qwen2.5-14B, mean 50.8%, EDD=0）同时改变了 5 个变量：(a) model family（Qwen vs Pythia/OLMo/GPT-2）, (b) tokenizer, (c) training data, (d) reference model（self-reference vs cross-reference Pythia-1.4B）, (e) model scale（14B vs 1-1.5B）。Appendix B.12 §Confounds 承认 \"it is therefore infeasible to attribute the observed accuracy gap to any single factor\"，但 Section 5.4 和 Section 6 仍声称 \"signal persists at 14B\"。当 EDD=0（no adjacent-depth pair exceeds T=0.70）时，声称 \"d1-d3 discrimination persists\" 与 EDD 指标的定义矛盾——EDD 正是为了衡量这种 discrimination，而它报告为 0。50.8% 仅为 2× chance，在高方差小样本下可能不稳定。\n- 为什么影响接收：这是 overclaiming。作者自己的 EDD 指标说 0，但结论说 \"persists\"，这是内部不一致。多重混淆使得无法将 50.8% 归因于 depth signal vs 其他因素。\n- 建议修改方向：(1) 将 Section 5.4 标题从 \"Preliminary Cross-Scale Observations\" 改为更明确的 caveat（如 \"Inconclusive Cross-Scale Observations\"）；(2) Section 6 中不应使用 \"persists\"，改为 \"above-chance accuracy is observed but cannot be attributed to depth signal due to multiple confounds\"；(3) 在 14B 实验中加入 Qwen2.5-14B 的 Pythia-referenced pipeline（而非 self-reference）以隔离 reference model 混淆。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Should-Fix] Self-reference 混淆使 3×3 atlas 内部不可比\n- 具体位置：Section 3.2 §Reference model, Table 2（†标注）, Appendix B.11 Table B.11\n- 问题：Pythia-1.4B 同时作为 reference model 和 generator，self-reference 优势 4-11pp（Table B.11: self 78.6% vs cross-OLMo 74.5% vs cross-GPT2 67.3%）。这意味着 Table 2 中 Pythia 的 78.7% 可能在 cross-reference 下降至 ~68-75%，与 OLMo 和 GPT-2 XL 的表观优势关系反转。虽然论文用 † 标注并在 Limitations 中讨论，但 atlas 分析（Section 4）中的所有 cross-cell 比较（如 \"GPT-2 XL achieves the highest accuracy under every strategy\"）均基于这个不公平基础。\n- 建议：在 Table 2 中增加一列 cross-reference accuracy（OLMo-1B 或 GPT-2 XL 作为 reference），使 atlas 内部比较基于相同条件。或者至少在 Section 4.1 的 axis effect 分析中明确说明 Pythia 行的可比性受限。\n\n**W2** [Should-Fix] Cross-strategy transfer d1-d3 仅 45.9%（1.38× chance），实用性存疑\n- 具体位置：Section 5.3 Table 6, Appendix B.23 §Cross-strategy conditional decomposition\n- 问题：d1-d3 balanced accuracy 45.9%（chance 33.3%）意味着在 decoding strategy 未知时，系统对 generated text 的深度估计几乎没有实用价值。d1/d2 boundary inversion（AUC<0.5）意味着系统在某些 strategy 下会系统性地反转深度判断。Two-stage pipeline 回收 11.5pp，但前提是 strategy space 已知且 strategy classifier 准确——论文未报告 strategy classifier 本身的准确率。\n- 建议：(1) 报告 two-stage pipeline 中 strategy classifier 的独立准确率；(2) 在 Section 6 中明确将 \"decoding strategy must be known or identifiable\" 列为部署前提条件，而非仅在 Limitations 中提及。\n\n**W3** [Should-Fix] 单一 LoRA 超参配置（r=16, α=32）无 sensitivity analysis\n- 具体位置：Section 3.2 §Generation pipeline, Appendix A Table A.1\n- 问题：所有 180K 样本和全部实验使用相同 LoRA 配置。不同 LoRA rank（r=4, 8, 32, 64）和 learning rate 可能产生不同的 distributional shift patterns。如果 depth signal 部分来源于特定 LoRA rank 的 underfitting/overfitting 特征（r=16 可能比 full fine-tuning 产生更大的 distributional gap），那么结论的普适性受限。论文在 Limitations 中承认 \"single LoRA instance\" 但未提供任何 sensitivity analysis。\n- 建议：至少在一个 model-strategy cell 上提供 r∈{4, 8, 16, 32} 的 sensitivity analysis，或与 full fine-tuning 对比一个 cell 的深度估计准确率。\n\n**W4** [Should-Fix] Cross-seed replication 不充分（3/9 cells），OLMo +3.17pp 非重叠 CI 表明 benchmark 不稳定\n- 具体位置：Appendix B.16 Table B.9\n- 问题：仅 Pythia/OLMo/GPT-2 XL 的 nucleus cell 有 2-seed replication（3/9 cells）。OLMo seed=42 78.94% → seed=43 82.11%（+3.17pp），CI 不重叠。这意味着 Table 2 中的 OLMo nucleus accuracy 有 ~3pp 不确定性。温度和 top-k cells 完全未复制。更严重的是，feature rankings 的 seed stability 虽被声称 \"identical top-3\"，但未报告跨 seed 的 importance 值变化幅度。\n- 建议：(1) 在所有 9 cells 上提供 cross-seed replication；(2) 报告 importance 值的 seed-wise 标准差。\n\n**W5** [Should-Fix] EDD T=0.70 阈值选择缺乏充分依据\n- 具体位置：Section 3.4, Section 4.3\n- 问题：T=0.70 被选为 primary threshold，理由是 \"corresponding to adequate discrimination in ROC analysis (8/9 cells achieve EDD ≥ 3)\"。这是循环论证——选择一个让大多数 cells 看起来好的阈值。T=0.75 时只有 7/9 cells 达到 EDD≥3，T=0.80 时只有 5/9。论文确实报告了 sensitivity analysis（Section 4.3），但 T=0.70 的 \"primary\" 地位未基于外部标准（如 classification error rate bound, information-theoretic argument）论证。\n- 建议：(1) 提供 T 选择的 principled justification（如与 downstream task performance 的关联，或与 classification error rate 的对应关系）；(2) 如无法提供，则在正文中将 T=0.70 定位为 \"illustrative\" 而非 \"primary\"。\n\n**W6** [Should-Fix] Perturbation-based baselines 从 binary → ordinal 的适配不充分\n- 具体位置：Section 5.1 Table 4, Appendix B.19\n- 问题：DetectGPT（28.8%）和 Min-K% Prob（33.2%）是二分类方法，被改造为序数分类 baselines。DetectGPT 使用 \"best-of-3\" calibration，Min-K% 使用 CORAL calibration。但这些方法从未被设计用于序数深度估计——它们的 score 空间（perturbation discrepancy, token-level log-probability）不一定具有序数结构。28-33% 的性能接近 chance（25%），这可能反映适配方法的局限而非方法本身的局限。Appendix B.19 中 augmented feature set（19 + Min-K%）提升 +0.48pp 并 Min-K% 排名 #3，说明 Min-K% 确实携带互补信号——当配合合适的特征工程时可以工作。\n- 建议：(1) 在 Table 4 中注明 \"adapted from binary detection; comparison reflects ordinal adaptation rather than original method\"；(2) 加入 min-K% 和 DetectGPT 的 binary d0-vs-d1+ 性能作为 sanity check。\n\n**W7** [Should-Fix] Curation PoC（Appendix B.10）主结论非显著（p>0.4），存在多重比较问题\n- 具体位置：Appendix B.10 Tables B.7 & B.8, Appendix B.23\n- 问题：RF-filtered vs unfiltered（p=0.407）——主假设不成立。RF-vs-random 的 3 个 pairwise comparison（p<0.02 before Bonferroni）在 Bonferroni 校正后仅 1/3 存活（p<0.003 vs threshold 0.017）。论文在 Appendix B.23 中部分承认（\"1 of 3 comparisons surviving\"），但 Appendix B.10 的呈现未充分强调非显著的主结论。\n- 建议：(1) 将 Appendix B.10 标题改为 \"Curation PoC (Inconclusive)\"；(2) 在正文中提及 curation 时使用 \"inconclusive\" 而非暗示有效。\n\n---\n\n## 小问题（不影响接收）\n\n- **[Minor]** Table 4 中 Binoculars 的 calibration 列写 \"threshold\" 和 \"RF (1 feat)\"，但 78.1% 的 11-feat RF 配置未出现在 table 中。建议补充。\n- **[Minor]** 引用验证：7 条在 OpenAlex 未找到（knowledge_collapse2025, falahati2026_curated, mitchell2023_detectgpt 等），多为 2025-2026 新论文或索引问题，非虚构。4 条有年份/first-author 微小 mismatch（he2021_deberta_v3 bib 标 2023 vs 实际 2021; alemohammad2024_mad first author mismatch）。建议修正 bib 年份。\n- **[Minor]** Appendix B.12 中 7-8B 实验使用 4-bit NF4 QLoRA（与 1-1.5B 的 bf16 LoRA 不同），这一差异在 Table B.6 中未标注。\n- **[Minor]** Section 5.1: \"Single-feature regression on mean perplexity performs at chance (25.1%)\" — 但 Table B.20 显示 p90_ppl alone 达到 58.3%。Mean perplexity 是最弱的 perplexity 特征，以它代表 \"surface-text ablation\" 可能低估了简单 baselines。\n- **[Minor]** Cross-boundary generalization（Appendix B.15）：heterogeneous chain 的 confound（architecture identity ≡ depth）虽有 reverse-chain control，但 reverse chain 也只是将另一组 architecture 映射到 depth，无法完全排除 architecture fingerprint 的贡献。\n\n---\n\n## 主要优势\n\n1. **问题定义新颖且有价值**：将递归生成深度估计形式化为序数分类问题，区别于现有的 binary human/machine detection，具有理论清晰性和实际意义。在 model collapse 文献中这是一个被忽视的逆问题。\n\n2. **Benchmark 设计系统**：180K 样本覆盖 3 model families × 3 decoding strategies × 4 depths 的完整网格，控制变量严格（固定 LoRA 配置、固定 reference model、固定 seed text）。Domain bias analysis（Appendix B.8, Sub-A/B/C）包括 bug 修复透明披露，体现了实验诚信。\n\n3. **EDD 指标有概念贡献**：将聚合准确率分解为逐深度边界的可判别性，提供了比单一准确率更有信息量的评估框架。虽然具体实现（contiguous prefix + fixed threshold）有改进空间，但概念方向正确。\n\n4. **Feature analysis 深入且一致**：三种 importance measures（Gini, SHAP, permutation）的高一致性（Kendall's W=0.90, p<0.005），perplexity tail 特征在 9/9 cells 中的统治性，以及理论 grounding（tail erosion → decreasing p90_ppl）形成了完整的叙事。\n\n5. **Limitations 异常全面**：论文用整整一页讨论了 10+ 个 limitations，包括 d0 inflation、FPR、self-reference confound、cross-strategy constraint 等。多数问题是作者自己识别并讨论的。这在 submission 中较为少见。\n\n6. **Appendix 丰富**（15页附录，含 23 个子实验）：包括 domain bias 修正、calibration、feature overlap、end-to-end comparison、depth-4/5 extension、prompted generation、instruction-tuned model、cross-boundary chain 等。\n\n---\n\n## Missing References / Related Work\n\n- **Recursive text generation detection**: 论文未引用 EditLens 之外的 partial-generation / mixed-origin detection 方法。虽然 depth estimation 是更窄的问题定义，但 sentence-level attribution 方法（如 SeqXGPT）与论文的 passage-level 假设形成对比，值得讨论。\n- **Ordinal classification baselines**: 论文在 Appendix B.19 中比较了 CORAL、Frank & Hall、Rennie & Srebro 等 ordinal methods，但主文 Table 4 仅列 RF。建议在 Table 4 中加入 XGBoost（67.2%）和 Ordinal MLP（66.7%）的 cross-model transfer 结果以完整呈现 classifier 比较。\n\n---\n\n## Reviewer Confidence\n4/5: 仔细阅读了 10 页正文 + 15 页附录的全部内容，核验了 EDD 定义的数学一致性、Table 2/4/5/6 的数值与 appendix 的对应关系、statistical tests 的使用（bootstrap CI, Wilson CI, paired t-test, Bonferroni correction）、以及 68 条引用的在线验证。对 model collapse 理论和 AI text detection 文献有一般性了解，但非该子领域核心研究者。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 方法严谨性审查（Round 1）\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 问题定义新颖、benchmark 构建系统，但 headline metrics 被 d0 系统性膨胀、与 Binoculars 无显著差异、cross-transfer 实用性不足、14B 实验严重混淆，作为主会议论文方法严谨性未达标，作为 Findings 论文贡献足够。\n\n---\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心 in-distribution 实验严谨；cross-transfer 和 cross-scale 的 claim 超出证据支撑；自引用混淆未充分隔离 |\n| Excitement | 3.5/5 | 问题本身新颖有价值（递归生成深度估计是新方向）；EDD 指标有概念贡献；但方法简单（RF + 手工特征），增量性较强 |\n| Reproducibility | 4.0/5 | 超参详尽（Appendix A），代码承诺开源；但 cross-seed 仅覆盖 3/9 cells，单一 LoRA 配置 |\n| Overall Assessment | 3.0 | Findings 水平——贡献真实但主会议接收需解决 d0 膨胀表述、baseline 差距不显著、cross-scale 混淆等关键问题 |\n| Confidence | 4/5 | 仔细阅读了全文和全部 25 页附录，核验了统计检验和引用 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Headline metrics 被 d0 召回率系统性膨胀，误导读者对方法实用性的判断\n- 具体位置：Abstract（\"accuracy of 59–82%\"）, Section 4.1 Table 2, Section 5.2 Table 5（\"66.4%\"）, Section 6\n- 问题：d0（human-written）召回率 >97%（Table 2 脚注），four-class accuracy 被 d0 严重拉高。Cross-model transfer 的 66.4% 中 d0 贡献巨大，d1-d3 balanced accuracy 仅 55.4%（1.66× chance）。Pythia holdout d2 recall 仅 26.8%（Table 5）。Abstract 和 Introduction 始终以 four-class accuracy 作为主指标，d1-d3 balanced accuracy 虽有报告但始终处于括号内或脚注位置。这在实际应用中会误导用户：一个能以 97% 识别人类文本但只有 26.8% 识别 d2 的系统，其实用价值与 \"66.4% accuracy\" 给人的印象截然不同。\n- 为什么影响接收：ACL ARR soundness 要求 claims 与 evidence 匹配。当前表述方式让读者高估了方法在真正困难（d1-d3 discriminability）场景下的能力。\n- 建议修改方向：(1) Abstract 和 Introduction 同时并列报告 four-class accuracy 和 d1-d3 balanced accuracy；(2) 在 Section 6 Discussion 中明确承认 d0 膨胀效应并量化其影响；(3) 考虑以 d1-d3 balanced accuracy 作为主指标。\n\n**N2** [critical] 与 Binoculars baseline 无显著差异（78.4% vs 78.1%, p>0.05），论文未充分定位自身方法的附加价值\n- 具体位置：Section 5.1 Table 4, Section 5.1 正文第 3 段, Appendix B.17 Table B.17\n- 问题：论文 19-feature RF（78.4%）与 Binoculars 11-feature RF calibration（78.1%）在 9-cell mean 上无统计显著差异。Table 4 中 Binoculars 行列出的是 threshold（69.8%）和 RF (1 feat)（63.7%）两个较弱配置，78.1% 的完整 11-feature 配置仅在正文中一句话提及。这种呈现方式不透明。Merged 30-feature 达到 82.6%（+4.2pp），说明两个管线的信号部分互补——但互补性本身暗示 19-feature pipeline 并未完全覆盖 Binoculars 的信号，反之亦然。\n- 为什么影响接收：如果一个已有方法（Binoculars + RF calibration）已经达到相同性能，那么本文的方法论贡献（19-feature pipeline）需要通过其他维度（如 interpretability、deployment cost、无需 performer model）来论证，而非仅以 accuracy 定位。\n- 建议修改方向：(1) Table 4 中加入 Binoculars 11-feat RF 行并标注 p-value；(2) 明确论证本文管线相对 Binoculars 的优势（如单一 reference model 即可、无需 observer-performer pair、特征可解释性、merged system 的增益来源）；(3) 将 merged 82.6% 作为推荐配置而非附录内容。\n\n**N3** [critical] 14B 实验严重混淆，\"signal persists\" claim 言过其实\n- 具体位置：Section 5.4, Section 6 第 1 段, Appendix B.12 Table B.6 及 §Confounds\n- 问题：14B 实验（Qwen2.5-14B, mean 50.8%, EDD=0）同时改变了 5 个变量：(a) model family（Qwen vs Pythia/OLMo/GPT-2）, (b) tokenizer, (c) training data, (d) reference model（self-reference vs cross-reference Pythia-1.4B）, (e) model scale（14B vs 1-1.5B）。Appendix B.12 §Confounds 承认 \"it is therefore infeasible to attribute the observed accuracy gap to any single factor\"，但 Section 5.4 和 Section 6 仍声称 \"signal persists at 14B\"。当 EDD=0（no adjacent-depth pair exceeds T=0.70）时，声称 \"d1-d3 discrimination persists\" 与 EDD 指标的定义矛盾——EDD 正是为了衡量这种 discrimination，而它报告为 0。50.8% 仅为 2× chance，在高方差小样本下可能不稳定。\n- 为什么影响接收：这是 overclaiming。作者自己的 EDD 指标说 0，但结论说 \"persists\"，这是内部不一致。多重混淆使得无法将 50.8% 归因于 depth signal vs 其他因素。\n- 建议修改方向：(1) 将 Section 5.4 标题从 \"Preliminary Cross-Scale Observations\" 改为更明确的 caveat（如 \"Inconclusive Cross-Scale Observations\"）；(2) Section 6 中不应使用 \"persists\"，改为 \"above-chance accuracy is observed but cannot be attributed to depth signal due to multiple confounds\"；(3) 在 14B 实验中加入 Qwen2.5-14B 的 Pythia-referenced pipeline（而非 self-reference）以隔离 reference model 混淆。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Should-Fix] Self-reference 混淆使 3×3 atlas 内部不可比\n- 具体位置：Section 3.2 §Reference model, Table 2（†标注）, Appendix B.11 Table B.11\n- 问题：Pythia-1.4B 同时作为 reference model 和 generator，self-reference 优势 4-11pp（Table B.11: self 78.6% vs cross-OLMo 74.5% vs cross-GPT2 67.3%）。这意味着 Table 2 中 Pythia 的 78.7% 可能在 cross-reference 下降至 ~68-75%，与 OLMo 和 GPT-2 XL 的表观优势关系反转。虽然论文用 † 标注并在 Limitations 中讨论，但 atlas 分析（Section 4）中的所有 cross-cell 比较（如 \"GPT-2 XL achieves the highest accuracy under every strategy\"）均基于这个不公平基础。\n- 建议：在 Table 2 中增加一列 cross-reference accuracy（OLMo-1B 或 GPT-2 XL 作为 reference），使 atlas 内部比较基于相同条件。或者至少在 Section 4.1 的 axis effect 分析中明确说明 Pythia 行的可比性受限。\n\n**W2** [Should-Fix] Cross-strategy transfer d1-d3 仅 45.9%（1.38× chance），实用性存疑\n- 具体位置：Section 5.3 Table 6, Appendix B.23 §Cross-strategy conditional decomposition\n- 问题：d1-d3 balanced accuracy 45.9%（chance 33.3%）意味着在 decoding strategy 未知时，系统对 generated text 的深度估计几乎没有实用价值。d1/d2 boundary inversion（AUC<0.5）意味着系统在某些 strategy 下会系统性地反转深度判断。Two-stage pipeline 回收 11.5pp，但前提是 strategy space 已知且 strategy classifier 准确——论文未报告 strategy classifier 本身的准确率。\n- 建议：(1) 报告 two-stage pipeline 中 strategy classifier 的独立准确率；(2) 在 Section 6 中明确将 \"decoding strategy must be known or identifiable\" 列为部署前提条件，而非仅在 Limitations 中提及。\n\n**W3** [Should-Fix] 单一 LoRA 超参配置（r=16, α=32）无 sensitivity analysis\n- 具体位置：Section 3.2 §Generation pipeline, Appendix A Table A.1\n- 问题：所有 180K 样本和全部实验使用相同 LoRA 配置。不同 LoRA rank（r=4, 8, 32, 64）和 learning rate 可能产生不同的 distributional shift patterns。如果 depth signal 部分来源于特定 LoRA rank 的 underfitting/overfitting 特征（r=16 可能比 full fine-tuning 产生更大的 distributional gap），那么结论的普适性受限。论文在 Limitations 中承认 \"single LoRA instance\" 但未提供任何 sensitivity analysis。\n- 建议：至少在一个 model-strategy cell 上提供 r∈{4, 8, 16, 32} 的 sensitivity analysis，或与 full fine-tuning 对比一个 cell 的深度估计准确率。\n\n**W4** [Should-Fix] Cross-seed replication 不充分（3/9 cells），OLMo +3.17pp 非重叠 CI 表明 benchmark 不稳定\n- 具体位置：Appendix B.16 Table B.9\n- 问题：仅 Pythia/OLMo/GPT-2 XL 的 nucleus cell 有 2-seed replication（3/9 cells）。OLMo seed=42 78.94% → seed=43 82.11%（+3.17pp），CI 不重叠。这意味着 Table 2 中的 OLMo nucleus accuracy 有 ~3pp 不确定性。温度和 top-k cells 完全未复制。更严重的是，feature rankings 的 seed stability 虽被声称 \"identical top-3\"，但未报告跨 seed 的 importance 值变化幅度。\n- 建议：(1) 在所有 9 cells 上提供 cross-seed replication；(2) 报告 importance 值的 seed-wise 标准差。\n\n**W5** [Should-Fix] EDD T=0.70 阈值选择缺乏充分依据\n- 具体位置：Section 3.4, Section 4.3\n- 问题：T=0.70 被选为 primary threshold，理由是 \"corresponding to adequate discrimination in ROC analysis (8/9 cells achieve EDD ≥ 3)\"。这是循环论证——选择一个让大多数 cells 看起来好的阈值。T=0.75 时只有 7/9 cells 达到 EDD≥3，T=0.80 时只有 5/9。论文确实报告了 sensitivity analysis（Section 4.3），但 T=0.70 的 \"primary\" 地位未基于外部标准（如 classification error rate bound, information-theoretic argument）论证。\n- 建议：(1) 提供 T 选择的 principled justification（如与 downstream task performance 的关联，或与 classification error rate 的对应关系）；(2) 如无法提供，则在正文中将 T=0.70 定位为 \"illustrative\" 而非 \"primary\"。\n\n**W6** [Should-Fix] Perturbation-based baselines 从 binary → ordinal 的适配不充分\n- 具体位置：Section 5.1 Table 4, Appendix B.19\n- 问题：DetectGPT（28.8%）和 Min-K% Prob（33.2%）是二分类方法，被改造为序数分类 baselines。DetectGPT 使用 \"best-of-3\" calibration，Min-K% 使用 CORAL calibration。但这些方法从未被设计用于序数深度估计——它们的 score 空间（perturbation discrepancy, token-level log-probability）不一定具有序数结构。28-33% 的性能接近 chance（25%），这可能反映适配方法的局限而非方法本身的局限。Appendix B.19 中 augmented feature set（19 + Min-K%）提升 +0.48pp 并 Min-K% 排名 #3，说明 Min-K% 确实携带互补信号——当配合合适的特征工程时可以工作。\n- 建议：(1) 在 Table 4 中注明 \"adapted from binary detection; comparison reflects ordinal adaptation rather than original method\"；(2) 加入 min-K% 和 DetectGPT 的 binary d0-vs-d1+ 性能作为 sanity check。\n\n**W7** [Should-Fix] Curation PoC（Appendix B.10）主结论非显著（p>0.4），存在多重比较问题\n- 具体位置：Appendix B.10 Tables B.7 & B.8, Appendix B.23\n- 问题：RF-filtered vs unfiltered（p=0.407）——主假设不成立。RF-vs-random 的 3 个 pairwise comparison（p<0.02 before Bonferroni）在 Bonferroni 校正后仅 1/3 存活（p<0.003 vs threshold 0.017）。论文在 Appendix B.23 中部分承认（\"1 of 3 comparisons surviving\"），但 Appendix B.10 的呈现未充分强调非显著的主结论。\n- 建议：(1) 将 Appendix B.10 标题改为 \"Curation PoC (Inconclusive)\"；(2) 在正文中提及 curation 时使用 \"inconclusive\" 而非暗示有效。\n\n---\n\n## 小问题（不影响接收）\n\n- **[Minor]** Table 4 中 Binoculars 的 calibration 列写 \"threshold\" 和 \"RF (1 feat)\"，但 78.1% 的 11-feat RF 配置未出现在 table 中。建议补充。\n- **[Minor]** 引用验证：7 条在 OpenAlex 未找到（knowledge_collapse2025, falahati2026_curated, mitchell2023_detectgpt 等），多为 2025-2026 新论文或索引问题，非虚构。4 条有年份/first-author 微小 mismatch（he2021_deberta_v3 bib 标 2023 vs 实际 2021; alemohammad2024_mad first author mismatch）。建议修正 bib 年份。\n- **[Minor]** Appendix B.12 中 7-8B 实验使用 4-bit NF4 QLoRA（与 1-1.5B 的 bf16 LoRA 不同），这一差异在 Table B.6 中未标注。\n- **[Minor]** Section 5.1: \"Single-feature regression on mean perplexity performs at chance (25.1%)\" — 但 Table B.20 显示 p90_ppl alone 达到 58.3%。Mean perplexity 是最弱的 perplexity 特征，以它代表 \"surface-text ablation\" 可能低估了简单 baselines。\n- **[Minor]** Cross-boundary generalization（Appendix B.15）：heterogeneous chain 的 confound（architecture identity ≡ depth）虽有 reverse-chain control，但 reverse chain 也只是将另一组 architecture 映射到 depth，无法完全排除 architecture fingerprint 的贡献。\n\n---\n\n## 主要优势\n\n1. **问题定义新颖且有价值**：将递归生成深度估计形式化为序数分类问题，区别于现有的 binary human/machine detection，具有理论清晰性和实际意义。在 model collapse 文献中这是一个被忽视的逆问题。\n\n2. **Benchmark 设计系统**：180K 样本覆盖 3 model families × 3 decoding strategies × 4 depths 的完整网格，控制变量严格（固定 LoRA 配置、固定 reference model、固定 seed text）。Domain bias analysis（Appendix B.8, Sub-A/B/C）包括 bug 修复透明披露，体现了实验诚信。\n\n3. **EDD 指标有概念贡献**：将聚合准确率分解为逐深度边界的可判别性，提供了比单一准确率更有信息量的评估框架。虽然具体实现（contiguous prefix + fixed threshold）有改进空间，但概念方向正确。\n\n4. **Feature analysis 深入且一致**：三种 importance measures（Gini, SHAP, permutation）的高一致性（Kendall's W=0.90, p<0.005），perplexity tail 特征在 9/9 cells 中的统治性，以及理论 grounding（tail erosion → decreasing p90_ppl）形成了完整的叙事。\n\n5. **Limitations 异常全面**：论文用整整一页讨论了 10+ 个 limitations，包括 d0 inflation、FPR、self-reference confound、cross-strategy constraint 等。多数问题是作者自己识别并讨论的。这在 submission 中较为少见。\n\n6. **Appendix 丰富**（15页附录，含 23 个子实验）：包括 domain bias 修正、calibration、feature overlap、end-to-end comparison、depth-4/5 extension、prompted generation、instruction-tuned model、cross-boundary chain 等。\n\n---\n\n## Missing References / Related Work\n\n- **Recursive text generation detection**: 论文未引用 EditLens 之外的 partial-generation / mixed-origin detection 方法。虽然 depth estimation 是更窄的问题定义，但 sentence-level attribution 方法（如 SeqXGPT）与论文的 passage-level 假设形成对比，值得讨论。\n- **Ordinal classification baselines**: 论文在 Appendix B.19 中比较了 CORAL、Frank & Hall、Rennie & Srebro 等 ordinal methods，但主文 Table 4 仅列 RF。建议在 Table 4 中加入 XGBoost（67.2%）和 Ordinal MLP（66.7%）的 cross-model transfer 结果以完整呈现 classifier 比较。\n\n---\n\n## Reviewer Confidence\n4/5: 仔细阅读了 10 页正文 + 15 页附录的全部内容，核验了 EDD 定义的数学一致性、Table 2/4/5/6 的数值与 appendix 的对应关系、statistical tests 的使用（bootstrap CI, Wilson CI, paired t-test, Bonferroni correction）、以及 68 条引用的在线验证。对 model collapse 理论和 AI text detection 文献有一般性了解，但非该子领域核心研究者。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-20T06:37:11.591668+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4528
}
```

</details>

---


### Tool call

_source line 778 · 2026-05-20T06:37:28.913114+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '获取 ACL ARR 官方 review form 评分维度', 'status': 'completed', 'activeForm': '获取 ACL ARR 官方 review form 评分维度'}, {'content': '通读论文 PDF 全文（正文 + appendix）', 'status': 'completed', 'activeForm': '通读论文 PDF 全文'}, {'content': '深度审查全部维度并撰写审稿意见', 'status': 'completed', 'activeForm': '深度审查并撰写审稿意见'}, {'content': '引用验证', 'status': 'completed', 'activeForm': '验证引用'}, {'content': '汇报审稿意见给 Director', 'status': 'completed', 'activeForm': '汇报审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '获取 ACL ARR 官方 review form 评分维度', 'status': 'completed', 'activeForm': '获取 ACL ARR 官方 review form 评分维度'}, {'content': '通读论文 PDF 全文（正文 + appendix）', 'status': 'completed', 'activeForm': '通读论文 PDF 全文'}, {'content': '深度审查全部维度并撰写审稿意见', 'status': 'completed', 'activeForm': '深度审查并撰写审稿意见'}, {'content': '引用验证', 'status': 'completed', 'activeForm': '验证引用'}, {'content': '汇报审稿意见给 Director', 'status': 'completed', 'activeForm': '汇报审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-20T06:37:28.963809+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 780 · 2026-05-20T06:37:43.774125+00:00_

审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.0（Findings），Soundness 3.0/5，Excitement 3.5/5，Reproducibility 4.0/5。

**3 个 Must-Fix 问题**：
1. Headline metrics 被 d0 召回率系统性膨胀（d1-d3 balanced accuracy 才是真正指标，但被 bracket 化处理）
2. 与 Binoculars 11-feat RF 无显著差异（78.4% vs 78.1%, p>0.05），方法附加价值定位不清
3. 14B 实验 5 重混淆下 EDD=0，"signal persists" 与自定义 EDD 指标矛盾

**7 个 Should-Fix 问题**：self-reference 混淆使 atlas 不可比、cross-strategy d1-d3 仅 1.38× chance、单一 LoRA 配置无 sensitivity analysis、cross-seed 仅 3/9 cells、EDD T=0.70 循环论证、perturbation baseline 适配不充分、curation PoC 非显著。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 27

## Round 27

4 recorded events


### User

_source line 781 · 2026-05-20T06:40:08.103445+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2（新颖性与完整性）的完整审稿原文。请逐条回应：
- **[AGREE]**：同意并简要说明理由
- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 — Round 1 审稿报告（新颖性与完整性）

### 总体评分
**Overall**: 3.0 / 5（Findings 级别）
**一句话总结**: 任务定义新颖且实验设计系统，但方法贡献有限（标准 RF + 标准特征），scale generalization 在 14B 时崩塌（EDD=0），full-replacement 假设严重限制生态效度，综合来看达到 Findings 标准但不足以被主会议接收。

### 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论严谨（5-fold CV, 多 seed, bootstrap CI），但 full-replacement 假设与 real-world accumulation 场景差距过大，14B 结果（EDD=0）与 "signal persists" 叙事存在张力 |
| Excitement | 2.5/5 | 任务定义有意义且时机恰当（model collapse 话题热度高），但执行层面无算法创新，RF+统计特征是成熟方法的直接应用；cross-transfer 性能较弱限制实用价值 |
| Reproducibility | 4.0/5 | LoRA 训练协议（Appendix A）、特征定义（Table 1）、超参数均有详细记录；承诺释放代码和数据；随机种子有报告 |
| Overall Assessment | 3.0/5 | Findings 可接收：新颖任务形式化 + 系统实证分析，但缺乏方法论贡献、scale 受限、实用性存疑 |
| Confidence | 4/5 | 熟悉 AI text detection 和 model collapse 文献 |

### Must-Fix 问题

**N1** [critical] Scale generalization 的叙事与证据之间存在系统性张力
- Abstract 声称 fingerprints "are consistent in direction but scale-dependent in magnitude"，但 14B 结果 EDD=0，4-class 准确率仅 50.8%（2× chance）。7-8B 优于 chance 但未重新训练分类器。在实际关心的模型规模（≥14B）上方法实用性未经验证。
- 建议：(1) Abstract 和 Introduction 中明确声明 14B EDD=0；(2) §5.4 扩展到主体正文；(3) 讨论 14B EDD=0 的可能原因及缓解方向。

**N2** [critical] Full-replacement 假设严重限制生态效度
- 所有实验使用 full-replacement 递归链。Gerstgrasser et al. (2024) 已证明 accumulation 可避免 collapse。如果深度信号仅在 replacement 场景下明显，整个方法的应用前景不明。Curation PoC（Appendix B.22）结果 inconclusive。
- 建议：(1) 增加 partial-mixing 实验（50% synthetic + 50% real）；(2) 如无法实验，在 Discussion 中深入分析。

**N3** [critical] 算法贡献有限，论文定位需要更谨慎
- 核心方法是标准 RF + 19 个标准统计特征。所有特征在 detection 文献中已有广泛使用（GLTR, Ghostbuster 等）。DeBERTa-v3 端到端基线反而低于 RF。论文在 p.2 称 "our contribution centers on task formalization and systematic empirical characterization"，定位诚实，但 Findings 级别也需要 non-trivial 的方法论 insight。
- 建议：(1) 深入分析为什么 RF 大幅优于 neural 方法；(2) 加强 EDD 的 formalization 使其成为更有理论深度的贡献。

### Should-Fix 问题

**W1** Abstract 信息过载，核心信息被淹没
- Abstract 包含过多具体数字（"180K-passage", "three model families", "19 statistical features", 多个百分比），核心贡献被稀释。
- 建议：精简到 1-2 个 headline 数字。

**W2** Discussion 过于单薄，核心洞察被放逐到 Appendix
- §6 约 1 页，混合讨论和结论。关键分析（multi-channel encoding, RF vs neural, curation PoC, cross-scale）全在 Appendix。
- 建议：将 Appendix B.9 和 B.22 核心结论提升到主体。

**W3** "Depth Degradation Atlas" 作为概念贡献被过度包装
- "Atlas" 暗示全面参考地图，但实际是 3×3 grid 的 empirical evaluation。
- 建议：使用更准确术语如 "systematic empirical analysis"。

**W4** Cross-model 和 cross-strategy transfer 性能较弱但讨论不足
- 用户需要先知道是哪个模型、哪种解码策略才能选择正确分类器，限制 blind deployment 实用性。
- 建议：Discussion 增加 practical deployment constraints 分析。

**W5** Curation PoC 结果 inconclusive 但论文仍暗示为 contribution
- d0-only 非最低 PPL，单次实验缺乏统计显著性，但 §6 语气偏乐观。
- 建议：明确定调为 preliminary/inconclusive。

### Minor 问题
- M1: 部分 bib entry 年份不匹配（he2021_deberta_v3, alemohammad2024_mad, guo2024_biscope）
- M2: gerstgrasser2024_accumulate 和 briesch2024selfconsuming 应更新为 inproceedings
- M3: AI 写作痕迹（-ing 分词短语多处出现）
- M4: Figure 1 heatmap 色彩对比度有限
- M5: 脚注 1 中 binary EDD 500 trees vs multi-class 200 trees 未解释

### 主要优势
1. 任务定义的新颖性和时效性
2. 实验设计的系统性（3×3×4 full grid + thorough appendix）
3. Perplexity tail insight 的理论连接
4. 诚实的局限性声明
5. 相关工作覆盖全面（68 篇引用，0 orphan/0 missing）
6. Strategy-dependent trajectory 的发现

### Claim-Evidence 匹配分析
- "59–82% four-class accuracy" ✅ 匹配
- "perplexity tail family dominates" ✅ 匹配
- "consistent in direction but scale-dependent" ⚠️ 14B EDD=0 使表述存疑
- "signal persists at larger scales" ⚠️ 50.8% 仅 2× chance
- "cross-model transfer 66.4%" ✅ 匹配但应突出 worst case
- "curation PoC" ⚠️ inconclusive 但语气偏乐观

### 可能遗漏的相关工作
1. PAN 2026 Shared Task（Generative Plagiarism Detection）
2. TROVE (NAACL 2025?) 和 GenProve (2026) — fine-grained text provenance
3. "Collapse or Thrive?" (arXiv:2410.16713, 2024) — synthetic data survey
4. "Rate of Model Collapse in Recursive Training" (arXiv:2412.17646, 2024) — collapse 速率理论

---

请逐条回应以上所有 Must-Fix、Should-Fix 和 Minor 问题。对每条明确标注 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-20T06:42:16.849717+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2（新颖性与完整性）审稿意见的逐条回应\n\n---\n\n### 总体评分\n[AGREE] R2 的 Overall 3.0 (Findings) 评分。我给出了相同分数，理由高度重叠：任务定义新颖、benchmark 系统，但方法贡献有限、scale generalization 不足、cross-transfer 实用性存疑。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Scale generalization 叙事与证据的系统性张力**\n\n完全同意。我在自己的 N3 中提出了本质相同的问题。补充两点 R2 未明确提到的证据：\n\n(1) 14B 实验的内部不一致更深层：论文自己定义的 EDD 指标（Section 3.4 Definition 1）在 14B 上报告 EDD=0，这意味着按照论文自己的度量标准，14B 文本的相邻深度不可判别。但 Section 6 第 1 段仍写 \"d1-d3 discrimination persists with strategy-specific AUC patterns\"——这与 EDD=0 的定义矛盾。\n\n(2) Table B.6 中 14B 的 d0v1 AUC（0.561-0.643）远低于 1-1.5B 的 >0.99。考虑到 d0/d1 boundary 是整个框架中最容易的判别（human vs first-gen），这个 boundary 的崩塌比 d1-d3 的困难更值得关注——它暗示 14B 的 depth signal 可能根本是不同性质的，而非同一信号的 scale-dependent attenuation。\n\n**[REBUT] R2-N2: Full-replacement 假设严重限制生态效度 → 不同意 \"critical\" 严重度**\n\nR2 将此标为 critical，我认为应降为 Should-Fix，理由如下：\n\n(1) Full-replacement 是研究递归生成深度的 *必要起点*。正如 controlled experiment 需要隔离变量，full-replacement 消除了 mixing ratio 这个连续混淆变量，使 depth 成为唯一自变量。论文明确声明 \"Our results therefore represent an upper bound on feature separability\"（Limitations §1），定位为 upper bound 而非 real-world deployment 方案。\n\n(2) Gerstgrasser et al. (2024) 证明 accumulation 可避免 collapse，但这恰恰说明 full-replacement 场景下 depth signal 更强——论文选择 signal 最强的设定来建立 feasibility，再逐步推广，是合理的研究策略。\n\n(3) 论文已有 partial evidence：prompted generation（Appendix B.22, Table B.15: 69.5%, -13.8pp）和 mixed-depth corpus（Appendix B.14: macro-recall Δ=-1.62pp）提供了部分 relaxation。完整的 accumulation 实验确实重要，但其缺失不构成对当前贡献的否定——它是 future work，不是 fatal flaw。\n\n(4) 作为 Findings 论文，在 controlled setting 下建立 feasibility + 系统实证分析已足够。要求 accumulation 实验等同于要求一篇论文同时解决 controlled 和 wild 场景。\n\n建议维持 Should-Fix：在 Discussion 中加深 accumulation 场景的分析，但不需要新实验。\n\n**[AGREE with nuance] R2-N3: 算法贡献有限**\n\n同意 R2 的判断，但有细微差异：\n\n(1) 同意 \"RF + 19 标准特征\" 本身无算法创新。但 R2 声称 \"所有特征在 detection 文献中已有广泛使用（GLTR, Ghostbuster 等）\" 不完全准确。GLTR 和 Ghostbuster 使用的是 token-level log-probability 和 per-token rank 特征，而本文的 *passage-level distributional statistics*（p90_ppl, var_surprisal, kurtosis_ppl）是对 token-level 信号的 distributional aggregation——这是一个非 trivial 的特征工程选择，并且论文展示了为什么这种 aggregation 有效（tail erosion 理论，Section 3.5）而 token-level 方法（DetectGPT 28.8%, Min-K% 33.2%）失败。\n\n(2) 同意 EDD 的 formalization 有改进空间。当前定义（Definition 1, Section 3.4）的 contiguous prefix 要求在 non-monotonic 场景下过于保守（如论文自己在 Limitations 中承认）。如果 EDD 能处理 non-contiguous discriminable regions，将显著增强理论贡献。\n\n(3) R2 建议 \"深入分析为什么 RF 大幅优于 neural 方法\" ——我强烈支持。论文有 partial 分析（Appendix B.7 feature overlap analysis: PLM [CLS] representations yield negative R² for var_surprisal and p90_ppl），但这个结果非常有趣且未在主文中充分展开。如果加强为 \"perplexity tail statistics are not linearly accessible in pretrained representation space\"，这可以成为一个有价值的 insight。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: Abstract 信息过载**\n\n不同意。ACL/EMNLP 的 abstract 惯例允许甚至鼓励包含具体数字以便检索和快速评估。我审查的 abstract 中的 key numbers（180K, 3 model families, 59-82%, 9-cell grid）每个都 serve a specific purpose：benchmark scale, generalization scope, performance range, experimental design。问题不在于数字过多，而在于 *which* numbers are highlighted——正如我在 N1 中指出，d1-d3 balanced accuracy 应与 four-class accuracy 并列呈现，而非用 four-class 单独 headline。\n\n**[AGREE] R2-W2: Discussion 过于单薄**\n\n同意。Section 6 约 1 页，混合了 summary 和 discussion。关键分析（multi-channel encoding 分解、RF vs neural 的 representational gap、cross-scale 趋势的 theoretical implications）全在 Appendix。建议将 Appendix B.7（feature overlap analysis）和 B.17（Binoculars signal decomposition）的核心结论提升到 Section 6，使 discussion 更有理论深度。\n\n**[REBUT] R2-W3: \"Depth Degradation Atlas\" 过度包装**\n\n不完全同意。\"Atlas\" 在计量学和系统生物学中指 systematic empirical map across a parameter grid——论文的 3 model families × 3 strategies × 4 depths × 19 features 的系统性评估，加上跨维度的 consistency analysis（feature rank correlation ρ̄=0.868, Table 3）和 sensitivity analysis（EDD at multiple thresholds），符合 \"atlas\" 的使用惯例。如果只是单一模型的 accuracy table，称 \"atlas\" 确实过度；但 9 cells 的完整交叉分析 + feature trajectory + EDD decay curve + importance heatmap（Figure 1）构成了一个有参考价值的 empirical map。\n\n不过 R2 说 \"暗示全面参考地图\" 有道理——3×3 grid 的覆盖范围确实有限（3 个 model families 均为 1-1.5B，且仅 nucleus/temp/top-k 三种 strategy）。建议折中：保留 \"atlas\" 但在首次使用时加注 scope（\"a 3×3 atlas at the 1-1.5B scale\"）。\n\n**[AGREE] R2-W4: Cross-model 和 cross-strategy transfer 性能较弱但讨论不足**\n\n同意。我在 W2 中提出了类似问题。补充一个 R2 未明确提到的点：two-stage pipeline（strategy identification + depth classification）回收 11.5pp，但论文未报告 strategy classifier 本身的准确率。如果 strategy identification 本身不可靠，two-stage pipeline 的实际增益会打折扣。这是 deployment feasibility 的关键缺失。\n\n**[AGREE] R2-W5: Curation PoC 结果 inconclusive 但论文仍暗示为 contribution**\n\n完全同意。我在 W7 中提出了相同问题。RF-vs-unfiltered p=0.407，主假设不成立。Bonferroni 校正后仅 1/3 RF-vs-random comparisons 存活（Appendix B.23 自己承认）。Section 6 和 Appendix B.23 的措辞（\"inconclusive preliminary evidence\"）已比早期版本改善，但 Appendix B.10 的标题（\"Downstream Curation PoC\"）和呈现方式仍可能给 skimming reader 留下 positive 印象。\n\n---\n\n### Minor 问题\n\n**[AGREE] R2-M1**: bib 年份不匹配。我在引用验证中也发现了相同问题（he2021_deberta_v3: bib=2023 vs actual=2021; alemohammad2024_mad: first author mismatch; guo2024_biscope: first author mismatch）。\n\n**[AGREE] R2-M2**: gerstgrasser2024_accumulate 等应从 misc 更新为 inproceedings（如已被会议接收）。\n\n**[REBUT] R2-M3: AI 写作痕迹（-ing 分词短语）**\n\n不同意将此列为问题。-ing participial phrases 是学术英语中的标准构造（如 \"confirming that...\", \"suggesting that...\", \"indicating that...\"），在 NLP/ML 论文中普遍使用。Ethics Statement 透明披露了 \"This research used AI coding assistants for experiment implementation and writing drafts\"（p.10）。除非 R2 能指出具体的不自然表述，仅以 -ing 频率为由标记 \"AI 写作痕迹\" 缺乏依据，且与 double-blind review 的精神相悖（不应基于写作风格推断作者身份或工具使用）。\n\n**[AGREE] R2-M4**: Figure 1 heatmap 对比度有限。从 PDF 视觉检查来看，低 importance 值之间的颜色区分确实不够明显。\n\n**[AGREE] R2-M5**: 脚注 1 中 EDD binary classifier 使用 500 trees vs main 4-class RF 200 trees，未解释原因。这是一个合理的实验设计问题——不同 tree 数量可能影响 AUC 估计，且 EDD 的 AUC 阈值判定对 classifier capacity 敏感。\n\n---\n\n### Claim-Evidence 匹配分析\n\n[AGREE] R2 的所有 6 条 claim-evidence 匹配判断。特别强调：\n\n- \"signal persists at larger scales\" ⚠️：这与我的 N3 一致。50.8% (2× chance) 在 5 个混淆变量下不能归因于 depth signal。\n- \"curation PoC\" ⚠️：p>0.4 的主假设检验不成立，应明确标记为 inconclusive。\n\n---\n\n### 可能遗漏的相关工作\n\n**[AGREE]** R2 建议补充的 4 篇参考文献均有道理：\n1. PAN 2026 (Generative Plagiarism Detection) — 如果确实存在该 shared task，直接相关\n2. TROVE / GenProve — fine-grained text provenance，与论文的 depth estimation 互补\n3. \"Collapse or Thrive?\" — synthetic data survey，可丰富 Related Work\n4. \"Rate of Model Collapse in Recursive Training\" — collapse 速率理论，可能与 EDD upper bound 分析（Section 3.5）直接相关\n\n建议作者核实这些参考文献的可用性并酌情补充。\n\n---\n\n### 与我审稿的一致性和差异\n\n**高度一致的判断**：\n- 14B \"signal persists\" overclaiming（R2-N1 ≈ 我的 N3）\n- d0 inflation（R2 在 claim-evidence 中提及，我的 N1 更详细）\n- Curation PoC inconclusive（R2-W5 ≈ 我的 W7）\n- Cross-transfer 实用性不足（R2-W4 ≈ 我的 W2）\n- 最终评分完全一致（3.0 Findings）\n\n**R2 强调而我未充分覆盖的**：\n- Full-replacement 生态效度（R2-N2）——我认为严重度应低于 R2 的判定\n- Discussion 单薄 / Appendix-heavy 结构（R2-W2）——我同意但在我的审稿中未单独列出\n\n**我强调而 R2 未充分覆盖的**：\n- Binoculars parity（我的 N2）：78.4% vs 78.1% (p>0.05) 是方法论贡献的核心挑战，R2 未提及\n- Self-reference confound（我的 W1）：Pythia-1.4B 同时作为 reference 和 generator，4-11pp 优势使 atlas 内部不可比\n- EDD T=0.70 阈值选择缺乏依据（我的 W5）\n- 单一 LoRA 配置无 sensitivity（我的 W3）",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2（新颖性与完整性）审稿意见的逐条回应\n\n---\n\n### 总体评分\n[AGREE] R2 的 Overall 3.0 (Findings) 评分。我给出了相同分数，理由高度重叠：任务定义新颖、benchmark 系统，但方法贡献有限、scale generalization 不足、cross-transfer 实用性存疑。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Scale generalization 叙事与证据的系统性张力**\n\n完全同意。我在自己的 N3 中提出了本质相同的问题。补充两点 R2 未明确提到的证据：\n\n(1) 14B 实验的内部不一致更深层：论文自己定义的 EDD 指标（Section 3.4 Definition 1）在 14B 上报告 EDD=0，这意味着按照论文自己的度量标准，14B 文本的相邻深度不可判别。但 Section 6 第 1 段仍写 \"d1-d3 discrimination persists with strategy-specific AUC patterns\"——这与 EDD=0 的定义矛盾。\n\n(2) Table B.6 中 14B 的 d0v1 AUC（0.561-0.643）远低于 1-1.5B 的 >0.99。考虑到 d0/d1 boundary 是整个框架中最容易的判别（human vs first-gen），这个 boundary 的崩塌比 d1-d3 的困难更值得关注——它暗示 14B 的 depth signal 可能根本是不同性质的，而非同一信号的 scale-dependent attenuation。\n\n**[REBUT] R2-N2: Full-replacement 假设严重限制生态效度 → 不同意 \"critical\" 严重度**\n\nR2 将此标为 critical，我认为应降为 Should-Fix，理由如下：\n\n(1) Full-replacement 是研究递归生成深度的 *必要起点*。正如 controlled experiment 需要隔离变量，full-replacement 消除了 mixing ratio 这个连续混淆变量，使 depth 成为唯一自变量。论文明确声明 \"Our results therefore represent an upper bound on feature separability\"（Limitations §1），定位为 upper bound 而非 real-world deployment 方案。\n\n(2) Gerstgrasser et al. (2024) 证明 accumulation 可避免 collapse，但这恰恰说明 full-replacement 场景下 depth signal 更强——论文选择 signal 最强的设定来建立 feasibility，再逐步推广，是合理的研究策略。\n\n(3) 论文已有 partial evidence：prompted generation（Appendix B.22, Table B.15: 69.5%, -13.8pp）和 mixed-depth corpus（Appendix B.14: macro-recall Δ=-1.62pp）提供了部分 relaxation。完整的 accumulation 实验确实重要，但其缺失不构成对当前贡献的否定——它是 future work，不是 fatal flaw。\n\n(4) 作为 Findings 论文，在 controlled setting 下建立 feasibility + 系统实证分析已足够。要求 accumulation 实验等同于要求一篇论文同时解决 controlled 和 wild 场景。\n\n建议维持 Should-Fix：在 Discussion 中加深 accumulation 场景的分析，但不需要新实验。\n\n**[AGREE with nuance] R2-N3: 算法贡献有限**\n\n同意 R2 的判断，但有细微差异：\n\n(1) 同意 \"RF + 19 标准特征\" 本身无算法创新。但 R2 声称 \"所有特征在 detection 文献中已有广泛使用（GLTR, Ghostbuster 等）\" 不完全准确。GLTR 和 Ghostbuster 使用的是 token-level log-probability 和 per-token rank 特征，而本文的 *passage-level distributional statistics*（p90_ppl, var_surprisal, kurtosis_ppl）是对 token-level 信号的 distributional aggregation——这是一个非 trivial 的特征工程选择，并且论文展示了为什么这种 aggregation 有效（tail erosion 理论，Section 3.5）而 token-level 方法（DetectGPT 28.8%, Min-K% 33.2%）失败。\n\n(2) 同意 EDD 的 formalization 有改进空间。当前定义（Definition 1, Section 3.4）的 contiguous prefix 要求在 non-monotonic 场景下过于保守（如论文自己在 Limitations 中承认）。如果 EDD 能处理 non-contiguous discriminable regions，将显著增强理论贡献。\n\n(3) R2 建议 \"深入分析为什么 RF 大幅优于 neural 方法\" ——我强烈支持。论文有 partial 分析（Appendix B.7 feature overlap analysis: PLM [CLS] representations yield negative R² for var_surprisal and p90_ppl），但这个结果非常有趣且未在主文中充分展开。如果加强为 \"perplexity tail statistics are not linearly accessible in pretrained representation space\"，这可以成为一个有价值的 insight。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: Abstract 信息过载**\n\n不同意。ACL/EMNLP 的 abstract 惯例允许甚至鼓励包含具体数字以便检索和快速评估。我审查的 abstract 中的 key numbers（180K, 3 model families, 59-82%, 9-cell grid）每个都 serve a specific purpose：benchmark scale, generalization scope, performance range, experimental design。问题不在于数字过多，而在于 *which* numbers are highlighted——正如我在 N1 中指出，d1-d3 balanced accuracy 应与 four-class accuracy 并列呈现，而非用 four-class 单独 headline。\n\n**[AGREE] R2-W2: Discussion 过于单薄**\n\n同意。Section 6 约 1 页，混合了 summary 和 discussion。关键分析（multi-channel encoding 分解、RF vs neural 的 representational gap、cross-scale 趋势的 theoretical implications）全在 Appendix。建议将 Appendix B.7（feature overlap analysis）和 B.17（Binoculars signal decomposition）的核心结论提升到 Section 6，使 discussion 更有理论深度。\n\n**[REBUT] R2-W3: \"Depth Degradation Atlas\" 过度包装**\n\n不完全同意。\"Atlas\" 在计量学和系统生物学中指 systematic empirical map across a parameter grid——论文的 3 model families × 3 strategies × 4 depths × 19 features 的系统性评估，加上跨维度的 consistency analysis（feature rank correlation ρ̄=0.868, Table 3）和 sensitivity analysis（EDD at multiple thresholds），符合 \"atlas\" 的使用惯例。如果只是单一模型的 accuracy table，称 \"atlas\" 确实过度；但 9 cells 的完整交叉分析 + feature trajectory + EDD decay curve + importance heatmap（Figure 1）构成了一个有参考价值的 empirical map。\n\n不过 R2 说 \"暗示全面参考地图\" 有道理——3×3 grid 的覆盖范围确实有限（3 个 model families 均为 1-1.5B，且仅 nucleus/temp/top-k 三种 strategy）。建议折中：保留 \"atlas\" 但在首次使用时加注 scope（\"a 3×3 atlas at the 1-1.5B scale\"）。\n\n**[AGREE] R2-W4: Cross-model 和 cross-strategy transfer 性能较弱但讨论不足**\n\n同意。我在 W2 中提出了类似问题。补充一个 R2 未明确提到的点：two-stage pipeline（strategy identification + depth classification）回收 11.5pp，但论文未报告 strategy classifier 本身的准确率。如果 strategy identification 本身不可靠，two-stage pipeline 的实际增益会打折扣。这是 deployment feasibility 的关键缺失。\n\n**[AGREE] R2-W5: Curation PoC 结果 inconclusive 但论文仍暗示为 contribution**\n\n完全同意。我在 W7 中提出了相同问题。RF-vs-unfiltered p=0.407，主假设不成立。Bonferroni 校正后仅 1/3 RF-vs-random comparisons 存活（Appendix B.23 自己承认）。Section 6 和 Appendix B.23 的措辞（\"inconclusive preliminary evidence\"）已比早期版本改善，但 Appendix B.10 的标题（\"Downstream Curation PoC\"）和呈现方式仍可能给 skimming reader 留下 positive 印象。\n\n---\n\n### Minor 问题\n\n**[AGREE] R2-M1**: bib 年份不匹配。我在引用验证中也发现了相同问题（he2021_deberta_v3: bib=2023 vs actual=2021; alemohammad2024_mad: first author mismatch; guo2024_biscope: first author mismatch）。\n\n**[AGREE] R2-M2**: gerstgrasser2024_accumulate 等应从 misc 更新为 inproceedings（如已被会议接收）。\n\n**[REBUT] R2-M3: AI 写作痕迹（-ing 分词短语）**\n\n不同意将此列为问题。-ing participial phrases 是学术英语中的标准构造（如 \"confirming that...\", \"suggesting that...\", \"indicating that...\"），在 NLP/ML 论文中普遍使用。Ethics Statement 透明披露了 \"This research used AI coding assistants for experiment implementation and writing drafts\"（p.10）。除非 R2 能指出具体的不自然表述，仅以 -ing 频率为由标记 \"AI 写作痕迹\" 缺乏依据，且与 double-blind review 的精神相悖（不应基于写作风格推断作者身份或工具使用）。\n\n**[AGREE] R2-M4**: Figure 1 heatmap 对比度有限。从 PDF 视觉检查来看，低 importance 值之间的颜色区分确实不够明显。\n\n**[AGREE] R2-M5**: 脚注 1 中 EDD binary classifier 使用 500 trees vs main 4-class RF 200 trees，未解释原因。这是一个合理的实验设计问题——不同 tree 数量可能影响 AUC 估计，且 EDD 的 AUC 阈值判定对 classifier capacity 敏感。\n\n---\n\n### Claim-Evidence 匹配分析\n\n[AGREE] R2 的所有 6 条 claim-evidence 匹配判断。特别强调：\n\n- \"signal persists at larger scales\" ⚠️：这与我的 N3 一致。50.8% (2× chance) 在 5 个混淆变量下不能归因于 depth signal。\n- \"curation PoC\" ⚠️：p>0.4 的主假设检验不成立，应明确标记为 inconclusive。\n\n---\n\n### 可能遗漏的相关工作\n\n**[AGREE]** R2 建议补充的 4 篇参考文献均有道理：\n1. PAN 2026 (Generative Plagiarism Detection) — 如果确实存在该 shared task，直接相关\n2. TROVE / GenProve — fine-grained text provenance，与论文的 depth estimation 互补\n3. \"Collapse or Thrive?\" — synthetic data survey，可丰富 Related Work\n4. \"Rate of Model Collapse in Recursive Training\" — collapse 速率理论，可能与 EDD upper bound 分析（Section 3.5）直接相关\n\n建议作者核实这些参考文献的可用性并酌情补充。\n\n---\n\n### 与我审稿的一致性和差异\n\n**高度一致的判断**：\n- 14B \"signal persists\" overclaiming（R2-N1 ≈ 我的 N3）\n- d0 inflation（R2 在 claim-evidence 中提及，我的 N1 更详细）\n- Curation PoC inconclusive（R2-W5 ≈ 我的 W7）\n- Cross-transfer 实用性不足（R2-W4 ≈ 我的 W2）\n- 最终评分完全一致（3.0 Findings）\n\n**R2 强调而我未充分覆盖的**：\n- Full-replacement 生态效度（R2-N2）——我认为严重度应低于 R2 的判定\n- Discussion 单薄 / Appendix-heavy 结构（R2-W2）——我同意但在我的审稿中未单独列出\n\n**我强调而 R2 未充分覆盖的**：\n- Binoculars parity（我的 N2）：78.4% vs 78.1% (p>0.05) 是方法论贡献的核心挑战，R2 未提及\n- Self-reference confound（我的 W1）：Pythia-1.4B 同时作为 reference 和 generator，4-11pp 优势使 atlas 内部不可比\n- EDD T=0.70 阈值选择缺乏依据（我的 W5）\n- 单一 LoRA 配置无 sensitivity（我的 W3）",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-20T06:42:21.197565+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4347
}
```

</details>

---


### Assistant

_source line 784 · 2026-05-20T06:42:29.227337+00:00_

交叉回应已提交给 Director。

核心判断：与 R2 在 Overall 评分（3.0 Findings）和多数问题上高度一致，尤其是 14B overclaiming、curation PoC inconclusive、cross-transfer 实用性不足。主要分歧在两点：(1) full-replacement 假设我认为应降为 Should-Fix 而非 critical——作为 controlled study 的起点合理；(2) abstract 信息量我认为是风格偏好而非缺陷。另外我补充了 R2 未覆盖的 Binoculars parity（78.4% vs 78.1%）和 self-reference confound 两个问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 28

## Round 28

78 recorded events


### User

_source line 785 · 2026-05-20T08:34:07.107986+00:00_

[Round 1 审稿请求]:
# Round 1 审稿任务 — Reviewer 1

## 论文信息
- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
- **文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`

## Venue 要求
- **目标**: EMNLP 2026 (ARR May 2026 cycle)
- **截止日期**: 2026-05-25 (ARR submission); 2026-08-02 (commitment)
- **类型**: Long Paper
- **正文页数限制**: 8 页（不含 Limitations、Ethics、References）
- **模板**: ACL format (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind（无匿名期要求）
- **附录**: 可选补充材料
- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

## 你的审查侧重：方法严谨性 + 实验设计

请重点审查以下维度：

1. **方法论严谨性**
   - 问题形式化（ordinal classification for depth estimation）是否合理？定义是否清晰无歧义？
   - 19 个统计特征的设计是否有充分理论/实证依据？特征间多重共线性（VIF>10 for 14-16/19 features）是否影响结论可靠性？
   - EDD 指标定义（Eq. 1）是否严密？阈值 T=0.70 的选择是否充分论证？monotonicity assumption 的局限性讨论是否充分？
   - Random Forest 作为主分类器的选择是否充分论证？与 XGBoost/LightGBM 收敛到 0.4pp 内是否真能说明"信号在特征不在分类器"？

2. **实验设计与 Benchmark**
   - Benchmark 构建（3 families × 3 strategies × 4 depths × 5000 samples）是否合理？为何选这3个模型（1-1.5B）？
   - LoRA finetuning pipeline（r=16, α=32, lr=2e-4, 3 epochs）的超参选择是否有依据？
   - BOS-seeded vs prompted generation：论文报告 −13.8pp 差异，是否充分讨论了影响？
   - 评估方案（5-fold stratified CV, 200 trees）是否恰当？是否有数据泄漏风险？
   - Reference model (Pythia-1.4B) 与 Pythia generator 重叠的 self-reference confound：4-11pp advantage 是否使 Pythia 结果不可比？Table 2 中 Pythia 标 † 是否足够？

3. **泛化实验严谨性**
   - Cross-model LOO transfer (mean 66.4%, d1-d3: 55.4%)：设计是否合理？d0 recall >98% 膨胀 headline 的问题？
   - Cross-strategy transfer (59.1%, d1-d3: 45.9%)：d1/d2 boundary inversion 问题是否说明方法有根本局限？z-score normalization 修复只改善 logistic regression 不改善 RF 的含义？
   - Cross-domain arXiv (74.1%)：仅一个域是否足够？C4/FineWeb FPR 34%/17% 说明什么？
   - 14B cross-scale (mean 50.8%, EDD₀.₇₀=0)：5 重混淆因素下的结论表述是否审慎？

4. **Baseline 比较公平性**
   - Binoculars 11-feat RF (78.1%) vs 本文 19-feat RF (78.4%)：p>0.05，无显著差异。Merged 30-feat (82.6%) 的讨论是否充分？部署优势论证是否成立（1 reference model vs observer-performer pair）？
   - DeBERTa-v3 end-to-end baseline 下降 16-32pp：是否因为 ordinal classification 对 neural encoder 本身就难？
   - DetectGPT (28.8%), Min-K% Prob (33.2%)：这些 binary detector 用 CORAL calibration 后仍只 40.4%，比较框架是否公平（它们并非为 ordinal 设计）？

5. **统计严谨性**
   - Bootstrap CI (B=1000) 和 permutation test 的使用是否正确？
   - 多重比较（9 cells × 多个 metrics）是否需要校正？
   - 效应量报告是否充分？MAE=0.23, QWK=0.89 等指标选择是否恰当？

请按以下结构输出审稿意见：
- **Strengths**（逐条）
- **Weaknesses**（分 Must-Fix / Should-Fix / Minor，每条说明理由并 cite 具体 Section/Table/Figure）
- **Questions**（需作者澄清的技术问题）
- **Missing References**（遗漏的重要相关工作）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-20T08:34:17.365988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-20T08:34:18.273154+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-20T08:34:18.323922+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-20T08:34:18.374748+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-20T08:34:22.647328+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 791 · 2026-05-20T08:34:23.652740+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "project": "recursive_gen_depth_est",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "project": "recursive_gen_depth_est",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-20T08:34:24.308399+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-20T08:34:30.788774+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here's what I found:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommend
…[truncated 1356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8141
}
```

</details>

---


### Tool result

_source line 794 · 2026-05-20T08:34:32.563006+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 553.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 554.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 433.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 543.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_
…[truncated 289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8910
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-20T08:35:34.880097+00:00_

&lt;persisted-output>
Output too large (58KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/2406c74c-2e41-4eaa-938c-797f41897efe/tool-results/toolu_01R1FETvP14QfexW3qa6B9XK.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 74, \"total_citations\": 112, \"unique_cited_keys\": 72, \"orphan_bib\": 2, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 63, \"online_not_found\": 7, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [\"dsir2023\", \"qurating2024\"], \"missing_bib\": [], \"orphan_count\": 2, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"au
…[truncated 362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 70571
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-20T08:35:39.091525+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-20T08:35:39.091983+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-20T08:35:39.697422+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 799 · 2026-05-20T08:35:40.235123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 800 · 2026-05-20T08:35:41.040674+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1343
}
```

</details>

---


### Tool call

_source line 801 · 2026-05-20T08:35:41.041152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 802 · 2026-05-20T08:35:41.444131+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1209
}
```

</details>

---


### Tool call

_source line 803 · 2026-05-20T08:35:41.494900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-20T08:35:41.947033+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-20T08:35:41.948199+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool result

_source line 806 · 2026-05-20T08:35:42.653284+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1158
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-20T08:35:42.905143+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-20T08:35:47.677476+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 809 · 2026-05-20T08:35:48.230995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-20T08:35:48.638068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-20T08:35:49.198520+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 967
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-20T08:35:49.198995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-20T08:35:50.105142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1467
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-20T08:35:50.105626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 815 · 2026-05-20T08:35:50.208068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 816 · 2026-05-20T08:35:50.361799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1162
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-20T08:35:51.569779+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1464
}
```

</details>

---


### Tool result

_source line 818 · 2026-05-20T08:35:51.621165+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1413
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-20T08:35:56.607478+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with unlikely but conceivable gaps
- **3**: Pretty sure but possible oversight of details
- **2**: Can defend evaluation but likely missed some details
- **1**: Outside expertise area or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: Most thorough study of its type
- **4**: Sufficient support for claims; extra experiments optional
- **3**: Adequate support for main claims with minor gaps
- **2**: Main claims lack sufficient support; major technical problems
- **1**: Insufficient rigor or irrelevant to ACL

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Would recommend this paper to others and/or attend its presentation"
- **4**: Would mention to others; effort to attend presentation
- **3**: Might mention points; attend if time permits
- **2**: Doesn't resonate personally but may interest others
- **1**: Not exciting; unlikely resonance with ACL community

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations possible
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Cannot reproduce regardless of effort

## 6. **Datasets**
Scale: 1-5
- **5**: Enabling for research direction choices
- **4**: Useful for ongoing work
- **3**: Potentially useful
- **2**: Documentary value only
- **1**: No usable datasets submitted

## 7. **Software**
Scale: 1-5
- **5**: Enabling for research choices
- **4**: Useful fo
…[truncated 846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8930
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-20T08:36:03.386018+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "project": "recursive_gen_depth_est",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "project": "recursive_gen_depth_est",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-20T08:36:06.535158+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 589.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.7}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.6}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.4}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.2}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper
…[truncated 307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3149
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-20T08:36:06.585825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/2406c74c-2e41-4eaa-938c-797f41897efe/tool-results/toolu_01R1FETvP14QfexW3qa6B9XK.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/2406c74c-2e41-4eaa-938c-797f41897efe/tool-results/toolu_01R1FETvP14QfexW3qa6B9XK.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-20T08:36:06.891462+00:00_

1	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 74, \"total_citations\": 112, \"unique_cited_keys\": 72, \"orphan_bib\": 2, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 63, \"online_not_found\": 7, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [\"dsir2023\", \"qurating2024\"], \"missing_bib\": [], \"orphan_count\": 2, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"type\": \"inproceedings\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic
…[truncated 57422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 305
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-20T08:36:12.985841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 825 · 2026-05-20T08:36:13.388126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 826 · 2026-05-20T08:36:14.343301+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-20T08:36:14.344510+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-20T08:36:14.395049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 829 · 2026-05-20T08:36:14.858030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-20T08:36:15.365071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-20T08:36:15.818935+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1423
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-20T08:36:15.819357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-20T08:36:16.071740+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1213
}
```

</details>

---


### Tool result

_source line 834 · 2026-05-20T08:36:16.880163+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1515
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-20T08:36:17.082779+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1263
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-20T08:36:21.356917+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "project": "recursive_gen_depth_est",
  "pages": "17-25",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "project": "recursive_gen_depth_est",
    "pages": "17-25",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-20T08:36:22.413149+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.6}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.4}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.2}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.0}, {\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.9}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.4}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.8}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.4}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 371.8}], \"total_pages\": 25, \"rendered_pages\": 9, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_
…[truncated 103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-20T08:36:26.781028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 839 · 2026-05-20T08:36:27.133724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 840 · 2026-05-20T08:36:27.742672+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-20T08:36:27.743134+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 842 · 2026-05-20T08:36:28.800707+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1666
}
```

</details>

---


### Tool call

_source line 843 · 2026-05-20T08:36:29.158576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p20.png"
  }
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-20T08:36:29.159020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-20T08:36:29.460198+00:00_

Image file is empty: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p20.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-20T08:36:29.460757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-20T08:36:30.219787+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2476
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-20T08:36:30.272058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 849 · 2026-05-20T08:36:30.927557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p24.png"
  }
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-20T08:36:31.531120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-20T08:36:31.985824+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2525
}
```

</details>

---


### Tool result

_source line 852 · 2026-05-20T08:36:32.037221+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2878
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-20T08:36:33.550156+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3278
}
```

</details>

---


### Tool result

_source line 854 · 2026-05-20T08:36:34.005182+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3077
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-20T08:36:34.008605+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2477
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-20T08:39:49.464580+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Round 1 审稿意见\n\n## 论文信息\n**标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 问题定义新颖、实验体量充足，但核心方法在 in-distribution 上与已有 Binoculars 特征持平（p>0.05），在 cross-strategy/cross-scale 上大幅退化，headline 数字被 d0 近完美可分性膨胀，实际深层区分能力（d1-d3）远低于报告值。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心 claim 有部分实验支撑，但 self-reference confound、Binoculars 平局、cross-strategy/scale 失败构成重大方法论缺口 |\n| Excitement | 3.0/5 | 问题定义（ordinal depth estimation）有新意，Degradation Atlas 有系统价值，但方法性能未超越现有 binary detector 特征的简单重用 |\n| Reproducibility | 4/5 | 附录细节充分（超参、硬件、种子），承诺代码/数据公开，但 LoRA pipeline 缺少超参敏感性分析 |\n| Confidence | 4/5 | 熟悉 model collapse、AI text detection、ordinal classification 相关文献 |\n\n---\n\n## 主要优势\n\n**S1. 问题定义新颖且有实际价值。** 将递归生成深度估计形式化为 ordinal classification（Section 3.1），区别于 binary human-vs-machine detection，是一个自然且未被充分探索的方向。这对理解训练数据污染程度有直接意义。\n\n**S2. Degradation Atlas 系统性强。** Section 4 的 atlas（3 families × 3 strategies × 4 depths）提供了关于递归生成如何改变文本统计特性的系统实证图景。Feature consistency 分析（Section 4.2）、monotonicity 分析（Section 4.3）、EDD 分析（Section 4.4）构成了一个有价值的 empirical contribution，独立于分类器性能。\n\n**S3. 评估方案设计合理。** 使用 ordinal-specific metrics（QWK=0.89, MAE=0.23），5-fold stratified CV，bootstrap CI (B=1000)，permutation test，体现了统计素养。CORAL ordinal regression 对照也是恰当的。\n\n**S4. 消融实验覆盖面广。** 附录 B.1-B.29 涵盖了 permutation importance、feature trajectories、per-class recall、DCOL iteration、temperature robustness、generation length、feature group ablation、Binoculars decomposition、domain bias、wild-data calibration、reference model ablation、cross-scale 等多个角度，展现了严肃的实验态度。\n\n**S5. 引用质量高。** 74 篇引用中 63 篇 OpenAlex 验证通过，7 篇 not_found 均为真实论文（OpenAlex 覆盖缺口），无伪造引用。cross-check 显示 0 missing_bib（所有 \\cite 都有对应 bib 条目）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Binoculars 特征平局严重削弱方法论贡献**\n- 具体位置：Section 5.1, Table 4\n- 问题：论文的 19-feature RF 达到 78.4%，而 Binoculars 的 11 features 用相同 RF 达到 78.1%，p>0.05 无显著差异。Merged 30-feature 达到 82.6%，但这说明信息是互补的、而非本文特征优于已有特征。论文声称的部署优势（\"1 reference model vs observer-performer pair\"，Section 5.1）是工程论证而非科学贡献。\n- 为什么影响接收：如果现有 binary detector 的特征简单重新标定（CORAL calibration）就能达到相同 ordinal 性能，则本文 19 个统计特征的设计贡献被大幅稀释。论文的核心 claim \"discriminative signal resides in feature design\"（Section 5.1）恰好被 Binoculars 平局所反驳——信号不在*这些*特征，而在*任何*能捕获分布偏移的特征。\n- 建议修改方向：(1) 在 abstract/intro 诚实报告 Binoculars 平局；(2) 将 contribution 重新定位为\"问题定义 + atlas + benchmark\"而非\"特征设计\"；(3) 分析为何 merged 30-feature 提升 4.2pp——互补信息来自哪里？\n\n**N2** [critical] **Self-reference confound 使 Pythia 结果不可比，膨胀 headline 数字**\n- 具体位置：Section 3.3（reference model = Pythia-1.4B），Table 2（Pythia 行标 †），Appendix B.13（Table 16）\n- 问题：Pythia-1.4B 同时是 generator（3 个 family 之一）和 reference model（特征提取的唯一模型）。Table 2 显示 Pythia 比 OLMo/GPT-2 XL 高 4-11pp。Appendix B.13 的 reference model ablation 显示换用 GPT-2 XL 作 reference 时 accuracy 降至 67.3%（−11pp）。这意味着 headline \"78.4%\" 中 Pythia 行的贡献包含了 self-reference 优势。\n- 为什么影响接收：1/3 的 in-distribution 结果存在系统性偏差。cross-model transfer（Table 5）中 Pythia holdout 行（62.4%）低于 OLMo（69.2%）反映了这一 confound 的传递。如果排除 Pythia 或使用 non-Pythia reference，headline 数字会下降。\n- 建议修改方向：(1) 主实验增加一个 non-overlapping reference model 的全量结果（如 GPT-NeoX）；(2) 报告 \"excluding Pythia\" 的 mean accuracy 作为 conservative estimate；(3) 将 † caveat 从脚注提升到正文讨论。\n\n**N3** [critical] **d0 膨胀 headline 数字，d1-d3 实际性能远低于报告值**\n- 具体位置：Abstract（\"68.9-85.9% accuracy\"），Section 4.1（\"Depth-0 recall exceeds 97%\"），Table 5（cross-model mean 66.4%），Table 6（cross-strategy 59.1%）\n- 问题：d0（人类文本）与 d1+ 的区分本质上是 binary human-vs-machine detection，已被大量现有工作解决。真正有价值的是 d1-d2-d3 的细粒度区分。但 cross-model d1-d3 仅 55.4%（chance 33%），cross-strategy d1-d3 仅 45.9%。Abstract 报告 \"68.9-85.9%\" 和 \"cross-model transfer reaches 66.4%\" 时没有突出 d1-d3 的大幅下降。\n- 为什么影响接收：这是一种 overclaiming——论文标题和 framing 围绕 \"depth estimation\"，但实际方法的深层区分能力接近 chance。读者会被 headline 数字误导。\n- 建议修改方向：(1) Abstract 和 Introduction 必须报告 d1-d3 准确率；(2) 正文中将 d0 结果与 d1-d3 结果明确分开讨论；(3) 承认深层区分是当前方法的主要瓶颈。\n\n**N4** [critical] **Cross-strategy 和 cross-scale 失败动摇方法的泛化 claim**\n- 具体位置：Section 5.3（Table 6, 59.1%），Section 5.4（14B: 50.8%, EDD₀.₇₀=0），Limitations（p.9）\n- 问题：Cross-strategy transfer d1-d3 仅 45.9%（接近 chance 33%），且出现 d1/d2 boundary inversion。z-score normalization 只修复 logistic regression 不修复 RF（Section 5.3），说明不同策略产生了根本不同的深度信号。14B cross-scale mean 50.8%、EDD₀.₇₀=0 意味着方法在更大模型上完全失效。论文在 Limitations 中承认了这些，但 abstract/introduction 的 framing 仍然偏乐观。\n- 为什么影响接收：一个 depth estimation 方法如果只在训练时见过的 strategy 上工作、且无法推广到实际部署的模型规模（7B/14B），其实际应用价值有限。这些不仅是 limitations，而是对核心 claim 的根本质疑。\n- 建议修改方向：(1) Abstract/intro 中对泛化限制进行显著标注，而非仅在 Limitations 提及；(2) 分析 cross-strategy 失败的根本原因——是特征空间不重叠还是 ordinal 结构消失？(3) 为 14B 实验分离至少一个 confound（如用 14B reference model）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **多重共线性与可解释性 claim 的矛盾**\n- 具体位置：Section 3.3（\"VIF>10 for 14-16/19 features\"），Section 4.2（feature importance via Gini/SHAP）\n- 问题：14-16/19 个特征 VIF>10 意味着严重的多重共线性。虽然 RF 对共线性相对鲁棒（就预测而言），但 Gini importance 和 SHAP 在共线性下不稳定——重要性会在相关特征间随机分配。Section 4.2 基于 Gini 和 SHAP 的特征重要性排序在这种共线性下是不可靠的。\n- 建议：(1) 使用 permutation importance（已在 Appendix B.2 做了，结论一致则强化论证）；(2) 对 SHAP 结果增加 caveat；(3) 或者使用降维后的特征子集做可解释性分析。\n\n**W2** [warning] **LoRA 微调超参无 ablation**\n- 具体位置：Section 3.2（\"LoRA (r=16, α=32, lr=2e-4, 3 epochs)\"），Appendix A（Table 7）\n- 问题：LoRA rank、learning rate、epoch 数直接影响生成文本的质量和多样性，进而影响 depth signatures。r=16 是一个特定选择——更高的 rank 产生更接近 full fine-tuning 的效果，可能产生不同的退化模式。论文未提供任何超参敏感性分析。\n- 建议：至少做一个 LoRA rank ablation（r=4, 8, 16, 32），验证 depth signatures 对微调强度的鲁棒性。\n\n**W3** [warning] **BOS-seeded generation 限制生态效度**\n- 具体位置：Section 3.2（generation pipeline），Appendix B.27（Table 29, −13.8pp for prompted generation）\n- 问题：主实验全部使用 BOS-seeded generation（从 BOS token 开始自由生成 512 tokens）。但现实中的递归生成（如 synthetic data pipeline、LLM 辅助写作）几乎都是 prompted generation。Appendix B.27 承认 prompted generation accuracy 下降 13.8pp。这不是边缘问题，而是核心 validity concern。\n- 建议：(1) 将 prompted generation 结果从附录提升到正文；(2) 讨论 BOS-seeded 与 prompted 在什么条件下等价/不等价；(3) 考虑混合 BOS/prompted 的训练数据。\n\n**W4** [warning] **单域 cross-domain 测试不够充分**\n- 具体位置：Section 5.4（\"cross-domain arXiv 74.1%\"），Appendix B.11（Table 13, C4 FPR 34%, FineWeb FPR 17%）\n- 问题：cross-domain 仅测试 arXiv（学术文本，本身有特定的文本统计特征）。WikiText-103 虽然用于 wild-data calibration（B.11），但不是 cross-domain 泛化测试。C4 上 34% 的 FPR 和 FineWeb 上 17% 的 FPR（Table 13）表明方法在非学术 web 文本上产生大量误报。\n- 建议：增加至少 2-3 个域（如 news、social media、code）的 cross-domain 评估，或者将 C4/FineWeb FPR 数据在正文中讨论而非藏在附录。\n\n**W5** [warning] **多重比较未校正**\n- 具体位置：Appendix B.2（\"multiple pairwise comparisons that were not corrected for multiplicity\"），Table 15（paired t-tests）\n- 问题：全文进行了大量统计检验（9 cells 的准确率比较、Table 15 的 pairwise comparisons、各种 ablation 中的 p 值），但均未做 Bonferroni/FDR 校正。Appendix B.2 中论文自己承认了这一点。Table 15 有 6 个 pairwise comparisons，p<0.05 可能仅因多重比较。\n- 建议：对所有包含多组比较的结果应用 Holm-Bonferroni 或 BH-FDR 校正，或者在正文中标注 adjusted p-values。\n\n**W6** [warning] **EDD 阈值 T=0.70 的论证依据不够充分**\n- 具体位置：Section 3.4（Eq. 1），引用 Hosmer & Lemeshow (2000)\n- 问题：T=0.70 引自 Hosmer & Lemeshow 的 AUC discrimination standard，但该标准是为 binary logistic regression 的 c-statistic 设计的，直接迁移到 multi-class ordinal 的 pairwise AUC 缺乏理论依据。虽然 Section 3.4 提供了 T∈{0.65,0.70,0.75,0.80} 的 sensitivity analysis，但没有解释为何 0.70 是 \"natural\" 的。\n- 建议：(1) 讨论为何 binary AUC 的 discrimination 标准可迁移到 ordinal pairwise AUC；(2) 或者提出一个 data-driven 的阈值选择方法。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Orphan bib entries: `dsir2023` 和 `qurating2024` 在 .bib 中定义但未在正文 \\cite，应清理。\n- **M2**: Table 2 脚注 1（\"RF binary classifiers use 500 trees; the main 4-class RF uses 200 trees\"）——为何 binary 和 4-class 用不同数量的树？未见讨论。\n- **M3**: Section 4.3 \"all 12 AUC profiles in our benchmark decay monotonically\" 与 Appendix B.14 中 GPT-2 XL 14B d4→d5 non-monotonic 的发现有 tension——应在正文中注明 monotonicity 仅在 1-1.5B 范围内成立。\n- **M4**: Figure 1 的 atlas heatmap 中颜色强度编码 RF Gini importance，但 W1 中指出的共线性问题意味着这些重要性值不稳定。\n- **M5**: Appendix B.28 \"Cross-strategy conditional decomposition\" 中 naïve pooled classifier 的讨论（\"the two-stage pipeline... yields 11.5pp gain\"）应考虑提到正文，因为它直接说明了 cross-strategy 失败的解决方向。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1**: 如果使用完全不同架构的 reference model（如 Mamba/RWKV 而非 Transformer），特征提取的结果会如何？当前 reference model ablation（B.13）仅在 Transformer LM 内部换模型。\n\n**Q2**: Perplexity tail features 真正捕获的是 \"depth-specific signature\" 还是仅仅是文本质量的代理（quality proxy）？一段由 depth-1 生成但碰巧质量较差的文本，与一段 depth-2 的 \"正常\" 文本，特征能否区分？\n\n**Q3**: Cross-strategy 中 z-score normalization 修复 logistic regression 但不修复 RF 的原因是什么？这是否说明 RF 学到了 strategy-specific 的非线性决策边界，而这些边界在 strategy 间不可迁移？\n\n**Q4**: DCOL iteration（Appendix B.5）中 convergence vs failure 的决定因素是什么？有没有可靠的 stopping criterion？\n\n**Q5**: 14B 实验中 5 个 confounders（Section 5.4）能否通过实验设计分离？例如用 14B 模型做 reference model 提取特征，是否能消除 scale mismatch confound？\n\n---\n\n## Missing References\n\n1. **Min-K%++ (Zhang et al., 2024)**: Min-K% Prob 的改进版本，在 membership inference 上有更好的性能，应作为 baseline 考虑。\n2. **Ordinal classification 综述**: 论文引用了 Frank (2001), McCullagh (1980), Rennie (2005) 等经典工作，但缺少对近年 ordinal classification 在 NLP 中的应用的系统综述引用。\n3. **RAID benchmark (Dugan et al., 2024)**: 虽然已引用，但未在实验中使用其数据或评估框架进行比较——考虑到 RAID 专门为 robustly evaluating detection 设计，解释为何不采用会更好。\n\n---\n\n## 格式合规检查\n\n- **页数**: 正文 8 页（pp.1-8），Limitations 在 p.9 开头，References 从 p.10 开始。符合 EMNLP 2026 的 8 页限制。\n- **匿名**: 使用 `\\usepackage[review]{acl}`，标题页为 \"Anonymous ACL submission\"，正文未见去匿名化内容。符合 double-blind 要求。\n- **Limitations section**: 存在（p.9），覆盖了 full-replacement vs accumulation、experimental setting、cross-strategy、controlled setting 等主要限制。\n- **Ethics statement**: 存在（p.10），讨论了潜在滥用风险。\n",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 1 审稿意见\n\n## 论文信息\n**标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 问题定义新颖、实验体量充足，但核心方法在 in-distribution 上与已有 Binoculars 特征持平（p>0.05），在 cross-strategy/cross-scale 上大幅退化，headline 数字被 d0 近完美可分性膨胀，实际深层区分能力（d1-d3）远低于报告值。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心 claim 有部分实验支撑，但 self-reference confound、Binoculars 平局、cross-strategy/scale 失败构成重大方法论缺口 |\n| Excitement | 3.0/5 | 问题定义（ordinal depth estimation）有新意，Degradation Atlas 有系统价值，但方法性能未超越现有 binary detector 特征的简单重用 |\n| Reproducibility | 4/5 | 附录细节充分（超参、硬件、种子），承诺代码/数据公开，但 LoRA pipeline 缺少超参敏感性分析 |\n| Confidence | 4/5 | 熟悉 model collapse、AI text detection、ordinal classification 相关文献 |\n\n---\n\n## 主要优势\n\n**S1. 问题定义新颖且有实际价值。** 将递归生成深度估计形式化为 ordinal classification（Section 3.1），区别于 binary human-vs-machine detection，是一个自然且未被充分探索的方向。这对理解训练数据污染程度有直接意义。\n\n**S2. Degradation Atlas 系统性强。** Section 4 的 atlas（3 families × 3 strategies × 4 depths）提供了关于递归生成如何改变文本统计特性的系统实证图景。Feature consistency 分析（Section 4.2）、monotonicity 分析（Section 4.3）、EDD 分析（Section 4.4）构成了一个有价值的 empirical contribution，独立于分类器性能。\n\n**S3. 评估方案设计合理。** 使用 ordinal-specific metrics（QWK=0.89, MAE=0.23），5-fold stratified CV，bootstrap CI (B=1000)，permutation test，体现了统计素养。CORAL ordinal regression 对照也是恰当的。\n\n**S4. 消融实验覆盖面广。** 附录 B.1-B.29 涵盖了 permutation importance、feature trajectories、per-class recall、DCOL iteration、temperature robustness、generation length、feature group ablation、Binoculars decomposition、domain bias、wild-data calibration、reference model ablation、cross-scale 等多个角度，展现了严肃的实验态度。\n\n**S5. 引用质量高。** 74 篇引用中 63 篇 OpenAlex 验证通过，7 篇 not_found 均为真实论文（OpenAlex 覆盖缺口），无伪造引用。cross-check 显示 0 missing_bib（所有 \\cite 都有对应 bib 条目）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Binoculars 特征平局严重削弱方法论贡献**\n- 具体位置：Section 5.1, Table 4\n- 问题：论文的 19-feature RF 达到 78.4%，而 Binoculars 的 11 features 用相同 RF 达到 78.1%，p>0.05 无显著差异。Merged 30-feature 达到 82.6%，但这说明信息是互补的、而非本文特征优于已有特征。论文声称的部署优势（\"1 reference model vs observer-performer pair\"，Section 5.1）是工程论证而非科学贡献。\n- 为什么影响接收：如果现有 binary detector 的特征简单重新标定（CORAL calibration）就能达到相同 ordinal 性能，则本文 19 个统计特征的设计贡献被大幅稀释。论文的核心 claim \"discriminative signal resides in feature design\"（Section 5.1）恰好被 Binoculars 平局所反驳——信号不在*这些*特征，而在*任何*能捕获分布偏移的特征。\n- 建议修改方向：(1) 在 abstract/intro 诚实报告 Binoculars 平局；(2) 将 contribution 重新定位为\"问题定义 + atlas + benchmark\"而非\"特征设计\"；(3) 分析为何 merged 30-feature 提升 4.2pp——互补信息来自哪里？\n\n**N2** [critical] **Self-reference confound 使 Pythia 结果不可比，膨胀 headline 数字**\n- 具体位置：Section 3.3（reference model = Pythia-1.4B），Table 2（Pythia 行标 †），Appendix B.13（Table 16）\n- 问题：Pythia-1.4B 同时是 generator（3 个 family 之一）和 reference model（特征提取的唯一模型）。Table 2 显示 Pythia 比 OLMo/GPT-2 XL 高 4-11pp。Appendix B.13 的 reference model ablation 显示换用 GPT-2 XL 作 reference 时 accuracy 降至 67.3%（−11pp）。这意味着 headline \"78.4%\" 中 Pythia 行的贡献包含了 self-reference 优势。\n- 为什么影响接收：1/3 的 in-distribution 结果存在系统性偏差。cross-model transfer（Table 5）中 Pythia holdout 行（62.4%）低于 OLMo（69.2%）反映了这一 confound 的传递。如果排除 Pythia 或使用 non-Pythia reference，headline 数字会下降。\n- 建议修改方向：(1) 主实验增加一个 non-overlapping reference model 的全量结果（如 GPT-NeoX）；(2) 报告 \"excluding Pythia\" 的 mean accuracy 作为 conservative estimate；(3) 将 † caveat 从脚注提升到正文讨论。\n\n**N3** [critical] **d0 膨胀 headline 数字，d1-d3 实际性能远低于报告值**\n- 具体位置：Abstract（\"68.9-85.9% accuracy\"），Section 4.1（\"Depth-0 recall exceeds 97%\"），Table 5（cross-model mean 66.4%），Table 6（cross-strategy 59.1%）\n- 问题：d0（人类文本）与 d1+ 的区分本质上是 binary human-vs-machine detection，已被大量现有工作解决。真正有价值的是 d1-d2-d3 的细粒度区分。但 cross-model d1-d3 仅 55.4%（chance 33%），cross-strategy d1-d3 仅 45.9%。Abstract 报告 \"68.9-85.9%\" 和 \"cross-model transfer reaches 66.4%\" 时没有突出 d1-d3 的大幅下降。\n- 为什么影响接收：这是一种 overclaiming——论文标题和 framing 围绕 \"depth estimation\"，但实际方法的深层区分能力接近 chance。读者会被 headline 数字误导。\n- 建议修改方向：(1) Abstract 和 Introduction 必须报告 d1-d3 准确率；(2) 正文中将 d0 结果与 d1-d3 结果明确分开讨论；(3) 承认深层区分是当前方法的主要瓶颈。\n\n**N4** [critical] **Cross-strategy 和 cross-scale 失败动摇方法的泛化 claim**\n- 具体位置：Section 5.3（Table 6, 59.1%），Section 5.4（14B: 50.8%, EDD₀.₇₀=0），Limitations（p.9）\n- 问题：Cross-strategy transfer d1-d3 仅 45.9%（接近 chance 33%），且出现 d1/d2 boundary inversion。z-score normalization 只修复 logistic regression 不修复 RF（Section 5.3），说明不同策略产生了根本不同的深度信号。14B cross-scale mean 50.8%、EDD₀.₇₀=0 意味着方法在更大模型上完全失效。论文在 Limitations 中承认了这些，但 abstract/introduction 的 framing 仍然偏乐观。\n- 为什么影响接收：一个 depth estimation 方法如果只在训练时见过的 strategy 上工作、且无法推广到实际部署的模型规模（7B/14B），其实际应用价值有限。这些不仅是 limitations，而是对核心 claim 的根本质疑。\n- 建议修改方向：(1) Abstract/intro 中对泛化限制进行显著标注，而非仅在 Limitations 提及；(2) 分析 cross-strategy 失败的根本原因——是特征空间不重叠还是 ordinal 结构消失？(3) 为 14B 实验分离至少一个 confound（如用 14B reference model）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **多重共线性与可解释性 claim 的矛盾**\n- 具体位置：Section 3.3（\"VIF>10 for 14-16/19 features\"），Section 4.2（feature importance via Gini/SHAP）\n- 问题：14-16/19 个特征 VIF>10 意味着严重的多重共线性。虽然 RF 对共线性相对鲁棒（就预测而言），但 Gini importance 和 SHAP 在共线性下不稳定——重要性会在相关特征间随机分配。Section 4.2 基于 Gini 和 SHAP 的特征重要性排序在这种共线性下是不可靠的。\n- 建议：(1) 使用 permutation importance（已在 Appendix B.2 做了，结论一致则强化论证）；(2) 对 SHAP 结果增加 caveat；(3) 或者使用降维后的特征子集做可解释性分析。\n\n**W2** [warning] **LoRA 微调超参无 ablation**\n- 具体位置：Section 3.2（\"LoRA (r=16, α=32, lr=2e-4, 3 epochs)\"），Appendix A（Table 7）\n- 问题：LoRA rank、learning rate、epoch 数直接影响生成文本的质量和多样性，进而影响 depth signatures。r=16 是一个特定选择——更高的 rank 产生更接近 full fine-tuning 的效果，可能产生不同的退化模式。论文未提供任何超参敏感性分析。\n- 建议：至少做一个 LoRA rank ablation（r=4, 8, 16, 32），验证 depth signatures 对微调强度的鲁棒性。\n\n**W3** [warning] **BOS-seeded generation 限制生态效度**\n- 具体位置：Section 3.2（generation pipeline），Appendix B.27（Table 29, −13.8pp for prompted generation）\n- 问题：主实验全部使用 BOS-seeded generation（从 BOS token 开始自由生成 512 tokens）。但现实中的递归生成（如 synthetic data pipeline、LLM 辅助写作）几乎都是 prompted generation。Appendix B.27 承认 prompted generation accuracy 下降 13.8pp。这不是边缘问题，而是核心 validity concern。\n- 建议：(1) 将 prompted generation 结果从附录提升到正文；(2) 讨论 BOS-seeded 与 prompted 在什么条件下等价/不等价；(3) 考虑混合 BOS/prompted 的训练数据。\n\n**W4** [warning] **单域 cross-domain 测试不够充分**\n- 具体位置：Section 5.4（\"cross-domain arXiv 74.1%\"），Appendix B.11（Table 13, C4 FPR 34%, FineWeb FPR 17%）\n- 问题：cross-domain 仅测试 arXiv（学术文本，本身有特定的文本统计特征）。WikiText-103 虽然用于 wild-data calibration（B.11），但不是 cross-domain 泛化测试。C4 上 34% 的 FPR 和 FineWeb 上 17% 的 FPR（Table 13）表明方法在非学术 web 文本上产生大量误报。\n- 建议：增加至少 2-3 个域（如 news、social media、code）的 cross-domain 评估，或者将 C4/FineWeb FPR 数据在正文中讨论而非藏在附录。\n\n**W5** [warning] **多重比较未校正**\n- 具体位置：Appendix B.2（\"multiple pairwise comparisons that were not corrected for multiplicity\"），Table 15（paired t-tests）\n- 问题：全文进行了大量统计检验（9 cells 的准确率比较、Table 15 的 pairwise comparisons、各种 ablation 中的 p 值），但均未做 Bonferroni/FDR 校正。Appendix B.2 中论文自己承认了这一点。Table 15 有 6 个 pairwise comparisons，p<0.05 可能仅因多重比较。\n- 建议：对所有包含多组比较的结果应用 Holm-Bonferroni 或 BH-FDR 校正，或者在正文中标注 adjusted p-values。\n\n**W6** [warning] **EDD 阈值 T=0.70 的论证依据不够充分**\n- 具体位置：Section 3.4（Eq. 1），引用 Hosmer & Lemeshow (2000)\n- 问题：T=0.70 引自 Hosmer & Lemeshow 的 AUC discrimination standard，但该标准是为 binary logistic regression 的 c-statistic 设计的，直接迁移到 multi-class ordinal 的 pairwise AUC 缺乏理论依据。虽然 Section 3.4 提供了 T∈{0.65,0.70,0.75,0.80} 的 sensitivity analysis，但没有解释为何 0.70 是 \"natural\" 的。\n- 建议：(1) 讨论为何 binary AUC 的 discrimination 标准可迁移到 ordinal pairwise AUC；(2) 或者提出一个 data-driven 的阈值选择方法。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Orphan bib entries: `dsir2023` 和 `qurating2024` 在 .bib 中定义但未在正文 \\cite，应清理。\n- **M2**: Table 2 脚注 1（\"RF binary classifiers use 500 trees; the main 4-class RF uses 200 trees\"）——为何 binary 和 4-class 用不同数量的树？未见讨论。\n- **M3**: Section 4.3 \"all 12 AUC profiles in our benchmark decay monotonically\" 与 Appendix B.14 中 GPT-2 XL 14B d4→d5 non-monotonic 的发现有 tension——应在正文中注明 monotonicity 仅在 1-1.5B 范围内成立。\n- **M4**: Figure 1 的 atlas heatmap 中颜色强度编码 RF Gini importance，但 W1 中指出的共线性问题意味着这些重要性值不稳定。\n- **M5**: Appendix B.28 \"Cross-strategy conditional decomposition\" 中 naïve pooled classifier 的讨论（\"the two-stage pipeline... yields 11.5pp gain\"）应考虑提到正文，因为它直接说明了 cross-strategy 失败的解决方向。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1**: 如果使用完全不同架构的 reference model（如 Mamba/RWKV 而非 Transformer），特征提取的结果会如何？当前 reference model ablation（B.13）仅在 Transformer LM 内部换模型。\n\n**Q2**: Perplexity tail features 真正捕获的是 \"depth-specific signature\" 还是仅仅是文本质量的代理（quality proxy）？一段由 depth-1 生成但碰巧质量较差的文本，与一段 depth-2 的 \"正常\" 文本，特征能否区分？\n\n**Q3**: Cross-strategy 中 z-score normalization 修复 logistic regression 但不修复 RF 的原因是什么？这是否说明 RF 学到了 strategy-specific 的非线性决策边界，而这些边界在 strategy 间不可迁移？\n\n**Q4**: DCOL iteration（Appendix B.5）中 convergence vs failure 的决定因素是什么？有没有可靠的 stopping criterion？\n\n**Q5**: 14B 实验中 5 个 confounders（Section 5.4）能否通过实验设计分离？例如用 14B 模型做 reference model 提取特征，是否能消除 scale mismatch confound？\n\n---\n\n## Missing References\n\n1. **Min-K%++ (Zhang et al., 2024)**: Min-K% Prob 的改进版本，在 membership inference 上有更好的性能，应作为 baseline 考虑。\n2. **Ordinal classification 综述**: 论文引用了 Frank (2001), McCullagh (1980), Rennie (2005) 等经典工作，但缺少对近年 ordinal classification 在 NLP 中的应用的系统综述引用。\n3. **RAID benchmark (Dugan et al., 2024)**: 虽然已引用，但未在实验中使用其数据或评估框架进行比较——考虑到 RAID 专门为 robustly evaluating detection 设计，解释为何不采用会更好。\n\n---\n\n## 格式合规检查\n\n- **页数**: 正文 8 页（pp.1-8），Limitations 在 p.9 开头，References 从 p.10 开始。符合 EMNLP 2026 的 8 页限制。\n- **匿名**: 使用 `\\usepackage[review]{acl}`，标题页为 \"Anonymous ACL submission\"，正文未见去匿名化内容。符合 double-blind 要求。\n- **Limitations section**: 存在（p.9），覆盖了 full-replacement vs accumulation、experimental setting、cross-strategy、controlled setting 等主要限制。\n- **Ethics statement**: 存在（p.10），讨论了潜在滥用风险。\n",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-20T08:39:53.685229+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4220
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-20T08:39:58.174519+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-20T08:39:58.175293+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-20T08:40:02.858180+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-20T08:40:02.908834+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 862 · 2026-05-20T08:40:11.853459+00:00_

Round 1 审稿完成，已提交给 Review Director。

**核心判断**: Overall 3.0（Findings）。问题定义新颖、实验体量大，但四个 critical 问题影响接收决定：

1. **Binoculars 平局**（78.1% vs 78.4%, p>0.05）——19-feature 设计的增量贡献不成立
2. **Self-reference confound**——Pythia 同时做 generator 和 reference model，1/3 结果存在系统偏差
3. **d0 膨胀 headline**——cross-model d1-d3 仅 55.4%（报告 66.4%），cross-strategy d1-d3 仅 45.9%（报告 59.1%）
4. **Cross-strategy/scale 泛化失败**——14B EDD₀.₇₀=0，方法在实际模型规模上完全失效

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 29

## Round 29

4 recorded events


### User

_source line 863 · 2026-05-20T08:43:16.060460+00:00_

[Round 1 审稿请求]:
# 交叉审稿 — Reviewer 2 的完整审稿意见

请逐条回应 Reviewer 2 的审稿意见。对每个 Must-Fix 和 Should-Fix 问题，请标注：
- **[AGREE]** 同意并简要说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 2 的完整审稿意见：

## 总体评分
**Overall**: 3.0 — Findings

## Must-Fix 问题

**N1** [critical] **Pipeline 缺乏算法创新，贡献主要在 task formalization + empirical characterization**
- 核心 pipeline 是 19 个标准统计特征 + 标准 Random Forest。特征和分类器均为已有方法的直接应用，无算法层面创新。EMNLP 主会议期望至少在方法或理论层面有所推进。纯 benchmark-driven + empirical characterization 的贡献更适合 Findings track。

**N2** [critical] **与 Binoculars 无显著差异（78.1% vs. 78.4%），削弱方法贡献**
- Binoculars 11-feature RF 和 19-feature pipeline 差异仅 −0.3pp。Appendix B.26 feature ablation 显示 Binoculars 6 个 cross-perplexity 特征单独就能达到 75.9%，仅比完整 pipeline 低 2.2pp。读者会合理地问：为什么不直接用 Binoculars？

**N3** [critical] **模型规模严重受限（≤1.5B），2026 年的实用性存疑**
- 主实验仅覆盖 ≤1.5B 模型。14B 扩展实验 EDD_{τ=0.70} 仅为 d1，4-class accuracy 61%。2026 年主流模型 7B-70B+，≤1.5B 结论实用参考价值有限。14B 结果提供"scaling 可能破坏 depth signal"的证据，动摇核心 claim。

## Should-Fix 问题

**W1** Abstract 信息密度过载（10+ 个数字）
**W2** d0 膨胀导致 headline metrics 误导性（同你的 N3）
**W3** Full-replacement 设置与现实场景脱节（accumulation 缺失）
**W4** EDD 指标理论动机薄弱（τ=0.70 选择依据不足，阈值敏感性高）
**W5** Depth Degradation Atlas 贡献独立性存疑（用设计来捕捉 depth signal 的特征来描述 depth signal 的变化——循环性）
**W6** Cross-strategy transfer 严重不足（59.1%），部署前景堪忧

## Minor
- M1: 2 个 orphan bib entries (dsir2023, qurating2024)
- M2: 引用 author 顺序 mismatch（3 个条目）
- M3: 主文过度引用附录，阅读碎片化
- M4: "depth"术语在不同语境含义不同需区分
- M5: Table 1 特征命名需更好说明

## Questions
- Q1: 14B EDD 降至 d1 是否意味着 ≥7B 规模下方法根本不可行？
- Q2: 19-feature pipeline 相对 Binoculars 的实际优势是什么？
- Q3: Temperature d1/d2 boundary inversion 是否使该策略下 estimation 本质不可靠？
- Q4: 主 benchmark 仅 seed=42，能否提供 multi-seed 结果？
- Q5: surprisal variance 和 perplexity tail 是否只是同一信号的不同视角？

## Missing References
1. **[critical]** Markovian Generation Chains in Large Language Models (arxiv:2603.11228, ICLR 2026) — 直接研究 LLM 迭代处理的 Markov 链动态
2. [minor] 更强的 neural ordinal methods（proportional odds model 等）
3. [minor] PAN 2026 / M4-SemEval 的评估协议讨论

## EMNLP 适合度
Reviewer 2 认为：benchmark paper + empirical characterization 更符合 Findings 定位。Long Paper format 合理（内容量支撑）。

---

请对以上每个 Must-Fix（N1-N3）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-20T08:45:07.587535+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: Pipeline 缺乏算法创新**\n\n同意。核心 pipeline（19 个统计特征 + RF）在技术层面确实无新方法。特征集由标准 perplexity/surprisal/lexical/repetition 统计量组成（Table 1），分类器是 off-the-shelf RF（200 trees, Section 3.4）。Section 5.1 自己也验证了 RF/XGBoost/LightGBM 在 0.4pp 内收敛，进一步证实信号在特征不在分类器——但这同时意味着分类器选择无技术门槛。\n\n补充我的发现：Binoculars 平局（N2）进一步加剧了这一问题。如果已有 detector 的特征重组就能达到相同性能，则连特征设计的贡献也被稀释。论文的真正贡献在于：(1) 问题形式化（ordinal depth estimation，Section 3.1 的 Definition 1）；(2) Degradation Atlas 的系统 empirical characterization（Section 4）；(3) 180K benchmark 构建。这些确实更符合 Findings 定位。\n\n**[AGREE] R2-N2: 与 Binoculars 无显著差异**\n\n完全同意，与我的 N1 一致。补充两点证据：\n\n1. Appendix B.26（Table 26）中 Binoculars 6 个 cross-perplexity 特征单独达到 75.9%，是论文 19-feature pipeline（78.4%）的 96.8%。而 Binoculars 的完整 11 特征达到 78.1%，p>0.05。这说明 observer-performer divergence 已足以捕获 depth signal 的主要部分。\n\n2. Merged 30-feature 达到 82.6%（+4.2pp），Table 26 分解显示 6 个 shared perplexity features 贡献 75.9%，本文独有的 13 个特征仅额外贡献 +2.5pp，Binoculars 独有的 5 个特征贡献 +4.2pp（从 78.4% 到 82.6%）。这意味着 Binoculars 独有特征的边际贡献反而**大于**本文独有特征——进一步削弱了特征设计的方法论贡献。\n\nR2 的质疑\"为什么不直接用 Binoculars\"是合理的。论文的 deployment 论证（Section 5.1, \"single reference model\"）是工程优势而非科学贡献。\n\n**[AGREE] R2-N3: 模型规模限制（≤1.5B）**\n\n同意核心论断，但对表述程度有保留。\n\n同意的部分：2026 年 ≤1.5B 模型确实不是主流 generator。14B 实验（Section 5.4, Appendix B.14）mean 50.8%, EDD₀.₇₀=0 是致命的实验结果。Section 5.4 列出的 5 个 confounders（instruction-tuning, self-reference, architecture shift, BPE mismatch, unknown training data）使得无法从 14B 失败中得出有用结论——既不能说方法失败，也不能说方法可行，这本身就是问题。\n\n保留的部分：R2 称 \"14B 结果提供 scaling 可能破坏 depth signal 的证据\"——我认为措辞应更审慎。由于 5 个 confounders 未分离，我们不知道是 scaling 破坏了 depth signal，还是 instruction-tuning / self-reference / architecture 等因素导致的。Appendix B.14 中 Llama-3.1-8B 在 instruct 变体上\"monotonicity breaks at d4\"而 base model 保持 monotonic decay（Table 17），这暗示 instruction-tuning 而非 scale 可能是更大的 confound。\n\n建议作者分离实验：例如对 Pythia-6.9B（同架构、无 instruction-tuning）做完整测试，可隔离 scale 因素。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract 信息密度过载**\n\n同意。Abstract 包含至少 12 个数字（78.4%, MAE=0.23, QWK=0.89, 66.4%, 59.1%, 74.1%, 82.6%, 50.8%, 19, 180K, 4, 3 等），信息密度过高。更重要的是，这些数字中部分因 d0 膨胀（我的 N3）和 self-reference confound（我的 N2）而具有误导性。\n\n建议：Abstract 聚焦于 (1) 问题定义 (2) 关键方法洞见 (3) 最重要的 1-2 个 takeaway 数字（附带 d1-d3 caveat）。\n\n**[AGREE] R2-W2: d0 膨胀导致 headline metrics 误导性**\n\n完全同意，与我的 N3 一致。d0 recall >97%（Section 4.1, Table 8 in Appendix B.4）本质上是 binary human-vs-machine detection 的已解决问题。Cross-model headline 66.4% 在排除 d0 后降至 55.4%，cross-strategy 59.1% 降至 45.9%（Section 5.2-5.3 中的 d1-d3 报告）。论文标题和核心 claim 围绕 \"depth estimation\" 而非 \"detection\"，因此 d1-d3 性能才是真正的贡献度量。\n\n**[AGREE] R2-W3: Full-replacement 设置与现实脱节**\n\n同意。论文 Limitations（p.9）承认\"full-replacement recursive chains where each depth fully replaces the prior training corpus\"是简化设置，现实中更多是 accumulation（混合真实数据和合成数据）。Gerstgrasser et al. (2024) 已证明 accumulation 显著缓解 model collapse——如果 accumulation 也缓解了统计 fingerprint 的深度差异，则本文方法的 applicability 进一步受限。\n\n不过需要指出，Limitations 中的讨论是公开透明的：\"Our results therefore represent an upper bound on depth discriminability\"（p.9）。问题不在于缺乏 awareness，而在于主实验未包含任何 accumulation 条件下的评估数据。\n\n**[REBUT] R2-W5: Degradation Atlas 贡献独立性存疑（循环性指控）**\n\n不同意 R2 的 \"循环性\" 论断。\n\nR2 的论点是：用设计来捕捉 depth signal 的特征来描述 depth signal 的变化构成逻辑循环。但这混淆了\"测量工具\"与\"测量发现\"。\n\n1. **特征是测量工具，Atlas 是测量发现。** 19 个特征是 text 的统计属性（perplexity percentiles, surprisal variance, type-token ratio, n-gram repetition 等），它们不预设 depth signal 的存在——人类文本同样有这些属性值。Atlas 的发现是这些属性**如何随 depth 系统性变化**，包括：哪些属性 monotonically decay（Section 4.3, perplexity tail），哪些先降后升（lexical diversity 在某些策略下），哪些对 strategy 敏感（temperature vs nucleus 产生不同 trajectory shapes, Section 4.5）。这些 pattern 是 empirical finding，不是循环推理。\n\n2. **Atlas 的反面发现证明非循环。** 如果是循环的，所有特征应都显示强 depth signal。但 Atlas 恰恰发现某些特征**不**随 depth 单调变化：Section 4.2 报告 repetition features 在 top-k 下 importance 低于其他策略；Section 4.3 报告某些 model-strategy cells 的 monotonicity breaks。这些\"负面发现\"不可能从循环论证中产出。\n\n3. **Atlas 对非本文特征同样有价值。** Atlas 的 methodology（系统性地 sweep model × strategy × depth 并报告 feature trajectories）可用于任何统计特征集。即使用 Binoculars 特征做同样的 atlas，发现仍然有价值。\n\n因此 Atlas 是一个 legitimate empirical contribution，不存在循环性问题。\n\n**[AGREE] R2-W4: EDD 指标理论动机薄弱**\n\n同意，与我的 W6 一致。τ=0.70 借自 Hosmer & Lemeshow (2000) 的 binary logistic regression AUC 判别标准（Section 3.4），但 EDD 是基于 ordinal pairwise AUC 的指标，两者的统计性质不同。Section 3.4 的 sensitivity analysis（T∈{0.65,0.70,0.75,0.80}）显示 T=0.80 时多个 cell 丢失一个 depth level（\"several cells lose one depth level\"，Limitations p.9），这暗示结论对阈值敏感。\n\n补充：EDD 的 monotonicity assumption（Definition 1, \"EDD_τ reports the longest contiguous prefix\"）要求相邻 depth 的 AUC 单调递减。Section 4.3 报告\"the sole non-monotonic case\"在 1-1.5B 范围内仅出现一次，但 14B 实验（B.14）中 monotonicity 频繁打破。如果 monotonicity 在 larger scale 不成立，EDD 的适用范围被进一步限制。\n\n**[AGREE] R2-W6: Cross-strategy transfer 严重不足**\n\n完全同意，与我的 N4 一致。补充一个 R2 未提及的发现：Section 5.3 报告 z-score normalization 修复了 logistic regression 的 cross-strategy 性能但**不修复 RF**。这说明 RF 的 cross-strategy 失败不仅是 feature scale 问题，而是因为 RF 学到了 strategy-specific 的非线性决策边界，这些边界在策略间不可迁移。这比单纯的 \"accuracy 低\" 更令人担忧——它暗示不同解码策略产生了**结构性不同**的 depth signal，而非仅是量表偏移。\n\nAppendix B.28 的 cross-strategy conditional decomposition 提出了两阶段 pipeline 作为缓解方案（先识别 strategy 再分别分类），但这需要额外的 strategy 标注，降低了方法的实用性。\n\n---\n\n## Questions 回应\n\n**R2-Q1（14B EDD 降至 d1 → ≥7B 不可行？）**: 证据不足以下此结论——5 个未分离的 confounders 意味着我们不知道是 scale 本身还是其他因素导致失败。Appendix B.14 Table 17 中 base model 与 instruct 变体的差异暗示 instruction-tuning 是更大的 confound。需要 controlled experiment（如 Pythia-6.9B base）来回答。\n\n**R2-Q2（19-feature vs Binoculars 优势？）**: 基于我的分析，科学优势不存在（p>0.05）。唯一优势是工程层面的（1 model vs 2 models）。Merged 30-feature 的 +4.2pp 提示正确方向是融合而非替代。\n\n**R2-Q3（Temperature boundary inversion → 本质不可靠？）**: 同意这是严重问题。Section 4.5 和 5.3 的讨论表明 temperature scaling 压缩 inter-depth distance，使 d1/d2 边界消失。但论文也报告在 temperature 下 d0-vs-d3 仍可分（Appendix B.7, Table 10），所以不是完全不可靠，而是 fine-grained depth 在该策略下不可解。\n\n**R2-Q4（Multi-seed？）**: 合理要求。Appendix B.24（Table 25）提供了 3 个 RF seed（42, 123, 456）的结果，std=0.06pp，但这只是 classifier seed。Data generation seed 未做 ablation，这是更大的 concern——不同 generation seed 可能产生不同质量的合成数据。\n\n**R2-Q5（surprisal variance vs perplexity tail 是否同一信号？）**: 部分同意。Section 4.2 报告 p50_ppl 和 var_surprisal 的 Spearman correlation 为 0.81（Appendix B.2），表明高度共线性。但 permutation importance（Appendix B.2）显示两者独立贡献 rank 在 top-5 中稳定出现，suggesting 不完全冗余。VIF>10 的共线性问题（我的 W1）使得这个问题无法从 importance 角度清晰回答。\n\n---\n\n## Missing References 回应\n\n**R2-MR1（Markovian Generation Chains, arxiv:2603.11228）**: 我未独立搜索到此引用。如果存在且直接研究 LLM 迭代生成的 Markov 链动态，确实与本文高度相关，应引用。建议 Director 验证此引用的真实性。\n\n**R2-MR2/MR3**: 同意 proportional odds model 应在 Related Work 讨论（当前仅在 Appendix B.25 引用 McCullagh 1980）。PAN 2026 已被引用（bevendorff2026_pan），但评估协议未被讨论。\n",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: Pipeline 缺乏算法创新**\n\n同意。核心 pipeline（19 个统计特征 + RF）在技术层面确实无新方法。特征集由标准 perplexity/surprisal/lexical/repetition 统计量组成（Table 1），分类器是 off-the-shelf RF（200 trees, Section 3.4）。Section 5.1 自己也验证了 RF/XGBoost/LightGBM 在 0.4pp 内收敛，进一步证实信号在特征不在分类器——但这同时意味着分类器选择无技术门槛。\n\n补充我的发现：Binoculars 平局（N2）进一步加剧了这一问题。如果已有 detector 的特征重组就能达到相同性能，则连特征设计的贡献也被稀释。论文的真正贡献在于：(1) 问题形式化（ordinal depth estimation，Section 3.1 的 Definition 1）；(2) Degradation Atlas 的系统 empirical characterization（Section 4）；(3) 180K benchmark 构建。这些确实更符合 Findings 定位。\n\n**[AGREE] R2-N2: 与 Binoculars 无显著差异**\n\n完全同意，与我的 N1 一致。补充两点证据：\n\n1. Appendix B.26（Table 26）中 Binoculars 6 个 cross-perplexity 特征单独达到 75.9%，是论文 19-feature pipeline（78.4%）的 96.8%。而 Binoculars 的完整 11 特征达到 78.1%，p>0.05。这说明 observer-performer divergence 已足以捕获 depth signal 的主要部分。\n\n2. Merged 30-feature 达到 82.6%（+4.2pp），Table 26 分解显示 6 个 shared perplexity features 贡献 75.9%，本文独有的 13 个特征仅额外贡献 +2.5pp，Binoculars 独有的 5 个特征贡献 +4.2pp（从 78.4% 到 82.6%）。这意味着 Binoculars 独有特征的边际贡献反而**大于**本文独有特征——进一步削弱了特征设计的方法论贡献。\n\nR2 的质疑\"为什么不直接用 Binoculars\"是合理的。论文的 deployment 论证（Section 5.1, \"single reference model\"）是工程优势而非科学贡献。\n\n**[AGREE] R2-N3: 模型规模限制（≤1.5B）**\n\n同意核心论断，但对表述程度有保留。\n\n同意的部分：2026 年 ≤1.5B 模型确实不是主流 generator。14B 实验（Section 5.4, Appendix B.14）mean 50.8%, EDD₀.₇₀=0 是致命的实验结果。Section 5.4 列出的 5 个 confounders（instruction-tuning, self-reference, architecture shift, BPE mismatch, unknown training data）使得无法从 14B 失败中得出有用结论——既不能说方法失败，也不能说方法可行，这本身就是问题。\n\n保留的部分：R2 称 \"14B 结果提供 scaling 可能破坏 depth signal 的证据\"——我认为措辞应更审慎。由于 5 个 confounders 未分离，我们不知道是 scaling 破坏了 depth signal，还是 instruction-tuning / self-reference / architecture 等因素导致的。Appendix B.14 中 Llama-3.1-8B 在 instruct 变体上\"monotonicity breaks at d4\"而 base model 保持 monotonic decay（Table 17），这暗示 instruction-tuning 而非 scale 可能是更大的 confound。\n\n建议作者分离实验：例如对 Pythia-6.9B（同架构、无 instruction-tuning）做完整测试，可隔离 scale 因素。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract 信息密度过载**\n\n同意。Abstract 包含至少 12 个数字（78.4%, MAE=0.23, QWK=0.89, 66.4%, 59.1%, 74.1%, 82.6%, 50.8%, 19, 180K, 4, 3 等），信息密度过高。更重要的是，这些数字中部分因 d0 膨胀（我的 N3）和 self-reference confound（我的 N2）而具有误导性。\n\n建议：Abstract 聚焦于 (1) 问题定义 (2) 关键方法洞见 (3) 最重要的 1-2 个 takeaway 数字（附带 d1-d3 caveat）。\n\n**[AGREE] R2-W2: d0 膨胀导致 headline metrics 误导性**\n\n完全同意，与我的 N3 一致。d0 recall >97%（Section 4.1, Table 8 in Appendix B.4）本质上是 binary human-vs-machine detection 的已解决问题。Cross-model headline 66.4% 在排除 d0 后降至 55.4%，cross-strategy 59.1% 降至 45.9%（Section 5.2-5.3 中的 d1-d3 报告）。论文标题和核心 claim 围绕 \"depth estimation\" 而非 \"detection\"，因此 d1-d3 性能才是真正的贡献度量。\n\n**[AGREE] R2-W3: Full-replacement 设置与现实脱节**\n\n同意。论文 Limitations（p.9）承认\"full-replacement recursive chains where each depth fully replaces the prior training corpus\"是简化设置，现实中更多是 accumulation（混合真实数据和合成数据）。Gerstgrasser et al. (2024) 已证明 accumulation 显著缓解 model collapse——如果 accumulation 也缓解了统计 fingerprint 的深度差异，则本文方法的 applicability 进一步受限。\n\n不过需要指出，Limitations 中的讨论是公开透明的：\"Our results therefore represent an upper bound on depth discriminability\"（p.9）。问题不在于缺乏 awareness，而在于主实验未包含任何 accumulation 条件下的评估数据。\n\n**[REBUT] R2-W5: Degradation Atlas 贡献独立性存疑（循环性指控）**\n\n不同意 R2 的 \"循环性\" 论断。\n\nR2 的论点是：用设计来捕捉 depth signal 的特征来描述 depth signal 的变化构成逻辑循环。但这混淆了\"测量工具\"与\"测量发现\"。\n\n1. **特征是测量工具，Atlas 是测量发现。** 19 个特征是 text 的统计属性（perplexity percentiles, surprisal variance, type-token ratio, n-gram repetition 等），它们不预设 depth signal 的存在——人类文本同样有这些属性值。Atlas 的发现是这些属性**如何随 depth 系统性变化**，包括：哪些属性 monotonically decay（Section 4.3, perplexity tail），哪些先降后升（lexical diversity 在某些策略下），哪些对 strategy 敏感（temperature vs nucleus 产生不同 trajectory shapes, Section 4.5）。这些 pattern 是 empirical finding，不是循环推理。\n\n2. **Atlas 的反面发现证明非循环。** 如果是循环的，所有特征应都显示强 depth signal。但 Atlas 恰恰发现某些特征**不**随 depth 单调变化：Section 4.2 报告 repetition features 在 top-k 下 importance 低于其他策略；Section 4.3 报告某些 model-strategy cells 的 monotonicity breaks。这些\"负面发现\"不可能从循环论证中产出。\n\n3. **Atlas 对非本文特征同样有价值。** Atlas 的 methodology（系统性地 sweep model × strategy × depth 并报告 feature trajectories）可用于任何统计特征集。即使用 Binoculars 特征做同样的 atlas，发现仍然有价值。\n\n因此 Atlas 是一个 legitimate empirical contribution，不存在循环性问题。\n\n**[AGREE] R2-W4: EDD 指标理论动机薄弱**\n\n同意，与我的 W6 一致。τ=0.70 借自 Hosmer & Lemeshow (2000) 的 binary logistic regression AUC 判别标准（Section 3.4），但 EDD 是基于 ordinal pairwise AUC 的指标，两者的统计性质不同。Section 3.4 的 sensitivity analysis（T∈{0.65,0.70,0.75,0.80}）显示 T=0.80 时多个 cell 丢失一个 depth level（\"several cells lose one depth level\"，Limitations p.9），这暗示结论对阈值敏感。\n\n补充：EDD 的 monotonicity assumption（Definition 1, \"EDD_τ reports the longest contiguous prefix\"）要求相邻 depth 的 AUC 单调递减。Section 4.3 报告\"the sole non-monotonic case\"在 1-1.5B 范围内仅出现一次，但 14B 实验（B.14）中 monotonicity 频繁打破。如果 monotonicity 在 larger scale 不成立，EDD 的适用范围被进一步限制。\n\n**[AGREE] R2-W6: Cross-strategy transfer 严重不足**\n\n完全同意，与我的 N4 一致。补充一个 R2 未提及的发现：Section 5.3 报告 z-score normalization 修复了 logistic regression 的 cross-strategy 性能但**不修复 RF**。这说明 RF 的 cross-strategy 失败不仅是 feature scale 问题，而是因为 RF 学到了 strategy-specific 的非线性决策边界，这些边界在策略间不可迁移。这比单纯的 \"accuracy 低\" 更令人担忧——它暗示不同解码策略产生了**结构性不同**的 depth signal，而非仅是量表偏移。\n\nAppendix B.28 的 cross-strategy conditional decomposition 提出了两阶段 pipeline 作为缓解方案（先识别 strategy 再分别分类），但这需要额外的 strategy 标注，降低了方法的实用性。\n\n---\n\n## Questions 回应\n\n**R2-Q1（14B EDD 降至 d1 → ≥7B 不可行？）**: 证据不足以下此结论——5 个未分离的 confounders 意味着我们不知道是 scale 本身还是其他因素导致失败。Appendix B.14 Table 17 中 base model 与 instruct 变体的差异暗示 instruction-tuning 是更大的 confound。需要 controlled experiment（如 Pythia-6.9B base）来回答。\n\n**R2-Q2（19-feature vs Binoculars 优势？）**: 基于我的分析，科学优势不存在（p>0.05）。唯一优势是工程层面的（1 model vs 2 models）。Merged 30-feature 的 +4.2pp 提示正确方向是融合而非替代。\n\n**R2-Q3（Temperature boundary inversion → 本质不可靠？）**: 同意这是严重问题。Section 4.5 和 5.3 的讨论表明 temperature scaling 压缩 inter-depth distance，使 d1/d2 边界消失。但论文也报告在 temperature 下 d0-vs-d3 仍可分（Appendix B.7, Table 10），所以不是完全不可靠，而是 fine-grained depth 在该策略下不可解。\n\n**R2-Q4（Multi-seed？）**: 合理要求。Appendix B.24（Table 25）提供了 3 个 RF seed（42, 123, 456）的结果，std=0.06pp，但这只是 classifier seed。Data generation seed 未做 ablation，这是更大的 concern——不同 generation seed 可能产生不同质量的合成数据。\n\n**R2-Q5（surprisal variance vs perplexity tail 是否同一信号？）**: 部分同意。Section 4.2 报告 p50_ppl 和 var_surprisal 的 Spearman correlation 为 0.81（Appendix B.2），表明高度共线性。但 permutation importance（Appendix B.2）显示两者独立贡献 rank 在 top-5 中稳定出现，suggesting 不完全冗余。VIF>10 的共线性问题（我的 W1）使得这个问题无法从 importance 角度清晰回答。\n\n---\n\n## Missing References 回应\n\n**R2-MR1（Markovian Generation Chains, arxiv:2603.11228）**: 我未独立搜索到此引用。如果存在且直接研究 LLM 迭代生成的 Markov 链动态，确实与本文高度相关，应引用。建议 Director 验证此引用的真实性。\n\n**R2-MR2/MR3**: 同意 proportional odds model 应在 Related Work 讨论（当前仅在 Appendix B.25 引用 McCullagh 1980）。PAN 2026 已被引用（bevendorff2026_pan），但评估协议未被讨论。\n",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-20T08:45:11.862054+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4274
}
```

</details>

---


### Assistant

_source line 866 · 2026-05-20T08:45:21.392482+00:00_

交叉回应已提交。总结：

- **N1-N3**: 全部 [AGREE]。算法创新不足、Binoculars 平局、规模限制三个问题与我的独立发现一致，共同指向 Findings 定位。
- **W1-W4, W6**: [AGREE]。d0 膨胀、full-replacement 脱节、EDD 理论动机薄弱、cross-strategy 失败均与我的 review 吻合。
- **W5（Atlas 循环性）**: [REBUT]。R2 混淆了测量工具与测量发现——Atlas 中的负面发现（某些特征不随 depth 单调变化）恰好证明了非循环性。Atlas 是独立的 empirical contribution。

两位 Reviewer 的核心共识：问题定义有价值，但方法性能（尤其是与 Binoculars 持平、cross-strategy/scale 失败、d0 膨胀 headline）不足以支撑 Main Conference，Findings 更合适。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 30

## Round 30

80 recorded events


### User

_source line 867 · 2026-05-20T14:02:05.648441+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计**。

## Venue 信息
- **目标会议**: EMNLP 2026（通过 ARR May cycle 提交）
- **截止日期**: 2026-06-15
- **页数限制**: 长文 8 页正文（参考文献不限；Limitations 和 Ethics 不计入页数）
- **模板**: ACL format (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind（提交必须匿名化）
- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

## 论文路径
- LaTeX 主文件: `docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`
- 补充材料: `artifacts/supplementary/README.md`

## 你的审查侧重

请重点审查以下方面：

### 1. 实验方法论与统计分析
- 180K benchmark 构建的科学性（LoRA 微调 pipeline、BOS-seeded generation 的影响）
- 19 特征 RF pipeline 的统计合理性：多重共线性（VIF>10 for 14-16/19 features）对 Gini/SHAP importance 的影响
- 5-fold CV 设计：是否存在数据泄露（跨深度无 passage lineage）
- 多重比较是否需要校正（论文脚注声明 p-values 为 exploratory）

### 2. Self-Reference Confound
- Pythia-1.4B 同时做 generator 和 reference model（1/3 结果），4-11pp 优势
- 这对 headline 数字和 cross-cell 比较的影响程度
- Appendix B.13 ablation 是否充分缓解

### 3. 泛化实验
- Cross-model transfer (66.4%, d1-d3: 55.4%) 的实际意义
- Cross-strategy transfer (59.1%, d1-d3: 45.9%) — 是否接近 chance (33%)？
- Cross-scale (14B: EDD=0, mean 50.8%) — 5 个 confounds 是否致命？
- Cross-domain (arXiv 74.1%) 和 wild-data FPR (C4 34%, FineWeb 17%)

### 4. EDD 指标
- T=0.70 阈值从 binary AUC 标准迁移的合理性
- 阈值敏感性：T=0.80 时多个 cell 丢失 depth level
- Monotonicity 假设的限制（14B 和 cross-strategy 违反）

### 5. Baseline 比较
- 与 Binoculars 11-feat RF 的关系：78.1% vs 78.4% (p>0.05)——如果两个独立特征集达到相同性能，方法贡献在哪里？
- Merged 30-feat 82.6% 说明什么？
- DeBERTa/RoBERTa end-to-end 为何大幅落后 RF？

### 6. 格式合规
- 8 页正文限制
- 匿名化
- Limitations 和 Ethics 是否齐全

请按以下结构输出你的审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条)
3. **Weaknesses** (逐条，标注 Must-Fix / Should-Fix / Minor)
4. **Questions** (给作者的问题)
5. **Missing References** (遗漏的重要相关工作)
6. **Minor Issues** (格式、typo 等)
7. **Overall Assessment** (评分 + 理由)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-20T14:02:14.481460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-20T14:02:15.234910+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-20T14:02:15.436183+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-20T14:02:15.486766+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-20T14:02:20.868327+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "project": "recursive_gen_depth_est",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "project": "recursive_gen_depth_est",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 873 · 2026-05-20T14:02:21.473759+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-20T14:02:21.878497+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-20T14:02:22.480916+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 550.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.9}], \"total_pages\": 25, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1612
}
```

</details>

---


### Tool result

_source line 876 · 2026-05-20T14:02:30.240000+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here is information about EMNLP 2026 call for papers submission guidelines related to ARR:

## Key Submission Guidelines

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. The conference has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Submission Process

Papers must be submitted, at latest, by the ARR 2026 May cycle. The ARR submission deadline for long and short papers is May 25, 2026, wi
…[truncated 709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8361
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-20T14:02:32.098245+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Review Form Criteria

The review form includes specific guidance on different recommendation levels:

- 5 = Consider for Award: Papers that 
…[truncated 1003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10624
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-20T14:02:37.523074+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions, scoring scales (1-5), descriptions for each score level, and any guidance text for reviewers. Include soundness, excitement, overall assessment, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all dimensions, scoring scales (1-5), descriptions for each score level, and any guidance text for reviewers. Include soundness, excitement, overall assessment, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 879 · 2026-05-20T14:02:38.026487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-20T14:02:38.529678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-20T14:02:39.084605+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-20T14:02:39.541100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-20T14:02:39.592498+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1062
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-20T14:02:39.592967+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-20T14:02:40.821723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1280
}
```

</details>

---


### Tool result

_source line 886 · 2026-05-20T14:02:40.923179+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1330
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-20T14:02:47.406354+00:00_

# ACL Rolling Review Form - Complete Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness** (1-5 scale)
Evaluates scientific rigor, claim support, and methodological validity:
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement** (1-5 scale)
Subjective assessment of innovation and impact:
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment** (1-5 scale)
Publication recommendation:
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award."
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions."
- **1**: 
…[truncated 2128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9883
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-20T14:02:51.777146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 889 · 2026-05-20T14:02:52.231934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 890 · 2026-05-20T14:02:53.138245+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 891 · 2026-05-20T14:02:53.139213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-20T14:02:53.292838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-20T14:02:53.899050+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1667
}
```

</details>

---


### Tool result

_source line 894 · 2026-05-20T14:02:54.758081+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1618
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-20T14:02:55.046822+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1753
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-20T14:03:00.879862+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "project": "recursive_gen_depth_est",
  "pages": "9-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "project": "recursive_gen_depth_est",
    "pages": "9-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 897 · 2026-05-20T14:03:01.482185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/supplementary/README.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/supplementary/README.md"
  }
}
```

</details>

---


### Tool result

_source line 898 · 2026-05-20T14:03:01.934234+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.0}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 584.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 584.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 553.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 424.4}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.9}], \"total_pages\": 25, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-20T14:03:01.934756+00:00_

1	# Supplementary Material: Recursive Generation Depth Estimation
2	
3	## Repository Structure
4	
5	```
6	├── scripts/                    # Pipeline and evaluation scripts
7	│   ├── lora_finetune.py        # LoRA fine-tuning (r=16, α=32, 3 epochs)
8	│   ├── generate_next_depth.py  # BOS-seeded generation for next depth
9	│   ├── run_pipeline.sh         # End-to-end pipeline (Pythia nucleus)
10	│   ├── run_pipeline_*.sh       # Per-cell pipeline variants (9 cells)
11	│   ├── atlas_analysis.py       # Atlas feature importance analysis
12	│   ├── d4_extension_eval*.py   # Depth extension (d4-d5) evaluation
13	│   ├── baseline_*.py           # Baseline methods (CORAL, DivEye, CE, ppl regression, zero-shot LLM)
14	│   ├── detection_baselines.py  # DetectGPT / Min-K% Prob baselines
15	│   └── prompted_generation_eval.py  # Topic-seeded generation validation
16	├── src/                        # Core analysis modules
17	│   ├── atlas_v2.py             # 9-cell atlas construction and RF training
18	│   ├── cross_model_loo.py      # Leave-one-model-family-out transfer
19	│   ├── binary_pairwise_eval.py # Pairwise AUC for EDD computation
20	│   ├── wild_data_calibration.py # Cross-domain FPR (C4, FineWeb, WikiText)
21	│   ├── w2_domain_bias.py       # LOGO / seed-group domain bias control
22	│   └── curation_poc.py         # Depth-graduated curation probe
23	├── docs/paper/                 # LaTeX source
24	│   ├── main.tex                # Main document
25	│   ├── section_appendix.tex    # Appendix (B.1-B.21)
26	│   └── figures/                # PDF figures (4 main + appendix)
27	└── artifacts/                  # Experiment outputs and analysis
28	```
29	
30	## Data Access
31	
32	**Seed corpus**: Wikipedia subset (English), publicly available.
33	
34	**Generated data**: 180K samples across 9 model-strategy cells (3 models × 3 strategies × 4 depths × 5,000 samples). Feature files (19-dimensional vectors per passage) will be released upon acceptance.
35	
36	**Models used**:
37	
…[truncated 3067 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-20T14:03:05.460980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 901 · 2026-05-20T14:03:05.963399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 902 · 2026-05-20T14:03:06.567839+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1106
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-20T14:03:06.669510+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---
