# paper claim language audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_paper_claim-language-audit_20260516T162609.log`
- **Structured JSON:** [`c2904e6b118d2692788f.json`](../../sessions/c2/c2904e6b118d2692788f.json)

## Before a recorded user message

37 recorded events

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
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "d3694555-3b54-4e36-9fa2-3d01b7ac89c9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1778961000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5dbd4080-0013-4130-b655-e9b35b2d6c61",
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper files to audit their claim language.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "892d2c84-c4e7-4de2-b393-e3f616a16487",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9TweX4QJwG3YahSoeWEgm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11639,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11639
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

_source line 5_

读取论文文件进行 claim 语言审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "a3709f03-cdec-46a0-a2ae-98ecb93454f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9TweX4QJwG3YahSoeWEgm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11639,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11639
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01WMfNCqg5n5pkZAd4gWo5ma`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "dc3fb1fa-6f89-4a9c-9028-996ff313048d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9TweX4QJwG3YahSoeWEgm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11639,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11639
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

_source line 7 · 2026-05-16T16:26:21.003Z_

<details><summary>↩ Tool result · `toolu_01WMfNCqg5n5pkZAd4gWo5ma`</summary>

```text
1	% Results Section — Draft v1
2	% Target: CoRL 2026
3	% Status: Draft, pending Director review
4	% Writing order: 1 (anchors all other sections)
5	
6	\section{Results}
7	\label{sec:results}
8	
9	We organize findings around five diagnostic questions, followed by a gradient decomposition analysis and a taxonomy of failure modes. All quantitative claims cite experiment identifiers for traceability; evaluation returns are means over 10 episodes at each checkpoint. Experiments use Walker Walk from the DeepMind Control Suite (see Section~\ref{sec:environment}).
10	
11	% ============================================================
12	% F1: ALL DT>1 DEGRADE
13	% ============================================================
14	
15	\subsection{Finding 1: All Variable-Rate Configurations Degrade Performance}
16	\label{sec:f1}
17	
18	\begin{figure}[t]
19	  \centering
20	  % PLACEHOLDER: Learning curves for exp_001, 005, 006, 007
21	  \includegraphics[width=\linewidth]{figures/fig1_learning_curves.pdf}
22	  \caption{Learning curves for all primary configurations. The \mbox{$\Delta t{=}1$} baseline (exp\_001) converges to ${\sim}950$; every $\Delta t{>}1$ variant degrades or collapses.}
23	  \label{fig:learning_curves}
24	\end{figure}
25	
26	Every tested variable-rate imagination configuration degrades asymptotic performance relative to the standard $\Delta t{=}1$ baseline. The baseline (exp\_001, seed~1) reaches 915.7 at 105K steps and converges to ${\sim}950$ asymptotically (peak 970.4 at 505K). In contrast:
27	
28	\begin{itemize}
29	    \item \textbf{Learned gate} (exp\_005): peaks at 541.2 at 55K, then declines to 98.8 by 145K---a 90\% drop from peak.
30	    \item \textbf{Fixed $\Delta t{=}2$} (exp\_006, $H{=}15$): peaks at 485.3 at 35K, then collapses to 132.9 by 65K as the value/eval ratio accelerates from 31\% to 272\%.
31	    \item \textbf{Fixed $\Delta t{=}4$} (exp\_007, $H{=}15$): peaks at 176.9 at 25K and plateaus around 144--152, never exceeding 19\% of the baseline's asymptotic level.
32	\end{itemize}
33	
34	No $\Delta t{>}1$ configuration achieves sustained performance above 60\% of the baseline beyond 65K steps. The degradation patterns vary---inverted-V collapse (exp\_006), monotonic decline (exp\_005), and severe suppression (exp\_007)---but the qualitative conclusion is uniform: variable-rate imagination degrades performance on Walker Walk across all tested configurations.
35	
36	
37	% ============================================================
38	% F2: TRAINED DT_EMB → CIVO
39	% ============================================================
40	
41	\subsection{Finding 2: Trained Temporal Embedding Reliably Triggers Pathological Value Overestimation}
42	\label{sec:f2}
43	
44	\begin{figure}[t]
45	  \centering
46	  % PLACEHOLDER: NVE trajectories with 1.5x threshold
47	  \includegraphics[width=\linewidth]{figures/fig2_nve_trajectories.pdf}
48	  \caption{Normalized value/eval ratio (NVE) trajectories. Dashed line: $1.5\times$ pathological threshold (applied at $k \geq 35\text{K}$). Both trained-$e_{\Delta t}$ seeds exceed the threshold; neither removed-$e_{\Delta t}$ seed does.}
49	  \label{fig:nve_trajectories}
50	\end{figure}
51	
52	The controlled comparison between exp\_008d (trained $e_{\Delta t}$, subsample \textsc{on}, $H{=}8$) and exp\_008f ($e_{\Delta t}$ removed, subsample \textsc{on}, $H{=}8$) isolates the temporal embedding as the causal factor for conditioning-induced value overestimation (CIVO). These experiments share identical configurations except for the presence of the trained temporal embedding.
53	
54	\paragraph{Diagnostic threshold.} Using the normalized value/eval ratio (NVE; see Section~\ref{sec:diagnostic}), the $\hat{r}_k > 1.5$ threshold at steps $\geq$35K achieves 4/4 classification accuracy across seeds:
55	
56	\begin{table}[h]
57	\centering
58	\small
59	\caption{NVE diagnostic: trained vs.\ removed temporal embedding. Peak NVE reported at steps $\geq$35K where baseline $r_k > 0.24$ ensures ratio stability.}
60	\label{tab:nve_separation}
61	\begin{tabular}{llcc}
62	\toprule
63	Condition & Seed & Peak NVE ($\geq$35K) & $>$1.5$\times$? \\
64	\midrule
65	Trained $e_{\Delta t}$ (exp\_008d) & 1 & 2.09$\times$ @ 45K & \textbf{Yes} \\
66	Trained $e_{\Delta t}$ (exp\_009b) & 2 & 1.62$\times$ @ 45K & \textbf{Yes} \\
67	Removed $e_{\Delta t}$ (exp\_008f) & 1 & 0.97$\times$ @ 55K & No \\
68	Removed $e_{\Delta t}$ (exp\_009c) & 2 & 1.14$\times$ @ 105K & No \\
69	\bottomrule
70	\end{tabular}
71	\end{table}
72	
73	Both trained-$e_{\Delta t}$ seeds exceed the pathological threshold; neither removed-$e_{\Delta t}$ seed does. The trained embedding reliably induces pathological value overestimation, though whether this overestimation progresses to catastrophic collapse is stochastic (see below).
74	
75	\paragraph{Causal isolation.} The factorial structure establishes that CIVO requires the combination of a \textit{trained} temporal embedding and exposure to multi-rate training data:
76	
77	\begin{figure}[h]
78	  \centering
79	  % PLACEHOLDER: 2×2 factorial grid summary
80	  \includegraphics[width=0.85\linewidth]{figures/fig3_factorial_grid.pdf}
81	  \caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\Delta t}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}
82	  \label{fig:factorial_grid}
83	\end{figure}
84	
85	\begin{table}[h]
86	\centering
87	\small
88	\caption{Causal isolation: $e_{\Delta t}$ configuration $\times$ multi-rate data exposure. All treatment conditions use $\Delta t{=}2$ imagination and $H{=}8$ (except exp\_008a: $H{=}15$).}
89	\label{tab:causal_matrix}
90	\begin{tabular}{lcc}
91	\toprule
92	& Multi-rate data (\textsc{on}) & Single-rate data (\textsc{off}) \\
93	\midrule
94	Trained $e_{\Delta t}$ & exp\_008d: CIVO & exp\_008a: healthy \\
95	 & NVE 2.09$\times$, collapse & NVE 0.59--0.93$\times$ \\
96	\midrule
97	Frozen $e_{\Delta t}$ & exp\_015b: grad.\ starvation & --- \\
98	 & NVE 0.39--0.47$\times$ & \\
99	\midrule
100	Removed $e_{\Delta t}$ & exp\_008f: no CIVO & --- \\
101	 & NVE $\leq$0.97$\times$ & \\
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	Exp\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\Delta t{>}1$ transitions during world-model training (subsample \textsc{off}). Despite sharing the same embedding architecture as exp\_008d, its NVE remains in the 0.59--0.93$\times$ range across 105K steps (exp\_008a). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\Delta t{>}1$ state predictions within the RSSM.
107	
108	\paragraph{Post-CIVO outcomes: seed-dependent trajectories.} The 008d configuration was run with two independent seeds, producing qualitatively distinct outcomes:
109	
110	\begin{enumerate}
111	    \item \textbf{Seed~1} (exp\_008d / exp\_009e): CIVO onset at 25K (NVE 1.78$\times$), eval declines from 167.2 to 82.8 by 55K (exp\_008d). Extended to 105K (exp\_009e), the run shows oscillatory degradation: a transient bounce to 250 at 65K, but actor loss flips positive ($+$0.011 at 85K, exp\_009e), signaling permanent actor damage. Eval oscillates between 131 and 250 without sustained recovery, ending at 131.1 at 105K (exp\_009e).
112	    \item \textbf{Seed~2} (exp\_009b): transient NVE of 1.62$\times$ at 45K, followed by self-correction---NVE declines monotonically from 1.62$\times$ to 0.38$\times$ between 45K and 105K. Value peaks at 110.9 at 65K then self-corrects to 67.3 by 105K, while eval rises from 141.0 to a peak of 278.5 at 95K (exp\_009b).
113	\end{enumerate}
114	
115	Both seeds cross the NVE~$>$~1.5$\times$ threshold, confirming the trained embedding as a reliable trigger. The downstream trajectory depends on whether overestimation is sustained across consecutive checkpoints (seed~1: $1.71\times \to 2.09\times \to 4.12\times$ at 35--55K, locking in the positive feedback loop) or transient (seed~2: $1.62\times$ at 45K $\to$ $1.41\times$ at 55K, declining).
116	
117	
118	% ============================================================
119	% F3: UNTRAINED DT_EMB → PROTECTION
120	% ============================================================
121	
122	\subsection{Finding 3: Unexposed Temporal Embedding Suppresses Value Drift}
123	\label{sec:f3}
124	
125	Exp\_008a (trained-but-unexposed $e_{\Delta t}$,\footnote{Exp\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\Delta t{>}1$ data due to subsample \textsc{off}; it is not frozen or absent. See Table~\ref{tab:factorial}.} subsample \textsc{off}, $H{=}15$) demonstrates sustained value growth suppression over 105K steps. Its NVE ranges from 0.59$\times$ to 0.93$\times$ across the 55K--105K window (exp\_008a), diverging further \textit{below} baseline levels over time rather than converging toward them.
126	
127	Performance follows two complete V-shaped recovery cycles: $500.8 \to 563.4 \to 487.9 \to 608.0 \to 469.9 \to 583.7 \to 572.2 \to 777.7$ over 35K--105K (exp\_008a). The final evaluation of 777.7 at 105K reaches 85\% of the baseline at the same step (915.7, exp\_001), with no collapse through 112K training steps.
128	
129	This contrasts sharply with exp\_006 (trained $e_{\Delta t}$, subsample \textsc{on}, $H{=}15$), where NVE accelerates from 1.61$\times$ at 45K to 2.31$\times$ at 55K before catastrophic collapse to 132.9 at 65K (exp\_006). The 006-vs-008a comparison corroborates the causal role of multi-rate data exposure: both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\Delta t{>}1$ transitions during training.
130	
131	
132	% ============================================================
133	% F4: DT AMPLIFICATION
134	% ============================================================
135	
136	\subsection{Finding 4: Longer Temporal Gaps Amplify Degradation}
137	\label{sec:f4}
138	
139	Increasing the imagination step size from $\Delta t{=}2$ to $\Delta t{=}4$ worsens degradation monotonically. Peak evaluation returns are ${\sim}950$ ($\Delta t{=}1$, exp\_001), 485.3 ($\Delta t{=}2$, exp\_006), and 176.9 ($\Delta t{=}4$, exp\_007).
140	
141	\begin{figure}[h]
142	  \centering
143	  % PLACEHOLDER: dt=1 vs dt=2 vs dt=4 comparison
144	  \includegraphics[width=0.7\linewidth]{figures/fig5_dt_amplification.pdf}
145	  \caption{Performance vs.\ imagination step size: monotonic degradation.}
146	  \label{fig:dt_amplification}
147	\end{figure}
148	
149	At $\Delta t{=}4$ (exp\_007), the value/eval ratio at 45K is 0.126 (exp\_007)---severely suppressed rather than inflated---indicating a qualitatively different failure: the RSSM prediction quality at $\Delta t{=}4$ is too poor even for overestimation to develop, consistent with compounding prediction error over longer temporal gaps. Only two $\Delta t$ values were tested; a finer grid would be needed to characterize the degradation curve.
150	
151	
152	% ============================================================
153	% F5: HORIZON/SUBSAMPLE SECONDARY
154	% ============================================================
155	
156	\subsection{Finding 5: Horizon and Subsampling Are Secondary Factors}
157	\label{sec:f5}
158	
159	Subsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO.
160	
161	\paragraph{Subsampling is not sufficient for collapse.} Exp\_008e\_v3 (trained $e_{\Delta t}$, subsample \textsc{on}, $\Delta t{=}1$ imagination, $H{=}15$) achieves 869.9 at 105K---95\% of baseline---with seed~1 (exp\_008e\_v3\_s1).\footnote{An independent run with seed~0 (exp\_008e\_v3) reproduces this trajectory.} This demonstrates that multi-rate training data alone does not degrade performance when imagination is restricted to $\Delta t{=}1$. Seed~2, however, collapses from 715.2 at 85K to 137.0 at 105K (exp\_008e\_v3\_s2), through a non-CIVO mechanism discussed in Section~\ref{sec:failure_taxonomy}.
162	
163	\paragraph{Horizon affects performance level but not the overestimation pattern.} Exp\_008c ($H{=}8$, unexposed $e_{\Delta t}$, subsample \textsc{off}) plateaus at 241.9 at 55K (exp\_008c), while exp\_008a ($H{=}15$, same configuration otherwise) reaches 777.7 at 105K (exp\_008a). Both maintain healthy NVE ($\leq$0.93$\times$), confirming that horizon length modulates the performance ceiling but does not trigger CIVO.
164	
165	
166	% ============================================================
167	% GRADIENT DECOMPOSITION
168	% ============================================================
169	
170	\subsection{Gradient Decomposition: Observation Decoders Dominate Temporal Embedding Learning}
171	\label{sec:gradient_decomposition_results}
172	
173	To identify which gradient pathway through $e_{\Delta t}$ drives CIVO, we performed a post-hoc gradient decomposition (D061) measuring each loss component's contribution to the temporal embedding parameters via \texttt{torch.autograd.grad}. The analysis was motivated by a targeted stop-gradient experiment (exp\_016e) in which $e_{\Delta t}$ was detached from the reward head during the backward pass---see Section~\ref{sec:sgs_gradient_analysis} for full experimental details.
174	
175	\begin{table}[h]
176	\centering
177	\small
178	\caption{Gradient contributions to $e_{\Delta t}$ parameters by loss component ($\ell_2$ norms of $\nabla_\theta \mathcal{L}_i$), measured at training step 95K (D061 analysis). Total gradient norm: 1.624.}
179	\label{tab:gradient_decomposition_results}
180	\begin{tabular}{lrr}
181	\toprule
182	Loss component & $\|\nabla_\theta \mathcal{L}_i\|_2$ & Share (\%) \\
183	\midrule
184	Observation decoders (orientations, velocity, height) & 1.505 & 92.7 \\
185	KL dynamics & 0.119 & 7.3 \\
186	Continuation head & $<$0.001 & $<$0.1 \\
187	Reward head & 0.000 & 0.0 \\
188	\bottomrule
189	\end{tabular}
190	\end{table}
191	
192	The reward head's contribution is numerically negligible---zero to within floating-point precision. This explains why exp\_016e (reward-only stop-gradient; identical to exp\_008d except \texttt{reward\_dt\_emb\_detach=True}) exhibits the same collapse pattern: peak 326.7 at 75K followed by catastrophic decline to 31.7 at 95K with NVE reaching $10.42\times$ (exp\_016e). The intervention detaches a gradient that does not exist---an architectural no-op. The timing differences between exp\_016e and exp\_008d (collapse onset ${\sim}$75K vs.\ ${\sim}$25K, peak 326.7 vs.\ 167.2) are consistent with cross-seed variation across the 008d configuration's trajectories (cf.\ exp\_009b, peak 278.5 at 95K).
193	
194	The 93\%/7\%/0\% split reveals that $e_{\Delta t}$ learns to encode temporal information that minimizes \textit{observation reconstruction error}, not reward prediction error. CIVO originates in the observation reconstruction objective's influence on latent dynamics---a structural property of DreamerV3's multi-head decoder architecture \citep{hafner2023dreamerv3}. This constrains the space of viable interventions: strategies targeting the reward pathway alone address $<$1\% of the gradient flow and cannot attenuate CIVO. The full-pathway SGS intervention (exp\_018; Section~\ref{sec:pending}) removes the dominant 93\% observation decoder contribution, constituting a genuine gradient-level intervention.
195	
196	This gradient asymmetry is consistent with prior observations on the dominance of reconstruction losses in world-model training \citep{hafner2023dreamerv3, ma2024harmonydream}, but the D061 analysis provides the first \textit{backward-pass decomposition} quantifying the per-component gradient contributions to a conditioning variable. HarmonyDream \citep{ma2024harmonydream} reports a two-order-of-magnitude gap between observation and reward loss magnitudes; our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.
197	
198	
199	% ============================================================
200	% THREE FAILURE MODES
201	% ============================================================
202	
203	\subsection{Three Distinct Failure Modes}
204	\label{sec:failure_taxonomy}
205	
206	\begin{figure}[t]
207	  \centering
208	  % PLACEHOLDER: Contrasting collapse dynamics across three mechanisms
209	  \includegraphics[width=\linewidth]{figures/fig6_failure_modes.pdf}
210	  \caption{Three failure modes triggered by temporal embedding configurations. Left: CIVO (exp\_008d)---value explosion drives eval decline, entropy decreases. Center: Gradient starvation (exp\_015b)---actor loss approaches zero, performance oscillates without convergence. Right: IRD (exp\_008e\_v3\_s2)---eval collapse precedes value rise, entropy increases.}
211	  \label{fig:failure_modes}
212	\end{figure}
213	
214	The experiments reveal three mechanistically distinct failure modes. Distinguishing these modes is necessary for designing targeted interventions, as surface-level metrics (e.g., low final eval return) are shared across all three but the underlying dynamics differ qualitatively.
215	
216	\begin{table}[h]
217	\centering
218	\small
219	\caption{Taxonomy of failure modes identified across temporal embedding configurations.}
220	\label{tab:failure_taxonomy}
221	\begin{tabular}{lccc}
222	\toprule
223	Feature & CIVO & Grad.\ Starvation & IRD \\
224	\midrule
225	Representative exp & 008d (seed 1) & 015b & 008e\_v3\_s2 \\
226	$e_{\Delta t}$ config & trained & frozen & trained \\
227	NVE trajectory & sustained $>$1.5$\times$ & $<$0.5$\times$ & passive rise \\
228	Value dynamics & explosion ($+$130\%) & suppressed & stable \\
229	Eval dynamics & decline & volatile (80--238) & collapse ($-$81\%) \\
230	Actor entropy & $\downarrow$ (locks in) & --- & $\uparrow$ (de-specializes) \\
231	\bottomrule
232	\end{tabular}
233	\end{table}
234	
235	\paragraph{Conditioning-Induced Value Overestimation (CIVO).} In exp\_008d and exp\_006, the trained temporal embedding enables the reward head to produce systematically biased $\Delta t{>}1$ predictions. RSSM fidelity analysis reveals a $2.78\times$ reward gap between $\Delta t{=}1$ and $\Delta t{=}2$ transitions in exp\_008d (see Table~\ref{tab:rssm_fidelity} in Section~\ref{sec:rssm_analysis}). The critic inherits these biases through the $\lambda$-return computation, overestimates values for $\Delta t{>}1$ trajectories, and the actor exploits the overestimated landscape. This positive feedback loop produces accelerating NVE ($1.71\times \to 2.09\times \to 4.12\times$ at 35--55K in exp\_008d) with decreasing actor entropy---the policy becomes increasingly deterministic as it converges on the overestimated region.
236	
237	\paragraph{Gradient Starvation.} A frozen temporal embedding (exp\_015b, $d{=}32$, \texttt{requires\_grad=False}) cannot co-adapt as RSSM representations drift during training. Actor loss approaches zero (0.0002 at 105K, exp\_015b), indicating gradient starvation: the actor receives insufficient learning signal. NVE remains at 0.39--0.47$\times$ (exp\_015b)---the critic \textit{under-estimates}, the opposite of CIVO. Evaluation oscillates between 80 and 238 without convergence. The NVE briefly reaches 1.45$\times$ at 55K but self-corrects to 0.65$\times$ by 65K---a transient, sub-threshold overestimation qualitatively different from CIVO's sustained acceleration.
238	
239	\paragraph{Imagination-Reality Divergence (IRD).} Exp\_008e\_v3\_s2 collapses despite using $\Delta t{=}1$-only imagination (\texttt{gate\_dt\_mean}$\,{=}\,$1.0 throughout, exp\_008e\_v3\_s2). Evaluation drops from 715.2 at 85K to 137.0 at 105K, while value estimates remain relatively stable (339.3 $\to$ 339.8), producing a passive NVE rise to $3.78\times$ (exp\_008e\_v3\_s2). Crucially, actor entropy \textit{increases} from $-5.21$ to $-3.83$ during collapse (policy de-specialization), the opposite of CIVO's entropy decrease. The baseline seed~2 (exp\_009a) is stable through the same window (618.7 $\to$ 836.5 at 85K--105K, exp\_009a), ruling out seed-specific fragility.
240	
241	This failure mode does not involve value overestimation driving actor exploitation. Rather, the trained embedding's interaction with multi-rate training data appears to create a latent representation vulnerability that manifests as policy instability independent of imagination $\Delta t$. The NVE rise is a \textit{consequence} of eval collapse, not a cause---distinguishing IRD from CIVO where the NVE rise precedes and drives the eval decline.
242	
243	The existence of IRD alongside CIVO suggests that the trained temporal embedding creates vulnerability through multiple pathways. Eliminating CIVO (e.g., via $\Delta t{=}1$ imagination) does not eliminate all failure modes.
244	
245	
246	% ============================================================
247	% PENDING EXPERIMENTS (PLACEHOLDERS)
248	% ============================================================
249	
250	\subsection{Pending Experiments}
251	\label{sec:pending}
252	
253	Two experiment series are queued to extend the diagnostic analysis:
254	
255	\paragraph{Full-pathway SGS (exp\_018).} Detaches all non-KL gradients from the temporal embedding, removing the dominant 93\% observation decoder contribution while retaining only the 7\% KL dynamics signal. If CIVO persists with only KL gradients, the vulnerability is representation-level (KL training alone sufficient); if eliminated, the observation decoder gradient pathway is the root cause. Results will be reported upon completion.
256	
257	\paragraph{Cross-environment validation (exp\_019 series).} PickCube-v1 (ManiSkill3) baseline (exp\_019a) and CIVO trigger condition (exp\_019b) to test whether the identified mechanisms transfer beyond locomotion to manipulation tasks with qualitatively different observation and reward structure.
258	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "9b34f8a4-41f7-4d24-9036-9d765615fbd8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results.md",
      "content": "% Results Section — Draft v1\n% Target: CoRL 2026\n% Status: Draft, pending Director review\n% Writing order: 1 (anchors all other sections)\n\n\\section{Results}\n\\label{sec:results}\n\nWe organize findings around five diagnostic questions, followed by a gradient decomposition analysis and a taxonomy of failure modes. All quantitative claims cite experiment identifiers for traceability; evaluation returns are means over 10 episodes at each checkpoint. Experiments use Walker Walk from the DeepMind Control Suite (see Section~\\ref{sec:environment}).\n\n% ============================================================\n% F1: ALL DT>1 DEGRADE\n% ============================================================\n\n\\subsection{Finding 1: All Variable-Rate Configurations Degrade Performance}\n\\label{sec:f1}\n\n\\begin{figure}[t]\n  \\centering\n  % PLACEHOLDER: Learning curves for exp_001, 005, 006, 007\n  \\includegraphics[width=\\linewidth]{figures/fig1_learning_curves.pdf}\n  \\caption{Learning curves for all primary configurations. The \\mbox{$\\Delta t{=}1$} baseline (exp\\_001) converges to ${\\sim}950$; every $\\Delta t{>}1$ variant degrades or collapses.}\n  \\label{fig:learning_curves}\n\\end{figure}\n\nEvery tested variable-rate imagination configuration degrades asymptotic performance relative to the standard $\\Delta t{=}1$ baseline. The baseline (exp\\_001, seed~1) reaches 915.7 at 105K steps and converges to ${\\sim}950$ asymptotically (peak 970.4 at 505K). In contrast:\n\n\\begin{itemize}\n    \\item \\textbf{Learned gate} (exp\\_005): peaks at 541.2 at 55K, then declines to 98.8 by 145K---a 90\\% drop from peak.\n    \\item \\textbf{Fixed $\\Delta t{=}2$} (exp\\_006, $H{=}15$): peaks at 485.3 at 35K, then collapses to 132.9 by 65K as the value/eval ratio accelerates from 31\\% to 272\\%.\n    \\item \\textbf{Fixed $\\Delta t{=}4$} (exp\\_007, $H{=}15$): peaks at 176.9 at 25K and plateaus around 144--152, never exceeding 19\\% of the baseline's asymptotic level.\n\\end{itemize}\n\nNo $\\Delta t{>}1$ configuration achieves sustained performance above 60\\% of the baseline beyond 65K steps. The degradation patterns vary---inverted-V collapse (exp\\_006), monotonic decline (exp\\_005), and severe suppression (exp\\_007)---but the qualitative conclusion is uniform: variable-rate imagination degrades performance on Walker Walk across all tested configurations.\n\n\n% ============================================================\n% F2: TRAINED DT_EMB → CIVO\n% ============================================================\n\n\\subsection{Finding 2: Trained Temporal Embedding Reliably Triggers Pathological Value Overestimation}\n\\label{sec:f2}\n\n\\begin{figure}[t]\n  \\centering\n  % PLACEHOLDER: NVE trajectories with 1.5x threshold\n  \\includegraphics[width=\\linewidth]{figures/fig2_nve_trajectories.pdf}\n  \\caption{Normalized value/eval ratio (NVE) trajectories. Dashed line: $1.5\\times$ pathological threshold (applied at $k \\geq 35\\text{K}$). Both trained-$e_{\\Delta t}$ seeds exceed the threshold; neither removed-$e_{\\Delta t}$ seed does.}\n  \\label{fig:nve_trajectories}\n\\end{figure}\n\nThe controlled comparison between exp\\_008d (trained $e_{\\Delta t}$, subsample \\textsc{on}, $H{=}8$) and exp\\_008f ($e_{\\Delta t}$ removed, subsample \\textsc{on}, $H{=}8$) isolates the temporal embedding as the causal factor for conditioning-induced value overestimation (CIVO). These experiments share identical configurations except for the presence of the trained temporal embedding.\n\n\\paragraph{Diagnostic threshold.} Using the normalized value/eval ratio (NVE; see Section~\\ref{sec:diagnostic}), the $\\hat{r}_k > 1.5$ threshold at steps $\\geq$35K achieves 4/4 classification accuracy across seeds:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NVE diagnostic: trained vs.\\ removed temporal embedding. Peak NVE reported at steps $\\geq$35K where baseline $r_k > 0.24$ ensures ratio stability.}\n\\label{tab:nve_separation}\n\\begin{tabular}{llcc}\n\\toprule\nCondition & Seed & Peak NVE ($\\geq$35K) & $>$1.5$\\times$? \\\\\n\\midrule\nTrained $e_{\\Delta t}$ (exp\\_008d) & 1 & 2.09$\\times$ @ 45K & \\textbf{Yes} \\\\\nTrained $e_{\\Delta t}$ (exp\\_009b) & 2 & 1.62$\\times$ @ 45K & \\textbf{Yes} \\\\\nRemoved $e_{\\Delta t}$ (exp\\_008f) & 1 & 0.97$\\times$ @ 55K & No \\\\\nRemoved $e_{\\Delta t}$ (exp\\_009c) & 2 & 1.14$\\times$ @ 105K & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth trained-$e_{\\Delta t}$ seeds exceed the pathological threshold; neither removed-$e_{\\Delta t}$ seed does. The trained embedding reliably induces pathological value overestimation, though whether this overestimation progresses to catastrophic collapse is stochastic (see below).\n\n\\paragraph{Causal isolation.} The factorial structure establishes that CIVO requires the combination of a \\textit{trained} temporal embedding and exposure to multi-rate training data:\n\n\\begin{figure}[h]\n  \\centering\n  % PLACEHOLDER: 2×2 factorial grid summary\n  \\includegraphics[width=0.85\\linewidth]{figures/fig3_factorial_grid.pdf}\n  \\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\Delta t}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n  \\label{fig:factorial_grid}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\Delta t}$ configuration $\\times$ multi-rate data exposure. All treatment conditions use $\\Delta t{=}2$ imagination and $H{=}8$ (except exp\\_008a: $H{=}15$).}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\Delta t}$ & exp\\_008d: CIVO & exp\\_008a: healthy \\\\\n & NVE 2.09$\\times$, collapse & NVE 0.59--0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\Delta t}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.39--0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\Delta t}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\Delta t{>}1$ transitions during world-model training (subsample \\textsc{off}). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the 0.59--0.93$\\times$ range across 105K steps (exp\\_008a). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\Delta t{>}1$ state predictions within the RSSM.\n\n\\paragraph{Post-CIVO outcomes: seed-dependent trajectories.} The 008d configuration was run with two independent seeds, producing qualitatively distinct outcomes:\n\n\\begin{enumerate}\n    \\item \\textbf{Seed~1} (exp\\_008d / exp\\_009e): CIVO onset at 25K (NVE 1.78$\\times$), eval declines from 167.2 to 82.8 by 55K (exp\\_008d). Extended to 105K (exp\\_009e), the run shows oscillatory degradation: a transient bounce to 250 at 65K, but actor loss flips positive ($+$0.011 at 85K, exp\\_009e), signaling permanent actor damage. Eval oscillates between 131 and 250 without sustained recovery, ending at 131.1 at 105K (exp\\_009e).\n    \\item \\textbf{Seed~2} (exp\\_009b): transient NVE of 1.62$\\times$ at 45K, followed by self-correction---NVE declines monotonically from 1.62$\\times$ to 0.38$\\times$ between 45K and 105K. Value peaks at 110.9 at 65K then self-corrects to 67.3 by 105K, while eval rises from 141.0 to a peak of 278.5 at 95K (exp\\_009b).\n\\end{enumerate}\n\nBoth seeds cross the NVE~$>$~1.5$\\times$ threshold, confirming the trained embedding as a reliable trigger. The downstream trajectory depends on whether overestimation is sustained across consecutive checkpoints (seed~1: $1.71\\times \\to 2.09\\times \\to 4.12\\times$ at 35--55K, locking in the positive feedback loop) or transient (seed~2: $1.62\\times$ at 45K $\\to$ $1.41\\times$ at 55K, declining).\n\n\n% ============================================================\n% F3: UNTRAINED DT_EMB → PROTECTION\n% ============================================================\n\n\\subsection{Finding 3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\nExp\\_008a (trained-but-unexposed $e_{\\Delta t}$,\\footnote{Exp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\Delta t{>}1$ data due to subsample \\textsc{off}; it is not frozen or absent. See Table~\\ref{tab:factorial}.} subsample \\textsc{off}, $H{=}15$) demonstrates sustained value growth suppression over 105K steps. Its NVE ranges from 0.59$\\times$ to 0.93$\\times$ across the 55K--105K window (exp\\_008a), diverging further \\textit{below} baseline levels over time rather than converging toward them.\n\nPerformance follows two complete V-shaped recovery cycles: $500.8 \\to 563.4 \\to 487.9 \\to 608.0 \\to 469.9 \\to 583.7 \\to 572.2 \\to 777.7$ over 35K--105K (exp\\_008a). The final evaluation of 777.7 at 105K reaches 85\\% of the baseline at the same step (915.7, exp\\_001), with no collapse through 112K training steps.\n\nThis contrasts sharply with exp\\_006 (trained $e_{\\Delta t}$, subsample \\textsc{on}, $H{=}15$), where NVE accelerates from 1.61$\\times$ at 45K to 2.31$\\times$ at 55K before catastrophic collapse to 132.9 at 65K (exp\\_006). The 006-vs-008a comparison corroborates the causal role of multi-rate data exposure: both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\Delta t{>}1$ transitions during training.\n\n\n% ============================================================\n% F4: DT AMPLIFICATION\n% ============================================================\n\n\\subsection{Finding 4: Longer Temporal Gaps Amplify Degradation}\n\\label{sec:f4}\n\nIncreasing the imagination step size from $\\Delta t{=}2$ to $\\Delta t{=}4$ worsens degradation monotonically. Peak evaluation returns are ${\\sim}950$ ($\\Delta t{=}1$, exp\\_001), 485.3 ($\\Delta t{=}2$, exp\\_006), and 176.9 ($\\Delta t{=}4$, exp\\_007).\n\n\\begin{figure}[h]\n  \\centering\n  % PLACEHOLDER: dt=1 vs dt=2 vs dt=4 comparison\n  \\includegraphics[width=0.7\\linewidth]{figures/fig5_dt_amplification.pdf}\n  \\caption{Performance vs.\\ imagination step size: monotonic degradation.}\n  \\label{fig:dt_amplification}\n\\end{figure}\n\nAt $\\Delta t{=}4$ (exp\\_007), the value/eval ratio at 45K is 0.126 (exp\\_007)---severely suppressed rather than inflated---indicating a qualitatively different failure: the RSSM prediction quality at $\\Delta t{=}4$ is too poor even for overestimation to develop, consistent with compounding prediction error over longer temporal gaps. Only two $\\Delta t$ values were tested; a finer grid would be needed to characterize the degradation curve.\n\n\n% ============================================================\n% F5: HORIZON/SUBSAMPLE SECONDARY\n% ============================================================\n\n\\subsection{Finding 5: Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nSubsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO.\n\n\\paragraph{Subsampling is not sufficient for collapse.} Exp\\_008e\\_v3 (trained $e_{\\Delta t}$, subsample \\textsc{on}, $\\Delta t{=}1$ imagination, $H{=}15$) achieves 869.9 at 105K---95\\% of baseline---with seed~1 (exp\\_008e\\_v3\\_s1).\\footnote{An independent run with seed~0 (exp\\_008e\\_v3) reproduces this trajectory.} This demonstrates that multi-rate training data alone does not degrade performance when imagination is restricted to $\\Delta t{=}1$. Seed~2, however, collapses from 715.2 at 85K to 137.0 at 105K (exp\\_008e\\_v3\\_s2), through a non-CIVO mechanism discussed in Section~\\ref{sec:failure_taxonomy}.\n\n\\paragraph{Horizon affects performance level but not the overestimation pattern.} Exp\\_008c ($H{=}8$, unexposed $e_{\\Delta t}$, subsample \\textsc{off}) plateaus at 241.9 at 55K (exp\\_008c), while exp\\_008a ($H{=}15$, same configuration otherwise) reaches 777.7 at 105K (exp\\_008a). Both maintain healthy NVE ($\\leq$0.93$\\times$), confirming that horizon length modulates the performance ceiling but does not trigger CIVO.\n\n\n% ============================================================\n% GRADIENT DECOMPOSITION\n% ============================================================\n\n\\subsection{Gradient Decomposition: Observation Decoders Dominate Temporal Embedding Learning}\n\\label{sec:gradient_decomposition_results}\n\nTo identify which gradient pathway through $e_{\\Delta t}$ drives CIVO, we performed a post-hoc gradient decomposition (D061) measuring each loss component's contribution to the temporal embedding parameters via \\texttt{torch.autograd.grad}. The analysis was motivated by a targeted stop-gradient experiment (exp\\_016e) in which $e_{\\Delta t}$ was detached from the reward head during the backward pass---see Section~\\ref{sec:sgs_gradient_analysis} for full experimental details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Gradient contributions to $e_{\\Delta t}$ parameters by loss component ($\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$), measured at training step 95K (D061 analysis). Total gradient norm: 1.624.}\n\\label{tab:gradient_decomposition_results}\n\\begin{tabular}{lrr}\n\\toprule\nLoss component & $\\|\\nabla_\\theta \\mathcal{L}_i\\|_2$ & Share (\\%) \\\\\n\\midrule\nObservation decoders (orientations, velocity, height) & 1.505 & 92.7 \\\\\nKL dynamics & 0.119 & 7.3 \\\\\nContinuation head & $<$0.001 & $<$0.1 \\\\\nReward head & 0.000 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reward head's contribution is numerically negligible---zero to within floating-point precision. This explains why exp\\_016e (reward-only stop-gradient; identical to exp\\_008d except \\texttt{reward\\_dt\\_emb\\_detach=True}) exhibits the same collapse pattern: peak 326.7 at 75K followed by catastrophic decline to 31.7 at 95K with NVE reaching $10.42\\times$ (exp\\_016e). The intervention detaches a gradient that does not exist---an architectural no-op. The timing differences between exp\\_016e and exp\\_008d (collapse onset ${\\sim}$75K vs.\\ ${\\sim}$25K, peak 326.7 vs.\\ 167.2) are consistent with cross-seed variation across the 008d configuration's trajectories (cf.\\ exp\\_009b, peak 278.5 at 95K).\n\nThe 93\\%/7\\%/0\\% split reveals that $e_{\\Delta t}$ learns to encode temporal information that minimizes \\textit{observation reconstruction error}, not reward prediction error. CIVO originates in the observation reconstruction objective's influence on latent dynamics---a structural property of DreamerV3's multi-head decoder architecture \\citep{hafner2023dreamerv3}. This constrains the space of viable interventions: strategies targeting the reward pathway alone address $<$1\\% of the gradient flow and cannot attenuate CIVO. The full-pathway SGS intervention (exp\\_018; Section~\\ref{sec:pending}) removes the dominant 93\\% observation decoder contribution, constituting a genuine gradient-level intervention.\n\nThis gradient asymmetry is consistent with prior observations on the dominance of reconstruction losses in world-model training \\citep{hafner2023dreamerv3, ma2024harmonydream}, but the D061 analysis provides the first \\textit{backward-pass decomposition} quantifying the per-component gradient contributions to a conditioning variable. HarmonyDream \\citep{ma2024harmonydream} reports a two-order-of-magnitude gap between observation and reward loss magnitudes; our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.\n\n\n% ============================================================\n% THREE FAILURE MODES\n% ============================================================\n\n\\subsection{Three Distinct Failure Modes}\n\\label{sec:failure_taxonomy}\n\n\\begin{figure}[t]\n  \\centering\n  % PLACEHOLDER: Contrasting collapse dynamics across three mechanisms\n  \\includegraphics[width=\\linewidth]{figures/fig6_failure_modes.pdf}\n  \\caption{Three failure modes triggered by temporal embedding configurations. Left: CIVO (exp\\_008d)---value explosion drives eval decline, entropy decreases. Center: Gradient starvation (exp\\_015b)---actor loss approaches zero, performance oscillates without convergence. Right: IRD (exp\\_008e\\_v3\\_s2)---eval collapse precedes value rise, entropy increases.}\n  \\label{fig:failure_modes}\n\\end{figure}\n\nThe experiments reveal three mechanistically distinct failure modes. Distinguishing these modes is necessary for designing targeted interventions, as surface-level metrics (e.g., low final eval return) are shared across all three but the underlying dynamics differ qualitatively.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Taxonomy of failure modes identified across temporal embedding configurations.}\n\\label{tab:failure_taxonomy}\n\\begin{tabular}{lccc}\n\\toprule\nFeature & CIVO & Grad.\\ Starvation & IRD \\\\\n\\midrule\nRepresentative exp & 008d (seed 1) & 015b & 008e\\_v3\\_s2 \\\\\n$e_{\\Delta t}$ config & trained & frozen & trained \\\\\nNVE trajectory & sustained $>$1.5$\\times$ & $<$0.5$\\times$ & passive rise \\\\\nValue dynamics & explosion ($+$130\\%) & suppressed & stable \\\\\nEval dynamics & decline & volatile (80--238) & collapse ($-$81\\%) \\\\\nActor entropy & $\\downarrow$ (locks in) & --- & $\\uparrow$ (de-specializes) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditioning-Induced Value Overestimation (CIVO).} In exp\\_008d and exp\\_006, the trained temporal embedding enables the reward head to produce systematically biased $\\Delta t{>}1$ predictions. RSSM fidelity analysis reveals a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions in exp\\_008d (see Table~\\ref{tab:rssm_fidelity} in Section~\\ref{sec:rssm_analysis}). The critic inherits these biases through the $\\lambda$-return computation, overestimates values for $\\Delta t{>}1$ trajectories, and the actor exploits the overestimated landscape. This positive feedback loop produces accelerating NVE ($1.71\\times \\to 2.09\\times \\to 4.12\\times$ at 35--55K in exp\\_008d) with decreasing actor entropy---the policy becomes increasingly deterministic as it converges on the overestimated region.\n\n\\paragraph{Gradient Starvation.} A frozen temporal embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}) cannot co-adapt as RSSM representations drift during training. Actor loss approaches zero (0.0002 at 105K, exp\\_015b), indicating gradient starvation: the actor receives insufficient learning signal. NVE remains at 0.39--0.47$\\times$ (exp\\_015b)---the critic \\textit{under-estimates}, the opposite of CIVO. Evaluation oscillates between 80 and 238 without convergence. The NVE briefly reaches 1.45$\\times$ at 55K but self-corrects to 0.65$\\times$ by 65K---a transient, sub-threshold overestimation qualitatively different from CIVO's sustained acceleration.\n\n\\paragraph{Imagination-Reality Divergence (IRD).} Exp\\_008e\\_v3\\_s2 collapses despite using $\\Delta t{=}1$-only imagination (\\texttt{gate\\_dt\\_mean}$\\,{=}\\,$1.0 throughout, exp\\_008e\\_v3\\_s2). Evaluation drops from 715.2 at 85K to 137.0 at 105K, while value estimates remain relatively stable (339.3 $\\to$ 339.8), producing a passive NVE rise to $3.78\\times$ (exp\\_008e\\_v3\\_s2). Crucially, actor entropy \\textit{increases} from $-5.21$ to $-3.83$ during collapse (policy de-specialization), the opposite of CIVO's entropy decrease. The baseline seed~2 (exp\\_009a) is stable through the same window (618.7 $\\to$ 836.5 at 85K--105K, exp\\_009a), ruling out seed-specific fragility.\n\nThis failure mode does not involve value overestimation driving actor exploitation. Rather, the trained embedding's interaction with multi-rate training data appears to create a latent representation vulnerability that manifests as policy instability independent of imagination $\\Delta t$. The NVE rise is a \\textit{consequence} of eval collapse, not a cause---distinguishing IRD from CIVO where the NVE rise precedes and drives the eval decline.\n\nThe existence of IRD alongside CIVO suggests that the trained temporal embedding creates vulnerability through multiple pathways. Eliminating CIVO (e.g., via $\\Delta t{=}1$ imagination) does not eliminate all failure modes.\n\n\n% ============================================================\n% PENDING EXPERIMENTS (PLACEHOLDERS)\n% ============================================================\n\n\\subsection{Pending Experiments}\n\\label{sec:pending}\n\nTwo experiment series are queued to extend the diagnostic analysis:\n\n\\paragraph{Full-pathway SGS (exp\\_018).} Detaches all non-KL gradients from the temporal embedding, removing the dominant 93\\% observation decoder contribution while retaining only the 7\\% KL dynamics signal. If CIVO persists with only KL gradients, the vulnerability is representation-level (KL training alone sufficient); if eliminated, the observation decoder gradient pathway is the root cause. Results will be reported upon completion.\n\n\\paragraph{Cross-environment validation (exp\\_019 series).} PickCube-v1 (ManiSkill3) baseline (exp\\_019a) and CIVO trigger condition (exp\\_019b) to test whether the identified mechanisms transfer beyond locomotion to manipulation tasks with qualitatively different observation and reward structure.\n",
      "numLines": 258,
      "startLine": 1,
      "totalLines": 258
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_0126KyfnjT6FM7ZMRum334Ut`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "b5523804-4698-44ca-a1e5-66f88fa837c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9TweX4QJwG3YahSoeWEgm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11639,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11639
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

_source line 9 · 2026-05-16T16:26:21.472Z_

<details><summary>↩ Tool result · `toolu_0126KyfnjT6FM7ZMRum334Ut`</summary>

```text
1	% Method — Draft v2
2	% Target: CoRL 2026
3	% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8).
4	% Note: Complements experimental_setup.md (Section 4). Some overlap in
5	%   diagnostic framework and factorial design is intentional—final paper
6	%   may merge or redistribute content between Sections 3 and 4.
7	
8	# 3. Methodology
9	
10	We present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.
11	
12	
13	## 3.1 Background: DreamerV3 and Variable-Rate Imagination
14	
15	### World-Model Actor-Critic
16	
17	DreamerV3 \citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:
18	
19	$$h_{t+1} = f_\theta(h_t, z_t, a_t), \quad \hat{z}_{t+1} \sim p_\theta(\cdot \mid h_{t+1})$$
20	
21	An actor $\pi_\psi$ selects actions and a critic $V_\xi$ estimates $\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\Delta t = 1$) and $H = 15$.
22	
23	### Temporal Abstraction via Variable-Rate Imagination
24	
25	Temporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.
26	
27	We introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:
28	
29	**Temporal step-size embedding.** An embedding $e_{\Delta t} \in \mathbb{R}^d$ conditions the RSSM transition on the step size:
30	
31	$$h_{t+\Delta t} = f_\theta(h_t, z_t, a_t, e_{\Delta t})$$
32	
33	We study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\Delta t$ values; the untrained and removed configurations serve as controls.
34	
35	**Temporal subsampling.** When enabled, the replay buffer stores both $\Delta t{=}1$ and $\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\Delta t{=}1$ transitions are used for world-model training.
36	
37	**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\Delta t{=}1$ (standard) or $\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.
38	
39	### Conditioning-Induced Value Overestimation (CIVO)
40	
41	When the RSSM predicts $\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\xi$ receives precise $\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.
42	
43	We term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \& Schuurmans' \citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\Delta t}$ and the RSSM's degraded fidelity at $\Delta t > 1$, not the policy's representational capacity.
44	
45	
46	## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio
47	
48	### Motivation
49	
50	Distinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\_001\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.
51	
52	### Definition
53	
54	**Value-evaluation ratio.** At training step $k$:
55	
56	$$r_k = \frac{\bar{v}_k}{\bar{R}_k}$$
57	
58	where $\bar{v}_k$ is the mean predicted value across imagined states and $\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.
59	
60	**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:
61	
62	$$\hat{r}_k = \frac{r_k^{\,\text{exp}}}{r_k^{\,\text{baseline}}}$$
63	
64	This removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.
65	
66	### Diagnostic Thresholds
67	
68	We calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:
69	
70	- **$\hat{r}_k > 1.5$ (at $k \geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\_embedding conditions exceed 1.5$\times$ at 35K+ steps (exp\_008d seed 1: 1.71$\times$@35K $\to$ 2.09$\times$@45K; exp\_009b seed 2: 1.62$\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\_008f seed 1 peak: 1.02$\times$@25K; exp\_009c seed 2 peak: 1.26$\times$@25K).
71	
72	- **$0.8 \leq \hat{r}_k \leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.
73	
74	- **$\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.
75	
76	**Temporal validity constraint.** The NVE threshold applies only at $k \geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\_009b at 25K shows NVE = 2.05$\times$ and exp\_008e\_v3 at 25K shows NVE = 1.93$\times$, both artifacts of the baseline's $r_{25\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.
77	
78	**Aggregate diagnostic power.** Evaluating the 1.5$\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\ref{tab:nve_sensitivity}). The single false positive is exp\_008e\_v3\_s2, which exhibits late-onset NVE = 3.78$\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \S3.3. At a stricter threshold of 1.7$\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).
79	
80	### Properties of the NVE Metric
81	
82	Two properties make NVE informative for detecting the CIVO:
83	
84	**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\_008d shows NVE = 1.71$\times$@35K $\to$ 2.09$\times$@45K $\to$ 4.12$\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\_008a, exp\_008f) show stable or declining NVE trajectories.
85	
86	**Collapse association.** Sustained NVE $>$ 1.5$\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\_008d seed 1: three consecutive checkpoints above 1.5$\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\_009b seed 2: 1.62$\times$@45K $\to$ 1.41$\times$@55K $\to$ 0.94$\times$@65K, declining) does not lead to collapse. This pattern is consistent with a "point of no return" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.
87	
88	
89	## 3.3 Causal Analysis Protocol
90	
91	### Design Rationale
92	
93	This is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.
94	
95	### Factorial Structure
96	
97	We vary three factors (temporal embedding type $\times$ subsampling $\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \S4 for the complete configuration matrix). Rather than filling all cells of the $3 \times 2 \times 2$ grid, we prioritize the comparisons most informative for causal isolation.
98	
99	### Causal Chain and Its Tests
100	
101	The causal chain under investigation is:
102	
103	$$\text{trained } e_{\Delta t} \;\xrightarrow{\text{Link 1}}\; \text{pathological NVE} \;\xrightarrow{\text{Link 2}}\; \text{actor exploitation} \;\xrightarrow{\text{Link 3}}\; \text{performance collapse}$$
104	
105	Each link is tested by a specific controlled comparison:
106	
107	**Link 1: Trained dt\_embedding $\to$ pathological overestimation.** The comparison between exp\_008d (trained dt\_embedding, $d{=}32$) and exp\_008f (removed dt\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\Delta t{=}2$ imagination). Exp\_008d exhibits accelerating NVE (1.71$\times$@35K $\to$ 2.09$\times$@45K), while exp\_008f remains in the normal range (0.73$\times$@35K $\to$ 0.83$\times$@45K). This is the primary causal evidence.
108	
109	**Link 2: Sustained overestimation $\to$ collapse (stochastic).** Multi-seed replication of exp\_008d reveals that the NVE $>$ 1.5$\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\_008d) shows sustained NVE $>$ 1.5$\times$ across three checkpoints and collapses; seed 2 (exp\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.
110	
111	**Link 3: Imagination $\Delta t$ as the critical variable.** Exp\_008e\_v3 uses a trained dt\_embedding (identical to exp\_008d and exp\_006) but restricts imagination rollouts to $\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\_008e\_v3, seed 1) with NVE = 0.80$\times$ (healthy). The contrast with exp\_006 (same trained dt\_embedding, subsample ON, $H{=}15$, but $\Delta t{=}2$ imagination $\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\Delta t > 1$ predictions during imagination.
112	
113	### 2$\times$2 Ablation Matrix
114	
115	To close the causal loop, we cross dt\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:
116	
117	| dt\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |
118	|:---:|:---:|:---:|:---:|:---:|
119	| Trained ($d{=}32$) | ON | 008d | 4.12$\times$@55K (sustained $\uparrow$) | CIVO $\to$ collapse |
120	| Trained ($d{=}32$) | OFF | 008a | 0.93$\times$@55K | Stable, 85\% baseline@105K |
121	| Frozen ($d{=}32$) | ON | 015b | 1.45$\times$@55K $\to$ 0.65$\times$@65K | Sub-threshold transient; gradient starvation collapse |
122	| Removed ($d{=}0$) | ON | 008f | $\leq$1.02$\times$ | No CIVO |
123	
124	Trained dt\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\_015b: peak 1.45$\times$@55K) that self-corrects to 0.65$\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\times$. The subsample-OFF condition (exp\_008a) confirms that a trained embedding without exposure to $\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.
125	
126	### Supporting Analyses
127	
128	**Horizon effect (C5).** Exp\_008c ($H{=}8$) vs. exp\_008a ($H{=}15$), both with trained-but-unexposed dt\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\_008a: 778@105K; exp\_008c: 241@65K plateau).
129	
130	**Temporal distance amplification (C4).** Exp\_006 ($\Delta t{=}2$, peak 485@35K $\to$ collapse) vs. exp\_007 ($\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\Delta t$, consistent with compounding RSSM prediction errors. Only two $\Delta t$ values are tested; we report the monotonic trend (dt=1 $\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.
131	
132	### RSSM Fidelity Analysis
133	
134	To ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\Delta t{=}1$ vs. $\Delta t{=}2$ across three conditions (exp\_rssm\_fidelity\_analysis):
135	
136	| Condition | $\Delta t{=}1$ obs MSE | $\Delta t{=}2$ obs MSE | Obs gap | $\Delta t{=}1$ rew MAE | $\Delta t{=}2$ rew MAE | Rew gap |
137	|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
138	| Baseline (exp\_001) | 13.49 | 27.50 | 2.04$\times$ | 0.0102 | 0.0159 | 1.56$\times$ |
139	| 008d (trained emb) | 41.31 | 53.67 | 1.30$\times$ | 0.0568 | 0.1579 | 2.78$\times$ |
140	| 008f (no emb) | 8.01 | 22.04 | 2.75$\times$ | 0.7469 | 0.7526 | 1.01$\times$ |
141	
142	Two patterns are diagnostically relevant:
143	
144	1. **Trained embedding enables differentiated but biased reward predictions.** In exp\_008d, the reward head produces sharply different predictions for $\Delta t{=}1$ vs. $\Delta t{=}2$ (reward gap 2.78$\times$), but these differentiated predictions rest on poor absolute state quality ($\Delta t{=}1$ obs MSE = 41.31, 3.1$\times$ baseline). The critic receives confident but systematically biased reward signals at $\Delta t{=}2$, fueling value overestimation.
145	
146	2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\_008f, the reward head cannot distinguish $\Delta t$ values (gap 1.01$\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\times$ baseline). Exp\_008f is therefore a *causal control* that confirms the dt\_embedding's role in overestimation, not a recommended configuration.
147	
148	**Caveat on obs gap ratios.** Exp\_008d's low obs gap ratio (1.30$\times$) is misleading---its $\Delta t{=}1$ absolute error is already 3.1$\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.
149	
150	### Gradient Decomposition of the Temporal Embedding
151	\label{sec:gradient_decomposition}
152	
153	To identify which loss component drives $e_{\Delta t}$'s learned representation, we decompose $\nabla_\theta e_{\Delta t}$ by loss term using \texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061). DreamerV3's joint loss \citep{hafner2023dreamerv3} sums observation reconstruction, reward prediction, continuation, and KL regularization terms; each backpropagates through the shared RSSM latent state to reach $e_{\Delta t}$.
154	
155	| Loss component | Gradient norm | Share (\%) |
156	|----------------|:---:|:---:|
157	| Observation decoders (orientations, velocity, height) | 1.505 | 93 |
158	| KL dynamics | 0.119 | 7 |
159	| Continuation head | $<$0.001 | $<$1 |
160	| Reward head | 0.000 | 0 |
161	
162	The temporal embedding receives 93\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). This gradient imbalance is consistent with findings that observation reconstruction dominates reward learning in DreamerV3-type world models \citep{shang2024harmonydream}, and represents an extreme instance of multi-task gradient magnitude imbalance \citep{chen2018gradnorm}. Three implications follow:
163	
164	1. **Exp\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.
165	
166	2. **$e_{\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.
167	
168	3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\% contribution from observation decoders. This motivates the full SGS design (exp\_018), which detaches $e_{\Delta t}$ from all non-KL gradient pathways.
169	
170	### Stop-Gradient Surgery: An Informative Negative (exp\_016e)
171	\label{sec:sgs_negative}
172	
173	The gradient decomposition above was motivated by a null result: exp\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\Delta t}$.
174	
175	**Configuration.** Exp\_016e replicates exp\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\Delta t}$, subsampling ON, $H{=}8$, $\Delta t{=}2$ imagination) with one modification: \texttt{reward\_dt\_emb\_detach=True}, which applies $\text{sg}(\cdot)$ to $e_{\Delta t}$ before the reward head during the backward pass.
176	
177	**Results.** Exp\_016e collapses in the same qualitative pattern as exp\_008d. Peak eval return reaches 326.7 at 75K (exp\_016e), then drops to 31.7 by 95K---a 90.3\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\times$ at 95K (exp\_016e). The timing difference relative to exp\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.
178	
179	**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\ 1 scalar reward) dominates the gradient signal to $e_{\Delta t}$ by two orders of magnitude.
180	
181	**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\% of the gradient flow to $e_{\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\_018) or by restructuring how $e_{\Delta t}$ interacts with the RSSM transition function.
182	
183	### Imagination Step Size as Causal Variable
184	
185	The factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:
186	
187	**$\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\_008e\_v3 uses the same trained dt\_embedding and multi-rate training data as exp\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\_008e\_v3, seed 1), 95\% of baseline (exp\_001\_baseline: 915.67@105K), with NVE = 0.80$\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\Delta t > 1$ predictions during imagination.
188	
189	**$\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\_008e\_v3\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\_008e\_v3\_s2), with NVE = 3.78$\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\_008e\_v3\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\_008d.
190	
191	**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:
192	
193	- *Pathway A (CIVO):* Trained dt\_embedding + $\Delta t{>}1$ imagination $\to$ value overestimation (NVE $\uparrow$) $\to$ actor over-exploitation (entropy $\downarrow$) $\to$ performance collapse. Observed in exp\_008d (seed 1) and exp\_009b (seed 2, transient).
194	
195	- *Pathway B (non-CIVO):* $\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\_008e\_v3\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.
196	
197	To rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\_009a), comparable to seed 1's 915.67 (exp\_001\_baseline). The collapse in exp\_008e\_v3\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.
198	
199	**Implication.** Restricting imagination to $\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "61b56313-702e-4e9a-9b8d-d13c84ffedf4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md",
      "content": "% Method — Draft v2\n% Target: CoRL 2026\n% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8).\n% Note: Complements experimental_setup.md (Section 4). Some overlap in\n%   diagnostic framework and factorial design is intentional—final paper\n%   may merge or redistribute content between Sections 3 and 4.\n\n# 3. Methodology\n\nWe present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \\citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \\citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.\n\n\n## 3.1 Background: DreamerV3 and Variable-Rate Imagination\n\n### World-Model Actor-Critic\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:\n\n$$h_{t+1} = f_\\theta(h_t, z_t, a_t), \\quad \\hat{z}_{t+1} \\sim p_\\theta(\\cdot \\mid h_{t+1})$$\n\nAn actor $\\pi_\\psi$ selects actions and a critic $V_\\xi$ estimates $\\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\\Delta t = 1$) and $H = 15$.\n\n### Temporal Abstraction via Variable-Rate Imagination\n\nTemporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \\citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.\n\nWe introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:\n\n**Temporal step-size embedding.** An embedding $e_{\\Delta t} \\in \\mathbb{R}^d$ conditions the RSSM transition on the step size:\n\n$$h_{t+\\Delta t} = f_\\theta(h_t, z_t, a_t, e_{\\Delta t})$$\n\nWe study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\\Delta t$ values; the untrained and removed configurations serve as controls.\n\n**Temporal subsampling.** When enabled, the replay buffer stores both $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\\Delta t{=}1$ transitions are used for world-model training.\n\n**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\\Delta t{=}1$ (standard) or $\\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.\n\n### Conditioning-Induced Value Overestimation (CIVO)\n\nWhen the RSSM predicts $\\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\\xi$ receives precise $\\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.\n\nWe term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \\& Schuurmans' \\citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\\Delta t}$ and the RSSM's degraded fidelity at $\\Delta t > 1$, not the policy's representational capacity.\n\n\n## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio\n\n### Motivation\n\nDistinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\\_001\\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.\n\n### Definition\n\n**Value-evaluation ratio.** At training step $k$:\n\n$$r_k = \\frac{\\bar{v}_k}{\\bar{R}_k}$$\n\nwhere $\\bar{v}_k$ is the mean predicted value across imagined states and $\\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.\n\n**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:\n\n$$\\hat{r}_k = \\frac{r_k^{\\,\\text{exp}}}{r_k^{\\,\\text{baseline}}}$$\n\nThis removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.\n\n### Diagnostic Thresholds\n\nWe calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:\n\n- **$\\hat{r}_k > 1.5$ (at $k \\geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\\_embedding conditions exceed 1.5$\\times$ at 35K+ steps (exp\\_008d seed 1: 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K; exp\\_009b seed 2: 1.62$\\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\\_008f seed 1 peak: 1.02$\\times$@25K; exp\\_009c seed 2 peak: 1.26$\\times$@25K).\n\n- **$0.8 \\leq \\hat{r}_k \\leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.\n\n- **$\\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.\n\n**Temporal validity constraint.** The NVE threshold applies only at $k \\geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\\_009b at 25K shows NVE = 2.05$\\times$ and exp\\_008e\\_v3 at 25K shows NVE = 1.93$\\times$, both artifacts of the baseline's $r_{25\\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.\n\n**Aggregate diagnostic power.** Evaluating the 1.5$\\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\\ref{tab:nve_sensitivity}). The single false positive is exp\\_008e\\_v3\\_s2, which exhibits late-onset NVE = 3.78$\\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \\S3.3. At a stricter threshold of 1.7$\\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).\n\n### Properties of the NVE Metric\n\nTwo properties make NVE informative for detecting the CIVO:\n\n**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\\_008d shows NVE = 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K $\\to$ 4.12$\\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\\_008a, exp\\_008f) show stable or declining NVE trajectories.\n\n**Collapse association.** Sustained NVE $>$ 1.5$\\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\\_008d seed 1: three consecutive checkpoints above 1.5$\\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\\_009b seed 2: 1.62$\\times$@45K $\\to$ 1.41$\\times$@55K $\\to$ 0.94$\\times$@65K, declining) does not lead to collapse. This pattern is consistent with a \"point of no return\" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.\n\n\n## 3.3 Causal Analysis Protocol\n\n### Design Rationale\n\nThis is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.\n\n### Factorial Structure\n\nWe vary three factors (temporal embedding type $\\times$ subsampling $\\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \\S4 for the complete configuration matrix). Rather than filling all cells of the $3 \\times 2 \\times 2$ grid, we prioritize the comparisons most informative for causal isolation.\n\n### Causal Chain and Its Tests\n\nThe causal chain under investigation is:\n\n$$\\text{trained } e_{\\Delta t} \\;\\xrightarrow{\\text{Link 1}}\\; \\text{pathological NVE} \\;\\xrightarrow{\\text{Link 2}}\\; \\text{actor exploitation} \\;\\xrightarrow{\\text{Link 3}}\\; \\text{performance collapse}$$\n\nEach link is tested by a specific controlled comparison:\n\n**Link 1: Trained dt\\_embedding $\\to$ pathological overestimation.** The comparison between exp\\_008d (trained dt\\_embedding, $d{=}32$) and exp\\_008f (removed dt\\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\\Delta t{=}2$ imagination). Exp\\_008d exhibits accelerating NVE (1.71$\\times$@35K $\\to$ 2.09$\\times$@45K), while exp\\_008f remains in the normal range (0.73$\\times$@35K $\\to$ 0.83$\\times$@45K). This is the primary causal evidence.\n\n**Link 2: Sustained overestimation $\\to$ collapse (stochastic).** Multi-seed replication of exp\\_008d reveals that the NVE $>$ 1.5$\\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\\_008d) shows sustained NVE $>$ 1.5$\\times$ across three checkpoints and collapses; seed 2 (exp\\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.\n\n**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n### 2$\\times$2 Ablation Matrix\n\nTo close the causal loop, we cross dt\\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:\n\n| dt\\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |\n|:---:|:---:|:---:|:---:|:---:|\n| Trained ($d{=}32$) | ON | 008d | 4.12$\\times$@55K (sustained $\\uparrow$) | CIVO $\\to$ collapse |\n| Trained ($d{=}32$) | OFF | 008a | 0.93$\\times$@55K | Stable, 85\\% baseline@105K |\n| Frozen ($d{=}32$) | ON | 015b | 1.45$\\times$@55K $\\to$ 0.65$\\times$@65K | Sub-threshold transient; gradient starvation collapse |\n| Removed ($d{=}0$) | ON | 008f | $\\leq$1.02$\\times$ | No CIVO |\n\nTrained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\\_015b: peak 1.45$\\times$@55K) that self-corrects to 0.65$\\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\\times$. The subsample-OFF condition (exp\\_008a) confirms that a trained embedding without exposure to $\\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.\n\n### Supporting Analyses\n\n**Horizon effect (C5).** Exp\\_008c ($H{=}8$) vs. exp\\_008a ($H{=}15$), both with trained-but-unexposed dt\\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\\_008a: 778@105K; exp\\_008c: 241@65K plateau).\n\n**Temporal distance amplification (C4).** Exp\\_006 ($\\Delta t{=}2$, peak 485@35K $\\to$ collapse) vs. exp\\_007 ($\\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\\Delta t$, consistent with compounding RSSM prediction errors. Only two $\\Delta t$ values are tested; we report the monotonic trend (dt=1 $\\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.\n\n### RSSM Fidelity Analysis\n\nTo ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\\Delta t{=}1$ vs. $\\Delta t{=}2$ across three conditions (exp\\_rssm\\_fidelity\\_analysis):\n\n| Condition | $\\Delta t{=}1$ obs MSE | $\\Delta t{=}2$ obs MSE | Obs gap | $\\Delta t{=}1$ rew MAE | $\\Delta t{=}2$ rew MAE | Rew gap |\n|-----------|:---:|:---:|:---:|:---:|:---:|:---:|\n| Baseline (exp\\_001) | 13.49 | 27.50 | 2.04$\\times$ | 0.0102 | 0.0159 | 1.56$\\times$ |\n| 008d (trained emb) | 41.31 | 53.67 | 1.30$\\times$ | 0.0568 | 0.1579 | 2.78$\\times$ |\n| 008f (no emb) | 8.01 | 22.04 | 2.75$\\times$ | 0.7469 | 0.7526 | 1.01$\\times$ |\n\nTwo patterns are diagnostically relevant:\n\n1. **Trained embedding enables differentiated but biased reward predictions.** In exp\\_008d, the reward head produces sharply different predictions for $\\Delta t{=}1$ vs. $\\Delta t{=}2$ (reward gap 2.78$\\times$), but these differentiated predictions rest on poor absolute state quality ($\\Delta t{=}1$ obs MSE = 41.31, 3.1$\\times$ baseline). The critic receives confident but systematically biased reward signals at $\\Delta t{=}2$, fueling value overestimation.\n\n2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\\_008f, the reward head cannot distinguish $\\Delta t$ values (gap 1.01$\\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\\times$ baseline). Exp\\_008f is therefore a *causal control* that confirms the dt\\_embedding's role in overestimation, not a recommended configuration.\n\n**Caveat on obs gap ratios.** Exp\\_008d's low obs gap ratio (1.30$\\times$) is misleading---its $\\Delta t{=}1$ absolute error is already 3.1$\\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.\n\n### Gradient Decomposition of the Temporal Embedding\n\\label{sec:gradient_decomposition}\n\nTo identify which loss component drives $e_{\\Delta t}$'s learned representation, we decompose $\\nabla_\\theta e_{\\Delta t}$ by loss term using \\texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061). DreamerV3's joint loss \\citep{hafner2023dreamerv3} sums observation reconstruction, reward prediction, continuation, and KL regularization terms; each backpropagates through the shared RSSM latent state to reach $e_{\\Delta t}$.\n\n| Loss component | Gradient norm | Share (\\%) |\n|----------------|:---:|:---:|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93 |\n| KL dynamics | 0.119 | 7 |\n| Continuation head | $<$0.001 | $<$1 |\n| Reward head | 0.000 | 0 |\n\nThe temporal embedding receives 93\\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). This gradient imbalance is consistent with findings that observation reconstruction dominates reward learning in DreamerV3-type world models \\citep{shang2024harmonydream}, and represents an extreme instance of multi-task gradient magnitude imbalance \\citep{chen2018gradnorm}. Three implications follow:\n\n1. **Exp\\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.\n\n2. **$e_{\\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.\n\n3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\\% contribution from observation decoders. This motivates the full SGS design (exp\\_018), which detaches $e_{\\Delta t}$ from all non-KL gradient pathways.\n\n### Stop-Gradient Surgery: An Informative Negative (exp\\_016e)\n\\label{sec:sgs_negative}\n\nThe gradient decomposition above was motivated by a null result: exp\\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\\Delta t}$.\n\n**Configuration.** Exp\\_016e replicates exp\\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\\Delta t}$, subsampling ON, $H{=}8$, $\\Delta t{=}2$ imagination) with one modification: \\texttt{reward\\_dt\\_emb\\_detach=True}, which applies $\\text{sg}(\\cdot)$ to $e_{\\Delta t}$ before the reward head during the backward pass.\n\n**Results.** Exp\\_016e collapses in the same qualitative pattern as exp\\_008d. Peak eval return reaches 326.7 at 75K (exp\\_016e), then drops to 31.7 by 95K---a 90.3\\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\\times$ at 95K (exp\\_016e). The timing difference relative to exp\\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.\n\n**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\\ 1 scalar reward) dominates the gradient signal to $e_{\\Delta t}$ by two orders of magnitude.\n\n**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.\n\n### Imagination Step Size as Causal Variable\n\nThe factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:\n\n**$\\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\\_008e\\_v3 uses the same trained dt\\_embedding and multi-rate training data as exp\\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95\\% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n**$\\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\\_008e\\_v3\\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\\_008e\\_v3\\_s2), with NVE = 3.78$\\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\\_008e\\_v3\\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\\_008d.\n\n**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:\n\n- *Pathway A (CIVO):* Trained dt\\_embedding + $\\Delta t{>}1$ imagination $\\to$ value overestimation (NVE $\\uparrow$) $\\to$ actor over-exploitation (entropy $\\downarrow$) $\\to$ performance collapse. Observed in exp\\_008d (seed 1) and exp\\_009b (seed 2, transient).\n\n- *Pathway B (non-CIVO):* $\\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\\_008e\\_v3\\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.\n\nTo rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\\_009a), comparable to seed 1's 915.67 (exp\\_001\\_baseline). The collapse in exp\\_008e\\_v3\\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.\n\n**Implication.** Restricting imagination to $\\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.\n",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 200
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01PPVcNhJNfBHHpVXKUr5cyL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/sgs_gradient_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "698d0284-e573-42f4-8de6-3c80687d5a1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9TweX4QJwG3YahSoeWEgm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11639,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11639
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

