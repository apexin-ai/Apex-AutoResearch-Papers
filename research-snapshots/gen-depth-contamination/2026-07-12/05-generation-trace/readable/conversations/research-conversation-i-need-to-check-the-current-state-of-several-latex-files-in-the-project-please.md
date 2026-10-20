# Research conversation: I need to check the current state of several LaTeX files in the project. Please: 1. Read `/home/ubuntu/.agent-ml-researc

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae896b46dd4096f76.jsonl`
- **Structured JSON:** [`6f868f76b06de2cc8a48.json`](../../sessions/6f/6f868f76b06de2cc8a48.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

9 recorded events

### User

_source line 1 · 2026-05-14T00:43:07.136Z_

I need to check the current state of several LaTeX files in the project. Please:

1. Read `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex` - I need to check:
   - Around line 30: the table note for Qwen-cont 0v1 — does it say p=0.000 or p=0.002? And AUC=0.9972 or 0.9971?
   - Around line 167: the Pythia→OLMo transfer retention percentage

2. Read `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex` - I need to check:
   - Line 5: wording about "fourth generation"
   - Lines 52-56: the paper structure paragraph — does it mention Discussion?
   - Line 31: the D017 claim wording

3. Read `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex` - I need to check:
   - Section 5.3: what are the T=1.2 top features listed? (should be hapax_ratio, ttr, surp_skew but may still incorrectly list freq_entropy)

Report the exact text found at each location. Be thorough - read the full files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3767a4dd-8323-40d5-adc2-11298901ddbf",
  "agentId": "ae896b46dd4096f76",
  "type": "user",
  "uuid": "6c907d1e-5802-46a6-9841-687f7a3b6ddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "de623504-6717-4729-8094-7e6a85d35da7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-petting-backus"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-14T00:43:08.405Z_

I'll read all three LaTeX files to check the specific details you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c907d1e-5802-46a6-9841-687f7a3b6ddd",
  "isSidechain": true,
  "agentId": "ae896b46dd4096f76",
  "requestId": "req_011Cb1XvfCs6GiqWaULBe6R5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe8c722f-19fc-45ef-ac0c-87e74333bd3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "de623504-6717-4729-8094-7e6a85d35da7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-petting-backus",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PqaEQpvETU9GyJQemFtjo1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20957,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20957,
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

_source line 3 · 2026-05-14T00:43:08.919Z_

<details open><summary>🔧 Tool call — Read · `toolu_014EqDRchPiLFyQgaSs7cPdr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe8c722f-19fc-45ef-ac0c-87e74333bd3f",
  "isSidechain": true,
  "agentId": "ae896b46dd4096f76",
  "requestId": "req_011Cb1XvfCs6GiqWaULBe6R5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ae3e8f41-8d60-43d6-9151-b31ea6a7ce2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "de623504-6717-4729-8094-7e6a85d35da7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-petting-backus",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PqaEQpvETU9GyJQemFtjo1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20957,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20957,
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

_source line 4 · 2026-05-14T00:43:08.940Z_

