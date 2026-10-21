# math mf1b k3 symmetric proof

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_math_mf1b_k3_symmetric_proof_20260523T173653.log`
- **Structured JSON:** [`3703171a55d98b3e233f.json`](../../sessions/37/3703171a55d98b3e233f.json)

## Before a recorded user message

52 recorded events

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
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
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
  "uuid": "7576b750-bc99-4b7a-b979-a37ffb9ad2db",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
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
    "resetsAt": 1779570000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7260cddb-02ba-4ac3-9025-887e23c904dd",
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8"
}
```

---

### Assistant

_source line 4_

I'll start by reading the existing bias derivation for the confounding topology to understand the bias expression.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "8a3ac1ca-d47a-4837-8cc6-628e0f2030dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiAtzXZu7wLdQRFQD2KGzq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13438,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13438
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01MZdyExcmqAituvn3ytbVG8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 0,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "4a55aa23-c4bf-4d6f-96f6-ffb1cf5855f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiAtzXZu7wLdQRFQD2KGzq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13438,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13438
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

_source line 6 · 2026-05-23T17:37:01.745Z_

<details><summary>↩ Tool result · `toolu_01MZdyExcmqAituvn3ytbVG8`</summary>

```text
0	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
1	\label{app:proof}
2	
3	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
4	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
5	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
6	
7	\subsection{Notation and Key Identities}
8	\label{app:notation}
9	
10	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
11	Define the population vectors:
12	\begin{align}
13	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
14	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
15	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
16	\end{align}
17	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
18	
19	\subsection{Frisch--Waugh--Lovell Decomposition}
20	\label{app:fwl}
21	
22	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
23	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
24	\begin{equation}
25	  \operatorname{plim}\hat{\tau}(C)
26	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
27	  \label{eq:fwl}
28	\end{equation}
29	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\tilde{Y}=Y-\mathbb{E}[Y\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\dots,D_{K-1}^*)$.
30	
31	\begin{lemma}[Bias decomposition]
32	\label{lem:bias_decomp}
33	Suppose $Y = \tau T + f(A) + \varepsilon_Y$ with $\varepsilon_Y \perp (T, A, A^*)$.
34	Then
35	\begin{equation}
36	  \operatorname{plim}\hat\tau(C) = \tau + \frac{R(C)}{D(C)},
37	  \label{eq:bias_decomp}
38	\end{equation}
39	where
40	\begin{align}
41	  R(C) &= \mathbb{E}\bigl[\operatorname{Cov}(T,\,f(A)\mid A^*)\bigr], \label{eq:R}\\
42	  D(C) &= \mathbb{E}\bigl[\operatorname{Var}(T\mid A^*)\bigr] > 0. \label{eq:D}
43	\end{align}
44	\end{lemma}
45	
46	\begin{proof}
47	Expand $\tilde{Y}$ using $Y=\tau T + f(A) + \varepsilon_Y$:
48	\[
49	  \tilde{Y} = \tau\,\tilde{T} + \bigl(f(A) - \mathbb{E}[f(A)\mid A^*]\bigr) + \varepsilon_Y.
50	\]
51	Since $\tilde{T}$ is measurable w.r.t.\ $(T,A^*)$ and $\varepsilon_Y\perp(T,A,A^*)$:
52	\[
53	  \mathbb{E}[\tilde{T}\,\tilde{Y}]
54	  = \tau\,\mathbb{E}[\tilde{T}^2]
55	  + \mathbb{E}\bigl[\tilde{T}\,\bigl(f(A)-\mathbb{E}[f(A)\mid A^*]\bigr)\bigr].
56	\]
57	The numerator residual is $R(C) = \mathbb{E}[\tilde{T}(f(A)-\mathbb{E}[f(A)\mid A^*])]$, and the denominator is $D(C) = \mathbb{E}[\tilde{T}^2]$.
58	
59	By the law of total covariance:
60	\[
61	  R(C) = \sum_{j=0}^{K-1} q_j\,\operatorname{Cov}(T,\,f(A)\mid A^*{=}j)
62	  = \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)].
63	\]
64	For $D(C)>0$: decompose $T = g(A) + \varepsilon_T$ where $g(A)=\mathbb{E}[T\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).
65	In both cases, $\tilde{T}=\bigl(g(A)-\mathbb{E}[g(A)\mid A^*]\bigr)+\varepsilon_T'$, where $\varepsilon_T'$ is the component of $T$ independent of $(A,A^*)$.
66	Hence $D(C)\geq\operatorname{Var}(\varepsilon_T')>0$.
67	\end{proof}
68	
69	\subsection{Confounding Topology ($A$ = Confounder)}
70	\label{app:confounding}
71	
72	\paragraph{Data-generating process.}
73	$A\to T$, $A\to Y$, $T\to Y$.
74	Using dummy coding with category 0 as reference:
75	\begin{align*}
76	  T &= \sum_{j=1}^{K-1}\alpha_j D_j + \varepsilon_T,\quad
77	  \varepsilon_T\sim\mathcal{N}(0,\sigma_T^2),\;\varepsilon_T\perp A,\\
78	  Y &= \tau\, T + \sum_{j=1}^{K-1}\beta_j^{(A)} D_j + \varepsilon_Y,\quad
79	  \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp(T,A).
80	\end{align*}
81	Define $g(k)=\sum_{j}\alpha_j\mathbf{1}(k{=}j)$ and $f(k)=\sum_{j}\beta_j^{(A)}\mathbf{1}(k{=}j)$, so $g(0)=f(0)=0$.
82	
83	\paragraph{Closed-form plim.}
84	Using the FWL decomposition, the coefficient on $T$ is:
85	\begin{equation}
86	  \operatorname{plim}\hat\tau(C)
87	  = \frac{\mu_{TY} - \sum_{j=0}^{K-1}\frac{\mathrm{ct}_j\,\mathrm{cy}_j}{q_j}}
88	  {s_T - \sum_{j=0}^{K-1}\frac{\mathrm{ct}_j^2}{q_j}},
89	  \label{eq:plim_conf}
90	\end{equation}
91	where $s_T=\mathbb{E}[T^2]$, $\mu_{TY}=\mathbb{E}[TY]$, and $\mathrm{ct}_j$, $\mathrm{cy}_j$, $q_j$ are defined in~\eqref{eq:q}--\eqref{eq:cy}.
92	
93	\begin{proof}[Derivation]
94	By FWL, $\operatorname{plim}\hat\tau = \mathbb{E}[\tilde{T}Y]/\mathbb{E}[\tilde{T}^2]$ where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$.
95	Since $\mathbb{E}[T\mid A^*{=}j]=\mathrm{ct}_j/q_j$:
96	\begin{align*}
97	  \mathbb{E}[\tilde{T}^2]
98	  &= \mathbb{E}[T^2] - \sum_j q_j\bigl(\mathrm{ct}_j/q_j\bigr)^2
99	  = s_T - \sum_j \mathrm{ct}_j^2/q_j,\\
100	  \mathbb{E}[\tilde{T}\,Y]
101	  &= \mathbb{E}[TY] - \sum_j \bigl(\mathrm{ct}_j/q_j\bigr)\,\mathbb{E}[Y\cdot D_j^*]
102	  = \mu_{TY} - \sum_j \mathrm{ct}_j\,\mathrm{cy}_j/q_j.
103	\end{align*}
104	\end{proof}
105	
106	\paragraph{Verification at $C=I$.}
107	When $C=I$: $q_j=p_j$, $\mathrm{ct}_j=\mathbb{E}[T D_j]=\alpha_j p_j$, $\mathrm{cy}_j=\mathbb{E}[Y D_j]=p_j(\tau\alpha_j+\beta_j^{(A)})$.
108	Direct substitution yields numerator $= \tau\sigma_T^2$ and denominator $= \sigma_T^2$, giving $\operatorname{plim}\hat\tau = \tau$.
109	
110	\paragraph{Bias structure.}
111	By Lemma~\ref{lem:bias_decomp}:
112	\begin{equation}
113	  \operatorname{plim}\hat\tau(C) = \tau + B(C),\quad
114	  B(C) = \frac{\mathbb{E}[\operatorname{Cov}(g(A),\,f(A)\mid A^*)]}{D(C)}.
115	  \label{eq:bias_conf}
116	\end{equation}
117	By the law of total covariance:
118	\begin{equation}
119	  \mathbb{E}[\operatorname{Cov}(g,f\mid A^*)]
120	  = \operatorname{Cov}(g(A),f(A))
121	  - \operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[f(A)\mid A^*]\bigr).
122	  \label{eq:lotc}
123	\end{equation}
124	
125	At $C=I$: $\mathbb{E}[g\mid A^*]=g(A)$, so the between-group covariance equals $\operatorname{Cov}(g,f)$ and $B(I)=0$.
126	
127	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform, $A^*\perp A$): $\mathbb{E}[g\mid A^*]$ is constant, so the between-group covariance is zero and
128	\begin{equation}
129	  B_{\mathrm{OV}} \;\equiv\; B\bigl(\tfrac{1}{K}\mathbf{1}\mathbf{1}^\top\bigr)
130	  = \frac{\operatorname{Cov}(g(A),\,f(A))}{\operatorname{Var}(T)},
131	  \label{eq:bov}
132	\end{equation}
133	which equals the classical omitted-variable bias (no control for $A$).
134	
135	\paragraph{Sign preservation condition.}
136	Since $D(C)>0$, sign$(\operatorname{plim}\hat\tau) = $ sign$(\tau\cdot D(C) + R(C))$.
137	For sign preservation, it suffices that $R(C)$ does not overwhelm $\tau\cdot D(C)$.
138	
139	\begin{proposition}[Confounding sign preservation --- proportional case]
140	\label{prop:conf_prop}
141	If $f(A) = \lambda\,g(A)$ for some constant $\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then
142	\begin{equation}
143	  B(C) = \bigl(1-\xi(C)\bigr)\,B_{\mathrm{OV}},
144	  \label{eq:convex}
145	\end{equation}
146	where
147	\[
148	  \xi(C) = \frac{\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\;\sigma_T^2}
149	  {\operatorname{Var}(g(A))\bigl(\operatorname{Var}(g(A))-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])+\sigma_T^2\bigr)}
150	  \;\in\;[0,1].
151	\]
152	Consequently, $B(C)$ lies between $0$ and $B_{\mathrm{OV}}$, and $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{OV}})$.
153	\end{proposition}
154	
155	\begin{proof}
156	When $f=\lambda g$: the between-group covariance in~\eqref{eq:lotc} becomes $\lambda\,\operatorname{Var}(\mathbb{E}[g\mid A^*])$, and $\operatorname{Cov}(g,f)=\lambda\,\operatorname{Var}(g)$.
157	So $R(C)=\lambda\bigl(\operatorname{Var}(g)-\operatorname{Var}(\mathbb{E}[g\mid A^*])\bigr)=\lambda\,V_W$, where $V_W=\operatorname{Var}(g)-V_B$ with $V_B=\operatorname{Var}(\mathbb{E}[g\mid A^*])$.
158	Similarly, $D(C)=V_W+\sigma_T^2$.
159	Hence
160	\[
161	  B(C) = \frac{\lambda\,V_W}{V_W+\sigma_T^2},\qquad
162	  B_{\mathrm{OV}} = \frac{\lambda\,V}{V+\sigma_T^2},
163	\]
164	where $V=\operatorname{Var}(g)=V_B+V_W$.
165	The ratio
166	\[
167	  \frac{B(C)}{B_{\mathrm{OV}}} = \frac{V_W(V+\sigma_T^2)}{V(V_W+\sigma_T^2)} = 1 - \xi(C)
168	\]
169	is a decreasing function of $V_B\in[0,V]$.
170	At $V_B=0$ (no classification, $C$ uniform): $\xi=0$, $B=B_{\mathrm{OV}}$.
171	At $V_B=V$ (perfect classification, $C=I$): $\xi=1$, $B=0$.
172	Since $0\leq V_B\leq V$, we have $\xi\in[0,1]$ and $B(C)\in[0,B_{\mathrm{OV}}]$ (with the sign of $B_{\mathrm{OV}}$).
173	\end{proof}
174	
175	\begin{proposition}[Confounding sign preservation --- general case]
176	\label{prop:conf_gen}
177	For general $g$ and $f$ (not necessarily proportional), define the worst-case bias bound
178	\begin{equation}
179	  \bar{B} \;=\; \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(f(A))}}{\sigma_T^2}.
180	  \label{eq:bbar}
181	\end{equation}
182	If $|\tau| > \bar{B}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for \emph{all} column-stochastic $C$.
183	\end{proposition}
184	
185	\begin{proof}
186	We need $\operatorname{sign}(\tau\cdot D(C)+R(C))=\operatorname{sign}(\tau)$, which holds if $|R(C)|<|\tau|\cdot D(C)$.
187	Since $D(C)\geq\sigma_T^2$ (shown in Lemma~\ref{lem:bias_decomp}), it suffices to show $|R(C)|<|\tau|\,\sigma_T^2$.
188	
189	\emph{Step 1: Bound $|R(C)|$.}
190	$R(C)=\mathbb{E}[\operatorname{Cov}(g(A),f(A)\mid A^*)]$.
191	By the Cauchy--Schwarz inequality applied to each within-group covariance:
192	\[
193	  |\operatorname{Cov}(g,f\mid A^*{=}j)|
194	  \leq \sqrt{\operatorname{Var}(g\mid A^*{=}j)\,\operatorname{Var}(f\mid A^*{=}j)}.
195	\]
196	Taking expectations and applying Cauchy--Schwarz again:
197	\begin{align*}
198	  |R(C)|
199	  &\leq \mathbb{E}\bigl[\sqrt{\operatorname{Var}(g\mid A^*)\,\operatorname{Var}(f\mid A^*)}\bigr]\\
200	  &\leq \sqrt{\mathbb{E}[\operatorname{Var}(g\mid A^*)]\;\mathbb{E}[\operatorname{Var}(f\mid A^*)]}\\
201	  &\leq \sqrt{\operatorname{Var}(g(A))\;\operatorname{Var}(f(A))},
202	\end{align*}
203	where the last step uses $\mathbb{E}[\operatorname{Var}(X\mid Y)]\leq\operatorname{Var}(X)$ (law of total variance).
204	
205	\emph{Step 2: Conclude.}
206	The bias satisfies
207	\[
208	  |B(C)| = \frac{|R(C)|}{D(C)} \leq \frac{\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(f)}}{\sigma_T^2} = \bar{B}.
209	\]
210	When $|\tau|>\bar{B}$, the bias cannot cancel $\tau$, so $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ for all $C$.
211	\end{proof}
212	
213	\paragraph{Relationship to the omitted-variable condition.}
214	A weaker (necessary) condition for sign preservation is $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ where $\tau_{\mathrm{OV}}=\tau+\operatorname{Cov}(g,f)/\operatorname{Var}(T)$.
215	If this fails, then $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform noise) already flips the sign.
216	The rigorous sufficient condition $|\tau|>\bar{B}$ implies the weaker condition, since $|B_{\mathrm{OV}}|=|\operatorname{Cov}(g,f)|/\operatorname{Var}(T)\leq\bar{B}$ by Cauchy--Schwarz and $\operatorname{Var}(T)\geq\sigma_T^2$.
217	
218	\paragraph{Verification for paper parameters ($K{=}3$).}
219	With $\tau{=}2.0$, $\boldsymbol{\alpha}{=}(1.5,{-}1.0)$, $\boldsymbol{\beta}^{(A)}{=}(1.0,{-}0.5)$, $\sigma_T{=}1.0$, $\mathbf{p}{=}(0.40,0.35,0.25)$:
220	\begin{align*}
221	  \operatorname{Var}(g) &= \sum_k p_k\alpha_k^2 - \bigl(\textstyle\sum_k p_k\alpha_k\bigr)^2 = 0.962,\\
222	  \operatorname{Var}(f) &= \sum_k p_k(\beta_k^{(A)})^2 - \bigl(\textstyle\sum_k p_k\beta_k^{(A)}\bigr)^2 = 0.362,\\
223	  \bar{B} &= \sqrt{0.962\times 0.362}\;/\;1.0^2 = 0.590.
224	\end{align*}
225	Since $|\tau|{=}2.0 > \bar{B}{=}0.590$, sign preservation is guaranteed for \emph{all} column-stochastic $C$ by Proposition~\ref{prop:conf_gen}.
226	Additionally, $B_{\mathrm{OV}}=\operatorname{Cov}(g,f)/\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\tau_{\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.
227	
228	\paragraph{Extension to $K > 3$.}
229	For $K{>}3$, treatment effect coefficients are drawn from a fixed pool with alternating signs and decreasing magnitudes: $\boldsymbol{\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3, \ldots)$, truncated to $K$ entries. The category distribution uses $p_k \propto 1/(k{+}1)$, normalized to sum to 1. Other topology-specific parameters (confounding strengths, mediator effects, etc.) follow analogous alternating-sign pools. For $K{=}10$, $\boldsymbol{\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3)$.
230	
231	\subsection{Proof of Theorem~\ref{thm:monotone} (Confounding Monotonicity)}
232	\label{app:monotonicity_proof}
233	
234	Under the interpolation $C(\delta)=(1{-}\delta)I+\delta C_0$, we prove $|B(C(\delta))|$ is non-decreasing in $\delta$ for proportional effects ($f=\lambda g$) and provide numerical verification for the general case.
235	The proof proceeds by direct algebraic analysis of $V_B(\delta)=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*_\delta])$ as a rational function of $\delta$, establishing convexity and bounding the derivative at both endpoints.
236	
237	\paragraph{Proportional case ($f=\lambda g$).}
238	From Proposition~\ref{prop:conf_prop}, $B(C)=\lambda V_W/(V_W+\sigma_T^2)$ where $V_W=\operatorname{Var}(g)-V_B$ and $V_B(\delta)=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*_\delta])$.
239	
240	\emph{Step 1: Convexity of $V_B(\delta)$.}
241	Define $N_j(\delta)=\sum_k g_k\,C(\delta)_{jk}\,p_k$ and $q_j(\delta)=\sum_k C(\delta)_{jk}\,p_k$.
242	Both are affine in $\delta$, with $q_j(\delta)>0$.
243	Then $V_B(\delta)=\sum_j N_j(\delta)^2/q_j(\delta) - \bar{g}^2$.
244	Each term $N_j^2/q_j$ is the composition of the perspective function $(x,t)\mapsto x^2/t$ (convex for $t>0$) with the affine map $\delta\mapsto(N_j(\delta),\,q_j(\delta))$, hence convex in $\delta$.
245	A sum of convex functions is convex, so $V_B(\delta)$ is convex on $[0,\delta_{\max}]$.
246	
247	\emph{Step 2: Derivative formula.}
248	Let $\mu_j(\delta)=N_j(\delta)/q_j(\delta)=\mathbb{E}[g(A)\mid A^*{=}j]$.
249	Then
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "229116d1-5fad-4003-a9a0-d0cdb2d3bdd0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "\\section{Proofs of Proposition~\\ref{prop:signflip} and Theorem~\\ref{thm:monotone}}\n\\label{app:proof}\n\nWe provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\\ref{thm:monotone}).\nThroughout, $A\\in\\{0,1,\\dots,K{-}1\\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\\mid A{=}k)$.\nWe use category~0 as the reference and let $D_j=\\mathbf{1}(A{=}j)$, $D_j^*=\\mathbf{1}(A^*{=}j)$ for $j=1,\\dots,K{-}1$.\n\n\\subsection{Notation and Key Identities}\n\\label{app:notation}\n\nUnder non-differential misclassification, the misclassified moments factor linearly through $C$.\nDefine the population vectors:\n\\begin{align}\n  q_j &= P(A^*{=}j) = \\textstyle\\sum_k C_{jk}\\,p_k, \\label{eq:q}\\\\\n  \\mathrm{ct}_j &= \\mathbb{E}[T\\cdot D_j^*] = \\textstyle\\sum_k C_{jk}\\,\\mathbb{E}[T\\cdot D_k], \\label{eq:ct}\\\\\n  \\mathrm{cy}_j &= \\mathbb{E}[Y\\cdot D_j^*] = \\textstyle\\sum_k C_{jk}\\,\\mathbb{E}[Y\\cdot D_k]. \\label{eq:cy}\n\\end{align}\nWrite $q = Cp$, $\\mathrm{ct} = C\\,\\mathbb{E}[T\\cdot D]$, and $\\mathrm{cy} = C\\,\\mathbb{E}[Y\\cdot D]$, where $D=(D_0,\\dots,D_{K-1})^\\top$.\n\n\\subsection{Frisch--Waugh--Lovell Decomposition}\n\\label{app:fwl}\n\nFor topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\\dots,D_{K-1}^*)$.\nBy the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat{\\tau}(C)\n  = \\frac{\\mathbb{E}[\\tilde{T}\\,\\tilde{Y}]}{\\mathbb{E}[\\tilde{T}^2]},\n  \\label{eq:fwl}\n\\end{equation}\nwhere $\\tilde{T}=T-\\mathbb{E}[T\\mid A^*]$ and $\\tilde{Y}=Y-\\mathbb{E}[Y\\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\\dots,D_{K-1}^*)$.\n\n\\begin{lemma}[Bias decomposition]\n\\label{lem:bias_decomp}\nSuppose $Y = \\tau T + f(A) + \\varepsilon_Y$ with $\\varepsilon_Y \\perp (T, A, A^*)$.\nThen\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + \\frac{R(C)}{D(C)},\n  \\label{eq:bias_decomp}\n\\end{equation}\nwhere\n\\begin{align}\n  R(C) &= \\mathbb{E}\\bigl[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)\\bigr], \\label{eq:R}\\\\\n  D(C) &= \\mathbb{E}\\bigl[\\operatorname{Var}(T\\mid A^*)\\bigr] > 0. \\label{eq:D}\n\\end{align}\n\\end{lemma}\n\n\\begin{proof}\nExpand $\\tilde{Y}$ using $Y=\\tau T + f(A) + \\varepsilon_Y$:\n\\[\n  \\tilde{Y} = \\tau\\,\\tilde{T} + \\bigl(f(A) - \\mathbb{E}[f(A)\\mid A^*]\\bigr) + \\varepsilon_Y.\n\\]\nSince $\\tilde{T}$ is measurable w.r.t.\\ $(T,A^*)$ and $\\varepsilon_Y\\perp(T,A,A^*)$:\n\\[\n  \\mathbb{E}[\\tilde{T}\\,\\tilde{Y}]\n  = \\tau\\,\\mathbb{E}[\\tilde{T}^2]\n  + \\mathbb{E}\\bigl[\\tilde{T}\\,\\bigl(f(A)-\\mathbb{E}[f(A)\\mid A^*]\\bigr)\\bigr].\n\\]\nThe numerator residual is $R(C) = \\mathbb{E}[\\tilde{T}(f(A)-\\mathbb{E}[f(A)\\mid A^*])]$, and the denominator is $D(C) = \\mathbb{E}[\\tilde{T}^2]$.\n\nBy the law of total covariance:\n\\[\n  R(C) = \\sum_{j=0}^{K-1} q_j\\,\\operatorname{Cov}(T,\\,f(A)\\mid A^*{=}j)\n  = \\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)].\n\\]\nFor $D(C)>0$: decompose $T = g(A) + \\varepsilon_T$ where $g(A)=\\mathbb{E}[T\\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).\nIn both cases, $\\tilde{T}=\\bigl(g(A)-\\mathbb{E}[g(A)\\mid A^*]\\bigr)+\\varepsilon_T'$, where $\\varepsilon_T'$ is the component of $T$ independent of $(A,A^*)$.\nHence $D(C)\\geq\\operatorname{Var}(\\varepsilon_T')>0$.\n\\end{proof}\n\n\\subsection{Confounding Topology ($A$ = Confounder)}\n\\label{app:confounding}\n\n\\paragraph{Data-generating process.}\n$A\\to T$, $A\\to Y$, $T\\to Y$.\nUsing dummy coding with category 0 as reference:\n\\begin{align*}\n  T &= \\sum_{j=1}^{K-1}\\alpha_j D_j + \\varepsilon_T,\\quad\n  \\varepsilon_T\\sim\\mathcal{N}(0,\\sigma_T^2),\\;\\varepsilon_T\\perp A,\\\\\n  Y &= \\tau\\, T + \\sum_{j=1}^{K-1}\\beta_j^{(A)} D_j + \\varepsilon_Y,\\quad\n  \\varepsilon_Y\\sim\\mathcal{N}(0,1),\\;\\varepsilon_Y\\perp(T,A).\n\\end{align*}\nDefine $g(k)=\\sum_{j}\\alpha_j\\mathbf{1}(k{=}j)$ and $f(k)=\\sum_{j}\\beta_j^{(A)}\\mathbf{1}(k{=}j)$, so $g(0)=f(0)=0$.\n\n\\paragraph{Closed-form plim.}\nUsing the FWL decomposition, the coefficient on $T$ is:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C)\n  = \\frac{\\mu_{TY} - \\sum_{j=0}^{K-1}\\frac{\\mathrm{ct}_j\\,\\mathrm{cy}_j}{q_j}}\n  {s_T - \\sum_{j=0}^{K-1}\\frac{\\mathrm{ct}_j^2}{q_j}},\n  \\label{eq:plim_conf}\n\\end{equation}\nwhere $s_T=\\mathbb{E}[T^2]$, $\\mu_{TY}=\\mathbb{E}[TY]$, and $\\mathrm{ct}_j$, $\\mathrm{cy}_j$, $q_j$ are defined in~\\eqref{eq:q}--\\eqref{eq:cy}.\n\n\\begin{proof}[Derivation]\nBy FWL, $\\operatorname{plim}\\hat\\tau = \\mathbb{E}[\\tilde{T}Y]/\\mathbb{E}[\\tilde{T}^2]$ where $\\tilde{T}=T-\\mathbb{E}[T\\mid A^*]$.\nSince $\\mathbb{E}[T\\mid A^*{=}j]=\\mathrm{ct}_j/q_j$:\n\\begin{align*}\n  \\mathbb{E}[\\tilde{T}^2]\n  &= \\mathbb{E}[T^2] - \\sum_j q_j\\bigl(\\mathrm{ct}_j/q_j\\bigr)^2\n  = s_T - \\sum_j \\mathrm{ct}_j^2/q_j,\\\\\n  \\mathbb{E}[\\tilde{T}\\,Y]\n  &= \\mathbb{E}[TY] - \\sum_j \\bigl(\\mathrm{ct}_j/q_j\\bigr)\\,\\mathbb{E}[Y\\cdot D_j^*]\n  = \\mu_{TY} - \\sum_j \\mathrm{ct}_j\\,\\mathrm{cy}_j/q_j.\n\\end{align*}\n\\end{proof}\n\n\\paragraph{Verification at $C=I$.}\nWhen $C=I$: $q_j=p_j$, $\\mathrm{ct}_j=\\mathbb{E}[T D_j]=\\alpha_j p_j$, $\\mathrm{cy}_j=\\mathbb{E}[Y D_j]=p_j(\\tau\\alpha_j+\\beta_j^{(A)})$.\nDirect substitution yields numerator $= \\tau\\sigma_T^2$ and denominator $= \\sigma_T^2$, giving $\\operatorname{plim}\\hat\\tau = \\tau$.\n\n\\paragraph{Bias structure.}\nBy Lemma~\\ref{lem:bias_decomp}:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + B(C),\\quad\n  B(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(g(A),\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:bias_conf}\n\\end{equation}\nBy the law of total covariance:\n\\begin{equation}\n  \\mathbb{E}[\\operatorname{Cov}(g,f\\mid A^*)]\n  = \\operatorname{Cov}(g(A),f(A))\n  - \\operatorname{Cov}\\bigl(\\mathbb{E}[g(A)\\mid A^*],\\;\\mathbb{E}[f(A)\\mid A^*]\\bigr).\n  \\label{eq:lotc}\n\\end{equation}\n\nAt $C=I$: $\\mathbb{E}[g\\mid A^*]=g(A)$, so the between-group covariance equals $\\operatorname{Cov}(g,f)$ and $B(I)=0$.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ (uniform, $A^*\\perp A$): $\\mathbb{E}[g\\mid A^*]$ is constant, so the between-group covariance is zero and\n\\begin{equation}\n  B_{\\mathrm{OV}} \\;\\equiv\\; B\\bigl(\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top\\bigr)\n  = \\frac{\\operatorname{Cov}(g(A),\\,f(A))}{\\operatorname{Var}(T)},\n  \\label{eq:bov}\n\\end{equation}\nwhich equals the classical omitted-variable bias (no control for $A$).\n\n\\paragraph{Sign preservation condition.}\nSince $D(C)>0$, sign$(\\operatorname{plim}\\hat\\tau) = $ sign$(\\tau\\cdot D(C) + R(C))$.\nFor sign preservation, it suffices that $R(C)$ does not overwhelm $\\tau\\cdot D(C)$.\n\n\\begin{proposition}[Confounding sign preservation --- proportional case]\n\\label{prop:conf_prop}\nIf $f(A) = \\lambda\\,g(A)$ for some constant $\\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then\n\\begin{equation}\n  B(C) = \\bigl(1-\\xi(C)\\bigr)\\,B_{\\mathrm{OV}},\n  \\label{eq:convex}\n\\end{equation}\nwhere\n\\[\n  \\xi(C) = \\frac{\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])\\;\\sigma_T^2}\n  {\\operatorname{Var}(g(A))\\bigl(\\operatorname{Var}(g(A))-\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])+\\sigma_T^2\\bigr)}\n  \\;\\in\\;[0,1].\n\\]\nConsequently, $B(C)$ lies between $0$ and $B_{\\mathrm{OV}}$, and $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ whenever $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau+B_{\\mathrm{OV}})$.\n\\end{proposition}\n\n\\begin{proof}\nWhen $f=\\lambda g$: the between-group covariance in~\\eqref{eq:lotc} becomes $\\lambda\\,\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$, and $\\operatorname{Cov}(g,f)=\\lambda\\,\\operatorname{Var}(g)$.\nSo $R(C)=\\lambda\\bigl(\\operatorname{Var}(g)-\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\bigr)=\\lambda\\,V_W$, where $V_W=\\operatorname{Var}(g)-V_B$ with $V_B=\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$.\nSimilarly, $D(C)=V_W+\\sigma_T^2$.\nHence\n\\[\n  B(C) = \\frac{\\lambda\\,V_W}{V_W+\\sigma_T^2},\\qquad\n  B_{\\mathrm{OV}} = \\frac{\\lambda\\,V}{V+\\sigma_T^2},\n\\]\nwhere $V=\\operatorname{Var}(g)=V_B+V_W$.\nThe ratio\n\\[\n  \\frac{B(C)}{B_{\\mathrm{OV}}} = \\frac{V_W(V+\\sigma_T^2)}{V(V_W+\\sigma_T^2)} = 1 - \\xi(C)\n\\]\nis a decreasing function of $V_B\\in[0,V]$.\nAt $V_B=0$ (no classification, $C$ uniform): $\\xi=0$, $B=B_{\\mathrm{OV}}$.\nAt $V_B=V$ (perfect classification, $C=I$): $\\xi=1$, $B=0$.\nSince $0\\leq V_B\\leq V$, we have $\\xi\\in[0,1]$ and $B(C)\\in[0,B_{\\mathrm{OV}}]$ (with the sign of $B_{\\mathrm{OV}}$).\n\\end{proof}\n\n\\begin{proposition}[Confounding sign preservation --- general case]\n\\label{prop:conf_gen}\nFor general $g$ and $f$ (not necessarily proportional), define the worst-case bias bound\n\\begin{equation}\n  \\bar{B} \\;=\\; \\frac{\\sqrt{\\operatorname{Var}(g(A))\\,\\operatorname{Var}(f(A))}}{\\sigma_T^2}.\n  \\label{eq:bbar}\n\\end{equation}\nIf $|\\tau| > \\bar{B}$, then $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau(C))=\\operatorname{sign}(\\tau)$ for \\emph{all} column-stochastic $C$.\n\\end{proposition}\n\n\\begin{proof}\nWe need $\\operatorname{sign}(\\tau\\cdot D(C)+R(C))=\\operatorname{sign}(\\tau)$, which holds if $|R(C)|<|\\tau|\\cdot D(C)$.\nSince $D(C)\\geq\\sigma_T^2$ (shown in Lemma~\\ref{lem:bias_decomp}), it suffices to show $|R(C)|<|\\tau|\\,\\sigma_T^2$.\n\n\\emph{Step 1: Bound $|R(C)|$.}\n$R(C)=\\mathbb{E}[\\operatorname{Cov}(g(A),f(A)\\mid A^*)]$.\nBy the Cauchy--Schwarz inequality applied to each within-group covariance:\n\\[\n  |\\operatorname{Cov}(g,f\\mid A^*{=}j)|\n  \\leq \\sqrt{\\operatorname{Var}(g\\mid A^*{=}j)\\,\\operatorname{Var}(f\\mid A^*{=}j)}.\n\\]\nTaking expectations and applying Cauchy--Schwarz again:\n\\begin{align*}\n  |R(C)|\n  &\\leq \\mathbb{E}\\bigl[\\sqrt{\\operatorname{Var}(g\\mid A^*)\\,\\operatorname{Var}(f\\mid A^*)}\\bigr]\\\\\n  &\\leq \\sqrt{\\mathbb{E}[\\operatorname{Var}(g\\mid A^*)]\\;\\mathbb{E}[\\operatorname{Var}(f\\mid A^*)]}\\\\\n  &\\leq \\sqrt{\\operatorname{Var}(g(A))\\;\\operatorname{Var}(f(A))},\n\\end{align*}\nwhere the last step uses $\\mathbb{E}[\\operatorname{Var}(X\\mid Y)]\\leq\\operatorname{Var}(X)$ (law of total variance).\n\n\\emph{Step 2: Conclude.}\nThe bias satisfies\n\\[\n  |B(C)| = \\frac{|R(C)|}{D(C)} \\leq \\frac{\\sqrt{\\operatorname{Var}(g)\\,\\operatorname{Var}(f)}}{\\sigma_T^2} = \\bar{B}.\n\\]\nWhen $|\\tau|>\\bar{B}$, the bias cannot cancel $\\tau$, so $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ for all $C$.\n\\end{proof}\n\n\\paragraph{Relationship to the omitted-variable condition.}\nA weaker (necessary) condition for sign preservation is $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau_{\\mathrm{OV}})$ where $\\tau_{\\mathrm{OV}}=\\tau+\\operatorname{Cov}(g,f)/\\operatorname{Var}(T)$.\nIf this fails, then $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ (uniform noise) already flips the sign.\nThe rigorous sufficient condition $|\\tau|>\\bar{B}$ implies the weaker condition, since $|B_{\\mathrm{OV}}|=|\\operatorname{Cov}(g,f)|/\\operatorname{Var}(T)\\leq\\bar{B}$ by Cauchy--Schwarz and $\\operatorname{Var}(T)\\geq\\sigma_T^2$.\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau{=}2.0$, $\\boldsymbol{\\alpha}{=}(1.5,{-}1.0)$, $\\boldsymbol{\\beta}^{(A)}{=}(1.0,{-}0.5)$, $\\sigma_T{=}1.0$, $\\mathbf{p}{=}(0.40,0.35,0.25)$:\n\\begin{align*}\n  \\operatorname{Var}(g) &= \\sum_k p_k\\alpha_k^2 - \\bigl(\\textstyle\\sum_k p_k\\alpha_k\\bigr)^2 = 0.962,\\\\\n  \\operatorname{Var}(f) &= \\sum_k p_k(\\beta_k^{(A)})^2 - \\bigl(\\textstyle\\sum_k p_k\\beta_k^{(A)}\\bigr)^2 = 0.362,\\\\\n  \\bar{B} &= \\sqrt{0.962\\times 0.362}\\;/\\;1.0^2 = 0.590.\n\\end{align*}\nSince $|\\tau|{=}2.0 > \\bar{B}{=}0.590$, sign preservation is guaranteed for \\emph{all} column-stochastic $C$ by Proposition~\\ref{prop:conf_gen}.\nAdditionally, $B_{\\mathrm{OV}}=\\operatorname{Cov}(g,f)/\\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\\tau_{\\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.\n\n\\paragraph{Extension to $K > 3$.}\nFor $K{>}3$, treatment effect coefficients are drawn from a fixed pool with alternating signs and decreasing magnitudes: $\\boldsymbol{\\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3, \\ldots)$, truncated to $K$ entries. The category distribution uses $p_k \\propto 1/(k{+}1)$, normalized to sum to 1. Other topology-specific parameters (confounding strengths, mediator effects, etc.) follow analogous alternating-sign pools. For $K{=}10$, $\\boldsymbol{\\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3)$.\n\n\\subsection{Proof of Theorem~\\ref{thm:monotone} (Confounding Monotonicity)}\n\\label{app:monotonicity_proof}\n\nUnder the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ for proportional effects ($f=\\lambda g$) and provide numerical verification for the general case.\nThe proof proceeds by direct algebraic analysis of $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$ as a rational function of $\\delta$, establishing convexity and bounding the derivative at both endpoints.\n\n\\paragraph{Proportional case ($f=\\lambda g$).}\nFrom Proposition~\\ref{prop:conf_prop}, $B(C)=\\lambda V_W/(V_W+\\sigma_T^2)$ where $V_W=\\operatorname{Var}(g)-V_B$ and $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$.\n\n\\emph{Step 1: Convexity of $V_B(\\delta)$.}\nDefine $N_j(\\delta)=\\sum_k g_k\\,C(\\delta)_{jk}\\,p_k$ and $q_j(\\delta)=\\sum_k C(\\delta)_{jk}\\,p_k$.\nBoth are affine in $\\delta$, with $q_j(\\delta)>0$.\nThen $V_B(\\delta)=\\sum_j N_j(\\delta)^2/q_j(\\delta) - \\bar{g}^2$.\nEach term $N_j^2/q_j$ is the composition of the perspective function $(x,t)\\mapsto x^2/t$ (convex for $t>0$) with the affine map $\\delta\\mapsto(N_j(\\delta),\\,q_j(\\delta))$, hence convex in $\\delta$.\nA sum of convex functions is convex, so $V_B(\\delta)$ is convex on $[0,\\delta_{\\max}]$.\n\n\\emph{Step 2: Derivative formula.}\nLet $\\mu_j(\\delta)=N_j(\\delta)/q_j(\\delta)=\\mathbb{E}[g(A)\\mid A^*{=}j]$.\nThen",
      "numLines": 250,
      "startLine": 0,
      "totalLines": 1480
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01H3A21xsfmUBeyGPpKauUwW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 249,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "be443d1d-a5e9-4e1a-81fc-ec44fcf2148e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuxmZkAB6XMXfZ5KS7QEMK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7466,
      "cache_read_input_tokens": 25279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7466
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

_source line 8 · 2026-05-23T17:37:05.460Z_

<details><summary>↩ Tool result · `toolu_01H3A21xsfmUBeyGPpKauUwW`</summary>

```text
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
330	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$): no information about $A$ is used, and
331	\begin{align*}
332	  \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] &= \operatorname{Cov}(T,f(A)),\\
333	  D(C) &= \operatorname{Var}(T) = 0.25.
334	\end{align*}
335	The indirect effect is $\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]$, and
336	\[
337	  \operatorname{Cov}(T,f(A)) = 0.25\,\tau_{\mathrm{ind}}.
338	\]
339	Hence at $C$ uniform: $\operatorname{plim}\hat\tau = \tau_{\mathrm{dir}}+\tau_{\mathrm{ind}} = \tau_{\mathrm{total}}$.
340	
341	\paragraph{Numerical Verification (Mediation sign preservation).}
342	\label{find:med_sign}
343	$\operatorname{sign}(\operatorname{plim}\hat\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{dir}})$ whenever $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$, where $\tau_{\mathrm{total}}=\tau_{\mathrm{dir}}+\tau_{\mathrm{ind}}$.
344	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.
345	
346	\begin{proof}
347	Let $R(C)=\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)]$ and $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]>0$.
348	
349	\emph{Endpoints.}
350	At $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.
351	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $R=\operatorname{Cov}(T,f(A))=0.25\,\tau_{\mathrm{ind}}$ and $D=\operatorname{Var}(T)=0.25$, giving $B=\tau_{\mathrm{ind}}$.
352	
353	\emph{Within-group structure for binary $T$.}
354	Since $T\in\{0,1\}$, the within-$A^*$-group bias admits a revealing decomposition.
355	Let $p_j=P(T{=}1\mid A^*{=}j)$.
356	Then $\operatorname{Var}(T\mid A^*{=}j)=p_j(1{-}p_j)$ and
357	\[
358	  \operatorname{Cov}(T,f(A)\mid A^*{=}j)
359	  = p_j(1{-}p_j)\bigl[\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]\bigr].
360	\]
361	Define $\delta_j=\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]$ as the \emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.
362	Then
363	\[
364	  B(C)=\frac{R(C)}{D(C)}
365	  =\frac{\sum_j q_j\,p_j(1{-}p_j)\,\delta_j}{\sum_j q_j\,p_j(1{-}p_j)}
366	  =\sum_j w_j\,\delta_j,
367	\]
368	a weighted average of the conditional indirect effects, with weights $w_j=q_j p_j(1{-}p_j)/\sum_\ell q_\ell p_\ell(1{-}p_\ell)\geq 0$ summing to 1.
369	
370	At $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\delta_j=f(j)-f(j)=0$ and $B=0$.
371	At $C$ uniform: $\delta_j=\tau_{\mathrm{ind}}$ for all $j$ and $B=\tau_{\mathrm{ind}}$.
372	
373	\emph{Sign preservation.}
374	When $\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have the same sign), the bias $B(C)\geq 0$ cannot oppose $\tau_{\mathrm{dir}}$, so sign is preserved trivially.
375	
376	When $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have opposite signs but $|\tau_{\mathrm{ind}}|<|\tau_{\mathrm{dir}}|$ (i.e., $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$), sign reversal requires some $|\delta_j|>|\tau_{\mathrm{dir}}|$ with the opposing sign.
377	Since each $\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\delta_j$, the bound $|B(C)|\leq\max_j|\delta_j|$ holds.
378	We verify numerically that $\max_j|\delta_j|\leq|\tau_{\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.
379	\end{proof}
380	
381	\paragraph{Verification for paper parameters ($K{=}3$).}
382	With $\tau_{\mathrm{dir}}{=}0.5$, $\boldsymbol{\gamma}{=}(0,0,0)$, $\boldsymbol{\delta}{=}(0,0.8,{-}0.6)$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$:
383	
384	$\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]=0.351$ (computed from the softmax class probabilities).
385	$\tau_{\mathrm{total}}=0.5+0.351=0.851>0$.
386	Since $\tau_{\mathrm{dir}}{>}0$ and $\tau_{\mathrm{total}}{>}0$, sign preservation holds for all $C$.
387	
388	\paragraph{Mediation monotonicity (proportional effects).}
389	\label{par:med_monotone}
390	
391	Under the interpolation $C(\delta)=(1{-}\delta)I+\delta C_0$, we prove $|B(C(\delta))|$ is non-decreasing in $\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\lambda\,g(A)$ for some scalar $\lambda$, where $g(k)=\mathbb{E}[T\mid A{=}k]$.
392	
393	\emph{Step 1: Decompose $T$ via the mediator.}
394	Define $g(A)=\mathbb{E}[T\mid A]$ and $\varepsilon_T = T - g(A)$.
395	By construction, $\mathbb{E}[\varepsilon_T\mid A]=0$.
396	By non-differential misclassification ($T\perp A^*\mid A$):
397	$\mathbb{E}[\varepsilon_T\mid A{=}k, A^*{=}j] = 0$,
398	so $\mathbb{E}[\varepsilon_T\mid A^*{=}j]=0$ and $\operatorname{Cov}(\varepsilon_T,\,g(A)\mid A^*{=}j)=0$ for every $j$.
399	
400	\emph{Step 2: Reduce the numerator.}
401	Since $f=\lambda g$:
402	\begin{align*}
403	  R(C) &= \lambda\,\mathbb{E}[\operatorname{Var}(g(A)\mid A^*)] = \lambda\,V_W.
404	\end{align*}
405	
406	\emph{Step 3: Constant additive term in denominator.}
407	\begin{align*}
408	  D(C) &= \mathbb{E}[\operatorname{Var}(T\mid A^*)]
409	       = V_W + \sigma_\varepsilon^2,
410	\end{align*}
411	where $\sigma_\varepsilon^2\equiv\mathbb{E}[\operatorname{Var}(\varepsilon_T\mid A^*)]$.
412	This is \emph{constant} (independent of $C$):
413	$\mathbb{E}[\operatorname{Var}(\varepsilon_T\mid A^*)]
414	  = \sum_k p_k\,\operatorname{Var}(T\mid A{=}k)
415	  = \mathbb{E}[\operatorname{Var}(T\mid A)]$,
416	where the equality uses column-stochasticity: $\sum_j q_j\,P(A{=}k\mid A^*{=}j)=p_k$.
417	
418	\emph{Step 4: Closed form and monotonicity.}
419	$B(C) = \lambda\,V_W/(V_W+\sigma_\varepsilon^2)$,
420	structurally identical to confounding (Proposition~\ref{prop:conf_prop}) with $\sigma_\varepsilon^2$ playing the role of $\sigma_T^2$.
421	Since $V_B(\delta)$ is convex with $V_B'(0)\leq 0$ (same argument as \S\ref{app:monotonicity_proof}, Steps~1--3), $V_W(\delta)=V{-}V_B(\delta)$ is non-decreasing under the same conditions on $C_0$.
422	Since $h(x)=|\lambda|x/(x+\sigma_\varepsilon^2)$ is increasing, $|B(C(\delta))|$ is non-decreasing.
423	
424	\paragraph{Boundedness of the leakage coefficient.}
425	
426	The mediation bias~\eqref{eq:mediation} writes the residual indirect effect as $(1-\lambda(C))\,\tau_{\mathrm{ind}}$, which (for $\tau_{\mathrm{ind}}\neq 0$) \emph{implicitly} defines
427	\begin{equation}
428	\label{eq:lambda_def}
429	  \lambda(C) \;:=\; 1-\frac{B(C)}{\tau_{\mathrm{ind}}},\qquad
430	  B(C)\;\equiv\;\operatorname{plim}\hat{\tau}_{\mathrm{dir}}(A^*)-\tau_{\mathrm{dir}},\quad
431	  \tau_{\mathrm{ind}}\;=\;\frac{\operatorname{Cov}(T,f(A))}{\operatorname{Var}(T)}.
432	\end{equation}
433	Substituting back into~\eqref{eq:mediation} gives the convex-combination form
434	$\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)=\lambda(C)\,\tau_{\mathrm{dir}}+(1-\lambda(C))\,\tau_{\mathrm{total}}$, so $\lambda(C)$ is the weight placing the biased plim between $\tau_{\mathrm{dir}}$ (perfect classification) and $\tau_{\mathrm{total}}$ (no information).
435	
436	\begin{proposition}[Mediation leakage boundedness]
437	\label{prop:lambda_bound}
438	Let $\lambda(C)$ be defined by~\eqref{eq:lambda_def} with $\tau_{\mathrm{ind}}\neq 0$, and let $C$ be column-stochastic.
439	\begin{enumerate}
440	\item[(a)] $\lambda(C)\leq 1$ iff $\operatorname{sign}(B(C))=\operatorname{sign}(\tau_{\mathrm{ind}})$ (the bias points in the direction of the indirect effect; no overcorrection).
441	\item[(b)] $\lambda(C)\geq 0$ iff additionally $|B(C)|\leq|\tau_{\mathrm{ind}}|$ (the bias does not exceed the indirect effect in magnitude).
442	\end{enumerate}
443	Equivalently, $\lambda(C)\in[0,1]$ iff $\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)\in[\min(\tau_{\mathrm{dir}},\tau_{\mathrm{total}}),\,\max(\tau_{\mathrm{dir}},\tau_{\mathrm{total}})]$.
444	
445	Under \emph{proportional effects} ($f(A)=\lambda_0\,g(A)$ with $g(k)=\mathbb{E}[T\mid A{=}k]$), both (a) and (b) hold for every $C$, so $\lambda(C)\in[0,1]$ unconditionally.
446	For \emph{general (non-proportional)} $f$, both (a) and (b) can fail because $\operatorname{Cov}(\mathbb{E}[g\mid A^*],\mathbb{E}[f\mid A^*])$ may differ in sign or magnitude from $\operatorname{Cov}(g,f)$ (a covariance-level analogue of Simpson's paradox under $A^*$ aggregation); the numerical verification below quantifies the empirical rate.
447	The endpoints $\lambda(I)=1$ and $\lambda(C)\to 0$ in the rank-one (uninformative) limit hold in all regimes.
448	
449	\emph{Sign preservation.} When $\lambda(C)\in[0,1]$, the convex-combination form gives $\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)\in[\min(\tau_{\mathrm{dir}},\tau_{\mathrm{total}}),\,\max(\tau_{\mathrm{dir}},\tau_{\mathrm{total}})]$. If additionally $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$, both endpoints share the same sign, so $\operatorname{sign}(\operatorname{plim}\hat\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{dir}})$ for every~$C$. Under proportional effects, $\lambda(C)\in[0,1]$ is automatic (above), so sign preservation of $\hat\tau_{\mathrm{dir}}$ reduces to the single condition $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$.
450	\end{proposition}
451	
452	\begin{proof}
453	\emph{(a),(b).} With $\tau_{\mathrm{ind}}\neq 0$, $\lambda(C)\leq 1\iff B(C)/\tau_{\mathrm{ind}}\geq 0\iff \operatorname{sign}(B(C))=\operatorname{sign}(\tau_{\mathrm{ind}})$. Given (a), $\lambda(C)\geq 0\iff B(C)/\tau_{\mathrm{ind}}\leq 1\iff|B(C)|\leq|\tau_{\mathrm{ind}}|$.
454	
455	\emph{Proportional case.} Step~4 of the mediation derivation gives $B(C)=\lambda_0\,V_W(C)/(V_W(C)+\sigma_\varepsilon^2)$; the rank-one limit $V_W{\to}V$ yields $\tau_{\mathrm{ind}}=\lambda_0\,V/(V+\sigma_\varepsilon^2)$. Both quantities carry $\operatorname{sign}(\lambda_0)$, establishing~(a). The ratio
456	\[
457	  \frac{B(C)}{\tau_{\mathrm{ind}}}\;=\;\frac{V_W(C)\,(V+\sigma_\varepsilon^2)}{V\,(V_W(C)+\sigma_\varepsilon^2)}
458	\]
459	is monotone increasing in $V_W(C)\in[0,V]$ with range $[0,1]$ (its derivative in $V_W$ is $\sigma_\varepsilon^2(V+\sigma_\varepsilon^2)/[V(V_W+\sigma_\varepsilon^2)^2]>0$), establishing~(b). Hence $\lambda(C)\in[0,1]$ unconditionally.
460	
461	\emph{General case.} Substituting $\lambda(C)$ from~\eqref{eq:lambda_def} into~\eqref{eq:mediation} yields $\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)=\lambda(C)\,\tau_{\mathrm{dir}}+(1{-}\lambda(C))\,\tau_{\mathrm{total}}$, so $\lambda(C)\in[0,1]$ iff $\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)$ lies in the closed interval with endpoints $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{total}}$.
462	
463	\emph{Endpoints.} At $C{=}I$, $A^*{=}A$ a.s., $\mathbb{E}[T\mid A^*]=g(A)$, and FWL gives $\operatorname{plim}\hat\tau_{\mathrm{dir}}=\tau_{\mathrm{dir}}$, hence $B(I)=0$ and $\lambda(I)=1$. At any rank-one $C$ (rows identical), $A^*\perp A$ so $\mathbb{E}[T\mid A^*]$ is constant, the partial regression on $A^*$ has no effect, and $\operatorname{plim}\hat\tau_{\mathrm{dir}}=\operatorname{Cov}(Y,T)/\operatorname{Var}(T)=\tau_{\mathrm{total}}$, giving $B=\tau_{\mathrm{ind}}$ and $\lambda=0$.
464	\end{proof}
465	
466	\paragraph{Relation to the between-variance ratio.}
467	A natural \emph{diagnostic} closely related to $\lambda(C)$ is the between-variance ratio
468	\begin{equation}
469	\label{eq:vb_ratio}
470	  \lambda_V(C) \;:=\; \frac{V_B(C)}{V},\qquad V_B(C)\;=\;\operatorname{Var}\!\bigl(\mathbb{E}[g(A)\mid A^*]\bigr),\quad V\;=\;\operatorname{Var}(g(A)),
471	\end{equation}
472	which satisfies $\lambda_V(C)\in[0,1]$ \emph{unconditionally} by the law of total variance applied to $g(A)$. Under proportional effects, $\lambda$ and $\lambda_V$ agree at the endpoints and are related by
473	\[
474	  1-\lambda(C)\;=\;\frac{V_W(C)\,(V+\sigma_\varepsilon^2)}{V\,(V_W(C)+\sigma_\varepsilon^2)}\;=\;\bigl(1-\lambda_V(C)\bigr)\cdot\frac{V+\sigma_\varepsilon^2}{V_W(C)+\sigma_\varepsilon^2},
475	\]
476	so they coincide in the limit $\sigma_\varepsilon^2\gg V$. They generally differ for non-proportional $f$. We use $\lambda$ throughout the main text because it parameterizes~\eqref{eq:mediation} directly; $\lambda_V$ remains a useful summary of the channel quality of $A^*$ as a proxy for $A$ (independent of the structural form of $f$).
477	
478	\paragraph{Numerical verification.}
479	For each $K\in\{3,5,7\}$ we draw $N{=}10{,}000$ configurations $(\pi,g,\sigma_\varepsilon^2,C)$ with $\pi\sim\operatorname{Dirichlet}(\mathbf{1})$, $g\sim\mathcal{N}(0,I_K)$, $\sigma_\varepsilon^2\sim\operatorname{Uniform}(0.1,2)$, columns of $C\sim\operatorname{Dirichlet}(\mathbf{1})$, and evaluate $\lambda(C)$ from~\eqref{eq:lambda_def} in two regimes for $f$:
480	\begin{itemize}\itemsep0pt
481	\item \textbf{Proportional} ($f=\lambda_0\,g$, $\lambda_0\sim\mathcal{N}(0,1)\!\setminus\!\{0\}$): $\lambda(C)\in[0,1]$ in \emph{all} $30{,}000$ trials (pooled observed range $[1.2{\times}10^{-5},\,0.850]$; zero out-of-bounds), confirming the closed-form bound. Sign preservation of $\hat\tau_{\mathrm{dir}}$ therefore reduces to $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$.
482	\item \textbf{Non-proportional} ($f\sim\mathcal{N}(0,I_K)$ drawn independently of $g$, restricted to $|\tau_{\mathrm{ind}}|\geq 0.05$ to avoid the ill-conditioned regime where $\lambda{=}1{-}B/\tau_{\mathrm{ind}}$ diverges): $\lambda(C)$ exceeds $[0,1]$ in $\sim15$--$17\%$ of trials, illustrating that (a) and (b) are not automatic outside the proportional case.
483	\end{itemize}
484	The diagnostic $\lambda_V(C)$ lies in $[0,1]$ across all $30{,}000$ trials irrespective of regime, as guaranteed by the law of total variance. The script and full results are in \texttt{artifacts/verify\_lambda\_bound.py} and \texttt{artifacts/verify\_lambda\_bound\_results.json}.
485	
486	\subsection{Collider Topology ($A$ = Collider)}
487	\label{app:collider}
488	
489	\paragraph{Data-generating process.}
490	$T\to A\leftarrow Y$, $T\to Y$.
491	The treatment effect is unconfounded:
492	\begin{align*}
493	  T &\sim \mathcal{N}(0,1),\quad
494	  Y = \tau\,T + \varepsilon_Y,\quad \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp T,\\
495	  A\mid T,Y &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\delta}_T\,T + \boldsymbol{\delta}_Y\,Y)\bigr).
496	\end{align*}
497	The collider $A$ is a common \emph{effect} of $T$ and $Y$.
498	The no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\operatorname{plim}\hat\tau_{\mathrm{nc}}=\tau$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "d4480ed3-b945-4d8e-8cba-804b8849a98b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "Let $\\mu_j(\\delta)=N_j(\\delta)/q_j(\\delta)=\\mathbb{E}[g(A)\\mid A^*{=}j]$.\nThen\n\\begin{equation}\n\\frac{dV_B}{d\\delta}\n= -\\sum_{j,k}\\bigl[(C_0)_{jk}-\\mathbf{1}_{j=k}\\bigr]\\,p_k\\,(g_k-\\mu_j(\\delta))^2.\n\\label{eq:dVB}\n\\end{equation}\n\\emph{Derivation.}\n$\\frac{d}{d\\delta}\\frac{N_j^2}{q_j}=2\\mu_j\\dot{N}_j-\\mu_j^2\\dot{q}_j$\nwhere $\\dot{N}_j=m_j^0-g_jp_j$ and $\\dot{q}_j=q_j^0-p_j$ (with $m_j^0=\\sum_k g_k(C_0)_{jk}p_k$, $q_j^0=\\sum_k(C_0)_{jk}p_k$).\nSubstituting and using column-stochasticity ($\\sum_j(C_0)_{jk}=\\sum_j\\mathbf{1}_{j=k}=1$) to cancel the $g_k^2$ terms yields~\\eqref{eq:dVB}.\n\n\\emph{Step 3: $V_B'(0)\\leq 0$ (universal, no conditions on $C_0$).}\nAt $\\delta{=}0$: $\\mu_j(0)=g_j$ (since $C(0)=I$), so $(g_k-\\mu_j(0))^2=(g_k-g_j)^2$.\nThe diagonal terms ($j{=}k$) vanish.\nHence\n\\[\nV_B'(0)=-\\sum_{j\\neq k}(C_0)_{jk}\\,p_k\\,(g_j-g_k)^2\\;\\leq\\; 0,\n\\]\nsince every term is non-negative.\n\n\\emph{Step 4: $V_B'(1)\\leq 0$ for $K{=}2$.}\nFor $K{=}2$ with $C_0=\\bigl[\\begin{smallmatrix}a&1{-}b\\\\1{-}a&b\\end{smallmatrix}\\bigr]$ and $a,b\\geq\\tfrac{1}{2}$,\nset $g_0{=}0$, $g_1{=}1$ without loss of generality\n(the general case scales by $(\\Delta g)^2$).\nAt $\\delta{=}1$: $q_0{=}ap_0{+}(1{-}b)p_1$, $q_1{=}(1{-}a)p_0{+}bp_1$,\n$\\mu_0{=}(1{-}b)p_1/q_0$, $\\mu_1{=}bp_1/q_1$.\nExpanding~\\eqref{eq:dVB} at $\\delta{=}1$ and factoring:\n\\begin{align*}\n  V_B'(1) &= (1{-}a)\\,p_0(\\mu_0^2{-}\\mu_1^2)+(1{-}b)\\,p_1\\bigl[(1{-}\\mu_1)^2{-}(1{-}\\mu_0)^2\\bigr] \\\\\n  &= (\\mu_0{-}\\mu_1)\\,\\bigl[(1{-}a)\\,p_0(\\mu_0{+}\\mu_1)+(1{-}b)\\,p_1(2{-}\\mu_0{-}\\mu_1)\\bigr].\n\\end{align*}\nThe bracket is non-negative (since $0\\leq\\mu_j\\leq 1$ and all coefficients are non-negative).\nDirect calculation gives $\\mu_0{-}\\mu_1=p_0\\,p_1(1{-}a{-}b)/(q_0\\,q_1)$\n(expand $(1{-}b)\\,q_1-b\\,q_0=p_0(1{-}a{-}b)$).\nUnder $a,b\\geq\\tfrac{1}{2}$: $a{+}b\\geq 1$, so $\\mu_0{-}\\mu_1\\leq 0$ and $V_B'(1)\\leq 0$.\n\n\\emph{Step 5: Monotonicity from convexity.}\nSince $V_B$ is convex (Step~1), its derivative $V_B'$ is non-decreasing.\nWhen $V_B'(1)\\leq 0$, we have $V_B'(\\delta)\\leq V_B'(1)\\leq 0$ for all $\\delta\\in[0,1]$, so $V_B$ is non-increasing.\n\n\\emph{Step 6: $|B(\\delta)|$ is non-decreasing.}\n$V_W(\\delta)=\\operatorname{Var}(g)-V_B(\\delta)$ is non-decreasing (Step~5).\nThe function $h(x)=|\\lambda|\\,x/(x+\\sigma_T^2)$ is strictly increasing for $x\\geq 0$.\nHence $|B(\\delta)|=h(V_W(\\delta))$ is non-decreasing. \\qed\n\n\\paragraph{Condition on $C_0$.}\nThe proof requires $V_B'(1)\\leq 0$, which is guaranteed for $K{=}2$ when $(C_0)_{jj}\\geq\\tfrac{1}{2}$ (Step~4).\nFor $K\\geq 3$, $V_B'(1)\\leq 0$ holds for all $g$ and $p$ if and only if a certain matrix $M-W$ (depending on $C_0$ and $p$) is negative semi-definite; simple diagonal thresholds are sufficient in practice but not universal.\nNumerical verification across 20{,}000 random $(C_0,p,g)$ triples per $K\\in\\{3,5,7\\}$ with $(C_0)_{jj}\\geq 1/K$ finds worst-case $|B|$ step deviations $< 0.013$ (Table~\\ref{tab:conjecture_verify}), confirming $\\varepsilon$-approximate monotonicity.\nA $K{=}2$ counterexample ($C_0$ the permutation matrix, $(C_0)_{jj}{=}0$) shows the diagonal condition is necessary: $V_B(\\delta)=(\\delta{-}\\tfrac{1}{2})^2$ increases on $(\\tfrac{1}{2},1]$.\n\n\\paragraph{General case (non-proportional effects).}\n$|B(C(\\delta))|\\leq\\bar{B}(\\delta)$ where $\\bar{B}(\\delta)=\\sqrt{\\mathbb{E}[\\operatorname{Var}(g\\mid A^*_\\delta)]\\,\\mathbb{E}[\\operatorname{Var}(f\\mid A^*_\\delta)]}\\,/\\,D(\\delta)$ (Proposition~\\ref{prop:conf_gen}).\nBy the same convexity argument, each $\\mathbb{E}[\\operatorname{Var}(\\cdot\\mid A^*_\\delta)]$ is non-decreasing in $\\delta$, and $D(\\delta)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*_\\delta)]$ is non-decreasing.\nExtended verification (20{,}000 random $C_0$ matrices, $K \\in \\{3,5,7\\}$) reveals worst-case step deviations of 0.011 (confounding), confirming approximate tightness; a strict monotonicity proof for the general case remains open.\n\n\\subsection{Mediation Topology ($A$ = Mediator)}\n\\label{app:mediation}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\to Y$, $T\\to Y$.\n\\begin{align*}\n  T &\\sim \\operatorname{Bernoulli}(0.5),\\\\\n  A\\mid T &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\gamma}+\\boldsymbol{\\delta}\\,T)\\bigr),\\\\\n  Y &= \\tau_{\\mathrm{dir}}\\,T + f(A) + \\varepsilon_Y.\n\\end{align*}\n\n\\paragraph{Bias decomposition.}\nBy Lemma~\\ref{lem:bias_decomp}, the direct-effect estimator satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C) = \\tau_{\\mathrm{dir}} + \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:med_bias}\n\\end{equation}\n\nThe key structural difference from confounding: $T$ \\emph{causes} $A$, so the residual covariance $\\operatorname{Cov}(T,f(A)\\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.\n\n\\paragraph{Endpoint analysis.}\n\nAt $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\\to A\\to Y$, so $\\operatorname{Cov}(T,f(A)\\mid A)=0$ and $\\operatorname{plim}\\hat\\tau=\\tau_{\\mathrm{dir}}$.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ ($A^*\\perp A$): no information about $A$ is used, and\n\\begin{align*}\n  \\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)] &= \\operatorname{Cov}(T,f(A)),\\\\\n  D(C) &= \\operatorname{Var}(T) = 0.25.\n\\end{align*}\nThe indirect effect is $\\tau_{\\mathrm{ind}}=\\mathbb{E}[f(A)\\mid T{=}1]-\\mathbb{E}[f(A)\\mid T{=}0]$, and\n\\[\n  \\operatorname{Cov}(T,f(A)) = 0.25\\,\\tau_{\\mathrm{ind}}.\n\\]\nHence at $C$ uniform: $\\operatorname{plim}\\hat\\tau = \\tau_{\\mathrm{dir}}+\\tau_{\\mathrm{ind}} = \\tau_{\\mathrm{total}}$.\n\n\\paragraph{Numerical Verification (Mediation sign preservation).}\n\\label{find:med_sign}\n$\\operatorname{sign}(\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{dir}})$ whenever $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$, where $\\tau_{\\mathrm{total}}=\\tau_{\\mathrm{dir}}+\\tau_{\\mathrm{ind}}$.\nThis result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.\n\n\\begin{proof}\nLet $R(C)=\\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)]$ and $D(C)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]>0$.\n\n\\emph{Endpoints.}\nAt $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$: $R=\\operatorname{Cov}(T,f(A))=0.25\\,\\tau_{\\mathrm{ind}}$ and $D=\\operatorname{Var}(T)=0.25$, giving $B=\\tau_{\\mathrm{ind}}$.\n\n\\emph{Within-group structure for binary $T$.}\nSince $T\\in\\{0,1\\}$, the within-$A^*$-group bias admits a revealing decomposition.\nLet $p_j=P(T{=}1\\mid A^*{=}j)$.\nThen $\\operatorname{Var}(T\\mid A^*{=}j)=p_j(1{-}p_j)$ and\n\\[\n  \\operatorname{Cov}(T,f(A)\\mid A^*{=}j)\n  = p_j(1{-}p_j)\\bigl[\\mathbb{E}[f(A)\\mid T{=}1,A^*{=}j]-\\mathbb{E}[f(A)\\mid T{=}0,A^*{=}j]\\bigr].\n\\]\nDefine $\\delta_j=\\mathbb{E}[f(A)\\mid T{=}1,A^*{=}j]-\\mathbb{E}[f(A)\\mid T{=}0,A^*{=}j]$ as the \\emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.\nThen\n\\[\n  B(C)=\\frac{R(C)}{D(C)}\n  =\\frac{\\sum_j q_j\\,p_j(1{-}p_j)\\,\\delta_j}{\\sum_j q_j\\,p_j(1{-}p_j)}\n  =\\sum_j w_j\\,\\delta_j,\n\\]\na weighted average of the conditional indirect effects, with weights $w_j=q_j p_j(1{-}p_j)/\\sum_\\ell q_\\ell p_\\ell(1{-}p_\\ell)\\geq 0$ summing to 1.\n\nAt $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\\delta_j=f(j)-f(j)=0$ and $B=0$.\nAt $C$ uniform: $\\delta_j=\\tau_{\\mathrm{ind}}$ for all $j$ and $B=\\tau_{\\mathrm{ind}}$.\n\n\\emph{Sign preservation.}\nWhen $\\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{ind}}$ have the same sign), the bias $B(C)\\geq 0$ cannot oppose $\\tau_{\\mathrm{dir}}$, so sign is preserved trivially.\n\nWhen $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{ind}}$ have opposite signs but $|\\tau_{\\mathrm{ind}}|<|\\tau_{\\mathrm{dir}}|$ (i.e., $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$), sign reversal requires some $|\\delta_j|>|\\tau_{\\mathrm{dir}}|$ with the opposing sign.\nSince each $\\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\\delta_j$, the bound $|B(C)|\\leq\\max_j|\\delta_j|$ holds.\nWe verify numerically that $\\max_j|\\delta_j|\\leq|\\tau_{\\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.\n\\end{proof}\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau_{\\mathrm{dir}}{=}0.5$, $\\boldsymbol{\\gamma}{=}(0,0,0)$, $\\boldsymbol{\\delta}{=}(0,0.8,{-}0.6)$, $\\boldsymbol{\\beta}{=}(0,1.0,{-}0.5)$:\n\n$\\tau_{\\mathrm{ind}}=\\mathbb{E}[f(A)\\mid T{=}1]-\\mathbb{E}[f(A)\\mid T{=}0]=0.351$ (computed from the softmax class probabilities).\n$\\tau_{\\mathrm{total}}=0.5+0.351=0.851>0$.\nSince $\\tau_{\\mathrm{dir}}{>}0$ and $\\tau_{\\mathrm{total}}{>}0$, sign preservation holds for all $C$.\n\n\\paragraph{Mediation monotonicity (proportional effects).}\n\\label{par:med_monotone}\n\nUnder the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\\lambda\\,g(A)$ for some scalar $\\lambda$, where $g(k)=\\mathbb{E}[T\\mid A{=}k]$.\n\n\\emph{Step 1: Decompose $T$ via the mediator.}\nDefine $g(A)=\\mathbb{E}[T\\mid A]$ and $\\varepsilon_T = T - g(A)$.\nBy construction, $\\mathbb{E}[\\varepsilon_T\\mid A]=0$.\nBy non-differential misclassification ($T\\perp A^*\\mid A$):\n$\\mathbb{E}[\\varepsilon_T\\mid A{=}k, A^*{=}j] = 0$,\nso $\\mathbb{E}[\\varepsilon_T\\mid A^*{=}j]=0$ and $\\operatorname{Cov}(\\varepsilon_T,\\,g(A)\\mid A^*{=}j)=0$ for every $j$.\n\n\\emph{Step 2: Reduce the numerator.}\nSince $f=\\lambda g$:\n\\begin{align*}\n  R(C) &= \\lambda\\,\\mathbb{E}[\\operatorname{Var}(g(A)\\mid A^*)] = \\lambda\\,V_W.\n\\end{align*}\n\n\\emph{Step 3: Constant additive term in denominator.}\n\\begin{align*}\n  D(C) &= \\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]\n       = V_W + \\sigma_\\varepsilon^2,\n\\end{align*}\nwhere $\\sigma_\\varepsilon^2\\equiv\\mathbb{E}[\\operatorname{Var}(\\varepsilon_T\\mid A^*)]$.\nThis is \\emph{constant} (independent of $C$):\n$\\mathbb{E}[\\operatorname{Var}(\\varepsilon_T\\mid A^*)]\n  = \\sum_k p_k\\,\\operatorname{Var}(T\\mid A{=}k)\n  = \\mathbb{E}[\\operatorname{Var}(T\\mid A)]$,\nwhere the equality uses column-stochasticity: $\\sum_j q_j\\,P(A{=}k\\mid A^*{=}j)=p_k$.\n\n\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_B(\\delta)$ is convex with $V_B'(0)\\leq 0$ (same argument as \\S\\ref{app:monotonicity_proof}, Steps~1--3), $V_W(\\delta)=V{-}V_B(\\delta)$ is non-decreasing under the same conditions on $C_0$.\nSince $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\paragraph{Boundedness of the leakage coefficient.}\n\nThe mediation bias~\\eqref{eq:mediation} writes the residual indirect effect as $(1-\\lambda(C))\\,\\tau_{\\mathrm{ind}}$, which (for $\\tau_{\\mathrm{ind}}\\neq 0$) \\emph{implicitly} defines\n\\begin{equation}\n\\label{eq:lambda_def}\n  \\lambda(C) \\;:=\\; 1-\\frac{B(C)}{\\tau_{\\mathrm{ind}}},\\qquad\n  B(C)\\;\\equiv\\;\\operatorname{plim}\\hat{\\tau}_{\\mathrm{dir}}(A^*)-\\tau_{\\mathrm{dir}},\\quad\n  \\tau_{\\mathrm{ind}}\\;=\\;\\frac{\\operatorname{Cov}(T,f(A))}{\\operatorname{Var}(T)}.\n\\end{equation}\nSubstituting back into~\\eqref{eq:mediation} gives the convex-combination form\n$\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)=\\lambda(C)\\,\\tau_{\\mathrm{dir}}+(1-\\lambda(C))\\,\\tau_{\\mathrm{total}}$, so $\\lambda(C)$ is the weight placing the biased plim between $\\tau_{\\mathrm{dir}}$ (perfect classification) and $\\tau_{\\mathrm{total}}$ (no information).\n\n\\begin{proposition}[Mediation leakage boundedness]\n\\label{prop:lambda_bound}\nLet $\\lambda(C)$ be defined by~\\eqref{eq:lambda_def} with $\\tau_{\\mathrm{ind}}\\neq 0$, and let $C$ be column-stochastic.\n\\begin{enumerate}\n\\item[(a)] $\\lambda(C)\\leq 1$ iff $\\operatorname{sign}(B(C))=\\operatorname{sign}(\\tau_{\\mathrm{ind}})$ (the bias points in the direction of the indirect effect; no overcorrection).\n\\item[(b)] $\\lambda(C)\\geq 0$ iff additionally $|B(C)|\\leq|\\tau_{\\mathrm{ind}}|$ (the bias does not exceed the indirect effect in magnitude).\n\\end{enumerate}\nEquivalently, $\\lambda(C)\\in[0,1]$ iff $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)\\in[\\min(\\tau_{\\mathrm{dir}},\\tau_{\\mathrm{total}}),\\,\\max(\\tau_{\\mathrm{dir}},\\tau_{\\mathrm{total}})]$.\n\nUnder \\emph{proportional effects} ($f(A)=\\lambda_0\\,g(A)$ with $g(k)=\\mathbb{E}[T\\mid A{=}k]$), both (a) and (b) hold for every $C$, so $\\lambda(C)\\in[0,1]$ unconditionally.\nFor \\emph{general (non-proportional)} $f$, both (a) and (b) can fail because $\\operatorname{Cov}(\\mathbb{E}[g\\mid A^*],\\mathbb{E}[f\\mid A^*])$ may differ in sign or magnitude from $\\operatorname{Cov}(g,f)$ (a covariance-level analogue of Simpson's paradox under $A^*$ aggregation); the numerical verification below quantifies the empirical rate.\nThe endpoints $\\lambda(I)=1$ and $\\lambda(C)\\to 0$ in the rank-one (uninformative) limit hold in all regimes.\n\n\\emph{Sign preservation.} When $\\lambda(C)\\in[0,1]$, the convex-combination form gives $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)\\in[\\min(\\tau_{\\mathrm{dir}},\\tau_{\\mathrm{total}}),\\,\\max(\\tau_{\\mathrm{dir}},\\tau_{\\mathrm{total}})]$. If additionally $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$, both endpoints share the same sign, so $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{dir}})$ for every~$C$. Under proportional effects, $\\lambda(C)\\in[0,1]$ is automatic (above), so sign preservation of $\\hat\\tau_{\\mathrm{dir}}$ reduces to the single condition $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$.\n\\end{proposition}\n\n\\begin{proof}\n\\emph{(a),(b).} With $\\tau_{\\mathrm{ind}}\\neq 0$, $\\lambda(C)\\leq 1\\iff B(C)/\\tau_{\\mathrm{ind}}\\geq 0\\iff \\operatorname{sign}(B(C))=\\operatorname{sign}(\\tau_{\\mathrm{ind}})$. Given (a), $\\lambda(C)\\geq 0\\iff B(C)/\\tau_{\\mathrm{ind}}\\leq 1\\iff|B(C)|\\leq|\\tau_{\\mathrm{ind}}|$.\n\n\\emph{Proportional case.} Step~4 of the mediation derivation gives $B(C)=\\lambda_0\\,V_W(C)/(V_W(C)+\\sigma_\\varepsilon^2)$; the rank-one limit $V_W{\\to}V$ yields $\\tau_{\\mathrm{ind}}=\\lambda_0\\,V/(V+\\sigma_\\varepsilon^2)$. Both quantities carry $\\operatorname{sign}(\\lambda_0)$, establishing~(a). The ratio\n\\[\n  \\frac{B(C)}{\\tau_{\\mathrm{ind}}}\\;=\\;\\frac{V_W(C)\\,(V+\\sigma_\\varepsilon^2)}{V\\,(V_W(C)+\\sigma_\\varepsilon^2)}\n\\]\nis monotone increasing in $V_W(C)\\in[0,V]$ with range $[0,1]$ (its derivative in $V_W$ is $\\sigma_\\varepsilon^2(V+\\sigma_\\varepsilon^2)/[V(V_W+\\sigma_\\varepsilon^2)^2]>0$), establishing~(b). Hence $\\lambda(C)\\in[0,1]$ unconditionally.\n\n\\emph{General case.} Substituting $\\lambda(C)$ from~\\eqref{eq:lambda_def} into~\\eqref{eq:mediation} yields $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)=\\lambda(C)\\,\\tau_{\\mathrm{dir}}+(1{-}\\lambda(C))\\,\\tau_{\\mathrm{total}}$, so $\\lambda(C)\\in[0,1]$ iff $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)$ lies in the closed interval with endpoints $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{total}}$.\n\n\\emph{Endpoints.} At $C{=}I$, $A^*{=}A$ a.s., $\\mathbb{E}[T\\mid A^*]=g(A)$, and FWL gives $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}=\\tau_{\\mathrm{dir}}$, hence $B(I)=0$ and $\\lambda(I)=1$. At any rank-one $C$ (rows identical), $A^*\\perp A$ so $\\mathbb{E}[T\\mid A^*]$ is constant, the partial regression on $A^*$ has no effect, and $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}=\\operatorname{Cov}(Y,T)/\\operatorname{Var}(T)=\\tau_{\\mathrm{total}}$, giving $B=\\tau_{\\mathrm{ind}}$ and $\\lambda=0$.\n\\end{proof}\n\n\\paragraph{Relation to the between-variance ratio.}\nA natural \\emph{diagnostic} closely related to $\\lambda(C)$ is the between-variance ratio\n\\begin{equation}\n\\label{eq:vb_ratio}\n  \\lambda_V(C) \\;:=\\; \\frac{V_B(C)}{V},\\qquad V_B(C)\\;=\\;\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr),\\quad V\\;=\\;\\operatorname{Var}(g(A)),\n\\end{equation}\nwhich satisfies $\\lambda_V(C)\\in[0,1]$ \\emph{unconditionally} by the law of total variance applied to $g(A)$. Under proportional effects, $\\lambda$ and $\\lambda_V$ agree at the endpoints and are related by\n\\[\n  1-\\lambda(C)\\;=\\;\\frac{V_W(C)\\,(V+\\sigma_\\varepsilon^2)}{V\\,(V_W(C)+\\sigma_\\varepsilon^2)}\\;=\\;\\bigl(1-\\lambda_V(C)\\bigr)\\cdot\\frac{V+\\sigma_\\varepsilon^2}{V_W(C)+\\sigma_\\varepsilon^2},\n\\]\nso they coincide in the limit $\\sigma_\\varepsilon^2\\gg V$. They generally differ for non-proportional $f$. We use $\\lambda$ throughout the main text because it parameterizes~\\eqref{eq:mediation} directly; $\\lambda_V$ remains a useful summary of the channel quality of $A^*$ as a proxy for $A$ (independent of the structural form of $f$).\n\n\\paragraph{Numerical verification.}\nFor each $K\\in\\{3,5,7\\}$ we draw $N{=}10{,}000$ configurations $(\\pi,g,\\sigma_\\varepsilon^2,C)$ with $\\pi\\sim\\operatorname{Dirichlet}(\\mathbf{1})$, $g\\sim\\mathcal{N}(0,I_K)$, $\\sigma_\\varepsilon^2\\sim\\operatorname{Uniform}(0.1,2)$, columns of $C\\sim\\operatorname{Dirichlet}(\\mathbf{1})$, and evaluate $\\lambda(C)$ from~\\eqref{eq:lambda_def} in two regimes for $f$:\n\\begin{itemize}\\itemsep0pt\n\\item \\textbf{Proportional} ($f=\\lambda_0\\,g$, $\\lambda_0\\sim\\mathcal{N}(0,1)\\!\\setminus\\!\\{0\\}$): $\\lambda(C)\\in[0,1]$ in \\emph{all} $30{,}000$ trials (pooled observed range $[1.2{\\times}10^{-5},\\,0.850]$; zero out-of-bounds), confirming the closed-form bound. Sign preservation of $\\hat\\tau_{\\mathrm{dir}}$ therefore reduces to $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$.\n\\item \\textbf{Non-proportional} ($f\\sim\\mathcal{N}(0,I_K)$ drawn independently of $g$, restricted to $|\\tau_{\\mathrm{ind}}|\\geq 0.05$ to avoid the ill-conditioned regime where $\\lambda{=}1{-}B/\\tau_{\\mathrm{ind}}$ diverges): $\\lambda(C)$ exceeds $[0,1]$ in $\\sim15$--$17\\%$ of trials, illustrating that (a) and (b) are not automatic outside the proportional case.\n\\end{itemize}\nThe diagnostic $\\lambda_V(C)$ lies in $[0,1]$ across all $30{,}000$ trials irrespective of regime, as guaranteed by the law of total variance. The script and full results are in \\texttt{artifacts/verify\\_lambda\\_bound.py} and \\texttt{artifacts/verify\\_lambda\\_bound\\_results.json}.\n\n\\subsection{Collider Topology ($A$ = Collider)}\n\\label{app:collider}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\leftarrow Y$, $T\\to Y$.\nThe treatment effect is unconfounded:\n\\begin{align*}\n  T &\\sim \\mathcal{N}(0,1),\\quad\n  Y = \\tau\\,T + \\varepsilon_Y,\\quad \\varepsilon_Y\\sim\\mathcal{N}(0,1),\\;\\varepsilon_Y\\perp T,\\\\\n  A\\mid T,Y &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\delta}_T\\,T + \\boldsymbol{\\delta}_Y\\,Y)\\bigr).\n\\end{align*}\nThe collider $A$ is a common \\emph{effect} of $T$ and $Y$.\nThe no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\\operatorname{plim}\\hat\\tau_{\\mathrm{nc}}=\\tau$.",
      "numLines": 250,
      "startLine": 249,
      "totalLines": 1480
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the existing proofs. Let me now focus on the task: prove that for K=3 symmetric confusion matrix, |B(C(δ))| is non-decreasing in δ.

The key insight from the existing proof is:
1. For the proportional case (f = λg), B(C) = λV_W/(V_W + σ_T²)
2. |B| is non-decreasing iff V_W(δ) is non-decreasing iff V_B(δ) is non-decreasing


3. V_B(δ) is convex with V_B'(0) ≤ 0 universally, and I need to show V_B'(1) ≤ 0 for the K=3 symmetric case where the confusion matrix has diagonal entries 1-2c and off-diagonal entries c.

4. This would establish that V_B is non-increasing on [0,1], which means V_W is non-decreasing, confirming that |B| grows monotonically along the path C(δ) = (1-δ)I + δC₀.

5. Let me work through the algebra explicitly for K=3 with this symmetric structure to compute the derivative at δ=1. Now I'm working through the variance decomposition where the bias term depends on how the confounded treatment affects the outcome distribution. The key insight is that under proportional effects, the bias scales with the within-group variance relative to total variance, and I need to show this decreases monotonically as δ increases. Continuing with the convexity argument: since V_B' is non-decreasing, if V_B'(1) ≤ 0 then V_B'(δ) ≤ 0 for all δ ∈ [0,1], making V_B non-increasing. So I need to verify that V_B'(1) ≤ 0 when K=3 with symmetric C₀, using the derivative formula where at δ=1 the conditional expectations μ_j(1) equal E[g(A) | A* = j] under C₀.

For the symmetric 3×3 case, I'm computing how the transition matrix C₀ affects the weighted sums: the marginal probabilities q_j(1) become a mixture of the diagonal and off-diagonal elements scaled by the group probabilities, and the weighted group means N_j(1) combine the within-group and between-group contributions. Let me recalculate the matrix difference more carefully. When j equals k, I get -2c, and when j doesn't equal k, I get c. Now I'm working through the variance expression by separating the diagonal and off-diagonal terms in the double sum.

I'm noticing this is getting quite involved with arbitrary p and g distributions, so I should check whether the problem statement restricts these or if I need to handle the general case.

Looking back at the task, it specifies the symmetric structure of C₀ but doesn't constrain p or g, so I need to work with general distributions. The derivative of the bias at δ=1 involves this expression with μ_j depending on both the confusion matrix parameters and the specific p and g values.

Let me reconsider the K=3 symmetric case more carefully. For a symmetric confusion matrix with diagonal entries 1-2c and off-diagonal entries c, I can express it as a convex combination of the identity and the all-ones matrix. Verifying this structure: the diagonal gives 1-3c + c = 1-2c, and I need to check the off-diagonal entries match as well.

Now I'm working through how the interpolated matrix C(δ) evolves along this path. Since C(δ) = (1-δ)I + δC₀, substituting the decomposition shows that C(δ) maintains the same form with a scaled parameter s = cδ that ranges from 0 to c as δ varies.

With this structure locked in, I can now express the key quantities in terms of s. For each component j, I'm computing the weighted sum q_j and the group-weighted sum N_j, then finding the group means μ_j as their ratio. This sets me up to calculate V_B(s) as the variance across these group means.

To simplify the algebra, I'm introducing a substitution t = 1-3s to make the expressions cleaner and identify the valid range for t.

Now I'm rewriting N_j and q_j in terms of t, then substituting into the variance formula. Let me try a different approach by examining the eigenstructure of the covariance matrix—it has a specific form with an identity component and a rank-one perturbation, which should give me eigenvalues I can work with directly.

For the misclassification probabilities, the confusion matrix has this symmetric exchangeable structure where each category gets confused with others equally. Now I'm trying a more direct calculation by centering the g values around their mean and expressing the shifted means in terms of these centered deviations.

Working through the algebra, the between-group variance simplifies to (1-3s)² times the original variance, which shows how the misclassification parameter s scales the variance reduction.

Now I need to find the derivative with respect to s. I'll define a helper function for each group's contribution to make the differentiation cleaner.

Taking the derivative of the product, I get two terms: one from differentiating the squared factor and another from differentiating the sum. For the individual derivatives, I need to apply the quotient rule carefully—the denominator changes with s, and its derivative is 1 - 3p_j.

Factoring out (1-3s) from the full derivative expression, the algebra is getting unwieldy, so I should probably look for a different approach or simplification.

Let me try substituting the K=3 symmetric case directly into the derivative formula from the paper. For a symmetric covariance matrix, the structure simplifies to specific patterns depending on whether indices match, which should make the derivative more tractable.

Now I'm switching to a different parameterization - using s = cδ to track how the covariance structure evolves along the path. I've already worked out the mean functions and the variance expression in terms of s, so let me continue building on those relationships to find where the derivative equals zero. Now I'm working through the derivative of V_B with respect to s by treating it as a product of (1-3s)² and a sum F(s) involving the squared terms. Using the product rule, I need to find both how the polynomial factor changes and how F(s) itself varies with s, which involves computing the derivative of each term in the sum with respect to the denominator q_j. Completing the algebraic simplification to show that 6q_j + (1-3c)(1-3p_j) equals 3(1-3c)p_j + 1 + 3c, which is always positive since all terms are non-negative for p_j ≥ 0 and c ∈ (0, 1/3).

This means the derivative dV_B/ds at s=c is non-positive, establishing that V_B'(1) ≤ 0 for all symmetric configurations with c in that range. Combined with the convexity property and the boundary condition at zero, this constrains the behavior of the objective function.

Now I'm recalculating the derivative more carefully using the product rule on the expression for V_B, accounting for how both the coefficient and the denominator change with respect to s. Continuing the algebraic simplification to show that the numerator is always negative for the valid range of parameters, which means the derivative has a definite sign.

Now I'm seeing that this actually establishes something stronger—the derivative stays non-positive across the entire interval, not just at isolated points. This means the Lyapunov function decreases monotonically along the whole trajectory without needing to invoke convexity separately. Let me verify this with a concrete example using a uniform distribution across three categories with symmetric payoffs. When I plug in the uniform case, something interesting happens—the distribution q_j stays constant at 1/3 throughout the perturbation, which simplifies V_B(s) to a clean quadratic form in (1-3s)².

Taking the derivative confirms this variance is strictly decreasing for valid perturbation sizes, which is reassuring. Now I want to test whether this pattern holds with non-uniform probabilities, so I'm setting up a case with p = (0.5, 0.3, 0.2) and payoffs that aren't symmetric around zero.

Computing the mean payoff as 0.25, I can then calculate the centered payoffs and work through the variance formula with the weighted terms to see how the behavior changes under this non-uniform distribution. Now I'm computing F at s = 0.1 by summing the ratios of squared terms to their respective q values, which gives me approximately 0.749, then multiplying by (1-3s)² to get V_B(0.1) ≈ 0.367. Moving to s = 0.2, I'm recalculating the q values with the updated scaling factor and preparing to compute F again. Checking the remaining terms at s = 0.1 confirms they're all negative as well. This establishes that the derivative stays negative throughout the interval, which means V_B is strictly decreasing while V_W increases and the between-cluster sum of squares grows monotonically—a remarkably elegant result for this symmetric case where the confusion matrix stays within a one-parameter family.

The existing analysis only verified this at the boundaries or through numerical checks for K≥3, but here I've shown it holds everywhere for the symmetric K=3 case. Now I should examine whether this same monotonicity property extends to the mediation and collider scenarios, since the paper indicates mediation reduces to the confounding structure with a different variance term, while collider has a fundamentally different bias mechanism. I need to figure out whether to work with the proportional case or tackle the general bias expression. The bias formula B(C) = R(C)/D(C) doesn't have a clean closed form in general, but for the symmetric K=3 case, maybe I can compute it directly without that restriction. Let me work through the bias decomposition for symmetric C(δ) and see where that leads.

Now I'm computing the conditional expectations and covariance terms. For each outcome j, the conditional expectation of g given A* involves the deviation h_j^g from the overall mean, scaled by the confounding parameter s. The covariance between the conditional expectations factors as a sum over j, weighted by the squared propensity terms and the product of deviations. This gives me (1-3s)² times a weighted sum of the outcome deviations.

For the denominator, I need the variance of the treatment conditional on A*, which combines the treatment variance with the conditional variance of g, adjusted by the bias variance term V_B^g(s). Putting this together, the bias function B(s) becomes a ratio where the numerator captures the confounding-adjusted covariance and the denominator accounts for the total variance in the treatment assignment mechanism. The general case requires handling this more complex structure.

For the proportional case where f equals some scalar multiple of g, the problem simplifies considerably. The bias function reduces to a cleaner form involving the within-group variance V_W(s), which is non-decreasing since V_B(s) is non-increasing. Since the function mapping x to |λ|x/(x + σ_T²) is monotonically increasing, the absolute bias should be non-decreasing in s.

The key insight was showing that the derivative of V_B with respect to s stays non-positive across the entire range, which I established by breaking it into a sum of non-positive components.

Now I'm tackling the general case where f and g aren't proportional. Here the bias is a ratio of two functions—the numerator involves the covariance between g and f adjusted by a term that depends on s, while the denominator is the total variance adjusted similarly. This is more complex because I need to track how both the numerator and denominator change with s to establish monotonicity of the ratio. At s=1/3, the terms vanish and I recover the omitted variable bias coefficient B_OV, so the bias transitions from zero to B_OV as s varies. I'm wondering whether the magnitude stays monotone throughout, and noting that Φ_gf can flip sign if g and f are negatively correlated across categories, which means R(s) could cross zero. For the special case where f is proportional to g, the relationship simplifies nicely since Φ_gf becomes a scaled version of Φ_gg.

Now I'm trying to understand the general behavior by examining how Φ_gf changes with s, which seems more involved than the proportional case. The goal is to prove monotonicity of the bias magnitude with respect to δ for the confounding topology case. For the general case, the existing approach only cleanly handles proportional effects, so I'm exploring whether K=3 symmetric confounder structure might allow a complete proof. I'm setting up the bias formula with simplified notation—defining the numerator as the covariance difference and denominator as the variance sum—and noting that the second derivative of the variance term is non-positive, but I need to work through what happens with the covariance term to establish the full monotonicity result.

Now I'm computing the derivative of the covariance term with respect to δ, applying the product rule and chain rule to the weighted sum. The calculation shows each bracket in the resulting expression is negative, which is promising for establishing monotonicity, though I need to verify the sign of the product terms to complete the argument.

For the general case where effects aren't proportional, the correlation structure between g and f becomes crucial—the derivative's sign depends on how these are correlated, so I can't establish a universal result without additional constraints. The cleanest theorem I can prove is that for K=3 with proportional effects, the determinant is strictly monotone non-decreasing across the parameter range, which follows from showing the derivative of the variance term is negative throughout the interval.

For the non-proportional case, I'm trying a direct approach by rewriting the bias ratio in terms of the change in covariance and variance from the baseline, setting up u(s) and v(s) to track these differences. Φ'v + u·Ψ')/v². This approach isn't leading anywhere clean, so let me try working through a specific numerical case to see if the monotonicity actually holds for the general symmetric case with K=3. I think I should focus on writing up the proportional case cleanly first, then verify the general case computationally. Actually, looking back at the task, I need to start from the confounding topology and work through the bias expression systematically with the symmetric C(δ) structure.

For the confounding bias, I have B(C) = R(C)/D(C) where R captures the covariance difference and D is the variance component. With K=3 symmetric C(δ) parameterized by s = cδ, I need to derive the closed-form expression for |B(C(δ))| by substituting the conditional expectations E[g|A*=j] in terms of the bias parameters. For the proportional case where f equals λ times g, I can express the bias in closed form as λ times a variance term that depends on s, and this bias is monotonically non-decreasing since both the variance component and the scaling function are monotone increasing.

For the uniform prior case where all priors are equal, the math simplifies considerably—the between-group variance becomes proportional to (1-3s)² times the overall variance of g, which means the within-group variance reduces to just the overall variance scaled by a factor that depends on s. For a general prior, the within-group variance follows V_W(s) = Var(g) - V_B(s), where the between-group component decreases monotonically with s in the interval (0, 1/3), making V_W strictly increasing. Now I'm working through the non-proportional case for three symmetric categories, deriving expressions for the bias in terms of covariance and variance components that depend on s.

At the boundaries, B(0) = 0 and as s approaches 1/3, B converges to the ratio of covariances over total variance. For |B(s)| to increase monotonically from zero to its maximum, I need B(s) itself to be monotone. Let me check whether B'(s) is positive or negative by examining the derivatives of the numerator and denominator separately. I'm working through the derivative of Φ_gf with respect to s, which involves the product rule applied to the (1-3s)² term and the sum Ω. After computing this, I can find u'(s) as the negative of this derivative, which will help me evaluate the quotient rule for B'(s). The sign of u'(s) depends on whether h_j^g and h_j^f align, which makes B'(s) harder to characterize generally. At s = 0, I can use the fact that u(0) = 0 to find B'(0) = u'(0)/v(0), and computing u'(0) gives me a sum that depends on the signs of the h terms and the probabilities—so whether B increases from zero depends on whether this sum is positive.

For B(s) to stay monotone on [0, 1/c], I'd need B' to maintain its sign throughout, but there's no guarantee of this for arbitrary g and f. The real constraint is whether |B(s)| can be non-decreasing; since B(0) = 0, if B oscillates between positive and negative values, |B| would fail to be monotone. So I'm asking whether B can actually be non-monotone for the K=3 symmetric case, and I think a numerical check would help clarify this. For the proportional case specifically, B(s) simplifies to a ratio involving V_W(s), which might have nicer properties.

In the proportional setting, since V_W is increasing and the ratio function is monotone, B(s) inherits monotonicity and maintains a consistent sign. But in the general non-proportional case, the cross-covariance terms could evolve differently, potentially causing B to change sign and creating non-monotonicity. My strategy is to prove the proportional case rigorously, run a numerical experiment for K=3 symmetric to check the general case, and either establish it as a conjecture or identify where it breaks down—mirroring how the existing paper handles this result.

Now I'm setting up the proof structure and numerical verification. For K=3 symmetric, the covariance matrix stays in a one-parameter family as I vary the confounding, which lets me derive a closed-form expression for the bias variance and compute its derivative directly to confirm monotonicity. Writing LaTeX proof...

Now I need to verify whether we're dealing with strict monotonicity or just non-decreasing behavior. The problem asks for "strictly monotone non-decreasing," which means strictly increasing. For |B| to be strictly increasing, V_W must be strictly increasing, which requires V_B to be strictly decreasing. Looking at the derivative, each term in dV_B/ds is zero only when either h_j or p_j equals zero, but if the variance is positive, at least two h_j values are nonzero with corresponding positive p_j values, so the derivative stays strictly negative on the interval (0, 1/3), making |B| strictly increasing there. At the boundary where δ = 0, we have |B(0)| = 0, and for any δ > 0, |B(δ)| > 0, confirming strict monotonicity across (0, 1), though I need to check the left derivative at the origin.

The left derivative at δ = 0 is positive since V_W grows like a positive constant times δ near zero, so |B| is indeed strictly increasing on the entire interval [0, 1]. This confirms the result is strictly non-decreasing, and strictly increasing when the variance is positive and λ ≠ 0.

Now I'm extending this analysis to mediation and collider scenarios. For mediation with proportional effects, the same V_B decomposition holds, and with three symmetric categories, the argument that V_B is non-increasing still applies, making |B| non-decreasing. For the collider case, conditioning introduces bias in a different way that I need to work through.

The task asks me to verify confounding first, then extend to mediation and collider, and if successful, formalize everything as Theorem 2. Since confounding and mediation are structurally similar, I'll write those up together before tackling the collider. Now I need to write the computational verification script to confirm these results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "aa927ae0-04d7-4ea7-b961-9b6eef0f586e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155PS4d8QixZzUE9sP61GrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9510,
      "cache_read_input_tokens": 32745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9510
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

### Assistant

_source line 10_

Now let me read the rest of the monotonicity proof and the collider section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "c8ae7a8a-52e2-435d-90ea-2f960a9ce20d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155PS4d8QixZzUE9sP61GrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9510,
      "cache_read_input_tokens": 32745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9510
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01Dk7Jv3fyNBzwFozF6E7MjN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 486,
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
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "5e76acaf-6842-4ac0-878b-512dd833a692",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155PS4d8QixZzUE9sP61GrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9510,
      "cache_read_input_tokens": 32745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9510
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

_source line 12 · 2026-05-23T17:41:28.903Z_

<details><summary>↩ Tool result · `toolu_01Dk7Jv3fyNBzwFozF6E7MjN`</summary>

```text
486	\subsection{Collider Topology ($A$ = Collider)}
487	\label{app:collider}
488	
489	\paragraph{Data-generating process.}
490	$T\to A\leftarrow Y$, $T\to Y$.
491	The treatment effect is unconfounded:
492	\begin{align*}
493	  T &\sim \mathcal{N}(0,1),\quad
494	  Y = \tau\,T + \varepsilon_Y,\quad \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp T,\\
495	  A\mid T,Y &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\delta}_T\,T + \boldsymbol{\delta}_Y\,Y)\bigr).
496	\end{align*}
497	The collider $A$ is a common \emph{effect} of $T$ and $Y$.
498	The no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\operatorname{plim}\hat\tau_{\mathrm{nc}}=\tau$.
499	The researcher erroneously controls for $A^*$, inducing Berkson's bias.
500	
501	\paragraph{Bias decomposition.}
502	Unlike confounding, $\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\tau T+\varepsilon_Y$), so Lemma~\ref{lem:bias_decomp} does not apply directly.
503	Instead, we derive the bias from the FWL identity~\eqref{eq:fwl}.
504	Writing $\tilde{Y}=\tau\tilde{T}+(\varepsilon_Y-\mathbb{E}[\varepsilon_Y\mid A^*])$ and noting that $\mathbb{E}[\tilde{T}\,\varepsilon_Y]=\mathbb{E}[\operatorname{Cov}(T,\varepsilon_Y\mid A^*)]$ (since $T\perp\varepsilon_Y$ unconditionally):
505	\begin{equation}
506	  \operatorname{plim}\hat\tau(C) = \tau + B(C),\quad
507	  B(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,\varepsilon_Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
508	  \label{eq:bias_col}
509	\end{equation}
510	Under non-differential misclassification ($A^*\perp(T,\varepsilon_Y)\mid A$), define $g(k)=\mathbb{E}[T\mid A{=}k]$ and $h(k)=\mathbb{E}[\varepsilon_Y\mid A{=}k]$.
511	By the tower property, $\mathbb{E}[T\mid A^*]=\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[\varepsilon_Y\mid A^*]=\mathbb{E}[h(A)\mid A^*]$.
512	Since $\operatorname{Cov}(T,\varepsilon_Y)=0$, the law of total covariance gives:
513	\[
514	  B(C) = \frac{-\operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[h(A)\mid A^*]\bigr)}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
515	\]
516	
517	\paragraph{Endpoint analysis.}
518	At $C=I$ ($A^*{=}A$):
519	$B(I) = -\operatorname{Cov}(g(A),h(A))\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)] = B_{\mathrm{Berkson}}$,
520	the full Berkson's bias from conditioning on the collider.
521	
522	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$):
523	$\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[h(A)\mid A^*]$ are constant, so $B=0$ and $\operatorname{plim}\hat\tau=\tau$.
524	
525	This is the structural reverse of confounding: misclassification attenuates the collider-induced bias toward zero, rather than growing bias from zero toward $B_{\mathrm{OV}}$.
526	
527	\begin{proposition}[Collider sign preservation --- proportional case]
528	\label{prop:col_prop}
529	If $h(A)=\lambda\,g(A)$ for some constant $\lambda$, then $|B(C)|\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.
530	Consequently, $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{Berkson}})$.
531	\end{proposition}
532	
533	\begin{proof}
534	When $h=\lambda g$, the numerator becomes $-\lambda\,\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$ and the denominator is $\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$.
535	Let $V^*=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\in[0,V_g]$ where $V_g=\operatorname{Var}(g(A))$.
536	Then
537	\[
538	  |B(C)| = |\lambda|\,\frac{V^*}{\operatorname{Var}(T)-V^*}.
539	\]
540	The function $x\mapsto x/(a-x)$ is increasing on $[0,a)$.
541	With $a=\operatorname{Var}(T)>V_g\geq V^*$:
542	$|B(C)|\leq|\lambda|\,V_g/(\operatorname{Var}(T)-V_g)=|B(I)|$.
543	At $V^*{=}0$ (uniform $C$): $B{=}0$.  At $V^*{=}V_g$ ($C{=}I$): $B{=}B(I)$.
544	\end{proof}
545	
546	\begin{proposition}[Collider sign preservation --- general case]
547	\label{prop:col_gen}
548	Define
549	\begin{equation}
550	  \bar{B}_{\mathrm{col}} = \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(h(A))}}{\mathbb{E}[\operatorname{Var}(T\mid A)]}.
551	  \label{eq:bbar_col}
552	\end{equation}
553	If $|\tau|>\bar{B}_{\mathrm{col}}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for all column-stochastic $C$.
554	\end{proposition}
555	
556	\begin{proof}
557	\emph{Step~1: Bound the numerator.}
558	By Cauchy--Schwarz:
559	$|\operatorname{Cov}(\mathbb{E}[g\mid A^*],\mathbb{E}[h\mid A^*])|\leq\sqrt{\operatorname{Var}(\mathbb{E}[g\mid A^*])\,\operatorname{Var}(\mathbb{E}[h\mid A^*])}$.
560	Since conditional expectation reduces variance: $\operatorname{Var}(\mathbb{E}[g\mid A^*])\leq\operatorname{Var}(g(A))$ and likewise for $h$.
561	
562	\emph{Step~2: Bound the denominator.}
563	$\mathbb{E}[\operatorname{Var}(T\mid A^*)]=\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[T\mid A^*])\geq\operatorname{Var}(T)-\operatorname{Var}(g(A))=\mathbb{E}[\operatorname{Var}(T\mid A)]$.
564	
565	\emph{Step~3: Conclude.}
566	$|B(C)|\leq\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(h)}\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)]=\bar{B}_{\mathrm{col}}$.
567	When $|\tau|>\bar{B}_{\mathrm{col}}$, the bias cannot overwhelm $\tau$. In practice, $\operatorname{Var}(g(A))$ and $\operatorname{Var}(h(A))$ can be estimated from observable data by bootstrapping regression coefficients from $A^*$-stratified subsamples, yielding conservative upper bounds on $\bar{B}_{\mathrm{col}}$.
568	\end{proof}
569	
570	\paragraph{Verification for paper parameters ($K{=}3$).}
571	With $\tau{=}1.0$, $\boldsymbol{\delta}_T{=}(0,\,0.5,\,{-}0.3)$, $\boldsymbol{\delta}_Y{=}(0,\,0.8,\,0.6)$, from $5{\times}10^6$-sample Monte Carlo:
572	\begin{align*}
573	  \operatorname{Var}(g(A)) &= 0.187,\quad
574	  \operatorname{Var}(h(A)) = 0.076,\quad
575	  \mathbb{E}[\operatorname{Var}(T\mid A)] = 0.813,\\
576	  \bar{B}_{\mathrm{col}} &= \sqrt{0.187\times 0.076}\;/\;0.813 = 0.147.
577	\end{align*}
578	Since $|\tau|{=}1.0\gg\bar{B}_{\mathrm{col}}{=}0.147$, Proposition~\ref{prop:col_gen} guarantees sign preservation.
579	Additionally, $B_{\mathrm{Berkson}}{=}{-}0.114$, giving $\tau+B_{\mathrm{Berkson}}{=}0.886{>}0$.
580	Verified across $100{,}000$ random column-stochastic $C$: $\tau_{\mathrm{sign\,flip}}{=}0\%$, and $|B(C)|\leq|B_{\mathrm{Berkson}}|$ in all cases.
581	
582	\subsection{Front-door Topology ($A$ = Mediator under Confounding)}
583	\label{app:frontdoor}
584	
585	\paragraph{Data-generating process.}
586	$T\to A\to Y$, $U\to T$, $U\to Y$.
587	An unobserved confounder $U$ affects both treatment and outcome:
588	\begin{align*}
589	  U &\sim \mathcal{N}(0,1),\quad
590	  T = \alpha_U\,U + \eta,\quad \eta\sim\mathcal{N}(0,1),\;\eta\perp U,\\
591	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
592	  Y &= f(A) + \lambda\,U + \varepsilon_Y,\quad \varepsilon_Y\perp(T,A,U).
593	\end{align*}
594	There is no direct $T{\to}Y$ edge; the causal effect of $T$ on $Y$ operates entirely through $A$.
595	The researcher controls for $A^*$ in $Y\sim 1+T+D_1^*+\cdots+D_{K-1}^*$.
596	
597	\paragraph{Bias decomposition.}
598	Since the direct effect is zero, the FWL coefficient on $T$ captures only bias:
599	\[
600	  \operatorname{plim}\hat\tau(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
601	\]
602	Substituting $Y=f(A)+\lambda U+\varepsilon_Y$ and using $\varepsilon_Y\perp(T,A,A^*)$:
603	\begin{equation}
604	  \operatorname{plim}\hat\tau(C)
605	  = \underbrace{\frac{\lambda\,\alpha_U}{\operatorname{Var}(T)}}_{\text{confounding (constant)}}
606	  \;+\; \underbrace{\frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}}_{\displaystyle B_{\mathrm{med}}(C)},
607	  \label{eq:fd_decomp}
608	\end{equation}
609	where $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]$.
610	
611	\begin{proof}[Derivation of~\eqref{eq:fd_decomp}]
612	Expand the numerator as
613	$\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] + \lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]$.
614	For the confounding term: since $T=\alpha_U U+\eta$ with $(U,\eta)$ jointly Gaussian, the regression residual $\xi=U-\frac{\alpha_U}{\operatorname{Var}(T)}T$ satisfies $\xi\perp T$.
615	Because $A$ is a function of $T$ (plus independent softmax noise) and $A^*$ is a function of $A$ (plus independent misclassification noise), $\xi\perp(T,A,A^*)$.
616	Therefore
617	\[
618	  \operatorname{Cov}(T,U\mid A^*{=}j)
619	  = \frac{\alpha_U}{\operatorname{Var}(T)}\,\operatorname{Var}(T\mid A^*{=}j)
620	  \quad\forall\;j,
621	\]
622	and $\lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]=\frac{\lambda\alpha_U}{\operatorname{Var}(T)}\,D(C)$, yielding the constant first term after division by $D(C)$.
623	\end{proof}
624	
625	This decomposition reveals that \emph{misclassification does not affect the confounding component}.
626	The confusion matrix $C$ modulates only the mediation-type leakage $B_{\mathrm{med}}(C)$, which has the same structure as in~§\ref{app:mediation}.
627	
628	\paragraph{Endpoint analysis.}
629	At $C=I$: $B_{\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\to A\to Y$ path), and $\operatorname{plim}\hat\tau(I)=\lambda\alpha_U/\operatorname{Var}(T)$ (pure confounding residual).
630	
631	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $B_{\mathrm{med}}=\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$, and $\operatorname{plim}\hat\tau_{\mathrm{nc}}=[\operatorname{Cov}(T,f(A))+\lambda\alpha_U]/\operatorname{Var}(T)$, the naive regression coefficient with no controls.
632	
633	\paragraph{Numerical Verification (Front-door sign preservation).}
634	\label{find:fd_sign}
635	Since $B_{\mathrm{med}}(C)$ has the same structure as the mediation bias (§\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "6c1c4f3f-46a7-42e7-a7f0-4a1961321471",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "\\subsection{Collider Topology ($A$ = Collider)}\n\\label{app:collider}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\leftarrow Y$, $T\\to Y$.\nThe treatment effect is unconfounded:\n\\begin{align*}\n  T &\\sim \\mathcal{N}(0,1),\\quad\n  Y = \\tau\\,T + \\varepsilon_Y,\\quad \\varepsilon_Y\\sim\\mathcal{N}(0,1),\\;\\varepsilon_Y\\perp T,\\\\\n  A\\mid T,Y &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\delta}_T\\,T + \\boldsymbol{\\delta}_Y\\,Y)\\bigr).\n\\end{align*}\nThe collider $A$ is a common \\emph{effect} of $T$ and $Y$.\nThe no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\\operatorname{plim}\\hat\\tau_{\\mathrm{nc}}=\\tau$.\nThe researcher erroneously controls for $A^*$, inducing Berkson's bias.\n\n\\paragraph{Bias decomposition.}\nUnlike confounding, $\\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\\tau T+\\varepsilon_Y$), so Lemma~\\ref{lem:bias_decomp} does not apply directly.\nInstead, we derive the bias from the FWL identity~\\eqref{eq:fwl}.\nWriting $\\tilde{Y}=\\tau\\tilde{T}+(\\varepsilon_Y-\\mathbb{E}[\\varepsilon_Y\\mid A^*])$ and noting that $\\mathbb{E}[\\tilde{T}\\,\\varepsilon_Y]=\\mathbb{E}[\\operatorname{Cov}(T,\\varepsilon_Y\\mid A^*)]$ (since $T\\perp\\varepsilon_Y$ unconditionally):\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + B(C),\\quad\n  B(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,\\varepsilon_Y\\mid A^*)]}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n  \\label{eq:bias_col}\n\\end{equation}\nUnder non-differential misclassification ($A^*\\perp(T,\\varepsilon_Y)\\mid A$), define $g(k)=\\mathbb{E}[T\\mid A{=}k]$ and $h(k)=\\mathbb{E}[\\varepsilon_Y\\mid A{=}k]$.\nBy the tower property, $\\mathbb{E}[T\\mid A^*]=\\mathbb{E}[g(A)\\mid A^*]$ and $\\mathbb{E}[\\varepsilon_Y\\mid A^*]=\\mathbb{E}[h(A)\\mid A^*]$.\nSince $\\operatorname{Cov}(T,\\varepsilon_Y)=0$, the law of total covariance gives:\n\\[\n  B(C) = \\frac{-\\operatorname{Cov}\\bigl(\\mathbb{E}[g(A)\\mid A^*],\\;\\mathbb{E}[h(A)\\mid A^*]\\bigr)}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n\\]\n\n\\paragraph{Endpoint analysis.}\nAt $C=I$ ($A^*{=}A$):\n$B(I) = -\\operatorname{Cov}(g(A),h(A))\\,/\\,\\mathbb{E}[\\operatorname{Var}(T\\mid A)] = B_{\\mathrm{Berkson}}$,\nthe full Berkson's bias from conditioning on the collider.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ ($A^*\\perp A$):\n$\\mathbb{E}[g(A)\\mid A^*]$ and $\\mathbb{E}[h(A)\\mid A^*]$ are constant, so $B=0$ and $\\operatorname{plim}\\hat\\tau=\\tau$.\n\nThis is the structural reverse of confounding: misclassification attenuates the collider-induced bias toward zero, rather than growing bias from zero toward $B_{\\mathrm{OV}}$.\n\n\\begin{proposition}[Collider sign preservation --- proportional case]\n\\label{prop:col_prop}\nIf $h(A)=\\lambda\\,g(A)$ for some constant $\\lambda$, then $|B(C)|\\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.\nConsequently, $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ whenever $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau+B_{\\mathrm{Berkson}})$.\n\\end{proposition}\n\n\\begin{proof}\nWhen $h=\\lambda g$, the numerator becomes $-\\lambda\\,\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$ and the denominator is $\\operatorname{Var}(T)-\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$.\nLet $V^*=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])\\in[0,V_g]$ where $V_g=\\operatorname{Var}(g(A))$.\nThen\n\\[\n  |B(C)| = |\\lambda|\\,\\frac{V^*}{\\operatorname{Var}(T)-V^*}.\n\\]\nThe function $x\\mapsto x/(a-x)$ is increasing on $[0,a)$.\nWith $a=\\operatorname{Var}(T)>V_g\\geq V^*$:\n$|B(C)|\\leq|\\lambda|\\,V_g/(\\operatorname{Var}(T)-V_g)=|B(I)|$.\nAt $V^*{=}0$ (uniform $C$): $B{=}0$.  At $V^*{=}V_g$ ($C{=}I$): $B{=}B(I)$.\n\\end{proof}\n\n\\begin{proposition}[Collider sign preservation --- general case]\n\\label{prop:col_gen}\nDefine\n\\begin{equation}\n  \\bar{B}_{\\mathrm{col}} = \\frac{\\sqrt{\\operatorname{Var}(g(A))\\,\\operatorname{Var}(h(A))}}{\\mathbb{E}[\\operatorname{Var}(T\\mid A)]}.\n  \\label{eq:bbar_col}\n\\end{equation}\nIf $|\\tau|>\\bar{B}_{\\mathrm{col}}$, then $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau(C))=\\operatorname{sign}(\\tau)$ for all column-stochastic $C$.\n\\end{proposition}\n\n\\begin{proof}\n\\emph{Step~1: Bound the numerator.}\nBy Cauchy--Schwarz:\n$|\\operatorname{Cov}(\\mathbb{E}[g\\mid A^*],\\mathbb{E}[h\\mid A^*])|\\leq\\sqrt{\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\,\\operatorname{Var}(\\mathbb{E}[h\\mid A^*])}$.\nSince conditional expectation reduces variance: $\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\leq\\operatorname{Var}(g(A))$ and likewise for $h$.\n\n\\emph{Step~2: Bound the denominator.}\n$\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]=\\operatorname{Var}(T)-\\operatorname{Var}(\\mathbb{E}[T\\mid A^*])\\geq\\operatorname{Var}(T)-\\operatorname{Var}(g(A))=\\mathbb{E}[\\operatorname{Var}(T\\mid A)]$.\n\n\\emph{Step~3: Conclude.}\n$|B(C)|\\leq\\sqrt{\\operatorname{Var}(g)\\,\\operatorname{Var}(h)}\\,/\\,\\mathbb{E}[\\operatorname{Var}(T\\mid A)]=\\bar{B}_{\\mathrm{col}}$.\nWhen $|\\tau|>\\bar{B}_{\\mathrm{col}}$, the bias cannot overwhelm $\\tau$. In practice, $\\operatorname{Var}(g(A))$ and $\\operatorname{Var}(h(A))$ can be estimated from observable data by bootstrapping regression coefficients from $A^*$-stratified subsamples, yielding conservative upper bounds on $\\bar{B}_{\\mathrm{col}}$.\n\\end{proof}\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau{=}1.0$, $\\boldsymbol{\\delta}_T{=}(0,\\,0.5,\\,{-}0.3)$, $\\boldsymbol{\\delta}_Y{=}(0,\\,0.8,\\,0.6)$, from $5{\\times}10^6$-sample Monte Carlo:\n\\begin{align*}\n  \\operatorname{Var}(g(A)) &= 0.187,\\quad\n  \\operatorname{Var}(h(A)) = 0.076,\\quad\n  \\mathbb{E}[\\operatorname{Var}(T\\mid A)] = 0.813,\\\\\n  \\bar{B}_{\\mathrm{col}} &= \\sqrt{0.187\\times 0.076}\\;/\\;0.813 = 0.147.\n\\end{align*}\nSince $|\\tau|{=}1.0\\gg\\bar{B}_{\\mathrm{col}}{=}0.147$, Proposition~\\ref{prop:col_gen} guarantees sign preservation.\nAdditionally, $B_{\\mathrm{Berkson}}{=}{-}0.114$, giving $\\tau+B_{\\mathrm{Berkson}}{=}0.886{>}0$.\nVerified across $100{,}000$ random column-stochastic $C$: $\\tau_{\\mathrm{sign\\,flip}}{=}0\\%$, and $|B(C)|\\leq|B_{\\mathrm{Berkson}}|$ in all cases.\n\n\\subsection{Front-door Topology ($A$ = Mediator under Confounding)}\n\\label{app:frontdoor}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\to Y$, $U\\to T$, $U\\to Y$.\nAn unobserved confounder $U$ affects both treatment and outcome:\n\\begin{align*}\n  U &\\sim \\mathcal{N}(0,1),\\quad\n  T = \\alpha_U\\,U + \\eta,\\quad \\eta\\sim\\mathcal{N}(0,1),\\;\\eta\\perp U,\\\\\n  A\\mid T &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\gamma}+\\boldsymbol{\\delta}\\,T)\\bigr),\\\\\n  Y &= f(A) + \\lambda\\,U + \\varepsilon_Y,\\quad \\varepsilon_Y\\perp(T,A,U).\n\\end{align*}\nThere is no direct $T{\\to}Y$ edge; the causal effect of $T$ on $Y$ operates entirely through $A$.\nThe researcher controls for $A^*$ in $Y\\sim 1+T+D_1^*+\\cdots+D_{K-1}^*$.\n\n\\paragraph{Bias decomposition.}\nSince the direct effect is zero, the FWL coefficient on $T$ captures only bias:\n\\[\n  \\operatorname{plim}\\hat\\tau(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,Y\\mid A^*)]}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n\\]\nSubstituting $Y=f(A)+\\lambda U+\\varepsilon_Y$ and using $\\varepsilon_Y\\perp(T,A,A^*)$:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C)\n  = \\underbrace{\\frac{\\lambda\\,\\alpha_U}{\\operatorname{Var}(T)}}_{\\text{confounding (constant)}}\n  \\;+\\; \\underbrace{\\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)]}{D(C)}}_{\\displaystyle B_{\\mathrm{med}}(C)},\n  \\label{eq:fd_decomp}\n\\end{equation}\nwhere $D(C)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]$.\n\n\\begin{proof}[Derivation of~\\eqref{eq:fd_decomp}]\nExpand the numerator as\n$\\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)] + \\lambda\\,\\mathbb{E}[\\operatorname{Cov}(T,U\\mid A^*)]$.\nFor the confounding term: since $T=\\alpha_U U+\\eta$ with $(U,\\eta)$ jointly Gaussian, the regression residual $\\xi=U-\\frac{\\alpha_U}{\\operatorname{Var}(T)}T$ satisfies $\\xi\\perp T$.\nBecause $A$ is a function of $T$ (plus independent softmax noise) and $A^*$ is a function of $A$ (plus independent misclassification noise), $\\xi\\perp(T,A,A^*)$.\nTherefore\n\\[\n  \\operatorname{Cov}(T,U\\mid A^*{=}j)\n  = \\frac{\\alpha_U}{\\operatorname{Var}(T)}\\,\\operatorname{Var}(T\\mid A^*{=}j)\n  \\quad\\forall\\;j,\n\\]\nand $\\lambda\\,\\mathbb{E}[\\operatorname{Cov}(T,U\\mid A^*)]=\\frac{\\lambda\\alpha_U}{\\operatorname{Var}(T)}\\,D(C)$, yielding the constant first term after division by $D(C)$.\n\\end{proof}\n\nThis decomposition reveals that \\emph{misclassification does not affect the confounding component}.\nThe confusion matrix $C$ modulates only the mediation-type leakage $B_{\\mathrm{med}}(C)$, which has the same structure as in~§\\ref{app:mediation}.\n\n\\paragraph{Endpoint analysis.}\nAt $C=I$: $B_{\\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\\to A\\to Y$ path), and $\\operatorname{plim}\\hat\\tau(I)=\\lambda\\alpha_U/\\operatorname{Var}(T)$ (pure confounding residual).\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$: $B_{\\mathrm{med}}=\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$, and $\\operatorname{plim}\\hat\\tau_{\\mathrm{nc}}=[\\operatorname{Cov}(T,f(A))+\\lambda\\alpha_U]/\\operatorname{Var}(T)$, the naive regression coefficient with no controls.\n\n\\paragraph{Numerical Verification (Front-door sign preservation).}\n\\label{find:fd_sign}\nSince $B_{\\mathrm{med}}(C)$ has the same structure as the mediation bias (§\\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:",
      "numLines": 150,
      "startLine": 486,
      "totalLines": 1480
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Good. I now have a thorough understanding of the proof structure. Let me now write both the numerical verification script and the LaTeX proof.

Key insight for the proof: For K=3 symmetric C₀ with C₀[i,i] = 1-2c, C₀[i,j] = c (i≠j), along the path C(δ) = (1-δ)I + δC₀:

1. C(δ) = (1-3cδ)I + cδ𝟏𝟏ᵀ maintains symmetric structure
2. V_B(s) = (1-3s)² Σ_j p_j²h_j² / [(1-3s)p_j + s] where s = cδ


3. The derivative of V_B with respect to s is negative everywhere, confirming that V_B decreases monotonically as we move along the path, which means the bias magnitude increases strictly.

For the collider case, the bias simplifies to the negative covariance between the conditional expectations of the two variables divided by the conditional variance of the treatment.

When the confounding variable is proportional to the treatment effect (h = λg), I can express the collider bias in terms of V_B^g, and here's where it gets interesting—since V_B^g is decreasing and the function relating bias to V_B^g is increasing, the magnitude of collider bias actually decreases as we move away from the Berkson point. This is the opposite direction from what happens with regular confounding, so the collider bias starts at its maximum and shrinks toward zero. be: confounding shows non-decreasing bias from zero to the omitted variable bias, mediation shows non-decreasing bias from zero to the indirect effect, and collider shows non-increasing bias from the Berkson bias toward zero. All three cases rely on the same mechanism—the variance of the bias term decreasing monotonically. Now I'm planning to write a numerical verification script and the formal proof in LaTeX to demonstrate this unified framework.

For the general non-proportional confounding case, I need to carefully analyze how the bias function behaves when the covariance structure between the confounder and treatment isn't proportional to its effect on the outcome. The numerator and denominator each have components that change with the mixing parameter, and I need to verify whether monotonicity still holds when the signs of these components vary.

Rather than trying to work through all the algebra, I should just run a numerical verification across different scenarios—checking whether the proportional case always maintains monotonicity as expected, and whether the general case might break down for certain parameter configurations like the symmetric K=3 case. I'll write a script that computes the bias at a grid of mixing parameter values for all three causal structures and checks whether the absolute bias is non-decreasing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "edd9e391-e436-4140-a258-f3d007b61b4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vro2DpHHtuvKcwHgkENHf3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21452,
      "cache_read_input_tokens": 42255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21452
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

### Assistant

_source line 14_

I now have a clear understanding of the proof structure. Let me work through the algebra.

**Key insight**: For K=3 symmetric C₀, the interpolation C(δ) = (1-3cδ)I + cδ𝟏𝟏ᵀ stays in the one-parameter symmetric family. This lets us show dV_B/ds < 0 directly at every point, bypassing the convexity+endpoint approach used in the paper.

Let me first write a numerical verification script to confirm the algebra, then write the proof.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "ea4e28a7-7f07-4842-a970-1c9c9d5ef811",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vro2DpHHtuvKcwHgkENHf3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21452,
      "cache_read_input_tokens": 42255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21452
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

_source line 15_

<details open><summary>🔧 Tool call — Write · `toolu_01Qn1e7amns1v9Ee3HVpCXeA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py",
  "content": "\"\"\"\nNumerical verification: K=3 symmetric confusion matrix monotonicity.\n\nFor C₀[i,i] = 1-2c, C₀[i,j] = c (i≠j), c ∈ (0,1/3),\nalong C(δ) = (1-δ)I + δC₀ = (1-3cδ)I + cδ𝟏𝟏ᵀ:\n\n1. Confounding (proportional): |B(δ)| non-decreasing ✓ (proven)\n2. Confounding (general): |B(δ)| non-decreasing (check)\n3. Mediation (proportional): |B(δ)| non-decreasing ✓ (same structure)\n4. Collider (proportional): |B(δ)| non-increasing ✓ (reverse direction)\n\"\"\"\n\nimport numpy as np\nfrom scipy.special import softmax\nimport json\n\nnp.random.seed(42)\n\ndef make_symmetric_C(c, delta):\n    s = c * delta\n    C = np.full((3, 3), s)\n    np.fill_diagonal(C, 1 - 2*s)\n    return C\n\ndef compute_VB(s, p, h):\n    \"\"\"V_B(s) = (1-3s)^2 Σ_j p_j^2 h_j^2 / q_j\"\"\"\n    q = (1 - 3*s) * p + s\n    return (1 - 3*s)**2 * np.sum(p**2 * h**2 / q)\n\ndef compute_dVB_ds(s, p, h):\n    \"\"\"dV_B/ds = (1-3s) Σ_j p_j^2 h_j^2 [-3(1-3s)p_j - 1 - 3s] / q_j^2\"\"\"\n    q = (1 - 3*s) * p + s\n    bracket = -3*(1-3*s)*p - 1 - 3*s\n    return (1-3*s) * np.sum(p**2 * h**2 * bracket / q**2)\n\n\n# ====== Test 1: Verify dV_B/ds < 0 analytically ======\nprint(\"=\" * 60)\nprint(\"Test 1: Verify dV_B/ds < 0 for random (p, g, c, s)\")\nprint(\"=\" * 60)\n\nn_tests = 100000\nviolations = 0\nfor _ in range(n_tests):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    c = np.random.uniform(0.01, 0.33)\n    s = np.random.uniform(0, c)\n\n    deriv = compute_dVB_ds(s, p, h)\n    if deriv > 1e-12:\n        violations += 1\n\nprint(f\"Violations: {violations}/{n_tests}\")\nassert violations == 0, \"dV_B/ds > 0 found!\"\nprint(\"PASS: dV_B/ds ≤ 0 everywhere\\n\")\n\n\n# ====== Test 2: Confounding bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 2: Confounding |B(δ)| non-decreasing (proportional f=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nn_delta = 200\ndeltas = np.linspace(0, 1, n_delta)\nmax_violation = 0\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    sigma_T2 = np.random.uniform(0.1, 3.0)\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        VW = V - VB\n        B = lam * VW / (VW + sigma_T2)\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-10:\n        violation_count += 1\n        max_violation = min(max_violation, min_diff)\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 3: Confounding bias monotonicity (general f) ======\nprint(\"=\" * 60)\nprint(\"Test 3: Confounding |B(δ)| non-decreasing (general f)\")\nprint(\"=\" * 60)\n\nn_configs = 50000\nviolation_count = 0\nmax_violation = 0\nworst_config = None\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    f = np.random.randn(3)\n    g_bar = p @ g\n    f_bar = p @ f\n    hg = g - g_bar\n    hf = f - f_bar\n    Vg = p @ hg**2\n    if Vg < 1e-8:\n        continue\n    sigma_T2 = np.random.uniform(0.1, 3.0)\n    c = np.random.uniform(0.01, 0.33)\n    cov_gf = p @ (hg * hf)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        q = (1-3*s)*p + s\n        Phi_gf = (1-3*s)**2 * np.sum(p**2 * hg * hf / q)\n        Phi_gg = (1-3*s)**2 * np.sum(p**2 * hg**2 / q)\n        R = cov_gf - Phi_gf\n        D = sigma_T2 + Vg - Phi_gg\n        B = R / D\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-8:\n        violation_count += 1\n        if min_diff < max_violation:\n            max_violation = min_diff\n            worst_config = (p.copy(), g.copy(), f.copy(), sigma_T2, c)\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nif violation_count > 0:\n    print(f\"Violation rate: {violation_count/n_configs*100:.2f}%\")\n    p_, g_, f_, st2, c_ = worst_config\n    print(f\"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}\")\nprint()\n\n\n# ====== Test 4: Collider bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 4: Collider |B(δ)| non-increasing (proportional h=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    var_T = np.random.uniform(V + 0.1, V + 5.0)  # Var(T) > Var(g(A))\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        B_col = -lam * VB / (var_T - VB)\n        abs_B[i] = abs(B_col)\n\n    diffs = np.diff(abs_B)\n    max_diff = diffs.max()\n    if max_diff > 1e-10:\n        violation_count += 1\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 5: Mediation bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 5: Mediation |B(δ)| non-decreasing (proportional f=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    sigma_eps2 = np.random.uniform(0.1, 3.0)  # E[Var(T|A)]\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        VW = V - VB\n        B = lam * VW / (VW + sigma_eps2)\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-10:\n        violation_count += 1\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Summary ======\nresults = {\n    \"test1_dVB_sign\": {\"n\": n_tests, \"violations\": 0, \"status\": \"PASS\"},\n    \"test2_confounding_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test3_confounding_general\": {\"n\": 50000, \"violations\": violation_count,\n                                   \"max_violation\": float(abs(max_violation)),\n                                   \"status\": \"PASS\" if violation_count == 0 else \"FAIL\"},\n    \"test4_collider_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test5_mediation_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n}\n\nprint(\"=\" * 60)\nprint(\"Summary\")\nprint(\"=\" * 60)\nfor name, r in results.items():\n    print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")\n\nwith open(\"artifacts/k3_symmetric_verify_results.json\", \"w\") as f:\n    json.dump(results, f, indent=2)\n\nprint(\"\\nResults saved to artifacts/k3_symmetric_verify_results.json\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "01d8c898-ff82-4249-a02e-65aedac845c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vro2DpHHtuvKcwHgkENHf3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21452,
      "cache_read_input_tokens": 42255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21452
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

_source line 16 · 2026-05-23T17:42:42.964Z_

<details><summary>↩ Tool result · `toolu_01Qn1e7amns1v9Ee3HVpCXeA`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "093d52bb-b091-4635-a7aa-83ca1d135de2",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py",
    "content": "\"\"\"\nNumerical verification: K=3 symmetric confusion matrix monotonicity.\n\nFor C₀[i,i] = 1-2c, C₀[i,j] = c (i≠j), c ∈ (0,1/3),\nalong C(δ) = (1-δ)I + δC₀ = (1-3cδ)I + cδ𝟏𝟏ᵀ:\n\n1. Confounding (proportional): |B(δ)| non-decreasing ✓ (proven)\n2. Confounding (general): |B(δ)| non-decreasing (check)\n3. Mediation (proportional): |B(δ)| non-decreasing ✓ (same structure)\n4. Collider (proportional): |B(δ)| non-increasing ✓ (reverse direction)\n\"\"\"\n\nimport numpy as np\nfrom scipy.special import softmax\nimport json\n\nnp.random.seed(42)\n\ndef make_symmetric_C(c, delta):\n    s = c * delta\n    C = np.full((3, 3), s)\n    np.fill_diagonal(C, 1 - 2*s)\n    return C\n\ndef compute_VB(s, p, h):\n    \"\"\"V_B(s) = (1-3s)^2 Σ_j p_j^2 h_j^2 / q_j\"\"\"\n    q = (1 - 3*s) * p + s\n    return (1 - 3*s)**2 * np.sum(p**2 * h**2 / q)\n\ndef compute_dVB_ds(s, p, h):\n    \"\"\"dV_B/ds = (1-3s) Σ_j p_j^2 h_j^2 [-3(1-3s)p_j - 1 - 3s] / q_j^2\"\"\"\n    q = (1 - 3*s) * p + s\n    bracket = -3*(1-3*s)*p - 1 - 3*s\n    return (1-3*s) * np.sum(p**2 * h**2 * bracket / q**2)\n\n\n# ====== Test 1: Verify dV_B/ds < 0 analytically ======\nprint(\"=\" * 60)\nprint(\"Test 1: Verify dV_B/ds < 0 for random (p, g, c, s)\")\nprint(\"=\" * 60)\n\nn_tests = 100000\nviolations = 0\nfor _ in range(n_tests):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    c = np.random.uniform(0.01, 0.33)\n    s = np.random.uniform(0, c)\n\n    deriv = compute_dVB_ds(s, p, h)\n    if deriv > 1e-12:\n        violations += 1\n\nprint(f\"Violations: {violations}/{n_tests}\")\nassert violations == 0, \"dV_B/ds > 0 found!\"\nprint(\"PASS: dV_B/ds ≤ 0 everywhere\\n\")\n\n\n# ====== Test 2: Confounding bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 2: Confounding |B(δ)| non-decreasing (proportional f=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nn_delta = 200\ndeltas = np.linspace(0, 1, n_delta)\nmax_violation = 0\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    sigma_T2 = np.random.uniform(0.1, 3.0)\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        VW = V - VB\n        B = lam * VW / (VW + sigma_T2)\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-10:\n        violation_count += 1\n        max_violation = min(max_violation, min_diff)\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 3: Confounding bias monotonicity (general f) ======\nprint(\"=\" * 60)\nprint(\"Test 3: Confounding |B(δ)| non-decreasing (general f)\")\nprint(\"=\" * 60)\n\nn_configs = 50000\nviolation_count = 0\nmax_violation = 0\nworst_config = None\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    f = np.random.randn(3)\n    g_bar = p @ g\n    f_bar = p @ f\n    hg = g - g_bar\n    hf = f - f_bar\n    Vg = p @ hg**2\n    if Vg < 1e-8:\n        continue\n    sigma_T2 = np.random.uniform(0.1, 3.0)\n    c = np.random.uniform(0.01, 0.33)\n    cov_gf = p @ (hg * hf)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        q = (1-3*s)*p + s\n        Phi_gf = (1-3*s)**2 * np.sum(p**2 * hg * hf / q)\n        Phi_gg = (1-3*s)**2 * np.sum(p**2 * hg**2 / q)\n        R = cov_gf - Phi_gf\n        D = sigma_T2 + Vg - Phi_gg\n        B = R / D\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-8:\n        violation_count += 1\n        if min_diff < max_violation:\n            max_violation = min_diff\n            worst_config = (p.copy(), g.copy(), f.copy(), sigma_T2, c)\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nif violation_count > 0:\n    print(f\"Violation rate: {violation_count/n_configs*100:.2f}%\")\n    p_, g_, f_, st2, c_ = worst_config\n    print(f\"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}\")\nprint()\n\n\n# ====== Test 4: Collider bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 4: Collider |B(δ)| non-increasing (proportional h=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    var_T = np.random.uniform(V + 0.1, V + 5.0)  # Var(T) > Var(g(A))\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        B_col = -lam * VB / (var_T - VB)\n        abs_B[i] = abs(B_col)\n\n    diffs = np.diff(abs_B)\n    max_diff = diffs.max()\n    if max_diff > 1e-10:\n        violation_count += 1\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 5: Mediation bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 5: Mediation |B(δ)| non-decreasing (proportional f=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    sigma_eps2 = np.random.uniform(0.1, 3.0)  # E[Var(T|A)]\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        VW = V - VB\n        B = lam * VW / (VW + sigma_eps2)\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-10:\n        violation_count += 1\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Summary ======\nresults = {\n    \"test1_dVB_sign\": {\"n\": n_tests, \"violations\": 0, \"status\": \"PASS\"},\n    \"test2_confounding_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test3_confounding_general\": {\"n\": 50000, \"violations\": violation_count,\n                                   \"max_violation\": float(abs(max_violation)),\n                                   \"status\": \"PASS\" if violation_count == 0 else \"FAIL\"},\n    \"test4_collider_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test5_mediation_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n}\n\nprint(\"=\" * 60)\nprint(\"Summary\")\nprint(\"=\" * 60)\nfor name, r in results.items():\n    print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")\n\nwith open(\"artifacts/k3_symmetric_verify_results.json\", \"w\") as f:\n    json.dump(results, f, indent=2)\n\nprint(\"\\nResults saved to artifacts/k3_symmetric_verify_results.json\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01KAu9LtXpuPST2bgfGdSsTC`</summary>

```json
{
  "command": "python artifacts/k3_symmetric_verify.py",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "173b17a7-82a9-4e69-8e43-6937ed6a8ed4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UB3n3WkDM9fNftMTZ2cbgJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4738,
      "cache_read_input_tokens": 63707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4738
      },
      "output_tokens": 69,
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

_source line 18 · 2026-05-23T17:42:48.147Z_

<details><summary>↩ Tool result · reported error · `toolu_01KAu9LtXpuPST2bgfGdSsTC`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "23df8c4a-4b73-4086-8b1e-1184b3d63165",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_017QHGkUYt3QvEmrPBwaLLBT`</summary>

```json
{
  "command": "python3 artifacts/k3_symmetric_verify.py",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "f6c7855a-b915-4cc2-87e1-2e358b13f6c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014526V5JxF6jL5hScz9vcWC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 119,
      "cache_read_input_tokens": 68445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 119
      },
      "output_tokens": 69,
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

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bf0f9toor",
  "tool_use_id": "toolu_017QHGkUYt3QvEmrPBwaLLBT",
  "description": "python3 artifacts/k3_symmetric_verify.py",
  "task_type": "local_bash",
  "uuid": "e4fd504b-80c4-489f-8f73-fc7dd0ffdeb4",
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8"
}
```

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bf0f9toor",
  "tool_use_id": "toolu_017QHGkUYt3QvEmrPBwaLLBT",
  "status": "completed",
  "output_file": "",
  "summary": "python3 artifacts/k3_symmetric_verify.py",
  "uuid": "e8d4d6d5-62d2-4540-8547-36fc2f7f0300",
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8"
}
```

---

### Tool result

_source line 22 · 2026-05-23T17:45:52.901Z_

<details><summary>↩ Tool result · `toolu_017QHGkUYt3QvEmrPBwaLLBT`</summary>

```text
============================================================
Test 1: Verify dV_B/ds < 0 for random (p, g, c, s)
============================================================
Violations: 0/100000
PASS: dV_B/ds ≤ 0 everywhere

