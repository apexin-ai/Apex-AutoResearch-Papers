# paper writing threat model

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_writing_threat_model_20260522T151212.log`
- **Structured JSON:** [`64eceef00983b9ed1b02.json`](../../sessions/64/64eceef00983b9ed1b02.json)

## Before a recorded user message

14 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_figures_and_layout",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "7e1347d4-f24f-417e-b284-c9650628c132",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-cert-manip-resist-eval/memory/"
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
    "resetsAt": 1779472200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "64057c73-c714-4afd-a94e-4f37436dbca8",
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520"
}
```

---

### Assistant

_source line 4_

Let me start by reading the referenced files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "uuid": "71a06010-1ef2-4158-8d7b-3d7ef38d49cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7PYrTWAZCxPpP7vFaw7TU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12976,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12976
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

<details open><summary>🔧 Tool call — Read · `toolu_01ET2VAYC7x5BVy6tT42Gyv6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/_project/paper/theorem1_proof.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "uuid": "6717f72d-2d7a-47f5-bcda-804465169dfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7PYrTWAZCxPpP7vFaw7TU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12976,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12976
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

_source line 6 · 2026-05-22T15:12:22.866Z_

<details><summary>↩ Tool result · `toolu_01ET2VAYC7x5BVy6tT42Gyv6`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage{amsmath, amssymb, amsthm}
4	\usepackage{mathtools}
5	\usepackage[margin=1in]{geometry}
6	\usepackage{enumitem}
7	
8	\newtheorem{theorem}{Theorem}
9	\newtheorem{lemma}[theorem]{Lemma}
10	\newtheorem{proposition}[theorem]{Proposition}
11	\newtheorem{corollary}[theorem]{Corollary}
12	\newtheorem{definition}[theorem]{Definition}
13	\newtheorem*{remark}{Remark}
14	
15	\DeclareMathOperator*{\argmax}{arg\,max}
16	
17	\title{Weakest-Link Monotonicity Theorem for\\Majority-Vote Panel ASR}
18	\author{}
19	\date{}
20	
21	\begin{document}
22	\maketitle
23	
24	%% ================================================================
25	\section{Setup and Definitions}
26	%% ================================================================
27	
28	\begin{definition}[Panel and Majority Vote]
29	\label{def:panel}
30	A \emph{panel} $\mathcal{P} = \{J_1, \ldots, J_K\}$ consists of $K$ judges ($K$ odd) that independently evaluate a candidate text. The panel uses \emph{majority-vote aggregation}: it is \emph{compromised} if and only if at least $t = \lceil K/2 \rceil$ judges are individually compromised.
31	\end{definition}
32	
33	\begin{definition}[Attack Model]
34	\label{def:attack}
35	An \emph{attack} $a \in \mathcal{A}$ is an adversarial perturbation applied to the input that all judges evaluate. Under attack $a$, the judges' failure outcomes are described by a joint distribution over binary random variables $(X_1^a, \ldots, X_K^a) \in \{0,1\}^K$, where $X_j^a = 1$ indicates that judge $J_j$ is compromised. The \emph{individual vulnerability} of $J_j$ under attack $a$ is
36	\[
37	    \eta_j(a) \;=\; \Pr(X_j^a = 1).
38	\]
39	The \emph{panel ASR} under attack $a$ is
40	\[
41	    \mathrm{ASR}(\mathcal{P}, a) \;=\; \Pr\!\Bigl(\textstyle\sum_{j=1}^K X_j^a \;\geq\; t\Bigr).
42	\]
43	\end{definition}
44	
45	\begin{definition}[Adaptive Adversary]
46	\label{def:adversary}
47	An \emph{adaptive adversary} has full knowledge of the panel composition $\mathcal{P}$, including the per-judge vulnerability profiles $\{\eta_j(\cdot)\}_{j=1}^K$ and the inter-judge correlation structure. The adversary selects $a^* \in \mathcal{A}$ to maximize the panel ASR:
48	\[
49	    \mathrm{ASR}^*(\mathcal{P}) \;=\; \sup_{a \in \mathcal{A}}\; \mathrm{ASR}(\mathcal{P}, a).
50	\]
51	\end{definition}
52	
53	\begin{definition}[Pointwise Vulnerability Dominance]
54	\label{def:dominance}
55	Let $\mathcal{P} = \{J_1, \ldots, J_{K-1}, J_K\}$ and $\mathcal{P}' = \{J_1, \ldots, J_{K-1}, J_K'\}$ be two panels sharing the first $K-1$ judges. Write $\mathbf{X}_{-K}^a = (X_1^a, \ldots, X_{K-1}^a)$ for the shared judges' outcomes. We say $J_K'$ is \emph{pointwise more vulnerable} than $J_K$ if, for every attack $a \in \mathcal{A}$ and every realization $\mathbf{x}_{-K} \in \{0,1\}^{K-1}$:
56	\[
57	    \Pr\bigl(X_{K'}^a = 1 \;\big|\; \mathbf{X}_{-K}^a = \mathbf{x}_{-K}\bigr) \;\geq\; \Pr\bigl(X_K^a = 1 \;\big|\; \mathbf{X}_{-K}^a = \mathbf{x}_{-K}\bigr).
58	\]
59	We further require that for each attack $a$, the marginal joint distribution of $\mathbf{X}_{-K}^a$ is the same in both panels $\mathcal{P}$ and $\mathcal{P}'$.
60	\end{definition}
61	
62	\begin{remark}
63	Under conditional independence (i.e., $X_K^a \perp \mathbf{X}_{-K}^a$ for all $a$), pointwise dominance reduces to \emph{marginal dominance}: $\eta_{K'}(a) \geq \eta_K(a)$ for all $a \in \mathcal{A}$. The conditional form is needed when judge failures are correlated---for instance, when a shared architectural vulnerability causes multiple judges to fail on the same inputs.
64	\end{remark}
65	
66	
67	%% ================================================================
68	\section{Warm-Up: $K=3$, Independent Judges}
69	%% ================================================================
70	
71	\begin{lemma}[$K=3$ Monotonicity]\label{lem:k3}
72	For a panel of $K=3$ conditionally independent judges with vulnerabilities $\eta_1, \eta_2, \eta_3 \in [0,1]$ under a fixed attack, the panel ASR under majority vote ($t=2$) is
73	\[
74	    \mathrm{ASR} \;=\; \eta_1\eta_2 + \eta_1\eta_3 + \eta_2\eta_3 - 2\,\eta_1\eta_2\eta_3,
75	\]
76	and is strictly increasing in each $\eta_j$ whenever the other two judges are not simultaneously trivial. Letting $\eta_3 = \eta_{\max}$ without loss of generality:
77	\[
78	    \frac{\partial\,\mathrm{ASR}}{\partial\,\eta_{\max}} \;=\; \eta_1(1-\eta_2) + \eta_2(1-\eta_1) \;\geq\; 0,
79	\]
80	with equality if and only if $(\eta_1, \eta_2) \in \{(0,0),\, (1,1)\}$.
81	\end{lemma}
82	
83	\begin{proof}
84	The panel is compromised when at least 2 of 3 judges fail. Under independence, enumerating the four favorable configurations:
85	\begin{align}
86	    \mathrm{ASR}
87	    &= \Pr(X_1{=}1,\, X_2{=}1,\, X_3{=}0) + \Pr(X_1{=}1,\, X_2{=}0,\, X_3{=}1) \nonumber \\
88	    &\quad + \Pr(X_1{=}0,\, X_2{=}1,\, X_3{=}1) + \Pr(X_1{=}1,\, X_2{=}1,\, X_3{=}1) \nonumber \\[4pt]
89	    &= \eta_1\eta_2(1{-}\eta_3) + \eta_1(1{-}\eta_2)\eta_3 + (1{-}\eta_1)\eta_2\eta_3 + \eta_1\eta_2\eta_3. \label{eq:k3-expand}
90	\end{align}
91	Collecting terms:
92	\begin{align*}
93	    \mathrm{ASR}
94	    &= \eta_1\eta_2 \underbrace{-\, \eta_1\eta_2\eta_3 + \eta_1\eta_3 - \eta_1\eta_2\eta_3 + \eta_2\eta_3 - \eta_1\eta_2\eta_3 + \eta_1\eta_2\eta_3}_{\text{from the last three terms}} \\
95	    &= \eta_1\eta_2 + \eta_1\eta_3 + \eta_2\eta_3 - 2\,\eta_1\eta_2\eta_3.
96	\end{align*}
97	Differentiating with respect to $\eta_3$:
98	\[
99	    \frac{\partial\,\mathrm{ASR}}{\partial\,\eta_3}
100	    \;=\; \eta_1 + \eta_2 - 2\,\eta_1\eta_2
101	    \;=\; \eta_1(1 - \eta_2) + \eta_2(1 - \eta_1).
102	\]
103	Since $\eta_1, \eta_2 \in [0,1]$, both summands are non-negative. The derivative vanishes iff both are zero: $\eta_1(1{-}\eta_2) = 0$ and $\eta_2(1{-}\eta_1) = 0$. If $\eta_1 = 0$, the second equation forces $\eta_2 = 0$. If $\eta_2 = 1$, the first is automatic, and the second forces $\eta_1 = 1$. Hence equality holds iff $(\eta_1, \eta_2) \in \{(0,0),\, (1,1)\}$.
104	\end{proof}
105	
106	
107	%% ================================================================
108	\section{General $K$, Independent Judges}
109	%% ================================================================
110	
111	\begin{lemma}[General Monotonicity, Independent Case]\label{lem:general-indep}
112	For a panel of $K$ conditionally independent judges under a fixed attack, the panel ASR under majority vote with threshold $t = \lceil K/2 \rceil$ satisfies
113	\[
114	    \mathrm{ASR} \;=\; \Pr(Y \geq t) \;+\; \Pr(Y = t{-}1)\,\cdot\, \eta_K,
115	\]
116	where $Y = \sum_{j=1}^{K-1} X_j$ counts failures among the other $K{-}1$ judges. Consequently,
117	\[
118	    \frac{\partial\,\mathrm{ASR}}{\partial\,\eta_K} \;=\; \Pr(Y = t{-}1) \;\geq\; 0.
119	\]
120	\end{lemma}
121	
122	\begin{proof}
123	Conditioning on the binary outcome of judge $K$:
124	\begin{align*}
125	    \mathrm{ASR}
126	    &= \Pr(Y + X_K \geq t) \\
127	    &= \Pr(Y \geq t{-}1)\,\cdot\,\eta_K \;+\; \Pr(Y \geq t)\,\cdot\,(1 - \eta_K) \\
128	    &= \Pr(Y \geq t) \;+\; \bigl[\Pr(Y \geq t{-}1) - \Pr(Y \geq t)\bigr]\,\cdot\,\eta_K \\
129	    &= \Pr(Y \geq t) \;+\; \Pr(Y = t{-}1)\,\cdot\,\eta_K.
130	\end{align*}
131	The second line uses independence of $X_K$ and $Y$, conditioning on whether $X_K = 1$ (needing $Y \geq t{-}1$) or $X_K = 0$ (needing $Y \geq t$). The result is affine in $\eta_K$ with slope $\Pr(Y = t{-}1) \geq 0$.
132	\end{proof}
133	
134	\begin{remark}[Pivotal Voter Interpretation]
135	The slope $\Pr(Y = t{-}1)$ is exactly the probability that judge $K$ is \emph{pivotal}: the remaining $K{-}1$ judges produce exactly $t{-}1$ failures, and judge $K$'s outcome determines the panel decision. Monotonicity holds because a judge can only tip the panel toward compromise (by failing), never away from it.
136	\end{remark}
137	
138	
139	%% ================================================================
140	\section{Main Result: Correlated Judges, Adaptive Adversary}
141	%% ================================================================
142	
143	\begin{theorem}[Weakest-Link Monotonicity]\label{thm:main}
144	Let $\mathcal{P} = \{J_1, \ldots, J_{K-1}, J_K\}$ and $\mathcal{P}' = \{J_1, \ldots, J_{K-1}, J_K'\}$ be two panels using majority vote with threshold $t = \lceil K/2 \rceil$, sharing judges $J_1, \ldots, J_{K-1}$ and satisfying Definition~\ref{def:dominance} (pointwise vulnerability dominance of $J_K'$ over $J_K$). Then:
145	\begin{enumerate}[label=(\alph*)]
146	    \item For every fixed attack $a \in \mathcal{A}$:
147	    \[
148	        \mathrm{ASR}(\mathcal{P}', a) \;\geq\; \mathrm{ASR}(\mathcal{P}, a).
149	    \]
150	    \item For any adversary strategy, including an adaptive adversary:
151	    \[
152	        \mathrm{ASR}^*(\mathcal{P}') \;\geq\; \mathrm{ASR}^*(\mathcal{P}).
153	    \]
154	\end{enumerate}
155	In particular, replacing the weakest panel member with a more vulnerable judge (increasing $\eta_{\max}$) cannot decrease the panel ASR.
156	\end{theorem}
157	
158	\begin{proof}
159	\textbf{Part (a): Fixed attack.}
160	Fix an arbitrary attack $a \in \mathcal{A}$. Let $\mathbf{x}_{-K} = (x_1, \ldots, x_{K-1}) \in \{0,1\}^{K-1}$ denote a realization of the shared judges' outcomes, and let $s = \sum_{j=1}^{K-1} x_j$. By the law of total probability:
161	\begin{equation}\label{eq:total-prob}
162	    \mathrm{ASR}(\mathcal{P}, a)
163	    \;=\; \sum_{\mathbf{x}_{-K} \in \{0,1\}^{K-1}} \Pr(\mathbf{X}_{-K}^a = \mathbf{x}_{-K})\;\cdot\; \Pr\!\bigl(s + X_K^a \geq t \;\big|\; \mathbf{X}_{-K}^a = \mathbf{x}_{-K}\bigr).
164	\end{equation}
165	Since $X_K^a \in \{0,1\}$, the inner probability depends on $s$ in exactly three cases:
166	\begin{itemize}
167	    \item \textbf{Case $s \geq t$:} The panel is compromised regardless of $X_K^a$. Both panels contribute~$1$.
168	    \item \textbf{Case $s = t{-}1$:} The panel is compromised iff $X_K^a = 1$ (resp.\ $X_{K'}^a = 1$). By pointwise dominance:
169	    \[
170	        \Pr(X_{K'}^a = 1 \mid \mathbf{x}_{-K}) \;\geq\; \Pr(X_K^a = 1 \mid \mathbf{x}_{-K}).
171	    \]
172	    \item \textbf{Case $s \leq t{-}2$:} Even with $X_K^a = 1$, the total $s + 1 \leq t{-}1 < t$. Neither panel is compromised; both contribute~$0$.
173	\end{itemize}
174	Since the marginal distribution of $\mathbf{X}_{-K}^a$ is identical in both panels (Definition~\ref{def:dominance}), summing over all realizations yields
175	\begin{equation}\label{eq:pointwise-ineq}
176	    \mathrm{ASR}(\mathcal{P}', a) \;\geq\; \mathrm{ASR}(\mathcal{P}, a).
177	\end{equation}
178	
179	\medskip
180	\noindent\textbf{Part (b): Adaptive adversary.}
181	Taking the supremum over all attacks and applying \eqref{eq:pointwise-ineq}:
182	\[
183	    \mathrm{ASR}^*(\mathcal{P}')
184	    \;=\; \sup_{a \in \mathcal{A}} \mathrm{ASR}(\mathcal{P}', a)
185	    \;\geq\; \sup_{a \in \mathcal{A}} \mathrm{ASR}(\mathcal{P}, a)
186	    \;=\; \mathrm{ASR}^*(\mathcal{P}),
187	\]
188	since each term in the supremum on the right is bounded by the corresponding term on the left. \qedhere
189	\end{proof}
190	
191	\begin{remark}[Generality of the Result]
192	Three aspects of Theorem~\ref{thm:main} merit emphasis:
193	\begin{enumerate}[label=(\roman*)]
194	    \item \textbf{Arbitrary correlations.} The proof makes no independence assumption. Judges may exhibit arbitrary failure correlations---including those induced by shared architectural vulnerabilities, common training data, or attack transfer effects---as long as pointwise dominance holds.
195	    \item \textbf{Threshold generality.} The proof uses only the threshold structure of majority vote. It extends verbatim to any $t$-out-of-$K$ aggregation rule, including unanimity ($t = K$) and any-judge-fails ($t = 1$).
196	    \item \textbf{Adversary generality.} Part (b) holds for any adversary class that selects from the same attack space $\mathcal{A}$, including randomized adversaries (who select a distribution over $\mathcal{A}$, since a mixture preserves the pointwise inequality).
197	\end{enumerate}
198	\end{remark}
199	
200	\begin{remark}[Sufficient Conditions for Pointwise Dominance]
201	Pointwise dominance (Definition~\ref{def:dominance}) is satisfied whenever:
202	\begin{enumerate}[label=(\roman*)]
203	    \item \textbf{Model capability ordering.} $J_K'$ has strictly lower capability than $J_K$ on all tasks, so any attack that fools $J_K$ also fools $J_K'$, and $J_K'$ is vulnerable to additional attacks.
204	    \item \textbf{Vulnerability superset.} The set of inputs on which $J_K'$ errs is a superset of those on which $J_K$ errs, for every attack.
205	    \item \textbf{Conditional independence.} If $X_K^a \perp \mathbf{X}_{-K}^a$ for all $a$, then pointwise dominance reduces to $\eta_{K'}(a) \geq \eta_K(a)$ for all $a$ (marginal dominance), which is empirically verifiable by measuring individual ASR.
206	\end{enumerate}
207	\end{remark}
208	
209	\begin{remark}[Coupling Interpretation]
210	An equivalent proof uses a coupling argument: construct $(X_K^a, X_{K'}^a)$ on a common probability space such that $X_{K'}^a \geq X_K^a$ almost surely (feasible by the standard coupling for stochastic dominance whenever pointwise dominance holds). Then $\sum_{j=1}^{K-1} X_j^a + X_{K'}^a \geq \sum_{j=1}^{K-1} X_j^a + X_K^a$ pointwise, so $\{$panel~$\mathcal{P}$ fails$\} \subseteq \{$panel~$\mathcal{P}'$ fails$\}$ and $\mathrm{ASR}(\mathcal{P}', a) \geq \mathrm{ASR}(\mathcal{P}, a)$.
211	\end{remark}
212	
213	
214	%% ================================================================
215	\section{Tightness and Bounds}
216	%% ================================================================
217	
218	\begin{proposition}[Equality Conditions]\label{prop:tight}
219	Under the conditions of Theorem~\ref{thm:main}, for a fixed attack $a$:
220	\[
221	    \mathrm{ASR}(\mathcal{P}', a) = \mathrm{ASR}(\mathcal{P}, a)
222	\]
223	if and only if, for every realization $\mathbf{x}_{-K}$ with $\sum x_j = t{-}1$ and $\Pr(\mathbf{X}_{-K}^a = \mathbf{x}_{-K}) > 0$:
224	\[
225	    \Pr(X_{K'}^a = 1 \mid \mathbf{x}_{-K}) \;=\; \Pr(X_K^a = 1 \mid \mathbf{x}_{-K}).
226	\]
227	For conditionally independent judges, this simplifies to: either $\Pr(Y = t{-}1) = 0$ (no pivotal configuration exists) or $\eta_{K'}(a) = \eta_K(a)$.
228	\end{proposition}
229	
230	\begin{proof}
231	From the proof of Theorem~\ref{thm:main}, the ASR difference is:
232	\begin{align*}
233	    \Delta
234	    &= \mathrm{ASR}(\mathcal{P}', a) - \mathrm{ASR}(\mathcal{P}, a) \\
235	    &= \!\!\sum_{\substack{\mathbf{x}_{-K}:\, s = t-1}}\!\! \Pr(\mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})\,\bigl[\Pr(X_{K'}^a {=} 1 \mid \mathbf{x}_{-K}) - \Pr(X_K^a {=} 1 \mid \mathbf{x}_{-K})\bigr].
236	\end{align*}
237	Each summand is non-negative (pointwise dominance ensures the bracket is $\geq 0$; the probability weight is $\geq 0$). The sum vanishes iff every summand with positive weight has a zero bracket. Under conditional independence, $\Pr(X_K^a = 1 \mid \mathbf{x}_{-K}) = \eta_K(a)$ is constant across realizations, so the condition collapses to $\eta_{K'}(a) = \eta_K(a)$ or the event $\{Y = t{-}1\}$ having zero probability.
238	\end{proof}
239	
240	\begin{remark}
241	The condition $\Pr(Y = t{-}1) = 0$ is degenerate: it requires all $\eta_j \in \{0,1\}$ with the count of $\eta_j = 1$ never equaling $t{-}1$. In all non-degenerate panels, the monotonicity is \emph{strict} whenever $\eta_{K'} > \eta_K$ under some attack.
242	\end{remark}
243	
244	\begin{proposition}[Panel ASR Bounds]\label{prop:bounds}
245	For a panel of $K$ conditionally independent judges with ordered vulnerabilities $\eta_{(1)} \leq \cdots \leq \eta_{(K)} = \eta_{\max}$ under a fixed attack:
246	\[
247	    \prod_{j=K-t+1}^{K} \eta_{(j)} \;\leq\; \mathrm{ASR} \;\leq\; \sum_{k=t}^{K} \binom{K}{k}\, \eta_{\max}^{\,k}\, (1-\eta_{\max})^{K-k}.
248	\]
249	\end{proposition}
250	
251	\begin{proof}
252	\textit{Lower bound.}
253	The event that the $t$ most vulnerable judges ($J_{(K-t+1)}, \ldots, J_{(K)}$) all fail implies panel compromise. By independence:
254	\[
255	    \mathrm{ASR} \;\geq\; \Pr\!\bigl(\textstyle\bigcap_{j=K-t+1}^K \{X_{(j)} = 1\}\bigr) \;=\; \prod_{j=K-t+1}^{K} \eta_{(j)}.
256	\]
257	
258	\textit{Upper bound.}
259	Since $\eta_j \leq \eta_{\max}$ for all $j$, replacing each $\eta_j$ with $\eta_{\max}$ increases ASR by Lemma~\ref{lem:general-indep} (applied iteratively to each judge). The resulting panel has i.i.d.\ $\mathrm{Bernoulli}(\eta_{\max})$ failures, giving the binomial tail.
260	\end{proof}
261	
262	\begin{remark}[Scaling Regimes]
263	For small $\eta_{\max}$ and fixed $K$, the leading-order behavior is:
264	\begin{itemize}
265	    \item If the top $t$ vulnerabilities satisfy $\eta_{(j)} = \Theta(\eta_{\max})$ for $j \geq K{-}t{+}1$: \[ \mathrm{ASR} \;=\; \Theta\!\bigl(\eta_{\max}^{\,t}\bigr). \]
266	    Majority vote provides a $t$-th power suppression relative to the individual maximum.
267	    \item If the vulnerability distribution is \emph{heavy-tailed} (one judge much weaker than the rest): the lower bound $\prod \eta_{(j)}$ is small, but the adversary can still exploit correlated failures (attack transfer) to push ASR closer to $\binom{K}{t}\eta_{\max}^t$.
268	    \item For $K=3$, $t=2$: $\mathrm{ASR} = \Theta(\eta_{\max}^2)$ in the small-vulnerability regime.
269	\end{itemize}
270	\end{remark}
271	
272	
273	%% ================================================================
274	\section{Corollary: Panel Design}
275	%% ================================================================
276	
277	\begin{corollary}[Robustness-First Design Principle]\label{cor:design}
278	Under the adaptive adversary model of Definition~\ref{def:adversary}, the optimal panel selection strategy is \emph{robustness-first}:
279	\begin{enumerate}[label=\textbf{Stage~\arabic*}:]
280	    \item \textbf{Robustness screening.} From the candidate pool, retain only judges satisfying $\eta_j \leq \tau$ for a robustness threshold $\tau$. By Theorem~\ref{thm:main}, replacing any judge with $\eta_j > \tau$ by one with $\eta_j \leq \tau$ weakly reduces panel ASR.
281	    \item \textbf{Diversity maximization.} Among the retained judges, select the $K$-judge panel that maximizes effective independence $K_{\mathrm{eff}}$ (or any suitable diversity measure). This provides residual protection against broad-spectrum attacks without introducing weak links.
282	\end{enumerate}
283	The ordering is essential: diversity maximization without robustness screening may increase $\eta_{\max}$ via the diversity-capability tradeoff, which by Theorem~\ref{thm:main} weakly increases panel ASR.
284	\end{corollary}
285	
286	\begin{proof}
287	Stage~1 is a direct application of Theorem~\ref{thm:main}: if $J_K$ has $\eta_K > \tau$ and $J_K'$ has $\eta_{K'} \leq \tau < \eta_K$, and $J_K'$ satisfies pointwise dominance of $J_K$ over $J_K'$ (i.e., $J_K$ is pointwise more vulnerable than $J_K'$), then $\mathrm{ASR}^*(\mathcal{P}) \geq \mathrm{ASR}^*(\mathcal{P}')$. The robustness constraint $\eta_j \leq \tau$ for all panel members ensures $\eta_{\max} \leq \tau$, bounding the dominant predictor.
288	
289	Stage~2 is a secondary optimization: given $\eta_{\max} \leq \tau$, the residual variance in panel ASR is determined by inter-judge correlations and the specific attack-type vulnerability distribution. Maximizing $K_{\mathrm{eff}}$ provides protection in the regime where attacks exploit shared biases (broad-spectrum attacks), as the SDPI bound gives $\mathrm{ASR} \leq K_{\mathrm{eff}} \cdot \eta_{\max}$.
290	
291	The ordering matters because the diversity-capability tradeoff ($r \approx -0.78$, $p < 0.001$ empirically) implies that panels selected for maximal diversity tend to include weaker judges. By Theorem~\ref{thm:main}, the resulting increase in $\eta_{\max}$ dominates any benefit from increased independence.
292	\end{proof}
293	
294	
295	%% ================================================================
296	\section{Connection to Empirical Results}
297	%% ================================================================
298	
299	\begin{remark}[Empirical Validation]
300	Theorem~\ref{thm:main} makes a testable prediction: in a multivariate regression $\log(\mathrm{ASR}) \sim \beta_1 \log(\eta_{\max}) + \beta_2 \log(K_{\mathrm{eff}})$, $\eta_{\max}$ should be a significant predictor ($\beta_1 > 0$) while $K_{\mathrm{eff}}$ should be weak or non-significant ($\beta_2 \approx 0$), because the theorem establishes monotonicity in $\eta_{\max}$ but not in $K_{\mathrm{eff}}$.
301	
302	Across 12 experimental conditions (2 benchmarks $\times$ 6 attack types):
303	\begin{itemize}
304	    \item $\eta_{\max}$ is significant (BH-FDR $q < 0.05$) in 6/12 conditions (50\%), with 3/12 surviving Bonferroni correction.
305	    \item $K_{\mathrm{eff}}$ is significant in only 1/12 conditions (8\%). Residualized $K_{\mathrm{eff}}$ (orthogonalized against $\eta_{\max}$, VIF $= 1.04$) confirms this is not a collinearity artifact.
306	    \item The sole exception (ARC $\times$ sycophancy, $\beta_2 = -2.85$, $p = 0.003$) corresponds to the one attack type that exploits a \emph{shared} judge bias rather than targeting individual vulnerabilities---the ``BFT-like'' regime where faults are approximately random.
307	\end{itemize}
308	This pattern is precisely what Theorem~\ref{thm:main} predicts: monotonicity in $\eta_{\max}$ drives the primary effect, and $K_{\mathrm{eff}}$ matters only when the adversary cannot selectively target the weakest judge.
309	\end{remark}
310	
311	\begin{remark}[When Diversity Helps]
312	Theorem~\ref{thm:main} does \emph{not} claim diversity is useless. It establishes that \emph{reducing $\eta_{\max}$ weakly dominates increasing $K_{\mathrm{eff}}$} as a defense strategy. Diversity retains value in three regimes:
313	\begin{enumerate}[label=(\roman*)]
314	    \item \textbf{Controlled $\eta_{\max}$:} When all judges exceed a robustness threshold (Corollary~\ref{cor:design}, Stage~2), higher $K_{\mathrm{eff}}$ reduces the ASR ceiling via the SDPI bound $\mathrm{ASR} \leq K_{\mathrm{eff}} \cdot \eta_{\max}$.
315	    \item \textbf{Broad-spectrum attacks:} When attacks exploit biases shared across judges (sycophancy, position bias), failures approximate random faults and the BFT analogy holds.
316	    \item \textbf{Non-adversarial settings:} For calibration, bias reduction, and inter-rater agreement, diversity provides standard statistical benefits unrelated to adversarial robustness.
317	\end{enumerate}
318	\end{remark}
319	
320	
321	\end{document}
322	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "uuid": "43695cce-48a3-4a61-b275-7173a59d3052",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/_project/paper/theorem1_proof.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage{amsmath, amssymb, amsthm}\n\\usepackage{mathtools}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{enumitem}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{lemma}[theorem]{Lemma}\n\\newtheorem{proposition}[theorem]{Proposition}\n\\newtheorem{corollary}[theorem]{Corollary}\n\\newtheorem{definition}[theorem]{Definition}\n\\newtheorem*{remark}{Remark}\n\n\\DeclareMathOperator*{\\argmax}{arg\\,max}\n\n\\title{Weakest-Link Monotonicity Theorem for\\\\Majority-Vote Panel ASR}\n\\author{}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ================================================================\n\\section{Setup and Definitions}\n%% ================================================================\n\n\\begin{definition}[Panel and Majority Vote]\n\\label{def:panel}\nA \\emph{panel} $\\mathcal{P} = \\{J_1, \\ldots, J_K\\}$ consists of $K$ judges ($K$ odd) that independently evaluate a candidate text. The panel uses \\emph{majority-vote aggregation}: it is \\emph{compromised} if and only if at least $t = \\lceil K/2 \\rceil$ judges are individually compromised.\n\\end{definition}\n\n\\begin{definition}[Attack Model]\n\\label{def:attack}\nAn \\emph{attack} $a \\in \\mathcal{A}$ is an adversarial perturbation applied to the input that all judges evaluate. Under attack $a$, the judges' failure outcomes are described by a joint distribution over binary random variables $(X_1^a, \\ldots, X_K^a) \\in \\{0,1\\}^K$, where $X_j^a = 1$ indicates that judge $J_j$ is compromised. The \\emph{individual vulnerability} of $J_j$ under attack $a$ is\n\\[\n    \\eta_j(a) \\;=\\; \\Pr(X_j^a = 1).\n\\]\nThe \\emph{panel ASR} under attack $a$ is\n\\[\n    \\mathrm{ASR}(\\mathcal{P}, a) \\;=\\; \\Pr\\!\\Bigl(\\textstyle\\sum_{j=1}^K X_j^a \\;\\geq\\; t\\Bigr).\n\\]\n\\end{definition}\n\n\\begin{definition}[Adaptive Adversary]\n\\label{def:adversary}\nAn \\emph{adaptive adversary} has full knowledge of the panel composition $\\mathcal{P}$, including the per-judge vulnerability profiles $\\{\\eta_j(\\cdot)\\}_{j=1}^K$ and the inter-judge correlation structure. The adversary selects $a^* \\in \\mathcal{A}$ to maximize the panel ASR:\n\\[\n    \\mathrm{ASR}^*(\\mathcal{P}) \\;=\\; \\sup_{a \\in \\mathcal{A}}\\; \\mathrm{ASR}(\\mathcal{P}, a).\n\\]\n\\end{definition}\n\n\\begin{definition}[Pointwise Vulnerability Dominance]\n\\label{def:dominance}\nLet $\\mathcal{P} = \\{J_1, \\ldots, J_{K-1}, J_K\\}$ and $\\mathcal{P}' = \\{J_1, \\ldots, J_{K-1}, J_K'\\}$ be two panels sharing the first $K-1$ judges. Write $\\mathbf{X}_{-K}^a = (X_1^a, \\ldots, X_{K-1}^a)$ for the shared judges' outcomes. We say $J_K'$ is \\emph{pointwise more vulnerable} than $J_K$ if, for every attack $a \\in \\mathcal{A}$ and every realization $\\mathbf{x}_{-K} \\in \\{0,1\\}^{K-1}$:\n\\[\n    \\Pr\\bigl(X_{K'}^a = 1 \\;\\big|\\; \\mathbf{X}_{-K}^a = \\mathbf{x}_{-K}\\bigr) \\;\\geq\\; \\Pr\\bigl(X_K^a = 1 \\;\\big|\\; \\mathbf{X}_{-K}^a = \\mathbf{x}_{-K}\\bigr).\n\\]\nWe further require that for each attack $a$, the marginal joint distribution of $\\mathbf{X}_{-K}^a$ is the same in both panels $\\mathcal{P}$ and $\\mathcal{P}'$.\n\\end{definition}\n\n\\begin{remark}\nUnder conditional independence (i.e., $X_K^a \\perp \\mathbf{X}_{-K}^a$ for all $a$), pointwise dominance reduces to \\emph{marginal dominance}: $\\eta_{K'}(a) \\geq \\eta_K(a)$ for all $a \\in \\mathcal{A}$. The conditional form is needed when judge failures are correlated---for instance, when a shared architectural vulnerability causes multiple judges to fail on the same inputs.\n\\end{remark}\n\n\n%% ================================================================\n\\section{Warm-Up: $K=3$, Independent Judges}\n%% ================================================================\n\n\\begin{lemma}[$K=3$ Monotonicity]\\label{lem:k3}\nFor a panel of $K=3$ conditionally independent judges with vulnerabilities $\\eta_1, \\eta_2, \\eta_3 \\in [0,1]$ under a fixed attack, the panel ASR under majority vote ($t=2$) is\n\\[\n    \\mathrm{ASR} \\;=\\; \\eta_1\\eta_2 + \\eta_1\\eta_3 + \\eta_2\\eta_3 - 2\\,\\eta_1\\eta_2\\eta_3,\n\\]\nand is strictly increasing in each $\\eta_j$ whenever the other two judges are not simultaneously trivial. Letting $\\eta_3 = \\eta_{\\max}$ without loss of generality:\n\\[\n    \\frac{\\partial\\,\\mathrm{ASR}}{\\partial\\,\\eta_{\\max}} \\;=\\; \\eta_1(1-\\eta_2) + \\eta_2(1-\\eta_1) \\;\\geq\\; 0,\n\\]\nwith equality if and only if $(\\eta_1, \\eta_2) \\in \\{(0,0),\\, (1,1)\\}$.\n\\end{lemma}\n\n\\begin{proof}\nThe panel is compromised when at least 2 of 3 judges fail. Under independence, enumerating the four favorable configurations:\n\\begin{align}\n    \\mathrm{ASR}\n    &= \\Pr(X_1{=}1,\\, X_2{=}1,\\, X_3{=}0) + \\Pr(X_1{=}1,\\, X_2{=}0,\\, X_3{=}1) \\nonumber \\\\\n    &\\quad + \\Pr(X_1{=}0,\\, X_2{=}1,\\, X_3{=}1) + \\Pr(X_1{=}1,\\, X_2{=}1,\\, X_3{=}1) \\nonumber \\\\[4pt]\n    &= \\eta_1\\eta_2(1{-}\\eta_3) + \\eta_1(1{-}\\eta_2)\\eta_3 + (1{-}\\eta_1)\\eta_2\\eta_3 + \\eta_1\\eta_2\\eta_3. \\label{eq:k3-expand}\n\\end{align}\nCollecting terms:\n\\begin{align*}\n    \\mathrm{ASR}\n    &= \\eta_1\\eta_2 \\underbrace{-\\, \\eta_1\\eta_2\\eta_3 + \\eta_1\\eta_3 - \\eta_1\\eta_2\\eta_3 + \\eta_2\\eta_3 - \\eta_1\\eta_2\\eta_3 + \\eta_1\\eta_2\\eta_3}_{\\text{from the last three terms}} \\\\\n    &= \\eta_1\\eta_2 + \\eta_1\\eta_3 + \\eta_2\\eta_3 - 2\\,\\eta_1\\eta_2\\eta_3.\n\\end{align*}\nDifferentiating with respect to $\\eta_3$:\n\\[\n    \\frac{\\partial\\,\\mathrm{ASR}}{\\partial\\,\\eta_3}\n    \\;=\\; \\eta_1 + \\eta_2 - 2\\,\\eta_1\\eta_2\n    \\;=\\; \\eta_1(1 - \\eta_2) + \\eta_2(1 - \\eta_1).\n\\]\nSince $\\eta_1, \\eta_2 \\in [0,1]$, both summands are non-negative. The derivative vanishes iff both are zero: $\\eta_1(1{-}\\eta_2) = 0$ and $\\eta_2(1{-}\\eta_1) = 0$. If $\\eta_1 = 0$, the second equation forces $\\eta_2 = 0$. If $\\eta_2 = 1$, the first is automatic, and the second forces $\\eta_1 = 1$. Hence equality holds iff $(\\eta_1, \\eta_2) \\in \\{(0,0),\\, (1,1)\\}$.\n\\end{proof}\n\n\n%% ================================================================\n\\section{General $K$, Independent Judges}\n%% ================================================================\n\n\\begin{lemma}[General Monotonicity, Independent Case]\\label{lem:general-indep}\nFor a panel of $K$ conditionally independent judges under a fixed attack, the panel ASR under majority vote with threshold $t = \\lceil K/2 \\rceil$ satisfies\n\\[\n    \\mathrm{ASR} \\;=\\; \\Pr(Y \\geq t) \\;+\\; \\Pr(Y = t{-}1)\\,\\cdot\\, \\eta_K,\n\\]\nwhere $Y = \\sum_{j=1}^{K-1} X_j$ counts failures among the other $K{-}1$ judges. Consequently,\n\\[\n    \\frac{\\partial\\,\\mathrm{ASR}}{\\partial\\,\\eta_K} \\;=\\; \\Pr(Y = t{-}1) \\;\\geq\\; 0.\n\\]\n\\end{lemma}\n\n\\begin{proof}\nConditioning on the binary outcome of judge $K$:\n\\begin{align*}\n    \\mathrm{ASR}\n    &= \\Pr(Y + X_K \\geq t) \\\\\n    &= \\Pr(Y \\geq t{-}1)\\,\\cdot\\,\\eta_K \\;+\\; \\Pr(Y \\geq t)\\,\\cdot\\,(1 - \\eta_K) \\\\\n    &= \\Pr(Y \\geq t) \\;+\\; \\bigl[\\Pr(Y \\geq t{-}1) - \\Pr(Y \\geq t)\\bigr]\\,\\cdot\\,\\eta_K \\\\\n    &= \\Pr(Y \\geq t) \\;+\\; \\Pr(Y = t{-}1)\\,\\cdot\\,\\eta_K.\n\\end{align*}\nThe second line uses independence of $X_K$ and $Y$, conditioning on whether $X_K = 1$ (needing $Y \\geq t{-}1$) or $X_K = 0$ (needing $Y \\geq t$). The result is affine in $\\eta_K$ with slope $\\Pr(Y = t{-}1) \\geq 0$.\n\\end{proof}\n\n\\begin{remark}[Pivotal Voter Interpretation]\nThe slope $\\Pr(Y = t{-}1)$ is exactly the probability that judge $K$ is \\emph{pivotal}: the remaining $K{-}1$ judges produce exactly $t{-}1$ failures, and judge $K$'s outcome determines the panel decision. Monotonicity holds because a judge can only tip the panel toward compromise (by failing), never away from it.\n\\end{remark}\n\n\n%% ================================================================\n\\section{Main Result: Correlated Judges, Adaptive Adversary}\n%% ================================================================\n\n\\begin{theorem}[Weakest-Link Monotonicity]\\label{thm:main}\nLet $\\mathcal{P} = \\{J_1, \\ldots, J_{K-1}, J_K\\}$ and $\\mathcal{P}' = \\{J_1, \\ldots, J_{K-1}, J_K'\\}$ be two panels using majority vote with threshold $t = \\lceil K/2 \\rceil$, sharing judges $J_1, \\ldots, J_{K-1}$ and satisfying Definition~\\ref{def:dominance} (pointwise vulnerability dominance of $J_K'$ over $J_K$). Then:\n\\begin{enumerate}[label=(\\alph*)]\n    \\item For every fixed attack $a \\in \\mathcal{A}$:\n    \\[\n        \\mathrm{ASR}(\\mathcal{P}', a) \\;\\geq\\; \\mathrm{ASR}(\\mathcal{P}, a).\n    \\]\n    \\item For any adversary strategy, including an adaptive adversary:\n    \\[\n        \\mathrm{ASR}^*(\\mathcal{P}') \\;\\geq\\; \\mathrm{ASR}^*(\\mathcal{P}).\n    \\]\n\\end{enumerate}\nIn particular, replacing the weakest panel member with a more vulnerable judge (increasing $\\eta_{\\max}$) cannot decrease the panel ASR.\n\\end{theorem}\n\n\\begin{proof}\n\\textbf{Part (a): Fixed attack.}\nFix an arbitrary attack $a \\in \\mathcal{A}$. Let $\\mathbf{x}_{-K} = (x_1, \\ldots, x_{K-1}) \\in \\{0,1\\}^{K-1}$ denote a realization of the shared judges' outcomes, and let $s = \\sum_{j=1}^{K-1} x_j$. By the law of total probability:\n\\begin{equation}\\label{eq:total-prob}\n    \\mathrm{ASR}(\\mathcal{P}, a)\n    \\;=\\; \\sum_{\\mathbf{x}_{-K} \\in \\{0,1\\}^{K-1}} \\Pr(\\mathbf{X}_{-K}^a = \\mathbf{x}_{-K})\\;\\cdot\\; \\Pr\\!\\bigl(s + X_K^a \\geq t \\;\\big|\\; \\mathbf{X}_{-K}^a = \\mathbf{x}_{-K}\\bigr).\n\\end{equation}\nSince $X_K^a \\in \\{0,1\\}$, the inner probability depends on $s$ in exactly three cases:\n\\begin{itemize}\n    \\item \\textbf{Case $s \\geq t$:} The panel is compromised regardless of $X_K^a$. Both panels contribute~$1$.\n    \\item \\textbf{Case $s = t{-}1$:} The panel is compromised iff $X_K^a = 1$ (resp.\\ $X_{K'}^a = 1$). By pointwise dominance:\n    \\[\n        \\Pr(X_{K'}^a = 1 \\mid \\mathbf{x}_{-K}) \\;\\geq\\; \\Pr(X_K^a = 1 \\mid \\mathbf{x}_{-K}).\n    \\]\n    \\item \\textbf{Case $s \\leq t{-}2$:} Even with $X_K^a = 1$, the total $s + 1 \\leq t{-}1 < t$. Neither panel is compromised; both contribute~$0$.\n\\end{itemize}\nSince the marginal distribution of $\\mathbf{X}_{-K}^a$ is identical in both panels (Definition~\\ref{def:dominance}), summing over all realizations yields\n\\begin{equation}\\label{eq:pointwise-ineq}\n    \\mathrm{ASR}(\\mathcal{P}', a) \\;\\geq\\; \\mathrm{ASR}(\\mathcal{P}, a).\n\\end{equation}\n\n\\medskip\n\\noindent\\textbf{Part (b): Adaptive adversary.}\nTaking the supremum over all attacks and applying \\eqref{eq:pointwise-ineq}:\n\\[\n    \\mathrm{ASR}^*(\\mathcal{P}')\n    \\;=\\; \\sup_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}', a)\n    \\;\\geq\\; \\sup_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)\n    \\;=\\; \\mathrm{ASR}^*(\\mathcal{P}),\n\\]\nsince each term in the supremum on the right is bounded by the corresponding term on the left. \\qedhere\n\\end{proof}\n\n\\begin{remark}[Generality of the Result]\nThree aspects of Theorem~\\ref{thm:main} merit emphasis:\n\\begin{enumerate}[label=(\\roman*)]\n    \\item \\textbf{Arbitrary correlations.} The proof makes no independence assumption. Judges may exhibit arbitrary failure correlations---including those induced by shared architectural vulnerabilities, common training data, or attack transfer effects---as long as pointwise dominance holds.\n    \\item \\textbf{Threshold generality.} The proof uses only the threshold structure of majority vote. It extends verbatim to any $t$-out-of-$K$ aggregation rule, including unanimity ($t = K$) and any-judge-fails ($t = 1$).\n    \\item \\textbf{Adversary generality.} Part (b) holds for any adversary class that selects from the same attack space $\\mathcal{A}$, including randomized adversaries (who select a distribution over $\\mathcal{A}$, since a mixture preserves the pointwise inequality).\n\\end{enumerate}\n\\end{remark}\n\n\\begin{remark}[Sufficient Conditions for Pointwise Dominance]\nPointwise dominance (Definition~\\ref{def:dominance}) is satisfied whenever:\n\\begin{enumerate}[label=(\\roman*)]\n    \\item \\textbf{Model capability ordering.} $J_K'$ has strictly lower capability than $J_K$ on all tasks, so any attack that fools $J_K$ also fools $J_K'$, and $J_K'$ is vulnerable to additional attacks.\n    \\item \\textbf{Vulnerability superset.} The set of inputs on which $J_K'$ errs is a superset of those on which $J_K$ errs, for every attack.\n    \\item \\textbf{Conditional independence.} If $X_K^a \\perp \\mathbf{X}_{-K}^a$ for all $a$, then pointwise dominance reduces to $\\eta_{K'}(a) \\geq \\eta_K(a)$ for all $a$ (marginal dominance), which is empirically verifiable by measuring individual ASR.\n\\end{enumerate}\n\\end{remark}\n\n\\begin{remark}[Coupling Interpretation]\nAn equivalent proof uses a coupling argument: construct $(X_K^a, X_{K'}^a)$ on a common probability space such that $X_{K'}^a \\geq X_K^a$ almost surely (feasible by the standard coupling for stochastic dominance whenever pointwise dominance holds). Then $\\sum_{j=1}^{K-1} X_j^a + X_{K'}^a \\geq \\sum_{j=1}^{K-1} X_j^a + X_K^a$ pointwise, so $\\{$panel~$\\mathcal{P}$ fails$\\} \\subseteq \\{$panel~$\\mathcal{P}'$ fails$\\}$ and $\\mathrm{ASR}(\\mathcal{P}', a) \\geq \\mathrm{ASR}(\\mathcal{P}, a)$.\n\\end{remark}\n\n\n%% ================================================================\n\\section{Tightness and Bounds}\n%% ================================================================\n\n\\begin{proposition}[Equality Conditions]\\label{prop:tight}\nUnder the conditions of Theorem~\\ref{thm:main}, for a fixed attack $a$:\n\\[\n    \\mathrm{ASR}(\\mathcal{P}', a) = \\mathrm{ASR}(\\mathcal{P}, a)\n\\]\nif and only if, for every realization $\\mathbf{x}_{-K}$ with $\\sum x_j = t{-}1$ and $\\Pr(\\mathbf{X}_{-K}^a = \\mathbf{x}_{-K}) > 0$:\n\\[\n    \\Pr(X_{K'}^a = 1 \\mid \\mathbf{x}_{-K}) \\;=\\; \\Pr(X_K^a = 1 \\mid \\mathbf{x}_{-K}).\n\\]\nFor conditionally independent judges, this simplifies to: either $\\Pr(Y = t{-}1) = 0$ (no pivotal configuration exists) or $\\eta_{K'}(a) = \\eta_K(a)$.\n\\end{proposition}\n\n\\begin{proof}\nFrom the proof of Theorem~\\ref{thm:main}, the ASR difference is:\n\\begin{align*}\n    \\Delta\n    &= \\mathrm{ASR}(\\mathcal{P}', a) - \\mathrm{ASR}(\\mathcal{P}, a) \\\\\n    &= \\!\\!\\sum_{\\substack{\\mathbf{x}_{-K}:\\, s = t-1}}\\!\\! \\Pr(\\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K})\\,\\bigl[\\Pr(X_{K'}^a {=} 1 \\mid \\mathbf{x}_{-K}) - \\Pr(X_K^a {=} 1 \\mid \\mathbf{x}_{-K})\\bigr].\n\\end{align*}\nEach summand is non-negative (pointwise dominance ensures the bracket is $\\geq 0$; the probability weight is $\\geq 0$). The sum vanishes iff every summand with positive weight has a zero bracket. Under conditional independence, $\\Pr(X_K^a = 1 \\mid \\mathbf{x}_{-K}) = \\eta_K(a)$ is constant across realizations, so the condition collapses to $\\eta_{K'}(a) = \\eta_K(a)$ or the event $\\{Y = t{-}1\\}$ having zero probability.\n\\end{proof}\n\n\\begin{remark}\nThe condition $\\Pr(Y = t{-}1) = 0$ is degenerate: it requires all $\\eta_j \\in \\{0,1\\}$ with the count of $\\eta_j = 1$ never equaling $t{-}1$. In all non-degenerate panels, the monotonicity is \\emph{strict} whenever $\\eta_{K'} > \\eta_K$ under some attack.\n\\end{remark}\n\n\\begin{proposition}[Panel ASR Bounds]\\label{prop:bounds}\nFor a panel of $K$ conditionally independent judges with ordered vulnerabilities $\\eta_{(1)} \\leq \\cdots \\leq \\eta_{(K)} = \\eta_{\\max}$ under a fixed attack:\n\\[\n    \\prod_{j=K-t+1}^{K} \\eta_{(j)} \\;\\leq\\; \\mathrm{ASR} \\;\\leq\\; \\sum_{k=t}^{K} \\binom{K}{k}\\, \\eta_{\\max}^{\\,k}\\, (1-\\eta_{\\max})^{K-k}.\n\\]\n\\end{proposition}\n\n\\begin{proof}\n\\textit{Lower bound.}\nThe event that the $t$ most vulnerable judges ($J_{(K-t+1)}, \\ldots, J_{(K)}$) all fail implies panel compromise. By independence:\n\\[\n    \\mathrm{ASR} \\;\\geq\\; \\Pr\\!\\bigl(\\textstyle\\bigcap_{j=K-t+1}^K \\{X_{(j)} = 1\\}\\bigr) \\;=\\; \\prod_{j=K-t+1}^{K} \\eta_{(j)}.\n\\]\n\n\\textit{Upper bound.}\nSince $\\eta_j \\leq \\eta_{\\max}$ for all $j$, replacing each $\\eta_j$ with $\\eta_{\\max}$ increases ASR by Lemma~\\ref{lem:general-indep} (applied iteratively to each judge). The resulting panel has i.i.d.\\ $\\mathrm{Bernoulli}(\\eta_{\\max})$ failures, giving the binomial tail.\n\\end{proof}\n\n\\begin{remark}[Scaling Regimes]\nFor small $\\eta_{\\max}$ and fixed $K$, the leading-order behavior is:\n\\begin{itemize}\n    \\item If the top $t$ vulnerabilities satisfy $\\eta_{(j)} = \\Theta(\\eta_{\\max})$ for $j \\geq K{-}t{+}1$: \\[ \\mathrm{ASR} \\;=\\; \\Theta\\!\\bigl(\\eta_{\\max}^{\\,t}\\bigr). \\]\n    Majority vote provides a $t$-th power suppression relative to the individual maximum.\n    \\item If the vulnerability distribution is \\emph{heavy-tailed} (one judge much weaker than the rest): the lower bound $\\prod \\eta_{(j)}$ is small, but the adversary can still exploit correlated failures (attack transfer) to push ASR closer to $\\binom{K}{t}\\eta_{\\max}^t$.\n    \\item For $K=3$, $t=2$: $\\mathrm{ASR} = \\Theta(\\eta_{\\max}^2)$ in the small-vulnerability regime.\n\\end{itemize}\n\\end{remark}\n\n\n%% ================================================================\n\\section{Corollary: Panel Design}\n%% ================================================================\n\n\\begin{corollary}[Robustness-First Design Principle]\\label{cor:design}\nUnder the adaptive adversary model of Definition~\\ref{def:adversary}, the optimal panel selection strategy is \\emph{robustness-first}:\n\\begin{enumerate}[label=\\textbf{Stage~\\arabic*}:]\n    \\item \\textbf{Robustness screening.} From the candidate pool, retain only judges satisfying $\\eta_j \\leq \\tau$ for a robustness threshold $\\tau$. By Theorem~\\ref{thm:main}, replacing any judge with $\\eta_j > \\tau$ by one with $\\eta_j \\leq \\tau$ weakly reduces panel ASR.\n    \\item \\textbf{Diversity maximization.} Among the retained judges, select the $K$-judge panel that maximizes effective independence $K_{\\mathrm{eff}}$ (or any suitable diversity measure). This provides residual protection against broad-spectrum attacks without introducing weak links.\n\\end{enumerate}\nThe ordering is essential: diversity maximization without robustness screening may increase $\\eta_{\\max}$ via the diversity-capability tradeoff, which by Theorem~\\ref{thm:main} weakly increases panel ASR.\n\\end{corollary}\n\n\\begin{proof}\nStage~1 is a direct application of Theorem~\\ref{thm:main}: if $J_K$ has $\\eta_K > \\tau$ and $J_K'$ has $\\eta_{K'} \\leq \\tau < \\eta_K$, and $J_K'$ satisfies pointwise dominance of $J_K$ over $J_K'$ (i.e., $J_K$ is pointwise more vulnerable than $J_K'$), then $\\mathrm{ASR}^*(\\mathcal{P}) \\geq \\mathrm{ASR}^*(\\mathcal{P}')$. The robustness constraint $\\eta_j \\leq \\tau$ for all panel members ensures $\\eta_{\\max} \\leq \\tau$, bounding the dominant predictor.\n\nStage~2 is a secondary optimization: given $\\eta_{\\max} \\leq \\tau$, the residual variance in panel ASR is determined by inter-judge correlations and the specific attack-type vulnerability distribution. Maximizing $K_{\\mathrm{eff}}$ provides protection in the regime where attacks exploit shared biases (broad-spectrum attacks), as the SDPI bound gives $\\mathrm{ASR} \\leq K_{\\mathrm{eff}} \\cdot \\eta_{\\max}$.\n\nThe ordering matters because the diversity-capability tradeoff ($r \\approx -0.78$, $p < 0.001$ empirically) implies that panels selected for maximal diversity tend to include weaker judges. By Theorem~\\ref{thm:main}, the resulting increase in $\\eta_{\\max}$ dominates any benefit from increased independence.\n\\end{proof}\n\n\n%% ================================================================\n\\section{Connection to Empirical Results}\n%% ================================================================\n\n\\begin{remark}[Empirical Validation]\nTheorem~\\ref{thm:main} makes a testable prediction: in a multivariate regression $\\log(\\mathrm{ASR}) \\sim \\beta_1 \\log(\\eta_{\\max}) + \\beta_2 \\log(K_{\\mathrm{eff}})$, $\\eta_{\\max}$ should be a significant predictor ($\\beta_1 > 0$) while $K_{\\mathrm{eff}}$ should be weak or non-significant ($\\beta_2 \\approx 0$), because the theorem establishes monotonicity in $\\eta_{\\max}$ but not in $K_{\\mathrm{eff}}$.\n\nAcross 12 experimental conditions (2 benchmarks $\\times$ 6 attack types):\n\\begin{itemize}\n    \\item $\\eta_{\\max}$ is significant (BH-FDR $q < 0.05$) in 6/12 conditions (50\\%), with 3/12 surviving Bonferroni correction.\n    \\item $K_{\\mathrm{eff}}$ is significant in only 1/12 conditions (8\\%). Residualized $K_{\\mathrm{eff}}$ (orthogonalized against $\\eta_{\\max}$, VIF $= 1.04$) confirms this is not a collinearity artifact.\n    \\item The sole exception (ARC $\\times$ sycophancy, $\\beta_2 = -2.85$, $p = 0.003$) corresponds to the one attack type that exploits a \\emph{shared} judge bias rather than targeting individual vulnerabilities---the ``BFT-like'' regime where faults are approximately random.\n\\end{itemize}\nThis pattern is precisely what Theorem~\\ref{thm:main} predicts: monotonicity in $\\eta_{\\max}$ drives the primary effect, and $K_{\\mathrm{eff}}$ matters only when the adversary cannot selectively target the weakest judge.\n\\end{remark}\n\n\\begin{remark}[When Diversity Helps]\nTheorem~\\ref{thm:main} does \\emph{not} claim diversity is useless. It establishes that \\emph{reducing $\\eta_{\\max}$ weakly dominates increasing $K_{\\mathrm{eff}}$} as a defense strategy. Diversity retains value in three regimes:\n\\begin{enumerate}[label=(\\roman*)]\n    \\item \\textbf{Controlled $\\eta_{\\max}$:} When all judges exceed a robustness threshold (Corollary~\\ref{cor:design}, Stage~2), higher $K_{\\mathrm{eff}}$ reduces the ASR ceiling via the SDPI bound $\\mathrm{ASR} \\leq K_{\\mathrm{eff}} \\cdot \\eta_{\\max}$.\n    \\item \\textbf{Broad-spectrum attacks:} When attacks exploit biases shared across judges (sycophancy, position bias), failures approximate random faults and the BFT analogy holds.\n    \\item \\textbf{Non-adversarial settings:} For calibration, bias reduction, and inter-rater agreement, diversity provides standard statistical benefits unrelated to adversarial robustness.\n\\end{enumerate}\n\\end{remark}\n\n\n\\end{document}\n",
      "numLines": 322,
      "startLine": 1,
      "totalLines": 322
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01EbKRD3SoZPMDA6m5EGajWt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "uuid": "e85549a6-36b8-4f35-9449-5cfbeb7e4e99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7PYrTWAZCxPpP7vFaw7TU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12976,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12976
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

_source line 8 · 2026-05-22T15:12:23.323Z_

<details><summary>↩ Tool result · `toolu_01EbKRD3SoZPMDA6m5EGajWt`</summary>

```text
1	\section{Threat Model and Problem Formulation}
2	% [PLACEHOLDER — to be written by Worker]
3	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "uuid": "7540e5d1-caf1-402e-b468-65f6b4afb3e1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex",
      "content": "\\section{Threat Model and Problem Formulation}\n% [PLACEHOLDER — to be written by Worker]\n",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
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
Now I have all the information I need. Let me write the Threat Model and Problem Formulation section based on the theorem proof file and the task requirements.

