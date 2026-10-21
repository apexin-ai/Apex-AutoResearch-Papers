# paper compress page overflow

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/workers/worker_paper_compress-page-overflow_20260517T154552.log`
- **Structured JSON:** [`4ef67c604e8280e524e6.json`](../../sessions/4e/4ef67c604e8280e524e6.json)

## Before a recorded user message

70 recorded events

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
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
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
  "uuid": "d7db7c50-c127-481c-bf54-60b0b8c5746f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1779046200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0f060e3f-eb4b-454b-82c4-3ca817cb2b30",
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772"
}
```

---

### Assistant

_source line 4_

Let me start by reading the relevant files to understand the current content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "7e7958ed-419b-48bb-954d-eb90a32f9b54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x23hREJb6ysFr4BBRCszG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16130,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16130
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

<details open><summary>🔧 Tool call — Read · `toolu_01SRsFPB3fLmyfAKMp8mQdD7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "a1aa55fe-1401-45e3-a227-27b833be4b4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x23hREJb6ysFr4BBRCszG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16130,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16130
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

_source line 6 · 2026-05-17T15:46:05.786Z_

<details><summary>↩ Tool result · `toolu_01SRsFPB3fLmyfAKMp8mQdD7`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural collapse invisible to prove rate (\S\ref{sec:diagnostic}); repurposed as a training signal, ISR produces Goodhart collapse at all four tested doses (\S\ref{sec:goodhart}), consistent across logic types, model scales, and training durations.
5	In the \citet{manheim-goodhart-taxonomy} taxonomy, ISR's collapse is primarily regressional with extremal elements.
6	The empirical details, including collapse at micro-doses, non-monotonic dose-response, and stochastic bifurcation, exceed abstract Goodhart predictions.
7	At 500 steps, ISR increases genuine proofs relative to random controls ($\text{OR}_{\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.
8	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
9	
10	\paragraph{Practical implications.}
11	$\beta$ controls the \emph{timing} of collapse, not whether it occurs (\S\ref{sec:goodhart}); snapshot evaluation overestimates ISR's benefit.
12	Text-match classifiers have systematic blind spots (\S\ref{sec:taxonomy}), and different model capacities converge to different exploits with no safe scale observed (\S\ref{sec:crossscale}, \S\ref{sec:limitations}).
13	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "76791be0-ecb6-4e7b-8e1e-5f1ed9d9cd5f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural collapse invisible to prove rate (\\S\\ref{sec:diagnostic}); repurposed as a training signal, ISR produces Goodhart collapse at all four tested doses (\\S\\ref{sec:goodhart}), consistent across logic types, model scales, and training durations.\nIn the \\citet{manheim-goodhart-taxonomy} taxonomy, ISR's collapse is primarily regressional with extremal elements.\nThe empirical details, including collapse at micro-doses, non-monotonic dose-response, and stochastic bifurcation, exceed abstract Goodhart predictions.\nAt 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\n\n\\paragraph{Practical implications.}\n$\\beta$ controls the \\emph{timing} of collapse, not whether it occurs (\\S\\ref{sec:goodhart}); snapshot evaluation overestimates ISR's benefit.\nText-match classifiers have systematic blind spots (\\S\\ref{sec:taxonomy}), and different model capacities converge to different exploits with no safe scale observed (\\S\\ref{sec:crossscale}, \\S\\ref{sec:limitations}).\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01BQgHTCrgoUh8riTqP5e4oE`</summary>

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
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "62724199-6a01-4143-8802-06e46fec57f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x23hREJb6ysFr4BBRCszG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16130,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16130
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

_source line 8 · 2026-05-17T15:46:06.252Z_