_source line 11 · 2026-05-16T16:26:21.947Z_

<details><summary>↩ Tool result · `toolu_01PPVcNhJNfBHHpVXKUr5cyL`</summary>

```text
1	% SGS Gradient Analysis — Draft v1
2	% Target: CoRL 2026
3	% Status: Draft, pending Director review
4	% Depends on: method.md (Section 3), experimental_setup.md (Section 4)
5	% Note: Supersedes sgs_informative_negative.md with tighter structure
6	%   and stronger quantitative grounding per D061 gradient decomposition.
7	
8	\subsection{Selective Gradient Stopping and Gradient Decomposition}
9	\label{sec:sgs_gradient_analysis}
10	
11	\subsubsection{Design and Hypothesis}
12	\label{sec:sgs_design}
13	
14	The preceding analysis establishes that a trained temporal embedding $e_{\Delta t}$ is necessary for CIVO (Section~\ref{sec:civo_mechanism}). We next ask \textit{which gradient pathway} through $e_{\Delta t}$ amplifies the overestimation. In DreamerV3, the temporal embedding conditions all prediction heads simultaneously through the RSSM latent state. A natural hypothesis is that the \textit{reward head}---which directly supplies $\lambda$-return targets to the critic---is the primary amplifier: if reward predictions develop $\Delta t$-dependent biases, the critic inherits and compounds these biases across the $H$-step imagination rollout.
15	
16	To test this, we introduce \textit{selective gradient stopping} (SGS): during the backward pass, $e_{\Delta t}$ is detached before entering the reward head,
17	$$\hat{r}_t = f_{\text{reward}}\big(\operatorname{sg}(e_{\Delta t}),\; h_t,\; z_t\big),$$
18	where $\operatorname{sg}(\cdot)$ denotes the stop-gradient operator. This prevents reward-loss gradients from updating $e_{\Delta t}$'s parameters while preserving the embedding's forward-pass contribution. All other gradient pathways---observation decoders, continuation predictor, KL dynamics---remain intact. We apply this intervention to the primary CIVO-exhibiting configuration: Walker Walk, trained $e_{\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\Delta t{=}2$ imagination (exp\_016e; identical to exp\_008d except for \texttt{reward\_dt\_emb\_detach=True}).
19	
20	
21	\subsubsection{Gradient Decomposition Reveals the Reward Pathway is Inactive}
22	\label{sec:gradient_decomposition}
23	
24	Exp\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps (exp\_016e) followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\times$ (exp\_016e). The SGS intervention neither prevented nor attenuated CIVO.
25	
26	To explain this null result, we performed a gradient decomposition analysis using \texttt{torch.autograd.grad} to measure each loss component's contribution to $\nabla_\theta e_{\Delta t}$, where $\theta$ denotes the temporal embedding parameters (D061). Table~\ref{tab:gradient_decomposition} reports the results.
27	
28	\begin{table}[h]
29	\centering
30	\caption{Gradient contributions to the temporal embedding $e_{\Delta t}$ by loss component, measured via \texttt{torch.autograd.grad} (D061). Gradient norms are $\ell_2$ norms of $\nabla_\theta \mathcal{L}_i$ for each loss $\mathcal{L}_i$.}
31	\label{tab:gradient_decomposition}
32	\small
33	\begin{tabular}{lrr}
34	\toprule
35	Loss component & $\|\nabla_\theta \mathcal{L}_i\|_2$ & Share (\%) \\
36	\midrule
37	Observation decoders (orientations, velocity, height) & 1.505 & 92.7 \\
38	KL dynamics & 0.119 & 7.3 \\
39	Continuation head & $<$0.001 & $<$0.1 \\
40	Reward head & 0.000 & 0.0 \\
41	\midrule
42	\textbf{Total} & \textbf{1.624} & \textbf{100} \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	The reward head contributes \textit{numerically negligible---zero to within floating-point precision} gradient to the temporal embedding. Exp\_016e's stop-gradient intervention detaches a gradient pathway that carries no signal---it is an architectural no-op. The null result is therefore expected: the intervention removes nothing.
48	
49	The zero reward gradient is a consequence of the relative output dimensionality. All decoder losses backpropagate through the same RSSM latent state to reach $e_{\Delta t}$. The observation decoders reconstruct a 24-dimensional proprioceptive signal (14 orientations, 9 velocities, 1 height), while the reward head predicts a single scalar. This ${\sim}24\!\times$ dimensionality asymmetry, compounded by DreamerV3's symlog reward scaling which further compresses the reward gradient magnitude, renders the reward head's contribution numerically negligible---zero to within floating-point precision.
50	
51	
52	\subsubsection{Implications for the CIVO Mechanism}
53	\label{sec:sgs_implications}
54	
55	The gradient decomposition reframes the mechanistic understanding of how the temporal embedding drives CIVO.
56	
57	\paragraph{Observation reconstruction dominates temporal embedding learning.} The temporal embedding's parameters are shaped almost entirely (93\%) by the observation reconstruction objective (D061). This means $e_{\Delta t}$ learns to encode temporal information that helps minimize \textit{observation prediction error}, not reward prediction error. If this learned representation introduces systematic biases in latent state predictions at $\Delta t{>}1$---for instance, by encouraging the RSSM to produce states that are easy to decode but dynamically inaccurate---these biases propagate to \textit{all} downstream computation, including reward prediction and the critic's value estimates. CIVO thus originates in the observation reconstruction objective's influence on latent dynamics, not in reward-specific pathways.
58	
59	\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone---reward prediction regularization, reward-conditioned value clipping, or the reward-only SGS tested here---addresses $<$1\% of the gradient flow to $e_{\Delta t}$ and cannot attenuate CIVO. Effective gradient-level interventions must address the dominant observation decoder pathway. This motivates the \textit{full-pathway SGS} design (exp\_018): detaching $e_{\Delta t}$ from all decoder and reward gradients, retaining only the 7\% KL dynamics contribution. Full-pathway SGS removes 93\% of the gradient to $e_{\Delta t}$, constituting a genuine gradient-level intervention rather than the null operation of reward-only SGS.
60	
61	\paragraph{Connection to RSSM fidelity analysis.} The observation-dominated gradient structure is consistent with the RSSM fidelity results in Table~\ref{tab:rssm_fidelity}: the trained-embedding condition (exp\_008d) shows a $2.78\times$ reward gap between $\Delta t{=}1$ and $\Delta t{=}2$ transitions, despite the reward head receiving zero gradient from $e_{\Delta t}$. This confirms that the reward head's $\Delta t$-dependent biases are inherited \textit{through the latent state}---which is shaped by observation reconstruction gradients---rather than learned directly from the reward objective.
62	
63	
64	\subsubsection{Exp\_016e Reinterpreted as Stochastic Variation}
65	\label{sec:016e_reinterp}
66	
67	With the gradient decomposition establishing that exp\_016e is a no-op intervention, the apparent timing differences between exp\_016e and exp\_008d---later collapse onset (75K vs.\ 25K) and higher peak evaluation (326.7 vs.\ 167.2)---must be attributed to stochastic variation rather than SGS effects. This attribution is consistent with the seed-to-seed variability already observed within the trained-embedding condition: exp\_009b (same configuration as exp\_008d, seed 2) reaches peak evaluation 278.5 at 95K (exp\_009b) with transient NVE of $1.62\times$ at 45K before self-correcting, compared to exp\_008d's monotonic collapse from 25K. The qualitative diversity between exp\_008d (early collapse), exp\_009b (self-correction), and exp\_016e (delayed collapse) falls within the range of stochastic outcomes for a single trained-$e_{\Delta t}$ configuration.
68	
69	All three trajectories share the invariant identified by the NVE diagnostic: each crosses the $1.5\times$ pathological threshold at some point during training (exp\_008d at 35K: $1.71\times$; exp\_009b at 45K: $1.62\times$; exp\_016e at 95K: $10.42\times$). Whether this pathological overestimation leads to sustained collapse or transient recovery depends on early training stochasticity, not on the reward-only SGS intervention (D061).
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "684c6f65-0271-4469-9d0a-7cad20f97e49",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/sgs_gradient_analysis.md",
      "content": "% SGS Gradient Analysis — Draft v1\n% Target: CoRL 2026\n% Status: Draft, pending Director review\n% Depends on: method.md (Section 3), experimental_setup.md (Section 4)\n% Note: Supersedes sgs_informative_negative.md with tighter structure\n%   and stronger quantitative grounding per D061 gradient decomposition.\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Design and Hypothesis}\n\\label{sec:sgs_design}\n\nThe preceding analysis establishes that a trained temporal embedding $e_{\\Delta t}$ is necessary for CIVO (Section~\\ref{sec:civo_mechanism}). We next ask \\textit{which gradient pathway} through $e_{\\Delta t}$ amplifies the overestimation. In DreamerV3, the temporal embedding conditions all prediction heads simultaneously through the RSSM latent state. A natural hypothesis is that the \\textit{reward head}---which directly supplies $\\lambda$-return targets to the critic---is the primary amplifier: if reward predictions develop $\\Delta t$-dependent biases, the critic inherits and compounds these biases across the $H$-step imagination rollout.\n\nTo test this, we introduce \\textit{selective gradient stopping} (SGS): during the backward pass, $e_{\\Delta t}$ is detached before entering the reward head,\n$$\\hat{r}_t = f_{\\text{reward}}\\big(\\operatorname{sg}(e_{\\Delta t}),\\; h_t,\\; z_t\\big),$$\nwhere $\\operatorname{sg}(\\cdot)$ denotes the stop-gradient operator. This prevents reward-loss gradients from updating $e_{\\Delta t}$'s parameters while preserving the embedding's forward-pass contribution. All other gradient pathways---observation decoders, continuation predictor, KL dynamics---remain intact. We apply this intervention to the primary CIVO-exhibiting configuration: Walker Walk, trained $e_{\\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\\Delta t{=}2$ imagination (exp\\_016e; identical to exp\\_008d except for \\texttt{reward\\_dt\\_emb\\_detach=True}).\n\n\n\\subsubsection{Gradient Decomposition Reveals the Reward Pathway is Inactive}\n\\label{sec:gradient_decomposition}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps (exp\\_016e) followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$ (exp\\_016e). The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters (D061). Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} (D061). Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\nLoss component & $\\|\\nabla_\\theta \\mathcal{L}_i\\|_2$ & Share (\\%) \\\\\n\\midrule\nObservation decoders (orientations, velocity, height) & 1.505 & 92.7 \\\\\nKL dynamics & 0.119 & 7.3 \\\\\nContinuation head & $<$0.001 & $<$0.1 \\\\\nReward head & 0.000 & 0.0 \\\\\n\\midrule\n\\textbf{Total} & \\textbf{1.624} & \\textbf{100} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reward head contributes \\textit{numerically negligible---zero to within floating-point precision} gradient to the temporal embedding. Exp\\_016e's stop-gradient intervention detaches a gradient pathway that carries no signal---it is an architectural no-op. The null result is therefore expected: the intervention removes nothing.\n\nThe zero reward gradient is a consequence of the relative output dimensionality. All decoder losses backpropagate through the same RSSM latent state to reach $e_{\\Delta t}$. The observation decoders reconstruct a 24-dimensional proprioceptive signal (14 orientations, 9 velocities, 1 height), while the reward head predicts a single scalar. This ${\\sim}24\\!\\times$ dimensionality asymmetry, compounded by DreamerV3's symlog reward scaling which further compresses the reward gradient magnitude, renders the reward head's contribution numerically negligible---zero to within floating-point precision.\n\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reframes the mechanistic understanding of how the temporal embedding drives CIVO.\n\n\\paragraph{Observation reconstruction dominates temporal embedding learning.} The temporal embedding's parameters are shaped almost entirely (93\\%) by the observation reconstruction objective (D061). This means $e_{\\Delta t}$ learns to encode temporal information that helps minimize \\textit{observation prediction error}, not reward prediction error. If this learned representation introduces systematic biases in latent state predictions at $\\Delta t{>}1$---for instance, by encouraging the RSSM to produce states that are easy to decode but dynamically inaccurate---these biases propagate to \\textit{all} downstream computation, including reward prediction and the critic's value estimates. CIVO thus originates in the observation reconstruction objective's influence on latent dynamics, not in reward-specific pathways.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone---reward prediction regularization, reward-conditioned value clipping, or the reward-only SGS tested here---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and cannot attenuate CIVO. Effective gradient-level interventions must address the dominant observation decoder pathway. This motivates the \\textit{full-pathway SGS} design (exp\\_018): detaching $e_{\\Delta t}$ from all decoder and reward gradients, retaining only the 7\\% KL dynamics contribution. Full-pathway SGS removes 93\\% of the gradient to $e_{\\Delta t}$, constituting a genuine gradient-level intervention rather than the null operation of reward-only SGS.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The observation-dominated gradient structure is consistent with the RSSM fidelity results in Table~\\ref{tab:rssm_fidelity}: the trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions, despite the reward head receiving zero gradient from $e_{\\Delta t}$. This confirms that the reward head's $\\Delta t$-dependent biases are inherited \\textit{through the latent state}---which is shaped by observation reconstruction gradients---rather than learned directly from the reward objective.\n\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nWith the gradient decomposition establishing that exp\\_016e is a no-op intervention, the apparent timing differences between exp\\_016e and exp\\_008d---later collapse onset (75K vs.\\ 25K) and higher peak evaluation (326.7 vs.\\ 167.2)---must be attributed to stochastic variation rather than SGS effects. This attribution is consistent with the seed-to-seed variability already observed within the trained-embedding condition: exp\\_009b (same configuration as exp\\_008d, seed 2) reaches peak evaluation 278.5 at 95K (exp\\_009b) with transient NVE of $1.62\\times$ at 45K before self-correcting, compared to exp\\_008d's monotonic collapse from 25K. The qualitative diversity between exp\\_008d (early collapse), exp\\_009b (self-correction), and exp\\_016e (delayed collapse) falls within the range of stochastic outcomes for a single trained-$e_{\\Delta t}$ configuration.\n\nAll three trajectories share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training (exp\\_008d at 35K: $1.71\\times$; exp\\_009b at 45K: $1.62\\times$; exp\\_016e at 95K: $10.42\\times$). Whether this pathological overestimation leads to sustained collapse or transient recovery depends on early training stochasticity, not on the reward-only SGS intervention (D061).\n",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 70
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01GsBSATBKmnDuGywjbRbXtB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_90ca4b.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "cb5838fa-0412-41f5-a7c9-6ddc85ac0ee3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01811RhctftxkAkJpejv45FM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17371,
      "cache_read_input_tokens": 23480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17371
      },
      "output_tokens": 35,
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

_source line 13 · 2026-05-16T16:26:27.749Z_

<details><summary>↩ Tool result · `toolu_01GsBSATBKmnDuGywjbRbXtB`</summary>

```text
1	% Method — Draft v1
2	% Target: CoRL 2026
3	% Status: Draft, pending Director review
4	% Note: Complements experimental_setup.md (Section 4). Some overlap in
5	%   diagnostic framework and factorial design is intentional—final paper
6	%   may merge or redistribute content between Sections 3 and 4.
7	
8	# 3. Methodology
9	
10	We present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.
11	
12	
13	## 3.1 Background: DreamerV3 and Variable-Rate Imagination
14	
15	### World-Model Actor-Critic
16	
17	DreamerV3 \citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:
18	
19	$$h_{t+1} = f_\theta(h_t, z_t, a_t), \quad \hat{z}_{t+1} \sim p_\theta(\cdot \mid h_{t+1})$$
20	
21	An actor $\pi_\psi$ selects actions and a critic $V_\xi$ estimates $\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\Delta t = 1$) and $H = 15$.
22	
23	### Temporal Abstraction via Variable-Rate Imagination
24	
25	Temporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.
26	
27	We introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:
28	
29	**Temporal step-size embedding.** An embedding $e_{\Delta t} \in \mathbb{R}^d$ conditions the RSSM transition on the step size:
30	
31	$$h_{t+\Delta t} = f_\theta(h_t, z_t, a_t, e_{\Delta t})$$
32	
33	We study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\Delta t$ values; the untrained and removed configurations serve as controls.
34	
35	**Temporal subsampling.** When enabled, the replay buffer stores both $\Delta t{=}1$ and $\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\Delta t{=}1$ transitions are used for world-model training.
36	
37	**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\Delta t{=}1$ (standard) or $\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.
38	
39	### The Delusional Critic Hypothesis
40	
41	When the RSSM predicts $\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\xi$ receives precise $\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model's delusions but suboptimal in reality.
42	
43	We term this the *CIVO*, drawing on Lu \& Schuurmans \citep{lu2018nondelusional}'s concept of delusional policies, where function approximation introduces inconsistencies in Q-learning backups. In our setting, the inconsistency is model-induced: imagined states at $\Delta t > 1$ deviate systematically from reality, but the critic treats them as accurate. This is a distinct instantiation of the general phenomenon---the delusion source is the world model's temporal extrapolation error, not the policy's functional form.
44	
45	
46	## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio
47	
48	### Motivation
49	
50	Distinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\_001\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.
51	
52	### Definition
53	
54	**Value-evaluation ratio.** At training step $k$:
55	
56	$$r_k = \frac{\bar{v}_k}{\bar{R}_k}$$
57	
58	where $\bar{v}_k$ is the mean predicted value across imagined states and $\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.
59	
60	**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:
61	
62	$$\hat{r}_k = \frac{r_k^{\,\text{exp}}}{r_k^{\,\text{baseline}}}$$
63	
64	This removes the baseline's own overshoot trend, isolating excess overestimation. In the current analysis, $r_k^{\text{baseline}}$ is computed from a single baseline seed (exp\_001\_baseline, seed 1, 500K steps); we will update to the mean of seeds 1 and 2 once exp\_009a completes.
65	
66	### Diagnostic Thresholds
67	
68	We calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:
69	
70	- **$\hat{r}_k > 1.5$ (at $k \geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\_embedding conditions exceed 1.5$\times$ at 35K+ steps (exp\_008d seed 1: 1.71$\times$@35K $\to$ 2.09$\times$@45K; exp\_009b seed 2: 1.62$\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\_008f seed 1 peak: 1.02$\times$@25K; exp\_009c seed 2 peak: 1.26$\times$@25K).
71	
72	- **$0.8 \leq \hat{r}_k \leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.
73	
74	- **$\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.
75	
76	**Temporal validity constraint.** The NVE threshold applies only at $k \geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\_009b at 25K shows NVE = 2.05$\times$ and exp\_008e\_v3 at 25K shows NVE = 1.93$\times$, both artifacts of the baseline's $r_{25\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.
77	
78	### Properties of the NVE Metric
79	
80	Two properties make NVE informative for detecting the CIVO:
81	
82	**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\_008d shows NVE = 1.71$\times$@35K $\to$ 2.09$\times$@45K $\to$ 4.12$\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\_008a, exp\_008f) show stable or declining NVE trajectories.
83	
84	**Collapse association.** Sustained NVE $>$ 1.5$\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\_008d seed 1: three consecutive checkpoints above 1.5$\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\_009b seed 2: 1.62$\times$@45K $\to$ 1.41$\times$@55K $\to$ 0.94$\times$@65K, declining) does not lead to collapse. This pattern is consistent with a "point of no return" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.
85	
86	
87	## 3.3 Causal Analysis Protocol
88	
89	### Design Rationale
90	
91	This is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.
92	
93	### Factorial Structure
94	
95	We vary three factors (temporal embedding type $\times$ subsampling $\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \S4 for the complete configuration matrix). Rather than filling all cells of the $3 \times 2 \times 2$ grid, we prioritize the comparisons most informative for causal isolation.
96	
97	### Causal Chain and Its Tests
98	
99	The causal chain under investigation is:
100	
101	$$\text{trained } e_{\Delta t} \;\xrightarrow{\text{Link 1}}\; \text{pathological NVE} \;\xrightarrow{\text{Link 2}}\; \text{actor exploitation} \;\xrightarrow{\text{Link 3}}\; \text{performance collapse}$$
102	
103	Each link is tested by a specific controlled comparison:
104	
105	**Link 1: Trained dt\_embedding $\to$ pathological overestimation.** The comparison between exp\_008d (trained dt\_embedding, $d{=}32$) and exp\_008f (removed dt\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\Delta t{=}2$ imagination). Exp\_008d exhibits accelerating NVE (1.71$\times$@35K $\to$ 2.09$\times$@45K), while exp\_008f remains in the normal range (0.73$\times$@35K $\to$ 0.83$\times$@45K). This is the primary causal evidence.
106	
107	**Link 2: Sustained overestimation $\to$ collapse (stochastic).** Multi-seed replication of exp\_008d reveals that the NVE $>$ 1.5$\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\_008d) shows sustained NVE $>$ 1.5$\times$ across three checkpoints and collapses; seed 2 (exp\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to 268@105K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.
108	
109	**Link 3: Imagination $\Delta t$ as the critical variable.** Exp\_008e\_v3 uses a trained dt\_embedding (identical to exp\_008d and exp\_006) but restricts imagination rollouts to $\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\_008e\_v3, seed 1) with NVE = 0.80$\times$ (healthy). The contrast with exp\_006 (same trained dt\_embedding, subsample ON, $H{=}15$, but $\Delta t{=}2$ imagination $\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\Delta t > 1$ predictions during imagination.
110	
111	### Supporting Analyses
112	
113	**Horizon effect (C5).** Exp\_008c ($H{=}8$) vs. exp\_008a ($H{=}15$), both with untrained dt\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\_008a: 778@105K; exp\_008c: 241@65K plateau).
114	
115	**Temporal distance amplification (C4).** Exp\_006 ($\Delta t{=}2$, peak 485@35K $\to$ collapse) vs. exp\_007 ($\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\Delta t$, consistent with compounding RSSM prediction errors. Only two $\Delta t$ values are tested; we report the monotonic trend (dt=1 $\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.
116	
117	### RSSM Fidelity Analysis
118	
119	To ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\Delta t{=}1$ vs. $\Delta t{=}2$ across three conditions (exp\_rssm\_fidelity\_analysis):
120	
121	| Condition | $\Delta t{=}1$ obs MSE | $\Delta t{=}2$ obs MSE | Obs gap | $\Delta t{=}1$ rew MAE | $\Delta t{=}2$ rew MAE | Rew gap |
122	|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
123	| Baseline (exp\_001) | 13.49 | 27.50 | 2.04$\times$ | 0.0102 | 0.0159 | 1.56$\times$ |
124	| 008d (trained emb) | 41.31 | 53.67 | 1.30$\times$ | 0.0568 | 0.1579 | 2.78$\times$ |
125	| 008f (no emb) | 8.01 | 22.04 | 2.75$\times$ | 0.7469 | 0.7526 | 1.01$\times$ |
126	
127	Two patterns are diagnostically relevant:
128	
129	1. **Trained embedding enables differentiated but biased reward predictions.** In exp\_008d, the reward head produces sharply different predictions for $\Delta t{=}1$ vs. $\Delta t{=}2$ (reward gap 2.78$\times$), but these differentiated predictions rest on poor absolute state quality ($\Delta t{=}1$ obs MSE = 41.31, 3.1$\times$ baseline). The critic receives confident but systematically biased reward signals at $\Delta t{=}2$, fueling value overestimation.
130	
131	2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\_008f, the reward head cannot distinguish $\Delta t$ values (gap 1.01$\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\times$ baseline). Exp\_008f is therefore a *causal control* that confirms the dt\_embedding's role in overestimation, not a recommended configuration.
132	
133	**Caveat on obs gap ratios.** Exp\_008d's low obs gap ratio (1.30$\times$) is misleading---its $\Delta t{=}1$ absolute error is already 3.1$\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.
134	
135	### Mitigation: $\Delta t{=}1$ Imagination with Multi-Rate Training
136	
137	The causal analysis identifies the imagination step size---not the embedding training state or the training data composition---as the critical variable. This points to a zero-cost mitigation: retain the trained dt\_embedding and multi-rate training data, but restrict imagination rollouts to $\Delta t{=}1$.
138	
139	Exp\_008e\_v3 implements this: subsample ON (world model trains on $\Delta t \in \{1, 2\}$ data) + trained dt\_embedding + $H{=}15$, with imagination locked to $\Delta t{=}1$. At 105K steps, it achieves eval return 869.9 (exp\_008e\_v3, seed 1), 95% of baseline (exp\_001\_baseline: 915.67@105K), with NVE = 0.80$\times$ (healthy range). This is the only tested configuration that simultaneously avoids pathological overestimation, maintains full reward prediction quality, and approaches baseline performance.
140	
141	This mitigation requires no architecture changes---only a one-line modification to the imagination rollout loop. The world model still benefits from multi-rate training data, but the actor-critic is shielded from the model's inaccurate $\Delta t > 1$ predictions.
142	
143	We note two limitations of the current evidence for this mitigation: (1) the result rests on a single independent seed (seed 1; seed 2 is in progress as exp\_008e\_v3\_walker\_s2), and (2) it has been tested on a single environment (Walker Walk). Cross-seed and cross-environment validation are ongoing.
144	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "d45b63c3-16c7-45ad-9a2b-d97ba49cc775",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_90ca4b.md",
      "content": "% Method — Draft v1\n% Target: CoRL 2026\n% Status: Draft, pending Director review\n% Note: Complements experimental_setup.md (Section 4). Some overlap in\n%   diagnostic framework and factorial design is intentional—final paper\n%   may merge or redistribute content between Sections 3 and 4.\n\n# 3. Methodology\n\nWe present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \\citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \\citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.\n\n\n## 3.1 Background: DreamerV3 and Variable-Rate Imagination\n\n### World-Model Actor-Critic\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:\n\n$$h_{t+1} = f_\\theta(h_t, z_t, a_t), \\quad \\hat{z}_{t+1} \\sim p_\\theta(\\cdot \\mid h_{t+1})$$\n\nAn actor $\\pi_\\psi$ selects actions and a critic $V_\\xi$ estimates $\\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\\Delta t = 1$) and $H = 15$.\n\n### Temporal Abstraction via Variable-Rate Imagination\n\nTemporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \\citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.\n\nWe introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:\n\n**Temporal step-size embedding.** An embedding $e_{\\Delta t} \\in \\mathbb{R}^d$ conditions the RSSM transition on the step size:\n\n$$h_{t+\\Delta t} = f_\\theta(h_t, z_t, a_t, e_{\\Delta t})$$\n\nWe study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\\Delta t$ values; the untrained and removed configurations serve as controls.\n\n**Temporal subsampling.** When enabled, the replay buffer stores both $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\\Delta t{=}1$ transitions are used for world-model training.\n\n**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\\Delta t{=}1$ (standard) or $\\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.\n\n### The Delusional Critic Hypothesis\n\nWhen the RSSM predicts $\\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\\xi$ receives precise $\\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model's delusions but suboptimal in reality.\n\nWe term this the *CIVO*, drawing on Lu \\& Schuurmans \\citep{lu2018nondelusional}'s concept of delusional policies, where function approximation introduces inconsistencies in Q-learning backups. In our setting, the inconsistency is model-induced: imagined states at $\\Delta t > 1$ deviate systematically from reality, but the critic treats them as accurate. This is a distinct instantiation of the general phenomenon---the delusion source is the world model's temporal extrapolation error, not the policy's functional form.\n\n\n## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio\n\n### Motivation\n\nDistinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\\_001\\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.\n\n### Definition\n\n**Value-evaluation ratio.** At training step $k$:\n\n$$r_k = \\frac{\\bar{v}_k}{\\bar{R}_k}$$\n\nwhere $\\bar{v}_k$ is the mean predicted value across imagined states and $\\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.\n\n**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:\n\n$$\\hat{r}_k = \\frac{r_k^{\\,\\text{exp}}}{r_k^{\\,\\text{baseline}}}$$\n\nThis removes the baseline's own overshoot trend, isolating excess overestimation. In the current analysis, $r_k^{\\text{baseline}}$ is computed from a single baseline seed (exp\\_001\\_baseline, seed 1, 500K steps); we will update to the mean of seeds 1 and 2 once exp\\_009a completes.\n\n### Diagnostic Thresholds\n\nWe calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:\n\n- **$\\hat{r}_k > 1.5$ (at $k \\geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\\_embedding conditions exceed 1.5$\\times$ at 35K+ steps (exp\\_008d seed 1: 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K; exp\\_009b seed 2: 1.62$\\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\\_008f seed 1 peak: 1.02$\\times$@25K; exp\\_009c seed 2 peak: 1.26$\\times$@25K).\n\n- **$0.8 \\leq \\hat{r}_k \\leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.\n\n- **$\\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.\n\n**Temporal validity constraint.** The NVE threshold applies only at $k \\geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\\_009b at 25K shows NVE = 2.05$\\times$ and exp\\_008e\\_v3 at 25K shows NVE = 1.93$\\times$, both artifacts of the baseline's $r_{25\\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.\n\n### Properties of the NVE Metric\n\nTwo properties make NVE informative for detecting the CIVO:\n\n**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\\_008d shows NVE = 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K $\\to$ 4.12$\\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\\_008a, exp\\_008f) show stable or declining NVE trajectories.\n\n**Collapse association.** Sustained NVE $>$ 1.5$\\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\\_008d seed 1: three consecutive checkpoints above 1.5$\\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\\_009b seed 2: 1.62$\\times$@45K $\\to$ 1.41$\\times$@55K $\\to$ 0.94$\\times$@65K, declining) does not lead to collapse. This pattern is consistent with a \"point of no return\" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.\n\n\n## 3.3 Causal Analysis Protocol\n\n### Design Rationale\n\nThis is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.\n\n### Factorial Structure\n\nWe vary three factors (temporal embedding type $\\times$ subsampling $\\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \\S4 for the complete configuration matrix). Rather than filling all cells of the $3 \\times 2 \\times 2$ grid, we prioritize the comparisons most informative for causal isolation.\n\n### Causal Chain and Its Tests\n\nThe causal chain under investigation is:\n\n$$\\text{trained } e_{\\Delta t} \\;\\xrightarrow{\\text{Link 1}}\\; \\text{pathological NVE} \\;\\xrightarrow{\\text{Link 2}}\\; \\text{actor exploitation} \\;\\xrightarrow{\\text{Link 3}}\\; \\text{performance collapse}$$\n\nEach link is tested by a specific controlled comparison:\n\n**Link 1: Trained dt\\_embedding $\\to$ pathological overestimation.** The comparison between exp\\_008d (trained dt\\_embedding, $d{=}32$) and exp\\_008f (removed dt\\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\\Delta t{=}2$ imagination). Exp\\_008d exhibits accelerating NVE (1.71$\\times$@35K $\\to$ 2.09$\\times$@45K), while exp\\_008f remains in the normal range (0.73$\\times$@35K $\\to$ 0.83$\\times$@45K). This is the primary causal evidence.\n\n**Link 2: Sustained overestimation $\\to$ collapse (stochastic).** Multi-seed replication of exp\\_008d reveals that the NVE $>$ 1.5$\\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\\_008d) shows sustained NVE $>$ 1.5$\\times$ across three checkpoints and collapses; seed 2 (exp\\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to 268@105K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.\n\n**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n### Supporting Analyses\n\n**Horizon effect (C5).** Exp\\_008c ($H{=}8$) vs. exp\\_008a ($H{=}15$), both with untrained dt\\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\\_008a: 778@105K; exp\\_008c: 241@65K plateau).\n\n**Temporal distance amplification (C4).** Exp\\_006 ($\\Delta t{=}2$, peak 485@35K $\\to$ collapse) vs. exp\\_007 ($\\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\\Delta t$, consistent with compounding RSSM prediction errors. Only two $\\Delta t$ values are tested; we report the monotonic trend (dt=1 $\\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.\n\n### RSSM Fidelity Analysis\n\nTo ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\\Delta t{=}1$ vs. $\\Delta t{=}2$ across three conditions (exp\\_rssm\\_fidelity\\_analysis):\n\n| Condition | $\\Delta t{=}1$ obs MSE | $\\Delta t{=}2$ obs MSE | Obs gap | $\\Delta t{=}1$ rew MAE | $\\Delta t{=}2$ rew MAE | Rew gap |\n|-----------|:---:|:---:|:---:|:---:|:---:|:---:|\n| Baseline (exp\\_001) | 13.49 | 27.50 | 2.04$\\times$ | 0.0102 | 0.0159 | 1.56$\\times$ |\n| 008d (trained emb) | 41.31 | 53.67 | 1.30$\\times$ | 0.0568 | 0.1579 | 2.78$\\times$ |\n| 008f (no emb) | 8.01 | 22.04 | 2.75$\\times$ | 0.7469 | 0.7526 | 1.01$\\times$ |\n\nTwo patterns are diagnostically relevant:\n\n1. **Trained embedding enables differentiated but biased reward predictions.** In exp\\_008d, the reward head produces sharply different predictions for $\\Delta t{=}1$ vs. $\\Delta t{=}2$ (reward gap 2.78$\\times$), but these differentiated predictions rest on poor absolute state quality ($\\Delta t{=}1$ obs MSE = 41.31, 3.1$\\times$ baseline). The critic receives confident but systematically biased reward signals at $\\Delta t{=}2$, fueling value overestimation.\n\n2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\\_008f, the reward head cannot distinguish $\\Delta t$ values (gap 1.01$\\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\\times$ baseline). Exp\\_008f is therefore a *causal control* that confirms the dt\\_embedding's role in overestimation, not a recommended configuration.\n\n**Caveat on obs gap ratios.** Exp\\_008d's low obs gap ratio (1.30$\\times$) is misleading---its $\\Delta t{=}1$ absolute error is already 3.1$\\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.\n\n### Mitigation: $\\Delta t{=}1$ Imagination with Multi-Rate Training\n\nThe causal analysis identifies the imagination step size---not the embedding training state or the training data composition---as the critical variable. This points to a zero-cost mitigation: retain the trained dt\\_embedding and multi-rate training data, but restrict imagination rollouts to $\\Delta t{=}1$.\n\nExp\\_008e\\_v3 implements this: subsample ON (world model trains on $\\Delta t \\in \\{1, 2\\}$ data) + trained dt\\_embedding + $H{=}15$, with imagination locked to $\\Delta t{=}1$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). This is the only tested configuration that simultaneously avoids pathological overestimation, maintains full reward prediction quality, and approaches baseline performance.\n\nThis mitigation requires no architecture changes---only a one-line modification to the imagination rollout loop. The world model still benefits from multi-rate training data, but the actor-critic is shielded from the model's inaccurate $\\Delta t > 1$ predictions.\n\nWe note two limitations of the current evidence for this mitigation: (1) the result rests on a single independent seed (seed 1; seed 2 is in progress as exp\\_008e\\_v3\\_walker\\_s2), and (2) it has been tested on a single environment (Walker Walk). Cross-seed and cross-environment validation are ongoing.\n",
      "numLines": 144,
      "startLine": 1,
      "totalLines": 144
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_019MjDNELqjXsr7p6wcB871o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/018/paper/018_prewrite_two_versions.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "802638e5-b433-478d-b5f5-1279db779bd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01811RhctftxkAkJpejv45FM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17371,
      "cache_read_input_tokens": 23480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17371
      },
      "output_tokens": 35,
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

_source line 15 · 2026-05-16T16:26:28.490Z_

<details><summary>↩ Tool result · `toolu_019MjDNELqjXsr7p6wcB871o`</summary>

````text
1	# Exp\_018 Full-SGS Pre-Written Paragraphs (Two Versions)
2	
3	**Status:** Pre-written before results. Pick Version A or B based on actual 018 outcome.
4	
5	**Decision criteria:**
6	- eval ≥ 500, NVE < 1.5× in 35K+ window → **Version A** (CIVO eliminated)
7	- eval < 300, NVE > 1.5× → **Version B** (CIVO persists)
8	- eval 300–500 or NVE 1.3–1.7× → **Version C** (partial effect, ambiguous zone)
9	
10	---
11	
12	## Version A: CIVO Disappears (Gradient-Level Vulnerability)
13	
14	### analysis.tex §5.3.5 — Full-Pathway Gradient Stopping Eliminates CIVO
15	
16	```latex
17	\paragraph{Full-pathway SGS eliminates CIVO.}
18	The gradient decomposition in Table~\ref{tab:gradient_decomposition} reveals that
19	observation decoders contribute 92.7\% of all gradients flowing into the temporal
20	embedding $e_{\Delta t}$, with KL dynamics accounting for 7.3\% and the reward head
21	contributing exactly zero. Exp\_016e (reward-only SGS) confirmed this decomposition
22	empirically: detaching the reward pathway---a \emph{null intervention} given the zero
23	gradient share---left CIVO entirely intact (NVE $10.42\times$;
24	\S\ref{sec:016e_reinterp}). The critical test is whether removing the dominant 92.7\%
25	observation decoder pathway suffices.
26	
27	Exp\_018 applies full-pathway SGS, detaching all non-KL gradients from $e_{\Delta t}$
28	so that only the 7.3\% KL dynamics signal remains. Under the same configuration that
29	produces catastrophic CIVO in exp\_008d (trained $e_{\Delta t}$, $d{=}32$, subsample ON,
30	$H{=}8$), exp\_018 reaches evaluation [EVAL] at 105K steps with peak NVE [NVE]$\times$
31	in the 35K+ diagnostic window---well below the $1.5\times$ CIVO threshold. This
32	directly contrasts with exp\_008d's collapse to evaluation 82.8 and NVE $4.12\times$.
33	
34	The residual 7.3\% KL gradient does not trigger CIVO within the 105K training horizon
35	tested. The KL loss $D_\mathrm{KL}(q_\phi \| p_\theta)$ constrains only the consistency
36	between posterior and prior distributions---it enforces that the transition model's
37	predictions align with encoder observations, but does not directly encode
38	observation-level temporal patterns that enable scale-dependent reward prediction bias. In contrast, observation
39	decoder gradients back-propagate reconstruction objectives across the full
40	24-dimensional proprioceptive signal, providing a rich channel through which
41	$e_{\Delta t}$ can learn $\Delta t$-specific state features that the reward head
42	subsequently exploits.
43	
44	The progression across interventions establishes a clear causal chain:
45	exp\_016e removes 0\% of $e_{\Delta t}$ gradients (no-op) $\rightarrow$ full CIVO
46	($10.42\times$); exp\_018 removes 92.7\% $\rightarrow$ no CIVO ([NVE]$\times$);
47	exp\_008f removes 100\% (no embedding) $\rightarrow$ no CIVO ($0.97\times$). The
48	observation decoder gradient pathway is necessary for CIVO
49	induction---the dominant causal factor. The complete causal mechanism is: observation decoder gradients train
50	$e_{\Delta t}$ to encode $\Delta t$-specific temporal features $\rightarrow$ the RSSM
51	develops scale-dependent state representations $\rightarrow$ the reward head produces
52	biased predictions at $\dt{>}1$ $\rightarrow$ the critic overestimates imagined returns
53	$\rightarrow$ policy exploitation triggers CIVO collapse.
54	```
55	
56	### results.tex Table 1 Row (Version A)
57	
58	```latex
59	\rowcolor{white}
60	018 & Full-SGS & trn$^\ddagger$ & ON & 8 & [EVAL]@105K & [NVE]$\times$ & Healthy \\
61	```
62	
63	> $^\ddagger$: trained $e_{\Delta t}$ ($d{=}32$) with full-pathway stop-gradient (only KL dynamics gradients retained).
64	
65	---
66	
67	## Version B: CIVO Persists (Representation-Level Vulnerability)
68	
69	### analysis.tex §5.3.5 — Full-Pathway Gradient Stopping Fails to Eliminate CIVO
70	
71	```latex
72	\paragraph{Full-pathway SGS is insufficient: CIVO operates at the representation level.}
73	Exp\_018 applies full-pathway SGS to the temporal embedding $e_{\Delta t}$, detaching
74	all gradients except the 7.3\% KL dynamics contribution
75	(Table~\ref{tab:gradient_decomposition}). This removes the dominant observation decoder
76	pathway (92.7\%) that we hypothesized as CIVO's primary transmission channel. Yet under
77	the same configuration that produces CIVO in exp\_008d (trained $e_{\Delta t}$,
78	$d{=}32$, subsample ON, $H{=}8$), exp\_018 still collapses: evaluation degrades to
79	[EVAL] at [STEP]K steps with peak NVE [NVE]$\times$ in the 35K+ window, confirming
80	sustained value overestimation above the $1.5\times$ diagnostic threshold.
81	
82	This result decisively shifts the mechanistic interpretation. The 7.3\% KL dynamics
83	gradient, though small in magnitude, is sufficient to encode harmful temporal
84	information into the RSSM state representation. The KL loss
85	$D_\mathrm{KL}(q_\phi \| p_\theta)$ constrains the transition model to predict
86	accurate state distributions conditioned on $e_{\Delta t}$---but this is precisely the
87	channel through which $\Delta t$-dependent prediction bias enters. The transition model
88	\emph{must} learn different dynamics for different temporal scales to minimize the KL
89	objective; this scale-dependent state structure then propagates to all downstream heads,
90	including reward prediction, regardless of whether observation decoder gradients flow
91	back to $e_{\Delta t}$.
92	
93	The contrast with exp\_008f is instructive: removing $e_{\Delta t}$ entirely eliminates
94	CIVO (NVE $0.97\times$, evaluation 503.0), while retaining it with only 7.3\% of
95	gradients still triggers collapse ([NVE]$\times$). The vulnerability is not proportional
96	to gradient magnitude---it is binary in the \emph{architectural capacity} to represent
97	temporal information. As long as $e_{\Delta t}$ exists and receives \emph{any} learning
98	signal, the transition model can develop $\Delta t$-conditioned dynamics that produce
99	scale-dependent reward prediction bias.
100	
101	This has direct implications for hierarchical world-model methods such as
102	THICK~\citep{gumbsch2024thick} and Hieros~\citep{mattes2024hieros} that inherently operate across
103	temporal scales. If CIVO is a representation-level phenomenon rather than a
104	gradient-pathway artifact, flat gradient stopping is fundamentally insufficient.
105	Mitigation requires architectural interventions that enforce temporal separation in the
106	state space---e.g., orthogonality constraints between temporal-scale representations,
107	information bottlenecks that prevent $\Delta t$ from influencing reward-relevant state
108	dimensions, or explicit factorization of temporal and reward-relevant features.
109	```
110	
111	### results.tex Table 1 Row (Version B)
112	
113	```latex
114	\rowcolor{gray!15}
115	018 & Full-SGS & trn$^\ddagger$ & ON & 8 & [EVAL]@[STEP]K & [NVE]$\times$ & CIVO collapse \\
116	```
117	
118	> $^\ddagger$: trained $e_{\Delta t}$ ($d{=}32$) with full-pathway stop-gradient (only KL dynamics gradients retained).
119	
120	---
121	
122	## Placeholder Substitution Guide
123	
124	When 018 results arrive, replace:
125	
126	| Placeholder | Source |
127	|-------------|--------|
128	| `[EVAL]` | Final or peak evaluation score |
129	| `[NVE]` | Peak NVE in 35K+ window |
130	| `[STEP]` | Step at which eval is reported (Version B only) |
131	
132	## Quick Reference: Control Experiments
133	
134	| Exp | Intervention | Gradient removed | NVE | Eval | Outcome |
135	|-----|-------------|-----------------|-----|------|---------|
136	| 008d | None (full trained dt_emb) | 0% | 4.12× | 82.8 | CIVO collapse |
137	| 008f | Remove dt_emb entirely | 100% | 0.97× | 503.0 | Healthy |
138	| 016e | Reward-only SGS | 0% (reward=0, no-op) | 10.42× | 31.7 | CIVO collapse |
139	| 018 | Full-SGS (obs decoder detach) | 92.7% | **TBD** | **TBD** | **TBD** |
140	
141	---
142	
143	## Version C: Partial Effect (Ambiguous Zone)
144	
145	**Applies when:** eval 300–500 or NVE 1.3–1.7× (neither clearly eliminated nor clearly persisting).
146	
147	### analysis.tex §5.3.5 — Full-Pathway Gradient Stopping Attenuates but Does Not Eliminate CIVO
148	
149	```latex
150	\paragraph{Full-pathway SGS attenuates CIVO: observation decoder gradients are the primary but not sole pathway.}
151	Exp\_018 applies full-pathway SGS, detaching all non-KL gradients from $e_{\Delta t}$
152	so that only the 7.3\% KL dynamics signal remains. Under the same configuration that
153	produces catastrophic CIVO in exp\_008d (trained $e_{\Delta t}$, $d{=}32$, subsample ON,
154	$H{=}8$), exp\_018 reaches evaluation [EVAL] at 105K steps with peak NVE [NVE]$\times$
155	in the 35K+ diagnostic window. This represents a substantial attenuation relative to
156	exp\_008d (NVE $4.12\times$, eval 82.8) but does not achieve the full protection
157	observed in exp\_008f (NVE $0.97\times$, eval 503.0).
158	
159	The partial protection indicates that the observation decoder gradient pathway is the
160	\emph{primary} contributor to CIVO---removing it reduces NVE from $4.12\times$ to
161	[NVE]$\times$---but the residual 7.3\% KL dynamics gradient retains sufficient capacity
162	to induce sub-threshold overestimation within the 105K training horizon. The KL loss
163	$D_\mathrm{KL}(q_\phi \| p_\theta)$ provides a weaker but non-negligible channel:
164	the transition model must still condition on $e_{\Delta t}$ to satisfy the KL objective,
165	encoding some degree of $\Delta t$-dependent state structure that downstream heads can
166	exploit.
167	
168	This positions the vulnerability as \emph{primarily gradient-level} (93\% contribution
169	from observation decoders) with a \emph{secondary representation-level} component (7\%
170	KL pathway). The intervention hierarchy is: reward-only SGS (0\% removed, no-op,
171	$10.42\times$) $\rightarrow$ full-pathway SGS (92.7\% removed, attenuated,
172	[NVE]$\times$) $\rightarrow$ full removal (100\%, eliminated, $0.97\times$). Complete
173	mitigation likely requires either extending the gradient barrier to include KL dynamics
174	(removing all learning signal from $e_{\Delta t}$, functionally equivalent to removal)
175	or architectural separation of temporal and reward-relevant representations.
176	```
177	
178	### results.tex Table 1 Row (Version C)
179	
180	```latex
181	\rowcolor{white}
182	018 & Full-SGS & trn$^\ddagger$ & ON & 8 & [EVAL]@105K & [NVE]$\times$ & Attenuated \\
183	```
184	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "0214fa9a-4f28-46f9-9795-53d347df520b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/018/paper/018_prewrite_two_versions.md",
      "content": "# Exp\\_018 Full-SGS Pre-Written Paragraphs (Two Versions)\n\n**Status:** Pre-written before results. Pick Version A or B based on actual 018 outcome.\n\n**Decision criteria:**\n- eval ≥ 500, NVE < 1.5× in 35K+ window → **Version A** (CIVO eliminated)\n- eval < 300, NVE > 1.5× → **Version B** (CIVO persists)\n- eval 300–500 or NVE 1.3–1.7× → **Version C** (partial effect, ambiguous zone)\n\n---\n\n## Version A: CIVO Disappears (Gradient-Level Vulnerability)\n\n### analysis.tex §5.3.5 — Full-Pathway Gradient Stopping Eliminates CIVO\n\n```latex\n\\paragraph{Full-pathway SGS eliminates CIVO.}\nThe gradient decomposition in Table~\\ref{tab:gradient_decomposition} reveals that\nobservation decoders contribute 92.7\\% of all gradients flowing into the temporal\nembedding $e_{\\Delta t}$, with KL dynamics accounting for 7.3\\% and the reward head\ncontributing exactly zero. Exp\\_016e (reward-only SGS) confirmed this decomposition\nempirically: detaching the reward pathway---a \\emph{null intervention} given the zero\ngradient share---left CIVO entirely intact (NVE $10.42\\times$;\n\\S\\ref{sec:016e_reinterp}). The critical test is whether removing the dominant 92.7\\%\nobservation decoder pathway suffices.\n\nExp\\_018 applies full-pathway SGS, detaching all non-KL gradients from $e_{\\Delta t}$\nso that only the 7.3\\% KL dynamics signal remains. Under the same configuration that\nproduces catastrophic CIVO in exp\\_008d (trained $e_{\\Delta t}$, $d{=}32$, subsample ON,\n$H{=}8$), exp\\_018 reaches evaluation [EVAL] at 105K steps with peak NVE [NVE]$\\times$\nin the 35K+ diagnostic window---well below the $1.5\\times$ CIVO threshold. This\ndirectly contrasts with exp\\_008d's collapse to evaluation 82.8 and NVE $4.12\\times$.\n\nThe residual 7.3\\% KL gradient does not trigger CIVO within the 105K training horizon\ntested. The KL loss $D_\\mathrm{KL}(q_\\phi \\| p_\\theta)$ constrains only the consistency\nbetween posterior and prior distributions---it enforces that the transition model's\npredictions align with encoder observations, but does not directly encode\nobservation-level temporal patterns that enable scale-dependent reward prediction bias. In contrast, observation\ndecoder gradients back-propagate reconstruction objectives across the full\n24-dimensional proprioceptive signal, providing a rich channel through which\n$e_{\\Delta t}$ can learn $\\Delta t$-specific state features that the reward head\nsubsequently exploits.\n\nThe progression across interventions establishes a clear causal chain:\nexp\\_016e removes 0\\% of $e_{\\Delta t}$ gradients (no-op) $\\rightarrow$ full CIVO\n($10.42\\times$); exp\\_018 removes 92.7\\% $\\rightarrow$ no CIVO ([NVE]$\\times$);\nexp\\_008f removes 100\\% (no embedding) $\\rightarrow$ no CIVO ($0.97\\times$). The\nobservation decoder gradient pathway is necessary for CIVO\ninduction---the dominant causal factor. The complete causal mechanism is: observation decoder gradients train\n$e_{\\Delta t}$ to encode $\\Delta t$-specific temporal features $\\rightarrow$ the RSSM\ndevelops scale-dependent state representations $\\rightarrow$ the reward head produces\nbiased predictions at $\\dt{>}1$ $\\rightarrow$ the critic overestimates imagined returns\n$\\rightarrow$ policy exploitation triggers CIVO collapse.\n```\n\n### results.tex Table 1 Row (Version A)\n\n```latex\n\\rowcolor{white}\n018 & Full-SGS & trn$^\\ddagger$ & ON & 8 & [EVAL]@105K & [NVE]$\\times$ & Healthy \\\\\n```\n\n> $^\\ddagger$: trained $e_{\\Delta t}$ ($d{=}32$) with full-pathway stop-gradient (only KL dynamics gradients retained).\n\n---\n\n## Version B: CIVO Persists (Representation-Level Vulnerability)\n\n### analysis.tex §5.3.5 — Full-Pathway Gradient Stopping Fails to Eliminate CIVO\n\n```latex\n\\paragraph{Full-pathway SGS is insufficient: CIVO operates at the representation level.}\nExp\\_018 applies full-pathway SGS to the temporal embedding $e_{\\Delta t}$, detaching\nall gradients except the 7.3\\% KL dynamics contribution\n(Table~\\ref{tab:gradient_decomposition}). This removes the dominant observation decoder\npathway (92.7\\%) that we hypothesized as CIVO's primary transmission channel. Yet under\nthe same configuration that produces CIVO in exp\\_008d (trained $e_{\\Delta t}$,\n$d{=}32$, subsample ON, $H{=}8$), exp\\_018 still collapses: evaluation degrades to\n[EVAL] at [STEP]K steps with peak NVE [NVE]$\\times$ in the 35K+ window, confirming\nsustained value overestimation above the $1.5\\times$ diagnostic threshold.\n\nThis result decisively shifts the mechanistic interpretation. The 7.3\\% KL dynamics\ngradient, though small in magnitude, is sufficient to encode harmful temporal\ninformation into the RSSM state representation. The KL loss\n$D_\\mathrm{KL}(q_\\phi \\| p_\\theta)$ constrains the transition model to predict\naccurate state distributions conditioned on $e_{\\Delta t}$---but this is precisely the\nchannel through which $\\Delta t$-dependent prediction bias enters. The transition model\n\\emph{must} learn different dynamics for different temporal scales to minimize the KL\nobjective; this scale-dependent state structure then propagates to all downstream heads,\nincluding reward prediction, regardless of whether observation decoder gradients flow\nback to $e_{\\Delta t}$.\n\nThe contrast with exp\\_008f is instructive: removing $e_{\\Delta t}$ entirely eliminates\nCIVO (NVE $0.97\\times$, evaluation 503.0), while retaining it with only 7.3\\% of\ngradients still triggers collapse ([NVE]$\\times$). The vulnerability is not proportional\nto gradient magnitude---it is binary in the \\emph{architectural capacity} to represent\ntemporal information. As long as $e_{\\Delta t}$ exists and receives \\emph{any} learning\nsignal, the transition model can develop $\\Delta t$-conditioned dynamics that produce\nscale-dependent reward prediction bias.\n\nThis has direct implications for hierarchical world-model methods such as\nTHICK~\\citep{gumbsch2024thick} and Hieros~\\citep{mattes2024hieros} that inherently operate across\ntemporal scales. If CIVO is a representation-level phenomenon rather than a\ngradient-pathway artifact, flat gradient stopping is fundamentally insufficient.\nMitigation requires architectural interventions that enforce temporal separation in the\nstate space---e.g., orthogonality constraints between temporal-scale representations,\ninformation bottlenecks that prevent $\\Delta t$ from influencing reward-relevant state\ndimensions, or explicit factorization of temporal and reward-relevant features.\n```\n\n### results.tex Table 1 Row (Version B)\n\n```latex\n\\rowcolor{gray!15}\n018 & Full-SGS & trn$^\\ddagger$ & ON & 8 & [EVAL]@[STEP]K & [NVE]$\\times$ & CIVO collapse \\\\\n```\n\n> $^\\ddagger$: trained $e_{\\Delta t}$ ($d{=}32$) with full-pathway stop-gradient (only KL dynamics gradients retained).\n\n---\n\n## Placeholder Substitution Guide\n\nWhen 018 results arrive, replace:\n\n| Placeholder | Source |\n|-------------|--------|\n| `[EVAL]` | Final or peak evaluation score |\n| `[NVE]` | Peak NVE in 35K+ window |\n| `[STEP]` | Step at which eval is reported (Version B only) |\n\n## Quick Reference: Control Experiments\n\n| Exp | Intervention | Gradient removed | NVE | Eval | Outcome |\n|-----|-------------|-----------------|-----|------|---------|\n| 008d | None (full trained dt_emb) | 0% | 4.12× | 82.8 | CIVO collapse |\n| 008f | Remove dt_emb entirely | 100% | 0.97× | 503.0 | Healthy |\n| 016e | Reward-only SGS | 0% (reward=0, no-op) | 10.42× | 31.7 | CIVO collapse |\n| 018 | Full-SGS (obs decoder detach) | 92.7% | **TBD** | **TBD** | **TBD** |\n\n---\n\n## Version C: Partial Effect (Ambiguous Zone)\n\n**Applies when:** eval 300–500 or NVE 1.3–1.7× (neither clearly eliminated nor clearly persisting).\n\n### analysis.tex §5.3.5 — Full-Pathway Gradient Stopping Attenuates but Does Not Eliminate CIVO\n\n```latex\n\\paragraph{Full-pathway SGS attenuates CIVO: observation decoder gradients are the primary but not sole pathway.}\nExp\\_018 applies full-pathway SGS, detaching all non-KL gradients from $e_{\\Delta t}$\nso that only the 7.3\\% KL dynamics signal remains. Under the same configuration that\nproduces catastrophic CIVO in exp\\_008d (trained $e_{\\Delta t}$, $d{=}32$, subsample ON,\n$H{=}8$), exp\\_018 reaches evaluation [EVAL] at 105K steps with peak NVE [NVE]$\\times$\nin the 35K+ diagnostic window. This represents a substantial attenuation relative to\nexp\\_008d (NVE $4.12\\times$, eval 82.8) but does not achieve the full protection\nobserved in exp\\_008f (NVE $0.97\\times$, eval 503.0).\n\nThe partial protection indicates that the observation decoder gradient pathway is the\n\\emph{primary} contributor to CIVO---removing it reduces NVE from $4.12\\times$ to\n[NVE]$\\times$---but the residual 7.3\\% KL dynamics gradient retains sufficient capacity\nto induce sub-threshold overestimation within the 105K training horizon. The KL loss\n$D_\\mathrm{KL}(q_\\phi \\| p_\\theta)$ provides a weaker but non-negligible channel:\nthe transition model must still condition on $e_{\\Delta t}$ to satisfy the KL objective,\nencoding some degree of $\\Delta t$-dependent state structure that downstream heads can\nexploit.\n\nThis positions the vulnerability as \\emph{primarily gradient-level} (93\\% contribution\nfrom observation decoders) with a \\emph{secondary representation-level} component (7\\%\nKL pathway). The intervention hierarchy is: reward-only SGS (0\\% removed, no-op,\n$10.42\\times$) $\\rightarrow$ full-pathway SGS (92.7\\% removed, attenuated,\n[NVE]$\\times$) $\\rightarrow$ full removal (100\\%, eliminated, $0.97\\times$). Complete\nmitigation likely requires either extending the gradient barrier to include KL dynamics\n(removing all learning signal from $e_{\\Delta t}$, functionally equivalent to removal)\nor architectural separation of temporal and reward-relevant representations.\n```\n\n### results.tex Table 1 Row (Version C)\n\n```latex\n\\rowcolor{white}\n018 & Full-SGS & trn$^\\ddagger$ & ON & 8 & [EVAL]@105K & [NVE]$\\times$ & Attenuated \\\\\n```\n",
      "numLines": 184,
      "startLine": 1,
      "totalLines": 184
    }
  }
}
````

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have all five files. Let me analyze each one for overly strong claims containing "necessary and sufficient", "always", "inevitably", "guarantees", and similar language.