Key elements to include:
1. Panel and majority vote setup
2. Effective independence K_eff
3. Adaptive adversary definition (in definition environment)
4. Weakest-Link Monotonicity Theorem (in theorem environment, label: thm:monotonicity)
5. Testable prediction

Let me write this carefully, keeping it to ~0.5 page (400-500 words), compact paragraphs.


I need to make sure the theorem label is exactly `\label{thm:monotonicity}` as specified in the task, since the Related Work section already references it.

Writing the section now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "uuid": "47a6f68e-5c8c-423e-b637-5ec684a1762f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBu8Zc3J4YoFtz9UpxVp7m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9276,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9276
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

Now I'll write the section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "uuid": "8448df70-6c65-44f6-bec0-80c4330ab9fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBu8Zc3J4YoFtz9UpxVp7m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9276,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9276
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

<details open><summary>🔧 Tool call — Write · `toolu_015JGzHaJwurJ3ruKddFWsZX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex",
  "content": "\\section{Threat Model and Problem Formulation}\n\nA \\emph{panel} $\\mathcal{P} = \\{J_1, \\ldots, J_K\\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \\lceil K/2 \\rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised independently with probability $\\eta_j(a) = \\Pr(X_j^a = 1)$, where $X_j^a \\in \\{0,1\\}$ denotes the failure indicator. We write $\\eta_{\\max} = \\max_j \\eta_j$ for the vulnerability of the weakest judge. The \\emph{panel attack success rate} is $\\mathrm{ASR}(\\mathcal{P}, a) = \\Pr\\!\\bigl(\\sum_{j=1}^K X_j^a \\geq t\\bigr)$.\n\nTo quantify diversity, we derive the \\emph{effective independence} $K_{\\mathrm{eff}}$ from the eigenspectrum of the pairwise mutual-information matrix $\\mathbf{M}$ among judges. Let $\\lambda_1, \\ldots, \\lambda_K$ be the eigenvalues of $\\mathbf{M}$; then $K_{\\mathrm{eff}} = (\\sum_i \\lambda_i)^2 / \\sum_i \\lambda_i^2$. This quantity ranges from $K_{\\mathrm{eff}} = K$ (fully independent judges) to $K_{\\mathrm{eff}} = 1$ (perfectly correlated judges). Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies $\\eta_{\\mathrm{joint}} \\leq K_{\\mathrm{eff}} \\cdot \\eta_{\\max}$, suggesting that diversity should help---but this bound assumes non-adaptive faults.\n\n\\begin{definition}[Adaptive Adversary]\n\\label{def:adversary}\nAn \\emph{adaptive adversary} has full knowledge of the panel composition $\\mathcal{P}$, the per-judge vulnerability profiles $\\{\\eta_j(\\cdot)\\}_{j=1}^K$, and the inter-judge correlation structure. It selects the attack $a^* = \\arg\\max_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)$ to maximize the panel ASR, yielding $\\mathrm{ASR}^*(\\mathcal{P}) = \\sup_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)$.\n\\end{definition}\n\nThis departs from Byzantine fault-tolerance (BFT) models~\\cite{lamport1982byzantine,castro1999practical}, which assume faults are independent and randomly distributed. An adaptive adversary instead concentrates attack effort on the weakest link~\\cite{schneier2000secrets}, rendering diversity-based defenses less effective than the SDPI bound implies.\n\n\\begin{theorem}[Weakest-Link Monotonicity]\n\\label{thm:monotonicity}\nLet $\\mathcal{P}$ and $\\mathcal{P}'$ be two panels sharing $K{-}1$ judges and differing only in the $K$-th member, where $J_K'$ is pointwise more vulnerable than $J_K$ (i.e., $\\Pr(X_{K'}^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K}) \\geq \\Pr(X_K^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K})$ for all attacks $a$ and realizations $\\mathbf{x}_{-K}$). Then for any adversary, including an adaptive one: $\\mathrm{ASR}^*(\\mathcal{P}') \\geq \\mathrm{ASR}^*(\\mathcal{P})$.\n\\end{theorem}\n\n\\noindent Proof in Appendix~\\ref{app:proof}. Intuitively, the replaced judge is \\emph{pivotal} exactly when $t{-}1$ of the remaining judges have already failed; in such configurations, a more vulnerable replacement can only increase the probability of tipping the majority, never decrease it. The result holds under arbitrary inter-judge correlations and any attack space $\\mathcal{A}$.\n\nThe theorem yields a testable prediction: in a regression $\\log(\\mathrm{ASR}) \\sim \\beta_1 \\log(\\eta_{\\max}) + \\beta_2 \\log(K_{\\mathrm{eff}})$, we should observe $\\beta_1 > 0$ (significant) while $\\beta_2 \\approx 0$ (non-significant), since monotonicity is established in $\\eta_{\\max}$ but not in $K_{\\mathrm{eff}}$. Our experiments in \\S\\ref{sec:experiments} directly test this prediction across 12 conditions spanning two benchmarks and six attack types.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "uuid": "0d43504d-f90b-40fe-b172-178008299648",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBu8Zc3J4YoFtz9UpxVp7m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9276,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9276
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

_source line 12 · 2026-05-22T15:12:55.728Z_

<details><summary>↩ Tool result · `toolu_015JGzHaJwurJ3ruKddFWsZX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "uuid": "0d456f5e-603c-4f45-affa-2a094943ab24",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex",
    "content": "\\section{Threat Model and Problem Formulation}\n\nA \\emph{panel} $\\mathcal{P} = \\{J_1, \\ldots, J_K\\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \\lceil K/2 \\rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised independently with probability $\\eta_j(a) = \\Pr(X_j^a = 1)$, where $X_j^a \\in \\{0,1\\}$ denotes the failure indicator. We write $\\eta_{\\max} = \\max_j \\eta_j$ for the vulnerability of the weakest judge. The \\emph{panel attack success rate} is $\\mathrm{ASR}(\\mathcal{P}, a) = \\Pr\\!\\bigl(\\sum_{j=1}^K X_j^a \\geq t\\bigr)$.\n\nTo quantify diversity, we derive the \\emph{effective independence} $K_{\\mathrm{eff}}$ from the eigenspectrum of the pairwise mutual-information matrix $\\mathbf{M}$ among judges. Let $\\lambda_1, \\ldots, \\lambda_K$ be the eigenvalues of $\\mathbf{M}$; then $K_{\\mathrm{eff}} = (\\sum_i \\lambda_i)^2 / \\sum_i \\lambda_i^2$. This quantity ranges from $K_{\\mathrm{eff}} = K$ (fully independent judges) to $K_{\\mathrm{eff}} = 1$ (perfectly correlated judges). Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies $\\eta_{\\mathrm{joint}} \\leq K_{\\mathrm{eff}} \\cdot \\eta_{\\max}$, suggesting that diversity should help---but this bound assumes non-adaptive faults.\n\n\\begin{definition}[Adaptive Adversary]\n\\label{def:adversary}\nAn \\emph{adaptive adversary} has full knowledge of the panel composition $\\mathcal{P}$, the per-judge vulnerability profiles $\\{\\eta_j(\\cdot)\\}_{j=1}^K$, and the inter-judge correlation structure. It selects the attack $a^* = \\arg\\max_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)$ to maximize the panel ASR, yielding $\\mathrm{ASR}^*(\\mathcal{P}) = \\sup_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)$.\n\\end{definition}\n\nThis departs from Byzantine fault-tolerance (BFT) models~\\cite{lamport1982byzantine,castro1999practical}, which assume faults are independent and randomly distributed. An adaptive adversary instead concentrates attack effort on the weakest link~\\cite{schneier2000secrets}, rendering diversity-based defenses less effective than the SDPI bound implies.\n\n\\begin{theorem}[Weakest-Link Monotonicity]\n\\label{thm:monotonicity}\nLet $\\mathcal{P}$ and $\\mathcal{P}'$ be two panels sharing $K{-}1$ judges and differing only in the $K$-th member, where $J_K'$ is pointwise more vulnerable than $J_K$ (i.e., $\\Pr(X_{K'}^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K}) \\geq \\Pr(X_K^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K})$ for all attacks $a$ and realizations $\\mathbf{x}_{-K}$). Then for any adversary, including an adaptive one: $\\mathrm{ASR}^*(\\mathcal{P}') \\geq \\mathrm{ASR}^*(\\mathcal{P})$.\n\\end{theorem}\n\n\\noindent Proof in Appendix~\\ref{app:proof}. Intuitively, the replaced judge is \\emph{pivotal} exactly when $t{-}1$ of the remaining judges have already failed; in such configurations, a more vulnerable replacement can only increase the probability of tipping the majority, never decrease it. The result holds under arbitrary inter-judge correlations and any attack space $\\mathcal{A}$.\n\nThe theorem yields a testable prediction: in a regression $\\log(\\mathrm{ASR}) \\sim \\beta_1 \\log(\\eta_{\\max}) + \\beta_2 \\log(K_{\\mathrm{eff}})$, we should observe $\\beta_1 > 0$ (significant) while $\\beta_2 \\approx 0$ (non-significant), since monotonicity is established in $\\eta_{\\max}$ but not in $K_{\\mathrm{eff}}$. Our experiments in \\S\\ref{sec:experiments} directly test this prediction across 12 conditions spanning two benchmarks and six attack types.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 2,
        "newStart": 1,
        "newLines": 21,
        "lines": [
          " \\section{Threat Model and Problem Formulation}",
          "-% [PLACEHOLDER — to be written by Worker]",
          "+",
          "+A \\emph{panel} $\\mathcal{P} = \\{J_1, \\ldots, J_K\\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \\lceil K/2 \\rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised independently with probability $\\eta_j(a) = \\Pr(X_j^a = 1)$, where $X_j^a \\in \\{0,1\\}$ denotes the failure indicator. We write $\\eta_{\\max} = \\max_j \\eta_j$ for the vulnerability of the weakest judge. The \\emph{panel attack success rate} is $\\mathrm{ASR}(\\mathcal{P}, a) = \\Pr\\!\\bigl(\\sum_{j=1}^K X_j^a \\geq t\\bigr)$.",
          "+",
          "+To quantify diversity, we derive the \\emph{effective independence} $K_{\\mathrm{eff}}$ from the eigenspectrum of the pairwise mutual-information matrix $\\mathbf{M}$ among judges. Let $\\lambda_1, \\ldots, \\lambda_K$ be the eigenvalues of $\\mathbf{M}$; then $K_{\\mathrm{eff}} = (\\sum_i \\lambda_i)^2 / \\sum_i \\lambda_i^2$. This quantity ranges from $K_{\\mathrm{eff}} = K$ (fully independent judges) to $K_{\\mathrm{eff}} = 1$ (perfectly correlated judges). Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies $\\eta_{\\mathrm{joint}} \\leq K_{\\mathrm{eff}} \\cdot \\eta_{\\max}$, suggesting that diversity should help---but this bound assumes non-adaptive faults.",
          "+",
          "+\\begin{definition}[Adaptive Adversary]",
          "+\\label{def:adversary}",
          "+An \\emph{adaptive adversary} has full knowledge of the panel composition $\\mathcal{P}$, the per-judge vulnerability profiles $\\{\\eta_j(\\cdot)\\}_{j=1}^K$, and the inter-judge correlation structure. It selects the attack $a^* = \\arg\\max_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)$ to maximize the panel ASR, yielding $\\mathrm{ASR}^*(\\mathcal{P}) = \\sup_{a \\in \\mathcal{A}} \\mathrm{ASR}(\\mathcal{P}, a)$.",
          "+\\end{definition}",
          "+",
          "+This departs from Byzantine fault-tolerance (BFT) models~\\cite{lamport1982byzantine,castro1999practical}, which assume faults are independent and randomly distributed. An adaptive adversary instead concentrates attack effort on the weakest link~\\cite{schneier2000secrets}, rendering diversity-based defenses less effective than the SDPI bound implies.",
          "+",
          "+\\begin{theorem}[Weakest-Link Monotonicity]",
          "+\\label{thm:monotonicity}",
          "+Let $\\mathcal{P}$ and $\\mathcal{P}'$ be two panels sharing $K{-}1$ judges and differing only in the $K$-th member, where $J_K'$ is pointwise more vulnerable than $J_K$ (i.e., $\\Pr(X_{K'}^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K}) \\geq \\Pr(X_K^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K})$ for all attacks $a$ and realizations $\\mathbf{x}_{-K}$). Then for any adversary, including an adaptive one: $\\mathrm{ASR}^*(\\mathcal{P}') \\geq \\mathrm{ASR}^*(\\mathcal{P})$.",
          "+\\end{theorem}",
          "+",
          "+\\noindent Proof in Appendix~\\ref{app:proof}. Intuitively, the replaced judge is \\emph{pivotal} exactly when $t{-}1$ of the remaining judges have already failed; in such configurations, a more vulnerable replacement can only increase the probability of tipping the majority, never decrease it. The result holds under arbitrary inter-judge correlations and any attack space $\\mathcal{A}$.",
          "+",
          "+The theorem yields a testable prediction: in a regression $\\log(\\mathrm{ASR}) \\sim \\beta_1 \\log(\\eta_{\\max}) + \\beta_2 \\log(K_{\\mathrm{eff}})$, we should observe $\\beta_1 > 0$ (significant) while $\\beta_2 \\approx 0$ (non-significant), since monotonicity is established in $\\eta_{\\max}$ but not in $K_{\\mathrm{eff}}$. Our experiments in \\S\\ref{sec:experiments} directly test this prediction across 12 conditions spanning two benchmarks and six attack types."
        ]
      }
    ],
    "originalFile": "\\section{Threat Model and Problem Formulation}\n% [PLACEHOLDER — to be written by Worker]\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 13_

