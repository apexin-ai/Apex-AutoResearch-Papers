# math conjecture1 proof

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_math_conjecture1_proof_20260524T025551.log`
- **Structured JSON:** [`87e63f3d94d684910711.json`](../../sessions/87/87e63f3d94d684910711.json)

## Before a recorded user message

21 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "bdfb90b5-5942-4817-95f0-a206423e2b3e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779607800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3464e2c3-c179-473c-9d01-0a472b48b126",
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
This is a pure mathematics task about proving Conjecture 1 (ε-approximate envelope monotonicity) under diagonally dominant C₀. Let me start by reading the relevant files to understand the mathematical structure.

Let me read the key files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "6ee69a84-d266-4d59-a1f6-ada4341139ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkLWCxmfRm6Zu3w4qJSgty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14352,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14352
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

I'll start by reading all the relevant mathematical source files to understand the existing proof structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "9ad7a3f5-20f4-4c91-af81-03ac72f379c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkLWCxmfRm6Zu3w4qJSgty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14352,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14352
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_016jHEL8mM1b9YtHYux8mbtm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "a4981423-120f-45b8-ba03-3c306655428e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkLWCxmfRm6Zu3w4qJSgty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14352,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14352
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T02:56:04.075Z_

<details><summary>↩ Tool result · reported error · `toolu_016jHEL8mM1b9YtHYux8mbtm`</summary>

```text
File content (46121 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "8bb494a5-2fbc-4cb8-9eb2-86cd29a7b1aa",
  "tool_use_result": "Error: File content (46121 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01RmEmis5zznd9gZXYeNUsML`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "bbe4db90-d65d-4f8c-b1f1-f7d4bd3d354a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkLWCxmfRm6Zu3w4qJSgty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14352,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14352
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-24T02:56:04.788Z_

<details><summary>↩ Tool result · `toolu_01RmEmis5zznd9gZXYeNUsML`</summary>

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
10	Our analysis characterizes probability limits (plim, $N \to \infty$) rather than finite-sample variance. The FWL theorem~\cite{frisch1933partial} guarantees that each regression coefficient equals the coefficient from a simple regression after residualizing all other variables---this is why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}). Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}) collects all notation.
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	In batch annotation pipelines, the LLM processes each text independently without access to $Y$, making non-differentiality an architectural invariant~\cite{ziems2024can}; Y-stratified permutation tests confirm this (1/12 rejection at $\alpha{=}0.05$; Appendix~\ref{sec:y_stratified_test}). Non-differentiality holds when error is label-intrinsic (e.g., vague category boundaries); it may be violated when error depends on features correlated with $Y$, in which case we recommend the Y-stratified test. Under stress testing, sign reversal occurs in 14/16 $K{\geq}3$ exposure configurations at $\varepsilon{=}0.01$ structured departure, with sign-flip rate increasing from 2.0\% to 9.67\% at $\varepsilon{=}0.20$ (Appendix~\ref{sec:nondiff_stress}); formal degradation guarantees under differential misclassification remain an open problem.
18	
19	Throughout, $\tau$ denotes the causal estimand of interest, whose definition varies by topology: the confounder's coefficient, the treatment effect, the indirect effect, or the Wald ratio (Appendix~\ref{app:confounding}ff.).
20	
21	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009, hernan2020causal} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Throughout, we derive probability limits under \emph{linear} structural equation models~\cite{carroll2006}, the standard framework for exact characterization of topology-dependent bias; robustness under logistic regression~\cite{stefanski_carroll1985} is verified in Appendix~\ref{sec:logistic_dgp} and~\ref{sec:fwl_nonlinear}.
22	
23	\subsection{Multi-Class Bias Expressions}
24	\label{sec:bias_expressions}
25	
26	For each topology, we derive the $\text{plim}$\footnote{The probability limit (plim) is the value to which an estimator converges as sample size $N \to \infty$; it characterizes systematic bias separately from sampling variability.} of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter---its precise definition is topology-specific (e.g., the coefficient on $X$ for confounding, the category-specific $\beta_j$ for exposure, or the direct effect $\tau_{\text{direct}}$ for mediation)---and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
27	
28	\paragraph{Confounding ($A$ = confounder).}
29	When $A$ confounds the $X{\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit
30	\begin{equation}
31	\label{eq:confounding}
32	\text{plim}\;\hat{\tau}(A^*) = \bigl(\mathbb{E}[Z^{\prime}Z]\bigr)^{-1}\mathbb{E}[Z^{\prime}X]\,\boldsymbol{\beta},
33	\end{equation}
34	where $Z = [X, \text{dummies}(A^*)]$, $\boldsymbol{\beta}$ contains the true coefficients, and the target parameter $\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\hat{\tau}$ is preserved: $\tau_{\text{sign\_flip}} = 0$ structurally.\footnote{Consistent with \citet{brenner1993}: misclassification degrades confounding control, producing amplification ($|\hat{\tau}| > |\tau|$, universal in this topology) but never sign reversal ($\text{sign}(\hat{\tau}) \neq \text{sign}(\tau)$).}
35	
36	\paragraph{Exposure ($A$ = treatment variable).}
37	When $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:
38	\begin{equation}
39	\label{eq:exposure}
40	\text{plim}\;\hat{\beta}_j(A^*) = \sum_{k=1}^{K} w_{jk}\,\beta_k,
41	\end{equation}
42	where $w_{jk}$ depends on the confusion matrix $C$ and the population marginal $\pi_k = P(A{=}k)$. Unlike the binary case, where non-differential misclassification guarantees attenuation toward the null~\cite{brenner1993}, the $K{\geq}3$ case permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \emph{sign reversal}. A near-permutation confusion matrix effectively swaps category labels, making sign reversal the dominant outcome (83.4\% under uniform Dirichlet prior). This failure mode is structurally impossible at $K{=}2$ because a $2{\times}2$ stochastic matrix with positive diagonal cannot reverse the sign of a single coefficient.
43	
44	\begin{figure*}[t]
45	\centering
46	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
47	\vspace{-6pt}
48	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices (uniform Dirichlet; realistic-accuracy results in Section~\ref{sec:taxonomy_results}). Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
49	\label{fig:bias_distribution}
50	\end{figure*}
51	
52	\paragraph{Numerical Verification 2: Primary coefficient preservation.}
53	Across 23 empirical LLM configurations, the primary coefficient (the category with the largest true effect $|\beta_k|$) never reverses sign, while 61\% reverse a secondary (non-dominant) coefficient---confirmed under 100{,}000 Dirichlet matrices with diagonal ${\geq}\,0.7$ across six beta-ratio conditions (1.0 to 50.0) with 0\% primary sign-flip (Appendix~\ref{app:exposure}).
54	
55	\paragraph{Mediation ($A$ = mediator).}
56	When $A$ mediates the $X{\to}Y$ relationship~\cite{vanderweele2015explanation}, the direct effect estimator controlling for $A^*$ has probability limit
57	\begin{equation}
58	\label{eq:mediation}
59	\text{plim}\;\hat{\tau}_{\text{direct}}(A^*) = \tau_{\text{direct}} + \bigl(1 - \lambda(C)\bigr)\,\tau_{\text{indirect}},
60	\end{equation}
61	where $\lambda(C) \in [0,1]$ under proportional effects (Appendix~\ref{app:proof}, Proposition~\ref{prop:lambda_bound}), with $\lambda(I) = 1$ under perfect classification. Misclassification ($\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\hat{\tau}_{\text{direct}}|$ but preserving the sign ($\tau_{\text{sign\_flip}} = 0$).
62	
63	\paragraph{Collider, M-bias, and front-door.}
64	Three topologies exhibit \emph{protective} or \emph{immune} behavior. \textbf{Collider:} conditioning on $A^*$ instead of $A$ attenuates the spurious path, so annotation error reduces collider bias ($\tau_{\text{sign\_flip}} = 0$). \textbf{M-bias:} in the M-shaped DAG~\cite{greenland2003}, misclassifying $A$ weakens the M-bias path; this topology is immune ($\text{ASV} = \infty$). \textbf{Front-door:} the front-door estimator~\cite{bellemare_bloem2024} is attenuated in both $X \to A$ and $A \to Y$ stages, producing moderate bias with $\tau_{\text{sign\_flip}} = 0$.
65	
66	\paragraph{Instrumental variable ($A$ = instrument).}
67	The Wald estimator~\cite{angrist_imbens1995} $\hat{\tau}_{\text{IV}} = \hat{\text{cov}}(A^*, Y) / \hat{\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign; under random Dirichlet matrices, 52.6\% produce sign reversal, making IV the most fragile topology (Appendix~\ref{sec:iv_dirichlet_subspace}).
68	
69	\paragraph{Structural sign-flip guarantee.}
70	\begin{proposition}[Sign preservation---analytic results]
71	\label{prop:signflip}
72	Under non-differential misclassification with $C_{kk} > 0$ for all $k$:
73	\emph{(a)}~Confounding preserves sign when $\operatorname{sign}(\tau) = \operatorname{sign}(\tau {+} B_{\mathrm{OV}})$, where $B_{\mathrm{OV}} {=} \operatorname{Cov}(g(A),f(A))/\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\ref{app:confounding}).
74	\emph{(b)}~Collider preserves sign when $|\tau| > \sqrt{\operatorname{Var}(g)\operatorname{Var}(h)}/\mathbb{E}[\operatorname{Var}(T{\mid}A)]$ (Berkson attenuation; Appendix~\ref{app:collider}); empirically verified across 100{,}000 matrices with zero violations.
75	\emph{(c)}~Exposure can produce sign reversal for $K {\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\ref{app:exposure}).
76	\end{proposition}
77	
78	Sign preservation for non-exposure topologies holds under topology-specific conditions (Table~\ref{tab:sign_conditions}, Appendix~\ref{app:conditions}), verified across 100{,}000 random matrices with zero violations; analytic proofs for general $K$ remain open.
79	
80	\subsection{Annotation Sensitivity Values}
81	\label{sec:asv}
82	
83	We adapt the sensitivity analysis paradigm---E-values~\cite{vanderweele_ding2017}, partial-$R^2$ bounds~\cite{cinelli2020making}, coefficient stability~\cite{oster2019}---to $K{\times}K$ annotation error, defining Annotation Sensitivity Values (ASVs): we prove $\varepsilon$-approximate monotonicity along $C(\delta)$ (Theorem~\ref{thm:monotone}), reducing $K^2$ dimensions to a scalar; define three ASV diagnostics for topology-dependent failure modes; and combine ASVs with FWL invariance to route corrections.
84	
85	\paragraph{Parameterization.}
86	We set $C(\delta) = (1{-}\delta)I + \delta C_0$, where $C_0$ is a reference confusion matrix and $\delta \in [0,1]$ controls severity ($\delta{=}0$: perfect; $\delta{=}1$: matches $C_0$). This linear path is one of many in the column-stochastic polytope from $I$ to $C_0$; ASV thresholds are path-dependent, but our bootstrap procedure (Section~\ref{sec:asv_results}) captures estimation uncertainty along the empirical path. We recommend bootstrapping $C_0$ and reporting ASV confidence intervals (Appendix~\ref{sec:bootstrap_asv}).
87	\paragraph{Three ASV types.}
88	We define three complementary measures: (1)~\textbf{Magnitude ASV} $\delta^*_{\text{mag}} = \min\{\delta : |\text{plim}\;\hat{\tau}(C(\delta)) - \tau| > \epsilon\}$---analogous to E-values; (2)~\textbf{Significance ASV} $\delta^*_{\text{sig}} = \min\{\delta : |\text{plim}\;\hat{\tau}(C(\delta))| < z_{\alpha/2} \cdot SE(N)\}$---relevant for attenuating topologies; (3)~\textbf{Sign-flip ASV} $\delta^*_{\text{sf}} = \min\{\delta : \text{sign}(\hat{\tau}) \neq \text{sign}(\tau)\}$---exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.
89	
90	\begin{theorem}[Envelope monotonicity---$K{=}2$]
91	\label{thm:monotone}
92	For $K{=}2$ confounding and mediation topologies with proportional effects ($f = \lambda g$ for some scalar $\lambda$) under $C(\delta) = (1{-}\delta)I + \delta C_0$ with $(C_0)_{jj} \geq \tfrac{1}{2}$, $|B(C(\delta))|$ is monotonically non-decreasing in $\delta \in [0,1]$.
93	\end{theorem}
94	
95	The proof (Appendix~\ref{app:monotonicity_proof},~\ref{par:med_monotone}) exploits perspective function convexity; $(C_0)_{jj}{\geq}\tfrac{1}{2}$ excludes degenerate matrices. Proportional effects ($f{=}\lambda g$) is plausible when overall annotation competence drives both paths (e.g., a single quality dimension); it may fail under multi-dimensional asymmetric confusion where different error modes affect $f$ and $g$ differentially. All 23 empirical configurations preserve sign under this assumption, with 97.3\% preserving sign under non-proportional effects (Appendix~\ref{sec:proportional_effects}; Tables~\ref{tab:proportional_effects},~\ref{tab:proportional_empirical}).
96	
97	\begin{theorem}[$K{=}3$ symmetric monotonicity]
98	\label{thm:k3_symmetric}
99	For $K{=}3$ with symmetric confusion matrix $C_{jk} = c$ for $j \neq k$ and $C_{kk} = 1{-}2c$, $c \in (0, 1/3)$, and proportional effects ($f{=}\lambda g$), envelope monotonicity holds exactly: $|B(C(\delta))|$ is strictly monotone in $\delta$ for confounding, mediation, and collider topologies whenever $\mathrm{Var}(g) > 0$.
100	\end{theorem}
101	
102	Theorem~\ref{thm:k3_symmetric} serves as a theoretical anchor: exact monotonicity is achievable at $K{=}3$ under symmetric $C_0$. For general asymmetric matrices (empirical $K{=}3$ median $d_{\mathrm{rel}}{=}0.33$; Remark~\ref{rem:symmetry}), Conjecture~\ref{conj:monotone} provides numerical coverage ($\varepsilon < 0.017$). The proof (Appendix~\ref{app:k3_symmetric_proof}) exploits the one-parameter reduction $s = c\delta$ to show $dV_B/ds < 0$ pointwise; under non-proportional effects, approximate monotonicity holds ($\varepsilon < 0.005$; Appendix~\ref{app:k3_symmetric_proof}, Remark~2).
103	
104	\paragraph{From proofs to numerical evidence.}
105	Theorems~\ref{thm:monotone}--\ref{thm:k3_symmetric} establish exact monotonicity for $K{=}2$ and $K{=}3$ symmetric matrices. The factorization in Appendix~\ref{app:k3_symmetric_proof} exploits off-diagonal symmetry to reduce to univariate analysis---a strategy that does not extend to general $K{\geq}3$ column-stochastic structures. We therefore state a conjecture supported by numerical evidence:
106	
107	\begin{conjecture}[$\varepsilon$-approximate envelope monotonicity]
108	\label{conj:monotone}
109	For general $K{\geq}3$ non-IV topologies under $C(\delta) = (1{-}\delta)I + \delta C_0$, $|B(C(\delta))|$ is $\varepsilon$-approximately monotonic with $\varepsilon < 0.02$ for $|\beta| \leq 1$, scaling with effect magnitude (Table~\ref{tab:conjecture_verify},~\ref{tab:dgp_sensitivity}; Appendix~\ref{sec:conjecture_verify}). The safe/fragile partition---five sign-preserving topologies versus exposure and IV---is robust across all tested parameterizations.
110	\end{conjecture}
111	
112	Conjecture~\ref{conj:monotone} is supported by 100{,}000 Dirichlet-sampled matrices and 545{,}945 adversarial curves across four structural families (Appendix~\ref{app:adversarial_monotonicity}), with maximum observed violation $\varepsilon < 0.017$.
113	
114	\begin{remark}[ASV and E-values as complementary tools]
115	\label{rem:evalue}
116	ASV diagnostics and E-values~\cite{vanderweele_ding2017} address orthogonal bias sources---annotation error vs.\ unmeasured confounding---and are most valuable jointly (Table~\ref{tab:sensitivity_comparison}, Appendix). Key distinctions: ASV is topology-dependent (same $C$ has different consequences across topologies); sign-flip ASV targets a failure mode absent from confounding analysis; ASV searches the column-stochastic polytope while E-values optimize over $[1,\infty)$.
117	\end{remark}
118	
119	Under alternating-sign effects ($\boldsymbol{\beta}{=}[0,\,1.0,\,-0.5]$), magnitude ASV ranges from 0.09 (exposure) to $\infty$ (M-bias), a $4{\times}$ difference determined by topology (Table~\ref{tab:asv_stability}). Sign-flip ASV $< 1$ flags sign-reversal-prone pairs; magnitude ASV $< \delta_{\text{observed}}$ indicates bias exceeds tolerance (Algorithm~\ref{alg:correction}); the safe/fragile partition is stable across parameterizations ($\varepsilon < 0.02$; Appendix~\ref{sec:asv_stability}).
120	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "3490991b-b754-4b66-8cdc-f4e5b2935b38",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Setup and Notation}\n\\label{sec:notation}\n\nLet $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \\mid A{=}k)$, where each column sums to one (column-stochastic: each column gives the distribution of predicted labels for a given true label). Following \\citet{hernan_cole2009}, we represent this measurement process using \\emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.\n\n\\paragraph{Notation conventions.}\nOur analysis characterizes probability limits (plim, $N \\to \\infty$) rather than finite-sample variance. The FWL theorem~\\cite{frisch1933partial} guarantees that each regression coefficient equals the coefficient from a simple regression after residualizing all other variables---this is why matrix-based corrections fail for covariate topologies (Section~\\ref{sec:correction}). Table~\\ref{tab:notation} (Appendix~\\ref{app:notation_table}) collects all notation.\n\n\\begin{definition}[Non-differential misclassification]\n\\label{def:nondiff}\nMisclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\\mathbf{Z}$ if $P(A^*{=}j \\mid A{=}k, Y, \\mathbf{Z}) = P(A^*{=}j \\mid A{=}k) = C_{jk}$ for all $j,k$.\n\\end{definition}\n\nIn batch annotation pipelines, the LLM processes each text independently without access to $Y$, making non-differentiality an architectural invariant~\\cite{ziems2024can}; Y-stratified permutation tests confirm this (1/12 rejection at $\\alpha{=}0.05$; Appendix~\\ref{sec:y_stratified_test}). Non-differentiality holds when error is label-intrinsic (e.g., vague category boundaries); it may be violated when error depends on features correlated with $Y$, in which case we recommend the Y-stratified test. Under stress testing, sign reversal occurs in 14/16 $K{\\geq}3$ exposure configurations at $\\varepsilon{=}0.01$ structured departure, with sign-flip rate increasing from 2.0\\% to 9.67\\% at $\\varepsilon{=}0.20$ (Appendix~\\ref{sec:nondiff_stress}); formal degradation guarantees under differential misclassification remain an open problem.\n\nThroughout, $\\tau$ denotes the causal estimand of interest, whose definition varies by topology: the confounder's coefficient, the treatment effect, the indirect effect, or the Wald ratio (Appendix~\\ref{app:confounding}ff.).\n\nWe study seven canonical DAG topologies (Figure~\\ref{fig:dag_taxonomy})~\\cite{pearl2009, hernan2020causal} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Throughout, we derive probability limits under \\emph{linear} structural equation models~\\cite{carroll2006}, the standard framework for exact characterization of topology-dependent bias; robustness under logistic regression~\\cite{stefanski_carroll1985} is verified in Appendix~\\ref{sec:logistic_dgp} and~\\ref{sec:fwl_nonlinear}.\n\n\\subsection{Multi-Class Bias Expressions}\n\\label{sec:bias_expressions}\n\nFor each topology, we derive the $\\text{plim}$\\footnote{The probability limit (plim) is the value to which an estimator converges as sample size $N \\to \\infty$; it characterizes systematic bias separately from sampling variability.} of the naive estimator that substitutes $A^*$ for $A$. Let $\\tau$ denote the target causal parameter---its precise definition is topology-specific (e.g., the coefficient on $X$ for confounding, the category-specific $\\beta_j$ for exposure, or the direct effect $\\tau_{\\text{direct}}$ for mediation)---and $\\hat{\\tau}(A^*)$ the estimator using misclassified annotations.\n\n\\paragraph{Confounding ($A$ = confounder).}\nWhen $A$ confounds the $X{\\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:confounding}\n\\text{plim}\\;\\hat{\\tau}(A^*) = \\bigl(\\mathbb{E}[Z^{\\prime}Z]\\bigr)^{-1}\\mathbb{E}[Z^{\\prime}X]\\,\\boldsymbol{\\beta},\n\\end{equation}\nwhere $Z = [X, \\text{dummies}(A^*)]$, $\\boldsymbol{\\beta}$ contains the true coefficients, and the target parameter $\\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\\hat{\\tau}$ is preserved: $\\tau_{\\text{sign\\_flip}} = 0$ structurally.\\footnote{Consistent with \\citet{brenner1993}: misclassification degrades confounding control, producing amplification ($|\\hat{\\tau}| > |\\tau|$, universal in this topology) but never sign reversal ($\\text{sign}(\\hat{\\tau}) \\neq \\text{sign}(\\tau)$).}\n\n\\paragraph{Exposure ($A$ = treatment variable).}\nWhen $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:\n\\begin{equation}\n\\label{eq:exposure}\n\\text{plim}\\;\\hat{\\beta}_j(A^*) = \\sum_{k=1}^{K} w_{jk}\\,\\beta_k,\n\\end{equation}\nwhere $w_{jk}$ depends on the confusion matrix $C$ and the population marginal $\\pi_k = P(A{=}k)$. Unlike the binary case, where non-differential misclassification guarantees attenuation toward the null~\\cite{brenner1993}, the $K{\\geq}3$ case permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \\emph{sign reversal}. A near-permutation confusion matrix effectively swaps category labels, making sign reversal the dominant outcome (83.4\\% under uniform Dirichlet prior). This failure mode is structurally impossible at $K{=}2$ because a $2{\\times}2$ stochastic matrix with positive diagonal cannot reverse the sign of a single coefficient.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth,height=0.18\\textheight,keepaspectratio]{fig2_bias_distribution.pdf}\n\\vspace{-6pt}\n\\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices (uniform Dirichlet; realistic-accuracy results in Section~\\ref{sec:taxonomy_results}). Red = sign reversal. Exposure: 83.4\\% sign reversal; IV: 52.6\\%.}\n\\label{fig:bias_distribution}\n\\end{figure*}\n\n\\paragraph{Numerical Verification 2: Primary coefficient preservation.}\nAcross 23 empirical LLM configurations, the primary coefficient (the category with the largest true effect $|\\beta_k|$) never reverses sign, while 61\\% reverse a secondary (non-dominant) coefficient---confirmed under 100{,}000 Dirichlet matrices with diagonal ${\\geq}\\,0.7$ across six beta-ratio conditions (1.0 to 50.0) with 0\\% primary sign-flip (Appendix~\\ref{app:exposure}).\n\n\\paragraph{Mediation ($A$ = mediator).}\nWhen $A$ mediates the $X{\\to}Y$ relationship~\\cite{vanderweele2015explanation}, the direct effect estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:mediation}\n\\text{plim}\\;\\hat{\\tau}_{\\text{direct}}(A^*) = \\tau_{\\text{direct}} + \\bigl(1 - \\lambda(C)\\bigr)\\,\\tau_{\\text{indirect}},\n\\end{equation}\nwhere $\\lambda(C) \\in [0,1]$ under proportional effects (Appendix~\\ref{app:proof}, Proposition~\\ref{prop:lambda_bound}), with $\\lambda(I) = 1$ under perfect classification. Misclassification ($\\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\\hat{\\tau}_{\\text{direct}}|$ but preserving the sign ($\\tau_{\\text{sign\\_flip}} = 0$).\n\n\\paragraph{Collider, M-bias, and front-door.}\nThree topologies exhibit \\emph{protective} or \\emph{immune} behavior. \\textbf{Collider:} conditioning on $A^*$ instead of $A$ attenuates the spurious path, so annotation error reduces collider bias ($\\tau_{\\text{sign\\_flip}} = 0$). \\textbf{M-bias:} in the M-shaped DAG~\\cite{greenland2003}, misclassifying $A$ weakens the M-bias path; this topology is immune ($\\text{ASV} = \\infty$). \\textbf{Front-door:} the front-door estimator~\\cite{bellemare_bloem2024} is attenuated in both $X \\to A$ and $A \\to Y$ stages, producing moderate bias with $\\tau_{\\text{sign\\_flip}} = 0$.\n\n\\paragraph{Instrumental variable ($A$ = instrument).}\nThe Wald estimator~\\cite{angrist_imbens1995} $\\hat{\\tau}_{\\text{IV}} = \\hat{\\text{cov}}(A^*, Y) / \\hat{\\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign; under random Dirichlet matrices, 52.6\\% produce sign reversal, making IV the most fragile topology (Appendix~\\ref{sec:iv_dirichlet_subspace}).\n\n\\paragraph{Structural sign-flip guarantee.}\n\\begin{proposition}[Sign preservation---analytic results]\n\\label{prop:signflip}\nUnder non-differential misclassification with $C_{kk} > 0$ for all $k$:\n\\emph{(a)}~Confounding preserves sign when $\\operatorname{sign}(\\tau) = \\operatorname{sign}(\\tau {+} B_{\\mathrm{OV}})$, where $B_{\\mathrm{OV}} {=} \\operatorname{Cov}(g(A),f(A))/\\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\\ref{app:confounding}).\n\\emph{(b)}~Collider preserves sign when $|\\tau| > \\sqrt{\\operatorname{Var}(g)\\operatorname{Var}(h)}/\\mathbb{E}[\\operatorname{Var}(T{\\mid}A)]$ (Berkson attenuation; Appendix~\\ref{app:collider}); empirically verified across 100{,}000 matrices with zero violations.\n\\emph{(c)}~Exposure can produce sign reversal for $K {\\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\\ref{app:exposure}).\n\\end{proposition}\n\nSign preservation for non-exposure topologies holds under topology-specific conditions (Table~\\ref{tab:sign_conditions}, Appendix~\\ref{app:conditions}), verified across 100{,}000 random matrices with zero violations; analytic proofs for general $K$ remain open.\n\n\\subsection{Annotation Sensitivity Values}\n\\label{sec:asv}\n\nWe adapt the sensitivity analysis paradigm---E-values~\\cite{vanderweele_ding2017}, partial-$R^2$ bounds~\\cite{cinelli2020making}, coefficient stability~\\cite{oster2019}---to $K{\\times}K$ annotation error, defining Annotation Sensitivity Values (ASVs): we prove $\\varepsilon$-approximate monotonicity along $C(\\delta)$ (Theorem~\\ref{thm:monotone}), reducing $K^2$ dimensions to a scalar; define three ASV diagnostics for topology-dependent failure modes; and combine ASVs with FWL invariance to route corrections.\n\n\\paragraph{Parameterization.}\nWe set $C(\\delta) = (1{-}\\delta)I + \\delta C_0$, where $C_0$ is a reference confusion matrix and $\\delta \\in [0,1]$ controls severity ($\\delta{=}0$: perfect; $\\delta{=}1$: matches $C_0$). This linear path is one of many in the column-stochastic polytope from $I$ to $C_0$; ASV thresholds are path-dependent, but our bootstrap procedure (Section~\\ref{sec:asv_results}) captures estimation uncertainty along the empirical path. We recommend bootstrapping $C_0$ and reporting ASV confidence intervals (Appendix~\\ref{sec:bootstrap_asv}).\n\\paragraph{Three ASV types.}\nWe define three complementary measures: (1)~\\textbf{Magnitude ASV} $\\delta^*_{\\text{mag}} = \\min\\{\\delta : |\\text{plim}\\;\\hat{\\tau}(C(\\delta)) - \\tau| > \\epsilon\\}$---analogous to E-values; (2)~\\textbf{Significance ASV} $\\delta^*_{\\text{sig}} = \\min\\{\\delta : |\\text{plim}\\;\\hat{\\tau}(C(\\delta))| < z_{\\alpha/2} \\cdot SE(N)\\}$---relevant for attenuating topologies; (3)~\\textbf{Sign-flip ASV} $\\delta^*_{\\text{sf}} = \\min\\{\\delta : \\text{sign}(\\hat{\\tau}) \\neq \\text{sign}(\\tau)\\}$---exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.\n\n\\begin{theorem}[Envelope monotonicity---$K{=}2$]\n\\label{thm:monotone}\nFor $K{=}2$ confounding and mediation topologies with proportional effects ($f = \\lambda g$ for some scalar $\\lambda$) under $C(\\delta) = (1{-}\\delta)I + \\delta C_0$ with $(C_0)_{jj} \\geq \\tfrac{1}{2}$, $|B(C(\\delta))|$ is monotonically non-decreasing in $\\delta \\in [0,1]$.\n\\end{theorem}\n\nThe proof (Appendix~\\ref{app:monotonicity_proof},~\\ref{par:med_monotone}) exploits perspective function convexity; $(C_0)_{jj}{\\geq}\\tfrac{1}{2}$ excludes degenerate matrices. Proportional effects ($f{=}\\lambda g$) is plausible when overall annotation competence drives both paths (e.g., a single quality dimension); it may fail under multi-dimensional asymmetric confusion where different error modes affect $f$ and $g$ differentially. All 23 empirical configurations preserve sign under this assumption, with 97.3\\% preserving sign under non-proportional effects (Appendix~\\ref{sec:proportional_effects}; Tables~\\ref{tab:proportional_effects},~\\ref{tab:proportional_empirical}).\n\n\\begin{theorem}[$K{=}3$ symmetric monotonicity]\n\\label{thm:k3_symmetric}\nFor $K{=}3$ with symmetric confusion matrix $C_{jk} = c$ for $j \\neq k$ and $C_{kk} = 1{-}2c$, $c \\in (0, 1/3)$, and proportional effects ($f{=}\\lambda g$), envelope monotonicity holds exactly: $|B(C(\\delta))|$ is strictly monotone in $\\delta$ for confounding, mediation, and collider topologies whenever $\\mathrm{Var}(g) > 0$.\n\\end{theorem}\n\nTheorem~\\ref{thm:k3_symmetric} serves as a theoretical anchor: exact monotonicity is achievable at $K{=}3$ under symmetric $C_0$. For general asymmetric matrices (empirical $K{=}3$ median $d_{\\mathrm{rel}}{=}0.33$; Remark~\\ref{rem:symmetry}), Conjecture~\\ref{conj:monotone} provides numerical coverage ($\\varepsilon < 0.017$). The proof (Appendix~\\ref{app:k3_symmetric_proof}) exploits the one-parameter reduction $s = c\\delta$ to show $dV_B/ds < 0$ pointwise; under non-proportional effects, approximate monotonicity holds ($\\varepsilon < 0.005$; Appendix~\\ref{app:k3_symmetric_proof}, Remark~2).\n\n\\paragraph{From proofs to numerical evidence.}\nTheorems~\\ref{thm:monotone}--\\ref{thm:k3_symmetric} establish exact monotonicity for $K{=}2$ and $K{=}3$ symmetric matrices. The factorization in Appendix~\\ref{app:k3_symmetric_proof} exploits off-diagonal symmetry to reduce to univariate analysis---a strategy that does not extend to general $K{\\geq}3$ column-stochastic structures. We therefore state a conjecture supported by numerical evidence:\n\n\\begin{conjecture}[$\\varepsilon$-approximate envelope monotonicity]\n\\label{conj:monotone}\nFor general $K{\\geq}3$ non-IV topologies under $C(\\delta) = (1{-}\\delta)I + \\delta C_0$, $|B(C(\\delta))|$ is $\\varepsilon$-approximately monotonic with $\\varepsilon < 0.02$ for $|\\beta| \\leq 1$, scaling with effect magnitude (Table~\\ref{tab:conjecture_verify},~\\ref{tab:dgp_sensitivity}; Appendix~\\ref{sec:conjecture_verify}). The safe/fragile partition---five sign-preserving topologies versus exposure and IV---is robust across all tested parameterizations.\n\\end{conjecture}\n\nConjecture~\\ref{conj:monotone} is supported by 100{,}000 Dirichlet-sampled matrices and 545{,}945 adversarial curves across four structural families (Appendix~\\ref{app:adversarial_monotonicity}), with maximum observed violation $\\varepsilon < 0.017$.\n\n\\begin{remark}[ASV and E-values as complementary tools]\n\\label{rem:evalue}\nASV diagnostics and E-values~\\cite{vanderweele_ding2017} address orthogonal bias sources---annotation error vs.\\ unmeasured confounding---and are most valuable jointly (Table~\\ref{tab:sensitivity_comparison}, Appendix). Key distinctions: ASV is topology-dependent (same $C$ has different consequences across topologies); sign-flip ASV targets a failure mode absent from confounding analysis; ASV searches the column-stochastic polytope while E-values optimize over $[1,\\infty)$.\n\\end{remark}\n\nUnder alternating-sign effects ($\\boldsymbol{\\beta}{=}[0,\\,1.0,\\,-0.5]$), magnitude ASV ranges from 0.09 (exposure) to $\\infty$ (M-bias), a $4{\\times}$ difference determined by topology (Table~\\ref{tab:asv_stability}). Sign-flip ASV $< 1$ flags sign-reversal-prone pairs; magnitude ASV $< \\delta_{\\text{observed}}$ indicates bias exceeds tolerance (Algorithm~\\ref{alg:correction}); the safe/fragile partition is stable across parameterizations ($\\varepsilon < 0.02$; Appendix~\\ref{sec:asv_stability}).\n",
      "numLines": 120,
      "startLine": 1,
      "totalLines": 120
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01YNEdMkxbwWVPm96a2of1cw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/k3_symmetric_proof.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "503d4106-d751-4ceb-997e-8a013ae39150",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkLWCxmfRm6Zu3w4qJSgty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14352,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14352
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T02:56:05.228Z_

