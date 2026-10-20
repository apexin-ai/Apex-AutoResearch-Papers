# Research conversation: Read these files completely and extract EVERY numerical claim (percentages, decimals, counts, ranges). For each number, 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a20940d9e1e09d4c5.jsonl`
- **Structured JSON:** [`43b8f27945efe8ea46df.json`](../../sessions/43/43b8f27945efe8ea46df.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-23T19:17:34.528Z_

Read these files completely and extract EVERY numerical claim (percentages, decimals, counts, ranges). For each number, note the exact value, the surrounding context sentence, and the line number.

Files:
1. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex
2. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex (this is long ~1400 lines, read in chunks: lines 1-500, 501-1000, 1001-end)

Report format for each number:
- [file:line:N] "exact quote with the number" → value: X

Be exhaustive for data claims. Skip pure math constants (1.96, π), section/equation references, citation years. For appendix tables, capture every cell value.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6231d775-db71-46d9-bac6-397081d485cb",
  "agentId": "a20940d9e1e09d4c5",
  "type": "user",
  "uuid": "bc339efb-2ea4-4af1-a96e-e3a61af2eb09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T19:17:35.939Z_

I'll read these files completely and extract all numerical claims. Let me start by reading both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc339efb-2ea4-4af1-a96e-e3a61af2eb09",
  "isSidechain": true,
  "agentId": "a20940d9e1e09d4c5",
  "requestId": "req_011CbL3ByS6T665wtJ78caNV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7eb3d3c6-ef88-4966-8d2b-165f3987ca7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BkbQicPLSWXDNQpe5quzY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 17330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 649,
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

_source line 3 · 2026-05-23T19:17:36.197Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cb7QvKTYQHYfaj3e3LSPkY`</summary>

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
  "parentUuid": "7eb3d3c6-ef88-4966-8d2b-165f3987ca7f",
  "isSidechain": true,
  "agentId": "a20940d9e1e09d4c5",
  "requestId": "req_011CbL3ByS6T665wtJ78caNV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "85a6e470-335b-40a7-ad69-dc7df7f8b5f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BkbQicPLSWXDNQpe5quzY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 17330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 649,
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

_source line 4 · 2026-05-23T19:17:36.205Z_

<details><summary>↩ Tool result · `toolu_01Cb7QvKTYQHYfaj3e3LSPkY`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: at $K{\geq}3$, exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs yield a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective for four covariate topologies (FWL invariance). Practitioners should identify their topology and compute ASV before selecting corrections.
5	
6	\section*{Limitations}
7	
8	We assume non-differential misclassification (Appendix~\ref{sec:nondiff_stress}). Closed-form results (Theorems~1--2) assume linear SEMs with proportional effects ($f{=}\lambda g$); logistic robustness is verified in Appendix~\ref{sec:fwl_nonlinear}, and sign preservation holds at 97.3\% under non-proportional effects (Table~\ref{tab:proportional_empirical}), though $\lambda(C)$ falls outside $[0,1]$ in 15\% of configurations; under nonlinear models, FWL invariance may break, enabling matrix-based corrections. Proving general $K{\geq}3$ envelope monotonicity beyond symmetric matrices remains open~\cite{schennach2020mismeasured}.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85a6e470-335b-40a7-ad69-dc7df7f8b5f9",
  "isSidechain": true,
  "promptId": "6231d775-db71-46d9-bac6-397081d485cb",
  "agentId": "a20940d9e1e09d4c5",
  "type": "user",
  "uuid": "0b70b3e4-12aa-4d90-ad3e-b33157cb4f09",
  "sourceToolAssistantUUID": "85a6e470-335b-40a7-ad69-dc7df7f8b5f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T19:17:36.388Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GAaBvjGWabeYYRpfXPqd5x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b70b3e4-12aa-4d90-ad3e-b33157cb4f09",
  "isSidechain": true,
  "agentId": "a20940d9e1e09d4c5",
  "requestId": "req_011CbL3ByS6T665wtJ78caNV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "82d4171c-d418-4271-817d-8d9db368a760",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BkbQicPLSWXDNQpe5quzY2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 17330,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 649
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 17330,
          "cache_creation_input_tokens": 649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 649,
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

_source line 6 · 2026-05-23T19:17:36.706Z_

<details><summary>↩ Tool result · `toolu_01GAaBvjGWabeYYRpfXPqd5x`</summary>

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
151	  \;\in\;[0,1].
152	\]
153	Consequently, $B(C)$ lies between $0$ and $B_{\mathrm{OV}}$, and $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{OV}})$.
154	\end{proposition}
155	
156	\begin{proof}
157	When $f=\lambda g$: the between-group covariance in~\eqref{eq:lotc} becomes $\lambda\,\operatorname{Var}(\mathbb{E}[g\mid A^*])$, and $\operatorname{Cov}(g,f)=\lambda\,\operatorname{Var}(g)$.
158	So $R(C)=\lambda\bigl(\operatorname{Var}(g)-\operatorname{Var}(\mathbb{E}[g\mid A^*])\bigr)=\lambda\,V_W$, where $V_W=\operatorname{Var}(g)-V_B$ with $V_B=\operatorname{Var}(\mathbb{E}[g\mid A^*])$.
159	Similarly, $D(C)=V_W+\sigma_T^2$.
160	Hence
161	\[
162	  B(C) = \frac{\lambda\,V_W}{V_W+\sigma_T^2},\qquad
163	  B_{\mathrm{OV}} = \frac{\lambda\,V}{V+\sigma_T^2},
164	\]
165	where $V=\operatorname{Var}(g)=V_B+V_W$.
166	The ratio
167	\[
168	  \frac{B(C)}{B_{\mathrm{OV}}} = \frac{V_W(V+\sigma_T^2)}{V(V_W+\sigma_T^2)} = 1 - \xi(C)
169	\]
170	is a decreasing function of $V_B\in[0,V]$.
171	At $V_B=0$ (no classification, $C$ uniform): $\xi=0$, $B=B_{\mathrm{OV}}$.
172	At $V_B=V$ (perfect classification, $C=I$): $\xi=1$, $B=0$.
173	Since $0\leq V_B\leq V$, we have $\xi\in[0,1]$ and $B(C)\in[0,B_{\mathrm{OV}}]$ (with the sign of $B_{\mathrm{OV}}$).
174	\end{proof}
175	
176	\begin{proposition}[Confounding sign preservation --- general case]
177	\label{prop:conf_gen}
178	For general $g$ and $f$ (not necessarily proportional), define the worst-case bias bound
179	\begin{equation}
180	  \bar{B} \;=\; \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(f(A))}}{\sigma_T^2}.
181	  \label{eq:bbar}
182	\end{equation}
183	If $|\tau| > \bar{B}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for \emph{all} column-stochastic $C$.
184	\end{proposition}
185	
186	\begin{proof}
187	We need $\operatorname{sign}(\tau\cdot D(C)+R(C))=\operatorname{sign}(\tau)$, which holds if $|R(C)|<|\tau|\cdot D(C)$.
188	Since $D(C)\geq\sigma_T^2$ (shown in Lemma~\ref{lem:bias_decomp}), it suffices to show $|R(C)|<|\tau|\,\sigma_T^2$.
189	
190	\emph{Step 1: Bound $|R(C)|$.}
191	$R(C)=\mathbb{E}[\operatorname{Cov}(g(A),f(A)\mid A^*)]$.
192	By the Cauchy--Schwarz inequality applied to each within-group covariance:
193	\[
194	  |\operatorname{Cov}(g,f\mid A^*{=}j)|
195	  \leq \sqrt{\operatorname{Var}(g\mid A^*{=}j)\,\operatorname{Var}(f\mid A^*{=}j)}.
196	\]
197	Taking expectations and applying Cauchy--Schwarz again:
198	\begin{align*}
199	  |R(C)|
200	  &\leq \mathbb{E}\bigl[\sqrt{\operatorname{Var}(g\mid A^*)\,\operatorname{Var}(f\mid A^*)}\bigr]\\
201	  &\leq \sqrt{\mathbb{E}[\operatorname{Var}(g\mid A^*)]\;\mathbb{E}[\operatorname{Var}(f\mid A^*)]}\\
202	  &\leq \sqrt{\operatorname{Var}(g(A))\;\operatorname{Var}(f(A))},
203	\end{align*}
204	where the last step uses $\mathbb{E}[\operatorname{Var}(X\mid Y)]\leq\operatorname{Var}(X)$ (law of total variance).
205	
206	\emph{Step 2: Conclude.}
207	The bias satisfies
208	\[
209	  |B(C)| = \frac{|R(C)|}{D(C)} \leq \frac{\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(f)}}{\sigma_T^2} = \bar{B}.
210	\]
211	When $|\tau|>\bar{B}$, the bias cannot cancel $\tau$, so $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ for all $C$.
212	\end{proof}
213	
214	\paragraph{Relationship to the omitted-variable condition.}
215	A weaker (necessary) condition for sign preservation is $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ where $\tau_{\mathrm{OV}}=\tau+\operatorname{Cov}(g,f)/\operatorname{Var}(T)$.
216	If this fails, then $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform noise) already flips the sign.
217	The rigorous sufficient condition $|\tau|>\bar{B}$ implies the weaker condition, since $|B_{\mathrm{OV}}|=|\operatorname{Cov}(g,f)|/\operatorname{Var}(T)\leq\bar{B}$ by Cauchy--Schwarz and $\operatorname{Var}(T)\geq\sigma_T^2$.
218	
219	\paragraph{Verification for paper parameters ($K{=}3$).}
220	With $\tau{=}2.0$, $\boldsymbol{\alpha}{=}(1.5,{-}1.0)$, $\boldsymbol{\beta}^{(A)}{=}(1.0,{-}0.5)$, $\sigma_T{=}1.0$, $\mathbf{p}{=}(0.40,0.35,0.25)$:
221	\begin{align*}
222	  \operatorname{Var}(g) &= \sum_k p_k\alpha_k^2 - \bigl(\textstyle\sum_k p_k\alpha_k\bigr)^2 = 0.962,\\
223	  \operatorname{Var}(f) &= \sum_k p_k(\beta_k^{(A)})^2 - \bigl(\textstyle\sum_k p_k\beta_k^{(A)}\bigr)^2 = 0.362,\\
224	  \bar{B} &= \sqrt{0.962\times 0.362}\;/\;1.0^2 = 0.590.
225	\end{align*}
226	Since $|\tau|{=}2.0 > \bar{B}{=}0.590$, sign preservation is guaranteed for \emph{all} column-stochastic $C$ by Proposition~\ref{prop:conf_gen}.
227	Additionally, $B_{\mathrm{OV}}=\operatorname{Cov}(g,f)/\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\tau_{\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.
228	
229	\paragraph{Extension to $K > 3$.}
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
486	\subsection{Proof of Theorem~\ref{thm:k3_symmetric} ($K{=}3$ Symmetric Monotonicity)}
487	\label{app:k3_symmetric_proof}
488	
489	\input{k3_symmetric_proof.tex}
490	
491	\begin{remark}[Empirical symmetry of LLM confusion matrices]
492	\label{rem:symmetry}
493	Among 25 empirical LLM confusion matrices, 6 (24\%) satisfy $\|C - C_{\mathrm{sym}}\|_F / \|C\|_F < 0.05$ (near-symmetric); relative Frobenius deviation ranges from 0.015 (CivilComments, $K{=}2$) to 0.381 (VAST, $K{=}3$). Binary tasks ($K{=}2$) are inherently symmetric (one off-diagonal parameter); for $K{\geq}3$, Theorem~\ref{thm:k3_symmetric} provides a lower bound on monotonicity guarantees, with the gap to general matrices filled by the $\varepsilon$-approximate Conjecture~\ref{conj:monotone}.
494	\end{remark}
495	
496	\subsection{Collider Topology ($A$ = Collider)}
497	\label{app:collider}
498	
499	\paragraph{Data-generating process.}
500	$T\to A\leftarrow Y$, $T\to Y$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82d4171c-d418-4271-817d-8d9db368a760",
  "isSidechain": true,
  "promptId": "6231d775-db71-46d9-bac6-397081d485cb",
  "agentId": "a20940d9e1e09d4c5",
  "type": "user",
  "uuid": "e778b52d-249c-4485-87b6-21a4f8bb66b7",
  "sourceToolAssistantUUID": "82d4171c-d418-4271-817d-8d9db368a760",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-23T19:17:38.585Z_

Now let me continue reading the appendix_proofs.tex file in chunks:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e778b52d-249c-4485-87b6-21a4f8bb66b7",
  "isSidechain": true,
  "agentId": "a20940d9e1e09d4c5",
  "requestId": "req_011CbL3C8dV92jf1tKVzPK6Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04131509-ef4c-4fcb-b970-8c61e2f2af7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Too9YX2vZ4GyKyPvQUv1zJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18120,
      "cache_read_input_tokens": 17979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18120,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 8 · 2026-05-23T19:17:39.376Z_

<details open><summary>🔧 Tool call — Read · `toolu_0127Z4REZLhnjwfuJvUNKsHa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": 500,
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04131509-ef4c-4fcb-b970-8c61e2f2af7a",
  "isSidechain": true,
  "agentId": "a20940d9e1e09d4c5",
  "requestId": "req_011CbL3C8dV92jf1tKVzPK6Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0ee041e8-ab59-4caf-a81a-700dbbd926e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Too9YX2vZ4GyKyPvQUv1zJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18120,
      "cache_read_input_tokens": 17979,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18120
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 144,
          "cache_read_input_tokens": 17979,
          "cache_creation_input_tokens": 18120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18120,
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

_source line 9 · 2026-05-23T19:17:39.693Z_

<details><summary>↩ Tool result · `toolu_0127Z4REZLhnjwfuJvUNKsHa`</summary>

```text
500	$T\to A\leftarrow Y$, $T\to Y$.
501	The treatment effect is unconfounded:
502	\begin{align*}
503	  T &\sim \mathcal{N}(0,1),\quad
504	  Y = \tau\,T + \varepsilon_Y,\quad \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp T,\\
505	  A\mid T,Y &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\delta}_T\,T + \boldsymbol{\delta}_Y\,Y)\bigr).
506	\end{align*}
507	The collider $A$ is a common \emph{effect} of $T$ and $Y$.
508	The no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\operatorname{plim}\hat\tau_{\mathrm{nc}}=\tau$.
509	The researcher erroneously controls for $A^*$, inducing Berkson's bias.
510	
511	\paragraph{Bias decomposition.}
512	Unlike confounding, $\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\tau T+\varepsilon_Y$), so Lemma~\ref{lem:bias_decomp} does not apply directly.
513	Instead, we derive the bias from the FWL identity~\eqref{eq:fwl}.
514	Writing $\tilde{Y}=\tau\tilde{T}+(\varepsilon_Y-\mathbb{E}[\varepsilon_Y\mid A^*])$ and noting that $\mathbb{E}[\tilde{T}\,\varepsilon_Y]=\mathbb{E}[\operatorname{Cov}(T,\varepsilon_Y\mid A^*)]$ (since $T\perp\varepsilon_Y$ unconditionally):
515	\begin{equation}
516	  \operatorname{plim}\hat\tau(C) = \tau + B(C),\quad
517	  B(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,\varepsilon_Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
518	  \label{eq:bias_col}
519	\end{equation}
520	Under non-differential misclassification ($A^*\perp(T,\varepsilon_Y)\mid A$), define $g(k)=\mathbb{E}[T\mid A{=}k]$ and $h(k)=\mathbb{E}[\varepsilon_Y\mid A{=}k]$.
521	By the tower property, $\mathbb{E}[T\mid A^*]=\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[\varepsilon_Y\mid A^*]=\mathbb{E}[h(A)\mid A^*]$.
522	Since $\operatorname{Cov}(T,\varepsilon_Y)=0$, the law of total covariance gives:
523	\[
524	  B(C) = \frac{-\operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[h(A)\mid A^*]\bigr)}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
525	\]
526	
527	\paragraph{Endpoint analysis.}
528	At $C=I$ ($A^*{=}A$):
529	$B(I) = -\operatorname{Cov}(g(A),h(A))\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)] = B_{\mathrm{Berkson}}$,
530	the full Berkson's bias from conditioning on the collider.
531	
532	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$):
533	$\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[h(A)\mid A^*]$ are constant, so $B=0$ and $\operatorname{plim}\hat\tau=\tau$.
534	
535	This is the structural reverse of confounding: misclassification attenuates the collider-induced bias toward zero, rather than growing bias from zero toward $B_{\mathrm{OV}}$.
536	
537	\begin{proposition}[Collider sign preservation --- proportional case]
538	\label{prop:col_prop}
539	If $h(A)=\lambda\,g(A)$ for some constant $\lambda$, then $|B(C)|\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.
540	Consequently, $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{Berkson}})$.
541	\end{proposition}
542	
543	\begin{proof}
544	When $h=\lambda g$, the numerator becomes $-\lambda\,\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$ and the denominator is $\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$.
545	Let $V^*=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\in[0,V_g]$ where $V_g=\operatorname{Var}(g(A))$.
546	Then
547	\[
548	  |B(C)| = |\lambda|\,\frac{V^*}{\operatorname{Var}(T)-V^*}.
549	\]
550	The function $x\mapsto x/(a-x)$ is increasing on $[0,a)$.
551	With $a=\operatorname{Var}(T)>V_g\geq V^*$:
552	$|B(C)|\leq|\lambda|\,V_g/(\operatorname{Var}(T)-V_g)=|B(I)|$.
553	At $V^*{=}0$ (uniform $C$): $B{=}0$.  At $V^*{=}V_g$ ($C{=}I$): $B{=}B(I)$.
554	\end{proof}
555	
556	\begin{proposition}[Collider sign preservation --- general case]
557	\label{prop:col_gen}
558	Define
559	\begin{equation}
560	  \bar{B}_{\mathrm{col}} = \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(h(A))}}{\mathbb{E}[\operatorname{Var}(T\mid A)]}.
561	  \label{eq:bbar_col}
562	\end{equation}
563	If $|\tau|>\bar{B}_{\mathrm{col}}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for all column-stochastic $C$.
564	\end{proposition}
565	
566	\begin{proof}
567	\emph{Step~1: Bound the numerator.}
568	By Cauchy--Schwarz:
569	$|\operatorname{Cov}(\mathbb{E}[g\mid A^*],\mathbb{E}[h\mid A^*])|\leq\sqrt{\operatorname{Var}(\mathbb{E}[g\mid A^*])\,\operatorname{Var}(\mathbb{E}[h\mid A^*])}$.
570	Since conditional expectation reduces variance: $\operatorname{Var}(\mathbb{E}[g\mid A^*])\leq\operatorname{Var}(g(A))$ and likewise for $h$.
571	
572	\emph{Step~2: Bound the denominator.}
573	$\mathbb{E}[\operatorname{Var}(T\mid A^*)]=\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[T\mid A^*])\geq\operatorname{Var}(T)-\operatorname{Var}(g(A))=\mathbb{E}[\operatorname{Var}(T\mid A)]$.
574	
575	\emph{Step~3: Conclude.}
576	$|B(C)|\leq\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(h)}\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)]=\bar{B}_{\mathrm{col}}$.
577	When $|\tau|>\bar{B}_{\mathrm{col}}$, the bias cannot overwhelm $\tau$. In practice, $\operatorname{Var}(g(A))$ and $\operatorname{Var}(h(A))$ can be estimated from observable data by bootstrapping regression coefficients from $A^*$-stratified subsamples, yielding conservative upper bounds on $\bar{B}_{\mathrm{col}}$.
578	\end{proof}
579	
580	\paragraph{Verification for paper parameters ($K{=}3$).}
581	With $\tau{=}1.0$, $\boldsymbol{\delta}_T{=}(0,\,0.5,\,{-}0.3)$, $\boldsymbol{\delta}_Y{=}(0,\,0.8,\,0.6)$, from $5{\times}10^6$-sample Monte Carlo:
582	\begin{align*}
583	  \operatorname{Var}(g(A)) &= 0.187,\quad
584	  \operatorname{Var}(h(A)) = 0.076,\quad
585	  \mathbb{E}[\operatorname{Var}(T\mid A)] = 0.813,\\
586	  \bar{B}_{\mathrm{col}} &= \sqrt{0.187\times 0.076}\;/\;0.813 = 0.147.
587	\end{align*}
588	Since $|\tau|{=}1.0\gg\bar{B}_{\mathrm{col}}{=}0.147$, Proposition~\ref{prop:col_gen} guarantees sign preservation.
589	Additionally, $B_{\mathrm{Berkson}}{=}{-}0.114$, giving $\tau+B_{\mathrm{Berkson}}{=}0.886{>}0$.
590	Verified across $100{,}000$ random column-stochastic $C$: $\tau_{\mathrm{sign\,flip}}{=}0\%$, and $|B(C)|\leq|B_{\mathrm{Berkson}}|$ in all cases.
591	
592	\subsection{Front-door Topology ($A$ = Mediator under Confounding)}
593	\label{app:frontdoor}
594	
595	\paragraph{Data-generating process.}
596	$T\to A\to Y$, $U\to T$, $U\to Y$.
597	An unobserved confounder $U$ affects both treatment and outcome:
598	\begin{align*}
599	  U &\sim \mathcal{N}(0,1),\quad
600	  T = \alpha_U\,U + \eta,\quad \eta\sim\mathcal{N}(0,1),\;\eta\perp U,\\
601	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
602	  Y &= f(A) + \lambda\,U + \varepsilon_Y,\quad \varepsilon_Y\perp(T,A,U).
603	\end{align*}
604	There is no direct $T{\to}Y$ edge; the causal effect of $T$ on $Y$ operates entirely through $A$.
605	The researcher controls for $A^*$ in $Y\sim 1+T+D_1^*+\cdots+D_{K-1}^*$.
606	
607	\paragraph{Bias decomposition.}
608	Since the direct effect is zero, the FWL coefficient on $T$ captures only bias:
609	\[
610	  \operatorname{plim}\hat\tau(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
611	\]
612	Substituting $Y=f(A)+\lambda U+\varepsilon_Y$ and using $\varepsilon_Y\perp(T,A,A^*)$:
613	\begin{equation}
614	  \operatorname{plim}\hat\tau(C)
615	  = \underbrace{\frac{\lambda\,\alpha_U}{\operatorname{Var}(T)}}_{\text{confounding (constant)}}
616	  \;+\; \underbrace{\frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}}_{\displaystyle B_{\mathrm{med}}(C)},
617	  \label{eq:fd_decomp}
618	\end{equation}
619	where $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]$.
620	
621	\begin{proof}[Derivation of~\eqref{eq:fd_decomp}]
622	Expand the numerator as
623	$\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] + \lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]$.
624	For the confounding term: since $T=\alpha_U U+\eta$ with $(U,\eta)$ jointly Gaussian, the regression residual $\xi=U-\frac{\alpha_U}{\operatorname{Var}(T)}T$ satisfies $\xi\perp T$.
625	Because $A$ is a function of $T$ (plus independent softmax noise) and $A^*$ is a function of $A$ (plus independent misclassification noise), $\xi\perp(T,A,A^*)$.
626	Therefore
627	\[
628	  \operatorname{Cov}(T,U\mid A^*{=}j)
629	  = \frac{\alpha_U}{\operatorname{Var}(T)}\,\operatorname{Var}(T\mid A^*{=}j)
630	  \quad\forall\;j,
631	\]
632	and $\lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]=\frac{\lambda\alpha_U}{\operatorname{Var}(T)}\,D(C)$, yielding the constant first term after division by $D(C)$.
633	\end{proof}
634	
635	This decomposition reveals that \emph{misclassification does not affect the confounding component}.
636	The confusion matrix $C$ modulates only the mediation-type leakage $B_{\mathrm{med}}(C)$, which has the same structure as in~§\ref{app:mediation}.
637	
638	\paragraph{Endpoint analysis.}
639	At $C=I$: $B_{\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\to A\to Y$ path), and $\operatorname{plim}\hat\tau(I)=\lambda\alpha_U/\operatorname{Var}(T)$ (pure confounding residual).
640	
641	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $B_{\mathrm{med}}=\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$, and $\operatorname{plim}\hat\tau_{\mathrm{nc}}=[\operatorname{Cov}(T,f(A))+\lambda\alpha_U]/\operatorname{Var}(T)$, the naive regression coefficient with no controls.
642	
643	\paragraph{Numerical Verification (Front-door sign preservation).}
644	\label{find:fd_sign}
645	Since $B_{\mathrm{med}}(C)$ has the same structure as the mediation bias (§\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:
646	\[
647	  \operatorname{sign}\!\bigl(\lambda\alpha_U\bigr)
648	  = \operatorname{sign}\!\bigl(\lambda\alpha_U + \operatorname{Cov}(T,f(A))\bigr).
649	\]
650	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$.
651	
652	\paragraph{Verification for paper parameters ($K{=}3$).}
653	With $\alpha_U{=}1.0$, $\lambda{=}1.0$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$, $\boldsymbol{\gamma}{=}(0,0.5,{-}0.3)$, $\boldsymbol{\delta}{=}(0,1.0,{-}0.8)$:
654	\begin{align*}
655	  \lambda\alpha_U/\operatorname{Var}(T) &= 1.0\times 1.0\,/\,2.0 = 0.500,\\
656	  \operatorname{Cov}(T,f(A))/\operatorname{Var}(T) &= 0.594\,/\,2.0 = 0.297.
657	\end{align*}
658	Both components are positive, so $\operatorname{plim}\hat\tau(C)\in[0.500,\,0.797]>0$ for all $C$.
659	
660	\subsection{Exposure Topology: Sign Reversal Counterexample}
661	\label{app:exposure}
662	
663	\begin{proposition}[Exposure sign reversal]
664	\label{prop:exp_counter}
665	For $K{=}3$ with $A$ as the treatment variable, there exist a marginal distribution $\mathbf{p}$, treatment effects $\boldsymbol{\beta}$, and a column-stochastic $C$ with $C_{kk}>0.5$ for all $k$, such that $\operatorname{sign}(\operatorname{plim}\hat\beta_1)\neq\operatorname{sign}(\beta_1)$.
666	\end{proposition}
667	
668	\begin{proof}[Construction]
669	Consider the exposure DGP $Y = \beta_1 D_1 + \beta_2 D_2 + \varepsilon_Y$ with:
670	\begin{itemize}
671	  \item Uniform prior: $\mathbf{p}=(1/3,\,1/3,\,1/3)$.
672	  \item True effects: $\beta_1=1$,\; $\beta_2=-10$.
673	\end{itemize}
674	Choose the confusion matrix
675	\[
676	  C = \begin{pmatrix}
677	    0.60 & 0.10 & 0.10\\
678	    0.10 & 0.60 & 0.39\\
679	    0.30 & 0.30 & 0.51
680	  \end{pmatrix},\qquad
681	  C_{kk}\in\{0.60,\,0.60,\,0.51\},\;\text{all}>0.5.
682	\]
683	Column sums are $1$ (verifiable by inspection).
684	
685	The OLS estimator regresses $Y$ on $(1,D_1^*,D_2^*)$.
686	The plim of $\hat\beta_j$ equals $\mathbb{E}[Y\mid A^*{=}j]-\mathbb{E}[Y\mid A^*{=}0]$, where
687	\[
688	  \mathbb{E}[Y\mid A^*{=}j] = \sum_{k=0}^{2} P(A{=}k\mid A^*{=}j)\,\beta_k
689	  = \sum_{k=1}^{2}\frac{C_{jk}\,p_k}{q_j}\,\beta_k.
690	\]
691	
692	\emph{Marginal distribution of $A^*$:}
693	\begin{align*}
694	  q_0 &= \tfrac{1}{3}(0.60+0.10+0.10)=0.267,\\
695	  q_1 &= \tfrac{1}{3}(0.10+0.60+0.39)=0.363,\\
696	  q_2 &= \tfrac{1}{3}(0.30+0.30+0.51)=0.370.
697	\end{align*}
698	
699	\emph{Conditional means:}
700	\begin{align*}
701	  \mathbb{E}[Y\mid A^*{=}0]
702	  &= \frac{0.10\times\tfrac{1}{3}\times 1 + 0.10\times\tfrac{1}{3}\times({-}10)}{0.267}
703	  = \frac{0.0333-0.3333}{0.267} = -1.125,\\[4pt]
704	  \mathbb{E}[Y\mid A^*{=}1]
705	  &= \frac{0.60\times\tfrac{1}{3}\times 1 + 0.39\times\tfrac{1}{3}\times({-}10)}{0.363}
706	  = \frac{0.200-1.300}{0.363} = -3.028,\\[4pt]
707	  \mathbb{E}[Y\mid A^*{=}2]
708	  &= \frac{0.30\times\tfrac{1}{3}\times 1 + 0.51\times\tfrac{1}{3}\times({-}10)}{0.370}
709	  = \frac{0.100-1.700}{0.370} = -4.324.
710	\end{align*}
711	
712	\emph{Estimated coefficient:}
713	\[
714	  \operatorname{plim}\hat\beta_1 = \mathbb{E}[Y\mid A^*{=}1]-\mathbb{E}[Y\mid A^*{=}0]
715	  = -3.028-(-1.125) = \mathbf{-1.903}.
716	\]
717	The true $\beta_1=+1>0$ but $\operatorname{plim}\hat\beta_1=-1.903<0$: \textbf{sign reversal}.
718	
719	\emph{Mechanism.}
720	The large off-diagonal entry $C_{12}=0.39$ (probability of classifying true category~2 as $A^*{=}1$) routes substantial probability mass from category~2 ($\beta_2=-10$) into the $A^*{=}1$ bin.
721	Despite $C_{11}=0.60>0.5$, the contamination from the strongly negative $\beta_2$ overwhelms the positive $\beta_1$, reversing the sign of the estimated effect for category~1.
722	This failure mode is structurally impossible at $K{=}2$: a $2{\times}2$ column-stochastic matrix with $C_{kk}>0.5$ has the form $C=\bigl(\begin{smallmatrix}a&1{-}b\\1{-}a&b\end{smallmatrix}\bigr)$ with $a,b>0.5$, and the single coefficient $\hat\beta_1$ is a positive-weighted average of $\beta_1$, preserving sign.
723	For $K{\geq}3$, the additional degrees of freedom in $C$ permit cross-contamination between categories with opposite-sign effects.
724	\end{proof}
725	
726	\subsection{Summary of Conditions}
727	\label{app:conditions}
728	
729	\begin{table}[h]
730	\centering
731	\small
732	\begin{tabular}{lccc}
733	\toprule
734	\textbf{Topology} & \textbf{Sufficient condition} & \textbf{Status} & \textbf{Paper DGP} \\
735	\midrule
736	Confounding & $\operatorname{sign}(\tau)=\operatorname{sign}(\tau{+}B_{\mathrm{OV}})$ & Proved & $\checkmark$ ($2.0$ vs $2.3$)\\
737	Collider & $|\tau|>\bar{B}_{\mathrm{col}}$ (Prop.~\ref{prop:col_gen}) & Proved & $\checkmark$ ($1.0$ vs $0.15$)\\
738	\midrule
739	Mediation & $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$ & Empirical & $\checkmark$ ($0.5$ vs $0.85$)\\
740	M-bias & Bias is attenuating (toward $\tau$) & Empirical & $\checkmark$ \\
741	Front-door & $\operatorname{sign}(\lambda\alpha_U)=\operatorname{sign}(\lambda\alpha_U{+}\operatorname{Cov}(T,f))$ & Empirical & $\checkmark$ ($0.50$ vs $0.80$)\\
742	\midrule
743	Exposure & Not guaranteed for $K\geq 3$ & Counterex. & See §\ref{app:exposure} \\
744	IV & Not guaranteed (denominator instability) & --- & --- \\
745	\bottomrule
746	\end{tabular}
747	\caption{Sufficient conditions for sign preservation under non-differential misclassification.
748	``Proved'' = algebraic proof via Cauchy--Schwarz (confounding) or Berkson attenuation (collider).
749	``Empirical'' = verified across 100{,}000 random column-stochastic matrices with zero violations; analytic proof for general $K$ remains open.
750	All conditions are on DGP parameters (not on $C$): once satisfied, sign preservation holds for all column-stochastic $C$ with $C_{kk}>0$.}
751	\label{tab:sign_conditions}
752	\end{table}
753	
754	\paragraph{Structural argument for M-bias topology.}
755	\emph{M-bias:} The M-structure creates a backdoor path through two latent common causes.
756	Misclassification of $A$ weakens the statistical association along this backdoor path, reducing the spurious correlation rather than amplifying it.
757	The bias therefore interpolates between the full M-bias (perfect classification, $\delta{=}0$) and zero (no classification information, $\delta{\to}\delta_{\max}$), monotonically non-increasing in $\delta$.
758	
759	\paragraph{M-bias sign-flip ASV $= \infty$.}
760	For the four covariate topologies (confounding, mediation, collider, M-bias), FWL invariance (Appendix~\ref{app:fwl}) implies that the coefficient on $T$ depends on $A^*$ only through the residualized relationship $\tilde{T} = T - \mathbb{E}[T \mid A^*]$. For M-bias, the spurious path through $A$ is the sole source of bias, and misclassification attenuates this path for all column-stochastic $C$. Since $\text{bias}(C(\delta))$ is monotonically non-increasing in $\delta$ and starts at a value with the same sign as $\tau$, no $\delta \in [0, \delta_{\max}]$ can produce a sign reversal. Therefore $\delta^*_{\text{sign}} = \infty$, which is a direct consequence of FWL invariance combined with the protective monotonicity of M-bias misclassification.
761	
762	\paragraph{Remark.}
763	The sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.
764	Once the condition is satisfied, sign preservation holds for \emph{all} column-stochastic $C$ with $C_{kk}>0$---no diagonal-dominance restriction is needed.
765	Conversely, if the condition fails (i.e., the omitted-variable or total-effect estimate has the opposite sign from $\tau$), then there exist confusion matrices that produce sign reversal.
766	For the DGP parameters used throughout our experiments, the conditions are comfortably satisfied.
767	The sign-alignment condition is violated when the confounder has opposing effects on treatment and outcome (e.g., $\gamma_A > 0$ on $T$ but $\gamma_A < 0$ on $Y$), producing $\operatorname{sign}(\tau) \neq \operatorname{sign}(\tau_{\mathrm{OV}})$. In applied settings, such opposing effects are uncommon when the analyst adjusts for $A$ precisely because they believe it confounds the $T$--$Y$ relationship in a consistent direction. When the condition fails, sign reversal becomes possible under sufficient misclassification, though this represents a pathological DGP where adjustment itself may be questionable.
768	
769	\subsection{Adversarial Monotonicity Verification}
770	\label{app:adversarial_monotonicity}
771	
772	We test Conjecture~\ref{conj:monotone} under four adversarial confusion matrix structures designed to challenge envelope monotonicity: near-permutation ($C_0 = (1{-}\epsilon)P + \epsilon \cdot \mathbf{1}\mathbf{1}^\top/K$, $P$ a random permutation), block-diagonal (within-block confusion only), sparse (two nonzero entries per column), and near-uniform ($C_{kk} \to 1/K$). For each structure, we sweep $\delta \in [0,1]$ along $C(\delta) = (1{-}\delta)I + \delta C_0$ and measure the maximum single-step monotonicity violation $\varepsilon_{\mathrm{abs}}$.
773	
774	\begin{table}[h]
775	\centering
776	\small
777	\caption{Adversarial monotonicity test across $K{=}3,5,7$, seven topologies, and three $\beta$ configurations ($N{=}1{,}000$ matrices per cell, 545{,}945 total curves).}
778	\label{tab:adversarial_monotonicity}
779	\begin{tabular}{lcc}
780	\toprule
781	\textbf{Structure} & \textbf{Non-monotone \%} & \textbf{Max $\varepsilon_{\mathrm{abs}}$} \\
782	\midrule
783	Near-permutation & 35.3\% & 0.016 \\
784	Block-diagonal & 0\% & 0 \\
785	Sparse & 2.3\% & 0.003 \\
786	Near-uniform & 0\% & 0 \\
787	\midrule
788	\textbf{All structures} & 11.9\% & \textbf{0.016} \\
789	\bottomrule
790	\end{tabular}
791	\end{table}
792	
793	The global maximum violation $\varepsilon_{\mathrm{abs}} = 0.016 < 0.02$ confirms that Conjecture~\ref{conj:monotone} holds under adversarial matrix structures. Near-permutation matrices with alternating-sign $\beta$ coefficients represent the most challenging case; even here, violations remain below the conjectured bound. Block-diagonal and near-uniform structures show exact monotonicity.
794	
795	\section{Supplementary Tables, Figures, and Algorithm}
796	\label{app:supplementary}
797	
798	\subsection{Binarization Collapse}
799	\label{app:binarization}
800	
801	Collapsing $K$-class annotations to binary before analysis discards multi-class error structure. We quantify ``binarization collapse'' as $\Delta = |\text{bias}_{K} - \text{bias}_{K \to 2}|$.
802	
803	For $K{=}3$, binarization introduces additional bias varying 154$\times$ across topologies: from $\bar{\Delta}{=}0.006$ (M-bias) to $\bar{\Delta}{=}0.926$ (IV). Exposure and IV also introduce sign flips during binarization (14\% and 17.5\%), a phenomenon absent in the other topologies (Figure~\ref{fig:binarization}).
804	
805	
806	\begin{table}[h]
807	\centering
808	\caption{ASV type applicability and sensitivity across DAG topologies. Magnitude ASV at $\tau{=}0.5$, 10\% threshold. Power at $\tau{=}0.05$ significance filter. ---: not applicable.}
809	\label{tab:asv_grid}
810	\small
811	\begin{tabular}{lcccl}
812	\toprule
813	\textbf{Topology} & \textbf{Mag. ASV} & \textbf{Signif.} & \textbf{Sign-flip} & \textbf{Rank} \\
814	\midrule
815	IV & 0.101--0.607 & 0\% & 1.1--6.7 & 1 (fragile) \\
816	Front-door & 0.064--0.387 & 100\% & --- & 2 \\
817	Confounding & 0.081--0.487 & 100\% & --- & 3 \\
818	Mediation & 0.076--0.454 & 0\% & --- & 4 \\
819	Collider & 0.338--2.028 & 0\% & --- & 5 \\
820	M-bias & $\infty$ & 96--100\% & --- & 6 (immune) \\
821	Exposure & --- & --- & 83.4\%$^*$ & --- \\
822	\bottomrule
823	\multicolumn{5}{l}{\scriptsize $^*$Fraction of $C_0$ with $\tau_{\text{sign\_flip}} < 1$. Exposure uses sign-flip ASV exclusively.}
824	\end{tabular}
825	\end{table}
826	
827	\begin{figure}[h]
828	\centering
829	\includegraphics[width=\columnwidth]{fig7_dirichlet_overlay.pdf}
830	\caption{Empirical LLM confusion matrices overlaid on theoretical violation-rate curves (exposure, left; IV, right). Theoretical curves are derived from $K{=}3$ Dirichlet random matrices; empirical points are positioned at their minimum diagonal entry. Markers denote datasets (circles: HumAID $K{=}10$; squares: VAST $K{=}3$; triangles: CivilComments $K{=}2$).}
831	\label{fig:dirichlet_overlay}
832	\end{figure}
833	
834	\begin{figure}[h]
835	\centering
836	\includegraphics[width=\columnwidth]{fig4_binarization.pdf}
837	\caption{Binarization collapse $\Delta$ across topologies. Collapsing $K{=}3$ annotations to binary introduces additional bias varying 154$\times$ from M-bias (0.006) to IV (0.926).}
838	\label{fig:binarization}
839	\end{figure}
840	
841	\begin{figure}[h]
842	\centering
843	\includegraphics[width=\columnwidth]{fig6_asv_heatmap.pdf}
844	\caption{ASV magnitude ranges across topologies for HumAID ($K{=}10$). Left: magnitude ASV ($\delta^*$) range across 8 LLM configurations; lower values indicate greater fragility. ``Safe'' topologies never exceed the 10\% bias threshold. Right: percentage of configurations flagged as ASV-unsafe.}
845	\label{fig:asv_heatmap}
846	\end{figure}
847	
848	\begin{table}[h]
849	\centering
850	\caption{RMSE reduction (\%) by correction method and DAG topology (mean across 6 error structures, $N_{\text{sim}}{=}1{,}000$). Positive = reduced RMSE; negative = increased RMSE. Naive/MLA show 0.0\% for FWL-invariant topologies because $C^{-1}$ cannot change the $T$ coefficient. \textbf{Bold}: best method per topology; \underline{underline}: best gold-free method.}
851	\label{tab:correction}
852	\small
853	\begin{tabular}{lccccc}
854	\toprule
855	\textbf{Topology} & \textbf{Naive} & \textbf{MLA} & \textbf{DSL} & \textbf{SIMEX} & \textbf{PPI++} \\
856	\midrule
857	Confounding & 0.0 & 0.0 & \underline{48.0} & 35.1 & \textbf{83.2} \\
858	Mediation & 0.0 & 0.0 & \underline{52.9} & 39.1 & \textbf{54.1} \\
859	Collider & 0.0 & 0.0 & $-$92.6 & \underline{31.8} & \textbf{50.5} \\
860	M-bias & 0.0 & 0.0 & $-$267 & \textbf{\underline{0.1}} & $-$88.0 \\
861	\midrule
862	Front-door & $-$52.7 & $-$111.5 & \underline{$-$29.0} & $-$62.4 & \textbf{74.1} \\
863	Exposure & $-$44.8 & $-$89.0 & $-$59.5 & \underline{$-$9.8} & \textbf{75.5} \\
864	IV & $-$40.4 & $-$58.7 & $-$206.1 & \underline{59.4} & \textbf{79.4} \\
865	\midrule
866	Grand mean & $-$19.7 & $-$37.0 & $-$79.0 & 13.3 & \textbf{47.0} \\
867	\bottomrule
868	\end{tabular}
869	\end{table}
870	
871	\paragraph{Error structures used in correction experiments.}
872	The six confusion matrix structures used for Table~\ref{tab:correction} are:
873	(1)~\emph{Diagonal-dominant}: $C_{kk}{=}0.7$, off-diagonal uniform;
874	(2)~\emph{Moderate noise}: $C_{kk}{=}0.5$, off-diagonal uniform;
875	(3)~\emph{Near-permutation}: $C_{kk}{=}0.4$, largest off-diagonal 0.5;
876	(4)~\emph{Asymmetric}: $C_{kk}$ varies (0.8, 0.5, 0.3);
877	(5)~\emph{Block confusion}: two classes confused ($C_{12}{=}C_{21}{=}0.4$), third clean;
878	(6)~\emph{Heavy noise}: $C_{kk}{=}0.4$, off-diagonal uniform.
879	All are column-stochastic with $K{=}3$. Results are averaged across all six structures.
880	
881	\begin{algorithm}[h]
882	\caption{Correction method selection for LLM-annotated causal inference. This topology-based classification is robust to $\varepsilon$-approximate deviations; practitioners computing quantitative ASV thresholds should note the $\varepsilon$-approximate bounds (Conjecture~\ref{conj:monotone}, Section~\ref{sec:asv}). Assumes linear structural equations; FWL-based routing may not apply under nonlinear models (see Appendix~\ref{sec:logistic_dgp}). Thresholds calibrated for $K{=}3$ linear SEM; recalibrate for different $K$ using topology-specific bias functions.}
883	\label{alg:correction}
884	\small
885	\begin{algorithmic}[1]
886	\REQUIRE DAG topology $\mathcal{T}$, gold-label availability $G \in \{\textsc{yes}, \textsc{no}\}$
887	\ENSURE Recommended method $M$, risk level $R$
888	\STATE
889	\STATE \textbf{Step 0: DAG uncertainty} \COMMENT{If $\mathcal{T}$ is uncertain, repeat Steps 1--3 under each candidate topology and report the range}
890	\STATE
891	\STATE \textbf{Step 1: Assess risk level}
892	\IF{$\mathcal{T} \in \{\text{M-bias}\}$}
893	    \STATE $R \gets \textsc{Low}$ \COMMENT{$|\text{bias}| < 0.04$ for all $C$}
894	\ELSIF{$\mathcal{T} \in \{\text{Conf., Med., Coll., Front-door}\}$}
895	    \STATE $R \gets \textsc{Medium}$ \COMMENT{bounded bias, no sign reversal}
896	\ELSE
897	    \STATE $R \gets \textsc{High}$ \COMMENT{Exposure, IV: sign reversal 83.4\% / 52.6\%}
898	\ENDIF
899	\STATE
900	\STATE \textbf{Step 2: Select correction method}
901	\IF{$G = \textsc{yes}$}
902	    \IF{$\mathcal{T} = \text{M-bias}$}
903	        \STATE $M \gets \textsc{None}$ \COMMENT{PPI++ RMSE red.\ $-$88.0\%; no correction preferred}
904	    \ELSE
905	        \STATE $M \gets \text{PPI++}$ \COMMENT{47.0\% RMSE red., 96.8\% coverage}
906	    \ENDIF
907	\ELSE
908	    \STATE \COMMENT{no gold labels}
909	    \IF{$\mathcal{T} \in \{\text{Confounding, Mediation}\}$}
910	        \STATE $M \gets \text{DSL}$ \COMMENT{48.0\% / 52.9\% RMSE reduction}
911	    \ELSIF{$\mathcal{T} = \text{IV}$}
912	        \STATE $M \gets \text{MC-SIMEX}$ \COMMENT{59.4\% RMSE reduction}
913	    \ELSIF{$\mathcal{T} \in \{\text{Collider, M-bias}\}$}
914	        \STATE $M \gets \text{MC-SIMEX}$ \COMMENT{31.8\% / 0.1\% RMSE reduction}
915	    \ELSE
916	        \STATE $M \gets \emptyset$; flag: acquire gold labels \COMMENT{no reliable gold-free method}
917	    \ENDIF
918	\ENDIF
919	\STATE
920	\STATE \textbf{Step 3: FWL invariance warning}
921	\IF{$\mathcal{T} \in \{\text{Conf., Med., Coll., M-bias}\}$}
922	    \STATE Skip Naive plug-in and MLA \COMMENT{0\% bias red.\ on $T$ coeff.\ (Table~\ref{tab:correction}: below 2\%, no method improves)}
923	\ENDIF
924	\RETURN $(M, R)$
925	\end{algorithmic}
926	\end{algorithm}
927	
928	\subsection{Proof of FWL Invariance}
929	\label{app:fwl_proof}
930	
931	For the four topologies where $A$ enters as a covariate (confounding, mediation, collider, M-bias), the regression is $Y = \tau T + \boldsymbol{\gamma}^\top \mathbf{D}^* + \varepsilon$, where $\mathbf{D}^*$ is the $N \times (K{-}1)$ dummy matrix for $A^*$. Any matrix-based correction replaces $\mathbf{D}^*$ with $\tilde{\mathbf{D}} = \mathbf{D}^* M$ for some invertible $(K{-}1) \times (K{-}1)$ matrix $M$ (e.g., $M = C^{-1}$ for plug-in, or $M = (C^\top C)^{-1} C^\top$ for MLE). By the Frisch--Waugh--Lovell theorem~\cite{lovell1963}, $\hat{\tau}$ depends only on the residual of $T$ projected off $\operatorname{col}(\mathbf{D}^*)$. Since $\operatorname{col}(\mathbf{D}^* M) = \operatorname{col}(\mathbf{D}^*)$ for invertible $M$, the projection is unchanged and $\hat{\tau}(\tilde{\mathbf{D}}) = \hat{\tau}(\mathbf{D}^*)$ exactly. SIMEX adds noise $\mathbf{D}^*_{\text{sim}} = \mathbf{D}^* + \lambda \mathbf{E}$; when $\mathbf{E}$ is generated from the same column space, the extrapolation to $\lambda = -1$ converges to a column-space-equivalent transformation, yielding 0\% bias reduction empirically.
932	
933	\paragraph{FWL breakdown under logistic regression.}
934	\label{sec:fwl_logistic}
935	The column-space argument applies only to estimators whose treatment coefficient is a function of $T$ residualized off $\operatorname{col}(\mathbf{D}^*)$---a property of linear projection. The logistic MLE solves $\sum_i (Y_i - \sigma(\mathbf{x}_i^\top\boldsymbol{\beta}))\mathbf{x}_i = \mathbf{0}$; the implicit weighting by $\sigma'(\cdot)$ depends on the actual values of the design columns, not only on their span, so replacing $\mathbf{D}^*$ by $\mathbf{D}^* M$ generally changes the fitted $\hat\tau$. We verify this on the confounding topology ($K{=}3$, $\tau{=}0.5$, $N{=}10{,}000\times 500$ MC reps) under both linear ($Y = \tau T + \mathbf{D}\boldsymbol{\beta}+\varepsilon$) and logistic ($Y\sim\mathrm{Bern}(\sigma(\tau T + \mathbf{D}\boldsymbol{\beta}))$) DGPs, comparing the uncorrected estimator (fit on $\mathbf{D}^*$) against Naive plug-in (fit on per-sample $(C^{-1}\mathbf{e}_{A^*})_{1:K}$). Per-rep estimates are paired (same $A^*$, same outcome).
936	
937	\begin{table}[h]
938	\centering
939	\small
940	\caption{FWL invariance under OLS vs. breakdown under logistic regression. $|\Delta|_{\max}=\max_m|\hat\tau_{\mathrm{corr}}^{(m)}-\hat\tau_{\mathrm{un}}^{(m)}|$ over 500 MC reps; bias reduction = $1-|\hat\tau_{\mathrm{corr}}-\tau_*|/|\hat\tau_{\mathrm{un}}-\tau_*|$. Confounding DAG, $K{=}3$, $N{=}10{,}000$.}
941	\label{tab:fwl_logistic}
942	\begin{tabular}{lcccc}
943	\toprule
944	 & \multicolumn{2}{c}{\textbf{OLS}} & \multicolumn{2}{c}{\textbf{Logistic}} \\
945	\cmidrule(lr){2-3}\cmidrule(lr){4-5}
946	CM (VAST K=3) & $|\Delta|_{\max}$ & bias red. & $|\Delta|_{\max}$ & bias red. \\
947	\midrule
948	deepseek\_zero-shot     & $2.3\!\times\!10^{-15}$ & $+0.00\%$ & $8.1\!\times\!10^{-4}$ & $-0.09\%$ \\
949	llama4\_few-shot-3      & $5.2\!\times\!10^{-15}$ & $+0.00\%$ & $6.8\!\times\!10^{-4}$ & $-0.07\%$ \\
950	llama4\_few-shot-5      & $4.3\!\times\!10^{-15}$ & $+0.00\%$ & $6.8\!\times\!10^{-4}$ & $-0.06\%$ \\
951	llama4\_zero-shot       & $1.6\!\times\!10^{-15}$ & $+0.00\%$ & $5.9\!\times\!10^{-4}$ & $-0.05\%$ \\
952	qwen2.5-7b\_few-shot-3  & $7.2\!\times\!10^{-15}$ & $-0.00\%$ & $6.8\!\times\!10^{-4}$ & $-0.01\%$ \\
953	qwen2.5-7b\_few-shot-5  & $8.2\!\times\!10^{-15}$ & $+0.00\%$ & $5.6\!\times\!10^{-4}$ & $+0.05\%$ \\
954	\midrule
955	\textbf{Mean}           & ---                     & $\mathbf{0.0\%}$ & ---            & $\mathbf{-0.04\%}$ \\
956	\bottomrule
957	\end{tabular}
958	\end{table}
959	
960	Two findings: (i) Under OLS, $\hat\tau_{\mathrm{corr}}^{(m)}=\hat\tau_{\mathrm{un}}^{(m)}$ to machine precision in every replication, confirming Proposition~\ref{app:fwl_proof} as an exact algebraic identity. (ii) Under logistic regression, per-replication estimates differ by $|\Delta|_{\max}\!\sim\!10^{-3}$---thirteen orders of magnitude larger than the OLS gap---so the invariance fails formally. However, the directional effect on bias is negligible: mean bias reduction is $-0.04\%$ across the six confusion matrices (range $[-0.09\%, +0.05\%]$, not even consistent in sign). Matrix-based corrections remain practically useless under logistic regression---not by an exact invariance, but because the deviation is too small to systematically offset the misclassification-induced bias (which itself is $\sim\!0.10$ in absolute units, two orders of magnitude larger than $|\Delta|$). The routing rule of Algorithm~\ref{alg:correction} (skip Naive/MLA for these four topologies) is therefore conservative-but-correct under logistic regression as well. Script: \texttt{artifacts/exp\_fwl\_logistic\_breakdown.py}; results: \texttt{exp\_fwl\_logistic\_results.json}.
961	
962	\subsection{Applied Illustration: ClinicalBERT Case Study}
963	\label{app:case_study}
964	
965	To demonstrate the framework's end-to-end utility, we apply it retrospectively to \citet{lee_wood_doughty2024}, who use ClinicalBERT to classify patient smoking status ($K{=}4$: never, past, current, unknown) from clinical notes and control for this predicted confounder when estimating the causal effect of echocardiography on mortality in 4{,}735 MIMIC-III sepsis patients.
966	Our taxonomy identifies this as a \emph{confounding topology}: the annotated variable enters as a confounder between treatment and outcome.
967	Three conclusions follow directly.
968	First, the zero sign-flip guarantee for confounding (Table~\ref{tab:taxonomy}) ensures that the estimated protective effect (OR~$= 0.89$) cannot reverse direction due to annotation error---a reassurance unavailable without topology-specific analysis.
969	Second, the FWL invariance result implies that any correction reducing to $C^{-1}$ applied to the dummy-coded confounder achieves exactly 0\% bias reduction for the treatment coefficient; naive plug-in is provably futile here.
970	Third, our correction guidance ranks PPI++ (83.2\% RMSE reduction for confounding) above MC-SIMEX (35.1\%) when gold labels are available---a concrete recommendation the original study lacked.
971	This example illustrates the intended workflow: DAG identification $\to$ topology-specific guarantees $\to$ correction method selection.
972	
973	\subsection{IV Wald Estimator: Diagonal-Dominance Subspaces}
974	\label{sec:iv_dirichlet_subspace}
975	
976	Section~\ref{sec:taxonomy_results} reports a 52.6\% Wald sign-flip rate
977	over the full Dirichlet$(1,1,1)$ prior. Because realistic LLM confusion
978	matrices are diagonal-dominant, we replicate the exposure-DAG stratification
979	for the IV topology, restricting the sample
980	space to $\{C : \min_k C_{kk} \geq d\}$ for $d \in \{0, 0.5, 0.7, 0.9\}$
981	(100{,}000 random matrices per threshold).
982	
983	\begin{table}[h]
984	\centering
985	\caption{IV Wald estimator bias by minimum-diagonal subspace ($K{=}3$, $\tau_{\text{true}}{=}1.41$).
986	Rates over 100{,}000 Dirichlet-truncated random $C$ per threshold.}
987	\label{tab:iv_dirichlet_subspace}
988	\small
989	\begin{tabular}{lcccc}
990	\toprule
991	\textbf{Subspace} & \textbf{Violation} & \textbf{Sign Flip} & \textbf{Amplif.} & \textbf{Worst} \\
992	\midrule
993	Full           & 100.0\% & 51.7\% & 48.3\% & $10^{5}\!\times$ \\
994	$d \geq 0.5$   & 100.0\% & 0.0\%  & 100.0\% & $28.6\times$ \\
995	$d \geq 0.7$   & 100.0\% & 0.0\%  & 100.0\% & $2.4\times$ \\
996	$d \geq 0.9$   & 100.0\% & 0.0\%  & 100.0\% & $1.2\times$ \\
997	\bottomrule
998	\end{tabular}
999	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ee041e8-ab59-4caf-a81a-700dbbd926e7",
  "isSidechain": true,
  "promptId": "6231d775-db71-46d9-bac6-397081d485cb",
  "agentId": "a20940d9e1e09d4c5",
  "type": "user",
  "uuid": "03f1fa5d-eb9d-42dd-ad6a-79abe4892bf9",
  "sourceToolAssistantUUID": "0ee041e8-ab59-4caf-a81a-700dbbd926e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-23T19:17:41.506Z_

Now let me read the rest of the appendix file (lines 1001 onwards):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03f1fa5d-eb9d-42dd-ad6a-79abe4892bf9",
  "isSidechain": true,
  "agentId": "a20940d9e1e09d4c5",
  "requestId": "req_011CbL3CMRBPAMyWqF7sn32d",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2c0a84d8-3fdf-4319-91bc-6cb3f41a4c35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PR15q7oDfC5c1TzEJjULRT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 15090,
      "cache_read_input_tokens": 36099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15090,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 11 · 2026-05-23T19:17:42.608Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FgL6FueNiTN8yUZHpD71pB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": 500,
  "offset": 1000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c0a84d8-3fdf-4319-91bc-6cb3f41a4c35",
  "isSidechain": true,
  "agentId": "a20940d9e1e09d4c5",
  "requestId": "req_011CbL3CMRBPAMyWqF7sn32d",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9ee99d54-1504-486a-8ef8-d26a70c42800",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PR15q7oDfC5c1TzEJjULRT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 15090,
      "cache_read_input_tokens": 36099,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15090
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 147,
          "cache_read_input_tokens": 36099,
          "cache_creation_input_tokens": 15090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15090,
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

_source line 12 · 2026-05-23T19:17:42.959Z_

<details><summary>↩ Tool result · `toolu_01FgL6FueNiTN8yUZHpD71pB`</summary>

```text
1000	
1001	The contrast with exposure is instructive: at $d{\geq}0.7$, exposure violation drops to 13.7\% (sign reversal 2.1\%, amplification 11.7\%), while IV maintains 100\% violation with pure amplification. IV sign reversal is entirely driven by pathological (near-random) confusion matrices where the Wald denominator crosses zero; diagonal dominance reduces this crossing to near-zero under empirical accuracy conditions but cannot prevent amplification. Even at $d{\geq}0.9$, the Wald estimator inflates $|\tau|$ by up to $1.24\times$ with probability~1.
1002	
1003	\subsection{Non-Differential Misclassification Verification}
1004	\label{sec:nondiff_verify}
1005	
1006	The non-differential assumption $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k)$ holds \emph{by design} in standard LLM annotation pipelines: the model receives only source text as input and classifies without observing the outcome $Y$ or covariates $\mathbf{Z}$. The annotation API call is structurally independent of downstream variables, satisfying the conditional independence requirement.
1007	
1008	To provide empirical support beyond the design argument, we examine topic-stratified confusion matrices using the VAST dataset ($K{=}3$, stance detection), where the \texttt{topic} field (e.g., ``gun control,'' ``college'') serves as a proxy for latent factors correlated with $Y$. Across 10 model configurations (3 LLMs $\times$ 2--4 prompt types) and 19 qualifying topics (minimum 10 samples per topic), we compute per-topic confusion matrices $C_{\text{topic}}(t) = P(A^*{=}j \mid A{=}k, \text{topic}{=}t)$ and compare against the overall $C = P(A^*{=}j \mid A{=}k)$.
1009	
1010	Per-topic sample sizes range from 10 to 42, making individual topic CMs inherently noisy. A bootstrap permutation test ($B{=}10{,}000$) under the non-differential null shows that the expected grand maximum deviation $\max_{t,j,k} |C_{\text{topic}}(j,k) - C(j,k)|$ at the 95th percentile ranges from 0.90 to 0.98 across model configurations---driven by the smallest topics. For the 5 largest topics ($n \geq 28$), expected per-topic max deviation at the 95th percentile is 0.38--0.49, consistent with finite-sample variation rather than systematic topic-dependence. The observed per-topic variation is fully consistent with the non-differential null.
1011	
1012	This proxy-based test is necessarily limited: topic is not the actual outcome $Y$, and small per-topic samples reduce statistical power. The design argument (LLM input excludes $Y$) remains the primary justification; the stress test in Section~\ref{sec:nondiff_stress} below quantifies bias degradation under hypothetical violations.
1013	
1014	\subsection{Non-Differential Assumption Stress Test}
1015	\label{sec:nondiff_stress}
1016	
1017	Our main analysis assumes non-differential misclassification: the confusion matrix $C$ does not depend on the outcome $Y$. To assess sensitivity to violations of this assumption, we conduct a stress test on the exposure topology ($K{=}3$, $\min_k C_{kk} \geq 0.7$, 10{,}000 random matrices per $\varepsilon$). For each base matrix $C_0$, observations with $Y > \text{median}(Y)$ are misclassified using a perturbed matrix $\tilde{C} = \text{renormalize}(C_0 + \varepsilon \cdot \Delta)$ where $\Delta_{jk} \sim \text{Uniform}(-1,1)$ for $j \neq k$, while observations with $Y \leq \text{median}(Y)$ retain $C_0$.
1018	
1019	\begin{table}[h]
1020	\centering
1021	\small
1022	\caption{Effect of differential misclassification on bias violation rates (exposure DAG, $K{=}3$, $\min_k C_{kk} \geq 0.7$, $N{=}50{,}000$ MC samples per trial).}
1023	\label{tab:nondiff_stress}
1024	\begin{tabular}{cccc}
1025	\toprule
1026	$\varepsilon$ & Sign-Flip (\%) & Amplification (\%) & Any Violation (\%) \\
1027	\midrule
1028	0.00 & 2.0 & 11.5 & 13.3 \\
1029	0.01 & 2.4 & 12.4 & 14.7 \\
1030	0.05 & 2.8 & 13.0 & 15.7 \\
1031	0.10 & 4.5 & 16.7 & 20.9 \\
1032	0.20 & 9.7 & 23.7 & 32.6 \\
1033	0.30 & 15.5 & 28.7 & 42.8 \\
1034	0.50 & 22.9 & 34.9 & 54.6 \\
1035	\bottomrule
1036	\end{tabular}
1037	\end{table}
1038	
1039	The $\varepsilon{=}0$ baseline (13.3\% violation) closely matches the analytical result (13.7\%) from Section~\ref{sec:taxonomy_results}. Small departures ($\varepsilon \leq 0.05$) change rates by fewer than 3 percentage points. At $\varepsilon{=}0.10$, the violation rate increases by 7.6~pp; at $\varepsilon{=}0.50$, it rises to 54.6\% (+41.2~pp), indicating substantial sensitivity to large differential error. Our main conclusions hold under mild violations but should be interpreted cautiously when outcome-conditional annotation is suspected.
1040	
1041	\paragraph{Extended stress test.}
1042	An extended stress test across 96 configurations (4 topologies $\times$ 2 $K$ $\times$ 3 CM qualities $\times$ 4 $\varepsilon$, 100 MC replications each; Table~\ref{tab:stress-test}) confirms these patterns broadly: at $\varepsilon{=}0$, sign-flip rates are zero for all configurations; at $\varepsilon{=}0.10$, the maximum sign-flip rate is 7\% (IV, low-quality $C_{kk}{=}0.4$, $K{=}3$). At $K{=}10$, sign-flip rates remain zero for all topologies and $\varepsilon$ values, suggesting that higher $K$ provides additional robustness to differential misclassification.
1043	
1044	\input{exp_a_stress_test_table.tex}
1045	
1046	\paragraph{Structured violation models.}
1047	Beyond uniform perturbations, we compare two structured violation models across all seven topologies ($K{=}3$, 1{,}000 matrices per $\varepsilon$, $\min_k C_{kk}{\geq}0.7$): (1)~\emph{outcome-conditional}, where $\tilde{C}$ applies to $Y{>}\text{median}(Y)$ while $C_0$ applies below; (2)~\emph{label-specific}, where off-diagonal perturbation magnitude scales with $|\text{corr}(A{=}k, Y)|$, modeling accuracy degradation on $Y$-predictive categories. For exposure at $\varepsilon{=}0.20$, label-specific violations are substantially milder than uniform (sign-flip 0.1\% vs.\ 10.1\%), while outcome-conditional violations are more severe (sign-flip 13.9\%, mean relative bias 0.50 vs.\ 0.40). All five sign-preserving topologies maintain 0\% sign-flip under both structured models at all $\varepsilon$ tested; IV likewise shows 0\% sign-flip (its vulnerability requires pathological diagonal structure, not differential error). These results indicate that the uniform perturbation model is neither uniformly conservative nor uniformly liberal: practitioners should assess which violation pattern is most plausible for their annotation pipeline.
1048	
1049	\subsection{Robustness to Nonlinear DGP}
1050	\label{sec:logistic_dgp}
1051	
1052	We replace the linear structural equations with $Y \sim \text{Bernoulli}(\sigma(\mathbf{x}^\top\boldsymbol{\beta}))$ and estimate via logistic regression (control function for IV) for all seven topologies, using $K{=}3$, six real VAST confusion matrices, 500 MC replications, and $N{=}10{,}000$. Mean sign-flip rates across the six CMs:
1053	
1054	\begin{center}
1055	\small
1056	\begin{tabular}{lcccc}
1057	\toprule
1058	Topology & Linear SF$_\tau$ & Logistic SF$_\tau$ & Linear SF$_\text{any}$ & Logistic SF$_\text{any}$ \\
1059	\midrule
1060	Confounding & 0.000 & 0.000 & 0.573 & 0.559 \\
1061	Mediation & 0.000 & 0.000 & 0.703 & 0.695 \\
1062	Collider & 0.000 & 0.000 & 0.060 & 0.060 \\
1063	Exposure & --- & --- & 0.577 & 0.574 \\
1064	M-bias & 0.000 & 0.000 & 0.095 & 0.099 \\
1065	Front-door & 0.000 & 0.000 & 0.590 & 0.579 \\
1066	IV & 0.086 & 0.074 & 0.086 & 0.560 \\
1067	\bottomrule
1068	\end{tabular}
1069	\end{center}
1070	
1071	Treatment-effect sign-flip rates (SF$_\tau$) are zero for all five guaranteed topologies under both linear and logistic DGPs, and differ by $< 0.02$ for IV. The SF$_\text{any}$ discrepancy for IV reflects estimator dimensionality: the control function includes a residual coefficient prone to sign noise; the core comparison is SF$_\tau$, where both estimators agree. Linear and logistic DGPs produce virtually identical sign-flip patterns across all seven topologies ($|\Delta\,\text{SF}_\tau| < 0.02$). Under logistic DGP, bias is measured in log-odds units; directional conclusions (sign preservation, topology ranking) transfer directly, while magnitudes are not directly comparable to linear plim expressions. For practitioners requiring finite-sample inference under logistic DGP, bias-corrected bootstrap provides a nonparametric alternative that bypasses the linear plim framework.
1072	
1073	\subsection{Bootstrap Uncertainty of ASV}
1074	\label{sec:bootstrap_asv}
1075	
1076	We assess confusion-matrix estimation uncertainty by bootstrapping label pairs from HumAID DeepSeek zero-shot ($K{=}10$, $n{=}1{,}500$): resample with replacement $B{=}1{,}000$ times, re-estimate $C_0$, and recompute magnitude ASV $\delta^*$ at a 10\% bias threshold.
1077	
1078	\begin{center}
1079	\small
1080	\begin{tabular}{lccc}
1081	\toprule
1082	Topology & $\delta^*$ (point) & 95\% CI & Valid / 1000 \\
1083	\midrule
1084	Confounding & --- & --- & 0 \\
1085	Exposure & 0.937 & [0.602, 1.363] & 907 \\
1086	IV & 0.754 & [0.435, 1.290] & 902 \\
1087	\bottomrule
1088	\end{tabular}
1089	\end{center}
1090	
1091	Confounding never reaches the 10\% threshold across all 1{,}000 bootstraps, confirming robustness. For IV, the 95\% CI spans a $3{\times}$ range (0.435 to 1.290); practitioners should bootstrap $C_0$ rather than rely on a point estimate when ASV is near the decision boundary. CI width scales as $O(1/\sqrt{n})$ where $n$ is the gold-label validation set size; at $n{=}1{,}500$, IV CIs are ${\sim}3{\times}$ wider than exposure CIs, reflecting the Wald estimator's denominator instability. A convergence study ($K{=}3$, $B{=}1{,}000$) confirms this scaling: exposure CI width narrows from 0.60 ($n{=}500$) to 0.05 ($n{=}50{,}000$), and IV from 0.52 to 0.04, with the product $\text{width} \times \sqrt{n}$ approximately constant (CV $< 0.20$).
1092	
1093	\begin{figure}[h]
1094	\centering
1095	\includegraphics[width=0.9\columnwidth]{exp_c_bootstrap_figure.pdf}
1096	\caption{Bootstrap distribution of magnitude ASV $\delta^*$ ($B{=}1{,}000$) for HumAID DeepSeek zero-shot ($K{=}10$). Dashed line: point estimate; shaded: 95\% CI.}
1097	\label{fig:bootstrap_asv}
1098	\end{figure}
1099	
1100	\subsection{Cross-$K$ Robustness}
1101	\label{sec:cross_k_robustness}
1102	
1103	All structural patterns persist at $K{=}5,7$ (100{,}000 matrices each): sign-flip guarantees hold for the same five topologies, and IV sign-flip rates remain within 51--53\%.
1104	
1105	\subsection{ASV Diagnostic Results}
1106	\label{sec:asv_diagnostics}
1107	
1108	For HumAID ($K{=}10$, 56 scenarios), 55.4\% are flagged as magnitude-ASV-unsafe---IV, mediation, front-door, and exposure all trigger, while confounding, collider, and M-bias remain below 10\% bias (Figure~\ref{fig:asv_heatmap}). For CivilComments ($K{=}2$), 100\% of scenarios are ASV-unsafe despite $F_1$ ranging from $0.69$ (7B) to $0.82$ (frontier).
1109	
1110	Overlaying all 23 empirical matrices onto the theoretical Dirichlet violation-rate curves (Figure~\ref{fig:dirichlet_overlay}) confirms placement: VAST in the danger zone, HumAID mid-range, CivilComments approaching safe for exposure but still in IV amplification.
1111	
1112	\subsection{ASV Stability Across DGP Parameters}
1113	\label{sec:asv_stability}
1114	
1115	We test whether ASV rankings are stable across different data-generating process (DGP) configurations by varying the treatment-effect vector $\boldsymbol{\beta}$ across three settings: alternating-large ($\boldsymbol{\beta}=[0,\,1.0,\,-0.5]$), same-sign ($\boldsymbol{\beta}=[0,\,0.5,\,0.3]$), and alternating-small ($\boldsymbol{\beta}=[0,\,0.2,\,-0.1]$), with $K{=}3$, $\tau{=}0.5$, and five $C_0$ diagonal values $\in\{0.5,0.6,0.7,0.8,0.9\}$.
1116	
1117	\input{exp_e_asv_stability_table.tex}
1118	
1119	Three patterns emerge (Table~\ref{tab:asv_stability}). First, IV magnitude ASV is identical across all three DGPs ($\delta^*{=}0.203$). This is a mathematical identity, not an empirical finding: the Wald estimator $\hat{\tau}_{\text{IV}} = \text{RF}/\text{FS}$ has $\boldsymbol{\beta}$ in both numerator and denominator, and the ratio depends only on $C$ and the first-stage structure, making ASV invariant to $\boldsymbol{\beta}$ by construction. Second, exposure ASV depends on the coefficient ratio structure: alternating-large ($\beta_2/\beta_1 = -0.5$) and alternating-small ($\beta_2/\beta_1 = -0.5$) share the same ratio and yield identical $\delta^*{=}0.090$, while same-sign ($\beta_2/\beta_1 = 0.6$) gives $\delta^*{=}0.223$---thus the experiment provides two distinct sign-structure conditions, not three. Third, confounding ASV depends on effect magnitudes: only alternating-large triggers the 10\% threshold ($\delta^*{=}0.348$); smaller effects never reach 10\% bias.
1120	
1121	Confounding is consistently the most robust topology (highest ASV or no violation), and M-bias remains immune (not shown). However, the relative fragility of exposure vs.\ IV inverts with coefficient sign structure: under alternating signs, exposure is most fragile ($0.090 < 0.203$); under same-sign effects, IV is most fragile ($0.203 < 0.223$). Practitioners should compute ASV with their specific DGP rather than relying on generic rankings.
1122	
1123	\subsection{Extended Conjecture Verification}
1124	\label{sec:conjecture_verify}
1125	
1126	We test envelope monotonicity (Conjecture~\ref{conj:monotone}) by sampling 10{,}000 random $C_0$ matrices from Dirichlet$(1,\dots,1)$ per topology for $K \in \{3,5,7\}$ (210{,}000 total), sweeping $\delta$ in steps of 0.01, and counting matrices with at least one non-monotonic step exceeding tolerance $10^{-12}$. Bias at each $\delta$ is computed via analytic probability limits using Gauss--Hermite quadrature (100 points), eliminating sampling noise entirely.
1127	
1128	\begin{table}[h]
1129	\centering
1130	\small
1131	\caption{Envelope monotonicity violations per 10{,}000 random $C_0$ matrices ($\delta$ step $= 0.01$). ``Worst mag.''\ is the largest single-step deviation $|B(\delta_{i+1})|-|B(\delta_i)|$ in the non-monotonic direction. $^*$100{,}000 matrices at step $= 0.005$ yield exposure $\varepsilon = 0.075$.}
1132	\label{tab:conjecture_verify}
1133	\begin{tabular}{lccccc}
1134	\toprule
1135	\textbf{Topology} & $K{=}3$ & $K{=}5$ & $K{=}7$ & \textbf{Worst mag.} & \textbf{Direction} \\
1136	\midrule
1137	Confounding & 8467 & 8063 & 7892 & 0.011 & non-dec \\
1138	Mediation   & 8236 & 7905 & 7893 & 0.013 & non-dec \\
1139	Collider    & 8683 & 7669 & 7570 & 0.005 & non-inc \\
1140	Exposure    & 485  & 205  & 77   & 0.056$^*$ & non-dec \\
1141	M-bias      & 9791 & 7783 & 7399 & 0.002 & non-inc \\
1142	IV          & 7433 & 6015 & 5711 & $>10^6$ & non-dec \\
1143	Front-door  & 8429 & 8079 & 7899 & 0.013 & non-dec \\
1144	\bottomrule
1145	\end{tabular}
1146	\end{table}
1147	
1148	Violation counts are high (60--97\% of matrices), but magnitudes are small for non-IV topologies under the default parameterization (Table~\ref{tab:conjecture_verify}); DGP sensitivity analysis (Table~\ref{tab:dgp_sensitivity}) shows $\varepsilon$ scales with effect magnitude $|\beta|$, remaining below 0.02 for $|\beta| \leq 1$ across non-exposure topologies. These results are computed from analytic probability limits with zero sampling noise, confirming the violations are structural properties of multi-class confusion matrices rather than numerical artifacts. IV deviations reflect Wald estimator singularities when the first-stage coefficient passes near zero---this is a property of the Wald estimator, not of the ASV parameterization. Adversarial search (500 restarts per configuration, $K \in \{3,5\}$) finds genuine counterexamples for all topologies except IV $K{=}3$, confirming that strict monotonicity does not hold universally. The bias envelope is $\varepsilon$-approximately monotonic with $\varepsilon < 0.03$ for collider and M-bias across all tested $\tau$; confounding, mediation, and front-door achieve $\varepsilon < 0.06$ at default DGP parameters (see DGP sensitivity below); exposure satisfies $\varepsilon_{p99} < 0.008$ but extreme-tail matrices ($<$0.02\% of draws) reach $\varepsilon \approx 0.15$. Empirically, $\varepsilon$ scales as $O(1/K^\alpha)$ with $\alpha \in [0.6, 1.5]$ (topology-dependent): for confounding, mediation, and front-door, $\alpha \approx 1.4$; for exposure, $\alpha \approx 1.0$; for collider and M-bias, $\alpha \approx 0.7$. A universal empirical upper bound is $\varepsilon \leq 0.137/\sqrt{K}$, verified across all tested configurations ($K \in \{3,5,7\}$). This scaling supports the practical validity of ASV as a sensitivity tool at any meaningful bias threshold.
1149	
1150	\paragraph{DGP parameter sensitivity.}
1151	We repeat the verification across $\tau \in \{0.1, 0.5, 1.0, 2.0, 5.0\}$, varying the direct $T{\to}Y$ coefficient for confounding ($\beta_T{=}\tau$), mediation, collider, and M-bias (DGP $\tau$), and rescaling the $A{\to}Y$ coefficient vector to $\boldsymbol{\beta}\cdot\tau$ for exposure and front-door. With 10{,}000 random $C_0$ per $(K,\tau)$ setting (Table~\ref{tab:conjecture_tau_sens}), $\varepsilon$ remains small ($< 0.03$) for $\tau \geq 0.5$ for confounding, mediation, collider, and M-bias, but grows at $\tau{=}0.1$: mediation produces 1{,}950 / 30{,}000 violations across $K \in \{3,5,7\}$ (worst $\varepsilon{=}0.130$ at $K{=}3$) and confounding 200 / 30{,}000 (worst $\varepsilon{=}0.118$ at $K{=}3$). The mechanism is dimensional: additive terms not scaling with $\tau$ (e.g.\ the $\boldsymbol{\beta}$-contribution to $\mathbb{E}[Y D_k]$ in mediation and confounding) contribute a $\tau$-independent offset to the bias numerator, so the ratio $|B|/|\tau|$ inflates as $\tau \to 0$. A single mediation violation at $\tau{=}2.0$ ($\varepsilon{=}0.112$, 1/30{,}000 matrices) arises from a specific confusion matrix structure where off-diagonal entries induce partial cancellation along the mediation pathway; this isolated case does not affect the $p_{99}$ bound ($\varepsilon_{p99}{=}0.005$). Collider and M-bias remain robust at all $\tau$ ($\varepsilon{<}0.022$ and $\varepsilon{<}0.015$ respectively). Exposure shows scattered tail outliers but $\overline{\varepsilon} \approx 3\!\times\!10^{-4}$ at every $\tau$, consistent with linear scaling: when $\boldsymbol{\beta}$ rescales by $\tau$, both bias and $\tau_{\text{true}}$ scale by the same factor and $\varepsilon$ is theoretically invariant. Front-door inverts the pattern ($\varepsilon$ \emph{grows} with $\tau$, reaching $0.139$ at $\tau{=}5$, $K{=}3$, with 664 violations) because $\tau_{\text{true}} = \operatorname{plim}(\hat{\tau}_T \mid C{=}I)$ is pinned at $0.5$ by the $U$-confounding path while bias magnitudes scale with $\boldsymbol{\beta}$---this is an artefact of how $\tau_{\text{true}}$ is normalised, not a genuine failure of envelope monotonicity. In practice, ASV's $\delta^*$ thresholds (typically $\geq 0.1$ in our deployment) are well above the region where these $\varepsilon$-violations occur, so the small-$\tau$ degradation does not affect ASV's operational reliability; we flag it as a caveat for applications targeting $|\tau| \lesssim 0.1$ in standardised units.
1152	
1153	\begin{table}[h]
1154	\centering
1155	\small
1156	\caption{$\varepsilon \equiv \max_\delta(|B(\delta{+}\Delta)|{-}|B(\delta)|)/|\tau_{\text{true}}|$ in the non-monotonic direction (max over $K \in \{3,5,7\}$; 10{,}000 random $C_0$ per cell). Bold marks $\varepsilon > 0.02$ (non-exposure) or $\varepsilon > 0.08$ (exposure). Counts in parentheses are violations / 30{,}000. Tables~\ref{tab:conjecture_verify} and~\ref{tab:conjecture_tau_sens} use independent random seeds; for topologies with low violation rates (exposure $<$0.02\%), the worst-case $\varepsilon$ is sample-sensitive.}
1157	\label{tab:conjecture_tau_sens}
1158	\begin{tabular}{lccccc}
1159	\toprule
1160	\textbf{Topology} & $\tau{=}0.1$ & $\tau{=}0.5$ & $\tau{=}1.0$ & $\tau{=}2.0$ & $\tau{=}5.0$ \\
1161	\midrule
1162	Confounding & \textbf{0.118} (200) & 0.027 (0) & 0.014 (0) & 0.007 (0) & 0.002 (0) \\
1163	Mediation   & \textbf{0.130} (1950) & 0.026 (0) & 0.013 (0) & \textbf{0.112} (1) & 0.003 (0) \\
1164	Collider    & 0.022 (0) & 0.006 (0) & 0.005 (0) & 0.004 (0) & 0.002 (0) \\
1165	Exposure    & \textbf{0.111} (5) & \textbf{0.122} (2) & \textbf{0.152} (2) & \textbf{0.089} (3) & \textbf{0.148} (3) \\
1166	M-bias      & 0.014 (0) & 0.003 (0) & 0.001 (0) & 0.001 (0) & 0.000 (0) \\
1167	Front-door  & 0.003 (0) & 0.013 (0) & 0.027 (0) & 0.051 (0) & \textbf{0.139} (664) \\
1168	\bottomrule
1169	\end{tabular}
1170	\end{table}
1171	
1172	\paragraph{Effect-magnitude sensitivity.}
1173	We further vary the direct effect $\beta \in \{0.1, 0.5, 1.0, 2.0, 5.0\}$ and noise variance $\sigma^2 \in \{0.5, 1.0, 2.0\}$ across all seven topologies ($K{=}3$, 10{,}000 Dirichlet$(1,\ldots,1)$ matrices per cell). Table~\ref{tab:dgp_sensitivity} reports the worst-case relative envelope deviation $\varepsilon_{\text{rel}}$. For non-exposure topologies, $\varepsilon$ scales approximately linearly with $|\beta|$; the safe/fragile partition is stable across all 105 cells.
1174	
1175	\input{conjecture_dgp_sensitivity_table.tex}
1176	
1177	\subsection{Proportional Effects Breakdown}
1178	\label{sec:proportional_effects}
1179	
1180	Theorem~\ref{thm:monotone} requires proportional effects ($f = \lambda g$); here we quantify how $\lambda(C)$ out-of-bounds (OOB) rates depend on the degree of departure from proportionality. We simulate $K{=}3$ mediation with 100{,}000 random confusion matrices (diagonal $\geq 0.5$, Dirichlet off-diagonal) at five proportionality degrees: exact ($f_j {-} f_0 = \lambda(g_j {-} g_0)$), near-proportional ($f = \lambda g + \epsilon$, $\epsilon \sim \mathcal{N}(0,\sigma^2)$, $\sigma \in \{0.1, 0.3, 0.5\}$), and fully independent ($f \perp g$). Table~\ref{tab:proportional_effects} reports the $\lambda(C) \notin [0,1]$ rate.
1181	
1182	\begin{table}[h]
1183	\centering
1184	\small
1185	\caption{$\lambda(C)$ out-of-bounds rate and mediation sign failure rate by degree of departure from proportional effects ($K{=}3$, 100K random confusion matrices per row).}
1186	\label{tab:proportional_effects}
1187	\begin{tabular}{lcc}
1188	\toprule
1189	\textbf{Proportionality degree} & $\lambda(C) \notin [0,1]$ & Sign failure \\
1190	\midrule
1191	Exact ($\sigma{=}0$) & 0.0\% & 0.85\% \\
1192	Near ($\sigma{=}0.1$) & 10.3\% & 0.87\% \\
1193	Near ($\sigma{=}0.3$) & 19.0\% & 0.96\% \\
1194	Near ($\sigma{=}0.5$) & 22.4\% & 0.93\% \\
1195	Independent ($f \perp g$) & 22.9\% & 0.17\% \\
1196	\midrule
1197	NLP-realistic (plan\_006 DGP) & 0.07\% & 0.0\% \\
1198	\bottomrule
1199	\end{tabular}
1200	\end{table}
1201	
1202	The $\lambda$ OOB rate rises steeply from 0\% to ${\sim}10$\% at $\sigma{=}0.1$ and saturates near 23\% for independent $(f,g)$. Sign failure rates remain below 1\% across all conditions because $\lambda$ excursions outside $[0,1]$ are typically small and do not reverse the dominant effect direction. The NLP-realistic DGP ($\delta{=}[0, 0.8, {-}0.6]$, $\beta{=}[0, 1.0, {-}0.5]$) exhibits near-zero OOB (0.07\%) and zero sign failures, confirming that proportional effects hold approximately in practice.
1203	
1204	\subsection{FWL Invariance Under Nonlinear Models}
1205	\label{sec:fwl_nonlinear}
1206	
1207	FWL invariance guarantees exactly 0\% bias reduction from matrix-based corrections (MLA, naive plug-in) under linear OLS for covariate topologies (confounding, mediation, collider, M-bias). Here we test whether this invariance persists under logistic regression across sample sizes $N \in \{1000, 5000, 10{,}000, 50{,}000\}$ and three error levels ($C_{kk} \in \{0.9, 0.7, 0.5\}$), with 200 Monte Carlo replicates per cell. Table~\ref{tab:fwl_nonlinear} reports the mean logistic bias reduction (positive = correction helps).
1208	
1209	\begin{table}[h]
1210	\centering
1211	\small
1212	\caption{Mean logistic bias reduction (\%) from matrix-based correction, by topology and error level (averaged over $N \in \{1K, 5K, 10K, 50K\}$; 200 MC reps each). Under linear OLS, all covariate topologies yield exactly 0\%. Exposure is shown for comparison.}
1213	\label{tab:fwl_nonlinear}
1214	\begin{tabular}{lccc}
1215	\toprule
1216	\textbf{Topology} & \textbf{Low} ($C_{kk}{=}0.9$) & \textbf{Med} ($C_{kk}{=}0.7$) & \textbf{High} ($C_{kk}{=}0.5$) \\
1217	\midrule
1218	Confounding & $-$0.003\% & $<$0.001\% & $<$0.001\% \\
1219	Mediation & $-$0.004\% & $<$0.001\% & $<$0.001\% \\
1220	Collider & $-$0.033\% & $-$0.020\% & $<$0.001\% \\
1221	M-bias & $-$0.049\% & $-$0.010\% & $<$0.001\% \\
1222	Front-door & 0.001\% & $-$0.001\% & $<$0.001\% \\
1223	\midrule
1224	Exposure & $-$68.5\% & $-$48.7\% & $-$22.5\% \\
1225	\bottomrule
1226	\end{tabular}
1227	\end{table}
1228	
1229	For all five covariate topologies, logistic bias reduction is negligible ($|$mean$| < 0.05\%$) across all $N$ and error levels, with no systematic $N$-scaling: medians cluster within $\pm 0.002\%$ at $N{=}50{,}000$. The large standard deviations observed at certain $(N, \text{error})$ cells for collider and M-bias (up to 2.6\% std at $N{=}10{,}000$) reflect rare outlier replicates; medians remain near zero. This confirms that FWL invariance is a robust structural property that extends beyond linear models for covariate topologies.
1230	
1231	In contrast, exposure shows substantial FWL breakdown under logistic regression: $-$22\% to $-$78\% bias reduction (negative = correction worsens bias), stabilising at $N \geq 5{,}000$. The breakdown magnitude increases with accuracy ($C_{kk}$), consistent with the exposure topology's sensitivity to the nonlinear link function transforming category weights.
1232	
1233	\subsection{PPI++ Gold Label Ratio Sensitivity}
1234	\label{sec:ppi_gold_ratio}
1235	
1236	We test PPI++ correction performance as a function of gold label fraction ($K{=}3$, $N{=}10{,}000$, 100 MC replications, 5 Dirichlet confusion matrices with $\min_k C_{kk}{\geq}0.6$).
1237	
1238	\begin{table}[h]
1239	\centering
1240	\small
1241	\caption{PPI++ RMSE reduction (\%) vs.\ gold label fraction across five topologies. Negative values indicate PPI++ increases RMSE relative to the naive estimator.}
1242	\label{tab:ppi_gold_ratio}
1243	\begin{tabular}{lccccc}
1244	\toprule
1245	Topology & 5\% & 10\% & 20\% & 50\% & 100\% \\
1246	\midrule
1247	Confounding & $+$84.8 & $+$88.6 & $+$91.8 & $+$94.2 & $+$95.2 \\
1248	Exposure & $+$75.2 & $+$83.1 & $+$87.1 & $+$91.2 & $+$93.8 \\
1249	Mediation & $+$56.7 & $+$70.4 & $+$77.2 & $+$85.3 & $+$88.7 \\
1250	IV & $+$1.4 & $+$22.1 & $+$50.1 & $+$66.7 & $+$76.4 \\
1251	M-bias & $-$125.3 & $-$43.6 & $-$19.6 & $+$6.0 & $+$18.5 \\
1252	\bottomrule
1253	\end{tabular}
1254	\end{table}
1255	
1256	For confounding and exposure, PPI++ achieves $>$75\% RMSE reduction even at 5\% gold labels; IV requires ${\geq}20\%$ gold to reach 50\% reduction, reflecting the Wald estimator's higher variance. M-bias exhibits harmful correction at ${\leq}20\%$ gold ($-125\%$ at 5\%), because PPI++ re-exposes the M-bias pathway that annotation error had attenuated; only at ${\geq}50\%$ gold does the estimator become weakly beneficial ($+6\%$).
1257	
1258	\subsection{Realistic Differential Misclassification Thresholds}
1259	\label{sec:realistic_epsilon}
1260	
1261	Our non-differential assumption (Definition~\ref{def:nondiff}) requires $P(A^*{\mid}A,Y) = P(A^*{\mid}A)$. We estimate how much $Y$-stratified differential error each of our 23 empirical LLM confusion matrices can tolerate before exposure sign reversal exceeds 5\%. For each matrix $C$, we construct $C_{\text{high}} = \text{renorm}(C + \varepsilon\Delta)$ and $C_{\text{low}} = \text{renorm}(C - \varepsilon\Delta)$ with random off-diagonal perturbation $\Delta$ (500 MC trials per $\varepsilon$), sweep $\varepsilon \in [0, 0.50]$, and report the safe threshold $\varepsilon^*_{\text{safe}} = \max\{\varepsilon : \text{reversal rate} < 5\%\}$ (Table~\ref{tab:realistic_epsilon}).
1262	
1263	\begin{table}[h]
1264	\centering
1265	\small
1266	\caption{Safe differential misclassification thresholds $\varepsilon^*_{\text{safe}}$ by dataset/K. For $K{=}2$ (binary), no configuration produces sign reversal up to $\varepsilon{=}0.50$. For $K{\geq}3$, the majority of configurations are fragile ($\varepsilon^*_{\text{safe}}{=}0$), confirming that the non-differential assumption is load-bearing for multi-class exposure.}
1267	\label{tab:realistic_epsilon}
1268	\begin{tabular}{lccccc}
1269	\toprule
1270	\textbf{Dataset} & $K$ & $n$ & \textbf{Mean} $\varepsilon^*$ & \textbf{Median} $\varepsilon^*$ & $\varepsilon^*{=}0$ \\
1271	\midrule
1272	Civil Comments & 2 & 7 & 0.50 & 0.50 & 0/7 \\
1273	VAST & 3 & 8 & 0.003 & 0.00 & 7/8 \\
1274	HuMAID & 10 & 8 & 0.045 & 0.00 & 7/8 \\
1275	\bottomrule
1276	\end{tabular}
1277	\end{table}
1278	
1279	The distribution is sharply bimodal: all $K{=}2$ configurations are immune to differential misclassification within the tested range ($\varepsilon^*_{\text{safe}}{=}0.50$), consistent with the binary sign-preservation guarantee (Proposition~\ref{prop:signflip}(c)). For $K{\geq}3$, 14 of 16 configurations have $\varepsilon^*_{\text{safe}}{=}0$---sign reversal occurs at the smallest tested $\varepsilon{=}0.01$. Two outliers (VAST: $\varepsilon^*{=}0.02$; HuMAID: $\varepsilon^*{=}0.36$) have atypically structured confusion matrices. This confirms that even small violations of non-differential misclassification are consequential for multi-class exposure, underscoring the practical importance of validating $P(A^*{\mid}A,Y) \approx P(A^*{\mid}A)$ on gold-labeled subsets when $K \geq 3$.
1280	
1281	\subsection{Proportional Effects with Empirical Confusion Matrices}
1282	\label{sec:proportional_real_matrices}
1283	
1284	Theorem~\ref{thm:monotone} assumes proportional effects ($f = \lambda g$). We evaluate this assumption using all 23 empirical LLM confusion matrices under four DGP groups in the mediation topology (23 matrices $\times$ 50 seeds $\times$ 100{,}000 precomputed samples per seed).
1285	
1286	\begin{table}[h]
1287	\centering
1288	\small
1289	\caption{Proportional effects validation with 23 real LLM confusion matrices under mediation DGP. $\lambda(C) \in [0,1]$: proportion satisfying the Theorem~\ref{thm:monotone} bound. Sign pres.: sign preservation rate of the direct effect estimate.}
1290	\label{tab:proportional_empirical}
1291	\begin{tabular}{lcccc}
1292	\toprule
1293	\textbf{DGP Group} & $\lambda(C)$ \textbf{mean} & $\lambda(C) \in [0,1]$ & \textbf{Sign pres.} & \textbf{CV} \\
1294	\midrule
1295	Proportional ($f{=}\lambda g$) & 0.271 & 99.8\% & 100\% & 0.00 \\
1296	Near-prop.\ ($\sigma{=}0.1$) & 0.285 & 99.2\% & 100\% & 1.06 \\
1297	Non-proportional & 0.240 & 85.0\% & 97.3\% & 3.60 \\
1298	Sparse & 0.296 & 75.8\% & 98.6\% & 6.59 \\
1299	\bottomrule
1300	\end{tabular}
1301	\end{table}
1302	
1303	Under proportional and near-proportional effects, $\lambda(C)$ remains within $[0,1]$ for ${\geq}99\%$ of configurations with 100\% sign preservation---the Theorem~\ref{thm:monotone} conditions are satisfied by real LLM confusion matrices. Even under non-proportional effects ($f$ independent of $g$), sign preservation remains at 97.3\%, with $\lambda(C)$ exceeding $[0,1]$ in 15\% of cases. The per-$K$ breakdown shows that $\lambda(C)$ is dimension-dependent: $K{=}2$ (mean 0.249), $K{=}3$ (mean 0.082), $K{=}10$ (mean 0.490), with 100\% in $[0,1]$ across all $K$ under proportional effects. Sparse DGP (zero-effect categories) produces the highest violation rate (24.2\%), consistent with the breakdown mechanism: zero-effect categories make $f/g$ ratios undefined, maximally departing from proportionality.
1304	
1305	\subsection{Case Study: ASV Diagnosis of Political Ad Tone Classification}
1306	\label{sec:asv_case_study}
1307	
1308	We illustrate the ASV diagnostic workflow on a concrete CSS application. \citet{egami_hinck_stewart_wei2023} use LLM classifiers to annotate political advertising tone ($K{=}3$: promote/contrast/attack) from the Fowler \& Ridout database, then estimate the causal effect of ad tone on voter outcomes. The annotated variable is the \textbf{exposure} (treatment). Using a representative $K{=}3$ confusion matrix from our empirical set (VAST DeepSeek zero-shot, mean diagonal 0.734) as a proxy:
1309	
1310	\begin{center}
1311	\small
1312	\begin{tabular}{lccc}
1313	\toprule
1314	Coefficient & $\delta^*_{\text{mag}}$ (10\%) & $\delta^*_{\text{sf}}$ & Relative bias at $\delta{=}1$ \\
1315	\midrule
1316	$\beta_1$ (primary) & 0.234 & $> 1.5$ & 39.7\% \\
1317	$\beta_2$ (secondary) & 0.154 & $> 1.5$ & 60.4\% \\
1318	\bottomrule
1319	\end{tabular}
1320	\end{center}
1321	
1322	Both coefficients are magnitude-unsafe ($\delta^* < 1$), with the secondary coefficient more fragile ($\delta^*{=}0.154$). If the same annotator were instead classifying a \textbf{confounder} (e.g., media framing as a control variable), magnitude ASV rises to $\delta^*{=}0.690$---a $3{\times}$ increase in error tolerance from the same confusion matrix. This demonstrates the central insight: topology, not annotator quality, determines vulnerability. Algorithm~\ref{alg:correction} routes this exposure topology to PPI++ or DSL correction; matrix-based methods (naive plug-in, MLA) are ineffective due to FWL non-applicability.
1323	
1324	\subsection{End-to-End Demonstration}
1325	\label{sec:e2e_demo}
1326	
1327	\input{e2e_demo_table.tex}
1328	
1329	We use a symmetric $C_0$ (diagonal $= 0.7$) for expository clarity; empirical matrices deviate by median $d_{\mathrm{rel}}{=}0.160$ (Remark~\ref{rem:symmetry}), and core findings are robust to asymmetric structures (Section~\ref{sec:empirical}).
1330	
1331	\subsection{Correction Method Sensitivity to $K$}
1332	\label{sec:correction_k_sensitivity}
1333	
1334	We test whether the correction method ranking from Table~\ref{tab:correction} ($K{=}3$) is stable at $K{=}5$ and $K{=}10$. For each $K$, we sample 5 random Dirichlet confusion matrices (diagonal $\geq 0.6$), run 100 MC replications per topology--matrix combination ($N{=}5{,}000$, 10\% gold fraction), and compute RMSE reduction for all five methods across all seven topologies.
1335	
1336	\paragraph{Grand ranking stability.}
1337	Spearman rank correlations across all topology--method pairs: $\rho_{3,5} = 0.80$, $\rho_{3,10} = 0.84$, $\rho_{5,10} = 0.93$ (all $p < 10^{-8}$). Per-topology correlations are even stronger: 5 of 7 topologies (confounding, collider, M-bias, IV, and exposure at $K{=}10$) achieve $\rho = 1.0$ between $K{=}3$ and $K{=}10$.
1338	
1339	\paragraph{Method-specific patterns.}
1340	PPI++ effectiveness degrades with $K$: confounding RMSE reduction drops from 85.6\% ($K{=}3$) to 75.6\% ($K{=}10$); mediation drops from 57.1\% to 9.0\%. At $K{=}10$, PPI++ becomes harmful for IV ($-124\%$) and exposure ($-11\%$). MC-SIMEX is the most $K$-robust method, maintaining the top rank for 5/7 topologies at $K{=}10$ (vs.\ 3/7 at $K{=}3$). FWL invariance (naive plug-in and MLA achieving 0\% bias reduction on the treatment coefficient) holds at all $K$ tested, confirming the structural nature of this result.
1341	
1342	\begin{table}[h]
1343	\centering
1344	\small
1345	\caption{Top correction method and RMSE reduction (\%) by topology across $K$. Bold = top method for that topology--$K$ combination.}
1346	\label{tab:correction_k}
1347	\begin{tabular}{lccc}
1348	\toprule
1349	\textbf{Topology} & $K{=}3$ & $K{=}5$ & $K{=}10$ \\
1350	\midrule
1351	Confounding & \textbf{PPI++} 85.6 & \textbf{PPI++} 76.4 & \textbf{PPI++} 75.6 \\
1352	Mediation & \textbf{PPI++} 57.1 & \textbf{SIMEX} 59.7 & \textbf{SIMEX} 59.0 \\
1353	Collider & \textbf{SIMEX} 55.4 & \textbf{SIMEX} 63.4 & \textbf{SIMEX} 57.3 \\
1354	Exposure & \textbf{SIMEX} 72.5 & \textbf{SIMEX} 65.0 & \textbf{SIMEX} 47.3 \\
1355	M-bias & \textbf{SIMEX} 3.2 & \textbf{SIMEX} 47.0 & \textbf{SIMEX} 43.7 \\
1356	IV & \textbf{SIMEX} 30.9 & \textbf{SIMEX} 30.4 & \textbf{SIMEX} 27.1 \\
1357	Front-door & \textbf{PPI++} 82.9 & \textbf{PPI++} 69.0 & \textbf{SIMEX} 70.1 \\
1358	\bottomrule
1359	\end{tabular}
1360	\end{table}
1361	
1362	\subsection{Comparison with Related Sensitivity Frameworks}
1363	\label{sec:sensitivity_comparison}
1364	
1365	\begin{table}[h]
1366	\centering
1367	\caption{Comparison of sensitivity frameworks.}
1368	\label{tab:sensitivity_comparison}
1369	\small
1370	\begin{tabular}{lccc}
1371	\toprule
1372	& \textbf{ASV} & \textbf{E-value} & \textbf{Partial} $R^2$ \\
1373	\midrule
1374	Parameter space & $K{\times}K$ confusion $C(\delta)$ & Scalar confounder & $R^2$ of omitted var \\
1375	Sensitivity path & $(1{-}\delta)I + \delta C_0$ & Monotone scalar & Monotone scalar \\
1376	Topology-specific & \checkmark & \ding{55} & \ding{55} \\
1377	Sign-flip diagnostic & \checkmark ($\delta^*_{\text{sign}}$) & \ding{55} & \ding{55} \\
1378	Topology dependence & \checkmark (7 topologies ranked) & \ding{55} & \ding{55} \\
1379	Monotonicity & Proved $K{=}2$; conj.\ $K{\geq}3$ & Guaranteed & Guaranteed \\
1380	Target & Annotation error & Unmeasured confounding & Omitted variable \\
1381	\bottomrule
1382	\end{tabular}
1383	\end{table}
1384	
1385	\subsection{Per-Topology $F_1$--Bias Correlation}
1386	\label{sec:within_topo_f1}
1387	
1388	The cross-topology correlation between macro $F_1$ and $|\text{bias}|$ is weak ($\rho = -0.10$, $p = 0.45$; \S\ref{sec:empirical}), but decomposing by topology reveals a structured pattern. Table~\ref{tab:within_topo_f1} reports Spearman correlations computed over 23 LLM configurations (HumAID $K{=}10$, VAST $K{=}3$, CivilComments $K{=}2$; 161 total scenarios).
1389	
1390	\begin{table}[h]
1391	\centering
1392	\small
1393	\caption{Within-topology Spearman $\rho(F_1, |\text{bias}|)$ across 23 empirical LLM configurations $\times$ 3 datasets. Negative $\rho$: higher $F_1$ $\to$ lower bias (expected). Positive $\rho$: higher $F_1$ $\to$ higher bias (protective attenuation removed).}
1394	\label{tab:within_topo_f1}
1395	\begin{tabular}{lccc}
1396	\toprule
1397	\textbf{Topology} & $n$ & $\rho$ & $p$ \\
1398	\midrule
1399	Confounding & 23 & $-0.557$ & 0.006 \\
1400	Mediation & 23 & $-0.565$ & 0.005 \\
1401	Exposure & 23 & $-0.531$ & 0.009 \\
1402	Front-door & 23 & $-0.568$ & 0.005 \\
1403	IV & 23 & $-0.700$ & $<$0.001 \\
1404	Collider & 23 & $+0.310$ & 0.150 \\
1405	M-bias & 23 & $+0.867$ & $<$0.001 \\
1406	\bottomrule
1407	\end{tabular}
1408	\end{table}
1409	
1410	Five topologies show the expected negative correlation: better annotation quality ($F_1{\uparrow}$) reduces causal bias. IV shows the strongest effect ($\rho = -0.70$), consistent with the Wald estimator's sensitivity to misclassification in the first stage. M-bias uniquely reverses: $\rho = +0.87$ ($p < 0.001$). The mechanism is that misclassification attenuates the spurious M-bias path, so the naive estimator under noisy annotations is \emph{closer} to the true causal effect; improving annotation quality (higher $F_1$) removes this protective attenuation and \emph{increases} bias. This is consistent with the correction results (\S\ref{sec:correction}), where PPI++ harms M-bias ($-$88\%) by removing the same protective noise. Collider shows a positive but non-significant trend ($\rho = +0.31$, $p = 0.15$), consistent with Berkson bias attenuation. Per-dataset breakdowns (CivilComments $K{=}2$: $\rho = -1.0$ for all topologies with $n{=}7$) should be interpreted with caution given the small sample and limited $F_1$ variation within the binary task.
1411	
1412	\subsection{Confusion Matrix Estimation Robustness}
1413	\label{sec:c_robustness}
1414	
1415	The ASV framework requires the confusion matrix $C$, which in practice must be estimated from a held-out gold-labeled subset. We assess how estimation noise in $\hat{C}$ propagates to the safe/fragile partition and ASV ranking. For each of 8 empirical confusion matrices (VAST, 4 LLMs $\times$ 2 prompting strategies), we draw $n_{\text{gold}} \in \{50, 100, 200, 500\}$ samples from a $\text{Multinomial}(n_{\text{gold}}, C_{\cdot k})$ distribution per column, compute $\hat{C}$, and evaluate the resulting ASV ranking across 200 bootstrap replicates.
1416	
1417	\begin{table}[h]
1418	\centering
1419	\small
1420	\caption{$\hat{C}$ estimation robustness: safe/fragile partition stability and ASV ranking correlation (Spearman $\rho$ vs.\ true-$C$ ranking) under multinomial bootstrap from finite gold sets. 8 empirical matrices $\times$ 200 bootstrap replicates per $n_{\text{gold}}$.}
1421	\label{tab:c_robustness}
1422	\begin{tabular}{lccc}
1423	\toprule
1424	$n_{\text{gold}}$ & Partition stability & $\rho$ (median) & $\rho$ ($q_{25}$) \\
1425	\midrule
1426	50 & 50.4\% & 0.991 & 0.789 \\
1427	100 & 82.0\% & 1.000 & 0.991 \\
1428	200 & 85.6\% & 1.000 & 0.991 \\
1429	500 & 88.5\% & 1.000 & 0.991 \\
1430	\bottomrule
1431	\end{tabular}
1432	\end{table}
1433	
1434	The ASV ranking is highly robust: median Spearman $\rho \geq 0.99$ even at $n_{\text{gold}}{=}50$. The safe/fragile partition (5 safe vs.\ 2 fragile topologies) recovers reliably from $n_{\text{gold}} \geq 100$ (82\% stability), increasing to 89\% at $n_{\text{gold}}{=}500$. The remaining instability concentrates in source matrices with low diagonal dominance (e.g., VAST DeepSeek few-shot: $\min C_{kk} = 0.16$), where bootstrap noise can shift borderline ASV values across the partition boundary. All 8 truth partitions match the canonical safe/fragile partition, confirming that the theoretical dichotomy holds empirically.
1435	
1436	\subsection{Sign Reversal Determinants}
1437	\label{sec:sign_determinants}
1438	
1439	We investigate which confusion matrix features predict exposure sign reversal across the 23 empirical LLM configurations. For each matrix, we compute 10 structural features: $\min_k C_{kk}$ (minimum diagonal), $\overline{C_{kk}}$ (mean diagonal), $\max_{j \neq k} C_{jk}$ (maximum off-diagonal), $\max_{j \neq k} C_{jk}/C_{kk}$ (off-diagonal ratio), $\log(\kappa(C))$ (log condition number), mean and max column entropy, spectral gap, $\det(C)$, and minimum singular value. Sign reversal is defined as any exposure coefficient reversing sign under misclassification.
1440	
1441	\begin{table}[h]
1442	\centering
1443	\small
1444	\caption{Sign reversal rates by $K$ and best single-feature decision rule. Rule: $\det(C) < 0.014 \to$ sign reversal (accuracy 91.3\%, sensitivity 85.7\%, specificity 100\%). An AND rule ($\min_k C_{kk} < 0.55$ and mean entropy $> 0.40$) achieves 95.7\% accuracy with 100\% sensitivity.}
1445	\label{tab:sign_determinants}
1446	\begin{tabular}{lcc}
1447	\toprule
1448	$K$ & $n$ & Sign reversal rate \\
1449	\midrule
1450	2 & 7 & 0/7 (0\%) \\
1451	3 & 8 & 7/8 (87.5\%) \\
1452	10 & 8 & 7/8 (87.5\%) \\
1453	\bottomrule
1454	\end{tabular}
1455	\end{table}
1456	
1457	Binary matrices ($K{=}2$) never produce exposure sign reversal, consistent with classical attenuation theory. For $K \geq 3$, the determinant of $C$ is the strongest single predictor: $\det(C) < 0.014$ identifies sign-reversing matrices with 100\% specificity (zero false positives) and 85.7\% sensitivity. An AND rule combining $\min_k C_{kk} < 0.55$ with mean column entropy $> 0.40$ achieves 100\% sensitivity at 88.9\% specificity. These rules are robust to $\beta$-scaling (accuracy unchanged at $0.3{\times}$ and $3{\times}$ effect magnitude) but sensitive to $\beta$-sign structure: under uniform-positive $\beta$ (all coefficients same sign), no matrices produce sign reversal regardless of $C$, as cancellation across differently-signed coefficients is the underlying mechanism.
1458	
1459	\subsection{Y-Stratified Non-Differential Verification}
1460	\label{sec:y_stratified_test}
1461	
1462	We directly test the non-differential assumption (Definition~\ref{def:nondiff}) by stratifying confusion matrices by outcome-proxy variables and testing $C(Y{=}\text{high}) \approx C(Y{=}\text{low})$. Using 12 LLM configurations on VAST ($K{=}3$; 4 models $\times$ 3 prompting strategies, 1{,}500 samples each), we compute per-stratum confusion matrices under three Y-proxies and apply permutation tests ($B{=}10{,}000$, test statistic: $\max_{j,k} |C^{(0)}_{jk} - C^{(1)}_{jk}|$).
1463	
1464	\begin{table}[h]
1465	\centering
1466	\small
1467	\caption{Y-stratified non-differential test. Content-independent Y (text length) shows no significant violation (1/12 rejection $\approx$ expected false positive rate at $\alpha{=}0.05$). Content-dependent proxies (topic, sentiment) show expected violations since LLMs observe text content.}
1468	\label{tab:y_stratified}
1469	\begin{tabular}{lccc}
1470	\toprule
1471	\textbf{Y proxy} & \textbf{Type} & \textbf{Reject ($\alpha{=}0.05$)} & \textbf{Median $p$} \\
1472	\midrule
1473	Text length & Content-indep. & 1/12 & 0.490 \\
1474	Topic & Content-dep. & 11/12 & 0.002 \\
1475	Sentiment & Content-dep. & 10/12 & 0.017 \\
1476	\bottomrule
1477	\end{tabular}
1478	\end{table}
1479	
1480	The single text-length rejection (Llama-4 few-shot-3, $p{=}0.027$) is consistent with the expected false positive rate ($0.05 \times 12 = 0.6$). Content-dependent proxies (topic, sentiment) show systematic rejection because LLMs process text content from which these variables can be inferred, violating $Y \perp \text{text} \mid A$. In causal inference applications, $Y$ is typically an external outcome (e.g., health status, economic indicator) that cannot be inferred from the annotated text, satisfying the independence condition. The content-dependent rejections confirm statistical power: the test can detect violations when they exist.
1481	
1482	\section{Notation}
1483	\label{app:notation_table}
1484	
1485	\begin{table}[h]
1486	\centering
1487	\small
1488	\caption{Key notation used throughout the paper.}
1489	\label{tab:notation}
1490	\begin{tabular}{cl}
1491	\toprule
1492	\textbf{Symbol} & \textbf{Description} \\
1493	\midrule
1494	$K$ & Number of annotation categories \\
1495	$C$ & Column-stochastic confusion matrix, $C_{jk} = P(A^*{=}j \mid A{=}k)$ \\
1496	$A$, $A^*$ & True and observed (misclassified) annotation \\
1497	$T$ & Treatment variable \\
1498	$Y$ & Outcome variable \\
1499	$\tau$ & Causal effect of interest \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ee99d54-1504-486a-8ef8-d26a70c42800",
  "isSidechain": true,
  "promptId": "6231d775-db71-46d9-bac6-397081d485cb",
  "agentId": "a20940d9e1e09d4c5",
  "type": "user",
  "uuid": "b0eb8895-6a8d-4009-a77c-a4ff4f04689d",
  "sourceToolAssistantUUID": "9ee99d54-1504-486a-8ef8-d26a70c42800",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T19:17:44.815Z_

