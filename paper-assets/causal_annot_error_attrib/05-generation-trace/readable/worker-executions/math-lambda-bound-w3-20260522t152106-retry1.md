# math lambda bound w3 20260522T152106 retry1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_math_lambda_bound_w3_20260522T152106_retry1.log`
- **Structured JSON:** [`5aad089cecfdc716d691.json`](../../sessions/5a/5aad089cecfdc716d691.json)

## Before a recorded user message

59 recorded events

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
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
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
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "ed275261-099e-4230-b49d-79ac1af93268",
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
    "resetsAt": 1779475800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "71ee01b2-d7b3-4e80-97d0-936b407f0849",
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "a1ba3a57-ad10-48b2-8aa7-0f09df207757",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01YXiSMMGQgPnvcSQ5kWWAL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 17158,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17158
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01YanmcqDjNxWFNh3TB2wtAt`</summary>

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
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "cb67f789-1149-4001-9470-b631003a3e35",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01YXiSMMGQgPnvcSQ5kWWAL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 17158,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17158
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

### Tool result

_source line 6 · 2026-05-22T15:21:26.559Z_

<details><summary>↩ Tool result · `toolu_01YanmcqDjNxWFNh3TB2wtAt`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This assumption is satisfied when the LLM does not observe outcome-related text during annotation---for instance, when treatment labels are assigned from source documents that exclude outcome measurements.
15	
16	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.
17	
18	\subsection{Multi-Class Bias Expressions}
19	\label{sec:bias_expressions}
20	
21	For each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
22	
23	\paragraph{Confounding ($A$ = confounder).}
24	When $A$ confounds the $X{\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit
25	\begin{equation}
26	\label{eq:confounding}
27	\text{plim}\;\hat{\tau}(A^*) = \bigl(\mathbb{E}[Z^{\prime}Z]\bigr)^{-1}\mathbb{E}[Z^{\prime}X]\,\boldsymbol{\beta},
28	\end{equation}
29	where $Z = [X, \text{dummies}(A^*)]$, $\boldsymbol{\beta}$ contains the true coefficients, and the target parameter $\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\hat{\tau}$ is preserved: $\tau_{\text{sign\_flip}} = 0$ structurally.\footnote{This result is consistent with \citet{brenner1993}, who showed that the adjusted estimate with misclassified polytomous confounders can be biased toward or away from the null. Both findings hold simultaneously: misclassification degrades confounding control, producing residual bias whose magnitude can exceed the correctly adjusted estimate (amplification), but the treatment effect sign is never reversed. The distinction is between \emph{sign reversal} ($\text{sign}(\hat{\tau}) \neq \text{sign}(\tau)$, which we show never occurs) and \emph{amplification} ($|\hat{\tau}| > |\tau|$, which occurs universally in this topology).}
30	
31	\paragraph{Exposure ($A$ = treatment variable).}
32	When $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:
33	\begin{equation}
34	\label{eq:exposure}
35	\text{plim}\;\hat{\beta}_j(A^*) = \sum_{k=1}^{K} w_{jk}\,\beta_k,
36	\end{equation}
37	where $w_{jk}$ depends on the confusion matrix $C$ and the marginal distribution of $A$. Unlike the binary case, where non-differential misclassification guarantees attenuation toward the null~\cite{brenner1993}, the $K{\geq}3$ case permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \emph{sign reversal}. A near-permutation confusion matrix effectively swaps category labels, making sign reversal the dominant outcome (83.4\% under uniform Dirichlet prior). This failure mode is structurally impossible at $K{=}2$ because a $2{\times}2$ stochastic matrix with positive diagonal cannot reverse the sign of a single coefficient.
38	
39	\paragraph{Mediation ($A$ = mediator).}
40	When $A$ mediates the $X{\to}Y$ relationship, the direct effect estimator controlling for $A^*$ has probability limit
41	\begin{equation}
42	\label{eq:mediation}
43	\text{plim}\;\hat{\tau}_{\text{direct}}(A^*) = \tau_{\text{direct}} + \bigl(1 - \lambda(C)\bigr)\,\tau_{\text{indirect}},
44	\end{equation}
45	where $\lambda(C) \in [0,1]$ summarizes attenuation (Appendix~\ref{app:proof}, Proposition~3), with $\lambda(I) = 1$ under perfect classification. Misclassification ($\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\hat{\tau}_{\text{direct}}|$ but preserving the sign ($\tau_{\text{sign\_flip}} = 0$).
46	
47	\paragraph{Collider ($A$ = collider, conditioned on $A^*$).}
48	Conditioning on a collider $A$ of $X$ and $Y$ opens a spurious path. When we condition on $A^*$ instead, misclassification attenuates this spurious association because $A^*$ is a noisy proxy for $A$. The collider topology thus exhibits a \emph{protective} property: annotation error reduces rather than amplifies the bias from collider stratification, with $\tau_{\text{sign\_flip}} = 0$.
49	
50	\paragraph{M-bias ($A$ = intermediate collider).}
51	In the M-shaped DAG ($U_1 \to X$, $U_1 \to A$, $U_2 \to A$, $U_2 \to Y$, $X \to Y$), adjusting for $A$ introduces a small spurious association via the M-bias path~\cite{greenland2003}. Misclassifying $A$ weakens this adjustment, reducing the M-bias. This topology is \emph{immune}: $\hat{\tau}(A^*)$ is closer to $\tau$ than $\hat{\tau}(A)$ for all non-trivial confusion matrices, yielding $\text{ASV} = \infty$.
52	
53	\paragraph{Front-door ($A$ = front-door mediator).}
54	In the front-door DAG ($X \to A \to Y$ with unmeasured $U \to X$, $U \to Y$), the front-door estimator~\cite{bellemare_bloem2024} uses $A$ to identify effects despite unmeasured confounding. Misclassification attenuates both $X \to A$ and $A \to Y$ relationships, producing moderate bias with $\tau_{\text{sign\_flip}} = 0$.
55	
56	\paragraph{Instrumental variable ($A$ = instrument).}
57	The Wald estimator~\cite{angrist_imbens1995} $\hat{\tau}_{\text{IV}} = \hat{\text{cov}}(A^*, Y) / \hat{\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign, causing the ratio estimator to diverge or flip. Under random Dirichlet matrices, 52.6\% produce sign reversal, making IV the most fragile topology.
58	
59	\paragraph{Structural sign-flip guarantee.}
60	\begin{proposition}[Sign preservation---analytic results]
61	\label{prop:signflip}
62	Under non-differential misclassification with $C_{kk} > 0$ for all $k$:
63	\emph{(a)}~Confounding preserves sign when $\operatorname{sign}(\tau) = \operatorname{sign}(\tau {+} B_{\mathrm{OV}})$, where $B_{\mathrm{OV}} {=} \operatorname{Cov}(g(A),f(A))/\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\ref{app:confounding}).
64	\emph{(b)}~Collider preserves sign when $|\tau| > \sqrt{\operatorname{Var}(g)\operatorname{Var}(h)}/\mathbb{E}[\operatorname{Var}(T{\mid}A)]$ (Berkson attenuation; Appendix~\ref{app:collider}).
65	\emph{(c)}~Exposure can produce sign reversal for $K {\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\ref{app:exposure}).
66	\end{proposition}
67	
68	\paragraph{Empirical Finding 1} (Mediation, M-bias, front-door).
69	Sign preservation holds under topology-specific conditions: mediation requires $\operatorname{sign}(\tau_{\mathrm{dir}}) {=} \operatorname{sign}(\tau_{\mathrm{total}})$; front-door requires $\operatorname{sign}(\lambda\alpha_U) {=} \operatorname{sign}(\lambda\alpha_U {+} \operatorname{Cov}(T,f(A)))$; M-bias is attenuating for all $C$. Verified across 100{,}000 random matrices with zero violations (Appendix~\ref{app:conditions}); analytic proofs for general $K$ remain open.
70	
71	These conditions involve true DGP parameters, which in practice must be estimated. The ASV framework (§\ref{sec:asv}) provides a complementary assessment that does not require knowledge of the exact sufficient conditions.
72	
73	\subsection{Annotation Sensitivity Values}
74	\label{sec:asv}
75	
76	We introduce Annotation Sensitivity Values (ASVs) as a unified sensitivity analysis framework, analogous to E-values for unmeasured confounding~\cite{vanderweele_ding2017} but designed for annotation-induced bias.
77	
78	\paragraph{Parameterization.}
79	We parameterize the confusion matrix as $C(\delta) = (1{-}\delta)I + \delta C_0$, where $C_0$ is a reference confusion matrix (e.g., estimated from a validation set) and $\delta \geq 0$ controls the severity of misclassification. At $\delta{=}0$, classification is perfect; at $\delta{=}1$, classification matches $C_0$. Non-negativity of $C(\delta)$ requires $\delta \leq \delta_{\max} = \min_j \frac{1}{1 - (C_0)_{jj}}$. Since $(C_0)_{jj} \in [0,1]$, we have $\delta_{\max} \geq 1$ for all valid $C_0$, ensuring the full range $[0,1]$ is always feasible; all ASV computations are constrained to $[0, \delta_{\max}]$. In practice, $C_0$ is estimated from a finite validation set and subject to sampling uncertainty; we recommend bootstrapping $C_0$ and reporting ASV confidence intervals. The linear path $C(\delta)$ is the natural first-order approximation; alternative parameterizations (e.g., matrix exponential or Dirichlet-based paths) could capture nonlinear degradation but sacrifice the interpretability of $\delta$ as a scalar severity dial.
80	
81	\paragraph{Three ASV types.}
82	We define three complementary measures: (1)~\textbf{Magnitude ASV} $\delta^*_{\text{mag}} = \min\{\delta : |\text{plim}\;\hat{\tau}(C(\delta)) - \tau| > \epsilon\}$---analogous to E-values; (2)~\textbf{Significance ASV} $\delta^*_{\text{sig}} = \min\{\delta : |\text{plim}\;\hat{\tau}(C(\delta))| < z_{\alpha/2} \cdot SE(N)\}$---relevant for attenuating topologies; (3)~\textbf{Sign-flip ASV} $\delta^*_{\text{sf}} = \min\{\delta : \text{sign}(\hat{\tau}) \neq \text{sign}(\tau)\}$---exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.
83	
84	\begin{theorem}[Envelope monotonicity---confounding and mediation]
85	\label{thm:monotone}
86	For confounding and mediation topologies with proportional effects ($f = \lambda g$ for some scalar $\lambda$) under $C(\delta) = (1{-}\delta)I + \delta C_0$, $|B(C(\delta))|$ is monotonically non-decreasing in $\delta \in [0, \delta_{\max}]$.
87	\end{theorem}
88	
89	\emph{Proof sketch.} Both topologies reduce to $B(C(\delta)) {=} \lambda V_W(\delta)/(V_W(\delta) {+} \sigma^2)$ where $V_W(\delta) {=} \operatorname{Var}(g) {-} \operatorname{Var}(\mathbb{E}[g{\mid}A^*_\delta])$ and $\sigma^2$ is a topology-specific constant ($\sigma_T^2$ for confounding, $\mathbb{E}[\operatorname{Var}(T{\mid}A)]$ for mediation). As $\delta$ increases, $A^*$ becomes a noisier channel for $A$, so $\operatorname{Var}(\mathbb{E}[g{\mid}A^*_\delta])$ decreases by the data processing inequality, increasing $V_W$. Since $x/(x{+}c)$ is increasing for $c{>}0$, $|B|$ is non-decreasing (full proofs in Appendix~\ref{app:monotonicity_proof} and~\ref{par:med_monotone}). For general (non-proportional) effects, numerical verification across 10{,}000 random matrices confirms $\varepsilon$-approximate monotonicity with $\varepsilon < 0.02$ (Appendix~\ref{app:monotonicity_proof}).
90	
91	\begin{conjecture}[$\varepsilon$-approximate envelope monotonicity]
92	\label{conj:monotone}
93	For the five remaining non-IV topologies under $C(\delta) = (1{-}\delta)I + \delta C_0$: exposure and front-door are $\varepsilon$-approximately non-decreasing in $\delta$, and collider and M-bias (protective topologies) are $\varepsilon$-approximately non-increasing in $\delta$, with $\varepsilon < 0.06$ ($<$6\% of $\tau$). Verified across 10{,}000 random matrices per topology and $K \in \{3,5,7\}$ using analytic probability limits (Appendix~\ref{sec:conjecture_verify}).
94	\end{conjecture}
95	
96	The instrumental variable topology is excluded from Conjecture~\ref{conj:monotone}: the Wald estimator $\hat{\tau} = \hat{\gamma}_{Y{\sim}A^*} / \hat{\gamma}_{T{\sim}A^*}$ exhibits singularities when the first-stage coefficient passes through zero as $\delta$ increases, producing unbounded deviations ($>10^6$). This is a property of the Wald estimator itself, not of the ASV framework; magnitude ASV remains well-defined for IV away from first-stage singularities.
97	
98	When strict monotonicity holds only approximately ($\varepsilon < 0.06$), the reported ASV threshold $\delta^*$ may differ from the true threshold by at most $\varepsilon/\eta$ in $\delta$-units, where $\eta$ is the practitioner's bias tolerance. At the recommended $\eta = 10\%$, this uncertainty is below 0.6 $\delta$-steps---negligible for practical sensitivity assessment. Topology rankings (which topologies are most fragile) are preserved across all tested configurations.
99	
100	Binarization of $K{=}3$ annotations introduces additional topology-dependent bias (Appendix~\ref{app:binarization}).
101	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "8cbae9d0-b113-44c7-83e1-e1ad82a8c00d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Setup and Notation}\n\\label{sec:notation}\n\nLet $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \\mid A{=}k)$, where each column sums to one. Following \\citet{hernan_cole2009}, we represent this measurement process using \\emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.\n\n\\begin{definition}[Non-differential misclassification]\n\\label{def:nondiff}\nMisclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\\mathbf{Z}$ if $P(A^*{=}j \\mid A{=}k, Y, \\mathbf{Z}) = P(A^*{=}j \\mid A{=}k) = C_{jk}$ for all $j,k$.\n\\end{definition}\n\nThis assumption is satisfied when the LLM does not observe outcome-related text during annotation---for instance, when treatment labels are assigned from source documents that exclude outcome measurements.\n\nWe study seven canonical DAG topologies (Figure~\\ref{fig:dag_taxonomy})~\\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.\n\n\\subsection{Multi-Class Bias Expressions}\n\\label{sec:bias_expressions}\n\nFor each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\\tau$ denote the target causal parameter and $\\hat{\\tau}(A^*)$ the estimator using misclassified annotations.\n\n\\paragraph{Confounding ($A$ = confounder).}\nWhen $A$ confounds the $X{\\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:confounding}\n\\text{plim}\\;\\hat{\\tau}(A^*) = \\bigl(\\mathbb{E}[Z^{\\prime}Z]\\bigr)^{-1}\\mathbb{E}[Z^{\\prime}X]\\,\\boldsymbol{\\beta},\n\\end{equation}\nwhere $Z = [X, \\text{dummies}(A^*)]$, $\\boldsymbol{\\beta}$ contains the true coefficients, and the target parameter $\\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\\hat{\\tau}$ is preserved: $\\tau_{\\text{sign\\_flip}} = 0$ structurally.\\footnote{This result is consistent with \\citet{brenner1993}, who showed that the adjusted estimate with misclassified polytomous confounders can be biased toward or away from the null. Both findings hold simultaneously: misclassification degrades confounding control, producing residual bias whose magnitude can exceed the correctly adjusted estimate (amplification), but the treatment effect sign is never reversed. The distinction is between \\emph{sign reversal} ($\\text{sign}(\\hat{\\tau}) \\neq \\text{sign}(\\tau)$, which we show never occurs) and \\emph{amplification} ($|\\hat{\\tau}| > |\\tau|$, which occurs universally in this topology).}\n\n\\paragraph{Exposure ($A$ = treatment variable).}\nWhen $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:\n\\begin{equation}\n\\label{eq:exposure}\n\\text{plim}\\;\\hat{\\beta}_j(A^*) = \\sum_{k=1}^{K} w_{jk}\\,\\beta_k,\n\\end{equation}\nwhere $w_{jk}$ depends on the confusion matrix $C$ and the marginal distribution of $A$. Unlike the binary case, where non-differential misclassification guarantees attenuation toward the null~\\cite{brenner1993}, the $K{\\geq}3$ case permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \\emph{sign reversal}. A near-permutation confusion matrix effectively swaps category labels, making sign reversal the dominant outcome (83.4\\% under uniform Dirichlet prior). This failure mode is structurally impossible at $K{=}2$ because a $2{\\times}2$ stochastic matrix with positive diagonal cannot reverse the sign of a single coefficient.\n\n\\paragraph{Mediation ($A$ = mediator).}\nWhen $A$ mediates the $X{\\to}Y$ relationship, the direct effect estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:mediation}\n\\text{plim}\\;\\hat{\\tau}_{\\text{direct}}(A^*) = \\tau_{\\text{direct}} + \\bigl(1 - \\lambda(C)\\bigr)\\,\\tau_{\\text{indirect}},\n\\end{equation}\nwhere $\\lambda(C) \\in [0,1]$ summarizes attenuation (Appendix~\\ref{app:proof}, Proposition~3), with $\\lambda(I) = 1$ under perfect classification. Misclassification ($\\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\\hat{\\tau}_{\\text{direct}}|$ but preserving the sign ($\\tau_{\\text{sign\\_flip}} = 0$).\n\n\\paragraph{Collider ($A$ = collider, conditioned on $A^*$).}\nConditioning on a collider $A$ of $X$ and $Y$ opens a spurious path. When we condition on $A^*$ instead, misclassification attenuates this spurious association because $A^*$ is a noisy proxy for $A$. The collider topology thus exhibits a \\emph{protective} property: annotation error reduces rather than amplifies the bias from collider stratification, with $\\tau_{\\text{sign\\_flip}} = 0$.\n\n\\paragraph{M-bias ($A$ = intermediate collider).}\nIn the M-shaped DAG ($U_1 \\to X$, $U_1 \\to A$, $U_2 \\to A$, $U_2 \\to Y$, $X \\to Y$), adjusting for $A$ introduces a small spurious association via the M-bias path~\\cite{greenland2003}. Misclassifying $A$ weakens this adjustment, reducing the M-bias. This topology is \\emph{immune}: $\\hat{\\tau}(A^*)$ is closer to $\\tau$ than $\\hat{\\tau}(A)$ for all non-trivial confusion matrices, yielding $\\text{ASV} = \\infty$.\n\n\\paragraph{Front-door ($A$ = front-door mediator).}\nIn the front-door DAG ($X \\to A \\to Y$ with unmeasured $U \\to X$, $U \\to Y$), the front-door estimator~\\cite{bellemare_bloem2024} uses $A$ to identify effects despite unmeasured confounding. Misclassification attenuates both $X \\to A$ and $A \\to Y$ relationships, producing moderate bias with $\\tau_{\\text{sign\\_flip}} = 0$.\n\n\\paragraph{Instrumental variable ($A$ = instrument).}\nThe Wald estimator~\\cite{angrist_imbens1995} $\\hat{\\tau}_{\\text{IV}} = \\hat{\\text{cov}}(A^*, Y) / \\hat{\\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign, causing the ratio estimator to diverge or flip. Under random Dirichlet matrices, 52.6\\% produce sign reversal, making IV the most fragile topology.\n\n\\paragraph{Structural sign-flip guarantee.}\n\\begin{proposition}[Sign preservation---analytic results]\n\\label{prop:signflip}\nUnder non-differential misclassification with $C_{kk} > 0$ for all $k$:\n\\emph{(a)}~Confounding preserves sign when $\\operatorname{sign}(\\tau) = \\operatorname{sign}(\\tau {+} B_{\\mathrm{OV}})$, where $B_{\\mathrm{OV}} {=} \\operatorname{Cov}(g(A),f(A))/\\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\\ref{app:confounding}).\n\\emph{(b)}~Collider preserves sign when $|\\tau| > \\sqrt{\\operatorname{Var}(g)\\operatorname{Var}(h)}/\\mathbb{E}[\\operatorname{Var}(T{\\mid}A)]$ (Berkson attenuation; Appendix~\\ref{app:collider}).\n\\emph{(c)}~Exposure can produce sign reversal for $K {\\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\\ref{app:exposure}).\n\\end{proposition}\n\n\\paragraph{Empirical Finding 1} (Mediation, M-bias, front-door).\nSign preservation holds under topology-specific conditions: mediation requires $\\operatorname{sign}(\\tau_{\\mathrm{dir}}) {=} \\operatorname{sign}(\\tau_{\\mathrm{total}})$; front-door requires $\\operatorname{sign}(\\lambda\\alpha_U) {=} \\operatorname{sign}(\\lambda\\alpha_U {+} \\operatorname{Cov}(T,f(A)))$; M-bias is attenuating for all $C$. Verified across 100{,}000 random matrices with zero violations (Appendix~\\ref{app:conditions}); analytic proofs for general $K$ remain open.\n\nThese conditions involve true DGP parameters, which in practice must be estimated. The ASV framework (§\\ref{sec:asv}) provides a complementary assessment that does not require knowledge of the exact sufficient conditions.\n\n\\subsection{Annotation Sensitivity Values}\n\\label{sec:asv}\n\nWe introduce Annotation Sensitivity Values (ASVs) as a unified sensitivity analysis framework, analogous to E-values for unmeasured confounding~\\cite{vanderweele_ding2017} but designed for annotation-induced bias.\n\n\\paragraph{Parameterization.}\nWe parameterize the confusion matrix as $C(\\delta) = (1{-}\\delta)I + \\delta C_0$, where $C_0$ is a reference confusion matrix (e.g., estimated from a validation set) and $\\delta \\geq 0$ controls the severity of misclassification. At $\\delta{=}0$, classification is perfect; at $\\delta{=}1$, classification matches $C_0$. Non-negativity of $C(\\delta)$ requires $\\delta \\leq \\delta_{\\max} = \\min_j \\frac{1}{1 - (C_0)_{jj}}$. Since $(C_0)_{jj} \\in [0,1]$, we have $\\delta_{\\max} \\geq 1$ for all valid $C_0$, ensuring the full range $[0,1]$ is always feasible; all ASV computations are constrained to $[0, \\delta_{\\max}]$. In practice, $C_0$ is estimated from a finite validation set and subject to sampling uncertainty; we recommend bootstrapping $C_0$ and reporting ASV confidence intervals. The linear path $C(\\delta)$ is the natural first-order approximation; alternative parameterizations (e.g., matrix exponential or Dirichlet-based paths) could capture nonlinear degradation but sacrifice the interpretability of $\\delta$ as a scalar severity dial.\n\n\\paragraph{Three ASV types.}\nWe define three complementary measures: (1)~\\textbf{Magnitude ASV} $\\delta^*_{\\text{mag}} = \\min\\{\\delta : |\\text{plim}\\;\\hat{\\tau}(C(\\delta)) - \\tau| > \\epsilon\\}$---analogous to E-values; (2)~\\textbf{Significance ASV} $\\delta^*_{\\text{sig}} = \\min\\{\\delta : |\\text{plim}\\;\\hat{\\tau}(C(\\delta))| < z_{\\alpha/2} \\cdot SE(N)\\}$---relevant for attenuating topologies; (3)~\\textbf{Sign-flip ASV} $\\delta^*_{\\text{sf}} = \\min\\{\\delta : \\text{sign}(\\hat{\\tau}) \\neq \\text{sign}(\\tau)\\}$---exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.\n\n\\begin{theorem}[Envelope monotonicity---confounding and mediation]\n\\label{thm:monotone}\nFor confounding and mediation topologies with proportional effects ($f = \\lambda g$ for some scalar $\\lambda$) under $C(\\delta) = (1{-}\\delta)I + \\delta C_0$, $|B(C(\\delta))|$ is monotonically non-decreasing in $\\delta \\in [0, \\delta_{\\max}]$.\n\\end{theorem}\n\n\\emph{Proof sketch.} Both topologies reduce to $B(C(\\delta)) {=} \\lambda V_W(\\delta)/(V_W(\\delta) {+} \\sigma^2)$ where $V_W(\\delta) {=} \\operatorname{Var}(g) {-} \\operatorname{Var}(\\mathbb{E}[g{\\mid}A^*_\\delta])$ and $\\sigma^2$ is a topology-specific constant ($\\sigma_T^2$ for confounding, $\\mathbb{E}[\\operatorname{Var}(T{\\mid}A)]$ for mediation). As $\\delta$ increases, $A^*$ becomes a noisier channel for $A$, so $\\operatorname{Var}(\\mathbb{E}[g{\\mid}A^*_\\delta])$ decreases by the data processing inequality, increasing $V_W$. Since $x/(x{+}c)$ is increasing for $c{>}0$, $|B|$ is non-decreasing (full proofs in Appendix~\\ref{app:monotonicity_proof} and~\\ref{par:med_monotone}). For general (non-proportional) effects, numerical verification across 10{,}000 random matrices confirms $\\varepsilon$-approximate monotonicity with $\\varepsilon < 0.02$ (Appendix~\\ref{app:monotonicity_proof}).\n\n\\begin{conjecture}[$\\varepsilon$-approximate envelope monotonicity]\n\\label{conj:monotone}\nFor the five remaining non-IV topologies under $C(\\delta) = (1{-}\\delta)I + \\delta C_0$: exposure and front-door are $\\varepsilon$-approximately non-decreasing in $\\delta$, and collider and M-bias (protective topologies) are $\\varepsilon$-approximately non-increasing in $\\delta$, with $\\varepsilon < 0.06$ ($<$6\\% of $\\tau$). Verified across 10{,}000 random matrices per topology and $K \\in \\{3,5,7\\}$ using analytic probability limits (Appendix~\\ref{sec:conjecture_verify}).\n\\end{conjecture}\n\nThe instrumental variable topology is excluded from Conjecture~\\ref{conj:monotone}: the Wald estimator $\\hat{\\tau} = \\hat{\\gamma}_{Y{\\sim}A^*} / \\hat{\\gamma}_{T{\\sim}A^*}$ exhibits singularities when the first-stage coefficient passes through zero as $\\delta$ increases, producing unbounded deviations ($>10^6$). This is a property of the Wald estimator itself, not of the ASV framework; magnitude ASV remains well-defined for IV away from first-stage singularities.\n\nWhen strict monotonicity holds only approximately ($\\varepsilon < 0.06$), the reported ASV threshold $\\delta^*$ may differ from the true threshold by at most $\\varepsilon/\\eta$ in $\\delta$-units, where $\\eta$ is the practitioner's bias tolerance. At the recommended $\\eta = 10\\%$, this uncertainty is below 0.6 $\\delta$-steps---negligible for practical sensitivity assessment. Topology rankings (which topologies are most fragile) are preserved across all tested configurations.\n\nBinarization of $K{=}3$ annotations introduces additional topology-dependent bias (Appendix~\\ref{app:binarization}).\n",
      "numLines": 101,
      "startLine": 1,
      "totalLines": 101
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Grep · `toolu_01MPYgQ1mgKTUuH7xd79DRfS`</summary>

```json
{
  "pattern": "mediation|lambda|\\\\lambda",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "1f5f7ad3-95b1-4ba0-867b-2abf56859313",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01YXiSMMGQgPnvcSQ5kWWAL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 17158,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17158
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

### Tool result

_source line 8 · 2026-05-22T15:21:27.772Z_

<details><summary>↩ Tool result · `toolu_01MPYgQ1mgKTUuH7xd79DRfS`</summary>

```text
4:We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Empirical Finding~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
23:For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
65:For $D(C)>0$: decompose $T = g(A) + \varepsilon_T$ where $g(A)=\mathbb{E}[T\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).
142:If $f(A) = \lambda\,g(A)$ for some constant $\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then
157:When $f=\lambda g$: the between-group covariance in~\eqref{eq:lotc} becomes $\lambda\,\operatorname{Var}(\mathbb{E}[g\mid A^*])$, and $\operatorname{Cov}(g,f)=\lambda\,\operatorname{Var}(g)$.
158:So $R(C)=\lambda\bigl(\operatorname{Var}(g)-\operatorname{Var}(\mathbb{E}[g\mid A^*])\bigr)=\lambda\,V_W$, where $V_W=\operatorname{Var}(g)-V_B$ with $V_B=\operatorname{Var}(\mathbb{E}[g\mid A^*])$.
162:  B(C) = \frac{\lambda\,V_W}{V_W+\sigma_T^2},\qquad
163:  B_{\mathrm{OV}} = \frac{\lambda\,V}{V+\sigma_T^2},
235:Under the interpolation $C(\delta)=(1{-}\delta)I+\delta C_0$, we prove $|B(C(\delta))|$ is non-decreasing in $\delta$ for proportional effects ($f=\lambda g$) and provide numerical verification for the general case.
237:\paragraph{Proportional case ($f=\lambda g$).}
238:From Proposition~\ref{prop:conf_prop}, $B(C)=\lambda V_W/(V_W+\sigma_T^2)$ where $V_W=\operatorname{Var}(g)-V_B$ and $V_B(\delta)=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*_\delta])$.
247:The function $h(x)=|\lambda|\,x/(x+\sigma_T^2)$ is strictly increasing for $x\geq 0$ and $\sigma_T^2>0$.
257:\label{app:mediation}
341:Under the interpolation $C(\delta)=(1{-}\delta)I+\delta C_0$, we prove $|B(C(\delta))|$ is non-decreasing in $\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\lambda\,g(A)$ for some scalar $\lambda$, where $g(k)=\mathbb{E}[T\mid A{=}k]$.
351:Since $f=\lambda g$:
353:  R(C) &= \lambda\,\mathbb{E}[\operatorname{Var}(g(A)\mid A^*)] = \lambda\,V_W.
369:$B(C) = \lambda\,V_W/(V_W+\sigma_\varepsilon^2)$,
371:Since $V_W(\delta)$ is non-decreasing by DPI (same argument as \S\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\lambda|x/(x+\sigma_\varepsilon^2)$ is increasing, $|B(C(\delta))|$ is non-decreasing.
416:If $h(A)=\lambda\,g(A)$ for some constant $\lambda$, then $|B(C)|\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.
421:When $h=\lambda g$, the numerator becomes $-\lambda\,\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$ and the denominator is $\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$.
425:  |B(C)| = |\lambda|\,\frac{V^*}{\operatorname{Var}(T)-V^*}.
429:$|B(C)|\leq|\lambda|\,V_g/(\operatorname{Var}(T)-V_g)=|B(I)|$.
479:  Y &= f(A) + \lambda\,U + \varepsilon_Y,\quad \varepsilon_Y\perp(T,A,U).
489:Substituting $Y=f(A)+\lambda U+\varepsilon_Y$ and using $\varepsilon_Y\perp(T,A,A^*)$:
492:  = \underbrace{\frac{\lambda\,\alpha_U}{\operatorname{Var}(T)}}_{\text{confounding (constant)}}
500:$\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] + \lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]$.
509:and $\lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]=\frac{\lambda\alpha_U}{\operatorname{Var}(T)}\,D(C)$, yielding the constant first term after division by $D(C)$.
513:The confusion matrix $C$ modulates only the mediation-type leakage $B_{\mathrm{med}}(C)$, which has the same structure as in~§\ref{app:mediation}.
516:At $C=I$: $B_{\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\to A\to Y$ path), and $\operatorname{plim}\hat\tau(I)=\lambda\alpha_U/\operatorname{Var}(T)$ (pure confounding residual).
518:At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $B_{\mathrm{med}}=\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$, and $\operatorname{plim}\hat\tau_{\mathrm{nc}}=[\operatorname{Cov}(T,f(A))+\lambda\alpha_U]/\operatorname{Var}(T)$, the naive regression coefficient with no controls.
522:Since $B_{\mathrm{med}}(C)$ has the same structure as the mediation bias (§\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:
524:  \operatorname{sign}\!\bigl(\lambda\alpha_U\bigr)
525:  = \operatorname{sign}\!\bigl(\lambda\alpha_U + \operatorname{Cov}(T,f(A))\bigr).
530:With $\alpha_U{=}1.0$, $\lambda{=}1.0$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$, $\boldsymbol{\gamma}{=}(0,0.5,{-}0.3)$, $\boldsymbol{\delta}{=}(0,1.0,{-}0.8)$:
532:  \lambda\alpha_U/\operatorname{Var}(T) &= 1.0\times 1.0\,/\,2.0 = 0.500,\\
618:Front-door & $\operatorname{sign}(\lambda\alpha_U)=\operatorname{sign}(\lambda\alpha_U{+}\operatorname{Cov}(T,f))$ & Empirical & $\checkmark$ ($0.50$ vs $0.80$)\\
637:The sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.
783:[Omitted long matching line]
914:For HumAID ($K{=}10$, 56 scenarios), 55.4\% are flagged as magnitude-ASV-unsafe---IV, mediation, front-door, and exposure all trigger, while confounding, collider, and M-bias remain below 10\% bias (Figure~\ref{fig:asv_heatmap}). For CivilComments ($K{=}2$), 100\% of scenarios are ASV-unsafe despite $F_1$ ranging from $0.69$ (7B) to $0.82$ (frontier).
954:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "252e089f-530e-496f-9858-217ed3a8cf59",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "4:We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Empirical Finding~1), and the monotonicity proof for confounding (Theorem~\\ref{thm:monotone}).\n23:For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\\dots,D_{K-1}^*)$.\n65:For $D(C)>0$: decompose $T = g(A) + \\varepsilon_T$ where $g(A)=\\mathbb{E}[T\\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).\n142:If $f(A) = \\lambda\\,g(A)$ for some constant $\\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then\n157:When $f=\\lambda g$: the between-group covariance in~\\eqref{eq:lotc} becomes $\\lambda\\,\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$, and $\\operatorname{Cov}(g,f)=\\lambda\\,\\operatorname{Var}(g)$.\n158:So $R(C)=\\lambda\\bigl(\\operatorname{Var}(g)-\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\bigr)=\\lambda\\,V_W$, where $V_W=\\operatorname{Var}(g)-V_B$ with $V_B=\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$.\n162:  B(C) = \\frac{\\lambda\\,V_W}{V_W+\\sigma_T^2},\\qquad\n163:  B_{\\mathrm{OV}} = \\frac{\\lambda\\,V}{V+\\sigma_T^2},\n235:Under the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ for proportional effects ($f=\\lambda g$) and provide numerical verification for the general case.\n237:\\paragraph{Proportional case ($f=\\lambda g$).}\n238:From Proposition~\\ref{prop:conf_prop}, $B(C)=\\lambda V_W/(V_W+\\sigma_T^2)$ where $V_W=\\operatorname{Var}(g)-V_B$ and $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$.\n247:The function $h(x)=|\\lambda|\\,x/(x+\\sigma_T^2)$ is strictly increasing for $x\\geq 0$ and $\\sigma_T^2>0$.\n257:\\label{app:mediation}\n341:Under the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\\lambda\\,g(A)$ for some scalar $\\lambda$, where $g(k)=\\mathbb{E}[T\\mid A{=}k]$.\n351:Since $f=\\lambda g$:\n353:  R(C) &= \\lambda\\,\\mathbb{E}[\\operatorname{Var}(g(A)\\mid A^*)] = \\lambda\\,V_W.\n369:$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\n371:Since $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n416:If $h(A)=\\lambda\\,g(A)$ for some constant $\\lambda$, then $|B(C)|\\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.\n421:When $h=\\lambda g$, the numerator becomes $-\\lambda\\,\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$ and the denominator is $\\operatorname{Var}(T)-\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$.\n425:  |B(C)| = |\\lambda|\\,\\frac{V^*}{\\operatorname{Var}(T)-V^*}.\n429:$|B(C)|\\leq|\\lambda|\\,V_g/(\\operatorname{Var}(T)-V_g)=|B(I)|$.\n479:  Y &= f(A) + \\lambda\\,U + \\varepsilon_Y,\\quad \\varepsilon_Y\\perp(T,A,U).\n489:Substituting $Y=f(A)+\\lambda U+\\varepsilon_Y$ and using $\\varepsilon_Y\\perp(T,A,A^*)$:\n492:  = \\underbrace{\\frac{\\lambda\\,\\alpha_U}{\\operatorname{Var}(T)}}_{\\text{confounding (constant)}}\n500:$\\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)] + \\lambda\\,\\mathbb{E}[\\operatorname{Cov}(T,U\\mid A^*)]$.\n509:and $\\lambda\\,\\mathbb{E}[\\operatorname{Cov}(T,U\\mid A^*)]=\\frac{\\lambda\\alpha_U}{\\operatorname{Var}(T)}\\,D(C)$, yielding the constant first term after division by $D(C)$.\n513:The confusion matrix $C$ modulates only the mediation-type leakage $B_{\\mathrm{med}}(C)$, which has the same structure as in~§\\ref{app:mediation}.\n516:At $C=I$: $B_{\\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\\to A\\to Y$ path), and $\\operatorname{plim}\\hat\\tau(I)=\\lambda\\alpha_U/\\operatorname{Var}(T)$ (pure confounding residual).\n518:At $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$: $B_{\\mathrm{med}}=\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$, and $\\operatorname{plim}\\hat\\tau_{\\mathrm{nc}}=[\\operatorname{Cov}(T,f(A))+\\lambda\\alpha_U]/\\operatorname{Var}(T)$, the naive regression coefficient with no controls.\n522:Since $B_{\\mathrm{med}}(C)$ has the same structure as the mediation bias (§\\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:\n524:  \\operatorname{sign}\\!\\bigl(\\lambda\\alpha_U\\bigr)\n525:  = \\operatorname{sign}\\!\\bigl(\\lambda\\alpha_U + \\operatorname{Cov}(T,f(A))\\bigr).\n530:With $\\alpha_U{=}1.0$, $\\lambda{=}1.0$, $\\boldsymbol{\\beta}{=}(0,1.0,{-}0.5)$, $\\boldsymbol{\\gamma}{=}(0,0.5,{-}0.3)$, $\\boldsymbol{\\delta}{=}(0,1.0,{-}0.8)$:\n532:  \\lambda\\alpha_U/\\operatorname{Var}(T) &= 1.0\\times 1.0\\,/\\,2.0 = 0.500,\\\\\n618:Front-door & $\\operatorname{sign}(\\lambda\\alpha_U)=\\operatorname{sign}(\\lambda\\alpha_U{+}\\operatorname{Cov}(T,f))$ & Empirical & $\\checkmark$ ($0.50$ vs $0.80$)\\\\\n637:The sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.\n783:[Omitted long matching line]\n914:For HumAID ($K{=}10$, 56 scenarios), 55.4\\% are flagged as magnitude-ASV-unsafe---IV, mediation, front-door, and exposure all trigger, while confounding, collider, and M-bias remain below 10\\% bias (Figure~\\ref{fig:asv_heatmap}). For CivilComments ($K{=}2$), 100\\% of scenarios are ASV-unsafe despite $F_1$ ranging from $0.69$ (7B) to $0.82$ (frontier).\n954:[Omitted long matching line]",
    "numLines": 40
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01Lu88nVQZQSg7bb5CwsALqQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 255,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "fe605014-be51-4e34-bf87-690e7c77ade2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EMEeijToMYa6znMGSP3xCm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9671,
      "cache_read_input_tokens": 33399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9671
      },
      "output_tokens": 40,
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

_source line 10 · 2026-05-22T15:21:32.032Z_

<details><summary>↩ Tool result · `toolu_01Lu88nVQZQSg7bb5CwsALqQ`</summary>

```text
255	
256	\subsection{Mediation Topology ($A$ = Mediator)}
257	\label{app:mediation}
258	
259	\paragraph{Data-generating process.}
260	$T\to A\to Y$, $T\to Y$.
261	\begin{align*}
262	  T &\sim \operatorname{Bernoulli}(0.5),\\
263	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
264	  Y &= \tau_{\mathrm{dir}}\,T + f(A) + \varepsilon_Y.
265	\end{align*}
266	
267	\paragraph{Bias decomposition.}
268	By Lemma~\ref{lem:bias_decomp}, the direct-effect estimator satisfies:
269	\begin{equation}
270	  \operatorname{plim}\hat\tau_{\mathrm{dir}}(C) = \tau_{\mathrm{dir}} + \frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}.
271	  \label{eq:med_bias}
272	\end{equation}
273	
274	The key structural difference from confounding: $T$ \emph{causes} $A$, so the residual covariance $\operatorname{Cov}(T,f(A)\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.
275	
276	\paragraph{Endpoint analysis.}
277	
278	At $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\to A\to Y$, so $\operatorname{Cov}(T,f(A)\mid A)=0$ and $\operatorname{plim}\hat\tau=\tau_{\mathrm{dir}}$.
279	
280	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$): no information about $A$ is used, and
281	\begin{align*}
282	  \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] &= \operatorname{Cov}(T,f(A)),\\
283	  D(C) &= \operatorname{Var}(T) = 0.25.
284	\end{align*}
285	The indirect effect is $\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]$, and
286	\[
287	  \operatorname{Cov}(T,f(A)) = 0.25\,\tau_{\mathrm{ind}}.
288	\]
289	Hence at $C$ uniform: $\operatorname{plim}\hat\tau = \tau_{\mathrm{dir}}+\tau_{\mathrm{ind}} = \tau_{\mathrm{total}}$.
290	
291	\paragraph{Empirical Finding (Mediation sign preservation).}
292	\label{find:med_sign}
293	$\operatorname{sign}(\operatorname{plim}\hat\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{dir}})$ whenever $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$, where $\tau_{\mathrm{total}}=\tau_{\mathrm{dir}}+\tau_{\mathrm{ind}}$.
294	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.
295	
296	\begin{proof}
297	Let $R(C)=\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)]$ and $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]>0$.
298	
299	\emph{Endpoints.}
300	At $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.
301	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $R=\operatorname{Cov}(T,f(A))=0.25\,\tau_{\mathrm{ind}}$ and $D=\operatorname{Var}(T)=0.25$, giving $B=\tau_{\mathrm{ind}}$.
302	
303	\emph{Within-group structure for binary $T$.}
304	Since $T\in\{0,1\}$, the within-$A^*$-group bias admits a revealing decomposition.
305	Let $p_j=P(T{=}1\mid A^*{=}j)$.
306	Then $\operatorname{Var}(T\mid A^*{=}j)=p_j(1{-}p_j)$ and
307	\[
308	  \operatorname{Cov}(T,f(A)\mid A^*{=}j)
309	  = p_j(1{-}p_j)\bigl[\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]\bigr].
310	\]
311	Define $\delta_j=\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]$ as the \emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.
312	Then
313	\[
314	  B(C)=\frac{R(C)}{D(C)}
315	  =\frac{\sum_j q_j\,p_j(1{-}p_j)\,\delta_j}{\sum_j q_j\,p_j(1{-}p_j)}
316	  =\sum_j w_j\,\delta_j,
317	\]
318	a weighted average of the conditional indirect effects, with weights $w_j=q_j p_j(1{-}p_j)/\sum_\ell q_\ell p_\ell(1{-}p_\ell)\geq 0$ summing to 1.
319	
320	At $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\delta_j=f(j)-f(j)=0$ and $B=0$.
321	At $C$ uniform: $\delta_j=\tau_{\mathrm{ind}}$ for all $j$ and $B=\tau_{\mathrm{ind}}$.
322	
323	\emph{Sign preservation.}
324	When $\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have the same sign), the bias $B(C)\geq 0$ cannot oppose $\tau_{\mathrm{dir}}$, so sign is preserved trivially.
325	
326	When $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have opposite signs but $|\tau_{\mathrm{ind}}|<|\tau_{\mathrm{dir}}|$ (i.e., $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$), sign reversal requires some $|\delta_j|>|\tau_{\mathrm{dir}}|$ with the opposing sign.
327	Since each $\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\delta_j$, the bound $|B(C)|\leq\max_j|\delta_j|$ holds.
328	We verify numerically that $\max_j|\delta_j|\leq|\tau_{\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.
329	\end{proof}
330	
331	\paragraph{Verification for paper parameters ($K{=}3$).}
332	With $\tau_{\mathrm{dir}}{=}0.5$, $\boldsymbol{\gamma}{=}(0,0,0)$, $\boldsymbol{\delta}{=}(0,0.8,{-}0.6)$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$:
333	
334	$\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]=0.351$ (computed from the softmax class probabilities).
335	$\tau_{\mathrm{total}}=0.5+0.351=0.851>0$.
336	Since $\tau_{\mathrm{dir}}{>}0$ and $\tau_{\mathrm{total}}{>}0$, sign preservation holds for all $C$.
337	
338	\paragraph{Mediation monotonicity (proportional effects).}
339	\label{par:med_monotone}
340	
341	Under the interpolation $C(\delta)=(1{-}\delta)I+\delta C_0$, we prove $|B(C(\delta))|$ is non-decreasing in $\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\lambda\,g(A)$ for some scalar $\lambda$, where $g(k)=\mathbb{E}[T\mid A{=}k]$.
342	
343	\emph{Step 1: Decompose $T$ via the mediator.}
344	Define $g(A)=\mathbb{E}[T\mid A]$ and $\varepsilon_T = T - g(A)$.
345	By construction, $\mathbb{E}[\varepsilon_T\mid A]=0$.
346	By non-differential misclassification ($T\perp A^*\mid A$):
347	$\mathbb{E}[\varepsilon_T\mid A{=}k, A^*{=}j] = 0$,
348	so $\mathbb{E}[\varepsilon_T\mid A^*{=}j]=0$ and $\operatorname{Cov}(\varepsilon_T,\,g(A)\mid A^*{=}j)=0$ for every $j$.
349	
350	\emph{Step 2: Reduce the numerator.}
351	Since $f=\lambda g$:
352	\begin{align*}
353	  R(C) &= \lambda\,\mathbb{E}[\operatorname{Var}(g(A)\mid A^*)] = \lambda\,V_W.
354	\end{align*}
355	
356	\emph{Step 3: Constant additive term in denominator.}
357	\begin{align*}
358	  D(C) &= \mathbb{E}[\operatorname{Var}(T\mid A^*)]
359	       = V_W + \sigma_\varepsilon^2,
360	\end{align*}
361	where $\sigma_\varepsilon^2\equiv\mathbb{E}[\operatorname{Var}(\varepsilon_T\mid A^*)]$.
362	This is \emph{constant} (independent of $C$):
363	$\mathbb{E}[\operatorname{Var}(\varepsilon_T\mid A^*)]
364	  = \sum_k p_k\,\operatorname{Var}(T\mid A{=}k)
365	  = \mathbb{E}[\operatorname{Var}(T\mid A)]$,
366	where the equality uses column-stochasticity: $\sum_j q_j\,P(A{=}k\mid A^*{=}j)=p_k$.
367	
368	\emph{Step 4: Closed form and monotonicity.}
369	$B(C) = \lambda\,V_W/(V_W+\sigma_\varepsilon^2)$,
370	structurally identical to confounding (Proposition~\ref{prop:conf_prop}) with $\sigma_\varepsilon^2$ playing the role of $\sigma_T^2$.
371	Since $V_W(\delta)$ is non-decreasing by DPI (same argument as \S\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\lambda|x/(x+\sigma_\varepsilon^2)$ is increasing, $|B(C(\delta))|$ is non-decreasing.
372	
373	\subsection{Collider Topology ($A$ = Collider)}
374	\label{app:collider}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "0c2f6987-03bb-4a4e-84e0-cffc73effe6b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "\n\\subsection{Mediation Topology ($A$ = Mediator)}\n\\label{app:mediation}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\to Y$, $T\\to Y$.\n\\begin{align*}\n  T &\\sim \\operatorname{Bernoulli}(0.5),\\\\\n  A\\mid T &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\gamma}+\\boldsymbol{\\delta}\\,T)\\bigr),\\\\\n  Y &= \\tau_{\\mathrm{dir}}\\,T + f(A) + \\varepsilon_Y.\n\\end{align*}\n\n\\paragraph{Bias decomposition.}\nBy Lemma~\\ref{lem:bias_decomp}, the direct-effect estimator satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C) = \\tau_{\\mathrm{dir}} + \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:med_bias}\n\\end{equation}\n\nThe key structural difference from confounding: $T$ \\emph{causes} $A$, so the residual covariance $\\operatorname{Cov}(T,f(A)\\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.\n\n\\paragraph{Endpoint analysis.}\n\nAt $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\\to A\\to Y$, so $\\operatorname{Cov}(T,f(A)\\mid A)=0$ and $\\operatorname{plim}\\hat\\tau=\\tau_{\\mathrm{dir}}$.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ ($A^*\\perp A$): no information about $A$ is used, and\n\\begin{align*}\n  \\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)] &= \\operatorname{Cov}(T,f(A)),\\\\\n  D(C) &= \\operatorname{Var}(T) = 0.25.\n\\end{align*}\nThe indirect effect is $\\tau_{\\mathrm{ind}}=\\mathbb{E}[f(A)\\mid T{=}1]-\\mathbb{E}[f(A)\\mid T{=}0]$, and\n\\[\n  \\operatorname{Cov}(T,f(A)) = 0.25\\,\\tau_{\\mathrm{ind}}.\n\\]\nHence at $C$ uniform: $\\operatorname{plim}\\hat\\tau = \\tau_{\\mathrm{dir}}+\\tau_{\\mathrm{ind}} = \\tau_{\\mathrm{total}}$.\n\n\\paragraph{Empirical Finding (Mediation sign preservation).}\n\\label{find:med_sign}\n$\\operatorname{sign}(\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{dir}})$ whenever $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$, where $\\tau_{\\mathrm{total}}=\\tau_{\\mathrm{dir}}+\\tau_{\\mathrm{ind}}$.\nThis result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.\n\n\\begin{proof}\nLet $R(C)=\\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)]$ and $D(C)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]>0$.\n\n\\emph{Endpoints.}\nAt $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$: $R=\\operatorname{Cov}(T,f(A))=0.25\\,\\tau_{\\mathrm{ind}}$ and $D=\\operatorname{Var}(T)=0.25$, giving $B=\\tau_{\\mathrm{ind}}$.\n\n\\emph{Within-group structure for binary $T$.}\nSince $T\\in\\{0,1\\}$, the within-$A^*$-group bias admits a revealing decomposition.\nLet $p_j=P(T{=}1\\mid A^*{=}j)$.\nThen $\\operatorname{Var}(T\\mid A^*{=}j)=p_j(1{-}p_j)$ and\n\\[\n  \\operatorname{Cov}(T,f(A)\\mid A^*{=}j)\n  = p_j(1{-}p_j)\\bigl[\\mathbb{E}[f(A)\\mid T{=}1,A^*{=}j]-\\mathbb{E}[f(A)\\mid T{=}0,A^*{=}j]\\bigr].\n\\]\nDefine $\\delta_j=\\mathbb{E}[f(A)\\mid T{=}1,A^*{=}j]-\\mathbb{E}[f(A)\\mid T{=}0,A^*{=}j]$ as the \\emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.\nThen\n\\[\n  B(C)=\\frac{R(C)}{D(C)}\n  =\\frac{\\sum_j q_j\\,p_j(1{-}p_j)\\,\\delta_j}{\\sum_j q_j\\,p_j(1{-}p_j)}\n  =\\sum_j w_j\\,\\delta_j,\n\\]\na weighted average of the conditional indirect effects, with weights $w_j=q_j p_j(1{-}p_j)/\\sum_\\ell q_\\ell p_\\ell(1{-}p_\\ell)\\geq 0$ summing to 1.\n\nAt $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\\delta_j=f(j)-f(j)=0$ and $B=0$.\nAt $C$ uniform: $\\delta_j=\\tau_{\\mathrm{ind}}$ for all $j$ and $B=\\tau_{\\mathrm{ind}}$.\n\n\\emph{Sign preservation.}\nWhen $\\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{ind}}$ have the same sign), the bias $B(C)\\geq 0$ cannot oppose $\\tau_{\\mathrm{dir}}$, so sign is preserved trivially.\n\nWhen $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{ind}}$ have opposite signs but $|\\tau_{\\mathrm{ind}}|<|\\tau_{\\mathrm{dir}}|$ (i.e., $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$), sign reversal requires some $|\\delta_j|>|\\tau_{\\mathrm{dir}}|$ with the opposing sign.\nSince each $\\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\\delta_j$, the bound $|B(C)|\\leq\\max_j|\\delta_j|$ holds.\nWe verify numerically that $\\max_j|\\delta_j|\\leq|\\tau_{\\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.\n\\end{proof}\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau_{\\mathrm{dir}}{=}0.5$, $\\boldsymbol{\\gamma}{=}(0,0,0)$, $\\boldsymbol{\\delta}{=}(0,0.8,{-}0.6)$, $\\boldsymbol{\\beta}{=}(0,1.0,{-}0.5)$:\n\n$\\tau_{\\mathrm{ind}}=\\mathbb{E}[f(A)\\mid T{=}1]-\\mathbb{E}[f(A)\\mid T{=}0]=0.351$ (computed from the softmax class probabilities).\n$\\tau_{\\mathrm{total}}=0.5+0.351=0.851>0$.\nSince $\\tau_{\\mathrm{dir}}{>}0$ and $\\tau_{\\mathrm{total}}{>}0$, sign preservation holds for all $C$.\n\n\\paragraph{Mediation monotonicity (proportional effects).}\n\\label{par:med_monotone}\n\nUnder the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\\lambda\\,g(A)$ for some scalar $\\lambda$, where $g(k)=\\mathbb{E}[T\\mid A{=}k]$.\n\n\\emph{Step 1: Decompose $T$ via the mediator.}\nDefine $g(A)=\\mathbb{E}[T\\mid A]$ and $\\varepsilon_T = T - g(A)$.\nBy construction, $\\mathbb{E}[\\varepsilon_T\\mid A]=0$.\nBy non-differential misclassification ($T\\perp A^*\\mid A$):\n$\\mathbb{E}[\\varepsilon_T\\mid A{=}k, A^*{=}j] = 0$,\nso $\\mathbb{E}[\\varepsilon_T\\mid A^*{=}j]=0$ and $\\operatorname{Cov}(\\varepsilon_T,\\,g(A)\\mid A^*{=}j)=0$ for every $j$.\n\n\\emph{Step 2: Reduce the numerator.}\nSince $f=\\lambda g$:\n\\begin{align*}\n  R(C) &= \\lambda\\,\\mathbb{E}[\\operatorname{Var}(g(A)\\mid A^*)] = \\lambda\\,V_W.\n\\end{align*}\n\n\\emph{Step 3: Constant additive term in denominator.}\n\\begin{align*}\n  D(C) &= \\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]\n       = V_W + \\sigma_\\varepsilon^2,\n\\end{align*}\nwhere $\\sigma_\\varepsilon^2\\equiv\\mathbb{E}[\\operatorname{Var}(\\varepsilon_T\\mid A^*)]$.\nThis is \\emph{constant} (independent of $C$):\n$\\mathbb{E}[\\operatorname{Var}(\\varepsilon_T\\mid A^*)]\n  = \\sum_k p_k\\,\\operatorname{Var}(T\\mid A{=}k)\n  = \\mathbb{E}[\\operatorname{Var}(T\\mid A)]$,\nwhere the equality uses column-stochasticity: $\\sum_j q_j\\,P(A{=}k\\mid A^*{=}j)=p_k$.\n\n\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\subsection{Collider Topology ($A$ = Collider)}\n\\label{app:collider}",
      "numLines": 120,
      "startLine": 255,
      "totalLines": 982
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "122e6a33-07c0-4dd8-b23a-c440ff647452",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01M9JMraBAJbk18GBvqv8uZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4620,
      "cache_read_input_tokens": 43070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4620
      },
      "output_tokens": 39,
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

