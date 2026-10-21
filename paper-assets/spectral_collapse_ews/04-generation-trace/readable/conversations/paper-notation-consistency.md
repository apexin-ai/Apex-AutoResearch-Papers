# paper notation consistency

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 40
- **Original source:** `logs/chats/worker_paper_notation-consistency_20260519T181220.jsonl`
- **Structured JSON:** [`801d84f2fb220fff002c.json`](../../sessions/80/801d84f2fb220fff002c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

81 recorded events

### Tool call

_source line 1 · 2026-05-19T18:17:17.705050+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T18:17:17.705501+00:00_

paper/sections/related_work.tex
paper/sections/introduction.tex
paper/sections/abstract.tex
paper/sections/method.tex
paper/sections/experiments.tex
paper/sections/conclusion.tex
paper/main.tex
paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T18:17:17.705742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T18:17:17.705903+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
19	
20	\title{Spectral Early Warning Signals for Model Collapse in Recursive Synthetic Training}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\section{Introduction}
32	\label{sec:intro}
33	\input{sections/introduction}
34	
35	\section{Method}
36	\label{sec:method}
37	\input{sections/method}
38	
39	\section{Experiments}
40	\label{sec:experiments}
41	\input{sections/experiments}
42	
43	\section{Related Work}
44	\label{sec:related}
45	\input{sections/related_work}
46	
47	\section{Conclusion}
48	\label{sec:conclusion}
49	\input{sections/conclusion}
50	
51	\input{sections/limitations}
52	
53	\bibliography{references}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T18:17:17.706041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T18:17:17.706174+00:00_

1	Recursive synthetic training, where each model generation fine-tunes on its predecessor's outputs, causes model collapse: a progressive loss of distributional diversity and downstream capability.
2	Detecting collapse currently requires costly text generation or benchmark evaluation at every generation.
3	Spectral analysis of internal representations offers a cheaper alternative, but the spectral dynamics of recursive collapse lack systematic characterization, and no prior work connects spectral indicators to closed-loop prevention.
4	We track spectral properties of the embedding Gram matrix across 10 recursive generations of Pythia-410M, with pilot validation on Pythia-1B.
5	Our analysis reveals a reproducible three-phase pattern: spectral decompression (generations 0--2), where effective rank and spectral log-volume (SLV) increase even as downstream performance degrades; collapse onset (generations 2--4), where spectral indicators reverse; and accelerating collapse (generations 4--10), where spectral contraction proceeds at 2.43$\times$ the onset-generation rate.
6	Among the indicators we examine, SLV is particularly suited for automated monitoring: it requires only a forward pass on held-out data, captures distributed volume changes across all spectral directions, and exhibits post-decompression monotonic decline amenable to threshold-based control.
7	By varying the real-data mixing ratio across five levels, we construct a collapse phase diagram that localizes the critical mixing ratio $r_{\text{crit}}$ to the interval $(0.25, 0.3]$, separating monotonic spectral expansion from a transitional regime with initial contraction followed by recovery.
8	We further design a proof-of-concept proportional controller and discover a signal attenuation paradox: moderate real-data mixing prevents the spectral contraction that would activate the controller, so reactive spectral feedback becomes ineffective precisely when prevention succeeds.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T18:17:17.706318+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T18:17:17.706466+00:00_

1	
2	Synthetic data has become integral to language model training.
3	Instruction tuning, knowledge distillation, and data augmentation all routinely use model-generated text, and as synthetic corpora are recycled into training pipelines, the process often becomes recursive: each generation of models is fine-tuned on outputs from the previous one.
4	Recent work demonstrates that such recursive synthetic training triggers \textit{model collapse}, a progressive erosion of distributional tails and downstream capability~\cite{shumailov2024collapse, dohmatob2024tails, alemohammad2024mad}.
5	The problem is especially pressing as web-scraped corpora increasingly contain model-generated content, a trend that introduces implicit recursive loops even without deliberate data reuse.
6	
7	While model collapse is now well-characterized through theoretical analysis~\cite{dohmatob2024tails} and empirical studies~\cite{shumailov2024collapse, alemohammad2024mad}, its effect on the geometric structure of learned representations remains poorly understood.
8	Characterizing how the embedding space contracts during recursive training could yield computationally cheap collapse indicators from internal model states alone, without text generation or benchmark evaluation.
9	
10	Current collapse detection depends on downstream metrics such as perplexity and benchmark accuracy, or on analysis of generated text through lexical diversity measures.
11	Both approaches require either costly inference or external evaluation infrastructure at every generation.
12	SIGMA~\cite{gu2026sigma} introduced spectral monitoring through embedding covariance analysis and showed that spectral indicators can track collapse, but validated only on OPT-125M over short generation horizons.
13	Four gaps remain open.
14	First, no work has systematically characterized spectral dynamics beyond a few generations at 410M+ parameters.
15	Second, the temporal relationship between spectral indicators and downstream degradation 
…[truncated 2634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T18:17:17.706692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T18:17:17.706896+00:00_

1	\subsection{Spectral Metrics}
2	\label{subsec:spectral_metrics}
3	
4	Given a language model at generation $t$, we extract last-layer embeddings for $n{=}1{,}000$ held-out samples to form $\mathbf{E} \in \mathbb{R}^{n \times d}$ and compute the Gram matrix $\mathbf{G} = \mathbf{E}^\top \mathbf{E}$.
5	Let $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_d$ denote the singular values of $\mathbf{E}$.
6	We track three complementary spectral indicators:
7	
8	\paragraph{Spectral Log-Volume (SLV).}
9	$\text{SLV} = \sum_i \log \sigma_i = \frac{1}{2} \log \det \mathbf{G}$.
10	This quantity measures the total volume spanned by the embedding cloud in log-space.
11	Because it sums over all singular values, SLV is sensitive to contraction along any spectral direction, not only the dominant ones.
12	
13	\paragraph{Effective Rank.}
14	$r_{\text{eff}} = \exp(H(\mathbf{p}))$, where $p_i = \sigma_i / \sum_j \sigma_j$ and $H$ is the Shannon entropy, measuring how many dimensions carry substantial variance (uniform $\to d$, concentrated $\to 1$).
15	
16	\paragraph{Leading Singular Value.}
17	$\sigma_1$ tracks the dominant spectral direction; rising $\sigma_1$ under falling $r_{\text{eff}}$ signals representational collapse into a low-dimensional subspace.
18	
19	\subsection{Adaptive Mixing Controller}
20	\label{subsec:controller}
21	
22	We propose a closed-loop controller that adjusts the real-data mixing ratio $r_t$ at each generation based on the rate of spectral change.
23	The update rule is:
24	\begin{equation}
25	\label{eq:controller}
26	r_{t+1} = \frac{B_{\text{rem}}}{T - t} + k \cdot \max(0,\; \Delta_t - \tau)
27	\end{equation}
28	where $B_{\text{rem}}$ is the remaining real-data budget (fraction of total budget not yet consumed), $T$ is the total number of generations, $\tau{=}0.002$ is a sensitivity threshold, and $k{=}10$ is the controller gain.
29	The signal $\Delta_t$ is the baseline-normalized SLV drop: $\Delta_t = (\widetilde{S}_{t-1} - \widetilde{S}_t) / |\widetilde{S}_
…[truncated 3571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T18:17:17.707054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T18:17:17.707255+00:00_

1	
2	\subsection{Experimental Setup}
3	\label{subsec:setup}
4	
5	We use Pythia-410M-deduped \cite{biderman2023pythia} as our base model and fine-tune on a 50K-subset of OpenWebText.
6	Starting from the pretrained checkpoint (generation~0), each subsequent generation fine-tunes on synthetic text produced by the previous generation, for a total of 10 recursive generations.
7	At each generation we compute the spectral indicators from \S\ref{subsec:spectral_metrics} on the Gram matrix of 1K held-out last-layer embeddings, paired with three downstream metrics: perplexity, HellaSwag accuracy (0-shot), and distinct-4.
8	
9	For the mixing comparison (\S\ref{subsec:phase1}), we evaluate three strategies sharing the same total real-data budget:
10	(1)~\textbf{pure collapse} ($r_t{=}0$),
11	(2)~\textbf{fixed mix} ($r_t{=}0.50$), and
12	(3)~\textbf{adaptive} ($k{=}10$, Eq.~\ref{eq:controller}).
13	
14	\subsection{Spectral Collapse Characterization}
15	\label{subsec:phase0}
16	
17	Table~\ref{tab:phase0} reports spectral and downstream metrics across 10 recursive generations, which reveal a three-phase structure.
18	
19	\begin{table}[t]
20	\centering
21	\small
22	\begin{tabular}{@{}rrrrrrc@{}}
23	\toprule
24	Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
25	\midrule
26	0  & 417.55 & 2366.68 &  9.55 & .413 & .741 & 1942.8 \\
27	2  & \textbf{496.44} & \textbf{2469.93} & 13.58 & .376 & .515 &  712.0 \\
28	5  & 479.21 & 2370.17 & 24.59 & .344 & .463 &  741.0 \\
29	7  & 464.20 & 2304.19 & 38.89 & .319 & .447 &  791.3 \\
30	10 & 442.46 & 2178.95 & 76.78 & .295 & .426 &  825.7 \\
31	\bottomrule
32	\end{tabular}
33	\caption{Spectral and downstream metrics at selected generations (Pythia-410M; full trajectory described in text). Bold marks the spectral peak before collapse onset.}
34	\label{tab:phase0}
35	\end{table}
36	
37	\begin{figure}[t]
38	\centering
39	\includegraphics[width=\columnwidth]{figures/spectral_trajectory.pdf}
40	\caption{SLV across 10 recursive generatio
…[truncated 11750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T18:17:17.707406+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T18:17:17.707542+00:00_

1	
2	We presented a systematic spectral characterization of model collapse across 10 recursive generations of Pythia-410M and identified a three-phase trajectory (decompression, onset, 2.43$\times$ acceleration) confirmed at the 1B scale.
3	SLV is particularly suited for automated monitoring: it requires only a forward pass, declines monotonically after its peak, and captures volume changes before they manifest as dimensionality reduction.
4	By varying the mixing ratio across five levels, we construct a collapse phase diagram that localizes $r_{\text{crit}} \in (0.25, 0.3]$: above this threshold SLV expands monotonically (Type~III), while just below it a transitional regime (Type~II) exhibits an initial contraction transient followed by recovery.
5	A proof-of-concept proportional controller exposes a signal attenuation paradox.
6	The maximum per-generation controller signal weakens monotonically with the real-data fraction: $\max \Delta_t = 0.0019$ at $r{=}0.2$ (just below $\tau{=}0.002$), $0.00028$ at $r{=}0.25$ ($6.7\times$ weaker), and no decline signal at $r \geq 0.3$ where SLV expands monotonically.
7	The controller falls silent along a continuous gradient, not at a single threshold.
8	Because all seven EWS indicators reverse under sufficient mixing (\S\ref{subsec:alt_ews}), this paradox generalizes beyond SLV: any per-generation reactive controller faces the same tradeoff between prevention and detectability~\cite{scheffer2009ews}.
9	Even when mixing prevents spectral collapse, monitoring retains value: $r_{\text{crit}}$ varies across domains and architectures, and spectral indicators reveal whether the current ratio lies in the transitional or stable zone without waiting for downstream degradation.
10	
11	The signal attenuation paradox motivates three directions for future work.
12	First, cumulative indicators that integrate spectral trajectory shape across generations may detect sub-critical regimes where per-generation differences vanish.
13	Second, non-spe
…[truncated 400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T18:17:17.707754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T18:17:17.707910+00:00_

1	
2	\paragraph{Model Collapse.}
3	\citet{shumailov2024collapse} showed that recursive training on model-generated data progressively erodes the tails of learned distributions, a phenomenon they termed \emph{model collapse}.
4	\citet{dohmatob2024tails} formalized this decay through scaling laws that predict tail erosion as a function of recursive depth, and \citet{dohmatob2024demystified} provided a regression-theoretic analysis of the underlying mechanism.
5	The self-consuming loop accelerates collapse even under data accumulation~\cite{alemohammad2024mad}, and \citet{dohmatob2025strong} demonstrated that as little as 1\% synthetic contamination suffices to trigger degradation, though \citet{gerstgrasser2024inevitable} showed that preserving all prior real data can delay it.
6	These studies diagnose collapse through output distributions, benchmark scores, or theoretical scaling laws.
7	We complement them by tracking collapse through the spectral geometry of internal representations, which requires no text generation or external evaluation.
8	
9	\paragraph{Spectral Analysis of Representations.}
10	Random matrix theory (RMT) applied to neural network weights reveals implicit regularization structure in the eigenspectrum~\cite{martin2021implicit}.
11	Effective rank~\cite{roy2007effectiverank} and its normalized variant RankMe~\cite{rankme2023} have become standard tools for quantifying representational dimensionality.
12	Recent work has connected spectral properties to training pathologies: \citet{he2025spectral} linked spectral collapse in hidden representations to plasticity loss in continual learning, and \citet{naderi2025mindgap} identified spectral rank collapse in attention matrices as a failure mode of deep transformers.
13	Most directly relevant, \citet{gu2026sigma} proposed SIGMA, a spectral monitoring framework that tracks singular-value distributions during recursive training on OPT-125M over short horizons.
14	We extend this line of work along several axes
…[truncated 2078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T18:17:17.708055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T18:17:17.708178+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	All experiments use a single random seed; multi-seed replication is needed to establish statistical robustness.
5	We validate at two model scales only (Pythia-410M and a 1B pilot through Gen~3), leaving open whether the three-phase pattern holds at larger scales or with different architectures.
6	Ten recursive generations may be shorter than production pipelines, and the spectral trajectory beyond this horizon is unknown.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T18:17:17.708326+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "r_\\{?\\\\text\\{crit\\}|r_\\{?crit\\}|r_\\\\text\\{crit",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "r_\\{?\\\\text\\{crit\\}|r_\\{?crit\\}|r_\\\\text\\{crit",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:17:17.708471+00:00_

paper/sections/experiments.tex:72:Since pure collapse ($r{=}0$) produces SLV decline from Gen~3 while fixed mix ($r{=}0.5$) yields sustained growth from Gen~2, and $r{=}0.2$ falls below $r_{\text{crit}}$ (\S\ref{subsec:phase_diagram_exp}), we bound $0.2 < r_{\text{crit}} \leq 0.5$.
paper/sections/experiments.tex:110:This universality confirms that the signal attenuation paradox (\S\ref{subsec:controller}) is not specific to SLV: any per-generation reactive controller based on these indicators will fall silent when mixing exceeds $r_{\text{crit}}$.
paper/sections/experiments.tex:125:Because $\widetilde{S}_2 < \widetilde{S}_1$, the non-decreasing condition is violated and $r{=}0.2$ formally lies below $r_{\text{crit}}$.
paper/sections/experiments.tex:135:SLV rises monotonically from Gen~2 onward, reaching 2572 at Gen~10 ($+$8.7\% above baseline), consistent with $r{=}0.5 \geq r_{\text{crit}}$ (\S\ref{subsec:phase1}).
paper/sections/experiments.tex:137:These three types partition the mixing-ratio axis into collapse ($r < r_{\text{crit}}$), transitional, and stable ($r \geq r_{\text{crit}}$) zones.
paper/sections/experiments.tex:139:This confirms $r{=}0.3 \geq r_{\text{crit}}$ over the full 10-generation horizon, tightening the bound to $0.25 < r_{\text{crit}} \leq 0.3$.
paper/sections/experiments.tex:142:The Type~II trajectory clarifies what $r_{\text{crit}}$ marks in practice: not a boundary between collapse and stability in final outcome, but a transition in trajectory shape.
paper/sections/experiments.tex:143:Below $r_{\text{crit}}$, real-data mixing fails to suppress the initial SLV contraction transient but sustains spectral expansion over the observed five generations once the transient passes.
paper/sections/conclusion.tex:4:By varying the mixing ratio across five levels, we construct a collapse phase diagram that localizes $r_{\text{crit}} \in (0.25, 0.3]$: above this threshold SLV expands monotonically (Type~III), while just below it a transitional regime (Typ
…[truncated 2312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T18:17:17.708662+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\tilde\\{|\\\\widetilde\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\tilde\\{|\\\\widetilde\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T18:17:17.708820+00:00_

paper/sections/experiments.tex:125:Because $\widetilde{S}_2 < \widetilde{S}_1$, the non-decreasing condition is violated and $r{=}0.2$ formally lies below $r_{\text{crit}}$.
paper/sections/experiments.tex:128:The effective rank still rises at Gen~2 ($476.7 \to 481.6$) while the EMA-smoothed SLV registers a net decline ($\widetilde{S}_2 < \widetilde{S}_1$), evidence that smoothed SLV detects spectral contraction earlier at this mixing ratio.
paper/sections/experiments.tex:131:The EMA-smoothed sequence confirms the sub-critical classification: $\widetilde{S}_1 = 2364.4$, $\widetilde{S}_2 = 2363.8$, satisfying $\widetilde{S}_2 < \widetilde{S}_1$ and violating the non-decreasing condition.
paper/sections/method.tex:29:The signal $\Delta_t$ is the baseline-normalized SLV drop: $\Delta_t = (\widetilde{S}_{t-1} - \widetilde{S}_t) / |\widetilde{S}_0|$, where $\widetilde{S}_t$ is the exponential moving average (EMA)-smoothed SLV ($\alpha{=}0.5$) and $\widetilde{S}_0$ is initialized from the pretrained model (Gen~0, SLV${=}2366.68$).
paper/sections/method.tex:38:Define $r_{\text{crit}}$ as the minimum constant mixing ratio such that SLV is non-decreasing from the second generation onward: $\widetilde{S}_t \geq \widetilde{S}_{t-1}$ for all $t \in \{2, \ldots, T\}$ (excluding the initial fine-tuning transient at $t{=}1$).
paper/sections/method.tex:50:\Delta^2_t = \widetilde{\Delta}_{t-1} - \widetilde{\Delta}_t
paper/sections/method.tex:52:where $\widetilde{\Delta}_t$ is the EMA-smoothed first-order signal with smoothing parameter $\alpha_2$ (a tunable hyperparameter; we use $\alpha_2{=}0.3$ in our experiments).
paper/sections/method.tex:62:We estimate $r_{\text{crit}}$ by evaluating multiple constant ratios and identifying the lowest $r$ for which $\widetilde{S}_t \geq \widetilde{S}_{t-1}$ holds for all $t \in \{2, \ldots, T\}$.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T18:17:17.708957+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "r_\\{?\\\\text\\{eff\\}|r_\\{?eff\\}|r_\\\\text\\{eff",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "r_\\{?\\\\text\\{eff\\}|r_\\{?eff\\}|r_\\\\text\\{eff",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T18:17:17.709094+00:00_

paper/sections/experiments.tex:24:Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
paper/sections/experiments.tex:45:We identify phase boundaries at inflection points where $r_{\text{eff}}$ and SLV transition from rising to declining.
paper/sections/experiments.tex:46:In the first two generations, $r_{\text{eff}}$ rises from 417.55 to 496.44 (+18.9\%) and SLV increases from 2366.68 to 2469.93 (+4.4\%), while $\sigma_1$ drops sharply from 1942.8 to 712.0 as spectral mass redistributes from the dominant direction to smaller components.
paper/sections/experiments.tex:53:Both $r_{\text{eff}}$ and SLV reverse after Gen~2 ($r_{\text{eff}}$: 496.44$\to$493.31, SLV: 2470$\to$2441), and this reversal marks the transition from decompression to collapse while perplexity continues its monotonic rise.
paper/sections/experiments.tex:56:Spectral contraction accelerates: the mean per-generation percentage $r_{\text{eff}}$ decline in Phase~III is 2.43$\times$ the onset-generation rate (Gen~2$\to$3).
paper/sections/experiments.tex:57:By Gen~10, $r_{\text{eff}}$ falls to 442.46 ($-$10.9\% from peak), SLV drops to 2178.95 ($-$7.9\% from baseline), perplexity reaches 76.78 ($+$704\%), and $\sigma_1$ reverses its earlier decline (700.7$\to$825.7), a sign of renewed spectral concentration (Figure~\ref{fig:spectral_trajectory}).
paper/sections/experiments.tex:62:Repeating the protocol on Pythia-1B (Gen~0--3) confirms the same decompression-onset structure ($r_{\text{eff}}$ peak at Gen~2, SLV peak one generation earlier). SLV's low cost and monotonic post-peak decline make it well-suited as an automated collapse monitor.
paper/sections/method.tex:14:$r_{\text{eff}} = \exp(H(\mathbf{p}))$, where $p_i = \sigma_i / \sum_j \sigma_j$ and $H$ is the Shannon entropy, measuring how many dimensions carry substantial variance (uniform $\to d$, concentrated $\to 1$).
paper/sections/method.tex:17:$\sigma_1$ tracks the dominant spectral direction; rising $\sigma_1$ under falling $r_{\text
…[truncated 533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T18:17:17.709240+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\Delta_t|\\\\Delta t|\\\\Delta\\^2_t|\\\\Delta_\\{t",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\Delta_t|\\\\Delta t|\\\\Delta\\^2_t|\\\\Delta_\\{t",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T18:17:17.709380+00:00_

paper/sections/experiments.tex:70:The adaptive controller ($k{=}10$) remains silent through all ten generations: $\Delta_t$ is non-positive from Gen~2 onward, and the sole positive value ($\Delta_1 \approx 0.0003$) falls $6\times$ below $\tau{=}0.002$.
paper/sections/experiments.tex:71:Since $\Delta_t \leq 0$ for all $t \geq 2$, the controller stays silent for any finite $k$ and any $\tau > 0$ (\S\ref{subsec:controller}); larger gain values do not escape the paradox.
paper/sections/experiments.tex:127:Even at $r{=}0.2$, where SLV dips at Gen~2, the smoothed signal never exceeds the controller threshold ($\max \Delta_t = 0.0019 < \tau = 0.002$), so as little as 20\% real data silences the controller entirely.
paper/sections/experiments.tex:132:Controller silence is more pronounced than at $r{=}0.2$: $\max \Delta_t = 0.00028 < \tau = 0.002$, a $6.7\times$ weaker signal than the $r{=}0.2$ maximum ($0.0019$), consistent with further signal attenuation as the real-data fraction increases.
paper/sections/conclusion.tex:6:The maximum per-generation controller signal weakens monotonically with the real-data fraction: $\max \Delta_t = 0.0019$ at $r{=}0.2$ (just below $\tau{=}0.002$), $0.00028$ at $r{=}0.25$ ($6.7\times$ weaker), and no decline signal at $r \geq 0.3$ where SLV expands monotonically.
paper/sections/method.tex:26:r_{t+1} = \frac{B_{\text{rem}}}{T - t} + k \cdot \max(0,\; \Delta_t - \tau)
paper/sections/method.tex:29:The signal $\Delta_t$ is the baseline-normalized SLV drop: $\Delta_t = (\widetilde{S}_{t-1} - \widetilde{S}_t) / |\widetilde{S}_0|$, where $\widetilde{S}_t$ is the exponential moving average (EMA)-smoothed SLV ($\alpha{=}0.5$) and $\widetilde{S}_0$ is initialized from the pretrained model (Gen~0, SLV${=}2366.68$).
paper/sections/method.tex:30:The signed form ensures that spectral decompression ($\Delta_t < 0$) does not trigger the controller; only contraction activates the $\max(0, \cdot)$ gate in Eq.~\ref{eq:controller}.
paper/sections/method.tex:3
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T18:17:17.709523+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "r\\{=\\}|r=0\\.|r =",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "r\\{=\\}|r=0\\.|r =",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T18:17:17.709718+00:00_

paper/sections/experiments.tex:72:Since pure collapse ($r{=}0$) produces SLV decline from Gen~3 while fixed mix ($r{=}0.5$) yields sustained growth from Gen~2, and $r{=}0.2$ falls below $r_{\text{crit}}$ (\S\ref{subsec:phase_diagram_exp}), we bound $0.2 < r_{\text{crit}} \leq 0.5$.
paper/sections/experiments.tex:83:Table~\ref{tab:ews_comparison} summarizes the comparison under pure-synthetic training ($r{=}0$).
paper/sections/experiments.tex:105:\caption{Alternative early warning indicators under pure-synthetic training ($r{=}0$, Pythia-410M, 10 gen). \textbf{Peak}: generation at which the indicator reverses (--- = monotonic from Gen~0). \textbf{Mono?}: post-peak monotonicity (\checkmark\ = yes; number = violations). \textbf{Rel $\Delta$}: total relative change Gen~0--10. \textbf{Rev.?}: direction reversal under $r{=}0.5$ mixing (\checkmark\ = reversed).}
paper/sections/experiments.tex:119:\paragraph{Type~I: Pure Collapse ($r{=}0$).}
paper/sections/experiments.tex:123:\paragraph{Type~II: Near-critical Mixing ($r{=}0.2$).}
paper/sections/experiments.tex:124:Twenty percent real data suppresses the SLV decompression phase: SLV rises only 0.8 points from Gen~0 to Gen~1 (vs.\ $+$98 under $r{=}0$), dips at Gen~2 ($2367.5 \to 2358.3$, $-9.2$), then recovers through Gen~3--5 ($2362.5 \to 2379.2 \to 2399.0$, accelerating at $+4.2$, $+16.7$, $+19.7$ per generation), surpassing the Gen~0 baseline by 32.2 points at Gen~5.
paper/sections/experiments.tex:125:Because $\widetilde{S}_2 < \widetilde{S}_1$, the non-decreasing condition is violated and $r{=}0.2$ formally lies below $r_{\text{crit}}$.
paper/sections/experiments.tex:127:Even at $r{=}0.2$, where SLV dips at Gen~2, the smoothed signal never exceeds the controller threshold ($\max \Delta_t = 0.0019 < \tau = 0.002$), so as little as 20\% real data silences the controller entirely.
paper/sections/experiments.tex:130:At $r{=}0.25$, the full 10-generation trajectory follows the same Type~II pattern: SLV dips from Gen~0 to Gen~1
…[truncated 1718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T18:17:17.709874+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\sigma_1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\sigma_1",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T18:17:17.710005+00:00_

paper/sections/experiments.tex:24:Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
paper/sections/experiments.tex:46:In the first two generations, $r_{\text{eff}}$ rises from 417.55 to 496.44 (+18.9\%) and SLV increases from 2366.68 to 2469.93 (+4.4\%), while $\sigma_1$ drops sharply from 1942.8 to 712.0 as spectral mass redistributes from the dominant direction to smaller components.
paper/sections/experiments.tex:57:By Gen~10, $r_{\text{eff}}$ falls to 442.46 ($-$10.9\% from peak), SLV drops to 2178.95 ($-$7.9\% from baseline), perplexity reaches 76.78 ($+$704\%), and $\sigma_1$ reverses its earlier decline (700.7$\to$825.7), a sign of renewed spectral concentration (Figure~\ref{fig:spectral_trajectory}).
paper/sections/method.tex:5:Let $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_d$ denote the singular values of $\mathbf{E}$.
paper/sections/method.tex:17:$\sigma_1$ tracks the dominant spectral direction; rising $\sigma_1$ under falling $r_{\text{eff}}$ signals representational collapse into a low-dimensional subspace.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T18:17:17.710182+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{(tab|fig):",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{(tab|fig):",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T18:17:17.710311+00:00_

paper/sections/experiments.tex:34:\label{tab:phase0}
paper/sections/experiments.tex:41:\label{fig:spectral_trajectory}
paper/sections/experiments.tex:106:\label{tab:ews_comparison}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T18:17:17.710429+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{(tab|fig):",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{(tab|fig):",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T18:17:17.710551+00:00_

paper/sections/experiments.tex:17:Table~\ref{tab:phase0} reports spectral and downstream metrics across 10 recursive generations, which reveal a three-phase structure.
paper/sections/experiments.tex:57:By Gen~10, $r_{\text{eff}}$ falls to 442.46 ($-$10.9\% from peak), SLV drops to 2178.95 ($-$7.9\% from baseline), perplexity reaches 76.78 ($+$704\%), and $\sigma_1$ reverses its earlier decline (700.7$\to$825.7), a sign of renewed spectral concentration (Figure~\ref{fig:spectral_trajectory}).
paper/sections/experiments.tex:83:Table~\ref{tab:ews_comparison} summarizes the comparison under pure-synthetic training ($r{=}0$).
paper/sections/experiments.tex:109:The final column of Table~\ref{tab:ews_comparison} reveals that all seven indicators reverse direction under 50\% real-data mixing.
paper/sections/introduction.tex:20:Our analysis reveals a reproducible three-phase pattern (Figure~\ref{fig:spectral_trajectory}): spectral decompression (Gen~0--2), where effective rank ($r_{\text{eff}}$) and spectral log-volume (SLV) rise while downstream performance already declines; collapse onset (Gen~2--4), where spectral indicators reverse; and accelerating collapse (Gen~4--10), where contraction proceeds at 2.43$\times$ the onset-generation rate.
paper/sections/introduction.tex:26:\item \textbf{C1:} The first joint spectral-downstream characterization at 410M+ scale: a three-phase collapse pattern (decompression, onset, 2.43$\times$ acceleration) across 10 generations (\S\ref{subsec:phase0}, Table~\ref{tab:phase0}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T18:17:17.710725+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\b|\\\\citet\\b|\\\\citep\\b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\b|\\\\citet\\b|\\\\citep\\b",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T18:17:17.710881+00:00_

paper/sections/related_work.tex:3:\citet{shumailov2024collapse} showed that recursive training on model-generated data progressively erodes the tails of learned distributions, a phenomenon they termed \emph{model collapse}.
paper/sections/related_work.tex:4:\citet{dohmatob2024tails} formalized this decay through scaling laws that predict tail erosion as a function of recursive depth, and \citet{dohmatob2024demystified} provided a regression-theoretic analysis of the underlying mechanism.
paper/sections/related_work.tex:5:The self-consuming loop accelerates collapse even under data accumulation~\cite{alemohammad2024mad}, and \citet{dohmatob2025strong} demonstrated that as little as 1\% synthetic contamination suffices to trigger degradation, though \citet{gerstgrasser2024inevitable} showed that preserving all prior real data can delay it.
paper/sections/related_work.tex:10:Random matrix theory (RMT) applied to neural network weights reveals implicit regularization structure in the eigenspectrum~\cite{martin2021implicit}.
paper/sections/related_work.tex:11:Effective rank~\cite{roy2007effectiverank} and its normalized variant RankMe~\cite{rankme2023} have become standard tools for quantifying representational dimensionality.
paper/sections/related_work.tex:12:Recent work has connected spectral properties to training pathologies: \citet{he2025spectral} linked spectral collapse in hidden representations to plasticity loss in continual learning, and \citet{naderi2025mindgap} identified spectral rank collapse in attention matrices as a failure mode of deep transformers.
paper/sections/related_work.tex:13:Most directly relevant, \citet{gu2026sigma} proposed SIGMA, a spectral monitoring framework that tracks singular-value distributions during recursive training on OPT-125M over short horizons.
paper/sections/related_work.tex:17:The theory of early warning signals (EWS) for critical transitions originates in ecology, where \citet{scheffer2009ews} established that rising auto
…[truncated 3364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T18:17:17.711029+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Gen[ ~]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Gen[ ~]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T18:17:17.711190+00:00_

paper/sections/experiments.tex:24:Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
paper/sections/experiments.tex:40:\caption{SLV across 10 recursive generations of Pythia-410M under pure-synthetic training (solid) and 50\% real-data mixing (dashed). Three phases are visible in the pure-synthetic trajectory: decompression (Gen~0--2, SLV peaks at 2470), onset (Gen~2--4), and acceleration (Gen~4--10, SLV falls 12\% from peak to 2179). Under 50\% mixing, SLV rises monotonically (except a negligible Gen~1 dip) to 2572 at Gen~10, 8.7\% above baseline and 102 points above the pure-collapse peak.}
paper/sections/experiments.tex:44:\paragraph{Phase I: Spectral Decompression (Gen 0--2).}
paper/sections/experiments.tex:48:HellaSwag already declines 5.6\% from Gen~0 to Gen~1, precisely when spectral indicators are still rising; this asymmetry suggests that decompression captures distributional broadening rather than preservation of task-supporting representations.
paper/sections/experiments.tex:52:\paragraph{Phase II: Collapse Onset (Gen 2--4).}
paper/sections/experiments.tex:53:Both $r_{\text{eff}}$ and SLV reverse after Gen~2 ($r_{\text{eff}}$: 496.44$\to$493.31, SLV: 2470$\to$2441), and this reversal marks the transition from decompression to collapse while perplexity continues its monotonic rise.
paper/sections/experiments.tex:55:\paragraph{Phase III: Accelerating Collapse (Gen 4--10).}
paper/sections/experiments.tex:56:Spectral contraction accelerates: the mean per-generation percentage $r_{\text{eff}}$ decline in Phase~III is 2.43$\times$ the onset-generation rate (Gen~2$\to$3).
paper/sections/experiments.tex:57:By Gen~10, $r_{\text{eff}}$ falls to 442.46 ($-$10.9\% from peak), SLV drops to 2178.95 ($-$7.9\% from baseline), perplexity reaches 76.78 ($+$704\%), and $\sigma_1$ reverses its earlier decline (700.7$\to$825.7), a sign of renewed spectral concentration (Figure~\ref{fig:spectral_trajectory}).
paper/sections/experiments.tex:62:Repeating the protoco
…[truncated 6381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T18:17:17.711337+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\%",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T18:17:17.711484+00:00_

paper/sections/related_work.tex:5:The self-consuming loop accelerates collapse even under data accumulation~\cite{alemohammad2024mad}, and \citet{dohmatob2025strong} demonstrated that as little as 1\% synthetic contamination suffices to trigger degradation, though \citet{gerstgrasser2024inevitable} showed that preserving all prior real data can delay it.
paper/sections/experiments.tex:40:\caption{SLV across 10 recursive generations of Pythia-410M under pure-synthetic training (solid) and 50\% real-data mixing (dashed). Three phases are visible in the pure-synthetic trajectory: decompression (Gen~0--2, SLV peaks at 2470), onset (Gen~2--4), and acceleration (Gen~4--10, SLV falls 12\% from peak to 2179). Under 50\% mixing, SLV rises monotonically (except a negligible Gen~1 dip) to 2572 at Gen~10, 8.7\% above baseline and 102 points above the pure-collapse peak.}
paper/sections/experiments.tex:46:In the first two generations, $r_{\text{eff}}$ rises from 417.55 to 496.44 (+18.9\%) and SLV increases from 2366.68 to 2469.93 (+4.4\%), while $\sigma_1$ drops sharply from 1942.8 to 712.0 as spectral mass redistributes from the dominant direction to smaller components.
paper/sections/experiments.tex:47:Crucially, this decompression does not indicate improved model quality: HellaSwag drops from 0.413 to 0.376 ($-$8.9\%) and distinct-4 falls from 0.741 to 0.515 ($-$30.5\%) during the same interval.
paper/sections/experiments.tex:48:HellaSwag already declines 5.6\% from Gen~0 to Gen~1, precisely when spectral indicators are still rising; this asymmetry suggests that decompression captures distributional broadening rather than preservation of task-supporting representations.
paper/sections/experiments.tex:57:By Gen~10, $r_{\text{eff}}$ falls to 442.46 ($-$10.9\% from peak), SLV drops to 2178.95 ($-$7.9\% from baseline), perplexity reaches 76.78 ($+$704\%), and $\sigma_1$ reverses its earlier decline (700.7$\to$825.7), a sign of renewed spectral concentration (Figure~\ref{fig:spect
…[truncated 2905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T18:17:17.711641+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "SLV|EWS|EMA|PPL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "SLV|EWS|EMA|PPL",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T18:17:17.711771+00:00_

5:Our analysis reveals a reproducible three-phase pattern: spectral decompression (generations 0--2), where effective rank and spectral log-volume (SLV) increase even as downstream performance degrades; collapse onset (generations 2--4), where spectral indicators reverse; and accelerating collapse (generations 4--10), where spectral contraction proceeds at 2.43$\times$ the onset-generation rate.
6:Among the indicators we examine, SLV is particularly suited for automated monitoring: it requires only a forward pass on held-out data, captures distributed volume changes across all spectral directions, and exhibits post-decompression monotonic decline amenable to threshold-based control.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T18:17:17.711991+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\bEWS\\b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\bEWS\\b",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T18:17:17.712132+00:00_

paper/sections/related_work.tex:17:The theory of early warning signals (EWS) for critical transitions originates in ecology, where \citet{scheffer2009ews} established that rising autocorrelation and variance precede regime shifts in complex systems.
paper/sections/related_work.tex:18:\citet{dakos2012methods} developed a methodological toolbox for detecting these signals, and \citet{bury2021deeplearning} showed that deep learning can identify EWS in systems where classical indicators fail.
paper/sections/related_work.tex:19:A central tension in EWS theory is that stabilization interventions suppress the very precursors they rely on~\cite{scheffer2009ews}.
paper/sections/experiments.tex:77:\subsection{Alternative EWS Comparison}
paper/sections/conclusion.tex:8:Because all seven EWS indicators reverse under sufficient mixing (\S\ref{subsec:alt_ews}), this paradox generalizes beyond SLV: any per-generation reactive controller faces the same tradeoff between prevention and detectability~\cite{scheffer2009ews}.
paper/sections/conclusion.tex:14:Third, hybrid approaches combining spectral EWS with periodic probing at reduced real-data fractions may sustain controller sensitivity without sacrificing collapse prevention.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T18:17:17.712263+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\bEMA\\b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\bEMA\\b",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T18:17:17.712388+00:00_

paper/sections/experiments.tex:128:The effective rank still rises at Gen~2 ($476.7 \to 481.6$) while the EMA-smoothed SLV registers a net decline ($\widetilde{S}_2 < \widetilde{S}_1$), evidence that smoothed SLV detects spectral contraction earlier at this mixing ratio.
paper/sections/experiments.tex:131:The EMA-smoothed sequence confirms the sub-critical classification: $\widetilde{S}_1 = 2364.4$, $\widetilde{S}_2 = 2363.8$, satisfying $\widetilde{S}_2 < \widetilde{S}_1$ and violating the non-decreasing condition.
paper/sections/method.tex:29:The signal $\Delta_t$ is the baseline-normalized SLV drop: $\Delta_t = (\widetilde{S}_{t-1} - \widetilde{S}_t) / |\widetilde{S}_0|$, where $\widetilde{S}_t$ is the exponential moving average (EMA)-smoothed SLV ($\alpha{=}0.5$) and $\widetilde{S}_0$ is initialized from the pretrained model (Gen~0, SLV${=}2366.68$).
paper/sections/method.tex:52:where $\widetilde{\Delta}_t$ is the EMA-smoothed first-order signal with smoothing parameter $\alpha_2$ (a tunable hyperparameter; we use $\alpha_2{=}0.3$ in our experiments).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T18:17:17.712511+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\bPPL\\b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\bPPL\\b",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T18:17:17.712645+00:00_

paper/sections/experiments.tex:24:Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
paper/sections/experiments.tex:102:PPL growth  & ppl       & ---   & $\sim$\,(1) &  ---   & \checkmark \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T18:17:17.712767+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "generation [0-9]|generations [0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "generation [0-9]|generations [0-9]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T18:17:17.712888+00:00_

paper/sections/abstract.tex:5:Our analysis reveals a reproducible three-phase pattern: spectral decompression (generations 0--2), where effective rank and spectral log-volume (SLV) increase even as downstream performance degrades; collapse onset (generations 2--4), where spectral indicators reverse; and accelerating collapse (generations 4--10), where spectral contraction proceeds at 2.43$\times$ the onset-generation rate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T18:17:17.713006+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Gen [0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Gen [0-9]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T18:17:17.713122+00:00_

paper/sections/experiments.tex:44:\paragraph{Phase I: Spectral Decompression (Gen 0--2).}
paper/sections/experiments.tex:52:\paragraph{Phase II: Collapse Onset (Gen 2--4).}
paper/sections/experiments.tex:55:\paragraph{Phase III: Accelerating Collapse (Gen 4--10).}
paper/sections/experiments.tex:96:SLV         & emb-Gram  & Gen 2 & \checkmark & 11.8\% & \checkmark \\
paper/sections/experiments.tex:97:RankMe      & emb-SVD   & Gen 2 & \checkmark &  4.7\% & \checkmark \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T18:17:17.713236+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "[0-9]-[0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "[0-9]-[0-9]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T18:17:17.713345+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T18:17:17.713522+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{subsec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{subsec:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T18:17:17.713671+00:00_

paper/sections/experiments.tex:3:\label{subsec:setup}
paper/sections/experiments.tex:15:\label{subsec:phase0}
paper/sections/experiments.tex:60:\label{subsec:cross_scale}
paper/sections/experiments.tex:65:\label{subsec:phase1}
paper/sections/experiments.tex:78:\label{subsec:alt_ews}
paper/sections/experiments.tex:114:\label{subsec:phase_diagram_exp}
paper/sections/method.tex:2:\label{subsec:spectral_metrics}
paper/sections/method.tex:20:\label{subsec:controller}
paper/sections/method.tex:44:\label{subsec:second_order}
paper/sections/method.tex:57:\label{subsec:phase_diagram}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T18:17:17.713797+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{subsec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{subsec:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T18:17:17.713941+00:00_

paper/sections/related_work.tex:20:We encounter a parallel tension in model collapse, but the failure mode is distinct: ecological stabilization reduces the signal-to-noise ratio while preserving signal direction, whereas real-data mixing reverses the spectral trajectory and eliminates the signal entirely (\S\ref{subsec:controller}).
paper/sections/experiments.tex:7:At each generation we compute the spectral indicators from \S\ref{subsec:spectral_metrics} on the Gram matrix of 1K held-out last-layer embeddings, paired with three downstream metrics: perplexity, HellaSwag accuracy (0-shot), and distinct-4.
paper/sections/experiments.tex:9:For the mixing comparison (\S\ref{subsec:phase1}), we evaluate three strategies sharing the same total real-data budget:
paper/sections/experiments.tex:67:Under pure synthetic training (\S\ref{subsec:phase0}), SLV peaks at Gen~2 (2470) and declines monotonically thereafter.
paper/sections/experiments.tex:71:Since $\Delta_t \leq 0$ for all $t \geq 2$, the controller stays silent for any finite $k$ and any $\tau > 0$ (\S\ref{subsec:controller}); larger gain values do not escape the paradox.
paper/sections/experiments.tex:72:Since pure collapse ($r{=}0$) produces SLV decline from Gen~3 while fixed mix ($r{=}0.5$) yields sustained growth from Gen~2, and $r{=}0.2$ falls below $r_{\text{crit}}$ (\S\ref{subsec:phase_diagram_exp}), we bound $0.2 < r_{\text{crit}} \leq 0.5$.
paper/sections/experiments.tex:75:This reinforces the asymmetry from \S\ref{subsec:phase0}: spectral health under mixed training does not guarantee model health, and the signal attenuation paradox renders per-generation reactive controllers ineffective precisely when collapse prevention succeeds.
paper/sections/experiments.tex:80:To assess whether the spectral patterns in \S\ref{subsec:phase0} reflect a broader embedding-level geometric phenomenon rather than an artifact of a single metric, we compare SLV against six alternative collapse indicators from three signal sourc
…[truncated 3050 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T18:17:17.714131+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "True",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex",
  "old_string": "~\\cite{",
  "new_string": "~\\citep{"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "True",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex",
    "old_string": "~\\cite{",
    "new_string": "~\\citep{"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T18:17:17.714285+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex has been updated. All occurrences were successfully replaced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T18:17:17.714411+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "True",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/related_work.tex",
  "old_string": "~\\cite{",
  "new_string": "~\\citep{"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "True",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/related_work.tex",
    "old_string": "~\\cite{",
    "new_string": "~\\citep{"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T18:17:17.714558+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/related_work.tex has been updated. All occurrences were successfully replaced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T18:17:17.714717+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "True",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "old_string": "~\\cite{",
  "new_string": "~\\citep{"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "True",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "old_string": "~\\cite{",
    "new_string": "~\\citep{"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T18:17:17.714889+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex has been updated. All occurrences were successfully replaced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T18:17:17.715020+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "True",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/conclusion.tex",
  "old_string": "~\\cite{",
  "new_string": "~\\citep{"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "True",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/conclusion.tex",
    "old_string": "~\\cite{",
    "new_string": "~\\citep{"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T18:17:17.715153+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/conclusion.tex has been updated. All occurrences were successfully replaced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-19T18:17:17.715283+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "old_string": "Pythia-410M-deduped \\cite{biderman2023pythia}",
  "new_string": "Pythia-410M-deduped \\citep{biderman2023pythia}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "old_string": "Pythia-410M-deduped \\cite{biderman2023pythia}",
    "new_string": "Pythia-410M-deduped \\citep{biderman2023pythia}"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T18:17:17.715442+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T18:17:17.715561+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "old_string": "(Gen 0--2)",
  "new_string": "(Gen~0--2)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "old_string": "(Gen 0--2)",
    "new_string": "(Gen~0--2)"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T18:17:17.715743+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T18:17:17.715865+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "old_string": "(Gen 2--4)",
  "new_string": "(Gen~2--4)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "old_string": "(Gen 2--4)",
    "new_string": "(Gen~2--4)"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T18:17:17.716022+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T18:17:17.716141+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
  "old_string": "(Gen 4--10)",
  "new_string": "(Gen~4--10)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex",
    "old_string": "(Gen 4--10)",
    "new_string": "(Gen~4--10)"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T18:17:17.716296+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-19T18:17:17.716414+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex",
  "old_string": "early warning signals~\\citep{scheffer2009ews}",
  "new_string": "early warning signals (EWS)~\\citep{scheffer2009ews}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex",
    "old_string": "early warning signals~\\citep{scheffer2009ews}",
    "new_string": "early warning signals (EWS)~\\citep{scheffer2009ews}"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T18:17:17.716553+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T18:17:17.716708+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-19T18:17:17.716825+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-19T18:17:17.716938+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Gen [0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Gen [0-9]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T18:17:17.717051+00:00_

paper/sections/experiments.tex:96:SLV         & emb-Gram  & Gen 2 & \checkmark & 11.8\% & \checkmark \\
paper/sections/experiments.tex:97:RankMe      & emb-SVD   & Gen 2 & \checkmark &  4.7\% & \checkmark \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_notation-consistency_20260519T181220",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-19T18:17:17.717229+00:00_

All `\cite{}` converted — zero bare `\cite{` remaining. The two `Gen 2` in table cells are acceptable (no line-break risk).

## 汇总

### 已修复：22 个问题

| 类别 | 数量 | 文件 |
|------|------|------|
| `\cite{}` → `\citep{}` (parenthetical引用) | 18 | introduction.tex (6), related_work.tex (8), experiments.tex (3), conclusion.tex (1) |
| `Gen 0--2` → `Gen~0--2` (段落标题缺 `~`) | 3 | experiments.tex (lines 44, 52, 55) |
| EWS 缩写首次展开 | 1 | introduction.tex line 16: 添加 "(EWS)" |

### 检查通过（无需修改）

- `$r_{\text{crit}}$` — 全文统一 ✅
- `$\widetilde{S}_t$` — 全文统一，无 `\tilde` 混用 ✅
- `$r_{\text{eff}}$` — 全文统一 ✅
- `$\sigma_1$` — 全文统一 ✅
- `$\Delta_t$` — 全文统一 ✅
- `$r{=}0.x$` thin space — 全文统一 ✅
- Table/Figure 引用 — 3 个 label 全部有对应 ref，无 undefined ✅
- En-dash `--` 数值范围 — 全文统一，无 hyphen 混用 ✅
- `\%` 格式 — 全文统一（无空格） ✅
- SLV 缩写 — abstract + introduction 均展开 ✅
- EMA 缩写 — method 首次使用时展开 ✅
- Subsection labels — 全部 `\ref` 有对应 `\label` ✅

### 待确认：2 个

1. **PPL 缩写**：仅出现在 Table 1/2 列头（`PPL`、`PPL growth`），正文均用全称 "perplexity"。作为 NLP 标准缩写可接受，但如需严谨可在 Table 1 caption 中注明。
2. **未被引用的 subsection labels**：`subsec:cross_scale` 和 `subsec:second_order` 定义了但未被 `\ref` 引用。如果需要正文交叉引用可补上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_notation-consistency_20260519T181220"
}
```

</details>

---
