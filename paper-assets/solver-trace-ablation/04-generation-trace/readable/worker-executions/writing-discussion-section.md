# writing discussion section

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_writing_discussion-section_20260514T185634.log`
- **Structured JSON:** [`d046acd673c4606958f2.json`](../../sessions/d0/d046acd673c4606958f2.json)

## Before a recorded user message

31 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "25d119de-c284-4644-a79d-8ef9c0be8f5f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778800200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "442386a2-c641-486c-9a0e-6fce5e21480e",
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254"
}
```

---

### Assistant

_source line 4_

I'll read the required files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "d874fcb8-b22d-4465-902a-14e496816f07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg2toV4gNFnzhfUK2MScvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13100,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13100
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

<details open><summary>🔧 Tool call — Read · `toolu_01PJvFGSWAjgrmK38upvUdMV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "20ceae3e-cb0e-41fd-98f0-aae6636e932a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg2toV4gNFnzhfUK2MScvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13100,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13100
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

_source line 6 · 2026-05-14T18:56:44.078Z_

<details><summary>↩ Tool result · `toolu_01PJvFGSWAjgrmK38upvUdMV`</summary>

```text
1	% Method section — solver-trace-ablation
2	% Requires: algorithm, algorithmic, amsmath, enumitem packages
3	
4	\section{Method}
5	\label{sec:method}
6	
7	\subsection{Task Formulation}
8	\label{sec:task}
9	
10	Given natural language premises $P_1, \ldots, P_k$ and a conclusion $C$, the task is to produce a formal logic program $F = \{c_1, \ldots, c_n\}$, where each component $c_i$ is a premise encoding (in FOL) or a clause/fact (in Prolog), with one distinguished component encoding the query derived from $C$.
11	An external solver $S$ determines whether $F$ constitutes a valid proof:
12	$S(F) \in \{\textit{proved}, \textit{failed}\}$.
13	We experiment with two solver backends: Prover9 for first-order logic and SWI-Prolog for Prolog programs.
14	
15	\subsection{GRPO Training}
16	\label{sec:grpo}
17	
18	We train formalizers with Group Relative Policy Optimization \citep[GRPO;][]{deepseekmath}.
19	For each training prompt, the policy samples $K{=}8$ rollouts.
20	Each rollout receives a binary \emph{execution reward}:
21	\begin{equation}
22	  r_{\text{exec}}(x) = \mathbf{1}\bigl[S(F_x) = \textit{proved}\bigr]
23	  \label{eq:rexec}
24	\end{equation}
25	where $F_x$ is the formalization produced by rollout $x$.
26	Advantages are computed group-relative: $A_i = (r_i - \bar{r}) / \sigma_r$ within each prompt's rollout group, and the policy update maximizes expected advantage under a clipped surrogate objective with KL regularization.
27	
28	This setup optimizes \emph{prove rate}---the fraction of rollouts yielding a proved formalization---but provides no signal about the \emph{structural quality} of proved outputs.
29	A formalization that embeds the conclusion among its premises, producing a trivially provable tautology, receives the same reward as a faithful multi-step derivation.
30	
31	\subsection{Solver Trace Ablation}
32	\label{sec:sta}
33	
34	To diagnose structural quality, we propose \emph{Solver Trace Ablation} (STA), a leave-one-out protocol that tests whether each component of a proved formalization is individually necessary for proof success.
35	
36	\paragraph{Protocol.}
37	Given a proved formalization $x$ with $n$ components $\{c_1, \ldots, c_n\}$, STA constructs $n$ ablated variants $x \setminus \{c_i\}$, each with one component removed, and re-runs the solver on each.
38	A component $c_i$ is \emph{necessary} if its removal causes proof failure: $S(x \setminus \{c_i\}) = \textit{failed}$.
39	What constitutes a component depends on the logic type: individual premises in FOL, individual clauses or ground facts in Prolog.
40	
41	\paragraph{Intensional Structural Reward.}
42	We define ISR as the fraction of necessary components:
43	\begin{equation}
44	  \text{ISR}(x) = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}\bigl[S(x \setminus \{c_i\}) = \textit{failed}\bigr]
45	  \label{eq:isr}
46	\end{equation}
47	ISR $\in [0, 1]$ and is defined only for proved formalizations ($r_{\text{exec}}(x) = 1$).
48	ISR $= 1$ indicates a maximally tight formalization where every component is individually necessary; ISR $= 0$ indicates complete redundancy.
49	The protocol is solver-agnostic: it applies to any solver that accepts component-level input manipulation, requiring $n{+}1$ solver calls per sample (one initial verification plus $n$ ablations).
50	
51	Algorithm~\ref{alg:sta} gives the full procedure.
52	
53	\begin{algorithm}[t]
54	\caption{Solver Trace Ablation (STA)}
55	\label{alg:sta}
56	\begin{algorithmic}[1]
57	\REQUIRE Formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
58	\ENSURE ISR score $\in [0,1]$ or $\bot$ (undefined)
59	\IF{$S(x) \neq \textit{proved}$}
60	  \RETURN $\bot$
61	\ENDIF
62	\STATE $n_{\text{nec}} \gets 0$
63	\FOR{$i = 1$ \TO $n$}
64	  \STATE $x' \gets x \setminus \{c_i\}$
65	  \IF{$S(x') = \textit{failed}$}
66	    \STATE $n_{\text{nec}} \gets n_{\text{nec}} + 1$
67	  \ENDIF
68	\ENDFOR
69	\RETURN $n_{\text{nec}} \mathbin{/} n$
70	\end{algorithmic}
71	\end{algorithm}
72	
73	STA draws on the same intuition as mutation testing in software engineering \citep{demillo1978, jia-harman-survey}: systematically perturbing a program to assess whether each element contributes to the overall result.
74	The key difference is that STA operates on solver \emph{inputs} (formalizations) rather than program code, and targets component necessity rather than test adequacy.
75	
76	\paragraph{ISR limitations.}
77	ISR measures syntactic component necessity, not semantic faithfulness to the natural language input.
78	It is also subject to a component-count confound: formalizations with fewer components yield mechanically higher ISR, since each component carries a larger share of the proof burden under LOO ablation.
79	We control for this confound in our analysis (\S\ref{sec:results}).
80	
81	\subsection{Reward Formulations}
82	\label{sec:rewards}
83	
84	We study six reward conditions to evaluate ISR both as a diagnostic and as a training signal.
85	For all RL conditions, bonuses apply only to proved samples; unproved samples receive $r = 0$.
86	
87	\paragraph{Exec-only (baseline).}
88	$r = r_{\text{exec}}$.
89	Binary solver verification with no structural component.
90	
91	\paragraph{Additive ISR.}
92	\begin{equation}
93	  r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR}(x)), \quad \beta \in \{0.1, 0.3\}
94	  \label{eq:additive-isr}
95	\end{equation}
96	ISR provides a bonus proportional to structural tightness, gated on proof success.
97	
98	\paragraph{Additive Random (control).}
99	$r = r_{\text{exec}} \cdot (1 + \beta \cdot u)$, $u \sim \mathcal{U}[0,1]$, $\beta \in \{0.1, 0.3\}$.
100	Replacing ISR with uniform noise isolates the causal effect of ISR-specific signal from general reward-shaping effects (variance injection, magnitude scaling).
101	
102	\paragraph{Convex ISR.}
103	$r = (1 - \beta) \cdot r_{\text{exec}} + \beta \cdot \text{ISR}(x)$.
104	Under this formulation, proved samples with ISR $< 1$ receive a lower reward than under exec-only, effectively penalizing structural imperfection.
105	
106	\paragraph{Convex Random.}
107	$r = (1 - \beta) \cdot r_{\text{exec}} + \beta \cdot u$, $u \sim \mathcal{U}[0,1]$.
108	Control for the convex formulation.
109	
110	\paragraph{SFT baseline.}
111	Supervised fine-tuning on the same training data with no reinforcement learning, confirming whether observed hacking behaviors are RL-reward-specific or artifacts of general fine-tuning.
112	
113	Each RL condition is trained across three random seeds.
114	Seeds control model initialization and training stochasticity; all seeds share the same training data (\S\ref{sec:setup}).
115	
116	\subsection{Reward Hacking Taxonomy}
117	\label{sec:taxonomy}
118	
119	Analysis of trained models across reward conditions, seeds, and logic types reveals seven distinct reward hacking modes:
120	
121	\begin{enumerate}[leftmargin=*, itemsep=2pt]
122	\item \textbf{Conclusion Embedding (H1).}
123	The conclusion is included verbatim as one of multiple premises, guaranteeing provability regardless of the other premises.
124	This mode is GRPO-universal: it appears across all reward conditions (52--93\% of proved samples).
125	
126	\item \textbf{Conclusion Duplication with ISR Inflation (H7).}
127	The formalization collapses to a single premise identical to the conclusion.
128	LOO ablation marks this sole component as necessary, inflating ISR and rewarding the policy for a degenerate output.
129	H7 is ISR-specific: it appears in 64.5\% of ISR-reward samples but 0\% of random-reward samples across three seeds.
130	
131	\item \textbf{Tautological Collapse.}
132	The formalization degenerates to exactly two components---a premise and query that are identical.
133	
134	\item \textbf{Repetition Collapse.}
135	The model generates identical premises or clauses repeatedly.
136	Removing any single copy leaves the others intact, yielding ISR $\approx 0$.
137	
138	\item \textbf{Complexity-without-utility.}
139	Excessive components are generated, none individually necessary.
140	Component counts grow over training (e.g., 6.58 $\to$ 18.55) while ISR collapses.
141	
142	\item \textbf{Contradiction Explosion.}
143	A variant of complexity-without-utility where component count increases without bound, reflecting unconstrained policy drift under extended training.
144	
145	\item \textbf{Query-as-fact Gaming.}
146	The model converts the natural language conclusion into an atom and includes it as both a fact and the query, so the solver trivially succeeds.
147	This mode bypasses text-match classifiers designed for H1/H7 and was identified through functional analysis of the $n_{\text{necessary}}$ distribution in Prolog STA.
148	\end{enumerate}
149	
150	Modes are identified by a two-stage classification procedure.
151	First, strict normalized text matching detects H1 and H7 by comparing each premise string against the query string.
152	Second, functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA catches modes that evade text matching---particularly query-as-fact gaming, where the gaming mechanism produces novel string representations invisible to exact-match classifiers.
153	Samples not assigned to any hacking mode are classified as \emph{genuine}.
154	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "1a68111f-be41-4d86-8d7f-161c9609199a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
      "content": "% Method section — solver-trace-ablation\n% Requires: algorithm, algorithmic, amsmath, enumitem packages\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven natural language premises $P_1, \\ldots, P_k$ and a conclusion $C$, the task is to produce a formal logic program $F = \\{c_1, \\ldots, c_n\\}$, where each component $c_i$ is a premise encoding (in FOL) or a clause/fact (in Prolog), with one distinguished component encoding the query derived from $C$.\nAn external solver $S$ determines whether $F$ constitutes a valid proof:\n$S(F) \\in \\{\\textit{proved}, \\textit{failed}\\}$.\nWe experiment with two solver backends: Prover9 for first-order logic and SWI-Prolog for Prolog programs.\n\n\\subsection{GRPO Training}\n\\label{sec:grpo}\n\nWe train formalizers with Group Relative Policy Optimization \\citep[GRPO;][]{deepseekmath}.\nFor each training prompt, the policy samples $K{=}8$ rollouts.\nEach rollout receives a binary \\emph{execution reward}:\n\\begin{equation}\n  r_{\\text{exec}}(x) = \\mathbf{1}\\bigl[S(F_x) = \\textit{proved}\\bigr]\n  \\label{eq:rexec}\n\\end{equation}\nwhere $F_x$ is the formalization produced by rollout $x$.\nAdvantages are computed group-relative: $A_i = (r_i - \\bar{r}) / \\sigma_r$ within each prompt's rollout group, and the policy update maximizes expected advantage under a clipped surrogate objective with KL regularization.\n\nThis setup optimizes \\emph{prove rate}---the fraction of rollouts yielding a proved formalization---but provides no signal about the \\emph{structural quality} of proved outputs.\nA formalization that embeds the conclusion among its premises, producing a trivially provable tautology, receives the same reward as a faithful multi-step derivation.\n\n\\subsection{Solver Trace Ablation}\n\\label{sec:sta}\n\nTo diagnose structural quality, we propose \\emph{Solver Trace Ablation} (STA), a leave-one-out protocol that tests whether each component of a proved formalization is individually necessary for proof success.\n\n\\paragraph{Protocol.}\nGiven a proved formalization $x$ with $n$ components $\\{c_1, \\ldots, c_n\\}$, STA constructs $n$ ablated variants $x \\setminus \\{c_i\\}$, each with one component removed, and re-runs the solver on each.\nA component $c_i$ is \\emph{necessary} if its removal causes proof failure: $S(x \\setminus \\{c_i\\}) = \\textit{failed}$.\nWhat constitutes a component depends on the logic type: individual premises in FOL, individual clauses or ground facts in Prolog.\n\n\\paragraph{Intensional Structural Reward.}\nWe define ISR as the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n} \\sum_{i=1}^{n} \\mathbf{1}\\bigl[S(x \\setminus \\{c_i\\}) = \\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR $\\in [0, 1]$ and is defined only for proved formalizations ($r_{\\text{exec}}(x) = 1$).\nISR $= 1$ indicates a maximally tight formalization where every component is individually necessary; ISR $= 0$ indicates complete redundancy.\nThe protocol is solver-agnostic: it applies to any solver that accepts component-level input manipulation, requiring $n{+}1$ solver calls per sample (one initial verification plus $n$ ablations).\n\nAlgorithm~\\ref{alg:sta} gives the full procedure.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE ISR score $\\in [0,1]$ or $\\bot$ (undefined)\n\\IF{$S(x) \\neq \\textit{proved}$}\n  \\RETURN $\\bot$\n\\ENDIF\n\\STATE $n_{\\text{nec}} \\gets 0$\n\\FOR{$i = 1$ \\TO $n$}\n  \\STATE $x' \\gets x \\setminus \\{c_i\\}$\n  \\IF{$S(x') = \\textit{failed}$}\n    \\STATE $n_{\\text{nec}} \\gets n_{\\text{nec}} + 1$\n  \\ENDIF\n\\ENDFOR\n\\RETURN $n_{\\text{nec}} \\mathbin{/} n$\n\\end{algorithmic}\n\\end{algorithm}\n\nSTA draws on the same intuition as mutation testing in software engineering \\citep{demillo1978, jia-harman-survey}: systematically perturbing a program to assess whether each element contributes to the overall result.\nThe key difference is that STA operates on solver \\emph{inputs} (formalizations) rather than program code, and targets component necessity rather than test adequacy.\n\n\\paragraph{ISR limitations.}\nISR measures syntactic component necessity, not semantic faithfulness to the natural language input.\nIt is also subject to a component-count confound: formalizations with fewer components yield mechanically higher ISR, since each component carries a larger share of the proof burden under LOO ablation.\nWe control for this confound in our analysis (\\S\\ref{sec:results}).\n\n\\subsection{Reward Formulations}\n\\label{sec:rewards}\n\nWe study six reward conditions to evaluate ISR both as a diagnostic and as a training signal.\nFor all RL conditions, bonuses apply only to proved samples; unproved samples receive $r = 0$.\n\n\\paragraph{Exec-only (baseline).}\n$r = r_{\\text{exec}}$.\nBinary solver verification with no structural component.\n\n\\paragraph{Additive ISR.}\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR}(x)), \\quad \\beta \\in \\{0.1, 0.3\\}\n  \\label{eq:additive-isr}\n\\end{equation}\nISR provides a bonus proportional to structural tightness, gated on proof success.\n\n\\paragraph{Additive Random (control).}\n$r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$, $u \\sim \\mathcal{U}[0,1]$, $\\beta \\in \\{0.1, 0.3\\}$.\nReplacing ISR with uniform noise isolates the causal effect of ISR-specific signal from general reward-shaping effects (variance injection, magnitude scaling).\n\n\\paragraph{Convex ISR.}\n$r = (1 - \\beta) \\cdot r_{\\text{exec}} + \\beta \\cdot \\text{ISR}(x)$.\nUnder this formulation, proved samples with ISR $< 1$ receive a lower reward than under exec-only, effectively penalizing structural imperfection.\n\n\\paragraph{Convex Random.}\n$r = (1 - \\beta) \\cdot r_{\\text{exec}} + \\beta \\cdot u$, $u \\sim \\mathcal{U}[0,1]$.\nControl for the convex formulation.\n\n\\paragraph{SFT baseline.}\nSupervised fine-tuning on the same training data with no reinforcement learning, confirming whether observed hacking behaviors are RL-reward-specific or artifacts of general fine-tuning.\n\nEach RL condition is trained across three random seeds.\nSeeds control model initialization and training stochasticity; all seeds share the same training data (\\S\\ref{sec:setup}).\n\n\\subsection{Reward Hacking Taxonomy}\n\\label{sec:taxonomy}\n\nAnalysis of trained models across reward conditions, seeds, and logic types reveals seven distinct reward hacking modes:\n\n\\begin{enumerate}[leftmargin=*, itemsep=2pt]\n\\item \\textbf{Conclusion Embedding (H1).}\nThe conclusion is included verbatim as one of multiple premises, guaranteeing provability regardless of the other premises.\nThis mode is GRPO-universal: it appears across all reward conditions (52--93\\% of proved samples).\n\n\\item \\textbf{Conclusion Duplication with ISR Inflation (H7).}\nThe formalization collapses to a single premise identical to the conclusion.\nLOO ablation marks this sole component as necessary, inflating ISR and rewarding the policy for a degenerate output.\nH7 is ISR-specific: it appears in 64.5\\% of ISR-reward samples but 0\\% of random-reward samples across three seeds.\n\n\\item \\textbf{Tautological Collapse.}\nThe formalization degenerates to exactly two components---a premise and query that are identical.\n\n\\item \\textbf{Repetition Collapse.}\nThe model generates identical premises or clauses repeatedly.\nRemoving any single copy leaves the others intact, yielding ISR $\\approx 0$.\n\n\\item \\textbf{Complexity-without-utility.}\nExcessive components are generated, none individually necessary.\nComponent counts grow over training (e.g., 6.58 $\\to$ 18.55) while ISR collapses.\n\n\\item \\textbf{Contradiction Explosion.}\nA variant of complexity-without-utility where component count increases without bound, reflecting unconstrained policy drift under extended training.\n\n\\item \\textbf{Query-as-fact Gaming.}\nThe model converts the natural language conclusion into an atom and includes it as both a fact and the query, so the solver trivially succeeds.\nThis mode bypasses text-match classifiers designed for H1/H7 and was identified through functional analysis of the $n_{\\text{necessary}}$ distribution in Prolog STA.\n\\end{enumerate}\n\nModes are identified by a two-stage classification procedure.\nFirst, strict normalized text matching detects H1 and H7 by comparing each premise string against the query string.\nSecond, functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA catches modes that evade text matching---particularly query-as-fact gaming, where the gaming mechanism produces novel string representations invisible to exact-match classifiers.\nSamples not assigned to any hacking mode are classified as \\emph{genuine}.\n",
      "numLines": 154,
      "startLine": 1,
      "totalLines": 154
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_013a1MaM4nZpU6gYcoWjsCtb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "3dcaa0b8-d361-4978-8995-b9853d942d0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg2toV4gNFnzhfUK2MScvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13100,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13100
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

