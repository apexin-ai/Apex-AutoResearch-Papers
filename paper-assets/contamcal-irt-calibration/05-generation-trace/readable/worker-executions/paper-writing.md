# paper writing

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_writing_20260517T021118.log`
- **Structured JSON:** [`3e8c274514c3b5faeb6d.json`](../../sessions/3e/3e8c274514c3b5faeb6d.json)

## Before a recorded user message

14 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "838cfc76-4058-4342-843b-e830eedc24a9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1778997000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "52f6f1e0-b59f-401c-b3e2-4448cdf262b3",
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current file to see what needs to be replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "uuid": "dd38bd4e-e143-4a0e-93f4-d7b05da7e9ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xH8vRQGAoa68vKuXYvRpT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16454,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16454
      },
      "output_tokens": 38,
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

<details open><summary>🔧 Tool call — Read · `toolu_01VwZusC4z5h7n9Zj3iWjoDD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experiments.tex",
  "offset": 85
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "uuid": "b6ffcd37-825c-43b8-abb8-35951e6f952d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xH8vRQGAoa68vKuXYvRpT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16454,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16454
      },
      "output_tokens": 38,
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

_source line 6 · 2026-05-17T02:11:29.623Z_

<details><summary>↩ Tool result · `toolu_01VwZusC4z5h7n9Zj3iWjoDD`</summary>

```text
85	    \tau = \frac{C - D}{\binom{N}{2}},
86	\end{equation}
87	where $C$ and $D$ are the numbers of concordant and discordant pairs. Values near 1 indicate that calibration preserves the true model ordering; deviations reveal methods that correct absolute scores but distort relative comparisons.
88	
89	\paragraph{Dose-response monotonicity.}
90	We verify that the estimated contamination effect increases monotonically with dosage. Specifically, we compute Spearman's rank correlation between dosage level~$d$ and the posterior mean $\hat{\gamma}_k$ across the five dosage conditions per benchmark. Monotonic dose-response is a necessary (though not sufficient) condition for valid contamination modeling.
91	
92	\subsection{Results}
93	\label{sec:results}
94	
95	\paragraph{Main calibration results.}
96	Table~\ref{tab:main_results} presents calibration performance across all methods and benchmarks. \textbf{[PLACEHOLDER: exp-006]} ContamCal achieves MAE of \textbf{[PLACEHOLDER: exp-006]} percentage points averaged across benchmarks, compared to \textbf{[PLACEHOLDER: exp-006]} for the best baseline (B6, DCR). The 95\% credible intervals achieve \textbf{[PLACEHOLDER: exp-006]}\% coverage (nominal: 95\%), with average width of \textbf{[PLACEHOLDER: exp-006]} percentage points. Ranking preservation (Kendall's~$\tau$) is \textbf{[PLACEHOLDER: exp-006]}, indicating that calibration largely preserves the ground-truth model ordering.
97	
98	\begin{table}[t]
99	\centering
100	\small
101	\begin{tabular}{l cccc c}
102	\toprule
103	\textbf{Method} & \textbf{MMLU} & \textbf{GSM8K} & \textbf{ARC-C} & \textbf{HE} & \textbf{Avg} \\
104	\midrule
105	\multicolumn{6}{l}{\emph{MAE $\downarrow$ (percentage points)}} \\
106	B0. Raw & XX.X & XX.X & XX.X & XX.X & XX.X \\
107	B1. Remove-rescore & XX.X & XX.X & XX.X & XX.X & XX.X \\
108	B2. 2PL+$\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\
109	B3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\
110	B4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\
111	B5. Emperor's & XX.X & XX.X & XX.X & XX.X & XX.X \\
112	B6. DCR & XX.X & XX.X & XX.X & XX.X & XX.X \\
113	\textbf{ContamCal} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} \\
114	\midrule
115	\multicolumn{6}{l}{\emph{50\% CI Coverage $\uparrow$ (nominal: 50\%)}} \\
116	B2. 2PL+$\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\
117	B3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\
118	B4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\
119	\textbf{ContamCal} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} \\
120	\midrule
121	\multicolumn{6}{l}{\emph{80\% CI Coverage $\uparrow$ (nominal: 80\%)}} \\
122	B2. 2PL+$\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\
123	B3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\
124	B4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\
125	\textbf{ContamCal} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} \\
126	\midrule
127	\multicolumn{6}{l}{\emph{95\% CI Coverage $\uparrow$ (nominal: 95\%)}} \\
128	B2. 2PL+$\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\
129	B3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\
130	B4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\
131	\textbf{ContamCal} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} & \textbf{XX.X} \\
132	\midrule
133	\multicolumn{6}{l}{\emph{Kendall's $\tau$ $\uparrow$}} \\
134	B0. Raw & X.XX & X.XX & X.XX & X.XX & X.XX \\
135	B6. DCR & X.XX & X.XX & X.XX & X.XX & X.XX \\
136	\textbf{ContamCal} & \textbf{X.XX} & \textbf{X.XX} & \textbf{X.XX} & \textbf{X.XX} & \textbf{X.XX} \\
137	\bottomrule
138	\end{tabular}
139	\caption{Main calibration results across four benchmarks. \textbf{[PLACEHOLDER: exp-006]} MAE: mean absolute error between calibrated and ground-truth clean accuracy (lower is better). Coverage at 50\%/80\%/95\%: fraction of true values within credible interval (closer to nominal is better). HE\,=\,HumanEval, ARC-C\,=\,ARC-Challenge. Best results in \textbf{bold}.}
140	\label{tab:main_results}
141	\end{table}
142	
143	\paragraph{RRF signal ablation.}
144	Table~\ref{tab:rrf_ablation} reports signal aggregation ablations. \textbf{[PLACEHOLDER: exp-003]} Full four-signal RRF achieves AUC of \textbf{[PLACEHOLDER: exp-003]} for contaminated-vs-clean discrimination, compared to \textbf{[PLACEHOLDER: exp-003]} for the best single signal. Drop-one analysis reveals that removing \textbf{[PLACEHOLDER: exp-003]} causes the largest AUC decrease, while removing \textbf{[PLACEHOLDER: exp-003]} has minimal impact, suggesting complementary rather than redundant signal contributions.
145	
146	\begin{table}[t]
147	\centering
148	\small
149	\begin{tabular}{l cc}
150	\toprule
151	\textbf{Configuration} & \textbf{AUC} & \textbf{$\Delta$AUC} \\
152	\midrule
153	\multicolumn{3}{l}{\emph{Single-signal}} \\
154	Embedding retrieval & [TBD] & --- \\
155	Min-K\%++ & [TBD] & --- \\
156	ConStat & [TBD] & --- \\
157	Self-Critique & [TBD] & --- \\
158	\midrule
159	\multicolumn{3}{l}{\emph{Drop-one from full RRF}} \\
160	$-$ Embedding & [TBD] & [TBD] \\
161	$-$ Min-K\%++ & [TBD] & [TBD] \\
162	$-$ ConStat & [TBD] & [TBD] \\
163	$-$ Self-Critique & [TBD] & [TBD] \\
164	\midrule
165	Full RRF (4 signals) & \textbf{[TBD]} & --- \\
166	\bottomrule
167	\end{tabular}
168	\caption{Signal aggregation ablation. \textbf{[PLACEHOLDER: exp-003]} AUC for contaminated-vs-clean item discrimination, averaged across benchmarks and model scales. $\Delta$AUC: change relative to full RRF.}
169	\label{tab:rrf_ablation}
170	\end{table}
171	
172	\paragraph{RRF $k$-sensitivity.}
173	Table~\ref{tab:k_sensitivity} shows that calibration MAE and detection AUC are stable across $k \in \{20, 40, 60, 80, 100\}$, confirming that ContamCal is not sensitive to the RRF smoothing constant. \textbf{[PLACEHOLDER: exp-003]}
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\begin{tabular}{l ccccc}
179	\toprule
180	$k$ & 20 & 40 & \textbf{60} & 80 & 100 \\
181	\midrule
182	MAE & [TBD] & [TBD] & \textbf{[TBD]} & [TBD] & [TBD] \\
183	AUC & [TBD] & [TBD] & \textbf{[TBD]} & [TBD] & [TBD] \\
184	\bottomrule
185	\end{tabular}
186	\caption{Sensitivity to RRF smoothing constant~$k$. \textbf{[PLACEHOLDER: exp-003]} Default $k\!=\!60$ in bold.}
187	\label{tab:k_sensitivity}
188	\end{table}
189	
190	\paragraph{Dose-response curves.}
191	Figure~\ref{fig:dose_response} plots raw accuracy, calibrated accuracy, and ground-truth clean accuracy as a function of contamination dosage for each benchmark and model scale. \textbf{[PLACEHOLDER: exp-006]} Raw scores inflate monotonically with dosage, while calibrated scores remain approximately flat, tracking the ground-truth clean performance. The posterior mean $\hat{\gamma}_k$ increases monotonically with dosage across all benchmarks (Spearman $\rho =$ \textbf{[PLACEHOLDER: exp-006]}, $p <$ \textbf{[PLACEHOLDER: exp-006]}).
192	
193	\begin{figure}[t]
194	    \centering
195	    % \includegraphics[width=\columnwidth]{figures/dose_response.pdf}
196	    \fbox{\parbox{0.9\columnwidth}{\centering\vspace{2em}\textbf{[PLACEHOLDER: exp-006]}\\ Dose-response curves: raw vs.\ calibrated vs.\ ground-truth accuracy across 5 dosage levels, faceted by benchmark and model scale. Shaded bands = 95\% credible intervals.\vspace{2em}}}
197	    \caption{Dose-response curves across four benchmarks and three model scales (0.5B, 1.5B, 3B). \textbf{[PLACEHOLDER: exp-006]}}
198	    \label{fig:dose_response}
199	\end{figure}
200	
201	\paragraph{Uncertainty calibration and noise propagation.}
202	Figure~\ref{fig:ci_width} shows credible interval width as a function of measurement error variance~$\sigma_e^2$ (Eq.~\eqref{eq:measurement_error}). \textbf{[PLACEHOLDER: exp-005]} As detection signal noise increases, ContamCal produces appropriately wider intervals while maintaining nominal coverage. This confirms that the measurement error model successfully propagates detection uncertainty into the calibrated scores.
203	
204	\begin{figure}[t]
205	    \centering
206	    % \includegraphics[width=\columnwidth]{figures/ci_width_noise.pdf}
207	    \fbox{\parbox{0.9\columnwidth}{\centering\vspace{2em}\textbf{[PLACEHOLDER: exp-005]}\\ CI width and coverage vs.\ measurement error variance $\sigma_e^2$. Coverage should remain near nominal as width increases.\vspace{2em}}}
208	    \caption{Credible interval width (left axis) and coverage (right axis) as a function of measurement error variance. \textbf{[PLACEHOLDER: exp-005]}}
209	    \label{fig:ci_width}
210	\end{figure}
211	
212	\paragraph{Signal survival under RL.}
213	Figure~\ref{fig:signal_survival} presents detection signal AUCs across training regimes (SFT vs.\ RL with GRPO). \textbf{[PLACEHOLDER: exp-008]} Probability-based signals (Min-K\%++, ConStat) degrade from AUC \textbf{[PLACEHOLDER: exp-008]} under SFT to \textbf{[PLACEHOLDER: exp-008]} under RL---a cliff-like drop rather than gradual attenuation, consistent with the hypothesis in \S\ref{sec:signal_survival}. Self-Critique retains higher AUC of \textbf{[PLACEHOLDER: exp-008]} post-RL, validating its inclusion as a robustness anchor in the signal ensemble. This regime-dependent degradation is automatically captured by the measurement error model: RL-trained models receive wider credible intervals reflecting genuine epistemic uncertainty about their contamination status.
214	
215	\begin{figure}[t]
216	    \centering
217	    % \includegraphics[width=\columnwidth]{figures/signal_survival.pdf}
218	    \fbox{\parbox{0.9\columnwidth}{\centering\vspace{2em}\textbf{[PLACEHOLDER: exp-008, if available]}\\ Signal AUC by training regime (SFT vs.\ RL). Grouped bar chart showing cliff-like degradation for probability-based signals vs.\ retention for Self-Critique.\vspace{2em}}}
219	    \caption{Detection signal AUC across training regimes. \textbf{[PLACEHOLDER: exp-008]}}
220	    \label{fig:signal_survival}
221	\end{figure}
222	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "uuid": "f6f833d6-7190-4dd6-a522-9f9d2f28b2ec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experiments.tex",
      "content": "    \\tau = \\frac{C - D}{\\binom{N}{2}},\n\\end{equation}\nwhere $C$ and $D$ are the numbers of concordant and discordant pairs. Values near 1 indicate that calibration preserves the true model ordering; deviations reveal methods that correct absolute scores but distort relative comparisons.\n\n\\paragraph{Dose-response monotonicity.}\nWe verify that the estimated contamination effect increases monotonically with dosage. Specifically, we compute Spearman's rank correlation between dosage level~$d$ and the posterior mean $\\hat{\\gamma}_k$ across the five dosage conditions per benchmark. Monotonic dose-response is a necessary (though not sufficient) condition for valid contamination modeling.\n\n\\subsection{Results}\n\\label{sec:results}\n\n\\paragraph{Main calibration results.}\nTable~\\ref{tab:main_results} presents calibration performance across all methods and benchmarks. \\textbf{[PLACEHOLDER: exp-006]} ContamCal achieves MAE of \\textbf{[PLACEHOLDER: exp-006]} percentage points averaged across benchmarks, compared to \\textbf{[PLACEHOLDER: exp-006]} for the best baseline (B6, DCR). The 95\\% credible intervals achieve \\textbf{[PLACEHOLDER: exp-006]}\\% coverage (nominal: 95\\%), with average width of \\textbf{[PLACEHOLDER: exp-006]} percentage points. Ranking preservation (Kendall's~$\\tau$) is \\textbf{[PLACEHOLDER: exp-006]}, indicating that calibration largely preserves the ground-truth model ordering.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l cccc c}\n\\toprule\n\\textbf{Method} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC-C} & \\textbf{HE} & \\textbf{Avg} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{MAE $\\downarrow$ (percentage points)}} \\\\\nB0. Raw & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB1. Remove-rescore & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB5. Emperor's & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB6. DCR & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{50\\% CI Coverage $\\uparrow$ (nominal: 50\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{80\\% CI Coverage $\\uparrow$ (nominal: 80\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{95\\% CI Coverage $\\uparrow$ (nominal: 95\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Kendall's $\\tau$ $\\uparrow$}} \\\\\nB0. Raw & X.XX & X.XX & X.XX & X.XX & X.XX \\\\\nB6. DCR & X.XX & X.XX & X.XX & X.XX & X.XX \\\\\n\\textbf{ContamCal} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Main calibration results across four benchmarks. \\textbf{[PLACEHOLDER: exp-006]} MAE: mean absolute error between calibrated and ground-truth clean accuracy (lower is better). Coverage at 50\\%/80\\%/95\\%: fraction of true values within credible interval (closer to nominal is better). HE\\,=\\,HumanEval, ARC-C\\,=\\,ARC-Challenge. Best results in \\textbf{bold}.}\n\\label{tab:main_results}\n\\end{table}\n\n\\paragraph{RRF signal ablation.}\nTable~\\ref{tab:rrf_ablation} reports signal aggregation ablations. \\textbf{[PLACEHOLDER: exp-003]} Full four-signal RRF achieves AUC of \\textbf{[PLACEHOLDER: exp-003]} for contaminated-vs-clean discrimination, compared to \\textbf{[PLACEHOLDER: exp-003]} for the best single signal. Drop-one analysis reveals that removing \\textbf{[PLACEHOLDER: exp-003]} causes the largest AUC decrease, while removing \\textbf{[PLACEHOLDER: exp-003]} has minimal impact, suggesting complementary rather than redundant signal contributions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AUC} & \\textbf{$\\Delta$AUC} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Single-signal}} \\\\\nEmbedding retrieval & [TBD] & --- \\\\\nMin-K\\%++ & [TBD] & --- \\\\\nConStat & [TBD] & --- \\\\\nSelf-Critique & [TBD] & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Drop-one from full RRF}} \\\\\n$-$ Embedding & [TBD] & [TBD] \\\\\n$-$ Min-K\\%++ & [TBD] & [TBD] \\\\\n$-$ ConStat & [TBD] & [TBD] \\\\\n$-$ Self-Critique & [TBD] & [TBD] \\\\\n\\midrule\nFull RRF (4 signals) & \\textbf{[TBD]} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Signal aggregation ablation. \\textbf{[PLACEHOLDER: exp-003]} AUC for contaminated-vs-clean item discrimination, averaged across benchmarks and model scales. $\\Delta$AUC: change relative to full RRF.}\n\\label{tab:rrf_ablation}\n\\end{table}\n\n\\paragraph{RRF $k$-sensitivity.}\nTable~\\ref{tab:k_sensitivity} shows that calibration MAE and detection AUC are stable across $k \\in \\{20, 40, 60, 80, 100\\}$, confirming that ContamCal is not sensitive to the RRF smoothing constant. \\textbf{[PLACEHOLDER: exp-003]}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccccc}\n\\toprule\n$k$ & 20 & 40 & \\textbf{60} & 80 & 100 \\\\\n\\midrule\nMAE & [TBD] & [TBD] & \\textbf{[TBD]} & [TBD] & [TBD] \\\\\nAUC & [TBD] & [TBD] & \\textbf{[TBD]} & [TBD] & [TBD] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to RRF smoothing constant~$k$. \\textbf{[PLACEHOLDER: exp-003]} Default $k\\!=\\!60$ in bold.}\n\\label{tab:k_sensitivity}\n\\end{table}\n\n\\paragraph{Dose-response curves.}\nFigure~\\ref{fig:dose_response} plots raw accuracy, calibrated accuracy, and ground-truth clean accuracy as a function of contamination dosage for each benchmark and model scale. \\textbf{[PLACEHOLDER: exp-006]} Raw scores inflate monotonically with dosage, while calibrated scores remain approximately flat, tracking the ground-truth clean performance. The posterior mean $\\hat{\\gamma}_k$ increases monotonically with dosage across all benchmarks (Spearman $\\rho =$ \\textbf{[PLACEHOLDER: exp-006]}, $p <$ \\textbf{[PLACEHOLDER: exp-006]}).\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/dose_response.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-006]}\\\\ Dose-response curves: raw vs.\\ calibrated vs.\\ ground-truth accuracy across 5 dosage levels, faceted by benchmark and model scale. Shaded bands = 95\\% credible intervals.\\vspace{2em}}}\n    \\caption{Dose-response curves across four benchmarks and three model scales (0.5B, 1.5B, 3B). \\textbf{[PLACEHOLDER: exp-006]}}\n    \\label{fig:dose_response}\n\\end{figure}\n\n\\paragraph{Uncertainty calibration and noise propagation.}\nFigure~\\ref{fig:ci_width} shows credible interval width as a function of measurement error variance~$\\sigma_e^2$ (Eq.~\\eqref{eq:measurement_error}). \\textbf{[PLACEHOLDER: exp-005]} As detection signal noise increases, ContamCal produces appropriately wider intervals while maintaining nominal coverage. This confirms that the measurement error model successfully propagates detection uncertainty into the calibrated scores.\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/ci_width_noise.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-005]}\\\\ CI width and coverage vs.\\ measurement error variance $\\sigma_e^2$. Coverage should remain near nominal as width increases.\\vspace{2em}}}\n    \\caption{Credible interval width (left axis) and coverage (right axis) as a function of measurement error variance. \\textbf{[PLACEHOLDER: exp-005]}}\n    \\label{fig:ci_width}\n\\end{figure}\n\n\\paragraph{Signal survival under RL.}\nFigure~\\ref{fig:signal_survival} presents detection signal AUCs across training regimes (SFT vs.\\ RL with GRPO). \\textbf{[PLACEHOLDER: exp-008]} Probability-based signals (Min-K\\%++, ConStat) degrade from AUC \\textbf{[PLACEHOLDER: exp-008]} under SFT to \\textbf{[PLACEHOLDER: exp-008]} under RL---a cliff-like drop rather than gradual attenuation, consistent with the hypothesis in \\S\\ref{sec:signal_survival}. Self-Critique retains higher AUC of \\textbf{[PLACEHOLDER: exp-008]} post-RL, validating its inclusion as a robustness anchor in the signal ensemble. This regime-dependent degradation is automatically captured by the measurement error model: RL-trained models receive wider credible intervals reflecting genuine epistemic uncertainty about their contamination status.\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/signal_survival.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-008, if available]}\\\\ Signal AUC by training regime (SFT vs.\\ RL). Grouped bar chart showing cliff-like degradation for probability-based signals vs.\\ retention for Self-Critique.\\vspace{2em}}}\n    \\caption{Detection signal AUC across training regimes. \\textbf{[PLACEHOLDER: exp-008]}}\n    \\label{fig:signal_survival}\n\\end{figure}\n",
      "numLines": 138,
      "startLine": 85,
      "totalLines": 222
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

Now let me also read lines 1-91 to understand the full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "uuid": "08c20a74-0c02-422a-92de-a451a309a9cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPuXREq396ba4wfHCJKbE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4027,
      "cache_read_input_tokens": 28295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4027
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

<details open><summary>🔧 Tool call — Read · `toolu_01T2TR2aGF3ptEEonem21NRx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experiments.tex",
  "limit": 91
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "uuid": "a42c31c6-6230-49fe-9a12-45bdb48dad94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPuXREq396ba4wfHCJKbE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4027,
      "cache_read_input_tokens": 28295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4027
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

