# research ref audit C — Part 2 of 2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../research-ref-audit-c.md) · [Structured JSON](../../../sessions/2a/2a5362dc626ba0aad254.json)

## Round 7

### Tool result

_source line 389 · 2026-05-26T10:22:27.884Z_

<details><summary>↩ Tool result · `toolu_01Rk2pQ8txd9qdYgRDy1Vpma`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=0.75\columnwidth]{figures/fig1_daf_scatter.pdf}
7	\caption{Per-task death rate differential vs.\ performance gap ($n{=}11$ task types). The near-perfect correlation ($r = 0.97$) is a structural consequence of death dominance (DAF $\to 1 \Rightarrow r \to 1$), not an independent finding. The sole outlier (\texttt{find-non-living-thing}, diamond marker) has zero deaths; its $\Delta_{\text{full}} = +9.58$ arises entirely from non-death score differences.}
8	\label{fig:decomposition}
9	\end{figure}
10	
11	\begin{table}[t]
12	\centering
13	\scriptsize
14	\resizebox{\columnwidth}{!}{%
15	\begin{tabular}{@{}lrr@{}}
16	\toprule
17	Condition & Death\% & $N$ \\
18	\midrule
19	Single-trial baseline & 42.9 & 245 \\
20	Reflexion ($3{\times}$) & 31.4 & 220 \\
21	Qwen2.5-72B ($10{\times}$) & 30.6 & 255 \\
22	Deterministic baseline & 16.3 & 245 \\
23	\midrule
24	\multicolumn{3}{@{}l}{\textit{10 death-prone tasks only:}} \\
25	Death-prone baseline & 48.0 & 200 \\
26	Retry ($5{\times}$) & 43.5 & 200 \\
27	\bottomrule
28	\end{tabular}}
29	\caption{Internal-strategy death rates under improvement methods. Top: all 11 tasks. Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded). No intervention approaches deterministic-level safety.}
30	\label{tab:agent-improvement}
31	\end{table}
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=0.95\columnwidth]{figures/death_action_timeline.pdf}
36	\vspace{-2mm}
37	\caption{Action sequences for 6 representative death episodes. The fatal \texttt{focus on} (arrow) appears in final steps after long \texttt{connect} sequences (``connect loop $\to$ fatal focus'').}
38	\label{fig:death-timeline}
39	\end{figure}
40	
41	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). An anti-cherry-picking analysis confirms death dominance holds in 18 of these 19 types ($\overline{\Delta\text{DR}} = +38.2$\,pp $>$ included tasks' $+28.7$\,pp; Appendix~\ref{app:per-task}), with extended validation on representative excluded tasks in Appendix~\ref{app:extended-validation}.
42	
43	\subsection{Death Avoidance Decomposition}
44	\label{sec:death-decomp}
45	
46	\begin{table}[t]
47	\centering
48	\scriptsize
49	\setlength{\tabcolsep}{2.5pt}
50	\resizebox{\columnwidth}{!}{%
51	\begin{tabular}{@{}lrrccc@{}}
52	\toprule
53	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
54	\midrule
55	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
56	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
57	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
58	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
59	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
60	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
61	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
62	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
63	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
64	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
65	\midrule
66	find-non-living$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
67	\midrule
68	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
69	\bottomrule
70	\end{tabular}}
71	\caption{Per-task decomposition. D\%: death rate for internal/deterministic. D/I/N: det-preferred / int-preferred / no-preference labels. $\dagger$\,Only task with zero deaths; $n{=}40$ (two batches).}
72	\label{tab:per-task}
73	\end{table}
74	
75	Of the 95 non-tie routing labels, 75 (78.9\%; 95\% CI: $[70.7\%, 87.0\%]$, episode-level bootstrap) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these, 54 are sole-signal labels where death was the only discriminator; at $P{=}0$ these reduce to ties, but the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}).
76	
77	DAF $= 90.4\%$ at $P{=}100$ ($\Delta_{\text{full}} = +29.60$, $\Delta_{\text{nd}} = +2.84$; 95\% CI$_{\text{DAF}}$: $[81.3\%, 99.1\%]$, episode-level bootstrap). The 78.9\% label fraction provides the more robust, penalty-invariant characterization (\S\ref{sec:daf}).
78	
79	\paragraph{Per-task structure.}
80	The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic; all 105 internal deaths are triggered by the \texttt{focus on} action (Appendix~\ref{app:failure-modes}). Per-task $\Delta$DR correlates with $\Delta_{\text{full}}$ at $r = 0.97$ (Figure~\ref{fig:decomposition}; leave-one-out and bootstrap robustness in Appendix~\ref{app:correlation}), a structural consequence of DAF$\to 1$ rather than an independent finding. Figure~\ref{fig:death-timeline} illustrates the typical death trajectory.
81	
82	\paragraph{Binary structure and robustness.}
83	All 10 death-prone task types produce 100\% death-asymmetry labels; only \texttt{find-non-living-thing} (zero deaths) produces non-death signal (SCI $= 0.21$; Appendix~\ref{app:sci}). Leave-one-task-out (Table~\ref{tab:loto-daf}) confirms robustness: removing any single task changes DAF by $\leq$3.0~pp. Bootstrap 95\% CIs: DAF $[81.3\%, 99.1\%]$; cluster-robust $[73.3\%, 100.0\%]$ ($K{=}11$; Appendix~\ref{app:wild-cluster}). Two replications (Gemma-2-9B-it; seed=123) converge within 0.7~pp.
84	
85	\subsection{Multi-Model Validation (7--9B Tier)}
86	\label{sec:cross-model}
87	
88	Llama-3.1-8B~\citep{llama3-2024} ($N{=}220$) and Gemma-2-9B-it~\citep{gemma2-2024} ($N{=}220$) independently replicate death dominance: DAF $= 88.2\%$ and $89.7\%$ respectively, with 10/10 directional consistency on death-prone tasks (Appendix~\ref{app:cross-model}; per-task CIs in Appendix~\ref{app:per-task-ci}). Three architecturally distinct families (Qwen, Llama, Gemma) converge on DAF $88$--$90\%$ (spread 2.2~pp), suggesting death dominance is an environment-level property. Scaling $10{\times}$ to two 70B-class models (\S\ref{sec:agent-improvement}) yields DAF${=}92.4$--$101.0\%$, indicating the pattern persists at larger scale.
89	
90	\begin{table}[t]
91	\centering
92	\scriptsize
93	\setlength{\tabcolsep}{2pt}
94	\resizebox{\columnwidth}{!}{%
95	\begin{tabular}{@{}llcrrrcl@{}}
96	\toprule
97	Model & Env & $n$ & Int DR & Det DR & $\Delta$DR & DAF [95\% CI] & Signal \\
98	\midrule
99	Qwen2.5-7B & SW & 245 & 42.9 & 16.3 & +26.5 & 90.4 [81.3, 99.1] & death \\
100	Llama-3.1-8B & SW & 220 & 41.4 & 11.4 & +30.0 & 88.2 [80.2, 95.1] & death \\
101	Gemma-2-9B & SW & 220 & 36.4 & 14.1 & +22.3 & 89.7 [79.5, 98.4] & death \\
102	Qwen2.5-72B & SW & 255 & 30.6 & 2.8 & +27.8 & 92.4 [86.1, 97.9] & death \\
103	Llama-70B & SW & 220 & 48.6 & 20.0 & +28.6 & 101.0 [95.3, 107.5] & death \\
104	\midrule
105	Qwen2.5-7B & ALF & 135 & 0 & 0 & 0 & 0 & info-asym \\
106	Llama-3.1-8B & ALF & 135 & 0 & 0 & 0 & 0 & info-asym \\
107	\midrule
108	Qwen2.5-7B & MATH & 795 & --- & --- & --- & --- & none \\
109	\bottomrule
110	\end{tabular}}
111	\caption{Cross-model and cross-environment summary. SW = ScienceWorld, ALF = ALFWorld. Death dominance replicates across three 7--9B families and intensifies under $10{\times}$ scaling; ALFWorld shows information-asymmetry signal; MATH shows none. DR = death rate (\%).}
112	\label{tab:cross-model-env}
113	\end{table}
114	
115	\begin{table}[t]
116	\centering
117	\scriptsize
118	\setlength{\tabcolsep}{3pt}
119	\resizebox{\columnwidth}{!}{%
120	\begin{tabular}{@{}lrrr@{}}
121	\toprule
122	Removed Task & $N_\text{rem}$ & DAF (\%) & $\Delta$ (pp) \\
123	\midrule
124	(none, full) & 245 & 78.9 & --- \\
125	\midrule
126	Find Non-Living$^\dagger$ & 205 & 100.0 & +21.1 \\
127	Lifespan Longest & 220 & 75.9 & $-$3.0 \\
128	Life Stages 1 & 225 & 76.7 & $-$2.2 \\
129	Lifespan Long+Short & 225 & 76.7 & $-$2.2 \\
130	Chemistry Mix & 225 & 77.0 & $-$1.9 \\
131	Grow Fruit & 225 & 77.3 & $-$1.7 \\
132	Inclined Plane & 225 & 77.3 & $-$1.7 \\
133	Freeze & 225 & 77.5 & $-$1.4 \\
134	Life Stages 2 & 225 & 77.5 & $-$1.4 \\
135	Melt Pt Unknown & 225 & 77.5 & $-$1.4 \\
136	Find Animal & 225 & 77.8 & $-$1.2 \\
137	\bottomrule
138	\end{tabular}}
139	\caption{Leave-one-task-out DAF sensitivity (label fraction). Removing any death-prone task changes DAF by $\leq$3.0\,pp. $\dagger$\,Sole death-free task; removal raises DAF to 100\% by construction.}
140	\label{tab:loto-daf}
141	\end{table}
142	
143	\subsection{Agent Improvement Baselines}
144	\label{sec:agent-improvement}
145	
146	We test whether agent-level improvement reduces death dominance (Table~\ref{tab:agent-improvement}). Retry (re-executing the episode without explicit reflection; $N{=}5$) yields marginal reduction ($43.5\%$ vs.\ $48.0\%$). Reflexion~\citep{reflexion-2023} reduces death to $31.4\%$ but the gap to deterministic remains $15.1$~pp; under matched-episode analysis ($N{=}3$), $\Delta_{\text{nd}} = -0.47$, yielding DAF${}>100\%$. Scaling to Qwen2.5-72B ($N{=}255$) reduces death rate to $30.6\%$ with DAF $= 92.4\%$ (95\% CI: $[86.1\%, 97.9\%]$). A second 70B model, Llama-3.1-70B ($N{=}220$), yields DAF $= 101.0\%$ ($[95.3\%, 107.5\%]$): death avoidance more than fully accounts for the gap. Both 70B-class models suggest that scaling does not attenuate death dominance.
147	
148	\paragraph{Dose-response analysis.}
149	We extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\ref{fig:dose-response}). Retry is nearly flat ($48.0\% \to 43.5\%$). Reflexion drops steeply to $34.0\%$ at $N{=}3$ ($\Delta = -13.5$~pp, $p = 0.003$) then stabilizes ($34$--$36.5\%$ for $N \geq 3$, pairwise $p > 0.5$); both the decline and plateau are well-powered (minimum detectable effect ${\sim}8$~pp at 80\% power; Appendix~\ref{app:dose-response}).
150	
151	\begin{figure}[t]
152	\centering
153	\includegraphics[width=\columnwidth]{figures/dose_response.pdf}
154	\caption{Death rate vs.\ trial count for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Reflexion drops steeply through $N{=}3$ then plateaus; Retry is nearly flat. Horizontal lines: 72B ($30.6\%$) and deterministic ($16.3\%$) baselines. Error bands: Wilson 95\% CIs.}
155	\label{fig:dose-response}
156	\end{figure}
157	
158	\subsection{Cross-Environment Boundary Probes}
159	\label{sec:math-contrast}
160	\label{sec:cross-env}
161	
162	We probe two environments as boundary cases to test the framework's specificity (Figure~\ref{fig:signal-reversal}). On MATH Level~4--5~\citep{math-2021} ($N{=}795$), internal reasoning and code-interpreter accuracy are near-identical ($73.5\%$ vs.\ $73.0\%$, $p = 0.81$): without a catastrophic failure mechanism, no routing signal emerges despite substantial task difficulty. ALFWorld~\citep{alfworld-2021} (135 games, no death mechanism, DAF $= 0\%$) shows 94.6\% of non-tie labels favoring the information-advantaged strategy (which enumerates admissible actions); Llama-3.1-8B replicates at 100\%. The framework identifies this qualitatively different mechanism, information asymmetry rather than death avoidance, without modification, indicating that DAF correctly attributes zero signal to death when none exists (full label distributions and per-task breakdowns in Appendix~\ref{app:cross-env-details}).
163	
164	\subsection{Baselines}
165	\label{sec:baselines}
166	
167	Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points (Table~\ref{tab:baselines}). Random routing ($-22.38$) falls between the two pure strategies, confirming that the gap is not an artifact of evaluation methodology. The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic, an \emph{oracle degeneracy} where perfect per-episode foresight provides marginal benefit over the trivial always-deterministic baseline (Appendix~\ref{sec:threshold-routing}).
168	
169	\subsection{Router Training: Inconclusive Results}
170	\label{sec:router-diagnostic}
171	
172	A Qwen3 LoRA router (0.6B--4B; Appendix~\ref{app:router-details}) trained on counterfactual labels shows flat step-level balanced accuracy ($56$--$59\%$) across all model scales; episode-level evaluation yields $47.1 \pm 2.2\%$, below majority-vote.\footnote{Consistent with noisy-label bounds~\citep{natarajan2013learning}: ${\sim}$88\% of step-level labels are uninformative with 90.5\%/3.7\% class imbalance (Appendix~\ref{app:seed-robustness}).} Leave-one-task-out degrades to chance ($50.0\%$), suggesting signal is a per-task-type constant rather than a learnable function of step-level observations. Deployed end-to-end, the best router (4B) scores $-10.70$, not exceeding always-deterministic ($-9.47$); this negative result is consistent with the death-dominance finding, as death avoidance cannot be predicted from pre-episode features when it depends on multi-step trajectory dynamics. Additional ablations (capacity scaling, generative routing, reasoning depth) are in Appendix~\ref{app:ablations}.
173	
174	\begin{figure}[t]
175	\centering
176	\includegraphics[width=0.95\columnwidth]{figures/signal_reversal.pdf}
177	\vspace{-2mm}
178	\caption{Cross-environment label distributions. ScienceWorld and ALFWorld both favor deterministic via different mechanisms (death avoidance vs.\ information asymmetry); MATH shows no routing signal.}
179	\label{fig:signal-reversal}
180	\end{figure}
181	
182	\begin{table}[t]
183	\centering
184	\small
185	\resizebox{\columnwidth}{!}{%
186	\begin{tabular}{@{}lccc@{}}
187	\toprule
188	Strategy & Score & 95\% CI & Death \% \\
189	\midrule
190	Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
191	Always-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
192	Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
193	Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
194	\midrule
195	Trained Router$^\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\
196	\bottomrule
197	\end{tabular}}
198	\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). $\dagger$\,Single seed (42); see Appendix~\ref{app:seed-robustness} for 8-seed robustness.}
199	\label{tab:baselines}
200	\end{table}
201	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "4face18e-b8be-4b8d-bcd8-eeabbb92a7cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig1_daf_scatter.pdf}\n\\caption{Per-task death rate differential vs.\\ performance gap ($n{=}11$ task types). The near-perfect correlation ($r = 0.97$) is a structural consequence of death dominance (DAF $\\to 1 \\Rightarrow r \\to 1$), not an independent finding. The sole outlier (\\texttt{find-non-living-thing}, diamond marker) has zero deaths; its $\\Delta_{\\text{full}} = +9.58$ arises entirely from non-death score differences.}\n\\label{fig:decomposition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\nCondition & Death\\% & $N$ \\\\\n\\midrule\nSingle-trial baseline & 42.9 & 245 \\\\\nReflexion ($3{\\times}$) & 31.4 & 220 \\\\\nQwen2.5-72B ($10{\\times}$) & 30.6 & 255 \\\\\nDeterministic baseline & 16.3 & 245 \\\\\n\\midrule\n\\multicolumn{3}{@{}l}{\\textit{10 death-prone tasks only:}} \\\\\nDeath-prone baseline & 48.0 & 200 \\\\\nRetry ($5{\\times}$) & 43.5 & 200 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Internal-strategy death rates under improvement methods. Top: all 11 tasks. Bottom: 10 death-prone tasks (\\texttt{find-non-living-thing} excluded). No intervention approaches deterministic-level safety.}\n\\label{tab:agent-improvement}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/death_action_timeline.pdf}\n\\vspace{-2mm}\n\\caption{Action sequences for 6 representative death episodes. The fatal \\texttt{focus on} (arrow) appears in final steps after long \\texttt{connect} sequences (``connect loop $\\to$ fatal focus'').}\n\\label{fig:death-timeline}\n\\end{figure}\n\nWe analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). An anti-cherry-picking analysis confirms death dominance holds in 18 of these 19 types ($\\overline{\\Delta\\text{DR}} = +38.2$\\,pp $>$ included tasks' $+28.7$\\,pp; Appendix~\\ref{app:per-task}), with extended validation on representative excluded tasks in Appendix~\\ref{app:extended-validation}.\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2.5pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrccc@{}}\n\\toprule\nTask & $n$ & $\\Delta_\\text{full}$ & D\\%\\textsubscript{int} & D\\%\\textsubscript{det} & D / I / N \\\\\n\\midrule\nid-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\\\\nlifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\\\\nlifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\\\\ninclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\\\\nfreeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\\\\nmeas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\\\\nid-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\\\\nfind-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\\\\ngrow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\\\\nchem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\\\\n\\midrule\nfind-non-living$^\\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\\\\n\\midrule\n\\textbf{All (11 tasks)} & \\textbf{245} & $\\mathbf{+29.60}$ & \\textbf{42.9} & \\textbf{16.3} & \\textbf{86 / 9 / 150} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Per-task decomposition. D\\%: death rate for internal/deterministic. D/I/N: det-preferred / int-preferred / no-preference labels. $\\dagger$\\,Only task with zero deaths; $n{=}40$ (two batches).}\n\\label{tab:per-task}\n\\end{table}\n\nOf the 95 non-tie routing labels, 75 (78.9\\%; 95\\% CI: $[70.7\\%, 87.0\\%]$, episode-level bootstrap) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these, 54 are sole-signal labels where death was the only discriminator; at $P{=}0$ these reduce to ties, but the labeling function itself is penalty-independent (Algorithm~\\ref{alg:labeling}).\n\nDAF $= 90.4\\%$ at $P{=}100$ ($\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{nd}} = +2.84$; 95\\% CI$_{\\text{DAF}}$: $[81.3\\%, 99.1\\%]$, episode-level bootstrap). The 78.9\\% label fraction provides the more robust, penalty-invariant characterization (\\S\\ref{sec:daf}).\n\n\\paragraph{Per-task structure.}\nThe internal strategy dies in 42.9\\% of episodes versus 16.3\\% for deterministic; all 105 internal deaths are triggered by the \\texttt{focus on} action (Appendix~\\ref{app:failure-modes}). Per-task $\\Delta$DR correlates with $\\Delta_{\\text{full}}$ at $r = 0.97$ (Figure~\\ref{fig:decomposition}; leave-one-out and bootstrap robustness in Appendix~\\ref{app:correlation}), a structural consequence of DAF$\\to 1$ rather than an independent finding. Figure~\\ref{fig:death-timeline} illustrates the typical death trajectory.\n\n\\paragraph{Binary structure and robustness.}\nAll 10 death-prone task types produce 100\\% death-asymmetry labels; only \\texttt{find-non-living-thing} (zero deaths) produces non-death signal (SCI $= 0.21$; Appendix~\\ref{app:sci}). Leave-one-task-out (Table~\\ref{tab:loto-daf}) confirms robustness: removing any single task changes DAF by $\\leq$3.0~pp. Bootstrap 95\\% CIs: DAF $[81.3\\%, 99.1\\%]$; cluster-robust $[73.3\\%, 100.0\\%]$ ($K{=}11$; Appendix~\\ref{app:wild-cluster}). Two replications (Gemma-2-9B-it; seed=123) converge within 0.7~pp.\n\n\\subsection{Multi-Model Validation (7--9B Tier)}\n\\label{sec:cross-model}\n\nLlama-3.1-8B~\\citep{llama3-2024} ($N{=}220$) and Gemma-2-9B-it~\\citep{gemma2-2024} ($N{=}220$) independently replicate death dominance: DAF $= 88.2\\%$ and $89.7\\%$ respectively, with 10/10 directional consistency on death-prone tasks (Appendix~\\ref{app:cross-model}; per-task CIs in Appendix~\\ref{app:per-task-ci}). Three architecturally distinct families (Qwen, Llama, Gemma) converge on DAF $88$--$90\\%$ (spread 2.2~pp), suggesting death dominance is an environment-level property. Scaling $10{\\times}$ to two 70B-class models (\\S\\ref{sec:agent-improvement}) yields DAF${=}92.4$--$101.0\\%$, indicating the pattern persists at larger scale.\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcrrrcl@{}}\n\\toprule\nModel & Env & $n$ & Int DR & Det DR & $\\Delta$DR & DAF [95\\% CI] & Signal \\\\\n\\midrule\nQwen2.5-7B & SW & 245 & 42.9 & 16.3 & +26.5 & 90.4 [81.3, 99.1] & death \\\\\nLlama-3.1-8B & SW & 220 & 41.4 & 11.4 & +30.0 & 88.2 [80.2, 95.1] & death \\\\\nGemma-2-9B & SW & 220 & 36.4 & 14.1 & +22.3 & 89.7 [79.5, 98.4] & death \\\\\nQwen2.5-72B & SW & 255 & 30.6 & 2.8 & +27.8 & 92.4 [86.1, 97.9] & death \\\\\nLlama-70B & SW & 220 & 48.6 & 20.0 & +28.6 & 101.0 [95.3, 107.5] & death \\\\\n\\midrule\nQwen2.5-7B & ALF & 135 & 0 & 0 & 0 & 0 & info-asym \\\\\nLlama-3.1-8B & ALF & 135 & 0 & 0 & 0 & 0 & info-asym \\\\\n\\midrule\nQwen2.5-7B & MATH & 795 & --- & --- & --- & --- & none \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model and cross-environment summary. SW = ScienceWorld, ALF = ALFWorld. Death dominance replicates across three 7--9B families and intensifies under $10{\\times}$ scaling; ALFWorld shows information-asymmetry signal; MATH shows none. DR = death rate (\\%).}\n\\label{tab:cross-model-env}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nRemoved Task & $N_\\text{rem}$ & DAF (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n(none, full) & 245 & 78.9 & --- \\\\\n\\midrule\nFind Non-Living$^\\dagger$ & 205 & 100.0 & +21.1 \\\\\nLifespan Longest & 220 & 75.9 & $-$3.0 \\\\\nLife Stages 1 & 225 & 76.7 & $-$2.2 \\\\\nLifespan Long+Short & 225 & 76.7 & $-$2.2 \\\\\nChemistry Mix & 225 & 77.0 & $-$1.9 \\\\\nGrow Fruit & 225 & 77.3 & $-$1.7 \\\\\nInclined Plane & 225 & 77.3 & $-$1.7 \\\\\nFreeze & 225 & 77.5 & $-$1.4 \\\\\nLife Stages 2 & 225 & 77.5 & $-$1.4 \\\\\nMelt Pt Unknown & 225 & 77.5 & $-$1.4 \\\\\nFind Animal & 225 & 77.8 & $-$1.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Leave-one-task-out DAF sensitivity (label fraction). Removing any death-prone task changes DAF by $\\leq$3.0\\,pp. $\\dagger$\\,Sole death-free task; removal raises DAF to 100\\% by construction.}\n\\label{tab:loto-daf}\n\\end{table}\n\n\\subsection{Agent Improvement Baselines}\n\\label{sec:agent-improvement}\n\nWe test whether agent-level improvement reduces death dominance (Table~\\ref{tab:agent-improvement}). Retry (re-executing the episode without explicit reflection; $N{=}5$) yields marginal reduction ($43.5\\%$ vs.\\ $48.0\\%$). Reflexion~\\citep{reflexion-2023} reduces death to $31.4\\%$ but the gap to deterministic remains $15.1$~pp; under matched-episode analysis ($N{=}3$), $\\Delta_{\\text{nd}} = -0.47$, yielding DAF${}>100\\%$. Scaling to Qwen2.5-72B ($N{=}255$) reduces death rate to $30.6\\%$ with DAF $= 92.4\\%$ (95\\% CI: $[86.1\\%, 97.9\\%]$). A second 70B model, Llama-3.1-70B ($N{=}220$), yields DAF $= 101.0\\%$ ($[95.3\\%, 107.5\\%]$): death avoidance more than fully accounts for the gap. Both 70B-class models suggest that scaling does not attenuate death dominance.\n\n\\paragraph{Dose-response analysis.}\nWe extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\\ref{fig:dose-response}). Retry is nearly flat ($48.0\\% \\to 43.5\\%$). Reflexion drops steeply to $34.0\\%$ at $N{=}3$ ($\\Delta = -13.5$~pp, $p = 0.003$) then stabilizes ($34$--$36.5\\%$ for $N \\geq 3$, pairwise $p > 0.5$); both the decline and plateau are well-powered (minimum detectable effect ${\\sim}8$~pp at 80\\% power; Appendix~\\ref{app:dose-response}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/dose_response.pdf}\n\\caption{Death rate vs.\\ trial count for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Reflexion drops steeply through $N{=}3$ then plateaus; Retry is nearly flat. Horizontal lines: 72B ($30.6\\%$) and deterministic ($16.3\\%$) baselines. Error bands: Wilson 95\\% CIs.}\n\\label{fig:dose-response}\n\\end{figure}\n\n\\subsection{Cross-Environment Boundary Probes}\n\\label{sec:math-contrast}\n\\label{sec:cross-env}\n\nWe probe two environments as boundary cases to test the framework's specificity (Figure~\\ref{fig:signal-reversal}). On MATH Level~4--5~\\citep{math-2021} ($N{=}795$), internal reasoning and code-interpreter accuracy are near-identical ($73.5\\%$ vs.\\ $73.0\\%$, $p = 0.81$): without a catastrophic failure mechanism, no routing signal emerges despite substantial task difficulty. ALFWorld~\\citep{alfworld-2021} (135 games, no death mechanism, DAF $= 0\\%$) shows 94.6\\% of non-tie labels favoring the information-advantaged strategy (which enumerates admissible actions); Llama-3.1-8B replicates at 100\\%. The framework identifies this qualitatively different mechanism, information asymmetry rather than death avoidance, without modification, indicating that DAF correctly attributes zero signal to death when none exists (full label distributions and per-task breakdowns in Appendix~\\ref{app:cross-env-details}).\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\nAlways-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points (Table~\\ref{tab:baselines}). Random routing ($-22.38$) falls between the two pure strategies, confirming that the gap is not an artifact of evaluation methodology. The oracle improves only to $-6.58$, with 96.3\\% of decisions matching always-deterministic, an \\emph{oracle degeneracy} where perfect per-episode foresight provides marginal benefit over the trivial always-deterministic baseline (Appendix~\\ref{sec:threshold-routing}).\n\n\\subsection{Router Training: Inconclusive Results}\n\\label{sec:router-diagnostic}\n\nA Qwen3 LoRA router (0.6B--4B; Appendix~\\ref{app:router-details}) trained on counterfactual labels shows flat step-level balanced accuracy ($56$--$59\\%$) across all model scales; episode-level evaluation yields $47.1 \\pm 2.2\\%$, below majority-vote.\\footnote{Consistent with noisy-label bounds~\\citep{natarajan2013learning}: ${\\sim}$88\\% of step-level labels are uninformative with 90.5\\%/3.7\\% class imbalance (Appendix~\\ref{app:seed-robustness}).} Leave-one-task-out degrades to chance ($50.0\\%$), suggesting signal is a per-task-type constant rather than a learnable function of step-level observations. Deployed end-to-end, the best router (4B) scores $-10.70$, not exceeding always-deterministic ($-9.47$); this negative result is consistent with the death-dominance finding, as death avoidance cannot be predicted from pre-episode features when it depends on multi-step trajectory dynamics. Additional ablations (capacity scaling, generative routing, reasoning depth) are in Appendix~\\ref{app:ablations}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/signal_reversal.pdf}\n\\vspace{-2mm}\n\\caption{Cross-environment label distributions. ScienceWorld and ALFWorld both favor deterministic via different mechanisms (death avoidance vs.\\ information asymmetry); MATH shows no routing signal.}\n\\label{fig:signal-reversal}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStrategy & Score & 95\\% CI & Death \\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\\\\nAlways-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\\\\nRandom & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\\\\nOracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\\\\n\\midrule\nTrained Router$^\\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). $\\dagger$\\,Single seed (42); see Appendix~\\ref{app:seed-robustness} for 8-seed robustness.}\n\\label{tab:baselines}\n\\end{table}\n",
      "numLines": 201,
      "startLine": 1,
      "totalLines": 201
    }
  }
}
```

</details>

---


### Tool call

_source line 390_

<details open><summary>🔧 Tool call — Read · `toolu_01JDtsv1CmnFDUHpXX8DgJ2P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "b78b330d-c5e6-465a-966d-948068643a5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ntzcxx1RnUtesFPMJiEccj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21185,
      "cache_read_input_tokens": 37689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21185
      },
      "output_tokens": 25,
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

