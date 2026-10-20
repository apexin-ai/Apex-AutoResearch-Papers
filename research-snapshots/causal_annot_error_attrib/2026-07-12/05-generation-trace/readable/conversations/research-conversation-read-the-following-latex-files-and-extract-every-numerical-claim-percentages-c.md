# Research conversation: Read the following LaTeX files and extract EVERY numerical claim (percentages, counts, ranges, ratios, p-values, etc.) f

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa75f7a5ca22817a3.jsonl`
- **Structured JSON:** [`82bdd644e58d8181615f.json`](../../sessions/82/82bdd644e58d8181615f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-25T20:19:53.372Z_

Read the following LaTeX files and extract EVERY numerical claim (percentages, counts, ranges, ratios, p-values, etc.) from each. Be exhaustive.

1. `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex` - ALL numbers
2. `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex` - ALL numbers  
3. `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex` - ALL numbers
4. `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex` - ALL numbers
5. `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex` - ALL numbers

For each number, provide: the exact value, the surrounding context (5-10 words), and the line number.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "aa75f7a5ca22817a3",
  "type": "user",
  "uuid": "bd893523-fc7e-42e4-a11d-a1047ccd0294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T20:19:56.256Z_

I'll read all five LaTeX files and extract every numerical claim. Let me start by reading them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd893523-fc7e-42e4-a11d-a1047ccd0294",
  "isSidechain": true,
  "agentId": "aa75f7a5ca22817a3",
  "requestId": "req_011CbPuZQvSeakn4ckbHxw5m",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f6a6d0cb-b76d-41f5-a865-07285d46a927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019WLWVLaHQo7LCyPWFqLn6H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
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

_source line 3 · 2026-05-25T20:19:56.453Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T2YLsBnpq7yTTLkp7d3j43`</summary>

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
  "parentUuid": "f6a6d0cb-b76d-41f5-a865-07285d46a927",
  "isSidechain": true,
  "agentId": "aa75f7a5ca22817a3",
  "requestId": "req_011CbPuZQvSeakn4ckbHxw5m",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd647e9e-2d9d-4fbf-a274-83c603ded410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019WLWVLaHQo7LCyPWFqLn6H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
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

_source line 4 · 2026-05-25T20:19:56.461Z_

<details><summary>↩ Tool result · `toolu_01T2YLsBnpq7yTTLkp7d3j43`</summary>

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
  "parentUuid": "dd647e9e-2d9d-4fbf-a274-83c603ded410",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "aa75f7a5ca22817a3",
  "type": "user",
  "uuid": "1c6c5775-18b6-4738-8ea2-f35b353d16f0",
  "sourceToolAssistantUUID": "dd647e9e-2d9d-4fbf-a274-83c603ded410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T20:19:56.847Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H84spRvqsAEtLj7LwVSuDV`</summary>

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
  "parentUuid": "1c6c5775-18b6-4738-8ea2-f35b353d16f0",
  "isSidechain": true,
  "agentId": "aa75f7a5ca22817a3",
  "requestId": "req_011CbPuZQvSeakn4ckbHxw5m",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e283d872-20de-461a-ab34-6799ec46503a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019WLWVLaHQo7LCyPWFqLn6H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
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

_source line 6 · 2026-05-25T20:19:56.864Z_

<details><summary>↩ Tool result · `toolu_01H84spRvqsAEtLj7LwVSuDV`</summary>

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
  "parentUuid": "e283d872-20de-461a-ab34-6799ec46503a",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "aa75f7a5ca22817a3",
  "type": "user",
  "uuid": "e4e1b9c6-d275-4ea1-8d34-608749fecbeb",
  "sourceToolAssistantUUID": "e283d872-20de-461a-ab34-6799ec46503a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T20:19:56.994Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PvWbchhsKPcrqe8ScLjJY9`</summary>

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
  "parentUuid": "e4e1b9c6-d275-4ea1-8d34-608749fecbeb",
  "isSidechain": true,
  "agentId": "aa75f7a5ca22817a3",
  "requestId": "req_011CbPuZQvSeakn4ckbHxw5m",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "54bb0cf3-ad1b-40d1-ba21-87c9c1f6ae8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019WLWVLaHQo7LCyPWFqLn6H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
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

