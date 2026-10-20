# Research conversation: Read the following LaTeX files from `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/p

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a63b50c90ee8743e8.jsonl`
- **Structured JSON:** [`53a37454dfacc3374ba8.json`](../../sessions/53/53a37454dfacc3374ba8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-25T20:12:00.042Z_

Read the following LaTeX files from `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/` and extract EVERY numerical claim (percentages, counts, ranges, ratios). For each number, note the file, line number, and surrounding context.

Files to read:
1. `abstract.tex` — all numbers
2. `introduction.tex` — all numbers  
3. `experiments.tex` — all numbers (this is the most important one, read it fully)
4. `conclusion.tex` — all numbers
5. `method.tex` — all numbers (read fully, especially §3.2 topology-specific rates)

Focus especially on:
- Percentages (violation rates, sign-flip rates, bias reduction, etc.)
- Ranges (e.g., "12.4--42.1%", "0.614--0.690")
- Specific values (e.g., "1.6% MAPE", "52.6%", "83.4%", "93.6%")
- Counts (e.g., "161 scenarios", "23 configurations", "100,000 matrices")
- Correlation values (rho, p-values)

List each number as: [file:line] "quoted context" → number_value

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a63b50c90ee8743e8",
  "type": "user",
  "uuid": "0c75032e-e597-42eb-ae37-c97e9445b970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T20:12:02.538Z_

I'll systematically extract all numerical claims from these LaTeX files. Let me start by reading them all in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c75032e-e597-42eb-ae37-c97e9445b970",
  "isSidechain": true,
  "agentId": "a63b50c90ee8743e8",
  "requestId": "req_011CbPtxX5Yi2QX7TBSs283U",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c1a0e0d1-fbe6-4cb9-a24f-3ec995184cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ro5KRg6Z39DHbu6iP55xiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 3 · 2026-05-25T20:12:02.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K5yiSvMXULQmaV1prVWs3N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1a0e0d1-fbe6-4cb9-a24f-3ec995184cc2",
  "isSidechain": true,
  "agentId": "a63b50c90ee8743e8",
  "requestId": "req_011CbPtxX5Yi2QX7TBSs283U",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ed5e2b12-1259-4ceb-a18b-c55385a8a607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ro5KRg6Z39DHbu6iP55xiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 4 · 2026-05-25T20:12:02.771Z_

<details><summary>↩ Tool result · `toolu_01K5yiSvMXULQmaV1prVWs3N`</summary>

```text
1	\begin{abstract}
2	When large language model (LLM)-generated annotations feed into causal inference, annotation quality alone is insufficient to assess causal validity; the causal directed acyclic graph (DAG) topology determines whether errors attenuate, amplify, or reverse the treatment effect estimate. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification in linear structural equation models and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. Under proportional effects, five topologies preserve the treatment effect sign under regularity conditions; exposure and instrumental variable (IV) can reverse it. Under empirical LLM confusion matrices, sign reversal is confined to exposure topology. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$, $K{=}3$ symmetric) and extensively validated (general $K{\geq}3$) monotonicity that yields a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. A case study with 10 real LLM confusion matrices confirms: topology-aware correction reduces exposure bias from ${\sim}$61\% to ${<}$1\%, while topology-blind corrections are provably futile under linear regression for four topologies\footnote{Code and data are available at \url{https://anonymous.4open.science/r/causal_annot_error_attrib-C146/}.}.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed5e2b12-1259-4ceb-a18b-c55385a8a607",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a63b50c90ee8743e8",
  "type": "user",
  "uuid": "0a1ddce7-ae1c-46d8-a08a-211f7685d605",
  "sourceToolAssistantUUID": "ed5e2b12-1259-4ceb-a18b-c55385a8a607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T20:12:03.004Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GY26vBLsZroigi9JRSJSRJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a1ddce7-ae1c-46d8-a08a-211f7685d605",
  "isSidechain": true,
  "agentId": "a63b50c90ee8743e8",
  "requestId": "req_011CbPtxX5Yi2QX7TBSs283U",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff644b9c-edd8-4d2e-9e21-d875ef2a61a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ro5KRg6Z39DHbu6iP55xiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 6 · 2026-05-25T20:12:03.012Z_

<details><summary>↩ Tool result · `toolu_01GY26vBLsZroigi9JRSJSRJ`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models (LLMs) are rapidly replacing human annotators in computational social science~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Most tasks are inherently multi-class (stance detection: 3--4 categories, sentiment: 5, disaster response: 10+), and annotation errors propagate into downstream causal estimates in ways that depend on both error structure and causal design. \citet{baumann2025} show that 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, with 60\% error correlation across models~\cite{kim_garg2025}. Standard metrics do not capture this risk: within $F_1$ 0.61--0.69, causal bias varies by an order of magnitude across topologies.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs, an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee vanishes at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients; sign reversal can occur even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient is never reversed under the tested $\beta$ configurations where a single category dominates ($\beta_1 \gg \beta_2$), an empirical regularity we discuss in Section~\ref{sec:method}.
7	
8	$F_1$ does not exhibit significant rank correlation with causal bias ($\rho = -0.10$, $p = 0.45$ across 56 HumAID scenarios; bias varies $>$10${\times}$ (from $<$6\% to 42.1\%) within $F_1$ 0.614--0.690). Prior work noted polytomous sign reversal~\cite{dosemeci1990, veirod_laake2001} and confounder amplification~\cite{brenner1993}, but covered at most one topology~\cite{lee_wood_doughty2024}. We present the first systematic analysis jointly addressing multi-class ($K{\geq}3$) misclassification across seven directed acyclic graph (DAG) topologies, with analytical predictions matching Monte Carlo within 1.6\% MAPE across 161 scenarios.
9	
10	We address these gaps with three contributions:
11	
12	\begin{enumerate}
13	\item \textbf{Multi-class bias taxonomy.} We derive bias expressions for seven canonical DAG topologies\footnote{These span the four structural roles of the annotated variable: treatment (exposure), outcome-side covariate (confounding, mediation, M-bias, front-door), selection variable (collider), and instrumental variable (IV).} (Figure~\ref{fig:dag_taxonomy}) under $K$-class non-differential misclassification and establish a sign-preservation/reversal dichotomy: five topologies preserve the treatment effect sign under topology-specific regularity conditions (Proposition~\ref{prop:signflip}), while exposure and IV can reverse it.
14	
15	\item \textbf{Annotation Sensitivity Values.} We define three ASV diagnostics (magnitude, significance, and sign-flip) with proved envelope monotonicity (Theorems~\ref{thm:monotone},~\ref{thm:k3_symmetric}) and $\varepsilon$-approximate monotonicity for general $K{\geq}3$ (Conjecture~\ref{conj:monotone}). This reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune).
16	
17	\item \textbf{Topology-aware correction routing.} Frisch--Waugh--Lovell (FWL) invariance renders matrix-based corrections provably ineffective for four topologies (confounding, mediation, collider, M-bias). We evaluate five correction methods and provide a topology-aware decision procedure (Algorithm~\ref{alg:correction}), validated with real LLM confusion matrices.
18	\end{enumerate}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff644b9c-edd8-4d2e-9e21-d875ef2a61a3",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a63b50c90ee8743e8",
  "type": "user",
  "uuid": "fe4b5e20-b0ea-4fde-9e35-61153e61dadc",
  "sourceToolAssistantUUID": "ff644b9c-edd8-4d2e-9e21-d875ef2a61a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T20:12:03.172Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GJzkWBRbGRFY9QCUdtfVrG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe4b5e20-b0ea-4fde-9e35-61153e61dadc",
  "isSidechain": true,
  "agentId": "a63b50c90ee8743e8",
  "requestId": "req_011CbPtxX5Yi2QX7TBSs283U",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6dbd6b2a-a66f-42e5-9729-3ca00cb47fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ro5KRg6Z39DHbu6iP55xiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 8 · 2026-05-25T20:12:03.180Z_

<details><summary>↩ Tool result · `toolu_01GJzkWBRbGRFY9QCUdtfVrG`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{table}[t]
5	\centering
6	\caption{Bias under $K{=}3$ non-differential misclassification (100{,}000 Dirichlet$(1,1,1)$ matrices). Violation: $|\text{bias}| > 0$; Sign Flip: any coefficient reverses sign; Amplif.: $|\hat{\tau}| > |\tau|$. $\tau_{\text{sf}}{=}0$?: sign-flip guarantee holds unconditionally (Yes), conditionally (Cond.; Proposition~\ref{prop:signflip}), or not (No). Collider 100\% amplification reflects Berkson bias; misclassification is protective.}
7	\label{tab:taxonomy}
8	\small
9	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
10	\toprule
11	\textbf{Topology} & \textbf{Violation} & \textbf{Sign Flip} & \textbf{Amplif.} & $\tau_{\text{sf}}{=}0$? \\
12	\midrule
13	Confounding & 100\% & 0\% & 100\% & Cond. \\
14	Exposure & 85\% & 83.4\% & 14.1\% & No \\
15	Mediation & 100\% & 0\% & 100\% & Cond. \\
16	Front-door & 100\% & 0\% & 100\% & Cond. \\
17	Collider & 100\% & 0\% & 100\% & Cond. \\
18	M-bias & 53.2\% & 0\% & 10.4\% & Yes \\
19	IV & 100\% & 52.6\% & 100\% & No \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three natural language processing (NLP) tasks ($K{=}2,3,10$).
25	
26	\subsection{Setup}
27	\label{sec:setup}
28	
29	For each topology, we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute analytical probability limits, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
30	
31	\subsection{Bias Taxonomy}
32	\label{sec:taxonomy_results}
33	
34	\begin{figure}[t]
35	\centering
36	\includegraphics[width=\columnwidth]{fig7_dirichlet_overlay.pdf}
37	\caption{Empirical LLM confusion matrices (markers) overlaid on theoretical violation-rate curves from $K{=}3$ Dirichlet analysis. Left: exposure; right: IV. Real-world accuracy places all models in the low-risk region for IV sign reversal but not for exposure.}
38	\label{fig:dirichlet_overlay}
39	\end{figure}
40	
41	\paragraph{Theory-MC agreement.}
42	Analytical probability limits match Monte Carlo estimates with mean absolute percentage error (MAPE) of 1.6\%, averaged across 161 scenarios (23 LLM configurations $\times$ 7 topologies; per-topology range: 0.3\%--3.7\%), validating the closed-form derivations and justifying probability limits as practical bias diagnostics.
43	
44	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
45	Under realistic accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; at diagonal $\geq 0.9$, violation persists at 11.9\% (Appendix~\ref{sec:iv_dirichlet_subspace}). Under the full Dirichlet prior, 85\% of matrices violate the binary ``toward-null'' guarantee and 83.4\% cause sign reversal; $\min_k C_{kk} < 0.55$ predicts sign reversal with 91\% accuracy (Appendix~\ref{sec:sign_determinants}). The $K{=}2$ control confirms classical attenuation~\cite{brenner1993}. This establishes the multi-class failure as structurally distinct.
46	
47	\paragraph{Structural guarantee for non-exposure topologies.}
48	Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\ref{conj:monotone}); M-bias shows weakest sensitivity (53.2\% violation). All patterns persist at $K{=}5,7$ (Appendix~\ref{sec:cross_k_robustness}).
49	
50	\paragraph{IV: Wald estimator instability.}
51	The IV topology is the sole non-exposure exception: 52.6\% of random matrices cause sign reversal, stable across $K{=}3,5,7$. Diagonal dominance ($C_{kk} > 0.5$) eliminates sign reversal but preserves amplification (Appendix~\ref{sec:iv_dirichlet_subspace}); however, all 23 empirical LLM configurations show zero IV sign reversal.
52	
53	Figure~\ref{fig:dirichlet_overlay} overlays all 23 empirical LLM configurations onto the theoretical violation-rate curves; real-world accuracy ($\min_k C_{kk} \geq 0.6$) places all models in the low-risk region for IV but leaves exposure vulnerable.
54	
55	\subsection{ASV Framework Validation}
56	\label{sec:asv_results}
57	
58	\begin{table}[t]
59	\centering
60	\small
61	\caption{ASV summary across topologies ($K{=}3$, $\tau{=}0.5$). ---: not applicable.}
62	\label{tab:asv_summary}
63	\begin{tabular}{lccc}
64	\toprule
65	\textbf{Topology} & \textbf{Mag ASV} & \textbf{Power} & \textbf{Sign-flip} \\
66	\midrule
67	IV          & 0.10--0.61 & 0\%   & 1.1--6.7 \\
68	Front-door  & 0.06--0.39 & 100\% & --- \\
69	Confounding & 0.08--0.49 & 100\% & --- \\
70	Mediation   & 0.08--0.45 & 0\%   & --- \\
71	Collider    & 0.34--2.03 & 0\%   & --- \\
72	M-bias      & $\infty$   & 98\%  & --- \\
73	Exposure    & ---        & ---   & 83.4\% \\
74	\bottomrule
75	\end{tabular}
76	\end{table}
77	
78	\paragraph{ASV results.}
79	The ASV envelope is $\varepsilon$-approximately monotonic ($\varepsilon < 0.02$; Conjecture~\ref{conj:monotone}); IV is maximally fragile, M-bias is immune ($\text{ASV} = \infty$; Figure~\ref{fig:asv_ranking}). Sign-flip ASV: 83.4\% of exposure matrices yield $\delta^*_{\text{sf}} < 1$; IV ranges 1.1--6.7 (Table~\ref{tab:asv_summary}). Significance ASV exhibits a phase transition at $N^* \approx 6{,}000$--$10{,}000$; bootstrap CIs (Appendix~\ref{sec:bootstrap_asv},~\ref{sec:c_robustness}) confirm stable topology ranking, with the safe/fragile partition recovering from $n_{\text{gold}} \geq 100$ (82\% stability; Appendix~\ref{sec:asv_diagnostics},~\ref{sec:asv_case_study}).
80	
81	\subsection{Empirical Validation}
82	\label{sec:empirical}
83	
84	We validate using real LLM confusion matrices from HumAID~\cite{alam2021humaid} ($K{=}10$), VAST ($K{=}3$), and CivilComments ($K{=}2$): four LLMs, 23 configurations, 161 bias scenarios. HumAID ($K{=}10$) matches predictions: IV (12.4--42.1\%) and exposure (9.0--17.4\%) dominate; remaining topologies $<$15\%. $F_1$ does not exhibit significant rank correlation with bias ($\rho = -0.10$, $p = 0.45$; Figure~\ref{fig:f1_vs_bias}), but per-topology patterns diverge ($\rho \leq -0.53$ for five topologies vs.\ $0.87$ for M-bias; Appendix~\ref{sec:within_topo_f1}). Of exposure coefficients, 14/23 (61\%) exhibit sign reversal, all secondary; zero across 138 non-exposure scenarios.
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=\columnwidth]{fig5_f1_vs_bias.pdf}
89	\caption{Topology determines downstream causal bias, not $F_1$. HumAID $K{=}10$ (56 points): within $F_1$ range 0.614--0.690, bias varies $10{\times}$ (IV 42.1\% vs.\ collider $<$5.6\%).}
90	\label{fig:f1_vs_bias}
91	\end{figure}
92	
93	\subsection{Correction Guidance}
94	\label{sec:correction}
95	
96	We evaluate five correction methods (naive plug-in, maximum likelihood adjustment (MLA), design-based supervised learning (DSL)~\cite{egami_hinck_stewart_wei2023}, Monte Carlo simulation extrapolation (MC-SIMEX)~\cite{kuchenhoff2006simex}, PPI++~\cite{angelopoulos2023}) across all topologies (210 configurations; Table~\ref{tab:correction}, Appendix~\ref{app:supplementary}).
97	
98	\paragraph{FWL invariance.}
99	Under linear regression, FWL invariance renders matrix-based methods (naive plug-in, MLA) provably ineffective for covariate topologies (0\% bias reduction; Appendix~\ref{app:fwl_proof}): the treatment coefficient depends only on the projection orthogonal to the covariate space, so relabeling $A^* \to A$ leaves the coefficient unchanged. Under logistic regression this invariance breaks, but the method ranking persists ($|\Delta| < 0.02$; Appendix~\ref{sec:fwl_nonlinear}).
100	
101	\begin{figure}[t]
102	\centering
103	\includegraphics[width=\columnwidth]{fig4_binarization.pdf}
104	\caption{Binarization collapse $\Delta$: additional bias from collapsing $K{=}3$ to binary. Topology determines severity ($>$150$\times$ range); exposure and IV exhibit sign flips.}
105	\label{fig:binarization}
106	\end{figure}
107	
108	\paragraph{Method ranking and decision procedure.}
109	PPI++ achieves the highest root mean squared error (RMSE) reduction (47.0\% at $K{=}3$) but requires gold labels (Appendix~\ref{sec:ppi_gold_ratio}) and harms M-bias ($-$88\%); MC-SIMEX is gold-free and $K$-robust (27--70\%), though it harms front-door ($-$62.4\%); rankings are stable across $K$ ($\rho \geq 0.80$; Appendix~\ref{sec:correction_k_sensitivity}). Algorithm~\ref{alg:correction} routes through risk assessment, method selection, and FWL screening. End-to-end demos (Appendix~\ref{sec:e2e_demo},~\ref{sec:real_cm_demo},~\ref{app:case_study}) validate: PPI++ reduces exposure bias from 42.9\% to 0.2\%, while topology-agnostic IV correction amplifies bias ($-$139\%). Collapsing $K{=}3$ to binary is not a safe fallback: the additional bias $\Delta$ varies $>$150$\times$ by topology (Figure~\ref{fig:binarization}; Appendix~\ref{app:binarization}).
110	
111	\begin{algorithm}[t]
112	\caption{Correction method selection for LLM-annotated causal inference.}
113	\label{alg:correction}
114	\footnotesize
115	\begin{algorithmic}[1]
116	\REQUIRE DAG topology $\mathcal{T}$, gold-label availability $G \in \{\textsc{yes}, \textsc{no}\}$
117	\ENSURE Recommended method $M$, risk level $R$
118	\STATE \textbf{Step 1: Risk assessment} \COMMENT{If $\mathcal{T}$ uncertain, repeat per candidate}
119	\STATE $R \gets$ \textsc{Low} if M-bias; \textsc{Med} if Conf/Med/Coll/FD; \textsc{High} if Exp/IV
120	\STATE \textbf{Step 2: Method selection}
121	\IF{$G = \textsc{yes}$}
122	    \STATE $M \gets \text{PPI++}$ (47\% RMSE red.) except M-bias $\to$ \textsc{None} ($-$88\%)
123	\ELSE
124	    \STATE $M \gets \text{DSL}$ if Conf/Med; \text{MC-SIMEX} if IV/Coll/M-bias; $\emptyset$ otherwise
125	\ENDIF
126	\STATE \textbf{Step 3: FWL screening}
127	\IF{$\mathcal{T} \in \{\text{Conf., Med., Coll., M-bias}\}$}
128	    \STATE Skip Naive plug-in and MLA \COMMENT{0\% bias red.\ on $T$}
129	\ENDIF
130	\RETURN $(M, R)$
131	\end{algorithmic}
132	\end{algorithm}
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dbd6b2a-a66f-42e5-9729-3ca00cb47fd5",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a63b50c90ee8743e8",
  "type": "user",
  "uuid": "60a3deed-d81a-49d9-a34d-9f52648b58e4",
  "sourceToolAssistantUUID": "6dbd6b2a-a66f-42e5-9729-3ca00cb47fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T20:12:03.383Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VszqL3u6YJzxZghCAuhUoC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60a3deed-d81a-49d9-a34d-9f52648b58e4",
  "isSidechain": true,
  "agentId": "a63b50c90ee8743e8",
  "requestId": "req_011CbPtxX5Yi2QX7TBSs283U",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "afa9c025-62cf-4274-8f5f-96f446c9f07b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ro5KRg6Z39DHbu6iP55xiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 10 · 2026-05-25T20:12:03.390Z_

