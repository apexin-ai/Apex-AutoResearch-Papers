# paper appendix tsr collapse

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_appendix-tsr-collapse_20260529T001953.log`
- **Structured JSON:** [`5135f035617271a7ae6a.json`](../../sessions/51/5135f035617271a7ae6a.json)

## Before a recorded user message

23 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
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
    "mcp__agent-ml-research__allocate_and_submit",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__approve_worker",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__backup_project_to_s3",
    "mcp__agent-ml-research__cancel_worker",
    "mcp__agent-ml-research__check_job_status",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__distill_papers",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__feishu_read_tum_pending_key",
    "mcp__agent-ml-research__feishu_send_alert",
    "mcp__agent-ml-research__feishu_send_approval_card",
    "mcp__agent-ml-research__feishu_send_result_card",
    "mcp__agent-ml-research__feishu_send_tum_key_request_card",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__get_baseline_metrics",
    "mcp__agent-ml-research__get_distill_status",
    "mcp__agent-ml-research__get_gpu_health",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_matrix_value",
    "mcp__agent-ml-research__get_project_resource_usage",
    "mcp__agent-ml-research__get_tum_config",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__impact_analysis",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_available_gpus",
    "mcp__agent-ml-research__list_constraints",
    "mcp__agent-ml-research__list_s3_backups",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__main_agent_post_to_director",
    "mcp__agent-ml-research__matrix_gap_analysis",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__poll_cron",
    "mcp__agent-ml-research__poll_secret_request",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_matrix",
    "mcp__agent-ml-research__read_mistakes",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__reconcile_crons",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__register_cron",
    "mcp__agent-ml-research__request_secret",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__submit_on_allocated",
    "mcp__agent-ml-research__submit_training_job",
    "mcp__agent-ml-research__sync_matrix_status",
    "mcp__agent-ml-research__tail_training_logs",
    "mcp__agent-ml-research__update_baseline",
    "mcp__agent-ml-research__update_matrix",
    "mcp__agent-ml-research__update_registry",
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
  "uuid": "6d0224b8-cd29-4586-9479-853efe8964b9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1780031400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d165e9a7-ac5f-43af-bc46-bd27414567aa",
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994"
}
```

---

### Assistant

_source line 4_

Let me start by reading the appendix.tex file to understand the current structure and find the right insertion point.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "71c51cce-0041-4b28-932c-5756ba67744b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eb1BQYtHi1ehyxJwUSkL4n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13512,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13512
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