Let me go through each file:

**1. results.md**

- Line 34: "the qualitative conclusion is uniform" — mild, not overly strong
- Line 52: "isolates the temporal embedding as the causal factor" — this is okay, it's specific about what the factorial structure shows
- Line 73: "The trained embedding reliably induces pathological value overestimation" — "reliably" is okay given 2/2 seeds


- Line 159: "Subsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO." — This is actually fine since it's a negative claim saying these factors aren't necessary or sufficient, implying the trained dt_emb is the key factor
- Line 193: "strategies targeting the reward pathway alone address <1% of the gradient flow and cannot attenuate CIVO." — The "cannot" here is strong, but it's grounded in the quantitative finding about gradient flow
- Line 196: "definitively rules out reward-pathway interventions" — "definitively" is a strong word that might overstate the case

Now I'm scanning through the other files for similar language patterns. In method_framingB_reaudit_v2.md, I see "Trained dt_embedding is the necessary condition for sustained" — this is another necessary/sufficient claim I need to evaluate in context. Now I'm scanning through the remaining files for problematic necessity-and-sufficiency language. In results.md, I found a statement saying something "is neither necessary nor sufficient" which is actually fine—that's a valid logical claim. Let me continue checking the other documents more systematically for any overreaching causal language. I'm realizing there's a factual error in the original statement — the data actually shows subsample is necessary for CIVO, not neither necessary nor sufficient. Looking at the experiments, subsample ON is required alongside trained dt_emb to achieve CIVO, while subsample OFF (exp_008a) prevents it entirely. So the claim needs to be corrected to reflect that subsample is necessary but not sufficient. the project's own understanding! It should say something like "not independently sufficient" but it IS necessary.

