# writing notation figures audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_writing_notation-figures-audit_20260514T054927.jsonl`
- **Structured JSON:** [`c84436d6bce966294e7b.json`](../../sessions/c8/c84436d6bce966294e7b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-14T05:53:49.633301+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T05:53:49.633818+00:00_

docs/paper/experiments_c1.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T05:53:49.634071+00:00_

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
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T05:53:49.634260+00:00_

1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	% Template: standard article class (swap to acl.sty for final submission)
4	\documentclass[11pt,a4paper]{article}
5	\usepackage[margin=1in]{geometry}
6	\usepackage{times}
7	\usepackage{graphicx}
8	\usepackage{amsmath}
9	\usepackage{amssymb}
10	\usepackage{amsthm}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{hyperref}
15	\usepackage[numbers]{natbib}
16	\usepackage{enumitem}
17	\usepackage{subcaption}
18	
19	\newcommand{\Kstar}{K^*}
20	\newcommand{\Kempirical}{K^*_{\text{empirical}}}
21	\newcommand{\Ktheory}{K^*_{\text{theory}}}
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
34	Web-scale text corpora are increasingly contaminated by recursive synthetic content---text recursively generated across multiple generations. Information degrades monotonically per the Data Processing Inequality with each generation, yet no method estimates a document's generational depth. We introduce the first systematic framework for generational depth estimation. Our approach extracts 15 statistical features and classifies depth via Ordinal Binary Decomposition (OBD) with LightGBM, preserving ordinal structure. We empirically measure the discrimination boundary $\Kstar$, the maximum depth at which adjacent generations remain statistically distinguishable. Across 4 model-mode configurations and 4 decoding strategies (8 conditions total) at the $\leq$1.5B parameter scale, we find $\Kstar=2$ is consistent: bootstrap 95\% CI lower bounds for 1-vs-2 all exceed $\theta=0.60$ while all 2-vs-3 CI upper bounds fall below it; decoding strategies likewise yield AUC above $\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers 
…[truncated 1386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T05:53:49.634434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T05:53:49.634605+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Each pass through a language model constitutes a lossy channel: first-generation synthetic text retains much of the information structure of its human-written source, but within just two or three generations the output is qualitatively different---tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
6	This recursive degradation is not merely a theoretical concern; as synthetic text proliferates on the open web, training corpora inevitably ingest documents at varying generational depths, amplifying the risk of model collapse in downstream systems.
7	Yet the dominant paradigm in synthetic text detection treats all machine-generated text identically: a document is classified as human or synthetic, with no regard for how many rounds of recursive generation it has undergone.
8	This binary framing discards the generational depth dimension entirely.
9	
10	The gap cuts across three research communities.
11	Binary detection methods---including DivEye~\cite{basani2026diveye}, Min-K\%++~\cite{zhang2024minkpp}, and CoDeC~\cite{zawalski2026codec}---achieve strong human-versus-machine separation but produce no depth estimate.
12	The model collapse literature provides macro-level characterizations of recursive degradation: Shumailov et al.~\cite{shumailov2024collapse} demonstrated irreversible tail loss, Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved convergence to a fixed point, and Schaeffer et al.~\cite{schaeffer2025position} organized the field into a taxonomy of eight definitions---yet none of these works provides a tool for estimating the generational depth of an individual text.
13	Data selection methods such as DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023do
…[truncated 5407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T05:53:49.634764+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T05:53:49.635082+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model Collapse and Recursive Generation.}
5	Training on model-generated data can cause progressive distribution shift known as \emph{model collapse}.
6	Shumailov et al.~\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.
7	Alemohammad et al.~\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.
8	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.
9	Schaeffer et al.~\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.
10	Our $\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.
11	Kazdan et al.~\cite{kazdan2025collapse} distinguished \emph{replace} and \emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.
12	Our prompt-chain protocol operates in the replace regime, so $\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\Kstar$.
13	Shi et al.~\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.
14	Gerstgrasser et al.~\cite{gerstgrasser2024inevitable} proved that collapse is avoidable when sufficient original data is retained alongside synthetic samples, a condition that depth-aware curation can enforce by constru
…[truncated 6904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T05:53:49.635280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T05:53:49.635497+00:00_

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
15	Recursive text generation naturally forms an iterated lossy channel.
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
30	Since mutual information is bounded below by zero, this monotone sequence converges: the original signal degrades monotonically across generations.
31	Moreover, when the generation operator defines a finite-state Markov chain, the marginal distributions of adjacent generations converge to a shared stationary distribution, so that any classifier's ability to distinguish depth $k$ from depth $k{+}1$ must eventually degrade to chance.
32	Togethe
…[truncated 11404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T05:53:49.635652+00:00_

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
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T05:53:49.635959+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on four model configurations:
5	Pythia-1.4B and OLMo-1B in continuation mode, and Qwen2.5-1.5B-Instruct in both rewrite and continuation modes.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set described in Section~\ref{sec:method}.
7	Each configuration uses a balanced corpus of 5{,}000 texts per depth level (generations 0--5).
8	We organize results around four questions:
9	(1)~Does $\Kempirical = 2$ hold across configurations?
10	(2)~Do depth classifiers transfer across models?
11	(3)~Is the feature degradation ordering model-independent?
12	(4)~How does generation mode affect detectability?
13	
14	%% ====================================================================
15	\subsection{$\Kempirical = 2$ Across All Configurations}
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
30	All 0v1 permutation $p \leq 0.002$ (Qwen-continuation 0v1: CI [0.9963, 0.9978], $p = 0.002$).}
31	\label{tab:kstar_ci}
32	\begin{tabular}{lcccc}
33	\toprule
34	 & Qwen-rw & Pythia & OLMo & Qwen-cont \\
35	\midrule
36	0v1 & 0.9956 & 0.9932 & 0.9970 & 0.9971 \\[4pt]
37	1v2 & 0.6955 & 0.6539 & 0.6145 & 0.6112 \\
38	{\footnotesize CI}
39	  & {\footnotesize [.6859,\,.7041]}
40	  & {\footnotesize [.6454,\,.6630]}
41	  & {\footnotesize [.6045,\,.6247]}
42	  & {\footnotesize [.6015,\,.6213]} \\
43	{\footnote
…[truncated 14425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T05:53:49.636144+00:00_

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
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T05:53:49.636370+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	\label{sec:discuss_kstar}
6	
7	The Data Processing Inequality guarantees the existence of a finite $\Ktheory$ beyond which adjacent generations become indistinguishable (Section~\ref{sec:formulation}).
8	Our empirical result---$\Kempirical = 2$ uniformly across all 8 tested configurations (4 model-mode combinations from Section~\ref{sec:kstar_boundary} and 4 decoding strategies from the ablation)---establishes that this boundary is not only finite but remarkably shallow at the $\leq$1.5B parameter scale.
9	
10	The shallowness of $\Kempirical$ is explained by the rate of information loss across generations.
11	The 0v1 boundary is near-trivially separable ($\auc > 0.99$ across all configurations), reflecting the large distributional gap between human text and first-generation synthetic text.
12	At the 1v2 boundary, $\auc$ drops by approximately 30 percentage points ($\auc$ range: 0.6112--0.7039 across all eight model$\times$decoding conditions), indicating that the majority of the discriminative signal is consumed in the first generation step.
13	By the 2v3 boundary, $\auc$ falls to 0.5496--0.5917 across all eight model$\times$decoding conditions (upper bound from nucleus $p{=}0.9$ decoding; see Section~\ref{sec:discuss_kstar})---below the operational threshold $\theta = 0.60$---and deeper pairs converge toward chance.
14	Recursive generation thus acts as a severely lossy channel whose information bottleneck is traversed within two steps.
15	
16	The feature degradation analysis (Section~\ref{sec:feature_degradation}) provides mechanistic evidence for this rapid collapse.
17	The most discriminative features---surprisal variance (\texttt{surp\_d1\_std}, \texttt{surp\_std}) and its derivatives---all capture the heterogeneity of token-level predictability.
18	Human text exhibits high surprisal variance reflecting diverse syntactic structures and unpredictable 
…[truncated 17479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T05:53:49.636524+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T05:53:49.636703+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	% === Contribution 1: K*=2 universal boundary ===
5	% Sources: exp_007 (bootstrap CI + permutation), exp_001/exp_002/exp_017/mvp_pilot (model-mode), exp_003 (decoding ablation)
6	We presented the first systematic measurement of the generational depth
7	discrimination boundary $\Kempirical$ for recursive synthetic text.
8	Across three model architectures in four model-mode configurations
9	(Pythia-1.4B and OLMo-1B in continuation mode; Qwen2.5-1.5B-Instruct in both
10	continuation and rewrite modes) and 4 decoding strategies---totaling 8
11	conditions---we establish $\Kempirical = 2$ as a universal boundary:
12	classifiers reliably distinguish adjacent generations up to depth~2, but all
13	deeper pairs fall below the operational threshold $\theta = 0.60$.
14	For the four model-mode configurations, bootstrap 95\% confidence intervals
15	and permutation tests confirm statistical significance at the 1v2 boundary
16	($p \leq 0.002$ for all four); the most marginal case, Qwen-continuation,
17	yields a CI lower bound of 0.6015, exceeding $\theta$ by only 0.15\,pp.
18	All four decoding configurations (greedy, nucleus, $T{=}0.7$, $T{=}1.2$)
19	likewise yield 1v2 point-estimate $\auc$ above $\theta$.
20	The 0v1 boundary is near-perfectly separable ($\auc > 0.99$), followed by a
21	sharp ${\sim}$30\,pp drop at 1v2 ($\auc$: 0.6112--0.7039 across all
22	conditions), while all 2v3 pairs fall below~$\theta$.
23	Recursive generation thus acts as a severely lossy channel whose discriminable
24	statistical fingerprint is exhausted within two steps.
25	
26	% === Contribution 2: Ordinal depth estimation framework ===
27	% Sources: exp_010 (OBD vs baselines), exp_013 (cross-model transfer), exp_005 (feature degradation), exp_011 (LLM zero-shot)
28	To operationalize depth estimation, we introduced an ordinal binary
29	decomposition (OBD) framework pairing 15 hand-crafted statistical features
30	with LightGBM classifiers.
31	Cross-model
…[truncated 3048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T05:53:49.636985+00:00_

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
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T05:53:49.637158+00:00_

1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	  \centering
6	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
7	  \caption{Pairwise $\auc$ decay curves for four model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kstar=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
8	  \label{fig:s1_auc_decay_ci}
9	\end{figure}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T05:53:49.637359+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "K\\^?\\*|K\\^\\*|K\\^{?\\*}?|\\\\Kstar|\\\\Kempirical|\\\\Ktheory",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "tool_args": {
    "pattern": "K\\^?\\*|K\\^\\*|K\\^{?\\*}?|\\\\Kstar|\\\\Kempirical|\\\\Ktheory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T05:53:49.637492+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T05:53:49.637618+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "AUC|\\\\auc",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "tool_args": {
    "pattern": "AUC|\\\\auc",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T05:53:49.637847+00:00_

docs/paper/main.tex:22:\newcommand{\auc}{\text{AUC}}
docs/paper/main.tex:34:[Omitted long matching line]
docs/paper/conclusion.tex:19:likewise yield 1v2 point-estimate $\auc$ above $\theta$.
docs/paper/conclusion.tex:20:The 0v1 boundary is near-perfectly separable ($\auc > 0.99$), followed by a
docs/paper/conclusion.tex:21:sharp ${\sim}$30\,pp drop at 1v2 ($\auc$: 0.6112--0.7039 across all
docs/paper/conclusion.tex:33:Pythia$\leftrightarrow$OLMo achieving 90--92\% and 0v1 transfer $\auc$
docs/paper/conclusion.tex:45:A preliminary neural probing experiment suggests that this operational bound is not tight: a frozen Qwen2.5-1.5B encoder paired with an MLP classifier achieves $\Kempirical^{\text{neural}} = 3$ on the Qwen-continuation dataset (2v3 $\auc = 0.6195$ versus 0.5609 with hand-crafted features), indicating that learned representations recover depth signal beyond the 15-dimensional feature set.
docs/paper/experiments_c1.tex:18:Table~\ref{tab:kstar_ci} reports pairwise $\auc$ for adjacent depth pairs
docs/paper/experiments_c1.tex:26:\caption{Pairwise $\auc$ for adjacent depth pairs.  Bootstrap 95\% CIs
docs/paper/experiments_c1.tex:66:0v1 discrimination is near-perfect ($\auc > 0.99$),
docs/paper/experiments_c1.tex:67:followed by a sharp drop at 1v2 ($\auc$ range: 0.6112--0.6955),
docs/paper/experiments_c1.tex:69:($\auc$ range: 0.5496--0.5893).
docs/paper/experiments_c1.tex:76:\caption{Pairwise $\auc$ as a function of depth pair across four model-mode configurations (solid) and four decoding strategies (dashed).  All configurations show a sharp drop between 0v1 and 1v2, with 2v3 and deeper pairs falling below the decision threshold $\theta = 0.60$ (horizontal dashed line).  Error bars show bootstrap 95\% CIs for model-mode configurations; decoding strategy curves omit CIs as they were computed on a separate experimental setup.}
docs/paper/experiments_c1.tex:95:The absolute 1v2 $\auc$ varies across models:
docs/paper/experiments_c1.tex:187:At the 0v1 boundary, cr
…[truncated 10987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T05:53:49.638038+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\theta|θ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\theta|θ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T05:53:49.638215+00:00_

docs/paper/discussion.tex:13:By the 2v3 boundary, $\auc$ falls to 0.5496--0.5917 across all eight model$\times$decoding conditions (upper bound from nucleus $p{=}0.9$ decoding; see Section~\ref{sec:discuss_kstar})---below the operational threshold $\theta = 0.60$---and deeper pairs converge toward chance.
docs/paper/discussion.tex:30:A frozen Qwen2.5-1.5B encoder (1536-dimensional last-layer representations) paired with a lightweight MLP classifier achieves 2v3 $\auc = 0.6195$ ($\text{std} = 0.0094$) on the Qwen-continuation dataset, exceeding the $\theta = 0.60$ threshold that the same dataset's LightGBM classifier fails to cross ($\auc = 0.5609$; Section~\ref{sec:kstar_boundary}).
docs/paper/discussion.tex:33:At 3v4, the neural probe reaches $\auc = 0.5930$---below $\theta$ but closer to the threshold than any hand-crafted configuration---suggesting that a still richer representation might push the boundary further.
docs/paper/discussion.tex:109:$\Kempirical$ depends on the operational threshold $\theta$.
docs/paper/discussion.tex:110:$\Kempirical \geq 2$ across $\theta \in \{0.55, 0.60, 0.65\}$ for all four decoding strategies, rising to $\Kempirical = 3$ at $\theta = 0.55$ (all four 2v3 $\auc$ values exceed 0.55) and returning to $\Kempirical = 2$ at $\theta \in \{0.60, 0.65\}$; at $\theta = 0.70$, $\Kempirical = 1$ for all model-mode configurations.
docs/paper/discussion.tex:111:Beyond decoding parameters, the threshold sensitivity extends to generation mode: at $\theta{=}0.65$, continuation-mode configurations drop to $\Kempirical{=}1$, while rewrite mode retains $\Kempirical{=}2$.
docs/paper/discussion.tex:113:The boundary is robust within a practical range but not invariant to threshold choice; our conclusions are conditioned on $\theta = 0.60$.
docs/paper/discussion.tex:117:On the lower side, Qwen-continuation's 1v2 CI lower bound (0.6015) exceeds $\theta = 0.60$ by only $+$0.15\,pp.
docs/paper/discussion.tex:118:On the upper side, Qwen-rewrite's 2v3 CI upp
…[truncated 5926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T05:53:49.638373+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "[≥≤×±]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "tool_args": {
    "pattern": "[≥≤×±]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T05:53:49.638501+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T05:53:49.638619+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\caption\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-A": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\caption\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-A": "5"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T05:53:49.638791+00:00_

docs/paper/experiments_c1.tex:26:\caption{Pairwise $\auc$ for adjacent depth pairs.  Bootstrap 95\% CIs
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-27-and permutation $p$-values shown for the $\Kstar$ boundary rows (1v2,
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-28-2v3).  $\Kempirical = 2$ requires 1v2 $\text{CI}_\text{low} > \theta$
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-29-and 2v3 $\text{CI}_\text{high} < \theta$ with $\theta = 0.60$.
docs/paper/experiments_c1.tex-30-All 0v1 permutation $p \leq 0.002$ (Qwen-continuation 0v1: CI [0.9963, 0.9978], $p = 0.002$).}
docs/paper/experiments_c1.tex-31-\label{tab:kstar_ci}
--
docs/paper/experiments_c1.tex:76:\caption{Pairwise $\auc$ as a function of depth pair across four model-mode configurations (solid) and four decoding strategies (dashed).  All configurations show a sharp drop between 0v1 and 1v2, with 2v3 and deeper pairs falling below the decision threshold $\theta = 0.60$ (horizontal dashed line).  Error bars show bootstrap 95\% CIs for model-mode configurations; decoding strategy curves omit CIs as they were computed on a separate experimental setup.}
docs/paper/experiments_c1.tex-77-\label{fig:auc_decay}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-78-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-79-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-80-For the $\Kempirical$ determination, all four 1v2 CI lower bounds exceed
docs/paper/experiments_c1.tex-81-$\theta$: Qwen-rewrite ($\text{CI}_\text{low} = 0.6859$), Pythia (0.6454),
--
docs/paper/experiments_c1.tex:130:\caption{Cross-model transfer accuracy (6-cl
…[truncated 5239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T05:53:49.638949+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T05:53:49.639088+00:00_

docs/paper/related_work.tex:2:\label{sec:related_work}
docs/paper/conclusion.tex:2:\label{sec:conclusion}
docs/paper/experiments_c1.tex:2:\label{sec:experiments}
docs/paper/experiments_c1.tex:16:\label{sec:kstar_boundary}
docs/paper/experiments_c1.tex:31:\label{tab:kstar_ci}
docs/paper/experiments_c1.tex:77:\label{fig:auc_decay}
docs/paper/experiments_c1.tex:119:\label{sec:transfer}
docs/paper/experiments_c1.tex:135:\label{tab:transfer_matrix}
docs/paper/experiments_c1.tex:162:\label{fig:transfer_heatmap}
docs/paper/experiments_c1.tex:203:\label{sec:feature_degradation}
docs/paper/experiments_c1.tex:220:\label{tab:top_features}
docs/paper/experiments_c1.tex:292:\label{sec:generation_mode}
docs/paper/discussion.tex:2:\label{sec:discussion}
docs/paper/discussion.tex:5:\label{sec:discuss_kstar}
docs/paper/discussion.tex:43:\label{sec:discuss_transfer}
docs/paper/discussion.tex:58:\label{sec:discuss_features}
docs/paper/discussion.tex:73:\label{sec:discuss_llm}
docs/paper/discussion.tex:87:\label{sec:limitations}
docs/paper/discussion.tex:139:\label{sec:broader_impact}
docs/paper/method.tex:2:\label{sec:method}
docs/paper/method.tex:9:% \label{fig:pipeline}
docs/paper/method.tex:13:\label{sec:formulation}
docs/paper/method.tex:20:  \label{eq:markov}
docs/paper/method.tex:28:  \label{eq:dpi}
docs/paper/method.tex:38:  \label{eq:kstar}
docs/paper/method.tex:44:\label{sec:features}
docs/paper/method.tex:53:\label{tab:features}
docs/paper/method.tex:91:\label{sec:classifier}
docs/paper/method.tex:113:\label{sec:kstar_operational}
docs/paper/method.tex:130:\label{sec:experimental_setup}
docs/paper/method.tex:138:\label{tab:setup}
docs/paper/method.tex:167:\label{sec:generation_mode_method}
docs/paper/appendix.tex:8:  \label{fig:s1_auc_decay_ci}
docs/paper/introduction.tex:2:\label{sec:introduction}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T05:53:49.639217+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T05:53:49.639372+00:00_

docs/paper/experiments_c1.tex:6:All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set described in Section~\ref{sec:method}.
docs/paper/experiments_c1.tex:18:Table~\ref{tab:kstar_ci} reports pairwise $\auc$ for adjacent depth pairs
docs/paper/experiments_c1.tex:71:Figure~\ref{fig:auc_decay} visualizes this decay.
docs/paper/experiments_c1.tex:103:We examine both factors in Sections~\ref{sec:transfer}
docs/paper/experiments_c1.tex:104:and~\ref{sec:generation_mode}.
docs/paper/experiments_c1.tex:123:Table~\ref{tab:transfer_matrix} shows the full
docs/paper/experiments_c1.tex:165:Two principal findings emerge (Figure~\ref{fig:transfer_heatmap}).
docs/paper/experiments_c1.tex:253:(Table~\ref{tab:top_features}).
docs/paper/experiments_c1.tex:266:Section~\ref{sec:transfer}---rewrite-mode classifiers learn
docs/paper/experiments_c1.tex:295:Qwen2.5-1.5B-Instruct provides a controlled comparison: rewrite (instruction-based paraphrasing) and continuation (prompt truncation) share the same model weights, as defined in Section~\ref{sec:method}, isolating the effect of generation protocol.
docs/paper/discussion.tex:7:The Data Processing Inequality guarantees the existence of a finite $\Ktheory$ beyond which adjacent generations become indistinguishable (Section~\ref{sec:formulation}).
docs/paper/discussion.tex:8:Our empirical result---$\Kempirical = 2$ uniformly across all 8 tested configurations (4 model-mode combinations from Section~\ref{sec:kstar_boundary} and 4 decoding strategies from the ablation)---establishes that this boundary is not only finite but remarkably shallow at the $\leq$1.5B parameter scale.
docs/paper/discussion.tex:13:By the 2v3 boundary, $\auc$ falls to 0.5496--0.5917 across all eight model$\times$decoding conditions (upper bound from nucleus $p{=}0.9$ decoding; see Section~\ref{sec:discuss_kstar})---below the operational threshold $\theta = 0.60$---and deeper pairs converge toward chance.
docs/paper/discussion.tex:16:The fea
…[truncated 5272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T05:53:49.639516+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(Figure|Table|Section|Equation|Appendix)\\s+\\d",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(Figure|Table|Section|Equation|Appendix)\\s+\\d",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T05:53:49.639645+00:00_

docs/paper/main.tex:37:% === Section 1: Introduction ===
docs/paper/main.tex:40:% === Section 2: Related Work ===
docs/paper/main.tex:43:% === Section 3: Method ===
docs/paper/main.tex:46:% === Section 4: Experiments ===
docs/paper/main.tex:49:% === Section 4.x: Graduated Filtering (DEFERRED) ===
docs/paper/main.tex:52:% === Section 5: Discussion ===
docs/paper/main.tex:55:% === Section 6: Conclusion ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T05:53:49.639764+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\?\\?",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\?\\?",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T05:53:49.639903+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T05:53:49.640153+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "old_string": "decoding strategies likewise yield AUC above $\\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators, with binary (0-vs-1) AUC exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\\Kstar_{\\text{neural}}=3$, suggesting our 15-feature $\\Kstar=2$ is a representation-dependent lower bound.",
  "new_string": "decoding strategies likewise yield $\\auc$ above $\\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators, with binary (0-vs-1) $\\auc$ exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\\Kempirical^{\\text{neural}}=3$, suggesting our 15-feature $\\Kempirical=2$ is a representation-dependent lower bound."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "old_string": "decoding strategies likewise yield AUC above $\\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators, with binary (0-vs-1) AUC exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\\Kstar_{\\text{neural}}=3$, suggesting our 15-feature $\\Kstar=2$ is a representation-dependent lower bound.",
    "new_string": "decoding strategies likewise yield $\\auc$ above $\\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators, with binary (0-vs-1) $\\auc$ exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\\Kempirical^{\\text{neural}}=3$, suggesting our 15-feature $\\Kempirical=2$ is a representation-dependent lower bound."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T05:53:49.640299+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T05:53:49.640429+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "The shaded region marks the $\\Kstar=2$ boundary where $\\auc$ drops below $\\theta=0.60$.",
  "new_string": "The shaded region marks the $\\Kempirical=2$ boundary where $\\auc$ drops below $\\theta=0.60$."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "old_string": "The shaded region marks the $\\Kstar=2$ boundary where $\\auc$ drops below $\\theta=0.60$.",
    "new_string": "The shaded region marks the $\\Kempirical=2$ boundary where $\\auc$ drops below $\\theta=0.60$."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T05:53:49.640563+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T05:53:49.640684+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "old_string": "Results for graduated filtering (Section~\\ref{sec:graduated-filtering}) will be added upon completion of ongoing experiments.",
  "new_string": "Results for graduated filtering will be added upon completion of ongoing experiments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "old_string": "Results for graduated filtering (Section~\\ref{sec:graduated-filtering}) will be added upon completion of ongoing experiments.",
    "new_string": "Results for graduated filtering will be added upon completion of ongoing experiments."
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T05:53:49.640909+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T05:53:49.641082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "offset": "30",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "offset": "30",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T05:53:49.641222+00:00_

30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale text corpora are increasingly contaminated by recursive synthetic content---text recursively generated across multiple generations. Information degrades monotonically per the Data Processing Inequality with each generation, yet no method estimates a document's generational depth. We introduce the first systematic framework for generational depth estimation. Our approach extracts 15 statistical features and classifies depth via Ordinal Binary Decomposition (OBD) with LightGBM, preserving ordinal structure. We empirically measure the discrimination boundary $\Kstar$, the maximum depth at which adjacent generations remain statistically distinguishable. Across 4 model-mode configurations and 4 decoding strategies (8 conditions total) at the $\leq$1.5B parameter scale, we find $\Kstar=2$ is consistent: bootstrap 95\% CI lower bounds for 1-vs-2 across the four model-mode configurations all exceed $\theta=0.60$ while all 2-vs-3 CI upper bounds fall below it; decoding strategies likewise yield AUC above $\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\% accuracy across generators, with binary (0-vs-1) AUC exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\Kempirical^{\text{neural}}=3$, suggesting our 15-feature $\Kstar=2$ is a representation-dependent lower bound. Frontier LLMs achieve ${\sim}88\%$ binary detection but only ${\sim}33\%$ five-class depth accuracy---below our OBD classifier's 38.6\%---confirming depth estimation as a non-trivial task requiring specialized features. Our findings motivate a three-tier taxonomy (human / generation-1 / generation-2+) for depth-aware data curation; we investigate whether this coarse ordinal signal enables graduated filtering that outperforms binary approaches discarding all synthetic content indiscriminately.
35	\end{abstract}
36	
37	% === Section
…[truncated 48 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T05:53:49.641398+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "old_string": "decoding strategies likewise yield AUC above $\\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators, with binary (0-vs-1) AUC exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\\Kempirical^{\\text{neural}}=3$, suggesting our 15-feature $\\Kstar=2$ is a representation-dependent lower bound.",
  "new_string": "decoding strategies likewise yield $\\auc$ above $\\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators, with binary (0-vs-1) $\\auc$ exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\\Kempirical^{\\text{neural}}=3$, suggesting our 15-feature $\\Kempirical=2$ is a representation-dependent lower bound."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "old_string": "decoding strategies likewise yield AUC above $\\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators, with binary (0-vs-1) AUC exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\\Kempirical^{\\text{neural}}=3$, suggesting our 15-feature $\\Kstar=2$ is a representation-dependent lower bound.",
    "new_string": "decoding strategies likewise yield $\\auc$ above $\\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators, with binary (0-vs-1) $\\auc$ exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\\Kempirical^{\\text{neural}}=3$, suggesting our 15-feature $\\Kempirical=2$ is a representation-dependent lower bound."
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T05:53:49.641570+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_notation-figures-audit_20260514T054927",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-14T05:53:49.641739+00:00_

All fixes applied. Here's the report:

---

## 1. Notation 修复列表

| 位置 | 问题 | 修复 |
|------|------|------|
| `main.tex:34` (abstract) | 裸 "AUC" ×2（`yield AUC above`, `(0-vs-1) AUC exceeding`） | → `$\auc$` |
| `main.tex:34` (abstract) | `$\Kstar=2$`（15-feature 上下文中应为 empirical） | → `$\Kempirical=2$` |
| `appendix.tex:7` (caption) | `$\Kstar=2$`（指 empirical 结果） | → `$\Kempirical=2$` |

**无问题项：**
- `$\theta$`：全文统一使用 math mode，无裸 θ
- `≥ ≤ × ±`：无 Unicode 裸字符，全部使用 LaTeX 命令（`\leq`, `\geq`, `\times`, `\pm`）
- `$\auc$` macro：除 abstract 中已修复的两处外，其余全部通过 macro 使用
- `\Kstar` / `\Kempirical` / `\Ktheory`：正文中使用一致（generic concept 用 `\Kstar`，empirical result 用 `\Kempirical`，theoretical bound 用 `\Ktheory`）

## 2. Caption 状况

所有 caption 均自包含，无未展开缩写。具体评估：

- **Table 1** (`tab:features`): 简短但 table 内有 Group/Feature/Description 列，可接受
- **Table 3** (`tab:kstar_ci`): 自包含，定义了 threshold 条件
- **Figure 2** (`fig:auc_decay`): 优秀，完整描述了图中所有视觉元素
- **Table 4** (`tab:transfer_matrix`): 解释了矩阵结构和 retention 计算方式
- **Figure 3** (`fig:transfer_heatmap`): 自包含，有定量结论
- **Table 5** (`tab:top_features`): 解释了 bold 含义，包含 Spearman ρ 数值
- **Figure S1** (`fig:s1_auc_decay_ci`): 自包含（已修复 `\Kstar` → `\Kempirical`）

无需进一步修改。

## 3. Cross-reference 问题

| 位置 | 问题 | 修复 |
|------|------|------|
| `discussion.tex:136` | `\ref{sec:graduated-filtering}` 指向不存在的 label（对应 section 在 main.tex 中已注释） | 移除 `Section~\ref{...}`，改为纯文本 |

**其余 cross-ref 均完整：** 全部 33 个 `\ref{...}` 目标（17 个 section、5 个 table、3 个 figure、3 个 equation）都有对应 `\label{...}` 定义。无硬编码的 "Figure X" / "Table X" / "Section X"（仅注释中有）。无 `??` 输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_notation-figures-audit_20260514T054927"
}
```

</details>

---