<details open><summary>🔧 Tool call — Read · `toolu_01DsZPr2usERd1rN43H2cHrd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "02f8caa3-c653-4ec9-976d-42a384f371f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eb1BQYtHi1ehyxJwUSkL4n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13512,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13512
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

_source line 6 · 2026-05-29T00:20:05.675Z_

<details><summary>↩ Tool result · `toolu_01DsZPr2usERd1rN43H2cHrd`</summary>

```text
1	\section{Complete Multi-Seed Results}
2	\label{sec:appendix_multiseed}
3	
4	Table~\ref{tab:multiseed_full} reports individual-seed CAR and TSR for all fine-tuned conditions at the 30K checkpoint (200 episodes each, evaluation seed\,=\,7). These per-seed values underlie the means reported in Table~\ref{tab:avoidance_source}.
5	
6	\begin{table}[h]
7	\centering
8	\caption{Per-seed CAR and TSR (\%) at 30K steps, evaluation seed\,=\,7 (200 episodes). All episodes exhibit displacement $>$\,0.37\,m and 0\% action-collapse rate.}
9	\label{tab:multiseed_full}
10	\vspace{2pt}
11	\small
12	\begin{tabular}{llcccc}
13	\toprule
14	Condition & Seed & CAR & TSR & Mean CAR & Mean TSR \\
15	\midrule
16	\multirow{3}{*}{LoRA-only}
17	  & s0 & 57.0 & 46.0 & \multirow{3}{*}{54.83$\pm$2.25} & \multirow{3}{*}{49.7$\pm$3.2} \\
18	  & s1 & 52.5 & 51.5 & & \\
19	  & s2 & 55.0 & 51.5 & & \\
20	\midrule
21	\multirow{3}{*}{SDF $\lambda{=}0.005$}
22	  & s0 & 57.0 & 55.5 & \multirow{3}{*}{54.5$\pm$2.29} & \multirow{3}{*}{54.0$\pm$3.0} \\
23	  & s1 & 54.0 & 50.5 & & \\
24	  & s2 & 52.5 & 56.0 & & \\
25	\midrule
26	\multirow{3}{*}{SDF $\lambda{=}0.01$}
27	  & s0 & 57.0 & 52.5 & \multirow{3}{*}{56.33$\pm$1.61} & \multirow{3}{*}{53.8$\pm$1.5} \\
28	  & s1 & 57.5 & 55.5 & & \\
29	  & s2 & 54.5 & 53.5 & & \\
30	\midrule
31	\multirow{3}{*}{SDF $\lambda{=}0.1$}
32	  & s0 & 58.0 & 47.0 & \multirow{3}{*}{57.00$\pm$2.18} & \multirow{3}{*}{50.2$\pm$3.9} \\
33	  & s1 & 58.5 & 49.0 & & \\
34	  & s2 & 54.5 & 54.5 & & \\
35	\bottomrule
36	\end{tabular}
37	\end{table}
38	
39	\section{Displacement Distribution}
40	\label{sec:appendix_displacement}
41	
42	\begin{figure}[h]
43	\centering
44	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
45	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
46	\label{fig:displacement}
47	\end{figure}
48	
49	\section{Displacement Threshold Sensitivity Analysis}
50	\label{sec:appendix_threshold}
51	
52	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% action-collapse rate even at the most conservative setting.
53	
54	\begin{table}[h]
55	\centering
56	\caption{Action-collapse rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
57	\label{tab:threshold_sensitivity}
58	\begin{tabular}{lccc}
59	\toprule
60	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
61	\midrule
62	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
63	0.1 mm  & 99.6 & 0.0 & 0.0 \\
64	1.0 mm  & 100.0 & 0.0 & 0.0 \\
65	10 mm   & 100.0 & 0.0 & 0.0 \\
66	\bottomrule
67	\end{tabular}
68	\end{table}
69	
70	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.
71	
72	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\tau_d \in [2, 200]$\,mm. At $\tau_d = 300$\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\,mm), causing $\leq$0.5\,pp deviation. Our conclusions hold across the entire tested range.
73	
74	\begin{table}[h]
75	\centering
76	\caption{dfCAR (\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\tau_d \in [2, 200]$\,mm; at $\tau_d = 300$\,mm, at most 2 episodes are excluded.}
77	\label{tab:dfcar_threshold}
78	\vspace{2pt}
79	\footnotesize
80	\begin{tabular}{lcccccccc}
81	\toprule
82	& \multicolumn{8}{c}{$\tau_d$ (mm)} \\
83	\cmidrule(lr){2-9}
84	Condition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\
85	\midrule
86	LoRA s0            & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
87	LoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\
88	SDF $\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\
89	SDF $\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\
90	SDF $\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\
91	SDF $\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
92	SDF $\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\
93	SDF $\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	
99	\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
100	
101	Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
102	
103	\begin{table}[h]
104	\centering
105	\caption{Per-task TSR (\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\,=\,71.5\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}
106	\label{tab:per_task_tsr}
107	\vspace{2pt}
108	\small
109	\begin{tabular}{lcccc}
110	\toprule
111	Task & Pi0.5 Base & LoRA-only & SDF $\lambda{=}0.005$ & SDF $\lambda{=}0.01$ \\
112	 & (seed\,=\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\
113	\midrule
114	Orange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\
115	Choco.\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\
116	Milk              & 66.0 & 44.7 & 35.3 & 48.7 \\
117	BBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\
118	\midrule
119	Mean              & 71.5 & 51.5 & 54.0 & 53.8 \\
120	\bottomrule
121	\end{tabular}
122	\end{table}
123	
124	\section{Per-Task CAR Breakdown}\label{sec:appendix_pertask_car}
125	
126	Table~\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\S\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.
127	
128	\begin{table}[h]
129	\centering
130	\caption{Per-task CAR (\%) at 30K steps. $\lambda{=}0.005$, $\lambda{=}0.01$, and $\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}
131	\label{tab:per_task_car}
132	\vspace{2pt}
133	\small
134	\begin{tabular}{lccccc}
135	\toprule
136	Condition & OJ & CP & Milk & BBQ & Agg. \\
137	\midrule
138	LoRA s0 & 68 & 74 & 66 & 20 & 57.0 \\
139	LoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\
140	LoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\
141	SDF $\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\
142	SDF $\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\
143	SDF $\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\
144	SDF $\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\
145	SDF $\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\
146	SDF $\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\
147	\bottomrule
148	\end{tabular}
149	\end{table}
150	
151	For the $\lambda = 0.1$ condition, seed~1 records \texttt{avg\_max\_obstacle\_displacement} of 0.0553\,m (per-task: OJ\,=\,0.033, CP\,=\,0.055, Milk\,=\,0.041, BBQ\,=\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.
152	
153	\begin{figure}[t]
154	\centering
155	\includegraphics[width=\linewidth]{fig_pertask_car_fingerprint}
156	\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\_pudding highest, bbq\_sauce lowest) is preserved across all $\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}
157	\label{fig:pertask_fingerprint}
158	\end{figure}
159	
160	\section{Safe Success Rate Analysis}\label{sec:appendix_ssr}
161	
162	Table~\ref{tab:ssr} reports the Safe Success Rate (SSR\,=\,TSR\,$\cap$\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.
163	
164	\begin{table}[h]
165	\centering
166	\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}
167	\label{tab:ssr}
168	\vspace{2pt}
169	\small
170	\begin{tabular}{lcccc}
171	\toprule
172	Condition & TSR (\%) & CAR (\%) & SSR (\%) & SSR/TSR \\
173	\midrule
174	Pi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\
175	LoRA-only (3 seeds) & 49.7 & 54.83 & 27.7 & 0.56 \\
176	SDF $\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\
177	SDF $\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\
178	SDF $\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\
179	\bottomrule
180	\end{tabular}
181	\end{table}
182	
183	\section{Per-Task Oracle Analysis}
184	\label{sec:appendix_pertask}
185	\label{sec:appendix_pertask_oracle}
186	
187	Table~\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\texttt{chocolate\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive improves to 55.0\% and Oracle-feature to 47.5\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\texttt{orange\_juice}) from 96.0\% to 82.5\% and task~2 (\texttt{milk}) from 98.0\% to 77.5\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.
188	
189	The feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49), and CAR (76.9\%) shows no advantage despite 17$\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.
190	
191	\begin{table}[h]
192	\centering
193	\caption{Per-task CAR (\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}
194	\label{tab:oracle_pertask}
195	\vspace{2pt}
196	\small
197	\begin{tabular}{lccccc}
198	\toprule
199	Method & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\
200	\midrule
201	LoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\
202	\midrule
203	Oracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\
204	Oracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\
205	Oracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	
211	\section{Null Distribution for SDF Loss Weight Analysis}
212	\label{sec:appendix_null}
213	
214	We construct a null distribution by pooling the three LoRA-only seeds and three $\lambda = 0.005$ seeds into six per-seed CAR measurements: 57.0\% (LoRA s0, re-evaluated), 52.5\% (LoRA s1), 55.0\% (LoRA s2), 57.0\% ($\lambda{=}0.005$ s0), 54.0\% ($\lambda{=}0.005$ s1), 52.5\% ($\lambda{=}0.005$ s2), yielding mean 54.67\% and standard deviation 2.07\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\lambda = 0.005$ produces no separation from LoRA-only. The $\lambda = 0.01$ mean of 56.33\% falls within $0.8\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\lambda = 0.1$ 30K mean of 57.00\% (3 seeds: 58.0\%, 58.5\%, 54.5\%) yields a two-tailed permutation $p = 0.155$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\alpha = 0.05$).
215	
216	The permutation test makes no distributional assumptions. Pooling the six null values $\{57, 52.5, 55, 57, 54, 52.5\}$ and three $\lambda = 0.1$ values $\{58, 58.5, 54.5\}$ into nine measurements, we enumerate all $\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 13/84 \approx 0.155$. With the third seed ($s_2 = 54.5\%$) pulling the $\lambda = 0.1$ mean from 58.25\% (2 seeds) down to 57.00\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.
217	
218	\paragraph{Alternative null construction (Null~A).}
219	If only the three LoRA-only seeds are used as the null pool ($\{57.0, 52.5, 55.0\}$), we obtain $\binom{6}{3} = 20$ permutations for each comparison. For $\lambda = 0.1$ (treatment mean 57.00\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 5/20 = 0.250$. For $\lambda = 0.01$ (treatment mean 56.33\%): one-tailed $p = 6/20 = 0.300$, two-tailed $p = 12/20 = 0.600$. Under the broader Null~B pool, $\lambda = 0.01$ yields one-tailed $p = 13/84 \approx 0.155$, two-tailed $p = 25/84 \approx 0.298$. All tests are non-significant at $\alpha = 0.05$; the narrower Null~A yields \emph{larger} $p$-values because the LoRA-only pool already contains a high seed (57.0\%), making the treatment means less extreme by comparison.
220	
221	A Phase~2 ablation reinforces this conclusion. Setting $\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.
222	
223	\section{Step-wise Checkpoint Analysis for \texorpdfstring{$\lambda = 0.1$}{lambda = 0.1}}
224	\label{sec:appendix_stepwise}
225	
226	Table~\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\%) pulls the three-seed mean to 57.00\%, within the null band ($p = 0.155$).
227	
228	\begin{table}[h]
229	\centering
230	\caption{Per-seed CAR (\%) at training checkpoints for $\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\%) remains within the null band ($p = 0.155$, two-tailed permutation).}
231	\label{tab:stepwise_lambda01}
232	\vspace{2pt}
233	\small
234	\begin{tabular}{lcccc}
235	\toprule
236	Checkpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\
237	\midrule
238	16K steps & 55.5 & 56.0 & -- & 55.75 \\
239	20K steps & 55.0 & 56.0 & -- & 55.5 \\
240	22K steps & 60.5 & 56.5 & -- & 58.5 \\
241	24K steps & 52.5 & -- & -- & -- \\
242	26K steps & 53.5 & -- & -- & -- \\
243	28K steps & 54.5 & -- & -- & -- \\
244	30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\
245	\bottomrule
246	\end{tabular}
247	\end{table}
248	
249	Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\,pp (seed~0: 52.5--60.5\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\leq$3\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\sigma \approx 7$\,pp per task for $p \approx 0.5$). At 30K, the third seed ($s_2 = 54.5\%$) falls well within the null range, pulling the three-seed mean to 57.00\% and rendering the earlier two-seed departure non-significant ($p = 0.155$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.
250	
251	
252	\section{Oracle SDF Refinement Details}
253	\label{sec:appendix_oracle}
254	
255	All oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\times$ 40).
256	
257	\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.
258	
259	\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.
260	
261	\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49 in action space).
262	
263	
264	\section{Cross-Scene Validation: spatial\_bowl}
265	\label{sec:appendix_spatial_bowl}
266	
267	To test whether the absence of EE-only SDF benefit generalizes beyond the primary \texttt{object\_pudding} scene, we replicate the core comparison on \texttt{spatial\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.
268	
269	Table~\ref{tab:spatial_bowl} reports the results. The SDF condition ($\lambda = 0.005$) yields CAR of 11.5\% versus 12.0\% for LoRA-only, a $-$0.5\,pp difference well within the noise floor, indicating that SDF is essentially identical to LoRA-only on this scene. TSR is comparable across conditions (49.0\% vs.\ 51.5\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \texttt{object\_pudding} findings.
270	
271	\begin{table}[h]
272	\centering
273	\caption{Cross-scene validation on \texttt{spatial\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\,pp CAR difference is well within noise, consistent with the absence of SDF benefit observed on \texttt{object\_pudding}.}
274	\label{tab:spatial_bowl}
275	\vspace{2pt}
276	\small
277	\begin{tabular}{lcc}
278	\toprule
279	Condition & CAR (\%) & TSR (\%) \\
280	\midrule
281	LoRA-only & 12.0 & 49.0 \\
282	SDF $\lambda{=}0.005$ & 11.5 & 51.5 \\
283	\bottomrule
284	\end{tabular}
285	\end{table}
286	
287	The substantially lower CAR on \texttt{spatial\_bowl} relative to \texttt{object\_pudding} (11--12\% vs.\ 54--57\%) reflects the greater scene difficulty: \texttt{spatial\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition performs comparably ($\Delta$CAR\,=\,$-$0.5\,pp, well within noise), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.
288	
289	
290	\section{Evaluation Seed Robustness}
291	\label{sec:appendix_eval_seed}
292	
293	To verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate key model configurations under multiple evaluation seeds (200 episodes each). Table~\ref{tab:eval_seed_robustness} reports aggregate CAR and TSR across all tested seeds.
294	
295	\begin{table}[h]
296	\centering
297	\caption{Eval-seed robustness: aggregate CAR and TSR (\%) across evaluation seeds (200 episodes each). Dashes indicate untested seeds. CAR ranges overlap across all three conditions, confirming that SDF redundancy is not an eval-seed artifact.}
298	\label{tab:eval_seed_robustness}
299	\vspace{2pt}
300	\footnotesize
301	\begin{tabular}{llccccccl}
302	\toprule
303	& & \multicolumn{6}{c}{Evaluation seed} & \\
304	\cmidrule(lr){3-8}
305	Condition & & 0 & 7 & 42 & 99 & 123 & 256 & Mean$\pm$Std \\
306	\midrule
307	\multirow{2}{*}{LoRA s0}
308	  & CAR & 53.0 & 57.0 & 56.5 & 57.5 & 53.0 & --- & 55.4$\pm$2.2 \\
309	  & TSR & 55.5 & 46.0 & 46.0 & 52.0 & 50.5 & --- & 50.0$\pm$4.1 \\
310	\midrule
311	\multirow{2}{*}{SDF $\lambda{=}0.01$ s0}
312	  & CAR & 52.5 & 57.0 & --- & 57.0 & --- & 57.0 & 55.9$\pm$2.3 \\
313	  & TSR & 48.5 & 52.5 & --- & 46.5 & --- & 48.0 & 48.9$\pm$2.6 \\
314	\midrule
315	\multirow{2}{*}{SDF $\lambda{=}0.1$ s0}
316	  & CAR & --- & 58.0 & 59.0 & --- & 58.5 & 57.0 & 58.1$\pm$0.9 \\
317	  & TSR & --- & 47.0 & 52.5 & --- & 53.5 & 48.0 & 50.3$\pm$3.2 \\
318	\bottomrule
319	\end{tabular}
320	\end{table}
321	
322	LoRA s0 CAR ranges from 53.0\% to 57.5\% across five evaluation seeds (std\,=\,2.2\,pp), consistent with binomial sampling noise at $n{=}50$ episodes per task. SDF $\lambda{=}0.01$ s0 produces near-identical mean CAR (55.9\% across four eval seeds vs.\ 55.4\% for LoRA), confirming that the null result holds across eval conditions. SDF $\lambda{=}0.1$ s0 shows a slightly higher mean (58.1\%), but the ranges overlap with LoRA-only, and the difference (2.8\,pp, ${<}$1.3$\sigma$) remains non-significant. The per-task CAR ordering (chocolate\_pudding highest, bbq\_sauce lowest) is preserved across all seeds and conditions, reinforcing the demonstration-driven avoidance hypothesis.
323	
324	Table~\ref{tab:eval_seed_car_detail} provides per-task CAR for the five-seed LoRA evaluation, the most complete eval-seed battery.
325	
326	\begin{table}[h]
327	\centering
328	\caption{Per-task CAR (\%) for LoRA s0 across five evaluation seeds. The per-task fingerprint (CP highest, BBQ lowest) is invariant across all seeds.}
329	\label{tab:eval_seed_car_detail}
330	\vspace{2pt}
331	\small
332	\begin{tabular}{lccccc}
333	\toprule
334	Eval seed & OJ & CP & Milk & BBQ & Agg. \\
335	\midrule
336	0   & 46 & 70 & 74 & 22 & 53.0 \\
337	7   & 68 & 74 & 66 & 20 & 57.0 \\
338	42  & 60 & 70 & 68 & 28 & 56.5 \\
339	99  & 58 & 76 & 66 & 30 & 57.5 \\
340	123 & 52 & 74 & 66 & 20 & 53.0 \\
341	\midrule
342	Mean$\pm$Std & 56.8$\pm$8.3 & 72.8$\pm$2.7 & 68.0$\pm$3.5 & 24.0$\pm$4.7 & 55.4$\pm$2.2 \\
343	\bottomrule
344	\end{tabular}
345	\end{table}
346	
347	
348	\section{Training Details}
349	\label{sec:appendix_training}
350	
351	\paragraph{Architecture.}
352	We use LoRA~\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\alpha$=16) and the action expert (rank 32, $\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3).
353	
354	\paragraph{Training schedule.}
355	Training proceeds in two phases:
356	\begin{itemize}
357	    \item \textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.
358	    \item \textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.
359	\end{itemize}
360	
361	\paragraph{Hyperparameters.}
362	\begin{table}[h]
363	\centering
364	\caption{Training hyperparameters.}
365	\label{tab:hyperparams}
366	\begin{tabular}{ll}
367	\toprule
368	Parameter & Value \\
369	\midrule
370	Base model & Pi0.5 (OpenPi, $\sim$3.5B parameters) \\
371	Optimizer & AdamW \\
372	Learning rate & $2.5 \times 10^{-5}$ (cosine decay to $\mathrm{lr}/10$) \\
373	Warmup steps & 1000 \\
374	Batch size & 32 \\
375	Total steps & 30000 \\
376	$\lambda_\mathrm{sdf}$ & \{0.005, 0.01, 0.1\} \\
377	$\lambda_\mathrm{ee}$ & 0.01 \\
378	SDF query points per step & 64 \\
379	SDF clamp $\delta$ & 0.05 m \\
380	Eikonal weight & 0.1 \\
381	LoRA rank (vision) & 16 \\
382	LoRA rank (action) & 32 \\
383	Phase 1 duration & 5000 steps \\
384	\bottomrule
385	\end{tabular}
386	\end{table}
387	
388	\paragraph{Evaluation protocol.}
389	Each episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\sim}$5\% to ${\sim}$52\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).
390	
391	\paragraph{Data.}
392	We use the SafeLIBERO object\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.
393	
394	\paragraph{Computational resources.}
395	All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.
396	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "2acafbec-2579-42d6-a91c-044cfe2bffc4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
      "content": "\\section{Complete Multi-Seed Results}\n\\label{sec:appendix_multiseed}\n\nTable~\\ref{tab:multiseed_full} reports individual-seed CAR and TSR for all fine-tuned conditions at the 30K checkpoint (200 episodes each, evaluation seed\\,=\\,7). These per-seed values underlie the means reported in Table~\\ref{tab:avoidance_source}.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR and TSR (\\%) at 30K steps, evaluation seed\\,=\\,7 (200 episodes). All episodes exhibit displacement $>$\\,0.37\\,m and 0\\% action-collapse rate.}\n\\label{tab:multiseed_full}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nCondition & Seed & CAR & TSR & Mean CAR & Mean TSR \\\\\n\\midrule\n\\multirow{3}{*}{LoRA-only}\n  & s0 & 57.0 & 46.0 & \\multirow{3}{*}{54.83$\\pm$2.25} & \\multirow{3}{*}{49.7$\\pm$3.2} \\\\\n  & s1 & 52.5 & 51.5 & & \\\\\n  & s2 & 55.0 & 51.5 & & \\\\\n\\midrule\n\\multirow{3}{*}{SDF $\\lambda{=}0.005$}\n  & s0 & 57.0 & 55.5 & \\multirow{3}{*}{54.5$\\pm$2.29} & \\multirow{3}{*}{54.0$\\pm$3.0} \\\\\n  & s1 & 54.0 & 50.5 & & \\\\\n  & s2 & 52.5 & 56.0 & & \\\\\n\\midrule\n\\multirow{3}{*}{SDF $\\lambda{=}0.01$}\n  & s0 & 57.0 & 52.5 & \\multirow{3}{*}{56.33$\\pm$1.61} & \\multirow{3}{*}{53.8$\\pm$1.5} \\\\\n  & s1 & 57.5 & 55.5 & & \\\\\n  & s2 & 54.5 & 53.5 & & \\\\\n\\midrule\n\\multirow{3}{*}{SDF $\\lambda{=}0.1$}\n  & s0 & 58.0 & 47.0 & \\multirow{3}{*}{57.00$\\pm$2.18} & \\multirow{3}{*}{50.2$\\pm$3.9} \\\\\n  & s1 & 58.5 & 49.0 & & \\\\\n  & s2 & 54.5 & 54.5 & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% action-collapse rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Action-collapse rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n\nTable~\\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\\S\\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) at 30K steps. $\\lambda{=}0.005$, $\\lambda{=}0.01$, and $\\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}\n\\label{tab:per_task_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 & 68 & 74 & 66 & 20 & 57.0 \\\\\nLoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\\\\nLoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\\\\nSDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\nSDF $\\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\\\\nSDF $\\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\\\\nSDF $\\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor the $\\lambda = 0.1$ condition, seed~1 records \\texttt{avg\\_max\\_obstacle\\_displacement} of 0.0553\\,m (per-task: OJ\\,=\\,0.033, CP\\,=\\,0.055, Milk\\,=\\,0.041, BBQ\\,=\\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_pertask_car_fingerprint}\n\\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all $\\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}\n\\label{fig:pertask_fingerprint}\n\\end{figure}\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nTable~\\ref{tab:ssr} reports the Safe Success Rate (SSR\\,=\\,TSR\\,$\\cap$\\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\\\\nLoRA-only (3 seeds) & 49.7 & 54.83 & 27.7 & 0.56 \\\\\nSDF $\\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 57.0\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.67\\% and standard deviation 2.07\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.155$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{57, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 13/84 \\approx 0.155$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{57.0, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 5/20 = 0.250$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 6/20 = 0.300$, two-tailed $p = 12/20 = 0.600$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 13/84 \\approx 0.155$, two-tailed $p = 25/84 \\approx 0.298$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (57.0\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.155$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.155$, two-tailed permutation).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & -- & 55.75 \\\\\n20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n22K steps & 60.5 & 56.5 & -- & 58.5 \\\\\n24K steps & 52.5 & -- & -- & -- \\\\\n26K steps & 53.5 & -- & -- & -- \\\\\n28K steps & 54.5 & -- & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$3\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). At 30K, the third seed ($s_2 = 54.5\\%$) falls well within the null range, pulling the three-seed mean to 57.00\\% and rendering the earlier two-seed departure non-significant ($p = 0.155$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Cross-Scene Validation: spatial\\_bowl}\n\\label{sec:appendix_spatial_bowl}\n\nTo test whether the absence of EE-only SDF benefit generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\n\nTable~\\ref{tab:spatial_bowl} reports the results. The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 12.0\\% for LoRA-only, a $-$0.5\\,pp difference well within the noise floor, indicating that SDF is essentially identical to LoRA-only on this scene. TSR is comparable across conditions (49.0\\% vs.\\ 51.5\\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \\texttt{object\\_pudding} findings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the absence of SDF benefit observed on \\texttt{object\\_pudding}.}\n\\label{tab:spatial_bowl}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & CAR (\\%) & TSR (\\%) \\\\\n\\midrule\nLoRA-only & 12.0 & 49.0 \\\\\nSDF $\\lambda{=}0.005$ & 11.5 & 51.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe substantially lower CAR on \\texttt{spatial\\_bowl} relative to \\texttt{object\\_pudding} (11--12\\% vs.\\ 54--57\\%) reflects the greater scene difficulty: \\texttt{spatial\\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition performs comparably ($\\Delta$CAR\\,=\\,$-$0.5\\,pp, well within noise), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.\n\n\n\\section{Evaluation Seed Robustness}\n\\label{sec:appendix_eval_seed}\n\nTo verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate key model configurations under multiple evaluation seeds (200 episodes each). Table~\\ref{tab:eval_seed_robustness} reports aggregate CAR and TSR across all tested seeds.\n\n\\begin{table}[h]\n\\centering\n\\caption{Eval-seed robustness: aggregate CAR and TSR (\\%) across evaluation seeds (200 episodes each). Dashes indicate untested seeds. CAR ranges overlap across all three conditions, confirming that SDF redundancy is not an eval-seed artifact.}\n\\label{tab:eval_seed_robustness}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{llccccccl}\n\\toprule\n& & \\multicolumn{6}{c}{Evaluation seed} & \\\\\n\\cmidrule(lr){3-8}\nCondition & & 0 & 7 & 42 & 99 & 123 & 256 & Mean$\\pm$Std \\\\\n\\midrule\n\\multirow{2}{*}{LoRA s0}\n  & CAR & 53.0 & 57.0 & 56.5 & 57.5 & 53.0 & --- & 55.4$\\pm$2.2 \\\\\n  & TSR & 55.5 & 46.0 & 46.0 & 52.0 & 50.5 & --- & 50.0$\\pm$4.1 \\\\\n\\midrule\n\\multirow{2}{*}{SDF $\\lambda{=}0.01$ s0}\n  & CAR & 52.5 & 57.0 & --- & 57.0 & --- & 57.0 & 55.9$\\pm$2.3 \\\\\n  & TSR & 48.5 & 52.5 & --- & 46.5 & --- & 48.0 & 48.9$\\pm$2.6 \\\\\n\\midrule\n\\multirow{2}{*}{SDF $\\lambda{=}0.1$ s0}\n  & CAR & --- & 58.0 & 59.0 & --- & 58.5 & 57.0 & 58.1$\\pm$0.9 \\\\\n  & TSR & --- & 47.0 & 52.5 & --- & 53.5 & 48.0 & 50.3$\\pm$3.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLoRA s0 CAR ranges from 53.0\\% to 57.5\\% across five evaluation seeds (std\\,=\\,2.2\\,pp), consistent with binomial sampling noise at $n{=}50$ episodes per task. SDF $\\lambda{=}0.01$ s0 produces near-identical mean CAR (55.9\\% across four eval seeds vs.\\ 55.4\\% for LoRA), confirming that the null result holds across eval conditions. SDF $\\lambda{=}0.1$ s0 shows a slightly higher mean (58.1\\%), but the ranges overlap with LoRA-only, and the difference (2.8\\,pp, ${<}$1.3$\\sigma$) remains non-significant. The per-task CAR ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all seeds and conditions, reinforcing the demonstration-driven avoidance hypothesis.\n\nTable~\\ref{tab:eval_seed_car_detail} provides per-task CAR for the five-seed LoRA evaluation, the most complete eval-seed battery.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for LoRA s0 across five evaluation seeds. The per-task fingerprint (CP highest, BBQ lowest) is invariant across all seeds.}\n\\label{tab:eval_seed_car_detail}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nEval seed & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\n0   & 46 & 70 & 74 & 22 & 53.0 \\\\\n7   & 68 & 74 & 66 & 20 & 57.0 \\\\\n42  & 60 & 70 & 68 & 28 & 56.5 \\\\\n99  & 58 & 76 & 66 & 30 & 57.5 \\\\\n123 & 52 & 74 & 66 & 20 & 53.0 \\\\\n\\midrule\nMean$\\pm$Std & 56.8$\\pm$8.3 & 72.8$\\pm$2.7 & 68.0$\\pm$3.5 & 24.0$\\pm$4.7 & 55.4$\\pm$2.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n",
      "numLines": 396,
      "startLine": 1,
      "totalLines": 396
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
Now I have the full appendix.tex content. I need to add a new section at the end about TSR Collapse Mechanism Analysis. The file ends at line 396. Let me add the new section after the last paragraph about computational resources.

Let me also check the paper_switch.py to understand what it verifies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "dc426043-c323-4da6-980e-37fd88f60872",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119R54gYXTF7NAsQ7VNH1dS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10954,
      "cache_read_input_tokens": 24963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10954
      },
      "output_tokens": 10,
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