Looking back at the experimental results, exp_008e_v3 with subsample ON but $\Delta t=1$ imagination achieves 869.9 at 105K—95% of baseline—so subsample alone doesn't trigger CIVO. But the factorial design is clear: without subsample (exp_008a with trained dt_emb and subsample OFF), CIVO never occurs, which means subsample is actually a necessary condition, not optional.

I think the paper's Finding 5 might be reframing this as "subsampling alone is insufficient" and "horizon alone doesn't trigger CIVO," but the claim that it's "neither necessary nor sufficient" is the real problem. Now I'm scanning through the results for overly strong language—words like "always," "inevitably," or "guarantees"—and checking them against the experimental evidence. The "reliably induces" and "reliable trigger" claims seem defensible with 2/2 seeds on Walker, and "cannot attenuate CIVO" logically follows from the zero gradient observation, but I need to verify the rest of the strong claims.

Looking at the method framing document, I'm noticing some contradictions. The statement that "the trained embedding itself is not harmful" conflicts with the paper's own findings about IRD—seed 2 of 008e_v3 shows the embedding can cause harm through non-CIVO pathways even at dt=1. Similarly, calling the trained embedding "the necessary condition" for sustained CIVO oversimplifies when the task context clearly shows subsampling and sufficient horizon are also required components. These absolute framings need to be softened to reflect the actual joint dependencies.

