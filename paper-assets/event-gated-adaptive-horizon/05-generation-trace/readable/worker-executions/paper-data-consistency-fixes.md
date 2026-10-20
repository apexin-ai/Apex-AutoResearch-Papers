# paper data consistency fixes

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_data-consistency-fixes_20260517T110948.log`
- **Structured JSON:** [`fc5fb9c38ef698c1e6b1.json`](../../sessions/fc/fc5fb9c38ef698c1e6b1.json)

## Before a recorded user message

36 recorded events

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
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
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
  "uuid": "404142ae-2ac4-4ef4-ac23-9569ec5089e2",
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
    "resetsAt": 1779024600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2bead12f-1303-4fb4-838a-ccf9c47d0b41",
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the results.tex file to understand the current content and locate the items that need to be fixed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "3b60b25c-fd8d-4a38-914b-be42af72b170",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LCvMMQfRS53kLccS4HVPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14056,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14056
      },
      "output_tokens": 49,
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

<details open><summary>🔧 Tool call — Read · `toolu_017yueTHniKS4NFmNbGkziTt`</summary>

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
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "0ff5e658-c57e-496b-bce8-9fc955d00ff1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LCvMMQfRS53kLccS4HVPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14056,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14056
      },
      "output_tokens": 49,
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

_source line 6 · 2026-05-17T11:10:02.419Z_

<details><summary>↩ Tool result · `toolu_017yueTHniKS4NFmNbGkziTt`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
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
31	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
32	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
33	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
34	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\times$ & Grad.\ starvation \\
35	\midrule
36	018 s1 & Full-SGS & trn$^\ddagger$ & ON & 8 & \sgseval{} @105K & \sgsnve{}$\times$$^*$ & No collapse \\
37	\rowcolor{gray!15}
38	018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
39	008e\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\times$ & Healthy \\
40	008e\_v3 s2$^\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\times$ & Non-CIVO collapse \\
41	\midrule
42	\multicolumn{8}{l}{\textit{Cross-environment validation (Cheetah Run)}} \\
43	\rowcolor{gray!15}
44	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 14.59$\times$ & Collapsed \\
45	\bottomrule
46	\end{tabular}
47	\vspace{1pt}
48	{\raggedright\footnotesize
49	trn = trained ($d{=}32$, subsample ON);
50	trn$^\ddagger$ = full-pathway SGS (all non-KL gradients detached);
51	exp$^a$ = trained, subsample OFF;
52	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
53	--- = removed ($d{=}0$).\\
54	$^*$ Seed 1 only: peak NVE with transient exceedances (1.61$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
55	$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\par}
56	\end{table*}
57	
58	%% ============================================================
59	%% F1: All dt>1 degrade
60	%% ============================================================
61	
62	\subsection{F1: All Variable-Rate Configurations Degrade}
63	\label{sec:f1}
64	
65	Every configuration that introduces $\dt > 1$ imagination degrades relative to the $\dt{=}1$ baseline (Figure~\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\%$ of baseline); fixed $\dt{=}4$ (007) never exceeds 176.9 ($19\%$); the learned gate (005) collapses to 98.8 ($11\%$).
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=0.65\columnwidth]{figures/paper/fig1_learning_curves.pdf}
70	\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}
71	\label{fig:learning_curves}
72	\end{figure}
73	
74	%% ============================================================
75	%% F2: Trained dt_embedding → nve > 1.5x
76	%% ============================================================
77	
78	\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}
79	\label{sec:f2}
80	
81	The factorial design isolates trained $\dt$-embedding as the causal trigger. Comparing exp\_008d (trained, subsample ON) against exp\_008f (no embedding, subsample ON): 008d reaches $\nve = 4.12\times$ and collapses (eval 82.8), while 008f maintains $\nve \leq 0.97\times$ (eval 503.0). The $\nve \geq 1.5\times$ threshold (35K+ window) correctly classifies 7/8 seeds (AUROC${=}0.933$; Figure~\ref{fig:nve_trajectory}).
82	
83	\begin{figure}[t]
84	\centering
85	\includegraphics[width=0.65\columnwidth]{figures/fig1_nve_trajectory.pdf}
86	\caption{NVE trajectories (mean $\pm$ seed range). Trained $\dt$-embedding (red, $n{=}3$) exceeds the $1.5\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}
87	\label{fig:nve_trajectory}
88	\end{figure}
89	
90	The trained $\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\times$, $1.62\times$, $1.53\times$; all $\geq 1.5\times$ threshold), universally degrading performance to below 30\% of baseline (mean eval 206.3, 21.3\% of baseline 970.41). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 8.6\% of baseline), seed~3 (008d\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 27.6\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\ref{sec:seed_divergence}).
91	
92	%% ============================================================
93	%% F3--F5: Summary (details in Appendix B)
94	%% ============================================================
95	
96	\subsection{F3--F5: Factorial Ablation (Appendix~\ref{sec:appendix_factorial})}
97	\label{sec:f3f5_summary}
98	
99	Trained $\dt$-embedding and multi-rate data exposure are \emph{jointly necessary} for CIVO. Neither factor alone triggers pathological overestimation: trained embedding without multi-rate exposure (008a, NVE $= 0.93\times$) and multi-rate exposure without embedding (008f, NVE $= 0.97\times$) both remain well below the $1.5\times$ diagnostic threshold, while frozen embedding under full exposure (015b) never exceeds $0.47\times$ (Figure~\ref{fig:factorial_grid}). Degradation scales monotonically with $\dt$ ($-47\%$ at $\dt{=}2$, $-81\%$ at $\dt{=}4$; Figure~\ref{fig:dt_amplification}).
100	
101	%% ============================================================
102	%% F6--F7: Interventions and cross-environment
103	%% ============================================================
104	
105	\subsection{F6--F7: Interventions and Multiple Pathways}
106	\label{sec:f6}
107	
108	\paragraph{F6: $\dt{=}1$ imagination does not prevent all collapse.}
109	Exp\_008e\_v3 restricts imagination to $\dt{=}1$ while retaining the trained embedding. Seed~1 is healthy (eval 869.9, $\nve = 0.80\times$); seed~2 collapses (eval $715 \rightarrow 137$, $\nve = 3.78\times$), but via a qualitatively distinct mechanism (Figure~\ref{fig:multiple_pathways}). Classic CIVO (008d, Pathway~A) shows value explosion followed by evaluation decline with decreasing entropy; 008e\_v3\_s2 (Pathway~B) shows evaluation crash with \emph{increasing} entropy ($-5.21 \rightarrow -3.83$) while values remain stable. This produces the sole false positive in the NVE classification.
110	
111	\begin{figure}[t]
112	\centering
113	\includegraphics[width=0.65\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}
114	\caption{Contrasting collapse dynamics. \textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \textbf{Right:} 008e\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}
115	\label{fig:multiple_pathways}
116	\end{figure}
117	
118	\paragraph{F7: Full-pathway gradient stopping shows mixed results.}
119	Exp\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\dt$-embedding alone produces $-73\%$ peak and $-86\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \sgseval{}, $-51\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\%$), yielding a 50\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\%$); peak NVE $14.59\times$.
120	
121	\begin{figure}[t]
122	\centering
123	\includegraphics[width=0.75\columnwidth]{figures/fig2_civo_decomposition.pdf}
124	\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\dt}$, two seeds. Trained $\dt$-embedding degrades peak eval by $73\%$ and final eval by $86\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\%$ final, no collapse) but seed~2 collapses ($-96\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\%$). All percentages relative to Baseline 001.}
125	\label{fig:civo_decomposition}
126	\end{figure}
127	
128	%% ============================================================
129	%% TABLE 2: RSSM Fidelity
130	%% ============================================================
131	
132	\begin{table}[t]
133	\centering
134	\caption{RSSM fidelity at $\dt{=}1$ vs.\ $\dt{=}2$. Trained embedding (008d) produces $2.78\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}
135	\label{tab:rssm_fidelity}
136	\footnotesize
137	\setlength{\tabcolsep}{4pt}
138	\begin{tabular}{lcccccc}
139	\toprule
140	& \multicolumn{3}{c}{\textbf{obs\_MSE}} & \multicolumn{3}{c}{\textbf{reward\_MAE}} \\
141	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
142	\textbf{Config} & $\dt{=}1$ & $\dt{=}2$ & Gap & $\dt{=}1$ & $\dt{=}2$ & Gap \\
143	\midrule
144	Baseline & 13.49 & 27.50 & 2.04$\times$ & 0.0102 & 0.0159 & 1.56$\times$ \\
145	008d (trained) & 41.31 & 53.67 & 1.30$\times$ & 0.0568 & 0.1579 & 2.78$\times$ \\
146	008f (no emb) & 8.01 & 22.04 & 2.75$\times$ & 0.7469 & 0.7526 & 1.01$\times$ \\
147	\bottomrule
148	\end{tabular}
149	\end{table}
150	
151	The trained embedding in 008d produces a $2.78\times$ reward prediction gap between $\dt{=}1$ and $\dt{=}2$ (Table~\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes as optimistic value estimates. Having established the mechanistic basis of CIVO, we now ask whether it can be detected during training without access to a reference baseline.
152	
153	%% ============================================================
154	%% F8: Online CIVO Detection
155	%% ============================================================
156	
157	\subsection{Online CIVO Detection}
158	\label{sec:detector}
159	
160	\paragraph{Motivation.}
161	The Normalized Value Excess ($\nve$) quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment cannot serve as an early warning.
162	
163	We therefore ask whether the \emph{dynamics} of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. By tracking the trajectory of the value-to-evaluation ratio $r_t = \bar{V}_t / \max(\bar{E}_t, \varepsilon)$ (with $\varepsilon = 10^{-6}$ for numerical stability) across checkpoints, a lightweight rule-based detector can flag dangerous overestimation using only quantities available within a single run.
164	
165	The causal structure of CIVO motivates acceleration as the key detection signal. CIVO operates as a positive feedback loop: the trained embedding biases reward predictions, which inflate value estimates, which in turn distort actor gradients toward trajectories that reinforce the bias (\S\ref{sec:civo_mechanism}). This self-amplifying cycle produces superlinear growth in $r_t$. In healthy training, a natural negative feedback counteracts value growth: improved value estimates yield a better actor, which raises evaluation returns, stabilizing the ratio. CIVO breaks this negative feedback, so sustained positive acceleration in $r_t$ serves as a causal signature that distinguishes pathological divergence from normal value learning.
166	
167	\paragraph{Algorithm.}
168	The detector monitors $r_t$ and fires an alert only when four conditions hold simultaneously at checkpoint $t$ (Algorithm~\ref{alg:civo_detector}). The conjunction makes the detector conservative: any single noisy checkpoint is unlikely to satisfy magnitude, velocity, acceleration, and decline together. The computational cost is negligible (four scalar comparisons per checkpoint, no additional model inference).
169	
170	\begin{algorithm}[t]
171	\caption{Online CIVO Detector}
172	\label{alg:civo_detector}
173	\begin{algorithmic}[1]
174	\REQUIRE Stream of $(\bar{V}_t, \bar{E}_t)$ at each checkpoint $t$
175	\STATE $\tau_\text{mag} \leftarrow 0.49$, \quad $\tau_\text{vel} \leftarrow 0.1$, \quad $\varepsilon \leftarrow 10^{-6}$
176	\STATE Initialize $r_\text{prev} \leftarrow 0$, $\Delta r_\text{prev} \leftarrow 0$, $\mathcal{H} \leftarrow []$
177	\FOR{each checkpoint $t$}
178	  \STATE $r_t \leftarrow \bar{V}_t \,/\, \max(\bar{E}_t,\, \varepsilon)$
179	  \STATE $\Delta r_t \leftarrow r_t - r_\text{prev}$
180	  \STATE $c_\text{mag} \leftarrow (r_t \geq \tau_\text{mag})$
181	  \STATE $c_\text{vel} \leftarrow (\Delta r_t > \tau_\text{vel})$
182	  \STATE $c_\text{acc} \leftarrow (\Delta r_\text{prev} > \tau_\text{vel}) \wedge (\Delta r_t > \Delta r_\text{prev})$
183	  \STATE $c_\text{dec} \leftarrow \bigl|\{i : \mathcal{H}[i] < \mathcal{H}[i{-}1],\; i \in \text{last 3}\}\bigr| \geq 2$
184	  \IF{$c_\text{mag} \wedge c_\text{vel} \wedge c_\text{acc} \wedge c_\text{dec}$}
185	    \STATE \textbf{Alert:} CIVO onset at step $t$
186	  \ENDIF
187	  \STATE $r_\text{prev} \leftarrow r_t$, \quad $\Delta r_\text{prev} \leftarrow \Delta r_t$
188	  \STATE Append $\bar{E}_t$ to $\mathcal{H}$
189	\ENDFOR
190	\end{algorithmic}
191	\end{algorithm}
192	
193	The four conditions capture complementary signals: (1)~\emph{Magnitude} ($r_t \geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\emph{Velocity} ($\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\emph{Acceleration} ($\Delta r_t > \Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths where the ratio rises and falls without sustained divergence; (4)~\emph{Evaluation decline} ($\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A 2-of-3 majority threshold balances noise robustness against single-checkpoint evaluation variance with sensitivity to sustained decline.\footnote{A full comparison of window sizes (3/3, 2/3, 2/5) and their trade-offs appears in Appendix~\ref{sec:appendix_sensitivity}.}
194	
195	Sensitivity analysis over $\tau_\text{mag} \in [0.30, 0.70]$ confirms that $\tau_\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives, since both false alarms have $r_t > 0.70$ at trigger time. The velocity threshold $\tau_\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $3/3$); we retain $0.1$ to avoid overfitting to $n{=}10$ runs.
196	
197	\paragraph{Validation.}
198	We apply the detector retrospectively to ten runs spanning three conditions: trained duration embedding (CIVO-positive, $n{=}3$), untrained or absent embedding (CIVO-negative, $n{=}3$), and vanilla baselines ($n{=}4$). Ground truth labels derive from manual inspection: a run is CIVO-positive if it exhibits sustained $\nve \geq 1.5\times$ with subsequent evaluation collapse. Table~\ref{tab:detector-validation} reports all results.
199	
200	\begin{table}[t]
201	\centering
202	\caption{Retrospective CIVO detector validation ($n{=}10$). Detection type: ``predictive'' = alert precedes 20\% eval decline; ``reactive'' = alert follows decline onset.}
203	\label{tab:detector-validation}
204	\footnotesize
205	\setlength{\tabcolsep}{3pt}
206	\begin{tabular}{llccccc}
207	\toprule
208	\textbf{Exp} & \textbf{Config} & \textbf{Verdict} & \textbf{Trigger} & \textbf{Type} & \textbf{Peak Eval} & $r_\text{ve}$ \\
209	\midrule
210	008d s0 & trained $\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\
211	010b & trained $\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\
212	008d s3 & trained $\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\
213	\midrule
214	008f s3 & no $\dt$-emb & TN & -- & -- & 594 & -- \\
215	009b s2 & trained $\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\
216	baseline s1 & vanilla & TN & -- & -- & 970 & -- \\
217	009d s0 & vanilla & TN & -- & -- & 951 & -- \\
218	009d s1 & vanilla & TN & -- & -- & 920 & -- \\
219	\midrule
220	009c s2 & no $\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\
221	009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\
222	\midrule
223	\multicolumn{7}{l}{TPR = 3/3 (1.00), \quad FPR = 2/7 (0.29)} \\
224	\bottomrule
225	\end{tabular}
226	\end{table}
227	
228	\paragraph{Results.}
229	The detector identifies all three CIVO-positive runs (TPR = 3/3). Two of three are detected \emph{predictively}: 008d seed~0 triggers at 45K, one checkpoint before evaluation crosses the 20\% decline threshold; seed~3 triggers at 45K, a full 50K steps before decline begins. The third case (010b, Cheetah Run) involves single-step collapse (evaluation drops 80\% in one interval), and the detector fires reactively at the next available checkpoint. No checkpoint-based monitor can provide advance warning for instantaneous collapse.
230	
231	Two false positives occur among seven negative cases (FPR = 2/7, precision = 3/5 = 0.60, F$_1$ = 0.75). Run 009c (no duration embedding) develops genuine late-stage value overestimation unrelated to CIVO; the detector correctly identifies value-performance dissociation, and the alert is arguably useful despite the label mismatch. Run 009a (vanilla baseline) triggers during a transient three-checkpoint eval dip at 85K; the model subsequently recovers to 966, constituting a pure false alarm. In practice, the cost of a false alert (manual checkpoint inspection, minutes) is orders of magnitude lower than the cost of undetected collapse (wasted GPU-hours, corrupted model); moderate FPR is therefore acceptable in this application.
232	
233	All three true positives triggered before 65K steps (range 45--65K) while both false positives occurred after 85K (range 85--105K), suggesting that early-training alerts carry higher diagnostic confidence. In practice, alerts before 70K steps can be treated as high-confidence CIVO indicators; later alerts warrant manual inspection.
234	
235	\paragraph{Limitations.}
236	Four constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse (the source of the 009a false alarm). Second, the acceleration condition assumes monotonically increasing overestimation during onset; oscillatory trajectories that eventually collapse could evade detection until acceleration stabilizes. Third, the detector identifies a \emph{pattern} (rising value-evaluation ratio with declining performance) rather than a \emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values ($\tau_\text{mag} = 0.49$, $\tau_\text{vel} = 0.1$) were calibrated on ten runs across two environments; generalization to different reward scales requires further validation.
237	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "0ea79dfa-b1b2-4403-b99d-7796d38d3092",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & No collapse \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation (Cheetah Run)}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 14.59$\\times$ & Collapsed \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.61$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the causal trigger. Comparing exp\\_008d (trained, subsample ON) against exp\\_008f (no embedding, subsample ON): 008d reaches $\\nve = 4.12\\times$ and collapses (eval 82.8), while 008f maintains $\\nve \\leq 0.97\\times$ (eval 503.0). The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 7/8 seeds (AUROC${=}0.933$; Figure~\\ref{fig:nve_trajectory}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, $n{=}3$) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.3, 21.3\\% of baseline 970.41). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 8.6\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 27.6\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly necessary} for CIVO. Neither factor alone triggers pathological overestimation: trained embedding without multi-rate exposure (008a, NVE $= 0.93\\times$) and multi-rate exposure without embedding (008f, NVE $= 0.97\\times$) both remain well below the $1.5\\times$ diagnostic threshold, while frozen embedding under full exposure (015b) never exceeds $0.47\\times$ (Figure~\\ref{fig:factorial_grid}). Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: $\\dt{=}1$ imagination does not prevent all collapse.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Seed~1 is healthy (eval 869.9, $\\nve = 0.80\\times$); seed~2 collapses (eval $715 \\rightarrow 137$, $\\nve = 3.78\\times$), but via a qualitatively distinct mechanism (Figure~\\ref{fig:multiple_pathways}). Classic CIVO (008d, Pathway~A) shows value explosion followed by evaluation decline with decreasing entropy; 008e\\_v3\\_s2 (Pathway~B) shows evaluation crash with \\emph{increasing} entropy ($-5.21 \\rightarrow -3.83$) while values remain stable. This produces the sole false positive in the NVE classification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe trained embedding in 008d produces a $2.78\\times$ reward prediction gap between $\\dt{=}1$ and $\\dt{=}2$ (Table~\\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes as optimistic value estimates. Having established the mechanistic basis of CIVO, we now ask whether it can be detected during training without access to a reference baseline.\n\n%% ============================================================\n%% F8: Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\n\\paragraph{Motivation.}\nThe Normalized Value Excess ($\\nve$) quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment cannot serve as an early warning.\n\nWe therefore ask whether the \\emph{dynamics} of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. By tracking the trajectory of the value-to-evaluation ratio $r_t = \\bar{V}_t / \\max(\\bar{E}_t, \\varepsilon)$ (with $\\varepsilon = 10^{-6}$ for numerical stability) across checkpoints, a lightweight rule-based detector can flag dangerous overestimation using only quantities available within a single run.\n\nThe causal structure of CIVO motivates acceleration as the key detection signal. CIVO operates as a positive feedback loop: the trained embedding biases reward predictions, which inflate value estimates, which in turn distort actor gradients toward trajectories that reinforce the bias (\\S\\ref{sec:civo_mechanism}). This self-amplifying cycle produces superlinear growth in $r_t$. In healthy training, a natural negative feedback counteracts value growth: improved value estimates yield a better actor, which raises evaluation returns, stabilizing the ratio. CIVO breaks this negative feedback, so sustained positive acceleration in $r_t$ serves as a causal signature that distinguishes pathological divergence from normal value learning.\n\n\\paragraph{Algorithm.}\nThe detector monitors $r_t$ and fires an alert only when four conditions hold simultaneously at checkpoint $t$ (Algorithm~\\ref{alg:civo_detector}). The conjunction makes the detector conservative: any single noisy checkpoint is unlikely to satisfy magnitude, velocity, acceleration, and decline together. The computational cost is negligible (four scalar comparisons per checkpoint, no additional model inference).\n\n\\begin{algorithm}[t]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths where the ratio rises and falls without sustained divergence; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A 2-of-3 majority threshold balances noise robustness against single-checkpoint evaluation variance with sensitivity to sustained decline.\\footnote{A full comparison of window sizes (3/3, 2/3, 2/5) and their trade-offs appears in Appendix~\\ref{sec:appendix_sensitivity}.}\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives, since both false alarms have $r_t > 0.70$ at trigger time. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $3/3$); we retain $0.1$ to avoid overfitting to $n{=}10$ runs.\n\n\\paragraph{Validation.}\nWe apply the detector retrospectively to ten runs spanning three conditions: trained duration embedding (CIVO-positive, $n{=}3$), untrained or absent embedding (CIVO-negative, $n{=}3$), and vanilla baselines ($n{=}4$). Ground truth labels derive from manual inspection: a run is CIVO-positive if it exhibits sustained $\\nve \\geq 1.5\\times$ with subsequent evaluation collapse. Table~\\ref{tab:detector-validation} reports all results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}10$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 3/3 (1.00), \\quad FPR = 2/7 (0.29)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nThe detector identifies all three CIVO-positive runs (TPR = 3/3). Two of three are detected \\emph{predictively}: 008d seed~0 triggers at 45K, one checkpoint before evaluation crosses the 20\\% decline threshold; seed~3 triggers at 45K, a full 50K steps before decline begins. The third case (010b, Cheetah Run) involves single-step collapse (evaluation drops 80\\% in one interval), and the detector fires reactively at the next available checkpoint. No checkpoint-based monitor can provide advance warning for instantaneous collapse.\n\nTwo false positives occur among seven negative cases (FPR = 2/7, precision = 3/5 = 0.60, F$_1$ = 0.75). Run 009c (no duration embedding) develops genuine late-stage value overestimation unrelated to CIVO; the detector correctly identifies value-performance dissociation, and the alert is arguably useful despite the label mismatch. Run 009a (vanilla baseline) triggers during a transient three-checkpoint eval dip at 85K; the model subsequently recovers to 966, constituting a pure false alarm. In practice, the cost of a false alert (manual checkpoint inspection, minutes) is orders of magnitude lower than the cost of undetected collapse (wasted GPU-hours, corrupted model); moderate FPR is therefore acceptable in this application.\n\nAll three true positives triggered before 65K steps (range 45--65K) while both false positives occurred after 85K (range 85--105K), suggesting that early-training alerts carry higher diagnostic confidence. In practice, alerts before 70K steps can be treated as high-confidence CIVO indicators; later alerts warrant manual inspection.\n\n\\paragraph{Limitations.}\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse (the source of the 009a false alarm). Second, the acceleration condition assumes monotonically increasing overestimation during onset; oscillatory trajectories that eventually collapse could evade detection until acceleration stabilizes. Third, the detector identifies a \\emph{pattern} (rising value-evaluation ratio with declining performance) rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values ($\\tau_\\text{mag} = 0.49$, $\\tau_\\text{vel} = 0.1$) were calibrated on ten runs across two environments; generalization to different reward scales requires further validation.\n",
      "numLines": 237,
      "startLine": 1,
      "totalLines": 237
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

Now I can see the full file. Let me identify all the locations that need fixes:

1. Line 119: "collapsing to 22.7 ($-93\%$)"
2. Line 90: "8.6\% of baseline"
3. Line 54: "1.61$\times$ at 35K"
4. Line 90: "970.41" and percentages using it
5. Line 124: Figure 2 caption with "(008d, 009b)"
6. Need to add footnote about 008d data extension

Let me search for all relevant patterns to be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "917fdab3-9084-4111-9d95-644c30b67dbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qb7LyJwhS4F2cymvGn1u8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7640,
      "cache_read_input_tokens": 25503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7640
      },
      "output_tokens": 3,
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

<details open><summary>🔧 Tool call — Grep · `toolu_013nc883s9CmEsBPDuwqRsZ4`</summary>

```json
{
  "pattern": "970\\.4|22\\.7|8\\.6|1\\.61",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "4b1685f5-991a-408a-b2f7-66e8c5daa06b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qb7LyJwhS4F2cymvGn1u8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7640,
      "cache_read_input_tokens": 25503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7640
      },
      "output_tokens": 3,
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