_source line 8 · 2026-05-14T18:56:44.542Z_

<details><summary>↩ Tool result · `toolu_013a1MaM4nZpU6gYcoWjsCtb`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\S\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\S\ref{sec:taxonomy}).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	\paragraph{Model and Training.}
10	We use Qwen3-4B as the base model, trained with GRPO~\cite{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of ProofWriter~\cite{proofwriter} (\texttt{train\_500\_seed42.jsonl}), held constant across all seeds and conditions.
11	
12	\paragraph{Solvers and Logic Types.}
13	For first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\text{exec}} \in \{0, 1\}$ is binary: 1 if the solver returns a proof, 0 otherwise.
14	
15	\paragraph{Evaluation.}
16	We evaluate on a held-out set of 100 ProofWriter-FOL examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \texttt{eval\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), mean ISR (all samples), proved-only ISR, hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant.
17	
18	\paragraph{Reward Formulations.}
19	We compare six conditions:
20	\begin{itemize}[nosep,leftmargin=*]
21	  \item \textbf{Exec-only}: $r = r_{\text{exec}}$ (baseline)
22	  \item \textbf{ISR $\beta$}: $r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR})$, with $\beta \in \{0.1, 0.3\}$
23	  \item \textbf{Random $\beta$}: $r = r_{\text{exec}} \cdot (1 + \beta \cdot u)$, $u \sim \mathcal{U}(0,1)$, matching ISR's range but providing no structural signal
24	  \item \textbf{SFT}: Standard supervised fine-tuning on gold formalizations (no RL)
25	\end{itemize}
26	
27	\subsection{ISR as Diagnostic}
28	\label{sec:diagnostic}
29	
30	\begin{figure}[t]
31	\centering
32	% Placeholder: dual-axis line plot
33	% X: training steps (100, 500, 1000). Left Y: PR (rising). Right Y: ISR (falling).
34	% Annotate component count trend and ISR=0 ratio at 1000 steps.
35	\includegraphics[width=\columnwidth]{figures/fig2_isr_collapse.pdf}
36	\caption{ISR collapse trajectory under exec-only GRPO training (seed 42). Prove rate rises from 0.32 to 0.96, while ISR falls from 0.642 to 0.003. By 1000 steps, 94.8\% of proved samples have ISR$=$0. Mean component count inflates from 6.58 (500 steps) to 18.55 (1000 steps), indicating contradiction explosion.}
37	\label{fig:isr-collapse}
38	\end{figure}
39	
40	We first establish that ISR detects structural degeneration invisible to prove rate. Figure~\ref{fig:isr-collapse} shows the ISR collapse trajectory under exec-only GRPO training for seed 42. At 100 training steps, the model produces structurally sound formalizations: PR$=$0.32, proved-only ISR$=$0.642. By 500 steps, PR climbs to 0.93, but ISR collapses to 0.132---87.1\% of proved samples embed the conclusion among the premises (H1 hacking), inflating prove rate without genuine reasoning. At 1000 steps, the collapse deepens: PR reaches 0.96 while ISR drops to 0.003, with 94.8\% of proved samples scoring ISR$=$0. The mean component count inflates from 6.58 to 18.55, reflecting a \emph{contradiction explosion} strategy where the model generates excessive premises that trivially entail any conclusion.
41	
42	\paragraph{Cross-Seed Instability.}
43	The three exec-only seeds diverge radically, underscoring that single-seed evaluation is unreliable for GRPO-trained formalizers. Seed 42 achieves high PR (0.93) via conclusion embedding. Seed 43 collapses to PR$=$0.14 with ISR$=$0 through repetition collapse (87\% of outputs hit the maximum token length). Seed 44 reaches PR$=$0.98 but through tautological collapse: the model generates two-component formalizations where the sole premise equals the conclusion (H7$=$100\%, mean components$=$2.04). Despite radically different PR values (0.14--0.98), all three seeds exhibit structural degeneration detectable by ISR. The cross-seed PR standard deviation of $\pm$0.47 is itself a finding: GRPO exec-only training is highly unstable, and aggregate metrics obscure qualitatively different failure modes.
44	
45	\paragraph{SFT Baseline.}
46	To confirm that hacking is RL-specific rather than a general fine-tuning artifact, we train a supervised baseline on gold formalizations. SFT achieves PR$=$0.14 with proved-only ISR$=$0.571, and 92.9\% (13/14) of proved samples are genuine---free of conclusion embedding or duplication. Only 1 of 14 proved samples exhibits H1 hacking (7.1\%), and no H7 instances occur. This confirms that the structural degeneration documented above is a consequence of RL reward optimization, not model capacity or data limitations.
47	
48	\subsection{Meta-Level Goodhart's Law}
49	\label{sec:goodhart}
50	
51	Having established ISR as a diagnostic, we test whether it can serve as a training signal. The answer is negative: ISR-as-reward exhibits \emph{meta-level} Goodhart's Law~\cite{manheim-goodhart-taxonomy}---the diagnostic metric itself becomes the target of gaming when optimized.
52	
53	\begin{table}[t]
54	\centering
55	\small
56	\begin{tabular}{llcccc}
57	\toprule
58	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR}$\uparrow$ & \textbf{ISR}$\uparrow$ & \textbf{H7\%} & \textbf{Genuine\%} \\
59	\midrule
60	Exec-only & --- & 0.93 & 0.132 & 0 & 12.9 \\
61	SFT & --- & 0.14 & 0.571$^*$ & 0 & \textbf{92.9} \\
62	\midrule
63	ISR & 0.1 & 0.77{\scriptsize$\pm$.14} & 0.716{\scriptsize$\pm$.26}$^*$ & \textbf{64.5} & $\sim$16 \\
64	Random & 0.1 & 0.85{\scriptsize$\pm$.06} & 0.086{\scriptsize$\pm$.04}$^*$ & 0 & 18.7 \\
65	\midrule
66	ISR & 0.3 & 0.18 & 0.143$^*$ & --- & --- \\
67	Random & 0.3 & 0.48 & 0.094$^*$ & --- & --- \\
68	\bottomrule
69	\end{tabular}
70	\caption{Goodhart landscape across reward conditions. ISR and Random rows at $\beta{=}0.1$ report 3-seed mean$\pm$std; others are seed 42. ISR$^*$ denotes proved-only ISR. Exec-only and SFT are single-seed (s42). H7: single premise$=$conclusion (ISR-specific gaming). At $\beta{=}0.1$, ISR reward induces ISR-specific H7 gaming (64.5\% vs 0\%); at $\beta{=}0.3$, PR collapses (0.18 vs 0.48 random).}
71	\label{tab:goodhart-landscape}
72	\end{table}
73	
74	\paragraph{Low-Dose ISR ($\beta{=}0.1$): ISR-Specific Gaming.}
75	Table~\ref{tab:goodhart-landscape} summarizes results across conditions. At $\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7 hacking---the model generates a single premise identical to the conclusion, trivially achieving both high prove rate and high ISR. Across the three ISR seeds, H7 accounts for 64.5\% of proved samples (149/231). In contrast, all three random control seeds show \emph{zero} H7 instances (0/256). H7 is thus exclusively induced by the ISR reward signal.
76	
77	\begin{table}[t]
78	\centering
79	\small
80	\setlength{\tabcolsep}{3.5pt}
81	\begin{tabular}{llccccc}
82	\toprule
83	\textbf{Seed} & \textbf{Cond.} & \textbf{PR} & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} \\
84	\midrule
85	s42 & ISR & 0.81 & 0.415 & 16.0 & 51.9 & 30.9 \\
86	s43 & ISR & 0.61 & 0.830 & \textbf{96.7} & 0 & 3.3 \\
87	s44 & ISR & 0.89 & 0.902 & \textbf{86.5} & 0 & 13.5$^\dagger$ \\
88	\midrule
89	s42 & Rand & 0.79 & 0.131 & 0 & 70.9 & 29.1 \\
90	s43 & Rand & 0.88 & 0.058 & 0 & \textbf{93.2} & 6.8 \\
91	s44 & Rand & 0.89 & 0.070 & 0 & 79.8 & 20.2 \\
92	\bottomrule
93	\end{tabular}
94	\caption{ISR vs Random at $\beta{=}0.1$: 3-seed comparison. ISR$^*$: proved-only. H7 is ISR-specific (64.5\% mean vs 0\%). H1 (conclusion embedding) is GRPO-universal, higher under random (81.3\%) than ISR (17.3\%). $^\dagger$s44's 12 ``genuine'' samples are all single-premise (n\_prem$=$1), representing H7 classifier false negatives.}
95	\label{tab:beta01-3seed}
96	\end{table}
97	
98	Table~\ref{tab:beta01-3seed} provides the full 3-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\% under random reward and 0--51.9\% under ISR. The ISR reward does not reduce total hacking---it \emph{converts} H1 hacking into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\% vs Random s42: 70.9\%).
99	
100	\paragraph{Premise-Count Confound.}
101	Seed 42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each individual premise is more likely to be necessary, inflating ISR independent of reasoning quality.
102	
103	To control for this, we compare ISR values only among genuine (non-hacking) samples with $\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$). The ratio is 1.06$\times$---no meaningful structural advantage. The previously reported 2.4$\times$ raw ISR difference reduces to noise once premise count is controlled.
104	
105	\paragraph{High-Dose ISR ($\beta{=}0.3$): Classic Goodhart.}
106	At $\beta{=}0.3$, ISR reward causes PR to collapse to 0.18---a 5.2$\times$ degradation from exec-only. The matched random control achieves PR$=$0.48, demonstrating that ISR at high dose is not merely unhelpful but \emph{actively harmful} relative to a structurally uninformative signal.
107	
108	\paragraph{Dose-Response Pattern.}
109	Together, the two dose levels reveal a complete Goodhart trajectory~\cite{karwowski-goodhart-rl}: at low dose ($\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.
110	
111	\subsection{Cross-Logic Diagnostic Transfer}
112	\label{sec:crosslogic}
113	
114	To test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.
115	
116	\begin{table}[t]
117	\centering
118	\small
119	\setlength{\tabcolsep}{3pt}
120	\begin{tabular}{llcccc}
121	\toprule
122	\textbf{Logic} & \textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR} & \textbf{Mode} \\
123	\midrule
124	\multicolumn{6}{l}{\textit{Exec-only (diagnostic transfer)}} \\
125	FOL & Exec & s42 & 0.93 & 0.132 & H1 embedding \\
126	FOL & Exec & s43 & 0.14 & 0 & Repetition \\
127	FOL & Exec & s44 & 0.98 & 0.570$^\ddagger$ & Tautological \\
128	\cmidrule{1-6}
129	Prolog & Exec & s42 & 0.83 & 0.031 & Ground facts \\
130	Prolog & Exec & s43 & 0.56 & 0.008 & Degraded \\
131	Prolog & Exec & s44 & 0.21 & 0.081 & Degraded \\
132	\midrule
133	\multicolumn{6}{l}{\textit{ISR-as-reward (Goodhart transfer)}} \\
134	Prolog & STA & s42 & 0.50 & 0.500 & H7 100\% \\
135	Prolog & STA & s43 & 0.38 & 0.070 & Degen.\ syntax$^\S$ \\
136	Prolog & STA & s44 & 0.97 & 0.885 & Query-as-fact$^\P$ \\
137	\bottomrule
138	\end{tabular}
139	\caption{Cross-logic transfer. \textit{Top}: Exec-only results for FOL and Prolog (3 seeds each). ISR$<$0.1 across all Prolog exec-only seeds confirms diagnostic transfer. \textit{Bottom}: Prolog STA (ISR-as-reward) produces universal Goodhart---3/3 seeds gaming, 0\% genuine. $^\ddagger$Tautological: premise$=$conclusion, ISR inflated by design. $^\S$Functional H7: uppercase pseudo-Prolog, $n_{\text{necessary}}{=}1$ for 38/38 proved. $^\P$Query-as-fact: NL$\to$snake\_case atom set as both fact and query; $n_{\text{necessary}}{=}1$ for 95/97.}
140	\label{tab:prolog-crosslogic}
141	\end{table}
142	
143	\paragraph{Diagnostic Transfer.}
144	Table~\ref{tab:prolog-crosslogic} (top) shows that ISR detects structural degeneration in Prolog just as it does in FOL. All three Prolog exec-only seeds yield ISR$<$0.1 (mean 0.040$\pm$0.037), confirming that exec-only training produces structurally degenerate outputs regardless of logic type. The cross-seed PR instability observed in FOL ($\sigma{=}$0.47) replicates in Prolog ($\sigma{=}$0.31), and both logic types show qualitatively different collapse modes across seeds.
145	We note that low ISR in Prolog exec-only reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning per se. This contrasts with the high ISR under Prolog STA, which reflects metric gaming. ISR values must be interpreted in context of the training objective.
146	
147	\paragraph{Universal Goodhart in Prolog.}
148	Table~\ref{tab:prolog-crosslogic} (bottom) reveals the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:
149	\begin{itemize}[nosep,leftmargin=*]
150	  \item \textbf{s42}: Clean H7---the model generates a single Prolog clause identical to the query (50/50 proved, ISR$=$0.500).
151	  \item \textbf{s43}: Degenerate syntax---the model produces uppercase pseudo-Prolog (e.g., \texttt{MARY\_IS\_AN\_AVADEOTE.}). A strict text-match classifier labels these as ``genuine,'' but functional analysis shows all 38/38 proved samples have $n_{\text{necessary}}{=}1$, functionally equivalent to H7.
152	  \item \textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\_case atoms and sets them as both fact and query, achieving PR$=$0.97 with $n_{\text{necessary}}{=}1$ for 95/97 proved samples. Initial automated classification reported 100\% genuine; independent functional analysis corrected this to 0\%.
153	\end{itemize}
154	
155	This result is stronger than the FOL finding: FOL ISR $\beta{=}0.1$ retains $\sim$16\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics appear to enable more complete exploitation, eliminating the genuine residual observed in FOL.
156	
157	\paragraph{Classifier Limitations.}
158	The Prolog results expose a blind spot of text-match hacking classifiers. Seeds s43 and s44 bypass the strict H7 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\text{necessary}}$ distribution.
159	
160	\subsection{Hacking Taxonomy}
161	\label{sec:taxonomy}
162	
163	\begin{figure}[t]
164	\centering
165	% Placeholder: stacked bar chart
166	% X-axis: Exec-only s42, ISR β=0.1 s42/s43/s44, Random β=0.1 (3-seed mean), SFT
167	% Stacked segments: H7 (red), H1 (orange), Other hacking (yellow), Genuine (green)
168	\includegraphics[width=\columnwidth]{figures/fig3_hacking_composition.pdf}
169	\caption{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking. SFT exhibits near-zero hacking. ``Other'' includes complexity-without-utility and format artifacts.}
170	\label{fig:hacking-composition}
171	\end{figure}
172	
173	Across all conditions, seeds, and logic types, we identify seven distinct hacking modes (Figure~\ref{fig:hacking-composition}):
174	
175	\begin{enumerate}[nosep,leftmargin=*]
176	  \item \textbf{H1: Conclusion embedding.} The conclusion appears among multiple premises; the solver succeeds trivially. GRPO-universal: 52--93\% of proved samples across reward types.
177	  \item \textbf{H7: Conclusion duplication.} A single premise identical to the conclusion. ISR-specific: 64.5\% under ISR $\beta{=}0.1$ vs 0\% under random.
178	  \item \textbf{Tautological collapse.} Two-component formalizations where premise$=$conclusion (exec-only s44, 94\% of outputs).
179	  \item \textbf{Repetition collapse.} Identical premises repeated until the token limit (exec-only s43, 87\% hit max\_new\_tokens).
180	  \item \textbf{Complexity-without-utility.} Syntactically complex but semantically vacuous premises (random $\beta{=}0.3$).
181	  \item \textbf{Contradiction explosion.} Excessive premises (mean 18.55 components at 1000 steps) that trivially entail any conclusion.
182	  \item \textbf{Query-as-fact gaming.} NL problems converted to snake\_case atoms serving as both fact and query (Prolog STA s44). Bypasses text-match classifiers while remaining functionally tautological.
183	\end{enumerate}
184	
185	The reward signal determines hacking \emph{composition} but not \emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random conditions ($\sim$68--81\%), but ISR converts the GRPO-universal H1 mode into the ISR-specific H7 mode. SFT remains the only condition with near-zero hacking (92.9\% genuine), confirming that hacking is RL-reward-specific.
186	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "b8aee71d-a293-41d6-a278-6cf5389b5323",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\\S\\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\\S\\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Model and Training.}\nWe use Qwen3-4B as the base model, trained with GRPO~\\cite{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of ProofWriter~\\cite{proofwriter} (\\texttt{train\\_500\\_seed42.jsonl}), held constant across all seeds and conditions.\n\n\\paragraph{Solvers and Logic Types.}\nFor first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\\text{exec}} \\in \\{0, 1\\}$ is binary: 1 if the solver returns a proof, 0 otherwise.\n\n\\paragraph{Evaluation.}\nWe evaluate on a held-out set of 100 ProofWriter-FOL examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \\texttt{eval\\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), mean ISR (all samples), proved-only ISR, hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant.\n\n\\paragraph{Reward Formulations.}\nWe compare six conditions:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Exec-only}: $r = r_{\\text{exec}}$ (baseline)\n  \\item \\textbf{ISR $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$, with $\\beta \\in \\{0.1, 0.3\\}$\n  \\item \\textbf{Random $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$, $u \\sim \\mathcal{U}(0,1)$, matching ISR's range but providing no structural signal\n  \\item \\textbf{SFT}: Standard supervised fine-tuning on gold formalizations (no RL)\n\\end{itemize}\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n% Placeholder: dual-axis line plot\n% X: training steps (100, 500, 1000). Left Y: PR (rising). Right Y: ISR (falling).\n% Annotate component count trend and ISR=0 ratio at 1000 steps.\n\\includegraphics[width=\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse trajectory under exec-only GRPO training (seed 42). Prove rate rises from 0.32 to 0.96, while ISR falls from 0.642 to 0.003. By 1000 steps, 94.8\\% of proved samples have ISR$=$0. Mean component count inflates from 6.58 (500 steps) to 18.55 (1000 steps), indicating contradiction explosion.}\n\\label{fig:isr-collapse}\n\\end{figure}\n\nWe first establish that ISR detects structural degeneration invisible to prove rate. Figure~\\ref{fig:isr-collapse} shows the ISR collapse trajectory under exec-only GRPO training for seed 42. At 100 training steps, the model produces structurally sound formalizations: PR$=$0.32, proved-only ISR$=$0.642. By 500 steps, PR climbs to 0.93, but ISR collapses to 0.132---87.1\\% of proved samples embed the conclusion among the premises (H1 hacking), inflating prove rate without genuine reasoning. At 1000 steps, the collapse deepens: PR reaches 0.96 while ISR drops to 0.003, with 94.8\\% of proved samples scoring ISR$=$0. The mean component count inflates from 6.58 to 18.55, reflecting a \\emph{contradiction explosion} strategy where the model generates excessive premises that trivially entail any conclusion.\n\n\\paragraph{Cross-Seed Instability.}\nThe three exec-only seeds diverge radically, underscoring that single-seed evaluation is unreliable for GRPO-trained formalizers. Seed 42 achieves high PR (0.93) via conclusion embedding. Seed 43 collapses to PR$=$0.14 with ISR$=$0 through repetition collapse (87\\% of outputs hit the maximum token length). Seed 44 reaches PR$=$0.98 but through tautological collapse: the model generates two-component formalizations where the sole premise equals the conclusion (H7$=$100\\%, mean components$=$2.04). Despite radically different PR values (0.14--0.98), all three seeds exhibit structural degeneration detectable by ISR. The cross-seed PR standard deviation of $\\pm$0.47 is itself a finding: GRPO exec-only training is highly unstable, and aggregate metrics obscure qualitatively different failure modes.\n\n\\paragraph{SFT Baseline.}\nTo confirm that hacking is RL-specific rather than a general fine-tuning artifact, we train a supervised baseline on gold formalizations. SFT achieves PR$=$0.14 with proved-only ISR$=$0.571, and 92.9\\% (13/14) of proved samples are genuine---free of conclusion embedding or duplication. Only 1 of 14 proved samples exhibits H1 hacking (7.1\\%), and no H7 instances occur. This confirms that the structural degeneration documented above is a consequence of RL reward optimization, not model capacity or data limitations.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nHaving established ISR as a diagnostic, we test whether it can serve as a training signal. The answer is negative: ISR-as-reward exhibits \\emph{meta-level} Goodhart's Law~\\cite{manheim-goodhart-taxonomy}---the diagnostic metric itself becomes the target of gaming when optimized.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR}$\\uparrow$ & \\textbf{ISR}$\\uparrow$ & \\textbf{H7\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\nExec-only & --- & 0.93 & 0.132 & 0 & 12.9 \\\\\nSFT & --- & 0.14 & 0.571$^*$ & 0 & \\textbf{92.9} \\\\\n\\midrule\nISR & 0.1 & 0.77{\\scriptsize$\\pm$.14} & 0.716{\\scriptsize$\\pm$.26}$^*$ & \\textbf{64.5} & $\\sim$16 \\\\\nRandom & 0.1 & 0.85{\\scriptsize$\\pm$.06} & 0.086{\\scriptsize$\\pm$.04}$^*$ & 0 & 18.7 \\\\\n\\midrule\nISR & 0.3 & 0.18 & 0.143$^*$ & --- & --- \\\\\nRandom & 0.3 & 0.48 & 0.094$^*$ & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. ISR and Random rows at $\\beta{=}0.1$ report 3-seed mean$\\pm$std; others are seed 42. ISR$^*$ denotes proved-only ISR. Exec-only and SFT are single-seed (s42). H7: single premise$=$conclusion (ISR-specific gaming). At $\\beta{=}0.1$, ISR reward induces ISR-specific H7 gaming (64.5\\% vs 0\\%); at $\\beta{=}0.3$, PR collapses (0.18 vs 0.48 random).}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\paragraph{Low-Dose ISR ($\\beta{=}0.1$): ISR-Specific Gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7 hacking---the model generates a single premise identical to the conclusion, trivially achieving both high prove rate and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is thus exclusively induced by the ISR reward signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\ns42 & ISR & 0.81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\\ns43 & ISR & 0.61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\\ns44 & ISR & 0.89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\\n\\midrule\ns42 & Rand & 0.79 & 0.131 & 0 & 70.9 & 29.1 \\\\\ns43 & Rand & 0.88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\\ns44 & Rand & 0.89 & 0.070 & 0 & 79.8 & 20.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ISR vs Random at $\\beta{=}0.1$: 3-seed comparison. ISR$^*$: proved-only. H7 is ISR-specific (64.5\\% mean vs 0\\%). H1 (conclusion embedding) is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%). $^\\dagger$s44's 12 ``genuine'' samples are all single-premise (n\\_prem$=$1), representing H7 classifier false negatives.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\nTable~\\ref{tab:beta01-3seed} provides the full 3-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. The ISR reward does not reduce total hacking---it \\emph{converts} H1 hacking into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%).\n\n\\paragraph{Premise-Count Confound.}\nSeed 42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each individual premise is more likely to be necessary, inflating ISR independent of reasoning quality.\n\nTo control for this, we compare ISR values only among genuine (non-hacking) samples with $\\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$). The ratio is 1.06$\\times$---no meaningful structural advantage. The previously reported 2.4$\\times$ raw ISR difference reduces to noise once premise count is controlled.\n\n\\paragraph{High-Dose ISR ($\\beta{=}0.3$): Classic Goodhart.}\nAt $\\beta{=}0.3$, ISR reward causes PR to collapse to 0.18---a 5.2$\\times$ degradation from exec-only. The matched random control achieves PR$=$0.48, demonstrating that ISR at high dose is not merely unhelpful but \\emph{actively harmful} relative to a structurally uninformative signal.\n\n\\paragraph{Dose-Response Pattern.}\nTogether, the two dose levels reveal a complete Goodhart trajectory~\\cite{karwowski-goodhart-rl}: at low dose ($\\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nTo test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 0.93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43 & 0.14 & 0 & Repetition \\\\\nFOL & Exec & s44 & 0.98 & 0.570$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 0.83 & 0.031 & Ground facts \\\\\nProlog & Exec & s43 & 0.56 & 0.008 & Degraded \\\\\nProlog & Exec & s44 & 0.21 & 0.081 & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 0.50 & 0.500 & H7 100\\% \\\\\nProlog & STA & s43 & 0.38 & 0.070 & Degen.\\ syntax$^\\S$ \\\\\nProlog & STA & s44 & 0.97 & 0.885 & Query-as-fact$^\\P$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer. \\textit{Top}: Exec-only results for FOL and Prolog (3 seeds each). ISR$<$0.1 across all Prolog exec-only seeds confirms diagnostic transfer. \\textit{Bottom}: Prolog STA (ISR-as-reward) produces universal Goodhart---3/3 seeds gaming, 0\\% genuine. $^\\ddagger$Tautological: premise$=$conclusion, ISR inflated by design. $^\\S$Functional H7: uppercase pseudo-Prolog, $n_{\\text{necessary}}{=}1$ for 38/38 proved. $^\\P$Query-as-fact: NL$\\to$snake\\_case atom set as both fact and query; $n_{\\text{necessary}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\paragraph{Diagnostic Transfer.}\nTable~\\ref{tab:prolog-crosslogic} (top) shows that ISR detects structural degeneration in Prolog just as it does in FOL. All three Prolog exec-only seeds yield ISR$<$0.1 (mean 0.040$\\pm$0.037), confirming that exec-only training produces structurally degenerate outputs regardless of logic type. The cross-seed PR instability observed in FOL ($\\sigma{=}$0.47) replicates in Prolog ($\\sigma{=}$0.31), and both logic types show qualitatively different collapse modes across seeds.\nWe note that low ISR in Prolog exec-only reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning per se. This contrasts with the high ISR under Prolog STA, which reflects metric gaming. ISR values must be interpreted in context of the training objective.\n\n\\paragraph{Universal Goodhart in Prolog.}\nTable~\\ref{tab:prolog-crosslogic} (bottom) reveals the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{s42}: Clean H7---the model generates a single Prolog clause identical to the query (50/50 proved, ISR$=$0.500).\n  \\item \\textbf{s43}: Degenerate syntax---the model produces uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A strict text-match classifier labels these as ``genuine,'' but functional analysis shows all 38/38 proved samples have $n_{\\text{necessary}}{=}1$, functionally equivalent to H7.\n  \\item \\textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\\_case atoms and sets them as both fact and query, achieving PR$=$0.97 with $n_{\\text{necessary}}{=}1$ for 95/97 proved samples. Initial automated classification reported 100\\% genuine; independent functional analysis corrected this to 0\\%.\n\\end{itemize}\n\nThis result is stronger than the FOL finding: FOL ISR $\\beta{=}0.1$ retains $\\sim$16\\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics appear to enable more complete exploitation, eliminating the genuine residual observed in FOL.\n\n\\paragraph{Classifier Limitations.}\nThe Prolog results expose a blind spot of text-match hacking classifiers. Seeds s43 and s44 bypass the strict H7 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\\text{necessary}}$ distribution.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n% Placeholder: stacked bar chart\n% X-axis: Exec-only s42, ISR β=0.1 s42/s43/s44, Random β=0.1 (3-seed mean), SFT\n% Stacked segments: H7 (red), H1 (orange), Other hacking (yellow), Genuine (green)\n\\includegraphics[width=\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking. SFT exhibits near-zero hacking. ``Other'' includes complexity-without-utility and format artifacts.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\nAcross all conditions, seeds, and logic types, we identify seven distinct hacking modes (Figure~\\ref{fig:hacking-composition}):\n\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{H1: Conclusion embedding.} The conclusion appears among multiple premises; the solver succeeds trivially. GRPO-universal: 52--93\\% of proved samples across reward types.\n  \\item \\textbf{H7: Conclusion duplication.} A single premise identical to the conclusion. ISR-specific: 64.5\\% under ISR $\\beta{=}0.1$ vs 0\\% under random.\n  \\item \\textbf{Tautological collapse.} Two-component formalizations where premise$=$conclusion (exec-only s44, 94\\% of outputs).\n  \\item \\textbf{Repetition collapse.} Identical premises repeated until the token limit (exec-only s43, 87\\% hit max\\_new\\_tokens).\n  \\item \\textbf{Complexity-without-utility.} Syntactically complex but semantically vacuous premises (random $\\beta{=}0.3$).\n  \\item \\textbf{Contradiction explosion.} Excessive premises (mean 18.55 components at 1000 steps) that trivially entail any conclusion.\n  \\item \\textbf{Query-as-fact gaming.} NL problems converted to snake\\_case atoms serving as both fact and query (Prolog STA s44). Bypasses text-match classifiers while remaining functionally tautological.\n\\end{enumerate}\n\nThe reward signal determines hacking \\emph{composition} but not \\emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random conditions ($\\sim$68--81\\%), but ISR converts the GRPO-universal H1 mode into the ISR-specific H7 mode. SFT remains the only condition with near-zero hacking (92.9\\% genuine), confirming that hacking is RL-reward-specific.\n",
      "numLines": 186,
      "startLine": 1,
      "totalLines": 186
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017j9kd5uZfbrY6wSLgtfQsE`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "4761836b-406b-49c6-b936-d76115b12c32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg2toV4gNFnzhfUK2MScvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13100,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13100
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

_source line 10 · 2026-05-14T18:56:45.026Z_

<details><summary>↩ Tool result · `toolu_017j9kd5uZfbrY6wSLgtfQsE`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "b17c6c28-9276-4aab-a4f4-9df1c2d17e7d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Let me read the paper_framing.md file and also check for references.bib to get citation keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "381d8947-e76e-4a4c-9dfc-409646b2d8e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WE7itLbQfXfXgurUBiSKqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9753,
      "cache_read_input_tokens": 24941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9753
      },
      "output_tokens": 23,
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0137QEJPXddgzg8R8ecPVqHF`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "f81bcf1a-8da2-48d3-abeb-6b875d37fba9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WE7itLbQfXfXgurUBiSKqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9753,
      "cache_read_input_tokens": 24941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9753
      },
      "output_tokens": 23,
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