_source line 391 · 2026-05-26T10:22:28.382Z_

<details><summary>↩ Tool result · `toolu_01JDtsv1CmnFDUHpXX8DgJ2P`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Signal granularity and router failure.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property, but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants (0.6B--4B) converge on near-chance balanced accuracy ($56$--$59\%$); leave-one-task-out degrades to $50.0\%$, suggesting the router captures only task-type identity rather than a learnable function of step-level observations. Scaling $10{\times}$ to 70B-class models does not attenuate this pattern (DAF $92$--$101\%$), and cross-model death-rate stability ($31$--$49\%$ across five models) confirms death vulnerability is a task-environment property, better addressed through action-space constraints (Appendix~\ref{app:grounding-ablation}) than learned routing policies.
6	
7	\paragraph{Failure mechanism.}
8	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, ScienceWorld's answer-submission command, applied to irrelevant targets (rooms, doors, inventory items). The action distribution analysis (Figure~\ref{fig:death-action-dist}, Appendix~\ref{app:failure-modes}) shows that \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while Figure~\ref{fig:death-comparison} reveals that within death episodes both strategies exhibit comparable rates (${\sim}5\%$). The higher internal death count reflects more frequent entry into catastrophic states, not different action selection within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} is the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Action-space filtering that blocks \texttt{focus on} during the exploration phase reduces death by 19~pp with zero leaks and zero passthroughs (Appendix~\ref{app:grounding-ablation}), confirming shallow behavioral origins amenable to simple interventions.
9	
10	\paragraph{Oracle degeneracy and practical implications.}
11	Always-deterministic matches 96.3\% of oracle decisions (\S\ref{sec:baselines}), capping routing's marginal value at 2.89 points---an \emph{oracle degeneracy} where $\Delta_{\text{nd}} = 2.84$ (9.6\% of total gap). This degeneracy arises because the deterministic strategy already avoids the primary failure mode, leaving only a residual non-death gap for the oracle to exploit. A ${\sim}$50-episode pilot suffices to compute the death-label fraction $f_{\text{death}}$ (the proportion of non-tie labels where exactly one strategy dies) and assess whether learned routing adds value before committing to full-scale router training. Table~\ref{tab:decision-validation} shows the three-stage procedure (Appendix~\ref{app:decision-framework}) correctly classifies all four conditions, including ALFWorld's information-asymmetry signal where DAF $= 0\%$ correctly identifies a non-death mechanism.
12	
13	\begin{table}[t]
14	\centering
15	\scriptsize
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}lrrll@{}}
18	\toprule
19	Condition & $\Delta$DR & $f_{\text{death}}$ & Prediction & Actual \\
20	\midrule
21	Qwen-7B (SW) & +26.5 & 78.9\% & det-fixed & det wins \\
22	Llama-8B (SW) & +30.0 & $>$75\% & det-fixed & det wins \\
23	Qwen-72B (SW) & +27.8 & $>$75\% & det-fixed & det wins \\
24	MATH & +0.5 & 0\% & router viable & no signal \\
25	\bottomrule
26	\end{tabular}}
27	\caption{Retrospective validation of the practitioner decision framework. SW = ScienceWorld. The three-stage diagnostic correctly classifies all four conditions (4/4).}
28	\label{tab:decision-validation}
29	\end{table}
30	
31	\paragraph{Scope and applicability conditions.}
32	The decomposition requires: (i)~binary catastrophic failures with fixed penalty, (ii)~asymmetric failure rates, and (iii)~$P \gg \Delta_\text{nd}$. ScienceWorld satisfies all three; MATH and ALFWorld lack the first. Graded penalties or symmetric failure rates would require DAF extensions. The penalty sensitivity analysis (Table~\ref{tab:penalty-sensitivity}, Appendix~\ref{app:penalty}) confirms that DAF is mechanically driven by $P$: the label fraction (78.9\%) is $P$-invariant, while the score-based DAF ranges from $7.4\%$ at $P{=}0$ to $97.9\%$ at $P{=}500$. In death-dominated settings, targeted safety interventions may outperform general-purpose routing, shifting the problem from ``which strategy to route to'' to ``how to prevent catastrophic actions.''
33	
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "4b0c813f-1d16-433b-b651-3f4a9b862f78",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Signal granularity and router failure.}\nThe router diagnostic (\\S\\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property, but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants (0.6B--4B) converge on near-chance balanced accuracy ($56$--$59\\%$); leave-one-task-out degrades to $50.0\\%$, suggesting the router captures only task-type identity rather than a learnable function of step-level observations. Scaling $10{\\times}$ to 70B-class models does not attenuate this pattern (DAF $92$--$101\\%$), and cross-model death-rate stability ($31$--$49\\%$ across five models) confirms death vulnerability is a task-environment property, better addressed through action-space constraints (Appendix~\\ref{app:grounding-ablation}) than learned routing policies.\n\n\\paragraph{Failure mechanism.}\nAll 105 internal-strategy deaths trace to misuse of \\texttt{focus on [object]}, ScienceWorld's answer-submission command, applied to irrelevant targets (rooms, doors, inventory items). The action distribution analysis (Figure~\\ref{fig:death-action-dist}, Appendix~\\ref{app:failure-modes}) shows that \\texttt{focus on} is moderately more frequent in death episodes ($5.4\\%$ vs.\\ $3.4\\%$), while Figure~\\ref{fig:death-comparison} reveals that within death episodes both strategies exhibit comparable rates (${\\sim}5\\%$). The higher internal death count reflects more frequent entry into catastrophic states, not different action selection within those states. Among fatal \\texttt{focus on} targets, \\texttt{workshop} is the most frequent (20.0\\%), followed by \\texttt{inventory} (17.1\\%) and \\texttt{kitchen} (10.5\\%), indicating a systematic object bias rather than random exploration. Action-space filtering that blocks \\texttt{focus on} during the exploration phase reduces death by 19~pp with zero leaks and zero passthroughs (Appendix~\\ref{app:grounding-ablation}), confirming shallow behavioral origins amenable to simple interventions.\n\n\\paragraph{Oracle degeneracy and practical implications.}\nAlways-deterministic matches 96.3\\% of oracle decisions (\\S\\ref{sec:baselines}), capping routing's marginal value at 2.89 points---an \\emph{oracle degeneracy} where $\\Delta_{\\text{nd}} = 2.84$ (9.6\\% of total gap). This degeneracy arises because the deterministic strategy already avoids the primary failure mode, leaving only a residual non-death gap for the oracle to exploit. A ${\\sim}$50-episode pilot suffices to compute the death-label fraction $f_{\\text{death}}$ (the proportion of non-tie labels where exactly one strategy dies) and assess whether learned routing adds value before committing to full-scale router training. Table~\\ref{tab:decision-validation} shows the three-stage procedure (Appendix~\\ref{app:decision-framework}) correctly classifies all four conditions, including ALFWorld's information-asymmetry signal where DAF $= 0\\%$ correctly identifies a non-death mechanism.\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrll@{}}\n\\toprule\nCondition & $\\Delta$DR & $f_{\\text{death}}$ & Prediction & Actual \\\\\n\\midrule\nQwen-7B (SW) & +26.5 & 78.9\\% & det-fixed & det wins \\\\\nLlama-8B (SW) & +30.0 & $>$75\\% & det-fixed & det wins \\\\\nQwen-72B (SW) & +27.8 & $>$75\\% & det-fixed & det wins \\\\\nMATH & +0.5 & 0\\% & router viable & no signal \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Retrospective validation of the practitioner decision framework. SW = ScienceWorld. The three-stage diagnostic correctly classifies all four conditions (4/4).}\n\\label{tab:decision-validation}\n\\end{table}\n\n\\paragraph{Scope and applicability conditions.}\nThe decomposition requires: (i)~binary catastrophic failures with fixed penalty, (ii)~asymmetric failure rates, and (iii)~$P \\gg \\Delta_\\text{nd}$. ScienceWorld satisfies all three; MATH and ALFWorld lack the first. Graded penalties or symmetric failure rates would require DAF extensions. The penalty sensitivity analysis (Table~\\ref{tab:penalty-sensitivity}, Appendix~\\ref{app:penalty}) confirms that DAF is mechanically driven by $P$: the label fraction (78.9\\%) is $P$-invariant, while the score-based DAF ranges from $7.4\\%$ at $P{=}0$ to $97.9\\%$ at $P{=}500$. In death-dominated settings, targeted safety interventions may outperform general-purpose routing, shifting the problem from ``which strategy to route to'' to ``how to prevent catastrophic actions.''\n\n",
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

_source line 392_

<details open><summary>🔧 Tool call — Read · `toolu_01NtH6a8mc2ECCipdHwvzuVH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "9e3edc5b-c2fb-4e00-a39a-ed138c082ba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ntzcxx1RnUtesFPMJiEccj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21185,
      "cache_read_input_tokens": 37689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21185
      },
      "output_tokens": 25,
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

_source line 393 · 2026-05-26T10:22:28.679Z_

<details><summary>↩ Tool result · `toolu_01NtH6a8mc2ECCipdHwvzuVH`</summary>

```text
1	\section{Conclusion}
2	
3	Our episode-level counterfactual framework reveals that routing signal in ScienceWorld is dominated by a single mechanism: 78.9\% of non-tie labels trace to death asymmetry, a finding stable across three model families and two 70B-class models (DAF $92$--$101\%$). When routing signal collapses to catastrophic-failure avoidance, always-deterministic approaches oracle performance, and learned step-level routing offers limited additional value.
4	
5	The framework's diagnostic value extends beyond negative results. The practitioner decision procedure (Table~\ref{tab:decision-validation}) correctly classifies four distinct conditions, and boundary probes demonstrate that the same decomposition identifies qualitatively different signal sources without modification, suggesting utility as a general pre-routing diagnostic.
6	
7	Key open directions include validating death dominance in other catastrophic-failure environments (e.g., safety-critical robotics, irreversible web actions), developing hybrid approaches that combine action-space filtering for death-prone tasks with learned routing for non-death tasks, extending DAF to graded penalties and stochastic failure severity, and investigating whether the concentration of routing signal in a single mechanism generalizes to other agent benchmarks with asymmetric failure modes. More broadly, our results suggest that diagnosing signal composition \emph{before} training a router can save substantial compute by identifying when a simple fixed strategy already captures most of the available signal.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "1bc9f81d-177f-46fb-82a4-6db153e213a4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\nOur episode-level counterfactual framework reveals that routing signal in ScienceWorld is dominated by a single mechanism: 78.9\\% of non-tie labels trace to death asymmetry, a finding stable across three model families and two 70B-class models (DAF $92$--$101\\%$). When routing signal collapses to catastrophic-failure avoidance, always-deterministic approaches oracle performance, and learned step-level routing offers limited additional value.\n\nThe framework's diagnostic value extends beyond negative results. The practitioner decision procedure (Table~\\ref{tab:decision-validation}) correctly classifies four distinct conditions, and boundary probes demonstrate that the same decomposition identifies qualitatively different signal sources without modification, suggesting utility as a general pre-routing diagnostic.\n\nKey open directions include validating death dominance in other catastrophic-failure environments (e.g., safety-critical robotics, irreversible web actions), developing hybrid approaches that combine action-space filtering for death-prone tasks with learned routing for non-death tasks, extending DAF to graded penalties and stochastic failure severity, and investigating whether the concentration of routing signal in a single mechanism generalizes to other agent benchmarks with asymmetric failure modes. More broadly, our results suggest that diagnosing signal composition \\emph{before} training a router can save substantial compute by identifying when a simple fixed strategy already captures most of the available signal.\n",
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

_source line 394_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information. Let me review the citation contexts in the tex files to check if any citations are misattributed.

Let me review each citation usage:

1. **introduction.tex**:
   - `\citep{toolformer-2023}` — "inserting API calls by perplexity reduction" — Toolformer does use perplexity to decide when to insert tool calls. ✓
   - `\citep{art-2023,chameleon-2023}` — "decomposing tasks into tool-augmented programs" — Both ART and Chameleon do task decomposition. ✓
   - `\citep{cogrouter-2026,ares-2026}` — "adaptively selecting reasoning depths" — Both papers address adaptive reasoning. ✓
   - `\citep{mtrouter-2026,budget-aware-routing-2026}` — "model tiers" — MTRouter handles multi-turn routing while Budget-Aware focuses on agentic routing. ✓
   - `\citep{scienceworld-2022}` — "ScienceWorld" — ✓

2. **related_work.tex**: Continuing to verify the remaining citations...
   - `\citep{toolformer-2023,toolace-2025}` — "self-supervised invocation" — Toolformer uses self-supervised learning and ToolACE addresses function calling. ✓
   - `\citep{art-2023,chameleon-2023}` — "task-level decomposition" — ✓
   - `\citep{retool-2025,tool-learning-survey-2024}` — "RL-based tool selection" — ReTool employs RL for tool selection; the survey provides broader context though it's a looser fit. ✓
   - `\citet{when2tool-2026}` — "accuracy-latency tradeoffs" — Need to verify whether when2tool actually examines accuracy-latency tradeoffs. The title suggests it's about LLM agents knowing when to invoke tools without explicit reasoning, which might not directly address the tradeoff angle I'm grouping it under.
   - `\citet{tool-use-tax-2026}` — "quantify invocation overhead" — "Unveiling the Tool-Use Tax" directly measures the overhead costs of tool invocation. ✓
   - `\citet{to-call-or-not-2026,tool-overuse-illusion-2026}` — "investigate overuse patterns" — Both papers examine tool overuse phenomena. ✓
   - `\citep{graves2016act}` — "learned halting" — ACT introduces adaptive computation time with learned stopping mechanisms. ✓
   - `\citep{mixture-of-recursions-2025}` — "token-level recursion" — ✓
   - `\citep{cogrouter-2026,ares-2026}` — "per-step depth adjustment" — Still checking these citations... I'm noticing some potential mismatches between the citation descriptions and what the papers actually cover. The axis-2026 paper on counterfactual simulations for multi-agent behavior might not align well with "axis-aligned perturbations," and the CSO paper about critical step optimization seems like it's being characterized as causal structure discovery, which could be off-base.

Now I'm going through a checklist of other citations to verify their descriptions are accurate — most of these look solid, like the counterfactual data augmentation work, ScienceWorld, ALFWorld, and the various agent frameworks like ReAct and Reflexion. Finishing up the causal inference citations — Rubin's potential outcomes framework and Pearl's structural causal models — then moving through the method section to verify ReAct as the reasoning baseline, confirm the Qwen2.5 model choice, and check that the ScienceWorld environment citation is properly justified alongside Ng's work on reward shaping and policy invariance.

Now checking the experiments section citations for Reflexion, the three language models (Llama-3.1, Gemma-2), the MATH and ALFWorld benchmarks, and the noisy-label bounds reference — all appear correctly placed and contextually sound.

Compiling the full audit findings, I've identified several issues: the Gajcin paper is a doctoral consortium entry missing that designation, Reflexion is missing an author, the first author name for ToolACE is incorrect, PONA is misclassified as arXiv when it's accepted to NeurIPS 2025, and SALT has an incomplete author entry. I'm noting that #22 routellm-2024 is listed as arXiv but was actually accepted at ICLR 2025, and there are a few minor formatting issues like capitalization and terminology choices that don't constitute real errors. Now I need to verify the author name for the kadavath2022 paper — the agent flagged "Eli Tran-Geesaman" as potentially incorrect, but I'm checking the actual arXiv submission to confirm whether this is the right spelling. I'm also noticing that some papers have been published at conferences since their arXiv versions — routellm and ona2025abstract have both moved from arXiv to conference venues. I'm tallying up the issues now: five hard errors that need fixing (wrong author names in toolace, automix, agent-safetybench, and salt; missing author in reflexion), a couple moderate issues worth addressing, and some minor suggestions for venue upgrades.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "679b96f4-a231-4eef-a3f7-6896282dca82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYXRzv7ryxoXqS9xfAQj5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13768,
      "cache_read_input_tokens": 58874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13768
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

_source line 395_

Now I'll compile the full audit report. Let me also verify one uncertain finding — the kadavath2022 author name.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "fda0050e-9658-4c8e-a9ce-c6e6aec98916",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYXRzv7ryxoXqS9xfAQj5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13768,
      "cache_read_input_tokens": 58874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13768
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

_source line 396_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G6kfmCj4dAcDbu63HSTrjB`</summary>

```json
{
  "query": "arxiv 2207.05221 \"Language Models Mostly Know What They Know\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "3b8179e4-ea95-4b0d-9675-73c3686f5e0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYXRzv7ryxoXqS9xfAQj5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13768,
      "cache_read_input_tokens": 58874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13768
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

_source line 397 · 2026-05-26T10:23:52.549Z_

<details><summary>↩ Tool result · `toolu_01G6kfmCj4dAcDbu63HSTrjB`</summary>

```text
Web search results for query: "arxiv 2207.05221 "Language Models Mostly Know What They Know" authors"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"Language Models (Mostly) Know What They Know","url":"https://arxiv.org/pdf/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"[2207.05221v4] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221v4"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"Language Models (Mostly) Know What They Know - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220705221K/abstract"},{"title":"[2207.05221] Language Models (Mostly) Know What They Know – Papiers","url":"https://papiers.ai/2207.05221"}]

Based on the search results, here are the authors of the arxiv paper 2207.05221 titled "Language Models (Mostly) Know What They Know":

The authors are Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez, Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli Tran-Johnson, Scott Johnston, Sheer El-Showk, Andy Jones, Nelson Elhage, Tristan Hume, Anna Chen, Yuntao Bai, Sam Bowman, Stanislav Fort, Deep Ganguli, Danny Hernandez, Josh Jacobson, Jackson Kernion, Shauna Kravec, Liane Lovitt, Kamal Ndousse, Catherine Olsson, Sam Ringer, Dario Amodei, Tom Brown, Jack Clark, Nicholas Joseph, Ben Mann, Sam McCandlish, Chris Olah, and Jared Kaplan.

The paper was submitted on July 11, 2022 (v1) and last revised on November 21, 2022 (v4).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "a3f01bf8-2dc1-4308-95ff-1fcc0234fe65",
  "tool_use_result": {
    "query": "arxiv 2207.05221 \"Language Models Mostly Know What They Know\" authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_019ESyVvgAPt9xjrat2Ld1bm",
        "content": [
          {
            "title": "[2207.05221] Language Models (Mostly) Know What They Know",
            "url": "https://arxiv.org/abs/2207.05221"
          },
          {
            "title": "Language Models (Mostly) Know What They Know",
            "url": "https://arxiv.org/pdf/2207.05221"
          },
          {
            "title": "(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations",
            "url": "https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"
          },
          {
            "title": "(PDF) Language Models (Mostly) Know What They Know",
            "url": "https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"
          },
          {
            "title": "[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"
          },
          {
            "title": "[2207.05221v4] Language Models (Mostly) Know What They Know",
            "url": "https://arxiv.org/abs/2207.05221v4"
          },
          {
            "title": "Language Models (Mostly) Know What They Know",
            "url": "https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"
          },
          {
            "title": "Language Models (Mostly) Know What They Know - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2022arXiv220705221K/abstract"
          },
          {
            "title": "[2207.05221] Language Models (Mostly) Know What They Know – Papiers",
            "url": "https://papiers.ai/2207.05221"
          }
        ]
      },
      "Based on the search results, here are the authors of the arxiv paper 2207.05221 titled \"Language Models (Mostly) Know What They Know\":\n\nThe authors are Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez, Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli Tran-Johnson, Scott Johnston, Sheer El-Showk, Andy Jones, Nelson Elhage, Tristan Hume, Anna Chen, Yuntao Bai, Sam Bowman, Stanislav Fort, Deep Ganguli, Danny Hernandez, Josh Jacobson, Jackson Kernion, Shauna Kravec, Liane Lovitt, Kamal Ndousse, Catherine Olsson, Sam Ringer, Dario Amodei, Tom Brown, Jack Clark, Nicholas Joseph, Ben Mann, Sam McCandlish, Chris Olah, and Jared Kaplan.\n\nThe paper was submitted on July 11, 2022 (v1) and last revised on November 21, 2022 (v4)."
    ],
    "durationSeconds": 14.000707830000028
  }
}
```

</details>

---


### Assistant

_source line 398_

<details><summary>Logged reasoning block</summary>

```text
Confirmed: the author is "Eli Tran-Johnson" not "Eli Tran-Geesaman" as in the bib entry.

Now let me create the output directory and write the full audit report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "99f5fe2a-33d6-4d8b-a75a-c9ebe2c4946f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4mNj6YyuWTXCSjZwGkWJP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4043,
      "cache_read_input_tokens": 72642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4043
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

_source line 399_

Confirmed: the bib has "Eli Tran-Geesaman" but the actual author is "Eli Tran-Johnson". Now I'll write the full audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "fa5f5dad-732a-4c5f-9e65-d8309b5a77e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4mNj6YyuWTXCSjZwGkWJP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4043,
      "cache_read_input_tokens": 72642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4043
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

_source line 400_

<details open><summary>🔧 Tool call — Bash · `toolu_01DU5ThcoFbhbksRkuPXTRHe`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit",
  "description": "Create ref-audit directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "ee97d716-440c-4153-95d2-5341b706d085",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4mNj6YyuWTXCSjZwGkWJP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4043,
      "cache_read_input_tokens": 72642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4043
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

_source line 401 · 2026-05-26T10:24:05.397Z_

<details><summary>↩ Tool result · `toolu_01DU5ThcoFbhbksRkuPXTRHe`</summary>

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
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "3c988c9e-00db-4deb-83a6-2627702dd5d2",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---


### Tool call

_source line 402_

<details open><summary>🔧 Tool call — Write · `toolu_01Ux48nVdLLQTWb7MPcZgL3e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_C.md",
  "content": "# Reference Audit — Worker C\n\n## 总结\n- 总条目数：68\n- ✓ 确认正确：59\n- ✗ 发现问题：9（5 项硬错误，2 项中等问题，2 项 venue 升级建议）\n\n### 硬错误（必须修正）\n\n| # | cite_key | 问题 |\n|---|----------|------|\n| 33 | toolace-2025 | 第一作者姓名错误：\"Zhang, Weiwen\" → **\"Liu, Weiwen\"** |\n| 59 | automix-2024 | 作者列表严重错误：多个名字拼错，缺少 7 位作者，包含不存在的作者 |\n| 51 | agent-safetybench-2024 | 作者列表错误：\"Junhao Yang\" → \"Junxiao Yang\"，包含 3 名非作者，缺少 \"Hongning Wang\" |\n| 46 | salt-2026 | 第三作者错误：\"David Yan\" → **\"Qiaojing Yan\"** |\n| 23 | reflexion-2023 | 缺少作者 Edward Berman |\n\n### 中等问题（建议修正）\n\n| # | cite_key | 问题 |\n|---|----------|------|\n| 64 | kadavath2022language | 作者 \"Eli Tran-Geesaman\" → **\"Eli Tran-Johnson\"** |\n| 20 | gajcin2023counterfactual | 实为 AAMAS 2023 Doctoral Consortium 论文，非正式论文；标题省略了 \": Doctoral Consortium\" 后缀 |\n\n### Venue 升级建议（arXiv → 已被会议接收）\n\n| # | cite_key | 当前 venue | 实际已接收 |\n|---|----------|-----------|-----------|\n| 22 | routellm-2024 | arXiv 2406.18665 | **ICLR 2025** |\n| 43 | pona2025abstract | arXiv 2506.02946 | **NeurIPS 2025** |\n\n---\n\n## 逐条核对\n\n### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (EMNLP 2022)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICLR 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓ (大小写差异属 BibTeX 正常行为)\n- Venue：✓ (arXiv:2303.09014)\n- ID：✓\n- 正文引用上下文：✓\n\n### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 6. [retool-2025] — ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2504.11536)\n- ID：✓\n- 正文引用上下文：✓\n\n### 7. [cogrouter-2026] — Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.12662)\n- ID：✓\n- 正文引用上下文：✓\n\n### 8. [ares-2026] — Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2603.07915)\n- ID：✓\n- 正文引用上下文：✓\n\n### 9. [mixture-of-recursions-2025] — Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (NeurIPS 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 10. [mtrouter-2026] — MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (ACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2604.19749)\n- ID：✓\n- 正文引用上下文：✓\n\n### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.09252)\n- ID：✓\n- 正文引用上下文：✓\n\n### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00136)\n- ID：✓\n- 正文引用上下文：✓\n\n### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00737)\n- ID：✓\n- 正文引用上下文：✓\n\n### 15. [dagger-2011] — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2011)\n- 标题：✓\n- Venue：✓ (AISTATS 2011)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 17. [alfworld-2021] — ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 18. [garcia2015comprehensive] — A Comprehensive Survey on Safe Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (JMLR vol 16(1), pp 1437-1480)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (AAAI 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✗ 实际标题为 \"Counterfactual Explanations for Reinforcement Learning Agents: Doctoral Consortium\"，bib 省略了后缀\n- Venue：✗ 实为 AAMAS 2023 Doctoral Consortium 论文，非正式会议论文\n- ID：N/A\n- 正文引用上下文：✓\n\n### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (Artificial Intelligence, vol 295, pp 103455)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✗ bib 标注为 arXiv 2406.18665，但已被 **ICLR 2025** 接收，建议更新\n- ID：✓ (2406.18665)\n- 正文引用上下文：✓\n\n### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning\n- 真实性：✓\n- 作者：✗ 缺少作者 **Edward Berman**。完整作者应为 Shinn, Cassano, **Berman**, Gopinath, Narasimhan, Yao\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2405.17935)\n- ID：✓\n- 正文引用上下文：✓\n\n### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 27. [lats-2024] — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 29. [qwen25-2024] — Qwen2.5 Technical Report\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.15115)\n- ID：✓\n- 正文引用上下文：✓\n\n### 30. [llama3-2024] — The Llama 3 Herd of Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2407.21783)\n- ID：✓\n- 正文引用上下文：✓\n\n### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2008)\n- 标题：✓\n- Venue：✓ (The Review of Economics and Statistics, vol 90(3), pp 414-427)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 32. [achiam2017cpo] — Constrained Policy Optimization\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2017)\n- 标题：✓\n- Venue：✓ (ICML 2017)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling\n- 真实性：✓\n- 作者：✗ 第一作者姓名错误。bib 写 **\"Zhang, Weiwen\"**，实际第一作者为 **\"Liu, Weiwen\"** (Weiwen Liu)。完整作者列表包含 Weiwen Liu, Xu Huang, Xingshan Zeng 等 27 人\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (ICLR 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (Canadian Journal of Economics, vol 56(3), pp 839-858)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2012)\n- 标题：✓\n- Venue：✓ (ICML 2012)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 36. [graves2016act] — Adaptive Computation Time for Recurrent Neural Networks\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2016)\n- 标题：✓\n- Venue：✓ (arXiv:1603.08983)\n- ID：✓\n- 正文引用上下文：✓\n\n### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓ (bib 用 \"LLMs\" 缩写，原文用 \"Large Language Models\"，可接受)\n- Venue：✓ (Findings of ACL 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 39. [altman1999constrained] — Constrained Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (Chapman & Hall/CRC)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2002)\n- 标题：✓\n- Venue：✓ (Machine Learning, vol 49(2-3), pp 267-290)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 41. [natarajan2013learning] — Learning with Noisy Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2013)\n- 标题：✓\n- Venue：✓ (NeurIPS 2013)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.21227)\n- ID：✓\n- 正文引用上下文：✓\n\n### 43. [pona2025abstract] — Abstract Counterfactuals for Language Model Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✗ bib 标注为 arXiv 2506.02946，但已被 **NeurIPS 2025** 接收，建议更新\n- ID：✓ (2506.02946)\n- 正文引用上下文：✓\n\n### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.03412)\n- ID：✓\n- 正文引用上下文：✓\n\n### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2505.17801)\n- ID：✓\n- 正文引用上下文：✓\n\n### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\n- 真实性：✓\n- 作者：✗ 第三作者错误。bib 写 **\"Yan, David\"**，ACL Anthology 实际为 **\"Qiaojing Yan\"**\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (Findings of EACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size\n- 真实性：✓\n- 作者：✓ (Gemma Team)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2408.00118)\n- ID：✓\n- 正文引用上下文：✓\n\n### 48. [northcutt2021confident] — Confident Learning: Estimating Uncertainty in Dataset Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (JAIR, vol 70, pp 1373-1411)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 50. [ng1999policy] — Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (ICML 1999)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents\n- 真实性：✓\n- 作者：✗ 作者列表严重错误。bib 列出 9 人，实际为 7 人。具体问题：(1) \"Junhao Yang\" 应为 **\"Junxiao Yang\"**；(2) \"Jie Liu\"、\"Renhao Wang\"、\"Jiangjie Li\" 三人并非该论文作者；(3) 缺少作者 **\"Hongning Wang\"**。正确作者列表：Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.14470)\n- ID：✓\n- 正文引用上下文：✓\n\n### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2009)\n- 标题：✓\n- Venue：✓ (Cambridge University Press, 2nd ed.)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 53. [rubin1974estimating] — Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1974)\n- 标题：✓\n- Venue：✓ (Journal of Educational Psychology, vol 66(5), pp 688-701)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (JMLR, vol 23(120), pp 1-39)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2018)\n- 标题：✓\n- Venue：✓ (AAAI 2018)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 57. [kaushik2020learning] — Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 58. [frugalgpt-2023] — FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (arXiv:2305.05176)\n- ID：✓\n- 正文引用上下文：✓\n\n### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models\n- 真实性：✓\n- 作者：✗ 作者列表严重错误。bib 列出 6 人中 3 个名字有误且遗漏 7 位作者：(1) \"Anand, Prakhar\" 应为 **\"Anand, Ankit\"**；(2) \"Potdar, Srividya\" 应为 **\"Potharaju, Srividya Pranavi\"**；(3) \"Gupta, Swaroop\" 应为 **\"Mishra, Swaroop\"**；(4) \"Tandon, Niket\" 并非该论文作者；(5) 缺少 Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam 等作者。正确完整列表：Pranjal Aggarwal, Aman Madaan, Ankit Anand, Srividya Pranavi Potharaju, Swaroop Mishra, Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (NeurIPS 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 61. [leviathan2023speculative] — Fast Inference from Transformers via Speculative Decoding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICML 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2510.16492)\n- ID：✓\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (EMNLP 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know\n- 真实性：✓\n- 作者：✗ 第 10 位作者姓名错误。bib 写 **\"Eli Tran-Geesaman\"**，实际为 **\"Eli Tran-Johnson\"**（已通过 arXiv 2207.05221 原始页面确认）\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (arXiv:2207.05221)\n- ID：✓\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 65. [xin2020deebert] — DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ACL 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 66. [zhou2020bert] — BERT Loses Patience: Fast and Robust Inference with Early Exit\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (NeurIPS 2020)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (NeurIPS 2015)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (AAAI 2015)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n---\n\n## 正文引用上下文检查\n\n逐篇 tex 文件检查 `\\cite{}` 用法是否存在\"引用 paper A 但描述 paper B 结论\"的情况：\n\n- **introduction.tex**：所有引用与描述匹配。✓\n- **related_work.tex**：所有引用与描述匹配。✓\n- **method.tex**：所有引用与描述匹配。✓\n- **experiments.tex**：所有引用与描述匹配。✓\n- **discussion.tex**：无引用。✓\n- **conclusion.tex**：无引用。✓\n\n未发现引用上下文错配。\n\n## 附加发现\n\n1. bib 中有 12 条 entry 未在正文 tex 中被 `\\cite` 引用：dagger-2011, toolkengpt-2023, altman1999constrained, mihatsch2002risk, northcutt2021confident, li2020dividemix, moldovan2012safe, leviathan2023speculative, bonagiri2025check, manakul2023selfcheckgpt, kadavath2022language, zhou2020bert, chow2015risk, tamar2015optimizing。这些可能在 appendix 中使用，或为冗余条目。\n2. cite key `axis-2026` 对应的 bib entry year 为 2025（arXiv:2505.17801），key 与年份不一致（不影响编译，但不规范）。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "1b52fc23-a34a-4b35-958b-74661a4f4466",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pwGAUq6sSt1oLfWdMCWNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 339,
      "cache_read_input_tokens": 76685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 339
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

_source line 403 · 2026-05-26T10:26:22.849Z_

<details><summary>↩ Tool result · `toolu_01Ux48nVdLLQTWb7MPcZgL3e`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_C.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "ebdc0312-d0d7-4c18-9009-7afe6c7cfed5",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_C.md",
    "content": "# Reference Audit — Worker C\n\n## 总结\n- 总条目数：68\n- ✓ 确认正确：59\n- ✗ 发现问题：9（5 项硬错误，2 项中等问题，2 项 venue 升级建议）\n\n### 硬错误（必须修正）\n\n| # | cite_key | 问题 |\n|---|----------|------|\n| 33 | toolace-2025 | 第一作者姓名错误：\"Zhang, Weiwen\" → **\"Liu, Weiwen\"** |\n| 59 | automix-2024 | 作者列表严重错误：多个名字拼错，缺少 7 位作者，包含不存在的作者 |\n| 51 | agent-safetybench-2024 | 作者列表错误：\"Junhao Yang\" → \"Junxiao Yang\"，包含 3 名非作者，缺少 \"Hongning Wang\" |\n| 46 | salt-2026 | 第三作者错误：\"David Yan\" → **\"Qiaojing Yan\"** |\n| 23 | reflexion-2023 | 缺少作者 Edward Berman |\n\n### 中等问题（建议修正）\n\n| # | cite_key | 问题 |\n|---|----------|------|\n| 64 | kadavath2022language | 作者 \"Eli Tran-Geesaman\" → **\"Eli Tran-Johnson\"** |\n| 20 | gajcin2023counterfactual | 实为 AAMAS 2023 Doctoral Consortium 论文，非正式论文；标题省略了 \": Doctoral Consortium\" 后缀 |\n\n### Venue 升级建议（arXiv → 已被会议接收）\n\n| # | cite_key | 当前 venue | 实际已接收 |\n|---|----------|-----------|-----------|\n| 22 | routellm-2024 | arXiv 2406.18665 | **ICLR 2025** |\n| 43 | pona2025abstract | arXiv 2506.02946 | **NeurIPS 2025** |\n\n---\n\n## 逐条核对\n\n### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (EMNLP 2022)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICLR 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓ (大小写差异属 BibTeX 正常行为)\n- Venue：✓ (arXiv:2303.09014)\n- ID：✓\n- 正文引用上下文：✓\n\n### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 6. [retool-2025] — ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2504.11536)\n- ID：✓\n- 正文引用上下文：✓\n\n### 7. [cogrouter-2026] — Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.12662)\n- ID：✓\n- 正文引用上下文：✓\n\n### 8. [ares-2026] — Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2603.07915)\n- ID：✓\n- 正文引用上下文：✓\n\n### 9. [mixture-of-recursions-2025] — Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (NeurIPS 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 10. [mtrouter-2026] — MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (ACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2604.19749)\n- ID：✓\n- 正文引用上下文：✓\n\n### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.09252)\n- ID：✓\n- 正文引用上下文：✓\n\n### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00136)\n- ID：✓\n- 正文引用上下文：✓\n\n### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00737)\n- ID：✓\n- 正文引用上下文：✓\n\n### 15. [dagger-2011] — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2011)\n- 标题：✓\n- Venue：✓ (AISTATS 2011)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 17. [alfworld-2021] — ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 18. [garcia2015comprehensive] — A Comprehensive Survey on Safe Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (JMLR vol 16(1), pp 1437-1480)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (AAAI 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✗ 实际标题为 \"Counterfactual Explanations for Reinforcement Learning Agents: Doctoral Consortium\"，bib 省略了后缀\n- Venue：✗ 实为 AAMAS 2023 Doctoral Consortium 论文，非正式会议论文\n- ID：N/A\n- 正文引用上下文：✓\n\n### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (Artificial Intelligence, vol 295, pp 103455)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✗ bib 标注为 arXiv 2406.18665，但已被 **ICLR 2025** 接收，建议更新\n- ID：✓ (2406.18665)\n- 正文引用上下文：✓\n\n### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning\n- 真实性：✓\n- 作者：✗ 缺少作者 **Edward Berman**。完整作者应为 Shinn, Cassano, **Berman**, Gopinath, Narasimhan, Yao\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2405.17935)\n- ID：✓\n- 正文引用上下文：✓\n\n### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 27. [lats-2024] — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 29. [qwen25-2024] — Qwen2.5 Technical Report\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.15115)\n- ID：✓\n- 正文引用上下文：✓\n\n### 30. [llama3-2024] — The Llama 3 Herd of Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2407.21783)\n- ID：✓\n- 正文引用上下文：✓\n\n### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2008)\n- 标题：✓\n- Venue：✓ (The Review of Economics and Statistics, vol 90(3), pp 414-427)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 32. [achiam2017cpo] — Constrained Policy Optimization\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2017)\n- 标题：✓\n- Venue：✓ (ICML 2017)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling\n- 真实性：✓\n- 作者：✗ 第一作者姓名错误。bib 写 **\"Zhang, Weiwen\"**，实际第一作者为 **\"Liu, Weiwen\"** (Weiwen Liu)。完整作者列表包含 Weiwen Liu, Xu Huang, Xingshan Zeng 等 27 人\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (ICLR 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (Canadian Journal of Economics, vol 56(3), pp 839-858)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2012)\n- 标题：✓\n- Venue：✓ (ICML 2012)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 36. [graves2016act] — Adaptive Computation Time for Recurrent Neural Networks\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2016)\n- 标题：✓\n- Venue：✓ (arXiv:1603.08983)\n- ID：✓\n- 正文引用上下文：✓\n\n### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓ (bib 用 \"LLMs\" 缩写，原文用 \"Large Language Models\"，可接受)\n- Venue：✓ (Findings of ACL 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 39. [altman1999constrained] — Constrained Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (Chapman & Hall/CRC)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2002)\n- 标题：✓\n- Venue：✓ (Machine Learning, vol 49(2-3), pp 267-290)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 41. [natarajan2013learning] — Learning with Noisy Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2013)\n- 标题：✓\n- Venue：✓ (NeurIPS 2013)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.21227)\n- ID：✓\n- 正文引用上下文：✓\n\n### 43. [pona2025abstract] — Abstract Counterfactuals for Language Model Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✗ bib 标注为 arXiv 2506.02946，但已被 **NeurIPS 2025** 接收，建议更新\n- ID：✓ (2506.02946)\n- 正文引用上下文：✓\n\n### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.03412)\n- ID：✓\n- 正文引用上下文：✓\n\n### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2505.17801)\n- ID：✓\n- 正文引用上下文：✓\n\n### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\n- 真实性：✓\n- 作者：✗ 第三作者错误。bib 写 **\"Yan, David\"**，ACL Anthology 实际为 **\"Qiaojing Yan\"**\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (Findings of EACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size\n- 真实性：✓\n- 作者：✓ (Gemma Team)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2408.00118)\n- ID：✓\n- 正文引用上下文：✓\n\n### 48. [northcutt2021confident] — Confident Learning: Estimating Uncertainty in Dataset Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (JAIR, vol 70, pp 1373-1411)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 50. [ng1999policy] — Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (ICML 1999)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents\n- 真实性：✓\n- 作者：✗ 作者列表严重错误。bib 列出 9 人，实际为 7 人。具体问题：(1) \"Junhao Yang\" 应为 **\"Junxiao Yang\"**；(2) \"Jie Liu\"、\"Renhao Wang\"、\"Jiangjie Li\" 三人并非该论文作者；(3) 缺少作者 **\"Hongning Wang\"**。正确作者列表：Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.14470)\n- ID：✓\n- 正文引用上下文：✓\n\n### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2009)\n- 标题：✓\n- Venue：✓ (Cambridge University Press, 2nd ed.)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 53. [rubin1974estimating] — Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1974)\n- 标题：✓\n- Venue：✓ (Journal of Educational Psychology, vol 66(5), pp 688-701)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (JMLR, vol 23(120), pp 1-39)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2018)\n- 标题：✓\n- Venue：✓ (AAAI 2018)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 57. [kaushik2020learning] — Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 58. [frugalgpt-2023] — FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (arXiv:2305.05176)\n- ID：✓\n- 正文引用上下文：✓\n\n### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models\n- 真实性：✓\n- 作者：✗ 作者列表严重错误。bib 列出 6 人中 3 个名字有误且遗漏 7 位作者：(1) \"Anand, Prakhar\" 应为 **\"Anand, Ankit\"**；(2) \"Potdar, Srividya\" 应为 **\"Potharaju, Srividya Pranavi\"**；(3) \"Gupta, Swaroop\" 应为 **\"Mishra, Swaroop\"**；(4) \"Tandon, Niket\" 并非该论文作者；(5) 缺少 Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam 等作者。正确完整列表：Pranjal Aggarwal, Aman Madaan, Ankit Anand, Srividya Pranavi Potharaju, Swaroop Mishra, Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (NeurIPS 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 61. [leviathan2023speculative] — Fast Inference from Transformers via Speculative Decoding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICML 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2510.16492)\n- ID：✓\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (EMNLP 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know\n- 真实性：✓\n- 作者：✗ 第 10 位作者姓名错误。bib 写 **\"Eli Tran-Geesaman\"**，实际为 **\"Eli Tran-Johnson\"**（已通过 arXiv 2207.05221 原始页面确认）\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (arXiv:2207.05221)\n- ID：✓\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 65. [xin2020deebert] — DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ACL 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 66. [zhou2020bert] — BERT Loses Patience: Fast and Robust Inference with Early Exit\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (NeurIPS 2020)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (NeurIPS 2015)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (AAAI 2015)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n---\n\n## 正文引用上下文检查\n\n逐篇 tex 文件检查 `\\cite{}` 用法是否存在\"引用 paper A 但描述 paper B 结论\"的情况：\n\n- **introduction.tex**：所有引用与描述匹配。✓\n- **related_work.tex**：所有引用与描述匹配。✓\n- **method.tex**：所有引用与描述匹配。✓\n- **experiments.tex**：所有引用与描述匹配。✓\n- **discussion.tex**：无引用。✓\n- **conclusion.tex**：无引用。✓\n\n未发现引用上下文错配。\n\n## 附加发现\n\n1. bib 中有 12 条 entry 未在正文 tex 中被 `\\cite` 引用：dagger-2011, toolkengpt-2023, altman1999constrained, mihatsch2002risk, northcutt2021confident, li2020dividemix, moldovan2012safe, leviathan2023speculative, bonagiri2025check, manakul2023selfcheckgpt, kadavath2022language, zhou2020bert, chow2015risk, tamar2015optimizing。这些可能在 appendix 中使用，或为冗余条目。\n2. cite key `axis-2026` 对应的 bib entry year 为 2025（arXiv:2505.17801），key 与年份不一致（不影响编译，但不规范）。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Assistant

_source line 404_

审核完成。报告已写入 `artifacts/ref-audit/audit_worker_C.md`。

68 条 bib entry 中发现 9 条有问题：

**硬错误（5）：**
- `toolace-2025`：第一作者 "Zhang, Weiwen" → **Liu, Weiwen**
- `automix-2024`：作者列表严重错误（3 个名字拼错 + 缺少 7 位作者 + 含 1 位非作者）
- `agent-safetybench-2024`：作者列表错误（"Junhao Yang" → "Junxiao Yang"，含 3 名非作者，缺 "Hongning Wang"）
- `salt-2026`：第三作者 "David Yan" → **Qiaojing Yan**
- `reflexion-2023`：缺少作者 Edward Berman

**中等问题（2）：**
- `kadavath2022language`：作者 "Eli Tran-Geesaman" → **Eli Tran-Johnson**
- `gajcin2023counterfactual`：实为 AAMAS 2023 Doctoral Consortium 论文，非正式论文

**Venue 升级建议（2）：**
- `routellm-2024`：arXiv → 已被 ICLR 2025 接收
- `pona2025abstract`：arXiv → 已被 NeurIPS 2025 接收

无 hallucinated paper，无引用上下文错配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "uuid": "979fbff3-6895-47a4-acab-4a44f42c7df2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFEWHEuJEMFiDTDCnfdGsA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9701,
      "cache_read_input_tokens": 77024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9701
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

_source line 405_

审核完成。报告已写入 `artifacts/ref-audit/audit_worker_C.md`。

68 条 bib entry 中发现 9 条有问题：

**硬错误（5）：**
- `toolace-2025`：第一作者 "Zhang, Weiwen" → **Liu, Weiwen**
- `automix-2024`：作者列表严重错误（3 个名字拼错 + 缺少 7 位作者 + 含 1 位非作者）
- `agent-safetybench-2024`：作者列表错误（"Junhao Yang" → "Junxiao Yang"，含 3 名非作者，缺 "Hongning Wang"）
- `salt-2026`：第三作者 "David Yan" → **Qiaojing Yan**
- `reflexion-2023`：缺少作者 Edward Berman

**中等问题（2）：**
- `kadavath2022language`：作者 "Eli Tran-Geesaman" → **Eli Tran-Johnson**
- `gajcin2023counterfactual`：实为 AAMAS 2023 Doctoral Consortium 论文，非正式论文

**Venue 升级建议（2）：**
- `routellm-2024`：arXiv → 已被 ICLR 2025 接收
- `pona2025abstract`：arXiv → 已被 NeurIPS 2025 接收

无 hallucinated paper，无引用上下文错配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 654187,
  "duration_api_ms": 1807003,
  "num_turns": 20,
  "stop_reason": "end_turn",
  "session_id": "3f558b97-fe40-4fc8-b778-9b466beda5a7",
  "total_cost_usd": 5.728557750000001,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 74884,
    "cache_read_input_tokens": 395396,
    "output_tokens": 24490,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 74884,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 422,
        "cache_read_input_tokens": 77024,
        "cache_creation_input_tokens": 9701,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 9701
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1124171,
      "outputTokens": 37780,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 104,
      "costUSD": 2.353071,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8965,
      "outputTokens": 44387,
      "cacheReadInputTokens": 1636111,
      "cacheCreationInputTokens": 224469,
      "webSearchRequests": 0,
      "costUSD": 3.37548675,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2798a1d3-1cf9-4811-a4af-9fe79b1992b2"
}
```

</details>

---