Let me continue reading the rest:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0eb8895-6a8d-4009-a77c-a4ff4f04689d",
  "isSidechain": true,
  "agentId": "a20940d9e1e09d4c5",
  "requestId": "req_011CbL3CbM5xwd1fpEDNdxu3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "10e58809-7ccf-49dd-b866-685bf4017f95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SnJ7paqk7EfzGF2dMnHn5D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 17800,
      "cache_read_input_tokens": 51189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17800,
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

_source line 14 · 2026-05-23T19:17:45.797Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LSeZrGj7A7m8MtLiaowrcg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": 100,
  "offset": 1500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10e58809-7ccf-49dd-b866-685bf4017f95",
  "isSidechain": true,
  "agentId": "a20940d9e1e09d4c5",
  "requestId": "req_011CbL3CbM5xwd1fpEDNdxu3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8dcdfbbc-324f-43c1-bfe1-0fbdf507e1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SnJ7paqk7EfzGF2dMnHn5D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 17800,
      "cache_read_input_tokens": 51189,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 135,
          "cache_read_input_tokens": 51189,
          "cache_creation_input_tokens": 17800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17800,
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

_source line 15 · 2026-05-23T19:17:45.802Z_

<details><summary>↩ Tool result · `toolu_01LSeZrGj7A7m8MtLiaowrcg`</summary>