_source line 12_

Now I understand the context. Let me look at the appendix structure around the mediation monotonicity proof to find the right insertion point.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "b15733f6-78c6-4e41-a859-7dcfe37cc9f2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01M9JMraBAJbk18GBvqv8uZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4620,
      "cache_read_input_tokens": 43070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4620
      },
      "output_tokens": 39,
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01PCvPDutgKU6d1VH6zCMrSk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 335,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "fef9b05b-331a-4378-bb3a-e28afd6e2b95",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01M9JMraBAJbk18GBvqv8uZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4620,
      "cache_read_input_tokens": 43070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4620
      },
      "output_tokens": 39,
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

_source line 14 · 2026-05-22T15:22:36.765Z_

<details><summary>↩ Tool result · `toolu_01PCvPDutgKU6d1VH6zCMrSk`</summary>

```text
335	$\tau_{\mathrm{total}}=0.5+0.351=0.851>0$.
336	Since $\tau_{\mathrm{dir}}{>}0$ and $\tau_{\mathrm{total}}{>}0$, sign preservation holds for all $C$.
337	
338	\paragraph{Mediation monotonicity (proportional effects).}
339	\label{par:med_monotone}
340	
341	Under the interpolation $C(\delta)=(1{-}\delta)I+\delta C_0$, we prove $|B(C(\delta))|$ is non-decreasing in $\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\lambda\,g(A)$ for some scalar $\lambda$, where $g(k)=\mathbb{E}[T\mid A{=}k]$.
342	
343	\emph{Step 1: Decompose $T$ via the mediator.}
344	Define $g(A)=\mathbb{E}[T\mid A]$ and $\varepsilon_T = T - g(A)$.
345	By construction, $\mathbb{E}[\varepsilon_T\mid A]=0$.
346	By non-differential misclassification ($T\perp A^*\mid A$):
347	$\mathbb{E}[\varepsilon_T\mid A{=}k, A^*{=}j] = 0$,
348	so $\mathbb{E}[\varepsilon_T\mid A^*{=}j]=0$ and $\operatorname{Cov}(\varepsilon_T,\,g(A)\mid A^*{=}j)=0$ for every $j$.
349	
350	\emph{Step 2: Reduce the numerator.}
351	Since $f=\lambda g$:
352	\begin{align*}
353	  R(C) &= \lambda\,\mathbb{E}[\operatorname{Var}(g(A)\mid A^*)] = \lambda\,V_W.
354	\end{align*}
355	
356	\emph{Step 3: Constant additive term in denominator.}
357	\begin{align*}
358	  D(C) &= \mathbb{E}[\operatorname{Var}(T\mid A^*)]
359	       = V_W + \sigma_\varepsilon^2,
360	\end{align*}
361	where $\sigma_\varepsilon^2\equiv\mathbb{E}[\operatorname{Var}(\varepsilon_T\mid A^*)]$.
362	This is \emph{constant} (independent of $C$):
363	$\mathbb{E}[\operatorname{Var}(\varepsilon_T\mid A^*)]
364	  = \sum_k p_k\,\operatorname{Var}(T\mid A{=}k)
365	  = \mathbb{E}[\operatorname{Var}(T\mid A)]$,
366	where the equality uses column-stochasticity: $\sum_j q_j\,P(A{=}k\mid A^*{=}j)=p_k$.
367	
368	\emph{Step 4: Closed form and monotonicity.}
369	$B(C) = \lambda\,V_W/(V_W+\sigma_\varepsilon^2)$,
370	structurally identical to confounding (Proposition~\ref{prop:conf_prop}) with $\sigma_\varepsilon^2$ playing the role of $\sigma_T^2$.
371	Since $V_W(\delta)$ is non-decreasing by DPI (same argument as \S\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\lambda|x/(x+\sigma_\varepsilon^2)$ is increasing, $|B(C(\delta))|$ is non-decreasing.
372	
373	\subsection{Collider Topology ($A$ = Collider)}
374	\label{app:collider}
375	
376	\paragraph{Data-generating process.}
377	$T\to A\leftarrow Y$, $T\to Y$.
378	The treatment effect is unconfounded:
379	\begin{align*}
380	  T &\sim \mathcal{N}(0,1),\quad
381	  Y = \tau\,T + \varepsilon_Y,\quad \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp T,\\
382	  A\mid T,Y &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\delta}_T\,T + \boldsymbol{\delta}_Y\,Y)\bigr).
383	\end{align*}
384	The collider $A$ is a common \emph{effect} of $T$ and $Y$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "4d4ee4d1-809c-4200-91cf-3ccc72b83e64",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "$\\tau_{\\mathrm{total}}=0.5+0.351=0.851>0$.\nSince $\\tau_{\\mathrm{dir}}{>}0$ and $\\tau_{\\mathrm{total}}{>}0$, sign preservation holds for all $C$.\n\n\\paragraph{Mediation monotonicity (proportional effects).}\n\\label{par:med_monotone}\n\nUnder the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\\lambda\\,g(A)$ for some scalar $\\lambda$, where $g(k)=\\mathbb{E}[T\\mid A{=}k]$.\n\n\\emph{Step 1: Decompose $T$ via the mediator.}\nDefine $g(A)=\\mathbb{E}[T\\mid A]$ and $\\varepsilon_T = T - g(A)$.\nBy construction, $\\mathbb{E}[\\varepsilon_T\\mid A]=0$.\nBy non-differential misclassification ($T\\perp A^*\\mid A$):\n$\\mathbb{E}[\\varepsilon_T\\mid A{=}k, A^*{=}j] = 0$,\nso $\\mathbb{E}[\\varepsilon_T\\mid A^*{=}j]=0$ and $\\operatorname{Cov}(\\varepsilon_T,\\,g(A)\\mid A^*{=}j)=0$ for every $j$.\n\n\\emph{Step 2: Reduce the numerator.}\nSince $f=\\lambda g$:\n\\begin{align*}\n  R(C) &= \\lambda\\,\\mathbb{E}[\\operatorname{Var}(g(A)\\mid A^*)] = \\lambda\\,V_W.\n\\end{align*}\n\n\\emph{Step 3: Constant additive term in denominator.}\n\\begin{align*}\n  D(C) &= \\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]\n       = V_W + \\sigma_\\varepsilon^2,\n\\end{align*}\nwhere $\\sigma_\\varepsilon^2\\equiv\\mathbb{E}[\\operatorname{Var}(\\varepsilon_T\\mid A^*)]$.\nThis is \\emph{constant} (independent of $C$):\n$\\mathbb{E}[\\operatorname{Var}(\\varepsilon_T\\mid A^*)]\n  = \\sum_k p_k\\,\\operatorname{Var}(T\\mid A{=}k)\n  = \\mathbb{E}[\\operatorname{Var}(T\\mid A)]$,\nwhere the equality uses column-stochasticity: $\\sum_j q_j\\,P(A{=}k\\mid A^*{=}j)=p_k$.\n\n\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\subsection{Collider Topology ($A$ = Collider)}\n\\label{app:collider}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\leftarrow Y$, $T\\to Y$.\nThe treatment effect is unconfounded:\n\\begin{align*}\n  T &\\sim \\mathcal{N}(0,1),\\quad\n  Y = \\tau\\,T + \\varepsilon_Y,\\quad \\varepsilon_Y\\sim\\mathcal{N}(0,1),\\;\\varepsilon_Y\\perp T,\\\\\n  A\\mid T,Y &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\delta}_T\\,T + \\boldsymbol{\\delta}_Y\\,Y)\\bigr).\n\\end{align*}\nThe collider $A$ is a common \\emph{effect} of $T$ and $Y$.",
      "numLines": 50,
      "startLine": 335,
      "totalLines": 982
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01L6cK4BDFv7hGMxgTupNS2w`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ | head -30",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "b242f9e5-0435-45d7-92eb-45c32b3f5a74",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01M9JMraBAJbk18GBvqv8uZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4620,
      "cache_read_input_tokens": 43070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4620
      },
      "output_tokens": 39,
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

