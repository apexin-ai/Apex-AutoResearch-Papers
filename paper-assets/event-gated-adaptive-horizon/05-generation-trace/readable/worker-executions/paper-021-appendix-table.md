# paper 021 appendix table

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_021-appendix-table_20260517T234234.log`
- **Structured JSON:** [`06b044cf5ab880ad3dac.json`](../../sessions/06/06b044cf5ab880ad3dac.json)

## Before a recorded user message

29 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
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
  "uuid": "ea1f41c7-80d5-4b48-9230-be232cf4fb54",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779067800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8ded831f-cc20-4e0f-ae66-ac51e092b678",
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9"
}
```

---

### Assistant

_source line 4_

Let me read the relevant files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "4cbebb4d-7555-4fea-a052-9f045b8eeda4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWD7PP6RPSwckWjzRWFV5g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13041,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13041
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

<details open><summary>🔧 Tool call — Read · `toolu_0124LhfZkgABsEzcajeJTrsk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "1d98580b-329b-4e4a-8c52-6d344c89bf8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWD7PP6RPSwckWjzRWFV5g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13041,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13041
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

_source line 6 · 2026-05-17T23:42:47.381Z_

<details><summary>↩ Tool result · `toolu_0124LhfZkgABsEzcajeJTrsk`</summary>

```text
1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 17 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3), SGS interventions (018), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
11	\label{tab:complete_results}
12	\footnotesize
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{llcccccl}
15	\toprule
16	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
17	\midrule
18	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
19	\rowcolor{gray!15}
20	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
21	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
22	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
23	\midrule
24	\rowcolor{gray!15}
25	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
26	\rowcolor{gray!15}
27	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
28	\rowcolor{gray!15}
29	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
30	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
31	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
32	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
33	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
34	\midrule
35	018 s1 & Full-SGS & trn$^\ddagger$ & ON & 8 & \sgseval{} @105K & \sgsnve{}$\times$$^*$ & No collapse \\
36	\rowcolor{gray!15}
37	018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
38	008e\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\times$ & Healthy \\
39	008e\_v3 s2$^\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\times$ & Non-CIVO collapse \\
40	\midrule
41	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
42	\rowcolor{gray!15}
43	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
44	021 & Cheetah Run & trn+SGS & ON & 8 & 221.5 @105K & $<$1$\times$$^d$ & Recovery \\
45	\rowcolor{gray!15}
46	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
47	\bottomrule
48	\end{tabular}
49	\vspace{1pt}
50	{\raggedright\footnotesize
51	trn = trained ($d{=}32$, subsample ON);
52	trn$^\ddagger$ = full-pathway SGS (all non-KL gradients detached);
53	trn+SGS = trained ($d{=}32$) with Full-SGS;
54	exp$^a$ = trained, subsample OFF;
55	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
56	--- = removed ($d{=}0$).\\
57	$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
58	$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\
59	$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
60	$^d$ Sustained NVE (55K--105K). Peak NVE $9.94\times$ at 45K (transient CIVO onset, self-correcting); normalized against exp\_023a/023b Cheetah baselines.\par}
61	\end{table*}
62	
63	\section{NVE Threshold Sensitivity Analysis}
64	\label{sec:appendix_sensitivity}
65	
66	We report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\nve \geq 1.5\times$). Here we additionally present Task~B1, which restricts the positive class to \emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.
67	
68	\subsection{Per-Experiment NVE Values}
69	
70	Table~\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eight factorial experiments. Experiments are sorted by descending NVE. Experiment 008e\_v3\_s2 exhibits elevated NVE ($3.78\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks.
71	
72	\begin{table}[h]
73	\centering
74	\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\ = transient CIVO with self-correction.}
75	\label{tab:nve_raw}
76	\small
77	\begin{tabular}{@{}lrccc@{}}
78	\toprule
79	Experiment & NVE & Mechanism & B1 & B2 \\
80	\midrule
81	006          & 4.84 & sustained CIVO & $+$ & $+$ \\
82	008d         & 4.13 & sustained CIVO & $+$ & $+$ \\
83	008e\_v3\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\
84	009b         & 1.62 & transient CIVO & $-$ & $+$ \\
85	001          & 1.00 & non-CIVO       & $-$ & $-$ \\
86	008f         & 0.97 & non-CIVO       & $-$ & $-$ \\
87	008e\_v3\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\
88	008a         & 0.93 & non-CIVO       & $-$ & $-$ \\
89	\bottomrule
90	\end{tabular}
91	\end{table}
92	
93	\subsection{Multi-Threshold Classification Performance}
94	
95	Table~\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\text{AUROC} = 1.000$ because the minimum positive NVE ($4.13\times$, exp~008d) exceeds the maximum negative NVE ($3.78\times$, exp~008e\_v3\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.13]$; we report $\geq 3.9\times$ as a representative value. Table~\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\text{AUROC} = 0.933$, imperfect separation due to 008e\_v3\_s2).
96	
97	\begin{table*}[t]
98	\centering
99	\caption{\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\text{pos}}=2$, $n_{\text{neg}}=6$, $n=8$, $\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\alpha=0.05$). Thresholds 1.2$\times$/1.5$\times$ and 1.7$\times$/2.0$\times$ yield identical operating points (no NVE values in those intervals). $^\dagger$Optimal threshold in $(3.78, 4.13]$.}
100	\label{tab:sensitivity_b1}
101	\small
102	\setlength{\tabcolsep}{5pt}
103	\begin{tabular}{@{}lcccccccc@{}}
104	\toprule
105	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
106	\midrule
107	$\geq 1.0\times$ & 2 & 3 & 0 & 3 & 62.5\% \; [24.5, 91.5] & 40.0\% & 100\% & 57.1\% \\
108	$\geq 1.2\times$ & 2 & 2 & 0 & 4 & 75.0\% \; [34.9, 96.8] & 50.0\% & 100\% & 66.7\% \\
109	$\geq 1.5\times$ & 2 & 2 & 0 & 4 & 75.0\% \; [34.9, 96.8] & 50.0\% & 100\% & 66.7\% \\
110	\rowcolor{gray!15}
111	$\geq 1.7\times$ & 2 & 1 & 0 & 5 & 87.5\% \; [47.3, 99.7] & 66.7\% & 100\% & 80.0\% \\
112	$\geq 2.0\times$ & 2 & 1 & 0 & 5 & 87.5\% \; [47.3, 99.7] & 66.7\% & 100\% & 80.0\% \\
113	\rowcolor{gray!15}
114	$\geq 3.9\times^\dagger$ & 2 & 0 & 0 & 6 & 100\% \; [63.1, 100] & 100\% & 100\% & 100\% \\
115	\bottomrule
116	\end{tabular}
117	\end{table*}
118	
119	\begin{table*}[t]
120	\centering
121	\caption{\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\text{pos}}=3$, $n_{\text{neg}}=5$, $n=8$, $\text{AUROC}=0.933$). The single false positive at $\geq 1.5\times$ is 008e\_v3\_s2 (IRD mechanism, not CIVO). The $1.5\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}
122	\label{tab:sensitivity_b2}
123	\small
124	\setlength{\tabcolsep}{5pt}
125	\begin{tabular}{@{}lcccccccc@{}}
126	\toprule
127	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
128	\midrule
129	$\geq 1.0\times$ & 3 & 2 & 0 & 3 & 75.0\% \; [34.9, 96.8] & 60.0\% & 100\% & 75.0\% \\
130	$\geq 1.2\times$ & 3 & 1 & 0 & 4 & 87.5\% \; [47.3, 99.7] & 75.0\% & 100\% & 85.7\% \\
131	\rowcolor{gray!15}
132	$\geq 1.5\times$ & 3 & 1 & 0 & 4 & 87.5\% \; [47.3, 99.7] & 75.0\% & 100\% & 85.7\% \\
133	$\geq 1.7\times$ & 2 & 1 & 1 & 4 & 75.0\% \; [34.9, 96.8] & 66.7\% & 66.7\% & 66.7\% \\
134	$\geq 2.0\times$ & 2 & 1 & 1 & 4 & 75.0\% \; [34.9, 96.8] & 66.7\% & 66.7\% & 66.7\% \\
135	$\geq 3.9\times$ & 2 & 0 & 1 & 5 & 87.5\% \; [47.3, 99.7] & 100\% & 66.7\% & 80.0\% \\
136	\bottomrule
137	\end{tabular}
138	\end{table*}
139	
140	\subsection{Threshold Recommendation}
141	
142	For the main diagnostic (Task~B2), we recommend $\nve \geq 1.5\times$ as the operating threshold for three reasons:
143	
144	\begin{enumerate}[nosep,leftmargin=*]
145	\item \textbf{Maximum recall.} The $1.5\times$ threshold achieves 100\% recall, detecting all three CIVO cases including the transient case (009b, $\nve = 1.62\times$). Raising the threshold to $1.7\times$ loses 009b, dropping recall to 66.7\%.
146	\item \textbf{Best F1.} At $1.5\times$, F1 = 85.7\%, the highest among all tested thresholds for B2. The single false positive (008e\_v3\_s2) is mechanistically identifiable as IRD rather than CIVO.
147	\item \textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\times$) add false positives without gaining true positives. Higher thresholds ($\geq 1.7\times$) sacrifice recall without eliminating the 008e\_v3\_s2 false positive (which requires $\tau > 3.78$).
148	\end{enumerate}
149	
150	For Task~B1 (sustained CIVO only), perfect classification is achievable at $\nve \geq 3.9\times$, but with only $n_{\text{pos}} = 2$ the statistical power is severely limited (accuracy 95\% CI: [63.1\%, 100\%]).
151	
152	\paragraph{Limitations.} With $n = 8$ experiments, all Clopper-Pearson confidence intervals are wide (e.g., 87.5\% accuracy has 95\% CI [47.3\%, 99.7\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds.
153	
154	% --- APPENDIX B: Factorial Ablation Details ---
155	
156	\section{Factorial Ablation Details}
157	\label{sec:appendix_factorial}
158	
159	This appendix provides the full factorial ablation results summarized in \S\ref{sec:f3f5_summary} of the main text.
160	
161	\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}
162	\label{sec:f3}
163	
164	\begin{figure}[t]
165	\centering
166	\includegraphics[width=\columnwidth]{figures/paper/fig3_factorial_grid.pdf}
167	\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}
168	\label{fig:factorial_grid}
169	\end{figure}
170	
171	The causal claim that trained embedding \emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.
172	
173	\paragraph{Evidence A: exposure is necessary (exp\_008a).}
174	Exp\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\_008d, its NVE remains in the $0.59$--$0.93\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\dt{>}1$ state predictions within the RSSM.
175	
176	This contrasts with exp\_006 (trained $e_{\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\times$ at 45K to $2.31\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\dt{>}1$ transitions during training, confirming that multi-rate data exposure, not embedding architecture, is the operative variable.
177	
178	\paragraph{Evidence B: trainability is necessary (exp\_015b).}
179	Exp\_015b uses a frozen random-projection embedding ($d{=}32$, \texttt{requires\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\_008d, but with a non-trainable temporal signal. Despite full exposure to $\dt{>}1$ transitions, the NVE peaks at $1.45\times$ at 55K but does not sustain escalation: it retreats to $0.65\times$ by 65K and settles at $0.55\times$ by 105K (trajectory: $0.81 \rightarrow 1.26 \rightarrow 1.45 \rightarrow 0.65 \rightarrow 1.05 \rightarrow 0.60 \rightarrow 0.59 \rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \S\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.
180	
181	The contrast with exp\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\times$ with sustained monotonic escalation ($1.78 \rightarrow 1.71 \rightarrow 2.09 \rightarrow 4.12$) and triggers full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\times$ before self-correcting to $0.55\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\dt$-embedding must be able to \emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.
182	
183	Together, these two controls establish that CIVO requires the \emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.
184	
185	\begin{table}[h]
186	\centering
187	\small
188	\caption{Causal isolation: $e_{\dt}$ configuration $\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}
189	\label{tab:causal_matrix}
190	\begin{tabular}{lcc}
191	\toprule
192	& Multi-rate data (\textsc{on}) & Single-rate data (\textsc{off}) \\
193	\midrule
194	Trained $e_{\dt}$ & exp\_008d: \textbf{CIVO} & exp\_008a: healthy \\
195	 & NVE 4.12$\times$, collapse & NVE 0.93$\times$ \\
196	\midrule
197	Frozen $e_{\dt}$ & exp\_015b: grad.\ starvation & --- \\
198	 & peak NVE 1.45$\times$ (transient) & \\
199	\midrule
200	Removed $e_{\dt}$ & exp\_008f: no CIVO & --- \\
201	 & NVE $\leq$0.97$\times$ & \\
202	\bottomrule
203	\end{tabular}
204	\end{table}
205	
206	Only the upper-left cell (trained embedding with multi-rate exposure) triggers CIVO (Table~\ref{tab:causal_matrix}). This 2$\times$2 structure establishes that both factors are jointly necessary.
207	
208	\subsection{F4: Degradation Scales Monotonically with \texorpdfstring{$\dt$}{dt}}
209	\label{sec:f4}
210	
211	\begin{figure}[t]
212	\centering
213	\includegraphics[width=\columnwidth]{figures/paper/fig5_dt_amplification.pdf}
214	\caption{Peak evaluation return as a function of imagination $\dt$. Performance degrades monotonically: $\dt{=}1$ (915.7) $>$ $\dt{=}2$ (485.3, $-47\%$) $>$ $\dt{=}4$ (176.9, $-81\%$).}
215	\label{fig:dt_amplification}
216	\end{figure}
217	
218	The magnitude of degradation scales monotonically with the imagination step size (Figure~\ref{fig:dt_amplification}). From the $\dt{=}1$ baseline (915.7 at 105K), fixed $\dt{=}2$ (exp\_006) achieves a peak of only 485.3 ($-47\%$), and fixed $\dt{=}4$ (exp\_007) peaks at 176.9 ($-81\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.
219	
220	\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}
221	\label{sec:f5}
222	
223	Neither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\nve < 0.93\times$ (\S\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\nve = 4.12\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\ 009c: 148.3) but neither exhibits $\nve > 1.5\times$, confirming that low evaluation alone does not indicate CIVO.
224	
225	The $3.2\times$ performance gap (008a: 777.7 vs.\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\leq$0.93$\times$).
226	
227	% --- APPENDIX C: Full Analysis & Discussion ---
228	
229	\section{Full Analysis \& Discussion}
230	\label{sec:appendix_analysis}
231	
232	This appendix provides the complete mechanistic analysis summarized in Section~\ref{sec:discussion} of the main text.
233	
234	\subsection{The CIVO Mechanism}
235	\label{sec:civo_mechanism}
236	
237	The RSSM fidelity analysis (Table~\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\dt{=}1$ is $0.0568$, while at $\dt{=}2$ it rises to $0.1579$, a $2.78\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\times$ gap, and the baseline shows $1.56\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.
238	
239	This asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\dt$-embedding causes RSSM predictions at $\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\nve$ above $1.5\times$, followed by evaluation collapse.
240	
241	A random-policy control experiment ($N{=}100$ rollouts, 95\% bootstrap CI) decomposes CIVO into two necessary stages.  \textbf{Stage~1 (dynamics bias):} even under a random policy, $\dt{=}2$ imagination produces $1.68\times$ higher mean reward than $\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\dt > 1$, independent of actor behavior.  \textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\times$ and the trained-actor ratio is $0.98\times$.  The decomposition attributes $\approx 36\%$ of the total effect to dynamics bias and $\approx 64\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.
242	
243	This mechanism is analogous to delusional bias \citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced: the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.
244	
245	\subsection{Selective Gradient Stopping and Gradient Decomposition}
246	\label{sec:sgs_gradient_analysis}
247	
248	\subsubsection{Gradient Decomposition Results}
249	\label{sec:gradient_decomposition}
250	
251	\begin{figure}[t]
252	\centering
253	\includegraphics[width=0.75\columnwidth]{figures/fig3_gradient_decomposition.pdf}
254	\caption{Gradient contribution to $e_{\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\%) yet reward-only SGS (exp\_016e) fails; the observation decoder channel (16--22\%) carries the critical $\dt$-specific spatial information that drives the RSSM fidelity gap.}
255	\label{fig:gradient_decomp}
256	\end{figure}
257	
258	Exp\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\times$. The SGS intervention neither prevented nor attenuated CIVO.
259	
260	To explain this null result, we performed a gradient decomposition analysis using \texttt{torch.autograd.grad} to measure each loss component's contribution to $\nabla_\theta e_{\Delta t}$, where $\theta$ denotes the temporal embedding parameters. Table~\ref{tab:gradient_decomposition} reports the results.
261	
262	\begin{table}[h]
263	\centering
264	\caption{Gradient contributions to the temporal embedding $e_{\Delta t}$ by loss component, measured via \texttt{torch.autograd.grad} with training configuration \texttt{gate\_fixed\_dt=2}. Gradient norms are $\ell_2$ norms of $\nabla_\theta \mathcal{L}_i$ for each loss $\mathcal{L}_i$.}
265	\label{tab:gradient_decomposition}
266	\small
267	\begin{tabular}{lrrrr}
268	\toprule
269	& \multicolumn{2}{c}{\textbf{@55K}} & \multicolumn{2}{c}{\textbf{@112K}} \\
270	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
271	Loss component & Share & (\%) & Share & (\%) \\
272	\midrule
273	Reward head & --- & 49.0 & --- & 38.1 \\
274	KL dynamics & --- & 34.7 & --- & 40.4 \\
275	Observation decoders & --- & 16.3 & --- & 21.5 \\
276	\bottomrule
277	\end{tabular}
278	\end{table}
279	
280	The gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\% at 55K, 38.1\% at 112K), yet reward-only SGS (exp\_016e) fails catastrophically (NVE $10.42\times$). The observation decoder channel contributes the smallest share (16.3\% at 55K, 21.5\% at 112K) yet carries the critical $\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.
281	
282	The gradient structure is relatively stable across training (reward shifts from 49\% to 38\%, obs from 16\% to 22\%, KL from 35\% to 40\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.
283	
284	\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\times$ reward MAE ratio, Table~\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\Delta t}$, though its 50\% prevention rate (1/2 seeds) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.
285	
286	\subsubsection{Implications for the CIVO Mechanism}
287	\label{sec:sgs_implications}
288	
289	The gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.
290	
291	\paragraph{Gradient importance $\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\%) to $e_{\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\dt$-specific structural information: it adjusts $e_{\Delta t}$ to minimize a scalar prediction error that is largely $\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\Delta t}$ learns scale-dependent latent biases.
292	
293	\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\_016e (NVE $10.42\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\_018) detaches $e_{\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.
294	
295	\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\_008d) shows a $2.78\times$ reward gap between $\Delta t{=}1$ and $\Delta t{=}2$ transitions (Table~\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\Delta t}$ to produce latent states that are spatially biased at $\dt{>}1$, and the reward head inherits these biases \textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\Delta t}$'s parameters but not causal responsibility for the fidelity gap.
296	
297	\subsubsection{Entropy Dynamics Across Configurations}
298	\label{sec:entropy_dynamics}
299	
300	\begin{figure}[h]
301	\centering
302	\includegraphics[width=0.85\columnwidth]{figures/fig4_entropy_dynamics.pdf}
303	\caption{Actor entropy trajectories for three configurations. All start at ${\sim}8$ nats and converge to similar values (${\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}
304	\label{fig:entropy_dynamics}
305	\end{figure}
306	
307	\subsubsection{Exp\_016e Reinterpreted as Stochastic Variation}
308	\label{sec:016e_reinterp}
309	
310	The gradient decomposition establishes that exp\_016e targets the largest gradient pathway (reward: 38--49\%) but not the informationally critical one (observation decoders: 16--22\%).  The apparent timing differences between exp\_016e and exp\_008d (later collapse onset, 75K vs.\ 25K, and higher peak evaluation, 326.7 vs.\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\_008d, exp\_009b, exp\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\times$ pathological threshold at some point during training.
311	
312	\subsection{Post-CIVO Outcomes: Why Seeds Diverge}
313	\label{sec:seed_divergence}
314	
315	\begin{table}[h]
316	\centering
317	\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window.}
318	\label{tab:post_civo}
319	\footnotesize
320	\setlength{\tabcolsep}{3pt}
321	\begin{tabular}{lcccl}
322	\toprule
323	\textbf{Seed} & \textbf{Peak} & \textbf{Final} & \textbf{Eval} & \textbf{Outcome} \\
324	\midrule
325	s1 (008d) & 4.12$\times$ & 4.12$\times$ & 82.8 & Full collapse \\
326	s2 (009b) & 1.62$\times$ & 0.38$\times$ & 267.9 & Transient CIVO \\
327	\bottomrule
328	\end{tabular}
329	\end{table}
330	
331	The two post-CIVO outcomes (Table~\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\nve > 1.5\times$ threshold, yet the downstream damage is stochastic.\footnote{Exp\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control, confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).
332	
333	\subsection{Why MPC Is Immune}
334	\label{sec:mpc_immune}
335	
336	\citet{nhu2025tawm} show that $\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\dt > 1$ is amplified through the closed actor-critic loop.
337	
338	\subsection{The \texorpdfstring{$\dt$}{dt}-Embedding Dilemma}
339	\label{sec:embedding_dilemma}
340	
341	The factorial results reveal a fundamental tension: removing the $\dt$-embedding (008f) eliminates CIVO but at a $13\times$ cost to reward prediction quality ($0.7469$ vs.\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\dt{=}1$ while retaining the trained embedding (008e\_v3) prevents CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\S\ref{sec:f6}).  Neither approach alone provides a complete solution.
342	
343	\subsection{Multiple Vulnerability Pathways}
344	\label{sec:pathways}
345	
346	The two collapse mechanisms identified in \S\ref{sec:f6}, CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing), have distinct diagnostic signatures but a shared root cause: the trained $\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\times$ for 008e\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.
347	
348	\subsection{Implications for Temporal Abstraction in World Models}
349	\label{sec:implications}
350	
351	CIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \citep{gumbsch2024thick}, Hieros \citep{mattes2024hieros}, LS-Imagine \citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.
352	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "2cfa0296-63a1-4136-9f63-809dffdd677c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 17 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3), SGS interventions (018), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & No collapse \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n021 & Cheetah Run & trn+SGS & ON & 8 & 221.5 @105K & $<$1$\\times$$^d$ & Recovery \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\ntrn+SGS = trained ($d{=}32$) with Full-SGS;\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Sustained NVE (55K--105K). Peak NVE $9.94\\times$ at 45K (transient CIVO onset, self-correcting); normalized against exp\\_023a/023b Cheetah baselines.\\par}\n\\end{table*}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eight factorial experiments. Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.84 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.13 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.13\\times$, exp~008d) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.13]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.933$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=2$, $n_{\\text{neg}}=6$, $n=8$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). Thresholds 1.2$\\times$/1.5$\\times$ and 1.7$\\times$/2.0$\\times$ yield identical operating points (no NVE values in those intervals). $^\\dagger$Optimal threshold in $(3.78, 4.13]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 2 & 3 & 0 & 3 & 62.5\\% \\; [24.5, 91.5] & 40.0\\% & 100\\% & 57.1\\% \\\\\n$\\geq 1.2\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.5\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 2 & 0 & 0 & 6 & 100\\% \\; [63.1, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=5$, $n=8$, $\\text{AUROC}=0.933$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 2 & 0 & 3 & 75.0\\% \\; [34.9, 96.8] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.2\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 1.7\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 3.9\\times$ & 2 & 0 & 1 & 5 & 87.5\\% \\; [47.3, 99.7] & 100\\% & 66.7\\% & 80.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all three CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 66.7\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 85.7\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 2$ the statistical power is severely limited (accuracy 95\\% CI: [63.1\\%, 100\\%]).\n\n\\paragraph{Limitations.} With $n = 8$ experiments, all Clopper-Pearson confidence intervals are wide (e.g., 87.5\\% accuracy has 95\\% CI [47.3\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training, confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.55\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.60 \\rightarrow 0.59 \\rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and triggers full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.55\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$, confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced: the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 50\\% prevention rate (1/2 seeds) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe two post-CIVO outcomes (Table~\\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control, confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) prevents CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse mechanisms identified in \\S\\ref{sec:f6}, CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing), have distinct diagnostic signatures but a shared root cause: the trained $\\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.\n",
      "numLines": 352,
      "startLine": 1,
      "totalLines": 352
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_014QbjdLgV9eGWtdJ6tmjrj5`</summary>

```json
{
  "pattern": "**/sgs_informative_negative.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "0463ccfb-8047-4cbc-b6d0-2e7bb0c45245",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWD7PP6RPSwckWjzRWFV5g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13041,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13041
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

_source line 8 · 2026-05-17T23:42:48.066Z_

<details><summary>↩ Tool result · `toolu_014QbjdLgV9eGWtdJ6tmjrj5`</summary>

```text
paper/sections/sgs_informative_negative.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "f488e08d-6a75-4058-adb5-0f6302cef245",
  "tool_use_result": {
    "filenames": [
      "paper/sections/sgs_informative_negative.md"
    ],
    "durationMs": 18,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01QAbEHuNSAhT8timPcF7V11`</summary>

```json
{
  "pattern": "**/exp_021_full_sgs_cheetah_s1/report/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "1480f4f8-6c3d-4cd9-85c6-17f730d99c73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWD7PP6RPSwckWjzRWFV5g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13041,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13041
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

_source line 10 · 2026-05-17T23:42:48.519Z_

<details><summary>↩ Tool result · `toolu_01QAbEHuNSAhT8timPcF7V11`</summary>

```text
artifacts/exp_021_full_sgs_cheetah_s1/report/analysis.md
artifacts/exp_021_full_sgs_cheetah_s1/report/analysis_24b7c0.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "c77155ce-d056-44e1-8f4b-07facf083726",
  "tool_use_result": {
    "filenames": [
      "artifacts/exp_021_full_sgs_cheetah_s1/report/analysis.md",
      "artifacts/exp_021_full_sgs_cheetah_s1/report/analysis_24b7c0.md"
    ],
    "durationMs": 14,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

````text
The appendix already has exp_021 in the complete results table (line 44). Let me check the current content more carefully and also read the other files.

Looking at line 44:
```
021 & Cheetah Run & trn+SGS & ON & 8 & 221.5 @105K & $<$1$\times$$^d$ & Recovery \\
```

And there's footnote $^d$ on line 60:
```
$^d$ Sustained NVE (55K--105K). Peak NVE $9.94\times$ at 45K (transient CIVO onset, self-correcting); normalized against exp\_023a/023b Cheetah baselines.\par}


```

Now I need to check the other files to see what else might need updating.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "2808f075-6ba1-44af-a4c3-14b1c551ba5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gn3Kiy1Ggu7kzyeNLf51dg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11976,
      "cache_read_input_tokens": 24488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11976
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

exp_021 is already in the complete results table at line 44 with the correct data (221.5 @105K, Recovery). Let me check the other files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "0d3e84b8-3069-48b2-94d1-75b6fec31457",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gn3Kiy1Ggu7kzyeNLf51dg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11976,
      "cache_read_input_tokens": 24488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11976
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

<details open><summary>🔧 Tool call — Read · `toolu_01QjszYeeurK2MGSQ8YJdjq3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/sgs_informative_negative.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "e876e6d1-591f-4109-8d22-e0254a1c0b2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gn3Kiy1Ggu7kzyeNLf51dg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11976,
      "cache_read_input_tokens": 24488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11976
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

_source line 14 · 2026-05-17T23:43:00.410Z_

<details><summary>↩ Tool result · `toolu_01QjszYeeurK2MGSQ8YJdjq3`</summary>

```text
1	% SGS Informative Negative — Draft v1
2	% Target: CoRL 2026
3	% Status: Draft, pending Director review
4	% Depends on: experimental_setup.md (Section 4), method.md (Section 3)
5	
6	\subsection{Stop-Gradient Surgery: An Informative Negative Result}
7	\label{sec:sgs_informative_negative}
8	
9	The factorial analysis in Section~\ref{sec:factorial} establishes that a trained temporal embedding ($e_{\Delta t}$) is necessary for pathological value overestimation: conditions with removed or untrained embeddings do not exhibit CIVO (Section~\ref{sec:civo_mechanism}). A natural follow-up question is \textit{which gradient pathway} through $e_{\Delta t}$ amplifies the overestimation. We hypothesized that the reward head---which directly supplies the critic's $\lambda$-return targets---would be the primary amplifier: if reward predictions are systematically biased by $\Delta t$ conditioning, the critic inherits and compounds these biases across the imagination horizon. This section reports a stop-gradient intervention designed to test this hypothesis, and the gradient decomposition analysis that revealed why the intervention had no effect.
10	
11	\subsubsection{Hypothesis: Reward-Pathway Amplification}
12	
13	In DreamerV3, the temporal embedding $e_{\Delta t}$ is concatenated to the RSSM decoder input and conditions all prediction heads---observation decoders, reward head, and continuation predictor---simultaneously. The reward head's predictions enter the critic's $\lambda$-return computation directly:
14	$$G_t^\lambda = r_t + \gamma \big[(1-\lambda)\,V(s_{t+1}) + \lambda\, G_{t+1}^\lambda\big]$$
15	If the reward head learns $\Delta t$-dependent biases (e.g., systematically predicting higher rewards for $\Delta t{=}2$ transitions), these biases accumulate across the $H$-step imagination rollout. We therefore conjectured that detaching $e_{\Delta t}$ from the reward head's gradient computation would attenuate CIVO by preventing the reward predictor from specializing its parameters to the temporal embedding signal.
16	
17	\subsubsection{Experiment: Reward-Only Stop-Gradient (exp\_016e)}
18	
19	We implemented a targeted stop-gradient intervention, termed \textit{reward-only SGS} (Stop-Gradient Surgery), in which the temporal embedding is detached before entering the reward head during the backward pass:
20	$$\hat{r}_t = f_{\text{reward}}\big(\text{sg}(e_{\Delta t}),\; h_t,\; z_t\big)$$
21	where $\text{sg}(\cdot)$ denotes the stop-gradient operator. This prevents reward-loss gradients from updating $e_{\Delta t}$'s parameters while preserving the embedding's forward-pass contribution to reward prediction. All other gradient pathways through $e_{\Delta t}$---observation decoders, continuation predictor, KL dynamics loss---remain intact.
22	
23	The experiment uses the same configuration as exp\_008d (the primary CIVO-exhibiting condition): Walker Walk, trained $e_{\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\Delta t{=}2$ imagination, seed 1. The only modification is \texttt{reward\_dt\_emb\_detach=True}.
24	
25	\subsubsection{Results: Delayed but Equivalent Collapse}
26	
27	Exp\_016e exhibits the same qualitative failure mode as the unmodified control (exp\_008d): an initial learning phase followed by catastrophic performance collapse coinciding with NVE divergence.
28	
29	\paragraph{Evaluation trajectory.} Exp\_016e reaches a peak evaluation return of 326.7 at step 75K (exp\_016e), compared to 167.2 at step 25K for exp\_008d. Performance then collapses to 31.7 by step 95K (exp\_016e), a 90.3\% drop from peak. Exp\_008d follows a qualitatively similar trajectory: after peaking at 25K, evaluation declines steadily to 82.7 at 55K (exp\_008d).
30	
31	\paragraph{NVE trajectory.} The NVE for exp\_016e remains within the normal range ($0.8$--$1.9\times$) through step 85K, then spikes to $10.42\times$ at step 95K (exp\_016e)---well above the pathological threshold of $1.5\times$. Exp\_008d crosses the pathological threshold earlier: $\hat{r} = 1.71\times$ at 35K, rising to $4.12\times$ at 55K (exp\_008d).
32	
33	\paragraph{Interpretation of timing differences.} The delayed onset of CIVO in exp\_016e (85K vs.\ ${\sim}$25K in exp\_008d) and its higher peak evaluation (326.7 vs.\ 167.2) might suggest a partial protective effect of reward-pathway detachment. However, the gradient decomposition analysis below reveals that the intervention is an \textit{architectural no-op}, making any apparent differences attributable to seed variability rather than the SGS intervention. Both experiments use different random seeds in practice (exp\_016e: seed 1; exp\_008d: seed 1, but with different initialization order due to the code modification), and single-seed comparisons cannot distinguish intervention effects from stochastic variation in DreamerV3 training dynamics.
34	
35	\subsubsection{Gradient Decomposition: The Reward Pathway Carries Zero Gradient}
36	\label{sec:gradient_decomposition}
37	
38	To understand why the reward-only SGS had no effect, we performed a post-hoc gradient decomposition analysis (D061) using \texttt{torch.autograd.grad} to measure each loss component's contribution to $\nabla_{\theta} e_{\Delta t}$, where $\theta$ denotes the parameters of the temporal embedding layer (\texttt{dt\_emb.weight}).
39	
40	The decomposition reveals a striking asymmetry in gradient flow to the temporal embedding:
41	
42	\begin{table}[h]
43	\centering
44	\caption{Gradient contributions to $e_{\Delta t}$ parameters by loss component (D061 analysis). Gradient norms are measured at step 95K.}
45	\label{tab:gradient_decomposition}
46	\small
47	\begin{tabular}{lrr}
48	\toprule
49	Loss component & Gradient norm & Share (\%) \\
50	\midrule
51	Observation decoders (orientations, velocity, height) & 1.505 & 93 \\
52	KL dynamics & 0.119 & 7 \\
53	Continuation head & $<$0.001 & $<$1 \\
54	Reward head & 0.000 & 0 \\
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	The reward head contributes \textit{numerically negligible---zero to within floating-point precision} gradient to the temporal embedding parameters. This means exp\_016e's \texttt{reward\_dt\_emb\_detach} operation detaches a gradient that does not exist: it is an architectural no-op. The intervention's null effect is therefore expected---it removes nothing.
60	
61	\paragraph{Why is the reward gradient zero?} The reward head in DreamerV3 is a small MLP (typically 4 layers, 512 units) that maps from the same latent state as the observation decoders. The temporal embedding's influence on reward prediction flows through the RSSM's latent state, not through a direct connection to the reward head. In this architecture, the reward loss's gradient with respect to $e_{\Delta t}$ passes through the RSSM transition function---the same path as all other decoder losses. The observation decoders, with their substantially higher-dimensional output space (14 orientation dimensions + 9 velocity dimensions + 1 height dimension = 24 total, vs.\ 1 scalar reward), dominate the gradient signal by approximately two orders of magnitude. The reward head's gradient contribution is numerically negligible, effectively rounded to zero.
62	
63	\subsubsection{Implications for the CIVO Causal Chain}
64	
65	The gradient decomposition shifts the mechanistic picture of CIVO in an important direction.
66	
67	\paragraph{Observation decoders as the primary gradient source.} The temporal embedding's parameters are shaped overwhelmingly (93\%) by observation reconstruction gradients (D061). This means $e_{\Delta t}$ learns to encode whatever temporal information helps the observation decoders minimize reconstruction error. If this learned representation introduces systematic biases in latent state predictions at $\Delta t{>}1$---for instance, by encouraging the RSSM to produce states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. The CIVO mechanism thus originates not in the reward pathway, but in the observation reconstruction objective's influence on latent dynamics.
68	
69	\paragraph{KL dynamics as a secondary contributor.} The KL divergence loss contributes 7\% of the gradient to $e_{\Delta t}$ (D061). This loss regularizes the RSSM's prior and posterior distributions, and its gradient could either help or hinder temporal generalization. Its modest contribution suggests it plays a secondary role relative to the observation decoders.
70	
71	\paragraph{Reframing the intervention target.} The reward-only SGS targeted a gradient pathway that carries no signal. A meaningful gradient-level intervention must address the dominant 93\% contribution from observation decoders---and potentially the 7\% from KL dynamics. This motivates the \textit{full SGS} intervention (exp\_018, Section~\ref{sec:full_sgs}), which detaches $e_{\Delta t}$ from \textit{all} non-KL gradient pathways, removing the observation decoders' influence on the temporal embedding entirely.
72	
73	\subsubsection{Framing: Informative Negative, Not Failure}
74	
75	Exp\_016e did not achieve its intended effect, but it produced a finding more valuable than a positive result would have been. The gradient decomposition it motivated (D061) reveals that the temporal embedding's training signal is dominated by observation reconstruction---a structural fact about DreamerV3's loss landscape that was not \textit{a priori} obvious.
76	
77	This finding constrains the space of viable interventions. Any strategy that targets the reward head alone (e.g., reward prediction regularization, reward-conditioned value clipping) would address $<$1\% of the gradient flow to $e_{\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying the gradient flow (full SGS, exp\_018) or by restructuring how $e_{\Delta t}$ interacts with the RSSM transition function.
78	
79	The progression from exp\_016e's null result to the D061 gradient analysis to the full SGS design (exp\_018) exemplifies the diagnostic methodology's value: each experiment, whether it succeeds or fails at its immediate objective, narrows the causal hypothesis space and motivates a more targeted follow-up.
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "037435d9-1d1b-48e4-bb6e-3790e926c6d7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/sgs_informative_negative.md",
      "content": "% SGS Informative Negative — Draft v1\n% Target: CoRL 2026\n% Status: Draft, pending Director review\n% Depends on: experimental_setup.md (Section 4), method.md (Section 3)\n\n\\subsection{Stop-Gradient Surgery: An Informative Negative Result}\n\\label{sec:sgs_informative_negative}\n\nThe factorial analysis in Section~\\ref{sec:factorial} establishes that a trained temporal embedding ($e_{\\Delta t}$) is necessary for pathological value overestimation: conditions with removed or untrained embeddings do not exhibit CIVO (Section~\\ref{sec:civo_mechanism}). A natural follow-up question is \\textit{which gradient pathway} through $e_{\\Delta t}$ amplifies the overestimation. We hypothesized that the reward head---which directly supplies the critic's $\\lambda$-return targets---would be the primary amplifier: if reward predictions are systematically biased by $\\Delta t$ conditioning, the critic inherits and compounds these biases across the imagination horizon. This section reports a stop-gradient intervention designed to test this hypothesis, and the gradient decomposition analysis that revealed why the intervention had no effect.\n\n\\subsubsection{Hypothesis: Reward-Pathway Amplification}\n\nIn DreamerV3, the temporal embedding $e_{\\Delta t}$ is concatenated to the RSSM decoder input and conditions all prediction heads---observation decoders, reward head, and continuation predictor---simultaneously. The reward head's predictions enter the critic's $\\lambda$-return computation directly:\n$$G_t^\\lambda = r_t + \\gamma \\big[(1-\\lambda)\\,V(s_{t+1}) + \\lambda\\, G_{t+1}^\\lambda\\big]$$\nIf the reward head learns $\\Delta t$-dependent biases (e.g., systematically predicting higher rewards for $\\Delta t{=}2$ transitions), these biases accumulate across the $H$-step imagination rollout. We therefore conjectured that detaching $e_{\\Delta t}$ from the reward head's gradient computation would attenuate CIVO by preventing the reward predictor from specializing its parameters to the temporal embedding signal.\n\n\\subsubsection{Experiment: Reward-Only Stop-Gradient (exp\\_016e)}\n\nWe implemented a targeted stop-gradient intervention, termed \\textit{reward-only SGS} (Stop-Gradient Surgery), in which the temporal embedding is detached before entering the reward head during the backward pass:\n$$\\hat{r}_t = f_{\\text{reward}}\\big(\\text{sg}(e_{\\Delta t}),\\; h_t,\\; z_t\\big)$$\nwhere $\\text{sg}(\\cdot)$ denotes the stop-gradient operator. This prevents reward-loss gradients from updating $e_{\\Delta t}$'s parameters while preserving the embedding's forward-pass contribution to reward prediction. All other gradient pathways through $e_{\\Delta t}$---observation decoders, continuation predictor, KL dynamics loss---remain intact.\n\nThe experiment uses the same configuration as exp\\_008d (the primary CIVO-exhibiting condition): Walker Walk, trained $e_{\\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\\Delta t{=}2$ imagination, seed 1. The only modification is \\texttt{reward\\_dt\\_emb\\_detach=True}.\n\n\\subsubsection{Results: Delayed but Equivalent Collapse}\n\nExp\\_016e exhibits the same qualitative failure mode as the unmodified control (exp\\_008d): an initial learning phase followed by catastrophic performance collapse coinciding with NVE divergence.\n\n\\paragraph{Evaluation trajectory.} Exp\\_016e reaches a peak evaluation return of 326.7 at step 75K (exp\\_016e), compared to 167.2 at step 25K for exp\\_008d. Performance then collapses to 31.7 by step 95K (exp\\_016e), a 90.3\\% drop from peak. Exp\\_008d follows a qualitatively similar trajectory: after peaking at 25K, evaluation declines steadily to 82.7 at 55K (exp\\_008d).\n\n\\paragraph{NVE trajectory.} The NVE for exp\\_016e remains within the normal range ($0.8$--$1.9\\times$) through step 85K, then spikes to $10.42\\times$ at step 95K (exp\\_016e)---well above the pathological threshold of $1.5\\times$. Exp\\_008d crosses the pathological threshold earlier: $\\hat{r} = 1.71\\times$ at 35K, rising to $4.12\\times$ at 55K (exp\\_008d).\n\n\\paragraph{Interpretation of timing differences.} The delayed onset of CIVO in exp\\_016e (85K vs.\\ ${\\sim}$25K in exp\\_008d) and its higher peak evaluation (326.7 vs.\\ 167.2) might suggest a partial protective effect of reward-pathway detachment. However, the gradient decomposition analysis below reveals that the intervention is an \\textit{architectural no-op}, making any apparent differences attributable to seed variability rather than the SGS intervention. Both experiments use different random seeds in practice (exp\\_016e: seed 1; exp\\_008d: seed 1, but with different initialization order due to the code modification), and single-seed comparisons cannot distinguish intervention effects from stochastic variation in DreamerV3 training dynamics.\n\n\\subsubsection{Gradient Decomposition: The Reward Pathway Carries Zero Gradient}\n\\label{sec:gradient_decomposition}\n\nTo understand why the reward-only SGS had no effect, we performed a post-hoc gradient decomposition analysis (D061) using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_{\\theta} e_{\\Delta t}$, where $\\theta$ denotes the parameters of the temporal embedding layer (\\texttt{dt\\_emb.weight}).\n\nThe decomposition reveals a striking asymmetry in gradient flow to the temporal embedding:\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to $e_{\\Delta t}$ parameters by loss component (D061 analysis). Gradient norms are measured at step 95K.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\nLoss component & Gradient norm & Share (\\%) \\\\\n\\midrule\nObservation decoders (orientations, velocity, height) & 1.505 & 93 \\\\\nKL dynamics & 0.119 & 7 \\\\\nContinuation head & $<$0.001 & $<$1 \\\\\nReward head & 0.000 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reward head contributes \\textit{numerically negligible---zero to within floating-point precision} gradient to the temporal embedding parameters. This means exp\\_016e's \\texttt{reward\\_dt\\_emb\\_detach} operation detaches a gradient that does not exist: it is an architectural no-op. The intervention's null effect is therefore expected---it removes nothing.\n\n\\paragraph{Why is the reward gradient zero?} The reward head in DreamerV3 is a small MLP (typically 4 layers, 512 units) that maps from the same latent state as the observation decoders. The temporal embedding's influence on reward prediction flows through the RSSM's latent state, not through a direct connection to the reward head. In this architecture, the reward loss's gradient with respect to $e_{\\Delta t}$ passes through the RSSM transition function---the same path as all other decoder losses. The observation decoders, with their substantially higher-dimensional output space (14 orientation dimensions + 9 velocity dimensions + 1 height dimension = 24 total, vs.\\ 1 scalar reward), dominate the gradient signal by approximately two orders of magnitude. The reward head's gradient contribution is numerically negligible, effectively rounded to zero.\n\n\\subsubsection{Implications for the CIVO Causal Chain}\n\nThe gradient decomposition shifts the mechanistic picture of CIVO in an important direction.\n\n\\paragraph{Observation decoders as the primary gradient source.} The temporal embedding's parameters are shaped overwhelmingly (93\\%) by observation reconstruction gradients (D061). This means $e_{\\Delta t}$ learns to encode whatever temporal information helps the observation decoders minimize reconstruction error. If this learned representation introduces systematic biases in latent state predictions at $\\Delta t{>}1$---for instance, by encouraging the RSSM to produce states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. The CIVO mechanism thus originates not in the reward pathway, but in the observation reconstruction objective's influence on latent dynamics.\n\n\\paragraph{KL dynamics as a secondary contributor.} The KL divergence loss contributes 7\\% of the gradient to $e_{\\Delta t}$ (D061). This loss regularizes the RSSM's prior and posterior distributions, and its gradient could either help or hinder temporal generalization. Its modest contribution suggests it plays a secondary role relative to the observation decoders.\n\n\\paragraph{Reframing the intervention target.} The reward-only SGS targeted a gradient pathway that carries no signal. A meaningful gradient-level intervention must address the dominant 93\\% contribution from observation decoders---and potentially the 7\\% from KL dynamics. This motivates the \\textit{full SGS} intervention (exp\\_018, Section~\\ref{sec:full_sgs}), which detaches $e_{\\Delta t}$ from \\textit{all} non-KL gradient pathways, removing the observation decoders' influence on the temporal embedding entirely.\n\n\\subsubsection{Framing: Informative Negative, Not Failure}\n\nExp\\_016e did not achieve its intended effect, but it produced a finding more valuable than a positive result would have been. The gradient decomposition it motivated (D061) reveals that the temporal embedding's training signal is dominated by observation reconstruction---a structural fact about DreamerV3's loss landscape that was not \\textit{a priori} obvious.\n\nThis finding constrains the space of viable interventions. Any strategy that targets the reward head alone (e.g., reward prediction regularization, reward-conditioned value clipping) would address $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying the gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.\n\nThe progression from exp\\_016e's null result to the D061 gradient analysis to the full SGS design (exp\\_018) exemplifies the diagnostic methodology's value: each experiment, whether it succeeds or fails at its immediate objective, narrows the causal hypothesis space and motivates a more targeted follow-up.\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01ViN6QotBkHdHMbSpj3NoLK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_021_full_sgs_cheetah_s1/report/analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "ee25d93e-20ba-4761-a5e0-ecd8a5be5ae9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gn3Kiy1Ggu7kzyeNLf51dg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11976,
      "cache_read_input_tokens": 24488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11976
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

_source line 16 · 2026-05-17T23:43:00.802Z_

<details><summary>↩ Tool result · `toolu_01ViN6QotBkHdHMbSpj3NoLK`</summary>

````text
1	# exp_021_full_sgs_cheetah_s1 Analysis
2	
3	## Configuration
4	- Environment: Cheetah Run
5	- gate_enabled=True, gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8
6	- full_sgs=True (Stop-Gradient on all non-KL gradients from dt_emb)
7	- seed=1, 105K eval steps (training continued to ~112K)
8	
9	## Final Metrics
10	
11	| Metric | Value |
12	|--------|-------|
13	| eval_return_final | 221.5 |
14	| eval_return_peak | 221.5 (step 105K) |
15	| peak_step | 105000 |
16	| NVE_peak | 9.94 (step 45K) |
17	| NVE_peak_step | 45000 |
18	| NVE_sustained_avg (55K-105K) | 0.338 |
19	| civo | **True** (transient, self-correcting) |
20	| actor_grad_norm | 0.0-0.1 (very small under SGS) |
21	
22	## Eval Return Trajectory
23	
24	| Step | eval_return | value_mean | NVE (ve_ratio) |
25	|------|-------------|------------|----------------|
26	| 5K   | 13.5  | 0.0   | 0.000 |
27	| 15K  | 105.4 | 1.9   | 0.018 |
28	| 25K  | 85.0  | 15.0  | 0.177 |
29	| 35K  | 145.3 | 34.3  | 0.236 |
30	| 45K  | 4.6   | 45.6  | **9.94** |
31	| 55K  | 77.4  | 44.9  | 0.580 |
32	| 65K  | 85.2  | 40.1  | 0.470 |
33	| 75K  | 129.1 | 33.7  | 0.261 |
34	| 85K  | 108.7 | 28.3  | 0.261 |
35	| 95K  | 68.3  | 24.3  | 0.355 |
36	| 105K | 221.5 | 21.2  | 0.096 |
37	
38	## Key Observations
39	
40	1. **Transient CIVO at step 45K**: NVE spiked to 9.94 with eval_return collapsing to 4.6. Unlike 010b (permanent collapse), the agent recovered within ~10K steps.
41	
42	2. **Value_mean trajectory**: Rose to peak 45.6 at step 45K, then monotonically decreased to 21.2 at 105K. SGS appears to constrain value growth after the initial spike, but did NOT prevent it.
43	
44	3. **Post-recovery NVE is healthy**: After 55K, NVE sustained average = 0.338, well below 1.5x threshold. SGS maintains value discipline after the transient event.
45	
46	4. **Actor learning severely impaired**: actor_grad_norm = 0.0-0.1 throughout (vs typical 1-10 in non-SGS runs). Full SGS may be over-aggressive in blocking gradients.
47	
48	5. **Performance far below baseline**: 221.5 / 572.5 = **38.7% of baseline** (baselines: 023a=624.7, 023b=520.3, mean=572.5).
49	
50	## Comparison with 010b (Cheetah, no SGS, gate dt=2)
51	
52	| Metric | 010b (no SGS) | 021 (Full-SGS) |
53	|--------|---------------|-----------------|
54	| NVE_peak | 8.27 | 9.94 |
55	| eval_return_final | 51.7 | 221.5 |
56	| Collapse | Permanent | Transient (recovered) |
57	| civo | True | True |
58	
59	SGS did NOT prevent the CIVO spike, but enabled recovery. Final performance is 4.3x better than 010b but still 61% below baseline.
60	
61	## Comparison with 018 (Walker, Full-SGS)
62	
63	| Metric | 018 (Walker SGS) | 021 (Cheetah SGS) |
64	|--------|-------------------|---------------------|
65	| NVE_peak | 0.72 | 9.94 |
66	| NVE_sustained_avg | 0.55 | 0.338 |
67	| civo | False | True (transient) |
68	| Cross-env consistent | Yes (Walker) | **No** (Cheetah) |
69	
70	**Cross-environment consistency NOT confirmed.** SGS fully prevents CIVO in Walker but only partially mitigates it in Cheetah.
71	
72	## Conclusion: **PARTIAL NEGATIVE**
73	
74	- Full-SGS does NOT reliably prevent CIVO across environments
75	- In Cheetah, a transient CIVO event still occurs (NVE=9.94 at 45K)
76	- SGS enables recovery (unlike permanent collapse in 010b), suggesting partial protective effect
77	- However, performance remains far below baseline (38.7%), likely due to over-aggressive gradient blocking (actor_grad_norm near zero)
78	- The hypothesis that SGS eliminates NVE>1.5x is **rejected** for Cheetah
79	
80	## Suggested Registry Entry
81	
82	```python
83	{
84	    "exp_id": "exp_021_full_sgs_cheetah_s1",
85	    "env": "cheetah_run",
86	    "intervention": "full_sgs",
87	    "seed": 1,
88	    "steps": 105000,
89	    "metrics": {
90	        "eval_return_final": 221.5,
91	        "eval_return_peak": 221.5,
92	        "peak_step": 105000,
93	        "NVE_peak": 9.94,
94	        "NVE_peak_step": 45000,
95	        "NVE_sustained_avg": 0.338,
96	        "civo": True,
97	        "civo_type": "transient_recovered",
98	        "baseline_ratio": 0.387,
99	        "actor_grad_norm_range": [0.0, 0.1]
100	    },
101	    "conclusion": "partial_negative",
102	    "notes": "SGS enables recovery from CIVO (vs 010b permanent collapse) but does NOT prevent initial spike. Cross-env consistency with Walker NOT confirmed. Performance 38.7% of baseline."
103	}
104	```
105	
106	## Next Steps (Suggested)
107	
108	1. Investigate why CIVO still occurs under SGS in Cheetah but not Walker (environment-specific dynamics?)
109	2. Consider partial SGS or SGS with warmup to avoid over-blocking actor gradients
110	3. Run seed=0 variant to check if the transient CIVO at 45K is seed-dependent
111	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "d3450370-395a-4a79-a5a5-840c5147ac5a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_021_full_sgs_cheetah_s1/report/analysis.md",
      "content": "# exp_021_full_sgs_cheetah_s1 Analysis\n\n## Configuration\n- Environment: Cheetah Run\n- gate_enabled=True, gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8\n- full_sgs=True (Stop-Gradient on all non-KL gradients from dt_emb)\n- seed=1, 105K eval steps (training continued to ~112K)\n\n## Final Metrics\n\n| Metric | Value |\n|--------|-------|\n| eval_return_final | 221.5 |\n| eval_return_peak | 221.5 (step 105K) |\n| peak_step | 105000 |\n| NVE_peak | 9.94 (step 45K) |\n| NVE_peak_step | 45000 |\n| NVE_sustained_avg (55K-105K) | 0.338 |\n| civo | **True** (transient, self-correcting) |\n| actor_grad_norm | 0.0-0.1 (very small under SGS) |\n\n## Eval Return Trajectory\n\n| Step | eval_return | value_mean | NVE (ve_ratio) |\n|------|-------------|------------|----------------|\n| 5K   | 13.5  | 0.0   | 0.000 |\n| 15K  | 105.4 | 1.9   | 0.018 |\n| 25K  | 85.0  | 15.0  | 0.177 |\n| 35K  | 145.3 | 34.3  | 0.236 |\n| 45K  | 4.6   | 45.6  | **9.94** |\n| 55K  | 77.4  | 44.9  | 0.580 |\n| 65K  | 85.2  | 40.1  | 0.470 |\n| 75K  | 129.1 | 33.7  | 0.261 |\n| 85K  | 108.7 | 28.3  | 0.261 |\n| 95K  | 68.3  | 24.3  | 0.355 |\n| 105K | 221.5 | 21.2  | 0.096 |\n\n## Key Observations\n\n1. **Transient CIVO at step 45K**: NVE spiked to 9.94 with eval_return collapsing to 4.6. Unlike 010b (permanent collapse), the agent recovered within ~10K steps.\n\n2. **Value_mean trajectory**: Rose to peak 45.6 at step 45K, then monotonically decreased to 21.2 at 105K. SGS appears to constrain value growth after the initial spike, but did NOT prevent it.\n\n3. **Post-recovery NVE is healthy**: After 55K, NVE sustained average = 0.338, well below 1.5x threshold. SGS maintains value discipline after the transient event.\n\n4. **Actor learning severely impaired**: actor_grad_norm = 0.0-0.1 throughout (vs typical 1-10 in non-SGS runs). Full SGS may be over-aggressive in blocking gradients.\n\n5. **Performance far below baseline**: 221.5 / 572.5 = **38.7% of baseline** (baselines: 023a=624.7, 023b=520.3, mean=572.5).\n\n## Comparison with 010b (Cheetah, no SGS, gate dt=2)\n\n| Metric | 010b (no SGS) | 021 (Full-SGS) |\n|--------|---------------|-----------------|\n| NVE_peak | 8.27 | 9.94 |\n| eval_return_final | 51.7 | 221.5 |\n| Collapse | Permanent | Transient (recovered) |\n| civo | True | True |\n\nSGS did NOT prevent the CIVO spike, but enabled recovery. Final performance is 4.3x better than 010b but still 61% below baseline.\n\n## Comparison with 018 (Walker, Full-SGS)\n\n| Metric | 018 (Walker SGS) | 021 (Cheetah SGS) |\n|--------|-------------------|---------------------|\n| NVE_peak | 0.72 | 9.94 |\n| NVE_sustained_avg | 0.55 | 0.338 |\n| civo | False | True (transient) |\n| Cross-env consistent | Yes (Walker) | **No** (Cheetah) |\n\n**Cross-environment consistency NOT confirmed.** SGS fully prevents CIVO in Walker but only partially mitigates it in Cheetah.\n\n## Conclusion: **PARTIAL NEGATIVE**\n\n- Full-SGS does NOT reliably prevent CIVO across environments\n- In Cheetah, a transient CIVO event still occurs (NVE=9.94 at 45K)\n- SGS enables recovery (unlike permanent collapse in 010b), suggesting partial protective effect\n- However, performance remains far below baseline (38.7%), likely due to over-aggressive gradient blocking (actor_grad_norm near zero)\n- The hypothesis that SGS eliminates NVE>1.5x is **rejected** for Cheetah\n\n## Suggested Registry Entry\n\n```python\n{\n    \"exp_id\": \"exp_021_full_sgs_cheetah_s1\",\n    \"env\": \"cheetah_run\",\n    \"intervention\": \"full_sgs\",\n    \"seed\": 1,\n    \"steps\": 105000,\n    \"metrics\": {\n        \"eval_return_final\": 221.5,\n        \"eval_return_peak\": 221.5,\n        \"peak_step\": 105000,\n        \"NVE_peak\": 9.94,\n        \"NVE_peak_step\": 45000,\n        \"NVE_sustained_avg\": 0.338,\n        \"civo\": True,\n        \"civo_type\": \"transient_recovered\",\n        \"baseline_ratio\": 0.387,\n        \"actor_grad_norm_range\": [0.0, 0.1]\n    },\n    \"conclusion\": \"partial_negative\",\n    \"notes\": \"SGS enables recovery from CIVO (vs 010b permanent collapse) but does NOT prevent initial spike. Cross-env consistency with Walker NOT confirmed. Performance 38.7% of baseline.\"\n}\n```\n\n## Next Steps (Suggested)\n\n1. Investigate why CIVO still occurs under SGS in Cheetah but not Walker (environment-specific dynamics?)\n2. Consider partial SGS or SGS with warmup to avoid over-blocking actor gradients\n3. Run seed=0 variant to check if the transient CIVO at 45K is seed-dependent\n",
      "numLines": 111,
      "startLine": 1,
      "totalLines": 111
    }
  }
}
````

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

````text
Now let me check what's already in the appendix and the sgs_informative_negative.md file.

Key findings:

1. **appendix.tex (complete results table)**: exp_021 is already present at line 44:
   ```
   021 & Cheetah Run & trn+SGS & ON & 8 & 221.5 @105K & $<$1$\times$$^d$ & Recovery \\
   ```
   With footnote $^d$ at line 60 explaining the NVE details.
   
2. **sgs_informative_negative.md**: This file covers exp_016e (reward-only SGS) and the gradient decomposition, references exp_018 (full SGS), but doesn't mention exp_021 (Cheetah Full-SGS). The final section points to "full SGS design (exp\_018)" as the next step.

3. **exp_021 analysis report**: The detailed findings show that SGS enables recovery compared to the permanent collapse in exp_010b, though it doesn't eliminate the initial spike.

Now I need to check the appendix SGS section (\ref{sec:sgs_gradient_analysis}) to see what results are already discussed there.

Looking at lines 245-296, the appendix mentions exp_018 results showing seed 1 avoids collapse while seed 2 collapses, with a 50% prevention rate noted. But exp_021 isn't referenced. The text at line 284 frames this as "Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\Delta t}$, though its 50\% prevention rate (1/2 seeds) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability."

This framing needs updating based on exp_021's cross-environment findings—in Cheetah, SGS doesn't prevent the transient CIVO spike (NVE peaked at 9.94x) but does enable recovery afterward. So the narrative should shift from "50% prevention rate" to emphasizing that SGS enables recovery rather than preventing collapse entirely, which aligns with the D088 conclusion.

The table already shows exp_021 with "Recovery" marked, but the discussion text around lines 293-296 doesn't incorporate this evidence. I need to revise that section to include the cross-environment results and reframe what SGS actually accomplishes. The sustained NVE value in the table is correct—it's showing the average rather than the peak, which aligns with the footnote explaining the normalized baseline. Now I need to revise the SGS discussion in the appendix to incorporate exp_021 as evidence that SGS enables recovery across environments, and I should check whether the draft markdown file needs updating as well.

For the appendix edit around line 293, I'm planning to add exp_021 right after the exp_018 discussion to show that the cross-environment validation supports the recovery mechanism interpretation. I'll also review the sgs_informative_negative.md file to see if it needs a note about exp_021 given that it's a draft document. I'm locating the right section in the appendix to integrate this evidence—the SGS gradient analysis subsection around line 293 is where the reframing should go. I'll add the exp_021 data showing how Full-SGS allowed recovery in Cheetah Run despite the initial spike, shifting the narrative from prevention to enabling self-correction.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "86782750-b6ca-4d35-bcce-ed33b2350c96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QovcXpabPsJtiHD11sis3J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5239,
      "cache_read_input_tokens": 36464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5239
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

exp_021 is already in the complete results table (line 44) with correct data and footnote. The appendix SGS discussion section (lines 245-296) doesn't mention exp_021's cross-environment evidence though, and it needs to be updated to align with D088's "enables recovery" framing. Let me update that section and check the draft md file.

I'll add exp_021 cross-environment evidence to the SGS discussion paragraph:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "1618a14c-aa4c-47cb-98a7-59f989e66bed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QovcXpabPsJtiHD11sis3J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5239,
      "cache_read_input_tokens": 36464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5239
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

<details open><summary>🔧 Tool call — Edit · `toolu_01HV2W5zwmrvuLcmJuKsJ97u`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.",
  "new_string": "Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This pattern reframes Full-SGS as \\emph{enabling recovery from CIVO} rather than preventing its onset: the gradient detachment constrains value growth after the transient spike, allowing the critic to recalibrate.  Performance nonetheless remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's mixed Walker results (1/2 seeds), these findings indicate that gradient-level interventions alone do not fully eliminate the CIVO vulnerability, and that additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "a9549d67-8de1-4ca6-a80e-4530424f02e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QovcXpabPsJtiHD11sis3J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5239,
      "cache_read_input_tokens": 36464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5239
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

_source line 20 · 2026-05-17T23:43:52.709Z_

<details><summary>↩ Tool result · reported error · `toolu_01HV2W5zwmrvuLcmJuKsJ97u`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "6429e198-0d8e-4f16-946e-d262748700ab",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01Umh744vWpeBbu27jCYyBAB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 285,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "245d72bb-b5c4-4eae-9c6c-d2d4ba29b633",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJtDmA2TQAsVuPysT5GUmg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2372,
      "cache_read_input_tokens": 41703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2372
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

_source line 22 · 2026-05-17T23:43:55.570Z_

<details><summary>↩ Tool result · `toolu_01Umh744vWpeBbu27jCYyBAB`</summary>

```text
285	
286	\subsubsection{Implications for the CIVO Mechanism}
287	\label{sec:sgs_implications}
288	
289	The gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.
290	
291	\paragraph{Gradient importance $\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\%) to $e_{\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\dt$-specific structural information: it adjusts $e_{\Delta t}$ to minimize a scalar prediction error that is largely $\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\Delta t}$ learns scale-dependent latent biases.
292	
293	\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\_016e (NVE $10.42\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\_018) detaches $e_{\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.
294	
295	\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\_008d) shows a $2.78\times$ reward gap between $\Delta t{=}1$ and $\Delta t{=}2$ transitions (Table~\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\Delta t}$ to produce latent states that are spatially biased at $\dt{>}1$, and the reward head inherits these biases \textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\Delta t}$'s parameters but not causal responsibility for the fidelity gap.
296	
297	\subsubsection{Entropy Dynamics Across Configurations}
298	\label{sec:entropy_dynamics}
299	
300	\begin{figure}[h]
301	\centering
302	\includegraphics[width=0.85\columnwidth]{figures/fig4_entropy_dynamics.pdf}
303	\caption{Actor entropy trajectories for three configurations. All start at ${\sim}8$ nats and converge to similar values (${\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}
304	\label{fig:entropy_dynamics}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "4a9ce613-32e3-4fde-bac3-43a8aeb41fa5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}",
      "numLines": 20,
      "startLine": 285,
      "totalLines": 352
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01Y7YXCfEw6dMNjvDQ9f342F`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.",
  "new_string": "Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This pattern reframes Full-SGS as \\emph{enabling recovery from CIVO} rather than preventing its onset: the gradient detachment constrains value growth after the transient spike, allowing the critic to recalibrate.  Performance nonetheless remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's mixed Walker results (1/2 seeds), these findings indicate that gradient-level interventions alone do not fully eliminate the CIVO vulnerability, and that additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "bb3e30c3-0bd7-4dc0-810d-8a34c4556eed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VBjW3cpKGtDKnKLG7Nss4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 44075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 46,
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

_source line 24 · 2026-05-17T23:44:12.374Z_

<details><summary>↩ Tool result · `toolu_01Y7YXCfEw6dMNjvDQ9f342F`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "f6af61ab-453d-48b7-a754-874b90c8ce8c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.",
    "newString": "Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This pattern reframes Full-SGS as \\emph{enabling recovery from CIVO} rather than preventing its onset: the gradient detachment constrains value growth after the transient spike, allowing the critic to recalibrate.  Performance nonetheless remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's mixed Walker results (1/2 seeds), these findings indicate that gradient-level interventions alone do not fully eliminate the CIVO vulnerability, and that additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.",
    "originalFile": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 17 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3), SGS interventions (018), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & No collapse \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n021 & Cheetah Run & trn+SGS & ON & 8 & 221.5 @105K & $<$1$\\times$$^d$ & Recovery \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\ntrn+SGS = trained ($d{=}32$) with Full-SGS;\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Sustained NVE (55K--105K). Peak NVE $9.94\\times$ at 45K (transient CIVO onset, self-correcting); normalized against exp\\_023a/023b Cheetah baselines.\\par}\n\\end{table*}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eight factorial experiments. Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.84 & sustained CIVO & $+$ & $+$ \\\\\n008d         & 4.13 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 1.000$ because the minimum positive NVE ($4.13\\times$, exp~008d) exceeds the maximum negative NVE ($3.78\\times$, exp~008e\\_v3\\_s2), yielding perfect rank separation. The optimal threshold lies in the interval $(3.78, 4.13]$; we report $\\geq 3.9\\times$ as a representative value. Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.933$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=2$, $n_{\\text{neg}}=6$, $n=8$, $\\text{AUROC}=1.000$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). Thresholds 1.2$\\times$/1.5$\\times$ and 1.7$\\times$/2.0$\\times$ yield identical operating points (no NVE values in those intervals). $^\\dagger$Optimal threshold in $(3.78, 4.13]$.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 2 & 3 & 0 & 3 & 62.5\\% \\; [24.5, 91.5] & 40.0\\% & 100\\% & 57.1\\% \\\\\n$\\geq 1.2\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.5\\times$ & 2 & 2 & 0 & 4 & 75.0\\% \\; [34.9, 96.8] & 50.0\\% & 100\\% & 66.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 0 & 5 & 87.5\\% \\; [47.3, 99.7] & 66.7\\% & 100\\% & 80.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 2 & 0 & 0 & 6 & 100\\% \\; [63.1, 100] & 100\\% & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=5$, $n=8$, $\\text{AUROC}=0.933$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 2 & 0 & 3 & 75.0\\% \\; [34.9, 96.8] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 1.2\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 3 & 1 & 0 & 4 & 87.5\\% \\; [47.3, 99.7] & 75.0\\% & 100\\% & 85.7\\% \\\\\n$\\geq 1.7\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 2.0\\times$ & 2 & 1 & 1 & 4 & 75.0\\% \\; [34.9, 96.8] & 66.7\\% & 66.7\\% & 66.7\\% \\\\\n$\\geq 3.9\\times$ & 2 & 0 & 1 & 5 & 87.5\\% \\; [47.3, 99.7] & 100\\% & 66.7\\% & 80.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all three CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 66.7\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 85.7\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), perfect classification is achievable at $\\nve \\geq 3.9\\times$, but with only $n_{\\text{pos}} = 2$ the statistical power is severely limited (accuracy 95\\% CI: [63.1\\%, 100\\%]).\n\n\\paragraph{Limitations.} With $n = 8$ experiments, all Clopper-Pearson confidence intervals are wide (e.g., 87.5\\% accuracy has 95\\% CI [47.3\\%, 99.7\\%]). These results should be interpreted as a diagnostic proof-of-concept rather than a validated clinical threshold. Replication across additional environments and seeds is needed to establish tighter bounds.\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training, confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.55\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.60 \\rightarrow 0.59 \\rightarrow 0.55$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and triggers full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.55\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$, confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced: the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 50\\% prevention rate (1/2 seeds) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe two post-CIVO outcomes (Table~\\ref{tab:post_civo}), full collapse and transient CIVO with self-correction, both cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Bootstrap resampling ($B{=}10000$) over the $n{=}2$ effective seeds yields peak NVE mean $3.085$ (95\\% CI: $[2.05, 4.12]$), collapse rate $0.5$, and Cohen's $d = 2.60$ (mean difference $2.205$) relative to the no-embedding control, confirming a large effect despite the limited sample.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) avoids CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse mechanisms identified in \\S\\ref{sec:f6}, CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing), have distinct diagnostic signatures but a shared root cause: the trained $\\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.\n",
    "structuredPatch": [
      {
        "oldStart": 290,
        "oldLines": 8,
        "newStart": 290,
        "newLines": 10,
        "lines": [
          " ",
          " \\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.",
          " ",
          "-\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.  The 50\\% prevention rate suggests that CIVO involves additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) beyond those capturable by gradient-level interventions alone.",
          "+\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention yields mixed results: seed~1 avoids collapse (eval 448.3) while seed~2 collapses (eval 40.8), indicating that removing the observation decoder gradient channel is necessary but not sufficient.",
          " ",
          "+Cross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This pattern reframes Full-SGS as \\emph{enabling recovery from CIVO} rather than preventing its onset: the gradient detachment constrains value growth after the transient spike, allowing the critic to recalibrate.  Performance nonetheless remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's mixed Walker results (1/2 seeds), these findings indicate that gradient-level interventions alone do not fully eliminate the CIVO vulnerability, and that additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.",
          "+",
          " \\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.",
          " ",
          " \\subsubsection{Entropy Dynamics Across Configurations}"
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

_source line 25_

Now update the `sgs_informative_negative.md` draft to reference exp_021:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "85f01ca6-e432-447d-90ff-6613dae36a02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XeafTjQH8B9Aai74x5DCXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 45214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 746
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

<details open><summary>🔧 Tool call — Edit · `toolu_01AoZDQXSLLtrTzuLNK8Ej8g`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/sgs_informative_negative.md",
  "old_string": "The progression from exp\\_016e's null result to the D061 gradient analysis to the full SGS design (exp\\_018) exemplifies the diagnostic methodology's value: each experiment, whether it succeeds or fails at its immediate objective, narrows the causal hypothesis space and motivates a more targeted follow-up.",
  "new_string": "The progression from exp\\_016e's null result to the D061 gradient analysis to the full SGS design (exp\\_018) exemplifies the diagnostic methodology's value: each experiment, whether it succeeds or fails at its immediate objective, narrows the causal hypothesis space and motivates a more targeted follow-up.\n\n\\subsubsection{Cross-Environment Validation: Full-SGS on Cheetah Run (exp\\_021)}\n\\label{sec:sgs_cheetah}\n\nExp\\_021 applies Full-SGS to Cheetah Run, where exp\\_010b exhibited permanent CIVO collapse (NVE $8.27\\times$, eval 51.7). Full-SGS did not prevent the initial CIVO spike (NVE $9.94\\times$ at 45K), but the agent self-corrected within ${\\sim}$10K steps: sustained NVE dropped to $0.34\\times$ (55K--105K) and final evaluation recovered to 221.5 (vs.\\ 010b's permanent collapse to 51.7). This reframes Full-SGS as \\emph{enabling recovery} rather than preventing collapse (D088). Performance remains at 38.7\\% of Cheetah baselines (mean 572.5), with actor gradient norms near zero throughout, suggesting over-aggressive gradient blocking impairs actor learning even when CIVO is controlled."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "ac258f9d-d042-45e7-ac58-f360d26acdc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XeafTjQH8B9Aai74x5DCXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 45214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 746
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

_source line 27 · 2026-05-17T23:44:24.276Z_

<details><summary>↩ Tool result · `toolu_01AoZDQXSLLtrTzuLNK8Ej8g`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/sgs_informative_negative.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "2778da60-3e37-4e24-aa89-65cb099f20e6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/sections/sgs_informative_negative.md",
    "oldString": "The progression from exp\\_016e's null result to the D061 gradient analysis to the full SGS design (exp\\_018) exemplifies the diagnostic methodology's value: each experiment, whether it succeeds or fails at its immediate objective, narrows the causal hypothesis space and motivates a more targeted follow-up.",
    "newString": "The progression from exp\\_016e's null result to the D061 gradient analysis to the full SGS design (exp\\_018) exemplifies the diagnostic methodology's value: each experiment, whether it succeeds or fails at its immediate objective, narrows the causal hypothesis space and motivates a more targeted follow-up.\n\n\\subsubsection{Cross-Environment Validation: Full-SGS on Cheetah Run (exp\\_021)}\n\\label{sec:sgs_cheetah}\n\nExp\\_021 applies Full-SGS to Cheetah Run, where exp\\_010b exhibited permanent CIVO collapse (NVE $8.27\\times$, eval 51.7). Full-SGS did not prevent the initial CIVO spike (NVE $9.94\\times$ at 45K), but the agent self-corrected within ${\\sim}$10K steps: sustained NVE dropped to $0.34\\times$ (55K--105K) and final evaluation recovered to 221.5 (vs.\\ 010b's permanent collapse to 51.7). This reframes Full-SGS as \\emph{enabling recovery} rather than preventing collapse (D088). Performance remains at 38.7\\% of Cheetah baselines (mean 572.5), with actor gradient norms near zero throughout, suggesting over-aggressive gradient blocking impairs actor learning even when CIVO is controlled.",
    "originalFile": "% SGS Informative Negative — Draft v1\n% Target: CoRL 2026\n% Status: Draft, pending Director review\n% Depends on: experimental_setup.md (Section 4), method.md (Section 3)\n\n\\subsection{Stop-Gradient Surgery: An Informative Negative Result}\n\\label{sec:sgs_informative_negative}\n\nThe factorial analysis in Section~\\ref{sec:factorial} establishes that a trained temporal embedding ($e_{\\Delta t}$) is necessary for pathological value overestimation: conditions with removed or untrained embeddings do not exhibit CIVO (Section~\\ref{sec:civo_mechanism}). A natural follow-up question is \\textit{which gradient pathway} through $e_{\\Delta t}$ amplifies the overestimation. We hypothesized that the reward head---which directly supplies the critic's $\\lambda$-return targets---would be the primary amplifier: if reward predictions are systematically biased by $\\Delta t$ conditioning, the critic inherits and compounds these biases across the imagination horizon. This section reports a stop-gradient intervention designed to test this hypothesis, and the gradient decomposition analysis that revealed why the intervention had no effect.\n\n\\subsubsection{Hypothesis: Reward-Pathway Amplification}\n\nIn DreamerV3, the temporal embedding $e_{\\Delta t}$ is concatenated to the RSSM decoder input and conditions all prediction heads---observation decoders, reward head, and continuation predictor---simultaneously. The reward head's predictions enter the critic's $\\lambda$-return computation directly:\n$$G_t^\\lambda = r_t + \\gamma \\big[(1-\\lambda)\\,V(s_{t+1}) + \\lambda\\, G_{t+1}^\\lambda\\big]$$\nIf the reward head learns $\\Delta t$-dependent biases (e.g., systematically predicting higher rewards for $\\Delta t{=}2$ transitions), these biases accumulate across the $H$-step imagination rollout. We therefore conjectured that detaching $e_{\\Delta t}$ from the reward head's gradient computation would attenuate CIVO by preventing the reward predictor from specializing its parameters to the temporal embedding signal.\n\n\\subsubsection{Experiment: Reward-Only Stop-Gradient (exp\\_016e)}\n\nWe implemented a targeted stop-gradient intervention, termed \\textit{reward-only SGS} (Stop-Gradient Surgery), in which the temporal embedding is detached before entering the reward head during the backward pass:\n$$\\hat{r}_t = f_{\\text{reward}}\\big(\\text{sg}(e_{\\Delta t}),\\; h_t,\\; z_t\\big)$$\nwhere $\\text{sg}(\\cdot)$ denotes the stop-gradient operator. This prevents reward-loss gradients from updating $e_{\\Delta t}$'s parameters while preserving the embedding's forward-pass contribution to reward prediction. All other gradient pathways through $e_{\\Delta t}$---observation decoders, continuation predictor, KL dynamics loss---remain intact.\n\nThe experiment uses the same configuration as exp\\_008d (the primary CIVO-exhibiting condition): Walker Walk, trained $e_{\\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\\Delta t{=}2$ imagination, seed 1. The only modification is \\texttt{reward\\_dt\\_emb\\_detach=True}.\n\n\\subsubsection{Results: Delayed but Equivalent Collapse}\n\nExp\\_016e exhibits the same qualitative failure mode as the unmodified control (exp\\_008d): an initial learning phase followed by catastrophic performance collapse coinciding with NVE divergence.\n\n\\paragraph{Evaluation trajectory.} Exp\\_016e reaches a peak evaluation return of 326.7 at step 75K (exp\\_016e), compared to 167.2 at step 25K for exp\\_008d. Performance then collapses to 31.7 by step 95K (exp\\_016e), a 90.3\\% drop from peak. Exp\\_008d follows a qualitatively similar trajectory: after peaking at 25K, evaluation declines steadily to 82.7 at 55K (exp\\_008d).\n\n\\paragraph{NVE trajectory.} The NVE for exp\\_016e remains within the normal range ($0.8$--$1.9\\times$) through step 85K, then spikes to $10.42\\times$ at step 95K (exp\\_016e)---well above the pathological threshold of $1.5\\times$. Exp\\_008d crosses the pathological threshold earlier: $\\hat{r} = 1.71\\times$ at 35K, rising to $4.12\\times$ at 55K (exp\\_008d).\n\n\\paragraph{Interpretation of timing differences.} The delayed onset of CIVO in exp\\_016e (85K vs.\\ ${\\sim}$25K in exp\\_008d) and its higher peak evaluation (326.7 vs.\\ 167.2) might suggest a partial protective effect of reward-pathway detachment. However, the gradient decomposition analysis below reveals that the intervention is an \\textit{architectural no-op}, making any apparent differences attributable to seed variability rather than the SGS intervention. Both experiments use different random seeds in practice (exp\\_016e: seed 1; exp\\_008d: seed 1, but with different initialization order due to the code modification), and single-seed comparisons cannot distinguish intervention effects from stochastic variation in DreamerV3 training dynamics.\n\n\\subsubsection{Gradient Decomposition: The Reward Pathway Carries Zero Gradient}\n\\label{sec:gradient_decomposition}\n\nTo understand why the reward-only SGS had no effect, we performed a post-hoc gradient decomposition analysis (D061) using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_{\\theta} e_{\\Delta t}$, where $\\theta$ denotes the parameters of the temporal embedding layer (\\texttt{dt\\_emb.weight}).\n\nThe decomposition reveals a striking asymmetry in gradient flow to the temporal embedding:\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to $e_{\\Delta t}$ parameters by loss component (D061 analysis). Gradient norms are measured at step 95K.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\nLoss component & Gradient norm & Share (\\%) \\\\\n\\midrule\nObservation decoders (orientations, velocity, height) & 1.505 & 93 \\\\\nKL dynamics & 0.119 & 7 \\\\\nContinuation head & $<$0.001 & $<$1 \\\\\nReward head & 0.000 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reward head contributes \\textit{numerically negligible---zero to within floating-point precision} gradient to the temporal embedding parameters. This means exp\\_016e's \\texttt{reward\\_dt\\_emb\\_detach} operation detaches a gradient that does not exist: it is an architectural no-op. The intervention's null effect is therefore expected---it removes nothing.\n\n\\paragraph{Why is the reward gradient zero?} The reward head in DreamerV3 is a small MLP (typically 4 layers, 512 units) that maps from the same latent state as the observation decoders. The temporal embedding's influence on reward prediction flows through the RSSM's latent state, not through a direct connection to the reward head. In this architecture, the reward loss's gradient with respect to $e_{\\Delta t}$ passes through the RSSM transition function---the same path as all other decoder losses. The observation decoders, with their substantially higher-dimensional output space (14 orientation dimensions + 9 velocity dimensions + 1 height dimension = 24 total, vs.\\ 1 scalar reward), dominate the gradient signal by approximately two orders of magnitude. The reward head's gradient contribution is numerically negligible, effectively rounded to zero.\n\n\\subsubsection{Implications for the CIVO Causal Chain}\n\nThe gradient decomposition shifts the mechanistic picture of CIVO in an important direction.\n\n\\paragraph{Observation decoders as the primary gradient source.} The temporal embedding's parameters are shaped overwhelmingly (93\\%) by observation reconstruction gradients (D061). This means $e_{\\Delta t}$ learns to encode whatever temporal information helps the observation decoders minimize reconstruction error. If this learned representation introduces systematic biases in latent state predictions at $\\Delta t{>}1$---for instance, by encouraging the RSSM to produce states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. The CIVO mechanism thus originates not in the reward pathway, but in the observation reconstruction objective's influence on latent dynamics.\n\n\\paragraph{KL dynamics as a secondary contributor.} The KL divergence loss contributes 7\\% of the gradient to $e_{\\Delta t}$ (D061). This loss regularizes the RSSM's prior and posterior distributions, and its gradient could either help or hinder temporal generalization. Its modest contribution suggests it plays a secondary role relative to the observation decoders.\n\n\\paragraph{Reframing the intervention target.} The reward-only SGS targeted a gradient pathway that carries no signal. A meaningful gradient-level intervention must address the dominant 93\\% contribution from observation decoders---and potentially the 7\\% from KL dynamics. This motivates the \\textit{full SGS} intervention (exp\\_018, Section~\\ref{sec:full_sgs}), which detaches $e_{\\Delta t}$ from \\textit{all} non-KL gradient pathways, removing the observation decoders' influence on the temporal embedding entirely.\n\n\\subsubsection{Framing: Informative Negative, Not Failure}\n\nExp\\_016e did not achieve its intended effect, but it produced a finding more valuable than a positive result would have been. The gradient decomposition it motivated (D061) reveals that the temporal embedding's training signal is dominated by observation reconstruction---a structural fact about DreamerV3's loss landscape that was not \\textit{a priori} obvious.\n\nThis finding constrains the space of viable interventions. Any strategy that targets the reward head alone (e.g., reward prediction regularization, reward-conditioned value clipping) would address $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying the gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.\n\nThe progression from exp\\_016e's null result to the D061 gradient analysis to the full SGS design (exp\\_018) exemplifies the diagnostic methodology's value: each experiment, whether it succeeds or fails at its immediate objective, narrows the causal hypothesis space and motivates a more targeted follow-up.\n",
    "structuredPatch": [
      {
        "oldStart": 77,
        "oldLines": 3,
        "newStart": 77,
        "newLines": 8,
        "lines": [
          " This finding constrains the space of viable interventions. Any strategy that targets the reward head alone (e.g., reward prediction regularization, reward-conditioned value clipping) would address $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying the gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.",
          " ",
          " The progression from exp\\_016e's null result to the D061 gradient analysis to the full SGS design (exp\\_018) exemplifies the diagnostic methodology's value: each experiment, whether it succeeds or fails at its immediate objective, narrows the causal hypothesis space and motivates a more targeted follow-up.",
          "+",
          "+\\subsubsection{Cross-Environment Validation: Full-SGS on Cheetah Run (exp\\_021)}",
          "+\\label{sec:sgs_cheetah}",
          "+",
          "+Exp\\_021 applies Full-SGS to Cheetah Run, where exp\\_010b exhibited permanent CIVO collapse (NVE $8.27\\times$, eval 51.7). Full-SGS did not prevent the initial CIVO spike (NVE $9.94\\times$ at 45K), but the agent self-corrected within ${\\sim}$10K steps: sustained NVE dropped to $0.34\\times$ (55K--105K) and final evaluation recovered to 221.5 (vs.\\ 010b's permanent collapse to 51.7). This reframes Full-SGS as \\emph{enabling recovery} rather than preventing collapse (D088). Performance remains at 38.7\\% of Cheetah baselines (mean 572.5), with actor gradient norms near zero throughout, suggesting over-aggressive gradient blocking impairs actor learning even when CIVO is controlled."
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

_source line 28_

修改了两个文件：

1. **`docs/paper/sections/appendix.tex`** (line ~293): 在 "Reframing the intervention target" 段落中，exp_018 讨论之后新增一段 exp_021 的跨环境验证证据。核心内容：Full-SGS 在 Cheetah 上未阻止 CIVO 初始 spike (NVE 9.94x at 45K)，但使 agent 在 ~10K steps 内自修复（sustained NVE 0.34x, eval 221.5 vs 010b 的 51.7），将 SGS 重新定性为 "enables recovery" 而非 "prevents collapse"。

2. **`paper/sections/sgs_informative_negative.md`**: 末尾新增 `\subsubsection{Cross-Environment Validation: Full-SGS on Cheetah Run (exp\_021)}`，总结 021 结果并引用 D088 结论。

完整实验表中 exp_021 行已存在（line 44: `221.5 @105K, Recovery`），无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "uuid": "2b3456f0-abd0-42d8-b5bb-4ea15c09a5a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5Q1Ve96ZCcwBupiCFaQj3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 45960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
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

_source line 29_

修改了两个文件：

1. **`docs/paper/sections/appendix.tex`** (line ~293): 在 "Reframing the intervention target" 段落中，exp_018 讨论之后新增一段 exp_021 的跨环境验证证据。核心内容：Full-SGS 在 Cheetah 上未阻止 CIVO 初始 spike (NVE 9.94x at 45K)，但使 agent 在 ~10K steps 内自修复（sustained NVE 0.34x, eval 221.5 vs 010b 的 51.7），将 SGS 重新定性为 "enables recovery" 而非 "prevents collapse"。

2. **`paper/sections/sgs_informative_negative.md`**: 末尾新增 `\subsubsection{Cross-Environment Validation: Full-SGS on Cheetah Run (exp\_021)}`，总结 021 结果并引用 D088 结论。

完整实验表中 exp_021 行已存在（line 44: `221.5 @105K, Recovery`），无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 112298,
  "duration_api_ms": 113192,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "1362769a-1b89-4b3c-9f13-f6235b8be9a9",
  "total_cost_usd": 0.46342475,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 35133,
    "cache_read_input_tokens": 249351,
    "output_tokens": 4712,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35133,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 304,
        "cache_read_input_tokens": 45960,
        "cache_creation_input_tokens": 620,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 620
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1233,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001323,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 4712,
      "cacheReadInputTokens": 249351,
      "cacheCreationInputTokens": 35133,
      "webSearchRequests": 0,
      "costUSD": 0.46210175000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f5fc31c4-3767-4c9b-a4a7-0612662a9f7a"
}
```

</details>

---
