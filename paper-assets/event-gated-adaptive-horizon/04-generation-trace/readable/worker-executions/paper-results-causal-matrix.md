# paper results causal matrix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_results-causal-matrix_20260516T075402.log`
- **Structured JSON:** [`e5829295f50071098c25.json`](../../sessions/e5/e5829295f50071098c25.json)

## Before a recorded user message

13 recorded events

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
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
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
  "uuid": "2865104d-b2e6-49ab-9532-2da872b4451b",
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
    "resetsAt": 1778924400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4e87649b-f57e-4778-8597-62d30afe6a3c",
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the results.tex file to find the correct locations for both insertions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
  "uuid": "d8dcdcc9-c687-46e0-81f7-fce7ff68ebdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGYtW4MZm2De2GB2g1F2er",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11895,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11895
      },
      "output_tokens": 32,
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

<details open><summary>🔧 Tool call — Read · `toolu_01L7swruH3aEQfeb2CMsYuYz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
  "uuid": "a497499b-1b2a-40e2-8ce4-3fac866e5574",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGYtW4MZm2De2GB2g1F2er",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11895,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11895
      },
      "output_tokens": 32,
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

_source line 6 · 2026-05-16T07:54:15.945Z_

<details><summary>↩ Tool result · `toolu_01L7swruH3aEQfeb2CMsYuYz`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{All configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	\rowcolor{gray!15}
22	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
23	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
24	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
25	\midrule
26	\rowcolor{gray!15}
27	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
28	\rowcolor{gray!15}
29	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
30	\rowcolor{gray!15}
31	009e & Factorial (s1) & trn & ON & 8 & 131.1 @105K & 4.12$\times$ & Oscillatory \\
32	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
33	009c & No dt\_emb (s2) & --- & ON & 8 & 148.3 @105K & 1.14$\times$ & Declining \\
34	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
35	008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\times$ & Slow learner \\
36	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\times$ & Grad.\ starvation \\
37	\midrule
38	008e\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\times$ & Healthy \\
39	008e\_v3 s2$^\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\times$ & Non-CIVO collapse \\
40	009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\
41	\bottomrule
42	\end{tabular}
43	\vspace{1pt}
44	{\raggedright\footnotesize
45	trn = trained ($d{=}32$, exposed to $\dt{>}1$ data via subsample ON);
46	exp$^a$ = trained ($d{=}32$) but never exposed to $\dt{>}1$ data (subsample OFF);
47	frz$^b$ = frozen random projection ($d{=}32$, \texttt{requires\_grad=False});
48	--- = removed ($d{=}0$).\par}
49	\end{table*}
50	
51	%% ============================================================
52	%% F1: All dt>1 degrade
53	%% ============================================================
54	
55	\subsection{F1: All Variable-Rate Configurations Degrade}
56	\label{sec:f1}
57	
58	Every configuration that introduces $\dt > 1$ imagination degrades relative to the $\dt{=}1$ baseline, regardless of mechanism (Figure~\ref{fig:learning_curves}). The baseline (exp\_001) reaches 915.7 at 105K steps and peaks at 970.4 at 505K. In contrast, fixed $\dt{=}2$ (exp\_006) peaks at 485.3 at 35K before collapsing to 132.9 by 65K---a $-73\%$ decline from its own peak (14\% of baseline). Fixed $\dt{=}4$ (exp\_007) peaks at only 176.9 at 25K and never exceeds 152.5 thereafter. The learned-gate configuration (exp\_005) peaks at 541.2 at 55K but collapses to 98.8 by 145K. This uniform degradation motivates the factorial analysis that follows.
59	
60	\begin{figure}[t]
61	\centering
62	\includegraphics[width=\columnwidth]{figures/paper/fig1_learning_curves.pdf}
63	\caption{Learning curves for all configurations. The $\dt{=}1$ baseline (black) reaches 915.7 at 105K; all variable-rate configurations degrade, with fixed $\dt{=}4$ and the learned gate collapsing most severely.}
64	\label{fig:learning_curves}
65	\end{figure}
66	
67	%% ============================================================
68	%% F2: Trained dt_embedding → nve > 1.5x
69	%% ============================================================
70	
71	\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}
72	\label{sec:f2}
73	
74	The factorial design isolates trained $\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\_008d (trained $\dt$-embedding, subsampling ON, $H{=}8$) against exp\_008f (identical configuration but \emph{no} trained $\dt$-embedding). As shown in Figure~\ref{fig:nve_trajectory}:
75	
76	\begin{itemize}[nosep,leftmargin=*]
77	\item \textbf{008d} (trained): $\nve = 1.78\times$ at 25K $\rightarrow$ $4.12\times$ at 55K $\rightarrow$ collapse (eval 167$\rightarrow$82.8).
78	\item \textbf{008f} (no dt\_emb): $\nve = 1.02\times$ at 25K $\rightarrow$ $0.30\times$ at 105K $\rightarrow$ no collapse (eval 503.0 at 105K).
79	\end{itemize}
80	
81	In the 35K+ window (\S\ref{sec:metrics}), the $\nve \geq 1.5\times$ threshold correctly classifies 7/8 seeds (AUROC${=}0.933$, Clopper--Pearson 95\% CI $[0.47, 1.0]$): 3 CIVO-positive (exp\_006, 008d, 009b) and 4 CIVO-negative, with one non-CIVO false positive (008e\_v3 s2, $3.78\times$; \S\ref{sec:f6}).  The gap between the lowest true positive ($1.62\times$) and the highest true negative ($1.00\times$) is $0.62$.
82	
83	\begin{figure}[t]
84	\centering
85	\includegraphics[width=\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}
86	\caption{Normalized value-to-eval ratio ($\nve$) trajectories. The dashed line marks the $1.5\times$ threshold. All trained-embedding configurations with $\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\_v3 s1, dash-dot) with $\dt{=}1$-only imagination remains below it.}
87	\label{fig:nve_trajectory}
88	\end{figure}
89	
90	\paragraph{Three post-CIVO outcomes.}
91	Running the 008d configuration with two independent seeds (s1, s2) reveals that trained $\dt$-embedding triggers CIVO---yet the downstream consequence is stochastic. Exp\_009e extends seed~1 (008d) beyond 55K to 105K steps:
92	
93	%% ============================================================
94	%% TABLE 3: Three post-CIVO outcomes
95	%% ============================================================
96	
97	\begin{table}[t]
98	\centering
99	\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window. Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K.}
100	\label{tab:post_civo}
101	\footnotesize
102	\setlength{\tabcolsep}{3pt}
103	\begin{tabular}{lcccl}
104	\toprule
105	\textbf{Seed} & \textbf{Peak} & \textbf{Final} & \textbf{Eval} & \textbf{Outcome} \\
106	\midrule
107	s1 (008d) & 4.12$\times$ & 4.12$\times$ & 82.8 & Full collapse \\
108	s2 (009b) & 1.62$\times$ & 0.38$\times$ & 267.9 & Transient CIVO \\
109	s1 ext (009e) & 4.12$\times$ & 1.57$\times$ & 131.1 & Oscillatory \\
110	\bottomrule
111	\end{tabular}
112	\end{table}
113	
114	\noindent\textbf{Seed 1 (008d):} Full collapse (Pathway A). Value explosion ($+130\%$), evaluation declines from 167 to 82.8, entropy decreases---the classic CIVO feedback loop.
115	
116	\noindent\textbf{Seed 2 (009b):} Transient CIVO. The $\nve$ reaches $1.62\times$ at 45K (35K+ window), exceeding the $1.5\times$ threshold, but the value function self-corrects to $0.38\times$ by 105K, and evaluation recovers to 267.9. This demonstrates the threshold's sensitivity to early CIVO signals even in cases that spontaneously recover.
117	
118	\noindent\textbf{Seed 1 extended (009e):} Oscillatory degradation. Continuing 008d beyond 55K, evaluation oscillates between 82.7 and 250 before settling at 131.1; the value function rises then reverses (peak $\nve = 4.12\times$ at 55K, final $1.57\times$).
119	
120	All runs exceed $\nve \geq 1.5\times$ in the 35K+ window, confirming deterministic CIVO triggering, but downstream outcomes are seed-dependent (1/2 persistent collapse rate among independent seeds).
121	
122	%% ============================================================
123	%% F3: Unexposed dt_embedding suppresses value drift
124	%% ============================================================
125	
126	\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}
127	\label{sec:f3}
128	
129	\begin{figure}[t]
130	\centering
131	\includegraphics[width=\columnwidth]{figures/paper/fig3_factorial_grid.pdf}
132	\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}
133	\label{fig:factorial_grid}
134	\end{figure}
135	
136	Exp\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\_008d, its NVE remains in the $0.59$--$0.93\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\dt{>}1$ state predictions within the RSSM.
137	
138	This contrasts with exp\_006 (trained $e_{\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\times$ at 45K to $2.31\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.
139	
140	The frozen embedding (exp\_015b, $d{=}32$, \texttt{requires\_grad=False}, subsample ON) provides additional causal evidence: despite full exposure to multi-rate data, its NVE remains at $0.39$--$0.47\times$ and never triggers CIVO, instead failing through gradient starvation (actor loss $\to$ 0; see \S\ref{sec:failure_taxonomy}). This confirms that trainability of the embedding is also necessary---a frozen random projection cannot co-adapt with RSSM dynamics to produce the systematic bias that drives CIVO.
141	
142	%% ============================================================
143	%% F4: dt=2 > dt=4 monotonic degradation
144	%% ============================================================
145	
146	\subsection{F4: Degradation Scales Monotonically with \texorpdfstring{$\dt$}{dt}}
147	\label{sec:f4}
148	
149	\begin{figure}[t]
150	\centering
151	\includegraphics[width=\columnwidth]{figures/paper/fig5_dt_amplification.pdf}
152	\caption{Peak evaluation return as a function of imagination $\dt$. Performance degrades monotonically: $\dt{=}1$ (915.7) $>$ $\dt{=}2$ (485.3, $-47\%$) $>$ $\dt{=}4$ (176.9, $-81\%$).}
153	\label{fig:dt_amplification}
154	\end{figure}
155	
156	The magnitude of degradation scales monotonically with the imagination step size (Figure~\ref{fig:dt_amplification}). From the $\dt{=}1$ baseline (915.7 at 105K), fixed $\dt{=}2$ (exp\_006) achieves a peak of only 485.3 ($-47\%$), and fixed $\dt{=}4$ (exp\_007) peaks at 176.9 ($-81\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.
157	
158	%% ============================================================
159	%% F5: Horizon and subsample secondary
160	%% ============================================================
161	
162	\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}
163	\label{sec:f5}
164	
165	Neither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\nve < 0.93\times$ (\S\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\nve = 4.12\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\ 009c: 148.3) but neither exhibits $\nve > 1.5\times$---confirming that low evaluation alone does not indicate CIVO.
166	
167	%% ============================================================
168	%% F6: dt=1 imagination does not prevent collapse
169	%% ============================================================
170	
171	\subsection{F6: Restricting Imagination to \texorpdfstring{$\dt{=}1$}{dt=1} Does Not Prevent Collapse}
172	\label{sec:f6}
173	
174	\begin{figure}[t]
175	\centering
176	\includegraphics[width=\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}
177	\caption{Contrasting collapse dynamics. \textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \textbf{Right:} 008e\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}
178	\label{fig:multiple_pathways}
179	\end{figure}
180	
181	The mitigation experiment exp\_008e\_v3 restricts imagination to $\dt{=}1$ while retaining the trained $\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:
182	
183	\begin{itemize}[nosep,leftmargin=*]
184	\item \textbf{Seed 1} (008e\_v3\_s1): Healthy. Eval 869.9 at 105K ($95\%$ of baseline), $\nve = 0.80\times$.
185	\item \textbf{Seed 2} (008e\_v3\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\nve = 3.78\times$.
186	\end{itemize}
187	
188	The baseline with seed 2 (exp\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.
189	
190	\paragraph{Distinct collapse mechanisms.}
191	The collapse dynamics of 008e\_v3\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\ref{tab:main_results}, Figure~\ref{fig:multiple_pathways}):
192	
193	\begin{itemize}[nosep,leftmargin=*]
194	\item \textbf{008d (CIVO, Pathway A):} value explosion ($+130\%$) $\rightarrow$ evaluation decline $\rightarrow$ entropy decreases.
195	\item \textbf{008e\_v3\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\%$) $\rightarrow$ value remains stable $\rightarrow$ entropy \emph{increases} ($-5.21 \rightarrow -3.83$).
196	\end{itemize}
197	
198	In Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\dt{=}1$ prevents the CIVO mechanism---no early $\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.
199	
200	This case also produces the sole false positive in the $\nve \geq 1.5\times$ classification: 008e\_v3\_s2's late evaluation decline inflates $\nve$ to $3.78\times$ through a non-CIVO mechanism (\S\ref{sec:pathways}).
201	
202	%% ============================================================
203	%% TABLE 2: RSSM Fidelity
204	%% ============================================================
205	
206	\begin{table}[t]
207	\centering
208	\caption{RSSM fidelity at $\dt{=}1$ vs.\ $\dt{=}2$. Trained embedding (008d) produces $2.78\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}
209	\label{tab:rssm_fidelity}
210	\footnotesize
211	\setlength{\tabcolsep}{4pt}
212	\begin{tabular}{lcccccc}
213	\toprule
214	& \multicolumn{3}{c}{\textbf{obs\_MSE}} & \multicolumn{3}{c}{\textbf{reward\_MAE}} \\
215	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
216	\textbf{Config} & $\dt{=}1$ & $\dt{=}2$ & Gap & $\dt{=}1$ & $\dt{=}2$ & Gap \\
217	\midrule
218	Baseline & 13.49 & 27.50 & 2.04$\times$ & 0.0102 & 0.0159 & 1.56$\times$ \\
219	008d (trained) & 41.31 & 53.67 & 1.30$\times$ & 0.0568 & 0.1579 & 2.78$\times$ \\
220	008f (no emb) & 8.01 & 22.04 & 2.75$\times$ & 0.7469 & 0.7526 & 1.01$\times$ \\
221	\bottomrule
222	\end{tabular}
223	\end{table}
224	
225	\paragraph{RSSM fidelity analysis.}
226	Table~\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\dt$-embedding in 008d produces a $2.78\times$ gap in reward prediction error between $\dt{=}1$ and $\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\ $0.0568$ for 008d at $\dt{=}1$).
227	
228	\paragraph{Summary.}
229	F1--F5 establish the combination of trained $\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\dt$.  F6 shows that restricting imagination to $\dt{=}1$ prevents CIVO but not all collapse modes: $\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.
230	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
  "uuid": "cfb2918a-841c-4c84-9d94-77a7ecd884c8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n009e & Factorial (s1) & trn & ON & 8 & 131.1 @105K & 4.12$\\times$ & Oscillatory \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n009c & No dt\\_emb (s2) & --- & ON & 8 & 148.3 @105K & 1.14$\\times$ & Declining \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\\times$ & Slow learner \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline, regardless of mechanism (Figure~\\ref{fig:learning_curves}). The baseline (exp\\_001) reaches 915.7 at 105K steps and peaks at 970.4 at 505K. In contrast, fixed $\\dt{=}2$ (exp\\_006) peaks at 485.3 at 35K before collapsing to 132.9 by 65K---a $-73\\%$ decline from its own peak (14\\% of baseline). Fixed $\\dt{=}4$ (exp\\_007) peaks at only 176.9 at 25K and never exceeds 152.5 thereafter. The learned-gate configuration (exp\\_005) peaks at 541.2 at 55K but collapses to 98.8 by 145K. This uniform degradation motivates the factorial analysis that follows.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves for all configurations. The $\\dt{=}1$ baseline (black) reaches 915.7 at 105K; all variable-rate configurations degrade, with fixed $\\dt{=}4$ and the learned gate collapsing most severely.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\\_008d (trained $\\dt$-embedding, subsampling ON, $H{=}8$) against exp\\_008f (identical configuration but \\emph{no} trained $\\dt$-embedding). As shown in Figure~\\ref{fig:nve_trajectory}:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d} (trained): $\\nve = 1.78\\times$ at 25K $\\rightarrow$ $4.12\\times$ at 55K $\\rightarrow$ collapse (eval 167$\\rightarrow$82.8).\n\\item \\textbf{008f} (no dt\\_emb): $\\nve = 1.02\\times$ at 25K $\\rightarrow$ $0.30\\times$ at 105K $\\rightarrow$ no collapse (eval 503.0 at 105K).\n\\end{itemize}\n\nIn the 35K+ window (\\S\\ref{sec:metrics}), the $\\nve \\geq 1.5\\times$ threshold correctly classifies 7/8 seeds (AUROC${=}0.933$, Clopper--Pearson 95\\% CI $[0.47, 1.0]$): 3 CIVO-positive (exp\\_006, 008d, 009b) and 4 CIVO-negative, with one non-CIVO false positive (008e\\_v3 s2, $3.78\\times$; \\S\\ref{sec:f6}).  The gap between the lowest true positive ($1.62\\times$) and the highest true negative ($1.00\\times$) is $0.62$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}\n\\caption{Normalized value-to-eval ratio ($\\nve$) trajectories. The dashed line marks the $1.5\\times$ threshold. All trained-embedding configurations with $\\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\\_v3 s1, dash-dot) with $\\dt{=}1$-only imagination remains below it.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\n\\paragraph{Three post-CIVO outcomes.}\nRunning the 008d configuration with two independent seeds (s1, s2) reveals that trained $\\dt$-embedding triggers CIVO---yet the downstream consequence is stochastic. Exp\\_009e extends seed~1 (008d) beyond 55K to 105K steps:\n\n%% ============================================================\n%% TABLE 3: Three post-CIVO outcomes\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window. Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\ns1 ext (009e) & 4.12$\\times$ & 1.57$\\times$ & 131.1 & Oscillatory \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Seed 1 (008d):} Full collapse (Pathway A). Value explosion ($+130\\%$), evaluation declines from 167 to 82.8, entropy decreases---the classic CIVO feedback loop.\n\n\\noindent\\textbf{Seed 2 (009b):} Transient CIVO. The $\\nve$ reaches $1.62\\times$ at 45K (35K+ window), exceeding the $1.5\\times$ threshold, but the value function self-corrects to $0.38\\times$ by 105K, and evaluation recovers to 267.9. This demonstrates the threshold's sensitivity to early CIVO signals even in cases that spontaneously recover.\n\n\\noindent\\textbf{Seed 1 extended (009e):} Oscillatory degradation. Continuing 008d beyond 55K, evaluation oscillates between 82.7 and 250 before settling at 131.1; the value function rises then reverses (peak $\\nve = 4.12\\times$ at 55K, final $1.57\\times$).\n\nAll runs exceed $\\nve \\geq 1.5\\times$ in the 35K+ window, confirming deterministic CIVO triggering, but downstream outcomes are seed-dependent (1/2 persistent collapse rate among independent seeds).\n\n%% ============================================================\n%% F3: Unexposed dt_embedding suppresses value drift\n%% ============================================================\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\nThe frozen embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}, subsample ON) provides additional causal evidence: despite full exposure to multi-rate data, its NVE remains at $0.39$--$0.47\\times$ and never triggers CIVO, instead failing through gradient starvation (actor loss $\\to$ 0; see \\S\\ref{sec:failure_taxonomy}). This confirms that trainability of the embedding is also necessary---a frozen random projection cannot co-adapt with RSSM dynamics to produce the systematic bias that drives CIVO.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n%% ============================================================\n%% F5: Horizon and subsample secondary\n%% ============================================================\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\n%% ============================================================\n%% F6: dt=1 imagination does not prevent collapse\n%% ============================================================\n\n\\subsection{F6: Restricting Imagination to \\texorpdfstring{$\\dt{=}1$}{dt=1} Does Not Prevent Collapse}\n\\label{sec:f6}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \\textbf{Right:} 008e\\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \\emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\nThe mitigation experiment exp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained $\\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Seed 1} (008e\\_v3\\_s1): Healthy. Eval 869.9 at 105K ($95\\%$ of baseline), $\\nve = 0.80\\times$.\n\\item \\textbf{Seed 2} (008e\\_v3\\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\\nve = 3.78\\times$.\n\\end{itemize}\n\nThe baseline with seed 2 (exp\\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.\n\n\\paragraph{Distinct collapse mechanisms.}\nThe collapse dynamics of 008e\\_v3\\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\\ref{tab:main_results}, Figure~\\ref{fig:multiple_pathways}):\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d (CIVO, Pathway A):} value explosion ($+130\\%$) $\\rightarrow$ evaluation decline $\\rightarrow$ entropy decreases.\n\\item \\textbf{008e\\_v3\\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\\%$) $\\rightarrow$ value remains stable $\\rightarrow$ entropy \\emph{increases} ($-5.21 \\rightarrow -3.83$).\n\\end{itemize}\n\nIn Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\\dt{=}1$ prevents the CIVO mechanism---no early $\\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.\n\nThis case also produces the sole false positive in the $\\nve \\geq 1.5\\times$ classification: 008e\\_v3\\_s2's late evaluation decline inflates $\\nve$ to $3.78\\times$ through a non-CIVO mechanism (\\S\\ref{sec:pathways}).\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RSSM fidelity analysis.}\nTable~\\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\\dt$-embedding in 008d produces a $2.78\\times$ gap in reward prediction error between $\\dt{=}1$ and $\\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\\ $0.0568$ for 008d at $\\dt{=}1$).\n\n\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.\n",
      "numLines": 230,
      "startLine": 1,
      "totalLines": 230
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

Now I can see the file. I need to:
1. Insert the causal matrix table after line 140 (end of F3 section, before F4 comment block)
2. Add the quantitative comparison in F5 section

Let me make both edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
  "uuid": "8095e044-e00a-4086-9c17-80a4712163e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUq7LD7DChHsNtXisgL28q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6450,
      "cache_read_input_tokens": 23342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6450
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

_source line 8_

<details open><summary>🔧 Tool call — Edit · `toolu_014jzAFAr6gtw6TwtvGLeuxn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "The frozen embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}, subsample ON) provides additional causal evidence: despite full exposure to multi-rate data, its NVE remains at $0.39$--$0.47\\times$ and never triggers CIVO, instead failing through gradient starvation (actor loss $\\to$ 0; see \\S\\ref{sec:failure_taxonomy}). This confirms that trainability of the embedding is also necessary---a frozen random projection cannot co-adapt with RSSM dynamics to produce the systematic bias that drives CIVO.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================",
  "new_string": "The frozen embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}, subsample ON) provides additional causal evidence: despite full exposure to multi-rate data, its NVE remains at $0.39$--$0.47\\times$ and never triggers CIVO, instead failing through gradient starvation (actor loss $\\to$ 0; see \\S\\ref{sec:failure_taxonomy}). This confirms that trainability of the embedding is also necessary---a frozen random projection cannot co-adapt with RSSM dynamics to produce the systematic bias that drives CIVO.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 2.09$\\times$, collapse & NVE 0.59--0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.39--0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
  "uuid": "059567d6-9ed4-4772-9db2-a9dd4727cc1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUq7LD7DChHsNtXisgL28q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6450,
      "cache_read_input_tokens": 23342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6450
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