_source line 16 · 2026-05-22T15:22:37.586Z_

<details><summary>↩ Tool result · `toolu_01L6cK4BDFv7hGMxgTupNS2w`</summary>

```text
__pycache__
_project
analyze_epsilon_bound.py
analyze_epsilon_sign_structure.py
annotate.py
compute_all_tasks.py
compute_delta_max.py
compute_ppi_empirical.py
compute_theory_empirical_mape.py
compute_updated_empirical.py
delta_max_results.json
dream_reports
exp_a_stress_test.py
exp_a_stress_test_results.json
exp_a_stress_test_table.tex
exp_b_logistic_dgp.py
exp_b_logistic_results.json
exp_b_logistic_table.tex
exp_c_bootstrap_asv.py
exp_c_bootstrap_figure.pdf
exp_c_bootstrap_results.json
exp_d_conjecture_results.json
exp_d_conjecture_results_v2.json
exp_d_conjecture_verify.py
exp_d_conjecture_verify_v2.py
exp_e_asv_stability.py
exp_e_asv_stability_results.json
exp_e_asv_stability_table.tex
iv_dirichlet_subspace_appendix.tex
iv_dirichlet_subspace_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "8925af95-25ab-497d-8852-48362c6fedba",
  "tool_use_result": {
    "stdout": "__pycache__\n_project\nanalyze_epsilon_bound.py\nanalyze_epsilon_sign_structure.py\nannotate.py\ncompute_all_tasks.py\ncompute_delta_max.py\ncompute_ppi_empirical.py\ncompute_theory_empirical_mape.py\ncompute_updated_empirical.py\ndelta_max_results.json\ndream_reports\nexp_a_stress_test.py\nexp_a_stress_test_results.json\nexp_a_stress_test_table.tex\nexp_b_logistic_dgp.py\nexp_b_logistic_results.json\nexp_b_logistic_table.tex\nexp_c_bootstrap_asv.py\nexp_c_bootstrap_figure.pdf\nexp_c_bootstrap_results.json\nexp_d_conjecture_results.json\nexp_d_conjecture_results_v2.json\nexp_d_conjecture_verify.py\nexp_d_conjecture_verify_v2.py\nexp_e_asv_stability.py\nexp_e_asv_stability_results.json\nexp_e_asv_stability_table.tex\niv_dirichlet_subspace_appendix.tex\niv_dirichlet_subspace_results.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "e094a401-167a-444b-b834-6ce9182a31f6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015HCbbFxgT8AdBAugtsPbwp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7398,
      "cache_read_input_tokens": 47690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7398
      },
      "output_tokens": 48,
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

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01LdNoXvGRLLYDH8N1XvtYDN`</summary>

```json
{
  "pattern": "\\\\begin\\{proposition\\}|\\\\label\\{prop:",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "769ee8f8-38f3-421d-a90a-1c982f97c347",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015HCbbFxgT8AdBAugtsPbwp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7398,
      "cache_read_input_tokens": 47690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7398
      },
      "output_tokens": 48,
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

_source line 19 · 2026-05-22T15:22:45.357Z_

<details><summary>↩ Tool result · `toolu_01LdNoXvGRLLYDH8N1XvtYDN`</summary>

```text
docs/paper/method.tex:60:\begin{proposition}[Sign preservation---analytic results]
docs/paper/method.tex:61:\label{prop:signflip}
docs/paper/appendix_proofs.tex:140:\begin{proposition}[Confounding sign preservation --- proportional case]
docs/paper/appendix_proofs.tex:141:\label{prop:conf_prop}
docs/paper/appendix_proofs.tex:176:\begin{proposition}[Confounding sign preservation --- general case]
docs/paper/appendix_proofs.tex:177:\label{prop:conf_gen}
docs/paper/appendix_proofs.tex:414:\begin{proposition}[Collider sign preservation --- proportional case]
docs/paper/appendix_proofs.tex:415:\label{prop:col_prop}
docs/paper/appendix_proofs.tex:433:\begin{proposition}[Collider sign preservation --- general case]
docs/paper/appendix_proofs.tex:434:\label{prop:col_gen}
docs/paper/appendix_proofs.tex:540:\begin{proposition}[Exposure sign reversal]
docs/paper/appendix_proofs.tex:541:\label{prop:exp_counter}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "6fd00434-1c64-45b1-8f7b-8c3bc2efb432",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/method.tex:60:\\begin{proposition}[Sign preservation---analytic results]\ndocs/paper/method.tex:61:\\label{prop:signflip}\ndocs/paper/appendix_proofs.tex:140:\\begin{proposition}[Confounding sign preservation --- proportional case]\ndocs/paper/appendix_proofs.tex:141:\\label{prop:conf_prop}\ndocs/paper/appendix_proofs.tex:176:\\begin{proposition}[Confounding sign preservation --- general case]\ndocs/paper/appendix_proofs.tex:177:\\label{prop:conf_gen}\ndocs/paper/appendix_proofs.tex:414:\\begin{proposition}[Collider sign preservation --- proportional case]\ndocs/paper/appendix_proofs.tex:415:\\label{prop:col_prop}\ndocs/paper/appendix_proofs.tex:433:\\begin{proposition}[Collider sign preservation --- general case]\ndocs/paper/appendix_proofs.tex:434:\\label{prop:col_gen}\ndocs/paper/appendix_proofs.tex:540:\\begin{proposition}[Exposure sign reversal]\ndocs/paper/appendix_proofs.tex:541:\\label{prop:exp_counter}",
    "numLines": 12
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "17bac82d-c3b9-46e4-a633-6488bfbdc4c5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Y65G5HVntyTDBNJ1rUkPAx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 55088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
      },
      "output_tokens": 46,
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

_source line 21_

Now I'll write the verification script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "9abc7988-e7e5-4995-9e97-9824101ba932",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Y65G5HVntyTDBNJ1rUkPAx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 55088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
      },
      "output_tokens": 46,
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

_source line 22_

<details open><summary>🔧 Tool call — Write · `toolu_01Buhx2ACriEJeZL1kC1VojU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/verify_lambda_bound.py",
  "content": "\"\"\"\nNumerical verification that the mediation leakage coefficient\n\n    lambda(C) := Var(E[g(A) | A*]) / Var(g(A))\n\nlies in [0, 1] for any column-stochastic confusion matrix C and any\nnon-degenerate marginal distribution pi over A and any non-constant g.\n\nThe bound is the law-of-total-variance identity\n    Var(g) = Var(E[g|A*]) + E[Var(g|A*)]\napplied to the random variable g(A) under the joint law P(A,A*) = pi(A)*C(A*|A).\n\nThis script samples random (C, pi, g) triples for K in {3, 5, 7} and checks\nthat lambda(C) lies in [0, 1] in every case. It also verifies the two\nextremal cases analytically:\n  - C = I (perfect classification):    lambda = 1\n  - C = (1/K) * 1 1^T (rank-one row):  lambda = 0\n\"\"\"\n\nimport json\nimport os\nfrom pathlib import Path\n\nimport numpy as np\n\n\nRNG = np.random.default_rng(20260522)\nN_TRIALS_PER_K = 10_000\nKS = (3, 5, 7)\nATOL = 1e-12\n\n\ndef sample_column_stochastic(K, rng):\n    \"\"\"Each column ~ Dirichlet(1,...,1) on the K-simplex.\"\"\"\n    M = rng.dirichlet(np.ones(K), size=K).T  # rows: a*, cols: a\n    return M\n\n\ndef lambda_of(C, pi, g):\n    \"\"\"\n    lambda(C) := Var(E[g|A*]) / Var(g)\n    where the joint law is P(A=k) = pi[k], P(A*=j|A=k) = C[j,k].\n    \"\"\"\n    K = pi.size\n    # Joint P(A*=j, A=k) = C[j,k] * pi[k]\n    joint = C * pi[None, :]              # shape (K, K), rows j, cols k\n    p_astar = joint.sum(axis=1)          # P(A*=j)\n    # Conditional P(A=k | A*=j) = joint[j,k] / p_astar[j]\n    # Handle degenerate columns (p_astar=0) by skipping their contribution.\n    cond_mean = np.zeros(K)\n    safe = p_astar > 0\n    cond_mean[safe] = (joint[safe] @ g) / p_astar[safe]\n    mean_g = pi @ g\n    V_B = np.sum(p_astar * (cond_mean - mean_g) ** 2)\n    V = float(np.sum(pi * (g - mean_g) ** 2))\n    if V <= 0:\n        return None  # g is constant on the support; lambda undefined\n    return float(V_B / V)\n\n\ndef run():\n    results = {\"per_K\": {}}\n    overall_min = np.inf\n    overall_max = -np.inf\n    n_total = 0\n    n_oob = 0\n\n    for K in KS:\n        mins = []\n        maxs = []\n        lambdas = []\n        for _ in range(N_TRIALS_PER_K):\n            C = sample_column_stochastic(K, RNG)\n            pi = RNG.dirichlet(np.ones(K))\n            g = RNG.normal(size=K)\n            lam = lambda_of(C, pi, g)\n            if lam is None:\n                continue\n            lambdas.append(lam)\n            if lam < -ATOL or lam > 1.0 + ATOL:\n                n_oob += 1\n            mins.append(lam)\n            maxs.append(lam)\n        arr = np.array(lambdas)\n        results[\"per_K\"][K] = {\n            \"n_trials\": int(arr.size),\n            \"min\": float(arr.min()),\n            \"max\": float(arr.max()),\n            \"mean\": float(arr.mean()),\n            \"median\": float(np.median(arr)),\n            \"n_out_of_bounds\": int(((arr < -ATOL) | (arr > 1.0 + ATOL)).sum()),\n        }\n        overall_min = min(overall_min, float(arr.min()))\n        overall_max = max(overall_max, float(arr.max()))\n        n_total += int(arr.size)\n\n    # Analytic extremes\n    K_ref = 3\n    pi_ref = np.array([0.4, 0.35, 0.25])\n    g_ref = np.array([-0.7, 0.2, 1.1])\n    lam_I = lambda_of(np.eye(K_ref), pi_ref, g_ref)\n    lam_unif = lambda_of(np.full((K_ref, K_ref), 1.0 / K_ref), pi_ref, g_ref)\n\n    results[\"extremes_K3\"] = {\n        \"lambda_at_identity\":    lam_I,\n        \"lambda_at_uniform_C\":   lam_unif,\n    }\n    results[\"overall\"] = {\n        \"n_total\": n_total,\n        \"min\": overall_min,\n        \"max\": overall_max,\n        \"n_out_of_bounds\": n_oob,\n        \"atol\": ATOL,\n    }\n\n    out_path = Path(__file__).with_name(\"verify_lambda_bound_results.json\")\n    out_path.write_text(json.dumps(results, indent=2))\n\n    print(f\"K values tested: {KS}\")\n    for K, r in results[\"per_K\"].items():\n        print(f\"  K={K}: n={r['n_trials']}, lambda in [{r['min']:.6f}, {r['max']:.6f}], OOB={r['n_out_of_bounds']}\")\n    print(f\"Overall: n={n_total}, lambda in [{overall_min:.6f}, {overall_max:.6f}], OOB={n_oob}\")\n    print(f\"Identity check (K=3):  lambda(I)       = {lam_I:.12f}  (expect 1.0)\")\n    print(f\"Uniform-C check (K=3): lambda(1 1^T/K) = {lam_unif:.12e}  (expect 0.0)\")\n    print(f\"Results written to {out_path}\")\n\n    assert overall_min >= -ATOL and overall_max <= 1.0 + ATOL, (\n        f\"BOUND VIOLATION: lambda outside [0,1] in {n_oob} of {n_total} trials\"\n    )\n    assert abs(lam_I - 1.0) < 1e-12\n    assert abs(lam_unif) < 1e-12\n\n\nif __name__ == \"__main__\":\n    run()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "bfb711a6-1be1-4c83-b734-c1cfce50fa29",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Y65G5HVntyTDBNJ1rUkPAx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 55088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
      },
      "output_tokens": 46,
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

_source line 23 · 2026-05-22T15:23:22.081Z_

<details><summary>↩ Tool result · `toolu_01Buhx2ACriEJeZL1kC1VojU`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/verify_lambda_bound.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "f95bfd61-cf0f-4d38-923d-4a724eb33e4f",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/verify_lambda_bound.py",
    "content": "\"\"\"\nNumerical verification that the mediation leakage coefficient\n\n    lambda(C) := Var(E[g(A) | A*]) / Var(g(A))\n\nlies in [0, 1] for any column-stochastic confusion matrix C and any\nnon-degenerate marginal distribution pi over A and any non-constant g.\n\nThe bound is the law-of-total-variance identity\n    Var(g) = Var(E[g|A*]) + E[Var(g|A*)]\napplied to the random variable g(A) under the joint law P(A,A*) = pi(A)*C(A*|A).\n\nThis script samples random (C, pi, g) triples for K in {3, 5, 7} and checks\nthat lambda(C) lies in [0, 1] in every case. It also verifies the two\nextremal cases analytically:\n  - C = I (perfect classification):    lambda = 1\n  - C = (1/K) * 1 1^T (rank-one row):  lambda = 0\n\"\"\"\n\nimport json\nimport os\nfrom pathlib import Path\n\nimport numpy as np\n\n\nRNG = np.random.default_rng(20260522)\nN_TRIALS_PER_K = 10_000\nKS = (3, 5, 7)\nATOL = 1e-12\n\n\ndef sample_column_stochastic(K, rng):\n    \"\"\"Each column ~ Dirichlet(1,...,1) on the K-simplex.\"\"\"\n    M = rng.dirichlet(np.ones(K), size=K).T  # rows: a*, cols: a\n    return M\n\n\ndef lambda_of(C, pi, g):\n    \"\"\"\n    lambda(C) := Var(E[g|A*]) / Var(g)\n    where the joint law is P(A=k) = pi[k], P(A*=j|A=k) = C[j,k].\n    \"\"\"\n    K = pi.size\n    # Joint P(A*=j, A=k) = C[j,k] * pi[k]\n    joint = C * pi[None, :]              # shape (K, K), rows j, cols k\n    p_astar = joint.sum(axis=1)          # P(A*=j)\n    # Conditional P(A=k | A*=j) = joint[j,k] / p_astar[j]\n    # Handle degenerate columns (p_astar=0) by skipping their contribution.\n    cond_mean = np.zeros(K)\n    safe = p_astar > 0\n    cond_mean[safe] = (joint[safe] @ g) / p_astar[safe]\n    mean_g = pi @ g\n    V_B = np.sum(p_astar * (cond_mean - mean_g) ** 2)\n    V = float(np.sum(pi * (g - mean_g) ** 2))\n    if V <= 0:\n        return None  # g is constant on the support; lambda undefined\n    return float(V_B / V)\n\n\ndef run():\n    results = {\"per_K\": {}}\n    overall_min = np.inf\n    overall_max = -np.inf\n    n_total = 0\n    n_oob = 0\n\n    for K in KS:\n        mins = []\n        maxs = []\n        lambdas = []\n        for _ in range(N_TRIALS_PER_K):\n            C = sample_column_stochastic(K, RNG)\n            pi = RNG.dirichlet(np.ones(K))\n            g = RNG.normal(size=K)\n            lam = lambda_of(C, pi, g)\n            if lam is None:\n                continue\n            lambdas.append(lam)\n            if lam < -ATOL or lam > 1.0 + ATOL:\n                n_oob += 1\n            mins.append(lam)\n            maxs.append(lam)\n        arr = np.array(lambdas)\n        results[\"per_K\"][K] = {\n            \"n_trials\": int(arr.size),\n            \"min\": float(arr.min()),\n            \"max\": float(arr.max()),\n            \"mean\": float(arr.mean()),\n            \"median\": float(np.median(arr)),\n            \"n_out_of_bounds\": int(((arr < -ATOL) | (arr > 1.0 + ATOL)).sum()),\n        }\n        overall_min = min(overall_min, float(arr.min()))\n        overall_max = max(overall_max, float(arr.max()))\n        n_total += int(arr.size)\n\n    # Analytic extremes\n    K_ref = 3\n    pi_ref = np.array([0.4, 0.35, 0.25])\n    g_ref = np.array([-0.7, 0.2, 1.1])\n    lam_I = lambda_of(np.eye(K_ref), pi_ref, g_ref)\n    lam_unif = lambda_of(np.full((K_ref, K_ref), 1.0 / K_ref), pi_ref, g_ref)\n\n    results[\"extremes_K3\"] = {\n        \"lambda_at_identity\":    lam_I,\n        \"lambda_at_uniform_C\":   lam_unif,\n    }\n    results[\"overall\"] = {\n        \"n_total\": n_total,\n        \"min\": overall_min,\n        \"max\": overall_max,\n        \"n_out_of_bounds\": n_oob,\n        \"atol\": ATOL,\n    }\n\n    out_path = Path(__file__).with_name(\"verify_lambda_bound_results.json\")\n    out_path.write_text(json.dumps(results, indent=2))\n\n    print(f\"K values tested: {KS}\")\n    for K, r in results[\"per_K\"].items():\n        print(f\"  K={K}: n={r['n_trials']}, lambda in [{r['min']:.6f}, {r['max']:.6f}], OOB={r['n_out_of_bounds']}\")\n    print(f\"Overall: n={n_total}, lambda in [{overall_min:.6f}, {overall_max:.6f}], OOB={n_oob}\")\n    print(f\"Identity check (K=3):  lambda(I)       = {lam_I:.12f}  (expect 1.0)\")\n    print(f\"Uniform-C check (K=3): lambda(1 1^T/K) = {lam_unif:.12e}  (expect 0.0)\")\n    print(f\"Results written to {out_path}\")\n\n    assert overall_min >= -ATOL and overall_max <= 1.0 + ATOL, (\n        f\"BOUND VIOLATION: lambda outside [0,1] in {n_oob} of {n_total} trials\"\n    )\n    assert abs(lam_I - 1.0) < 1e-12\n    assert abs(lam_unif) < 1e-12\n\n\nif __name__ == \"__main__\":\n    run()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01CZmRnBCnpdNfr8F2RTG8zz`</summary>

```json
{
  "command": "python3 artifacts/verify_lambda_bound.py",
  "description": "Run lambda bound verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "94ec9a9f-a5e3-42b4-ba1e-a36c44d6d0f7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0166GrJmV2zE6j54mCWFaFk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2991,
      "cache_read_input_tokens": 55931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2991
      },
      "output_tokens": 68,
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

_source line 25 · 2026-05-22T15:23:27.376Z_

<details><summary>↩ Tool result · `toolu_01CZmRnBCnpdNfr8F2RTG8zz`</summary>

```text
K values tested: (3, 5, 7)
  K=3: n=10000, lambda in [0.000008, 0.893676], OOB=0
  K=5: n=10000, lambda in [0.000689, 0.629296], OOB=0
  K=7: n=10000, lambda in [0.002574, 0.533417], OOB=0
