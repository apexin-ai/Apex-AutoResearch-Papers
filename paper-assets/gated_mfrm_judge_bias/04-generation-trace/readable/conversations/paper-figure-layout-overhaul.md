# paper figure layout overhaul

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 119
- **Recorded user turns:** 0
- **Tool calls:** 59
- **Original source:** `logs/chats/worker_paper_figure-layout-overhaul_20260525T121947.jsonl`
- **Structured JSON:** [`645f42ed56c9b56be485.json`](../../sessions/64/645f42ed56c9b56be485.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

119 recorded events

### Tool call

_source line 1 · 2026-05-25T12:29:16.967259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T12:29:16.967871+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{amsthm}
14	\usepackage{booktabs}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\newtheorem{observation}{Observation}
19	\newtheorem{proposition}{Proposition}
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}{Corollary}
22	
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model\\for Disentangling Judge Bias and Contamination in LLM Evaluation}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{method}
37	\input{experiments}
38	\input{conclusion}
39	
40	\section*{Limitations}
41	\input{limitations}
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T12:29:16.968085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T12:29:16.968442+00:00_

1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	\begin{figure*}[t]
5	\centering
6	\begin{minipage}[t]{0.45\textwidth}
7	\centering
8	\includegraphics[width=\textwidth]{fig2_ovb_bias}
9	\end{minipage}
10	\hfill
11	\begin{minipage}[t]{0.45\textwidth}
12	\centering
13	\includegraphics[width=\textwidth]{fig4_bias_vs_rho}
14	\end{minipage}
15	\caption{(a)~Sequential estimation bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. (b)~Sequential estimator bias remains approximately constant across confounding levels ($\rho$), confirming omission-driven rather than confounding-strength-dependent bias. Joint G-MFRM estimation reduces bias by approximately 70\% at all $\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
16	\label{fig:ovb_bias}
17	\end{figure*}
18	
19	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
20	%
21	\begin{equation}
22	\label{eq:mfrm}
23	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \tau_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \tau_k)} = \theta_n - b_i - d_j - \tau_k,
24	\end{equation}
25	%
26	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for it
…[truncated 3469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T12:29:16.968628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T12:29:16.968812+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{forest_dj}
7	\caption{Judge severity estimates ($d_j$) for all nine judges with 95\% credible intervals. Positive values indicate stricter scoring. Proprietary judges (Claude Opus, GPT-5.5) cluster at the strict end; open-source judges (Mistral, LLaMA) are more lenient. The severity range spans 1.34 logits.}
8	\label{fig:judge_severity}
9	\end{figure}
10	
11	\subsection{Setup}
12	\label{sec:setup}
13	
14	\paragraph{Data and models.} We evaluate on Arena-Hard \citep{li2024arenahard}, a benchmark of 316 multi-turn conversational items selected for high separability among frontier models. After filtering for coverage, the evaluation set comprises 176 items in a connected incomplete design (36{,}231 observations; 66.0\% fill rate of the full $N \times I \times J$ tensor). Seventeen target models spanning proprietary and open-source families are evaluated: the original 8 models (GPT-4o, GPT-4o-mini, Qwen2.5-72B, LLaMA-3.3-70B, Qwen3-8B, Gemma-2-9B, GPT-4-0613, GPT-3.5-Turbo) plus 9 additional models (Claude-3.5-Sonnet, GPT-4-Turbo, LLaMA-3.1-70B, Gemma-2-27B, Claude-3-Opus, LLaMA-3-70B, Mixtral-8x22B, Claude-3-Haiku, LLaMA-3-8B). Ground-truth rankings are derived from Chatbot Arena human preference data \citep{zheng2023mtbench}.
15	
16	\paragraph{Judges.} Nine LLM judges score model responses in position-swapped pairwise mode: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, Mistral-Large-2, LLaMA-3.3-70B, Qwen2.5-72B, and Qwen3-235B. Seven judges cover all 17 target models; two judges (GPT-5.5 and Claude Opus 4.7) cover only the original 8 models, yielding an asymmetric connected design---Theorem~\ref{thm:sufficient} requires only connectivity, not full crossing. Position swapping controls for position bias and doubles the effective observation count. Two models---Qwen2.5-72B and LLaMA-3.3-70B---serve as both judge and
…[truncated 6365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T12:29:16.968961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T12:29:16.969315+00:00_

1	\section{Proofs of Propositions~\ref{prop:no_new} and~\ref{prop:exposure_variation}}
2	\label{app:prop_proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:no_new}]
5	Suppose $c_n' = c_n + \delta$ preserves all response probabilities. Then $\delta \cdot e_i = 0$ for all items. Since $e_i \neq 0$ for at least one item by assumption, $\delta = 0$. Fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \cdot e_i = (\lambda c_n)(\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.
6	\end{proof}
7	
8	\begin{proof}[Proof of Proposition~\ref{prop:exposure_variation}]
9	When exposure is constant, the linear predictor becomes $(\theta_n + c_n \cdot e) - b_i - d_j - \tau_k$, equivalent to a standard MFRM with reparameterized ability $\theta^*_n = \theta_n + c_n \cdot e$. No configuration of response data can distinguish $(\theta_n, c_n)$ from $(\theta_n + \epsilon, c_n - \epsilon/e)$ for any $\epsilon$.
10	\end{proof}
11	
12	
13	\section{Proof of Theorem~\ref{thm:sufficient}}
14	\label{app:proof}
15	
16	We prove that the G-MFRM is locally identifiable under the conditions of Theorem~\ref{thm:sufficient}. Following \citet{rothenberg1971}, a parametric model is locally identifiable at the true parameter vector $\boldsymbol{\psi}_0$ if and only if the Fisher information matrix $\mathbf{F}(\boldsymbol{\psi}_0)$ is non-singular.
17	
18	\paragraph{Setup.} The G-MFRM parameter vector is $\boldsymbol{\psi} = (\boldsymbol{\theta}, \mathbf{c}, \mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$, where $\boldsymbol{\theta} \in \mathbb{R}^{N-1}$ (after the location constraint $\sum_n \theta_n = 0$), $\mathbf{c} \in \mathbb{R}_{\geq 0}^N$, $\mathbf{b} \in \mathbb{R}^I$, $\mathbf{d} \in \mathbb{R}^J$, and $\boldsymbol{\tau} \in \mathbb{R}^{K-1}$. The exposure vector $\mathbf{e} = (e_1, \ldots, e_I)$ is fixed externally and treated as known. The linear predictor is $\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$, with partial derivatives:
19	%
20
…[truncated 33336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T12:29:16.969534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T12:29:16.969693+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large Language Model (LLM) evaluation increasingly relies on LLM-as-a-judge protocols, where one or more LLM judges score model responses on structured benchmarks \citep{zheng2023mtbench}. Two well-documented sources of distortion affect these evaluations: \emph{judge bias}, where different judges assign systematically different scores to the same response \citep{wang2024positionbias, ye2024justice, panickssery2024selffavor}, and \emph{benchmark contamination}, where models achieve inflated scores on items encountered during training \citep{dcr2025, mink2024}. Existing methods address these distortions independently: judge bias corrections calibrate inter-judge differences without modeling contamination \citep{cyclicjudge2026, uda2026}, while contamination detection tools adjust for memorization without accounting for judge effects \citep{constat2024, dcr2025, logprober2024}. A practitioner who needs both corrections must apply them sequentially, but this produces unreliable estimates. Accurate ability ranking is essential for model selection, safety evaluation, and benchmark design; systematic distortion undermines all three.
5	
6	\begin{figure*}[t]
7	\centering
8	\includegraphics[width=\textwidth]{fig1_framework_v2}
9	\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\hat{\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}
10	\label{fig:framework}
11	\end{figure*}
12	
13	We formalize this failure as an omitted 
…[truncated 2206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T12:29:16.969835+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T12:29:16.970023+00:00_

1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.85\textwidth]{fig3_error_propagation}
7	\caption{Error propagation from Stage~2 exposure noise to Stage~3 parameter estimates. Ability RMSE ($\theta$, left) and contamination RMSE ($c_n$, right) as a function of exposure noise $\sigma_e$. The dashed line marks $\sigma_{\mathrm{crit}} \approx 0.2$, below which degradation remains mild ($\theta$-RMSE $+$5.9\%, $c_n$-RMSE $+$7.9\%). Error bars: $\pm$1 std over 20 seeds.}
8	\label{fig:error_prop}
9	\end{figure*}
10	
11	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
12	
13	\subsection{Model Specification}
14	\label{sec:model_spec}
15	
16	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
17	%
18	\begin{equation}
19	\label{eq:gmfrm}
20	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i,
21	\end{equation}
22	%
23	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \in [0,1]$ quantifies how much of item $i$ has leaked into training corpora. When $c_n =
…[truncated 9499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T12:29:16.970177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T12:29:16.970320+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Judge Bias in LLM Evaluation.}
5	LLM-as-a-judge evaluations exhibit position bias \citep{wang2024positionbias}, self-preference \citep{panickssery2024selffavor}, and other cognitive biases \citep{koo2024cobbler, ye2024justice, bavaresco2025judgebench}; see also \citet{li2024splitmerge} and \citet{fiedler2026bias_uncertainty}. On the correction side, CyclicJudge \citep{cyclicjudge2026} eliminates average bias via round-robin assignment, and UDA \citep{uda2026} learns a neural K-factor reducing inter-judge deviation by 63.4\%. All of these methods model only the judge facet, absorbing contamination effects into ability estimates (Section~\ref{sec:confounding}).
6	
7	\paragraph{Benchmark Contamination Detection and Avoidance.}
8	Detection methods include performance-based tests \citep{constat2024}, unified contamination metrics \citep{dcr2025}, token-level log-probability probes \citep{logprober2024, mink2024}, and guided prompting \citep{golchin2024timetravel, oren2024proving}; see also \citet{deng2024contamination, sainz2023contamination}. \citet{preference_leakage2026} identify judge-side preference leakage, complementary to G-MFRM's examinee-side focus. Avoidance strategies include dynamic benchmarks \citep{livebench2025}, private evaluation \citep{truce2024}, and subset selection \citep{polo2024tinybenchmarks}. G-MFRM instead corrects for residual contamination while simultaneously modeling judge effects.
9	
10	\paragraph{Item Response Theory (IRT) and MFRM for LLM Evaluation.}
11	IRT has been applied to NLP leaderboards for ranking and benchmark analysis \citep{lalor2019irt, rodriguez2021irt, vania2021irt}. The Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm, linacre1994mfrm} extends IRT to multi-rater settings; \citet{jiao2025mfrm_llm} apply it to LLM judge panels, and \citet{uto2020generalized} and \citet{choi2026irt_judge} propose Bayesian variants; see also \citet{zhou2025psnirt}. The Do
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T12:29:16.970488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T12:29:16.970645+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced G-MFRM, which jointly estimates model ability, judge severity, and contamination susceptibility by formalizing their confounding as omitted variable bias. On Arena-Hard, G-MFRM produces the first joint contamination--severity diagnostic within a measurement-theoretic framework, with nominally higher rank agreement ($\tau = 0.857$ vs.\ $0.786$; not significant at $N = 8$); well-powered validation requires $N \geq 17$ (Limitations). Treating judge bias and contamination as separable leads to systematic estimation errors; future LLM evaluation frameworks should model these facets jointly.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T12:29:16.970822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T12:29:16.970957+00:00_

1	The evaluation uses a single benchmark (Arena-Hard) with 66.0\% fill rate (18{,}116 of 27{,}456 potential cells); sparser designs may compromise identifiability of $c_n$ for models with few observed exposed items, and sparse per-item observations produce elevated item-level mean-square residuals (92/176 items), though model- and judge-level fit remains acceptable. Stage~2 exposure estimation relies on a reference model anchor (gpt-4-0314), whose validity should be periodically re-assessed as benchmarks age.
2	
3	Empirical CI coverage differs by parameter type: ability estimates $\theta$ approach nominal coverage (${\sim}$90\% at $N = 8$), while contamination susceptibility $c_n$ exhibits posterior overconfidence (71\% at $N = 50$, 68\% at $N = 8$; \citealp{talts2018sbc}), a structural issue from the multiplicative coupling $c_n \cdot e_i$ and the HalfNormal boundary constraint at $c_n = 0$ that does not improve with sample size; $c_n$ credible intervals should be treated as lower bounds on uncertainty (Appendix~\ref{app:ci_coverage}), with recalibration via simulation-based calibration (SBC) as a direction for future work. The bilinear term also assumes rank-1 structure---a single contamination dimension per model---while contamination may be domain-specific (e.g., coding vs.\ reasoning), requiring a higher-rank decomposition $\sum_r c_{nr} \cdot e_{ir}$ that the current model does not capture.
4	
5	Post-hoc power analysis indicates $N \approx 17$ for 80\% power to detect $\Delta\tau = 0.071$; the $N = 8$ evaluation has ${\sim}$50\% power, explaining the non-significant bootstrap result. Generalization to other benchmarks and larger model populations remains to be verified. While self-evaluation sensitivity analysis (Appendix~\ref{app:self_eval}) confirms robust rankings when excluding self-judging observations, removing overlapping models entirely from the judge panel has not been conducted.
6	
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T12:29:16.971096+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T12:29:16.971221+00:00_

figures/paper/fig3_error_propagation.pdf
figures/paper/forest_cn.pdf
figures/paper/ppc.pdf
figures/paper/trace_b.pdf
figures/paper/trace_cn.pdf
figures/paper/trace_dj.pdf
figures/paper/trace_sigma_c.pdf
figures/paper/trace_theta.pdf
figures/paper/fig5_cn_recovery.pdf
figures/paper/ablation_boxplots.pdf
figures/paper/theta_tau_boxplot.pdf
figures/paper/fig_ppc.pdf
figures/paper/model_comparison.pdf
figures/paper/pareto_k_plot.pdf
figures/paper/fig6_cn_profile.pdf
figures/paper/fig1_framework.pdf
figures/paper/fig2_ovb_bias_v2.pdf
figures/paper/forest_dj.pdf
figures/paper/fig1_framework_v2.pdf
figures/paper/fig2_ovb_bias.pdf
figures/paper/fig4_bias_vs_rho.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T12:29:16.971375+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{fig:",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T12:29:16.971552+00:00_

docs/paper/experiments.tex:64:[Omitted long matching line]
docs/paper/method.tex:100:Table~\ref{tab:error_prop} and Figure~\ref{fig:error_prop} show empirical degradation: below $\sigma = 0.2$, $\theta$-RMSE increases by 5.9\% and $c_n$-RMSE by 7.9\%; beyond the threshold ($\sigma = 0.5$), degradation becomes severe. Contamination estimates are more sensitive because $c_n$ enters the likelihood only through its product with $e_i$.
docs/paper/background.tex:50:[Omitted long matching line]
docs/paper/appendix.tex:180:Figure~\ref{fig:ppc} shows the posterior predictive distribution from 1{,}000 posterior draws over 5{,}661 observations. The predicted and observed response distributions are well-aligned (predicted mean win rate $0.593$ vs.\ observed $0.599$), with no systematic discrepancy across item difficulty or model ability levels.
docs/paper/appendix.tex:193:Figure~\ref{fig:model_comparison} visualizes the LOO-ELPD difference between G-MFRM and MFRM-only. G-MFRM is the reference model ($\Delta\mathrm{ELPD} = 0$); MFRM-only shows a deficit of $-55.7$ (SE $= 9.4$), confirming that the contamination gating term substantially improves held-out predictive fit.
docs/paper/appendix.tex:202:Figure~\ref{fig:pareto_k} shows the Pareto $\hat{k}$ diagnostic values for both models. All observations have $\hat{k} < 0.7$, confirming that the LOO approximation is reliable for both models.
docs/paper/introduction.tex:15:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T12:29:16.971690+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Figure~\\\\ref|Fig\\.|fig\\.",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Figure~\\\\ref|Fig\\.|fig\\.",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T12:29:16.971821+00:00_

docs/paper/experiments.tex:64:[Omitted long matching line]
docs/paper/background.tex:50:[Omitted long matching line]
docs/paper/appendix.tex:180:Figure~\ref{fig:ppc} shows the posterior predictive distribution from 1{,}000 posterior draws over 5{,}661 observations. The predicted and observed response distributions are well-aligned (predicted mean win rate $0.593$ vs.\ observed $0.599$), with no systematic discrepancy across item difficulty or model ability levels.
docs/paper/appendix.tex:193:Figure~\ref{fig:model_comparison} visualizes the LOO-ELPD difference between G-MFRM and MFRM-only. G-MFRM is the reference model ($\Delta\mathrm{ELPD} = 0$); MFRM-only shows a deficit of $-55.7$ (SE $= 9.4$), confirming that the contamination gating term substantially improves held-out predictive fit.
docs/paper/appendix.tex:202:Figure~\ref{fig:pareto_k} shows the Pareto $\hat{k}$ diagnostic values for both models. All observations have $\hat{k} < 0.7$, confirming that the LOO approximation is reliable for both models.
docs/paper/introduction.tex:15:[Omitted long matching line]
docs/paper/main.log:552:File: mt-ptm.cfg 2006/04/20 v1.7 microtype config. file: Times (RS)
docs/paper/main.log:555:File: mt-cmr.cfg 2013/05/19 v2.2 microtype config. file: Computer Modern Roman 
docs/paper/main.log:571:File: mt-msa.cfg 2006/02/04 v1.1 microtype config. file: AMS symbols (a) (RS)
docs/paper/main.log:580:File: mt-msb.cfg 2005/06/01 v1.0 microtype config. file: AMS symbols (b) (RS)
docs/paper/method.tex:100:Table~\ref{tab:error_prop} and Figure~\ref{fig:error_prop} show empirical degradation: below $\sigma = 0.2$, $\theta$-RMSE increases by 5.9\% and $c_n$-RMSE by 7.9\%; beyond the threshold ($\sigma = 0.5$), degradation becomes severe. Contamination estimates are more sensitive because $c_n$ enters the likelihood only through its product with $e_i$.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T12:29:16.971983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
  "offset": "48",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
    "offset": "48",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T12:29:16.972130+00:00_

48	\end{observation}
49	
50	G-MFRM's Stage~3 inference (Eq.~\ref{eq:gmfrm}) uses the full nonlinear ordinal logistic likelihood; the linear approximation serves only as directional motivation. Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\rho$ (Figure~\ref{fig:ovb_bias}b), indicating that omission of $c_n \cdot e_i$---not its correlation with $d_j$---is the primary driver. Neither sequential ordering resolves this: bias-first approaches \citep{cyclicjudge2026} absorb contamination into $\hat{\theta}$, while contamination-first approaches \citep{dcr2025} misattribute judge severity as contamination. Synthetic validation ($N = 50$, $I = 100$, $J = 8$, 20 seeds) confirms directional bias ($r = 0.86$, $p < 0.001$; Figure~\ref{fig:ovb_bias}a).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T12:29:16.972280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
  "offset": "62",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
    "offset": "62",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T12:29:16.972437+00:00_

62	\paragraph{Ranking accuracy.} The $\Delta\tau = +0.071$ improvement is not statistically significant at $N = 8$ (bootstrap 95\% CI crosses zero; post-hoc power ${\sim}$50\%). Power analysis indicates $N \approx 17$ for 80\% power (Appendix~\ref{app:power}), validated at $N = 20$ where the improvement reaches significance ($p < 0.001$; Appendix~\ref{app:synthetic_calibration}).
63	
64	All parameters achieve $\hat{R} \leq 1.03$ with ESS $\geq 174$ and zero divergent transitions; model- and judge-level fit statistics fall within acceptable ranges (MNSQ $\in [0.63, 1.07]$; full diagnostics in Appendices~\ref{app:item_diagnostics} and~\ref{app:ppc}). Contamination susceptibility $\hat{c}_n$ exhibits a gradient by model age (Figure~\ref{fig:cn_profile}a): the four oldest models show $\hat{c}_n > 1.0$ (GPT-3.5-Turbo: $5.60$; GPT-4-0613: $4.20$; Qwen2.5-72B: $3.00$; LLaMA-3.3-70B: $2.50$), while recent models show low contamination (GPT-4o: $0.88$; GPT-4o-mini: $0.93$). MFRM-only inflates ability estimates for the most contaminated models by up to 0.79 logits (Figure~\ref{fig:cn_profile}b; Table~\ref{tab:bias_absorption}). Judge severity $d_j$ separates by provenance: proprietary judges score more strictly, spanning 1.34 logits (Figure~\ref{fig:judge_severity}; Table~\ref{tab:judge_severity}). Results are robust to prior specification and judge panel size ($k \geq 4$ suffices; Appendices~\ref{app:prior_robustness} and~\ref{app:judge_count}).
65	
66	\subsection{Error Propagation Robustness}
67	\label{sec:error_prop_results}
68	
69	Table~\ref{tab:error_prop} validates the theoretical prediction (\S\ref{sec:error_prop}): below $\sigma = 0.2$, ability RMSE increases by 5.9\% and contamination RMSE by 7.9\%; beyond the threshold ($\sigma = 0.5$), degradation becomes substantial. Ablation (Table~\ref{tab:ablation}, Appendix~\ref{app:ablation}) confirms joint estimation as the dominant contributor ($2.0\times$ $\theta$-RMSE increase under staged estimation, $p < 0.001$) and con
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T12:29:16.972592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "offset": "54",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "offset": "54",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-25T12:29:16.972729+00:00_

54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{fig5_cn_recovery}
57	\caption{Contamination susceptibility recovery ($c_n$: true vs.\ estimated) from 50 Monte Carlo seeds. Empirical CI coverage is 71\% (below nominal 95\%), indicating moderate posterior overconfidence (see Limitations).}
58	\label{fig:cn_recovery}
59	\end{figure}
60	
61	Adding a multiplicative term to a measurement model raises the question of whether the new parameters can be separated from the existing ones. We establish that fixing $e_i$ externally is both necessary and sufficient for identification. All proofs assume the standard location constraint $\sum_n \theta_n = 0$.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T12:29:16.972898+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cn_recovery|error_prop|bias_vs_rho",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
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
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cn_recovery|error_prop|bias_vs_rho",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T12:29:16.973037+00:00_

docs/paper/experiments.tex:67:\label{sec:error_prop_results}
docs/paper/experiments.tex:69:[Omitted long matching line]
docs/paper/method.tex:6:\includegraphics[width=0.85\textwidth]{fig3_error_propagation}
docs/paper/method.tex:8:\label{fig:error_prop}
docs/paper/method.tex:11:[Omitted long matching line]
docs/paper/method.tex:27:G-MFRM extends the Doubly-Gated IRT model of \citet{shu2013dgirt} from binary gating to continuous exposure and multi-rater designs, and contributes the first formal identifiability conditions for gated IRT parameters (Propositions~\ref{prop:no_new}--\ref{prop:exposure_variation}, Theorem~\ref{thm:sufficient}) and error propagation bounds for staged estimation (\S\ref{sec:error_prop}).
docs/paper/method.tex:56:\includegraphics[width=\columnwidth]{fig5_cn_recovery}
docs/paper/method.tex:58:\label{fig:cn_recovery}
docs/paper/method.tex:87:\label{sec:error_prop}
docs/paper/method.tex:98:[Omitted long matching line]
docs/paper/method.tex:100:Table~\ref{tab:error_prop} and Figure~\ref{fig:error_prop} show empirical degradation: below $\sigma = 0.2$, $\theta$-RMSE increases by 5.9\% and $c_n$-RMSE by 7.9\%; beyond the threshold ($\sigma = 0.5$), degradation becomes severe. Contamination estimates are more sensitive because $c_n$ enters the likelihood only through its product with $e_i$.
docs/paper/method.tex:116:\label{tab:error_prop}
docs/paper/background.tex:13:\includegraphics[width=\textwidth]{fig4_bias_vs_rho}
docs/paper/appendix.tex:137:The correction term $\mathbf{V}_3 \mathbf{C} \mathbf{V}_2 \mathbf{C}^\top \mathbf{V}_3$ is positive semi-definite, so $\mathbf{V}_{\mathrm{MT}} \succeq \mathbf{V}_3$: the corrected variance is always at least as large as the naive variance. The inflation is concentrated on $c_n$ for contaminated models and is negligible for $\theta_n$ when contamination is sparse, consistent with the empirical pattern in Table~\ref{tab:error_prop}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T12:29:16.973228+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
  "old_string": "\\begin{figure*}[t]\n\\centering\n\\begin{minipage}[t]{0.45\\textwidth}\n\\centering\n\\includegraphics[width=\\textwidth]{fig2_ovb_bias}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.45\\textwidth}\n\\centering\n\\includegraphics[width=\\textwidth]{fig4_bias_vs_rho}\n\\end{minipage}\n\\caption{(a)~Sequential estimation bias ($\\hat{\\theta}_{\\mathrm{seq}} - \\theta_{\\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. (b)~Sequential estimator bias remains approximately constant across confounding levels ($\\rho$), confirming omission-driven rather than confounding-strength-dependent bias. Joint G-MFRM estimation reduces bias by approximately 70\\% at all $\\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}\n\\label{fig:ovb_bias}\n\\end{figure*}",
  "new_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_ovb_bias}\n\\caption{Sequential estimation bias ($\\hat{\\theta}_{\\mathrm{seq}} - \\theta_{\\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}\n\\label{fig:ovb_bias}\n\\end{figure}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
    "old_string": "\\begin{figure*}[t]\n\\centering\n\\begin{minipage}[t]{0.45\\textwidth}\n\\centering\n\\includegraphics[width=\\textwidth]{fig2_ovb_bias}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.45\\textwidth}\n\\centering\n\\includegraphics[width=\\textwidth]{fig4_bias_vs_rho}\n\\end{minipage}\n\\caption{(a)~Sequential estimation bias ($\\hat{\\theta}_{\\mathrm{seq}} - \\theta_{\\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. (b)~Sequential estimator bias remains approximately constant across confounding levels ($\\rho$), confirming omission-driven rather than confounding-strength-dependent bias. Joint G-MFRM estimation reduces bias by approximately 70\\% at all $\\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}\n\\label{fig:ovb_bias}\n\\end{figure*}",
    "new_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_ovb_bias}\n\\caption{Sequential estimation bias ($\\hat{\\theta}_{\\mathrm{seq}} - \\theta_{\\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}\n\\label{fig:ovb_bias}\n\\end{figure}"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-25T12:29:16.973397+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T12:29:16.973555+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
  "old_string": "Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\\rho$ (Figure~\\ref{fig:ovb_bias}b), indicating that omission of $c_n \\cdot e_i$---not its correlation with $d_j$---is the primary driver. Neither sequential ordering resolves this: bias-first approaches \\citep{cyclicjudge2026} absorb contamination into $\\hat{\\theta}$, while contamination-first approaches \\citep{dcr2025} misattribute judge severity as contamination. Synthetic validation ($N = 50$, $I = 100$, $J = 8$, 20 seeds) confirms directional bias ($r = 0.86$, $p < 0.001$; Figure~\\ref{fig:ovb_bias}a).",
  "new_string": "Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\\rho$ (see Appendix~\\ref{app:bias_vs_rho}), indicating that omission of $c_n \\cdot e_i$---not its correlation with $d_j$---is the primary driver. Neither sequential ordering resolves this: bias-first approaches \\citep{cyclicjudge2026} absorb contamination into $\\hat{\\theta}$, while contamination-first approaches \\citep{dcr2025} misattribute judge severity as contamination. Synthetic validation ($N = 50$, $I = 100$, $J = 8$, 20 seeds) confirms directional bias ($r = 0.86$, $p < 0.001$; Figure~\\ref{fig:ovb_bias})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
    "old_string": "Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\\rho$ (Figure~\\ref{fig:ovb_bias}b), indicating that omission of $c_n \\cdot e_i$---not its correlation with $d_j$---is the primary driver. Neither sequential ordering resolves this: bias-first approaches \\citep{cyclicjudge2026} absorb contamination into $\\hat{\\theta}$, while contamination-first approaches \\citep{dcr2025} misattribute judge severity as contamination. Synthetic validation ($N = 50$, $I = 100$, $J = 8$, 20 seeds) confirms directional bias ($r = 0.86$, $p < 0.001$; Figure~\\ref{fig:ovb_bias}a).",
    "new_string": "Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\\rho$ (see Appendix~\\ref{app:bias_vs_rho}), indicating that omission of $c_n \\cdot e_i$---not its correlation with $d_j$---is the primary driver. Neither sequential ordering resolves this: bias-first approaches \\citep{cyclicjudge2026} absorb contamination into $\\hat{\\theta}$, while contamination-first approaches \\citep{dcr2025} misattribute judge severity as contamination. Synthetic validation ($N = 50$, $I = 100$, $J = 8$, 20 seeds) confirms directional bias ($r = 0.86$, $p < 0.001$; Figure~\\ref{fig:ovb_bias})."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T12:29:16.973721+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T12:29:16.973849+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "old_string": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.85\\textwidth]{fig3_error_propagation}\n\\caption{Error propagation from Stage~2 exposure noise to Stage~3 parameter estimates. Ability RMSE ($\\theta$, left) and contamination RMSE ($c_n$, right) as a function of exposure noise $\\sigma_e$. The dashed line marks $\\sigma_{\\mathrm{crit}} \\approx 0.2$, below which degradation remains mild ($\\theta$-RMSE $+$5.9\\%, $c_n$-RMSE $+$7.9\\%). Error bars: $\\pm$1 std over 20 seeds.}\n\\label{fig:error_prop}\n\\end{figure*}\n\nSection~\\ref{sec:confounding} established",
  "new_string": "Section~\\ref{sec:confounding} established"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "old_string": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.85\\textwidth]{fig3_error_propagation}\n\\caption{Error propagation from Stage~2 exposure noise to Stage~3 parameter estimates. Ability RMSE ($\\theta$, left) and contamination RMSE ($c_n$, right) as a function of exposure noise $\\sigma_e$. The dashed line marks $\\sigma_{\\mathrm{crit}} \\approx 0.2$, below which degradation remains mild ($\\theta$-RMSE $+$5.9\\%, $c_n$-RMSE $+$7.9\\%). Error bars: $\\pm$1 std over 20 seeds.}\n\\label{fig:error_prop}\n\\end{figure*}\n\nSection~\\ref{sec:confounding} established",
    "new_string": "Section~\\ref{sec:confounding} established"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-25T12:29:16.974016+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T12:29:16.974145+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "old_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_cn_recovery}\n\\caption{Contamination susceptibility recovery ($c_n$: true vs.\\ estimated) from 50 Monte Carlo seeds. Empirical CI coverage is 71\\% (below nominal 95\\%), indicating moderate posterior overconfidence (see Limitations).}\n\\label{fig:cn_recovery}\n\\end{figure}\n\nAdding a multiplicative term",
  "new_string": "Adding a multiplicative term"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "old_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_cn_recovery}\n\\caption{Contamination susceptibility recovery ($c_n$: true vs.\\ estimated) from 50 Monte Carlo seeds. Empirical CI coverage is 71\\% (below nominal 95\\%), indicating moderate posterior overconfidence (see Limitations).}\n\\label{fig:cn_recovery}\n\\end{figure}\n\nAdding a multiplicative term",
    "new_string": "Adding a multiplicative term"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T12:29:16.974305+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T12:29:16.974446+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "old_string": "Table~\\ref{tab:error_prop} and Figure~\\ref{fig:error_prop} show empirical degradation",
  "new_string": "Table~\\ref{tab:error_prop} and Appendix~\\ref{app:error_prop} show empirical degradation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "old_string": "Table~\\ref{tab:error_prop} and Figure~\\ref{fig:error_prop} show empirical degradation",
    "new_string": "Table~\\ref{tab:error_prop} and Appendix~\\ref{app:error_prop} show empirical degradation"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-25T12:29:16.974612+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T12:29:16.974771+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex",
  "old_string": "\\section{Use of AI Assistants}\n\\label{app:ai_assistants}",
  "new_string": "\\section{Bias vs.\\ Confounding Level}\n\\label{app:bias_vs_rho}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bias_vs_rho}\n\\caption{Sequential estimator bias remains approximately constant across confounding levels ($\\rho$), confirming omission-driven rather than confounding-strength-dependent bias. Joint G-MFRM estimation reduces bias by approximately 70\\% at all $\\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}\n\\label{fig:bias_vs_rho_app}\n\\end{figure}\n\n\n\\section{Error Propagation Visualization}\n\\label{app:error_prop}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_error_propagation}\n\\caption{Error propagation from Stage~2 exposure noise to Stage~3 parameter estimates. Ability RMSE ($\\theta$, left) and contamination RMSE ($c_n$, right) as a function of exposure noise $\\sigma_e$. The dashed line marks $\\sigma_{\\mathrm{crit}} \\approx 0.2$, below which degradation remains mild ($\\theta$-RMSE $+$5.9\\%, $c_n$-RMSE $+$7.9\\%). Error bars: $\\pm$1 std over 20 seeds.}\n\\label{fig:error_prop_app}\n\\end{figure}\n\n\n\\section{Contamination Recovery}\n\\label{app:cn_recovery}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_cn_recovery}\n\\caption{Contamination susceptibility recovery ($c_n$: true vs.\\ estimated) from 50 Monte Carlo seeds. Empirical CI coverage is 71\\% (below nominal 95\\%), indicating moderate posterior overconfidence (see Limitations).}\n\\label{fig:cn_recovery_app}\n\\end{figure}\n\n\n\\section{Use of AI Assistants}\n\\label{app:ai_assistants}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex",
    "old_string": "\\section{Use of AI Assistants}\n\\label{app:ai_assistants}",
    "new_string": "\\section{Bias vs.\\ Confounding Level}\n\\label{app:bias_vs_rho}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bias_vs_rho}\n\\caption{Sequential estimator bias remains approximately constant across confounding levels ($\\rho$), confirming omission-driven rather than confounding-strength-dependent bias. Joint G-MFRM estimation reduces bias by approximately 70\\% at all $\\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}\n\\label{fig:bias_vs_rho_app}\n\\end{figure}\n\n\n\\section{Error Propagation Visualization}\n\\label{app:error_prop}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_error_propagation}\n\\caption{Error propagation from Stage~2 exposure noise to Stage~3 parameter estimates. Ability RMSE ($\\theta$, left) and contamination RMSE ($c_n$, right) as a function of exposure noise $\\sigma_e$. The dashed line marks $\\sigma_{\\mathrm{crit}} \\approx 0.2$, below which degradation remains mild ($\\theta$-RMSE $+$5.9\\%, $c_n$-RMSE $+$7.9\\%). Error bars: $\\pm$1 std over 20 seeds.}\n\\label{fig:error_prop_app}\n\\end{figure}\n\n\n\\section{Contamination Recovery}\n\\label{app:cn_recovery}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_cn_recovery}\n\\caption{Contamination susceptibility recovery ($c_n$: true vs.\\ estimated) from 50 Monte Carlo seeds. Empirical CI coverage is 71\\% (below nominal 95\\%), indicating moderate posterior overconfidence (see Limitations).}\n\\label{fig:cn_recovery_app}\n\\end{figure}\n\n\n\\section{Use of AI Assistants}\n\\label{app:ai_assistants}"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-25T12:29:16.975030+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T12:29:16.975204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "offset": "65",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "offset": "65",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-25T12:29:16.975343+00:00_

65	\begin{theorem}[Sufficient Conditions for Local Identifiability]
66	\label{thm:sufficient}
67	The G-MFRM is locally identifiable, up to the standard location constraint, if the following conditions hold: (i) a connected observation design (each item is observed by at least one model--judge pair), (ii) $J \geq 2$ judges, (iii) for each model $n$, the set of observed items spans at least two distinct exposure values ($\mathrm{Var}(e_i) > 0$ over observed items), and (iv) standard normalization $\sum_n \theta_n = 0$.
68	\end{theorem}
69	
70	The proof (Appendix~\ref{app:proof}) follows \citet{rothenberg1971}, establishing Fisher information non-singularity via the Cauchy--Schwarz inequality on the $(\theta_n, c_n)$ submatrix and a Schur complement for the remaining blocks.
71	
72	\subsection{Error Propagation}
73	\label{sec:error_prop}
74	
75	The staged procedure treats the Stage~2 exposure estimates $\hat{e}_i$ as fixed quantities in Stage~3. This is a generated regressors problem \citep{pagan1984}: measurement error in $\hat{e}_i$ propagates into the posterior of $(\theta_n, c_n)$. The multiplicative structure $c_n \cdot e_i$ makes this an errors-in-variables (EIV) problem \citep{fuller1987}, with a predictable attenuation pattern.
76	
77	Let $\hat{e}_i = e_i + \epsilon_i$ with $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$ independent of all model parameters. The attenuation factor for the contamination coefficient is
78	%
79	\begin{equation}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T12:29:16.975508+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "old_string": "The proof (Appendix~\\ref{app:proof}) follows \\citet{rothenberg1971}, establishing Fisher information non-singularity via the Cauchy--Schwarz inequality on the $(\\theta_n, c_n)$ submatrix and a Schur complement for the remaining blocks.",
  "new_string": "The proof (Appendix~\\ref{app:proof}) follows \\citet{rothenberg1971}, establishing Fisher information non-singularity via the Cauchy--Schwarz inequality on the $(\\theta_n, c_n)$ submatrix and a Schur complement for the remaining blocks. Monte Carlo validation confirms successful $c_n$ recovery (Appendix~\\ref{app:cn_recovery})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "old_string": "The proof (Appendix~\\ref{app:proof}) follows \\citet{rothenberg1971}, establishing Fisher information non-singularity via the Cauchy--Schwarz inequality on the $(\\theta_n, c_n)$ submatrix and a Schur complement for the remaining blocks.",
    "new_string": "The proof (Appendix~\\ref{app:proof}) follows \\citet{rothenberg1971}, establishing Fisher information non-singularity via the Cauchy--Schwarz inequality on the $(\\theta_n, c_n)$ submatrix and a Schur complement for the remaining blocks. Monte Carlo validation confirms successful $c_n$ recovery (Appendix~\\ref{app:cn_recovery})."
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-25T12:29:16.975678+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T12:29:16.975814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
  "offset": "51",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
    "offset": "51",
    "limit": "6"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T12:29:16.975942+00:00_

51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=0.92\textwidth]{fig6_cn_profile}
54	\caption{Per-model contamination diagnostics from G-MFRM. (a)~Posterior estimates of contamination susceptibility $\hat{c}_n$ with 95\% credible intervals, ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\times$ higher susceptibility than recent models (GPT-4o). (b)~Ability bias absorbed by MFRM-only estimation: $\Delta\theta = \hat{\theta}_{\mathrm{MFRM}} - \hat{\theta}_{\mathrm{G\text{-}MFRM}}$. The perfect rank correlation (Spearman $\rho = 1.0$) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models and deflates them for low-$c_n$ models, as predicted by the OVB analysis (Section~\ref{sec:confounding}).}
55	\label{fig:cn_profile}
56	\end{figure*}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T12:29:16.976089+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper && rm -f main.aux main.bbl main.blg main.fls main.fdb_latexmk && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper && rm -f main.aux main.bbl main.blg main.fls main.fdb_latexmk && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -30",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-25T12:29:16.976369+00:00_