<details><summary>↩ Tool result · `toolu_01VszqL3u6YJzxZghCAuhUoC`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: at $K{\geq}3$, exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs provide a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective for four topologies (FWL invariance). Practitioners should identify the topology first: for exposure, PPI++ reduces bias from ${\sim}61\%$ to ${<}1\%$ (Table~\ref{tab:e2e-real-cm}); for IV, topology-agnostic correction can amplify bias ($-$139\% in our demo; Table~\ref{tab:e2e-demo}). High $F_1$ does not guarantee low causal bias; topology assessment must precede downstream inference.
5	
6	The practical workflow we recommend is: (1)~draw the DAG and locate the annotated variable, (2)~compute ASVs to quantify vulnerability, (3)~apply Algorithm~\ref{alg:correction} for topology-aware method selection, and (4)~report ASV confidence intervals alongside effect estimates. This pipeline requires only a gold-label subsample and the confusion matrix---resources already available in most LLM annotation workflows.
7	
8	Our framework opens several directions. Extending the analysis to \emph{differential} misclassification---where error rates depend on $Y$ or covariates---would cover settings where annotator difficulty correlates with outcome severity. Nonlinear identification strategies (matching, doubly robust estimation) break the FWL invariance that underlies our correction routing; characterizing which topologies remain tractable under nonlinear models is an important next step. Proving Conjecture~\ref{conj:monotone} for general $K$ would place the ASV framework on exact rather than $\varepsilon$-approximate foundations.
9	
10	\section*{Limitations}
11	
12	Our closed-form results assume linear SEMs with proportional effects ($f{=}\lambda g$); sign preservation empirically holds at 97.3\% under non-proportional effects (Appendix~\ref{sec:proportional_real_matrices}), but recommendations do not directly extend to nonlinear models (matching, doubly-robust). The framework assumes a known DAG with non-differential misclassification (Appendix~\ref{sec:nondiff_stress},~\ref{sec:realistic_epsilon}); DAG misspecification under measurement error may compound bias. ASV computation requires gold labels for $C^{-1}$; error propagation under small gold-label budgets ($<$500) and general $K{\geq}3$ envelope monotonicity (Conjecture~\ref{conj:monotone}) remain open.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afa9c025-62cf-4274-8f5f-96f446c9f07b",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a63b50c90ee8743e8",
  "type": "user",
  "uuid": "265e4eb0-8e89-4151-aaa6-a3659db9cde2",
  "sourceToolAssistantUUID": "afa9c025-62cf-4274-8f5f-96f446c9f07b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T20:12:03.621Z_