Overall: n=30000, lambda in [0.000008, 0.893676], OOB=0
Identity check (K=3):  lambda(I)       = 1.000000000000  (expect 1.0)
Uniform-C check (K=3): lambda(1 1^T/K) = 3.789149465127e-34  (expect 0.0)
Results written to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/verify_lambda_bound_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "0b953b22-62a5-495a-9b1b-cbe3f479d5a8",
  "tool_use_result": {
    "stdout": "K values tested: (3, 5, 7)\n  K=3: n=10000, lambda in [0.000008, 0.893676], OOB=0\n  K=5: n=10000, lambda in [0.000689, 0.629296], OOB=0\n  K=7: n=10000, lambda in [0.002574, 0.533417], OOB=0\nOverall: n=30000, lambda in [0.000008, 0.893676], OOB=0\nIdentity check (K=3):  lambda(I)       = 1.000000000000  (expect 1.0)\nUniform-C check (K=3): lambda(1 1^T/K) = 3.789149465127e-34  (expect 0.0)\nResults written to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/verify_lambda_bound_results.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "0def85d2-8c92-44b7-85e5-9ebd4c4796ec",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QoEzRNnJt2M5yLWgHJSYrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 58922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 560
      },
      "output_tokens": 40,
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

_source line 27_

Verification passed (n=30000, all λ ∈ [8e-6, 0.894], 0 OOB; λ(I)=1, λ(uniform)≈0). Now adding the Proposition to the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "6bab675f-c12d-4974-bbce-1381f9312a32",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QoEzRNnJt2M5yLWgHJSYrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 58922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 560
      },
      "output_tokens": 40,
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

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_01VaAuNpakijJ3rxr1cEVBeQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "old_string": "\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\subsection{Collider Topology ($A$ = Collider)}",
  "new_string": "\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\paragraph{Boundedness of the leakage coefficient.}\n\nThe mediation bias expression in~\\eqref{eq:mediation} writes the residual indirect effect as $(1-\\lambda(C))\\,\\tau_{\\mathrm{ind}}$, where\n\\begin{equation}\n\\label{eq:lambda_def}\n  \\lambda(C) \\;:=\\; \\frac{V_B(C)}{V},\\qquad V_B(C)=\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr),\\quad V=\\operatorname{Var}(g(A)),\n\\end{equation}\nwith $g(k)=\\mathbb{E}[T\\mid A{=}k]$ (the mediator's information about $T$). $\\lambda(C)$ measures the fraction of $g$-variance preserved by the noisy channel $A\\to A^*$: at $\\lambda(C)=1$, conditioning on $A^*$ fully blocks the mediated path; at $\\lambda(C)=0$, $A^*$ carries no information about $A$ and the entire indirect effect leaks into $\\hat\\tau_{\\mathrm{dir}}$.\n\n\\begin{proposition}[Mediation leakage boundedness]\n\\label{prop:lambda_bound}\nFor any column-stochastic confusion matrix $C\\in\\mathbb{R}^{K\\times K}$ and any non-degenerate marginal $\\pi$ over $A$ with $V=\\operatorname{Var}(g(A))>0$, the leakage coefficient defined in~\\eqref{eq:lambda_def} satisfies\n\\[\n  \\lambda(C)\\in[0,1].\n\\]\nMoreover, $\\lambda(I)=1$ (perfect classification) and $\\lambda(C)=0$ whenever the rows of $C$ are identical (rank-one, uninformative classification, e.g.\\ $C=\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$).\n\\end{proposition}\n\n\\begin{proof}\nBy the law of total variance applied to $g(A)$ under the joint law $P(A{=}k,A^*{=}j)=\\pi_k C_{jk}$,\n\\[\n  V \\;=\\; \\operatorname{Var}(g(A)) \\;=\\; \\underbrace{\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr)}_{V_B(C)} \\;+\\; \\underbrace{\\mathbb{E}\\!\\bigl[\\operatorname{Var}(g(A)\\mid A^*)\\bigr]}_{\\geq 0}.\n\\]\nBoth terms on the right are non-negative, so $0\\leq V_B(C)\\leq V$, and dividing by $V>0$ gives $\\lambda(C)\\in[0,1]$.\n\n\\emph{Endpoints.}\nAt $C=I$, $A^*=A$ a.s., so $\\mathbb{E}[g(A)\\mid A^*]=g(A^*)$ and $V_B(I)=V$, giving $\\lambda(I)=1$.\nIf the rows of $C$ are identical—i.e.\\ $C_{jk}=r_k$ for every $j$—then $P(A{=}k\\mid A^*{=}j)=\\pi_k$ for every $j$, hence $\\mathbb{E}[g(A)\\mid A^*]=\\mathbb{E}[g(A)]$ is constant, $V_B=0$, and $\\lambda=0$.\nThis covers the uniform case $C=\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ as the symmetric instance.\n\\end{proof}\n\n\\paragraph{Consistency with the proportional-effects formula.}\nThe closed form $B(C)=\\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$ derived under $f=\\lambda g$ uses $V_W(C)=\\mathbb{E}[\\operatorname{Var}(g\\mid A^*)]=V-V_B(C)$.\nEquation~\\eqref{eq:mediation} and $\\tau_{\\mathrm{ind}}=B(C{=}\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top)=\\lambda V/(V+\\sigma_\\varepsilon^2)$ then yield\n\\[\n  1-\\lambda(C) \\;=\\; \\frac{B(C)}{\\tau_{\\mathrm{ind}}} \\;=\\; \\frac{V_W(C)\\,(V+\\sigma_\\varepsilon^2)}{V\\,(V_W(C)+\\sigma_\\varepsilon^2)},\n\\]\nwhich is monotonically decreasing in $V_B(C)$ and equals $1$ at $V_B=0$, $0$ at $V_B=V$.\nThus the simple definition~\\eqref{eq:lambda_def} and the proportional-case bias share the same $\\{0,1\\}$ endpoints; they coincide in the limit $\\sigma_\\varepsilon^2\\gg V_W$ and remain within $[0,1]$ throughout (cf.\\ Proposition~\\ref{prop:lambda_bound}).\n\n\\paragraph{Numerical verification.}\nWe sample $N=10{,}000$ column-stochastic matrices per $K\\in\\{3,5,7\\}$ (each column drawn from $\\operatorname{Dirichlet}(\\mathbf{1})$), with independently sampled $\\pi\\sim\\operatorname{Dirichlet}(\\mathbf{1})$ and $g\\sim\\mathcal{N}(0,I_K)$, and compute $\\lambda(C)$ from~\\eqref{eq:lambda_def}.\nAll $30{,}000$ trials satisfy $\\lambda(C)\\in[0,1]$ (observed range $[8.0\\times 10^{-6},\\,0.894]$, zero out-of-bounds violations).\nThe analytic endpoints $\\lambda(I)=1$ and $\\lambda(\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top)=0$ are recovered to machine precision.\nThe script and results are in \\texttt{artifacts/verify\\_lambda\\_bound.py} and \\texttt{artifacts/verify\\_lambda\\_bound\\_results.json}.\n\n\\subsection{Collider Topology ($A$ = Collider)}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "c694ccfe-77f6-4a6c-8444-118ea81e1cc4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QoEzRNnJt2M5yLWgHJSYrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 58922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 560
      },
      "output_tokens": 40,
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

_source line 29 · 2026-05-22T15:24:04.234Z_

<details><summary>↩ Tool result · reported error · `toolu_01VaAuNpakijJ3rxr1cEVBeQ`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "ff2da1ea-3d5a-4601-b36b-77c09086a108",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01Bx8dNuLSGpq7Pt4tut8C5T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 365,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "267bdaa1-eee6-40d6-8712-15f94cc4709e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TMsvRJ8thFTYHCXS18cntN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3267,
      "cache_read_input_tokens": 59482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3267
      },
      "output_tokens": 41,
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

_source line 31 · 2026-05-22T15:24:09.676Z_

<details><summary>↩ Tool result · `toolu_01Bx8dNuLSGpq7Pt4tut8C5T`</summary>

