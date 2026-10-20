# paper final check and compile

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 3
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_paper_final-check-and-compile_20260522T114610.log`
- **Structured JSON:** [`44af9f06b3053a4513f2.json`](../../sessions/44/44af9f06b3053a4513f2.json)

## Before a recorded user message

47 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
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
    "mcp__agent-ml-research__clone_repo",
    "mcp__agent-ml-research__list_repo_tree",
    "mcp__agent-ml-research__read_repo_file",
    "mcp__agent-ml-research__search_repo",
    "mcp__agent-ml-research__sync_code_to_remote"
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
  "uuid": "a0356402-3c5e-45e1-8b7a-7cdc18592c63",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 2_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779459600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ecf3e2f0-7aa4-4460-bdd7-3a360862f97f",
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to do three main tasks:
1. Check 8B results in appendix and limitations
2. Sync paper/ and docs/paper/ directories
3. Final compilation

They also tried to spawn a worker for review issues audit, but that's an MCP tool call that failed or is separate. Let me focus on the three tasks they outlined.

Let me start by reading the relevant files and running the sync check in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "6803bed2-6357-4487-be40-0613fe45cfe3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtZhD1hg5SHdHYWAeEdYHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16133,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16133
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

### Assistant

_source line 4_

I'll start by reading the relevant files and checking sync status in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "2a0ff9bc-ac1e-436d-948a-b40a7c7db6e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtZhD1hg5SHdHYWAeEdYHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16133,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16133
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01MQFtibmscJazyDc3dWpEkX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "ff59b60a-db02-49a5-878e-e820e1f78532",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtZhD1hg5SHdHYWAeEdYHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16133,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16133
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

_source line 6 · 2026-05-22T12:05:40.054Z_

<details><summary>↩ Tool result · `toolu_01MQFtibmscJazyDc3dWpEkX`</summary>

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
10	\begin{table}[ht]
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
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.
56	
57	\paragraph{SFT convergence.}
58	SFT training converged across all three seeds: final-step loss ${\leq}0.04$ and token accuracy ${>}99\%$ after ${\sim}8$ epochs on 500 examples (seed~42: $0.029$; seed~44: $0.033$); the 1000-step extension further decreases loss to $0.017$.
59	
60	\paragraph{Evaluation exception.}
61	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
62	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
63	
64	\paragraph{Reward formulation.}
65	An additive variant ($r = r_{\text{exec}} + \beta\,\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\text{exec}}\cdot(1+\beta\,\text{ISR})$ ensures ISR modulates only proved outputs.
66	
67	\paragraph{ProofFOL dataset construction.}
68	\label{app:prooffol-construction}
69	ProofFOL is derived from ProofWriter~\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\sim}70\%$ retention; failures from timeouts, unsupported constructs, and translation errors).
70	Of the translated examples, 99.1\% parse successfully (92 skipped due to empty FOL output).
71	We sample 500 training and 100 evaluation examples (seed~42) from the verified pool.
72	Table~\ref{tab:prooffol-vs-folio} compares key structural properties.
73	
74	\begin{table}[!ht]
75	\centering
76	\caption{ProofFOL vs.\ FOLIO structural comparison (training sets, $n{=}500$ each).}
77	\label{tab:prooffol-vs-folio}
78	\footnotesize
79	\resizebox{\columnwidth}{!}{%
80	\begin{tabular}{@{}lcc@{}}
81	\toprule
82	\textbf{Property} & \textbf{ProofFOL} & \textbf{FOLIO} \\
83	\midrule
84	FOL premises (mean$\pm$std) & $18.2 \pm 3.2$ & $5.3 \pm 1.4$ \\
85	\quad Ground facts & $10.2 \pm 3.0$ & $1.8 \pm 1.5$ \\
86	\quad Rules & $8.1 \pm 1.1$ & $3.5 \pm 1.9$ \\
87	XOR ($\oplus$) samples & 0\% & 37.2\% \\
88	Dominant depth & 4--5 & 2--3 \\
89	Predicate style & synthetic & real-world \\
90	FOL source & GPT-4o (silver) & human (gold) \\
91	\bottomrule
92	\end{tabular}}
93	\end{table}
94	
95	ProofFOL problems are structurally more complex ($3.4{\times}$ more premises) but use simpler, synthetic predicates (e.g., \texttt{Blue(x)}, \texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.
96	The absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.
97	
98	\section{STA Algorithm}
99	\label{app:algorithm}
100	
101	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
102	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
103	
104	
105	\section{Extended Discussion}
106	\label{app:extended-discussion}
107	
108	\paragraph{What ISR measures---and what it does not.}
109	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
110	This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.
111	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
112	ISR and downstream task performance are uncorrelated.
113	ISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
114	
115	Critically, low ISR carries different semantics depending on the training objective.
116	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
117	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
118	ISR values must always be interpreted relative to the optimization objective that produced them.
119	
120	\paragraph{The premise-count confound.}
121	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
122	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
123	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
124	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
125	This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
126	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
127	
128	\begin{table*}[ht]
129	\centering
130	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
131	\label{tab:bootstrap-ci}
132	\small
133	\begin{tabular}{@{}lcccc@{}}
134	\toprule
135	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
136	\midrule
137	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (PG+FN corrected)}} \\
138	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
139	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
140	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
141	\midrule
142	\multicolumn{5}{@{}l}{\textit{TS gaming rate}} \\
143	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
144	\midrule
145	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
146	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
147	\bottomrule
148	\end{tabular}
149	\\[2pt]
150	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
151	\end{table*}
152	
153	\paragraph{TS dose-response gradient.}
154	TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
155	The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
156	
157	\paragraph{Goodhart effects: implications.}
158	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.
159	The dose-response pattern maps onto the Manheim \& Garrabrant taxonomy~\citep{manheim-goodhart-taxonomy}: $\beta{=}0.1$ on FOLIO instantiates \emph{regressional} Goodhart ($P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR erroneously rewards the shortcut); $\beta{\geq}0.2$ introduces \emph{extremal} elements (PR collapse to 18\% vs.\ 48\% random at $\beta{=}0.3$).
160	The implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \S\ref{sec:crossdomain}).
161	
162	\paragraph{Single-seed unreliability.}
163	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
164	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\S\ref{sec:goodhart}).
165	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
166	
167	\paragraph{Classifier limitations.}
168	Text-match hacking classifiers have systematic blind spots that functional analysis exposes.
169	In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-detailed}).
170	One seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.
171	Practitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.
172	
173	\paragraph{Practical guidelines.}
174	\label{app:practical-guidelines}
175	Our findings yield five guidelines for GRPO-trained neurosymbolic systems:
176	(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.
177	(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\S\ref{sec:diagnostic}).
178	(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.
179	(4)~Treat LOO-based metrics as component-count-biased until normalized.
180	(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.
181	
182	\paragraph{Multiple testing correction.}
183	\label{app:statistical-details}
184	We define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).
185	Within the FOLIO family, Bonferroni correction at $\alpha{=}0.05$ yields adjusted thresholds of $p_{\text{adj}}{=}0.05/14{=}0.0036$.
186	Three primary comparisons survive correction: the TS rate difference (ISR vs.\ random; $p_{\text{bonf}}{=}1.82{\times}10^{-38}$), the SFT vs.\ exec-only non-hacking rate ($p_{\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\text{bonf}}{<}10^{-8}$).
187	The matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\text{bonf}}{=}0.056$), significant at $\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).
188	The ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.
189	Bonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.
190	We report the most conservative Bonferroni results for transparency.
191	
192	
193	\section{Hacking Mode Definitions}
194	\label{app:hacking-modes}
195	
196	We identify eight distinct reward hacking modes across all experiments.
197	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
198	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
199	
200	\begin{table*}[ht]
201	\centering
202	\small
203	\begin{tabular}{@{}llcccc@{}}
204	\toprule
205	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
206	\midrule
207	CE & Concl.\ in premises & 87 & 18 & 71 & 7 \\
208	TS & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
209	PG & Premise-subset gaming & 6 & 5 & -- & 0 \\
210	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
211	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
212	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
213	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
214	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
215	\bottomrule
216	\end{tabular}
217	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\dagger$Random TS driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: CE${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
218	\label{tab:hacking-taxonomy-app}
219	\end{table*}
220	
221	\paragraph{Classifier Validation.}
222	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
223	CE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
224	No training data or manual annotation is used for classification.
225	
226	To estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
227	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
228	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
229	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
230	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
231	
232	\paragraph{Boundary case validation.}
233	Stratified validation across 82 samples (all five hacking categories) yields Cohen's $\kappa{=}1.0$; independent re-annotation confirms full agreement.
234	Structured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.
235	Short-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.
236	Low-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.
237	3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.
238	
239	\subsection{PG --- Premise-Subset Gaming}
240	\label{app:h8}
241	
242	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).
243	We term this \textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
244	
245	\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
246	Automated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.
247	
248	\paragraph{Audit scope and limitations.}
249	Full PG audit was completed for ISR $\beta{=}0.1$ seed~42 only.
250	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.
251	Random $\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.
252	
253	\paragraph{TS false-negative correction (TSb obfuscated tautology).}
254	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
255	Manual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
256	We classify these as \textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.
257	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\S\ref{sec:taxonomy}).
258	After correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.
259	
260	\paragraph{Impact on non-hacking-rate comparison.}
261	After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
262	The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
263	
264	\subsection{CE --- Conclusion Embedding}
265	
266	\paragraph{Definition.}
267	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
268	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
269	
270	\paragraph{Example (FOL).}
271	\smallskip\noindent\rule{\columnwidth}{0.3pt}
272	{\small\begin{verbatim}
273	Premises:
274	  all x (bird(x) -> flies(x)).
275	  bird(tweety).
276	  flies(tweety).  % conclusion embedded
277	Conclusion: flies(tweety).
278	\end{verbatim}}
279	\noindent\rule{\columnwidth}{0.3pt}\smallskip
280	
281	\paragraph{ISR interaction.}
282	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
283	ISR does not distinguish trivial from substantive necessity.
284	
285	\paragraph{Prevalence.}
286	Conclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\% across all RL conditions.
287	Under exec-only and Random reward, it manifests as CE (71--93\%); under ISR reward, it shifts to TS (70.6\% pooled).
288	
289	
290	\subsection{TSa --- Conclusion Duplication (Standard)}
291	
292	\paragraph{Definition.}
293	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
294	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
295	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
296	
297	\paragraph{Example (FOL).}
298	\smallskip\noindent\rule{\columnwidth}{0.3pt}
299	{\small\begin{verbatim}
300	Premises:
301	  all x ((A(x)&B(x))->(C(x)|D(x))).
302	Conclusion:
303	  all x ((A(x)&B(x))->(C(x)|D(x))).
304	\end{verbatim}}
305	\noindent\rule{\columnwidth}{0.3pt}\smallskip
306	
307	\paragraph{ISR interaction.}
308	ISR~$\approx 0.8$--$1.0$.
309	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
310	TSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.
311	
312	\paragraph{Prevalence.}
313	TSa (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
314	Combined TS (TSa + TSb): 70.6\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).
315	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all TSa; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
316	
317	
318	\subsection{TSb --- Obfuscated Tautology}
319	
320	\paragraph{Definition.}
321	A single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.
322	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
323	
324	\paragraph{Example (FOL, vacuous quantifier wrapping).}
325	\smallskip\noindent\rule{\columnwidth}{0.3pt}
326	{\small\begin{verbatim}
327	Premises:
328	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
329	Conclusion:
330	  all x ((A(x)&B(x))->(C(x)|D(x))).
331	\end{verbatim}}
332	\noindent\rule{\columnwidth}{0.3pt}\smallskip
333	The premise introduces a vacuous second variable $y$, immediately unified with $x$; the formulas are logically equivalent but differ textually.
334	
335	\paragraph{ISR interaction.}
336	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
337	TSb simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).
338	This triple gaming makes TSb the most complete Goodhart case we observe.
339	
340	\paragraph{Prevalence.}
341	Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
342	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
343	
344	
345	\subsection{Tautological Collapse}
346	
347	\paragraph{Definition.}
348	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
349	
350	\paragraph{Example (FOL).}
351	\smallskip\noindent\rule{\columnwidth}{0.3pt}
352	\begin{verbatim}
353	Premises: p(a).
354	Conclusion: p(a).
355	\end{verbatim}
356	\noindent\rule{\columnwidth}{0.3pt}\smallskip
357	
358	\paragraph{ISR interaction.}
359	ISR~$=1.0$ (the sole premise is necessary).
360	Distinguished from TS by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
361	
362	\paragraph{Prevalence.}
363	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% TS by strict classifier).
364	Also observed in Prolog exec+STA seed~42 (100\% TS, PR~$=0.50$).
365	
366	
367	\subsection{Repetition Collapse}
368	
369	\paragraph{Definition.}
370	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
371	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
372	
373	\paragraph{Example (Prolog).}
374	\smallskip\noindent\rule{\columnwidth}{0.3pt}
375	\begin{verbatim}
376	penguin(fido).
377	penguin(fido).
378	penguin(fido).
379	... (repeated to 512 tokens)
380	query(penguin(fido)).
381	\end{verbatim}
382	\noindent\rule{\columnwidth}{0.3pt}\smallskip
383	
384	\paragraph{ISR interaction.}
385	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
386	ISR correctly diagnoses this degeneration.
387	
388	\paragraph{Prevalence.}
389	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
390	
391	
392	\subsection{Complexity-without-Utility}
393	
394	\paragraph{Definition.}
395	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.
396	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
397	
398	\paragraph{Example (FOL).}
399	\smallskip\noindent\rule{\columnwidth}{0.3pt}
400	{\small\begin{verbatim}
401	Premises:
402	  all x all y (R(x,y) ->
403	    exists z (S(x,z) & T(z,y))).
404	  all x (P(x) -> Q(x)).
405	  P(a).            % only this needed
406	Conclusion: Q(a).
407	\end{verbatim}}
408	\noindent\rule{\columnwidth}{0.3pt}\smallskip
409	
410	\paragraph{ISR interaction.}
411	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
412	This is the mode ISR is best calibrated for.
413	
414	\paragraph{Prevalence.}
415	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
416	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
417	
418	
419	\subsection{Contradiction Explosion}
420	
421	\paragraph{Definition.}
422	The component count grows unboundedly over training.
423	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
424	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
425	
426	\paragraph{Example (FOL, 1000-step exec-only).}
427	\smallskip\noindent\rule{\columnwidth}{0.3pt}
428	{\small\begin{verbatim}
429	Premises:
430	  c1. c2. c3. ... c18. % 18.55 mean
431	  % conclusion embedded among premises
432	Conclusion: Q(a).
433	\end{verbatim}}
434	\noindent\rule{\columnwidth}{0.3pt}\smallskip
435	
436	\paragraph{ISR interaction.}
437	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
438	
439	\paragraph{Prevalence.}
440	Observed in extended exec-only training (seed~42, 1000 steps).
441	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
442	
443	
444	\subsection{Query-as-Fact Gaming}
445	
446	\paragraph{Definition.}
447	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
448	Prolog trivially proves the query by unifying with the fact.
449	This mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.
450	
451	\paragraph{Example (Prolog).}
452	\smallskip\noindent\rule{\columnwidth}{0.3pt}
453	\begin{verbatim}
454	% NL: "Fido is happy."
455	% Model output:
456	fido_is_happy.
457	:- fido_is_happy.     % query = fact
458	\end{verbatim}
459	\noindent\rule{\columnwidth}{0.3pt}\smallskip
460	
461	\paragraph{ISR interaction.}
462	ISR~$\approx 0.9$--$1.0$.
463	The single fact is trivially necessary (its removal breaks the query), inflating ISR.
464	Functionally equivalent to TS but with a distinct surface mechanism.
465	
466	\paragraph{Prevalence.}
467	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
468	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
469	
470	
471	\section{Per-Seed Detailed Results}
472	\label{app:detailed-results}
473	
474	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
475	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
476	ISR values are proved-only ISR$^*$.
477	
478	\begin{table*}[t]
479	\centering
480	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\times}2$ vs.\ $2{\times}4$, mathematically equivalent).}
481	\label{tab:fol-detailed}
482	\label{tab:fol-beta01-detailed}
483	\footnotesize
484	\setlength{\tabcolsep}{3pt}
485	\resizebox{\textwidth}{!}{%
486	\begin{tabular}{@{}llccccccl@{}}
487	\toprule
488	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
489	\midrule
490	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
491	Base model (no training)
492	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
493	Ground-truth FOL
494	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
495	SFT
496	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
497	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
498	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
499	\cmidrule(l){2-9}
500	  & \multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \textbf{92.3} & $n{=}39$ proved \\
501	\midrule
502	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
503	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
504	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\%$ \\
505	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
506	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
507	  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\
508	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
509	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & PG${=}15\%$ \\
510	\cmidrule(l){2-9}
511	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.68{\pm}0.47$ & $0.238{\pm}0.30$ & & & & 500-step \\
512	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.02$ & $0.029{\pm}0.05$ & & & $2.1{\pm}3.6$ & 1000-step \\
513	\midrule
514	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
515	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed CE+TS+PG \\
516	  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\
517	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\
518	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\
519	  & 45$^\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \textbf{54.8} & PG${=}1$; $n{=}42$ \\
520	  & 46$^\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \textbf{54.5} & PG${=}4$; $n{=}77$ \\
521	\cmidrule(l){2-9}
522	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.77{\pm}0.14$ & $0.716{\pm}0.26$ & & & & 500-step (s42--44) \\
523	  & \multicolumn{2}{l}{5-seed mean$\pm$std} & $0.70{\pm}0.19$ & $0.633{\pm}0.23$ & & & & 500-step (s42--46) \\
524	\midrule
525	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
526	  & \multicolumn{8}{l}{See Table~\ref{tab:beta03-detailed} for per-seed $\beta{=}0.3$ results.} \\
527	\midrule
528	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
529	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\
530	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\
531	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\cap$PG: 6) \\
532	\cmidrule(l){2-9}
533	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.87{\pm}0.08$ & $0.117{\pm}0.042$ & & & & TS seed-dep.: 0/38/0\% \\
534	\midrule
535	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
536	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
537	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
538	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
539	\cmidrule(l){2-9}
540	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & & \\
541	\midrule
542	\multicolumn{9}{@{}l}{\textit{Shuffled-ISR $\beta{=}0.1$ (deconfounding control)}} \\
543	  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
544	  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \textbf{87.5} & $n{=}16$ proved \\
545	  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
546	\cmidrule(l){2-9}
547	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.153{\pm}0.006$ & $0.559{\pm}0.015$ & $6.5$ & $6.5$ & \textbf{87.0} & $N{=}46$ proved \\
548	\bottomrule
549	\end{tabular}}% end resizebox
550	\end{table*}
551	
552	
553	\begin{table*}[t]
554	\centering
555	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
556	\label{tab:prolog-detailed}
557	\small
558	\begin{tabular}{@{}llcccccl@{}}
559	\toprule
560	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
561	\midrule
562	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
563	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
564	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
565	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
566	\cmidrule(l){2-8}
567	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.53{\pm}0.31$ & $0.146{\pm}0.21$ & & & \\
568	\midrule
569	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
570	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & TS tautological \\
571	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional TS$^a$ \\
572	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
573	\cmidrule(l){2-8}
574	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.62{\pm}0.31$ & $0.699{\pm}0.45$ & & & 3/3 Goodhart, 0\% non-hacking \\
575	\bottomrule
576	\end{tabular}
577	
578	\vspace{4pt}
579	{\footnotesize
580	$^a$ Strict TS classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
581	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\
582	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
583	}
584	\end{table*}
585	
586	\begin{table*}[t]
587	\centering
588	\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\S\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\text{f50}}{>}0.90$.}
589	\label{tab:prooffol-detailed}
590	\small
591	\begin{tabular}{@{}llcccccl@{}}
592	\toprule
593	\textbf{Condition} & \textbf{Seed} & \textbf{PR$_{\text{f50}}$} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{Genuine\%} & \textbf{Notes} \\
594	\midrule
595	Base & --- & 0.16 & 0.310 & 0 & 0 & \textbf{100} & $n{=}16$ proved \\
596	\midrule
597	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
598	  & 42 & ${\approx}$1.0 & 0.066 & \textbf{100} & 0 & 0 & $n{=}99$; stable \\
599	  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\
600	  & 44 & ${\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\
601	\cmidrule(l){2-8}
602	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{17.4\% genuine (mean of seeds)} & \\
603	\midrule
604	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
605	  & 42 & 0.35 & 0.12 & 0 & 0 & \textbf{100} & $n{=}46$; collapsed \\
606	  & 43 & ${\approx}$0.47 & ${\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\
607	  & 44 & 0.49 & 0.145 & 0 & 0 & \textbf{100} & $n{=}66$; oscillation \\
608	\cmidrule(l){2-8}
609	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{\textbf{76.8\%} genuine (mean of seeds)} & \\
610	\bottomrule
611	\end{tabular}
612	
613	\vspace{4pt}
614	{\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}
615	\end{table*}
616	
617	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
618	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
619	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
620	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.
621	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
622	
623	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
624	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
625	seed~42 produces clean TS tautologies (single premise~$=$~conclusion),
626	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
627	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
628	The diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
629	
630	\subsection{Per-Seed Results at $\beta{=}0.2$ and $\beta{=}0.3$}
631	\label{app:beta03}
632	
633	Table~\ref{tab:beta03-detailed} reports per-seed results for ISR at $\beta{=}0.2$ and both ISR and Random at $\beta{=}0.3$.
634	At $\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\% or near-100\% TS), confirming $\beta{\geq}0.2$ as the extremal Goodhart regime.
635	The three ISR $\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
636	
637	\begin{table*}[ht]
638	\centering
639	\caption{Per-seed results at $\beta{=}0.2$ and $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}
640	\label{tab:beta03-detailed}
641	\small
642	\begin{tabular}{@{}llcccccl@{}}
643	\toprule
644	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Mode} \\
645	\midrule
646	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.2$}} \\
647	  & 42 & 1.00 & 0.602 & \textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\
648	  & 43 & 0.96 & 0.552 & \textbf{96.9} & 1.0 & 0 & PG${=}2$ \\
649	  & 44 & 0.94 & 0.964 & \textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\
650	\cmidrule(l){2-8}
651	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.03$ & $0.71{\pm}0.22$ & & & 3/3 TS Goodhart \\
652	\midrule
653	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
654	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\
655	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\
656	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure TS Goodhart \\
657	\cmidrule(l){2-8}
658	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.66{\pm}0.42$ & $0.39{\pm}0.31$ & & & \\
659	\midrule
660	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
661	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\
662	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
663	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
664	\cmidrule(l){2-8}
665	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & \\
666	\bottomrule
667	\end{tabular}
668	\end{table*}
669	
670	\FloatBarrier
671	
672	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
673	\label{app:100step}
674	
675	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%, higher than SFT (13.0\%, 3-seed pooled) but still early in training.
676	Of the 32 proved samples, 9 (28.1\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
677	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
678	This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
679	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
680	
681	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
682	\label{app:o1-ablation}
683	
684	All main experiments (\S\ref{sec:diagnostic}--\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\texttt{execution\_fast\_sta}) but is used only in the ablation reported here.
685	The two signals measure fundamentally different properties, not approximations of the same quantity.
686	The binary signal tests \emph{collective} premise necessity: $\text{fast\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
687	LOO tests \emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.
688	
689	\paragraph{Evaluation-time comparison.}
690	Across 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.
691	This renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.
692	By contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.
693	Of 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.
694	
695	\paragraph{Training-time ablation.}
696	As a training reward ($r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$, functionally zero, compared to $\text{ISR}^*{=}0.132$ under exec-only and $\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\beta{=}0.1$.
697	The tautology check depresses prove rate by 30\,pp relative to exec-only ($63\%$ vs.\ $93\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.
698	That even the fine-grained $O(n)$ LOO signal, which \emph{does} provide per-component necessity feedback, is ultimately gamed (\S\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.
699	
700	\paragraph{Computational overhead.}
701	Full LOO requires $n{+}1$ solver calls per sample (mean $n{\approx}6$ for FOLIO).
702	With Prover9 at ${\sim}5$\,ms per call, STA evaluation adds ${\sim}55$\,ms per sample versus ${\sim}4$\,s for LLM inference (${<}1\%$ overhead).
703	The $O(1)$ binary check adds a single solver call per proved sample (${<}2\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.
704	
705	\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}
706	\label{app:llama-coldstart}
707	
708	We applied the identical GRPO configuration (Table~\ref{tab:hyperparams}) to LLaMA-3.2-3B~\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).
709	Across 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\footnote{This run was also affected by a generation-termination configuration issue (dual EOS tokens); the zero prove rate reflects both the base model's lack of FOL generation capability and truncated outputs.}
710	This establishes a \emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.
711	Qwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\ 4B), likely reflecting pretraining data composition.
712	An SFT warmstart (3 epochs on gold formalizations, lr$=$2$\times$10$^{-5}$) achieves $\text{PR}{=}16\%$ ($n{=}100$) after correcting the generation-termination issue.
713	However, the model produces Unicode FOL notation ($\forall$, $\to$, $\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data; the 16\% prove rate reflects Prover9's partial Unicode tolerance rather than correct format adherence.
714	Subsequent GRPO runs (exec-only, 500 steps from SFT warmstart, 3 seeds) fail to improve beyond SFT baseline ($\text{PR}{=}15.0{\pm}1.0\%$, $n{=}14$--$16$ proved per seed), yet produce no structural degeneration: $86.6{\pm}0.9\%$ of proved samples are genuine across seeds, with cross-seed variance near zero ($\sigma_{\text{PR}}{=}1$\,pp).
715	This contrasts sharply with Qwen3-4B, where GRPO reaches $93\%$ PR but collapses to $8\%$ genuine with high cross-seed variance.
716	The result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.
717	
718	\subsection{Seed-Dependent Convergence in Exec-Only GRPO}
719	\label{app:seed-convergence}
720	
721	Not all exec-only seeds converge.
722	Of 6 seeds tested (s42--s46, s52), we observe three regimes: \emph{converging with degeneration} (s42: $\text{PR}{=}93\%$, genuine${=}7.5\%$; s44: $\text{PR}{=}96\%$, genuine${=}0\%$; s46: $\text{PR}{=}93\%$ at 500 steps), \emph{slow convergence with degeneration} (s43: $\text{PR}{=}14\%$ but $100\%$ hacking at 500 steps), and \emph{non-converging} (s45: $\text{PR}{=}15\%$, genuine${=}86.7\%$; s52: $\text{PR}{=}14\%$, genuine${=}85.7\%$).
723	Non-converging seeds retain high genuine rates (85--87\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.
724	Extended training to 1000 steps for s45 confirms persistent non-convergence ($\text{PR}{=}15\%$, $\text{ISR}^*{=}0.592$, genuine${=}86.7\%$, $n{=}15$ proved); the model neither improves nor degenerates.
725	
726	This parallels the LLaMA-3.2-3B finding (Appendix~\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.
727	Both cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.
728	
729	\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}
730	\label{app:8b-results}
731	
732	To test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yielding zero GRPO advantage and no learning signal).
733	Table~\ref{tab:8b-combined} summarizes configuration differences and results.
734	
735	\begin{table}[H]
736	\centering
737	\small
738	\begin{tabular}{lcc}
739	\toprule
740	& \textbf{Qwen3-4B} & \textbf{Qwen3-8B} \\
741	\midrule
742	Rollouts ($K$) & 4 & 8 \\
743	Batch size & 4 & 1 \\
744	Gradient accum. & 2 & 16 \\
745	Effective batch & 8 & 16 \\
746	\bottomrule
747	\end{tabular}
748	
749	\vspace{4pt}
750	
751	\resizebox{\columnwidth}{!}{%
752	\begin{tabular}{lcccc}
753	\toprule
754	\textbf{Config} & \textbf{PR\%} & \textbf{Genuine\%} & \textbf{Converged?} & \textbf{Gradient} \\
755	\midrule
756	4B $K{=}4$ s42 & 93 & 7.5 & Yes (degenerate) & Sufficient \\
757	8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\
758	8B $K{=}8$ s42 & 14 & 92.9 & No & Partial \\
759	\bottomrule
760	\end{tabular}}
761	\caption{Cross-scale: Qwen3-4B vs.\ Qwen3-8B. \textbf{Top}: Configuration; $K{=}8$ required at 8B because $K{=}4$ produces near-identical rollouts. \textbf{Bottom}: Results; 4B converges with degeneration, both 8B configurations fail to converge, preserving structural integrity.}
762	\label{tab:8b-combined}
763	\label{tab:8b-config}
764	\label{tab:8b-comparison}
765	\end{table}
766	
767	We first tested $K{=}4$ (matching the 4B configuration): the 8B model produces near-identical rollouts across all four completions, yielding zero GRPO advantage throughout 500 steps and no learning signal ($\text{PR}{=}15.5\%$, cold-start stagnation).
768	Increasing to $K{=}8$ provides non-zero reward variance during mid-training (approximately 40--50\% of steps between 20--370 show non-zero advantage), but this signal proves insufficient for convergence: held-out evaluation yields $\text{PR}{=}14\%$ ($n{=}14$ proved), $\text{ISR}^*{=}0.573$, genuine${=}92.9\%$ (13/14), with a single CE sample.
769	Cosine learning-rate decay combined with insufficient early bootstrap appears to prevent the model from escaping the low-PR regime.
770	
771	This result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.
772	Together, these cases establish a convergence threshold for GRPO-driven degeneration: the structural collapse documented in \S\ref{sec:diagnostic} requires successful RL optimization as a prerequisite, and at 8B scale the rollout diversity bottleneck prevents this optimization from occurring under our configuration.
773	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "2c3de298-4459-4c85-9720-0e08b8a79598",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 4 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Compute resources.}\nExperiments were run on single-GPU setups (NVIDIA RTX 4090 24\\,GB and RTX PRO 6000 96\\,GB).\nEach GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).\nTotal compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.\n\n\\paragraph{SFT convergence.}\nSFT training converged across all three seeds: final-step loss ${\\leq}0.04$ and token accuracy ${>}99\\%$ after ${\\sim}8$ epochs on 500 examples (seed~42: $0.029$; seed~44: $0.033$); the 1000-step extension further decreases loss to $0.017$.\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\\paragraph{Reward formulation.}\nAn additive variant ($r = r_{\\text{exec}} + \\beta\\,\\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\\text{exec}}\\cdot(1+\\beta\\,\\text{ISR})$ ensures ISR modulates only proved outputs.\n\n\\paragraph{ProofFOL dataset construction.}\n\\label{app:prooffol-construction}\nProofFOL is derived from ProofWriter~\\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \\citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\\sim}70\\%$ retention; failures from timeouts, unsupported constructs, and translation errors).\nOf the translated examples, 99.1\\% parse successfully (92 skipped due to empty FOL output).\nWe sample 500 training and 100 evaluation examples (seed~42) from the verified pool.\nTable~\\ref{tab:prooffol-vs-folio} compares key structural properties.\n\n\\begin{table}[!ht]\n\\centering\n\\caption{ProofFOL vs.\\ FOLIO structural comparison (training sets, $n{=}500$ each).}\n\\label{tab:prooffol-vs-folio}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Property} & \\textbf{ProofFOL} & \\textbf{FOLIO} \\\\\n\\midrule\nFOL premises (mean$\\pm$std) & $18.2 \\pm 3.2$ & $5.3 \\pm 1.4$ \\\\\n\\quad Ground facts & $10.2 \\pm 3.0$ & $1.8 \\pm 1.5$ \\\\\n\\quad Rules & $8.1 \\pm 1.1$ & $3.5 \\pm 1.9$ \\\\\nXOR ($\\oplus$) samples & 0\\% & 37.2\\% \\\\\nDominant depth & 4--5 & 2--3 \\\\\nPredicate style & synthetic & real-world \\\\\nFOL source & GPT-4o (silver) & human (gold) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nProofFOL problems are structurally more complex ($3.4{\\times}$ more premises) but use simpler, synthetic predicates (e.g., \\texttt{Blue(x)}, \\texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.\nThe absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (PG+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table*}\n\n\\paragraph{TS dose-response gradient.}\nTS tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ TS ($36/262$ pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient (random $\\beta{=}0.1$ ($13.7\\%$) $\\to$ random $\\beta{=}0.3$ (4--7 TSa per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.\n\n\\paragraph{Goodhart effects: implications.}\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern maps onto the Manheim \\& Garrabrant taxonomy~\\citep{manheim-goodhart-taxonomy}: $\\beta{=}0.1$ on FOLIO instantiates \\emph{regressional} Goodhart ($P{\\to}P$ tautologies yield $\\text{ISR}{\\geq}0.5$, so ISR erroneously rewards the shortcut); $\\beta{\\geq}0.2$ introduces \\emph{extremal} elements (PR collapse to 18\\% vs.\\ 48\\% random at $\\beta{=}0.3$).\nThe implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \\S\\ref{sec:crossdomain}).\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\\paragraph{Classifier limitations.}\nText-match hacking classifiers have systematic blind spots that functional analysis exposes.\nIn Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-detailed}).\nOne seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.\nPractitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.\n\n\\paragraph{Practical guidelines.}\n\\label{app:practical-guidelines}\nOur findings yield five guidelines for GRPO-trained neurosymbolic systems:\n(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.\n(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\\S\\ref{sec:diagnostic}).\n(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.\n(4)~Treat LOO-based metrics as component-count-biased until normalized.\n(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.\n\n\\paragraph{Multiple testing correction.}\n\\label{app:statistical-details}\nWe define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).\nWithin the FOLIO family, Bonferroni correction at $\\alpha{=}0.05$ yields adjusted thresholds of $p_{\\text{adj}}{=}0.05/14{=}0.0036$.\nThree primary comparisons survive correction: the TS rate difference (ISR vs.\\ random; $p_{\\text{bonf}}{=}1.82{\\times}10^{-38}$), the SFT vs.\\ exec-only non-hacking rate ($p_{\\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\\text{bonf}}{<}10^{-8}$).\nThe matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\\text{bonf}}{=}0.056$), significant at $\\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).\nThe ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.\nBonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.\nWe report the most conservative Bonferroni results for transparency.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify eight distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table*}[ht]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nCE & Concl.\\ in premises & 87 & 18 & 71 & 7 \\\\\nTS & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nPG & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\\dagger$Random TS driven by seed~43 (38.3\\%); seeds~42/44: 0\\%. Exec: CE${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table*}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nCE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\n\\paragraph{Boundary case validation.}\nStratified validation across 82 samples (all five hacking categories) yields Cohen's $\\kappa{=}1.0$; independent re-annotation confirms full agreement.\nStructured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.\nShort-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.\nLow-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.\n3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.\n\n\\subsection{PG --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).\nWe term this \\textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull PG audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.\n\n\\paragraph{TS false-negative correction (TSb obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{CE --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as CE (71--93\\%); under ISR reward, it shifts to TS (70.6\\% pooled).\n\n\n\\subsection{TSa --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nTSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nTSa (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined TS (TSa + TSb): 70.6\\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 13.7\\% (36/262, all TSa; driven by seed~43 at 38.3\\%, seeds~42 and~44 at 0\\%).\n\n\n\\subsection{TSb --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\nThe premise introduces a vacuous second variable $y$, immediately unified with $x$; the formulas are logically equivalent but differ textually.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nTSb simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).\nThis triple gaming makes TSb the most complete Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound primarily in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from TS by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% TS by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% TS, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe single fact is trivially necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to TS but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\\times}2$ vs.\\ $2{\\times}4$, mathematically equivalent).}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \\textbf{92.3} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & PG${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.68{\\pm}0.47$ & $0.238{\\pm}0.30$ & & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.02$ & $0.029{\\pm}0.05$ & & & $2.1{\\pm}3.6$ & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed CE+TS+PG \\\\\n  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\\\\n  & 45$^\\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \\textbf{54.8} & PG${=}1$; $n{=}42$ \\\\\n  & 46$^\\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \\textbf{54.5} & PG${=}4$; $n{=}77$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.77{\\pm}0.14$ & $0.716{\\pm}0.26$ & & & & 500-step (s42--44) \\\\\n  & \\multicolumn{2}{l}{5-seed mean$\\pm$std} & $0.70{\\pm}0.19$ & $0.633{\\pm}0.23$ & & & & 500-step (s42--46) \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & \\multicolumn{8}{l}{See Table~\\ref{tab:beta03-detailed} for per-seed $\\beta{=}0.3$ results.} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\\cap$PG: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.87{\\pm}0.08$ & $0.117{\\pm}0.042$ & & & & TS seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Shuffled-ISR $\\beta{=}0.1$ (deconfounding control)}} \\\\\n  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \\textbf{87.5} & $n{=}16$ proved \\\\\n  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.153{\\pm}0.006$ & $0.559{\\pm}0.015$ & $6.5$ & $6.5$ & \\textbf{87.0} & $N{=}46$ proved \\\\\n\\bottomrule\n\\end{tabular}}% end resizebox\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.53{\\pm}0.31$ & $0.146{\\pm}0.21$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & TS tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional TS$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.62{\\pm}0.31$ & $0.699{\\pm}0.45$ & & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict TS classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\\S\\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\\text{f50}}{>}0.90$.}\n\\label{tab:prooffol-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR$_{\\text{f50}}$} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{Genuine\\%} & \\textbf{Notes} \\\\\n\\midrule\nBase & --- & 0.16 & 0.310 & 0 & 0 & \\textbf{100} & $n{=}16$ proved \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & ${\\approx}$1.0 & 0.066 & \\textbf{100} & 0 & 0 & $n{=}99$; stable \\\\\n  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\\\\n  & 44 & ${\\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{17.4\\% genuine (mean of seeds)} & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 0.35 & 0.12 & 0 & 0 & \\textbf{100} & $n{=}46$; collapsed \\\\\n  & 43 & ${\\approx}$0.47 & ${\\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\\\\n  & 44 & 0.49 & 0.145 & 0 & 0 & \\textbf{100} & $n{=}66$; oscillation \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{\\textbf{76.8\\%} genuine (mean of seeds)} & \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean TS tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for ISR at $\\beta{=}0.2$ and both ISR and Random at $\\beta{=}0.3$.\nAt $\\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\\% or near-100\\% TS), confirming $\\beta{\\geq}0.2$ as the extremal Goodhart regime.\nThe three ISR $\\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.2$ and $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.2$}} \\\\\n  & 42 & 1.00 & 0.602 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\\\\n  & 43 & 0.96 & 0.552 & \\textbf{96.9} & 1.0 & 0 & PG${=}2$ \\\\\n  & 44 & 0.94 & 0.964 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.03$ & $0.71{\\pm}0.22$ & & & 3/3 TS Goodhart \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure TS Goodhart \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.66{\\pm}0.42$ & $0.39{\\pm}0.31$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\FloatBarrier\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nAll main experiments (\\S\\ref{sec:diagnostic}--\\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\\texttt{execution\\_fast\\_sta}) but is used only in the ablation reported here.\nThe two signals measure fundamentally different properties, not approximations of the same quantity.\nThe binary signal tests \\emph{collective} premise necessity: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nLOO tests \\emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.\n\n\\paragraph{Evaluation-time comparison.}\nAcross 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.\nThis renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.\nBy contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.\nOf 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.\n\n\\paragraph{Training-time ablation.}\nAs a training reward ($r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$, functionally zero, compared to $\\text{ISR}^*{=}0.132$ under exec-only and $\\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\\beta{=}0.1$.\nThe tautology check depresses prove rate by 30\\,pp relative to exec-only ($63\\%$ vs.\\ $93\\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.\nThat even the fine-grained $O(n)$ LOO signal, which \\emph{does} provide per-component necessity feedback, is ultimately gamed (\\S\\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.\n\n\\paragraph{Computational overhead.}\nFull LOO requires $n{+}1$ solver calls per sample (mean $n{\\approx}6$ for FOLIO).\nWith Prover9 at ${\\sim}5$\\,ms per call, STA evaluation adds ${\\sim}55$\\,ms per sample versus ${\\sim}4$\\,s for LLM inference (${<}1\\%$ overhead).\nThe $O(1)$ binary check adds a single solver call per proved sample (${<}2\\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.\n\n\\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}\n\\label{app:llama-coldstart}\n\nWe applied the identical GRPO configuration (Table~\\ref{tab:hyperparams}) to LLaMA-3.2-3B~\\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).\nAcross 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\\footnote{This run was also affected by a generation-termination configuration issue (dual EOS tokens); the zero prove rate reflects both the base model's lack of FOL generation capability and truncated outputs.}\nThis establishes a \\emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.\nQwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\\ 4B), likely reflecting pretraining data composition.\nAn SFT warmstart (3 epochs on gold formalizations, lr$=$2$\\times$10$^{-5}$) achieves $\\text{PR}{=}16\\%$ ($n{=}100$) after correcting the generation-termination issue.\nHowever, the model produces Unicode FOL notation ($\\forall$, $\\to$, $\\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data; the 16\\% prove rate reflects Prover9's partial Unicode tolerance rather than correct format adherence.\nSubsequent GRPO runs (exec-only, 500 steps from SFT warmstart, 3 seeds) fail to improve beyond SFT baseline ($\\text{PR}{=}15.0{\\pm}1.0\\%$, $n{=}14$--$16$ proved per seed), yet produce no structural degeneration: $86.6{\\pm}0.9\\%$ of proved samples are genuine across seeds, with cross-seed variance near zero ($\\sigma_{\\text{PR}}{=}1$\\,pp).\nThis contrasts sharply with Qwen3-4B, where GRPO reaches $93\\%$ PR but collapses to $8\\%$ genuine with high cross-seed variance.\nThe result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \\emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.\n\n\\subsection{Seed-Dependent Convergence in Exec-Only GRPO}\n\\label{app:seed-convergence}\n\nNot all exec-only seeds converge.\nOf 6 seeds tested (s42--s46, s52), we observe three regimes: \\emph{converging with degeneration} (s42: $\\text{PR}{=}93\\%$, genuine${=}7.5\\%$; s44: $\\text{PR}{=}96\\%$, genuine${=}0\\%$; s46: $\\text{PR}{=}93\\%$ at 500 steps), \\emph{slow convergence with degeneration} (s43: $\\text{PR}{=}14\\%$ but $100\\%$ hacking at 500 steps), and \\emph{non-converging} (s45: $\\text{PR}{=}15\\%$, genuine${=}86.7\\%$; s52: $\\text{PR}{=}14\\%$, genuine${=}85.7\\%$).\nNon-converging seeds retain high genuine rates (85--87\\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.\nExtended training to 1000 steps for s45 confirms persistent non-convergence ($\\text{PR}{=}15\\%$, $\\text{ISR}^*{=}0.592$, genuine${=}86.7\\%$, $n{=}15$ proved); the model neither improves nor degenerates.\n\nThis parallels the LLaMA-3.2-3B finding (Appendix~\\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.\nBoth cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.\n\n\\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}\n\\label{app:8b-results}\n\nTo test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yielding zero GRPO advantage and no learning signal).\nTable~\\ref{tab:8b-combined} summarizes configuration differences and results.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{Qwen3-4B} & \\textbf{Qwen3-8B} \\\\\n\\midrule\nRollouts ($K$) & 4 & 8 \\\\\nBatch size & 4 & 1 \\\\\nGradient accum. & 2 & 16 \\\\\nEffective batch & 8 & 16 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{PR\\%} & \\textbf{Genuine\\%} & \\textbf{Converged?} & \\textbf{Gradient} \\\\\n\\midrule\n4B $K{=}4$ s42 & 93 & 7.5 & Yes (degenerate) & Sufficient \\\\\n8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\\\\n8B $K{=}8$ s42 & 14 & 92.9 & No & Partial \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-scale: Qwen3-4B vs.\\ Qwen3-8B. \\textbf{Top}: Configuration; $K{=}8$ required at 8B because $K{=}4$ produces near-identical rollouts. \\textbf{Bottom}: Results; 4B converges with degeneration, both 8B configurations fail to converge, preserving structural integrity.}\n\\label{tab:8b-combined}\n\\label{tab:8b-config}\n\\label{tab:8b-comparison}\n\\end{table}\n\nWe first tested $K{=}4$ (matching the 4B configuration): the 8B model produces near-identical rollouts across all four completions, yielding zero GRPO advantage throughout 500 steps and no learning signal ($\\text{PR}{=}15.5\\%$, cold-start stagnation).\nIncreasing to $K{=}8$ provides non-zero reward variance during mid-training (approximately 40--50\\% of steps between 20--370 show non-zero advantage), but this signal proves insufficient for convergence: held-out evaluation yields $\\text{PR}{=}14\\%$ ($n{=}14$ proved), $\\text{ISR}^*{=}0.573$, genuine${=}92.9\\%$ (13/14), with a single CE sample.\nCosine learning-rate decay combined with insufficient early bootstrap appears to prevent the model from escaping the low-PR regime.\n\nThis result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.\nTogether, these cases establish a convergence threshold for GRPO-driven degeneration: the structural collapse documented in \\S\\ref{sec:diagnostic} requires successful RL optimization as a prerequisite, and at 8B scale the rollout diversity bottleneck prevents this optimization from occurring under our configuration.\n",
      "numLines": 773,
      "startLine": 1,
      "totalLines": 773
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01XiqopnWj3iRHhzj6mxf5oQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "27621b4e-84fa-4f99-bfdc-93328f386e44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtZhD1hg5SHdHYWAeEdYHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16133,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16133
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

_source line 8 · 2026-05-22T12:05:40.254Z_

<details><summary>↩ Tool result · `toolu_01XiqopnWj3iRHhzj6mxf5oQ`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\ref{app:8b-results},~\ref{app:llama-coldstart}), leaving cross-scale generalization untested.
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "07df0868-ea39-43b8-bec4-14ccbd6982dd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\\ref{app:8b-results},~\\ref{app:llama-coldstart}), leaving cross-scale generalization untested.\nThree to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.\nISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_01UHPY2bFaHnjs3pmGhSqyhH`</summary>