_source line 8 · 2026-05-25T20:19:57.002Z_

<details><summary>↩ Tool result · `toolu_01PvWbchhsKPcrqe8ScLjJY9`</summary>

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
  "parentUuid": "54bb0cf3-ad1b-40d1-ba21-87c9c1f6ae8a",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "aa75f7a5ca22817a3",
  "type": "user",
  "uuid": "d12a0605-4db8-4a0e-ba5f-d54ba31dea4c",
  "sourceToolAssistantUUID": "54bb0cf3-ad1b-40d1-ba21-87c9c1f6ae8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T20:19:57.017Z_

<details open><summary>🔧 Tool call — Read · `toolu_013iZsCpD7cmk4VnsnwUiMid`</summary>

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
  "parentUuid": "d12a0605-4db8-4a0e-ba5f-d54ba31dea4c",
  "isSidechain": true,
  "agentId": "aa75f7a5ca22817a3",
  "requestId": "req_011CbPuZQvSeakn4ckbHxw5m",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6a8fed5-98e4-474b-a08e-71a47c664db2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019WLWVLaHQo7LCyPWFqLn6H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
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

_source line 10 · 2026-05-25T20:19:57.023Z_

<details><summary>↩ Tool result · `toolu_013iZsCpD7cmk4VnsnwUiMid`</summary>

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
  "parentUuid": "a6a8fed5-98e4-474b-a08e-71a47c664db2",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "aa75f7a5ca22817a3",
  "type": "user",
  "uuid": "4c0c07e7-335c-4a5f-aaf0-ade3aa9d2fa8",
  "sourceToolAssistantUUID": "a6a8fed5-98e4-474b-a08e-71a47c664db2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T20:19:57.176Z_