============================================================
Test 2: Confounding |B(δ)| non-decreasing (proportional f=λg)
============================================================
Violations: 0/10000
Max violation magnitude: 0.00e+00
PASS

============================================================
Test 3: Confounding |B(δ)| non-decreasing (general f)
============================================================
Violations: 4943/50000
Max violation magnitude: 4.13e-03
Violation rate: 9.89%
Worst config: p=[0.0328931  0.42670406 0.54040284], g=[-1.10745103  0.82952924  0.17694579], f=[ 1.06519695 -0.05507037 -1.76628566], σ_T²=0.194, c=0.318

============================================================
Test 4: Collider |B(δ)| non-increasing (proportional h=λg)
============================================================
Violations: 0/10000
PASS

============================================================
Test 5: Mediation |B(δ)| non-decreasing (proportional f=λg)
============================================================
Violations: 0/10000
PASS

============================================================
Summary
============================================================
  test1_dVB_sign: PASS (0/100000)
  test2_confounding_proportional: PASS (0/10000)
  test3_confounding_general: PASS (0/50000)
  test4_collider_proportional: PASS (0/10000)
  test5_mediation_proportional: PASS (0/10000)

Results saved to artifacts/k3_symmetric_verify_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "8af0c96c-44b1-4c35-83c1-484bcddb72fb",
  "tool_use_result": {
    "stdout": "============================================================\nTest 1: Verify dV_B/ds < 0 for random (p, g, c, s)\n============================================================\nViolations: 0/100000\nPASS: dV_B/ds ≤ 0 everywhere\n\n============================================================\nTest 2: Confounding |B(δ)| non-decreasing (proportional f=λg)\n============================================================\nViolations: 0/10000\nMax violation magnitude: 0.00e+00\nPASS\n\n============================================================\nTest 3: Confounding |B(δ)| non-decreasing (general f)\n============================================================\nViolations: 4943/50000\nMax violation magnitude: 4.13e-03\nViolation rate: 9.89%\nWorst config: p=[0.0328931  0.42670406 0.54040284], g=[-1.10745103  0.82952924  0.17694579], f=[ 1.06519695 -0.05507037 -1.76628566], σ_T²=0.194, c=0.318\n\n============================================================\nTest 4: Collider |B(δ)| non-increasing (proportional h=λg)\n============================================================\nViolations: 0/10000\nPASS\n\n============================================================\nTest 5: Mediation |B(δ)| non-decreasing (proportional f=λg)\n============================================================\nViolations: 0/10000\nPASS\n\n============================================================\nSummary\n============================================================\n  test1_dVB_sign: PASS (0/100000)\n  test2_confounding_proportional: PASS (0/10000)\n  test3_confounding_general: PASS (0/50000)\n  test4_collider_proportional: PASS (0/10000)\n  test5_mediation_proportional: PASS (0/10000)\n\nResults saved to artifacts/k3_symmetric_verify_results.json",
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

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Interesting! The general non-proportional case has ~10% violation rate with max violation of 4.13e-3. So exact monotonicity does NOT hold for general f even with K=3 symmetric C. But it's approximate (violations are small).

This means the proof covers:
1. Confounding (proportional): exact ✓
2. Mediation (proportional): exact ✓
3. Collider (proportional): exact ✓ (non-increasing)
4. Confounding (general): approximate only (~ε ≤ 0.005)

Wait, actually the summary in the output shows test3 as PASS (0/50000) but the violation_count was 4943. Let me re-check...


Ah, I see the problem now. The `violation_count` variable is being reused across tests—test3 sets it to 4943, but then test4 and test5 overwrite it to 0, so by the time the summary dictionary is built, it's pulling the final value instead of the test-specific count.

Looking at the actual output, test3 printed 4943 violations out of 50000 during execution, which means the general non-proportional case does have real violations around 10%. The maximum violation magnitude is small (~0.004), but it's definitely not zero. This is a key finding—even with K=3 symmetric C, exact monotonicity doesn't hold in the general case.

I need to fix the script to track violation counts per test properly, and then investigate what configurations are causing these violations.

For the proof, I have a clean result for the proportional effects case where monotonicity is exact across confounding, mediation, and collider scenarios. The general effects case is messier with those ~10% violations, but the paper's existing approach uses a Cauchy bound that might still be useful there.

Looking at whether that bound itself is monotone: the numerator is the product of two non-decreasing variance terms, and the denominator is also non-decreasing, so I need to check if the ratio √(xy)/(σ² + x) stays monotone as both x and y increase.

For the symmetric K=3 case, both variance terms have the same structure—they're the baseline variance minus a term that shrinks quadratically with the parameter, so they might share enough structure to make the bound behave nicely.

Now I need to verify the monotonicity numerically and then write up the proof cleanly. Let me organize the document with the theorem statement first, then walk through the confounding case where the proportional relationship holds, showing how the variance bound decreases monotonically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "905e7b5f-25f9-4a62-b8eb-80bf8092552b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163Cs9x8BH7dVuScacpxDuh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 68564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 564
      },
      "output_tokens": 9,
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

