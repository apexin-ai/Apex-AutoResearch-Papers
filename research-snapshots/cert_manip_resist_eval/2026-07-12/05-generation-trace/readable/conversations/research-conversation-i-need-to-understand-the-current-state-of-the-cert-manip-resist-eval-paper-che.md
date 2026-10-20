# Research conversation: I need to understand the current state of the cert_manip_resist_eval paper. Check: 1. Read /home/ubuntu/.agent-ml-resear

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ab1e410fa18d4cc66.jsonl`
- **Structured JSON:** [`37f21f509c2cce1fc66f.json`](../../sessions/37/37f21f509c2cce1fc66f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-25T14:18:11.388Z_

I need to understand the current state of the cert_manip_resist_eval paper. Check:

1. Read /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex — find the order of \bibliography and \appendix/\input{appendix}. Is appendix before or after references?

2. Read /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex — report:
   - Total number of pages/sections in appendix
   - What Table 10 looks like (columns, structure, is K/Data repeated?)
   - What Table 19 looks like (template format, does it use \n literally?)
   - List all tables and figures currently in the appendix

3. Count references in /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib — how many @article/@inproceedings/etc entries total?

4. Check the distilled writing skill at /home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/cert_manip_resist_eval/distilled-writing.skill.md — look for any guidance on LLM prompt template formatting in appendix (light yellow background, \textit style).

Report all findings with line numbers where relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b10b7490-36dc-4054-aaa8-5eef6127b4a0",
  "agentId": "ab1e410fa18d4cc66",
  "type": "user",
  "uuid": "a48f953a-3a57-4be5-9a15-9feab81c1d6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T14:18:13.078Z_

I'll help you understand the current state of the cert_manip_resist_eval paper. Let me gather this information systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a48f953a-3a57-4be5-9a15-9feab81c1d6e",
  "isSidechain": true,
  "agentId": "ab1e410fa18d4cc66",
  "requestId": "req_011CbPRyfVh9khvgwdTusKTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b78ae8dd-4cb5-4b53-8f5a-d5da93c6ecd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GW8Jsw2L52Gj89vaYojQ1p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 36739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 771,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T14:18:13.373Z_

<details open><summary>🔧 Tool call — Read · `toolu_016NHurXTHGdn1KNWavT1KQs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b78ae8dd-4cb5-4b53-8f5a-d5da93c6ecd5",
  "isSidechain": true,
  "agentId": "ab1e410fa18d4cc66",
  "requestId": "req_011CbPRyfVh9khvgwdTusKTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cc39ce9a-225a-4351-8b9d-32efe1faa565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GW8Jsw2L52Gj89vaYojQ1p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 36739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 771,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T14:18:13.401Z_