<details><summary>↩ Tool result · `toolu_01YNEdMkxbwWVPm96a2of1cw`</summary>

```text
1	% K=3 Symmetric Confusion Matrix: Monotonicity Proof
2	% Theorem statement is in method.tex; this file contains the proof and remarks only.
3	
4	\begin{proof}
5	All three parts reduce to a single lemma about the between-group variance
6	$V_B(\delta)=\operatorname{Var}\bigl(\mathbb{E}[g(A)\mid A^*_\delta]\bigr)$.
7	
8	\paragraph{Step 1: Structural reduction.}
9	The symmetric $C_0$ decomposes as $C_0=(1{-}3c)\,I+c\,\mathbf{1}\mathbf{1}^\top$, so
10	\[
11	  C(\delta) = (1{-}\delta)I + \delta\bigl[(1{-}3c)\,I+c\,\mathbf{1}\mathbf{1}^\top\bigr]
12	  = (1{-}3c\delta)\,I + c\delta\,\mathbf{1}\mathbf{1}^\top.
13	\]
14	Setting $s=c\delta\in[0,c]$, each entry is
15	$C(\delta)_{j\ell}=(1{-}3s)\,\mathbf{1}_{j=\ell}+s$,
16	so $C(\delta)$ stays in the one-parameter symmetric family.
17	In particular:
18	\begin{align}
19	  q_j(s) &= \textstyle\sum_k C(\delta)_{jk}\,p_k = (1{-}3s)\,p_j + s, \label{eq:k3q} \\
20	  \mu_j(s) &\equiv \mathbb{E}[g(A)\mid A^*{=}j]
21	  = \bar{g} + \frac{(1{-}3s)\,p_j\,h_j}{q_j(s)}, \label{eq:k3mu}
22	\end{align}
23	where $h_j=g_j-\bar{g}$, $\bar{g}=\sum_k p_k g_k$.
24	
25	\paragraph{Step 2: Closed-form $V_B(s)$.}
26	The between-group variance admits a clean factorization:
27	\begin{equation}
28	  V_B(s) = \sum_j q_j\,(\mu_j-\bar{g})^2
29	  = (1{-}3s)^2\sum_{j=0}^{2}\frac{p_j^2\,h_j^2}{q_j(s)}.
30	  \label{eq:k3VB}
31	\end{equation}
32	\emph{Verification.}
33	At $s{=}0$: $q_j{=}p_j$, so $V_B(0)=\sum_j p_j h_j^2=\operatorname{Var}(g)$.
34	At $s{=}\tfrac{1}{3}$: $V_B(\tfrac{1}{3})=0$.
35	
36	\paragraph{Step 3: $V_B$ is strictly decreasing on $[0,\tfrac{1}{3})$ (pointwise, not just at endpoints).}
37	Differentiating~\eqref{eq:k3VB} via the product rule:
38	\begin{equation}
39	  \frac{dV_B}{ds}
40	  = (1{-}3s)\sum_{j=0}^{2}\frac{p_j^2\,h_j^2}{q_j^2}\;\bigl[\underbrace{-3(1{-}3s)\,p_j - 1 - 3s}_{\displaystyle\Lambda_j(s)}\bigr].
41	  \label{eq:k3dVB}
42	\end{equation}
43	
44	\emph{Derivation.}
45	Write $V_B=(1{-}3s)^2 F(s)$ with $F(s)=\sum_j p_j^2 h_j^2/q_j(s)$.
46	The product rule gives $V_B'=-6(1{-}3s)F+(1{-}3s)^2 F'$.
47	Since $q_j'(s)=1{-}3p_j$, we have $F'(s)=\sum_j p_j^2 h_j^2(3p_j{-}1)/q_j^2$.
48	Combining:
49	\begin{align*}
50	  V_B'
51	  &= (1{-}3s)\Bigl[-6\sum_j \frac{p_j^2 h_j^2}{q_j}+(1{-}3s)\sum_j \frac{p_j^2 h_j^2(3p_j{-}1)}{q_j^2}\Bigr] \\
52	  &= (1{-}3s)\sum_j \frac{p_j^2 h_j^2}{q_j^2}\bigl[-6q_j+(1{-}3s)(3p_j{-}1)\bigr].
53	\end{align*}
54	Expanding the bracket:
55	\[
56	  -6q_j+(1{-}3s)(3p_j{-}1)
57	  = -6(1{-}3s)p_j-6s+3(1{-}3s)p_j-(1{-}3s)
58	  = -3(1{-}3s)p_j-1-3s
59	  = \Lambda_j(s).
60	\]
61	
62	\emph{Sign analysis.}
63	For $s\in[0,\tfrac{1}{3})$: $(1{-}3s)>0$, $p_j\geq 0$, so
64	\[
65	  \Lambda_j(s) = -3(1{-}3s)\,p_j - (1+3s) < 0
66	  \quad\text{for all } j,
67	\]
68	since $1+3s>0$ alone forces $\Lambda_j<0$.
69	Every term $p_j^2 h_j^2/q_j^2\geq 0$, and the prefactor $(1{-}3s)>0$.
70	Hence $dV_B/ds\leq 0$ for all $s\in[0,\tfrac{1}{3})$.
71	
72	\emph{Strict inequality.}
73	If $\operatorname{Var}(g){>}0$, at least two categories $j$ satisfy $p_j>0$ and $h_j\neq 0$, contributing strictly positive terms.
74	Since $\Lambda_j<0$, the sum is strictly negative:
75	$dV_B/ds<0$ for all $s\in(0,\tfrac{1}{3})$.
76	
77	\paragraph{Step 4: From $V_B$ to $|B|$ --- confounding (a).}
78	Under proportional effects $f=\lambda g$ (Proposition~\ref{prop:conf_prop}):
79	\[
80	  B(C(\delta)) = \frac{\lambda\,V_W(\delta)}{V_W(\delta)+\sigma_T^2},
81	  \quad V_W(\delta)=\operatorname{Var}(g)-V_B(c\delta).
82	\]
83	Step~3 shows $V_B(s)$ is strictly decreasing in $s=c\delta$, so $V_W(\delta)$ is strictly increasing from $0$ to $\operatorname{Var}(g)$.
84	Since $x\mapsto |\lambda|\,x/(x+\sigma_T^2)$ is strictly increasing for $x\geq 0$:
85	\[
86	  |B(C(\delta))| = |\lambda|\,\frac{V_W(\delta)}{V_W(\delta)+\sigma_T^2}
87	\]
88	is strictly non-decreasing.
89	
90	\paragraph{Step 5: Mediation (b).}
91	Under proportional effects $f=\lambda g$ with $g(k)=\mathbb{E}[T\mid A{=}k]$, the mediation bias
92	(§\ref{par:med_monotone}) has the identical form
93	$B=\lambda\,V_W/(V_W+\sigma_\varepsilon^2)$
94	with $\sigma_\varepsilon^2=\mathbb{E}[\operatorname{Var}(T\mid A)]$ replacing $\sigma_T^2$.
95	The same argument yields $|B|$ strictly non-decreasing.
96	
97	\paragraph{Step 6: Collider (c).}
98	Under proportional effects $h=\lambda g$ (Proposition~\ref{prop:col_prop}):
99	\[
100	  B_{\mathrm{col}}(C(\delta)) = -\frac{\lambda\,V_B(c\delta)}{\operatorname{Var}(T)-V_B(c\delta)},
101	  \qquad
102	  |B_{\mathrm{col}}| = |\lambda|\,\frac{V_B(c\delta)}{\operatorname{Var}(T)-V_B(c\delta)}.
103	\]
104	Since $x\mapsto x/(a{-}x)$ is strictly increasing for $x\in[0,a)$
105	and $V_B(s)$ is strictly decreasing (Step~3),
106	$|B_{\mathrm{col}}(C(\delta))|$ is strictly non-increasing:
107	from $|B_{\mathrm{Berkson}}|=|\lambda|\,V_g/(\operatorname{Var}(T){-}V_g)$ at $\delta{=}0$
108	to $0$ at $\delta$ such that $V_B\to 0$.
109	\end{proof}
110	
111	\begin{remark}[Comparison with the general-$K$ proof]
112	\label{rem:k3_vs_general}
113	The general-$K$ monotonicity proof (§\ref{app:monotonicity_proof}) relies on
114	convexity of $V_B(\delta)$ plus the endpoint condition $V_B'(1)\leq 0$,
115	the latter verified only for $K{=}2$ analytically and $K\geq 3$ numerically.
116	The $K{=}3$ symmetric proof is \emph{stronger}:
117	it establishes $dV_B/ds<0$ at every interior point via the signed decomposition~\eqref{eq:k3dVB},
118	bypassing both the convexity argument and the endpoint condition entirely.
119	The key enabler is that the symmetric $C_0$ keeps $C(\delta)$ within the one-parameter family
120	$(1{-}3s)I+s\,\mathbf{1}\mathbf{1}^\top$, yielding the factored form~\eqref{eq:k3VB}
121	in which the $(1{-}3s)^2$ prefactor and the $q_j^{-1}$ terms interact to produce
122	a uniformly signed derivative.
123	\end{remark}
124	
125	\begin{remark}[General (non-proportional) effects]
126	\label{rem:k3_general}
127	For non-proportional effects ($f\neq\lambda g$), the confounding bias
128	$B(C)=\mathbb{E}[\operatorname{Cov}(g,f\mid A^*)]/D(C)$
129	does not factor through $V_W$ alone,
130	and exact monotonicity of $|B(C(\delta))|$ can fail even for $K{=}3$ symmetric $C_0$.
131	Numerical verification ($50{,}000$ random configurations) finds violations in ${\sim}10\%$ of cases,
132	with maximum step deviation ${\sim}0.004$,
133	confirming $\varepsilon$-approximate monotonicity consistent with the general-$K$ results
134	(Table~\ref{tab:conjecture_verify}).
135	\end{remark}
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "38cde5ff-ea9e-4dfb-a491-fc14b470e20d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/k3_symmetric_proof.tex",
      "content": "% K=3 Symmetric Confusion Matrix: Monotonicity Proof\n% Theorem statement is in method.tex; this file contains the proof and remarks only.\n\n\\begin{proof}\nAll three parts reduce to a single lemma about the between-group variance\n$V_B(\\delta)=\\operatorname{Var}\\bigl(\\mathbb{E}[g(A)\\mid A^*_\\delta]\\bigr)$.\n\n\\paragraph{Step 1: Structural reduction.}\nThe symmetric $C_0$ decomposes as $C_0=(1{-}3c)\\,I+c\\,\\mathbf{1}\\mathbf{1}^\\top$, so\n\\[\n  C(\\delta) = (1{-}\\delta)I + \\delta\\bigl[(1{-}3c)\\,I+c\\,\\mathbf{1}\\mathbf{1}^\\top\\bigr]\n  = (1{-}3c\\delta)\\,I + c\\delta\\,\\mathbf{1}\\mathbf{1}^\\top.\n\\]\nSetting $s=c\\delta\\in[0,c]$, each entry is\n$C(\\delta)_{j\\ell}=(1{-}3s)\\,\\mathbf{1}_{j=\\ell}+s$,\nso $C(\\delta)$ stays in the one-parameter symmetric family.\nIn particular:\n\\begin{align}\n  q_j(s) &= \\textstyle\\sum_k C(\\delta)_{jk}\\,p_k = (1{-}3s)\\,p_j + s, \\label{eq:k3q} \\\\\n  \\mu_j(s) &\\equiv \\mathbb{E}[g(A)\\mid A^*{=}j]\n  = \\bar{g} + \\frac{(1{-}3s)\\,p_j\\,h_j}{q_j(s)}, \\label{eq:k3mu}\n\\end{align}\nwhere $h_j=g_j-\\bar{g}$, $\\bar{g}=\\sum_k p_k g_k$.\n\n\\paragraph{Step 2: Closed-form $V_B(s)$.}\nThe between-group variance admits a clean factorization:\n\\begin{equation}\n  V_B(s) = \\sum_j q_j\\,(\\mu_j-\\bar{g})^2\n  = (1{-}3s)^2\\sum_{j=0}^{2}\\frac{p_j^2\\,h_j^2}{q_j(s)}.\n  \\label{eq:k3VB}\n\\end{equation}\n\\emph{Verification.}\nAt $s{=}0$: $q_j{=}p_j$, so $V_B(0)=\\sum_j p_j h_j^2=\\operatorname{Var}(g)$.\nAt $s{=}\\tfrac{1}{3}$: $V_B(\\tfrac{1}{3})=0$.\n\n\\paragraph{Step 3: $V_B$ is strictly decreasing on $[0,\\tfrac{1}{3})$ (pointwise, not just at endpoints).}\nDifferentiating~\\eqref{eq:k3VB} via the product rule:\n\\begin{equation}\n  \\frac{dV_B}{ds}\n  = (1{-}3s)\\sum_{j=0}^{2}\\frac{p_j^2\\,h_j^2}{q_j^2}\\;\\bigl[\\underbrace{-3(1{-}3s)\\,p_j - 1 - 3s}_{\\displaystyle\\Lambda_j(s)}\\bigr].\n  \\label{eq:k3dVB}\n\\end{equation}\n\n\\emph{Derivation.}\nWrite $V_B=(1{-}3s)^2 F(s)$ with $F(s)=\\sum_j p_j^2 h_j^2/q_j(s)$.\nThe product rule gives $V_B'=-6(1{-}3s)F+(1{-}3s)^2 F'$.\nSince $q_j'(s)=1{-}3p_j$, we have $F'(s)=\\sum_j p_j^2 h_j^2(3p_j{-}1)/q_j^2$.\nCombining:\n\\begin{align*}\n  V_B'\n  &= (1{-}3s)\\Bigl[-6\\sum_j \\frac{p_j^2 h_j^2}{q_j}+(1{-}3s)\\sum_j \\frac{p_j^2 h_j^2(3p_j{-}1)}{q_j^2}\\Bigr] \\\\\n  &= (1{-}3s)\\sum_j \\frac{p_j^2 h_j^2}{q_j^2}\\bigl[-6q_j+(1{-}3s)(3p_j{-}1)\\bigr].\n\\end{align*}\nExpanding the bracket:\n\\[\n  -6q_j+(1{-}3s)(3p_j{-}1)\n  = -6(1{-}3s)p_j-6s+3(1{-}3s)p_j-(1{-}3s)\n  = -3(1{-}3s)p_j-1-3s\n  = \\Lambda_j(s).\n\\]\n\n\\emph{Sign analysis.}\nFor $s\\in[0,\\tfrac{1}{3})$: $(1{-}3s)>0$, $p_j\\geq 0$, so\n\\[\n  \\Lambda_j(s) = -3(1{-}3s)\\,p_j - (1+3s) < 0\n  \\quad\\text{for all } j,\n\\]\nsince $1+3s>0$ alone forces $\\Lambda_j<0$.\nEvery term $p_j^2 h_j^2/q_j^2\\geq 0$, and the prefactor $(1{-}3s)>0$.\nHence $dV_B/ds\\leq 0$ for all $s\\in[0,\\tfrac{1}{3})$.\n\n\\emph{Strict inequality.}\nIf $\\operatorname{Var}(g){>}0$, at least two categories $j$ satisfy $p_j>0$ and $h_j\\neq 0$, contributing strictly positive terms.\nSince $\\Lambda_j<0$, the sum is strictly negative:\n$dV_B/ds<0$ for all $s\\in(0,\\tfrac{1}{3})$.\n\n\\paragraph{Step 4: From $V_B$ to $|B|$ --- confounding (a).}\nUnder proportional effects $f=\\lambda g$ (Proposition~\\ref{prop:conf_prop}):\n\\[\n  B(C(\\delta)) = \\frac{\\lambda\\,V_W(\\delta)}{V_W(\\delta)+\\sigma_T^2},\n  \\quad V_W(\\delta)=\\operatorname{Var}(g)-V_B(c\\delta).\n\\]\nStep~3 shows $V_B(s)$ is strictly decreasing in $s=c\\delta$, so $V_W(\\delta)$ is strictly increasing from $0$ to $\\operatorname{Var}(g)$.\nSince $x\\mapsto |\\lambda|\\,x/(x+\\sigma_T^2)$ is strictly increasing for $x\\geq 0$:\n\\[\n  |B(C(\\delta))| = |\\lambda|\\,\\frac{V_W(\\delta)}{V_W(\\delta)+\\sigma_T^2}\n\\]\nis strictly non-decreasing.\n\n\\paragraph{Step 5: Mediation (b).}\nUnder proportional effects $f=\\lambda g$ with $g(k)=\\mathbb{E}[T\\mid A{=}k]$, the mediation bias\n(§\\ref{par:med_monotone}) has the identical form\n$B=\\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$\nwith $\\sigma_\\varepsilon^2=\\mathbb{E}[\\operatorname{Var}(T\\mid A)]$ replacing $\\sigma_T^2$.\nThe same argument yields $|B|$ strictly non-decreasing.\n\n\\paragraph{Step 6: Collider (c).}\nUnder proportional effects $h=\\lambda g$ (Proposition~\\ref{prop:col_prop}):\n\\[\n  B_{\\mathrm{col}}(C(\\delta)) = -\\frac{\\lambda\\,V_B(c\\delta)}{\\operatorname{Var}(T)-V_B(c\\delta)},\n  \\qquad\n  |B_{\\mathrm{col}}| = |\\lambda|\\,\\frac{V_B(c\\delta)}{\\operatorname{Var}(T)-V_B(c\\delta)}.\n\\]\nSince $x\\mapsto x/(a{-}x)$ is strictly increasing for $x\\in[0,a)$\nand $V_B(s)$ is strictly decreasing (Step~3),\n$|B_{\\mathrm{col}}(C(\\delta))|$ is strictly non-increasing:\nfrom $|B_{\\mathrm{Berkson}}|=|\\lambda|\\,V_g/(\\operatorname{Var}(T){-}V_g)$ at $\\delta{=}0$\nto $0$ at $\\delta$ such that $V_B\\to 0$.\n\\end{proof}\n\n\\begin{remark}[Comparison with the general-$K$ proof]\n\\label{rem:k3_vs_general}\nThe general-$K$ monotonicity proof (§\\ref{app:monotonicity_proof}) relies on\nconvexity of $V_B(\\delta)$ plus the endpoint condition $V_B'(1)\\leq 0$,\nthe latter verified only for $K{=}2$ analytically and $K\\geq 3$ numerically.\nThe $K{=}3$ symmetric proof is \\emph{stronger}:\nit establishes $dV_B/ds<0$ at every interior point via the signed decomposition~\\eqref{eq:k3dVB},\nbypassing both the convexity argument and the endpoint condition entirely.\nThe key enabler is that the symmetric $C_0$ keeps $C(\\delta)$ within the one-parameter family\n$(1{-}3s)I+s\\,\\mathbf{1}\\mathbf{1}^\\top$, yielding the factored form~\\eqref{eq:k3VB}\nin which the $(1{-}3s)^2$ prefactor and the $q_j^{-1}$ terms interact to produce\na uniformly signed derivative.\n\\end{remark}\n\n\\begin{remark}[General (non-proportional) effects]\n\\label{rem:k3_general}\nFor non-proportional effects ($f\\neq\\lambda g$), the confounding bias\n$B(C)=\\mathbb{E}[\\operatorname{Cov}(g,f\\mid A^*)]/D(C)$\ndoes not factor through $V_W$ alone,\nand exact monotonicity of $|B(C(\\delta))|$ can fail even for $K{=}3$ symmetric $C_0$.\nNumerical verification ($50{,}000$ random configurations) finds violations in ${\\sim}10\\%$ of cases,\nwith maximum step deviation ${\\sim}0.004$,\nconfirming $\\varepsilon$-approximate monotonicity consistent with the general-$K$ results\n(Table~\\ref{tab:conjecture_verify}).\n\\end{remark}\n",
      "numLines": 136,
      "startLine": 1,
      "totalLines": 136
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01Ex2AXsiL2ZuezEGy1ejJX3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "dc73f0db-0749-4f1a-b7ea-99bfdee2c0fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkLWCxmfRm6Zu3w4qJSgty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14352,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14352
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T02:56:05.833Z_

<details><summary>↩ Tool result · `toolu_01Ex2AXsiL2ZuezEGy1ejJX3`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	MF-1a: Adversarial Monotonicity Test for Conjecture 1.
4	
5	Verifies ε-approximate envelope monotonicity of |B(C(δ))| along
6	C(δ)=(1-δ)I+δC₀ for δ∈[0,1] under 4 adversarial confusion matrix structures.
7	
8	Grid: 4 adversarial C₀ types × ~9 param configs × 3 K × 7 topologies × 3 β × 100 C₀
9	"""
10	
11	import json
12	import os
13	import sys
14	import time
15	import numpy as np
16	
17	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
18	from exp_d_conjecture_verify_v2 import (
19	    ALL_TOPOS, NON_DECREASING, NON_INCREASING,
20	    _COMPUTE_SS, make_all_params, get_tau_true,
21	    compute_bias_curve,
22	)
23	
24	K_VALUES = [3, 5, 7]
25	N_DELTA = 101
26	DELTA_STEP = 0.01
27	N_C0 = 1000
28	SEED = 2024
29	EPS_THRESHOLD = 0.001
30	
31	BETA_CONFIGS = ['alternating_large', 'same_sign', 'alternating_small']
32	ADV_TYPES = ['near_perm', 'block_diag', 'sparse', 'near_uniform']
33	ADV_PARAMS = {
34	    'near_perm': [{'eps': 0.05}, {'eps': 0.1}, {'eps': 0.2}],
35	    'block_diag': [{}],
36	    'sparse': [{'p_diag': 0.3}, {'p_diag': 0.5}, {'p_diag': 0.7}],
37	    'near_uniform': [{'eps': 0.01}, {'eps': 0.05}],
38	}
39	
40	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
41	
42	
43	def make_beta_vec(name, K):
44	    pools = {
45	        'alternating_large': [0, 1, -0.5, 0.3, -0.2, 0.1, -0.08],
46	        'same_sign':         [0, 0.5, 0.3, 0.2, 0.1, 0.08, 0.05],
47	        'alternating_small': [0, 0.2, -0.1, 0.05, -0.03, 0.02, -0.01],
48	    }
49	    return np.array(pools[name][:K])
50	
51	
52	def make_params_with_beta(K, beta_name):
53	    params = make_all_params(K)
54	    bv = make_beta_vec(beta_name, K)
55	    params['exposure']['beta'] = bv.copy()
56	    params['iv']['beta'] = bv.copy()
57	    params['mediation']['beta'] = bv.copy()
58	    params['frontdoor']['beta'] = bv.copy()
59	    params['confounding']['beta_A'] = bv[1:].copy()
60	    params['collider']['dY'] = bv.copy()
61	    params['mbias']['a1'] = bv.copy()
62	    return params
63	
64	
65	def gen_C0(adv_type, cfg, K, rng):
66	    if adv_type == 'near_perm':
67	        perm = rng.permutation(K)
68	        P = np.zeros((K, K))
69	        P[perm, np.arange(K)] = 1.0
70	        e = cfg['eps']
71	        return (1 - e) * P + e / K
72	
73	    if adv_type == 'block_diag':
74	        split = max(1, K // 2)
75	        C0 = np.zeros((K, K))
76	        for j in range(K):
77	            if j < split:
78	                C0[:split, j] = 1.0 / split
79	            else:
80	                C0[split:, j] = 1.0 / (K - split)
81	        return C0
82	
83	    if adv_type == 'sparse':
84	        pd = cfg['p_diag']
85	        C0 = np.zeros((K, K))
86	        for k in range(K):
87	            C0[k, k] = pd
88	            off = [i for i in range(K) if i != k]
89	            C0[rng.choice(off), k] = 1 - pd
90	        return C0
91	
92	    if adv_type == 'near_uniform':
93	        e = cfg['eps']
94	        dv = 1.0 / K + e
95	        ov = (1 - dv) / (K - 1)
96	        C0 = np.full((K, K), ov)
97	        np.fill_diagonal(C0, dv)
98	        return C0
99	
100	
101	def compute_fixed_curve(topo, C0, ss, tau_true):
102	    """Compute |B(C(δ))| for δ∈[0,1]. Returns (bias_abs[0:101], weak_iv)."""
103	    if topo == 'iv':
104	        FS = ss.FS
105	        a = float(FS[1])
106	        b = float((C0 @ FS)[1])
107	        if abs(a) < 1e-15:
108	            return None, True
109	        if abs(a - b) > 1e-15:
110	            d_cross = a / (a - b)
111	            if 0 < d_cross < 1:
112	                return None, True
113	
114	    deltas_full, bias_full = compute_bias_curve(
115	        topo, C0, ss, tau_true, delta_step=DELTA_STEP)
116	    n = min(N_DELTA, len(bias_full))
117	    if n < N_DELTA:
118	        return None, False
119	    return bias_full[:N_DELTA], False
120	
121	
122	def measure_violation(bias_abs, topo):
123	    """Return max single-step violation magnitude."""
124	    valid = ~np.isnan(bias_abs)
125	    ba = bias_abs[valid]
126	    if len(ba) < 2:
127	        return 0.0
128	    diffs = np.diff(ba)
129	    if topo in NON_DECREASING:
130	        drops = -diffs[diffs < 0]
131	    else:
132	        drops = diffs[diffs > 0]
133	    return float(drops.max()) if len(drops) > 0 else 0.0
134	
135	
136	def main():
137	    t0 = time.time()
138	    rng = np.random.default_rng(SEED)
139	
140	    print("=" * 78)
141	    print("MF-1a: Adversarial Monotonicity Test")
142	    print(f"  K={K_VALUES}  β={BETA_CONFIGS}")
143	    print(f"  Adversarial: {ADV_TYPES}")
144	    print(f"  N_C0={N_C0}  δ steps={N_DELTA}  ε threshold={EPS_THRESHOLD}")
145	    print("=" * 78)
146	    sys.stdout.flush()
147	
148	    all_eps = []
149	    by_adv = {a: {'n': 0, 'nm': 0, 'mx': 0.0} for a in ADV_TYPES}
150	    by_topo = {t: {'n': 0, 'nm': 0, 'mx': 0.0} for t in ALL_TOPOS}
151	    by_K = {str(k): {'n': 0, 'nm': 0, 'mx': 0.0} for k in K_VALUES}
152	    worst = []
153	    total_weak_iv = 0
154	    total_skipped = 0
155	
156	    n_adv_cfgs = sum(len(v) for v in ADV_PARAMS.values())
157	    n_cells = len(K_VALUES) * len(BETA_CONFIGS) * len(ALL_TOPOS) * n_adv_cfgs
158	    cell_i = 0
159	
160	    for K in K_VALUES:
161	        for beta_name in BETA_CONFIGS:
162	            params = make_params_with_beta(K, beta_name)
163	
164	            for topo in ALL_TOPOS:
165	                ss = _COMPUTE_SS[topo](K, params[topo])
166	                tau_true = get_tau_true(topo, K, params, ss)
167	
168	                if np.isnan(tau_true) or abs(tau_true) < 1e-12:
169	                    cell_i += n_adv_cfgs
170	                    total_skipped += n_adv_cfgs * N_C0
171	                    continue
172	
173	                for adv_type in ADV_TYPES:
174	                    for adv_cfg in ADV_PARAMS[adv_type]:
175	                        cell_i += 1
176	                        cell_eps = []
177	                        cell_nm = 0
178	                        cell_weak = 0
179	
180	                        for _ in range(N_C0):
181	                            C0 = gen_C0(adv_type, adv_cfg, K, rng)
182	                            curve, weak = compute_fixed_curve(
183	                                topo, C0, ss, tau_true)
184	
185	                            if weak:
186	                                cell_weak += 1
187	                                continue
188	                            if curve is None:
189	                                continue
190	
191	                            eps = measure_violation(curve, topo)
192	                            cell_eps.append(eps)
193	                            if eps > EPS_THRESHOLD:
194	                                cell_nm += 1
195	
196	                        n_valid = len(cell_eps)
197	                        if n_valid == 0:
198	                            total_weak_iv += cell_weak
199	                            continue
200	
201	                        mx = max(cell_eps)
202	                        total_weak_iv += cell_weak
203	                        all_eps.extend(cell_eps)
204	
205	                        for acc, key in [(by_adv, adv_type),
206	                                         (by_topo, topo),
207	                                         (by_K, str(K))]:
208	                            acc[key]['n'] += n_valid
209	                            acc[key]['nm'] += cell_nm
210	                            acc[key]['mx'] = max(acc[key]['mx'], mx)
211	
212	                        if mx > EPS_THRESHOLD:
213	                            worst.append({
214	                                'topology': topo, 'K': K,
215	                                'adversarial': adv_type,
216	                                'adv_config': json.dumps(adv_cfg)
217	                                              if adv_cfg else "{}",
218	                                'beta': beta_name,
219	                                'eps_abs': mx,
220	                                'non_mono_frac': cell_nm / n_valid,
221	                                'n_valid': n_valid,
222	                                'weak_iv': cell_weak,
223	                            })
224	
225	                        if cell_i % 63 == 0 or cell_i == n_cells:
226	                            print(
227	                                f"  [{cell_i:>4}/{n_cells}] K={K} "
228	                                f"{topo:<12} {adv_type:<14} "
229	                                f"β={beta_name:<18} max_ε={mx:.6f} "
230	                                f"nm={cell_nm}/{n_valid}  "
231	                                f"({time.time()-t0:.1f}s)")
232	                            sys.stdout.flush()
233	
234	    eps_arr = np.array(all_eps) if all_eps else np.array([0.0])
235	    total_curves = len(all_eps)
236	    total_nm = sum(1 for e in all_eps if e > EPS_THRESHOLD)
237	
238	    safe_topos = {'confounding', 'mediation', 'exposure', 'frontdoor'}
239	    fragile_topos = {'collider', 'mbias', 'iv'}
240	
241	    def fmt_acc(d):
242	        return {k: {
243	            'total_curves': v['n'],
244	            'non_monotone_count': v['nm'],
245	            'non_monotone_fraction': v['nm'] / max(v['n'], 1),
246	            'max_eps_abs': v['mx'],
247	        } for k, v in d.items()}
248	
249	    worst.sort(key=lambda x: -x['eps_abs'])
250	    worst = worst[:20]
251	
252	    output = {
253	        'description':
254	            'Adversarial envelope monotonicity test for Conjecture 1',
255	        'config': {
256	            'K_values': K_VALUES,
257	            'adversarial_types': ADV_TYPES,
258	            'adversarial_params': ADV_PARAMS,
259	            'topologies': ALL_TOPOS,
260	            'beta_configs': BETA_CONFIGS,
261	            'n_C0_per_cell': N_C0,
262	            'n_delta_steps': N_DELTA,
263	            'delta_step': DELTA_STEP,
264	            'eps_threshold': EPS_THRESHOLD,
265	            'seed': SEED,
266	        },
267	        'summary': {
268	            'total_curves': total_curves,
269	            'non_monotone_fraction':
270	                total_nm / max(total_curves, 1),
271	            'max_eps_abs': float(eps_arr.max()),
272	            'median_eps_abs': float(np.median(eps_arr)),
273	            'mean_eps_abs': float(np.mean(eps_arr)),
274	            'p95_eps_abs': float(np.percentile(eps_arr, 95)),
275	            'p99_eps_abs': float(np.percentile(eps_arr, 99)),
276	            'safe_topo_max_eps': float(
277	                max(by_topo[t]['mx'] for t in safe_topos)),
278	            'fragile_topo_max_eps': float(
279	                max(by_topo[t]['mx'] for t in fragile_topos)),
280	            'total_weak_iv_filtered': total_weak_iv,
281	            'total_skipped_zero_tau': total_skipped,
282	        },
283	        'by_adversarial_type': fmt_acc(by_adv),
284	        'by_topology': fmt_acc(by_topo),
285	        'by_K': fmt_acc(by_K),
286	        'worst_cases': worst,
287	        'elapsed_seconds': time.time() - t0,
288	    }
289	
290	    out_path = os.path.join(OUT_DIR, 'adversarial_monotonicity_results.json')
291	    with open(out_path, 'w') as f:
292	        json.dump(output, f, indent=2, default=str)
293	
294	    print(f"\nJSON -> {out_path}")
295	    print(f"\n{'='*60}")
296	    print(f"Total curves: {total_curves:,}  "
297	          f"Non-monotone: {total_nm} "
298	          f"({total_nm/max(total_curves,1)*100:.3f}%)")
299	    print(f"Max ε_abs: {eps_arr.max():.6f}  "
300	          f"Median: {np.median(eps_arr):.6f}")
301	    print(f"Safe max ε: "
302	          f"{max(by_topo[t]['mx'] for t in safe_topos):.6f}  "
303	          f"Fragile max ε: "
304	          f"{max(by_topo[t]['mx'] for t in fragile_topos):.6f}")
305	    print(f"Weak-IV filtered: {total_weak_iv}")
306	
307	    print(f"\nBy topology:")
308	    for t in ALL_TOPOS:
309	        d = by_topo[t]
310	        dr = 'non-dec' if t in NON_DECREASING else 'non-inc'
311	        print(f"  {t:<14} [{dr}]  n={d['n']:>6}  nm={d['nm']:>5}  "
312	              f"({d['nm']/max(d['n'],1)*100:.2f}%)  "
313	              f"max_ε={d['mx']:.6f}")
314	
315	    print(f"\nBy adversarial type:")
316	    for a in ADV_TYPES:
317	        d = by_adv[a]
318	        print(f"  {a:<14}  n={d['n']:>6}  nm={d['nm']:>5}  "
319	              f"({d['nm']/max(d['n'],1)*100:.2f}%)  "
320	              f"max_ε={d['mx']:.6f}")
321	
322	    print(f"\nBy K:")
323	    for k in K_VALUES:
324	        d = by_K[str(k)]
325	        print(f"  K={k}  n={d['n']:>6}  nm={d['nm']:>5}  "
326	              f"({d['nm']/max(d['n'],1)*100:.2f}%)  "
327	              f"max_ε={d['mx']:.6f}")
328	
329	    if worst:
330	        print(f"\nWorst cases (top 5):")
331	        for w in worst[:5]:
332	            print(f"  {w['topology']:<14} K={w['K']} "
333	                  f"{w['adversarial']:<14} "
334	                  f"β={w['beta']:<18} ε={w['eps_abs']:.6f}")
335	
336	    print(f"\nElapsed: {time.time()-t0:.1f}s")
337	    print('=' * 60)
338	
339	
340	if __name__ == '__main__':
341	    main()
342	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "e1c9bbfd-da57-40d7-a764-132d021d43b0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nMF-1a: Adversarial Monotonicity Test for Conjecture 1.\n\nVerifies ε-approximate envelope monotonicity of |B(C(δ))| along\nC(δ)=(1-δ)I+δC₀ for δ∈[0,1] under 4 adversarial confusion matrix structures.\n\nGrid: 4 adversarial C₀ types × ~9 param configs × 3 K × 7 topologies × 3 β × 100 C₀\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\nimport numpy as np\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom exp_d_conjecture_verify_v2 import (\n    ALL_TOPOS, NON_DECREASING, NON_INCREASING,\n    _COMPUTE_SS, make_all_params, get_tau_true,\n    compute_bias_curve,\n)\n\nK_VALUES = [3, 5, 7]\nN_DELTA = 101\nDELTA_STEP = 0.01\nN_C0 = 1000\nSEED = 2024\nEPS_THRESHOLD = 0.001\n\nBETA_CONFIGS = ['alternating_large', 'same_sign', 'alternating_small']\nADV_TYPES = ['near_perm', 'block_diag', 'sparse', 'near_uniform']\nADV_PARAMS = {\n    'near_perm': [{'eps': 0.05}, {'eps': 0.1}, {'eps': 0.2}],\n    'block_diag': [{}],\n    'sparse': [{'p_diag': 0.3}, {'p_diag': 0.5}, {'p_diag': 0.7}],\n    'near_uniform': [{'eps': 0.01}, {'eps': 0.05}],\n}\n\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\n\n\ndef make_beta_vec(name, K):\n    pools = {\n        'alternating_large': [0, 1, -0.5, 0.3, -0.2, 0.1, -0.08],\n        'same_sign':         [0, 0.5, 0.3, 0.2, 0.1, 0.08, 0.05],\n        'alternating_small': [0, 0.2, -0.1, 0.05, -0.03, 0.02, -0.01],\n    }\n    return np.array(pools[name][:K])\n\n\ndef make_params_with_beta(K, beta_name):\n    params = make_all_params(K)\n    bv = make_beta_vec(beta_name, K)\n    params['exposure']['beta'] = bv.copy()\n    params['iv']['beta'] = bv.copy()\n    params['mediation']['beta'] = bv.copy()\n    params['frontdoor']['beta'] = bv.copy()\n    params['confounding']['beta_A'] = bv[1:].copy()\n    params['collider']['dY'] = bv.copy()\n    params['mbias']['a1'] = bv.copy()\n    return params\n\n\ndef gen_C0(adv_type, cfg, K, rng):\n    if adv_type == 'near_perm':\n        perm = rng.permutation(K)\n        P = np.zeros((K, K))\n        P[perm, np.arange(K)] = 1.0\n        e = cfg['eps']\n        return (1 - e) * P + e / K\n\n    if adv_type == 'block_diag':\n        split = max(1, K // 2)\n        C0 = np.zeros((K, K))\n        for j in range(K):\n            if j < split:\n                C0[:split, j] = 1.0 / split\n            else:\n                C0[split:, j] = 1.0 / (K - split)\n        return C0\n\n    if adv_type == 'sparse':\n        pd = cfg['p_diag']\n        C0 = np.zeros((K, K))\n        for k in range(K):\n            C0[k, k] = pd\n            off = [i for i in range(K) if i != k]\n            C0[rng.choice(off), k] = 1 - pd\n        return C0\n\n    if adv_type == 'near_uniform':\n        e = cfg['eps']\n        dv = 1.0 / K + e\n        ov = (1 - dv) / (K - 1)\n        C0 = np.full((K, K), ov)\n        np.fill_diagonal(C0, dv)\n        return C0\n\n\ndef compute_fixed_curve(topo, C0, ss, tau_true):\n    \"\"\"Compute |B(C(δ))| for δ∈[0,1]. Returns (bias_abs[0:101], weak_iv).\"\"\"\n    if topo == 'iv':\n        FS = ss.FS\n        a = float(FS[1])\n        b = float((C0 @ FS)[1])\n        if abs(a) < 1e-15:\n            return None, True\n        if abs(a - b) > 1e-15:\n            d_cross = a / (a - b)\n            if 0 < d_cross < 1:\n                return None, True\n\n    deltas_full, bias_full = compute_bias_curve(\n        topo, C0, ss, tau_true, delta_step=DELTA_STEP)\n    n = min(N_DELTA, len(bias_full))\n    if n < N_DELTA:\n        return None, False\n    return bias_full[:N_DELTA], False\n\n\ndef measure_violation(bias_abs, topo):\n    \"\"\"Return max single-step violation magnitude.\"\"\"\n    valid = ~np.isnan(bias_abs)\n    ba = bias_abs[valid]\n    if len(ba) < 2:\n        return 0.0\n    diffs = np.diff(ba)\n    if topo in NON_DECREASING:\n        drops = -diffs[diffs < 0]\n    else:\n        drops = diffs[diffs > 0]\n    return float(drops.max()) if len(drops) > 0 else 0.0\n\n\ndef main():\n    t0 = time.time()\n    rng = np.random.default_rng(SEED)\n\n    print(\"=\" * 78)\n    print(\"MF-1a: Adversarial Monotonicity Test\")\n    print(f\"  K={K_VALUES}  β={BETA_CONFIGS}\")\n    print(f\"  Adversarial: {ADV_TYPES}\")\n    print(f\"  N_C0={N_C0}  δ steps={N_DELTA}  ε threshold={EPS_THRESHOLD}\")\n    print(\"=\" * 78)\n    sys.stdout.flush()\n\n    all_eps = []\n    by_adv = {a: {'n': 0, 'nm': 0, 'mx': 0.0} for a in ADV_TYPES}\n    by_topo = {t: {'n': 0, 'nm': 0, 'mx': 0.0} for t in ALL_TOPOS}\n    by_K = {str(k): {'n': 0, 'nm': 0, 'mx': 0.0} for k in K_VALUES}\n    worst = []\n    total_weak_iv = 0\n    total_skipped = 0\n\n    n_adv_cfgs = sum(len(v) for v in ADV_PARAMS.values())\n    n_cells = len(K_VALUES) * len(BETA_CONFIGS) * len(ALL_TOPOS) * n_adv_cfgs\n    cell_i = 0\n\n    for K in K_VALUES:\n        for beta_name in BETA_CONFIGS:\n            params = make_params_with_beta(K, beta_name)\n\n            for topo in ALL_TOPOS:\n                ss = _COMPUTE_SS[topo](K, params[topo])\n                tau_true = get_tau_true(topo, K, params, ss)\n\n                if np.isnan(tau_true) or abs(tau_true) < 1e-12:\n                    cell_i += n_adv_cfgs\n                    total_skipped += n_adv_cfgs * N_C0\n                    continue\n\n                for adv_type in ADV_TYPES:\n                    for adv_cfg in ADV_PARAMS[adv_type]:\n                        cell_i += 1\n                        cell_eps = []\n                        cell_nm = 0\n                        cell_weak = 0\n\n                        for _ in range(N_C0):\n                            C0 = gen_C0(adv_type, adv_cfg, K, rng)\n                            curve, weak = compute_fixed_curve(\n                                topo, C0, ss, tau_true)\n\n                            if weak:\n                                cell_weak += 1\n                                continue\n                            if curve is None:\n                                continue\n\n                            eps = measure_violation(curve, topo)\n                            cell_eps.append(eps)\n                            if eps > EPS_THRESHOLD:\n                                cell_nm += 1\n\n                        n_valid = len(cell_eps)\n                        if n_valid == 0:\n                            total_weak_iv += cell_weak\n                            continue\n\n                        mx = max(cell_eps)\n                        total_weak_iv += cell_weak\n                        all_eps.extend(cell_eps)\n\n                        for acc, key in [(by_adv, adv_type),\n                                         (by_topo, topo),\n                                         (by_K, str(K))]:\n                            acc[key]['n'] += n_valid\n                            acc[key]['nm'] += cell_nm\n                            acc[key]['mx'] = max(acc[key]['mx'], mx)\n\n                        if mx > EPS_THRESHOLD:\n                            worst.append({\n                                'topology': topo, 'K': K,\n                                'adversarial': adv_type,\n                                'adv_config': json.dumps(adv_cfg)\n                                              if adv_cfg else \"{}\",\n                                'beta': beta_name,\n                                'eps_abs': mx,\n                                'non_mono_frac': cell_nm / n_valid,\n                                'n_valid': n_valid,\n                                'weak_iv': cell_weak,\n                            })\n\n                        if cell_i % 63 == 0 or cell_i == n_cells:\n                            print(\n                                f\"  [{cell_i:>4}/{n_cells}] K={K} \"\n                                f\"{topo:<12} {adv_type:<14} \"\n                                f\"β={beta_name:<18} max_ε={mx:.6f} \"\n                                f\"nm={cell_nm}/{n_valid}  \"\n                                f\"({time.time()-t0:.1f}s)\")\n                            sys.stdout.flush()\n\n    eps_arr = np.array(all_eps) if all_eps else np.array([0.0])\n    total_curves = len(all_eps)\n    total_nm = sum(1 for e in all_eps if e > EPS_THRESHOLD)\n\n    safe_topos = {'confounding', 'mediation', 'exposure', 'frontdoor'}\n    fragile_topos = {'collider', 'mbias', 'iv'}\n\n    def fmt_acc(d):\n        return {k: {\n            'total_curves': v['n'],\n            'non_monotone_count': v['nm'],\n            'non_monotone_fraction': v['nm'] / max(v['n'], 1),\n            'max_eps_abs': v['mx'],\n        } for k, v in d.items()}\n\n    worst.sort(key=lambda x: -x['eps_abs'])\n    worst = worst[:20]\n\n    output = {\n        'description':\n            'Adversarial envelope monotonicity test for Conjecture 1',\n        'config': {\n            'K_values': K_VALUES,\n            'adversarial_types': ADV_TYPES,\n            'adversarial_params': ADV_PARAMS,\n            'topologies': ALL_TOPOS,\n            'beta_configs': BETA_CONFIGS,\n            'n_C0_per_cell': N_C0,\n            'n_delta_steps': N_DELTA,\n            'delta_step': DELTA_STEP,\n            'eps_threshold': EPS_THRESHOLD,\n            'seed': SEED,\n        },\n        'summary': {\n            'total_curves': total_curves,\n            'non_monotone_fraction':\n                total_nm / max(total_curves, 1),\n            'max_eps_abs': float(eps_arr.max()),\n            'median_eps_abs': float(np.median(eps_arr)),\n            'mean_eps_abs': float(np.mean(eps_arr)),\n            'p95_eps_abs': float(np.percentile(eps_arr, 95)),\n            'p99_eps_abs': float(np.percentile(eps_arr, 99)),\n            'safe_topo_max_eps': float(\n                max(by_topo[t]['mx'] for t in safe_topos)),\n            'fragile_topo_max_eps': float(\n                max(by_topo[t]['mx'] for t in fragile_topos)),\n            'total_weak_iv_filtered': total_weak_iv,\n            'total_skipped_zero_tau': total_skipped,\n        },\n        'by_adversarial_type': fmt_acc(by_adv),\n        'by_topology': fmt_acc(by_topo),\n        'by_K': fmt_acc(by_K),\n        'worst_cases': worst,\n        'elapsed_seconds': time.time() - t0,\n    }\n\n    out_path = os.path.join(OUT_DIR, 'adversarial_monotonicity_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n\n    print(f\"\\nJSON -> {out_path}\")\n    print(f\"\\n{'='*60}\")\n    print(f\"Total curves: {total_curves:,}  \"\n          f\"Non-monotone: {total_nm} \"\n          f\"({total_nm/max(total_curves,1)*100:.3f}%)\")\n    print(f\"Max ε_abs: {eps_arr.max():.6f}  \"\n          f\"Median: {np.median(eps_arr):.6f}\")\n    print(f\"Safe max ε: \"\n          f\"{max(by_topo[t]['mx'] for t in safe_topos):.6f}  \"\n          f\"Fragile max ε: \"\n          f\"{max(by_topo[t]['mx'] for t in fragile_topos):.6f}\")\n    print(f\"Weak-IV filtered: {total_weak_iv}\")\n\n    print(f\"\\nBy topology:\")\n    for t in ALL_TOPOS:\n        d = by_topo[t]\n        dr = 'non-dec' if t in NON_DECREASING else 'non-inc'\n        print(f\"  {t:<14} [{dr}]  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    print(f\"\\nBy adversarial type:\")\n    for a in ADV_TYPES:\n        d = by_adv[a]\n        print(f\"  {a:<14}  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    print(f\"\\nBy K:\")\n    for k in K_VALUES:\n        d = by_K[str(k)]\n        print(f\"  K={k}  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    if worst:\n        print(f\"\\nWorst cases (top 5):\")\n        for w in worst[:5]:\n            print(f\"  {w['topology']:<14} K={w['K']} \"\n                  f\"{w['adversarial']:<14} \"\n                  f\"β={w['beta']:<18} ε={w['eps_abs']:.6f}\")\n\n    print(f\"\\nElapsed: {time.time()-t0:.1f}s\")\n    print('=' * 60)\n\n\nif __name__ == '__main__':\n    main()\n",
      "numLines": 342,
      "startLine": 1,
      "totalLines": 342
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

Now let me read the appendix_proofs.tex in sections, focusing on the monotonicity proof and V_B analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "bd84a615-93a5-4b12-9204-d3d6c8d7e31f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CqqswJgda6WWxLJMbMhD9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14324,
      "cache_read_input_tokens": 26193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14324
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_0183WSSAHt7vZxTZnyLQiRJM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 1,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "3bd5a82f-610d-4c55-982a-208f6e8b7ce6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CqqswJgda6WWxLJMbMhD9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14324,
      "cache_read_input_tokens": 26193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14324
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T02:56:11.309Z_

<details><summary>↩ Tool result · `toolu_0183WSSAHt7vZxTZnyLQiRJM`</summary>

```text
1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\tilde{Y}=Y-\mathbb{E}[Y\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\dots,D_{K-1}^*)$.
31	
32	\begin{lemma}[Bias decomposition]
33	\label{lem:bias_decomp}
34	Suppose $Y = \tau T + f(A) + \varepsilon_Y$ with $\varepsilon_Y \perp (T, A, A^*)$.
35	Then
36	\begin{equation}
37	  \operatorname{plim}\hat\tau(C) = \tau + \frac{R(C)}{D(C)},
38	  \label{eq:bias_decomp}
39	\end{equation}
40	where
41	\begin{align}
42	  R(C) &= \mathbb{E}\bigl[\operatorname{Cov}(T,\,f(A)\mid A^*)\bigr], \label{eq:R}\\
43	  D(C) &= \mathbb{E}\bigl[\operatorname{Var}(T\mid A^*)\bigr] > 0. \label{eq:D}
44	\end{align}
45	\end{lemma}
46	
47	\begin{proof}
48	Expand $\tilde{Y}$ using $Y=\tau T + f(A) + \varepsilon_Y$:
49	\[
50	  \tilde{Y} = \tau\,\tilde{T} + \bigl(f(A) - \mathbb{E}[f(A)\mid A^*]\bigr) + \varepsilon_Y.
51	\]
52	Since $\tilde{T}$ is measurable w.r.t.\ $(T,A^*)$ and $\varepsilon_Y\perp(T,A,A^*)$:
53	\[
54	  \mathbb{E}[\tilde{T}\,\tilde{Y}]
55	  = \tau\,\mathbb{E}[\tilde{T}^2]
56	  + \mathbb{E}\bigl[\tilde{T}\,\bigl(f(A)-\mathbb{E}[f(A)\mid A^*]\bigr)\bigr].
57	\]
58	The numerator residual is $R(C) = \mathbb{E}[\tilde{T}(f(A)-\mathbb{E}[f(A)\mid A^*])]$, and the denominator is $D(C) = \mathbb{E}[\tilde{T}^2]$.
59	
60	By the law of total covariance:
61	\[
62	  R(C) = \sum_{j=0}^{K-1} q_j\,\operatorname{Cov}(T,\,f(A)\mid A^*{=}j)
63	  = \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)].
64	\]
65	For $D(C)>0$: decompose $T = g(A) + \varepsilon_T$ where $g(A)=\mathbb{E}[T\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).
66	In both cases, $\tilde{T}=\bigl(g(A)-\mathbb{E}[g(A)\mid A^*]\bigr)+\varepsilon_T'$, where $\varepsilon_T'$ is the component of $T$ independent of $(A,A^*)$.
67	Hence $D(C)\geq\operatorname{Var}(\varepsilon_T')>0$.
68	\end{proof}
69	
70	\subsection{Confounding Topology ($A$ = Confounder)}
71	\label{app:confounding}
72	
73	\paragraph{Data-generating process.}
74	$A\to T$, $A\to Y$, $T\to Y$.
75	Using dummy coding with category 0 as reference:
76	\begin{align*}
77	  T &= \sum_{j=1}^{K-1}\alpha_j D_j + \varepsilon_T,\quad
78	  \varepsilon_T\sim\mathcal{N}(0,\sigma_T^2),\;\varepsilon_T\perp A,\\
79	  Y &= \tau\, T + \sum_{j=1}^{K-1}\beta_j^{(A)} D_j + \varepsilon_Y,\quad
80	  \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp(T,A).
81	\end{align*}
82	Define $g(k)=\sum_{j}\alpha_j\mathbf{1}(k{=}j)$ and $f(k)=\sum_{j}\beta_j^{(A)}\mathbf{1}(k{=}j)$, so $g(0)=f(0)=0$.
83	
84	\paragraph{Closed-form plim.}
85	Using the FWL decomposition, the coefficient on $T$ is:
86	\begin{equation}
87	  \operatorname{plim}\hat\tau(C)
88	  = \frac{\mu_{TY} - \sum_{j=0}^{K-1}\frac{\mathrm{ct}_j\,\mathrm{cy}_j}{q_j}}
89	  {s_T - \sum_{j=0}^{K-1}\frac{\mathrm{ct}_j^2}{q_j}},
90	  \label{eq:plim_conf}
91	\end{equation}
92	where $s_T=\mathbb{E}[T^2]$, $\mu_{TY}=\mathbb{E}[TY]$, and $\mathrm{ct}_j$, $\mathrm{cy}_j$, $q_j$ are defined in~\eqref{eq:q}--\eqref{eq:cy}.
93	
94	\begin{proof}[Derivation]
95	By FWL, $\operatorname{plim}\hat\tau = \mathbb{E}[\tilde{T}Y]/\mathbb{E}[\tilde{T}^2]$ where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$.
96	Since $\mathbb{E}[T\mid A^*{=}j]=\mathrm{ct}_j/q_j$:
97	\begin{align*}
98	  \mathbb{E}[\tilde{T}^2]
99	  &= \mathbb{E}[T^2] - \sum_j q_j\bigl(\mathrm{ct}_j/q_j\bigr)^2
100	  = s_T - \sum_j \mathrm{ct}_j^2/q_j,\\
101	  \mathbb{E}[\tilde{T}\,Y]
102	  &= \mathbb{E}[TY] - \sum_j \bigl(\mathrm{ct}_j/q_j\bigr)\,\mathbb{E}[Y\cdot D_j^*]
103	  = \mu_{TY} - \sum_j \mathrm{ct}_j\,\mathrm{cy}_j/q_j.
104	\end{align*}
105	\end{proof}
106	
107	\paragraph{Verification at $C=I$.}
108	When $C=I$: $q_j=p_j$, $\mathrm{ct}_j=\mathbb{E}[T D_j]=\alpha_j p_j$, $\mathrm{cy}_j=\mathbb{E}[Y D_j]=p_j(\tau\alpha_j+\beta_j^{(A)})$.
109	Direct substitution yields numerator $= \tau\sigma_T^2$ and denominator $= \sigma_T^2$, giving $\operatorname{plim}\hat\tau = \tau$.
110	
111	\paragraph{Bias structure.}
112	By Lemma~\ref{lem:bias_decomp}:
113	\begin{equation}
114	  \operatorname{plim}\hat\tau(C) = \tau + B(C),\quad
115	  B(C) = \frac{\mathbb{E}[\operatorname{Cov}(g(A),\,f(A)\mid A^*)]}{D(C)}.
116	  \label{eq:bias_conf}
117	\end{equation}
118	By the law of total covariance:
119	\begin{equation}
120	  \mathbb{E}[\operatorname{Cov}(g,f\mid A^*)]
121	  = \operatorname{Cov}(g(A),f(A))
122	  - \operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[f(A)\mid A^*]\bigr).
123	  \label{eq:lotc}
124	\end{equation}
125	
126	At $C=I$: $\mathbb{E}[g\mid A^*]=g(A)$, so the between-group covariance equals $\operatorname{Cov}(g,f)$ and $B(I)=0$.
127	
128	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform, $A^*\perp A$): $\mathbb{E}[g\mid A^*]$ is constant, so the between-group covariance is zero and
129	\begin{equation}
130	  B_{\mathrm{OV}} \;\equiv\; B\bigl(\tfrac{1}{K}\mathbf{1}\mathbf{1}^\top\bigr)
131	  = \frac{\operatorname{Cov}(g(A),\,f(A))}{\operatorname{Var}(T)},
132	  \label{eq:bov}
133	\end{equation}
134	which equals the classical omitted-variable bias (no control for $A$).
135	
136	\paragraph{Sign preservation condition.}
137	Since $D(C)>0$, sign$(\operatorname{plim}\hat\tau) = $ sign$(\tau\cdot D(C) + R(C))$.
138	For sign preservation, it suffices that $R(C)$ does not overwhelm $\tau\cdot D(C)$.
139	
140	\begin{proposition}[Confounding sign preservation --- proportional case]
141	\label{prop:conf_prop}
142	If $f(A) = \lambda\,g(A)$ for some constant $\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then
143	\begin{equation}
144	  B(C) = \bigl(1-\xi(C)\bigr)\,B_{\mathrm{OV}},
145	  \label{eq:convex}
146	\end{equation}
147	where
148	\[
149	  \xi(C) = \frac{\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\;\sigma_T^2}
150	  {\operatorname{Var}(g(A))\bigl(\operatorname{Var}(g(A))-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])+\sigma_T^2\bigr)}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "7219dda8-7405-4d7a-9dcc-d0ef7361cf4a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "\\section{Proofs of Proposition~\\ref{prop:signflip} and Theorem~\\ref{thm:monotone}}\n\\label{app:proof}\n\nWe provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\\ref{thm:monotone}).\nThroughout, $A\\in\\{0,1,\\dots,K{-}1\\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\\mid A{=}k)$.\nWe use category~0 as the reference and let $D_j=\\mathbf{1}(A{=}j)$, $D_j^*=\\mathbf{1}(A^*{=}j)$ for $j=1,\\dots,K{-}1$.\n\n\\subsection{Notation and Key Identities}\n\\label{app:notation}\n\nUnder non-differential misclassification, the misclassified moments factor linearly through $C$.\nDefine the population vectors:\n\\begin{align}\n  q_j &= P(A^*{=}j) = \\textstyle\\sum_k C_{jk}\\,p_k, \\label{eq:q}\\\\\n  \\mathrm{ct}_j &= \\mathbb{E}[T\\cdot D_j^*] = \\textstyle\\sum_k C_{jk}\\,\\mathbb{E}[T\\cdot D_k], \\label{eq:ct}\\\\\n  \\mathrm{cy}_j &= \\mathbb{E}[Y\\cdot D_j^*] = \\textstyle\\sum_k C_{jk}\\,\\mathbb{E}[Y\\cdot D_k]. \\label{eq:cy}\n\\end{align}\nWrite $q = Cp$, $\\mathrm{ct} = C\\,\\mathbb{E}[T\\cdot D]$, and $\\mathrm{cy} = C\\,\\mathbb{E}[Y\\cdot D]$, where $D=(D_0,\\dots,D_{K-1})^\\top$.\n\n\\subsection{Frisch--Waugh--Lovell Decomposition}\n\\label{app:fwl}\n\nFor topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\\dots,D_{K-1}^*)$.\nBy the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat{\\tau}(C)\n  = \\frac{\\mathbb{E}[\\tilde{T}\\,\\tilde{Y}]}{\\mathbb{E}[\\tilde{T}^2]},\n  \\label{eq:fwl}\n\\end{equation}\nwhere $\\tilde{T}=T-\\mathbb{E}[T\\mid A^*]$ and $\\tilde{Y}=Y-\\mathbb{E}[Y\\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\\dots,D_{K-1}^*)$.\n\n\\begin{lemma}[Bias decomposition]\n\\label{lem:bias_decomp}\nSuppose $Y = \\tau T + f(A) + \\varepsilon_Y$ with $\\varepsilon_Y \\perp (T, A, A^*)$.\nThen\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + \\frac{R(C)}{D(C)},\n  \\label{eq:bias_decomp}\n\\end{equation}\nwhere\n\\begin{align}\n  R(C) &= \\mathbb{E}\\bigl[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)\\bigr], \\label{eq:R}\\\\\n  D(C) &= \\mathbb{E}\\bigl[\\operatorname{Var}(T\\mid A^*)\\bigr] > 0. \\label{eq:D}\n\\end{align}\n\\end{lemma}\n\n\\begin{proof}\nExpand $\\tilde{Y}$ using $Y=\\tau T + f(A) + \\varepsilon_Y$:\n\\[\n  \\tilde{Y} = \\tau\\,\\tilde{T} + \\bigl(f(A) - \\mathbb{E}[f(A)\\mid A^*]\\bigr) + \\varepsilon_Y.\n\\]\nSince $\\tilde{T}$ is measurable w.r.t.\\ $(T,A^*)$ and $\\varepsilon_Y\\perp(T,A,A^*)$:\n\\[\n  \\mathbb{E}[\\tilde{T}\\,\\tilde{Y}]\n  = \\tau\\,\\mathbb{E}[\\tilde{T}^2]\n  + \\mathbb{E}\\bigl[\\tilde{T}\\,\\bigl(f(A)-\\mathbb{E}[f(A)\\mid A^*]\\bigr)\\bigr].\n\\]\nThe numerator residual is $R(C) = \\mathbb{E}[\\tilde{T}(f(A)-\\mathbb{E}[f(A)\\mid A^*])]$, and the denominator is $D(C) = \\mathbb{E}[\\tilde{T}^2]$.\n\nBy the law of total covariance:\n\\[\n  R(C) = \\sum_{j=0}^{K-1} q_j\\,\\operatorname{Cov}(T,\\,f(A)\\mid A^*{=}j)\n  = \\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)].\n\\]\nFor $D(C)>0$: decompose $T = g(A) + \\varepsilon_T$ where $g(A)=\\mathbb{E}[T\\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).\nIn both cases, $\\tilde{T}=\\bigl(g(A)-\\mathbb{E}[g(A)\\mid A^*]\\bigr)+\\varepsilon_T'$, where $\\varepsilon_T'$ is the component of $T$ independent of $(A,A^*)$.\nHence $D(C)\\geq\\operatorname{Var}(\\varepsilon_T')>0$.\n\\end{proof}\n\n\\subsection{Confounding Topology ($A$ = Confounder)}\n\\label{app:confounding}\n\n\\paragraph{Data-generating process.}\n$A\\to T$, $A\\to Y$, $T\\to Y$.\nUsing dummy coding with category 0 as reference:\n\\begin{align*}\n  T &= \\sum_{j=1}^{K-1}\\alpha_j D_j + \\varepsilon_T,\\quad\n  \\varepsilon_T\\sim\\mathcal{N}(0,\\sigma_T^2),\\;\\varepsilon_T\\perp A,\\\\\n  Y &= \\tau\\, T + \\sum_{j=1}^{K-1}\\beta_j^{(A)} D_j + \\varepsilon_Y,\\quad\n  \\varepsilon_Y\\sim\\mathcal{N}(0,1),\\;\\varepsilon_Y\\perp(T,A).\n\\end{align*}\nDefine $g(k)=\\sum_{j}\\alpha_j\\mathbf{1}(k{=}j)$ and $f(k)=\\sum_{j}\\beta_j^{(A)}\\mathbf{1}(k{=}j)$, so $g(0)=f(0)=0$.\n\n\\paragraph{Closed-form plim.}\nUsing the FWL decomposition, the coefficient on $T$ is:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C)\n  = \\frac{\\mu_{TY} - \\sum_{j=0}^{K-1}\\frac{\\mathrm{ct}_j\\,\\mathrm{cy}_j}{q_j}}\n  {s_T - \\sum_{j=0}^{K-1}\\frac{\\mathrm{ct}_j^2}{q_j}},\n  \\label{eq:plim_conf}\n\\end{equation}\nwhere $s_T=\\mathbb{E}[T^2]$, $\\mu_{TY}=\\mathbb{E}[TY]$, and $\\mathrm{ct}_j$, $\\mathrm{cy}_j$, $q_j$ are defined in~\\eqref{eq:q}--\\eqref{eq:cy}.\n\n\\begin{proof}[Derivation]\nBy FWL, $\\operatorname{plim}\\hat\\tau = \\mathbb{E}[\\tilde{T}Y]/\\mathbb{E}[\\tilde{T}^2]$ where $\\tilde{T}=T-\\mathbb{E}[T\\mid A^*]$.\nSince $\\mathbb{E}[T\\mid A^*{=}j]=\\mathrm{ct}_j/q_j$:\n\\begin{align*}\n  \\mathbb{E}[\\tilde{T}^2]\n  &= \\mathbb{E}[T^2] - \\sum_j q_j\\bigl(\\mathrm{ct}_j/q_j\\bigr)^2\n  = s_T - \\sum_j \\mathrm{ct}_j^2/q_j,\\\\\n  \\mathbb{E}[\\tilde{T}\\,Y]\n  &= \\mathbb{E}[TY] - \\sum_j \\bigl(\\mathrm{ct}_j/q_j\\bigr)\\,\\mathbb{E}[Y\\cdot D_j^*]\n  = \\mu_{TY} - \\sum_j \\mathrm{ct}_j\\,\\mathrm{cy}_j/q_j.\n\\end{align*}\n\\end{proof}\n\n\\paragraph{Verification at $C=I$.}\nWhen $C=I$: $q_j=p_j$, $\\mathrm{ct}_j=\\mathbb{E}[T D_j]=\\alpha_j p_j$, $\\mathrm{cy}_j=\\mathbb{E}[Y D_j]=p_j(\\tau\\alpha_j+\\beta_j^{(A)})$.\nDirect substitution yields numerator $= \\tau\\sigma_T^2$ and denominator $= \\sigma_T^2$, giving $\\operatorname{plim}\\hat\\tau = \\tau$.\n\n\\paragraph{Bias structure.}\nBy Lemma~\\ref{lem:bias_decomp}:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + B(C),\\quad\n  B(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(g(A),\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:bias_conf}\n\\end{equation}\nBy the law of total covariance:\n\\begin{equation}\n  \\mathbb{E}[\\operatorname{Cov}(g,f\\mid A^*)]\n  = \\operatorname{Cov}(g(A),f(A))\n  - \\operatorname{Cov}\\bigl(\\mathbb{E}[g(A)\\mid A^*],\\;\\mathbb{E}[f(A)\\mid A^*]\\bigr).\n  \\label{eq:lotc}\n\\end{equation}\n\nAt $C=I$: $\\mathbb{E}[g\\mid A^*]=g(A)$, so the between-group covariance equals $\\operatorname{Cov}(g,f)$ and $B(I)=0$.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ (uniform, $A^*\\perp A$): $\\mathbb{E}[g\\mid A^*]$ is constant, so the between-group covariance is zero and\n\\begin{equation}\n  B_{\\mathrm{OV}} \\;\\equiv\\; B\\bigl(\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top\\bigr)\n  = \\frac{\\operatorname{Cov}(g(A),\\,f(A))}{\\operatorname{Var}(T)},\n  \\label{eq:bov}\n\\end{equation}\nwhich equals the classical omitted-variable bias (no control for $A$).\n\n\\paragraph{Sign preservation condition.}\nSince $D(C)>0$, sign$(\\operatorname{plim}\\hat\\tau) = $ sign$(\\tau\\cdot D(C) + R(C))$.\nFor sign preservation, it suffices that $R(C)$ does not overwhelm $\\tau\\cdot D(C)$.\n\n\\begin{proposition}[Confounding sign preservation --- proportional case]\n\\label{prop:conf_prop}\nIf $f(A) = \\lambda\\,g(A)$ for some constant $\\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then\n\\begin{equation}\n  B(C) = \\bigl(1-\\xi(C)\\bigr)\\,B_{\\mathrm{OV}},\n  \\label{eq:convex}\n\\end{equation}\nwhere\n\\[\n  \\xi(C) = \\frac{\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])\\;\\sigma_T^2}\n  {\\operatorname{Var}(g(A))\\bigl(\\operatorname{Var}(g(A))-\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])+\\sigma_T^2\\bigr)}",
      "numLines": 150,
      "startLine": 1,
      "totalLines": 1525
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01BjUEU6fCDtpDmNFHmTk1Yz`</summary>

```json
{
  "pattern": "monotonicity_proof|app:monotonicity|V_B|V_W|endpoint|convex",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "output_mode": "content",
  "head_limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "107726b0-eff1-4f2b-bfe3-b0939dbe3f59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CqqswJgda6WWxLJMbMhD9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14324,
      "cache_read_input_tokens": 26193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14324
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T02:56:12.859Z_

<details><summary>↩ Tool result · `toolu_01BjUEU6fCDtpDmNFHmTk1Yz`</summary>

```text
145:  \label{eq:convex}
158:So $R(C)=\lambda\bigl(\operatorname{Var}(g)-\operatorname{Var}(\mathbb{E}[g\mid A^*])\bigr)=\lambda\,V_W$, where $V_W=\operatorname{Var}(g)-V_B$ with $V_B=\operatorname{Var}(\mathbb{E}[g\mid A^*])$.
159:Similarly, $D(C)=V_W+\sigma_T^2$.
162:  B(C) = \frac{\lambda\,V_W}{V_W+\sigma_T^2},\qquad
165:where $V=\operatorname{Var}(g)=V_B+V_W$.
168:  \frac{B(C)}{B_{\mathrm{OV}}} = \frac{V_W(V+\sigma_T^2)}{V(V_W+\sigma_T^2)} = 1 - \xi(C)
170:is a decreasing function of $V_B\in[0,V]$.
171:At $V_B=0$ (no classification, $C$ uniform): $\xi=0$, $B=B_{\mathrm{OV}}$.
172:At $V_B=V$ (perfect classification, $C=I$): $\xi=1$, $B=0$.
173:Since $0\leq V_B\leq V$, we have $\xi\in[0,1]$ and $B(C)\in[0,B_{\mathrm{OV}}]$ (with the sign of $B_{\mathrm{OV}}$).
233:\label{app:monotonicity_proof}
236:The proof proceeds by direct algebraic analysis of $V_B(\delta)=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*_\delta])$ as a rational function of $\delta$, establishing convexity and bounding the derivative at both endpoints.
239:From Proposition~\ref{prop:conf_prop}, $B(C)=\lambda V_W/(V_W+\sigma_T^2)$ where $V_W=\operatorname{Var}(g)-V_B$ and $V_B(\delta)=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*_\delta])$.
241:\emph{Step 1: Convexity of $V_B(\delta)$.}
244:Then $V_B(\delta)=\sum_j N_j(\delta)^2/q_j(\delta) - \bar{g}^2$.
245:Each term $N_j^2/q_j$ is the composition of the perspective function $(x,t)\mapsto x^2/t$ (convex for $t>0$) with the affine map $\delta\mapsto(N_j(\delta),\,q_j(\delta))$, hence convex in $\delta$.
246:A sum of convex functions is convex, so $V_B(\delta)$ is convex on $[0,\delta_{\max}]$.
252:\frac{dV_B}{d\delta}
261:\emph{Step 3: $V_B'(0)\leq 0$ (universal, no conditions on $C_0$).}
266:V_B'(0)=-\sum_{j\neq k}(C_0)_{jk}\,p_k\,(g_j-g_k)^2\;\leq\; 0,
270:\emph{Step 4: $V_B'(1)\leq 0$ for $K{=}2$.}
278:  V_B'(1) &= (1{-}a)\,p_0(\mu_0^2{-}\mu_1^2)+(1{-}b)\,p_1\bigl[(1{-}\mu_1)^2{-}(1{-}\mu_0)^2\bigr] \\
284:Under $a,b\geq\tfrac{1}{2}$: $a{+}b\geq 1$, so $\mu_0{-}\mu_1\leq 0$ and $V_B'(1)\leq 0$.
286:\emph{Step 5: Monotonicity from convexity.}
287:Since $V_B$ is convex (Step~1), its derivative $V_B'$ is non-decreasing.
288:When $V_B'(1)\leq 0$, we have $V_B'(\delta)\leq V_B'(1)\leq 0$ for all $\delta\in[0,1]$, so $V_B$ is non-increasing.
291:$V_W(\delta)=\operatorname{Var}(g)-V_B(\delta)$ is non-decreasing (Step~5).
293:Hence $|B(\delta)|=h(V_W(\delta))$ is non-decreasing. \qed
296:The proof requires $V_B'(1)\leq 0$, which is guaranteed for $K{=}2$ when $(C_0)_{jj}\geq\tfrac{1}{2}$ (Step~4).
297:For $K\geq 3$, $V_B'(1)\leq 0$ holds for all $g$ and $p$ if and only if a certain matrix $M-W$ (depending on $C_0$ and $p$) is negative semi-definite; simple diagonal thresholds are sufficient in practice but not universal.
299:A $K{=}2$ counterexample ($C_0$ the permutation matrix, $(C_0)_{jj}{=}0$) shows the diagonal condition is necessary: $V_B(\delta)=(\delta{-}\tfrac{1}{2})^2$ increases on $(\tfrac{1}{2},1]$.
303:By the same convexity argument, each $\mathbb{E}[\operatorname{Var}(\cdot\mid A^*_\delta)]$ is non-decreasing in $\delta$, and $D(\delta)=\mathbb{E}[\operatorname{Var}(T\mid A^*_\delta)]$ is non-decreasing.
377:Since each $\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\delta_j$, the bound $|B(C)|\leq\max_j|\delta_j|$ holds.
403:  R(C) &= \lambda\,\mathbb{E}[\operatorname{Var}(g(A)\mid A^*)] = \lambda\,V_W.
409:       = V_W + \sigma_\varepsilon^2,
419:$B(C) = \lambda\,V_W/(V_W+\sigma_\varepsilon^2)$,
421:Since $V_B(\delta)$ is convex with $V_B'(0)\leq 0$ (same argument as \S\ref{app:monotonicity_proof}, Steps~1--3), $V_W(\delta)=V{-}V_B(\delta)$ is non-decreasing under the same conditions on $C_0$.
433:Substituting back into~\eqref{eq:mediation} gives the convex-combination form
447:The endpoints $\lambda(I)=1$ and $\lambda(C)\to 0$ in the rank-one (uninformative) limit hold in all regimes.
449:[Omitted long matching line]
455:\emph{Proportional case.} Step~4 of the mediation derivation gives $B(C)=\lambda_0\,V_W(C)/(V_W(C)+\sigma_\varepsilon^2)$; the rank-one limit $V_W{\to}V$ yields $\tau_{\mathrm{ind}}=\lambda_0\,V/(V+\sigma_\varepsilon^2)$. Both quantities carry $\operatorname{sign}(\lambda_0)$, establishing~(a). The ratio
457:  \frac{B(C)}{\tau_{\mathrm{ind}}}\;=\;\frac{V_W(C)\,(V+\sigma_\varepsilon^2)}{V\,(V_W(C)+\sigma_\varepsilon^2)}
459:is monotone increasing in $V_W(C)\in[0,V]$ with range $[0,1]$ (its derivative in $V_W$ is $\sigma_\varepsilon^2(V+\sigma_\varepsilon^2)/[V(V_W+\sigma_\varepsilon^2)^2]>0$), establishing~(b). Hence $\lambda(C)\in[0,1]$ unconditionally.
461:\emph{General case.} Substituting $\lambda(C)$ from~\eqref{eq:lambda_def} into~\eqref{eq:mediation} yields $\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)=\lambda(C)\,\tau_{\mathrm{dir}}+(1{-}\lambda(C))\,\tau_{\mathrm{total}}$, so $\lambda(C)\in[0,1]$ iff $\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)$ lies in the closed interval with endpoints $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{total}}$.
470:  \lambda_V(C) \;:=\; \frac{V_B(C)}{V},\qquad V_B(C)\;=\;\operatorname{Var}\!\bigl(\mathbb{E}[g(A)\mid A^*]\bigr),\quad V\;=\;\operatorname{Var}(g(A)),
472:which satisfies $\lambda_V(C)\in[0,1]$ \emph{unconditionally} by the law of total variance applied to $g(A)$. Under proportional effects, $\lambda$ and $\lambda_V$ agree at the endpoints and are related by
474:  1-\lambda(C)\;=\;\frac{V_W(C)\,(V+\sigma_\varepsilon^2)}{V\,(V_W(C)+\sigma_\varepsilon^2)}\;=\;\bigl(1-\lambda_V(C)\bigr)\cdot\frac{V+\sigma_\varepsilon^2}{V_W(C)+\sigma_\varepsilon^2},
645:Since $B_{\mathrm{med}}(C)$ has the same structure as the mediation bias (§\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "b9ecd756-b13a-4849-9724-af2190855b42",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "145:  \\label{eq:convex}\n158:So $R(C)=\\lambda\\bigl(\\operatorname{Var}(g)-\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\bigr)=\\lambda\\,V_W$, where $V_W=\\operatorname{Var}(g)-V_B$ with $V_B=\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$.\n159:Similarly, $D(C)=V_W+\\sigma_T^2$.\n162:  B(C) = \\frac{\\lambda\\,V_W}{V_W+\\sigma_T^2},\\qquad\n165:where $V=\\operatorname{Var}(g)=V_B+V_W$.\n168:  \\frac{B(C)}{B_{\\mathrm{OV}}} = \\frac{V_W(V+\\sigma_T^2)}{V(V_W+\\sigma_T^2)} = 1 - \\xi(C)\n170:is a decreasing function of $V_B\\in[0,V]$.\n171:At $V_B=0$ (no classification, $C$ uniform): $\\xi=0$, $B=B_{\\mathrm{OV}}$.\n172:At $V_B=V$ (perfect classification, $C=I$): $\\xi=1$, $B=0$.\n173:Since $0\\leq V_B\\leq V$, we have $\\xi\\in[0,1]$ and $B(C)\\in[0,B_{\\mathrm{OV}}]$ (with the sign of $B_{\\mathrm{OV}}$).\n233:\\label{app:monotonicity_proof}\n236:The proof proceeds by direct algebraic analysis of $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$ as a rational function of $\\delta$, establishing convexity and bounding the derivative at both endpoints.\n239:From Proposition~\\ref{prop:conf_prop}, $B(C)=\\lambda V_W/(V_W+\\sigma_T^2)$ where $V_W=\\operatorname{Var}(g)-V_B$ and $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$.\n241:\\emph{Step 1: Convexity of $V_B(\\delta)$.}\n244:Then $V_B(\\delta)=\\sum_j N_j(\\delta)^2/q_j(\\delta) - \\bar{g}^2$.\n245:Each term $N_j^2/q_j$ is the composition of the perspective function $(x,t)\\mapsto x^2/t$ (convex for $t>0$) with the affine map $\\delta\\mapsto(N_j(\\delta),\\,q_j(\\delta))$, hence convex in $\\delta$.\n246:A sum of convex functions is convex, so $V_B(\\delta)$ is convex on $[0,\\delta_{\\max}]$.\n252:\\frac{dV_B}{d\\delta}\n261:\\emph{Step 3: $V_B'(0)\\leq 0$ (universal, no conditions on $C_0$).}\n266:V_B'(0)=-\\sum_{j\\neq k}(C_0)_{jk}\\,p_k\\,(g_j-g_k)^2\\;\\leq\\; 0,\n270:\\emph{Step 4: $V_B'(1)\\leq 0$ for $K{=}2$.}\n278:  V_B'(1) &= (1{-}a)\\,p_0(\\mu_0^2{-}\\mu_1^2)+(1{-}b)\\,p_1\\bigl[(1{-}\\mu_1)^2{-}(1{-}\\mu_0)^2\\bigr] \\\\\n284:Under $a,b\\geq\\tfrac{1}{2}$: $a{+}b\\geq 1$, so $\\mu_0{-}\\mu_1\\leq 0$ and $V_B'(1)\\leq 0$.\n286:\\emph{Step 5: Monotonicity from convexity.}\n287:Since $V_B$ is convex (Step~1), its derivative $V_B'$ is non-decreasing.\n288:When $V_B'(1)\\leq 0$, we have $V_B'(\\delta)\\leq V_B'(1)\\leq 0$ for all $\\delta\\in[0,1]$, so $V_B$ is non-increasing.\n291:$V_W(\\delta)=\\operatorname{Var}(g)-V_B(\\delta)$ is non-decreasing (Step~5).\n293:Hence $|B(\\delta)|=h(V_W(\\delta))$ is non-decreasing. \\qed\n296:The proof requires $V_B'(1)\\leq 0$, which is guaranteed for $K{=}2$ when $(C_0)_{jj}\\geq\\tfrac{1}{2}$ (Step~4).\n297:For $K\\geq 3$, $V_B'(1)\\leq 0$ holds for all $g$ and $p$ if and only if a certain matrix $M-W$ (depending on $C_0$ and $p$) is negative semi-definite; simple diagonal thresholds are sufficient in practice but not universal.\n299:A $K{=}2$ counterexample ($C_0$ the permutation matrix, $(C_0)_{jj}{=}0$) shows the diagonal condition is necessary: $V_B(\\delta)=(\\delta{-}\\tfrac{1}{2})^2$ increases on $(\\tfrac{1}{2},1]$.\n303:By the same convexity argument, each $\\mathbb{E}[\\operatorname{Var}(\\cdot\\mid A^*_\\delta)]$ is non-decreasing in $\\delta$, and $D(\\delta)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*_\\delta)]$ is non-decreasing.\n377:Since each $\\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\\delta_j$, the bound $|B(C)|\\leq\\max_j|\\delta_j|$ holds.\n403:  R(C) &= \\lambda\\,\\mathbb{E}[\\operatorname{Var}(g(A)\\mid A^*)] = \\lambda\\,V_W.\n409:       = V_W + \\sigma_\\varepsilon^2,\n419:$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\n421:Since $V_B(\\delta)$ is convex with $V_B'(0)\\leq 0$ (same argument as \\S\\ref{app:monotonicity_proof}, Steps~1--3), $V_W(\\delta)=V{-}V_B(\\delta)$ is non-decreasing under the same conditions on $C_0$.\n433:Substituting back into~\\eqref{eq:mediation} gives the convex-combination form\n447:The endpoints $\\lambda(I)=1$ and $\\lambda(C)\\to 0$ in the rank-one (uninformative) limit hold in all regimes.\n449:[Omitted long matching line]\n455:\\emph{Proportional case.} Step~4 of the mediation derivation gives $B(C)=\\lambda_0\\,V_W(C)/(V_W(C)+\\sigma_\\varepsilon^2)$; the rank-one limit $V_W{\\to}V$ yields $\\tau_{\\mathrm{ind}}=\\lambda_0\\,V/(V+\\sigma_\\varepsilon^2)$. Both quantities carry $\\operatorname{sign}(\\lambda_0)$, establishing~(a). The ratio\n457:  \\frac{B(C)}{\\tau_{\\mathrm{ind}}}\\;=\\;\\frac{V_W(C)\\,(V+\\sigma_\\varepsilon^2)}{V\\,(V_W(C)+\\sigma_\\varepsilon^2)}\n459:is monotone increasing in $V_W(C)\\in[0,V]$ with range $[0,1]$ (its derivative in $V_W$ is $\\sigma_\\varepsilon^2(V+\\sigma_\\varepsilon^2)/[V(V_W+\\sigma_\\varepsilon^2)^2]>0$), establishing~(b). Hence $\\lambda(C)\\in[0,1]$ unconditionally.\n461:\\emph{General case.} Substituting $\\lambda(C)$ from~\\eqref{eq:lambda_def} into~\\eqref{eq:mediation} yields $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)=\\lambda(C)\\,\\tau_{\\mathrm{dir}}+(1{-}\\lambda(C))\\,\\tau_{\\mathrm{total}}$, so $\\lambda(C)\\in[0,1]$ iff $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)$ lies in the closed interval with endpoints $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{total}}$.\n470:  \\lambda_V(C) \\;:=\\; \\frac{V_B(C)}{V},\\qquad V_B(C)\\;=\\;\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr),\\quad V\\;=\\;\\operatorname{Var}(g(A)),\n472:which satisfies $\\lambda_V(C)\\in[0,1]$ \\emph{unconditionally} by the law of total variance applied to $g(A)$. Under proportional effects, $\\lambda$ and $\\lambda_V$ agree at the endpoints and are related by\n474:  1-\\lambda(C)\\;=\\;\\frac{V_W(C)\\,(V+\\sigma_\\varepsilon^2)}{V\\,(V_W(C)+\\sigma_\\varepsilon^2)}\\;=\\;\\bigl(1-\\lambda_V(C)\\bigr)\\cdot\\frac{V+\\sigma_\\varepsilon^2}{V_W(C)+\\sigma_\\varepsilon^2},\n645:Since $B_{\\mathrm{med}}(C)$ has the same structure as the mediation bias (§\\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:",
    "numLines": 48
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01JeAuT4JyJSHrmPie2H6tTT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 230,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "8a1a6d11-1e62-47f6-9c96-3c213fe75ed1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018o8dBnYHkM8f4q2Kn1YAmL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7166,
      "cache_read_input_tokens": 40517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7166
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T02:56:16.715Z_

<details><summary>↩ Tool result · `toolu_01JeAuT4JyJSHrmPie2H6tTT`</summary>

```text
230	For $K{>}3$, treatment effect coefficients are drawn from a fixed pool with alternating signs and decreasing magnitudes: $\boldsymbol{\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3, \ldots)$, truncated to $K$ entries. The category distribution uses $p_k \propto 1/(k{+}1)$, normalized to sum to 1. Other topology-specific parameters (confounding strengths, mediator effects, etc.) follow analogous alternating-sign pools. For $K{=}10$, $\boldsymbol{\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3)$.
231	
232	\subsection{Proof of Theorem~\ref{thm:monotone} (Confounding Monotonicity)}
233	\label{app:monotonicity_proof}
234	
235	Under the interpolation $C(\delta)=(1{-}\delta)I+\delta C_0$, we prove $|B(C(\delta))|$ is non-decreasing in $\delta$ for proportional effects ($f=\lambda g$) and provide numerical verification for the general case.
236	The proof proceeds by direct algebraic analysis of $V_B(\delta)=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*_\delta])$ as a rational function of $\delta$, establishing convexity and bounding the derivative at both endpoints.
237	
238	\paragraph{Proportional case ($f=\lambda g$).}
239	From Proposition~\ref{prop:conf_prop}, $B(C)=\lambda V_W/(V_W+\sigma_T^2)$ where $V_W=\operatorname{Var}(g)-V_B$ and $V_B(\delta)=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*_\delta])$.
240	
241	\emph{Step 1: Convexity of $V_B(\delta)$.}
242	Define $N_j(\delta)=\sum_k g_k\,C(\delta)_{jk}\,p_k$ and $q_j(\delta)=\sum_k C(\delta)_{jk}\,p_k$.
243	Both are affine in $\delta$, with $q_j(\delta)>0$.
244	Then $V_B(\delta)=\sum_j N_j(\delta)^2/q_j(\delta) - \bar{g}^2$.
245	Each term $N_j^2/q_j$ is the composition of the perspective function $(x,t)\mapsto x^2/t$ (convex for $t>0$) with the affine map $\delta\mapsto(N_j(\delta),\,q_j(\delta))$, hence convex in $\delta$.
246	A sum of convex functions is convex, so $V_B(\delta)$ is convex on $[0,\delta_{\max}]$.
247	
248	\emph{Step 2: Derivative formula.}
249	Let $\mu_j(\delta)=N_j(\delta)/q_j(\delta)=\mathbb{E}[g(A)\mid A^*{=}j]$.
250	Then
251	\begin{equation}
252	\frac{dV_B}{d\delta}
253	= -\sum_{j,k}\bigl[(C_0)_{jk}-\mathbf{1}_{j=k}\bigr]\,p_k\,(g_k-\mu_j(\delta))^2.
254	\label{eq:dVB}
255	\end{equation}
256	\emph{Derivation.}
257	$\frac{d}{d\delta}\frac{N_j^2}{q_j}=2\mu_j\dot{N}_j-\mu_j^2\dot{q}_j$
258	where $\dot{N}_j=m_j^0-g_jp_j$ and $\dot{q}_j=q_j^0-p_j$ (with $m_j^0=\sum_k g_k(C_0)_{jk}p_k$, $q_j^0=\sum_k(C_0)_{jk}p_k$).
259	Substituting and using column-stochasticity ($\sum_j(C_0)_{jk}=\sum_j\mathbf{1}_{j=k}=1$) to cancel the $g_k^2$ terms yields~\eqref{eq:dVB}.
260	
261	\emph{Step 3: $V_B'(0)\leq 0$ (universal, no conditions on $C_0$).}
262	At $\delta{=}0$: $\mu_j(0)=g_j$ (since $C(0)=I$), so $(g_k-\mu_j(0))^2=(g_k-g_j)^2$.
263	The diagonal terms ($j{=}k$) vanish.
264	Hence
265	\[
266	V_B'(0)=-\sum_{j\neq k}(C_0)_{jk}\,p_k\,(g_j-g_k)^2\;\leq\; 0,
267	\]
268	since every term is non-negative.
269	
270	\emph{Step 4: $V_B'(1)\leq 0$ for $K{=}2$.}
271	For $K{=}2$ with $C_0=\bigl[\begin{smallmatrix}a&1{-}b\\1{-}a&b\end{smallmatrix}\bigr]$ and $a,b\geq\tfrac{1}{2}$,
272	set $g_0{=}0$, $g_1{=}1$ without loss of generality
273	(the general case scales by $(\Delta g)^2$).
274	At $\delta{=}1$: $q_0{=}ap_0{+}(1{-}b)p_1$, $q_1{=}(1{-}a)p_0{+}bp_1$,
275	$\mu_0{=}(1{-}b)p_1/q_0$, $\mu_1{=}bp_1/q_1$.
276	Expanding~\eqref{eq:dVB} at $\delta{=}1$ and factoring:
277	\begin{align*}
278	  V_B'(1) &= (1{-}a)\,p_0(\mu_0^2{-}\mu_1^2)+(1{-}b)\,p_1\bigl[(1{-}\mu_1)^2{-}(1{-}\mu_0)^2\bigr] \\
279	  &= (\mu_0{-}\mu_1)\,\bigl[(1{-}a)\,p_0(\mu_0{+}\mu_1)+(1{-}b)\,p_1(2{-}\mu_0{-}\mu_1)\bigr].
280	\end{align*}
281	The bracket is non-negative (since $0\leq\mu_j\leq 1$ and all coefficients are non-negative).
282	Direct calculation gives $\mu_0{-}\mu_1=p_0\,p_1(1{-}a{-}b)/(q_0\,q_1)$
283	(expand $(1{-}b)\,q_1-b\,q_0=p_0(1{-}a{-}b)$).
284	Under $a,b\geq\tfrac{1}{2}$: $a{+}b\geq 1$, so $\mu_0{-}\mu_1\leq 0$ and $V_B'(1)\leq 0$.
285	
286	\emph{Step 5: Monotonicity from convexity.}
287	Since $V_B$ is convex (Step~1), its derivative $V_B'$ is non-decreasing.
288	When $V_B'(1)\leq 0$, we have $V_B'(\delta)\leq V_B'(1)\leq 0$ for all $\delta\in[0,1]$, so $V_B$ is non-increasing.
289	
290	\emph{Step 6: $|B(\delta)|$ is non-decreasing.}
291	$V_W(\delta)=\operatorname{Var}(g)-V_B(\delta)$ is non-decreasing (Step~5).
292	The function $h(x)=|\lambda|\,x/(x+\sigma_T^2)$ is strictly increasing for $x\geq 0$.
293	Hence $|B(\delta)|=h(V_W(\delta))$ is non-decreasing. \qed
294	
295	\paragraph{Condition on $C_0$.}
296	The proof requires $V_B'(1)\leq 0$, which is guaranteed for $K{=}2$ when $(C_0)_{jj}\geq\tfrac{1}{2}$ (Step~4).
297	For $K\geq 3$, $V_B'(1)\leq 0$ holds for all $g$ and $p$ if and only if a certain matrix $M-W$ (depending on $C_0$ and $p$) is negative semi-definite; simple diagonal thresholds are sufficient in practice but not universal.
298	Numerical verification across 20{,}000 random $(C_0,p,g)$ triples per $K\in\{3,5,7\}$ with $(C_0)_{jj}\geq 1/K$ finds worst-case $|B|$ step deviations $< 0.013$ (Table~\ref{tab:conjecture_verify}), confirming $\varepsilon$-approximate monotonicity.
299	A $K{=}2$ counterexample ($C_0$ the permutation matrix, $(C_0)_{jj}{=}0$) shows the diagonal condition is necessary: $V_B(\delta)=(\delta{-}\tfrac{1}{2})^2$ increases on $(\tfrac{1}{2},1]$.
300	
301	\paragraph{General case (non-proportional effects).}
302	$|B(C(\delta))|\leq\bar{B}(\delta)$ where $\bar{B}(\delta)=\sqrt{\mathbb{E}[\operatorname{Var}(g\mid A^*_\delta)]\,\mathbb{E}[\operatorname{Var}(f\mid A^*_\delta)]}\,/\,D(\delta)$ (Proposition~\ref{prop:conf_gen}).
303	By the same convexity argument, each $\mathbb{E}[\operatorname{Var}(\cdot\mid A^*_\delta)]$ is non-decreasing in $\delta$, and $D(\delta)=\mathbb{E}[\operatorname{Var}(T\mid A^*_\delta)]$ is non-decreasing.
304	Extended verification (20{,}000 random $C_0$ matrices, $K \in \{3,5,7\}$) reveals worst-case step deviations of 0.011 (confounding), confirming approximate tightness; a strict monotonicity proof for the general case remains open.
305	
306	\subsection{Mediation Topology ($A$ = Mediator)}
307	\label{app:mediation}
308	
309	\paragraph{Data-generating process.}
310	$T\to A\to Y$, $T\to Y$.
311	\begin{align*}
312	  T &\sim \operatorname{Bernoulli}(0.5),\\
313	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
314	  Y &= \tau_{\mathrm{dir}}\,T + f(A) + \varepsilon_Y.
315	\end{align*}
316	
317	\paragraph{Bias decomposition.}
318	By Lemma~\ref{lem:bias_decomp}, the direct-effect estimator satisfies:
319	\begin{equation}
320	  \operatorname{plim}\hat\tau_{\mathrm{dir}}(C) = \tau_{\mathrm{dir}} + \frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}.
321	  \label{eq:med_bias}
322	\end{equation}
323	
324	The key structural difference from confounding: $T$ \emph{causes} $A$, so the residual covariance $\operatorname{Cov}(T,f(A)\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.
325	
326	\paragraph{Endpoint analysis.}
327	
328	At $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\to A\to Y$, so $\operatorname{Cov}(T,f(A)\mid A)=0$ and $\operatorname{plim}\hat\tau=\tau_{\mathrm{dir}}$.
329	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "a44a7f64-b4ee-4df3-8cbc-391a3ab3ebde",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "For $K{>}3$, treatment effect coefficients are drawn from a fixed pool with alternating signs and decreasing magnitudes: $\\boldsymbol{\\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3, \\ldots)$, truncated to $K$ entries. The category distribution uses $p_k \\propto 1/(k{+}1)$, normalized to sum to 1. Other topology-specific parameters (confounding strengths, mediator effects, etc.) follow analogous alternating-sign pools. For $K{=}10$, $\\boldsymbol{\\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3)$.\n\n\\subsection{Proof of Theorem~\\ref{thm:monotone} (Confounding Monotonicity)}\n\\label{app:monotonicity_proof}\n\nUnder the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ for proportional effects ($f=\\lambda g$) and provide numerical verification for the general case.\nThe proof proceeds by direct algebraic analysis of $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$ as a rational function of $\\delta$, establishing convexity and bounding the derivative at both endpoints.\n\n\\paragraph{Proportional case ($f=\\lambda g$).}\nFrom Proposition~\\ref{prop:conf_prop}, $B(C)=\\lambda V_W/(V_W+\\sigma_T^2)$ where $V_W=\\operatorname{Var}(g)-V_B$ and $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$.\n\n\\emph{Step 1: Convexity of $V_B(\\delta)$.}\nDefine $N_j(\\delta)=\\sum_k g_k\\,C(\\delta)_{jk}\\,p_k$ and $q_j(\\delta)=\\sum_k C(\\delta)_{jk}\\,p_k$.\nBoth are affine in $\\delta$, with $q_j(\\delta)>0$.\nThen $V_B(\\delta)=\\sum_j N_j(\\delta)^2/q_j(\\delta) - \\bar{g}^2$.\nEach term $N_j^2/q_j$ is the composition of the perspective function $(x,t)\\mapsto x^2/t$ (convex for $t>0$) with the affine map $\\delta\\mapsto(N_j(\\delta),\\,q_j(\\delta))$, hence convex in $\\delta$.\nA sum of convex functions is convex, so $V_B(\\delta)$ is convex on $[0,\\delta_{\\max}]$.\n\n\\emph{Step 2: Derivative formula.}\nLet $\\mu_j(\\delta)=N_j(\\delta)/q_j(\\delta)=\\mathbb{E}[g(A)\\mid A^*{=}j]$.\nThen\n\\begin{equation}\n\\frac{dV_B}{d\\delta}\n= -\\sum_{j,k}\\bigl[(C_0)_{jk}-\\mathbf{1}_{j=k}\\bigr]\\,p_k\\,(g_k-\\mu_j(\\delta))^2.\n\\label{eq:dVB}\n\\end{equation}\n\\emph{Derivation.}\n$\\frac{d}{d\\delta}\\frac{N_j^2}{q_j}=2\\mu_j\\dot{N}_j-\\mu_j^2\\dot{q}_j$\nwhere $\\dot{N}_j=m_j^0-g_jp_j$ and $\\dot{q}_j=q_j^0-p_j$ (with $m_j^0=\\sum_k g_k(C_0)_{jk}p_k$, $q_j^0=\\sum_k(C_0)_{jk}p_k$).\nSubstituting and using column-stochasticity ($\\sum_j(C_0)_{jk}=\\sum_j\\mathbf{1}_{j=k}=1$) to cancel the $g_k^2$ terms yields~\\eqref{eq:dVB}.\n\n\\emph{Step 3: $V_B'(0)\\leq 0$ (universal, no conditions on $C_0$).}\nAt $\\delta{=}0$: $\\mu_j(0)=g_j$ (since $C(0)=I$), so $(g_k-\\mu_j(0))^2=(g_k-g_j)^2$.\nThe diagonal terms ($j{=}k$) vanish.\nHence\n\\[\nV_B'(0)=-\\sum_{j\\neq k}(C_0)_{jk}\\,p_k\\,(g_j-g_k)^2\\;\\leq\\; 0,\n\\]\nsince every term is non-negative.\n\n\\emph{Step 4: $V_B'(1)\\leq 0$ for $K{=}2$.}\nFor $K{=}2$ with $C_0=\\bigl[\\begin{smallmatrix}a&1{-}b\\\\1{-}a&b\\end{smallmatrix}\\bigr]$ and $a,b\\geq\\tfrac{1}{2}$,\nset $g_0{=}0$, $g_1{=}1$ without loss of generality\n(the general case scales by $(\\Delta g)^2$).\nAt $\\delta{=}1$: $q_0{=}ap_0{+}(1{-}b)p_1$, $q_1{=}(1{-}a)p_0{+}bp_1$,\n$\\mu_0{=}(1{-}b)p_1/q_0$, $\\mu_1{=}bp_1/q_1$.\nExpanding~\\eqref{eq:dVB} at $\\delta{=}1$ and factoring:\n\\begin{align*}\n  V_B'(1) &= (1{-}a)\\,p_0(\\mu_0^2{-}\\mu_1^2)+(1{-}b)\\,p_1\\bigl[(1{-}\\mu_1)^2{-}(1{-}\\mu_0)^2\\bigr] \\\\\n  &= (\\mu_0{-}\\mu_1)\\,\\bigl[(1{-}a)\\,p_0(\\mu_0{+}\\mu_1)+(1{-}b)\\,p_1(2{-}\\mu_0{-}\\mu_1)\\bigr].\n\\end{align*}\nThe bracket is non-negative (since $0\\leq\\mu_j\\leq 1$ and all coefficients are non-negative).\nDirect calculation gives $\\mu_0{-}\\mu_1=p_0\\,p_1(1{-}a{-}b)/(q_0\\,q_1)$\n(expand $(1{-}b)\\,q_1-b\\,q_0=p_0(1{-}a{-}b)$).\nUnder $a,b\\geq\\tfrac{1}{2}$: $a{+}b\\geq 1$, so $\\mu_0{-}\\mu_1\\leq 0$ and $V_B'(1)\\leq 0$.\n\n\\emph{Step 5: Monotonicity from convexity.}\nSince $V_B$ is convex (Step~1), its derivative $V_B'$ is non-decreasing.\nWhen $V_B'(1)\\leq 0$, we have $V_B'(\\delta)\\leq V_B'(1)\\leq 0$ for all $\\delta\\in[0,1]$, so $V_B$ is non-increasing.\n\n\\emph{Step 6: $|B(\\delta)|$ is non-decreasing.}\n$V_W(\\delta)=\\operatorname{Var}(g)-V_B(\\delta)$ is non-decreasing (Step~5).\nThe function $h(x)=|\\lambda|\\,x/(x+\\sigma_T^2)$ is strictly increasing for $x\\geq 0$.\nHence $|B(\\delta)|=h(V_W(\\delta))$ is non-decreasing. \\qed\n\n\\paragraph{Condition on $C_0$.}\nThe proof requires $V_B'(1)\\leq 0$, which is guaranteed for $K{=}2$ when $(C_0)_{jj}\\geq\\tfrac{1}{2}$ (Step~4).\nFor $K\\geq 3$, $V_B'(1)\\leq 0$ holds for all $g$ and $p$ if and only if a certain matrix $M-W$ (depending on $C_0$ and $p$) is negative semi-definite; simple diagonal thresholds are sufficient in practice but not universal.\nNumerical verification across 20{,}000 random $(C_0,p,g)$ triples per $K\\in\\{3,5,7\\}$ with $(C_0)_{jj}\\geq 1/K$ finds worst-case $|B|$ step deviations $< 0.013$ (Table~\\ref{tab:conjecture_verify}), confirming $\\varepsilon$-approximate monotonicity.\nA $K{=}2$ counterexample ($C_0$ the permutation matrix, $(C_0)_{jj}{=}0$) shows the diagonal condition is necessary: $V_B(\\delta)=(\\delta{-}\\tfrac{1}{2})^2$ increases on $(\\tfrac{1}{2},1]$.\n\n\\paragraph{General case (non-proportional effects).}\n$|B(C(\\delta))|\\leq\\bar{B}(\\delta)$ where $\\bar{B}(\\delta)=\\sqrt{\\mathbb{E}[\\operatorname{Var}(g\\mid A^*_\\delta)]\\,\\mathbb{E}[\\operatorname{Var}(f\\mid A^*_\\delta)]}\\,/\\,D(\\delta)$ (Proposition~\\ref{prop:conf_gen}).\nBy the same convexity argument, each $\\mathbb{E}[\\operatorname{Var}(\\cdot\\mid A^*_\\delta)]$ is non-decreasing in $\\delta$, and $D(\\delta)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*_\\delta)]$ is non-decreasing.\nExtended verification (20{,}000 random $C_0$ matrices, $K \\in \\{3,5,7\\}$) reveals worst-case step deviations of 0.011 (confounding), confirming approximate tightness; a strict monotonicity proof for the general case remains open.\n\n\\subsection{Mediation Topology ($A$ = Mediator)}\n\\label{app:mediation}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\to Y$, $T\\to Y$.\n\\begin{align*}\n  T &\\sim \\operatorname{Bernoulli}(0.5),\\\\\n  A\\mid T &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\gamma}+\\boldsymbol{\\delta}\\,T)\\bigr),\\\\\n  Y &= \\tau_{\\mathrm{dir}}\\,T + f(A) + \\varepsilon_Y.\n\\end{align*}\n\n\\paragraph{Bias decomposition.}\nBy Lemma~\\ref{lem:bias_decomp}, the direct-effect estimator satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C) = \\tau_{\\mathrm{dir}} + \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:med_bias}\n\\end{equation}\n\nThe key structural difference from confounding: $T$ \\emph{causes} $A$, so the residual covariance $\\operatorname{Cov}(T,f(A)\\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.\n\n\\paragraph{Endpoint analysis.}\n\nAt $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\\to A\\to Y$, so $\\operatorname{Cov}(T,f(A)\\mid A)=0$ and $\\operatorname{plim}\\hat\\tau=\\tau_{\\mathrm{dir}}$.\n",
      "numLines": 100,
      "startLine": 230,
      "totalLines": 1525
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the mathematical structure. Let me understand the key points:

1. **V_B(δ) = Var(E[g(A)|A*_δ])** is the between-group variance
2. **V_B is convex** in δ (perspective function argument)
3. **V_B'(0) ≤ 0** always holds
4. **If V_B'(1) ≤ 0**, then by convexity, V_B is non-increasing on [0,1]


5. For K=2, the condition V_B'(1) ≤ 0 reduces to (C₀)_{jj} ≥ 1/2, but for K≥3 it's equivalent to a matrix M-W being negative semidefinite

Now I need to work out the general derivative V_B'(1) and identify what this matrix M-W actually is, then show it's NSD under diagonal dominance conditions.

Starting from the derivative formula, at δ=1 where C(1) = C₀, I can separate the diagonal and off-diagonal contributions. The diagonal terms give me a positive contribution proportional to (1 - (C₀)_{jj}), while the off-diagonal terms subtract out the cross-group variance effects. The key insight is that C₀ being column-stochastic constrains how these pieces fit together. I'm rewriting this expression by factoring out the covariance matrix terms and separating the diagonal from off-diagonal components, then expanding the squared term to isolate how g_k appears in the quadratic form.

Now I'm working through the conditional distribution more carefully—given A*=j under C₀, the probability of observing A=k follows from the covariance structure weighted by the marginal probabilities, which lets me express the conditional mean μ_j and set up the conditional variance calculation. I'm completing the law of total variance relationship, so the conditional variance term equals Var(g) minus the between-group variance. Now I need to work through the second term in the derivative, which is a weighted sum of squared deviations between the group means and conditional means. Let me try re-deriving the derivative more carefully by going back to the original formula and expanding it systematically.

Expanding the squared term and distributing the summation across the three resulting components...

The first term vanishes because the columns of the transition matrix sum to zero. For the third term, I can use the fact that summing over k gives me the difference between the stationary distribution q and the initial distribution p. The second term requires collecting the μ_j coefficients and examining what happens when I sum over k.

Now I'm simplifying the second term by recognizing that the inner sum equals q_j μ_j by definition, which lets me expand and combine all three terms together to get the final expression for V_B'(1). I need to recalculate this more carefully. Let me expand the variance expression properly by factoring out the squared term and simplifying the algebra step by step. Now I'm expanding that squared term and simplifying—the $\sum_j p_j g_j^2$ terms cancel out, leaving me with $\sum_j q_j \mu_j^2 + \sum_j p_j \mu_j^2 - 2\sum_j p_j g_j \mu_j$. This form is cleaner, though I'm wondering if there's an even better way to express it.

Let me try a different angle using the between-group variance formula directly. I know that $V_B = \sum_j q_j \mu_j^2 - \bar{g}^2$ where $\bar{g}$ is the overall mean. If I substitute this into my expression for $V_B'(1)$, I can rewrite it as the between-group variance plus the within-group sum of squares minus another variance term—the calculation is getting close but I need to finish simplifying.

Now I see the full picture: $V_B'(1) = V_B(1) - \text{Var}(g) + \sum_j p_j (\mu_j - g_j)^2$. By the law of total variance, the first two terms combine to give the negative of the within-group variance, which is non-positive. The third term is always non-negative, so whether $V_B'(1)$ stays negative depends on whether the between-group differences outweigh the within-group variance.

The key insight is that this entire expression is a quadratic form in $g$, so I can represent it as a matrix equation and analyze when it's negative semidefinite. I'm working through the matrix algebra more carefully now. I need to express the first term as a quadratic form, so I'm computing L^T Q L where L relates the means μ to the parameter vector g. The product involves summing over j with the covariance matrix C₀, the probability vectors p and q, which is getting algebraically involved, so let me reorganize by defining diagonal matrices P and Q directly from the probability distributions. Now I'm expanding the quadratic form by distributing the matrix products and collecting terms with M_op, factoring out g^T and g to isolate the coefficient matrix that determines V_B'(1). So for V_B'(1) ≤ 0 to hold across all g vectors, W itself must be negative semidefinite. Now I'm working through the algebra to simplify W by substituting the definition of M_op and expanding each term—computing products like M_op^T Q M_op and M_op^T P M_op to see if there's a cleaner form.

The expression is getting messy with all these matrix products, so I'm trying a change of variables where u = P^{1/2} g to see if that transforms the problem into something more tractable. Actually, let me step back and return to the original derivative formula to find a cleaner way to express this condition.

Now I'm breaking down the derivative into diagonal and off-diagonal components, then regrouping the off-diagonal terms by column to see if there's a pattern. The key observation is that the sum of off-diagonal elements in each column relates to one minus the diagonal element. I'm applying Jensen's inequality to bound that sum, but the direction goes the wrong way—it makes the subtracted term larger, which would make the whole expression more negative. I need to flip my approach and show that the positive term is actually smaller than or equal to the negative term. Let me reframe this by defining a weighted average of the μ values for each column k, excluding the diagonal. (g_k - \mu_k)^2 - \sum_{j \neq k} \frac{(C_0)_{jk}}{1 - d_k} (g_k - \mu_j)^2]$$

For the derivative to be non-positive, the diagonal term—how far each group mean is from its own conditional mean—needs to be outweighed by the cross-terms measuring distances to other conditional means, weighted by the covariance structure.

This condition holds naturally when C₀ is diagonal-dominant: each g_k stays close to μ_k since most of the mass in column k concentrates on row k, while the other μ_j values are farther away. Let me try a more direct approach by setting up a quadratic form. If I define a vector where each component is the scaled deviation √(p_j)(g_j - μ_j), then the sum of squared deviations becomes the norm of that vector. But V_B'(1) mixes g_k with μ_j across different indices, so this simple decomposition doesn't capture the full structure. I need to compute V_B'(1) directly from the formula and identify the underlying matrix structure.

Using the derivative formula, I can express V_B'(1) as a quadratic form in g. Since μ_j depends linearly on g through the matrix L with entries L_{j\ell} = (C_0)_{j\ell} p_\ell / q_j, the squared term (g_k - μ_j)² becomes quadratic in g. Now I'm working out the explicit form of the matrix W that gives V_B'(1) = g^T W g by taking second derivatives with respect to the g components. I'm defining a matrix $\mathcal{M}$ that captures the weighted sum of outer products, then checking whether it's positive semidefinite—which would confirm that $V_B'(1) \leq 0$ holds under the diagonal dominance condition of $C_0$. I need to reconsider the sign structure here. The diagonal terms where j=k actually contribute positively to V_B' since the coefficient flips to (1 - (C_0)_{jj}), while the off-diagonal terms are negative contributions that could drive V_B' below zero depending on the magnitude of the correlation entries. Now I'm reformulating this in terms of quadratic forms—V_B'(1) equals g transposed times a matrix difference times g, where the diagonal component captures the within-group variance contributions and the off-diagonal component captures the between-group mixing. The condition for V_B'(1) to be non-positive is that the off-diagonal matrix dominates the diagonal one in the positive semidefinite ordering.

When the confusion matrix approaches perfect diagonal dominance, the diagonal elements trend toward one while off-diagonal elements vanish, which simultaneously drives both A_diag and A_offdiag toward zero—a degenerate case. But looking at the structure more carefully, under strong diagonal dominance the group means μ_j cluster tightly around their corresponding group centers g_j, while the cross-group differences (g_k - μ_j) for k≠j remain substantial.

This means the diagonal contribution (1-d_j) p_j (g_j - μ_j)² becomes negligible since μ_j ≈ g_j, whereas the off-diagonal terms (C₀)_{jk} p_k (g_k - μ_j)² stay significant because they involve the larger differences between distinct group centers. So the off-diagonal terms, which drive V_B'(1) negative, actually dominate under diagonal dominance.

To formalize this, I'm parameterizing the confusion matrix by its diagonal entries d_j and off-diagonal entries (C₀)_{jk} for j≠k. I'm simplifying this expression by substituting the definition of q_j, which lets me factor out the terms and show that g_j - μ_j is actually a weighted average of the differences (g_j - g_k). Under diagonal dominance, these weights become small, so the deviation from the mean is bounded by the maximum difference between any pair of values.

This algebraic approach is getting unwieldy, so I'm switching to the Gershgorin circle theorem instead—I need to verify that the matrix W (constructed from the diagonal and off-diagonal parts of A) has all non-positive eigenvalues to establish negative semi-definiteness.

Actually, let me try something more direct: I'll work with V_B'(1) and decompose it term by term to find a sufficient condition for it to be non-positive. For each index k, I'm separating the diagonal contribution (1 - d_k) p_k (g_k - μ_k)² from the off-diagonal terms involving (C₀)_{jk} p_k (g_k - μ_j)².

Since the off-diagonal entries of C₀ sum to 1 - d_k for each column, I can factor this out and rewrite the expression as a weighted average of squared differences, where the weights w_{jk} = (C₀)_{jk}/(1-d_k) form a probability distribution over j ≠ k.

For V_B'(1) to be non-positive, I need each component to satisfy a key inequality: the squared distance from g_k to its own mean μ_k must not exceed the weighted average of squared distances from g_k to all other means μ_j. Now I'm working through an expression for g_k - μ_k in terms of differences between the g values, which should help me verify whether this inequality actually holds.

I'm also computing g_k - μ_j for j ≠ k, which involves the full decomposition of μ_j. The algebra is getting intricate, so I'm shifting strategy to exploit strong diagonal dominance, which should give me the approximation that each μ_j is very close to g_j. I'm recognizing that the approximation approach has limits—I need a rigorous condition rather than just heuristic arguments. The core insight is that V_B is convex with V_B'(0) ≤ 0 already established, so if I can pin down that V_B'(1) ≤ 0 as well, the proof would be complete.

Let me work directly with the derivative formula by setting up the matrices precisely: defining P as the diagonal probability matrix, Q as the weighted row sums, and L as the normalized transition matrix, then showing that the matrix W appearing in V_B'(1) = g^T W g is negative semidefinite under diagonal dominance of C₀. Now I'm decomposing W into two parts: a sum over distinct indices that's negative semi-definite, and a diagonal sum that's positive semi-definite. For W to be negative semi-definite overall, the negative part needs to dominate the positive part.

Each rank-1 matrix (e_k - L_j)(e_k - L_j)^T contributes positively with weight (1-d_j)p_j along direction (e_j - L_j), while the negative contributions are weighted by (C₀)_{jk}p_k along direction (e_k - L_j). Under diagonal dominance where d_j is bounded below by η, the positive weights become small and the vectors (e_j - L_j) shrink since L_{jj} ≈ 1, which should help ensure the negative contributions dominate.

Let me check the boundary case where C₀ = I: then d_j = 1, all off-diagonal entries vanish, q_j = p_j, L = I, and both sums equal zero, so V_B'(1) = 0—this makes sense since C(δ) stays constant. For a small perturbation C₀ = I + εE with zero column sums, both the positive and negative parts grow linearly in ε, so I need to track which dominates at leading order.

Actually, I think computing the quadratic form directly might give cleaner insight into the structure.

Let me rewrite V_B'(1) using a centered version of g. If I define h_k = g_k - ḡ where ḡ is the weighted average of the g values, then since shifting all g_k by a constant doesn't change the variance of the conditional expectation, I can assume without loss of generality that the h_k values are centered. Then μ_j becomes a weighted sum of these centered values...

Actually, I realize that μ_j itself shifts by the same constant when g shifts, so g_k - μ_j is invariant under this transformation. This confirms that V_B'(1) depends only on the centered g values.

Now with the assumption that the g values are centered, I can express V_B'(1) in terms of the conditional means μ_j. Breaking down the formula, I get V_B'(1) equals V_B(1) plus a term involving the squared deviations of the conditional means from the actual g values, minus the variance of g itself.

Let me work through this more carefully by expanding what each piece represents and checking whether this simplifies to a clean relationship between the between-group and within-group variances. Now I'm computing V_B'(1) using the formula from Step 4, which factors as a product of (μ_0 - μ_1) and a bracket term involving the transition probabilities and means. Under the constraint that a, b ≥ 1/2, I can verify that V_B'(1) ≤ 0 since the first factor is non-positive and the bracket is non-negative. Since V_B'(1) = g^T W g, I need to establish that W is negative semidefinite by applying the Gershgorin circle theorem, which requires checking diagonal dominance conditions.

Now I'm working out the explicit matrix entries for W by computing the second derivatives with respect to g_a and g_b, using the fact that (g_k - μ_j) can be expressed as a linear combination of the g variables through the L matrix. The resulting expression for W_{ab} involves a double sum over j and k with terms involving the covariance matrix C₀ and the indicator differences.

The notation is getting unwieldy, so I'm going to switch to a computational approach—I'll write a Python script to numerically compute W for some random diagonally dominant matrices and verify my formula by checking the eigenvalues. This should help me confirm whether the matrix is indeed negative semidefinite under the diagonal dominance condition, and then I can work backward to find a cleaner analytical proof. I'm also thinking about whether there's a simpler way to reformulate this problem that avoids the heavy notation. I'm working through the algebra more carefully now—the Kronecker deltas do depend on k, so I can't factor them out of the sum. Let me split this into separate terms where I handle the products of deltas and the L matrix elements, being careful about which indices are summed over.

Now I'm evaluating each of the four resulting terms. For the first one, when a and b are different, the delta functions force k to equal both a and b simultaneously, which is impossible, so that vanishes. When a equals b, I get a simpler expression involving just the a-th index. I'm substituting the expression for $L_{jb}$ and defining a new matrix $S_{ab}$ to simplify the sum, which lets me rewrite Term 2 as $p_a p_b S_{ab} - (C₀)_{ab} p_a p_b / q_a$.

For Term 3, I'm applying symmetry by swapping the indices—since $S_{ab}$ is symmetric in $a$ and $b$, this gives me $p_a p_b [S_{ab} - (C₀)_{ba}/q_b]$.

Now I'm moving to Term 4, which involves a double sum over the loss terms and a difference between the transition matrix and the identity. Continuing the derivation by combining all the terms together to get the final expression for $W_{ab}$, which simplifies to show how the different components—the $S_{ab}$ terms, the inverse capacity matrix elements, and the $T_{ab}$ term—all contribute to the overall result. I'm factoring out the diagonal matrix of probabilities and recognizing that W has the form P·W̃·P, which means W is negative semidefinite if and only if W̃ is negative semidefinite. This reduces the problem to checking whether W̃ satisfies the necessary condition for V_B'(1) ≤ 0 across all possible g values.

Now I'm examining the explicit structure of W̃ by breaking it into components—a sum involving ratios of C₀ entries weighted by inverse q_j terms, plus a correction term involving p_j, minus two diagonal-like terms. Let me check what happens at the diagonal entries to understand the structure better. Now I'm recognizing that I can express these sums more elegantly using matrix notation. If I define S as C₀ᵀQ⁻¹C₀, then the diagonal and off-diagonal components of W̃ can be written in terms of this matrix and a similar one T involving the weighted terms with p_j. I'm factoring out the common terms and simplifying using the identity that I + PQ^{-1} equals Q^{-1}(Q + P), which lets me rewrite the expression more compactly before the calculation gets cut off. I'm getting tangled up in the index notation here—let me be more careful with the matrix dimensions and make sure I'm tracking which indices correspond to what. I need to verify that S, T, and the R terms all have compatible shapes before I can combine them into the expression for W̃. So $T_{ab}$ follows the same pattern with the weighting by $p_j$ over $q_j^2$, giving me $R^T P R$. The individual matrix entries check out as expected. Now I'm assembling the full expression for $\tilde{W}$ by combining these pieces: $R^T Q R + R^T P R$ minus the correction terms, which factors as $R^T(Q+P)R$ minus...

I'm checking whether $R$ has any special structure—specifically if it's row-stochastic. Since $C_0$ is column-stochastic, its row sums aren't constrained to equal one, so $R$ won't necessarily be row-stochastic either.

However, I notice that when I weight the rows by the vector $p$, something interesting happens: $\sum_b R_{jb} p_b = 1$, which means $R$ is $p$-stochastic. This connects to the matrix $L = RP$ I defined earlier, which is genuinely row-stochastic since its rows sum to one.

Now I'm working with the expression $\tilde{W} = R^T \Sigma R - R - R^T$ where $\Sigma = Q + P$ is a positive definite diagonal matrix. For the stability condition $V_B'(1) \leq 0$ to hold for all $g$, I need $\tilde{W}$ to be negative semidefinite, and since $Pg$ can span all of $\mathbb{R}^K$ when all $p_k > 0$, this requirement is both necessary and sufficient.

Let me test this with the special case where $C_0 = I$. Then $Q = P$, so $\Sigma = 2P$, and $R = P^{-1}$. Working through the algebra: $R^T \Sigma R = 2P^{-1}$ and $R + R^T = 2P^{-1}$, which means $\tilde{W} = 0$—confirming that the derivative is zero at the identity, as it should be.

Now I want to explore what happens when $C_0$ is close to the identity. Let me work through the matrix algebra more carefully. Since P⁻¹ is diagonal with entries 1/p_a, I need to track how it interacts with the diagonal matrix of r values. When I multiply P⁻¹ by diag(r), I get another diagonal matrix where each entry is r_j/p_j.

Now expanding the product R ≈ (P⁻¹ - εdiag(r_j/p_j)P⁻¹)(I+εE), I can distribute and keep only first-order terms in ε. This gives me P⁻¹ plus a correction term involving both E and the diagonal scaling. Looking at the individual entry R_{ja}, I get the identity contribution δ_{ja}/p_a plus a first-order correction that splits into two parts: one from the E matrix scaled by 1/p_a, and another from the r_j weighting that only appears on the diagonal.

For the diagonal entries where j = a, I have 1/p_a plus the E correction minus the r_a weighting term. Off-diagonal entries j ≠ a are purely first-order, just the E contribution. Now I need to compute W̃ = R^T ΣR - R - R^T to first order in ε, and I can verify that at zeroth order this vanishes as expected. The first-order calculation is getting complicated, so I'm going to switch to a numerical approach to check whether the conjecture holds before diving deeper into the algebra.

Actually, let me try a different strategy entirely—maybe I can write W̃ in a form that makes its negative semidefiniteness transparent. If I rearrange to get R + R^T - R^T ΣR, I'm looking for a way to express this as minus something positive semidefinite. I could try completing the square or finding a matrix A such that the expression factors nicely, though R might not be invertible which complicates things.

Let me work through whether A = Σ^{-1} works by expanding the completion-of-squares form and matching coefficients—if A^T Σ = I, then the cross terms A^T ΣR + R^T ΣA would give me exactly R + R^T, which is what I need. So I'm getting that $\tilde{W} = (R - \Sigma^{-1})^T \Sigma (R - \Sigma^{-1}) - \Sigma^{-1}$, and for this to be negative semidefinite, I need the quadratic form $(R - \Sigma^{-1})^T \Sigma (R - \Sigma^{-1})$ to stay bounded by $\Sigma^{-1}$, which translates to a norm constraint on the scaled deviation.

Expanding this out, the cross terms cancel and I'm left with $\|\Sigma^{1/2} R x\|^2 \leq 2 x^T R^T x$ as the key inequality to satisfy.

Wait, I need to be careful here—$x^T R^T x$ isn't necessarily symmetric unless $R$ is symmetric, which it isn't. Let me reconsider the algebra. The condition $\tilde{W} \preceq 0$ should translate to $(R-\Sigma^{-1})^T \Sigma (R-\Sigma^{-1}) \preceq \Sigma^{-1}$, which gives me a cleaner form to work with.

Now I'm substituting $y = \Sigma^{1/2}(R-\Sigma^{-1})x$ to simplify the quadratic form, which lets me rewrite the inequality in terms of norms and expand out the cross terms. I'm realizing this approach has a constraint issue—since z and x are linked by z = Rx, I can't treat them as independent variables, so the inequality doesn't simplify cleanly. Let me step back and analyze the quadratic form directly instead.

Looking at the expression for V_B'(1), I need to show it's non-positive under diagonal dominance by examining how the diagonal terms (1-d_k)p_k(g_k - μ_k)² balance against the off-diagonal coupling terms. I'm trying a change of variables using weighted, centered perturbations φ_j to capture the structure, though I need to be careful about what the centering condition actually implies. I'm switching to a direct approach—computing V_B'(1) and bounding each term to show it's non-positive. For column k, I'm isolating its contribution by separating the diagonal term from the off-diagonal interactions, then using the constraint that the weights sum to 1 - d_k to compare the two parts. the first term only involves $\mu_k$ while the second averages over $\mu_j$ for $j \neq k$.

$\text{col}_k = (1-d_k) p_k \left[(g_k - \mu_k)^2 - \sum_{j \neq k} \frac{(C_0)_{jk}}{1-d_k} (g_k - \mu_j)^2\right]$

For this to be ≤ 0, we need:
$(g_k - \mu_k)^2 \leq \sum_{j \neq k} w_{jk} (g_k - \mu_j)^2$ where $w_{jk} = \frac{(C_0)_{jk}}{1-d_k}$ for $j \neq k$.

This is saying the squared distance from $g_k$ to its own conditional mean $\mu_k$ must be bounded by a weighted average of squared distances to the other conditional means. I can express $g_k - \mu_k$ as a weighted combination of differences between $g_k$ and other $g_\ell$ values, which gives me a bound in terms of the maximum pairwise distance among the $g$ values. I'm realizing my bound isn't quite right—C₀ is column-stochastic, not row-stochastic, so the row sums aren't necessarily constrained. Let me reconsider: the sum of off-diagonal elements in row k is bounded by q_k itself, which means the coefficient simplifies to something involving the difference between q_k and d_k p_k.

The column-by-column approach seems problematic because the local condition I need doesn't hold independently for each k. I should step back and think about what would actually make the global quadratic form negative semidefinite.

Let me try a numerical approach to verify this...

Writing verification script...

But I'm also noticing something from the K=3 symmetric case that might generalize. The key was showing the derivative stays negative everywhere, not just at endpoints. The factor that made this work was universally negative across all points. For the general K case, I need to examine whether the derivative formula can be shown to be non-positive throughout.

Looking at the derivative more carefully, I see the off-diagonal terms contribute negatively while diagonal terms are positive, so I need the off-diagonal dominance to hold. The diagonal contribution comes from the difference between 1 and the diagonal entries of C₀, weighted by the squared deviations. Let me reconsider the exact form of this derivative to make sure I'm tracking which matrix entries matter.

For the convexity argument, if V_B is convex and V_B'(0) ≤ 0, then showing V_B'(1) ≤ 0 would mean the derivative stays non-positive throughout [0,1] by the monotonicity property of convex functions. But I should double-check whether I have the direction of this argument correct by looking back at the proof structure.

Actually, the key insight is that the entire proof reduces to establishing V_B'(1) ≤ 0 under the M-W matrix condition, since convexity of V_B guarantees that a non-positive derivative at the endpoint extends to the entire interval.

Now I'm going to verify this computationally and work through the analytical proof in parallel. My approach is to write a Python script that tests random diagonally dominant matrices, computing V_B'(1) and checking whether the associated matrix is negative semidefinite, then identify the tightest diagonal dominance threshold. For the analytical side, I'm exploring whether the Schur complement structure of the matrix can directly establish the negative semidefiniteness condition.

The key insight I'm pursuing is that if I can express the problem in terms of a substitution like z = Rx, I might be able to reduce it to a simpler inequality involving the relationship between z and x. Completing the inequality, I get $P \preceq (2C₀^{-1} - I)Q$, but the matrix $2C₀^{-1} - I$ isn't necessarily positive definite, and $Q$ itself depends on both $C₀$ and $p$, making this hard to work with. The approach does require $C₀$ to be invertible, which holds for diagonally dominant matrices, but verifying $P + Q \preceq 2C₀^{-1}Q$ in general seems intractable. Let me step back and try reformulating this using the original expression for $\tilde{W}$ directly.

I'm rewriting the condition as needing $x^T R^T \Sigma R x \leq x^T (R + R^T) x$ for all $x$, then attempting a substitution with $z = \Sigma^{1/2} R x$, but the resulting inequality doesn't simplify cleanly. Instead, I should leverage the structure that $C₀$ is column-stochastic and work with the row-stochastic matrix $L = Q^{-1}C₀P = RP$, where the entries relate to the normalized columns of $C₀$ scaled by the probability vector $p$.

Now I'm expanding the variance expression $V_B'(1)$ using the fact that $\mu_j = (Lg)_j$ represents a weighted average of the $g$ values, and I'm collecting terms to express it in matrix form as a quadratic in $\mu$.

I'm substituting $\mu = Lg$ and $\Sigma = P + Q$ into the expression, then factoring to get $g^T (L^T \Sigma L - 2PL) g$. But I need to verify whether the matrix $L^T \Sigma L - 2PL$ is symmetric for this to be a valid quadratic form, since $PL$ isn't necessarily symmetric.

Since any quadratic form can be expressed using its symmetric part, I'm taking the symmetrization: $W = L^T \Sigma L - PL - L^T P$, which gives me the effective matrix that properly defines the quadratic form.

Now I'm substituting the definitions $L = Q^{-1}C_0P$ and $\Sigma = P + Q$ to verify this matches my earlier work, expanding out the component-wise calculation for $W_{ab}$. Now I'm completing the calculation for $W_{ab}$ and verifying it matches the expected form. Since $W = P\tilde{W}P$ where $\tilde{W}$ is the normalized version, the negative semi-definiteness of $W$ depends on $\tilde{W}$. Moving forward, I'm analyzing $W = L^T \Sigma L - PL - L^T P$ using the fact that $L$ is row-stochastic, which means $\mathbf{1}$ is a right eigenvector with eigenvalue 1. Completing the calculation, I find that $L^T q = p$, which means $W\mathbf{1} = 0$—so the all-ones vector is in the null space of W. This makes intuitive sense: adding a constant to g doesn't affect the value function, so its derivative should vanish in that direction. Now I need to determine whether all other eigenvalues of this symmetric matrix are non-positive.

The key insight is that since g must satisfy the centering constraint $p^T g = 0$, I really need W to be negative semidefinite when restricted to that hyperplane. Let me reconsider whether the quadratic form $g^T W g$ is actually what appears in $V_B'(1)$, or if there's a different structure I'm missing. For W to be negative semidefinite, all eigenvalues need to be ≤ 0, and since we already have 0 as one eigenvalue, the remaining K-1 eigenvalues must also be non-positive. Since W is symmetric, its eigenvectors are orthogonal in the standard inner product, so I need to figure out how the eigenvector structure relates to the transformation through P.

Let me try a cleaner approach by substituting u = P^{1/2}g, which transforms the condition into requiring that the matrix P^{1/2} W P^{-1/2} be negative semidefinite. I'll define a new matrix as the symmetric transformation of W through P^{1/2}, and that's what needs to satisfy the NSD condition.

Now I'm working out the explicit form of this transformed matrix in terms of the components S, T, and C₀, and checking whether the stationary distribution vector has the right properties under this transformation. Since $P$ is invertible and $W\mathbf{1} = 0$, I can conclude that $\tilde{W}p = 0$, meaning $p$ is in the null space of $\tilde{W}$. Now I need to verify that $\hat{W}(P^{1/2}p) = 0$ as well, using the relationship $\hat{W} = P^{1/2}\tilde{W}P^{1/2}$. Now I need to find what vector actually satisfies the null condition for $\hat{W}$. If $\hat{W}v = 0$, then applying the definition gives me $P^{1/2}\tilde{W}P^{1/2}v = 0$, which means I need to solve for the right eigenvector.

Since $\tilde{W}p = 0$, the null space constraint tells me that $P^{1/2}v$ must be proportional to $p$, so $v = \alpha P^{-1/2}p$, which simplifies to $v = \alpha \sqrt{p}$ where the square root is applied element-wise.

I can verify that $\hat{W}\sqrt{p} = 0$ holds, and now I'm working toward the cleanest formulation of the weight matrix in terms of $L$ and $P$.

The key properties I need are that $W$ annihilates the all-ones vector and is negative semidefinite, which I can check by verifying that $g^T W g \leq 0$ for all vectors $g$. I'm exploring whether a diagonal dominance condition like $(C_0)_{kk} \geq 1/2$ for all $k$ would be sufficient to guarantee this, though the numerical evidence suggests I need to examine the specific case more carefully.

Looking at the empirical results with adversarial matrices, the error bounds stay quite small (under 0.017), which hints that the required condition might be weaker than I initially thought. The natural candidate is $d_k > 1/2$, which captures the idea that each column of the confusion matrix has more weight on its diagonal than spread across off-diagonal entries—exactly the condition that worked for the $K=2$ case.

Now I'm setting up the proof using the matrix formulation, checking whether $g^T W g \leq 0$ holds for all $g$ under this diagonal dominance condition, where $W$ encodes the stability properties of the algorithm. I'm working through the algebra to express $g^T W g$ in terms of the bias and variance components. Let me verify that $V_B(1) = \sum_j q_j \mu_j^2 - \bar{g}^2$ and $\text{Var}(g) = \sum_j p_j g_j^2 - \bar{g}^2$, then substitute these back to simplify the full expression. I'm expanding the expectation of the conditional variance using the transition matrix structure, then separating out the diagonal-matched terms from the off-diagonal contributions to get the full expression for $V_B'(1)$. I'm verifying that this expression matches what I derived earlier, which is good. Now I need to examine the condition for $V_B'(1) \leq 0$, which requires the diagonal contribution to be bounded by the expected conditional variance. I'm reorganizing the right-hand side by swapping the order of summation to group terms by k, which will help me analyze what each component contributes. I'm rearranging the inequality to isolate the difference between the matching distance and the weighted average, then expanding it to separate out the diagonal term from the off-diagonal ones to see what constraint this actually imposes. I'm applying Jensen's inequality to bound the weighted sum, which gives me $(g_k - \bar{\mu}_{-k})^2$ as a lower bound where $\bar{\mu}_{-k}$ is the weighted average of the other means. Now I need to connect this back to the original constraint—checking whether $(g_k - \mu_k)^2$ can actually be bounded by this expression. The term-by-term approach won't work because the inequality $|g_k - \mu_k| \leq |g_k - \bar{\mu}_{-k}|$ doesn't hold generally. I need to step back and use a global argument instead, leveraging the spectral properties of the matrix L. Since L is row-stochastic with largest eigenvalue 1 and eigenvector $\mathbf{1}$, and the diagonal dominance condition makes L close to the identity matrix, I should examine how the diagonal entries of L relate to the problem structure.

Actually, the diagonal entries depend on row sums of C₀, which can vary even when C₀ is column-stochastic, so this approach is getting complicated. Let me try a different angle using Cauchy-Schwarz on the quadratic form directly—I want to show that $\sum_j p_j(g_j - \mu_j)^2 \leq E[Var(g|A^*)]$, where the right side equals $Var(g) - V_B$.

Now I'm expanding both sides algebraically. The left side breaks down into terms involving $p_j g_j^2$, $p_j g_j \mu_j$, and $p_j \mu_j^2$. For the right side, I'm using the fact that $Var(g) = \sum_k p_k g_k^2 - \bar{g}^2$ and $V_B = \sum_j q_j(\mu_j - \bar{g})^2$, which simplifies to $\sum_j q_j \mu_j^2 - \bar{g}^2$. After canceling the $\bar{g}^2$ terms, the inequality reduces to a comparison between the weighted sums of squared deviations.

Rearranging, I get that $(p_j + q_j)\mu_j^2 \leq 2p_j g_j \mu_j$. Since $\mu_j$ is a linear combination of the $g_k$ values through the matrix $L$, I can express both sides in matrix form: the left becomes $g^T L^T \Sigma L g$ and the right becomes $2g^T PL g$, where $\Sigma$ is the diagonal matrix with entries $p_j + q_j$.

So I need $L^T \Sigma L \preceq PL + L^T P$ as a matrix inequality. Let me substitute $\mu = Lg$ to reframe this: the condition becomes $\mu^T \Sigma \mu \leq 2g^T P \mu$. Since $L$ might not be invertible, I can't directly invert it, but I can think about this geometrically—$L$ is row-stochastic with positive entries, so it maps the all-ones vector to itself and produces smoothed versions of $g$.

Now I'm trying different approaches to verify this inequality. Cauchy-Schwarz gives me a bound on $g^T P \mu$, but it bounds the right side from above, which doesn't help me establish a lower bound. AM-GM also goes the wrong direction—it bounds $2g^T P \mu$ from above using $g^T P g + \mu^T P \mu$, but I need to show the inequality holds, not find an upper bound on the RHS.

Let me decompose $g$ as $\mu$ plus a residual term $r = g - \mu$. Expanding $2g^T P \mu$ with this decomposition and substituting $\Sigma = P + Q$, I can rewrite the original condition as $\mu^T Q \mu - \mu^T P \mu \leq 2r^T P \mu$.

The left side becomes $\sum_j (q_j - p_j)\mu_j^2$ and the right side is $2\sum_j p_j(g_j - \mu_j)\mu_j$, but this doesn't lead anywhere obvious. Let me shift perspective and think about the spectrum of the transition matrix $L$, where $L_{jk} = (C_0)_{jk} p_k / q_j$. Since $L$ is row-stochastic, its eigenvalues are bounded in $[-1,1]$ with the Perron eigenvalue at 1, which might give me a handle on the matrix inequality $L^T \Sigma L \preceq PL + L^T P$.

The issue is that $L$ isn't symmetric, so its eigenvalues could be complex, making diagonalization tricky. Maybe I should try a different route using generalized Cauchy-Schwarz or Young's inequality instead, or work directly with the singular values to handle the non-symmetric case.

After manipulating the inequality algebraically, I'm getting a cleaner form: the difference between posterior and prior marginals, weighted by $\mu_j^2$, is bounded by a covariance-like term involving the residuals. Since $\mu_j$ is essentially a weighted average of $g$ with weights concentrated on $g_j$ when the covariance is diagonally dominant, this structure might give me leverage to bound the divergence.

Now I'm wondering which term shrinks faster as the covariance approaches the identity—the LHS measuring how much the posterior deviates from the prior, or the RHS capturing the residual structure. To explore this, I'm parameterizing the covariance as a perturbation around the identity matrix, where the perturbation is controlled by a small parameter $\epsilon$ and a column-stochastic matrix $E$ with zero diagonal.

For a more general column-stochastic covariance with diagonal entries $d_j = 1 - \epsilon_j$, I can decompose it so that each column $k$ is a convex combination of the identity component and an off-diagonal distribution $F_{jk}$. This gives me expressions for the posterior $q_j$ as a weighted average of the prior $p_j$ and the off-diagonal contributions, and similarly for the conditional expectation $\mu_j$. The difference $g_j - \mu_j$ then depends on how these terms balance out.

Working through the algebra, both $g_j - \mu_j$ and $q_j - p_j$ turn out to be first-order in $\epsilon$, which means the products appearing in the balance equations are second-order. The perturbative expansion is becoming quite involved, so let me step back and try a computational verification instead to build intuition, then return to the analytical argument. Actually, let me attempt one more direct approach by working through the specific case of three states with asymmetric transitions.

For K=3, the matrix W is 3×3 with W𝟏 = 0, so it has rank at most 2. For W to be negative semidefinite, I need both non-zero eigenvalues to be non-positive. This is equivalent to checking that the trace is non-positive and the determinant of the 2×2 principal minor is non-negative.

Now I'm working out the trace condition explicitly. The trace decomposes into weighted sums involving the matrix C₀ and the parameters p, q, and d. I can simplify the sum S_{aa} + T_{aa} by factoring out common terms, which gives me a cleaner expression to verify the trace constraint. I'm simplifying the numerator by factoring out $q_a$ and $d_a p_a$, then using the constraint that $d_a \leq 1$ to show this expression is non-positive, which means the first term contributes negatively to the overall sum.

The second term from the off-diagonal elements is strictly positive, so the sign of each diagonal entry in $\tilde{W}$ remains unclear—the Gershgorin circle theorem won't directly apply here without more careful analysis.

I should pivot to a computational approach: write a script to verify my matrix formula numerically, use it to experimentally identify the tightest diagonal dominance condition, then attempt a rigorous proof based on whatever structure the data reveals, possibly through a Schur complement argument or direct calculation.

Let me explore whether projecting onto the orthogonal complement of $\mathbf{1}$ clarifies the negative semidefiniteness. Since $W\mathbf{1} = 0$, I can use the projection $\Pi = I - \frac{1}{K}\mathbf{1}\mathbf{1}^T$ to work with $W$ restricted to this subspace, or define a weighted projection using the $P$-inner product—though this is getting complicated quickly.

I'll move forward with the direct computation and proof instead. The key insight is that $V_B'(1) \leq 0$ is equivalent to showing the weighted sum of squared deviations from group means is bounded by a cross-term involving the covariance matrix. I'll organize the proof by grouping contributions from each row $j$, where each term measures how much the group-specific effect $(g_j - \mu_j)$ contributes to the overall variance, weighted against the covariance structure. I'm trying to bound the sum from below by factoring out common terms, but this approach isn't yielding useful results. Let me shift strategy and try bounding the cross-term differently.

I can rewrite the sum involving the off-diagonal elements in terms of the conditional variance of g given the assignment, then subtract out the diagonal contribution to isolate what I need. I'm completing the algebraic simplification by splitting the sum and recognizing that the conditional variance term equals the total variance minus the between-group variance, which confirms the decomposition holds.

Now I'm interpreting what this inequality means: the left side measures how well the posterior means predict the actual values, while the right side represents the unexplained variance after accounting for group structure. Under near-identity covariance, both sides become small, so I need to examine their relative rates of decay through a perturbation analysis.

I'm decomposing the confusion matrix as a deviation from identity, separating the diagonal dominance (how well each group stays in itself) from the off-diagonal leakage (misclassification between groups). This lets me express the posterior probabilities and means in terms of these perturbation parameters, tracking how classification errors propagate through to affect the posterior estimates. Now I'm working through the variance calculation under the perturbation, expressing how the transition probabilities $L_{jk}$ relate to the original matrix elements and showing that the diagonal term stays close to 1 while off-diagonal terms scale with the exchange rates.

The key insight is that the variance conditional on the perturbed state is order $\epsilon$, while the between-group variance is only order $\epsilon^2$, which means the expected conditional variance dominates and drives $V_B'(1)$ negative—confirming the result holds when the original matrix has strong diagonal dominance.

Now I need to pin down the exact threshold where the sign of $V_B'(1)$ flips. The two-state case suggests $d_j \geq 1/2$ is the critical point, but I should verify whether this generalizes to arbitrary $K$ or if the threshold scales differently. Let me work through the algebra assuming $d_j \geq 1/2$ to see if I can establish this rigorously.

I'm applying Cauchy-Schwarz to bound the squared deviation term, which should help me show that the variance contribution becomes sufficiently small under this threshold to flip the sign of the derivative. I'm comparing $(g_k - \mu_j)^2$ with $(g_j - g_k)^2$ and noting they differ because the conditional mean $\mu_j$ isn't equal to $g_j$. Using the triangle inequality, I can bound the difference, and under strong diagonal dominance the gap $|g_j - \mu_j|$ should be small—I need to find a quantitative bound for it using the weighted sum of differences. I'm getting confused about the indexing here—I need to be careful about whether I'm looking at rows or columns. The column-stochastic property means each column of C₀ sums to 1, so for column k, the sum across all rows j should equal 1, which means the off-diagonal entries sum to 1 minus the diagonal entry. So the numerator simplifies to the sum over non-diagonal elements, and I can bound the absolute difference by factoring out the maximum gap between values, which gives me $(g_j - \mu_j) \leq \frac{q_j - d_j p_j}{q_j} \max_{k \neq j} |g_j - g_k|$. Under the diagonal dominance condition where $d_j \geq 1/2$, this ratio becomes tighter.

Now I'm checking whether the ratio $(q_j - d_j p_j)/q_j$ actually stays bounded—since $q_j \geq d_j p_j$, it's constrained to $[0, 1]$. But I'm realizing that column-diagonal dominance of $C_0$ alone doesn't guarantee $L$ is diagonally dominant, because $L$ depends on both the matrix entries and the marginals $p$. Let me test this with a uniform distribution where $p_k = 1/K$ for all $k$ to see if the bound holds.

With uniform $p$, the column sums become $q_j = \frac{1}{K}r_j$ where $r_j$ is the row sum of $C_0$, and the entries of $L$ scale as $(C_0)_{jk}$ divided by the row sum—making $L$ row-stochastic. Rather than keep chasing the theoretical conditions, I should just run a computational check to verify the formula works, find the actual threshold, and then construct the cleanest proof I can from there.

Actually, I'm noticing the proof structure more clearly now. The convexity of $V_B$ holds universally, and $V_B'(0) \leq 0$ is always true, but $V_B'(1) \leq 0$ requires a specific constraint on $C_0$. Since $V_B'(1) = g^T W g$ where $W = L^T(P+Q)L - PL - L^T P$, I need to show $W \preceq 0$ under the right condition. Let me try framing this as an operator norm bound instead. I'm making a substitution with $u = P^{1/2}g$ to simplify the inequality, which transforms the right side nicely but leaves the left side as $u^T P^{-1/2} L^T \Sigma L P^{-1/2} u$. So I'm defining $M = P^{-1/2} L^T \Sigma L P^{-1/2}$ and $N = \tilde{L}$ to reframe this as a comparison between two quadratic forms: $u^T M u \leq 2 u^T N u$ for all $u$.

Now I'm realizing that since $\tilde{L}$ isn't necessarily symmetric, I need to account for both $N$ and $N^T$ in the condition, which gives me $M \preceq N + N^T$. Substituting the definitions of $M$ and $N$ in terms of the original matrices, I can expand everything out to see what constraints this actually imposes. I'm checking whether $\tilde{L}$ could be symmetric by examining the structure $\tilde{L}_{jk} = \sqrt{p_j p_k}/q_j \cdot (C₀)_{jk}$, which would require a specific relationship between the entries of $C₀$ and the weight parameters.

This symmetry condition is equivalent to the detailed balance property for reversible Markov chains, but that's too restrictive for the general case. Let me abandon this approach and instead work directly with the Cauchy-Schwarz inequality to establish the bound.

Now I'm expanding the right-hand side of the inequality to see what terms emerge when I distribute the products. - 2 g^T P \mu + \mu^T P \mu$, where the cross term expands to $\sum_j p_j g_j \mu_j$. Now I'm working through the inequality condition, simplifying to show that $\sum_j (p_j + q_j) \mu_j^2$ must be bounded above by the cross term.

Let me try proving this directly by rewriting the expression as $2\sum_j p_j \mu_j (g_j - \mu_j) + \sum_j (p_j - q_j) \mu_j^2$, which separates the problem into a weighted difference term and a term involving the difference between the p and q weights.

Since the p and q distributions both sum to 1, their difference sums to zero, so the second term can be rewritten as a variance-weighted expression. This is getting complicated, so I'll move forward with implementing the computational approach alongside a cleaner theoretical result: for column-stochastic matrices with diagonal entries at least 1/2 and any positive prior, the derivative at 1 is non-positive regardless of the choice of g.

Now I'm trying a fresh approach using the Schur complement to characterize when this condition holds, setting up a block matrix structure to analyze the relationship between the covariance, transition matrix, and stationary distribution. So L is indeed a Markov transition matrix with non-negative entries and rows that sum to 1. Now I'm trying to find its stationary distribution π where π^T L = π^T, but the calculation gets messy—it doesn't simplify to p being the stationary distribution, since that would require a specific condition on the column sums that doesn't obviously hold.

However, q does have a relationship to L through the matrix structure. Rather than continue wrestling with the algebra, I should just move forward with implementation—I'll write a verification script and a proof document to check this rigorously. My plan is to explicitly construct the matrix W, verify it numerically...

Actually, I think I see a cleaner approach using Cauchy-Schwarz. I can express the deviation $g_j - \mu_j$ as a weighted sum of differences between $g_j$ and other $g_k$ values, then apply Cauchy-Schwarz to bound the squared deviation... I'm completing the Cauchy-Schwarz bound by substituting back and establishing that the variance of $g$ given the state can be bounded in terms of the pairwise differences, then using this to constrain how far individual values can deviate from their conditional means. I'm expanding the variance term by decomposing it into differences between individual values and the mean, which gives me three components: the squared differences between states, a cross term involving the mean deviation, and a term with the sum of transition probabilities. Now I'm working through the variance calculation, substituting the relationship I derived and simplifying to show how the conditional variance decomposes into the sum of squared deviations between states and a correction term involving the absorption probability. Now I'm substituting the expression for the conditional variance and expanding the terms, which lets me combine the $(p_j + q_j)$ coefficients and reorganize the double sum over distinct indices. I'm about to apply the Cauchy-Schwarz inequality to bound this expression. Now I'm checking what condition ensures V_B'(1) ≤ 0, which requires the left side to be bounded by the right side. I notice the double sum on the right counts all ordered pairs (j,k) where j ≠ k, and since (g_j - g_k)² = (g_k - g_j)², this is equivalent to the same expression written with reversed indices.

But looking more carefully at the two sums, they're actually structured differently—the first has a weighted coefficient α_j multiplying an inner sum over k ≠ j, while the second is a direct double sum over all pairs (j,k). The key difference is how the matrix element (C_0)_{jk} is indexed relative to the pair of indices.

Wait, I need to be more precise here. Let me rewrite both expressions carefully to compare them directly. The RHS is a double sum over j and k ≠ j with (C_0)_{jk} p_k (g_k - g_j)^2, and the LHS bound has the same structure but with each term weighted by α_j. Since the squared difference (g_k - g_j)^2 equals (g_j - g_k)^2, these expressions have the same form—so the condition for the bound to hold is that α_j relates to the coefficients in a specific way.

Now I'm simplifying the inequality α_j ≤ 1, which gives me a condition on the parameters p_j, q_j, and d_j. Expanding the algebraic inequality and canceling terms to isolate the constraint. I'm working through the algebra to simplify this constraint, and I see that it depends on both the matrix C₀ and the vector p. But since we need this to hold for all possible p values, I need to reconsider what conditions on C₀ alone would guarantee this inequality universally. The issue is that when $p_j$ becomes very small while other probabilities are large, the cross-terms $\sum_{k \neq j} (C_0)_{jk} p_k$ can dominate and violate the constraint, even when $d_j \geq 1/2$. I'm checking this with a concrete example where $K=3$, $d_j = 2/3$, and the probability distribution is heavily skewed toward one component.

The Cauchy-Schwarz approach appears too loose to capture the actual constraint—it doesn't account for the dependence on the specific probability distribution. So either the diagonal dominance condition isn't sufficient to guarantee $V_B'(1) \leq 0$ for all $p$, or I need a tighter analysis that avoids the wasteful bounding step. Let me test this numerically with an extreme case to see if the derivative actually stays non-positive.

Computing the $q$ values for a specific configuration...

Now I'm calculating the conditional expectations $\mu_i$ by taking weighted averages of the test function values, normalized by the $q$ probabilities. Continuing to compute the variance components, I'm finishing the calculation of the between-group variance and then finding the expected value of the conditional variance by subtracting it from the overall variance.

The result shows that even at the extreme case, the derivative is negative, confirming the pattern holds. But the Cauchy-Schwarz inequality gave me a bound that was too loose, so I need to find a tighter argument by looking more carefully at how the weighted squared differences behave.

Let me shift strategies entirely. Instead of trying to bound the squared deviations separately and then compare them, I'll work directly with the expression for the derivative as a quadratic form in the differences between the g values.

Now I'm rewriting the second sum using the antisymmetry of the pairwise differences, which lets me combine terms over unordered pairs. For the first sum, I'm applying Cauchy-Schwarz to bound the squared deviation of each g_j from its mean in terms of a product involving the transition matrix entries and the pairwise differences. I'm introducing a coefficient $\gamma_j$ that captures the weighted interaction between variables, defined as $(p_j+q_j)(q_j - d_j p_j)/q_j^2$, and then establishing the condition needed for the Lyapunov function to be non-increasing: the sum of these weighted cross-terms must not exceed the original cross-term sum.

Since each term shares the non-negative factor $(C_0)_{jk}p_k\Delta_{jk}^2$, the inequality holds whenever $\gamma_j \leq 1$ for all $j$, which translates to $q_j(1-d_j) \leq d_j p_j$—but this condition breaks down at extreme parameter values. Numerically though, the Lyapunov derivative stays non-positive even when this sufficient condition fails, suggesting the Cauchy-Schwarz approach is too conservative because it treats each row independently without accounting for how the $\mu_j$ values couple them together. I need to find a tighter bound that leverages this coupling structure.

Let me work directly with the quadratic form instead of applying Cauchy-Schwarz. I can rewrite the Lyapunov derivative as a sum of weighted squared deviations minus cross-row interaction terms, where the weights are $\sigma_j = p_j + q_j$. The key is that each deviation $(g_j - \mu_j)$ can be expressed in terms of the differences between rows, which should reveal how the coupling actually constrains the expression. Now I'm introducing normalized weights that sum to one across the off-diagonal terms, which lets me rewrite the deviation as a weighted sum. Then I'm applying Jensen's inequality to bound the squared sum of weighted differences by the weighted sum of squared differences. At Cauchy-Schwarz equality, I can express $(g_j - \mu_j)^2$ in terms of the variance and the weighted sum of squared differences. The sufficient condition $\gamma_j \leq 1$ then simplifies to a polynomial inequality in $p_j$, $q_j$, and $d_j$ that matches what I derived earlier.

However, achieving equality requires a very restrictive structure: for each row $j$, all the $g_k$ values in the support of column $j$ must differ from $g_j$ by the same constant $c_j$. When $C_0$ is strictly positive, this means $g_k = g_j - c_j$ for all $k \neq j$, and this constraint must hold simultaneously for every $j$, which forces $g$ into a highly specific configuration that's generally impossible to satisfy.

For $K=3$, the constraints from different rows contradict each other—they force $g$ to be constant, which makes $V_B'(1) = 0$. Since strict positivity of $C_0$ with $K \geq 3$ prevents the Cauchy-Schwarz equality from holding across all rows simultaneously, the bound must be strict. This means I need to abandon the Cauchy-Schwarz approach and instead work directly with the quadratic form inequality, showing that the weighted sum of squared bracket terms is bounded by the double sum of weighted squared differences.

The key insight is that $\Delta_{jk} = g_j - g_k$ isn't arbitrary—it's antisymmetric and satisfies the cocycle condition, forming only a $(K-1)$-dimensional family parametrized by the vector $g$. This constraint is what ensures the global inequality holds even when individual row inequalities fail.

Now I'm wondering if I can exploit the antisymmetry $\Delta_{jk} = -\Delta_{kj}$ to derive a tighter bound. Let me rewrite the LHS using $a_{jk} = (C_0)_{jk}p_k$ and expand $\Delta_{jk} = g_j - g_k$ in terms of the individual $g$ values, factoring out the coefficients that depend on the row sums and weighted sums.

After simplifying, the cross terms cancel and I'm left with $\sum_j \sigma_j(g_j - \mu_j)^2$, which is exactly what I started with—so this approach doesn't yield any improvement.

Let me try a different strategy using the deficiency structure. I'll define $r_j = g_j - \mu_j$ to separate the deviation from the mean, then rewrite the bound in terms of these residuals and see if the antisymmetry constraint gives me something useful.

Expanding this out, the cross-coupling term becomes increasingly messy with multiple interaction terms between the residuals and mean differences, which suggests this algebraic path is getting more complicated rather than simpler. I should step back and think about what mathematical structure might actually help here.

I'm realizing that $V_B'(1)$ is fundamentally a quadratic form in $g$, which I can express as $g^T W g$ where the matrix $W$ combines the covariance structure through $\Sigma = P + Q$ with the row-stochastic matrix $L$ and the projection $P$. The key insight is that negative semidefiniteness of $W$ relates to bounding the spectral properties of $L$ in the $\Sigma$-norm, which ties together how the cost matrix $C_0$ and the stationary distribution $p$ interact through the covariance.

I'm wondering if there's a connection to reversible Markov chains here—specifically, whether the symmetrized form $P^{1/2}LP^{-1/2}$ has spectral radius at most 1, which would hold for reversible chains but not necessarily for $L$ in general. Let me try approaching this through the reverse Markov chain instead.

I'm defining the time-reversal operator $L^*$ and rewriting $V_B'(1)$ by expanding it in terms of the transition matrix and its adjoint, then isolating the key terms like $\|\mu\|_P^2$ and the inner products involving $g$ and $\mu$.

Now I'm simplifying the P-weighted terms by recognizing that $\|\mu\|_P^2 - 2\langle g, \mu\rangle_P$ can be rewritten as $\|g - \mu\|_P^2 - \|g\|_P^2$, so let me just expand this directly to verify the algebra. I'm simplifying the expression by substituting $r = g - \mu$ and expanding $\|g\|_P^2$ as $\|\mu + r\|_P^2$, then canceling the $\|r\|_P^2$ terms to isolate the relationship between the Q and P norms of $\mu$. Now I'm simplifying the expression by factoring out $L^T$ and combining the $P$ terms, which gives me $V_B'(1) = g^T L^T[\Sigma L - 2P]g$. Let me double-check this result by expanding it back out to make sure the algebra is correct. I need to check whether L is invertible to proceed. Since L is K×K with the property that $L\mathbf{1} = \mathbf{1}$, it might have a nontrivial null space, but for diagonally dominant matrices like C₀, L should be invertible. If so, I can express the condition for negative semidefiniteness as $\Sigma \preceq 2PL^{-1}$ applied to vectors in the range of L.

Now I'm working through the algebra: substituting $L = Q^{-1}C_0 P$ to get $L^{-1} = P^{-1}C_0^{-1}Q$, then translating the semidefinite constraint into a condition on $C_0^{-1}Q$ in terms of P and Q.

Rearranging gives $(2C_0^{-1} - I)Q \succeq P$, which is tricky to verify directly since Q itself depends on $C_0$ and P. Let me check the boundary case where $C_0 = I$: this gives $Q = P$, so the condition becomes $P \succeq P$, which holds with equality. For small perturbations around $C_0 = I$, the condition should persist by continuity, but I need to think through whether this generalizes.

Let me focus on a concrete symmetric structure where $C_0$ has constant diagonal and off-diagonal entries. Using Sherman-Morrison inversion...

Actually, I should be more careful with the algebra. If $C_0 = aI + b\mathbf{1}\mathbf{1}^T$ with $a = 1-Kc$ and $b = c$, then the inverse simplifies nicely since $a + Kb = 1$, giving me $C_0^{-1} = \frac{1}{a}I - \frac{c}{a}\mathbf{1}\mathbf{1}^T$.

Now checking the uniform case where $p = \frac{1}{K}\mathbf{1}$: applying $C_0$ to this gives back $\frac{1}{K}\mathbf{1}$, so the fixed point condition $Q = P$ holds. This means I can reduce the constraint $(2C_0^{-1} - I)Q \succeq P$ to checking whether $C_0^{-1} \succeq I$.

To verify this, I'm computing $C_0^{-1} - I$ and analyzing its eigenstructure. The difference factors as $\frac{c}{1-Kc}(KI - \mathbf{11}^T)$, which has eigenvalue $K$ in the $(K-1)$-dimensional subspace orthogonal to $\mathbf{1}$ and eigenvalue $0$ along $\mathbf{1}$ itself.

For this to be positive semidefinite, I need $c/(1-Kc) \geq 0$, which holds whenever $c > 0$ given the constraint $c \in (0, 1/K)$. So with uniform probabilities and symmetric $C_0$, the condition $V_B'(1) \leq 0$ is automatically satisfied without requiring diagonal dominance.

Now I'm extending this to the non-uniform case, where $Q_j = (1-Kc)p_j + c$ and I need to verify $(2C_0^{-1} - I)Q \succeq P$.

Expanding the matrix inequality and using the fact that $\mathbf{1}^T Q = 1$ since $Q$ is diagonal, I can simplify to $\frac{1+Kc}{1-Kc}Q - \frac{2c}{1-Kc}\mathbf{11}^T \succeq P$, and now checking the diagonal entries...

Substituting $q_j = (1-Kc)p_j + c$ into the diagonal constraint and simplifying through algebraic manipulation to isolate the conditions on $p_j$. I see that $p_j$ might actually be less than $1/K$, which means the diagonal condition can fail. But I realize I need to look beyond just the diagonal—what matters is whether the full matrix is positive semidefinite, which requires checking eigenvalues. Let me rewrite this in terms of the rank-1 perturbation structure: $(1+Kc)Q - 2c\mathbf{11}^T$ is a diagonal matrix plus a rank-1 update, so I can analyze its eigenvalues directly.

This analytical approach is getting unwieldy, so I'm going to pivot to numerical verification instead. I'll compute the matrix $W$ formula directly, find where diagonal dominance actually holds empirically, write up what I can prove rigorously, and create a verification script to validate the key claims.

The core theorem I want to establish is that diagonal dominance in $C_0$ (specifically when all diagonal entries are at least 1/2) guarantees $V_B'(1) \leq 0$ across all parameter choices. The numerical evidence supports this, but proving it analytically requires showing that a certain operator inequality holds—specifically that $L - 2\Sigma^{-1}P$ has the right spectral properties. I'm completing the algebraic manipulation to show the diagonal entries are non-positive by combining the fractions and using the constraint that $q_j \geq d_j p_j$ to bound the numerator, which establishes that the diagonal of $L - 2\Sigma^{-1}P$ is non-positive.

Now I'm recognizing the matrix structure: it has negative diagonal entries and non-negative off-diagonal entries, which means its negative is a Z-matrix with the right properties for an M-matrix. Rather than pursuing the matrix theory further, I should move forward with writing out the proof and code, anchoring everything on the key identity for $V_B'(1)$.

The proof strategy hinges on two critical bounds: the squared deviations $(g_j - \mu_j)^2$ scale as $O(\epsilon^2)$ where $\epsilon$ measures the worst-case deviation from the target, while the conditional variance $E[\text{Var}(g|A^*)]$ only scales as $O(\epsilon)$. To formalize this, I'm introducing a P-weighted centered version of $g$ to work with a cleaner constraint structure.

Now I'm trying a different matrix decomposition for $W$, breaking it down in terms of $L$, $\Sigma$, $P$, and $Q$ to see if I can apply positivity results or the Schur product theorem to establish the bounds more rigorously. Let me switch to cleaner notation by defining $E = L - I$, which captures the structure of the Laplacian matrix where diagonal entries are negative and off-diagonal entries are non-negative with rows summing to zero. Now I'm expanding $L^T PL - L^T P - PL$ in terms of $E$ to see if this algebraic manipulation simplifies.

After working through the expansion, I get $W = E^T PE + L^T QL - P$, and since both $E^T PE$ and $L^T QL$ are positive semidefinite, I need their sum to be dominated by $P$ for the stability condition to hold. This suggests decomposing the constraint into two separate conditions: $E^T PE \preceq \alpha P$ and $L^T QL \preceq (1-\alpha) P$ for some convex combination parameter $\alpha$.

Now I'm converting these matrix inequalities into spectral norm conditions. The first constraint becomes a bound on the squared spectral norm of the transformed error matrix, and the second involves the spectral norm of the transformed disturbance term, which I can express in terms of $Q^{1/2}LP^{-1/2}$ after substituting the relationship $L = Q^{-1}C_0P^{1/2}$.

The squared norm equals the largest eigenvalue of $P^{1/2}C_0^T Q^{-1}C_0P^{1/2}$. When $C_0 = I$, this simplifies nicely since $Q = P$, making the norm equal to 1, which forces $\alpha = 0$ for both conditions to be satisfied simultaneously.

For perturbations near the identity, the norm stays close to 1 while the error term shrinks quadratically, so the conditions remain feasible for sufficiently small perturbations with the right choice of $\alpha$. Getting a clean threshold like $d_j \geq 1/2$ would require explicit bounds on these operator norms, which is getting complicated.

I think I'll pivot to a more direct approach for the proof. I can cleanly establish that $V_B$ is convex using the perspective function argument regardless of the choice of $K$, and I can show that the derivative at zero is non-positive.

For the derivative at 1, I need the matrix $W = L^T(P+Q)L - PL - L^T P$ to be negative semidefinite. I can provide the explicit form of $W$, verify numerically that it's NSD when $d_j \geq 1/2$, and prove it rigorously for special cases like $K=2$ or symmetric $C_0$. For the general case, if a clean analytical proof doesn't emerge, I'll state it as a formally verified theorem.

Let me try one more angle: proving this for column-diagonally dominant matrices, which should cover most of the relevant cases.

Now I'm attempting a different approach by transforming the inequality $L^T(P+Q)L \preceq PL + L^T P$ through a similarity transformation using $P^{-1/2}$, which should simplify the structure and make the semidefiniteness easier to verify. I'm factoring out the transformed matrices to get $\tilde{L}^T(I + \tilde{Q})\tilde{L}$ where $\tilde{Q}$ is diagonal with entries $q_j/p_j$, then reformulating the condition as an inequality involving $M$. I'm substituting $y = \tilde{L}x$ to simplify the quadratic form, then expanding $x^T M x$ in terms of $y$ and trying to show it's non-positive by completing the square or finding a useful decomposition. Now I'm expanding the matrix $M$ and simplifying the expression by collecting terms, which gives me $(I-\tilde{L})^T(I-\tilde{L}) + \tilde{L}^T\tilde{Q}\tilde{L} - I$. For the condition $M \preceq 0$ to hold, I need both quadratic terms to be bounded by the identity matrix.

I'm considering sufficient conditions for this constraint—the operator norm approach would require both terms to individually satisfy a norm bound, but that's overly restrictive since they don't commute. A weaker approach is to check the condition pointwise for all unit vectors, requiring that the sum of squared norms stays below 1.

Now I'm substituting $y = \tilde{L}x$ and expanding the constraint algebraically. After simplifying, I get $\|y\|^2 + y^T\tilde{Q}y \leq 2x^Ty$, but trying to decompose this component-wise doesn't quite work since the cross terms don't separate cleanly.

Rewriting in terms of the diagonal entries, I have $\sum_j \frac{p_j+q_j}{p_j}y_j^2 \leq 2\sum_j x_j y_j$. I'm trying to apply Cauchy-Schwarz to bound the right side, but that gives me an upper bound when I actually need a lower bound to make progress. The inequality goes the wrong direction for what I need here.

For a stochastic matrix $\tilde{L}$ that's close to the identity, there might be a different approach... y \approx x$, so $2x^Ty \approx 2\|x\|^2$ while $\|y\|^2(1+\tilde{Q}) \approx \|x\|^2(1 + q_j/p_j)$.

For uniform p and symmetric C₀: $q_j = p_j$, so $(1+q_j/p_j) = 2$, and we need $2\|y\|^2 \leq 2x^Ty$, i.e., $\|y\|^2 \leq x^Ty$. Since $y = \tilde{L}x$ and $\tilde{L}$ is symmetric with all eigenvalues in $[0,1]$ (for symmetric C₀ with positive diagonal), we have $y^T y = x^T\tilde{L}^2 x$ and $x^Ty = x^T\tilde{L}x$. The inequality $\|y\|^2 \leq x^Ty$ holds because $\lambda^2 \leq \lambda$ for all $\lambda \in [0,1]$, so this case checks out. Now for the general case where $\tilde{L}$ isn't symmetric and could have complex eigenvalues—I think the key is that $L$ is a stochastic matrix, which might constrain its numerical range in a way that makes the inequality still work. I'm expanding the expression for $y_j$ in terms of the transformed matrix $\tilde{L}$ and its interaction with $x_k$, but this approach is getting quite complex. Let me shift to actually writing out the proof and code instead—I'll structure the writeup to include the derivation of $V_B'(1) = g^T W g$, the explicit form of $W$, the complete proof for $K=2$, numerical verification for general $K$, and a theoretical result for when $C_0$ has column diagonal dominance and $L$ satisfies a contraction property like $L^T P L \preceq P$.

Now I'm realizing that if $\tilde{L}^T \tilde{L} \preceq I$ holds—meaning $L$ is a contraction in the $P$-norm—then the norm of $y$ is bounded by the norm of $x$, which constrains what $\tilde{Q}$ can be for the inequality to hold in the limit where $y \approx x$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "139608b8-2fec-42aa-a428-0b99bb5652d4",
  "uuid": "fbc21f9e-c300-4694-95e2-bb71bf2bf3b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RAc84SmFNy2KtifuGffje",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3657,
      "cache_read_input_tokens": 47683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3657
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---