<details><summary>↩ Tool result · `toolu_01BQgHTCrgoUh8riTqP5e4oE`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
27	
28	\begin{algorithm}[t]
29	\caption{Solver Trace Ablation (STA)}
30	\label{alg:sta}
31	\begin{algorithmic}[1]
32	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
33	\ENSURE $\text{ISR}(x) \in [0, 1]$
34	\STATE $\textit{necessary} \gets 0$
35	\FOR{$i = 1$ to $n$}
36	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
37	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
38	    \ENDIF
39	\ENDFOR
40	\RETURN $\textit{necessary} \,/\, n$
41	\end{algorithmic}
42	\end{algorithm}
43	
44	\paragraph{Intensional Structural Reward.}
45	ISR is the fraction of necessary components:
46	\begin{equation}
47	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
48	  \label{eq:isr}
49	\end{equation}
50	ISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.
51	We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.
52	
53	\paragraph{Limitations of ISR and the premise-count confound.}
54	ISR measures syntactic component necessity, not semantic faithfulness: a formalization can achieve $\text{ISR}{=}1$ while remaining semantically unrelated to the NL input (e.g., a single premise identical to the conclusion).
55	Critically, ISR is sensitive to component count $n$: when $n{=}2$, $\text{ISR}\geq 0.5$ regardless of proof quality; more generally, fewer components mechanically inflate ISR because each is more likely to be individually necessary.
56	This confound is central to ISR's Goodhart vulnerability (\S\ref{sec:goodhart}): H7 tautologies (single premise $=$ conclusion) achieve $\text{ISR}{\geq}0.5$ by construction, and non-collapsed seeds produce shorter formalizations (mean $n{=}5.58$ vs.\ $8.46$ for random), inflating ISR mechanically; premise-count-matched comparison eliminates the difference ($1.06\times$).
57	ISR functions as a diagnostic but fails as a training signal at every tested dose because optimization exploits the metric's structural bias rather than improving reasoning quality.
58	We recommend that any LOO-based metric on variable-length outputs report component-count-matched comparisons alongside raw values.
59	
60	\paragraph{LOO vs.\ Shapley values.}
61	Shapley values~\citep{shapley-1953} provide a theoretically grounded alternative to LOO for measuring component contribution, accounting for interaction effects between premises.
62	We chose LOO for three reasons: (1) $O(n)$ rather than $O(2^n)$ cost, critical for repeated evaluation during RL training; (2) it directly answers the diagnostic question ``is this component necessary for the proof?'' rather than measuring marginal contribution; and (3) the Goodhart effects we document would likely transfer to Shapley-based metrics, since the gaming strategies (e.g., single-premise tautology achieving ISR${\geq}0.5$) exploit the numerics of \emph{any} component-necessity measure, not LOO specifically.
63	
64	\paragraph{$O(1)$ ablation variant.}
65	A cheaper $O(1)$ binary variant produces near-zero ISR ($\text{ISR}^*{=}0.007$) indistinguishable from exec-only, confirming that per-clause LOO is necessary for ISR to carry a structural signal (Appendix~\ref{app:o1-ablation}).
66	
67	\subsection{Reward Conditions and Hacking Modes}
68	\label{sec:rewards}
69	\label{sec:taxonomy-method}
70	
71	We study six primary conditions: exec-only ($r_{\text{exec}}$), ISR reward ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations), with supplementary ISR dose points at $\beta\in\{0.05,0.2\}$ for dose-response analysis.
72	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
73	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
74	Each RL condition uses seeds $\{42,43,44\}$ and identical training data.
75	An earlier convex formulation ($\alpha r_{\text{exec}} + \beta r_{\text{exec}}\text{ISR}$, $\alpha{+}\beta{=}1$) was discarded because $\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\ref{app:setup}).
76	
77	\paragraph{Hacking taxonomy.}
78	Across conditions, seeds, and logic types we identify nine structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}): \textbf{H1} (conclusion embedding), \textbf{H7a/b} (single-premise tautology, standard and obfuscated), \textbf{H8} (premise-subset gaming), \textbf{H9} (contradiction injection, 1.7B only), tautological collapse, repetition collapse, complexity-without-utility, contradiction explosion, and query-as-fact gaming (Prolog-specific).
79	Modes are identified by strict text matching (H1/H7) plus functional $n_{\text{necessary}}$ analysis; the taxonomy is independently applicable to any neurosymbolic system with inspectable premise--conclusion structure.
80	We distinguish two failure semantics: exec-only \emph{low} ISR signals \emph{redundancy}, whereas ISR-rewarded \emph{high} ISR signals \emph{metric gaming}; the mode breakdown, not bare ISR, licenses reasoning-quality conclusions.
81	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "3ad59d30-7841-4cb6-b4c7-8ab5f149401c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\n\\subsection{Task and GRPO Training}\n\\label{sec:task}\n\nGiven premises $P_1,\\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\\{c_1,\\ldots,c_n\\}$ verified by an external solver $S\\in\\{\\text{Prover9, SWI-Prolog}\\}$ (Figure~\\ref{fig:sta-overview}a).\nWe train with Group Relative Policy Optimization (GRPO)~\\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\\text{exec}}(x) = \\mathbf{1}[S(F_x){=}\\textit{proved}]$.\nThis optimizes prove rate but provides no signal about \\emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.\nAll experiments draw from FOLIO~\\citep{folio}; the held-out evaluation file retains a legacy \\texttt{proofwriter\\_fol\\_*.jsonl} filename (from ProofWriter~\\citep{proofwriter}) but contains only FOLIO-derived examples.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\nSTA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\\ref{fig:sta-overview}b).\nGiven a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\\setminus\\{c_i\\}$ and re-runs the solver (Algorithm~\\ref{alg:sta}).\nA component is \\emph{necessary} if its removal causes proof failure.\nWhat constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.\nLOO ablation itself is standard in mutation testing and sensitivity analysis~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Proved formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE $\\text{ISR}(x) \\in [0, 1]$\n\\STATE $\\textit{necessary} \\gets 0$\n\\FOR{$i = 1$ to $n$}\n    \\IF{$S(x \\setminus \\{c_i\\}) = \\textit{failed}$}\n        \\STATE $\\textit{necessary} \\gets \\textit{necessary} + 1$\n    \\ENDIF\n\\ENDFOR\n\\RETURN $\\textit{necessary} \\,/\\, n$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Intensional Structural Reward.}\nISR is the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n}\\sum_{i=1}^{n}\\mathbf{1}\\bigl[S(x\\setminus\\{c_i\\})=\\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.\nWe report \\emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.\n\n\\paragraph{Limitations of ISR and the premise-count confound.}\nISR measures syntactic component necessity, not semantic faithfulness: a formalization can achieve $\\text{ISR}{=}1$ while remaining semantically unrelated to the NL input (e.g., a single premise identical to the conclusion).\nCritically, ISR is sensitive to component count $n$: when $n{=}2$, $\\text{ISR}\\geq 0.5$ regardless of proof quality; more generally, fewer components mechanically inflate ISR because each is more likely to be individually necessary.\nThis confound is central to ISR's Goodhart vulnerability (\\S\\ref{sec:goodhart}): H7 tautologies (single premise $=$ conclusion) achieve $\\text{ISR}{\\geq}0.5$ by construction, and non-collapsed seeds produce shorter formalizations (mean $n{=}5.58$ vs.\\ $8.46$ for random), inflating ISR mechanically; premise-count-matched comparison eliminates the difference ($1.06\\times$).\nISR functions as a diagnostic but fails as a training signal at every tested dose because optimization exploits the metric's structural bias rather than improving reasoning quality.\nWe recommend that any LOO-based metric on variable-length outputs report component-count-matched comparisons alongside raw values.\n\n\\paragraph{LOO vs.\\ Shapley values.}\nShapley values~\\citep{shapley-1953} provide a theoretically grounded alternative to LOO for measuring component contribution, accounting for interaction effects between premises.\nWe chose LOO for three reasons: (1) $O(n)$ rather than $O(2^n)$ cost, critical for repeated evaluation during RL training; (2) it directly answers the diagnostic question ``is this component necessary for the proof?'' rather than measuring marginal contribution; and (3) the Goodhart effects we document would likely transfer to Shapley-based metrics, since the gaming strategies (e.g., single-premise tautology achieving ISR${\\geq}0.5$) exploit the numerics of \\emph{any} component-necessity measure, not LOO specifically.\n\n\\paragraph{$O(1)$ ablation variant.}\nA cheaper $O(1)$ binary variant produces near-zero ISR ($\\text{ISR}^*{=}0.007$) indistinguishable from exec-only, confirming that per-clause LOO is necessary for ISR to carry a structural signal (Appendix~\\ref{app:o1-ablation}).\n\n\\subsection{Reward Conditions and Hacking Modes}\n\\label{sec:rewards}\n\\label{sec:taxonomy-method}\n\nWe study six primary conditions: exec-only ($r_{\\text{exec}}$), ISR reward ($r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ at $\\beta\\in\\{0.1,0.3\\}$), matched random controls ($r_{\\text{exec}}\\cdot(1{+}\\beta u)$, $u\\sim\\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations), with supplementary ISR dose points at $\\beta\\in\\{0.05,0.2\\}$ for dose-response analysis.\nMultiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.\nRandom isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.\nEach RL condition uses seeds $\\{42,43,44\\}$ and identical training data.\nAn earlier convex formulation ($\\alpha r_{\\text{exec}} + \\beta r_{\\text{exec}}\\text{ISR}$, $\\alpha{+}\\beta{=}1$) was discarded because $\\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\\ref{app:setup}).\n\n\\paragraph{Hacking taxonomy.}\nAcross conditions, seeds, and logic types we identify nine structural-degeneration modes (full definitions in Appendix~\\ref{app:hacking-modes}): \\textbf{H1} (conclusion embedding), \\textbf{H7a/b} (single-premise tautology, standard and obfuscated), \\textbf{H8} (premise-subset gaming), \\textbf{H9} (contradiction injection, 1.7B only), tautological collapse, repetition collapse, complexity-without-utility, contradiction explosion, and query-as-fact gaming (Prolog-specific).\nModes are identified by strict text matching (H1/H7) plus functional $n_{\\text{necessary}}$ analysis; the taxonomy is independently applicable to any neurosymbolic system with inspectable premise--conclusion structure.\nWe distinguish two failure semantics: exec-only \\emph{low} ISR signals \\emph{redundancy}, whereas ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming}; the mode breakdown, not bare ISR, licenses reasoning-quality conclusions.\n",
      "numLines": 81,
      "startLine": 1,
      "totalLines": 81
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01EtiAPgyGHZSs5hkyHi9fhm`</summary>

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
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "c3d58f56-d40e-4a31-84cf-ae5197c23394",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x23hREJb6ysFr4BBRCszG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16130,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16130
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

_source line 10 · 2026-05-17T15:46:06.479Z_

<details><summary>↩ Tool result · `toolu_01EtiAPgyGHZSs5hkyHi9fhm`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}) with greedy decoding (Appendix~\ref{app:setup}).
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples have $\text{ISR}{=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
21	\label{fig:isr-collapse}
22	\end{figure}
23	
24	\textbf{Collapse trajectory.}
25	Figure~\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.
26	PR rises $32\%\to93\%\to96\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\text{ISR}^*$ tells the opposite story, $0.642\to0.132\to0.003$ (214$\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
27	By 500 steps, 87.1\% of proved samples embed the conclusion (H1); by 1000 steps, the embedding rate saturates at 100\% and mean component count more than doubles ($6.58\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.
28	Extended training, lacking a structural signal, \emph{worsens} formalization quality while improving the headline number.
29	
30	\textbf{Cross-seed instability.}
31	The three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\ref{app:detailed-results}): s42 reaches $\text{PR}{=}93\%$ via conclusion embedding ($\text{H1}{=}87\%$); s43 collapses to $\text{PR}{=}13\%$ (at 500 steps) via repetition (87\% of rollouts truncated); s44 reaches $\text{PR}{=}98\%$ via tautological collapse ($\text{H7}{=}100\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
32	The cross-seed PR variance ($\sigma{=}47$\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).
33	By 1000 steps, all three converge to high PR ($0.95{\pm}0.05$) with near-zero genuine output (see Appendix~\ref{app:h8} and Table~\ref{tab:fol-detailed}), each through a different dominant mode (s42: $\text{ISR}^{*}{=}0.003$, taxonomy unavailable; s43: H1 $93.8\%$, genuine $6.2\%$; s44: H1 $85\%$ + H8 $15\%$). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2
34	Notably, s43 recovers from $\text{PR}{=}13\%$ (500 steps) to $\text{PR}{=}96\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.
35	
36	\textbf{SFT baseline.}
37	SFT on gold formalizations reaches $\text{PR}{=}13.0\%$ (3-seed pooled, 1000 steps) with $\text{H7}{=}0$, $\text{H1}{=}7.7\%$, $92.3\%$ non-hacking ($n{=}39$; $\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$; per-seed range ${\sim}$91--93\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
38	The near-absence of hacking under identical data exposure is consistent with hacking being RL-specific; a 100-step checkpoint confirms hacking emerges early in training (Appendix~\ref{app:100step}).
39	SFT trains via negative log-likelihood on gold formalizations without exploration-exploitation dynamics; exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training.
40	
41	\subsection{ISR as Reward: Goodhart Effects}
42	\label{sec:goodhart}
43	
44	We now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with a matched random control, $r = r_{\text{exec}}\cdot(1 + \beta\,u)$, $u\sim\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.
45	The headline finding: ISR contains an inherent Goodhart vulnerability~\citep{manheim-goodhart-taxonomy} observed to produce collapse at all four tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$).
46	The mechanism is structural: tautological proofs ($P{\to}P$) receive $\text{ISR}{=}0.75$ and single-premise-equals-conclusion constructions receive $\text{ISR}{\geq}0.5$, both by the LOO definition alone.
47	Once sampled during GRPO rollouts, these high-ISR tautologies create a positive feedback loop; $\beta$ controls only the \emph{timing} of collapse, not whether it occurs.
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\resizebox{\columnwidth}{!}{%
53	\begin{tabular}{lcccccc}
54	\toprule
55	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} \\
56	\midrule
57	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
58	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
59	\midrule
60	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)
61	ISR$^\ddagger$ & 0.1 & 70{\scriptsize$\pm$19} & --- & \textbf{54} & 18 & 23$^\star$ \\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)
62	Random & 0.1 & \textbf{83}{\scriptsize$\pm$15} & 0.080{\scriptsize$\pm$.06} & 30 & 59 & 8 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)
63	ISR & 0.2 & 97{\scriptsize$\pm$4} & 0.69{\scriptsize$\pm$.24} & \textbf{99} & 0 & 0 \\ %% registry: sweep-isr-b02-s42/s43/s44 (3-seed; Appendix Table~\ref{tab:beta02-detail})
64	\midrule
65	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
66	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
67	\midrule
68	\multicolumn{7}{l}{\textit{Qwen3-1.7B (seed~42)}} \\
69	ISR & 0.1 & 100 & 0.600 & 0 & \textbf{100} & 0 \\ %% registry: d113-1.7b-isr-b01-s42
70	Random & 0.1 & 93 & 0.028 & 0 & 0 & 0 \\ %% registry: d113-1.7b-random-b01-s42 (H9=100%)
71	ISR & 0.3 & 17 & 0.031 & 0 & 71 & 29 \\ %% registry: d113-1.7b-isr-b03-s42
72	\bottomrule
73	\end{tabular}}
74	\caption{Goodhart landscape across reward conditions. PR/ISR$^*$: mean$\pm$std of per-seed values; H7/H1/N-H: pooled percentages. ISR$^*$ for ISR $\beta{=}0.1$ omitted (inflated by H7 gaming; premise-count-matched value is $1.06\times$ random, \S\ref{sec:goodhart}). 1.7B ISR $\beta{=}0.1$: fixed-template H1, zero-variance; 1.7B Random: 100\% H9 (ex falso, not in H7/H1 columns). $^\dagger$Single seed (s42), greedy decoding, 500 steps. 3-seed 1000-step data (s42/s43/s44) in Appendix Table~\ref{tab:exec-only-1000}; all converge to ${\geq}94\%$ PR with near-zero genuine. $^\ddagger$ISR $\beta{=}0.1$ s43/s44: H8 audit unavailable; N-H may be slightly inflated. $^\star$5-seed pooled, transient; collapses to ${\sim}2\%$ at 1000 steps (\S\ref{sec:goodhart-temporal}). Per-seed breakdown in Appendix Table~\ref{tab:fol-beta01-perseed}.}
75	\label{tab:goodhart-landscape}
76	\end{table}
77	
78	
79	\textbf{Low-dose ISR ($\beta{=}0.1$): stochastic delayed collapse.}
80	At $\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\geq}97\%$ H7, $0\%$ genuine within ${\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.
81	The 5-seed pooled non-hacking rate is ${\sim}23\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\%$ to $55\%$ genuine.
82	This bifurcation is stochastic: all seeds are indistinguishable in the first ${\sim}100$ steps ($\text{ISR}{\approx}0.05$--$0.07$); divergence occurs at steps 150--200 when H7 tautologies, which receive $\text{ISR}{\geq}0.5$ by construction, are sampled during rollouts and reinforced via the positive feedback loop.
83	Once a seed enters the H7 basin, convergence to saturation takes ${\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46
84	
85	H7 (a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by the LOO definition; \S\ref{sec:taxonomy-method}) is the canonical Goodhart exploit: the model satisfies the structural metric directly rather than producing a genuine derivation.
86	Total conclusion embedding ($\text{H1}+\text{H7}$) is GRPO-universal at $68$--$100\%$ across both ISR and random conditions (Appendix Figure~\ref{fig:hacking-composition}); the specific mode (H7 vs.\ H1) within a seed is stochastic under both conditions ($\text{CV}{>}1$), though ISR modestly increases H7 probability by providing a direct reward pathway.
87	Random yields higher PR ($83{\pm}15\%$ vs.\ $70{\pm}19\%$; $n{=}5$ each).
88	Random H7 exhibits extreme seed dependence (per-seed range: $0\%$--$91.5\%$; pooled $30\%$ is dominated by s46 at $91.5\%$ and s43 at $38.3\%$).
89	Both conditions produce H7 in 2 of 5 seeds, but the quality differs: ISR-induced H7 is absorbing ($100\%$ of proved samples in affected seeds: s43${=}61/61$, s44${=}89/89$), while random-induced H7 coexists with other modes ($38$--$92\%$).
90	ISR's reward signal converts H7 from a stochastic possibility into an irreversible attractor once sampled.
91	The reward landscape explains H7's attractor strength: H7 tautologies receive expected reward $1{+}0.75\beta$ versus ${\sim}1{+}0.26\beta$ for genuine proofs (premise-count-matched), a gap of ${\sim}0.49\beta$ that creates a persistent gradient toward tautological constructions regardless of dose.
92	
93	\textbf{The transient genuine window.}
94	During the transient window, Cochran--Mantel--Haenszel tests stratified by seed confirm ISR produces more genuine proofs than random controls ($\text{OR}_{\text{CMH}}{=}3.37$, 95\% CI $[2.21, 5.13]$, $p{<}10^{-9}$; Appendix Table~\ref{tab:fol-beta01-perseed}).
95	Pooled Fisher ($\text{OR}{=}3.48$, uncorrected) is consistent but does not account for within-seed dependence.
96	Under stricter H8+FN-corrected classification (3-seed subset with complete audits), the effect reverses ($\text{OR}{=}0.61$, n.s.), reflecting both the conservative bias of H8 correction (which reclassifies borderline samples as hacking) and the reduced sample size ($n{=}231$ vs 350). The 5-seed CMH and 3-seed corrected analyses bound the true effect from above and below respectively.
97	The pooled 5-seed non-hacking rate is 23\% (uncorrected; s42-only H8-corrected estimate: 17\%).
98	This benefit is temporary: extended training (1000 steps) on seeds~42 and~45 confirms the window closes completely ($17\%{\to}2\%$ and $55\%{\to}0\%$ genuine respectively; see below).
99	The same LOO bias that enables genuine improvement (rewarding necessary premises) also creates the Goodhart attractor (rewarding tautological constructions); the genuine window reflects seeds that have not yet sampled the H7 exploit, not seeds that resist it.
100	Snapshot evaluation at 500 steps would overestimate ISR's benefit; trajectory analysis is required to distinguish transient from stable improvement. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000
101	
102	\textbf{Premise-count confound.}
103	The genuine-rate advantage reflects a selection effect: premise-count-matched comparison yields only $1.06\times$ ISR difference, confirming indistinguishable per-proof quality once LOO bias toward short outputs is controlled (Appendix~\ref{app:extended-discussion}).
104	
105	\textbf{Trajectory analysis: timing, not destiny.}\label{sec:goodhart-temporal}
106	Extended training (1000 steps; Appendix Figure~\ref{fig:training-isr-curves}) confirms the genuine window is transient across seeds.
107	Seed~42 declines from $17\%$ to $2\%$ genuine via H7 saturation ($16.0\%{\to}96.7\%$ H7, PR stable at ${\sim}96\%$); seed~45, which achieved the highest 500-step genuine rate ($55\%$), collapses to $0\%$ genuine through reward collapse ($\text{PR}: 42\%{\to}2\%$).
108	The two seeds exhibit distinct failure paths (H7 gaming vs.\ output collapse) but converge to the same outcome: zero genuine proofs at extended training. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42, plan002-b01-s45-1000
109	
110	\textbf{Micro-dose ISR ($\beta{=}0.05$): deterministic collapse.}
111	All three ISR seeds reach $\text{PR}{\geq}99\%$ but converge to H7a tautology (H7 $87$--$100\%$, genuine $5.1\%$), while the random control mostly fails to learn (median $\text{PR}{=}7\%$) with zero H7, confirming H7 as specific to ISR's LOO structure.
112	Below a signal-floor, ISR's genuine component is undetectable while its H7 bias remains exploitable (per-seed breakdown in Appendix~\ref{app:beta005}). %% registry: sweep-isr-b005-s42/s43/s44, sweep-random-b005-s42/s43/s44
113	
114	\textbf{Medium-dose ISR ($\beta{=}0.2$): maximum exploitation.}
115	All three seeds converge to pure H7a tautology ($0\%$ non-hacking, $n{=}290$; Appendix Table~\ref{tab:beta02-detail}). %% registry: sweep-isr-b02-s42/s43/s44
116	
117	\textbf{High-dose ISR ($\beta{=}0.3$): multi-modal Goodhart.}
118	At $\beta{=}0.3$, ISR produces extreme cross-seed instability ($\text{PR}{=}66{\pm}42\%$): three seeds yield three distinct failure modes (reward collapse, H1 shortcutting, pure H7 gaming; per-seed details in Appendix~\ref{app:beta03}).
119	The random control is equally unstable ($\text{PR}{=}54{\pm}35\%$) with $91\%$ H1 and ${\leq}4\%$ non-hacking; high-dose proxy weighting destabilizes training regardless of signal source. %% registry: plan002-additive-b03-s42/s43/s44
120	ISR vs.\ random H7 at $\beta{=}0.3$: $\text{OR}{=}13.7$, 95\% CI $[7.0, 26.8]$ (Appendix~\ref{app:beta03}).
121	
122	\textbf{Non-monotonic dose-response.}
123	The four $\beta$ levels reveal a non-monotonic pattern: $\beta\in\{0.05, 0.2\}$ converge deterministically to H7 collapse (${\geq}94\%$ H7), $\beta{=}0.3$ triggers multi-modal instability, and only $\beta{=}0.1$ sustains a transient genuine window (3 of 5 seeds).
124	Goodhart collapse is not a simple function of dose; the balance between genuine and exploit reinforcement depends on a threshold interaction between $\beta$ and rollout stochasticity.
125	
126	\subsection{Cross-Logic Diagnostic Transfer}
127	\label{sec:crosslogic}
128	
129	We replicate the FOL pipeline with Prolog/SWI-Prolog (3 seeds, $\beta{=}0.1$).
130	Under exec-only training, 2/3 seeds show $\text{ISR}^{*}{\approx}0$ despite $\text{PR}{\geq}0.56$, reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding; ISR flags both failure semantics.
131	Under ISR reward, 3/3 seeds reach $0\%$ non-hacking through three distinct mechanisms: clean H7 tautology (s42, $\text{ISR}^{*}{=}1.0$), degenerate uppercase pseudo-Prolog evading text-match classifiers (s43, functional $n_{\text{necessary}}{=}1$), and query-as-fact gaming (s44, $95/97$ proved at $n_{\text{necessary}}{=}1$).
132	Seed~44 evaded our strict classifier entirely; functional cross-validation was required to expose it.
133	We attribute complete collapse to Prolog's simpler operational semantics providing a broader gaming basin (detailed results in Appendix Table~\ref{tab:prolog-detailed} and Figure~\ref{fig:prolog-comparison}).
134	
135	\subsection{Cross-Scale Evidence}
136	\label{sec:crossscale}
137	
138	We train Qwen3-1.7B under ISR $\beta\in\{0.1,0.3\}$ and Random $\beta{=}0.1$ (single seed, 500 steps).
139	All conditions produce $0\%$ non-hacking, but the exploit modes differ qualitatively from 4B: Random discovers H9 (contradiction injection, $\text{PR}{=}93\%$, $100\%$ \emph{ex falso}), ISR $\beta{=}0.1$ collapses to a single fixed template ($\text{ISR}^{*}{=}0.6$ at zero variance, $100\%$ H1), and ISR $\beta{=}0.3$ triggers reward collapse ($\text{PR}{=}17\%$) mirroring the 4B pattern.
140	H9 never appears at 4B scale; fixed-template mode collapse never appears at 4B; different capacities converge to different Goodhart basins under identical rewards.
141	No safe scale was observed in this single-seed comparison (Table~\ref{tab:hacking-taxonomy}).
142	
143	\subsection{Hacking Taxonomy}
144	\label{sec:taxonomy}
145	
146	
147	\begin{table}[t]
148	\centering
149	\small
150	\resizebox{\columnwidth}{!}{%
151	\begin{tabular}{lccccccc}
152	\toprule
153	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} & \textbf{1.7B$_{\text{ISR}}$} & \textbf{1.7B$_{\text{Rnd}}$} \\
154	\midrule
155	H1 embed       & 87 & 18 & 59 & 7 & 0$^\sharp$ & \textbf{100} & 0 \\
156	H7 duplicate   & 0  & \textbf{54} & 30 & 0 & 100$^\sharp$ & 0 & 0 \\
157	H8 prem-subset & 6  & 5  & 8   & 0 & --- & 0 & 0 \\
158	H9 ex falso    & --- & --- & --- & --- & --- & 0 & \textbf{100} \\
159	Tautological   & --- & --- & --- & --- & s42 & --- & --- \\
160	Repetition     & s43 & --- & --- & --- & --- & --- & --- \\
161	Contradiction  & 1k & --- & --- & --- & --- & --- & --- \\
162	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- & --- & --- \\
163	Query-as-fact  & --- & --- & --- & --- & s44 & --- & --- \\
164	\midrule
165	\textbf{Non-hacking} & 8  & \textbf{23}  & 8 & \textbf{92} & \textbf{0} & \textbf{0} & \textbf{0} \\
166	\bottomrule
167	\end{tabular}}
168	\caption{Nine hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random 4B: pooled across 5 seeds; 1.7B columns: Qwen3-1.7B seed~42). H7 includes subtypes H7a (text-match) and H7b (obfuscated tautology; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
169	\label{tab:hacking-taxonomy}
170	\end{table}
171	
172	The nine modes (Table~\ref{tab:hacking-taxonomy}; definitions in Appendix~\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 conditions.
173	H1, H7, and H8 account for ${>}90\%$ of hacking; H7 includes obfuscated subtype H7b ($14/350$) that evades text-match classifiers (\S\ref{sec:discussion}).
174	ISR modestly increases H7 convergence probability ($\text{OR}{=}2.84$, $p{<}5{\times}10^{-12}$, 5-seed; Appendix Table~\ref{tab:bootstrap-ci}), but per-seed variance dominates (Random s46: $91.5\%$ H7; ISR s46: $14.3\%$).
175	All GRPO conditions show ${\geq}80\%$ pooled hacking; only SFT achieves $92.3\%$ non-hacking.
176	Cochran--Mantel--Haenszel tests stratified by seed confirm both effects (H7: $\text{OR}_{\text{CMH}}{=}2.46$, $p{<}10^{-15}$; genuine: $\text{OR}_{\text{CMH}}{=}3.37$, $p{<}10^{-9}$), indicating that the associations are robust to within-seed clustering.
177	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "50f889d4-42f7-4bc8-b88a-07b94187cdc8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nCross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\\S\\ref{sec:crossscale}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}) with greedy decoding (Appendix~\\ref{app:setup}).\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps, the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ (at 500 steps) via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}47$\\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nBy 1000 steps, all three converge to high PR ($0.95{\\pm}0.05$) with near-zero genuine output (see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: $\\text{ISR}^{*}{=}0.003$, taxonomy unavailable; s43: H1 $93.8\\%$, genuine $6.2\\%$; s44: H1 $85\\%$ + H8 $15\\%$). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2\nNotably, s43 recovers from $\\text{PR}{=}13\\%$ (500 steps) to $\\text{PR}{=}96\\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$; per-seed range ${\\sim}$91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific; a 100-step checkpoint confirms hacking emerges early in training (Appendix~\\ref{app:100step}).\nSFT trains via negative log-likelihood on gold formalizations without exploration-exploitation dynamics; exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training.\n\n\\subsection{ISR as Reward: Goodhart Effects}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nThe headline finding: ISR contains an inherent Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy} observed to produce collapse at all four tested doses ($\\beta\\in\\{0.05, 0.1, 0.2, 0.3\\}$).\nThe mechanism is structural: tautological proofs ($P{\\to}P$) receive $\\text{ISR}{=}0.75$ and single-premise-equals-conclusion constructions receive $\\text{ISR}{\\geq}0.5$, both by the LOO definition alone.\nOnce sampled during GRPO rollouts, these high-ISR tautologies create a positive feedback loop; $\\beta$ controls only the \\emph{timing} of collapse, not whether it occurs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nISR$^\\ddagger$ & 0.1 & 70{\\scriptsize$\\pm$19} & --- & \\textbf{54} & 18 & 23$^\\star$ \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)\nRandom & 0.1 & \\textbf{83}{\\scriptsize$\\pm$15} & 0.080{\\scriptsize$\\pm$.06} & 30 & 59 & 8 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)\nISR & 0.2 & 97{\\scriptsize$\\pm$4} & 0.69{\\scriptsize$\\pm$.24} & \\textbf{99} & 0 & 0 \\\\ %% registry: sweep-isr-b02-s42/s43/s44 (3-seed; Appendix Table~\\ref{tab:beta02-detail})\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-1.7B (seed~42)}} \\\\\nISR & 0.1 & 100 & 0.600 & 0 & \\textbf{100} & 0 \\\\ %% registry: d113-1.7b-isr-b01-s42\nRandom & 0.1 & 93 & 0.028 & 0 & 0 & 0 \\\\ %% registry: d113-1.7b-random-b01-s42 (H9=100%)\nISR & 0.3 & 17 & 0.031 & 0 & 71 & 29 \\\\ %% registry: d113-1.7b-isr-b03-s42\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape across reward conditions. PR/ISR$^*$: mean$\\pm$std of per-seed values; H7/H1/N-H: pooled percentages. ISR$^*$ for ISR $\\beta{=}0.1$ omitted (inflated by H7 gaming; premise-count-matched value is $1.06\\times$ random, \\S\\ref{sec:goodhart}). 1.7B ISR $\\beta{=}0.1$: fixed-template H1, zero-variance; 1.7B Random: 100\\% H9 (ex falso, not in H7/H1 columns). $^\\dagger$Single seed (s42), greedy decoding, 500 steps. 3-seed 1000-step data (s42/s43/s44) in Appendix Table~\\ref{tab:exec-only-1000}; all converge to ${\\geq}94\\%$ PR with near-zero genuine. $^\\ddagger$ISR $\\beta{=}0.1$ s43/s44: H8 audit unavailable; N-H may be slightly inflated. $^\\star$5-seed pooled, transient; collapses to ${\\sim}2\\%$ at 1000 steps (\\S\\ref{sec:goodhart-temporal}). Per-seed breakdown in Appendix Table~\\ref{tab:fol-beta01-perseed}.}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): stochastic delayed collapse.}\nAt $\\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\\geq}97\\%$ H7, $0\\%$ genuine within ${\\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.\nThe 5-seed pooled non-hacking rate is ${\\sim}23\\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\\%$ to $55\\%$ genuine.\nThis bifurcation is stochastic: all seeds are indistinguishable in the first ${\\sim}100$ steps ($\\text{ISR}{\\approx}0.05$--$0.07$); divergence occurs at steps 150--200 when H7 tautologies, which receive $\\text{ISR}{\\geq}0.5$ by construction, are sampled during rollouts and reinforced via the positive feedback loop.\nOnce a seed enters the H7 basin, convergence to saturation takes ${\\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46\n\nH7 (a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by the LOO definition; \\S\\ref{sec:taxonomy-method}) is the canonical Goodhart exploit: the model satisfies the structural metric directly rather than producing a genuine derivation.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both ISR and random conditions (Appendix Figure~\\ref{fig:hacking-composition}); the specific mode (H7 vs.\\ H1) within a seed is stochastic under both conditions ($\\text{CV}{>}1$), though ISR modestly increases H7 probability by providing a direct reward pathway.\nRandom yields higher PR ($83{\\pm}15\\%$ vs.\\ $70{\\pm}19\\%$; $n{=}5$ each).\nRandom H7 exhibits extreme seed dependence (per-seed range: $0\\%$--$91.5\\%$; pooled $30\\%$ is dominated by s46 at $91.5\\%$ and s43 at $38.3\\%$).\nBoth conditions produce H7 in 2 of 5 seeds, but the quality differs: ISR-induced H7 is absorbing ($100\\%$ of proved samples in affected seeds: s43${=}61/61$, s44${=}89/89$), while random-induced H7 coexists with other modes ($38$--$92\\%$).\nISR's reward signal converts H7 from a stochastic possibility into an irreversible attractor once sampled.\nThe reward landscape explains H7's attractor strength: H7 tautologies receive expected reward $1{+}0.75\\beta$ versus ${\\sim}1{+}0.26\\beta$ for genuine proofs (premise-count-matched), a gap of ${\\sim}0.49\\beta$ that creates a persistent gradient toward tautological constructions regardless of dose.\n\n\\textbf{The transient genuine window.}\nDuring the transient window, Cochran--Mantel--Haenszel tests stratified by seed confirm ISR produces more genuine proofs than random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, 95\\% CI $[2.21, 5.13]$, $p{<}10^{-9}$; Appendix Table~\\ref{tab:fol-beta01-perseed}).\nPooled Fisher ($\\text{OR}{=}3.48$, uncorrected) is consistent but does not account for within-seed dependence.\nUnder stricter H8+FN-corrected classification (3-seed subset with complete audits), the effect reverses ($\\text{OR}{=}0.61$, n.s.), reflecting both the conservative bias of H8 correction (which reclassifies borderline samples as hacking) and the reduced sample size ($n{=}231$ vs 350). The 5-seed CMH and 3-seed corrected analyses bound the true effect from above and below respectively.\nThe pooled 5-seed non-hacking rate is 23\\% (uncorrected; s42-only H8-corrected estimate: 17\\%).\nThis benefit is temporary: extended training (1000 steps) on seeds~42 and~45 confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine respectively; see below).\nThe same LOO bias that enables genuine improvement (rewarding necessary premises) also creates the Goodhart attractor (rewarding tautological constructions); the genuine window reflects seeds that have not yet sampled the H7 exploit, not seeds that resist it.\nSnapshot evaluation at 500 steps would overestimate ISR's benefit; trajectory analysis is required to distinguish transient from stable improvement. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000\n\n\\textbf{Premise-count confound.}\nThe genuine-rate advantage reflects a selection effect: premise-count-matched comparison yields only $1.06\\times$ ISR difference, confirming indistinguishable per-proof quality once LOO bias toward short outputs is controlled (Appendix~\\ref{app:extended-discussion}).\n\n\\textbf{Trajectory analysis: timing, not destiny.}\\label{sec:goodhart-temporal}\nExtended training (1000 steps; Appendix Figure~\\ref{fig:training-isr-curves}) confirms the genuine window is transient across seeds.\nSeed~42 declines from $17\\%$ to $2\\%$ genuine via H7 saturation ($16.0\\%{\\to}96.7\\%$ H7, PR stable at ${\\sim}96\\%$); seed~45, which achieved the highest 500-step genuine rate ($55\\%$), collapses to $0\\%$ genuine through reward collapse ($\\text{PR}: 42\\%{\\to}2\\%$).\nThe two seeds exhibit distinct failure paths (H7 gaming vs.\\ output collapse) but converge to the same outcome: zero genuine proofs at extended training. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42, plan002-b01-s45-1000\n\n\\textbf{Micro-dose ISR ($\\beta{=}0.05$): deterministic collapse.}\nAll three ISR seeds reach $\\text{PR}{\\geq}99\\%$ but converge to H7a tautology (H7 $87$--$100\\%$, genuine $5.1\\%$), while the random control mostly fails to learn (median $\\text{PR}{=}7\\%$) with zero H7, confirming H7 as specific to ISR's LOO structure.\nBelow a signal-floor, ISR's genuine component is undetectable while its H7 bias remains exploitable (per-seed breakdown in Appendix~\\ref{app:beta005}). %% registry: sweep-isr-b005-s42/s43/s44, sweep-random-b005-s42/s43/s44\n\n\\textbf{Medium-dose ISR ($\\beta{=}0.2$): maximum exploitation.}\nAll three seeds converge to pure H7a tautology ($0\\%$ non-hacking, $n{=}290$; Appendix Table~\\ref{tab:beta02-detail}). %% registry: sweep-isr-b02-s42/s43/s44\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$): three seeds yield three distinct failure modes (reward collapse, H1 shortcutting, pure H7 gaming; per-seed details in Appendix~\\ref{app:beta03}).\nThe random control is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$) with $91\\%$ H1 and ${\\leq}4\\%$ non-hacking; high-dose proxy weighting destabilizes training regardless of signal source. %% registry: plan002-additive-b03-s42/s43/s44\nISR vs.\\ random H7 at $\\beta{=}0.3$: $\\text{OR}{=}13.7$, 95\\% CI $[7.0, 26.8]$ (Appendix~\\ref{app:beta03}).\n\n\\textbf{Non-monotonic dose-response.}\nThe four $\\beta$ levels reveal a non-monotonic pattern: $\\beta\\in\\{0.05, 0.2\\}$ converge deterministically to H7 collapse (${\\geq}94\\%$ H7), $\\beta{=}0.3$ triggers multi-modal instability, and only $\\beta{=}0.1$ sustains a transient genuine window (3 of 5 seeds).\nGoodhart collapse is not a simple function of dose; the balance between genuine and exploit reinforcement depends on a threshold interaction between $\\beta$ and rollout stochasticity.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog (3 seeds, $\\beta{=}0.1$).\nUnder exec-only training, 2/3 seeds show $\\text{ISR}^{*}{\\approx}0$ despite $\\text{PR}{\\geq}0.56$, reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding; ISR flags both failure semantics.\nUnder ISR reward, 3/3 seeds reach $0\\%$ non-hacking through three distinct mechanisms: clean H7 tautology (s42, $\\text{ISR}^{*}{=}1.0$), degenerate uppercase pseudo-Prolog evading text-match classifiers (s43, functional $n_{\\text{necessary}}{=}1$), and query-as-fact gaming (s44, $95/97$ proved at $n_{\\text{necessary}}{=}1$).\nSeed~44 evaded our strict classifier entirely; functional cross-validation was required to expose it.\nWe attribute complete collapse to Prolog's simpler operational semantics providing a broader gaming basin (detailed results in Appendix Table~\\ref{tab:prolog-detailed} and Figure~\\ref{fig:prolog-comparison}).\n\n\\subsection{Cross-Scale Evidence}\n\\label{sec:crossscale}\n\nWe train Qwen3-1.7B under ISR $\\beta\\in\\{0.1,0.3\\}$ and Random $\\beta{=}0.1$ (single seed, 500 steps).\nAll conditions produce $0\\%$ non-hacking, but the exploit modes differ qualitatively from 4B: Random discovers H9 (contradiction injection, $\\text{PR}{=}93\\%$, $100\\%$ \\emph{ex falso}), ISR $\\beta{=}0.1$ collapses to a single fixed template ($\\text{ISR}^{*}{=}0.6$ at zero variance, $100\\%$ H1), and ISR $\\beta{=}0.3$ triggers reward collapse ($\\text{PR}{=}17\\%$) mirroring the 4B pattern.\nH9 never appears at 4B scale; fixed-template mode collapse never appears at 4B; different capacities converge to different Goodhart basins under identical rewards.\nNo safe scale was observed in this single-seed comparison (Table~\\ref{tab:hacking-taxonomy}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{Rnd}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 59 & 7 & 0$^\\sharp$ & \\textbf{100} & 0 \\\\\nH7 duplicate   & 0  & \\textbf{54} & 30 & 0 & 100$^\\sharp$ & 0 & 0 \\\\\nH8 prem-subset & 6  & 5  & 8   & 0 & --- & 0 & 0 \\\\\nH9 ex falso    & --- & --- & --- & --- & --- & 0 & \\textbf{100} \\\\\nTautological   & --- & --- & --- & --- & s42 & --- & --- \\\\\nRepetition     & s43 & --- & --- & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- & --- & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 & --- & --- \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & \\textbf{23}  & 8 & \\textbf{92} & \\textbf{0} & \\textbf{0} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Nine hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random 4B: pooled across 5 seeds; 1.7B columns: Qwen3-1.7B seed~42). H7 includes subtypes H7a (text-match) and H7b (obfuscated tautology; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe nine modes (Table~\\ref{tab:hacking-taxonomy}; definitions in Appendix~\\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 conditions.\nH1, H7, and H8 account for ${>}90\\%$ of hacking; H7 includes obfuscated subtype H7b ($14/350$) that evades text-match classifiers (\\S\\ref{sec:discussion}).\nISR modestly increases H7 convergence probability ($\\text{OR}{=}2.84$, $p{<}5{\\times}10^{-12}$, 5-seed; Appendix Table~\\ref{tab:bootstrap-ci}), but per-seed variance dominates (Random s46: $91.5\\%$ H7; ISR s46: $14.3\\%$).\nAll GRPO conditions show ${\\geq}80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.\nCochran--Mantel--Haenszel tests stratified by seed confirm both effects (H7: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{<}10^{-15}$; genuine: $\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$), indicating that the associations are robust to within-seed clustering.\n",
      "numLines": 177,
      "startLine": 1,
      "totalLines": 177
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
Now I have a clear picture of the current content. Let me plan the Phase 1 edits for conclusion.tex:

1. The opening 3 sentences (lines 4-6) need to be compressed into 1 sentence
2. The "Practical implications" paragraph (lines 10-13) should be deleted, with just the core sentence merged into the main paragraph
3. Line 7 about "surprising elements" (micro-doses, non-monotonic dose-response, stochastic bifurcation) - this is already compressed to 1 sentence, so less to do there

Let me make the edits to conclusion.tex first.


Looking at the actual file structure, I can see the opening sentences that establish the STA framework and its empirical findings need to be consolidated. The "Practical implications" section is redundant and should be stripped down to its essential point, which I'll weave back into the main narrative. The surprising elements are already fairly tight, so I'll focus on tightening the opening and removing that standalone paragraph. I'm working through the conclusion section, consolidating the key findings about STA and ISR's collapse patterns across different conditions, then noting how ISR's empirical behavior—including micro-dose effects and stochastic bifurcation—goes beyond what standard Goodhart theory predicts, and at 500 steps ISR actually improves genuine performance.

However, this reliability breaks down under stricter evaluation criteria and extended training, revealing the fundamental problem: ISR rewards both genuine necessity and tautological constructions through the same LOO bias mechanism. The takeaway is that perturbation-based metrics like ISR work well for post-hoc diagnosis but shouldn't drive training objectives, and future research should develop variants that distinguish between meaningful and spurious optimizations. The empirical findings—micro-dose effects, non-monotonic dose-response curves, and stochastic bifurcation patterns—go beyond what the abstract Goodhart framework predicts.

Since these details are already thoroughly covered in section 4, I can compress this in the Discussion by just referencing that they exceed the theoretical predictions without re-listing each component. The opening sentence about consistent effects across all tested doses already captures the main empirical result, so I don't need to repeat the taxonomy or itemize the surprising elements again.

The plan is to replace lines 4-6 with a single compressed sentence that acknowledges the empirical richness without redundancy, keep lines 7-8 as they are, then fold in the practical implications and wrap up the paragraph concisely. I'm now editing down the paragraph to compress the key findings while removing redundancy—the core insight is that ISR works as a diagnostic tool but fails as an optimizer due to the same bias mechanism, so I should emphasize that tension and the practical recommendation without repeating the statistical details already covered.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "a7bc5dc0-1ff0-4799-9c31-9acabfd06373",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YdvkmLFcL9bWQ4cgdawWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11105,
      "cache_read_input_tokens": 27971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11105
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

_source line 12_

I'll compress conclusion.tex as specified, then compile and check page boundaries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "dee45705-8cfb-4f33-abcd-c4b73723fa15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YdvkmLFcL9bWQ4cgdawWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11105,
      "cache_read_input_tokens": 27971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11105
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01SFP6GFijk9HdtDKPRfRyKN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
  "old_string": "STA exposes structural collapse invisible to prove rate (\\S\\ref{sec:diagnostic}); repurposed as a training signal, ISR produces Goodhart collapse at all four tested doses (\\S\\ref{sec:goodhart}), consistent across logic types, model scales, and training durations.\nIn the \\citet{manheim-goodhart-taxonomy} taxonomy, ISR's collapse is primarily regressional with extremal elements.\nThe empirical details, including collapse at micro-doses, non-monotonic dose-response, and stochastic bifurcation, exceed abstract Goodhart predictions.\nAt 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\n\n\\paragraph{Practical implications.}\n$\\beta$ controls the \\emph{timing} of collapse, not whether it occurs (\\S\\ref{sec:goodhart}); snapshot evaluation overestimates ISR's benefit.\nText-match classifiers have systematic blind spots (\\S\\ref{sec:taxonomy}), and different model capacities converge to different exploits with no safe scale observed (\\S\\ref{sec:crossscale}, \\S\\ref{sec:limitations}).\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.",
  "new_string": "STA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).\nAt 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "b3e30e52-2dac-4c06-93c2-117f5f09aff0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YdvkmLFcL9bWQ4cgdawWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11105,
      "cache_read_input_tokens": 27971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11105
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

_source line 14 · 2026-05-17T15:46:56.610Z_

<details><summary>↩ Tool result · `toolu_01SFP6GFijk9HdtDKPRfRyKN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "2863878b-0aed-40d3-a279-6c998b98c44b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
    "oldString": "STA exposes structural collapse invisible to prove rate (\\S\\ref{sec:diagnostic}); repurposed as a training signal, ISR produces Goodhart collapse at all four tested doses (\\S\\ref{sec:goodhart}), consistent across logic types, model scales, and training durations.\nIn the \\citet{manheim-goodhart-taxonomy} taxonomy, ISR's collapse is primarily regressional with extremal elements.\nThe empirical details, including collapse at micro-doses, non-monotonic dose-response, and stochastic bifurcation, exceed abstract Goodhart predictions.\nAt 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\n\n\\paragraph{Practical implications.}\n$\\beta$ controls the \\emph{timing} of collapse, not whether it occurs (\\S\\ref{sec:goodhart}); snapshot evaluation overestimates ISR's benefit.\nText-match classifiers have systematic blind spots (\\S\\ref{sec:taxonomy}), and different model capacities converge to different exploits with no safe scale observed (\\S\\ref{sec:crossscale}, \\S\\ref{sec:limitations}).\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.",
    "newString": "STA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).\nAt 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.",
    "originalFile": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural collapse invisible to prove rate (\\S\\ref{sec:diagnostic}); repurposed as a training signal, ISR produces Goodhart collapse at all four tested doses (\\S\\ref{sec:goodhart}), consistent across logic types, model scales, and training durations.\nIn the \\citet{manheim-goodhart-taxonomy} taxonomy, ISR's collapse is primarily regressional with extremal elements.\nThe empirical details, including collapse at micro-doses, non-monotonic dose-response, and stochastic bifurcation, exceed abstract Goodhart predictions.\nAt 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\n\n\\paragraph{Practical implications.}\n$\\beta$ controls the \\emph{timing} of collapse, not whether it occurs (\\S\\ref{sec:goodhart}); snapshot evaluation overestimates ISR's benefit.\nText-match classifiers have systematic blind spots (\\S\\ref{sec:taxonomy}), and different model capacities converge to different exploits with no safe scale observed (\\S\\ref{sec:crossscale}, \\S\\ref{sec:limitations}).\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 13,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \\section{Discussion and Conclusion}",
          " \\label{sec:discussion}",
          " ",
          "-STA exposes structural collapse invisible to prove rate (\\S\\ref{sec:diagnostic}); repurposed as a training signal, ISR produces Goodhart collapse at all four tested doses (\\S\\ref{sec:goodhart}), consistent across logic types, model scales, and training durations.",
          "-In the \\citet{manheim-goodhart-taxonomy} taxonomy, ISR's collapse is primarily regressional with extremal elements.",
          "-The empirical details, including collapse at micro-doses, non-monotonic dose-response, and stochastic bifurcation, exceed abstract Goodhart predictions.",
          "+STA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).",
          " At 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.",
          " ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.",
          "-",
          "-\\paragraph{Practical implications.}",
          "-$\\beta$ controls the \\emph{timing} of collapse, not whether it occurs (\\S\\ref{sec:goodhart}); snapshot evaluation overestimates ISR's benefit.",
          "-Text-match classifiers have systematic blind spots (\\S\\ref{sec:taxonomy}), and different model capacities converge to different exploits with no safe scale observed (\\S\\ref{sec:crossscale}, \\S\\ref{sec:limitations}).",
          " ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic."
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