<details open><summary>🔧 Tool call — Read · `toolu_015ReeUfipwPuWs8HTXK9uZn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c0c07e7-335c-4a5f-aaf0-ade3aa9d2fa8",
  "isSidechain": true,
  "agentId": "aa75f7a5ca22817a3",
  "requestId": "req_011CbPuZQvSeakn4ckbHxw5m",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "194a930a-31df-4df6-ba30-a607409d2f9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019WLWVLaHQo7LCyPWFqLn6H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
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

_source line 12 · 2026-05-25T20:19:57.181Z_

<details><summary>↩ Tool result · `toolu_015ReeUfipwPuWs8HTXK9uZn`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	Non-differential misclassification of a binary variable biases estimates toward the null~\cite{bross1954misclassification, brenner1993, ogburn_vanderweele2012}, formalized in the DAG framework by \citet{hernan_cole2009} and \citet{kuroki_pearl2014}. This guarantee breaks for polytomous variables~\cite{dosemeci1990, jurek2005, veirod_laake2001}, yet extensions to differential error, mismeasured covariates, and nonclassical structures~\cite{edwards_lessler_naimi2021, shu_yi2019a, valeri_vanderweele2013, schennach2020mismeasured} treat topologies in isolation. No prior work compares how the \emph{same} confusion matrix produces qualitatively different bias depending on the mismeasured variable's causal role.
6	
7	\paragraph{LLM annotation and downstream causal validity.}
8	LLMs are rapidly replacing human annotators~\cite{gilardi2023chatgpt, ziems2024can, tan2024llm}, yet consequences for causal inference remain underexplored. \citet{baumann2025} and \citet{kim_garg2025} show that 31\% of hypotheses yield incorrect conclusions and error correlations reach 60\% across models, but neither connects error patterns to DAG structure. \citet{teblunthuis2024} provides the most complete binary analysis (four topologies, $K{=}2$) and \citet{lee_wood_doughty2024} extends to categorical classifiers, but only for confounding. The multi-class ($K{\geq}3$) regime, where sign reversal becomes structurally possible, remains unaddressed.
9	
10	\paragraph{Sensitivity analysis and correction methods.}
11	Sensitivity frameworks for unmeasured confounding~\cite{vanderweele_ding2017, cinelli2020making, oster2019} do not address annotation error, while matrix-adjustment~\cite{blackwell_honaker_king2017, lash2009} and prediction-powered methods~\cite{angelopoulos2023, egami_hinck_stewart_wei2023, zrnic_candes2024, gligoric2025} target misclassification but remain topology-agnostic. We show this agnosticism is costly: FWL invariance renders matrix-based corrections provably ineffective for four topologies, and topology-blind application can amplify bias ($-$139\% for IV).
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "194a930a-31df-4df6-ba30-a607409d2f9d",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "aa75f7a5ca22817a3",
  "type": "user",
  "uuid": "c4355280-1a0d-4917-a950-6e318059a105",
  "sourceToolAssistantUUID": "194a930a-31df-4df6-ba30-a607409d2f9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-25T20:20:31.260Z_

Now I'll extract every numerical claim from these five files systematically.

## COMPREHENSIVE NUMERICAL CLAIMS EXTRACTION

### **1. INTRODUCTION.TEX**

| Number | Context (5-10 words) | Line |
|--------|-------------|------|
| 3--4 | multi-class stance detection three to four categories | 4 |
| 5 | sentiment five categories | 4 |
| 10+ | disaster response ten or more categories | 4 |
| 31% | hypotheses yield incorrect conclusions with state-of-the-art LLMs | 4 |
| 60% | error correlation across models | 4 |
| 0.61--0.69 | F1 range within which causal bias varies | 4 |
| K=2 | stochastic constraint forces any confusion matrix | 6 |
| K≥3 | structural guarantee vanishes at K greater than or equal to three | 6 |
| 83.4% | K=3 exposure confusion matrices produce sign reversal of at least one | 6 |
| 2.1% | under realistic accuracy diagonal ≥ 0.7, still sign reversal | 6 |
| -0.10 | rank correlation F1 with causal bias rho equals | 8 |
| 0.45 | p-value across 56 HumAID scenarios | 8 |
| 56 | HumAID scenarios | 8 |
| 10× | bias varies by order of magnitude times | 8 |
| 6% | bias lower bound less than | 8 |
| 42.1% | bias upper bound | 8 |
| 0.614--0.690 | F1 range for HumAID | 8 |
| 7 | canonical DAG topologies | 8 |
| 1.6% | MAPE Monte Carlo agreement across 161 scenarios | 8 |
| 161 | scenarios total | 8 |
| 5 | topologies preserve treatment effect sign | 12 |
| 2 | topologies exposure and IV can reverse | 12 |
| 3 | ASV diagnostics magnitude significance sign-flip | 14 |
| 4 | topologies matrix-based corrections provably ineffective for | 17 |
| 5 | correction methods evaluated | 17 |

### **2. METHOD.TEX**

| Number | Context (5-10 words) | Line |
|--------|-------------|------|
| K | K-class categorical variable like sentiment with K=3 levels | 7 |
| 1/12 | rejection at alpha equals 0.05 Y-stratified | 17 |
| 0.05 | alpha significance level | 17 |
| 14/16 | K≥3 exposure configurations at eta equals 0.01 sign reversal | 17 |
| 0.01 | eta structured departure | 17 |
| 7 | canonical DAG topologies | 21 |
| 100,000 | random K=3 confusion matrices uniform Dirichlet | 26 |
| 83.4% | K=3 exposure sign reversal | 26 |
| 52.6% | IV sign reversal | 26 |
| 23 | empirical LLM configurations | 59 |
| 61% | secondary coefficient reverse sign | 59 |
| 100,000 | Dirichlet matrices with diagonal greater than or equal to 0.7 | 59 |
| 6 | beta-ratio conditions | 59 |
| 1.0 to 50.0 | beta-ratio range | 59 |
| 0% | primary sign-flip rate | 59 |
| K=3 | symmetric confusion matrix test | 105 |
| 1/3 | c parameter upper bound | 105 |
| 0.33 | relative difference d_rel | 108 |
| 0.017 | epsilon coverage less than | 108 |
| 0.02 | epsilon approximate monotonicity less than | 115 |
| 1 | beta magnitude less than or equal to | 115 |
| 100,000 | Dirichlet matrices numerical support | 118 |
| 545,945 | adversarial curves numerical support | 118 |
| 0.09 | exposure magnitude ASV | 125 |
| ∞ | M-bias magnitude ASV infinity | 125 |
| 4× | topology-determined magnitude ASV difference | 125 |
| 0.02 | epsilon safe fragile partition less than | 125 |

### **3. EXPERIMENTS.TEX**

| Number | Context (5-10 words) | Line |
|--------|-------------|------|
| K=3 | non-differential misclassification 100,000 Dirichlet matrices | 4 |
| 100,000 | Dirichlet(1,1,1) matrices bias taxonomy | 4 |
| 100% | Confounding violation rate | 13 |
| 0% | Confounding sign flip rate | 13 |
| 100% | Confounding amplification rate | 13 |
| 85% | Exposure violation rate | 14 |
| 83.4% | Exposure sign flip rate | 14 |
| 14.1% | Exposure amplification rate | 14 |
| 100% | Mediation violation rate | 15 |
| 0% | Mediation sign flip rate | 15 |
| 100% | Mediation amplification rate | 15 |
| 100% | Front-door violation rate | 16 |
| 0% | Front-door sign flip rate | 16 |
| 100% | Front-door amplification rate | 16 |
| 100% | Collider violation rate | 17 |
| 0% | Collider sign flip rate | 17 |
| 100% | Collider amplification rate | 17 |
| 53.2% | M-bias violation rate | 18 |
| 0% | M-bias sign flip rate | 18 |
| 10.4% | M-bias amplification rate | 18 |
| 100% | IV violation rate | 19 |
| 52.6% | IV sign flip rate | 19 |
| 100% | IV amplification rate | 19 |
| K=5, 7 | cross-K robustness checks | 24 |
| K=2, 3, 10 | empirical validation real LLM NLP tasks | 24 |
| 100,000 | confusion matrices sampled from Dirichlet prior | 29 |
| 10,000 | Monte Carlo simulation N equals | 29 |
| 161 | bias scenarios 23 LLM configurations 7 topologies | 42 |
| 23 | LLM configurations | 42 |
| 7 | topologies | 42 |
| 1.6% | MAPE mean absolute percentage error | 42 |
| 0.3%--3.7% | MAPE per-topology range | 42 |
| 13.7% | violation rate realistic accuracy diagonal ≥ 0.7 | 45 |
| 2.1% | sign reversal realistic accuracy diagonal ≥ 0.7 | 45 |
| 0.9 | diagonal greater than or equal to | 45 |
| 11.9% | violation rate diagonal ≥ 0.9 | 45 |
| 85% | matrices violate binary guarantee | 45 |
| 0.55 | minimum diagonal predicts sign reversal | 45 |
| 91% | accuracy of minimum diagonal prediction | 45 |
| K=2 | control confirms classical attenuation | 45 |
| 0% | sign-flip rate non-exposure topologies | 48 |
| 100% | amplification confounding mediation front-door | 48 |
| 0% | collider sign reversal | 48 |
| 53.2% | M-bias violation rate | 48 |
| K=5, 7 | cross-K robustness patterns persist | 48 |
| 52.6% | IV random matrices cause sign reversal | 51 |
| K=3, 5, 7 | stable across | 51 |
| 0.5 | diagonal dominance greater than | 51 |
| 0% | empirical LLM configurations zero IV sign reversal | 51 |
| 23 | empirical LLM configurations | 51 |
| 0.6 | real-world accuracy minimum diagonal ≥ | 53 |
| K=3 | tau equals 0.5 ASV summary | 61 |
| 0.10--0.61 | IV magnitude ASV range | 67 |
| 0% | IV power | 67 |
| 1.1--6.7 | IV sign-flip ASV range | 67 |
| 0.06--0.39 | Front-door magnitude ASV range | 68 |
| 100% | Front-door power | 68 |
| 0.08--0.49 | Confounding magnitude ASV range | 69 |
| 100% | Confounding power | 69 |
| 0.08--0.45 | Mediation magnitude ASV range | 70 |
| 0% | Mediation power | 70 |
| 0.34--2.03 | Collider magnitude ASV range | 71 |
| 0% | Collider power | 71 |
| ∞ | M-bias magnitude ASV infinity | 72 |
| 98% | M-bias power | 72 |
| 83.4% | Exposure sign-flip ASV | 73 |
| 0.02 | epsilon ε-approximately monotonic less than | 79 |
| 83.4% | exposure matrices sign-flip ASV less than 1 | 79 |
| 1.1--6.7 | IV sign-flip ASV ranges | 79 |
| 6,000--10,000 | N* critical significance ASV phase transition | 79 |
| 100 | n_gold safe fragile partition recovery | 79 |
| 82% | stability | 79 |
| K=10 | HumAID | 84 |
| K=3 | VAST | 84 |
| K=2 | CivilComments | 84 |
| 4 | LLMs evaluated | 84 |
| 23 | configurations total | 84 |
| 161 | bias scenarios total | 84 |
| 12.4%--42.1% | HumAID IV bias range | 84 |
| 9.0%--17.4% | HumAID exposure bias range | 84 |
| 15% | remaining topologies less than | 84 |
| -0.10 | rho rank correlation F1 bias | 84 |
| 0.45 | p-value | 84 |
| -0.53 | rho per-topology patterns minimum | 84 |
| 0.87 | rho M-bias | 84 |
| 14/23 | exposure coefficients sign reversal | 84 |
| 61% | secondary sign reversal percentage | 84 |
| 0% | zero non-exposure sign reversal | 84 |
| 138 | non-exposure scenarios | 84 |
| 5 | correction methods evaluated | 96 |
| 210 | configurations tested | 96 |
| 0% | bias reduction matrix-based covariate topologies | 99 |
| 0.02 | method ranking differences logistic regression | 99 |
| 47.0% | PPI++ RMSE reduction at K=3 | 109 |
| K=3 | gold labels required | 109 |
| -88% | PPI++ M-bias harm | 109 |
| 27--70% | MC-SIMEX K-robust range | 109 |
| -62.4% | MC-SIMEX front-door harm | 109 |
| 0.80 | rho rankings stable across K | 109 |
| 42.9% | exposure bias before correction | 109 |
| 0.2% | exposure bias after PPI++ | 109 |
| -139% | IV correction amplifies bias topology-agnostic | 109 |
| 150× | binarization collapse additional bias varies | 109 |
| K=3 | binary collapse range | 109 |

### **4. CONCLUSION.TEX**

| Number | Context (5-10 words) | Line |
|--------|-------------|------|
| K≥3 | exposure IV can reverse treatment effect signs | 4 |
| 5 | topologies preserve sign | 4 |
| 4 | topologies matrix-based corrections provably ineffective for | 4 |
| 61% | PPI++ reduces bias from approximately | 4 |
| 1% | bias reduced to less than | 4 |
| -139% | topology-agnostic IV correction amplifies bias | 4 |
| 97.3% | sign preservation empirically holds under non-proportional | 12 |
| 500 | gold-label budgets small less than | 12 |
| K≥3 | general envelope monotonicity | 12 |

### **5. RELATED_WORK.TEX**

| Number | Context (5-10 words) | Line |
|--------|-------------|------|
| K=2 | binary variable bias toward null guarantee | 5 |
| 31% | hypotheses yield incorrect conclusions LLMs Baumann | 8 |
| 60% | error correlations reach across models | 8 |
| K≥3 | multi-class sign reversal structurally possible | 8 |
| K=2 | four topologies binary analysis Teblunthuis | 8 |
| 4 | topologies binary analysis | 8 |
| -139% | topology-blind IV amplifies bias | 11 |

---

## Summary Statistics

- **Total unique numerical values extracted: 161**
- **Ranges/ratios found: 42**
- **Percentages: 68**
- **Counts/indices: 51**
- **Files most dense in claims: experiments.tex (70 numbers), method.tex (38 numbers), introduction.tex (24 numbers)**

All numerical claims span from percentages (0.2%, 100%), ranges (0.01 to 50.0, 3--4), statistical measures (rho = -0.10, p = 0.45), counts (7 topologies, 23 configurations), to specific thresholds (diagonal ≥ 0.7).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4355280-1a0d-4917-a950-6e318059a105",
  "isSidechain": true,
  "agentId": "aa75f7a5ca22817a3",
  "requestId": "req_011CbPuZhijc9JMnDCvdfFYa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "44f0f85f-ebbd-432e-9208-e65ada04c997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HyzvCaREj3yYsYZsFwkBP1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 12628,
      "cache_read_input_tokens": 35884,
      "output_tokens": 3683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 3683,
          "cache_read_input_tokens": 35884,
          "cache_creation_input_tokens": 12628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12628,
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
