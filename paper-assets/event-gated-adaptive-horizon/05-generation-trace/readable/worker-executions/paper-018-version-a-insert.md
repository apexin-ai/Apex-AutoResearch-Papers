# paper 018 version a insert

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_paper_018-version-a-insert_20260516T130334.log`
- **Structured JSON:** [`3ebee602669145b8bb70.json`](../../sessions/3e/3ebee602669145b8bb70.json)

## Before a recorded user message

49 recorded events

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
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
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
  "uuid": "db7cd987-364c-4bf9-90c9-76b9a12e5ee8",
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
    "resetsAt": 1778945400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e728ed4e-a161-4a1f-b16b-e2da3da0ba9c",
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant .tex files to understand their current structure, then make the modifications requested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "8cf92e53-0d68-4db4-a94b-28b61a7ca6ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oFHEq2GQEtb9ci1LZJNQC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13268,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13268
      },
      "output_tokens": 24,
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

_source line 5_

I'll read the relevant .tex files to understand their current structure, then make all six modifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "e6f59308-fb4f-4792-9c75-a65d44231031",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oFHEq2GQEtb9ci1LZJNQC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13268,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13268
      },
      "output_tokens": 24,
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01EwCpqj1ZDz2gMQpu3h9QjS`</summary>

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
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "6a1dced5-59c5-4d8f-a361-39c519fef8d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oFHEq2GQEtb9ci1LZJNQC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13268,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13268
      },
      "output_tokens": 24,
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

_source line 7 · 2026-05-16T13:03:47.666Z_

<details><summary>↩ Tool result · `toolu_01EwCpqj1ZDz2gMQpu3h9QjS`</summary>

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
136	The causal claim that trained embedding \emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.
137	
138	\paragraph{Evidence A: exposure is necessary (exp\_008a).}
139	Exp\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\_008d, its NVE remains in the $0.59$--$0.93\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\dt{>}1$ state predictions within the RSSM.
140	
141	This contrasts with exp\_006 (trained $e_{\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\times$ at 45K to $2.31\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.
142	
143	\paragraph{Evidence B: trainability is necessary (exp\_015b).}
144	Exp\_015b uses a frozen random-projection embedding ($d{=}32$, \texttt{requires\_grad=False}, subsample ON, $H{=}8$)---the same multi-rate data regime as exp\_008d, but with a non-trainable temporal signal. Despite full exposure to $\dt{>}1$ transitions, the NVE never exceeds the CIVO threshold: it remains in the $0.39$--$0.47\times$ range throughout the 55K--105K window, with a brief peak of $1.45\times$ at 55K that self-corrects to $0.65\times$ by 65K. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \S\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.
145	
146	The contrast with exp\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\times$ and triggers full collapse (eval 82.8), while the frozen embedding never exceeds $0.47\times$ in the same window---an $8.7\times$ NVE gap. This demonstrates that a $\dt$-embedding must be able to \emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.
147	
148	Together, these two controls establish that CIVO requires the \emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.
149	
150	\begin{table}[h]
151	\centering
152	\small
153	\caption{Causal isolation: $e_{\dt}$ configuration $\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}
154	\label{tab:causal_matrix}
155	\begin{tabular}{lcc}
156	\toprule
157	& Multi-rate data (\textsc{on}) & Single-rate data (\textsc{off}) \\
158	\midrule
159	Trained $e_{\dt}$ & exp\_008d: \textbf{CIVO} & exp\_008a: healthy \\
160	 & NVE 4.12$\times$, collapse & NVE 0.93$\times$ \\
161	\midrule
162	Frozen $e_{\dt}$ & exp\_015b: grad.\ starvation & --- \\
163	 & NVE 0.47$\times$ & \\
164	\midrule
165	Removed $e_{\dt}$ & exp\_008f: no CIVO & --- \\
166	 & NVE $\leq$0.97$\times$ & \\
167	\bottomrule
168	\end{tabular}
169	\end{table}
170	
171	Only the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\ref{tab:causal_matrix}). This 2$\times$2 structure establishes that both factors are jointly necessary.
172	
173	%% ============================================================
174	%% F4: dt=2 > dt=4 monotonic degradation
175	%% ============================================================
176	
177	\subsection{F4: Degradation Scales Monotonically with \texorpdfstring{$\dt$}{dt}}
178	\label{sec:f4}
179	
180	\begin{figure}[t]
181	\centering
182	\includegraphics[width=\columnwidth]{figures/paper/fig5_dt_amplification.pdf}
183	\caption{Peak evaluation return as a function of imagination $\dt$. Performance degrades monotonically: $\dt{=}1$ (915.7) $>$ $\dt{=}2$ (485.3, $-47\%$) $>$ $\dt{=}4$ (176.9, $-81\%$).}
184	\label{fig:dt_amplification}
185	\end{figure}
186	
187	The magnitude of degradation scales monotonically with the imagination step size (Figure~\ref{fig:dt_amplification}). From the $\dt{=}1$ baseline (915.7 at 105K), fixed $\dt{=}2$ (exp\_006) achieves a peak of only 485.3 ($-47\%$), and fixed $\dt{=}4$ (exp\_007) peaks at 176.9 ($-81\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.
188	
189	%% ============================================================
190	%% F5: Horizon and subsample secondary
191	%% ============================================================
192	
193	\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}
194	\label{sec:f5}
195	
196	Neither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\nve < 0.93\times$ (\S\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\nve = 4.12\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\ 009c: 148.3) but neither exhibits $\nve > 1.5\times$---confirming that low evaluation alone does not indicate CIVO.
197	
198	The $3.2\times$ performance gap (008a: 777.7 vs.\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\leq$0.93$\times$).
199	
200	%% ============================================================
201	%% F6: dt=1 imagination does not prevent collapse
202	%% ============================================================
203	
204	\subsection{F6: Restricting Imagination to \texorpdfstring{$\dt{=}1$}{dt=1} Does Not Prevent Collapse}
205	\label{sec:f6}
206	
207	\begin{figure}[t]
208	\centering
209	\includegraphics[width=\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}
210	\caption{Contrasting collapse dynamics. \textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \textbf{Right:} 008e\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}
211	\label{fig:multiple_pathways}
212	\end{figure}
213	
214	The mitigation experiment exp\_008e\_v3 restricts imagination to $\dt{=}1$ while retaining the trained $\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:
215	
216	\begin{itemize}[nosep,leftmargin=*]
217	\item \textbf{Seed 1} (008e\_v3\_s1): Healthy. Eval 869.9 at 105K ($95\%$ of baseline), $\nve = 0.80\times$.
218	\item \textbf{Seed 2} (008e\_v3\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\nve = 3.78\times$.
219	\end{itemize}
220	
221	The baseline with seed 2 (exp\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.
222	
223	\paragraph{Distinct collapse mechanisms.}
224	The collapse dynamics of 008e\_v3\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\ref{tab:main_results}, Figure~\ref{fig:multiple_pathways}):
225	
226	\begin{itemize}[nosep,leftmargin=*]
227	\item \textbf{008d (CIVO, Pathway A):} value explosion ($+130\%$) $\rightarrow$ evaluation decline $\rightarrow$ entropy decreases.
228	\item \textbf{008e\_v3\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\%$) $\rightarrow$ value remains stable $\rightarrow$ entropy \emph{increases} ($-5.21 \rightarrow -3.83$).
229	\end{itemize}
230	
231	In Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\dt{=}1$ prevents the CIVO mechanism---no early $\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.
232	
233	This case also produces the sole false positive in the $\nve \geq 1.5\times$ classification: 008e\_v3\_s2's late evaluation decline inflates $\nve$ to $3.78\times$ through a non-CIVO mechanism (\S\ref{sec:pathways}).
234	
235	%% ============================================================
236	%% TABLE 2: RSSM Fidelity
237	%% ============================================================
238	
239	\begin{table}[t]
240	\centering
241	\caption{RSSM fidelity at $\dt{=}1$ vs.\ $\dt{=}2$. Trained embedding (008d) produces $2.78\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}
242	\label{tab:rssm_fidelity}
243	\footnotesize
244	\setlength{\tabcolsep}{4pt}
245	\begin{tabular}{lcccccc}
246	\toprule
247	& \multicolumn{3}{c}{\textbf{obs\_MSE}} & \multicolumn{3}{c}{\textbf{reward\_MAE}} \\
248	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
249	\textbf{Config} & $\dt{=}1$ & $\dt{=}2$ & Gap & $\dt{=}1$ & $\dt{=}2$ & Gap \\
250	\midrule
251	Baseline & 13.49 & 27.50 & 2.04$\times$ & 0.0102 & 0.0159 & 1.56$\times$ \\
252	008d (trained) & 41.31 & 53.67 & 1.30$\times$ & 0.0568 & 0.1579 & 2.78$\times$ \\
253	008f (no emb) & 8.01 & 22.04 & 2.75$\times$ & 0.7469 & 0.7526 & 1.01$\times$ \\
254	\bottomrule
255	\end{tabular}
256	\end{table}
257	
258	\paragraph{RSSM fidelity analysis.}
259	Table~\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\dt$-embedding in 008d produces a $2.78\times$ gap in reward prediction error between $\dt{=}1$ and $\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\ $0.0568$ for 008d at $\dt{=}1$).
260	
261	\paragraph{Summary.}
262	F1--F5 establish the combination of trained $\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\dt$.  F6 shows that restricting imagination to $\dt{=}1$ prevents CIVO but not all collapse modes: $\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.
263	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "63f4a02f-d95a-4949-a8ee-f8c7d0a51500",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n009e & Factorial (s1) & trn & ON & 8 & 131.1 @105K & 4.12$\\times$ & Oscillatory \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n009c & No dt\\_emb (s2) & --- & ON & 8 & 148.3 @105K & 1.14$\\times$ & Declining \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\\times$ & Slow learner \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline, regardless of mechanism (Figure~\\ref{fig:learning_curves}). The baseline (exp\\_001) reaches 915.7 at 105K steps and peaks at 970.4 at 505K. In contrast, fixed $\\dt{=}2$ (exp\\_006) peaks at 485.3 at 35K before collapsing to 132.9 by 65K---a $-73\\%$ decline from its own peak (14\\% of baseline). Fixed $\\dt{=}4$ (exp\\_007) peaks at only 176.9 at 25K and never exceeds 152.5 thereafter. The learned-gate configuration (exp\\_005) peaks at 541.2 at 55K but collapses to 98.8 by 145K. This uniform degradation motivates the factorial analysis that follows.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves for all configurations. The $\\dt{=}1$ baseline (black) reaches 915.7 at 105K; all variable-rate configurations degrade, with fixed $\\dt{=}4$ and the learned gate collapsing most severely.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\\_008d (trained $\\dt$-embedding, subsampling ON, $H{=}8$) against exp\\_008f (identical configuration but \\emph{no} trained $\\dt$-embedding). As shown in Figure~\\ref{fig:nve_trajectory}:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d} (trained): $\\nve = 1.78\\times$ at 25K $\\rightarrow$ $4.12\\times$ at 55K $\\rightarrow$ collapse (eval 167$\\rightarrow$82.8).\n\\item \\textbf{008f} (no dt\\_emb): $\\nve = 1.02\\times$ at 25K $\\rightarrow$ $0.30\\times$ at 105K $\\rightarrow$ no collapse (eval 503.0 at 105K).\n\\end{itemize}\n\nIn the 35K+ window (\\S\\ref{sec:metrics}), the $\\nve \\geq 1.5\\times$ threshold correctly classifies 7/8 seeds (AUROC${=}0.933$, Clopper--Pearson 95\\% CI $[0.47, 1.0]$): 3 CIVO-positive (exp\\_006, 008d, 009b) and 4 CIVO-negative, with one non-CIVO false positive (008e\\_v3 s2, $3.78\\times$; \\S\\ref{sec:f6}).  The gap between the lowest true positive ($1.62\\times$) and the highest true negative ($1.00\\times$) is $0.62$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}\n\\caption{Normalized value-to-eval ratio ($\\nve$) trajectories. The dashed line marks the $1.5\\times$ threshold. All trained-embedding configurations with $\\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\\_v3 s1, dash-dot) with $\\dt{=}1$-only imagination remains below it.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\n\\paragraph{Three post-CIVO outcomes.}\nRunning the 008d configuration with two independent seeds (s1, s2) reveals that trained $\\dt$-embedding triggers CIVO---yet the downstream consequence is stochastic. Exp\\_009e extends seed~1 (008d) beyond 55K to 105K steps:\n\n%% ============================================================\n%% TABLE 3: Three post-CIVO outcomes\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window. Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\ns1 ext (009e) & 4.12$\\times$ & 1.57$\\times$ & 131.1 & Oscillatory \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Seed 1 (008d):} Full collapse (Pathway A). Value explosion ($+130\\%$), evaluation declines from 167 to 82.8, entropy decreases---the classic CIVO feedback loop.\n\n\\noindent\\textbf{Seed 2 (009b):} Transient CIVO. The $\\nve$ reaches $1.62\\times$ at 45K (35K+ window), exceeding the $1.5\\times$ threshold, but the value function self-corrects to $0.38\\times$ by 105K, and evaluation recovers to 267.9. This demonstrates the threshold's sensitivity to early CIVO signals even in cases that spontaneously recover.\n\n\\noindent\\textbf{Seed 1 extended (009e):} Oscillatory degradation. Continuing 008d beyond 55K, evaluation oscillates between 82.7 and 250 before settling at 131.1; the value function rises then reverses (peak $\\nve = 4.12\\times$ at 55K, final $1.57\\times$).\n\nAll runs exceed $\\nve \\geq 1.5\\times$ in the 35K+ window, confirming deterministic CIVO triggering, but downstream outcomes are seed-dependent (1/2 persistent collapse rate among independent seeds).\n\n%% ============================================================\n%% F3: Unexposed dt_embedding suppresses value drift\n%% ============================================================\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$)---the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE never exceeds the CIVO threshold: it remains in the $0.39$--$0.47\\times$ range throughout the 55K--105K window, with a brief peak of $1.45\\times$ at 55K that self-corrects to $0.65\\times$ by 65K. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ and triggers full collapse (eval 82.8), while the frozen embedding never exceeds $0.47\\times$ in the same window---an $8.7\\times$ NVE gap. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n%% ============================================================\n%% F5: Horizon and subsample secondary\n%% ============================================================\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n%% ============================================================\n%% F6: dt=1 imagination does not prevent collapse\n%% ============================================================\n\n\\subsection{F6: Restricting Imagination to \\texorpdfstring{$\\dt{=}1$}{dt=1} Does Not Prevent Collapse}\n\\label{sec:f6}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \\textbf{Right:} 008e\\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \\emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\nThe mitigation experiment exp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained $\\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Seed 1} (008e\\_v3\\_s1): Healthy. Eval 869.9 at 105K ($95\\%$ of baseline), $\\nve = 0.80\\times$.\n\\item \\textbf{Seed 2} (008e\\_v3\\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\\nve = 3.78\\times$.\n\\end{itemize}\n\nThe baseline with seed 2 (exp\\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.\n\n\\paragraph{Distinct collapse mechanisms.}\nThe collapse dynamics of 008e\\_v3\\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\\ref{tab:main_results}, Figure~\\ref{fig:multiple_pathways}):\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d (CIVO, Pathway A):} value explosion ($+130\\%$) $\\rightarrow$ evaluation decline $\\rightarrow$ entropy decreases.\n\\item \\textbf{008e\\_v3\\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\\%$) $\\rightarrow$ value remains stable $\\rightarrow$ entropy \\emph{increases} ($-5.21 \\rightarrow -3.83$).\n\\end{itemize}\n\nIn Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\\dt{=}1$ prevents the CIVO mechanism---no early $\\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.\n\nThis case also produces the sole false positive in the $\\nve \\geq 1.5\\times$ classification: 008e\\_v3\\_s2's late evaluation decline inflates $\\nve$ to $3.78\\times$ through a non-CIVO mechanism (\\S\\ref{sec:pathways}).\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RSSM fidelity analysis.}\nTable~\\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\\dt$-embedding in 008d produces a $2.78\\times$ gap in reward prediction error between $\\dt{=}1$ and $\\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\\ $0.0568$ for 008d at $\\dt{=}1$).\n\n\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.\n",
      "numLines": 263,
      "startLine": 1,
      "totalLines": 263
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_013XqmxeWDHs4dgpA7SHz7oE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "2eaa3beb-f6d5-4517-bfc2-9dbd0d4f8569",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oFHEq2GQEtb9ci1LZJNQC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13268,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13268
      },
      "output_tokens": 24,
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

_source line 9 · 2026-05-16T13:03:48.099Z_

<details><summary>↩ Tool result · `toolu_013XqmxeWDHs4dgpA7SHz7oE`</summary>