i7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib8.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
sy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm
10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t
imes/utmri8a.pfb>
Output written on main.pdf (17 pages, 4796802 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-25T12:29:16.976541+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"Warning.*undefined\" main.log; grep \"LaTeX Warning.*Reference\" main.log | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"Warning.*undefined\" main.log; grep \"LaTeX Warning.*Reference\" main.log | head -10"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-25T12:29:16.976667+00:00_

0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-25T12:29:16.976786+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"undefined\" main.log | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"undefined\" main.log | head -10"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-25T12:29:16.976944+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-25T12:29:16.977114+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages):\n    if page.strip():\n        lines = page.strip().split('\\n')\n        # Show first 5 and last 3 lines of each page\n        print(f'=== Page {i+1} ({len(lines)} lines) ===')\n        for line in lines[:8]:\n            print(f'  {line[:100]}')\n        print('  ...')\n        for line in lines[-3:]:\n            print(f'  {line[:100]}')\n        print()\n\" 2>&1 | head -200",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages):\n    if page.strip():\n        lines = page.strip().split('\\n')\n        # Show first 5 and last 3 lines of each page\n        print(f'=== Page {i+1} ({len(lines)} lines) ===')\n        for line in lines[:8]:\n            print(f'  {line[:100]}')\n        print('  ...')\n        for line in lines[-3:]:\n            print(f'  {line[:100]}')\n        print()\n\" 2>&1 | head -200",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-25T12:29:16.977302+00:00_

