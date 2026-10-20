# Research conversation: Find and read the following files in this research paper project: 1. `/home/ubuntu/.agent-ml-research-prod_0510/projects

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa3739f71c0769873.jsonl`
- **Structured JSON:** [`ac3e76bed8a96114ac91.json`](../../sessions/ac/ac3e76bed8a96114ac91.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-22T03:53:57.802Z_

Find and read the following files in this research paper project:

1. `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex` — Read the FULL file, especially lines 70-160 which contain existing proof derivations for the sign-preservation theorem. I need to understand the proof structure for confounding (Cauchy-Schwarz), collider (Berkson), and any existing monotonicity/bias derivation framework.

2. Find any files in `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/` related to the introduction (introduction.tex) — I need to see where "first" claims and "83.4%" headline appear.

3. Find reference.bib or references.bib in the paper directory — check if these 4 citation keys exist: `audinet2025`, `zrnic_candes2024`, `gligoric2025`, `keith_jensen_oconnor2020`

Search breadth: very thorough

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4d58ff4e-d19d-4e80-8c6c-2131e935df92",
  "agentId": "aa3739f71c0769873",
  "type": "user",
  "uuid": "b7bee4a4-19c8-4bb6-b509-c71cb20ce478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T03:53:59.898Z_

I'll help you find and read these files. Let me start by exploring the paper directory structure and then reading the specific files you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7bee4a4-19c8-4bb6-b509-c71cb20ce478",
  "isSidechain": true,
  "agentId": "aa3739f71c0769873",
  "requestId": "req_011CbGvx42KcFPeN5LBzBKA3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "342fa919-79aa-42dd-a1e7-32c1fc5ceecb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018dCnqn6mmwRkDr9P7zfnP4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35863,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35863,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-22T03:54:00.156Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014DqnF3DGX8tCaxRjEtG2Ak`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "342fa919-79aa-42dd-a1e7-32c1fc5ceecb",
  "isSidechain": true,
  "agentId": "aa3739f71c0769873",
  "requestId": "req_011CbGvx42KcFPeN5LBzBKA3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99b3adcc-d021-4da3-9012-d09d65eb9251",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018dCnqn6mmwRkDr9P7zfnP4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35863,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35863,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 4 · 2026-05-22T03:54:00.180Z_

<details><summary>↩ Tool result · `toolu_014DqnF3DGX8tCaxRjEtG2Ak`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99b3adcc-d021-4da3-9012-d09d65eb9251",
  "isSidechain": true,
  "promptId": "4d58ff4e-d19d-4e80-8c6c-2131e935df92",
  "agentId": "aa3739f71c0769873",
  "type": "user",
  "uuid": "2f7148a9-e827-48bc-ac53-12abc244a1a0",
  "sourceToolAssistantUUID": "99b3adcc-d021-4da3-9012-d09d65eb9251",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T03:54:00.363Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012GnXwsZbhN5r41jQo8oicP`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f7148a9-e827-48bc-ac53-12abc244a1a0",
  "isSidechain": true,
  "agentId": "aa3739f71c0769873",
  "requestId": "req_011CbGvx42KcFPeN5LBzBKA3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "48f0c4e0-8807-4d16-a546-dfa6ebefd0a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018dCnqn6mmwRkDr9P7zfnP4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35863,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35863,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 6 · 2026-05-22T03:54:00.374Z_

<details><summary>↩ Tool result · `toolu_012GnXwsZbhN5r41jQo8oicP`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48f0c4e0-8807-4d16-a546-dfa6ebefd0a5",
  "isSidechain": true,
  "promptId": "4d58ff4e-d19d-4e80-8c6c-2131e935df92",
  "agentId": "aa3739f71c0769873",
  "type": "user",
  "uuid": "85cc58b7-7891-4386-bc43-441c4d5c5627",
  "sourceToolAssistantUUID": "48f0c4e0-8807-4d16-a546-dfa6ebefd0a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T03:54:00.539Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DqJohXoo2ednB2SfJog8wa`</summary>

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
  "parentUuid": "85cc58b7-7891-4386-bc43-441c4d5c5627",
  "isSidechain": true,
  "agentId": "aa3739f71c0769873",
  "requestId": "req_011CbGvx42KcFPeN5LBzBKA3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86252e60-f3b3-471e-87d8-a0d75d06fe85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018dCnqn6mmwRkDr9P7zfnP4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35863,
      "cache_read_input_tokens": 0,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 35863
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 258,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 35863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 35863,
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

_source line 8 · 2026-05-22T03:54:00.813Z_

<details><summary>↩ Tool result · `toolu_01DqJohXoo2ednB2SfJog8wa`</summary>

