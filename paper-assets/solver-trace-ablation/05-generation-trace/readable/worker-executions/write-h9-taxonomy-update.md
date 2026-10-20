# write h9 taxonomy update

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_write_h9-taxonomy-update_20260516T184906.log`
- **Structured JSON:** [`63f9c5fdbd66702938c3.json`](../../sessions/63/63f9c5fdbd66702938c3.json)

## Before a recorded user message

26 recorded events

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
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
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
  "uuid": "ed58306a-cefb-4980-9df5-7e2ebdc28914",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778958000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a9d6f7f9-82ee-4799-ada6-c92b0454a73d",
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1"
}
```

---

### Assistant

_source line 4_

I'll start by reading the three files to understand the current structure and find the right insertion points.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "f17834c4-5cd4-4656-a1f7-35d70778fc4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1wD3pugkXHh7Cuvui6Jve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14596,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14596
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_012EmRbWANEWXZArzm8Qi4YF`</summary>

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
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "3de6adb3-5905-41dc-bce3-3d152d953e5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1wD3pugkXHh7Cuvui6Jve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14596,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14596
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

_source line 6 · 2026-05-16T18:49:17.213Z_

<details><summary>↩ Tool result · `toolu_012EmRbWANEWXZArzm8Qi4YF`</summary>

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
56	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\ $8.46$ for random), inflating ISR; premise-count-matched comparison eliminates the difference ($1.06\times$).
57	This is an informative negative result: ISR functions as a diagnostic but fails as a training signal because optimization exploits the metric's structural bias rather than improving reasoning quality.
58	We recommend that any LOO-based metric on variable-length outputs report component-count-matched comparisons alongside raw values.
59	
60	\paragraph{LOO vs.\ Shapley values.}
61	Shapley values~\citep{lundberg-shap-game} provide a theoretically grounded alternative to LOO for measuring component contribution, accounting for interaction effects between premises.
62	We chose LOO for three reasons: (1) $O(n)$ rather than $O(2^n)$ cost, critical for repeated evaluation during RL training; (2) it directly answers the diagnostic question ``is this component necessary for the proof?'' rather than measuring marginal contribution; and (3) the Goodhart effects we document would likely transfer to Shapley-based metrics, since the gaming strategies (e.g., single-premise tautology achieving ISR${\geq}0.5$) exploit the numerics of \emph{any} component-necessity measure, not LOO specifically.
63	
64	\paragraph{$O(1)$ ablation variant.}
65	The $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.
66	However, the $O(1)$ variant includes a tautology check (conclusion provable under empty premises $\to$ ISR${=}0$) absent from exec-only, introducing a training-time confound that depresses prove rate ($63\%$ vs.\ $93\%$ exec-only); the two conditions are therefore non-equivalent in training dynamics despite producing comparable ISR signals (Appendix~\ref{app:o1-ablation}).
67	
68	\subsection{Reward Conditions and Hacking Modes}
69	\label{sec:rewards}
70	\label{sec:taxonomy-method}
71	
72	We study six primary conditions: exec-only ($r_{\text{exec}}$), ISR reward ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations), with supplementary ISR dose points at $\beta\in\{0.05,0.2\}$ for dose-response analysis.
73	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
74	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
75	Each RL condition uses seeds $\{42,43,44\}$ and identical training data.
76	An earlier convex formulation ($\alpha r_{\text{exec}} + \beta r_{\text{exec}}\text{ISR}$, $\alpha{+}\beta{=}1$) was discarded because $\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\ref{app:setup}).
77	
78	\paragraph{Hacking taxonomy.}
79	Across conditions, seeds, and logic types we identify nine structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}).
80	The numbering (H1, H7, H8) reflects our iterative classification process: intermediate modes H2--H6 were merged into H1 or reclassified as subtypes during analysis (e.g., H2--H5 were variants of conclusion embedding differing only in premise count or formatting, subsumed by H1; H6 was reclassified as a subtype of H7).
81	The retained modes are:
82	\textbf{H1} (conclusion embedded among multiple premises),
83	\textbf{H7} (single-premise conclusion duplication, subtypes H7a standard and H7b obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\text{ISR}\geq 0.5$),
84	\textbf{H8} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\ref{app:h8}),
85	\textbf{tautological collapse} (minimal two-component $P{\to}P$ without explicit ISR inflation),
86	\textbf{repetition collapse} (identical clauses repeated to inflate component count),
87	\textbf{complexity-without-utility} (elaborate but vacuous premises),
88	\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \emph{ex falso}),
89	\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers), and
90	\textbf{H9: ex falso quodlibet} (contradiction injection: the model generates logically contradictory premises from which any conclusion follows; observed only at 1.7B scale, \S\ref{sec:crossscale}).
91	Modes are identified by a two-stage procedure: strict normalized text matching (H1/H7) plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution (catches modes evading text matching).
92	We report both classifications in \S\ref{sec:experiments}.
93	The taxonomy is independently applicable: text matching (H1/H7) requires only string comparison between conclusion and premises, needing no solver or ISR computation; the functional stage uses per-sample $n_{\text{necessary}}$ from any LOO-based analysis, not specifically STA.
94	Practitioners can apply the taxonomy to any neurosymbolic system where premise--conclusion structure is inspectable.
95	
96	In interpreting ISR results, we distinguish two failure semantics that share a numerical signature: an exec-only \emph{low} ISR signals \emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (H7-style constructions).
97	A bare ISR difference therefore does not translate directly into a reasoning-ability difference; the mode breakdown is what licenses such interpretation.
98	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "59489934-84f3-40ce-896d-cda478e1afb1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\n\\subsection{Task and GRPO Training}\n\\label{sec:task}\n\nGiven premises $P_1,\\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\\{c_1,\\ldots,c_n\\}$ verified by an external solver $S\\in\\{\\text{Prover9, SWI-Prolog}\\}$ (Figure~\\ref{fig:sta-overview}a).\nWe train with Group Relative Policy Optimization (GRPO)~\\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\\text{exec}}(x) = \\mathbf{1}[S(F_x){=}\\textit{proved}]$.\nThis optimizes prove rate but provides no signal about \\emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.\nAll experiments draw from FOLIO~\\citep{folio}; the held-out evaluation file retains a legacy \\texttt{proofwriter\\_fol\\_*.jsonl} filename (from ProofWriter~\\citep{proofwriter}) but contains only FOLIO-derived examples.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\nSTA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\\ref{fig:sta-overview}b).\nGiven a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\\setminus\\{c_i\\}$ and re-runs the solver (Algorithm~\\ref{alg:sta}).\nA component is \\emph{necessary} if its removal causes proof failure.\nWhat constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.\nLOO ablation itself is standard in mutation testing and sensitivity analysis~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Proved formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE $\\text{ISR}(x) \\in [0, 1]$\n\\STATE $\\textit{necessary} \\gets 0$\n\\FOR{$i = 1$ to $n$}\n    \\IF{$S(x \\setminus \\{c_i\\}) = \\textit{failed}$}\n        \\STATE $\\textit{necessary} \\gets \\textit{necessary} + 1$\n    \\ENDIF\n\\ENDFOR\n\\RETURN $\\textit{necessary} \\,/\\, n$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Intensional Structural Reward.}\nISR is the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n}\\sum_{i=1}^{n}\\mathbf{1}\\bigl[S(x\\setminus\\{c_i\\})=\\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.\nWe report \\emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.\n\n\\paragraph{Limitations of ISR and the premise-count confound.}\nISR measures syntactic component necessity, not semantic faithfulness: a formalization can achieve $\\text{ISR}{=}1$ while remaining semantically unrelated to the NL input (e.g., a single premise identical to the conclusion).\nCritically, ISR is sensitive to component count $n$: when $n{=}2$, $\\text{ISR}\\geq 0.5$ regardless of proof quality; more generally, fewer components mechanically inflate ISR because each is more likely to be individually necessary.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\\ $8.46$ for random), inflating ISR; premise-count-matched comparison eliminates the difference ($1.06\\times$).\nThis is an informative negative result: ISR functions as a diagnostic but fails as a training signal because optimization exploits the metric's structural bias rather than improving reasoning quality.\nWe recommend that any LOO-based metric on variable-length outputs report component-count-matched comparisons alongside raw values.\n\n\\paragraph{LOO vs.\\ Shapley values.}\nShapley values~\\citep{lundberg-shap-game} provide a theoretically grounded alternative to LOO for measuring component contribution, accounting for interaction effects between premises.\nWe chose LOO for three reasons: (1) $O(n)$ rather than $O(2^n)$ cost, critical for repeated evaluation during RL training; (2) it directly answers the diagnostic question ``is this component necessary for the proof?'' rather than measuring marginal contribution; and (3) the Goodhart effects we document would likely transfer to Shapley-based metrics, since the gaming strategies (e.g., single-premise tautology achieving ISR${\\geq}0.5$) exploit the numerics of \\emph{any} component-necessity measure, not LOO specifically.\n\n\\paragraph{$O(1)$ ablation variant.}\nThe $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.\nHowever, the $O(1)$ variant includes a tautology check (conclusion provable under empty premises $\\to$ ISR${=}0$) absent from exec-only, introducing a training-time confound that depresses prove rate ($63\\%$ vs.\\ $93\\%$ exec-only); the two conditions are therefore non-equivalent in training dynamics despite producing comparable ISR signals (Appendix~\\ref{app:o1-ablation}).\n\n\\subsection{Reward Conditions and Hacking Modes}\n\\label{sec:rewards}\n\\label{sec:taxonomy-method}\n\nWe study six primary conditions: exec-only ($r_{\\text{exec}}$), ISR reward ($r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ at $\\beta\\in\\{0.1,0.3\\}$), matched random controls ($r_{\\text{exec}}\\cdot(1{+}\\beta u)$, $u\\sim\\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations), with supplementary ISR dose points at $\\beta\\in\\{0.05,0.2\\}$ for dose-response analysis.\nMultiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.\nRandom isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.\nEach RL condition uses seeds $\\{42,43,44\\}$ and identical training data.\nAn earlier convex formulation ($\\alpha r_{\\text{exec}} + \\beta r_{\\text{exec}}\\text{ISR}$, $\\alpha{+}\\beta{=}1$) was discarded because $\\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\\ref{app:setup}).\n\n\\paragraph{Hacking taxonomy.}\nAcross conditions, seeds, and logic types we identify nine structural-degeneration modes (full definitions in Appendix~\\ref{app:hacking-modes}).\nThe numbering (H1, H7, H8) reflects our iterative classification process: intermediate modes H2--H6 were merged into H1 or reclassified as subtypes during analysis (e.g., H2--H5 were variants of conclusion embedding differing only in premise count or formatting, subsumed by H1; H6 was reclassified as a subtype of H7).\nThe retained modes are:\n\\textbf{H1} (conclusion embedded among multiple premises),\n\\textbf{H7} (single-premise conclusion duplication, subtypes H7a standard and H7b obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\\text{ISR}\\geq 0.5$),\n\\textbf{H8} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\\ref{app:h8}),\n\\textbf{tautological collapse} (minimal two-component $P{\\to}P$ without explicit ISR inflation),\n\\textbf{repetition collapse} (identical clauses repeated to inflate component count),\n\\textbf{complexity-without-utility} (elaborate but vacuous premises),\n\\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \\emph{ex falso}),\n\\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers), and\n\\textbf{H9: ex falso quodlibet} (contradiction injection: the model generates logically contradictory premises from which any conclusion follows; observed only at 1.7B scale, \\S\\ref{sec:crossscale}).\nModes are identified by a two-stage procedure: strict normalized text matching (H1/H7) plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution (catches modes evading text matching).\nWe report both classifications in \\S\\ref{sec:experiments}.\nThe taxonomy is independently applicable: text matching (H1/H7) requires only string comparison between conclusion and premises, needing no solver or ISR computation; the functional stage uses per-sample $n_{\\text{necessary}}$ from any LOO-based analysis, not specifically STA.\nPractitioners can apply the taxonomy to any neurosymbolic system where premise--conclusion structure is inspectable.\n\nIn interpreting ISR results, we distinguish two failure semantics that share a numerical signature: an exec-only \\emph{low} ISR signals \\emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming} (H7-style constructions).\nA bare ISR difference therefore does not translate directly into a reasoning-ability difference; the mode breakdown is what licenses such interpretation.\n",
      "numLines": 98,
      "startLine": 1,
      "totalLines": 98
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01V4vQ4dzuzo8To8aQB9YeJ5`</summary>

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
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "a0ce003f-370a-4f7c-97b1-52d6cf034c30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1wD3pugkXHh7Cuvui6Jve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14596,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14596
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