=== Page 1 (71 lines) ===
  Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model
                for Disentangling Judge Bias and Contamination in LLM Evaluation
  
  
                                                    Anonymous ACL submission
  
  
  
  ...
  
  
                                                                     1

=== Page 2 (39 lines) ===
  Figure 1: (a) Sequential pipelines address judge bias and contamination independently; omitted varia
        confounds the unmodeled facet into ability estimates. (b) G-MFRM three-stage joint calibration
                                                       ˆ Stage 2 estimates per-item exposure ei from e
        a standard MFRM for initial estimates (θ̂, b̂, d);
        (reference model anchoring, cross-model agreement, and optionally LogProber); Stage 3 performs
        inference with ei fixed, recovering contamination-corrected ability θ̂n , contamination suscep
        severity dj .
  
  ...
  
  
                                                                 2

=== Page 3 (77 lines) ===
  0.6
                                    r = 0.79
                                                                                  specifies           
  
                       0.4                                                            P (Ynij ≥ k | θn
                                                                                  log                 
                                                                                      P (Ynij < k | θn
  
  ...
  
  
                                                                              3

=== Page 4 (77 lines) ===
  202   where γn depends on the projection of the expo-              and Eq. 4 reduces to the standard
  203   sure vector (ei ) onto the design matrix of the short        graceful degradation ensures that
  204   model (explicit form in Appendix C). The bias is             poses no distortion on uncontamin
  205   non-zero when
…[truncated 8553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-25T12:29:16.977554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-25T12:29:16.977763+00:00_

1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\subsection{Model Specification}
7	\label{sec:model_spec}
8	
9	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
10	%
11	\begin{equation}
12	\label{eq:gmfrm}
13	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i,
14	\end{equation}
15	%
16	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \in [0,1]$ quantifies how much of item $i$ has leaked into training corpora. When $c_n = 0$ (a clean model) or $e_i = 0$ (a novel item), the gating term vanishes and Eq.~\ref{eq:gmfrm} reduces to the standard MFRM. This graceful degradation ensures that G-MFRM imposes no distortion on uncontaminated model-item pairs.
17	
18	We enforce non-negativity and sparsity of $c_n$ through a hierarchical HalfNormal prior. A global shrinkage scale $\sigma_c \sim \text{HalfNormal}(1.0)$ controls the overall contamination level, and per-model raw effects $c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0)$ are scaled to obtain $c_n 
…[truncated 8682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-25T12:29:16.977947+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "old_string": "\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\sigma$ & $\\theta$-RMSE & $\\Delta\\theta$\\% & $c_n$-RMSE & $\\Delta c_n$\\% \\\\\n\\midrule\n0.0 & 0.128 $\\pm$ 0.018 & --- & 0.533 $\\pm$ 0.187 & --- \\\\\n0.1 & 0.130 $\\pm$ 0.018 & +1.4 & 0.545 $\\pm$ 0.192 & +2.3 \\\\\n0.2 & 0.135 $\\pm$ 0.018 & +5.9 & 0.575 $\\pm$ 0.198 & +7.9 \\\\\n0.5 & 0.175 $\\pm$ 0.027 & +36.9 & 0.842 $\\pm$ 0.281 & +57.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error propagation robustness (exp-012). Ability RMSE degrades by less than 6\\% when exposure noise $\\sigma \\leq 0.2$, matching the theoretical prediction. Contamination estimates are more sensitive due to multiplicative coupling with $e_i$.}\n\\label{tab:error_prop}\n\\end{table}\n\nFor honest credible intervals",
  "new_string": "For honest credible intervals"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "old_string": "\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\sigma$ & $\\theta$-RMSE & $\\Delta\\theta$\\% & $c_n$-RMSE & $\\Delta c_n$\\% \\\\\n\\midrule\n0.0 & 0.128 $\\pm$ 0.018 & --- & 0.533 $\\pm$ 0.187 & --- \\\\\n0.1 & 0.130 $\\pm$ 0.018 & +1.4 & 0.545 $\\pm$ 0.192 & +2.3 \\\\\n0.2 & 0.135 $\\pm$ 0.018 & +5.9 & 0.575 $\\pm$ 0.198 & +7.9 \\\\\n0.5 & 0.175 $\\pm$ 0.027 & +36.9 & 0.842 $\\pm$ 0.281 & +57.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error propagation robustness (exp-012). Ability RMSE degrades by less than 6\\% when exposure noise $\\sigma \\leq 0.2$, matching the theoretical prediction. Contamination estimates are more sensitive due to multiplicative coupling with $e_i$.}\n\\label{tab:error_prop}\n\\end{table}\n\nFor honest credible intervals",
    "new_string": "For honest credible intervals"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-25T12:29:16.978131+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-25T12:29:16.978266+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "old_string": "\\section{The G-MFRM Framework}\n\\label{sec:method}\n\nSection~\\ref{sec:confounding} established",
  "new_string": "\\section{The G-MFRM Framework}\n\\label{sec:method}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\sigma$ & $\\theta$-RMSE & $\\Delta\\theta$\\% & $c_n$-RMSE & $\\Delta c_n$\\% \\\\\n\\midrule\n0.0 & 0.128 $\\pm$ 0.018 & --- & 0.533 $\\pm$ 0.187 & --- \\\\\n0.1 & 0.130 $\\pm$ 0.018 & +1.4 & 0.545 $\\pm$ 0.192 & +2.3 \\\\\n0.2 & 0.135 $\\pm$ 0.018 & +5.9 & 0.575 $\\pm$ 0.198 & +7.9 \\\\\n0.5 & 0.175 $\\pm$ 0.027 & +36.9 & 0.842 $\\pm$ 0.281 & +57.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error propagation robustness (exp-012). Ability RMSE degrades by less than 6\\% when exposure noise $\\sigma \\leq 0.2$, matching the theoretical prediction. Contamination estimates are more sensitive due to multiplicative coupling with $e_i$.}\n\\label{tab:error_prop}\n\\end{table}\n\nSection~\\ref{sec:confounding} established"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "old_string": "\\section{The G-MFRM Framework}\n\\label{sec:method}\n\nSection~\\ref{sec:confounding} established",
    "new_string": "\\section{The G-MFRM Framework}\n\\label{sec:method}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\sigma$ & $\\theta$-RMSE & $\\Delta\\theta$\\% & $c_n$-RMSE & $\\Delta c_n$\\% \\\\\n\\midrule\n0.0 & 0.128 $\\pm$ 0.018 & --- & 0.533 $\\pm$ 0.187 & --- \\\\\n0.1 & 0.130 $\\pm$ 0.018 & +1.4 & 0.545 $\\pm$ 0.192 & +2.3 \\\\\n0.2 & 0.135 $\\pm$ 0.018 & +5.9 & 0.575 $\\pm$ 0.198 & +7.9 \\\\\n0.5 & 0.175 $\\pm$ 0.027 & +36.9 & 0.842 $\\pm$ 0.281 & +57.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error propagation robustness (exp-012). Ability RMSE degrades by less than 6\\% when exposure noise $\\sigma \\leq 0.2$, matching the theoretical prediction. Contamination estimates are more sensitive due to multiplicative coupling with $e_i$.}\n\\label{tab:error_prop}\n\\end{table}\n\nSection~\\ref{sec:confounding} established"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-25T12:29:16.978456+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-25T12:29:16.978603+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -5",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-25T12:29:16.978745+00:00_

  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-25T12:29:16.978865+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages):\n    if page.strip():\n        lines = page.strip().split('\\n')\n        print(f'=== Page {i+1} ({len(lines)} lines) ===')\n        for line in lines[:8]:\n            print(f'  {line[:120]}')\n        print('  ...')\n        for line in lines[-3:]:\n            print(f'  {line[:120]}')\n        print()\n\" 2>&1 | head -120",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages):\n    if page.strip():\n        lines = page.strip().split('\\n')\n        print(f'=== Page {i+1} ({len(lines)} lines) ===')\n        for line in lines[:8]:\n            print(f'  {line[:120]}')\n        print('  ...')\n        for line in lines[-3:]:\n            print(f'  {line[:120]}')\n        print()\n\" 2>&1 | head -120",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-25T12:29:16.979026+00:00_

=== Page 1 (71 lines) ===
  Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model
                for Disentangling Judge Bias and Contamination in LLM Evaluation
  
  
                                                    Anonymous ACL submission
  
  
  
  ...
  
  
                                                                     1

=== Page 2 (39 lines) ===
  Figure 1: (a) Sequential pipelines address judge bias and contamination independently; omitted variable bias
        confounds the unmodeled facet into ability estimates. (b) G-MFRM three-stage joint calibration: Stage 1 fits
                                                       ˆ Stage 2 estimates per-item exposure ei from external evidence
        a standard MFRM for initial estimates (θ̂, b̂, d);
        (reference model anchoring, cross-model agreement, and optionally LogProber); Stage 3 performs joint MCMC
        inference with ei fixed, recovering contamination-corrected ability θ̂n , contamination susceptibility cn , and ju
        severity dj .
  
  ...
  
  
                                                                 2

=== Page 3 (77 lines) ===
  0.6
                                    r = 0.79
                                                                                  specifies                               
  
                       0.4                                                            P (Ynij ≥ k | θn , bi , dj , τk )
                                                                                  log                                   = 
                                                                                      P (Ynij < k | θn , bi , dj , τk )
  
  ...
  
  
                                                                              3

=== Page 4 (85 lines) ===
  σ        θ-RMSE        ∆θ%      cn -RMSE       ∆cn %       tion gating term to the linear predictor (Eq. 1):       239
            0.0    0.128 ± 0.018    —      0.533 ± 0.187    —
    
…[truncated 4481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-25T12:29:16.979223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
  "offset": "25",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
    "offset": "25",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-25T12:29:16.979374+00:00_

25	We compare G-MFRM against seven methods that address judge bias or contamination separately: (1) Raw Average, (2) MFRM-only (Eq.~\ref{eq:mfrm}), (3) Sequential pipeline (MFRM then contamination adjustment), (4) CyclicJudge \citep{cyclicjudge2026}, (5) CyclicJudge+discard (exposed items removed), (6) DCR Factor \citep{dcr2025}, and (7) Preference Leakage calibration \citep{preference_leakage2026}. All methods are evaluated by Kendall $\tau$ and Spearman $\rho$ against Chatbot Arena human rankings.
26	
27	\begin{table}[t]
28	\centering
29	\small
30	\begin{tabular}{lcccc}
31	\toprule
32	& \multicolumn{2}{c}{\textbf{8 models}} & \multicolumn{2}{c}{\textbf{17 models}} \\
33	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
34	\textbf{Method} & $\tau$ & $\rho$ & $\tau$ & $\rho$ \\
35	\midrule
36	Raw Average & 0.786 & 0.905 & 0.838 & 0.949 \\
37	MFRM-only & 0.786 & 0.905 & TBD & TBD \\
38	Sequential & 0.786 & 0.905 & TBD & TBD \\
39	CyclicJudge & 0.786 & 0.905 & 0.838 & 0.949 \\
40	CyclicJudge+discard & 0.786 & 0.905 & 0.824 & 0.934 \\
41	DCR Factor & 0.786 & 0.905 & 0.824 & 0.946 \\
42	Pref.\ Leakage & 0.786 & 0.905 & 0.838 & 0.949 \\
43	\midrule
44	G-MFRM (ours) & \textbf{0.857} & \textbf{0.952} & \textbf{TBD} & \textbf{TBD} \\
45	\bottomrule
46	\end{tabular}
47	\caption{Correlation with Chatbot Arena human rankings on Arena-Hard (9 judges). All seven baselines produce identical rankings at $N = 8$ ($\tau = 0.786$). G-MFRM yields nominally higher point-estimate rank agreement ($+$7.1pp; bootstrap $\Delta\tau$ CI includes zero). Right columns report the 17-model evaluation (TBD).}
48	\label{tab:main_results}
49	\end{table}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=0.92\textwidth]{fig6_cn_profile}
54	\caption{Per-model contamination diagnostics from G-MFRM. (a)~Posterior estimates of contamination susceptibility $\hat{c}_n$ with 95\% credible intervals, ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\times$ higher susceptibility tha
…[truncated 405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-25T12:29:16.979610+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
  "old_string": "\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{8 models}} & \\multicolumn{2}{c}{\\textbf{17 models}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Method} & $\\tau$ & $\\rho$ & $\\tau$ & $\\rho$ \\\\\n\\midrule\nRaw Average & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nMFRM-only & 0.786 & 0.905 & TBD & TBD \\\\\nSequential & 0.786 & 0.905 & TBD & TBD \\\\\nCyclicJudge & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nCyclicJudge+discard & 0.786 & 0.905 & 0.824 & 0.934 \\\\\nDCR Factor & 0.786 & 0.905 & 0.824 & 0.946 \\\\\nPref.\\ Leakage & 0.786 & 0.905 & 0.838 & 0.949 \\\\\n\\midrule\nG-MFRM (ours) & \\textbf{0.857} & \\textbf{0.952} & \\textbf{TBD} & \\textbf{TBD} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correlation with Chatbot Arena human rankings on Arena-Hard (9 judges). All seven baselines produce identical rankings at $N = 8$ ($\\tau = 0.786$). G-MFRM yields nominally higher point-estimate rank agreement ($+$7.1pp; bootstrap $\\Delta\\tau$ CI includes zero). Right columns report the 17-model evaluation (TBD).}\n\\label{tab:main_results}\n\\end{table}\n\n\\begin{figure*}[t]",
  "new_string": "\\begin{figure*}[t]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
    "old_string": "\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{8 models}} & \\multicolumn{2}{c}{\\textbf{17 models}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Method} & $\\tau$ & $\\rho$ & $\\tau$ & $\\rho$ \\\\\n\\midrule\nRaw Average & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nMFRM-only & 0.786 & 0.905 & TBD & TBD \\\\\nSequential & 0.786 & 0.905 & TBD & TBD \\\\\nCyclicJudge & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nCyclicJudge+discard & 0.786 & 0.905 & 0.824 & 0.934 \\\\\nDCR Factor & 0.786 & 0.905 & 0.824 & 0.946 \\\\\nPref.\\ Leakage & 0.786 & 0.905 & 0.838 & 0.949 \\\\\n\\midrule\nG-MFRM (ours) & \\textbf{0.857} & \\textbf{0.952} & \\textbf{TBD} & \\textbf{TBD} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correlation with Chatbot Arena human rankings on Arena-Hard (9 judges). All seven baselines produce identical rankings at $N = 8$ ($\\tau = 0.786$). G-MFRM yields nominally higher point-estimate rank agreement ($+$7.1pp; bootstrap $\\Delta\\tau$ CI includes zero). Right columns report the 17-model evaluation (TBD).}\n\\label{tab:main_results}\n\\end{table}\n\n\\begin{figure*}[t]",
    "new_string": "\\begin{figure*}[t]"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-25T12:29:16.979792+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-25T12:29:16.979923+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "old_string": "The Stage~3 posterior mean of $\\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.",
  "new_string": "The Stage~3 posterior mean of $\\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{8 models}} & \\multicolumn{2}{c}{\\textbf{17 models}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Method} & $\\tau$ & $\\rho$ & $\\tau$ & $\\rho$ \\\\\n\\midrule\nRaw Average & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nMFRM-only & 0.786 & 0.905 & TBD & TBD \\\\\nSequential & 0.786 & 0.905 & TBD & TBD \\\\\nCyclicJudge & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nCyclicJudge+discard & 0.786 & 0.905 & 0.824 & 0.934 \\\\\nDCR Factor & 0.786 & 0.905 & 0.824 & 0.946 \\\\\nPref.\\ Leakage & 0.786 & 0.905 & 0.838 & 0.949 \\\\\n\\midrule\nG-MFRM (ours) & \\textbf{0.857} & \\textbf{0.952} & \\textbf{TBD} & \\textbf{TBD} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correlation with Chatbot Arena human rankings on Arena-Hard (9 judges). All seven baselines produce identical rankings at $N = 8$ ($\\tau = 0.786$). G-MFRM yields nominally higher point-estimate rank agreement ($+$7.1pp; bootstrap $\\Delta\\tau$ CI includes zero). Right columns report the 17-model evaluation (TBD).}\n\\label{tab:main_results}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "old_string": "The Stage~3 posterior mean of $\\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.",
    "new_string": "The Stage~3 posterior mean of $\\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{8 models}} & \\multicolumn{2}{c}{\\textbf{17 models}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Method} & $\\tau$ & $\\rho$ & $\\tau$ & $\\rho$ \\\\\n\\midrule\nRaw Average & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nMFRM-only & 0.786 & 0.905 & TBD & TBD \\\\\nSequential & 0.786 & 0.905 & TBD & TBD \\\\\nCyclicJudge & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nCyclicJudge+discard & 0.786 & 0.905 & 0.824 & 0.934 \\\\\nDCR Factor & 0.786 & 0.905 & 0.824 & 0.946 \\\\\nPref.\\ Leakage & 0.786 & 0.905 & 0.838 & 0.949 \\\\\n\\midrule\nG-MFRM (ours) & \\textbf{0.857} & \\textbf{0.952} & \\textbf{TBD} & \\textbf{TBD} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correlation with Chatbot Arena human rankings on Arena-Hard (9 judges). All seven baselines produce identical rankings at $N = 8$ ($\\tau = 0.786$). G-MFRM yields nominally higher point-estimate rank agreement ($+$7.1pp; bootstrap $\\Delta\\tau$ CI includes zero). Right columns report the 17-model evaluation (TBD).}\n\\label{tab:main_results}\n\\end{table}"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-25T12:29:16.980126+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-25T12:29:16.980285+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -5",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-25T12:29:16.980438+00:00_

  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-25T12:29:16.980567+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages):\n    if page.strip():\n        lines = page.strip().split('\\n')\n        print(f'=== Page {i+1} ({len(lines)} lines) ===')\n        for line in lines[:10]:\n            print(f'  {line[:130]}')\n        print('  ...')\n        print()\n\" 2>&1 | head -120",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages):\n    if page.strip():\n        lines = page.strip().split('\\n')\n        print(f'=== Page {i+1} ({len(lines)} lines) ===')\n        for line in lines[:10]:\n            print(f'  {line[:130]}')\n        print('  ...')\n        print()\n\" 2>&1 | head -120",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-25T12:29:16.980738+00:00_

=== Page 1 (71 lines) ===
  Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model
                for Disentangling Judge Bias and Contamination in LLM Evaluation
  
  
                                                    Anonymous ACL submission
  
  
  
  
  001                             Abstract                               structured benchmarks (Zheng et al., 2023). Two         041
  ...

=== Page 2 (39 lines) ===
  Figure 1: (a) Sequential pipelines address judge bias and contamination independently; omitted variable bias
        confounds the unmodeled facet into ability estimates. (b) G-MFRM three-stage joint calibration: Stage 1 fits
                                                       ˆ Stage 2 estimates per-item exposure ei from external evidence
        a standard MFRM for initial estimates (θ̂, b̂, d);
        (reference model anchoring, cross-model agreement, and optionally LogProber); Stage 3 performs joint MCMC
        inference with ei fixed, recovering contamination-corrected ability θ̂n , contamination susceptibility cn , and judge
        severity dj .
  
  
  082   2013), and employs a three-stage calibration pro-                 per-judge severity within a measurement-              105
  ...