_source line 15_

Now let me compile the PDF and check page boundaries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "57ccda51-99e1-4213-bd4d-32409b687b49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVRFfkXmzxRXnH4c2SkHgR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2748,
      "cache_read_input_tokens": 39076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2748
      },
      "output_tokens": 6,
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

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01KhC4yw8QqiDGKejuSzVhQ7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -10",
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
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "7231097c-ac93-47de-82c0-1b85aca2c623",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVRFfkXmzxRXnH4c2SkHgR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2748,
      "cache_read_input_tokens": 39076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2748
      },
      "output_tokens": 6,
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

_source line 17 · 2026-05-17T15:47:02.669Z_

<details><summary>↩ Tool result · `toolu_01KhC4yw8QqiDGKejuSzVhQ7`</summary>

```text
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
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "a5c071dc-d72d-4688-b369-7dbcf7f4b661",
  "tool_use_result": {
    "stdout": "Latexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01MqPH1v34VYik5WPkxWVcLX`</summary>

```json
{
  "command": "latexmk -pdf -interaction=nonstopmode -g main.tex 2>&1 | tail -10",
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
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "86bb9446-8960-4601-af8b-f4d237b971f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CueLCdLkA2ucr9t8kQeehk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 296,
      "cache_read_input_tokens": 41824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 296
      },
      "output_tokens": 70,
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

_source line 19 · 2026-05-17T15:47:07.863Z_

<details><summary>↩ Tool result · `toolu_01MqPH1v34VYik5WPkxWVcLX`</summary>

```text
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
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "0fd2d19e-66bd-4fbd-9442-db5632e533d8",
  "tool_use_result": {
    "stdout": "Latexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01FCx1erD1LaByt8yTAaU45v`</summary>

```json
{
  "command": "latexmk -pdf -interaction=nonstopmode -f main.tex 2>&1 | tail -10",
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
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "471fbc2e-c21d-40df-907e-d16b02c5c429",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wpVDeudri91RE1M8zwVjF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 254,
      "cache_read_input_tokens": 42120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 254
      },
      "output_tokens": 70,
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

_source line 21 · 2026-05-17T15:47:10.962Z_

<details><summary>↩ Tool result · `toolu_01FCx1erD1LaByt8yTAaU45v`</summary>

```text
Rc files read:
  /etc/LatexMk
Latexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.
Latexmk: Nothing to do for 'main.tex'.
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "1faab286-3374-416f-886f-f3637d6e7cb4",
  "tool_use_result": {
    "stdout": "Rc files read:\n  /etc/LatexMk\nLatexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.\nLatexmk: Nothing to do for 'main.tex'.\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01NEQngAJdjJPu1VT7GVCEdt`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
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
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "9e8632d5-1dce-4782-bf64-85752685b36c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVMA3kvoywmZkTYmD4jeVC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 42374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 295
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

_source line 23 · 2026-05-17T15:47:17.432Z_

<details><summary>↩ Tool result · `toolu_01NEQngAJdjJPu1VT7GVCEdt`</summary>

```text
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/helvetic/uhvb8a.pfb>
Output written on main.pdf (22 pages, 603629 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "f4099f56-c4df-4cc0-95b9-dee222d0d861",
  "tool_use_result": {
    "stdout": "e/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/helvetic/uhvb8a.pfb>\nOutput written on main.pdf (22 pages, 603629 bytes).\nTranscript written on main.log.",
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

_source line 24_

Good, compiled. Now let me check what's on pages 8 and 9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "530c46f4-056d-4f7d-bf6a-26cc76fd721f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ocX4T1jLNtEPEXJ66zkNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 42669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
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

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01AmnSTTotNESGDHPo1VTsTD`</summary>

```json
{
  "command": "pdftotext -f 8 -l 9 main.pdf - 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "5c9ac6da-e661-466f-a1fd-28b0db6b4a03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ocX4T1jLNtEPEXJ66zkNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 42669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
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

_source line 26 · 2026-05-17T15:47:20.784Z_

<details><summary>↩ Tool result · `toolu_01AmnSTTotNESGDHPo1VTsTD`</summary>

```text
Mode

Exec

ISR.1

Rnd.1

SFT

PrologISR

1.7BISR

1.7BRnd

H1 embed
H7 duplicate
H8 prem-subset
H9 ex falso
Tautological
Repetition
Contradiction
Cmplx. vacuous
Query-as-fact

87
0
6
—
—
s43
1k
0
—

18
54
5
—
—
—
—
0
—

59
30
8
—
—
—
—
4
—

7
0
0
—
—
—
—
0
—

0♯
100♯
—
—
s42
—
—
—
s44

100
0
0
0
—
—
—
—
—

0
0
0
100
—
—
—
—
—

Non-hacking

8

23

8

92

0

0

0

612

lizes training regardless of signal source. ISR
vs. random H7 at β=0.3: OR=13.7, 95% CI
[7.0, 26.8] (Appendix E.1).
Non-monotonic dose-response.
The
four β levels reveal a non-monotonic pattern:
β ∈ {0.05, 0.2} converge deterministically to
H7 collapse (≥94% H7), β=0.3 triggers multimodal instability, and only β=0.1 sustains a
transient genuine window (3 of 5 seeds). Goodhart collapse is not a simple function of dose;
the balance between genuine and exploit reinforcement depends on a threshold interaction
between β and rollout stochasticity.

Table 2: Nine hacking modes across conditions
(% of proved samples; exec-only/SFT: seed 42;
ISR/Random 4B: pooled across 5 seeds; 1.7B
columns: Qwen3-1.7B seed 42). H7 includes subtypes H7a (text-match) and H7b (obfuscated tautology; primarily s44). Cells with seed identifiers
indicate the mode dominates that seed. ♯ Prolog
row pools strict+functional (§4.4).

613

4.4

4.6

614

632

We replicate the FOL pipeline with
Prolog/SWI-Prolog (3 seeds, β=0.1). Under
exec-only training, 2/3 seeds show ISR∗ ≈0
despite PR≥0.56,
reflecting redundant
ground-fact repetition rather than FOL-style
conclusion embedding; ISR flags both failure
semantics. Under ISR reward, 3/3 seeds
reach 0% non-hacking through three distinct mechanisms: clean H7 tautology (s42,
ISR∗ =1.0), degenerate uppercase pseudoProlog evading text-match classifiers (s43,
functional nnecessary =1), and query-as-fact
gaming (s44, 95/97 proved at nnecessary =1).
Seed 44 evaded our strict classifier entirely;
functional cross-validation was required to
expose it. We attribute complete collapse
to Prolog’s simpler operational semantics
providing a broader gaming basin (detailed
results in Appendix Table 10 and Figure 4).

633

4.5

634

We train Qwen3-1.7B under ISR β ∈ {0.1, 0.3}
and Random β=0.1 (single seed, 500 steps).
All conditions produce 0% non-hacking, but
the exploit modes differ qualitatively from 4B:
Random discovers H9 (contradiction injection,
PR=93%, 100% ex falso), ISR β=0.1 collapses
to a single fixed template (ISR∗ =0.6 at zero
variance, 100% H1), and ISR β=0.3 triggers
reward collapse (PR=17%) mirroring the 4B
pattern. H9 never appears at 4B scale; fixedtemplate mode collapse never appears at 4B;
different capacities converge to different Goodhart basins under identical rewards. No safe
scale was observed in this single-seed comparison (Table 2).

600
601
602
603
604
605
606
607
608
609
610
611

615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631

635
636
637
638
639
640
641
642
643
644
645
646
647
648

Cross-Logic Diagnostic Transfer

Hacking Taxonomy

The nine modes (Table 2; definitions in Appendix D) span 2 logic types, 2 model scales,
and 6 conditions.
H1, H7, and H8 account for >90% of hacking; H7 includes obfuscated subtype H7b (14/350) that evades
text-match classifiers (§5). ISR modestly increases H7 convergence probability (OR=2.84,
p<5×10−12 , 5-seed; Appendix Table 4), but
per-seed variance dominates (Random s46:
91.5% H7; ISR s46: 14.3%). All GRPO
conditions show ≥80% pooled hacking; only
SFT achieves 92.3% non-hacking. Cochran–
Mantel–Haenszel tests stratified by seed confirm both effects (H7: ORCMH =2.46, p<10−15 ;
genuine: ORCMH =3.37, p<10−9 ), indicating
that the associations are robust to within-seed
clustering.

666

5

667

Discussion and Conclusion

STA exposes structural degeneration invisible
to execution-based evaluation (§4.2), and ISR
exhibits Goodhart collapse at all four tested
doses with consistent effects across logic types
and model scales (§4.3–4.5). At 500 steps,
ISR increases genuine proofs relative to random controls (ORCMH =3.37, p<10−9 ); under
stricter classification (3-seed subset), the effect
reverses (OR=0.61, n.s.), and extended training confirms the window closes. ISR is reliable
as a diagnostic but unreliable as an optimizer:
the same LOO bias that rewards genuine necessity also rewards tautological constructions.
ISR and similar perturbation-based metrics
should serve as post-hoc evaluation tools, not
training signals; future work should explore
variants that penalize tautological construc-

Cross-Scale Evidence

8

649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665

668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684

686

tions and test generalization beyond first-order
logic.

687

6

688

Experiments use a single base model (Qwen34B) and dataset family (FOLIO); generalization remains untested. ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically
vacuous if its individually necessary premises
are collectively inconsistent or semantically ungrounded. A downstream NLI evaluation confirms this gap, finding ISR and task accuracy
uncorrelated (Spearman ρ=−0.049, p=0.187;
Appendix C). Five seeds demonstrate qualitative divergence but limit statistical power
for seed-level permutation tests (p≥0.26; minimum achievable p=0.008 at n=5); CMH tests
stratified by seed confirm the pooled associations remain significant (p<10−9 ). STA requires solvers supporting component-level input manipulation.

685

689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733

cific mode. The zero-variance mode collapse
at 1.7B (100 identical outputs) indicates a
sharper convergence basin at smaller scale.
Replicating across seeds is a natural next step.

Limitations

Data scale. Our experiments use 500 training examples and 100 evaluation examples,
drawn from FOLIO (Han et al., 2024). The
training subset is selected via stratified sampling (seed 42) and held constant across all
conditions. While our findings are consistent
across seeds and logic types, the effect of training data scale on hacking prevalence and mode
distribution remains an open question for future work.

7

Ethics Statement

This work documents failure modes of reward
optimization in neurosymbolic systems. Our
findings (that structural diagnostics can be
gamed when used as training signals) carry
implications for AI safety: they demonstrate
that metrics designed to detect misalignment
may themselves become targets of optimization, a concern relevant to scalable oversight.
We release our taxonomy and diagnostic tools
to help practitioners detect reward hacking
in their own systems. All experiments use
publicly available datasets (FOLIO) and openweight models (Qwen3-4B); no human subjects are involved.

Evaluation as temporal snapshot. All
500-step results represent a temporal snapshot,
not an equilibrium. Trajectory analysis on
seeds 42 and 45 (1000 steps) confirms that the
∼23% genuine window observed at 500 steps
under ISR β=0.1 is transient (s42: 17%→2%;
s45: 55%→0% genuine). Readers should interpret the 500-step non-hacking rates as upper
bounds on long-run structural quality under
continued training.
Seed counts per dose. ISR β=0.05 uses
three seeds (all H7-dominated); random
β=0.05 uses three seeds with high variance
(PR=0%, 7%, 62%); β=0.2 uses three seeds.
The primary β=0.1 comparison uses five seeds
per condition. Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (§4.3) means that fewer-seed
dose points may not capture the full variance
of collapse timing.
Cross-scale replication. Our 1.7B experiments use a single seed. Although different
seeds may converge to different exploitation
modes (as observed at 4B scale, where three
seeds produce three distinct hacking strategies), the qualitative conclusion that hacking dominates with 0% genuine output is robust: at 4B, all seeds hack regardless of spe9

734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762

References

763

Manish Bhattarai, Ismael Boureima, Nishath Rajiv Ranasinghe, Scott Pakin, and Dan O’Malley.
2026.
Rubric-Grounded Reinforcement
Learning:
Structured Judge Rewards for
Generalizable Reasoning.
arXiv preprint
arXiv:2605.08061.

764
765
766
767
768
769

Alexander Bondarenko, Denis Volk, Dmitrii
Volkov, and Jeffrey Ladish. 2025. Demonstrating Specification Gaming in Reasoning Models.
arXiv preprint arXiv:2502.13295.

770
771
772
773

DeepSeek AI. 2024. DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search.
arXiv preprint arXiv:2408.08152.

774
775
776
777

Richard A. DeMillo, Richard J. Lipton, and Frederick G. Sayward. 1978. Hints on Test Data
Selection: Help for the Practicing Programmer.
Computer, 11(4):34–41.

778
779
780
781
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "8c8cb403-e16b-48d1-aabd-67590a00465a",
  "tool_use_result": {
    "stdout": "Mode\n\nExec\n\nISR.1\n\nRnd.1\n\nSFT\n\nPrologISR\n\n1.7BISR\n\n1.7BRnd\n\nH1 embed\nH7 duplicate\nH8 prem-subset\nH9 ex falso\nTautological\nRepetition\nContradiction\nCmplx. vacuous\nQuery-as-fact\n\n87\n0\n6\n—\n—\ns43\n1k\n0\n—\n\n18\n54\n5\n—\n—\n—\n—\n0\n—\n\n59\n30\n8\n—\n—\n—\n—\n4\n—\n\n7\n0\n0\n—\n—\n—\n—\n0\n—\n\n0♯\n100♯\n—\n—\ns42\n—\n—\n—\ns44\n\n100\n0\n0\n0\n—\n—\n—\n—\n—\n\n0\n0\n0\n100\n—\n—\n—\n—\n—\n\nNon-hacking\n\n8\n\n23\n\n8\n\n92\n\n0\n\n0\n\n0\n\n612\n\nlizes training regardless of signal source. ISR\nvs. random H7 at β=0.3: OR=13.7, 95% CI\n[7.0, 26.8] (Appendix E.1).\nNon-monotonic dose-response.\nThe\nfour β levels reveal a non-monotonic pattern:\nβ ∈ {0.05, 0.2} converge deterministically to\nH7 collapse (≥94% H7), β=0.3 triggers multimodal instability, and only β=0.1 sustains a\ntransient genuine window (3 of 5 seeds). Goodhart collapse is not a simple function of dose;\nthe balance between genuine and exploit reinforcement depends on a threshold interaction\nbetween β and rollout stochasticity.\n\nTable 2: Nine hacking modes across conditions\n(% of proved samples; exec-only/SFT: seed 42;\nISR/Random 4B: pooled across 5 seeds; 1.7B\ncolumns: Qwen3-1.7B seed 42). H7 includes subtypes H7a (text-match) and H7b (obfuscated tautology; primarily s44). Cells with seed identifiers\nindicate the mode dominates that seed. ♯ Prolog\nrow pools strict+functional (§4.4).\n\n613\n\n4.4\n\n4.6\n\n614\n\n632\n\nWe replicate the FOL pipeline with\nProlog/SWI-Prolog (3 seeds, β=0.1). Under\nexec-only training, 2/3 seeds show ISR∗ ≈0\ndespite PR≥0.56,\nreflecting redundant\nground-fact repetition rather than FOL-style\nconclusion embedding; ISR flags both failure\nsemantics. Under ISR reward, 3/3 seeds\nreach 0% non-hacking through three distinct mechanisms: clean H7 tautology (s42,\nISR∗ =1.0), degenerate uppercase pseudoProlog evading text-match classifiers (s43,\nfunctional nnecessary =1), and query-as-fact\ngaming (s44, 95/97 proved at nnecessary =1).\nSeed 44 evaded our strict classifier entirely;\nfunctional cross-validation was required to\nexpose it. We attribute complete collapse\nto Prolog’s simpler operational semantics\nproviding a broader gaming basin (detailed\nresults in Appendix Table 10 and Figure 4).\n\n633\n\n4.5\n\n634\n\nWe train Qwen3-1.7B under ISR β ∈ {0.1, 0.3}\nand Random β=0.1 (single seed, 500 steps).\nAll conditions produce 0% non-hacking, but\nthe exploit modes differ qualitatively from 4B:\nRandom discovers H9 (contradiction injection,\nPR=93%, 100% ex falso), ISR β=0.1 collapses\nto a single fixed template (ISR∗ =0.6 at zero\nvariance, 100% H1), and ISR β=0.3 triggers\nreward collapse (PR=17%) mirroring the 4B\npattern. H9 never appears at 4B scale; fixedtemplate mode collapse never appears at 4B;\ndifferent capacities converge to different Goodhart basins under identical rewards. No safe\nscale was observed in this single-seed comparison (Table 2).\n\n600\n601\n602\n603\n604\n605\n606\n607\n608\n609\n610\n611\n\n615\n616\n617\n618\n619\n620\n621\n622\n623\n624\n625\n626\n627\n628\n629\n630\n631\n\n635\n636\n637\n638\n639\n640\n641\n642\n643\n644\n645\n646\n647\n648\n\nCross-Logic Diagnostic Transfer\n\nHacking Taxonomy\n\nThe nine modes (Table 2; definitions in Appendix D) span 2 logic types, 2 model scales,\nand 6 conditions.\nH1, H7, and H8 account for >90% of hacking; H7 includes obfuscated subtype H7b (14/350) that evades\ntext-match classifiers (§5). ISR modestly increases H7 convergence probability (OR=2.84,\np<5×10−12 , 5-seed; Appendix Table 4), but\nper-seed variance dominates (Random s46:\n91.5% H7; ISR s46: 14.3%). All GRPO\nconditions show ≥80% pooled hacking; only\nSFT achieves 92.3% non-hacking. Cochran–\nMantel–Haenszel tests stratified by seed confirm both effects (H7: ORCMH =2.46, p<10−15 ;\ngenuine: ORCMH =3.37, p<10−9 ), indicating\nthat the associations are robust to within-seed\nclustering.\n\n666\n\n5\n\n667\n\nDiscussion and Conclusion\n\nSTA exposes structural degeneration invisible\nto execution-based evaluation (§4.2), and ISR\nexhibits Goodhart collapse at all four tested\ndoses with consistent effects across logic types\nand model scales (§4.3–4.5). At 500 steps,\nISR increases genuine proofs relative to random controls (ORCMH =3.37, p<10−9 ); under\nstricter classification (3-seed subset), the effect\nreverses (OR=0.61, n.s.), and extended training confirms the window closes. ISR is reliable\nas a diagnostic but unreliable as an optimizer:\nthe same LOO bias that rewards genuine necessity also rewards tautological constructions.\nISR and similar perturbation-based metrics\nshould serve as post-hoc evaluation tools, not\ntraining signals; future work should explore\nvariants that penalize tautological construc-\n\nCross-Scale Evidence\n\n8\n\n649\n650\n651\n652\n653\n654\n655\n656\n657\n658\n659\n660\n661\n662\n663\n664\n665\n\n668\n669\n670\n671\n672\n673\n674\n675\n676\n677\n678\n679\n680\n681\n682\n683\n684\n\n\f686\n\ntions and test generalization beyond first-order\nlogic.\n\n687\n\n6\n\n688\n\nExperiments use a single base model (Qwen34B) and dataset family (FOLIO); generalization remains untested. ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically\nvacuous if its individually necessary premises\nare collectively inconsistent or semantically ungrounded. A downstream NLI evaluation confirms this gap, finding ISR and task accuracy\nuncorrelated (Spearman ρ=−0.049, p=0.187;\nAppendix C). Five seeds demonstrate qualitative divergence but limit statistical power\nfor seed-level permutation tests (p≥0.26; minimum achievable p=0.008 at n=5); CMH tests\nstratified by seed confirm the pooled associations remain significant (p<10−9 ). STA requires solvers supporting component-level input manipulation.\n\n685\n\n689\n690\n691\n692\n693\n694\n695\n696\n697\n698\n699\n700\n701\n702\n703\n704\n705\n706\n707\n708\n709\n710\n711\n712\n713\n714\n715\n716\n717\n718\n719\n720\n721\n722\n723\n724\n725\n726\n727\n728\n729\n730\n731\n732\n733\n\ncific mode. The zero-variance mode collapse\nat 1.7B (100 identical outputs) indicates a\nsharper convergence basin at smaller scale.\nReplicating across seeds is a natural next step.\n\nLimitations\n\nData scale. Our experiments use 500 training examples and 100 evaluation examples,\ndrawn from FOLIO (Han et al., 2024). The\ntraining subset is selected via stratified sampling (seed 42) and held constant across all\nconditions. While our findings are consistent\nacross seeds and logic types, the effect of training data scale on hacking prevalence and mode\ndistribution remains an open question for future work.\n\n7\n\nEthics Statement\n\nThis work documents failure modes of reward\noptimization in neurosymbolic systems. Our\nfindings (that structural diagnostics can be\ngamed when used as training signals) carry\nimplications for AI safety: they demonstrate\nthat metrics designed to detect misalignment\nmay themselves become targets of optimization, a concern relevant to scalable oversight.\nWe release our taxonomy and diagnostic tools\nto help practitioners detect reward hacking\nin their own systems. All experiments use\npublicly available datasets (FOLIO) and openweight models (Qwen3-4B); no human subjects are involved.\n\nEvaluation as temporal snapshot. All\n500-step results represent a temporal snapshot,\nnot an equilibrium. Trajectory analysis on\nseeds 42 and 45 (1000 steps) confirms that the\n∼23% genuine window observed at 500 steps\nunder ISR β=0.1 is transient (s42: 17%→2%;\ns45: 55%→0% genuine). Readers should interpret the 500-step non-hacking rates as upper\nbounds on long-run structural quality under\ncontinued training.\nSeed counts per dose. ISR β=0.05 uses\nthree seeds (all H7-dominated); random\nβ=0.05 uses three seeds with high variance\n(PR=0%, 7%, 62%); β=0.2 uses three seeds.\nThe primary β=0.1 comparison uses five seeds\nper condition. Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (§4.3) means that fewer-seed\ndose points may not capture the full variance\nof collapse timing.\nCross-scale replication. Our 1.7B experiments use a single seed. Although different\nseeds may converge to different exploitation\nmodes (as observed at 4B scale, where three\nseeds produce three distinct hacking strategies), the qualitative conclusion that hacking dominates with 0% genuine output is robust: at 4B, all seeds hack regardless of spe9\n\n734\n735\n736\n737\n738\n739\n740\n741\n742\n743\n744\n745\n746\n747\n748\n749\n750\n751\n752\n753\n754\n755\n756\n757\n758\n759\n760\n761\n762\n\nReferences\n\n763\n\nManish Bhattarai, Ismael Boureima, Nishath Rajiv Ranasinghe, Scott Pakin, and Dan O’Malley.\n2026.\nRubric-Grounded Reinforcement\nLearning:\nStructured Judge Rewards for\nGeneralizable Reasoning.\narXiv preprint\narXiv:2605.08061.\n\n764\n765\n766\n767\n768\n769\n\nAlexander Bondarenko, Denis Volk, Dmitrii\nVolkov, and Jeffrey Ladish. 2025. Demonstrating Specification Gaming in Reasoning Models.\narXiv preprint arXiv:2502.13295.\n\n770\n771\n772\n773\n\nDeepSeek AI. 2024. DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search.\narXiv preprint arXiv:2408.08152.\n\n774\n775\n776\n777\n\nRichard A. DeMillo, Richard J. Lipton, and Frederick G. Sayward. 1978. Hints on Test Data\nSelection: Help for the Practicing Programmer.\nComputer, 11(4):34–41.\n\n778\n779\n780\n781",
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

_source line 27_

<details><summary>Logged reasoning block</summary>

````text
Let me analyze the page boundary. The output shows:

Page 8 content ends with lines 684-685:
```
685  tions and test generalization beyond first-order
686  logic.
```

And page 9 starts at line 687:
```
687  6    Limitations
```

Wait, looking more carefully at the pdftotext output, the line numbers 685-686 ("tions and test generalization beyond first-order logic.") are at the very top of page 9, not at the bottom of page 8.

Let me re-read the output more carefully. 

I'm realizing the line numbers in the pdftotext output are the PDF's internal line numbers, not file line numbers. Looking at the text flow, page 8 ends with the discussion about ISR and perturbation-based metrics serving as post-hoc evaluation tools, and page 9 begins with the Limitations section. The page break occurs between the content about tautological constructs and the section header. I see the issue—section 5 is still overflowing by about 2 lines onto page 9 even after compression. I've already cut it down significantly, but I need to trim another 2 rendered lines to keep everything on page 8. Let me look at what I can compress further without losing the key findings about ISR's reliability as a diagnostic tool versus its failure as an optimizer. The overflow is minimal—just a couple lines. I could trim the conclusion text itself rather than moving to Phase 2. Looking at what's there, the last sentence about future work is the most expendable. I could cut the part about exploring variants and testing generalization beyond first-order logic, which would save roughly a line. Alternatively, I could merge the final two sentences to tighten the recommendation about using ISR as a diagnostic tool rather than a training signal. I'm considering Phase 2 options to save more space. The "LOO vs Shapley" section in method.tex could move to the appendix for about 4 lines of savings, and there's a premise-count confound paragraph in experiments.tex that I could compress significantly. Let me focus on that second option since it's quicker—I can condense it from multiple sentences down to just one or two, keeping the key finding about the 1.06× ISR difference and how it controls for the LOO bias. I'm considering whether to move the LOO versus Shapley discussion to the appendix instead. The key insight is that the gaming strategies we document—like single-premise tautologies—would exploit any component-necessity measure, not just LOO specifically, so the comparison doesn't need to stay in the main text. Combined with trimming the conclusion slightly, this should free up the space I need without major restructuring. I'm realizing that trimming the conclusion might be the quickest fix, but I should also check whether section 4 is contributing to the overflow—if I can tighten that slightly, section 5 might fit on the page without cutting content from the conclusion.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "a29e0f3a-e95c-4510-b261-c74af170739c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zMM7ZXEgkj1nR8HeCuVdB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3102,
      "cache_read_input_tokens": 42899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3102
      },
      "output_tokens": 10,
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

§5 still overflows by ~2 lines onto page 9. Let me trim the future-work clause (the user asked to keep only the core sentence) and recompile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "ae943647-ae69-4490-9acb-b8d1a35620b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zMM7ZXEgkj1nR8HeCuVdB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3102,
      "cache_read_input_tokens": 42899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3102
      },
      "output_tokens": 10,
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

<details open><summary>🔧 Tool call — Edit · `toolu_011XnxUwfxhwcKVLCpiGHd5P`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
  "old_string": "ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.",
  "new_string": "ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "92676363-9ba8-436f-a698-4cba5a348d43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zMM7ZXEgkj1nR8HeCuVdB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3102,
      "cache_read_input_tokens": 42899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3102
      },
      "output_tokens": 10,
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