_source line 9 · 2026-05-17T02:11:34.704Z_

<details><summary>↩ Tool result · `toolu_01T2TR2aGF3ptEEonem21NRx`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate ContamCal through controlled contamination injection across multiple model scales, dosage levels, and benchmarks. The experimental design provides ground-truth clean performance for every configuration, enabling direct measurement of calibration quality.
5	
6	\subsection{Experimental Setup}
7	\label{sec:exp_setup}
8	
9	Our evaluation follows a controlled SFT injection pipeline: we deliberately contaminate models at known dosage levels, compute detection signals, fit the contamination-augmented IRT model, and compare calibrated scores against the known ground truth. This design provides the internal validity necessary for rigorous evaluation---we know the true contamination status of every item for every model.
10	
11	We use the Qwen2.5 model family at three scales---0.5B, 1.5B, and 3B parameters---all fine-tuned via LoRA. A separate Qwen2.5-7B-Instruct model serves as the paraphrase generator for ConStat signal computation (\S\ref{sec:stage1}). We evaluate on four benchmarks spanning diverse evaluation modalities:
12	\begin{itemize}
13	    \item \textbf{MMLU} \citep{hendrycks2021mmlu}: knowledge-intensive multiple-choice (14,042 items);
14	    \item \textbf{GSM8K} \citep{cobbe2021gsm8k}: mathematical reasoning with free-form answers (1,319 items);
15	    \item \textbf{ARC-Challenge} \citep{clark2018arc}: science reasoning multiple-choice (1,172 items);
16	    \item \textbf{HumanEval} \citep{chen2021humaneval}: code generation with execution-based evaluation (164 items).
17	\end{itemize}
18	HumanEval's small item count may limit 4PL parameter estimation reliability; we include it to test ContamCal at the boundary of applicability.
19	
20	\subsection{Controlled Contamination Injection}
21	\label{sec:injection}
22	
23	For each model scale, we inject contamination at five dosage levels: 0\% (clean baseline), 5\%, 25\%, 50\%, and 100\% of benchmark items. At each dosage level~$d$, a random subset of $\lfloor d \cdot |B| \rfloor$ items from benchmark~$B$ is selected for injection. Selected items are paraphrased using the 7B-Instruct model to produce surface-form variants that evade $n$-gram decontamination, following the protocol of \citet{yang2026rl}. Models are then fine-tuned via LoRA ($r\!=\!16$, $\alpha\!=\!32$) on the paraphrased items mixed with a held-out instruction-tuning corpus, for 1 epoch with learning rate $2 \times 10^{-4}$.
24	
25	Each configuration (3 model scales $\times$ 5 dosage levels) is run with 3 random seeds controlling both item selection and LoRA initialization, yielding 45 model checkpoints, each evaluated on 4 benchmarks (180 model--benchmark evaluation pairs). The 0\%-dosage models serve as ground-truth baselines for computing calibration error.
26	
27	\subsection{Detection Signals and Aggregation}
28	\label{sec:exp_signals}
29	
30	We compute four detection signals on all model--item pairs, as described in \S\ref{sec:stage1}. \textbf{Embedding retrieval} indexes the training corpus via a sentence transformer and retrieves near-duplicate benchmark items by cosine similarity. \textbf{Min-K\%++} computes membership inference statistics using the 0\%-dosage model of matching scale as reference. \textbf{ConStat} measures the accuracy gap between original and paraphrased item variants. \textbf{Self-Critique} quantifies entropy collapse in model self-evaluations. Signals are aggregated via RRF (Eq.~\eqref{eq:rrf}) with $k\!=\!60$.
31	
32	We conduct three ablation studies on signal aggregation: (i)~a \emph{drop-one} ablation that removes each signal in turn to assess marginal contribution; (ii)~a \emph{single-signal} ablation evaluating each signal independently; and (iii)~a $k$-sensitivity sweep over $k \in \{20, 40, 60, 80, 100\}$. All ablations report AUC for contaminated-vs-clean item discrimination.
33	
34	\subsection{IRT Calibration and Baselines}
35	\label{sec:exp_irt}
36	
37	We fit the contamination-augmented 4PL IRT model (Eq.~\eqref{eq:4pl}) separately per benchmark using CmdStanPy \citep{carpenter2017} with the NUTS sampler \citep{hoffman2014}. Each fit uses 4 independent chains of 2,000 iterations (1,000 warmup), with convergence assessed via split-$\hat{R} < 1.01$, $\text{ESS} > 400$, and $< 0.1\%$ divergent transitions (\S\ref{sec:inference}). The measurement error model (Eq.~\eqref{eq:measurement_error}) treats RRF exposure scores as noisy proxies for latent contamination~$\tau_{ij}$. Calibrated scores are computed via Eq.~\eqref{eq:calibrated_mc} by setting exposure to zero and marginalizing over posterior draws.
38	
39	We also fit an analytical measurement error (ME) variant that eliminates latent $\tau$ parameters via conjugate normal integration, retaining MCMC (Stan NUTS) for the remaining IRT parameters. This provides scalability to large item pools (e.g., MMLU's 14K items) without introducing additional latent variables.
40	
41	We compare ContamCal against seven baselines:
42	\begin{enumerate}
43	    \item[\textbf{B0.}] \textbf{Raw}: original benchmark scores with no adjustment, serving as the anchor for quantifying contamination inflation.
44	    \item[\textbf{B1.}] \textbf{Remove-and-rescore}: items with RRF exposure score above the 75th percentile are removed; accuracy is recomputed on remaining items.
45	    \item[\textbf{B2.}] \textbf{Single-signal 2PL+$\boldsymbol{\gamma}$}: the best-performing single detection signal (by AUC) enters a 2PL IRT model with contamination covariate~$\gamma$ but without guessing ($c\!=\!0$) or slip ($d\!=\!1$) parameters.
46	    \item[\textbf{B3.}] \textbf{Vanilla 4PL} ($\boldsymbol{\gamma\!=\!0}$): standard 4PL IRT without contamination covariate, representing current IRT-based evaluation practice \citep{gu2026psnirt,polo2026growing}.
47	    \item[\textbf{B4.}] \textbf{Linear exposure regression}: $\text{Acc}_i = \beta_0 + \beta_1 \bar{e}_i + \epsilon$, where $\bar{e}_i$ is the mean RRF exposure score, with bootstrap confidence intervals. Tests whether a simple regression suffices without the IRT machinery.
48	    \item[\textbf{B5.}] \textbf{Emperor's mitigation}: two representative strategies from \citet{xu2025emperor}---item rephrasing and option shuffling---applied at evaluation time. We report the better-performing strategy per benchmark.
49	    \item[\textbf{B6.}] \textbf{DCR}: the decontaminated calibration and ranking method of \citet{li2025dcr}, which produces adjusted accuracy via fuzzy inference over detection signals without uncertainty quantification.
50	\end{enumerate}
51	
52	\subsection{Evaluation Protocol}
53	\label{sec:eval_protocol}
54	
55	We assess calibration quality using five metrics that jointly characterize accuracy, uncertainty quantification, ranking fidelity, and mechanistic validity.
56	
57	\paragraph{Calibration error.}
58	Mean absolute error between the calibrated score $\widehat{\text{Acc}}_i^{\text{cal}}$ (Eq.~\eqref{eq:calibrated_mc}) and the ground-truth clean accuracy $\text{Acc}_i^{\text{clean}}$ measured on 0\%-dosage models:
59	\begin{equation}
60	\label{eq:mae}
61	    \text{MAE} = \frac{1}{N} \sum_{i=1}^{N} \left| \widehat{\text{Acc}}_i^{\text{cal}} - \text{Acc}_i^{\text{clean}} \right|.
62	\end{equation}
63	We report bootstrap 95\% confidence intervals computed over 1,000 resamples of model--benchmark pairs.
64	
65	\paragraph{Interval coverage.}
66	The fraction of models whose ground-truth clean accuracy falls within the $\alpha$-level credible interval:
67	\begin{equation}
68	\label{eq:coverage}
69	    \text{Cov}(\alpha) = \frac{1}{N} \sum_{i=1}^{N} \mathbf{1}\!\left[\text{Acc}_i^{\text{clean}} \in \text{CI}_i^{(\alpha)}\right].
70	\end{equation}
71	We evaluate at $\alpha \in \{50\%, 80\%, 95\%\}$. Nominal coverage ($\text{Cov}(\alpha) \approx \alpha$) indicates well-calibrated uncertainty. For baselines without native uncertainty quantification (B0, B1, B5, B6), we use bootstrap resampling to construct confidence intervals.
72	
73	\paragraph{Interval sharpness.}
74	Average width of the credible interval at coverage level~$\alpha$:
75	\begin{equation}
76	\label{eq:sharpness}
77	    \text{Sharp}(\alpha) = \frac{1}{N} \sum_{i=1}^{N} \text{width}\!\left(\text{CI}_i^{(\alpha)}\right).
78	\end{equation}
79	Narrower intervals are preferred at fixed coverage; the ideal method achieves nominal coverage with minimal width.
80	
81	\paragraph{Ranking preservation.}
82	Kendall's $\tau$ between the calibrated model ranking and the ground-truth clean ranking:
83	\begin{equation}
84	\label{eq:kendall}
85	    \tau = \frac{C - D}{\binom{N}{2}},
86	\end{equation}
87	where $C$ and $D$ are the numbers of concordant and discordant pairs. Values near 1 indicate that calibration preserves the true model ordering; deviations reveal methods that correct absolute scores but distort relative comparisons.
88	
89	\paragraph{Dose-response monotonicity.}
90	We verify that the estimated contamination effect increases monotonically with dosage. Specifically, we compute Spearman's rank correlation between dosage level~$d$ and the posterior mean $\hat{\gamma}_k$ across the five dosage conditions per benchmark. Monotonic dose-response is a necessary (though not sufficient) condition for valid contamination modeling.
91	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "uuid": "7327f328-14fd-42e4-b6be-690b9ab26ad5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ContamCal through controlled contamination injection across multiple model scales, dosage levels, and benchmarks. The experimental design provides ground-truth clean performance for every configuration, enabling direct measurement of calibration quality.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\nOur evaluation follows a controlled SFT injection pipeline: we deliberately contaminate models at known dosage levels, compute detection signals, fit the contamination-augmented IRT model, and compare calibrated scores against the known ground truth. This design provides the internal validity necessary for rigorous evaluation---we know the true contamination status of every item for every model.\n\nWe use the Qwen2.5 model family at three scales---0.5B, 1.5B, and 3B parameters---all fine-tuned via LoRA. A separate Qwen2.5-7B-Instruct model serves as the paraphrase generator for ConStat signal computation (\\S\\ref{sec:stage1}). We evaluate on four benchmarks spanning diverse evaluation modalities:\n\\begin{itemize}\n    \\item \\textbf{MMLU} \\citep{hendrycks2021mmlu}: knowledge-intensive multiple-choice (14,042 items);\n    \\item \\textbf{GSM8K} \\citep{cobbe2021gsm8k}: mathematical reasoning with free-form answers (1,319 items);\n    \\item \\textbf{ARC-Challenge} \\citep{clark2018arc}: science reasoning multiple-choice (1,172 items);\n    \\item \\textbf{HumanEval} \\citep{chen2021humaneval}: code generation with execution-based evaluation (164 items).\n\\end{itemize}\nHumanEval's small item count may limit 4PL parameter estimation reliability; we include it to test ContamCal at the boundary of applicability.\n\n\\subsection{Controlled Contamination Injection}\n\\label{sec:injection}\n\nFor each model scale, we inject contamination at five dosage levels: 0\\% (clean baseline), 5\\%, 25\\%, 50\\%, and 100\\% of benchmark items. At each dosage level~$d$, a random subset of $\\lfloor d \\cdot |B| \\rfloor$ items from benchmark~$B$ is selected for injection. Selected items are paraphrased using the 7B-Instruct model to produce surface-form variants that evade $n$-gram decontamination, following the protocol of \\citet{yang2026rl}. Models are then fine-tuned via LoRA ($r\\!=\\!16$, $\\alpha\\!=\\!32$) on the paraphrased items mixed with a held-out instruction-tuning corpus, for 1 epoch with learning rate $2 \\times 10^{-4}$.\n\nEach configuration (3 model scales $\\times$ 5 dosage levels) is run with 3 random seeds controlling both item selection and LoRA initialization, yielding 45 model checkpoints, each evaluated on 4 benchmarks (180 model--benchmark evaluation pairs). The 0\\%-dosage models serve as ground-truth baselines for computing calibration error.\n\n\\subsection{Detection Signals and Aggregation}\n\\label{sec:exp_signals}\n\nWe compute four detection signals on all model--item pairs, as described in \\S\\ref{sec:stage1}. \\textbf{Embedding retrieval} indexes the training corpus via a sentence transformer and retrieves near-duplicate benchmark items by cosine similarity. \\textbf{Min-K\\%++} computes membership inference statistics using the 0\\%-dosage model of matching scale as reference. \\textbf{ConStat} measures the accuracy gap between original and paraphrased item variants. \\textbf{Self-Critique} quantifies entropy collapse in model self-evaluations. Signals are aggregated via RRF (Eq.~\\eqref{eq:rrf}) with $k\\!=\\!60$.\n\nWe conduct three ablation studies on signal aggregation: (i)~a \\emph{drop-one} ablation that removes each signal in turn to assess marginal contribution; (ii)~a \\emph{single-signal} ablation evaluating each signal independently; and (iii)~a $k$-sensitivity sweep over $k \\in \\{20, 40, 60, 80, 100\\}$. All ablations report AUC for contaminated-vs-clean item discrimination.\n\n\\subsection{IRT Calibration and Baselines}\n\\label{sec:exp_irt}\n\nWe fit the contamination-augmented 4PL IRT model (Eq.~\\eqref{eq:4pl}) separately per benchmark using CmdStanPy \\citep{carpenter2017} with the NUTS sampler \\citep{hoffman2014}. Each fit uses 4 independent chains of 2,000 iterations (1,000 warmup), with convergence assessed via split-$\\hat{R} < 1.01$, $\\text{ESS} > 400$, and $< 0.1\\%$ divergent transitions (\\S\\ref{sec:inference}). The measurement error model (Eq.~\\eqref{eq:measurement_error}) treats RRF exposure scores as noisy proxies for latent contamination~$\\tau_{ij}$. Calibrated scores are computed via Eq.~\\eqref{eq:calibrated_mc} by setting exposure to zero and marginalizing over posterior draws.\n\nWe also fit an analytical measurement error (ME) variant that eliminates latent $\\tau$ parameters via conjugate normal integration, retaining MCMC (Stan NUTS) for the remaining IRT parameters. This provides scalability to large item pools (e.g., MMLU's 14K items) without introducing additional latent variables.\n\nWe compare ContamCal against seven baselines:\n\\begin{enumerate}\n    \\item[\\textbf{B0.}] \\textbf{Raw}: original benchmark scores with no adjustment, serving as the anchor for quantifying contamination inflation.\n    \\item[\\textbf{B1.}] \\textbf{Remove-and-rescore}: items with RRF exposure score above the 75th percentile are removed; accuracy is recomputed on remaining items.\n    \\item[\\textbf{B2.}] \\textbf{Single-signal 2PL+$\\boldsymbol{\\gamma}$}: the best-performing single detection signal (by AUC) enters a 2PL IRT model with contamination covariate~$\\gamma$ but without guessing ($c\\!=\\!0$) or slip ($d\\!=\\!1$) parameters.\n    \\item[\\textbf{B3.}] \\textbf{Vanilla 4PL} ($\\boldsymbol{\\gamma\\!=\\!0}$): standard 4PL IRT without contamination covariate, representing current IRT-based evaluation practice \\citep{gu2026psnirt,polo2026growing}.\n    \\item[\\textbf{B4.}] \\textbf{Linear exposure regression}: $\\text{Acc}_i = \\beta_0 + \\beta_1 \\bar{e}_i + \\epsilon$, where $\\bar{e}_i$ is the mean RRF exposure score, with bootstrap confidence intervals. Tests whether a simple regression suffices without the IRT machinery.\n    \\item[\\textbf{B5.}] \\textbf{Emperor's mitigation}: two representative strategies from \\citet{xu2025emperor}---item rephrasing and option shuffling---applied at evaluation time. We report the better-performing strategy per benchmark.\n    \\item[\\textbf{B6.}] \\textbf{DCR}: the decontaminated calibration and ranking method of \\citet{li2025dcr}, which produces adjusted accuracy via fuzzy inference over detection signals without uncertainty quantification.\n\\end{enumerate}\n\n\\subsection{Evaluation Protocol}\n\\label{sec:eval_protocol}\n\nWe assess calibration quality using five metrics that jointly characterize accuracy, uncertainty quantification, ranking fidelity, and mechanistic validity.\n\n\\paragraph{Calibration error.}\nMean absolute error between the calibrated score $\\widehat{\\text{Acc}}_i^{\\text{cal}}$ (Eq.~\\eqref{eq:calibrated_mc}) and the ground-truth clean accuracy $\\text{Acc}_i^{\\text{clean}}$ measured on 0\\%-dosage models:\n\\begin{equation}\n\\label{eq:mae}\n    \\text{MAE} = \\frac{1}{N} \\sum_{i=1}^{N} \\left| \\widehat{\\text{Acc}}_i^{\\text{cal}} - \\text{Acc}_i^{\\text{clean}} \\right|.\n\\end{equation}\nWe report bootstrap 95\\% confidence intervals computed over 1,000 resamples of model--benchmark pairs.\n\n\\paragraph{Interval coverage.}\nThe fraction of models whose ground-truth clean accuracy falls within the $\\alpha$-level credible interval:\n\\begin{equation}\n\\label{eq:coverage}\n    \\text{Cov}(\\alpha) = \\frac{1}{N} \\sum_{i=1}^{N} \\mathbf{1}\\!\\left[\\text{Acc}_i^{\\text{clean}} \\in \\text{CI}_i^{(\\alpha)}\\right].\n\\end{equation}\nWe evaluate at $\\alpha \\in \\{50\\%, 80\\%, 95\\%\\}$. Nominal coverage ($\\text{Cov}(\\alpha) \\approx \\alpha$) indicates well-calibrated uncertainty. For baselines without native uncertainty quantification (B0, B1, B5, B6), we use bootstrap resampling to construct confidence intervals.\n\n\\paragraph{Interval sharpness.}\nAverage width of the credible interval at coverage level~$\\alpha$:\n\\begin{equation}\n\\label{eq:sharpness}\n    \\text{Sharp}(\\alpha) = \\frac{1}{N} \\sum_{i=1}^{N} \\text{width}\\!\\left(\\text{CI}_i^{(\\alpha)}\\right).\n\\end{equation}\nNarrower intervals are preferred at fixed coverage; the ideal method achieves nominal coverage with minimal width.\n\n\\paragraph{Ranking preservation.}\nKendall's $\\tau$ between the calibrated model ranking and the ground-truth clean ranking:\n\\begin{equation}\n\\label{eq:kendall}\n    \\tau = \\frac{C - D}{\\binom{N}{2}},\n\\end{equation}\nwhere $C$ and $D$ are the numbers of concordant and discordant pairs. Values near 1 indicate that calibration preserves the true model ordering; deviations reveal methods that correct absolute scores but distort relative comparisons.\n\n\\paragraph{Dose-response monotonicity.}\nWe verify that the estimated contamination effect increases monotonically with dosage. Specifically, we compute Spearman's rank correlation between dosage level~$d$ and the posterior mean $\\hat{\\gamma}_k$ across the five dosage conditions per benchmark. Monotonic dose-response is a necessary (though not sufficient) condition for valid contamination modeling.\n",
      "numLines": 91,
      "startLine": 1,
      "totalLines": 222
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

Now I have the full picture. I need to replace everything from line 92 to the end of the file. Let me write the new Results section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "uuid": "81e5d4bc-7c82-42a7-957f-98c52a6ccd2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FwuhrEHjh4oYSFxT3efq9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3044,
      "cache_read_input_tokens": 32322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3044
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01UEFRoNSGGbZrsqD4QYK38S`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experiments.tex",
  "old_string": "\\subsection{Results}\n\\label{sec:results}\n\n\\paragraph{Main calibration results.}\nTable~\\ref{tab:main_results} presents calibration performance across all methods and benchmarks. \\textbf{[PLACEHOLDER: exp-006]} ContamCal achieves MAE of \\textbf{[PLACEHOLDER: exp-006]} percentage points averaged across benchmarks, compared to \\textbf{[PLACEHOLDER: exp-006]} for the best baseline (B6, DCR). The 95\\% credible intervals achieve \\textbf{[PLACEHOLDER: exp-006]}\\% coverage (nominal: 95\\%), with average width of \\textbf{[PLACEHOLDER: exp-006]} percentage points. Ranking preservation (Kendall's~$\\tau$) is \\textbf{[PLACEHOLDER: exp-006]}, indicating that calibration largely preserves the ground-truth model ordering.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l cccc c}\n\\toprule\n\\textbf{Method} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC-C} & \\textbf{HE} & \\textbf{Avg} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{MAE $\\downarrow$ (percentage points)}} \\\\\nB0. Raw & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB1. Remove-rescore & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB5. Emperor's & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB6. DCR & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{50\\% CI Coverage $\\uparrow$ (nominal: 50\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{80\\% CI Coverage $\\uparrow$ (nominal: 80\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{95\\% CI Coverage $\\uparrow$ (nominal: 95\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Kendall's $\\tau$ $\\uparrow$}} \\\\\nB0. Raw & X.XX & X.XX & X.XX & X.XX & X.XX \\\\\nB6. DCR & X.XX & X.XX & X.XX & X.XX & X.XX \\\\\n\\textbf{ContamCal} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Main calibration results across four benchmarks. \\textbf{[PLACEHOLDER: exp-006]} MAE: mean absolute error between calibrated and ground-truth clean accuracy (lower is better). Coverage at 50\\%/80\\%/95\\%: fraction of true values within credible interval (closer to nominal is better). HE\\,=\\,HumanEval, ARC-C\\,=\\,ARC-Challenge. Best results in \\textbf{bold}.}\n\\label{tab:main_results}\n\\end{table}\n\n\\paragraph{RRF signal ablation.}\nTable~\\ref{tab:rrf_ablation} reports signal aggregation ablations. \\textbf{[PLACEHOLDER: exp-003]} Full four-signal RRF achieves AUC of \\textbf{[PLACEHOLDER: exp-003]} for contaminated-vs-clean discrimination, compared to \\textbf{[PLACEHOLDER: exp-003]} for the best single signal. Drop-one analysis reveals that removing \\textbf{[PLACEHOLDER: exp-003]} causes the largest AUC decrease, while removing \\textbf{[PLACEHOLDER: exp-003]} has minimal impact, suggesting complementary rather than redundant signal contributions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AUC} & \\textbf{$\\Delta$AUC} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Single-signal}} \\\\\nEmbedding retrieval & [TBD] & --- \\\\\nMin-K\\%++ & [TBD] & --- \\\\\nConStat & [TBD] & --- \\\\\nSelf-Critique & [TBD] & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Drop-one from full RRF}} \\\\\n$-$ Embedding & [TBD] & [TBD] \\\\\n$-$ Min-K\\%++ & [TBD] & [TBD] \\\\\n$-$ ConStat & [TBD] & [TBD] \\\\\n$-$ Self-Critique & [TBD] & [TBD] \\\\\n\\midrule\nFull RRF (4 signals) & \\textbf{[TBD]} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Signal aggregation ablation. \\textbf{[PLACEHOLDER: exp-003]} AUC for contaminated-vs-clean item discrimination, averaged across benchmarks and model scales. $\\Delta$AUC: change relative to full RRF.}\n\\label{tab:rrf_ablation}\n\\end{table}\n\n\\paragraph{RRF $k$-sensitivity.}\nTable~\\ref{tab:k_sensitivity} shows that calibration MAE and detection AUC are stable across $k \\in \\{20, 40, 60, 80, 100\\}$, confirming that ContamCal is not sensitive to the RRF smoothing constant. \\textbf{[PLACEHOLDER: exp-003]}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccccc}\n\\toprule\n$k$ & 20 & 40 & \\textbf{60} & 80 & 100 \\\\\n\\midrule\nMAE & [TBD] & [TBD] & \\textbf{[TBD]} & [TBD] & [TBD] \\\\\nAUC & [TBD] & [TBD] & \\textbf{[TBD]} & [TBD] & [TBD] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to RRF smoothing constant~$k$. \\textbf{[PLACEHOLDER: exp-003]} Default $k\\!=\\!60$ in bold.}\n\\label{tab:k_sensitivity}\n\\end{table}\n\n\\paragraph{Dose-response curves.}\nFigure~\\ref{fig:dose_response} plots raw accuracy, calibrated accuracy, and ground-truth clean accuracy as a function of contamination dosage for each benchmark and model scale. \\textbf{[PLACEHOLDER: exp-006]} Raw scores inflate monotonically with dosage, while calibrated scores remain approximately flat, tracking the ground-truth clean performance. The posterior mean $\\hat{\\gamma}_k$ increases monotonically with dosage across all benchmarks (Spearman $\\rho =$ \\textbf{[PLACEHOLDER: exp-006]}, $p <$ \\textbf{[PLACEHOLDER: exp-006]}).\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/dose_response.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-006]}\\\\ Dose-response curves: raw vs.\\ calibrated vs.\\ ground-truth accuracy across 5 dosage levels, faceted by benchmark and model scale. Shaded bands = 95\\% credible intervals.\\vspace{2em}}}\n    \\caption{Dose-response curves across four benchmarks and three model scales (0.5B, 1.5B, 3B). \\textbf{[PLACEHOLDER: exp-006]}}\n    \\label{fig:dose_response}\n\\end{figure}\n\n\\paragraph{Uncertainty calibration and noise propagation.}\nFigure~\\ref{fig:ci_width} shows credible interval width as a function of measurement error variance~$\\sigma_e^2$ (Eq.~\\eqref{eq:measurement_error}). \\textbf{[PLACEHOLDER: exp-005]} As detection signal noise increases, ContamCal produces appropriately wider intervals while maintaining nominal coverage. This confirms that the measurement error model successfully propagates detection uncertainty into the calibrated scores.\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/ci_width_noise.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-005]}\\\\ CI width and coverage vs.\\ measurement error variance $\\sigma_e^2$. Coverage should remain near nominal as width increases.\\vspace{2em}}}\n    \\caption{Credible interval width (left axis) and coverage (right axis) as a function of measurement error variance. \\textbf{[PLACEHOLDER: exp-005]}}\n    \\label{fig:ci_width}\n\\end{figure}\n\n\\paragraph{Signal survival under RL.}\nFigure~\\ref{fig:signal_survival} presents detection signal AUCs across training regimes (SFT vs.\\ RL with GRPO). \\textbf{[PLACEHOLDER: exp-008]} Probability-based signals (Min-K\\%++, ConStat) degrade from AUC \\textbf{[PLACEHOLDER: exp-008]} under SFT to \\textbf{[PLACEHOLDER: exp-008]} under RL---a cliff-like drop rather than gradual attenuation, consistent with the hypothesis in \\S\\ref{sec:signal_survival}. Self-Critique retains higher AUC of \\textbf{[PLACEHOLDER: exp-008]} post-RL, validating its inclusion as a robustness anchor in the signal ensemble. This regime-dependent degradation is automatically captured by the measurement error model: RL-trained models receive wider credible intervals reflecting genuine epistemic uncertainty about their contamination status.\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/signal_survival.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-008, if available]}\\\\ Signal AUC by training regime (SFT vs.\\ RL). Grouped bar chart showing cliff-like degradation for probability-based signals vs.\\ retention for Self-Critique.\\vspace{2em}}}\n    \\caption{Detection signal AUC across training regimes. \\textbf{[PLACEHOLDER: exp-008]}}\n    \\label{fig:signal_survival}\n\\end{figure}",
  "new_string": "\\subsection{Results}\n\\label{sec:results}\n\nWe organize results around four claims: contamination effects are domain-heterogeneous (\\S\\ref{sec:res_domain}), existing detection signals fail in predictable ways (\\S\\ref{sec:res_signal}), $\\gamma$ identifiability has sharp boundaries (\\S\\ref{sec:res_identifiability}), and calibration value derives from IRT ability estimation rather than $\\gamma$ correction (\\S\\ref{sec:res_calibration}).\n\n\\subsubsection{Domain-Differential Contamination Effects}\n\\label{sec:res_domain}\n\nBenchmark-level contamination estimates mask substantial within-benchmark heterogeneity. We fit 2PL+$\\gamma$ models at the MMLU domain level ($N=23$ respondents, 8 domains) and find that contamination effects range from strong inflation to null to negative, depending on domain.\n\nTable~\\ref{tab:domain_gamma} reports domain-level results. STEM\\_Math ($\\hat{\\gamma}=0.969$, PPP$=0.438$, 95\\% CI excludes zero) and STEM\\_Science ($\\hat{\\gamma}=0.838$, PPP$=0.807$, CI excludes zero) show strong positive contamination effects: memorization of injected items inflates measured accuracy. In contrast, STEM\\_CS\\_Eng ($\\hat{\\gamma}=0.197$, CI includes zero), Medical (negative $\\hat{\\gamma}$), Humanities (negative, $\\hat{R}=1.014$), and Social\\_Sciences (negative) show null or deflation effects. Business\\_Law is non-significant.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l r r c r l}\n\\toprule\n\\textbf{Domain} & $N_{\\text{items}}$ & $\\hat{\\gamma}$ & \\textbf{95\\% CI} & \\textbf{PPP} & \\textbf{Interpretation} \\\\\n\\midrule\nSTEM\\_Math & 1190 & 0.969 & excl.\\ 0 & 0.438 & inflation \\\\\nSTEM\\_Science & 1397 & 0.838 & excl.\\ 0 & 0.807 & inflation \\\\\nSTEM\\_CS\\_Eng & 557 & 0.197 & incl.\\ 0 & 0.892 & null \\\\\nMedical & -- & $<0$ & excl.\\ 0 & -- & deflation \\\\\nHumanities & -- & $<0$ & excl.\\ 0 & -- & deflation$^\\dagger$ \\\\\nSocial\\_Sciences & -- & $<0$ & excl.\\ 0 & -- & deflation \\\\\nBusiness\\_Law & -- & -- & incl.\\ 0 & -- & null \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Cross-benchmark (2PL+$\\gamma$, Qwen-only)}} \\\\\nARC (N=16) & 1172 & 0.727 & [0.02, 1.44] & 0.003 & inflation$^\\ddagger$ \\\\\nGSM8K (N=24) & 1319 & 0.064 & [$-$0.36, 0.49] & 0.541 & null \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Domain-level contamination effects under 2PL+$\\gamma$. $^\\dagger$Marginal convergence ($\\hat{R}=1.014$). $^\\ddagger$Low PPP indicates imperfect model fit; interpret $\\hat{\\gamma}$ with caution.}\n\\label{tab:domain_gamma}\n\\end{table}\n\n\\paragraph{Dilution masking.} When MMLU is analyzed at the pooled benchmark level ($N=16$), the aggregate estimate is $\\hat{\\gamma}=0.655$ with CI$=[-0.41, 1.74]$, which does not exclude zero. The positive STEM effects ($\\hat{\\gamma} \\approx 0.84$--$0.97$) are averaged with negative non-STEM effects, producing an aggregate null. This dilution masking phenomenon explains why prior benchmark-level contamination analyses report inconsistent findings: heterogeneous domain effects cancel when pooled.\n\n\\paragraph{Cross-benchmark patterns.} ARC shows a positive effect ($\\hat{\\gamma}=0.727$, CI$=[0.02, 1.44]$), though the low PPP (0.003) indicates the 2PL+$\\gamma$ model fits ARC data poorly. GSM8K shows no contamination effect ($\\hat{\\gamma}=0.064$), consistent with the hypothesis that free-form mathematical reasoning resists memorization-based inflation.\n\n\\paragraph{Cross-family analysis.} Pooling Qwen and Llama families (D122 v3) collapses all effects: ARC $\\hat{\\gamma}=0.002$ (from 0.73 Qwen-only), MMLU $\\hat{\\gamma}=0.213$, GSM8K $\\hat{\\gamma}=-0.110$, all CIs including zero. This reveals that contamination effects are family-specific. The IRT $\\theta$ estimates remain well-calibrated cross-family (calMAE: 0.015, 0.017, 0.008 for MMLU, ARC, GSM8K), indicating that ability estimation generalizes even when $\\gamma$ does not. These results support per-family contamination modeling rather than universal correction factors.\n\nFigure~\\ref{fig:domain_gamma} visualizes the domain-level heterogeneity. Figure~\\ref{fig:dose_response} shows dose-response curves confirming monotonic inflation in STEM domains.\n\n\\subsubsection{Detection Signal Failure}\n\\label{sec:res_signal}\n\nThe four-signal RRF ensemble degrades in practice to a single reliable signal. We evaluate signal discriminability (AUC for contaminated vs.\\ clean items) at the lowest non-trivial dosage (d005, 0.5B scale) where detection is most challenging.\n\n\\paragraph{Signal-level AUC.} Embedding retrieval achieves near-perfect discrimination (AUC: MMLU 0.953, GSM8K 0.988, ARC 0.995). Min-K++ performs \\emph{below chance} across all benchmarks (AUC: MMLU 0.466, GSM8K 0.465, ARC 0.466), indicating a directional reversal where contaminated items receive \\emph{lower} membership scores than clean items. Self-Critique is near chance (AUC: MMLU 0.517, GSM8K 0.495, ARC 0.433).\n\n\\paragraph{Min-K++ reversal.} The below-chance AUC is not random noise but a systematic directional failure. At d100 across model scales, Min-K++ yields Cohen's $d = -1.98$ (strong negative separation), compared to $+3.6$ for embedding retrieval and $+0.45$ for Self-Critique. This reversal occurs because SFT on paraphrased items \\emph{increases} model perplexity on the original surface forms, inverting the membership signal. Exploratory cross-family analysis (Llama-3.2-3B, $N=4$) replicates the reversal direction.\n\n\\paragraph{Practical implication.} In the IRT+MIA framework, RRF aggregation assigns equal fusion weight to all signals. When $K-1$ of $K$ signals carry no information or reversed information, the fused exposure score inherits noise that propagates into $\\gamma$ estimation. The measurement error model (\\S\\ref{sec:stage2}) partially absorbs this noise, but signal failure at the detection stage imposes a fundamental ceiling on contamination quantification.\n\nFigure~\\ref{fig:signal_heatmap} displays the signal-by-benchmark AUC matrix.\n\n\\subsubsection{Identifiability Boundaries}\n\\label{sec:res_identifiability}\n\nWe characterize the $(N, \\text{AUC})$ conditions under which $\\gamma$ is recoverable via analytical Fisher information and simulation sweeps.\n\n\\paragraph{Power thresholds.} The Fisher information analysis yields 80\\% power boundaries: AUC$\\geq$0.80 requires $N\\geq$12--16 respondents; AUC$\\geq$0.75 requires $N\\geq$20; AUC$\\geq$0.70 requires $N\\geq$30; AUC$\\geq$0.65 requires $N\\geq$50. CI width scales as $N^{-0.48}$, near the theoretical $\\sqrt{N}$ rate.\n\n\\paragraph{Simulation validation.} We run recovery simulations across the $(N, \\text{AUC})$ grid. At AUC$=$0.55 (near the boundary of informative detection), recovery succeeds with $N\\geq$50 (10/10 seeds). At AUC$=$0.80, recovery succeeds with $N=$20 (10/10 seeds). These results confirm that $\\gamma$ recovery is structurally possible at low signal quality, but requires sample sizes beyond typical LLM evaluation practice.\n\n\\paragraph{Mismatch with LLM evaluation.} Current LLM benchmarking operates at $N=$8--30 models per evaluation. Given that practical detection AUC concentrates at 0.45--0.55 for all signals except embedding retrieval (\\S\\ref{sec:res_signal}), most $(N, \\text{AUC})$ operating points fall below the identifiability boundary. This is a domain-method mismatch specific to the IRT+MIA framework in LLM evaluation, not a general impossibility result.\n\nFigure~\\ref{fig:identifiability_heatmap} displays the Fisher power surface with current operating points marked.\n\n\\subsubsection{Calibration Value Decomposition}\n\\label{sec:res_calibration}\n\nWe isolate the source of calibration improvement by comparing vanilla 2PL (no contamination covariate) against 2PL+$\\gamma$ under matched conditions ($N=16$, Qwen-only).\n\n\\paragraph{$\\gamma$ provides no calibration benefit.} Table~\\ref{tab:baselines} reports calibration MAE. The vanilla 2PL and 2PL+$\\gamma$ models achieve near-identical performance: GSM8K calMAE 0.0063 vs.\\ 0.0062, MMLU 0.0068 vs.\\ 0.0070, ARC 0.0158 vs.\\ 0.0201 (vanilla slightly better). Adding $\\gamma$ does not reduce calibration error because the IRT ability parameter $\\theta$ already absorbs contamination-induced performance variation through its latent trait estimation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\n\\textbf{Method} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{calMAE $\\downarrow$}} \\\\\nRaw scores & 0.016 & 0.163 & 0.034 \\\\\nVanilla 2PL ($\\gamma=0$) & 0.0068 & 0.0063 & 0.0158 \\\\\n2PL+$\\gamma$ & 0.0070 & 0.0062 & 0.0201 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{$\\Delta$MAE (raw $-$ calibrated)}} \\\\\n2PL+$\\gamma$ & 0.010 & 0.155 & 0.018 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Calibration comparison ($N=16$, Qwen-only, all scales pooled). Adding $\\gamma$ provides no improvement over vanilla 2PL; both reduce raw error substantially through $\\theta$ estimation.}\n\\label{tab:baselines}\n\\end{table}\n\n\\paragraph{Calibration from $\\theta$ estimation.} The large $\\Delta$MAE reductions (0.155 for GSM8K, 0.018 for ARC, 0.010 for MMLU) derive entirely from IRT ability estimation. By mapping raw accuracies onto a latent ability scale and back-transforming through item parameters, the IRT framework corrects for item difficulty variation that inflates or deflates benchmark-level scores. This correction operates independently of contamination detection.\n\n\\paragraph{$\\gamma$ as diagnostic, not corrective.} The value of $\\gamma$ is diagnostic rather than corrective. Domain-level $\\gamma$ estimation (\\S\\ref{sec:res_domain}) reveals which knowledge areas are susceptible to memorization-based inflation, enabling targeted benchmark maintenance decisions. But for the practical goal of score calibration, $\\theta$ alone suffices.\n\n\\paragraph{Cross-family calibration.} The $\\theta$-based calibration transfers across model families without retraining: pooled Qwen+Llama calMAE is 0.017 (MMLU), 0.015 (ARC), 0.008 (GSM8K), with $\\Delta$MAE of 0.028, 0.055, and 0.171 respectively. This cross-family validity confirms that IRT ability estimation captures a stable latent construct independent of architecture-specific contamination patterns.\n\nFigure~\\ref{fig:calibration} shows calibrated vs.\\ true accuracy scatter plots across benchmarks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "uuid": "825bb6f1-bb0d-4b6b-b5a3-26874052d5c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FwuhrEHjh4oYSFxT3efq9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3044,
      "cache_read_input_tokens": 32322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3044
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

_source line 12 · 2026-05-17T02:13:27.483Z_

<details><summary>↩ Tool result · `toolu_01UEFRoNSGGbZrsqD4QYK38S`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "uuid": "e863bb11-e7d4-49e4-a02d-99945f3dfa6a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experiments.tex",
    "oldString": "\\subsection{Results}\n\\label{sec:results}\n\n\\paragraph{Main calibration results.}\nTable~\\ref{tab:main_results} presents calibration performance across all methods and benchmarks. \\textbf{[PLACEHOLDER: exp-006]} ContamCal achieves MAE of \\textbf{[PLACEHOLDER: exp-006]} percentage points averaged across benchmarks, compared to \\textbf{[PLACEHOLDER: exp-006]} for the best baseline (B6, DCR). The 95\\% credible intervals achieve \\textbf{[PLACEHOLDER: exp-006]}\\% coverage (nominal: 95\\%), with average width of \\textbf{[PLACEHOLDER: exp-006]} percentage points. Ranking preservation (Kendall's~$\\tau$) is \\textbf{[PLACEHOLDER: exp-006]}, indicating that calibration largely preserves the ground-truth model ordering.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l cccc c}\n\\toprule\n\\textbf{Method} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC-C} & \\textbf{HE} & \\textbf{Avg} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{MAE $\\downarrow$ (percentage points)}} \\\\\nB0. Raw & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB1. Remove-rescore & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB5. Emperor's & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB6. DCR & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{50\\% CI Coverage $\\uparrow$ (nominal: 50\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{80\\% CI Coverage $\\uparrow$ (nominal: 80\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{95\\% CI Coverage $\\uparrow$ (nominal: 95\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Kendall's $\\tau$ $\\uparrow$}} \\\\\nB0. Raw & X.XX & X.XX & X.XX & X.XX & X.XX \\\\\nB6. DCR & X.XX & X.XX & X.XX & X.XX & X.XX \\\\\n\\textbf{ContamCal} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Main calibration results across four benchmarks. \\textbf{[PLACEHOLDER: exp-006]} MAE: mean absolute error between calibrated and ground-truth clean accuracy (lower is better). Coverage at 50\\%/80\\%/95\\%: fraction of true values within credible interval (closer to nominal is better). HE\\,=\\,HumanEval, ARC-C\\,=\\,ARC-Challenge. Best results in \\textbf{bold}.}\n\\label{tab:main_results}\n\\end{table}\n\n\\paragraph{RRF signal ablation.}\nTable~\\ref{tab:rrf_ablation} reports signal aggregation ablations. \\textbf{[PLACEHOLDER: exp-003]} Full four-signal RRF achieves AUC of \\textbf{[PLACEHOLDER: exp-003]} for contaminated-vs-clean discrimination, compared to \\textbf{[PLACEHOLDER: exp-003]} for the best single signal. Drop-one analysis reveals that removing \\textbf{[PLACEHOLDER: exp-003]} causes the largest AUC decrease, while removing \\textbf{[PLACEHOLDER: exp-003]} has minimal impact, suggesting complementary rather than redundant signal contributions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AUC} & \\textbf{$\\Delta$AUC} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Single-signal}} \\\\\nEmbedding retrieval & [TBD] & --- \\\\\nMin-K\\%++ & [TBD] & --- \\\\\nConStat & [TBD] & --- \\\\\nSelf-Critique & [TBD] & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Drop-one from full RRF}} \\\\\n$-$ Embedding & [TBD] & [TBD] \\\\\n$-$ Min-K\\%++ & [TBD] & [TBD] \\\\\n$-$ ConStat & [TBD] & [TBD] \\\\\n$-$ Self-Critique & [TBD] & [TBD] \\\\\n\\midrule\nFull RRF (4 signals) & \\textbf{[TBD]} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Signal aggregation ablation. \\textbf{[PLACEHOLDER: exp-003]} AUC for contaminated-vs-clean item discrimination, averaged across benchmarks and model scales. $\\Delta$AUC: change relative to full RRF.}\n\\label{tab:rrf_ablation}\n\\end{table}\n\n\\paragraph{RRF $k$-sensitivity.}\nTable~\\ref{tab:k_sensitivity} shows that calibration MAE and detection AUC are stable across $k \\in \\{20, 40, 60, 80, 100\\}$, confirming that ContamCal is not sensitive to the RRF smoothing constant. \\textbf{[PLACEHOLDER: exp-003]}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccccc}\n\\toprule\n$k$ & 20 & 40 & \\textbf{60} & 80 & 100 \\\\\n\\midrule\nMAE & [TBD] & [TBD] & \\textbf{[TBD]} & [TBD] & [TBD] \\\\\nAUC & [TBD] & [TBD] & \\textbf{[TBD]} & [TBD] & [TBD] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to RRF smoothing constant~$k$. \\textbf{[PLACEHOLDER: exp-003]} Default $k\\!=\\!60$ in bold.}\n\\label{tab:k_sensitivity}\n\\end{table}\n\n\\paragraph{Dose-response curves.}\nFigure~\\ref{fig:dose_response} plots raw accuracy, calibrated accuracy, and ground-truth clean accuracy as a function of contamination dosage for each benchmark and model scale. \\textbf{[PLACEHOLDER: exp-006]} Raw scores inflate monotonically with dosage, while calibrated scores remain approximately flat, tracking the ground-truth clean performance. The posterior mean $\\hat{\\gamma}_k$ increases monotonically with dosage across all benchmarks (Spearman $\\rho =$ \\textbf{[PLACEHOLDER: exp-006]}, $p <$ \\textbf{[PLACEHOLDER: exp-006]}).\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/dose_response.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-006]}\\\\ Dose-response curves: raw vs.\\ calibrated vs.\\ ground-truth accuracy across 5 dosage levels, faceted by benchmark and model scale. Shaded bands = 95\\% credible intervals.\\vspace{2em}}}\n    \\caption{Dose-response curves across four benchmarks and three model scales (0.5B, 1.5B, 3B). \\textbf{[PLACEHOLDER: exp-006]}}\n    \\label{fig:dose_response}\n\\end{figure}\n\n\\paragraph{Uncertainty calibration and noise propagation.}\nFigure~\\ref{fig:ci_width} shows credible interval width as a function of measurement error variance~$\\sigma_e^2$ (Eq.~\\eqref{eq:measurement_error}). \\textbf{[PLACEHOLDER: exp-005]} As detection signal noise increases, ContamCal produces appropriately wider intervals while maintaining nominal coverage. This confirms that the measurement error model successfully propagates detection uncertainty into the calibrated scores.\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/ci_width_noise.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-005]}\\\\ CI width and coverage vs.\\ measurement error variance $\\sigma_e^2$. Coverage should remain near nominal as width increases.\\vspace{2em}}}\n    \\caption{Credible interval width (left axis) and coverage (right axis) as a function of measurement error variance. \\textbf{[PLACEHOLDER: exp-005]}}\n    \\label{fig:ci_width}\n\\end{figure}\n\n\\paragraph{Signal survival under RL.}\nFigure~\\ref{fig:signal_survival} presents detection signal AUCs across training regimes (SFT vs.\\ RL with GRPO). \\textbf{[PLACEHOLDER: exp-008]} Probability-based signals (Min-K\\%++, ConStat) degrade from AUC \\textbf{[PLACEHOLDER: exp-008]} under SFT to \\textbf{[PLACEHOLDER: exp-008]} under RL---a cliff-like drop rather than gradual attenuation, consistent with the hypothesis in \\S\\ref{sec:signal_survival}. Self-Critique retains higher AUC of \\textbf{[PLACEHOLDER: exp-008]} post-RL, validating its inclusion as a robustness anchor in the signal ensemble. This regime-dependent degradation is automatically captured by the measurement error model: RL-trained models receive wider credible intervals reflecting genuine epistemic uncertainty about their contamination status.\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/signal_survival.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-008, if available]}\\\\ Signal AUC by training regime (SFT vs.\\ RL). Grouped bar chart showing cliff-like degradation for probability-based signals vs.\\ retention for Self-Critique.\\vspace{2em}}}\n    \\caption{Detection signal AUC across training regimes. \\textbf{[PLACEHOLDER: exp-008]}}\n    \\label{fig:signal_survival}\n\\end{figure}",
    "newString": "\\subsection{Results}\n\\label{sec:results}\n\nWe organize results around four claims: contamination effects are domain-heterogeneous (\\S\\ref{sec:res_domain}), existing detection signals fail in predictable ways (\\S\\ref{sec:res_signal}), $\\gamma$ identifiability has sharp boundaries (\\S\\ref{sec:res_identifiability}), and calibration value derives from IRT ability estimation rather than $\\gamma$ correction (\\S\\ref{sec:res_calibration}).\n\n\\subsubsection{Domain-Differential Contamination Effects}\n\\label{sec:res_domain}\n\nBenchmark-level contamination estimates mask substantial within-benchmark heterogeneity. We fit 2PL+$\\gamma$ models at the MMLU domain level ($N=23$ respondents, 8 domains) and find that contamination effects range from strong inflation to null to negative, depending on domain.\n\nTable~\\ref{tab:domain_gamma} reports domain-level results. STEM\\_Math ($\\hat{\\gamma}=0.969$, PPP$=0.438$, 95\\% CI excludes zero) and STEM\\_Science ($\\hat{\\gamma}=0.838$, PPP$=0.807$, CI excludes zero) show strong positive contamination effects: memorization of injected items inflates measured accuracy. In contrast, STEM\\_CS\\_Eng ($\\hat{\\gamma}=0.197$, CI includes zero), Medical (negative $\\hat{\\gamma}$), Humanities (negative, $\\hat{R}=1.014$), and Social\\_Sciences (negative) show null or deflation effects. Business\\_Law is non-significant.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l r r c r l}\n\\toprule\n\\textbf{Domain} & $N_{\\text{items}}$ & $\\hat{\\gamma}$ & \\textbf{95\\% CI} & \\textbf{PPP} & \\textbf{Interpretation} \\\\\n\\midrule\nSTEM\\_Math & 1190 & 0.969 & excl.\\ 0 & 0.438 & inflation \\\\\nSTEM\\_Science & 1397 & 0.838 & excl.\\ 0 & 0.807 & inflation \\\\\nSTEM\\_CS\\_Eng & 557 & 0.197 & incl.\\ 0 & 0.892 & null \\\\\nMedical & -- & $<0$ & excl.\\ 0 & -- & deflation \\\\\nHumanities & -- & $<0$ & excl.\\ 0 & -- & deflation$^\\dagger$ \\\\\nSocial\\_Sciences & -- & $<0$ & excl.\\ 0 & -- & deflation \\\\\nBusiness\\_Law & -- & -- & incl.\\ 0 & -- & null \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Cross-benchmark (2PL+$\\gamma$, Qwen-only)}} \\\\\nARC (N=16) & 1172 & 0.727 & [0.02, 1.44] & 0.003 & inflation$^\\ddagger$ \\\\\nGSM8K (N=24) & 1319 & 0.064 & [$-$0.36, 0.49] & 0.541 & null \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Domain-level contamination effects under 2PL+$\\gamma$. $^\\dagger$Marginal convergence ($\\hat{R}=1.014$). $^\\ddagger$Low PPP indicates imperfect model fit; interpret $\\hat{\\gamma}$ with caution.}\n\\label{tab:domain_gamma}\n\\end{table}\n\n\\paragraph{Dilution masking.} When MMLU is analyzed at the pooled benchmark level ($N=16$), the aggregate estimate is $\\hat{\\gamma}=0.655$ with CI$=[-0.41, 1.74]$, which does not exclude zero. The positive STEM effects ($\\hat{\\gamma} \\approx 0.84$--$0.97$) are averaged with negative non-STEM effects, producing an aggregate null. This dilution masking phenomenon explains why prior benchmark-level contamination analyses report inconsistent findings: heterogeneous domain effects cancel when pooled.\n\n\\paragraph{Cross-benchmark patterns.} ARC shows a positive effect ($\\hat{\\gamma}=0.727$, CI$=[0.02, 1.44]$), though the low PPP (0.003) indicates the 2PL+$\\gamma$ model fits ARC data poorly. GSM8K shows no contamination effect ($\\hat{\\gamma}=0.064$), consistent with the hypothesis that free-form mathematical reasoning resists memorization-based inflation.\n\n\\paragraph{Cross-family analysis.} Pooling Qwen and Llama families (D122 v3) collapses all effects: ARC $\\hat{\\gamma}=0.002$ (from 0.73 Qwen-only), MMLU $\\hat{\\gamma}=0.213$, GSM8K $\\hat{\\gamma}=-0.110$, all CIs including zero. This reveals that contamination effects are family-specific. The IRT $\\theta$ estimates remain well-calibrated cross-family (calMAE: 0.015, 0.017, 0.008 for MMLU, ARC, GSM8K), indicating that ability estimation generalizes even when $\\gamma$ does not. These results support per-family contamination modeling rather than universal correction factors.\n\nFigure~\\ref{fig:domain_gamma} visualizes the domain-level heterogeneity. Figure~\\ref{fig:dose_response} shows dose-response curves confirming monotonic inflation in STEM domains.\n\n\\subsubsection{Detection Signal Failure}\n\\label{sec:res_signal}\n\nThe four-signal RRF ensemble degrades in practice to a single reliable signal. We evaluate signal discriminability (AUC for contaminated vs.\\ clean items) at the lowest non-trivial dosage (d005, 0.5B scale) where detection is most challenging.\n\n\\paragraph{Signal-level AUC.} Embedding retrieval achieves near-perfect discrimination (AUC: MMLU 0.953, GSM8K 0.988, ARC 0.995). Min-K++ performs \\emph{below chance} across all benchmarks (AUC: MMLU 0.466, GSM8K 0.465, ARC 0.466), indicating a directional reversal where contaminated items receive \\emph{lower} membership scores than clean items. Self-Critique is near chance (AUC: MMLU 0.517, GSM8K 0.495, ARC 0.433).\n\n\\paragraph{Min-K++ reversal.} The below-chance AUC is not random noise but a systematic directional failure. At d100 across model scales, Min-K++ yields Cohen's $d = -1.98$ (strong negative separation), compared to $+3.6$ for embedding retrieval and $+0.45$ for Self-Critique. This reversal occurs because SFT on paraphrased items \\emph{increases} model perplexity on the original surface forms, inverting the membership signal. Exploratory cross-family analysis (Llama-3.2-3B, $N=4$) replicates the reversal direction.\n\n\\paragraph{Practical implication.} In the IRT+MIA framework, RRF aggregation assigns equal fusion weight to all signals. When $K-1$ of $K$ signals carry no information or reversed information, the fused exposure score inherits noise that propagates into $\\gamma$ estimation. The measurement error model (\\S\\ref{sec:stage2}) partially absorbs this noise, but signal failure at the detection stage imposes a fundamental ceiling on contamination quantification.\n\nFigure~\\ref{fig:signal_heatmap} displays the signal-by-benchmark AUC matrix.\n\n\\subsubsection{Identifiability Boundaries}\n\\label{sec:res_identifiability}\n\nWe characterize the $(N, \\text{AUC})$ conditions under which $\\gamma$ is recoverable via analytical Fisher information and simulation sweeps.\n\n\\paragraph{Power thresholds.} The Fisher information analysis yields 80\\% power boundaries: AUC$\\geq$0.80 requires $N\\geq$12--16 respondents; AUC$\\geq$0.75 requires $N\\geq$20; AUC$\\geq$0.70 requires $N\\geq$30; AUC$\\geq$0.65 requires $N\\geq$50. CI width scales as $N^{-0.48}$, near the theoretical $\\sqrt{N}$ rate.\n\n\\paragraph{Simulation validation.} We run recovery simulations across the $(N, \\text{AUC})$ grid. At AUC$=$0.55 (near the boundary of informative detection), recovery succeeds with $N\\geq$50 (10/10 seeds). At AUC$=$0.80, recovery succeeds with $N=$20 (10/10 seeds). These results confirm that $\\gamma$ recovery is structurally possible at low signal quality, but requires sample sizes beyond typical LLM evaluation practice.\n\n\\paragraph{Mismatch with LLM evaluation.} Current LLM benchmarking operates at $N=$8--30 models per evaluation. Given that practical detection AUC concentrates at 0.45--0.55 for all signals except embedding retrieval (\\S\\ref{sec:res_signal}), most $(N, \\text{AUC})$ operating points fall below the identifiability boundary. This is a domain-method mismatch specific to the IRT+MIA framework in LLM evaluation, not a general impossibility result.\n\nFigure~\\ref{fig:identifiability_heatmap} displays the Fisher power surface with current operating points marked.\n\n\\subsubsection{Calibration Value Decomposition}\n\\label{sec:res_calibration}\n\nWe isolate the source of calibration improvement by comparing vanilla 2PL (no contamination covariate) against 2PL+$\\gamma$ under matched conditions ($N=16$, Qwen-only).\n\n\\paragraph{$\\gamma$ provides no calibration benefit.} Table~\\ref{tab:baselines} reports calibration MAE. The vanilla 2PL and 2PL+$\\gamma$ models achieve near-identical performance: GSM8K calMAE 0.0063 vs.\\ 0.0062, MMLU 0.0068 vs.\\ 0.0070, ARC 0.0158 vs.\\ 0.0201 (vanilla slightly better). Adding $\\gamma$ does not reduce calibration error because the IRT ability parameter $\\theta$ already absorbs contamination-induced performance variation through its latent trait estimation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\n\\textbf{Method} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{calMAE $\\downarrow$}} \\\\\nRaw scores & 0.016 & 0.163 & 0.034 \\\\\nVanilla 2PL ($\\gamma=0$) & 0.0068 & 0.0063 & 0.0158 \\\\\n2PL+$\\gamma$ & 0.0070 & 0.0062 & 0.0201 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{$\\Delta$MAE (raw $-$ calibrated)}} \\\\\n2PL+$\\gamma$ & 0.010 & 0.155 & 0.018 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Calibration comparison ($N=16$, Qwen-only, all scales pooled). Adding $\\gamma$ provides no improvement over vanilla 2PL; both reduce raw error substantially through $\\theta$ estimation.}\n\\label{tab:baselines}\n\\end{table}\n\n\\paragraph{Calibration from $\\theta$ estimation.} The large $\\Delta$MAE reductions (0.155 for GSM8K, 0.018 for ARC, 0.010 for MMLU) derive entirely from IRT ability estimation. By mapping raw accuracies onto a latent ability scale and back-transforming through item parameters, the IRT framework corrects for item difficulty variation that inflates or deflates benchmark-level scores. This correction operates independently of contamination detection.\n\n\\paragraph{$\\gamma$ as diagnostic, not corrective.} The value of $\\gamma$ is diagnostic rather than corrective. Domain-level $\\gamma$ estimation (\\S\\ref{sec:res_domain}) reveals which knowledge areas are susceptible to memorization-based inflation, enabling targeted benchmark maintenance decisions. But for the practical goal of score calibration, $\\theta$ alone suffices.\n\n\\paragraph{Cross-family calibration.} The $\\theta$-based calibration transfers across model families without retraining: pooled Qwen+Llama calMAE is 0.017 (MMLU), 0.015 (ARC), 0.008 (GSM8K), with $\\Delta$MAE of 0.028, 0.055, and 0.171 respectively. This cross-family validity confirms that IRT ability estimation captures a stable latent construct independent of architecture-specific contamination patterns.\n\nFigure~\\ref{fig:calibration} shows calibrated vs.\\ true accuracy scatter plots across benchmarks.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ContamCal through controlled contamination injection across multiple model scales, dosage levels, and benchmarks. The experimental design provides ground-truth clean performance for every configuration, enabling direct measurement of calibration quality.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\nOur evaluation follows a controlled SFT injection pipeline: we deliberately contaminate models at known dosage levels, compute detection signals, fit the contamination-augmented IRT model, and compare calibrated scores against the known ground truth. This design provides the internal validity necessary for rigorous evaluation---we know the true contamination status of every item for every model.\n\nWe use the Qwen2.5 model family at three scales---0.5B, 1.5B, and 3B parameters---all fine-tuned via LoRA. A separate Qwen2.5-7B-Instruct model serves as the paraphrase generator for ConStat signal computation (\\S\\ref{sec:stage1}). We evaluate on four benchmarks spanning diverse evaluation modalities:\n\\begin{itemize}\n    \\item \\textbf{MMLU} \\citep{hendrycks2021mmlu}: knowledge-intensive multiple-choice (14,042 items);\n    \\item \\textbf{GSM8K} \\citep{cobbe2021gsm8k}: mathematical reasoning with free-form answers (1,319 items);\n    \\item \\textbf{ARC-Challenge} \\citep{clark2018arc}: science reasoning multiple-choice (1,172 items);\n    \\item \\textbf{HumanEval} \\citep{chen2021humaneval}: code generation with execution-based evaluation (164 items).\n\\end{itemize}\nHumanEval's small item count may limit 4PL parameter estimation reliability; we include it to test ContamCal at the boundary of applicability.\n\n\\subsection{Controlled Contamination Injection}\n\\label{sec:injection}\n\nFor each model scale, we inject contamination at five dosage levels: 0\\% (clean baseline), 5\\%, 25\\%, 50\\%, and 100\\% of benchmark items. At each dosage level~$d$, a random subset of $\\lfloor d \\cdot |B| \\rfloor$ items from benchmark~$B$ is selected for injection. Selected items are paraphrased using the 7B-Instruct model to produce surface-form variants that evade $n$-gram decontamination, following the protocol of \\citet{yang2026rl}. Models are then fine-tuned via LoRA ($r\\!=\\!16$, $\\alpha\\!=\\!32$) on the paraphrased items mixed with a held-out instruction-tuning corpus, for 1 epoch with learning rate $2 \\times 10^{-4}$.\n\nEach configuration (3 model scales $\\times$ 5 dosage levels) is run with 3 random seeds controlling both item selection and LoRA initialization, yielding 45 model checkpoints, each evaluated on 4 benchmarks (180 model--benchmark evaluation pairs). The 0\\%-dosage models serve as ground-truth baselines for computing calibration error.\n\n\\subsection{Detection Signals and Aggregation}\n\\label{sec:exp_signals}\n\nWe compute four detection signals on all model--item pairs, as described in \\S\\ref{sec:stage1}. \\textbf{Embedding retrieval} indexes the training corpus via a sentence transformer and retrieves near-duplicate benchmark items by cosine similarity. \\textbf{Min-K\\%++} computes membership inference statistics using the 0\\%-dosage model of matching scale as reference. \\textbf{ConStat} measures the accuracy gap between original and paraphrased item variants. \\textbf{Self-Critique} quantifies entropy collapse in model self-evaluations. Signals are aggregated via RRF (Eq.~\\eqref{eq:rrf}) with $k\\!=\\!60$.\n\nWe conduct three ablation studies on signal aggregation: (i)~a \\emph{drop-one} ablation that removes each signal in turn to assess marginal contribution; (ii)~a \\emph{single-signal} ablation evaluating each signal independently; and (iii)~a $k$-sensitivity sweep over $k \\in \\{20, 40, 60, 80, 100\\}$. All ablations report AUC for contaminated-vs-clean item discrimination.\n\n\\subsection{IRT Calibration and Baselines}\n\\label{sec:exp_irt}\n\nWe fit the contamination-augmented 4PL IRT model (Eq.~\\eqref{eq:4pl}) separately per benchmark using CmdStanPy \\citep{carpenter2017} with the NUTS sampler \\citep{hoffman2014}. Each fit uses 4 independent chains of 2,000 iterations (1,000 warmup), with convergence assessed via split-$\\hat{R} < 1.01$, $\\text{ESS} > 400$, and $< 0.1\\%$ divergent transitions (\\S\\ref{sec:inference}). The measurement error model (Eq.~\\eqref{eq:measurement_error}) treats RRF exposure scores as noisy proxies for latent contamination~$\\tau_{ij}$. Calibrated scores are computed via Eq.~\\eqref{eq:calibrated_mc} by setting exposure to zero and marginalizing over posterior draws.\n\nWe also fit an analytical measurement error (ME) variant that eliminates latent $\\tau$ parameters via conjugate normal integration, retaining MCMC (Stan NUTS) for the remaining IRT parameters. This provides scalability to large item pools (e.g., MMLU's 14K items) without introducing additional latent variables.\n\nWe compare ContamCal against seven baselines:\n\\begin{enumerate}\n    \\item[\\textbf{B0.}] \\textbf{Raw}: original benchmark scores with no adjustment, serving as the anchor for quantifying contamination inflation.\n    \\item[\\textbf{B1.}] \\textbf{Remove-and-rescore}: items with RRF exposure score above the 75th percentile are removed; accuracy is recomputed on remaining items.\n    \\item[\\textbf{B2.}] \\textbf{Single-signal 2PL+$\\boldsymbol{\\gamma}$}: the best-performing single detection signal (by AUC) enters a 2PL IRT model with contamination covariate~$\\gamma$ but without guessing ($c\\!=\\!0$) or slip ($d\\!=\\!1$) parameters.\n    \\item[\\textbf{B3.}] \\textbf{Vanilla 4PL} ($\\boldsymbol{\\gamma\\!=\\!0}$): standard 4PL IRT without contamination covariate, representing current IRT-based evaluation practice \\citep{gu2026psnirt,polo2026growing}.\n    \\item[\\textbf{B4.}] \\textbf{Linear exposure regression}: $\\text{Acc}_i = \\beta_0 + \\beta_1 \\bar{e}_i + \\epsilon$, where $\\bar{e}_i$ is the mean RRF exposure score, with bootstrap confidence intervals. Tests whether a simple regression suffices without the IRT machinery.\n    \\item[\\textbf{B5.}] \\textbf{Emperor's mitigation}: two representative strategies from \\citet{xu2025emperor}---item rephrasing and option shuffling---applied at evaluation time. We report the better-performing strategy per benchmark.\n    \\item[\\textbf{B6.}] \\textbf{DCR}: the decontaminated calibration and ranking method of \\citet{li2025dcr}, which produces adjusted accuracy via fuzzy inference over detection signals without uncertainty quantification.\n\\end{enumerate}\n\n\\subsection{Evaluation Protocol}\n\\label{sec:eval_protocol}\n\nWe assess calibration quality using five metrics that jointly characterize accuracy, uncertainty quantification, ranking fidelity, and mechanistic validity.\n\n\\paragraph{Calibration error.}\nMean absolute error between the calibrated score $\\widehat{\\text{Acc}}_i^{\\text{cal}}$ (Eq.~\\eqref{eq:calibrated_mc}) and the ground-truth clean accuracy $\\text{Acc}_i^{\\text{clean}}$ measured on 0\\%-dosage models:\n\\begin{equation}\n\\label{eq:mae}\n    \\text{MAE} = \\frac{1}{N} \\sum_{i=1}^{N} \\left| \\widehat{\\text{Acc}}_i^{\\text{cal}} - \\text{Acc}_i^{\\text{clean}} \\right|.\n\\end{equation}\nWe report bootstrap 95\\% confidence intervals computed over 1,000 resamples of model--benchmark pairs.\n\n\\paragraph{Interval coverage.}\nThe fraction of models whose ground-truth clean accuracy falls within the $\\alpha$-level credible interval:\n\\begin{equation}\n\\label{eq:coverage}\n    \\text{Cov}(\\alpha) = \\frac{1}{N} \\sum_{i=1}^{N} \\mathbf{1}\\!\\left[\\text{Acc}_i^{\\text{clean}} \\in \\text{CI}_i^{(\\alpha)}\\right].\n\\end{equation}\nWe evaluate at $\\alpha \\in \\{50\\%, 80\\%, 95\\%\\}$. Nominal coverage ($\\text{Cov}(\\alpha) \\approx \\alpha$) indicates well-calibrated uncertainty. For baselines without native uncertainty quantification (B0, B1, B5, B6), we use bootstrap resampling to construct confidence intervals.\n\n\\paragraph{Interval sharpness.}\nAverage width of the credible interval at coverage level~$\\alpha$:\n\\begin{equation}\n\\label{eq:sharpness}\n    \\text{Sharp}(\\alpha) = \\frac{1}{N} \\sum_{i=1}^{N} \\text{width}\\!\\left(\\text{CI}_i^{(\\alpha)}\\right).\n\\end{equation}\nNarrower intervals are preferred at fixed coverage; the ideal method achieves nominal coverage with minimal width.\n\n\\paragraph{Ranking preservation.}\nKendall's $\\tau$ between the calibrated model ranking and the ground-truth clean ranking:\n\\begin{equation}\n\\label{eq:kendall}\n    \\tau = \\frac{C - D}{\\binom{N}{2}},\n\\end{equation}\nwhere $C$ and $D$ are the numbers of concordant and discordant pairs. Values near 1 indicate that calibration preserves the true model ordering; deviations reveal methods that correct absolute scores but distort relative comparisons.\n\n\\paragraph{Dose-response monotonicity.}\nWe verify that the estimated contamination effect increases monotonically with dosage. Specifically, we compute Spearman's rank correlation between dosage level~$d$ and the posterior mean $\\hat{\\gamma}_k$ across the five dosage conditions per benchmark. Monotonic dose-response is a necessary (though not sufficient) condition for valid contamination modeling.\n\n\\subsection{Results}\n\\label{sec:results}\n\n\\paragraph{Main calibration results.}\nTable~\\ref{tab:main_results} presents calibration performance across all methods and benchmarks. \\textbf{[PLACEHOLDER: exp-006]} ContamCal achieves MAE of \\textbf{[PLACEHOLDER: exp-006]} percentage points averaged across benchmarks, compared to \\textbf{[PLACEHOLDER: exp-006]} for the best baseline (B6, DCR). The 95\\% credible intervals achieve \\textbf{[PLACEHOLDER: exp-006]}\\% coverage (nominal: 95\\%), with average width of \\textbf{[PLACEHOLDER: exp-006]} percentage points. Ranking preservation (Kendall's~$\\tau$) is \\textbf{[PLACEHOLDER: exp-006]}, indicating that calibration largely preserves the ground-truth model ordering.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l cccc c}\n\\toprule\n\\textbf{Method} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC-C} & \\textbf{HE} & \\textbf{Avg} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{MAE $\\downarrow$ (percentage points)}} \\\\\nB0. Raw & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB1. Remove-rescore & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB5. Emperor's & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB6. DCR & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{50\\% CI Coverage $\\uparrow$ (nominal: 50\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{80\\% CI Coverage $\\uparrow$ (nominal: 80\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{95\\% CI Coverage $\\uparrow$ (nominal: 95\\%)}} \\\\\nB2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\nB4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\\n\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Kendall's $\\tau$ $\\uparrow$}} \\\\\nB0. Raw & X.XX & X.XX & X.XX & X.XX & X.XX \\\\\nB6. DCR & X.XX & X.XX & X.XX & X.XX & X.XX \\\\\n\\textbf{ContamCal} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Main calibration results across four benchmarks. \\textbf{[PLACEHOLDER: exp-006]} MAE: mean absolute error between calibrated and ground-truth clean accuracy (lower is better). Coverage at 50\\%/80\\%/95\\%: fraction of true values within credible interval (closer to nominal is better). HE\\,=\\,HumanEval, ARC-C\\,=\\,ARC-Challenge. Best results in \\textbf{bold}.}\n\\label{tab:main_results}\n\\end{table}\n\n\\paragraph{RRF signal ablation.}\nTable~\\ref{tab:rrf_ablation} reports signal aggregation ablations. \\textbf{[PLACEHOLDER: exp-003]} Full four-signal RRF achieves AUC of \\textbf{[PLACEHOLDER: exp-003]} for contaminated-vs-clean discrimination, compared to \\textbf{[PLACEHOLDER: exp-003]} for the best single signal. Drop-one analysis reveals that removing \\textbf{[PLACEHOLDER: exp-003]} causes the largest AUC decrease, while removing \\textbf{[PLACEHOLDER: exp-003]} has minimal impact, suggesting complementary rather than redundant signal contributions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AUC} & \\textbf{$\\Delta$AUC} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Single-signal}} \\\\\nEmbedding retrieval & [TBD] & --- \\\\\nMin-K\\%++ & [TBD] & --- \\\\\nConStat & [TBD] & --- \\\\\nSelf-Critique & [TBD] & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Drop-one from full RRF}} \\\\\n$-$ Embedding & [TBD] & [TBD] \\\\\n$-$ Min-K\\%++ & [TBD] & [TBD] \\\\\n$-$ ConStat & [TBD] & [TBD] \\\\\n$-$ Self-Critique & [TBD] & [TBD] \\\\\n\\midrule\nFull RRF (4 signals) & \\textbf{[TBD]} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Signal aggregation ablation. \\textbf{[PLACEHOLDER: exp-003]} AUC for contaminated-vs-clean item discrimination, averaged across benchmarks and model scales. $\\Delta$AUC: change relative to full RRF.}\n\\label{tab:rrf_ablation}\n\\end{table}\n\n\\paragraph{RRF $k$-sensitivity.}\nTable~\\ref{tab:k_sensitivity} shows that calibration MAE and detection AUC are stable across $k \\in \\{20, 40, 60, 80, 100\\}$, confirming that ContamCal is not sensitive to the RRF smoothing constant. \\textbf{[PLACEHOLDER: exp-003]}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccccc}\n\\toprule\n$k$ & 20 & 40 & \\textbf{60} & 80 & 100 \\\\\n\\midrule\nMAE & [TBD] & [TBD] & \\textbf{[TBD]} & [TBD] & [TBD] \\\\\nAUC & [TBD] & [TBD] & \\textbf{[TBD]} & [TBD] & [TBD] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to RRF smoothing constant~$k$. \\textbf{[PLACEHOLDER: exp-003]} Default $k\\!=\\!60$ in bold.}\n\\label{tab:k_sensitivity}\n\\end{table}\n\n\\paragraph{Dose-response curves.}\nFigure~\\ref{fig:dose_response} plots raw accuracy, calibrated accuracy, and ground-truth clean accuracy as a function of contamination dosage for each benchmark and model scale. \\textbf{[PLACEHOLDER: exp-006]} Raw scores inflate monotonically with dosage, while calibrated scores remain approximately flat, tracking the ground-truth clean performance. The posterior mean $\\hat{\\gamma}_k$ increases monotonically with dosage across all benchmarks (Spearman $\\rho =$ \\textbf{[PLACEHOLDER: exp-006]}, $p <$ \\textbf{[PLACEHOLDER: exp-006]}).\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/dose_response.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-006]}\\\\ Dose-response curves: raw vs.\\ calibrated vs.\\ ground-truth accuracy across 5 dosage levels, faceted by benchmark and model scale. Shaded bands = 95\\% credible intervals.\\vspace{2em}}}\n    \\caption{Dose-response curves across four benchmarks and three model scales (0.5B, 1.5B, 3B). \\textbf{[PLACEHOLDER: exp-006]}}\n    \\label{fig:dose_response}\n\\end{figure}\n\n\\paragraph{Uncertainty calibration and noise propagation.}\nFigure~\\ref{fig:ci_width} shows credible interval width as a function of measurement error variance~$\\sigma_e^2$ (Eq.~\\eqref{eq:measurement_error}). \\textbf{[PLACEHOLDER: exp-005]} As detection signal noise increases, ContamCal produces appropriately wider intervals while maintaining nominal coverage. This confirms that the measurement error model successfully propagates detection uncertainty into the calibrated scores.\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/ci_width_noise.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-005]}\\\\ CI width and coverage vs.\\ measurement error variance $\\sigma_e^2$. Coverage should remain near nominal as width increases.\\vspace{2em}}}\n    \\caption{Credible interval width (left axis) and coverage (right axis) as a function of measurement error variance. \\textbf{[PLACEHOLDER: exp-005]}}\n    \\label{fig:ci_width}\n\\end{figure}\n\n\\paragraph{Signal survival under RL.}\nFigure~\\ref{fig:signal_survival} presents detection signal AUCs across training regimes (SFT vs.\\ RL with GRPO). \\textbf{[PLACEHOLDER: exp-008]} Probability-based signals (Min-K\\%++, ConStat) degrade from AUC \\textbf{[PLACEHOLDER: exp-008]} under SFT to \\textbf{[PLACEHOLDER: exp-008]} under RL---a cliff-like drop rather than gradual attenuation, consistent with the hypothesis in \\S\\ref{sec:signal_survival}. Self-Critique retains higher AUC of \\textbf{[PLACEHOLDER: exp-008]} post-RL, validating its inclusion as a robustness anchor in the signal ensemble. This regime-dependent degradation is automatically captured by the measurement error model: RL-trained models receive wider credible intervals reflecting genuine epistemic uncertainty about their contamination status.\n\n\\begin{figure}[t]\n    \\centering\n    % \\includegraphics[width=\\columnwidth]{figures/signal_survival.pdf}\n    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-008, if available]}\\\\ Signal AUC by training regime (SFT vs.\\ RL). Grouped bar chart showing cliff-like degradation for probability-based signals vs.\\ retention for Self-Critique.\\vspace{2em}}}\n    \\caption{Detection signal AUC across training regimes. \\textbf{[PLACEHOLDER: exp-008]}}\n    \\label{fig:signal_survival}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 92,
        "oldLines": 130,
        "newStart": 92,
        "newLines": 104,
        "lines": [
          " \\subsection{Results}",
          " \\label{sec:results}",
          " ",
          "-\\paragraph{Main calibration results.}",
          "-Table~\\ref{tab:main_results} presents calibration performance across all methods and benchmarks. \\textbf{[PLACEHOLDER: exp-006]} ContamCal achieves MAE of \\textbf{[PLACEHOLDER: exp-006]} percentage points averaged across benchmarks, compared to \\textbf{[PLACEHOLDER: exp-006]} for the best baseline (B6, DCR). The 95\\% credible intervals achieve \\textbf{[PLACEHOLDER: exp-006]}\\% coverage (nominal: 95\\%), with average width of \\textbf{[PLACEHOLDER: exp-006]} percentage points. Ranking preservation (Kendall's~$\\tau$) is \\textbf{[PLACEHOLDER: exp-006]}, indicating that calibration largely preserves the ground-truth model ordering.",
          "+We organize results around four claims: contamination effects are domain-heterogeneous (\\S\\ref{sec:res_domain}), existing detection signals fail in predictable ways (\\S\\ref{sec:res_signal}), $\\gamma$ identifiability has sharp boundaries (\\S\\ref{sec:res_identifiability}), and calibration value derives from IRT ability estimation rather than $\\gamma$ correction (\\S\\ref{sec:res_calibration}).",
          " ",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\small",
          "-\\begin{tabular}{l cccc c}",
          "-\\toprule",
          "-\\textbf{Method} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC-C} & \\textbf{HE} & \\textbf{Avg} \\\\",
          "-\\midrule",
          "-\\multicolumn{6}{l}{\\emph{MAE $\\downarrow$ (percentage points)}} \\\\",
          "-B0. Raw & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B1. Remove-rescore & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B5. Emperor's & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B6. DCR & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\",
          "-\\midrule",
          "-\\multicolumn{6}{l}{\\emph{50\\% CI Coverage $\\uparrow$ (nominal: 50\\%)}} \\\\",
          "-B2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\",
          "-\\midrule",
          "-\\multicolumn{6}{l}{\\emph{80\\% CI Coverage $\\uparrow$ (nominal: 80\\%)}} \\\\",
          "-B2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\",
          "-\\midrule",
          "-\\multicolumn{6}{l}{\\emph{95\\% CI Coverage $\\uparrow$ (nominal: 95\\%)}} \\\\",
          "-B2. 2PL+$\\gamma$ & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B3. Vanilla 4PL & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-B4. Linear reg. & XX.X & XX.X & XX.X & XX.X & XX.X \\\\",
          "-\\textbf{ContamCal} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} & \\textbf{XX.X} \\\\",
          "-\\midrule",
          "-\\multicolumn{6}{l}{\\emph{Kendall's $\\tau$ $\\uparrow$}} \\\\",
          "-B0. Raw & X.XX & X.XX & X.XX & X.XX & X.XX \\\\",
          "-B6. DCR & X.XX & X.XX & X.XX & X.XX & X.XX \\\\",
          "-\\textbf{ContamCal} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} & \\textbf{X.XX} \\\\",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\caption{Main calibration results across four benchmarks. \\textbf{[PLACEHOLDER: exp-006]} MAE: mean absolute error between calibrated and ground-truth clean accuracy (lower is better). Coverage at 50\\%/80\\%/95\\%: fraction of true values within credible interval (closer to nominal is better). HE\\,=\\,HumanEval, ARC-C\\,=\\,ARC-Challenge. Best results in \\textbf{bold}.}",
          "-\\label{tab:main_results}",
          "-\\end{table}",
          "+\\subsubsection{Domain-Differential Contamination Effects}",
          "+\\label{sec:res_domain}",
          " ",
          "-\\paragraph{RRF signal ablation.}",
          "-Table~\\ref{tab:rrf_ablation} reports signal aggregation ablations. \\textbf{[PLACEHOLDER: exp-003]} Full four-signal RRF achieves AUC of \\textbf{[PLACEHOLDER: exp-003]} for contaminated-vs-clean discrimination, compared to \\textbf{[PLACEHOLDER: exp-003]} for the best single signal. Drop-one analysis reveals that removing \\textbf{[PLACEHOLDER: exp-003]} causes the largest AUC decrease, while removing \\textbf{[PLACEHOLDER: exp-003]} has minimal impact, suggesting complementary rather than redundant signal contributions.",
          "+Benchmark-level contamination estimates mask substantial within-benchmark heterogeneity. We fit 2PL+$\\gamma$ models at the MMLU domain level ($N=23$ respondents, 8 domains) and find that contamination effects range from strong inflation to null to negative, depending on domain.",
          " ",
          "+Table~\\ref{tab:domain_gamma} reports domain-level results. STEM\\_Math ($\\hat{\\gamma}=0.969$, PPP$=0.438$, 95\\% CI excludes zero) and STEM\\_Science ($\\hat{\\gamma}=0.838$, PPP$=0.807$, CI excludes zero) show strong positive contamination effects: memorization of injected items inflates measured accuracy. In contrast, STEM\\_CS\\_Eng ($\\hat{\\gamma}=0.197$, CI includes zero), Medical (negative $\\hat{\\gamma}$), Humanities (negative, $\\hat{R}=1.014$), and Social\\_Sciences (negative) show null or deflation effects. Business\\_Law is non-significant.",
          "+",
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\begin{tabular}{l cc}",
          "+\\begin{tabular}{l r r c r l}",
          " \\toprule",
          "-\\textbf{Configuration} & \\textbf{AUC} & \\textbf{$\\Delta$AUC} \\\\",
          "+\\textbf{Domain} & $N_{\\text{items}}$ & $\\hat{\\gamma}$ & \\textbf{95\\% CI} & \\textbf{PPP} & \\textbf{Interpretation} \\\\",
          " \\midrule",
          "-\\multicolumn{3}{l}{\\emph{Single-signal}} \\\\",
          "-Embedding retrieval & [TBD] & --- \\\\",
          "-Min-K\\%++ & [TBD] & --- \\\\",
          "-ConStat & [TBD] & --- \\\\",
          "-Self-Critique & [TBD] & --- \\\\",
          "+STEM\\_Math & 1190 & 0.969 & excl.\\ 0 & 0.438 & inflation \\\\",
          "+STEM\\_Science & 1397 & 0.838 & excl.\\ 0 & 0.807 & inflation \\\\",
          "+STEM\\_CS\\_Eng & 557 & 0.197 & incl.\\ 0 & 0.892 & null \\\\",
          "+Medical & -- & $<0$ & excl.\\ 0 & -- & deflation \\\\",
          "+Humanities & -- & $<0$ & excl.\\ 0 & -- & deflation$^\\dagger$ \\\\",
          "+Social\\_Sciences & -- & $<0$ & excl.\\ 0 & -- & deflation \\\\",
          "+Business\\_Law & -- & -- & incl.\\ 0 & -- & null \\\\",
          " \\midrule",
          "-\\multicolumn{3}{l}{\\emph{Drop-one from full RRF}} \\\\",
          "-$-$ Embedding & [TBD] & [TBD] \\\\",
          "-$-$ Min-K\\%++ & [TBD] & [TBD] \\\\",
          "-$-$ ConStat & [TBD] & [TBD] \\\\",
          "-$-$ Self-Critique & [TBD] & [TBD] \\\\",
          "-\\midrule",
          "-Full RRF (4 signals) & \\textbf{[TBD]} & --- \\\\",
          "+\\multicolumn{6}{l}{\\emph{Cross-benchmark (2PL+$\\gamma$, Qwen-only)}} \\\\",
          "+ARC (N=16) & 1172 & 0.727 & [0.02, 1.44] & 0.003 & inflation$^\\ddagger$ \\\\",
          "+GSM8K (N=24) & 1319 & 0.064 & [$-$0.36, 0.49] & 0.541 & null \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Signal aggregation ablation. \\textbf{[PLACEHOLDER: exp-003]} AUC for contaminated-vs-clean item discrimination, averaged across benchmarks and model scales. $\\Delta$AUC: change relative to full RRF.}",
          "-\\label{tab:rrf_ablation}",
          "+\\caption{Domain-level contamination effects under 2PL+$\\gamma$. $^\\dagger$Marginal convergence ($\\hat{R}=1.014$). $^\\ddagger$Low PPP indicates imperfect model fit; interpret $\\hat{\\gamma}$ with caution.}",
          "+\\label{tab:domain_gamma}",
          " \\end{table}",
          " ",
          "-\\paragraph{RRF $k$-sensitivity.}",
          "-Table~\\ref{tab:k_sensitivity} shows that calibration MAE and detection AUC are stable across $k \\in \\{20, 40, 60, 80, 100\\}$, confirming that ContamCal is not sensitive to the RRF smoothing constant. \\textbf{[PLACEHOLDER: exp-003]}",
          "+\\paragraph{Dilution masking.} When MMLU is analyzed at the pooled benchmark level ($N=16$), the aggregate estimate is $\\hat{\\gamma}=0.655$ with CI$=[-0.41, 1.74]$, which does not exclude zero. The positive STEM effects ($\\hat{\\gamma} \\approx 0.84$--$0.97$) are averaged with negative non-STEM effects, producing an aggregate null. This dilution masking phenomenon explains why prior benchmark-level contamination analyses report inconsistent findings: heterogeneous domain effects cancel when pooled.",
          " ",
          "+\\paragraph{Cross-benchmark patterns.} ARC shows a positive effect ($\\hat{\\gamma}=0.727$, CI$=[0.02, 1.44]$), though the low PPP (0.003) indicates the 2PL+$\\gamma$ model fits ARC data poorly. GSM8K shows no contamination effect ($\\hat{\\gamma}=0.064$), consistent with the hypothesis that free-form mathematical reasoning resists memorization-based inflation.",
          "+",
          "+\\paragraph{Cross-family analysis.} Pooling Qwen and Llama families (D122 v3) collapses all effects: ARC $\\hat{\\gamma}=0.002$ (from 0.73 Qwen-only), MMLU $\\hat{\\gamma}=0.213$, GSM8K $\\hat{\\gamma}=-0.110$, all CIs including zero. This reveals that contamination effects are family-specific. The IRT $\\theta$ estimates remain well-calibrated cross-family (calMAE: 0.015, 0.017, 0.008 for MMLU, ARC, GSM8K), indicating that ability estimation generalizes even when $\\gamma$ does not. These results support per-family contamination modeling rather than universal correction factors.",
          "+",
          "+Figure~\\ref{fig:domain_gamma} visualizes the domain-level heterogeneity. Figure~\\ref{fig:dose_response} shows dose-response curves confirming monotonic inflation in STEM domains.",
          "+",
          "+\\subsubsection{Detection Signal Failure}",
          "+\\label{sec:res_signal}",
          "+",
          "+The four-signal RRF ensemble degrades in practice to a single reliable signal. We evaluate signal discriminability (AUC for contaminated vs.\\ clean items) at the lowest non-trivial dosage (d005, 0.5B scale) where detection is most challenging.",
          "+",
          "+\\paragraph{Signal-level AUC.} Embedding retrieval achieves near-perfect discrimination (AUC: MMLU 0.953, GSM8K 0.988, ARC 0.995). Min-K++ performs \\emph{below chance} across all benchmarks (AUC: MMLU 0.466, GSM8K 0.465, ARC 0.466), indicating a directional reversal where contaminated items receive \\emph{lower} membership scores than clean items. Self-Critique is near chance (AUC: MMLU 0.517, GSM8K 0.495, ARC 0.433).",
          "+",
          "+\\paragraph{Min-K++ reversal.} The below-chance AUC is not random noise but a systematic directional failure. At d100 across model scales, Min-K++ yields Cohen's $d = -1.98$ (strong negative separation), compared to $+3.6$ for embedding retrieval and $+0.45$ for Self-Critique. This reversal occurs because SFT on paraphrased items \\emph{increases} model perplexity on the original surface forms, inverting the membership signal. Exploratory cross-family analysis (Llama-3.2-3B, $N=4$) replicates the reversal direction.",
          "+",
          "+\\paragraph{Practical implication.} In the IRT+MIA framework, RRF aggregation assigns equal fusion weight to all signals. When $K-1$ of $K$ signals carry no information or reversed information, the fused exposure score inherits noise that propagates into $\\gamma$ estimation. The measurement error model (\\S\\ref{sec:stage2}) partially absorbs this noise, but signal failure at the detection stage imposes a fundamental ceiling on contamination quantification.",
          "+",
          "+Figure~\\ref{fig:signal_heatmap} displays the signal-by-benchmark AUC matrix.",
          "+",
          "+\\subsubsection{Identifiability Boundaries}",
          "+\\label{sec:res_identifiability}",
          "+",
          "+We characterize the $(N, \\text{AUC})$ conditions under which $\\gamma$ is recoverable via analytical Fisher information and simulation sweeps.",
          "+",
          "+\\paragraph{Power thresholds.} The Fisher information analysis yields 80\\% power boundaries: AUC$\\geq$0.80 requires $N\\geq$12--16 respondents; AUC$\\geq$0.75 requires $N\\geq$20; AUC$\\geq$0.70 requires $N\\geq$30; AUC$\\geq$0.65 requires $N\\geq$50. CI width scales as $N^{-0.48}$, near the theoretical $\\sqrt{N}$ rate.",
          "+",
          "+\\paragraph{Simulation validation.} We run recovery simulations across the $(N, \\text{AUC})$ grid. At AUC$=$0.55 (near the boundary of informative detection), recovery succeeds with $N\\geq$50 (10/10 seeds). At AUC$=$0.80, recovery succeeds with $N=$20 (10/10 seeds). These results confirm that $\\gamma$ recovery is structurally possible at low signal quality, but requires sample sizes beyond typical LLM evaluation practice.",
          "+",
          "+\\paragraph{Mismatch with LLM evaluation.} Current LLM benchmarking operates at $N=$8--30 models per evaluation. Given that practical detection AUC concentrates at 0.45--0.55 for all signals except embedding retrieval (\\S\\ref{sec:res_signal}), most $(N, \\text{AUC})$ operating points fall below the identifiability boundary. This is a domain-method mismatch specific to the IRT+MIA framework in LLM evaluation, not a general impossibility result.",
          "+",
          "+Figure~\\ref{fig:identifiability_heatmap} displays the Fisher power surface with current operating points marked.",
          "+",
          "+\\subsubsection{Calibration Value Decomposition}",
          "+\\label{sec:res_calibration}",
          "+",
          "+We isolate the source of calibration improvement by comparing vanilla 2PL (no contamination covariate) against 2PL+$\\gamma$ under matched conditions ($N=16$, Qwen-only).",
          "+",
          "+\\paragraph{$\\gamma$ provides no calibration benefit.} Table~\\ref{tab:baselines} reports calibration MAE. The vanilla 2PL and 2PL+$\\gamma$ models achieve near-identical performance: GSM8K calMAE 0.0063 vs.\\ 0.0062, MMLU 0.0068 vs.\\ 0.0070, ARC 0.0158 vs.\\ 0.0201 (vanilla slightly better). Adding $\\gamma$ does not reduce calibration error because the IRT ability parameter $\\theta$ already absorbs contamination-induced performance variation through its latent trait estimation.",
          "+",
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\begin{tabular}{l ccccc}",
          "+\\begin{tabular}{l ccc}",
          " \\toprule",
          "-$k$ & 20 & 40 & \\textbf{60} & 80 & 100 \\\\",
          "+\\textbf{Method} & \\textbf{MMLU} & \\textbf{GSM8K} & \\textbf{ARC} \\\\",
          " \\midrule",
          "-MAE & [TBD] & [TBD] & \\textbf{[TBD]} & [TBD] & [TBD] \\\\",
          "-AUC & [TBD] & [TBD] & \\textbf{[TBD]} & [TBD] & [TBD] \\\\",
          "+\\multicolumn{4}{l}{\\emph{calMAE $\\downarrow$}} \\\\",
          "+Raw scores & 0.016 & 0.163 & 0.034 \\\\",
          "+Vanilla 2PL ($\\gamma=0$) & 0.0068 & 0.0063 & 0.0158 \\\\",
          "+2PL+$\\gamma$ & 0.0070 & 0.0062 & 0.0201 \\\\",
          "+\\midrule",
          "+\\multicolumn{4}{l}{\\emph{$\\Delta$MAE (raw $-$ calibrated)}} \\\\",
          "+2PL+$\\gamma$ & 0.010 & 0.155 & 0.018 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Sensitivity to RRF smoothing constant~$k$. \\textbf{[PLACEHOLDER: exp-003]} Default $k\\!=\\!60$ in bold.}",
          "-\\label{tab:k_sensitivity}",
          "+\\caption{Calibration comparison ($N=16$, Qwen-only, all scales pooled). Adding $\\gamma$ provides no improvement over vanilla 2PL; both reduce raw error substantially through $\\theta$ estimation.}",
          "+\\label{tab:baselines}",
          " \\end{table}",
          " ",
          "-\\paragraph{Dose-response curves.}",
          "-Figure~\\ref{fig:dose_response} plots raw accuracy, calibrated accuracy, and ground-truth clean accuracy as a function of contamination dosage for each benchmark and model scale. \\textbf{[PLACEHOLDER: exp-006]} Raw scores inflate monotonically with dosage, while calibrated scores remain approximately flat, tracking the ground-truth clean performance. The posterior mean $\\hat{\\gamma}_k$ increases monotonically with dosage across all benchmarks (Spearman $\\rho =$ \\textbf{[PLACEHOLDER: exp-006]}, $p <$ \\textbf{[PLACEHOLDER: exp-006]}).",
          "+\\paragraph{Calibration from $\\theta$ estimation.} The large $\\Delta$MAE reductions (0.155 for GSM8K, 0.018 for ARC, 0.010 for MMLU) derive entirely from IRT ability estimation. By mapping raw accuracies onto a latent ability scale and back-transforming through item parameters, the IRT framework corrects for item difficulty variation that inflates or deflates benchmark-level scores. This correction operates independently of contamination detection.",
          " ",
          "-\\begin{figure}[t]",
          "-    \\centering",
          "-    % \\includegraphics[width=\\columnwidth]{figures/dose_response.pdf}",
          "-    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-006]}\\\\ Dose-response curves: raw vs.\\ calibrated vs.\\ ground-truth accuracy across 5 dosage levels, faceted by benchmark and model scale. Shaded bands = 95\\% credible intervals.\\vspace{2em}}}",
          "-    \\caption{Dose-response curves across four benchmarks and three model scales (0.5B, 1.5B, 3B). \\textbf{[PLACEHOLDER: exp-006]}}",
          "-    \\label{fig:dose_response}",
          "-\\end{figure}",
          "+\\paragraph{$\\gamma$ as diagnostic, not corrective.} The value of $\\gamma$ is diagnostic rather than corrective. Domain-level $\\gamma$ estimation (\\S\\ref{sec:res_domain}) reveals which knowledge areas are susceptible to memorization-based inflation, enabling targeted benchmark maintenance decisions. But for the practical goal of score calibration, $\\theta$ alone suffices.",
          " ",
          "-\\paragraph{Uncertainty calibration and noise propagation.}",
          "-Figure~\\ref{fig:ci_width} shows credible interval width as a function of measurement error variance~$\\sigma_e^2$ (Eq.~\\eqref{eq:measurement_error}). \\textbf{[PLACEHOLDER: exp-005]} As detection signal noise increases, ContamCal produces appropriately wider intervals while maintaining nominal coverage. This confirms that the measurement error model successfully propagates detection uncertainty into the calibrated scores.",
          "+\\paragraph{Cross-family calibration.} The $\\theta$-based calibration transfers across model families without retraining: pooled Qwen+Llama calMAE is 0.017 (MMLU), 0.015 (ARC), 0.008 (GSM8K), with $\\Delta$MAE of 0.028, 0.055, and 0.171 respectively. This cross-family validity confirms that IRT ability estimation captures a stable latent construct independent of architecture-specific contamination patterns.",
          " ",
          "-\\begin{figure}[t]",
          "-    \\centering",
          "-    % \\includegraphics[width=\\columnwidth]{figures/ci_width_noise.pdf}",
          "-    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-005]}\\\\ CI width and coverage vs.\\ measurement error variance $\\sigma_e^2$. Coverage should remain near nominal as width increases.\\vspace{2em}}}",
          "-    \\caption{Credible interval width (left axis) and coverage (right axis) as a function of measurement error variance. \\textbf{[PLACEHOLDER: exp-005]}}",
          "-    \\label{fig:ci_width}",
          "-\\end{figure}",
          "-",
          "-\\paragraph{Signal survival under RL.}",
          "-Figure~\\ref{fig:signal_survival} presents detection signal AUCs across training regimes (SFT vs.\\ RL with GRPO). \\textbf{[PLACEHOLDER: exp-008]} Probability-based signals (Min-K\\%++, ConStat) degrade from AUC \\textbf{[PLACEHOLDER: exp-008]} under SFT to \\textbf{[PLACEHOLDER: exp-008]} under RL---a cliff-like drop rather than gradual attenuation, consistent with the hypothesis in \\S\\ref{sec:signal_survival}. Self-Critique retains higher AUC of \\textbf{[PLACEHOLDER: exp-008]} post-RL, validating its inclusion as a robustness anchor in the signal ensemble. This regime-dependent degradation is automatically captured by the measurement error model: RL-trained models receive wider credible intervals reflecting genuine epistemic uncertainty about their contamination status.",
          "-",
          "-\\begin{figure}[t]",
          "-    \\centering",
          "-    % \\includegraphics[width=\\columnwidth]{figures/signal_survival.pdf}",
          "-    \\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textbf{[PLACEHOLDER: exp-008, if available]}\\\\ Signal AUC by training regime (SFT vs.\\ RL). Grouped bar chart showing cliff-like degradation for probability-based signals vs.\\ retention for Self-Critique.\\vspace{2em}}}",
          "-    \\caption{Detection signal AUC across training regimes. \\textbf{[PLACEHOLDER: exp-008]}}",
          "-    \\label{fig:signal_survival}",
          "-\\end{figure}",
          "+Figure~\\ref{fig:calibration} shows calibrated vs.\\ true accuracy scatter plots across benchmarks."
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

Done. The Results section (§5) has been rewritten with four subsections:

1. **§5.1 Domain-Differential Contamination Effects** -- reports domain-level γ heterogeneity, dilution masking, cross-benchmark patterns, and cross-family analysis with Table 1.
2. **§5.2 Detection Signal Failure** -- documents Min-K++ directional reversal (AUC < 0.5), embedding-only reliability, and practical implications for RRF.
3. **§5.3 Identifiability Boundaries** -- presents Fisher power thresholds, simulation validation, and the N/AUC mismatch with LLM evaluation practice.
4. **§5.4 Calibration Value Decomposition** -- shows γ provides no calibration benefit over vanilla 2PL, establishes θ as the source of calibration, frames γ as diagnostic, with Table 2 and cross-family validation.

All quantitative claims are backed by the provided data. No em-dashes, no -ing phrase endings, no AI-style filler.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "uuid": "82ddfbca-5771-4bea-bf73-c165860edac2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EY5ePVm9UkGUc7UyGUo74M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6978,
      "cache_read_input_tokens": 35366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6978
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

_source line 14_

Done. The Results section (§5) has been rewritten with four subsections:

1. **§5.1 Domain-Differential Contamination Effects** -- reports domain-level γ heterogeneity, dilution masking, cross-benchmark patterns, and cross-family analysis with Table 1.
2. **§5.2 Detection Signal Failure** -- documents Min-K++ directional reversal (AUC < 0.5), embedding-only reliability, and practical implications for RRF.
3. **§5.3 Identifiability Boundaries** -- presents Fisher power thresholds, simulation validation, and the N/AUC mismatch with LLM evaluation practice.
4. **§5.4 Calibration Value Decomposition** -- shows γ provides no calibration benefit over vanilla 2PL, establishes θ as the source of calibration, frames γ as diagnostic, with Table 2 and cross-family validation.

All quantitative claims are backed by the provided data. No em-dashes, no -ing phrase endings, no AI-style filler.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 128741,
  "duration_api_ms": 129739,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "889dbd0a-2110-4bd7-b48c-46a42a842722",
  "total_cost_usd": 0.43483775,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 30503,
    "cache_read_input_tokens": 107824,
    "output_tokens": 7422,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30503,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 254,
        "cache_read_input_tokens": 35366,
        "cache_creation_input_tokens": 6978,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6978
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 4617,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.004702,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 7422,
      "cacheReadInputTokens": 107824,
      "cacheCreationInputTokens": 30503,
      "webSearchRequests": 0,
      "costUSD": 0.43013575,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8f6d70ad-d402-4a7d-a133-52c7b9e9785e"
}
```

</details>

---