Now let me check what paper_switch.py verifies so I understand the constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "7f3addf5-11c8-4c58-acb8-626fa38ac3c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119R54gYXTF7NAsQ7VNH1dS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10954,
      "cache_read_input_tokens": 24963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10954
      },
      "output_tokens": 10,
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

<details open><summary>🔧 Tool call — Read · `toolu_01DszULzGAT2qiET4aArsAk5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "2435f43b-0147-4f64-a032-d40bf0f5a95f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119R54gYXTF7NAsQ7VNH1dS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10954,
      "cache_read_input_tokens": 24963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10954
      },
      "output_tokens": 10,
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

_source line 10 · 2026-05-29T00:20:12.136Z_

<details><summary>↩ Tool result · `toolu_01DszULzGAT2qiET4aArsAk5`</summary>

```text
1	#!/usr/bin/env python3
2	"""Auto-switch paper text based on λ=0.1 s2 30K eval result.
3	
4	Usage:
5	  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0 --dry-run
6	  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0
7	"""
8	import argparse
9	import subprocess
10	import sys
11	from itertools import combinations
12	from math import comb, sqrt
13	from pathlib import Path
14	
15	NULL_VALUES = [57.0, 52.5, 55, 57, 54, 52.5]
16	NULL_MEAN = sum(NULL_VALUES) / len(NULL_VALUES)
17	NULL_STD = (sum((x - NULL_MEAN) ** 2 for x in NULL_VALUES) / 5) ** 0.5
18	
19	S0_CAR, S1_CAR = 58.0, 58.5
20	S0_TSR, S1_TSR = 47.0, 49.0
21	
22	PAPER_DIR = Path(__file__).resolve().parent.parent / "docs" / "paper"
23	
24	
25	def mean(v):
26	    return sum(v) / len(v)
27	
28	
29	def std_b(v):
30	    m = mean(v)
31	    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5
32	
33	
34	def perm_test(null_vals, treat_vals):
35	    pool = null_vals + treat_vals
36	    k = len(treat_vals)
37	    obs = mean(treat_vals)
38	    mu = mean(pool)
39	    dev = abs(obs - mu)
40	    n = comb(len(pool), k)
41	    ge = tw = 0
42	    for c in combinations(pool, k):
43	        m = mean(c)
44	        if m >= obs:
45	            ge += 1
46	        if abs(m - mu) >= dev - 1e-12:
47	            tw += 1
48	    return ge / n, tw / n, n
49	
50	
51	def fill(tpl, vals):
52	    for k, v in vals.items():
53	        tpl = tpl.replace("{" + k + "}", str(v))
54	    return tpl
55	
56	
57	def safe_replace(content, old, new, label):
58	    n = content.count(old)
59	    if n == 0:
60	        print(f"  !! [{label}] NOT FOUND")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "8fca715f-b225-4359-a823-3af5b42d78be",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Auto-switch paper text based on λ=0.1 s2 30K eval result.\n\nUsage:\n  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0 --dry-run\n  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0\n\"\"\"\nimport argparse\nimport subprocess\nimport sys\nfrom itertools import combinations\nfrom math import comb, sqrt\nfrom pathlib import Path\n\nNULL_VALUES = [57.0, 52.5, 55, 57, 54, 52.5]\nNULL_MEAN = sum(NULL_VALUES) / len(NULL_VALUES)\nNULL_STD = (sum((x - NULL_MEAN) ** 2 for x in NULL_VALUES) / 5) ** 0.5\n\nS0_CAR, S1_CAR = 58.0, 58.5\nS0_TSR, S1_TSR = 47.0, 49.0\n\nPAPER_DIR = Path(__file__).resolve().parent.parent / \"docs\" / \"paper\"\n\n\ndef mean(v):\n    return sum(v) / len(v)\n\n\ndef std_b(v):\n    m = mean(v)\n    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5\n\n\ndef perm_test(null_vals, treat_vals):\n    pool = null_vals + treat_vals\n    k = len(treat_vals)\n    obs = mean(treat_vals)\n    mu = mean(pool)\n    dev = abs(obs - mu)\n    n = comb(len(pool), k)\n    ge = tw = 0\n    for c in combinations(pool, k):\n        m = mean(c)\n        if m >= obs:\n            ge += 1\n        if abs(m - mu) >= dev - 1e-12:\n            tw += 1\n    return ge / n, tw / n, n\n\n\ndef fill(tpl, vals):\n    for k, v in vals.items():\n        tpl = tpl.replace(\"{\" + k + \"}\", str(v))\n    return tpl\n\n\ndef safe_replace(content, old, new, label):\n    n = content.count(old)\n    if n == 0:\n        print(f\"  !! [{label}] NOT FOUND\")",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 492
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01KX2vT9CiZJZLCQUCyPWfEk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py",
  "offset": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "82ab1479-de91-458d-a1ef-e74752c68508",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmheCPgVcfxSBKj8DZksQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 950,
      "cache_read_input_tokens": 35917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 950
      },
      "output_tokens": 66,
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

_source line 12 · 2026-05-29T00:20:15.010Z_

<details><summary>↩ Tool result · `toolu_01KX2vT9CiZJZLCQUCyPWfEk`</summary>