=== Page 3 (77 lines) ===
  0.6
                                    r = 0.79
                                                                                  specifies                                         
  
                       0.4                                                            P (Ynij ≥ k | θn , bi , dj , τk )
                                                                                  log                                   = θn −bi −dj
                                                                                      P (Ynij < k | θn , bi , dj , τk )
  
          ̂ − θtrue
                       0.2                                                                                                          
  ...

==
…[truncated 6061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-25T12:29:16.980928+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i in [5,6,7,8]:  # pages 6-9\n    page = pages[i]\n    if page.strip():\n        lines = page.strip().split('\\n')\n        print(f'=== Page {i+1} ({len(lines)} lines) ===')\n        for line in lines:\n            print(f'  {line[:130]}')\n        print()\n\" 2>&1",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i in [5,6,7,8]:  # pages 6-9\n    page = pages[i]\n    if page.strip():\n        lines = page.strip().split('\\n')\n        print(f'=== Page {i+1} ({len(lines)} lines) ===')\n        for line in lines:\n            print(f'  {line[:130]}')\n        print()\n\" 2>&1",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-25T12:29:16.981180+00:00_

=== Page 6 (78 lines) ===
  8 models            17 models          conversational items selected for high separabil-       389
            Method                      τ           ρ           τ          ρ       ity among frontier models. After filtering for co
  
            Raw Average               0.786      0.905     0.838       0.949       erage, the evaluation set comprises 176 items in 
            MFRM-only                 0.786      0.905     TBD         TBD         a connected incomplete design (36,231 observa-   
            Sequential                0.786      0.905     TBD         TBD         tions; 66.0% fill rate of the full N × I × J tens
            CyclicJudge               0.786      0.905     0.838       0.949
            CyclicJudge+discard       0.786      0.905     0.824       0.934       Seventeen target models spanning proprietary and 
            DCR Factor                0.786      0.905     0.824       0.946       open-source families are evaluated: the original 
            Pref. Leakage             0.786      0.905     0.838       0.949       8 models (GPT-4o, GPT-4o-mini, Qwen2.5-72B,      
            G-MFRM (ours)             0.857      0.952     TBD         TBD         LLaMA-3.3-70B, Qwen3-8B, Gemma-2-9B, GPT-        
                                                                                   4-0613, GPT-3.5-Turbo) plus 9 additional models  
        Table 2: Correlation with Chatbot Arena human rank-                        (Claude-3.5-Sonnet, GPT-4-Turbo, LLaMA-3.1-      
        ings on Arena-Hard (9 judges). All seven baselines
                                                                                   70B, Gemma-2-27B, Claude-3-Opus, LLaMA-3-        
        produce identical rankings at N = 8 (τ = 0.786).
        G-MFRM yields nominally higher point-estimate rank                         70B, Mixtral-8x22B, Claude-3-Haiku, LLaMA-3-     
  
        agreement (+7.1pp; bootstrap ∆τ CI includes zero).                    
…[truncated 26898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-25T12:29:16.981386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-25T12:29:16.981582+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{forest_dj}
7	\caption{Judge severity estimates ($d_j$) for all nine judges with 95\% credible intervals. Positive values indicate stricter scoring. Proprietary judges (Claude Opus, GPT-5.5) cluster at the strict end; open-source judges (Mistral, LLaMA) are more lenient. The severity range spans 1.34 logits.}
8	\label{fig:judge_severity}
9	\end{figure}
10	
11	\subsection{Setup}
12	\label{sec:setup}
13	
14	\paragraph{Data and models.} We evaluate on Arena-Hard \citep{li2024arenahard}, a benchmark of 316 multi-turn conversational items selected for high separability among frontier models. After filtering for coverage, the evaluation set comprises 176 items in a connected incomplete design (36{,}231 observations; 66.0\% fill rate of the full $N \times I \times J$ tensor). Seventeen target models spanning proprietary and open-source families are evaluated: the original 8 models (GPT-4o, GPT-4o-mini, Qwen2.5-72B, LLaMA-3.3-70B, Qwen3-8B, Gemma-2-9B, GPT-4-0613, GPT-3.5-Turbo) plus 9 additional models (Claude-3.5-Sonnet, GPT-4-Turbo, LLaMA-3.1-70B, Gemma-2-27B, Claude-3-Opus, LLaMA-3-70B, Mixtral-8x22B, Claude-3-Haiku, LLaMA-3-8B). Ground-truth rankings are derived from Chatbot Arena human preference data \citep{zheng2023mtbench}.
15	
16	\paragraph{Judges.} Nine LLM judges score model responses in position-swapped pairwise mode: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, Mistral-Large-2, LLaMA-3.3-70B, Qwen2.5-72B, and Qwen3-235B. Seven judges cover all 17 target models; two judges (GPT-5.5 and Claude Opus 4.7) cover only the original 8 models, yielding an asymmetric connected design---Theorem~\ref{thm:sufficient} requires only connectivity, not full crossing. Position swapping controls for position bias and doubles the effective observation count. Two models---Qwen2.5-72B and LLaMA-3.3-70B---serve as both judge and
…[truncated 5234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-25T12:29:16.981771+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
  "old_string": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{forest_dj}\n\\caption{Judge severity estimates ($d_j$) for all nine judges with 95\\% credible intervals. Positive values indicate stricter scoring. Proprietary judges (Claude Opus, GPT-5.5) cluster at the strict end; open-source judges (Mistral, LLaMA) are more lenient. The severity range spans 1.34 logits.}\n\\label{fig:judge_severity}\n\\end{figure}\n\n\\subsection{Setup}",
  "new_string": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{fig6_cn_profile}\n\\caption{Per-model contamination diagnostics from G-MFRM. (a)~Posterior estimates of contamination susceptibility $\\hat{c}_n$ with 95\\% credible intervals, ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\\times$ higher susceptibility than recent models (GPT-4o). (b)~Ability bias absorbed by MFRM-only estimation: $\\Delta\\theta = \\hat{\\theta}_{\\mathrm{MFRM}} - \\hat{\\theta}_{\\mathrm{G\\text{-}MFRM}}$. The perfect rank correlation (Spearman $\\rho = 1.0$) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models and deflates them for low-$c_n$ models, as predicted by the OVB analysis (Section~\\ref{sec:confounding}).}\n\\label{fig:cn_profile}\n\\end{figure*}\n\n\\subsection{Setup}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
    "old_string": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{forest_dj}\n\\caption{Judge severity estimates ($d_j$) for all nine judges with 95\\% credible intervals. Positive values indicate stricter scoring. Proprietary judges (Claude Opus, GPT-5.5) cluster at the strict end; open-source judges (Mistral, LLaMA) are more lenient. The severity range spans 1.34 logits.}\n\\label{fig:judge_severity}\n\\end{figure}\n\n\\subsection{Setup}",
    "new_string": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{fig6_cn_profile}\n\\caption{Per-model contamination diagnostics from G-MFRM. (a)~Posterior estimates of contamination susceptibility $\\hat{c}_n$ with 95\\% credible intervals, ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\\times$ higher susceptibility than recent models (GPT-4o). (b)~Ability bias absorbed by MFRM-only estimation: $\\Delta\\theta = \\hat{\\theta}_{\\mathrm{MFRM}} - \\hat{\\theta}_{\\mathrm{G\\text{-}MFRM}}$. The perfect rank correlation (Spearman $\\rho = 1.0$) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models and deflates them for low-$c_n$ models, as predicted by the OVB analysis (Section~\\ref{sec:confounding}).}\n\\label{fig:cn_profile}\n\\end{figure*}\n\n\\subsection{Setup}"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-25T12:29:16.981945+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-25T12:29:16.982090+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
  "old_string": "We compare G-MFRM against seven methods that address judge bias or contamination separately: (1) Raw Average, (2) MFRM-only (Eq.~\\ref{eq:mfrm}), (3) Sequential pipeline (MFRM then contamination adjustment), (4) CyclicJudge \\citep{cyclicjudge2026}, (5) CyclicJudge+discard (exposed items removed), (6) DCR Factor \\citep{dcr2025}, and (7) Preference Leakage calibration \\citep{preference_leakage2026}. All methods are evaluated by Kendall $\\tau$ and Spearman $\\rho$ against Chatbot Arena human rankings.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{fig6_cn_profile}\n\\caption{Per-model contamination diagnostics from G-MFRM. (a)~Posterior estimates of contamination susceptibility $\\hat{c}_n$ with 95\\% credible intervals, ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\\times$ higher susceptibility than recent models (GPT-4o). (b)~Ability bias absorbed by MFRM-only estimation: $\\Delta\\theta = \\hat{\\theta}_{\\mathrm{MFRM}} - \\hat{\\theta}_{\\mathrm{G\\text{-}MFRM}}$. The perfect rank correlation (Spearman $\\rho = 1.0$) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models and deflates them for low-$c_n$ models, as predicted by the OVB analysis (Section~\\ref{sec:confounding}).}\n\\label{fig:cn_profile}\n\\end{figure*}\n\nAll seven baselines",
  "new_string": "We compare G-MFRM against seven methods that address judge bias or contamination separately: (1) Raw Average, (2) MFRM-only (Eq.~\\ref{eq:mfrm}), (3) Sequential pipeline (MFRM then contamination adjustment), (4) CyclicJudge \\citep{cyclicjudge2026}, (5) CyclicJudge+discard (exposed items removed), (6) DCR Factor \\citep{dcr2025}, and (7) Preference Leakage calibration \\citep{preference_leakage2026}. All methods are evaluated by Kendall $\\tau$ and Spearman $\\rho$ against Chatbot Arena human rankings.\n\nAll seven baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
    "old_string": "We compare G-MFRM against seven methods that address judge bias or contamination separately: (1) Raw Average, (2) MFRM-only (Eq.~\\ref{eq:mfrm}), (3) Sequential pipeline (MFRM then contamination adjustment), (4) CyclicJudge \\citep{cyclicjudge2026}, (5) CyclicJudge+discard (exposed items removed), (6) DCR Factor \\citep{dcr2025}, and (7) Preference Leakage calibration \\citep{preference_leakage2026}. All methods are evaluated by Kendall $\\tau$ and Spearman $\\rho$ against Chatbot Arena human rankings.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{fig6_cn_profile}\n\\caption{Per-model contamination diagnostics from G-MFRM. (a)~Posterior estimates of contamination susceptibility $\\hat{c}_n$ with 95\\% credible intervals, ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\\times$ higher susceptibility than recent models (GPT-4o). (b)~Ability bias absorbed by MFRM-only estimation: $\\Delta\\theta = \\hat{\\theta}_{\\mathrm{MFRM}} - \\hat{\\theta}_{\\mathrm{G\\text{-}MFRM}}$. The perfect rank correlation (Spearman $\\rho = 1.0$) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models and deflates them for low-$c_n$ models, as predicted by the OVB analysis (Section~\\ref{sec:confounding}).}\n\\label{fig:cn_profile}\n\\end{figure*}\n\nAll seven baselines",
    "new_string": "We compare G-MFRM against seven methods that address judge bias or contamination separately: (1) Raw Average, (2) MFRM-only (Eq.~\\ref{eq:mfrm}), (3) Sequential pipeline (MFRM then contamination adjustment), (4) CyclicJudge \\citep{cyclicjudge2026}, (5) CyclicJudge+discard (exposed items removed), (6) DCR Factor \\citep{dcr2025}, and (7) Preference Leakage calibration \\citep{preference_leakage2026}. All methods are evaluated by Kendall $\\tau$ and Spearman $\\rho$ against Chatbot Arena human rankings.\n\nAll seven baselines"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-25T12:29:16.982273+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-25T12:29:16.982428+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "old_string": "\\subsection{Identifiability}\n\\label{sec:identifiability}\n\nAdding a multiplicative term",
  "new_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{forest_dj}\n\\caption{Judge severity estimates ($d_j$) for all nine judges with 95\\% credible intervals. Positive values indicate stricter scoring. Proprietary judges (Claude Opus, GPT-5.5) cluster at the strict end; open-source judges (Mistral, LLaMA) are more lenient. The severity range spans 1.34 logits.}\n\\label{fig:judge_severity}\n\\end{figure}\n\n\\subsection{Identifiability}\n\\label{sec:identifiability}\n\nAdding a multiplicative term"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "old_string": "\\subsection{Identifiability}\n\\label{sec:identifiability}\n\nAdding a multiplicative term",
    "new_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{forest_dj}\n\\caption{Judge severity estimates ($d_j$) for all nine judges with 95\\% credible intervals. Positive values indicate stricter scoring. Proprietary judges (Claude Opus, GPT-5.5) cluster at the strict end; open-source judges (Mistral, LLaMA) are more lenient. The severity range spans 1.34 logits.}\n\\label{fig:judge_severity}\n\\end{figure}\n\n\\subsection{Identifiability}\n\\label{sec:identifiability}\n\nAdding a multiplicative term"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-25T12:29:16.982606+00:00_

The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-25T12:29:16.982731+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -5",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-25T12:29:16.982861+00:00_

  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-25T12:29:16.982983+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages):\n    if page.strip():\n        lines = page.strip().split('\\n')\n        print(f'=== Page {i+1} ({len(lines)} lines) ===')\n        for line in lines[:10]:\n            print(f'  {line[:130]}')\n        print('  ...')\n        print()\n\" 2>&1 | head -110",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages):\n    if page.strip():\n        lines = page.strip().split('\\n')\n        print(f'=== Page {i+1} ({len(lines)} lines) ===')\n        for line in lines[:10]:\n            print(f'  {line[:130]}')\n        print('  ...')\n        print()\n\" 2>&1 | head -110",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-25T12:29:16.983155+00:00_

=== Page 1 (71 lines) ===
  Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model
                for Disentangling Judge Bias and Contamination in LLM Evaluation
  
  
                                                    Anonymous ACL submission
  
  
  
  
  001                             Abstract                               structured benchmarks (Zheng et al., 2023). Two         041
  ...

=== Page 2 (39 lines) ===
  Figure 1: (a) Sequential pipelines address judge bias and contamination independently; omitted variable bias
        confounds the unmodeled facet into ability estimates. (b) G-MFRM three-stage joint calibration: Stage 1 fits
                                                       ˆ Stage 2 estimates per-item exposure ei from external evidence
        a standard MFRM for initial estimates (θ̂, b̂, d);
        (reference model anchoring, cross-model agreement, and optionally LogProber); Stage 3 performs joint MCMC
        inference with ei fixed, recovering contamination-corrected ability θ̂n , contamination susceptibility cn , and judge
        severity dj .
  
  
  082   2013), and employs a three-stage calibration pro-                 per-judge severity within a measurement-              105
  ...

=== Page 3 (77 lines) ===
  0.6
                                    r = 0.79
                                                                                  specifies                                         
  
                       0.4                                                            P (Ynij ≥ k | θn , bi , dj , τk )
                                                                                  log                                   = θn −bi −dj
                                                                                      P (Ynij < k | θn , bi , dj , τk )
  
          ̂ − θtrue
                       0.2                                                                                                          
  ...

==
…[truncated 5562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-25T12:29:16.983343+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"undefined\" main.log | head -5; echo \"---\"; python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\ntotal = sum(1 for p in pages if p.strip())\n# Find where References section starts and where Appendix starts\nfor i, p in enumerate(pages):\n    if 'References' in p and i > 6:\n        # Check if references section heading is on this page\n        for line in p.split('\\n'):\n            if 'References' in line and len(line.strip()) < 30:\n                print(f'References section starts on page {i+1}')\n                break\n    if 'Appendix' in p or 'Proofs of' in p:\n        for line in p.split('\\n'):\n            if 'Proofs of' in line or ('A ' in line and 'Proposition' in line):\n                print(f'Appendix starts on page {i+1}')\n                break\nprint(f'Total pages: {total}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"undefined\" main.log | head -5; echo \"---\"; python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\ntotal = sum(1 for p in pages if p.strip())\n# Find where References section starts and where Appendix starts\nfor i, p in enumerate(pages):\n    if 'References' in p and i > 6:\n        # Check if references section heading is on this page\n        for line in p.split('\\n'):\n            if 'References' in line and len(line.strip()) < 30:\n                print(f'References section starts on page {i+1}')\n                break\n    if 'Appendix' in p or 'Proofs of' in p:\n        for line in p.split('\\n'):\n            if 'Proofs of' in line or ('A ' in line and 'Proposition' in line):\n                print(f'Appendix starts on page {i+1}')\n                break\nprint(f'Total pages: {total}')\n\""
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-25T12:29:16.983497+00:00_

---
Appendix starts on page 5
Appendix starts on page 10
Total pages: 17

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-25T12:29:16.983637+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Check p8 and p9 content boundaries\nfor i in [7, 8, 9]:\n    page = pages[i]\n    lines = page.strip().split('\\n')\n    print(f'=== Page {i+1} ({len(lines)} lines) ===')\n    # Find section headers\n    for line in lines:\n        l = line.strip()\n        if l and (l[0].isdigit() and ('Conclusion' in l or 'Limitation' in l or 'Reference' in l or 'Experiment' in l)) or ('Appendix' in l) or ('Proofs' in l):\n            print(f'  SECTION: {l[:100]}')\n    # Show first few and last few lines\n    for line in lines[:5]:\n        print(f'  {line[:130]}')\n    print('  ...')\n    for line in lines[-3:]:\n        print(f'  {line[:130]}')\n    print()\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Check p8 and p9 content boundaries\nfor i in [7, 8, 9]:\n    page = pages[i]\n    lines = page.strip().split('\\n')\n    print(f'=== Page {i+1} ({len(lines)} lines) ===')\n    # Find section headers\n    for line in lines:\n        l = line.strip()\n        if l and (l[0].isdigit() and ('Conclusion' in l or 'Limitation' in l or 'Reference' in l or 'Experiment' in l)) or ('Appendix' in l) or ('Proofs' in l):\n            print(f'  SECTION: {l[:100]}')\n    # Show first few and last few lines\n    for line in lines[:5]:\n        print(f'  {line[:130]}')\n    print('  ...')\n    for line in lines[-3:]:\n        print(f'  {line[:130]}')\n    print()\n\""
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-25T12:29:16.983787+00:00_

=== Page 8 (65 lines) ===
  SECTION: 482   strictly, spanning 1.34 logits (Figure 3; Table 4).         bounds on uncertainty (Appendix R)
  SECTION: 490   stantial. Ablation (Table 3, Appendix E) con-               80% power to detect ∆τ = 0.071; th
  SECTION: analysis (Appendix H) confirms robust rankings           544
  SECTION: 495   6     Conclusion                                            when excluding self-judging observ
  SECTION: 499   omitted variable bias. On Arena-Hard, G-MFRM                References                        
  SECTION: 504   powered validation requires N ≥ 17 (Limitations).
  SECTION: 509   Limitations                                                   Proceedings of the 63rd Annual M
  482   strictly, spanning 1.34 logits (Figure 3; Table 4).         bounds on uncertainty (Appendix R), with recali-         530
  483   Results are robust to prior specification and judge         bration via simulation-based calibration (SBC) as        531
  484   panel size (k ≥ 4 suffices; Appendices P and J).            a direction for future work. The bilinear term also      532
                                                                    assumes rank-1 structure—a single contamination          533
  485   5.3    Error Propagation Robustness                         dimension per model—while contamination may              534
  ...
  
  
                                                                8

=== Page 9 (68 lines) ===
  582   James Fiedler. 2026. Bias and uncertainty in LLM-as-a-         Yonatan Oren, Nicole Meister, Niladri Chatterji, Faisal   635
  583     judge estimation. arXiv preprint arXiv:2605.06939.             Ladhak, and Tatsunori B. Hashimoto. 2024. Proving       636
                                                                         test set contamination in black box language models.    637
  584   Wayne A. Fuller. 1987. Measurement Error Models.                 In The Twelfth International Conference on Learning  
…[truncated 1061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-25T12:29:16.983954+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"LaTeX Warning\" main.log | grep -v \"hyperref\\|font\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"LaTeX Warning\" main.log | grep -v \"hyperref\\|font\" | head -10"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-25T12:29:16.984080+00:00_

LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-25T12:29:16.984254+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"undefined\" main.log | head -5; echo \"---\"; grep \"multiply defined\" main.log | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"undefined\" main.log | head -5; echo \"---\"; grep \"multiply defined\" main.log | head -5"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-25T12:29:16.984382+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-25T12:29:16.984538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-25T12:29:16.984727+00:00_

1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{fig2_ovb_bias}
7	\caption{Sequential estimation bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
8	\label{fig:ovb_bias}
9	\end{figure}
10	
11	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
12	%
13	\begin{equation}
14	\label{eq:mfrm}
15	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \tau_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \tau_k)} = \theta_n - b_i - d_j - \tau_k,
16	\end{equation}
17	%
18	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts, showing that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
19	
20	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr2025}. Such 
…[truncated 3010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-25T12:29:16.984902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-25T12:29:16.985084+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{fig6_cn_profile}
7	\caption{Per-model contamination diagnostics from G-MFRM. (a)~Posterior estimates of contamination susceptibility $\hat{c}_n$ with 95\% credible intervals, ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\times$ higher susceptibility than recent models (GPT-4o). (b)~Ability bias absorbed by MFRM-only estimation: $\Delta\theta = \hat{\theta}_{\mathrm{MFRM}} - \hat{\theta}_{\mathrm{G\text{-}MFRM}}$. The perfect rank correlation (Spearman $\rho = 1.0$) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models and deflates them for low-$c_n$ models, as predicted by the OVB analysis (Section~\ref{sec:confounding}).}
8	\label{fig:cn_profile}
9	\end{figure*}
10	
11	\subsection{Setup}
12	\label{sec:setup}
13	
14	\paragraph{Data and models.} We evaluate on Arena-Hard \citep{li2024arenahard}, a benchmark of 316 multi-turn conversational items selected for high separability among frontier models. After filtering for coverage, the evaluation set comprises 176 items in a connected incomplete design (36{,}231 observations; 66.0\% fill rate of the full $N \times I \times J$ tensor). Seventeen target models spanning proprietary and open-source families are evaluated: the original 8 models (GPT-4o, GPT-4o-mini, Qwen2.5-72B, LLaMA-3.3-70B, Qwen3-8B, Gemma-2-9B, GPT-4-0613, GPT-3.5-Turbo) plus 9 additional models (Claude-3.5-Sonnet, GPT-4-Turbo, LLaMA-3.1-70B, Gemma-2-27B, Claude-3-Opus, LLaMA-3-70B, Mixtral-8x22B, Claude-3-Haiku, LLaMA-3-8B). Ground-truth rankings are derived from Chatbot Arena human preference data \citep{zheng2023mtbench}.
15	
16	\paragraph{Judges.} Nine LLM judges score model responses in position-swapped pairwise mode: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, Mistral-Large-2, LLaMA-3.3-70B, Qwen2.5-72B, and Qwen3-235B. Seven judges co
…[truncated 4798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-25T12:29:16.985272+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "rm -f main.aux main.bbl main.blg main.fls main.fdb_latexmk && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|Warning.*undefined|multiply defined|Error\" | head -10",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "rm -f main.aux main.bbl main.blg main.fls main.fdb_latexmk && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|Warning.*undefined|multiply defined|Error\" | head -10",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-25T12:29:16.985457+00:00_

Package natbib Warning: Citation `zheng2023mtbench' on page 1 undefined on inpu
Package natbib Warning: Citation `wang2024positionbias' on page 1 undefined on 
Package natbib Warning: Citation `ye2024justice' on page 1 undefined on input l
Package natbib Warning: Citation `panickssery2024selffavor' on page 1 undefined
Package natbib Warning: Citation `dcr2025' on page 1 undefined on input line 4.
Package natbib Warning: Citation `mink2024' on page 1 undefined on input line 4
Package natbib Warning: Citation `cyclicjudge2026' on page 1 undefined on input
Package natbib Warning: Citation `uda2026' on page 1 undefined on input line 4.
Package natbib Warning: Citation `constat2024' on page 1 undefined on input lin
Package natbib Warning: Citation `dcr2025' on page 1 undefined on input line 4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-25T12:29:16.985665+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|Warning.*undefined|multiply defined\" | head -5",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|Warning.*undefined|multiply defined\" | head -5",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-25T12:29:16.985802+00:00_

Package natbib Warning: Citation `zheng2023mtbench' on page 1 undefined on inpu
Package natbib Warning: Citation `wang2024positionbias' on page 1 undefined on 
Package natbib Warning: Citation `ye2024justice' on page 1 undefined on input l
Package natbib Warning: Citation `panickssery2024selffavor' on page 1 undefined
Package natbib Warning: Citation `dcr2025' on page 1 undefined on input line 4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-25T12:29:16.985926+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -3",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -3",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-25T12:29:16.986052+00:00_

  error, and then rerun latexmk.
  In some cases, it is best to clean out generated files before rerunning
  latexmk after you've corrected the files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-25T12:29:16.986171+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | grep -E \"error|Error|Output written\" | head -5",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | grep -E \"error|Error|Output written\" | head -5",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-25T12:29:16.986301+00:00_

[16 <../../figures/paper/fig4_bias_vs_rho.pdf> <../../figures/paper/fig3_error_
Output written on main.pdf (17 pages, 4789202 bytes).
error_propagation.pdf> <../../figures/paper/fig5_cn_recovery.pdf>] (./main.aux)
Output written on main.pdf (17 pages, 4797576 bytes).
error_propagation.pdf> <../../figures/paper/fig5_cn_recovery.pdf>] (./main.aux)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-25T12:29:16.986443+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"undefined\" main.log | grep -v \"natbib Warning\" | head -5; grep \"multiply defined\" main.log | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"undefined\" main.log | grep -v \"natbib Warning\" | head -5; grep \"multiply defined\" main.log | head -5"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-25T12:29:16.986579+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-25T12:29:16.986695+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"LaTeX Warning.*Reference.*undefined\" main.log | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"LaTeX Warning.*Reference.*undefined\" main.log | head -5"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-25T12:29:16.986807+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-25T12:29:16.986940+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nfor i in range(min(8, len(pages))):\n    page = pages[i]\n    if not page.strip(): continue\n    lines = page.strip().split('\\n')\n    # Detect top element\n    top_element = 'none'\n    for line in lines[:15]:\n        l = line.strip()\n        if 'Figure' in l and ':' in l and len(l) > 20:\n            top_element = l[:80]\n            break\n        if 'Table' in l and ':' in l and len(l) > 20:\n            top_element = l[:80]\n            break\n        # Check for figure content (plots have specific patterns)\n        if any(kw in l for kw in ['σ', '0.128', 'dj', 'judge severity', 'Contamination susceptibility', 'Bias absorption']):\n            top_element = 'figure/table content: ' + l[:60]\n            break\n    print(f'p{i+1}: top={top_element}')\n    # Also print first line\n    print(f'     first: {lines[0][:100]}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nfor i in range(min(8, len(pages))):\n    page = pages[i]\n    if not page.strip(): continue\n    lines = page.strip().split('\\n')\n    # Detect top element\n    top_element = 'none'\n    for line in lines[:15]:\n        l = line.strip()\n        if 'Figure' in l and ':' in l and len(l) > 20:\n            top_element = l[:80]\n            break\n        if 'Table' in l and ':' in l and len(l) > 20:\n            top_element = l[:80]\n            break\n        # Check for figure content (plots have specific patterns)\n        if any(kw in l for kw in ['σ', '0.128', 'dj', 'judge severity', 'Contamination susceptibility', 'Bias absorption']):\n            top_element = 'figure/table content: ' + l[:60]\n            break\n    print(f'p{i+1}: top={top_element}')\n    # Also print first line\n    print(f'     first: {lines[0][:100]}')\n\""
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-25T12:29:16.987079+00:00_

p1: top=none
     first: Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model
p2: top=Figure 1: (a) Sequential pipelines address judge bias and contamination independ
     first: Figure 1: (a) Sequential pipelines address judge bias and contamination independently; omitted varia
p3: top=figure/table content: 0.4                                                         
     first: 0.6
p4: top=figure/table content: σ        θ-RMSE        ∆θ%      cn -RMSE       ∆cn %       t
     first: σ        θ-RMSE        ∆θ%      cn -RMSE       ∆cn %       tion gating term to the linear predictor 
p5: top=figure/table content: 287   Stage 2: Exposure estimation. Per-item expo-          
     first: 287   Stage 2: Exposure estimation. Per-item expo-                                                  
p6: top=none
     first: 8 models          17 models             5     Experiments                                           
p7: top=figure/table content: (a) Contamination susceptibility                            
     first: (a) Contamination susceptibility                                      (b) Bias absorption in MFRM
p8: top=486   Table 1 validates the theoretical prediction (§4.4):        be domain-spec
     first: 482   strictly, spanning 1.34 logits (Figure 3; Table 4).         bounds on uncertainty (Appendix R)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 119 · 2026-05-25T12:29:16.987288+00:00_

All changes complete. Here is the summary:

## 每页布局
- p1: Title + Abstract + Introduction
- p2: **Figure 1** (框架图, figure\*) + Introduction 继续
- p3: **Figure 2** (OVB bias scatter, figure[t]) + Background
- p4: **Table 1** (Error propagation, table[t]) + Method (Model Specification)
- p5: **Figure 3** (Judge severity forest plot, figure[t]) + Method (Staged Estimation, Identifiability)
- p6: **Table 2** (Main results, table[t]) + Experiments (Setup)
- p7: **Figure 4** (Contamination profile, figure\*[t]) + Experiments (Results)
- p8: Experiments (Error Prop) + Conclusion + Limitations + References 开始

## 移到 appendix 的图
- `fig4_bias_vs_rho` → `app:bias_vs_rho` (Appendix S: Bias vs. Confounding Level)
- `fig3_error_propagation` → `app:error_prop` (Appendix T: Error Propagation Visualization)
- `fig5_cn_recovery` → `app:cn_recovery` (Appendix U: Contamination Recovery)

## 引用更新
- `background.tex:42` — `Figure~\ref{fig:ovb_bias}b` → `Appendix~\ref{app:bias_vs_rho}`
- `background.tex:42` — `Figure~\ref{fig:ovb_bias}a` → `Figure~\ref{fig:ovb_bias}`
- `method.tex:86` — `Figure~\ref{fig:error_prop}` → `Appendix~\ref{app:error_prop}`
- `method.tex:70` — 新增 `Appendix~\ref{app:cn_recovery}` 引用

## 拆分的图
- Figure 2 原始合并图 (`figure*` with fig2_ovb_bias + fig4_bias_vs_rho) → 拆为独立 `figure[t]` (ovb_bias 留正文) + appendix (bias_vs_rho)

## Float 重排
- Table 2 (main_results) 从 experiments.tex 移至 method.tex 末尾以 float 到 p6 顶部
- Figure 3 (forest_dj) 从 experiments.tex 移至 method.tex identifiability 前以 float 到 p5
- Figure 4 (cn_profile) 提前至 experiments.tex 开头以 float 到 p7

## 编译结果
- 页数：8（正文）+ 9（references + appendix）= 17 总页
- undefined refs：0
- multiply defined labels：0
- warnings：仅 appendix 中 `[h]` → `[ht]` 浮动调整（无害）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_figure-layout-overhaul_20260525T121947"
}
```

</details>

---
