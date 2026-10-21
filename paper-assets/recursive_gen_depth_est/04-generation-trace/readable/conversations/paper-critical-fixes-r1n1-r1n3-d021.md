# paper critical fixes r1n1 r1n3 d021

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738.jsonl`
- **Structured JSON:** [`5a690959c7475a9385ba.json`](../../sessions/5a/5a690959c7475a9385ba.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-15T13:43:19.629763+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T13:43:19.630111+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T13:43:19.630290+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T13:43:19.630538+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper_framing.md\", \"content\": \"# Paper Framing — recursive_gen_depth_est\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\\n- EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\\n\\n## Core Claims (2 条 + Discussion implication)\\n\\n1. **Ordinal depth estimation is feasible and accurate**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark, Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all 9 settings.\\n\\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v
…[truncated 11471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T13:43:19.630700+00:00_

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
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T13:43:19.630906+00:00_

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
…[truncated 8341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T13:43:19.631071+00:00_

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
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T13:43:19.631245+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	The atlas (\S\ref{sec:atlas}) established in-distribution accuracy of 69.6--85.4\%.
5	We now test whether these results reflect genuine statistical regularities or artifacts of specific training conditions, evaluating four axes: classifier choice (\S\ref{sec:gen:baselines}), cross-model transfer (\S\ref{sec:gen:crossmodel}), cross-strategy transfer (\S\ref{sec:gen:crossstrategy}), and end-to-end learned representations (\S\ref{sec:gen:dcol}).
6	
7	\subsection{Baseline Comparison}
8	\label{sec:gen:baselines}
9	
10	Table~\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.
11	Three feature-based methods---Random Forest (RF), CORAL ordinal regression \cite{coral2020}, and DivEye \cite{diveye2026}---all operate on the same 19 statistical features and achieve statistically indistinguishable accuracy (78.1--78.2\%; pairwise bootstrap $p>0.05$ after Bonferroni correction, 95\% CI within $\pm$1.1pp).
12	These three significantly outperform CE-MLP ($p<0.001$, $+$3.8pp), which in turn trails logistic regression by $\sim$0.1pp.
13	Single-feature regression on mean perplexity performs at chance (25.1\%), confirming that depth estimation requires the multi-dimensional feature representation defined in \S\ref{sec:method}.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Comparison of classification methods on Pythia-1.4B nucleus. RF, CORAL, and DivEye use the same 19 statistical features and are statistically indistinguishable (bootstrap $p>0.05$, Bonferroni-corrected). Chance = 25\%. 5-fold CV std: 0.2--0.9pp across all methods.}
19	\label{tab:baselines}
20	\begin{tabular}{lc}
21	\toprule
22	Method & 4-class Acc (\%) \\
23	\midrule
24	RF (19 features) & 78.2 \\
25	CORAL & 78.1 \\
26	DivEye & 78.2 \\
27	CE-MLP & 74.9 \\
28	LR & 75.0 \\
29	DeepSeek V3.2 (zero-shot)\footnotemark & 40.0 \\
30	ppl-regression (single feature) & 25.1 \\
31	\bottomrule
32	\end{tabula
…[truncated 5924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T13:43:19.631394+00:00_

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
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T13:43:19.631522+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Depth-graduated data curation.}
5	Binary synthetic-data filters discard all machine-generated text indiscriminately, yet first-generation outputs may be beneficial for training \cite{drayson2025_detection_prevents_collapse}.
6	Predicted depth can serve as a continuous quality proxy for importance weighting in curation pipelines \cite{dsir2023,qurating2024}, retaining shallow-generation text while down-weighting deeply recursive samples.
7	
8	\paragraph{Feature evolution tracks tail erosion.}
9	Feature importance shifts with depth: \textsc{var\_surprisal} dominates at shallow recursions while \textsc{p90\_ppl} and kurtosis assume greater importance at deeper depths, aligning with the tail erosion theory of \citet{shumailov2024_nature}.
10	
11	\paragraph{Cross-strategy deployment.}
12	The temperature-induced d1/d2 AUC inversion (\S\ref{sec:gen:crossstrategy}) means that deploying a depth estimator without knowing the target decoding strategy risks systematic prediction reversals; strategy-conditioned classifiers are needed but strategy identification from text remains open.
13	
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T13:43:19.631669+00:00_

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
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T13:43:19.631832+00:00_

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
24	Each model is paired with three sampling methods: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	
27	\paragraph{Depth and scale.}
28	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
29	For depth exten
…[truncated 5774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T13:43:19.632038+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "z.score|z-score|normalization.*recover|normalization.*restor",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "-i": "True",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Grep",
  "tool_args": {
    "pattern": "z.score|z-score|normalization.*recover|normalization.*restor",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "output_mode": "content",
    "-i": "True",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T13:43:19.632240+00:00_

docs/paper/generalization.tex:105:\paragraph{Z-score normalization does not resolve the inversion.}
docs/paper/generalization.tex:106:A natural hypothesis is that per-feature z-score normalization might correct this covariate shift \cite{sugiyama2007_importance_weighting}.
docs/paper/generalization.tex:108:Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).
docs/paper/abstract.tex:7:Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%, though temperature sampling induces a d1/d2 AUC inversion that z-score normalization cannot resolve.
docs/paper/introduction.tex:31:[Omitted long matching line]
docs/paper/main.aux:735:\@writefile{toc}{\contentsline {paragraph}{Z-score normalization does not resolve the inversion.}{8}{section*.26}\protected@file@percent }

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T13:43:19.632477+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
  "offset": "25",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
    "offset": "25",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:43:19.632698+00:00_

25	
26	\begin{itemize}
27	    \item \textbf{Task formalization.} We define recursive generation depth estimation as ordinal classification, distinguishing it from binary detection and single-pass editing estimation. We introduce the EDD metric, which summarizes the maximum depth at which adjacent generations remain separable above a given AUC threshold.
28	
29	    \item \textbf{Depth Degradation Atlas.} We construct a systematic $3 \times 3$ map across model families and decoding strategies, revealing that \textsc{p90\_ppl} ranks in the top 2 in all 9 cells (100\%) and \textsc{var\_surprisal} in 7/9 (78\%), with a mean Spearman rank correlation of $\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.
30	
31	    \item \textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\% mean accuracy and cross-strategy transfer 59.1\% (chance = 25\%), demonstrating partial universality of depth fingerprints. We identify a temperature-induced d1/d2 AUC inversion (GPT-2~XL: 0.13, OLMo: 0.25) caused by accelerated convergence. Z-score normalization recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89) but fails to resolve the temperature-specific inversion, revealing a two-layer covariate shift structure.
32	
33	    \item \textbf{End-to-end learning as negative result.} Both DeBERTa-v3-base (58.3\%) and RoBERTa-base (59.5\%) achieve ${\sim}$59\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\%)---with the architecture-invariant gap ruling out model selection bias. Probing reveals a significant negative correlation ($\rho{=}{-}0.48$) between transformer attention and RF feature importance, confirming complementary representations.
34	\end{itemize}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T13:43:19.632960+00:00_

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
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T13:43:19.633179+00:00_

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
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T13:43:19.633579+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "old_string": "\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe formalize this via the \\emph{Effective Discriminable Depth} (EDD; defined in \\S\\ref{sec:method}): $\\mathrm{EDD}_T$ is the maximum depth $d^*$ such that the pairwise AUC between $d^*$ and $d^*{+}1$ exceeds a threshold $T$, using a dedicated binary RF per adjacent pair.",
  "new_string": "\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFor each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$---the ROC AUC of this pairwise classifier at separating depth-$d$ from depth-$(d{+}1)$ samples.\nGiven a discrimination threshold $T$, EDD is defined as:\n\\[\n\\mathrm{EDD}_T = \\max \\bigl\\{ d^*{+}1 : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T \\bigr\\}\n\\]\nwhere $d^* \\in \\{0, 1, \\dots, K{-}1\\}$.\nIntuitively, $\\mathrm{EDD}_T$ is the deepest generation depth at which the classifier can still reliably separate it from the preceding depth; beyond this boundary, adjacent depths become statistically indistinguishable.\nWe set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
    "old_string": "\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe formalize this via the \\emph{Effective Discriminable Depth} (EDD; defined in \\S\\ref{sec:method}): $\\mathrm{EDD}_T$ is the maximum depth $d^*$ such that the pairwise AUC between $d^*$ and $d^*{+}1$ exceeds a threshold $T$, using a dedicated binary RF per adjacent pair.",
    "new_string": "\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.\nWe quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFor each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$---the ROC AUC of this pairwise classifier at separating depth-$d$ from depth-$(d{+}1)$ samples.\nGiven a discrimination threshold $T$, EDD is defined as:\n\\[\n\\mathrm{EDD}_T = \\max \\bigl\\{ d^*{+}1 : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T \\bigr\\}\n\\]\nwhere $d^* \\in \\{0, 1, \\dots, K{-}1\\}$.\nIntuitively, $\\mathrm{EDD}_T$ is the deepest generation depth at which the classifier can still reliably separate it from the preceding depth; beyond this boundary, adjacent depths become statistically indistinguishable.\nWe set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T13:43:19.633800+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T13:43:19.633996+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
  "old_string": "\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nWe train DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nBoth achieve ${\\sim}$59\\% (DeBERTa 58.3$\\pm$4.7\\%, RoBERTa 59.5$\\pm$3.2\\%), 19pp below feature-based classifiers (78.2\\%).\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nThe 1.2pp inter-backbone gap rules out model selection bias.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\nProbing reveals a negative correlation between DeBERTa attention importance and RF permutation importance ($\\rho{=}{-}0.48$, $p{=}0.036$; top-5 Jaccard$\\,{=}\\,0$): transformers attend to lexical patterns (TTR, repeated bigrams) while RF relies on perplexity tail statistics, confirming complementary---not redundant---representations.",
  "new_string": "\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nTo test whether pretrained language models can learn depth signals directly from raw text, we finetune DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nTable~\\ref{tab:e2e_baselines} summarizes the comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{End-to-end baseline comparison on Pythia-1.4B nucleus. RF uses 19 hand-crafted statistical features; PLM baselines are finetuned on raw text. 5-fold CV (std where shown). Chance = 25\\%.}\n\\label{tab:e2e_baselines}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & 4-class Acc (\\%) & $\\Delta$ vs RF \\\\\n\\midrule\nRF (19 features) & 78.2 & --- \\\\\nRoBERTa-base finetune & 59.5 $\\pm$ 3.2 & $-$18.7pp \\\\\nDeBERTa-v3-base finetune & 58.3 $\\pm$ 4.7 & $-$19.9pp \\\\\nDeepSeek V3.2 (zero-shot) & 40.0 & $-$38.2pp \\\\\nChance & 25.0 & $-$53.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth PLM architectures---masked language modeling (RoBERTa) and disentangled attention (DeBERTa)---converge to ${\\sim}$59\\%, with the 1.2pp inter-backbone gap ruling out architecture selection bias.\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\n\n\\paragraph{Feature overlap analysis.}\nProbing reveals a significant negative correlation between DeBERTa attention importance and RF permutation importance (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.\nThis confirms that hand-crafted statistical features capture depth signals that PLMs cannot learn from raw text alone, particularly the distributional tail properties that constitute the dominant depth markers (\\S\\ref{sec:atlas:features})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
    "old_string": "\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nWe train DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nBoth achieve ${\\sim}$59\\% (DeBERTa 58.3$\\pm$4.7\\%, RoBERTa 59.5$\\pm$3.2\\%), 19pp below feature-based classifiers (78.2\\%).\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nThe 1.2pp inter-backbone gap rules out model selection bias.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\nProbing reveals a negative correlation between DeBERTa attention importance and RF permutation importance ($\\rho{=}{-}0.48$, $p{=}0.036$; top-5 Jaccard$\\,{=}\\,0$): transformers attend to lexical patterns (TTR, repeated bigrams) while RF relies on perplexity tail statistics, confirming complementary---not redundant---representations.",
    "new_string": "\\subsection{End-to-End Learning}\n\\label{sec:gen:dcol}\n\nTo test whether pretrained language models can learn depth signals directly from raw text, we finetune DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\\,{=}\\,2{\\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.\nTable~\\ref{tab:e2e_baselines} summarizes the comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{End-to-end baseline comparison on Pythia-1.4B nucleus. RF uses 19 hand-crafted statistical features; PLM baselines are finetuned on raw text. 5-fold CV (std where shown). Chance = 25\\%.}\n\\label{tab:e2e_baselines}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & 4-class Acc (\\%) & $\\Delta$ vs RF \\\\\n\\midrule\nRF (19 features) & 78.2 & --- \\\\\nRoBERTa-base finetune & 59.5 $\\pm$ 3.2 & $-$18.7pp \\\\\nDeBERTa-v3-base finetune & 58.3 $\\pm$ 4.7 & $-$19.9pp \\\\\nDeepSeek V3.2 (zero-shot) & 40.0 & $-$38.2pp \\\\\nChance & 25.0 & $-$53.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth PLM architectures---masked language modeling (RoBERTa) and disentangled attention (DeBERTa)---converge to ${\\sim}$59\\%, with the 1.2pp inter-backbone gap ruling out architecture selection bias.\nBoth easily separate d0 (F1$>$0.95) but fail at adjacent-depth discrimination (d1/d2 F1$<$0.42), precisely where \\textsc{p90\\_ppl} and \\textsc{var\\_surprisal} excel.\nDCOL \\cite{cloc2025} with RoBERTa-large fared worse (best 64.5\\%, 5/6 runs unstable).\n\n\\paragraph{Feature overlap analysis.}\nProbing reveals a significant negative correlation between DeBERTa attention importance and RF permutation importance (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.\nThis confirms that hand-crafted statistical features capture depth signals that PLMs cannot learn from raw text alone, particularly the distributional tail properties that constitute the dominant depth markers (\\S\\ref{sec:atlas:features})."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T13:43:19.634210+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T13:43:19.634345+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
  "old_string": "Z-score normalization recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89) but fails to resolve the temperature-specific inversion, revealing a two-layer covariate shift structure.",
  "new_string": "Z-score normalization improves overall LR cross-strategy accuracy (25\\%$\\to$61\\%) but does not recover the temperature-induced d1/d2 inversion (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19), confirming a genuine geometry-level shift rather than a correctable scale difference."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
    "old_string": "Z-score normalization recovers logistic regression performance for non-temperature holdouts (d1v2 AUC 0.61--0.89) but fails to resolve the temperature-specific inversion, revealing a two-layer covariate shift structure.",
    "new_string": "Z-score normalization improves overall LR cross-strategy accuracy (25\\%$\\to$61\\%) but does not recover the temperature-induced d1/d2 inversion (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19), confirming a genuine geometry-level shift rather than a correctable scale difference."
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T13:43:19.634495+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T13:43:19.634616+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
  "old_string": "Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).\nThis two-layer structure---scale shift addressable by normalization, plus a deeper geometric shift specific to temperature sampling---suggests that temperature decoding induces qualitatively different feature distributions that cannot be reconciled by linear rescaling.",
  "new_string": "Z-score standardization improves overall logistic regression cross-strategy accuracy from 25\\% to 61\\%, with d1v2 AUC gains for nucleus and top-$k$ holdouts (0.61--0.89).\nHowever, it does not recover the temperature-induced d1v2 inversion---AUC worsens for two of three models (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19; Pythia 0.52), confirming that temperature decoding induces a genuine geometry-level shift in feature space rather than a correctable scale difference."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
    "old_string": "Z-score standardization substantially improves logistic regression cross-strategy transfer for nucleus and top-$k$ holdouts (d1v2 AUC 0.61--0.89), but fails to resolve the temperature-induced inversion (d1v2 AUC remains near or below chance: Pythia 0.52, GPT-2~XL 0.24, OLMo 0.19).\nThis two-layer structure---scale shift addressable by normalization, plus a deeper geometric shift specific to temperature sampling---suggests that temperature decoding induces qualitatively different feature distributions that cannot be reconciled by linear rescaling.",
    "new_string": "Z-score standardization improves overall logistic regression cross-strategy accuracy from 25\\% to 61\\%, with d1v2 AUC gains for nucleus and top-$k$ holdouts (0.61--0.89).\nHowever, it does not recover the temperature-induced d1v2 inversion---AUC worsens for two of three models (GPT-2~XL 0.50$\\to$0.24, OLMo 0.50$\\to$0.19; Pythia 0.52), confirming that temperature decoding induces a genuine geometry-level shift in feature space rather than a correctable scale difference."
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T13:43:19.634775+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T13:43:19.634952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "offset": "57",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
    "offset": "57",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T13:43:19.635123+00:00_

57	\label{sec:atlas:edd}
58	
59	Aggregate accuracy masks the fact that adjacent depths become harder to distinguish as depth increases.
60	We quantify this via the \emph{Effective Discriminable Depth} (EDD).
61	For each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\mathrm{AUC}(d, d{+}1)$---the ROC AUC of this pairwise classifier at separating depth-$d$ from depth-$(d{+}1)$ samples.
62	Given a discrimination threshold $T$, EDD is defined as:
63	\[
64	\mathrm{EDD}_T = \max \bigl\{ d^*{+}1 : \mathrm{AUC}(d^*, d^*{+}1) \geq T \bigr\}
65	\]
66	where $d^* \in \{0, 1, \dots, K{-}1\}$.
67	Intuitively, $\mathrm{EDD}_T$ is the deepest generation depth at which the classifier can still reliably separate it from the preceding depth; beyond this boundary, adjacent depths become statistically indistinguishable.
68	We set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \in \{0.65, 0.70, 0.75, 0.80\}$ below.
69	
70	Within the 4-class atlas (d0--d3), 7 of 9 cells achieve $\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \S\ref{sec:atlas:indist}.
71	
72	To probe deeper, we extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair (we increase from 200 to 500 trees for binary classifiers to ensure convergence on the smaller per-pair sample sizes).
73	Figure~\ref{fig:auc_decay} shows the pairwise AUC decay curve.
74	The d0\,vs.\,d1 boundary is near-perfect (AUC\,=\,0.998), reflecting the well-known human--machine gap.
75	Subsequent boundaries degrade monotonically: d1\,vs.\,d2 achieves 0.925 [95\% CI: 0.914,\,0.935], d2\,vs.\,d3 reaches 0.823 [0.805,\,0.840], and d3\,vs.\,d4 yields 0.784 [0.765,\,0.802]---with the confidence interval lower bound still 
…[truncated 140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T13:43:19.635295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
  "offset": "105",
  "limit": "45"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
    "offset": "105",
    "limit": "45"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T13:43:19.635525+00:00_

105	\paragraph{Z-score normalization does not resolve the inversion.}
106	A natural hypothesis is that per-feature z-score normalization might correct this covariate shift \cite{sugiyama2007_importance_weighting}.
107	For RF, z-normalization leaves accuracy essentially unchanged (59.1\% $\to$ 59.2\%) and does not improve d1v2 AUC ($\Delta < 0.02$), as expected since tree splits depend on feature rank order, not scale.
108	Z-score standardization improves overall logistic regression cross-strategy accuracy from 25\% to 61\%, with d1v2 AUC gains for nucleus and top-$k$ holdouts (0.61--0.89).
109	However, it does not recover the temperature-induced d1v2 inversion---AUC worsens for two of three models (GPT-2~XL 0.50$\to$0.24, OLMo 0.50$\to$0.19; Pythia 0.52), confirming that temperature decoding induces a genuine geometry-level shift in feature space rather than a correctable scale difference.
110	
111	\subsection{End-to-End Learning}
112	\label{sec:gen:dcol}
113	
114	To test whether pretrained language models can learn depth signals directly from raw text, we finetune DeBERTa-v3-base and RoBERTa-base end-to-end (lr$\,{=}\,2{\times}10^{-5}$, 3 epochs, 5-fold CV) on Pythia-1.4B nucleus data.
115	Table~\ref{tab:e2e_baselines} summarizes the comparison.
116	
117	\begin{table}[t]
118	\centering
119	\small
120	\caption{End-to-end baseline comparison on Pythia-1.4B nucleus. RF uses 19 hand-crafted statistical features; PLM baselines are finetuned on raw text. 5-fold CV (std where shown). Chance = 25\%.}
121	\label{tab:e2e_baselines}
122	\begin{tabular}{lcc}
123	\toprule
124	Method & 4-class Acc (\%) & $\Delta$ vs RF \\
125	\midrule
126	RF (19 features) & 78.2 & --- \\
127	RoBERTa-base finetune & 59.5 $\pm$ 3.2 & $-$18.7pp \\
128	DeBERTa-v3-base finetune & 58.3 $\pm$ 4.7 & $-$19.9pp \\
129	DeepSeek V3.2 (zero-shot) & 40.0 & $-$38.2pp \\
130	Chance & 25.0 & $-$53.2pp \\
131	\bottomrule
132	\end{tabular}
133	\end{table}
134	
135	Both PLM architectures---masked language modeling 
…[truncated 1139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T13:43:19.635770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
  "offset": "29",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
    "offset": "29",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T13:43:19.636011+00:00_

29	    \item \textbf{Depth Degradation Atlas.} We construct a systematic $3 \times 3$ map across model families and decoding strategies, revealing that \textsc{p90\_ppl} ranks in the top 2 in all 9 cells (100\%) and \textsc{var\_surprisal} in 7/9 (78\%), with a mean Spearman rank correlation of $\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.
30	
31	    \item \textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\% mean accuracy and cross-strategy transfer 59.1\% (chance = 25\%), demonstrating partial universality of depth fingerprints. We identify a temperature-induced d1/d2 AUC inversion (GPT-2~XL: 0.13, OLMo: 0.25) caused by accelerated convergence. Z-score normalization improves overall LR cross-strategy accuracy (25\%$\to$61\%) but does not recover the temperature-induced d1/d2 inversion (GPT-2~XL 0.50$\to$0.24, OLMo 0.50$\to$0.19), confirming a genuine geometry-level shift rather than a correctable scale difference.
32	
33	    \item \textbf{End-to-end learning as negative result.} Both DeBERTa-v3-base (58.3\%) and RoBERTa-base (59.5\%) achieve ${\sim}$59\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\%)---with the architecture-invariant gap ruling out model selection bias. Probing reveals a significant negative correlation ($\rho{=}{-}0.48$) between transformer attention and RF feature importance, confirming complementary representations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-15T13:43:19.636249+00:00_

所有改动已验证正确。

### 修改汇总

**atlas.tex** — Issue 1 (R1-N1 EDD 正式定义)
- `sec:atlas:edd` 子节：原来一句话引用 method section，改为完整的 EDD 定义段落
- 添加了正式数学公式 `EDD_T = max{d*+1 : AUC(d*, d*+1) ≥ T}`
- 说明了 AUC(d, d+1) 是 binary pairwise classifier 的 ROC AUC
- 说明了 T=0.75 默认阈值及其选择理由
- 添加了直觉含义：超过此深度后相邻深度变得统计不可区分

**generalization.tex** — Issue 2 (R1-N3 end-to-end baseline 对比表)
- `sec:gen:dcol` 子节：添加了 `tab:e2e_baselines` 表格（RF 78.2% / RoBERTa 59.5±3.2% / DeBERTa 58.3±4.7% / DeepSeek 40.0% / Chance 25.0%，含 Δ vs RF 列）
- 说明 MLM vs disentangled attention 两种架构一致结论（1.2pp gap），排除 architecture bias
- 新增 "Feature overlap analysis" 段落：Spearman ρ=-0.484 (p=0.036)，PLM 擅长 TTR (R²=0.85) 但 var_surprisal/p90_ppl R² 为负，结论：hand-crafted features 捕获 PLM 无法学到的深度信号

**generalization.tex** — Issue 3 (D021 z-score claim 修正)
- z-score 段落：删除 "substantially improves...for nucleus and top-k holdouts" 的 recovery 措辞
- 改为：overall LR accuracy 25%→61%，但 temp d1v2 AUC 恶化（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19）
- 结论改为 "genuine geometry-level shift in feature space rather than a correctable scale difference"

**introduction.tex** — Issue 3 (D021 z-score claim 修正)
- 贡献列表第 3 条：删除 "recovers logistic regression performance for non-temperature holdouts"
- 改为：overall LR accuracy 25%→61% + 不恢复 temperature d1v2 inversion + 确认 geometry-level shift

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738"
}
```

</details>

---