```text
365	  = \mathbb{E}[\operatorname{Var}(T\mid A)]$,
366	where the equality uses column-stochasticity: $\sum_j q_j\,P(A{=}k\mid A^*{=}j)=p_k$.
367	
368	\emph{Step 4: Closed form and monotonicity.}
369	$B(C) = \lambda\,V_W/(V_W+\sigma_\varepsilon^2)$,
370	structurally identical to confounding (Proposition~\ref{prop:conf_prop}) with $\sigma_\varepsilon^2$ playing the role of $\sigma_T^2$.
371	Since $V_W(\delta)$ is non-decreasing by DPI (same argument as \S\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\lambda|x/(x+\sigma_\varepsilon^2)$ is increasing, $|B(C(\delta))|$ is non-decreasing.
372	
373	\subsection{Collider Topology ($A$ = Collider)}
374	\label{app:collider}
375	
376	\paragraph{Data-generating process.}
377	$T\to A\leftarrow Y$, $T\to Y$.
378	The treatment effect is unconfounded:
379	\begin{align*}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "f9410d57-524a-4f38-92f2-07cb44b232ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "  = \\mathbb{E}[\\operatorname{Var}(T\\mid A)]$,\nwhere the equality uses column-stochasticity: $\\sum_j q_j\\,P(A{=}k\\mid A^*{=}j)=p_k$.\n\n\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\subsection{Collider Topology ($A$ = Collider)}\n\\label{app:collider}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\leftarrow Y$, $T\\to Y$.\nThe treatment effect is unconfounded:\n\\begin{align*}",
      "numLines": 15,
      "startLine": 365,
      "totalLines": 982
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01RSAAPRGrEUA7MiAyvF9RE1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "old_string": "\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\subsection{Collider Topology ($A$ = Collider)}",
  "new_string": "\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\paragraph{Boundedness of the leakage coefficient.}\n\nThe mediation bias expression in~\\eqref{eq:mediation} writes the residual indirect effect as $(1-\\lambda(C))\\,\\tau_{\\mathrm{ind}}$, where\n\\begin{equation}\n\\label{eq:lambda_def}\n  \\lambda(C) \\;:=\\; \\frac{V_B(C)}{V},\\qquad V_B(C)=\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr),\\quad V=\\operatorname{Var}(g(A)),\n\\end{equation}\nwith $g(k)=\\mathbb{E}[T\\mid A{=}k]$ (the mediator's information about $T$). $\\lambda(C)$ measures the fraction of $g$-variance preserved by the noisy channel $A\\to A^*$: at $\\lambda(C)=1$, conditioning on $A^*$ fully blocks the mediated path; at $\\lambda(C)=0$, $A^*$ carries no information about $A$ and the entire indirect effect leaks into $\\hat\\tau_{\\mathrm{dir}}$.\n\n\\begin{proposition}[Mediation leakage boundedness]\n\\label{prop:lambda_bound}\nFor any column-stochastic confusion matrix $C\\in\\mathbb{R}^{K\\times K}$ and any non-degenerate marginal $\\pi$ over $A$ with $V=\\operatorname{Var}(g(A))>0$, the leakage coefficient defined in~\\eqref{eq:lambda_def} satisfies\n\\[\n  \\lambda(C)\\in[0,1].\n\\]\nMoreover, $\\lambda(I)=1$ (perfect classification) and $\\lambda(C)=0$ whenever the rows of $C$ are identical (rank-one, uninformative classification, e.g.\\ $C=\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$).\n\\end{proposition}\n\n\\begin{proof}\nBy the law of total variance applied to $g(A)$ under the joint law $P(A{=}k,A^*{=}j)=\\pi_k C_{jk}$,\n\\[\n  V \\;=\\; \\operatorname{Var}(g(A)) \\;=\\; \\underbrace{\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr)}_{V_B(C)} \\;+\\; \\underbrace{\\mathbb{E}\\!\\bigl[\\operatorname{Var}(g(A)\\mid A^*)\\bigr]}_{\\geq 0}.\n\\]\nBoth terms on the right are non-negative, so $0\\leq V_B(C)\\leq V$, and dividing by $V>0$ gives $\\lambda(C)\\in[0,1]$.\n\n\\emph{Endpoints.}\nAt $C=I$, $A^*=A$ a.s., so $\\mathbb{E}[g(A)\\mid A^*]=g(A^*)$ and $V_B(I)=V$, giving $\\lambda(I)=1$.\nIf the rows of $C$ are identical---i.e.\\ $C_{jk}=r_k$ for every $j$---then $P(A{=}k\\mid A^*{=}j)=\\pi_k$ for every $j$, hence $\\mathbb{E}[g(A)\\mid A^*]=\\mathbb{E}[g(A)]$ is constant, $V_B=0$, and $\\lambda=0$.\nThis covers the uniform case $C=\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ as the symmetric instance.\n\\end{proof}\n\n\\paragraph{Consistency with the proportional-effects formula.}\nThe closed form $B(C)=\\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$ derived under $f=\\lambda g$ uses $V_W(C)=\\mathbb{E}[\\operatorname{Var}(g\\mid A^*)]=V-V_B(C)$.\nEquation~\\eqref{eq:mediation} and $\\tau_{\\mathrm{ind}}=B(C{=}\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top)=\\lambda V/(V+\\sigma_\\varepsilon^2)$ then yield\n\\[\n  1-\\lambda(C) \\;=\\; \\frac{B(C)}{\\tau_{\\mathrm{ind}}} \\;=\\; \\frac{V_W(C)\\,(V+\\sigma_\\varepsilon^2)}{V\\,(V_W(C)+\\sigma_\\varepsilon^2)},\n\\]\nwhich is monotonically decreasing in $V_B(C)$ and equals $1$ at $V_B=0$, $0$ at $V_B=V$.\nThus the simple definition~\\eqref{eq:lambda_def} and the proportional-case bias share the same $\\{0,1\\}$ endpoints; they coincide in the limit $\\sigma_\\varepsilon^2\\gg V_W$ and remain within $[0,1]$ throughout (cf.\\ Proposition~\\ref{prop:lambda_bound}).\n\n\\paragraph{Numerical verification.}\nWe sample $N=10{,}000$ column-stochastic matrices per $K\\in\\{3,5,7\\}$ (each column drawn from $\\operatorname{Dirichlet}(\\mathbf{1})$), with independently sampled $\\pi\\sim\\operatorname{Dirichlet}(\\mathbf{1})$ and $g\\sim\\mathcal{N}(0,I_K)$, and compute $\\lambda(C)$ from~\\eqref{eq:lambda_def}.\nAll $30{,}000$ trials satisfy $\\lambda(C)\\in[0,1]$ (observed range $[8.0{\\times}10^{-6},\\,0.894]$, zero out-of-bounds violations).\nThe analytic endpoints $\\lambda(I)=1$ and $\\lambda(\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top)=0$ are recovered to machine precision.\nThe script and results are in \\texttt{artifacts/verify\\_lambda\\_bound.py} and \\texttt{artifacts/verify\\_lambda\\_bound\\_results.json}.\n\n\\subsection{Collider Topology ($A$ = Collider)}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "7c2f3a73-44b6-4435-9304-11ad12f1a83e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HMvRHvxMcMXWfqTKvFBsEy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 62749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 616
      },
      "output_tokens": 61,
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

_source line 33 · 2026-05-22T15:24:36.306Z_

<details><summary>↩ Tool result · `toolu_01RSAAPRGrEUA7MiAyvF9RE1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "baa0ec38-7694-44d2-8815-69c947e83fdc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "oldString": "\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\subsection{Collider Topology ($A$ = Collider)}",
    "newString": "\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\paragraph{Boundedness of the leakage coefficient.}\n\nThe mediation bias expression in~\\eqref{eq:mediation} writes the residual indirect effect as $(1-\\lambda(C))\\,\\tau_{\\mathrm{ind}}$, where\n\\begin{equation}\n\\label{eq:lambda_def}\n  \\lambda(C) \\;:=\\; \\frac{V_B(C)}{V},\\qquad V_B(C)=\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr),\\quad V=\\operatorname{Var}(g(A)),\n\\end{equation}\nwith $g(k)=\\mathbb{E}[T\\mid A{=}k]$ (the mediator's information about $T$). $\\lambda(C)$ measures the fraction of $g$-variance preserved by the noisy channel $A\\to A^*$: at $\\lambda(C)=1$, conditioning on $A^*$ fully blocks the mediated path; at $\\lambda(C)=0$, $A^*$ carries no information about $A$ and the entire indirect effect leaks into $\\hat\\tau_{\\mathrm{dir}}$.\n\n\\begin{proposition}[Mediation leakage boundedness]\n\\label{prop:lambda_bound}\nFor any column-stochastic confusion matrix $C\\in\\mathbb{R}^{K\\times K}$ and any non-degenerate marginal $\\pi$ over $A$ with $V=\\operatorname{Var}(g(A))>0$, the leakage coefficient defined in~\\eqref{eq:lambda_def} satisfies\n\\[\n  \\lambda(C)\\in[0,1].\n\\]\nMoreover, $\\lambda(I)=1$ (perfect classification) and $\\lambda(C)=0$ whenever the rows of $C$ are identical (rank-one, uninformative classification, e.g.\\ $C=\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$).\n\\end{proposition}\n\n\\begin{proof}\nBy the law of total variance applied to $g(A)$ under the joint law $P(A{=}k,A^*{=}j)=\\pi_k C_{jk}$,\n\\[\n  V \\;=\\; \\operatorname{Var}(g(A)) \\;=\\; \\underbrace{\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr)}_{V_B(C)} \\;+\\; \\underbrace{\\mathbb{E}\\!\\bigl[\\operatorname{Var}(g(A)\\mid A^*)\\bigr]}_{\\geq 0}.\n\\]\nBoth terms on the right are non-negative, so $0\\leq V_B(C)\\leq V$, and dividing by $V>0$ gives $\\lambda(C)\\in[0,1]$.\n\n\\emph{Endpoints.}\nAt $C=I$, $A^*=A$ a.s., so $\\mathbb{E}[g(A)\\mid A^*]=g(A^*)$ and $V_B(I)=V$, giving $\\lambda(I)=1$.\nIf the rows of $C$ are identical---i.e.\\ $C_{jk}=r_k$ for every $j$---then $P(A{=}k\\mid A^*{=}j)=\\pi_k$ for every $j$, hence $\\mathbb{E}[g(A)\\mid A^*]=\\mathbb{E}[g(A)]$ is constant, $V_B=0$, and $\\lambda=0$.\nThis covers the uniform case $C=\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ as the symmetric instance.\n\\end{proof}\n\n\\paragraph{Consistency with the proportional-effects formula.}\nThe closed form $B(C)=\\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$ derived under $f=\\lambda g$ uses $V_W(C)=\\mathbb{E}[\\operatorname{Var}(g\\mid A^*)]=V-V_B(C)$.\nEquation~\\eqref{eq:mediation} and $\\tau_{\\mathrm{ind}}=B(C{=}\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top)=\\lambda V/(V+\\sigma_\\varepsilon^2)$ then yield\n\\[\n  1-\\lambda(C) \\;=\\; \\frac{B(C)}{\\tau_{\\mathrm{ind}}} \\;=\\; \\frac{V_W(C)\\,(V+\\sigma_\\varepsilon^2)}{V\\,(V_W(C)+\\sigma_\\varepsilon^2)},\n\\]\nwhich is monotonically decreasing in $V_B(C)$ and equals $1$ at $V_B=0$, $0$ at $V_B=V$.\nThus the simple definition~\\eqref{eq:lambda_def} and the proportional-case bias share the same $\\{0,1\\}$ endpoints; they coincide in the limit $\\sigma_\\varepsilon^2\\gg V_W$ and remain within $[0,1]$ throughout (cf.\\ Proposition~\\ref{prop:lambda_bound}).\n\n\\paragraph{Numerical verification.}\nWe sample $N=10{,}000$ column-stochastic matrices per $K\\in\\{3,5,7\\}$ (each column drawn from $\\operatorname{Dirichlet}(\\mathbf{1})$), with independently sampled $\\pi\\sim\\operatorname{Dirichlet}(\\mathbf{1})$ and $g\\sim\\mathcal{N}(0,I_K)$, and compute $\\lambda(C)$ from~\\eqref{eq:lambda_def}.\nAll $30{,}000$ trials satisfy $\\lambda(C)\\in[0,1]$ (observed range $[8.0{\\times}10^{-6},\\,0.894]$, zero out-of-bounds violations).\nThe analytic endpoints $\\lambda(I)=1$ and $\\lambda(\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top)=0$ are recovered to machine precision.\nThe script and results are in \\texttt{artifacts/verify\\_lambda\\_bound.py} and \\texttt{artifacts/verify\\_lambda\\_bound\\_results.json}.\n\n\\subsection{Collider Topology ($A$ = Collider)}",
    "originalFile": "\\section{Proofs of Proposition~\\ref{prop:signflip} and Theorem~\\ref{thm:monotone}}\n\\label{app:proof}\n\nWe provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\\ref{thm:monotone}).\nThroughout, $A\\in\\{0,1,\\dots,K{-}1\\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\\mid A{=}k)$.\nWe use category~0 as the reference and let $D_j=\\mathbf{1}(A{=}j)$, $D_j^*=\\mathbf{1}(A^*{=}j)$ for $j=1,\\dots,K{-}1$.\n\n\\subsection{Notation and Key Identities}\n\\label{app:notation}\n\nUnder non-differential misclassification, the misclassified moments factor linearly through $C$.\nDefine the population vectors:\n\\begin{align}\n  q_j &= P(A^*{=}j) = \\textstyle\\sum_k C_{jk}\\,p_k, \\label{eq:q}\\\\\n  \\mathrm{ct}_j &= \\mathbb{E}[T\\cdot D_j^*] = \\textstyle\\sum_k C_{jk}\\,\\mathbb{E}[T\\cdot D_k], \\label{eq:ct}\\\\\n  \\mathrm{cy}_j &= \\mathbb{E}[Y\\cdot D_j^*] = \\textstyle\\sum_k C_{jk}\\,\\mathbb{E}[Y\\cdot D_k]. \\label{eq:cy}\n\\end{align}\nWrite $q = Cp$, $\\mathrm{ct} = C\\,\\mathbb{E}[T\\cdot D]$, and $\\mathrm{cy} = C\\,\\mathbb{E}[Y\\cdot D]$, where $D=(D_0,\\dots,D_{K-1})^\\top$.\n\n\\subsection{Frisch--Waugh--Lovell Decomposition}\n\\label{app:fwl}\n\nFor topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\\dots,D_{K-1}^*)$.\nBy the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat{\\tau}(C)\n  = \\frac{\\mathbb{E}[\\tilde{T}\\,\\tilde{Y}]}{\\mathbb{E}[\\tilde{T}^2]},\n  \\label{eq:fwl}\n\\end{equation}\nwhere $\\tilde{T}=T-\\mathbb{E}[T\\mid A^*]$ and $\\tilde{Y}=Y-\\mathbb{E}[Y\\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\\dots,D_{K-1}^*)$.\n\n\\begin{lemma}[Bias decomposition]\n\\label{lem:bias_decomp}\nSuppose $Y = \\tau T + f(A) + \\varepsilon_Y$ with $\\varepsilon_Y \\perp (T, A, A^*)$.\nThen\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + \\frac{R(C)}{D(C)},\n  \\label{eq:bias_decomp}\n\\end{equation}\nwhere\n\\begin{align}\n  R(C) &= \\mathbb{E}\\bigl[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)\\bigr], \\label{eq:R}\\\\\n  D(C) &= \\mathbb{E}\\bigl[\\operatorname{Var}(T\\mid A^*)\\bigr] > 0. \\label{eq:D}\n\\end{align}\n\\end{lemma}\n\n\\begin{proof}\nExpand $\\tilde{Y}$ using $Y=\\tau T + f(A) + \\varepsilon_Y$:\n\\[\n  \\tilde{Y} = \\tau\\,\\tilde{T} + \\bigl(f(A) - \\mathbb{E}[f(A)\\mid A^*]\\bigr) + \\varepsilon_Y.\n\\]\nSince $\\tilde{T}$ is measurable w.r.t.\\ $(T,A^*)$ and $\\varepsilon_Y\\perp(T,A,A^*)$:\n\\[\n  \\mathbb{E}[\\tilde{T}\\,\\tilde{Y}]\n  = \\tau\\,\\mathbb{E}[\\tilde{T}^2]\n  + \\mathbb{E}\\bigl[\\tilde{T}\\,\\bigl(f(A)-\\mathbb{E}[f(A)\\mid A^*]\\bigr)\\bigr].\n\\]\nThe numerator residual is $R(C) = \\mathbb{E}[\\tilde{T}(f(A)-\\mathbb{E}[f(A)\\mid A^*])]$, and the denominator is $D(C) = \\mathbb{E}[\\tilde{T}^2]$.\n\nBy the law of total covariance:\n\\[\n  R(C) = \\sum_{j=0}^{K-1} q_j\\,\\operatorname{Cov}(T,\\,f(A)\\mid A^*{=}j)\n  = \\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)].\n\\]\nFor $D(C)>0$: decompose $T = g(A) + \\varepsilon_T$ where $g(A)=\\mathbb{E}[T\\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).\nIn both cases, $\\tilde{T}=\\bigl(g(A)-\\mathbb{E}[g(A)\\mid A^*]\\bigr)+\\varepsilon_T'$, where $\\varepsilon_T'$ is the component of $T$ independent of $(A,A^*)$.\nHence $D(C)\\geq\\operatorname{Var}(\\varepsilon_T')>0$.\n\\end{proof}\n\n\\subsection{Confounding Topology ($A$ = Confounder)}\n\\label{app:confounding}\n\n\\paragraph{Data-generating process.}\n$A\\to T$, $A\\to Y$, $T\\to Y$.\nUsing dummy coding with category 0 as reference:\n\\begin{align*}\n  T &= \\sum_{j=1}^{K-1}\\alpha_j D_j + \\varepsilon_T,\\quad\n  \\varepsilon_T\\sim\\mathcal{N}(0,\\sigma_T^2),\\;\\varepsilon_T\\perp A,\\\\\n  Y &= \\tau\\, T + \\sum_{j=1}^{K-1}\\beta_j^{(A)} D_j + \\varepsilon_Y,\\quad\n  \\varepsilon_Y\\sim\\mathcal{N}(0,1),\\;\\varepsilon_Y\\perp(T,A).\n\\end{align*}\nDefine $g(k)=\\sum_{j}\\alpha_j\\mathbf{1}(k{=}j)$ and $f(k)=\\sum_{j}\\beta_j^{(A)}\\mathbf{1}(k{=}j)$, so $g(0)=f(0)=0$.\n\n\\paragraph{Closed-form plim.}\nUsing the FWL decomposition, the coefficient on $T$ is:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C)\n  = \\frac{\\mu_{TY} - \\sum_{j=0}^{K-1}\\frac{\\mathrm{ct}_j\\,\\mathrm{cy}_j}{q_j}}\n  {s_T - \\sum_{j=0}^{K-1}\\frac{\\mathrm{ct}_j^2}{q_j}},\n  \\label{eq:plim_conf}\n\\end{equation}\nwhere $s_T=\\mathbb{E}[T^2]$, $\\mu_{TY}=\\mathbb{E}[TY]$, and $\\mathrm{ct}_j$, $\\mathrm{cy}_j$, $q_j$ are defined in~\\eqref{eq:q}--\\eqref{eq:cy}.\n\n\\begin{proof}[Derivation]\nBy FWL, $\\operatorname{plim}\\hat\\tau = \\mathbb{E}[\\tilde{T}Y]/\\mathbb{E}[\\tilde{T}^2]$ where $\\tilde{T}=T-\\mathbb{E}[T\\mid A^*]$.\nSince $\\mathbb{E}[T\\mid A^*{=}j]=\\mathrm{ct}_j/q_j$:\n\\begin{align*}\n  \\mathbb{E}[\\tilde{T}^2]\n  &= \\mathbb{E}[T^2] - \\sum_j q_j\\bigl(\\mathrm{ct}_j/q_j\\bigr)^2\n  = s_T - \\sum_j \\mathrm{ct}_j^2/q_j,\\\\\n  \\mathbb{E}[\\tilde{T}\\,Y]\n  &= \\mathbb{E}[TY] - \\sum_j \\bigl(\\mathrm{ct}_j/q_j\\bigr)\\,\\mathbb{E}[Y\\cdot D_j^*]\n  = \\mu_{TY} - \\sum_j \\mathrm{ct}_j\\,\\mathrm{cy}_j/q_j.\n\\end{align*}\n\\end{proof}\n\n\\paragraph{Verification at $C=I$.}\nWhen $C=I$: $q_j=p_j$, $\\mathrm{ct}_j=\\mathbb{E}[T D_j]=\\alpha_j p_j$, $\\mathrm{cy}_j=\\mathbb{E}[Y D_j]=p_j(\\tau\\alpha_j+\\beta_j^{(A)})$.\nDirect substitution yields numerator $= \\tau\\sigma_T^2$ and denominator $= \\sigma_T^2$, giving $\\operatorname{plim}\\hat\\tau = \\tau$.\n\n\\paragraph{Bias structure.}\nBy Lemma~\\ref{lem:bias_decomp}:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + B(C),\\quad\n  B(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(g(A),\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:bias_conf}\n\\end{equation}\nBy the law of total covariance:\n\\begin{equation}\n  \\mathbb{E}[\\operatorname{Cov}(g,f\\mid A^*)]\n  = \\operatorname{Cov}(g(A),f(A))\n  - \\operatorname{Cov}\\bigl(\\mathbb{E}[g(A)\\mid A^*],\\;\\mathbb{E}[f(A)\\mid A^*]\\bigr).\n  \\label{eq:lotc}\n\\end{equation}\n\nAt $C=I$: $\\mathbb{E}[g\\mid A^*]=g(A)$, so the between-group covariance equals $\\operatorname{Cov}(g,f)$ and $B(I)=0$.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ (uniform, $A^*\\perp A$): $\\mathbb{E}[g\\mid A^*]$ is constant, so the between-group covariance is zero and\n\\begin{equation}\n  B_{\\mathrm{OV}} \\;\\equiv\\; B\\bigl(\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top\\bigr)\n  = \\frac{\\operatorname{Cov}(g(A),\\,f(A))}{\\operatorname{Var}(T)},\n  \\label{eq:bov}\n\\end{equation}\nwhich equals the classical omitted-variable bias (no control for $A$).\n\n\\paragraph{Sign preservation condition.}\nSince $D(C)>0$, sign$(\\operatorname{plim}\\hat\\tau) = $ sign$(\\tau\\cdot D(C) + R(C))$.\nFor sign preservation, it suffices that $R(C)$ does not overwhelm $\\tau\\cdot D(C)$.\n\n\\begin{proposition}[Confounding sign preservation --- proportional case]\n\\label{prop:conf_prop}\nIf $f(A) = \\lambda\\,g(A)$ for some constant $\\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then\n\\begin{equation}\n  B(C) = \\bigl(1-\\eta(C)\\bigr)\\,B_{\\mathrm{OV}},\n  \\label{eq:convex}\n\\end{equation}\nwhere\n\\[\n  \\eta(C) = \\frac{\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])\\;\\sigma_T^2}\n  {\\operatorname{Var}(g(A))\\bigl(\\operatorname{Var}(g(A))-\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])+\\sigma_T^2\\bigr)}\n  \\;\\in\\;[0,1].\n\\]\nConsequently, $B(C)$ lies between $0$ and $B_{\\mathrm{OV}}$, and $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ whenever $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau+B_{\\mathrm{OV}})$.\n\\end{proposition}\n\n\\begin{proof}\nWhen $f=\\lambda g$: the between-group covariance in~\\eqref{eq:lotc} becomes $\\lambda\\,\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$, and $\\operatorname{Cov}(g,f)=\\lambda\\,\\operatorname{Var}(g)$.\nSo $R(C)=\\lambda\\bigl(\\operatorname{Var}(g)-\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\bigr)=\\lambda\\,V_W$, where $V_W=\\operatorname{Var}(g)-V_B$ with $V_B=\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$.\nSimilarly, $D(C)=V_W+\\sigma_T^2$.\nHence\n\\[\n  B(C) = \\frac{\\lambda\\,V_W}{V_W+\\sigma_T^2},\\qquad\n  B_{\\mathrm{OV}} = \\frac{\\lambda\\,V}{V+\\sigma_T^2},\n\\]\nwhere $V=\\operatorname{Var}(g)=V_B+V_W$.\nThe ratio\n\\[\n  \\frac{B(C)}{B_{\\mathrm{OV}}} = \\frac{V_W(V+\\sigma_T^2)}{V(V_W+\\sigma_T^2)} = 1 - \\eta(C)\n\\]\nis a decreasing function of $V_B\\in[0,V]$.\nAt $V_B=0$ (no classification, $C$ uniform): $\\eta=0$, $B=B_{\\mathrm{OV}}$.\nAt $V_B=V$ (perfect classification, $C=I$): $\\eta=1$, $B=0$.\nSince $0\\leq V_B\\leq V$, we have $\\eta\\in[0,1]$ and $B(C)\\in[0,B_{\\mathrm{OV}}]$ (with the sign of $B_{\\mathrm{OV}}$).\n\\end{proof}\n\n\\begin{proposition}[Confounding sign preservation --- general case]\n\\label{prop:conf_gen}\nFor general $g$ and $f$ (not necessarily proportional), define the worst-case bias bound\n\\begin{equation}\n  \\bar{B} \\;=\\; \\frac{\\sqrt{\\operatorname{Var}(g(A))\\,\\operatorname{Var}(f(A))}}{\\sigma_T^2}.\n  \\label{eq:bbar}\n\\end{equation}\nIf $|\\tau| > \\bar{B}$, then $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau(C))=\\operatorname{sign}(\\tau)$ for \\emph{all} column-stochastic $C$.\n\\end{proposition}\n\n\\begin{proof}\nWe need $\\operatorname{sign}(\\tau\\cdot D(C)+R(C))=\\operatorname{sign}(\\tau)$, which holds if $|R(C)|<|\\tau|\\cdot D(C)$.\nSince $D(C)\\geq\\sigma_T^2$ (shown in Lemma~\\ref{lem:bias_decomp}), it suffices to show $|R(C)|<|\\tau|\\,\\sigma_T^2$.\n\n\\emph{Step 1: Bound $|R(C)|$.}\n$R(C)=\\mathbb{E}[\\operatorname{Cov}(g(A),f(A)\\mid A^*)]$.\nBy the Cauchy--Schwarz inequality applied to each within-group covariance:\n\\[\n  |\\operatorname{Cov}(g,f\\mid A^*{=}j)|\n  \\leq \\sqrt{\\operatorname{Var}(g\\mid A^*{=}j)\\,\\operatorname{Var}(f\\mid A^*{=}j)}.\n\\]\nTaking expectations and applying Cauchy--Schwarz again:\n\\begin{align*}\n  |R(C)|\n  &\\leq \\mathbb{E}\\bigl[\\sqrt{\\operatorname{Var}(g\\mid A^*)\\,\\operatorname{Var}(f\\mid A^*)}\\bigr]\\\\\n  &\\leq \\sqrt{\\mathbb{E}[\\operatorname{Var}(g\\mid A^*)]\\;\\mathbb{E}[\\operatorname{Var}(f\\mid A^*)]}\\\\\n  &\\leq \\sqrt{\\operatorname{Var}(g(A))\\;\\operatorname{Var}(f(A))},\n\\end{align*}\nwhere the last step uses $\\mathbb{E}[\\operatorname{Var}(X\\mid Y)]\\leq\\operatorname{Var}(X)$ (law of total variance).\n\n\\emph{Step 2: Conclude.}\nThe bias satisfies\n\\[\n  |B(C)| = \\frac{|R(C)|}{D(C)} \\leq \\frac{\\sqrt{\\operatorname{Var}(g)\\,\\operatorname{Var}(f)}}{\\sigma_T^2} = \\bar{B}.\n\\]\nWhen $|\\tau|>\\bar{B}$, the bias cannot cancel $\\tau$, so $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ for all $C$.\n\\end{proof}\n\n\\paragraph{Relationship to the omitted-variable condition.}\nA weaker (necessary) condition for sign preservation is $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau_{\\mathrm{OV}})$ where $\\tau_{\\mathrm{OV}}=\\tau+\\operatorname{Cov}(g,f)/\\operatorname{Var}(T)$.\nIf this fails, then $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ (uniform noise) already flips the sign.\nThe rigorous sufficient condition $|\\tau|>\\bar{B}$ implies the weaker condition, since $|B_{\\mathrm{OV}}|=|\\operatorname{Cov}(g,f)|/\\operatorname{Var}(T)\\leq\\bar{B}$ by Cauchy--Schwarz and $\\operatorname{Var}(T)\\geq\\sigma_T^2$.\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau{=}2.0$, $\\boldsymbol{\\alpha}{=}(1.5,{-}1.0)$, $\\boldsymbol{\\beta}^{(A)}{=}(1.0,{-}0.5)$, $\\sigma_T{=}1.0$, $\\mathbf{p}{=}(0.40,0.35,0.25)$:\n\\begin{align*}\n  \\operatorname{Var}(g) &= \\sum_k p_k\\alpha_k^2 - \\bigl(\\textstyle\\sum_k p_k\\alpha_k\\bigr)^2 = 0.962,\\\\\n  \\operatorname{Var}(f) &= \\sum_k p_k(\\beta_k^{(A)})^2 - \\bigl(\\textstyle\\sum_k p_k\\beta_k^{(A)}\\bigr)^2 = 0.362,\\\\\n  \\bar{B} &= \\sqrt{0.962\\times 0.362}\\;/\\;1.0^2 = 0.590.\n\\end{align*}\nSince $|\\tau|{=}2.0 > \\bar{B}{=}0.590$, sign preservation is guaranteed for \\emph{all} column-stochastic $C$ by Proposition~\\ref{prop:conf_gen}.\nAdditionally, $B_{\\mathrm{OV}}=\\operatorname{Cov}(g,f)/\\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\\tau_{\\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.\n\n\\paragraph{Extension to $K > 3$.}\nFor $K{>}3$, treatment effect coefficients are drawn from a fixed pool with alternating signs and decreasing magnitudes: $\\boldsymbol{\\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3, \\ldots)$, truncated to $K$ entries. The category distribution uses $p_k \\propto 1/(k{+}1)$, normalized to sum to 1. Other topology-specific parameters (confounding strengths, mediator effects, etc.) follow analogous alternating-sign pools. For $K{=}10$, $\\boldsymbol{\\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3)$.\n\n\\subsection{Proof of Theorem~\\ref{thm:monotone} (Confounding Monotonicity)}\n\\label{app:monotonicity_proof}\n\nUnder the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ for proportional effects ($f=\\lambda g$) and provide numerical verification for the general case.\n\n\\paragraph{Proportional case ($f=\\lambda g$).}\nFrom Proposition~\\ref{prop:conf_prop}, $B(C)=\\lambda V_W/(V_W+\\sigma_T^2)$ where $V_W=\\operatorname{Var}(g)-V_B$ and $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$.\n\n\\emph{Step 1: $V_B(\\delta)$ is non-increasing.}\nThe conditional expectation $\\mathbb{E}[g(A)\\mid A^*_\\delta]$ is a linear function of the posterior $P(A\\mid A^*_\\delta)$, which in turn depends on $C(\\delta)$.\nAs $\\delta$ increases, $C(\\delta)$ becomes a noisier channel: the mutual information $I(A;A^*_\\delta)$ decreases.\nWhile the exact degradation factorization $C(\\delta_2)=M\\cdot C(\\delta_1)$ for a stochastic $M$ is non-trivial for the linear interpolation family, the monotonic decrease of $V_B(\\delta)$ can be verified directly: for $K{=}2$ symmetric $C_0$, $dV_B/d\\delta < 0$ follows by differentiation; for general $K$, we verify $V_B(\\delta_2)\\leq V_B(\\delta_1)$ numerically across all test configurations with zero violations.\n\n\\emph{Step 2: $|B(\\delta)|$ is non-decreasing.}\n$V_W(\\delta)=\\operatorname{Var}(g)-V_B(\\delta)$ is non-decreasing (Step~1).\nThe function $h(x)=|\\lambda|\\,x/(x+\\sigma_T^2)$ is strictly increasing for $x\\geq 0$ and $\\sigma_T^2>0$.\nHence $|B(\\delta)|=h(V_W(\\delta))$ is non-decreasing.\n\n\\paragraph{General case.}\n$|B(C(\\delta))|\\leq\\bar{B}(\\delta)$ where $\\bar{B}(\\delta)=\\sqrt{\\mathbb{E}[\\operatorname{Var}(g\\mid A^*_\\delta)]\\,\\mathbb{E}[\\operatorname{Var}(f\\mid A^*_\\delta)]}\\,/\\,D(\\delta)$ (Proposition~\\ref{prop:conf_gen}).\nBy the same data processing argument, each $\\mathbb{E}[\\operatorname{Var}(\\cdot\\mid A^*_\\delta)]$ is non-decreasing in $\\delta$, and $D(\\delta)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*_\\delta)]$ is non-decreasing.\nThe numerator grows at least as fast as the denominator (since $D(\\delta)\\leq\\operatorname{Var}(T)$), maintaining monotonicity of the bound.\nExtended verification (10{,}000 random $C_0$ matrices, $K \\in \\{3,5,7\\}$) reveals worst-case step deviations of 0.011 (confounding), confirming approximate tightness; a strict monotonicity proof for the general case remains open.\n\n\\subsection{Mediation Topology ($A$ = Mediator)}\n\\label{app:mediation}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\to Y$, $T\\to Y$.\n\\begin{align*}\n  T &\\sim \\operatorname{Bernoulli}(0.5),\\\\\n  A\\mid T &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\gamma}+\\boldsymbol{\\delta}\\,T)\\bigr),\\\\\n  Y &= \\tau_{\\mathrm{dir}}\\,T + f(A) + \\varepsilon_Y.\n\\end{align*}\n\n\\paragraph{Bias decomposition.}\nBy Lemma~\\ref{lem:bias_decomp}, the direct-effect estimator satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C) = \\tau_{\\mathrm{dir}} + \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:med_bias}\n\\end{equation}\n\nThe key structural difference from confounding: $T$ \\emph{causes} $A$, so the residual covariance $\\operatorname{Cov}(T,f(A)\\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.\n\n\\paragraph{Endpoint analysis.}\n\nAt $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\\to A\\to Y$, so $\\operatorname{Cov}(T,f(A)\\mid A)=0$ and $\\operatorname{plim}\\hat\\tau=\\tau_{\\mathrm{dir}}$.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ ($A^*\\perp A$): no information about $A$ is used, and\n\\begin{align*}\n  \\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)] &= \\operatorname{Cov}(T,f(A)),\\\\\n  D(C) &= \\operatorname{Var}(T) = 0.25.\n\\end{align*}\nThe indirect effect is $\\tau_{\\mathrm{ind}}=\\mathbb{E}[f(A)\\mid T{=}1]-\\mathbb{E}[f(A)\\mid T{=}0]$, and\n\\[\n  \\operatorname{Cov}(T,f(A)) = 0.25\\,\\tau_{\\mathrm{ind}}.\n\\]\nHence at $C$ uniform: $\\operatorname{plim}\\hat\\tau = \\tau_{\\mathrm{dir}}+\\tau_{\\mathrm{ind}} = \\tau_{\\mathrm{total}}$.\n\n\\paragraph{Numerical Verification (Mediation sign preservation).}\n\\label{find:med_sign}\n$\\operatorname{sign}(\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{dir}})$ whenever $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$, where $\\tau_{\\mathrm{total}}=\\tau_{\\mathrm{dir}}+\\tau_{\\mathrm{ind}}$.\nThis result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.\n\n\\begin{proof}\nLet $R(C)=\\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)]$ and $D(C)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]>0$.\n\n\\emph{Endpoints.}\nAt $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$: $R=\\operatorname{Cov}(T,f(A))=0.25\\,\\tau_{\\mathrm{ind}}$ and $D=\\operatorname{Var}(T)=0.25$, giving $B=\\tau_{\\mathrm{ind}}$.\n\n\\emph{Within-group structure for binary $T$.}\nSince $T\\in\\{0,1\\}$, the within-$A^*$-group bias admits a revealing decomposition.\nLet $p_j=P(T{=}1\\mid A^*{=}j)$.\nThen $\\operatorname{Var}(T\\mid A^*{=}j)=p_j(1{-}p_j)$ and\n\\[\n  \\operatorname{Cov}(T,f(A)\\mid A^*{=}j)\n  = p_j(1{-}p_j)\\bigl[\\mathbb{E}[f(A)\\mid T{=}1,A^*{=}j]-\\mathbb{E}[f(A)\\mid T{=}0,A^*{=}j]\\bigr].\n\\]\nDefine $\\delta_j=\\mathbb{E}[f(A)\\mid T{=}1,A^*{=}j]-\\mathbb{E}[f(A)\\mid T{=}0,A^*{=}j]$ as the \\emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.\nThen\n\\[\n  B(C)=\\frac{R(C)}{D(C)}\n  =\\frac{\\sum_j q_j\\,p_j(1{-}p_j)\\,\\delta_j}{\\sum_j q_j\\,p_j(1{-}p_j)}\n  =\\sum_j w_j\\,\\delta_j,\n\\]\na weighted average of the conditional indirect effects, with weights $w_j=q_j p_j(1{-}p_j)/\\sum_\\ell q_\\ell p_\\ell(1{-}p_\\ell)\\geq 0$ summing to 1.\n\nAt $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\\delta_j=f(j)-f(j)=0$ and $B=0$.\nAt $C$ uniform: $\\delta_j=\\tau_{\\mathrm{ind}}$ for all $j$ and $B=\\tau_{\\mathrm{ind}}$.\n\n\\emph{Sign preservation.}\nWhen $\\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{ind}}$ have the same sign), the bias $B(C)\\geq 0$ cannot oppose $\\tau_{\\mathrm{dir}}$, so sign is preserved trivially.\n\nWhen $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{ind}}$ have opposite signs but $|\\tau_{\\mathrm{ind}}|<|\\tau_{\\mathrm{dir}}|$ (i.e., $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$), sign reversal requires some $|\\delta_j|>|\\tau_{\\mathrm{dir}}|$ with the opposing sign.\nSince each $\\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\\delta_j$, the bound $|B(C)|\\leq\\max_j|\\delta_j|$ holds.\nWe verify numerically that $\\max_j|\\delta_j|\\leq|\\tau_{\\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.\n\\end{proof}\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau_{\\mathrm{dir}}{=}0.5$, $\\boldsymbol{\\gamma}{=}(0,0,0)$, $\\boldsymbol{\\delta}{=}(0,0.8,{-}0.6)$, $\\boldsymbol{\\beta}{=}(0,1.0,{-}0.5)$:\n\n$\\tau_{\\mathrm{ind}}=\\mathbb{E}[f(A)\\mid T{=}1]-\\mathbb{E}[f(A)\\mid T{=}0]=0.351$ (computed from the softmax class probabilities).\n$\\tau_{\\mathrm{total}}=0.5+0.351=0.851>0$.\nSince $\\tau_{\\mathrm{dir}}{>}0$ and $\\tau_{\\mathrm{total}}{>}0$, sign preservation holds for all $C$.\n\n\\paragraph{Mediation monotonicity (proportional effects).}\n\\label{par:med_monotone}\n\nUnder the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\\lambda\\,g(A)$ for some scalar $\\lambda$, where $g(k)=\\mathbb{E}[T\\mid A{=}k]$.\n\n\\emph{Step 1: Decompose $T$ via the mediator.}\nDefine $g(A)=\\mathbb{E}[T\\mid A]$ and $\\varepsilon_T = T - g(A)$.\nBy construction, $\\mathbb{E}[\\varepsilon_T\\mid A]=0$.\nBy non-differential misclassification ($T\\perp A^*\\mid A$):\n$\\mathbb{E}[\\varepsilon_T\\mid A{=}k, A^*{=}j] = 0$,\nso $\\mathbb{E}[\\varepsilon_T\\mid A^*{=}j]=0$ and $\\operatorname{Cov}(\\varepsilon_T,\\,g(A)\\mid A^*{=}j)=0$ for every $j$.\n\n\\emph{Step 2: Reduce the numerator.}\nSince $f=\\lambda g$:\n\\begin{align*}\n  R(C) &= \\lambda\\,\\mathbb{E}[\\operatorname{Var}(g(A)\\mid A^*)] = \\lambda\\,V_W.\n\\end{align*}\n\n\\emph{Step 3: Constant additive term in denominator.}\n\\begin{align*}\n  D(C) &= \\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]\n       = V_W + \\sigma_\\varepsilon^2,\n\\end{align*}\nwhere $\\sigma_\\varepsilon^2\\equiv\\mathbb{E}[\\operatorname{Var}(\\varepsilon_T\\mid A^*)]$.\nThis is \\emph{constant} (independent of $C$):\n$\\mathbb{E}[\\operatorname{Var}(\\varepsilon_T\\mid A^*)]\n  = \\sum_k p_k\\,\\operatorname{Var}(T\\mid A{=}k)\n  = \\mathbb{E}[\\operatorname{Var}(T\\mid A)]$,\nwhere the equality uses column-stochasticity: $\\sum_j q_j\\,P(A{=}k\\mid A^*{=}j)=p_k$.\n\n\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\subsection{Collider Topology ($A$ = Collider)}\n\\label{app:collider}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\leftarrow Y$, $T\\to Y$.\nThe treatment effect is unconfounded:\n\\begin{align*}\n  T &\\sim \\mathcal{N}(0,1),\\quad\n  Y = \\tau\\,T + \\varepsilon_Y,\\quad \\varepsilon_Y\\sim\\mathcal{N}(0,1),\\;\\varepsilon_Y\\perp T,\\\\\n  A\\mid T,Y &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\delta}_T\\,T + \\boldsymbol{\\delta}_Y\\,Y)\\bigr).\n\\end{align*}\nThe collider $A$ is a common \\emph{effect} of $T$ and $Y$.\nThe no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\\operatorname{plim}\\hat\\tau_{\\mathrm{nc}}=\\tau$.\nThe researcher erroneously controls for $A^*$, inducing Berkson's bias.\n\n\\paragraph{Bias decomposition.}\nUnlike confounding, $\\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\\tau T+\\varepsilon_Y$), so Lemma~\\ref{lem:bias_decomp} does not apply directly.\nInstead, we derive the bias from the FWL identity~\\eqref{eq:fwl}.\nWriting $\\tilde{Y}=\\tau\\tilde{T}+(\\varepsilon_Y-\\mathbb{E}[\\varepsilon_Y\\mid A^*])$ and noting that $\\mathbb{E}[\\tilde{T}\\,\\varepsilon_Y]=\\mathbb{E}[\\operatorname{Cov}(T,\\varepsilon_Y\\mid A^*)]$ (since $T\\perp\\varepsilon_Y$ unconditionally):\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + B(C),\\quad\n  B(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,\\varepsilon_Y\\mid A^*)]}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n  \\label{eq:bias_col}\n\\end{equation}\nUnder non-differential misclassification ($A^*\\perp(T,\\varepsilon_Y)\\mid A$), define $g(k)=\\mathbb{E}[T\\mid A{=}k]$ and $h(k)=\\mathbb{E}[\\varepsilon_Y\\mid A{=}k]$.\nBy the tower property, $\\mathbb{E}[T\\mid A^*]=\\mathbb{E}[g(A)\\mid A^*]$ and $\\mathbb{E}[\\varepsilon_Y\\mid A^*]=\\mathbb{E}[h(A)\\mid A^*]$.\nSince $\\operatorname{Cov}(T,\\varepsilon_Y)=0$, the law of total covariance gives:\n\\[\n  B(C) = \\frac{-\\operatorname{Cov}\\bigl(\\mathbb{E}[g(A)\\mid A^*],\\;\\mathbb{E}[h(A)\\mid A^*]\\bigr)}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n\\]\n\n\\paragraph{Endpoint analysis.}\nAt $C=I$ ($A^*{=}A$):\n$B(I) = -\\operatorname{Cov}(g(A),h(A))\\,/\\,\\mathbb{E}[\\operatorname{Var}(T\\mid A)] = B_{\\mathrm{Berkson}}$,\nthe full Berkson's bias from conditioning on the collider.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ ($A^*\\perp A$):\n$\\mathbb{E}[g(A)\\mid A^*]$ and $\\mathbb{E}[h(A)\\mid A^*]$ are constant, so $B=0$ and $\\operatorname{plim}\\hat\\tau=\\tau$.\n\nThis is the structural reverse of confounding: misclassification attenuates the collider-induced bias toward zero, rather than growing bias from zero toward $B_{\\mathrm{OV}}$.\n\n\\begin{proposition}[Collider sign preservation --- proportional case]\n\\label{prop:col_prop}\nIf $h(A)=\\lambda\\,g(A)$ for some constant $\\lambda$, then $|B(C)|\\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.\nConsequently, $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ whenever $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau+B_{\\mathrm{Berkson}})$.\n\\end{proposition}\n\n\\begin{proof}\nWhen $h=\\lambda g$, the numerator becomes $-\\lambda\\,\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$ and the denominator is $\\operatorname{Var}(T)-\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$.\nLet $V^*=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])\\in[0,V_g]$ where $V_g=\\operatorname{Var}(g(A))$.\nThen\n\\[\n  |B(C)| = |\\lambda|\\,\\frac{V^*}{\\operatorname{Var}(T)-V^*}.\n\\]\nThe function $x\\mapsto x/(a-x)$ is increasing on $[0,a)$.\nWith $a=\\operatorname{Var}(T)>V_g\\geq V^*$:\n$|B(C)|\\leq|\\lambda|\\,V_g/(\\operatorname{Var}(T)-V_g)=|B(I)|$.\nAt $V^*{=}0$ (uniform $C$): $B{=}0$.  At $V^*{=}V_g$ ($C{=}I$): $B{=}B(I)$.\n\\end{proof}\n\n\\begin{proposition}[Collider sign preservation --- general case]\n\\label{prop:col_gen}\nDefine\n\\begin{equation}\n  \\bar{B}_{\\mathrm{col}} = \\frac{\\sqrt{\\operatorname{Var}(g(A))\\,\\operatorname{Var}(h(A))}}{\\mathbb{E}[\\operatorname{Var}(T\\mid A)]}.\n  \\label{eq:bbar_col}\n\\end{equation}\nIf $|\\tau|>\\bar{B}_{\\mathrm{col}}$, then $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau(C))=\\operatorname{sign}(\\tau)$ for all column-stochastic $C$.\n\\end{proposition}\n\n\\begin{proof}\n\\emph{Step~1: Bound the numerator.}\nBy Cauchy--Schwarz:\n$|\\operatorname{Cov}(\\mathbb{E}[g\\mid A^*],\\mathbb{E}[h\\mid A^*])|\\leq\\sqrt{\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\,\\operatorname{Var}(\\mathbb{E}[h\\mid A^*])}$.\nSince conditional expectation reduces variance: $\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\leq\\operatorname{Var}(g(A))$ and likewise for $h$.\n\n\\emph{Step~2: Bound the denominator.}\n$\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]=\\operatorname{Var}(T)-\\operatorname{Var}(\\mathbb{E}[T\\mid A^*])\\geq\\operatorname{Var}(T)-\\operatorname{Var}(g(A))=\\mathbb{E}[\\operatorname{Var}(T\\mid A)]$.\n\n\\emph{Step~3: Conclude.}\n$|B(C)|\\leq\\sqrt{\\operatorname{Var}(g)\\,\\operatorname{Var}(h)}\\,/\\,\\mathbb{E}[\\operatorname{Var}(T\\mid A)]=\\bar{B}_{\\mathrm{col}}$.\nWhen $|\\tau|>\\bar{B}_{\\mathrm{col}}$, the bias cannot overwhelm $\\tau$.\n\\end{proof}\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau{=}1.0$, $\\boldsymbol{\\delta}_T{=}(0,\\,0.5,\\,{-}0.3)$, $\\boldsymbol{\\delta}_Y{=}(0,\\,0.8,\\,0.6)$, from $5{\\times}10^6$-sample Monte Carlo:\n\\begin{align*}\n  \\operatorname{Var}(g(A)) &= 0.187,\\quad\n  \\operatorname{Var}(h(A)) = 0.076,\\quad\n  \\mathbb{E}[\\operatorname{Var}(T\\mid A)] = 0.813,\\\\\n  \\bar{B}_{\\mathrm{col}} &= \\sqrt{0.187\\times 0.076}\\;/\\;0.813 = 0.147.\n\\end{align*}\nSince $|\\tau|{=}1.0\\gg\\bar{B}_{\\mathrm{col}}{=}0.147$, Proposition~\\ref{prop:col_gen} guarantees sign preservation.\nAdditionally, $B_{\\mathrm{Berkson}}{=}{-}0.114$, giving $\\tau+B_{\\mathrm{Berkson}}{=}0.886{>}0$.\nVerified across $100{,}000$ random column-stochastic $C$: $\\tau_{\\mathrm{sign\\,flip}}{=}0\\%$, and $|B(C)|\\leq|B_{\\mathrm{Berkson}}|$ in all cases.\n\n\\subsection{Front-door Topology ($A$ = Mediator under Confounding)}\n\\label{app:frontdoor}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\to Y$, $U\\to T$, $U\\to Y$.\nAn unobserved confounder $U$ affects both treatment and outcome:\n\\begin{align*}\n  U &\\sim \\mathcal{N}(0,1),\\quad\n  T = \\alpha_U\\,U + \\eta,\\quad \\eta\\sim\\mathcal{N}(0,1),\\;\\eta\\perp U,\\\\\n  A\\mid T &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\gamma}+\\boldsymbol{\\delta}\\,T)\\bigr),\\\\\n  Y &= f(A) + \\lambda\\,U + \\varepsilon_Y,\\quad \\varepsilon_Y\\perp(T,A,U).\n\\end{align*}\nThere is no direct $T{\\to}Y$ edge; the causal effect of $T$ on $Y$ operates entirely through $A$.\nThe researcher controls for $A^*$ in $Y\\sim 1+T+D_1^*+\\cdots+D_{K-1}^*$.\n\n\\paragraph{Bias decomposition.}\nSince the direct effect is zero, the FWL coefficient on $T$ captures only bias:\n\\[\n  \\operatorname{plim}\\hat\\tau(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,Y\\mid A^*)]}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n\\]\nSubstituting $Y=f(A)+\\lambda U+\\varepsilon_Y$ and using $\\varepsilon_Y\\perp(T,A,A^*)$:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C)\n  = \\underbrace{\\frac{\\lambda\\,\\alpha_U}{\\operatorname{Var}(T)}}_{\\text{confounding (constant)}}\n  \\;+\\; \\underbrace{\\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)]}{D(C)}}_{\\displaystyle B_{\\mathrm{med}}(C)},\n  \\label{eq:fd_decomp}\n\\end{equation}\nwhere $D(C)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]$.\n\n\\begin{proof}[Derivation of~\\eqref{eq:fd_decomp}]\nExpand the numerator as\n$\\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)] + \\lambda\\,\\mathbb{E}[\\operatorname{Cov}(T,U\\mid A^*)]$.\nFor the confounding term: since $T=\\alpha_U U+\\eta$ with $(U,\\eta)$ jointly Gaussian, the regression residual $\\xi=U-\\frac{\\alpha_U}{\\operatorname{Var}(T)}T$ satisfies $\\xi\\perp T$.\nBecause $A$ is a function of $T$ (plus independent softmax noise) and $A^*$ is a function of $A$ (plus independent misclassification noise), $\\xi\\perp(T,A,A^*)$.\nTherefore\n\\[\n  \\operatorname{Cov}(T,U\\mid A^*{=}j)\n  = \\frac{\\alpha_U}{\\operatorname{Var}(T)}\\,\\operatorname{Var}(T\\mid A^*{=}j)\n  \\quad\\forall\\;j,\n\\]\nand $\\lambda\\,\\mathbb{E}[\\operatorname{Cov}(T,U\\mid A^*)]=\\frac{\\lambda\\alpha_U}{\\operatorname{Var}(T)}\\,D(C)$, yielding the constant first term after division by $D(C)$.\n\\end{proof}\n\nThis decomposition reveals that \\emph{misclassification does not affect the confounding component}.\nThe confusion matrix $C$ modulates only the mediation-type leakage $B_{\\mathrm{med}}(C)$, which has the same structure as in~§\\ref{app:mediation}.\n\n\\paragraph{Endpoint analysis.}\nAt $C=I$: $B_{\\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\\to A\\to Y$ path), and $\\operatorname{plim}\\hat\\tau(I)=\\lambda\\alpha_U/\\operatorname{Var}(T)$ (pure confounding residual).\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$: $B_{\\mathrm{med}}=\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$, and $\\operatorname{plim}\\hat\\tau_{\\mathrm{nc}}=[\\operatorname{Cov}(T,f(A))+\\lambda\\alpha_U]/\\operatorname{Var}(T)$, the naive regression coefficient with no controls.\n\n\\paragraph{Numerical Verification (Front-door sign preservation).}\n\\label{find:fd_sign}\nSince $B_{\\mathrm{med}}(C)$ has the same structure as the mediation bias (§\\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:\n\\[\n  \\operatorname{sign}\\!\\bigl(\\lambda\\alpha_U\\bigr)\n  = \\operatorname{sign}\\!\\bigl(\\lambda\\alpha_U + \\operatorname{Cov}(T,f(A))\\bigr).\n\\]\nThis result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$.\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\alpha_U{=}1.0$, $\\lambda{=}1.0$, $\\boldsymbol{\\beta}{=}(0,1.0,{-}0.5)$, $\\boldsymbol{\\gamma}{=}(0,0.5,{-}0.3)$, $\\boldsymbol{\\delta}{=}(0,1.0,{-}0.8)$:\n\\begin{align*}\n  \\lambda\\alpha_U/\\operatorname{Var}(T) &= 1.0\\times 1.0\\,/\\,2.0 = 0.500,\\\\\n  \\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T) &= 0.594\\,/\\,2.0 = 0.297.\n\\end{align*}\nBoth components are positive, so $\\operatorname{plim}\\hat\\tau(C)\\in[0.500,\\,0.797]>0$ for all $C$.\n\n\\subsection{Exposure Topology: Sign Reversal Counterexample}\n\\label{app:exposure}\n\n\\begin{proposition}[Exposure sign reversal]\n\\label{prop:exp_counter}\nFor $K{=}3$ with $A$ as the treatment variable, there exist a marginal distribution $\\mathbf{p}$, treatment effects $\\boldsymbol{\\beta}$, and a column-stochastic $C$ with $C_{kk}>0.5$ for all $k$, such that $\\operatorname{sign}(\\operatorname{plim}\\hat\\beta_1)\\neq\\operatorname{sign}(\\beta_1)$.\n\\end{proposition}\n\n\\begin{proof}[Construction]\nConsider the exposure DGP $Y = \\beta_1 D_1 + \\beta_2 D_2 + \\varepsilon_Y$ with:\n\\begin{itemize}\n  \\item Uniform prior: $\\mathbf{p}=(1/3,\\,1/3,\\,1/3)$.\n  \\item True effects: $\\beta_1=1$,\\; $\\beta_2=-10$.\n\\end{itemize}\nChoose the confusion matrix\n\\[\n  C = \\begin{pmatrix}\n    0.60 & 0.10 & 0.10\\\\\n    0.10 & 0.60 & 0.39\\\\\n    0.30 & 0.30 & 0.51\n  \\end{pmatrix},\\qquad\n  C_{kk}\\in\\{0.60,\\,0.60,\\,0.51\\},\\;\\text{all}>0.5.\n\\]\nColumn sums are $1$ (verifiable by inspection).\n\nThe OLS estimator regresses $Y$ on $(1,D_1^*,D_2^*)$.\nThe plim of $\\hat\\beta_j$ equals $\\mathbb{E}[Y\\mid A^*{=}j]-\\mathbb{E}[Y\\mid A^*{=}0]$, where\n\\[\n  \\mathbb{E}[Y\\mid A^*{=}j] = \\sum_{k=0}^{2} P(A{=}k\\mid A^*{=}j)\\,\\beta_k\n  = \\sum_{k=1}^{2}\\frac{C_{jk}\\,p_k}{q_j}\\,\\beta_k.\n\\]\n\n\\emph{Marginal distribution of $A^*$:}\n\\begin{align*}\n  q_0 &= \\tfrac{1}{3}(0.60+0.10+0.10)=0.267,\\\\\n  q_1 &= \\tfrac{1}{3}(0.10+0.60+0.39)=0.363,\\\\\n  q_2 &= \\tfrac{1}{3}(0.30+0.30+0.51)=0.370.\n\\end{align*}\n\n\\emph{Conditional means:}\n\\begin{align*}\n  \\mathbb{E}[Y\\mid A^*{=}0]\n  &= \\frac{0.10\\times\\tfrac{1}{3}\\times 1 + 0.10\\times\\tfrac{1}{3}\\times({-}10)}{0.267}\n  = \\frac{0.0333-0.3333}{0.267} = -1.125,\\\\[4pt]\n  \\mathbb{E}[Y\\mid A^*{=}1]\n  &= \\frac{0.60\\times\\tfrac{1}{3}\\times 1 + 0.39\\times\\tfrac{1}{3}\\times({-}10)}{0.363}\n  = \\frac{0.200-1.300}{0.363} = -3.028,\\\\[4pt]\n  \\mathbb{E}[Y\\mid A^*{=}2]\n  &= \\frac{0.30\\times\\tfrac{1}{3}\\times 1 + 0.51\\times\\tfrac{1}{3}\\times({-}10)}{0.370}\n  = \\frac{0.100-1.700}{0.370} = -4.324.\n\\end{align*}\n\n\\emph{Estimated coefficient:}\n\\[\n  \\operatorname{plim}\\hat\\beta_1 = \\mathbb{E}[Y\\mid A^*{=}1]-\\mathbb{E}[Y\\mid A^*{=}0]\n  = -3.028-(-1.125) = \\mathbf{-1.903}.\n\\]\nThe true $\\beta_1=+1>0$ but $\\operatorname{plim}\\hat\\beta_1=-1.903<0$: \\textbf{sign reversal}.\n\n\\emph{Mechanism.}\nThe large off-diagonal entry $C_{12}=0.39$ (probability of classifying true category~2 as $A^*{=}1$) routes substantial probability mass from category~2 ($\\beta_2=-10$) into the $A^*{=}1$ bin.\nDespite $C_{11}=0.60>0.5$, the contamination from the strongly negative $\\beta_2$ overwhelms the positive $\\beta_1$, reversing the sign of the estimated effect for category~1.\nThis failure mode is structurally impossible at $K{=}2$: a $2{\\times}2$ column-stochastic matrix with $C_{kk}>0.5$ has the form $C=\\bigl(\\begin{smallmatrix}a&1{-}b\\\\1{-}a&b\\end{smallmatrix}\\bigr)$ with $a,b>0.5$, and the single coefficient $\\hat\\beta_1$ is a positive-weighted average of $\\beta_1$, preserving sign.\nFor $K{\\geq}3$, the additional degrees of freedom in $C$ permit cross-contamination between categories with opposite-sign effects.\n\\end{proof}\n\n\\subsection{Summary of Conditions}\n\\label{app:conditions}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Topology} & \\textbf{Sufficient condition} & \\textbf{Status} & \\textbf{Paper DGP} \\\\\n\\midrule\nConfounding & $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau{+}B_{\\mathrm{OV}})$ & Proved & $\\checkmark$ ($2.0$ vs $2.3$)\\\\\nCollider & $|\\tau|>\\bar{B}_{\\mathrm{col}}$ (Prop.~\\ref{prop:col_gen}) & Proved & $\\checkmark$ ($1.0$ vs $0.15$)\\\\\n\\midrule\nMediation & $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$ & Empirical & $\\checkmark$ ($0.5$ vs $0.85$)\\\\\nM-bias & Bias is attenuating (toward $\\tau$) & Empirical & $\\checkmark$ \\\\\nFront-door & $\\operatorname{sign}(\\lambda\\alpha_U)=\\operatorname{sign}(\\lambda\\alpha_U{+}\\operatorname{Cov}(T,f))$ & Empirical & $\\checkmark$ ($0.50$ vs $0.80$)\\\\\n\\midrule\nExposure & Not guaranteed for $K\\geq 3$ & Counterex. & See §\\ref{app:exposure} \\\\\nIV & Not guaranteed (denominator instability) & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sufficient conditions for sign preservation under non-differential misclassification.\n``Proved'' = algebraic proof via Cauchy--Schwarz (confounding) or Berkson attenuation (collider).\n``Empirical'' = verified across 100{,}000 random column-stochastic matrices with zero violations; analytic proof for general $K$ remains open.\nAll conditions are on DGP parameters (not on $C$): once satisfied, sign preservation holds for all column-stochastic $C$ with $C_{kk}>0$.}\n\\label{tab:sign_conditions}\n\\end{table}\n\n\\paragraph{Structural argument for M-bias topology.}\n\\emph{M-bias:} The M-structure creates a backdoor path through two latent common causes.\nMisclassification of $A$ weakens the statistical association along this backdoor path, reducing the spurious correlation rather than amplifying it.\nThe bias therefore interpolates between the full M-bias (perfect classification, $\\delta{=}0$) and zero (no classification information, $\\delta{\\to}\\delta_{\\max}$), monotonically non-increasing in $\\delta$.\n\n\\paragraph{Remark.}\nThe sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.\nOnce the condition is satisfied, sign preservation holds for \\emph{all} column-stochastic $C$ with $C_{kk}>0$---no diagonal-dominance restriction is needed.\nConversely, if the condition fails (i.e., the omitted-variable or total-effect estimate has the opposite sign from $\\tau$), then there exist confusion matrices that produce sign reversal.\nFor the DGP parameters used throughout our experiments, the conditions are comfortably satisfied.\nThe sign-alignment condition is violated when the confounder has opposing effects on treatment and outcome (e.g., $\\gamma_A > 0$ on $T$ but $\\gamma_A < 0$ on $Y$), producing $\\operatorname{sign}(\\tau) \\neq \\operatorname{sign}(\\tau_{\\mathrm{OV}})$. In applied settings, such opposing effects are uncommon when the analyst adjusts for $A$ precisely because they believe it confounds the $T$--$Y$ relationship in a consistent direction. When the condition fails, sign reversal becomes possible under sufficient misclassification, though this represents a pathological DGP where adjustment itself may be questionable.\n\n\\section{Supplementary Tables, Figures, and Algorithm}\n\\label{app:supplementary}\n\n\\subsection{Binarization Collapse}\n\\label{app:binarization}\n\nCollapsing $K$-class annotations to binary before analysis discards multi-class error structure. We quantify ``binarization collapse'' as $\\Delta = |\\text{bias}_{K} - \\text{bias}_{K \\to 2}|$.\n\nFor $K{=}3$, binarization introduces additional bias varying 154$\\times$ across topologies: from $\\bar{\\Delta}{=}0.006$ (M-bias) to $\\bar{\\Delta}{=}0.926$ (IV). Exposure and IV also introduce sign flips during binarization (14\\% and 17.5\\%), a phenomenon absent in the other topologies (Figure~\\ref{fig:binarization}).\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{fig3_asv_ranking.pdf}\n\\caption{ASV sensitivity ranking across topologies. Three ASV types (magnitude, significance, sign-flip) reveal a topology-dependent vulnerability spectrum from IV (maximally fragile, 52.6\\% sign reversal; sign-flip ASV $= 1.1$--$6.7$) to M-bias (immune, ASV $= \\infty$).}\n\\label{fig:asv_ranking}\n\\end{figure*}\n\n\\begin{table}[h]\n\\centering\n\\caption{ASV type applicability and sensitivity across DAG topologies. Magnitude ASV at $\\tau{=}0.5$, 10\\% threshold. Power at $\\tau{=}0.05$ significance filter. ---: not applicable.}\n\\label{tab:asv_grid}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Topology} & \\textbf{Mag. ASV} & \\textbf{Signif.} & \\textbf{Sign-flip} & \\textbf{Rank} \\\\\n\\midrule\nIV & 0.101--0.607 & 0\\% & 1.1--6.7 & 1 (fragile) \\\\\nFront-door & 0.064--0.387 & 100\\% & --- & 2 \\\\\nConfounding & 0.081--0.487 & 100\\% & --- & 3 \\\\\nMediation & 0.076--0.454 & 0\\% & --- & 4 \\\\\nCollider & 0.338--2.028 & 0\\% & --- & 5 \\\\\nM-bias & $\\infty$ & 96--100\\% & --- & 6 (immune) \\\\\nExposure & --- & --- & 83.4\\%$^*$ & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\scriptsize $^*$Fraction of $C_0$ with $\\tau_{\\text{sign\\_flip}} < 1$. Exposure uses sign-flip ASV exclusively.}\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig7_dirichlet_overlay.pdf}\n\\caption{Empirical LLM confusion matrices overlaid on theoretical violation-rate curves (exposure, left; IV, right). Theoretical curves are derived from $K{=}3$ Dirichlet random matrices; empirical points are positioned at their minimum diagonal entry. Markers denote datasets (circles: HumAID $K{=}10$; squares: VAST $K{=}3$; triangles: CivilComments $K{=}2$).}\n\\label{fig:dirichlet_overlay}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_binarization.pdf}\n\\caption{Binarization collapse $\\Delta$ across topologies. Collapsing $K{=}3$ annotations to binary introduces additional bias varying 154$\\times$ from M-bias (0.006) to IV (0.926).}\n\\label{fig:binarization}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig6_asv_heatmap.pdf}\n\\caption{ASV magnitude ranges across topologies for HumAID ($K{=}10$). Left: magnitude ASV ($\\delta^*$) range across 8 LLM configurations; lower values indicate greater fragility. ``Safe'' topologies never exceed the 10\\% bias threshold. Right: percentage of configurations flagged as ASV-unsafe.}\n\\label{fig:asv_heatmap}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{RMSE reduction (\\%) by correction method and DAG topology (mean across 6 error structures, $N_{\\text{sim}}{=}1{,}000$). Positive = reduced RMSE; negative = increased RMSE. Naive/MLA show 0.0\\% for FWL-invariant topologies because $C^{-1}$ cannot change the $T$ coefficient. \\textbf{Bold}: best method per topology; \\underline{underline}: best gold-free method.}\n\\label{tab:correction}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Topology} & \\textbf{Naive} & \\textbf{MLA} & \\textbf{DSL} & \\textbf{SIMEX} & \\textbf{PPI++} \\\\\n\\midrule\nConfounding & 0.0 & 0.0 & \\underline{48.0} & 35.1 & \\textbf{83.2} \\\\\nMediation & 0.0 & 0.0 & \\underline{52.9} & 39.1 & \\textbf{54.1} \\\\\nCollider & 0.0 & 0.0 & $-$92.6 & \\underline{31.8} & \\textbf{50.5} \\\\\nM-bias & 0.0 & 0.0 & $-$267 & \\textbf{\\underline{0.1}} & $-$88.0 \\\\\n\\midrule\nFront-door & $-$52.7 & $-$111.5 & \\underline{$-$29.0} & $-$62.4 & \\textbf{74.1} \\\\\nExposure & $-$44.8 & $-$89.0 & $-$59.5 & \\underline{$-$9.8} & \\textbf{75.5} \\\\\nIV & $-$40.4 & $-$58.7 & $-$206.1 & \\underline{59.4} & \\textbf{79.4} \\\\\n\\midrule\nGrand mean & $-$19.7 & $-$37.0 & $-$79.0 & 13.3 & \\textbf{47.0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Error structures used in correction experiments.}\nThe six confusion matrix structures used for Table~\\ref{tab:correction} are:\n(1)~\\emph{Diagonal-dominant}: $C_{kk}{=}0.7$, off-diagonal uniform;\n(2)~\\emph{Moderate noise}: $C_{kk}{=}0.5$, off-diagonal uniform;\n(3)~\\emph{Near-permutation}: $C_{kk}{=}0.4$, largest off-diagonal 0.5;\n(4)~\\emph{Asymmetric}: $C_{kk}$ varies (0.8, 0.5, 0.3);\n(5)~\\emph{Block confusion}: two classes confused ($C_{12}{=}C_{21}{=}0.4$), third clean;\n(6)~\\emph{Heavy noise}: $C_{kk}{=}0.4$, off-diagonal uniform.\nAll are column-stochastic with $K{=}3$. Results are averaged across all six structures.\n\n\\begin{algorithm}[h]\n\\caption{Correction method selection for LLM-annotated causal inference. Assumes linear structural equations; FWL-based routing may not apply under nonlinear models (see Appendix~\\ref{sec:logistic_dgp}).}\n\\label{alg:correction}\n\\small\n\\begin{algorithmic}[1]\n\\REQUIRE DAG topology $\\mathcal{T}$, gold-label availability $G \\in \\{\\textsc{yes}, \\textsc{no}\\}$\n\\ENSURE Recommended method $M$, risk level $R$\n\\STATE\n\\STATE \\textbf{Step 1: Assess risk level}\n\\IF{$\\mathcal{T} \\in \\{\\text{M-bias}\\}$}\n    \\STATE $R \\gets \\textsc{Low}$ \\COMMENT{$|\\text{bias}| < 0.04$ for all $C$}\n\\ELSIF{$\\mathcal{T} \\in \\{\\text{Conf., Med., Coll., Front-door}\\}$}\n    \\STATE $R \\gets \\textsc{Medium}$ \\COMMENT{bounded bias, no sign reversal}\n\\ELSE\n    \\STATE $R \\gets \\textsc{High}$ \\COMMENT{Exposure, IV: sign reversal 83.4\\% / 52.6\\%}\n\\ENDIF\n\\STATE\n\\STATE \\textbf{Step 2: Select correction method}\n\\IF{$G = \\textsc{yes}$}\n    \\IF{$\\mathcal{T} = \\text{M-bias}$}\n        \\STATE $M \\gets \\textsc{None}$ \\COMMENT{PPI++ RMSE red.\\ $-$88.0\\%; no correction preferred}\n    \\ELSE\n        \\STATE $M \\gets \\text{PPI++}$ \\COMMENT{47.0\\% RMSE red., 96.8\\% coverage}\n    \\ENDIF\n\\ELSE\n    \\STATE \\COMMENT{no gold labels}\n    \\IF{$\\mathcal{T} \\in \\{\\text{Confounding, Mediation}\\}$}\n        \\STATE $M \\gets \\text{DSL}$ \\COMMENT{48.0\\% / 52.9\\% RMSE reduction}\n    \\ELSIF{$\\mathcal{T} = \\text{IV}$}\n        \\STATE $M \\gets \\text{MC-SIMEX}$ \\COMMENT{59.4\\% RMSE reduction}\n    \\ELSIF{$\\mathcal{T} \\in \\{\\text{Collider, M-bias}\\}$}\n        \\STATE $M \\gets \\text{MC-SIMEX}$ \\COMMENT{31.8\\% / 0.1\\% RMSE reduction}\n    \\ELSE\n        \\STATE $M \\gets \\emptyset$; flag: acquire gold labels \\COMMENT{no reliable gold-free method}\n    \\ENDIF\n\\ENDIF\n\\STATE\n\\STATE \\textbf{Step 3: FWL invariance warning}\n\\IF{$\\mathcal{T} \\in \\{\\text{Conf., Med., Coll., M-bias}\\}$}\n    \\STATE Skip Naive plug-in and MLA \\COMMENT{0\\% bias red.\\ on $T$ coeff.}\n\\ENDIF\n\\RETURN $(M, R)$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Proof of FWL Invariance}\n\\label{app:fwl_proof}\n\nFor the four topologies where $A$ enters as a covariate (confounding, mediation, collider, M-bias), the regression is $Y = \\tau T + \\boldsymbol{\\gamma}^\\top \\mathbf{D}^* + \\varepsilon$, where $\\mathbf{D}^*$ is the $N \\times (K{-}1)$ dummy matrix for $A^*$. Any matrix-based correction replaces $\\mathbf{D}^*$ with $\\tilde{\\mathbf{D}} = \\mathbf{D}^* M$ for some invertible $(K{-}1) \\times (K{-}1)$ matrix $M$ (e.g., $M = C^{-1}$ for plug-in, or $M = (C^\\top C)^{-1} C^\\top$ for MLE). By the Frisch--Waugh--Lovell theorem~\\cite{lovell1963}, $\\hat{\\tau}$ depends only on the residual of $T$ projected off $\\operatorname{col}(\\mathbf{D}^*)$. Since $\\operatorname{col}(\\mathbf{D}^* M) = \\operatorname{col}(\\mathbf{D}^*)$ for invertible $M$, the projection is unchanged and $\\hat{\\tau}(\\tilde{\\mathbf{D}}) = \\hat{\\tau}(\\mathbf{D}^*)$ exactly. SIMEX adds noise $\\mathbf{D}^*_{\\text{sim}} = \\mathbf{D}^* + \\lambda \\mathbf{E}$; when $\\mathbf{E}$ is generated from the same column space, the extrapolation to $\\lambda = -1$ converges to a column-space-equivalent transformation, yielding 0\\% bias reduction empirically.\n\n\\subsection{Applied Illustration: ClinicalBERT Case Study}\n\\label{app:case_study}\n\nTo demonstrate the framework's end-to-end utility, we apply it retrospectively to \\citet{lee_wood_doughty2024}, who use ClinicalBERT to classify patient smoking status ($K{=}4$: never, past, current, unknown) from clinical notes and control for this predicted confounder when estimating the causal effect of echocardiography on mortality in 4{,}735 MIMIC-III sepsis patients.\nOur taxonomy identifies this as a \\emph{confounding topology}: the annotated variable enters as a confounder between treatment and outcome.\nThree conclusions follow directly.\nFirst, the zero sign-flip guarantee for confounding (Table~\\ref{tab:taxonomy}) ensures that the estimated protective effect (OR~$= 0.89$) cannot reverse direction due to annotation error---a reassurance unavailable without topology-specific analysis.\nSecond, the FWL invariance result implies that any correction reducing to $C^{-1}$ applied to the dummy-coded confounder achieves exactly 0\\% bias reduction for the treatment coefficient; naive plug-in is provably futile here.\nThird, our correction guidance ranks PPI++ (83.2\\% RMSE reduction for confounding) above MC-SIMEX (35.1\\%) when gold labels are available---a concrete recommendation the original study lacked.\nThis example illustrates the intended workflow: DAG identification $\\to$ topology-specific guarantees $\\to$ correction method selection.\n\n\\subsection{IV Wald Estimator: Diagonal-Dominance Subspaces}\n\\label{sec:iv_dirichlet_subspace}\n\nSection~\\ref{sec:taxonomy_results} reports a 52.6\\% Wald sign-flip rate\nover the full Dirichlet$(1,1,1)$ prior. Because realistic LLM confusion\nmatrices are diagonal-dominant, we replicate the exposure-DAG stratification\nfor the IV topology, restricting the sample\nspace to $\\{C : \\min_k C_{kk} \\geq d\\}$ for $d \\in \\{0, 0.5, 0.7, 0.9\\}$\n(100{,}000 random matrices per threshold).\n\n\\begin{table}[h]\n\\centering\n\\caption{IV Wald estimator bias by minimum-diagonal subspace ($K{=}3$, $\\tau_{\\text{true}}{=}1.41$).\nRates over 100{,}000 Dirichlet-truncated random $C$ per threshold.}\n\\label{tab:iv_dirichlet_subspace}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Subspace} & \\textbf{Violation} & \\textbf{Sign Flip} & \\textbf{Amplif.} & \\textbf{Worst} \\\\\n\\midrule\nFull           & 100.0\\% & 51.7\\% & 48.3\\% & $10^{5}\\!\\times$ \\\\\n$d \\geq 0.5$   & 100.0\\% & 0.0\\%  & 100.0\\% & $28.6\\times$ \\\\\n$d \\geq 0.7$   & 100.0\\% & 0.0\\%  & 100.0\\% & $2.4\\times$ \\\\\n$d \\geq 0.9$   & 100.0\\% & 0.0\\%  & 100.0\\% & $1.2\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe contrast with exposure is instructive: at $d{\\geq}0.7$, exposure violation drops to 13.7\\% (sign reversal 2.1\\%, amplification 11.7\\%), while IV maintains 100\\% violation with pure amplification. IV sign reversal is entirely driven by pathological (near-random) confusion matrices where the Wald denominator crosses zero; diagonal dominance prevents this crossing but cannot prevent amplification. Even at $d{\\geq}0.9$, the Wald estimator inflates $|\\tau|$ by up to $1.24\\times$ with probability~1.\n\n\\subsection{Non-Differential Assumption Stress Test}\n\\label{sec:nondiff_stress}\n\nOur main analysis assumes non-differential misclassification: the confusion matrix $C$ does not depend on the outcome $Y$. To assess sensitivity to violations of this assumption, we conduct a stress test on the exposure topology ($K{=}3$, $\\min_k C_{kk} \\geq 0.7$, 10{,}000 random matrices per $\\varepsilon$). For each base matrix $C_0$, observations with $Y > \\text{median}(Y)$ are misclassified using a perturbed matrix $\\tilde{C} = \\text{renormalize}(C_0 + \\varepsilon \\cdot \\Delta)$ where $\\Delta_{jk} \\sim \\text{Uniform}(-1,1)$ for $j \\neq k$, while observations with $Y \\leq \\text{median}(Y)$ retain $C_0$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Effect of differential misclassification on bias violation rates (exposure DAG, $K{=}3$, $\\min_k C_{kk} \\geq 0.7$, $N{=}50{,}000$ MC samples per trial).}\n\\label{tab:nondiff_stress}\n\\begin{tabular}{cccc}\n\\toprule\n$\\varepsilon$ & Sign-Flip (\\%) & Amplification (\\%) & Any Violation (\\%) \\\\\n\\midrule\n0.00 & 2.0 & 11.5 & 13.3 \\\\\n0.01 & 2.4 & 12.4 & 14.7 \\\\\n0.05 & 2.8 & 13.0 & 15.7 \\\\\n0.10 & 4.5 & 16.7 & 20.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\varepsilon{=}0$ baseline (13.3\\% violation) closely matches the analytical result (13.7\\%) from Section~\\ref{sec:taxonomy_results}. Even at $\\varepsilon{=}0.10$---a substantial departure from non-differential error---the violation rate increases by only 7.6 percentage points. Small departures ($\\varepsilon \\leq 0.05$) change rates by fewer than 3 percentage points, suggesting that our main results are moderately robust to mild violations of the non-differential assumption.\n\n\\paragraph{Extended stress test.}\nAn extended stress test across 96 configurations (4 topologies $\\times$ 2 $K$ $\\times$ 3 CM qualities $\\times$ 4 $\\varepsilon$, 100 MC replications each; Table~\\ref{tab:stress-test}) confirms these patterns broadly: at $\\varepsilon{=}0$, sign-flip rates are zero for all configurations; at $\\varepsilon{=}0.10$, the maximum sign-flip rate is 7\\% (IV, low-quality $C_{kk}{=}0.4$, $K{=}3$). At $K{=}10$, sign-flip rates remain zero for all topologies and $\\varepsilon$ values, suggesting that higher $K$ provides additional robustness to differential misclassification.\n\n\\input{exp_a_stress_test_table.tex}\n\n\\subsection{Robustness to Nonlinear DGP}\n\\label{sec:logistic_dgp}\n\nWe replace the linear structural equations with $Y \\sim \\text{Bernoulli}(\\sigma(\\mathbf{x}^\\top\\boldsymbol{\\beta}))$ and estimate via logistic regression (control function for IV) for all seven topologies, using $K{=}3$, six real VAST confusion matrices, 500 MC replications, and $N{=}10{,}000$. Mean sign-flip rates across the six CMs:\n\n\\begin{center}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTopology & Linear SF$_\\tau$ & Logistic SF$_\\tau$ & Linear SF$_\\text{any}$ & Logistic SF$_\\text{any}$ \\\\\n\\midrule\nConfounding & 0.000 & 0.000 & 0.573 & 0.559 \\\\\nMediation & 0.000 & 0.000 & 0.703 & 0.695 \\\\\nCollider & 0.000 & 0.000 & 0.060 & 0.060 \\\\\nExposure & --- & --- & 0.577 & 0.574 \\\\\nM-bias & 0.000 & 0.000 & 0.095 & 0.099 \\\\\nFront-door & 0.000 & 0.000 & 0.590 & 0.579 \\\\\nIV & 0.086 & 0.074 & 0.086 & 0.560 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{center}\n\nTreatment-effect sign-flip rates (SF$_\\tau$) are zero for all five guaranteed topologies under both linear and logistic DGPs, and differ by $< 0.02$ for IV. The SF$_\\text{any}$ discrepancy for IV reflects estimator dimensionality: the control function includes a residual coefficient prone to sign noise; the core comparison is SF$_\\tau$, where both estimators agree. Linear and logistic DGPs produce virtually identical sign-flip patterns across all seven topologies ($|\\Delta\\,\\text{SF}_\\tau| < 0.02$).\n\n\\subsection{Bootstrap Uncertainty of ASV}\n\\label{sec:bootstrap_asv}\n\nWe assess confusion-matrix estimation uncertainty by bootstrapping label pairs from HumAID DeepSeek zero-shot ($K{=}10$, $n{=}1{,}500$): resample with replacement $B{=}1{,}000$ times, re-estimate $C_0$, and recompute magnitude ASV $\\delta^*$ at a 10\\% bias threshold.\n\n\\begin{center}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTopology & $\\delta^*$ (point) & 95\\% CI & Valid / 1000 \\\\\n\\midrule\nConfounding & --- & --- & 0 \\\\\nExposure & 0.937 & [0.602, 1.363] & 907 \\\\\nIV & 0.754 & [0.435, 1.290] & 902 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{center}\n\nConfounding never reaches the 10\\% threshold across all 1{,}000 bootstraps, confirming robustness. For IV, the 95\\% CI spans a $3{\\times}$ range (0.435 to 1.290); practitioners should bootstrap $C_0$ rather than rely on a point estimate when ASV is near the decision boundary.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.9\\columnwidth]{exp_c_bootstrap_figure.pdf}\n\\caption{Bootstrap distribution of magnitude ASV $\\delta^*$ ($B{=}1{,}000$) for HumAID DeepSeek zero-shot ($K{=}10$). Dashed line: point estimate; shaded: 95\\% CI.}\n\\label{fig:bootstrap_asv}\n\\end{figure}\n\n\\subsection{Cross-$K$ Robustness}\n\\label{sec:cross_k_robustness}\n\nAll structural patterns persist at $K{=}5,7$ (100{,}000 matrices each): sign-flip guarantees hold for the same five topologies, and IV sign-flip rates remain within 51--53\\%.\n\n\\subsection{ASV Diagnostic Results}\n\\label{sec:asv_diagnostics}\n\nFor HumAID ($K{=}10$, 56 scenarios), 55.4\\% are flagged as magnitude-ASV-unsafe---IV, mediation, front-door, and exposure all trigger, while confounding, collider, and M-bias remain below 10\\% bias (Figure~\\ref{fig:asv_heatmap}). For CivilComments ($K{=}2$), 100\\% of scenarios are ASV-unsafe despite $F_1$ ranging from $0.69$ (7B) to $0.82$ (frontier).\n\nOverlaying all 23 empirical matrices onto the theoretical Dirichlet violation-rate curves (Figure~\\ref{fig:dirichlet_overlay}) confirms placement: VAST in the danger zone, HumAID mid-range, CivilComments approaching safe for exposure but still in IV amplification.\n\n\\subsection{ASV Stability Across DGP Parameters}\n\\label{sec:asv_stability}\n\nWe test whether ASV rankings are stable across different data-generating process (DGP) configurations by varying the treatment-effect vector $\\boldsymbol{\\beta}$ across three settings: alternating-large ($\\boldsymbol{\\beta}=[0,\\,1.0,\\,-0.5]$), same-sign ($\\boldsymbol{\\beta}=[0,\\,0.5,\\,0.3]$), and alternating-small ($\\boldsymbol{\\beta}=[0,\\,0.2,\\,-0.1]$), with $K{=}3$, $\\tau{=}0.5$, and five $C_0$ diagonal values $\\in\\{0.5,0.6,0.7,0.8,0.9\\}$.\n\n\\input{exp_e_asv_stability_table.tex}\n\nThree patterns emerge (Table~\\ref{tab:asv_stability}). First, IV magnitude ASV is identical across all three DGPs ($\\delta^*{=}0.203$). This is a mathematical identity, not an empirical finding: the Wald estimator $\\hat{\\tau}_{\\text{IV}} = \\text{RF}/\\text{FS}$ has $\\boldsymbol{\\beta}$ in both numerator and denominator, and the ratio depends only on $C$ and the first-stage structure, making ASV invariant to $\\boldsymbol{\\beta}$ by construction. Second, exposure ASV depends on the coefficient ratio structure: alternating-large ($\\beta_2/\\beta_1 = -0.5$) and alternating-small ($\\beta_2/\\beta_1 = -0.5$) share the same ratio and yield identical $\\delta^*{=}0.090$, while same-sign ($\\beta_2/\\beta_1 = 0.6$) gives $\\delta^*{=}0.223$---thus the experiment provides two distinct sign-structure conditions, not three. Third, confounding ASV depends on effect magnitudes: only alternating-large triggers the 10\\% threshold ($\\delta^*{=}0.348$); smaller effects never reach 10\\% bias.\n\nConfounding is consistently the most robust topology (highest ASV or no violation), and M-bias remains immune (not shown). However, the relative fragility of exposure vs.\\ IV inverts with coefficient sign structure: under alternating signs, exposure is most fragile ($0.090 < 0.203$); under same-sign effects, IV is most fragile ($0.203 < 0.223$). Practitioners should compute ASV with their specific DGP rather than relying on generic rankings.\n\n\\subsection{Extended Conjecture Verification}\n\\label{sec:conjecture_verify}\n\nWe test envelope monotonicity (Conjecture~\\ref{conj:monotone}) by sampling 10{,}000 random $C_0$ matrices from Dirichlet$(1,\\dots,1)$ per topology for $K \\in \\{3,5,7\\}$ (210{,}000 total), sweeping $\\delta$ in steps of 0.01, and counting matrices with at least one non-monotonic step exceeding tolerance $10^{-12}$. Bias at each $\\delta$ is computed via analytic probability limits using Gauss--Hermite quadrature (100 points), eliminating sampling noise entirely.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Envelope monotonicity violations per 10{,}000 random $C_0$ matrices. ``Worst mag.''\\ is the largest single-step deviation $|B(\\delta_{i+1})|-|B(\\delta_i)|$ in the non-monotonic direction.}\n\\label{tab:conjecture_verify}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Topology} & $K{=}3$ & $K{=}5$ & $K{=}7$ & \\textbf{Worst mag.} & \\textbf{Direction} \\\\\n\\midrule\nConfounding & 8467 & 8063 & 7892 & 0.011 & non-dec \\\\\nMediation   & 8236 & 7905 & 7893 & 0.013 & non-dec \\\\\nCollider    & 8683 & 7669 & 7570 & 0.005 & non-inc \\\\\nExposure    & 485  & 205  & 77   & 0.056 & non-dec \\\\\nM-bias      & 9791 & 7783 & 7399 & 0.002 & non-inc \\\\\nIV          & 7433 & 6015 & 5711 & $>10^6$ & non-dec \\\\\nFront-door  & 8429 & 8079 & 7899 & 0.013 & non-dec \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nViolation counts are high (60--97\\% of matrices), but magnitudes are negligible for non-IV topologies: all worst-case deviations fall below 0.06 ($<$6\\% of the respective $\\tau$). These results are computed from analytic probability limits with zero sampling noise, confirming the violations are structural properties of multi-class confusion matrices rather than numerical artifacts. IV deviations reflect Wald estimator singularities when the first-stage coefficient passes near zero---this is a property of the Wald estimator, not of the ASV parameterization. Adversarial search (500 restarts per configuration, $K \\in \\{3,5\\}$) finds genuine counterexamples for all topologies except IV $K{=}3$, confirming that strict monotonicity does not hold universally. The bias envelope is $\\varepsilon$-approximately monotonic with $\\varepsilon < 0.06$ for all six non-IV topologies. Empirically, $\\varepsilon$ scales as $O(1/K^\\alpha)$ with $\\alpha \\in [0.6, 1.5]$ (topology-dependent): for confounding, mediation, and front-door, $\\alpha \\approx 1.4$; for exposure, $\\alpha \\approx 1.0$; for collider and M-bias, $\\alpha \\approx 0.7$. A universal empirical upper bound is $\\varepsilon \\leq 0.137/\\sqrt{K}$, verified across all tested configurations ($K \\in \\{3,5,7\\}$). This scaling supports the practical validity of ASV as a sensitivity tool at any meaningful bias threshold.\n\n\\section{Notation}\n\\label{app:notation_table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Key notation used throughout the paper.}\n\\label{tab:notation}\n\\begin{tabular}{cl}\n\\toprule\n\\textbf{Symbol} & \\textbf{Description} \\\\\n\\midrule\n$K$ & Number of annotation categories \\\\\n$C$ & Column-stochastic confusion matrix, $C_{jk} = P(A^*{=}j \\mid A{=}k)$ \\\\\n$A$, $A^*$ & True and observed (misclassified) annotation \\\\\n$T$ & Treatment variable \\\\\n$Y$ & Outcome variable \\\\\n$\\tau$ & Causal effect of interest \\\\\n$\\delta$ & ASV perturbation parameter, $C(\\delta) = (1{-}\\delta)I + \\delta C_0$ \\\\\n$\\delta^*$ & Critical ASV value (magnitude/significance/sign-flip) \\\\\n$B(C)$ & Bias function, $= \\operatorname{plim}(\\hat{\\tau}) - \\tau$ \\\\\n$\\beta_k$ & Treatment effect coefficient for category $k$ \\\\\n$D_k$ & Dummy variable for category $k$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 370,
        "oldLines": 6,
        "newStart": 370,
        "newLines": 52,
        "lines": [
          " structurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.",
          " Since $V_W(\\delta)$ is non-decreasing by DPI (same argument as \\S\\ref{app:monotonicity_proof}, Step~1) and $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.",
          " ",
          "+\\paragraph{Boundedness of the leakage coefficient.}",
          "+",
          "+The mediation bias expression in~\\eqref{eq:mediation} writes the residual indirect effect as $(1-\\lambda(C))\\,\\tau_{\\mathrm{ind}}$, where",
          "+\\begin{equation}",
          "+\\label{eq:lambda_def}",
          "+  \\lambda(C) \\;:=\\; \\frac{V_B(C)}{V},\\qquad V_B(C)=\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr),\\quad V=\\operatorname{Var}(g(A)),",
          "+\\end{equation}",
          "+with $g(k)=\\mathbb{E}[T\\mid A{=}k]$ (the mediator's information about $T$). $\\lambda(C)$ measures the fraction of $g$-variance preserved by the noisy channel $A\\to A^*$: at $\\lambda(C)=1$, conditioning on $A^*$ fully blocks the mediated path; at $\\lambda(C)=0$, $A^*$ carries no information about $A$ and the entire indirect effect leaks into $\\hat\\tau_{\\mathrm{dir}}$.",
          "+",
          "+\\begin{proposition}[Mediation leakage boundedness]",
          "+\\label{prop:lambda_bound}",
          "+For any column-stochastic confusion matrix $C\\in\\mathbb{R}^{K\\times K}$ and any non-degenerate marginal $\\pi$ over $A$ with $V=\\operatorname{Var}(g(A))>0$, the leakage coefficient defined in~\\eqref{eq:lambda_def} satisfies",
          "+\\[",
          "+  \\lambda(C)\\in[0,1].",
          "+\\]",
          "+Moreover, $\\lambda(I)=1$ (perfect classification) and $\\lambda(C)=0$ whenever the rows of $C$ are identical (rank-one, uninformative classification, e.g.\\ $C=\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$).",
          "+\\end{proposition}",
          "+",
          "+\\begin{proof}",
          "+By the law of total variance applied to $g(A)$ under the joint law $P(A{=}k,A^*{=}j)=\\pi_k C_{jk}$,",
          "+\\[",
          "+  V \\;=\\; \\operatorname{Var}(g(A)) \\;=\\; \\underbrace{\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr)}_{V_B(C)} \\;+\\; \\underbrace{\\mathbb{E}\\!\\bigl[\\operatorname{Var}(g(A)\\mid A^*)\\bigr]}_{\\geq 0}.",
          "+\\]",
          "+Both terms on the right are non-negative, so $0\\leq V_B(C)\\leq V$, and dividing by $V>0$ gives $\\lambda(C)\\in[0,1]$.",
          "+",
          "+\\emph{Endpoints.}",
          "+At $C=I$, $A^*=A$ a.s., so $\\mathbb{E}[g(A)\\mid A^*]=g(A^*)$ and $V_B(I)=V$, giving $\\lambda(I)=1$.",
          "+If the rows of $C$ are identical---i.e.\\ $C_{jk}=r_k$ for every $j$---then $P(A{=}k\\mid A^*{=}j)=\\pi_k$ for every $j$, hence $\\mathbb{E}[g(A)\\mid A^*]=\\mathbb{E}[g(A)]$ is constant, $V_B=0$, and $\\lambda=0$.",
          "+This covers the uniform case $C=\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ as the symmetric instance.",
          "+\\end{proof}",
          "+",
          "+\\paragraph{Consistency with the proportional-effects formula.}",
          "+The closed form $B(C)=\\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$ derived under $f=\\lambda g$ uses $V_W(C)=\\mathbb{E}[\\operatorname{Var}(g\\mid A^*)]=V-V_B(C)$.",
          "+Equation~\\eqref{eq:mediation} and $\\tau_{\\mathrm{ind}}=B(C{=}\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top)=\\lambda V/(V+\\sigma_\\varepsilon^2)$ then yield",
          "+\\[",
          "+  1-\\lambda(C) \\;=\\; \\frac{B(C)}{\\tau_{\\mathrm{ind}}} \\;=\\; \\frac{V_W(C)\\,(V+\\sigma_\\varepsilon^2)}{V\\,(V_W(C)+\\sigma_\\varepsilon^2)},",
          "+\\]",
          "+which is monotonically decreasing in $V_B(C)$ and equals $1$ at $V_B=0$, $0$ at $V_B=V$.",
          "+Thus the simple definition~\\eqref{eq:lambda_def} and the proportional-case bias share the same $\\{0,1\\}$ endpoints; they coincide in the limit $\\sigma_\\varepsilon^2\\gg V_W$ and remain within $[0,1]$ throughout (cf.\\ Proposition~\\ref{prop:lambda_bound}).",
          "+",
          "+\\paragraph{Numerical verification.}",
          "+We sample $N=10{,}000$ column-stochastic matrices per $K\\in\\{3,5,7\\}$ (each column drawn from $\\operatorname{Dirichlet}(\\mathbf{1})$), with independently sampled $\\pi\\sim\\operatorname{Dirichlet}(\\mathbf{1})$ and $g\\sim\\mathcal{N}(0,I_K)$, and compute $\\lambda(C)$ from~\\eqref{eq:lambda_def}.",
          "+All $30{,}000$ trials satisfy $\\lambda(C)\\in[0,1]$ (observed range $[8.0{\\times}10^{-6},\\,0.894]$, zero out-of-bounds violations).",
          "+The analytic endpoints $\\lambda(I)=1$ and $\\lambda(\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top)=0$ are recovered to machine precision.",
          "+The script and results are in \\texttt{artifacts/verify\\_lambda\\_bound.py} and \\texttt{artifacts/verify\\_lambda\\_bound\\_results.json}.",
          "+",
          " \\subsection{Collider Topology ($A$ = Collider)}",
          " \\label{app:collider}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 34_

Now update the forward reference in method.tex to use \ref instead of hardcoded "Proposition~3".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "4d769d83-b9c6-45d4-a09f-beda40ae5cb0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UWrEACkypVZCwT9s3n7YJn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2911,
      "cache_read_input_tokens": 63365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2911
      },
      "output_tokens": 5,
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

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_016qdVkaJKLL2k2u5h99UoHZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
  "old_string": "where $\\lambda(C) \\in [0,1]$ summarizes attenuation (Appendix~\\ref{app:proof}, Proposition~3), with $\\lambda(I) = 1$ under perfect classification.",
  "new_string": "where $\\lambda(C) \\in [0,1]$ summarizes attenuation (Proposition~\\ref{prop:lambda_bound}), with $\\lambda(I) = 1$ under perfect classification."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "92786985-b4a4-4504-9276-40f6b6c8fbc1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UWrEACkypVZCwT9s3n7YJn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2911,
      "cache_read_input_tokens": 63365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2911
      },
      "output_tokens": 5,
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