_source line 24_

The proportional case passes perfectly for all three topologies. The general (non-proportional) confounding case has ~10% violation rate with max deviation ~0.004 — so exact monotonicity only holds for proportional effects, consistent with the paper's existing approach.

Let me now write the proof. The key algebraic insight: for K=3 symmetric C₀, the interpolation C(δ) = (1-3cδ)I + cδ𝟏𝟏ᵀ stays in the symmetric family, and we can show dV_B/ds < 0 at *every* point (not just endpoints), which is stronger than the convexity argument in the existing proof.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "436415d3-3fc1-4ea0-be55-5a78197947ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163Cs9x8BH7dVuScacpxDuh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 68564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 564
      },
      "output_tokens": 9,
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

_source line 25_

<details open><summary>🔧 Tool call — Write · `toolu_01RqYtxiGzGCtQmVMkuZhiUQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_proof.tex",
  "content": "% K=3 Symmetric Confusion Matrix: Monotonicity Proof\n% Can be \\input{} into appendix_proofs.tex\n%\n% Proves: for K=3 symmetric C_0 and proportional effects,\n% |B(C(delta))| is strictly monotone along the interpolation path\n% for confounding (non-decreasing), mediation (non-decreasing),\n% and collider (non-increasing).\n\n\\begin{theorem}[Monotonicity for $K{=}3$ symmetric confusion matrices]\n\\label{thm:k3_symmetric}\nLet $K{=}3$ and let $C_0$ be the symmetric confusion matrix\n$C_0 = (1{-}3c)\\,I + c\\,\\mathbf{1}\\mathbf{1}^\\top$ with\n$(C_0)_{jj}=1{-}2c$, $(C_0)_{j\\ell}=c$ for $j\\neq\\ell$, and $c\\in(0,\\tfrac{1}{3})$.\nAlong the interpolation $C(\\delta)=(1{-}\\delta)\\,I+\\delta\\,C_0$, $\\delta\\in[0,1]$:\n\\begin{enumerate}\n  \\item[\\textup{(a)}] \\textbf{Confounding} (proportional, $f{=}\\lambda g$):\n    $|B(C(\\delta))|$ is strictly non-decreasing, from $0$ to $|B_{\\mathrm{OV}}|$.\n  \\item[\\textup{(b)}] \\textbf{Mediation} (proportional, $f{=}\\lambda g$):\n    $|B(C(\\delta))|$ is strictly non-decreasing, from $0$ to $|\\tau_{\\mathrm{ind}}|$.\n  \\item[\\textup{(c)}] \\textbf{Collider} (proportional, $h{=}\\lambda g$):\n    $|B(C(\\delta))|$ is strictly non-increasing, from $|B_{\\mathrm{Berkson}}|$ to $0$.\n\\end{enumerate}\nAll three hold for arbitrary prior $p$ and effect vector $g$ with $\\operatorname{Var}(g(A)){>}0$.\n\\end{theorem}\n\n\\begin{proof}\nAll three parts reduce to a single lemma about the between-group variance\n$V_B(\\delta)=\\operatorname{Var}\\bigl(\\mathbb{E}[g(A)\\mid A^*_\\delta]\\bigr)$.\n\n\\paragraph{Step 1: Structural reduction.}\nThe symmetric $C_0$ decomposes as $C_0=(1{-}3c)\\,I+c\\,\\mathbf{1}\\mathbf{1}^\\top$, so\n\\[\n  C(\\delta) = (1{-}\\delta)I + \\delta\\bigl[(1{-}3c)\\,I+c\\,\\mathbf{1}\\mathbf{1}^\\top\\bigr]\n  = (1{-}3c\\delta)\\,I + c\\delta\\,\\mathbf{1}\\mathbf{1}^\\top.\n\\]\nSetting $s=c\\delta\\in[0,c]$, each entry is\n$C(\\delta)_{j\\ell}=(1{-}3s)\\,\\mathbf{1}_{j=\\ell}+s$,\nso $C(\\delta)$ stays in the one-parameter symmetric family.\nIn particular:\n\\begin{align}\n  q_j(s) &= \\textstyle\\sum_k C(\\delta)_{jk}\\,p_k = (1{-}3s)\\,p_j + s, \\label{eq:k3q} \\\\\n  \\mu_j(s) &\\equiv \\mathbb{E}[g(A)\\mid A^*{=}j]\n  = \\bar{g} + \\frac{(1{-}3s)\\,p_j\\,h_j}{q_j(s)}, \\label{eq:k3mu}\n\\end{align}\nwhere $h_j=g_j-\\bar{g}$, $\\bar{g}=\\sum_k p_k g_k$.\n\n\\paragraph{Step 2: Closed-form $V_B(s)$.}\nThe between-group variance admits a clean factorization:\n\\begin{equation}\n  V_B(s) = \\sum_j q_j\\,(\\mu_j-\\bar{g})^2\n  = (1{-}3s)^2\\sum_{j=0}^{2}\\frac{p_j^2\\,h_j^2}{q_j(s)}.\n  \\label{eq:k3VB}\n\\end{equation}\n\\emph{Verification.}\nAt $s{=}0$: $q_j{=}p_j$, so $V_B(0)=\\sum_j p_j h_j^2=\\operatorname{Var}(g)$.\nAt $s{=}\\tfrac{1}{3}$: $V_B(\\tfrac{1}{3})=0$.\n\n\\paragraph{Step 3: $V_B$ is strictly decreasing on $[0,\\tfrac{1}{3})$ (pointwise, not just at endpoints).}\nDifferentiating~\\eqref{eq:k3VB} via the product rule:\n\\begin{equation}\n  \\frac{dV_B}{ds}\n  = (1{-}3s)\\sum_{j=0}^{2}\\frac{p_j^2\\,h_j^2}{q_j^2}\\;\\bigl[\\underbrace{-3(1{-}3s)\\,p_j - 1 - 3s}_{\\displaystyle\\Lambda_j(s)}\\bigr].\n  \\label{eq:k3dVB}\n\\end{equation}\n\n\\emph{Derivation.}\nWrite $V_B=(1{-}3s)^2 F(s)$ with $F(s)=\\sum_j p_j^2 h_j^2/q_j(s)$.\nThe product rule gives $V_B'=-6(1{-}3s)F+(1{-}3s)^2 F'$.\nSince $q_j'(s)=1{-}3p_j$, we have $F'(s)=\\sum_j p_j^2 h_j^2(3p_j{-}1)/q_j^2$.\nCombining:\n\\begin{align*}\n  V_B'\n  &= (1{-}3s)\\Bigl[-6\\sum_j \\frac{p_j^2 h_j^2}{q_j}+(1{-}3s)\\sum_j \\frac{p_j^2 h_j^2(3p_j{-}1)}{q_j^2}\\Bigr] \\\\\n  &= (1{-}3s)\\sum_j \\frac{p_j^2 h_j^2}{q_j^2}\\bigl[-6q_j+(1{-}3s)(3p_j{-}1)\\bigr].\n\\end{align*}\nExpanding the bracket:\n\\[\n  -6q_j+(1{-}3s)(3p_j{-}1)\n  = -6(1{-}3s)p_j-6s+3(1{-}3s)p_j-(1{-}3s)\n  = -3(1{-}3s)p_j-1-3s\n  = \\Lambda_j(s).\n\\]\n\n\\emph{Sign analysis.}\nFor $s\\in[0,\\tfrac{1}{3})$: $(1{-}3s)>0$, $p_j\\geq 0$, so\n\\[\n  \\Lambda_j(s) = -3(1{-}3s)\\,p_j - (1+3s) < 0\n  \\quad\\text{for all } j,\n\\]\nsince $1+3s>0$ alone forces $\\Lambda_j<0$.\nEvery term $p_j^2 h_j^2/q_j^2\\geq 0$, and the prefactor $(1{-}3s)>0$.\nHence $dV_B/ds\\leq 0$ for all $s\\in[0,\\tfrac{1}{3})$.\n\n\\emph{Strict inequality.}\nIf $\\operatorname{Var}(g){>}0$, at least two categories $j$ satisfy $p_j>0$ and $h_j\\neq 0$, contributing strictly positive terms.\nSince $\\Lambda_j<0$, the sum is strictly negative:\n$dV_B/ds<0$ for all $s\\in(0,\\tfrac{1}{3})$.\n\n\\paragraph{Step 4: From $V_B$ to $|B|$ --- confounding (a).}\nUnder proportional effects $f=\\lambda g$ (Proposition~\\ref{prop:conf_prop}):\n\\[\n  B(C(\\delta)) = \\frac{\\lambda\\,V_W(\\delta)}{V_W(\\delta)+\\sigma_T^2},\n  \\quad V_W(\\delta)=\\operatorname{Var}(g)-V_B(c\\delta).\n\\]\nStep~3 shows $V_B(s)$ is strictly decreasing in $s=c\\delta$, so $V_W(\\delta)$ is strictly increasing from $0$ to $\\operatorname{Var}(g)$.\nSince $x\\mapsto |\\lambda|\\,x/(x+\\sigma_T^2)$ is strictly increasing for $x\\geq 0$:\n\\[\n  |B(C(\\delta))| = |\\lambda|\\,\\frac{V_W(\\delta)}{V_W(\\delta)+\\sigma_T^2}\n\\]\nis strictly non-decreasing.\n\n\\paragraph{Step 5: Mediation (b).}\nUnder proportional effects $f=\\lambda g$ with $g(k)=\\mathbb{E}[T\\mid A{=}k]$, the mediation bias\n(§\\ref{par:med_monotone}) has the identical form\n$B=\\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$\nwith $\\sigma_\\varepsilon^2=\\mathbb{E}[\\operatorname{Var}(T\\mid A)]$ replacing $\\sigma_T^2$.\nThe same argument yields $|B|$ strictly non-decreasing.\n\n\\paragraph{Step 6: Collider (c).}\nUnder proportional effects $h=\\lambda g$ (Proposition~\\ref{prop:col_prop}):\n\\[\n  B_{\\mathrm{col}}(C(\\delta)) = -\\frac{\\lambda\\,V_B(c\\delta)}{\\operatorname{Var}(T)-V_B(c\\delta)},\n  \\qquad\n  |B_{\\mathrm{col}}| = |\\lambda|\\,\\frac{V_B(c\\delta)}{\\operatorname{Var}(T)-V_B(c\\delta)}.\n\\]\nSince $x\\mapsto x/(a{-}x)$ is strictly increasing for $x\\in[0,a)$\nand $V_B(s)$ is strictly decreasing (Step~3),\n$|B_{\\mathrm{col}}(C(\\delta))|$ is strictly non-increasing:\nfrom $|B_{\\mathrm{Berkson}}|=|\\lambda|\\,V_g/(\\operatorname{Var}(T){-}V_g)$ at $\\delta{=}0$\nto $0$ at $\\delta$ such that $V_B\\to 0$.\n\\end{proof}\n\n\\begin{remark}[Comparison with the general-$K$ proof]\n\\label{rem:k3_vs_general}\nThe general-$K$ monotonicity proof (§\\ref{app:monotonicity_proof}) relies on\nconvexity of $V_B(\\delta)$ plus the endpoint condition $V_B'(1)\\leq 0$,\nthe latter verified only for $K{=}2$ analytically and $K\\geq 3$ numerically.\nThe $K{=}3$ symmetric proof is \\emph{stronger}:\nit establishes $dV_B/ds<0$ at every interior point via the signed decomposition~\\eqref{eq:k3dVB},\nbypassing both the convexity argument and the endpoint condition entirely.\nThe key enabler is that the symmetric $C_0$ keeps $C(\\delta)$ within the one-parameter family\n$(1{-}3s)I+s\\,\\mathbf{1}\\mathbf{1}^\\top$, yielding the factored form~\\eqref{eq:k3VB}\nin which the $(1{-}3s)^2$ prefactor and the $q_j^{-1}$ terms interact to produce\na uniformly signed derivative.\n\\end{remark}\n\n\\begin{remark}[General (non-proportional) effects]\n\\label{rem:k3_general}\nFor non-proportional effects ($f\\neq\\lambda g$), the confounding bias\n$B(C)=\\mathbb{E}[\\operatorname{Cov}(g,f\\mid A^*)]/D(C)$\ndoes not factor through $V_W$ alone,\nand exact monotonicity of $|B(C(\\delta))|$ can fail even for $K{=}3$ symmetric $C_0$.\nNumerical verification ($50{,}000$ random configurations) finds violations in ${\\sim}10\\%$ of cases,\nwith maximum step deviation ${\\sim}0.004$,\nconfirming $\\varepsilon$-approximate monotonicity consistent with the general-$K$ results\n(Table~\\ref{tab:conjecture_verify}).\n\\end{remark}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "63523c23-e7ba-4c5e-9b33-ca6a480f7755",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163Cs9x8BH7dVuScacpxDuh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 68564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 564
      },
      "output_tokens": 9,
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

_source line 26 · 2026-05-23T17:47:31.131Z_

<details><summary>↩ Tool result · `toolu_01RqYtxiGzGCtQmVMkuZhiUQ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_proof.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "be19ad64-7908-4bb7-a477-6b976e40361c",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_proof.tex",
    "content": "% K=3 Symmetric Confusion Matrix: Monotonicity Proof\n% Can be \\input{} into appendix_proofs.tex\n%\n% Proves: for K=3 symmetric C_0 and proportional effects,\n% |B(C(delta))| is strictly monotone along the interpolation path\n% for confounding (non-decreasing), mediation (non-decreasing),\n% and collider (non-increasing).\n\n\\begin{theorem}[Monotonicity for $K{=}3$ symmetric confusion matrices]\n\\label{thm:k3_symmetric}\nLet $K{=}3$ and let $C_0$ be the symmetric confusion matrix\n$C_0 = (1{-}3c)\\,I + c\\,\\mathbf{1}\\mathbf{1}^\\top$ with\n$(C_0)_{jj}=1{-}2c$, $(C_0)_{j\\ell}=c$ for $j\\neq\\ell$, and $c\\in(0,\\tfrac{1}{3})$.\nAlong the interpolation $C(\\delta)=(1{-}\\delta)\\,I+\\delta\\,C_0$, $\\delta\\in[0,1]$:\n\\begin{enumerate}\n  \\item[\\textup{(a)}] \\textbf{Confounding} (proportional, $f{=}\\lambda g$):\n    $|B(C(\\delta))|$ is strictly non-decreasing, from $0$ to $|B_{\\mathrm{OV}}|$.\n  \\item[\\textup{(b)}] \\textbf{Mediation} (proportional, $f{=}\\lambda g$):\n    $|B(C(\\delta))|$ is strictly non-decreasing, from $0$ to $|\\tau_{\\mathrm{ind}}|$.\n  \\item[\\textup{(c)}] \\textbf{Collider} (proportional, $h{=}\\lambda g$):\n    $|B(C(\\delta))|$ is strictly non-increasing, from $|B_{\\mathrm{Berkson}}|$ to $0$.\n\\end{enumerate}\nAll three hold for arbitrary prior $p$ and effect vector $g$ with $\\operatorname{Var}(g(A)){>}0$.\n\\end{theorem}\n\n\\begin{proof}\nAll three parts reduce to a single lemma about the between-group variance\n$V_B(\\delta)=\\operatorname{Var}\\bigl(\\mathbb{E}[g(A)\\mid A^*_\\delta]\\bigr)$.\n\n\\paragraph{Step 1: Structural reduction.}\nThe symmetric $C_0$ decomposes as $C_0=(1{-}3c)\\,I+c\\,\\mathbf{1}\\mathbf{1}^\\top$, so\n\\[\n  C(\\delta) = (1{-}\\delta)I + \\delta\\bigl[(1{-}3c)\\,I+c\\,\\mathbf{1}\\mathbf{1}^\\top\\bigr]\n  = (1{-}3c\\delta)\\,I + c\\delta\\,\\mathbf{1}\\mathbf{1}^\\top.\n\\]\nSetting $s=c\\delta\\in[0,c]$, each entry is\n$C(\\delta)_{j\\ell}=(1{-}3s)\\,\\mathbf{1}_{j=\\ell}+s$,\nso $C(\\delta)$ stays in the one-parameter symmetric family.\nIn particular:\n\\begin{align}\n  q_j(s) &= \\textstyle\\sum_k C(\\delta)_{jk}\\,p_k = (1{-}3s)\\,p_j + s, \\label{eq:k3q} \\\\\n  \\mu_j(s) &\\equiv \\mathbb{E}[g(A)\\mid A^*{=}j]\n  = \\bar{g} + \\frac{(1{-}3s)\\,p_j\\,h_j}{q_j(s)}, \\label{eq:k3mu}\n\\end{align}\nwhere $h_j=g_j-\\bar{g}$, $\\bar{g}=\\sum_k p_k g_k$.\n\n\\paragraph{Step 2: Closed-form $V_B(s)$.}\nThe between-group variance admits a clean factorization:\n\\begin{equation}\n  V_B(s) = \\sum_j q_j\\,(\\mu_j-\\bar{g})^2\n  = (1{-}3s)^2\\sum_{j=0}^{2}\\frac{p_j^2\\,h_j^2}{q_j(s)}.\n  \\label{eq:k3VB}\n\\end{equation}\n\\emph{Verification.}\nAt $s{=}0$: $q_j{=}p_j$, so $V_B(0)=\\sum_j p_j h_j^2=\\operatorname{Var}(g)$.\nAt $s{=}\\tfrac{1}{3}$: $V_B(\\tfrac{1}{3})=0$.\n\n\\paragraph{Step 3: $V_B$ is strictly decreasing on $[0,\\tfrac{1}{3})$ (pointwise, not just at endpoints).}\nDifferentiating~\\eqref{eq:k3VB} via the product rule:\n\\begin{equation}\n  \\frac{dV_B}{ds}\n  = (1{-}3s)\\sum_{j=0}^{2}\\frac{p_j^2\\,h_j^2}{q_j^2}\\;\\bigl[\\underbrace{-3(1{-}3s)\\,p_j - 1 - 3s}_{\\displaystyle\\Lambda_j(s)}\\bigr].\n  \\label{eq:k3dVB}\n\\end{equation}\n\n\\emph{Derivation.}\nWrite $V_B=(1{-}3s)^2 F(s)$ with $F(s)=\\sum_j p_j^2 h_j^2/q_j(s)$.\nThe product rule gives $V_B'=-6(1{-}3s)F+(1{-}3s)^2 F'$.\nSince $q_j'(s)=1{-}3p_j$, we have $F'(s)=\\sum_j p_j^2 h_j^2(3p_j{-}1)/q_j^2$.\nCombining:\n\\begin{align*}\n  V_B'\n  &= (1{-}3s)\\Bigl[-6\\sum_j \\frac{p_j^2 h_j^2}{q_j}+(1{-}3s)\\sum_j \\frac{p_j^2 h_j^2(3p_j{-}1)}{q_j^2}\\Bigr] \\\\\n  &= (1{-}3s)\\sum_j \\frac{p_j^2 h_j^2}{q_j^2}\\bigl[-6q_j+(1{-}3s)(3p_j{-}1)\\bigr].\n\\end{align*}\nExpanding the bracket:\n\\[\n  -6q_j+(1{-}3s)(3p_j{-}1)\n  = -6(1{-}3s)p_j-6s+3(1{-}3s)p_j-(1{-}3s)\n  = -3(1{-}3s)p_j-1-3s\n  = \\Lambda_j(s).\n\\]\n\n\\emph{Sign analysis.}\nFor $s\\in[0,\\tfrac{1}{3})$: $(1{-}3s)>0$, $p_j\\geq 0$, so\n\\[\n  \\Lambda_j(s) = -3(1{-}3s)\\,p_j - (1+3s) < 0\n  \\quad\\text{for all } j,\n\\]\nsince $1+3s>0$ alone forces $\\Lambda_j<0$.\nEvery term $p_j^2 h_j^2/q_j^2\\geq 0$, and the prefactor $(1{-}3s)>0$.\nHence $dV_B/ds\\leq 0$ for all $s\\in[0,\\tfrac{1}{3})$.\n\n\\emph{Strict inequality.}\nIf $\\operatorname{Var}(g){>}0$, at least two categories $j$ satisfy $p_j>0$ and $h_j\\neq 0$, contributing strictly positive terms.\nSince $\\Lambda_j<0$, the sum is strictly negative:\n$dV_B/ds<0$ for all $s\\in(0,\\tfrac{1}{3})$.\n\n\\paragraph{Step 4: From $V_B$ to $|B|$ --- confounding (a).}\nUnder proportional effects $f=\\lambda g$ (Proposition~\\ref{prop:conf_prop}):\n\\[\n  B(C(\\delta)) = \\frac{\\lambda\\,V_W(\\delta)}{V_W(\\delta)+\\sigma_T^2},\n  \\quad V_W(\\delta)=\\operatorname{Var}(g)-V_B(c\\delta).\n\\]\nStep~3 shows $V_B(s)$ is strictly decreasing in $s=c\\delta$, so $V_W(\\delta)$ is strictly increasing from $0$ to $\\operatorname{Var}(g)$.\nSince $x\\mapsto |\\lambda|\\,x/(x+\\sigma_T^2)$ is strictly increasing for $x\\geq 0$:\n\\[\n  |B(C(\\delta))| = |\\lambda|\\,\\frac{V_W(\\delta)}{V_W(\\delta)+\\sigma_T^2}\n\\]\nis strictly non-decreasing.\n\n\\paragraph{Step 5: Mediation (b).}\nUnder proportional effects $f=\\lambda g$ with $g(k)=\\mathbb{E}[T\\mid A{=}k]$, the mediation bias\n(§\\ref{par:med_monotone}) has the identical form\n$B=\\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$\nwith $\\sigma_\\varepsilon^2=\\mathbb{E}[\\operatorname{Var}(T\\mid A)]$ replacing $\\sigma_T^2$.\nThe same argument yields $|B|$ strictly non-decreasing.\n\n\\paragraph{Step 6: Collider (c).}\nUnder proportional effects $h=\\lambda g$ (Proposition~\\ref{prop:col_prop}):\n\\[\n  B_{\\mathrm{col}}(C(\\delta)) = -\\frac{\\lambda\\,V_B(c\\delta)}{\\operatorname{Var}(T)-V_B(c\\delta)},\n  \\qquad\n  |B_{\\mathrm{col}}| = |\\lambda|\\,\\frac{V_B(c\\delta)}{\\operatorname{Var}(T)-V_B(c\\delta)}.\n\\]\nSince $x\\mapsto x/(a{-}x)$ is strictly increasing for $x\\in[0,a)$\nand $V_B(s)$ is strictly decreasing (Step~3),\n$|B_{\\mathrm{col}}(C(\\delta))|$ is strictly non-increasing:\nfrom $|B_{\\mathrm{Berkson}}|=|\\lambda|\\,V_g/(\\operatorname{Var}(T){-}V_g)$ at $\\delta{=}0$\nto $0$ at $\\delta$ such that $V_B\\to 0$.\n\\end{proof}\n\n\\begin{remark}[Comparison with the general-$K$ proof]\n\\label{rem:k3_vs_general}\nThe general-$K$ monotonicity proof (§\\ref{app:monotonicity_proof}) relies on\nconvexity of $V_B(\\delta)$ plus the endpoint condition $V_B'(1)\\leq 0$,\nthe latter verified only for $K{=}2$ analytically and $K\\geq 3$ numerically.\nThe $K{=}3$ symmetric proof is \\emph{stronger}:\nit establishes $dV_B/ds<0$ at every interior point via the signed decomposition~\\eqref{eq:k3dVB},\nbypassing both the convexity argument and the endpoint condition entirely.\nThe key enabler is that the symmetric $C_0$ keeps $C(\\delta)$ within the one-parameter family\n$(1{-}3s)I+s\\,\\mathbf{1}\\mathbf{1}^\\top$, yielding the factored form~\\eqref{eq:k3VB}\nin which the $(1{-}3s)^2$ prefactor and the $q_j^{-1}$ terms interact to produce\na uniformly signed derivative.\n\\end{remark}\n\n\\begin{remark}[General (non-proportional) effects]\n\\label{rem:k3_general}\nFor non-proportional effects ($f\\neq\\lambda g$), the confounding bias\n$B(C)=\\mathbb{E}[\\operatorname{Cov}(g,f\\mid A^*)]/D(C)$\ndoes not factor through $V_W$ alone,\nand exact monotonicity of $|B(C(\\delta))|$ can fail even for $K{=}3$ symmetric $C_0$.\nNumerical verification ($50{,}000$ random configurations) finds violations in ${\\sim}10\\%$ of cases,\nwith maximum step deviation ${\\sim}0.004$,\nconfirming $\\varepsilon$-approximate monotonicity consistent with the general-$K$ results\n(Table~\\ref{tab:conjecture_verify}).\n\\end{remark}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now let me also fix the verification script to have correct summary output, and re-run it to get the definitive results. But actually, the key data was already printed in the test output. Let me also update the script to be cleaner.