已写入 `docs/paper/threat_model.tex`。~470 词，覆盖全部 5 个段落：panel/majority-vote 设置、$K_{\mathrm{eff}}$ 定义与 SDPI bound、adaptive adversary definition 环境（含 BFT 对比）、weakest-link monotonicity theorem（标签 `thm:monotonicity`，证明留 appendix，含 pivotal voter 直觉）、testable prediction 连接实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "uuid": "f3344298-518b-44c2-8cb2-dc0f6c8b0991",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdTJWyauGjrxuPXMzTnRmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1691,
      "cache_read_input_tokens": 34093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1691
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

_source line 14_

已写入 `docs/paper/threat_model.tex`。~470 词，覆盖全部 5 个段落：panel/majority-vote 设置、$K_{\mathrm{eff}}$ 定义与 SDPI bound、adaptive adversary definition 环境（含 BFT 对比）、weakest-link monotonicity theorem（标签 `thm:monotonicity`，证明留 appendix，含 pivotal voter 直觉）、testable prediction 连接实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 43180,
  "duration_api_ms": 44237,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "6df10c67-8bea-4038-97b7-2f90845c6520",
  "total_cost_usd": 0.23564724999999997,
  "usage": {
    "input_tokens": 4,
    "cache_creation_input_tokens": 23943,
    "cache_read_input_tokens": 70751,
    "output_tokens": 1948,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 23943,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 134,
        "cache_read_input_tokens": 34093,
        "cache_creation_input_tokens": 1691,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1691
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1823,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001908,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4,
      "outputTokens": 1948,
      "cacheReadInputTokens": 70751,
      "cacheCreationInputTokens": 23943,
      "webSearchRequests": 0,
      "costUSD": 0.23373924999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9c7fcad6-bce4-4606-888d-35e655fab2ab"
}
```

</details>

---