_source line 36 · 2026-05-22T15:24:44.100Z_

<details><summary>↩ Tool result · reported error · `toolu_016qdVkaJKLL2k2u5h99UoHZ`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "c5a719b1-021e-456f-b82f-d58dc806c944",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01T6yH7Wuavmv7TpYMsRFsox`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
  "offset": 40,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "b2d708fd-57c0-4f56-8e16-00d9ad69bbf0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RsMHEdRBc4bhC37wKSrFLh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 66276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 418
      },
      "output_tokens": 65,
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

_source line 38 · 2026-05-22T15:24:48.397Z_

<details><summary>↩ Tool result · `toolu_01T6yH7Wuavmv7TpYMsRFsox`</summary>

```text
40	When $A$ mediates the $X{\to}Y$ relationship, the direct effect estimator controlling for $A^*$ has probability limit
41	\begin{equation}
42	\label{eq:mediation}
43	\text{plim}\;\hat{\tau}_{\text{direct}}(A^*) = \tau_{\text{direct}} + \bigl(1 - \lambda(C)\bigr)\,\tau_{\text{indirect}},
44	\end{equation}
45	where $\lambda(C) \in [0,1]$ summarizes attenuation (Appendix~\ref{app:proof}, Proposition~3), with $\lambda(I) = 1$ under perfect classification. Misclassification ($\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\hat{\tau}_{\text{direct}}|$ but preserving the sign ($\tau_{\text{sign\_flip}} = 0$).
46	
47	\paragraph{Collider ($A$ = collider, conditioned on $A^*$).}
48	Conditioning on a collider $A$ of $X$ and $Y$ opens a spurious path. When we condition on $A^*$ instead, misclassification attenuates this spurious association because $A^*$ is a noisy proxy for $A$. The collider topology thus exhibits a \emph{protective} property: annotation error reduces rather than amplifies the bias from collider stratification, with $\tau_{\text{sign\_flip}} = 0$.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "1d518c5b-a723-43be-8d9f-426c0d1b3fba",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
      "content": "When $A$ mediates the $X{\\to}Y$ relationship, the direct effect estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:mediation}\n\\text{plim}\\;\\hat{\\tau}_{\\text{direct}}(A^*) = \\tau_{\\text{direct}} + \\bigl(1 - \\lambda(C)\\bigr)\\,\\tau_{\\text{indirect}},\n\\end{equation}\nwhere $\\lambda(C) \\in [0,1]$ summarizes attenuation (Appendix~\\ref{app:proof}, Proposition~3), with $\\lambda(I) = 1$ under perfect classification. Misclassification ($\\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\\hat{\\tau}_{\\text{direct}}|$ but preserving the sign ($\\tau_{\\text{sign\\_flip}} = 0$).\n\n\\paragraph{Collider ($A$ = collider, conditioned on $A^*$).}\nConditioning on a collider $A$ of $X$ and $Y$ opens a spurious path. When we condition on $A^*$ instead, misclassification attenuates this spurious association because $A^*$ is a noisy proxy for $A$. The collider topology thus exhibits a \\emph{protective} property: annotation error reduces rather than amplifies the bias from collider stratification, with $\\tau_{\\text{sign\\_flip}} = 0$.\n",
      "numLines": 10,
      "startLine": 40,
      "totalLines": 101
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_0199JcdeRk8h3cMxyoQxUTyq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
  "old_string": "where $\\lambda(C) \\in [0,1]$ summarizes attenuation (Appendix~\\ref{app:proof}, Proposition~3), with $\\lambda(I) = 1$ under perfect classification.",
  "new_string": "where $\\lambda(C) \\in [0,1]$ summarizes attenuation (Proposition~\\ref{prop:lambda_bound}), with $\\lambda(I) = 1$ under perfect classification."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "f5e2c691-77f2-4708-874b-9ec6d0eb0ce2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01YZGuDvgSFpRSZpokeJ4oGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 66694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 692
      },
      "output_tokens": 66,
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