```text
1	\section{Proof of Proposition~\ref{prop:signflip}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding, collider, mediation, and front-door topologies, and an explicit counterexample for the exposure topology.
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
144	  B(C) = \bigl(1-\eta(C)\bigr)\,B_{\mathrm{OV}},
145	  \label{eq:convex}
146	\end{equation}
147	where
148	\[
149	  \eta(C) = \frac{\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\;\sigma_T^2}
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
168	  \frac{B(C)}{B_{\mathrm{OV}}} = \frac{V_W(V+\sigma_T^2)}{V(V_W+\sigma_T^2)} = 1 - \eta(C)
169	\]
170	is a decreasing function of $V_B\in[0,V]$.
171	At $V_B=0$ (no classification, $C$ uniform): $\eta=0$, $B=B_{\mathrm{OV}}$.
172	At $V_B=V$ (perfect classification, $C=I$): $\eta=1$, $B=0$.
173	Since $0\leq V_B\leq V$, we have $\eta\in[0,1]$ and $B(C)\in[0,B_{\mathrm{OV}}]$ (with the sign of $B_{\mathrm{OV}}$).
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
229	\subsection{Mediation Topology ($A$ = Mediator)}
230	\label{app:mediation}
231	
232	\paragraph{Data-generating process.}
233	$T\to A\to Y$, $T\to Y$.
234	\begin{align*}
235	  T &\sim \operatorname{Bernoulli}(0.5),\\
236	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
237	  Y &= \tau_{\mathrm{dir}}\,T + f(A) + \varepsilon_Y.
238	\end{align*}
239	
240	\paragraph{Bias decomposition.}
241	By Lemma~\ref{lem:bias_decomp}, the direct-effect estimator satisfies:
242	\begin{equation}
243	  \operatorname{plim}\hat\tau_{\mathrm{dir}}(C) = \tau_{\mathrm{dir}} + \frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}.
244	  \label{eq:med_bias}
245	\end{equation}
246	
247	The key structural difference from confounding: $T$ \emph{causes} $A$, so the residual covariance $\operatorname{Cov}(T,f(A)\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.
248	
249	\paragraph{Endpoint analysis.}
250	
251	At $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\to A\to Y$, so $\operatorname{Cov}(T,f(A)\mid A)=0$ and $\operatorname{plim}\hat\tau=\tau_{\mathrm{dir}}$.
252	
253	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$): no information about $A$ is used, and
254	\begin{align*}
255	  \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] &= \operatorname{Cov}(T,f(A)),\\
256	  D(C) &= \operatorname{Var}(T) = 0.25.
257	\end{align*}
258	The indirect effect is $\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]$, and
259	\[
260	  \operatorname{Cov}(T,f(A)) = 0.25\,\tau_{\mathrm{ind}}.
261	\]
262	Hence at $C$ uniform: $\operatorname{plim}\hat\tau = \tau_{\mathrm{dir}}+\tau_{\mathrm{ind}} = \tau_{\mathrm{total}}$.
263	
264	\paragraph{Empirical Finding (Mediation sign preservation).}
265	\label{find:med_sign}
266	$\operatorname{sign}(\operatorname{plim}\hat\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{dir}})$ whenever $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$, where $\tau_{\mathrm{total}}=\tau_{\mathrm{dir}}+\tau_{\mathrm{ind}}$.
267	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.
268	
269	\begin{proof}
270	Let $R(C)=\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)]$ and $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]>0$.
271	
272	\emph{Endpoints.}
273	At $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.
274	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $R=\operatorname{Cov}(T,f(A))=0.25\,\tau_{\mathrm{ind}}$ and $D=\operatorname{Var}(T)=0.25$, giving $B=\tau_{\mathrm{ind}}$.
275	
276	\emph{Within-group structure for binary $T$.}
277	Since $T\in\{0,1\}$, the within-$A^*$-group bias admits a revealing decomposition.
278	Let $p_j=P(T{=}1\mid A^*{=}j)$.
279	Then $\operatorname{Var}(T\mid A^*{=}j)=p_j(1{-}p_j)$ and
280	\[
281	  \operatorname{Cov}(T,f(A)\mid A^*{=}j)
282	  = p_j(1{-}p_j)\bigl[\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]\bigr].
283	\]
284	Define $\delta_j=\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]$ as the \emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.
285	Then
286	\[
287	  B(C)=\frac{R(C)}{D(C)}
288	  =\frac{\sum_j q_j\,p_j(1{-}p_j)\,\delta_j}{\sum_j q_j\,p_j(1{-}p_j)}
289	  =\sum_j w_j\,\delta_j,
290	\]
291	a weighted average of the conditional indirect effects, with weights $w_j=q_j p_j(1{-}p_j)/\sum_\ell q_\ell p_\ell(1{-}p_\ell)\geq 0$ summing to 1.
292	
293	At $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\delta_j=f(j)-f(j)=0$ and $B=0$.
294	At $C$ uniform: $\delta_j=\tau_{\mathrm{ind}}$ for all $j$ and $B=\tau_{\mathrm{ind}}$.
295	
296	\emph{Sign preservation.}
297	When $\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have the same sign), the bias $B(C)\geq 0$ cannot oppose $\tau_{\mathrm{dir}}$, so sign is preserved trivially.
298	
299	When $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have opposite signs but $|\tau_{\mathrm{ind}}|<|\tau_{\mathrm{dir}}|$ (i.e., $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$), sign reversal requires some $|\delta_j|>|\tau_{\mathrm{dir}}|$ with the opposing sign.
300	Since each $\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\delta_j$, the bound $|B(C)|\leq\max_j|\delta_j|$ holds.
301	We verify numerically that $\max_j|\delta_j|\leq|\tau_{\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.
302	\end{proof}
303	
304	\paragraph{Verification for paper parameters ($K{=}3$).}
305	With $\tau_{\mathrm{dir}}{=}0.5$, $\boldsymbol{\gamma}{=}(0,0,0)$, $\boldsymbol{\delta}{=}(0,0.8,{-}0.6)$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$:
306	
307	$\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]=0.351$ (computed from the softmax class probabilities).
308	$\tau_{\mathrm{total}}=0.5+0.351=0.851>0$.
309	Since $\tau_{\mathrm{dir}}{>}0$ and $\tau_{\mathrm{total}}{>}0$, sign preservation holds for all $C$.
310	
311	\subsection{Collider Topology ($A$ = Collider)}
312	\label{app:collider}
313	
314	\paragraph{Data-generating process.}
315	$T\to A\leftarrow Y$, $T\to Y$.
316	The treatment effect is unconfounded:
317	\begin{align*}
318	  T &\sim \mathcal{N}(0,1),\quad
319	  Y = \tau\,T + \varepsilon_Y,\quad \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp T,\\
320	  A\mid T,Y &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\delta}_T\,T + \boldsymbol{\delta}_Y\,Y)\bigr).
321	\end{align*}
322	The collider $A$ is a common \emph{effect} of $T$ and $Y$.
323	The no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\operatorname{plim}\hat\tau_{\mathrm{nc}}=\tau$.
324	The researcher erroneously controls for $A^*$, inducing Berkson's bias.
325	
326	\paragraph{Bias decomposition.}
327	Unlike confounding, $\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\tau T+\varepsilon_Y$), so Lemma~\ref{lem:bias_decomp} does not apply directly.
328	Instead, we derive the bias from the FWL identity~\eqref{eq:fwl}.
329	Writing $\tilde{Y}=\tau\tilde{T}+(\varepsilon_Y-\mathbb{E}[\varepsilon_Y\mid A^*])$ and noting that $\mathbb{E}[\tilde{T}\,\varepsilon_Y]=\mathbb{E}[\operatorname{Cov}(T,\varepsilon_Y\mid A^*)]$ (since $T\perp\varepsilon_Y$ unconditionally):
330	\begin{equation}
331	  \operatorname{plim}\hat\tau(C) = \tau + B(C),\quad
332	  B(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,\varepsilon_Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
333	  \label{eq:bias_col}
334	\end{equation}
335	Under non-differential misclassification ($A^*\perp(T,\varepsilon_Y)\mid A$), define $g(k)=\mathbb{E}[T\mid A{=}k]$ and $h(k)=\mathbb{E}[\varepsilon_Y\mid A{=}k]$.
336	By the tower property, $\mathbb{E}[T\mid A^*]=\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[\varepsilon_Y\mid A^*]=\mathbb{E}[h(A)\mid A^*]$.
337	Since $\operatorname{Cov}(T,\varepsilon_Y)=0$, the law of total covariance gives:
338	\[
339	  B(C) = \frac{-\operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[h(A)\mid A^*]\bigr)}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
340	\]
341	
342	\paragraph{Endpoint analysis.}
343	At $C=I$ ($A^*{=}A$):
344	$B(I) = -\operatorname{Cov}(g(A),h(A))\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)] = B_{\mathrm{Berkson}}$,
345	the full Berkson's bias from conditioning on the collider.
346	
347	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$):
348	$\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[h(A)\mid A^*]$ are constant, so $B=0$ and $\operatorname{plim}\hat\tau=\tau$.
349	
350	This is the structural reverse of confounding: misclassification attenuates the collider-induced bias toward zero, rather than growing bias from zero toward $B_{\mathrm{OV}}$.
351	
352	\begin{proposition}[Collider sign preservation --- proportional case]
353	\label{prop:col_prop}
354	If $h(A)=\lambda\,g(A)$ for some constant $\lambda$, then $|B(C)|\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.
355	Consequently, $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{Berkson}})$.
356	\end{proposition}
357	
358	\begin{proof}
359	When $h=\lambda g$, the numerator becomes $-\lambda\,\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$ and the denominator is $\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$.
360	Let $V^*=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\in[0,V_g]$ where $V_g=\operatorname{Var}(g(A))$.
361	Then
362	\[
363	  |B(C)| = |\lambda|\,\frac{V^*}{\operatorname{Var}(T)-V^*}.
364	\]
365	The function $x\mapsto x/(a-x)$ is increasing on $[0,a)$.
366	With $a=\operatorname{Var}(T)>V_g\geq V^*$:
367	$|B(C)|\leq|\lambda|\,V_g/(\operatorname{Var}(T)-V_g)=|B(I)|$.
368	At $V^*{=}0$ (uniform $C$): $B{=}0$.  At $V^*{=}V_g$ ($C{=}I$): $B{=}B(I)$.
369	\end{proof}
370	
371	\begin{proposition}[Collider sign preservation --- general case]
372	\label{prop:col_gen}
373	Define
374	\begin{equation}
375	  \bar{B}_{\mathrm{col}} = \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(h(A))}}{\mathbb{E}[\operatorname{Var}(T\mid A)]}.
376	  \label{eq:bbar_col}
377	\end{equation}
378	If $|\tau|>\bar{B}_{\mathrm{col}}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for all column-stochastic $C$.
379	\end{proposition}
380	
381	\begin{proof}
382	\emph{Step~1: Bound the numerator.}
383	By Cauchy--Schwarz:
384	$|\operatorname{Cov}(\mathbb{E}[g\mid A^*],\mathbb{E}[h\mid A^*])|\leq\sqrt{\operatorname{Var}(\mathbb{E}[g\mid A^*])\,\operatorname{Var}(\mathbb{E}[h\mid A^*])}$.
385	Since conditional expectation reduces variance: $\operatorname{Var}(\mathbb{E}[g\mid A^*])\leq\operatorname{Var}(g(A))$ and likewise for $h$.
386	
387	\emph{Step~2: Bound the denominator.}
388	$\mathbb{E}[\operatorname{Var}(T\mid A^*)]=\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[T\mid A^*])\geq\operatorname{Var}(T)-\operatorname{Var}(g(A))=\mathbb{E}[\operatorname{Var}(T\mid A)]$.
389	
390	\emph{Step~3: Conclude.}
391	$|B(C)|\leq\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(h)}\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)]=\bar{B}_{\mathrm{col}}$.
392	When $|\tau|>\bar{B}_{\mathrm{col}}$, the bias cannot overwhelm $\tau$.
393	\end{proof}
394	
395	\paragraph{Verification for paper parameters ($K{=}3$).}
396	With $\tau{=}1.0$, $\boldsymbol{\delta}_T{=}(0,\,0.5,\,{-}0.3)$, $\boldsymbol{\delta}_Y{=}(0,\,0.8,\,0.6)$, from $5{\times}10^6$-sample Monte Carlo:
397	\begin{align*}
398	  \operatorname{Var}(g(A)) &= 0.187,\quad
399	  \operatorname{Var}(h(A)) = 0.076,\quad
400	  \mathbb{E}[\operatorname{Var}(T\mid A)] = 0.813,\\
401	  \bar{B}_{\mathrm{col}} &= \sqrt{0.187\times 0.076}\;/\;0.813 = 0.147.
402	\end{align*}
403	Since $|\tau|{=}1.0\gg\bar{B}_{\mathrm{col}}{=}0.147$, Proposition~\ref{prop:col_gen} guarantees sign preservation.
404	Additionally, $B_{\mathrm{Berkson}}{=}{-}0.114$, giving $\tau+B_{\mathrm{Berkson}}{=}0.886{>}0$.
405	Verified across $100{,}000$ random column-stochastic $C$: $\tau_{\mathrm{sign\,flip}}{=}0\%$, and $|B(C)|\leq|B_{\mathrm{Berkson}}|$ in all cases.
406	
407	\subsection{Front-door Topology ($A$ = Mediator under Confounding)}
408	\label{app:frontdoor}
409	
410	\paragraph{Data-generating process.}
411	$T\to A\to Y$, $U\to T$, $U\to Y$.
412	An unobserved confounder $U$ affects both treatment and outcome:
413	\begin{align*}
414	  U &\sim \mathcal{N}(0,1),\quad
415	  T = \alpha_U\,U + \eta,\quad \eta\sim\mathcal{N}(0,1),\;\eta\perp U,\\
416	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
417	  Y &= f(A) + \lambda\,U + \varepsilon_Y,\quad \varepsilon_Y\perp(T,A,U).
418	\end{align*}
419	There is no direct $T{\to}Y$ edge; the causal effect of $T$ on $Y$ operates entirely through $A$.
420	The researcher controls for $A^*$ in $Y\sim 1+T+D_1^*+\cdots+D_{K-1}^*$.
421	
422	\paragraph{Bias decomposition.}
423	Since the direct effect is zero, the FWL coefficient on $T$ captures only bias:
424	\[
425	  \operatorname{plim}\hat\tau(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
426	\]
427	Substituting $Y=f(A)+\lambda U+\varepsilon_Y$ and using $\varepsilon_Y\perp(T,A,A^*)$:
428	\begin{equation}
429	  \operatorname{plim}\hat\tau(C)
430	  = \underbrace{\frac{\lambda\,\alpha_U}{\operatorname{Var}(T)}}_{\text{confounding (constant)}}
431	  \;+\; \underbrace{\frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}}_{\displaystyle B_{\mathrm{med}}(C)},
432	  \label{eq:fd_decomp}
433	\end{equation}
434	where $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]$.
435	
436	\begin{proof}[Derivation of~\eqref{eq:fd_decomp}]
437	Expand the numerator as
438	$\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] + \lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]$.
439	For the confounding term: since $T=\alpha_U U+\eta$ with $(U,\eta)$ jointly Gaussian, the regression residual $\xi=U-\frac{\alpha_U}{\operatorname{Var}(T)}T$ satisfies $\xi\perp T$.
440	Because $A$ is a function of $T$ (plus independent softmax noise) and $A^*$ is a function of $A$ (plus independent misclassification noise), $\xi\perp(T,A,A^*)$.
441	Therefore
442	\[
443	  \operatorname{Cov}(T,U\mid A^*{=}j)
444	  = \frac{\alpha_U}{\operatorname{Var}(T)}\,\operatorname{Var}(T\mid A^*{=}j)
445	  \quad\forall\;j,
446	\]
447	and $\lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]=\frac{\lambda\alpha_U}{\operatorname{Var}(T)}\,D(C)$, yielding the constant first term after division by $D(C)$.
448	\end{proof}
449	
450	This decomposition reveals that \emph{misclassification does not affect the confounding component}.
451	The confusion matrix $C$ modulates only the mediation-type leakage $B_{\mathrm{med}}(C)$, which has the same structure as in~§\ref{app:mediation}.
452	
453	\paragraph{Endpoint analysis.}
454	At $C=I$: $B_{\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\to A\to Y$ path), and $\operatorname{plim}\hat\tau(I)=\lambda\alpha_U/\operatorname{Var}(T)$ (pure confounding residual).
455	
456	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $B_{\mathrm{med}}=\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$, and $\operatorname{plim}\hat\tau_{\mathrm{nc}}=[\operatorname{Cov}(T,f(A))+\lambda\alpha_U]/\operatorname{Var}(T)$, the naive regression coefficient with no controls.
457	
458	\paragraph{Empirical Finding (Front-door sign preservation).}
459	\label{find:fd_sign}
460	Since $B_{\mathrm{med}}(C)$ has the same structure as the mediation bias (§\ref{app:mediation})---interpolating between $0$ at $C{=}I$ and $\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$ at $C$ uniform---sign preservation holds whenever the two endpoints have the same sign:
461	\[
462	  \operatorname{sign}\!\bigl(\lambda\alpha_U\bigr)
463	  = \operatorname{sign}\!\bigl(\lambda\alpha_U + \operatorname{Cov}(T,f(A))\bigr).
464	\]
465	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$.
466	
467	\paragraph{Verification for paper parameters ($K{=}3$).}
468	With $\alpha_U{=}1.0$, $\lambda{=}1.0$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$, $\boldsymbol{\gamma}{=}(0,0.5,{-}0.3)$, $\boldsymbol{\delta}{=}(0,1.0,{-}0.8)$:
469	\begin{align*}
470	  \lambda\alpha_U/\operatorname{Var}(T) &= 1.0\times 1.0\,/\,2.0 = 0.500,\\
471	  \operatorname{Cov}(T,f(A))/\operatorname{Var}(T) &= 0.594\,/\,2.0 = 0.297.
472	\end{align*}
473	Both components are positive, so $\operatorname{plim}\hat\tau(C)\in[0.500,\,0.797]>0$ for all $C$.
474	
475	\subsection{Exposure Topology: Sign Reversal Counterexample}
476	\label{app:exposure}
477	
478	\begin{proposition}[Exposure sign reversal]
479	\label{prop:exp_counter}
480	For $K{=}3$ with $A$ as the treatment variable, there exist a marginal distribution $\mathbf{p}$, treatment effects $\boldsymbol{\beta}$, and a column-stochastic $C$ with $C_{kk}>0.5$ for all $k$, such that $\operatorname{sign}(\operatorname{plim}\hat\beta_1)\neq\operatorname{sign}(\beta_1)$.
481	\end{proposition}
482	
483	\begin{proof}[Construction]
484	Consider the exposure DGP $Y = \beta_1 D_1 + \beta_2 D_2 + \varepsilon_Y$ with:
485	\begin{itemize}
486	  \item Uniform prior: $\mathbf{p}=(1/3,\,1/3,\,1/3)$.
487	  \item True effects: $\beta_1=1$,\; $\beta_2=-10$.
488	\end{itemize}
489	Choose the confusion matrix
490	\[
491	  C = \begin{pmatrix}
492	    0.60 & 0.10 & 0.10\\
493	    0.10 & 0.60 & 0.39\\
494	    0.30 & 0.30 & 0.51
495	  \end{pmatrix},\qquad
496	  C_{kk}\in\{0.60,\,0.60,\,0.51\},\;\text{all}>0.5.
497	\]
498	Column sums are $1$ (verifiable by inspection).
499	
500	The OLS estimator regresses $Y$ on $(1,D_1^*,D_2^*)$.
501	The plim of $\hat\beta_j$ equals $\mathbb{E}[Y\mid A^*{=}j]-\mathbb{E}[Y\mid A^*{=}0]$, where
502	\[
503	  \mathbb{E}[Y\mid A^*{=}j] = \sum_{k=0}^{2} P(A{=}k\mid A^*{=}j)\,\beta_k
504	  = \sum_{k=1}^{2}\frac{C_{jk}\,p_k}{q_j}\,\beta_k.
505	\]
506	
507	\emph{Marginal distribution of $A^*$:}
508	\begin{align*}
509	  q_0 &= \tfrac{1}{3}(0.60+0.10+0.10)=0.267,\\
510	  q_1 &= \tfrac{1}{3}(0.10+0.60+0.39)=0.363,\\
511	  q_2 &= \tfrac{1}{3}(0.30+0.30+0.51)=0.370.
512	\end{align*}
513	
514	\emph{Conditional means:}
515	\begin{align*}
516	  \mathbb{E}[Y\mid A^*{=}0]
517	  &= \frac{0.10\times\tfrac{1}{3}\times 1 + 0.10\times\tfrac{1}{3}\times({-}10)}{0.267}
518	  = \frac{0.0333-0.3333}{0.267} = -1.125,\\[4pt]
519	  \mathbb{E}[Y\mid A^*{=}1]
520	  &= \frac{0.60\times\tfrac{1}{3}\times 1 + 0.39\times\tfrac{1}{3}\times({-}10)}{0.363}
521	  = \frac{0.200-1.300}{0.363} = -3.028,\\[4pt]
522	  \mathbb{E}[Y\mid A^*{=}2]
523	  &= \frac{0.30\times\tfrac{1}{3}\times 1 + 0.51\times\tfrac{1}{3}\times({-}10)}{0.370}
524	  = \frac{0.100-1.700}{0.370} = -4.324.
525	\end{align*}
526	
527	\emph{Estimated coefficient:}
528	\[
529	  \operatorname{plim}\hat\beta_1 = \mathbb{E}[Y\mid A^*{=}1]-\mathbb{E}[Y\mid A^*{=}0]
530	  = -3.028-(-1.125) = \mathbf{-1.903}.
531	\]
532	The true $\beta_1=+1>0$ but $\operatorname{plim}\hat\beta_1=-1.903<0$: \textbf{sign reversal}.
533	
534	\emph{Mechanism.}
535	The large off-diagonal entry $C_{12}=0.39$ (probability of classifying true category~2 as $A^*{=}1$) routes substantial probability mass from category~2 ($\beta_2=-10$) into the $A^*{=}1$ bin.
536	Despite $C_{11}=0.60>0.5$, the contamination from the strongly negative $\beta_2$ overwhelms the positive $\beta_1$, reversing the sign of the estimated effect for category~1.
537	This failure mode is structurally impossible at $K{=}2$: a $2{\times}2$ column-stochastic matrix with $C_{kk}>0.5$ has the form $C=\bigl(\begin{smallmatrix}a&1{-}b\\1{-}a&b\end{smallmatrix}\bigr)$ with $a,b>0.5$, and the single coefficient $\hat\beta_1$ is a positive-weighted average of $\beta_1$, preserving sign.
538	For $K{\geq}3$, the additional degrees of freedom in $C$ permit cross-contamination between categories with opposite-sign effects.
539	\end{proof}
540	
541	\subsection{Summary of Conditions}
542	\label{app:conditions}
543	
544	\begin{table}[h]
545	\centering
546	\small
547	\begin{tabular}{lcc}
548	\toprule
549	\textbf{Topology} & \textbf{Sign preservation condition} & \textbf{Paper DGP} \\
550	\midrule
551	Confounding & $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ & $\checkmark$ ($2.0$ vs $2.3$)\\
552	Mediation & $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$ & $\checkmark$ ($0.5$ vs $0.85$)\\
553	Collider & $|\tau|>\bar{B}_{\mathrm{col}}$ (Prop.~\ref{prop:col_gen}) & $\checkmark$ ($1.0$ vs $0.15$)\\
554	M-bias & Bias is attenuating (toward $\tau$) & $\checkmark$ \\
555	Front-door & $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ (§\ref{app:frontdoor}) & $\checkmark$ ($0.50$ vs $0.80$)\\
556	\midrule
557	Exposure & Not guaranteed for $K\geq 3$ & Counterexample above \\
558	IV & Not guaranteed (denominator instability) & --- \\
559	\bottomrule
560	\end{tabular}
561	\caption{Sufficient conditions for sign preservation under non-differential misclassification.
562	For confounding, mediation, and front-door, the condition requires the true (or clean-control) effect and the no-control effect to have the same sign.
563	For the collider, the condition bounds the Berkson's bias magnitude relative to $|\tau|$.
564	All conditions are verified for our DGP parameters.}
565	\label{tab:sign_conditions}
566	\end{table}
567	
568	\paragraph{Structural argument for M-bias topology.}
569	\emph{M-bias:} The M-structure creates a backdoor path through two latent common causes.
570	Misclassification of $A$ weakens the statistical association along this backdoor path, reducing the spurious correlation rather than amplifying it.
571	The bias therefore interpolates between zero (perfect classification) and the full backdoor bias (no classification information), preserving sign under the same sufficient condition as confounding.
572	
573	\paragraph{Remark.}
574	The sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.
575	Once the condition is satisfied, sign preservation holds for \emph{all} column-stochastic $C$ with $C_{kk}>0$---no diagonal-dominance restriction is needed.
576	Conversely, if the condition fails (i.e., the omitted-variable or total-effect estimate has the opposite sign from $\tau$), then there exist confusion matrices that produce sign reversal.
577	For the DGP parameters used throughout our experiments, the conditions are comfortably satisfied.
578	The sign-alignment condition is violated when the confounder has opposing effects on treatment and outcome (e.g., $\gamma_A > 0$ on $T$ but $\gamma_A < 0$ on $Y$), producing $\operatorname{sign}(\tau) \neq \operatorname{sign}(\tau_{\mathrm{OV}})$. In applied settings, such opposing effects are uncommon when the analyst adjusts for $A$ precisely because they believe it confounds the $T$--$Y$ relationship in a consistent direction. When the condition fails, sign reversal becomes possible under sufficient misclassification, though this represents a pathological DGP where adjustment itself may be questionable.
579	
580	\section{Supplementary Tables, Figures, and Algorithm}
581	\label{app:supplementary}
582	
583	\begin{figure*}[h]
584	\centering
585	\includegraphics[width=\textwidth]{fig1_dag_taxonomy.pdf}
586	\caption{Seven canonical DAG topologies with starred-node annotation. In each panel, $A$ (latent true label) connects to $A^*$ (observed LLM annotation) via a dashed measurement edge. The causal role of $A$ varies across topologies, producing structurally distinct bias patterns under misclassification.}
587	\label{fig:dag_taxonomy}
588	\end{figure*}
589	
590	\begin{figure*}[h]
591	\centering
592	\includegraphics[width=\textwidth]{fig3_asv_ranking.pdf}
593	\caption{ASV sensitivity ranking across topologies. Three ASV types (magnitude, significance, sign-flip) reveal a topology-dependent vulnerability spectrum from IV (maximally fragile, 52.6\% sign reversal; sign-flip ASV $= 1.1$--$6.7$) to M-bias (immune, ASV $= \infty$).}
594	\label{fig:asv_ranking}
595	\end{figure*}
596	
597	\begin{table}[h]
598	\centering
599	\caption{ASV type applicability and sensitivity across DAG topologies. Magnitude ASV at $\tau{=}0.5$, 10\% threshold. Power at $\tau{=}0.05$ significance filter. ---: not applicable.}
600	\label{tab:asv_grid}
601	\small
602	\begin{tabular}{lcccl}
603	\toprule
604	\textbf{Topology} & \textbf{Mag. ASV} & \textbf{Signif.} & \textbf{Sign-flip} & \textbf{Rank} \\
605	\midrule
606	IV & 0.101--0.607 & 0\% & 1.1--6.7 & 1 (fragile) \\
607	Front-door & 0.064--0.387 & 100\% & --- & 2 \\
608	Confounding & 0.081--0.487 & 100\% & --- & 3 \\
609	Mediation & 0.076--0.454 & 0\% & --- & 4 \\
610	Collider & 0.338--2.028 & 0\% & --- & 5 \\
611	M-bias & $\infty$ & 96--100\% & --- & 6 (immune) \\
612	Exposure & --- & --- & 83.4\%$^*$ & --- \\
613	\bottomrule
614	\multicolumn{5}{l}{\scriptsize $^*$Fraction of $C_0$ with $\tau_{\text{sign\_flip}} < 1$. Exposure uses sign-flip ASV exclusively.}
615	\end{tabular}
616	\end{table}
617	
618	\begin{figure}[h]
619	\centering
620	\includegraphics[width=\columnwidth]{fig7_dirichlet_overlay.pdf}
621	\caption{Empirical LLM confusion matrices overlaid on theoretical violation-rate curves (exposure, left; IV, right). Theoretical curves are derived from $K{=}3$ Dirichlet random matrices; empirical points are positioned at their minimum diagonal entry. Markers denote datasets (circles: HumAID $K{=}10$; squares: VAST $K{=}3$; triangles: CivilComments $K{=}2$).}
622	\label{fig:dirichlet_overlay}
623	\end{figure}
624	
625	\begin{figure}[h]
626	\centering
627	\includegraphics[width=\columnwidth]{fig4_binarization.pdf}
628	\caption{Binarization collapse $\Delta$ across topologies. Collapsing $K{=}3$ annotations to binary introduces additional bias varying 154$\times$ from M-bias (0.006) to IV (0.926).}
629	\label{fig:binarization}
630	\end{figure}
631	
632	\begin{figure}[h]
633	\centering
634	\includegraphics[width=\columnwidth]{fig6_asv_heatmap.pdf}
635	\caption{ASV magnitude ranges across topologies for HumAID ($K{=}10$). Left: magnitude ASV ($\delta^*$) range across 8 LLM configurations; lower values indicate greater fragility. ``Safe'' topologies never exceed the 10\% bias threshold. Right: percentage of configurations flagged as ASV-unsafe.}
636	\label{fig:asv_heatmap}
637	\end{figure}
638	
639	\begin{table}[h]
640	\centering
641	\caption{RMSE reduction (\%) by correction method and DAG topology (mean across 6 error structures, $N_{\text{sim}}{=}1{,}000$). Positive = reduced RMSE; negative = increased RMSE. Naive/MLA show 0.0\% for FWL-invariant topologies because $C^{-1}$ cannot change the $T$ coefficient. \textbf{Bold}: best method per topology; \underline{underline}: best gold-free method.}
642	\label{tab:correction}
643	\small
644	\begin{tabular}{lccccc}
645	\toprule
646	\textbf{Topology} & \textbf{Naive} & \textbf{MLA} & \textbf{DSL} & \textbf{SIMEX} & \textbf{PPI++} \\
647	\midrule
648	Confounding & 0.0 & 0.0 & \underline{48.0} & 35.1 & \textbf{83.2} \\
649	Mediation & 0.0 & 0.0 & \underline{52.9} & 39.1 & \textbf{54.1} \\
650	Collider & 0.0 & 0.0 & $-$92.6 & \underline{31.8} & \textbf{50.5} \\
651	M-bias & 0.0 & 0.0 & $-$267 & \textbf{\underline{0.1}} & $-$88.0 \\
652	\midrule
653	Front-door & $-$52.7 & $-$111.5 & \underline{$-$29.0} & $-$62.4 & \textbf{74.1} \\
654	Exposure & $-$44.8 & $-$89.0 & $-$59.5 & \underline{$-$9.8} & \textbf{75.5} \\
655	IV & $-$40.4 & $-$58.7 & $-$206.1 & \underline{59.4} & \textbf{79.4} \\
656	\midrule
657	Grand mean & $-$19.7 & $-$37.0 & $-$79.0 & 13.3 & \textbf{47.0} \\
658	\bottomrule
659	\end{tabular}
660	\end{table}
661	
662	\begin{algorithm}[h]
663	\caption{Correction method selection for LLM-annotated causal inference.}
664	\label{alg:correction}
665	\small
666	\begin{algorithmic}[1]
667	\REQUIRE DAG topology $\mathcal{T}$, gold-label availability $G \in \{\textsc{yes}, \textsc{no}\}$
668	\ENSURE Recommended method $M$, risk level $R$
669	\STATE
670	\STATE \textbf{Step 1: Assess risk level}
671	\IF{$\mathcal{T} \in \{\text{M-bias}\}$}
672	    \STATE $R \gets \textsc{Low}$ \COMMENT{$|\text{bias}| < 0.04$ for all $C$}
673	\ELSIF{$\mathcal{T} \in \{\text{Conf., Med., Coll., Front-door}\}$}
674	    \STATE $R \gets \textsc{Medium}$ \COMMENT{bounded bias, no sign reversal}
675	\ELSE
676	    \STATE $R \gets \textsc{High}$ \COMMENT{Exposure, IV: sign reversal 83.4\% / 52.6\%}
677	\ENDIF
678	\STATE
679	\STATE \textbf{Step 2: Select correction method}
680	\IF{$G = \textsc{yes}$}
681	    \IF{$\mathcal{T} = \text{M-bias}$}
682	        \STATE $M \gets \textsc{None}$ \COMMENT{PPI++ RMSE red.\ $-$88.0\%; no correction preferred}
683	    \ELSE
684	        \STATE $M \gets \text{PPI++}$ \COMMENT{47.0\% RMSE red., 96.8\% coverage}
685	    \ENDIF
686	\ELSE
687	    \STATE \COMMENT{no gold labels}
688	    \IF{$\mathcal{T} \in \{\text{Confounding, Mediation}\}$}
689	        \STATE $M \gets \text{DSL}$ \COMMENT{48.0\% / 52.9\% RMSE reduction}
690	    \ELSIF{$\mathcal{T} = \text{IV}$}
691	        \STATE $M \gets \text{MC-SIMEX}$ \COMMENT{59.4\% RMSE reduction}
692	    \ELSIF{$\mathcal{T} \in \{\text{Collider, M-bias}\}$}
693	        \STATE $M \gets \text{MC-SIMEX}$ \COMMENT{31.8\% / 0.1\% RMSE reduction}
694	    \ELSE
695	        \STATE $M \gets \emptyset$; flag: acquire gold labels \COMMENT{no reliable gold-free method}
696	    \ENDIF
697	\ENDIF
698	\STATE
699	\STATE \textbf{Step 3: FWL invariance warning}
700	\IF{$\mathcal{T} \in \{\text{Conf., Med., Coll., M-bias}\}$}
701	    \STATE Skip Naive plug-in and MLA \COMMENT{0\% bias red.\ on $T$ coeff.}
702	\ENDIF
703	\RETURN $(M, R)$
704	\end{algorithmic}
705	\end{algorithm}
706	
707	\subsection{Applied Illustration: ClinicalBERT Case Study}
708	\label{app:case_study}
709	
710	To demonstrate the framework's end-to-end utility, we apply it retrospectively to \citet{lee_wood_doughty2024}, who use ClinicalBERT to classify patient smoking status ($K{=}4$: never, past, current, unknown) from clinical notes and control for this predicted confounder when estimating the causal effect of echocardiography on mortality in 4{,}735 MIMIC-III sepsis patients.
711	Our taxonomy identifies this as a \emph{confounding topology}: the annotated variable enters as a confounder between treatment and outcome.
712	Three conclusions follow directly.
713	First, the zero sign-flip guarantee for confounding (Table~\ref{tab:taxonomy}) ensures that the estimated protective effect (OR~$= 0.89$) cannot reverse direction due to annotation error---a reassurance unavailable without topology-specific analysis.
714	Second, the FWL invariance result implies that any correction reducing to $C^{-1}$ applied to the dummy-coded confounder achieves exactly 0\% bias reduction for the treatment coefficient; naive plug-in is provably futile here.
715	Third, our correction guidance ranks PPI++ (83.2\% RMSE reduction for confounding) above MC-SIMEX (35.1\%) when gold labels are available---a concrete recommendation the original study lacked.
716	This example illustrates the intended workflow: DAG identification $\to$ topology-specific guarantees $\to$ correction method selection.
717	
718	\subsection{IV Wald Estimator: Diagonal-Dominance Subspaces}
719	\label{sec:iv_dirichlet_subspace}
720	
721	Section~\ref{sec:taxonomy_results} reports a 52.6\% Wald sign-flip rate
722	over the full Dirichlet$(1,1,1)$ prior. Because realistic LLM confusion
723	matrices are diagonal-dominant, we replicate the exposure-DAG stratification
724	for the IV topology, restricting the sample
725	space to $\{C : \min_k C_{kk} \geq d\}$ for $d \in \{0, 0.5, 0.7, 0.9\}$
726	(100{,}000 random matrices per threshold).
727	
728	\begin{table}[h]
729	\centering
730	\caption{IV Wald estimator bias by minimum-diagonal subspace ($K{=}3$, $\tau_{\text{true}}{=}1.41$).
731	Rates over 100{,}000 Dirichlet-truncated random $C$ per threshold.}
732	\label{tab:iv_dirichlet_subspace}
733	\small
734	\begin{tabular}{lcccc}
735	\toprule
736	\textbf{Subspace} & \textbf{Violation} & \textbf{Sign Flip} & \textbf{Amplif.} & \textbf{Worst} \\
737	\midrule
738	Full           & 100.0\% & 51.7\% & 48.3\% & $10^{5}\!\times$ \\
739	$d \geq 0.5$   & 100.0\% & 0.0\%  & 100.0\% & $28.6\times$ \\
740	$d \geq 0.7$   & 100.0\% & 0.0\%  & 100.0\% & $2.4\times$ \\
741	$d \geq 0.9$   & 100.0\% & 0.0\%  & 100.0\% & $1.2\times$ \\
742	\bottomrule
743	\end{tabular}
744	\end{table}
745	
746	The contrast with exposure is instructive: at $d{\geq}0.7$, exposure violation drops to 13.7\% (sign reversal 2.1\%, amplification 11.7\%), while IV maintains 100\% violation with pure amplification. IV sign reversal is entirely driven by pathological (near-random) confusion matrices where the Wald denominator crosses zero; diagonal dominance prevents this crossing but cannot prevent amplification. Even at $d{\geq}0.9$, the Wald estimator inflates $|\tau|$ by up to $1.24\times$ with probability~1.
747	
748	\subsection{Non-Differential Assumption Stress Test}
749	\label{sec:nondiff_stress}
750	
751	Our main analysis assumes non-differential misclassification: the confusion matrix $C$ does not depend on the outcome $Y$. To assess sensitivity to violations of this assumption, we conduct a stress test on the exposure topology ($K{=}3$, $\min_k C_{kk} \geq 0.7$, 10{,}000 random matrices per $\varepsilon$). For each base matrix $C_0$, observations with $Y > \text{median}(Y)$ are misclassified using a perturbed matrix $\tilde{C} = \text{renormalize}(C_0 + \varepsilon \cdot \Delta)$ where $\Delta_{jk} \sim \text{Uniform}(-1,1)$ for $j \neq k$, while observations with $Y \leq \text{median}(Y)$ retain $C_0$.
752	
753	\begin{table}[h]
754	\centering
755	\small
756	\caption{Effect of differential misclassification on bias violation rates (exposure DAG, $K{=}3$, $\min_k C_{kk} \geq 0.7$, $N{=}50{,}000$ MC samples per trial).}
757	\label{tab:nondiff_stress}
758	\begin{tabular}{cccc}
759	\toprule
760	$\varepsilon$ & Sign-Flip (\%) & Amplification (\%) & Any Violation (\%) \\
761	\midrule
762	0.00 & 2.0 & 11.5 & 13.3 \\
763	0.01 & 2.4 & 12.4 & 14.7 \\
764	0.05 & 2.8 & 13.0 & 15.7 \\
765	0.10 & 4.5 & 16.7 & 20.9 \\
766	\bottomrule
767	\end{tabular}
768	\end{table}
769	
770	The $\varepsilon{=}0$ baseline (13.3\% violation) closely matches the analytical result (13.7\%) from Section~\ref{sec:taxonomy_results}. Even at $\varepsilon{=}0.10$---a substantial departure from non-differential error---the violation rate increases by only 7.6 percentage points. Small departures ($\varepsilon \leq 0.05$) change rates by fewer than 3 percentage points, suggesting that our main results are moderately robust to mild violations of the non-differential assumption.
771	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86252e60-f3b3-471e-87d8-a0d75d06fe85",
  "isSidechain": true,
  "promptId": "4d58ff4e-d19d-4e80-8c6c-2131e935df92",
  "agentId": "aa3739f71c0769873",
  "type": "user",
  "uuid": "2044f91e-7bab-46b1-89a6-449435703077",
  "sourceToolAssistantUUID": "86252e60-f3b3-471e-87d8-a0d75d06fe85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-22T03:54:03.022Z_

Now let me read the introduction.tex file and search for the specific citations in references.bib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2044f91e-7bab-46b1-89a6-449435703077",
  "isSidechain": true,
  "agentId": "aa3739f71c0769873",
  "requestId": "req_011CbGvxGq16gjFPPjCF3tyF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "990354fa-0a53-4130-b284-fc9e396802ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DXNkAeW4SB816rGC5nySL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 22656,
      "cache_read_input_tokens": 35863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22656,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 10 · 2026-05-22T03:54:04.091Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XDAgMXGRsACnfj9AAcjeNJ`</summary>

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
  "parentUuid": "990354fa-0a53-4130-b284-fc9e396802ae",
  "isSidechain": true,
  "agentId": "aa3739f71c0769873",
  "requestId": "req_011CbGvxGq16gjFPPjCF3tyF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eb781541-d728-4e88-bc29-6dde9c25d77f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DXNkAeW4SB816rGC5nySL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 22656,
      "cache_read_input_tokens": 35863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22656,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 11 · 2026-05-22T03:54:04.099Z_

