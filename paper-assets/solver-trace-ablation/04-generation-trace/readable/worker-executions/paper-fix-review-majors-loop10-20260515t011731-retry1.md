# paper fix review majors loop10 20260515T011731 retry1

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_fix-review-majors-loop10_20260515T011731_retry1.log`
- **Structured JSON:** [`152da646b68ae1d42b04.json`](../../sessions/15/152da646b68ae1d42b04.json)

## Before a recorded user message

22 recorded events

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
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
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
  "uuid": "06561603-454c-465f-ad6e-c984fdcdcd85",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778821800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1fe4afd6-4dae-4c5d-b928-3ce915dbc915",
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a"
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
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "4329818d-8600-42e8-b1e1-67b94b393125",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0118seg2Ss6h42zUz8QWuYt3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16557,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16557
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

<details open><summary>🔧 Tool call — Bash · `toolu_016WACtysSMwoVyBrPigwpPx`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "d7a7701a-0fa5-4696-a5da-0fb5698ea241",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0118seg2Ss6h42zUz8QWuYt3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16557,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16557
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

_source line 6 · 2026-05-15T01:17:48.069Z_

<details><summary>↩ Tool result · `toolu_016WACtysSMwoVyBrPigwpPx`</summary>

```text
_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
conclusion.tex
experiments.tex
figures
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "596c0261-5f99-499e-adeb-0ae487367fdc",
  "tool_use_result": {
    "stdout": "_pdf_images\nabstract.tex\nacl.sty\nacl_natbib.bst\nappendix.tex\nconclusion.tex\nexperiments.tex\nfigures\nintroduction.tex\nlimitations.tex\nmain.aux\nmain.bbl\nmain.blg\nmain.log\nmain.out\nmain.pdf\nmain.tex\nmethod.tex\nreferences.bib\nrelated_work.tex",
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

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01MFjrEjQdVdvdsPYYJH6MxT`</summary>

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
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "0b5b0131-a345-4797-b568-c754a20b6a25",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01GaoUkF96kmT4DZ7o7gMTAS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 306,
      "cache_read_input_tokens": 32798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 306
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

### Tool result

_source line 8 · 2026-05-15T01:17:52.907Z_

<details><summary>↩ Tool result · `toolu_01MFjrEjQdVdvdsPYYJH6MxT`</summary>

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
25	Rollouts per prompt ($K$) & 8 \\
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
60	Algorithm~\ref{alg:sta} gives the full procedure for computing ISR over a proved formalization.
61	
62	\begin{algorithm}[h]
63	\caption{Solver Trace Ablation (STA)}
64	\label{alg:sta}
65	\begin{algorithmic}[1]
66	\REQUIRE Formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
67	\ENSURE ISR score $\in [0,1]$ or $\bot$ (undefined)
68	\IF{$S(x) \neq \textit{proved}$}
69	  \RETURN $\bot$
70	\ENDIF
71	\STATE $n_{\text{nec}} \gets 0$
72	\FOR{$i = 1$ \TO $n$}
73	  \STATE $x' \gets x \setminus \{c_i\}$
74	  \IF{$S(x') = \textit{failed}$}
75	    \STATE $n_{\text{nec}} \gets n_{\text{nec}} + 1$
76	  \ENDIF
77	\ENDFOR
78	\RETURN $n_{\text{nec}} \mathbin{/} n$
79	\end{algorithmic}
80	\end{algorithm}
81	
82	
83	\section{Extended Discussion}
84	\label{app:extended-discussion}
85	
86	\paragraph{What ISR measures---and what it does not.}
87	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
88	This is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.
89	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
90	ISR and downstream task performance are uncorrelated.
91	ISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
92	
93	Critically, low ISR carries different semantics depending on the training objective.
94	Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\S\ref{sec:crosslogic}).
95	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
96	ISR values must always be interpreted relative to the optimization objective that produced them.
97	
98	\paragraph{The premise-count confound.}
99	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
100	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.
101	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
102	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:beta01-3seed}).
103	This bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
104	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
105	
106	\paragraph{Meta-level Goodhart: implications.}
107	The meta-Goodhart finding extends beyond this specific system.
108	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.
109	The dose-response pattern ($\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.3$: PR collapse to 18\% vs.\ 48\% random) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.
110	$\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.
111	The practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.
112	
113	\paragraph{Single-seed unreliability.}
114	The three exec-only seeds diverge radically (PR $\sigma{=}\pm 47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
115	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
116	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
117	
118	
119	\section{Hacking Mode Definitions}
120	\label{app:hacking-modes}
121	
122	We identify seven distinct reward hacking modes across all experiments.
123	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
124	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
125	
126	\begin{table}[h]
127	\centering
128	\small
129	\resizebox{\columnwidth}{!}{%
130	\begin{tabular}{@{}llcccc@{}}
131	\toprule
132	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
133	\midrule
134	H1 & Concl.\ in premises & 87 & 17 & 81 & 7 \\
135	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{65} & 0 & 0 \\
136	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
137	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
138	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
139	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
140	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
141	\bottomrule
142	\end{tabular}}
143	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed means. Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-crosslogic}).}
144	\label{tab:hacking-taxonomy-app}
145	\end{table}
146	
147	\paragraph{Classifier Validation.}
148	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
149	H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
150	No training data or manual annotation is used for classification.
151	
152	To estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
153	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
154	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
155	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
156	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
157	
158	\subsection{H1 --- Conclusion Embedding}
159	
160	\paragraph{Definition.}
161	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
162	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
163	
164	\paragraph{Example (FOL).}
165	{\small\begin{verbatim}
166	Premises:
167	  all x (bird(x) -> flies(x)).
168	  bird(tweety).
169	  flies(tweety).  % conclusion embedded
170	Conclusion: flies(tweety).
171	\end{verbatim}}
172	
173	\paragraph{ISR interaction.}
174	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
175	ISR does not distinguish trivial from substantive necessity.
176	
177	\paragraph{Prevalence.}
178	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\% across all RL conditions.
179	Under exec-only and Random reward, it manifests as H1 (71--93\%); under ISR reward, it shifts to H7 (64.5\% pooled).
180	
181	
182	\subsection{H7 --- Conclusion Duplication}
183	
184	\paragraph{Definition.}
185	The entire formalization collapses to a single premise whose content is identical to the conclusion.
186	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
187	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
188	
189	\paragraph{Example (FOL).}
190	{\small\begin{verbatim}
191	Premises:
192	  all x ((A(x)&B(x))->(C(x)|D(x))).
193	Conclusion:
194	  all x ((A(x)&B(x))->(C(x)|D(x))).
195	\end{verbatim}}
196	
197	\paragraph{ISR interaction.}
198	ISR~$\approx 0.8$--$1.0$.
199	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
200	H7 is the only mode that simultaneously games both exec reward and ISR reward.
201	
202	\paragraph{Prevalence.}
203	ISR-specific: 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
204	\textbf{Zero} occurrences under Random~$\beta{=}0.1$ across all three seeds ($0/256$).
205	
206	
207	\subsection{Tautological Collapse}
208	
209	\paragraph{Definition.}
210	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
211	
212	\paragraph{Example (FOL).}
213	\begin{verbatim}
214	Premises: p(a).
215	Conclusion: p(a).
216	\end{verbatim}
217	
218	\paragraph{ISR interaction.}
219	ISR~$=1.0$ (the sole premise is necessary).
220	Distinguished from H7 by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
221	
222	\paragraph{Prevalence.}
223	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
224	Also observed in Prolog exec+STA seed~42 (100\% H7, PR~$=0.50$).
225	
226	
227	\subsection{Repetition Collapse}
228	
229	\paragraph{Definition.}
230	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
231	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
232	
233	\paragraph{Example (Prolog).}
234	\begin{verbatim}
235	penguin(fido).
236	penguin(fido).
237	penguin(fido).
238	... (repeated to 512 tokens)
239	query(penguin(fido)).
240	\end{verbatim}
241	
242	\paragraph{ISR interaction.}
243	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
244	ISR correctly diagnoses this degeneration.
245	
246	\paragraph{Prevalence.}
247	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=14$\%, ISR~$=0$).
248	
249	
250	\subsection{Complexity-without-Utility}
251	
252	\paragraph{Definition.}
253	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.
254	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
255	
256	\paragraph{Example (FOL).}
257	{\small\begin{verbatim}
258	Premises:
259	  all x all y (R(x,y) ->
260	    exists z (S(x,z) & T(z,y))).
261	  all x (P(x) -> Q(x)).
262	  P(a).            % only this needed
263	Conclusion: Q(a).
264	\end{verbatim}}
265	
266	\paragraph{ISR interaction.}
267	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
268	This is the mode ISR is best calibrated for.
269	
270	\paragraph{Prevalence.}
271	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
272	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
273	
274	
275	\subsection{Contradiction Explosion}
276	
277	\paragraph{Definition.}
278	The component count grows unboundedly over training.
279	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
280	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
281	
282	\paragraph{Example (FOL, 1000-step exec-only).}
283	{\small\begin{verbatim}
284	Premises:
285	  c1. c2. c3. ... c18. % 18.55 mean
286	  % conclusion embedded among premises
287	Conclusion: Q(a).
288	\end{verbatim}}
289	
290	\paragraph{ISR interaction.}
291	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
292	
293	\paragraph{Prevalence.}
294	Observed in extended exec-only training (seed~42, 1000 steps).
295	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
296	
297	
298	\subsection{Query-as-Fact Gaming}
299	
300	\paragraph{Definition.}
301	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
302	Prolog trivially proves the query by unifying with the fact.
303	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
304	
305	\paragraph{Example (Prolog).}
306	\begin{verbatim}
307	% NL: "Fido is happy."
308	% Model output:
309	fido_is_happy.
310	:- fido_is_happy.     % query = fact
311	\end{verbatim}
312	
313	\paragraph{ISR interaction.}
314	ISR~$\approx 0.9$--$1.0$.
315	The fact is necessarily necessary (its removal breaks the query), inflating ISR.
316	Functionally equivalent to H7 but with a distinct surface mechanism.
317	
318	\paragraph{Prevalence.}
319	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
320	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
321	
322	
323	\section{Per-Seed Detailed Results}
324	\label{app:detailed-results}
325	
326	Tables~\ref{tab:beta01-3seed} and \ref{tab:prolog-crosslogic} report full per-seed results.
327	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
328	ISR values are proved-only ISR$^*$.
329	
330	\begin{table*}[t]
331	\centering
332	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$).}
333	\label{tab:fol-detailed}
334	\label{tab:beta01-3seed}
335	\footnotesize
336	\setlength{\tabcolsep}{3pt}
337	\begin{tabular}{@{}llccccccl@{}}
338	\toprule
339	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
340	\midrule
341	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
342	Base model (no training)
343	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
344	Ground-truth FOL
345	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
346	SFT
347	  & 42 & ${\sim}$8 ep. & 0.14 & 0.571 & 0 & 7.1 & \textbf{92.9} & Supervised, no RL \\
348	\midrule
349	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
350	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
351	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 12.9 & \\
352	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
353	  & 43 & 500 & 0.14 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Sampling $T{=}0.7$ \\
354	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
355	\cmidrule(l){2-9}
356	  & \multicolumn{2}{l}{3-seed mean$\pm$std$^\dagger$} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step only \\
357	\midrule
358	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
359	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{30.9} & Mixed H1+H7 \\
360	  & 43 & 500 & 0.61 & 0.830 & \textbf{96.7} & 0 & ${\sim}$3 & H7 dominant \\
361	  & 44 & 500 & 0.89 & 0.902 & 86.5 & 0 & ${\sim}$13.5 & H7 dominant \\
362	\cmidrule(l){2-9}
363	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
364	\midrule
365	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
366	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\
367	\midrule
368	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
369	  & 42 & 500 & 0.79 & 0.131 & 0 & 70.9 & 29.1 & \\
370	  & 43 & 500 & 0.88 & 0.058 & 0 & 93.2 & 6.8 & \\
371	  & 44 & 500 & 0.89 & 0.070 & 0 & 79.8 & 20.2 & \\
372	\cmidrule(l){2-9}
373	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.85{\pm}0.06$} & & \makebox[0pt][l]{$0.086{\pm}0.039$} & & & H7 = 0\% all seeds \\
374	\midrule
375	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
376	  & 42 & 500 & 0.48 & 0.094 & --- & --- & --- & $n_{\text{comp}} = 9.6$ \\
377	\bottomrule
378	\end{tabular}
379	\end{table*}
380	
381	
382	\begin{table*}[t]
383	\centering
384	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
385	\label{tab:prolog-crosslogic}
386	\small
387	\begin{tabular}{@{}llcccccl@{}}
388	\toprule
389	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
390	\midrule
391	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
392	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
393	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
394	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
395	\cmidrule(l){2-8}
396	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
397	\midrule
398	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
399	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
400	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
401	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
402	\cmidrule(l){2-8}
403	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.699{\pm}0.45$} & & 3/3 Goodhart, 0\% non-hacking \\
404	\bottomrule
405	\end{tabular}
406	
407	\vspace{4pt}
408	{\footnotesize
409	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
410	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\
411	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
412	}
413	\end{table*}
414	
415	\begin{figure}[t]
416	\centering
417	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
418	\caption{Prolog cross-logic comparison. Exec-only vs Exec+ISR (STA reward) across three seeds, illustrating universal Goodhart under ISR-as-reward (3/3 seeds, 0\% non-hacking) and three distinct gaming pathways (H7 tautological, uppercase pseudo-Prolog, query-as-fact).}
419	\label{fig:prolog-comparison}
420	\end{figure}
421	
422	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
423	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
424	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
425	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
426	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
427	
428	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
429	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
430	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
431	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
432	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
433	The diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
434	
435	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
436	\label{app:100step}
437	
438	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%---higher than SFT (14\%) but still early in training.
439	Of the 32 proved samples, 9 (28.1\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
440	By contrast, SFT at comparable or lower PR shows 7.1\% hacking (1/14 proved samples).
441	This demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.
442	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.1\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
443	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "1031db05-d097-4168-b3e8-a5f2c5fcf8ab",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 8 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} gives the full procedure for computing ISR over a proved formalization.\n\n\\begin{algorithm}[h]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE ISR score $\\in [0,1]$ or $\\bot$ (undefined)\n\\IF{$S(x) \\neq \\textit{proved}$}\n  \\RETURN $\\bot$\n\\ENDIF\n\\STATE $n_{\\text{nec}} \\gets 0$\n\\FOR{$i = 1$ \\TO $n$}\n  \\STATE $x' \\gets x \\setminus \\{c_i\\}$\n  \\IF{$S(x') = \\textit{failed}$}\n    \\STATE $n_{\\text{nec}} \\gets n_{\\text{nec}} + 1$\n  \\ENDIF\n\\ENDFOR\n\\RETURN $n_{\\text{nec}} \\mathbin{/} n$\n\\end{algorithmic}\n\\end{algorithm}\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:beta01-3seed}).\nThis bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\paragraph{Meta-level Goodhart: implications.}\nThe meta-Goodhart finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\\beta{=}0.3$: PR collapse to 18\\% vs.\\ 48\\% random) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.\n$\\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.\nThe practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}\\pm 47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify seven distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ in premises & 87 & 17 & 81 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{65} & 0 & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed means. Exec: H1${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-crosslogic}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nH1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\n\\subsection{H1 --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as H1 (71--93\\%); under ISR reward, it shifts to H7 (64.5\\% pooled).\n\n\n\\subsection{H7 --- Conclusion Duplication}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nH7 is the only mode that simultaneously games both exec reward and ISR reward.\n\n\\paragraph{Prevalence.}\nISR-specific: 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\n\\textbf{Zero} occurrences under Random~$\\beta{=}0.1$ across all three seeds ($0/256$).\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from H7 by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% H7 by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% H7, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=14$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe fact is necessarily necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to H7 but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:beta01-3seed} and \\ref{tab:prolog-crosslogic} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$).}\n\\label{tab:fol-detailed}\n\\label{tab:beta01-3seed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & ${\\sim}$8 ep. & 0.14 & 0.571 & 0 & 7.1 & \\textbf{92.9} & Supervised, no RL \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 12.9 & \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.14 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Sampling $T{=}0.7$ \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std$^\\dagger$} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step only \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{30.9} & Mixed H1+H7 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{96.7} & 0 & ${\\sim}$3 & H7 dominant \\\\\n  & 44 & 500 & 0.89 & 0.902 & 86.5 & 0 & ${\\sim}$13.5 & H7 dominant \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 70.9 & 29.1 & \\\\\n  & 43 & 500 & 0.88 & 0.058 & 0 & 93.2 & 6.8 & \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 79.8 & 20.2 & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.85{\\pm}0.06$} & & \\makebox[0pt][l]{$0.086{\\pm}0.039$} & & & H7 = 0\\% all seeds \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & --- & --- & --- & $n_{\\text{comp}} = 9.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-crosslogic}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.53{\\pm}0.31$} & & \\makebox[0pt][l]{$0.146{\\pm}0.21$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & H7 tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional H7$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.62{\\pm}0.31$} & & \\makebox[0pt][l]{$0.699{\\pm}0.45$} & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict H7 classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Prolog cross-logic comparison. Exec-only vs Exec+ISR (STA reward) across three seeds, illustrating universal Goodhart under ISR-as-reward (3/3 seeds, 0\\% non-hacking) and three distinct gaming pathways (H7 tautological, uppercase pseudo-Prolog, query-as-fact).}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean H7 tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%---higher than SFT (14\\%) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.1\\% hacking (1/14 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.1\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n",
      "numLines": 443,
      "startLine": 1,
      "totalLines": 443
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01ETCEVMcJ4WrBuvD1ssQRAU`</summary>

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
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "ee7ae4f5-db7e-4597-9dc4-ea9eef35390c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SGFKFcWWt5ttNwRSmJfQdE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11938,
      "cache_read_input_tokens": 33104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11938
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

_source line 10 · 2026-05-15T01:17:56.801Z_

<details><summary>↩ Tool result · `toolu_01ETCEVMcJ4WrBuvD1ssQRAU`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}); and as a cross-logic protocol (\S\ref{sec:crosslogic}). We synthesize results into a hacking taxonomy (\S\ref{sec:taxonomy}).
5	
6	\subsection{Setup}\label{sec:setup}
7	
8	We train Qwen3-4B with GRPO~\citep{deepseekmath} ($K{=}8$ rollouts, 500 steps default, 1000 where noted) across seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across conditions. %% data: C001
9	Evaluation uses 100 held-out examples with greedy decoding; cross-run ISR values are computed uniformly by \texttt{eval\_sta.py}. %% C004
10	We report PR, proved-only ISR (ISR$^*$), hacking rates (H7, H1\footnote{H1/H7 numbering follows our taxonomy (Appendix~\ref{app:hacking-modes}).}), and non-hacking rate.\footnote{Non-hacking: not matching any of seven identified patterns (Table~\ref{tab:hacking-taxonomy-app}); does not imply semantic correctness.}
11	Full hyperparameters in Appendix~\ref{app:setup}.
12	
13	\subsection{ISR as Diagnostic}
14	\label{sec:diagnostic}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
19	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$96\% while proved-only ISR falls 0.642$\to$0.003 over 1000 steps. By step 1000, 94.8\% of proved samples have ISR${=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
20	\label{fig:isr-collapse}
21	\end{figure}
22	
23	\textbf{Collapse trajectory.}
24	Figure~\ref{fig:isr-collapse} traces exec-only GRPO (seed~42): PR rises 32\%$\to$93\%$\to$96\% while ISR$^*$ falls $0.642{\to}0.132{\to}0.003$ over 1000 steps. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
25	By step 500, 87.1\% of proved samples embed the conclusion (H1); by 1000, H1${=}100$\% with mean 18.55 components.
26	The monotonic ISR$^*$ decline shows extended training worsens structural degeneration invisible to PR.
27	
28	\textbf{Cross-seed instability.}
29	The three exec-only seeds diverge radically: s42 hacks via H1 (PR${=}93$\%, H1${=}87.1$\%); s43 collapses to PR${=}13$\% via repetition (87\% hit max length); s44 reaches PR${=}98$\% via tautological collapse (H7${=}100$\%). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
30	Despite PR$\in[13,98]$\%, all three exhibit structural degeneration detectable by ISR; the $\sigma{=}\pm47$\,pp cross-seed variance shows aggregate metrics obscure qualitatively different failure modes (per-seed: Table~\ref{tab:beta01-3seed}).
31	
32	\textbf{SFT baseline.}
33	SFT achieves PR${=}14$\% with ISR$^*{=}0.571$: 92.9\% non-hacking, only 1/14 exhibits H1, zero H7. %% registry: plan009-sft-baseline-s42-r4
34	The near-absence of hacking is consistent with hacking being RL-specific; a 100-step RL checkpoint analysis controlling for the PR-level confound is in Appendix~\ref{app:100step}.
35	
36	\subsection{Meta-Level Goodhart's Law}
37	\label{sec:goodhart}
38	
39	ISR-as-reward provides the first empirical demonstration of Goodhart's Law at the meta level~\citep{manheim-goodhart-taxonomy}: the diagnostic itself becomes the target of gaming when optimized.
40	
41	\begin{table}[t]
42	\centering
43	\small
44	\resizebox{\columnwidth}{!}{%
45	\begin{tabular}{lcccccc}
46	\toprule
47	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} \\
48	\midrule
49	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
50	SFT & --- & 14 & 0.571 & 0 & 7 & \textbf{93} \\ %% registry: plan009-sft-baseline-s42-r4
51	\midrule
52	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 13 \\ %% registry: plan001-exec-only-s42-r2
53	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{65} & 17 & ${\sim}$16 \\ %% registry: plan002-additive-b01-s42/s43/s44
54	Random & 0.1 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.04} & 0 & 81 & 19 \\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44
55	\midrule
56	ISR & 0.3 & 18 & 0.143 & --- & --- & --- \\ %% registry: plan002-additive-b03-s42
57	Random & 0.3 & 48$^\S$ & 0.094$^\S$ & --- & --- & --- \\ %% registry: plan017-additive-random-s42 (s44 pending rerun)
58	\bottomrule
59	\end{tabular}}
60	\caption{Goodhart landscape across reward conditions. 3-seed rows show mean$\pm$std. $^\dagger$Seed~42; see \S\ref{sec:diagnostic} for 3-seed divergence. $\ddagger$ISR$^*$ omitted: inflated by H7 gaming (Appendix Table~\ref{tab:beta01-3seed}). $^\S$Random $\beta{=}0.3$: seed~42 only (s44 pending rerun). H7 and H1 rates are simple means across available seeds. Best PR and N-H\% bolded per group.}
61	\label{tab:goodhart-landscape}
62	\end{table}
63	
64	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-specific gaming.}
65	Table~\ref{tab:goodhart-landscape} summarizes results.
66	At $\beta{=}0.1$, 2/3 ISR seeds are dominated by H7 (64.5\% of proved samples, 149/231) vs.\ zero H7 under random controls (0/256), confirming H7 is exclusively ISR-induced. %% registry: plan002-additive-b01-s42/s43/s44 vs plan018-additive-random-b01-s42/s43-r2/s44
67	Conclusion embedding (H1+H7) is GRPO-universal at 68--97\%: random produces only H1, while ISR converts H1$\to$H7 without reducing the total (Figure~\ref{fig:hacking-composition}; per-seed: Appendix Table~\ref{tab:beta01-3seed}).
68	Random also achieves higher and more stable PR (85$\pm$6\% vs 77$\pm$14\%). %% registry: plan018 vs plan002 3-seed means
69	
70	\textbf{Premise-count confound.}
71	The only ISR seed not dominated by H7 (s42) shows higher raw ISR$^*$ (0.415 vs 0.131), but this is entirely a premise-minimization artifact: ISR-trained models produce shorter formalizations (5.58 vs 8.46 components), biasing LOO upward. %% registry: plan002-additive-b01-s42, plan018-additive-random-b01-s42
72	Restricting to non-hacking samples with $\geq$3 premises: ISR$^*{=}0.258$ ($n{=}11$) vs random ISR$^*{=}0.243$ ($n{=}21$)---a 1.06$\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis
73	
74	\textbf{High-dose ISR ($\beta{=}0.3$): classic Goodhart.}
75	At $\beta{=}0.3$, ISR causes PR collapse to 18\% (vs.\ 48\% random), completing the Goodhart trajectory: low-dose gaming ($\beta{=}0.1$) gives way to high-dose collapse~\cite{gao-reward-overoptimization}. %% registry: plan002-additive-b03-s42, plan017-additive-random-s42
76	
77	\subsection{Cross-Logic Diagnostic Transfer}
78	\label{sec:crosslogic}
79	
80	Replication in Prolog/SWI-Prolog confirms diagnostic transfer (full results: Appendix Table~\ref{tab:prolog-crosslogic}).
81	Exec-only: 2/3 seeds show ISR$^*{\approx}0$ despite moderate-high PR, reflecting \emph{redundant coding} (repeated ground facts), not absent reasoning. %% registry: plan006-prolog-exec-s42 (ISR*=0.037), plan006-prolog-exec-s43-r3 (ISR*=0.015), plan006-prolog-exec-s44 (ISR*=0.387, small-sample n=21); C006
82	ISR-as-reward yields 0\% non-hacking across 185 proved samples via three distinct mechanisms: s42 H7 tautologies (ISR$^*{=}1.0$); s43 uppercase pseudo-Prolog functionally equivalent to H7; s44 query-as-fact gaming that bypasses text classifiers (Figure~\ref{fig:prolog-comparison}). %% registry: plan006-prolog-sta-s42, plan006-prolog-sta-s43, plan006-prolog-sta-s44
83	
84	\subsection{Hacking Taxonomy}
85	\label{sec:taxonomy}
86	
87	\begin{figure}[t]
88	\centering
89	\includegraphics[width=0.9\columnwidth]{figures/fig3_hacking_composition.pdf}
90	\caption{Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\% non-hacking).}
91	\label{fig:hacking-composition}
92	\end{figure}
93	
94	Seven modes span two logic types (definitions and breakdown in Appendix~\ref{app:hacking-modes}): \textbf{H1} (GRPO-universal, 68--97\%), \textbf{H7} (ISR-specific, 64.5\% vs.\ 0\% random), \textbf{tautological collapse} (exec-only s44), \textbf{repetition collapse} (exec-only s43), \textbf{contradiction explosion} (1000-step), \textbf{complexity-without-utility} (random $\beta{=}0.1$), and \textbf{query-as-fact} (Prolog ISR s44). %% registry: plan001-exec-only-s44, plan001-exec-only-s43-r4, plan016-extended-1000-s42, plan006-prolog-sta-s44
95	The reward signal determines hacking \emph{composition} but not \emph{prevalence}: ISR converts H1 into H7 without reducing totals (${\sim}82$\% pooled); SFT alone shows near-zero hacking (Figure~\ref{fig:hacking-composition}). %% registry: plan009-sft-baseline-s42-r4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "0ff26223-b099-43e3-8e8a-25af84e1eea1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); as a training reward exhibiting meta-level Goodhart's Law (\\S\\ref{sec:goodhart}); and as a cross-logic protocol (\\S\\ref{sec:crosslogic}). We synthesize results into a hacking taxonomy (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B with GRPO~\\citep{deepseekmath} ($K{=}8$ rollouts, 500 steps default, 1000 where noted) across seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across conditions. %% data: C001\nEvaluation uses 100 held-out examples with greedy decoding; cross-run ISR values are computed uniformly by \\texttt{eval\\_sta.py}. %% C004\nWe report PR, proved-only ISR (ISR$^*$), hacking rates (H7, H1\\footnote{H1/H7 numbering follows our taxonomy (Appendix~\\ref{app:hacking-modes}).}), and non-hacking rate.\\footnote{Non-hacking: not matching any of seven identified patterns (Table~\\ref{tab:hacking-taxonomy-app}); does not imply semantic correctness.}\nFull hyperparameters in Appendix~\\ref{app:setup}.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$96\\% while proved-only ISR falls 0.642$\\to$0.003 over 1000 steps. By step 1000, 94.8\\% of proved samples have ISR${=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42): PR rises 32\\%$\\to$93\\%$\\to$96\\% while ISR$^*$ falls $0.642{\\to}0.132{\\to}0.003$ over 1000 steps. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy step 500, 87.1\\% of proved samples embed the conclusion (H1); by 1000, H1${=}100$\\% with mean 18.55 components.\nThe monotonic ISR$^*$ decline shows extended training worsens structural degeneration invisible to PR.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge radically: s42 hacks via H1 (PR${=}93$\\%, H1${=}87.1$\\%); s43 collapses to PR${=}13$\\% via repetition (87\\% hit max length); s44 reaches PR${=}98$\\% via tautological collapse (H7${=}100$\\%). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nDespite PR$\\in[13,98]$\\%, all three exhibit structural degeneration detectable by ISR; the $\\sigma{=}\\pm47$\\,pp cross-seed variance shows aggregate metrics obscure qualitatively different failure modes (per-seed: Table~\\ref{tab:beta01-3seed}).\n\n\\textbf{SFT baseline.}\nSFT achieves PR${=}14$\\% with ISR$^*{=}0.571$: 92.9\\% non-hacking, only 1/14 exhibits H1, zero H7. %% registry: plan009-sft-baseline-s42-r4\nThe near-absence of hacking is consistent with hacking being RL-specific; a 100-step RL checkpoint analysis controlling for the PR-level confound is in Appendix~\\ref{app:100step}.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nISR-as-reward provides the first empirical demonstration of Goodhart's Law at the meta level~\\citep{manheim-goodhart-taxonomy}: the diagnostic itself becomes the target of gaming when optimized.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 14 & 0.571 & 0 & 7 & \\textbf{93} \\\\ %% registry: plan009-sft-baseline-s42-r4\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 13 \\\\ %% registry: plan001-exec-only-s42-r2\nISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{65} & 17 & ${\\sim}$16 \\\\ %% registry: plan002-additive-b01-s42/s43/s44\nRandom & 0.1 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.04} & 0 & 81 & 19 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44\n\\midrule\nISR & 0.3 & 18 & 0.143 & --- & --- & --- \\\\ %% registry: plan002-additive-b03-s42\nRandom & 0.3 & 48$^\\S$ & 0.094$^\\S$ & --- & --- & --- \\\\ %% registry: plan017-additive-random-s42 (s44 pending rerun)\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows show mean$\\pm$std. $^\\dagger$Seed~42; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR$^*$ omitted: inflated by H7 gaming (Appendix Table~\\ref{tab:beta01-3seed}). $^\\S$Random $\\beta{=}0.3$: seed~42 only (s44 pending rerun). H7 and H1 rates are simple means across available seeds. Best PR and N-H\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results.\nAt $\\beta{=}0.1$, 2/3 ISR seeds are dominated by H7 (64.5\\% of proved samples, 149/231) vs.\\ zero H7 under random controls (0/256), confirming H7 is exclusively ISR-induced. %% registry: plan002-additive-b01-s42/s43/s44 vs plan018-additive-random-b01-s42/s43-r2/s44\nConclusion embedding (H1+H7) is GRPO-universal at 68--97\\%: random produces only H1, while ISR converts H1$\\to$H7 without reducing the total (Figure~\\ref{fig:hacking-composition}; per-seed: Appendix Table~\\ref{tab:beta01-3seed}).\nRandom also achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%). %% registry: plan018 vs plan002 3-seed means\n\n\\textbf{Premise-count confound.}\nThe only ISR seed not dominated by H7 (s42) shows higher raw ISR$^*$ (0.415 vs 0.131), but this is entirely a premise-minimization artifact: ISR-trained models produce shorter formalizations (5.58 vs 8.46 components), biasing LOO upward. %% registry: plan002-additive-b01-s42, plan018-additive-random-b01-s42\nRestricting to non-hacking samples with $\\geq$3 premises: ISR$^*{=}0.258$ ($n{=}11$) vs random ISR$^*{=}0.243$ ($n{=}21$)---a 1.06$\\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR causes PR collapse to 18\\% (vs.\\ 48\\% random), completing the Goodhart trajectory: low-dose gaming ($\\beta{=}0.1$) gives way to high-dose collapse~\\cite{gao-reward-overoptimization}. %% registry: plan002-additive-b03-s42, plan017-additive-random-s42\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nReplication in Prolog/SWI-Prolog confirms diagnostic transfer (full results: Appendix Table~\\ref{tab:prolog-crosslogic}).\nExec-only: 2/3 seeds show ISR$^*{\\approx}0$ despite moderate-high PR, reflecting \\emph{redundant coding} (repeated ground facts), not absent reasoning. %% registry: plan006-prolog-exec-s42 (ISR*=0.037), plan006-prolog-exec-s43-r3 (ISR*=0.015), plan006-prolog-exec-s44 (ISR*=0.387, small-sample n=21); C006\nISR-as-reward yields 0\\% non-hacking across 185 proved samples via three distinct mechanisms: s42 H7 tautologies (ISR$^*{=}1.0$); s43 uppercase pseudo-Prolog functionally equivalent to H7; s44 query-as-fact gaming that bypasses text classifiers (Figure~\\ref{fig:prolog-comparison}). %% registry: plan006-prolog-sta-s42, plan006-prolog-sta-s43, plan006-prolog-sta-s44\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.9\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples). ISR converts H1 (conclusion embedding) into more extreme H7 (conclusion duplication) without reducing total hacking; SFT is near-zero hacking (92.9\\% non-hacking).}\n\\label{fig:hacking-composition}\n\\end{figure}\n\nSeven modes span two logic types (definitions and breakdown in Appendix~\\ref{app:hacking-modes}): \\textbf{H1} (GRPO-universal, 68--97\\%), \\textbf{H7} (ISR-specific, 64.5\\% vs.\\ 0\\% random), \\textbf{tautological collapse} (exec-only s44), \\textbf{repetition collapse} (exec-only s43), \\textbf{contradiction explosion} (1000-step), \\textbf{complexity-without-utility} (random $\\beta{=}0.1$), and \\textbf{query-as-fact} (Prolog ISR s44). %% registry: plan001-exec-only-s44, plan001-exec-only-s43-r4, plan016-extended-1000-s42, plan006-prolog-sta-s44\nThe reward signal determines hacking \\emph{composition} but not \\emph{prevalence}: ISR converts H1 into H7 without reducing totals (${\\sim}82$\\% pooled); SFT alone shows near-zero hacking (Figure~\\ref{fig:hacking-composition}). %% registry: plan009-sft-baseline-s42-r4",
      "numLines": 95,
      "startLine": 1,
      "totalLines": 95
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
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "b0f78e44-87c6-4ad3-9b9a-28d32e2807e8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XhToBxtWjyqpK9MXuEGw8M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4567,
      "cache_read_input_tokens": 45042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4567
      },
      "output_tokens": 46,
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

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01YRJSnxd3TsN79FiFRCtpS7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "a9dc8f2d-b44b-4379-96c1-d154c8c4d92e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XhToBxtWjyqpK9MXuEGw8M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4567,
      "cache_read_input_tokens": 45042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4567
      },
      "output_tokens": 46,
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