<details><summary>↩ Tool result · `toolu_014EqDRchPiLFyQgaSs7cPdr`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on four model configurations:
5	Pythia-1.4B and OLMo-1B in continuation mode, and Qwen2.5-1.5B-Instruct in both rewrite and continuation modes.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set described in Section~\ref{sec:method}.
7	Each configuration uses a balanced corpus of 5{,}000 texts per depth level (generations 0--5).
8	We organize results around four questions:
9	(1)~Does $\Kempirical = 2$ hold across configurations?
10	(2)~Do depth classifiers transfer across models?
11	(3)~Is the feature degradation ordering model-independent?
12	(4)~How does generation mode affect detectability?
13	
14	%% ====================================================================
15	\subsection{$\Kempirical = 2$ Across All Configurations}
16	\label{sec:kstar_boundary}
17	
18	Table~\ref{tab:kstar_ci} reports pairwise $\auc$ for adjacent depth pairs
19	across all four configurations, with bootstrap 95\% confidence intervals
20	(1{,}000 resamples) and permutation-test $p$-values for the critical 1v2
21	and 2v3 boundaries.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\caption{Pairwise $\auc$ for adjacent depth pairs.  Bootstrap 95\% CIs
27	and permutation $p$-values shown for the $\Kstar$ boundary rows (1v2,
28	2v3).  $\Kempirical = 2$ requires 1v2 $\text{CI}_\text{low} > \theta$
29	and 2v3 $\text{CI}_\text{high} < \theta$ with $\theta = 0.60$.
30	All 0v1 permutation $p \leq 0.002$ (Qwen-cont 0v1: CI [0.9963, 0.9978], $p = 0.000$).}
31	\label{tab:kstar_ci}
32	\begin{tabular}{lcccc}
33	\toprule
34	 & Qwen-rw & Pythia & OLMo & Qwen-cont \\
35	\midrule
36	0v1 & 0.9956 & 0.9932 & 0.9970 & 0.9972 \\[4pt]
37	1v2 & 0.6955 & 0.6539 & 0.6145 & 0.6112 \\
38	{\footnotesize CI}
39	  & {\footnotesize [.6859,\,.7041]}
40	  & {\footnotesize [.6454,\,.6630]}
41	  & {\footnotesize [.6045,\,.6247]}
42	  & {\footnotesize [.6015,\,.6213]} \\
43	{\footnotesize $p$}
44	  & {\footnotesize .002}
45	  & {\footnotesize .002}
46	  & {\footnotesize .002}
47	  & {\footnotesize .002} \\[4pt]
48	2v3 & 0.5893 & 0.5514 & 0.5496 & 0.5609 \\
49	{\footnotesize CI}
50	  & {\footnotesize [.5795,\,.5991]}
51	  & {\footnotesize [.5417,\,.5628]}
52	  & {\footnotesize [.5399,\,.5596]}
53	  & {\footnotesize [.5511,\,.5712]} \\
54	{\footnotesize $p$}
55	  & {\footnotesize .002}
56	  & {\footnotesize .002}
57	  & {\footnotesize .002}
58	  & {\footnotesize .002} \\[4pt]
59	3v4 & 0.5435 & 0.5152 & 0.5091 & 0.5409 \\
60	4v5 & 0.5340 & 0.5136 & 0.5045 & 0.5141 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	The pattern is uniform across all four configurations:
66	0v1 discrimination is near-perfect ($\auc > 0.99$),
67	followed by a sharp drop at 1v2 ($\auc$ range: 0.6112--0.6955),
68	with 2v3 falling below the decision threshold $\theta = 0.60$
69	($\auc$ range: 0.5496--0.5893).
70	All subsequent pairs (3v4, 4v5) converge toward chance.
71	Figure~\ref{fig:auc_decay} visualizes this decay.
72	
73	\begin{figure}[t]
74	\centering
75	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
76	\caption{Pairwise $\auc$ as a function of depth pair across four model-mode configurations (solid) and four decoding strategies (dashed).  All configurations show a sharp drop between 0v1 and 1v2, with 2v3 and deeper pairs falling below the decision threshold $\theta = 0.60$ (horizontal dashed line).  Error bars show bootstrap 95\% CIs for model-mode configurations; decoding strategy curves omit CIs as they were computed on a separate experimental setup.}
77	\label{fig:auc_decay}
78	\end{figure}
79	
80	For the $\Kempirical$ determination, all four 1v2 CI lower bounds exceed
81	$\theta$: Qwen-rw ($\text{CI}_\text{low} = 0.6859$), Pythia (0.6454),
82	OLMo (0.6045), and Qwen-cont (0.6015).
83	Conversely, all four 2v3 CI upper bounds fall below $\theta$:
84	Qwen-rw ($\text{CI}_\text{high} = 0.5991$), Qwen-cont (0.5712),
85	Pythia (0.5628), and OLMo (0.5596).
86	Permutation tests confirm $p = 0.002$ for all eight boundary comparisons.
87	Together these establish $\Kempirical = 2$ as a consistent discrimination boundary across all tested configurations at $\leq$1.5B scale, suggesting universality beyond the specific models studied.
88	
89	The most marginal case is Qwen-cont, where the 1v2 CI lower bound
90	(0.6015) exceeds $\theta$ by only 0.0015.  This narrow margin
91	indicates that $\Kempirical = 2$ is robust but not trivially so---continuation-mode
92	generation produces weaker depth artifacts than rewrite mode, pushing the
93	boundary closer to the detection threshold.
94	
95	The absolute 1v2 $\auc$ varies across models:
96	Qwen-rw (0.6955) $>$ Pythia (0.6539) $>$ OLMo (0.6145) $\approx$ Qwen-cont (0.6112).
97	Notably, the spread due to generation mode within a single model
98	(Qwen-rw vs.\ Qwen-cont: $\Delta = 8.4$\,pp) exceeds the spread
99	across models in the same mode
100	(Pythia vs.\ OLMo: $\Delta = 3.9$\,pp),
101	suggesting that generation protocol is a stronger determinant
102	of detectability than model identity.
103	We examine both factors in Sections~\ref{sec:transfer}
104	and~\ref{sec:generation_mode}.
105	
106	Beyond the $\Kempirical$ boundary, depth discrimination deteriorates
107	rapidly.
108	OLMo shows nonsignificant permutation $p$-values at 3v4
109	($p = 0.064$) and 4v5 ($p = 0.232$), indicating that depth
110	classification beyond generation~2 is indistinguishable from
111	random for this model.
112	Pythia retains marginal effects at these depths
113	($p = 0.006$ and $p = 0.008$, respectively),
114	while Qwen-cont shows weak but detectable discrimination through
115	3v4 ($p = 0.002$) that fades at 4v5 ($p = 0.006$).
116	
117	%% ====================================================================
118	\subsection{Cross-Model Transfer}
119	\label{sec:transfer}
120	
121	Having established $\Kempirical = 2$ consistently, we next ask: is this boundary a property of the text itself, or an artifact of model self-familiarity?
122	To answer this, we train classifiers on one model's outputs and evaluate on another's.
123	Table~\ref{tab:transfer_matrix} shows the full
124	$4 \times 4$ transfer accuracy matrix for 6-class ordinal depth
125	classification.
126	
127	\begin{table}[t]
128	\centering
129	\small
130	\caption{Cross-model transfer accuracy (6-class ordinal
131	classification).  Diagonal entries (bold): within-model accuracy.
132	Off-diagonal: cross-model transfer.  Retention is computed as
133	off-diagonal accuracy divided by the diagonal entry of the training
134	model.}
135	\label{tab:transfer_matrix}
136	\begin{tabular}{lcccc}
137	\toprule
138	Train $\downarrow$ / Test $\rightarrow$
139	  & Qwen-rw & Pythia & OLMo & Qwen-cont \\
140	\midrule
141	Qwen-rw
142	  & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
143	Pythia
144	  & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
145	OLMo
146	  & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
147	Qwen-cont
148	  & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
149	\bottomrule
150	\end{tabular}
151	\end{table}
152	
153	\begin{figure}[t]
154	\centering
155	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
156	\caption{Cross-model transfer heatmap (6-class ordinal accuracy).
157	Rows: training model; columns: test model.
158	Pythia$\leftrightarrow$OLMo (both continuation mode) shows high
159	mutual transfer (90--92\% accuracy retention), while Qwen-rewrite
160	transfers poorly to continuation-mode models (61--63\%).
161	Diagonal entries are within-model baselines.}
162	\label{fig:transfer_heatmap}
163	\end{figure}
164	
165	Two principal findings emerge (Figure~\ref{fig:transfer_heatmap}).
166	First, transfer between continuation-mode models is high.
167	Pythia$\to$OLMo retains 90--92\% of within-model accuracy, and
168	the reverse direction is comparable
169	(85--86\% retention by Kendall $\tau$).
170	The accuracy-based retention of 90--92\% is complemented by the
171	$\tau$-based retention of 85--86\%, indicating that not only
172	classification accuracy but also the relative depth ordering of
173	predictions is largely preserved.
174	Qwen-cont$\leftrightarrow$Pythia also transfers well
175	(84--85\% accuracy retention),
176	and Qwen-cont$\leftrightarrow$OLMo achieves 80--85\%.
177	These retention rates---80--92\% of within-model accuracy preserved across continuation-mode pairs---suggest that a large component of the depth signal is text-intrinsic rather than tied to a specific generator.
178	
179	Second, Qwen-rewrite exhibits catastrophic transfer failure.
180	Classifiers trained on Qwen-rewrite retain only 61--63\% of
181	within-model accuracy when evaluated on Pythia or OLMo
182	(45--50\% by $\tau$).
183	The reverse direction transfers asymmetrically: Pythia/OLMo${\to}$Qwen-rw retains 70--72\% of within-model accuracy, higher than the forward 61--63\% but still far below continuation-mode transfer rates (80--92\%).
184	This confirms that rewrite-mode classifiers rely on generation
185	artifacts that do not generalize across models, in contrast
186	to Qwen-cont, which achieves 80--85\% retention to the same targets.
187	
188	At the 0v1 boundary, cross-model pairwise $\auc$ exceeds 0.96
189	for all model pairs, confirming that the human-vs.-synthetic
190	distinction is universally transferable regardless of generator
191	or mode.
192	The transfer degradation concentrates at deeper boundaries
193	(1v2 and beyond), where model- and mode-specific factors dominate.
194	
195	The aggregate picture is one of modest cross-model loss:
196	mean pairwise $\auc$ is 0.6099 within-model versus 0.5905
197	cross-model.
198	This gap is driven primarily by Qwen-rewrite; among
199	continuation-mode pairs the within/cross difference narrows
200	further.
201	
202	%% ====================================================================
203	\subsection{Feature Degradation Ordering}
204	\label{sec:feature_degradation}
205	
206	The transfer results indicate that depth signals are largely text-intrinsic.
207	We next ask what drives discrimination: if the signal is text-intrinsic, different generators should rely on the same features in the same order.
208	We test this by computing single-feature $\auc$ rankings
209	independently for each model and comparing them via rank
210	correlation.
211	
212	\begin{table}[t]
213	\centering
214	\small
215	\caption{Top-3 features by single-feature $\auc$ ranking for each
216	model configuration.
217	Features shared across all three continuation-mode models are in bold.
218	Qwen-rewrite's top feature (\texttt{freq\_entropy}) is mode-specific.
219	Spearman $\rho$ (continuation-mode pairs): Pythia--OLMo 0.95,
220	Pythia--Qwen-cont 0.9143, OLMo--Qwen-cont 0.85.}
221	\label{tab:top_features}
222	\begin{tabular}{cllll}
223	\toprule
224	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
225	\midrule
226	1
227	  & \textbf{\texttt{surp\_d1\_std}}
228	  & \textbf{\texttt{surp\_std}}
229	  & \texttt{freq\_entropy}
230	  & \textbf{\texttt{surp\_d1\_std}} \\
231	2
232	  & \textbf{\texttt{surp\_d2\_std}}
233	  & \textbf{\texttt{surp\_d1\_std}}
234	  & \textbf{\texttt{surp\_std}}
235	  & \textbf{\texttt{surp\_std}} \\
236	3
237	  & \textbf{\texttt{surp\_std}}
238	  & \textbf{\texttt{surp\_d2\_std}}
239	  & \textbf{\texttt{surp\_d1\_std}}
240	  & \textbf{\texttt{surp\_d2\_std}} \\
241	\bottomrule
242	\end{tabular}
243	\end{table}
244	
245	Among continuation-mode models, single-feature $\auc$ rankings
246	are highly correlated:
247	Pythia vs.\ OLMo $\rho = 0.95$,
248	Pythia vs.\ Qwen-cont $\rho = 0.9143$,
249	OLMo vs.\ Qwen-cont $\rho = 0.85$
250	(all $\rho \geq 0.85$).
251	The top-3 features---\texttt{surp\_d1\_std}, \texttt{surp\_std},
252	and \texttt{surp\_d2\_std}---are shared (up to ordering) across
253	all three continuation-mode configurations
254	(Table~\ref{tab:top_features}).
255	All three measure variability of surprisal or its derivatives,
256	capturing the \emph{heterogeneity} of token-level predictability
257	across the text.
258	That these features degrade in a shared order across generators
259	suggests a common mechanism: each generation step smooths the
260	token-level surprisal landscape, reducing its variance in a
261	model-independent fashion.
262	
263	Qwen-rewrite diverges: its top-ranked feature is
264	\texttt{freq\_entropy}, a lexical diversity measure absent from
265	the continuation-mode top-3 for any model.
266	This corroborates the transfer results in
267	Section~\ref{sec:transfer}---rewrite-mode classifiers learn
268	partly from instruction-following artifacts rather than the
269	shared surprisal-based signals.
270	
271	Kendall $\tau$ provides a complementary, more conservative
272	perspective:
273	Pythia vs.\ OLMo $\tau = 0.733$,
274	Pythia vs.\ Qwen-cont $\tau = 0.695$,
275	OLMo vs.\ Qwen-cont $\tau = 0.543$.
276	Cross-mode correlations are lower:
277	Pythia vs.\ Qwen-rw $\tau = 0.467$,
278	OLMo vs.\ Qwen-rw $\tau = 0.429$.
279	
280	\paragraph{Limitation.}
281	The high Spearman $\rho$ characterizes the \emph{aggregate}
282	feature ranking, but at the depth-pair level the agreement
283	weakens: $\tau \approx 0.37$ at the 1v2 boundary.
284	This means that while the overall importance ordering is shared,
285	the relative contribution of individual features at the
286	discrimination boundary---where precision matters most---varies
287	across models.
288	We view this as a genuine limitation of the text-intrinsic
289	interpretation and a direction for future investigation.
290	
291	%% ====================================================================
292	\subsection{Generation Mode Effect}
293	\label{sec:generation_mode}
294	
295	Finally, we ask whether generation mode---an experimental design choice rather than a text property---affects depth detectability.
296	Qwen2.5-1.5B-Instruct provides a controlled comparison: rewrite (instruction-based paraphrasing) and continuation (prompt truncation) share the same model weights, as defined in Section~\ref{sec:method}, isolating the effect of generation protocol.
297	
298	Rewrite mode yields higher 1v2 $\auc$ than continuation:
299	0.6955 vs.\ 0.6112, a difference of $+$8.4 percentage points.
300	The advantage persists at 2v3
301	(0.5893 vs.\ 0.5609, $\Delta = +$2.8\,pp)
302	and narrows at 3v4
303	(0.5435 vs.\ 0.5409, $\Delta = +$0.3\,pp),
304	with both modes converging toward chance at deeper levels.
305	The amplified detectability under rewrite mode is consistent
306	with instruction-following introducing systematic deviations
307	from the source text's style---additional artifacts that are
308	discriminable but mode-specific rather than text-intrinsic.
309	
310	Transfer between modes is asymmetric.
311	A classifier trained on Qwen-cont and evaluated on Qwen-rw
312	retains 89\% of within-model accuracy
313	(0.3440 vs.\ 0.3875 diagonal),
314	whereas the reverse direction---Qwen-rw trained,
315	Qwen-cont tested---retains 82\%
316	(0.3466 vs.\ 0.4229 diagonal).
317	The direction of the asymmetry is intuitive:
318	continuation-mode signals form a subset of the information
319	available in rewrite-mode data
320	(which adds instruction-following artifacts on top),
321	so a continuation-trained classifier can partially recognize
322	rewrite-mode outputs but not vice versa.
323	
324	This asymmetry is mirrored in the feature rankings.
325	Qwen-rewrite's top feature (\texttt{freq\_entropy}) is
326	mode-specific and ranks outside the top-3 for every
327	continuation-mode model.
328	Qwen-cont's top feature (\texttt{surp\_d1\_std}) is shared
329	with Pythia and OLMo, confirming that continuation mode
330	captures primarily text-intrinsic depth signals.
331	
332	The practical implication is a detectability--generalizability
333	tradeoff.
334	Rewrite-mode classifiers achieve higher absolute $\auc$ but
335	transfer poorly across models
336	(Qwen-rw$\to$Pythia/OLMo: 61--63\% retention).
337	Continuation-mode classifiers sacrifice 8.4\,pp of within-model
338	$\auc$ but achieve robust cross-model transfer
339	(Qwen-cont$\to$Pythia: 84--85\%).
340	For deployment scenarios requiring model-agnostic depth
341	estimation, continuation-mode features provide a more reliable
342	foundation despite lower raw discriminability.
343	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae3e8f41-8d60-43d6-9151-b31ea6a7ce2d",
  "isSidechain": true,
  "promptId": "3767a4dd-8323-40d5-adc2-11298901ddbf",
  "agentId": "ae896b46dd4096f76",
  "type": "user",
  "uuid": "1a99ee5e-adcc-45fb-b9aa-b1a662c0d14c",
  "sourceToolAssistantUUID": "ae3e8f41-8d60-43d6-9151-b31ea6a7ce2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "de623504-6717-4729-8094-7e6a85d35da7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-petting-backus"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T00:43:09.055Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J82FRJCYEQ27326mLgzd9Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a99ee5e-adcc-45fb-b9aa-b1a662c0d14c",
  "isSidechain": true,
  "agentId": "ae896b46dd4096f76",
  "requestId": "req_011Cb1XvfCs6GiqWaULBe6R5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "05b828ab-1c43-4457-a3c4-ad42bead9cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "de623504-6717-4729-8094-7e6a85d35da7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-petting-backus",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PqaEQpvETU9GyJQemFtjo1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20957,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20957,
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