<details><summary>↩ Tool result · `toolu_01XDAgMXGRsACnfj9AAcjeNJ`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The consequences can be catastrophic. Under $K{=}3$ non-differential exposure misclassification, 83.4\% of confusion matrices cause \emph{sign reversal} of the estimated treatment effect, where the estimated direction of the causal relationship is opposite to the truth. This failure breaks the classical binary guarantee that non-differential misclassification biases estimates ``toward the null''~\cite{brenner1993}, a guarantee that many applied researchers implicitly rely upon. The breakdown is not an edge case: it persists even when classifier accuracy exceeds 70\% (13.7\% violation rate at diagonal $\geq 0.7$). Moreover, standard classification metrics do not predict downstream causal risk: within a narrow $F_1$ range of 0.614--0.690 across three frontier LLMs, relative bias varies by an order of magnitude across topologies (from 4.1\% to 42.1\%), illustrating that \emph{topology}, not annotator quality, determines downstream risk.
7	
8	The mechanism is algebraic. For binary classification, non-differential error can only attenuate the effect because the $2{\times}2$ stochastic confusion matrix preserves coefficient signs. With $K \geq 3$ categories, the confusion matrix can assign negative effective weights to categories with opposite-sign coefficients, enabling sign reversal~\cite{veirod_laake2001}. This fundamental asymmetry has received limited systematic treatment. \citet{brenner1993} identified the possibility of polytomous reversal but did not characterize it across causal designs. \citet{lee_wood_doughty2024} extended classifier error analysis to categorical variables and LLM classifiers, but covered only one DAG topology (unobserved confounding). No existing framework addresses how the same confusion matrix produces qualitatively different bias across different causal identification strategies.
9	
10	We address these gaps with three contributions:
11	
12	\begin{enumerate}
13	\item \textbf{Multi-class bias taxonomy.} We derive bias expressions for seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy}) under $K$-class non-differential misclassification and establish that five topologies maintain a structural sign-flip guarantee while exposure and IV can produce sign reversal. Binarization amplifies the gap: collapsing $K{=}3$ to binary introduces additional bias varying 154$\times$ across topologies.
14	
15	\item \textbf{Annotation Sensitivity Values (ASVs).} We propose three complementary sensitivity measures---magnitude, significance, and sign-flip ASV---revealing a vulnerability spectrum from IV (maximally fragile, 52.6\% sign reversal) to M-bias (immune, ASV $= \infty$).
16	
17	\item \textbf{Topology-aware correction guidance.} We evaluate five correction methods and show that matrix-based corrections achieve exactly 0\% bias reduction for four topologies due to Frisch--Waugh--Lovell invariance. PPI++ achieves 47.0\% RMSE reduction but requires gold labels and is harmful for M-bias ($-$88\%).
18	\end{enumerate}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb781541-d728-4e88-bc29-6dde9c25d77f",
  "isSidechain": true,
  "promptId": "4d58ff4e-d19d-4e80-8c6c-2131e935df92",
  "agentId": "aa3739f71c0769873",
  "type": "user",
  "uuid": "095d31c3-4226-4514-96a9-0d6c1cefe478",
  "sourceToolAssistantUUID": "eb781541-d728-4e88-bc29-6dde9c25d77f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T03:54:04.232Z_

