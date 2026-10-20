# Research conversation: In the file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex, sear

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9357ac62a46de49c.jsonl`
- **Structured JSON:** [`48c9cacd0f3cec2ab946.json`](../../sessions/48/48c9cacd0f3cec2ab946.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-23T12:53:33.338Z_

In the file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex, search for 1000-step ISR β=0.1 per-seed data for seeds s42, s43, s44, s45, s46. I need to verify these specific N-H (non-hacking) percentages claimed in a figure:
- s42: 6% N-H at 1000 steps
- s43: 2% N-H at 1000 steps
- s44: 0% N-H at 1000 steps
- s45: 55% N-H at 1000 steps
- s46: 55% N-H at 1000 steps

Look for sections mentioning "1000" steps, ISR β=0.1 seed-level breakdown, and any tables that show per-seed non-hacking rates at 1000 steps. Also check if s45/s46 even have 1000-step data or only 500-step data. Search breadth: medium.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ca423cf5-8734-4110-8dbb-7aa294c951c7",
  "agentId": "a9357ac62a46de49c",
  "type": "user",
  "uuid": "ae49ff01-a6df-4485-a51d-de1765a6b8cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T12:53:34.823Z_

I'll search for the specific ISR β=0.1 1000-step per-seed data in the appendix file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae49ff01-a6df-4485-a51d-de1765a6b8cd",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXuWR4pkRhRm6kAA8fE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e2f389e6-1df0-42c4-b4fe-2f2fb324753e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSDb6pT8iHrRBMG2QJacHy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18929,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18929,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 3 · 2026-05-23T12:53:35.090Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HCKEFLJVJKwgZAPjJQ9GPB`</summary>

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
  "parentUuid": "e2f389e6-1df0-42c4-b4fe-2f2fb324753e",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXuWR4pkRhRm6kAA8fE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d72de43e-efce-4505-9d3c-e3475b1cefe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSDb6pT8iHrRBMG2QJacHy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18929,
      "cache_read_input_tokens": 0,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18929
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18929,
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

_source line 4 · 2026-05-23T12:53:35.447Z_