_source line 9 · 2026-05-17T11:10:11.506Z_

<details><summary>↩ Tool result · `toolu_013nc883s9CmEsBPDuwqRsZ4`</summary>

```text
54:$^*$ Seed 1 only: peak NVE with transient exceedances (1.61$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
90:[Omitted long matching line]
119:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "8f18eafc-531a-4fbe-ab75-4b78c135251a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "54:$^*$ Seed 1 only: peak NVE with transient exceedances (1.61$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n90:[Omitted long matching line]\n119:[Omitted long matching line]",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 10_

Now I have a clear picture. Let me make all the fixes. Let me start with the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "955f78db-a33d-4488-acad-5b6abdc513ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAfojwuVkvu5Xt7QauGYCk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 384,
      "cache_read_input_tokens": 33143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 384
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01SrPJ962P8WwoLpN84PVJcb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "$^*$ Seed 1 only: peak NVE with transient exceedances (1.61$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\",
  "new_string": "$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "625b8072-cfce-47ff-b963-e75e57c4cc53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAfojwuVkvu5Xt7QauGYCk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 384,
      "cache_read_input_tokens": 33143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 384
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

_source line 12 · 2026-05-17T11:10:16.391Z_

<details><summary>↩ Tool result · `toolu_01SrPJ962P8WwoLpN84PVJcb`</summary>

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
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "bf39b842-bacb-4fb6-870a-673acc3fd491",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "$^*$ Seed 1 only: peak NVE with transient exceedances (1.61$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\",
    "newString": "$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & No collapse \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation (Cheetah Run)}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 14.59$\\times$ & Collapsed \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.61$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the causal trigger. Comparing exp\\_008d (trained, subsample ON) against exp\\_008f (no embedding, subsample ON): 008d reaches $\\nve = 4.12\\times$ and collapses (eval 82.8), while 008f maintains $\\nve \\leq 0.97\\times$ (eval 503.0). The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 7/8 seeds (AUROC${=}0.933$; Figure~\\ref{fig:nve_trajectory}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, $n{=}3$) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.3, 21.3\\% of baseline 970.41). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 8.6\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 27.6\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly necessary} for CIVO. Neither factor alone triggers pathological overestimation: trained embedding without multi-rate exposure (008a, NVE $= 0.93\\times$) and multi-rate exposure without embedding (008f, NVE $= 0.97\\times$) both remain well below the $1.5\\times$ diagnostic threshold, while frozen embedding under full exposure (015b) never exceeds $0.47\\times$ (Figure~\\ref{fig:factorial_grid}). Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: $\\dt{=}1$ imagination does not prevent all collapse.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Seed~1 is healthy (eval 869.9, $\\nve = 0.80\\times$); seed~2 collapses (eval $715 \\rightarrow 137$, $\\nve = 3.78\\times$), but via a qualitatively distinct mechanism (Figure~\\ref{fig:multiple_pathways}). Classic CIVO (008d, Pathway~A) shows value explosion followed by evaluation decline with decreasing entropy; 008e\\_v3\\_s2 (Pathway~B) shows evaluation crash with \\emph{increasing} entropy ($-5.21 \\rightarrow -3.83$) while values remain stable. This produces the sole false positive in the NVE classification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe trained embedding in 008d produces a $2.78\\times$ reward prediction gap between $\\dt{=}1$ and $\\dt{=}2$ (Table~\\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes as optimistic value estimates. Having established the mechanistic basis of CIVO, we now ask whether it can be detected during training without access to a reference baseline.\n\n%% ============================================================\n%% F8: Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\n\\paragraph{Motivation.}\nThe Normalized Value Excess ($\\nve$) quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment cannot serve as an early warning.\n\nWe therefore ask whether the \\emph{dynamics} of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. By tracking the trajectory of the value-to-evaluation ratio $r_t = \\bar{V}_t / \\max(\\bar{E}_t, \\varepsilon)$ (with $\\varepsilon = 10^{-6}$ for numerical stability) across checkpoints, a lightweight rule-based detector can flag dangerous overestimation using only quantities available within a single run.\n\nThe causal structure of CIVO motivates acceleration as the key detection signal. CIVO operates as a positive feedback loop: the trained embedding biases reward predictions, which inflate value estimates, which in turn distort actor gradients toward trajectories that reinforce the bias (\\S\\ref{sec:civo_mechanism}). This self-amplifying cycle produces superlinear growth in $r_t$. In healthy training, a natural negative feedback counteracts value growth: improved value estimates yield a better actor, which raises evaluation returns, stabilizing the ratio. CIVO breaks this negative feedback, so sustained positive acceleration in $r_t$ serves as a causal signature that distinguishes pathological divergence from normal value learning.\n\n\\paragraph{Algorithm.}\nThe detector monitors $r_t$ and fires an alert only when four conditions hold simultaneously at checkpoint $t$ (Algorithm~\\ref{alg:civo_detector}). The conjunction makes the detector conservative: any single noisy checkpoint is unlikely to satisfy magnitude, velocity, acceleration, and decline together. The computational cost is negligible (four scalar comparisons per checkpoint, no additional model inference).\n\n\\begin{algorithm}[t]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths where the ratio rises and falls without sustained divergence; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A 2-of-3 majority threshold balances noise robustness against single-checkpoint evaluation variance with sensitivity to sustained decline.\\footnote{A full comparison of window sizes (3/3, 2/3, 2/5) and their trade-offs appears in Appendix~\\ref{sec:appendix_sensitivity}.}\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives, since both false alarms have $r_t > 0.70$ at trigger time. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $3/3$); we retain $0.1$ to avoid overfitting to $n{=}10$ runs.\n\n\\paragraph{Validation.}\nWe apply the detector retrospectively to ten runs spanning three conditions: trained duration embedding (CIVO-positive, $n{=}3$), untrained or absent embedding (CIVO-negative, $n{=}3$), and vanilla baselines ($n{=}4$). Ground truth labels derive from manual inspection: a run is CIVO-positive if it exhibits sustained $\\nve \\geq 1.5\\times$ with subsequent evaluation collapse. Table~\\ref{tab:detector-validation} reports all results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}10$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 3/3 (1.00), \\quad FPR = 2/7 (0.29)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nThe detector identifies all three CIVO-positive runs (TPR = 3/3). Two of three are detected \\emph{predictively}: 008d seed~0 triggers at 45K, one checkpoint before evaluation crosses the 20\\% decline threshold; seed~3 triggers at 45K, a full 50K steps before decline begins. The third case (010b, Cheetah Run) involves single-step collapse (evaluation drops 80\\% in one interval), and the detector fires reactively at the next available checkpoint. No checkpoint-based monitor can provide advance warning for instantaneous collapse.\n\nTwo false positives occur among seven negative cases (FPR = 2/7, precision = 3/5 = 0.60, F$_1$ = 0.75). Run 009c (no duration embedding) develops genuine late-stage value overestimation unrelated to CIVO; the detector correctly identifies value-performance dissociation, and the alert is arguably useful despite the label mismatch. Run 009a (vanilla baseline) triggers during a transient three-checkpoint eval dip at 85K; the model subsequently recovers to 966, constituting a pure false alarm. In practice, the cost of a false alert (manual checkpoint inspection, minutes) is orders of magnitude lower than the cost of undetected collapse (wasted GPU-hours, corrupted model); moderate FPR is therefore acceptable in this application.\n\nAll three true positives triggered before 65K steps (range 45--65K) while both false positives occurred after 85K (range 85--105K), suggesting that early-training alerts carry higher diagnostic confidence. In practice, alerts before 70K steps can be treated as high-confidence CIVO indicators; later alerts warrant manual inspection.\n\n\\paragraph{Limitations.}\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse (the source of the 009a false alarm). Second, the acceleration condition assumes monotonically increasing overestimation during onset; oscillatory trajectories that eventually collapse could evade detection until acceleration stabilizes. Third, the detector identifies a \\emph{pattern} (rising value-evaluation ratio with declining performance) rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values ($\\tau_\\text{mag} = 0.49$, $\\tau_\\text{vel} = 0.1$) were calibrated on ten runs across two environments; generalization to different reward scales requires further validation.\n",
    "structuredPatch": [
      {
        "oldStart": 51,
        "oldLines": 7,
        "newStart": 51,
        "newLines": 7,
        "lines": [
          " exp$^a$ = trained, subsample OFF;",
          " frz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});",
          " --- = removed ($d{=}0$).\\\\",
          "-$^*$ Seed 1 only: peak NVE with transient exceedances (1.61$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\",
          "+$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\",
          " $^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\par}",
          " \\end{table*}",
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

_source line 13_

Now fix 2 and 4 (the F2 paragraph with baseline 970.41 and 8.6%):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "affe8dd3-cda6-4ba4-bd55-4dc363886480",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AY7qTKTyEaf8Ek8UgewHvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 358,
      "cache_read_input_tokens": 33527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 358
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

_source line 14_

<details open><summary>🔧 Tool call — Edit · `toolu_01ENQP9CazwH8nzQYCAEUCGk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "The trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.3, 21.3\\% of baseline 970.41). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 8.6\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 27.6\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).",
  "new_string": "The trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.2, 22.5\\% of baseline). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 9.0\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 29.3\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "25ed58a4-0873-44cd-b2e5-d7963087f4a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AY7qTKTyEaf8Ek8UgewHvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 358,
      "cache_read_input_tokens": 33527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 358
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