_source line 9 · 2026-05-16T07:54:31.204Z_

<details><summary>↩ Tool result · `toolu_014jzAFAr6gtw6TwtvGLeuxn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
  "uuid": "0e851826-d3c3-4b5c-b246-aa59a6a9a846",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "The frozen embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}, subsample ON) provides additional causal evidence: despite full exposure to multi-rate data, its NVE remains at $0.39$--$0.47\\times$ and never triggers CIVO, instead failing through gradient starvation (actor loss $\\to$ 0; see \\S\\ref{sec:failure_taxonomy}). This confirms that trainability of the embedding is also necessary---a frozen random projection cannot co-adapt with RSSM dynamics to produce the systematic bias that drives CIVO.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================",
    "newString": "The frozen embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}, subsample ON) provides additional causal evidence: despite full exposure to multi-rate data, its NVE remains at $0.39$--$0.47\\times$ and never triggers CIVO, instead failing through gradient starvation (actor loss $\\to$ 0; see \\S\\ref{sec:failure_taxonomy}). This confirms that trainability of the embedding is also necessary---a frozen random projection cannot co-adapt with RSSM dynamics to produce the systematic bias that drives CIVO.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 2.09$\\times$, collapse & NVE 0.59--0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.39--0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n009e & Factorial (s1) & trn & ON & 8 & 131.1 @105K & 4.12$\\times$ & Oscillatory \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n009c & No dt\\_emb (s2) & --- & ON & 8 & 148.3 @105K & 1.14$\\times$ & Declining \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\\times$ & Slow learner \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline, regardless of mechanism (Figure~\\ref{fig:learning_curves}). The baseline (exp\\_001) reaches 915.7 at 105K steps and peaks at 970.4 at 505K. In contrast, fixed $\\dt{=}2$ (exp\\_006) peaks at 485.3 at 35K before collapsing to 132.9 by 65K---a $-73\\%$ decline from its own peak (14\\% of baseline). Fixed $\\dt{=}4$ (exp\\_007) peaks at only 176.9 at 25K and never exceeds 152.5 thereafter. The learned-gate configuration (exp\\_005) peaks at 541.2 at 55K but collapses to 98.8 by 145K. This uniform degradation motivates the factorial analysis that follows.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves for all configurations. The $\\dt{=}1$ baseline (black) reaches 915.7 at 105K; all variable-rate configurations degrade, with fixed $\\dt{=}4$ and the learned gate collapsing most severely.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\\_008d (trained $\\dt$-embedding, subsampling ON, $H{=}8$) against exp\\_008f (identical configuration but \\emph{no} trained $\\dt$-embedding). As shown in Figure~\\ref{fig:nve_trajectory}:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d} (trained): $\\nve = 1.78\\times$ at 25K $\\rightarrow$ $4.12\\times$ at 55K $\\rightarrow$ collapse (eval 167$\\rightarrow$82.8).\n\\item \\textbf{008f} (no dt\\_emb): $\\nve = 1.02\\times$ at 25K $\\rightarrow$ $0.30\\times$ at 105K $\\rightarrow$ no collapse (eval 503.0 at 105K).\n\\end{itemize}\n\nIn the 35K+ window (\\S\\ref{sec:metrics}), the $\\nve \\geq 1.5\\times$ threshold correctly classifies 7/8 seeds (AUROC${=}0.933$, Clopper--Pearson 95\\% CI $[0.47, 1.0]$): 3 CIVO-positive (exp\\_006, 008d, 009b) and 4 CIVO-negative, with one non-CIVO false positive (008e\\_v3 s2, $3.78\\times$; \\S\\ref{sec:f6}).  The gap between the lowest true positive ($1.62\\times$) and the highest true negative ($1.00\\times$) is $0.62$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}\n\\caption{Normalized value-to-eval ratio ($\\nve$) trajectories. The dashed line marks the $1.5\\times$ threshold. All trained-embedding configurations with $\\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\\_v3 s1, dash-dot) with $\\dt{=}1$-only imagination remains below it.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\n\\paragraph{Three post-CIVO outcomes.}\nRunning the 008d configuration with two independent seeds (s1, s2) reveals that trained $\\dt$-embedding triggers CIVO---yet the downstream consequence is stochastic. Exp\\_009e extends seed~1 (008d) beyond 55K to 105K steps:\n\n%% ============================================================\n%% TABLE 3: Three post-CIVO outcomes\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window. Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\ns1 ext (009e) & 4.12$\\times$ & 1.57$\\times$ & 131.1 & Oscillatory \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Seed 1 (008d):} Full collapse (Pathway A). Value explosion ($+130\\%$), evaluation declines from 167 to 82.8, entropy decreases---the classic CIVO feedback loop.\n\n\\noindent\\textbf{Seed 2 (009b):} Transient CIVO. The $\\nve$ reaches $1.62\\times$ at 45K (35K+ window), exceeding the $1.5\\times$ threshold, but the value function self-corrects to $0.38\\times$ by 105K, and evaluation recovers to 267.9. This demonstrates the threshold's sensitivity to early CIVO signals even in cases that spontaneously recover.\n\n\\noindent\\textbf{Seed 1 extended (009e):} Oscillatory degradation. Continuing 008d beyond 55K, evaluation oscillates between 82.7 and 250 before settling at 131.1; the value function rises then reverses (peak $\\nve = 4.12\\times$ at 55K, final $1.57\\times$).\n\nAll runs exceed $\\nve \\geq 1.5\\times$ in the 35K+ window, confirming deterministic CIVO triggering, but downstream outcomes are seed-dependent (1/2 persistent collapse rate among independent seeds).\n\n%% ============================================================\n%% F3: Unexposed dt_embedding suppresses value drift\n%% ============================================================\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\nThe frozen embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}, subsample ON) provides additional causal evidence: despite full exposure to multi-rate data, its NVE remains at $0.39$--$0.47\\times$ and never triggers CIVO, instead failing through gradient starvation (actor loss $\\to$ 0; see \\S\\ref{sec:failure_taxonomy}). This confirms that trainability of the embedding is also necessary---a frozen random projection cannot co-adapt with RSSM dynamics to produce the systematic bias that drives CIVO.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n%% ============================================================\n%% F5: Horizon and subsample secondary\n%% ============================================================\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\n%% ============================================================\n%% F6: dt=1 imagination does not prevent collapse\n%% ============================================================\n\n\\subsection{F6: Restricting Imagination to \\texorpdfstring{$\\dt{=}1$}{dt=1} Does Not Prevent Collapse}\n\\label{sec:f6}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \\textbf{Right:} 008e\\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \\emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\nThe mitigation experiment exp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained $\\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Seed 1} (008e\\_v3\\_s1): Healthy. Eval 869.9 at 105K ($95\\%$ of baseline), $\\nve = 0.80\\times$.\n\\item \\textbf{Seed 2} (008e\\_v3\\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\\nve = 3.78\\times$.\n\\end{itemize}\n\nThe baseline with seed 2 (exp\\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.\n\n\\paragraph{Distinct collapse mechanisms.}\nThe collapse dynamics of 008e\\_v3\\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\\ref{tab:main_results}, Figure~\\ref{fig:multiple_pathways}):\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d (CIVO, Pathway A):} value explosion ($+130\\%$) $\\rightarrow$ evaluation decline $\\rightarrow$ entropy decreases.\n\\item \\textbf{008e\\_v3\\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\\%$) $\\rightarrow$ value remains stable $\\rightarrow$ entropy \\emph{increases} ($-5.21 \\rightarrow -3.83$).\n\\end{itemize}\n\nIn Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\\dt{=}1$ prevents the CIVO mechanism---no early $\\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.\n\nThis case also produces the sole false positive in the $\\nve \\geq 1.5\\times$ classification: 008e\\_v3\\_s2's late evaluation decline inflates $\\nve$ to $3.78\\times$ through a non-CIVO mechanism (\\S\\ref{sec:pathways}).\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RSSM fidelity analysis.}\nTable~\\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\\dt$-embedding in 008d produces a $2.78\\times$ gap in reward prediction error between $\\dt{=}1$ and $\\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\\ $0.0568$ for 008d at $\\dt{=}1$).\n\n\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.\n",
    "structuredPatch": [
      {
        "oldStart": 139,
        "oldLines": 6,
        "newStart": 139,
        "newLines": 29,
        "lines": [
          " ",
          " The frozen embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}, subsample ON) provides additional causal evidence: despite full exposure to multi-rate data, its NVE remains at $0.39$--$0.47\\times$ and never triggers CIVO, instead failing through gradient starvation (actor loss $\\to$ 0; see \\S\\ref{sec:failure_taxonomy}). This confirms that trainability of the embedding is also necessary---a frozen random projection cannot co-adapt with RSSM dynamics to produce the systematic bias that drives CIVO.",
          " ",
          "+\\begin{table}[h]",
          "+\\centering",
          "+\\small",
          "+\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}",
          "+\\label{tab:causal_matrix}",
          "+\\begin{tabular}{lcc}",
          "+\\toprule",
          "+& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\",
          "+\\midrule",
          "+Trained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\",
          "+ & NVE 2.09$\\times$, collapse & NVE 0.59--0.93$\\times$ \\\\",
          "+\\midrule",
          "+Frozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\",
          "+ & NVE 0.39--0.47$\\times$ & \\\\",
          "+\\midrule",
          "+Removed $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\",
          "+ & NVE $\\leq$0.97$\\times$ & \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          "+Only the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.",
          "+",
          " %% ============================================================",
          " %% F4: dt=2 > dt=4 monotonic degradation",
          " %% ============================================================"
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

_source line 10_

<details open><summary>🔧 Tool call — Edit · `toolu_01QZiQQd1DKocwFAP8ph9Z3m`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "Neither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.",
  "new_string": "Neither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
  "uuid": "5978991a-3434-4237-bad6-53397805b979",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUq7LD7DChHsNtXisgL28q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6450,
      "cache_read_input_tokens": 23342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6450
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

_source line 11 · 2026-05-16T07:54:35.685Z_

<details><summary>↩ Tool result · `toolu_01QZiQQd1DKocwFAP8ph9Z3m`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
  "uuid": "cb58073c-47ae-4f7b-93a1-2bcbaa92152f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "Neither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.",
    "newString": "Neither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n009e & Factorial (s1) & trn & ON & 8 & 131.1 @105K & 4.12$\\times$ & Oscillatory \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n009c & No dt\\_emb (s2) & --- & ON & 8 & 148.3 @105K & 1.14$\\times$ & Declining \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\\times$ & Slow learner \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline, regardless of mechanism (Figure~\\ref{fig:learning_curves}). The baseline (exp\\_001) reaches 915.7 at 105K steps and peaks at 970.4 at 505K. In contrast, fixed $\\dt{=}2$ (exp\\_006) peaks at 485.3 at 35K before collapsing to 132.9 by 65K---a $-73\\%$ decline from its own peak (14\\% of baseline). Fixed $\\dt{=}4$ (exp\\_007) peaks at only 176.9 at 25K and never exceeds 152.5 thereafter. The learned-gate configuration (exp\\_005) peaks at 541.2 at 55K but collapses to 98.8 by 145K. This uniform degradation motivates the factorial analysis that follows.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves for all configurations. The $\\dt{=}1$ baseline (black) reaches 915.7 at 105K; all variable-rate configurations degrade, with fixed $\\dt{=}4$ and the learned gate collapsing most severely.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\\_008d (trained $\\dt$-embedding, subsampling ON, $H{=}8$) against exp\\_008f (identical configuration but \\emph{no} trained $\\dt$-embedding). As shown in Figure~\\ref{fig:nve_trajectory}:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d} (trained): $\\nve = 1.78\\times$ at 25K $\\rightarrow$ $4.12\\times$ at 55K $\\rightarrow$ collapse (eval 167$\\rightarrow$82.8).\n\\item \\textbf{008f} (no dt\\_emb): $\\nve = 1.02\\times$ at 25K $\\rightarrow$ $0.30\\times$ at 105K $\\rightarrow$ no collapse (eval 503.0 at 105K).\n\\end{itemize}\n\nIn the 35K+ window (\\S\\ref{sec:metrics}), the $\\nve \\geq 1.5\\times$ threshold correctly classifies 7/8 seeds (AUROC${=}0.933$, Clopper--Pearson 95\\% CI $[0.47, 1.0]$): 3 CIVO-positive (exp\\_006, 008d, 009b) and 4 CIVO-negative, with one non-CIVO false positive (008e\\_v3 s2, $3.78\\times$; \\S\\ref{sec:f6}).  The gap between the lowest true positive ($1.62\\times$) and the highest true negative ($1.00\\times$) is $0.62$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}\n\\caption{Normalized value-to-eval ratio ($\\nve$) trajectories. The dashed line marks the $1.5\\times$ threshold. All trained-embedding configurations with $\\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\\_v3 s1, dash-dot) with $\\dt{=}1$-only imagination remains below it.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\n\\paragraph{Three post-CIVO outcomes.}\nRunning the 008d configuration with two independent seeds (s1, s2) reveals that trained $\\dt$-embedding triggers CIVO---yet the downstream consequence is stochastic. Exp\\_009e extends seed~1 (008d) beyond 55K to 105K steps:\n\n%% ============================================================\n%% TABLE 3: Three post-CIVO outcomes\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window. Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\ns1 ext (009e) & 4.12$\\times$ & 1.57$\\times$ & 131.1 & Oscillatory \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Seed 1 (008d):} Full collapse (Pathway A). Value explosion ($+130\\%$), evaluation declines from 167 to 82.8, entropy decreases---the classic CIVO feedback loop.\n\n\\noindent\\textbf{Seed 2 (009b):} Transient CIVO. The $\\nve$ reaches $1.62\\times$ at 45K (35K+ window), exceeding the $1.5\\times$ threshold, but the value function self-corrects to $0.38\\times$ by 105K, and evaluation recovers to 267.9. This demonstrates the threshold's sensitivity to early CIVO signals even in cases that spontaneously recover.\n\n\\noindent\\textbf{Seed 1 extended (009e):} Oscillatory degradation. Continuing 008d beyond 55K, evaluation oscillates between 82.7 and 250 before settling at 131.1; the value function rises then reverses (peak $\\nve = 4.12\\times$ at 55K, final $1.57\\times$).\n\nAll runs exceed $\\nve \\geq 1.5\\times$ in the 35K+ window, confirming deterministic CIVO triggering, but downstream outcomes are seed-dependent (1/2 persistent collapse rate among independent seeds).\n\n%% ============================================================\n%% F3: Unexposed dt_embedding suppresses value drift\n%% ============================================================\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\nThe frozen embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}, subsample ON) provides additional causal evidence: despite full exposure to multi-rate data, its NVE remains at $0.39$--$0.47\\times$ and never triggers CIVO, instead failing through gradient starvation (actor loss $\\to$ 0; see \\S\\ref{sec:failure_taxonomy}). This confirms that trainability of the embedding is also necessary---a frozen random projection cannot co-adapt with RSSM dynamics to produce the systematic bias that drives CIVO.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 2.09$\\times$, collapse & NVE 0.59--0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.39--0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n%% ============================================================\n%% F5: Horizon and subsample secondary\n%% ============================================================\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\n%% ============================================================\n%% F6: dt=1 imagination does not prevent collapse\n%% ============================================================\n\n\\subsection{F6: Restricting Imagination to \\texorpdfstring{$\\dt{=}1$}{dt=1} Does Not Prevent Collapse}\n\\label{sec:f6}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \\textbf{Right:} 008e\\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \\emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\nThe mitigation experiment exp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained $\\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Seed 1} (008e\\_v3\\_s1): Healthy. Eval 869.9 at 105K ($95\\%$ of baseline), $\\nve = 0.80\\times$.\n\\item \\textbf{Seed 2} (008e\\_v3\\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\\nve = 3.78\\times$.\n\\end{itemize}\n\nThe baseline with seed 2 (exp\\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.\n\n\\paragraph{Distinct collapse mechanisms.}\nThe collapse dynamics of 008e\\_v3\\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\\ref{tab:main_results}, Figure~\\ref{fig:multiple_pathways}):\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d (CIVO, Pathway A):} value explosion ($+130\\%$) $\\rightarrow$ evaluation decline $\\rightarrow$ entropy decreases.\n\\item \\textbf{008e\\_v3\\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\\%$) $\\rightarrow$ value remains stable $\\rightarrow$ entropy \\emph{increases} ($-5.21 \\rightarrow -3.83$).\n\\end{itemize}\n\nIn Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\\dt{=}1$ prevents the CIVO mechanism---no early $\\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.\n\nThis case also produces the sole false positive in the $\\nve \\geq 1.5\\times$ classification: 008e\\_v3\\_s2's late evaluation decline inflates $\\nve$ to $3.78\\times$ through a non-CIVO mechanism (\\S\\ref{sec:pathways}).\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RSSM fidelity analysis.}\nTable~\\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\\dt$-embedding in 008d produces a $2.78\\times$ gap in reward prediction error between $\\dt{=}1$ and $\\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\\ $0.0568$ for 008d at $\\dt{=}1$).\n\n\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.\n",
    "structuredPatch": [
      {
        "oldStart": 187,
        "oldLines": 6,
        "newStart": 187,
        "newLines": 8,
        "lines": [
          " ",
          " Neither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.",
          " ",
          "+The $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).",
          "+",
          " %% ============================================================",
          " %% F6: dt=1 imagination does not prevent collapse",
          " %% ============================================================"
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

_source line 12_

两处编辑完成：
1. F3 末尾插入了 `tab:causal_matrix` 表格及因果结论总结句
2. F5 段落末尾添加了 008a vs 008c 的 $3.2\times$ 定量对比句

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
  "uuid": "0c3519ba-41b2-4f17-980e-ca3a585b779c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXCcBAmpsSkTu1YtCdP8Zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 29792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1557
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

_source line 13_

两处编辑完成：
1. F3 末尾插入了 `tab:causal_matrix` 表格及因果结论总结句
2. F5 段落末尾添加了 008a vs 008c 的 $3.2\times$ 定量对比句

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 27364,
  "duration_api_ms": 28371,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "3f00ec96-b931-45cf-a528-1039c764051b",
  "total_cost_usd": 0.19750500000000001,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 19902,
    "cache_read_input_tokens": 64581,
    "output_tokens": 1574,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 19902,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 80,
        "cache_read_input_tokens": 29792,
        "cache_creation_input_tokens": 1557,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1557
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1347,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0014520000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 1574,
      "cacheReadInputTokens": 64581,
      "cacheCreationInputTokens": 19902,
      "webSearchRequests": 0,
      "costUSD": 0.196053,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7b11a6ff-4b91-4143-9896-0778d23bf3a3"
}
```

</details>

---