<details><summary>↩ Tool result · `toolu_01HCKEFLJVJKwgZAPjJQ9GPB`</summary>

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
14	\small
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
78	\small
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
121	\label{app:premise-count}
122	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
123	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
124	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
125	Premise-count-matched comparison eliminates the difference ($1.06\times$, McNemar's test $p{=}0.317$; Table~\ref{tab:fol-beta01-detailed}), confirming that the scalar ISR advantage is not statistically significant.
126	This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
127	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
128	Mode composition analysis (CE vs.\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\S\ref{app:hacking-modes}), not on the number of premises in the formalization.
129	
130	\begin{table}[h]
131	\centering
132	\resizebox{\columnwidth}{!}{%
133	\begin{tabular}{@{}llrrrr@{}}
134	\toprule
135	\textbf{Premises} & \textbf{Condition} & \textbf{$N_{\text{proved}}$} & \textbf{CE\%} & \textbf{TS\%} & \textbf{Genuine\%} \\
136	\midrule
137	$\leq$3 & ISR $\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\
138	         & Random $\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\
139	\midrule
140	4--6     & ISR $\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\
141	         & Random $\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\
142	\midrule
143	$\geq$7  & ISR $\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\
144	         & Random $\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\
145	\bottomrule
146	\end{tabular}}
147	\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}
148	\label{tab:premise-bin-modes}
149	\end{table}
150	
151	\begin{table*}[ht]
152	\centering
153	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
154	\label{tab:bootstrap-ci}
155	\small
156	\begin{tabular}{@{}lcccc@{}}
157	\toprule
158	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
159	\midrule
160	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (PG+FN corrected)}} \\
161	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
162	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
163	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
164	\midrule
165	\multicolumn{5}{@{}l}{\textit{TS gaming rate}} \\
166	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
167	\midrule
168	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
169	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
170	\bottomrule
171	\end{tabular}
172	\\[2pt]
173	{\small ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
174	\end{table*}
175	
176	\paragraph{TS dose-response gradient.}
177	TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
178	The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
179	
180	\paragraph{Goodhart effects: implications.}
181	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.
182	The dose-response pattern maps onto the Manheim \& Garrabrant taxonomy~\citep{manheim-goodhart-taxonomy}: $\beta{=}0.1$ on FOLIO instantiates \emph{regressional} Goodhart ($P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR erroneously rewards the shortcut); $\beta{\geq}0.2$ introduces \emph{extremal} elements (PR collapse to 18\% vs.\ 48\% random at $\beta{=}0.3$).
183	The implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \S\ref{sec:crossdomain}).
184	
185	\paragraph{Single-seed unreliability.}
186	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
187	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\S\ref{sec:goodhart}).
188	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
189	
190	\paragraph{Classifier limitations.}
191	Text-match hacking classifiers have systematic blind spots that functional analysis exposes.
192	In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-detailed}).
193	One seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.
194	Practitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.
195	
196	\paragraph{Practical guidelines.}
197	\label{app:practical-guidelines}
198	Our findings yield five guidelines for GRPO-trained neurosymbolic systems:
199	(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.
200	(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\S\ref{sec:diagnostic}).
201	(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.
202	(4)~Treat LOO-based metrics as component-count-biased until normalized.
203	(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.
204	
205	\paragraph{Multiple testing correction.}
206	\label{app:statistical-details}
207	We define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).
208	Within the FOLIO family, Bonferroni correction at $\alpha{=}0.05$ yields adjusted thresholds of $p_{\text{adj}}{=}0.05/14{=}0.0036$.
209	Three primary comparisons survive correction: the TS rate difference (ISR vs.\ random; $p_{\text{bonf}}{=}1.82{\times}10^{-38}$), the SFT vs.\ exec-only non-hacking rate ($p_{\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\text{bonf}}{<}10^{-8}$).
210	The matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\text{bonf}}{=}0.056$), significant at $\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).
211	The ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.
212	Bonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.
213	We report the most conservative Bonferroni results for transparency.
214	
215	\paragraph{Mode distribution $\chi^2$ test.}
216	A pooled $3{\times}2$ contingency table (TS/CE/N-H $\times$ ISR/Random, 3-seed, 500 steps) yields $\chi^2{=}174.8$, $\text{df}{=}2$, $p{=}1.08{\times}10^{-38}$, confirming that ISR reward shifts the overall hacking mode composition, not merely the TS rate.
217	Per-seed tests are individually significant (s42: $\chi^2{=}15.8$, $p{<}0.001$; s43: $\chi^2{=}59.4$, $p{<}10^{-13}$; s44: $\chi^2{=}168.0$, $p{<}10^{-36}$).
218	The previously reported $\text{OR}_{\text{CMH}}{=}2.46$ for TS specifically ($p{<}10^{-8}$) captures a narrower slice of this distributional shift.
219	
220	
221	\section{Hacking Mode Definitions}
222	\label{app:hacking-modes}
223	
224	We identify eight distinct reward hacking modes across all experiments.
225	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
226	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
227	
228	\begin{table*}[ht]
229	\centering
230	\small
231	\begin{tabular}{@{}llcccc@{}}
232	\toprule
233	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
234	\midrule
235	CE & Concl.\ in premises & 87 & 18 & 71 & 7 \\
236	TS & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
237	PG & Premise-subset gaming & 6 & 5 & --- & 0 \\
238	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
239	Repetition & Output degen. & $\bullet$ & --- & --- & --- \\
240	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & --- & --- & --- \\
241	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
242	Q-as-fact & Atom = fact+query & --- & --- & --- & --- \\
243	\bottomrule
244	\end{tabular}
245	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\dagger$Random TS driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: CE${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
246	\label{tab:hacking-taxonomy-app}
247	\end{table*}
248	
249	\paragraph{Classifier Validation.}
250	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
251	CE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
252	No training data or manual annotation is used for classification.
253	
254	To estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
255	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
256	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
257	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
258	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
259	\paragraph{Boundary case validation.}
260	Stratified validation across 82 samples (all five hacking categories) yields Cohen's $\kappa{=}1.0$; independent re-annotation confirms full agreement.
261	Structured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.
262	Short-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.
263	Low-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.
264	3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.
265	
266	\begin{table}[h]
267	\centering
268	\small
269	\begin{tabular}{@{}lcr@{}}
270	\toprule
271	\textbf{Mode} & \textbf{Val.\ $N$} & \textbf{Prec.} \\
272	\midrule
273	CE (Concl.\ Embed.) & 80$^\dagger$ & 1.00 \\
274	TS (Tautological) & 7 & 1.00 \\
275	PG (Premise-Subset) & 20 & 1.00 \\
276	Contradiction & 20 & 1.00 \\
277	Genuine & 25 & 1.00 \\
278	\midrule
279	\textbf{Overall} & \textbf{152} & \textbf{1.00} \\
280	\bottomrule
281	\end{tabular}
282	\caption{Per-mode classifier precision on 152 manually validated samples (stratified + boundary + random; three exercises pooled). $^\dagger$Includes 50 randomly sampled CE$\cup$TS outputs (pool ratio CE:TS${=}$374:2). Recall is not estimable from a validation-only design.}
283	\label{tab:classifier-precision}
284	\end{table}
285	
286	The TS\textsubscript{b} subcategory (functional LOO tautologies undetectable by text matching) provides a lower bound on TS recall: ${\geq}91\%$ ($149/163$) under ISR $\beta{=}0.1$. Other modes' recall is not estimable from the validation-only design; non-hacking rates throughout should be interpreted as upper bounds.
287	
288	\subsection{PG -- Premise-Subset Gaming}
289	\label{app:h8}
290	
291	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).
292	We term this \textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
293	
294	\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
295	Automated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.
296	
297	\paragraph{Audit scope and limitations.}
298	Full PG audit was completed for ISR $\beta{=}0.1$ seed~42 only.
299	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.
300	Random $\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.
301	
302	\paragraph{TS false-negative correction (TSb obfuscated tautology).}
303	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
304	Manual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
305	We classify these as \textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.
306	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\S\ref{sec:taxonomy}).
307	After correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.
308	
309	\paragraph{Impact on non-hacking-rate comparison.}
310	After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
311	The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
312	
313	\subsection{CE -- Conclusion Embedding}
314	
315	\paragraph{Definition.}
316	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
317	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
318	
319	\paragraph{Example (FOL).}
320	\smallskip\noindent\rule{\columnwidth}{0.3pt}
321	{\small\begin{verbatim}
322	Premises:
323	  all x (bird(x) -> flies(x)).
324	  bird(tweety).
325	  flies(tweety).  % conclusion embedded
326	Conclusion: flies(tweety).
327	\end{verbatim}}
328	\noindent\rule{\columnwidth}{0.3pt}\smallskip
329	
330	\paragraph{ISR interaction.}
331	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
332	ISR does not distinguish trivial from substantive necessity.
333	
334	\paragraph{Prevalence.}
335	Conclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\% across all RL conditions.
336	Under exec-only and Random reward, it manifests as CE (71--93\%); under ISR reward, it shifts to TS (70.6\% pooled).
337	
338	
339	\subsection{TSa -- Conclusion Duplication (Standard)}
340	
341	\paragraph{Definition.}
342	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
343	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
344	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
345	
346	\paragraph{Example (FOL).}
347	\smallskip\noindent\rule{\columnwidth}{0.3pt}
348	{\small\begin{verbatim}
349	Premises:
350	  all x ((A(x)&B(x))->(C(x)|D(x))).
351	Conclusion:
352	  all x ((A(x)&B(x))->(C(x)|D(x))).
353	\end{verbatim}}
354	\noindent\rule{\columnwidth}{0.3pt}\smallskip
355	
356	\paragraph{ISR interaction.}
357	ISR~$\approx 0.8$--$1.0$.
358	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
359	TSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.
360	
361	\paragraph{Prevalence.}
362	TSa (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
363	Combined TS (TSa + TSb): 70.6\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).
364	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all TSa; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
365	
366	
367	\subsection{TSb -- Obfuscated Tautology}
368	
369	\paragraph{Definition.}
370	A single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.
371	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
372	
373	\paragraph{Example (FOL, vacuous quantifier wrapping).}
374	\smallskip\noindent\rule{\columnwidth}{0.3pt}
375	{\small\begin{verbatim}
376	Premises:
377	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
378	Conclusion:
379	  all x ((A(x)&B(x))->(C(x)|D(x))).
380	\end{verbatim}}
381	\noindent\rule{\columnwidth}{0.3pt}\smallskip
382	
383	\noindent The premise introduces a vacuous variable $y$, unified with~$x$ at proof time; the formulas are logically equivalent but textually distinct.
384	
385	\paragraph{ISR interaction.}
386	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
387	TSb simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).
388	This triple gaming makes TSb the most complete Goodhart case we observe.
389	
390	\paragraph{Prevalence.}
391	Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
392	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
393	
394	
395	\subsection{Tautological Collapse}
396	
397	\paragraph{Definition.}
398	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
399	
400	\paragraph{Example (FOL).}
401	\smallskip\noindent\rule{\columnwidth}{0.3pt}
402	\begin{verbatim}
403	Premises: p(a).
404	Conclusion: p(a).
405	\end{verbatim}
406	\noindent\rule{\columnwidth}{0.3pt}\smallskip
407	
408	\paragraph{ISR interaction.}
409	ISR~$=1.0$ (the sole premise is necessary).
410	Distinguished from TS by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
411	
412	\paragraph{Prevalence.}
413	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% TS by strict classifier).
414	Also observed in Prolog exec+STA seed~42 (100\% TS, PR~$=0.50$).
415	
416	
417	\subsection{Repetition Collapse}
418	
419	\paragraph{Definition.}
420	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
421	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
422	
423	\paragraph{Example (Prolog).}
424	\smallskip\noindent\rule{\columnwidth}{0.3pt}
425	\begin{verbatim}
426	penguin(fido).
427	penguin(fido).
428	penguin(fido).
429	... (repeated to 512 tokens)
430	query(penguin(fido)).
431	\end{verbatim}
432	\noindent\rule{\columnwidth}{0.3pt}\smallskip
433	
434	\paragraph{ISR interaction.}
435	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
436	ISR correctly diagnoses this degeneration.
437	
438	\paragraph{Prevalence.}
439	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
440	
441	
442	\subsection{Complexity-without-Utility}
443	
444	\paragraph{Definition.}
445	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.
446	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
447	
448	\paragraph{Example (FOL).}
449	\smallskip\noindent\rule{\columnwidth}{0.3pt}
450	{\small\begin{verbatim}
451	Premises:
452	  all x all y (R(x,y) ->
453	    exists z (S(x,z) & T(z,y))).
454	  all x (P(x) -> Q(x)).
455	  P(a).            % only this needed
456	Conclusion: Q(a).
457	\end{verbatim}}
458	\noindent\rule{\columnwidth}{0.3pt}\smallskip
459	
460	\paragraph{ISR interaction.}
461	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
462	This is the mode ISR is best calibrated for.
463	
464	\paragraph{Prevalence.}
465	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
466	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
467	
468	
469	\subsection{Contradiction Explosion}
470	
471	\paragraph{Definition.}
472	The component count grows unboundedly over training.
473	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
474	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
475	
476	\paragraph{Example (FOL, 1000-step exec-only).}
477	\smallskip\noindent\rule{\columnwidth}{0.3pt}
478	{\small\begin{verbatim}
479	Premises:
480	  c1. c2. c3. ... c18. % 18.55 mean
481	  % conclusion embedded among premises
482	Conclusion: Q(a).
483	\end{verbatim}}
484	\noindent\rule{\columnwidth}{0.3pt}\smallskip
485	
486	\paragraph{ISR interaction.}
487	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
488	
489	\paragraph{Prevalence.}
490	Observed in extended exec-only training (seed~42, 1000 steps).
491	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
492	
493	
494	\subsection{Query-as-Fact Gaming}
495	
496	\paragraph{Definition.}
497	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
498	Prolog trivially proves the query by unifying with the fact.
499	This mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.
500	
501	\paragraph{Example (Prolog).}
502	\smallskip\noindent\rule{\columnwidth}{0.3pt}
503	\begin{verbatim}
504	% NL: "Fido is happy."
505	% Model output:
506	fido_is_happy.
507	:- fido_is_happy.     % query = fact
508	\end{verbatim}
509	\noindent\rule{\columnwidth}{0.3pt}\smallskip
510	
511	\paragraph{ISR interaction.}
512	ISR~$\approx 0.9$--$1.0$.
513	The single fact is trivially necessary (its removal breaks the query), inflating ISR.
514	Functionally equivalent to TS but with a distinct surface mechanism.
515	
516	\paragraph{Prevalence.}
517	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
518	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
519	
520	
521	\section{Per-Seed Detailed Results}
522	\label{app:detailed-results}
523	
524	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
525	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
526	ISR values are proved-only ISR$^*$.
527	
528	\begin{table*}[t]
529	\centering
530	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\times}2$ vs.\ $2{\times}4$, mathematically equivalent).}
531	\label{tab:fol-detailed}
532	\label{tab:fol-beta01-detailed}
533	\small
534	\setlength{\tabcolsep}{3pt}
535	\resizebox{\textwidth}{!}{%
536	\begin{tabular}{@{}llccccccl@{}}
537	\toprule
538	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
539	\midrule
540	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
541	Base model (no training)
542	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
543	Ground-truth FOL
544	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
545	SFT
546	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
547	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
548	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
549	\cmidrule(l){2-9}
550	  & \multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \textbf{92.3} & $n{=}39$ proved \\
551	\midrule
552	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
553	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
554	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\%$ \\
555	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
556	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
557	  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\
558	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
559	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & PG${=}15\%$ \\
560	\cmidrule(l){2-9}
561	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.68{\pm}0.47$ & $0.238{\pm}0.30$ & & & & 500-step \\
562	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.02$ & $0.029{\pm}0.05$ & & & $2.1{\pm}3.6$ & 1000-step \\
563	\midrule
564	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
565	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed CE+TS+PG \\
566	  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\
567	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\
568	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\
569	  & 45$^\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \textbf{54.8} & PG${=}1$; $n{=}42$ \\
570	  & 46$^\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \textbf{54.5} & PG${=}4$; $n{=}77$ \\
571	\cmidrule(l){2-9}
572	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.77{\pm}0.14$ & $0.716{\pm}0.26$ & & & & 500-step (s42--44) \\
573	  & \multicolumn{2}{l}{5-seed mean$\pm$std} & $0.70{\pm}0.19$ & $0.633{\pm}0.23$ & & & & 500-step (s42--46) \\
574	\midrule
575	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
576	  & \multicolumn{8}{l}{See Table~\ref{tab:beta03-detailed} for per-seed $\beta{=}0.3$ results.} \\
577	\midrule
578	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
579	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\
580	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\
581	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\cap$PG: 6) \\
582	\cmidrule(l){2-9}
583	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.87{\pm}0.08$ & $0.117{\pm}0.042$ & & & & TS seed-dep.: 0/38/0\% \\
584	\midrule
585	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
586	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
587	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
588	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
589	\cmidrule(l){2-9}
590	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & & \\
591	\midrule
592	\multicolumn{9}{@{}l}{\textit{Shuffled-ISR $\beta{=}0.1$ (deconfounding control)}} \\
593	  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
594	  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \textbf{87.5} & $n{=}16$ proved \\
595	  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
596	\cmidrule(l){2-9}
597	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.153{\pm}0.006$ & $0.559{\pm}0.015$ & $6.5$ & $6.5$ & \textbf{87.0} & $N{=}46$ proved \\
598	\bottomrule
599	\end{tabular}}% end resizebox
600	\end{table*}
601	
602	\begin{table*}[t]
603	\centering
604	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
605	\label{tab:prolog-detailed}
606	\small
607	\begin{tabular}{@{}llcccccl@{}}
608	\toprule
609	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
610	\midrule
611	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
612	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
613	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
614	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
615	\cmidrule(l){2-8}
616	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.53{\pm}0.31$ & $0.146{\pm}0.21$ & & & \\
617	\midrule
618	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
619	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & TS tautological \\
620	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional TS$^a$ \\
621	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
622	\cmidrule(l){2-8}
623	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.62{\pm}0.31$ & $0.699{\pm}0.45$ & & & 3/3 Goodhart, 0\% non-hacking \\
624	\bottomrule
625	\end{tabular}
626	
627	\vspace{4pt}
628	{\small
629	$^a$ Strict TS classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
630	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\
631	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
632	}
633	\end{table*}
634	
635	\begin{table*}[t]
636	\centering
637	\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\S\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\text{f50}}{>}0.90$.}
638	\label{tab:prooffol-detailed}
639	\small
640	\begin{tabular}{@{}llcccccl@{}}
641	\toprule
642	\textbf{Condition} & \textbf{Seed} & \textbf{PR$_{\text{f50}}$} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{Genuine\%} & \textbf{Notes} \\
643	\midrule
644	Base & --- & 0.16 & 0.310 & 0 & 0 & \textbf{100} & $n{=}16$ proved \\
645	\midrule
646	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
647	  & 42 & ${\approx}$1.0 & 0.066 & \textbf{100} & 0 & 0 & $n{=}99$; stable \\
648	  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\
649	  & 44 & ${\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\
650	\cmidrule(l){2-8}
651	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{17.4\% genuine (mean of seeds)} & \\
652	\midrule
653	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
654	  & 42 & 0.35 & 0.12 & 0 & 0 & \textbf{100} & $n{=}46$; collapsed \\
655	  & 43 & ${\approx}$0.47 & ${\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\
656	  & 44 & 0.49 & 0.145 & 0 & 0 & \textbf{100} & $n{=}66$; oscillation \\
657	\cmidrule(l){2-8}
658	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{\textbf{76.8\%} genuine (mean of seeds)} & \\
659	\bottomrule
660	\end{tabular}
661	
662	\vspace{4pt}
663	{\small Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}
664	\end{table*}
665	
666	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
667	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
668	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
669	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.
670	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
671	
672	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
673	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
674	seed~42 produces clean TS tautologies (single premise~$=$~conclusion),
675	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
676	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
677	The diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
678	
679	\subsection{Per-Seed Results at $\beta{=}0.2$ and $\beta{=}0.3$}
680	\label{app:beta03}
681	
682	Table~\ref{tab:beta03-detailed} reports per-seed results for ISR at $\beta{=}0.2$ and both ISR and Random at $\beta{=}0.3$.
683	At $\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\% or near-100\% TS), confirming $\beta{\geq}0.2$ as the extremal Goodhart regime.
684	The three ISR $\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
685	
686	\begin{table*}[ht]
687	\centering
688	\caption{Per-seed results at $\beta{=}0.2$ and $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}
689	\label{tab:beta03-detailed}
690	\small
691	\begin{tabular}{@{}llcccccl@{}}
692	\toprule
693	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Mode} \\
694	\midrule
695	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.2$}} \\
696	  & 42 & 1.00 & 0.602 & \textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\
697	  & 43 & 0.96 & 0.552 & \textbf{96.9} & 1.0 & 0 & PG${=}2$ \\
698	  & 44 & 0.94 & 0.964 & \textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\
699	\cmidrule(l){2-8}
700	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.03$ & $0.71{\pm}0.22$ & & & 3/3 TS Goodhart \\
701	\midrule
702	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
703	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\
704	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\
705	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure TS Goodhart \\
706	\cmidrule(l){2-8}
707	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.66{\pm}0.42$ & $0.39{\pm}0.31$ & & & \\
708	\midrule
709	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
710	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\
711	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
712	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
713	\cmidrule(l){2-8}
714	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & \\
715	\bottomrule
716	\end{tabular}
717	\end{table*}
718	
719	\FloatBarrier
720	
721	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
722	\label{app:100step}
723	
724	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%, higher than SFT (13.0\%, 3-seed pooled) but still early in training.
725	Of the 32 proved samples, 9 (28.1\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
726	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
727	This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
728	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
729	
730	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
731	\label{app:o1-ablation}
732	
733	All main experiments (\S\ref{sec:diagnostic}--\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\texttt{execution\_fast\_sta}) but is used only in the ablation reported here.
734	The two signals measure fundamentally different properties, not approximations of the same quantity.
735	The binary signal tests \emph{collective} premise necessity: $\text{fast\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
736	LOO tests \emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.
737	
738	\paragraph{Evaluation-time comparison.}
739	Across 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.
740	This renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.
741	By contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.
742	Of 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.
743	
744	\paragraph{Training-time ablation.}
745	As a training reward ($r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$, functionally zero, compared to $\text{ISR}^*{=}0.132$ under exec-only and $\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\beta{=}0.1$.
746	The tautology check depresses prove rate by 30\,pp relative to exec-only ($63\%$ vs.\ $93\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.
747	That even the fine-grained $O(n)$ LOO signal, which \emph{does} provide per-component necessity feedback, is ultimately gamed (\S\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.
748	
749	\paragraph{Computational overhead.}
750	Full LOO requires $n{+}1$ solver calls per sample (mean $n{\approx}6$ for FOLIO).
751	With Prover9 at ${\sim}5$\,ms per call, STA evaluation adds ${\sim}55$\,ms per sample versus ${\sim}4$\,s for LLM inference (${<}1\%$ overhead).
752	The $O(1)$ binary check adds a single solver call per proved sample (${<}2\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.
753	
754	\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}
755	\label{app:llama-coldstart}
756	
757	We applied the identical GRPO configuration (Table~\ref{tab:hyperparams}) to LLaMA-3.2-3B~\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).
758	Across 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\footnote{This run was also affected by a generation-termination configuration issue (dual EOS tokens); the zero prove rate reflects both the base model's lack of FOL generation capability and truncated outputs.}
759	This establishes a \emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.
760	Qwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\ 4B), likely reflecting pretraining data composition.
761	An SFT warmstart (3 epochs on gold formalizations, lr$=$2$\times$10$^{-5}$) achieves $\text{PR}{=}16\%$ ($n{=}100$) after correcting the generation-termination issue.
762	However, the model produces Unicode FOL notation ($\forall$, $\to$, $\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data; the 16\% prove rate reflects Prover9's partial Unicode tolerance rather than correct format adherence.
763	Subsequent GRPO runs (exec-only, 500 steps from SFT warmstart, 3 seeds) fail to improve beyond SFT baseline ($\text{PR}{=}15.0{\pm}1.0\%$, $n{=}14$--$16$ proved per seed), yet produce no structural degeneration: $86.6{\pm}0.9\%$ of proved samples are genuine across seeds, with cross-seed variance near zero ($\sigma_{\text{PR}}{=}1$\,pp).
764	This contrasts sharply with Qwen3-4B, where GRPO reaches $93\%$ PR but collapses to $8\%$ genuine with high cross-seed variance.
765	The result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.
766	
767	\subsection{Seed-Dependent Convergence in Exec-Only GRPO}
768	\label{app:seed-convergence}
769	
770	Not all exec-only seeds converge.
771	Of 6 seeds tested (s42--s46, s52; s52 uses $K{=}4$, all others $K{=}8$), we observe three regimes: \emph{converging with degeneration} (s42: $\text{PR}{=}93\%$, genuine${=}7.5\%$; s44: $\text{PR}{=}96\%$, genuine${=}0\%$; s46: $\text{PR}{=}93\%$ at 500 steps), \emph{slow convergence with degeneration} (s43: $\text{PR}{=}14\%$ but $100\%$ hacking at 500 steps), and \emph{non-converging} (s45: $\text{PR}{=}15\%$, genuine${=}86.7\%$; s52: $\text{PR}{=}14\%$, genuine${=}85.7\%$).
772	Non-converging seeds retain high genuine rates (85--87\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.
773	Extended training to 1000 steps for s45 confirms persistent non-convergence ($\text{PR}{=}15\%$, $\text{ISR}^*{=}0.592$, genuine${=}86.7\%$, $n{=}15$ proved); the model neither improves nor degenerates.
774	
775	This parallels the LLaMA-3.2-3B finding (Appendix~\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.
776	Both cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.
777	
778	\subsection{$N{=}2$ Sensitivity Analysis (Excluding Seed 43)}
779	\label{app:n2-sensitivity}
780	
781	Seed~43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding (\S\ref{app:setup}).
782	To assess whether this non-standard protocol affects qualitative conclusions, Table~\ref{tab:n2-sensitivity} reports pooled statistics from seeds~42 and~44 only.
783	
784	\begin{table}[h]
785	\centering
786	\resizebox{\columnwidth}{!}{%
787	\begin{tabular}{@{}lccc@{}}
788	\toprule
789	\textbf{Condition} & \textbf{PR (\%)} & \textbf{ISR$^*$} & \textbf{N-H (\%)} \\
790	\midrule
791	Exec-only 500-step & $95.5 \pm 3.5$ & $0.357 \pm 0.318$ & $3.8 \pm 5.3$ \\
792	Exec-only 1000-step & $98.0 \pm 2.8$ & $0.003 \pm 0.001$ & $0.0 \pm 0.0$ \\
793	ISR $\beta{=}0.1$ 500-step & $85.0 \pm 5.7$ & $0.659 \pm 0.344$ & $8.7 \pm 12.2$ \\
794	\bottomrule
795	\end{tabular}}
796	\caption{Pooled statistics excluding seed~43 ($N{=}2$, seeds~42 and~44 only). Mean$\pm$std of per-seed values. Qualitative patterns preserved: exec-only converges to ${\leq}7.5\%$ non-hacking; ISR $\beta{=}0.1$ shifts composition toward TS.}
797	\label{tab:n2-sensitivity}
798	\end{table}
799	
800	Excluding seed~43, exec-only converges to ${\leq}7.5\%$ non-hacking at 500 steps and $0\%$ at 1000 steps.
801	Under ISR $\beta{=}0.1$, TS dominates both remaining seeds (s42: $16\%$, s44: $100\%$), confirming that ISR reward shifts hacking composition toward tautological shortcuts independent of the s43 evaluation anomaly.
802	The large per-seed ISR$^*$ variance ($0.357 \pm 0.318$) reflects different degeneration modes (CE in s42 vs.\ TS in s44), not data quality issues.
803	
804	\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}
805	\label{app:8b-results}
806	
807	To test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yielding zero GRPO advantage and no learning signal).
808	Table~\ref{tab:8b-combined} summarizes configuration differences and results.
809	
810	\begin{table}[H]
811	\centering
812	\small
813	\begin{tabular}{lcc}
814	\toprule
815	& \textbf{Qwen3-4B} & \textbf{Qwen3-8B} \\
816	\midrule
817	Rollouts ($K$) & 4 & 8 \\
818	Batch size & 4 & 1 \\
819	Gradient accum. & 2 & 16 \\
820	Effective batch & 8 & 16 \\
821	\bottomrule
822	\end{tabular}
823	
824	\vspace{4pt}
825	
826	\resizebox{\columnwidth}{!}{%
827	\begin{tabular}{lcccc}
828	\toprule
829	\textbf{Config} & \textbf{PR\%} & \textbf{Genuine\%} & \textbf{Converged?} & \textbf{Gradient} \\
830	\midrule
831	4B $K{=}4$ s42 & 93 & 7.5 & Yes (degenerate) & Sufficient \\
832	8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\
833	8B $K{=}8$ s42 & 14 & 92.9 & No & Partial \\
834	\bottomrule
835	\end{tabular}}
836	\caption{Cross-scale: Qwen3-4B vs.\ Qwen3-8B. \textbf{Top}: Configuration; $K{=}8$ required at 8B because $K{=}4$ produces near-identical rollouts. \textbf{Bottom}: Results; 4B converges with degeneration, both 8B configurations fail to converge, preserving structural integrity.}
837	\label{tab:8b-combined}
838	\end{table}
839	
840	We first tested $K{=}4$ (matching the 4B configuration): the 8B model produces near-identical rollouts across all four completions, yielding zero GRPO advantage throughout 500 steps and no learning signal ($\text{PR}{=}15.5\%$, cold-start stagnation).
841	Increasing to $K{=}8$ provides non-zero reward variance during mid-training (approximately 40--50\% of steps between 20--370 show non-zero advantage), but this signal proves insufficient for convergence: held-out evaluation yields $\text{PR}{=}14\%$ ($n{=}14$ proved), $\text{ISR}^*{=}0.573$, genuine${=}92.9\%$ (13/14), with a single CE sample.
842	Cosine learning-rate decay combined with insufficient early bootstrap appears to prevent the model from escaping the low-PR regime.
843	
844	This result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.
845	Together, these cases establish a convergence threshold for GRPO-driven degeneration: the structural collapse documented in \S\ref{sec:diagnostic} requires successful RL optimization as a prerequisite, and at 8B scale the rollout diversity bottleneck prevents this optimization from occurring under our configuration.
846	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d72de43e-efce-4505-9d3c-e3475b1cefe2",
  "isSidechain": true,
  "promptId": "ca423cf5-8734-4110-8dbb-7aa294c951c7",
  "agentId": "a9357ac62a46de49c",
  "type": "user",
  "uuid": "1b414f2c-f0b6-4b81-8b55-93091164c6e1",
  "sourceToolAssistantUUID": "d72de43e-efce-4505-9d3c-e3475b1cefe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T12:53:37.556Z_

Let me search more carefully for the specific ISR β=0.1 1000-step per-seed data you're looking for.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b414f2c-f0b6-4b81-8b55-93091164c6e1",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXufQKH7tsC94X4BUUm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eac80ee5-5176-42e7-9684-ace78292cb0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JiczdeagVXrfRn6ZXSjCAN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 23219,
      "cache_read_input_tokens": 18929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23219,
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

_source line 6 · 2026-05-23T12:53:38.769Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01V65VaE37fNEDBnrKQxergP`</summary>

```json
{
  "pattern": "1000.*ISR.*β|s45.*1000|s46.*1000",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eac80ee5-5176-42e7-9684-ace78292cb0d",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXufQKH7tsC94X4BUUm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9443707-af6c-4f92-b816-eb77d8e8cbe5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JiczdeagVXrfRn6ZXSjCAN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 23219,
      "cache_read_input_tokens": 18929,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23219
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 189,
          "cache_read_input_tokens": 18929,
          "cache_creation_input_tokens": 23219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23219,
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

_source line 7 · 2026-05-23T12:53:38.796Z_

<details><summary>↩ Tool result · `toolu_01V65VaE37fNEDBnrKQxergP`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9443707-af6c-4f92-b816-eb77d8e8cbe5",
  "isSidechain": true,
  "promptId": "ca423cf5-8734-4110-8dbb-7aa294c951c7",
  "agentId": "a9357ac62a46de49c",
  "type": "user",
  "uuid": "cbd70f32-4f30-46ac-8653-7ed51c9455e0",
  "sourceToolAssistantUUID": "d9443707-af6c-4f92-b816-eb77d8e8cbe5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-23T12:53:40.469Z_

Let me search for the specific seed data in the detailed results table more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbd70f32-4f30-46ac-8653-7ed51c9455e0",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXuuhYQ3W5vWQkN759K",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c65f763-df60-4dc1-9ea1-0df158394320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QMdFV7AKgtatNce2qzqJFs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 42148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 204,
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

_source line 9 · 2026-05-23T12:53:41.103Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017StUbCcxNZNTA7fhX9SQx4`</summary>

```json
{
  "pattern": "42.*1000|43.*1000|44.*1000|45.*500|46.*500",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c65f763-df60-4dc1-9ea1-0df158394320",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXuuhYQ3W5vWQkN759K",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "80f40e52-25bf-422a-92de-a6154520ffd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QMdFV7AKgtatNce2qzqJFs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 42148,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 204
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 179,
          "cache_read_input_tokens": 42148,
          "cache_creation_input_tokens": 204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 204,
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

_source line 10 · 2026-05-23T12:53:41.151Z_

<details><summary>↩ Tool result · `toolu_017StUbCcxNZNTA7fhX9SQx4`</summary>

```text
56-
57-\paragraph{SFT convergence.}
58:SFT training converged across all three seeds: final-step loss ${\leq}0.04$ and token accuracy ${>}99\%$ after ${\sim}8$ epochs on 500 examples (seed~42: $0.029$; seed~44: $0.033$); the 1000-step extension further decreases loss to $0.017$.
59-
60-\paragraph{Evaluation exception.}
--
171-\end{tabular}
172-\\[2pt]
173:{\small ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
174-\end{table*}
175-
--
243-\bottomrule
244-\end{tabular}
245:[Omitted long matching line]
246-\label{tab:hacking-taxonomy-app}
247-\end{table*}
--
488-
489-\paragraph{Prevalence.}
490:Observed in extended exec-only training (seed~42, 1000 steps).
491-Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
492-
--
528-\begin{table*}[t]
529-\centering
530:[Omitted long matching line]
531-\label{tab:fol-detailed}
532-\label{tab:fol-beta01-detailed}
--
544-  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
545-SFT
546:  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
547:  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
548:  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
549-\cmidrule(l){2-9}
550-  & \multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \textbf{92.3} & $n{=}39$ proved \\
--
553-  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
554-  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\%$ \\
555:  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
556-  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
557:  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\
558-  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
559:  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & PG${=}15\%$ \\
560-\cmidrule(l){2-9}
561-  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.68{\pm}0.47$ & $0.238{\pm}0.30$ & & & & 500-step \\
--
564-\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
565-  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed CE+TS+PG \\
566:  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\
567-  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\
568-  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\
569:  & 45$^\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \textbf{54.8} & PG${=}1$; $n{=}42$ \\
570:  & 46$^\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \textbf{54.5} & PG${=}4$; $n{=}77$ \\
571-\cmidrule(l){2-9}
572-  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.77{\pm}0.14$ & $0.716{\pm}0.26$ & & & & 500-step (s42--44) \\
--
666-\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
667-Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
668:ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
669-PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.
670-By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
--
769-
770-Not all exec-only seeds converge.
771:Of 6 seeds tested (s42--s46, s52; s52 uses $K{=}4$, all others $K{=}8$), we observe three regimes: \emph{converging with degeneration} (s42: $\text{PR}{=}93\%$, genuine${=}7.5\%$; s44: $\text{PR}{=}96\%$, genuine${=}0\%$; s46: $\text{PR}{=}93\%$ at 500 steps), \emph{slow convergence with degeneration} (s43: $\text{PR}{=}14\%$ but $100\%$ hacking at 500 steps), and \emph{non-converging} (s45: $\text{PR}{=}15\%$, genuine${=}86.7\%$; s52: $\text{PR}{=}14\%$, genuine${=}85.7\%$).
772-Non-converging seeds retain high genuine rates (85--87\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.
773-Extended training to 1000 steps for s45 confirms persistent non-convergence ($\text{PR}{=}15\%$, $\text{ISR}^*{=}0.592$, genuine${=}86.7\%$, $n{=}15$ proved); the model neither improves nor degenerates.
--
798-\end{table}
799-
800:Excluding seed~43, exec-only converges to ${\leq}7.5\%$ non-hacking at 500 steps and $0\%$ at 1000 steps.
801-Under ISR $\beta{=}0.1$, TS dominates both remaining seeds (s42: $16\%$, s44: $100\%$), confirming that ISR reward shifts hacking composition toward tautological shortcuts independent of the s43 evaluation anomaly.
802-The large per-seed ISR$^*$ variance ($0.357 \pm 0.318$) reflects different degeneration modes (CE in s42 vs.\ TS in s44), not data quality issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80f40e52-25bf-422a-92de-a6154520ffd3",
  "isSidechain": true,
  "promptId": "ca423cf5-8734-4110-8dbb-7aa294c951c7",
  "agentId": "a9357ac62a46de49c",
  "type": "user",
  "uuid": "a6b6d0e5-88db-4ed1-8cb9-255b1dd60215",
  "sourceToolAssistantUUID": "80f40e52-25bf-422a-92de-a6154520ffd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-23T12:53:43.022Z_

Now I can see the critical information. Let me verify the exact N-H percentages from the table more clearly by reading the relevant section directly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6b6d0e5-88db-4ed1-8cb9-255b1dd60215",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXv5jnPaD9w7fVxRNXH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3d78c6d7-a7c3-4537-a7ab-e363b35464ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CnAdQkNWMi3WtRHNFPQLHE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2537,
      "cache_read_input_tokens": 42352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2537,
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

_source line 12 · 2026-05-23T12:53:43.875Z_

<details open><summary>🔧 Tool call — Read · `toolu_012i3WwZytKQ1T6tgTWRtTFe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": 564,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d78c6d7-a7c3-4537-a7ab-e363b35464ea",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXv5jnPaD9w7fVxRNXH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "59812051-bf6d-40d1-a326-73698981539b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CnAdQkNWMi3WtRHNFPQLHE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2537,
      "cache_read_input_tokens": 42352,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2537
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 154,
          "cache_read_input_tokens": 42352,
          "cache_creation_input_tokens": 2537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2537,
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

_source line 13 · 2026-05-23T12:53:43.882Z_

<details><summary>↩ Tool result · `toolu_012i3WwZytKQ1T6tgTWRtTFe`</summary>

```text
564	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
565	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed CE+TS+PG \\
566	  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\
567	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\
568	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\
569	  & 45$^\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \textbf{54.8} & PG${=}1$; $n{=}42$ \\
570	  & 46$^\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \textbf{54.5} & PG${=}4$; $n{=}77$ \\
571	\cmidrule(l){2-9}
572	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.77{\pm}0.14$ & $0.716{\pm}0.26$ & & & & 500-step (s42--44) \\
573	  & \multicolumn{2}{l}{5-seed mean$\pm$std} & $0.70{\pm}0.19$ & $0.633{\pm}0.23$ & & & & 500-step (s42--46) \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59812051-bf6d-40d1-a326-73698981539b",
  "isSidechain": true,
  "promptId": "ca423cf5-8734-4110-8dbb-7aa294c951c7",
  "agentId": "a9357ac62a46de49c",
  "type": "user",
  "uuid": "56b1f359-2503-4ca6-9857-a9eb60a41c45",
  "sourceToolAssistantUUID": "59812051-bf6d-40d1-a326-73698981539b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-23T12:53:45.580Z_

Perfect! Now let me verify the table column headers to understand exactly what N-H means:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56b1f359-2503-4ca6-9857-a9eb60a41c45",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXvHZgoi9gDVHNMHwcs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c442ba6-1a99-4c03-a8c1-406cfc53cb7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MgeGH9QerFBBWnwQku44bU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 44889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 701,
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

_source line 15 · 2026-05-23T12:53:45.822Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uh8kgBLi5FK3rei6ytm35G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": 536,
  "limit": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c442ba6-1a99-4c03-a8c1-406cfc53cb7f",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXvHZgoi9gDVHNMHwcs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b4666f6-3dd3-435b-9247-2dcddb1a18f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MgeGH9QerFBBWnwQku44bU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 44889,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 701
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 143,
          "cache_read_input_tokens": 44889,
          "cache_creation_input_tokens": 701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 701,
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

_source line 16 · 2026-05-23T12:53:45.828Z_

<details><summary>↩ Tool result · `toolu_01Uh8kgBLi5FK3rei6ytm35G`</summary>

```text
536	\begin{tabular}{@{}llccccccl@{}}
537	\toprule
538	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b4666f6-3dd3-435b-9247-2dcddb1a18f0",
  "isSidechain": true,
  "promptId": "ca423cf5-8734-4110-8dbb-7aa294c951c7",
  "agentId": "a9357ac62a46de49c",
  "type": "user",
  "uuid": "54c4e560-0e5a-4df7-9965-b37a3ced28c4",
  "sourceToolAssistantUUID": "0b4666f6-3dd3-435b-9247-2dcddb1a18f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T12:53:47.638Z_

Now let me check if there's any 1000-step ISR β=0.1 data for s42, s43, s44 and verify whether s45/s46 have any 1000-step runs:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54c4e560-0e5a-4df7-9965-b37a3ced28c4",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXvRyhXPKyaXaBxsM39",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8fea398f-c6fc-49f3-9ba4-22e48b34f5c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018T1X6o2T3uJd1yXygnDMKX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 45590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 272,
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

_source line 18 · 2026-05-23T12:53:48.254Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GoSyQuNmnxLvKVhFzYJ44v`</summary>

```json
{
  "pattern": "ISR.*β|β.*ISR|ISR.*0.1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "output_mode": "content",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fea398f-c6fc-49f3-9ba4-22e48b34f5c2",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXvRyhXPKyaXaBxsM39",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c8c6e033-f35c-4fa5-a5b6-e05930bae936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018T1X6o2T3uJd1yXygnDMKX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 45590,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 272
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 209,
          "cache_read_input_tokens": 45590,
          "cache_creation_input_tokens": 272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 272,
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

_source line 19 · 2026-05-23T12:53:48.268Z_

<details><summary>↩ Tool result · `toolu_01GoSyQuNmnxLvKVhFzYJ44v`</summary>

```text
111:We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
124:This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
137:$\leq$3 & ISR $\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\
140:4--6     & ISR $\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\
143:$\geq$7  & ISR $\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\
153:\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
161:ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
177:TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
178:The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
187:ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\S\ref{sec:goodhart}).
245:[Omitted long matching line]
286:The TS\textsubscript{b} subcategory (functional LOO tautologies undetectable by text matching) provides a lower bound on TS recall: ${\geq}91\%$ ($149/163$) under ISR $\beta{=}0.1$. Other modes' recall is not estimable from the validation-only design; non-hacking rates throughout should be interpreted as upper bounds.
291:Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).
298:Full PG audit was completed for ISR $\beta{=}0.1$ seed~42 only.
303:ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
310:After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
362:TSa (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
386:$\text{ISR}{\geq}0.83$ ($10/12$ samples).
391:Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
564:\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
592:\multicolumn{9}{@{}l}{\textit{Shuffled-ISR $\beta{=}0.1$ (deconfounding control)}} \\
653:\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
663:{\small Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}
668:ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
741:By contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.
745:As a training reward ($r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$, functionally zero, compared to $\text{ISR}^*{=}0.132$ under exec-only and $\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\beta{=}0.1$.
793:ISR $\beta{=}0.1$ 500-step & $85.0 \pm 5.7$ & $0.659 \pm 0.344$ & $8.7 \pm 12.2$ \\
796:\caption{Pooled statistics excluding seed~43 ($N{=}2$, seeds~42 and~44 only). Mean$\pm$std of per-seed values. Qualitative patterns preserved: exec-only converges to ${\leq}7.5\%$ non-hacking; ISR $\beta{=}0.1$ shifts composition toward TS.}
801:Under ISR $\beta{=}0.1$, TS dominates both remaining seeds (s42: $16\%$, s44: $100\%$), confirming that ISR reward shifts hacking composition toward tautological shortcuts independent of the s43 evaluation anomaly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8c6e033-f35c-4fa5-a5b6-e05930bae936",
  "isSidechain": true,
  "promptId": "ca423cf5-8734-4110-8dbb-7aa294c951c7",
  "agentId": "a9357ac62a46de49c",
  "type": "user",
  "uuid": "82c5d089-813c-4b99-abcf-6e8230be4d45",
  "sourceToolAssistantUUID": "c8c6e033-f35c-4fa5-a5b6-e05930bae936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-23T12:53:49.817Z_

Now let me check the footnote about s45 and s46 to see if they have 1000-step runs:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82c5d089-813c-4b99-abcf-6e8230be4d45",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXvcEM25xocc9JVN5mt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5bf1f2f0-7ca4-494c-bb63-bfc477fd204c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V9e8rkQgaWFSeJ5etQj4hT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2102,
      "cache_read_input_tokens": 45862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2102,
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

_source line 21 · 2026-05-23T12:53:52.146Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H9mgJ3B8CQev41qBLkmCU6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": 528,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bf1f2f0-7ca4-494c-bb63-bfc477fd204c",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXvcEM25xocc9JVN5mt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6be1a1a2-c5d1-4f2e-8740-14de98672810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V9e8rkQgaWFSeJ5etQj4hT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2102,
      "cache_read_input_tokens": 45862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2102,
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

### Tool result

_source line 22 · 2026-05-23T12:53:52.151Z_

<details><summary>↩ Tool result · `toolu_01H9mgJ3B8CQev41qBLkmCU6`</summary>

```text
528	\begin{table*}[t]
529	\centering
530	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\times}2$ vs.\ $2{\times}4$, mathematically equivalent).}
531	\label{tab:fol-detailed}
532	\label{tab:fol-beta01-detailed}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6be1a1a2-c5d1-4f2e-8740-14de98672810",
  "isSidechain": true,
  "promptId": "ca423cf5-8734-4110-8dbb-7aa294c951c7",
  "agentId": "a9357ac62a46de49c",
  "type": "user",
  "uuid": "fd269261-06db-45df-936f-0a41a05628dc",
  "sourceToolAssistantUUID": "6be1a1a2-c5d1-4f2e-8740-14de98672810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-23T12:54:00.039Z_

Perfect! Now I have the critical information. Let me summarize my findings:

## Verification Results

Based on my search of `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex`, here are my findings regarding the ISR β=0.1 per-seed N-H (non-hacking) percentages:

### **1000-Step ISR β=0.1 Data Found:**

**s42 at 1000 steps (Line 566):**
- N-H%: **2.2%** (not 6% as claimed)
- Full row: PR=0.90, ISR*=0.877, TS%=96.7, CE%=0, N-H%=2.2
- Note: "TS collapse; PG=1 (n=90)"

**s43:** 
- No 1000-step ISR β=0.1 data in the table. Only 500-step data exists (N-H%=0)

**s44:**
- No 1000-step ISR β=0.1 data in the table. Only 500-step data exists (N-H%=0)

### **s45 and s46 Data Status:**

**s45 and s46 have ONLY 500-step data** – not 1000-step:
- s45: 500 steps only, N-H%=54.8% (line 569)
- s46: 500 steps only, N-H%=54.5% (line 570)

The footnote at line 530 explicitly states: "$^\diamond$Seeds 45--46 added post-hoc under identical hyperparameters." They appear to have been added as additional replicates but only at the 500-step training length.

Extended 1000-step data for s45 exists only in the **exec-only condition** (line 773), not ISR β=0.1.

### **Critical Discrepancies with Your Claims:**

1. **s42 1000-step N-H: 2.2% (not 6%)**
2. **s43 & s44: No 1000-step ISR β=0.1 data exists** – only 500-step
3. **s45 & s46: Only 500-step data exists** (54.8% and 54.5%, not the 55% you mention)
4. **s45/s46 at 55% N-H**: These percentages appear in the 500-step ISR β=0.1 rows, not 1000-step

The 1000-step N-H percentages you're looking for may not exist in the appendix. The only confirmed 1000-step ISR β=0.1 data is for **s42 with 2.2% N-H**, which contradicts your claimed 6%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd269261-06db-45df-936f-0a41a05628dc",
  "isSidechain": true,
  "agentId": "a9357ac62a46de49c",
  "requestId": "req_011CbKXvwEb4NaEjZxZ142a4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5c95e7ee-d2c5-420c-bfab-ea87dfc0caeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/reviewer_5c7e23f1",
  "sessionId": "59dfdc98-1b60-42b8-ab9a-89938a9c03fb",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-toasting-pelican",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0193683CNz6CJMqA9NLJ5sZW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 456,
      "cache_read_input_tokens": 47964,
      "output_tokens": 695,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 456
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 695,
          "cache_read_input_tokens": 47964,
          "cache_creation_input_tokens": 456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 456,
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