_source line 15 · 2026-05-17T11:10:33.497Z_

<details><summary>↩ Tool result · `toolu_01ENQP9CazwH8nzQYCAEUCGk`</summary>

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
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "b1a5b522-3002-495c-bb4a-ad992f86a253",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "The trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.3, 21.3\\% of baseline 970.41). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 8.6\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 27.6\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).",
    "newString": "The trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.2, 22.5\\% of baseline). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 9.0\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 29.3\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & No collapse \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation (Cheetah Run)}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 14.59$\\times$ & Collapsed \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the causal trigger. Comparing exp\\_008d (trained, subsample ON) against exp\\_008f (no embedding, subsample ON): 008d reaches $\\nve = 4.12\\times$ and collapses (eval 82.8), while 008f maintains $\\nve \\leq 0.97\\times$ (eval 503.0). The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 7/8 seeds (AUROC${=}0.933$; Figure~\\ref{fig:nve_trajectory}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, $n{=}3$) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.3, 21.3\\% of baseline 970.41). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 8.6\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 27.6\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly necessary} for CIVO. Neither factor alone triggers pathological overestimation: trained embedding without multi-rate exposure (008a, NVE $= 0.93\\times$) and multi-rate exposure without embedding (008f, NVE $= 0.97\\times$) both remain well below the $1.5\\times$ diagnostic threshold, while frozen embedding under full exposure (015b) never exceeds $0.47\\times$ (Figure~\\ref{fig:factorial_grid}). Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: $\\dt{=}1$ imagination does not prevent all collapse.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Seed~1 is healthy (eval 869.9, $\\nve = 0.80\\times$); seed~2 collapses (eval $715 \\rightarrow 137$, $\\nve = 3.78\\times$), but via a qualitatively distinct mechanism (Figure~\\ref{fig:multiple_pathways}). Classic CIVO (008d, Pathway~A) shows value explosion followed by evaluation decline with decreasing entropy; 008e\\_v3\\_s2 (Pathway~B) shows evaluation crash with \\emph{increasing} entropy ($-5.21 \\rightarrow -3.83$) while values remain stable. This produces the sole false positive in the NVE classification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe trained embedding in 008d produces a $2.78\\times$ reward prediction gap between $\\dt{=}1$ and $\\dt{=}2$ (Table~\\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes as optimistic value estimates. Having established the mechanistic basis of CIVO, we now ask whether it can be detected during training without access to a reference baseline.\n\n%% ============================================================\n%% F8: Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\n\\paragraph{Motivation.}\nThe Normalized Value Excess ($\\nve$) quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment cannot serve as an early warning.\n\nWe therefore ask whether the \\emph{dynamics} of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. By tracking the trajectory of the value-to-evaluation ratio $r_t = \\bar{V}_t / \\max(\\bar{E}_t, \\varepsilon)$ (with $\\varepsilon = 10^{-6}$ for numerical stability) across checkpoints, a lightweight rule-based detector can flag dangerous overestimation using only quantities available within a single run.\n\nThe causal structure of CIVO motivates acceleration as the key detection signal. CIVO operates as a positive feedback loop: the trained embedding biases reward predictions, which inflate value estimates, which in turn distort actor gradients toward trajectories that reinforce the bias (\\S\\ref{sec:civo_mechanism}). This self-amplifying cycle produces superlinear growth in $r_t$. In healthy training, a natural negative feedback counteracts value growth: improved value estimates yield a better actor, which raises evaluation returns, stabilizing the ratio. CIVO breaks this negative feedback, so sustained positive acceleration in $r_t$ serves as a causal signature that distinguishes pathological divergence from normal value learning.\n\n\\paragraph{Algorithm.}\nThe detector monitors $r_t$ and fires an alert only when four conditions hold simultaneously at checkpoint $t$ (Algorithm~\\ref{alg:civo_detector}). The conjunction makes the detector conservative: any single noisy checkpoint is unlikely to satisfy magnitude, velocity, acceleration, and decline together. The computational cost is negligible (four scalar comparisons per checkpoint, no additional model inference).\n\n\\begin{algorithm}[t]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths where the ratio rises and falls without sustained divergence; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A 2-of-3 majority threshold balances noise robustness against single-checkpoint evaluation variance with sensitivity to sustained decline.\\footnote{A full comparison of window sizes (3/3, 2/3, 2/5) and their trade-offs appears in Appendix~\\ref{sec:appendix_sensitivity}.}\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives, since both false alarms have $r_t > 0.70$ at trigger time. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $3/3$); we retain $0.1$ to avoid overfitting to $n{=}10$ runs.\n\n\\paragraph{Validation.}\nWe apply the detector retrospectively to ten runs spanning three conditions: trained duration embedding (CIVO-positive, $n{=}3$), untrained or absent embedding (CIVO-negative, $n{=}3$), and vanilla baselines ($n{=}4$). Ground truth labels derive from manual inspection: a run is CIVO-positive if it exhibits sustained $\\nve \\geq 1.5\\times$ with subsequent evaluation collapse. Table~\\ref{tab:detector-validation} reports all results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}10$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 3/3 (1.00), \\quad FPR = 2/7 (0.29)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nThe detector identifies all three CIVO-positive runs (TPR = 3/3). Two of three are detected \\emph{predictively}: 008d seed~0 triggers at 45K, one checkpoint before evaluation crosses the 20\\% decline threshold; seed~3 triggers at 45K, a full 50K steps before decline begins. The third case (010b, Cheetah Run) involves single-step collapse (evaluation drops 80\\% in one interval), and the detector fires reactively at the next available checkpoint. No checkpoint-based monitor can provide advance warning for instantaneous collapse.\n\nTwo false positives occur among seven negative cases (FPR = 2/7, precision = 3/5 = 0.60, F$_1$ = 0.75). Run 009c (no duration embedding) develops genuine late-stage value overestimation unrelated to CIVO; the detector correctly identifies value-performance dissociation, and the alert is arguably useful despite the label mismatch. Run 009a (vanilla baseline) triggers during a transient three-checkpoint eval dip at 85K; the model subsequently recovers to 966, constituting a pure false alarm. In practice, the cost of a false alert (manual checkpoint inspection, minutes) is orders of magnitude lower than the cost of undetected collapse (wasted GPU-hours, corrupted model); moderate FPR is therefore acceptable in this application.\n\nAll three true positives triggered before 65K steps (range 45--65K) while both false positives occurred after 85K (range 85--105K), suggesting that early-training alerts carry higher diagnostic confidence. In practice, alerts before 70K steps can be treated as high-confidence CIVO indicators; later alerts warrant manual inspection.\n\n\\paragraph{Limitations.}\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse (the source of the 009a false alarm). Second, the acceleration condition assumes monotonically increasing overestimation during onset; oscillatory trajectories that eventually collapse could evade detection until acceleration stabilizes. Third, the detector identifies a \\emph{pattern} (rising value-evaluation ratio with declining performance) rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values ($\\tau_\\text{mag} = 0.49$, $\\tau_\\text{vel} = 0.1$) were calibrated on ten runs across two environments; generalization to different reward scales requires further validation.\n",
    "structuredPatch": [
      {
        "oldStart": 87,
        "oldLines": 7,
        "newStart": 87,
        "newLines": 7,
        "lines": [
          " \\label{fig:nve_trajectory}",
          " \\end{figure}",
          " ",
          "-The trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.3, 21.3\\% of baseline 970.41). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 8.6\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 27.6\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).",
          "+The trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.2, 22.5\\% of baseline). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 9.0\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 29.3\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).",
          " ",
          " %% ============================================================",
          " %% F3--F5: Summary (details in Appendix B)"
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

_source line 16_

Now fix 1 (Cheetah "collapsing to 22.7" in F6-F7):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "4df93c6c-3d47-407c-9c0d-135c950e076a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BxRxcuqVQG8mkNPVP3Bmf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 33885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 825
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

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01Xfg8RYh8AFc15CucJwuqjp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.",
  "new_string": "Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before declining to 51.7 at 105K ($-84\\%$, minimum 22.7 at 65K); peak NVE $14.59\\times$."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "760d9dd9-49bb-4255-bc4b-d8c482df6458",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BxRxcuqVQG8mkNPVP3Bmf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 33885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 825
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

_source line 18 · 2026-05-17T11:10:39.614Z_

<details><summary>↩ Tool result · `toolu_01Xfg8RYh8AFc15CucJwuqjp`</summary>

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
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "e2fe6156-808a-4d99-98d0-e444bbb4b04b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.",
    "newString": "Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before declining to 51.7 at 105K ($-84\\%$, minimum 22.7 at 65K); peak NVE $14.59\\times$.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & No collapse \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation (Cheetah Run)}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 14.59$\\times$ & Collapsed \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the causal trigger. Comparing exp\\_008d (trained, subsample ON) against exp\\_008f (no embedding, subsample ON): 008d reaches $\\nve = 4.12\\times$ and collapses (eval 82.8), while 008f maintains $\\nve \\leq 0.97\\times$ (eval 503.0). The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 7/8 seeds (AUROC${=}0.933$; Figure~\\ref{fig:nve_trajectory}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, $n{=}3$) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.2, 22.5\\% of baseline). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 9.0\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 29.3\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly necessary} for CIVO. Neither factor alone triggers pathological overestimation: trained embedding without multi-rate exposure (008a, NVE $= 0.93\\times$) and multi-rate exposure without embedding (008f, NVE $= 0.97\\times$) both remain well below the $1.5\\times$ diagnostic threshold, while frozen embedding under full exposure (015b) never exceeds $0.47\\times$ (Figure~\\ref{fig:factorial_grid}). Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: $\\dt{=}1$ imagination does not prevent all collapse.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Seed~1 is healthy (eval 869.9, $\\nve = 0.80\\times$); seed~2 collapses (eval $715 \\rightarrow 137$, $\\nve = 3.78\\times$), but via a qualitatively distinct mechanism (Figure~\\ref{fig:multiple_pathways}). Classic CIVO (008d, Pathway~A) shows value explosion followed by evaluation decline with decreasing entropy; 008e\\_v3\\_s2 (Pathway~B) shows evaluation crash with \\emph{increasing} entropy ($-5.21 \\rightarrow -3.83$) while values remain stable. This produces the sole false positive in the NVE classification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe trained embedding in 008d produces a $2.78\\times$ reward prediction gap between $\\dt{=}1$ and $\\dt{=}2$ (Table~\\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes as optimistic value estimates. Having established the mechanistic basis of CIVO, we now ask whether it can be detected during training without access to a reference baseline.\n\n%% ============================================================\n%% F8: Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\n\\paragraph{Motivation.}\nThe Normalized Value Excess ($\\nve$) quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment cannot serve as an early warning.\n\nWe therefore ask whether the \\emph{dynamics} of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. By tracking the trajectory of the value-to-evaluation ratio $r_t = \\bar{V}_t / \\max(\\bar{E}_t, \\varepsilon)$ (with $\\varepsilon = 10^{-6}$ for numerical stability) across checkpoints, a lightweight rule-based detector can flag dangerous overestimation using only quantities available within a single run.\n\nThe causal structure of CIVO motivates acceleration as the key detection signal. CIVO operates as a positive feedback loop: the trained embedding biases reward predictions, which inflate value estimates, which in turn distort actor gradients toward trajectories that reinforce the bias (\\S\\ref{sec:civo_mechanism}). This self-amplifying cycle produces superlinear growth in $r_t$. In healthy training, a natural negative feedback counteracts value growth: improved value estimates yield a better actor, which raises evaluation returns, stabilizing the ratio. CIVO breaks this negative feedback, so sustained positive acceleration in $r_t$ serves as a causal signature that distinguishes pathological divergence from normal value learning.\n\n\\paragraph{Algorithm.}\nThe detector monitors $r_t$ and fires an alert only when four conditions hold simultaneously at checkpoint $t$ (Algorithm~\\ref{alg:civo_detector}). The conjunction makes the detector conservative: any single noisy checkpoint is unlikely to satisfy magnitude, velocity, acceleration, and decline together. The computational cost is negligible (four scalar comparisons per checkpoint, no additional model inference).\n\n\\begin{algorithm}[t]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths where the ratio rises and falls without sustained divergence; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A 2-of-3 majority threshold balances noise robustness against single-checkpoint evaluation variance with sensitivity to sustained decline.\\footnote{A full comparison of window sizes (3/3, 2/3, 2/5) and their trade-offs appears in Appendix~\\ref{sec:appendix_sensitivity}.}\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives, since both false alarms have $r_t > 0.70$ at trigger time. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $3/3$); we retain $0.1$ to avoid overfitting to $n{=}10$ runs.\n\n\\paragraph{Validation.}\nWe apply the detector retrospectively to ten runs spanning three conditions: trained duration embedding (CIVO-positive, $n{=}3$), untrained or absent embedding (CIVO-negative, $n{=}3$), and vanilla baselines ($n{=}4$). Ground truth labels derive from manual inspection: a run is CIVO-positive if it exhibits sustained $\\nve \\geq 1.5\\times$ with subsequent evaluation collapse. Table~\\ref{tab:detector-validation} reports all results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}10$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 3/3 (1.00), \\quad FPR = 2/7 (0.29)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nThe detector identifies all three CIVO-positive runs (TPR = 3/3). Two of three are detected \\emph{predictively}: 008d seed~0 triggers at 45K, one checkpoint before evaluation crosses the 20\\% decline threshold; seed~3 triggers at 45K, a full 50K steps before decline begins. The third case (010b, Cheetah Run) involves single-step collapse (evaluation drops 80\\% in one interval), and the detector fires reactively at the next available checkpoint. No checkpoint-based monitor can provide advance warning for instantaneous collapse.\n\nTwo false positives occur among seven negative cases (FPR = 2/7, precision = 3/5 = 0.60, F$_1$ = 0.75). Run 009c (no duration embedding) develops genuine late-stage value overestimation unrelated to CIVO; the detector correctly identifies value-performance dissociation, and the alert is arguably useful despite the label mismatch. Run 009a (vanilla baseline) triggers during a transient three-checkpoint eval dip at 85K; the model subsequently recovers to 966, constituting a pure false alarm. In practice, the cost of a false alert (manual checkpoint inspection, minutes) is orders of magnitude lower than the cost of undetected collapse (wasted GPU-hours, corrupted model); moderate FPR is therefore acceptable in this application.\n\nAll three true positives triggered before 65K steps (range 45--65K) while both false positives occurred after 85K (range 85--105K), suggesting that early-training alerts carry higher diagnostic confidence. In practice, alerts before 70K steps can be treated as high-confidence CIVO indicators; later alerts warrant manual inspection.\n\n\\paragraph{Limitations.}\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse (the source of the 009a false alarm). Second, the acceleration condition assumes monotonically increasing overestimation during onset; oscillatory trajectories that eventually collapse could evade detection until acceleration stabilizes. Third, the detector identifies a \\emph{pattern} (rising value-evaluation ratio with declining performance) rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values ($\\tau_\\text{mag} = 0.49$, $\\tau_\\text{vel} = 0.1$) were calibrated on ten runs across two environments; generalization to different reward scales requires further validation.\n",
    "structuredPatch": [
      {
        "oldStart": 116,
        "oldLines": 7,
        "newStart": 116,
        "newLines": 7,
        "lines": [
          " \\end{figure}",
          " ",
          " \\paragraph{F7: Full-pathway gradient stopping shows mixed results.}",
          "-Exp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before collapsing to 22.7 ($-93\\%$); peak NVE $14.59\\times$.",
          "+Exp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before declining to 51.7 at 105K ($-84\\%$, minimum 22.7 at 65K); peak NVE $14.59\\times$.",
          " ",
          " \\begin{figure}[t]",
          " \\centering"
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

_source line 19_

Now fix 5 (Figure 2 caption). The caption at line 124 mentions "(008d, 009b)" — let me check what the actual data source is. Based on the task description, the figure uses 008d (via 009e continuation). Let me update the caption and also add the footnote for fix 6:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "fc8403a6-a777-4b37-8161-9ddb19a97e52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6TCzZnSJWGauTCGcyw5RR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 34710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 360
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

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01W8Sz2D9HLcjUFgteB65gii`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}",
  "new_string": "\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d)\\footnotemark: DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "2cc32d81-cb8a-413d-8dad-bb9a8d7742f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6TCzZnSJWGauTCGcyw5RR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 34710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 360
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

_source line 21 · 2026-05-17T11:10:54.576Z_

<details><summary>↩ Tool result · `toolu_01W8Sz2D9HLcjUFgteB65gii`</summary>

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
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "18e62fab-4d73-454a-acaa-34f0960a39a5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}",
    "newString": "\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d)\\footnotemark: DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & No collapse \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation (Cheetah Run)}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 14.59$\\times$ & Collapsed \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the causal trigger. Comparing exp\\_008d (trained, subsample ON) against exp\\_008f (no embedding, subsample ON): 008d reaches $\\nve = 4.12\\times$ and collapses (eval 82.8), while 008f maintains $\\nve \\leq 0.97\\times$ (eval 503.0). The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 7/8 seeds (AUROC${=}0.933$; Figure~\\ref{fig:nve_trajectory}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, $n{=}3$) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.2, 22.5\\% of baseline). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 9.0\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 29.3\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly necessary} for CIVO. Neither factor alone triggers pathological overestimation: trained embedding without multi-rate exposure (008a, NVE $= 0.93\\times$) and multi-rate exposure without embedding (008f, NVE $= 0.97\\times$) both remain well below the $1.5\\times$ diagnostic threshold, while frozen embedding under full exposure (015b) never exceeds $0.47\\times$ (Figure~\\ref{fig:factorial_grid}). Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: $\\dt{=}1$ imagination does not prevent all collapse.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Seed~1 is healthy (eval 869.9, $\\nve = 0.80\\times$); seed~2 collapses (eval $715 \\rightarrow 137$, $\\nve = 3.78\\times$), but via a qualitatively distinct mechanism (Figure~\\ref{fig:multiple_pathways}). Classic CIVO (008d, Pathway~A) shows value explosion followed by evaluation decline with decreasing entropy; 008e\\_v3\\_s2 (Pathway~B) shows evaluation crash with \\emph{increasing} entropy ($-5.21 \\rightarrow -3.83$) while values remain stable. This produces the sole false positive in the NVE classification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before declining to 51.7 at 105K ($-84\\%$, minimum 22.7 at 65K); peak NVE $14.59\\times$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe trained embedding in 008d produces a $2.78\\times$ reward prediction gap between $\\dt{=}1$ and $\\dt{=}2$ (Table~\\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes as optimistic value estimates. Having established the mechanistic basis of CIVO, we now ask whether it can be detected during training without access to a reference baseline.\n\n%% ============================================================\n%% F8: Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\n\\paragraph{Motivation.}\nThe Normalized Value Excess ($\\nve$) quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment cannot serve as an early warning.\n\nWe therefore ask whether the \\emph{dynamics} of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. By tracking the trajectory of the value-to-evaluation ratio $r_t = \\bar{V}_t / \\max(\\bar{E}_t, \\varepsilon)$ (with $\\varepsilon = 10^{-6}$ for numerical stability) across checkpoints, a lightweight rule-based detector can flag dangerous overestimation using only quantities available within a single run.\n\nThe causal structure of CIVO motivates acceleration as the key detection signal. CIVO operates as a positive feedback loop: the trained embedding biases reward predictions, which inflate value estimates, which in turn distort actor gradients toward trajectories that reinforce the bias (\\S\\ref{sec:civo_mechanism}). This self-amplifying cycle produces superlinear growth in $r_t$. In healthy training, a natural negative feedback counteracts value growth: improved value estimates yield a better actor, which raises evaluation returns, stabilizing the ratio. CIVO breaks this negative feedback, so sustained positive acceleration in $r_t$ serves as a causal signature that distinguishes pathological divergence from normal value learning.\n\n\\paragraph{Algorithm.}\nThe detector monitors $r_t$ and fires an alert only when four conditions hold simultaneously at checkpoint $t$ (Algorithm~\\ref{alg:civo_detector}). The conjunction makes the detector conservative: any single noisy checkpoint is unlikely to satisfy magnitude, velocity, acceleration, and decline together. The computational cost is negligible (four scalar comparisons per checkpoint, no additional model inference).\n\n\\begin{algorithm}[t]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths where the ratio rises and falls without sustained divergence; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A 2-of-3 majority threshold balances noise robustness against single-checkpoint evaluation variance with sensitivity to sustained decline.\\footnote{A full comparison of window sizes (3/3, 2/3, 2/5) and their trade-offs appears in Appendix~\\ref{sec:appendix_sensitivity}.}\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives, since both false alarms have $r_t > 0.70$ at trigger time. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $3/3$); we retain $0.1$ to avoid overfitting to $n{=}10$ runs.\n\n\\paragraph{Validation.}\nWe apply the detector retrospectively to ten runs spanning three conditions: trained duration embedding (CIVO-positive, $n{=}3$), untrained or absent embedding (CIVO-negative, $n{=}3$), and vanilla baselines ($n{=}4$). Ground truth labels derive from manual inspection: a run is CIVO-positive if it exhibits sustained $\\nve \\geq 1.5\\times$ with subsequent evaluation collapse. Table~\\ref{tab:detector-validation} reports all results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}10$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 3/3 (1.00), \\quad FPR = 2/7 (0.29)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nThe detector identifies all three CIVO-positive runs (TPR = 3/3). Two of three are detected \\emph{predictively}: 008d seed~0 triggers at 45K, one checkpoint before evaluation crosses the 20\\% decline threshold; seed~3 triggers at 45K, a full 50K steps before decline begins. The third case (010b, Cheetah Run) involves single-step collapse (evaluation drops 80\\% in one interval), and the detector fires reactively at the next available checkpoint. No checkpoint-based monitor can provide advance warning for instantaneous collapse.\n\nTwo false positives occur among seven negative cases (FPR = 2/7, precision = 3/5 = 0.60, F$_1$ = 0.75). Run 009c (no duration embedding) develops genuine late-stage value overestimation unrelated to CIVO; the detector correctly identifies value-performance dissociation, and the alert is arguably useful despite the label mismatch. Run 009a (vanilla baseline) triggers during a transient three-checkpoint eval dip at 85K; the model subsequently recovers to 966, constituting a pure false alarm. In practice, the cost of a false alert (manual checkpoint inspection, minutes) is orders of magnitude lower than the cost of undetected collapse (wasted GPU-hours, corrupted model); moderate FPR is therefore acceptable in this application.\n\nAll three true positives triggered before 65K steps (range 45--65K) while both false positives occurred after 85K (range 85--105K), suggesting that early-training alerts carry higher diagnostic confidence. In practice, alerts before 70K steps can be treated as high-confidence CIVO indicators; later alerts warrant manual inspection.\n\n\\paragraph{Limitations.}\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse (the source of the 009a false alarm). Second, the acceleration condition assumes monotonically increasing overestimation during onset; oscillatory trajectories that eventually collapse could evade detection until acceleration stabilizes. Third, the detector identifies a \\emph{pattern} (rising value-evaluation ratio with declining performance) rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values ($\\tau_\\text{mag} = 0.49$, $\\tau_\\text{vel} = 0.1$) were calibrated on ten runs across two environments; generalization to different reward scales requires further validation.\n",
    "structuredPatch": [
      {
        "oldStart": 121,
        "oldLines": 7,
        "newStart": 121,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}",
          "-\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d, 009b): DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data, two seeds. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}",
          "+\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d)\\footnotemark: DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}",
          " \\label{fig:civo_decomposition}",
          " \\end{figure}",
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

_source line 22_

Now add the footnote text after the figure environment (fix 6):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "4dab03ac-4576-409c-a5fa-f486165c7d9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrJGucB6KDzuo22tDqonNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 897,
      "cache_read_input_tokens": 35070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 897
      },
      "output_tokens": 6,
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

<details open><summary>🔧 Tool call — Edit · `toolu_018Nj6VkBCJ2sbKWqGLrcTUb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "old_string": "\\label{fig:civo_decomposition}\n\\end{figure}",
  "new_string": "\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "eac4d4f3-a7cb-4e3d-af59-dca5acb6be2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrJGucB6KDzuo22tDqonNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 897,
      "cache_read_input_tokens": 35070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 897
      },
      "output_tokens": 6,
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

_source line 24 · 2026-05-17T11:10:59.766Z_

<details><summary>↩ Tool result · `toolu_018Nj6VkBCJ2sbKWqGLrcTUb`</summary>

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
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "db510f80-bd4f-4473-a2f6-85735886b461",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "oldString": "\\label{fig:civo_decomposition}\n\\end{figure}",
    "newString": "\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\\nve$, \\S\\ref{sec:metrics}).\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{All configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 0.47$\\times$ & Grad.\\ starvation \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & No collapse \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.80$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation (Cheetah Run)}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 14.59$\\times$ & Collapsed \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the causal trigger. Comparing exp\\_008d (trained, subsample ON) against exp\\_008f (no embedding, subsample ON): 008d reaches $\\nve = 4.12\\times$ and collapses (eval 82.8), while 008f maintains $\\nve \\leq 0.97\\times$ (eval 503.0). The $\\nve \\geq 1.5\\times$ threshold (35K+ window) correctly classifies 7/8 seeds (AUROC${=}0.933$; Figure~\\ref{fig:nve_trajectory}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, $n{=}3$) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.2, 22.5\\% of baseline). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 9.0\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 29.3\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Factorial Ablation (Appendix~\\ref{sec:appendix_factorial})}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding and multi-rate data exposure are \\emph{jointly necessary} for CIVO. Neither factor alone triggers pathological overestimation: trained embedding without multi-rate exposure (008a, NVE $= 0.93\\times$) and multi-rate exposure without embedding (008f, NVE $= 0.97\\times$) both remain well below the $1.5\\times$ diagnostic threshold, while frozen embedding under full exposure (015b) never exceeds $0.47\\times$ (Figure~\\ref{fig:factorial_grid}). Degradation scales monotonically with $\\dt$ ($-47\\%$ at $\\dt{=}2$, $-81\\%$ at $\\dt{=}4$; Figure~\\ref{fig:dt_amplification}).\n\n%% ============================================================\n%% F6--F7: Interventions and cross-environment\n%% ============================================================\n\n\\subsection{F6--F7: Interventions and Multiple Pathways}\n\\label{sec:f6}\n\n\\paragraph{F6: $\\dt{=}1$ imagination does not prevent all collapse.}\nExp\\_008e\\_v3 restricts imagination to $\\dt{=}1$ while retaining the trained embedding. Seed~1 is healthy (eval 869.9, $\\nve = 0.80\\times$); seed~2 collapses (eval $715 \\rightarrow 137$, $\\nve = 3.78\\times$), but via a qualitatively distinct mechanism (Figure~\\ref{fig:multiple_pathways}). Classic CIVO (008d, Pathway~A) shows value explosion followed by evaluation decline with decreasing entropy; 008e\\_v3\\_s2 (Pathway~B) shows evaluation crash with \\emph{increasing} entropy ($-5.21 \\rightarrow -3.83$) while values remain stable. This produces the sole false positive in the NVE classification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting collapse dynamics. \\textbf{Left:} 008d (CIVO), value explosion with entropy decrease. \\textbf{Right:} 008e\\_v3 s2 (non-CIVO), evaluation crash with entropy increase.}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before declining to 51.7 at 105K ($-84\\%$, minimum 22.7 at 65K); peak NVE $14.59\\times$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d)\\footnotemark: DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n\n\\begin{table}[t]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe trained embedding in 008d produces a $2.78\\times$ reward prediction gap between $\\dt{=}1$ and $\\dt{=}2$ (Table~\\ref{tab:rssm_fidelity}), providing the systematic bias that the critic internalizes as optimistic value estimates. Having established the mechanistic basis of CIVO, we now ask whether it can be detected during training without access to a reference baseline.\n\n%% ============================================================\n%% F8: Online CIVO Detection\n%% ============================================================\n\n\\subsection{Online CIVO Detection}\n\\label{sec:detector}\n\n\\paragraph{Motivation.}\nThe Normalized Value Excess ($\\nve$) quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment cannot serve as an early warning.\n\nWe therefore ask whether the \\emph{dynamics} of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. By tracking the trajectory of the value-to-evaluation ratio $r_t = \\bar{V}_t / \\max(\\bar{E}_t, \\varepsilon)$ (with $\\varepsilon = 10^{-6}$ for numerical stability) across checkpoints, a lightweight rule-based detector can flag dangerous overestimation using only quantities available within a single run.\n\nThe causal structure of CIVO motivates acceleration as the key detection signal. CIVO operates as a positive feedback loop: the trained embedding biases reward predictions, which inflate value estimates, which in turn distort actor gradients toward trajectories that reinforce the bias (\\S\\ref{sec:civo_mechanism}). This self-amplifying cycle produces superlinear growth in $r_t$. In healthy training, a natural negative feedback counteracts value growth: improved value estimates yield a better actor, which raises evaluation returns, stabilizing the ratio. CIVO breaks this negative feedback, so sustained positive acceleration in $r_t$ serves as a causal signature that distinguishes pathological divergence from normal value learning.\n\n\\paragraph{Algorithm.}\nThe detector monitors $r_t$ and fires an alert only when four conditions hold simultaneously at checkpoint $t$ (Algorithm~\\ref{alg:civo_detector}). The conjunction makes the detector conservative: any single noisy checkpoint is unlikely to satisfy magnitude, velocity, acceleration, and decline together. The computational cost is negligible (four scalar comparisons per checkpoint, no additional model inference).\n\n\\begin{algorithm}[t]\n\\caption{Online CIVO Detector}\n\\label{alg:civo_detector}\n\\begin{algorithmic}[1]\n\\REQUIRE Stream of $(\\bar{V}_t, \\bar{E}_t)$ at each checkpoint $t$\n\\STATE $\\tau_\\text{mag} \\leftarrow 0.49$, \\quad $\\tau_\\text{vel} \\leftarrow 0.1$, \\quad $\\varepsilon \\leftarrow 10^{-6}$\n\\STATE Initialize $r_\\text{prev} \\leftarrow 0$, $\\Delta r_\\text{prev} \\leftarrow 0$, $\\mathcal{H} \\leftarrow []$\n\\FOR{each checkpoint $t$}\n  \\STATE $r_t \\leftarrow \\bar{V}_t \\,/\\, \\max(\\bar{E}_t,\\, \\varepsilon)$\n  \\STATE $\\Delta r_t \\leftarrow r_t - r_\\text{prev}$\n  \\STATE $c_\\text{mag} \\leftarrow (r_t \\geq \\tau_\\text{mag})$\n  \\STATE $c_\\text{vel} \\leftarrow (\\Delta r_t > \\tau_\\text{vel})$\n  \\STATE $c_\\text{acc} \\leftarrow (\\Delta r_\\text{prev} > \\tau_\\text{vel}) \\wedge (\\Delta r_t > \\Delta r_\\text{prev})$\n  \\STATE $c_\\text{dec} \\leftarrow \\bigl|\\{i : \\mathcal{H}[i] < \\mathcal{H}[i{-}1],\\; i \\in \\text{last 3}\\}\\bigr| \\geq 2$\n  \\IF{$c_\\text{mag} \\wedge c_\\text{vel} \\wedge c_\\text{acc} \\wedge c_\\text{dec}$}\n    \\STATE \\textbf{Alert:} CIVO onset at step $t$\n  \\ENDIF\n  \\STATE $r_\\text{prev} \\leftarrow r_t$, \\quad $\\Delta r_\\text{prev} \\leftarrow \\Delta r_t$\n  \\STATE Append $\\bar{E}_t$ to $\\mathcal{H}$\n\\ENDFOR\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths where the ratio rises and falls without sustained divergence; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A 2-of-3 majority threshold balances noise robustness against single-checkpoint evaluation variance with sensitivity to sustained decline.\\footnote{A full comparison of window sizes (3/3, 2/3, 2/5) and their trade-offs appears in Appendix~\\ref{sec:appendix_sensitivity}.}\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives, since both false alarms have $r_t > 0.70$ at trigger time. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $3/3$); we retain $0.1$ to avoid overfitting to $n{=}10$ runs.\n\n\\paragraph{Validation.}\nWe apply the detector retrospectively to ten runs spanning three conditions: trained duration embedding (CIVO-positive, $n{=}3$), untrained or absent embedding (CIVO-negative, $n{=}3$), and vanilla baselines ($n{=}4$). Ground truth labels derive from manual inspection: a run is CIVO-positive if it exhibits sustained $\\nve \\geq 1.5\\times$ with subsequent evaluation collapse. Table~\\ref{tab:detector-validation} reports all results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}10$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 3/3 (1.00), \\quad FPR = 2/7 (0.29)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nThe detector identifies all three CIVO-positive runs (TPR = 3/3). Two of three are detected \\emph{predictively}: 008d seed~0 triggers at 45K, one checkpoint before evaluation crosses the 20\\% decline threshold; seed~3 triggers at 45K, a full 50K steps before decline begins. The third case (010b, Cheetah Run) involves single-step collapse (evaluation drops 80\\% in one interval), and the detector fires reactively at the next available checkpoint. No checkpoint-based monitor can provide advance warning for instantaneous collapse.\n\nTwo false positives occur among seven negative cases (FPR = 2/7, precision = 3/5 = 0.60, F$_1$ = 0.75). Run 009c (no duration embedding) develops genuine late-stage value overestimation unrelated to CIVO; the detector correctly identifies value-performance dissociation, and the alert is arguably useful despite the label mismatch. Run 009a (vanilla baseline) triggers during a transient three-checkpoint eval dip at 85K; the model subsequently recovers to 966, constituting a pure false alarm. In practice, the cost of a false alert (manual checkpoint inspection, minutes) is orders of magnitude lower than the cost of undetected collapse (wasted GPU-hours, corrupted model); moderate FPR is therefore acceptable in this application.\n\nAll three true positives triggered before 65K steps (range 45--65K) while both false positives occurred after 85K (range 85--105K), suggesting that early-training alerts carry higher diagnostic confidence. In practice, alerts before 70K steps can be treated as high-confidence CIVO indicators; later alerts warrant manual inspection.\n\n\\paragraph{Limitations.}\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse (the source of the 009a false alarm). Second, the acceleration condition assumes monotonically increasing overestimation during onset; oscillatory trajectories that eventually collapse could evade detection until acceleration stabilizes. Third, the detector identifies a \\emph{pattern} (rising value-evaluation ratio with declining performance) rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values ($\\tau_\\text{mag} = 0.49$, $\\tau_\\text{vel} = 0.1$) were calibrated on ten runs across two environments; generalization to different reward scales requires further validation.\n",
    "structuredPatch": [
      {
        "oldStart": 124,
        "oldLines": 6,
        "newStart": 124,
        "newLines": 7,
        "lines": [
          " \\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d)\\footnotemark: DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}",
          " \\label{fig:civo_decomposition}",
          " \\end{figure}",
          "+\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}",
          " ",
          " %% ============================================================",
          " %% TABLE 2: RSSM Fidelity"
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

Now let me check if there are any other references to 970.41 or percentages that need updating elsewhere in the file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "9f3fa45c-fa74-4087-aa0c-b2b7411e93c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeZQKHN9K8q2igGWBeBmwt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 288,
      "cache_read_input_tokens": 35967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 288
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

_source line 26_

<details open><summary>🔧 Tool call — Grep · `toolu_018WUTREuE4emB2uzkT3sjuQ`</summary>

```json
{
  "pattern": "970",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "70d27a3b-9fab-46df-9d33-beab50a27457",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeZQKHN9K8q2igGWBeBmwt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 288,
      "cache_read_input_tokens": 35967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 288
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

_source line 27 · 2026-05-17T11:11:03.871Z_

<details><summary>↩ Tool result · `toolu_018WUTREuE4emB2uzkT3sjuQ`</summary>

```text
217:baseline s1 & vanilla & TN & -- & -- & 970 & -- \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "d4893bd7-c80a-4749-8bd1-f1e7b9887cb8",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "217:baseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 28_

That's fine — it's just reporting a peak eval value in the detector validation table, not used as a baseline denominator.

Let me also check the F1 section percentages (line 65) which use baseline 915.7:

Line 65: "132.9 ($14\%$ of baseline)" → 132.9/915.7 = 14.5% ≈ 14% ✓
"176.9 ($19\%$)" → 176.9/915.7 = 19.3% ≈ 19% ✓
"98.8 ($11\%$)" → 98.8/915.7 = 10.8% ≈ 11% ✓

Those are all consistent with baseline 915.7 already.

Let me verify the final file looks correct around the edited sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "2659138d-7ee3-43a5-b990-85e32af5973b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCeFAkhQ8dNhtAc86tYhLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 36255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_018yr776W4rhvc19tMMqNMHb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": 50,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "77e80ced-5e20-4aa6-9139-b30a3551f265",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCeFAkhQ8dNhtAc86tYhLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 36255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

_source line 30 · 2026-05-17T11:11:11.845Z_

<details><summary>↩ Tool result · `toolu_018yr776W4rhvc19tMMqNMHb`</summary>

```text
50	trn$^\ddagger$ = full-pathway SGS (all non-KL gradients detached);
51	exp$^a$ = trained, subsample OFF;
52	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
53	--- = removed ($d{=}0$).\\
54	$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
55	$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\par}
56	\end{table*}
57	
58	%% ============================================================
59	%% F1: All dt>1 degrade
60	%% ============================================================
61	
62	\subsection{F1: All Variable-Rate Configurations Degrade}
63	\label{sec:f1}
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "b853512c-f383-464e-b33d-dcb34037b11b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
      "content": "trn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F1: All dt>1 degrade\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:f1}\n",
      "numLines": 15,
      "startLine": 50,
      "totalLines": 238
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01XR6Kgw35ACSwvDFQZTvPrY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": 86,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "9eea8a36-c14c-4363-b9f4-2b8038450097",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCeFAkhQ8dNhtAc86tYhLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 36255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

_source line 32 · 2026-05-17T11:11:12.789Z_

<details><summary>↩ Tool result · `toolu_01XR6Kgw35ACSwvDFQZTvPrY`</summary>

```text
86	\caption{NVE trajectories (mean $\pm$ seed range). Trained $\dt$-embedding (red, $n{=}3$) exceeds the $1.5\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}
87	\label{fig:nve_trajectory}
88	\end{figure}
89	
90	The trained $\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\times$, $1.62\times$, $1.53\times$; all $\geq 1.5\times$ threshold), universally degrading performance to below 30\% of baseline (mean eval 206.2, 22.5\% of baseline). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 9.0\% of baseline), seed~3 (008d\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 29.3\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\ref{sec:seed_divergence}).
91	
92	%% ============================================================
93	%% F3--F5: Summary (details in Appendix B)
94	%% ============================================================
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "9b524adb-3053-48a0-8a40-5138adc01419",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
      "content": "\\caption{NVE trajectories (mean $\\pm$ seed range). Trained $\\dt$-embedding (red, $n{=}3$) exceeds the $1.5\\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding triggers CIVO in all three tested seeds (peak NVE: $4.12\\times$, $1.62\\times$, $1.53\\times$; all $\\geq 1.5\\times$ threshold), universally degrading performance to below 30\\% of baseline (mean eval 206.2, 22.5\\% of baseline). Downstream trajectories diverge: seed~1 (008d) undergoes immediate full collapse (eval 82.8, 9.0\\% of baseline), seed~3 (008d\\_s3) exhibits late-onset collapse still in progress at 105K (eval 268, train returns declining 70\\% over final 8K steps), while seed~2 (009b) self-corrects after transient overestimation (eval 267.9, 29.3\\% of baseline). This pattern establishes universal CIVO onset with stochastic downstream resolution: collapse is the majority outcome (2/3 seeds) but exhibits variable onset timing (35K vs 70K steps). The 1/3 self-correction case remains severely degraded, confirming that CIVO universally damages performance regardless of whether full collapse follows (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n",
      "numLines": 10,
      "startLine": 86,
      "totalLines": 238
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01XdygYyFz14ZX5ksHhHnD5j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": 115,
  "limit": 18
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "b36d3678-476e-4bac-a48d-c539c7c1929c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCeFAkhQ8dNhtAc86tYhLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 36255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

_source line 34 · 2026-05-17T11:11:13.495Z_

<details><summary>↩ Tool result · `toolu_01XdygYyFz14ZX5ksHhHnD5j`</summary>

```text
115	\label{fig:multiple_pathways}
116	\end{figure}
117	
118	\paragraph{F7: Full-pathway gradient stopping shows mixed results.}
119	Exp\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\dt$-embedding alone produces $-73\%$ peak and $-86\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \sgseval{}, $-51\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\%$), yielding a 50\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before declining to 51.7 at 105K ($-84\%$, minimum 22.7 at 65K); peak NVE $14.59\times$.
120	
121	\begin{figure}[t]
122	\centering
123	\includegraphics[width=0.75\columnwidth]{figures/fig2_civo_decomposition.pdf}
124	\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \textbf{Trained dt-emb} (008d)\footnotemark: DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data. \textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\dt}$, two seeds. Trained $\dt$-embedding degrades peak eval by $73\%$ and final eval by $86\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\%$ final, no collapse) but seed~2 collapses ($-96\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\%$). All percentages relative to Baseline 001.}
125	\label{fig:civo_decomposition}
126	\end{figure}
127	\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}
128	
129	%% ============================================================
130	%% TABLE 2: RSSM Fidelity
131	%% ============================================================
132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "ef3d6059-cd40-406f-b6d4-17370c0d8445",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
      "content": "\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nExp\\_018 applies Selective Gradient Stopping (SGS) by detaching all non-KL gradients from $e_{\\dt}$, blocking the observation decoder pathway identified in F2 as the primary CIVO conduit. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions. Trained $\\dt$-embedding alone produces $-73\\%$ peak and $-86\\%$ final eval degradation relative to the baseline. Full-SGS seed~1 avoids collapse (eval \\sgseval{}, $-51\\%$ final relative to baseline) while seed~2 collapses (eval 40.8, $-96\\%$), yielding a 50\\% prevention rate. SGS reduces but does not eliminate CIVO risk: the gradient pathway it blocks is necessary but not sufficient for reliable prevention. Reward-only SGS (016e) fails entirely (NVE $10.42\\times$). Cross-environment validation on Cheetah Run (010b) confirms CIVO generalization: evaluation peaks at 321.9 before declining to 51.7 at 105K ($-84\\%$, minimum 22.7 at 65K); peak NVE $14.59\\times$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk (DMC) across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3, no temporal embedding. \\textbf{Trained dt-emb} (008d)\\footnotemark: DreamerV3 with a learned $d{=}32$ temporal embedding exposed to multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with Selective Gradient Stopping that detaches all non-KL gradients from $e_{\\dt}$, two seeds. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$ relative to the baseline. Full-SGS seed~1 partially recovers ($-51\\%$ final, no collapse) but seed~2 collapses ($-96\\%$ final, marked ``collapsed''), indicating that SGS reduces but does not reliably prevent CIVO (prevention rate $= 50\\%$). All percentages relative to Baseline 001.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n\n%% ============================================================\n%% TABLE 2: RSSM Fidelity\n%% ============================================================\n",
      "numLines": 18,
      "startLine": 115,
      "totalLines": 238
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

All edits applied correctly. Let me also check the Table 1 entry for 010b (line 44) to ensure it's consistent with the new text:

Line 44 shows "51.7 @105K" which matches the fix. 

Here's the summary of all modifications:

### Fix 1: Cheetah eval description (line 119)
- **Old:** `collapsing to 22.7 ($-93\%$)`
- **New:** `declining to 51.7 at 105K ($-84\%$, minimum 22.7 at 65K)`

### Fix 2: "8.6% of baseline" → 9.0% (line 90)
- **Old:** `8.6\% of baseline`
- **New:** `9.0\% of baseline`
- **Calc:** 82.8 / 915.7 = 0.0904 → 9.0%

### Fix 3: "1.61×" → "1.60×" (line 54)
- **Old:** `1.61$\times$ at 35K`
- **New:** `1.60$\times$ at 35K`

### Fix 4: Unified baseline to 915.7 (line 90)
All percentages recalculated with denominator 915.7 instead of 970.41:
| Value | Old (÷970.41) | New (÷915.7) |
|-------|--------------|--------------|
| mean 206.2 | 21.3% | 22.5% |
| 82.8 (008d) | 8.6% | 9.0% |
| 267.9 (009b) | 27.6% | 29.3% |

Also removed explicit "970.41" reference; now just says "of baseline" (baseline=915.7 is established in F1).

### Fix 5: Figure 2 caption (line 124)
- **Old:** `(008d, 009b)` with "two seeds"
- **New:** `(008d)\footnotemark` with single-seed description

### Fix 6: 008d data extension footnote (line 127)
- **Added:** `\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "uuid": "c6a86f57-0010-4d8e-8d5c-3cbab5bd79b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SwuSMoaM3pLXUNBtrcyWDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2127,
      "cache_read_input_tokens": 36445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2127
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

_source line 36_

All edits applied correctly. Let me also check the Table 1 entry for 010b (line 44) to ensure it's consistent with the new text:

Line 44 shows "51.7 @105K" which matches the fix. 

Here's the summary of all modifications:

### Fix 1: Cheetah eval description (line 119)
- **Old:** `collapsing to 22.7 ($-93\%$)`
- **New:** `declining to 51.7 at 105K ($-84\%$, minimum 22.7 at 65K)`

### Fix 2: "8.6% of baseline" → 9.0% (line 90)
- **Old:** `8.6\% of baseline`
- **New:** `9.0\% of baseline`
- **Calc:** 82.8 / 915.7 = 0.0904 → 9.0%

### Fix 3: "1.61×" → "1.60×" (line 54)
- **Old:** `1.61$\times$ at 35K`
- **New:** `1.60$\times$ at 35K`

### Fix 4: Unified baseline to 915.7 (line 90)
All percentages recalculated with denominator 915.7 instead of 970.41:
| Value | Old (÷970.41) | New (÷915.7) |
|-------|--------------|--------------|
| mean 206.2 | 21.3% | 22.5% |
| 82.8 (008d) | 8.6% | 9.0% |
| 267.9 (009b) | 27.6% | 29.3% |

Also removed explicit "970.41" reference; now just says "of baseline" (baseline=915.7 is established in F1).

### Fix 5: Figure 2 caption (line 124)
- **Old:** `(008d, 009b)` with "two seeds"
- **New:** `(008d)\footnotemark` with single-seed description

### Fix 6: 008d data extension footnote (line 127)
- **Added:** `\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 87961,
  "duration_api_ms": 88976,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "1c6c4358-7087-49f8-8f14-5d5f5bae9fb3",
  "total_cost_usd": 0.42951025,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 27125,
    "cache_read_input_tokens": 315952,
    "output_tokens": 3984,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 27125,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 571,
        "cache_read_input_tokens": 36445,
        "cache_creation_input_tokens": 2127,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2127
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2248,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002343,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 3984,
      "cacheReadInputTokens": 315952,
      "cacheCreationInputTokens": 27125,
      "webSearchRequests": 0,
      "costUSD": 0.42716725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0b856cde-8a7d-4c76-980e-7837d756613a"
}
```

</details>

---