_source line 40 · 2026-05-22T15:24:52.641Z_

<details><summary>↩ Tool result · `toolu_0199JcdeRk8h3cMxyoQxUTyq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "88239582-4047-4036-8162-78ce4ed5f72a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
    "oldString": "where $\\lambda(C) \\in [0,1]$ summarizes attenuation (Appendix~\\ref{app:proof}, Proposition~3), with $\\lambda(I) = 1$ under perfect classification.",
    "newString": "where $\\lambda(C) \\in [0,1]$ summarizes attenuation (Proposition~\\ref{prop:lambda_bound}), with $\\lambda(I) = 1$ under perfect classification.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Setup and Notation}\n\\label{sec:notation}\n\nLet $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \\mid A{=}k)$, where each column sums to one. Following \\citet{hernan_cole2009}, we represent this measurement process using \\emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.\n\n\\begin{definition}[Non-differential misclassification]\n\\label{def:nondiff}\nMisclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\\mathbf{Z}$ if $P(A^*{=}j \\mid A{=}k, Y, \\mathbf{Z}) = P(A^*{=}j \\mid A{=}k) = C_{jk}$ for all $j,k$.\n\\end{definition}\n\nThis assumption is satisfied when the LLM does not observe outcome-related text during annotation---for instance, when treatment labels are assigned from source documents that exclude outcome measurements.\n\nWe study seven canonical DAG topologies (Figure~\\ref{fig:dag_taxonomy})~\\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.\n\n\\subsection{Multi-Class Bias Expressions}\n\\label{sec:bias_expressions}\n\nFor each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\\tau$ denote the target causal parameter and $\\hat{\\tau}(A^*)$ the estimator using misclassified annotations.\n\n\\paragraph{Confounding ($A$ = confounder).}\nWhen $A$ confounds the $X{\\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:confounding}\n\\text{plim}\\;\\hat{\\tau}(A^*) = \\bigl(\\mathbb{E}[Z^{\\prime}Z]\\bigr)^{-1}\\mathbb{E}[Z^{\\prime}X]\\,\\boldsymbol{\\beta},\n\\end{equation}\nwhere $Z = [X, \\text{dummies}(A^*)]$, $\\boldsymbol{\\beta}$ contains the true coefficients, and the target parameter $\\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\\hat{\\tau}$ is preserved: $\\tau_{\\text{sign\\_flip}} = 0$ structurally.\\footnote{This result is consistent with \\citet{brenner1993}, who showed that the adjusted estimate with misclassified polytomous confounders can be biased toward or away from the null. Both findings hold simultaneously: misclassification degrades confounding control, producing residual bias whose magnitude can exceed the correctly adjusted estimate (amplification), but the treatment effect sign is never reversed. The distinction is between \\emph{sign reversal} ($\\text{sign}(\\hat{\\tau}) \\neq \\text{sign}(\\tau)$, which we show never occurs) and \\emph{amplification} ($|\\hat{\\tau}| > |\\tau|$, which occurs universally in this topology).}\n\n\\paragraph{Exposure ($A$ = treatment variable).}\nWhen $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:\n\\begin{equation}\n\\label{eq:exposure}\n\\text{plim}\\;\\hat{\\beta}_j(A^*) = \\sum_{k=1}^{K} w_{jk}\\,\\beta_k,\n\\end{equation}\nwhere $w_{jk}$ depends on the confusion matrix $C$ and the marginal distribution of $A$. Unlike the binary case, where non-differential misclassification guarantees attenuation toward the null~\\cite{brenner1993}, the $K{\\geq}3$ case permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \\emph{sign reversal}. A near-permutation confusion matrix effectively swaps category labels, making sign reversal the dominant outcome (83.4\\% under uniform Dirichlet prior). This failure mode is structurally impossible at $K{=}2$ because a $2{\\times}2$ stochastic matrix with positive diagonal cannot reverse the sign of a single coefficient.\n\n\\paragraph{Mediation ($A$ = mediator).}\nWhen $A$ mediates the $X{\\to}Y$ relationship, the direct effect estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:mediation}\n\\text{plim}\\;\\hat{\\tau}_{\\text{direct}}(A^*) = \\tau_{\\text{direct}} + \\bigl(1 - \\lambda(C)\\bigr)\\,\\tau_{\\text{indirect}},\n\\end{equation}\nwhere $\\lambda(C) \\in [0,1]$ summarizes attenuation (Appendix~\\ref{app:proof}, Proposition~3), with $\\lambda(I) = 1$ under perfect classification. Misclassification ($\\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\\hat{\\tau}_{\\text{direct}}|$ but preserving the sign ($\\tau_{\\text{sign\\_flip}} = 0$).\n\n\\paragraph{Collider ($A$ = collider, conditioned on $A^*$).}\nConditioning on a collider $A$ of $X$ and $Y$ opens a spurious path. When we condition on $A^*$ instead, misclassification attenuates this spurious association because $A^*$ is a noisy proxy for $A$. The collider topology thus exhibits a \\emph{protective} property: annotation error reduces rather than amplifies the bias from collider stratification, with $\\tau_{\\text{sign\\_flip}} = 0$.\n\n\\paragraph{M-bias ($A$ = intermediate collider).}\nIn the M-shaped DAG ($U_1 \\to X$, $U_1 \\to A$, $U_2 \\to A$, $U_2 \\to Y$, $X \\to Y$), adjusting for $A$ introduces a small spurious association via the M-bias path~\\cite{greenland2003}. Misclassifying $A$ weakens this adjustment, reducing the M-bias. This topology is \\emph{immune}: $\\hat{\\tau}(A^*)$ is closer to $\\tau$ than $\\hat{\\tau}(A)$ for all non-trivial confusion matrices, yielding $\\text{ASV} = \\infty$.\n\n\\paragraph{Front-door ($A$ = front-door mediator).}\nIn the front-door DAG ($X \\to A \\to Y$ with unmeasured $U \\to X$, $U \\to Y$), the front-door estimator~\\cite{bellemare_bloem2024} uses $A$ to identify effects despite unmeasured confounding. Misclassification attenuates both $X \\to A$ and $A \\to Y$ relationships, producing moderate bias with $\\tau_{\\text{sign\\_flip}} = 0$.\n\n\\paragraph{Instrumental variable ($A$ = instrument).}\nThe Wald estimator~\\cite{angrist_imbens1995} $\\hat{\\tau}_{\\text{IV}} = \\hat{\\text{cov}}(A^*, Y) / \\hat{\\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign, causing the ratio estimator to diverge or flip. Under random Dirichlet matrices, 52.6\\% produce sign reversal, making IV the most fragile topology.\n\n\\paragraph{Structural sign-flip guarantee.}\n\\begin{proposition}[Sign preservation---analytic results]\n\\label{prop:signflip}\nUnder non-differential misclassification with $C_{kk} > 0$ for all $k$:\n\\emph{(a)}~Confounding preserves sign when $\\operatorname{sign}(\\tau) = \\operatorname{sign}(\\tau {+} B_{\\mathrm{OV}})$, where $B_{\\mathrm{OV}} {=} \\operatorname{Cov}(g(A),f(A))/\\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\\ref{app:confounding}).\n\\emph{(b)}~Collider preserves sign when $|\\tau| > \\sqrt{\\operatorname{Var}(g)\\operatorname{Var}(h)}/\\mathbb{E}[\\operatorname{Var}(T{\\mid}A)]$ (Berkson attenuation; Appendix~\\ref{app:collider}).\n\\emph{(c)}~Exposure can produce sign reversal for $K {\\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\\ref{app:exposure}).\n\\end{proposition}\n\n\\paragraph{Numerical Verification 1} (Mediation, M-bias, front-door).\nSign preservation holds under topology-specific conditions: mediation requires $\\operatorname{sign}(\\tau_{\\mathrm{dir}}) {=} \\operatorname{sign}(\\tau_{\\mathrm{total}})$; front-door requires $\\operatorname{sign}(\\lambda\\alpha_U) {=} \\operatorname{sign}(\\lambda\\alpha_U {+} \\operatorname{Cov}(T,f(A)))$; M-bias is attenuating for all $C$. Verified across 100{,}000 random matrices with zero violations (Appendix~\\ref{app:conditions}); analytic proofs for general $K$ remain open.\n\nThese conditions involve true DGP parameters, which in practice must be estimated. The ASV framework (§\\ref{sec:asv}) provides a complementary assessment that does not require knowledge of the exact sufficient conditions.\n\n\\subsection{Annotation Sensitivity Values}\n\\label{sec:asv}\n\nWe introduce Annotation Sensitivity Values (ASVs) as a unified sensitivity analysis framework, analogous to E-values for unmeasured confounding~\\cite{vanderweele_ding2017} but designed for annotation-induced bias.\n\n\\paragraph{Parameterization.}\nWe parameterize the confusion matrix as $C(\\delta) = (1{-}\\delta)I + \\delta C_0$, where $C_0$ is a reference confusion matrix (e.g., estimated from a validation set) and $\\delta \\geq 0$ controls the severity of misclassification. At $\\delta{=}0$, classification is perfect; at $\\delta{=}1$, classification matches $C_0$. Non-negativity of $C(\\delta)$ requires $\\delta \\leq \\delta_{\\max} = \\min_j \\frac{1}{1 - (C_0)_{jj}}$. Since $(C_0)_{jj} \\in [0,1]$, we have $\\delta_{\\max} \\geq 1$ for all valid $C_0$, ensuring the full range $[0,1]$ is always feasible; all ASV computations are constrained to $[0, \\delta_{\\max}]$. In practice, $C_0$ is estimated from a finite validation set and subject to sampling uncertainty; we recommend bootstrapping $C_0$ and reporting ASV confidence intervals. The linear path $C(\\delta)$ is the natural first-order approximation; alternative parameterizations (e.g., matrix exponential or Dirichlet-based paths) could capture nonlinear degradation but sacrifice the interpretability of $\\delta$ as a scalar severity dial.\n\n\\paragraph{Three ASV types.}\nWe define three complementary measures: (1)~\\textbf{Magnitude ASV} $\\delta^*_{\\text{mag}} = \\min\\{\\delta : |\\text{plim}\\;\\hat{\\tau}(C(\\delta)) - \\tau| > \\epsilon\\}$---analogous to E-values; (2)~\\textbf{Significance ASV} $\\delta^*_{\\text{sig}} = \\min\\{\\delta : |\\text{plim}\\;\\hat{\\tau}(C(\\delta))| < z_{\\alpha/2} \\cdot SE(N)\\}$---relevant for attenuating topologies; (3)~\\textbf{Sign-flip ASV} $\\delta^*_{\\text{sf}} = \\min\\{\\delta : \\text{sign}(\\hat{\\tau}) \\neq \\text{sign}(\\tau)\\}$---exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.\n\n\\begin{theorem}[Envelope monotonicity---confounding and mediation]\n\\label{thm:monotone}\nFor confounding and mediation topologies with proportional effects ($f = \\lambda g$ for some scalar $\\lambda$) under $C(\\delta) = (1{-}\\delta)I + \\delta C_0$, $|B(C(\\delta))|$ is monotonically non-decreasing in $\\delta \\in [0, \\delta_{\\max}]$.\n\\end{theorem}\n\n\\emph{Proof sketch.} Both topologies reduce to $B(C(\\delta)) {=} \\lambda V_W(\\delta)/(V_W(\\delta) {+} \\sigma^2)$ where $V_W(\\delta) {=} \\operatorname{Var}(g) {-} \\operatorname{Var}(\\mathbb{E}[g{\\mid}A^*_\\delta])$ and $\\sigma^2$ is a topology-specific constant ($\\sigma_T^2$ for confounding, $\\mathbb{E}[\\operatorname{Var}(T{\\mid}A)]$ for mediation). As $\\delta$ increases, $A^*$ becomes a noisier channel for $A$, so $\\operatorname{Var}(\\mathbb{E}[g{\\mid}A^*_\\delta])$ decreases by the data processing inequality, increasing $V_W$. Since $x/(x{+}c)$ is increasing for $c{>}0$, $|B|$ is non-decreasing (full proofs in Appendix~\\ref{app:monotonicity_proof} and~\\ref{par:med_monotone}). For general (non-proportional) effects, numerical verification across 10{,}000 random matrices confirms $\\varepsilon$-approximate monotonicity with $\\varepsilon < 0.02$ (Appendix~\\ref{app:monotonicity_proof}).\n\n\\begin{conjecture}[$\\varepsilon$-approximate envelope monotonicity]\n\\label{conj:monotone}\nFor the five remaining non-IV topologies under $C(\\delta) = (1{-}\\delta)I + \\delta C_0$: exposure and front-door are $\\varepsilon$-approximately non-decreasing in $\\delta$, and collider and M-bias (protective topologies) are $\\varepsilon$-approximately non-increasing in $\\delta$, with $\\varepsilon < 0.06$ ($<$6\\% of $\\tau$). Verified across 10{,}000 random matrices per topology and $K \\in \\{3,5,7\\}$ using analytic probability limits (Appendix~\\ref{sec:conjecture_verify}).\n\\end{conjecture}\n\nThe instrumental variable topology is excluded from Conjecture~\\ref{conj:monotone}: the Wald estimator $\\hat{\\tau} = \\hat{\\gamma}_{Y{\\sim}A^*} / \\hat{\\gamma}_{T{\\sim}A^*}$ exhibits singularities when the first-stage coefficient passes through zero as $\\delta$ increases, producing unbounded deviations ($>10^6$). This is a property of the Wald estimator itself, not of the ASV framework; magnitude ASV remains well-defined for IV away from first-stage singularities.\n\nWhen strict monotonicity holds only approximately ($\\varepsilon < 0.06$), the reported ASV threshold $\\delta^*$ may differ from the true threshold by at most $\\varepsilon/\\eta$ in $\\delta$-units, where $\\eta$ is the practitioner's bias tolerance. At the recommended $\\eta = 10\\%$, this uncertainty is below 0.6 $\\delta$-steps---negligible for practical sensitivity assessment. Topology rankings (which topologies are most fragile) are preserved across all tested configurations.\n\nBinarization of $K{=}3$ annotations introduces additional topology-dependent bias (Appendix~\\ref{app:binarization}).\n",
    "structuredPatch": [
      {
        "oldStart": 42,
        "oldLines": 7,
        "newStart": 42,
        "newLines": 7,
        "lines": [
          " \\label{eq:mediation}",
          " \\text{plim}\\;\\hat{\\tau}_{\\text{direct}}(A^*) = \\tau_{\\text{direct}} + \\bigl(1 - \\lambda(C)\\bigr)\\,\\tau_{\\text{indirect}},",
          " \\end{equation}",
          "-where $\\lambda(C) \\in [0,1]$ summarizes attenuation (Appendix~\\ref{app:proof}, Proposition~3), with $\\lambda(I) = 1$ under perfect classification. Misclassification ($\\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\\hat{\\tau}_{\\text{direct}}|$ but preserving the sign ($\\tau_{\\text{sign\\_flip}} = 0$).",
          "+where $\\lambda(C) \\in [0,1]$ summarizes attenuation (Proposition~\\ref{prop:lambda_bound}), with $\\lambda(I) = 1$ under perfect classification. Misclassification ($\\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\\hat{\\tau}_{\\text{direct}}|$ but preserving the sign ($\\tau_{\\text{sign\\_flip}} = 0$).",
          " ",
          " \\paragraph{Collider ($A$ = collider, conditioned on $A^*$).}",
          " Conditioning on a collider $A$ of $X$ and $Y$ opens a spurious path. When we condition on $A^*$ instead, misclassification attenuates this spurious association because $A^*$ is a noisy proxy for $A$. The collider topology thus exhibits a \\emph{protective} property: annotation error reduces rather than amplifies the bias from collider stratification, with $\\tau_{\\text{sign\\_flip}} = 0$."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 41_

Now compile to confirm the proposition typesets cleanly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "97a32ac2-d3e9-49d0-a990-81dfd017e014",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KfXdeRJG2dBvWfeh9sDkTg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 67386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
      },
      "output_tokens": 2,
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

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01VQUdeZbpKP5XWCvm4Pz8aq`</summary>