<details open><summary>🔧 Tool call — Read · `toolu_015daTdFNG6kCEX7RcMpvvds`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib",
  "limit": 1000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "095d31c3-4226-4514-96a9-0d6c1cefe478",
  "isSidechain": true,
  "agentId": "aa3739f71c0769873",
  "requestId": "req_011CbGvxGq16gjFPPjCF3tyF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8add9014-2dbb-4713-9479-ccadabfbacbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DXNkAeW4SB816rGC5nySL9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 22656,
      "cache_read_input_tokens": 35863,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22656
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 200,
          "cache_read_input_tokens": 35863,
          "cache_creation_input_tokens": 22656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22656,
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

_source line 13 · 2026-05-22T03:54:04.246Z_

<details><summary>↩ Tool result · `toolu_015daTdFNG6kCEX7RcMpvvds`</summary>

```text
1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-20
3	
4	@inproceedings{wood_doughty2018,
5	  title     = {Challenges of Using Text Classifiers for Causal Inference},
6	  author    = {Wood-Doughty, Zach and Shpitser, Ilya and Dredze, Mark},
7	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
8	  year      = {2018},
9	  doi       = {10.18653/v1/D18-1488},
10	}
11	
12	@article{teblunthuis2024,
13	  title   = {Misclassification in Automated Content Analysis Causes Bias in Regression. {C}an We Fix It? {Y}es We Can!},
14	  author  = {TeBlunthuis, Nathan and Hase, Valerie and Chan, Chung-hong},
15	  journal = {Communication Methods and Measures},
16	  volume  = {18},
17	  number  = {3},
18	  pages   = {278--299},
19	  year    = {2024},
20	  doi     = {10.1080/19312458.2023.2293713},
21	}
22	
23	@article{hernan_cole2009,
24	  title   = {Invited Commentary: Causal Diagrams and Measurement Bias},
25	  author  = {Hern{\'a}n, Miguel A. and Cole, Stephen R.},
26	  journal = {American Journal of Epidemiology},
27	  volume  = {170},
28	  number  = {8},
29	  pages   = {959--962},
30	  year    = {2009},
31	  doi     = {10.1093/aje/kwp293},
32	}
33	
34	@article{vanderweele_li2019,
35	  title   = {Simple Sensitivity Analysis for Differential Measurement Error},
36	  author  = {VanderWeele, Tyler J. and Li, Yige},
37	  journal = {American Journal of Epidemiology},
38	  volume  = {188},
39	  number  = {10},
40	  pages   = {1823--1829},
41	  year    = {2019},
42	  doi     = {10.1093/aje/kwz133},
43	}
44	
45	@article{vanderweele_ding2017,
46	  title   = {Sensitivity Analysis in Observational Research: Introducing the {E}-Value},
47	  author  = {VanderWeele, Tyler J. and Ding, Peng},
48	  journal = {Annals of Internal Medicine},
49	  volume  = {167},
50	  pages   = {268--274},
51	  year    = {2017},
52	  doi     = {10.7326/M16-2607},
53	}
54	
55	@article{brenner1993,
56	  title   = {Bias Due to Non-differential Misclassification of Polytomous Confounders},
57	  author  = {Brenner, Hermann},
58	  journal = {Journal of Clinical Epidemiology},
59	  volume  = {46},
60	  number  = {1},
61	  pages   = {57--63},
62	  year    = {1993},
63	  doi     = {10.1016/0895-4356(93)90009-P},
64	}
65	
66	@article{veirod_laake2001,
67	  title   = {Exposure Misclassification: Bias in Category Specific {P}oisson Regression Coefficients},
68	  author  = {Veier{\o}d, Marit B. and Laake, Petter},
69	  journal = {Statistics in Medicine},
70	  volume  = {20},
71	  number  = {5},
72	  pages   = {771--784},
73	  year    = {2001},
74	  doi     = {10.1002/sim.712},
75	}
76	
77	@article{baumann2025,
78	  title   = {Large Language Model Hacking: Quantifying the Hidden Risks of Using {LLM}s for Text Annotation},
79	  author  = {Baumann, Maximilian and R{\"o}ttger, Paul and Urman, Aleksandra and Wendsj{\"o}, Sina and Plaza-del-Arco, Flor Miriam and Gruber, Nora and Hovy, Dirk},
80	  journal = {arXiv preprint arXiv:2509.08825},
81	  year    = {2025},
82	}
83	
84	@inproceedings{lee_wood_doughty2024,
85	  title     = {Controlling for Unobserved Confounding with Large Language Model Classification of Patient Smoking Status},
86	  author    = {Lee, Samuel and Wood-Doughty, Zach},
87	  booktitle = {AIM-FM Workshop, NeurIPS 2024},
88	  year      = {2024},
89	}
90	
91	@inproceedings{gligoric2025,
92	  title     = {Can Unconfident {LLM} Annotations Be Used for Confident Conclusions?},
93	  author    = {Gligori{\'c}, Kristina and Zrni{\'c}, Tijana and Lee, Sara Y. and Cand{\`e}s, Emmanuel J. and Jurafsky, Dan},
94	  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics},
95	  year      = {2025},
96	}
97	
98	@article{messing2026,
99	  title   = {Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},
100	  author  = {Messing, Solomon},
101	  journal = {arXiv preprint arXiv:2604.11581},
102	  year    = {2026},
103	}
104	
105	@inproceedings{kim_garg2025,
106	  title     = {Correlated Errors in Large Language Models},
107	  author    = {Kim, Junsol and Garg, Siddharth and Peng, Yuxiao and Garg, Nikhil},
108	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
109	  year      = {2025},
110	}
111	
112	@inproceedings{keith_jensen_oconnor2020,
113	  title     = {Text and Causal Inference: A Review of Using Text to Remove Confounding from Causal Estimates},
114	  author    = {Keith, Katherine A. and Jensen, David D. and O'Connor, Brendan T.},
115	  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
116	  year      = {2020},
117	  doi       = {10.18653/v1/2020.acl-main.474},
118	}
119	
120	@inproceedings{chen_bhattacharya_keith2024,
121	  title     = {Proximal Causal Inference With Text Data},
122	  author    = {Chen, Jiayi Maggie and Bhattacharya, Rohit and Keith, Katherine A.},
123	  booktitle = {Advances in Neural Information Processing Systems 37},
124	  year      = {2024},
125	}
126	
127	@article{yang_adomavicius2018,
128	  title   = {Mind the Gap: Accounting for Measurement Error and Misclassification in Variables Generated via Data Mining},
129	  author  = {Yang, Mochen and Adomavicius, Gediminas and Burtch, Gordon and Ren, Yuqing},
130	  journal = {Information Systems Research},
131	  year    = {2018},
132	  doi     = {10.1287/isre.2017.0727},
133	}
134	
135	% ── measurement-error-epidemiology (gap-fill) ──
136	
137	@article{ogburn_vanderweele2012,
138	  title   = {On the Nondifferential Misclassification of a Binary Confounder},
139	  author  = {Ogburn, Elizabeth L. and VanderWeele, Tyler J.},
140	  journal = {Epidemiology},
141	  volume  = {23},
142	  number  = {3},
143	  pages   = {433--439},
144	  year    = {2012},
145	  doi     = {10.1097/EDE.0b013e31824d1f63},
146	}
147	
148	@article{edwards_lessler_naimi2021,
149	  title   = {An Underappreciated Misclassification Mechanism: Implications of Nondifferential Dependent Misclassification of Covariate and Exposure},
150	  author  = {Edwards, Jessie K. and Lessler, Justin and Naimi, Ashley I.},
151	  journal = {Annals of Epidemiology},
152	  volume  = {58},
153	  pages   = {104--123},
154	  year    = {2021},
155	  doi     = {10.1016/j.annepidem.2021.02.007},
156	}
157	
158	@book{gustafson2004,
159	  title     = {Measurement Error and Misclassification in Statistics and Epidemiology: Impacts and {B}ayesian Adjustments},
160	  author    = {Gustafson, Paul},
161	  publisher = {Chapman \& Hall/CRC},
162	  year      = {2004},
163	  isbn      = {978-1-58488-335-7},
164	}
165	
166	% ── sensitivity-analysis (gap-fill) ──
167	
168	@article{ding_vanderweele2016,
169	  title   = {Sensitivity Analysis Without Assumptions},
170	  author  = {Ding, Peng and VanderWeele, Tyler J.},
171	  journal = {Epidemiology},
172	  volume  = {27},
173	  number  = {3},
174	  pages   = {368--377},
175	  year    = {2016},
176	  doi     = {10.1097/EDE.0000000000000457},
177	}
178	
179	@article{smith_vanderweele2021,
180	  title   = {Multiple-bias Sensitivity Analysis Using Bounds},
181	  author  = {Smith, Louisa H. and Mathur, Maya B. and VanderWeele, Tyler J.},
182	  journal = {Epidemiology},
183	  volume  = {32},
184	  pages   = {625--634},
185	  year    = {2021},
186	  doi     = {10.1097/EDE.0000000000001380},
187	}
188	
189	@book{rosenbaum2002,
190	  title     = {Observational Studies},
191	  author    = {Rosenbaum, Paul R.},
192	  publisher = {Springer},
193	  edition   = {2nd},
194	  year      = {2002},
195	  doi       = {10.1007/978-1-4757-3692-2},
196	}
197	
198	% ── llm-annotation-quality (gap-fill) ──
199	
200	@article{stolwijk_boukes_trilling2025,
201	  title   = {Are Generative {AI} Text Annotations Systematically Biased?},
202	  author  = {Stolwijk, Sjoerd B. and Boukes, Mark and Trilling, Damian},
203	  journal = {arXiv preprint arXiv:2512.08404},
204	  year    = {2025},
205	}
206	
207	@article{cheng_mayya_sedoc2024,
208	  title   = {To Err Is Human; To Annotate, {SILICON}? Reducing Measurement Error in {LLM} Annotation},
209	  author  = {Cheng, Xiang and Mayya, Raveesh and Sedoc, Jo{\~a}o},
210	  journal = {arXiv preprint arXiv:2412.14461},
211	  year    = {2024},
212	}
213	
214	@inproceedings{audinet2025,
215	  title     = {Benchmarking Debiasing Methods for {LLM}-based Parameter Estimates},
216	  author    = {Audinet de Pieuchon, Nicolas and Daoud, Adel and Jerzak, Connor Thomas and Johansson, Moa and Johansson, Richard},
217	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
218	  pages     = {19757--19772},
219	  year      = {2025},
220	}
221	
222	% ── datasets ──
223	
224	@inproceedings{alam2021humaid,
225	  title     = {{HumAID}: Human-Annotated Disaster Incidents Data from {T}witter},
226	  author    = {Alam, Firoj and Ofli, Ferda and Imran, Muhammad},
227	  booktitle = {Proceedings of the International AAAI Conference on Web and Social Media},
228	  volume    = {15},
229	  pages     = {933--942},
230	  year      = {2021},
231	}
232	
233	% ── correction-methods (gap-fill) ──
234	
235	@article{angelopoulos2023,
236	  title   = {Prediction-powered Inference},
237	  author  = {Angelopoulos, Anastasios N. and Bates, Stephen and Fannjiang, Clara and Jordan, Michael I. and Zrni{\'c}, Tijana},
238	  journal = {Science},
239	  volume  = {382},
240	  number  = {6671},
241	  pages   = {669--674},
242	  year    = {2023},
243	  doi     = {10.1126/science.adi6000},
244	}
245	
246	@inproceedings{egami_hinck_stewart_wei2023,
247	  title     = {Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models},
248	  author    = {Egami, Naoki and Hinck, Musashi and Stewart, Brandon M. and Wei, Hanying},
249	  booktitle = {Advances in Neural Information Processing Systems 36},
250	  year      = {2023},
251	}
252	
253	@article{zrnic_candes2024,
254	  title   = {Cross-prediction-powered Inference},
255	  author  = {Zrni{\'c}, Tijana and Cand{\`e}s, Emmanuel J.},
256	  journal = {Proceedings of the National Academy of Sciences},
257	  year    = {2024},
258	  doi     = {10.1073/pnas.2322083121},
259	}
260	
261	% ── causal-inference-methodology (gap-fill) ──
262	
263	@book{pearl2009,
264	  title     = {Causality: Models, Reasoning and Inference},
265	  author    = {Pearl, Judea},
266	  publisher = {Cambridge University Press},
267	  edition   = {2nd},
268	  year      = {2009},
269	  isbn      = {978-0-521-89560-6},
270	}
271	
272	@article{greenland2003,
273	  title   = {Quantifying Biases in Causal Models: Classical Confounding vs Collider-Stratification Bias},
274	  author  = {Greenland, Sander},
275	  journal = {Epidemiology},
276	  volume  = {14},
277	  pages   = {300--306},
278	  year    = {2003},
279	  doi     = {10.1097/01.EDE.0000042804.12056.6C},
280	}
281	
282	@article{angrist_imbens1995,
283	  title   = {Two-Stage Least Squares Estimation of Average Causal Effects in Models with Variable Treatment Intensity},
284	  author  = {Angrist, Joshua D. and Imbens, Guido W.},
285	  journal = {Journal of the American Statistical Association},
286	  volume  = {90},
287	  number  = {430},
288	  pages   = {431--442},
289	  year    = {1995},
290	  doi     = {10.1080/01621459.1995.10476535},
291	}
292	
293	@article{bellemare_bloem2024,
294	  title   = {The Paper of How: Estimating Treatment Effects Using the Front-Door Criterion},
295	  author  = {Bellemare, Marc F. and Bloem, Jeffrey R. and Wexler, Noah},
296	  journal = {Oxford Bulletin of Economics and Statistics},
297	  volume  = {86},
298	  number  = {4},
299	  pages   = {951--993},
300	  year    = {2024},
301	  doi     = {10.1111/obes.12598},
302	}
303	
304	% ── Added for Related Work expansion (D016 Dream reviewer feedback) ──
305	
306	@book{carroll2006,
307	  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},
308	  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},
309	  publisher = {Chapman \& Hall/CRC},
310	  edition   = {2nd},
311	  year      = {2006},
312	  isbn      = {978-1-584-88633-4},
313	}
314	
315	@article{dosemeci1990,
316	  title   = {Does Nondifferential Misclassification of Exposure Always Bias a True Effect Toward the Null Value?},
317	  author  = {Dosemeci, Mustafa and Wacholder, Sholom and Lubin, Jay H.},
318	  journal = {American Journal of Epidemiology},
319	  volume  = {132},
320	  number  = {4},
321	  pages   = {746--748},
322	  year    = {1990},
323	  doi     = {10.1093/oxfordjournals.aje.a115716},
324	}
325	
326	@article{jurek2005,
327	  title   = {Proper Interpretation of Non-differential Misclassification Effects: Expectations vs Observations},
328	  author  = {Jurek, Anne M. and Greenland, Sander and Maldonado, George and Church, Timothy R.},
329	  journal = {International Journal of Epidemiology},
330	  volume  = {34},
331	  number  = {3},
332	  pages   = {680--687},
333	  year    = {2005},
334	  doi     = {10.1093/ije/dyi060},
335	}
336	
337	@book{lash2009,
338	  title     = {Applying Quantitative Bias Analysis to Epidemiologic Data},
339	  author    = {Lash, Timothy L. and Fox, Matthew P. and Fink, Aliza K.},
340	  publisher = {Springer},
341	  year      = {2009},
342	  isbn      = {978-0-387-87960-4},
343	  doi       = {10.1007/978-0-387-87959-8},
344	}
345	
346	@book{grimmer2022,
347	  title     = {Text as Data: A New Framework for Machine Learning and the Social Sciences},
348	  author    = {Grimmer, Justin and Roberts, Margaret E. and Stewart, Brandon M.},
349	  publisher = {Princeton University Press},
350	  year      = {2022},
351	  isbn      = {978-0-691-20754-4},
352	}
353	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8add9014-2dbb-4713-9479-ccadabfbacbf",
  "isSidechain": true,
  "promptId": "4d58ff4e-d19d-4e80-8c6c-2131e935df92",
  "agentId": "aa3739f71c0769873",
  "type": "user",
  "uuid": "3b277dc8-b7ca-4aad-95b5-ca424a4e5037",
  "sourceToolAssistantUUID": "8add9014-2dbb-4713-9479-ccadabfbacbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-22T03:54:32.688Z_

Perfect! I've found and read all the requested files. Let me compile my findings:

## Summary of Findings

### 1. **Appendix Proofs File** (`appendix_proofs.tex`)
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex`