Moving through the gradient analysis and method documents, I'm checking for similar overstatements. The claim about restricting imagination to dt=1 "eliminating" Pathway A is too strong based on just one seed per environment. Most other claims hold up reasonably well, though the recurring issue of treating the trained embedding as inherently harmless keeps appearing across multiple sections and needs consistent revision. Now I'm compiling all the findings into an audit report and identifying which claims need correction in the main results document and the reframed methodology version. Looking at the key issues: the claim about subsample necessity is factually wrong based on the project data, "definitively rules out" overstates the evidence, and "reliably induces" needs scrutiny given only two seeds were tested on Walker—I should verify whether that's sufficient to support the reliability claim. I'm catching some language precision issues in the remaining files—particularly around claims of "complete" causal mechanisms and binary architectural statements that need softening. Before finalizing the audit report and edits, I should double-check whether "reliably" holds up given we only have 2 seeds tested on Walker in the actual paper, even though the project context mentions additional environments. That distinction matters for how strongly I can justify the language. Looking at the constraint about single-environment results, I need to check whether the paper actually reports both Walker and Cheetah data. If it's only Walker, then "reliably" is too strong without that multi-environment support, even though the sentence already acknowledges the stochasticity of collapse. I should flag this as a potential issue depending on what environments are actually reported.

Now I'm systematically searching through the documents for absolute language like "always," "inevitably," or "guarantees" that might overstate the findings. So far the documents look clean on this front—no problematic uses of these terms in claim contexts.

I'm also flagging "The complete causal mechanism" in the prewrite as implying more certainty than warranted. And I notice the "first backward-pass decomposition" claim in results.md, though that's a novelty claim rather than a necessity/sufficiency claim, so it's outside the scope of this audit.

The key finding so far is that "neither necessary nor sufficient for CIVO" appears only once in line 159 of results.md, which is the only explicit statement of this kind I can find across the documents.

Now I'm moving into the editing phase. I need to address the overly strong language in both files: the "neither necessary nor sufficient" claim and "definitively rules out" in results.md, plus several instances in method_framingB_reaudit_v2.md where I'm making absolute claims about necessity or harmfulness that should be qualified. Let me start drafting the specific revisions.

For the results.md edit on line 159, I'm reconsidering the claim about subsampling and imagination horizon. Looking back at the experiments, the trained embedding plus subsampling plus sufficient horizon together form the joint trigger condition, but I need to be precise about what's actually necessary versus what's just part of the pattern. The horizon requirement isn't cleanly defined—there's a minimum threshold but it's not sharply bounded—so I should frame this as a joint requirement rather than claiming each factor is independently necessary. I'm refining the language around subsampling and imagination horizon—subsampling is actually necessary for CIVO to emerge, but horizon alone doesn't trigger it, just affects performance ceiling. So I need to rewrite that opening claim to be more precise. For the results section, I'm also tightening up the phrasing about the reward gradient finding to make it clearer and more concise. A trained dt_embedding is necessary for sustained CIVO, but it's not sufficient on its own—multi-rate training data exposure is also required. Now I'm applying these refinements across the document, including a parallel edit at line 187 that clarifies the same distinction about when the embedding becomes problematic during imagination.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "7fed0023-d4ec-4c80-b046-15251fab24cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEubfG28au4APwt8djdfwn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8640,
      "cache_read_input_tokens": 40851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8640
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

_source line 17_

文件已全部读取。开始整理过强 claim 并生成审计报告和修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "4a76fe0e-e148-456a-aeba-0d901843ca24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEubfG28au4APwt8djdfwn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8640,
      "cache_read_input_tokens": 40851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8640
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

_source line 18_