```text
1500	$\delta$ & ASV perturbation parameter, $C(\delta) = (1{-}\delta)I + \delta C_0$ \\
1501	$\delta^*$ & Critical ASV value (magnitude/significance/sign-flip) \\
1502	$B(C)$ & Bias function, $= \operatorname{plim}(\hat{\tau}) - \tau$ \\
1503	$\beta_k$ & Treatment effect coefficient for category $k$ \\
1504	$D_k$ & Dummy variable for category $k$ \\
1505	\bottomrule
1506	\end{tabular}
1507	\end{table}
1508	
1509	\section{Use of AI Assistants}
1510	\label{app:ai-assistants}
1511	
1512	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
1513	\begin{itemize}
1514	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
1515	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
1516	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
1517	\end{itemize}
1518	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dcdfbbc-324f-43c1-bfe1-0fbdf507e1e8",
  "isSidechain": true,
  "promptId": "6231d775-db71-46d9-bac6-397081d485cb",
  "agentId": "a20940d9e1e09d4c5",
  "type": "user",
  "uuid": "a0983d91-4444-416f-ba51-fd565b0964f5",
  "sourceToolAssistantUUID": "8dcdfbbc-324f-43c1-bfe1-0fbdf507e1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-23T19:19:33.029Z_

Now let me compile all the numerical claims I've extracted from both files:

## COMPREHENSIVE NUMERICAL EXTRACTION REPORT

### File 1: conclusion.tex

**[file:conclusion.tex:4]** "at $K{\geq}3$, exposure and IV can reverse treatment effect signs while five topologies preserve them" → value: K ≥ 3

**[file:conclusion.tex:8]** "sign preservation holds at 97.3\% under non-proportional effects" → value: 97.3%

**[file:conclusion.tex:8]** "$\lambda(C)$ falls outside $[0,1]$ in 15\% of configurations" → value: 15%

---

### File 2: appendix_proofs.tex

**[file:appendix_proofs.tex:220]** "$\tau{=}2.0$, $\boldsymbol{\alpha}{=}(1.5,{-}1.0)$" → value: 2.0, 1.5, -1.0

**[file:appendix_proofs.tex:220]** "$\boldsymbol{\beta}^{(A)}{=}(1.0,{-}0.5)$, $\sigma_T{=}1.0$, $\mathbf{p}{=}(0.40,0.35,0.25)$" → value: 1.0, -0.5, 1.0, 0.40, 0.35, 0.25

**[file:appendix_proofs.tex:222]** "$\operatorname{Var}(g) = 0.962$" → value: 0.962

**[file:appendix_proofs.tex:223]** "$\operatorname{Var}(f) = 0.362$" → value: 0.362

**[file:appendix_proofs.tex:224]** "$\bar{B} = \sqrt{0.962\times 0.362}\;/\;1.0^2 = 0.590$" → value: 0.590

**[file:appendix_proofs.tex:226]** "$|\tau|{=}2.0 > \bar{B}{=}0.590$" → value: 2.0, 0.590

**[file:appendix_proofs.tex:227]** "$B_{\mathrm{OV}}=\operatorname{Cov}(g,f)/\operatorname{Var}(T)=0.588/1.962={+}0.300$" → value: 0.588, 1.962, 0.300

**[file:appendix_proofs.tex:227]** "$\tau_{\mathrm{OV}}{=}2.300>0$" → value: 2.300

**[file:appendix_proofs.tex:230]** "$K{=}10$, $\boldsymbol{\beta} = (0, 1.0, {-}0.5, 0.7, {-}0.3, 0.5, {-}0.2, 0.4, {-}0.15, 0.3)$" → value: 10, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3

**[file:appendix_proofs.tex:298]** "20{,}000 random $(C_0,p,g)$ triples per $K\in\{3,5,7\}$" → value: 20000, 3, 5, 7

**[file:appendix_proofs.tex:298]** "worst-case $|B|$ step deviations $< 0.013$" → value: 0.013

**[file:appendix_proofs.tex:299]** "worst-case $|B|$ step deviations $< 0.013$; ... $V_B(\delta)=(\delta{-}\tfrac{1}{2})^2$ increases on $(\tfrac{1}{2},1]$" → value: 0.013, 0.5, 1

**[file:appendix_proofs.tex:304]** "20{,}000 random $C_0$ matrices, $K \in \{3,5,7\}$" → value: 20000, 3, 5, 7

**[file:appendix_proofs.tex:304]** "worst-case step deviations of 0.011 (confounding)" → value: 0.011

**[file:appendix_proofs.tex:312]** "$T \sim \operatorname{Bernoulli}(0.5)$" → value: 0.5

**[file:appendix_proofs.tex:333]** "$D(C) = \operatorname{Var}(T) = 0.25$" → value: 0.25

**[file:appendix_proofs.tex:337]** "$\operatorname{Cov}(T,f(A)) = 0.25\,\tau_{\mathrm{ind}}$" → value: 0.25

**[file:appendix_proofs.tex:344]** "$100{,}000$ independently sampled column-stochastic matrices $C$" → value: 100000

**[file:appendix_proofs.tex:351]** "$R=\operatorname{Cov}(T,f(A))=0.25\,\tau_{\mathrm{ind}}$ and $D=\operatorname{Var}(T)=0.25$" → value: 0.25

**[file:appendix_proofs.tex:355]** "$T\in\{0,1\}$" → value: 0, 1

**[file:appendix_proofs.tex:382]** "$\tau_{\mathrm{dir}}{=}0.5$, $\boldsymbol{\gamma}{=}(0,0,0)$, $\boldsymbol{\delta}{=}(0,0.8,{-}0.6)$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$" → value: 0.5, 0.8, -0.6, 1.0, -0.5

**[file:appendix_proofs.tex:384]** "$\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]=0.351$" → value: 0.351

**[file:appendix_proofs.tex:385]** "$\tau_{\mathrm{total}}=0.5+0.351=0.851>0$" → value: 0.5, 0.351, 0.851

**[file:appendix_proofs.tex:481]** "$N{=}10{,}000$ configurations" → value: 10000

**[file:appendix_proofs.tex:481]** "30{,}000 trials (pooled observed range $[1.2{\times}10^{-5},\,0.850]$; zero out-of-bounds)" → value: 30000, 0.85

**[file:appendix_proofs.tex:482]** "$\lambda(C)$ exceeds $[0,1]$ in $\sim15$--$17\%$ of trials" → value: 15%-17%

**[file:appendix_proofs.tex:494]** "6 (24\%) satisfy $\|C - C_{\mathrm{sym}}\|_F / \|C\|_F < 0.05$" → value: 6, 24%, 0.05

**[file:appendix_proofs.tex:494]** "relative Frobenius deviation ranges from 0.015 to 0.381" → value: 0.015, 0.381

**[file:appendix_proofs.tex:581]** "$\tau{=}1.0$, $\boldsymbol{\delta}_T{=}(0,\,0.5,\,{-}0.3)$, $\boldsymbol{\delta}_Y{=}(0,\,0.8,\,0.6)$" → value: 1.0, 0.5, -0.3, 0.8, 0.6

**[file:appendix_proofs.tex:581]** "$5{\times}10^6$-sample Monte Carlo" → value: 5000000

**[file:appendix_proofs.tex:583]** "$\operatorname{Var}(g(A)) = 0.187$" → value: 0.187

**[file:appendix_proofs.tex:584]** "$\operatorname{Var}(h(A)) = 0.076$" → value: 0.076

**[file:appendix_proofs.tex:585]** "$\mathbb{E}[\operatorname{Var}(T\mid A)] = 0.813$" → value: 0.813

**[file:appendix_proofs.tex:586]** "$\bar{B}_{\mathrm{col}} = \sqrt{0.187\times 0.076}\;/\;0.813 = 0.147$" → value: 0.147

**[file:appendix_proofs.tex:588]** "Proposition~\ref{prop:col_gen} guarantees sign preservation" → value: none (reference)

**[file:appendix_proofs.tex:589]** "$B_{\mathrm{Berkson}}{=}{-}0.114$, giving $\tau+B_{\mathrm{Berkson}}{=}0.886{>}0$" → value: -0.114, 0.886

**[file:appendix_proofs.tex:590]** "$\tau_{\mathrm{sign\,flip}}{=}0\%$" → value: 0%

**[file:appendix_proofs.tex:590]** "$100{,}000$ random column-stochastic $C$" → value: 100000

**[file:appendix_proofs.tex:653]** "$\alpha_U{=}1.0$, $\lambda{=}1.0$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$, $\boldsymbol{\gamma}{=}(0,0.5,{-}0.3)$, $\boldsymbol{\delta}{=}(0,1.0,{-}0.8)$" → value: 1.0, 1.0, 1.0, -0.5, 0.5, -0.3, 1.0, -0.8

**[file:appendix_proofs.tex:655]** "$\lambda\alpha_U/\operatorname{Var}(T) = 1.0\times 1.0\,/\,2.0 = 0.500$" → value: 1.0, 1.0, 2.0, 0.500

**[file:appendix_proofs.tex:656]** "$\operatorname{Cov}(T,f(A))/\operatorname{Var}(T) = 0.594\,/\,2.0 = 0.297$" → value: 0.594, 2.0, 0.297

**[file:appendix_proofs.tex:658]** "$\operatorname{plim}\hat\tau(C)\in[0.500,\,0.797]>0$ for all $C$" → value: 0.500, 0.797

**[file:appendix_proofs.tex:671]** "Uniform prior: $\mathbf{p}=(1/3,\,1/3,\,1/3)$" → value: 1/3, 1/3, 1/3

**[file:appendix_proofs.tex:672]** "$\beta_1=1$,\; $\beta_2=-10$" → value: 1, -10

**[file:appendix_proofs.tex:677-679]** Confusion matrix with values: "0.60, 0.10, 0.10, 0.10, 0.60, 0.39, 0.30, 0.30, 0.51" → values: 0.60, 0.10, 0.10, 0.10, 0.60, 0.39, 0.30, 0.30, 0.51

**[file:appendix_proofs.tex:681]** "$C_{kk}\in\{0.60,\,0.60,\,0.51\}$, all > 0.5" → value: 0.60, 0.60, 0.51, 0.5

**[file:appendix_proofs.tex:694-696]** "$q_0 = \tfrac{1}{3}(0.60+0.10+0.10)=0.267$, $q_1 = \tfrac{1}{3}(0.10+0.60+0.39)=0.363$, $q_2 = \tfrac{1}{3}(0.30+0.30+0.51)=0.370$" → values: 0.267, 0.363, 0.370

**[file:appendix_proofs.tex:702]** "$\mathbb{E}[Y\mid A^*{=}0] = \frac{0.0333-0.3333}{0.267} = -1.125$" → value: 0.0333, -0.3333, 0.267, -1.125

**[file:appendix_proofs.tex:705]** "$\mathbb{E}[Y\mid A^*{=}1] = \frac{0.200-1.300}{0.363} = -3.028$" → value: 0.200, -1.300, 0.363, -3.028

**[file:appendix_proofs.tex:708]** "$\mathbb{E}[Y\mid A^*{=}2] = \frac{0.100-1.700}{0.370} = -4.324$" → value: 0.100, -1.700, 0.370, -4.324

**[file:appendix_proofs.tex:714]** "$\operatorname{plim}\hat\beta_1 = \mathbb{E}[Y\mid A^*{=}1]-\mathbb{E}[Y\mid A^*{=}0] = -3.028-(-1.125) = \mathbf{-1.903}$" → value: -3.028, -1.125, -1.903

**[file:appendix_proofs.tex:717]** "true $\beta_1=+1>0$ but $\operatorname{plim}\hat\beta_1=-1.903<0$" → value: 1, -1.903

**[file:appendix_proofs.tex:720]** "$C_{12}=0.39$ (probability of classifying true category~2 as $A^*{=}1$)" → value: 0.39

**[file:appendix_proofs.tex:750]** "$C_{kk}>0$" → value: 0

**[file:appendix_proofs.tex:772]** "$\epsilon$, $P$ a random permutation), block-diagonal... near-uniform ($C_{kk} \to 1/K$)" → value: 1/K

**[file:appendix_proofs.tex:778]** "$K{=}3,5,7$, seven topologies, and three $\beta$ configurations ($N{=}1{,}000$ matrices per cell, 545{,}945 total curves)" → value: 3, 5, 7, 1000, 545945

**[file:appendix_proofs.tex:783]** "Near-permutation: 35.3\%" → value: 35.3%

**[file:appendix_proofs.tex:783]** "Non-monotone: Near-permutation 35.3\%, Max $\varepsilon_{\mathrm{abs}}$ = 0.016" → value: 35.3%, 0.016

**[file:appendix_proofs.tex:784]** "Block-diagonal: 0\%, 0" → value: 0%, 0

**[file:appendix_proofs.tex:785]** "Sparse: 2.3\%, 0.003" → value: 2.3%, 0.003

**[file:appendix_proofs.tex:786]** "Near-uniform: 0\%, 0" → value: 0%, 0

**[file:appendix_proofs.tex:788]** "All structures: 11.9\%, 0.016" → value: 11.9%, 0.016

**[file:appendix_proofs.tex:793]** "$\varepsilon_{\mathrm{abs}} = 0.016 < 0.02$" → value: 0.016, 0.02

**[file:appendix_proofs.tex:803]** "Binarization introduces additional bias varying 154$\times$ across topologies: from $\bar{\Delta}{=}0.006$ (M-bias) to $\bar{\Delta}{=}0.926$ (IV)" → value: 154, 0.006, 0.926

**[file:appendix_proofs.tex:803]** "14\% and 17.5\% sign flips during binarization" → value: 14%, 17.5%

**[file:appendix_proofs.tex:808]** "Magnitude ASV at $\tau{=}0.5$, 10\% threshold" → value: 0.5, 10%

**[file:appendix_proofs.tex:815]** "IV: 0.101--0.607" → value: 0.101, 0.607

**[file:appendix_proofs.tex:815]** "IV sign-flip: 1.1--6.7" → value: 1.1, 6.7

**[file:appendix_proofs.tex:816]** "Front-door: 0.064--0.387" → value: 0.064, 0.387

**[file:appendix_proofs.tex:817]** "Confounding: 0.081--0.487" → value: 0.081, 0.487

**[file:appendix_proofs.tex:818]** "Mediation: 0.076--0.454" → value: 0.076, 0.454

**[file:appendix_proofs.tex:819]** "Collider: 0.338--2.028" → value: 0.338, 2.028

**[file:appendix_proofs.tex:820]** "M-bias: $\infty$" → value: infinity

**[file:appendix_proofs.tex:821]** "Exposure sign-flip: 83.4\%$^*$" → value: 83.4%

**[file:appendix_proofs.tex:830]** "circles: HumAID $K{=}10$; squares: VAST $K{=}3$; triangles: CivilComments $K{=}2$" → value: 10, 3, 2

**[file:appendix_proofs.tex:837]** "Binarization collapse $\Delta$ across topologies... varying 154$\times$ from M-bias (0.006) to IV (0.926)" → value: 154, 0.006, 0.926

**[file:appendix_proofs.tex:857]** "Confounding DSL: 48.0%, SIMEX: 35.1%, PPI++: 83.2%" → value: 48.0%, 35.1%, 83.2%

**[file:appendix_proofs.tex:858]** "Mediation DSL: 52.9%, SIMEX: 39.1%, PPI++: 54.1%" → value: 52.9%, 39.1%, 54.1%

**[file:appendix_proofs.tex:859]** "Collider DSL: -92.6%, SIMEX: 31.8%, PPI++: 50.5%" → value: -92.6%, 31.8%, 50.5%

**[file:appendix_proofs.tex:860]** "M-bias DSL: -267, SIMEX: 0.1%, PPI++: -88.0%" → value: -267, 0.1%, -88.0%

**[file:appendix_proofs.tex:862]** "Front-door Naive: -52.7%, MLA: -111.5%, DSL: -29.0%, SIMEX: -62.4%, PPI++: 74.1%" → value: -52.7%, -111.5%, -29.0%, -62.4%, 74.1%

**[file:appendix_proofs.tex:863]** "Exposure: -44.8%, -89.0%, -59.5%, -9.8%, 75.5%" → value: -44.8%, -89.0%, -59.5%, -9.8%, 75.5%

**[file:appendix_proofs.tex:864]** "IV: -40.4%, -58.7%, -206.1%, 59.4%, 79.4%" → value: -40.4%, -58.7%, -206.1%, 59.4%, 79.4%

**[file:appendix_proofs.tex:866]** "Grand mean: -19.7%, -37.0%, -79.0%, 13.3%, 47.0%" → value: -19.7%, -37.0%, -79.0%, 13.3%, 47.0%

**[file:appendix_proofs.tex:876]** "Diagonal-dominant: $C_{kk}{=}0.7$" → value: 0.7

**[file:appendix_proofs.tex:876]** "Moderate noise: $C_{kk}{=}0.5$" → value: 0.5

**[file:appendix_proofs.tex:875]** "Near-permutation: $C_{kk}{=}0.4$, largest off-diagonal 0.5" → value: 0.4, 0.5

**[file:appendix_proofs.tex:876]** "Asymmetric: $C_{kk}$ varies (0.8, 0.5, 0.3)" → value: 0.8, 0.5, 0.3

**[file:appendix_proofs.tex:877]** "Block confusion: $C_{12}{=}C_{21}{=}0.4$" → value: 0.4

**[file:appendix_proofs.tex:878]** "Heavy noise: $C_{kk}{=}0.4$" → value: 0.4

**[file:appendix_proofs.tex:897]** "Exposure, IV: sign reversal 83.4\% / 52.6\%" → value: 83.4%, 52.6%

**[file:appendix_proofs.tex:905]** "47.0\% RMSE red., 96.8\% coverage" → value: 47.0%, 96.8%

**[file:appendix_proofs.tex:910]** "48.0\% / 52.9\% RMSE reduction" → value: 48.0%, 52.9%

**[file:appendix_proofs.tex:912]** "59.4\% RMSE reduction" → value: 59.4%

**[file:appendix_proofs.tex:948]** "$2.3\!\times\!10^{-15}$" → value: 2.3e-15

**[file:appendix_proofs.tex:948]** "deepseek_zero-shot: $2.3\!\times\!10^{-15}$, +0.00%, $8.1\!\times\!10^{-4}$, -0.09\%" → value: 2.3e-15, 0.00%, 8.1e-4, -0.09%

**[file:appendix_proofs.tex:949]** "llama4_few-shot-3: $5.2\!\times\!10^{-15}$, +0.00%, $6.8\!\times\!10^{-4}$, -0.07\%" → value: 5.2e-15, 0.00%, 6.8e-4, -0.07%

**[file:appendix_proofs.tex:950]** "llama4_few-shot-5: $4.3\!\times\!10^{-15}$, +0.00%, $6.8\!\times\!10^{-4}$, -0.06\%" → value: 4.3e-15, 0.00%, 6.8e-4, -0.06%

**[file:appendix_proofs.tex:951]** "llama4_zero-shot: $1.6\!\times\!10^{-15}$, +0.00%, $5.9\!\times\!10^{-4}$, -0.05\%" → value: 1.6e-15, 0.00%, 5.9e-4, -0.05%

**[file:appendix_proofs.tex:952]** "qwen2.5-7b_few-shot-3: $7.2\!\times\!10^{-15}$, -0.00%, $6.8\!\times\!10^{-4}$, -0.01\%" → value: 7.2e-15, -0.00%, 6.8e-4, -0.01%

**[file:appendix_proofs.tex:953]** "qwen2.5-7b_few-shot-5: $8.2\!\times\!10^{-15}$, +0.00%, $5.6\!\times\!10^{-4}$, +0.05\%" → value: 8.2e-15, 0.00%, 5.6e-4, 0.05%

**[file:appendix_proofs.tex:955]** "Mean: 0.0%, -0.04\%" → value: 0.0%, -0.04%

**[file:appendix_proofs.tex:960]** "mean bias reduction is $-0.04\%$... range $[-0.09\%, +0.05\%]$" → value: -0.04%, -0.09%, 0.05%

**[file:appendix_proofs.tex:968]** "OR~$= 0.89$" → value: 0.89

**[file:appendix_proofs.tex:970]** "83.2\% RMSE reduction for confounding" → value: 83.2%

**[file:appendix_proofs.tex:970]** "MC-SIMEX (35.1%)" → value: 35.1%

**[file:appendix_proofs.tex:976]** "52.6\% Wald sign-flip rate" → value: 52.6%

**[file:appendix_proofs.tex:993]** "Full: 100.0%, 51.7%, 48.3%, $10^{5}\!\times$" → value: 100.0%, 51.7%, 48.3%, 100000

**[file:appendix_proofs.tex:994]** "$d \geq 0.5$: 100.0%, 0.0%, 100.0%, $28.6\times$" → value: 0.5, 100.0%, 0.0%, 100.0%, 28.6

**[file:appendix_proofs.tex:995]** "$d \geq 0.7$: 100.0%, 0.0%, 100.0%, $2.4\times$" → value: 0.7, 100.0%, 0.0%, 100.0%, 2.4

**[file:appendix_proofs.tex:996]** "$d \geq 0.9$: 100.0%, 0.0%, 100.0%, $1.2\times$" → value: 0.9, 100.0%, 0.0%, 100.0%, 1.2

**[file:appendix_proofs.tex:1001]** "$d{\geq}0.7$, exposure violation drops to 13.7\% (sign reversal 2.1\%, amplification 11.7\%)" → value: 0.7, 13.7%, 2.1%, 11.7%

**[file:appendix_proofs.tex:1001]** "At $d{\geq}0.9$... inflates $|\tau|$ by up to $1.24\times$" → value: 0.9, 1.24

**[file:appendix_proofs.tex:1008]** "10 model configurations (3 LLMs $\times$ 2--4 prompt types) and 19 qualifying topics (minimum 10 samples per topic)" → value: 10, 3, 2-4, 19, 10

**[file:appendix_proofs.tex:1010]** "$B{=}10{,}000$" → value: 10000

**[file:appendix_proofs.tex:1010]** "95th percentile ranges from 0.90 to 0.98" → value: 0.90, 0.98

**[file:appendix_proofs.tex:1010]** "For the 5 largest topics ($n \geq 28$), expected per-topic max deviation at the 95th percentile is 0.38--0.49" → value: 5, 28, 0.38, 0.49

**[file:appendix_proofs.tex:1017]** "$n_{\text{gold}} \in \{50, 100, 200, 500\}$" → value: 50, 100, 200, 500

**[file:appendix_proofs.tex:1017]** "10{,}000 random matrices per $\varepsilon$" → value: 10000

**[file:appendix_proofs.tex:1028]** "$\varepsilon{=}0.00$: 2.0%, 11.5%, 13.3%" → value: 0.00, 2.0%, 11.5%, 13.3%

**[file:appendix_proofs.tex:1029]** "$\varepsilon{=}0.01$: 2.4%, 12.4%, 14.7%" → value: 0.01, 2.4%, 12.4%, 14.7%

**[file:appendix_proofs.tex:1030]** "$\varepsilon{=}0.05$: 2.8%, 13.0%, 15.7%" → value: 0.05, 2.8%, 13.0%, 15.7%

**[file:appendix_proofs.tex:1031]** "$\varepsilon{=}0.10$: 4.5%, 16.7%, 20.9%" → value: 0.10, 4.5%, 16.7%, 20.9%

**[file:appendix_proofs.tex:1032]** "$\varepsilon{=}0.20$: 9.7%, 23.7%, 32.6%" → value: 0.20, 9.7%, 23.7%, 32.6%

**[file:appendix_proofs.tex:1033]** "$\varepsilon{=}0.30$: 15.5%, 28.7%, 42.8%" → value: 0.30, 15.5%, 28.7%, 42.8%

**[file:appendix_proofs.tex:1034]** "$\varepsilon{=}0.50$: 22.9%, 34.9%, 54.6%" → value: 0.50, 22.9%, 34.9%, 54.6%

**[file:appendix_proofs.tex:1039]** "At $\varepsilon{=}0.10$, the violation rate increases by 7.6~pp" → value: 0.10, 7.6

**[file:appendix_proofs.tex:1039]** "at $\varepsilon{=}0.50$, it rises to 54.6\% (+41.2~pp)" → value: 0.50, 54.6%, 41.2

**[file:appendix_proofs.tex:1042]** "96 configurations (4 topologies $\times$ 2 $K$ $\times$ 3 CM qualities $\times$ 4 $\varepsilon$, 100 MC replications each)" → value: 96, 4, 2, 3, 4, 100

**[file:appendix_proofs.tex:1042]** "At $\varepsilon{=}0.10$, the maximum sign-flip rate is 7\% (IV, low-quality $C_{kk}{=}0.4$, $K{=}3$)" → value: 0.10, 7%, 0.4, 3

**[file:appendix_proofs.tex:1103]** "100{,}000 matrices each: sign-flip guarantees hold for the same five topologies, and IV sign-flip rates remain within 51--53\%" → value: 100000, 51%-53%

**[file:appendix_proofs.tex:1076]** "$n{=}1{,}500$, $B{=}1{,}000$" → value: 1500, 1000

**[file:appendix_proofs.tex:1085]** "Exposure: $\delta^*{=}0.937$, 95\% CI [0.602, 1.363], 907 / 1000" → value: 0.937, 0.602, 1.363, 907, 1000

**[file:appendix_proofs.tex:1086]** "IV: $\delta^*{=}0.754$, 95\% CI [0.435, 1.290], 902 / 1000" → value: 0.754, 0.435, 1.290, 902, 1000

**[file:appendix_proofs.tex:1091]** "exposure CI width narrows from 0.60 ($n{=}500$) to 0.05 ($n{=}50{,}000$)" → value: 0.60, 500, 0.05, 50000

**[file:appendix_proofs.tex:1091]** "IV from 0.52 to 0.04" → value: 0.52, 0.04

**[file:appendix_proofs.tex:1108]** "55.4\% are flagged as magnitude-ASV-unsafe" → value: 55.4%

**[file:appendix_proofs.tex:1108]** "CivilComments ($K{=}2$), 100\% of scenarios are ASV-unsafe" → value: 2, 100%

**[file:appendix_proofs.tex:1108]** "$F_1$ ranging from 0.69 to 0.82" → value: 0.69, 0.82

**[file:appendix_proofs.tex:1115]** "$K{=}3$, $\tau{=}0.5$, five $C_0$ diagonal values $\in\{0.5,0.6,0.7,0.8,0.9\}$" → value: 3, 0.5, 0.5, 0.6, 0.7, 0.8, 0.9

**[file:appendix_proofs.tex:1119]** "alternating-large ($\delta^*{=}0.348$)" → value: 0.348

**[file:appendix_proofs.tex:1119]** "alternating-large ($\beta_2/\beta_1 = -0.5$) and alternating-small ($\beta_2/\beta_1 = -0.5$) share the same ratio and yield identical $\delta^*{=}0.090$" → value: -0.5, -0.5, 0.090

**[file:appendix_proofs.tex:1119]** "same-sign ($\beta_2/\beta_1 = 0.6$) gives $\delta^*{=}0.223$" → value: 0.6, 0.223

**[file:appendix_proofs.tex:1126]** "10{,}000 random $C_0$ matrices from Dirichlet$(1,\dots,1)$ per topology for $K \in \{3,5,7\}$ (210{,}000 total)" → value: 10000, 3, 5, 7, 210000

**[file:appendix_proofs.tex:1126]** "100 points" (Gauss-Hermite quadrature) → value: 100

**[file:appendix_proofs.tex:1131]** "$\delta$ step $= 0.01$" → value: 0.01

**[file:appendix_proofs.tex:1137]** "Confounding: $K{=}3$ 8467, $K{=}5$ 8063, $K{=}7$ 7892, worst mag. 0.011, non-dec" → value: 8467, 8063, 7892, 0.011

**[file:appendix_proofs.tex:1138]** "Mediation: 8236, 7905, 7893, 0.013, non-dec" → value: 8236, 7905, 7893, 0.013

**[file:appendix_proofs.tex:1139]** "Collider: 8683, 7669, 7570, 0.005, non-inc" → value: 8683, 7669, 7570, 0.005

**[file:appendix_proofs.tex:1140]** "Exposure: 485, 205, 77, 0.056$^*$, non-dec" → value: 485, 205, 77, 0.056

**[file:appendix_proofs.tex:1141]** "M-bias: 9791, 7783, 7399, 0.002, non-inc" → value: 9791, 7783, 7399, 0.002

**[file:appendix_proofs.tex:1142]** "IV: 7433, 6015, 5711, $>10^6$, non-dec" → value: 7433, 6015, 5711

**[file:appendix_proofs.tex:1143]** "Front-door: 8429, 8079, 7899, 0.013, non-dec" → value: 8429, 8079, 7899, 0.013

**[file:appendix_proofs.tex:1148]** "Violations are 60--97\% of matrices" → value: 60%-97%

**[file:appendix_proofs.tex:1148]** "Adversarial search (500 restarts per configuration)" → value: 500

**[file:appendix_proofs.tex:1148]** "$\varepsilon < 0.03$ for collider and M-bias" → value: 0.03

**[file:appendix_proofs.tex:1148]** "$\varepsilon < 0.06$ at default DGP parameters... exposure satisfies $\varepsilon_{p99} < 0.008$" → value: 0.06, 0.008

**[file:appendix_proofs.tex:1148]** "extreme-tail matrices ($<$0.02\% of draws) reach $\varepsilon \approx 0.15$" → value: 0.02%, 0.15

**[file:appendix_proofs.tex:1148]** "$\alpha \in [0.6, 1.5]$ (topology-dependent): ... confounding, mediation, and front-door, $\alpha \approx 1.4$; ... exposure, $\alpha \approx 1.0$; ... collider and M-bias, $\alpha \approx 0.7$" → value: 0.6, 1.5, 1.4, 1.0, 0.7

**[file:appendix_proofs.tex:1148]** "$\varepsilon \leq 0.137/\sqrt{K}$" → value: 0.137

**[file:appendix_proofs.tex:1150]** "$\tau \in \{0.1, 0.5, 1.0, 2.0, 5.0\}$" → value: 0.1, 0.5, 1.0, 2.0, 5.0

**[file:appendix_proofs.tex:1151]** "$\varepsilon < 0.03$ for $\tau \geq 0.5$" → value: 0.03, 0.5

**[file:appendix_proofs.tex:1151]** "mediation produces 1{,}950 / 30{,}000 violations (worst $\varepsilon{=}0.130$ at $K{=}3$)" → value: 1950, 30000, 0.130, 3

**[file:appendix_proofs.tex:1151]** "confounding 200 / 30{,}000 (worst $\varepsilon{=}0.118$ at $K{=}3$)" → value: 200, 30000, 0.118, 3

**[file:appendix_proofs.tex:1151]** "single mediation violation at $\tau{=}2.0$ ($\varepsilon{=}0.112$, 1/30{,}000 matrices)" → value: 2.0, 0.112, 30000

**[file:appendix_proofs.tex:1151]** "$p_{99}$ bound ($\varepsilon_{p99}{=}0.005$)" → value: 0.005

**[file:appendix_proofs.tex:1151]** "Collider and M-bias remain robust at all $\tau$ ($\varepsilon{<}0.022$ and $\varepsilon{<}0.015$ respectively)" → value: 0.022, 0.015

**[file:appendix_proofs.tex:1151]** "Exposure shows scattered tail outliers but $\overline{\varepsilon} \approx 3\!\times\!10^{-4}$" → value: 3e-4

**[file:appendix_proofs.tex:1151]** "Front-door inverts the pattern... reaching $0.139$ at $\tau{=}5$, $K{=}3$, with 664 violations" → value: 0.139, 5, 3, 664

**[file:appendix_proofs.tex:1162]** "Confounding: $\tau{=}0.1$ 0.118, $\tau{=}0.5$ 0.027, $\tau{=}1.0$ 0.014, $\tau{=}2.0$ 0.007, $\tau{=}5.0$ 0.002" → value: 0.1, 0.118, 0.5, 0.027, 1.0, 0.014, 2.0, 0.007, 5.0, 0.002

**[file:appendix_proofs.tex:1163]** "Mediation: 0.130 (1950), 0.026, 0.013, 0.112 (1), 0.003" → value: 0.130, 1950, 0.026, 0.013, 0.112, 1, 0.003

**[file:appendix_proofs.tex:1164]** "Collider: 0.022, 0.006, 0.005, 0.004, 0.002" → value: 0.022, 0.006, 0.005, 0.004, 0.002

**[file:appendix_proofs.tex:1165]** "Exposure: 0.111 (5), 0.122 (2), 0.152 (2), 0.089 (3), 0.148 (3)" → value: 0.111, 5, 0.122, 2, 0.152, 2, 0.089, 3, 0.148, 3

**[file:appendix_proofs.tex:1166]** "M-bias: 0.014, 0.003, 0.001, 0.001, 0.000" → value: 0.014, 0.003, 0.001, 0.001, 0.000

**[file:appendix_proofs.tex:1167]** "Front-door: 0.003, 0.013, 0.027, 0.051, 0.139 (664)" → value: 0.003, 0.013, 0.027, 0.051, 0.139, 664

**[file:appendix_proofs.tex:1173]** "$\beta \in \{0.1, 0.5, 1.0, 2.0, 5.0\}$ and noise variance $\sigma^2 \in \{0.5, 1.0, 2.0\}$" → value: 0.1, 0.5, 1.0, 2.0, 5.0, 0.5, 1.0, 2.0

**[file:appendix_proofs.tex:1192]** "Near ($\sigma{=}0.1$): 10.3%, 0.87\%" → value: 0.1, 10.3%, 0.87%

**[file:appendix_proofs.tex:1193]** "Near ($\sigma{=}0.3$): 19.0%, 0.96\%" → value: 0.3, 19.0%, 0.96%

**[file:appendix_proofs.tex:1194]** "Near ($\sigma{=}0.5$): 22.4%, 0.93\%" → value: 0.5, 22.4%, 0.93%

**[file:appendix_proofs.tex:1195]** "Independent ($f \perp g$): 22.9%, 0.17\%" → value: 22.9%, 0.17%

**[file:appendix_proofs.tex:1197]** "NLP-realistic: 0.07%, 0.0\%" → value: 0.07%, 0.0%

**[file:appendix_proofs.tex:1207]** "$N \in \{1000, 5000, 10{,}000, 50{,}000\}$ and three error levels ($C_{kk} \in \{0.9, 0.7, 0.5\}$), 200 Monte Carlo replicates per cell" → value: 1000, 5000, 10000, 50000, 0.9, 0.7, 0.5, 200

**[file:appendix_proofs.tex:1218]** "Confounding Low: -0.003\%" → value: -0.003%

**[file:appendix_proofs.tex:1218]** "Confounding Med: <0.001\%" → value: 0.001%

**[file:appendix_proofs.tex:1218]** "Confounding High: <0.001\%" → value: 0.001%

**[file:appendix_proofs.tex:1219]** "Mediation: -0.004%, <0.001%, <0.001\%" → value: -0.004%, 0.001%, 0.001%

**[file:appendix_proofs.tex:1220]** "Collider: -0.033%, -0.020%, <0.001\%" → value: -0.033%, -0.020%, 0.001%

**[file:appendix_proofs.tex:1221]** "M-bias: -0.049%, -0.010%, <0.001\%" → value: -0.049%, -0.010%, 0.001%

**[file:appendix_proofs.tex:1222]** "Front-door: 0.001%, -0.001%, <0.001\%" → value: 0.001%, -0.001%, 0.001%

**[file:appendix_proofs.tex:1224]** "Exposure: -68.5%, -48.7%, -22.5\%" → value: -68.5%, -48.7%, -22.5%

**[file:appendix_proofs.tex:1229]** "standard deviations... up to 2.6\% std at $N{=}10{,}000$" → value: 2.6%, 10000

**[file:appendix_proofs.tex:1236]** "$K{=}3$, $N{=}10{,}000$, 100 MC replications, 5 Dirichlet confusion matrices with $\min_k C_{kk}{\geq}0.6$" → value: 3, 10000, 100, 5, 0.6

**[file:appendix_proofs.tex:1247]** "Confounding: +84.8%, +88.6%, +91.8%, +94.2%, +95.2%" → value: 84.8%, 88.6%, 91.8%, 94.2%, 95.2%

**[file:appendix_proofs.tex:1248]** "Exposure: +75.2%, +83.1%, +87.1%, +91.2%, +93.8%" → value: 75.2%, 83.1%, 87.1%, 91.2%, 93.8%

**[file:appendix_proofs.tex:1249]** "Mediation: +56.7%, +70.4%, +77.2%, +85.3%, +88.7%" → value: 56.7%, 70.4%, 77.2%, 85.3%, 88.7%

**[file:appendix_proofs.tex:1250]** "IV: +1.4%, +22.1%, +50.1%, +66.7%, +76.4%" → value: 1.4%, 22.1%, 50.1%, 66.7%, 76.4%

**[file:appendix_proofs.tex:1251]** "M-bias: -125.3%, -43.6%, -19.6%, +6.0%, +18.5%" → value: -125.3%, -43.6%, -19.6%, 6.0%, 18.5%

**[file:appendix_proofs.tex:1256]** "At ${\geq}20\%$ gold to reach 50\% reduction" → value: 20%, 50%

**[file:appendix_proofs.tex:1270]** "Civil Comments: $K{=}2$, $n{=}7$, 0.50, 0.50, 0/7" → value: 2, 7, 0.50, 0.50, 0, 7

**[file:appendix_proofs.tex:1274]** "VAST: $K{=}3$, $n{=}8$, 0.003, 0.00, 7/8" → value: 3, 8, 0.003, 0.00, 7, 8

**[file:appendix_proofs.tex:1274]** "HuMAID: $K{=}10$, $n{=}8$, 0.045, 0.00, 7/8" → value: 10, 8, 0.045, 0.00, 7, 8

**[file:appendix_proofs.tex:1279]** "14 of 16 configurations have $\varepsilon^*_{\text{safe}}{=}0$" → value: 14, 16, 0

**[file:appendix_proofs.tex:1279]** "Two outliers (VAST: $\varepsilon^*{=}0.02$; HuMAID: $\varepsilon^*{=}0.36$)" → value: 0.02, 0.36

**[file:appendix_proofs.tex:1284]** "23 matrices $\times$ 50 seeds $\times$ 100{,}000 precomputed samples per seed" → value: 23, 50, 100000

**[file:appendix_proofs.tex:1295]** "Proportional: 0.271, 99.8%, 100%, 0.00" → value: 0.271, 99.8%, 100%, 0.00

**[file:appendix_proofs.tex:1296]** "Near-prop. ($\sigma{=}0.1$): 0.285, 99.2%, 100%, 1.06" → value: 0.1, 0.285, 99.2%, 100%, 1.06

**[file:appendix_proofs.tex:1297]** "Non-proportional: 0.240, 85.0%, 97.3%, 3.60" → value: 0.240, 85.0%, 97.3%, 3.60

**[file:appendix_proofs.tex:1298]** "Sparse: 0.296, 75.8%, 98.6%, 6.59" → value: 0.296, 75.8%, 98.6%, 6.59

**[file:appendix_proofs.tex:1308]** "VAST DeepSeek zero-shot, mean diagonal 0.734" → value: 0.734

**[file:appendix_proofs.tex:1316]** "$\beta_1$ (primary): 0.234, > 1.5, 39.7\%" → value: 0.234, 1.5, 39.7%

**[file:appendix_proofs.tex:1317]** "$\beta_2$ (secondary): 0.154, > 1.5, 60.4\%" → value: 0.154, 1.5, 60.4%

**[file:appendix_proofs.tex:1322]** "magnitude ASV rises to $\delta^*{=}0.690$---a $3{\times}$ increase" → value: 0.690, 3

**[file:appendix_proofs.tex:1329]** "median $d_{\mathrm{rel}}{=}0.160$" → value: 0.160

**[file:appendix_proofs.tex:1334]** "5 random Dirichlet confusion matrices (diagonal $\geq 0.6$), 100 MC replications per topology--matrix combination ($N{=}5{,}000$)" → value: 5, 0.6, 100, 5000

**[file:appendix_proofs.tex:1337]** "$\rho_{3,5} = 0.80$, $\rho_{3,10} = 0.84$, $\rho_{5,10} = 0.93$" → value: 0.80, 0.84, 0.93

**[file:appendix_proofs.tex:1351]** "Confounding: PPI++ 85.6 ($K{=}3$), 76.4 ($K{=}5$), 75.6 ($K{=}10$)" → value: 85.6, 3, 76.4, 5, 75.6, 10

**[file:appendix_proofs.tex:1352]** "Mediation: PPI++ 57.1 ($K{=}3$), SIMEX 59.7 ($K{=}5$), SIMEX 59.0 ($K{=}10$)" → value: 57.1, 3, 59.7, 5, 59.0, 10

**[file:appendix_proofs.tex:1353]** "Collider: SIMEX 55.4 ($K{=}3$), 63.4 ($K{=}5$), 57.3 ($K{=}10$)" → value: 55.4, 3, 63.4, 5, 57.3, 10

**[file:appendix_proofs.tex:1354]** "Exposure: SIMEX 72.5 ($K{=}3$), 65.0 ($K{=}5$), 47.3 ($K{=}10$)" → value: 72.5, 3, 65.0, 5, 47.3, 10

**[file:appendix_proofs.tex:1355]** "M-bias: SIMEX 3.2 ($K{=}3$), 47.0 ($K{=}5$), 43.7 ($K{=}10$)" → value: 3.2, 3, 47.0, 5, 43.7, 10

**[file:appendix_proofs.tex:1356]** "IV: SIMEX 30.9 ($K{=}3$), 30.4 ($K{=}5$), 27.1 ($K{=}10$)" → value: 30.9, 3, 30.4, 5, 27.1, 10

**[file:appendix_proofs.tex:1357]** "Front-door: PPI++ 82.9 ($K{=}3$), 69.0 ($K{=}5$), SIMEX 70.1 ($K{=}10$)" → value: 82.9, 3, 69.0, 5, 70.1, 10

**[file:appendix_proofs.tex:1415]** "$n_{\text{gold}} \in \{50, 100, 200, 500\}$... 200 bootstrap replicates" → value: 50, 100, 200, 500, 200

**[file:appendix_proofs.tex:1426]** "50: 50.4%, 0.991, 0.789" → value: 50, 50.4%, 0.991, 0.789

**[file:appendix_proofs.tex:1427]** "100: 82.0%, 1.000, 0.991" → value: 100, 82.0%, 1.000, 0.991

**[file:appendix_proofs.tex:1428]** "200: 85.6%, 1.000, 0.991" → value: 200, 85.6%, 1.000, 0.991

**[file:appendix_proofs.tex:1429]** "500: 88.5%, 1.000, 0.991" → value: 500, 88.5%, 1.000, 0.991

**[file:appendix_proofs.tex:1432]** "$n_{\text{gold}} \geq 100$ (82\% stability), increasing to 89\% at $n_{\text{gold}}{=}500$" → value: 100, 82%, 89%, 500

**[file:appendix_proofs.tex:1450]** "2: 7, 0\%" → value: 2, 7, 0%

**[file:appendix_proofs.tex:1451]** "3: 8, 87.5\%" → value: 3, 8, 87.5%

**[file:appendix_proofs.tex:1452]** "10: 8, 87.5\%" → value: 10, 8, 87.5%

**[file:appendix_proofs.tex:1444]** "Rule: $\det(C) < 0.014$ → sign reversal (accuracy 91.3\%, sensitivity 85.7\%, specificity 100\%)" → value: 0.014, 91.3%, 85.7%, 100%

**[file:appendix_proofs.tex:1444]** "AND rule... 95.7\% accuracy with 100\% sensitivity" → value: 95.7%, 100%

**[file:appendix_proofs.tex:1462]** "12 LLM configurations (4 models $\times$ 3 prompting strategies), 1{,}500 samples" → value: 12, 4, 3, 1500

**[file:appendix_proofs.tex:1463]** "10{,}000 bootstrap replicates ($B{=}10{,}000$)" → value: 10000

**[file:appendix_proofs.tex:1473]** "Text length: 1/12, 0.490" → value: 1, 12, 0.490

**[file:appendix_proofs.tex:1474]** "Topic: 11/12, 0.002" → value: 11, 12, 0.002

**[file:appendix_proofs.tex:1475]** "Sentiment: 10/12, 0.017" → value: 10, 12, 0.017

**[file:appendix_proofs.tex:1460]** "Confounding: 0.000, 0.000, 0.573, 0.559" → value: 0.000, 0.000, 0.573, 0.559

**[file:appendix_proofs.tex:1461]** "Mediation: 0.000, 0.000, 0.703, 0.695" → value: 0.000, 0.000, 0.703, 0.695

**[file:appendix_proofs.tex:1062]** "Collider: 0.000, 0.000, 0.060, 0.060" → value: 0.000, 0.000, 0.060, 0.060

**[file:appendix_proofs.tex:1063]** "Exposure: ---, ---, 0.577, 0.574" → value: 0.577, 0.574

**[file:appendix_proofs.tex:1064]** "M-bias: 0.000, 0.000, 0.095, 0.099" → value: 0.000, 0.000, 0.095, 0.099

**[file:appendix_proofs.tex:1065]** "Front-door: 0.000, 0.000, 0.590, 0.579" → value: 0.000, 0.000, 0.590, 0.579

**[file:appendix_proofs.tex:1066]** "IV: 0.086, 0.074, 0.086, 0.560" → value: 0.086, 0.074, 0.086, 0.560

**[file:appendix_proofs.tex:1399]** "Confounding: 23, -0.557, 0.006" → value: 23, -0.557, 0.006

**[file:appendix_proofs.tex:1400]** "Mediation: 23, -0.565, 0.005" → value: 23, -0.565, 0.005

**[file:appendix_proofs.tex:1401]** "Exposure: 23, -0.531, 0.009" → value: 23, -0.531, 0.009

**[file:appendix_proofs.tex:1402]** "Front-door: 23, -0.568, 0.005" → value: 23, -0.568, 0.005

**[file:appendix_proofs.tex:1403]** "IV: 23, -0.700, <0.001" → value: 23, -0.700

**[file:appendix_proofs.tex:1404]** "Collider: 23, +0.310, 0.150" → value: 23, 0.310, 0.150

**[file:appendix_proofs.tex:1405]** "M-bias: 23, +0.867, <0.001" → value: 23, 0.867

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0983d91-4444-416f-ba51-fd565b0964f5",
  "isSidechain": true,
  "agentId": "a20940d9e1e09d4c5",
  "requestId": "req_011CbL3CofW6eyVw6am5XQ5T",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "39104833-e230-4140-b07f-5ea752c6bfaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QxuZ34RM9Bo5dspFv8d33x",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 68989,
      "output_tokens": 16337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 500
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 16337,
          "cache_read_input_tokens": 68989,
          "cache_creation_input_tokens": 500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 500,
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
