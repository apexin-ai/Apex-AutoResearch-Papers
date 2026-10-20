# Reviewer 2 coordination — Part 3 of 3

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-2-coordination.md) · [Structured JSON](../../../sessions/c9/c95db014e7f41ee38e2b.json)

## Round 27

### Tool result

_source line 1090 · 2026-05-25T21:17:38.644670+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 405.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_ima
…[truncated 1002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6981
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-25T21:17:38.645155+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\graphicspath{{../../artifacts/figures/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{amsthm}
14	\usepackage{algorithm}
15	\usepackage{algorithmic}
16	\usepackage{booktabs}
17	\usepackage{multirow}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	\setlength{\textfloatsep}{6pt plus 2pt minus 2pt}
30	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
31	\setlength{\abovecaptionskip}{4pt plus 1pt minus 1pt}
32	\setlength{\belowcaptionskip}{0pt}
33	\title{When Does Detect-and-Reweight Work for Synthetic Contamination?}
34	
35	\author{Anonymous}
36	
37	\begin{document}
38	\maketitle
39	
40	\begin{abstract}
41	\input{sections/abstract}
42	\end{abstract}
43	
44	\section{Introduction}
45	\label{sec:intro}
46	\input{sections/introduction}
47	
48	\section{Related Work}
49	\label{sec:related}
50	\input{sections/related_work}
51	
52	\section{Method}
53	\label{sec:method}
54	\input{sections/method}
55	
56	\section{Experimental Setup}
57	\label{sec:experiments}
58	\input{sections/experiments}
59	
60	\section{Results}
61	\label{sec:results}
62	\input{sections/results}
63	
64	\section{Discussion}
65	\label{sec:discussion}
66	\input{sections/discussion}
67	
68	\section{Conclusion}
69	\label{sec:conclusion}
70	\input{sections/conclusion}
71	
72	\section*{Limitations}
73	\label{sec:limitations}
74	\input{sections/limitations}
75	
76	\bibliography{references}
77	
78	\appendix
79	\input{sections/appendix}
80	
81	\end{document}
82	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6730
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-25T21:17:45.475252+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidance for each criterion. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidance for each criterion. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 1093 · 2026-05-25T21:17:45.827047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1094 · 2026-05-25T21:17:46.228527+00:00_

1	As synthetic text pervades web corpora, detect-and-reweight methods that downweight likely-synthetic samples during training have emerged to prevent model collapse, yet when they actually help remains unclear.
2	We investigate this question through controlled continued-pretraining experiments (Qwen3-0.6B, 132M tokens, 5 seeds) and identify three effectiveness conditions.
3	First, detect-and-remove (D\&R) outperforms all reweighting methods in our setting; epoch-matched controls attribute over 95\% of the advantage to multi-epoch exposure on filtered data, identifying the mechanism behind D\&R's effectiveness.
4	Second, the detector must provide both sufficient discrimination \emph{and} good calibration; high-AUC detectors with poor calibration degrade performance below uniform training.
5	Third, minimum intervention, applying the smallest reweighting exponent that meets a quality floor, outperforms unconstrained weight maximization.
6	As an illustrative application of the minimum-intervention principle, we derive a dual-constrained adaptive exponent $\bstar$ that improves over uniform training at contamination ratios $\rho \geq 0.4$, reaching conventional significance after multiple-comparison correction, while requiring no per-model tuning.
7	These findings apply within our self-contamination setup at 0.6B scale; generalization to cross-model contamination and larger models remains to be established\footnote{Code and data are available at \url{https://anonymous.4open.science/r/provenance_weight_training-F72D/}.}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1095 · 2026-05-25T21:17:46.228996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1096 · 2026-05-25T21:17:47.231930+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	\begin{figure*}[t]
6	\centering
7	\includegraphics[width=\textwidth]{fig1_overview}
8	\caption{Three effectiveness conditions for detect-and-reweight.
9	\textbf{(a)}~D\&R achieves the best raw PPL; epoch-matched controls reveal that multi-epoch exposure on filtered data accounts for the bulk of the advantage (\S\ref{sec:results}).
10	\textbf{(b)}~Only detectors with both high AUC \emph{and} low ECE fall in the effective zone; comparable AUC with poor calibration degrades PPL below uniform.
11	\textbf{(c)}~Adaptive $\bstar{\approx}0.9$ operates near the grid-search optimum, while ESS-only $b{\approx}3.5$ falls in the degradation zone.}
12	\label{fig:overview}
13	\end{figure*}
14	
15	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
16	What mechanism drives D\&R's strong performance, and how does it compare to soft reweighting under controlled conditions?
17	What detector properties are necessary for effective reweighting?
18	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
19	
20	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 5 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
21	To ground the analysis of exponent selection, we impleme
…[truncated 1838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1002
}
```

</details>

---


### Tool call

_source line 1097 · 2026-05-25T21:17:47.282531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1098 · 2026-05-25T21:17:47.734062+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality inevitably degrades without fresh real data.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng2025contamination} confirm that synthetic content now constitutes an estimated 20--60\% of web corpora, though accumulating real data avoids divergence~\citep{kazdan2025collapse} and even minimal curation suffices~\citep{amin2025escaping}.
6	Not all synthetic data is harmful: the Phi series~\citep{gunasekar2023textbooks,li2023textbooks2} demonstrates that curated synthetic data can improve training efficiency, but this assumes intentional generation with quality control, unlike the uncontrolled web contamination we address.
7	
8	\paragraph{Detection, Filtering, and Data Reweighting.}
9	Continuous-score detectors---probability curvature~\citep{mitchell2023detectgpt}, cross-perplexity ratios~\citep{hans2024binoculars}, low-probability token statistics~\citep{shi2024minkprob}---enable document-level weighting~\citep{wu2025survey}.
10	Data composition is optimized via perplexity filtering~\citep{wenzek2020ccnet}, domain-level importance sampling~\citep{xie2023doremi,xie2023dsir,grangier2025crisp,ye2025mixing}, instance-level strategies~\citep{bengio2009curriculum,mindermann2022prioritized,sow2025dynamic,engstrom2024dsdm}, and deduplication~\citep{abbas2023semdedup}; see \citet{albalak2024survey}.
11	None targets synthetic provenance; moreover, classifier-based quality scores may capture stylistic similarity rather than intrinsic quality~\citep{naitsaada2025illusion}.
12	Most directly related, \citet{drayson2025detection} propose $w_j = (1{-
…[truncated 2560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1099 · 2026-05-25T21:17:47.734490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1100 · 2026-05-25T21:17:48.186092+00:00_

1	\begin{figure}[t]
2	\centering
3	\includegraphics[width=\columnwidth]{dr_pipeline_concept}
4	\caption{Overview of the detect-and-reweight pipeline. A TF-IDF + LR detector assigns contamination scores $q(x)$; a dual-constrained optimizer selects $b$ to satisfy quality-floor and effective-sample-size constraints; the resulting weights $w(x) = (1{-}q(x))^{b}$ are applied during training.}
5	\label{fig:pipeline}
6	\end{figure}
7	
8	Figure~\ref{fig:pipeline} illustrates the pipeline. Let $\mathcal{D}$ denote a pretraining corpus with unknown synthetic contamination ratio $\rho$~\citep{cheng2025contamination}.
9	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
10	Rather than selecting $b$ via grid search, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
11	
12	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
13	
14	\paragraph{Quality floor.}
15	The \emph{effective authenticity} $\aeff(b) = \sum_i w_i(b)(1{-}q_i) / \sum_i w_i(b)$ measures the weighted mean detector confidence that samples are real.
16	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
17	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.79$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
18	
19	\paragraph{Stability ceiling.}
20	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
21	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
22	
23	\paragraph{Adaptive $\bstar$.}
24	Since $\aeff$ i
…[truncated 1925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1101 · 2026-05-25T21:17:48.186453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1102 · 2026-05-25T21:17:48.713831+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution, providing a controlled testbed with known ground-truth labels but limiting ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss implications for detection difficulty in \S\ref{sec:limitations}.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.048 after temperature scaling with $T{=}0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness} (implementation details in Appendix~\ref{app:detector_details}).
11	
12	\paragraph{Training.}
13	Table~\ref{tab:config} summarizes the training configuration.
14	We use $B{=}4
…[truncated 2489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 527
}
```

</details>

---


### Tool call

_source line 1103 · 2026-05-25T21:17:48.715995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1104 · 2026-05-25T21:17:49.170835+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\setlength{\tabcolsep}{3pt}
5	\resizebox{\columnwidth}{!}{%
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
9	\midrule
10	Uniform                & 17.694 & 17.686 & 17.702 & 17.697 $\pm$ .008 \\
11	Adaptive $\bstar$ (ours) & \textbf{17.680} & \textbf{17.666} & \textbf{17.677} & \textbf{17.674} $\pm$ .006 \\
12	ESS-only               & 17.730 & 17.720 & 17.760 & 17.737 $\pm$ .021 \\
13	Random $\mathcal{U}(0,2)$ & 17.830 & 17.800 & 17.777 & 17.802 $\pm$ .027 \\
14	Permuted $q$-scores  & 17.919 & --     & --     & 17.919 \\
15	\bottomrule
16	\end{tabular}}
17	\caption{Main comparison: held-out PPL ($\downarrow$) at $\rho{=}0.4$, 1 content epoch.
18	Adaptive and Uniform: 5-seed means (seeds 42, 123, 456, 789, 234); ESS-only and Random: 3-seed means (seeds 42, 123, 456); Permuted: single seed (42).
19	Adaptive uses $\tau{=}0.7$, $\nmin{=}2$.
20	Permuted randomly shuffles $q$-scores across samples, destroying provenance signal while preserving weight non-uniformity ($\Delta{=}{+}0.225$).}
21	\label{tab:main}
22	\end{table}
23	
24	\subsection{Main Results}
25	\label{sec:main-results}
26	
27	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across five seeds.
28	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
29	
30	Adaptive $\bstar$ achieves 5-seed mean PPL 17.674, compared to 17.697 for uniform ($\Delta{=}{-}0.023$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean, post-hoc oracle; gap $+$0.054; Table~\ref{tab:aux}).
31	A paired $t$-test yields $t(4){=}{-}8.21$, $p{=}0.0012$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.011$, reaching conventional significance at $\alpha{=}0.05$.
32	The engineering benefit is eliminating $b$ grid search (nine full training runs~\citep{dray
…[truncated 13772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1105 · 2026-05-25T21:17:49.171298+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1106 · 2026-05-25T21:17:49.625807+00:00_

1	\paragraph{D\&R as the strongest strategy.}
2	D\&R outperforms all reweighting methods by $0.35$--$0.42$ PPL (Table~\ref{tab:epoch_match}), but epoch-matched controls attribute ${>}$95\% of this advantage to multi-epoch exposure on filtered data rather than superior per-token learning.
3	This benefit was invisible in \citet{drayson2025detection}, where from-scratch pretraining rarely completes one epoch; in continued pretraining, it becomes the dominant factor.
4	
5	\paragraph{When uniform beats reweighting.}
6	Table~\ref{tab:decision} summarizes three prerequisites for effective soft reweighting: (i)~sufficient detector discrimination \emph{and} calibration (AUC\,$\geq$\,0.9, ECE\,$\leq$\,0.05; \S\ref{sec:robustness}); (ii)~contamination $\rho \geq 0.4$, below which the method degrades ($+$0.046 at $\rho{=}0.2$; Appendix~\ref{app:rho02}) with a sharp transition in $[0.3, 0.4]$ (Figure~\ref{fig:delta_vs_rho}, Appendix~\ref{app:rho03}); (iii)~generator--trainee mismatch (at 1.7B the benefit diminishes to $\Delta{=}{-}0.013$ with OOD mixed).
7	When any condition is violated, uniform is the safer default.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\setlength{\tabcolsep}{3pt}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}lcll@{}}
15	\toprule
16	\textbf{Condition} & \textbf{Observed?} & \textbf{Evidence} & \textbf{$\Delta$ PPL} \\
17	\midrule
18	Detector AUC $\geq 0.9$ & Yes & N-gram (0.73) degrades & $+$0.129 \\
19	Detector ECE $\leq 0.05$ & Yes & GPT-2 (0.131) degrades & $+$0.098 \\
20	Contamination $\rho \geq 0.4$ & Yes & $\rho{=}0.2$ degrades & $+$0.046 \\
21	Generator $\neq$ trainee & Tentative & 1.7B: $\Delta{=}{-}0.013$, OOD mixed & -- \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Decision summary for practitioners.
25	$\Delta$ values are relative to uniform (positive = worse).
26	When any observed condition is violated, uniform is the safer default.}
27	\label{tab:decision}
28	\end{table}
29	
30	\paragraph{Effect size and downstream impact.}
31
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1107 · 2026-05-25T21:17:49.626190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1108 · 2026-05-25T21:17:50.077994+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (i)~D\&R is the strongest method in our setting, with multi-epoch exposure on filtered data accounting for ${>}$95\% of its advantage over reweighting; (ii)~detector calibration alongside discrimination, as high-AUC detectors with poor calibration degrade PPL below uniform; and (iii)~minimum intervention over unconstrained maximization, supported by the ESS-only ablation and the fixed-$b$ grid curve (Figure~\ref{fig:grid_b_trend}).
2	A dual-constrained adaptive $\bstar$ implementing these principles improves over uniform training at $\rho \geq 0.4$ without per-model tuning (Table~\ref{tab:decision}), though without measurable downstream gains at 0.6B scale.
3	Whether these conditions hold at full pretraining scale ($>$100B tokens), where contamination ratios are lower but corpora are harder to curate, is the central open question; a second priority is extending the detector--calibration axis to neural classifiers whose ECE profiles differ qualitatively from the TF-IDF family tested here.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1109 · 2026-05-25T21:17:50.078327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1110 · 2026-05-25T21:17:50.630576+00:00_

1	\begin{itemize}[nosep,leftmargin=*]
2	\item \textbf{Scope.}
3	All experiments use Qwen3 (0.6B and 1.7B) under self-contamination with 132--200M tokens of continued pretraining.
4	Generalization to other architectures, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination, where generator-corpus distribution mismatch may reduce detector accuracy, remains untested.
5	
6	\item \textbf{Detector coverage.}
7	Only three detectors from two families (discriminative TF-IDF+LR and generative perplexity scorers) were evaluated; fine-tuned neural classifiers (e.g., ModernBERT) and zero-shot methods (e.g., DetectGPT, Binoculars) remain untested, so the AUC/ECE thresholds reported here may shift with broader detector coverage.
8	
9	\item \textbf{Evaluation scope.}
10	Our primary metric is held-out perplexity; downstream accuracy is unchanged across conditions (Appendix~\ref{app:downstream}), so the practical benefit at 0.6B scale is limited to distributional quality rather than task performance.
11	\end{itemize}
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1111 · 2026-05-25T21:17:50.630977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1112 · 2026-05-25T21:17:50.883122+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least two samples with distinct $q$-values.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, (1 - q_i).
14	\end{equation*}
15	Taking the derivative with respect to $b$:
16	\begin{align*}
17	  \frac{d\pi_i}{db}
18	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
19	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
20	\end{align*}
21	Substituting,
22	\begin{align*}
23	  \frac{d\alpha_{\mathrm{eff}}}{db}
24	  &= \sum_i (1{-}q_i)\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
25	  &= \mathrm{Cov}_{\pi}\!\bigl(1{-}q_i,\, \ln(1{-}q_i)\bigr).
26	\end{align*}
27	Since $(1{-}q_i)$ and $\ln(1{-}q_i)$ are both increasing functions of $(1{-}q_i)$, they are positively associated, so the covariance is non-negative.
28	\end{proof}
29	
30	\begin{proposition}[ESS monotonicity]
31	\label{prop:ess_mono}
32	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
33	\end{proposition}
34	
35	\begin{proof}
36	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
37	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
38	Differentiating $H$ with respect to $b$:
39	\begin{equation*}
40	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
41	\end{equation*}
42	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; the $\pi^2$-weighted sum assigns greater mass to terms where $\ln(1{-}q_i) > \ma
…[truncated 28571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-25T21:17:54.752112+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with unlikely but possible oversights
- **3**: Pretty sure, though details may have been missed
- **2**: Willing to defend evaluation, but likely missed some details
- **1**: Outside expertise area or paper is difficult to understand

## 2. **Soundness**
Scale: 1-5 (with 0.5 increments)
- **5**: Excellent - among the most thorough studies in its category
- **4**: Strong - sufficient support for claims; extra experiments optional
- **3**: Acceptable - main claims supported; minor points need detail
- **2**: Poor - main claims lack support; major technical problems
- **1**: Major Issues - insufficient rigor or not relevant to ACL

Guidance: Assess scientific claims, experimental depth/breadth, methodological validity, and data collection rigor.

## 3. **Excitement**
Scale: 1-5 (with 0.5 increments)
- **5**: "I would recommend this paper to others and/or attend its presentation"
- **4**: Would mention to colleagues; effort to attend presentation
- **3**: Might mention points; attend if time permits
- **2**: Doesn't resonate personally; may resonate with others
- **1**: No personal resonance; unlikely to interest broader community

Guidance: Consider transformational breakthroughs, community impact, and personal relevance.

## 4. **Overall Assessment**
Scale: 1-5 (with 0.5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle with substantial revisions
- **1.5**: Resubmit after next cycle; major revisions needed
- **1**: Do not resubmit; fundamentally flawed or off-topic

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parame
…[truncated 1056 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 9276
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-25T21:18:00.622629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1115 · 2026-05-25T21:18:01.175544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1116 · 2026-05-25T21:18:02.133212+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1510
}
```

</details>

---


### Tool call

_source line 1117 · 2026-05-25T21:18:02.133642+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1118 · 2026-05-25T21:18:02.337714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1162
}
```

</details>

---


### Tool call

_source line 1119 · 2026-05-25T21:18:02.338183+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1120 · 2026-05-25T21:18:03.393451+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1259
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-25T21:18:03.394189+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-25T21:18:08.970811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1123 · 2026-05-25T21:18:09.928556+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-25T21:18:10.079700+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1125 · 2026-05-25T21:18:10.231026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1126 · 2026-05-25T21:18:10.587802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-25T21:18:10.792868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 561
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-25T21:18:15.715424+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf",
  "project": "provenance_weight_training",
  "pages": "13-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/submitted.pdf",
    "project": "provenance_weight_training",
    "pages": "13-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-25T21:18:16.117549+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.5}], \"total_pages\": 15, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1130 · 2026-05-25T21:18:18.804370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1131 · 2026-05-25T21:18:19.417024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 1132 · 2026-05-25T21:18:19.759137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-25T21:18:20.130923+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1326
}
```

</details>

---


### Tool result

_source line 1134 · 2026-05-25T21:18:20.888974+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1471
}
```

</details>

---


### Tool result

_source line 1135 · 2026-05-25T21:18:20.990617+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1231
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-25T21:20:46.566111+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
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

_source line 1137 · 2026-05-25T21:20:46.616702+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-25T21:20:50.565578+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_14/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-25T21:20:50.566088+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-25T21:22:57.144860+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "# Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量\n\n**论文**: \"When Does Detect-and-Reweight Work for Synthetic Contamination?\"\n**Venue**: EMNLP 2026 via ARR (Long paper)\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验设计严谨、自我评估诚实的分析论文，但实验范围过窄（self-contamination / 0.6B / 单一数据源）导致三个 effectiveness conditions 的一般性不足，且无下游任务提升，实际影响有限。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 在限定范围内实验设计严谨（epoch-matching、permuted controls、多 seed），但部分统计声明存在 overclaim（见 N1），且三个 conditions 的实验覆盖面不足以支撑一般性结论 |\n| Excitement | 2.5/5 | 方法新颖性有限（w=(1-q)^b 完全来自 Drayson et al.，dual constraint + bisection 是标准方法）；分析贡献在窄设定下有价值，但无法转化为可操作的实践指导 |\n| Reproducibility | 4.0/5 | 提供匿名代码库，详细报告超参数、seed、训练配置；但部分结果为 single-seed（Grid at ρ=0.6、Golden Ratio），限制可复现验证 |\n| Overall Assessment | 3.0/5 | Findings 水平——soundness 在其 scope 内达标，但 scope 太窄、excitement 不足、无下游影响，不满足 conference acceptance 标准 |\n\n**Reviewer Confidence**: 4/5 — 熟悉 data curation/reweighting 和 synthetic contamination 文献，仔细阅读了全文和 appendix。\n\n---\n\n## 主要优势\n\n1. **严谨的实验控制设计**：epoch-matched D&R controls（Table 3）是本文最有价值的贡献之一，揭示了 D&R 的优势>95% 来自 multi-epoch exposure 而非 per-token learning quality。这一 decomposition 在此前文献（如 Drayson et al.）中缺失，对 practitioners 选择数据策略有直接指导意义。\n\n2. **诚实的 self-assessment**：论文在 Abstract 末句、§1 末段、§6 Discussion 和 Limitations 中反复承认 scope 限制（self-contamination、0.6B、无下游提升），这种透明度在 NLP 投稿中难得。Appendix O 对 checkpoint-resume artifact 的详细披露尤其值得肯定。\n\n3. **消融设计清晰，隔离变量有效**：5-method ablation hierarchy（Adaptive < Uniform < ESS-only < Random < Permuted）配合 permuted q-scores（Δ=+0.225）有效隔离了 detector provenance signal 的作用，逻辑链完整。\n\n4. **统计处理高于平均水平**：Bonferroni-Holm correction、paired t-test、Cohen's d power analysis（Appendix Q）、cross-seed variance 报告，这些在同类论文中少见。\n\n5. **Calibration finding 有实用价值**：TF-IDF (AUC=0.94, ECE=0.048) vs. GPT-2 (AUC=0.91, ECE=0.131) 的对比（§5.2, Figure 1b）在 comparable AUC 下隔离了 calibration 的作用，对 detector 选择有指导意义。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 中 \"ρ ≥ 0.4\" 统计显著性声明存在 overclaim\n- 具体位置：Abstract 第6句；§5.1 第1段\n- 问题：Abstract 写 \"improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction\"。句法结构暗示 ρ=0.4 和 ρ=0.6 均达到显著性。但 §5.2 明确报告 ρ=0.6 的 p_BH=0.064，**未通过** Bonferroni-Holm correction at α=0.05。实际上只有 ρ=0.4 达到显著性（p_BH=0.011）。\n- 为什么影响接收：这是论文核心 claim 的准确性问题。Overclaimed statistical significance 是 reviewer 一票否决的典型原因。\n- 建议修改方向：改为 \"improves over uniform training at ρ=0.4 (p_BH=0.011) with directionally consistent but non-significant improvement at ρ=0.6 (p_BH=0.064)\" 或类似表述。\n\n**N2** [critical] 标题 scope 与实验覆盖面严重不匹配\n- 具体位置：标题、Abstract\n- 问题：\"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示对该范式的一般性回答。但实验仅覆盖：(a) self-contamination（同一模型生成+训练），(b) 0.6B scale（1.7B 仅为补充），(c) continued pretraining（非 from-scratch），(d) 单一真实数据源（FineWeb），(e) 主要一个 detector family（TF-IDF+LR）。论文自己在 §6 Discussion 承认 \"When any condition is violated, uniform is the safer default\"，但这些 conditions 本身只在极窄范围内被验证。\n- 为什么影响接收：标题的一般性 framing 会让读者期待跨模型、跨规模、跨场景的系统性研究。当发现全部结论仅基于 self-contamination + 0.6B 时，会产生 expectation gap，削弱论文可信度。\n- 建议修改方向：标题加限定，如 \"When Does Detect-and-Reweight Work? A Controlled Study of Self-Contamination at Small Scale\" 或在 abstract 更早处明确 scope。\n\n**N3** [critical] 无下游任务提升，但 Abstract 未提及——读者可能产生实际影响的错误期待\n- 具体位置：Abstract（全文）；§6 \"Effect size and downstream impact\" 段\n- 问题：Abstract 说 \"improves over uniform training\" 而不指定 metric。读者自然理解为综合质量提升。但 §6 和 Appendix H 明确报告 downstream accuracy 完全无变化（0.5414 vs. 0.5415, 5 benchmarks, |Δ|≤0.01）。Δ=-0.023 PPL 仅为约 0.13% 的相对改善，且未转化为任何可测量的能力提升。对于 analysis paper 的 actionable conclusions，\"no downstream gain\" 是关键信息，不应被 Abstract 遗漏。\n- 为什么影响接收：这影响论文的 practical significance 评估。不知道这一事实的读者可能高估论文贡献。\n- 建议修改方向：Abstract 中在 \"improves over uniform training\" 后补充 \"(in-distribution perplexity; downstream accuracy is unchanged at 0.6B scale)\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] §6 Discussion 第一段与 §5.1 内容高度重复\n- 具体位置：§6 \"D&R as the strongest strategy\" 段 vs. §5.1 \"Hard filtering and multi-epoch exposure\" 段\n- 问题：§6 开头段几乎逐字重述 §5.1 的 D&R epoch-matching 结论（\"outperforms all reweighting methods by 0.35-0.42 PPL\"、\">95% of this advantage to multi-epoch exposure\"）。类似地，§6 \"When uniform beats reweighting\" 段重述 Table 5 内容。在 8 页限制下，这种冗余浪费了约半页篇幅。\n- 建议：§6 应聚焦 §5 未涵盖的 implications 和 open questions，而非重述 findings。可以将省出的空间用于讨论 cross-model contamination 的预期行为或更深入的 detector calibration 分析。\n\n**W2** [warning] \"Three effectiveness conditions\" 的 framing 过度概括\n- 具体位置：Abstract、§1、§7\n- 问题：论文将其发现包装为 \"three effectiveness conditions\"，但这些更准确地说是 \"在 self-contamination + 0.6B + continued pretraining 设定下的三个实证观察\"。\"Conditions\" 一词暗示充要条件或一般性规律，但每个 condition 的验证范围极有限：Condition 1（D&R 最强）仅在一个设定下测试；Condition 2（calibration 要求）仅用 3 个 detectors 验证；Condition 3（minimum intervention）仅用一种 dual-constraint 方法体现。\n- 建议：将 \"conditions\" 改为 \"empirical observations\" 或 \"findings\"，或在首次使用时加限定词（\"three effectiveness conditions observed in our controlled setting\"）。\n\n**W3** [warning] Related Work 缺少若干近期 instance-level reweighting 方法\n- 具体位置：§2 \"Detection, Filtering, and Data Reweighting\"\n- 问题：论文引用了 domain-level 方法（DoReMi, DSIR, CRISP）和部分 instance-level 方法（Sow et al., DSDM），但缺少几个直接相关的近期工作：\n  - **MATES** (Yu et al., 2024): instance-level data selection via data influence models，与本文的 instance-level reweighting 直接相关\n  - **Aioli** (Balachandran et al., 2024): adaptive online data mixing，与 per-batch adaptation 机制相关\n  - **RAID** (Dugan et al., 2024) 和 **M4** (Wang et al., 2024): synthetic text detection benchmarks，与 detector evaluation 相关\n  - 这些工作与论文的 instance-level reweighting 和 detector evaluation 直接相关，应至少在 §2 中讨论定位差异。\n- 建议：增加一段讨论 instance-level selection 最新进展（MATES、Aioli），明确本文与这些方法在目标（synthetic contamination vs. general data quality）和机制（provenance-based vs. influence-based）上的区别。Detection benchmark（RAID、M4）至少值得提及以说明 detector evaluation 的广泛背景。\n\n**W4** [warning] Decision summary（Table 5）的实用性受限于验证范围\n- 具体位置：Table 5, §6 \"When uniform beats reweighting\"\n- 问题：Table 5 标题为 \"Decision summary for practitioners\"，列出了四个条件（AUC≥0.9, ECE≤0.05, ρ≥0.4, generator≠trainee）。但这些阈值均来自 self-contamination + 0.6B + FineWeb 设定下的单一实验。例如，AUC≥0.9 的阈值仅基于 3 个 detectors（0.73/0.91/0.94），采样密度不足以确定精确 boundary；ECE≤0.05 仅基于 TF-IDF (0.048) vs. GPT-2 (0.131) 的对比，中间值未测试。将这些称为 \"for practitioners\" 可能误导读者认为这些是经过充分验证的通用阈值。\n- 建议：将标题改为 \"Summary of observed conditions (self-contamination, 0.6B)\" 或在 caption 中明确指出这些阈值仅为当前设定下的观察值，不应直接推广。\n\n**W5** [warning] Δ=-0.023 的效应量在 continued pretraining 语境中的意义缺乏充分论证\n- 具体位置：§5.1, §6 \"Effect size and downstream impact\"\n- 问题：PPL 从 17.697 降至 17.674（Δ=-0.023, 约 0.13% 相对改善）。论文在 §6 承认 \"the paradigm's impact at current scales is modest\"，但未提供 continued pretraining 文献中的 PPL improvement baselines 来 contextualize 这个数字。读者无法判断 0.13% 的 PPL 改善在 continued pretraining 中是 meaningful signal 还是 noise floor。对比：D&R 的 epoch-matched 结果（Δ=0.017）与 adaptive 的 gap 仅 0.006 PPL，暗示 adaptive 的 marginal value 极低。\n- 建议：引用 continued pretraining 文献中的 typical PPL improvement ranges（如 domain-adaptive 方法的效应量），让读者能 calibrate 本文结果的实际意义。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1** [info] Table 1（主结果表）caption 声明 \"Adaptive and Uniform: 5-seed means\"，但表格正文只显示 3 列 seed（42, 123, 456）。其余 2 个 seed（789, 234）的结果未展示，只体现在 Mean 列中。建议在表格中增加这两列或在 caption 中解释省略原因。\n\n- **M2** [info] §5.2 报告 ρ=0.6 时 \"paired t=-9.95, p_BH=0.064\"，但 Appendix I Table 7 给出 \"paired t=-15.4, p=0.004\"（full precision）和 \"t=-9.95, p=0.010\"（3dp rounding）。正文和 appendix 的 t 值不一致（-9.95 vs -15.4），虽然 appendix 解释了 rounding 差异，但正文引用的 p_BH=0.064 与 appendix 的 p=0.010（未校正）存在跳跃，读者可能混淆。建议统一呈现。\n\n- **M3** [info] Introduction 中 \"three effectiveness conditions\" 的编号与 Discussion/Conclusion 的顺序不完全一致（Introduction: D&R → detector requirements → minimum intervention；Discussion 同序但 Conclusion 措辞略有变化），minor但在 8 页论文中增加阅读摩擦。\n\n- **M4** [info] Appendix P 的 ρ=0.3 结果（Table 16）seed 456 缺少 OOD 评估（OWT/Wiki 列为 \"--\"），caption 未解释原因。\n\n- **M5** [info] §4 \"Evaluation\" 提到 \"sliding-window evaluation (stride 1024)\" 但未说明 window size。对于 PPL 结果的可复现性，这个信息应在 main text 或 appendix 中明确。\n\n---\n\n## Questions to Authors\n\n1. 在 ρ=0.4 设定下，adaptive b* 相对 uniform 的 PPL 改善（Δ=-0.023）约等于 D&R epoch-matched 的结果（Δ=-0.017 gap to adaptive）。如果 D&R 是 practitioners 的更优选择（如论文所建议），那么 adaptive reweighting 的 use case 是什么？在什么场景下 practitioner 会选择 soft reweighting 而非 D&R？\n\n2. 论文强调 calibration 的重要性（ECE≤0.05），但 temperature scaling 的 T=0.204 是在一个 held-out labeled split 上调的——这本身需要 labeled data。如果 practitioner 没有 labeled data（这是 web-scale 的常见场景），这个 calibration 前提如何满足？\n\n3. Batch size B=4 在 modern pretraining 中极不常见（通常 B≥256）。论文在 §5.3 展示了 B=16 时效果更好（Δ=-0.068），但实际训练中 B 通常大 2-3 个数量级。是否有 B=64/128 的预期行为分析？\n\n---\n\n## Missing References\n\n- Yu, B., et al. (2024). \"MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models.\" NeurIPS 2024.\n- Balachandran, V., et al. (2024). \"Aioli: A Unified Optimization Framework for Language Model Data Mixing.\" arXiv.\n- Dugan, L., et al. (2024). \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors.\" ACL 2024.\n- Wang, Y., et al. (2024). \"M4: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection.\" EACL 2024.\n\n---\n\n## 格式合规检查\n\n| 项目 | 结果 | 备注 |\n|------|------|------|\n| 正文页数（§1-§7） | ✓ 8页 | §7 Conclusion 结束于第8页底部 |\n| Abstract ≤ 200 words | ✓ ~171 words | |\n| Limitations 在正文中 | ✓ | 第9页，§7之后、References之前，非 appendix |\n| Limitations 内容量 | ✓ | 3个 bullet point，适当 |\n| Responsible NLP Checklist 不在 PDF 中 | ✓ | 未出现 |\n| Appendix double-column | ✓ | 第10-15页均为 double-column ACL style |\n| 引用格式一致性 | ✓ | (Author, Year) 格式统一 |\n| Double-blind 匿名 | ✓ | Author 显示 \"Anonymous ACL submission\"，代码链接用 anonymous.4open.science |\n| AI assistant 使用声明 | ✓ | Appendix S 披露使用 Claude |",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "# Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量\n\n**论文**: \"When Does Detect-and-Reweight Work for Synthetic Contamination?\"\n**Venue**: EMNLP 2026 via ARR (Long paper)\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验设计严谨、自我评估诚实的分析论文，但实验范围过窄（self-contamination / 0.6B / 单一数据源）导致三个 effectiveness conditions 的一般性不足，且无下游任务提升，实际影响有限。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 在限定范围内实验设计严谨（epoch-matching、permuted controls、多 seed），但部分统计声明存在 overclaim（见 N1），且三个 conditions 的实验覆盖面不足以支撑一般性结论 |\n| Excitement | 2.5/5 | 方法新颖性有限（w=(1-q)^b 完全来自 Drayson et al.，dual constraint + bisection 是标准方法）；分析贡献在窄设定下有价值，但无法转化为可操作的实践指导 |\n| Reproducibility | 4.0/5 | 提供匿名代码库，详细报告超参数、seed、训练配置；但部分结果为 single-seed（Grid at ρ=0.6、Golden Ratio），限制可复现验证 |\n| Overall Assessment | 3.0/5 | Findings 水平——soundness 在其 scope 内达标，但 scope 太窄、excitement 不足、无下游影响，不满足 conference acceptance 标准 |\n\n**Reviewer Confidence**: 4/5 — 熟悉 data curation/reweighting 和 synthetic contamination 文献，仔细阅读了全文和 appendix。\n\n---\n\n## 主要优势\n\n1. **严谨的实验控制设计**：epoch-matched D&R controls（Table 3）是本文最有价值的贡献之一，揭示了 D&R 的优势>95% 来自 multi-epoch exposure 而非 per-token learning quality。这一 decomposition 在此前文献（如 Drayson et al.）中缺失，对 practitioners 选择数据策略有直接指导意义。\n\n2. **诚实的 self-assessment**：论文在 Abstract 末句、§1 末段、§6 Discussion 和 Limitations 中反复承认 scope 限制（self-contamination、0.6B、无下游提升），这种透明度在 NLP 投稿中难得。Appendix O 对 checkpoint-resume artifact 的详细披露尤其值得肯定。\n\n3. **消融设计清晰，隔离变量有效**：5-method ablation hierarchy（Adaptive < Uniform < ESS-only < Random < Permuted）配合 permuted q-scores（Δ=+0.225）有效隔离了 detector provenance signal 的作用，逻辑链完整。\n\n4. **统计处理高于平均水平**：Bonferroni-Holm correction、paired t-test、Cohen's d power analysis（Appendix Q）、cross-seed variance 报告，这些在同类论文中少见。\n\n5. **Calibration finding 有实用价值**：TF-IDF (AUC=0.94, ECE=0.048) vs. GPT-2 (AUC=0.91, ECE=0.131) 的对比（§5.2, Figure 1b）在 comparable AUC 下隔离了 calibration 的作用，对 detector 选择有指导意义。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 中 \"ρ ≥ 0.4\" 统计显著性声明存在 overclaim\n- 具体位置：Abstract 第6句；§5.1 第1段\n- 问题：Abstract 写 \"improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction\"。句法结构暗示 ρ=0.4 和 ρ=0.6 均达到显著性。但 §5.2 明确报告 ρ=0.6 的 p_BH=0.064，**未通过** Bonferroni-Holm correction at α=0.05。实际上只有 ρ=0.4 达到显著性（p_BH=0.011）。\n- 为什么影响接收：这是论文核心 claim 的准确性问题。Overclaimed statistical significance 是 reviewer 一票否决的典型原因。\n- 建议修改方向：改为 \"improves over uniform training at ρ=0.4 (p_BH=0.011) with directionally consistent but non-significant improvement at ρ=0.6 (p_BH=0.064)\" 或类似表述。\n\n**N2** [critical] 标题 scope 与实验覆盖面严重不匹配\n- 具体位置：标题、Abstract\n- 问题：\"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示对该范式的一般性回答。但实验仅覆盖：(a) self-contamination（同一模型生成+训练），(b) 0.6B scale（1.7B 仅为补充），(c) continued pretraining（非 from-scratch），(d) 单一真实数据源（FineWeb），(e) 主要一个 detector family（TF-IDF+LR）。论文自己在 §6 Discussion 承认 \"When any condition is violated, uniform is the safer default\"，但这些 conditions 本身只在极窄范围内被验证。\n- 为什么影响接收：标题的一般性 framing 会让读者期待跨模型、跨规模、跨场景的系统性研究。当发现全部结论仅基于 self-contamination + 0.6B 时，会产生 expectation gap，削弱论文可信度。\n- 建议修改方向：标题加限定，如 \"When Does Detect-and-Reweight Work? A Controlled Study of Self-Contamination at Small Scale\" 或在 abstract 更早处明确 scope。\n\n**N3** [critical] 无下游任务提升，但 Abstract 未提及——读者可能产生实际影响的错误期待\n- 具体位置：Abstract（全文）；§6 \"Effect size and downstream impact\" 段\n- 问题：Abstract 说 \"improves over uniform training\" 而不指定 metric。读者自然理解为综合质量提升。但 §6 和 Appendix H 明确报告 downstream accuracy 完全无变化（0.5414 vs. 0.5415, 5 benchmarks, |Δ|≤0.01）。Δ=-0.023 PPL 仅为约 0.13% 的相对改善，且未转化为任何可测量的能力提升。对于 analysis paper 的 actionable conclusions，\"no downstream gain\" 是关键信息，不应被 Abstract 遗漏。\n- 为什么影响接收：这影响论文的 practical significance 评估。不知道这一事实的读者可能高估论文贡献。\n- 建议修改方向：Abstract 中在 \"improves over uniform training\" 后补充 \"(in-distribution perplexity; downstream accuracy is unchanged at 0.6B scale)\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] §6 Discussion 第一段与 §5.1 内容高度重复\n- 具体位置：§6 \"D&R as the strongest strategy\" 段 vs. §5.1 \"Hard filtering and multi-epoch exposure\" 段\n- 问题：§6 开头段几乎逐字重述 §5.1 的 D&R epoch-matching 结论（\"outperforms all reweighting methods by 0.35-0.42 PPL\"、\">95% of this advantage to multi-epoch exposure\"）。类似地，§6 \"When uniform beats reweighting\" 段重述 Table 5 内容。在 8 页限制下，这种冗余浪费了约半页篇幅。\n- 建议：§6 应聚焦 §5 未涵盖的 implications 和 open questions，而非重述 findings。可以将省出的空间用于讨论 cross-model contamination 的预期行为或更深入的 detector calibration 分析。\n\n**W2** [warning] \"Three effectiveness conditions\" 的 framing 过度概括\n- 具体位置：Abstract、§1、§7\n- 问题：论文将其发现包装为 \"three effectiveness conditions\"，但这些更准确地说是 \"在 self-contamination + 0.6B + continued pretraining 设定下的三个实证观察\"。\"Conditions\" 一词暗示充要条件或一般性规律，但每个 condition 的验证范围极有限：Condition 1（D&R 最强）仅在一个设定下测试；Condition 2（calibration 要求）仅用 3 个 detectors 验证；Condition 3（minimum intervention）仅用一种 dual-constraint 方法体现。\n- 建议：将 \"conditions\" 改为 \"empirical observations\" 或 \"findings\"，或在首次使用时加限定词（\"three effectiveness conditions observed in our controlled setting\"）。\n\n**W3** [warning] Related Work 缺少若干近期 instance-level reweighting 方法\n- 具体位置：§2 \"Detection, Filtering, and Data Reweighting\"\n- 问题：论文引用了 domain-level 方法（DoReMi, DSIR, CRISP）和部分 instance-level 方法（Sow et al., DSDM），但缺少几个直接相关的近期工作：\n  - **MATES** (Yu et al., 2024): instance-level data selection via data influence models，与本文的 instance-level reweighting 直接相关\n  - **Aioli** (Balachandran et al., 2024): adaptive online data mixing，与 per-batch adaptation 机制相关\n  - **RAID** (Dugan et al., 2024) 和 **M4** (Wang et al., 2024): synthetic text detection benchmarks，与 detector evaluation 相关\n  - 这些工作与论文的 instance-level reweighting 和 detector evaluation 直接相关，应至少在 §2 中讨论定位差异。\n- 建议：增加一段讨论 instance-level selection 最新进展（MATES、Aioli），明确本文与这些方法在目标（synthetic contamination vs. general data quality）和机制（provenance-based vs. influence-based）上的区别。Detection benchmark（RAID、M4）至少值得提及以说明 detector evaluation 的广泛背景。\n\n**W4** [warning] Decision summary（Table 5）的实用性受限于验证范围\n- 具体位置：Table 5, §6 \"When uniform beats reweighting\"\n- 问题：Table 5 标题为 \"Decision summary for practitioners\"，列出了四个条件（AUC≥0.9, ECE≤0.05, ρ≥0.4, generator≠trainee）。但这些阈值均来自 self-contamination + 0.6B + FineWeb 设定下的单一实验。例如，AUC≥0.9 的阈值仅基于 3 个 detectors（0.73/0.91/0.94），采样密度不足以确定精确 boundary；ECE≤0.05 仅基于 TF-IDF (0.048) vs. GPT-2 (0.131) 的对比，中间值未测试。将这些称为 \"for practitioners\" 可能误导读者认为这些是经过充分验证的通用阈值。\n- 建议：将标题改为 \"Summary of observed conditions (self-contamination, 0.6B)\" 或在 caption 中明确指出这些阈值仅为当前设定下的观察值，不应直接推广。\n\n**W5** [warning] Δ=-0.023 的效应量在 continued pretraining 语境中的意义缺乏充分论证\n- 具体位置：§5.1, §6 \"Effect size and downstream impact\"\n- 问题：PPL 从 17.697 降至 17.674（Δ=-0.023, 约 0.13% 相对改善）。论文在 §6 承认 \"the paradigm's impact at current scales is modest\"，但未提供 continued pretraining 文献中的 PPL improvement baselines 来 contextualize 这个数字。读者无法判断 0.13% 的 PPL 改善在 continued pretraining 中是 meaningful signal 还是 noise floor。对比：D&R 的 epoch-matched 结果（Δ=0.017）与 adaptive 的 gap 仅 0.006 PPL，暗示 adaptive 的 marginal value 极低。\n- 建议：引用 continued pretraining 文献中的 typical PPL improvement ranges（如 domain-adaptive 方法的效应量），让读者能 calibrate 本文结果的实际意义。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1** [info] Table 1（主结果表）caption 声明 \"Adaptive and Uniform: 5-seed means\"，但表格正文只显示 3 列 seed（42, 123, 456）。其余 2 个 seed（789, 234）的结果未展示，只体现在 Mean 列中。建议在表格中增加这两列或在 caption 中解释省略原因。\n\n- **M2** [info] §5.2 报告 ρ=0.6 时 \"paired t=-9.95, p_BH=0.064\"，但 Appendix I Table 7 给出 \"paired t=-15.4, p=0.004\"（full precision）和 \"t=-9.95, p=0.010\"（3dp rounding）。正文和 appendix 的 t 值不一致（-9.95 vs -15.4），虽然 appendix 解释了 rounding 差异，但正文引用的 p_BH=0.064 与 appendix 的 p=0.010（未校正）存在跳跃，读者可能混淆。建议统一呈现。\n\n- **M3** [info] Introduction 中 \"three effectiveness conditions\" 的编号与 Discussion/Conclusion 的顺序不完全一致（Introduction: D&R → detector requirements → minimum intervention；Discussion 同序但 Conclusion 措辞略有变化），minor但在 8 页论文中增加阅读摩擦。\n\n- **M4** [info] Appendix P 的 ρ=0.3 结果（Table 16）seed 456 缺少 OOD 评估（OWT/Wiki 列为 \"--\"），caption 未解释原因。\n\n- **M5** [info] §4 \"Evaluation\" 提到 \"sliding-window evaluation (stride 1024)\" 但未说明 window size。对于 PPL 结果的可复现性，这个信息应在 main text 或 appendix 中明确。\n\n---\n\n## Questions to Authors\n\n1. 在 ρ=0.4 设定下，adaptive b* 相对 uniform 的 PPL 改善（Δ=-0.023）约等于 D&R epoch-matched 的结果（Δ=-0.017 gap to adaptive）。如果 D&R 是 practitioners 的更优选择（如论文所建议），那么 adaptive reweighting 的 use case 是什么？在什么场景下 practitioner 会选择 soft reweighting 而非 D&R？\n\n2. 论文强调 calibration 的重要性（ECE≤0.05），但 temperature scaling 的 T=0.204 是在一个 held-out labeled split 上调的——这本身需要 labeled data。如果 practitioner 没有 labeled data（这是 web-scale 的常见场景），这个 calibration 前提如何满足？\n\n3. Batch size B=4 在 modern pretraining 中极不常见（通常 B≥256）。论文在 §5.3 展示了 B=16 时效果更好（Δ=-0.068），但实际训练中 B 通常大 2-3 个数量级。是否有 B=64/128 的预期行为分析？\n\n---\n\n## Missing References\n\n- Yu, B., et al. (2024). \"MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models.\" NeurIPS 2024.\n- Balachandran, V., et al. (2024). \"Aioli: A Unified Optimization Framework for Language Model Data Mixing.\" arXiv.\n- Dugan, L., et al. (2024). \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors.\" ACL 2024.\n- Wang, Y., et al. (2024). \"M4: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection.\" EACL 2024.\n\n---\n\n## 格式合规检查\n\n| 项目 | 结果 | 备注 |\n|------|------|------|\n| 正文页数（§1-§7） | ✓ 8页 | §7 Conclusion 结束于第8页底部 |\n| Abstract ≤ 200 words | ✓ ~171 words | |\n| Limitations 在正文中 | ✓ | 第9页，§7之后、References之前，非 appendix |\n| Limitations 内容量 | ✓ | 3个 bullet point，适当 |\n| Responsible NLP Checklist 不在 PDF 中 | ✓ | 未出现 |\n| Appendix double-column | ✓ | 第10-15页均为 double-column ACL style |\n| 引用格式一致性 | ✓ | (Author, Year) 格式统一 |\n| Double-blind 匿名 | ✓ | Author 显示 \"Anonymous ACL submission\"，代码链接用 anonymous.4open.science |\n| AI assistant 使用声明 | ✓ | Appendix S 披露使用 Claude |",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-25T21:23:00.911334+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 1142 · 2026-05-25T21:23:10.302576+00:00_

审稿报告已提交给 Review Director。

**总结**：Overall 3.0 (Findings)。论文实验设计严谨（epoch-matching controls、permuted ablation、统计校正），自我评估诚实，但存在三个 Must-Fix 问题：(1) Abstract 对 ρ≥0.4 的显著性声明存在 overclaim（ρ=0.6 实际未通过校正，p_BH=0.064）；(2) 标题 scope 远超实验覆盖面（self-contamination / 0.6B / 单一数据源）；(3) Abstract 未提及下游任务无提升这一关键事实。此外还有 Discussion 与 Results 内容重复、Related Work 缺少 MATES/Aioli 等近期方法、Decision summary 实用性受限等 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---


## Round 28

## Round 28

4 recorded events


### User

_source line 1143 · 2026-05-25T21:27:07.860893+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见：方法严谨性 + 实验设计

**Overall Assessment**: 3.0 — Findings
**Soundness**: 3.5/5 | **Excitement**: 2.5/5

### 主要优势
- S1: Epoch-matched control 分析是本文最大亮点
- S2: Ablation 设计层层递进，控制变量清晰
- S3: 对自身局限性的透明度值得肯定
- S4: Dual-constrained adaptive 方法有理论动机
- S5: Batch-size amplification 结果有价值

### Must-Fix 问题

**N1** [critical] Effect size 与 practitioner framing 之间的根本矛盾
- PPL 改善仅 0.023（0.13% relative），下游任务准确率完全相同（0.5414 vs 0.5415），1.7B 效应再减半至 Δ=-0.013 且 OOD 方向不一致。对下游任务零贡献的方法，其 "effectiveness conditions" 对实践者的指导意义何在？
- 建议重新定位为 mechanism analysis 而非 practitioner guide。

**N2** [critical] Cohen's d = 3.83 被 deterministic data ordering 系统性放大
- 5 个 seed 仅改变模型初始化，dataloader 完全 deterministic。SD_Δ=0.006 反映初始化噪声极小方差，而非方法在不同数据条件下的稳健性。如果 data ordering 也随机化，SD_Δ 很可能大幅增加，Cohen's d 可能降至 <1。

### Should-Fix 问题

**W1** [warning] 缺少 uniform × multi-epoch baseline
- D&R (q>0.3) raw PPL=17.250 源于 ~3.2 content epochs。缺少全部数据做 ~3.2 epochs 的 uniform baseline，无法区分 pure repetition vs selective filtering。

**W2** [warning] α_eff proxy 的 37% 未解释方差削弱理论保证
- R²≈0.63，未量化 α_eff ≥ τ 但 true fraction < τ 的 violation 频率。

**W3** [warning] Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差
- α_eff 的 negative bias 导致 over-intervention，PPL gap 0.054 是 adaptive-vs-uniform gain 的 2.3×。违背 minimum intervention 原则。

**W4** [warning] 3 个 detector 不足以支撑 AUC/ECE threshold 通用性

**W5** [warning] Scale 效应递减 43%，practitioner 适用性存疑
- 0.6B→1.7B Δ 减半，7B+ 效应可能趋零。

### 小问题
- M1: B=4 主实验低估方法潜力
- M2: Paired t-test 正态性假设 n=5 下无法验证
- M3: Abstract word count 接近 200-word 限制

### Questions to Authors
1. 是否有不同 data permutation 下的实验？
2. Uniform × multi-epoch baseline 的预期结果？
3. α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例？
4. Calibration-corrected α_eff 能否缩小 b* vs grid-optimal 的 gap？
5. 1.7B 实验选择 τ=0.8 而非 0.7 的理由？

---

请对上述每条 Must-Fix、Should-Fix 和 Questions 给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-25T21:29:20.792259+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: Effect size 与 practitioner framing 之间的根本矛盾**\n\n同意。这与我的 N3（Abstract 未提及无下游提升）和 W5（效应量论证不足）一致。Δ=-0.023 PPL（0.13% relative）在 §6 被承认为 \"modest\"，但 Table 5 标题仍为 \"Decision summary for practitioners\"，且 Abstract 中 \"improves over uniform training\" 未限定为 PPL-only。论文内部存在定位矛盾：一方面诚实承认影响有限（§6 \"does not transfer to downstream accuracy\"），另一方面仍以 practitioner guidance 包装结论。\n\n补充发现：§7 Conclusion 最后一句提到 \"whether these conditions hold at full pretraining scale (>100B tokens)...is the central open question\"，但如果 0.6B→1.7B 效应已减半（§5.2, Δ=-0.013），且 1.7B OOD 方向不一致（OWT Δ=-0.008, Wiki Δ=+0.013），那么 full-scale 的前景进一步存疑。R1 建议重新定位为 mechanism analysis 是合理的——论文最有价值的贡献（D&R epoch-matching decomposition、calibration 发现）本质上是分析性的，不需要 practitioner framing 来体现价值。\n\n**[AGREE] R1-N2: Cohen's d = 3.83 被 deterministic data ordering 系统性放大**\n\n同意，这是一个重要的方法论问题。Appendix Q 明确承认 \"seeds affect only parameter initialization, not data order (the dataloader is deterministic), so the primary stochastic axis is initialization noise at 0.6B scale\"。这意味着 SD_Δ=0.006 仅反映初始化噪声的极小方差，而非方法在不同数据采样条件下的稳健性。\n\nCohen's d=3.83 和 power>0.99 的呈现方式在 §5.1 中给读者留下了\"效果极其稳健\"的印象，但实际上只是说\"在固定数据顺序下，不同初始化产生的结果非常一致\"——这是一个远弱于\"方法在不同条件下稳健有效\"的声明。论文在 Appendix Q 的透明度值得肯定（\"the low dispersion is a property of the experimental setting rather than a method artifact\"），但这个关键 caveat 应出现在 §5.1 主文而非仅在 appendix 中。\n\n补充：uniform baseline 也有类似的低方差（σ=0.008），说明窄方差确实是实验设定的属性。但这恰恰意味着 paired t-test 的高显著性并不能推广到更广泛的 data conditions。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: 缺少 uniform × multi-epoch baseline**\n\n同意。论文的 epoch-matched D&R controls（Table 3）回答了\"D&R 在等 epoch 条件下是否优于 adaptive\"（answer: gap 仅 0.017），但未回答 R1 提出的更基本问题：**在包含合成数据的全部语料上做 3.2 epochs 的 uniform 训练，PPL 会如何？** 这个 baseline 可以区分两个假说：(a) D&R 的优势来自 filtering quality（去除坏数据）vs (b) 单纯来自 repetition（多看数据本身就有帮助，即使包含合成数据）。如果 uniform × 3.2 epochs 也大幅改善 PPL，那 D&R 的 \"filtering\" 叙事需要修正。\n\n这个 baseline 的计算成本很低（一次训练），应该被包含。\n\n**[AGREE] R1-W2: α_eff proxy 的 37% 未解释方差——但建议更具体**\n\n同意 R1 的核心关切。§6 \"Limitations of α_eff as a proxy\" 段定性地承认了 \"some batches satisfying α_eff ≥ τ may have true fractions below τ\"，但未给出具体的 violation 频率。Appendix J Table 12 报告了 Pearson r≈0.79（连续 formulation）和 consistent negative bias ≈-0.03，但 violation rate（α_eff ≥ 0.7 且 true real fraction < 0.7 的 batch 比例）是一个可以直接从现有数据计算的量，缺失是一个遗漏。\n\n不过我要补充一点 nuance：negative bias（α_eff 低估 true fraction）意味着方法偏向 conservative intervention（多干预而非少干预），这在 safety 角度是可取的——但也解释了 W3 中 b*≈0.9 系统高于 grid-optimal b=0.3 的问题。两个 weakness 是 mechanistically linked。\n\n**[REBUT] R1-W3: Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差——部分反驳**\n\nR1 的观察（b*≈0.9 > grid-optimal b=0.3）是准确的，但 \"违背 minimum intervention 原则\" 的结论需要 nuance：\n\n1. **比较框架不对等**：Grid-optimal b=0.3 是对所有 batch 施加固定 b 的全局最优值（Table 8, Appendix C），而 adaptive b* 是逐 batch 计算的。Mean b*≈0.9 ≠ \"每个 batch 都用 0.9\"。Figure 10（Appendix B, b* trajectory）显示 b* 在 0 到 ~5 之间大幅波动，包括 5.8% 的 clean batches（b*=0）。Per-batch 的 b* 分布均值为 0.9，但这不能简单类比为固定 b=0.9（fixed b=1.0 的 PPL=17.692 ≈ uniform，见 §5.1）。\n\n2. **PPL gap 的归因**：0.054 的 gap（adaptive 17.674 vs grid 17.620）部分来自 α_eff 的 negative bias 导致的 over-intervention，但也部分来自 grid-search 的 post-hoc oracle advantage（grid-best 是从 9 个候选中选出的最优值，具有 overfitting 风险；其 cross-seed SD=0.035 是 adaptive 的 ~6×，见 §5.1）。\n\n3. **但 R1 的核心 concern 成立**：α_eff 的 systematic negative bias（-0.03, Table 12）确实会系统性地推高 b*，这是 adaptive 方法的一个结构性缺陷。论文未讨论 bias correction 的可能性（如用 calibrated offset 调整 α_eff），这是一个改进方向。\n\n综合判断：R1 的观察有价值，但 \"违背 minimum intervention 原则\" 的表述过强。更准确的说法是 \"α_eff 的 systematic underestimation 导致 adaptive 方法未能完全实现 minimum intervention，有改进空间\"。\n\n**[AGREE] R1-W4: 3 个 detector 不足以支撑 AUC/ECE threshold 通用性**\n\n完全同意，这与我的 W4 一致。3 个 detectors（AUC 分别为 0.73/0.91/0.94）的采样密度不足以确定 AUC≥0.9 的阈值——AUC=0.85 或 0.88 的 detector 表现如何完全未知。ECE 方面同理：0.048 和 0.131 之间的巨大空白使得 ECE≤0.05 的 threshold 更像是一个 coincidental observation 而非 validated boundary。\n\n**[AGREE] R1-W5: Scale 效应递减 43%，practitioner 适用性存疑**\n\n同意。0.6B→1.7B 效应减半（Δ: -0.023 → -0.013），且 1.7B 的 OOD 结果方向不一致（§5.2: OWT -0.008, Wiki +0.013）。论文的解释（\"larger models being more robust to self-generated contamination\"）合理但也暗示了方法的结构性局限：如果效果依赖于 generator-trainee distribution mismatch，而 self-contamination 中 mismatch 随模型增大而缩小，那么方法在最常见的 self-contamination 场景下可能 inherently limited。\n\n---\n\n## 小问题\n\n**[AGREE] R1-M1: B=4 主实验低估方法潜力**\n\n同意。§5.3 的 batch-size amplification（B=4→16, Δ 从 -0.023 到 -0.068）暗示 B=4 不是方法的最佳展示。但论文选择 B=4 作为主实验有合理理由（\"reflecting memory constraints typical of continued pretraining setups\"），且 B=8/16 结果已在 §5.3 补充。这是 framing issue 而非 experimental flaw。\n\n**[AGREE] R1-M2: Paired t-test 正态性假设 n=5 下无法验证**\n\n同意，但这是 small-sample 研究的通用局限。论文提供了 directional consistency（所有 5 个 seed 都改善）作为补充证据，部分弥补了参数检验假设无法验证的问题。建议补充 non-parametric test（如 Wilcoxon signed-rank）作为 robustness check。\n\n**[REBUT] R1-M3: Abstract word count 接近 200-word 限制**\n\n不同意这是一个问题。我实际计数约 171 words，距离 200-word 限制还有约 29 words 的余量（~15%）。\"接近限制\" 不构成 weakness。\n\n---\n\n## Questions 回应\n\n**Q1: 是否有不同 data permutation 下的实验？**\n论文中没有。这与 N2 直接相关——如果增加 data ordering randomization 作为额外 stochastic axis，当前的高 Cohen's d 很可能显著下降。这是一个合理的 revision requirement。\n\n**Q2: Uniform × multi-epoch baseline 的预期结果？**\n同意 R1 的预期——这个 baseline 对区分 repetition vs filtering 至关重要。如果 uniform × 3.2 epochs 也大幅改善（例如达到 17.3-17.5 range），那 D&R 的 filtering 叙事需要大幅弱化；如果 uniform × 3.2 epochs 反而因为合成数据的 multi-epoch 放大而 degradation，则强化 filtering 的价值。两种结果都有信息量。\n\n**Q3: α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例？**\n同意这应该被报告。从现有数据（Appendix J, Table 12: MAE=0.114, bias=-0.03 at B=4）可以粗略推断 violation rate 不会太高（因为 negative bias 意味着 α_eff 倾向于低估，所以 α_eff ≥ τ 的 batch 通常 true fraction 也 ≥ τ），但精确数字应从数据中直接计算。\n\n**Q4: Calibration-corrected α_eff 能否缩小 b* vs grid-optimal 的 gap？**\n这是一个有建设性的建议。如果用 empirical bias correction（加回 +0.03 offset）调整 α_eff，b_τ 会降低（更少干预），可能使 mean b* 从 0.9 下降到更接近 grid-optimal 的 0.3-0.5 range。论文未探索这个方向，是一个合理的 revision suggestion。\n\n**Q5: 1.7B 实验选择 τ=0.8 而非 0.7 的理由？**\n论文在 §5.2 报告 1.7B 使用 τ=0.8 但未解释选择理由。考虑到 0.6B 的主结果推荐 τ=0.7（§5.3 Table 6 明确显示 τ=0.7 在 holdout 和 OOD 上均优于 τ=0.8），1.7B 却用 τ=0.8 缺乏 justification。如果 1.7B 用 τ=0.7 结果可能不同，这是一个 confound——无法确定 1.7B 效应减弱是因为 scale 还是因为 suboptimal τ。这是一个值得指出的实验设计问题。\n\n---\n\n## 综合评估\n\nR1 的审稿意见在方法论层面质量很高，多数 concerns 与我的独立评估一致。两份审稿的核心共识：\n\n1. **论文最大价值在分析贡献**（D&R epoch-matching、calibration finding），而非 adaptive method 本身\n2. **Effect size 过小且无下游影响**，practitioner framing 不恰当\n3. **实验 scope 过窄**，不足以支撑标题和 \"conditions\" 的一般性 claim\n4. **统计显著性的呈现方式**需要更多 caveats\n\n我维持 **Overall 3.0 (Findings)** 的评分。论文在其 scope 内 soundness 达标，但需要：(a) 重新定位为 mechanism analysis；(b) 修正 abstract 中的统计 overclaim；(c) 补充 uniform × multi-epoch baseline。",
  "reviewer_id": "2",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: Effect size 与 practitioner framing 之间的根本矛盾**\n\n同意。这与我的 N3（Abstract 未提及无下游提升）和 W5（效应量论证不足）一致。Δ=-0.023 PPL（0.13% relative）在 §6 被承认为 \"modest\"，但 Table 5 标题仍为 \"Decision summary for practitioners\"，且 Abstract 中 \"improves over uniform training\" 未限定为 PPL-only。论文内部存在定位矛盾：一方面诚实承认影响有限（§6 \"does not transfer to downstream accuracy\"），另一方面仍以 practitioner guidance 包装结论。\n\n补充发现：§7 Conclusion 最后一句提到 \"whether these conditions hold at full pretraining scale (>100B tokens)...is the central open question\"，但如果 0.6B→1.7B 效应已减半（§5.2, Δ=-0.013），且 1.7B OOD 方向不一致（OWT Δ=-0.008, Wiki Δ=+0.013），那么 full-scale 的前景进一步存疑。R1 建议重新定位为 mechanism analysis 是合理的——论文最有价值的贡献（D&R epoch-matching decomposition、calibration 发现）本质上是分析性的，不需要 practitioner framing 来体现价值。\n\n**[AGREE] R1-N2: Cohen's d = 3.83 被 deterministic data ordering 系统性放大**\n\n同意，这是一个重要的方法论问题。Appendix Q 明确承认 \"seeds affect only parameter initialization, not data order (the dataloader is deterministic), so the primary stochastic axis is initialization noise at 0.6B scale\"。这意味着 SD_Δ=0.006 仅反映初始化噪声的极小方差，而非方法在不同数据采样条件下的稳健性。\n\nCohen's d=3.83 和 power>0.99 的呈现方式在 §5.1 中给读者留下了\"效果极其稳健\"的印象，但实际上只是说\"在固定数据顺序下，不同初始化产生的结果非常一致\"——这是一个远弱于\"方法在不同条件下稳健有效\"的声明。论文在 Appendix Q 的透明度值得肯定（\"the low dispersion is a property of the experimental setting rather than a method artifact\"），但这个关键 caveat 应出现在 §5.1 主文而非仅在 appendix 中。\n\n补充：uniform baseline 也有类似的低方差（σ=0.008），说明窄方差确实是实验设定的属性。但这恰恰意味着 paired t-test 的高显著性并不能推广到更广泛的 data conditions。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: 缺少 uniform × multi-epoch baseline**\n\n同意。论文的 epoch-matched D&R controls（Table 3）回答了\"D&R 在等 epoch 条件下是否优于 adaptive\"（answer: gap 仅 0.017），但未回答 R1 提出的更基本问题：**在包含合成数据的全部语料上做 3.2 epochs 的 uniform 训练，PPL 会如何？** 这个 baseline 可以区分两个假说：(a) D&R 的优势来自 filtering quality（去除坏数据）vs (b) 单纯来自 repetition（多看数据本身就有帮助，即使包含合成数据）。如果 uniform × 3.2 epochs 也大幅改善 PPL，那 D&R 的 \"filtering\" 叙事需要修正。\n\n这个 baseline 的计算成本很低（一次训练），应该被包含。\n\n**[AGREE] R1-W2: α_eff proxy 的 37% 未解释方差——但建议更具体**\n\n同意 R1 的核心关切。§6 \"Limitations of α_eff as a proxy\" 段定性地承认了 \"some batches satisfying α_eff ≥ τ may have true fractions below τ\"，但未给出具体的 violation 频率。Appendix J Table 12 报告了 Pearson r≈0.79（连续 formulation）和 consistent negative bias ≈-0.03，但 violation rate（α_eff ≥ 0.7 且 true real fraction < 0.7 的 batch 比例）是一个可以直接从现有数据计算的量，缺失是一个遗漏。\n\n不过我要补充一点 nuance：negative bias（α_eff 低估 true fraction）意味着方法偏向 conservative intervention（多干预而非少干预），这在 safety 角度是可取的——但也解释了 W3 中 b*≈0.9 系统高于 grid-optimal b=0.3 的问题。两个 weakness 是 mechanistically linked。\n\n**[REBUT] R1-W3: Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差——部分反驳**\n\nR1 的观察（b*≈0.9 > grid-optimal b=0.3）是准确的，但 \"违背 minimum intervention 原则\" 的结论需要 nuance：\n\n1. **比较框架不对等**：Grid-optimal b=0.3 是对所有 batch 施加固定 b 的全局最优值（Table 8, Appendix C），而 adaptive b* 是逐 batch 计算的。Mean b*≈0.9 ≠ \"每个 batch 都用 0.9\"。Figure 10（Appendix B, b* trajectory）显示 b* 在 0 到 ~5 之间大幅波动，包括 5.8% 的 clean batches（b*=0）。Per-batch 的 b* 分布均值为 0.9，但这不能简单类比为固定 b=0.9（fixed b=1.0 的 PPL=17.692 ≈ uniform，见 §5.1）。\n\n2. **PPL gap 的归因**：0.054 的 gap（adaptive 17.674 vs grid 17.620）部分来自 α_eff 的 negative bias 导致的 over-intervention，但也部分来自 grid-search 的 post-hoc oracle advantage（grid-best 是从 9 个候选中选出的最优值，具有 overfitting 风险；其 cross-seed SD=0.035 是 adaptive 的 ~6×，见 §5.1）。\n\n3. **但 R1 的核心 concern 成立**：α_eff 的 systematic negative bias（-0.03, Table 12）确实会系统性地推高 b*，这是 adaptive 方法的一个结构性缺陷。论文未讨论 bias correction 的可能性（如用 calibrated offset 调整 α_eff），这是一个改进方向。\n\n综合判断：R1 的观察有价值，但 \"违背 minimum intervention 原则\" 的表述过强。更准确的说法是 \"α_eff 的 systematic underestimation 导致 adaptive 方法未能完全实现 minimum intervention，有改进空间\"。\n\n**[AGREE] R1-W4: 3 个 detector 不足以支撑 AUC/ECE threshold 通用性**\n\n完全同意，这与我的 W4 一致。3 个 detectors（AUC 分别为 0.73/0.91/0.94）的采样密度不足以确定 AUC≥0.9 的阈值——AUC=0.85 或 0.88 的 detector 表现如何完全未知。ECE 方面同理：0.048 和 0.131 之间的巨大空白使得 ECE≤0.05 的 threshold 更像是一个 coincidental observation 而非 validated boundary。\n\n**[AGREE] R1-W5: Scale 效应递减 43%，practitioner 适用性存疑**\n\n同意。0.6B→1.7B 效应减半（Δ: -0.023 → -0.013），且 1.7B 的 OOD 结果方向不一致（§5.2: OWT -0.008, Wiki +0.013）。论文的解释（\"larger models being more robust to self-generated contamination\"）合理但也暗示了方法的结构性局限：如果效果依赖于 generator-trainee distribution mismatch，而 self-contamination 中 mismatch 随模型增大而缩小，那么方法在最常见的 self-contamination 场景下可能 inherently limited。\n\n---\n\n## 小问题\n\n**[AGREE] R1-M1: B=4 主实验低估方法潜力**\n\n同意。§5.3 的 batch-size amplification（B=4→16, Δ 从 -0.023 到 -0.068）暗示 B=4 不是方法的最佳展示。但论文选择 B=4 作为主实验有合理理由（\"reflecting memory constraints typical of continued pretraining setups\"），且 B=8/16 结果已在 §5.3 补充。这是 framing issue 而非 experimental flaw。\n\n**[AGREE] R1-M2: Paired t-test 正态性假设 n=5 下无法验证**\n\n同意，但这是 small-sample 研究的通用局限。论文提供了 directional consistency（所有 5 个 seed 都改善）作为补充证据，部分弥补了参数检验假设无法验证的问题。建议补充 non-parametric test（如 Wilcoxon signed-rank）作为 robustness check。\n\n**[REBUT] R1-M3: Abstract word count 接近 200-word 限制**\n\n不同意这是一个问题。我实际计数约 171 words，距离 200-word 限制还有约 29 words 的余量（~15%）。\"接近限制\" 不构成 weakness。\n\n---\n\n## Questions 回应\n\n**Q1: 是否有不同 data permutation 下的实验？**\n论文中没有。这与 N2 直接相关——如果增加 data ordering randomization 作为额外 stochastic axis，当前的高 Cohen's d 很可能显著下降。这是一个合理的 revision requirement。\n\n**Q2: Uniform × multi-epoch baseline 的预期结果？**\n同意 R1 的预期——这个 baseline 对区分 repetition vs filtering 至关重要。如果 uniform × 3.2 epochs 也大幅改善（例如达到 17.3-17.5 range），那 D&R 的 filtering 叙事需要大幅弱化；如果 uniform × 3.2 epochs 反而因为合成数据的 multi-epoch 放大而 degradation，则强化 filtering 的价值。两种结果都有信息量。\n\n**Q3: α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例？**\n同意这应该被报告。从现有数据（Appendix J, Table 12: MAE=0.114, bias=-0.03 at B=4）可以粗略推断 violation rate 不会太高（因为 negative bias 意味着 α_eff 倾向于低估，所以 α_eff ≥ τ 的 batch 通常 true fraction 也 ≥ τ），但精确数字应从数据中直接计算。\n\n**Q4: Calibration-corrected α_eff 能否缩小 b* vs grid-optimal 的 gap？**\n这是一个有建设性的建议。如果用 empirical bias correction（加回 +0.03 offset）调整 α_eff，b_τ 会降低（更少干预），可能使 mean b* 从 0.9 下降到更接近 grid-optimal 的 0.3-0.5 range。论文未探索这个方向，是一个合理的 revision suggestion。\n\n**Q5: 1.7B 实验选择 τ=0.8 而非 0.7 的理由？**\n论文在 §5.2 报告 1.7B 使用 τ=0.8 但未解释选择理由。考虑到 0.6B 的主结果推荐 τ=0.7（§5.3 Table 6 明确显示 τ=0.7 在 holdout 和 OOD 上均优于 τ=0.8），1.7B 却用 τ=0.8 缺乏 justification。如果 1.7B 用 τ=0.7 结果可能不同，这是一个 confound——无法确定 1.7B 效应减弱是因为 scale 还是因为 suboptimal τ。这是一个值得指出的实验设计问题。\n\n---\n\n## 综合评估\n\nR1 的审稿意见在方法论层面质量很高，多数 concerns 与我的独立评估一致。两份审稿的核心共识：\n\n1. **论文最大价值在分析贡献**（D&R epoch-matching、calibration finding），而非 adaptive method 本身\n2. **Effect size 过小且无下游影响**，practitioner framing 不恰当\n3. **实验 scope 过窄**，不足以支撑标题和 \"conditions\" 的一般性 claim\n4. **统计显著性的呈现方式**需要更多 caveats\n\n我维持 **Overall 3.0 (Findings)** 的评分。论文在其 scope 内 soundness 达标，但需要：(a) 重新定位为 mechanism analysis；(b) 修正 abstract 中的统计 overclaim；(c) 补充 uniform × multi-epoch baseline。",
    "reviewer_id": "2",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-25T21:29:24.488397+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3696
}
```

</details>

---


### Assistant

_source line 1146 · 2026-05-25T21:29:30.747393+00:00_

已提交对 Reviewer 1 的逐条回应。核心结论：

- R1 的 10 条意见中，**8 条 AGREE**（N1, N2, W1, W2, W4, W5, M1, M2），**1 条 partial REBUT**（W3: adaptive b* vs grid-optimal 的比较框架不对等），**1 条 full REBUT**（M3: abstract word count 实际约 171 words，距限制有余量）
- 两份审稿的核心共识：论文应重新定位为 mechanism analysis，修正统计 overclaim，补充 uniform × multi-epoch baseline
- 维持 Overall 3.0 (Findings) 评分

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2"
}
```

</details>

---
