# Research conversation: Read the appendix.tex file at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad3e2f0fd1e966b13.jsonl`
- **Structured JSON:** [`c51563c122b058d47ea7.json`](../../sessions/c5/c51563c122b058d47ea7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-24T04:28:00.292Z_

Read the appendix.tex file at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex, specifically looking for:

1. The per-seed FOL detailed table (tab:fol-detailed or tab:fol-beta01-detailed) - read lines around 550-700 to find it
2. The ProofFOL detailed table (tab:prooffol-detailed) - search for it
3. The SFT detailed results (3-seed pooled)
4. The McNemar test results
5. The 5-seed ISR results (s45, s46 data)
6. The seed convergence appendix section

For each table found, report:
- The per-seed TS counts, CE counts, genuine counts, n_proved, PR
- The pooled totals
- Any footnotes or annotations

Also check: does the appendix SFT section show 3-seed pooled data? What are the per-seed SFT n_proved and CE/genuine counts?

Search breadth: very thorough

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9a129a0b-cfed-4bc2-b351-d0299b5a1826",
  "agentId": "ad3e2f0fd1e966b13",
  "type": "user",
  "uuid": "2890a4fa-4782-47cc-b9e7-fe292f22f1de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T04:28:01.836Z_

I'll read the appendix.tex file and search for the specific tables you mentioned. Let me start by reading the file with a focus on the sections you're interested in.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2890a4fa-4782-47cc-b9e7-fe292f22f1de",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmASmykYau12zejPcuF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d519ab5b-0a5f-47f9-b287-af45be8ff811",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PrYn2goi9oRVofLJdFBvM2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30198,
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

_source line 3 · 2026-05-24T04:28:02.094Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QhNfkqW81BwNnXDWRqgj7G`</summary>

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
  "parentUuid": "d519ab5b-0a5f-47f9-b287-af45be8ff811",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmASmykYau12zejPcuF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3d7e5195-c1a8-4264-9d16-e94f6ba7aeb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PrYn2goi9oRVofLJdFBvM2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30198,
      "cache_read_input_tokens": 0,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 30198
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 30198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 30198,
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

_source line 4 · 2026-05-24T04:28:02.375Z_

<details><summary>↩ Tool result · `toolu_01QhNfkqW81BwNnXDWRqgj7G`</summary>

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
554	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}5.4\%$ \\
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
847	\section{Use of AI Assistants}
848	\label{app:ai-assistants}
849	
850	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
851	\begin{itemize}
852	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
853	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
854	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
855	\end{itemize}
856	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d7e5195-c1a8-4264-9d16-e94f6ba7aeb5",
  "isSidechain": true,
  "promptId": "9a129a0b-cfed-4bc2-b351-d0299b5a1826",
  "agentId": "ad3e2f0fd1e966b13",
  "type": "user",
  "uuid": "3e99c4a5-443c-4272-b6bf-899a4171252b",
  "sourceToolAssistantUUID": "3d7e5195-c1a8-4264-9d16-e94f6ba7aeb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-24T04:28:04.003Z_

The file is quite long. Let me search for the specific tables and sections you mentioned. I'll use grep to find the key tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e99c4a5-443c-4272-b6bf-899a4171252b",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmAbc3UGcP69B57tezy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b95d3784-a61b-42f3-86e4-287c9d64b2a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RTzsD6ti9JN5GLrq6aDKSB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 23398,
      "cache_read_input_tokens": 30198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23398,
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

_source line 6 · 2026-05-24T04:28:04.967Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01UqnwLvXyrRsasMdQSPhLCw`</summary>

```json
{
  "pattern": "tab:fol.*detailed|tab:fol-beta01-detailed|tab:prooffol-detailed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b95d3784-a61b-42f3-86e4-287c9d64b2a6",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmAbc3UGcP69B57tezy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86250939-b180-4859-82a3-4d6f56d2f0d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RTzsD6ti9JN5GLrq6aDKSB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 23398,
      "cache_read_input_tokens": 30198,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23398
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 152,
          "cache_read_input_tokens": 30198,
          "cache_creation_input_tokens": 23398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23398,
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

_source line 7 · 2026-05-24T04:28:04.993Z_

<details><summary>↩ Tool result · `toolu_01UqnwLvXyrRsasMdQSPhLCw`</summary>

```text
Found 3 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86250939-b180-4859-82a3-4d6f56d2f0d6",
  "isSidechain": true,
  "promptId": "9a129a0b-cfed-4bc2-b351-d0299b5a1826",
  "agentId": "ad3e2f0fd1e966b13",
  "type": "user",
  "uuid": "156bff02-c76f-4994-9d28-a41cbd8ccb7c",
  "sourceToolAssistantUUID": "86250939-b180-4859-82a3-4d6f56d2f0d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-24T04:28:07.088Z_

Now let me search for the specific table references in the appendix to understand where they are:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "156bff02-c76f-4994-9d28-a41cbd8ccb7c",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmAnpVDzJHH83K9iW7t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e4fb048-a421-43af-8905-2daa2af874f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0114LuAusahYV6wHMpQPBCyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 53596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 281,
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

_source line 9 · 2026-05-24T04:28:07.301Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HufGtHfV7VuEgVkjp5U1dC`</summary>

```json
{
  "command": "grep -n \"label{tab:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e4fb048-a421-43af-8905-2daa2af874f2",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmAnpVDzJHH83K9iW7t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7fef7255-ec9c-420e-a030-73b695452f41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0114LuAusahYV6wHMpQPBCyy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 53596,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 281
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 120,
          "cache_read_input_tokens": 53596,
          "cache_creation_input_tokens": 281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 281,
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

_source line 10 · 2026-05-24T04:28:07.483Z_

<details><summary>↩ Tool result · `toolu_01HufGtHfV7VuEgVkjp5U1dC`</summary>

```text
13:\label{tab:hyperparams}
77:\label{tab:prooffol-vs-folio}
148:\label{tab:premise-bin-modes}
154:\label{tab:bootstrap-ci}
246:\label{tab:hacking-taxonomy-app}
283:\label{tab:classifier-precision}
531:\label{tab:fol-detailed}
532:\label{tab:fol-beta01-detailed}
605:\label{tab:prolog-detailed}
638:\label{tab:prooffol-detailed}
689:\label{tab:beta03-detailed}
797:\label{tab:n2-sensitivity}
837:\label{tab:8b-combined}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fef7255-ec9c-420e-a030-73b695452f41",
  "isSidechain": true,
  "promptId": "9a129a0b-cfed-4bc2-b351-d0299b5a1826",
  "agentId": "ad3e2f0fd1e966b13",
  "type": "user",
  "uuid": "d8133964-6f0c-4fef-8379-c43a92b0311a",
  "sourceToolAssistantUUID": "7fef7255-ec9c-420e-a030-73b695452f41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-24T04:28:09.498Z_

Perfect! I have the table labels and line numbers. The tables are at:
- tab:fol-detailed and tab:fol-beta01-detailed: lines 531-532 (table starts around line 528-600)
- tab:prolog-detailed: line 605 (table around 602-633)
- tab:prooffol-detailed: line 638 (table around 635-664)

Let me read these sections in detail:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8133964-6f0c-4fef-8379-c43a92b0311a",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmAyRTd33sVjDxJaJbu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c82098b8-4533-47f6-a693-3af983b34d2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Qhopr6AB6mgx7QFZGX6pLD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 53877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 295,
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

_source line 12 · 2026-05-24T04:28:09.751Z_

<details open><summary>🔧 Tool call — Read · `toolu_014QRNnvR5p44iyMYDh3nTym`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": 528,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c82098b8-4533-47f6-a693-3af983b34d2e",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmAyRTd33sVjDxJaJbu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9f7f136f-5c1f-46da-8dc1-d8c9bd43c483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Qhopr6AB6mgx7QFZGX6pLD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 53877,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 295
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 227,
          "cache_read_input_tokens": 53877,
          "cache_creation_input_tokens": 295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 295,
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

_source line 13 · 2026-05-24T04:28:09.767Z_

<details><summary>↩ Tool result · `toolu_014QRNnvR5p44iyMYDh3nTym`</summary>

```text
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
554	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}5.4\%$ \\
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f7f136f-5c1f-46da-8dc1-d8c9bd43c483",
  "isSidechain": true,
  "promptId": "9a129a0b-cfed-4bc2-b351-d0299b5a1826",
  "agentId": "ad3e2f0fd1e966b13",
  "type": "user",
  "uuid": "9ebf2aec-c893-44bb-beea-cc8e4fab1225",
  "sourceToolAssistantUUID": "9f7f136f-5c1f-46da-8dc1-d8c9bd43c483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-24T04:28:11.247Z_

Excellent! Now let me search for the McNemar test results and ISR results sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ebf2aec-c893-44bb-beea-cc8e4fab1225",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmB9bPirRoNUxeujzLp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b35ddb6-616a-42d7-a020-51d98cdb2e09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Pqm5nPX5LUyA3TfYQFyc54",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6827,
      "cache_read_input_tokens": 54172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6827,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 15 · 2026-05-24T04:28:12.290Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015Pi6megcB9YzsVvVwZPz2c`</summary>

```json
{
  "command": "grep -n \"McNemar\\|5-seed\\|s45\\|s46\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b35ddb6-616a-42d7-a020-51d98cdb2e09",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmB9bPirRoNUxeujzLp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f985be96-2b97-4800-9f77-155876730cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Pqm5nPX5LUyA3TfYQFyc54",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6827,
      "cache_read_input_tokens": 54172,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6827
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 54172,
          "cache_creation_input_tokens": 6827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6827,
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

_source line 16 · 2026-05-24T04:28:12.374Z_

<details><summary>↩ Tool result · `toolu_015Pi6megcB9YzsVvVwZPz2c`</summary>

```text
125:Premise-count-matched comparison eliminates the difference ($1.06\times$, McNemar's test $p{=}0.317$; Table~\ref{tab:fol-beta01-detailed}), confirming that the scalar ISR advantage is not statistically significant.
210:The matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\text{bonf}}{=}0.056$), significant at $\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).
573:  & \multicolumn{2}{l}{5-seed mean$\pm$std} & $0.70{\pm}0.19$ & $0.633{\pm}0.23$ & & & & 500-step (s42--46) \\
771:Of 6 seeds tested (s42--s46, s52; s52 uses $K{=}4$, all others $K{=}8$), we observe three regimes: \emph{converging with degeneration} (s42: $\text{PR}{=}93\%$, genuine${=}7.5\%$; s44: $\text{PR}{=}96\%$, genuine${=}0\%$; s46: $\text{PR}{=}93\%$ at 500 steps), \emph{slow convergence with degeneration} (s43: $\text{PR}{=}14\%$ but $100\%$ hacking at 500 steps), and \emph{non-converging} (s45: $\text{PR}{=}15\%$, genuine${=}86.7\%$; s52: $\text{PR}{=}14\%$, genuine${=}85.7\%$).
773:Extended training to 1000 steps for s45 confirms persistent non-convergence ($\text{PR}{=}15\%$, $\text{ISR}^*{=}0.592$, genuine${=}86.7\%$, $n{=}15$ proved); the model neither improves nor degenerates.
844:This result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f985be96-2b97-4800-9f77-155876730cca",
  "isSidechain": true,
  "promptId": "9a129a0b-cfed-4bc2-b351-d0299b5a1826",
  "agentId": "ad3e2f0fd1e966b13",
  "type": "user",
  "uuid": "fd1a8890-faec-4fdd-bc2a-f83863381d00",
  "sourceToolAssistantUUID": "f985be96-2b97-4800-9f77-155876730cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-24T04:28:13.678Z_

Now let me search for the seed convergence appendix section and related detailed information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd1a8890-faec-4fdd-bc2a-f83863381d00",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmBLKKPuQJdmEfXZY9K",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "94569816-c88f-4abe-a765-7c11c0ebf324",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015hvU4SorHLGzWmqZjRB6np",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 60999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 770,
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

_source line 18 · 2026-05-24T04:28:14.009Z_

<details open><summary>🔧 Tool call — Read · `toolu_01956YpLFky4TmqXRD2QTXkc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": 767,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94569816-c88f-4abe-a765-7c11c0ebf324",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmBLKKPuQJdmEfXZY9K",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cadc899c-76e2-40cf-a4d2-52d8a842ada4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015hvU4SorHLGzWmqZjRB6np",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 60999,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 770
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 141,
          "cache_read_input_tokens": 60999,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 770,
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

_source line 19 · 2026-05-24T04:28:14.014Z_

<details><summary>↩ Tool result · `toolu_01956YpLFky4TmqXRD2QTXkc`</summary>

```text
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
847	\section{Use of AI Assistants}
848	\label{app:ai-assistants}
849	
850	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
851	\begin{itemize}
852	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
853	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
854	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
855	\end{itemize}
856	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cadc899c-76e2-40cf-a4d2-52d8a842ada4",
  "isSidechain": true,
  "promptId": "9a129a0b-cfed-4bc2-b351-d0299b5a1826",
  "agentId": "ad3e2f0fd1e966b13",
  "type": "user",
  "uuid": "2582e2d9-bfd3-4970-ac3d-bafee3788278",
  "sourceToolAssistantUUID": "cadc899c-76e2-40cf-a4d2-52d8a842ada4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-24T04:28:15.231Z_

Perfect! Now let me search for any additional information about the McNemar test and premise-count matched comparisons:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2582e2d9-bfd3-4970-ac3d-bafee3788278",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmBTQxToZTxV132cnaR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "40994a4b-e461-4419-a61a-512ba7663259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EWecrjWCAcRCQPULaKDHG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 61769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2607,
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

_source line 21 · 2026-05-24T04:28:16.191Z_

<details open><summary>🔧 Tool call — Read · `toolu_013St5VNtNueZecFdEufDsWa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": 120,
  "limit": 70
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40994a4b-e461-4419-a61a-512ba7663259",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmBTQxToZTxV132cnaR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9038cd9f-e4d3-4611-ba91-9e221500d96a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EWecrjWCAcRCQPULaKDHG3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 61769,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 148,
          "cache_read_input_tokens": 61769,
          "cache_creation_input_tokens": 2607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2607,
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

_source line 22 · 2026-05-24T04:28:16.196Z_

<details><summary>↩ Tool result · `toolu_013St5VNtNueZecFdEufDsWa`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9038cd9f-e4d3-4611-ba91-9e221500d96a",
  "isSidechain": true,
  "promptId": "9a129a0b-cfed-4bc2-b351-d0299b5a1826",
  "agentId": "ad3e2f0fd1e966b13",
  "type": "user",
  "uuid": "e4e50b1b-5757-4775-b6aa-dd5354bf1a23",
  "sourceToolAssistantUUID": "9038cd9f-e4d3-4611-ba91-9e221500d96a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-24T04:28:46.757Z_

Perfect! Now let me compile all the information I've found about the SFT section to confirm the 3-seed pooled data:

Based on my thorough reading of the appendix.tex file, here is my comprehensive report of the specific tables and data you requested:

---

## DETAILED TABLE FINDINGS

### 1. **FOL DETAILED TABLE (tab:fol-beta01-detailed / tab:fol-detailed)** 
**Location: Lines 528-600**

#### SFT 3-Seed Pooled Results (Lines 545-550)
- **PR (Prove Rate)**: 0.130 (13%)
- **ISR*** (Proved-only ISR): 0.595
- **TS%**: 0% 
- **CE%**: 7.8%
- **N-H% (Non-Hacking)**: **92.3%** ✓ (BOLD in table)
- **n_proved**: 39 total proved samples
- **Per-seed breakdown**:
  - Seed 42: PR=0.13, ISR*=0.568, TS=0, CE=7.7%, N-H=92.3%
  - Seed 43: PR=0.11, ISR*=0.635, TS=0, CE=9.1%, N-H=90.9%
  - Seed 44: PR=0.15, ISR*=0.589, TS=0, CE=6.7%, N-H=93.3%
- **Note**: All SFT at 1000 steps, supervised (no RL)

#### ISR β=0.1 Results (5-seed expansion, Lines 564-573)
- **3-seed (s42-44) at 500 steps**:
  - PR: 0.77±0.14
  - ISR*: 0.716±0.26
  - Per-seed PR/ISR values:
    - s42: PR=0.81, ISR*=0.415, TS%=16.0, CE%=51.9, N-H=17.3%
    - s43: PR=0.61, ISR*=0.830, TS%=100, CE%=0, N-H=0%
    - s44: PR=0.89, ISR*=0.902, TS%=100, CE%=0, N-H=0%

- **5-seed (s42-46) at 500 steps**:
  - PR: 0.70±0.19
  - ISR*: 0.633±0.23
  - **NEW SEEDS s45, s46** (post-hoc, marked with ◇):
    - s45: PR=0.42, ISR*=0.605, TS%=38.1, CE%=4.8, N-H=54.8%, n=42
    - s46: PR=0.77, ISR*=0.411, TS%=14.3, CE%=26.0, N-H=54.5%, n=77
  - **Footnote**: "Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: 4×2 vs. 2×4, mathematically equivalent)"

#### Exec-Only Results (500-step, Lines 552-562)
- **3-seed mean**: PR=0.68±0.47, ISR*=0.238±0.30 (500 steps)
- Per-seed:
  - s42: PR=0.93, ISR*=0.132, TS%=0, CE%=87.1, N-H=7.5%, PG=5.4%
  - s43: PR=0.13, ISR*=0†, sampling eval (T=0.7)
  - s44: PR=0.98, ISR*=0.582, TS%=100, CE%=0, N-H=0%

### 2. **PROLOG DETAILED TABLE (tab:prolog-detailed)**
**Location: Lines 602-633**

#### Exec+ISR (STA reward) - All Seeds Show 0% Non-Hacking (Lines 618-623)
- **Seed 42**: PR=0.50, ISR*=1.000, TS%=**100**, CE%=0, N-H=0%
  - **Mode**: TS tautological (clean single premise = conclusion)
  
- **Seed 43**: PR=0.38, ISR*=0.185, TS%=0†, CE%=97.4, N-H=0%
  - **Footnote†a**: "Strict TS classifier reports 0%, but functional analysis shows all 38/38 proved samples are tautological (n_necessary=1). Uppercase pseudo-Prolog syntax bypasses the text-match classifier."
  - **Mode**: Functional TS (uppercase pseudo-Prolog)
  
- **Seed 44**: PR=0.97, ISR*=0.912, TS%=0†, CE%=0, N-H=0†
  - **Footnote†b**: "Strict classifier reports Non-hacking=100%, but 95/97 proved samples have n_necessary=1. The model converts NL to snake_case atoms serving as both fact and query, a third distinct Goodhart pathway."
  - **Mode**: Query-as-fact gaming
  
- **3-seed mean**: PR=0.62±0.31, ISR*=0.699±0.45, **0% non-hacking** (3/3 Goodhart, 0% non-hacking)

#### Exec-Only Prolog (Lines 611-616)
- **3-seed mean**: PR=0.53±0.31, ISR*=0.146±0.21
- Per-seed: s42: PR=0.83, ISR*=0.037; s43: PR=0.56, ISR*=0.015; s44: PR=0.21, ISR*=0.387

### 3. **PROOFFOL DETAILED TABLE (tab:prooffol-detailed)**
**Location: Lines 635-664**

#### Exec-only Results
- s42: PR_f50≈1.0, ISR*=0.066, TS%=**100**, CE%=0, Genuine%=0, n=99 (stable)
- s43: PR_f50=0.55, ISR*=0.119, TS%=0, CE%=49.2, Genuine%=50.8, n=63 (partial)
- s44: PR_f50≈1.0, ISR*=0.043, TS%=0, CE%=98.6, Genuine%=1.4, n=72 (stable)
- **Aggregate genuine rate**: 17.4% (mean of seeds)

#### ISR β=0.1 Results
- s42: PR_f50=0.35, ISR*=0.12, TS%=0, CE%=0, **Genuine%=100**, n=46 (collapsed)
- s43: PR_f50≈0.47, ISR*≈0.13, TS%=0, CE%=69.6, Genuine%=30.4, n=56 (unstable)
- s44: PR_f50=0.49, ISR*=0.145, TS%=0, CE%=0, **Genuine%=100**, n=66 (oscillation)
- **Aggregate genuine rate**: **76.8%** (mean of seeds)
- **Permutation test**: p=0.10, N=3 per group

---

## 4. **MCNEMAR TEST RESULTS**
**Location: Lines 120-125**

"Premise-count-matched comparison eliminates the difference ($1.06\times$, **McNemar's test $p{=}0.317$**; Table~\ref{tab:fol-beta01-detailed}), confirming that the scalar ISR advantage is not statistically significant."

- **Comparison**: ISR β=0.1 seed 42 vs. Random β=0.1 on matched premise counts
- **Result**: The apparent 1.06× ISR advantage is **not statistically significant** at p=0.317
- **Interpretation**: ISR's mechanical inflation from shorter formalizations is accounted for; genuine effect disappears when controlling for premise count

---

## 5. **5-SEED ISR RESULTS (s45, s46 POST-HOC DATA)**
**Location: Lines 569-573**

Both s45 and s46 were run at 500 steps, ISR β=0.1, FOLIO dataset:

| Seed | PR | ISR* | TS% | CE% | N-H% | Notes |
|------|-----|-------|-----|-----|------|-------|
| s45 | 0.42 | 0.605 | 38.1 | 4.8 | 54.8 | PG=1; n=42 |
| s46 | 0.77 | 0.411 | 14.3 | 26.0 | 54.5 | PG=4; n=77 |

**5-seed aggregate (s42-46) at 500 steps**: PR=0.70±0.19, ISR*=0.633±0.23

**Footnote context** (line 530): "Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: 4×2 vs. 2×4, mathematically equivalent)."

---

## 6. **SEED CONVERGENCE APPENDIX SECTION**
**Location: Lines 767-776 (Section App:seed-convergence)**

**6 total seeds tested (s42-46, s52):**

**Converging with degeneration** (successful GRPO):
- s42: PR=93%, Genuine=7.5%
- s44: PR=96%, Genuine=0%
- s46: PR=93% (at 500 steps)

**Slow convergence with degeneration**:
- s43: PR=14% but 100% hacking at 500 steps

**Non-converging** (failed to bootstrap):
- s45: PR=15%, Genuine=86.7%, ISR*=0.592 (even at 1000 steps), n=15
- s52: PR=14%, Genuine=85.7%, K=4 (different rollouts parameter)

**Key insight**: "Non-converging seeds retain high genuine rates (85--87%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity."

---

## 7. **ADDITIONAL STATISTICAL TESTS**
**Location: Lines 151-174 (Table tab:bootstrap-ci)**

Fisher exact tests (3-seed pooled):
- **ISR vs. Random non-hacking**: ISR=6.06% [3.6%, 9.9%] vs. Random=9.5% [6.5%, 13.7%], OR=0.61, p=0.182 (n.s.)
- **ISR vs. Random TS gaming**: ISR=70.6% [64.3%, 76.3%] vs. Random=13.7% [9.9%, 18.6%], OR=15.05, p=1.3×10^-39
- **SFT vs. Exec-only non-hacking**: SFT=92.3% [79.7%, 97.3%] vs. Exec-only=7.5%, OR=147, p<0.001

Sample sizes:
- ISR: n=231 (3 seeds)
- Random: n=262 (3 seeds)
- Exec-only: n=93 (s42 only, 500 steps)
- SFT: n=39 (3 seeds, 1000 steps)

---

## SUMMARY ANSWER TO YOUR SPECIFIC QUESTIONS

**1. SFT Pooled (3-seed) Data:**
- YES, the appendix shows 3-seed pooled SFT: PR=13.0%, ISR*=0.595, **92.3% non-hacking**
- Per-seed n_proved: 13, 11, 15 respectively
- Per-seed CE/Genuine: 7.7%/92.3%, 9.1%/90.9%, 6.7%/93.3%

**2. McNemar Test:**
- Specific result: p=0.317 (n.s.) for premise-count-matched ISR vs. Random comparison
- Conclusion: Apparent ISR advantage (1.06×) is not statistically significant

**3. 5-seed ISR Results (s45, s46):**
- s45: Highest N-H% (54.8%), lowest PR (42%)
- s46: Moderate N-H% (54.5%), higher PR (77%)
- Both are "non-converging" seeds with much higher genuine rates than s42/43/44

**4. Seed Convergence Section:**
- Clearly documented at lines 767-776
- Key finding: Degeneration is byproduct of successful RL optimization, not training procedure itself

All tables have been identified with exact line numbers and complete per-seed data extracted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4e50b1b-5757-4775-b6aa-dd5354bf1a23",
  "isSidechain": true,
  "agentId": "ad3e2f0fd1e966b13",
  "requestId": "req_011CbLmBcryZQ5JL4P12uSHA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d004fe7-8466-4022-97af-9e3a92aa835a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6",
  "sessionId": "34e9a4ca-36ed-4c0b-9ff5-69e710917f8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "quirky-wishing-lake",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BhZWS89UYupuJYgvNz2Fbx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2381,
      "cache_read_input_tokens": 64376,
      "output_tokens": 3305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2381
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3305,
          "cache_read_input_tokens": 64376,
          "cache_creation_input_tokens": 2381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2381,
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