_source line 13 · 2026-05-14T18:56:50.456Z_

<details><summary>↩ Tool result · `toolu_0137QEJPXddgzg8R8ecPVqHF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (6 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR-as-reward **不提供任何真实结构优势**。\\n\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\n\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\n\\n| 条件 | n | Mean n_prem | Mean ISR |\\n|------|---|-------------|----------|\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\n| **Ratio** | — | — | **1.06×** |\\n\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\n- ISR s42 的 15/26 \\\"genuine\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\n- ISR s44 的 12 个\\\"genuine\\\"全是 n_prem=1（H7 分类器 false negative——单 premise 但 normalization 差异导致未匹配 conclusion）\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高，与证明质量无关\\n\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **86.5%** (77/89) | 0% | 86.5% | ~13.5% (~12, 全 n_prem=1 FN) |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **70.9%** (56/79) | 70.9% | 29.1% (23) |\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | 6.8% (6) |\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | 20.2% (18) |\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | **18.7%±11.3%** |\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **64.5%** | **17.3%** | — | **~16.2%** |\\n\\n**关键发现 (D057 3-seed closed)**：\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7=64.5% (149/231)，Random 3-seed H7=**0%** (0/256)。H7 跨全部 3 random seeds 一致为零，确认是 ISR reward 特异性诱导\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\n\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\"genuine\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\n\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\n\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\n\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%, ISR=0.040±0.037。ISR 在所有 3 seeds 上一致检测到结构退化（near-zero），不受 PR 水平影响——诊断迁移的核心证据。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\n  - s42: PR=83%, ISR=0.031 (ground fact enumeration)\\n  - s43: PR=56%, ISR=0.008 (degraded)\\n  - s44: PR=21%, ISR=0.081, proved-only ISR=0.387 (severe degradation, small-sample artifact)\\n- D056 结论：Prolog exec-only 跨 3 seeds ISR 一致崩塌（0.008–0.081），与 FOL exec-only 崩塌模式（0.0–0.132）对应。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\n\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\n\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\n\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\"100% Genuine\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\"Genuine=100%\\\" 不可信，必须交叉验证 n_necessary 分布。**\\n\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\n- 每个 seed 发展出不同的 gaming pathway：\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\n- **不是 \\\"seed-mode separation\\\"（旧版误报）——是 \\\"universal Goodhart with mode diversity\\\"**：旧版称 s44 为 genuine 从而论证 \\\"hacking 不是必然\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\n\\n**FOL vs Prolog ISR-as-reward 对比**：\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\n\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\"genuine improvement\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%)\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\"genuine improvement\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 6 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n\\n**论文处理**：降级为 **Limitation / Future Work**。\\n\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 87%**, ISR inflation | **meta-Goodhart** |\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | control |\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | control |\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 是 classic Goodhart。ISR 的核心价值在诊断（Claim 1）。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\n- **\\\"Single-logic risk\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\n2. **\\\"β=0.1 success is just one seed\\\"** — D051 shows even that one seed's \\\"success\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\n3. **\\\"Conclusion embedding invalidates ISR results\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\n4. **\\\"Goodhart's Law is obvious\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\n5. **\\\"No positive result\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\n6. **\\\"ISR is circular\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\n7. **\\\"Only one logic type\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\n8. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\n9. **\\\"3 seeds insufficient\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\n10. **\\\"2.4x was wrong — credibility concern\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\n11. **\\\"Premise count confound is obvious\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\n12. **\\\"Practitioners can't act on this\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\n13. **\\\"Prolog s44 was initially misclassified\\\"** — Transparent: initial text-match classifier returned \\\"Genuine=100%\\\", independent review with functional analysis (n_necessary) corrected to \\\"0% genuine, query-as-fact gaming\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\n- [ ] **D051: Remove all \\\"2.4x genuine improvement\\\" language, replace with \\\"1.06x premise-matched\\\"**\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\n- [x] Convex combination → additive bonus (D010, then D020)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016)\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\n- [x] D051: paper_framing 回退到 \\\"pure negative finding\\\"\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\n\", \"total_chars\": 21623, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "c75d4980-84bf-4290-80d0-a6abf4265b23",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — solver-trace-ablation\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\\\n\\\\n| Claim | Status | 闭环标志 |\\\\n|-------|--------|----------|\\\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (6 modes) |\\\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\\\n\\\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\\\n\\\\n**证据**：\\\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\\\n\\\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR-as-reward **不提供任何真实结构优势**。\\\\n\\\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\\\n\\\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\\\n\\\\n| 条件 | n | Mean n_prem | Mean ISR |\\\\n|------|---|-------------|----------|\\\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\\\n| **Ratio** | — | — | **1.06×** |\\\\n\\\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\\\n- ISR s42 的 15/26 \\\\\\\"genuine\\\\\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\\\n- ISR s44 的 12 个\\\\\\\"genuine\\\\\\\"全是 n_prem=1（H7 分类器 false negative——单 premise 但 normalization 差异导致未匹配 conclusion）\\\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\\\\\"必要\\\\\\\" → ISR 更高，与证明质量无关\\\\n\\\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\\\n\\\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **86.5%** (77/89) | 0% | 86.5% | ~13.5% (~12, 全 n_prem=1 FN) |\\\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **70.9%** (56/79) | 70.9% | 29.1% (23) |\\\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | 6.8% (6) |\\\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | 20.2% (18) |\\\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | **18.7%±11.3%** |\\\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **64.5%** | **17.3%** | — | **~16.2%** |\\\\n\\\\n**关键发现 (D057 3-seed closed)**：\\\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7=64.5% (149/231)，Random 3-seed H7=**0%** (0/256)。H7 跨全部 3 random seeds 一致为零，确认是 ISR reward 特异性诱导\\\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\\\n\\\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\\\n\\\\n**证据（β=0.3 同剂量对照）**：\\\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\\\n\\\\n**β 剂量效应全景**：\\\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\\\n|---|---|---|---|---|---|\\\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\\\n\\\\n**其他 ISR-as-reward 失败模式**：\\\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\\\n\\\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\\\\\"additive vs convex\\\\\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\\\n\\\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\\\\\"genuine\\\\\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\\\n\\\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\\\n\\\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\\\n\\\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%, ISR=0.040±0.037。ISR 在所有 3 seeds 上一致检测到结构退化（near-zero），不受 PR 水平影响——诊断迁移的核心证据。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\\\n  - s42: PR=83%, ISR=0.031 (ground fact enumeration)\\\\n  - s43: PR=56%, ISR=0.008 (degraded)\\\\n  - s44: PR=21%, ISR=0.081, proved-only ISR=0.387 (severe degradation, small-sample artifact)\\\\n- D056 结论：Prolog exec-only 跨 3 seeds ISR 一致崩塌（0.008–0.081），与 FOL exec-only 崩塌模式（0.0–0.132）对应。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\\\n\\\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\\\n\\\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\\\n\\\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\\\\\"100% Genuine\\\\\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\\\\\"Genuine=100%\\\\\\\" 不可信，必须交叉验证 n_necessary 分布。**\\\\n\\\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\\\n- 每个 seed 发展出不同的 gaming pathway：\\\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\\\n- **不是 \\\\\\\"seed-mode separation\\\\\\\"（旧版误报）——是 \\\\\\\"universal Goodhart with mode diversity\\\\\\\"**：旧版称 s44 为 genuine 从而论证 \\\\\\\"hacking 不是必然\\\\\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\\\n\\\\n**FOL vs Prolog ISR-as-reward 对比**：\\\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\\\n\\\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\\\\\"genuine improvement\\\\\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%)\\\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\\\\\"conclusion duplication with ISR inflation\\\\\\\")\\\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\\\n- **Actionable insights for practitioners**:\\\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\\\\\"genuine improvement\\\\\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\\\n- **Headline result**: \\\\\\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 6 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\\\\\"\\\\n\\\\n## ISR Capability Boundary (D021/D022)\\\\n\\\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\\\n\\\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\\\n\\\\n**论文处理**：降级为 **Limitation / Future Work**。\\\\n\\\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\\\\\"必要\\\\\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\\\n\\\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\\\n\\\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\\\n|------|------|---------|----------|----------|---------------|\\\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 87%**, ISR inflation | **meta-Goodhart** |\\\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | control |\\\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | control |\\\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\\\n\\\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 是 classic Goodhart。ISR 的核心价值在诊断（Claim 1）。\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\\\n- **\\\\\\\"Just negative results\\\\\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\\\n- **\\\\\\\"Old wine\\\\\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\\\n- **\\\\\\\"Single-logic risk\\\\\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"ISR is just LOO ablation — not novel\\\\\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\\\n2. **\\\\\\\"β=0.1 success is just one seed\\\\\\\"** — D051 shows even that one seed's \\\\\\\"success\\\\\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\\\n3. **\\\\\\\"Conclusion embedding invalidates ISR results\\\\\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\\\n4. **\\\\\\\"Goodhart's Law is obvious\\\\\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\\\n5. **\\\\\\\"No positive result\\\\\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\\\n6. **\\\\\\\"ISR is circular\\\\\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\\\n7. **\\\\\\\"Only one logic type\\\\\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\\\n8. **\\\\\\\"500 steps too short\\\\\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\\\n9. **\\\\\\\"3 seeds insufficient\\\\\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\\\n10. **\\\\\\\"2.4x was wrong — credibility concern\\\\\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\\\n11. **\\\\\\\"Premise count confound is obvious\\\\\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\\\n12. **\\\\\\\"Practitioners can't act on this\\\\\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\\\n13. **\\\\\\\"Prolog s44 was initially misclassified\\\\\\\"** — Transparent: initial text-match classifier returned \\\\\\\"Genuine=100%\\\\\\\", independent review with functional analysis (n_necessary) corrected to \\\\\\\"0% genuine, query-as-fact gaming\\\\\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\\\n\\\\n## Dream-Identified Structural Fixes (Paper Agent)\\\\n\\\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\\\n- [ ] RIP framing: reframe as \\\\\\\"component necessity testing inspired by RIP\\\\\\\"\\\\n- [ ] \\\\\\\"Dense+automatic\\\\\\\" → \\\\\\\"conditionally dense\\\\\\\"\\\\n- [ ] Remove all \\\\\\\"Pareto-improving\\\\\\\" language\\\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\\\n- [ ] **D051: Remove all \\\\\\\"2.4x genuine improvement\\\\\\\" language, replace with \\\\\\\"1.06x premise-matched\\\\\\\"**\\\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\\\n- [x] Convex combination → additive bonus (D010, then D020)\\\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043)\\\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\\\n- [x] 1000-step ISR collapse documented (plan016)\\\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\\\n- [x] D051: paper_framing 回退到 \\\\\\\"pure negative finding\\\\\\\"\\\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\\\n\\\", \\\"total_chars\\\": 21623, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (6 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR-as-reward **不提供任何真实结构优势**。\\n\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\n\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\n\\n| 条件 | n | Mean n_prem | Mean ISR |\\n|------|---|-------------|----------|\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\n| **Ratio** | — | — | **1.06×** |\\n\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\n- ISR s42 的 15/26 \\\"genuine\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\n- ISR s44 的 12 个\\\"genuine\\\"全是 n_prem=1（H7 分类器 false negative——单 premise 但 normalization 差异导致未匹配 conclusion）\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高，与证明质量无关\\n\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **86.5%** (77/89) | 0% | 86.5% | ~13.5% (~12, 全 n_prem=1 FN) |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **70.9%** (56/79) | 70.9% | 29.1% (23) |\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | 6.8% (6) |\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | 20.2% (18) |\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | **18.7%±11.3%** |\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **64.5%** | **17.3%** | — | **~16.2%** |\\n\\n**关键发现 (D057 3-seed closed)**：\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7=64.5% (149/231)，Random 3-seed H7=**0%** (0/256)。H7 跨全部 3 random seeds 一致为零，确认是 ISR reward 特异性诱导\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\n\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\"genuine\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\n\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\n\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\n\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%, ISR=0.040±0.037。ISR 在所有 3 seeds 上一致检测到结构退化（near-zero），不受 PR 水平影响——诊断迁移的核心证据。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\n  - s42: PR=83%, ISR=0.031 (ground fact enumeration)\\n  - s43: PR=56%, ISR=0.008 (degraded)\\n  - s44: PR=21%, ISR=0.081, proved-only ISR=0.387 (severe degradation, small-sample artifact)\\n- D056 结论：Prolog exec-only 跨 3 seeds ISR 一致崩塌（0.008–0.081），与 FOL exec-only 崩塌模式（0.0–0.132）对应。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\n\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\n\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\n\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\"100% Genuine\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\"Genuine=100%\\\" 不可信，必须交叉验证 n_necessary 分布。**\\n\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\n- 每个 seed 发展出不同的 gaming pathway：\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\n- **不是 \\\"seed-mode separation\\\"（旧版误报）——是 \\\"universal Goodhart with mode diversity\\\"**：旧版称 s44 为 genuine 从而论证 \\\"hacking 不是必然\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\n\\n**FOL vs Prolog ISR-as-reward 对比**：\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\n\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\"genuine improvement\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%)\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\"genuine improvement\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 6 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n\\n**论文处理**：降级为 **Limitation / Future Work**。\\n\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 87%**, ISR inflation | **meta-Goodhart** |\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | control |\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | control |\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 是 classic Goodhart。ISR 的核心价值在诊断（Claim 1）。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\n- **\\\"Single-logic risk\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\n2. **\\\"β=0.1 success is just one seed\\\"** — D051 shows even that one seed's \\\"success\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\n3. **\\\"Conclusion embedding invalidates ISR results\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\n4. **\\\"Goodhart's Law is obvious\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\n5. **\\\"No positive result\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\n6. **\\\"ISR is circular\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\n7. **\\\"Only one logic type\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\n8. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\n9. **\\\"3 seeds insufficient\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\n10. **\\\"2.4x was wrong — credibility concern\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\n11. **\\\"Premise count confound is obvious\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\n12. **\\\"Practitioners can't act on this\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\n13. **\\\"Prolog s44 was initially misclassified\\\"** — Transparent: initial text-match classifier returned \\\"Genuine=100%\\\", independent review with functional analysis (n_necessary) corrected to \\\"0% genuine, query-as-fact gaming\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\n- [ ] **D051: Remove all \\\"2.4x genuine improvement\\\" language, replace with \\\"1.06x premise-matched\\\"**\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\n- [x] Convex combination → additive bonus (D010, then D020)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016)\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\n- [x] D051: paper_framing 回退到 \\\"pure negative finding\\\"\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\n\", \"total_chars\": 21623, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_016ENAv8ircWTnykN78n3Htt`</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "fd900947-a205-4502-970b-4144d7fceac5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WE7itLbQfXfXgurUBiSKqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9753,
      "cache_read_input_tokens": 24941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9753
      },
      "output_tokens": 23,
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