_source line 6 · 2026-05-14T00:43:09.061Z_

<details><summary>↩ Tool result · `toolu_01J82FRJCYEQ27326mLgzd9Y`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Each pass through a language model constitutes a lossy channel: first-generation synthetic text retains much of the information structure of its human-written source, but by the fourth generation the output is qualitatively different---tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
6	This recursive degradation is not merely a theoretical concern; as synthetic text proliferates on the open web, training corpora inevitably ingest documents at varying generational depths, amplifying the risk of model collapse in downstream systems.
7	Yet the dominant paradigm in synthetic text detection treats all machine-generated text identically: a document is classified as human or synthetic, with no regard for how many rounds of recursive generation it has undergone.
8	This binary framing discards the generational depth dimension entirely.
9	
10	The gap cuts across three research communities.
11	Binary detection methods---including DivEye~\cite{basani2026diveye}, Min-K\%++~\cite{zhang2024minkpp}, and CoDeC~\cite{zawalski2026codec}---achieve strong human-versus-machine separation but produce no depth estimate.
12	The model collapse literature provides macro-level characterizations of recursive degradation: Shumailov et al.~\cite{shumailov2024collapse} demonstrated irreversible tail loss, Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved convergence to a fixed point, and Schaeffer et al.~\cite{schaeffer2025position} organized the field into a taxonomy of eight definitions---yet none of these works provides a tool for estimating the generational depth of an individual text.
13	Data selection methods such as DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2024d4}, and DoReMi~\cite{xie2024doremi} perform distribution matching to improve corpus quality but ignore recursive depth altogether.
14	The closest prior work is Drayson et al.~\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling to prevent model collapse---but their approach remains fundamentally binary.
15	No existing method estimates how many rounds of recursive generation a text has undergone, nor quantifies the boundary beyond which such estimation becomes infeasible.
16	
17	Recursive generation forms an iterated lossy channel; the Data Processing Inequality guarantees that the original signal degrades monotonically across generations, motivating the existence of a finite discrimination boundary $\Kstar$ beyond which adjacent generations become indistinguishable.
18	Markov chain convergence further implies that adjacent-generation distributions converge to a shared stationary distribution, so the classifier's task grows harder with each step.
19	Motivated by this theoretical structure, we set out to empirically measure $\Kempirical$---the maximum depth at which a classifier can reliably distinguish adjacent generations.
20	Our approach combines a 15-dimensional statistical feature pipeline---capturing surprisal moments, surprisal derivatives, vocabulary diversity, and frequency tail statistics---with an Ordinal Binary Decomposition (OBD) LightGBM classifier that respects the ordinal structure of depth.
21	We operationalize $\Kempirical$ as the deepest generation at which adjacent depths remain statistically distinguishable, with the bootstrap 95\% CI for pairwise $\auc$ exceeding an operational threshold $\theta = 0.60$ (formal definition in Section~\ref{sec:method}).
22	The choice of interpretable statistical features---rather than learned representations---is deliberate: it enables cross-generator transfer without retraining and permits attribution of discriminative power to specific text properties.
23	
24	Our contributions are organized into two groups.
25	The primary contribution is a systematic empirical characterization of $\Kempirical$ and its properties:
26	
27	\begin{enumerate}[label=(\alph*)]
28	  \item \textbf{$\Kempirical = 2$: a consistent boundary across all tested conditions.}
29	    Across 4 model-mode configurations and 4 decoding strategies (8 conditions total), all 1v2 bootstrap CI lower bounds exceed $\theta = 0.60$ and all 2v3 CI upper bounds fall below $\theta$, with permutation $p \leq 0.002$ for all boundary comparisons.
30	    The most marginal case is Qwen-cont, where $\text{CI}_\text{lower} = 0.6015$.
31	    $\Kempirical = 2$ is thus established as a consistent discrimination boundary across all 8 tested conditions at $\leq$1.5B scale, suggesting universality beyond the specific models and decoding strategies studied.
32	    Higher decoding entropy increases signal strength ($\auc_{1,2}$: $0.69$ greedy $\to$ $0.70$ at $T{=}1.2$) but does not shift the boundary.
33	
34	  \item \textbf{Cross-model transfer.}
35	    Classifiers trained on one continuation-mode model and evaluated on another retain 80--92\% of within-model accuracy (Pythia$\leftrightarrow$OLMo: 90--92\%).
36	    At the 0v1 boundary, cross-model $\auc$ exceeds 0.96 universally.
37	    Transfer retention of 80--92\% suggests a large text-intrinsic component of the depth signal, rather than generator-specific artifacts.
38	
39	  \item \textbf{Degradation ordering consistency.}
40	    Single-feature $\auc$ rankings are highly correlated across continuation-mode models (Spearman $\rho \geq 0.85$), with the same top features---\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}---appearing across all three families.
41	    This shared ordering suggests a common degradation mechanism: each generation step smooths the token-level surprisal landscape.
42	    A limitation is that depth-pair-level agreement weakens ($\tau \approx 0.37$ at 1v2), indicating that individual feature contributions at the boundary vary across models.
43	
44	  \item \textbf{Generation mode analysis.}
45	    Within Qwen2.5-1.5B-Instruct, rewrite mode yields 1v2 $\auc = 0.6955$ versus continuation's $0.6112$ ($\Delta = +8.4$\,pp), but rewrite-trained classifiers transfer poorly across models (61--63\% retention versus 80--92\% for continuation).
46	    Cross-mode transfer is asymmetric: continuation$\to$rewrite retains 89\% while rewrite$\to$continuation retains 82\%.
47	    Continuation mode is therefore recommended as the canonical condition for cross-model comparisons.
48	\end{enumerate}
49	
50	\noindent As a secondary contribution, we investigate whether the coarse 3-class ordinal signal implied by $\Kempirical = 2$ enables \emph{graduated filtering}---depth-aware data curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\geq 3$)---and whether such filtering can improve upon binary approaches that discard all synthetic content indiscriminately (Section~\ref{sec:experiments}).
51	
52	The remainder of this paper is organized as follows.
53	Section~\ref{sec:related_work} reviews related work.
54	Section~\ref{sec:method} describes the method.
55	Section~\ref{sec:experiments} presents experimental results.
56	Section~\ref{sec:conclusion} concludes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05b828ab-1c43-4457-a3c4-ad42bead9cff",
  "isSidechain": true,
  "promptId": "3767a4dd-8323-40d5-adc2-11298901ddbf",
  "agentId": "ae896b46dd4096f76",
  "type": "user",
  "uuid": "15fdf0a7-b488-4708-a623-5f36308e5901",
  "sourceToolAssistantUUID": "05b828ab-1c43-4457-a3c4-ad42bead9cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "de623504-6717-4729-8094-7e6a85d35da7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-petting-backus"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T00:43:09.206Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NYB84MpUsNAEQPEgcVTW7h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15fdf0a7-b488-4708-a623-5f36308e5901",
  "isSidechain": true,
  "agentId": "ae896b46dd4096f76",
  "requestId": "req_011Cb1XvfCs6GiqWaULBe6R5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "be1aeff8-14a4-49e9-bd63-6e753eda3fa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "de623504-6717-4729-8094-7e6a85d35da7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-petting-backus",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PqaEQpvETU9GyJQemFtjo1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20957,
      "cache_read_input_tokens": 0,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 250,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 20957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20957,
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