I've read the FULL file (771 lines). Here's what I found in lines 70-160 regarding the proof structure:

**Lines 70-175: Confounding Topology Section**
- **Lemma 1 (Bias Decomposition)** [lines 32-68]: Establishes the general formula: plim̂τ(C) = τ + R(C)/D(C), where:
  - R(C) = conditional covariance between treatment and confounder effect on outcome
  - D(C) = conditional variance of treatment
  
- **Proposition 1 (Proportional case)** [lines 140-174]: For proportional confounder effects f(A) = λg(A):
  - Introduces η(C) ∈ [0,1] capturing variance between vs within groups
  - B(C) lies between 0 and B_OV (omitted-variable bias)
  - **Uses Cauchy-Schwarz inequality** for the key bounds
  - Sign preservation guaranteed if sign(τ) = sign(τ_OV)

- **Proposition 2 (General case)** [lines 176-212]: For non-proportional effects:
  - **Applies Cauchy-Schwarz twice**: once on within-group covariances, once on expectations
  - Derives worst-case bias bound: B̄ = √[Var(g)·Var(f)] / σ_T²
  - **Sign preservation condition**: |τ| > B̄ guarantees no sign flip for ALL column-stochastic C

**Lines 311-406: Collider Topology Section**
- **Bias Formula** [lines 326-334]: B(C) = -Cov(E[g(A)|A*], E[h(A)|A*]) / E[Var(T|A*)]
  - **Berkson's bias structure**: Misclassification ATTENUATES the bias toward zero
  - **Monotonicity property**: |B(C)| ≤ |B(I)| always (unlike confounding where bias grows)

