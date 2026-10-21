# review strategic review

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_review_strategic-review_20260514T075125.jsonl`
- **Structured JSON:** [`5e6f246b04d7e549f59f.json`](../../sessions/5e/5e6f246b04d7e549f59f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-14T07:52:25.708098+00:00_

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
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T07:52:25.708471+00:00_

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
34	Web-scale text corpora are increasingly contaminated by recursive synthetic content---text recursively generated across multiple generations. Information degrades monotonically per the Data Processing Inequality with each generation, yet no method estimates a document's generational depth. We introduce the first systematic framework for generational depth estimation. Our approach extracts 15 statistical features and classifies depth via Ordinal Binary Decomposition (OBD) with LightGBM, preserving ordinal structure. We empirically measure the discrimination boundary $\Kempirical$, the maximum depth at which adjacent generations remain statistically distinguishable. Across 4 model-mode configurations and 4 decoding strategies (8 conditions total) at the $\leq$1.5B parameter scale, we find $\Kempirical=2$ is consistent: bootstrap 95\% CI lower bounds for 1-vs-2 across the four model-mode configurations all exceed $\theta=0.60$ while all 2-vs-3 CI upper bounds fall below it; decoding strategies likewise yield $\auc$ above $\theta$ at 1-vs-2 and b
…[truncated 1472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T07:52:25.708667+00:00_

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
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T07:52:25.708897+00:00_

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
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T07:52:25.709083+00:00_

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
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T07:52:25.709261+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model Collapse and Recursive Generation.}
5	Training on model-generated data can cause progressive distribution shift known as \emph{model collapse}.
6	Shumailov et al.~\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.
7	Alemohammad et al.~\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.
8	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.
9	Further work shows that even a vanishingly small fraction of synthetic data suffices to trigger collapse, with the effect amplified in larger models~\citep{dohmatob2025strong}.
10	Schaeffer et al.~\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.
11	Our $\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.
12	Kazdan et al.~\cite{kazdan2025collapse} distinguished \emph{replace} and \emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.
13	Our prompt-chain protocol operates in the replace regime, so $\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\Kstar$.
14	Shi et al.~\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.
15	Gerstgrasser et al.~\cite{gerstgrasser2
…[truncated 7469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T07:52:25.709408+00:00_

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
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T07:52:25.709637+00:00_

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
…[truncated 11646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T07:52:25.709884+00:00_

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
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T07:52:25.710142+00:00_

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
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T07:52:25.710305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T07:52:25.710486+00:00_

1	\subsection{Graduated Filtering for Depth-Aware Data Curation}
2	\label{sec:graduated-filtering}
3	
4	The $\Kempirical = 2$ boundary establishes a three-tier taxonomy: human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
5	Binary filtering discards all synthetic content indiscriminately, sacrificing depth-1 text that retains most of the original signal.
6	We ask whether exploiting the coarse ordinal structure---weighting samples by predicted depth rather than applying a hard human/synthetic threshold---improves downstream language model quality.
7	
8	\paragraph{Filtering strategies.}
9	We compare six data curation strategies applied to a corpus of 30{,}000 documents (5{,}000 per depth level, depths 0--5) produced by the generational depth pipeline:
10	
11	\begin{enumerate}[label=(\roman*)]
12	  \item \textbf{No-filter}: all documents receive uniform weight (baseline).
13	
14	  \item \textbf{Binary-ours}: a LightGBM classifier trained on the 15-dimensional feature set distinguishes human (depth~0) from synthetic (depth~$\geq 1$).
15	  Each document receives weight $w = 1 - P(\text{synthetic})$.
16	  This represents the natural binary extension of our depth estimation framework.
17	
18	  \item \textbf{Binary-Drayson}: stratified importance resampling following Drayson et al.~\cite{drayson2025}, with $w_j = (1 - q(x_j))^b / Z$, $b = 1.5$, and oversampling factor $k = 1.5$.
19	  This is the strongest existing baseline for contamination-aware data curation.
20	
21	  \item \textbf{Graduated}: our proposed depth-aware strategy.
22	  The OBD-LightGBM classifier (Section~\ref{sec:classifier}) predicts a full depth distribution $P(d \mid \mathbf{x})$ for each document, from which we compute the expected depth $\hat{d} = \sum_d d \cdot P(d \mid \mathbf{x})$.
23	  Sample weights follow an exponential decay: $w = \exp(-\alpha \cdot \hat{d})$, where $\alpha$ controls the penalty for predicted depth.
24	  Low $\alpha$ values retain more s
…[truncated 6173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T07:52:25.710630+00:00_

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
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T07:52:25.710916+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	\label{sec:discuss_kstar}
6	
7	The Data Processing Inequality guarantees the existence of a finite $\Ktheory$ beyond which adjacent generations become indistinguishable (Section~\ref{sec:formulation}).
8	Our empirical result---$\Kempirical = 2$ consistently across all 8 tested configurations (4 model-mode combinations and 4 decoding strategies; Section~\ref{sec:kstar_boundary}, Figure~\ref{fig:auc_decay})---establishes that this boundary is not only finite but remarkably shallow at the $\leq$1.5B parameter scale.
9	
10	The shallowness of $\Kempirical$ is explained by the rate of information loss across generations.
11	The 0v1 boundary is near-trivially separable ($\auc > 0.99$ across all configurations; Table~\ref{tab:kstar_ci}), reflecting the large distributional gap between human text and first-generation synthetic text.
12	At the 1v2 boundary, $\auc$ drops by approximately 30 percentage points ($\auc$ range: 0.6112--0.7039 across all eight model$\times$decoding conditions; Table~\ref{tab:kstar_ci}, Figure~\ref{fig:auc_decay}; see also Figure~\ref{fig:s1_auc_decay_ci} in the Appendix), indicating that the majority of the discriminative signal is consumed in the first generation step.
13	By the 2v3 boundary, $\auc$ falls to 0.5496--0.5917 across all eight model$\times$decoding conditions (upper bound from nucleus $p{=}0.9$ decoding; Figure~\ref{fig:auc_decay})---below the operational threshold $\theta = 0.60$---and deeper pairs converge toward chance.
14	Recursive generation thus acts as a severely lossy channel whose information bottleneck is traversed within two steps.
15	
16	The feature degradation analysis (Section~\ref{sec:feature_degradation}) provides mechanistic evidence for this rapid collapse.
17	The most discriminative features---surprisal variance (\texttt{surp\_d1\_std}, \texttt{surp\_std}) and its derivatives---all capture the heterogenei
…[truncated 18125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T07:52:25.711177+00:00_

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
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T07:52:25.711446+00:00_

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
11	conditions---we establish $\Kempirical = 2$ as a consistent boundary:
12	classifiers reliably distinguish adjacent generations up to depth~2, but all
13	deeper pairs fall below the operational threshold $\theta = 0.60$.
14	For the four model-mode configurations, bootstrap 95\% confidence intervals
15	and permutation tests confirm statistical significance at the 1v2 boundary
16	($p \leq 0.002$ for all four); the most marginal case, Qwen-continuation,
17	yields a CI lower bound of 0.6015, exceeding $\theta$ by only 0.15\,pp.
18	All four decoding configurations (greedy, nucleus, $T{=}0.70$, $T{=}1.2$)
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
31	Cross-mod
…[truncated 3306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T07:52:25.711673+00:00_

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
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T07:52:25.712055+00:00_

1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	  \centering
6	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
7	  \caption{Pairwise $\auc$ decay curves for four model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
8	  \label{fig:s1_auc_decay_ci}
9	\end{figure}
10	
11	\section{Supplementary Tables}
12	
13	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
14	\begin{table*}[t]
15	  \centering
16	  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
17	  \label{tab:s1_transfer}
18	  \begin{tabular}{lcccc}
19	    \toprule
20	    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
21	    \cmidrule(lr){2-5}
22	    & Qwen-rw & Pythia & OLMo & Qwen-cont \\
23	    \midrule
24	    Qwen-rw   & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
25	    Pythia    & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
26	    OLMo      & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
27	    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
28	    \bottomrule
29	  \end{tabular}
30	  \vspace{4pt}
31	
32	  \footnotesize
33	  \textit{Transfer retention} between models $A$ and $B$ is defined as $\frac{1}{2}\bigl(\frac{\mathrm{acc}(A \to B)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}} + \frac{\mathrm{acc}(B \to A)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mat
…[truncated 12605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_strategic-review_20260514T075125",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T07:52:25.712403+00:00_

## Strategic Review — EMNLP Reviewer Perspective

### Q1: Weakest Sections

**1. `experiments_c3.tex` (Graduated Filtering).** The entire section is placeholder values. It's commented out in `main.tex:50`. This is the paper's secondary contribution (C3), and without results, the claim in `introduction.tex:50` ("we investigate whether...graduated filtering...can improve upon binary approaches") is an empty promise. The experimental structure (6 strategies, α sweep) is well-designed, but a section with `XX.X` values and TODO comments cannot survive review. If exp-006 doesn't complete in time, this section must either be cut entirely or repositioned as "proposed framework" with the downstream evaluation deferred.

**2. `conclusion.tex`.** Lines 48–53 contain a TODO placeholder for C3 results. The conclusion currently reads as if graduated filtering is a contribution, but delivers zero evidence. This creates a bait-and-switch: the abstract (main.tex:34) promises graduated filtering results, the conclusion promises them, but neither delivers. A reviewer will notice this inconsistency immediately.

### Q2: Thinnest Evidence Chains

**Claim (a): "suggesting universality beyond the specific models and decoding strategies studied"** (`introduction.tex:31`). This is over-claimed. The evidence covers 3 model families, all ≤1.5B, all English, all C4. "Universality" implies scale-invariant and language-invariant generalization. The limitations section (`discussion.tex:92–93`) correctly flags model scale, but the claim language in the intro doesn't hedge enough. The Qwen-continuation margin of 0.0015 above θ (`experiments_c1.tex:89–93`) makes this claim especially fragile.

**Claim (secondary): graduated filtering outperforms binary.** Zero evidence currently. The intro (`introduction.tex:50`) frames this as an investigation, which is defensible, but the abstract (`main.tex:34`) is stronger: "we investigate whether this coarse ordinal signal enables graduated filtering that outperforms binary approaches." Without results, this reads as an unsupported hypothesis rather than a contribution.

**Neural probe claim (K*_neural = 3).** Based on a single dataset, no bootstrap CIs, no cross-model validation (`discussion.tex:35`). The paper correctly caveats this, but it's cited 4+ times across sections as evidence that K_theory ≥ 3. Over-reliance on a preliminary single-dataset result weakens the credibility of the theoretical framing.

### Q3: Most Likely Rejection Reasons

**1. Scale limitation (≤1.5B only).** This is the single largest risk. A skeptical reviewer will argue that 1.5B models produce notoriously low-quality text, and K*=2 may simply reflect that small models produce easily distinguishable artifacts. The paper has no evidence that K*=2 holds for 7B/70B+ models. The "universality" language amplifies this vulnerability.

**2. Incomplete C3 / weak practical contribution.** Without graduated filtering results, the paper is a characterization study (K*=2) with limited practical impact. The depth estimation framework is interesting but incremental—the practical payoff (better data curation) is unproven. Reviewers increasingly expect "so what?" answers, and the paper currently can't deliver one for its secondary contribution.

**3. Threshold sensitivity / boundary marginality.** The K*=2 result hinges on θ=0.60. At θ=0.65, continuation-mode drops to K*=1 (`discussion.tex:112`). The Qwen-cont CI lower bound exceeds θ by only 0.0015 (`experiments_c1.tex:89`). A reviewer could argue that K*=2 is an artifact of threshold choice rather than a robust finding. The paper discusses this honestly, but the headline claim doesn't reflect the fragility.

### Q4: Pre-exp-006 Improvements

1. **Soften "universality" language.** Replace "suggesting universality" in `introduction.tex:31` with "consistent across all tested conditions at ≤1.5B scale." Similar adjustments in `discussion.tex:8` and `conclusion.tex:11-12`.

2. **Add a "what if C3 doesn't land" contingency.** Prepare an alternative framing where graduated filtering is presented as a proposed framework with theoretical motivation (the trichotomy follows logically from K*=2), and downstream validation is explicitly listed as future work. This is strictly weaker but avoids the current half-empty state.

3. **Strengthen the K*=2 narrative against scale critique.** Add a paragraph in Discussion arguing why K*=2 at small scale is informative even if larger models behave differently—it establishes a lower bound on the degradation rate and provides the first measurement methodology. Frame the scale limitation as motivation for follow-up, not as an invalidation.

4. **Tighten the abstract.** The abstract at 220+ words is dense. The graduated filtering sentence (main.tex:34) should either commit ("we show that") once results exist, or be cut to a single clause ("we propose graduated filtering as an application"). Currently it promises without delivering.

5. **Add a pipeline figure.** `method.tex:5-10` has a commented-out placeholder. A clear visual of seed → chain → features → OBD would significantly improve readability and is low-effort to produce.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_strategic-review_20260514T075125"
}
```

</details>

---