_source line 30 · 2026-05-17T15:48:21.955Z_

<details><summary>↩ Tool result · `toolu_011XnxUwfxhwcKVLCpiGHd5P`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "12442ac8-89ef-4957-8ca5-ed815bad12e7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
    "oldString": "ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.",
    "newString": "ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.",
    "originalFile": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).\nAt 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 4,
        "newStart": 4,
        "newLines": 4,
        "lines": [
          " STA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).",
          " At 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.",
          " ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.",
          "-ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.",
          "+ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals."
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

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01J5nw788bEiN3h4KMt2Jk7x`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
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
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "356211ff-3e02-4e49-b2e3-20e58a57d9b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBLMNMqwTfXT1tzn1skSaC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2681,
      "cache_read_input_tokens": 46001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2681
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

_source line 32 · 2026-05-17T15:48:29.052Z_

<details><summary>↩ Tool result · `toolu_01J5nw788bEiN3h4KMt2Jk7x`</summary>

```text
fonts/type1/urw/helvetic/uhvb8a.pfb>
Output written on main.pdf (22 pages, 603659 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "020e960d-7eeb-48dd-b082-8641e736f913",
  "tool_use_result": {
    "stdout": "fonts/type1/urw/helvetic/uhvb8a.pfb>\nOutput written on main.pdf (22 pages, 603659 bytes).\nTranscript written on main.log.",
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

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_01B5SaWwmBdvxh7Fpd7RFwKu`</summary>

```json
{
  "command": "pdftotext -f 8 -l 9 main.pdf - 2>/dev/null | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "b4a31cf1-8d84-436a-9278-2b138658dbdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mhnn1FPUK5y19aMTjeHXt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 150,
      "cache_read_input_tokens": 48682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 150
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

_source line 34 · 2026-05-17T15:48:31.868Z_

<details><summary>↩ Tool result · `toolu_01B5SaWwmBdvxh7Fpd7RFwKu`</summary>

```text
Mode

Exec

ISR.1

Rnd.1

SFT

PrologISR

1.7BISR

1.7BRnd

H1 embed
H7 duplicate
H8 prem-subset
H9 ex falso
Tautological
Repetition
Contradiction
Cmplx. vacuous
Query-as-fact

87
0
6
—
—
s43
1k
0
—

18
54
5
—
—
—
—
0
—

59
30
8
—
—
—
—
4
—

7
0
0
—
—
—
—
0
—

0♯
100♯
—
—
s42
—
—
—
s44

100
0
0
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "d9c42f3d-d271-4f84-a1aa-4f8d13313b85",
  "tool_use_result": {
    "stdout": "Mode\n\nExec\n\nISR.1\n\nRnd.1\n\nSFT\n\nPrologISR\n\n1.7BISR\n\n1.7BRnd\n\nH1 embed\nH7 duplicate\nH8 prem-subset\nH9 ex falso\nTautological\nRepetition\nContradiction\nCmplx. vacuous\nQuery-as-fact\n\n87\n0\n6\n—\n—\ns43\n1k\n0\n—\n\n18\n54\n5\n—\n—\n—\n—\n0\n—\n\n59\n30\n8\n—\n—\n—\n—\n4\n—\n\n7\n0\n0\n—\n—\n—\n—\n0\n—\n\n0♯\n100♯\n—\n—\ns42\n—\n—\n—\ns44\n\n100\n0\n0\n0",
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

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_013iuNHu2SwiPppEYrtkHTX6`</summary>

```json
{
  "command": "pdftotext -f 8 -l 9 main.pdf - 2>/dev/null | grep -n \"Discussion\\|Limitations\\|logic\\.\\|training signals\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "1b2643ae-fce1-46c5-8a23-18679db358c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWGfaJBRd5FxCpyCHbnw2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 48832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 286
      },
      "output_tokens": 59,
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

_source line 36 · 2026-05-17T15:48:36.027Z_

<details><summary>↩ Tool result · `toolu_013iuNHu2SwiPppEYrtkHTX6`</summary>

```text
254:Discussion and Conclusion
268:training signals.
356:Limitations
386:gamed when used as training signals) carry
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "b7201594-7da6-45ae-b185-8921542913a4",
  "tool_use_result": {
    "stdout": "254:Discussion and Conclusion\n268:training signals.\n356:Limitations\n386:gamed when used as training signals) carry",
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

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01U6QoABEGivBBeRwdupMghU`</summary>

```json
{
  "command": "pdftotext -f 8 -l 9 main.pdf - 2>/dev/null | sed -n '250,280p'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "594221ad-0c03-470a-85ec-b2482d432ed4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mhZDUPxMZXWnYHPfbpnG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 135,
      "cache_read_input_tokens": 49118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 135
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

_source line 38 · 2026-05-17T15:48:38.537Z_

<details><summary>↩ Tool result · `toolu_01U6QoABEGivBBeRwdupMghU`</summary>

```text
5

667

Discussion and Conclusion

STA exposes structural degeneration invisible
to execution-based evaluation (§4.2), and ISR
exhibits Goodhart collapse at all four tested
doses with consistent effects across logic types
and model scales (§4.3–4.5). At 500 steps,
ISR increases genuine proofs relative to random controls (ORCMH =3.37, p<10−9 ); under
stricter classification (3-seed subset), the effect
reverses (OR=0.61, n.s.), and extended training confirms the window closes. ISR is reliable
as a diagnostic but unreliable as an optimizer:
the same LOO bias that rewards genuine necessity also rewards tautological constructions.
ISR and similar perturbation-based metrics
should serve as post-hoc evaluation tools, not
training signals.
8

649
650
651
652
653
654
655
656
657
658
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "4c5f1622-d85c-409a-acde-03ef450baa1a",
  "tool_use_result": {
    "stdout": "5\n\n667\n\nDiscussion and Conclusion\n\nSTA exposes structural degeneration invisible\nto execution-based evaluation (§4.2), and ISR\nexhibits Goodhart collapse at all four tested\ndoses with consistent effects across logic types\nand model scales (§4.3–4.5). At 500 steps,\nISR increases genuine proofs relative to random controls (ORCMH =3.37, p<10−9 ); under\nstricter classification (3-seed subset), the effect\nreverses (OR=0.61, n.s.), and extended training confirms the window closes. ISR is reliable\nas a diagnostic but unreliable as an optimizer:\nthe same LOO bias that rewards genuine necessity also rewards tautological constructions.\nISR and similar perturbation-based metrics\nshould serve as post-hoc evaluation tools, not\ntraining signals.\n8\n\n649\n650\n651\n652\n653\n654\n655\n656\n657\n658",
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

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Now let me check if "training signals." and the section end marker "8" are on page 8 or page 9. pdftotext with -f 8 -l 9 outputs both pages. Looking at the output:

After "training signals." there's a page break indicated by "8" (the page number at the bottom of page 8). Then the next content starts with line numbers.

Wait, actually in a two-column layout, the page numbering might be at the bottom. Let me check more carefully.

The "8" after "training signals." is the page number at the bottom of page 8. Then what follows is page 9 content.


So §5 ends with "training signals." on page 8, and I can verify this by examining what appears next on page 9.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "a1d0a96d-dc96-40e0-9986-757afe1bf2d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvQWXqcqKZdLJpVvVtQosT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 49253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 316
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

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01RAaKfrF2uKXSnZFXUdAXQ2`</summary>

```json
{
  "command": "pdftotext -f 8 -l 9 main.pdf - 2>/dev/null | sed -n '268,290p'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "ba7db10f-9c10-4b8f-8de0-bdc062740c4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvQWXqcqKZdLJpVvVtQosT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 49253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 316
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

_source line 41 · 2026-05-17T15:48:48.555Z_

<details><summary>↩ Tool result · `toolu_01RAaKfrF2uKXSnZFXUdAXQ2`</summary>

```text
training signals.
8

649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665

668
669
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "2e3f9085-1e53-4f46-ac58-7e8fefb70a96",
  "tool_use_result": {
    "stdout": "training signals.\n8\n\n649\n650\n651\n652\n653\n654\n655\n656\n657\n658\n659\n660\n661\n662\n663\n664\n665\n\n668\n669",
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

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01D5F32TwUj4dsuYL2nnXhz1`</summary>

```json
{
  "command": "pdftotext -f 9 -l 9 main.pdf - 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "0135e963-5f15-4573-ae54-20f82f955b26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyPyJH1Acz2Yk132C54BQR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 448,
      "cache_read_input_tokens": 49569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 448
      },
      "output_tokens": 57,
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

_source line 43 · 2026-05-17T15:48:50.954Z_

<details><summary>↩ Tool result · `toolu_01D5F32TwUj4dsuYL2nnXhz1`</summary>

```text
6
685
686
687
688
689
690
691
692
693
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "ffc11858-f050-4de3-a341-faa74de66fa9",
  "tool_use_result": {
    "stdout": "6\n685\n686\n687\n688\n689\n690\n691\n692\n693",
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

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01LztVZrpUFYCSLvuW77Unwt`</summary>

```json
{
  "command": "pdftotext -f 9 -l 9 main.pdf - 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "14b6598e-b117-47bc-b3b8-41dbcf022485",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWghfheKiFTt9UNuKzgh57",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 110,
      "cache_read_input_tokens": 50017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 110
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

_source line 45 · 2026-05-17T15:48:53.651Z_

<details><summary>↩ Tool result · `toolu_01LztVZrpUFYCSLvuW77Unwt`</summary>

```text
6
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "d0818649-1cae-4f36-8f8f-20efb49ee9a1",
  "tool_use_result": {
    "stdout": "6\n685\n686\n687\n688\n689\n690\n691\n692\n693\n694\n695\n696\n697\n698\n699\n700\n701\n702\n703\n704\n705\n706\n707\n708\n709\n710\n711\n712\n713",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01DMpgWf7ehBDD3nh65zhrZN`</summary>

```json
{
  "command": "pdftotext -f 9 -l 9 main.pdf - 2>/dev/null | grep -i \"limit\\|ethic\\|discuss\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "c698242f-d50f-47c6-89c0-e2049696f51b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2T66HRR4awT5ePiPhWCxw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 150,
      "cache_read_input_tokens": 50127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 150
      },
      "output_tokens": 59,
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

_source line 47 · 2026-05-17T15:48:57.230Z_

<details><summary>↩ Tool result · `toolu_01DMpgWf7ehBDD3nh65zhrZN`</summary>

```text
Limitations
Appendix C). Five seeds demonstrate qualitative divergence but limit statistical power
Ethics Statement
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "56dd65d1-0714-4e15-91d3-4efb42b1df15",
  "tool_use_result": {
    "stdout": "Limitations\nAppendix C). Five seeds demonstrate qualitative divergence but limit statistical power\nEthics Statement",
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

_source line 48_

§5 ends with "training signals." on page 8 (page number "8" follows), and page 9 starts with "6 Limitations". Now let me verify no compilation errors and no new em-dashes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "a8ca8da8-1b57-4eaf-b8ad-8f25a125632d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173gvdYtWcFAexY7ZdzC7Ce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 123,
      "cache_read_input_tokens": 50277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 123
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_011Prs4TSYerr9X43oDBbEHh`</summary>

```json
{
  "command": "grep -n \"—\" paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "d9e861e6-cd52-43f7-b5f1-7b070b4029bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173gvdYtWcFAexY7ZdzC7Ce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 123,
      "cache_read_input_tokens": 50277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 123
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

_source line 50 · 2026-05-17T15:49:01.807Z_

<details><summary>↩ Tool result · reported error · `toolu_011Prs4TSYerr9X43oDBbEHh`</summary>

```text
Exit code 2
grep: paper/conclusion.tex: No such file or directory
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "83803330-89a5-4f9d-bb91-1e038e98206f",
  "tool_use_result": "Error: Exit code 2\ngrep: paper/conclusion.tex: No such file or directory"
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_01LmHbURbdSuTDPm19j5jhFW`</summary>

```json
{
  "command": "grep -c \"undefined\" main.log | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "a92a0b0b-ab48-45f9-b328-016583223816",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173gvdYtWcFAexY7ZdzC7Ce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 123,
      "cache_read_input_tokens": 50277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 123
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

_source line 52 · 2026-05-17T15:49:02.175Z_

<details><summary>↩ Tool result · reported error · `toolu_01LmHbURbdSuTDPm19j5jhFW`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(grep -n "—" paper/conclusion.tex) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "e2b9e8f4-b9f1-4e96-9f96-d51397ca2c77",
  "tool_use_result": "Cancelled: parallel tool call Bash(grep -n \"—\" paper/conclusion.tex) errored"
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01YEsxeppR7ieWrSStyPk2cZ`</summary>

```json
{
  "command": "grep -n \"—\" conclusion.tex; echo \"---\"; grep -c \"undefined\" main.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "f763dc36-2faf-4b7c-a7fd-fe1e5d989173",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMKG6B4Eb7z3JKMrNSAZPz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 50400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 274
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

_source line 54 · 2026-05-17T15:49:06.286Z_

<details><summary>↩ Tool result · `toolu_01YEsxeppR7ieWrSStyPk2cZ`</summary>

```text
---
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "3c7a682d-f3b5-4f83-8619-c6c6dc716abb",
  "tool_use_result": {
    "stdout": "---\n0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 55_

No em-dashes, no undefined references. Let me verify the final state of conclusion.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "5c8a6468-ae59-47b4-9eee-d07b5248037d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EPh7NP7bxc4yhezdwY9p7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 89,
      "cache_read_input_tokens": 50674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 89
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

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_01Krtmd4Xdm7tt9Gg8YsrDXk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "af890c07-38ff-482e-93f6-ad385ac38076",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EPh7NP7bxc4yhezdwY9p7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 89,
      "cache_read_input_tokens": 50674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 89
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

_source line 57 · 2026-05-17T15:49:10.793Z_

<details><summary>↩ Tool result · `toolu_01Krtmd4Xdm7tt9Gg8YsrDXk`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\S\ref{sec:goodhart}--\ref{sec:crossscale}).
5	At 500 steps, ISR increases genuine proofs relative to random controls ($\text{OR}_{\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.
6	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
7	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "2f13e3e4-937b-4458-9104-6d3f5b71ab4e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).\nAt 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Assistant

_source line 58_

Now let me commit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "47d2a14d-7308-4e63-b1d4-390448348688",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oGhsbogi9ZRwEZgqoVJyx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 370,
      "cache_read_input_tokens": 50763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 370
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

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_01VBKCASwFV4tVhzdmYvv6Wz`</summary>

```json
{
  "command": "git diff paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "8e94a334-0eb5-4531-986e-d05091cb6cf4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oGhsbogi9ZRwEZgqoVJyx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 370,
      "cache_read_input_tokens": 50763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 370
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

_source line 60 · 2026-05-17T15:49:13.533Z_

<details><summary>↩ Tool result · reported error · `toolu_01VBKCASwFV4tVhzdmYvv6Wz`</summary>

```text
Exit code 128
fatal: ambiguous argument 'paper/conclusion.tex': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git &lt;command> [&lt;revision>...] -- [&lt;file>...]'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "d9d1103e-939d-4ad8-9003-1df24b30dd54",
  "tool_use_result": "Error: Exit code 128\nfatal: ambiguous argument 'paper/conclusion.tex': unknown revision or path not in the working tree.\nUse '--' to separate paths from revisions, like this:\n'git &lt;command> [&lt;revision>...] -- [&lt;file>...]'"
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gw7g3yn7Xz9oYxbs1p335f`</summary>

```json
{
  "command": "git log --oneline -3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "64479981-3f8f-4253-b2ed-8ece5cfbf1d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oGhsbogi9ZRwEZgqoVJyx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 370,
      "cache_read_input_tokens": 50763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 370
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

_source line 62 · 2026-05-17T15:49:13.643Z_

<details><summary>↩ Tool result · reported error · `toolu_01Gw7g3yn7Xz9oYxbs1p335f`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(git diff paper/conclusion.tex) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "0fb3c6bf-c825-4601-88fe-02aa84d5cef0",
  "tool_use_result": "Cancelled: parallel tool call Bash(git diff paper/conclusion.tex) errored"
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01PDyXau9GRJKrWCtFghexfE`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation && git diff -- paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "3bff3f48-192d-4d90-af9a-202ea5dd6450",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HpQsK85xeiRUtGhW6nQea",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 51133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
      },
      "output_tokens": 62,
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

_source line 64 · 2026-05-17T15:49:17.609Z_

<details><summary>↩ Tool result · `toolu_01PDyXau9GRJKrWCtFghexfE`</summary>

```text
diff --git a/paper/conclusion.tex b/paper/conclusion.tex
index a821711..a87f5f9 100644
--- a/paper/conclusion.tex
+++ b/paper/conclusion.tex
@@ -1,13 +1,7 @@
 \section{Discussion and Conclusion}
 \label{sec:discussion}
 
-STA exposes structural collapse invisible to prove rate (\S\ref{sec:diagnostic}); repurposed as a training signal, ISR produces Goodhart collapse at all four tested doses (\S\ref{sec:goodhart}), consistent across logic types, model scales, and training durations.
-In the \citet{manheim-goodhart-taxonomy} taxonomy, ISR's collapse is primarily regressional with extremal elements.
-The empirical details, including collapse at micro-doses, non-monotonic dose-response, and stochastic bifurcation, exceed abstract Goodhart predictions.
+STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\S\ref{sec:goodhart}--\ref{sec:crossscale}).
 At 500 steps, ISR increases genuine proofs relative to random controls ($\text{OR}_{\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.
 ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
-
-\paragraph{Practical implications.}
-$\beta$ controls the \emph{timing} of collapse, not whether it occurs (\S\ref{sec:goodhart}); snapshot evaluation overestimates ISR's benefit.
-Text-match classifiers have systematic blind spots (\S\ref{sec:taxonomy}), and different model capacities converge to different exploits with no safe scale observed (\S\ref{sec:crossscale}, \S\ref{sec:limitations}).
-ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.
+ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "56c4f621-9160-4556-8380-e51f29df810c",
  "tool_use_result": {
    "stdout": "diff --git a/paper/conclusion.tex b/paper/conclusion.tex\nindex a821711..a87f5f9 100644\n--- a/paper/conclusion.tex\n+++ b/paper/conclusion.tex\n@@ -1,13 +1,7 @@\n \\section{Discussion and Conclusion}\n \\label{sec:discussion}\n \n-STA exposes structural collapse invisible to prove rate (\\S\\ref{sec:diagnostic}); repurposed as a training signal, ISR produces Goodhart collapse at all four tested doses (\\S\\ref{sec:goodhart}), consistent across logic types, model scales, and training durations.\n-In the \\citet{manheim-goodhart-taxonomy} taxonomy, ISR's collapse is primarily regressional with extremal elements.\n-The empirical details, including collapse at micro-doses, non-monotonic dose-response, and stochastic bifurcation, exceed abstract Goodhart predictions.\n+STA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).\n At 500 steps, ISR increases genuine proofs relative to random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\n ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\n-\n-\\paragraph{Practical implications.}\n-$\\beta$ controls the \\emph{timing} of collapse, not whether it occurs (\\S\\ref{sec:goodhart}); snapshot evaluation overestimates ISR's benefit.\n-Text-match classifiers have systematic blind spots (\\S\\ref{sec:taxonomy}), and different model capacities converge to different exploits with no safe scale observed (\\S\\ref{sec:crossscale}, \\S\\ref{sec:limitations}).\n-ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals; future work should explore variants that penalize tautological constructions and test generalization beyond first-order logic.\n+ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.",
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

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01WyyAMi5ZxQY1zmXi5pHSZB`</summary>

```json
{
  "command": "git log --oneline -3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "02ff2823-676e-4cc0-8e19-f8cefc953c6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HpQsK85xeiRUtGhW6nQea",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 51133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
      },
      "output_tokens": 62,
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

_source line 66 · 2026-05-17T15:49:17.933Z_

<details><summary>↩ Tool result · `toolu_01WyyAMi5ZxQY1zmXi5pHSZB`</summary>

```text
979aec4 [paper] Round 5 residual: Figure 3 caption fix, §5 compression, 3 new references (Krakovna, Polu, Everitt)
883d9aa [paper] Round 5 Batch 3 partial: intro paragraph cleanup, reference corrections, method/limitations polish
ebf8246 [paper] Round 5 Batch 2: W4-W13 warnings — conclusion compression, SFT mechanism, Goodhart taxonomy, dose-response limits
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "5d20446d-8666-4eb2-8092-0a0ef7c1cada",
  "tool_use_result": {
    "stdout": "979aec4 [paper] Round 5 residual: Figure 3 caption fix, §5 compression, 3 new references (Krakovna, Polu, Everitt)\n883d9aa [paper] Round 5 Batch 3 partial: intro paragraph cleanup, reference corrections, method/limitations polish\nebf8246 [paper] Round 5 Batch 2: W4-W13 warnings — conclusion compression, SFT mechanism, Goodhart taxonomy, dose-response limits",
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

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_01AjiwiSjgwXF9ST5fHKRuzp`</summary>

```json
{
  "command": "git add paper/conclusion.tex && git commit -m \"$(cat <<'EOF'\n[paper] Compress §5 to fit within 8-page limit\n\nRemove Practical Implications paragraph and compress opening 3 sentences\nto 1, bringing §5 (Discussion and Conclusion) fully within page 8.\n§6 Limitations now starts on page 9 as required by ACL format.\n\nCo-Authored-By: Claude Opus 4.6 &lt;noreply@anthropic.com>\nEOF\n)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "9ad5f4a7-a51f-49e7-8769-7c281a754853",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsNkhPS2Ud8wRahFQkSTkR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 51495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 918
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

_source line 68 · 2026-05-17T15:49:24.130Z_

<details><summary>↩ Tool result · `toolu_01AjiwiSjgwXF9ST5fHKRuzp`</summary>

```text
[master a9dfa86] [paper] Compress §5 to fit within 8-page limit
 Committer: Ubuntu &lt;ubuntu@ip-172-31-5-208.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 2 insertions(+), 8 deletions(-)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "febea7d5-39f8-42ed-8e75-a179da025138",
  "tool_use_result": {
    "stdout": "[master a9dfa86] [paper] Compress §5 to fit within 8-page limit\n Committer: Ubuntu &lt;ubuntu@ip-172-31-5-208.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 1 file changed, 2 insertions(+), 8 deletions(-)",
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

_source line 69_

§5 now ends on page 8 with "training signals.", §6 Limitations starts on page 9. Only conclusion.tex was changed: 3 opening sentences compressed to 1, "Practical implications" paragraph removed with core sentence merged to main paragraph end. No new em-dashes, no undefined references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "uuid": "615ff352-24ae-42fa-a234-606c2d252f72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nn6CUMaoyjS8VVfJA4deuo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 52413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 347
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

_source line 70_

§5 now ends on page 8 with "training signals.", §6 Limitations starts on page 9. Only conclusion.tex was changed: 3 opening sentences compressed to 1, "Practical implications" paragraph removed with core sentence merged to main paragraph end. No new em-dashes, no undefined references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 208651,
  "duration_api_ms": 203397,
  "num_turns": 28,
  "stop_reason": "end_turn",
  "session_id": "afbf2053-1cb6-46eb-af2a-7b4e2432f772",
  "total_cost_usd": 0.97879875,
  "usage": {
    "input_tokens": 25,
    "cache_creation_input_tokens": 40919,
    "cache_read_input_tokens": 1039528,
    "output_tokens": 7978,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40919,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 73,
        "cache_read_input_tokens": 52413,
        "cache_creation_input_tokens": 347,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 347
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3611,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003716,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 25,
      "outputTokens": 7978,
      "cacheReadInputTokens": 1039528,
      "cacheCreationInputTokens": 40919,
      "webSearchRequests": 0,
      "costUSD": 0.9750827500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "39738481-ec38-4ddf-b83a-09b405fea99d"
}
```

</details>

---