### Tool result

_source line 13 · 2026-05-15T01:18:23.451Z_

<details><summary>↩ Tool result · `toolu_01YRJSnxd3TsN79FiFRCtpS7`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic Reasoning with LLMs.}
5	Prompting-based pipelines couple LLMs with external solvers---SatLM~\cite{satlm}, Logic-LM~\cite{logic-lm}, LINC~\cite{linc}, LoRP~\cite{lorp}, FOVER~\cite{fover-pei2025}---but evaluate execution accuracy alone without diagnosing structural quality.
6	RL approaches train against solver feedback~\cite{mellgren-prolog-grpo, logic-rl, thought-like-pro}, optimizing prove rate with binary reward.
7	STA provides a diagnostic layer: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, suggesting prior prove-rate gains may overstate genuine reasoning.
8	We use FOLIO~\cite{folio}, the only public NLI benchmark with both FOL and Prolog annotations enabling cross-logic diagnostic transfer.
9	
10	\paragraph{Reward Shaping and Process Supervision.}
11	Learned PRMs~\cite{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from design-choice sensitivity~\cite{gao-effective-rl-reward} and distribution shift~\cite{processbench}; recent advances~\cite{thinkprm, versaprm, rprm} improve quality but remain learned and require curated supervision.
12	ISR is solver-grounded rather than learned, eliminating reward-model noise.
13	Yet our \S\ref{sec:goodhart} result shows that even non-learned, deterministic process signals Goodhart when optimized---suggesting the problem is fundamental to process-level reward shaping, not specific to learned models.
14	
15	\paragraph{Reward Hacking and Goodhart's Law.}
16	Goodhart's Law is established theoretically~\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\cite{gao-reward-overoptimization} and frontier models~\cite{metr-reward-hacking}; specification gaming~\cite{bondarenko-spec-gaming}, formalization gaming~\cite{kim-game-formalization}, and spurious rewards~\cite{spurious-rewards} have been documented, but the proxy is a learned reward model.
17	Kim et al.~\cite{kim-game-formalization} diagnose gaming in inference-time outputs of frontier models; we study gaming that \emph{emerges during RL training} with a systematic taxonomy and cross-logic analysis.
18	Our setting differs: ISR is deterministic and solver-derived, and the Goodhart effect operates at a \emph{meta} level---the diagnostic for gaming becomes gamed when optimized---a phenomenon not previously documented.
19	
20	\paragraph{Mutation Testing.}
21	STA adapts the LOO mutation paradigm~\cite{demillo1978, jia-harman-survey} from software testing to solver inputs.
22	The novelty lies in application and findings (ISR collapse, meta-Goodhart, hacking taxonomy), not in the perturbation technique itself.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "8992a8fb-0d6d-47df-8b8b-e4730e4677e0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic Reasoning with LLMs.}\nPrompting-based pipelines couple LLMs with external solvers---SatLM~\\cite{satlm}, Logic-LM~\\cite{logic-lm}, LINC~\\cite{linc}, LoRP~\\cite{lorp}, FOVER~\\cite{fover-pei2025}---but evaluate execution accuracy alone without diagnosing structural quality.\nRL approaches train against solver feedback~\\cite{mellgren-prolog-grpo, logic-rl, thought-like-pro}, optimizing prove rate with binary reward.\nSTA provides a diagnostic layer: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, suggesting prior prove-rate gains may overstate genuine reasoning.\nWe use FOLIO~\\cite{folio}, the only public NLI benchmark with both FOL and Prolog annotations enabling cross-logic diagnostic transfer.\n\n\\paragraph{Reward Shaping and Process Supervision.}\nLearned PRMs~\\cite{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from design-choice sensitivity~\\cite{gao-effective-rl-reward} and distribution shift~\\cite{processbench}; recent advances~\\cite{thinkprm, versaprm, rprm} improve quality but remain learned and require curated supervision.\nISR is solver-grounded rather than learned, eliminating reward-model noise.\nYet our \\S\\ref{sec:goodhart} result shows that even non-learned, deterministic process signals Goodhart when optimized---suggesting the problem is fundamental to process-level reward shaping, not specific to learned models.\n\n\\paragraph{Reward Hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\\cite{gao-reward-overoptimization} and frontier models~\\cite{metr-reward-hacking}; specification gaming~\\cite{bondarenko-spec-gaming}, formalization gaming~\\cite{kim-game-formalization}, and spurious rewards~\\cite{spurious-rewards} have been documented, but the proxy is a learned reward model.\nKim et al.~\\cite{kim-game-formalization} diagnose gaming in inference-time outputs of frontier models; we study gaming that \\emph{emerges during RL training} with a systematic taxonomy and cross-logic analysis.\nOur setting differs: ISR is deterministic and solver-derived, and the Goodhart effect operates at a \\emph{meta} level---the diagnostic for gaming becomes gamed when optimized---a phenomenon not previously documented.\n\n\\paragraph{Mutation Testing.}\nSTA adapts the LOO mutation paradigm~\\cite{demillo1978, jia-harman-survey} from software testing to solver inputs.\nThe novelty lies in application and findings (ISR collapse, meta-Goodhart, hacking taxonomy), not in the perturbation technique itself.\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_014nALHASp7L5aafpJbumca7`</summary>

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
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "323608a1-268a-48ee-a49d-00161006a76d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01J6Hr4u84JAtFRF3Sqj8Qw6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3328,
      "cache_read_input_tokens": 49609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3328
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

_source line 15 · 2026-05-15T01:18:26.166Z_

<details><summary>↩ Tool result · `toolu_014nALHASp7L5aafpJbumca7`</summary>

```text
1	\section{Discussion and Conclusion}
2	
3	We introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.
4	Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\S\ref{sec:diagnostic}).
5	When repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses (18\% vs.\ 48\% random); the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\S\ref{sec:goodhart}).
6	Both diagnostic utility and Goodhart vulnerability transfer to Prolog/SWI-Prolog: ISR-as-reward yields universal gaming across all seeds with zero non-hacking proofs, each via a distinct mechanism (\S\ref{sec:crosslogic}).
7	Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
8	
9	\paragraph{Interpreting ISR.}
10	ISR values must be read relative to the optimization objective: under exec-only Prolog, \emph{low} ISR reflects redundant coding, not absent reasoning; under ISR-as-reward, \emph{high} ISR reflects metric gaming.
11	The premise-count confound applies to any ablation-based diagnostic on variable-length outputs; Shapley values could provide more nuanced attribution at higher cost.
12	
13	\paragraph{Meta-Level Goodhart.}
14	ISR was designed to \emph{detect} reward gaming, yet becomes gamed itself when optimized---a regress where any diagnostic metric risks becoming a target.
15	The dose-response pattern ($\beta{=}0.1$: proxy gaming; $\beta{=}0.3$: collapse) maps onto~\cite{gao-reward-overoptimization} at a meta level.
16	ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools; the asymmetry (reliable observer, unreliable optimizer) may generalize to other perturbation-based quality metrics.
17	Open directions include reward functions robust to identified gaming modes and extending STA to broader logic types.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "3c287af3-dcc6-446e-b48f-49fe954c29e7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\nWe introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.\nApplied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\\S\\ref{sec:diagnostic}).\nWhen repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses (18\\% vs.\\ 48\\% random); the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\\S\\ref{sec:goodhart}).\nBoth diagnostic utility and Goodhart vulnerability transfer to Prolog/SWI-Prolog: ISR-as-reward yields universal gaming across all seeds with zero non-hacking proofs, each via a distinct mechanism (\\S\\ref{sec:crosslogic}).\nAcross six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\n\n\\paragraph{Interpreting ISR.}\nISR values must be read relative to the optimization objective: under exec-only Prolog, \\emph{low} ISR reflects redundant coding, not absent reasoning; under ISR-as-reward, \\emph{high} ISR reflects metric gaming.\nThe premise-count confound applies to any ablation-based diagnostic on variable-length outputs; Shapley values could provide more nuanced attribution at higher cost.\n\n\\paragraph{Meta-Level Goodhart.}\nISR was designed to \\emph{detect} reward gaming, yet becomes gamed itself when optimized---a regress where any diagnostic metric risks becoming a target.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming; $\\beta{=}0.3$: collapse) maps onto~\\cite{gao-reward-overoptimization} at a meta level.\nISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools; the asymmetry (reliable observer, unreliable optimizer) may generalize to other perturbation-based quality metrics.\nOpen directions include reward functions robust to identified gaming modes and extending STA to broader logic types.\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01PoZxzL9QPBGapxunDKKVHv`</summary>

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
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "19bf5a81-413d-4d36-a9ba-ab5bf8d8bdd7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VcMG5JqGBzXvTaZcYieZbg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 52937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1032
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

_source line 17 · 2026-05-15T01:18:28.877Z_

<details><summary>↩ Tool result · `toolu_01PoZxzL9QPBGapxunDKKVHv`</summary>

```text
1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
31	  archivePrefix = {arXiv},
32	  primaryClass = {cs.AI},
33	}
34	
35	@inproceedings{satlm,
36	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
37	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
38	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
39	  year         = {2023},
40	}
41	
42	@article{thought-like-pro,
43	  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},
44	  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},
45	  journal      = {arXiv preprint arXiv:2407.14562},
46	  year         = {2024},
47	  eprint       = {2407.14562},
48	  archivePrefix = {arXiv},
49	  primaryClass = {cs.AI},
50	}
51	
52	% ============================================================
53	% Category 2: Reward shaping for code/formal verification
54	% ============================================================
55	
56	@inproceedings{lightman-verify-step,
57	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
58	  title        = {{Let's Verify Step by Step}},
59	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
60	  year         = {2024},
61	  note         = {arXiv:2305.20050},
62	}
63	
64	@article{rubric-grpo,
65	  author       = {Manish Bhattarai and Ismael Boureima and Nishath Rajiv Ranasinghe and Scott Pakin and Dan O'Malley},
66	  title        = {{Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning}},
67	  journal      = {arXiv preprint arXiv:2605.08061},
68	  year         = {2026},
69	  eprint       = {2605.08061},
70	  archivePrefix = {arXiv},
71	  primaryClass = {cs.AI},
72	}
73	
74	@article{gao-effective-rl-reward,
75	  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},
76	  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},
77	  journal      = {arXiv preprint arXiv:2410.15115},
78	  year         = {2024},
79	  eprint       = {2410.15115},
80	  archivePrefix = {arXiv},
81	  primaryClass = {cs.AI},
82	}
83	
84	@article{prof-process-outcome,
85	  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},
86	  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},
87	  journal      = {arXiv preprint arXiv:2509.03403},
88	  year         = {2025},
89	  eprint       = {2509.03403},
90	  archivePrefix = {arXiv},
91	  primaryClass = {cs.AI},
92	}
93	
94	@inproceedings{skalse-reward-hacking,
95	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
96	  title        = {{Defining and Characterizing Reward Hacking}},
97	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
98	  year         = {2022},
99	  note         = {arXiv:2209.13085},
100	}
101	
102	@article{progrs-outcome-conditioned,
103	  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},
104	  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},
105	  journal      = {arXiv preprint arXiv:2604.02341},
106	  year         = {2026},
107	  eprint       = {2604.02341},
108	  archivePrefix = {arXiv},
109	  primaryClass = {cs.AI},
110	}
111	
112	@inproceedings{qwen-prm-lessons,
113	  author       = {Zhenru Zhang and others},
114	  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},
115	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
116	  year         = {2025},
117	  note         = {arXiv:2501.07301},
118	}
119	
120	% ============================================================
121	% Category 3: Mutation testing in software engineering
122	% ============================================================
123	
124	@article{demillo1978,
125	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
126	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
127	  journal      = {Computer},
128	  volume       = {11},
129	  number       = {4},
130	  pages        = {34--41},
131	  year         = {1978},
132	}
133	
134	@article{offutt-coupling,
135	  author       = {A. Jefferson Offutt},
136	  title        = {{Investigations of the Software Testing Coupling Effect}},
137	  journal      = {ACM Transactions on Software Engineering and Methodology},
138	  volume       = {1},
139	  number       = {1},
140	  pages        = {5--20},
141	  year         = {1992},
142	}
143	
144	@article{jia-harman-survey,
145	  author       = {Yue Jia and Mark Harman},
146	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
147	  journal      = {IEEE Transactions on Software Engineering},
148	  volume       = {37},
149	  number       = {5},
150	  pages        = {649--678},
151	  year         = {2011},
152	}
153	
154	@inproceedings{just-mutants-real-faults,
155	  author       = {Ren{\'e} Just and Darioush Jalali and Laura Inozemtseva and others},
156	  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},
157	  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},
158	  year         = {2014},
159	}
160	
161	@article{llmorpheus,
162	  author       = {Frank Tip and Jon Bell and others},
163	  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},
164	  journal      = {IEEE Transactions on Software Engineering},
165	  year         = {2025},
166	}
167	
168	@article{spurious-rewards,
169	  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},
170	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
171	  journal      = {arXiv preprint arXiv:2506.10947},
172	  year         = {2025},
173	  eprint       = {2506.10947},
174	  archivePrefix = {arXiv},
175	  primaryClass = {cs.AI},
176	}
177	
178	@article{bondarenko-spec-gaming,
179	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
180	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
181	  journal      = {arXiv preprint arXiv:2502.13295},
182	  year         = {2025},
183	  eprint       = {2502.13295},
184	  archivePrefix = {arXiv},
185	  primaryClass = {cs.AI},
186	}
187	
188	@inproceedings{kim-game-formalization,
189	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
190	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
191	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
192	  year         = {2026},
193	  note         = {arXiv:2604.19459},
194	}
195	
196	@inproceedings{gao-reward-overoptimization,
197	  author       = {Leo Gao and John Schulman and Jacob Hilton},
198	  title        = {{Scaling Laws for Reward Model Overoptimization}},
199	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
200	  year         = {2023},
201	  note         = {arXiv:2210.10760},
202	}
203	
204	@inproceedings{karwowski-goodhart-rl,
205	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
206	  title        = {{Goodhart's Law in Reinforcement Learning}},
207	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
208	  year         = {2024},
209	  note         = {arXiv:2310.09144},
210	}
211	
212	% ============================================================
213	% Category 6: FOL/Prolog formalization with LLMs
214	% ============================================================
215	
216	@inproceedings{folio,
217	  author       = {Simeng Han and others},
218	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
219	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
220	  year         = {2024},
221	  note         = {arXiv:2209.00840},
222	}
223	
224	@inproceedings{logic-lm,
225	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},
226	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
227	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
228	  year         = {2023},
229	}
230	
231	@inproceedings{linc,
232	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},
233	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
234	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
235	  year         = {2023},
236	}
237	
238	@article{fover-pei2025,
239	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
240	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
241	  journal      = {Transactions of the Association for Computational Linguistics},
242	  volume       = {13},
243	  pages        = {1340--1359},
244	  year         = {2025},
245	}
246	
247	@article{lorp,
248	  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},
249	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
250	  journal      = {Knowledge-Based Systems},
251	  year         = {2025},
252	}
253	
254	@article{manheim-goodhart-taxonomy,
255	  author       = {David Manheim and Scott Garrabrant},
256	  title        = {{Categorizing Variants of Goodhart's Law}},
257	  journal      = {arXiv preprint arXiv:1803.04585},
258	  year         = {2019},
259	  eprint       = {1803.04585},
260	  archivePrefix = {arXiv},
261	  primaryClass = {cs.AI},
262	}
263	
264	@inproceedings{pan-reward-misspecification,
265	  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},
266	  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},
267	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
268	  year         = {2022},
269	}
270	
271	@inproceedings{kwa-catastrophic-goodhart,
272	  author       = {Thomas Kwa and Drake Thomas and Adri{\`a} Garriga-Alonso},
273	  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},
274	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
275	  year         = {2024},
276	}
277	
278	@article{rlsf,
279	  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},
280	  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},
281	  journal      = {arXiv preprint arXiv:2405.16661},
282	  year         = {2024},
283	  eprint       = {2405.16661},
284	  archivePrefix = {arXiv},
285	  primaryClass = {cs.AI},
286	}
287	
288	@inproceedings{math-shepherd,
289	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},
290	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
291	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
292	  year         = {2024},
293	  note         = {arXiv:2312.08935},
294	}
295	
296	% ============================================================
297	% Additional reward-shaping papers
298	% ============================================================
299	
300	@article{reward-hacking-survey,
301	  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},
302	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
303	  journal      = {arXiv preprint arXiv:2604.13602},
304	  year         = {2026},
305	  eprint       = {2604.13602},
306	  archiveprefix = {arXiv},
307	}
308	
309	@article{thinkprm,
310	  author       = {Muhammad Khalifa and others},
311	  title        = {{Process Reward Models That Think}},
312	  journal      = {arXiv preprint arXiv:2504.16828},
313	  year         = {2025},
314	  eprint       = {2504.16828},
315	  archivePrefix = {arXiv},
316	  primaryClass = {cs.AI},
317	}
318	
319	@inproceedings{versaprm,
320	  author       = {Thomas Zeng and others},
321	  title        = {{VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data}},
322	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
323	  year         = {2025},
324	  note         = {arXiv:2502.06737},
325	}
326	
327	@inproceedings{rprm,
328	  author       = {Shuaijie She and Junxiao Liu and Yifeng Liu and Jiajun Chen and Xin Huang and Shujian Huang},
329	  title        = {{R-PRM: Reasoning-Driven Process Reward Modeling}},
330	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
331	  year         = {2025},
332	  note         = {arXiv:2503.21295},
333	}
334	
335	@inproceedings{proofwriter,
336	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
337	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
338	  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},
339	  year         = {2021},
340	  note         = {arXiv:2012.13048},
341	}
342	
343	@inproceedings{prontoqa,
344	  author       = {Abulhair Saparov and He He},
345	  title        = {{Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought}},
346	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
347	  year         = {2023},
348	  note         = {arXiv:2210.01240},
349	}
350	
351	@misc{metr-reward-hacking,
352	  author       = {{METR}},
353	  title        = {{Recent Frontier Models Are Reward Hacking}},
354	  year         = {2025},
355	  howpublished = {METR blog post},
356	  note         = {\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},
357	}
358	
359	@inproceedings{processbench,
360	  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},
361	  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},
362	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
363	  year         = {2025},
364	  note         = {arXiv:2412.06559},
365	}
366	
367	@article{school-reward-hacks,
368	  author       = {Mia Taylor and James Chua and Jan Betley and Johannes Treutlein and Owain Evans},
369	  title        = {{School of Reward Hacks: Hacking Harmless Tasks Generalizes to Misaligned Behavior in LLMs}},
370	  journal      = {arXiv preprint arXiv:2508.17511},
371	  year         = {2025},
372	  eprint       = {2508.17511},
373	  archivePrefix = {arXiv},
374	  primaryClass = {cs.AI},
375	}
376	
377	@article{macdiarmid-emergent-misalignment,
378	  author       = {Monte MacDiarmid and Benjamin Wright and Jonathan Uesato and Joe Benton and others},
379	  title        = {{Natural Emergent Misalignment from Reward Hacking in Production RL}},
380	  journal      = {arXiv preprint arXiv:2511.18397},
381	  year         = {2025},
382	  eprint       = {2511.18397},
383	  archivePrefix = {arXiv},
384	  primaryClass = {cs.AI},
385	}
386	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "2563fb47-6716-4795-9c10-bdbed8de101c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
      "content": "% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n@article{thought-like-pro,\n  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},\n  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},\n  journal      = {arXiv preprint arXiv:2407.14562},\n  year         = {2024},\n  eprint       = {2407.14562},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@article{rubric-grpo,\n  author       = {Manish Bhattarai and Ismael Boureima and Nishath Rajiv Ranasinghe and Scott Pakin and Dan O'Malley},\n  title        = {{Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning}},\n  journal      = {arXiv preprint arXiv:2605.08061},\n  year         = {2026},\n  eprint       = {2605.08061},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{prof-process-outcome,\n  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},\n  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},\n  journal      = {arXiv preprint arXiv:2509.03403},\n  year         = {2025},\n  eprint       = {2509.03403},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n@article{progrs-outcome-conditioned,\n  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},\n  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},\n  journal      = {arXiv preprint arXiv:2604.02341},\n  year         = {2026},\n  eprint       = {2604.02341},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{qwen-prm-lessons,\n  author       = {Zhenru Zhang and others},\n  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2501.07301},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--41},\n  year         = {1978},\n}\n\n@article{offutt-coupling,\n  author       = {A. Jefferson Offutt},\n  title        = {{Investigations of the Software Testing Coupling Effect}},\n  journal      = {ACM Transactions on Software Engineering and Methodology},\n  volume       = {1},\n  number       = {1},\n  pages        = {5--20},\n  year         = {1992},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@inproceedings{just-mutants-real-faults,\n  author       = {Ren{\\'e} Just and Darioush Jalali and Laura Inozemtseva and others},\n  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2014},\n}\n\n@article{llmorpheus,\n  author       = {Frank Tip and Jon Bell and others},\n  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},\n  journal      = {IEEE Transactions on Software Engineering},\n  year         = {2025},\n}\n\n@article{spurious-rewards,\n  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and others},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{pan-reward-misspecification,\n  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},\n  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2022},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Thomas Kwa and Drake Thomas and Adri{\\`a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@article{rlsf,\n  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},\n  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@article{reward-hacking-survey,\n  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archiveprefix = {arXiv},\n}\n\n@article{thinkprm,\n  author       = {Muhammad Khalifa and others},\n  title        = {{Process Reward Models That Think}},\n  journal      = {arXiv preprint arXiv:2504.16828},\n  year         = {2025},\n  eprint       = {2504.16828},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{versaprm,\n  author       = {Thomas Zeng and others},\n  title        = {{VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2025},\n  note         = {arXiv:2502.06737},\n}\n\n@inproceedings{rprm,\n  author       = {Shuaijie She and Junxiao Liu and Yifeng Liu and Jiajun Chen and Xin Huang and Shujian Huang},\n  title        = {{R-PRM: Reasoning-Driven Process Reward Modeling}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2025},\n  note         = {arXiv:2503.21295},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},\n  year         = {2021},\n  note         = {arXiv:2012.13048},\n}\n\n@inproceedings{prontoqa,\n  author       = {Abulhair Saparov and He He},\n  title        = {{Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2023},\n  note         = {arXiv:2210.01240},\n}\n\n@misc{metr-reward-hacking,\n  author       = {{METR}},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR blog post},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{school-reward-hacks,\n  author       = {Mia Taylor and James Chua and Jan Betley and Johannes Treutlein and Owain Evans},\n  title        = {{School of Reward Hacks: Hacking Harmless Tasks Generalizes to Misaligned Behavior in LLMs}},\n  journal      = {arXiv preprint arXiv:2508.17511},\n  year         = {2025},\n  eprint       = {2508.17511},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{macdiarmid-emergent-misalignment,\n  author       = {Monte MacDiarmid and Benjamin Wright and Jonathan Uesato and Joe Benton and others},\n  title        = {{Natural Emergent Misalignment from Reward Hacking in Production RL}},\n  journal      = {arXiv preprint arXiv:2511.18397},\n  year         = {2025},\n  eprint       = {2511.18397},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n",
      "numLines": 386,
      "startLine": 1,
      "totalLines": 386
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

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
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "dd6718c3-e151-4176-b53c-73f68b17236b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N4i9vDAf8ohC8Kx7gnhEcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7845,
      "cache_read_input_tokens": 53969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7845
      },
      "output_tokens": 50,
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

<details open><summary>🔧 Tool call — Grep · `toolu_01BzPFqfxh3pbxr2N3oe4kco`</summary>

```json
{
  "pattern": "\\\\cite[a-z]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
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
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "f76470f1-52e2-424b-9eba-3c83c6988754",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01N4i9vDAf8ohC8Kx7gnhEcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7845,
      "cache_read_input_tokens": 53969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7845
      },
      "output_tokens": 50,
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

_source line 20 · 2026-05-15T01:18:35.132Z_

<details><summary>↩ Tool result · `toolu_01BzPFqfxh3pbxr2N3oe4kco`</summary>

```text
paper/related_work.tex:5:Prompting-based pipelines couple LLMs with external solvers---SatLM~\cite{satlm}, Logic-LM~\cite{logic-lm}, LINC~\cite{linc}, LoRP~\cite{lorp}, FOVER~\cite{fover-pei2025}---but evaluate execution accuracy alone without diagnosing structural quality.
paper/related_work.tex:6:RL approaches train against solver feedback~\cite{mellgren-prolog-grpo, logic-rl, thought-like-pro}, optimizing prove rate with binary reward.
paper/related_work.tex:8:We use FOLIO~\cite{folio}, the only public NLI benchmark with both FOL and Prolog annotations enabling cross-logic diagnostic transfer.
paper/related_work.tex:11:Learned PRMs~\cite{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from design-choice sensitivity~\cite{gao-effective-rl-reward} and distribution shift~\cite{processbench}; recent advances~\cite{thinkprm, versaprm, rprm} improve quality but remain learned and require curated supervision.
paper/related_work.tex:16:Goodhart's Law is established theoretically~\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\cite{gao-reward-overoptimization} and frontier models~\cite{metr-reward-hacking}; specification gaming~\cite{bondarenko-spec-gaming}, formalization gaming~\cite{kim-game-formalization}, and spurious rewards~\cite{spurious-rewards} have been documented, but the proxy is a learned reward model.
paper/related_work.tex:17:Kim et al.~\cite{kim-game-formalization} diagnose gaming in inference-time outputs of frontier models; we study gaming that \emph{emerges during RL training} with a systematic taxonomy and cross-logic analysis.
paper/related_work.tex:21:STA adapts the LOO mutation paradigm~\cite{demillo1978, jia-harman-survey} from software testing to solver inputs.
paper/experiments.tex:8:We train Qwen3-4B with GRPO~\citep{deepseekmath} ($K{=}8$ rollouts, 500 steps default, 1000 where noted) across seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across conditions. %% data: C001
paper/experiments.tex:39:ISR-as-reward provides the first empirical demonstration of Goodhart's Law at the meta level~\citep{manheim-goodhart-taxonomy}: the diagnostic itself becomes the target of gaming when optimized.
paper/experiments.tex:75:At $\beta{=}0.3$, ISR causes PR collapse to 18\% (vs.\ 48\% random), completing the Goodhart trajectory: low-dose gaming ($\beta{=}0.1$) gives way to high-dose collapse~\cite{gao-reward-overoptimization}. %% registry: plan002-additive-b03-s42, plan017-additive-random-s42
paper/conclusion.tex:15:The dose-response pattern ($\beta{=}0.1$: proxy gaming; $\beta{=}0.3$: collapse) maps onto~\cite{gao-reward-overoptimization} at a meta level.
paper/method.tex:15:We train with GRPO~\citep{deepseekmath} ($K{=}8$ rollouts), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x) = \textit{proved}]$.
paper/limitations.tex:10:Our experiments use 500 training examples and 100 evaluation examples, reflecting the FOLIO dataset's total size of 1,435 annotated examples~\citep{folio}.
paper/introduction.tex:8:Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\cite{skalse-reward-hacking, reward-hacking-survey}.
paper/introduction.tex:9:Recent work applies GRPO~\cite{deepseekmath} to train LLMs that generate solver-verified formal programs~\cite{mellgren-prolog-grpo, logic-rl} using binary execution feedback as reward; this drives rapid PR gains but gives no gradient on structural quality.
paper/introduction.tex:10:Process reward models~\cite{lightman-verify-step} offer step-level supervision but require expensive annotations and do not transfer to arbitrary solver-backed settings.
paper/introduction.tex:13:We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\autoref{fig:sta-overview}).
paper/introduction.tex:17:Applied as a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\cite{folio} data, ISR reveals a structural collapse trajectory entirely invisible to prove rate: ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\% degradation---while prove rate simultaneously rises from 32\% to 96\%.
paper/introduction.tex:21:A natural question is whether ISR can serve as a training signal. The answer is negative: when ISR is added to the reward ($r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR})$), the model games the diagnostic itself---\emph{meta-level Goodhart's Law}~\cite{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.
paper/appendix.tex:109:The dose-response pattern ($\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.3$: PR collapse to 18\% vs.\ 48\% random) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "d0905c45-8fba-4b06-90e4-e5f93b92cfcb",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/related_work.tex:5:Prompting-based pipelines couple LLMs with external solvers---SatLM~\\cite{satlm}, Logic-LM~\\cite{logic-lm}, LINC~\\cite{linc}, LoRP~\\cite{lorp}, FOVER~\\cite{fover-pei2025}---but evaluate execution accuracy alone without diagnosing structural quality.\npaper/related_work.tex:6:RL approaches train against solver feedback~\\cite{mellgren-prolog-grpo, logic-rl, thought-like-pro}, optimizing prove rate with binary reward.\npaper/related_work.tex:8:We use FOLIO~\\cite{folio}, the only public NLI benchmark with both FOL and Prolog annotations enabling cross-logic diagnostic transfer.\npaper/related_work.tex:11:Learned PRMs~\\cite{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from design-choice sensitivity~\\cite{gao-effective-rl-reward} and distribution shift~\\cite{processbench}; recent advances~\\cite{thinkprm, versaprm, rprm} improve quality but remain learned and require curated supervision.\npaper/related_work.tex:16:Goodhart's Law is established theoretically~\\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\\cite{gao-reward-overoptimization} and frontier models~\\cite{metr-reward-hacking}; specification gaming~\\cite{bondarenko-spec-gaming}, formalization gaming~\\cite{kim-game-formalization}, and spurious rewards~\\cite{spurious-rewards} have been documented, but the proxy is a learned reward model.\npaper/related_work.tex:17:Kim et al.~\\cite{kim-game-formalization} diagnose gaming in inference-time outputs of frontier models; we study gaming that \\emph{emerges during RL training} with a systematic taxonomy and cross-logic analysis.\npaper/related_work.tex:21:STA adapts the LOO mutation paradigm~\\cite{demillo1978, jia-harman-survey} from software testing to solver inputs.\npaper/experiments.tex:8:We train Qwen3-4B with GRPO~\\citep{deepseekmath} ($K{=}8$ rollouts, 500 steps default, 1000 where noted) across seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across conditions. %% data: C001\npaper/experiments.tex:39:ISR-as-reward provides the first empirical demonstration of Goodhart's Law at the meta level~\\citep{manheim-goodhart-taxonomy}: the diagnostic itself becomes the target of gaming when optimized.\npaper/experiments.tex:75:At $\\beta{=}0.3$, ISR causes PR collapse to 18\\% (vs.\\ 48\\% random), completing the Goodhart trajectory: low-dose gaming ($\\beta{=}0.1$) gives way to high-dose collapse~\\cite{gao-reward-overoptimization}. %% registry: plan002-additive-b03-s42, plan017-additive-random-s42\npaper/conclusion.tex:15:The dose-response pattern ($\\beta{=}0.1$: proxy gaming; $\\beta{=}0.3$: collapse) maps onto~\\cite{gao-reward-overoptimization} at a meta level.\npaper/method.tex:15:We train with GRPO~\\citep{deepseekmath} ($K{=}8$ rollouts), where each rollout receives binary execution reward $r_{\\text{exec}}(x) = \\mathbf{1}[S(F_x) = \\textit{proved}]$.\npaper/limitations.tex:10:Our experiments use 500 training examples and 100 evaluation examples, reflecting the FOLIO dataset's total size of 1,435 annotated examples~\\citep{folio}.\npaper/introduction.tex:8:Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\\cite{skalse-reward-hacking, reward-hacking-survey}.\npaper/introduction.tex:9:Recent work applies GRPO~\\cite{deepseekmath} to train LLMs that generate solver-verified formal programs~\\cite{mellgren-prolog-grpo, logic-rl} using binary execution feedback as reward; this drives rapid PR gains but gives no gradient on structural quality.\npaper/introduction.tex:10:Process reward models~\\cite{lightman-verify-step} offer step-level supervision but require expensive annotations and do not transfer to arbitrary solver-backed settings.\npaper/introduction.tex:13:We address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\\autoref{fig:sta-overview}).\npaper/introduction.tex:17:Applied as a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\cite{folio} data, ISR reveals a structural collapse trajectory entirely invisible to prove rate: ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\\% degradation---while prove rate simultaneously rises from 32\\% to 96\\%.\npaper/introduction.tex:21:A natural question is whether ISR can serve as a training signal. The answer is negative: when ISR is added to the reward ($r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$), the model games the diagnostic itself---\\emph{meta-level Goodhart's Law}~\\cite{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.\npaper/appendix.tex:109:The dose-response pattern ($\\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\\beta{=}0.3$: PR collapse to 18\\% vs.\\ 48\\% random) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.",
    "numLines": 20
  }
}
```

</details>

---

### Assistant

_source line 21_

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
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "6f350b22-461d-4c43-8716-9531e976c93f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EfjJwvaWpi7Mr8CV8epxSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 61814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2559
      },
      "output_tokens": 64,
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

_source line 22_

Now I have full context. Let me execute the fixes.

**M1: Fix s43 PR 13% inconsistency in Tab.4**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d657170b-2524-4d66-bab0-a2a1a71a3d4a",
  "uuid": "069b37f6-15ff-4385-943f-b33bf105dfb5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EfjJwvaWpi7Mr8CV8epxSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 61814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2559
      },
      "output_tokens": 64,
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