```json
{
  "command": "for f in docs/paper/*.tex docs/paper/*.bib; do base=$(basename \"$f\"); if [ -f \"paper/$base\" ]; then if ! diff -q \"$f\" \"paper/$base\" > /dev/null 2>&1; then echo \"DIFFER: $base\"; fi; else echo \"MISSING in paper/: $base\"; fi; done",
  "description": "Check sync status between docs/paper/ and paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "86b948e8-1f17-431b-951b-b59627232e28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtZhD1hg5SHdHYWAeEdYHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16133,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16133
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

_source line 10 · 2026-05-22T12:05:41.974Z_

<details><summary>↩ Tool result · `toolu_01UHPY2bFaHnjs3pmGhSqyhH`</summary>

```text
DIFFER: main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "adc2ce05-3cb6-48dc-8a46-d6334e145cec",
  "tool_use_result": {
    "stdout": "DIFFER: main.tex",
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

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_01JtRhMfeFcDSmyCudhj6jiq`</summary>

```json
{
  "command": "diff -rq docs/paper/figures/ paper/figures/ 2>/dev/null | head -20",
  "description": "Check figures sync status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "bf04c20d-f745-428a-9967-b39f4baf18ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtZhD1hg5SHdHYWAeEdYHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16133,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16133
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

_source line 12 · 2026-05-22T12:05:42.467Z_

<details><summary>↩ Tool result · `toolu_01JtRhMfeFcDSmyCudhj6jiq`</summary>

```text
Files docs/paper/figures/fig4_prolog_comparison.pdf and paper/figures/fig4_prolog_comparison.pdf differ
Files docs/paper/figures/fig4_prolog_comparison.png and paper/figures/fig4_prolog_comparison.png differ
Files docs/paper/figures/fig5_training_isr_curves.pdf and paper/figures/fig5_training_isr_curves.pdf differ
Files docs/paper/figures/fig5_training_isr_curves.png and paper/figures/fig5_training_isr_curves.png differ
Files docs/paper/figures/gen_fig4.py and paper/figures/gen_fig4.py differ
Files docs/paper/figures/gen_fig5.py and paper/figures/gen_fig5.py differ
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "e1389cdb-255d-41bd-bc93-09071a2348ab",
  "tool_use_result": {
    "stdout": "Files docs/paper/figures/fig4_prolog_comparison.pdf and paper/figures/fig4_prolog_comparison.pdf differ\nFiles docs/paper/figures/fig4_prolog_comparison.png and paper/figures/fig4_prolog_comparison.png differ\nFiles docs/paper/figures/fig5_training_isr_curves.pdf and paper/figures/fig5_training_isr_curves.pdf differ\nFiles docs/paper/figures/fig5_training_isr_curves.png and paper/figures/fig5_training_isr_curves.png differ\nFiles docs/paper/figures/gen_fig4.py and paper/figures/gen_fig4.py differ\nFiles docs/paper/figures/gen_fig5.py and paper/figures/gen_fig5.py differ",
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

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the findings:

**Task 1A: 8B results in appendix**
The appendix has a complete section `\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}` at `\label{app:8b-results}` (line 729). It contains:
- K=8 exec-only s42: PR=14%, ISR*=0.573, genuine=92.9% (13/14), CE=1 ✓
- K=4 stagnation mentioned (line 767) ✓
- K=8 also not converged ✓


- Training details about zero gradient signal ✓

The data matches what was requested. The requested metrics are all present—PR at 14%, ISR* at 0.573, and genuine accuracy at 92.9%—while the narrative covers the cold-start stagnation and zero GRPO advantage that explain the underlying training dynamics.

Now I'm checking the limitations section for the 8B model caveat, starting at line 4 where it mentions neither Qwen3-8B nor LLaMA-3.2...

The statement correctly captures that the 8B models don't converge under the GRPO configuration and that cross-scale generalization remains untested, which aligns with the appendix references. This is consistent with the earlier findings.

Moving on to sync the files—only main.tex has differences among the LaTeX and bibliography files, along with some figure variations related to fig4 and fig5. Let me identify what changed in main.tex and proceed with the synchronization and compilation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "f2439649-4afd-4702-8e73-f0d121be5108",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8YJvuWyG1PFa1W1JmsAjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21241,
      "cache_read_input_tokens": 27974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21241
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

**Task 1A**: Appendix `app:8b-results` (line 729) is complete — PR=14%, ISR*=0.573, genuine=92.9%, CE=1, K=4 stagnation, K=8 non-convergence all present. No changes needed.

**Task 1B**: Limitations (line 4) correctly states "neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration" with appendix refs. Consistent.

**Task 2**: Only `main.tex` differs among .tex/.bib. Figures: fig4 and fig5 (pdf/png/gen_*.py) differ. Let me check the main.tex diff, then sync and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "5715754a-880d-4441-8589-df3bbccc873d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8YJvuWyG1PFa1W1JmsAjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21241,
      "cache_read_input_tokens": 27974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21241
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

<details open><summary>🔧 Tool call — Bash · `toolu_01TAB4SEoKwe6hqFfjmiCadz`</summary>

```json
{
  "command": "diff docs/paper/main.tex paper/main.tex | head -60",
  "description": "Check main.tex differences"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "06332327-15a6-4482-bd54-b26c84888c59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8YJvuWyG1PFa1W1JmsAjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21241,
      "cache_read_input_tokens": 27974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21241
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

_source line 16 · 2026-05-22T12:06:09.666Z_

<details><summary>↩ Tool result · `toolu_01TAB4SEoKwe6hqFfjmiCadz`</summary>

```text
12,13d11
< \usepackage{float}
< \usepackage{placeins}
44a43,44
> 
> \input{checklist}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "8443a408-37ac-4a65-9347-9040b9ea7484",
  "tool_use_result": {
    "stdout": "12,13d11\n< \\usepackage{float}\n< \\usepackage{placeins}\n44a43,44\n> \n> \\input{checklist}",
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
The differences in main.tex:
1. `docs/paper/main.tex` has `\usepackage{float}` and `\usepackage{placeins}` that `paper/main.tex` doesn't
2. `paper/main.tex` has `\input{checklist}` that `docs/paper/main.tex` doesn't

The appendix uses `\FloatBarrier` (line 670) and `[H]` float placement (line 735), which require `float` and `placeins` packages. So docs/paper/main.tex is the correct source. Let me sync.


But wait — the user wants me to overwrite paper/ with docs/paper/, yet paper/main.tex includes a checklist input that docs/paper/main.tex doesn't have. If that checklist is needed for the ARR submission, removing it could be problematic. I should verify whether checklist.tex exists in docs/paper/ before proceeding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "ab2a43cf-d726-4e51-9dab-b9a56431429d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxsrinRP7fNgMEiUFfnGq8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 49215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1059
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

`main.tex` diff: docs/paper has `\usepackage{float}` + `\usepackage{placeins}` (needed for `[H]` and `\FloatBarrier` in appendix); paper/ has `\input{checklist}` which docs/paper doesn't. Let me check if checklist.tex exists in docs/paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "5ae588a1-1898-4053-b208-005464f1773f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxsrinRP7fNgMEiUFfnGq8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 49215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1059
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Wd3RXfJCxKRMGThWAW6c7T`</summary>

```json
{
  "command": "ls -la docs/paper/checklist.tex paper/checklist.tex 2>&1",
  "description": "Check checklist.tex existence in both dirs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "f2b45bb5-70aa-4b7b-b4af-565a1b903b97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxsrinRP7fNgMEiUFfnGq8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 49215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1059
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

_source line 20 · 2026-05-22T12:06:22.753Z_

<details><summary>↩ Tool result · `toolu_01Wd3RXfJCxKRMGThWAW6c7T`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 4277 May 20 19:15 docs/paper/checklist.tex
-rw-r--r-- 1 ubuntu ubuntu 4277 May 22 11:53 paper/checklist.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "099f2013-c36b-47b1-bee6-755043b42c0a",
  "tool_use_result": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 4277 May 20 19:15 docs/paper/checklist.tex\n-rw-r--r-- 1 ubuntu ubuntu 4277 May 22 11:53 paper/checklist.tex",
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

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Both have checklist.tex. The issue is that docs/paper/main.tex doesn't have `\input{checklist}` while paper/main.tex does. For ACL ARR submission, the checklist should be included. But the user says docs/paper/ is the authoritative source. 

I think the best approach is: copy docs/paper/main.tex to paper/main.tex, but then add the missing `\input{checklist}` and also keep the float/placeins packages. Actually wait, docs/paper already has float and placeins. The only thing paper/ has that docs/paper/ doesn't is `\input{checklist}`.
 
Wait, I'm reading the diff backwards. Looking at it again, docs/paper/main.tex actually has the float and placeins packages on lines 12-13, but paper/main.tex doesn't have them. And paper/main.tex has the checklist input on lines 43-44, but docs/paper/main.tex is missing that. So docs/paper/ is missing the checklist while paper/ is missing the float and placeins packages.

But hold on—the user's documentation says the checklist is supposed to be filled out manually in the OpenReview submission form, not embedded in the PDF itself. So maybe having `\input{checklist}` in paper/main.tex is actually incorrect, or it's just there for internal reference. Let me think about what the actual source of truth should be here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "25c8837c-3125-4d8f-97b7-917544a18b6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BedNhZY8dx3Jgrcw9FFCyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 50274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 555
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

_source line 22_

The CLAUDE.md says "ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面" — so `\input{checklist}` in paper/main.tex may be intentional for review but isn't required in the PDF. I'll sync docs/paper → paper (which drops checklist from main.tex) since the checklist is filled on OpenReview, not in the PDF. Let me also check if the float/placeins packages are needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "23bd76a4-2b53-4365-b0ba-630578f2240d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BedNhZY8dx3Jgrcw9FFCyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 50274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 555
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

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01CrLrwx2wVncNSvngwSZgKX`</summary>

```json
{
  "command": "cp docs/paper/main.tex paper/main.tex && cp docs/paper/figures/fig4_prolog_comparison.pdf paper/figures/fig4_prolog_comparison.pdf && cp docs/paper/figures/fig4_prolog_comparison.png paper/figures/fig4_prolog_comparison.png && cp docs/paper/figures/fig5_training_isr_curves.pdf paper/figures/fig5_training_isr_curves.pdf && cp docs/paper/figures/fig5_training_isr_curves.png paper/figures/fig5_training_isr_curves.png && cp docs/paper/figures/gen_fig4.py paper/figures/gen_fig4.py && cp docs/paper/figures/gen_fig5.py paper/figures/gen_fig5.py && echo \"SYNC DONE\"",
  "description": "Sync docs/paper/ to paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "29ec8e10-ff3c-4f83-9d52-f8a4edcf51eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BedNhZY8dx3Jgrcw9FFCyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 50274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 555
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

_source line 24 · 2026-05-22T12:06:59.369Z_

<details><summary>↩ Tool result · `toolu_01CrLrwx2wVncNSvngwSZgKX`</summary>

```text
SYNC DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "05e91d24-6a7b-4d1f-98b9-b307b0573ab3",
  "tool_use_result": {
    "stdout": "SYNC DONE",
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

Now verify sync is clean, then compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "3688a95e-b501-42db-9a60-3edea702f63f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qt5aFcFE18izM63HaE8n1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 50829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1042
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

<details open><summary>🔧 Tool call — Bash · `toolu_01QRAv6QvJpzLiqddnCbSwyd`</summary>

```json
{
  "command": "for f in docs/paper/*.tex docs/paper/*.bib; do base=$(basename \"$f\"); if [ -f \"paper/$base\" ]; then if ! diff -q \"$f\" \"paper/$base\" > /dev/null 2>&1; then echo \"STILL DIFFER: $base\"; fi; fi; done && diff -rq docs/paper/figures/ paper/figures/ 2>/dev/null | head -20; echo \"VERIFY DONE\"",
  "description": "Verify sync is clean"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "e582a4fb-8775-468f-993b-dbc83ddbedab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qt5aFcFE18izM63HaE8n1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 50829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1042
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

_source line 27 · 2026-05-22T12:07:06.955Z_

<details><summary>↩ Tool result · `toolu_01QRAv6QvJpzLiqddnCbSwyd`</summary>

```text
VERIFY DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "e3263175-0d22-452c-bb5d-ec63dc6eda7e",
  "tool_use_result": {
    "stdout": "VERIFY DONE",
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

_source line 28_

Sync clean. Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "89022b3c-32ee-42f9-b056-8470b4a14b9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNGfpRdzCWeuXEQsw1Kukf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 51871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 204
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

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01QyVDGX3HDNTB6nxmrvrMMp`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper",
  "timeout": 180000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "cf47555f-ddd7-4399-b6b1-3cce7061ee05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNGfpRdzCWeuXEQsw1Kukf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 51871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 204
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

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "boqsw021w",
  "tool_use_id": "toolu_01QyVDGX3HDNTB6nxmrvrMMp",
  "description": "Compile LaTeX paper",
  "task_type": "local_bash",
  "uuid": "8efb8061-9c00-4ff6-8bb4-bf180e24a2d7",
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c"
}
```

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "boqsw021w",
  "tool_use_id": "toolu_01QyVDGX3HDNTB6nxmrvrMMp",
  "status": "completed",
  "output_file": "",
  "summary": "Compile LaTeX paper",
  "uuid": "af3b34bf-e594-4a18-b493-26df56219b4e",
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c"
}
```

---

### Tool result

_source line 32 · 2026-05-22T12:07:15.311Z_

<details><summary>↩ Tool result · `toolu_01QyVDGX3HDNTB6nxmrvrMMp`</summary>

```text
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/helvetic/uhvb8a.pfb>
Output written on main.pdf (22 pages, 587741 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
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
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "8c6dd43a-5bea-4702-8fd8-b027fb812aa9",
  "tool_use_result": {
    "stdout": "sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/helvetic/uhvb8a.pfb>\nOutput written on main.pdf (22 pages, 587741 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 33_

Compilation succeeded (22 pages). Now running all checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "0d167879-c61a-460f-9496-a6cce49543e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cwkwqaE6tb572t2DmQ3P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 997,
      "cache_read_input_tokens": 52075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 997
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

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_015JVjjFpHjPQzp5d5C3HPWZ`</summary>

```json
{
  "command": "pdfinfo main.pdf | grep Pages",
  "description": "Check total page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "41c92a6f-3865-403f-abe8-1409e0f2d216",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cwkwqaE6tb572t2DmQ3P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 997,
      "cache_read_input_tokens": 52075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 997
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

_source line 35 · 2026-05-22T12:07:23.539Z_

<details><summary>↩ Tool result · `toolu_015JVjjFpHjPQzp5d5C3HPWZ`</summary>

```text
Pages:           22
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "720d3132-e254-473b-bc67-02619efb031f",
  "tool_use_result": {
    "stdout": "Pages:           22",
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

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_014tfQbBqKUccz7NJEvQsBWJ`</summary>

```json
{
  "command": "grep -i \"undefined\" main.log | head -20",
  "description": "Check undefined references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "ff2d88a1-dd33-46c9-a034-ca84f3b1e356",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cwkwqaE6tb572t2DmQ3P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 997,
      "cache_read_input_tokens": 52075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 997
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

_source line 37 · 2026-05-22T12:07:24.013Z_

<details><summary>↩ Tool result · `toolu_014tfQbBqKUccz7NJEvQsBWJ`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "b40468a5-bc1a-475d-80f8-80812d21f184",
  "tool_use_result": {
    "stdout": "",
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01YDQeX7ycMBDeKt8v8mbT13`</summary>

```json
{
  "command": "grep -i \"citation.*undefined\" main.log | head -20",
  "description": "Check missing citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "5f40291b-8055-44b6-b371-387452d0e742",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cwkwqaE6tb572t2DmQ3P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 997,
      "cache_read_input_tokens": 52075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 997
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

_source line 39 · 2026-05-22T12:07:24.938Z_

<details><summary>↩ Tool result · `toolu_01YDQeX7ycMBDeKt8v8mbT13`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "8e941053-33e6-401e-bcf3-7c306dd21fa4",
  "tool_use_result": {
    "stdout": "",
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

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_01VJRb1pzqFo6ebpzEy8Cd6C`</summary>

```json
{
  "pattern": "—|---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "bd864903-445b-453a-ae58-7411dc344625",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cwkwqaE6tb572t2DmQ3P2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 997,
      "cache_read_input_tokens": 52075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 997
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

_source line 41 · 2026-05-22T12:07:26.356Z_

<details><summary>↩ Tool result · `toolu_01VJRb1pzqFo6ebpzEy8Cd6C`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:56:Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:57:SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:59:Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (PG corrected)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:141:PG prem-subset & 6  & 5  & 8   & 0 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:142:Tautological   & --- & --- & --- & --- & s42 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:143:Repetition     & s43 & --- & --- & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:144:Contradiction  & 1k & --- & --- & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:145:Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:146:Query-as-fact  & --- & --- & --- & --- & s44 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:1:% Appendix — solver-trace-ablation
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:108:\paragraph{What ISR measures---and what it does not.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:239:\subsection{PG --- Premise-Subset Gaming}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:264:\subsection{CE --- Conclusion Embedding}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:290:\subsection{TSa --- Conclusion Duplication (Standard)}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:318:\subsection{TSb --- Obfuscated Tautology}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:480:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:492:  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:494:  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:503:  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:506:  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:555:\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:563:  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:564:  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:565:  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:595:Base & --- & 0.16 & 0.310 & 0 & 0 & \textbf{100} & $n{=}16$ proved \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:757:8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "d68c1c31-81ac-4af3-8ff5-9b1c1e3ae441",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:56:Base (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:57:SFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:59:Exec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:141:PG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:142:Tautological   & --- & --- & --- & --- & s42 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:143:Repetition     & s43 & --- & --- & --- & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:144:Contradiction  & 1k & --- & --- & --- & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:145:Cmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:146:Query-as-fact  & --- & --- & --- & --- & s44 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:1:% Appendix — solver-trace-ablation\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:108:\\paragraph{What ISR measures---and what it does not.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:239:\\subsection{PG --- Premise-Subset Gaming}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:264:\\subsection{CE --- Conclusion Embedding}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:290:\\subsection{TSa --- Conclusion Duplication (Standard)}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:318:\\subsection{TSb --- Obfuscated Tautology}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:480:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:492:  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:494:  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:503:  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:506:  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:555:\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:563:  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:564:  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:565:  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:595:Base & --- & 0.16 & 0.310 & 0 & 0 & \\textbf{100} & $n{=}16$ proved \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:757:8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\\\",
    "numLines": 26
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Let me check where the main text ends and references begin - need to verify the 8-page limit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "e5ca9e98-716d-4a12-bfff-89b301e3dddc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACtCEDXGepzGtQeFosqRHn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2311,
      "cache_read_input_tokens": 53072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2311
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

_source line 43_

Now let me check where the main text ends (page limit compliance).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "4289e853-62cc-4046-ac52-82a9e7ebf6e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACtCEDXGepzGtQeFosqRHn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2311,
      "cache_read_input_tokens": 53072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2311
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

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01BsUPzUejhqeDPZR1BMDWhR`</summary>

```json
{
  "command": "pdftotext main.pdf - 2>/dev/null | grep -n \"References\\|\\\\\\\\bibliography\\|Limitations\" | head -10",
  "description": "Find where References/Limitations sections start in PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "4086a896-b429-4c72-bed5-ca32b07f1342",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACtCEDXGepzGtQeFosqRHn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2311,
      "cache_read_input_tokens": 53072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2311
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

_source line 45 · 2026-05-22T12:07:35.136Z_

<details><summary>↩ Tool result · `toolu_01BsUPzUejhqeDPZR1BMDWhR`</summary>

```text
650:Limitations of ISR. ISR captures component necessity, not semantic faithfulness; it
1447:Limitations
1491:References
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "c15734eb-0101-49ce-9cc6-265f7a0d58e2",
  "tool_use_result": {
    "stdout": "650:Limitations of ISR. ISR captures component necessity, not semantic faithfulness; it\n1447:Limitations\n1491:References",
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

<details open><summary>🔧 Tool call — Read · `toolu_013YCtrjopBt6JM72znC1QDW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "8-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "248e55ee-13ba-4910-9513-8073c8048110",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YN55hxxF1EWjWnZ5HkJPf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 309,
      "cache_read_input_tokens": 55383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 309
      },
      "output_tokens": 53,
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

_source line 47 · 2026-05-22T12:07:39.173Z_

<details><summary>↩ Tool result · `toolu_013YCtrjopBt6JM72znC1QDW`</summary>

```text
PDF pages extracted: 3 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf (574KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "8651cd63-c596-47f2-838b-604f18446dde",
  "tool_use_result": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
      "originalSize": 587741,
      "outputDir": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/7e220319-3a29-486a-91e1-6f6e9b6cc54c/tool-results/pdf-09ef53d2-5d56-4987-ad6c-908cdb435da2",
      "count": 3
    }
  }
}
```

</details>

---

## Round 1

1 recorded events

### User

_source line 48 · 2026-05-22T12:07:39.171Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "6adc2a6f-3201-40dd-99c5-000000000000",
  "isSynthetic": true
}
```

</details>

---

## Round 2

1 recorded events

### User

_source line 49 · 2026-05-22T12:07:39.171Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "6adc2a6f-3201-40dd-99c5-000000000001",
  "isSynthetic": true
}
```

</details>

---

## Round 3

4 recorded events

### User

_source line 50 · 2026-05-22T12:07:39.171Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "6adc2a6f-3201-40dd-99c5-000000000002",
  "isSynthetic": true
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
From the PDF, I can see:
- Page 8: Limitations section ends, Ethics Statement (§7) ends, References begin on page 8
- Page 9-10: More references
- Page 10: Appendix A starts at the bottom

So the main text (§1-§7 including Ethics and Limitations) fits within 8 pages. References start on page 8. The appendix starts on page 10.

Let me verify: the main text content ends with Ethics Statement on page 8 (line 562: "man subjects are involved."), then References start at line 563 on the same page 8.

The EMNLP rule says: "8-page limit for main text, with unlimited space for references. 

Mandatory limitations and optional ethical considerations do not count towards this page limit." So Limitations and Ethics don't count. The main text (§1-5) needs to be within 8 pages. I need to check where the Conclusion ends versus where Limitations begins to understand the actual page count for the countable sections.

Looking at the PDF, I can see the Limitations section starts around line 539, followed by the Ethics Statement at line 548, with References beginning at line 563. This means the main numbered sections must conclude before the Limitations section starts. Let me identify which sections are actually included in this paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "3016111d-a12e-4ec5-b5cf-a75a363656f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mfmV2y9F6jTs5x5xCGdUd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3958,
      "cache_read_input_tokens": 55692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3958
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

_source line 52_

Results summary:

**1. 8B appendix** (`app:8b-results`, line 729): Complete. PR=14%, ISR*=0.573, genuine=92.9%, CE=1, K=4 stagnation, K=8 non-convergence — all present. No changes needed.

**2. Limitations 8B caveat** (line 4): Consistent — "neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration" with correct appendix refs.

**3. Sync status**: 
- .tex/.bib files: only `main.tex` differed (docs/paper had float/placeins packages; paper/ had `\input{checklist}` which per CLAUDE.md belongs on OpenReview, not in PDF). Synced docs/paper → paper.
- Figures: fig4, fig5 (pdf/png/gen_*.py) differed. Synced.
- Now clean — zero diffs.

**4. Compilation**: Success.
- Total pages: **22**
- Main text (§1-5) ends on page 8, References start on page 8 — **within 8-page limit** (Limitations + Ethics don't count per EMNLP rules)
- Appendix starts page 10
- **Undefined references: 0**
- **Missing citations: 0**

**5. Em-dash check**: All `---` occurrences are legitimate LaTeX em-dashes (used as "N/A" markers in tables like `--- & 12 & ---`) or standard LaTeX triple-dash em-dashes in section headers (e.g., `"What ISR measures---and what it does not"`). The Unicode em-dash `—` appears only in a comment line (`% Appendix — solver-trace-ablation`). No issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "uuid": "74486408-0248-4703-8803-1a17d4425a02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mfmV2y9F6jTs5x5xCGdUd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3958,
      "cache_read_input_tokens": 55692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3958
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

### Task result

_source line 53_

Results summary:

**1. 8B appendix** (`app:8b-results`, line 729): Complete. PR=14%, ISR*=0.573, genuine=92.9%, CE=1, K=4 stagnation, K=8 non-convergence — all present. No changes needed.

**2. Limitations 8B caveat** (line 4): Consistent — "neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration" with correct appendix refs.

**3. Sync status**: 
- .tex/.bib files: only `main.tex` differed (docs/paper had float/placeins packages; paper/ had `\input{checklist}` which per CLAUDE.md belongs on OpenReview, not in PDF). Synced docs/paper → paper.
- Figures: fig4, fig5 (pdf/png/gen_*.py) differed. Synced.
- Now clean — zero diffs.

**4. Compilation**: Success.
- Total pages: **22**
- Main text (§1-5) ends on page 8, References start on page 8 — **within 8-page limit** (Limitations + Ethics don't count per EMNLP rules)
- Appendix starts page 10
- **Undefined references: 0**
- **Missing citations: 0**

**5. Em-dash check**: All `---` occurrences are legitimate LaTeX em-dashes (used as "N/A" markers in tables like `--- & 12 & ---`) or standard LaTeX triple-dash em-dashes in section headers (e.g., `"What ISR measures---and what it does not"`). The Unicode em-dash `—` appears only in a comment line (`% Appendix — solver-trace-ablation`). No issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 158053,
  "duration_api_ms": 154940,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "7e220319-3a29-486a-91e1-6f6e9b6cc54c",
  "total_cost_usd": 0.6557742500000001,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 47809,
    "cache_read_input_tokens": 458226,
    "output_tokens": 4944,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 47809,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 767,
        "cache_read_input_tokens": 55692,
        "cache_creation_input_tokens": 3958,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3958
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 4115,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00419,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 4944,
      "cacheReadInputTokens": 458226,
      "cacheCreationInputTokens": 47809,
      "webSearchRequests": 0,
      "costUSD": 0.6515842500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b2dabd52-d786-49ad-82db-3298cbde986c"
}
```

</details>

---