<details open><summary>🔧 Tool call — Write · `toolu_01NGecLTh7ffC8HoyxNyJimn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/claim_audit_report.md",
  "content": "# Claim Language Audit Report\n\n**Purpose:** Ensure all claims align with the empirical evidence: trained dt_emb is a necessary (not sufficient) condition for CIVO; triggering requires subsample ON + dt>1 imagination; collapse probability is environment-dependent.\n\n---\n\n## Findings\n\n### [CRITICAL] results.md line 159 — Factually incorrect necessity claim\n\n**Original:**\n> Subsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO.\n\n**Problem:** Subsample ON IS necessary for CIVO (exp_008a: trained dt_emb + subsample OFF → no CIVO). Saying it's \"neither necessary\" contradicts the paper's own factorial data.\n\n**Suggested fix:**\n> Subsampling is a necessary co-factor for CIVO but not independently sufficient; imagination horizon modulates performance level without independently triggering overestimation.\n\n---\n\n### [HIGH] method_framingB_reaudit_v2.md line 111 — Overly absolute \"not harmful\"\n\n**Original:**\n> The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n**Problem:** The paper's own IRD finding (exp_008e_v3_s2) shows that the trained embedding CAN cause collapse even at dt=1 imagination through a non-CIVO pathway. \"Not harmful\" is an unqualified absolute.\n\n**Suggested fix:**\n> The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises specifically when the actor-critic exploits the embedding's $\\Delta t > 1$ predictions during imagination.\n\n---\n\n### [HIGH] method_framingB_reaudit_v2.md line 124 — \"The necessary condition\" implies sole sufficiency\n\n**Original:**\n> Trained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints).\n\n**Problem:** Using \"the necessary condition\" (definite article, singular) implies it's the only required factor. Multi-rate data exposure is also required (exp_008a proves this).\n\n**Suggested fix:**\n> A trained dt\\_embedding is necessary for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints), though not independently sufficient---multi-rate training data exposure is jointly required.\n\n---\n\n### [HIGH] method_framingB_reaudit_v2.md line 187 — Repeated \"not harmful\" absolute\n\n**Original:**\n> The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n**Problem:** Same as line 111. Contradicted by IRD pathway.\n\n**Suggested fix:**\n> The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n---\n\n### [MEDIUM] results.md line 196 — \"definitively rules out\"\n\n**Original:**\n> our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.\n\n**Problem:** \"Definitively\" overstates certainty. The measurement is at one checkpoint (95K) in one configuration. While the architectural argument is strong, \"definitively\" implies mathematical proof.\n\n**Suggested fix:**\n> our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result, ruling out reward-pathway interventions for this architecture.\n\n---\n\n### [MEDIUM] 018_prewrite_two_versions.md line 53 — \"The complete causal mechanism\"\n\n**Original (Version A):**\n> The complete causal mechanism is: observation decoder gradients train $e_{\\Delta t}$...\n\n**Problem:** \"Complete\" implies no unknown factors. With only 2 seeds on 2 envs, the mechanism may have additional factors not yet observed.\n\n**Suggested fix:**\n> The identified causal mechanism is: observation decoder gradients train $e_{\\Delta t}$...\n\n---\n\n### [LOW] method_90ca4b.md line 109 — \"not harmful\" (same pattern)\n\n**Original:**\n> The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n**Problem:** Same absolute claim as in framingB. This is an older draft version so lower priority.\n\n**Suggested fix:** Same as framingB line 111.\n\n---\n\n### [LOW] results.md line 73 — \"reliably induces\" in single-env context\n\n**Original:**\n> The trained embedding reliably induces pathological value overestimation, though whether this overestimation progresses to catastrophic collapse is stochastic.\n\n**Problem:** \"Reliably\" based on 2/2 seeds in one environment. The subsequent clause about stochastic collapse is correct, and the NVE evidence supports high trigger probability. Borderline acceptable.\n\n**Suggested fix (optional):**\n> The trained embedding triggers pathological value overestimation in all tested seeds (2/2), though whether this overestimation progresses to catastrophic collapse is stochastic.\n\n---\n\n## Summary\n\n| Severity | Count | Files affected |\n|----------|-------|----------------|\n| CRITICAL | 1 | results.md |\n| HIGH | 3 | method_framingB_reaudit_v2.md |\n| MEDIUM | 2 | results.md, 018_prewrite_two_versions.md |\n| LOW | 2 | method_90ca4b.md, results.md |\n\n**Total: 8 overly strong claims found.**\n\nKey patterns:\n1. **Incorrect \"neither necessary nor sufficient\"** — subsample IS necessary per factorial data (1 instance)\n2. **Unqualified \"not harmful\" absolutes** — contradicted by the paper's own IRD finding (3 instances)\n3. **\"Definitively\"/\"complete\" certainty language** — overstates evidence from limited seeds/envs (2 instances)\n4. **\"The necessary condition\" (sole)** — implies independent sufficiency (1 instance)\n\nAll CRITICAL and HIGH findings are directly edited in results.md and method_framingB_reaudit_v2.md.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "c922a96a-e8d2-48ee-9292-1acea727562e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEubfG28au4APwt8djdfwn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8640,
      "cache_read_input_tokens": 40851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8640
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

_source line 19 · 2026-05-16T16:28:45.267Z_

<details><summary>↩ Tool result · `toolu_01NGecLTh7ffC8HoyxNyJimn`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/claim_audit_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "b9a7490b-9867-4f07-a050-870b35bb80ac",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/claim_audit_report.md",
    "content": "# Claim Language Audit Report\n\n**Purpose:** Ensure all claims align with the empirical evidence: trained dt_emb is a necessary (not sufficient) condition for CIVO; triggering requires subsample ON + dt>1 imagination; collapse probability is environment-dependent.\n\n---\n\n## Findings\n\n### [CRITICAL] results.md line 159 — Factually incorrect necessity claim\n\n**Original:**\n> Subsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO.\n\n**Problem:** Subsample ON IS necessary for CIVO (exp_008a: trained dt_emb + subsample OFF → no CIVO). Saying it's \"neither necessary\" contradicts the paper's own factorial data.\n\n**Suggested fix:**\n> Subsampling is a necessary co-factor for CIVO but not independently sufficient; imagination horizon modulates performance level without independently triggering overestimation.\n\n---\n\n### [HIGH] method_framingB_reaudit_v2.md line 111 — Overly absolute \"not harmful\"\n\n**Original:**\n> The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n**Problem:** The paper's own IRD finding (exp_008e_v3_s2) shows that the trained embedding CAN cause collapse even at dt=1 imagination through a non-CIVO pathway. \"Not harmful\" is an unqualified absolute.\n\n**Suggested fix:**\n> The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises specifically when the actor-critic exploits the embedding's $\\Delta t > 1$ predictions during imagination.\n\n---\n\n### [HIGH] method_framingB_reaudit_v2.md line 124 — \"The necessary condition\" implies sole sufficiency\n\n**Original:**\n> Trained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints).\n\n**Problem:** Using \"the necessary condition\" (definite article, singular) implies it's the only required factor. Multi-rate data exposure is also required (exp_008a proves this).\n\n**Suggested fix:**\n> A trained dt\\_embedding is necessary for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints), though not independently sufficient---multi-rate training data exposure is jointly required.\n\n---\n\n### [HIGH] method_framingB_reaudit_v2.md line 187 — Repeated \"not harmful\" absolute\n\n**Original:**\n> The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n**Problem:** Same as line 111. Contradicted by IRD pathway.\n\n**Suggested fix:**\n> The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n---\n\n### [MEDIUM] results.md line 196 — \"definitively rules out\"\n\n**Original:**\n> our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.\n\n**Problem:** \"Definitively\" overstates certainty. The measurement is at one checkpoint (95K) in one configuration. While the architectural argument is strong, \"definitively\" implies mathematical proof.\n\n**Suggested fix:**\n> our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result, ruling out reward-pathway interventions for this architecture.\n\n---\n\n### [MEDIUM] 018_prewrite_two_versions.md line 53 — \"The complete causal mechanism\"\n\n**Original (Version A):**\n> The complete causal mechanism is: observation decoder gradients train $e_{\\Delta t}$...\n\n**Problem:** \"Complete\" implies no unknown factors. With only 2 seeds on 2 envs, the mechanism may have additional factors not yet observed.\n\n**Suggested fix:**\n> The identified causal mechanism is: observation decoder gradients train $e_{\\Delta t}$...\n\n---\n\n### [LOW] method_90ca4b.md line 109 — \"not harmful\" (same pattern)\n\n**Original:**\n> The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n**Problem:** Same absolute claim as in framingB. This is an older draft version so lower priority.\n\n**Suggested fix:** Same as framingB line 111.\n\n---\n\n### [LOW] results.md line 73 — \"reliably induces\" in single-env context\n\n**Original:**\n> The trained embedding reliably induces pathological value overestimation, though whether this overestimation progresses to catastrophic collapse is stochastic.\n\n**Problem:** \"Reliably\" based on 2/2 seeds in one environment. The subsequent clause about stochastic collapse is correct, and the NVE evidence supports high trigger probability. Borderline acceptable.\n\n**Suggested fix (optional):**\n> The trained embedding triggers pathological value overestimation in all tested seeds (2/2), though whether this overestimation progresses to catastrophic collapse is stochastic.\n\n---\n\n## Summary\n\n| Severity | Count | Files affected |\n|----------|-------|----------------|\n| CRITICAL | 1 | results.md |\n| HIGH | 3 | method_framingB_reaudit_v2.md |\n| MEDIUM | 2 | results.md, 018_prewrite_two_versions.md |\n| LOW | 2 | method_90ca4b.md, results.md |\n\n**Total: 8 overly strong claims found.**\n\nKey patterns:\n1. **Incorrect \"neither necessary nor sufficient\"** — subsample IS necessary per factorial data (1 instance)\n2. **Unqualified \"not harmful\" absolutes** — contradicted by the paper's own IRD finding (3 instances)\n3. **\"Definitively\"/\"complete\" certainty language** — overstates evidence from limited seeds/envs (2 instances)\n4. **\"The necessary condition\" (sole)** — implies independent sufficiency (1 instance)\n\nAll CRITICAL and HIGH findings are directly edited in results.md and method_framingB_reaudit_v2.md.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 20_

Now applying edits to results.md and method_framingB_reaudit_v2.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "422249b0-dae4-42b5-a93d-248feed293c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V54jiNVxjBmLXbjUEkzwbF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7082,
      "cache_read_input_tokens": 49491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7082
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01RFt79CsuMaaHvwg8Xuo8Wd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results.md",
  "old_string": "Subsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO.",
  "new_string": "Subsampling is a necessary co-factor for CIVO but not independently sufficient; imagination horizon modulates performance level without independently triggering overestimation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "837f2e36-85a5-48f0-a497-be53e7c9a3c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V54jiNVxjBmLXbjUEkzwbF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7082,
      "cache_read_input_tokens": 49491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7082
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

_source line 22 · 2026-05-16T16:28:51.342Z_

<details><summary>↩ Tool result · `toolu_01RFt79CsuMaaHvwg8Xuo8Wd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "a2a14f96-7205-45ab-b15e-c681a81b188d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results.md",
    "oldString": "Subsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO.",
    "newString": "Subsampling is a necessary co-factor for CIVO but not independently sufficient; imagination horizon modulates performance level without independently triggering overestimation.",
    "originalFile": "% Results Section — Draft v1\n% Target: CoRL 2026\n% Status: Draft, pending Director review\n% Writing order: 1 (anchors all other sections)\n\n\\section{Results}\n\\label{sec:results}\n\nWe organize findings around five diagnostic questions, followed by a gradient decomposition analysis and a taxonomy of failure modes. All quantitative claims cite experiment identifiers for traceability; evaluation returns are means over 10 episodes at each checkpoint. Experiments use Walker Walk from the DeepMind Control Suite (see Section~\\ref{sec:environment}).\n\n% ============================================================\n% F1: ALL DT>1 DEGRADE\n% ============================================================\n\n\\subsection{Finding 1: All Variable-Rate Configurations Degrade Performance}\n\\label{sec:f1}\n\n\\begin{figure}[t]\n  \\centering\n  % PLACEHOLDER: Learning curves for exp_001, 005, 006, 007\n  \\includegraphics[width=\\linewidth]{figures/fig1_learning_curves.pdf}\n  \\caption{Learning curves for all primary configurations. The \\mbox{$\\Delta t{=}1$} baseline (exp\\_001) converges to ${\\sim}950$; every $\\Delta t{>}1$ variant degrades or collapses.}\n  \\label{fig:learning_curves}\n\\end{figure}\n\nEvery tested variable-rate imagination configuration degrades asymptotic performance relative to the standard $\\Delta t{=}1$ baseline. The baseline (exp\\_001, seed~1) reaches 915.7 at 105K steps and converges to ${\\sim}950$ asymptotically (peak 970.4 at 505K). In contrast:\n\n\\begin{itemize}\n    \\item \\textbf{Learned gate} (exp\\_005): peaks at 541.2 at 55K, then declines to 98.8 by 145K---a 90\\% drop from peak.\n    \\item \\textbf{Fixed $\\Delta t{=}2$} (exp\\_006, $H{=}15$): peaks at 485.3 at 35K, then collapses to 132.9 by 65K as the value/eval ratio accelerates from 31\\% to 272\\%.\n    \\item \\textbf{Fixed $\\Delta t{=}4$} (exp\\_007, $H{=}15$): peaks at 176.9 at 25K and plateaus around 144--152, never exceeding 19\\% of the baseline's asymptotic level.\n\\end{itemize}\n\nNo $\\Delta t{>}1$ configuration achieves sustained performance above 60\\% of the baseline beyond 65K steps. The degradation patterns vary---inverted-V collapse (exp\\_006), monotonic decline (exp\\_005), and severe suppression (exp\\_007)---but the qualitative conclusion is uniform: variable-rate imagination degrades performance on Walker Walk across all tested configurations.\n\n\n% ============================================================\n% F2: TRAINED DT_EMB → CIVO\n% ============================================================\n\n\\subsection{Finding 2: Trained Temporal Embedding Reliably Triggers Pathological Value Overestimation}\n\\label{sec:f2}\n\n\\begin{figure}[t]\n  \\centering\n  % PLACEHOLDER: NVE trajectories with 1.5x threshold\n  \\includegraphics[width=\\linewidth]{figures/fig2_nve_trajectories.pdf}\n  \\caption{Normalized value/eval ratio (NVE) trajectories. Dashed line: $1.5\\times$ pathological threshold (applied at $k \\geq 35\\text{K}$). Both trained-$e_{\\Delta t}$ seeds exceed the threshold; neither removed-$e_{\\Delta t}$ seed does.}\n  \\label{fig:nve_trajectories}\n\\end{figure}\n\nThe controlled comparison between exp\\_008d (trained $e_{\\Delta t}$, subsample \\textsc{on}, $H{=}8$) and exp\\_008f ($e_{\\Delta t}$ removed, subsample \\textsc{on}, $H{=}8$) isolates the temporal embedding as the causal factor for conditioning-induced value overestimation (CIVO). These experiments share identical configurations except for the presence of the trained temporal embedding.\n\n\\paragraph{Diagnostic threshold.} Using the normalized value/eval ratio (NVE; see Section~\\ref{sec:diagnostic}), the $\\hat{r}_k > 1.5$ threshold at steps $\\geq$35K achieves 4/4 classification accuracy across seeds:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NVE diagnostic: trained vs.\\ removed temporal embedding. Peak NVE reported at steps $\\geq$35K where baseline $r_k > 0.24$ ensures ratio stability.}\n\\label{tab:nve_separation}\n\\begin{tabular}{llcc}\n\\toprule\nCondition & Seed & Peak NVE ($\\geq$35K) & $>$1.5$\\times$? \\\\\n\\midrule\nTrained $e_{\\Delta t}$ (exp\\_008d) & 1 & 2.09$\\times$ @ 45K & \\textbf{Yes} \\\\\nTrained $e_{\\Delta t}$ (exp\\_009b) & 2 & 1.62$\\times$ @ 45K & \\textbf{Yes} \\\\\nRemoved $e_{\\Delta t}$ (exp\\_008f) & 1 & 0.97$\\times$ @ 55K & No \\\\\nRemoved $e_{\\Delta t}$ (exp\\_009c) & 2 & 1.14$\\times$ @ 105K & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth trained-$e_{\\Delta t}$ seeds exceed the pathological threshold; neither removed-$e_{\\Delta t}$ seed does. The trained embedding reliably induces pathological value overestimation, though whether this overestimation progresses to catastrophic collapse is stochastic (see below).\n\n\\paragraph{Causal isolation.} The factorial structure establishes that CIVO requires the combination of a \\textit{trained} temporal embedding and exposure to multi-rate training data:\n\n\\begin{figure}[h]\n  \\centering\n  % PLACEHOLDER: 2×2 factorial grid summary\n  \\includegraphics[width=0.85\\linewidth]{figures/fig3_factorial_grid.pdf}\n  \\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\Delta t}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n  \\label{fig:factorial_grid}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\Delta t}$ configuration $\\times$ multi-rate data exposure. All treatment conditions use $\\Delta t{=}2$ imagination and $H{=}8$ (except exp\\_008a: $H{=}15$).}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\Delta t}$ & exp\\_008d: CIVO & exp\\_008a: healthy \\\\\n & NVE 2.09$\\times$, collapse & NVE 0.59--0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\Delta t}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.39--0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\Delta t}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\Delta t{>}1$ transitions during world-model training (subsample \\textsc{off}). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the 0.59--0.93$\\times$ range across 105K steps (exp\\_008a). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\Delta t{>}1$ state predictions within the RSSM.\n\n\\paragraph{Post-CIVO outcomes: seed-dependent trajectories.} The 008d configuration was run with two independent seeds, producing qualitatively distinct outcomes:\n\n\\begin{enumerate}\n    \\item \\textbf{Seed~1} (exp\\_008d / exp\\_009e): CIVO onset at 25K (NVE 1.78$\\times$), eval declines from 167.2 to 82.8 by 55K (exp\\_008d). Extended to 105K (exp\\_009e), the run shows oscillatory degradation: a transient bounce to 250 at 65K, but actor loss flips positive ($+$0.011 at 85K, exp\\_009e), signaling permanent actor damage. Eval oscillates between 131 and 250 without sustained recovery, ending at 131.1 at 105K (exp\\_009e).\n    \\item \\textbf{Seed~2} (exp\\_009b): transient NVE of 1.62$\\times$ at 45K, followed by self-correction---NVE declines monotonically from 1.62$\\times$ to 0.38$\\times$ between 45K and 105K. Value peaks at 110.9 at 65K then self-corrects to 67.3 by 105K, while eval rises from 141.0 to a peak of 278.5 at 95K (exp\\_009b).\n\\end{enumerate}\n\nBoth seeds cross the NVE~$>$~1.5$\\times$ threshold, confirming the trained embedding as a reliable trigger. The downstream trajectory depends on whether overestimation is sustained across consecutive checkpoints (seed~1: $1.71\\times \\to 2.09\\times \\to 4.12\\times$ at 35--55K, locking in the positive feedback loop) or transient (seed~2: $1.62\\times$ at 45K $\\to$ $1.41\\times$ at 55K, declining).\n\n\n% ============================================================\n% F3: UNTRAINED DT_EMB → PROTECTION\n% ============================================================\n\n\\subsection{Finding 3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\nExp\\_008a (trained-but-unexposed $e_{\\Delta t}$,\\footnote{Exp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\Delta t{>}1$ data due to subsample \\textsc{off}; it is not frozen or absent. See Table~\\ref{tab:factorial}.} subsample \\textsc{off}, $H{=}15$) demonstrates sustained value growth suppression over 105K steps. Its NVE ranges from 0.59$\\times$ to 0.93$\\times$ across the 55K--105K window (exp\\_008a), diverging further \\textit{below} baseline levels over time rather than converging toward them.\n\nPerformance follows two complete V-shaped recovery cycles: $500.8 \\to 563.4 \\to 487.9 \\to 608.0 \\to 469.9 \\to 583.7 \\to 572.2 \\to 777.7$ over 35K--105K (exp\\_008a). The final evaluation of 777.7 at 105K reaches 85\\% of the baseline at the same step (915.7, exp\\_001), with no collapse through 112K training steps.\n\nThis contrasts sharply with exp\\_006 (trained $e_{\\Delta t}$, subsample \\textsc{on}, $H{=}15$), where NVE accelerates from 1.61$\\times$ at 45K to 2.31$\\times$ at 55K before catastrophic collapse to 132.9 at 65K (exp\\_006). The 006-vs-008a comparison corroborates the causal role of multi-rate data exposure: both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\Delta t{>}1$ transitions during training.\n\n\n% ============================================================\n% F4: DT AMPLIFICATION\n% ============================================================\n\n\\subsection{Finding 4: Longer Temporal Gaps Amplify Degradation}\n\\label{sec:f4}\n\nIncreasing the imagination step size from $\\Delta t{=}2$ to $\\Delta t{=}4$ worsens degradation monotonically. Peak evaluation returns are ${\\sim}950$ ($\\Delta t{=}1$, exp\\_001), 485.3 ($\\Delta t{=}2$, exp\\_006), and 176.9 ($\\Delta t{=}4$, exp\\_007).\n\n\\begin{figure}[h]\n  \\centering\n  % PLACEHOLDER: dt=1 vs dt=2 vs dt=4 comparison\n  \\includegraphics[width=0.7\\linewidth]{figures/fig5_dt_amplification.pdf}\n  \\caption{Performance vs.\\ imagination step size: monotonic degradation.}\n  \\label{fig:dt_amplification}\n\\end{figure}\n\nAt $\\Delta t{=}4$ (exp\\_007), the value/eval ratio at 45K is 0.126 (exp\\_007)---severely suppressed rather than inflated---indicating a qualitatively different failure: the RSSM prediction quality at $\\Delta t{=}4$ is too poor even for overestimation to develop, consistent with compounding prediction error over longer temporal gaps. Only two $\\Delta t$ values were tested; a finer grid would be needed to characterize the degradation curve.\n\n\n% ============================================================\n% F5: HORIZON/SUBSAMPLE SECONDARY\n% ============================================================\n\n\\subsection{Finding 5: Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nSubsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO.\n\n\\paragraph{Subsampling is not sufficient for collapse.} Exp\\_008e\\_v3 (trained $e_{\\Delta t}$, subsample \\textsc{on}, $\\Delta t{=}1$ imagination, $H{=}15$) achieves 869.9 at 105K---95\\% of baseline---with seed~1 (exp\\_008e\\_v3\\_s1).\\footnote{An independent run with seed~0 (exp\\_008e\\_v3) reproduces this trajectory.} This demonstrates that multi-rate training data alone does not degrade performance when imagination is restricted to $\\Delta t{=}1$. Seed~2, however, collapses from 715.2 at 85K to 137.0 at 105K (exp\\_008e\\_v3\\_s2), through a non-CIVO mechanism discussed in Section~\\ref{sec:failure_taxonomy}.\n\n\\paragraph{Horizon affects performance level but not the overestimation pattern.} Exp\\_008c ($H{=}8$, unexposed $e_{\\Delta t}$, subsample \\textsc{off}) plateaus at 241.9 at 55K (exp\\_008c), while exp\\_008a ($H{=}15$, same configuration otherwise) reaches 777.7 at 105K (exp\\_008a). Both maintain healthy NVE ($\\leq$0.93$\\times$), confirming that horizon length modulates the performance ceiling but does not trigger CIVO.\n\n\n% ============================================================\n% GRADIENT DECOMPOSITION\n% ============================================================\n\n\\subsection{Gradient Decomposition: Observation Decoders Dominate Temporal Embedding Learning}\n\\label{sec:gradient_decomposition_results}\n\nTo identify which gradient pathway through $e_{\\Delta t}$ drives CIVO, we performed a post-hoc gradient decomposition (D061) measuring each loss component's contribution to the temporal embedding parameters via \\texttt{torch.autograd.grad}. The analysis was motivated by a targeted stop-gradient experiment (exp\\_016e) in which $e_{\\Delta t}$ was detached from the reward head during the backward pass---see Section~\\ref{sec:sgs_gradient_analysis} for full experimental details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Gradient contributions to $e_{\\Delta t}$ parameters by loss component ($\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$), measured at training step 95K (D061 analysis). Total gradient norm: 1.624.}\n\\label{tab:gradient_decomposition_results}\n\\begin{tabular}{lrr}\n\\toprule\nLoss component & $\\|\\nabla_\\theta \\mathcal{L}_i\\|_2$ & Share (\\%) \\\\\n\\midrule\nObservation decoders (orientations, velocity, height) & 1.505 & 92.7 \\\\\nKL dynamics & 0.119 & 7.3 \\\\\nContinuation head & $<$0.001 & $<$0.1 \\\\\nReward head & 0.000 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reward head's contribution is numerically negligible---zero to within floating-point precision. This explains why exp\\_016e (reward-only stop-gradient; identical to exp\\_008d except \\texttt{reward\\_dt\\_emb\\_detach=True}) exhibits the same collapse pattern: peak 326.7 at 75K followed by catastrophic decline to 31.7 at 95K with NVE reaching $10.42\\times$ (exp\\_016e). The intervention detaches a gradient that does not exist---an architectural no-op. The timing differences between exp\\_016e and exp\\_008d (collapse onset ${\\sim}$75K vs.\\ ${\\sim}$25K, peak 326.7 vs.\\ 167.2) are consistent with cross-seed variation across the 008d configuration's trajectories (cf.\\ exp\\_009b, peak 278.5 at 95K).\n\nThe 93\\%/7\\%/0\\% split reveals that $e_{\\Delta t}$ learns to encode temporal information that minimizes \\textit{observation reconstruction error}, not reward prediction error. CIVO originates in the observation reconstruction objective's influence on latent dynamics---a structural property of DreamerV3's multi-head decoder architecture \\citep{hafner2023dreamerv3}. This constrains the space of viable interventions: strategies targeting the reward pathway alone address $<$1\\% of the gradient flow and cannot attenuate CIVO. The full-pathway SGS intervention (exp\\_018; Section~\\ref{sec:pending}) removes the dominant 93\\% observation decoder contribution, constituting a genuine gradient-level intervention.\n\nThis gradient asymmetry is consistent with prior observations on the dominance of reconstruction losses in world-model training \\citep{hafner2023dreamerv3, ma2024harmonydream}, but the D061 analysis provides the first \\textit{backward-pass decomposition} quantifying the per-component gradient contributions to a conditioning variable. HarmonyDream \\citep{ma2024harmonydream} reports a two-order-of-magnitude gap between observation and reward loss magnitudes; our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.\n\n\n% ============================================================\n% THREE FAILURE MODES\n% ============================================================\n\n\\subsection{Three Distinct Failure Modes}\n\\label{sec:failure_taxonomy}\n\n\\begin{figure}[t]\n  \\centering\n  % PLACEHOLDER: Contrasting collapse dynamics across three mechanisms\n  \\includegraphics[width=\\linewidth]{figures/fig6_failure_modes.pdf}\n  \\caption{Three failure modes triggered by temporal embedding configurations. Left: CIVO (exp\\_008d)---value explosion drives eval decline, entropy decreases. Center: Gradient starvation (exp\\_015b)---actor loss approaches zero, performance oscillates without convergence. Right: IRD (exp\\_008e\\_v3\\_s2)---eval collapse precedes value rise, entropy increases.}\n  \\label{fig:failure_modes}\n\\end{figure}\n\nThe experiments reveal three mechanistically distinct failure modes. Distinguishing these modes is necessary for designing targeted interventions, as surface-level metrics (e.g., low final eval return) are shared across all three but the underlying dynamics differ qualitatively.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Taxonomy of failure modes identified across temporal embedding configurations.}\n\\label{tab:failure_taxonomy}\n\\begin{tabular}{lccc}\n\\toprule\nFeature & CIVO & Grad.\\ Starvation & IRD \\\\\n\\midrule\nRepresentative exp & 008d (seed 1) & 015b & 008e\\_v3\\_s2 \\\\\n$e_{\\Delta t}$ config & trained & frozen & trained \\\\\nNVE trajectory & sustained $>$1.5$\\times$ & $<$0.5$\\times$ & passive rise \\\\\nValue dynamics & explosion ($+$130\\%) & suppressed & stable \\\\\nEval dynamics & decline & volatile (80--238) & collapse ($-$81\\%) \\\\\nActor entropy & $\\downarrow$ (locks in) & --- & $\\uparrow$ (de-specializes) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditioning-Induced Value Overestimation (CIVO).} In exp\\_008d and exp\\_006, the trained temporal embedding enables the reward head to produce systematically biased $\\Delta t{>}1$ predictions. RSSM fidelity analysis reveals a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions in exp\\_008d (see Table~\\ref{tab:rssm_fidelity} in Section~\\ref{sec:rssm_analysis}). The critic inherits these biases through the $\\lambda$-return computation, overestimates values for $\\Delta t{>}1$ trajectories, and the actor exploits the overestimated landscape. This positive feedback loop produces accelerating NVE ($1.71\\times \\to 2.09\\times \\to 4.12\\times$ at 35--55K in exp\\_008d) with decreasing actor entropy---the policy becomes increasingly deterministic as it converges on the overestimated region.\n\n\\paragraph{Gradient Starvation.} A frozen temporal embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}) cannot co-adapt as RSSM representations drift during training. Actor loss approaches zero (0.0002 at 105K, exp\\_015b), indicating gradient starvation: the actor receives insufficient learning signal. NVE remains at 0.39--0.47$\\times$ (exp\\_015b)---the critic \\textit{under-estimates}, the opposite of CIVO. Evaluation oscillates between 80 and 238 without convergence. The NVE briefly reaches 1.45$\\times$ at 55K but self-corrects to 0.65$\\times$ by 65K---a transient, sub-threshold overestimation qualitatively different from CIVO's sustained acceleration.\n\n\\paragraph{Imagination-Reality Divergence (IRD).} Exp\\_008e\\_v3\\_s2 collapses despite using $\\Delta t{=}1$-only imagination (\\texttt{gate\\_dt\\_mean}$\\,{=}\\,$1.0 throughout, exp\\_008e\\_v3\\_s2). Evaluation drops from 715.2 at 85K to 137.0 at 105K, while value estimates remain relatively stable (339.3 $\\to$ 339.8), producing a passive NVE rise to $3.78\\times$ (exp\\_008e\\_v3\\_s2). Crucially, actor entropy \\textit{increases} from $-5.21$ to $-3.83$ during collapse (policy de-specialization), the opposite of CIVO's entropy decrease. The baseline seed~2 (exp\\_009a) is stable through the same window (618.7 $\\to$ 836.5 at 85K--105K, exp\\_009a), ruling out seed-specific fragility.\n\nThis failure mode does not involve value overestimation driving actor exploitation. Rather, the trained embedding's interaction with multi-rate training data appears to create a latent representation vulnerability that manifests as policy instability independent of imagination $\\Delta t$. The NVE rise is a \\textit{consequence} of eval collapse, not a cause---distinguishing IRD from CIVO where the NVE rise precedes and drives the eval decline.\n\nThe existence of IRD alongside CIVO suggests that the trained temporal embedding creates vulnerability through multiple pathways. Eliminating CIVO (e.g., via $\\Delta t{=}1$ imagination) does not eliminate all failure modes.\n\n\n% ============================================================\n% PENDING EXPERIMENTS (PLACEHOLDERS)\n% ============================================================\n\n\\subsection{Pending Experiments}\n\\label{sec:pending}\n\nTwo experiment series are queued to extend the diagnostic analysis:\n\n\\paragraph{Full-pathway SGS (exp\\_018).} Detaches all non-KL gradients from the temporal embedding, removing the dominant 93\\% observation decoder contribution while retaining only the 7\\% KL dynamics signal. If CIVO persists with only KL gradients, the vulnerability is representation-level (KL training alone sufficient); if eliminated, the observation decoder gradient pathway is the root cause. Results will be reported upon completion.\n\n\\paragraph{Cross-environment validation (exp\\_019 series).} PickCube-v1 (ManiSkill3) baseline (exp\\_019a) and CIVO trigger condition (exp\\_019b) to test whether the identified mechanisms transfer beyond locomotion to manipulation tasks with qualitatively different observation and reward structure.\n",
    "structuredPatch": [
      {
        "oldStart": 156,
        "oldLines": 7,
        "newStart": 156,
        "newLines": 7,
        "lines": [
          " \\subsection{Finding 5: Horizon and Subsampling Are Secondary Factors}",
          " \\label{sec:f5}",
          " ",
          "-Subsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO.",
          "+Subsampling is a necessary co-factor for CIVO but not independently sufficient; imagination horizon modulates performance level without independently triggering overestimation.",
          " ",
          " \\paragraph{Subsampling is not sufficient for collapse.} Exp\\_008e\\_v3 (trained $e_{\\Delta t}$, subsample \\textsc{on}, $\\Delta t{=}1$ imagination, $H{=}15$) achieves 869.9 at 105K---95\\% of baseline---with seed~1 (exp\\_008e\\_v3\\_s1).\\footnote{An independent run with seed~0 (exp\\_008e\\_v3) reproduces this trajectory.} This demonstrates that multi-rate training data alone does not degrade performance when imagination is restricted to $\\Delta t{=}1$. Seed~2, however, collapses from 715.2 at 85K to 137.0 at 105K (exp\\_008e\\_v3\\_s2), through a non-CIVO mechanism discussed in Section~\\ref{sec:failure_taxonomy}.",
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_014m8fTXqjYmV3K7CA4p8jf1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results.md",
  "old_string": "our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.",
  "new_string": "our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result, ruling out reward-pathway interventions for this architecture."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "8c5e712e-28bf-4d86-9c6c-cc67e33db942",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V54jiNVxjBmLXbjUEkzwbF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7082,
      "cache_read_input_tokens": 49491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7082
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

_source line 24 · 2026-05-16T16:28:52.745Z_

<details><summary>↩ Tool result · `toolu_014m8fTXqjYmV3K7CA4p8jf1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "793c9896-9a7f-4f87-a8ff-70b68de621d5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results.md",
    "oldString": "our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.",
    "newString": "our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result, ruling out reward-pathway interventions for this architecture.",
    "originalFile": "% Results Section — Draft v1\n% Target: CoRL 2026\n% Status: Draft, pending Director review\n% Writing order: 1 (anchors all other sections)\n\n\\section{Results}\n\\label{sec:results}\n\nWe organize findings around five diagnostic questions, followed by a gradient decomposition analysis and a taxonomy of failure modes. All quantitative claims cite experiment identifiers for traceability; evaluation returns are means over 10 episodes at each checkpoint. Experiments use Walker Walk from the DeepMind Control Suite (see Section~\\ref{sec:environment}).\n\n% ============================================================\n% F1: ALL DT>1 DEGRADE\n% ============================================================\n\n\\subsection{Finding 1: All Variable-Rate Configurations Degrade Performance}\n\\label{sec:f1}\n\n\\begin{figure}[t]\n  \\centering\n  % PLACEHOLDER: Learning curves for exp_001, 005, 006, 007\n  \\includegraphics[width=\\linewidth]{figures/fig1_learning_curves.pdf}\n  \\caption{Learning curves for all primary configurations. The \\mbox{$\\Delta t{=}1$} baseline (exp\\_001) converges to ${\\sim}950$; every $\\Delta t{>}1$ variant degrades or collapses.}\n  \\label{fig:learning_curves}\n\\end{figure}\n\nEvery tested variable-rate imagination configuration degrades asymptotic performance relative to the standard $\\Delta t{=}1$ baseline. The baseline (exp\\_001, seed~1) reaches 915.7 at 105K steps and converges to ${\\sim}950$ asymptotically (peak 970.4 at 505K). In contrast:\n\n\\begin{itemize}\n    \\item \\textbf{Learned gate} (exp\\_005): peaks at 541.2 at 55K, then declines to 98.8 by 145K---a 90\\% drop from peak.\n    \\item \\textbf{Fixed $\\Delta t{=}2$} (exp\\_006, $H{=}15$): peaks at 485.3 at 35K, then collapses to 132.9 by 65K as the value/eval ratio accelerates from 31\\% to 272\\%.\n    \\item \\textbf{Fixed $\\Delta t{=}4$} (exp\\_007, $H{=}15$): peaks at 176.9 at 25K and plateaus around 144--152, never exceeding 19\\% of the baseline's asymptotic level.\n\\end{itemize}\n\nNo $\\Delta t{>}1$ configuration achieves sustained performance above 60\\% of the baseline beyond 65K steps. The degradation patterns vary---inverted-V collapse (exp\\_006), monotonic decline (exp\\_005), and severe suppression (exp\\_007)---but the qualitative conclusion is uniform: variable-rate imagination degrades performance on Walker Walk across all tested configurations.\n\n\n% ============================================================\n% F2: TRAINED DT_EMB → CIVO\n% ============================================================\n\n\\subsection{Finding 2: Trained Temporal Embedding Reliably Triggers Pathological Value Overestimation}\n\\label{sec:f2}\n\n\\begin{figure}[t]\n  \\centering\n  % PLACEHOLDER: NVE trajectories with 1.5x threshold\n  \\includegraphics[width=\\linewidth]{figures/fig2_nve_trajectories.pdf}\n  \\caption{Normalized value/eval ratio (NVE) trajectories. Dashed line: $1.5\\times$ pathological threshold (applied at $k \\geq 35\\text{K}$). Both trained-$e_{\\Delta t}$ seeds exceed the threshold; neither removed-$e_{\\Delta t}$ seed does.}\n  \\label{fig:nve_trajectories}\n\\end{figure}\n\nThe controlled comparison between exp\\_008d (trained $e_{\\Delta t}$, subsample \\textsc{on}, $H{=}8$) and exp\\_008f ($e_{\\Delta t}$ removed, subsample \\textsc{on}, $H{=}8$) isolates the temporal embedding as the causal factor for conditioning-induced value overestimation (CIVO). These experiments share identical configurations except for the presence of the trained temporal embedding.\n\n\\paragraph{Diagnostic threshold.} Using the normalized value/eval ratio (NVE; see Section~\\ref{sec:diagnostic}), the $\\hat{r}_k > 1.5$ threshold at steps $\\geq$35K achieves 4/4 classification accuracy across seeds:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NVE diagnostic: trained vs.\\ removed temporal embedding. Peak NVE reported at steps $\\geq$35K where baseline $r_k > 0.24$ ensures ratio stability.}\n\\label{tab:nve_separation}\n\\begin{tabular}{llcc}\n\\toprule\nCondition & Seed & Peak NVE ($\\geq$35K) & $>$1.5$\\times$? \\\\\n\\midrule\nTrained $e_{\\Delta t}$ (exp\\_008d) & 1 & 2.09$\\times$ @ 45K & \\textbf{Yes} \\\\\nTrained $e_{\\Delta t}$ (exp\\_009b) & 2 & 1.62$\\times$ @ 45K & \\textbf{Yes} \\\\\nRemoved $e_{\\Delta t}$ (exp\\_008f) & 1 & 0.97$\\times$ @ 55K & No \\\\\nRemoved $e_{\\Delta t}$ (exp\\_009c) & 2 & 1.14$\\times$ @ 105K & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth trained-$e_{\\Delta t}$ seeds exceed the pathological threshold; neither removed-$e_{\\Delta t}$ seed does. The trained embedding reliably induces pathological value overestimation, though whether this overestimation progresses to catastrophic collapse is stochastic (see below).\n\n\\paragraph{Causal isolation.} The factorial structure establishes that CIVO requires the combination of a \\textit{trained} temporal embedding and exposure to multi-rate training data:\n\n\\begin{figure}[h]\n  \\centering\n  % PLACEHOLDER: 2×2 factorial grid summary\n  \\includegraphics[width=0.85\\linewidth]{figures/fig3_factorial_grid.pdf}\n  \\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\Delta t}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n  \\label{fig:factorial_grid}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\Delta t}$ configuration $\\times$ multi-rate data exposure. All treatment conditions use $\\Delta t{=}2$ imagination and $H{=}8$ (except exp\\_008a: $H{=}15$).}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\Delta t}$ & exp\\_008d: CIVO & exp\\_008a: healthy \\\\\n & NVE 2.09$\\times$, collapse & NVE 0.59--0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\Delta t}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & NVE 0.39--0.47$\\times$ & \\\\\n\\midrule\nRemoved $e_{\\Delta t}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\Delta t{>}1$ transitions during world-model training (subsample \\textsc{off}). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the 0.59--0.93$\\times$ range across 105K steps (exp\\_008a). The critical trigger is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\Delta t{>}1$ state predictions within the RSSM.\n\n\\paragraph{Post-CIVO outcomes: seed-dependent trajectories.} The 008d configuration was run with two independent seeds, producing qualitatively distinct outcomes:\n\n\\begin{enumerate}\n    \\item \\textbf{Seed~1} (exp\\_008d / exp\\_009e): CIVO onset at 25K (NVE 1.78$\\times$), eval declines from 167.2 to 82.8 by 55K (exp\\_008d). Extended to 105K (exp\\_009e), the run shows oscillatory degradation: a transient bounce to 250 at 65K, but actor loss flips positive ($+$0.011 at 85K, exp\\_009e), signaling permanent actor damage. Eval oscillates between 131 and 250 without sustained recovery, ending at 131.1 at 105K (exp\\_009e).\n    \\item \\textbf{Seed~2} (exp\\_009b): transient NVE of 1.62$\\times$ at 45K, followed by self-correction---NVE declines monotonically from 1.62$\\times$ to 0.38$\\times$ between 45K and 105K. Value peaks at 110.9 at 65K then self-corrects to 67.3 by 105K, while eval rises from 141.0 to a peak of 278.5 at 95K (exp\\_009b).\n\\end{enumerate}\n\nBoth seeds cross the NVE~$>$~1.5$\\times$ threshold, confirming the trained embedding as a reliable trigger. The downstream trajectory depends on whether overestimation is sustained across consecutive checkpoints (seed~1: $1.71\\times \\to 2.09\\times \\to 4.12\\times$ at 35--55K, locking in the positive feedback loop) or transient (seed~2: $1.62\\times$ at 45K $\\to$ $1.41\\times$ at 55K, declining).\n\n\n% ============================================================\n% F3: UNTRAINED DT_EMB → PROTECTION\n% ============================================================\n\n\\subsection{Finding 3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\nExp\\_008a (trained-but-unexposed $e_{\\Delta t}$,\\footnote{Exp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\Delta t{>}1$ data due to subsample \\textsc{off}; it is not frozen or absent. See Table~\\ref{tab:factorial}.} subsample \\textsc{off}, $H{=}15$) demonstrates sustained value growth suppression over 105K steps. Its NVE ranges from 0.59$\\times$ to 0.93$\\times$ across the 55K--105K window (exp\\_008a), diverging further \\textit{below} baseline levels over time rather than converging toward them.\n\nPerformance follows two complete V-shaped recovery cycles: $500.8 \\to 563.4 \\to 487.9 \\to 608.0 \\to 469.9 \\to 583.7 \\to 572.2 \\to 777.7$ over 35K--105K (exp\\_008a). The final evaluation of 777.7 at 105K reaches 85\\% of the baseline at the same step (915.7, exp\\_001), with no collapse through 112K training steps.\n\nThis contrasts sharply with exp\\_006 (trained $e_{\\Delta t}$, subsample \\textsc{on}, $H{=}15$), where NVE accelerates from 1.61$\\times$ at 45K to 2.31$\\times$ at 55K before catastrophic collapse to 132.9 at 65K (exp\\_006). The 006-vs-008a comparison corroborates the causal role of multi-rate data exposure: both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\Delta t{>}1$ transitions during training.\n\n\n% ============================================================\n% F4: DT AMPLIFICATION\n% ============================================================\n\n\\subsection{Finding 4: Longer Temporal Gaps Amplify Degradation}\n\\label{sec:f4}\n\nIncreasing the imagination step size from $\\Delta t{=}2$ to $\\Delta t{=}4$ worsens degradation monotonically. Peak evaluation returns are ${\\sim}950$ ($\\Delta t{=}1$, exp\\_001), 485.3 ($\\Delta t{=}2$, exp\\_006), and 176.9 ($\\Delta t{=}4$, exp\\_007).\n\n\\begin{figure}[h]\n  \\centering\n  % PLACEHOLDER: dt=1 vs dt=2 vs dt=4 comparison\n  \\includegraphics[width=0.7\\linewidth]{figures/fig5_dt_amplification.pdf}\n  \\caption{Performance vs.\\ imagination step size: monotonic degradation.}\n  \\label{fig:dt_amplification}\n\\end{figure}\n\nAt $\\Delta t{=}4$ (exp\\_007), the value/eval ratio at 45K is 0.126 (exp\\_007)---severely suppressed rather than inflated---indicating a qualitatively different failure: the RSSM prediction quality at $\\Delta t{=}4$ is too poor even for overestimation to develop, consistent with compounding prediction error over longer temporal gaps. Only two $\\Delta t$ values were tested; a finer grid would be needed to characterize the degradation curve.\n\n\n% ============================================================\n% F5: HORIZON/SUBSAMPLE SECONDARY\n% ============================================================\n\n\\subsection{Finding 5: Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nSubsampling is a necessary co-factor for CIVO but not independently sufficient; imagination horizon modulates performance level without independently triggering overestimation.\n\n\\paragraph{Subsampling is not sufficient for collapse.} Exp\\_008e\\_v3 (trained $e_{\\Delta t}$, subsample \\textsc{on}, $\\Delta t{=}1$ imagination, $H{=}15$) achieves 869.9 at 105K---95\\% of baseline---with seed~1 (exp\\_008e\\_v3\\_s1).\\footnote{An independent run with seed~0 (exp\\_008e\\_v3) reproduces this trajectory.} This demonstrates that multi-rate training data alone does not degrade performance when imagination is restricted to $\\Delta t{=}1$. Seed~2, however, collapses from 715.2 at 85K to 137.0 at 105K (exp\\_008e\\_v3\\_s2), through a non-CIVO mechanism discussed in Section~\\ref{sec:failure_taxonomy}.\n\n\\paragraph{Horizon affects performance level but not the overestimation pattern.} Exp\\_008c ($H{=}8$, unexposed $e_{\\Delta t}$, subsample \\textsc{off}) plateaus at 241.9 at 55K (exp\\_008c), while exp\\_008a ($H{=}15$, same configuration otherwise) reaches 777.7 at 105K (exp\\_008a). Both maintain healthy NVE ($\\leq$0.93$\\times$), confirming that horizon length modulates the performance ceiling but does not trigger CIVO.\n\n\n% ============================================================\n% GRADIENT DECOMPOSITION\n% ============================================================\n\n\\subsection{Gradient Decomposition: Observation Decoders Dominate Temporal Embedding Learning}\n\\label{sec:gradient_decomposition_results}\n\nTo identify which gradient pathway through $e_{\\Delta t}$ drives CIVO, we performed a post-hoc gradient decomposition (D061) measuring each loss component's contribution to the temporal embedding parameters via \\texttt{torch.autograd.grad}. The analysis was motivated by a targeted stop-gradient experiment (exp\\_016e) in which $e_{\\Delta t}$ was detached from the reward head during the backward pass---see Section~\\ref{sec:sgs_gradient_analysis} for full experimental details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Gradient contributions to $e_{\\Delta t}$ parameters by loss component ($\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$), measured at training step 95K (D061 analysis). Total gradient norm: 1.624.}\n\\label{tab:gradient_decomposition_results}\n\\begin{tabular}{lrr}\n\\toprule\nLoss component & $\\|\\nabla_\\theta \\mathcal{L}_i\\|_2$ & Share (\\%) \\\\\n\\midrule\nObservation decoders (orientations, velocity, height) & 1.505 & 92.7 \\\\\nKL dynamics & 0.119 & 7.3 \\\\\nContinuation head & $<$0.001 & $<$0.1 \\\\\nReward head & 0.000 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reward head's contribution is numerically negligible---zero to within floating-point precision. This explains why exp\\_016e (reward-only stop-gradient; identical to exp\\_008d except \\texttt{reward\\_dt\\_emb\\_detach=True}) exhibits the same collapse pattern: peak 326.7 at 75K followed by catastrophic decline to 31.7 at 95K with NVE reaching $10.42\\times$ (exp\\_016e). The intervention detaches a gradient that does not exist---an architectural no-op. The timing differences between exp\\_016e and exp\\_008d (collapse onset ${\\sim}$75K vs.\\ ${\\sim}$25K, peak 326.7 vs.\\ 167.2) are consistent with cross-seed variation across the 008d configuration's trajectories (cf.\\ exp\\_009b, peak 278.5 at 95K).\n\nThe 93\\%/7\\%/0\\% split reveals that $e_{\\Delta t}$ learns to encode temporal information that minimizes \\textit{observation reconstruction error}, not reward prediction error. CIVO originates in the observation reconstruction objective's influence on latent dynamics---a structural property of DreamerV3's multi-head decoder architecture \\citep{hafner2023dreamerv3}. This constrains the space of viable interventions: strategies targeting the reward pathway alone address $<$1\\% of the gradient flow and cannot attenuate CIVO. The full-pathway SGS intervention (exp\\_018; Section~\\ref{sec:pending}) removes the dominant 93\\% observation decoder contribution, constituting a genuine gradient-level intervention.\n\nThis gradient asymmetry is consistent with prior observations on the dominance of reconstruction losses in world-model training \\citep{hafner2023dreamerv3, ma2024harmonydream}, but the D061 analysis provides the first \\textit{backward-pass decomposition} quantifying the per-component gradient contributions to a conditioning variable. HarmonyDream \\citep{ma2024harmonydream} reports a two-order-of-magnitude gap between observation and reward loss magnitudes; our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.\n\n\n% ============================================================\n% THREE FAILURE MODES\n% ============================================================\n\n\\subsection{Three Distinct Failure Modes}\n\\label{sec:failure_taxonomy}\n\n\\begin{figure}[t]\n  \\centering\n  % PLACEHOLDER: Contrasting collapse dynamics across three mechanisms\n  \\includegraphics[width=\\linewidth]{figures/fig6_failure_modes.pdf}\n  \\caption{Three failure modes triggered by temporal embedding configurations. Left: CIVO (exp\\_008d)---value explosion drives eval decline, entropy decreases. Center: Gradient starvation (exp\\_015b)---actor loss approaches zero, performance oscillates without convergence. Right: IRD (exp\\_008e\\_v3\\_s2)---eval collapse precedes value rise, entropy increases.}\n  \\label{fig:failure_modes}\n\\end{figure}\n\nThe experiments reveal three mechanistically distinct failure modes. Distinguishing these modes is necessary for designing targeted interventions, as surface-level metrics (e.g., low final eval return) are shared across all three but the underlying dynamics differ qualitatively.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Taxonomy of failure modes identified across temporal embedding configurations.}\n\\label{tab:failure_taxonomy}\n\\begin{tabular}{lccc}\n\\toprule\nFeature & CIVO & Grad.\\ Starvation & IRD \\\\\n\\midrule\nRepresentative exp & 008d (seed 1) & 015b & 008e\\_v3\\_s2 \\\\\n$e_{\\Delta t}$ config & trained & frozen & trained \\\\\nNVE trajectory & sustained $>$1.5$\\times$ & $<$0.5$\\times$ & passive rise \\\\\nValue dynamics & explosion ($+$130\\%) & suppressed & stable \\\\\nEval dynamics & decline & volatile (80--238) & collapse ($-$81\\%) \\\\\nActor entropy & $\\downarrow$ (locks in) & --- & $\\uparrow$ (de-specializes) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditioning-Induced Value Overestimation (CIVO).} In exp\\_008d and exp\\_006, the trained temporal embedding enables the reward head to produce systematically biased $\\Delta t{>}1$ predictions. RSSM fidelity analysis reveals a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions in exp\\_008d (see Table~\\ref{tab:rssm_fidelity} in Section~\\ref{sec:rssm_analysis}). The critic inherits these biases through the $\\lambda$-return computation, overestimates values for $\\Delta t{>}1$ trajectories, and the actor exploits the overestimated landscape. This positive feedback loop produces accelerating NVE ($1.71\\times \\to 2.09\\times \\to 4.12\\times$ at 35--55K in exp\\_008d) with decreasing actor entropy---the policy becomes increasingly deterministic as it converges on the overestimated region.\n\n\\paragraph{Gradient Starvation.} A frozen temporal embedding (exp\\_015b, $d{=}32$, \\texttt{requires\\_grad=False}) cannot co-adapt as RSSM representations drift during training. Actor loss approaches zero (0.0002 at 105K, exp\\_015b), indicating gradient starvation: the actor receives insufficient learning signal. NVE remains at 0.39--0.47$\\times$ (exp\\_015b)---the critic \\textit{under-estimates}, the opposite of CIVO. Evaluation oscillates between 80 and 238 without convergence. The NVE briefly reaches 1.45$\\times$ at 55K but self-corrects to 0.65$\\times$ by 65K---a transient, sub-threshold overestimation qualitatively different from CIVO's sustained acceleration.\n\n\\paragraph{Imagination-Reality Divergence (IRD).} Exp\\_008e\\_v3\\_s2 collapses despite using $\\Delta t{=}1$-only imagination (\\texttt{gate\\_dt\\_mean}$\\,{=}\\,$1.0 throughout, exp\\_008e\\_v3\\_s2). Evaluation drops from 715.2 at 85K to 137.0 at 105K, while value estimates remain relatively stable (339.3 $\\to$ 339.8), producing a passive NVE rise to $3.78\\times$ (exp\\_008e\\_v3\\_s2). Crucially, actor entropy \\textit{increases} from $-5.21$ to $-3.83$ during collapse (policy de-specialization), the opposite of CIVO's entropy decrease. The baseline seed~2 (exp\\_009a) is stable through the same window (618.7 $\\to$ 836.5 at 85K--105K, exp\\_009a), ruling out seed-specific fragility.\n\nThis failure mode does not involve value overestimation driving actor exploitation. Rather, the trained embedding's interaction with multi-rate training data appears to create a latent representation vulnerability that manifests as policy instability independent of imagination $\\Delta t$. The NVE rise is a \\textit{consequence} of eval collapse, not a cause---distinguishing IRD from CIVO where the NVE rise precedes and drives the eval decline.\n\nThe existence of IRD alongside CIVO suggests that the trained temporal embedding creates vulnerability through multiple pathways. Eliminating CIVO (e.g., via $\\Delta t{=}1$ imagination) does not eliminate all failure modes.\n\n\n% ============================================================\n% PENDING EXPERIMENTS (PLACEHOLDERS)\n% ============================================================\n\n\\subsection{Pending Experiments}\n\\label{sec:pending}\n\nTwo experiment series are queued to extend the diagnostic analysis:\n\n\\paragraph{Full-pathway SGS (exp\\_018).} Detaches all non-KL gradients from the temporal embedding, removing the dominant 93\\% observation decoder contribution while retaining only the 7\\% KL dynamics signal. If CIVO persists with only KL gradients, the vulnerability is representation-level (KL training alone sufficient); if eliminated, the observation decoder gradient pathway is the root cause. Results will be reported upon completion.\n\n\\paragraph{Cross-environment validation (exp\\_019 series).} PickCube-v1 (ManiSkill3) baseline (exp\\_019a) and CIVO trigger condition (exp\\_019b) to test whether the identified mechanisms transfer beyond locomotion to manipulation tasks with qualitatively different observation and reward structure.\n",
    "structuredPatch": [
      {
        "oldStart": 193,
        "oldLines": 7,
        "newStart": 193,
        "newLines": 7,
        "lines": [
          " ",
          " The 93\\%/7\\%/0\\% split reveals that $e_{\\Delta t}$ learns to encode temporal information that minimizes \\textit{observation reconstruction error}, not reward prediction error. CIVO originates in the observation reconstruction objective's influence on latent dynamics---a structural property of DreamerV3's multi-head decoder architecture \\citep{hafner2023dreamerv3}. This constrains the space of viable interventions: strategies targeting the reward pathway alone address $<$1\\% of the gradient flow and cannot attenuate CIVO. The full-pathway SGS intervention (exp\\_018; Section~\\ref{sec:pending}) removes the dominant 93\\% observation decoder contribution, constituting a genuine gradient-level intervention.",
          " ",
          "-This gradient asymmetry is consistent with prior observations on the dominance of reconstruction losses in world-model training \\citep{hafner2023dreamerv3, ma2024harmonydream}, but the D061 analysis provides the first \\textit{backward-pass decomposition} quantifying the per-component gradient contributions to a conditioning variable. HarmonyDream \\citep{ma2024harmonydream} reports a two-order-of-magnitude gap between observation and reward loss magnitudes; our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.",
          "+This gradient asymmetry is consistent with prior observations on the dominance of reconstruction losses in world-model training \\citep{hafner2023dreamerv3, ma2024harmonydream}, but the D061 analysis provides the first \\textit{backward-pass decomposition} quantifying the per-component gradient contributions to a conditioning variable. HarmonyDream \\citep{ma2024harmonydream} reports a two-order-of-magnitude gap between observation and reward loss magnitudes; our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result, ruling out reward-pathway interventions for this architecture.",
          " ",
          " ",
          " % ============================================================"
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01M1Y3zzbWinGowx82HV7p1w`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md",
  "old_string": "**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.",
  "new_string": "**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises specifically when the actor-critic exploits the embedding's $\\Delta t > 1$ predictions during imagination."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "dd1eca2c-4ceb-4de4-833d-47317b339d75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V54jiNVxjBmLXbjUEkzwbF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7082,
      "cache_read_input_tokens": 49491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7082
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

_source line 26 · 2026-05-16T16:29:02.286Z_

<details><summary>↩ Tool result · `toolu_01M1Y3zzbWinGowx82HV7p1w`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "15cfc7a0-51d7-4cdb-a4fb-a86c16b9dcd8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md",
    "oldString": "**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.",
    "newString": "**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises specifically when the actor-critic exploits the embedding's $\\Delta t > 1$ predictions during imagination.",
    "originalFile": "% Method — Draft v2\n% Target: CoRL 2026\n% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8).\n% Note: Complements experimental_setup.md (Section 4). Some overlap in\n%   diagnostic framework and factorial design is intentional—final paper\n%   may merge or redistribute content between Sections 3 and 4.\n\n# 3. Methodology\n\nWe present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \\citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \\citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.\n\n\n## 3.1 Background: DreamerV3 and Variable-Rate Imagination\n\n### World-Model Actor-Critic\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:\n\n$$h_{t+1} = f_\\theta(h_t, z_t, a_t), \\quad \\hat{z}_{t+1} \\sim p_\\theta(\\cdot \\mid h_{t+1})$$\n\nAn actor $\\pi_\\psi$ selects actions and a critic $V_\\xi$ estimates $\\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\\Delta t = 1$) and $H = 15$.\n\n### Temporal Abstraction via Variable-Rate Imagination\n\nTemporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \\citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.\n\nWe introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:\n\n**Temporal step-size embedding.** An embedding $e_{\\Delta t} \\in \\mathbb{R}^d$ conditions the RSSM transition on the step size:\n\n$$h_{t+\\Delta t} = f_\\theta(h_t, z_t, a_t, e_{\\Delta t})$$\n\nWe study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\\Delta t$ values; the untrained and removed configurations serve as controls.\n\n**Temporal subsampling.** When enabled, the replay buffer stores both $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\\Delta t{=}1$ transitions are used for world-model training.\n\n**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\\Delta t{=}1$ (standard) or $\\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.\n\n### Conditioning-Induced Value Overestimation (CIVO)\n\nWhen the RSSM predicts $\\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\\xi$ receives precise $\\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.\n\nWe term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \\& Schuurmans' \\citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\\Delta t}$ and the RSSM's degraded fidelity at $\\Delta t > 1$, not the policy's representational capacity.\n\n\n## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio\n\n### Motivation\n\nDistinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\\_001\\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.\n\n### Definition\n\n**Value-evaluation ratio.** At training step $k$:\n\n$$r_k = \\frac{\\bar{v}_k}{\\bar{R}_k}$$\n\nwhere $\\bar{v}_k$ is the mean predicted value across imagined states and $\\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.\n\n**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:\n\n$$\\hat{r}_k = \\frac{r_k^{\\,\\text{exp}}}{r_k^{\\,\\text{baseline}}}$$\n\nThis removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.\n\n### Diagnostic Thresholds\n\nWe calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:\n\n- **$\\hat{r}_k > 1.5$ (at $k \\geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\\_embedding conditions exceed 1.5$\\times$ at 35K+ steps (exp\\_008d seed 1: 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K; exp\\_009b seed 2: 1.62$\\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\\_008f seed 1 peak: 1.02$\\times$@25K; exp\\_009c seed 2 peak: 1.26$\\times$@25K).\n\n- **$0.8 \\leq \\hat{r}_k \\leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.\n\n- **$\\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.\n\n**Temporal validity constraint.** The NVE threshold applies only at $k \\geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\\_009b at 25K shows NVE = 2.05$\\times$ and exp\\_008e\\_v3 at 25K shows NVE = 1.93$\\times$, both artifacts of the baseline's $r_{25\\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.\n\n**Aggregate diagnostic power.** Evaluating the 1.5$\\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\\ref{tab:nve_sensitivity}). The single false positive is exp\\_008e\\_v3\\_s2, which exhibits late-onset NVE = 3.78$\\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \\S3.3. At a stricter threshold of 1.7$\\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).\n\n### Properties of the NVE Metric\n\nTwo properties make NVE informative for detecting the CIVO:\n\n**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\\_008d shows NVE = 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K $\\to$ 4.12$\\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\\_008a, exp\\_008f) show stable or declining NVE trajectories.\n\n**Collapse association.** Sustained NVE $>$ 1.5$\\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\\_008d seed 1: three consecutive checkpoints above 1.5$\\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\\_009b seed 2: 1.62$\\times$@45K $\\to$ 1.41$\\times$@55K $\\to$ 0.94$\\times$@65K, declining) does not lead to collapse. This pattern is consistent with a \"point of no return\" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.\n\n\n## 3.3 Causal Analysis Protocol\n\n### Design Rationale\n\nThis is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.\n\n### Factorial Structure\n\nWe vary three factors (temporal embedding type $\\times$ subsampling $\\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \\S4 for the complete configuration matrix). Rather than filling all cells of the $3 \\times 2 \\times 2$ grid, we prioritize the comparisons most informative for causal isolation.\n\n### Causal Chain and Its Tests\n\nThe causal chain under investigation is:\n\n$$\\text{trained } e_{\\Delta t} \\;\\xrightarrow{\\text{Link 1}}\\; \\text{pathological NVE} \\;\\xrightarrow{\\text{Link 2}}\\; \\text{actor exploitation} \\;\\xrightarrow{\\text{Link 3}}\\; \\text{performance collapse}$$\n\nEach link is tested by a specific controlled comparison:\n\n**Link 1: Trained dt\\_embedding $\\to$ pathological overestimation.** The comparison between exp\\_008d (trained dt\\_embedding, $d{=}32$) and exp\\_008f (removed dt\\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\\Delta t{=}2$ imagination). Exp\\_008d exhibits accelerating NVE (1.71$\\times$@35K $\\to$ 2.09$\\times$@45K), while exp\\_008f remains in the normal range (0.73$\\times$@35K $\\to$ 0.83$\\times$@45K). This is the primary causal evidence.\n\n**Link 2: Sustained overestimation $\\to$ collapse (stochastic).** Multi-seed replication of exp\\_008d reveals that the NVE $>$ 1.5$\\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\\_008d) shows sustained NVE $>$ 1.5$\\times$ across three checkpoints and collapses; seed 2 (exp\\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.\n\n**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n### 2$\\times$2 Ablation Matrix\n\nTo close the causal loop, we cross dt\\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:\n\n| dt\\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |\n|:---:|:---:|:---:|:---:|:---:|\n| Trained ($d{=}32$) | ON | 008d | 4.12$\\times$@55K (sustained $\\uparrow$) | CIVO $\\to$ collapse |\n| Trained ($d{=}32$) | OFF | 008a | 0.93$\\times$@55K | Stable, 85\\% baseline@105K |\n| Frozen ($d{=}32$) | ON | 015b | 1.45$\\times$@55K $\\to$ 0.65$\\times$@65K | Sub-threshold transient; gradient starvation collapse |\n| Removed ($d{=}0$) | ON | 008f | $\\leq$1.02$\\times$ | No CIVO |\n\nTrained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\\_015b: peak 1.45$\\times$@55K) that self-corrects to 0.65$\\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\\times$. The subsample-OFF condition (exp\\_008a) confirms that a trained embedding without exposure to $\\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.\n\n### Supporting Analyses\n\n**Horizon effect (C5).** Exp\\_008c ($H{=}8$) vs. exp\\_008a ($H{=}15$), both with trained-but-unexposed dt\\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\\_008a: 778@105K; exp\\_008c: 241@65K plateau).\n\n**Temporal distance amplification (C4).** Exp\\_006 ($\\Delta t{=}2$, peak 485@35K $\\to$ collapse) vs. exp\\_007 ($\\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\\Delta t$, consistent with compounding RSSM prediction errors. Only two $\\Delta t$ values are tested; we report the monotonic trend (dt=1 $\\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.\n\n### RSSM Fidelity Analysis\n\nTo ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\\Delta t{=}1$ vs. $\\Delta t{=}2$ across three conditions (exp\\_rssm\\_fidelity\\_analysis):\n\n| Condition | $\\Delta t{=}1$ obs MSE | $\\Delta t{=}2$ obs MSE | Obs gap | $\\Delta t{=}1$ rew MAE | $\\Delta t{=}2$ rew MAE | Rew gap |\n|-----------|:---:|:---:|:---:|:---:|:---:|:---:|\n| Baseline (exp\\_001) | 13.49 | 27.50 | 2.04$\\times$ | 0.0102 | 0.0159 | 1.56$\\times$ |\n| 008d (trained emb) | 41.31 | 53.67 | 1.30$\\times$ | 0.0568 | 0.1579 | 2.78$\\times$ |\n| 008f (no emb) | 8.01 | 22.04 | 2.75$\\times$ | 0.7469 | 0.7526 | 1.01$\\times$ |\n\nTwo patterns are diagnostically relevant:\n\n1. **Trained embedding enables differentiated but biased reward predictions.** In exp\\_008d, the reward head produces sharply different predictions for $\\Delta t{=}1$ vs. $\\Delta t{=}2$ (reward gap 2.78$\\times$), but these differentiated predictions rest on poor absolute state quality ($\\Delta t{=}1$ obs MSE = 41.31, 3.1$\\times$ baseline). The critic receives confident but systematically biased reward signals at $\\Delta t{=}2$, fueling value overestimation.\n\n2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\\_008f, the reward head cannot distinguish $\\Delta t$ values (gap 1.01$\\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\\times$ baseline). Exp\\_008f is therefore a *causal control* that confirms the dt\\_embedding's role in overestimation, not a recommended configuration.\n\n**Caveat on obs gap ratios.** Exp\\_008d's low obs gap ratio (1.30$\\times$) is misleading---its $\\Delta t{=}1$ absolute error is already 3.1$\\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.\n\n### Gradient Decomposition of the Temporal Embedding\n\\label{sec:gradient_decomposition}\n\nTo identify which loss component drives $e_{\\Delta t}$'s learned representation, we decompose $\\nabla_\\theta e_{\\Delta t}$ by loss term using \\texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061). DreamerV3's joint loss \\citep{hafner2023dreamerv3} sums observation reconstruction, reward prediction, continuation, and KL regularization terms; each backpropagates through the shared RSSM latent state to reach $e_{\\Delta t}$.\n\n| Loss component | Gradient norm | Share (\\%) |\n|----------------|:---:|:---:|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93 |\n| KL dynamics | 0.119 | 7 |\n| Continuation head | $<$0.001 | $<$1 |\n| Reward head | 0.000 | 0 |\n\nThe temporal embedding receives 93\\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). This gradient imbalance is consistent with findings that observation reconstruction dominates reward learning in DreamerV3-type world models \\citep{shang2024harmonydream}, and represents an extreme instance of multi-task gradient magnitude imbalance \\citep{chen2018gradnorm}. Three implications follow:\n\n1. **Exp\\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.\n\n2. **$e_{\\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.\n\n3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\\% contribution from observation decoders. This motivates the full SGS design (exp\\_018), which detaches $e_{\\Delta t}$ from all non-KL gradient pathways.\n\n### Stop-Gradient Surgery: An Informative Negative (exp\\_016e)\n\\label{sec:sgs_negative}\n\nThe gradient decomposition above was motivated by a null result: exp\\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\\Delta t}$.\n\n**Configuration.** Exp\\_016e replicates exp\\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\\Delta t}$, subsampling ON, $H{=}8$, $\\Delta t{=}2$ imagination) with one modification: \\texttt{reward\\_dt\\_emb\\_detach=True}, which applies $\\text{sg}(\\cdot)$ to $e_{\\Delta t}$ before the reward head during the backward pass.\n\n**Results.** Exp\\_016e collapses in the same qualitative pattern as exp\\_008d. Peak eval return reaches 326.7 at 75K (exp\\_016e), then drops to 31.7 by 95K---a 90.3\\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\\times$ at 95K (exp\\_016e). The timing difference relative to exp\\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.\n\n**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\\ 1 scalar reward) dominates the gradient signal to $e_{\\Delta t}$ by two orders of magnitude.\n\n**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.\n\n### Imagination Step Size as Causal Variable\n\nThe factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:\n\n**$\\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\\_008e\\_v3 uses the same trained dt\\_embedding and multi-rate training data as exp\\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95\\% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n**$\\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\\_008e\\_v3\\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\\_008e\\_v3\\_s2), with NVE = 3.78$\\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\\_008e\\_v3\\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\\_008d.\n\n**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:\n\n- *Pathway A (CIVO):* Trained dt\\_embedding + $\\Delta t{>}1$ imagination $\\to$ value overestimation (NVE $\\uparrow$) $\\to$ actor over-exploitation (entropy $\\downarrow$) $\\to$ performance collapse. Observed in exp\\_008d (seed 1) and exp\\_009b (seed 2, transient).\n\n- *Pathway B (non-CIVO):* $\\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\\_008e\\_v3\\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.\n\nTo rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\\_009a), comparable to seed 1's 915.67 (exp\\_001\\_baseline). The collapse in exp\\_008e\\_v3\\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.\n\n**Implication.** Restricting imagination to $\\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.\n",
    "structuredPatch": [
      {
        "oldStart": 108,
        "oldLines": 7,
        "newStart": 108,
        "newLines": 7,
        "lines": [
          " ",
          " **Link 2: Sustained overestimation $\\to$ collapse (stochastic).** Multi-seed replication of exp\\_008d reveals that the NVE $>$ 1.5$\\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\\_008d) shows sustained NVE $>$ 1.5$\\times$ across three checkpoints and collapses; seed 2 (exp\\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.",
          " ",
          "-**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.",
          "+**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises specifically when the actor-critic exploits the embedding's $\\Delta t > 1$ predictions during imagination.",
          " ",
          " ### 2$\\times$2 Ablation Matrix",
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_012DKbU8PdNeHSqWrFGj9ntY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md",
  "old_string": "Trained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints).",
  "new_string": "A trained dt\\_embedding is necessary for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints), though not independently sufficient---multi-rate training data exposure is jointly required."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "25201a9e-e3a2-4e36-bbb1-3a73d4cdf906",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V54jiNVxjBmLXbjUEkzwbF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7082,
      "cache_read_input_tokens": 49491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7082
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

_source line 28 · 2026-05-16T16:29:03.562Z_

<details><summary>↩ Tool result · `toolu_012DKbU8PdNeHSqWrFGj9ntY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "1608f349-e596-4b31-b218-761b1d32640a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md",
    "oldString": "Trained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints).",
    "newString": "A trained dt\\_embedding is necessary for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints), though not independently sufficient---multi-rate training data exposure is jointly required.",
    "originalFile": "% Method — Draft v2\n% Target: CoRL 2026\n% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8).\n% Note: Complements experimental_setup.md (Section 4). Some overlap in\n%   diagnostic framework and factorial design is intentional—final paper\n%   may merge or redistribute content between Sections 3 and 4.\n\n# 3. Methodology\n\nWe present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \\citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \\citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.\n\n\n## 3.1 Background: DreamerV3 and Variable-Rate Imagination\n\n### World-Model Actor-Critic\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:\n\n$$h_{t+1} = f_\\theta(h_t, z_t, a_t), \\quad \\hat{z}_{t+1} \\sim p_\\theta(\\cdot \\mid h_{t+1})$$\n\nAn actor $\\pi_\\psi$ selects actions and a critic $V_\\xi$ estimates $\\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\\Delta t = 1$) and $H = 15$.\n\n### Temporal Abstraction via Variable-Rate Imagination\n\nTemporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \\citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.\n\nWe introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:\n\n**Temporal step-size embedding.** An embedding $e_{\\Delta t} \\in \\mathbb{R}^d$ conditions the RSSM transition on the step size:\n\n$$h_{t+\\Delta t} = f_\\theta(h_t, z_t, a_t, e_{\\Delta t})$$\n\nWe study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\\Delta t$ values; the untrained and removed configurations serve as controls.\n\n**Temporal subsampling.** When enabled, the replay buffer stores both $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\\Delta t{=}1$ transitions are used for world-model training.\n\n**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\\Delta t{=}1$ (standard) or $\\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.\n\n### Conditioning-Induced Value Overestimation (CIVO)\n\nWhen the RSSM predicts $\\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\\xi$ receives precise $\\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.\n\nWe term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \\& Schuurmans' \\citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\\Delta t}$ and the RSSM's degraded fidelity at $\\Delta t > 1$, not the policy's representational capacity.\n\n\n## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio\n\n### Motivation\n\nDistinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\\_001\\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.\n\n### Definition\n\n**Value-evaluation ratio.** At training step $k$:\n\n$$r_k = \\frac{\\bar{v}_k}{\\bar{R}_k}$$\n\nwhere $\\bar{v}_k$ is the mean predicted value across imagined states and $\\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.\n\n**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:\n\n$$\\hat{r}_k = \\frac{r_k^{\\,\\text{exp}}}{r_k^{\\,\\text{baseline}}}$$\n\nThis removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.\n\n### Diagnostic Thresholds\n\nWe calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:\n\n- **$\\hat{r}_k > 1.5$ (at $k \\geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\\_embedding conditions exceed 1.5$\\times$ at 35K+ steps (exp\\_008d seed 1: 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K; exp\\_009b seed 2: 1.62$\\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\\_008f seed 1 peak: 1.02$\\times$@25K; exp\\_009c seed 2 peak: 1.26$\\times$@25K).\n\n- **$0.8 \\leq \\hat{r}_k \\leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.\n\n- **$\\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.\n\n**Temporal validity constraint.** The NVE threshold applies only at $k \\geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\\_009b at 25K shows NVE = 2.05$\\times$ and exp\\_008e\\_v3 at 25K shows NVE = 1.93$\\times$, both artifacts of the baseline's $r_{25\\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.\n\n**Aggregate diagnostic power.** Evaluating the 1.5$\\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\\ref{tab:nve_sensitivity}). The single false positive is exp\\_008e\\_v3\\_s2, which exhibits late-onset NVE = 3.78$\\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \\S3.3. At a stricter threshold of 1.7$\\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).\n\n### Properties of the NVE Metric\n\nTwo properties make NVE informative for detecting the CIVO:\n\n**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\\_008d shows NVE = 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K $\\to$ 4.12$\\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\\_008a, exp\\_008f) show stable or declining NVE trajectories.\n\n**Collapse association.** Sustained NVE $>$ 1.5$\\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\\_008d seed 1: three consecutive checkpoints above 1.5$\\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\\_009b seed 2: 1.62$\\times$@45K $\\to$ 1.41$\\times$@55K $\\to$ 0.94$\\times$@65K, declining) does not lead to collapse. This pattern is consistent with a \"point of no return\" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.\n\n\n## 3.3 Causal Analysis Protocol\n\n### Design Rationale\n\nThis is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.\n\n### Factorial Structure\n\nWe vary three factors (temporal embedding type $\\times$ subsampling $\\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \\S4 for the complete configuration matrix). Rather than filling all cells of the $3 \\times 2 \\times 2$ grid, we prioritize the comparisons most informative for causal isolation.\n\n### Causal Chain and Its Tests\n\nThe causal chain under investigation is:\n\n$$\\text{trained } e_{\\Delta t} \\;\\xrightarrow{\\text{Link 1}}\\; \\text{pathological NVE} \\;\\xrightarrow{\\text{Link 2}}\\; \\text{actor exploitation} \\;\\xrightarrow{\\text{Link 3}}\\; \\text{performance collapse}$$\n\nEach link is tested by a specific controlled comparison:\n\n**Link 1: Trained dt\\_embedding $\\to$ pathological overestimation.** The comparison between exp\\_008d (trained dt\\_embedding, $d{=}32$) and exp\\_008f (removed dt\\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\\Delta t{=}2$ imagination). Exp\\_008d exhibits accelerating NVE (1.71$\\times$@35K $\\to$ 2.09$\\times$@45K), while exp\\_008f remains in the normal range (0.73$\\times$@35K $\\to$ 0.83$\\times$@45K). This is the primary causal evidence.\n\n**Link 2: Sustained overestimation $\\to$ collapse (stochastic).** Multi-seed replication of exp\\_008d reveals that the NVE $>$ 1.5$\\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\\_008d) shows sustained NVE $>$ 1.5$\\times$ across three checkpoints and collapses; seed 2 (exp\\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.\n\n**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises specifically when the actor-critic exploits the embedding's $\\Delta t > 1$ predictions during imagination.\n\n### 2$\\times$2 Ablation Matrix\n\nTo close the causal loop, we cross dt\\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:\n\n| dt\\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |\n|:---:|:---:|:---:|:---:|:---:|\n| Trained ($d{=}32$) | ON | 008d | 4.12$\\times$@55K (sustained $\\uparrow$) | CIVO $\\to$ collapse |\n| Trained ($d{=}32$) | OFF | 008a | 0.93$\\times$@55K | Stable, 85\\% baseline@105K |\n| Frozen ($d{=}32$) | ON | 015b | 1.45$\\times$@55K $\\to$ 0.65$\\times$@65K | Sub-threshold transient; gradient starvation collapse |\n| Removed ($d{=}0$) | ON | 008f | $\\leq$1.02$\\times$ | No CIVO |\n\nTrained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\\_015b: peak 1.45$\\times$@55K) that self-corrects to 0.65$\\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\\times$. The subsample-OFF condition (exp\\_008a) confirms that a trained embedding without exposure to $\\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.\n\n### Supporting Analyses\n\n**Horizon effect (C5).** Exp\\_008c ($H{=}8$) vs. exp\\_008a ($H{=}15$), both with trained-but-unexposed dt\\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\\_008a: 778@105K; exp\\_008c: 241@65K plateau).\n\n**Temporal distance amplification (C4).** Exp\\_006 ($\\Delta t{=}2$, peak 485@35K $\\to$ collapse) vs. exp\\_007 ($\\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\\Delta t$, consistent with compounding RSSM prediction errors. Only two $\\Delta t$ values are tested; we report the monotonic trend (dt=1 $\\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.\n\n### RSSM Fidelity Analysis\n\nTo ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\\Delta t{=}1$ vs. $\\Delta t{=}2$ across three conditions (exp\\_rssm\\_fidelity\\_analysis):\n\n| Condition | $\\Delta t{=}1$ obs MSE | $\\Delta t{=}2$ obs MSE | Obs gap | $\\Delta t{=}1$ rew MAE | $\\Delta t{=}2$ rew MAE | Rew gap |\n|-----------|:---:|:---:|:---:|:---:|:---:|:---:|\n| Baseline (exp\\_001) | 13.49 | 27.50 | 2.04$\\times$ | 0.0102 | 0.0159 | 1.56$\\times$ |\n| 008d (trained emb) | 41.31 | 53.67 | 1.30$\\times$ | 0.0568 | 0.1579 | 2.78$\\times$ |\n| 008f (no emb) | 8.01 | 22.04 | 2.75$\\times$ | 0.7469 | 0.7526 | 1.01$\\times$ |\n\nTwo patterns are diagnostically relevant:\n\n1. **Trained embedding enables differentiated but biased reward predictions.** In exp\\_008d, the reward head produces sharply different predictions for $\\Delta t{=}1$ vs. $\\Delta t{=}2$ (reward gap 2.78$\\times$), but these differentiated predictions rest on poor absolute state quality ($\\Delta t{=}1$ obs MSE = 41.31, 3.1$\\times$ baseline). The critic receives confident but systematically biased reward signals at $\\Delta t{=}2$, fueling value overestimation.\n\n2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\\_008f, the reward head cannot distinguish $\\Delta t$ values (gap 1.01$\\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\\times$ baseline). Exp\\_008f is therefore a *causal control* that confirms the dt\\_embedding's role in overestimation, not a recommended configuration.\n\n**Caveat on obs gap ratios.** Exp\\_008d's low obs gap ratio (1.30$\\times$) is misleading---its $\\Delta t{=}1$ absolute error is already 3.1$\\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.\n\n### Gradient Decomposition of the Temporal Embedding\n\\label{sec:gradient_decomposition}\n\nTo identify which loss component drives $e_{\\Delta t}$'s learned representation, we decompose $\\nabla_\\theta e_{\\Delta t}$ by loss term using \\texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061). DreamerV3's joint loss \\citep{hafner2023dreamerv3} sums observation reconstruction, reward prediction, continuation, and KL regularization terms; each backpropagates through the shared RSSM latent state to reach $e_{\\Delta t}$.\n\n| Loss component | Gradient norm | Share (\\%) |\n|----------------|:---:|:---:|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93 |\n| KL dynamics | 0.119 | 7 |\n| Continuation head | $<$0.001 | $<$1 |\n| Reward head | 0.000 | 0 |\n\nThe temporal embedding receives 93\\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). This gradient imbalance is consistent with findings that observation reconstruction dominates reward learning in DreamerV3-type world models \\citep{shang2024harmonydream}, and represents an extreme instance of multi-task gradient magnitude imbalance \\citep{chen2018gradnorm}. Three implications follow:\n\n1. **Exp\\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.\n\n2. **$e_{\\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.\n\n3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\\% contribution from observation decoders. This motivates the full SGS design (exp\\_018), which detaches $e_{\\Delta t}$ from all non-KL gradient pathways.\n\n### Stop-Gradient Surgery: An Informative Negative (exp\\_016e)\n\\label{sec:sgs_negative}\n\nThe gradient decomposition above was motivated by a null result: exp\\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\\Delta t}$.\n\n**Configuration.** Exp\\_016e replicates exp\\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\\Delta t}$, subsampling ON, $H{=}8$, $\\Delta t{=}2$ imagination) with one modification: \\texttt{reward\\_dt\\_emb\\_detach=True}, which applies $\\text{sg}(\\cdot)$ to $e_{\\Delta t}$ before the reward head during the backward pass.\n\n**Results.** Exp\\_016e collapses in the same qualitative pattern as exp\\_008d. Peak eval return reaches 326.7 at 75K (exp\\_016e), then drops to 31.7 by 95K---a 90.3\\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\\times$ at 95K (exp\\_016e). The timing difference relative to exp\\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.\n\n**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\\ 1 scalar reward) dominates the gradient signal to $e_{\\Delta t}$ by two orders of magnitude.\n\n**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.\n\n### Imagination Step Size as Causal Variable\n\nThe factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:\n\n**$\\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\\_008e\\_v3 uses the same trained dt\\_embedding and multi-rate training data as exp\\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95\\% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n**$\\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\\_008e\\_v3\\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\\_008e\\_v3\\_s2), with NVE = 3.78$\\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\\_008e\\_v3\\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\\_008d.\n\n**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:\n\n- *Pathway A (CIVO):* Trained dt\\_embedding + $\\Delta t{>}1$ imagination $\\to$ value overestimation (NVE $\\uparrow$) $\\to$ actor over-exploitation (entropy $\\downarrow$) $\\to$ performance collapse. Observed in exp\\_008d (seed 1) and exp\\_009b (seed 2, transient).\n\n- *Pathway B (non-CIVO):* $\\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\\_008e\\_v3\\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.\n\nTo rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\\_009a), comparable to seed 1's 915.67 (exp\\_001\\_baseline). The collapse in exp\\_008e\\_v3\\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.\n\n**Implication.** Restricting imagination to $\\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.\n",
    "structuredPatch": [
      {
        "oldStart": 121,
        "oldLines": 7,
        "newStart": 121,
        "newLines": 7,
        "lines": [
          " | Frozen ($d{=}32$) | ON | 015b | 1.45$\\times$@55K $\\to$ 0.65$\\times$@65K | Sub-threshold transient; gradient starvation collapse |",
          " | Removed ($d{=}0$) | ON | 008f | $\\leq$1.02$\\times$ | No CIVO |",
          " ",
          "-Trained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\\_015b: peak 1.45$\\times$@55K) that self-corrects to 0.65$\\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\\times$. The subsample-OFF condition (exp\\_008a) confirms that a trained embedding without exposure to $\\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.",
          "+A trained dt\\_embedding is necessary for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints), though not independently sufficient---multi-rate training data exposure is jointly required. Frozen embedding produces sub-threshold transient overestimation (exp\\_015b: peak 1.45$\\times$@55K) that self-corrects to 0.65$\\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\\times$. The subsample-OFF condition (exp\\_008a) confirms that a trained embedding without exposure to $\\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.",
          " ",
          " ### Supporting Analyses",
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_01BFmSit1bNKezafWPckYUTU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md",
  "old_string": "The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.",
  "new_string": "The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "2c3fa197-1c90-4ede-8515-32de88639c8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V54jiNVxjBmLXbjUEkzwbF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7082,
      "cache_read_input_tokens": 49491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7082
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

_source line 30 · 2026-05-16T16:29:05.108Z_

<details><summary>↩ Tool result · `toolu_01BFmSit1bNKezafWPckYUTU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "adf74a51-9ebf-475d-b616-3484337e22a0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md",
    "oldString": "The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.",
    "newString": "The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.",
    "originalFile": "% Method — Draft v2\n% Target: CoRL 2026\n% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8).\n% Note: Complements experimental_setup.md (Section 4). Some overlap in\n%   diagnostic framework and factorial design is intentional—final paper\n%   may merge or redistribute content between Sections 3 and 4.\n\n# 3. Methodology\n\nWe present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \\citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \\citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.\n\n\n## 3.1 Background: DreamerV3 and Variable-Rate Imagination\n\n### World-Model Actor-Critic\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:\n\n$$h_{t+1} = f_\\theta(h_t, z_t, a_t), \\quad \\hat{z}_{t+1} \\sim p_\\theta(\\cdot \\mid h_{t+1})$$\n\nAn actor $\\pi_\\psi$ selects actions and a critic $V_\\xi$ estimates $\\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\\Delta t = 1$) and $H = 15$.\n\n### Temporal Abstraction via Variable-Rate Imagination\n\nTemporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \\citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.\n\nWe introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:\n\n**Temporal step-size embedding.** An embedding $e_{\\Delta t} \\in \\mathbb{R}^d$ conditions the RSSM transition on the step size:\n\n$$h_{t+\\Delta t} = f_\\theta(h_t, z_t, a_t, e_{\\Delta t})$$\n\nWe study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\\Delta t$ values; the untrained and removed configurations serve as controls.\n\n**Temporal subsampling.** When enabled, the replay buffer stores both $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\\Delta t{=}1$ transitions are used for world-model training.\n\n**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\\Delta t{=}1$ (standard) or $\\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.\n\n### Conditioning-Induced Value Overestimation (CIVO)\n\nWhen the RSSM predicts $\\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\\xi$ receives precise $\\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.\n\nWe term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \\& Schuurmans' \\citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\\Delta t}$ and the RSSM's degraded fidelity at $\\Delta t > 1$, not the policy's representational capacity.\n\n\n## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio\n\n### Motivation\n\nDistinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\\_001\\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.\n\n### Definition\n\n**Value-evaluation ratio.** At training step $k$:\n\n$$r_k = \\frac{\\bar{v}_k}{\\bar{R}_k}$$\n\nwhere $\\bar{v}_k$ is the mean predicted value across imagined states and $\\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.\n\n**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:\n\n$$\\hat{r}_k = \\frac{r_k^{\\,\\text{exp}}}{r_k^{\\,\\text{baseline}}}$$\n\nThis removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.\n\n### Diagnostic Thresholds\n\nWe calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:\n\n- **$\\hat{r}_k > 1.5$ (at $k \\geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\\_embedding conditions exceed 1.5$\\times$ at 35K+ steps (exp\\_008d seed 1: 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K; exp\\_009b seed 2: 1.62$\\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\\_008f seed 1 peak: 1.02$\\times$@25K; exp\\_009c seed 2 peak: 1.26$\\times$@25K).\n\n- **$0.8 \\leq \\hat{r}_k \\leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.\n\n- **$\\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.\n\n**Temporal validity constraint.** The NVE threshold applies only at $k \\geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\\_009b at 25K shows NVE = 2.05$\\times$ and exp\\_008e\\_v3 at 25K shows NVE = 1.93$\\times$, both artifacts of the baseline's $r_{25\\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.\n\n**Aggregate diagnostic power.** Evaluating the 1.5$\\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\\ref{tab:nve_sensitivity}). The single false positive is exp\\_008e\\_v3\\_s2, which exhibits late-onset NVE = 3.78$\\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \\S3.3. At a stricter threshold of 1.7$\\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).\n\n### Properties of the NVE Metric\n\nTwo properties make NVE informative for detecting the CIVO:\n\n**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\\_008d shows NVE = 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K $\\to$ 4.12$\\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\\_008a, exp\\_008f) show stable or declining NVE trajectories.\n\n**Collapse association.** Sustained NVE $>$ 1.5$\\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\\_008d seed 1: three consecutive checkpoints above 1.5$\\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\\_009b seed 2: 1.62$\\times$@45K $\\to$ 1.41$\\times$@55K $\\to$ 0.94$\\times$@65K, declining) does not lead to collapse. This pattern is consistent with a \"point of no return\" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.\n\n\n## 3.3 Causal Analysis Protocol\n\n### Design Rationale\n\nThis is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.\n\n### Factorial Structure\n\nWe vary three factors (temporal embedding type $\\times$ subsampling $\\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \\S4 for the complete configuration matrix). Rather than filling all cells of the $3 \\times 2 \\times 2$ grid, we prioritize the comparisons most informative for causal isolation.\n\n### Causal Chain and Its Tests\n\nThe causal chain under investigation is:\n\n$$\\text{trained } e_{\\Delta t} \\;\\xrightarrow{\\text{Link 1}}\\; \\text{pathological NVE} \\;\\xrightarrow{\\text{Link 2}}\\; \\text{actor exploitation} \\;\\xrightarrow{\\text{Link 3}}\\; \\text{performance collapse}$$\n\nEach link is tested by a specific controlled comparison:\n\n**Link 1: Trained dt\\_embedding $\\to$ pathological overestimation.** The comparison between exp\\_008d (trained dt\\_embedding, $d{=}32$) and exp\\_008f (removed dt\\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\\Delta t{=}2$ imagination). Exp\\_008d exhibits accelerating NVE (1.71$\\times$@35K $\\to$ 2.09$\\times$@45K), while exp\\_008f remains in the normal range (0.73$\\times$@35K $\\to$ 0.83$\\times$@45K). This is the primary causal evidence.\n\n**Link 2: Sustained overestimation $\\to$ collapse (stochastic).** Multi-seed replication of exp\\_008d reveals that the NVE $>$ 1.5$\\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\\_008d) shows sustained NVE $>$ 1.5$\\times$ across three checkpoints and collapses; seed 2 (exp\\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.\n\n**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises specifically when the actor-critic exploits the embedding's $\\Delta t > 1$ predictions during imagination.\n\n### 2$\\times$2 Ablation Matrix\n\nTo close the causal loop, we cross dt\\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:\n\n| dt\\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |\n|:---:|:---:|:---:|:---:|:---:|\n| Trained ($d{=}32$) | ON | 008d | 4.12$\\times$@55K (sustained $\\uparrow$) | CIVO $\\to$ collapse |\n| Trained ($d{=}32$) | OFF | 008a | 0.93$\\times$@55K | Stable, 85\\% baseline@105K |\n| Frozen ($d{=}32$) | ON | 015b | 1.45$\\times$@55K $\\to$ 0.65$\\times$@65K | Sub-threshold transient; gradient starvation collapse |\n| Removed ($d{=}0$) | ON | 008f | $\\leq$1.02$\\times$ | No CIVO |\n\nA trained dt\\_embedding is necessary for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints), though not independently sufficient---multi-rate training data exposure is jointly required. Frozen embedding produces sub-threshold transient overestimation (exp\\_015b: peak 1.45$\\times$@55K) that self-corrects to 0.65$\\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\\times$. The subsample-OFF condition (exp\\_008a) confirms that a trained embedding without exposure to $\\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.\n\n### Supporting Analyses\n\n**Horizon effect (C5).** Exp\\_008c ($H{=}8$) vs. exp\\_008a ($H{=}15$), both with trained-but-unexposed dt\\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\\_008a: 778@105K; exp\\_008c: 241@65K plateau).\n\n**Temporal distance amplification (C4).** Exp\\_006 ($\\Delta t{=}2$, peak 485@35K $\\to$ collapse) vs. exp\\_007 ($\\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\\Delta t$, consistent with compounding RSSM prediction errors. Only two $\\Delta t$ values are tested; we report the monotonic trend (dt=1 $\\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.\n\n### RSSM Fidelity Analysis\n\nTo ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\\Delta t{=}1$ vs. $\\Delta t{=}2$ across three conditions (exp\\_rssm\\_fidelity\\_analysis):\n\n| Condition | $\\Delta t{=}1$ obs MSE | $\\Delta t{=}2$ obs MSE | Obs gap | $\\Delta t{=}1$ rew MAE | $\\Delta t{=}2$ rew MAE | Rew gap |\n|-----------|:---:|:---:|:---:|:---:|:---:|:---:|\n| Baseline (exp\\_001) | 13.49 | 27.50 | 2.04$\\times$ | 0.0102 | 0.0159 | 1.56$\\times$ |\n| 008d (trained emb) | 41.31 | 53.67 | 1.30$\\times$ | 0.0568 | 0.1579 | 2.78$\\times$ |\n| 008f (no emb) | 8.01 | 22.04 | 2.75$\\times$ | 0.7469 | 0.7526 | 1.01$\\times$ |\n\nTwo patterns are diagnostically relevant:\n\n1. **Trained embedding enables differentiated but biased reward predictions.** In exp\\_008d, the reward head produces sharply different predictions for $\\Delta t{=}1$ vs. $\\Delta t{=}2$ (reward gap 2.78$\\times$), but these differentiated predictions rest on poor absolute state quality ($\\Delta t{=}1$ obs MSE = 41.31, 3.1$\\times$ baseline). The critic receives confident but systematically biased reward signals at $\\Delta t{=}2$, fueling value overestimation.\n\n2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\\_008f, the reward head cannot distinguish $\\Delta t$ values (gap 1.01$\\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\\times$ baseline). Exp\\_008f is therefore a *causal control* that confirms the dt\\_embedding's role in overestimation, not a recommended configuration.\n\n**Caveat on obs gap ratios.** Exp\\_008d's low obs gap ratio (1.30$\\times$) is misleading---its $\\Delta t{=}1$ absolute error is already 3.1$\\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.\n\n### Gradient Decomposition of the Temporal Embedding\n\\label{sec:gradient_decomposition}\n\nTo identify which loss component drives $e_{\\Delta t}$'s learned representation, we decompose $\\nabla_\\theta e_{\\Delta t}$ by loss term using \\texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061). DreamerV3's joint loss \\citep{hafner2023dreamerv3} sums observation reconstruction, reward prediction, continuation, and KL regularization terms; each backpropagates through the shared RSSM latent state to reach $e_{\\Delta t}$.\n\n| Loss component | Gradient norm | Share (\\%) |\n|----------------|:---:|:---:|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93 |\n| KL dynamics | 0.119 | 7 |\n| Continuation head | $<$0.001 | $<$1 |\n| Reward head | 0.000 | 0 |\n\nThe temporal embedding receives 93\\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). This gradient imbalance is consistent with findings that observation reconstruction dominates reward learning in DreamerV3-type world models \\citep{shang2024harmonydream}, and represents an extreme instance of multi-task gradient magnitude imbalance \\citep{chen2018gradnorm}. Three implications follow:\n\n1. **Exp\\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.\n\n2. **$e_{\\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.\n\n3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\\% contribution from observation decoders. This motivates the full SGS design (exp\\_018), which detaches $e_{\\Delta t}$ from all non-KL gradient pathways.\n\n### Stop-Gradient Surgery: An Informative Negative (exp\\_016e)\n\\label{sec:sgs_negative}\n\nThe gradient decomposition above was motivated by a null result: exp\\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\\Delta t}$.\n\n**Configuration.** Exp\\_016e replicates exp\\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\\Delta t}$, subsampling ON, $H{=}8$, $\\Delta t{=}2$ imagination) with one modification: \\texttt{reward\\_dt\\_emb\\_detach=True}, which applies $\\text{sg}(\\cdot)$ to $e_{\\Delta t}$ before the reward head during the backward pass.\n\n**Results.** Exp\\_016e collapses in the same qualitative pattern as exp\\_008d. Peak eval return reaches 326.7 at 75K (exp\\_016e), then drops to 31.7 by 95K---a 90.3\\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\\times$ at 95K (exp\\_016e). The timing difference relative to exp\\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.\n\n**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\\ 1 scalar reward) dominates the gradient signal to $e_{\\Delta t}$ by two orders of magnitude.\n\n**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.\n\n### Imagination Step Size as Causal Variable\n\nThe factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:\n\n**$\\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\\_008e\\_v3 uses the same trained dt\\_embedding and multi-rate training data as exp\\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95\\% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n**$\\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\\_008e\\_v3\\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\\_008e\\_v3\\_s2), with NVE = 3.78$\\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\\_008e\\_v3\\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\\_008d.\n\n**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:\n\n- *Pathway A (CIVO):* Trained dt\\_embedding + $\\Delta t{>}1$ imagination $\\to$ value overestimation (NVE $\\uparrow$) $\\to$ actor over-exploitation (entropy $\\downarrow$) $\\to$ performance collapse. Observed in exp\\_008d (seed 1) and exp\\_009b (seed 2, transient).\n\n- *Pathway B (non-CIVO):* $\\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\\_008e\\_v3\\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.\n\nTo rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\\_009a), comparable to seed 1's 915.67 (exp\\_001\\_baseline). The collapse in exp\\_008e\\_v3\\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.\n\n**Implication.** Restricting imagination to $\\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.\n",
    "structuredPatch": [
      {
        "oldStart": 184,
        "oldLines": 7,
        "newStart": 184,
        "newLines": 7,
        "lines": [
          " ",
          " The factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:",
          " ",
          "-**$\\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\\_008e\\_v3 uses the same trained dt\\_embedding and multi-rate training data as exp\\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95\\% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.",
          "+**$\\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\\_008e\\_v3 uses the same trained dt\\_embedding and multi-rate training data as exp\\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95\\% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). The trained embedding does not trigger CIVO when imagination is restricted to $\\Delta t{=}1$; the pathological overestimation arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.",
          " ",
          " **$\\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\\_008e\\_v3\\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\\_008e\\_v3\\_s2), with NVE = 3.78$\\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\\_008e\\_v3\\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\\_008d.",
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

_source line 31_

Now registering the audit report artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "39794529-8632-456a-98c4-5fa47d886959",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZtiEcErdA4cwHv4jhi6HG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1966,
      "cache_read_input_tokens": 56573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1966
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

_source line 32_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HKLvEsrrUty4tLWSsLTuuu`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "b3df1eb8-9009-44b6-b136-45e00e8ee385",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZtiEcErdA4cwHv4jhi6HG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1966,
      "cache_read_input_tokens": 56573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1966
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

_source line 33 · 2026-05-16T16:29:14.615Z_

<details><summary>↩ Tool result · `toolu_01HKLvEsrrUty4tLWSsLTuuu`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "ed498e33-98e1-43ab-ae51-7eb1cbede42b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Tf4xFtohfjnR9sMFZKLZDe`</summary>

```json
{
  "name": "D3 Claim Language Audit Report",
  "type": "report",
  "description": "Audit of overly strong claims (necessary-and-sufficient, always, definitively, etc.) across 5 paper files. Found 8 issues: 1 CRITICAL (factually incorrect necessity claim), 3 HIGH (unqualified absolutes contradicted by IRD), 2 MEDIUM (certainty language), 2 LOW. CRITICAL and HIGH fixes applied to results.md and method_framingB_reaudit_v2.md.",
  "project": "event-gated-adaptive-horizon",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/claim_audit_report.md",
  "tags": [
    "paper",
    "audit",
    "D3",
    "claim-language"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "bd439f74-9c8a-4a86-b74c-ac5297fe3e54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDfzW1hKWaLSkAgburZCZH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 58539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
      },
      "output_tokens": 5,
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

_source line 35 · 2026-05-16T16:29:21.714Z_

<details><summary>↩ Tool result · `toolu_01Tf4xFtohfjnR9sMFZKLZDe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_d0e61a\", \"name\": \"D3 Claim Language Audit Report\", \"type\": \"report\", \"description\": \"Audit of overly strong claims (necessary-and-sufficient, always, definitively, etc.) across 5 paper files. Found 8 issues: 1 CRITICAL (factually incorrect necessity claim), 3 HIGH (unqualified absolutes contradicted by IRD), 2 MEDIUM (certainty language), 2 LOW. CRITICAL and HIGH fixes applied to results.md and method_framingB_reaudit_v2.md.\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/claim_audit_report.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:29:21.513502+00:00\", \"tags\": [\"paper\", \"audit\", \"D3\", \"claim-language\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "b8d7a436-723d-407d-b949-0a40314f9320",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_d0e61a\\\", \\\"name\\\": \\\"D3 Claim Language Audit Report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Audit of overly strong claims (necessary-and-sufficient, always, definitively, etc.) across 5 paper files. Found 8 issues: 1 CRITICAL (factually incorrect necessity claim), 3 HIGH (unqualified absolutes contradicted by IRD), 2 MEDIUM (certainty language), 2 LOW. CRITICAL and HIGH fixes applied to results.md and method_framingB_reaudit_v2.md.\\\", \\\"path\\\": \\\"projects/event-gated-adaptive-horizon/artifacts/_project/report/claim_audit_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"event-gated-adaptive-horizon\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T16:29:21.513502+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"audit\\\", \\\"D3\\\", \\\"claim-language\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_d0e61a\", \"name\": \"D3 Claim Language Audit Report\", \"type\": \"report\", \"description\": \"Audit of overly strong claims (necessary-and-sufficient, always, definitively, etc.) across 5 paper files. Found 8 issues: 1 CRITICAL (factually incorrect necessity claim), 3 HIGH (unqualified absolutes contradicted by IRD), 2 MEDIUM (certainty language), 2 LOW. CRITICAL and HIGH fixes applied to results.md and method_framingB_reaudit_v2.md.\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/claim_audit_report.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:29:21.513502+00:00\", \"tags\": [\"paper\", \"audit\", \"D3\", \"claim-language\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

完成。

**审计结果：8 处过强 claim，已修复 5 处（CRITICAL + HIGH）。**

已直接修改的文件：
- **results.md**：(1) "neither necessary nor sufficient" → 修正为 subsample 是必要 co-factor 但非独立充分条件；(2) "definitively rules out" → 去掉 "definitively"
- **method_framingB_reaudit_v2.md**：(1)(2) 两处 "not harmful" 绝对表述 → 改为 "does not trigger CIVO when imagination restricted to dt=1"；(3) "the necessary condition" → "a necessary condition... not independently sufficient"

未修改（仅记录在报告中）：
- `018_prewrite_two_versions.md`："The complete causal mechanism" — 待结果出来选版本时改
- `method_90ca4b.md`：旧版本，同样的 "not harmful" 问题，优先级低
- `results.md` line 73 "reliably induces"：边界可接受（2/2 seeds），标记为 LOW

审计报告：`artifacts/_project/paper/claim_audit_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "uuid": "d675a718-1c0c-406a-9a25-f36ccbbf0315",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HdoFBZnfUawmQStX5ZLYej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 59260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 683
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

_source line 37_

完成。

**审计结果：8 处过强 claim，已修复 5 处（CRITICAL + HIGH）。**

已直接修改的文件：
- **results.md**：(1) "neither necessary nor sufficient" → 修正为 subsample 是必要 co-factor 但非独立充分条件；(2) "definitively rules out" → 去掉 "definitively"
- **method_framingB_reaudit_v2.md**：(1)(2) 两处 "not harmful" 绝对表述 → 改为 "does not trigger CIVO when imagination restricted to dt=1"；(3) "the necessary condition" → "a necessary condition... not independently sufficient"

未修改（仅记录在报告中）：
- `018_prewrite_two_versions.md`："The complete causal mechanism" — 待结果出来选版本时改
- `method_90ca4b.md`：旧版本，同样的 "not harmful" 问题，优先级低
- `results.md` line 73 "reliably induces"：边界可接受（2/2 seeds），标记为 LOW

审计报告：`artifacts/_project/paper/claim_audit_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 201661,
  "duration_api_ms": 202694,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "3af79e7c-7756-4e68-b871-1a15dabb4214",
  "total_cost_usd": 0.692986,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 48102,
    "cache_read_input_tokens": 300035,
    "output_tokens": 9628,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48102,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 324,
        "cache_read_input_tokens": 59260,
        "cache_creation_input_tokens": 683,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 683
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1481,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001576,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 9628,
      "cacheReadInputTokens": 300035,
      "cacheCreationInputTokens": 48102,
      "webSearchRequests": 0,
      "costUSD": 0.69141,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7134f5a6-78b1-46cb-aba5-186f698433fa"
}
```

</details>

---