<details open><summary>🔧 Tool call — Read · `toolu_018sLggrmqb2epNjD9ArXyQe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "265e4eb0-8e89-4151-aaa6-a3659db9cde2",
  "isSidechain": true,
  "agentId": "a63b50c90ee8743e8",
  "requestId": "req_011CbPtxX5Yi2QX7TBSs283U",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9b033bf5-4638-443f-b54c-be417b08a06d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ro5KRg6Z39DHbu6iP55xiH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 35175,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 736
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 35175,
          "cache_creation_input_tokens": 736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 736,
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

_source line 12 · 2026-05-25T20:12:03.630Z_

<details><summary>↩ Tool result · `toolu_018sLggrmqb2epNjD9ArXyQe`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one (column-stochastic: each column gives the distribution of predicted labels for a given true label). Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\paragraph{Notation conventions.}
10	Our analysis characterizes probability limits ($N \to \infty$) under the FWL theorem~\cite{frisch1933partial}, which explains why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}). Notation is collected in Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}).
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	In batch annotation pipelines, the LLM processes each text independently without access to $Y$, making non-differentiality an architectural invariant~\cite{ziems2024can}; Y-stratified permutation tests confirm this (1/12 rejection at $\alpha{=}0.05$; Appendix~\ref{sec:nondiff_verify},~\ref{sec:y_stratified_test}). Non-differentiality may be violated when $Y$ correlates with text content, in which case our Y-stratified test provides empirical verification. Under stress testing, sign reversal occurs in 14/16 $K{\geq}3$ exposure configurations at $\eta{=}0.01$ structured departure (Appendix~\ref{sec:nondiff_stress}).
18	
19	Throughout, $\tau$ denotes the causal estimand of interest, whose definition varies by topology: the confounder's coefficient, the treatment effect, the indirect effect, or the Wald ratio (Appendix~\ref{app:confounding}ff.).
20	
21	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009, hernan2020causal}, deriving probability limits under linear structural equation models (SEMs)~\cite{carroll2006}; logistic regression robustness is verified in Appendix~\ref{sec:logistic_dgp} and~\ref{sec:fwl_nonlinear}.
22	
23	\begin{figure*}[t]
24	\centering
25	\includegraphics[width=\textwidth]{fig2_bias_distribution.pdf}
26	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices (uniform Dirichlet; realistic-accuracy results in Section~\ref{sec:taxonomy_results}). Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
27	\label{fig:bias_distribution}
28	\end{figure*}
29	
30	\subsection{Multi-Class Bias Expressions}
31	\label{sec:bias_expressions}
32	
33	For each topology, we derive the $\operatorname{plim}$\footnote{The probability limit (plim) is the value to which an estimator converges as sample size $N \to \infty$; it characterizes systematic bias separately from sampling variability.} of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter, whose precise definition is topology-specific (e.g., the coefficient on $X$ for confounding, the category-specific $\beta_j$ for exposure, or the direct effect $\tau_{\text{direct}}$ for mediation), and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
34	
35	\paragraph{Confounding ($A$ = confounder).}
36	When $A$ confounds the $X{\to}Y$ relationship, the ordinary least squares (OLS) estimator controlling for $A^*$ has probability limit
37	\begin{equation}
38	\label{eq:confounding}
39	\operatorname{plim}\;\hat{\tau}(A^*) = \bigl(\mathbb{E}[Z^{\prime}Z]\bigr)^{-1}\mathbb{E}[Z^{\prime}X]\,\boldsymbol{\beta},
40	\end{equation}
41	where $Z = [X, \text{dummies}(A^*)]$, $\boldsymbol{\beta}$ contains the true coefficients, and the target parameter $\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\hat{\tau}$ is preserved: $\tau_{\text{sign\_flip}} = 0$ structurally.\footnote{Consistent with \citet{brenner1993}: misclassification degrades confounding control, producing amplification ($|\hat{\tau}| > |\tau|$, universal in this topology) but never sign reversal ($\operatorname{sign}(\hat{\tau}) \neq \operatorname{sign}(\tau)$).}
42	
43	\paragraph{Exposure ($A$ = treatment variable).}
44	When $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:
45	\begin{equation}
46	\label{eq:exposure}
47	\operatorname{plim}\;\hat{\beta}_j(A^*) = \sum_{k=1}^{K} w_{jk}\,\beta_k,
48	\end{equation}
49	where $w_{jk}$ depends on the confusion matrix $C$ and the population marginal $\pi_k = P(A{=}k)$. Unlike binary misclassification~\cite{brenner1993}, $K{\geq}3$ permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \emph{sign reversal} (83.4\% under uniform Dirichlet prior); this is structurally impossible at $K{=}2$.
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=\textwidth]{fig3_asv_ranking.pdf}
54	\caption{ASV vulnerability ranking across topologies. Three ASV types (magnitude, significance, sign-flip) reveal a topology-dependent spectrum from IV (maximally fragile) to M-bias (immune, ASV $= \infty$).}
55	\label{fig:asv_ranking}
56	\end{figure*}
57	
58	\paragraph{Primary coefficient preservation.}
59	Across 23 empirical LLM configurations, the primary coefficient (the category with the largest true effect $|\beta_k|$) never reverses sign, while 61\% reverse a secondary (non-dominant) coefficient, confirmed under 100{,}000 Dirichlet matrices with diagonal ${\geq}\,0.7$ across six beta-ratio conditions (1.0 to 50.0) with 0\% primary sign-flip (Appendix~\ref{app:exposure}).
60	
61	\paragraph{Mediation ($A$ = mediator).}
62	When $A$ mediates the $X{\to}Y$ relationship~\cite{vanderweele2015explanation}, the direct effect estimator controlling for $A^*$ has probability limit
63	\begin{equation}
64	\label{eq:mediation}
65	\operatorname{plim}\;\hat{\tau}_{\text{direct}}(A^*) = \tau_{\text{direct}} + \bigl(1 - \lambda(C)\bigr)\,\tau_{\text{indirect}},
66	\end{equation}
67	where $\lambda(C) \in [0,1]$ under proportional effects (Appendix~\ref{app:mediation}, Proposition~\ref{prop:lambda_bound}), with $\lambda(I) = 1$ under perfect classification. Misclassification ($\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\hat{\tau}_{\text{direct}}|$ but preserving the sign ($\tau_{\text{sign\_flip}} = 0$).
68	
69	\paragraph{Collider, M-bias, and front-door.}
70	Three topologies exhibit protective or immune behavior. \textbf{Collider:} conditioning on $A^*$ instead of $A$ attenuates Berkson bias by weakening the spurious path, so annotation error is protective ($\tau_{\text{sign\_flip}} = 0$). \textbf{M-bias:} in the M-shaped DAG~\cite{greenland2003}, misclassifying $A$ attenuates the non-causal path, making this topology immune ($\text{ASV} = \infty$). \textbf{Front-door:} the front-door estimator~\cite{bellemare_bloem2024} requires two stages ($X \to A$ and $A \to Y$), each attenuated by $C$; the compound effect produces moderate bias with $\tau_{\text{sign\_flip}} = 0$ (Appendix~\ref{app:frontdoor}).
71	
72	\paragraph{Instrumental variable ($A$ = instrument).}
73	The Wald estimator~\cite{angrist_imbens1995} $\hat{\tau}_{\text{IV}} = \hat{\text{cov}}(A^*, Y) / \hat{\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign; under random Dirichlet matrices, 52.6\% produce sign reversal; IV is the most fragile topology (Appendix~\ref{sec:iv_dirichlet_subspace}).
74	
75	\paragraph{Structural sign-flip guarantee.}
76	\begin{proposition}[Sign preservation: analytic results]
77	\label{prop:signflip}
78	Under non-differential misclassification with $C_{kk} > 0$ for all $k$:
79	\emph{(a)}~Confounding preserves sign when $\operatorname{sign}(\tau) = \operatorname{sign}(\tau {+} B_{\mathrm{OV}})$, where $B_{\mathrm{OV}} {=} \operatorname{Cov}(g(A),f(A))/\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\ref{app:confounding}).
80	\emph{(b)}~Collider preserves sign when $|\tau| > \sqrt{\operatorname{Var}(g)\operatorname{Var}(h)}/\mathbb{E}[\operatorname{Var}(T{\mid}A)]$ (Berkson attenuation; Appendix~\ref{app:collider}); empirically verified across 100{,}000 matrices with zero violations.
81	\emph{(c)}~Exposure can produce sign reversal for $K {\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\ref{app:exposure}).
82	\end{proposition}
83	
84	Sign preservation for non-exposure topologies holds under topology-specific conditions (Table~\ref{tab:sign_conditions}, Appendix~\ref{app:conditions}), verified across 100{,}000 random matrices with zero violations; analytic proofs for general $K$ remain open.
85	
86	\subsection{Annotation Sensitivity Values}
87	\label{sec:asv}
88	
89	We adapt the sensitivity analysis paradigm (E-values~\cite{vanderweele_ding2017}, partial-$R^2$ bounds~\cite{cinelli2020making}, coefficient stability~\cite{oster2019}) to $K{\times}K$ annotation error and define Annotation Sensitivity Values (ASVs): we prove $\varepsilon$-approximate monotonicity along $C(\delta)$ (Theorem~\ref{thm:monotone}), which reduces $K^2$ dimensions to a scalar; define three ASV diagnostics for topology-dependent failure modes; and combine ASVs with FWL invariance to route corrections.
90	
91	\paragraph{Parameterization.}
92	We set $C(\delta) = (1{-}\delta)I + \delta C_0$, where $C_0$ is a reference confusion matrix and $\delta \in [0,1]$ controls severity ($\delta{=}0$: perfect; $\delta{=}1$: matches $C_0$). This linear path is one of many in the column-stochastic polytope from $I$ to $C_0$; ASV thresholds are path-dependent, but our bootstrap procedure (Section~\ref{sec:asv_results}) captures estimation uncertainty along the empirical path. We recommend bootstrapping $C_0$ and reporting ASV confidence intervals (Appendix~\ref{sec:bootstrap_asv}).
93	\paragraph{Three ASV types.}
94	We define three complementary measures: (1)~\textbf{Magnitude ASV} $\delta^*_{\text{mag}} = \min\{\delta : |\operatorname{plim}\;\hat{\tau}(C(\delta)) - \tau| > \epsilon\}$, analogous to E-values; (2)~\textbf{Significance ASV} $\delta^*_{\text{sig}} = \min\{\delta : |\operatorname{plim}\;\hat{\tau}(C(\delta))| < z_{\alpha/2} \cdot SE(N)\}$, relevant for attenuating topologies; (3)~\textbf{Sign-flip ASV} $\delta^*_{\text{sf}} = \min\{\delta : \operatorname{sign}(\hat{\tau}) \neq \operatorname{sign}(\tau)\}$, for exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.
95	
96	\begin{theorem}[Envelope monotonicity, $K{=}2$]
97	\label{thm:monotone}
98	For $K{=}2$ confounding and mediation topologies with proportional effects ($f = \lambda g$ for some scalar $\lambda$) under $C(\delta) = (1{-}\delta)I + \delta C_0$ with $(C_0)_{jj} \geq \tfrac{1}{2}$, $|B(C(\delta))|$ is monotonically non-decreasing in $\delta \in [0,1]$.
99	\end{theorem}
100	
101	The proof (Appendix~\ref{app:monotonicity_proof},~\ref{par:med_monotone}) exploits perspective function convexity. All 23 empirical configurations preserve sign; 97.3\% do so under non-proportional effects (Appendix~\ref{sec:proportional_effects}).
102	
103	\begin{theorem}[$K{=}3$ symmetric monotonicity]
104	\label{thm:k3_symmetric}
105	For $K{=}3$ with symmetric confusion matrix $C_{jk} = c$ for $j \neq k$ and $C_{kk} = 1{-}2c$, $c \in (0, 1/3)$, and proportional effects ($f{=}\lambda g$), envelope monotonicity holds exactly: $|B(C(\delta))|$ is strictly monotone in $\delta$ for confounding, mediation, and collider topologies whenever $\mathrm{Var}(g) > 0$.
106	\end{theorem}
107	
108	Theorem~\ref{thm:k3_symmetric} anchors exact monotonicity at $K{=}3$; for general asymmetric matrices ($d_{\mathrm{rel}}{=}0.33$; Remark~\ref{rem:symmetry}), Conjecture~\ref{conj:monotone} provides $\varepsilon < 0.017$ coverage. The proof exploits the reduction $s = c\delta$ (Appendix~\ref{app:k3_symmetric_proof}).
109	
110	\paragraph{From proofs to numerical evidence.}
111	Exact monotonicity (Theorems~\ref{thm:monotone}--\ref{thm:k3_symmetric}) does not extend to general $K{\geq}3$ column-stochastic structures; we state a conjecture supported by numerical evidence:
112	
113	\begin{conjecture}[$\varepsilon$-approximate envelope monotonicity]
114	\label{conj:monotone}
115	For general $K{\geq}3$ non-IV topologies under $C(\delta) = (1{-}\delta)I + \delta C_0$, $|B(C(\delta))|$ is $\varepsilon$-approximately monotonic with $\varepsilon < 0.02$ for $|\beta| \leq 1$, scaling with effect magnitude (Table~\ref{tab:conjecture_verify},~\ref{tab:dgp_sensitivity}; Appendix~\ref{sec:conjecture_verify}). The safe/fragile partition (five sign-preserving topologies versus exposure and IV) is robust across all tested parameterizations.
116	\end{conjecture}
117	
118	Numerical support spans 100{,}000 Dirichlet matrices and 545{,}945 adversarial curves (Appendix~\ref{app:adversarial_monotonicity}).
119	
120	\begin{remark}[ASV and E-values as complementary tools]
121	\label{rem:evalue}
122	ASV and E-values~\cite{vanderweele_ding2017} address orthogonal sources (annotation error vs.\ unmeasured confounding; Appendix~\ref{sec:sensitivity_comparison}) and are most valuable jointly.
123	\end{remark}
124	
125	Under alternating-sign effects ($\boldsymbol{\beta}{=}[0,\,1.0,\,-0.5]$), magnitude ASV ranges from 0.09 (exposure) to $\infty$ (M-bias), a $4{\times}$ difference determined by topology (Table~\ref{tab:asv_stability}). Sign-flip ASV $< 1$ flags sign-reversal-prone pairs; magnitude ASV $< \delta_{\text{observed}}$ indicates bias exceeds tolerance (Algorithm~\ref{alg:correction}); the safe/fragile partition is stable across parameterizations ($\varepsilon < 0.02$; Appendix~\ref{sec:asv_stability}).
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b033bf5-4638-443f-b54c-be417b08a06d",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a63b50c90ee8743e8",
  "type": "user",
  "uuid": "5561c751-3ec0-405d-8dea-73833c61916c",
  "sourceToolAssistantUUID": "9b033bf5-4638-443f-b54c-be417b08a06d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-25T20:12:40.386Z_

Now I'll extract all numerical claims systematically. Let me organize the findings by file:

## NUMERICAL CLAIMS EXTRACTION

### abstract.tex

1. [abstract.tex:2] "K ≥ 3 introduces a structural possibility of sign reversal" → **K ≥ 3**
2. [abstract.tex:2] "sign reversal is confined to exposure topology" → **exposure topology only** (implicit count)
3. [abstract.tex:2] "topology-aware correction reduces exposure bias from ∼61% to <1%" → **61% → <1%**
4. [abstract.tex:2] "four topologies due to Frisch--Waugh--Lovell invariance" → **4 topologies**

### introduction.tex

5. [introduction.tex:4] "3--4 categories, sentiment: 5, disaster response: 10+" → **3, 4, 5, 10+**
6. [introduction.tex:4] "31% of hypotheses yield incorrect conclusions with state-of-the-art LLMs" → **31%**
7. [introduction.tex:4] "60% error correlation across models" → **60%**
8. [introduction.tex:4] "within F₁ 0.61--0.69, causal bias varies by an order of magnitude across topologies" → **0.61--0.69 (F₁ range)**
9. [introduction.tex:5] "83.4% of K=3 exposure confusion matrices produce sign reversal of at least one secondary coefficient" → **83.4%**
10. [introduction.tex:5] "under realistic accuracy (diagonal ≥ 0.7), 2.1% still do" → **2.1%**
11. [introduction.tex:6] "ρ = -0.10, p = 0.45 across 56 HumAID scenarios" → **ρ = -0.10, p = 0.45, 56 scenarios**
12. [introduction.tex:6] "bias varies >10× (from <6% to 42.1%) within F₁ 0.614--0.690" → **>10× variation, 6%, 42.1%, F₁ 0.614--0.690**
13. [introduction.tex:8] "analytical predictions matching Monte Carlo within 1.6% MAPE across 161 scenarios" → **1.6% MAPE, 161 scenarios**
14. [introduction.tex:13] "five topologies preserve the treatment effect sign" → **5 topologies**
15. [introduction.tex:13] "exposure and IV can reverse it" → **2 topologies (exposure, IV)**

### experiments.tex

16. [experiments.tex:5] "100,000 Dirichlet(1,1,1) matrices" → **100,000 matrices**
17. [experiments.tex:13] "Confounding 100% violation, 0% sign flip, 100% amplification" → **100%, 0%, 100%**
18. [experiments.tex:14] "Exposure 85% violation, 83.4% sign flip, 14.1% amplification" → **85%, 83.4%, 14.1%**
19. [experiments.tex:15] "Mediation 100%, 0%, 100%" → **100%, 0%, 100%**
20. [experiments.tex:16] "Front-door 100%, 0%, 100%" → **100%, 0%, 100%**
21. [experiments.tex:17] "Collider 100%, 0%, 100%" → **100%, 0%, 100%**
22. [experiments.tex:18] "M-bias 53.2% violation, 0% sign flip, 10.4% amplification" → **53.2%, 0%, 10.4%**
23. [experiments.tex:19] "IV 100% violation, 52.6% sign flip, 100% amplification" → **100%, 52.6%, 100%**
24. [experiments.tex:24] "K=5,7 cross-robustness checks" → **K = 5, 7**
25. [experiments.tex:29] "100,000 confusion matrices from Dirichlet(1,1,1) prior; N=10,000 Monte Carlo" → **100,000 matrices, N = 10,000**
26. [experiments.tex:42] "mean absolute percentage error (MAPE) of 1.6% averaged across 161 scenarios (23 LLM configurations × 7 topologies; per-topology range: 0.3%--3.7%)" → **1.6% MAPE, 161 scenarios, 23 LLM configs, 7 topologies, 0.3--3.7% range**
27. [experiments.tex:45] "Under realistic accuracy (diagonal ≥ 0.7), violation rate is 13.7% with 2.1% sign reversal; at diagonal ≥ 0.9, violation persists at 11.9%" → **diagonal ≥ 0.7: 13.7% violation, 2.1% sign flip; diagonal ≥ 0.9: 11.9% violation**
28. [experiments.tex:45] "Under full Dirichlet prior, 85% of matrices violate binary 'toward-null' guarantee and 83.4% cause sign reversal" → **85%, 83.4%**
29. [experiments.tex:45] "min_k C_kk < 0.55 predicts sign reversal with 91% accuracy" → **0.55 threshold, 91% accuracy**
30. [experiments.tex:45] "1.6% MAPE across 161 scenarios" → **1.6% MAPE, 161 scenarios**
31. [experiments.tex:48] "Five topologies exhibit zero sign-flip rate" → **5 topologies, 0% sign flip**
32. [experiments.tex:48] "M-bias shows weakest sensitivity (53.2% violation)" → **53.2%**
33. [experiments.tex:51] "52.6% of random matrices cause sign reversal" → **52.6%**
34. [experiments.tex:51] "all 23 empirical LLM configurations show zero IV sign reversal" → **23 LLM configs, 0% IV sign flip**
35. [experiments.tex:53] "min_k C_kk ≥ 0.6 places all models in low-risk region for IV but leaves exposure vulnerable" → **≥0.6 threshold for IV safety**
36. [experiments.tex:67] "IV 0.10--0.61 magnitude ASV, 0% power, 1.1--6.7 sign-flip ASV" → **0.10--0.61, 0%, 1.1--6.7**
37. [experiments.tex:68] "Front-door 0.06--0.39, 100%, ---" → **0.06--0.39, 100%**
38. [experiments.tex:69] "Confounding 0.08--0.49, 100%, ---" → **0.08--0.49, 100%**
39. [experiments.tex:70] "Mediation 0.08--0.45, 0%, ---" → **0.08--0.45, 0%**
40. [experiments.tex:71] "Collider 0.34--2.03, 0%, ---" → **0.34--2.03, 0%**
41. [experiments.tex:72] "M-bias infinity, 98%, ---" → **∞, 98%**
42. [experiments.tex:73] "Exposure ---, ---, 83.4%" → **83.4%**
43. [experiments.tex:79] "ASV envelope ε-approximately monotonic (ε < 0.02)" → **ε < 0.02**
44. [experiments.tex:79] "Significance ASV exhibits phase transition at N* ≈ 6,000--10,000" → **N* ≈ 6,000--10,000**
45. [experiments.tex:79] "82% stability with n_gold ≥ 100" → **n_gold ≥ 100, 82% stability**
46. [experiments.tex:84] "HumAID (K=10) IV (12.4--42.1%) and exposure (9.0--17.4%)" → **K=10, IV 12.4--42.1%, exposure 9.0--17.4%**
47. [experiments.tex:84] "remaining topologies <15%" → **<15%**
48. [experiments.tex:84] "ρ = -0.10, p = 0.45 (56 HumAID scenarios)" → **ρ = -0.10, p = 0.45, 56 scenarios**
49. [experiments.tex:84] "bias varies 10× (IV 42.1% vs. collider <5.6%) within F₁ range 0.614--0.690" → **10×, 42.1%, <5.6%, F₁ 0.614--0.690**
50. [experiments.tex:84] "14/23 (61%) exposure coefficients exhibit sign reversal" → **14/23, 61%**
51. [experiments.tex:84] "zero across 138 non-exposure scenarios" → **138 scenarios, 0%**
52. [experiments.tex:89] "within F₁ range 0.614--0.690, bias varies 10× (IV 42.1% vs. collider <5.6%)" → **F₁ 0.614--0.690, 10×, 42.1%, 5.6%**
53. [experiments.tex:96] "five correction methods across all topologies (210 configurations)" → **5 methods, 210 configurations**
54. [experiments.tex:99] "0% bias reduction; FWL invariance renders matrix-based methods provably ineffective for covariate topologies" → **0% bias reduction**
55. [experiments.tex:99] "logistic regression method ranking persists (|Δ| < 0.02)" → **|Δ| < 0.02**
56. [experiments.tex:104] ">150× range binarization collapse; exposure and IV exhibit sign flips" → **>150× range**
57. [experiments.tex:109] "PPI++ achieves highest RMSE reduction (47.0% at K=3)" → **47.0% RMSE reduction, K=3**
58. [experiments.tex:109] "harms M-bias (-88%)" → **-88%**
59. [experiments.tex:109] "MC-SIMEX is gold-free and K-robust (27--70%)" → **27--70% range**
60. [experiments.tex:109] "harms front-door (-62.4%)" → **-62.4%**
61. [experiments.tex:109] "rankings stable across K (ρ ≥ 0.80)" → **ρ ≥ 0.80**
62. [experiments.tex:109] "PPI++ reduces exposure bias from 42.9% to 0.2%" → **42.9% → 0.2%**
63. [experiments.tex:109] "topology-agnostic IV correction amplifies bias (-139%)" → **-139%**
64. [experiments.tex:109] "additional bias Δ varies >150× by topology" → **>150× variation**
65. [experiments.tex:122] "PPI++ 47% RMSE reduction except M-bias → None (-88%)" → **47%, -88%**
66. [experiments.tex:124] "MC-SIMEX for IV/Coll/M-bias" → **topology routing**
67. [experiments.tex:128] "0% bias reduction on T" → **0%**

### conclusion.tex

68. [conclusion.tex:4] "at K≥3, exposure and IV can reverse treatment effect signs while five topologies preserve them" → **K≥3, 2 topologies (exposure, IV) reverse, 5 preserve**
69. [conclusion.tex:4] "PPI++ reduces bias from ∼61% to <1%" → **61% → <1%**
70. [conclusion.tex:4] "topology-agnostic correction can amplify bias (-139%)" → **-139%**
71. [conclusion.tex:11] "sign preservation empirically holds at 97.3% under non-proportional effects" → **97.3%**

### method.tex

72. [method.tex:17] "Y-stratified permutation tests confirm this (1/12 rejection at α=0.05)" → **1/12 rejection, α=0.05**
73. [method.tex:17] "sign reversal occurs in 14/16 K≥3 exposure configurations at η=0.01 structured departure" → **14/16 configs, η=0.01**
74. [method.tex:26] "83.4% sign reversal; IV: 52.6%" → **83.4%, 52.6%**
75. [method.tex:49] "83.4% under uniform Dirichlet prior" → **83.4%**
76. [method.tex:59] "61% reverse a secondary coefficient, confirmed under 100,000 Dirichlet matrices with diagonal ≥ 0.7 across six beta-ratio conditions (1.0 to 50.0) with 0% primary sign-flip" → **61%, 100,000 matrices, diagonal ≥ 0.7, 6 beta ratios 1.0--50.0, 0% primary flip**
77. [method.tex:98] "For K=2 confounding and mediation topologies with proportional effects under C(δ)=(1-δ)I+δC₀ with (C₀)_jj ≥ 1/2" → **K=2, threshold ≥ 1/2**
78. [method.tex:101] "All 23 empirical configurations preserve sign; 97.3% do so under non-proportional effects" → **23 configs, 97.3%**
79. [method.tex:105] "For K=3 with symmetric confusion matrix...c ∈ (0, 1/3)" → **K=3, c ∈ (0, 1/3)**
80. [method.tex:108] "d_rel=0.33" → **d_rel = 0.33**
81. [method.tex:108] "ε < 0.017 coverage" → **ε < 0.017**
82. [method.tex:115] "ε < 0.02 for |β| ≤ 1" → **ε < 0.02, |β| ≤ 1**
83. [method.tex:118] "545,945 adversarial curves" → **545,945 curves**
84. [method.tex:125] "magnitude ASV ranges from 0.09 (exposure) to ∞ (M-bias), 4× difference" → **0.09 (exposure), ∞ (M-bias), 4× difference**
85. [method.tex:125] "ε < 0.02" → **ε < 0.02**

---

## Summary

**Total numerical claims extracted: 85**

**Key recurring numbers:**
- **83.4%** — exposure sign reversal rate (appears 6 times across files)
- **52.6%** — IV sign reversal rate (appears 4 times)
- **100,000 matrices** — simulation sample size (appears 3 times)
- **61%** — bias reduction target / secondary coefficient flip rate (appears 3 times)
- **23** — LLM configurations (appears 4 times)
- **161 scenarios** — total test scenarios (appears 3 times)
- **1.6% MAPE** — theory-MC agreement (appears 3 times)
- **47.0%** — PPI++ RMSE reduction (appears 2 times)

All numbers are now tracked with precise file locations, line numbers, and surrounding context for verification against paper claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5561c751-3ec0-405d-8dea-73833c61916c",
  "isSidechain": true,
  "agentId": "a63b50c90ee8743e8",
  "requestId": "req_011CbPtxnVVicz9Lavqfet2i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23b69bcc-9a20-44b5-9420-ed40bd658afb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LafMK3FzeEdhRh8Fup7Xhu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12357,
      "cache_read_input_tokens": 35911,
      "output_tokens": 4009,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12357
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 4009,
          "cache_read_input_tokens": 35911,
          "cache_creation_input_tokens": 12357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12357,
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