_source line 8 · 2026-05-14T00:43:09.219Z_

<details><summary>↩ Tool result · `toolu_01NYB84MpUsNAEQPEgcVTW7h`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	\label{sec:discuss_kstar}
6	
7	The Data Processing Inequality guarantees the existence of a finite $\Ktheory$ beyond which adjacent generations become indistinguishable (Section~\ref{sec:formulation}).
8	Our empirical result---$\Kempirical = 2$ uniformly across all 8 tested configurations (4 model-mode combinations from Section~\ref{sec:kstar_boundary} and 4 decoding strategies from the ablation)---establishes that this boundary is not only finite but remarkably shallow at the $\leq$1.5B parameter scale.
9	
10	The shallowness of $\Kempirical$ is explained by the rate of information loss across generations.
11	The 0v1 boundary is near-trivially separable ($\auc > 0.99$ across all configurations), reflecting the large distributional gap between human text and first-generation synthetic text.
12	At the 1v2 boundary, $\auc$ drops by approximately 30 percentage points ($\auc$ range: 0.6112--0.6955), indicating that the majority of the discriminative signal is consumed in the first generation step.
13	By the 2v3 boundary, $\auc$ falls to 0.5496--0.5893---below the operational threshold $\theta = 0.60$---and deeper pairs converge toward chance.
14	Recursive generation thus acts as a severely lossy channel whose information bottleneck is traversed within two steps.
15	
16	The feature degradation analysis (Section~\ref{sec:feature_degradation}) provides mechanistic evidence for this rapid collapse.
17	The most discriminative features---surprisal variance (\texttt{surp\_d1\_std}, \texttt{surp\_std}) and its derivatives---all capture the heterogeneity of token-level predictability.
18	Human text exhibits high surprisal variance reflecting diverse syntactic structures and unpredictable discourse patterns.
19	The first generation step smooths this variance substantially, replacing high-surprisal tokens and atypical constructions with more predictable alternatives; the second step reduces the remaining variance to near-floor levels, leaving insufficient statistical fingerprint for reliable adjacent-depth discrimination.
20	Crucially, this degradation ordering is consistent across model families (Spearman $\rho \geq 0.85$ for all continuation-mode pairs), suggesting that the two-step information loss is governed by the autoregressive generation mechanism itself rather than by model-specific biases.
21	
22	This pattern aligns with findings from the model collapse literature.
23	Shumailov et al.~\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations, with minority modes vanishing before the output distribution stabilizes.
24	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws demonstrating that tail probability mass is lost at rates predictable from model and data scale.
25	Our $\Kempirical = 2$ provides a complementary, classifier-based measurement of this phenomenon: the information-theoretic discrimination horizon is reached after just two generation steps.
26	Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved convergence to a fixed point for self-consuming generative models; $\Kempirical = 2$ indicates that, operationally, the approach to this fixed point is rapid enough that adjacent-generation distinctions collapse within two steps.
27	
28	The invariance of $\Kempirical = 2$ across decoding strategies merits emphasis.
29	Greedy decoding, nucleus sampling ($p{=}0.9$), $T{=}0.7$, and $T{=}1.2$ all yield $\Kempirical = 2$, with 1v2 $\auc$ spanning a narrow range of [0.6866, 0.7039].
30	Higher decoding entropy modestly increases signal strength ($\auc_{1,2}$: 0.69 greedy $\to$ 0.70 at $T{=}1.2$) but does not shift the boundary.
31	This robustness suggests that $\Kempirical$ is governed by the fundamental information bottleneck of the generation process rather than by surface-level properties of the sampling algorithm.
32	
33	\subsection{Implications of Cross-Model Transfer}
34	\label{sec:discuss_transfer}
35	
36	The cross-model transfer results (Section~\ref{sec:transfer}) indicate that depth signals are largely encoded in text-level statistical properties rather than generator-specific artifacts.
37	Classifiers trained on Pythia-1.4B and evaluated on OLMo-1B retain 90--92\% of within-model accuracy, and the broader continuation-mode transfer matrix shows 80--92\% retention across all model pairs.
38	At the 0v1 boundary, cross-model $\auc$ exceeds 0.96 universally, confirming that binary contamination detection is fully transferable across generators.
39	
40	The practical implication is direct: a single depth classifier trained on one model's outputs can be deployed to estimate generational depth for texts produced by other models, without model-specific retraining.
41	This transferability extends the utility of depth estimation to open-web settings where the generating model is unknown---precisely the scenario where depth-aware data curation is most needed.
42	
43	Two caveats bound this conclusion.
44	First, the retention rates suggest that depth signals are approximately 70--85\% text-intrinsic and 15--30\% attributable to model self-familiarity, estimated from the off-diagonal transfer retention across continuation-mode pairs.
45	This decomposition is approximate---it assumes linearity in the accuracy-retention metric---but the magnitude is informative: the text-intrinsic component dominates, yet a nontrivial model-specific residual persists.
46	The Pythia$\leftrightarrow$OLMo pair, which spans different architectures and training corpora, achieves the highest cross-family retention (91--92\%), consistent with the depth signal being largely architecture-agnostic within continuation mode.
47	Second, Qwen-cont$\leftrightarrow$OLMo retention (80--85\%) is lower than Pythia$\leftrightarrow$OLMo (91--92\%), indicating that model family similarity modulates transfer even among continuation-mode configurations.
48	
49	\subsection{Feature Importance Across Decoding Strategies}
50	\label{sec:discuss_features}
51	
52	While $\Kempirical = 2$ is invariant to decoding strategy (4/4 configurations), the feature importance ordering is not uniformly consistent.
53	Greedy decoding and $T{=}0.7$ share highly correlated feature rankings (Spearman $\rho = 0.914$), with top features dominated by vocabulary diversity measures: \texttt{self\_bleu}, \texttt{hapax\_ratio}, and \texttt{ttr}.
54	In contrast, greedy versus $T{=}1.2$ yields a lower correlation ($\rho = 0.53$, $p = 0.041$; suggestive but nonsignificant after Bonferroni correction for 6 pairwise comparisons), with $T{=}1.2$ promoting \texttt{hapax\_ratio}, \texttt{ttr}, and \texttt{surp\_skew} to the top ranks.
55	Notably, \texttt{freq\_entropy} rises from rank~10 under greedy ($\auc = 0.5139$) to rank~5 under $T{=}1.2$ ($\auc = 0.5905$), illustrating how high-entropy decoding amplifies frequency-distribution artifacts.
56	
57	This dissociation reveals an important distinction: the \emph{existence} of the depth boundary is robust, but the \emph{optimal feature subset} for detecting it depends on the sampling strategy.
58	High-entropy decoding amplifies frequency-distribution artifacts while attenuating vocabulary-diversity signals, shifting which text properties carry the most discriminative power without altering whether adjacent generations can be distinguished.
59	For practitioners, this implies that a universal depth classifier should incorporate features from multiple groups---surprisal moments, vocabulary diversity, and frequency tail statistics---to maintain performance across unknown decoding conditions.
60	
61	The cross-model feature ordering (Section~\ref{sec:feature_degradation}) provides a complementary perspective: among continuation-mode models, single-feature $\auc$ rankings are highly consistent (Spearman $\rho \geq 0.85$), with surprisal-variance features---\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}---dominating uniformly.
62	A genuine limitation, however, is that depth-pair-level agreement weakens to $\tau \approx 0.37$ at the 1v2 boundary (Section~\ref{sec:feature_degradation}), indicating that the relative contribution of individual features at the discrimination boundary varies across models even when the aggregate ordering is shared.
63	
64	\subsection{LLM Zero-Shot Baseline}
65	\label{sec:discuss_llm}
66	
67	Frontier LLMs provide a natural baseline for depth estimation.
68	On a 500-sample test set with 5 depth classes (depths 0--4), GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10) and Claude Opus~4.6 achieves 33.1\% accuracy (MAE = 1.15)---both below the OBD-LightGBM baseline of 38.6\% (MAE = 1.11).
69	Simultaneously, both models achieve approximately 88\% binary accuracy on the human-vs.-synthetic distinction (GPT-5.5: 87.8\%, Claude: 88.2\%).
70	
71	This gap between binary detection and depth estimation is informative.
72	Frontier LLMs can reliably determine \emph{whether} a text is machine-generated but cannot estimate \emph{how many generations of recursive processing} it has undergone.
73	Depth estimation requires sensitivity to subtle distributional shifts between adjacent generations---shifts orders of magnitude smaller than the human-vs.-machine gap.
74	The 15-dimensional statistical feature pipeline, despite its simplicity, captures these fine-grained shifts more effectively than frontier LLMs in a zero-shot setting.
75	This motivates the dedicated feature-engineering approach: the task demands specialized statistical sensitivity rather than general language understanding.
76	
77	\subsection{Limitations}
78	\label{sec:limitations}
79	
80	We identify seven limitations that bound the generalizability of our findings.
81	
82	\emph{Model scale.}
83	All experiments use models at or below 1.5B parameters (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct).
84	Larger models may produce higher-fidelity text with weaker depth signatures, potentially shifting $\Kempirical$ beyond~2.
85	
86	\emph{Prompt-chain versus retrain-chain.}
87	Our recursive generation protocol is a prompt-chain: the same fixed model repeatedly generates from the previous output.
88	Real-world model collapse involves retrain-chains, where models are retrained on data from earlier generations~\cite{shumailov2024collapse}.
89	Retrain-chains introduce additional degradation through training dynamics, potentially producing different $\Kstar$ values.
90	
91	\emph{Language and domain.}
92	All experiments use English text from the C4 corpus.
93	Depth dynamics may differ across languages, domains (e.g., code, scientific text), and source corpora with different distributional properties.
94	
95	\emph{Decoding coverage.}
96	We test four decoding strategies (greedy, nucleus $p{=}0.9$, $T{=}0.7$, $T{=}1.2$).
97	Other strategies---top-$k$ sampling, beam search, contrastive decoding---remain untested and may yield different feature importance patterns or boundary behavior.
98	
99	\emph{Threshold sensitivity.}
100	$\Kempirical$ depends on the operational threshold $\theta$.
101	Sensitivity analysis across four decoding configurations shows $\Kempirical = 3$ at $\theta = 0.55$, $\Kempirical = 2$ for $\theta \in [0.60, 0.65]$, and $\Kempirical = 1$ at $\theta = 0.70$ (3 of 4 configurations).
102	The boundary is robust within a practical range but not invariant to threshold choice; our conclusions are conditioned on $\theta = 0.60$.
103	
104	\emph{Operational versus theoretical boundary.}
105	$\Kempirical$ is an operational lower bound that depends on the specific feature set and classifier.
106	$\Ktheory$ may be strictly greater; a more expressive classifier or richer feature representation could push $\Kempirical$ higher.
107	
108	\emph{Feature representation.}
109	The 15-dimensional hand-crafted feature set, while interpretable and transferable, is unlikely to be optimal.
110	Learned representations---fine-tuned embeddings or probing classifiers---may capture depth-discriminative patterns that statistical features miss, potentially achieving a higher $\Kempirical$.
111	
112	\paragraph{Graduated Filtering.}
113	% TODO: exp-006 graduated filtering 结果填充
114	
115	\subsection{Broader Impact}
116	\label{sec:broader_impact}
117	
118	The $\Kempirical = 2$ boundary has implications beyond the immediate scope of depth classification.
119	
120	\paragraph{Synthetic data curation.}
121	The practical consequence of $\Kempirical = 2$ is a three-tier taxonomy of text quality: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
122	Texts at depth~$\geq 2$ are mutually indistinguishable and can be treated as a single category for curation purposes.
123	For practitioners filtering training data, this implies that a single round of synthetic rewriting suffices to make text statistically indistinguishable from text that has undergone multiple rounds of recycling---a form of one-wash laundering that limits the granularity of quality-based filtering.
124	Graduated filtering strategies that exploit this trichotomy may outperform binary human/synthetic filters, as the coarse ordinal signal (human / shallow / deep) captures the dominant axis of quality variation.
125	
126	\paragraph{Relation to model collapse.}
127	Shumailov et al.~\cite{shumailov2024collapse} and Alemohammad et al.~\cite{alemohammad2024selfconsuming} study model collapse under \emph{retrain-chains}, where models are iteratively trained on their own outputs.
128	Our prompt-chain protocol measures an adjacent but distinct phenomenon: the degradation of statistical distinguishability under recursive generation by a fixed model.
129	The rapid convergence we observe ($\Kempirical = 2$) is consistent with the theoretical prediction of convergence to a fixed point, but the precise relationship between prompt-chain $\Kempirical$ and retrain-chain convergence rates remains an open question.
130	If prompt-chain depth signals serve as an observable proxy for early-stage model collapse, depth estimation could provide a lightweight diagnostic for data curation pipelines without requiring expensive retraining experiments.
131	
132	\paragraph{AI text detection.}
133	Current AI text detection is predominantly binary: human versus machine.
134	Our results suggest that \emph{depth-aware} detection provides a strictly more informative signal.
135	The near-perfect 0v1 separability ($\auc > 0.99$) confirms that binary detection is reliable at this scale, but the 1v2 boundary ($\auc$: 0.61--0.70) reveals that first-generation text retains measurable statistical distance from deeper synthetic text.
136	This additional dimension---how many generations of processing a text has undergone---may prove valuable for provenance tracking and corpus quality assessment, where the binary human/AI label elides important distinctions between lightly and heavily recycled content.
137	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be1aeff8-14a4-49e9-bd63-6e753eda3fa8",
  "isSidechain": true,
  "promptId": "3767a4dd-8323-40d5-adc2-11298901ddbf",
  "agentId": "ae896b46dd4096f76",
  "type": "user",
  "uuid": "3a05c7be-b6fb-49fc-8e91-3e5a3c79414b",
  "sourceToolAssistantUUID": "be1aeff8-14a4-49e9-bd63-6e753eda3fa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "de623504-6717-4729-8094-7e6a85d35da7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-petting-backus"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-14T00:43:20.951Z_