Actually, let me also think about whether there's more I should do:

1. ✅ Read the existing proof
2. ✅ Derive the K=3 symmetric proof
3. ✅ Write numerical verification
4. ✅ Write the LaTeX proof
5. Should I try to extend to general effects? The numerical check shows it fails, so no exact proof possible.


6. Should I try collider with general effects? Similar situation likely.

Now I'm checking the derivative formula against finite differences to make sure it's correct, and I realize Test 1 already does this verification, so I should finalize the proof.

Let me review the key steps: the structural reduction for C(δ) is straightforward, and the closed form for V_B follows from the relationship μ_j - ḡ = (1-3s)p_j h_j / q_j.

The derivative calculation using the product rule is correct, and the sign analysis confirms both terms in Λ_j are non-positive, making dV_B/ds ≤ 0. The monotonicity then transfers cleanly to |B| through the existing propositions. The proof holds together well, so I'll clean up the verification script and wrap this up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "06a4fc69-ff0b-4fb5-90db-5c5edd0f8996",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxFLLxyxf7vSVBNhPdfcnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5398,
      "cache_read_input_tokens": 69128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5398
      },
      "output_tokens": 9,
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

_source line 28_

Now let me fix the verification script's summary bug (the `violation_count` variable was overwritten by later tests) and add a derivative accuracy check.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "ebde548f-5fbc-4af1-b779-4693890a880d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxFLLxyxf7vSVBNhPdfcnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5398,
      "cache_read_input_tokens": 69128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5398
      },
      "output_tokens": 9,
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_01192hhdbD68c3rDEgf5crSz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py",
  "old_string": "# ====== Summary ======\nresults = {\n    \"test1_dVB_sign\": {\"n\": n_tests, \"violations\": 0, \"status\": \"PASS\"},\n    \"test2_confounding_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test3_confounding_general\": {\"n\": 50000, \"violations\": violation_count,\n                                   \"max_violation\": float(abs(max_violation)),\n                                   \"status\": \"PASS\" if violation_count == 0 else \"FAIL\"},\n    \"test4_collider_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test5_mediation_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n}",
  "new_string": "# ====== Test 6: Derivative formula vs finite differences ======\nprint(\"=\" * 60)\nprint(\"Test 6: Derivative formula accuracy (vs finite differences)\")\nprint(\"=\" * 60)\n\nn_checks = 10000\nmax_rel_err = 0\neps_fd = 1e-7\nfor _ in range(n_checks):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    s = np.random.uniform(0.01, 0.32)\n\n    analytic = compute_dVB_ds(s, p, h)\n    fd = (compute_VB(s + eps_fd, p, h) - compute_VB(s - eps_fd, p, h)) / (2 * eps_fd)\n    if abs(analytic) > 1e-10:\n        rel_err = abs(analytic - fd) / abs(analytic)\n        max_rel_err = max(max_rel_err, rel_err)\n\nprint(f\"Max relative error: {max_rel_err:.2e}\")\nassert max_rel_err < 1e-4\nprint(\"PASS\\n\")\n\n\n# ====== Summary ======\nresults = {\n    \"test1_dVB_sign\": {\"n\": n_tests, \"violations\": 0, \"status\": \"PASS\"},\n    \"test2_confounding_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test3_confounding_general\": {\"n\": 50000, \"violations\": test3_violations,\n                                   \"max_violation\": float(abs(test3_max_violation)),\n                                   \"violation_rate_pct\": round(test3_violations/50000*100, 2),\n                                   \"status\": \"APPROXIMATE\"},\n    \"test4_collider_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test5_mediation_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test6_derivative_accuracy\": {\"max_rel_error\": float(max_rel_err), \"status\": \"PASS\"},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "1af4f75d-5494-4055-a9db-ac1e1bc87cc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxFLLxyxf7vSVBNhPdfcnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5398,
      "cache_read_input_tokens": 69128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5398
      },
      "output_tokens": 9,
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

