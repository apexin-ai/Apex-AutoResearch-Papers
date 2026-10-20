# ops arr submission form

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_ops_arr-submission-form_20260523T041551.jsonl`
- **Structured JSON:** [`d08dcd66dedd538f93dd.json`](../../sessions/d0/d08dcd66dedd538f93dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-23T04:18:15.328953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T04:18:15.329283+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\irtfit}{\textsc{IRT-FIT}}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	\input{sections/abstract}
30	\end{abstract}
31	
32	\input{sections/introduction}
33	\input{sections/related_work}
34	\input{sections/method}
35	\input{sections/results}
36	\input{sections/discussion}
37	\input{sections/conclusion}
38	
39	\input{sections/limitations}
40	
41	\section*{Reproducibility Statement}
42	Code and response data will be released upon acceptance.
43	Bootstrap confidence intervals use the percentile method with 10,000 resamples.
44	All three model families use clean baseline seeds 0--9 ($n{=}10$ per family).
45	Pre-calibrated 4PL item parameters are from the publicly available PSN-IRT item bank \citep{psnirt2026}.
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{sections/appendix}
51	
52	\end{document}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T04:18:15.329508+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T04:18:15.329671+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T04:18:15.329826+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T04:18:15.329977+00:00_

paper/sections/experiments.tex
paper/sections/background.tex
paper/sections/sec_empirical.tex
paper/sections/sec_simulation.tex
paper/sections/sec_setup.tex
paper/sections/sec_ctrl_contam.tex
paper/sections/related_work.tex
paper/main.tex
paper/sections/method.tex
paper/sections/abstract.tex
paper/sections/conclusion.tex
paper/sections/introduction.tex
paper/sections/results.tex
paper/sections/discussion.tex
paper/sections/appendix.tex
paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T04:18:15.330104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T04:18:15.330230+00:00_

1	Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We present the first controlled characterization of IRT person-fit statistics for detecting SFT-stage contamination: the framework requires only binary response patterns from the target model---no access to weights, gradients, logits, or training data---combined with externally calibrated 4PL item parameters from a large-scale item bank; diagnostic $\theta$-anchoring additionally requires a clean baseline.
3	A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	Using $\ell_z^*$ in a matched-difference design ($\Delta\ell_z^*$) across three 7--8B model families ($n{=}10$ clean baseline seeds per model family) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify three behavior boundaries:
5	(1) model-specific $\theta$-shift dynamics, where contamination-induced ability inflation absorbs the person-fit signal; $\theta$-anchoring is necessary for reliable detection of high-ability models at high contamination (2.4$\times$ amplification, inter-seed CV reduced from 60\% to 19\%);
6	(2) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack $\ell_z^*$'s diagnostic capabilities (seen/unseen decomposition, mechanistic $\theta$-shift analysis);
7	and (3, exploratory) ability-dependent non-monotonic dose-response under free-$\theta$ estimation, driven by $\theta$-shift absorption; $\theta$-anchored analysis reveals stable detection with a strong positive dose-response at higher contamination levels.
8	These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T04:18:15.330405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T04:18:15.330542+00:00_

1	\section*{Limitations}
2	
3	Our controlled experiments cover three 7--8B model families with QLoRA fine-tuning; generalization to larger scales, mixture-of-experts architectures, full-parameter fine-tuning, and pretraining-stage contamination remains untested.
4	Most contamination conditions use a single training run, and multi-seed replication (available for Qwen) reveals high seed dependence at 50\% contamination (CV${=}$60\%), partially resolved by $\theta$-anchoring; the post-RL characterization is $N{=}1$.
5	The framework depends on pre-calibrated 4PL item parameters from PSN-IRT, whose calibration sample may include contaminated models, and we do not provide head-to-head comparison with logit-based methods (MIA, ConStat) that operate at a different information level.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T04:18:15.330667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T04:18:15.330932+00:00_

1	\section{Simulation Validation}
2	\label{app:simulation}
3	
4	Under the null (no contamination), bootstrap $\ell_z^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
5	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
6	$\ell_z^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
7	
8	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels.
9	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
10	The empirical power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution, achieves $R^2 = 0.957$ against simulated values, with approximate minimum benchmark size of $n \geq 7{,}958$ items for 80\% power at 15\% contamination under MMLU item parameters.
11	
12	\section{4PL vs.\ 3PL Ablation Details}
13	\label{app:4pl_ablation}
14	
15	Table~\ref{tab:4pl_3pl_power} reports detection power (proportion of 2{,}000 simulation replicates rejecting $H_0$ at $\alpha{=}0.05$, two-sided) for 4PL and 3PL parameterizations across five benchmarks and seven contamination levels.
16	The 4PL model yields higher power than 3PL at every non-trivial contamination level on every benchmark.
17	The advantage is largest on MMLU and HellaSwag, where upper-asymptote ($d < 1$) violations are most prevalent, and smallest on ARC-Challenge and HumanEval, where limited item counts constrain power under both parameterizations.
18	
19	Power is non-monotonic at 75\% contamination under 4PL on four of five benchmarks (e.g., MMLU: $.952 \to .938$; GSM8K: $.846 \to .802$).
20	This reflects the $\theta$-shift boundary condition described in \S\ref{sec:inverted_u}: at
…[truncated 22148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T04:18:15.331091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T04:18:15.331305+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Detection Signal Across Model Families}
5	\label{sec:detection}
6	
7	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
8	All confidence intervals exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
9	
10	On MMLU, effect sizes range from $|d|{=}2.27$ (Llama at 15\%) to $|d|{=}7.44$ (Qwen at 25\%), with Qwen at 5\% ($|d|{=}4.15$) confirming detection at the lowest contamination level tested. Llama ($|d|{=}2.27$/$2.97$/$2.50$) and Mistral ($|d|{=}3.01$/$3.50$) show comparable magnitudes.
11	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
12	
13	Clean-model $\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\text{SD}{=}2.05$), Llama ${+}0.29$ ($\text{SD}{=}1.45$), and ARC-C Qwen ${-}5.42$ ($\text{SD}{=}0.16$).
14	Absolute $\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\ell_z^*$ at 15\% (${+}3.85$) is still positive.
15	The $\Delta\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}2.27$--$7.44$) despite order-of-magnitude differences.
16	Figure~\ref{fig:heatmap} provides a visual summary.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds). Single-seed conditions: percentile bootstrap 95\% CI (10,000 resamples) reflecting clean-seed variability. Qwen MMLU 15\%/25\%/50\%: multi-seed mean $\pm$ SD ($n{=}3$ independent contamination runs). All exclude zero.}
21	\label{tab:cohens_d}
22	\footnotesize
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}llrrrr@{}}
25	\toprule
26	Model & Bench. & $
…[truncated 12642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T04:18:15.331479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T04:18:15.331646+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip).
14	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset; we use these external parameters rather than re-estimating from potentially contaminated data, since our MML-EM refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data.
15	
16	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
17	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}; \citet{magis2012} provide a detailed treatment of how response model selection and ability estimation affect $\ell_z^*$.
18	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
19	
20	\subsection{$\Delta\ell_z^*$ Matched-Difference Design}
21	\label{sec:did}
22	
23	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
24	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, renderi
…[truncated 4353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T04:18:15.331792+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T04:18:15.331993+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	Our findings reveal both the strengths and boundaries of IRT person-fit for contamination detection: $\ell_z^*$ reliably detects SFT-stage contamination across model families, but three boundary conditions constrain its practical utility.
4	
5	\paragraph{Characterization over tool.}
6	The detection-diagnosis tradeoff (\S\ref{sec:degradation}) shows that simpler statistics detect contamination more powerfully than $\ell_z^*$: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger, and HT generally exceeds $\ell_z^*$.
7	The value of the IRT framework lies not in detection power but in mechanistic understanding: the $\theta$-shift analysis reveals \emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance.
8	These diagnostic capabilities are invisible to accuracy $z$-scores or HT.
9	Findings~1--2 are theoretically predictable from IRT principles; our contribution lies in quantifying these effects in the LLM setting, where the magnitude and boundary conditions are not derivable from theory alone.
10	
11	\paragraph{Practical implications.}
12	Two results have immediate consequences.
13	Free-$\theta$ estimation produces seed-dependent dose-response curves (CV up to 60\%); anchoring $\theta$ to a pre-contamination baseline stabilizes detection and amplifies the signal for models with substantial $\theta$-shift ($\Delta\theta > 0.2$).
14	The benchmark size boundary means $\ell_z^*$ is most informative for large benchmarks ($n > 7{,}000$ items for 80\% power at 15\% contamination); on small benchmarks like ARC-C (295 items), detection relies on concentrated contamination effects.
15	
16	\paragraph{Scope and calibration.}
17	Universal baseline misfit (57/60 cells flagged) confirms systemat
…[truncated 1257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T04:18:15.332160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T04:18:15.332287+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We characterized IRT person-fit statistics for LLM contamination detection across three 7--8B model families, establishing reliable SFT-stage detection while identifying boundary conditions: $\theta$-shift absorption necessitating $\theta$-anchored estimation for high-ability models, a detection-diagnosis tradeoff, and non-monotonic dose-response as a $\theta$-estimation artifact.
4	Future work should address pretraining-stage signatures and broader model scales.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T04:18:15.332514+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/arr_submission_form_draft.md",
  "content": "# ARR Submission Form Draft\n\n## Basic Information\n- **Title**: What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?\n- **Abstract**: Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities. We present the first controlled characterization of IRT person-fit statistics for detecting SFT-stage contamination: the framework requires only binary response patterns from the target model---no access to weights, gradients, logits, or training data---combined with externally calibrated 4PL item parameters from a large-scale item bank; diagnostic θ-anchoring additionally requires a clean baseline. A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge. Using ℓ_z* in a matched-difference design (Δℓ_z*) across three 7--8B model families (n=10 clean baseline seeds per model family) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify three behavior boundaries: (1) model-specific θ-shift dynamics, where contamination-induced ability inflation absorbs the person-fit signal; θ-anchoring is necessary for reliable detection of high-ability models at high contamination (2.4× amplification, inter-seed CV reduced from 60% to 19%); (2) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack ℓ_z*'s diagnostic capabilities (seen/unseen decomposition, mechanistic θ-shift analysis); and (3, exploratory) ability-dependent non-monotonic dose-response under free-θ estimation, driven by θ-shift absorption; θ-anchored analysis reveals stable detection with a strong positive dose-response at higher contamination levels. These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy.\n- **Authors**: Anonymous\n- **Track**: Long Paper\n- **Submission Type**: ARR (Rolling Review)\n\n---\n\n## Responsible NLP Research Checklist\n\n### A. For Every Submission\n\n**A1. Did you describe the limitations of your work?**\n→ **Yes** — Dedicated Limitations section covers three points: (1) generalization beyond 7-8B / QLoRA / SFT-stage untested, (2) high seed dependence at 50% contamination (CV=60%), partially resolved by θ-anchoring; post-RL is N=1, (3) dependence on PSN-IRT calibration and no head-to-head comparison with logit-based methods.\n\n**A2. Did you discuss any potential risks of your work?**\n→ **Yes** — The method detects contamination (defensive/auditing use). Potential dual-use risk (adversaries calibrating contamination to evade detection) is implicit in the dose-response analysis; however, the method's core contribution is enabling retrospective audits, which is net-positive for evaluation integrity.\n\n**A3. Do the authors provide complete proofs of all claims and statements?**\n→ **Yes** — All empirical claims are supported by tables with bootstrap 95% CIs, Cohen's d effect sizes, and multi-seed replication. Simulation validation (Appendix A) confirms ℓ_z* calibration under the null. Robustness analyses cover local dependence (Appendix E) and parameter noise sensitivity (Appendix F).\n\n**A4. Do the authors provide adequate citations and describe differences relative to existing work?**\n→ **Yes** — Related Work section covers IRT-based LLM evaluation, contamination detection methods (MIA, ConStat), and person-fit statistics literature. Discussion positions the method in an information-requirements hierarchy relative to logit-based and multi-benchmark methods.\n\n**A5. Does the paper include computational experiments?**\n→ **Yes** — Controlled contamination experiments across 3 model families × multiple contamination levels, with n=10 clean seeds and n=3 contamination seeds for Qwen. Simulation studies with 2,000 replicates per cell.\n\n**A6. Does the paper include theoretical contributions?**\n→ **N-A** — The paper is primarily empirical. It applies existing IRT theory (ℓ_z* statistic, 4PL model) to a new domain (LLM contamination) and provides empirical characterization rather than new theoretical results.\n\n### B. Did You Use Human Subjects or Human Data?\n\n**B1. Does the paper describe potential risks to study participants?**\n→ **N-A** — No human subjects involved. All data are LLM benchmark response patterns (MMLU, ARC-Challenge) and model outputs.\n\n**B2. Did you include the full text of instructions given to human participants?**\n→ **N-A** — No human participants.\n\n**B3. Did you describe potential participant risks and IRB approvals?**\n→ **N-A** — No human participants; no IRB required.\n\n**B4. Did you include estimated hourly wage and total compensation?**\n→ **N-A** — No human annotators or crowdworkers.\n\n**B5. Did you include demographic information of participants?**\n→ **N-A** — No human participants.\n\n**B6. Did you discuss ethical aspects of data collection?**\n→ **N-A** — Data consists of publicly available LLM benchmarks (MMLU, ARC-Challenge) and model outputs from controlled experiments. No personally identifiable information.\n\n### C. Computational Experiments\n\n**C1. Did you report the number of parameters, total computational budget, and computing infrastructure?**\n→ **Yes** — Three 7-8B parameter model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3). Training uses QLoRA (4-bit NF4) on single A100/4090 GPUs. Exact GPU-hour budget is not itemized but infrastructure is specified.\n\n**C2. Did you discuss the experimental setup, including hyperparameters?**\n→ **Yes** — Full QLoRA hyperparameter table in Appendix (Table 10): rank=16, α=32, dropout=0.05, lr=2e-4, AdamW, 3 epochs, effective batch size=16, max seq length=512. Target modules specified.\n\n**C3. Did you report descriptive statistics (error bars, summary statistics)?**\n→ **Yes** — Bootstrap 95% CIs (10,000 resamples, percentile method) for all Cohen's d estimates. Multi-seed means ± SD for Qwen (n=3 contamination seeds). BCa sensitivity check in Appendix confirms conservative coverage.\n\n**C4. If you used existing packages, did you report versions?**\n→ **No** — Model family names and versions are reported (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3). PSN-IRT item bank is cited. Software package versions (PyTorch, Transformers, PEFT) are not explicitly listed. *Consider adding a software versions footnote.*\n\n**C5. Did you report the seeds and number of runs?**\n→ **Yes** — n=10 clean baseline seeds per model family (seeds 0-9). n=3 independent contamination QLoRA runs for Qwen (seeds 42, 123, 456). Simulation studies use 2,000 replicates per cell (power analysis) and 1,000 replicates (robustness). All reported in Methods and Appendix.\n\n### D. Did You Use NLP Datasets?\n\n**D1. Did you include a link to the dataset(s)?**\n→ **Yes** — MMLU (Hendrycks et al., 2021) and ARC-Challenge (Clark et al., 2018) are cited with original references. PSN-IRT item bank is cited (psnirt2026).\n\n**D2. Did you describe the datasets and preprocessing steps?**\n→ **Yes** — MMLU (14,042 items) and ARC-Challenge (295 items) described in Section 3.3 (Experimental Setup). Contamination protocol (X% benchmark items mixed into SFT data with gold answers in standard evaluation format) is detailed.\n\n**D3. Did you discuss the license of the datasets?**\n→ **No** — MMLU and ARC-Challenge licenses are not explicitly discussed. Both are widely used public benchmarks. *Consider adding a brief license note.*\n\n**D4. Did you report statistics about the datasets?**\n→ **Yes** — Item counts reported: MMLU (14,042 items), ARC-Challenge (295 items). Item parameter distributions from PSN-IRT discussed (e.g., 46% of MMLU items have upper asymptote d < 0.95).\n\n**D5. Did you include the full details of train/validation/test splits?**\n→ **Yes** — Contamination conditions specify exact mixing ratios (5%, 15%, 25%, 50% of training data are benchmark items). Clean vs. contaminated splits are fully described. Evaluation uses the full benchmark test sets.\n\n---\n\n## Additional Notes\n\n- **Reproducibility Statement**: Included in paper — code and response data released upon acceptance; bootstrap parameters, seed counts, and item bank source specified.\n- **Ethics Statement**: Not separately included (not required by ARR); the work is methodological (contamination detection for evaluation integrity) with no human subjects.\n- **Supplementary Materials**: Appendix includes simulation validation, 4PL vs. 3PL ablation, seed sensitivity, robustness analyses (local dependence, parameter noise), BCa check, MML-EM refit, post-RL pilot, and full hyperparameters.\n\n### Items to Address Before Submission\n1. **C4**: Add software/library versions (PyTorch, Transformers, PEFT, bitsandbytes) as a footnote or in Appendix.\n2. **D3**: Add brief dataset license note for MMLU and ARC-Challenge.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/arr_submission_form_draft.md",
    "content": "# ARR Submission Form Draft\n\n## Basic Information\n- **Title**: What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?\n- **Abstract**: Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities. We present the first controlled characterization of IRT person-fit statistics for detecting SFT-stage contamination: the framework requires only binary response patterns from the target model---no access to weights, gradients, logits, or training data---combined with externally calibrated 4PL item parameters from a large-scale item bank; diagnostic θ-anchoring additionally requires a clean baseline. A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge. Using ℓ_z* in a matched-difference design (Δℓ_z*) across three 7--8B model families (n=10 clean baseline seeds per model family) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify three behavior boundaries: (1) model-specific θ-shift dynamics, where contamination-induced ability inflation absorbs the person-fit signal; θ-anchoring is necessary for reliable detection of high-ability models at high contamination (2.4× amplification, inter-seed CV reduced from 60% to 19%); (2) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack ℓ_z*'s diagnostic capabilities (seen/unseen decomposition, mechanistic θ-shift analysis); and (3, exploratory) ability-dependent non-monotonic dose-response under free-θ estimation, driven by θ-shift absorption; θ-anchored analysis reveals stable detection with a strong positive dose-response at higher contamination levels. These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy.\n- **Authors**: Anonymous\n- **Track**: Long Paper\n- **Submission Type**: ARR (Rolling Review)\n\n---\n\n## Responsible NLP Research Checklist\n\n### A. For Every Submission\n\n**A1. Did you describe the limitations of your work?**\n→ **Yes** — Dedicated Limitations section covers three points: (1) generalization beyond 7-8B / QLoRA / SFT-stage untested, (2) high seed dependence at 50% contamination (CV=60%), partially resolved by θ-anchoring; post-RL is N=1, (3) dependence on PSN-IRT calibration and no head-to-head comparison with logit-based methods.\n\n**A2. Did you discuss any potential risks of your work?**\n→ **Yes** — The method detects contamination (defensive/auditing use). Potential dual-use risk (adversaries calibrating contamination to evade detection) is implicit in the dose-response analysis; however, the method's core contribution is enabling retrospective audits, which is net-positive for evaluation integrity.\n\n**A3. Do the authors provide complete proofs of all claims and statements?**\n→ **Yes** — All empirical claims are supported by tables with bootstrap 95% CIs, Cohen's d effect sizes, and multi-seed replication. Simulation validation (Appendix A) confirms ℓ_z* calibration under the null. Robustness analyses cover local dependence (Appendix E) and parameter noise sensitivity (Appendix F).\n\n**A4. Do the authors provide adequate citations and describe differences relative to existing work?**\n→ **Yes** — Related Work section covers IRT-based LLM evaluation, contamination detection methods (MIA, ConStat), and person-fit statistics literature. Discussion positions the method in an information-requirements hierarchy relative to logit-based and multi-benchmark methods.\n\n**A5. Does the paper include computational experiments?**\n→ **Yes** — Controlled contamination experiments across 3 model families × multiple contamination levels, with n=10 clean seeds and n=3 contamination seeds for Qwen. Simulation studies with 2,000 replicates per cell.\n\n**A6. Does the paper include theoretical contributions?**\n→ **N-A** — The paper is primarily empirical. It applies existing IRT theory (ℓ_z* statistic, 4PL model) to a new domain (LLM contamination) and provides empirical characterization rather than new theoretical results.\n\n### B. Did You Use Human Subjects or Human Data?\n\n**B1. Does the paper describe potential risks to study participants?**\n→ **N-A** — No human subjects involved. All data are LLM benchmark response patterns (MMLU, ARC-Challenge) and model outputs.\n\n**B2. Did you include the full text of instructions given to human participants?**\n→ **N-A** — No human participants.\n\n**B3. Did you describe potential participant risks and IRB approvals?**\n→ **N-A** — No human participants; no IRB required.\n\n**B4. Did you include estimated hourly wage and total compensation?**\n→ **N-A** — No human annotators or crowdworkers.\n\n**B5. Did you include demographic information of participants?**\n→ **N-A** — No human participants.\n\n**B6. Did you discuss ethical aspects of data collection?**\n→ **N-A** — Data consists of publicly available LLM benchmarks (MMLU, ARC-Challenge) and model outputs from controlled experiments. No personally identifiable information.\n\n### C. Computational Experiments\n\n**C1. Did you report the number of parameters, total computational budget, and computing infrastructure?**\n→ **Yes** — Three 7-8B parameter model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3). Training uses QLoRA (4-bit NF4) on single A100/4090 GPUs. Exact GPU-hour budget is not itemized but infrastructure is specified.\n\n**C2. Did you discuss the experimental setup, including hyperparameters?**\n→ **Yes** — Full QLoRA hyperparameter table in Appendix (Table 10): rank=16, α=32, dropout=0.05, lr=2e-4, AdamW, 3 epochs, effective batch size=16, max seq length=512. Target modules specified.\n\n**C3. Did you report descriptive statistics (error bars, summary statistics)?**\n→ **Yes** — Bootstrap 95% CIs (10,000 resamples, percentile method) for all Cohen's d estimates. Multi-seed means ± SD for Qwen (n=3 contamination seeds). BCa sensitivity check in Appendix confirms conservative coverage.\n\n**C4. If you used existing packages, did you report versions?**\n→ **No** — Model family names and versions are reported (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3). PSN-IRT item bank is cited. Software package versions (PyTorch, Transformers, PEFT) are not explicitly listed. *Consider adding a software versions footnote.*\n\n**C5. Did you report the seeds and number of runs?**\n→ **Yes** — n=10 clean baseline seeds per model family (seeds 0-9). n=3 independent contamination QLoRA runs for Qwen (seeds 42, 123, 456). Simulation studies use 2,000 replicates per cell (power analysis) and 1,000 replicates (robustness). All reported in Methods and Appendix.\n\n### D. Did You Use NLP Datasets?\n\n**D1. Did you include a link to the dataset(s)?**\n→ **Yes** — MMLU (Hendrycks et al., 2021) and ARC-Challenge (Clark et al., 2018) are cited with original references. PSN-IRT item bank is cited (psnirt2026).\n\n**D2. Did you describe the datasets and preprocessing steps?**\n→ **Yes** — MMLU (14,042 items) and ARC-Challenge (295 items) described in Section 3.3 (Experimental Setup). Contamination protocol (X% benchmark items mixed into SFT data with gold answers in standard evaluation format) is detailed.\n\n**D3. Did you discuss the license of the datasets?**\n→ **No** — MMLU and ARC-Challenge licenses are not explicitly discussed. Both are widely used public benchmarks. *Consider adding a brief license note.*\n\n**D4. Did you report statistics about the datasets?**\n→ **Yes** — Item counts reported: MMLU (14,042 items), ARC-Challenge (295 items). Item parameter distributions from PSN-IRT discussed (e.g., 46% of MMLU items have upper asymptote d < 0.95).\n\n**D5. Did you include the full details of train/validation/test splits?**\n→ **Yes** — Contamination conditions specify exact mixing ratios (5%, 15%, 25%, 50% of training data are benchmark items). Clean vs. contaminated splits are fully described. Evaluation uses the full benchmark test sets.\n\n---\n\n## Additional Notes\n\n- **Reproducibility Statement**: Included in paper — code and response data released upon acceptance; bootstrap parameters, seed counts, and item bank source specified.\n- **Ethics Statement**: Not separately included (not required by ARR); the work is methodological (contamination detection for evaluation integrity) with no human subjects.\n- **Supplementary Materials**: Appendix includes simulation validation, 4PL vs. 3PL ablation, seed sensitivity, robustness analyses (local dependence, parameter noise), BCa check, MML-EM refit, post-RL pilot, and full hyperparameters.\n\n### Items to Address Before Submission\n1. **C4**: Add software/library versions (PyTorch, Transformers, PEFT, bitsandbytes) as a footnote or in Appendix.\n2. **D3**: Add brief dataset license note for MMLU and ARC-Challenge.\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T04:18:15.332756+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/arr_submission_form_draft.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T04:18:15.332887+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T04:18:15.333010+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T04:18:15.333140+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T04:18:15.333259+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T04:18:15.333391+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T04:18:15.333504+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_arr-submission-form_20260523T041551",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-23T04:18:15.333662+00:00_

`register_artifact` 工具不可用，文件已写入：

`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/arr_submission_form_draft.md`

草稿包含：
- **Basic Information**：从 main.tex 提取的 title 和 abstract
- **Responsible NLP Checklist (A-D)**：共 22 项，逐项基于论文内容给出 Yes/No/N-A + justification（引用具体章节）
- **提交前待处理**：标注了两个需补充的项——C4（软件版本号）和 D3（数据集 license）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_arr-submission-form_20260523T041551"
}
```

</details>

---