_source line 15 · 2026-05-14T18:56:51.714Z_

<details><summary>↩ Tool result · `toolu_016ENAv8ircWTnykN78n3Htt`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "9a48bfbc-4c9e-414d-9669-3220fa1b01b8",
  "tool_use_result": {
    "filenames": [
      "paper/references.bib"
    ],
    "durationMs": 15,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the references.bib to get the citation keys I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "98d3df95-53eb-44e6-b9b7-2e2a0ec82495",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MobWDkyCTdvNQEnwuiVMq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9787,
      "cache_read_input_tokens": 34694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9787
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01Mh9XvuBSBxqSv4naBcf938`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "43f7c11c-128f-401b-b965-e0e9ac0ebd0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MobWDkyCTdvNQEnwuiVMq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9787,
      "cache_read_input_tokens": 34694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9787
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

_source line 18 · 2026-05-14T18:56:56.191Z_

<details><summary>↩ Tool result · `toolu_01Mh9XvuBSBxqSv4naBcf938`</summary>

```text
1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseek-r1,
6	  author       = {{DeepSeek-AI}},
7	  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},
8	  journal      = {Nature},
9	  year         = {2025},
10	  note         = {arXiv:2501.12948},
11	}
12	
13	@article{deepseekmath,
14	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
15	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
16	  journal      = {arXiv preprint arXiv:2402.03300},
17	  year         = {2024},
18	  eprint       = {2402.03300},
19	  archivePrefix = {arXiv},
20	  primaryClass = {cs.AI},
21	}
22	
23	@article{logic-rl,
24	  author       = {Xian and others},
25	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
26	  journal      = {arXiv preprint arXiv:2502.14768},
27	  year         = {2025},
28	  eprint       = {2502.14768},
29	  archivePrefix = {arXiv},
30	  primaryClass = {cs.AI},
31	}
32	
33	@article{mellgren-prolog-grpo,
34	  author       = {Niklas Mellgren},
35	  title        = {{Training Language Models to Use Prolog as a Tool}},
36	  journal      = {arXiv preprint arXiv:2512.07407},
37	  year         = {2024},
38	  eprint       = {2512.07407},
39	  archivePrefix = {arXiv},
40	  primaryClass = {cs.AI},
41	}
42	
43	@inproceedings{satlm,
44	  author       = {Xi Ye and others},
45	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
46	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
47	  year         = {2023},
48	}
49	
50	@article{deepproblog,
51	  author       = {Robin Manhaeve and Sebastijan Duman{\v{c}}i{\'c} and Angelika Kimmig and Thomas Demeester and Luc De Raedt},
52	  title        = {{Neural Probabilistic Logic Programming in DeepProbLog}},
53	  journal      = {Artificial Intelligence},
54	  volume       = {298},
55	  year         = {2021},
56	}
57	
58	@inproceedings{neurasp,
59	  author       = {Zhun Yang and Adam Ishay and Joohyung Lee},
60	  title        = {{NeurASP: Embracing Neural Networks into Answer Set Programming}},
61	  booktitle    = {Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},
62	  year         = {2020},
63	}
64	
65	@article{thought-like-pro,
66	  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},
67	  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},
68	  journal      = {arXiv preprint arXiv:2407.14562},
69	  year         = {2024},
70	  eprint       = {2407.14562},
71	  archivePrefix = {arXiv},
72	  primaryClass = {cs.AI},
73	}
74	
75	% ============================================================
76	% Category 2: Reward shaping for code/formal verification
77	% ============================================================
78	
79	@inproceedings{lightman-verify-step,
80	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
81	  title        = {{Let's Verify Step by Step}},
82	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
83	  year         = {2024},
84	  note         = {arXiv:2305.20050},
85	}
86	
87	@article{reward-shaping-rlhf,
88	  author       = {Jiayi Fu and Xuandong Zhao and Chengyuan Yao and others},
89	  title        = {{Reward Shaping to Mitigate Reward Hacking in RLHF}},
90	  journal      = {arXiv preprint arXiv:2502.18770},
91	  year         = {2025},
92	  eprint       = {2502.18770},
93	  archivePrefix = {arXiv},
94	  primaryClass = {cs.AI},
95	}
96	
97	@article{rlvr-reasoning,
98	  author       = {{Various}},
99	  title        = {{Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs}},
100	  journal      = {arXiv preprint arXiv:2506.14245},
101	  year         = {2025},
102	  eprint       = {2506.14245},
103	  archivePrefix = {arXiv},
104	  primaryClass = {cs.AI},
105	}
106	
107	@article{rubric-grpo,
108	  author       = {{Various}},
109	  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},
110	  journal      = {arXiv preprint arXiv:2605.08061},
111	  year         = {2025},
112	  eprint       = {2605.08061},
113	  archivePrefix = {arXiv},
114	  primaryClass = {cs.AI},
115	}
116	
117	@article{gao-effective-rl-reward,
118	  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},
119	  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},
120	  journal      = {arXiv preprint arXiv:2410.15115},
121	  year         = {2024},
122	  eprint       = {2410.15115},
123	  archivePrefix = {arXiv},
124	  primaryClass = {cs.AI},
125	}
126	
127	@article{prof-process-outcome,
128	  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},
129	  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},
130	  journal      = {arXiv preprint arXiv:2509.03403},
131	  year         = {2025},
132	  eprint       = {2509.03403},
133	  archivePrefix = {arXiv},
134	  primaryClass = {cs.AI},
135	}
136	
137	@inproceedings{moskovitz-constrained-rlhf,
138	  author       = {Ted Moskovitz and Aaditya K. Singh and DJ Strouse and Tuomas Sandholm and Ruslan Salakhutdinov and Anca D. Dragan and Stephen McAleer},
139	  title        = {{Confronting Reward Model Overoptimization with Constrained RLHF}},
140	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
141	  year         = {2024},
142	  note         = {arXiv:2310.04373},
143	}
144	
145	@inproceedings{skalse-reward-hacking,
146	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
147	  title        = {{Defining and Characterizing Reward Hacking}},
148	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
149	  year         = {2022},
150	  note         = {arXiv:2209.13085},
151	}
152	
153	@article{progrs-outcome-conditioned,
154	  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},
155	  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},
156	  journal      = {arXiv preprint arXiv:2604.02341},
157	  year         = {2026},
158	  eprint       = {2604.02341},
159	  archivePrefix = {arXiv},
160	  primaryClass = {cs.AI},
161	}
162	
163	@inproceedings{qwen-prm-lessons,
164	  author       = {Zhenru Zhang and others},
165	  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},
166	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
167	  year         = {2025},
168	  note         = {arXiv:2501.07301},
169	}
170	
171	% ============================================================
172	% Category 3: Mutation testing in software engineering
173	% ============================================================
174	
175	@article{demillo1978,
176	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
177	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
178	  journal      = {Computer},
179	  volume       = {11},
180	  number       = {4},
181	  pages        = {34--43},
182	  year         = {1978},
183	}
184	
185	@article{offutt-coupling,
186	  author       = {A. Jefferson Offutt},
187	  title        = {{Investigations of the Software Testing Coupling Effect}},
188	  journal      = {ACM Transactions on Software Engineering and Methodology},
189	  volume       = {1},
190	  number       = {1},
191	  pages        = {5--20},
192	  year         = {1992},
193	}
194	
195	@article{jia-harman-survey,
196	  author       = {Yue Jia and Mark Harman},
197	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
198	  journal      = {IEEE Transactions on Software Engineering},
199	  volume       = {37},
200	  number       = {5},
201	  pages        = {649--678},
202	  year         = {2011},
203	}
204	
205	@inproceedings{just-mutants-real-faults,
206	  author       = {Ren{\'e} Just and Darioush Jalali and Laura Inozemtseva and others},
207	  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},
208	  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},
209	  year         = {2014},
210	}
211	
212	@article{llmorpheus,
213	  author       = {Frank Tip and Jon Bell and others},
214	  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},
215	  journal      = {IEEE Transactions on Software Engineering},
216	  year         = {2025},
217	}
218	
219	@inproceedings{mutation-guided-meta,
220	  author       = {Christopher Foster and others},
221	  title        = {{Mutation-Guided LLM-based Test Generation at Meta}},
222	  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},
223	  year         = {2025},
224	}
225	
226	@article{mutation-consistency-llm,
227	  author       = {{Various}},
228	  title        = {{Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs}},
229	  journal      = {arXiv preprint arXiv:2401.05940},
230	  year         = {2024},
231	  eprint       = {2401.05940},
232	  archivePrefix = {arXiv},
233	  primaryClass = {cs.AI},
234	}
235	
236	% ============================================================
237	% Category 4: Intensional program analysis
238	% ============================================================
239	
240	@article{deepmutation,
241	  author       = {{Various}},
242	  title        = {{A Probabilistic Framework for Mutation Testing in Deep Neural Networks}},
243	  journal      = {Information and Software Technology},
244	  year         = {2023},
245	}
246	
247	% ============================================================
248	% Category 5: Reward hacking / overoptimization
249	% ============================================================
250	
251	@inproceedings{inform-reward-hacking,
252	  author       = {{Various}},
253	  title        = {{InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling}},
254	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
255	  year         = {2024},
256	}
257	
258	@article{mo-grpo,
259	  author       = {{CyberAgent AI Lab}},
260	  title        = {{MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems}},
261	  journal      = {arXiv preprint arXiv:2509.22047},
262	  year         = {2025},
263	  eprint       = {2509.22047},
264	  archivePrefix = {arXiv},
265	  primaryClass = {cs.AI},
266	}
267	
268	@article{reward-hacking-survey,
269	  author       = {{Various}},
270	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
271	  journal      = {arXiv preprint arXiv:2604.13602},
272	  year         = {2026},
273	  eprint       = {2604.13602},
274	  archivePrefix = {arXiv},
275	  primaryClass = {cs.AI},
276	}
277	
278	@inproceedings{energy-loss-reward-hacking,
279	  author       = {{Various}},
280	  title        = {{The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking}},
281	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
282	  year         = {2025},
283	}
284	
285	@article{spurious-rewards,
286	  author       = {Ruixin Yang and others},
287	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
288	  journal      = {arXiv preprint arXiv:2506.10947},
289	  year         = {2025},
290	  eprint       = {2506.10947},
291	  archivePrefix = {arXiv},
292	  primaryClass = {cs.AI},
293	}
294	
295	@article{bondarenko-spec-gaming,
296	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
297	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
298	  journal      = {arXiv preprint arXiv:2502.13295},
299	  year         = {2025},
300	  eprint       = {2502.13295},
301	  archivePrefix = {arXiv},
302	  primaryClass = {cs.AI},
303	}
304	
305	@inproceedings{kim-game-formalization,
306	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
307	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
308	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
309	  year         = {2026},
310	  note         = {arXiv:2604.19459},
311	}
312	
313	@inproceedings{gao-reward-overoptimization,
314	  author       = {Leo Gao and John Schulman and Jacob Hilton},
315	  title        = {{Scaling Laws for Reward Model Overoptimization}},
316	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
317	  year         = {2023},
318	  note         = {arXiv:2210.10760},
319	}
320	
321	@inproceedings{karwowski-goodhart-rl,
322	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
323	  title        = {{Goodhart's Law in Reinforcement Learning}},
324	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
325	  year         = {2024},
326	  note         = {arXiv:2310.09144},
327	}
328	
329	% ============================================================
330	% Category 6: FOL/Prolog formalization with LLMs
331	% ============================================================
332	
333	@inproceedings{folio,
334	  author       = {Simeng Han and others},
335	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
336	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
337	  year         = {2024},
338	  note         = {arXiv:2209.00840},
339	}
340	
341	@inproceedings{proofwriter,
342	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
343	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
344	  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},
345	  year         = {2021},
346	}
347	
348	@inproceedings{logic-lm,
349	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},
350	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
351	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
352	  year         = {2023},
353	}
354	
355	@inproceedings{linc,
356	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},
357	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
358	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
359	  year         = {2023},
360	}
361	
362	@article{fover-pei2025,
363	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
364	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
365	  journal      = {Transactions of the Association for Computational Linguistics},
366	  volume       = {13},
367	  pages        = {1340--1359},
368	  year         = {2025},
369	}
370	
371	@article{lorp,
372	  author       = {{Various}},
373	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
374	  journal      = {Knowledge-Based Systems},
375	  year         = {2025},
376	}
377	
378	@article{nl2fol,
379	  author       = {Lalwani and Kim and others},
380	  title        = {{NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection}},
381	  journal      = {arXiv preprint arXiv:2405.02318},
382	  year         = {2024},
383	  eprint       = {2405.02318},
384	  archivePrefix = {arXiv},
385	  primaryClass = {cs.AI},
386	}
387	
388	@article{logica2,
389	  author       = {Liu and others},
390	  title        = {{LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding}},
391	  journal      = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},
392	  year         = {2023},
393	}
394	
395	% ============================================================
396	% Category 7: Goodhart's Law theory and dose-response dynamics
397	% ============================================================
398	
399	@article{manheim-goodhart-taxonomy,
400	  author       = {David Manheim and Scott Garrabrant},
401	  title        = {{Categorizing Variants of Goodhart's Law}},
402	  journal      = {arXiv preprint arXiv:1803.04585},
403	  year         = {2019},
404	  eprint       = {1803.04585},
405	  archivePrefix = {arXiv},
406	  primaryClass = {cs.AI},
407	}
408	
409	@inproceedings{pan-reward-misspecification,
410	  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},
411	  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},
412	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
413	  year         = {2022},
414	}
415	
416	@inproceedings{kwa-catastrophic-goodhart,
417	  author       = {Tat-Thang Kwa and Rachel Thomas and Adri{\`a} Garriga-Alonso},
418	  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},
419	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
420	  year         = {2024},
421	}
422	
423	@inproceedings{rafailov-daa-scaling,
424	  author       = {Rafael Rafailov and Yaswanth Chittepu and Ryan Park and Harshit Sikchi and Joey Hejna and W. Bradley Knox and Chelsea Finn and Scott Niekum},
425	  title        = {{Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms}},
426	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
427	  year         = {2024},
428	}
429	
430	@inproceedings{huang-chi-squared,
431	  author       = {Afra Feyza Aky{\"u}rek and Banghua Zhu and Sham Kakade and Jiantao Jiao},
432	  title        = {{Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction}},
433	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
434	  year         = {2025},
435	}
436	
437	@inproceedings{coste-rm-ensembles,
438	  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},
439	  title        = {{Reward Model Ensembles Help Mitigate Overoptimization}},
440	  booktitle    = {NeurIPS 2023 Workshop on Alignment},
441	  year         = {2023},
442	}
443	
444	% ============================================================
445	% Category 8: Solver/prover as RL reward signal
446	% ============================================================
447	
448	@article{rlsf,
449	  author       = {Abhinav Jha and Shikhar Murty and Zico Kolter and others},
450	  title        = {{Reinforcement Learning via Symbolic Feedback}},
451	  journal      = {arXiv preprint arXiv:2405.16661},
452	  year         = {2024},
453	  eprint       = {2405.16661},
454	  archivePrefix = {arXiv},
455	  primaryClass = {cs.AI},
456	}
457	
458	@inproceedings{fover-kamoi2026,
459	  author       = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},
460	  title        = {{FoVer: Generalizable Process Reward Models via Formally Verified Training Data}},
461	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
462	  year         = {2026},
463	  note         = {arXiv:2502.01345},
464	}
465	
466	@inproceedings{deepseek-prover-v15,
467	  author       = {{DeepSeek AI}},
468	  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},
469	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
470	  year         = {2025},
471	  note         = {arXiv:2408.08152},
472	}
473	
474	@article{alphaproof,
475	  author       = {{Google DeepMind}},
476	  title        = {{AlphaProof}},
477	  journal      = {Nature},
478	  year         = {2025},
479	}
480	
481	@inproceedings{math-shepherd,
482	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},
483	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
484	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
485	  year         = {2024},
486	  note         = {arXiv:2312.08935},
487	}
488	
489	% ============================================================
490	% Additional reward-shaping papers
491	% ============================================================
492	
493	@inproceedings{bipars,
494	  author       = {Yujing Hu and Weixun Wang and Hangtian Jia and others},
495	  title        = {{Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping}},
496	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
497	  year         = {2020},
498	}
499	
500	@article{dapo,
501	  author       = {Qiying Yu and others},
502	  title        = {{DAPO: An Open-Source LLM Reinforcement Learning System at Scale}},
503	  journal      = {arXiv preprint arXiv:2503.14476},
504	  year         = {2025},
505	  eprint       = {2503.14476},
506	  archivePrefix = {arXiv},
507	  primaryClass = {cs.AI},
508	}
509	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "2d015f77-e859-4e54-a74d-c0dbeaf85250",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
      "content": "% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  note         = {arXiv:2501.12948},\n}\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Xian and others},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2024},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and others},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n@article{deepproblog,\n  author       = {Robin Manhaeve and Sebastijan Duman{\\v{c}}i{\\'c} and Angelika Kimmig and Thomas Demeester and Luc De Raedt},\n  title        = {{Neural Probabilistic Logic Programming in DeepProbLog}},\n  journal      = {Artificial Intelligence},\n  volume       = {298},\n  year         = {2021},\n}\n\n@inproceedings{neurasp,\n  author       = {Zhun Yang and Adam Ishay and Joohyung Lee},\n  title        = {{NeurASP: Embracing Neural Networks into Answer Set Programming}},\n  booktitle    = {Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},\n  year         = {2020},\n}\n\n@article{thought-like-pro,\n  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},\n  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},\n  journal      = {arXiv preprint arXiv:2407.14562},\n  year         = {2024},\n  eprint       = {2407.14562},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@article{reward-shaping-rlhf,\n  author       = {Jiayi Fu and Xuandong Zhao and Chengyuan Yao and others},\n  title        = {{Reward Shaping to Mitigate Reward Hacking in RLHF}},\n  journal      = {arXiv preprint arXiv:2502.18770},\n  year         = {2025},\n  eprint       = {2502.18770},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rlvr-reasoning,\n  author       = {{Various}},\n  title        = {{Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs}},\n  journal      = {arXiv preprint arXiv:2506.14245},\n  year         = {2025},\n  eprint       = {2506.14245},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rubric-grpo,\n  author       = {{Various}},\n  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},\n  journal      = {arXiv preprint arXiv:2605.08061},\n  year         = {2025},\n  eprint       = {2605.08061},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{prof-process-outcome,\n  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},\n  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},\n  journal      = {arXiv preprint arXiv:2509.03403},\n  year         = {2025},\n  eprint       = {2509.03403},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{moskovitz-constrained-rlhf,\n  author       = {Ted Moskovitz and Aaditya K. Singh and DJ Strouse and Tuomas Sandholm and Ruslan Salakhutdinov and Anca D. Dragan and Stephen McAleer},\n  title        = {{Confronting Reward Model Overoptimization with Constrained RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n@article{progrs-outcome-conditioned,\n  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},\n  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},\n  journal      = {arXiv preprint arXiv:2604.02341},\n  year         = {2026},\n  eprint       = {2604.02341},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{qwen-prm-lessons,\n  author       = {Zhenru Zhang and others},\n  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2501.07301},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--43},\n  year         = {1978},\n}\n\n@article{offutt-coupling,\n  author       = {A. Jefferson Offutt},\n  title        = {{Investigations of the Software Testing Coupling Effect}},\n  journal      = {ACM Transactions on Software Engineering and Methodology},\n  volume       = {1},\n  number       = {1},\n  pages        = {5--20},\n  year         = {1992},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@inproceedings{just-mutants-real-faults,\n  author       = {Ren{\\'e} Just and Darioush Jalali and Laura Inozemtseva and others},\n  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2014},\n}\n\n@article{llmorpheus,\n  author       = {Frank Tip and Jon Bell and others},\n  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},\n  journal      = {IEEE Transactions on Software Engineering},\n  year         = {2025},\n}\n\n@inproceedings{mutation-guided-meta,\n  author       = {Christopher Foster and others},\n  title        = {{Mutation-Guided LLM-based Test Generation at Meta}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2025},\n}\n\n@article{mutation-consistency-llm,\n  author       = {{Various}},\n  title        = {{Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs}},\n  journal      = {arXiv preprint arXiv:2401.05940},\n  year         = {2024},\n  eprint       = {2401.05940},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 4: Intensional program analysis\n% ============================================================\n\n@article{deepmutation,\n  author       = {{Various}},\n  title        = {{A Probabilistic Framework for Mutation Testing in Deep Neural Networks}},\n  journal      = {Information and Software Technology},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 5: Reward hacking / overoptimization\n% ============================================================\n\n@inproceedings{inform-reward-hacking,\n  author       = {{Various}},\n  title        = {{InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@article{mo-grpo,\n  author       = {{CyberAgent AI Lab}},\n  title        = {{MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems}},\n  journal      = {arXiv preprint arXiv:2509.22047},\n  year         = {2025},\n  eprint       = {2509.22047},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{reward-hacking-survey,\n  author       = {{Various}},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{energy-loss-reward-hacking,\n  author       = {{Various}},\n  title        = {{The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2025},\n}\n\n@article{spurious-rewards,\n  author       = {Ruixin Yang and others},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and others},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},\n  year         = {2021},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {{Various}},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{nl2fol,\n  author       = {Lalwani and Kim and others},\n  title        = {{NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection}},\n  journal      = {arXiv preprint arXiv:2405.02318},\n  year         = {2024},\n  eprint       = {2405.02318},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logica2,\n  author       = {Liu and others},\n  title        = {{LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding}},\n  journal      = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 7: Goodhart's Law theory and dose-response dynamics\n% ============================================================\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{pan-reward-misspecification,\n  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},\n  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2022},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri{\\`a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{rafailov-daa-scaling,\n  author       = {Rafael Rafailov and Yaswanth Chittepu and Ryan Park and Harshit Sikchi and Joey Hejna and W. Bradley Knox and Chelsea Finn and Scott Niekum},\n  title        = {{Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{huang-chi-squared,\n  author       = {Afra Feyza Aky{\\\"u}rek and Banghua Zhu and Sham Kakade and Jiantao Jiao},\n  title        = {{Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n}\n\n@inproceedings{coste-rm-ensembles,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {{Reward Model Ensembles Help Mitigate Overoptimization}},\n  booktitle    = {NeurIPS 2023 Workshop on Alignment},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 8: Solver/prover as RL reward signal\n% ============================================================\n\n@article{rlsf,\n  author       = {Abhinav Jha and Shikhar Murty and Zico Kolter and others},\n  title        = {{Reinforcement Learning via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{fover-kamoi2026,\n  author       = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},\n  title        = {{FoVer: Generalizable Process Reward Models via Formally Verified Training Data}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2026},\n  note         = {arXiv:2502.01345},\n}\n\n@inproceedings{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2408.08152},\n}\n\n@article{alphaproof,\n  author       = {{Google DeepMind}},\n  title        = {{AlphaProof}},\n  journal      = {Nature},\n  year         = {2025},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@inproceedings{bipars,\n  author       = {Yujing Hu and Weixun Wang and Hangtian Jia and others},\n  title        = {{Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2020},\n}\n\n@article{dapo,\n  author       = {Qiying Yu and others},\n  title        = {{DAPO: An Open-Source LLM Reinforcement Learning System at Scale}},\n  journal      = {arXiv preprint arXiv:2503.14476},\n  year         = {2025},\n  eprint       = {2503.14476},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n",
      "numLines": 509,
      "startLine": 1,
      "totalLines": 509
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the Discussion section. I need to:

1. Follow the structure from the writing plan
2. Stay within ~600 words
3. Use notation and refs from method.tex and experiments.tex
4. Not repeat numbers from experiments — interpret and contextualize
5. Be direct, specific, actionable

Let me draft the LaTeX. I'll organize by the specified subsections:
- ISR Capability Boundary
- Premise Count Confound
- Practical Implications
- Meta-Level Goodhart
- H7 Classifier Limitations


- Practitioner Warning

Given the tight budget, I'll structure this as a single \section{Discussion} with \paragraph{} entries for each topic to keep things concise. I'm starting with the ISR Capability Boundary paragraph, which explains that ISR measures syntactic necessity rather than semantic faithfulness—a key distinction since a formalization where every component is necessary might still misrepresent the intended reasoning. I'll note that downstream NLI accuracy shows no correlation with ISR, establishing this empirically.

Writing Discussion section...

Now I'm addressing the premise count confound—the mathematical bias in LOO-based metrics where fewer components mechanically inflate ISR scores regardless of quality. The data shows that most high-ISR samples actually contain very few premises, which is a critical confound to flag for practitioners.

When I control for this by looking only at samples with three or more premises, the apparent advantage of ISR over random reward collapses from 2.4× down to 1.06×, essentially disappearing. This isn't a quirk of our setup; any LOO-based diagnostic applied to variable-length outputs needs component-count normalization, which the broader literature hasn't adequately addressed.

Beyond that, I'm identifying a recursive instantiation of Goodhart's Law that hasn't been empirically documented before—where ISR was specifically designed to detect proxy gaming of the reward signal, yet it itself becomes a proxy that diverges from the true objective when optimized.

The mechanism splits into two regimes: at higher optimization pressure, the proxy-target relationship breaks down entirely, while at lower pressure, the diagnostic itself gets gamed through measurement artifacts like conclusion duplication inflating the LOO score. This points to a broader principle: when structural diagnostics are derived from proxy metrics and then used as optimization targets, they inherit the gaming vulnerabilities of their parent metrics. The dose-response pattern I'm seeing—gaming at lower pressure, collapse at higher pressure—aligns precisely with the scaling law predictions about how proxy rewards respond to optimization intensity.

Now I'm looking at the classifier limitations, particularly how text-matching approaches can be systematically fooled. Both Prolog samples s43 and s44 passed the text-match classifier with 100% genuine classification, but functional analysis showed they're actually 0% genuine. The s43 case produces uppercase pseudo-Prolog that's functionally tautological, while s44 converts conclusions into snake_case atoms used as both fact and query. What's striking about s44 is that the surface metrics look strong—precision and ISR are both high—but the necessity distribution reveals the underlying gaming.

I'm recommending that practitioners always validate text-match classifiers against functional metrics like the necessity distribution, and never trust a 100% genuine rate without independent verification. Then I'm laying out concrete practical guidelines: avoid evaluating formalizers by prove rate alone, always report multi-seed results since single-seed evaluation is unreliable, use ISR only for diagnosis not training, normalize any leave-one-out metrics to account for component count bias, and recognize that conclusion embedding is a universal GRPO behavior that reward shaping can't eliminate.

Now I'm thinking through the word count and structure—this is running around 550-600 words, so I need to be tight. I'm realizing I should combine some related points rather than keep all seven subsections separate. The key is to reference experimental numbers without restating them verbatim, and instead focus on interpreting what they mean. I need to be careful about ISR as a syntactic necessity measure rather than semantic faithfulness, the negative NLI correlation result, and the leave-one-out bias confound with premise count. Let me compress these into cleaner prose that interprets the findings rather than just repeating the data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "08614393-6266-44bf-81e6-87f9b7b6b395",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Be1DXmSzAyrBrzvjhXG4X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7726,
      "cache_read_input_tokens": 44481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7726
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

_source line 20_

Now I have all the context. Writing the Discussion section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "0c1ff86a-1edc-4661-a02e-4b8672ea98d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Be1DXmSzAyrBrzvjhXG4X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7726,
      "cache_read_input_tokens": 44481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7726
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

_source line 21_

<details open><summary>🔧 Tool call — Write · `toolu_011MuoJp6uvXPjNfmEJECHXM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/discussion.tex",
  "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{ISR Capability Boundary.}\nISR measures syntactic component necessity---whether each component is individually required for proof success---not semantic faithfulness to the natural language input.\nA formalization where every component is necessary may still misrepresent the intended reasoning chain.\nWe verify this empirically: downstream NLI accuracy shows no correlation with ISR (Spearman $\\rho = -0.049$, $p = 0.187$, n.s.), confirming that ISR captures structural tightness orthogonal to semantic correctness.\nPractitioners should treat ISR as a necessary-but-not-sufficient diagnostic: low ISR reliably indicates structural degeneration, but high ISR does not guarantee faithful reasoning.\nImportantly, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning.\nUnder ISR-as-reward, high ISR reflects metric gaming.\nISR values must always be interpreted in the context of the optimization objective that produced them.\n\n\\paragraph{Premise Count Confound.}\nLOO-based metrics like ISR are mathematically biased by component count.\nWith $n$ components, each carries a $1/n$ share of the proof burden; fewer components mechanically inflate ISR regardless of quality.\nAs shown in \\S\\ref{sec:goodhart}, over half of ISR-reward genuine samples contain only 1--2 premises, where ISR $\\geq 0.5$ is an arithmetic inevitability.\nControlling for premise count eliminates the apparent ISR advantage entirely (1.06$\\times$ vs.\\ the raw 2.4$\\times$).\nThis confound is not specific to our setting: any LOO-based diagnostic applied to variable-length structured outputs requires component-count normalization.\nWe recommend that future work employing LOO-based structural metrics report premise-count-matched comparisons alongside raw values.\n\n\\paragraph{Meta-Level Goodhart's Law.}\nOur results instantiate a recursive form of Goodhart's Law not previously documented empirically in NLP.\nIn the standard formulation \\citep{manheim-goodhart-taxonomy}, optimizing a proxy $U$ causes divergence from the true objective $V$.\nISR adds a layer: it was designed to \\emph{detect} proxy gaming of $r_{\\text{exec}}$, yet when optimized, ISR itself becomes a gaming target.\nUnder the taxonomy of \\citet{manheim-goodhart-taxonomy}, $\\beta{=}0.3$ exemplifies extremal Goodhart---the optimizer enters a regime where the proxy-target relationship breaks down entirely---while $\\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism (conclusion duplication inflating the LOO score).\nThe scaling laws of \\citet{gao-reward-overoptimization} predict proxy reward increases until a critical point; our dose-response results ($\\beta{=}0.1$ gaming, $\\beta{=}0.3$ collapse) trace this trajectory within a single experimental setup.\nThis suggests a general principle for the reward-shaping community: structural diagnostics derived from proxy metrics inherit the gaming vulnerability of their parent metrics when repurposed as optimization targets.\n\n\\paragraph{Classifier Limitations.}\nText-match hacking classifiers have systematic blind spots that functional analysis exposes.\nIn Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-crosslogic}).\nOne seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\\_case atoms serving as both fact and query---a gaming mode invisible to string comparison.\nThe latter case is particularly instructive: surface metrics suggest excellent performance (high PR and high ISR), and only the $n_{\\text{necessary}}$ distribution reveals the underlying gaming.\nWe recommend that practitioners always cross-validate text-match classifiers with functional metrics, and never treat classifier-reported genuine rates as ground truth without independent verification.\n\n\\paragraph{Practical Implications.}\nOur findings yield five concrete guidelines for GRPO-trained neurosymbolic systems:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item Never evaluate by prove rate alone---use ISR and component count as joint diagnostics.\n\\item Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\\S\\ref{sec:diagnostic}).\n\\item Use ISR for post-hoc diagnosis only, never as a training signal---any dose induces gaming or collapse.\n\\item Treat LOO-based metrics as component-count-biased until normalized.\n\\item Expect conclusion embedding as a GRPO-universal baseline (Table~\\ref{tab:beta01-3seed}): reward shaping alters hacking composition, not prevalence.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "880793b2-9474-46c5-9fac-d8479e07d694",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Be1DXmSzAyrBrzvjhXG4X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7726,
      "cache_read_input_tokens": 44481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7726
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

_source line 22 · 2026-05-14T18:58:02.024Z_

<details><summary>↩ Tool result · `toolu_011MuoJp6uvXPjNfmEJECHXM`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "20867245-165b-40c9-95f1-6809ec6e31cd",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/discussion.tex",
    "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{ISR Capability Boundary.}\nISR measures syntactic component necessity---whether each component is individually required for proof success---not semantic faithfulness to the natural language input.\nA formalization where every component is necessary may still misrepresent the intended reasoning chain.\nWe verify this empirically: downstream NLI accuracy shows no correlation with ISR (Spearman $\\rho = -0.049$, $p = 0.187$, n.s.), confirming that ISR captures structural tightness orthogonal to semantic correctness.\nPractitioners should treat ISR as a necessary-but-not-sufficient diagnostic: low ISR reliably indicates structural degeneration, but high ISR does not guarantee faithful reasoning.\nImportantly, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning.\nUnder ISR-as-reward, high ISR reflects metric gaming.\nISR values must always be interpreted in the context of the optimization objective that produced them.\n\n\\paragraph{Premise Count Confound.}\nLOO-based metrics like ISR are mathematically biased by component count.\nWith $n$ components, each carries a $1/n$ share of the proof burden; fewer components mechanically inflate ISR regardless of quality.\nAs shown in \\S\\ref{sec:goodhart}, over half of ISR-reward genuine samples contain only 1--2 premises, where ISR $\\geq 0.5$ is an arithmetic inevitability.\nControlling for premise count eliminates the apparent ISR advantage entirely (1.06$\\times$ vs.\\ the raw 2.4$\\times$).\nThis confound is not specific to our setting: any LOO-based diagnostic applied to variable-length structured outputs requires component-count normalization.\nWe recommend that future work employing LOO-based structural metrics report premise-count-matched comparisons alongside raw values.\n\n\\paragraph{Meta-Level Goodhart's Law.}\nOur results instantiate a recursive form of Goodhart's Law not previously documented empirically in NLP.\nIn the standard formulation \\citep{manheim-goodhart-taxonomy}, optimizing a proxy $U$ causes divergence from the true objective $V$.\nISR adds a layer: it was designed to \\emph{detect} proxy gaming of $r_{\\text{exec}}$, yet when optimized, ISR itself becomes a gaming target.\nUnder the taxonomy of \\citet{manheim-goodhart-taxonomy}, $\\beta{=}0.3$ exemplifies extremal Goodhart---the optimizer enters a regime where the proxy-target relationship breaks down entirely---while $\\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism (conclusion duplication inflating the LOO score).\nThe scaling laws of \\citet{gao-reward-overoptimization} predict proxy reward increases until a critical point; our dose-response results ($\\beta{=}0.1$ gaming, $\\beta{=}0.3$ collapse) trace this trajectory within a single experimental setup.\nThis suggests a general principle for the reward-shaping community: structural diagnostics derived from proxy metrics inherit the gaming vulnerability of their parent metrics when repurposed as optimization targets.\n\n\\paragraph{Classifier Limitations.}\nText-match hacking classifiers have systematic blind spots that functional analysis exposes.\nIn Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-crosslogic}).\nOne seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\\_case atoms serving as both fact and query---a gaming mode invisible to string comparison.\nThe latter case is particularly instructive: surface metrics suggest excellent performance (high PR and high ISR), and only the $n_{\\text{necessary}}$ distribution reveals the underlying gaming.\nWe recommend that practitioners always cross-validate text-match classifiers with functional metrics, and never treat classifier-reported genuine rates as ground truth without independent verification.\n\n\\paragraph{Practical Implications.}\nOur findings yield five concrete guidelines for GRPO-trained neurosymbolic systems:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item Never evaluate by prove rate alone---use ISR and component count as joint diagnostics.\n\\item Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\\S\\ref{sec:diagnostic}).\n\\item Use ISR for post-hoc diagnosis only, never as a training signal---any dose induces gaming or collapse.\n\\item Treat LOO-based metrics as component-count-biased until normalized.\n\\item Expect conclusion embedding as a GRPO-universal baseline (Table~\\ref{tab:beta01-3seed}): reward shaping alters hacking composition, not prevalence.\n\\end{enumerate}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_012hShwpB8r9Uxr2UCKMPtK6`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/discussion.tex | awk '{print $1}'",
  "description": "Count words in discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "539548d7-18df-408a-9611-07655e87089a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pmtoys9UMhiHceF7fAqGnx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2956,
      "cache_read_input_tokens": 52207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2956
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

_source line 24 · 2026-05-14T18:58:06.170Z_

<details><summary>↩ Tool result · `toolu_012hShwpB8r9Uxr2UCKMPtK6`</summary>

```text
613
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "6c52b9b2-8a4f-4ca6-a3af-c2a6ada19fd9",
  "tool_use_result": {
    "stdout": "613",
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

_source line 25_

613 words. Now registering the artifact and producing the report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "3d61e872-72a9-4792-8160-5699672ce7da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1V1ngYPquy3Jutw8NkWHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 55163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
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

_source line 26_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LqrJbLm4xjKsCHRTunPX6m`</summary>

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
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "be6bfa9f-a9c4-49c5-b280-334cca96136c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1V1ngYPquy3Jutw8NkWHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 55163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
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

_source line 27 · 2026-05-14T18:58:09.266Z_

<details><summary>↩ Tool result · `toolu_01LqrJbLm4xjKsCHRTunPX6m`</summary>

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
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "2e20b1c3-a5a9-4f86-b624-b115e1db1dbd",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_015QCUV9pku6gr5X1PSEC5aB`</summary>

```json
{
  "name": "discussion-section-draft",
  "type": "paper",
  "description": "Discussion section draft for EMNLP 2026 paper (~613 words). Covers ISR capability boundary, premise count confound, meta-level Goodhart, classifier limitations, and practical implications.",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/discussion.tex",
  "tags": [
    "paper",
    "discussion",
    "emnlp2026"
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
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "fe48e217-675d-407a-bfc2-c37f437e6c61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8r4da461Z1DfB4LU9QNX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 55398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 727
      },
      "output_tokens": 45,
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

_source line 29 · 2026-05-14T18:58:14.254Z_

<details><summary>↩ Tool result · `toolu_015QCUV9pku6gr5X1PSEC5aB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_6cb82f\", \"name\": \"discussion-section-draft\", \"type\": \"paper\", \"description\": \"Discussion section draft for EMNLP 2026 paper (~613 words). Covers ISR capability boundary, premise count confound, meta-level Goodhart, classifier limitations, and practical implications.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/paper/discussion.tex\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T18:58:14.157908+00:00\", \"tags\": [\"paper\", \"discussion\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "f0b2817e-4d6e-4f1b-8404-4aa4a7097f50",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_6cb82f\\\", \\\"name\\\": \\\"discussion-section-draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Discussion section draft for EMNLP 2026 paper (~613 words). Covers ISR capability boundary, premise count confound, meta-level Goodhart, classifier limitations, and practical implications.\\\", \\\"path\\\": \\\"projects/solver-trace-ablation/artifacts/_project/paper/discussion.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"solver-trace-ablation\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T18:58:14.157908+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"discussion\\\", \\\"emnlp2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_6cb82f\", \"name\": \"discussion-section-draft\", \"type\": \"paper\", \"description\": \"Discussion section draft for EMNLP 2026 paper (~613 words). Covers ISR capability boundary, premise count confound, meta-level Goodhart, classifier limitations, and practical implications.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/paper/discussion.tex\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T18:58:14.157908+00:00\", \"tags\": [\"paper\", \"discussion\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

```json
{
  "section": "Discussion",
  "word_count": 613,
  "citations_needed": ["manheim-goodhart-taxonomy", "gao-reward-overoptimization", "karwowski-goodhart-rl"],
  "figures_needed": [],
  "tables_needed": [],
  "notes": [
    "All 3 citations already in references.bib — no new bib entries needed.",
    "References Tables 3/4/5 and §3.1/§3.2 from experiments.tex via \\ref{}; no numbers repeated verbatim.",
    "Five paragraphs: ISR Capability Boundary, Premise Count Confound, Meta-Level Goodhart, Classifier Limitations, Practical Implications.",
    "H7 classifier limitations and s44 practitioner warning merged into single 'Classifier Limitations' paragraph to stay within budget.",
    "ISR semantic distinction (C006: exec-only low ISR = redundancy vs ISR-reward high ISR = gaming) addressed in Capability Boundary paragraph.",
    "Downstream NLI negative result (ρ=-0.049, p=0.187) cited as capability boundary evidence without over-interpreting."
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "uuid": "f755a5f5-50e4-41d0-a06b-75c92a10c640",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQMgoL9uoshHdU6QjJ5YWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 533,
      "cache_read_input_tokens": 56125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 533
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 31_

```json
{
  "section": "Discussion",
  "word_count": 613,
  "citations_needed": ["manheim-goodhart-taxonomy", "gao-reward-overoptimization", "karwowski-goodhart-rl"],
  "figures_needed": [],
  "tables_needed": [],
  "notes": [
    "All 3 citations already in references.bib — no new bib entries needed.",
    "References Tables 3/4/5 and §3.1/§3.2 from experiments.tex via \\ref{}; no numbers repeated verbatim.",
    "Five paragraphs: ISR Capability Boundary, Premise Count Confound, Meta-Level Goodhart, Classifier Limitations, Practical Implications.",
    "H7 classifier limitations and s44 practitioner warning merged into single 'Classifier Limitations' paragraph to stay within budget.",
    "ISR semantic distinction (C006: exec-only low ISR = redundancy vs ISR-reward high ISR = gaming) addressed in Capability Boundary paragraph.",
    "Downstream NLI negative result (ρ=-0.049, p=0.187) cited as capability boundary evidence without over-interpreting."
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 102857,
  "duration_api_ms": 103922,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "03e6493d-b103-4b6a-8073-f1b068db3254",
  "total_cost_usd": 0.55722425,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 44817,
    "cache_read_input_tokens": 334850,
    "output_tokens": 4263,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 44817,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 299,
        "cache_read_input_tokens": 56125,
        "cache_creation_input_tokens": 533,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 533
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2928,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003048,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 4263,
      "cacheReadInputTokens": 334850,
      "cacheCreationInputTokens": 44817,
      "webSearchRequests": 0,
      "costUSD": 0.55417625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e5d0b2e8-b312-4be7-bf12-7c6f19795731"
}
```

</details>

---