```json
{
  "command": "cd docs/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -40",
  "description": "Compile LaTeX to check for errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "650d66a8-65cf-4d3f-9381-b09b7e4749cb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KfXdeRJG2dBvWfeh9sDkTg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 67386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
      },
      "output_tokens": 2,
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

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "brn83xnyn",
  "tool_use_id": "toolu_01VQUdeZbpKP5XWCvm4Pz8aq",
  "description": "Compile LaTeX to check for errors",
  "task_type": "local_bash",
  "uuid": "7cbbee5d-fdd9-4edd-863a-f7135175d068",
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727"
}
```

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "brn83xnyn",
  "tool_use_id": "toolu_01VQUdeZbpKP5XWCvm4Pz8aq",
  "status": "completed",
  "output_file": "",
  "summary": "Compile LaTeX to check for errors",
  "uuid": "d16bd1c7-3a92-452f-ae2f-a3d4b5c6b515",
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727"
}
```

---

### Tool result

_source line 45 · 2026-05-22T15:24:59.945Z_

<details><summary>↩ Tool result · `toolu_01VQUdeZbpKP5XWCvm4Pz8aq`</summary>

```text
s/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmcsc10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi
7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u
rw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/zapfding/
uzdr.pfb>
Output written on main.pdf (24 pages, 875176 bytes).
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "0b8699be-a603-4d9f-8e50-403ca6b36f7a",
  "tool_use_result": {
    "stdout": "s/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmcsc10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi\n7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u\nrw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/zapfding/\nuzdr.pfb>\nOutput written on main.pdf (24 pages, 875176 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01EpGAzJXi87FBQZHhxJcf1U`</summary>

```json
{
  "command": "cd docs/paper && grep -E \"undefined|Warning.*ref|multiply defined\" main.log | head -20",
  "description": "Check for ref warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "28d92ddf-555c-4a8d-ac0a-7f423e4aa66b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0158cHs1964pp7VPaLhErQdF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1839,
      "cache_read_input_tokens": 67776,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1839
      },
      "output_tokens": 56,
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

_source line 47 · 2026-05-22T15:25:03.062Z_

<details><summary>↩ Tool result · reported error · `toolu_01EpGAzJXi87FBQZHhxJcf1U`</summary>

```text
Exit code 1
/bin/bash: line 1: cd: docs/paper: No such file or directory
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "e822d00a-4eee-433e-a9c9-e78a0113fdd5",
  "tool_use_result": "Error: Exit code 1\n/bin/bash: line 1: cd: docs/paper: No such file or directory"
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Grep · `toolu_01M26v8nUTgSzbABV1AcxuFU`</summary>

```json
{
  "pattern": "undefined|Warning.*[Rr]ef|multiply defined|prop:lambda_bound",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.log",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "0b42163c-1f98-4c11-894c-f039ce3937c7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017eXMxy6dcBS5jswzmHQCxT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 181,
      "cache_read_input_tokens": 69615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 181
      },
      "output_tokens": 52,
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

_source line 49 · 2026-05-22T15:25:09.185Z_

<details><summary>↩ Tool result · `toolu_01M26v8nUTgSzbABV1AcxuFU`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "4038b048-0a1f-4701-a42c-0827ff8309fd",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "a924fd43-7ade-45d5-bf8c-0948d764ece5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01GogJfWz6vZ7yQfzTiry13G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 69796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
      },
      "output_tokens": 40,
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

_source line 51_

<details open><summary>🔧 Tool call — Grep · `toolu_01KQHWzPTtSKxCHwLSiSJAc4`</summary>

```json
{
  "pattern": "prop:lambda_bound",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.aux",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "93201db4-0208-4080-b116-56d972cc4b4c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01GogJfWz6vZ7yQfzTiry13G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 69796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
      },
      "output_tokens": 40,
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

_source line 52 · 2026-05-22T15:25:16.700Z_

<details><summary>↩ Tool result · `toolu_01KQHWzPTtSKxCHwLSiSJAc4`</summary>

```text
1524:\newlabel{prop:lambda_bound}{{4}{15}{Mediation leakage boundedness}{proposition.4}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "977ddce1-82c0-4760-9f2c-8a537c656e57",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1524:\\newlabel{prop:lambda_bound}{{4}{15}{Mediation leakage boundedness}{proposition.4}{}}",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 53_

Label resolved as Proposition 4 on page 15. Registering the new artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "761dc5fd-070b-4844-bcb7-26845b0813ce",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Mu557hRynoarui7HtdBzZa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 317,
      "cache_read_input_tokens": 70024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 317
      },
      "output_tokens": 2,
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

_source line 54_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011z1ZoDPMWNcMZo2Uq4QgJy`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "c3d0f0b2-8a4b-4da4-a0b2-8fb105db6954",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Mu557hRynoarui7HtdBzZa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 317,
      "cache_read_input_tokens": 70024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 317
      },
      "output_tokens": 2,
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

_source line 55 · 2026-05-22T15:25:20.126Z_

<details><summary>↩ Tool result · `toolu_011z1ZoDPMWNcMZo2Uq4QgJy`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "569c0f3a-7dfc-4580-b4cd-fef4048c7e4c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_015zpUW4t8E81nM2NFog6G7Q`</summary>

```json
{
  "name": "verify_lambda_bound",
  "type": "intermediate",
  "description": "Numerical verification that the mediation leakage coefficient lambda(C)=V_B/V lies in [0,1] across 30,000 random (C, pi, g) triples for K in {3,5,7}. Observed range [8e-6, 0.894], zero OOB. Analytic endpoints lambda(I)=1 and lambda(uniform)=0 recovered to machine precision. Supports Proposition prop:lambda_bound in appendix_proofs.tex.",
  "project": "causal_annot_error_attrib",
  "source_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/verify_lambda_bound.py",
  "tags": [
    "mediation",
    "proof",
    "appendix",
    "lambda_bound"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "76f687a0-b716-4bcf-b880-ba8c43b22d99",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01YEFKBRTzjY748FXKAxVo6u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 55054,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 55054
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 55024
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-22T15:25:27.936Z_

<details><summary>↩ Tool result · `toolu_015zpUW4t8E81nM2NFog6G7Q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_81fd9c\", \"name\": \"verify_lambda_bound\", \"type\": \"intermediate\", \"description\": \"Numerical verification that the mediation leakage coefficient lambda(C)=V_B/V lies in [0,1] across 30,000 random (C, pi, g) triples for K in {3,5,7}. Observed range [8e-6, 0.894], zero OOB. Analytic endpoints lambda(I)=1 and lambda(uniform)=0 recovered to machine precision. Supports Proposition prop:lambda_bound in appendix_proofs.tex.\", \"path\": \"projects/causal_annot_error_attrib/artifacts/_project/intermediate/verify_lambda_bound.py\", \"url\": null, \"project\": \"causal_annot_error_attrib\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T15:25:27.708220+00:00\", \"tags\": [\"mediation\", \"proof\", \"appendix\", \"lambda_bound\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "6ecb7ca8-5884-4006-91a5-11f72e57ae26",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260522_81fd9c\\\", \\\"name\\\": \\\"verify_lambda_bound\\\", \\\"type\\\": \\\"intermediate\\\", \\\"description\\\": \\\"Numerical verification that the mediation leakage coefficient lambda(C)=V_B/V lies in [0,1] across 30,000 random (C, pi, g) triples for K in {3,5,7}. Observed range [8e-6, 0.894], zero OOB. Analytic endpoints lambda(I)=1 and lambda(uniform)=0 recovered to machine precision. Supports Proposition prop:lambda_bound in appendix_proofs.tex.\\\", \\\"path\\\": \\\"projects/causal_annot_error_attrib/artifacts/_project/intermediate/verify_lambda_bound.py\\\", \\\"url\\\": null, \\\"project\\\": \\\"causal_annot_error_attrib\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-22T15:25:27.708220+00:00\\\", \\\"tags\\\": [\\\"mediation\\\", \\\"proof\\\", \\\"appendix\\\", \\\"lambda_bound\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_81fd9c\", \"name\": \"verify_lambda_bound\", \"type\": \"intermediate\", \"description\": \"Numerical verification that the mediation leakage coefficient lambda(C)=V_B/V lies in [0,1] across 30,000 random (C, pi, g) triples for K in {3,5,7}. Observed range [8e-6, 0.894], zero OOB. Analytic endpoints lambda(I)=1 and lambda(uniform)=0 recovered to machine precision. Supports Proposition prop:lambda_bound in appendix_proofs.tex.\", \"path\": \"projects/causal_annot_error_attrib/artifacts/_project/intermediate/verify_lambda_bound.py\", \"url\": null, \"project\": \"causal_annot_error_attrib\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T15:25:27.708220+00:00\", \"tags\": [\"mediation\", \"proof\", \"appendix\", \"lambda_bound\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 58_

完成。

**产出**：
- `artifacts/verify_lambda_bound.py` — Dirichlet 采样 + law-of-total-variance 计算
- `artifacts/verify_lambda_bound_results.json` — 验证结果
- `docs/paper/appendix_proofs.tex` — 在 `\paragraph{Mediation monotonicity (proportional effects).}` 之后追加 `\paragraph{Boundedness of the leakage coefficient.}`、定义 (eq:lambda_def)、`\begin{proposition}[Mediation leakage boundedness]\label{prop:lambda_bound}`、proof（LoTV + 两端点）、与 proportional-case 公式的一致性说明、numerical verification 段落
- `docs/paper/method.tex:45` — 把硬编码 "Proposition~3" 改为 `\ref{prop:lambda_bound}`（编译后解析为 Proposition 4）

**证明结构**：定义 λ(C) := V_B(C)/V，其中 V_B = Var(E[g|A*])、V = Var(g)、g(k) = E[T|A=k]。LoTV 给出 V = V_B + E[Var(g|A*)]，两项非负 ⇒ λ ∈ [0,1]。λ(I)=1 因 A*=A；λ=0 当 C 行恒等（含 uniform 作为对称特例），此时 E[g|A*] 恒为 E[g]。

**数值验证**：K ∈ {3,5,7} 各 10000 次随机采样（每列 Dirichlet(1,1,1)，π~Dir(1)，g~N(0,I)）。λ 范围 [8.0e-6, 0.894]，0 次越界；λ(I)=1.0、λ(uniform)≈3.8e-34（机器精度）。

**LaTeX 编译**：`latexmk -pdf` 成功，24 页，无 undefined ref / multiply defined 警告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "uuid": "921abf68-51d8-4882-a9ce-2a1bc320adeb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HyqKeqm11hDoYoSfdK7wVZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 71388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 940
      },
      "output_tokens": 1,
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

### Task result

_source line 59_

完成。

**产出**：
- `artifacts/verify_lambda_bound.py` — Dirichlet 采样 + law-of-total-variance 计算
- `artifacts/verify_lambda_bound_results.json` — 验证结果
- `docs/paper/appendix_proofs.tex` — 在 `\paragraph{Mediation monotonicity (proportional effects).}` 之后追加 `\paragraph{Boundedness of the leakage coefficient.}`、定义 (eq:lambda_def)、`\begin{proposition}[Mediation leakage boundedness]\label{prop:lambda_bound}`、proof（LoTV + 两端点）、与 proportional-case 公式的一致性说明、numerical verification 段落
- `docs/paper/method.tex:45` — 把硬编码 "Proposition~3" 改为 `\ref{prop:lambda_bound}`（编译后解析为 Proposition 4）

**证明结构**：定义 λ(C) := V_B(C)/V，其中 V_B = Var(E[g|A*])、V = Var(g)、g(k) = E[T|A=k]。LoTV 给出 V = V_B + E[Var(g|A*)]，两项非负 ⇒ λ ∈ [0,1]。λ(I)=1 因 A*=A；λ=0 当 C 行恒等（含 uniform 作为对称特例），此时 E[g|A*] 恒为 E[g]。

**数值验证**：K ∈ {3,5,7} 各 10000 次随机采样（每列 Dirichlet(1,1,1)，π~Dir(1)，g~N(0,I)）。λ 范围 [8.0e-6, 0.894]，0 次越界；λ(I)=1.0、λ(uniform)≈3.8e-34（机器精度）。

**LaTeX 编译**：`latexmk -pdf` 成功，24 页，无 undefined ref / multiply defined 警告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 257778,
  "duration_api_ms": 253068,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "acc969f7-460f-41bd-96a7-c1f7ced72727",
  "total_cost_usd": 1.6779895,
  "usage": {
    "input_tokens": 28,
    "cache_creation_input_tokens": 110094,
    "cache_read_input_tokens": 1061226,
    "output_tokens": 18297,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 110094,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 670,
        "cache_read_input_tokens": 71388,
        "cache_creation_input_tokens": 940,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 940
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1624,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001724,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 28,
      "outputTokens": 18297,
      "cacheReadInputTokens": 1061226,
      "cacheCreationInputTokens": 110094,
      "webSearchRequests": 0,
      "costUSD": 1.6762655,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c07a027c-a00f-40c9-9ca0-e068876deac2"
}
```

</details>

---
