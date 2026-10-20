# paper fix experiments

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_fix-experiments_20260515T010600.log`
- **Structured JSON:** [`c1fc602d9221fb2438ac.json`](../../sessions/c1/c1fc602d9221fb2438ac.json)

## Before a recorded user message

25 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe",
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
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
  "uuid": "3054e931-d2eb-4553-aee7-49cc75493edc",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-agent-progress-probe/memory/"
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
    "resetsAt": 1778814000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "32e0beff-3e64-45cf-b012-9ddcdd6bed9d",
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current experiments.tex file to understand the existing content and structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "1c9e5a44-3127-4192-a23f-1bd8b44d28f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQYAF6Mxcp4ptQ7d22iwfY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12682,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12682
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

<details open><summary>🔧 Tool call — Read · `toolu_01Pi8jVS2xyQcXHFWUKK5PjX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "666000e7-2e24-4dc9-a7ea-a8d73c4120b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQYAF6Mxcp4ptQ7d22iwfY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12682,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12682
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

_source line 6 · 2026-05-15T01:06:12.691Z_

<details><summary>↩ Tool result · `toolu_01Pi8jVS2xyQcXHFWUKK5PjX`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.
5	All reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\S\ref{sec:method}).
6	
7	\paragraph{Circular evaluation caveat.}
8	Structural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.
9	Consequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.
10	The cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\S\ref{sec:cmd_rep_ablation}).
11	A human-annotated gold set provides the definitive non-circular evaluation (\S\ref{sec:gold_set}).
12	
13	%-------------------------------------------------------------------
14	\subsection{Experimental Setup}
15	\label{sec:setup}
16	
17	\paragraph{Datasets.}
18	We extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.
19	\textbf{SWE-Agent} trajectories from SWE-bench \citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\%.
20	\textbf{OpenHands} (OH) trajectories \citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\%.
21	Silver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).
22	Unless stated otherwise, evaluation uses the conf${\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\begin{tabular}{llrrc}
28	\toprule
29	\textbf{Agent} & \textbf{Source} & \textbf{Windows} & \textbf{Stag\,\%} & \textbf{Conf${\geq}$2} \\
30	\midrule
31	SWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\
32	OpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\
33	\bottomrule
34	\end{tabular}
35	\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}
36	\label{tab:dataset_stats}
37	\end{table}
38	
39	\paragraph{Detection methods.}
40	(1)~\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).
41	(2)~\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \citep{cho2014gru} with attention \citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.
42	(3)~\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.
43	(4)~\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\$11.66 API cost for the SWE test set).
44	(5)~\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.
45	
46	\paragraph{Metrics.}
47	Macro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\textsubscript{stag}) and progress (F1\textsubscript{prog}).
48	
49	%-------------------------------------------------------------------
50	\subsection{Main Results}
51	\label{sec:main_results}
52	
53	Table~\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\geq}$2 test set and cross-agent transfer to OpenHands.
54	
55	\begin{table*}[t]
56	\centering
57	\small
58	\begin{tabular}{l ccc cc}
59	\toprule
60	& \multicolumn{3}{c}{\textbf{SWE-Agent In-Domain} (conf${\geq}$2)} & \multicolumn{2}{c}{\textbf{OpenHands Transfer}} \\
61	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
62	\textbf{Method} & Macro-F1 & F1\textsubscript{stag} & F1\textsubscript{prog} & All & Conf${\geq}$2 \\
63	\midrule
64	Structural RF$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \textbf{0.9959} \\
65	Structural GB$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & \textbf{0.9674} & \underline{0.9919} \\
66	Structural LR$^\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\
67	ProgressProbe (GRU)           & \underline{0.9055} & 0.8593 & 0.9518 & 0.530 & 0.528 \\
68	\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\
69	Mean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\
70	LLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\
71	Cosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\
72	\bottomrule
73	\end{tabular}
74	\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \textbf{bold}, second-best \underline{underlined}.}
75	\label{tab:main_results}
76	\end{table*}
77	
78	In-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\,pp.
79	However, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.
80	The more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.
81	The LLM judge underperforms all learned methods despite substantially higher cost.
82	
83	%-------------------------------------------------------------------
84	\subsection{Cross-Agent Transfer}
85	\label{sec:cross_agent}
86	
87	Table~\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.
88	Structural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\,pp above the probe fine-tuned on 100\% of OH data (0.751).
89	RF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.
90	Both structural models recover to $>$0.99 on conf${\geq}$2 OH windows, where label noise is lower.
91	
92	The probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\geq}$2) is near chance, and even full OH fine-tuning only reaches 0.751.
93	This asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.
94	
95	\paragraph{Multi-seed stability.}
96	Structural RF: $0.9951{\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\pm}0.0015$.
97	The probe shows higher variance: $0.9185{\pm}0.0113$, though all seeds exceed 0.90.
98	
99	%-------------------------------------------------------------------
100	\subsection{Robustness Analysis}
101	\label{sec:robustness}
102	
103	\paragraph{Encoder ablation.}
104	Replacing Qwen3-0.6B with BGE-M3 \citep{chen2024bgem3} or E5-large-v2 \citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\ 0.9055 for Qwen3).
105	All encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\ref{tab:encoder_ablation}.
106	
107	\paragraph{Window size.}
108	$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\,pp and $k{=}7$ drops 1.8\,pp.
109	Shorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.
110	The 0.9309 figure differs from the main table's 0.9055 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.
111	Details in Appendix Table~\ref{tab:window_ablation}.
112	
113	\paragraph{Data scaling.}
114	Figure~\ref{fig:data_scaling} compares data efficiency across methods.
115	Structural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\% training data, fully saturating by 50\%.
116	The probe scales monotonically from 0.805 (10\%) to 0.906 (100\%) but has not plateaued---a 10.1\,pp drop that is roughly 20$\times$ the structural degradation (${\sim}$0.4--0.8\,pp).
117	This data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.
118	
119	\begin{figure}[t]
120	\centering
121	\includegraphics[width=\columnwidth]{../../figures/paper/fig_data_scaling.pdf}
122	\caption{Macro-F1 vs.\ training data fraction. Structural classifiers (RF, GB) saturate by 50\% data; the probe scales monotonically but remains 9\,pp below at 100\%.}
123	\label{fig:data_scaling}
124	\end{figure}
125	
126	%-------------------------------------------------------------------
127	\subsection{Labeling Function Temporal Dynamics}
128	\label{sec:lf_temporal}
129	
130	We analyze when each LF first fires relative to the onset of stagnation episodes (Table~\ref{tab:lf_temporal}, Figure~\ref{fig:lf_temporal}).
131	
132	\begin{table}[t]
133	\centering
134	\small
135	\begin{tabular}{lrrrr}
136	\toprule
137	\textbf{LF} & \textbf{Lag} & \textbf{Lead\,\%} & \textbf{Conc.\,\%} & \textbf{Lag\,\%} \\
138	\midrule
139	cmd\_rep      & $-1.87$ & 36.1 & --- & --- \\
140	file\_diff    & $-1.20$ & 17.1 & --- & --- \\
141	outcome\_bp   & $+6.70$ & ---  & --- & 48.4 \\
142	\bottomrule
143	\end{tabular}
144	\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}
145	\label{tab:lf_temporal}
146	\end{table}
147	
148	The three LFs occupy distinct temporal niches.
149	Command repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.
150	File diff is near-concurrent ($-1.20$ steps).
151	Outcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.
152	
153	All pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\_rep vs.\ file\_diff $p{=}1.44{\times}10^{-26}$, cmd\_rep vs.\ outcome\_bp $p{=}6.67{\times}10^{-39}$, file\_diff vs.\ outcome\_bp $p{=}3.47{\times}10^{-47}$).
154	
155	\paragraph{Cross-agent reversal.}
156	On OpenHands, cmd\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).
157	This reversal explains the cmd\_rep pathology analyzed in \S\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\_rep on progress windows, inverting its diagnostic value.
158	
159	\begin{figure}[t]
160	\centering
161	\includegraphics[width=\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}
162	\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\_rep leads ($-1.87$ steps), file\_diff is near-concurrent ($-1.20$), outcome\_bp lags ($+6.70$). Inset: OH reversal where cmd\_rep becomes lagging.}
163	\label{fig:lf_temporal}
164	\end{figure}
165	
166	%-------------------------------------------------------------------
167	\subsection{Command Repetition Ablation}
168	\label{sec:cmd_rep_ablation}
169	
170	The cmd\_rep LF votes stagnation on 92.2\% of OH windows (vs.\ 65.5\% on SWE-Agent), with a 71\% false positive rate on OH progress windows.
171	Table~\ref{tab:cmd_rep_ablation} shows the effect of removing it.
172	
173	\begin{table}[t]
174	\centering
175	\small
176	\begin{tabular}{lcccc}
177	\toprule
178	\textbf{LF Config} & \textbf{ZS F1} & \textbf{FT F1} & \textbf{FT F1\textsubscript{s}} & \textbf{FT F1\textsubscript{p}} \\
179	\midrule
180	3-LF (w/ cmd\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\
181	2-LF (no cmd\_rep) & 0.607 & \textbf{0.927} & 0.938 & 0.917 \\
182	\midrule
183	$\Delta$ & +7.7\,pp & +17.6\,pp & +39.4\,pp & $-4.2$\,pp \\
184	\bottomrule
185	\end{tabular}
186	\caption{Effect of removing cmd\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\% OH data. F1\textsubscript{s}/F1\textsubscript{p} = stagnation/progress F1.}
187	\label{tab:cmd_rep_ablation}
188	\end{table}
189	
190	Removing cmd\_rep improves zero-shot transfer by 7.7\,pp and fine-tuned performance by 17.6\,pp.
191	The gain is driven almost entirely by stagnation recall (+39.4\,pp F1\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\,pp F1\textsubscript{prog}).
192	The 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.
193	Note that removing cmd\_rep also reduces training data from 101,713 to 72,554 windows (28.5\% reduction); however, the model trained on \emph{less} data with cleaner labels decisively outperforms the model trained on \emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.
194	This motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.
195	Appendix Table~\ref{tab:cross_agent_cmdrep} extends this analysis to structural zero-shot transfer, where removing cmd\_rep has the opposite effect ($-4.2$\,pp), revealing that the fix requires learned adaptation rather than simple LF deletion.
196	
197	%-------------------------------------------------------------------
198	\subsection{Temporal Label Models}
199	\label{sec:temporal_label_models}
200	
201	We investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).
202	Table~\ref{tab:temporal_models} compares three temporal label models \citep{ratner2017snorkel,safranchik2020linkedhmm}.
203	
204	\begin{table}[t]
205	\centering
206	\small
207	\begin{tabular}{lccc}
208	\toprule
209	\textbf{Method} & \textbf{Conf${\geq}$2 F1} & \textbf{MV Agr.} & \textbf{Probe F1$^\ddagger$} \\
210	\midrule
211	MV (baseline) & 0.8946$^\ast$ & 1.000 & 0.8468 \\
212	TWV ($\sigma{=}2$) & \textbf{0.9003} & 0.885 & 0.8211 \\
213	Lag-HMM & 0.8936 & 0.820 & --- \\
214	HMM & 0.7502 & 0.685 & 0.6564 \\
215	\bottomrule
216	\end{tabular}
217	\caption{Temporal label model comparison. $^\ast$MV conf${\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\ddagger$Downstream: probe trained on each method's labels, evaluated on the full SWE-Agent test set ($N{=}8{,}101$) against MV labels.}
218	\label{tab:temporal_models}
219	\end{table}
220	
221	TWV achieves the highest conf${\geq}$2 F1 (0.9003, +0.57\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\ 0.8468 for MV-trained ($-2.57$\,pp).
222	TWV flips 14.1\% of conf$=$1 labels, introducing noise that hurts probe training.
223	HMM overpredicts stagnation (29,176 stagnation vs.\ 25,633 progress windows), degrading downstream performance to 0.6564.
224	Lag-HMM closely tracks MV ($-0.1$\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \emph{aggregation}.
225	
226	\paragraph{TWV sensitivity.}
227	The Gaussian kernel bandwidth $\sigma$ is critical: $\sigma{=}2$ is optimal (0.9003); $\sigma{=}1$ drops to 0.8105 and $\sigma{=}5$ drops to 0.808.
228	This narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.
229	
230	These results constitute a negative finding: despite clear temporal structure in LF firing patterns (\S\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.
231	
232	%-------------------------------------------------------------------
233	\subsection{Gold Set Validation}
234	\label{sec:gold_set}
235	\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "d2f8723b-c114-4e94-8c15-c2e48bbd316c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.530 & 0.528 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe LLM judge underperforms all learned methods despite substantially higher cost.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\\geq}$2) is near chance, and even full OH fine-tuning only reaches 0.751.\nThis asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.9951{\\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$.\nThe probe shows higher variance: $0.9185{\\pm}0.0113$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\\ 0.9055 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nThe 0.9309 figure differs from the main table's 0.9055 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} compares data efficiency across methods.\nStructural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\\% training data, fully saturating by 50\\%.\nThe probe scales monotonically from 0.805 (10\\%) to 0.906 (100\\%) but has not plateaued---a 10.1\\,pp drop that is roughly 20$\\times$ the structural degradation (${\\sim}$0.4--0.8\\,pp).\nThis data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Macro-F1 vs.\\ training data fraction. Structural classifiers (RF, GB) saturate by 50\\% data; the probe scales monotonically but remains 9\\,pp below at 100\\%.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nThis reversal explains the cmd\\_rep pathology analyzed in \\S\\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\\_rep on progress windows, inverting its diagnostic value.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nNote that removing cmd\\_rep also reduces training data from 101,713 to 72,554 windows (28.5\\% reduction); however, the model trained on \\emph{less} data with cleaner labels decisively outperforms the model trained on \\emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\nAppendix Table~\\ref{tab:cross_agent_cmdrep} extends this analysis to structural zero-shot transfer, where removing cmd\\_rep has the opposite effect ($-4.2$\\,pp), revealing that the fix requires learned adaptation rather than simple LF deletion.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares three temporal label models \\citep{ratner2017snorkel,safranchik2020linkedhmm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{MV Agr.} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 0.8946$^\\ast$ & 1.000 & 0.8468 \\\\\nTWV ($\\sigma{=}2$) & \\textbf{0.9003} & 0.885 & 0.8211 \\\\\nLag-HMM & 0.8936 & 0.820 & --- \\\\\nHMM & 0.7502 & 0.685 & 0.6564 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal label model comparison. $^\\ast$MV conf${\\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\\ddagger$Downstream: probe trained on each method's labels, evaluated on the full SWE-Agent test set ($N{=}8{,}101$) against MV labels.}\n\\label{tab:temporal_models}\n\\end{table}\n\nTWV achieves the highest conf${\\geq}$2 F1 (0.9003, +0.57\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\\ 0.8468 for MV-trained ($-2.57$\\,pp).\nTWV flips 14.1\\% of conf$=$1 labels, introducing noise that hurts probe training.\nHMM overpredicts stagnation (29,176 stagnation vs.\\ 25,633 progress windows), degrading downstream performance to 0.6564.\nLag-HMM closely tracks MV ($-0.1$\\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \\emph{aggregation}.\n\n\\paragraph{TWV sensitivity.}\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal (0.9003); $\\sigma{=}1$ drops to 0.8105 and $\\sigma{=}5$ drops to 0.808.\nThis narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.\n\nThese results constitute a negative finding: despite clear temporal structure in LF firing patterns (\\S\\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\n\\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}",
      "numLines": 235,
      "startLine": 1,
      "totalLines": 235
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full file. Let me carefully go through the modification checklist and make all the changes. Let me plan the edits:

1. **Line 20**: OH stag ratio "6.6%" → "21.45%"
2. **Line 32 (Table)**: OH Stag% "6.6" → "21.4"
3. **Line 67**: ProgressProbe OH Transfer "0.530" → "0.598", "0.528" → "0.598"
4. **Line 68**: "+ full OH fine-tune" "0.7510" → "0.9763"


5. **Lines 87-93 (§5.3)**: Update cross-agent transfer narrative
6. **Lines 167-195 (§5.5)**: Complete rewrite

Let me make these edits systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "6aaf6c39-21c0-4458-b8eb-458dd4d94ba7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HThn6Ey7bdiBkfApEz7mtB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5932,
      "cache_read_input_tokens": 24523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5932
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

_source line 8_

Now I'll make all the edits. Starting with the simpler numerical fixes, then the narrative rewrites.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "e731682a-eee4-430e-a114-1e99804e0898",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HThn6Ey7bdiBkfApEz7mtB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5932,
      "cache_read_input_tokens": 24523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5932
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01BjzAiLLC2BjMQcZALSDUat`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
  "old_string": "\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\\%.",
  "new_string": "\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 21.4\\%."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "9a4da6ee-321e-4f1f-b521-049b922b04fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HThn6Ey7bdiBkfApEz7mtB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5932,
      "cache_read_input_tokens": 24523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5932
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

_source line 10 · 2026-05-15T01:06:25.217Z_

<details><summary>↩ Tool result · `toolu_01BjzAiLLC2BjMQcZALSDUat`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "2f50a195-9f5b-41e2-bb28-4b2dcc130976",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
    "oldString": "\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\\%.",
    "newString": "\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 21.4\\%.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.530 & 0.528 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe LLM judge underperforms all learned methods despite substantially higher cost.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\\geq}$2) is near chance, and even full OH fine-tuning only reaches 0.751.\nThis asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.9951{\\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$.\nThe probe shows higher variance: $0.9185{\\pm}0.0113$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\\ 0.9055 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nThe 0.9309 figure differs from the main table's 0.9055 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} compares data efficiency across methods.\nStructural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\\% training data, fully saturating by 50\\%.\nThe probe scales monotonically from 0.805 (10\\%) to 0.906 (100\\%) but has not plateaued---a 10.1\\,pp drop that is roughly 20$\\times$ the structural degradation (${\\sim}$0.4--0.8\\,pp).\nThis data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Macro-F1 vs.\\ training data fraction. Structural classifiers (RF, GB) saturate by 50\\% data; the probe scales monotonically but remains 9\\,pp below at 100\\%.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nThis reversal explains the cmd\\_rep pathology analyzed in \\S\\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\\_rep on progress windows, inverting its diagnostic value.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nNote that removing cmd\\_rep also reduces training data from 101,713 to 72,554 windows (28.5\\% reduction); however, the model trained on \\emph{less} data with cleaner labels decisively outperforms the model trained on \\emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\nAppendix Table~\\ref{tab:cross_agent_cmdrep} extends this analysis to structural zero-shot transfer, where removing cmd\\_rep has the opposite effect ($-4.2$\\,pp), revealing that the fix requires learned adaptation rather than simple LF deletion.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares three temporal label models \\citep{ratner2017snorkel,safranchik2020linkedhmm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{MV Agr.} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 0.8946$^\\ast$ & 1.000 & 0.8468 \\\\\nTWV ($\\sigma{=}2$) & \\textbf{0.9003} & 0.885 & 0.8211 \\\\\nLag-HMM & 0.8936 & 0.820 & --- \\\\\nHMM & 0.7502 & 0.685 & 0.6564 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal label model comparison. $^\\ast$MV conf${\\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\\ddagger$Downstream: probe trained on each method's labels, evaluated on the full SWE-Agent test set ($N{=}8{,}101$) against MV labels.}\n\\label{tab:temporal_models}\n\\end{table}\n\nTWV achieves the highest conf${\\geq}$2 F1 (0.9003, +0.57\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\\ 0.8468 for MV-trained ($-2.57$\\,pp).\nTWV flips 14.1\\% of conf$=$1 labels, introducing noise that hurts probe training.\nHMM overpredicts stagnation (29,176 stagnation vs.\\ 25,633 progress windows), degrading downstream performance to 0.6564.\nLag-HMM closely tracks MV ($-0.1$\\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \\emph{aggregation}.\n\n\\paragraph{TWV sensitivity.}\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal (0.9003); $\\sigma{=}1$ drops to 0.8105 and $\\sigma{=}5$ drops to 0.808.\nThis narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.\n\nThese results constitute a negative finding: despite clear temporal structure in LF firing patterns (\\S\\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\n\\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}",
    "structuredPatch": [
      {
        "oldStart": 17,
        "oldLines": 7,
        "newStart": 17,
        "newLines": 7,
        "lines": [
          " \\paragraph{Datasets.}",
          " We extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.",
          " \\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.",
          "-\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\\%.",
          "+\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 21.4\\%.",
          " Silver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).",
          " Unless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.",
          " "
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_0182Z4qL5RfigTTEUKby9rfc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
  "old_string": "OpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\\\",
  "new_string": "OpenHands & CodeAct   & 150,652 & 21.4 & 43,376 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "d30d95ac-1d13-4798-8b72-b54567c56d21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMJtwWHCKVjwnT3KhqxCwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 30455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
      },
      "output_tokens": 67,
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

_source line 12 · 2026-05-15T01:06:29.467Z_

<details><summary>↩ Tool result · `toolu_0182Z4qL5RfigTTEUKby9rfc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "e6182ccc-f106-489d-a4ab-7aecac4801e0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
    "oldString": "OpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\\\",
    "newString": "OpenHands & CodeAct   & 150,652 & 21.4 & 43,376 \\\\",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 21.4\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.530 & 0.528 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe LLM judge underperforms all learned methods despite substantially higher cost.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\\geq}$2) is near chance, and even full OH fine-tuning only reaches 0.751.\nThis asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.9951{\\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$.\nThe probe shows higher variance: $0.9185{\\pm}0.0113$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\\ 0.9055 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nThe 0.9309 figure differs from the main table's 0.9055 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} compares data efficiency across methods.\nStructural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\\% training data, fully saturating by 50\\%.\nThe probe scales monotonically from 0.805 (10\\%) to 0.906 (100\\%) but has not plateaued---a 10.1\\,pp drop that is roughly 20$\\times$ the structural degradation (${\\sim}$0.4--0.8\\,pp).\nThis data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Macro-F1 vs.\\ training data fraction. Structural classifiers (RF, GB) saturate by 50\\% data; the probe scales monotonically but remains 9\\,pp below at 100\\%.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nThis reversal explains the cmd\\_rep pathology analyzed in \\S\\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\\_rep on progress windows, inverting its diagnostic value.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nNote that removing cmd\\_rep also reduces training data from 101,713 to 72,554 windows (28.5\\% reduction); however, the model trained on \\emph{less} data with cleaner labels decisively outperforms the model trained on \\emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\nAppendix Table~\\ref{tab:cross_agent_cmdrep} extends this analysis to structural zero-shot transfer, where removing cmd\\_rep has the opposite effect ($-4.2$\\,pp), revealing that the fix requires learned adaptation rather than simple LF deletion.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares three temporal label models \\citep{ratner2017snorkel,safranchik2020linkedhmm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{MV Agr.} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 0.8946$^\\ast$ & 1.000 & 0.8468 \\\\\nTWV ($\\sigma{=}2$) & \\textbf{0.9003} & 0.885 & 0.8211 \\\\\nLag-HMM & 0.8936 & 0.820 & --- \\\\\nHMM & 0.7502 & 0.685 & 0.6564 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal label model comparison. $^\\ast$MV conf${\\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\\ddagger$Downstream: probe trained on each method's labels, evaluated on the full SWE-Agent test set ($N{=}8{,}101$) against MV labels.}\n\\label{tab:temporal_models}\n\\end{table}\n\nTWV achieves the highest conf${\\geq}$2 F1 (0.9003, +0.57\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\\ 0.8468 for MV-trained ($-2.57$\\,pp).\nTWV flips 14.1\\% of conf$=$1 labels, introducing noise that hurts probe training.\nHMM overpredicts stagnation (29,176 stagnation vs.\\ 25,633 progress windows), degrading downstream performance to 0.6564.\nLag-HMM closely tracks MV ($-0.1$\\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \\emph{aggregation}.\n\n\\paragraph{TWV sensitivity.}\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal (0.9003); $\\sigma{=}1$ drops to 0.8105 and $\\sigma{=}5$ drops to 0.808.\nThis narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.\n\nThese results constitute a negative finding: despite clear temporal structure in LF firing patterns (\\S\\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\n\\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}",
    "structuredPatch": [
      {
        "oldStart": 29,
        "oldLines": 7,
        "newStart": 29,
        "newLines": 7,
        "lines": [
          " \\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\",
          " \\midrule",
          " SWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\",
          "-OpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\\\",
          "+OpenHands & CodeAct   & 150,652 & 21.4 & 43,376 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}"
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01HjnHDVLMmgiKFCNguBnbyq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
  "old_string": "ProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.530 & 0.528 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\\\",
  "new_string": "ProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.598 & 0.598 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.9763 & --- \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "5c91fe12-f6a2-484b-a14b-df704eb808de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYkaETVCHGGC3QpKV88Rng",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 30977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 251
      },
      "output_tokens": 72,
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

_source line 14 · 2026-05-15T01:06:37.933Z_

<details><summary>↩ Tool result · `toolu_01HjnHDVLMmgiKFCNguBnbyq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "1ae7e3e1-6ad0-4da2-b1c3-bb4d630af9f2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
    "oldString": "ProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.530 & 0.528 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\\\",
    "newString": "ProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.598 & 0.598 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.9763 & --- \\\\",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 21.4\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 21.4 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.530 & 0.528 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe LLM judge underperforms all learned methods despite substantially higher cost.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\\geq}$2) is near chance, and even full OH fine-tuning only reaches 0.751.\nThis asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.9951{\\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$.\nThe probe shows higher variance: $0.9185{\\pm}0.0113$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\\ 0.9055 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nThe 0.9309 figure differs from the main table's 0.9055 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} compares data efficiency across methods.\nStructural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\\% training data, fully saturating by 50\\%.\nThe probe scales monotonically from 0.805 (10\\%) to 0.906 (100\\%) but has not plateaued---a 10.1\\,pp drop that is roughly 20$\\times$ the structural degradation (${\\sim}$0.4--0.8\\,pp).\nThis data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Macro-F1 vs.\\ training data fraction. Structural classifiers (RF, GB) saturate by 50\\% data; the probe scales monotonically but remains 9\\,pp below at 100\\%.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nThis reversal explains the cmd\\_rep pathology analyzed in \\S\\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\\_rep on progress windows, inverting its diagnostic value.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nNote that removing cmd\\_rep also reduces training data from 101,713 to 72,554 windows (28.5\\% reduction); however, the model trained on \\emph{less} data with cleaner labels decisively outperforms the model trained on \\emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\nAppendix Table~\\ref{tab:cross_agent_cmdrep} extends this analysis to structural zero-shot transfer, where removing cmd\\_rep has the opposite effect ($-4.2$\\,pp), revealing that the fix requires learned adaptation rather than simple LF deletion.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares three temporal label models \\citep{ratner2017snorkel,safranchik2020linkedhmm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{MV Agr.} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 0.8946$^\\ast$ & 1.000 & 0.8468 \\\\\nTWV ($\\sigma{=}2$) & \\textbf{0.9003} & 0.885 & 0.8211 \\\\\nLag-HMM & 0.8936 & 0.820 & --- \\\\\nHMM & 0.7502 & 0.685 & 0.6564 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal label model comparison. $^\\ast$MV conf${\\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\\ddagger$Downstream: probe trained on each method's labels, evaluated on the full SWE-Agent test set ($N{=}8{,}101$) against MV labels.}\n\\label{tab:temporal_models}\n\\end{table}\n\nTWV achieves the highest conf${\\geq}$2 F1 (0.9003, +0.57\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\\ 0.8468 for MV-trained ($-2.57$\\,pp).\nTWV flips 14.1\\% of conf$=$1 labels, introducing noise that hurts probe training.\nHMM overpredicts stagnation (29,176 stagnation vs.\\ 25,633 progress windows), degrading downstream performance to 0.6564.\nLag-HMM closely tracks MV ($-0.1$\\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \\emph{aggregation}.\n\n\\paragraph{TWV sensitivity.}\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal (0.9003); $\\sigma{=}1$ drops to 0.8105 and $\\sigma{=}5$ drops to 0.808.\nThis narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.\n\nThese results constitute a negative finding: despite clear temporal structure in LF firing patterns (\\S\\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\n\\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}",
    "structuredPatch": [
      {
        "oldStart": 64,
        "oldLines": 8,
        "newStart": 64,
        "newLines": 8,
        "lines": [
          " Structural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\",
          " Structural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\",
          " Structural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\",
          "-ProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.530 & 0.528 \\\\",
          "-\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\\\",
          "+ProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.598 & 0.598 \\\\",
          "+\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.9763 & --- \\\\",
          " Mean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\",
          " LLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\",
          " Cosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\"
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

Now the §5.3 Cross-Agent Transfer narrative rewrite.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "ced77974-b53a-4a62-8776-a3fa0242d2f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWwW2FkufHYRndLS9SrEsk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 31228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 351
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

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01L2ivEMyZWfohBaRQPeRYde`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
  "old_string": "Table~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\\geq}$2) is near chance, and even full OH fine-tuning only reaches 0.751.\nThis asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.",
  "new_string": "Table~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows.\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.598 on all windows) lags structural GB by 36.9\\,pp, but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.9763, within 2.2\\,pp of structural GB (0.967) on the same test set (\\S\\ref{sec:cmd_rep_ablation}).\nThe asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\\,pp gap); with target-domain labels, the probe converges to near-structural performance.\nThe practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "6c3a092c-3972-4946-ba1b-d2d44cb5dd83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWwW2FkufHYRndLS9SrEsk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 31228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 351
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

_source line 17 · 2026-05-15T01:06:55.621Z_

<details><summary>↩ Tool result · `toolu_01L2ivEMyZWfohBaRQPeRYde`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "1165fafc-925d-4c3b-a1ff-ab6c69f3c4df",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
    "oldString": "Table~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\\geq}$2) is near chance, and even full OH fine-tuning only reaches 0.751.\nThis asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.",
    "newString": "Table~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows.\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.598 on all windows) lags structural GB by 36.9\\,pp, but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.9763, within 2.2\\,pp of structural GB (0.967) on the same test set (\\S\\ref{sec:cmd_rep_ablation}).\nThe asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\\,pp gap); with target-domain labels, the probe converges to near-structural performance.\nThe practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 21.4\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 21.4 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.598 & 0.598 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.9763 & --- \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe LLM judge underperforms all learned methods despite substantially higher cost.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\\geq}$2) is near chance, and even full OH fine-tuning only reaches 0.751.\nThis asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.9951{\\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$.\nThe probe shows higher variance: $0.9185{\\pm}0.0113$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\\ 0.9055 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nThe 0.9309 figure differs from the main table's 0.9055 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} compares data efficiency across methods.\nStructural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\\% training data, fully saturating by 50\\%.\nThe probe scales monotonically from 0.805 (10\\%) to 0.906 (100\\%) but has not plateaued---a 10.1\\,pp drop that is roughly 20$\\times$ the structural degradation (${\\sim}$0.4--0.8\\,pp).\nThis data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Macro-F1 vs.\\ training data fraction. Structural classifiers (RF, GB) saturate by 50\\% data; the probe scales monotonically but remains 9\\,pp below at 100\\%.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nThis reversal explains the cmd\\_rep pathology analyzed in \\S\\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\\_rep on progress windows, inverting its diagnostic value.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nNote that removing cmd\\_rep also reduces training data from 101,713 to 72,554 windows (28.5\\% reduction); however, the model trained on \\emph{less} data with cleaner labels decisively outperforms the model trained on \\emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\nAppendix Table~\\ref{tab:cross_agent_cmdrep} extends this analysis to structural zero-shot transfer, where removing cmd\\_rep has the opposite effect ($-4.2$\\,pp), revealing that the fix requires learned adaptation rather than simple LF deletion.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares three temporal label models \\citep{ratner2017snorkel,safranchik2020linkedhmm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{MV Agr.} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 0.8946$^\\ast$ & 1.000 & 0.8468 \\\\\nTWV ($\\sigma{=}2$) & \\textbf{0.9003} & 0.885 & 0.8211 \\\\\nLag-HMM & 0.8936 & 0.820 & --- \\\\\nHMM & 0.7502 & 0.685 & 0.6564 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal label model comparison. $^\\ast$MV conf${\\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\\ddagger$Downstream: probe trained on each method's labels, evaluated on the full SWE-Agent test set ($N{=}8{,}101$) against MV labels.}\n\\label{tab:temporal_models}\n\\end{table}\n\nTWV achieves the highest conf${\\geq}$2 F1 (0.9003, +0.57\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\\ 0.8468 for MV-trained ($-2.57$\\,pp).\nTWV flips 14.1\\% of conf$=$1 labels, introducing noise that hurts probe training.\nHMM overpredicts stagnation (29,176 stagnation vs.\\ 25,633 progress windows), degrading downstream performance to 0.6564.\nLag-HMM closely tracks MV ($-0.1$\\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \\emph{aggregation}.\n\n\\paragraph{TWV sensitivity.}\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal (0.9003); $\\sigma{=}1$ drops to 0.8105 and $\\sigma{=}5$ drops to 0.808.\nThis narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.\n\nThese results constitute a negative finding: despite clear temporal structure in LF firing patterns (\\S\\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\n\\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}",
    "structuredPatch": [
      {
        "oldStart": 85,
        "oldLines": 12,
        "newStart": 85,
        "newLines": 13,
        "lines": [
          " \\label{sec:cross_agent}",
          " ",
          " Table~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.",
          "-Structural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).",
          "+Structural GB transfers best, achieving 0.967 macro-F1 on all OH windows.",
          " RF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.",
          " Both structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.",
          " ",
          "-The probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\\geq}$2) is near chance, and even full OH fine-tuning only reaches 0.751.",
          "-This asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.",
          "+The probe's zero-shot transfer (0.598 on all windows) lags structural GB by 36.9\\,pp, but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.9763, within 2.2\\,pp of structural GB (0.967) on the same test set (\\S\\ref{sec:cmd_rep_ablation}).",
          "+The asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\\,pp gap); with target-domain labels, the probe converges to near-structural performance.",
          "+The practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.",
          " ",
          " \\paragraph{Multi-seed stability.}",
          " Structural RF: $0.9951{\\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$."
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

_source line 18_

Now the complete rewrite of §5.5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "c085896d-a514-4771-a842-55fc6db9aef6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146rD5torW2yBuV6QDHz2PZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 763,
      "cache_read_input_tokens": 31579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 763
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01KfsX5Qoksdgv5FYBTzt3oZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
  "old_string": "\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nNote that removing cmd\\_rep also reduces training data from 101,713 to 72,554 windows (28.5\\% reduction); however, the model trained on \\emph{less} data with cleaner labels decisively outperforms the model trained on \\emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\nAppendix Table~\\ref{tab:cross_agent_cmdrep} extends this analysis to structural zero-shot transfer, where removing cmd\\_rep has the opposite effect ($-4.2$\\,pp), revealing that the fix requires learned adaptation rather than simple LF deletion.",
  "new_string": "\\subsection{Label Quality and cmd\\_rep Coverage}\n\\label{sec:cmd_rep_ablation}\n\nA label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.\nAfter correction, the OH stagnation rate shifted from 6.56\\% to 21.45\\%, with 21,898 window labels flipping.\nThis section quantifies how label quality and cmd\\_rep coverage jointly affect probe transfer.\n\n\\paragraph{Label correction impact on probe transfer.}\nWith corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.9763 (previously 0.751 under corrupted labels).\nThe improvement is most dramatic at low data fractions: 5\\% fine-tuning now reaches 0.850, exceeding the old 50\\% result (0.688) by 16.2\\,pp.\nLabel quality, not model capacity, was the transfer bottleneck.\n\n\\paragraph{Prevalence-matched ablation.}\nTo isolate cmd\\_rep's contribution, we compare 3-LF and 2-LF (no cmd\\_rep) models on the same test set with matched class prevalence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & \\textbf{0.9763} & 0.960 & 0.993 \\\\\n2-LF (no cmd\\_rep) & 0.6822 & 0.481 & 0.884 \\\\\n\\midrule\n$\\Delta$ & $-29.4$\\,pp & $-47.9$\\,pp & $-10.9$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\\%). Removing cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$).}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\\,pp F1\\textsubscript{stag}).\n\n\\paragraph{Coverage, not label quality, explains the gap.}\nThe 29.4\\,pp drop is not caused by cmd\\_rep improving label accuracy.\nAfter correction, cmd\\_rep fires on only 5.39\\% of OH windows (down from the previously reported 92.2\\% under corrupted embeddings) with 97.91\\% precision---a high-precision, low-recall signal.\nOn the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\\% of labels: cmd\\_rep does not change any label where the other two LFs already vote.\nIts contribution is purely \\emph{coverage}: including cmd\\_rep expands the training set from ${\\sim}$4K to ${\\sim}$43K windows (a ${\\sim}$10$\\times$ increase).\nThe 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.\n\n\\paragraph{Implications for weak supervision.}\nThese results reframe how labeling functions contribute to weak supervision pipelines.\nA high-precision, low-recall LF like cmd\\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.\nIn prevalence-matched evaluation, this data reduction manifests as a 29.4\\,pp F1 drop.\nThe core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "57fd6add-3378-4536-a36e-9b39960c3760",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146rD5torW2yBuV6QDHz2PZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 763,
      "cache_read_input_tokens": 31579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 763
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

_source line 20 · 2026-05-15T01:07:37.508Z_

<details><summary>↩ Tool result · `toolu_01KfsX5Qoksdgv5FYBTzt3oZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "605ffde4-9dda-4f81-b901-7f34ef19ff73",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
    "oldString": "\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nNote that removing cmd\\_rep also reduces training data from 101,713 to 72,554 windows (28.5\\% reduction); however, the model trained on \\emph{less} data with cleaner labels decisively outperforms the model trained on \\emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\nAppendix Table~\\ref{tab:cross_agent_cmdrep} extends this analysis to structural zero-shot transfer, where removing cmd\\_rep has the opposite effect ($-4.2$\\,pp), revealing that the fix requires learned adaptation rather than simple LF deletion.",
    "newString": "\\subsection{Label Quality and cmd\\_rep Coverage}\n\\label{sec:cmd_rep_ablation}\n\nA label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.\nAfter correction, the OH stagnation rate shifted from 6.56\\% to 21.45\\%, with 21,898 window labels flipping.\nThis section quantifies how label quality and cmd\\_rep coverage jointly affect probe transfer.\n\n\\paragraph{Label correction impact on probe transfer.}\nWith corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.9763 (previously 0.751 under corrupted labels).\nThe improvement is most dramatic at low data fractions: 5\\% fine-tuning now reaches 0.850, exceeding the old 50\\% result (0.688) by 16.2\\,pp.\nLabel quality, not model capacity, was the transfer bottleneck.\n\n\\paragraph{Prevalence-matched ablation.}\nTo isolate cmd\\_rep's contribution, we compare 3-LF and 2-LF (no cmd\\_rep) models on the same test set with matched class prevalence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & \\textbf{0.9763} & 0.960 & 0.993 \\\\\n2-LF (no cmd\\_rep) & 0.6822 & 0.481 & 0.884 \\\\\n\\midrule\n$\\Delta$ & $-29.4$\\,pp & $-47.9$\\,pp & $-10.9$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\\%). Removing cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$).}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\\,pp F1\\textsubscript{stag}).\n\n\\paragraph{Coverage, not label quality, explains the gap.}\nThe 29.4\\,pp drop is not caused by cmd\\_rep improving label accuracy.\nAfter correction, cmd\\_rep fires on only 5.39\\% of OH windows (down from the previously reported 92.2\\% under corrupted embeddings) with 97.91\\% precision---a high-precision, low-recall signal.\nOn the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\\% of labels: cmd\\_rep does not change any label where the other two LFs already vote.\nIts contribution is purely \\emph{coverage}: including cmd\\_rep expands the training set from ${\\sim}$4K to ${\\sim}$43K windows (a ${\\sim}$10$\\times$ increase).\nThe 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.\n\n\\paragraph{Implications for weak supervision.}\nThese results reframe how labeling functions contribute to weak supervision pipelines.\nA high-precision, low-recall LF like cmd\\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.\nIn prevalence-matched evaluation, this data reduction manifests as a 29.4\\,pp F1 drop.\nThe core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 21.4\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 21.4 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.598 & 0.598 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.9763 & --- \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe LLM judge underperforms all learned methods despite substantially higher cost.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows.\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.598 on all windows) lags structural GB by 36.9\\,pp, but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.9763, within 2.2\\,pp of structural GB (0.967) on the same test set (\\S\\ref{sec:cmd_rep_ablation}).\nThe asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\\,pp gap); with target-domain labels, the probe converges to near-structural performance.\nThe practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.9951{\\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$.\nThe probe shows higher variance: $0.9185{\\pm}0.0113$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\\ 0.9055 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nThe 0.9309 figure differs from the main table's 0.9055 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} compares data efficiency across methods.\nStructural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\\% training data, fully saturating by 50\\%.\nThe probe scales monotonically from 0.805 (10\\%) to 0.906 (100\\%) but has not plateaued---a 10.1\\,pp drop that is roughly 20$\\times$ the structural degradation (${\\sim}$0.4--0.8\\,pp).\nThis data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Macro-F1 vs.\\ training data fraction. Structural classifiers (RF, GB) saturate by 50\\% data; the probe scales monotonically but remains 9\\,pp below at 100\\%.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nThis reversal explains the cmd\\_rep pathology analyzed in \\S\\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\\_rep on progress windows, inverting its diagnostic value.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nNote that removing cmd\\_rep also reduces training data from 101,713 to 72,554 windows (28.5\\% reduction); however, the model trained on \\emph{less} data with cleaner labels decisively outperforms the model trained on \\emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\nAppendix Table~\\ref{tab:cross_agent_cmdrep} extends this analysis to structural zero-shot transfer, where removing cmd\\_rep has the opposite effect ($-4.2$\\,pp), revealing that the fix requires learned adaptation rather than simple LF deletion.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares three temporal label models \\citep{ratner2017snorkel,safranchik2020linkedhmm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{MV Agr.} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 0.8946$^\\ast$ & 1.000 & 0.8468 \\\\\nTWV ($\\sigma{=}2$) & \\textbf{0.9003} & 0.885 & 0.8211 \\\\\nLag-HMM & 0.8936 & 0.820 & --- \\\\\nHMM & 0.7502 & 0.685 & 0.6564 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal label model comparison. $^\\ast$MV conf${\\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\\ddagger$Downstream: probe trained on each method's labels, evaluated on the full SWE-Agent test set ($N{=}8{,}101$) against MV labels.}\n\\label{tab:temporal_models}\n\\end{table}\n\nTWV achieves the highest conf${\\geq}$2 F1 (0.9003, +0.57\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\\ 0.8468 for MV-trained ($-2.57$\\,pp).\nTWV flips 14.1\\% of conf$=$1 labels, introducing noise that hurts probe training.\nHMM overpredicts stagnation (29,176 stagnation vs.\\ 25,633 progress windows), degrading downstream performance to 0.6564.\nLag-HMM closely tracks MV ($-0.1$\\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \\emph{aggregation}.\n\n\\paragraph{TWV sensitivity.}\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal (0.9003); $\\sigma{=}1$ drops to 0.8105 and $\\sigma{=}5$ drops to 0.808.\nThis narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.\n\nThese results constitute a negative finding: despite clear temporal structure in LF firing patterns (\\S\\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\n\\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}",
    "structuredPatch": [
      {
        "oldStart": 165,
        "oldLines": 36,
        "newStart": 165,
        "newLines": 53,
        "lines": [
          " \\end{figure}",
          " ",
          " %-------------------------------------------------------------------",
          "-\\subsection{Command Repetition Ablation}",
          "+\\subsection{Label Quality and cmd\\_rep Coverage}",
          " \\label{sec:cmd_rep_ablation}",
          " ",
          "-The cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.",
          "-Table~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.",
          "+A label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.",
          "+After correction, the OH stagnation rate shifted from 6.56\\% to 21.45\\%, with 21,898 window labels flipping.",
          "+This section quantifies how label quality and cmd\\_rep coverage jointly affect probe transfer.",
          " ",
          "+\\paragraph{Label correction impact on probe transfer.}",
          "+With corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.9763 (previously 0.751 under corrupted labels).",
          "+The improvement is most dramatic at low data fractions: 5\\% fine-tuning now reaches 0.850, exceeding the old 50\\% result (0.688) by 16.2\\,pp.",
          "+Label quality, not model capacity, was the transfer bottleneck.",
          "+",
          "+\\paragraph{Prevalence-matched ablation.}",
          "+To isolate cmd\\_rep's contribution, we compare 3-LF and 2-LF (no cmd\\_rep) models on the same test set with matched class prevalence.",
          "+",
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\begin{tabular}{lcccc}",
          "+\\begin{tabular}{lccc}",
          " \\toprule",
          "-\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\",
          "+\\textbf{LF Config} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} \\\\",
          " \\midrule",
          "-3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\",
          "-2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\",
          "+3-LF (w/ cmd\\_rep) & \\textbf{0.9763} & 0.960 & 0.993 \\\\",
          "+2-LF (no cmd\\_rep) & 0.6822 & 0.481 & 0.884 \\\\",
          " \\midrule",
          "-$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\",
          "+$\\Delta$ & $-29.4$\\,pp & $-47.9$\\,pp & $-10.9$\\,pp \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}",
          "+\\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\\%). Removing cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$).}",
          " \\label{tab:cmd_rep_ablation}",
          " \\end{table}",
          " ",
          "-Removing cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.",
          "-The gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).",
          "-The 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.",
          "-Note that removing cmd\\_rep also reduces training data from 101,713 to 72,554 windows (28.5\\% reduction); however, the model trained on \\emph{less} data with cleaner labels decisively outperforms the model trained on \\emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.",
          "-This motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.",
          "-Appendix Table~\\ref{tab:cross_agent_cmdrep} extends this analysis to structural zero-shot transfer, where removing cmd\\_rep has the opposite effect ($-4.2$\\,pp), revealing that the fix requires learned adaptation rather than simple LF deletion.",
          "+Removing cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\\,pp F1\\textsubscript{stag}).",
          " ",
          "+\\paragraph{Coverage, not label quality, explains the gap.}",
          "+The 29.4\\,pp drop is not caused by cmd\\_rep improving label accuracy.",
          "+After correction, cmd\\_rep fires on only 5.39\\% of OH windows (down from the previously reported 92.2\\% under corrupted embeddings) with 97.91\\% precision---a high-precision, low-recall signal.",
          "+On the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\\% of labels: cmd\\_rep does not change any label where the other two LFs already vote.",
          "+Its contribution is purely \\emph{coverage}: including cmd\\_rep expands the training set from ${\\sim}$4K to ${\\sim}$43K windows (a ${\\sim}$10$\\times$ increase).",
          "+The 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.",
          "+",
          "+\\paragraph{Implications for weak supervision.}",
          "+These results reframe how labeling functions contribute to weak supervision pipelines.",
          "+A high-precision, low-recall LF like cmd\\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.",
          "+In prevalence-matched evaluation, this data reduction manifests as a 29.4\\,pp F1 drop.",
          "+The core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors.",
          "+",
          " %-------------------------------------------------------------------",
          " \\subsection{Temporal Label Models}",
          " \\label{sec:temporal_label_models}"
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

_source line 21_

Now let me verify the full file to confirm all changes are correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "0323f583-395f-4585-a2d9-6a812052b4bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVETfj9Kq1n3TQUqhQYA8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2108,
      "cache_read_input_tokens": 32342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2108
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01S1tQJjorNQVXxqJW93iFU7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "745f8cbe-13b2-4550-a9ca-9fa3ad6c82be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVETfj9Kq1n3TQUqhQYA8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2108,
      "cache_read_input_tokens": 32342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2108
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

_source line 23 · 2026-05-15T01:07:40.786Z_

<details><summary>↩ Tool result · `toolu_01S1tQJjorNQVXxqJW93iFU7`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.
5	All reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\S\ref{sec:method}).
6	
7	\paragraph{Circular evaluation caveat.}
8	Structural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.
9	Consequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.
10	The cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\S\ref{sec:cmd_rep_ablation}).
11	A human-annotated gold set provides the definitive non-circular evaluation (\S\ref{sec:gold_set}).
12	
13	%-------------------------------------------------------------------
14	\subsection{Experimental Setup}
15	\label{sec:setup}
16	
17	\paragraph{Datasets.}
18	We extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.
19	\textbf{SWE-Agent} trajectories from SWE-bench \citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\%.
20	\textbf{OpenHands} (OH) trajectories \citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 21.4\%.
21	Silver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).
22	Unless stated otherwise, evaluation uses the conf${\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\begin{tabular}{llrrc}
28	\toprule
29	\textbf{Agent} & \textbf{Source} & \textbf{Windows} & \textbf{Stag\,\%} & \textbf{Conf${\geq}$2} \\
30	\midrule
31	SWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\
32	OpenHands & CodeAct   & 150,652 & 21.4 & 43,376 \\
33	\bottomrule
34	\end{tabular}
35	\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}
36	\label{tab:dataset_stats}
37	\end{table}
38	
39	\paragraph{Detection methods.}
40	(1)~\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).
41	(2)~\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \citep{cho2014gru} with attention \citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.
42	(3)~\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.
43	(4)~\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\$11.66 API cost for the SWE test set).
44	(5)~\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.
45	
46	\paragraph{Metrics.}
47	Macro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\textsubscript{stag}) and progress (F1\textsubscript{prog}).
48	
49	%-------------------------------------------------------------------
50	\subsection{Main Results}
51	\label{sec:main_results}
52	
53	Table~\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\geq}$2 test set and cross-agent transfer to OpenHands.
54	
55	\begin{table*}[t]
56	\centering
57	\small
58	\begin{tabular}{l ccc cc}
59	\toprule
60	& \multicolumn{3}{c}{\textbf{SWE-Agent In-Domain} (conf${\geq}$2)} & \multicolumn{2}{c}{\textbf{OpenHands Transfer}} \\
61	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
62	\textbf{Method} & Macro-F1 & F1\textsubscript{stag} & F1\textsubscript{prog} & All & Conf${\geq}$2 \\
63	\midrule
64	Structural RF$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \textbf{0.9959} \\
65	Structural GB$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & \textbf{0.9674} & \underline{0.9919} \\
66	Structural LR$^\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\
67	ProgressProbe (GRU)           & \underline{0.9055} & 0.8593 & 0.9518 & 0.598 & 0.598 \\
68	\quad + full OH fine-tune      & ---    & ---    & ---    & 0.9763 & --- \\
69	Mean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\
70	LLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\
71	Cosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\
72	\bottomrule
73	\end{tabular}
74	\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \textbf{bold}, second-best \underline{underlined}.}
75	\label{tab:main_results}
76	\end{table*}
77	
78	In-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\,pp.
79	However, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.
80	The more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.
81	The LLM judge underperforms all learned methods despite substantially higher cost.
82	
83	%-------------------------------------------------------------------
84	\subsection{Cross-Agent Transfer}
85	\label{sec:cross_agent}
86	
87	Table~\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.
88	Structural GB transfers best, achieving 0.967 macro-F1 on all OH windows.
89	RF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.
90	Both structural models recover to $>$0.99 on conf${\geq}$2 OH windows, where label noise is lower.
91	
92	The probe's zero-shot transfer (0.598 on all windows) lags structural GB by 36.9\,pp, but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.9763, within 2.2\,pp of structural GB (0.967) on the same test set (\S\ref{sec:cmd_rep_ablation}).
93	The asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\,pp gap); with target-domain labels, the probe converges to near-structural performance.
94	The practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.
95	
96	\paragraph{Multi-seed stability.}
97	Structural RF: $0.9951{\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\pm}0.0015$.
98	The probe shows higher variance: $0.9185{\pm}0.0113$, though all seeds exceed 0.90.
99	
100	%-------------------------------------------------------------------
101	\subsection{Robustness Analysis}
102	\label{sec:robustness}
103	
104	\paragraph{Encoder ablation.}
105	Replacing Qwen3-0.6B with BGE-M3 \citep{chen2024bgem3} or E5-large-v2 \citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\ 0.9055 for Qwen3).
106	All encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\ref{tab:encoder_ablation}.
107	
108	\paragraph{Window size.}
109	$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\,pp and $k{=}7$ drops 1.8\,pp.
110	Shorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.
111	The 0.9309 figure differs from the main table's 0.9055 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.
112	Details in Appendix Table~\ref{tab:window_ablation}.
113	
114	\paragraph{Data scaling.}
115	Figure~\ref{fig:data_scaling} compares data efficiency across methods.
116	Structural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\% training data, fully saturating by 50\%.
117	The probe scales monotonically from 0.805 (10\%) to 0.906 (100\%) but has not plateaued---a 10.1\,pp drop that is roughly 20$\times$ the structural degradation (${\sim}$0.4--0.8\,pp).
118	This data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.
119	
120	\begin{figure}[t]
121	\centering
122	\includegraphics[width=\columnwidth]{../../figures/paper/fig_data_scaling.pdf}
123	\caption{Macro-F1 vs.\ training data fraction. Structural classifiers (RF, GB) saturate by 50\% data; the probe scales monotonically but remains 9\,pp below at 100\%.}
124	\label{fig:data_scaling}
125	\end{figure}
126	
127	%-------------------------------------------------------------------
128	\subsection{Labeling Function Temporal Dynamics}
129	\label{sec:lf_temporal}
130	
131	We analyze when each LF first fires relative to the onset of stagnation episodes (Table~\ref{tab:lf_temporal}, Figure~\ref{fig:lf_temporal}).
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\begin{tabular}{lrrrr}
137	\toprule
138	\textbf{LF} & \textbf{Lag} & \textbf{Lead\,\%} & \textbf{Conc.\,\%} & \textbf{Lag\,\%} \\
139	\midrule
140	cmd\_rep      & $-1.87$ & 36.1 & --- & --- \\
141	file\_diff    & $-1.20$ & 17.1 & --- & --- \\
142	outcome\_bp   & $+6.70$ & ---  & --- & 48.4 \\
143	\bottomrule
144	\end{tabular}
145	\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}
146	\label{tab:lf_temporal}
147	\end{table}
148	
149	The three LFs occupy distinct temporal niches.
150	Command repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.
151	File diff is near-concurrent ($-1.20$ steps).
152	Outcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.
153	
154	All pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\_rep vs.\ file\_diff $p{=}1.44{\times}10^{-26}$, cmd\_rep vs.\ outcome\_bp $p{=}6.67{\times}10^{-39}$, file\_diff vs.\ outcome\_bp $p{=}3.47{\times}10^{-47}$).
155	
156	\paragraph{Cross-agent reversal.}
157	On OpenHands, cmd\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).
158	This reversal explains the cmd\_rep pathology analyzed in \S\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\_rep on progress windows, inverting its diagnostic value.
159	
160	\begin{figure}[t]
161	\centering
162	\includegraphics[width=\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}
163	\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\_rep leads ($-1.87$ steps), file\_diff is near-concurrent ($-1.20$), outcome\_bp lags ($+6.70$). Inset: OH reversal where cmd\_rep becomes lagging.}
164	\label{fig:lf_temporal}
165	\end{figure}
166	
167	%-------------------------------------------------------------------
168	\subsection{Label Quality and cmd\_rep Coverage}
169	\label{sec:cmd_rep_ablation}
170	
171	A label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.
172	After correction, the OH stagnation rate shifted from 6.56\% to 21.45\%, with 21,898 window labels flipping.
173	This section quantifies how label quality and cmd\_rep coverage jointly affect probe transfer.
174	
175	\paragraph{Label correction impact on probe transfer.}
176	With corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.9763 (previously 0.751 under corrupted labels).
177	The improvement is most dramatic at low data fractions: 5\% fine-tuning now reaches 0.850, exceeding the old 50\% result (0.688) by 16.2\,pp.
178	Label quality, not model capacity, was the transfer bottleneck.
179	
180	\paragraph{Prevalence-matched ablation.}
181	To isolate cmd\_rep's contribution, we compare 3-LF and 2-LF (no cmd\_rep) models on the same test set with matched class prevalence.
182	
183	\begin{table}[t]
184	\centering
185	\small
186	\begin{tabular}{lccc}
187	\toprule
188	\textbf{LF Config} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} \\
189	\midrule
190	3-LF (w/ cmd\_rep) & \textbf{0.9763} & 0.960 & 0.993 \\
191	2-LF (no cmd\_rep) & 0.6822 & 0.481 & 0.884 \\
192	\midrule
193	$\Delta$ & $-29.4$\,pp & $-47.9$\,pp & $-10.9$\,pp \\
194	\bottomrule
195	\end{tabular}
196	\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\%). Removing cmd\_rep drops macro-F1 by 29.4\,pp (McNemar $\chi^2{=}1551$, $p{\approx}0$).}
197	\label{tab:cmd_rep_ablation}
198	\end{table}
199	
200	Removing cmd\_rep drops macro-F1 by 29.4\,pp (McNemar $\chi^2{=}1551$, $p{\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\,pp F1\textsubscript{stag}).
201	
202	\paragraph{Coverage, not label quality, explains the gap.}
203	The 29.4\,pp drop is not caused by cmd\_rep improving label accuracy.
204	After correction, cmd\_rep fires on only 5.39\% of OH windows (down from the previously reported 92.2\% under corrupted embeddings) with 97.91\% precision---a high-precision, low-recall signal.
205	On the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\% of labels: cmd\_rep does not change any label where the other two LFs already vote.
206	Its contribution is purely \emph{coverage}: including cmd\_rep expands the training set from ${\sim}$4K to ${\sim}$43K windows (a ${\sim}$10$\times$ increase).
207	The 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.
208	
209	\paragraph{Implications for weak supervision.}
210	These results reframe how labeling functions contribute to weak supervision pipelines.
211	A high-precision, low-recall LF like cmd\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.
212	In prevalence-matched evaluation, this data reduction manifests as a 29.4\,pp F1 drop.
213	The core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors.
214	
215	%-------------------------------------------------------------------
216	\subsection{Temporal Label Models}
217	\label{sec:temporal_label_models}
218	
219	We investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).
220	Table~\ref{tab:temporal_models} compares three temporal label models \citep{ratner2017snorkel,safranchik2020linkedhmm}.
221	
222	\begin{table}[t]
223	\centering
224	\small
225	\begin{tabular}{lccc}
226	\toprule
227	\textbf{Method} & \textbf{Conf${\geq}$2 F1} & \textbf{MV Agr.} & \textbf{Probe F1$^\ddagger$} \\
228	\midrule
229	MV (baseline) & 0.8946$^\ast$ & 1.000 & 0.8468 \\
230	TWV ($\sigma{=}2$) & \textbf{0.9003} & 0.885 & 0.8211 \\
231	Lag-HMM & 0.8936 & 0.820 & --- \\
232	HMM & 0.7502 & 0.685 & 0.6564 \\
233	\bottomrule
234	\end{tabular}
235	\caption{Temporal label model comparison. $^\ast$MV conf${\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\ddagger$Downstream: probe trained on each method's labels, evaluated on the full SWE-Agent test set ($N{=}8{,}101$) against MV labels.}
236	\label{tab:temporal_models}
237	\end{table}
238	
239	TWV achieves the highest conf${\geq}$2 F1 (0.9003, +0.57\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\ 0.8468 for MV-trained ($-2.57$\,pp).
240	TWV flips 14.1\% of conf$=$1 labels, introducing noise that hurts probe training.
241	HMM overpredicts stagnation (29,176 stagnation vs.\ 25,633 progress windows), degrading downstream performance to 0.6564.
242	Lag-HMM closely tracks MV ($-0.1$\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \emph{aggregation}.
243	
244	\paragraph{TWV sensitivity.}
245	The Gaussian kernel bandwidth $\sigma$ is critical: $\sigma{=}2$ is optimal (0.9003); $\sigma{=}1$ drops to 0.8105 and $\sigma{=}5$ drops to 0.808.
246	This narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.
247	
248	These results constitute a negative finding: despite clear temporal structure in LF firing patterns (\S\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.
249	
250	%-------------------------------------------------------------------
251	\subsection{Gold Set Validation}
252	\label{sec:gold_set}
253	\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "bae8a1a3-a7f0-410b-84ba-5ed72b04d71f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 21.4\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 21.4 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.598 & 0.598 \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.9763 & --- \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe LLM judge underperforms all learned methods despite substantially higher cost.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows.\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.598 on all windows) lags structural GB by 36.9\\,pp, but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.9763, within 2.2\\,pp of structural GB (0.967) on the same test set (\\S\\ref{sec:cmd_rep_ablation}).\nThe asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\\,pp gap); with target-domain labels, the probe converges to near-structural performance.\nThe practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.9951{\\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$.\nThe probe shows higher variance: $0.9185{\\pm}0.0113$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\\ 0.9055 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nThe 0.9309 figure differs from the main table's 0.9055 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} compares data efficiency across methods.\nStructural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\\% training data, fully saturating by 50\\%.\nThe probe scales monotonically from 0.805 (10\\%) to 0.906 (100\\%) but has not plateaued---a 10.1\\,pp drop that is roughly 20$\\times$ the structural degradation (${\\sim}$0.4--0.8\\,pp).\nThis data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Macro-F1 vs.\\ training data fraction. Structural classifiers (RF, GB) saturate by 50\\% data; the probe scales monotonically but remains 9\\,pp below at 100\\%.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nThis reversal explains the cmd\\_rep pathology analyzed in \\S\\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\\_rep on progress windows, inverting its diagnostic value.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Label Quality and cmd\\_rep Coverage}\n\\label{sec:cmd_rep_ablation}\n\nA label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.\nAfter correction, the OH stagnation rate shifted from 6.56\\% to 21.45\\%, with 21,898 window labels flipping.\nThis section quantifies how label quality and cmd\\_rep coverage jointly affect probe transfer.\n\n\\paragraph{Label correction impact on probe transfer.}\nWith corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.9763 (previously 0.751 under corrupted labels).\nThe improvement is most dramatic at low data fractions: 5\\% fine-tuning now reaches 0.850, exceeding the old 50\\% result (0.688) by 16.2\\,pp.\nLabel quality, not model capacity, was the transfer bottleneck.\n\n\\paragraph{Prevalence-matched ablation.}\nTo isolate cmd\\_rep's contribution, we compare 3-LF and 2-LF (no cmd\\_rep) models on the same test set with matched class prevalence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & \\textbf{0.9763} & 0.960 & 0.993 \\\\\n2-LF (no cmd\\_rep) & 0.6822 & 0.481 & 0.884 \\\\\n\\midrule\n$\\Delta$ & $-29.4$\\,pp & $-47.9$\\,pp & $-10.9$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\\%). Removing cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$).}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\\,pp F1\\textsubscript{stag}).\n\n\\paragraph{Coverage, not label quality, explains the gap.}\nThe 29.4\\,pp drop is not caused by cmd\\_rep improving label accuracy.\nAfter correction, cmd\\_rep fires on only 5.39\\% of OH windows (down from the previously reported 92.2\\% under corrupted embeddings) with 97.91\\% precision---a high-precision, low-recall signal.\nOn the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\\% of labels: cmd\\_rep does not change any label where the other two LFs already vote.\nIts contribution is purely \\emph{coverage}: including cmd\\_rep expands the training set from ${\\sim}$4K to ${\\sim}$43K windows (a ${\\sim}$10$\\times$ increase).\nThe 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.\n\n\\paragraph{Implications for weak supervision.}\nThese results reframe how labeling functions contribute to weak supervision pipelines.\nA high-precision, low-recall LF like cmd\\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.\nIn prevalence-matched evaluation, this data reduction manifests as a 29.4\\,pp F1 drop.\nThe core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares three temporal label models \\citep{ratner2017snorkel,safranchik2020linkedhmm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{MV Agr.} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 0.8946$^\\ast$ & 1.000 & 0.8468 \\\\\nTWV ($\\sigma{=}2$) & \\textbf{0.9003} & 0.885 & 0.8211 \\\\\nLag-HMM & 0.8936 & 0.820 & --- \\\\\nHMM & 0.7502 & 0.685 & 0.6564 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal label model comparison. $^\\ast$MV conf${\\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\\ddagger$Downstream: probe trained on each method's labels, evaluated on the full SWE-Agent test set ($N{=}8{,}101$) against MV labels.}\n\\label{tab:temporal_models}\n\\end{table}\n\nTWV achieves the highest conf${\\geq}$2 F1 (0.9003, +0.57\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\\ 0.8468 for MV-trained ($-2.57$\\,pp).\nTWV flips 14.1\\% of conf$=$1 labels, introducing noise that hurts probe training.\nHMM overpredicts stagnation (29,176 stagnation vs.\\ 25,633 progress windows), degrading downstream performance to 0.6564.\nLag-HMM closely tracks MV ($-0.1$\\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \\emph{aggregation}.\n\n\\paragraph{TWV sensitivity.}\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal (0.9003); $\\sigma{=}1$ drops to 0.8105 and $\\sigma{=}5$ drops to 0.808.\nThis narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.\n\nThese results constitute a negative finding: despite clear temporal structure in LF firing patterns (\\S\\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\n\\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}",
      "numLines": 253,
      "startLine": 1,
      "totalLines": 253
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

All edits applied correctly. Summary of changes:

**§5.1** — OH stagnation ratio: 6.6% → 21.4% (text line 20 + Table 1 line 32)

**§5.2 Table 2** — ProgressProbe OH Transfer: 0.530/0.528 → 0.598/0.598; fine-tune: 0.7510 → 0.9763

**§5.3** — Rewrote cross-agent narrative: removed the false 21.6pp claim, reframed as stage-dependent asymmetry (zero-shot gap 36.9pp closes to 2.2pp after FT), added deployment trade-off framing

**§5.5** — Complete rewrite as "Label Quality and cmd\_rep Coverage":
- Label audit discovery (stag rate 6.56%→21.45%, 21,898 labels flipped)
- Label quality as transfer bottleneck (FT 0.751→0.9763, 5% FT now beats old 50%)
- New Table 3: prevalence-matched ablation (3-LF 0.9763 vs 2-LF 0.6822, Δ=-29.4pp, McNemar p≈0)
- Coverage explanation (cmd\_rep fires 5.39%, precision 97.91%, 100% agreement on intersection, 4K→43K training data expansion)
- WS implications paragraph on coverage vs label refinement

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "uuid": "bdabe29c-288e-410c-9c18-0c7c7fcbbb25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XL2xj9ZroZxhPMVPZrBJ2q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6330,
      "cache_read_input_tokens": 34450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6330
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

_source line 25_

All edits applied correctly. Summary of changes:

**§5.1** — OH stagnation ratio: 6.6% → 21.4% (text line 20 + Table 1 line 32)

**§5.2 Table 2** — ProgressProbe OH Transfer: 0.530/0.528 → 0.598/0.598; fine-tune: 0.7510 → 0.9763

**§5.3** — Rewrote cross-agent narrative: removed the false 21.6pp claim, reframed as stage-dependent asymmetry (zero-shot gap 36.9pp closes to 2.2pp after FT), added deployment trade-off framing

**§5.5** — Complete rewrite as "Label Quality and cmd\_rep Coverage":
- Label audit discovery (stag rate 6.56%→21.45%, 21,898 labels flipped)
- Label quality as transfer bottleneck (FT 0.751→0.9763, 5% FT now beats old 50%)
- New Table 3: prevalence-matched ablation (3-LF 0.9763 vs 2-LF 0.6822, Δ=-29.4pp, McNemar p≈0)
- Coverage explanation (cmd\_rep fires 5.39%, precision 97.91%, 100% agreement on intersection, 4K→43K training data expansion)
- WS implications paragraph on coverage vs label refinement

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 111297,
  "duration_api_ms": 112402,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "7307d395-315f-421d-9b97-32ea4316dab7",
  "total_cost_usd": 0.40070525,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 28939,
    "cache_read_input_tokens": 227395,
    "output_tokens": 4154,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28939,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 356,
        "cache_read_input_tokens": 34450,
        "cache_creation_input_tokens": 6330,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6330
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2134,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002239,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 4154,
      "cacheReadInputTokens": 227395,
      "cacheCreationInputTokens": 28939,
      "webSearchRequests": 0,
      "costUSD": 0.39846625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a28c6ddb-9fe7-4283-8ddc-9699a9447678"
}
```

</details>

---