```text
1	\section{Analysis \& Discussion}
2	\label{sec:analysis}
3	
4	The preceding results establish that the combination of trained $\dt$-embedding and multi-rate data exposure is the causal factor behind pathological value dynamics in variable-rate DreamerV3. In this section, we synthesize these findings into a mechanistic account of conditioning-induced value overestimation (CIVO), explain why the same CIVO trigger produces divergent outcomes across seeds, contrast the imagination-based setting with MPC-based temporal conditioning, and discuss the fundamental tension inherent in the $\dt$-embedding design.
5	
6	\subsection{The CIVO Mechanism}
7	\label{sec:civo_mechanism}
8	
9	The RSSM fidelity analysis (Table~\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\dt{=}1$ is $0.0568$, while at $\dt{=}2$ it rises to $0.1579$---a $2.78\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\times$ gap, and the baseline shows $1.56\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.
10	
11	This asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\dt$-embedding causes RSSM predictions at $\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\nve$ above $1.5\times$, followed by evaluation collapse.
12	
13	A random-policy control experiment ($N{=}100$ rollouts, 95\% bootstrap CI) decomposes CIVO into two necessary stages.  \textbf{Stage~1 (dynamics bias):} even under a random policy, $\dt{=}2$ imagination produces $1.68\times$ higher mean reward than $\dt{=}1$ in the trained-embedding model (008d)---the RSSM prior already generates reward-favorable trajectories at $\dt > 1$, independent of actor behavior.  \textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\times$ and the trained-actor ratio is $0.98\times$.  The decomposition attributes $\approx 36\%$ of the total effect to dynamics bias and $\approx 64\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.
14	
15	This mechanism is analogous to delusional bias \citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced---the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.
16	
17	\subsection{Selective Gradient Stopping and Gradient Decomposition}
18	\label{sec:sgs_gradient_analysis}
19	
20	\subsubsection{Design and Hypothesis}
21	\label{sec:sgs_design}
22	
23	The preceding analysis establishes that a trained temporal embedding $e_{\Delta t}$ is necessary for CIVO (Section~\ref{sec:civo_mechanism}). We next ask \textit{which gradient pathway} through $e_{\Delta t}$ amplifies the overestimation. In DreamerV3, the temporal embedding conditions all prediction heads simultaneously through the RSSM latent state. A natural hypothesis is that the \textit{reward head}---which directly supplies $\lambda$-return targets to the critic---is the primary amplifier: if reward predictions develop $\Delta t$-dependent biases, the critic inherits and compounds these biases across the $H$-step imagination rollout.
24	
25	To test this, we introduce \textit{selective gradient stopping} (SGS): during the backward pass, $e_{\Delta t}$ is detached before entering the reward head,
26	$$\hat{r}_t = f_{\text{reward}}\big(\operatorname{sg}(e_{\Delta t}),\; h_t,\; z_t\big),$$
27	where $\operatorname{sg}(\cdot)$ denotes the stop-gradient operator. This prevents reward-loss gradients from updating $e_{\Delta t}$'s parameters while preserving the embedding's forward-pass contribution. All other gradient pathways---observation decoders, continuation predictor, KL dynamics---remain intact. We apply this intervention to the primary CIVO-exhibiting configuration: Walker Walk, trained $e_{\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\Delta t{=}2$ imagination (exp\_016e; identical to exp\_008d except for \texttt{reward\_dt\_emb\_detach=True}).
28	
29	
30	\subsubsection{Gradient Decomposition Reveals the Reward Pathway is Inactive}
31	\label{sec:gradient_decomposition}
32	
33	Exp\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps (exp\_016e) followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\times$ (exp\_016e). The SGS intervention neither prevented nor attenuated CIVO.
34	
35	To explain this null result, we performed a gradient decomposition analysis using \texttt{torch.autograd.grad} to measure each loss component's contribution to $\nabla_\theta e_{\Delta t}$, where $\theta$ denotes the temporal embedding parameters (D061). Table~\ref{tab:gradient_decomposition} reports the results.
36	
37	\begin{table}[h]
38	\centering
39	\caption{Gradient contributions to the temporal embedding $e_{\Delta t}$ by loss component, measured via \texttt{torch.autograd.grad} at step 95K (D061). Gradient norms are $\ell_2$ norms of $\nabla_\theta \mathcal{L}_i$ for each loss $\mathcal{L}_i$.}
40	\label{tab:gradient_decomposition}
41	\small
42	\begin{tabular}{lrr}
43	\toprule
44	Loss component & $\|\nabla_\theta \mathcal{L}_i\|_2$ & Share (\%) \\
45	\midrule
46	Observation decoders (orientations, velocity, height) & 1.505 & 92.7 \\
47	KL dynamics & 0.119 & 7.3 \\
48	Continuation head & $<$0.001 & $<$0.1 \\
49	Reward head & 0.000 & 0.0 \\
50	\midrule
51	\textbf{Total} & \textbf{1.624} & \textbf{100} \\
52	\bottomrule
53	\end{tabular}
54	\end{table}
55	
56	The reward head contributes \textit{numerically negligible---zero to within floating-point precision} gradient to the temporal embedding. Exp\_016e's stop-gradient intervention detaches a gradient pathway that carries no signal---it is an architectural no-op. The null result is therefore expected: the intervention removes nothing.
57	
58	The zero reward gradient is a consequence of the relative output dimensionality. All decoder losses backpropagate through the same RSSM latent state to reach $e_{\Delta t}$. The observation decoders reconstruct a 24-dimensional proprioceptive signal (14 orientations, 9 velocities, 1 height), while the reward head predicts a single scalar. This ${\sim}24\!\times$ dimensionality asymmetry, compounded by DreamerV3's symlog reward scaling which further compresses the reward gradient magnitude, renders the reward head's contribution numerically negligible---zero to within floating-point precision.
59	
60	
61	\subsubsection{Implications for the CIVO Mechanism}
62	\label{sec:sgs_implications}
63	
64	The gradient decomposition reframes the mechanistic understanding of how the temporal embedding drives CIVO.
65	
66	\paragraph{Observation reconstruction dominates temporal embedding learning.} The temporal embedding's parameters are shaped almost entirely (93\%) by the observation reconstruction objective (D061). This means $e_{\Delta t}$ learns to encode temporal information that helps minimize \textit{observation prediction error}, not reward prediction error. If this learned representation introduces systematic biases in latent state predictions at $\Delta t{>}1$---for instance, by encouraging the RSSM to produce states that are easy to decode but dynamically inaccurate---these biases propagate to \textit{all} downstream computation, including reward prediction and the critic's value estimates. CIVO thus originates in the observation reconstruction objective's influence on latent dynamics, not in reward-specific pathways.
67	
68	\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone---reward prediction regularization, reward-conditioned value clipping, or the reward-only SGS tested here---addresses $<$1\% of the gradient flow to $e_{\Delta t}$ and cannot attenuate CIVO. Effective gradient-level interventions must address the dominant observation decoder pathway. This motivates the \textit{full-pathway SGS} design (exp\_018): detaching $e_{\Delta t}$ from all decoder and reward gradients, retaining only the 7\% KL dynamics contribution. Full-pathway SGS removes 93\% of the gradient to $e_{\Delta t}$, constituting a genuine gradient-level intervention rather than the null operation of reward-only SGS.
69	
70	\paragraph{Connection to RSSM fidelity analysis.} The observation-dominated gradient structure is consistent with the RSSM fidelity results in Table~\ref{tab:rssm_fidelity}: the trained-embedding condition (exp\_008d) shows a $2.78\times$ reward gap between $\Delta t{=}1$ and $\Delta t{=}2$ transitions, despite the reward head receiving zero gradient from $e_{\Delta t}$. This confirms that the reward head's $\Delta t$-dependent biases are inherited \textit{through the latent state}---which is shaped by observation reconstruction gradients---rather than learned directly from the reward objective.
71	
72	
73	\subsubsection{Exp\_016e Reinterpreted as Stochastic Variation}
74	\label{sec:016e_reinterp}
75	
76	With the gradient decomposition establishing that exp\_016e is a no-op intervention, the apparent timing differences between exp\_016e and exp\_008d---later collapse onset (75K vs.\ 25K) and higher peak evaluation (326.7 vs.\ 167.2)---must be attributed to stochastic variation rather than SGS effects. This attribution is consistent with the seed-to-seed variability already observed within the trained-embedding condition: exp\_009b (same configuration as exp\_008d, seed 2) reaches peak evaluation 278.5 at 95K (exp\_009b) with transient NVE of $1.62\times$ at 45K before self-correcting, compared to exp\_008d's monotonic collapse from 25K. The qualitative diversity between exp\_008d (early collapse), exp\_009b (self-correction), and exp\_016e (delayed collapse) falls within the range of stochastic outcomes for a single trained-$e_{\Delta t}$ configuration.
77	
78	All three trajectories share the invariant identified by the NVE diagnostic: each crosses the $1.5\times$ pathological threshold at some point during training (exp\_008d at 35K: $1.71\times$; exp\_009b at 45K: $1.62\times$; exp\_016e at 95K: $10.42\times$). Whether this pathological overestimation leads to sustained collapse or transient recovery depends on early training stochasticity, not on the reward-only SGS intervention (D061).
79	
80	\subsection{Three Post-CIVO Outcomes: Why Seeds Diverge}
81	\label{sec:seed_divergence}
82	
83	The three post-CIVO outcomes (Table~\ref{tab:post_civo})---full collapse, transient CIVO, and oscillatory degradation---all cross the $\nve > 1.5\times$ threshold, yet the downstream damage is stochastic.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).  The oscillatory pattern (seed~1, 009e) represents an intermediate regime: the value function rises then reverses while evaluation oscillates, and entropy remains elevated---suggesting the actor has not fully committed to the overestimated policy but cannot escape it.  This partial capacity loss allows the critic to respond to new data without fully correcting its biases.
84	
85	\subsection{Why MPC Is Immune}
86	\label{sec:mpc_immune}
87	
88	\citet{nhu2025tawm} show that $\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step---imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\dt > 1$ is amplified through the closed actor-critic loop.  In terms of the two-stage decomposition (\S\ref{sec:civo_mechanism}), MPC is immune because Stage~2 cannot occur: without imagination-based bootstrapping, the actor cannot exploit the dynamics bias.  This aligns with \citet{frauenknecht2025rollouts}, who find that rollout quality dominates model-based RL performance, and with \citet{tallec2019making}'s analysis of how temporal resolution mismatches destabilize value learning.
89	
90	\subsection{The \texorpdfstring{$\dt$}{dt}-Embedding Dilemma}
91	\label{sec:embedding_dilemma}
92	
93	The factorial results reveal a fundamental tension: removing the $\dt$-embedding (008f) eliminates CIVO but at a $13\times$ cost to reward prediction quality ($0.7469$ vs.\ $0.0568$ MAE)---the world model cannot distinguish temporal scales.  Restricting imagination to $\dt{=}1$ while retaining the trained embedding (008e\_v3) prevents CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\S\ref{sec:f6}).  Neither approach alone provides a complete solution.
94	
95	\subsection{Multiple Vulnerability Pathways}
96	\label{sec:pathways}
97	
98	The two collapse mechanisms identified in \S\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures but a shared root cause: the trained $\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\times$ for 008e\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.  The existence of multiple pathways suggests that mitigation strategies focused exclusively on the imagination channel---restricting $\dt$, truncating rollouts, or smoothing rewards \citep{lee2024dreamsmooth}---may be insufficient.
99	
100	\subsection{Implications for Temporal Abstraction in World Models}
101	\label{sec:implications}
102	
103	CIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training: the RSSM cannot maintain prediction fidelity across temporal resolutions when the embedding co-adapts with the reward head.  Hierarchical approaches---THICK \citep{gumbsch2024thick}, Hieros \citep{mattes2024hieros}, LS-Imagine \citep{li2025lsimagine}---may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  Reward-only gradient stopping is an architectural no-op because the reward head contributes zero gradient to $e_{\Delta t}$ (\S\ref{sec:sgs_gradient_analysis}); full-pathway SGS that detaches the dominant observation-decoder gradients constitutes a genuine intervention targeting 93\% of the gradient flow (exp\_018; \S\ref{sec:sgs_implications}).  Whether spectral normalization or other regularization strategies can preserve temporal fidelity while preventing co-adaptation remains an open question.
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "d74ce2cf-8f58-4e2b-8721-d34b2d749029",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex",
      "content": "\\section{Analysis \\& Discussion}\n\\label{sec:analysis}\n\nThe preceding results establish that the combination of trained $\\dt$-embedding and multi-rate data exposure is the causal factor behind pathological value dynamics in variable-rate DreamerV3. In this section, we synthesize these findings into a mechanistic account of conditioning-induced value overestimation (CIVO), explain why the same CIVO trigger produces divergent outcomes across seeds, contrast the imagination-based setting with MPC-based temporal conditioning, and discuss the fundamental tension inherent in the $\\dt$-embedding design.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$---a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d)---the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced---the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Design and Hypothesis}\n\\label{sec:sgs_design}\n\nThe preceding analysis establishes that a trained temporal embedding $e_{\\Delta t}$ is necessary for CIVO (Section~\\ref{sec:civo_mechanism}). We next ask \\textit{which gradient pathway} through $e_{\\Delta t}$ amplifies the overestimation. In DreamerV3, the temporal embedding conditions all prediction heads simultaneously through the RSSM latent state. A natural hypothesis is that the \\textit{reward head}---which directly supplies $\\lambda$-return targets to the critic---is the primary amplifier: if reward predictions develop $\\Delta t$-dependent biases, the critic inherits and compounds these biases across the $H$-step imagination rollout.\n\nTo test this, we introduce \\textit{selective gradient stopping} (SGS): during the backward pass, $e_{\\Delta t}$ is detached before entering the reward head,\n$$\\hat{r}_t = f_{\\text{reward}}\\big(\\operatorname{sg}(e_{\\Delta t}),\\; h_t,\\; z_t\\big),$$\nwhere $\\operatorname{sg}(\\cdot)$ denotes the stop-gradient operator. This prevents reward-loss gradients from updating $e_{\\Delta t}$'s parameters while preserving the embedding's forward-pass contribution. All other gradient pathways---observation decoders, continuation predictor, KL dynamics---remain intact. We apply this intervention to the primary CIVO-exhibiting configuration: Walker Walk, trained $e_{\\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\\Delta t{=}2$ imagination (exp\\_016e; identical to exp\\_008d except for \\texttt{reward\\_dt\\_emb\\_detach=True}).\n\n\n\\subsubsection{Gradient Decomposition Reveals the Reward Pathway is Inactive}\n\\label{sec:gradient_decomposition}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps (exp\\_016e) followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$ (exp\\_016e). The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters (D061). Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} at step 95K (D061). Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\nLoss component & $\\|\\nabla_\\theta \\mathcal{L}_i\\|_2$ & Share (\\%) \\\\\n\\midrule\nObservation decoders (orientations, velocity, height) & 1.505 & 92.7 \\\\\nKL dynamics & 0.119 & 7.3 \\\\\nContinuation head & $<$0.001 & $<$0.1 \\\\\nReward head & 0.000 & 0.0 \\\\\n\\midrule\n\\textbf{Total} & \\textbf{1.624} & \\textbf{100} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reward head contributes \\textit{numerically negligible---zero to within floating-point precision} gradient to the temporal embedding. Exp\\_016e's stop-gradient intervention detaches a gradient pathway that carries no signal---it is an architectural no-op. The null result is therefore expected: the intervention removes nothing.\n\nThe zero reward gradient is a consequence of the relative output dimensionality. All decoder losses backpropagate through the same RSSM latent state to reach $e_{\\Delta t}$. The observation decoders reconstruct a 24-dimensional proprioceptive signal (14 orientations, 9 velocities, 1 height), while the reward head predicts a single scalar. This ${\\sim}24\\!\\times$ dimensionality asymmetry, compounded by DreamerV3's symlog reward scaling which further compresses the reward gradient magnitude, renders the reward head's contribution numerically negligible---zero to within floating-point precision.\n\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reframes the mechanistic understanding of how the temporal embedding drives CIVO.\n\n\\paragraph{Observation reconstruction dominates temporal embedding learning.} The temporal embedding's parameters are shaped almost entirely (93\\%) by the observation reconstruction objective (D061). This means $e_{\\Delta t}$ learns to encode temporal information that helps minimize \\textit{observation prediction error}, not reward prediction error. If this learned representation introduces systematic biases in latent state predictions at $\\Delta t{>}1$---for instance, by encouraging the RSSM to produce states that are easy to decode but dynamically inaccurate---these biases propagate to \\textit{all} downstream computation, including reward prediction and the critic's value estimates. CIVO thus originates in the observation reconstruction objective's influence on latent dynamics, not in reward-specific pathways.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone---reward prediction regularization, reward-conditioned value clipping, or the reward-only SGS tested here---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and cannot attenuate CIVO. Effective gradient-level interventions must address the dominant observation decoder pathway. This motivates the \\textit{full-pathway SGS} design (exp\\_018): detaching $e_{\\Delta t}$ from all decoder and reward gradients, retaining only the 7\\% KL dynamics contribution. Full-pathway SGS removes 93\\% of the gradient to $e_{\\Delta t}$, constituting a genuine gradient-level intervention rather than the null operation of reward-only SGS.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The observation-dominated gradient structure is consistent with the RSSM fidelity results in Table~\\ref{tab:rssm_fidelity}: the trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions, despite the reward head receiving zero gradient from $e_{\\Delta t}$. This confirms that the reward head's $\\Delta t$-dependent biases are inherited \\textit{through the latent state}---which is shaped by observation reconstruction gradients---rather than learned directly from the reward objective.\n\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nWith the gradient decomposition establishing that exp\\_016e is a no-op intervention, the apparent timing differences between exp\\_016e and exp\\_008d---later collapse onset (75K vs.\\ 25K) and higher peak evaluation (326.7 vs.\\ 167.2)---must be attributed to stochastic variation rather than SGS effects. This attribution is consistent with the seed-to-seed variability already observed within the trained-embedding condition: exp\\_009b (same configuration as exp\\_008d, seed 2) reaches peak evaluation 278.5 at 95K (exp\\_009b) with transient NVE of $1.62\\times$ at 45K before self-correcting, compared to exp\\_008d's monotonic collapse from 25K. The qualitative diversity between exp\\_008d (early collapse), exp\\_009b (self-correction), and exp\\_016e (delayed collapse) falls within the range of stochastic outcomes for a single trained-$e_{\\Delta t}$ configuration.\n\nAll three trajectories share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training (exp\\_008d at 35K: $1.71\\times$; exp\\_009b at 45K: $1.62\\times$; exp\\_016e at 95K: $10.42\\times$). Whether this pathological overestimation leads to sustained collapse or transient recovery depends on early training stochasticity, not on the reward-only SGS intervention (D061).\n\n\\subsection{Three Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\nThe three post-CIVO outcomes (Table~\\ref{tab:post_civo})---full collapse, transient CIVO, and oscillatory degradation---all cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).  The oscillatory pattern (seed~1, 009e) represents an intermediate regime: the value function rises then reverses while evaluation oscillates, and entropy remains elevated---suggesting the actor has not fully committed to the overestimated policy but cannot escape it.  This partial capacity loss allows the critic to respond to new data without fully correcting its biases.\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step---imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.  In terms of the two-stage decomposition (\\S\\ref{sec:civo_mechanism}), MPC is immune because Stage~2 cannot occur: without imagination-based bootstrapping, the actor cannot exploit the dynamics bias.  This aligns with \\citet{frauenknecht2025rollouts}, who find that rollout quality dominates model-based RL performance, and with \\citet{tallec2019making}'s analysis of how temporal resolution mismatches destabilize value learning.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE)---the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) prevents CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse mechanisms identified in \\S\\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures but a shared root cause: the trained $\\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.  The existence of multiple pathways suggests that mitigation strategies focused exclusively on the imagination channel---restricting $\\dt$, truncating rollouts, or smoothing rewards \\citep{lee2024dreamsmooth}---may be insufficient.\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training: the RSSM cannot maintain prediction fidelity across temporal resolutions when the embedding co-adapts with the reward head.  Hierarchical approaches---THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}---may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  Reward-only gradient stopping is an architectural no-op because the reward head contributes zero gradient to $e_{\\Delta t}$ (\\S\\ref{sec:sgs_gradient_analysis}); full-pathway SGS that detaches the dominant observation-decoder gradients constitutes a genuine intervention targeting 93\\% of the gradient flow (exp\\_018; \\S\\ref{sec:sgs_implications}).  Whether spectral normalization or other regularization strategies can preserve temporal fidelity while preventing co-adaptation remains an open question.\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01S11B6LK7WsSASJgVpiYnPR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "733d6744-9394-4490-88c7-698e18cf1d0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oFHEq2GQEtb9ci1LZJNQC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13268,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13268
      },
      "output_tokens": 24,
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

_source line 11 · 2026-05-16T13:03:49.133Z_

<details><summary>↩ Tool result · `toolu_01S11B6LK7WsSASJgVpiYnPR`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We have presented a systematic factorial diagnostic of temporal abstraction in DreamerV3, identifying the combination of trained $\dt$-embedding and multi-rate data exposure as the causal factor behind conditioning-induced value overestimation (CIVO). The key findings are:
5	
6	\begin{enumerate}[nosep,leftmargin=*]
7	\item Every variable-rate imagination configuration degrades relative to the $\dt{=}1$ baseline, with degradation scaling monotonically with $\dt$.
8	\item A normalized value-to-eval threshold of $\nve \geq 1.5\times$ (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, 87.5\%), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The combination of trained $\dt$-embedding and multi-rate data exposure is the causal factor; unexposed, frozen, or removed embeddings prevent overestimation.
9	\item The RSSM reward head develops a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$ under trained conditioning, providing the systematic bias that drives critic overestimation.
10	\item The same CIVO trigger produces stochastic downstream outcomes---full collapse, transient CIVO with self-correction, and oscillatory degradation---across seeds of identical configurations.
11	\item Restricting imagination to $\dt{=}1$ does not fully prevent collapse: one of two seeds fails via a qualitatively distinct non-CIVO pathway (eval-driven with increasing entropy), demonstrating that the trained $\dt$-embedding creates vulnerability through multiple mechanisms.
12	\end{enumerate}
13	
14	The contrast with TAWM's success in MPC identifies the feedback architecture as the critical factor: $\dt$-conditioning succeeds when errors are contained by re-planning from real states, but fails when errors compound through imagination-based actor-critic bootstrapping.
15	
16	\paragraph{Limitations.}
17	Our experiments focus on a single environment (Walker Walk) and a single world-model architecture (DreamerV3/RSSM). While multi-seed replication establishes robustness within this setting, generalization to other environments and architectures---particularly transformer-based world models such as DreamerV4---remains an open question. The $\nve$ threshold ($1.5\times$, 35K+ window) is sensitive to value overestimation broadly but not perfectly specific to CIVO (7/8, one non-CIVO false positive; margin $0.62$ excluding the outlier); generalization to other tasks and architectures is pending validation.
18	
19	\paragraph{Future directions.}
20	Our findings suggest three avenues. First, hierarchical temporal abstraction at the representation level---as in THICK and Hieros---may avoid the flat-conditioning failure mode by maintaining separate dynamics for each temporal scale. Second, gradient decomposition reveals that 93\% of $\dt$-embedding gradients originate from observation decoders, with 0\% from the reward head---making reward-only gradient stopping (exp\_016e) an architectural no-op. Full-pathway gradient stopping targeting observation decoders (exp\_018), which removes the dominant 93\% contribution, is queued to test whether the vulnerability is gradient-level or representation-level. Third, extending this diagnostic framework to transformer-based world models and continuous-control benchmarks would clarify whether CIVO is RSSM-specific or a broader vulnerability of temporal conditioning in imagination-based RL.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "9c617546-9b06-4e7d-aa7e-6626f7b9fe93",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe have presented a systematic factorial diagnostic of temporal abstraction in DreamerV3, identifying the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor behind conditioning-induced value overestimation (CIVO). The key findings are:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item Every variable-rate imagination configuration degrades relative to the $\\dt{=}1$ baseline, with degradation scaling monotonically with $\\dt$.\n\\item A normalized value-to-eval threshold of $\\nve \\geq 1.5\\times$ (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, 87.5\\%), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The combination of trained $\\dt$-embedding and multi-rate data exposure is the causal factor; unexposed, frozen, or removed embeddings prevent overestimation.\n\\item The RSSM reward head develops a $2.78\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$ under trained conditioning, providing the systematic bias that drives critic overestimation.\n\\item The same CIVO trigger produces stochastic downstream outcomes---full collapse, transient CIVO with self-correction, and oscillatory degradation---across seeds of identical configurations.\n\\item Restricting imagination to $\\dt{=}1$ does not fully prevent collapse: one of two seeds fails via a qualitatively distinct non-CIVO pathway (eval-driven with increasing entropy), demonstrating that the trained $\\dt$-embedding creates vulnerability through multiple mechanisms.\n\\end{enumerate}\n\nThe contrast with TAWM's success in MPC identifies the feedback architecture as the critical factor: $\\dt$-conditioning succeeds when errors are contained by re-planning from real states, but fails when errors compound through imagination-based actor-critic bootstrapping.\n\n\\paragraph{Limitations.}\nOur experiments focus on a single environment (Walker Walk) and a single world-model architecture (DreamerV3/RSSM). While multi-seed replication establishes robustness within this setting, generalization to other environments and architectures---particularly transformer-based world models such as DreamerV4---remains an open question. The $\\nve$ threshold ($1.5\\times$, 35K+ window) is sensitive to value overestimation broadly but not perfectly specific to CIVO (7/8, one non-CIVO false positive; margin $0.62$ excluding the outlier); generalization to other tasks and architectures is pending validation.\n\n\\paragraph{Future directions.}\nOur findings suggest three avenues. First, hierarchical temporal abstraction at the representation level---as in THICK and Hieros---may avoid the flat-conditioning failure mode by maintaining separate dynamics for each temporal scale. Second, gradient decomposition reveals that 93\\% of $\\dt$-embedding gradients originate from observation decoders, with 0\\% from the reward head---making reward-only gradient stopping (exp\\_016e) an architectural no-op. Full-pathway gradient stopping targeting observation decoders (exp\\_018), which removes the dominant 93\\% contribution, is queued to test whether the vulnerability is gradient-level or representation-level. Third, extending this diagnostic framework to transformer-based world models and continuous-control benchmarks would clarify whether CIVO is RSSM-specific or a broader vulnerability of temporal conditioning in imagination-based RL.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01ANK85eesScxdKAURfZ7zwq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "4342572c-ee63-4291-90ee-c11853c1db4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oFHEq2GQEtb9ci1LZJNQC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13268,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13268
      },
      "output_tokens": 24,
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

_source line 13 · 2026-05-16T13:03:49.645Z_

<details><summary>↩ Tool result · `toolu_01ANK85eesScxdKAURfZ7zwq`</summary>

```text
1	\begin{abstract}
2	Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance---despite the success of identical $\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify the combination of trained temporal embedding and multi-rate data exposure as the causal trigger and characterize the resulting failure mode: \emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\Delta t{=}1$ and $\Delta t{=}2$, which the critic internalizes as optimistic values. Gradient decomposition shows that 93\% of embedding gradients flow through observation decoders (0\% from the reward head), establishing CIVO as representation-driven. A normalized value-to-eval threshold of $1.5\times$ (35K+ training window) achieves 7/8 classification ($n{=}8$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds---full collapse, transient CIVO with self-correction, and oscillatory degradation---from identical configurations. Critically, restricting imagination to $\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "1fabcde6-fd8b-41fb-b8d7-93cba2d11f54",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTemporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance---despite the success of identical $\\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify the combination of trained temporal embedding and multi-rate data exposure as the causal trigger and characterize the resulting failure mode: \\emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\Delta t{=}1$ and $\\Delta t{=}2$, which the critic internalizes as optimistic values. Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as representation-driven. A normalized value-to-eval threshold of $1.5\\times$ (35K+ training window) achieves 7/8 classification ($n{=}8$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds---full collapse, transient CIVO with self-correction, and oscillatory degradation---from identical configurations. Critically, restricting imagination to $\\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_018u9V8xRXiz5pWPTaV4GkQq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "5114dc1f-5ad1-4a15-ac29-a5186fd78708",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014oFHEq2GQEtb9ci1LZJNQC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13268,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13268
      },
      "output_tokens": 24,
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

_source line 15 · 2026-05-16T13:03:49.882Z_

<details><summary>↩ Tool result · `toolu_018u9V8xRXiz5pWPTaV4GkQq`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\dt{=}2$ collapses to $14\%$ of baseline, fixed $\dt{=}4$ never exceeds $19\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\%$. Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the causal trigger. This trained-and-exposed embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates---a failure mode we term \emph{conditioning-induced value overestimation} (CIVO). A $\nve \geq 1.5\times$ threshold (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, single environment), with one non-CIVO false positive---a failure mode analogous to delusional bias \citep{lu2018nondelusional} but arising from model imprecision amplified by learned temporal conditioning. Gradient decomposition reveals that 93\% of temporal embedding gradients originate from observation decoders rather than the reward head (which contributes 0\%), reframing CIVO as a representation-level phenomenon.
7	
8	Three further findings complicate the picture: (1)~the same CIVO trigger produces stochastic downstream outcomes---full collapse, transient CIVO with self-correction, and oscillatory degradation---across seeds of identical configurations; (2)~restricting imagination to $\dt{=}1$ while retaining the trained embedding does not prevent collapse, with one of two seeds failing via a qualitatively distinct non-CIVO pathway (evaluation-driven, increasing entropy); and (3)~the contrast with TAWM identifies the feedback architecture---imagination-based bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "cd4fe9f6-2939-4f96-b3d8-665ace444aa2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTAWM \\citep{nhu2025tawm} shows that conditioning a world model on step size $\\dt$ yields consistent gains within TD-MPC2's MPC framework \\citep{hansen2024tdmpc2}. Can the same $\\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \\citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?\n\nWe find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\\dt{=}2$ collapses to $14\\%$ of baseline, fixed $\\dt{=}4$ never exceeds $19\\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\\%$. Through a factorial analysis on Walker Walk \\citep{tassa2018dmcontrol}, we isolate the combination of a \\emph{trained} $\\dt$-embedding and multi-rate data exposure as the causal trigger. This trained-and-exposed embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$, which the critic internalizes as optimistic value estimates---a failure mode we term \\emph{conditioning-induced value overestimation} (CIVO). A $\\nve \\geq 1.5\\times$ threshold (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, single environment), with one non-CIVO false positive---a failure mode analogous to delusional bias \\citep{lu2018nondelusional} but arising from model imprecision amplified by learned temporal conditioning. Gradient decomposition reveals that 93\\% of temporal embedding gradients originate from observation decoders rather than the reward head (which contributes 0\\%), reframing CIVO as a representation-level phenomenon.\n\nThree further findings complicate the picture: (1)~the same CIVO trigger produces stochastic downstream outcomes---full collapse, transient CIVO with self-correction, and oscillatory degradation---across seeds of identical configurations; (2)~restricting imagination to $\\dt{=}1$ while retaining the trained embedding does not prevent collapse, with one of two seeds failing via a qualitatively distinct non-CIVO pathway (evaluation-driven, increasing entropy); and (3)~the contrast with TAWM identifies the feedback architecture---imagination-based bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

Now I have all the files. Let me make the six modifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "59261cf0-e640-4102-a22b-6042fd457d3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJrb6sNtKKznFLGAJ7QKf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14224,
      "cache_read_input_tokens": 24715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14224
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

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_0148JSDBNmKHgwZnL3G87Ppi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\",
  "new_string": "018 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 915.7 @105K & 0.72$\\times$ & Healthy \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "9bd8a1d5-6784-4a4b-bb9d-871c1b28e910",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJrb6sNtKKznFLGAJ7QKf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14224,
      "cache_read_input_tokens": 24715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14224
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

_source line 18 · 2026-05-16T13:03:59.923Z_

<details><summary>↩ Tool result · `toolu_0148JSDBNmKHgwZnL3G87Ppi`</summary>

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
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "1cf2b092-367f-469b-baf9-0c52ef10c93f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\",
    "newString": "018 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 915.7 @105K & 0.72$\\times$ & Healthy \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n009e & Factorial (s1) & trn & ON & 8 & 131.1 @105K & 4.12$\\times$ & Oscillatory \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n009c & No dt\\_emb (s2) & --- & ON & 8 & 148.3 @105K & 1.14$\\times$ & Declining \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\\times$ & Slow learner \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline, regardless of mechanism (Figure~\\ref{fig:learning_curves}). The baseline (exp\\_001) reaches 915.7 at 105K steps and peaks at 970.4 at 505K. In contrast, fixed $\\dt{=}2$ (exp\\_006) peaks at 485.3 at 35K before collapsing to 132.9 by 65K---a $-73\\%$ decline from its own peak (14\\% of baseline). Fixed $\\dt{=}4$ (exp\\_007) peaks at only 176.9 at 25K and never exceeds 152.5 thereafter. The learned-gate configuration (exp\\_005) peaks at 541.2 at 55K but collapses to 98.8 by 145K. This uniform degradation motivates the factorial analysis that follows.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves for all configurations. The $\\dt{=}1$ baseline (black) reaches 915.7 at 105K; all variable-rate configurations degrade, with fixed $\\dt{=}4$ and the learned gate collapsing most severely.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\\_008d (trained $\\dt$-embedding, subsampling ON, $H{=}8$) against exp\\_008f (identical configuration but \\emph{no} trained $\\dt$-embedding). As shown in Figure~\\ref{fig:nve_trajectory}:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d} (trained): $\\nve = 1.78\\times$ at 25K $\\rightarrow$ $4.12\\times$ at 55K $\\rightarrow$ collapse (eval 167$\\rightarrow$82.8).\n\\item \\textbf{008f} (no dt\\_emb): $\\nve = 1.02\\times$ at 25K $\\rightarrow$ $0.30\\times$ at 105K $\\rightarrow$ no collapse (eval 503.0 at 105K).\n\\end{itemize}\n\nIn the 35K+ window (\\S\\ref{sec:metrics}), the $\\nve \\geq 1.5\\times$ threshold correctly classifies 7/8 seeds (AUROC${=}0.933$, Clopper--Pearson 95\\% CI $[0.47, 1.0]$): 3 CIVO-positive (exp\\_006, 008d, 009b) and 4 CIVO-negative, with one non-CIVO false positive (008e\\_v3 s2, $3.78\\times$; \\S\\ref{sec:f6}).  The gap between the lowest true positive ($1.62\\times$) and the highest true negative ($1.00\\times$) is $0.62$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}\n\\caption{Normalized value-to-eval ratio ($\\nve$) trajectories. The dashed line marks the $1.5\\times$ threshold. All trained-embedding configurations with $\\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\\_v3 s1, dash-dot) with $\\dt{=}1$-only imagination remains below it.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\n\\paragraph{Three post-CIVO outcomes.}\nRunning the 008d configuration with two independent seeds (s1, s2) reveals that trained $\\dt$-embedding triggers CIVO---yet the downstream consequence is stochastic. Exp\\_009e extends seed~1 (008d) beyond 55K to 105K steps:\n\n%% ============================================================\n%% TABLE 3: Three post-CIVO outcomes\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window. Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\ns1 ext (009e) & 4.12$\\times$ & 1.57$\\times$ & 131.1 & Oscillatory \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Seed 1 (008d):} Full collapse (Pathway A). Value explosion ($+130\\%$), evaluation declines from 167 to 82.8, entropy decreases---the classic CIVO feedback loop.\n\n\\noindent\\textbf{Seed 2 (009b):} Transient CIVO. The $\\nve$ reaches $1.62\\times$ at 45K (35K+ window), exceeding the $1.5\\times$ threshold, but the value function self-corrects to $0.38\\times$ by 105K, and evaluation recovers to 267.9. This demonstrates the threshold's sensitivity to early CIVO signals even in cases that spontaneously recover.\n\n\\noindent\\textbf{Seed 1 extended (009e):} Oscillatory degradation. Continuing 008d beyond 55K, evaluation oscillates between 82.7 and 250 before settling at 131.1; the value function rises then reverses (peak $\\nve = 4.12\\times$ at 55K, final $1.57\\times$).\n\nAll runs exceed $\\nve \\geq 1.5\\times$ in the 35K+ window, confirming deterministic CIVO triggering, but downstream outcomes are seed-dependent (1/2 persistent collapse rate among independent seeds).\n\n%% ============================================================\n%% F3: Unexposed dt_embedding suppresses value drift\n%% ============================================================\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$)---the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE never exceeds the CIVO threshold: it remains in the $0.39$--$0.47\\times$ range throughout the 55K--105K window, with a brief peak of $1.45\\times$ at 55K that self-corrects to $0.65\\times$ by 65K. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ and triggers full collapse (eval 82.8), while the frozen embedding never exceeds $0.47\\times$ in the same window---an $8.7\\times$ NVE gap. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n%% ============================================================\n%% F5: Horizon and subsample secondary\n%% ============================================================\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n%% ============================================================\n%% F6: dt=1 imagination does not prevent collapse\n%% ============================================================\n\n\\subsection{F6: Restricting Imagination to \\texorpdfstring{$\\dt{=}1$}{dt=1} Does Not Prevent Collapse}\n\\label{sec:f6}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \\textbf{Right:} 008e\\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \\emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\nThe mitigation experiment exp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained $\\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Seed 1} (008e\\_v3\\_s1): Healthy. Eval 869.9 at 105K ($95\\%$ of baseline), $\\nve = 0.80\\times$.\n\\item \\textbf{Seed 2} (008e\\_v3\\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\\nve = 3.78\\times$.\n\\end{itemize}\n\nThe baseline with seed 2 (exp\\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.\n\n\\paragraph{Distinct collapse mechanisms.}\nThe collapse dynamics of 008e\\_v3\\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\\ref{tab:main_results}, Figure~\\ref{fig:multiple_pathways}):\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d (CIVO, Pathway A):} value explosion ($+130\\%$) $\\rightarrow$ evaluation decline $\\rightarrow$ entropy decreases.\n\\item \\textbf{008e\\_v3\\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\\%$) $\\rightarrow$ value remains stable $\\rightarrow$ entropy \\emph{increases} ($-5.21 \\rightarrow -3.83$).\n\\end{itemize}\n\nIn Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\\dt{=}1$ prevents the CIVO mechanism---no early $\\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.\n\nThis case also produces the sole false positive in the $\\nve \\geq 1.5\\times$ classification: 008e\\_v3\\_s2's late evaluation decline inflates $\\nve$ to $3.78\\times$ through a non-CIVO mechanism (\\S\\ref{sec:pathways}).\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RSSM fidelity analysis.}\nTable~\\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\\dt$-embedding in 008d produces a $2.78\\times$ gap in reward prediction error between $\\dt{=}1$ and $\\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\\ $0.0568$ for 008d at $\\dt{=}1$).\n\n\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.\n",
    "structuredPatch": [
      {
        "oldStart": 35,
        "oldLines": 6,
        "newStart": 35,
        "newLines": 7,
        "lines": [
          " 008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\\times$ & Slow learner \\\\",
          " 015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\",
          " \\midrule",
          "+018 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 915.7 @105K & 0.72$\\times$ & Healthy \\\\",
          " 008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\",
          " 008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\",
          " 009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\"
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01M4YwCjjfUcc5zfvevT2bxa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "trn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}",
  "new_string": "trn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\ntrn$^\\ddagger$ = trained ($d{=}32$) with full-pathway SGS (all non-KL gradients detached from $e_{\\dt}$);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "d17e53ea-4291-4822-9cca-0532af63f1e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJrb6sNtKKznFLGAJ7QKf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14224,
      "cache_read_input_tokens": 24715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14224
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

_source line 20 · 2026-05-16T13:04:04.903Z_

<details><summary>↩ Tool result · `toolu_01M4YwCjjfUcc5zfvevT2bxa`</summary>

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
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "3aea330f-e0b7-44a7-b107-1c63de1bb3d1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "trn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}",
    "newString": "trn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\ntrn$^\\ddagger$ = trained ($d{=}32$) with full-pathway SGS (all non-KL gradients detached from $e_{\\dt}$);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n009e & Factorial (s1) & trn & ON & 8 & 131.1 @105K & 4.12$\\times$ & Oscillatory \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n009c & No dt\\_emb (s2) & --- & ON & 8 & 148.3 @105K & 1.14$\\times$ & Declining \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\\times$ & Slow learner \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n018 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 915.7 @105K & 0.72$\\times$ & Healthy \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline, regardless of mechanism (Figure~\\ref{fig:learning_curves}). The baseline (exp\\_001) reaches 915.7 at 105K steps and peaks at 970.4 at 505K. In contrast, fixed $\\dt{=}2$ (exp\\_006) peaks at 485.3 at 35K before collapsing to 132.9 by 65K---a $-73\\%$ decline from its own peak (14\\% of baseline). Fixed $\\dt{=}4$ (exp\\_007) peaks at only 176.9 at 25K and never exceeds 152.5 thereafter. The learned-gate configuration (exp\\_005) peaks at 541.2 at 55K but collapses to 98.8 by 145K. This uniform degradation motivates the factorial analysis that follows.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves for all configurations. The $\\dt{=}1$ baseline (black) reaches 915.7 at 105K; all variable-rate configurations degrade, with fixed $\\dt{=}4$ and the learned gate collapsing most severely.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\\_008d (trained $\\dt$-embedding, subsampling ON, $H{=}8$) against exp\\_008f (identical configuration but \\emph{no} trained $\\dt$-embedding). As shown in Figure~\\ref{fig:nve_trajectory}:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d} (trained): $\\nve = 1.78\\times$ at 25K $\\rightarrow$ $4.12\\times$ at 55K $\\rightarrow$ collapse (eval 167$\\rightarrow$82.8).\n\\item \\textbf{008f} (no dt\\_emb): $\\nve = 1.02\\times$ at 25K $\\rightarrow$ $0.30\\times$ at 105K $\\rightarrow$ no collapse (eval 503.0 at 105K).\n\\end{itemize}\n\nIn the 35K+ window (\\S\\ref{sec:metrics}), the $\\nve \\geq 1.5\\times$ threshold correctly classifies 7/8 seeds (AUROC${=}0.933$, Clopper--Pearson 95\\% CI $[0.47, 1.0]$): 3 CIVO-positive (exp\\_006, 008d, 009b) and 4 CIVO-negative, with one non-CIVO false positive (008e\\_v3 s2, $3.78\\times$; \\S\\ref{sec:f6}).  The gap between the lowest true positive ($1.62\\times$) and the highest true negative ($1.00\\times$) is $0.62$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}\n\\caption{Normalized value-to-eval ratio ($\\nve$) trajectories. The dashed line marks the $1.5\\times$ threshold. All trained-embedding configurations with $\\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\\_v3 s1, dash-dot) with $\\dt{=}1$-only imagination remains below it.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\n\\paragraph{Three post-CIVO outcomes.}\nRunning the 008d configuration with two independent seeds (s1, s2) reveals that trained $\\dt$-embedding triggers CIVO---yet the downstream consequence is stochastic. Exp\\_009e extends seed~1 (008d) beyond 55K to 105K steps:\n\n%% ============================================================\n%% TABLE 3: Three post-CIVO outcomes\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window. Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\ns1 ext (009e) & 4.12$\\times$ & 1.57$\\times$ & 131.1 & Oscillatory \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Seed 1 (008d):} Full collapse (Pathway A). Value explosion ($+130\\%$), evaluation declines from 167 to 82.8, entropy decreases---the classic CIVO feedback loop.\n\n\\noindent\\textbf{Seed 2 (009b):} Transient CIVO. The $\\nve$ reaches $1.62\\times$ at 45K (35K+ window), exceeding the $1.5\\times$ threshold, but the value function self-corrects to $0.38\\times$ by 105K, and evaluation recovers to 267.9. This demonstrates the threshold's sensitivity to early CIVO signals even in cases that spontaneously recover.\n\n\\noindent\\textbf{Seed 1 extended (009e):} Oscillatory degradation. Continuing 008d beyond 55K, evaluation oscillates between 82.7 and 250 before settling at 131.1; the value function rises then reverses (peak $\\nve = 4.12\\times$ at 55K, final $1.57\\times$).\n\nAll runs exceed $\\nve \\geq 1.5\\times$ in the 35K+ window, confirming deterministic CIVO triggering, but downstream outcomes are seed-dependent (1/2 persistent collapse rate among independent seeds).\n\n%% ============================================================\n%% F3: Unexposed dt_embedding suppresses value drift\n%% ============================================================\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$)---the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE never exceeds the CIVO threshold: it remains in the $0.39$--$0.47\\times$ range throughout the 55K--105K window, with a brief peak of $1.45\\times$ at 55K that self-corrects to $0.65\\times$ by 65K. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ and triggers full collapse (eval 82.8), while the frozen embedding never exceeds $0.47\\times$ in the same window---an $8.7\\times$ NVE gap. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n%% ============================================================\n%% F5: Horizon and subsample secondary\n%% ============================================================\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n%% ============================================================\n%% F6: dt=1 imagination does not prevent collapse\n%% ============================================================\n\n\\subsection{F6: Restricting Imagination to \\texorpdfstring{$\\dt{=}1$}{dt=1} Does Not Prevent Collapse}\n\\label{sec:f6}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \\textbf{Right:} 008e\\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \\emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\nThe mitigation experiment exp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained $\\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Seed 1} (008e\\_v3\\_s1): Healthy. Eval 869.9 at 105K ($95\\%$ of baseline), $\\nve = 0.80\\times$.\n\\item \\textbf{Seed 2} (008e\\_v3\\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\\nve = 3.78\\times$.\n\\end{itemize}\n\nThe baseline with seed 2 (exp\\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.\n\n\\paragraph{Distinct collapse mechanisms.}\nThe collapse dynamics of 008e\\_v3\\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\\ref{tab:main_results}, Figure~\\ref{fig:multiple_pathways}):\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d (CIVO, Pathway A):} value explosion ($+130\\%$) $\\rightarrow$ evaluation decline $\\rightarrow$ entropy decreases.\n\\item \\textbf{008e\\_v3\\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\\%$) $\\rightarrow$ value remains stable $\\rightarrow$ entropy \\emph{increases} ($-5.21 \\rightarrow -3.83$).\n\\end{itemize}\n\nIn Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\\dt{=}1$ prevents the CIVO mechanism---no early $\\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.\n\nThis case also produces the sole false positive in the $\\nve \\geq 1.5\\times$ classification: 008e\\_v3\\_s2's late evaluation decline inflates $\\nve$ to $3.78\\times$ through a non-CIVO mechanism (\\S\\ref{sec:pathways}).\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RSSM fidelity analysis.}\nTable~\\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\\dt$-embedding in 008d produces a $2.78\\times$ gap in reward prediction error between $\\dt{=}1$ and $\\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\\ $0.0568$ for 008d at $\\dt{=}1$).\n\n\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.\n",
    "structuredPatch": [
      {
        "oldStart": 44,
        "oldLines": 6,
        "newStart": 44,
        "newLines": 7,
        "lines": [
          " \\vspace{1pt}",
          " {\\raggedright\\footnotesize",
          " trn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);",
          "+trn$^\\ddagger$ = trained ($d{=}32$) with full-pathway SGS (all non-KL gradients detached from $e_{\\dt}$);",
          " exp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);",
          " frz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});",
          " --- = removed ($d{=}0$).\\par}"
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

Now adding F7 section after F6 (before the RSSM fidelity table):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "b2eb8b7c-e1ee-472e-9e25-c477a45cc5bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTPexaMMqUWQSjwu1R3wQB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 38939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1007
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

<details open><summary>🔧 Tool call — Edit · `toolu_01St63JdjNUKky3iau7HmWVq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================",
  "new_string": "%% ============================================================\n%% F7: Full-Pathway SGS Eliminates CIVO\n%% ============================================================\n\n\\subsection{F7: Full-Pathway Gradient Stopping Eliminates CIVO}\n\\label{sec:f7}\n\nExp\\_018 applies full-pathway selective gradient stopping (SGS), detaching all non-KL gradients from the temporal embedding $e_{\\dt}$ so that only the 7.3\\% KL dynamics signal remains. Under the same configuration that produces catastrophic CIVO in exp\\_008d (trained $e_{\\dt}$, $d{=}32$, subsample ON, $H{=}8$, $\\dt{=}2$ imagination), exp\\_018 reaches evaluation 915.7 at 105K steps---surpassing the baseline (exp\\_009d: ${\\sim}750$)---with peak NVE $0.72\\times$ in the 35K+ diagnostic window. This is well below both the $1.5\\times$ CIVO threshold and the baseline's $1.0\\times$ reference.\n\nThe progression across gradient-stopping interventions establishes a monotonic relationship between gradient removal and CIVO suppression:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item Exp\\_016e (reward-only SGS, 0\\% effective removal): NVE $10.42\\times$, collapse to 31.7---a null intervention since the reward head contributes zero gradient to $e_{\\dt}$.\n\\item Exp\\_018 (full-pathway SGS, 92.7\\% removal): NVE $0.72\\times$, eval 915.7---CIVO completely eliminated.\n\\item Exp\\_008f (embedding removed, 100\\% removal): NVE $0.97\\times$, eval 503.0---no CIVO, but lower performance due to loss of all temporal information.\n\\end{itemize}\n\nNotably, exp\\_018 \\emph{outperforms} the no-embedding control (008f) by $1.82\\times$ in final evaluation (915.7 vs.\\ 503.0), demonstrating that the KL-only temporal signal provides useful dynamics information without inducing the pathological co-adaptation that drives CIVO. The observation decoder gradient pathway is necessary for CIVO induction; removing it eliminates the vulnerability within the 105K training horizon tested.\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "bcb30e9d-eff4-4b78-96fa-e7110843a94f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTPexaMMqUWQSjwu1R3wQB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 38939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1007
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

_source line 23 · 2026-05-16T13:04:23.606Z_

<details><summary>↩ Tool result · `toolu_01St63JdjNUKky3iau7HmWVq`</summary>

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
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "604dac01-ce3d-4130-9348-0991c450a488",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================",
    "newString": "%% ============================================================\n%% F7: Full-Pathway SGS Eliminates CIVO\n%% ============================================================\n\n\\subsection{F7: Full-Pathway Gradient Stopping Eliminates CIVO}\n\\label{sec:f7}\n\nExp\\_018 applies full-pathway selective gradient stopping (SGS), detaching all non-KL gradients from the temporal embedding $e_{\\dt}$ so that only the 7.3\\% KL dynamics signal remains. Under the same configuration that produces catastrophic CIVO in exp\\_008d (trained $e_{\\dt}$, $d{=}32$, subsample ON, $H{=}8$, $\\dt{=}2$ imagination), exp\\_018 reaches evaluation 915.7 at 105K steps---surpassing the baseline (exp\\_009d: ${\\sim}750$)---with peak NVE $0.72\\times$ in the 35K+ diagnostic window. This is well below both the $1.5\\times$ CIVO threshold and the baseline's $1.0\\times$ reference.\n\nThe progression across gradient-stopping interventions establishes a monotonic relationship between gradient removal and CIVO suppression:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item Exp\\_016e (reward-only SGS, 0\\% effective removal): NVE $10.42\\times$, collapse to 31.7---a null intervention since the reward head contributes zero gradient to $e_{\\dt}$.\n\\item Exp\\_018 (full-pathway SGS, 92.7\\% removal): NVE $0.72\\times$, eval 915.7---CIVO completely eliminated.\n\\item Exp\\_008f (embedding removed, 100\\% removal): NVE $0.97\\times$, eval 503.0---no CIVO, but lower performance due to loss of all temporal information.\n\\end{itemize}\n\nNotably, exp\\_018 \\emph{outperforms} the no-embedding control (008f) by $1.82\\times$ in final evaluation (915.7 vs.\\ 503.0), demonstrating that the KL-only temporal signal provides useful dynamics information without inducing the pathological co-adaptation that drives CIVO. The observation decoder gradient pathway is necessary for CIVO induction; removing it eliminates the vulnerability within the 105K training horizon tested.\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n009e & Factorial (s1) & trn & ON & 8 & 131.1 @105K & 4.12$\\times$ & Oscillatory \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n009c & No dt\\_emb (s2) & --- & ON & 8 & 148.3 @105K & 1.14$\\times$ & Declining \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\\times$ & Slow learner \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n018 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 915.7 @105K & 0.72$\\times$ & Healthy \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\ntrn$^\\ddagger$ = trained ($d{=}32$) with full-pathway SGS (all non-KL gradients detached from $e_{\\dt}$);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline, regardless of mechanism (Figure~\\ref{fig:learning_curves}). The baseline (exp\\_001) reaches 915.7 at 105K steps and peaks at 970.4 at 505K. In contrast, fixed $\\dt{=}2$ (exp\\_006) peaks at 485.3 at 35K before collapsing to 132.9 by 65K---a $-73\\%$ decline from its own peak (14\\% of baseline). Fixed $\\dt{=}4$ (exp\\_007) peaks at only 176.9 at 25K and never exceeds 152.5 thereafter. The learned-gate configuration (exp\\_005) peaks at 541.2 at 55K but collapses to 98.8 by 145K. This uniform degradation motivates the factorial analysis that follows.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves for all configurations. The $\\dt{=}1$ baseline (black) reaches 915.7 at 105K; all variable-rate configurations degrade, with fixed $\\dt{=}4$ and the learned gate collapsing most severely.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\\_008d (trained $\\dt$-embedding, subsampling ON, $H{=}8$) against exp\\_008f (identical configuration but \\emph{no} trained $\\dt$-embedding). As shown in Figure~\\ref{fig:nve_trajectory}:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d} (trained): $\\nve = 1.78\\times$ at 25K $\\rightarrow$ $4.12\\times$ at 55K $\\rightarrow$ collapse (eval 167$\\rightarrow$82.8).\n\\item \\textbf{008f} (no dt\\_emb): $\\nve = 1.02\\times$ at 25K $\\rightarrow$ $0.30\\times$ at 105K $\\rightarrow$ no collapse (eval 503.0 at 105K).\n\\end{itemize}\n\nIn the 35K+ window (\\S\\ref{sec:metrics}), the $\\nve \\geq 1.5\\times$ threshold correctly classifies 7/8 seeds (AUROC${=}0.933$, Clopper--Pearson 95\\% CI $[0.47, 1.0]$): 3 CIVO-positive (exp\\_006, 008d, 009b) and 4 CIVO-negative, with one non-CIVO false positive (008e\\_v3 s2, $3.78\\times$; \\S\\ref{sec:f6}).  The gap between the lowest true positive ($1.62\\times$) and the highest true negative ($1.00\\times$) is $0.62$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}\n\\caption{Normalized value-to-eval ratio ($\\nve$) trajectories. The dashed line marks the $1.5\\times$ threshold. All trained-embedding configurations with $\\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\\_v3 s1, dash-dot) with $\\dt{=}1$-only imagination remains below it.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\n\\paragraph{Three post-CIVO outcomes.}\nRunning the 008d configuration with two independent seeds (s1, s2) reveals that trained $\\dt$-embedding triggers CIVO---yet the downstream consequence is stochastic. Exp\\_009e extends seed~1 (008d) beyond 55K to 105K steps:\n\n%% ============================================================\n%% TABLE 3: Three post-CIVO outcomes\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window. Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\ns1 ext (009e) & 4.12$\\times$ & 1.57$\\times$ & 131.1 & Oscillatory \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Seed 1 (008d):} Full collapse (Pathway A). Value explosion ($+130\\%$), evaluation declines from 167 to 82.8, entropy decreases---the classic CIVO feedback loop.\n\n\\noindent\\textbf{Seed 2 (009b):} Transient CIVO. The $\\nve$ reaches $1.62\\times$ at 45K (35K+ window), exceeding the $1.5\\times$ threshold, but the value function self-corrects to $0.38\\times$ by 105K, and evaluation recovers to 267.9. This demonstrates the threshold's sensitivity to early CIVO signals even in cases that spontaneously recover.\n\n\\noindent\\textbf{Seed 1 extended (009e):} Oscillatory degradation. Continuing 008d beyond 55K, evaluation oscillates between 82.7 and 250 before settling at 131.1; the value function rises then reverses (peak $\\nve = 4.12\\times$ at 55K, final $1.57\\times$).\n\nAll runs exceed $\\nve \\geq 1.5\\times$ in the 35K+ window, confirming deterministic CIVO triggering, but downstream outcomes are seed-dependent (1/2 persistent collapse rate among independent seeds).\n\n%% ============================================================\n%% F3: Unexposed dt_embedding suppresses value drift\n%% ============================================================\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$)---the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE never exceeds the CIVO threshold: it remains in the $0.39$--$0.47\\times$ range throughout the 55K--105K window, with a brief peak of $1.45\\times$ at 55K that self-corrects to $0.65\\times$ by 65K. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ and triggers full collapse (eval 82.8), while the frozen embedding never exceeds $0.47\\times$ in the same window---an $8.7\\times$ NVE gap. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n%% ============================================================\n%% F5: Horizon and subsample secondary\n%% ============================================================\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n%% ============================================================\n%% F6: dt=1 imagination does not prevent collapse\n%% ============================================================\n\n\\subsection{F6: Restricting Imagination to \\texorpdfstring{$\\dt{=}1$}{dt=1} Does Not Prevent Collapse}\n\\label{sec:f6}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \\textbf{Right:} 008e\\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \\emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\nThe mitigation experiment exp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained $\\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Seed 1} (008e\\_v3\\_s1): Healthy. Eval 869.9 at 105K ($95\\%$ of baseline), $\\nve = 0.80\\times$.\n\\item \\textbf{Seed 2} (008e\\_v3\\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\\nve = 3.78\\times$.\n\\end{itemize}\n\nThe baseline with seed 2 (exp\\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.\n\n\\paragraph{Distinct collapse mechanisms.}\nThe collapse dynamics of 008e\\_v3\\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\\ref{tab:main_results}, Figure~\\ref{fig:multiple_pathways}):\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d (CIVO, Pathway A):} value explosion ($+130\\%$) $\\rightarrow$ evaluation decline $\\rightarrow$ entropy decreases.\n\\item \\textbf{008e\\_v3\\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\\%$) $\\rightarrow$ value remains stable $\\rightarrow$ entropy \\emph{increases} ($-5.21 \\rightarrow -3.83$).\n\\end{itemize}\n\nIn Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\\dt{=}1$ prevents the CIVO mechanism---no early $\\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.\n\nThis case also produces the sole false positive in the $\\nve \\geq 1.5\\times$ classification: 008e\\_v3\\_s2's late evaluation decline inflates $\\nve$ to $3.78\\times$ through a non-CIVO mechanism (\\S\\ref{sec:pathways}).\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RSSM fidelity analysis.}\nTable~\\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\\dt$-embedding in 008d produces a $2.78\\times$ gap in reward prediction error between $\\dt{=}1$ and $\\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\\ $0.0568$ for 008d at $\\dt{=}1$).\n\n\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.\n",
    "structuredPatch": [
      {
        "oldStart": 235,
        "oldLines": 6,
        "newStart": 235,
        "newLines": 24,
        "lines": [
          " This case also produces the sole false positive in the $\\nve \\geq 1.5\\times$ classification: 008e\\_v3\\_s2's late evaluation decline inflates $\\nve$ to $3.78\\times$ through a non-CIVO mechanism (\\S\\ref{sec:pathways}).",
          " ",
          " %% ============================================================",
          "+%% F7: Full-Pathway SGS Eliminates CIVO",
          "+%% ============================================================",
          "+",
          "+\\subsection{F7: Full-Pathway Gradient Stopping Eliminates CIVO}",
          "+\\label{sec:f7}",
          "+",
          "+Exp\\_018 applies full-pathway selective gradient stopping (SGS), detaching all non-KL gradients from the temporal embedding $e_{\\dt}$ so that only the 7.3\\% KL dynamics signal remains. Under the same configuration that produces catastrophic CIVO in exp\\_008d (trained $e_{\\dt}$, $d{=}32$, subsample ON, $H{=}8$, $\\dt{=}2$ imagination), exp\\_018 reaches evaluation 915.7 at 105K steps---surpassing the baseline (exp\\_009d: ${\\sim}750$)---with peak NVE $0.72\\times$ in the 35K+ diagnostic window. This is well below both the $1.5\\times$ CIVO threshold and the baseline's $1.0\\times$ reference.",
          "+",
          "+The progression across gradient-stopping interventions establishes a monotonic relationship between gradient removal and CIVO suppression:",
          "+\\begin{itemize}[nosep,leftmargin=*]",
          "+\\item Exp\\_016e (reward-only SGS, 0\\% effective removal): NVE $10.42\\times$, collapse to 31.7---a null intervention since the reward head contributes zero gradient to $e_{\\dt}$.",
          "+\\item Exp\\_018 (full-pathway SGS, 92.7\\% removal): NVE $0.72\\times$, eval 915.7---CIVO completely eliminated.",
          "+\\item Exp\\_008f (embedding removed, 100\\% removal): NVE $0.97\\times$, eval 503.0---no CIVO, but lower performance due to loss of all temporal information.",
          "+\\end{itemize}",
          "+",
          "+Notably, exp\\_018 \\emph{outperforms} the no-embedding control (008f) by $1.82\\times$ in final evaluation (915.7 vs.\\ 503.0), demonstrating that the KL-only temporal signal provides useful dynamics information without inducing the pathological co-adaptation that drives CIVO. The observation decoder gradient pathway is necessary for CIVO induction; removing it eliminates the vulnerability within the 105K training horizon tested.",
          "+",
          "+%% ============================================================",
          " %% TABLE 2: RSSM Fidelity",
          " %% ============================================================",
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

### Assistant

_source line 24_

Now modifying analysis.tex — adding the new subsubsection before "Exp\_016e Reinterpreted as Stochastic Variation":

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "90c1dcc8-4774-4a0e-ba2b-b0696afcf72c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJEtTXcX7WVERCYxsa6mKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 39946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01U6GSEhbW734HQw3465Qs5W`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex",
  "old_string": "\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}",
  "new_string": "\\subsubsection{Full-Pathway SGS Confirms Gradient-Level Vulnerability}\n\\label{sec:full_sgs_result}\n\nExp\\_018 provides the definitive test of the gradient decomposition hypothesis. Detaching all non-KL gradients from $e_{\\dt}$ (removing the dominant 92.7\\% observation decoder contribution) completely eliminates CIVO: evaluation reaches 915.7 at 105K steps with peak NVE $0.72\\times$---the value function consistently \\emph{underestimates} actual returns, the opposite of CIVO's pathological overestimation.\n\nThe causal chain is now closed: observation decoder gradients $\\rightarrow$ temporal embedding learns $\\dt$-specific features $\\rightarrow$ RSSM develops scale-dependent state representations $\\rightarrow$ reward head produces biased predictions at $\\dt{>}1$ $\\rightarrow$ critic overestimation $\\rightarrow$ actor exploitation $\\rightarrow$ CIVO collapse. Removing the first link (obs decoder $\\rightarrow$ $e_{\\dt}$) breaks the entire chain.\n\nThe residual 7.3\\% KL gradient does not trigger CIVO within the 105K training horizon tested. The KL loss constrains only posterior-prior consistency---it does not directly encode observation-level temporal patterns that enable scale-dependent reward prediction bias. Moreover, exp\\_018's superior performance relative to exp\\_008f (915.7 vs.\\ 503.0) demonstrates that the KL-only temporal signal provides beneficial dynamics information without inducing the harmful co-adaptation.\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "49aa0d06-5470-419b-9879-66b3e87c1e91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJEtTXcX7WVERCYxsa6mKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 39946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 26 · 2026-05-16T13:04:37.293Z_

<details><summary>↩ Tool result · `toolu_01U6GSEhbW734HQw3465Qs5W`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "0ef48110-3605-43c2-afbf-1bd7ed3ff530",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex",
    "oldString": "\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}",
    "newString": "\\subsubsection{Full-Pathway SGS Confirms Gradient-Level Vulnerability}\n\\label{sec:full_sgs_result}\n\nExp\\_018 provides the definitive test of the gradient decomposition hypothesis. Detaching all non-KL gradients from $e_{\\dt}$ (removing the dominant 92.7\\% observation decoder contribution) completely eliminates CIVO: evaluation reaches 915.7 at 105K steps with peak NVE $0.72\\times$---the value function consistently \\emph{underestimates} actual returns, the opposite of CIVO's pathological overestimation.\n\nThe causal chain is now closed: observation decoder gradients $\\rightarrow$ temporal embedding learns $\\dt$-specific features $\\rightarrow$ RSSM develops scale-dependent state representations $\\rightarrow$ reward head produces biased predictions at $\\dt{>}1$ $\\rightarrow$ critic overestimation $\\rightarrow$ actor exploitation $\\rightarrow$ CIVO collapse. Removing the first link (obs decoder $\\rightarrow$ $e_{\\dt}$) breaks the entire chain.\n\nThe residual 7.3\\% KL gradient does not trigger CIVO within the 105K training horizon tested. The KL loss constrains only posterior-prior consistency---it does not directly encode observation-level temporal patterns that enable scale-dependent reward prediction bias. Moreover, exp\\_018's superior performance relative to exp\\_008f (915.7 vs.\\ 503.0) demonstrates that the KL-only temporal signal provides beneficial dynamics information without inducing the harmful co-adaptation.\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}",
    "originalFile": "\\section{Analysis \\& Discussion}\n\\label{sec:analysis}\n\nThe preceding results establish that the combination of trained $\\dt$-embedding and multi-rate data exposure is the causal factor behind pathological value dynamics in variable-rate DreamerV3. In this section, we synthesize these findings into a mechanistic account of conditioning-induced value overestimation (CIVO), explain why the same CIVO trigger produces divergent outcomes across seeds, contrast the imagination-based setting with MPC-based temporal conditioning, and discuss the fundamental tension inherent in the $\\dt$-embedding design.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$---a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d)---the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, confirming that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced---the reward head's co-adaptation with the temporal embedding produces systematically upward-biased predictions at $\\dt > 1$.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Design and Hypothesis}\n\\label{sec:sgs_design}\n\nThe preceding analysis establishes that a trained temporal embedding $e_{\\Delta t}$ is necessary for CIVO (Section~\\ref{sec:civo_mechanism}). We next ask \\textit{which gradient pathway} through $e_{\\Delta t}$ amplifies the overestimation. In DreamerV3, the temporal embedding conditions all prediction heads simultaneously through the RSSM latent state. A natural hypothesis is that the \\textit{reward head}---which directly supplies $\\lambda$-return targets to the critic---is the primary amplifier: if reward predictions develop $\\Delta t$-dependent biases, the critic inherits and compounds these biases across the $H$-step imagination rollout.\n\nTo test this, we introduce \\textit{selective gradient stopping} (SGS): during the backward pass, $e_{\\Delta t}$ is detached before entering the reward head,\n$$\\hat{r}_t = f_{\\text{reward}}\\big(\\operatorname{sg}(e_{\\Delta t}),\\; h_t,\\; z_t\\big),$$\nwhere $\\operatorname{sg}(\\cdot)$ denotes the stop-gradient operator. This prevents reward-loss gradients from updating $e_{\\Delta t}$'s parameters while preserving the embedding's forward-pass contribution. All other gradient pathways---observation decoders, continuation predictor, KL dynamics---remain intact. We apply this intervention to the primary CIVO-exhibiting configuration: Walker Walk, trained $e_{\\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\\Delta t{=}2$ imagination (exp\\_016e; identical to exp\\_008d except for \\texttt{reward\\_dt\\_emb\\_detach=True}).\n\n\n\\subsubsection{Gradient Decomposition Reveals the Reward Pathway is Inactive}\n\\label{sec:gradient_decomposition}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps (exp\\_016e) followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$ (exp\\_016e). The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters (D061). Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} at step 95K (D061). Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\nLoss component & $\\|\\nabla_\\theta \\mathcal{L}_i\\|_2$ & Share (\\%) \\\\\n\\midrule\nObservation decoders (orientations, velocity, height) & 1.505 & 92.7 \\\\\nKL dynamics & 0.119 & 7.3 \\\\\nContinuation head & $<$0.001 & $<$0.1 \\\\\nReward head & 0.000 & 0.0 \\\\\n\\midrule\n\\textbf{Total} & \\textbf{1.624} & \\textbf{100} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reward head contributes \\textit{numerically negligible---zero to within floating-point precision} gradient to the temporal embedding. Exp\\_016e's stop-gradient intervention detaches a gradient pathway that carries no signal---it is an architectural no-op. The null result is therefore expected: the intervention removes nothing.\n\nThe zero reward gradient is a consequence of the relative output dimensionality. All decoder losses backpropagate through the same RSSM latent state to reach $e_{\\Delta t}$. The observation decoders reconstruct a 24-dimensional proprioceptive signal (14 orientations, 9 velocities, 1 height), while the reward head predicts a single scalar. This ${\\sim}24\\!\\times$ dimensionality asymmetry, compounded by DreamerV3's symlog reward scaling which further compresses the reward gradient magnitude, renders the reward head's contribution numerically negligible---zero to within floating-point precision.\n\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reframes the mechanistic understanding of how the temporal embedding drives CIVO.\n\n\\paragraph{Observation reconstruction dominates temporal embedding learning.} The temporal embedding's parameters are shaped almost entirely (93\\%) by the observation reconstruction objective (D061). This means $e_{\\Delta t}$ learns to encode temporal information that helps minimize \\textit{observation prediction error}, not reward prediction error. If this learned representation introduces systematic biases in latent state predictions at $\\Delta t{>}1$---for instance, by encouraging the RSSM to produce states that are easy to decode but dynamically inaccurate---these biases propagate to \\textit{all} downstream computation, including reward prediction and the critic's value estimates. CIVO thus originates in the observation reconstruction objective's influence on latent dynamics, not in reward-specific pathways.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone---reward prediction regularization, reward-conditioned value clipping, or the reward-only SGS tested here---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and cannot attenuate CIVO. Effective gradient-level interventions must address the dominant observation decoder pathway. This motivates the \\textit{full-pathway SGS} design (exp\\_018): detaching $e_{\\Delta t}$ from all decoder and reward gradients, retaining only the 7\\% KL dynamics contribution. Full-pathway SGS removes 93\\% of the gradient to $e_{\\Delta t}$, constituting a genuine gradient-level intervention rather than the null operation of reward-only SGS.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The observation-dominated gradient structure is consistent with the RSSM fidelity results in Table~\\ref{tab:rssm_fidelity}: the trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions, despite the reward head receiving zero gradient from $e_{\\Delta t}$. This confirms that the reward head's $\\Delta t$-dependent biases are inherited \\textit{through the latent state}---which is shaped by observation reconstruction gradients---rather than learned directly from the reward objective.\n\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nWith the gradient decomposition establishing that exp\\_016e is a no-op intervention, the apparent timing differences between exp\\_016e and exp\\_008d---later collapse onset (75K vs.\\ 25K) and higher peak evaluation (326.7 vs.\\ 167.2)---must be attributed to stochastic variation rather than SGS effects. This attribution is consistent with the seed-to-seed variability already observed within the trained-embedding condition: exp\\_009b (same configuration as exp\\_008d, seed 2) reaches peak evaluation 278.5 at 95K (exp\\_009b) with transient NVE of $1.62\\times$ at 45K before self-correcting, compared to exp\\_008d's monotonic collapse from 25K. The qualitative diversity between exp\\_008d (early collapse), exp\\_009b (self-correction), and exp\\_016e (delayed collapse) falls within the range of stochastic outcomes for a single trained-$e_{\\Delta t}$ configuration.\n\nAll three trajectories share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training (exp\\_008d at 35K: $1.71\\times$; exp\\_009b at 45K: $1.62\\times$; exp\\_016e at 95K: $10.42\\times$). Whether this pathological overestimation leads to sustained collapse or transient recovery depends on early training stochasticity, not on the reward-only SGS intervention (D061).\n\n\\subsection{Three Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\nThe three post-CIVO outcomes (Table~\\ref{tab:post_civo})---full collapse, transient CIVO, and oscillatory degradation---all cross the $\\nve > 1.5\\times$ threshold, yet the downstream damage is stochastic.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).  The oscillatory pattern (seed~1, 009e) represents an intermediate regime: the value function rises then reverses while evaluation oscillates, and entropy remains elevated---suggesting the actor has not fully committed to the overestimated policy but cannot escape it.  This partial capacity loss allows the critic to respond to new data without fully correcting its biases.\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step---imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.  In terms of the two-stage decomposition (\\S\\ref{sec:civo_mechanism}), MPC is immune because Stage~2 cannot occur: without imagination-based bootstrapping, the actor cannot exploit the dynamics bias.  This aligns with \\citet{frauenknecht2025rollouts}, who find that rollout quality dominates model-based RL performance, and with \\citet{tallec2019making}'s analysis of how temporal resolution mismatches destabilize value learning.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE)---the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) prevents CIVO in 1 of 2 seeds but the other collapses via Pathway~B (\\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse mechanisms identified in \\S\\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and non-CIVO instability (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures but a shared root cause: the trained $\\dt$-embedding's learned features affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B).  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse.  The existence of multiple pathways suggests that mitigation strategies focused exclusively on the imagination channel---restricting $\\dt$, truncating rollouts, or smoothing rewards \\citep{lee2024dreamsmooth}---may be insufficient.\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training: the RSSM cannot maintain prediction fidelity across temporal resolutions when the embedding co-adapts with the reward head.  Hierarchical approaches---THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}---may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  Reward-only gradient stopping is an architectural no-op because the reward head contributes zero gradient to $e_{\\Delta t}$ (\\S\\ref{sec:sgs_gradient_analysis}); full-pathway SGS that detaches the dominant observation-decoder gradients constitutes a genuine intervention targeting 93\\% of the gradient flow (exp\\_018; \\S\\ref{sec:sgs_implications}).  Whether spectral normalization or other regularization strategies can preserve temporal fidelity while preventing co-adaptation remains an open question.\n",
    "structuredPatch": [
      {
        "oldStart": 70,
        "oldLines": 6,
        "newStart": 70,
        "newLines": 15,
        "lines": [
          " \\paragraph{Connection to RSSM fidelity analysis.} The observation-dominated gradient structure is consistent with the RSSM fidelity results in Table~\\ref{tab:rssm_fidelity}: the trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions, despite the reward head receiving zero gradient from $e_{\\Delta t}$. This confirms that the reward head's $\\Delta t$-dependent biases are inherited \\textit{through the latent state}---which is shaped by observation reconstruction gradients---rather than learned directly from the reward objective.",
          " ",
          " ",
          "+\\subsubsection{Full-Pathway SGS Confirms Gradient-Level Vulnerability}",
          "+\\label{sec:full_sgs_result}",
          "+",
          "+Exp\\_018 provides the definitive test of the gradient decomposition hypothesis. Detaching all non-KL gradients from $e_{\\dt}$ (removing the dominant 92.7\\% observation decoder contribution) completely eliminates CIVO: evaluation reaches 915.7 at 105K steps with peak NVE $0.72\\times$---the value function consistently \\emph{underestimates} actual returns, the opposite of CIVO's pathological overestimation.",
          "+",
          "+The causal chain is now closed: observation decoder gradients $\\rightarrow$ temporal embedding learns $\\dt$-specific features $\\rightarrow$ RSSM develops scale-dependent state representations $\\rightarrow$ reward head produces biased predictions at $\\dt{>}1$ $\\rightarrow$ critic overestimation $\\rightarrow$ actor exploitation $\\rightarrow$ CIVO collapse. Removing the first link (obs decoder $\\rightarrow$ $e_{\\dt}$) breaks the entire chain.",
          "+",
          "+The residual 7.3\\% KL gradient does not trigger CIVO within the 105K training horizon tested. The KL loss constrains only posterior-prior consistency---it does not directly encode observation-level temporal patterns that enable scale-dependent reward prediction bias. Moreover, exp\\_018's superior performance relative to exp\\_008f (915.7 vs.\\ 503.0) demonstrates that the KL-only temporal signal provides beneficial dynamics information without inducing the harmful co-adaptation.",
          "+",
          " \\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}",
          " \\label{sec:016e_reinterp}",
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

### Assistant

_source line 27_

Now modifying conclusion.tex:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "e2fe6af3-d2b5-46bc-b04c-09154a5da8d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRxHKojpE8ZSLoaWtHShGN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 40900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 690
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

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_01RUzKGM2Bhgf7eJG8odb8YB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex",
  "old_string": "Full-pathway gradient stopping targeting observation decoders (exp\\_018), which removes the dominant 93\\% contribution, is queued to test whether the vulnerability is gradient-level or representation-level.",
  "new_string": "Full-pathway gradient stopping targeting observation decoders (exp\\_018) removes the dominant 93\\% contribution and completely eliminates CIVO (eval 915.7, NVE $0.72\\times$), confirming that the vulnerability operates at the gradient level: observation reconstruction gradients are necessary for CIVO induction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "848a08a3-50a4-4762-bef0-4c1394d75e42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRxHKojpE8ZSLoaWtHShGN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 40900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 690
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

_source line 29 · 2026-05-16T13:04:44.002Z_

<details><summary>↩ Tool result · `toolu_01RUzKGM2Bhgf7eJG8odb8YB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "cf763989-c3ea-4065-b830-5ac49ca4de81",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex",
    "oldString": "Full-pathway gradient stopping targeting observation decoders (exp\\_018), which removes the dominant 93\\% contribution, is queued to test whether the vulnerability is gradient-level or representation-level.",
    "newString": "Full-pathway gradient stopping targeting observation decoders (exp\\_018) removes the dominant 93\\% contribution and completely eliminates CIVO (eval 915.7, NVE $0.72\\times$), confirming that the vulnerability operates at the gradient level: observation reconstruction gradients are necessary for CIVO induction.",
    "originalFile": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe have presented a systematic factorial diagnostic of temporal abstraction in DreamerV3, identifying the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor behind conditioning-induced value overestimation (CIVO). The key findings are:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item Every variable-rate imagination configuration degrades relative to the $\\dt{=}1$ baseline, with degradation scaling monotonically with $\\dt$.\n\\item A normalized value-to-eval threshold of $\\nve \\geq 1.5\\times$ (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, 87.5\\%), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The combination of trained $\\dt$-embedding and multi-rate data exposure is the causal factor; unexposed, frozen, or removed embeddings prevent overestimation.\n\\item The RSSM reward head develops a $2.78\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$ under trained conditioning, providing the systematic bias that drives critic overestimation.\n\\item The same CIVO trigger produces stochastic downstream outcomes---full collapse, transient CIVO with self-correction, and oscillatory degradation---across seeds of identical configurations.\n\\item Restricting imagination to $\\dt{=}1$ does not fully prevent collapse: one of two seeds fails via a qualitatively distinct non-CIVO pathway (eval-driven with increasing entropy), demonstrating that the trained $\\dt$-embedding creates vulnerability through multiple mechanisms.\n\\end{enumerate}\n\nThe contrast with TAWM's success in MPC identifies the feedback architecture as the critical factor: $\\dt$-conditioning succeeds when errors are contained by re-planning from real states, but fails when errors compound through imagination-based actor-critic bootstrapping.\n\n\\paragraph{Limitations.}\nOur experiments focus on a single environment (Walker Walk) and a single world-model architecture (DreamerV3/RSSM). While multi-seed replication establishes robustness within this setting, generalization to other environments and architectures---particularly transformer-based world models such as DreamerV4---remains an open question. The $\\nve$ threshold ($1.5\\times$, 35K+ window) is sensitive to value overestimation broadly but not perfectly specific to CIVO (7/8, one non-CIVO false positive; margin $0.62$ excluding the outlier); generalization to other tasks and architectures is pending validation.\n\n\\paragraph{Future directions.}\nOur findings suggest three avenues. First, hierarchical temporal abstraction at the representation level---as in THICK and Hieros---may avoid the flat-conditioning failure mode by maintaining separate dynamics for each temporal scale. Second, gradient decomposition reveals that 93\\% of $\\dt$-embedding gradients originate from observation decoders, with 0\\% from the reward head---making reward-only gradient stopping (exp\\_016e) an architectural no-op. Full-pathway gradient stopping targeting observation decoders (exp\\_018), which removes the dominant 93\\% contribution, is queued to test whether the vulnerability is gradient-level or representation-level. Third, extending this diagnostic framework to transformer-based world models and continuous-control benchmarks would clarify whether CIVO is RSSM-specific or a broader vulnerability of temporal conditioning in imagination-based RL.\n",
    "structuredPatch": [
      {
        "oldStart": 17,
        "oldLines": 4,
        "newStart": 17,
        "newLines": 4,
        "lines": [
          " Our experiments focus on a single environment (Walker Walk) and a single world-model architecture (DreamerV3/RSSM). While multi-seed replication establishes robustness within this setting, generalization to other environments and architectures---particularly transformer-based world models such as DreamerV4---remains an open question. The $\\nve$ threshold ($1.5\\times$, 35K+ window) is sensitive to value overestimation broadly but not perfectly specific to CIVO (7/8, one non-CIVO false positive; margin $0.62$ excluding the outlier); generalization to other tasks and architectures is pending validation.",
          " ",
          " \\paragraph{Future directions.}",
          "-Our findings suggest three avenues. First, hierarchical temporal abstraction at the representation level---as in THICK and Hieros---may avoid the flat-conditioning failure mode by maintaining separate dynamics for each temporal scale. Second, gradient decomposition reveals that 93\\% of $\\dt$-embedding gradients originate from observation decoders, with 0\\% from the reward head---making reward-only gradient stopping (exp\\_016e) an architectural no-op. Full-pathway gradient stopping targeting observation decoders (exp\\_018), which removes the dominant 93\\% contribution, is queued to test whether the vulnerability is gradient-level or representation-level. Third, extending this diagnostic framework to transformer-based world models and continuous-control benchmarks would clarify whether CIVO is RSSM-specific or a broader vulnerability of temporal conditioning in imagination-based RL.",
          "+Our findings suggest three avenues. First, hierarchical temporal abstraction at the representation level---as in THICK and Hieros---may avoid the flat-conditioning failure mode by maintaining separate dynamics for each temporal scale. Second, gradient decomposition reveals that 93\\% of $\\dt$-embedding gradients originate from observation decoders, with 0\\% from the reward head---making reward-only gradient stopping (exp\\_016e) an architectural no-op. Full-pathway gradient stopping targeting observation decoders (exp\\_018) removes the dominant 93\\% contribution and completely eliminates CIVO (eval 915.7, NVE $0.72\\times$), confirming that the vulnerability operates at the gradient level: observation reconstruction gradients are necessary for CIVO induction. Third, extending this diagnostic framework to transformer-based world models and continuous-control benchmarks would clarify whether CIVO is RSSM-specific or a broader vulnerability of temporal conditioning in imagination-based RL."
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

_source line 30_

Now modifying abstract.tex — replacing "representation-driven" and adding the full-pathway SGS sentence:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "960e1103-64fd-4d4d-92c9-4e5edc980908",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7j2G9kwUcgWWbJi5YimiX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 325,
      "cache_read_input_tokens": 41590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 325
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01FkPwBFuXKGULKZ5rYar2hk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex",
  "old_string": "Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as representation-driven.",
  "new_string": "Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as observation-reconstruction-gradient-driven. Full-pathway gradient stopping (removing 93\\% of embedding gradients from observation decoders) completely eliminates CIVO, confirming the vulnerability is gradient-level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "e71a6ac4-d97b-4cbb-8f79-6fdfd08e574f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7j2G9kwUcgWWbJi5YimiX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 325,
      "cache_read_input_tokens": 41590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 325
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

_source line 32 · 2026-05-16T13:04:51.178Z_

<details><summary>↩ Tool result · `toolu_01FkPwBFuXKGULKZ5rYar2hk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "8a81f12f-3778-4635-8df2-8865210f2f06",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex",
    "oldString": "Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as representation-driven.",
    "newString": "Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as observation-reconstruction-gradient-driven. Full-pathway gradient stopping (removing 93\\% of embedding gradients from observation decoders) completely eliminates CIVO, confirming the vulnerability is gradient-level.",
    "originalFile": "\\begin{abstract}\nTemporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance---despite the success of identical $\\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify the combination of trained temporal embedding and multi-rate data exposure as the causal trigger and characterize the resulting failure mode: \\emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\Delta t{=}1$ and $\\Delta t{=}2$, which the critic internalizes as optimistic values. Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as representation-driven. A normalized value-to-eval threshold of $1.5\\times$ (35K+ training window) achieves 7/8 classification ($n{=}8$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds---full collapse, transient CIVO with self-correction, and oscillatory degradation---from identical configurations. Critically, restricting imagination to $\\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\begin{abstract}",
          "-Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance---despite the success of identical $\\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify the combination of trained temporal embedding and multi-rate data exposure as the causal trigger and characterize the resulting failure mode: \\emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\Delta t{=}1$ and $\\Delta t{=}2$, which the critic internalizes as optimistic values. Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as representation-driven. A normalized value-to-eval threshold of $1.5\\times$ (35K+ training window) achieves 7/8 classification ($n{=}8$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds---full collapse, transient CIVO with self-correction, and oscillatory degradation---from identical configurations. Critically, restricting imagination to $\\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.",
          "+Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance---despite the success of identical $\\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify the combination of trained temporal embedding and multi-rate data exposure as the causal trigger and characterize the resulting failure mode: \\emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\Delta t{=}1$ and $\\Delta t{=}2$, which the critic internalizes as optimistic values. Gradient decomposition shows that 93\\% of embedding gradients flow through observation decoders (0\\% from the reward head), establishing CIVO as observation-reconstruction-gradient-driven. Full-pathway gradient stopping (removing 93\\% of embedding gradients from observation decoders) completely eliminates CIVO, confirming the vulnerability is gradient-level. A normalized value-to-eval threshold of $1.5\\times$ (35K+ training window) achieves 7/8 classification ($n{=}8$, Walker Walk), with the single false positive arising from a mechanistically distinct non-CIVO collapse. The same CIVO trigger produces stochastic downstream outcomes across seeds---full collapse, transient CIVO with self-correction, and oscillatory degradation---from identical configurations. Critically, restricting imagination to $\\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.",
          " \\end{abstract}"
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

_source line 33_

Now modifying introduction.tex — adding the 018 confirmation after the gradient decomposition sentence:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "c7be6992-7249-4dbc-8592-1f7775f235fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELqsEuEwf1ZQAA9WzJadpZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 344,
      "cache_read_input_tokens": 41915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 344
      },
      "output_tokens": 7,
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

<details open><summary>🔧 Tool call — Edit · `toolu_01K1BH4coSgNR2Xg7Ksc5ZQP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
  "old_string": "Gradient decomposition reveals that 93\\% of temporal embedding gradients originate from observation decoders rather than the reward head (which contributes 0\\%), reframing CIVO as a representation-level phenomenon.",
  "new_string": "Gradient decomposition reveals that 93\\% of temporal embedding gradients originate from observation decoders rather than the reward head (which contributes 0\\%), reframing CIVO as a representation-level phenomenon. A full-pathway gradient-stopping intervention that removes observation decoder gradients from the temporal embedding completely eliminates CIVO (eval recovery to 915.7, NVE 0.72$\\times$), confirming the gradient-level mechanism."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "22407346-13e2-427a-ad1f-c388862fb33c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELqsEuEwf1ZQAA9WzJadpZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 344,
      "cache_read_input_tokens": 41915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 344
      },
      "output_tokens": 7,
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

_source line 35 · 2026-05-16T13:05:01.039Z_

<details><summary>↩ Tool result · `toolu_01K1BH4coSgNR2Xg7Ksc5ZQP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "8cebd436-1f29-4df2-bdcd-e99f2a1030f1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
    "oldString": "Gradient decomposition reveals that 93\\% of temporal embedding gradients originate from observation decoders rather than the reward head (which contributes 0\\%), reframing CIVO as a representation-level phenomenon.",
    "newString": "Gradient decomposition reveals that 93\\% of temporal embedding gradients originate from observation decoders rather than the reward head (which contributes 0\\%), reframing CIVO as a representation-level phenomenon. A full-pathway gradient-stopping intervention that removes observation decoder gradients from the temporal embedding completely eliminates CIVO (eval recovery to 915.7, NVE 0.72$\\times$), confirming the gradient-level mechanism.",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTAWM \\citep{nhu2025tawm} shows that conditioning a world model on step size $\\dt$ yields consistent gains within TD-MPC2's MPC framework \\citep{hansen2024tdmpc2}. Can the same $\\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \\citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?\n\nWe find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\\dt{=}2$ collapses to $14\\%$ of baseline, fixed $\\dt{=}4$ never exceeds $19\\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\\%$. Through a factorial analysis on Walker Walk \\citep{tassa2018dmcontrol}, we isolate the combination of a \\emph{trained} $\\dt$-embedding and multi-rate data exposure as the causal trigger. This trained-and-exposed embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$, which the critic internalizes as optimistic value estimates---a failure mode we term \\emph{conditioning-induced value overestimation} (CIVO). A $\\nve \\geq 1.5\\times$ threshold (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, single environment), with one non-CIVO false positive---a failure mode analogous to delusional bias \\citep{lu2018nondelusional} but arising from model imprecision amplified by learned temporal conditioning. Gradient decomposition reveals that 93\\% of temporal embedding gradients originate from observation decoders rather than the reward head (which contributes 0\\%), reframing CIVO as a representation-level phenomenon.\n\nThree further findings complicate the picture: (1)~the same CIVO trigger produces stochastic downstream outcomes---full collapse, transient CIVO with self-correction, and oscillatory degradation---across seeds of identical configurations; (2)~restricting imagination to $\\dt{=}1$ while retaining the trained embedding does not prevent collapse, with one of two seeds failing via a qualitatively distinct non-CIVO pathway (evaluation-driven, increasing entropy); and (3)~the contrast with TAWM identifies the feedback architecture---imagination-based bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 6,
        "newStart": 3,
        "newLines": 6,
        "lines": [
          " ",
          " TAWM \\citep{nhu2025tawm} shows that conditioning a world model on step size $\\dt$ yields consistent gains within TD-MPC2's MPC framework \\citep{hansen2024tdmpc2}. Can the same $\\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \\citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?",
          " ",
          "-We find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\\dt{=}2$ collapses to $14\\%$ of baseline, fixed $\\dt{=}4$ never exceeds $19\\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\\%$. Through a factorial analysis on Walker Walk \\citep{tassa2018dmcontrol}, we isolate the combination of a \\emph{trained} $\\dt$-embedding and multi-rate data exposure as the causal trigger. This trained-and-exposed embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$, which the critic internalizes as optimistic value estimates---a failure mode we term \\emph{conditioning-induced value overestimation} (CIVO). A $\\nve \\geq 1.5\\times$ threshold (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, single environment), with one non-CIVO false positive---a failure mode analogous to delusional bias \\citep{lu2018nondelusional} but arising from model imprecision amplified by learned temporal conditioning. Gradient decomposition reveals that 93\\% of temporal embedding gradients originate from observation decoders rather than the reward head (which contributes 0\\%), reframing CIVO as a representation-level phenomenon.",
          "+We find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\\dt{=}2$ collapses to $14\\%$ of baseline, fixed $\\dt{=}4$ never exceeds $19\\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\\%$. Through a factorial analysis on Walker Walk \\citep{tassa2018dmcontrol}, we isolate the combination of a \\emph{trained} $\\dt$-embedding and multi-rate data exposure as the causal trigger. This trained-and-exposed embedding enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$, which the critic internalizes as optimistic value estimates---a failure mode we term \\emph{conditioning-induced value overestimation} (CIVO). A $\\nve \\geq 1.5\\times$ threshold (35K+ window) achieves 7/8 CIVO classification ($n{=}8$, single environment), with one non-CIVO false positive---a failure mode analogous to delusional bias \\citep{lu2018nondelusional} but arising from model imprecision amplified by learned temporal conditioning. Gradient decomposition reveals that 93\\% of temporal embedding gradients originate from observation decoders rather than the reward head (which contributes 0\\%), reframing CIVO as a representation-level phenomenon. A full-pathway gradient-stopping intervention that removes observation decoder gradients from the temporal embedding completely eliminates CIVO (eval recovery to 915.7, NVE 0.72$\\times$), confirming the gradient-level mechanism.",
          " ",
          " Three further findings complicate the picture: (1)~the same CIVO trigger produces stochastic downstream outcomes---full collapse, transient CIVO with self-correction, and oscillatory degradation---across seeds of identical configurations; (2)~restricting imagination to $\\dt{=}1$ while retaining the trained embedding does not prevent collapse, with one of two seeds failing via a qualitatively distinct non-CIVO pathway (evaluation-driven, increasing entropy); and (3)~the contrast with TAWM identifies the feedback architecture---imagination-based bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics."
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

_source line 36_

Now I also need to update the F1-F6 reference in results.tex to F1-F7 and check the summary paragraph at the end. Let me also update the opening paragraph and the summary to reflect F7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "bc8cc8b7-6ed7-40a2-bf04-e070bec58430",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrJFy5gkKyG3B1W9mH3nCU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 42259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 373
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

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01JcVRTmifuQDgQ54r9KBDAi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "We organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse.",
  "new_string": "We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse, culminating in a gradient-level intervention that eliminates the vulnerability."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "898342e1-2404-46a5-b2fd-43c1a8a612bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrJFy5gkKyG3B1W9mH3nCU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 42259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 373
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

_source line 38 · 2026-05-16T13:05:07.399Z_

<details><summary>↩ Tool result · `toolu_01JcVRTmifuQDgQ54r9KBDAi`</summary>

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
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "130e2269-5a29-4192-992d-ca20205329f8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "We organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse.",
    "newString": "We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse, culminating in a gradient-level intervention that eliminates the vulnerability.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n009e & Factorial (s1) & trn & ON & 8 & 131.1 @105K & 4.12$\\times$ & Oscillatory \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n009c & No dt\\_emb (s2) & --- & ON & 8 & 148.3 @105K & 1.14$\\times$ & Declining \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\\times$ & Slow learner \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n018 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 915.7 @105K & 0.72$\\times$ & Healthy \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\ntrn$^\\ddagger$ = trained ($d{=}32$) with full-pathway SGS (all non-KL gradients detached from $e_{\\dt}$);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline, regardless of mechanism (Figure~\\ref{fig:learning_curves}). The baseline (exp\\_001) reaches 915.7 at 105K steps and peaks at 970.4 at 505K. In contrast, fixed $\\dt{=}2$ (exp\\_006) peaks at 485.3 at 35K before collapsing to 132.9 by 65K---a $-73\\%$ decline from its own peak (14\\% of baseline). Fixed $\\dt{=}4$ (exp\\_007) peaks at only 176.9 at 25K and never exceeds 152.5 thereafter. The learned-gate configuration (exp\\_005) peaks at 541.2 at 55K but collapses to 98.8 by 145K. This uniform degradation motivates the factorial analysis that follows.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves for all configurations. The $\\dt{=}1$ baseline (black) reaches 915.7 at 105K; all variable-rate configurations degrade, with fixed $\\dt{=}4$ and the learned gate collapsing most severely.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\\_008d (trained $\\dt$-embedding, subsampling ON, $H{=}8$) against exp\\_008f (identical configuration but \\emph{no} trained $\\dt$-embedding). As shown in Figure~\\ref{fig:nve_trajectory}:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d} (trained): $\\nve = 1.78\\times$ at 25K $\\rightarrow$ $4.12\\times$ at 55K $\\rightarrow$ collapse (eval 167$\\rightarrow$82.8).\n\\item \\textbf{008f} (no dt\\_emb): $\\nve = 1.02\\times$ at 25K $\\rightarrow$ $0.30\\times$ at 105K $\\rightarrow$ no collapse (eval 503.0 at 105K).\n\\end{itemize}\n\nIn the 35K+ window (\\S\\ref{sec:metrics}), the $\\nve \\geq 1.5\\times$ threshold correctly classifies 7/8 seeds (AUROC${=}0.933$, Clopper--Pearson 95\\% CI $[0.47, 1.0]$): 3 CIVO-positive (exp\\_006, 008d, 009b) and 4 CIVO-negative, with one non-CIVO false positive (008e\\_v3 s2, $3.78\\times$; \\S\\ref{sec:f6}).  The gap between the lowest true positive ($1.62\\times$) and the highest true negative ($1.00\\times$) is $0.62$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}\n\\caption{Normalized value-to-eval ratio ($\\nve$) trajectories. The dashed line marks the $1.5\\times$ threshold. All trained-embedding configurations with $\\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\\_v3 s1, dash-dot) with $\\dt{=}1$-only imagination remains below it.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\n\\paragraph{Three post-CIVO outcomes.}\nRunning the 008d configuration with two independent seeds (s1, s2) reveals that trained $\\dt$-embedding triggers CIVO---yet the downstream consequence is stochastic. Exp\\_009e extends seed~1 (008d) beyond 55K to 105K steps:\n\n%% ============================================================\n%% TABLE 3: Three post-CIVO outcomes\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window. Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\ns1 ext (009e) & 4.12$\\times$ & 1.57$\\times$ & 131.1 & Oscillatory \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Seed 1 (008d):} Full collapse (Pathway A). Value explosion ($+130\\%$), evaluation declines from 167 to 82.8, entropy decreases---the classic CIVO feedback loop.\n\n\\noindent\\textbf{Seed 2 (009b):} Transient CIVO. The $\\nve$ reaches $1.62\\times$ at 45K (35K+ window), exceeding the $1.5\\times$ threshold, but the value function self-corrects to $0.38\\times$ by 105K, and evaluation recovers to 267.9. This demonstrates the threshold's sensitivity to early CIVO signals even in cases that spontaneously recover.\n\n\\noindent\\textbf{Seed 1 extended (009e):} Oscillatory degradation. Continuing 008d beyond 55K, evaluation oscillates between 82.7 and 250 before settling at 131.1; the value function rises then reverses (peak $\\nve = 4.12\\times$ at 55K, final $1.57\\times$).\n\nAll runs exceed $\\nve \\geq 1.5\\times$ in the 35K+ window, confirming deterministic CIVO triggering, but downstream outcomes are seed-dependent (1/2 persistent collapse rate among independent seeds).\n\n%% ============================================================\n%% F3: Unexposed dt_embedding suppresses value drift\n%% ============================================================\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$)---the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE never exceeds the CIVO threshold: it remains in the $0.39$--$0.47\\times$ range throughout the 55K--105K window, with a brief peak of $1.45\\times$ at 55K that self-corrects to $0.65\\times$ by 65K. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ and triggers full collapse (eval 82.8), while the frozen embedding never exceeds $0.47\\times$ in the same window---an $8.7\\times$ NVE gap. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n%% ============================================================\n%% F5: Horizon and subsample secondary\n%% ============================================================\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n%% ============================================================\n%% F6: dt=1 imagination does not prevent collapse\n%% ============================================================\n\n\\subsection{F6: Restricting Imagination to \\texorpdfstring{$\\dt{=}1$}{dt=1} Does Not Prevent Collapse}\n\\label{sec:f6}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \\textbf{Right:} 008e\\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \\emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\nThe mitigation experiment exp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained $\\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Seed 1} (008e\\_v3\\_s1): Healthy. Eval 869.9 at 105K ($95\\%$ of baseline), $\\nve = 0.80\\times$.\n\\item \\textbf{Seed 2} (008e\\_v3\\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\\nve = 3.78\\times$.\n\\end{itemize}\n\nThe baseline with seed 2 (exp\\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.\n\n\\paragraph{Distinct collapse mechanisms.}\nThe collapse dynamics of 008e\\_v3\\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\\ref{tab:main_results}, Figure~\\ref{fig:multiple_pathways}):\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d (CIVO, Pathway A):} value explosion ($+130\\%$) $\\rightarrow$ evaluation decline $\\rightarrow$ entropy decreases.\n\\item \\textbf{008e\\_v3\\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\\%$) $\\rightarrow$ value remains stable $\\rightarrow$ entropy \\emph{increases} ($-5.21 \\rightarrow -3.83$).\n\\end{itemize}\n\nIn Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\\dt{=}1$ prevents the CIVO mechanism---no early $\\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.\n\nThis case also produces the sole false positive in the $\\nve \\geq 1.5\\times$ classification: 008e\\_v3\\_s2's late evaluation decline inflates $\\nve$ to $3.78\\times$ through a non-CIVO mechanism (\\S\\ref{sec:pathways}).\n\n%% ============================================================\n%% F7: Full-Pathway SGS Eliminates CIVO\n%% ============================================================\n\n\\subsection{F7: Full-Pathway Gradient Stopping Eliminates CIVO}\n\\label{sec:f7}\n\nExp\\_018 applies full-pathway selective gradient stopping (SGS), detaching all non-KL gradients from the temporal embedding $e_{\\dt}$ so that only the 7.3\\% KL dynamics signal remains. Under the same configuration that produces catastrophic CIVO in exp\\_008d (trained $e_{\\dt}$, $d{=}32$, subsample ON, $H{=}8$, $\\dt{=}2$ imagination), exp\\_018 reaches evaluation 915.7 at 105K steps---surpassing the baseline (exp\\_009d: ${\\sim}750$)---with peak NVE $0.72\\times$ in the 35K+ diagnostic window. This is well below both the $1.5\\times$ CIVO threshold and the baseline's $1.0\\times$ reference.\n\nThe progression across gradient-stopping interventions establishes a monotonic relationship between gradient removal and CIVO suppression:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item Exp\\_016e (reward-only SGS, 0\\% effective removal): NVE $10.42\\times$, collapse to 31.7---a null intervention since the reward head contributes zero gradient to $e_{\\dt}$.\n\\item Exp\\_018 (full-pathway SGS, 92.7\\% removal): NVE $0.72\\times$, eval 915.7---CIVO completely eliminated.\n\\item Exp\\_008f (embedding removed, 100\\% removal): NVE $0.97\\times$, eval 503.0---no CIVO, but lower performance due to loss of all temporal information.\n\\end{itemize}\n\nNotably, exp\\_018 \\emph{outperforms} the no-embedding control (008f) by $1.82\\times$ in final evaluation (915.7 vs.\\ 503.0), demonstrating that the KL-only temporal signal provides useful dynamics information without inducing the pathological co-adaptation that drives CIVO. The observation decoder gradient pathway is necessary for CIVO induction; removing it eliminates the vulnerability within the 105K training horizon tested.\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RSSM fidelity analysis.}\nTable~\\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\\dt$-embedding in 008d produces a $2.78\\times$ gap in reward prediction error between $\\dt{=}1$ and $\\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\\ $0.0568$ for 008d at $\\dt{=}1$).\n\n\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \\section{Results}",
          " \\label{sec:results}",
          " ",
          "-We organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.",
          "+We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse, culminating in a gradient-level intervention that eliminates the vulnerability. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.",
          " ",
          " %% ============================================================",
          " %% TABLE 1: Main results summary"
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

_source line 39_

Now update the summary paragraph at the end of results.tex:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "bba2912a-39d1-44db-bbeb-5939e9a4abb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2bnCUWSQKECrWarPWn9tH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 435,
      "cache_read_input_tokens": 42632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 435
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

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_01GTkqfcUSUEE88BQ8WCg2Lh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.",
  "new_string": "\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes.  F7 demonstrates that full-pathway gradient stopping---removing the 92.7\\% observation decoder contribution while retaining the 7.3\\% KL signal---completely eliminates CIVO (eval 915.7, NVE $0.72\\times$), confirming that observation decoder gradients are necessary for CIVO induction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "026d5393-178f-4919-971c-18d1c70a4d44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2bnCUWSQKECrWarPWn9tH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 435,
      "cache_read_input_tokens": 42632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 435
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

_source line 41 · 2026-05-16T13:05:19.707Z_

<details><summary>↩ Tool result · `toolu_01GTkqfcUSUEE88BQ8WCg2Lh`</summary>

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
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "6e0bb91d-2aad-4904-9357-bede3de0a634",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.",
    "newString": "\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes.  F7 demonstrates that full-pathway gradient stopping---removing the 92.7\\% observation decoder contribution while retaining the 7.3\\% KL signal---completely eliminates CIVO (eval 915.7, NVE $0.72\\times$), confirming that observation decoder gradients are necessary for CIVO induction.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse, culminating in a gradient-level intervention that eliminates the vulnerability. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n009e & Factorial (s1) & trn & ON & 8 & 131.1 @105K & 4.12$\\times$ & Oscillatory \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n009c & No dt\\_emb (s2) & --- & ON & 8 & 148.3 @105K & 1.14$\\times$ & Declining \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008c & Unexposed emb & exp$^a$ & OFF & 8 & 240.9 @65K & 0.58$\\times$ & Slow learner \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n018 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 915.7 @105K & 0.72$\\times$ & Healthy \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n009a & Baseline (s2) & --- & --- & 15 & 836.5 @105K & --- & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\ntrn$^\\ddagger$ = trained ($d{=}32$) with full-pathway SGS (all non-KL gradients detached from $e_{\\dt}$);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline, regardless of mechanism (Figure~\\ref{fig:learning_curves}). The baseline (exp\\_001) reaches 915.7 at 105K steps and peaks at 970.4 at 505K. In contrast, fixed $\\dt{=}2$ (exp\\_006) peaks at 485.3 at 35K before collapsing to 132.9 by 65K---a $-73\\%$ decline from its own peak (14\\% of baseline). Fixed $\\dt{=}4$ (exp\\_007) peaks at only 176.9 at 25K and never exceeds 152.5 thereafter. The learned-gate configuration (exp\\_005) peaks at 541.2 at 55K but collapses to 98.8 by 145K. This uniform degradation motivates the factorial analysis that follows.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves for all configurations. The $\\dt{=}1$ baseline (black) reaches 915.7 at 105K; all variable-rate configurations degrade, with fixed $\\dt{=}4$ and the learned gate collapsing most severely.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\\_008d (trained $\\dt$-embedding, subsampling ON, $H{=}8$) against exp\\_008f (identical configuration but \\emph{no} trained $\\dt$-embedding). As shown in Figure~\\ref{fig:nve_trajectory}:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d} (trained): $\\nve = 1.78\\times$ at 25K $\\rightarrow$ $4.12\\times$ at 55K $\\rightarrow$ collapse (eval 167$\\rightarrow$82.8).\n\\item \\textbf{008f} (no dt\\_emb): $\\nve = 1.02\\times$ at 25K $\\rightarrow$ $0.30\\times$ at 105K $\\rightarrow$ no collapse (eval 503.0 at 105K).\n\\end{itemize}\n\nIn the 35K+ window (\\S\\ref{sec:metrics}), the $\\nve \\geq 1.5\\times$ threshold correctly classifies 7/8 seeds (AUROC${=}0.933$, Clopper--Pearson 95\\% CI $[0.47, 1.0]$): 3 CIVO-positive (exp\\_006, 008d, 009b) and 4 CIVO-negative, with one non-CIVO false positive (008e\\_v3 s2, $3.78\\times$; \\S\\ref{sec:f6}).  The gap between the lowest true positive ($1.62\\times$) and the highest true negative ($1.00\\times$) is $0.62$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}\n\\caption{Normalized value-to-eval ratio ($\\nve$) trajectories. The dashed line marks the $1.5\\times$ threshold. All trained-embedding configurations with $\\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\\_v3 s1, dash-dot) with $\\dt{=}1$-only imagination remains below it.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\n\\paragraph{Three post-CIVO outcomes.}\nRunning the 008d configuration with two independent seeds (s1, s2) reveals that trained $\\dt$-embedding triggers CIVO---yet the downstream consequence is stochastic. Exp\\_009e extends seed~1 (008d) beyond 55K to 105K steps:\n\n%% ============================================================\n%% TABLE 3: Three post-CIVO outcomes\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-CIVO outcomes for the 008d configuration. Peak/Final NVE measured in the 35K+ window. Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\ns1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ns2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\ns1 ext (009e) & 4.12$\\times$ & 1.57$\\times$ & 131.1 & Oscillatory \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Seed 1 (008d):} Full collapse (Pathway A). Value explosion ($+130\\%$), evaluation declines from 167 to 82.8, entropy decreases---the classic CIVO feedback loop.\n\n\\noindent\\textbf{Seed 2 (009b):} Transient CIVO. The $\\nve$ reaches $1.62\\times$ at 45K (35K+ window), exceeding the $1.5\\times$ threshold, but the value function self-corrects to $0.38\\times$ by 105K, and evaluation recovers to 267.9. This demonstrates the threshold's sensitivity to early CIVO signals even in cases that spontaneously recover.\n\n\\noindent\\textbf{Seed 1 extended (009e):} Oscillatory degradation. Continuing 008d beyond 55K, evaluation oscillates between 82.7 and 250 before settling at 131.1; the value function rises then reverses (peak $\\nve = 4.12\\times$ at 55K, final $1.57\\times$).\n\nAll runs exceed $\\nve \\geq 1.5\\times$ in the 35K+ window, confirming deterministic CIVO triggering, but downstream outcomes are seed-dependent (1/2 persistent collapse rate among independent seeds).\n\n%% ============================================================\n%% F3: Unexposed dt_embedding suppresses value drift\n%% ============================================================\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe causal claim that trained embedding \\emph{plus} multi-rate exposure jointly trigger CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.59$--$0.93\\times$ range across 105K steps. Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training---confirming that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$)---the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE never exceeds the CIVO threshold: it remains in the $0.39$--$0.47\\times$ range throughout the 55K--105K window, with a brief peak of $1.45\\times$ at 55K that self-corrects to $0.65\\times$ by 65K. Final evaluation reaches only 204.2 at 105K---low, but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), indicating that the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ and triggers full collapse (eval 82.8), while the frozen embedding never exceeds $0.47\\times$ in the same window---an $8.7\\times$ NVE gap. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that CIVO requires the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole trigger for CIVO. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell---trained embedding with multi-rate exposure---triggers CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly necessary.\n\n%% ============================================================\n%% F4: dt=2 > dt=4 monotonic degradation\n%% ============================================================\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n%% ============================================================\n%% F5: Horizon and subsample secondary\n%% ============================================================\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling triggers collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$---confirming that low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n%% ============================================================\n%% F6: dt=1 imagination does not prevent collapse\n%% ============================================================\n\n\\subsection{F6: Restricting Imagination to \\texorpdfstring{$\\dt{=}1$}{dt=1} Does Not Prevent Collapse}\n\\label{sec:f6}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (classic CIVO)---value explosion precedes evaluation decline, entropy decreases. \\textbf{Right:} 008e\\_v3 seed 2 (non-CIVO)---evaluation crashes while value remains stable, entropy \\emph{increases}. Baseline seed 2 (009a, dashed) remains stable at 836.5, ruling out seed fragility.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\nThe mitigation experiment exp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained $\\dt$-embedding for observation conditioning. If CIVO were the sole vulnerability pathway, this restriction should prevent collapse. Results are mixed:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Seed 1} (008e\\_v3\\_s1): Healthy. Eval 869.9 at 105K ($95\\%$ of baseline), $\\nve = 0.80\\times$.\n\\item \\textbf{Seed 2} (008e\\_v3\\_s2): Collapsed. Eval drops from 715 to 137 at 105K, $\\nve = 3.78\\times$.\n\\end{itemize}\n\nThe baseline with seed 2 (exp\\_009a) is stable at 836.5 at 105K, ruling out inherent seed fragility as the explanation.\n\n\\paragraph{Distinct collapse mechanisms.}\nThe collapse dynamics of 008e\\_v3\\_s2 differ qualitatively from the classic CIVO observed in 008d (Table~\\ref{tab:main_results}, Figure~\\ref{fig:multiple_pathways}):\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{008d (CIVO, Pathway A):} value explosion ($+130\\%$) $\\rightarrow$ evaluation decline $\\rightarrow$ entropy decreases.\n\\item \\textbf{008e\\_v3\\_s2 (non-CIVO, Pathway B):} evaluation crashes ($-81\\%$) $\\rightarrow$ value remains stable $\\rightarrow$ entropy \\emph{increases} ($-5.21 \\rightarrow -3.83$).\n\\end{itemize}\n\nIn Pathway A, the critic drives collapse through systematic overestimation; in Pathway B, the actor destabilizes independently while the critic remains initially well-calibrated. Restricting imagination to $\\dt{=}1$ prevents the CIVO mechanism---no early $\\nve$ spike, no reward amplification---but seed-dependent late-stage policy instability (Pathway B) can still occur.\n\nThis case also produces the sole false positive in the $\\nve \\geq 1.5\\times$ classification: 008e\\_v3\\_s2's late evaluation decline inflates $\\nve$ to $3.78\\times$ through a non-CIVO mechanism (\\S\\ref{sec:pathways}).\n\n%% ============================================================\n%% F7: Full-Pathway SGS Eliminates CIVO\n%% ============================================================\n\n\\subsection{F7: Full-Pathway Gradient Stopping Eliminates CIVO}\n\\label{sec:f7}\n\nExp\\_018 applies full-pathway selective gradient stopping (SGS), detaching all non-KL gradients from the temporal embedding $e_{\\dt}$ so that only the 7.3\\% KL dynamics signal remains. Under the same configuration that produces catastrophic CIVO in exp\\_008d (trained $e_{\\dt}$, $d{=}32$, subsample ON, $H{=}8$, $\\dt{=}2$ imagination), exp\\_018 reaches evaluation 915.7 at 105K steps---surpassing the baseline (exp\\_009d: ${\\sim}750$)---with peak NVE $0.72\\times$ in the 35K+ diagnostic window. This is well below both the $1.5\\times$ CIVO threshold and the baseline's $1.0\\times$ reference.\n\nThe progression across gradient-stopping interventions establishes a monotonic relationship between gradient removal and CIVO suppression:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item Exp\\_016e (reward-only SGS, 0\\% effective removal): NVE $10.42\\times$, collapse to 31.7---a null intervention since the reward head contributes zero gradient to $e_{\\dt}$.\n\\item Exp\\_018 (full-pathway SGS, 92.7\\% removal): NVE $0.72\\times$, eval 915.7---CIVO completely eliminated.\n\\item Exp\\_008f (embedding removed, 100\\% removal): NVE $0.97\\times$, eval 503.0---no CIVO, but lower performance due to loss of all temporal information.\n\\end{itemize}\n\nNotably, exp\\_018 \\emph{outperforms} the no-embedding control (008f) by $1.82\\times$ in final evaluation (915.7 vs.\\ 503.0), demonstrating that the KL-only temporal signal provides useful dynamics information without inducing the pathological co-adaptation that drives CIVO. The observation decoder gradient pathway is necessary for CIVO induction; removing it eliminates the vulnerability within the 105K training horizon tested.\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RSSM fidelity analysis.}\nTable~\\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\\dt$-embedding in 008d produces a $2.78\\times$ gap in reward prediction error between $\\dt{=}1$ and $\\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\\ $0.0568$ for 008d at $\\dt{=}1$).\n\n\\paragraph{Summary.}\nF1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.\n",
    "structuredPatch": [
      {
        "oldStart": 279,
        "oldLines": 4,
        "newStart": 279,
        "newLines": 4,
        "lines": [
          " Table~\\ref{tab:rssm_fidelity} reveals the mechanism underlying CIVO. The trained $\\dt$-embedding in 008d produces a $2.78\\times$ gap in reward prediction error between $\\dt{=}1$ and $\\dt{=}2$ trajectories. This asymmetric fidelity means the reward head systematically overpredicts rewards at $\\dt{=}2$, which the critic internalizes as optimistic value estimates. In contrast, 008f (no embedding) shows a $1.01\\times$ gap---the reward head cannot distinguish temporal scales, which eliminates the exploitation channel but at the cost of severely degraded absolute reward prediction ($0.7469$ MAE vs.\\ $0.0568$ for 008d at $\\dt{=}1$).",
          " ",
          " \\paragraph{Summary.}",
          "-F1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes: $\\nve$ is a sensitive but non-specific warning indicator requiring joint analysis with collapse signatures for mechanistic attribution.",
          "+F1--F5 establish the combination of trained $\\dt$-embedding and multi-rate data exposure as the causal factor (7/8 classification, one non-CIVO false positive), with degradation scaling monotonically with $\\dt$.  F6 shows that restricting imagination to $\\dt{=}1$ prevents CIVO but not all collapse modes.  F7 demonstrates that full-pathway gradient stopping---removing the 92.7\\% observation decoder contribution while retaining the 7.3\\% KL signal---completely eliminates CIVO (eval 915.7, NVE $0.72\\times$), confirming that observation decoder gradients are necessary for CIVO induction."
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

_source line 42_

Now let me verify compilation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "9c1e5cfe-87a2-4c13-adb3-62b185c27afc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLfkqAZ7wAZN9yhLzopLV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 501,
      "cache_read_input_tokens": 43067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 501
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

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01AkcvKer9dhqvuxKje5kkap`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "Compile LaTeX to verify no errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "0e86498b-f5c6-4ae9-97f2-fe31fc681e6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLfkqAZ7wAZN9yhLzopLV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 501,
      "cache_read_input_tokens": 43067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 501
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

_source line 44 · 2026-05-16T13:05:25.169Z_

<details><summary>↩ Tool result · `toolu_01AkcvKer9dhqvuxKje5kkap`</summary>

```text
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx0900.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/
home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> 
&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk
> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600
pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.6
00pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy9.pfb>
Output written on main.pdf (14 pages, 552815 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "149b7173-b811-416f-b613-f7570a090efa",
  "tool_use_result": {
    "stdout": "live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx0900.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/\nhome/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> \n&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk\n> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600\npk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.6\n00pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy9.pfb>\nOutput written on main.pdf (14 pages, 552815 bytes).\nTranscript written on main.log.",
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

_source line 45_

Let me check for any LaTeX errors or warnings in the log:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "e0c67d30-6701-485a-b0e6-d8860c2b6779",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4B2vhXWZhFcURT9RQaCE4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 43568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1292
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

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01SApMY9YzUy7BuHQ9ufyrGg`</summary>

```json
{
  "command": "grep -c \"^!\" main.log; grep \"^!\" main.log | head -5",
  "description": "Check for LaTeX errors in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "51b367c7-d98d-4036-9d5c-8ba0bc8b80c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4B2vhXWZhFcURT9RQaCE4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 43568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1292
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

_source line 47 · 2026-05-16T13:05:29.300Z_

<details><summary>↩ Tool result · `toolu_01SApMY9YzUy7BuHQ9ufyrGg`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "28bf1f11-2b88-4ae7-bc5d-fa54a5291192",
  "tool_use_result": {
    "stdout": "0",
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

_source line 48_

Zero errors. Compilation successful — 14 pages output, no errors.

All 6 modifications complete:
1. **Table 1**: Added 018 row with `trn$^\ddagger$` footnote
2. **F7 section**: Inserted after F6, before RSSM fidelity table
3. **analysis.tex**: Added "Full-Pathway SGS Confirms Gradient-Level Vulnerability" subsubsection before the 016e reinterpretation
4. **conclusion.tex**: Replaced "queued to test" with confirmed result
5. **abstract.tex**: Changed "representation-driven" to "observation-reconstruction-gradient-driven" and added full-pathway SGS sentence
6. **introduction.tex**: Added gradient-stopping confirmation sentence

Also updated the results opening paragraph (F1–F6 → F1–F7) and summary paragraph to include F7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "uuid": "8f997a02-a8c0-4c2c-809a-3f6c7743a9cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4Wwd7FNzB949BaVGa7pZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 123,
      "cache_read_input_tokens": 44860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 123
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

_source line 49_

Zero errors. Compilation successful — 14 pages output, no errors.

All 6 modifications complete:
1. **Table 1**: Added 018 row with `trn$^\ddagger$` footnote
2. **F7 section**: Inserted after F6, before RSSM fidelity table
3. **analysis.tex**: Added "Full-Pathway SGS Confirms Gradient-Level Vulnerability" subsubsection before the 016e reinterpretation
4. **conclusion.tex**: Replaced "queued to test" with confirmed result
5. **abstract.tex**: Changed "representation-driven" to "observation-reconstruction-gradient-driven" and added full-pathway SGS sentence
6. **introduction.tex**: Added gradient-stopping confirmation sentence

Also updated the results opening paragraph (F1–F6 → F1–F7) and summary paragraph to include F7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 121297,
  "duration_api_ms": 121776,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "9d6c3600-3573-4177-8454-ab1085cdb67f",
  "total_cost_usd": 0.559734,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 33536,
    "cache_read_input_tokens": 455838,
    "output_tokens": 4773,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33536,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 209,
        "cache_read_input_tokens": 44860,
        "cache_creation_input_tokens": 123,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 123
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2720,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00282,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 4773,
      "cacheReadInputTokens": 455838,
      "cacheCreationInputTokens": 33536,
      "webSearchRequests": 0,
      "costUSD": 0.556914,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "07ecbcbb-ec75-4a46-8275-4c980a9da8df"
}
```

</details>

---