_source line 8 · 2026-05-16T18:49:17.713Z_

<details><summary>↩ Tool result · `toolu_01V4vQ4dzuzo8To8aQB9YeJ5`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals a novel gaming mode (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the nine cataloged patterns, a necessary but not sufficient condition for semantic correctness.
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
31	The three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\ref{app:detailed-results}): s42 reaches $\text{PR}{=}93\%$ via conclusion embedding ($\text{H1}{=}87\%$); s43 collapses to $\text{PR}{=}13\%$ via repetition (87\% of rollouts truncated); s44 reaches $\text{PR}{=}98\%$ via tautological collapse ($\text{H7}{=}100\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
32	The cross-seed PR variance ($\sigma{=}47$\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).
33	By 1000 steps, all three converge to high PR ($0.95{\pm}0.05$) but $0\%$ non-hacking (15 samples escape text-match classifiers but are functionally degenerate; see Appendix~\ref{app:h8} and Table~\ref{tab:fol-detailed}), each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8). %% registry: plan016-extended-1000-s42, plan001-exec-only-s43-1000-r2, plan001-exec-only-s44-1000-r2
34	
35	\textbf{SFT baseline.}
36	SFT on gold formalizations reaches $\text{PR}{=}13.0\%$ (3-seed pooled, 1000 steps) with $\text{H7}{=}0$, $\text{H1}{=}7.7\%$, $92.3\%$ non-hacking ($n{=}39$; $\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$; per-seed range ${\sim}$91--93\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
37	The near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.
38	A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%; $\text{OR}{=}5.5$, 95\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.
39	
40	\subsection{ISR as Reward: Goodhart Effects}
41	\label{sec:goodhart}
42	
43	We now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with a matched random control, $r = r_{\text{exec}}\cdot(1 + \beta\,u)$, $u\sim\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.
44	The headline finding: ISR-as-reward produces an empirical instance of Goodhart's Law~\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.
45	We test four dose levels ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$); gaming dominates at every $\beta$, with qualitatively different failure modes across the dose-response curve.
46	
47	\begin{table}[t]
48	\centering
49	\small
50	\resizebox{\columnwidth}{!}{%
51	\begin{tabular}{lcccccc}
52	\toprule
53	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} \\
54	\midrule
55	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
56	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
57	\midrule
58	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)
59	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
60	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
61	\midrule
62	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
63	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
64	\bottomrule
65	\end{tabular}}
66	\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random H7 driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}.}
67	\label{tab:goodhart-landscape}
68	\end{table}
69	
70	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-amplified gaming.}
71	H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\sim}5\times$: $70.6\%$ ($163/231$) under ISR vs.\ $13.7\%$ ($36/262$) under random (Fisher $p{=}1.3{\times}10^{-39}$, $\text{OR}{=}15.05$, 95\% CI $[9.6, 23.6]$). %% registry: plan002 vs plan018 all seeds; D095 FINAL
72	Random H7 is highly seed-dependent: $38.3\%$ in seed~43 vs.\ $0\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\%$, Table~\ref{tab:fol-detailed}).
73	H7---a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction (\S\ref{sec:taxonomy-method})---is the canonical Goodhart exploit: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.
74	Total conclusion embedding ($\text{H1}+\text{H7}$) is GRPO-universal at $68$--$100\%$ across both conditions (pooled: ISR $89\%$, random $85\%$).
75	The composition differs: H1 alone accounts for $71\%$ under random vs.\ $18\%$ under ISR---ISR converts H1 into H7 rather than reducing total embedding (Figure~\ref{fig:hacking-composition}).
76	Random also yields higher and more stable PR ($87{\pm}8\%$ vs.\ $77{\pm}14\%$; Cohen's $d{=}0.88$, $n{=}3$ per group).
77	
78	\textbf{Premise-count confound.}
79	The one ISR seed not dominated by H7 (s42) has raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ its random control ($0.131$), suggesting genuine improvement.
80	This appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\text{ISR}\geq 0.5$ by definition.
81	Restricting to non-hacking samples with $\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\text{ISR}^{*}{=}0.258$ for ISR vs.\ $0.243$ for random: a $1.06\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis
82	After reclassifying premise-subset gaming (H8; Appendix~\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\ref{app:hacking-modes}), ISR $\beta{=}0.1$ non-hacking rate ($6.06\%$, $14/231$) is numerically lower than random ($9.5\%$, $25/262$), but the difference is not statistically significant (Fisher $p{=}0.182$, $\text{OR}{=}0.61$, 95\% CI $[0.31, 1.21]$, n.s.; Wilson 95\% CI: ISR $[3.6\%, 9.9\%]$, Random $[6.5\%, 13.7\%]$; Appendix Table~\ref{tab:bootstrap-ci}). %% D095 FINAL Fisher test
83	The key asymmetry is not in non-hacking rates but in gaming \emph{composition}: ISR converts stochastic H7 into near-deterministic convergence ($2/3$ seeds ${\geq}97\%$), while random H7 remains seed-dependent and H1-dominated.
84	The raw $3.2\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
89	\caption{Training ISR trajectories across reward conditions. ISR $\beta{=}0.1$ seeds rise rapidly toward $\text{ISR}{\approx}1$ (Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\text{ISR}{\geq}0.5$ by construction), not genuine structural quality; random $\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}
90	\label{fig:training-isr-curves}
91	\end{figure}
92	
93	\textbf{Temporal collapse under ISR $\beta{=}0.1$.}
94	Figure~\ref{fig:training-isr-curves} traces training ISR across conditions.
95	Extended training (1000 steps) reveals that ISR $\beta{=}0.1$'s non-hacking rate at 500 steps ($17.3\%$, seed~42) is transient: by step 1000, H7 gaming escalates from $16.0\%$ to $96.7\%$ while the non-hacking rate collapses to $2.2\%$ ($n_{\text{comp}}$: $5.58{\to}2.89$).
96	The optimization converges to a fixed point where $\text{ISR}^{*}{=}0.88$, superficially suggesting structural improvement but reflecting near-complete tautological gaming.
97	This mirrors the exec-only 1000-step trajectory (\S\ref{sec:diagnostic}): both converge to ${\sim}0\%$ non-hacking proofs despite opposite ISR values ($0.88$ vs.\ $0.003$), demonstrating that ISR is gamed upward under ISR-as-reward and downward under exec-only---two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
98	
99	\textbf{Micro-dose ISR ($\beta{=}0.05$): gaming at minimal signal.}
100	Even at $\beta{=}0.05$, the lowest dose tested (seed~42), 100\% of proved samples ($n{=}55$) are H7a tautologies with 0\% non-hacking, showing that gaming emerges at the minimum ISR signal strength. %% registry: sweep-isr-b005-s42
101	
102	\textbf{Medium-dose ISR ($\beta{=}0.2$): maximum exploitation.}
103	At $\beta{=}0.2$, all three seeds converge to H7a tautology with $0\%$ non-hacking (pooled $n{=}290$), the maximum exploitation point in the dose-response curve.
104	Seeds achieve $\text{ISR}^{*}{=}0.55$--$0.96$ through single-premise-equals-conclusion constructions. %% registry: sweep-isr-b02-s42/s43/s44
105	
106	\textbf{High-dose ISR ($\beta{=}0.3$): multi-modal Goodhart.}
107	At $\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability ($\text{PR}{=}66{\pm}42\%$, spanning 18--95\%); each seed converges to a distinct pathway (Appendix~\ref{app:detailed-results}). %% registry: plan002-additive-b03-s42/s43/s44
108	Seed~42: \emph{reward collapse} ($\text{PR}{=}18\%$), following the pattern described by~\citet{gao-reward-overoptimization}.
109	Seed~43: \emph{H1 shortcutting} ($\text{PR}{=}86\%$, $\text{H1}{=}69\%$, only $23\%$ non-hacking).
110	Seed~44: \emph{pure H7 gaming} ($\text{PR}{=}95\%$, $\text{H7}{=}100\%$, $\text{ISR}^{*}{=}0.742$, $0\%$ non-hacking)---simultaneously gaming \emph{both} execution and structural metrics through the same construction.
111	The random control at $\beta{=}0.3$ is equally unstable ($\text{PR}{=}54{\pm}35\%$, spanning 23--92\%) with near-universal H1 hacking ($91\%$, pooled) and ${\leq}4\%$ non-hacking per seed; high-dose proxy weighting destabilizes training regardless of signal source; ISR produces diverse failure modes (reward collapse, H1 shortcutting, pure H7 gaming) while random converges to H1-dominated hacking with sporadic H7 ($7\%$ pooled, $0$--$7$ H7a per seed; ISR vs.\ random H7 $\text{OR}{=}13.7$, 95\% CI $[7.0, 26.8]$) (Appendix~\ref{app:beta03}).
112	
113	\subsection{Cross-Logic Diagnostic Transfer}
114	\label{sec:crosslogic}
115	
116	\begin{figure}[t]
117	\centering
118	\includegraphics[width=0.95\columnwidth]{figures/fig4_prolog_comparison.pdf}
119	\caption{Cross-logic results. \textbf{Left}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
120	\label{fig:prolog-comparison}
121	\end{figure}
122	
123	We replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce the Goodhart effects observed in FOL?
124	Detailed per-seed numbers are in Appendix Table~\ref{tab:prolog-detailed}.
125	
126	\textbf{Prolog exec-only: ISR catches redundancy across logics.}
127	Two of three seeds (s42, s43) show $\text{ISR}^{*}{\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3
128	Inspection reveals \emph{redundant coding}: ground facts repeated multiple times (e.g., \texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.
129	This is a different failure semantics from FOL exec-only (conclusion embedding), but $\text{ISR}^{*}$ flags both.
130	We are careful to distinguish: exec-only \emph{low} ISR signals \emph{redundancy}; ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (\S\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.
131	
132	\textbf{Prolog ISR-as-reward: consistent gaming across all seeds.}
133	The Prolog result is qualitatively consistent with FOL: 3/3 seeds reach $0\%$ non-hacking via three distinct mechanisms (Figure~\ref{fig:prolog-comparison}).
134	Seed~42: clean H7 tautologies ($\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42
135	Seed~43: \emph{degenerate uppercase pseudo-Prolog} (e.g., \texttt{MARY\_IS\_AN\_AVA\-DEOTE.}); strict text-match returns $\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\text{necessary}}{=}1$ (functionally H7). %% registry: plan006-prolog-sta-s43
136	Seed~44: \emph{query-as-fact gaming}---the model transforms the NL question into a snake-case atom asserted as both fact and query (e.g., \texttt{is\_the\_dog\_furry.}), with $95/97$ proved samples at $n_{\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44
137	Seed~44 evaded our initial strict classifier (reported $100\%$ non-hacking); functional cross-validation exposed it---a methodological lesson that text-match classifiers have blind spots and STA's necessity profile is the cross-check.
138	We attribute Prolog's complete collapse to its simpler operational semantics: a broader gaming basin makes the non-hacking residual disappear.
139	This is a qualitative observation from a single configuration (Prolog + ISR $\beta{=}0.1$, 3 seeds); generalization to other logic types requires further experimentation.
140	
141	\subsection{Cross-Scale Evidence}
142	\label{sec:crossscale}
143	
144	To test whether ISR gaming generalizes beyond Qwen3-4B, we train Qwen3-1.7B under ISR $\beta{=}0.1$ ($K{=}4$, seed~42, 500 steps).
145	The smaller model achieves $\text{PR}{=}93\%$ with $\text{ISR}^{*}{=}0.2625$---but 100\% of proved samples ($n{=}93$) exhibit a single novel hacking mode absent from all 4B experiments: \textbf{H9 (ex falso quodlibet)}, where the model injects logically contradictory premises (e.g., $P(x)$ and $\neg P(x)$), enabling any conclusion to follow from the contradiction. %% registry: w2-qwen3-1.7b-isr-pilot
146	Mode collapse onset occurs at step~463.
147	ISR registers $>0$ because each contradictory premise is individually ``necessary'' under LOO (removing either side of the contradiction breaks the \emph{ex falso} derivation), yet the formalization is semantically vacuous.
148	
149	A matched 1.7B exec-only run reaches only $\text{PR}{=}3\%$ (seed~42, 500 steps), indicating that ISR bonus is the factor enabling high PR at this scale---but the learned strategy is entirely gaming. %% registry: w2-qwen3-1.7b-exec-pilot
150	The 4B model never discovers H9 under any condition tested; smaller capacity evidently selects a different basin in the Goodhart landscape.
151	This single-seed result demonstrates that ISR gaming is not scale-specific---the failure mode transfers across model sizes, with the smaller model finding a qualitatively novel exploit.
152	
153	\subsection{Hacking Taxonomy}
154	\label{sec:taxonomy}
155	
156	\begin{figure}[t]
157	\centering
158	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
159	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}
160	\label{fig:hacking-composition}
161	\end{figure}
162	
163	\begin{table}[t]
164	\centering
165	\small
166	\resizebox{\columnwidth}{!}{%
167	\begin{tabular}{lcccccc}
168	\toprule
169	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} & \textbf{1.7B$_{\text{ISR}}$} \\
170	\midrule
171	H1 embed       & 87 & 18 & 71 & 7 & 0$^\sharp$ & 0 \\
172	H7 duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ & 0 \\
173	H8 prem-subset & 6  & 5  & 8   & 0 & --- & 0 \\
174	H9 ex falso    & --- & --- & --- & --- & --- & \textbf{100} \\
175	Tautological   & --- & --- & --- & --- & s42 & --- \\
176	Repetition     & s43 & --- & --- & --- & --- & --- \\
177	Contradiction  & 1k & --- & --- & --- & --- & --- \\
178	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- & --- \\
179	Query-as-fact  & --- & --- & --- & --- & s44 & --- \\
180	\midrule
181	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} & \textbf{0} \\
182	\bottomrule
183	\end{tabular}}
184	\caption{Nine hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds; 1.7B: Qwen3-1.7B ISR $\beta{=}0.1$ seed~42). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
185	\label{tab:hacking-taxonomy}
186	\end{table}
187	
188	The nine modes (Table~\ref{tab:hacking-taxonomy}; definitions in Appendix~\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 reward conditions.
189	The three dominant modes---\textbf{H1} (conclusion embedding, GRPO-universal at $68$--$100\%$), \textbf{H7} (conclusion duplication, ISR-amplified ${\sim}5\times$; Fisher $p{=}1.3{\times}10^{-39}$), and \textbf{H8} (premise-subset gaming; Appendix~\ref{app:h8})---account for $>90\%$ of hacking.
190	H7 includes an obfuscated subtype \textbf{H7b} ($14/231$) that evades text-match classifiers via vacuous quantifier wrapping, simultaneously gaming execution reward, ISR, and the hacking detector (\S\ref{sec:discussion}).
191	The cross-condition pattern: \emph{reward formulation determines hacking composition but not prevalence}---all GRPO conditions show $\geq 80\%$ pooled hacking; only SFT achieves $92.3\%$ non-hacking.
192	No GRPO condition produces a high-PR, majority non-hacking run; the taxonomy is descriptive, not exhaustive (query-as-fact gaming was discovered only via functional cross-validation).
193	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "b1fd2b46-eec5-429e-89a5-f6648fad73bf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nCross-scale evidence from Qwen3-1.7B reveals a novel gaming mode (\\S\\ref{sec:crossscale}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\\texttt{eval\\_sta.py}) so training-log ISR is never compared across runs.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the nine cataloged patterns, a necessary but not sufficient condition for semantic correctness.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps, the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}47$\\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nBy 1000 steps, all three converge to high PR ($0.95{\\pm}0.05$) but $0\\%$ non-hacking (15 samples escape text-match classifiers but are functionally degenerate; see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8). %% registry: plan016-extended-1000-s42, plan001-exec-only-s43-1000-r2, plan001-exec-only-s44-1000-r2\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$; per-seed range ${\\sim}$91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.\nA 100-step RL checkpoint (Appendix~\\ref{app:100step}) at $\\text{PR}{=}32\\%$ already shows 31.2\\% hacking (vs.\\ SFT's 7.7\\%; $\\text{OR}{=}5.5$, 95\\% CI $[1.4, 22.0]$), indicating reward hacking emerges early in RL training, not merely at high PR.\n\n\\subsection{ISR as Reward: Goodhart Effects}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nThe headline finding: ISR-as-reward produces an empirical instance of Goodhart's Law~\\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.\nWe test four dose levels ($\\beta\\in\\{0.05, 0.1, 0.2, 0.3\\}$); gaming dominates at every $\\beta$, with qualitatively different failure modes across the dose-response curve.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random H7 driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}.}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-amplified gaming.}\nH7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\\sim}5\\times$: $70.6\\%$ ($163/231$) under ISR vs.\\ $13.7\\%$ ($36/262$) under random (Fisher $p{=}1.3{\\times}10^{-39}$, $\\text{OR}{=}15.05$, 95\\% CI $[9.6, 23.6]$). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nRandom H7 is highly seed-dependent: $38.3\\%$ in seed~43 vs.\\ $0\\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\\%$, Table~\\ref{tab:fol-detailed}).\nH7---a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction (\\S\\ref{sec:taxonomy-method})---is the canonical Goodhart exploit: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both conditions (pooled: ISR $89\\%$, random $85\\%$).\nThe composition differs: H1 alone accounts for $71\\%$ under random vs.\\ $18\\%$ under ISR---ISR converts H1 into H7 rather than reducing total embedding (Figure~\\ref{fig:hacking-composition}).\nRandom also yields higher and more stable PR ($87{\\pm}8\\%$ vs.\\ $77{\\pm}14\\%$; Cohen's $d{=}0.88$, $n{=}3$ per group).\n\n\\textbf{Premise-count confound.}\nThe one ISR seed not dominated by H7 (s42) has raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ its random control ($0.131$), suggesting genuine improvement.\nThis appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\\text{ISR}\\geq 0.5$ by definition.\nRestricting to non-hacking samples with $\\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\\text{ISR}^{*}{=}0.258$ for ISR vs.\\ $0.243$ for random: a $1.06\\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis\nAfter reclassifying premise-subset gaming (H8; Appendix~\\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\\ref{app:hacking-modes}), ISR $\\beta{=}0.1$ non-hacking rate ($6.06\\%$, $14/231$) is numerically lower than random ($9.5\\%$, $25/262$), but the difference is not statistically significant (Fisher $p{=}0.182$, $\\text{OR}{=}0.61$, 95\\% CI $[0.31, 1.21]$, n.s.; Wilson 95\\% CI: ISR $[3.6\\%, 9.9\\%]$, Random $[6.5\\%, 13.7\\%]$; Appendix Table~\\ref{tab:bootstrap-ci}). %% D095 FINAL Fisher test\nThe key asymmetry is not in non-hacking rates but in gaming \\emph{composition}: ISR converts stochastic H7 into near-deterministic convergence ($2/3$ seeds ${\\geq}97\\%$), while random H7 remains seed-dependent and H1-dominated.\nThe raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{Training ISR trajectories across reward conditions. ISR $\\beta{=}0.1$ seeds rise rapidly toward $\\text{ISR}{\\approx}1$ (Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\\text{ISR}{\\geq}0.5$ by construction), not genuine structural quality; random $\\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\textbf{Temporal collapse under ISR $\\beta{=}0.1$.}\nFigure~\\ref{fig:training-isr-curves} traces training ISR across conditions.\nExtended training (1000 steps) reveals that ISR $\\beta{=}0.1$'s non-hacking rate at 500 steps ($17.3\\%$, seed~42) is transient: by step 1000, H7 gaming escalates from $16.0\\%$ to $96.7\\%$ while the non-hacking rate collapses to $2.2\\%$ ($n_{\\text{comp}}$: $5.58{\\to}2.89$).\nThe optimization converges to a fixed point where $\\text{ISR}^{*}{=}0.88$, superficially suggesting structural improvement but reflecting near-complete tautological gaming.\nThis mirrors the exec-only 1000-step trajectory (\\S\\ref{sec:diagnostic}): both converge to ${\\sim}0\\%$ non-hacking proofs despite opposite ISR values ($0.88$ vs.\\ $0.003$), demonstrating that ISR is gamed upward under ISR-as-reward and downward under exec-only---two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\n\n\\textbf{Micro-dose ISR ($\\beta{=}0.05$): gaming at minimal signal.}\nEven at $\\beta{=}0.05$, the lowest dose tested (seed~42), 100\\% of proved samples ($n{=}55$) are H7a tautologies with 0\\% non-hacking, showing that gaming emerges at the minimum ISR signal strength. %% registry: sweep-isr-b005-s42\n\n\\textbf{Medium-dose ISR ($\\beta{=}0.2$): maximum exploitation.}\nAt $\\beta{=}0.2$, all three seeds converge to H7a tautology with $0\\%$ non-hacking (pooled $n{=}290$), the maximum exploitation point in the dose-response curve.\nSeeds achieve $\\text{ISR}^{*}{=}0.55$--$0.96$ through single-premise-equals-conclusion constructions. %% registry: sweep-isr-b02-s42/s43/s44\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$, spanning 18--95\\%); each seed converges to a distinct pathway (Appendix~\\ref{app:detailed-results}). %% registry: plan002-additive-b03-s42/s43/s44\nSeed~42: \\emph{reward collapse} ($\\text{PR}{=}18\\%$), following the pattern described by~\\citet{gao-reward-overoptimization}.\nSeed~43: \\emph{H1 shortcutting} ($\\text{PR}{=}86\\%$, $\\text{H1}{=}69\\%$, only $23\\%$ non-hacking).\nSeed~44: \\emph{pure H7 gaming} ($\\text{PR}{=}95\\%$, $\\text{H7}{=}100\\%$, $\\text{ISR}^{*}{=}0.742$, $0\\%$ non-hacking)---simultaneously gaming \\emph{both} execution and structural metrics through the same construction.\nThe random control at $\\beta{=}0.3$ is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$, spanning 23--92\\%) with near-universal H1 hacking ($91\\%$, pooled) and ${\\leq}4\\%$ non-hacking per seed; high-dose proxy weighting destabilizes training regardless of signal source; ISR produces diverse failure modes (reward collapse, H1 shortcutting, pure H7 gaming) while random converges to H1-dominated hacking with sporadic H7 ($7\\%$ pooled, $0$--$7$ H7a per seed; ISR vs.\\ random H7 $\\text{OR}{=}13.7$, 95\\% CI $[7.0, 26.8]$) (Appendix~\\ref{app:beta03}).\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Left}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \\textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce the Goodhart effects observed in FOL?\nDetailed per-seed numbers are in Appendix Table~\\ref{tab:prolog-detailed}.\n\n\\textbf{Prolog exec-only: ISR catches redundancy across logics.}\nTwo of three seeds (s42, s43) show $\\text{ISR}^{*}{\\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3\nInspection reveals \\emph{redundant coding}: ground facts repeated multiple times (e.g., \\texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.\nThis is a different failure semantics from FOL exec-only (conclusion embedding), but $\\text{ISR}^{*}$ flags both.\nWe are careful to distinguish: exec-only \\emph{low} ISR signals \\emph{redundancy}; ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming} (\\S\\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.\n\n\\textbf{Prolog ISR-as-reward: consistent gaming across all seeds.}\nThe Prolog result is qualitatively consistent with FOL: 3/3 seeds reach $0\\%$ non-hacking via three distinct mechanisms (Figure~\\ref{fig:prolog-comparison}).\nSeed~42: clean H7 tautologies ($\\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42\nSeed~43: \\emph{degenerate uppercase pseudo-Prolog} (e.g., \\texttt{MARY\\_IS\\_AN\\_AVA\\-DEOTE.}); strict text-match returns $\\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\\text{necessary}}{=}1$ (functionally H7). %% registry: plan006-prolog-sta-s43\nSeed~44: \\emph{query-as-fact gaming}---the model transforms the NL question into a snake-case atom asserted as both fact and query (e.g., \\texttt{is\\_the\\_dog\\_furry.}), with $95/97$ proved samples at $n_{\\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44\nSeed~44 evaded our initial strict classifier (reported $100\\%$ non-hacking); functional cross-validation exposed it---a methodological lesson that text-match classifiers have blind spots and STA's necessity profile is the cross-check.\nWe attribute Prolog's complete collapse to its simpler operational semantics: a broader gaming basin makes the non-hacking residual disappear.\nThis is a qualitative observation from a single configuration (Prolog + ISR $\\beta{=}0.1$, 3 seeds); generalization to other logic types requires further experimentation.\n\n\\subsection{Cross-Scale Evidence}\n\\label{sec:crossscale}\n\nTo test whether ISR gaming generalizes beyond Qwen3-4B, we train Qwen3-1.7B under ISR $\\beta{=}0.1$ ($K{=}4$, seed~42, 500 steps).\nThe smaller model achieves $\\text{PR}{=}93\\%$ with $\\text{ISR}^{*}{=}0.2625$---but 100\\% of proved samples ($n{=}93$) exhibit a single novel hacking mode absent from all 4B experiments: \\textbf{H9 (ex falso quodlibet)}, where the model injects logically contradictory premises (e.g., $P(x)$ and $\\neg P(x)$), enabling any conclusion to follow from the contradiction. %% registry: w2-qwen3-1.7b-isr-pilot\nMode collapse onset occurs at step~463.\nISR registers $>0$ because each contradictory premise is individually ``necessary'' under LOO (removing either side of the contradiction breaks the \\emph{ex falso} derivation), yet the formalization is semantically vacuous.\n\nA matched 1.7B exec-only run reaches only $\\text{PR}{=}3\\%$ (seed~42, 500 steps), indicating that ISR bonus is the factor enabling high PR at this scale---but the learned strategy is entirely gaming. %% registry: w2-qwen3-1.7b-exec-pilot\nThe 4B model never discovers H9 under any condition tested; smaller capacity evidently selects a different basin in the Goodhart landscape.\nThis single-seed result demonstrates that ISR gaming is not scale-specific---the failure mode transfers across model sizes, with the smaller model finding a qualitatively novel exploit.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{ISR}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ & 0 \\\\\nH7 duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ & 0 \\\\\nH8 prem-subset & 6  & 5  & 8   & 0 & --- & 0 \\\\\nH9 ex falso    & --- & --- & --- & --- & --- & \\textbf{100} \\\\\nTautological   & --- & --- & --- & --- & s42 & --- \\\\\nRepetition     & s43 & --- & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 & --- \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Nine hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds; 1.7B: Qwen3-1.7B ISR $\\beta{=}0.1$ seed~42). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe nine modes (Table~\\ref{tab:hacking-taxonomy}; definitions in Appendix~\\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 reward conditions.\nThe three dominant modes---\\textbf{H1} (conclusion embedding, GRPO-universal at $68$--$100\\%$), \\textbf{H7} (conclusion duplication, ISR-amplified ${\\sim}5\\times$; Fisher $p{=}1.3{\\times}10^{-39}$), and \\textbf{H8} (premise-subset gaming; Appendix~\\ref{app:h8})---account for $>90\\%$ of hacking.\nH7 includes an obfuscated subtype \\textbf{H7b} ($14/231$) that evades text-match classifiers via vacuous quantifier wrapping, simultaneously gaming execution reward, ISR, and the hacking detector (\\S\\ref{sec:discussion}).\nThe cross-condition pattern: \\emph{reward formulation determines hacking composition but not prevalence}---all GRPO conditions show $\\geq 80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.\nNo GRPO condition produces a high-PR, majority non-hacking run; the taxonomy is descriptive, not exhaustive (query-as-fact gaming was discovered only via functional cross-validation).\n",
      "numLines": 193,
      "startLine": 1,
      "totalLines": 193
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01LomvzGupKcspcP3nziFeAA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "e99cc56c-271e-43af-bc42-f758a1cac80a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1wD3pugkXHh7Cuvui6Jve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14596,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14596
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

_source line 10 · 2026-05-16T18:49:18.050Z_

<details><summary>↩ Tool result · `toolu_01LomvzGupKcspcP3nziFeAA`</summary>

```text
1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
55	
56	
57	\section{STA Algorithm}
58	\label{app:algorithm}
59	
60	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
61	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
62	
63	
64	\section{Extended Discussion}
65	\label{app:extended-discussion}
66	
67	\paragraph{What ISR measures---and what it does not.}
68	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
69	This is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.
70	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
71	ISR and downstream task performance are uncorrelated.
72	ISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
73	
74	Critically, low ISR carries different semantics depending on the training objective.
75	Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than an absence of reasoning (\S\ref{sec:crosslogic}).
76	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
77	ISR values must always be interpreted relative to the optimization objective that produced them.
78	
79	\paragraph{The premise-count confound.}
80	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
81	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.
82	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
83	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
84	This bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
85	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
86	
87	\begin{table}[h]
88	\centering
89	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for H8 reclassification and H7 false negatives (Appendix~\ref{app:h8}).}
90	\label{tab:bootstrap-ci}
91	\small
92	\resizebox{\columnwidth}{!}{%
93	\begin{tabular}{@{}lcccc@{}}
94	\toprule
95	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
96	\midrule
97	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (H8+FN corrected)}} \\
98	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
99	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
100	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
101	\midrule
102	\multicolumn{5}{@{}l}{\textit{H7 gaming rate}} \\
103	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
104	\midrule
105	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
106	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
107	\bottomrule
108	\end{tabular}}
109	\\[2pt]
110	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
111	\end{table}
112	
113	\paragraph{H7 dose-response gradient.}
114	H7 tautology follows a dose-response pattern across four ISR dose levels: $\beta{=}0.05$ (single seed) yields $100\%$ H7 ($n{=}55$), $\beta{=}0.1$ reaches $70.6\%$ ($163/231$ pooled), $\beta{=}0.2$ produces $100\%$ H7 across all three seeds ($n{=}290$), and $\beta{=}0.3$ shows $50\%$ pooled H7 with mode diversity.
115	The random control provides contrast: random $\beta{=}0.1$ produces $13.7\%$ H7 ($36/262$; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 H7a samples per seed.
116	H7 tautological collapse is an absorbing state under ISR reward: once discovered as the global ISR-maximizing exploit, genuine output drops to zero regardless of $\beta$---every ISR dose tested produces dominant gaming.
117	
118	\paragraph{Goodhart effects: implications.}
119	The finding extends beyond this specific system.
120	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---an instance of Goodhart's Law~\citep{manheim-goodhart-taxonomy} where any diagnostic metric risks becoming a target when optimized.
121	The dose-response pattern ($\beta{=}0.05$/$0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.2$: maximum exploitation; $\beta{=}0.3$: PR collapse to 18\% vs.\ 48\% random) maps onto the overoptimization trajectory predicted by~\citet{gao-reward-overoptimization}, with the additional feature that the proxy being gamed is itself a gaming detector.
122	$\beta\in\{0.05,0.1,0.2\}$ instantiate the regressional variant~\citep{manheim-goodhart-taxonomy} where the diagnostic is gamed through its own measurement mechanism; $\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.
123	The practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.
124	
125	\paragraph{Single-seed unreliability.}
126	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
127	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
128	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
129	
130	
131	\section{Hacking Mode Definitions}
132	\label{app:hacking-modes}
133	
134	We identify nine distinct reward hacking modes across all experiments.
135	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
136	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
137	
138	\begin{table}[h]
139	\centering
140	\small
141	\resizebox{\columnwidth}{!}{%
142	\begin{tabular}{@{}llcccc@{}}
143	\toprule
144	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
145	\midrule
146	H1 & Concl.\ in premises & 87 & 18 & 71 & 7 \\
147	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
148	H8 & Premise-subset gaming & 6 & 5 & -- & 0 \\
149	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
150	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
151	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
152	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
153	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
154	\bottomrule
155	\end{tabular}}
156	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$ ISR $+$ 36 random) and H7b (obfuscated tautology, $n{=}14$; primarily s44). $^\dagger$Random H7 driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
157	\label{tab:hacking-taxonomy-app}
158	\end{table}
159	
160	\paragraph{Classifier Validation.}
161	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
162	H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
163	No training data or manual annotation is used for classification.
164	
165	To estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
166	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
167	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
168	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
169	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
170	
171	\subsection{H8 --- Premise-Subset Gaming}
172	\label{app:h8}
173	
174	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).
175	We term this \textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
176	
177	\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
178	Automated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.
179	
180	\paragraph{Audit scope and limitations.}
181	Full H8 audit was completed for ISR $\beta{=}0.1$ seed~42 only.
182	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.
183	Random $\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.
184	
185	\paragraph{H7 false-negative correction (H7b obfuscated tautology).}
186	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
187	Manual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
188	We classify these as \textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.
189	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\S\ref{sec:taxonomy}).
190	After correction, ISR s44 non-hacking${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.
191	
192	\paragraph{Impact on non-hacking-rate comparison.}
193	After H8 reclassification and H7 false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
194	The direction is consistent with ISR-amplified gaming modes (H7, H8) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
195	
196	\subsection{H1 --- Conclusion Embedding}
197	
198	\paragraph{Definition.}
199	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
200	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
201	
202	\paragraph{Example (FOL).}
203	{\small\begin{verbatim}
204	Premises:
205	  all x (bird(x) -> flies(x)).
206	  bird(tweety).
207	  flies(tweety).  % conclusion embedded
208	Conclusion: flies(tweety).
209	\end{verbatim}}
210	
211	\paragraph{ISR interaction.}
212	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
213	ISR does not distinguish trivial from substantive necessity.
214	
215	\paragraph{Prevalence.}
216	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\% across all RL conditions.
217	Under exec-only and Random reward, it manifests as H1 (71--93\%); under ISR reward, it shifts to H7 (70.6\% pooled).
218	
219	
220	\subsection{H7a --- Conclusion Duplication (Standard)}
221	
222	\paragraph{Definition.}
223	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
224	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
225	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
226	
227	\paragraph{Example (FOL).}
228	{\small\begin{verbatim}
229	Premises:
230	  all x ((A(x)&B(x))->(C(x)|D(x))).
231	Conclusion:
232	  all x ((A(x)&B(x))->(C(x)|D(x))).
233	\end{verbatim}}
234	
235	\paragraph{ISR interaction.}
236	ISR~$\approx 0.8$--$1.0$.
237	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
238	H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.
239	
240	\paragraph{Prevalence.}
241	H7a (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
242	Combined H7 (H7a + H7b): 70.6\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).
243	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all H7a; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
244	
245	
246	\subsection{H7b --- Obfuscated Tautology}
247	
248	\paragraph{Definition.}
249	A single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.
250	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
251	
252	\paragraph{Example (FOL, vacuous quantifier wrapping).}
253	{\small\begin{verbatim}
254	Premises:
255	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
256	Conclusion:
257	  all x ((A(x)&B(x))->(C(x)|D(x))).
258	\end{verbatim}}
259	The premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.
260	
261	\paragraph{ISR interaction.}
262	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
263	H7b simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).
264	This triple gaming makes H7b the most complete Goodhart case we observe.
265	
266	\paragraph{Prevalence.}
267	Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
268	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
269	
270	
271	\subsection{Tautological Collapse}
272	
273	\paragraph{Definition.}
274	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
275	
276	\paragraph{Example (FOL).}
277	\begin{verbatim}
278	Premises: p(a).
279	Conclusion: p(a).
280	\end{verbatim}
281	
282	\paragraph{ISR interaction.}
283	ISR~$=1.0$ (the sole premise is necessary).
284	Distinguished from H7 by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
285	
286	\paragraph{Prevalence.}
287	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
288	Also observed in Prolog exec+STA seed~42 (100\% H7, PR~$=0.50$).
289	
290	
291	\subsection{Repetition Collapse}
292	
293	\paragraph{Definition.}
294	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
295	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
296	
297	\paragraph{Example (Prolog).}
298	\begin{verbatim}
299	penguin(fido).
300	penguin(fido).
301	penguin(fido).
302	... (repeated to 512 tokens)
303	query(penguin(fido)).
304	\end{verbatim}
305	
306	\paragraph{ISR interaction.}
307	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
308	ISR correctly diagnoses this degeneration.
309	
310	\paragraph{Prevalence.}
311	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
312	
313	
314	\subsection{Complexity-without-Utility}
315	
316	\paragraph{Definition.}
317	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.
318	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
319	
320	\paragraph{Example (FOL).}
321	{\small\begin{verbatim}
322	Premises:
323	  all x all y (R(x,y) ->
324	    exists z (S(x,z) & T(z,y))).
325	  all x (P(x) -> Q(x)).
326	  P(a).            % only this needed
327	Conclusion: Q(a).
328	\end{verbatim}}
329	
330	\paragraph{ISR interaction.}
331	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
332	This is the mode ISR is best calibrated for.
333	
334	\paragraph{Prevalence.}
335	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
336	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
337	
338	
339	\subsection{Contradiction Explosion}
340	
341	\paragraph{Definition.}
342	The component count grows unboundedly over training.
343	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
344	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
345	
346	\paragraph{Example (FOL, 1000-step exec-only).}
347	{\small\begin{verbatim}
348	Premises:
349	  c1. c2. c3. ... c18. % 18.55 mean
350	  % conclusion embedded among premises
351	Conclusion: Q(a).
352	\end{verbatim}}
353	
354	\paragraph{ISR interaction.}
355	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
356	
357	\paragraph{Prevalence.}
358	Observed in extended exec-only training (seed~42, 1000 steps).
359	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
360	
361	
362	\subsection{Query-as-Fact Gaming}
363	
364	\paragraph{Definition.}
365	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
366	Prolog trivially proves the query by unifying with the fact.
367	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
368	
369	\paragraph{Example (Prolog).}
370	\begin{verbatim}
371	% NL: "Fido is happy."
372	% Model output:
373	fido_is_happy.
374	:- fido_is_happy.     % query = fact
375	\end{verbatim}
376	
377	\paragraph{ISR interaction.}
378	ISR~$\approx 0.9$--$1.0$.
379	The single fact is trivially necessary (its removal breaks the query), inflating ISR.
380	Functionally equivalent to H7 but with a distinct surface mechanism.
381	
382	\paragraph{Prevalence.}
383	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
384	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
385	
386	
387	\subsection{H9 --- Ex Falso Quodlibet (Contradiction Injection)}
388	
389	\paragraph{Definition.}
390	The model generates a premise set containing logically contradictory assertions (e.g., $P(x)$ and $\neg P(x)$).
391	From contradictory premises, any conclusion follows by the \emph{ex falso quodlibet} principle, rendering the proof semantically vacuous regardless of the conclusion's content.
392	Unlike the ``contradiction explosion'' mode observed in 4B exec-only at 1000 steps (where contradictions arise incidentally among inflated premise counts), H9 is a \emph{targeted} strategy: the model constructs minimal contradictory pairs that directly enable the proof.
393	
394	\paragraph{Example (FOL).}
395	{\small\begin{verbatim}
396	Premises:
397	  all x (bird(x) -> flies(x)).
398	  bird(tweety).
399	  -bird(tweety).  % contradicts above
400	Conclusion: happy(tweety).
401	% Proof: bird(tweety) & -bird(tweety) -> False -> anything
402	\end{verbatim}}
403	
404	\paragraph{ISR interaction.}
405	ISR~$>0$ because each side of the contradiction is individually necessary under LOO: removing $P(x)$ leaves $\neg P(x)$ alone, which cannot derive a contradiction; removing $\neg P(x)$ leaves the premises consistent but insufficient to derive an unrelated conclusion.
406	The LOO test thus registers both contradictory premises as ``necessary,'' inflating ISR despite the formalization being semantically vacuous.
407	
408	\paragraph{Prevalence.}
409	Observed exclusively in Qwen3-1.7B under ISR $\beta{=}0.1$ (seed~42, 500 steps): 100\% of proved samples ($n{=}93$) exhibit H9.
410	Not observed in any Qwen3-4B experiment across all conditions and seeds tested.
411	Mode collapse onset at step~463 indicates the model converges to this exploit rapidly once discovered. %% registry: w2-qwen3-1.7b-isr-pilot
412	
413	
414	\section{Per-Seed Detailed Results}
415	\label{app:detailed-results}
416	
417	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
418	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
419	ISR values are proved-only ISR$^*$.
420	
421	\begin{table*}[t]
422	\centering
423	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\S$s43-1000 raw ISR (0.531) includes ${+}12\%$ inflation from \texttt{decompose\_fol()} splitting $\exists x(\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}
424	\label{tab:fol-detailed}
425	\label{tab:fol-beta01-detailed}
426	\footnotesize
427	\setlength{\tabcolsep}{3pt}
428	\begin{tabular}{@{}llccccccl@{}}
429	\toprule
430	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
431	\midrule
432	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
433	Base model (no training)
434	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
435	Ground-truth FOL
436	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
437	SFT
438	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
439	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
440	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
441	\cmidrule(l){2-9}
442	  & \multicolumn{2}{l}{3-seed pooled} & \makebox[0pt][l]{$0.130$} & & \makebox[0pt][l]{$0.595$} & & \makebox[0pt][l]{\textbf{92.3}} & $n{=}39$ proved \\
443	\midrule
444	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
445	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
446	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\%$ \\
447	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
448	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
449	  & 43 & 1000 & 0.90 & 0.465$^\S$ & 100 & 0 & 0 & H7 dominant \\
450	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
451	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & H8${=}15\%$ \\
452	\cmidrule(l){2-9}
453	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step \\
454	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.95{\pm}0.05$} & & \makebox[0pt][l]{$0.16{\pm}0.27$} & & \makebox[0pt][l]{$0.0{\pm}0.0$} & 1000-step \\
455	\midrule
456	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
457	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed H1+H7+H8 \\
458	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\
459	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\
460	\cmidrule(l){2-9}
461	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
462	\midrule
463	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
464	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\
465	\midrule
466	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
467	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\
468	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\
469	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\cap$H8: 6) \\
470	\cmidrule(l){2-9}
471	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.87{\pm}0.08$} & & \makebox[0pt][l]{$0.117{\pm}0.042$} & & & H7 seed-dep.: 0/38/0\% \\
472	\midrule
473	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
474	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
475	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{N-H}}{=}3$ \\
476	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
477	\cmidrule(l){2-9}
478	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & & \\
479	\bottomrule
480	\end{tabular}
481	\end{table*}
482	
483	
484	\begin{table*}[t]
485	\centering
486	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
487	\label{tab:prolog-detailed}
488	\small
489	\begin{tabular}{@{}llcccccl@{}}
490	\toprule
491	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
492	\midrule
493	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
494	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
495	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
496	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
497	\cmidrule(l){2-8}
498	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
499	\midrule
500	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
501	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
502	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
503	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
504	\cmidrule(l){2-8}
505	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.699{\pm}0.45$} & & 3/3 Goodhart, 0\% non-hacking \\
506	\bottomrule
507	\end{tabular}
508	
509	\vspace{4pt}
510	{\footnotesize
511	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
512	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\
513	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
514	}
515	\end{table*}
516	
517	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
518	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
519	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
520	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
521	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
522	
523	\paragraph{Prolog: consistent gaming across all seeds via three distinct pathways.}
524	All three Prolog exec+ISR seeds exhibit Goodhart effects with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
525	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
526	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
527	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
528	The diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
529	
530	\subsection{Per-Seed Results at $\beta{=}0.3$}
531	\label{app:beta03}
532	
533	Table~\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\beta{=}0.3$.
534	The three ISR seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
535	
536	\begin{table}[h]
537	\centering
538	\caption{Per-seed results at $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}
539	\label{tab:beta03-detailed}
540	\small
541	\resizebox{\columnwidth}{!}{%
542	\begin{tabular}{@{}llcccccl@{}}
543	\toprule
544	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Mode} \\
545	\midrule
546	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
547	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\
548	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & H1 shortcutting \\
549	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure H7 gaming \\
550	\cmidrule(l){2-8}
551	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.66{\pm}0.42$} & & \makebox[0pt][l]{$0.39{\pm}0.31$} & & \\
552	\midrule
553	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
554	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\
555	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{N-H}}{=}3$ \\
556	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
557	\cmidrule(l){2-8}
558	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & \\
559	\bottomrule
560	\end{tabular}}
561	\end{table}
562	
563	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
564	\label{app:100step}
565	
566	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%---higher than SFT (13.0\%, 3-seed pooled) but still early in training.
567	Of the 32 proved samples, 9 (28.1\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
568	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
569	This demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.
570	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
571	
572	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
573	\label{app:o1-ablation}
574	
575	To justify the per-clause LOO design (\S\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\text{fast\_ISR}(x) = 1$ if $x$ is proved \emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
576	The reward becomes $r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$.
577	After 500 steps (seed~42), this variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$---functionally zero---compared to $\text{ISR}^*{=}0.132$ under standard exec-only and $\text{ISR}^*{=}0.42$ under ISR $\beta{=}0.1$.
578	
579	\paragraph{ISR signal vs.\ training dynamics.}
580	At the \emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.
581	At the \emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.
582	This confound depresses prove rate by 30 percentage points ($63\%$ vs.\ $93\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.
583	The result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.
584	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "5935d6de-4b0b-4101-b06e-67de32fe0a11",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 4 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\begin{table}[h]\n\\centering\n\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for H8 reclassification and H7 false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (H8+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{H7 gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table}\n\n\\paragraph{H7 dose-response gradient.}\nH7 tautology follows a dose-response pattern across four ISR dose levels: $\\beta{=}0.05$ (single seed) yields $100\\%$ H7 ($n{=}55$), $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$ pooled), $\\beta{=}0.2$ produces $100\\%$ H7 across all three seeds ($n{=}290$), and $\\beta{=}0.3$ shows $50\\%$ pooled H7 with mode diversity.\nThe random control provides contrast: random $\\beta{=}0.1$ produces $13.7\\%$ H7 ($36/262$; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 H7a samples per seed.\nH7 tautological collapse is an absorbing state under ISR reward: once discovered as the global ISR-maximizing exploit, genuine output drops to zero regardless of $\\beta$---every ISR dose tested produces dominant gaming.\n\n\\paragraph{Goodhart effects: implications.}\nThe finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---an instance of Goodhart's Law~\\citep{manheim-goodhart-taxonomy} where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.05$/$0.1$: proxy gaming inflates ISR without genuine improvement; $\\beta{=}0.2$: maximum exploitation; $\\beta{=}0.3$: PR collapse to 18\\% vs.\\ 48\\% random) maps onto the overoptimization trajectory predicted by~\\citet{gao-reward-overoptimization}, with the additional feature that the proxy being gamed is itself a gaming detector.\n$\\beta\\in\\{0.05,0.1,0.2\\}$ instantiate the regressional variant~\\citep{manheim-goodhart-taxonomy} where the diagnostic is gamed through its own measurement mechanism; $\\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.\nThe practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify nine distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ in premises & 87 & 18 & 71 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nH8 & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$ ISR $+$ 36 random) and H7b (obfuscated tautology, $n{=}14$; primarily s44). $^\\dagger$Random H7 driven by seed~43 (38.3\\%); seeds~42/44: 0\\%. Exec: H1${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nH1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\n\\subsection{H8 --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).\nWe term this \\textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull H8 audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.\n\n\\paragraph{H7 false-negative correction (H7b obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter H8 reclassification and H7 false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (H7, H8) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{H1 --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as H1 (71--93\\%); under ISR reward, it shifts to H7 (70.6\\% pooled).\n\n\n\\subsection{H7a --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nH7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nH7a (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined H7 (H7a + H7b): 70.6\\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 13.7\\% (36/262, all H7a; driven by seed~43 at 38.3\\%, seeds~42 and~44 at 0\\%).\n\n\n\\subsection{H7b --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\nThe premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nH7b simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).\nThis triple gaming makes H7b the most complete Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound primarily in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from H7 by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% H7 by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% H7, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe single fact is trivially necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to H7 but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\subsection{H9 --- Ex Falso Quodlibet (Contradiction Injection)}\n\n\\paragraph{Definition.}\nThe model generates a premise set containing logically contradictory assertions (e.g., $P(x)$ and $\\neg P(x)$).\nFrom contradictory premises, any conclusion follows by the \\emph{ex falso quodlibet} principle, rendering the proof semantically vacuous regardless of the conclusion's content.\nUnlike the ``contradiction explosion'' mode observed in 4B exec-only at 1000 steps (where contradictions arise incidentally among inflated premise counts), H9 is a \\emph{targeted} strategy: the model constructs minimal contradictory pairs that directly enable the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  -bird(tweety).  % contradicts above\nConclusion: happy(tweety).\n% Proof: bird(tweety) & -bird(tweety) -> False -> anything\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$>0$ because each side of the contradiction is individually necessary under LOO: removing $P(x)$ leaves $\\neg P(x)$ alone, which cannot derive a contradiction; removing $\\neg P(x)$ leaves the premises consistent but insufficient to derive an unrelated conclusion.\nThe LOO test thus registers both contradictory premises as ``necessary,'' inflating ISR despite the formalization being semantically vacuous.\n\n\\paragraph{Prevalence.}\nObserved exclusively in Qwen3-1.7B under ISR $\\beta{=}0.1$ (seed~42, 500 steps): 100\\% of proved samples ($n{=}93$) exhibit H9.\nNot observed in any Qwen3-4B experiment across all conditions and seeds tested.\nMode collapse onset at step~463 indicates the model converges to this exploit rapidly once discovered. %% registry: w2-qwen3-1.7b-isr-pilot\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\\S$s43-1000 raw ISR (0.531) includes ${+}12\\%$ inflation from \\texttt{decompose\\_fol()} splitting $\\exists x(\\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & \\makebox[0pt][l]{$0.130$} & & \\makebox[0pt][l]{$0.595$} & & \\makebox[0pt][l]{\\textbf{92.3}} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.90 & 0.465$^\\S$ & 100 & 0 & 0 & H7 dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & H8${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.95{\\pm}0.05$} & & \\makebox[0pt][l]{$0.16{\\pm}0.27$} & & \\makebox[0pt][l]{$0.0{\\pm}0.0$} & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed H1+H7+H8 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\\cap$H8: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.87{\\pm}0.08$} & & \\makebox[0pt][l]{$0.117{\\pm}0.042$} & & & H7 seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.53{\\pm}0.31$} & & \\makebox[0pt][l]{$0.146{\\pm}0.21$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & H7 tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional H7$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.62{\\pm}0.31$} & & \\makebox[0pt][l]{$0.699{\\pm}0.45$} & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict H7 classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: consistent gaming across all seeds via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart effects with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean H7 tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\\beta{=}0.3$.\nThe three ISR seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & H1 shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure H7 gaming \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.66{\\pm}0.42$} & & \\makebox[0pt][l]{$0.39{\\pm}0.31$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%---higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nTo justify the per-clause LOO design (\\S\\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved \\emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nThe reward becomes $r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$.\nAfter 500 steps (seed~42), this variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$---functionally zero---compared to $\\text{ISR}^*{=}0.132$ under standard exec-only and $\\text{ISR}^*{=}0.42$ under ISR $\\beta{=}0.1$.\n\n\\paragraph{ISR signal vs.\\ training dynamics.}\nAt the \\emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.\nAt the \\emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.\nThis confound depresses prove rate by 30 percentage points ($63\\%$ vs.\\ $93\\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.\nThe result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.\n",
      "numLines": 584,
      "startLine": 1,
      "totalLines": 584
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
Now I have a clear picture of all three files. Let me identify what needs to change:

1. **method.tex**: The taxonomy section already mentions H9 and "nine" modes (lines 79, 88-90). Let me check if it needs updates. Looking at line 79: "we identify nine structural-degeneration modes" - this already says nine. Line 88-90 already mentions "contradiction explosion" and "H9: ex falso quodlibet". So method.tex already has H9 content.

Wait, let me re-read more carefully. 

Line 79 says "nine structural-degeneration modes" and lines 82-90 list all nine including H9 at line 90, so method.tex is already updated. For experiments.tex, line 5 mentions "Cross-scale evidence from Qwen3-1.7B reveals a novel gaming mode" and section 5.4 already describes H9 in detail, with line 12 saying "nine cataloged patterns" and the table at line 174 including H9. Line 188 also says "nine modes", so experiments.tex is already updated too. Now I need to check appendix.tex starting at line 134.

Lines 134 and 387-411 show that appendix.tex also has the full H9 subsection with "nine distinct reward hacking modes" mentioned. Wait—it looks like H9 is already present throughout all three files. Let me double-check by verifying the key references across each document to make sure nothing was missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "42f312a9-42a0-4915-b73a-916e34b679ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1BkRwpjgjWpNjZUawNKe8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25907,
      "cache_read_input_tokens": 26437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25907
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

All three files already contain H9 content. Let me verify there are no remaining references to "8 modes" or "H1-H8" that need updating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "b31f2dc9-d955-46f7-98be-bbbd6695dc38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1BkRwpjgjWpNjZUawNKe8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25907,
      "cache_read_input_tokens": 26437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25907
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

<details open><summary>🔧 Tool call — Grep · `toolu_01JGkkomhsikFWXqhW7jVeMT`</summary>

```json
{
  "pattern": "eight|8 modes|H1.H8|H1--H8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-i": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "ff61c6bf-4e3f-42ad-bab7-53776181a992",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1BkRwpjgjWpNjZUawNKe8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25907,
      "cache_read_input_tokens": 26437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25907
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

_source line 14 · 2026-05-16T18:49:35.726Z_

<details><summary>↩ Tool result · `toolu_01JGkkomhsikFWXqhW7jVeMT`</summary>

```text
paper/experiments.tex:33:By 1000 steps, all three converge to high PR ($0.95{\pm}0.05$) but $0\%$ non-hacking (15 samples escape text-match classifiers but are functionally degenerate; see Appendix~\ref{app:h8} and Table~\ref{tab:fol-detailed}), each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8). %% registry: plan016-extended-1000-s42, plan001-exec-only-s43-1000-r2, plan001-exec-only-s44-1000-r2
paper/experiments.tex:111:[Omitted long matching line]
paper/ethics.tex:7:All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
paper/appendix.tex:8:Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
paper/appendix.tex:423:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "a1c33441-9c08-4aaf-ad0a-e03d74a4e8ce",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:33:By 1000 steps, all three converge to high PR ($0.95{\\pm}0.05$) but $0\\%$ non-hacking (15 samples escape text-match classifiers but are functionally degenerate; see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8). %% registry: plan016-extended-1000-s42, plan001-exec-only-s43-1000-r2, plan001-exec-only-s44-1000-r2\npaper/experiments.tex:111:[Omitted long matching line]\npaper/ethics.tex:7:All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.\npaper/appendix.tex:8:Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\npaper/appendix.tex:423:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Grep · `toolu_01Bv13G7VppUBpTmc7wxkf3a`</summary>

```json
{
  "pattern": "nine|9 modes|H1.H9|H1--H9",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-i": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "79372449-d800-4c61-9031-aa809bb0af37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1BkRwpjgjWpNjZUawNKe8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25907,
      "cache_read_input_tokens": 26437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25907
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

_source line 16 · 2026-05-16T18:49:36.431Z_

<details><summary>↩ Tool result · `toolu_01Bv13G7VppUBpTmc7wxkf3a`</summary>

```text
paper/experiments.tex:12:We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the nine cataloged patterns, a necessary but not sufficient condition for semantic correctness.
paper/experiments.tex:184:\caption{Nine hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds; 1.7B: Qwen3-1.7B ISR $\beta{=}0.1$ seed~42). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
paper/experiments.tex:188:The nine modes (Table~\ref{tab:hacking-taxonomy}; definitions in Appendix~\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 reward conditions.
paper/method.tex:79:Across conditions, seeds, and logic types we identify nine structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}).
paper/appendix.tex:134:We identify nine distinct reward hacking modes across all experiments.
paper/introduction.tex:32:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "5b86dc20-a6d6-494f-be11-3e35c73c94a1",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:12:We report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the nine cataloged patterns, a necessary but not sufficient condition for semantic correctness.\npaper/experiments.tex:184:\\caption{Nine hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds; 1.7B: Qwen3-1.7B ISR $\\beta{=}0.1$ seed~42). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\npaper/experiments.tex:188:The nine modes (Table~\\ref{tab:hacking-taxonomy}; definitions in Appendix~\\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 reward conditions.\npaper/method.tex:79:Across conditions, seeds, and logic types we identify nine structural-degeneration modes (full definitions in Appendix~\\ref{app:hacking-modes}).\npaper/appendix.tex:134:We identify nine distinct reward hacking modes across all experiments.\npaper/introduction.tex:32:[Omitted long matching line]",
    "numLines": 6
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the introduction.tex and other files to make sure they're consistent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "84fec83a-4b1c-4094-bb76-6b35b5556041",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYRNeSQ3ZwfsSsLmDmHrqc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 52344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1752
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

_source line 18_

Let me check the introduction and other files for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "63222c8f-4ede-4f3f-8467-b6b937cf1d50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYRNeSQ3ZwfsSsLmDmHrqc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 52344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1752
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

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01616S7Grkd1tpnGQAUyLYgf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "43d71cd1-fd55-4f2d-9031-d4a8f76b2eac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYRNeSQ3ZwfsSsLmDmHrqc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 52344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1752
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

_source line 20 · 2026-05-16T18:49:40.262Z_

<details><summary>↩ Tool result · `toolu_01616S7Grkd1tpnGQAUyLYgf`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems---$95{\pm}5\%$ across three seeds (1000 steps)---yet at convergence, \emph{none} produce structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse---all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
16	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
17	ISR captures structural rather than semantic integrity (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
18	
19	\paragraph{ISR as diagnostic.}
20	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (seed~42; 99.5\% degradation) while PR rises $32\%{\to}96\%$.
21	Three seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.
22	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.
23	
24	\paragraph{ISR as reward: Goodhart effects.}
25	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition---an empirical instance of Goodhart's Law within the \citet{manheim-goodhart-taxonomy} taxonomy, where the diagnostic designed to detect gaming becomes gamed when optimized~\citep{karwowski-goodhart-rl, gao-reward-overoptimization}.
26	At $\beta{=}0.1$, 70.6\% of proved samples exhibit conclusion duplication---versus 13.7\% under matched random (Fisher $p{<}10^{-38}$; random tautological gaming is highly seed-dependent), showing ISR amplifies tautological collapse by ${\sim}5{\times}$; the one seed with a non-trivial residual reduces to $1.06\times$ random after controlling for a premise-count confound.
27	Across four dose levels ($\beta\in\{0.05,0.1,0.2,0.3\}$), gaming dominates at every $\beta$: $\beta{=}0.2$ is the maximum exploitation point (0\% non-hacking, all seeds), while $\beta{=}0.3$ exceeds the training stability boundary (PR $66{\pm}42\%$), with seeds diverging into reward collapse, shortcut dominance, and pure metric gaming.
28	The effect transfers to Prolog: 3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming} that bypasses text-match classifiers.
29	ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer.}
30	
31	\paragraph{Contributions.}
32	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\S\ref{sec:diagnostic}); (\textbf{C2}) an empirical instance of Goodhart's Law~\citep{manheim-goodhart-taxonomy} where a diagnostic is gamed when optimized---a random control shows ISR amplifies tautological gaming ${\sim}5{\times}$ (70.6\% vs.\ 13.7\%, $p{<}10^{-38}$), a dose-response across four $\beta$ values shows gaming dominates at every level, and premise-count-matched analysis shows the sole apparent gain is an LOO artifact (\S\ref{sec:goodhart}); (\textbf{C3}) cross-logic transfer to Prolog with consistent Goodhart effects across all seeds (\S\ref{sec:crosslogic}); (\textbf{C4}) a nine-mode hacking taxonomy including query-as-fact gaming, obfuscated tautology, and a scale-specific \emph{ex falso} mode, motivating functional cross-validation of diagnostics (\S\ref{sec:taxonomy}).
33	These are cautionary results for any work treating a structural proxy as a training signal.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "c744f3a8-c286-4e25-a976-177324ed2c26",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nGRPO-trained formalizers converge to high prove rates on first-order logic problems---$95{\\pm}5\\%$ across three seeds (1000 steps)---yet at convergence, \\emph{none} produce structurally sound outputs.\nEach seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse---all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.\n\n\\paragraph{The execution-only blind spot.}\nProve rate---the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line of work documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), which applies \\emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\nISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (seed~42; 99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.\n\n\\paragraph{ISR as reward: Goodhart effects.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR is gamed at its own definition---an empirical instance of Goodhart's Law within the \\citet{manheim-goodhart-taxonomy} taxonomy, where the diagnostic designed to detect gaming becomes gamed when optimized~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization}.\nAt $\\beta{=}0.1$, 70.6\\% of proved samples exhibit conclusion duplication---versus 13.7\\% under matched random (Fisher $p{<}10^{-38}$; random tautological gaming is highly seed-dependent), showing ISR amplifies tautological collapse by ${\\sim}5{\\times}$; the one seed with a non-trivial residual reduces to $1.06\\times$ random after controlling for a premise-count confound.\nAcross four dose levels ($\\beta\\in\\{0.05,0.1,0.2,0.3\\}$), gaming dominates at every $\\beta$: $\\beta{=}0.2$ is the maximum exploitation point (0\\% non-hacking, all seeds), while $\\beta{=}0.3$ exceeds the training stability boundary (PR $66{\\pm}42\\%$), with seeds diverging into reward collapse, shortcut dominance, and pure metric gaming.\nThe effect transfers to Prolog: 3/3 seeds yield 0\\% non-hacking via distinct mechanisms, including \\emph{query-as-fact gaming} that bypasses text-match classifiers.\nISR's asymmetry is the central finding: \\emph{reliable as observer, unreliable as optimizer.}\n\n\\paragraph{Contributions.}\nAcross 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) an empirical instance of Goodhart's Law~\\citep{manheim-goodhart-taxonomy} where a diagnostic is gamed when optimized---a random control shows ISR amplifies tautological gaming ${\\sim}5{\\times}$ (70.6\\% vs.\\ 13.7\\%, $p{<}10^{-38}$), a dose-response across four $\\beta$ values shows gaming dominates at every level, and premise-count-matched analysis shows the sole apparent gain is an LOO artifact (\\S\\ref{sec:goodhart}); (\\textbf{C3}) cross-logic transfer to Prolog with consistent Goodhart effects across all seeds (\\S\\ref{sec:crosslogic}); (\\textbf{C4}) a nine-mode hacking taxonomy including query-as-fact gaming, obfuscated tautology, and a scale-specific \\emph{ex falso} mode, motivating functional cross-validation of diagnostics (\\S\\ref{sec:taxonomy}).\nThese are cautionary results for any work treating a structural proxy as a training signal.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01NwoiFna7suz9KVvVZpC5gw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "24f282a5-f69d-4e89-bb52-6ad3cb7e4351",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYRNeSQ3ZwfsSsLmDmHrqc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 52344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1752
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

_source line 22 · 2026-05-16T18:49:40.642Z_

<details><summary>↩ Tool result · `toolu_01NwoiFna7suz9KVvVZpC5gw`</summary>

```text
1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($95{\pm}5\%$, 3 seeds) yet produce zero structurally sound outputs---a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), applying leave-one-out necessity testing to solver inputs.
4	The resulting metric (ISR) exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, localizing the failure to RL.
5	Repurposed as a reward signal, ISR provides an empirical instance of Goodhart's Law~\citep{manheim-goodhart-taxonomy}: it amplifies tautological gaming ${\sim}5{\times}$ versus a matched random control ($p{<}10^{-39}$), and the sole apparent benefit vanishes ($1.06{\times}$) after controlling for a premise-count confound.
6	Gaming dominates across all four dose levels tested; the effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and across model scale (Qwen3-1.7B discovers a qualitatively novel gaming mode absent in 4B).
7	Across 6 conditions, 2 logic types, 2 model scales, and 3 seeds, we catalog 9 hacking modes and document ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "ee4ac551-8d0c-4816-8034-372fcf0d73a4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex",
      "content": "\\begin{abstract}\nGRPO-trained formalizers converge to high prove rates on FOLIO ($95{\\pm}5\\%$, 3 seeds) yet produce zero structurally sound outputs---a failure invisible to execution-based evaluation.\nWe propose \\emph{Solver Trace Ablation} (STA), applying leave-one-out necessity testing to solver inputs.\nThe resulting metric (ISR) exposes a 99.5\\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\\% non-hacking on identical data, localizing the failure to RL.\nRepurposed as a reward signal, ISR provides an empirical instance of Goodhart's Law~\\citep{manheim-goodhart-taxonomy}: it amplifies tautological gaming ${\\sim}5{\\times}$ versus a matched random control ($p{<}10^{-39}$), and the sole apparent benefit vanishes ($1.06{\\times}$) after controlling for a premise-count confound.\nGaming dominates across all four dose levels tested; the effect transfers to Prolog (3/3 seeds, 0\\% non-hacking) and across model scale (Qwen3-1.7B discovers a qualitatively novel gaming mode absent in 4B).\nAcross 6 conditions, 2 logic types, 2 model scales, and 3 seeds, we catalog 9 hacking modes and document ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\\footnote{Code and data: \\url{[anonymized]}}\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_015S9cactK57cq9WGjwsvS26`</summary>

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
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "5c8cb32e-6040-4679-bcde-e71278467328",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYRNeSQ3ZwfsSsLmDmHrqc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 52344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1752
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

_source line 24 · 2026-05-16T18:49:40.911Z_

<details><summary>↩ Tool result · `toolu_015S9cactK57cq9WGjwsvS26`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
5	Repurposed as a training signal, ISR exhibits Goodhart effects~\citep{manheim-goodhart-taxonomy}: across four dose levels ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$), gaming dominates at every $\beta$---amplifying H7 tautological collapse ${\sim}5\times$ at $\beta{=}0.1$ ($70.6\%$ vs.\ $13.7\%$ random, $p{<}10^{-39}$), with the sole apparent ISR gain vanishing ($1.06\times$) after controlling for premise count.
6	The effect is consistent across logic types: Prolog yields 0\% non-hacking in 3/3 seeds via distinct mechanisms including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
7	ISR semantics are objective-dependent: exec-only \emph{low} ISR signals redundancy; ISR-rewarded \emph{high} ISR signals metric gaming.
8	
9	\paragraph{Dose-response pattern.}
10	The relationship between $\beta$ and failure mode is structured across four dose levels: $\beta{=}0.05$ already produces 100\% H7 gaming (single seed), $\beta{=}0.1$ shows ${\sim}5\times$ amplification with partial non-hacking residual, $\beta{=}0.2$ represents the maximum exploitation point (all seeds H7, $0\%$ genuine), and $\beta{=}0.3$ exceeds the training stability boundary with diverse failure modes.
11	H7 tautological collapse is an absorbing state: once discovered as the global ISR-maximizing exploit, genuine output drops to zero regardless of $\beta$.
12	
13	\paragraph{Classifier blind spots.}
14	H7b (obfuscated tautology) and Prolog query-as-fact gaming demonstrate that text-match classifiers have systematic blind spots exploitable by optimization.
15	In both cases, functional LOO analysis exposed gaming invisible to surface-level detection---H7b via vacuous quantifier wrapping ($10/12$ at $\text{ISR}{\geq}0.83$, triple gaming of execution, ISR, and classifier), query-as-fact via $95/97$ tautological samples the strict classifier labeled non-hacking (\S\ref{sec:crosslogic}).
16	H9 (contradiction injection, \S\ref{sec:crossscale}) extends this pattern further: contradictory premises register as individually necessary under LOO, bypassing both text-match and functional $n_{\text{necessary}}$ classifiers---detection requires logic-level consistency checking.
17	These cases collectively argue for mandatory functional cross-validation of text-based hacking classifiers, complemented by logic-level checks for novel exploit classes.
18	
19	\paragraph{Hacking mode switching.}
20	Under identical reward configurations, different seeds converge to qualitatively different modes (Table~\ref{tab:fol-detailed}): random $\beta{=}0.1$ ranges from H8-enriched (s44) to H7-dominant (s43) to highest non-hacking (s42); ISR $\beta{=}0.1$ similarly switches between H1-heavy (s42) and near-pure H7 (s43/s44, ${\geq}97\%$).
21	Single-seed results can therefore misrepresent a reward configuration's hacking profile; multi-seed evaluation with per-mode reporting should be standard.
22	
23	The asymmetry---reliable observer, unreliable optimizer---may generalize to other perturbation-based diagnostics; ISR and similar metrics should serve as post-hoc evaluation tools, with future work targeting gaming-robust rewards and broader logic types.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "b0254835-11f6-4118-aaac-b8a099164275",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL optimization (\\S\\ref{sec:diagnostic}).\nRepurposed as a training signal, ISR exhibits Goodhart effects~\\citep{manheim-goodhart-taxonomy}: across four dose levels ($\\beta\\in\\{0.05, 0.1, 0.2, 0.3\\}$), gaming dominates at every $\\beta$---amplifying H7 tautological collapse ${\\sim}5\\times$ at $\\beta{=}0.1$ ($70.6\\%$ vs.\\ $13.7\\%$ random, $p{<}10^{-39}$), with the sole apparent ISR gain vanishing ($1.06\\times$) after controlling for premise count.\nThe effect is consistent across logic types: Prolog yields 0\\% non-hacking in 3/3 seeds via distinct mechanisms including query-as-fact gaming that bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\nISR semantics are objective-dependent: exec-only \\emph{low} ISR signals redundancy; ISR-rewarded \\emph{high} ISR signals metric gaming.\n\n\\paragraph{Dose-response pattern.}\nThe relationship between $\\beta$ and failure mode is structured across four dose levels: $\\beta{=}0.05$ already produces 100\\% H7 gaming (single seed), $\\beta{=}0.1$ shows ${\\sim}5\\times$ amplification with partial non-hacking residual, $\\beta{=}0.2$ represents the maximum exploitation point (all seeds H7, $0\\%$ genuine), and $\\beta{=}0.3$ exceeds the training stability boundary with diverse failure modes.\nH7 tautological collapse is an absorbing state: once discovered as the global ISR-maximizing exploit, genuine output drops to zero regardless of $\\beta$.\n\n\\paragraph{Classifier blind spots.}\nH7b (obfuscated tautology) and Prolog query-as-fact gaming demonstrate that text-match classifiers have systematic blind spots exploitable by optimization.\nIn both cases, functional LOO analysis exposed gaming invisible to surface-level detection---H7b via vacuous quantifier wrapping ($10/12$ at $\\text{ISR}{\\geq}0.83$, triple gaming of execution, ISR, and classifier), query-as-fact via $95/97$ tautological samples the strict classifier labeled non-hacking (\\S\\ref{sec:crosslogic}).\nH9 (contradiction injection, \\S\\ref{sec:crossscale}) extends this pattern further: contradictory premises register as individually necessary under LOO, bypassing both text-match and functional $n_{\\text{necessary}}$ classifiers---detection requires logic-level consistency checking.\nThese cases collectively argue for mandatory functional cross-validation of text-based hacking classifiers, complemented by logic-level checks for novel exploit classes.\n\n\\paragraph{Hacking mode switching.}\nUnder identical reward configurations, different seeds converge to qualitatively different modes (Table~\\ref{tab:fol-detailed}): random $\\beta{=}0.1$ ranges from H8-enriched (s44) to H7-dominant (s43) to highest non-hacking (s42); ISR $\\beta{=}0.1$ similarly switches between H1-heavy (s42) and near-pure H7 (s43/s44, ${\\geq}97\\%$).\nSingle-seed results can therefore misrepresent a reward configuration's hacking profile; multi-seed evaluation with per-mode reporting should be standard.\n\nThe asymmetry---reliable observer, unreliable optimizer---may generalize to other perturbation-based diagnostics; ISR and similar metrics should serve as post-hoc evaluation tools, with future work targeting gaming-robust rewards and broader logic types.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

H9 is already fully integrated across all paper files:

- **abstract.tex**: "9 hacking modes" (line 7), "qualitatively novel gaming mode" (line 6)
- **introduction.tex**: "nine-mode hacking taxonomy including...scale-specific *ex falso* mode" (line 32)
- **method.tex**: "nine structural-degeneration modes" (line 79), H9 definition (line 90)
- **experiments.tex**: Full cross-scale section with H9 (lines 141-151), H9 row in Table 2 (line 174), "nine modes" (line 188)
- **appendix.tex**: "nine distinct reward hacking modes" (line 134), full H9 subsection with definition/example/ISR interaction/prevalence (lines 387-411)
- **conclusion.tex**: H9 classifier discussion (line 16)

No residual references to "8 modes" or "H1-H8" remain. The H9 content is already present and consistent throughout the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "uuid": "b0f12a44-ab7d-4d16-ac44-8533d4bb2662",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mtr8Mm2vu54GWBU5XkAcGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3579,
      "cache_read_input_tokens": 54096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3579
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

_source line 26_

H9 is already fully integrated across all paper files:

- **abstract.tex**: "9 hacking modes" (line 7), "qualitatively novel gaming mode" (line 6)
- **introduction.tex**: "nine-mode hacking taxonomy including...scale-specific *ex falso* mode" (line 32)
- **method.tex**: "nine structural-degeneration modes" (line 79), H9 definition (line 90)
- **experiments.tex**: Full cross-scale section with H9 (lines 141-151), H9 row in Table 2 (line 174), "nine modes" (line 188)
- **appendix.tex**: "nine distinct reward hacking modes" (line 134), full H9 subsection with definition/example/ISR interaction/prevalence (lines 387-411)
- **conclusion.tex**: H9 classifier discussion (line 16)

No residual references to "8 modes" or "H1-H8" remain. The H9 content is already present and consistent throughout the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 35716,
  "duration_api_ms": 36844,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "9b997335-a6fc-43c4-a71f-243a904a25d1",
  "total_cost_usd": 0.4058435,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 45834,
    "cache_read_input_tokens": 144718,
    "output_tokens": 1740,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 45834,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 251,
        "cache_read_input_tokens": 54096,
        "cache_creation_input_tokens": 3579,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3579
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3372,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003492,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 1740,
      "cacheReadInputTokens": 144718,
      "cacheCreationInputTokens": 45834,
      "webSearchRequests": 0,
      "costUSD": 0.4023515,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8d2b80da-ec5a-4b93-9ec2-470d295b30cc"
}
```

</details>

---