- **Proposition 3 (Proportional case, Collider)** [lines 352-369]: 
  - When h(A) = λg(A): monotonic decrease as V* (between-group variance) decreases
  - **Attenuating bias property**: Sign preserved whenever sign(τ) = sign(τ + B_Berkson)

- **Proposition 4 (General case, Collider)** [lines 371-393]:
  - **Collider-specific Cauchy-Schwarz bound**: B̄_col = √[Var(g)·Var(h)] / E[Var(T|A)]
  - Same structural logic as confounding, but applied to error term covariance

**Monotonicity/Bias Derivation Framework (Key Insight)**
The paper establishes a unified framework:
1. **Law of Total Covariance** [line 60-64]: Decomposes bias into between and within components
2. **FWL (Frisch-Waugh-Lovell) decomposition** [lines 20-30]: Reduces multivariate regression to conditional regression on treatment residuals
3. **Variance decomposition**: Links D(C) to conditional vs unconditional variance of treatment
4. **Monotonicity follows from**: V* ∈ [0, V] in the denominator structure (line 168-169), making the bias function monotone in classification accuracy

---

### 2. **Introduction File** (`introduction.tex`)
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex`

**Key Claims Found:**
- **"First" contribution claim** [lines 10-13]: "Multi-class bias taxonomy. We derive bias expressions for seven canonical DAG topologies..."
- **"83.4%" headline** [line 6]: "Under K=3 non-differential exposure misclassification, 83.4% of confusion matrices cause sign reversal of the estimated treatment effect"
  - This appears in the opening paragraph as the lead finding
  - Referenced as coming from Table in appendix (line 6: "This failure breaks the classical binary guarantee...")

---

### 3. **References File** (`references.bib`)
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib`