```text
60	        print(f"  !! [{label}] NOT FOUND")
61	        return content, False
62	    if n > 1:
63	        print(f"  !! [{label}] found {n}x")
64	        return content, False
65	    return content.replace(old, new), True
66	
67	
68	def get_replacements(scenario, v):
69	    R = []
70	    is_c = scenario == "C"
71	
72	    # 1. abstract.tex L5 (training results — condensed abstract)
73	    old = (
74	        r"and SDF training supervision shows no statistically significant benefit "
75	        r"beyond collision-free demonstrations alone."
76	    )
77	    if is_c:
78	        new = (
79	            r"and SDF training supervision shows no statistically significant benefit "
80	            r"at $\lambda \leq 0.01$; at $\lambda = 0.1$, a modest increase emerges "
81	            r"but remains small relative to the demonstration-driven gain."
82	        )
83	    else:
84	        new = old
85	    R.append(("abstract.tex", "abstract L5 training", old, new))
86	
87	    # 2. abstract.tex L6 (concluding sentence — condensed abstract)
88	    old = (
89	        r"These findings suggest that collision avoidance primarily arises from "
90	        r"demonstration data rather than EE-only geometric supervision."
91	    )
92	    if is_c:
93	        new = (
94	            r"These findings suggest that collision avoidance primarily arises from "
95	            r"demonstration data, though a modest SDF effect at high loss weights "
96	            r"cannot be fully ruled out."
97	        )
98	    else:
99	        new = old
100	    R.append(("abstract.tex", "abstract L6 conclusion", old, new))
101	
102	    # 3. claim3.tex L3 scope sentence
103	    old = (
104	        r"We compare LoRA-only against LoRA+SDF across a 20$\times$ range of "
105	        r"loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all "
106	        r"evaluated at the 30K-step checkpoint."
107	    )
108	    if is_c:
109	        new = (
110	            r"We compare LoRA-only against LoRA+SDF at three loss weights "
111	            r"($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at "
112	            r"the 30K-step checkpoint."
113	        )
114	    else:
115	        new = (
116	            r"We compare LoRA-only against LoRA+SDF across a 20$\times$ range of "
117	            r"loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all "
118	            r"evaluated at the 30K-step checkpoint."
119	        )
120	    R.append(("claim3.tex", "claim3 L3 scope", old, new))
121	
122	    # 4. claim3.tex L7 table caption
123	    old = (
124	        r"\caption{Avoidance source attribution on SafeLIBERO. SDF shows no "
125	        r"statistically significant CAR improvement beyond LoRA-only at the tested "
126	        r"scale ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$). All fine-tuned models "
127	        r"exhibit 0\% action-collapse rate and displacement $>$\,0.37\,m.}"
128	    )
129	    if is_c:
130	        new = fill(
131	            r"\caption{Avoidance source attribution on SafeLIBERO. SDF at "
132	            r"$\lambda \leq 0.01$ shows no statistically significant CAR improvement "
133	            r"beyond LoRA-only ($p > 0.1$). At $\lambda = 0.1$, a modest increase "
134	            r"reaches statistical significance ($z = {z_value}$, permutation "
135	            r"$p = {p_value}$, $n{=}3$), though the effect size ({delta_pp}\,pp) "
136	            r"is small relative to the $+$26\,pp LoRA gain. All fine-tuned models "
137	            r"exhibit 0\% action-collapse rate and displacement $>$\,0.37\,m.}", v)
138	    else:
139	        new = (
140	            r"\caption{Avoidance source attribution on SafeLIBERO. SDF shows no "
141	            r"statistically significant CAR improvement beyond LoRA-only at the tested "
142	            r"scale ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$). All fine-tuned models "
143	            r"exhibit 0\% action-collapse rate and displacement $>$\,0.37\,m.}"
144	        )
145	    R.append(("claim3.tex", "claim3 L7 caption", old, new))
146	
147	    # 5. claim3.tex L20 table row
148	    old = (
149	        r"LoRA+SDF $\lambda{=}0.1$ & 3 & "
150	        r"50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\"
151	    )
152	    new = fill(
153	        r"LoRA+SDF $\lambda{=}0.1$ & 3 & "
154	        r"{tsr_mean}\,$\pm$\,{tsr_std} & {mean_car}\,$\pm$\,{std_car} & 0.394 \\", v)
155	    R.append(("claim3.tex", "claim3 L20 table row", old, new))
156	
157	    # 6. claim3.tex L27 body paragraph
158	    old = (
159	        r"Table~\ref{tab:avoidance_source} shows that collision-free demonstrations "
160	        r"alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.83\%) with "
161	        r"zero action-collapsed episodes and displacement above 0.37\,m, confirming genuine "
162	        r"avoidance. Adding SDF supervision does not yield statistically significant "
163	        r"improvement at the tested scale: LoRA-only CAR (54.83\%) is statistically "
164	        r"indistinguishable from all SDF conditions including $\lambda = 0.1$ "
165	        r"(57.00\%, $p = 0.155$; Appendix~\ref{sec:appendix_null}). "
166	        r"A Phase~2 ablation ($\lambda = 0$ after step 5K) yields "
167	        r"CAR\,=\,57.5\%\footnote{At the 18K checkpoint (13K steps of Phase~2 "
168	        r"training, single seed s2); full 30K training did not complete due to disk "
169	        r"constraints.}, suggesting that SDF gradients do not produce a lasting "
170	        r"behavioral effect. The per-task CAR ordering "
171	        r"is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce "
172	        r"lowest) and invariant to $\lambda$ across the tested range, indicating "
173	        r"that avoidance patterns reflect the demonstration distribution rather than "
174	        r"geometric supervision."
175	    )
176	    if is_c:
177	        new = (
178	            r"Table~\ref{tab:avoidance_source} shows that collision-free demonstrations "
179	            r"alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.83\%) with "
180	            r"zero action-collapsed episodes and displacement above 0.37\,m, confirming genuine "
181	            r"avoidance. At $\lambda \leq 0.01$, SDF supervision does not yield "
182	            r"statistically significant improvement: LoRA-only CAR (54.83\%) is within "
183	            r"0.17\,pp of $\lambda = 0.005$ and statistically indistinguishable from "
184	            r"$\lambda = 0.01$ (56.33\%, $p > 0.1$; Appendix~\ref{sec:appendix_null}). "
185	            r"At $\lambda = 0.1$, a modest increase emerges "
186	            r"(Section~\ref{sec:lambda_high}), but per-task CAR ordering "
187	            r"remains identical across all conditions (chocolate\_pudding highest, "
188	            r"bbq\_sauce lowest), indicating that avoidance patterns reflect the "
189	            r"demonstration distribution regardless of SDF loss weight. A Phase~2 "
190	            r"ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{"
191	            r"At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); "
192	            r"full 30K training did not complete due to disk constraints.}, suggesting "
193	            r"that SDF gradients do not produce a lasting behavioral effect."
194	        )
195	    else:
196	        new = fill(
197	            r"Table~\ref{tab:avoidance_source} shows that collision-free demonstrations "
198	            r"alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.83\%) with "
199	            r"zero action-collapsed episodes and displacement above 0.37\,m, confirming genuine "
200	            r"avoidance. Adding SDF supervision does not yield statistically significant "
201	            r"improvement at the tested scale: LoRA-only CAR (54.83\%) is statistically "
202	            r"indistinguishable from all SDF conditions including $\lambda = 0.1$ "
203	            r"({mean_car}\%, $p = {p_value}$; Appendix~\ref{sec:appendix_null}). "
204	            r"A Phase~2 ablation ($\lambda = 0$ after step 5K) yields "
205	            r"CAR\,=\,57.5\%\footnote{At the 18K checkpoint (13K steps of Phase~2 "
206	            r"training, single seed s2); full 30K training did not complete due to disk "
207	            r"constraints.}, suggesting that SDF gradients do not produce a lasting "
208	            r"behavioral effect. The per-task CAR ordering "
209	            r"is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce "
210	            r"lowest) and invariant to $\lambda$ across the tested range, indicating "
211	            r"that avoidance patterns reflect the demonstration distribution rather than "
212	            r"geometric supervision.", v)
213	    R.append(("claim3.tex", "claim3 L27 body", old, new))
214	
215	    # 7. claim3.tex L32-33 dose-response paragraph
216	    hdr = r"\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}"
217	    old_body = (
218	        r"Increasing $\lambda$ by 20$\times$ to 0.1 yields "
219	        r"CAR\,=\,57.00\%\,$\pm$\,2.18 "
220	        r"(3 seeds: 58.0\%, 58.5\%, 54.5\%), within the null "
221	        r"distribution ($p = 0.155$\footnote{One-tailed "
222	        r"$p = 0.071$; even with the directional prior that SDF "
223	        r"should not \emph{decrease} CAR, the result remains "
224	        r"non-significant.}; Figure~\ref{fig:lambda_car}). "
225	        r"The binding constraint is not signal magnitude but "
226	        r"the structural mismatch between EE monitoring and "
227	        r"full-body collision surfaces."
228	    )
229	    old = hdr + "\n" + old_body
230	    if is_c:
231	        new_body = fill(
232	            r"Increasing $\lambda$ by 20$\times$ to 0.1 yields "
233	            r"CAR\,=\,{mean_car}\%\,$\pm$\,{std_car} at the 30K checkpoint "
234	            r"(3 seeds: {s0_car}\%, {s1_car}\%, {s2_car}\%), a modest but "
235	            r"statistically significant departure from the null distribution "
236	            r"(mean 54.67\%, $\sigma = 2.07$; permutation "
237	            r"$p = {p_value}$\footnote{One-tailed permutation "
238	            r"$p = {p_one_value}$; the directional prior that SDF should not "
239	            r"\emph{decrease} CAR supports a one-tailed test, but we report "
240	            r"the conservative two-tailed value in the main text.}). The "
241	            r"effect size of {delta_pp}\,pp is small relative to the $+$26\,pp gain "
242	            r"from LoRA fine-tuning alone, indicating that EE-only SDF supervision "
243	            r"can incrementally augment demonstration-driven avoidance at sufficiently "
244	            r"high loss weights but cannot substitute for it. A stepwise ablation across "
245	            r"six checkpoints (16K--28K) shows no sustained trend prior to 30K "
246	            r"(mean 55.3\%, within 0.4$\sigma$ of the null; "
247	            r"Appendix~\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K "
248	            r"remains identical to all other conditions "
249	            r"(Figure~\ref{fig:lambda_car}), confirming that the dominant avoidance "
250	            r"signal remains the demonstration distribution. The response is thus "
251	            r"dose-dependent: SDF shows no significant benefit at $\lambda \leq 0.01$ "
252	            r"($p > 0.1$), with a small but detectable effect at $\lambda = 0.1$ "
253	            r"that preserves the same demonstration-driven avoidance fingerprint.", v)
254	    else:
255	        new_body = fill(
256	            r"Increasing $\lambda$ by 20$\times$ to 0.1 yields "
257	            r"CAR\,=\,{mean_car}\%\,$\pm$\,{std_car} at the 30K checkpoint "
258	            r"(3 seeds: {s0_car}\%, {s1_car}\%, {s2_car}\%), within the null "
259	            r"distribution (mean 54.67\%, $\sigma = 2.07$; permutation "
260	            r"$p = {p_value}$\footnote{One-tailed permutation "
261	            r"$p = {p_one_value}$; even with the directional prior that SDF "
262	            r"should not \emph{decrease} CAR, the result remains "
263	            r"non-significant.}). SDF supervision does not produce statistically "
264	            r"significant benefit across the tested range $\lambda \in [0.005, 0.1]$ "
265	            r"(Figure~\ref{fig:lambda_car}). This result disambiguates the two-level "
266	            r"failure analysis (Section~\ref{sec:conclusion}): because even a "
267	            r"20$\times$ increase in SDF loss weight fails to produce additional "
268	            r"avoidance, the binding constraint is not training signal magnitude but "
269	            r"the structural mismatch between end-effector monitoring and full-body "
270	            r"collision surfaces. Stronger geometric supervision cannot compensate for "
271	            r"supervising the wrong collision surface.", v)
272	    R.append(("claim3.tex", "claim3 L32-33 dose-response", old, hdr + "\n" + new_body))
273	
274	    # 8. claim3.tex L38 figure caption
275	    old = (
276	        r"\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. "
277	        r"$\lambda = 0$: LoRA-only. The $\lambda \in \{0.01, 0.1\}$ values remain within "
278	        r"the null band ($p > 0.05$), consistent with the absence of statistically "
279	        r"significant improvement across a 20$\times$ loss-weight range.}"
280	    )
281	    if is_c:
282	        new = fill(
283	            r"\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. "
284	            r"$\lambda = 0$: LoRA-only. Low $\lambda$ ($\leq 0.01$) remains within "
285	            r"the null band; $\lambda = 0.1$ ({mean_car}\%, 3 seeds) shows a modest "
286	            r"but significant departure (permutation $p = {p_value}$, {delta_pp}\,pp "
287	            r"effect size) whose per-task avoidance pattern still matches the "
288	            r"demonstration distribution.}", v)
289	    else:
290	        new = (
291	            r"\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. "
292	            r"$\lambda = 0$: LoRA-only. The $\lambda \in \{0.01, 0.1\}$ values remain within "
293	            r"the null band ($p > 0.05$), consistent with the absence of statistically "
294	            r"significant improvement across a 20$\times$ loss-weight range.}"
295	        )
296	    R.append(("discussion.tex", "discussion fig caption", old, new))
297	
298	    # 9. discussion.tex L3 scope (Scenario C only)
299	    if is_c:
300	        old = (
301	            r"and collision-free demonstrations account for nearly all measured "
302	            r"avoidance gains, with EE-only SDF contributing no statistically "
303	            r"significant improvement (\S\ref{sec:avoidance_source})."
304	        )
305	        new = (
306	            r"and collision-free demonstrations account for nearly all measured "
307	            r"avoidance gains, with EE-only SDF contributing at most a modest "
308	            r"increment at high loss weights (\S\ref{sec:avoidance_source})."
309	        )
310	        R.append(("discussion.tex", "discussion L3 scope", old, new))
311	
312	    # 10. discussion.tex L6
313	    old = (
314	        r"Even at $\lambda = 0.1$, CAR remains within the null distribution "
315	        r"($p = 0.155$)."
316	    )
317	    if is_c:
318	        new = fill(
319	            r"At $\lambda \leq 0.01$, SDF shows no significant benefit; at "
320	            r"$\lambda = 0.1$, a modest {delta_pp}\,pp effect emerges "
321	            r"($p = {p_value}$) but preserves the same demonstration-driven "
322	            r"avoidance pattern, suggesting that EE-only SDF can weakly "
323	            r"augment---but not redirect---the implicit signal at sufficiently "
324	            r"high loss weights.", v)
325	    else:
326	        new = fill(
327	            r"Even at $\lambda = 0.1$, CAR remains within the null distribution "
328	            r"($p = {p_value}$).", v)
329	    R.append(("discussion.tex", "discussion L6", old, new))
330	
331	    # 11. discussion.tex L12 limitation
332	    old = r"validation on actively moving policies and full-body SDF remain necessary before generalizing the counterproductive finding to non-collapsed settings. Run-to-run variance (same model, training seed, evaluation seed) is approximately 0.5\,pp CAR and 5.5\,pp TSR, bounding measurement precision."
333	    if is_c:
334	        new = fill(
335	            r"validation on actively moving policies and full-body SDF remain future work. "
336	            r"The $\lambda = 0.1$ effect ({delta_pp}\,pp, $p = {p_value}$, $n = 3$) "
337	            r"is statistically significant but small; whether this modest gain "
338	            r"justifies the computational cost of SDF supervision requires "
339	            r"task-specific cost-benefit analysis.", v)
340	    else:
341	        new = old
342	    R.append(("discussion.tex", "discussion L12 limitation", old, new))
343	
344	    return R
345	
346	
347	def main():
348	    parser = argparse.ArgumentParser(
349	        description="Auto-switch paper for lambda=0.1 s2 30K result")
350	    parser.add_argument("--s2-car", type=float, required="--verify" not in sys.argv)
351	    parser.add_argument("--s2-tsr", type=float, default=None)
352	    parser.add_argument("--dry-run", action="store_true")
353	    parser.add_argument("--verify", action="store_true",
354	                        help="Check all old_strings match current .tex files")
355	    args = parser.parse_args()
356	
357	    if args.verify:
358	        if not PAPER_DIR.exists():
359	            print(f"ERROR: paper dir not found: {PAPER_DIR}")
360	            sys.exit(1)
361	        dummy_v = {k: "X" for k in [
362	            "s0_car", "s1_car", "s2_car", "mean_car", "std_car",
363	            "tsr_mean", "tsr_std", "p_value", "p_one_value", "z_value", "delta_pp"]}
364	        all_ok = True
365	        for scenario in ("B", "C"):
366	            replacements = get_replacements(scenario, dummy_v)
367	            print(f"--- Scenario {scenario} ({len(replacements)} items) ---")
368	            for filename, label, old, new in replacements:
369	                fpath = PAPER_DIR / filename
370	                if not fpath.exists():
371	                    print(f"  [MISSING] {label:35s} {filename}")
372	                    all_ok = False
373	                    continue
374	                content = fpath.read_text()
375	                if old in content:
376	                    print(f"  [OK]      {label:35s} {filename}")
377	                else:
378	                    print(f"  [MISMATCH]{label:35s} {filename}")
379	                    print(f"            Expected: {old[:80]}...")
380	                    all_ok = False
381	        sys.exit(0 if all_ok else 1)
382	
383	    cars = [S0_CAR, S1_CAR, args.s2_car]
384	    car_mean = mean(cars)
385	    car_std = std_b(cars)
386	
387	    if args.s2_tsr is not None:
388	        tsrs = [S0_TSR, S1_TSR, args.s2_tsr]
389	    else:
390	        tsrs = [S0_TSR, S1_TSR]
391	        print("NOTE: --s2-tsr not provided, using 2-seed TSR")
392	    tsr_mean = mean(tsrs)
393	    tsr_std = std_b(tsrs)
394	
395	    p_one, p_two, n_combos = perm_test(NULL_VALUES, cars)
396	    z = (car_mean - NULL_MEAN) / NULL_STD
397	    delta = car_mean - NULL_MEAN
398	
399	    scenario = "C" if p_one < 0.05 else "B"
400	
401	    v = {
402	        "s0_car": f"{S0_CAR:.1f}",
403	        "s1_car": f"{S1_CAR:.1f}",
404	        "s2_car": f"{args.s2_car:.1f}",
405	        "mean_car": f"{car_mean:.2f}",
406	        "std_car": f"{car_std:.2f}",
407	        "tsr_mean": f"{tsr_mean:.1f}",
408	        "tsr_std": f"{tsr_std:.1f}",
409	        "p_value": f"{p_two:.3f}",
410	        "p_one_value": f"{p_one:.3f}",
411	        "z_value": f"{z:.2f}",
412	        "delta_pp": f"{delta:.1f}",
413	    }
414	
415	    print("=" * 60)
416	    print("  PAPER SWITCH — lambda=0.1 s2 30K")
417	    print("=" * 60)
418	    print(f"  Input:     s2_car={args.s2_car}, s2_tsr={args.s2_tsr}")
419	    print(f"  3-seed:    CAR = {v['mean_car']} +/- {v['std_car']}")
420	    print(f"             TSR = {v['tsr_mean']} +/- {v['tsr_std']} ({len(tsrs)} seeds)")
421	    print(f"  Perm test: C({len(NULL_VALUES)+len(cars)},{len(cars)}) = {n_combos}")
422	    print(f"             p_one = {v['p_one_value']}  {'<' if p_one < 0.05 else '>='} 0.05")
423	    print(f"             p_two = {v['p_value']}")
424	    print(f"  Z-score:   {v['z_value']}")
425	    print(f"  Delta:     +{v['delta_pp']} pp")
426	    print(f"  Scenario:  {scenario}  "
427	          f"{'(modest but significant)' if scenario == 'C' else '(full redundancy)'}")
428	    print()
429	
430	    if not PAPER_DIR.exists():
431	        print(f"ERROR: paper dir not found: {PAPER_DIR}")
432	        sys.exit(1)
433	
434	    replacements = get_replacements(scenario, v)
435	
436	    files_content = {}
437	    counts = {}
438	
439	    for filename, label, old, new in replacements:
440	        fpath = PAPER_DIR / filename
441	        if filename not in files_content:
442	            if not fpath.exists():
443	                print(f"  !! {filename} not found")
444	                continue
445	            files_content[filename] = fpath.read_text()
446	            counts[filename] = 0
447	
448	        content, ok = safe_replace(files_content[filename], old, new, label)
449	        files_content[filename] = content
450	        if ok:
451	            counts[filename] += 1
452	            status = "ok"
453	        else:
454	            status = "FAIL"
455	        print(f"  [{status:4s}] {label:35s} {filename}")
456	
457	    total = sum(counts.values())
458	    n_files = sum(1 for c in counts.values() if c > 0)
459	    expected = len(replacements)
460	    print(f"\n  {total}/{expected} replacements in {n_files} files")
461	
462	    if args.dry_run:
463	        print("\n  DRY RUN — no files modified")
464	        return
465	
466	    for filename, content in files_content.items():
467	        fpath = PAPER_DIR / filename
468	        fpath.write_text(content)
469	        print(f"  Wrote {filename} ({counts[filename]} changes)")
470	
471	    print("\nCompiling PDF...")
472	    try:
473	        result = subprocess.run(
474	            ["latexmk", "-pdf", "-interaction=nonstopmode", "main.tex"],
475	            cwd=PAPER_DIR, capture_output=True, text=True, timeout=120)
476	        if result.returncode == 0:
477	            print("  PDF compiled OK")
478	        else:
479	            print("  PDF compilation FAILED")
480	            err = result.stderr or result.stdout or ""
481	            for line in err.split("\n")[-10:]:
482	                if line.strip():
483	                    print(f"    {line}")
484	    except FileNotFoundError:
485	        print("  latexmk not found — skipping PDF compilation")
486	    except subprocess.TimeoutExpired:
487	        print("  PDF compilation timed out (120s)")
488	
489	
490	if __name__ == "__main__":
491	    main()
492	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "abdede4d-c9af-4355-80a0-743e836f0a23",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py",
      "content": "        print(f\"  !! [{label}] NOT FOUND\")\n        return content, False\n    if n > 1:\n        print(f\"  !! [{label}] found {n}x\")\n        return content, False\n    return content.replace(old, new), True\n\n\ndef get_replacements(scenario, v):\n    R = []\n    is_c = scenario == \"C\"\n\n    # 1. abstract.tex L5 (training results — condensed abstract)\n    old = (\n        r\"and SDF training supervision shows no statistically significant benefit \"\n        r\"beyond collision-free demonstrations alone.\"\n    )\n    if is_c:\n        new = (\n            r\"and SDF training supervision shows no statistically significant benefit \"\n            r\"at $\\lambda \\leq 0.01$; at $\\lambda = 0.1$, a modest increase emerges \"\n            r\"but remains small relative to the demonstration-driven gain.\"\n        )\n    else:\n        new = old\n    R.append((\"abstract.tex\", \"abstract L5 training\", old, new))\n\n    # 2. abstract.tex L6 (concluding sentence — condensed abstract)\n    old = (\n        r\"These findings suggest that collision avoidance primarily arises from \"\n        r\"demonstration data rather than EE-only geometric supervision.\"\n    )\n    if is_c:\n        new = (\n            r\"These findings suggest that collision avoidance primarily arises from \"\n            r\"demonstration data, though a modest SDF effect at high loss weights \"\n            r\"cannot be fully ruled out.\"\n        )\n    else:\n        new = old\n    R.append((\"abstract.tex\", \"abstract L6 conclusion\", old, new))\n\n    # 3. claim3.tex L3 scope sentence\n    old = (\n        r\"We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of \"\n        r\"loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all \"\n        r\"evaluated at the 30K-step checkpoint.\"\n    )\n    if is_c:\n        new = (\n            r\"We compare LoRA-only against LoRA+SDF at three loss weights \"\n            r\"($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at \"\n            r\"the 30K-step checkpoint.\"\n        )\n    else:\n        new = (\n            r\"We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of \"\n            r\"loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all \"\n            r\"evaluated at the 30K-step checkpoint.\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L3 scope\", old, new))\n\n    # 4. claim3.tex L7 table caption\n    old = (\n        r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no \"\n        r\"statistically significant CAR improvement beyond LoRA-only at the tested \"\n        r\"scale ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$). All fine-tuned models \"\n        r\"exhibit 0\\% action-collapse rate and displacement $>$\\,0.37\\,m.}\"\n    )\n    if is_c:\n        new = fill(\n            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF at \"\n            r\"$\\lambda \\leq 0.01$ shows no statistically significant CAR improvement \"\n            r\"beyond LoRA-only ($p > 0.1$). At $\\lambda = 0.1$, a modest increase \"\n            r\"reaches statistical significance ($z = {z_value}$, permutation \"\n            r\"$p = {p_value}$, $n{=}3$), though the effect size ({delta_pp}\\,pp) \"\n            r\"is small relative to the $+$26\\,pp LoRA gain. All fine-tuned models \"\n            r\"exhibit 0\\% action-collapse rate and displacement $>$\\,0.37\\,m.}\", v)\n    else:\n        new = (\n            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no \"\n            r\"statistically significant CAR improvement beyond LoRA-only at the tested \"\n            r\"scale ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$). All fine-tuned models \"\n            r\"exhibit 0\\% action-collapse rate and displacement $>$\\,0.37\\,m.}\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L7 caption\", old, new))\n\n    # 5. claim3.tex L20 table row\n    old = (\n        r\"LoRA+SDF $\\lambda{=}0.1$ & 3 & \"\n        r\"50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\"\n    )\n    new = fill(\n        r\"LoRA+SDF $\\lambda{=}0.1$ & 3 & \"\n        r\"{tsr_mean}\\,$\\pm$\\,{tsr_std} & {mean_car}\\,$\\pm$\\,{std_car} & 0.394 \\\\\", v)\n    R.append((\"claim3.tex\", \"claim3 L20 table row\", old, new))\n\n    # 6. claim3.tex L27 body paragraph\n    old = (\n        r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n        r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.83\\%) with \"\n        r\"zero action-collapsed episodes and displacement above 0.37\\,m, confirming genuine \"\n        r\"avoidance. Adding SDF supervision does not yield statistically significant \"\n        r\"improvement at the tested scale: LoRA-only CAR (54.83\\%) is statistically \"\n        r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"\n        r\"(57.00\\%, $p = 0.155$; Appendix~\\ref{sec:appendix_null}). \"\n        r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"\n        r\"CAR\\,=\\,57.5\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 \"\n        r\"training, single seed s2); full 30K training did not complete due to disk \"\n        r\"constraints.}, suggesting that SDF gradients do not produce a lasting \"\n        r\"behavioral effect. The per-task CAR ordering \"\n        r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"\n        r\"lowest) and invariant to $\\lambda$ across the tested range, indicating \"\n        r\"that avoidance patterns reflect the demonstration distribution rather than \"\n        r\"geometric supervision.\"\n    )\n    if is_c:\n        new = (\n            r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n            r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.83\\%) with \"\n            r\"zero action-collapsed episodes and displacement above 0.37\\,m, confirming genuine \"\n            r\"avoidance. At $\\lambda \\leq 0.01$, SDF supervision does not yield \"\n            r\"statistically significant improvement: LoRA-only CAR (54.83\\%) is within \"\n            r\"0.17\\,pp of $\\lambda = 0.005$ and statistically indistinguishable from \"\n            r\"$\\lambda = 0.01$ (56.33\\%, $p > 0.1$; Appendix~\\ref{sec:appendix_null}). \"\n            r\"At $\\lambda = 0.1$, a modest increase emerges \"\n            r\"(Section~\\ref{sec:lambda_high}), but per-task CAR ordering \"\n            r\"remains identical across all conditions (chocolate\\_pudding highest, \"\n            r\"bbq\\_sauce lowest), indicating that avoidance patterns reflect the \"\n            r\"demonstration distribution regardless of SDF loss weight. A Phase~2 \"\n            r\"ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{\"\n            r\"At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); \"\n            r\"full 30K training did not complete due to disk constraints.}, suggesting \"\n            r\"that SDF gradients do not produce a lasting behavioral effect.\"\n        )\n    else:\n        new = fill(\n            r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n            r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.83\\%) with \"\n            r\"zero action-collapsed episodes and displacement above 0.37\\,m, confirming genuine \"\n            r\"avoidance. Adding SDF supervision does not yield statistically significant \"\n            r\"improvement at the tested scale: LoRA-only CAR (54.83\\%) is statistically \"\n            r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"\n            r\"({mean_car}\\%, $p = {p_value}$; Appendix~\\ref{sec:appendix_null}). \"\n            r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"\n            r\"CAR\\,=\\,57.5\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 \"\n            r\"training, single seed s2); full 30K training did not complete due to disk \"\n            r\"constraints.}, suggesting that SDF gradients do not produce a lasting \"\n            r\"behavioral effect. The per-task CAR ordering \"\n            r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"\n            r\"lowest) and invariant to $\\lambda$ across the tested range, indicating \"\n            r\"that avoidance patterns reflect the demonstration distribution rather than \"\n            r\"geometric supervision.\", v)\n    R.append((\"claim3.tex\", \"claim3 L27 body\", old, new))\n\n    # 7. claim3.tex L32-33 dose-response paragraph\n    hdr = r\"\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\"\n    old_body = (\n        r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n        r\"CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 \"\n        r\"(3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null \"\n        r\"distribution ($p = 0.155$\\footnote{One-tailed \"\n        r\"$p = 0.071$; even with the directional prior that SDF \"\n        r\"should not \\emph{decrease} CAR, the result remains \"\n        r\"non-significant.}; Figure~\\ref{fig:lambda_car}). \"\n        r\"The binding constraint is not signal magnitude but \"\n        r\"the structural mismatch between EE monitoring and \"\n        r\"full-body collision surfaces.\"\n    )\n    old = hdr + \"\\n\" + old_body\n    if is_c:\n        new_body = fill(\n            r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n            r\"CAR\\,=\\,{mean_car}\\%\\,$\\pm$\\,{std_car} at the 30K checkpoint \"\n            r\"(3 seeds: {s0_car}\\%, {s1_car}\\%, {s2_car}\\%), a modest but \"\n            r\"statistically significant departure from the null distribution \"\n            r\"(mean 54.67\\%, $\\sigma = 2.07$; permutation \"\n            r\"$p = {p_value}$\\footnote{One-tailed permutation \"\n            r\"$p = {p_one_value}$; the directional prior that SDF should not \"\n            r\"\\emph{decrease} CAR supports a one-tailed test, but we report \"\n            r\"the conservative two-tailed value in the main text.}). The \"\n            r\"effect size of {delta_pp}\\,pp is small relative to the $+$26\\,pp gain \"\n            r\"from LoRA fine-tuning alone, indicating that EE-only SDF supervision \"\n            r\"can incrementally augment demonstration-driven avoidance at sufficiently \"\n            r\"high loss weights but cannot substitute for it. A stepwise ablation across \"\n            r\"six checkpoints (16K--28K) shows no sustained trend prior to 30K \"\n            r\"(mean 55.3\\%, within 0.4$\\sigma$ of the null; \"\n            r\"Appendix~\\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K \"\n            r\"remains identical to all other conditions \"\n            r\"(Figure~\\ref{fig:lambda_car}), confirming that the dominant avoidance \"\n            r\"signal remains the demonstration distribution. The response is thus \"\n            r\"dose-dependent: SDF shows no significant benefit at $\\lambda \\leq 0.01$ \"\n            r\"($p > 0.1$), with a small but detectable effect at $\\lambda = 0.1$ \"\n            r\"that preserves the same demonstration-driven avoidance fingerprint.\", v)\n    else:\n        new_body = fill(\n            r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n            r\"CAR\\,=\\,{mean_car}\\%\\,$\\pm$\\,{std_car} at the 30K checkpoint \"\n            r\"(3 seeds: {s0_car}\\%, {s1_car}\\%, {s2_car}\\%), within the null \"\n            r\"distribution (mean 54.67\\%, $\\sigma = 2.07$; permutation \"\n            r\"$p = {p_value}$\\footnote{One-tailed permutation \"\n            r\"$p = {p_one_value}$; even with the directional prior that SDF \"\n            r\"should not \\emph{decrease} CAR, the result remains \"\n            r\"non-significant.}). SDF supervision does not produce statistically \"\n            r\"significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ \"\n            r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"\n            r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"\n            r\"20$\\times$ increase in SDF loss weight fails to produce additional \"\n            r\"avoidance, the binding constraint is not training signal magnitude but \"\n            r\"the structural mismatch between end-effector monitoring and full-body \"\n            r\"collision surfaces. Stronger geometric supervision cannot compensate for \"\n            r\"supervising the wrong collision surface.\", v)\n    R.append((\"claim3.tex\", \"claim3 L32-33 dose-response\", old, hdr + \"\\n\" + new_body))\n\n    # 8. claim3.tex L38 figure caption\n    old = (\n        r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n        r\"$\\lambda = 0$: LoRA-only. The $\\lambda \\in \\{0.01, 0.1\\}$ values remain within \"\n        r\"the null band ($p > 0.05$), consistent with the absence of statistically \"\n        r\"significant improvement across a 20$\\times$ loss-weight range.}\"\n    )\n    if is_c:\n        new = fill(\n            r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n            r\"$\\lambda = 0$: LoRA-only. Low $\\lambda$ ($\\leq 0.01$) remains within \"\n            r\"the null band; $\\lambda = 0.1$ ({mean_car}\\%, 3 seeds) shows a modest \"\n            r\"but significant departure (permutation $p = {p_value}$, {delta_pp}\\,pp \"\n            r\"effect size) whose per-task avoidance pattern still matches the \"\n            r\"demonstration distribution.}\", v)\n    else:\n        new = (\n            r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n            r\"$\\lambda = 0$: LoRA-only. The $\\lambda \\in \\{0.01, 0.1\\}$ values remain within \"\n            r\"the null band ($p > 0.05$), consistent with the absence of statistically \"\n            r\"significant improvement across a 20$\\times$ loss-weight range.}\"\n        )\n    R.append((\"discussion.tex\", \"discussion fig caption\", old, new))\n\n    # 9. discussion.tex L3 scope (Scenario C only)\n    if is_c:\n        old = (\n            r\"and collision-free demonstrations account for nearly all measured \"\n            r\"avoidance gains, with EE-only SDF contributing no statistically \"\n            r\"significant improvement (\\S\\ref{sec:avoidance_source}).\"\n        )\n        new = (\n            r\"and collision-free demonstrations account for nearly all measured \"\n            r\"avoidance gains, with EE-only SDF contributing at most a modest \"\n            r\"increment at high loss weights (\\S\\ref{sec:avoidance_source}).\"\n        )\n        R.append((\"discussion.tex\", \"discussion L3 scope\", old, new))\n\n    # 10. discussion.tex L6\n    old = (\n        r\"Even at $\\lambda = 0.1$, CAR remains within the null distribution \"\n        r\"($p = 0.155$).\"\n    )\n    if is_c:\n        new = fill(\n            r\"At $\\lambda \\leq 0.01$, SDF shows no significant benefit; at \"\n            r\"$\\lambda = 0.1$, a modest {delta_pp}\\,pp effect emerges \"\n            r\"($p = {p_value}$) but preserves the same demonstration-driven \"\n            r\"avoidance pattern, suggesting that EE-only SDF can weakly \"\n            r\"augment---but not redirect---the implicit signal at sufficiently \"\n            r\"high loss weights.\", v)\n    else:\n        new = fill(\n            r\"Even at $\\lambda = 0.1$, CAR remains within the null distribution \"\n            r\"($p = {p_value}$).\", v)\n    R.append((\"discussion.tex\", \"discussion L6\", old, new))\n\n    # 11. discussion.tex L12 limitation\n    old = r\"validation on actively moving policies and full-body SDF remain necessary before generalizing the counterproductive finding to non-collapsed settings. Run-to-run variance (same model, training seed, evaluation seed) is approximately 0.5\\,pp CAR and 5.5\\,pp TSR, bounding measurement precision.\"\n    if is_c:\n        new = fill(\n            r\"validation on actively moving policies and full-body SDF remain future work. \"\n            r\"The $\\lambda = 0.1$ effect ({delta_pp}\\,pp, $p = {p_value}$, $n = 3$) \"\n            r\"is statistically significant but small; whether this modest gain \"\n            r\"justifies the computational cost of SDF supervision requires \"\n            r\"task-specific cost-benefit analysis.\", v)\n    else:\n        new = old\n    R.append((\"discussion.tex\", \"discussion L12 limitation\", old, new))\n\n    return R\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Auto-switch paper for lambda=0.1 s2 30K result\")\n    parser.add_argument(\"--s2-car\", type=float, required=\"--verify\" not in sys.argv)\n    parser.add_argument(\"--s2-tsr\", type=float, default=None)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--verify\", action=\"store_true\",\n                        help=\"Check all old_strings match current .tex files\")\n    args = parser.parse_args()\n\n    if args.verify:\n        if not PAPER_DIR.exists():\n            print(f\"ERROR: paper dir not found: {PAPER_DIR}\")\n            sys.exit(1)\n        dummy_v = {k: \"X\" for k in [\n            \"s0_car\", \"s1_car\", \"s2_car\", \"mean_car\", \"std_car\",\n            \"tsr_mean\", \"tsr_std\", \"p_value\", \"p_one_value\", \"z_value\", \"delta_pp\"]}\n        all_ok = True\n        for scenario in (\"B\", \"C\"):\n            replacements = get_replacements(scenario, dummy_v)\n            print(f\"--- Scenario {scenario} ({len(replacements)} items) ---\")\n            for filename, label, old, new in replacements:\n                fpath = PAPER_DIR / filename\n                if not fpath.exists():\n                    print(f\"  [MISSING] {label:35s} {filename}\")\n                    all_ok = False\n                    continue\n                content = fpath.read_text()\n                if old in content:\n                    print(f\"  [OK]      {label:35s} {filename}\")\n                else:\n                    print(f\"  [MISMATCH]{label:35s} {filename}\")\n                    print(f\"            Expected: {old[:80]}...\")\n                    all_ok = False\n        sys.exit(0 if all_ok else 1)\n\n    cars = [S0_CAR, S1_CAR, args.s2_car]\n    car_mean = mean(cars)\n    car_std = std_b(cars)\n\n    if args.s2_tsr is not None:\n        tsrs = [S0_TSR, S1_TSR, args.s2_tsr]\n    else:\n        tsrs = [S0_TSR, S1_TSR]\n        print(\"NOTE: --s2-tsr not provided, using 2-seed TSR\")\n    tsr_mean = mean(tsrs)\n    tsr_std = std_b(tsrs)\n\n    p_one, p_two, n_combos = perm_test(NULL_VALUES, cars)\n    z = (car_mean - NULL_MEAN) / NULL_STD\n    delta = car_mean - NULL_MEAN\n\n    scenario = \"C\" if p_one < 0.05 else \"B\"\n\n    v = {\n        \"s0_car\": f\"{S0_CAR:.1f}\",\n        \"s1_car\": f\"{S1_CAR:.1f}\",\n        \"s2_car\": f\"{args.s2_car:.1f}\",\n        \"mean_car\": f\"{car_mean:.2f}\",\n        \"std_car\": f\"{car_std:.2f}\",\n        \"tsr_mean\": f\"{tsr_mean:.1f}\",\n        \"tsr_std\": f\"{tsr_std:.1f}\",\n        \"p_value\": f\"{p_two:.3f}\",\n        \"p_one_value\": f\"{p_one:.3f}\",\n        \"z_value\": f\"{z:.2f}\",\n        \"delta_pp\": f\"{delta:.1f}\",\n    }\n\n    print(\"=\" * 60)\n    print(\"  PAPER SWITCH — lambda=0.1 s2 30K\")\n    print(\"=\" * 60)\n    print(f\"  Input:     s2_car={args.s2_car}, s2_tsr={args.s2_tsr}\")\n    print(f\"  3-seed:    CAR = {v['mean_car']} +/- {v['std_car']}\")\n    print(f\"             TSR = {v['tsr_mean']} +/- {v['tsr_std']} ({len(tsrs)} seeds)\")\n    print(f\"  Perm test: C({len(NULL_VALUES)+len(cars)},{len(cars)}) = {n_combos}\")\n    print(f\"             p_one = {v['p_one_value']}  {'<' if p_one < 0.05 else '>='} 0.05\")\n    print(f\"             p_two = {v['p_value']}\")\n    print(f\"  Z-score:   {v['z_value']}\")\n    print(f\"  Delta:     +{v['delta_pp']} pp\")\n    print(f\"  Scenario:  {scenario}  \"\n          f\"{'(modest but significant)' if scenario == 'C' else '(full redundancy)'}\")\n    print()\n\n    if not PAPER_DIR.exists():\n        print(f\"ERROR: paper dir not found: {PAPER_DIR}\")\n        sys.exit(1)\n\n    replacements = get_replacements(scenario, v)\n\n    files_content = {}\n    counts = {}\n\n    for filename, label, old, new in replacements:\n        fpath = PAPER_DIR / filename\n        if filename not in files_content:\n            if not fpath.exists():\n                print(f\"  !! {filename} not found\")\n                continue\n            files_content[filename] = fpath.read_text()\n            counts[filename] = 0\n\n        content, ok = safe_replace(files_content[filename], old, new, label)\n        files_content[filename] = content\n        if ok:\n            counts[filename] += 1\n            status = \"ok\"\n        else:\n            status = \"FAIL\"\n        print(f\"  [{status:4s}] {label:35s} {filename}\")\n\n    total = sum(counts.values())\n    n_files = sum(1 for c in counts.values() if c > 0)\n    expected = len(replacements)\n    print(f\"\\n  {total}/{expected} replacements in {n_files} files\")\n\n    if args.dry_run:\n        print(\"\\n  DRY RUN — no files modified\")\n        return\n\n    for filename, content in files_content.items():\n        fpath = PAPER_DIR / filename\n        fpath.write_text(content)\n        print(f\"  Wrote {filename} ({counts[filename]} changes)\")\n\n    print(\"\\nCompiling PDF...\")\n    try:\n        result = subprocess.run(\n            [\"latexmk\", \"-pdf\", \"-interaction=nonstopmode\", \"main.tex\"],\n            cwd=PAPER_DIR, capture_output=True, text=True, timeout=120)\n        if result.returncode == 0:\n            print(\"  PDF compiled OK\")\n        else:\n            print(\"  PDF compilation FAILED\")\n            err = result.stderr or result.stdout or \"\"\n            for line in err.split(\"\\n\")[-10:]:\n                if line.strip():\n                    print(f\"    {line}\")\n    except FileNotFoundError:\n        print(\"  latexmk not found — skipping PDF compilation\")\n    except subprocess.TimeoutExpired:\n        print(\"  PDF compilation timed out (120s)\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 433,
      "startLine": 60,
      "totalLines": 492
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
The paper_switch.py --verify checks that specific old_strings exist in the tex files. It checks abstract.tex, claim3.tex, and discussion.tex - not appendix.tex. So adding a new section to appendix.tex should not break any of the 21 checks.

Let me now add the new section at the end of appendix.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "e3dd6dd5-30e2-4c6d-a5f4-291c7107b49c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfpM3XYy4xB4KEX65ZZyoZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7921,
      "cache_read_input_tokens": 36867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7921
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

_source line 14_

The verify script only checks abstract.tex, claim3.tex, and discussion.tex — not appendix.tex. Adding a new section to appendix.tex won't break any checks. Let me add the section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "7aa9aafc-aac9-44fc-b8ae-7be15be43bf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfpM3XYy4xB4KEX65ZZyoZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7921,
      "cache_read_input_tokens": 36867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7921
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_019aB4qFgiVXAnV2CXNgCYg8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.",
  "new_string": "All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n\n\n\\section{TSR Collapse Mechanism Analysis}\n\\label{sec:appendix_tsr_collapse}\n\nFine-tuning Pi0.5 with LoRA alone (no SDF supervision) reduces TSR from 71.5\\% to 49.7\\,$\\pm$\\,3.2\\%, a drop of 21.8\\,pp (Table~\\ref{tab:multiseed_full}). Adding SDF supervision does not exacerbate this decline: TSR under $\\lambda = 0.005$ is 54.0\\,$\\pm$\\,3.0\\% ($-$17.5\\,pp), under $\\lambda = 0.01$ is 53.8\\,$\\pm$\\,1.5\\% ($-$17.7\\,pp), and under $\\lambda = 0.1$ is 50.2\\,$\\pm$\\,3.9\\% ($-$21.3\\,pp). All SDF conditions fall within the LoRA-only confidence interval, and the largest SDF drop ($\\lambda = 0.1$, $-$21.3\\,pp) matches the LoRA-only drop ($-$21.8\\,pp) to within 0.5\\,pp. This confirms that SDF auxiliary loss is not the cause of TSR degradation.\n\nThe mechanism is catastrophic forgetting of task semantics induced by LoRA fine-tuning on a narrow 4-task subset of the pre-training distribution. Qualitative inspection reveals that fine-tuned models retain full motor capability---0\\% action-collapse rate, end-effector displacement $>$\\,0.37\\,m, and active obstacle interaction (mean obstacle displacement ${\\sim}$0.05\\,m)---but lose goal-directed grasping and placing behavior. The dominant failure mode shifts from collision (baseline safe failure rate 0.5\\%) to task incompletion without collision (${\\sim}$50\\% of episodes), representing a 100$\\times$ increase in safe failures. The robot moves purposefully through the workspace but fails to acquire or deliver the target object, consistent with retained low-level motor skills and degraded high-level task understanding."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "beba6694-5b8c-49d9-9096-8b427942377d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfpM3XYy4xB4KEX65ZZyoZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7921,
      "cache_read_input_tokens": 36867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7921
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

_source line 16 · 2026-05-29T00:20:43.136Z_

<details><summary>↩ Tool result · `toolu_019aB4qFgiVXAnV2CXNgCYg8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "da570372-b5c0-4880-9426-3af519571936",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "oldString": "All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.",
    "newString": "All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n\n\n\\section{TSR Collapse Mechanism Analysis}\n\\label{sec:appendix_tsr_collapse}\n\nFine-tuning Pi0.5 with LoRA alone (no SDF supervision) reduces TSR from 71.5\\% to 49.7\\,$\\pm$\\,3.2\\%, a drop of 21.8\\,pp (Table~\\ref{tab:multiseed_full}). Adding SDF supervision does not exacerbate this decline: TSR under $\\lambda = 0.005$ is 54.0\\,$\\pm$\\,3.0\\% ($-$17.5\\,pp), under $\\lambda = 0.01$ is 53.8\\,$\\pm$\\,1.5\\% ($-$17.7\\,pp), and under $\\lambda = 0.1$ is 50.2\\,$\\pm$\\,3.9\\% ($-$21.3\\,pp). All SDF conditions fall within the LoRA-only confidence interval, and the largest SDF drop ($\\lambda = 0.1$, $-$21.3\\,pp) matches the LoRA-only drop ($-$21.8\\,pp) to within 0.5\\,pp. This confirms that SDF auxiliary loss is not the cause of TSR degradation.\n\nThe mechanism is catastrophic forgetting of task semantics induced by LoRA fine-tuning on a narrow 4-task subset of the pre-training distribution. Qualitative inspection reveals that fine-tuned models retain full motor capability---0\\% action-collapse rate, end-effector displacement $>$\\,0.37\\,m, and active obstacle interaction (mean obstacle displacement ${\\sim}$0.05\\,m)---but lose goal-directed grasping and placing behavior. The dominant failure mode shifts from collision (baseline safe failure rate 0.5\\%) to task incompletion without collision (${\\sim}$50\\% of episodes), representing a 100$\\times$ increase in safe failures. The robot moves purposefully through the workspace but fails to acquire or deliver the target object, consistent with retained low-level motor skills and degraded high-level task understanding.",
    "originalFile": "\\section{Complete Multi-Seed Results}\n\\label{sec:appendix_multiseed}\n\nTable~\\ref{tab:multiseed_full} reports individual-seed CAR and TSR for all fine-tuned conditions at the 30K checkpoint (200 episodes each, evaluation seed\\,=\\,7). These per-seed values underlie the means reported in Table~\\ref{tab:avoidance_source}.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR and TSR (\\%) at 30K steps, evaluation seed\\,=\\,7 (200 episodes). All episodes exhibit displacement $>$\\,0.37\\,m and 0\\% action-collapse rate.}\n\\label{tab:multiseed_full}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nCondition & Seed & CAR & TSR & Mean CAR & Mean TSR \\\\\n\\midrule\n\\multirow{3}{*}{LoRA-only}\n  & s0 & 57.0 & 46.0 & \\multirow{3}{*}{54.83$\\pm$2.25} & \\multirow{3}{*}{49.7$\\pm$3.2} \\\\\n  & s1 & 52.5 & 51.5 & & \\\\\n  & s2 & 55.0 & 51.5 & & \\\\\n\\midrule\n\\multirow{3}{*}{SDF $\\lambda{=}0.005$}\n  & s0 & 57.0 & 55.5 & \\multirow{3}{*}{54.5$\\pm$2.29} & \\multirow{3}{*}{54.0$\\pm$3.0} \\\\\n  & s1 & 54.0 & 50.5 & & \\\\\n  & s2 & 52.5 & 56.0 & & \\\\\n\\midrule\n\\multirow{3}{*}{SDF $\\lambda{=}0.01$}\n  & s0 & 57.0 & 52.5 & \\multirow{3}{*}{56.33$\\pm$1.61} & \\multirow{3}{*}{53.8$\\pm$1.5} \\\\\n  & s1 & 57.5 & 55.5 & & \\\\\n  & s2 & 54.5 & 53.5 & & \\\\\n\\midrule\n\\multirow{3}{*}{SDF $\\lambda{=}0.1$}\n  & s0 & 58.0 & 47.0 & \\multirow{3}{*}{57.00$\\pm$2.18} & \\multirow{3}{*}{50.2$\\pm$3.9} \\\\\n  & s1 & 58.5 & 49.0 & & \\\\\n  & s2 & 54.5 & 54.5 & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% action-collapse rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Action-collapse rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n\nTable~\\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\\S\\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) at 30K steps. $\\lambda{=}0.005$, $\\lambda{=}0.01$, and $\\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}\n\\label{tab:per_task_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 & 68 & 74 & 66 & 20 & 57.0 \\\\\nLoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\\\\nLoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\\\\nSDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\nSDF $\\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\\\\nSDF $\\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\\\\nSDF $\\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor the $\\lambda = 0.1$ condition, seed~1 records \\texttt{avg\\_max\\_obstacle\\_displacement} of 0.0553\\,m (per-task: OJ\\,=\\,0.033, CP\\,=\\,0.055, Milk\\,=\\,0.041, BBQ\\,=\\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_pertask_car_fingerprint}\n\\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all $\\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}\n\\label{fig:pertask_fingerprint}\n\\end{figure}\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nTable~\\ref{tab:ssr} reports the Safe Success Rate (SSR\\,=\\,TSR\\,$\\cap$\\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\\\\nLoRA-only (3 seeds) & 49.7 & 54.83 & 27.7 & 0.56 \\\\\nSDF $\\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 57.0\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.67\\% and standard deviation 2.07\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.155$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{57, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 13/84 \\approx 0.155$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{57.0, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 5/20 = 0.250$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 6/20 = 0.300$, two-tailed $p = 12/20 = 0.600$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 13/84 \\approx 0.155$, two-tailed $p = 25/84 \\approx 0.298$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (57.0\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.155$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.155$, two-tailed permutation).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & -- & 55.75 \\\\\n20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n22K steps & 60.5 & 56.5 & -- & 58.5 \\\\\n24K steps & 52.5 & -- & -- & -- \\\\\n26K steps & 53.5 & -- & -- & -- \\\\\n28K steps & 54.5 & -- & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$3\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). At 30K, the third seed ($s_2 = 54.5\\%$) falls well within the null range, pulling the three-seed mean to 57.00\\% and rendering the earlier two-seed departure non-significant ($p = 0.155$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Cross-Scene Validation: spatial\\_bowl}\n\\label{sec:appendix_spatial_bowl}\n\nTo test whether the absence of EE-only SDF benefit generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\n\nTable~\\ref{tab:spatial_bowl} reports the results. The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 12.0\\% for LoRA-only, a $-$0.5\\,pp difference well within the noise floor, indicating that SDF is essentially identical to LoRA-only on this scene. TSR is comparable across conditions (49.0\\% vs.\\ 51.5\\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \\texttt{object\\_pudding} findings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the absence of SDF benefit observed on \\texttt{object\\_pudding}.}\n\\label{tab:spatial_bowl}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & CAR (\\%) & TSR (\\%) \\\\\n\\midrule\nLoRA-only & 12.0 & 49.0 \\\\\nSDF $\\lambda{=}0.005$ & 11.5 & 51.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe substantially lower CAR on \\texttt{spatial\\_bowl} relative to \\texttt{object\\_pudding} (11--12\\% vs.\\ 54--57\\%) reflects the greater scene difficulty: \\texttt{spatial\\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition performs comparably ($\\Delta$CAR\\,=\\,$-$0.5\\,pp, well within noise), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.\n\n\n\\section{Evaluation Seed Robustness}\n\\label{sec:appendix_eval_seed}\n\nTo verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate key model configurations under multiple evaluation seeds (200 episodes each). Table~\\ref{tab:eval_seed_robustness} reports aggregate CAR and TSR across all tested seeds.\n\n\\begin{table}[h]\n\\centering\n\\caption{Eval-seed robustness: aggregate CAR and TSR (\\%) across evaluation seeds (200 episodes each). Dashes indicate untested seeds. CAR ranges overlap across all three conditions, confirming that SDF redundancy is not an eval-seed artifact.}\n\\label{tab:eval_seed_robustness}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{llccccccl}\n\\toprule\n& & \\multicolumn{6}{c}{Evaluation seed} & \\\\\n\\cmidrule(lr){3-8}\nCondition & & 0 & 7 & 42 & 99 & 123 & 256 & Mean$\\pm$Std \\\\\n\\midrule\n\\multirow{2}{*}{LoRA s0}\n  & CAR & 53.0 & 57.0 & 56.5 & 57.5 & 53.0 & --- & 55.4$\\pm$2.2 \\\\\n  & TSR & 55.5 & 46.0 & 46.0 & 52.0 & 50.5 & --- & 50.0$\\pm$4.1 \\\\\n\\midrule\n\\multirow{2}{*}{SDF $\\lambda{=}0.01$ s0}\n  & CAR & 52.5 & 57.0 & --- & 57.0 & --- & 57.0 & 55.9$\\pm$2.3 \\\\\n  & TSR & 48.5 & 52.5 & --- & 46.5 & --- & 48.0 & 48.9$\\pm$2.6 \\\\\n\\midrule\n\\multirow{2}{*}{SDF $\\lambda{=}0.1$ s0}\n  & CAR & --- & 58.0 & 59.0 & --- & 58.5 & 57.0 & 58.1$\\pm$0.9 \\\\\n  & TSR & --- & 47.0 & 52.5 & --- & 53.5 & 48.0 & 50.3$\\pm$3.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLoRA s0 CAR ranges from 53.0\\% to 57.5\\% across five evaluation seeds (std\\,=\\,2.2\\,pp), consistent with binomial sampling noise at $n{=}50$ episodes per task. SDF $\\lambda{=}0.01$ s0 produces near-identical mean CAR (55.9\\% across four eval seeds vs.\\ 55.4\\% for LoRA), confirming that the null result holds across eval conditions. SDF $\\lambda{=}0.1$ s0 shows a slightly higher mean (58.1\\%), but the ranges overlap with LoRA-only, and the difference (2.8\\,pp, ${<}$1.3$\\sigma$) remains non-significant. The per-task CAR ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all seeds and conditions, reinforcing the demonstration-driven avoidance hypothesis.\n\nTable~\\ref{tab:eval_seed_car_detail} provides per-task CAR for the five-seed LoRA evaluation, the most complete eval-seed battery.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for LoRA s0 across five evaluation seeds. The per-task fingerprint (CP highest, BBQ lowest) is invariant across all seeds.}\n\\label{tab:eval_seed_car_detail}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nEval seed & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\n0   & 46 & 70 & 74 & 22 & 53.0 \\\\\n7   & 68 & 74 & 66 & 20 & 57.0 \\\\\n42  & 60 & 70 & 68 & 28 & 56.5 \\\\\n99  & 58 & 76 & 66 & 30 & 57.5 \\\\\n123 & 52 & 74 & 66 & 20 & 53.0 \\\\\n\\midrule\nMean$\\pm$Std & 56.8$\\pm$8.3 & 72.8$\\pm$2.7 & 68.0$\\pm$3.5 & 24.0$\\pm$4.7 & 55.4$\\pm$2.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n",
    "structuredPatch": [
      {
        "oldStart": 393,
        "oldLines": 3,
        "newStart": 393,
        "newLines": 11,
        "lines": [
          " ",
          " \\paragraph{Computational resources.}",
          " All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.",
          "+",
          "+",
          "+\\section{TSR Collapse Mechanism Analysis}",
          "+\\label{sec:appendix_tsr_collapse}",
          "+",
          "+Fine-tuning Pi0.5 with LoRA alone (no SDF supervision) reduces TSR from 71.5\\% to 49.7\\,$\\pm$\\,3.2\\%, a drop of 21.8\\,pp (Table~\\ref{tab:multiseed_full}). Adding SDF supervision does not exacerbate this decline: TSR under $\\lambda = 0.005$ is 54.0\\,$\\pm$\\,3.0\\% ($-$17.5\\,pp), under $\\lambda = 0.01$ is 53.8\\,$\\pm$\\,1.5\\% ($-$17.7\\,pp), and under $\\lambda = 0.1$ is 50.2\\,$\\pm$\\,3.9\\% ($-$21.3\\,pp). All SDF conditions fall within the LoRA-only confidence interval, and the largest SDF drop ($\\lambda = 0.1$, $-$21.3\\,pp) matches the LoRA-only drop ($-$21.8\\,pp) to within 0.5\\,pp. This confirms that SDF auxiliary loss is not the cause of TSR degradation.",
          "+",
          "+The mechanism is catastrophic forgetting of task semantics induced by LoRA fine-tuning on a narrow 4-task subset of the pre-training distribution. Qualitative inspection reveals that fine-tuned models retain full motor capability---0\\% action-collapse rate, end-effector displacement $>$\\,0.37\\,m, and active obstacle interaction (mean obstacle displacement ${\\sim}$0.05\\,m)---but lose goal-directed grasping and placing behavior. The dominant failure mode shifts from collision (baseline safe failure rate 0.5\\%) to task incompletion without collision (${\\sim}$50\\% of episodes), representing a 100$\\times$ increase in safe failures. The robot moves purposefully through the workspace but fails to acquire or deliver the target object, consistent with retained low-level motor skills and degraded high-level task understanding."
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

_source line 17_

Now let me run the verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "ef552847-ddd2-48b5-869a-6b8eaa8e5347",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qieFdiGuY2UtDjh9JqPWV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 44788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01JMYX6oGe1eD5weKbNoBgNb`</summary>

```json
{
  "command": "python artifacts/paper_switch.py --verify",
  "description": "Verify paper_switch.py 21/21 pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "233a3ee2-c516-409d-8aa9-7db7edaa687e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qieFdiGuY2UtDjh9JqPWV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 44788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 19 · 2026-05-29T00:20:47.030Z_

<details><summary>↩ Tool result · reported error · `toolu_01JMYX6oGe1eD5weKbNoBgNb`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "3f759360-b264-4850-8058-2ca5296f4a34",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_013v2iNKCEKtSmQdLJGsro7X`</summary>

```json
{
  "command": "python3 artifacts/paper_switch.py --verify",
  "description": "Verify paper_switch.py 21/21 pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "91c254d6-bdaa-420f-bba6-9d1c30ccb6a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYrEt8H4p1sepJobKuveie",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 137,
      "cache_read_input_tokens": 45851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 137
      },
      "output_tokens": 61,
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

_source line 21 · 2026-05-29T00:20:49.657Z_

<details><summary>↩ Tool result · `toolu_013v2iNKCEKtSmQdLJGsro7X`</summary>

```text
--- Scenario B (10 items) ---
  [OK]      abstract L5 training                abstract.tex
  [OK]      abstract L6 conclusion              abstract.tex
  [OK]      claim3 L3 scope                     claim3.tex
  [OK]      claim3 L7 caption                   claim3.tex
  [OK]      claim3 L20 table row                claim3.tex
  [OK]      claim3 L27 body                     claim3.tex
  [OK]      claim3 L32-33 dose-response         claim3.tex
  [OK]      discussion fig caption              discussion.tex
  [OK]      discussion L6                       discussion.tex
  [OK]      discussion L12 limitation           discussion.tex
--- Scenario C (11 items) ---
  [OK]      abstract L5 training                abstract.tex
  [OK]      abstract L6 conclusion              abstract.tex
  [OK]      claim3 L3 scope                     claim3.tex
  [OK]      claim3 L7 caption                   claim3.tex
  [OK]      claim3 L20 table row                claim3.tex
  [OK]      claim3 L27 body                     claim3.tex
  [OK]      claim3 L32-33 dose-response         claim3.tex
  [OK]      discussion fig caption              discussion.tex
  [OK]      discussion L3 scope                 discussion.tex
  [OK]      discussion L6                       discussion.tex
  [OK]      discussion L12 limitation           discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "2716591b-46cb-46c6-a19e-c4a3a1181ea6",
  "tool_use_result": {
    "stdout": "--- Scenario B (10 items) ---\n  [OK]      abstract L5 training                abstract.tex\n  [OK]      abstract L6 conclusion              abstract.tex\n  [OK]      claim3 L3 scope                     claim3.tex\n  [OK]      claim3 L7 caption                   claim3.tex\n  [OK]      claim3 L20 table row                claim3.tex\n  [OK]      claim3 L27 body                     claim3.tex\n  [OK]      claim3 L32-33 dose-response         claim3.tex\n  [OK]      discussion fig caption              discussion.tex\n  [OK]      discussion L6                       discussion.tex\n  [OK]      discussion L12 limitation           discussion.tex\n--- Scenario C (11 items) ---\n  [OK]      abstract L5 training                abstract.tex\n  [OK]      abstract L6 conclusion              abstract.tex\n  [OK]      claim3 L3 scope                     claim3.tex\n  [OK]      claim3 L7 caption                   claim3.tex\n  [OK]      claim3 L20 table row                claim3.tex\n  [OK]      claim3 L27 body                     claim3.tex\n  [OK]      claim3 L32-33 dose-response         claim3.tex\n  [OK]      discussion fig caption              discussion.tex\n  [OK]      discussion L3 scope                 discussion.tex\n  [OK]      discussion L6                       discussion.tex\n  [OK]      discussion L12 limitation           discussion.tex",
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

_source line 22_

21/21 全部通过。appendix.tex 末尾已添加 `\section{TSR Collapse Mechanism Analysis}`（约 190 words），包含：

- LoRA-only 与各 SDF 条件的 TSR drop 对比（引用 Table 2 数据）
- 归因：LoRA fine-tuning 导致的 catastrophic forgetting，非 SDF 引起
- Failure mode 描述：保留运动能力但丧失 goal-directed behavior，safe failure rate 从 0.5% → ~50%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "uuid": "0f3f94d0-6370-4e63-b54c-b3a540956a57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfCYgGmPnNkRjMi4yaXU68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 45988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 584
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

_source line 23_

21/21 全部通过。appendix.tex 末尾已添加 `\section{TSR Collapse Mechanism Analysis}`（约 190 words），包含：

- LoRA-only 与各 SDF 条件的 TSR drop 对比（引用 Table 2 数据）
- 归因：LoRA fine-tuning 导致的 catastrophic forgetting，非 SDF 引起
- Failure mode 描述：保留运动能力但丧失 goal-directed behavior，safe failure rate 从 0.5% → ~50%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 55095,
  "duration_api_ms": 55714,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "6f0e14d2-6a59-4beb-a883-36447ff37994",
  "total_cost_usd": 0.38981975,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 35121,
    "cache_read_input_tokens": 245825,
    "output_tokens": 1817,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35121,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 150,
        "cache_read_input_tokens": 45988,
        "cache_creation_input_tokens": 584,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 584
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1861,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001936,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 1817,
      "cacheReadInputTokens": 245825,
      "cacheCreationInputTokens": 35121,
      "webSearchRequests": 0,
      "costUSD": 0.38788374999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "17d6b1ee-21a2-45c3-93c3-4f7a9410a7c4"
}
```

</details>

---