I have read all three files. Here are the exact findings for each location you requested:

## 1. experiments_c1.tex

**Around line 30 (table note for Qwen-cont 0v1):**
- Line 30 reads: "All 0v1 permutation $p \leq 0.002$ (Qwen-cont 0v1: CI [0.9963, 0.9978], $p = 0.000$)."
- **p-value: 0.000** (not 0.002)
- **AUC value**: Looking at the table itself, line 36 shows "0v1 & 0.9956 & 0.9932 & 0.9970 & 0.9972" where Qwen-cont is the rightmost value = **0.9972** (not 0.9971)
- The confidence interval is [0.9963, 0.9978]

**Around line 167 (Pythia→OLMo transfer retention):**
- Lines 166-169 state: "Pythia$\to$OLMo retains 90--92\% of within-model accuracy, and the reverse direction is comparable (85--86\% retention by Kendall $\tau$)."
- **Transfer retention: 90--92%** for Pythia→OLMo (accuracy-based)

## 2. introduction.tex

**Line 5 (wording about "fourth generation"):**
- Line 5 reads: "...but by the fourth generation the output is qualitatively different---tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}."
- The wording uses "fourth generation" directly.

**Lines 52-56 (paper structure paragraph):**
- Lines 52-56 read:
  ```
  The remainder of this paper is organized as follows.
  Section~\ref{sec:related_work} reviews related work.
  Section~\ref{sec:method} describes the method.
  Section~\ref{sec:experiments} presents experimental results.
  Section~\ref{sec:conclusion} concludes.
  ```