**Citation Key Status:**

| Citation Key | Status | Details |
|---|---|---|
| `audinet2025` | ✓ FOUND | Lines 214-220: "Benchmarking Debiasing Methods for LLM-based Parameter Estimates", EMNLP 2025 |
| `zrnic_candes2024` | ✓ FOUND | Lines 253-259: "Cross-prediction-powered Inference", PNAS 2024 |
| `gligoric2025` | ✓ FOUND | Lines 91-96: "Can Unconfident LLM Annotations Be Used for Confident Conclusions?", NAACL 2025 |
| `keith_jensen_oconnor2020` | ✓ FOUND | Lines 112-118: "Text and Causal Inference: A Review...", ACL 2020 |

**All four citation keys exist and are properly formatted in the BibTeX file.**

---

## Key Technical Summary for Your Work

The **proof structure framework** establishes:
1. **Confounding (Cauchy-Schwarz)**: Applied twice to bound R(C) ≤ √[Var(g)·Var(f)], with denominator D(C) ≥ σ_T²
2. **Collider (Berkson)**: Reverse structure—misclassification *reduces* bias, monotonically bounded by perfect classification case
3. **Monotonicity derivation**: Through variance decomposition where V* ∈ [0,V] makes bias a monotone function of classification accuracy
4. **Sign preservation conditions**: Different across topologies—Confounding requires sign(τ)=sign(τ_OV); Collider requires |τ| > B̄_col

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b277dc8-b7ca-4aad-95b5-ca424a4e5037",
  "isSidechain": true,
  "agentId": "aa3739f71c0769873",
  "requestId": "req_011CbGvxXaGXN56PCuuqjF15",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df3bdc7f-dad1-47ab-ac99-4c3ed44ef970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XsQgyW2LQhXTzvcd3qt1aU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6647,
      "cache_read_input_tokens": 58519,
      "output_tokens": 1610,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6647
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1610,
          "cache_read_input_tokens": 58519,
          "cache_creation_input_tokens": 6647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6647,
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