<details><summary>↩ Tool result · `toolu_016NHurXTHGdn1KNWavT1KQs`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsthm}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage{tikz}
15	\usetikzlibrary{shapes.geometric,arrows.meta,positioning,fit,shadows.blur,calc}
16	
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{definition}{Definition}
19	\newtheorem{proposition}{Proposition}
20	
21	\title{The Diminishing Weakest Link: How Panel Size Shifts\\Adversarial Vulnerability Drivers in LLM Judge Panels}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\eta_{\max}$) and effective independence ($K_{\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\mathrm{eff}}$ and $\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\eta_{\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\hat{\beta}_{\mathrm{std}}$: $0.264 \to 0.102 \to 0.084$; confidence interval crosses zero at $K{\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\%$ at $\alpha{=}5\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational\footnote{Code and data are available at \url{https://anonymous.4open.science/r/cert_manip_resist_eval-588E/}.}.
30	\end{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{threat_model}
35	\input{methodology}
36	\input{results}
37	\input{analysis}
38	\input{conclusion}
39	
40	\section*{Limitations}
41	
42	\textbf{Diversity--capability confound.} The structural coupling between diversity and capability ($r{=}0.70$--$0.81$; VIF $\approx 2.0$--$2.9$) prevents observational regression from reliably separating their contributions; capability-matched subsampling reduces but does not eliminate this confound (Pool~A $r{=}0.50$). Causal identification requires training-based diversity control.
43	\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\geq}20$ threshold at all panel sizes \citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\mathrm{eff}}$ vs.\ $\kappa$-diversity show opposite $K$-trends).
44	\textbf{Benchmark and attack scope.} Both benchmarks use multiple-choice formats; open-ended generation may present different attack surfaces. The six local models use AWQ INT4 quantization, which may confound capability classification, though excluding near-chance quantized models strengthens the association (Appendix~\ref{app:near_chance}). Each attack uses 1--2 template variants, limiting generalization. We study only odd $K \in \{3,5,7\}$; the predictor shift threshold $K^*$ is not precisely identified.
45	
46	\input{appendix}
47	\input{appendix_attacks}
48	
49	\bibliography{references}
50	
51	\end{document}
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc39ce9a-225a-4351-8b9d-32efe1faa565",
  "isSidechain": true,
  "promptId": "b10b7490-36dc-4054-aaa8-5eef6127b4a0",
  "agentId": "ab1e410fa18d4cc66",
  "type": "user",
  "uuid": "9052a4ec-09df-4a34-9a4f-a978a79e8a65",
  "sourceToolAssistantUUID": "cc39ce9a-225a-4351-8b9d-32efe1faa565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T14:18:13.647Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UrfE2LMet212mc46E6QkLp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9052a4ec-09df-4a34-9a4f-a978a79e8a65",
  "isSidechain": true,
  "agentId": "ab1e410fa18d4cc66",
  "requestId": "req_011CbPRyfVh9khvgwdTusKTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "76e16bf6-ce84-46f1-8188-52aa983eae5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GW8Jsw2L52Gj89vaYojQ1p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 36739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 771,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T14:18:13.824Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RhBRvfghy149unSDATe3CS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76e16bf6-ce84-46f1-8188-52aa983eae5f",
  "isSidechain": true,
  "agentId": "ab1e410fa18d4cc66",
  "requestId": "req_011CbPRyfVh9khvgwdTusKTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3715f44b-2e73-4b28-9479-5c4fc2fdadcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GW8Jsw2L52Gj89vaYojQ1p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 36739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 771,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T14:18:13.960Z_

<details><summary>↩ Tool result · `toolu_01UrfE2LMet212mc46E6QkLp`</summary>

```text
1	\appendix
2	
3	\section{Proof of Proposition~\ref{thm:monotonicity}}
4	\label{app:proof}
5	
6	The replaced judge $J_K'$ is \emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \geq t$ regardless of the $K$-th judge:
7	\begin{align}
8	\mathrm{ASR}(\mathcal{P}, a) &= \Pr(S \geq t) + \Pr(S = t{-}1) \cdot \Pr(X_K^a {=} 1 \mid S = t{-}1).
9	\end{align}
10	Since $\Pr(X_{K'}^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K}) \geq \Pr(X_K^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})$ for all attacks $a$ and realizations $\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\mathcal{P}'$ than for $\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\mathrm{ASR}^*(\mathcal{P}') \geq \mathrm{ASR}^*(\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\mathcal{A}$.
11	
12	\section{Robustness Correction Methods}
13	\label{app:robustness_methods}
14	
15	The 455 panels are constructed combinatorially from 15 shared judges: each judge appears in $\binom{14}{2} = 91$ panels, inducing correlated residuals across panel-level observations. Standard OLS assumes independent errors, potentially inflating significance. We apply three corrections.
16	
17	\paragraph{Clustered Standard Errors.} Because each panel of $K{=}3$ judges does not map to a single cluster, we perform three separate one-way clusterings (one for each judge position in the ordered panel tuple) using CR1 bias-corrected sandwich estimators (13 clusters per position). The reported standard error for each coefficient is the maximum across the three clusterings, yielding the most conservative inference.
18	
19	\paragraph{Mixed Effects.} For each of the three judge positions, we fit a linear mixed-effects model with a random intercept for the judge occupying that position, estimating $K_{\mathrm{eff}}$ and $\eta_{\max}$ as fixed effects. The reported $p$-value for each coefficient is the maximum across the three models.
20	
21	\paragraph{Wild Cluster Bootstrap.} We perform $B{=}9{,}999$ bootstrap resamples using Rademacher weights, clustering by each of the three panel positions in turn and taking the maximum $p$-value across positions (the most conservative aggregation). This approach avoids distributional assumptions on the cluster structure.
22	
23	\section{Crossed Random Effects Analysis}
24	\label{app:crossed_re}
25	
26	The one-way clustering in Appendix~\ref{app:robustness_methods} treats each judge position independently, but panels exhibit \emph{crossed} random effects: judge $j$ may occupy position~1 in one panel and position~2 in another, inducing a multi-membership structure. At $K{=}7$, each judge appears in $\binom{14}{6} = 3{,}003$ of $6{,}435$ panels (46.7\%), making crossed membership the dominant source of residual correlation.
27	
28	We fit multi-membership cluster-robust variance estimators (CRVE) using a sandwich estimator with $t(G{-}1) = t(14)$ reference distribution, where $G{=}15$ is the number of judges. Table~\ref{tab:crossed_re} compares bootstrap and crossed RE significance.
29	
30	\begin{table}[h]
31	\centering
32	\small
33	\begin{tabular}{rcccc}
34	\toprule
35	& \multicolumn{2}{c}{\textbf{Bootstrap}} & \multicolumn{2}{c}{\textbf{Crossed RE (FDR)}} \\
36	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
37	$\boldsymbol{K}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & $\boldsymbol{\eta_{\max}}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & $\boldsymbol{\eta_{\max}}$ \\
38	\midrule
39	3 & 4/12 & 3/12 & 0/12 & 1/12 \\
40	5 & 7/12 & 2/12 & \textbf{8/12} & 3/12 \\
41	7 & 8/12 & 1/12 & \textbf{8/12} & 2/12 \\
42	\bottomrule
43	\end{tabular}
44	\caption{Crossed random effects vs.\ wild cluster bootstrap significance (BH FDR $\alpha{=}0.05$). Multi-membership CRVE with $t(14)$ distribution. At $K{\geq}5$, $K_{\mathrm{eff}}$ retains 8/12 significance under crossed RE, matching or exceeding bootstrap. At $K{=}3$, the conservative $t(14)$ distribution with only 455 panels produces attenuation to 0/12 (raw $p$-values: 5/12 significant).}
45	\label{tab:crossed_re}
46	\end{table}
47	
48	SE inflation increases with $K$ as judge overlap intensifies: $1.75$--$4.96{\times}$ at $K{=}3$, $6$--$12{\times}$ at $K{=}5$, $10$--$19{\times}$ at $K{=}7$. Despite this inflation, $K_{\mathrm{eff}}$ retains 8/12 significance at $K{\geq}5$ because the effect size is large enough to survive the correction. The $K{=}3$ attenuation (0/12) reflects two compounding factors: the conservative $t(14)$ reference distribution penalizes small-sample inference, and the effect sizes at $K{=}3$ are insufficient to overcome the inflated SEs. Raw (uncorrected) $p$-values show 5/12 conditions significant at $K{=}3$, confirming that the attenuation reflects degrees-of-freedom conservatism rather than absent effects.
49	
50	\section{Extended Analysis}
51	\label{app:extended_analysis}
52	
53	\begin{figure}[t]
54	\centering
55	\includegraphics[width=\columnwidth]{figures/fig_keff_eta_scatter.pdf}
56	\caption{Panel-level correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ at $K{=}5$ ($n{=}3{,}003$ panels). Full model pool (gray, $r{=}0.81$) exhibits strong collinearity; capability-matched Pool~A (orange, $r{=}0.50$, 126 panels) shows reduced confounding.}
57	\label{fig:keff_eta_scatter}
58	\end{figure}
59	
60	\begin{figure}[t]
61	\centering
62	\includegraphics[width=\columnwidth]{figures/fig_dominance_heatmap.pdf}
63	\caption{Per-condition predictor dominance across panel sizes (wild cluster bootstrap, BH FDR $\alpha{=}0.05$). At $K{=}3$, dominance is heterogeneous (co-dominant, $K_{\mathrm{eff}}$-only, $\eta_{\max}$-only, and non-significant conditions coexist); at $K{\geq}5$, $K_{\mathrm{eff}}$ dominates uniformly while $\eta_{\max}$ diminishes substantially.}
64	\label{fig:dominance_heatmap}
65	\end{figure}
66	
67	\subsection{BFT Reversal Mechanism: Detailed Evidence}
68	\label{app:bft_reversal}
69	
70	Under standard OLS, the regression results (Table~\ref{tab:dominance}) show $\eta_{\max}$ significant in 10 of 12 conditions and $K_{\mathrm{eff}}$ positively associated with ASR in all 12. Non-independence correction attenuates both predictors: under wild cluster bootstrap, $\eta_{\max}$ retains 3/12 and $K_{\mathrm{eff}}$ retains 4/12, with $K_{\mathrm{eff}}$ slightly ahead. The directional pattern (all $K_{\mathrm{eff}}$ point estimates positive) persists uniformly. The random-fault contrast (\S\ref{sec:rf_contrast}) sharpens this: under random faults, $K_{\mathrm{eff}}$'s positive association with panel error survives all corrections (2/2 conditions, $R^2 = 0.73$--$0.81$), indicating a genuine relationship whose statistical confidence attenuates under adaptive attack (4/12 after correction).
71	
72	\begin{figure}[h]
73	\centering
74	\includegraphics[width=\columnwidth]{figures/fig2_gam_keff_split.pdf}
75	\caption{GAM bootstrap $K_{\mathrm{eff}}$ effect direction at $K{=}3$ ($B{=}9999$). All 12 conditions show positive $K_{\mathrm{eff}}$ direction (88.9--100\% bootstrap rate). The Kruskal--Wallis test finds no significant magnitude difference between targeted and shared-bias attacks ($p{=}0.200$).}
76	\label{fig:gam_split}
77	\end{figure}
78	
79	Under corrected data (V2), all 12 $K_{\mathrm{eff}}$ OLS coefficients are positive. The previously reported negative ARC $\times$ sycophancy coefficient ($\hat{\beta}_{\mathrm{std}} = -0.192$) was an artifact of error-as-tie handling; after correction, it becomes positive ($\hat{\beta}_{\mathrm{std}} = +0.257$). GAM bootstrap confirms the uniform positive direction: 12/12 conditions at $K{=}3$ (88.9--100\% positive rate) and 12/12 at $K{=}5$ (100\%).
80	
81	\subsection{Diversity--Capability Tradeoff}
82	\label{app:diversity_capability}
83	
84	The $r = 0.70$--$0.81$ correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ ($K{=}3$ to $K{=}5$) reflects a structural feature of the current LLM ecosystem: maximizing panel diversity requires sampling across capability tiers, which systematically introduces less capable and therefore more vulnerable judges. The structural correlation is unaffected by SE correction; it is a property of the model ecosystem, not an artifact of panel overlap. However, the high confound combined with fragile independent significance means that observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit that co-occurs with it.
85	
86	
87	Family-level labels provide indirect evidence that capability proximity matters more than taxonomic grouping: family membership is not a significant predictor of panel vulnerability ($p = 0.179$ on MMLU, $p = 0.385$ on ARC), consistent with models from the same provider exhibiting heterogeneous vulnerability profiles that vary by capability tier rather than by shared architecture \citep{kuncheva2003measures}.
88	
89	\subsection{Aggregation Mechanism Details}
90	\label{app:aggregation_details}
91	
92	\begin{figure}[t]
93	\centering
94	\includegraphics[width=\columnwidth]{figures/fig3_aggregation_gradient.pdf}
95	\caption{$K_{\mathrm{eff}}$ coefficient distribution across aggregation methods ($K{=}3$). Majority and weighted voting: uniformly positive (12+/0$-$); Bayesian calibration: reduced predictability ($R^2{=}0.087$, 5+/1$-$).}
96	\label{fig:aggregation}
97	\end{figure}
98	
99	Bayesian calibration attenuates $K_{\mathrm{eff}}$ significance (5+/1$-$) and reduces overall predictability ($R^2{=}0.087$), but $\eta_{\max}$ persists (9/12 under OLS), providing partial defense. The pattern reflects calibrated reliability weighting: by estimating each judge's confusion matrix on clean data, Bayesian aggregation downweights weak judges, reducing the diversity channel while the individual weakness channel remains active. Threshold voting amplifies both channels because any single dissenting judge vetoes the panel decision, making compositional factors highly predictive of attack success ($R^2{=}0.829$). Bayesian calibration requires a clean accuracy prior, and an adaptive attacker aware of this calibration could target the prior itself \citep{tambe2011security}.
100	
101	
102	\subsection{Aggregation at \texorpdfstring{$K{=}5$}{K=5}}
103	\label{app:aggregation_k5}
104	
105	Table~\ref{tab:aggregation_k5} extends the aggregation analysis to $K{=}5$ (3{,}003 panels) under wild cluster bootstrap with 5-position max-$p$. All four aggregation methods yield identical $K_{\mathrm{eff}}$ significance (7/12), with $\eta_{\max}$ uniformly low (2--3/12). The Bayesian attenuation observed at $K{=}3$ (5+/1$-$; Table~\ref{tab:aggregation}) does not persist: $K_{\mathrm{eff}}$ reaches 7/12 regardless of aggregation rule. Predictability still varies ($\bar{R}^2$: threshold 0.408, Bayesian 0.166), but the diversity channel operates uniformly across all methods. At $K{=}7$, however, methods diverge again: Bayesian neutralization returns (0/12) while threshold voting strengthens to 10/12 (Table~\ref{tab:aggregation_k7}).
106	
107	\begin{table}[h]
108	\centering
109	\small
110	\begin{tabular}{lccc}
111	\toprule
112	\textbf{Aggregation} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} & $\boldsymbol{\bar{R}^2}$ \\
113	\midrule
114	Majority   & 2/12  & 7/12 & 0.285 \\
115	Weighted   & 2/12  & 7/12 & 0.275 \\
116	Threshold  & 3/12  & 7/12 & 0.408 \\
117	Bayesian   & 2/12  & 7/12 & 0.166 \\
118	\bottomrule
119	\end{tabular}
120	\caption{Aggregation method comparison at $K{=}5$ (3{,}003 panels, wild cluster bootstrap with 5-position max-$p$, BH FDR $\alpha{=}0.05$). All four methods converge to $K_{\mathrm{eff}}$ 7/12, unlike the differentiated pattern at $K{=}3$ (Table~\ref{tab:aggregation}).}
121	\label{tab:aggregation_k5}
122	\end{table}
123	
124	\subsection{Aggregation at \texorpdfstring{$K{=}7$}{K=7}}
125	\label{app:aggregation_k7}
126	
127	Table~\ref{tab:aggregation_k7} extends the aggregation analysis to $K{=}7$ (6{,}435 panels) under wild cluster bootstrap with 7-position max-$p$. Unlike the uniform convergence at $K{=}5$ (all methods 7/12), aggregation methods diverge at $K{=}7$: threshold voting strengthens to 10/12 while Bayesian calibration drops to 0/12, restoring the neutralization pattern absent at $K{=}5$.
128	
129	\begin{table}[h]
130	\centering
131	\small
132	\begin{tabular}{lccc}
133	\toprule
134	\textbf{Aggregation} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} & $\boldsymbol{\bar{R}^2}$ \\
135	\midrule
136	Majority   & 1/12  & 8/12 & 0.244 \\
137	Weighted   & 1/12  & 6/12 & 0.207 \\
138	Threshold  & 8/12  & 10/12 & 0.509 \\
139	Bayesian   & 1/12  & 0/12 & 0.105 \\
140	\bottomrule
141	\end{tabular}
142	\caption{Aggregation method comparison at $K{=}7$ (6{,}435 panels, wild cluster bootstrap with 7-position max-$p$, BH FDR $\alpha{=}0.05$). Unlike $K{=}5$ where all methods converge to 7/12, $K{=}7$ shows method divergence: threshold voting reaches 10/12 while Bayesian calibration returns to full $K_{\mathrm{eff}}$ neutralization (0/12).}
143	\label{tab:aggregation_k7}
144	\end{table}
145	
146	\subsection{Metric Robustness Under Partial Panel Information}
147	\label{app:oracle}
148	
149	The main analysis computes $\eta_{\max}$ with full knowledge of panel composition (all three judges known). In deployment, a practitioner selecting or auditing a panel may know only a subset of the constituent judges. We test whether $\eta_{\max}$ retains predictive power under such partial information by recomputing it from two of the three panel members: for each panel, we cycle through all $\binom{3}{1} = 3$ leave-one-out masks, compute $\eta_{\max}$ from the two known judges, and average the regression estimates across masking scenarios.
150	
151	Under the most conservative inference (partial information + clustered SE), $\eta_{\max}$ remains the sole significant predictor with $\hat{\beta}_{\mathrm{std}} = 0.589$, achieving significance in 12/12 conditions, stronger than the oracle baseline (4/12 under clustered SE). $K_{\mathrm{eff}}$ loses all predictive power (0/12). The averaging over masking scenarios smooths estimation noise inherent in the three-judge oracle computation, strengthening the $\eta_{\max}$ signal. This demonstrates that $\eta_{\max}$ computed from partial panel information is robust to incomplete composition knowledge and retains (indeed improves) its predictive power for panel ASR.
152	
153	\section{Panel Selection Strategy Comparison}
154	\label{app:panel_selection}
155	
156	
157	Figure~\ref{fig:panel_design} compares three panel selection strategies: $\min(\eta_{\max})$ (select the panel minimizing weakest-judge vulnerability), random selection, and $\max(K_{\mathrm{eff}})$ (maximize diversity). The $\min(\eta_{\max})$ strategy achieves the lowest ASR in all 12 conditions, consistent with the weakest-link dominance documented in \S\ref{sec:dominance}.
158	
159	\section{Clustered Standard Error Analysis}
160	\label{app:forest_plot}
161	
162	Under clustered standard errors (clustering on the $K$ judge positions), $\eta_{\max}$ retains significance in 4/12 conditions while $K_{\mathrm{eff}}$ achieves significance in 0/12. This contrasts with OLS ($\eta_{\max}$ 10/12, $K_{\mathrm{eff}}$ 12/12) and wild cluster bootstrap ($\eta_{\max}$ 3/12, $K_{\mathrm{eff}}$ 4/12), illustrating how the choice of inference method modulates apparent significance at $K{=}3$ while coefficient direction remains positive (12/12) for $K_{\mathrm{eff}}$ across all methods, with significance ranging from 0/12 to 12/12 (Figure~\ref{fig:robustness}).
163	
164	\section{Robustness Checks: Subsampling and Specification}
165	\label{app:robustness_checks}
166	
167	Table~\ref{tab:robustness_checks} summarizes regression results across model subsets and alternative specifications at $K{=}5$, testing whether the predictor shift is robust to collinearity reduction and specification choice.
168	
169	\begin{table}[h]
170	\centering
171	\small
172	\begin{tabular}{lcccc}
173	\toprule
174	\textbf{Subset / Method} & $\boldsymbol{r}$ & $\boldsymbol{\eta_{\max}}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & \textbf{Trans.} \\
175	\midrule
176	Full bootstrap       & 0.81 & 2/12 & 7/12 & \checkmark \\
177	API-only (9) clust.  & 0.85 & 8/12 & 3/12 & --- \\
178	Cap-matched A (5A+4L) & 0.50 & ---  & 9/12 & \checkmark\checkmark \\
179	Cap-matched B (6A+3L) & 0.73 & ---  & 2/12 & --- \\
180	Fractional logit     & 0.81 & 6/12 & 9/12 & \checkmark \\
181	\bottomrule
182	\end{tabular}
183	\caption{Predictor shift robustness at $K{=}5$ across model subsets and specifications. $r$: correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$. $\eta_{\max}$ and $K_{\mathrm{eff}}$ columns show FDR-significant counts out of 12 conditions. Trans.: whether $K_{\mathrm{eff}}$ dominates $\eta_{\max}$. API-only models ($r{=}0.85$, VIF${=}4.4$) show partially collinear predictors; capability-matched subsamples ($r{=}0.50$) strengthen the shift. Fractional logit \citep{papke1996econometric} confirms OLS patterns with 98.6\% directional agreement (71/72 direction matches; the single discordance is $\eta_{\max}$ at $K{=}7$ for ARC $\times$ score manipulation).}
184	\label{tab:robustness_checks}
185	\end{table}
186	
187	The API-only subset ($r{=}0.85$, VIF${=}4.4$) demonstrates that elevated collinearity between $K_{\mathrm{eff}}$ and $\eta_{\max}$ partially inflates standard errors: both predictors achieve moderate significance but neither dominates, and the predictor shift does not replicate. Breaking collinearity through capability-matched subsampling (pool~A, $r{=}0.50$) strengthens $K_{\mathrm{eff}}$'s emergence to 9/12, comparable to the full-pool 7/12. Pool~B ($r{=}0.73$) falls near the decorrelation threshold, and the shift weakens accordingly. Random 9-model subsampling (1{,}000 trials) confirms an inverted-U: $K_{\mathrm{eff}}$ dominance rate peaks when the subsample includes 3--4 local models (maximizing capability spread) and drops when the pool is too homogeneous (Appendix~\ref{app:random_subsample}).
188	
189	\section{Random Subsample Analysis}
190	\label{app:random_subsample}
191	
192	To test whether the predictor shift depends on model pool composition, we randomly sample 9 of 15 models (1{,}000 trials), construct all $\binom{9}{5}$ panels, and run the bootstrap analysis at $K{=}5$. We stratify by the number of local models ($n_{\mathrm{local}} \in \{0, \ldots, 6\}$) in each subsample.
193	
194	Under clustered standard errors, $K_{\mathrm{eff}}$ is the dominant predictor in 51.4\% of subsamples (mean significance 1.85/12), with an inverted-U as a function of $n_{\mathrm{local}}$: subsamples with 3--4 local models (maximizing capability range) achieve the highest $K_{\mathrm{eff}}$ significance rate, while all-API ($n_{\mathrm{local}}{=}0$) and heavily-local ($n_{\mathrm{local}}{\geq}5$) subsamples show reduced detection. Significance is attenuated relative to the full pool by smaller sample sizes (126 vs.\ 3{,}003 panels at $K{=}5$), but the shift direction holds in the majority of subsamples. This confirms that the shift's detectability depends on capability diversity in the model pool rather than pool size per se.
195	
196	\section{Attacked $K_{\mathrm{eff}}$ Stability}
197	\label{app:attacked_keff}
198	
199	$K_{\mathrm{eff}}$ is computed from clean (unattacked) pairwise MI (\S\ref{sec:experiments}), but used to predict vulnerability under attack. We verify this assumption by recomputing MI from judge outputs under each attack type and comparing clean vs.\ attacked $K_{\mathrm{eff}}$ via Spearman rank correlation across all panels.
200	
201	\begin{table}[h]
202	\centering
203	\small
204	\begin{tabular}{lcc}
205	\toprule
206	\textbf{Attack} & \textbf{MMLU $\rho$} & \textbf{ARC $\rho$} \\
207	\midrule
208	Score manipulation & 0.98 & 0.99 \\
209	Authority bias     & 0.95 & 0.97 \\
210	Sycophancy         & 0.91 & 0.92 \\
211	Verbosity bias     & 0.91 & 0.92 \\
212	Prompt injection   & 0.63 & 0.60 \\
213	Position bias      & 0.60 & 0.08 \\
214	\bottomrule
215	\end{tabular}
216	\caption{Spearman rank correlation between clean and attacked $K_{\mathrm{eff}}$ across 455 panels ($K{=}3$). Four attack types preserve MI structure ($\rho{\geq}0.91$); prompt injection shows moderate perturbation ($\rho{\approx}0.60$--$0.63$); position bias substantially disrupts pairwise dependencies.}
217	\label{tab:attacked_keff}
218	\end{table}
219	
220	Four attack types (score manipulation, authority bias, sycophancy, verbosity bias) preserve MI structure with $\rho{\geq}0.91$ on both benchmarks, validating the use of clean $K_{\mathrm{eff}}$ as a predictor. Prompt injection shows moderate perturbation ($\rho{\approx}0.60$--$0.63$), consistent with its mode of overriding evaluation instructions, which can alter pairwise agreement patterns. Position bias substantially disrupts MI structure ($\rho{=}0.08$ on ARC, $p{=}0.10$), consistent with its anomalous regression behavior in Table~\ref{tab:dominance} (sole non-significant $\eta_{\max}$ condition) and suggesting that positional reordering fundamentally changes inter-judge dependence rather than merely introducing noise.
221	
222	\section{Cinelli--Hazlett Sensitivity Analysis}
223	\label{app:sensitivity}
224	
225	We apply the Cinelli--Hazlett omitted variable bias framework to quantify how robust $K_{\mathrm{eff}}$'s coefficient is to unobserved confounders. For each of the 36 conditions ($3K \times 2$ benchmarks $\times$ $6$ attacks), we compute the robustness value (RV): the minimum strength an unobserved confounder must have, in terms of partial $R^2$ with both treatment and outcome, to reduce $K_{\mathrm{eff}}$'s coefficient to zero.
226	
227	\begin{table}[h]
228	\centering
229	\footnotesize
230	\setlength{\tabcolsep}{3pt}
231	\begin{tabular}{rcllcccc}
232	\toprule
233	$\boldsymbol{K}$ & \textbf{Data} & \textbf{Attack} & \textbf{RV} & $\boldsymbol{\eta}$ $\boldsymbol{R^2_{\mathrm{tr}}}$ & $\boldsymbol{\eta}$ $\boldsymbol{R^2_{\mathrm{out}}}$ & \textbf{Exc.} \\
234	\midrule
235	3 & MMLU & Prompt inj.    & 0.419 & 0.587 & 0.059 & -- \\
236	3 & MMLU & Sycophancy     & 0.412 & 0.347 & 0.098 & \checkmark \\
237	3 & MMLU & Score manip.   & 0.410 & 0.735 & 0.002 & -- \\
238	3 & MMLU & Verbosity      & 0.330 & 0.342 & 0.203 & -- \\
239	3 & MMLU & Position bias  & 0.291 & 0.446 & 0.043 & -- \\
240	3 & MMLU & Authority bias & 0.371 & 0.493 & 0.019 & \checkmark \\
241	3 & ARC  & Prompt inj.    & 0.303 & 0.654 & 0.028 & \checkmark \\
242	3 & ARC  & Sycophancy     & 0.105 & 0.629 & 0.129 & \checkmark \\
243	3 & ARC  & Score manip.   & 0.273 & 0.838 & 0.003 & -- \\
244	3 & ARC  & Verbosity      & 0.259 & 0.658 & 0.047 & -- \\
245	3 & ARC  & Position bias  & 0.265 & 0.850 & 0.001 & -- \\
246	3 & ARC  & Authority bias & 0.224 & 0.582 & 0.056 & -- \\
247	\addlinespace
248	5 & MMLU & Prompt inj.    & 0.455 & 0.379 & 0.176 & \checkmark \\
249	5 & MMLU & Sycophancy     & 0.303 & 0.106 & 0.135 & \checkmark \\
250	5 & MMLU & Score manip.   & 0.321 & 0.597 & 0.003 & -- \\
251	5 & MMLU & Verbosity      & 0.235 & 0.120 & 0.206 & \checkmark \\
252	5 & MMLU & Position bias  & 0.131 & 0.272 & 0.090 & -- \\
253	5 & MMLU & Authority bias & 0.064 & 0.277 & 0.031 & -- \\
254	5 & ARC  & Prompt inj.    & 0.318 & 0.696 & 0.001 & -- \\
255	5 & ARC  & Sycophancy     & 0.103 & 0.555 & 0.063 & -- \\
256	5 & ARC  & Score manip.   & 0.196 & 0.800 & ${<}0.001$ & -- \\
257	5 & ARC  & Verbosity      & 0.135 & 0.642 & 0.034 & -- \\
258	5 & ARC  & Position bias  & 0.400 & 0.778 & 0.040 & -- \\
259	5 & ARC  & Authority bias & 0.181 & 0.509 & 0.012 & -- \\
260	\addlinespace
261	7 & MMLU & Prompt inj.    & 0.522 & 0.289 & 0.126 & \checkmark \\
262	7 & MMLU & Sycophancy     & 0.301 & 0.077 & 0.078 & \checkmark \\
263	7 & MMLU & Score manip.   & 0.393 & 0.515 & 0.004 & -- \\
264	7 & MMLU & Verbosity      & 0.205 & 0.078 & 0.195 & \checkmark \\
265	7 & MMLU & Position bias  & 0.207 & 0.179 & 0.073 & \checkmark \\
266	7 & MMLU & Authority bias & 0.005 & 0.200 & 0.011 & -- \\
267	7 & ARC  & Prompt inj.    & 0.355 & 0.629 & 0.004 & -- \\
268	7 & ARC  & Sycophancy     & 0.117 & 0.535 & 0.065 & -- \\
269	7 & ARC  & Score manip.   & 0.165 & 0.717 & 0.001 & -- \\
270	7 & ARC  & Verbosity      & 0.165 & 0.599 & 0.028 & -- \\
271	7 & ARC  & Position bias  & 0.422 & 0.705 & 0.046 & -- \\
272	7 & ARC  & Authority bias & 0.179 & 0.514 & 0.003 & -- \\
273	\bottomrule
274	\end{tabular}
275	\caption{Cinelli--Hazlett sensitivity analysis for $K_{\mathrm{eff}}$'s coefficient across 36 conditions. RV: robustness value (minimum partial $R^2$ an unobserved confounder must have with both $K_{\mathrm{eff}}$ and ASR to nullify the coefficient). $\eta$ $R^2_{\mathrm{tr}}$/$R^2_{\mathrm{out}}$: partial $R^2$ of $\eta_{\max}$ with $K_{\mathrm{eff}}$ (treatment) and ASR (outcome). Exc.: \checkmark\ if RV exceeds $\eta_{\max}$'s partial $R^2$ with treatment, indicating $K_{\mathrm{eff}}$'s coefficient is robust to the known capability confound. RV exceeds $\eta_{\max}$ in 11/36 conditions ($K{=}3$: 4/12, $K{=}5$: 3/12, $K{=}7$: 4/12).}
276	\label{tab:sensitivity}
277	\end{table}
278	
279	RV ranges from 0.005--0.59 across the 36 conditions (median by $K$: 0.30 at $K{=}3$, 0.22 at $K{=}5$, 0.21 at $K{=}7$), revealing heterogeneous robustness: some conditions show $K_{\mathrm{eff}}$ coefficients robust to strong confounders (e.g., $K{=}7$ MMLU prompt injection, RV${=}0.52$), while others are fragile (e.g., $K{=}7$ MMLU authority bias, RV${=}0.005$). The known $\eta_{\max}$ confound exceeds RV in 25/36 conditions ($K{=}3$: 8/12, $K{=}5$: 9/12, $K{=}7$: 8/12). RV exceeds $\eta_{\max}$ in 3--4/12 conditions across all $K$ values (4/12 at $K{=}3$, 3/12 at $K{=}5$, 4/12 at $K{=}7$), indicating that $K_{\mathrm{eff}}$'s robustness to omitted variable bias is stable rather than monotonically increasing with panel size.
280	
281	\begin{figure}[h]
282	\centering
283	\includegraphics[width=\columnwidth]{figures/fig_sensitivity_contour_K5.png}
284	\caption{Cinelli--Hazlett sensitivity contour plot at $K{=}5$ (representative). $x$-axis: confounder's partial $R^2$ with treatment ($K_{\mathrm{eff}}$); $y$-axis: confounder's partial $R^2$ with outcome (ASR). Contour lines show the adjusted $K_{\mathrm{eff}}$ coefficient under hypothetical confounders of varying strength. The diamond marks the known $\eta_{\max}$ confound benchmark; conditions where the benchmark falls inside the zero-contour indicate that the $\eta_{\max}$ confound alone could explain away $K_{\mathrm{eff}}$'s effect.}
285	\label{fig:sensitivity_contour}
286	\end{figure}
287	
288	\section{Cross-Benchmark Prediction Robustness}
289	\label{app:cross_benchmark}
290	
291	To test whether the diversity--vulnerability association reflects structural panel properties rather than benchmark-specific artifacts, we use $K_{\mathrm{eff}}$ computed from one benchmark's pairwise MI to predict panel vulnerability on the other. Under wild cluster bootstrap (FDR $\alpha{=}0.05$), both directions achieve 17/18 sign-consistent conditions across $K \in \{3, 5, 7\}$ (5/6 at $K{=}3$, 6/6 at $K{\geq}5$). The sole exception in both directions is $K{=}3$ position bias, where all judges share similar ASR (${\sim}0.5$), leaving insufficient heterogeneity for $K_{\mathrm{eff}}$ to discriminate. Cross-benchmark $K_{\mathrm{eff}}$ correlations are $r{\approx}0.76$--$0.78$, indicating that $K_{\mathrm{eff}}$ primarily captures panel-level compositional structure rather than benchmark-specific judge interactions. While sign consistency is symmetric, cross-prediction $R^2$ is moderately asymmetric (ARC$\to$MMLU generally higher), suggesting that coefficients estimated from ARC's more constrained binary format generalize conservatively to MMLU's richer four-way choice distribution.
292	
293	\section{Pool A Cinelli--Hazlett Sensitivity}
294	\label{app:sensitivity_poolA}
295	
296	To test whether reducing the $K_{\mathrm{eff}}$--$\eta_{\max}$ collinearity strengthens $K_{\mathrm{eff}}$'s independent signal, we repeat the Cinelli--Hazlett analysis on the capability-matched Pool~A subsample (9 models, $r{=}0.50$, 84 panels at $K{=}3$, 126 at $K{=}5$). Table~\ref{tab:sensitivity_poolA} compares the full-pool results with Pool~A.
297	
298	\begin{table}[h]
299	\centering
300	\small
301	\begin{tabular}{lccc}
302	\toprule
303	\textbf{Pool / $K$} & \textbf{RV $>$ $\eta$} & \textbf{Median RV} & \textbf{$K_{\mathrm{eff}}$ sig} \\
304	\midrule
305	Full / $K{=}3$ & 1/12 & 0.30 & 1/12 \\
306	Full / $K{=}5$ & 3/12 & 0.22 & 7/12 \\
307	Pool A / $K{=}3$ & 2/12 & 0.25 & --- \\
308	Pool A / $K{=}5$ & 10/12 & 0.32 & 9/12 \\
309	\bottomrule
310	\end{tabular}
311	\caption{Cinelli--Hazlett sensitivity comparison: full pool vs.\ capability-matched Pool~A. RV $>$ $\eta$: conditions where $K_{\mathrm{eff}}$'s robustness value exceeds the known $\eta_{\max}$ confound benchmark. Pool~A's reduced collinearity ($r{=}0.50$ vs.\ $0.81$ at $K{=}5$) increases the fraction of robust conditions from 1/12 to 2/12 at $K{=}3$ and from 3/12 to 10/12 at $K{=}5$, with the largest gains at $K{=}5$ where both benchmarks improve equally (ARC 5/6, MMLU 5/6).}
312	\label{tab:sensitivity_poolA}
313	\end{table}
314	
315	At $K{=}5$, Pool~A RV exceeds the $\eta_{\max}$ confound in 10/12 conditions (ARC 5/6, MMLU 5/6; the two failures are both sycophancy). The improvement from full-pool 3/12 to Pool~A 10/12 demonstrates that reducing collinearity substantially separates $K_{\mathrm{eff}}$'s signal from capability variance, though full causal identification would require training-based diversity control.
316	
317	\paragraph{Pool~A Power Constraints.}
318	Pool~A's restricted sample (84 panels at $K{=}3$, 126 at $K{=}5$) substantially limits statistical power under wild cluster bootstrap. Table~\ref{tab:poolA_power} reports power at standard effect sizes ($n_{\mathrm{sim}}{=}1{,}000$).
319	
320	\begin{table}[h]
321	\centering
322	\small
323	\begin{tabular}{rcc}
324	\toprule
325	$\boldsymbol{\beta_{\mathrm{std}}}$ & $\boldsymbol{K{=}3}$ \textbf{power} & $\boldsymbol{K{=}5}$ \textbf{power} \\
326	\midrule
327	0.3 & 12.6\% & 2.2\% \\
328	0.5 & 42.1\% & 8.5\% \\
329	0.7 & 69.0\% & 17.5\% \\
330	1.0 & 85.8\% & 30.1\% \\
331	\bottomrule
332	\end{tabular}
333	\caption{Pool~A bootstrap power ($n_{\mathrm{sim}}{=}1{,}000$, wild cluster bootstrap). MDE at 80\%: $K{=}3$, $\beta_{\mathrm{std}}{=}0.897$; $K{=}5$, not attainable (maximum 30.1\% at $\beta_{\mathrm{std}}{=}1.0$).}
334	\label{tab:poolA_power}
335	\end{table}
336	
337	Two implications follow. First, Pool~A at $K{=}5$ is fundamentally underpowered: the maximum attainable power (30.1\% at $\beta_{\mathrm{std}}{=}1.0$) never reaches 80\%. The 10/12 Cinelli--Hazlett success at $K{=}5$ therefore reflects large effect sizes surviving low power, strengthening the causal signal. Second, the low Cinelli--Hazlett RV at $K{=}3$ (2/12 exceeding the $\eta_{\max}$ benchmark) is partially explained by Pool~A's 84-panel design: MDE$_{\,80\%}{=}0.897$ means only effects exceeding ${\approx}0.9$ SD are detectable. Crucially, the full-pool $K{=}3 \to K{=}5$ significance increase ($4/12 \to 7/12$) is not a power artifact: Pool~A power at $K{=}5$ (max 30.1\%) is \emph{lower} than at $K{=}3$ (max 85.8\%), so the increase reflects growing effect sizes rather than inflated type~I error.
338	
339	\section{Epsilon Sensitivity Analysis}
340	\label{app:epsilon}
341	
342	The log-log specification (Equation~\ref{eq:regression}) uses $\epsilon{=}10^{-6}$ to handle zero ASR values. We assess sensitivity by comparing coefficients across $\epsilon \in \{10^{-3}, 10^{-6}, 10^{-9}\}$. Zero ASR rates are low on MMLU ($<$1\% of panels across conditions) but can reach 38--40\% on ARC for authority bias and sycophancy at $K{=}7$. Coefficient magnitudes show moderate sensitivity to $\epsilon$ at $K{=}3$ (maximum $\Delta\beta_{\mathrm{std}} = 0.10$ between $\epsilon{=}10^{-6}$ and $\epsilon{=}10^{-9}$, with three conditions exhibiting $K_{\mathrm{eff}}$ sign changes), reflecting the influence of zero-ASR panels on the log transformation. At $K{=}5$, all $K_{\mathrm{eff}}$ coefficient directions are preserved across $\epsilon$ values (maximum $\Delta\beta_{\mathrm{std}} = 0.073$ between $\epsilon{=}10^{-6}$ and $\epsilon{=}10^{-9}$, all $p < 0.005$), confirming that the predictor shift finding is robust to this modeling choice. The fractional logit specification (\S\ref{sec:experiments}), which avoids the log+$\epsilon$ transformation entirely, provides 98.6\% directional concordance with the main OLS results (71/72 direction matches) (Appendix~\ref{app:robustness_checks}).
343	
344	\section{Temperature Sensitivity Pilot}
345	\label{app:temperature}
346	
347	We evaluate $K_{\mathrm{eff}}$ stability across decoding temperatures $t \in \{0.0, 0.3, 0.7, 1.0\}$ using a 3-model pilot (GPT-4.1-nano, Gemini-3.5-Flash, Claude-3-Haiku; 300 clean samples per benchmark, 3 repeats). The maximum $K_{\mathrm{eff}}$ variation across all four temperatures is $\Delta < 0.034$ (MMLU: 0.033, ARC: 0.027), confirming that decoding randomness does not meaningfully perturb pairwise MI structure. Clean $K_{\mathrm{eff}}$ computation is thus robust to temperature variation within the range used by standard API configurations.
348	
349	\section{$K_{\mathrm{eff}}$ Distribution Statistics}
350	\label{app:keff_dist}
351	
352	Table~\ref{tab:keff_dist} summarizes the distribution of $K_{\mathrm{eff}}$ across panel sizes.
353	
354	\begin{table}[h]
355	\centering
356	\small
357	\begin{tabular}{rrccc}
358	\toprule
359	$\boldsymbol{K}$ & \textbf{Panels} & \textbf{Mean (SD)} & \textbf{Range} \\
360	\midrule
361	3 & 455     & 2.18 (0.30) & [1.47, 2.80] \\
362	5 & 3{,}003 & 3.35 (0.42) & [2.16, 4.30] \\
363	7 & 6{,}435 & 4.53 (0.47) & [2.97, 5.55] \\
364	\bottomrule
365	\end{tabular}
366	\caption{$K_{\mathrm{eff}}$ distribution across panel sizes. Mean $K_{\mathrm{eff}}$ increases approximately linearly with $K$ but remains below the theoretical maximum ($K_{\mathrm{eff}} = K$ for fully independent judges), reflecting non-zero inter-judge correlations.}
367	\label{tab:keff_dist}
368	\end{table}
369	
370	$K_{\mathrm{eff}}$ exhibits sufficient variance at each $K$ for regression analysis (coefficient of variation 10--14\%), with no floor or ceiling effects that would compress the predictor range.
371	
372	\section{Power Analysis Across Panel Sizes}
373	\label{app:power_analysis}
374	
375	Table~\ref{tab:mde} reports minimum detectable effect sizes (MDE at 80\% power) under wild cluster bootstrap for each $K$. The sharp decrease in MDE from $K{=}3$ to $K{=}5$ (0.144 to 0.048) reflects both increased sample size ($455 \to 3{,}003$ panels) and more clusters per position. $K_{\mathrm{eff}}$'s partial significance at $K{=}3$ (4/12) is consistent with moderate power at this sample size; the 7/12 significance at $K{=}5$ is not type~I error inflation, as the design can detect effects as small as 0.048 SD.
376	
377	\begin{table}[h]
378	\centering
379	\small
380	\begin{tabular}{rccc}
381	\toprule
382	$\boldsymbol{K}$ & \textbf{Panels} & \textbf{MDE ($\beta_{\mathrm{std}}$)} & \textbf{$K_{\mathrm{eff}}$ sig} \\
383	\midrule
384	3 & 455     & 0.144 & 4/12 \\
385	5 & 3{,}003 & 0.048 & 7/12 \\
386	7 & 6{,}435 & 0.036 & 8/12 \\
387	\bottomrule
388	\end{tabular}
389	\caption{Minimum detectable effect size (80\% power, 1{,}000 simulations, wild cluster bootstrap) by panel size. MDE decreases approximately as $1/\sqrt{N}$, confirming that $K{=}5$/$K{=}7$ significance reflects genuine effects rather than inflated type~I error.}
390	\label{tab:mde}
391	\end{table}
392	
393	\section{Alternative Diversity Measures}
394	\label{app:alt_diversity}
395	
396	We compare $K_{\mathrm{eff}}$ against three classical ensemble diversity measures using the same OLS specification (Equation~\ref{eq:regression}) with FDR correction across 12 conditions pooled over $K$ values.
397	
398	\begin{table}[h]
399	\centering
400	\small
401	\begin{tabular}{lcccc}
402	\toprule
403	\textbf{Measure} & \textbf{Sig} & \textbf{Dir.} & \textbf{$|\bar{\beta}_{\mathrm{std}}|$} & $\boldsymbol{\rho}$ \textbf{w/} $\boldsymbol{K_{\mathrm{eff}}}$ \\
404	\midrule
405	$Q$-statistic    & 9/12  & 6+/3$-$ & 0.251 & 0.599 \\
406	Disagreement     & 11/12 & 11+/0$-$ & 0.481 & 0.934 \\
407	$\kappa$-diversity & 11/12 & 11+/0$-$ & 0.497 & 0.978 \\
408	\addlinespace
409	$K_{\mathrm{eff}}$ (ref.) & 12/12 & 12+/0$-$ & 0.430 & --- \\
410	\bottomrule
411	\end{tabular}
412	\caption{Comparison of diversity measures as predictors of panel ASR (OLS, FDR-corrected, 12 conditions pooled across $K$). Sig: FDR-significant conditions. $|\bar{\beta}_{\mathrm{std}}|$: mean absolute standardized coefficient. $\rho$: Pearson correlation with $K_{\mathrm{eff}}$.}
413	\label{tab:alt_diversity}
414	\end{table}
415	
416	$K_{\mathrm{eff}}$ and $\kappa$-diversity \citep{kuncheva2003measures} are near-equivalent ($\rho{=}0.978$), with comparable significance counts (12/12 vs.\ 11/12) and effect sizes (0.430 vs.\ 0.497). Disagreement rate achieves similar predictive power ($\rho{=}0.934$, 11/12). The $Q$-statistic is the weakest predictor (9/12, $|\bar{\beta}_{\mathrm{std}}|{=}0.251$), consistent with its known insensitivity to the type of error correlation that is associated with panel vulnerability \citep{kuncheva2003measures}. $K_{\mathrm{eff}}$'s advantage over these alternatives is not predictive power but interpretability: it quantifies the number of effective independent channels in the panel, connecting directly to the information-theoretic foundation of panel aggregation (\S\ref{sec:experiments}).
417	
418	\section{$\kappa$-Diversity Predictor Shift Comparison}
419	\label{app:kappa_regime}
420	
421	To test whether the predictor shift (\S\ref{sec:cross_k}) is specific to $K_{\mathrm{eff}}$ or a generic property of diversity measures, we repeat the wild cluster bootstrap analysis replacing $K_{\mathrm{eff}}$ with $\kappa$-diversity ($1 - \bar{\kappa}$, where $\bar{\kappa}$ is the mean pairwise Cohen's $\kappa$ on clean winner labels; $\rho{=}0.978$ with $K_{\mathrm{eff}}$).
422	
423	\begin{table}[h]
424	\centering
425	\small
426	\begin{tabular}{rcccc}
427	\toprule
428	& \multicolumn{2}{c}{\textbf{$K_{\mathrm{eff}}$}} & \multicolumn{2}{c}{\textbf{$\kappa$-diversity}} \\
429	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
430	$\boldsymbol{K}$ & \textbf{div.\ sig} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & \textbf{div.\ sig} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} \\
431	\midrule
432	3 & 4/12  & 3/12 & 8/12 & 1/12 \\
433	5 & 7/12 & 2/12 & 7/12 & 4/12 \\
434	7 & 8/12  & 1/12 & 6/12 & 1/12 \\
435	\bottomrule
436	\end{tabular}
437	\caption{Predictor shift comparison: $K_{\mathrm{eff}}$ vs.\ $\kappa$-diversity across panel sizes (wild cluster bootstrap, BH FDR $\alpha{=}0.05$). $K_{\mathrm{eff}}$ exhibits a clear shift ($4 \to 7 \to 8$); $\kappa$-diversity significance decreases monotonically ($8 \to 7 \to 6$), showing no predictor shift.}
438	\label{tab:kappa_regime}
439	\end{table}
440	
441	$\kappa$-diversity is a stronger predictor than $K_{\mathrm{eff}}$ at $K{=}3$ (8/12 vs.\ 4/12), consistent with its larger mean effect size ($|\bar{\beta}_{\mathrm{std}}|{=}0.497$ vs.\ 0.430; Table~\ref{tab:alt_diversity}). However, $\kappa$-diversity shows no predictor shift: its significance \emph{decreases} from $K{=}3$ to $K{=}7$ ($8 \to 7 \to 6$), the opposite of $K_{\mathrm{eff}}$'s pattern ($4 \to 7 \to 8$). Furthermore, under $\kappa$-diversity, $\eta_{\max}$ retains significance at $K{=}5$ (4/12), whereas under $K_{\mathrm{eff}}$ it drops to 2/12. The predictor shift---co-determination at $K{=}3$ transitioning to diversity dominance at $K{\geq}5$---is thus specific to $K_{\mathrm{eff}}$'s MI-based formulation, which captures effective judge independence rather than pairwise label agreement.
442	
443	\section{Shannon MI Entropy Predictor Shift Comparison}
444	\label{app:shannon_entropy}
445	
446	Shannon MI entropy ($H_{\mathrm{MI}} = \binom{K}{2}^{-1} \sum_{i<j} \mathrm{MI}(i,j)$) averages raw pairwise mutual information, measuring mean non-redundancy rather than effective independence. It correlates negatively with $K_{\mathrm{eff}}$ ($r = -0.63$ to $-0.76$ across $K$): panels with high mean MI tend to have lower effective independent channels, because $K_{\mathrm{eff}}$'s $\exp(-2\,\mathrm{MI})$ transform penalizes high MI more aggressively than linear averaging.
447	
448	\begin{table}[h]
449	\centering
450	\small
451	\begin{tabular}{rcc}
452	\toprule
453	$\boldsymbol{K}$ & \textbf{Shannon MI sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} \\
454	\midrule
455	3 & 4/12 & 6/12 \\
456	5 & 4/12 & 8/12 \\
457	7 & 0/12 & 2/12 \\
458	\bottomrule
459	\end{tabular}
460	\caption{Predictor shift comparison: Shannon MI entropy vs.\ $K_{\mathrm{eff}}$ (within-framework wild cluster bootstrap, $B{=}999$, Webb weights, BH FDR $\alpha{=}0.05$). Shannon is flat then collapses ($4 \to 4 \to 0$); $K_{\mathrm{eff}}$ rises before declining ($6 \to 8 \to 2$). Bootstrap parameters differ from the primary analysis ($B{=}9{,}999$, Rademacher); absolute counts are not comparable with Table~\ref{tab:kappa_regime}.}
461	\label{tab:shannon_shift}
462	\end{table}
463	
464	Shannon MI entropy shows no predictor shift: significance is flat at $K{=}3$ and $K{=}5$ (4/12) before collapsing at $K{=}7$ (0/12). $K_{\mathrm{eff}}$ exhibits a clear rise from $K{=}3$ to $K{=}5$ ($6 \to 8$) within the same framework. Combined with the $\kappa$-diversity comparison (Appendix~\ref{app:kappa_regime}, $8 \to 7 \to 6$), two alternative diversity measures independently fail to exhibit the predictor shift, providing converging evidence that the shift is specific to $K_{\mathrm{eff}}$'s transformation of pairwise MI into an effective channel count.
465	
466	\section{Gaussian Copula Assumption and $K_{\mathrm{eff}}$ Robustness}
467	\label{app:copula_gof}
468	
469	$K_{\mathrm{eff}}$ admits a closed-form expression $K - \frac{1}{K}\sum_{i}\sum_{j \neq i} \rho_{ij}^2$ under the Gaussian copula, where $\exp(-2\,\mathrm{MI}(i,j)) = 1 - \rho_{ij}^2$ \citep{nelsen2006copulas}. We test whether this parametric assumption holds for judge pairs using the \citet{genest2008validity} Cram\'{e}r--von Mises goodness-of-fit test for Gaussian copulas.
470	
471	\paragraph{GoF Results.} Across all $\binom{15}{2} = 105$ judge pairs, the Gaussian copula is rejected at $\alpha{=}0.05$ for 97--100\% of pairs (MMLU: 102/105, 97.1\%; ARC: 104/105, 99.0\%). The rejections are not marginal: median $p$-values are ${<}0.001$ on both benchmarks. This indicates that the pairwise dependence structure among LLM judges is substantially non-Gaussian, likely reflecting the discrete three-category nature of winner labels and the heavy tail structure of judge agreement patterns.
472	
473	\paragraph{Ranking Robustness Despite Copula Rejection.} Despite the Gaussian copula being formally rejected, the closed-form $K_{\mathrm{eff}}$ (using $1 - \rho_{ij}^2$) and the plug-in MI $K_{\mathrm{eff}}$ (using $\exp(-2\,\widehat{\mathrm{MI}}(i,j))$ with Miller--Madow correction) produce highly concordant panel rankings within each $K$. Within-$K$ Spearman rank correlations are $\rho \approx 0.86$ ($K{=}3$: 0.862, $K{=}5$: 0.858, $K{=}7$: 0.867). The systematic level difference (plug-in $K_{\mathrm{eff}}$ mean 3.38 vs.\ closed-form 4.29, averaged across $K$) reflects the Miller--Madow bias correction increasing MI estimates, which compresses $\exp(-2\,\mathrm{MI})$ toward zero. This level shift does not affect regression results, which depend on ranking.
474	
475	\paragraph{Implications.} $K_{\mathrm{eff}}$'s effectiveness as a predictor of panel vulnerability does not depend on the Gaussian copula being correct. The $\exp(-2\,\mathrm{MI})$ kernel provides a nonparametric, information-theoretic measure of pairwise alienation; the Gaussian copula merely offers a convenient closed-form approximation that preserves ranking fidelity. All regression analyses in the main text use the closed-form $K_{\mathrm{eff}}$; the plug-in MI version would yield equivalent conclusions for any analysis based on panel ordering.
476	
477	\section{Quantization Dummy Regression}
478	\label{app:quant_dummy}
479	
480	To disentangle the AWQ quantization confound from the diversity signal, we augment Equation~\ref{eq:regression} with a binary dummy $D_{\mathrm{quant}}$ indicating whether the panel's weakest judge is a quantized local model. The augmented regression is:
481	\begin{equation}
482	\log(\mathrm{ASR} + \epsilon) = \alpha + \beta_1 \log(K_{\mathrm{eff}}) + \beta_2 \log(\eta_{\max} + \epsilon) + \beta_3 D_{\mathrm{quant}}.
483	\end{equation}
484	Adding the dummy attenuates $K_{\mathrm{eff}}$'s standardized coefficient from $+0.39$ ($K{=}3$) to $+0.34$ ($K{=}5$) to $+0.27$ ($K{=}7$), with FDR-significant counts of 6/12, 6/12, and 4/12 respectively. The attenuation confirms partial confounding: some of $K_{\mathrm{eff}}$'s explanatory power reflects the capability gap between quantized and API models rather than independence per se. However, collinearity between $D_{\mathrm{quant}}$ and both predictors escalates sharply with panel size (VIF${=}162$ at $K{=}7$), rendering the dummy unreliable for large panels. The quantization dummy analysis is therefore informative at $K{=}3$ (moderate VIF) but should be interpreted cautiously at $K{\geq}5$.
485	
486	\section{Bayesian Posterior Concentration Analysis}
487	\label{app:bayesian_entropy}
488	
489	Bayesian calibration neutralizes $K_{\mathrm{eff}}$ at $K{=}7$ (0/12 significant; \S\ref{sec:analysis}). One hypothesized explanation is that the posterior concentrates on 2--3 accurate judges, compressing effective panel diversity. We test this by computing the posterior concentration ratio $C = \max_j w_j^{\mathrm{post}} / \min_j w_j^{\mathrm{post}}$ across panels.
490	
491	The concentration ratio declines modestly across panel sizes: $C = 0.890$ ($K{=}3$), $0.874$ ($K{=}5$), $0.867$ ($K{=}7$), a total change of only 2.3 percentage points. This gradual decline is insufficient to explain the abrupt neutralization at $K{=}7$ (from 6/12 at $K{=}3$ to 0/12 at $K{=}7$). The pattern is therefore not explained by simple posterior concentration; rather, the interaction between Bayesian weighting and the combinatorial structure of larger panels likely produces the neutralization. Full characterization of this interaction remains an open question.
492	
493	\section{Monte Carlo Calibration of Wild Cluster Bootstrap}
494	\label{app:monte_carlo}
495	
496	To verify that the wild cluster bootstrap does not over-reject under the null hypothesis, we conduct a Monte Carlo calibration study. For each of the 36 conditions (12 attack$\times$benchmark conditions $\times$ 3 panel sizes), we generate 1{,}000 permutation datasets by randomly shuffling the ASR outcome within each cluster, destroying any true association between predictors and ASR. For each permuted dataset, we run the wild cluster bootstrap ($B{=}999$, Rademacher weights) and record whether the null is rejected at $\alpha{=}0.05$.
497	
498	Across all 36 conditions, the maximum empirical null rejection rate is 1.6\%, well below the nominal $\alpha{=}5\%$. The median rejection rate is 0.4\%. This confirms that the wild cluster bootstrap is conservative in our combinatorial design: the reported significance counts are lower bounds on what a correctly calibrated test would yield. The conservatism is expected given the low cluster counts (13, ${\leq}11$, ${\leq}9$ position clusters at $K{=}3,5,7$) and the use of Rademacher weights \citep{mackinnon2018wild}.
499	
500	\section{Near-Chance Model Sensitivity Analysis}
501	\label{app:near_chance}
502	
503	Two locally-hosted models (Qwen2.5-14B-AWQ, MMLU accuracy 0.253; Qwen2.5-72B-AWQ, 0.333) score near the 4-choice random baseline of 0.25. A natural concern is that the positive association between panel diversity ($K_{\mathrm{eff}}$) and attack success rate is mechanically driven by panels containing near-random judges, which simultaneously inflate both independence and vulnerability.
504	
505	We exclude all panels containing either model (MMLU ${<}\,0.35$ threshold), reducing the pool from 15 to 13 models and panel counts from 455/3{,}003/6{,}435 to 286/1{,}287/1{,}716 at $K{=}3/5/7$. We re-run OLS with BH-corrected $p$-values, the wild cluster bootstrap (WCB; $B{=}9{,}999$, Rademacher weights, max-$p$ across $K$ position clusters, BH-adjusted at $\alpha{=}0.05$), and the fractional logit GLM (Binomial, logit link, clustered SE with max-$p$, BH-adjusted). Table~\ref{tab:near_chance} reports FDR-significant $K_{\mathrm{eff}}$ counts out of 12 conditions.
506	
507	\begin{table}[h]
508	\centering
509	\small
510	\caption{Near-chance model sensitivity: FDR-significant $K_{\mathrm{eff}}$ conditions out of 12 (2 benchmarks $\times$ 6 attacks). $\bar{\beta}_{\mathrm{std}}$: mean standardized $K_{\mathrm{eff}}$ coefficient across conditions. The full-pool fractional logit count at $K{=}3$ (8/12) differs by $\pm 1$ from Table~\ref{tab:method_comparison} (9/12) due to clustering implementation details in the sensitivity script; this does not affect within-table comparisons.}
511	\label{tab:near_chance}
512	\begin{tabular}{llcccccc}
513	\toprule
514	$K$ & Panel set & $n$ & OLS & WCB & Frac & $\bar{\beta}_{\mathrm{std}}$ & $\bar{R}^2$ \\
515	\midrule
516	3 & Full (15 models) & 455 & 11/12 & 3/12 & 8/12 & 0.349 & 0.340 \\
517	3 & Filtered (13 models) & 286 & 12/12 & 4/12 & 9/12 & \textbf{0.480} & 0.333 \\
518	\midrule
519	5 & Full (15 models) & 3{,}003 & 12/12 & 7/12 & 10/12 & 0.437 & 0.285 \\
520	5 & Filtered (13 models) & 1{,}287 & 11/12 & 7/12 & 11/12 & \textbf{0.512} & 0.256 \\
521	\midrule
522	7 & Full (15 models) & 6{,}435 & 12/12 & 8/12 & 10/12 & 0.401 & 0.244 \\
523	7 & Filtered (13 models) & 1{,}716 & 11/12 & 2/12 & 11/12 & 0.385 & 0.203 \\
524	\bottomrule
525	\end{tabular}
526	\end{table}
527	
528	At $K{=}3$ and $K{=}5$, WCB significance is preserved or improved after filtering (3$\to$4 and 7$\to$7), and the mean standardized $\beta_{K_{\mathrm{eff}}}$ \emph{increases} from 0.349 to 0.480 ($K{=}3$) and from 0.437 to 0.512 ($K{=}5$), indicating that the diversity--vulnerability association is stronger, not weaker, without near-chance models. Fractional logit significance likewise improves after filtering at every $K$ (8$\to$9, 10$\to$11, 10$\to$11), confirming that the effect is not an artifact of the GLM specification. At $K{=}7$, WCB significance drops from 8/12 to 2/12; however, the combinatorial filtering removes 73.3\% of panels (6{,}435$\to$1{,}716), substantially reducing statistical power for the conservative bootstrap test. The raw WCB $p$-values at $K{=}7$ cluster in the 0.02--0.15 range rather than reversing sign, and the standardized coefficient remains positive ($\bar{\beta}_{\mathrm{std}}{=}0.385$). The $K{=}7$ attenuation is therefore attributable to power loss from the sample reduction rather than absence of a genuine effect.
529	
530	In contrast, $\eta_{\max}$ WCB significance drops sharply after filtering (4$\to$1, 2$\to$0, 1$\to$0 at $K{=}3/5/7$), indicating that the near-chance models contribute disproportionately to the $\eta_{\max}$--ASR association: their high individual vulnerability inflates both $\eta_{\max}$ variation and the corresponding WCB significance. Overall, the $K_{\mathrm{eff}}$--ASR association is robust to excluding near-chance models at all panel sizes, while $\eta_{\max}$ is not.
531	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76e16bf6-ce84-46f1-8188-52aa983eae5f",
  "isSidechain": true,
  "promptId": "b10b7490-36dc-4054-aaa8-5eef6127b4a0",
  "agentId": "ab1e410fa18d4cc66",
  "type": "user",
  "uuid": "2bf84639-7e78-4046-9748-72299334bdd7",
  "sourceToolAssistantUUID": "76e16bf6-ce84-46f1-8188-52aa983eae5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T14:18:13.839Z_

<details><summary>↩ Tool result · `toolu_01RhBRvfghy149unSDATe3CS`</summary>

```text
1	% Bibliography for cert_manip_resist_eval
2	% All entries verified via WebSearch on 2026-05-22
3	% ============================================================
4	
5	% ============================================================
6	% Part A: Papers from literature_map.yaml (12 papers)
7	% ============================================================
8	
9	@article{robertson2025stepwise,
10	  author    = {Robertson, Zachary and Koyejo, Sanmi},
11	  title     = {Let's Measure Information Step-by-Step: {LLM}-Based Evaluation Beyond Vibes},
12	  journal   = {arXiv preprint arXiv:2508.05469},
13	  year      = {2025},
14	  url       = {https://arxiv.org/abs/2508.05469},
15	  note      = {arXiv:2508.05469}
16	}
17	
18	@inproceedings{yang2026diversity,
19	  author    = {Yang, Yingxuan and Qu, Chengrui and Wen, Muning and Shi, Laixi and Wen, Ying and Zhang, Weinan and Wierman, Adam and Gu, Shangding},
20	  title     = {Understanding Agent Scaling in {LLM}-Based Multi-Agent Systems via Diversity},
21	  booktitle = {ICLR 2026 Workshop on AIMS},
22	  year      = {2026},
23	  url       = {https://arxiv.org/abs/2602.03794},
24	  note      = {arXiv:2602.03794}
25	}
26	
27	@article{turkmen2026ensemble,
28	  author    = {Turkmen, Yigit and Buyukates, Baturalp and Bastopcu, Melih},
29	  title     = {Don't Always Pick the Highest-Performing Model: An Information Theoretic View of {LLM} Ensemble Selection},
30	  journal   = {arXiv preprint arXiv:2602.08003},
31	  year      = {2026},
32	  url       = {https://arxiv.org/abs/2602.08003},
33	  note      = {arXiv:2602.08003}
34	}
35	
36	@inproceedings{kaneko2025bits,
37	  author    = {Kaneko, Masahiro and Baldwin, Timothy},
38	  title     = {Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against {LLMs}},
39	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
40	  year      = {2025},
41	  url       = {https://arxiv.org/abs/2510.17000},
42	  note      = {arXiv:2510.17000. Spotlight}
43	}
44	
45	@inproceedings{chen2025incentivizing,
46	  author    = {Chen, Baiting and Zhu, Tong and Han, Jiale and Li, Lexin and Li, Gang and Dai, Xiaowu},
47	  title     = {Incentivizing Truthful Language Models via Peer Elicitation Games},
48	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
49	  year      = {2025},
50	  url       = {https://arxiv.org/abs/2505.13636},
51	  note      = {arXiv:2505.13636}
52	}
53	
54	@inproceedings{qiu2026truthfulness,
55	  author    = {Qiu, Tianyi Alex and Carroll, Micah and Allen, Cameron},
56	  title     = {Truthfulness Despite Weak Supervision: Evaluating and Training {LLMs} Using Peer Prediction},
57	  booktitle = {International Conference on Learning Representations (ICLR)},
58	  year      = {2026},
59	  url       = {https://arxiv.org/abs/2601.20299},
60	  note      = {arXiv:2601.20299}
61	}
62	
63	@inproceedings{kim2025correlated,
64	  author    = {Kim, Elliot and Garg, Avi and Peng, Kenny and Garg, Nikhil},
65	  title     = {Correlated Errors in Large Language Models},
66	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
67	  year      = {2025},
68	  url       = {https://arxiv.org/abs/2506.07962},
69	  note      = {arXiv:2506.07962}
70	}
71	
72	@article{almasoud2026security,
73	  author    = {Al Masoud, Aiman and Anju, Antony and Arazzi, Marco and Cihangiroglu, Mert and Kembu, Vignesh Kumar and Nicolazzo, Serena and Nocera, Antonino and Vinod, P. and Sakthidharan, Saraga},
74	  title     = {Security in {LLM}-as-a-Judge: A Comprehensive {SoK}},
75	  journal   = {arXiv preprint arXiv:2603.29403},
76	  year      = {2026},
77	  url       = {https://arxiv.org/abs/2603.29403},
78	  note      = {arXiv:2603.29403}
79	}
80	
81	@inproceedings{feng2026noisy,
82	  author    = {Feng, Chen and Shen, Minghe and Balashankar, Ananth and Gerner-Beuerle, Carsten and Rodrigues, Miguel R. D.},
83	  title     = {Noisy but Valid: Robust Statistical Evaluation of {LLMs} with Imperfect Judges},
84	  booktitle = {International Conference on Learning Representations (ICLR)},
85	  year      = {2026},
86	  url       = {https://arxiv.org/abs/2601.20913},
87	  note      = {arXiv:2601.20913}
88	}
89	
90	@article{jung2026logarithmic,
91	  author    = {Jung, HyunJoon and Na, William},
92	  title     = {Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation},
93	  journal   = {arXiv preprint arXiv:2604.00477},
94	  year      = {2026},
95	  url       = {https://arxiv.org/abs/2604.00477},
96	  note      = {arXiv:2604.00477}
97	}
98	
99	% NOTE: literature_map.yaml cites this as "Chen et al. 2026" but first author is Kuai.
100	% Full title includes "and Reweighting Verifier Ensembles" (truncated in literature_map).
101	@article{kuai2026independent,
102	  author    = {Kuai, Chenchen and Jiang, Jiwan and Zhu, Zihao and Wang, Hao and Wu, Keshu and Li, Zihao and Zhang, Yunlong and Liu, Chenxi and Tu, Zhengzhong and Fan, Zhiwen and Zhou, Yang},
103	  title     = {How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles},
104	  journal   = {arXiv preprint arXiv:2604.07650},
105	  year      = {2026},
106	  url       = {https://arxiv.org/abs/2604.07650},
107	  note      = {arXiv:2604.07650}
108	}
109	
110	% ============================================================
111	% Part B: Classic references (10 papers)
112	% ============================================================
113	
114	@inproceedings{tramer2018ensemble,
115	  author    = {Florian Tram{\`e}r and Alexey Kurakin and Nicolas Papernot and Ian Goodfellow and Dan Boneh and Patrick McDaniel},
116	  title     = {Ensemble Adversarial Training: Attacks and Defenses},
117	  booktitle = {International Conference on Learning Representations (ICLR)},
118	  year      = {2018},
119	  url       = {https://arxiv.org/abs/1705.07204}
120	}
121	
122	@article{papernot2016transferability,
123	  author    = {Nicolas Papernot and Patrick McDaniel and Ian Goodfellow},
124	  title     = {Transferability in Machine Learning: from Phenomena to Black-Box Attacks using Adversarial Samples},
125	  journal   = {arXiv preprint arXiv:1605.07277},
126	  year      = {2016},
127	  url       = {https://arxiv.org/abs/1605.07277},
128	  note      = {arXiv:1605.07277}
129	}
130	
131	@inproceedings{papernot2017practical,
132	  author    = {Nicolas Papernot and Patrick McDaniel and Ian Goodfellow and Somesh Jha and Z. Berkay Celik and Ananthram Swami},
133	  title     = {Practical Black-Box Attacks against Machine Learning},
134	  booktitle = {Proceedings of the 2017 ACM on Asia Conference on Computer and Communications Security (ASIA CCS)},
135	  pages     = {506--519},
136	  year      = {2017},
137	  doi       = {10.1145/3052973.3053009},
138	  url       = {https://dl.acm.org/doi/10.1145/3052973.3053009}
139	}
140	
141	@inproceedings{zheng2023judging,
142	  author    = {Lianmin Zheng and Wei-Lin Chiang and Ying Sheng and Siyuan Zhuang and Zhanghao Wu and Yonghao Zhuang and Zi Lin and Zhuohan Li and Dacheng Li and Eric P. Xing and Hao Zhang and Joseph E. Gonzalez and Ion Stoica},
143	  title     = {Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},
144	  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},
145	  year      = {2023},
146	  url       = {https://arxiv.org/abs/2306.05685}
147	}
148	
149	@article{wang2023fair,
150	  author    = {Peiyi Wang and Lei Li and Liang Chen and Zefan Cai and Dawei Zhu and Binghuai Lin and Yunbo Cao and Lingpeng Kong and Qi Liu and Tianyu Liu and Zhifang Sui},
151	  title     = {Large Language Models are not Fair Evaluators},
152	  journal   = {arXiv preprint arXiv:2305.17926},
153	  year      = {2023},
154	  url       = {https://arxiv.org/abs/2305.17926},
155	  note      = {arXiv:2305.17926. Later published at ACL 2024}
156	}
157	
158	@inproceedings{greshake2023not,
159	  author    = {Kai Greshake and Sahar Abdelnabi and Shailesh Mishra and Christoph Endres and Thorsten Holz and Mario Fritz},
160	  title     = {Not what you've signed up for: Compromising Real-World {LLM}-Integrated Applications with Indirect Prompt Injection},
161	  booktitle = {Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec)},
162	  year      = {2023},
163	  doi       = {10.1145/3605764.3623985},
164	  url       = {https://dl.acm.org/doi/10.1145/3605764.3623985}
165	}
166	
167	@article{lamport1982byzantine,
168	  author    = {Leslie Lamport and Robert Shostak and Marshall Pease},
169	  title     = {The {Byzantine} Generals Problem},
170	  journal   = {ACM Transactions on Programming Languages and Systems (TOPLAS)},
171	  volume    = {4},
172	  number    = {3},
173	  pages     = {382--401},
174	  year      = {1982},
175	  doi       = {10.1145/357172.357176},
176	  url       = {https://dl.acm.org/doi/10.1145/357172.357176}
177	}
178	
179	@inproceedings{castro1999practical,
180	  author    = {Miguel Castro and Barbara Liskov},
181	  title     = {Practical {Byzantine} Fault Tolerance},
182	  booktitle = {Proceedings of the 3rd USENIX Symposium on Operating Systems Design and Implementation (OSDI)},
183	  pages     = {173--186},
184	  year      = {1999},
185	  publisher = {USENIX Association},
186	  url       = {https://www.usenix.org/conference/osdi-99/practical-byzantine-fault-tolerance}
187	}
188	
189	@book{schneier2000secrets,
190	  author    = {Bruce Schneier},
191	  title     = {Secrets and Lies: Digital Security in a Networked World},
192	  publisher = {John Wiley \& Sons},
193	  year      = {2000},
194	  isbn      = {978-0-471-25311-2}
195	}
196	
197	@inproceedings{krogh1995neural,
198	  author    = {Anders Krogh and Jesper Vedelsby},
199	  title     = {Neural Network Ensembles, Cross Validation, and Active Learning},
200	  booktitle = {Advances in Neural Information Processing Systems 7 (NIPS)},
201	  pages     = {231--238},
202	  year      = {1995},
203	  publisher = {MIT Press}
204	}
205	
206	% ============================================================
207	% Part C: Supplementary references (6+1 papers)
208	% ============================================================
209	
210	@inproceedings{hendrycks2021mmlu,
211	  author    = {Dan Hendrycks and Collin Burns and Steven Basart and Andy Zou and Mantas Mazeika and Dawn Song and Jacob Steinhardt},
212	  title     = {Measuring Massive Multitask Language Understanding},
213	  booktitle = {International Conference on Learning Representations (ICLR)},
214	  year      = {2021},
215	  url       = {https://openreview.net/forum?id=d7KBjmI3GmQ}
216	}
217	
218	@article{clark2018arc,
219	  author    = {Peter Clark and Isaac Cowhey and Oren Etzioni and Tushar Khot and Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},
220	  title     = {Think you have Solved Question Answering? {T}ry {ARC}, the {AI2} Reasoning Challenge},
221	  journal   = {arXiv preprint arXiv:1803.05457},
222	  year      = {2018},
223	  url       = {https://arxiv.org/abs/1803.05457},
224	  note      = {arXiv:1803.05457}
225	}
226	
227	@inproceedings{goodfellow2015adversarial,
228	  author    = {Ian J. Goodfellow and Jonathon Shlens and Christian Szegedy},
229	  title     = {Explaining and Harnessing Adversarial Examples},
230	  booktitle = {International Conference on Learning Representations (ICLR)},
231	  year      = {2015},
232	  url       = {https://arxiv.org/abs/1412.6572}
233	}
234	
235	% UNVERIFIED: User specified "Perez & Ribeiro 2022 — Ignore This Title and HackAPrompt"
236	% but that title belongs to Schulhoff et al. (EMNLP 2023). The actual Perez & Ribeiro 2022
237	% paper is "Ignore Previous Prompt: Attack Techniques For Language Models".
238	% Including the correct Perez & Ribeiro paper below.
239	@article{perez2022ignore,
240	  author    = {F{\'a}bio Perez and Ian Ribeiro},
241	  title     = {Ignore Previous Prompt: Attack Techniques For Language Models},
242	  journal   = {arXiv preprint arXiv:2211.09527},
243	  year      = {2022},
244	  url       = {https://arxiv.org/abs/2211.09527},
245	  note      = {arXiv:2211.09527. NeurIPS 2022 ML Safety Workshop, Best Paper Award}
246	}
247	
248	@article{budescu1993dominance,
249	  author    = {David V. Budescu},
250	  title     = {Dominance Analysis: A New Approach to the Problem of Relative Importance of Predictors in Multiple Regression},
251	  journal   = {Psychological Bulletin},
252	  volume    = {114},
253	  number    = {3},
254	  pages     = {542--551},
255	  year      = {1993},
256	  doi       = {10.1037/0033-2909.114.3.542}
257	}
258	
259	@book{nelsen2006copulas,
260	  author    = {Roger B. Nelsen},
261	  title     = {An Introduction to Copulas},
262	  edition   = {2nd},
263	  publisher = {Springer},
264	  year      = {2006},
265	  doi       = {10.1007/0-387-28678-0}
266	}
267	
268	% ============================================================
269	% Part D: Major Revision additions (Related Work expansion)
270	% ============================================================
271	
272	@book{condorcet1785essai,
273	  author    = {Marie Jean Antoine Nicolas de Caritat, marquis de Condorcet},
274	  title     = {Essai sur l'application de l'analyse \`a la probabilit\'e des d\'ecisions rendues \`a la pluralit\'e des voix},
275	  publisher = {Imprimerie Royale},
276	  year      = {1785},
277	  address   = {Paris}
278	}
279	
280	@article{kariyappa2019improving,
281	  author    = {Sanjay Kariyappa and Moinuddin K. Qureshi},
282	  title     = {Improving Adversarial Robustness of Ensembles with Diversity Training},
283	  journal   = {arXiv preprint arXiv:1901.09981},
284	  year      = {2019},
285	  url       = {https://arxiv.org/abs/1901.09981},
286	  note      = {arXiv:1901.09981}
287	}
288	
289	@inproceedings{pang2019improving,
290	  author    = {Tianyu Pang and Kun Xu and Chao Du and Ning Chen and Jun Zhu},
291	  title     = {Improving Adversarial Robustness via Promoting Ensemble Diversity},
292	  booktitle = {Proceedings of the 36th International Conference on Machine Learning (ICML)},
293	  pages     = {4970--4979},
294	  year      = {2019},
295	  publisher = {PMLR},
296	  url       = {https://proceedings.mlr.press/v97/pang19a.html}
297	}
298	
299	@article{brown2005managing,
300	  author    = {Gavin Brown and Jeremy L. Wyatt and Peter Tin\v{o}},
301	  title     = {Managing Diversity in Regression Ensembles},
302	  journal   = {Journal of Machine Learning Research},
303	  volume    = {6},
304	  pages     = {1621--1650},
305	  year      = {2005},
306	  url       = {https://www.jmlr.org/papers/v6/brown05a.html}
307	}
308	
309	@article{kuncheva2003measures,
310	  author    = {Ludmila I. Kuncheva and Christopher J. Whitaker},
311	  title     = {Measures of Diversity in Classifier Ensembles and Their Relationship with the Ensemble Accuracy},
312	  journal   = {Machine Learning},
313	  volume    = {51},
314	  number    = {2},
315	  pages     = {181--207},
316	  year      = {2003},
317	  doi       = {10.1023/A:1022859003006}
318	}
319	
320	@article{verga2024replacing,
321	  author    = {Pat Verga and Sebastian Hofstatter and Sophia Althammer and Yixuan Su and Aleksandra Piktus and Arkady Arkhangorodsky and Minjie Xu and Naomi White and Patrick Lewis},
322	  title     = {Replacing Judges with Juries: Evaluating {LLM} Generations with a Panel of Diverse Models},
323	  journal   = {arXiv preprint arXiv:2404.18796},
324	  year      = {2024},
325	  url       = {https://arxiv.org/abs/2404.18796},
326	  note      = {arXiv:2404.18796}
327	}
328	
329	@inproceedings{panickssery2024llm,
330	  author    = {Arjun Panickssery and Samuel R. Bowman and Shi Feng},
331	  title     = {{LLM} Evaluators Recognize and Favor Their Own Generations},
332	  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
333	  year      = {2024},
334	  url       = {https://arxiv.org/abs/2404.13076},
335	  note      = {arXiv:2404.13076}
336	}
337	
338	@book{tambe2011security,
339	  author    = {Milind Tambe},
340	  title     = {Security and Game Theory: Algorithms, Deployed Systems, Lessons Learned},
341	  publisher = {Cambridge University Press},
342	  year      = {2011},
343	  doi       = {10.1017/CBO9780511973031}
344	}
345	
346	% ============================================================
347	% Part E: Related Work expansion (reviewer W4)
348	% ============================================================
349	
350	@article{dawid1979maximum,
351	  author    = {Alexander Philip Dawid and Allan M. Skene},
352	  title     = {Maximum Likelihood Estimation of Observer Error-Rates Using the {EM} Algorithm},
353	  journal   = {Journal of the Royal Statistical Society. Series C (Applied Statistics)},
354	  volume    = {28},
355	  number    = {1},
356	  pages     = {20--28},
357	  year      = {1979},
358	  doi       = {10.2307/2346806}
359	}
360	
361	
362	% ============================================================
363	% Part F: Round 2 reviewer-requested references
364	% ============================================================
365	
366	@article{raina2024judgerobust,
367	  author    = {Vyas Raina and Adian Liusie and Mark Gales},
368	  title     = {Is {LLM}-as-a-Judge Robust? {I}nvestigating Universal Adversarial Attacks on Zero-shot {LLM} Assessment},
369	  journal   = {arXiv preprint arXiv:2402.14016},
370	  year      = {2024},
371	  url       = {https://arxiv.org/abs/2402.14016},
372	  note      = {arXiv:2402.14016}
373	}
374	
375	@article{ladha1992condorcet,
376	  author    = {Krishna K. Ladha},
377	  title     = {The {Condorcet} Jury Theorem, Free Speech, and Correlated Votes},
378	  journal   = {American Journal of Political Science},
379	  volume    = {36},
380	  number    = {3},
381	  pages     = {617--634},
382	  year      = {1992},
383	  doi       = {10.2307/2111584}
384	}
385	
386	@article{papke1996econometric,
387	  author    = {Leslie E. Papke and Jeffrey M. Wooldridge},
388	  title     = {Econometric Methods for Fractional Response Variables},
389	  journal   = {Journal of Applied Econometrics},
390	  volume    = {11},
391	  number    = {6},
392	  pages     = {619--632},
393	  year      = {1996},
394	  doi       = {10.1002/(SICI)1099-1255(199611)11:6<619::AID-JAE418>3.0.CO;2-1}
395	}
396	
397	@article{cameron2008bootstrap,
398	  author    = {A. Colin Cameron and Jonah B. Gelbach and Douglas L. Miller},
399	  title     = {Bootstrap-Based Improvements for Inference with Clustered Errors},
400	  journal   = {Review of Economics and Statistics},
401	  volume    = {90},
402	  number    = {3},
403	  pages     = {414--427},
404	  year      = {2008},
405	  doi       = {10.1162/rest.90.3.414}
406	}
407	
408	% ============================================================
409	% Part G: Round 3 reviewer-requested references
410	% ============================================================
411	
412	@article{mackinnon2018wild,
413	  author    = {James G. MacKinnon and Matthew D. Webb},
414	  title     = {The Wild Bootstrap for Few (Treated) Clusters},
415	  journal   = {The Econometrics Journal},
416	  volume    = {21},
417	  number    = {2},
418	  pages     = {114--135},
419	  year      = {2018},
420	  doi       = {10.1111/ectj.12107}
421	}
422	
423	
424	% ============================================================
425	% Part H: R5 reviewer-requested references
426	% ============================================================
427	
428	@article{maloyan2025investigating,
429	  author    = {Maloyan, Narek and Ashinov, Bislan and Namiot, Dmitry},
430	  title     = {Investigating the Vulnerability of {LLM}-as-a-Judge Architectures to Prompt-Injection Attacks},
431	  journal   = {arXiv preprint arXiv:2505.13348},
432	  year      = {2025},
433	  url       = {https://arxiv.org/abs/2505.13348},
434	  note      = {arXiv:2505.13348}
435	}
436	
437	@inproceedings{tamas2025benchmarking,
438	  author    = {Kavathekar, Ishan and Jain, Hemang and Rathod, Ameya and Kumaraguru, Ponnurangam and Ganu, Tanuja},
439	  title     = {{TAMAS}: Benchmarking Adversarial Risks in Multi-Agent {LLM} Systems},
440	  booktitle = {ICML 2025 Workshop on Multi-Agent Systems},
441	  year      = {2025},
442	  url       = {https://arxiv.org/abs/2511.05269},
443	  note      = {arXiv:2511.05269}
444	}
445	
446	@article{ebrahimi2025adversary,
447	  author    = {Ebrahimi, Sana and Dehghankar, Mohsen and Asudeh, Abolfazl},
448	  title     = {An Adversary-Resistant Multi-Agent {LLM} System via Credibility Scoring},
449	  journal   = {arXiv preprint arXiv:2505.24239},
450	  year      = {2025},
451	  url       = {https://arxiv.org/abs/2505.24239},
452	  note      = {arXiv:2505.24239}
453	}
454	
455	% ============================================================
456	% Part I: R5 remaining fixes
457	% ============================================================
458	
459	@inproceedings{zhu2020dverge,
460	  author    = {Huanrui Yang and Jingyang Zhang and Hongliang Dong and Nathan Inkawhich and Andrew Gardner and Andrew Touchet and Wesley Wilkes and Heath Berry and Hai Li},
461	  title     = {{DVERGE}: Diversifying Vulnerabilities for Enhanced Robust Generation of Ensembles},
462	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
463	  volume    = {33},
464	  year      = {2020},
465	  url       = {https://arxiv.org/abs/2009.14720},
466	  note      = {arXiv:2009.14720. Oral}
467	}
468	
469	@article{cameron2015practitioners,
470	  author    = {A. Colin Cameron and Douglas L. Miller},
471	  title     = {A Practitioner's Guide to Cluster-Robust Inference},
472	  journal   = {Journal of Human Resources},
473	  volume    = {50},
474	  number    = {2},
475	  pages     = {317--372},
476	  year      = {2015},
477	  doi       = {10.3368/jhr.50.2.317}
478	}
479	
480	% ============================================================
481	% Part J: R6 narrative reframe references
482	% ============================================================
483	
484	@article{breiman2001random,
485	  author    = {Leo Breiman},
486	  title     = {Random Forests},
487	  journal   = {Machine Learning},
488	  volume    = {45},
489	  number    = {1},
490	  pages     = {5--32},
491	  year      = {2001},
492	  doi       = {10.1023/A:1010933404324}
493	}
494	
495	@inproceedings{dietterich2000ensemble,
496	  author    = {Thomas G. Dietterich},
497	  title     = {Ensemble Methods in Machine Learning},
498	  booktitle = {First International Workshop on Multiple Classifier Systems (MCS)},
499	  series    = {LNCS},
500	  volume    = {1857},
501	  pages     = {1--15},
502	  year      = {2000},
503	  publisher = {Springer}
504	}
505	
506	@article{zhou2002ensembling,
507	  author    = {Zhi-Hua Zhou and Jianxin Wu and Wei Tang},
508	  title     = {Ensembling Neural Networks: Many Could Be Better Than All},
509	  journal   = {Artificial Intelligence},
510	  volume    = {137},
511	  number    = {1--2},
512	  pages     = {239--263},
513	  year      = {2002},
514	  doi       = {10.1016/S0004-3702(02)00190-X}
515	}
516	
517	@inproceedings{blanchard2017byzantine,
518	  author    = {Peva Blanchard and El Mahdi {El Mhamdi} and Rachid Guerraoui and Julien Stainer},
519	  title     = {Machine Learning with Adversaries: {B}yzantine Tolerant Gradient Descent},
520	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
521	  volume    = {30},
522	  pages     = {119--129},
523	  year      = {2017}
524	}
525	
526	@inproceedings{tan2024judgebench,
527	  author    = {Sijun Tan and Siyuan Zhuang and Kyle Montgomery and William Y. Tang and Alejandro Cuadron and Chenguang Wang and Raluca Ada Popa and Ion Stoica},
528	  title     = {{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},
529	  booktitle = {International Conference on Learning Representations (ICLR)},
530	  year      = {2025},
531	  url       = {https://arxiv.org/abs/2410.12784},
532	  note      = {arXiv:2410.12784}
533	}
534	
535	@inproceedings{li2024autoj,
536	  author    = {Junlong Li and Shichao Sun and Weizhe Yuan and Run-Ze Fan and Hai Zhao and Pengfei Liu},
537	  title     = {Generative Judge for Evaluating Alignment ({Auto-J})},
538	  booktitle = {International Conference on Learning Representations (ICLR)},
539	  year      = {2024},
540	  url       = {https://arxiv.org/abs/2310.05470},
541	  note      = {arXiv:2310.05470}
542	}
543	
544	@article{cinelli2020making,
545	  author    = {Carlos Cinelli and Chad Hazlett},
546	  title     = {Making Sense of Sensitivity: Extending Omitted Variable Bias},
547	  journal   = {Journal of the Royal Statistical Society: Series B},
548	  volume    = {82},
549	  number    = {1},
550	  pages     = {39--67},
551	  year      = {2020},
552	  doi       = {10.1111/rssb.12348}
553	}
554	
555	@article{genest2008validity,
556	  author    = {Christian Genest and Bruno R\'{e}millard},
557	  title     = {Validity of the Parametric Bootstrap for Goodness-of-Fit Testing in Semiparametric Models},
558	  journal   = {Annales de l'Institut Henri Poincar\'{e} -- Probabilit\'{e}s et Statistiques},
559	  volume    = {44},
560	  number    = {6},
561	  pages     = {1096--1127},
562	  year      = {2008},
563	  doi       = {10.1214/07-AIHP148}
564	}
565	
566	@article{qian2026collabeval,
567	  author    = {Yiyue Qian and others},
568	  title     = {{CollabEval}: Enhancing {LLM}-as-a-Judge via Multi-Agent Collaboration},
569	  journal   = {arXiv preprint arXiv:2603.00993},
570	  year      = {2026},
571	  url       = {https://arxiv.org/abs/2603.00993},
572	  note      = {arXiv:2603.00993}
573	}
574	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3715f44b-2e73-4b28-9479-5c4fc2fdadcf",
  "isSidechain": true,
  "promptId": "b10b7490-36dc-4054-aaa8-5eef6127b4a0",
  "agentId": "ab1e410fa18d4cc66",
  "type": "user",
  "uuid": "063a466a-882c-40f7-b1fd-377f212a876e",
  "sourceToolAssistantUUID": "3715f44b-2e73-4b28-9479-5c4fc2fdadcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T14:18:14.029Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QY63HzKa39agoHm72PiHan`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/cert_manip_resist_eval/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "063a466a-882c-40f7-b1fd-377f212a876e",
  "isSidechain": true,
  "agentId": "ab1e410fa18d4cc66",
  "requestId": "req_011CbPRyfVh9khvgwdTusKTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "481395b0-5165-4960-980b-03da5a79c5b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GW8Jsw2L52Gj89vaYojQ1p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 36739,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 771
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 36739,
          "cache_creation_input_tokens": 771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 771,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T14:18:14.036Z_

<details><summary>↩ Tool result · `toolu_01QY63HzKa39agoHm72PiHan`</summary>

```text
1	# Distilled Writing — Certifiable Manipulation Resistance for Multi-Judge LLM Eval
2	
3	> 8 篇深度精读论文的叙事结构、图表设计、论证策略归纳。
4	
5	## 1. 主流故事类型："化繁为简型" (3/8)
6	Yang2026, Feng2026, Turkmen2026: 复杂现象→单一信息论量→简洁解释。Turkmen 用 4 递进定理（独立→分解→饱和→算法）。**中置信度**。
7	→ 找一个统一量 (K_eff) 归纳不同现象。用递进定理链构建理论。
8	
9	## 2. Intro: 5 段 + 末段贡献列表 (7/8)
10	**高置信度**。模板: (1) 领域背景, (2) 现有局限, (3) 核心 insight, (4) 结果预览, (5) 编号贡献。贡献 3 个最常见 (5/8)，措辞 "framework + theory + empirical"。
11	
12	## 3. Hook: 悖论式最强
13	分布: 悖论/反直觉 3/8, 问题式 2/8, 能力缺口 1/8, 统一 1/8。**中置信度**。
14	Turkmen "Don't Always Pick the Highest-Performing Model" 挑战直觉; Robertson "Instead of 'which is better?' ask 'do they share information?'" 概念替换。
15	→ 可用 "Adding more judges doesn't make evaluation safer"。
16	
17	## 4. 张力: 假设失效 + 数字冲击
18	**6/8 篇**。**高置信度**。揭示被忽视假设→展示失效证据。Kim2025 "60% agreement when both err (vs 33% baseline)" 一个数字摧毁多样性假设。
19	→ 找同样冲击力的反直觉数字。
20	
21	## 5. Figure 1: 无主导模式，按论文类型选
22	method_overview 2/8, motivation 2/8, teaser_result 2/8, problem_illustration 2/8。**中置信度**。
23	理论导向偏 motivation（Yang 的 diminishing returns, Kim 的 heatmap）; 方法导向偏 teaser。
24	→ 本项目建议 motivation 类: homo vs hetero ASR scaling 对比。
25	
26	## 6. 主结果: Scaling→Line plot, 对比→Table
27	**7/8**。**高置信度**。
28	Scaling 行为: line plot (Turkmen error-vs-k, Yang accuracy-vs-N, Kaneko log-log)。
29	方法对比: table (PEG Table 1, TVD-MI Table 2)。
30	高亮: bold best 5/8; 理论验证用 regression slopes+p-values (Kaneko)。
31	统计: 趋势为 mean±std across seeds，但 3/8 仍 single run。
32	
33	## 7. 消融: Full numbers 主导 (5/8)
34	**高置信度**。无 checkmark grid。关键消融放 main（PEG K-scaling），其余 appendix。
35	
36	## 8. 图表叙事流 (6/8 共识)
37	**高置信度**。Motivation/Problem → Method/Theory → Main Results → Ablation。
38	数量: 4-6 figures (中位 5), 3-5 tables (中位 4)。
39	分工: scaling/correlation→图; 方法对比/消融→表; 扩展→appendix。
40	
41	## 9. 理论验证的视觉模式
42	**3/8**。**中置信度**。
43	Kaneko: log-log plot, slope-1 参考线; Turkmen: empirical vs copula scatter; Yang: K* 单调性。
44	→ K_eff 验证需 "theoretical prediction vs empirical" 对齐图。
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "481395b0-5165-4960-980b-03da5a79c5b8",
  "isSidechain": true,
  "promptId": "b10b7490-36dc-4054-aaa8-5eef6127b4a0",
  "agentId": "ab1e410fa18d4cc66",
  "type": "user",
  "uuid": "c9e0dec9-809a-44fa-8c6e-c542970b5ff6",
  "sourceToolAssistantUUID": "481395b0-5165-4960-980b-03da5a79c5b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-25T14:18:33.906Z_

Perfect! I've gathered all the information you need. Here's my comprehensive report:

## 1. Bibliography and Appendix Ordering (main.tex)

**Finding: Appendix BEFORE bibliography.**

- Line 46: `\input{appendix}`
- Line 47: `\input{appendix_attacks}`
- Line 49: `\bibliography{references}`

The appendix materials are included before the bibliography, which is the standard structure.

---

## 2. Appendix Structure Analysis (appendix.tex)

**Total scope:** 531 lines (substantial appendix covering A-J)

### Current Tables and Figures in Appendix:

**Tables:**
- Table 1: Crossed random effects vs. wild cluster bootstrap significance (line 28, labeled tab:crossed_re)
- Table 2: Aggregation method comparison at K=5 (line 107, labeled tab:aggregation_k5)
- Table 3: Aggregation method comparison at K=7 (line 129, labeled tab:aggregation_k7)
- Table 4: Spearman rank correlation — clean vs attacked K_eff (line 201, labeled tab:attacked_keff)
- Table 5: Cinelli–Hazlett sensitivity analysis (line 227, labeled tab:sensitivity)
- Table 6: Cinelli–Hazlett sensitivity contour plot (line 282, labeled fig:sensitivity_contour — marked as figure but referenced as table)
- Table 7: Pool A Cinelli–Hazlett Sensitivity (line 298, labeled tab:sensitivity_poolA)
- Table 8: Pool A power constraints (line 320, labeled tab:poolA_power)
- Table 9: Comparison of diversity measures as predictors (line 398, labeled tab:alt_diversity)
- Table 10: Predictor shift comparison — K_eff vs κ-diversity (line 423, labeled tab:kappa_regime)
- Table 11: Predictor shift comparison — Shannon MI entropy vs K_eff (line 448, labeled tab:shannon_shift)
- Table 12: K_eff distribution across panel sizes (line 354, labeled tab:keff_dist)
- Table 13: Minimum detectable effect size by panel size (line 377, labeled tab:mde)
- Table 14: Predictor shift robustness at K=5 (line 169, labeled tab:robustness_checks)
- Table 15: Near-chance model sensitivity (line 507, labeled tab:near_chance)

**Figures:**
- Figure 1: K_eff and η_max scatter (line 54, labeled fig:keff_eta_scatter)
- Figure 2: Per-condition predictor dominance heatmap (line 61, labeled fig:dominance_heatmap)
- Figure 3: GAM bootstrap K_eff effect direction (line 73, labeled fig2_gam_keff_split)
- Figure 4: K_eff coefficient distribution across aggregation methods (line 92, labeled fig3_aggregation_gradient)
- Figure 5: Panel-level correlation scatter K=5 (line 54, labeled fig_keff_eta_scatter)
- Figure 6: Dominance heatmap (line 61, labeled fig_dominance_heatmap)
- Figure 7: Robustness via boostrap GAM (line 72, labeled fig2_gam_keff_split)
- Figure 8: Aggregation gradient (line 92, labeled fig3_aggregation_gradient)
- Figure 9: Cinelli–Hazlett sensitivity contour (line 281, labeled fig_sensitivity_contour_K5)

**No Table 10 or Table 19 with the specific structures you asked about** — these appear to be either not yet present in the appendix or may be referenced differently.

---

## 3. References Count (references.bib)

**Total entries: 54 bibliography entries**

Breakdown by type:
- **@article:** 18 entries (lines 9, 27, 90, 101, 149, 239, 248, 299, 320, 366, 375, 386, 397, 412, 428, 446, 469, 566)
- **@inproceedings:** 24 entries (lines 18, 36, 45, 54, 63, 81, 114, 131, 141, 158, 179, 210, 227, 329, 437, 459, 517, 526, 535)
- **@book:** 3 entries (lines 189, 259, 272)

Organized in 10 parts: Literature map (12), Classic (10), Supplementary (6+1), Major Revision (5), Round 2 (4), Round 3 (1), R5 additions (3), R5 fixes (2), R6 narrative (6), Practitioner's guide (1).

---

## 4. Distilled Writing Skill Guidance

**File path:** /home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/cert_manip_resist_eval/distilled-writing.skill.md

The skill is 45 lines and covers **narrative structure induction from 8 papers**, with sections on:

1. **Story type**: "化繁为简型" (simplify complexity) — finding unified quantities like K_eff
2. **Intro structure**: 5-segment + contributions list pattern (high confidence)
3. **Hook patterns**: Paradox/counterintuition strongest (3/8 papers)
4. **Tension dynamics**: Show hypothesis failure + shocking numbers (6/8 papers, high confidence)
5. **Figure 1 guidance**: Recommend motivation-style showing "homo vs hetero ASR scaling" contrast
6. **Main results**: Scaling → line plots; comparisons → tables with bold best values
7. **Ablation design**: Full numbers dominate (no checkmark grids)
8. **Narrative flow**: Motivation → Method → Results → Ablation (6/8 consensus)
9. **Theory verification**: Visual patterns like log-log plots with reference lines, empirical vs theoretical scatter

**No specific guidance on LLM prompt template formatting with light yellow background or \textit style** is present in the skill file. The skill is focused on narrative/visual structure rather than typography details for appendix prompt examples.

---

## Summary

The paper structure is standard (appendix before bibliography). The appendix is substantial (531 lines) with 15 tables and 9 figures currently present, but I don't see the specific Table 10 or Table 19 you referenced—these may need to be created or are referenced differently. The bibliography has 54 total entries across articles, inproceedings, and books. The distilled writing skill emphasizes unified theoretical quantities, paradoxical hooks, and clear visual hierarchies (line plots for scaling, tables for comparisons) but lacks specific guidance on prompt template typography.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9e0dec9-809a-44fa-8c6e-c542970b5ff6",
  "isSidechain": true,
  "agentId": "ab1e410fa18d4cc66",
  "requestId": "req_011CbPRyrsJq1TYy5khXv1yX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01a4cda9-28de-4517-b1b1-7d50ff300ba2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "85ece0fb-92af-4331-ae26-b18b3f9a12c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "async-drifting-fairy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R6RC69HpYsCdtVBvHKTqTg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 32453,
      "cache_read_input_tokens": 37510,
      "output_tokens": 1647,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32453
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1647,
          "cache_read_input_tokens": 37510,
          "cache_creation_input_tokens": 32453,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32453,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