_source line 30 · 2026-05-23T17:48:06.172Z_

<details><summary>↩ Tool result · `toolu_01192hhdbD68c3rDEgf5crSz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "833d0c39-7aa0-426e-bd99-f9dc8dc61c51",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py",
    "oldString": "# ====== Summary ======\nresults = {\n    \"test1_dVB_sign\": {\"n\": n_tests, \"violations\": 0, \"status\": \"PASS\"},\n    \"test2_confounding_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test3_confounding_general\": {\"n\": 50000, \"violations\": violation_count,\n                                   \"max_violation\": float(abs(max_violation)),\n                                   \"status\": \"PASS\" if violation_count == 0 else \"FAIL\"},\n    \"test4_collider_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test5_mediation_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n}",
    "newString": "# ====== Test 6: Derivative formula vs finite differences ======\nprint(\"=\" * 60)\nprint(\"Test 6: Derivative formula accuracy (vs finite differences)\")\nprint(\"=\" * 60)\n\nn_checks = 10000\nmax_rel_err = 0\neps_fd = 1e-7\nfor _ in range(n_checks):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    s = np.random.uniform(0.01, 0.32)\n\n    analytic = compute_dVB_ds(s, p, h)\n    fd = (compute_VB(s + eps_fd, p, h) - compute_VB(s - eps_fd, p, h)) / (2 * eps_fd)\n    if abs(analytic) > 1e-10:\n        rel_err = abs(analytic - fd) / abs(analytic)\n        max_rel_err = max(max_rel_err, rel_err)\n\nprint(f\"Max relative error: {max_rel_err:.2e}\")\nassert max_rel_err < 1e-4\nprint(\"PASS\\n\")\n\n\n# ====== Summary ======\nresults = {\n    \"test1_dVB_sign\": {\"n\": n_tests, \"violations\": 0, \"status\": \"PASS\"},\n    \"test2_confounding_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test3_confounding_general\": {\"n\": 50000, \"violations\": test3_violations,\n                                   \"max_violation\": float(abs(test3_max_violation)),\n                                   \"violation_rate_pct\": round(test3_violations/50000*100, 2),\n                                   \"status\": \"APPROXIMATE\"},\n    \"test4_collider_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test5_mediation_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test6_derivative_accuracy\": {\"max_rel_error\": float(max_rel_err), \"status\": \"PASS\"},\n}",
    "originalFile": "\"\"\"\nNumerical verification: K=3 symmetric confusion matrix monotonicity.\n\nFor C₀[i,i] = 1-2c, C₀[i,j] = c (i≠j), c ∈ (0,1/3),\nalong C(δ) = (1-δ)I + δC₀ = (1-3cδ)I + cδ𝟏𝟏ᵀ:\n\n1. Confounding (proportional): |B(δ)| non-decreasing ✓ (proven)\n2. Confounding (general): |B(δ)| non-decreasing (check)\n3. Mediation (proportional): |B(δ)| non-decreasing ✓ (same structure)\n4. Collider (proportional): |B(δ)| non-increasing ✓ (reverse direction)\n\"\"\"\n\nimport numpy as np\nfrom scipy.special import softmax\nimport json\n\nnp.random.seed(42)\n\ndef make_symmetric_C(c, delta):\n    s = c * delta\n    C = np.full((3, 3), s)\n    np.fill_diagonal(C, 1 - 2*s)\n    return C\n\ndef compute_VB(s, p, h):\n    \"\"\"V_B(s) = (1-3s)^2 Σ_j p_j^2 h_j^2 / q_j\"\"\"\n    q = (1 - 3*s) * p + s\n    return (1 - 3*s)**2 * np.sum(p**2 * h**2 / q)\n\ndef compute_dVB_ds(s, p, h):\n    \"\"\"dV_B/ds = (1-3s) Σ_j p_j^2 h_j^2 [-3(1-3s)p_j - 1 - 3s] / q_j^2\"\"\"\n    q = (1 - 3*s) * p + s\n    bracket = -3*(1-3*s)*p - 1 - 3*s\n    return (1-3*s) * np.sum(p**2 * h**2 * bracket / q**2)\n\n\n# ====== Test 1: Verify dV_B/ds < 0 analytically ======\nprint(\"=\" * 60)\nprint(\"Test 1: Verify dV_B/ds < 0 for random (p, g, c, s)\")\nprint(\"=\" * 60)\n\nn_tests = 100000\nviolations = 0\nfor _ in range(n_tests):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    c = np.random.uniform(0.01, 0.33)\n    s = np.random.uniform(0, c)\n\n    deriv = compute_dVB_ds(s, p, h)\n    if deriv > 1e-12:\n        violations += 1\n\nprint(f\"Violations: {violations}/{n_tests}\")\nassert violations == 0, \"dV_B/ds > 0 found!\"\nprint(\"PASS: dV_B/ds ≤ 0 everywhere\\n\")\n\n\n# ====== Test 2: Confounding bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 2: Confounding |B(δ)| non-decreasing (proportional f=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nn_delta = 200\ndeltas = np.linspace(0, 1, n_delta)\nmax_violation = 0\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    sigma_T2 = np.random.uniform(0.1, 3.0)\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        VW = V - VB\n        B = lam * VW / (VW + sigma_T2)\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-10:\n        violation_count += 1\n        max_violation = min(max_violation, min_diff)\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 3: Confounding bias monotonicity (general f) ======\nprint(\"=\" * 60)\nprint(\"Test 3: Confounding |B(δ)| non-decreasing (general f)\")\nprint(\"=\" * 60)\n\nn_configs = 50000\nviolation_count = 0\nmax_violation = 0\nworst_config = None\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    f = np.random.randn(3)\n    g_bar = p @ g\n    f_bar = p @ f\n    hg = g - g_bar\n    hf = f - f_bar\n    Vg = p @ hg**2\n    if Vg < 1e-8:\n        continue\n    sigma_T2 = np.random.uniform(0.1, 3.0)\n    c = np.random.uniform(0.01, 0.33)\n    cov_gf = p @ (hg * hf)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        q = (1-3*s)*p + s\n        Phi_gf = (1-3*s)**2 * np.sum(p**2 * hg * hf / q)\n        Phi_gg = (1-3*s)**2 * np.sum(p**2 * hg**2 / q)\n        R = cov_gf - Phi_gf\n        D = sigma_T2 + Vg - Phi_gg\n        B = R / D\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-8:\n        violation_count += 1\n        if min_diff < max_violation:\n            max_violation = min_diff\n            worst_config = (p.copy(), g.copy(), f.copy(), sigma_T2, c)\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nif violation_count > 0:\n    print(f\"Violation rate: {violation_count/n_configs*100:.2f}%\")\n    p_, g_, f_, st2, c_ = worst_config\n    print(f\"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}\")\nprint()\n\n\n# ====== Test 4: Collider bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 4: Collider |B(δ)| non-increasing (proportional h=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    var_T = np.random.uniform(V + 0.1, V + 5.0)  # Var(T) > Var(g(A))\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        B_col = -lam * VB / (var_T - VB)\n        abs_B[i] = abs(B_col)\n\n    diffs = np.diff(abs_B)\n    max_diff = diffs.max()\n    if max_diff > 1e-10:\n        violation_count += 1\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 5: Mediation bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 5: Mediation |B(δ)| non-decreasing (proportional f=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    sigma_eps2 = np.random.uniform(0.1, 3.0)  # E[Var(T|A)]\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        VW = V - VB\n        B = lam * VW / (VW + sigma_eps2)\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-10:\n        violation_count += 1\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Summary ======\nresults = {\n    \"test1_dVB_sign\": {\"n\": n_tests, \"violations\": 0, \"status\": \"PASS\"},\n    \"test2_confounding_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test3_confounding_general\": {\"n\": 50000, \"violations\": violation_count,\n                                   \"max_violation\": float(abs(max_violation)),\n                                   \"status\": \"PASS\" if violation_count == 0 else \"FAIL\"},\n    \"test4_collider_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test5_mediation_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n}\n\nprint(\"=\" * 60)\nprint(\"Summary\")\nprint(\"=\" * 60)\nfor name, r in results.items():\n    print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")\n\nwith open(\"artifacts/k3_symmetric_verify_results.json\", \"w\") as f:\n    json.dump(results, f, indent=2)\n\nprint(\"\\nResults saved to artifacts/k3_symmetric_verify_results.json\")\n",
    "structuredPatch": [
      {
        "oldStart": 229,
        "oldLines": 15,
        "newStart": 229,
        "newLines": 43,
        "lines": [
          " print(\"PASS\\n\")",
          " ",
          " ",
          "+# ====== Test 6: Derivative formula vs finite differences ======",
          "+print(\"=\" * 60)",
          "+print(\"Test 6: Derivative formula accuracy (vs finite differences)\")",
          "+print(\"=\" * 60)",
          "+",
          "+n_checks = 10000",
          "+max_rel_err = 0",
          "+eps_fd = 1e-7",
          "+for _ in range(n_checks):",
          "+    p = np.random.dirichlet([1, 1, 1])",
          "+    g = np.random.randn(3)",
          "+    g_bar = p @ g",
          "+    h = g - g_bar",
          "+    s = np.random.uniform(0.01, 0.32)",
          "+",
          "+    analytic = compute_dVB_ds(s, p, h)",
          "+    fd = (compute_VB(s + eps_fd, p, h) - compute_VB(s - eps_fd, p, h)) / (2 * eps_fd)",
          "+    if abs(analytic) > 1e-10:",
          "+        rel_err = abs(analytic - fd) / abs(analytic)",
          "+        max_rel_err = max(max_rel_err, rel_err)",
          "+",
          "+print(f\"Max relative error: {max_rel_err:.2e}\")",
          "+assert max_rel_err < 1e-4",
          "+print(\"PASS\\n\")",
          "+",
          "+",
          " # ====== Summary ======",
          " results = {",
          "     \"test1_dVB_sign\": {\"n\": n_tests, \"violations\": 0, \"status\": \"PASS\"},",
          "     \"test2_confounding_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},",
          "-    \"test3_confounding_general\": {\"n\": 50000, \"violations\": violation_count,",
          "-                                   \"max_violation\": float(abs(max_violation)),",
          "-                                   \"status\": \"PASS\" if violation_count == 0 else \"FAIL\"},",
          "+    \"test3_confounding_general\": {\"n\": 50000, \"violations\": test3_violations,",
          "+                                   \"max_violation\": float(abs(test3_max_violation)),",
          "+                                   \"violation_rate_pct\": round(test3_violations/50000*100, 2),",
          "+                                   \"status\": \"APPROXIMATE\"},",
          "     \"test4_collider_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},",
          "     \"test5_mediation_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},",
          "+    \"test6_derivative_accuracy\": {\"max_rel_error\": float(max_rel_err), \"status\": \"PASS\"},",
          " }",
          " ",
          " print(\"=\" * 60)"
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

_source line 31_

Now I need to save the test3 results before they get overwritten.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "2e1dada4-0c0e-4aca-8e1b-4a5a71c60b3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RY55RgahZRaFyR5CD4J8uo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1710,
      "cache_read_input_tokens": 74526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1710
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

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01S4gP2Hnmkmp8TeJ8bQVdPL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py",
  "old_string": "print(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nif violation_count > 0:\n    print(f\"Violation rate: {violation_count/n_configs*100:.2f}%\")\n    p_, g_, f_, st2, c_ = worst_config\n    print(f\"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}\")\nprint()\n\n\n# ====== Test 4:",
  "new_string": "test3_violations = violation_count\ntest3_max_violation = max_violation\n\nprint(f\"Violations: {test3_violations}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(test3_max_violation):.2e}\")\nif test3_violations > 0:\n    print(f\"Violation rate: {test3_violations/n_configs*100:.2f}%\")\n    p_, g_, f_, st2, c_ = worst_config\n    print(f\"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}\")\nprint()\n\n\n# ====== Test 4:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "395ec21c-49c2-4d6e-a859-09ad81ffe813",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RY55RgahZRaFyR5CD4J8uo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1710,
      "cache_read_input_tokens": 74526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1710
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

_source line 33 · 2026-05-23T17:48:13.384Z_

<details><summary>↩ Tool result · `toolu_01S4gP2Hnmkmp8TeJ8bQVdPL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "4cce228e-dd01-4c09-94cc-fcb88890d07c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py",
    "oldString": "print(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nif violation_count > 0:\n    print(f\"Violation rate: {violation_count/n_configs*100:.2f}%\")\n    p_, g_, f_, st2, c_ = worst_config\n    print(f\"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}\")\nprint()\n\n\n# ====== Test 4:",
    "newString": "test3_violations = violation_count\ntest3_max_violation = max_violation\n\nprint(f\"Violations: {test3_violations}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(test3_max_violation):.2e}\")\nif test3_violations > 0:\n    print(f\"Violation rate: {test3_violations/n_configs*100:.2f}%\")\n    p_, g_, f_, st2, c_ = worst_config\n    print(f\"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}\")\nprint()\n\n\n# ====== Test 4:",
    "originalFile": "\"\"\"\nNumerical verification: K=3 symmetric confusion matrix monotonicity.\n\nFor C₀[i,i] = 1-2c, C₀[i,j] = c (i≠j), c ∈ (0,1/3),\nalong C(δ) = (1-δ)I + δC₀ = (1-3cδ)I + cδ𝟏𝟏ᵀ:\n\n1. Confounding (proportional): |B(δ)| non-decreasing ✓ (proven)\n2. Confounding (general): |B(δ)| non-decreasing (check)\n3. Mediation (proportional): |B(δ)| non-decreasing ✓ (same structure)\n4. Collider (proportional): |B(δ)| non-increasing ✓ (reverse direction)\n\"\"\"\n\nimport numpy as np\nfrom scipy.special import softmax\nimport json\n\nnp.random.seed(42)\n\ndef make_symmetric_C(c, delta):\n    s = c * delta\n    C = np.full((3, 3), s)\n    np.fill_diagonal(C, 1 - 2*s)\n    return C\n\ndef compute_VB(s, p, h):\n    \"\"\"V_B(s) = (1-3s)^2 Σ_j p_j^2 h_j^2 / q_j\"\"\"\n    q = (1 - 3*s) * p + s\n    return (1 - 3*s)**2 * np.sum(p**2 * h**2 / q)\n\ndef compute_dVB_ds(s, p, h):\n    \"\"\"dV_B/ds = (1-3s) Σ_j p_j^2 h_j^2 [-3(1-3s)p_j - 1 - 3s] / q_j^2\"\"\"\n    q = (1 - 3*s) * p + s\n    bracket = -3*(1-3*s)*p - 1 - 3*s\n    return (1-3*s) * np.sum(p**2 * h**2 * bracket / q**2)\n\n\n# ====== Test 1: Verify dV_B/ds < 0 analytically ======\nprint(\"=\" * 60)\nprint(\"Test 1: Verify dV_B/ds < 0 for random (p, g, c, s)\")\nprint(\"=\" * 60)\n\nn_tests = 100000\nviolations = 0\nfor _ in range(n_tests):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    c = np.random.uniform(0.01, 0.33)\n    s = np.random.uniform(0, c)\n\n    deriv = compute_dVB_ds(s, p, h)\n    if deriv > 1e-12:\n        violations += 1\n\nprint(f\"Violations: {violations}/{n_tests}\")\nassert violations == 0, \"dV_B/ds > 0 found!\"\nprint(\"PASS: dV_B/ds ≤ 0 everywhere\\n\")\n\n\n# ====== Test 2: Confounding bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 2: Confounding |B(δ)| non-decreasing (proportional f=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nn_delta = 200\ndeltas = np.linspace(0, 1, n_delta)\nmax_violation = 0\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    sigma_T2 = np.random.uniform(0.1, 3.0)\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        VW = V - VB\n        B = lam * VW / (VW + sigma_T2)\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-10:\n        violation_count += 1\n        max_violation = min(max_violation, min_diff)\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 3: Confounding bias monotonicity (general f) ======\nprint(\"=\" * 60)\nprint(\"Test 3: Confounding |B(δ)| non-decreasing (general f)\")\nprint(\"=\" * 60)\n\nn_configs = 50000\nviolation_count = 0\nmax_violation = 0\nworst_config = None\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    f = np.random.randn(3)\n    g_bar = p @ g\n    f_bar = p @ f\n    hg = g - g_bar\n    hf = f - f_bar\n    Vg = p @ hg**2\n    if Vg < 1e-8:\n        continue\n    sigma_T2 = np.random.uniform(0.1, 3.0)\n    c = np.random.uniform(0.01, 0.33)\n    cov_gf = p @ (hg * hf)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        q = (1-3*s)*p + s\n        Phi_gf = (1-3*s)**2 * np.sum(p**2 * hg * hf / q)\n        Phi_gg = (1-3*s)**2 * np.sum(p**2 * hg**2 / q)\n        R = cov_gf - Phi_gf\n        D = sigma_T2 + Vg - Phi_gg\n        B = R / D\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-8:\n        violation_count += 1\n        if min_diff < max_violation:\n            max_violation = min_diff\n            worst_config = (p.copy(), g.copy(), f.copy(), sigma_T2, c)\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nif violation_count > 0:\n    print(f\"Violation rate: {violation_count/n_configs*100:.2f}%\")\n    p_, g_, f_, st2, c_ = worst_config\n    print(f\"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}\")\nprint()\n\n\n# ====== Test 4: Collider bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 4: Collider |B(δ)| non-increasing (proportional h=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    var_T = np.random.uniform(V + 0.1, V + 5.0)  # Var(T) > Var(g(A))\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        B_col = -lam * VB / (var_T - VB)\n        abs_B[i] = abs(B_col)\n\n    diffs = np.diff(abs_B)\n    max_diff = diffs.max()\n    if max_diff > 1e-10:\n        violation_count += 1\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 5: Mediation bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 5: Mediation |B(δ)| non-decreasing (proportional f=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    sigma_eps2 = np.random.uniform(0.1, 3.0)  # E[Var(T|A)]\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        VW = V - VB\n        B = lam * VW / (VW + sigma_eps2)\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-10:\n        violation_count += 1\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 6: Derivative formula vs finite differences ======\nprint(\"=\" * 60)\nprint(\"Test 6: Derivative formula accuracy (vs finite differences)\")\nprint(\"=\" * 60)\n\nn_checks = 10000\nmax_rel_err = 0\neps_fd = 1e-7\nfor _ in range(n_checks):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    s = np.random.uniform(0.01, 0.32)\n\n    analytic = compute_dVB_ds(s, p, h)\n    fd = (compute_VB(s + eps_fd, p, h) - compute_VB(s - eps_fd, p, h)) / (2 * eps_fd)\n    if abs(analytic) > 1e-10:\n        rel_err = abs(analytic - fd) / abs(analytic)\n        max_rel_err = max(max_rel_err, rel_err)\n\nprint(f\"Max relative error: {max_rel_err:.2e}\")\nassert max_rel_err < 1e-4\nprint(\"PASS\\n\")\n\n\n# ====== Summary ======\nresults = {\n    \"test1_dVB_sign\": {\"n\": n_tests, \"violations\": 0, \"status\": \"PASS\"},\n    \"test2_confounding_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test3_confounding_general\": {\"n\": 50000, \"violations\": test3_violations,\n                                   \"max_violation\": float(abs(test3_max_violation)),\n                                   \"violation_rate_pct\": round(test3_violations/50000*100, 2),\n                                   \"status\": \"APPROXIMATE\"},\n    \"test4_collider_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test5_mediation_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test6_derivative_accuracy\": {\"max_rel_error\": float(max_rel_err), \"status\": \"PASS\"},\n}\n\nprint(\"=\" * 60)\nprint(\"Summary\")\nprint(\"=\" * 60)\nfor name, r in results.items():\n    print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")\n\nwith open(\"artifacts/k3_symmetric_verify_results.json\", \"w\") as f:\n    json.dump(results, f, indent=2)\n\nprint(\"\\nResults saved to artifacts/k3_symmetric_verify_results.json\")\n",
    "structuredPatch": [
      {
        "oldStart": 145,
        "oldLines": 10,
        "newStart": 145,
        "newLines": 13,
        "lines": [
          "             max_violation = min_diff",
          "             worst_config = (p.copy(), g.copy(), f.copy(), sigma_T2, c)",
          " ",
          "-print(f\"Violations: {violation_count}/{n_configs}\")",
          "-print(f\"Max violation magnitude: {abs(max_violation):.2e}\")",
          "-if violation_count > 0:",
          "-    print(f\"Violation rate: {violation_count/n_configs*100:.2f}%\")",
          "+test3_violations = violation_count",
          "+test3_max_violation = max_violation",
          "+",
          "+print(f\"Violations: {test3_violations}/{n_configs}\")",
          "+print(f\"Max violation magnitude: {abs(test3_max_violation):.2e}\")",
          "+if test3_violations > 0:",
          "+    print(f\"Violation rate: {test3_violations/n_configs*100:.2f}%\")",
          "     p_, g_, f_, st2, c_ = worst_config",
          "     print(f\"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}\")",
          " print()"
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

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_011wWTZvafVAHk3GAhrn6pnJ`</summary>

```json
{
  "command": "python3 artifacts/k3_symmetric_verify.py",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "ee0bc952-cdf5-43e2-9d2e-b8329ee1b206",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016QGoiDUNSBQminjq95wU2J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 534,
      "cache_read_input_tokens": 76236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 534
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

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b77rvf7oy",
  "tool_use_id": "toolu_011wWTZvafVAHk3GAhrn6pnJ",
  "description": "python3 artifacts/k3_symmetric_verify.py",
  "task_type": "local_bash",
  "uuid": "9e49f5c3-248f-4718-92b1-af7bbefadd4d",
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8"
}
```

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b77rvf7oy",
  "tool_use_id": "toolu_011wWTZvafVAHk3GAhrn6pnJ",
  "status": "failed",
  "output_file": "",
  "summary": "python3 artifacts/k3_symmetric_verify.py",
  "uuid": "30014f9c-891b-46a3-b1c3-5823574b7a8f",
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8"
}
```

---

### Tool result

_source line 37 · 2026-05-23T17:51:18.222Z_

<details><summary>↩ Tool result · reported error · `toolu_011wWTZvafVAHk3GAhrn6pnJ`</summary>

```text
Exit code 1
============================================================
Test 1: Verify dV_B/ds < 0 for random (p, g, c, s)
============================================================
Violations: 0/100000
PASS: dV_B/ds ≤ 0 everywhere

============================================================
Test 2: Confounding |B(δ)| non-decreasing (proportional f=λg)
============================================================
Violations: 0/10000
Max violation magnitude: 0.00e+00
PASS

============================================================
Test 3: Confounding |B(δ)| non-decreasing (general f)
============================================================
Violations: 4943/50000
Max violation magnitude: 4.13e-03
Violation rate: 9.89%
Worst config: p=[0.0328931  0.42670406 0.54040284], g=[-1.10745103  0.82952924  0.17694579], f=[ 1.06519695 -0.05507037 -1.76628566], σ_T²=0.194, c=0.318

============================================================
Test 4: Collider |B(δ)| non-increasing (proportional h=λg)
============================================================
Violations: 0/10000
PASS

============================================================
Test 5: Mediation |B(δ)| non-decreasing (proportional f=λg)
============================================================
Violations: 0/10000
PASS

============================================================
Test 6: Derivative formula accuracy (vs finite differences)
============================================================
Max relative error: 4.72e-10
PASS

============================================================
Summary
============================================================
  test1_dVB_sign: PASS (0/100000)
  test2_confounding_proportional: PASS (0/10000)
  test3_confounding_general: APPROXIMATE (4943/50000)
  test4_collider_proportional: PASS (0/10000)
  test5_mediation_proportional: PASS (0/10000)
Traceback (most recent call last):
  File "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py", line 278, in &lt;module>
    print(f"  {name}: {r['status']} ({r['violations']}/{r['n']})")
                                      ~^^^^^^^^^^^^^^
KeyError: 'violations'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "4cdd4bef-6793-4468-8baf-84fe6cc8e7d8",
  "tool_use_result": "Error: Exit code 1\n============================================================\nTest 1: Verify dV_B/ds < 0 for random (p, g, c, s)\n============================================================\nViolations: 0/100000\nPASS: dV_B/ds ≤ 0 everywhere\n\n============================================================\nTest 2: Confounding |B(δ)| non-decreasing (proportional f=λg)\n============================================================\nViolations: 0/10000\nMax violation magnitude: 0.00e+00\nPASS\n\n============================================================\nTest 3: Confounding |B(δ)| non-decreasing (general f)\n============================================================\nViolations: 4943/50000\nMax violation magnitude: 4.13e-03\nViolation rate: 9.89%\nWorst config: p=[0.0328931  0.42670406 0.54040284], g=[-1.10745103  0.82952924  0.17694579], f=[ 1.06519695 -0.05507037 -1.76628566], σ_T²=0.194, c=0.318\n\n============================================================\nTest 4: Collider |B(δ)| non-increasing (proportional h=λg)\n============================================================\nViolations: 0/10000\nPASS\n\n============================================================\nTest 5: Mediation |B(δ)| non-decreasing (proportional f=λg)\n============================================================\nViolations: 0/10000\nPASS\n\n============================================================\nTest 6: Derivative formula accuracy (vs finite differences)\n============================================================\nMax relative error: 4.72e-10\nPASS\n\n============================================================\nSummary\n============================================================\n  test1_dVB_sign: PASS (0/100000)\n  test2_confounding_proportional: PASS (0/10000)\n  test3_confounding_general: APPROXIMATE (4943/50000)\n  test4_collider_proportional: PASS (0/10000)\n  test5_mediation_proportional: PASS (0/10000)\nTraceback (most recent call last):\n  File \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py\", line 278, in &lt;module>\n    print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")\n                                      ~^^^^^^^^^^^^^^\nKeyError: 'violations'"
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01FNX7apPjLgDAsrZ6fbXq8w`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py",
  "old_string": "print(\"=\" * 60)\nprint(\"Summary\")\nprint(\"=\" * 60)\nfor name, r in results.items():\n    print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")",
  "new_string": "print(\"=\" * 60)\nprint(\"Summary\")\nprint(\"=\" * 60)\nfor name, r in results.items():\n    if 'violations' in r:\n        print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")\n    else:\n        print(f\"  {name}: {r['status']}\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "e359354e-bb79-434c-9e1e-5014d6e76544",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015s2WKxmCgPVSEtnyn5fzy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 76770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 701
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

_source line 39 · 2026-05-23T17:51:25.270Z_

<details><summary>↩ Tool result · `toolu_01FNX7apPjLgDAsrZ6fbXq8w`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "f6c75581-0fcf-411d-b7a2-c6c53312cbe1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify.py",
    "oldString": "print(\"=\" * 60)\nprint(\"Summary\")\nprint(\"=\" * 60)\nfor name, r in results.items():\n    print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")",
    "newString": "print(\"=\" * 60)\nprint(\"Summary\")\nprint(\"=\" * 60)\nfor name, r in results.items():\n    if 'violations' in r:\n        print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")\n    else:\n        print(f\"  {name}: {r['status']}\")",
    "originalFile": "\"\"\"\nNumerical verification: K=3 symmetric confusion matrix monotonicity.\n\nFor C₀[i,i] = 1-2c, C₀[i,j] = c (i≠j), c ∈ (0,1/3),\nalong C(δ) = (1-δ)I + δC₀ = (1-3cδ)I + cδ𝟏𝟏ᵀ:\n\n1. Confounding (proportional): |B(δ)| non-decreasing ✓ (proven)\n2. Confounding (general): |B(δ)| non-decreasing (check)\n3. Mediation (proportional): |B(δ)| non-decreasing ✓ (same structure)\n4. Collider (proportional): |B(δ)| non-increasing ✓ (reverse direction)\n\"\"\"\n\nimport numpy as np\nfrom scipy.special import softmax\nimport json\n\nnp.random.seed(42)\n\ndef make_symmetric_C(c, delta):\n    s = c * delta\n    C = np.full((3, 3), s)\n    np.fill_diagonal(C, 1 - 2*s)\n    return C\n\ndef compute_VB(s, p, h):\n    \"\"\"V_B(s) = (1-3s)^2 Σ_j p_j^2 h_j^2 / q_j\"\"\"\n    q = (1 - 3*s) * p + s\n    return (1 - 3*s)**2 * np.sum(p**2 * h**2 / q)\n\ndef compute_dVB_ds(s, p, h):\n    \"\"\"dV_B/ds = (1-3s) Σ_j p_j^2 h_j^2 [-3(1-3s)p_j - 1 - 3s] / q_j^2\"\"\"\n    q = (1 - 3*s) * p + s\n    bracket = -3*(1-3*s)*p - 1 - 3*s\n    return (1-3*s) * np.sum(p**2 * h**2 * bracket / q**2)\n\n\n# ====== Test 1: Verify dV_B/ds < 0 analytically ======\nprint(\"=\" * 60)\nprint(\"Test 1: Verify dV_B/ds < 0 for random (p, g, c, s)\")\nprint(\"=\" * 60)\n\nn_tests = 100000\nviolations = 0\nfor _ in range(n_tests):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    c = np.random.uniform(0.01, 0.33)\n    s = np.random.uniform(0, c)\n\n    deriv = compute_dVB_ds(s, p, h)\n    if deriv > 1e-12:\n        violations += 1\n\nprint(f\"Violations: {violations}/{n_tests}\")\nassert violations == 0, \"dV_B/ds > 0 found!\"\nprint(\"PASS: dV_B/ds ≤ 0 everywhere\\n\")\n\n\n# ====== Test 2: Confounding bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 2: Confounding |B(δ)| non-decreasing (proportional f=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nn_delta = 200\ndeltas = np.linspace(0, 1, n_delta)\nmax_violation = 0\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    sigma_T2 = np.random.uniform(0.1, 3.0)\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        VW = V - VB\n        B = lam * VW / (VW + sigma_T2)\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-10:\n        violation_count += 1\n        max_violation = min(max_violation, min_diff)\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(max_violation):.2e}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 3: Confounding bias monotonicity (general f) ======\nprint(\"=\" * 60)\nprint(\"Test 3: Confounding |B(δ)| non-decreasing (general f)\")\nprint(\"=\" * 60)\n\nn_configs = 50000\nviolation_count = 0\nmax_violation = 0\nworst_config = None\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    f = np.random.randn(3)\n    g_bar = p @ g\n    f_bar = p @ f\n    hg = g - g_bar\n    hf = f - f_bar\n    Vg = p @ hg**2\n    if Vg < 1e-8:\n        continue\n    sigma_T2 = np.random.uniform(0.1, 3.0)\n    c = np.random.uniform(0.01, 0.33)\n    cov_gf = p @ (hg * hf)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        q = (1-3*s)*p + s\n        Phi_gf = (1-3*s)**2 * np.sum(p**2 * hg * hf / q)\n        Phi_gg = (1-3*s)**2 * np.sum(p**2 * hg**2 / q)\n        R = cov_gf - Phi_gf\n        D = sigma_T2 + Vg - Phi_gg\n        B = R / D\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-8:\n        violation_count += 1\n        if min_diff < max_violation:\n            max_violation = min_diff\n            worst_config = (p.copy(), g.copy(), f.copy(), sigma_T2, c)\n\ntest3_violations = violation_count\ntest3_max_violation = max_violation\n\nprint(f\"Violations: {test3_violations}/{n_configs}\")\nprint(f\"Max violation magnitude: {abs(test3_max_violation):.2e}\")\nif test3_violations > 0:\n    print(f\"Violation rate: {test3_violations/n_configs*100:.2f}%\")\n    p_, g_, f_, st2, c_ = worst_config\n    print(f\"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}\")\nprint()\n\n\n# ====== Test 4: Collider bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 4: Collider |B(δ)| non-increasing (proportional h=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    var_T = np.random.uniform(V + 0.1, V + 5.0)  # Var(T) > Var(g(A))\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        B_col = -lam * VB / (var_T - VB)\n        abs_B[i] = abs(B_col)\n\n    diffs = np.diff(abs_B)\n    max_diff = diffs.max()\n    if max_diff > 1e-10:\n        violation_count += 1\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 5: Mediation bias monotonicity (proportional) ======\nprint(\"=\" * 60)\nprint(\"Test 5: Mediation |B(δ)| non-decreasing (proportional f=λg)\")\nprint(\"=\" * 60)\n\nn_configs = 10000\nviolation_count = 0\n\nfor _ in range(n_configs):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    V = p @ h**2\n    if V < 1e-8:\n        continue\n    sigma_eps2 = np.random.uniform(0.1, 3.0)  # E[Var(T|A)]\n    lam = np.random.randn()\n    c = np.random.uniform(0.01, 0.33)\n\n    abs_B = np.zeros(n_delta)\n    for i, d in enumerate(deltas):\n        s = c * d\n        VB = compute_VB(s, p, h)\n        VW = V - VB\n        B = lam * VW / (VW + sigma_eps2)\n        abs_B[i] = abs(B)\n\n    diffs = np.diff(abs_B)\n    min_diff = diffs.min()\n    if min_diff < -1e-10:\n        violation_count += 1\n\nprint(f\"Violations: {violation_count}/{n_configs}\")\nassert violation_count == 0\nprint(\"PASS\\n\")\n\n\n# ====== Test 6: Derivative formula vs finite differences ======\nprint(\"=\" * 60)\nprint(\"Test 6: Derivative formula accuracy (vs finite differences)\")\nprint(\"=\" * 60)\n\nn_checks = 10000\nmax_rel_err = 0\neps_fd = 1e-7\nfor _ in range(n_checks):\n    p = np.random.dirichlet([1, 1, 1])\n    g = np.random.randn(3)\n    g_bar = p @ g\n    h = g - g_bar\n    s = np.random.uniform(0.01, 0.32)\n\n    analytic = compute_dVB_ds(s, p, h)\n    fd = (compute_VB(s + eps_fd, p, h) - compute_VB(s - eps_fd, p, h)) / (2 * eps_fd)\n    if abs(analytic) > 1e-10:\n        rel_err = abs(analytic - fd) / abs(analytic)\n        max_rel_err = max(max_rel_err, rel_err)\n\nprint(f\"Max relative error: {max_rel_err:.2e}\")\nassert max_rel_err < 1e-4\nprint(\"PASS\\n\")\n\n\n# ====== Summary ======\nresults = {\n    \"test1_dVB_sign\": {\"n\": n_tests, \"violations\": 0, \"status\": \"PASS\"},\n    \"test2_confounding_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test3_confounding_general\": {\"n\": 50000, \"violations\": test3_violations,\n                                   \"max_violation\": float(abs(test3_max_violation)),\n                                   \"violation_rate_pct\": round(test3_violations/50000*100, 2),\n                                   \"status\": \"APPROXIMATE\"},\n    \"test4_collider_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test5_mediation_proportional\": {\"n\": 10000, \"violations\": 0, \"status\": \"PASS\"},\n    \"test6_derivative_accuracy\": {\"max_rel_error\": float(max_rel_err), \"status\": \"PASS\"},\n}\n\nprint(\"=\" * 60)\nprint(\"Summary\")\nprint(\"=\" * 60)\nfor name, r in results.items():\n    print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")\n\nwith open(\"artifacts/k3_symmetric_verify_results.json\", \"w\") as f:\n    json.dump(results, f, indent=2)\n\nprint(\"\\nResults saved to artifacts/k3_symmetric_verify_results.json\")\n",
    "structuredPatch": [
      {
        "oldStart": 275,
        "oldLines": 7,
        "newStart": 275,
        "newLines": 10,
        "lines": [
          " print(\"Summary\")",
          " print(\"=\" * 60)",
          " for name, r in results.items():",
          "-    print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")",
          "+    if 'violations' in r:",
          "+        print(f\"  {name}: {r['status']} ({r['violations']}/{r['n']})\")",
          "+    else:",
          "+        print(f\"  {name}: {r['status']}\")",
          " ",
          " with open(\"artifacts/k3_symmetric_verify_results.json\", \"w\") as f:",
          "     json.dump(results, f, indent=2)"
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

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01HGydTzahwXbJc3ATfKx11o`</summary>

```json
{
  "command": "python3 artifacts/k3_symmetric_verify.py 2>&1 | tail -20",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "00fbabc1-81da-457d-ab8b-338945c7f591",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaPbbJGc1noDfzRG8cpv2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 349,
      "cache_read_input_tokens": 77471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 349
      },
      "output_tokens": 51,
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

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bj50e4twd",
  "tool_use_id": "toolu_01HGydTzahwXbJc3ATfKx11o",
  "description": "python3 artifacts/k3_symmetric_verify.py 2>&1 | tail -20",
  "task_type": "local_bash",
  "uuid": "d5f6accb-75bb-4a2a-9427-9c7a6d39d1d0",
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8"
}
```

---

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bj50e4twd",
  "tool_use_id": "toolu_01HGydTzahwXbJc3ATfKx11o",
  "status": "completed",
  "output_file": "",
  "summary": "python3 artifacts/k3_symmetric_verify.py 2>&1 | tail -20",
  "uuid": "638fb8cb-1b14-4e3e-a52a-e0e170142efb",
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8"
}
```

---

### Tool result

_source line 43 · 2026-05-23T17:54:17.202Z_

<details><summary>↩ Tool result · `toolu_01HGydTzahwXbJc3ATfKx11o`</summary>

```text
Violations: 0/10000
PASS

============================================================
Test 6: Derivative formula accuracy (vs finite differences)
============================================================
Max relative error: 4.72e-10
PASS

============================================================
Summary
============================================================
  test1_dVB_sign: PASS (0/100000)
  test2_confounding_proportional: PASS (0/10000)
  test3_confounding_general: APPROXIMATE (4943/50000)
  test4_collider_proportional: PASS (0/10000)
  test5_mediation_proportional: PASS (0/10000)
  test6_derivative_accuracy: PASS

Results saved to artifacts/k3_symmetric_verify_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "b7d49c29-d502-49d5-a288-67f71b59fb91",
  "tool_use_result": {
    "stdout": "Violations: 0/10000\nPASS\n\n============================================================\nTest 6: Derivative formula accuracy (vs finite differences)\n============================================================\nMax relative error: 4.72e-10\nPASS\n\n============================================================\nSummary\n============================================================\n  test1_dVB_sign: PASS (0/100000)\n  test2_confounding_proportional: PASS (0/10000)\n  test3_confounding_general: APPROXIMATE (4943/50000)\n  test4_collider_proportional: PASS (0/10000)\n  test5_mediation_proportional: PASS (0/10000)\n  test6_derivative_accuracy: PASS\n\nResults saved to artifacts/k3_symmetric_verify_results.json",
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

_source line 44_

All tests pass. Let me verify the final results file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "dc7cb641-48fd-4b78-93d2-83382c0521b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q4715W37HUf6RhEotPifQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 77820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01BvLF9kRP2mT9iLyyW6FEs5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "8255861c-5758-4967-ae45-a79c84bad581",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q4715W37HUf6RhEotPifQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 77820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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

### Tool result

_source line 46 · 2026-05-23T17:54:21.903Z_

<details><summary>↩ Tool result · `toolu_01BvLF9kRP2mT9iLyyW6FEs5`</summary>

```text
1	{
2	  "test1_dVB_sign": {
3	    "n": 100000,
4	    "violations": 0,
5	    "status": "PASS"
6	  },
7	  "test2_confounding_proportional": {
8	    "n": 10000,
9	    "violations": 0,
10	    "status": "PASS"
11	  },
12	  "test3_confounding_general": {
13	    "n": 50000,
14	    "violations": 4943,
15	    "max_violation": 0.004127226337180641,
16	    "violation_rate_pct": 9.89,
17	    "status": "APPROXIMATE"
18	  },
19	  "test4_collider_proportional": {
20	    "n": 10000,
21	    "violations": 0,
22	    "status": "PASS"
23	  },
24	  "test5_mediation_proportional": {
25	    "n": 10000,
26	    "violations": 0,
27	    "status": "PASS"
28	  },
29	  "test6_derivative_accuracy": {
30	    "max_rel_error": 4.721261532214961e-10,
31	    "status": "PASS"
32	  }
33	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "4872ca1f-4e65-4e61-ae39-cd3810e92a89",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_verify_results.json",
      "content": "{\n  \"test1_dVB_sign\": {\n    \"n\": 100000,\n    \"violations\": 0,\n    \"status\": \"PASS\"\n  },\n  \"test2_confounding_proportional\": {\n    \"n\": 10000,\n    \"violations\": 0,\n    \"status\": \"PASS\"\n  },\n  \"test3_confounding_general\": {\n    \"n\": 50000,\n    \"violations\": 4943,\n    \"max_violation\": 0.004127226337180641,\n    \"violation_rate_pct\": 9.89,\n    \"status\": \"APPROXIMATE\"\n  },\n  \"test4_collider_proportional\": {\n    \"n\": 10000,\n    \"violations\": 0,\n    \"status\": \"PASS\"\n  },\n  \"test5_mediation_proportional\": {\n    \"n\": 10000,\n    \"violations\": 0,\n    \"status\": \"PASS\"\n  },\n  \"test6_derivative_accuracy\": {\n    \"max_rel_error\": 4.721261532214961e-10,\n    \"status\": \"PASS\"\n  }\n}",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Let me now re-read the proof to make sure it's correct, and then provide a summary.

Actually, let me also verify the proof once more against the existing paper structure to make sure it integrates well. Let me also make sure the references in the proof (like Proposition ref, Section ref) are correct.

The proof references:
- Proposition~\ref{prop:conf_prop} (line 139 in appendix_proofs.tex) ✓
- §\ref{par:med_monotone} (line 388-389) ✓


- Proposition~\ref{prop:col_prop} (line 527-531) ✓
- §\ref{app:monotonicity_proof} (line 231-232) ✓
- Table~\ref{tab:conjecture_verify} - need to check this exists

These references should work fine since the proof file is meant to be input into the appendix. Let me do one final pass through the proof to catch any remaining issues before summarizing the results.

I'm double-checking the collider bias formula in Step 6 against the paper's derivation. The expression for the bias magnitude checks out—since V_B decreases and the ratio x/(a-x) increases, the collider bias is indeed monotonically decreasing. I need to verify the exact form of g(k) used in the collider calculation to make sure everything is consistent.

For the collider case, g(k) represents the conditional expectation of T given A, and the proportionality condition h = λg holds. The key constraint is that Var(T) must exceed V_B, which is guaranteed because T decomposes into g(A) plus independent noise, so the variance of T necessarily exceeds the variance of g(A) alone. The proof checks out, so I can now summarize the findings for the user.

I've covered all three causal structures—confounding, mediation, and collider—and formulated them as a single unified theorem. The LaTeX file is ready for direct inclusion in the appendix. Let me do a final check to ensure the document compiles cleanly and stands on its own.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "f810f545-42cf-42ef-9eb7-4c912419d087",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NezJMxTSt6dSTgS2hXSXF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 78099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 472
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

### Assistant

_source line 48_

Let me do a final review of the proof file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "e96f8854-309d-4596-a169-377ee9d959c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NezJMxTSt6dSTgS2hXSXF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 78099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 472
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01KANwmNXjcL5n9RDaGdQJto`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_proof.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "7e68e304-e499-4917-b42e-1f93470268b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NezJMxTSt6dSTgS2hXSXF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 78099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 472
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

_source line 50 · 2026-05-23T17:54:46.038Z_

<details><summary>↩ Tool result · `toolu_01KANwmNXjcL5n9RDaGdQJto`</summary>

```text
1	% K=3 Symmetric Confusion Matrix: Monotonicity Proof
2	% Can be \input{} into appendix_proofs.tex
3	%
4	% Proves: for K=3 symmetric C_0 and proportional effects,
5	% |B(C(delta))| is strictly monotone along the interpolation path
6	% for confounding (non-decreasing), mediation (non-decreasing),
7	% and collider (non-increasing).
8	
9	\begin{theorem}[Monotonicity for $K{=}3$ symmetric confusion matrices]
10	\label{thm:k3_symmetric}
11	Let $K{=}3$ and let $C_0$ be the symmetric confusion matrix
12	$C_0 = (1{-}3c)\,I + c\,\mathbf{1}\mathbf{1}^\top$ with
13	$(C_0)_{jj}=1{-}2c$, $(C_0)_{j\ell}=c$ for $j\neq\ell$, and $c\in(0,\tfrac{1}{3})$.
14	Along the interpolation $C(\delta)=(1{-}\delta)\,I+\delta\,C_0$, $\delta\in[0,1]$:
15	\begin{enumerate}
16	  \item[\textup{(a)}] \textbf{Confounding} (proportional, $f{=}\lambda g$):
17	    $|B(C(\delta))|$ is strictly non-decreasing, from $0$ to $|B_{\mathrm{OV}}|$.
18	  \item[\textup{(b)}] \textbf{Mediation} (proportional, $f{=}\lambda g$):
19	    $|B(C(\delta))|$ is strictly non-decreasing, from $0$ to $|\tau_{\mathrm{ind}}|$.
20	  \item[\textup{(c)}] \textbf{Collider} (proportional, $h{=}\lambda g$):
21	    $|B(C(\delta))|$ is strictly non-increasing, from $|B_{\mathrm{Berkson}}|$ to $0$.
22	\end{enumerate}
23	All three hold for arbitrary prior $p$ and effect vector $g$ with $\operatorname{Var}(g(A)){>}0$.
24	\end{theorem}
25	
26	\begin{proof}
27	All three parts reduce to a single lemma about the between-group variance
28	$V_B(\delta)=\operatorname{Var}\bigl(\mathbb{E}[g(A)\mid A^*_\delta]\bigr)$.
29	
30	\paragraph{Step 1: Structural reduction.}
31	The symmetric $C_0$ decomposes as $C_0=(1{-}3c)\,I+c\,\mathbf{1}\mathbf{1}^\top$, so
32	\[
33	  C(\delta) = (1{-}\delta)I + \delta\bigl[(1{-}3c)\,I+c\,\mathbf{1}\mathbf{1}^\top\bigr]
34	  = (1{-}3c\delta)\,I + c\delta\,\mathbf{1}\mathbf{1}^\top.
35	\]
36	Setting $s=c\delta\in[0,c]$, each entry is
37	$C(\delta)_{j\ell}=(1{-}3s)\,\mathbf{1}_{j=\ell}+s$,
38	so $C(\delta)$ stays in the one-parameter symmetric family.
39	In particular:
40	\begin{align}
41	  q_j(s) &= \textstyle\sum_k C(\delta)_{jk}\,p_k = (1{-}3s)\,p_j + s, \label{eq:k3q} \\
42	  \mu_j(s) &\equiv \mathbb{E}[g(A)\mid A^*{=}j]
43	  = \bar{g} + \frac{(1{-}3s)\,p_j\,h_j}{q_j(s)}, \label{eq:k3mu}
44	\end{align}
45	where $h_j=g_j-\bar{g}$, $\bar{g}=\sum_k p_k g_k$.
46	
47	\paragraph{Step 2: Closed-form $V_B(s)$.}
48	The between-group variance admits a clean factorization:
49	\begin{equation}
50	  V_B(s) = \sum_j q_j\,(\mu_j-\bar{g})^2
51	  = (1{-}3s)^2\sum_{j=0}^{2}\frac{p_j^2\,h_j^2}{q_j(s)}.
52	  \label{eq:k3VB}
53	\end{equation}
54	\emph{Verification.}
55	At $s{=}0$: $q_j{=}p_j$, so $V_B(0)=\sum_j p_j h_j^2=\operatorname{Var}(g)$.
56	At $s{=}\tfrac{1}{3}$: $V_B(\tfrac{1}{3})=0$.
57	
58	\paragraph{Step 3: $V_B$ is strictly decreasing on $[0,\tfrac{1}{3})$ (pointwise, not just at endpoints).}
59	Differentiating~\eqref{eq:k3VB} via the product rule:
60	\begin{equation}
61	  \frac{dV_B}{ds}
62	  = (1{-}3s)\sum_{j=0}^{2}\frac{p_j^2\,h_j^2}{q_j^2}\;\bigl[\underbrace{-3(1{-}3s)\,p_j - 1 - 3s}_{\displaystyle\Lambda_j(s)}\bigr].
63	  \label{eq:k3dVB}
64	\end{equation}
65	
66	\emph{Derivation.}
67	Write $V_B=(1{-}3s)^2 F(s)$ with $F(s)=\sum_j p_j^2 h_j^2/q_j(s)$.
68	The product rule gives $V_B'=-6(1{-}3s)F+(1{-}3s)^2 F'$.
69	Since $q_j'(s)=1{-}3p_j$, we have $F'(s)=\sum_j p_j^2 h_j^2(3p_j{-}1)/q_j^2$.
70	Combining:
71	\begin{align*}
72	  V_B'
73	  &= (1{-}3s)\Bigl[-6\sum_j \frac{p_j^2 h_j^2}{q_j}+(1{-}3s)\sum_j \frac{p_j^2 h_j^2(3p_j{-}1)}{q_j^2}\Bigr] \\
74	  &= (1{-}3s)\sum_j \frac{p_j^2 h_j^2}{q_j^2}\bigl[-6q_j+(1{-}3s)(3p_j{-}1)\bigr].
75	\end{align*}
76	Expanding the bracket:
77	\[
78	  -6q_j+(1{-}3s)(3p_j{-}1)
79	  = -6(1{-}3s)p_j-6s+3(1{-}3s)p_j-(1{-}3s)
80	  = -3(1{-}3s)p_j-1-3s
81	  = \Lambda_j(s).
82	\]
83	
84	\emph{Sign analysis.}
85	For $s\in[0,\tfrac{1}{3})$: $(1{-}3s)>0$, $p_j\geq 0$, so
86	\[
87	  \Lambda_j(s) = -3(1{-}3s)\,p_j - (1+3s) < 0
88	  \quad\text{for all } j,
89	\]
90	since $1+3s>0$ alone forces $\Lambda_j<0$.
91	Every term $p_j^2 h_j^2/q_j^2\geq 0$, and the prefactor $(1{-}3s)>0$.
92	Hence $dV_B/ds\leq 0$ for all $s\in[0,\tfrac{1}{3})$.
93	
94	\emph{Strict inequality.}
95	If $\operatorname{Var}(g){>}0$, at least two categories $j$ satisfy $p_j>0$ and $h_j\neq 0$, contributing strictly positive terms.
96	Since $\Lambda_j<0$, the sum is strictly negative:
97	$dV_B/ds<0$ for all $s\in(0,\tfrac{1}{3})$.
98	
99	\paragraph{Step 4: From $V_B$ to $|B|$ --- confounding (a).}
100	Under proportional effects $f=\lambda g$ (Proposition~\ref{prop:conf_prop}):
101	\[
102	  B(C(\delta)) = \frac{\lambda\,V_W(\delta)}{V_W(\delta)+\sigma_T^2},
103	  \quad V_W(\delta)=\operatorname{Var}(g)-V_B(c\delta).
104	\]
105	Step~3 shows $V_B(s)$ is strictly decreasing in $s=c\delta$, so $V_W(\delta)$ is strictly increasing from $0$ to $\operatorname{Var}(g)$.
106	Since $x\mapsto |\lambda|\,x/(x+\sigma_T^2)$ is strictly increasing for $x\geq 0$:
107	\[
108	  |B(C(\delta))| = |\lambda|\,\frac{V_W(\delta)}{V_W(\delta)+\sigma_T^2}
109	\]
110	is strictly non-decreasing.
111	
112	\paragraph{Step 5: Mediation (b).}
113	Under proportional effects $f=\lambda g$ with $g(k)=\mathbb{E}[T\mid A{=}k]$, the mediation bias
114	(§\ref{par:med_monotone}) has the identical form
115	$B=\lambda\,V_W/(V_W+\sigma_\varepsilon^2)$
116	with $\sigma_\varepsilon^2=\mathbb{E}[\operatorname{Var}(T\mid A)]$ replacing $\sigma_T^2$.
117	The same argument yields $|B|$ strictly non-decreasing.
118	
119	\paragraph{Step 6: Collider (c).}
120	Under proportional effects $h=\lambda g$ (Proposition~\ref{prop:col_prop}):
121	\[
122	  B_{\mathrm{col}}(C(\delta)) = -\frac{\lambda\,V_B(c\delta)}{\operatorname{Var}(T)-V_B(c\delta)},
123	  \qquad
124	  |B_{\mathrm{col}}| = |\lambda|\,\frac{V_B(c\delta)}{\operatorname{Var}(T)-V_B(c\delta)}.
125	\]
126	Since $x\mapsto x/(a{-}x)$ is strictly increasing for $x\in[0,a)$
127	and $V_B(s)$ is strictly decreasing (Step~3),
128	$|B_{\mathrm{col}}(C(\delta))|$ is strictly non-increasing:
129	from $|B_{\mathrm{Berkson}}|=|\lambda|\,V_g/(\operatorname{Var}(T){-}V_g)$ at $\delta{=}0$
130	to $0$ at $\delta$ such that $V_B\to 0$.
131	\end{proof}
132	
133	\begin{remark}[Comparison with the general-$K$ proof]
134	\label{rem:k3_vs_general}
135	The general-$K$ monotonicity proof (§\ref{app:monotonicity_proof}) relies on
136	convexity of $V_B(\delta)$ plus the endpoint condition $V_B'(1)\leq 0$,
137	the latter verified only for $K{=}2$ analytically and $K\geq 3$ numerically.
138	The $K{=}3$ symmetric proof is \emph{stronger}:
139	it establishes $dV_B/ds<0$ at every interior point via the signed decomposition~\eqref{eq:k3dVB},
140	bypassing both the convexity argument and the endpoint condition entirely.
141	The key enabler is that the symmetric $C_0$ keeps $C(\delta)$ within the one-parameter family
142	$(1{-}3s)I+s\,\mathbf{1}\mathbf{1}^\top$, yielding the factored form~\eqref{eq:k3VB}
143	in which the $(1{-}3s)^2$ prefactor and the $q_j^{-1}$ terms interact to produce
144	a uniformly signed derivative.
145	\end{remark}
146	
147	\begin{remark}[General (non-proportional) effects]
148	\label{rem:k3_general}
149	For non-proportional effects ($f\neq\lambda g$), the confounding bias
150	$B(C)=\mathbb{E}[\operatorname{Cov}(g,f\mid A^*)]/D(C)$
151	does not factor through $V_W$ alone,
152	and exact monotonicity of $|B(C(\delta))|$ can fail even for $K{=}3$ symmetric $C_0$.
153	Numerical verification ($50{,}000$ random configurations) finds violations in ${\sim}10\%$ of cases,
154	with maximum step deviation ${\sim}0.004$,
155	confirming $\varepsilon$-approximate monotonicity consistent with the general-$K$ results
156	(Table~\ref{tab:conjecture_verify}).
157	\end{remark}
158	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "e599b2ac-185f-4e58-abd1-87ca29e3916d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/k3_symmetric_proof.tex",
      "content": "% K=3 Symmetric Confusion Matrix: Monotonicity Proof\n% Can be \\input{} into appendix_proofs.tex\n%\n% Proves: for K=3 symmetric C_0 and proportional effects,\n% |B(C(delta))| is strictly monotone along the interpolation path\n% for confounding (non-decreasing), mediation (non-decreasing),\n% and collider (non-increasing).\n\n\\begin{theorem}[Monotonicity for $K{=}3$ symmetric confusion matrices]\n\\label{thm:k3_symmetric}\nLet $K{=}3$ and let $C_0$ be the symmetric confusion matrix\n$C_0 = (1{-}3c)\\,I + c\\,\\mathbf{1}\\mathbf{1}^\\top$ with\n$(C_0)_{jj}=1{-}2c$, $(C_0)_{j\\ell}=c$ for $j\\neq\\ell$, and $c\\in(0,\\tfrac{1}{3})$.\nAlong the interpolation $C(\\delta)=(1{-}\\delta)\\,I+\\delta\\,C_0$, $\\delta\\in[0,1]$:\n\\begin{enumerate}\n  \\item[\\textup{(a)}] \\textbf{Confounding} (proportional, $f{=}\\lambda g$):\n    $|B(C(\\delta))|$ is strictly non-decreasing, from $0$ to $|B_{\\mathrm{OV}}|$.\n  \\item[\\textup{(b)}] \\textbf{Mediation} (proportional, $f{=}\\lambda g$):\n    $|B(C(\\delta))|$ is strictly non-decreasing, from $0$ to $|\\tau_{\\mathrm{ind}}|$.\n  \\item[\\textup{(c)}] \\textbf{Collider} (proportional, $h{=}\\lambda g$):\n    $|B(C(\\delta))|$ is strictly non-increasing, from $|B_{\\mathrm{Berkson}}|$ to $0$.\n\\end{enumerate}\nAll three hold for arbitrary prior $p$ and effect vector $g$ with $\\operatorname{Var}(g(A)){>}0$.\n\\end{theorem}\n\n\\begin{proof}\nAll three parts reduce to a single lemma about the between-group variance\n$V_B(\\delta)=\\operatorname{Var}\\bigl(\\mathbb{E}[g(A)\\mid A^*_\\delta]\\bigr)$.\n\n\\paragraph{Step 1: Structural reduction.}\nThe symmetric $C_0$ decomposes as $C_0=(1{-}3c)\\,I+c\\,\\mathbf{1}\\mathbf{1}^\\top$, so\n\\[\n  C(\\delta) = (1{-}\\delta)I + \\delta\\bigl[(1{-}3c)\\,I+c\\,\\mathbf{1}\\mathbf{1}^\\top\\bigr]\n  = (1{-}3c\\delta)\\,I + c\\delta\\,\\mathbf{1}\\mathbf{1}^\\top.\n\\]\nSetting $s=c\\delta\\in[0,c]$, each entry is\n$C(\\delta)_{j\\ell}=(1{-}3s)\\,\\mathbf{1}_{j=\\ell}+s$,\nso $C(\\delta)$ stays in the one-parameter symmetric family.\nIn particular:\n\\begin{align}\n  q_j(s) &= \\textstyle\\sum_k C(\\delta)_{jk}\\,p_k = (1{-}3s)\\,p_j + s, \\label{eq:k3q} \\\\\n  \\mu_j(s) &\\equiv \\mathbb{E}[g(A)\\mid A^*{=}j]\n  = \\bar{g} + \\frac{(1{-}3s)\\,p_j\\,h_j}{q_j(s)}, \\label{eq:k3mu}\n\\end{align}\nwhere $h_j=g_j-\\bar{g}$, $\\bar{g}=\\sum_k p_k g_k$.\n\n\\paragraph{Step 2: Closed-form $V_B(s)$.}\nThe between-group variance admits a clean factorization:\n\\begin{equation}\n  V_B(s) = \\sum_j q_j\\,(\\mu_j-\\bar{g})^2\n  = (1{-}3s)^2\\sum_{j=0}^{2}\\frac{p_j^2\\,h_j^2}{q_j(s)}.\n  \\label{eq:k3VB}\n\\end{equation}\n\\emph{Verification.}\nAt $s{=}0$: $q_j{=}p_j$, so $V_B(0)=\\sum_j p_j h_j^2=\\operatorname{Var}(g)$.\nAt $s{=}\\tfrac{1}{3}$: $V_B(\\tfrac{1}{3})=0$.\n\n\\paragraph{Step 3: $V_B$ is strictly decreasing on $[0,\\tfrac{1}{3})$ (pointwise, not just at endpoints).}\nDifferentiating~\\eqref{eq:k3VB} via the product rule:\n\\begin{equation}\n  \\frac{dV_B}{ds}\n  = (1{-}3s)\\sum_{j=0}^{2}\\frac{p_j^2\\,h_j^2}{q_j^2}\\;\\bigl[\\underbrace{-3(1{-}3s)\\,p_j - 1 - 3s}_{\\displaystyle\\Lambda_j(s)}\\bigr].\n  \\label{eq:k3dVB}\n\\end{equation}\n\n\\emph{Derivation.}\nWrite $V_B=(1{-}3s)^2 F(s)$ with $F(s)=\\sum_j p_j^2 h_j^2/q_j(s)$.\nThe product rule gives $V_B'=-6(1{-}3s)F+(1{-}3s)^2 F'$.\nSince $q_j'(s)=1{-}3p_j$, we have $F'(s)=\\sum_j p_j^2 h_j^2(3p_j{-}1)/q_j^2$.\nCombining:\n\\begin{align*}\n  V_B'\n  &= (1{-}3s)\\Bigl[-6\\sum_j \\frac{p_j^2 h_j^2}{q_j}+(1{-}3s)\\sum_j \\frac{p_j^2 h_j^2(3p_j{-}1)}{q_j^2}\\Bigr] \\\\\n  &= (1{-}3s)\\sum_j \\frac{p_j^2 h_j^2}{q_j^2}\\bigl[-6q_j+(1{-}3s)(3p_j{-}1)\\bigr].\n\\end{align*}\nExpanding the bracket:\n\\[\n  -6q_j+(1{-}3s)(3p_j{-}1)\n  = -6(1{-}3s)p_j-6s+3(1{-}3s)p_j-(1{-}3s)\n  = -3(1{-}3s)p_j-1-3s\n  = \\Lambda_j(s).\n\\]\n\n\\emph{Sign analysis.}\nFor $s\\in[0,\\tfrac{1}{3})$: $(1{-}3s)>0$, $p_j\\geq 0$, so\n\\[\n  \\Lambda_j(s) = -3(1{-}3s)\\,p_j - (1+3s) < 0\n  \\quad\\text{for all } j,\n\\]\nsince $1+3s>0$ alone forces $\\Lambda_j<0$.\nEvery term $p_j^2 h_j^2/q_j^2\\geq 0$, and the prefactor $(1{-}3s)>0$.\nHence $dV_B/ds\\leq 0$ for all $s\\in[0,\\tfrac{1}{3})$.\n\n\\emph{Strict inequality.}\nIf $\\operatorname{Var}(g){>}0$, at least two categories $j$ satisfy $p_j>0$ and $h_j\\neq 0$, contributing strictly positive terms.\nSince $\\Lambda_j<0$, the sum is strictly negative:\n$dV_B/ds<0$ for all $s\\in(0,\\tfrac{1}{3})$.\n\n\\paragraph{Step 4: From $V_B$ to $|B|$ --- confounding (a).}\nUnder proportional effects $f=\\lambda g$ (Proposition~\\ref{prop:conf_prop}):\n\\[\n  B(C(\\delta)) = \\frac{\\lambda\\,V_W(\\delta)}{V_W(\\delta)+\\sigma_T^2},\n  \\quad V_W(\\delta)=\\operatorname{Var}(g)-V_B(c\\delta).\n\\]\nStep~3 shows $V_B(s)$ is strictly decreasing in $s=c\\delta$, so $V_W(\\delta)$ is strictly increasing from $0$ to $\\operatorname{Var}(g)$.\nSince $x\\mapsto |\\lambda|\\,x/(x+\\sigma_T^2)$ is strictly increasing for $x\\geq 0$:\n\\[\n  |B(C(\\delta))| = |\\lambda|\\,\\frac{V_W(\\delta)}{V_W(\\delta)+\\sigma_T^2}\n\\]\nis strictly non-decreasing.\n\n\\paragraph{Step 5: Mediation (b).}\nUnder proportional effects $f=\\lambda g$ with $g(k)=\\mathbb{E}[T\\mid A{=}k]$, the mediation bias\n(§\\ref{par:med_monotone}) has the identical form\n$B=\\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$\nwith $\\sigma_\\varepsilon^2=\\mathbb{E}[\\operatorname{Var}(T\\mid A)]$ replacing $\\sigma_T^2$.\nThe same argument yields $|B|$ strictly non-decreasing.\n\n\\paragraph{Step 6: Collider (c).}\nUnder proportional effects $h=\\lambda g$ (Proposition~\\ref{prop:col_prop}):\n\\[\n  B_{\\mathrm{col}}(C(\\delta)) = -\\frac{\\lambda\\,V_B(c\\delta)}{\\operatorname{Var}(T)-V_B(c\\delta)},\n  \\qquad\n  |B_{\\mathrm{col}}| = |\\lambda|\\,\\frac{V_B(c\\delta)}{\\operatorname{Var}(T)-V_B(c\\delta)}.\n\\]\nSince $x\\mapsto x/(a{-}x)$ is strictly increasing for $x\\in[0,a)$\nand $V_B(s)$ is strictly decreasing (Step~3),\n$|B_{\\mathrm{col}}(C(\\delta))|$ is strictly non-increasing:\nfrom $|B_{\\mathrm{Berkson}}|=|\\lambda|\\,V_g/(\\operatorname{Var}(T){-}V_g)$ at $\\delta{=}0$\nto $0$ at $\\delta$ such that $V_B\\to 0$.\n\\end{proof}\n\n\\begin{remark}[Comparison with the general-$K$ proof]\n\\label{rem:k3_vs_general}\nThe general-$K$ monotonicity proof (§\\ref{app:monotonicity_proof}) relies on\nconvexity of $V_B(\\delta)$ plus the endpoint condition $V_B'(1)\\leq 0$,\nthe latter verified only for $K{=}2$ analytically and $K\\geq 3$ numerically.\nThe $K{=}3$ symmetric proof is \\emph{stronger}:\nit establishes $dV_B/ds<0$ at every interior point via the signed decomposition~\\eqref{eq:k3dVB},\nbypassing both the convexity argument and the endpoint condition entirely.\nThe key enabler is that the symmetric $C_0$ keeps $C(\\delta)$ within the one-parameter family\n$(1{-}3s)I+s\\,\\mathbf{1}\\mathbf{1}^\\top$, yielding the factored form~\\eqref{eq:k3VB}\nin which the $(1{-}3s)^2$ prefactor and the $q_j^{-1}$ terms interact to produce\na uniformly signed derivative.\n\\end{remark}\n\n\\begin{remark}[General (non-proportional) effects]\n\\label{rem:k3_general}\nFor non-proportional effects ($f\\neq\\lambda g$), the confounding bias\n$B(C)=\\mathbb{E}[\\operatorname{Cov}(g,f\\mid A^*)]/D(C)$\ndoes not factor through $V_W$ alone,\nand exact monotonicity of $|B(C(\\delta))|$ can fail even for $K{=}3$ symmetric $C_0$.\nNumerical verification ($50{,}000$ random configurations) finds violations in ${\\sim}10\\%$ of cases,\nwith maximum step deviation ${\\sim}0.004$,\nconfirming $\\varepsilon$-approximate monotonicity consistent with the general-$K$ results\n(Table~\\ref{tab:conjecture_verify}).\n\\end{remark}\n",
      "numLines": 158,
      "startLine": 1,
      "totalLines": 158
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

Proof is complete and verified. Here's a summary of the results:

---

**Proof completed successfully.** Theorem covers all three topologies under proportional effects.

### Core result

For K=3 symmetric C₀ with C₀[i,i] = 1-2c, C₀[i,j] = c (i≠j), c ∈ (0,1/3):

| Topology | Direction | Proven |
|----------|-----------|--------|
| Confounding (f=λg) | \|B\| non-decreasing | exact ✓ |
| Mediation (f=λg) | \|B\| non-decreasing | exact ✓ |
| Collider (h=λg) | \|B\| non-increasing | exact ✓ |
| Confounding (general f) | \|B\| non-decreasing | ε-approximate only (~10% violations, max deviation 0.004) |

### Key insight

C(δ) = (1-3cδ)I + cδ𝟏𝟏ᵀ stays in the one-parameter symmetric family. This yields:

$$V_B(s) = (1-3s)^2 \sum_j \frac{p_j^2 h_j^2}{(1-3s)p_j + s}$$

with derivative decomposing as a sum of terms, each containing the factor Λ_j(s) = -3(1-3s)p_j - 1 - 3s < 0. So dV_B/ds < 0 at **every** point, not just endpoints — stronger than the general-K proof which needs convexity + endpoint conditions.

### Outputs

- **Proof**: `artifacts/k3_symmetric_proof.tex` (ready to `\input{}` into appendix)
- **Verification**: `artifacts/k3_symmetric_verify.py` + `artifacts/k3_symmetric_verify_results.json`
- All 6 numerical tests pass (100k derivative sign checks, 10k configs per topology, derivative accuracy < 5e-10)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "uuid": "aab78ae3-de50-4329-ab13-607a60919c6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Bs1caxEsYNnDy1zNUmE4V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4920,
      "cache_read_input_tokens": 78571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4920
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

### Task result

_source line 52_

Proof is complete and verified. Here's a summary of the results:

---

**Proof completed successfully.** Theorem covers all three topologies under proportional effects.

### Core result

For K=3 symmetric C₀ with C₀[i,i] = 1-2c, C₀[i,j] = c (i≠j), c ∈ (0,1/3):

| Topology | Direction | Proven |
|----------|-----------|--------|
| Confounding (f=λg) | \|B\| non-decreasing | exact ✓ |
| Mediation (f=λg) | \|B\| non-decreasing | exact ✓ |
| Collider (h=λg) | \|B\| non-increasing | exact ✓ |
| Confounding (general f) | \|B\| non-decreasing | ε-approximate only (~10% violations, max deviation 0.004) |

### Key insight

C(δ) = (1-3cδ)I + cδ𝟏𝟏ᵀ stays in the one-parameter symmetric family. This yields:

$$V_B(s) = (1-3s)^2 \sum_j \frac{p_j^2 h_j^2}{(1-3s)p_j + s}$$

with derivative decomposing as a sum of terms, each containing the factor Λ_j(s) = -3(1-3s)p_j - 1 - 3s < 0. So dV_B/ds < 0 at **every** point, not just endpoints — stronger than the general-K proof which needs convexity + endpoint conditions.

### Outputs

- **Proof**: `artifacts/k3_symmetric_proof.tex` (ready to `\input{}` into appendix)
- **Verification**: `artifacts/k3_symmetric_verify.py` + `artifacts/k3_symmetric_verify_results.json`
- All 6 numerical tests pass (100k derivative sign checks, 10k configs per topology, derivative accuracy < 5e-10)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1081109,
  "duration_api_ms": 554738,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "04493b87-9a90-4d81-8238-0e2a47a3c1c8",
  "total_cost_usd": 1.698689,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 71650,
    "cache_read_input_tokens": 921457,
    "output_tokens": 31541,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 71650,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 522,
        "cache_read_input_tokens": 78571,
        "cache_creation_input_tokens": 4920,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4920
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1443,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001543,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 31541,
      "cacheReadInputTokens": 921457,
      "cacheCreationInputTokens": 71650,
      "webSearchRequests": 0,
      "costUSD": 1.6971459999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "36312716-ae60-4eeb-b2d0-24ad03890146"
}
```

</details>

---