- **Does NOT mention Discussion section** — it goes directly from experiments to conclusion.

**Line 31 (D017 claim wording):**
- Line 31 reads: "$\Kempirical = 2$ is thus established as a consistent discrimination boundary across all 8 tested conditions at $\leq$1.5B scale, suggesting universality beyond the specific models and decoding strategies studied."
- There is no explicit "D017" label in the introduction. Line 31 is part of claim (a) about $\Kempirical = 2$.

## 3. discussion.tex

**Section 5.3 (around lines 49-62) — T=1.2 top features:**
- Line 54 states: "...with $T{=}1.2$ promoting \texttt{hapax\_ratio}, \texttt{ttr}, and \texttt{surp\_skew} to the top ranks."
- Line 55 continues: "Notably, \texttt{freq\_entropy} rises from rank~10 under greedy ($\auc = 0.5139$) to rank~5 under $T{=}1.2$ ($\auc = 0.5905$)..."
- **T=1.2 top features: hapax_ratio, ttr, surp_skew** (as expected)
- **freq_entropy is at rank 5, not in the top 3** — this appears to already be corrected in the current version

The files appear to be in a clean state. The key findings are:
- Qwen-cont 0v1: p=0.000, AUC=0.9972 ✓
- Pythia→OLMo transfer: 90--92% ✓
- Introduction doesn't mention Discussion section
- T=1.2 features are correct (hapax_ratio, ttr, surp_skew) with freq_entropy at rank 5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a05c7be-b6fb-49fc-8e91-3e5a3c79414b",
  "isSidechain": true,
  "agentId": "ae896b46dd4096f76",
  "requestId": "req_011Cb1XvoThpCLVpBv7GRpnm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "339e14c1-eab2-44a5-9adf-284bf96c3597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "de623504-6717-4729-8094-7e6a85d35da7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-petting-backus",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UCGHtHgJt2mgWVWJZE4VbU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12969,
      "cache_read_input_tokens": 20957,
      "output_tokens": 986,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12969
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 986,
          "cache_read_input_tokens": 20957,
          "cache_creation_input_tokens": 12969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12969,
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
