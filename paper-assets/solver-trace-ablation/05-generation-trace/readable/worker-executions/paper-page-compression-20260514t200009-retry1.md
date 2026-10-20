# paper page compression 20260514T200009 retry1

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_paper_page-compression_20260514T200009_retry1.log`
- **Structured JSON:** [`a17ad5c0f260fa8a5bb6.json`](../../sessions/a1/a17ad5c0f260fa8a5bb6.json)

## Before a recorded user message

39 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
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
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__feishu_read_tum_pending_key",
    "mcp__agent-ml-research__feishu_send_alert",
    "mcp__agent-ml-research__feishu_send_approval_card",
    "mcp__agent-ml-research__feishu_send_result_card",
    "mcp__agent-ml-research__feishu_send_tum_key_request_card",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__get_baseline_metrics",
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
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "076915bb-d98b-4a2e-9c83-ba6f801a1528",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778803800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "deea4244-f2ba-4c41-9f74-34d97a1e1ce3",
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "be5036e1-a2f4-4c47-bdf7-6d2e83628487",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018qEfNH5VECxS6m3A1eq5Pz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17521,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17521
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_012xVGCEuVqjbbv51qKPTd8f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "5da36159-a21b-4406-a167-4ff2d3ccbd05",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018qEfNH5VECxS6m3A1eq5Pz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17521,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17521
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

_source line 6 · 2026-05-14T20:00:32.382Z_

<details><summary>↩ Tool result · `toolu_012xVGCEuVqjbbv51qKPTd8f`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\S\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\S\ref{sec:taxonomy}).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	\paragraph{Model and training.}
10	We use Qwen3-4B as the base model, trained with GRPO~\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of FOLIO~\citep{folio} (\texttt{train\_500\_seed42.jsonl}), a corpus of human-annotated first-order logic problems, held constant across all seeds and conditions.
11	
12	\paragraph{Solvers and logic types.}
13	For first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\text{exec}} \in \{0, 1\}$ is binary: 1 if the solver returns a proof, 0 otherwise.
14	
15	\paragraph{Evaluation.}
16	We evaluate on a held-out set of 100 FOLIO examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \texttt{eval\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), proved-only ISR (ISR$^*$, computed over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant. All tabulated ISR values are proved-only unless otherwise noted.
17	
18	\paragraph{Reward formulations.}
19	We compare six conditions:
20	\begin{itemize}[nosep,leftmargin=*]
21	  \item \textbf{Exec-only}: $r = r_{\text{exec}}$ (baseline)
22	  \item \textbf{ISR $\beta$}: $r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR})$, with $\beta \in \{0.1, 0.3\}$
23	  \item \textbf{Random $\beta$}: $r = r_{\text{exec}} \cdot (1 + \beta \cdot u)$, $u \sim \mathcal{U}(0,1)$, matching ISR's range but providing no structural signal
24	  \item \textbf{SFT}: Standard supervised fine-tuning on gold formalizations (no RL)
25	\end{itemize}
26	
27	\paragraph{Output classification.}
28	We classify proved outputs into three categories: \textbf{H7} (single-premise tautology where the sole premise equals the conclusion), \textbf{H1} (multi-premise conclusion embedding where the conclusion appears among the premises), and \textbf{Genuine} (no conclusion duplication detected). Classification uses text matching cross-validated with functional analysis of the LOO necessity distribution ($n_{\text{necessary}}$).
29	
30	\subsection{ISR as Diagnostic}
31	\label{sec:diagnostic}
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=\columnwidth]{figures/fig2_isr_collapse.pdf}
36	\caption{ISR collapse trajectory under exec-only GRPO (seed~42). PR rises from 32\% to 96\% while proved-only ISR falls from 0.642 to 0.003 over 1000 steps. By step~1000, 94.8\% of proved samples have ISR${=}$0. Component count inflates from 6.58 to 18.55, indicating contradiction explosion.}
37	\label{fig:isr-collapse}
38	\end{figure}
39	
40	We first establish that ISR detects structural degeneration invisible to prove rate.
41	Figure~\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).
42	At 100 steps, the model produces structurally sound formalizations: PR${=}$32\%, proved-only ISR${=}$0.642.
43	By 500 steps, PR reaches 93\% but ISR collapses to 0.132---87.1\% of proved samples embed the conclusion among the premises (H1), making proof trivially achievable.
44	At 1000 steps, PR${=}$96\% while ISR drops to 0.003: every proved sample contains the conclusion in its premises (H1${=}$100\%), and the mean component count rises from 6.58 to 18.55.
45	The model generates excessive premises that trivially entail any conclusion via contradiction explosion.
46	The ISR trajectory (0.642 $\to$ 0.132 $\to$ 0.003) is monotonically decreasing with no recovery signal: extended training worsens structural degeneration.
47	
48	\paragraph{Cross-seed instability.}
49	The three exec-only seeds diverge radically, underscoring that single-seed evaluation is unreliable for GRPO-trained formalizers.
50	Seed~42 achieves PR${=}$93\% via conclusion embedding (H1${=}$87.1\%).
51	Seed~43 collapses to PR${=}$14\% with ISR${=}$0.000 through repetition collapse---87\% of outputs hit the maximum token length.
52	Seed~44 reaches PR${=}$98\% but through tautological collapse: the model generates two-component formalizations where the sole premise equals the conclusion (H7${=}$100\%, mean components${=}$2.04).
53	Despite PR values ranging from 14\% to 98\%, all three seeds exhibit structural degeneration detectable by ISR.
54	The cross-seed PR standard deviation ($\pm$47 percentage points) is itself a finding: GRPO exec-only training is highly unstable, and aggregate metrics obscure qualitatively different failure modes.
55	
56	\paragraph{SFT baseline.}
57	To confirm that hacking is RL-specific, we train a supervised baseline on gold formalizations.
58	SFT achieves PR${=}$14\% with proved-only ISR${=}$0.571: 92.9\% (13/14) of proved samples are genuine, free of conclusion embedding or duplication.
59	Only 1 of 14 proved samples exhibits H1 (7.1\%), and no H7 instances occur.
60	The near-absence of hacking confirms that the structural degeneration documented above is a consequence of RL reward optimization, not model capacity or data limitations.
61	
62	\subsection{Meta-Level Goodhart's Law}
63	\label{sec:goodhart}
64	
65	Having established ISR as a diagnostic, we test whether it can serve as a training signal. The answer is negative: ISR-as-reward exhibits \emph{meta-level} Goodhart's Law~\citep{manheim-goodhart-taxonomy}---the diagnostic metric itself becomes the target of gaming when optimized.
66	
67	\begin{table*}[t]
68	\centering
69	\small
70	\setlength{\tabcolsep}{3.5pt}
71	\begin{tabular}{llcccccccl}
72	\toprule
73	\textbf{Condition} & \textbf{Reward} & $\boldsymbol{\beta}$ & $\boldsymbol{n}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} & \textbf{Mode} \\
74	\midrule
75	Base (0-shot) & --- & --- & 1 & 12 & --- & --- & --- & --- & --- \\
76	SFT & supervised & --- & 1 & 14 & 0.571 & 0 & 7 & \textbf{93} & Genuine \\
77	\midrule
78	Exec-only & $r_e$ & --- & 1$^\dagger$ & 93 & 0.132 & 0 & 87 & 13 & H1 embedding \\
79	ISR & $r_e(1{+}\beta{\cdot}\text{ISR})$ & 0.1 & 3 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{65} & 17 & ${\sim}$16 & H7 gaming \\
80	Random & $r_e(1{+}\beta{\cdot}U)$ & 0.1 & 3 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.039} & 0 & 81 & 19 & H1 embedding \\
81	\midrule
82	ISR & $r_e(1{+}\beta{\cdot}\text{ISR})$ & 0.3 & 1 & 18 & 0.143 & --- & --- & --- & PR collapse \\
83	Random & $r_e(1{+}\beta{\cdot}U)$ & 0.3 & 1 & 48 & 0.094 & --- & --- & --- & Redundant \\
84	\bottomrule
85	\end{tabular}
86	\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\pm$std. ISR$^*$: proved-only. $U \sim \mathcal{U}(0,1)$; $r_e = r_{\text{exec}}$. $^\dagger$Seed~42 shown; see \S\ref{sec:diagnostic} for 3-seed divergence. $\ddagger$ISR omitted: inflated by H7 gaming (64.5\% of proved samples are single-premise tautologies); per-seed ISR in Table~\ref{tab:beta01-3seed}. H7/H1/Gen.\% unavailable for $\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\% bolded per group.}
87	\label{tab:goodhart-landscape}
88	\end{table*}
89	
90	\paragraph{Low-dose ISR ($\beta{=}0.1$): ISR-specific gaming.}
91	Table~\ref{tab:goodhart-landscape} summarizes results across conditions. At $\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\% of proved samples (149/231). In contrast, all three random control seeds show \emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.
92	
93	\begin{table}[t]
94	\centering
95	\small
96	\setlength{\tabcolsep}{3pt}
97	\begin{tabular}{llccccc}
98	\toprule
99	\textbf{Seed} & \textbf{Cond.} & \textbf{PR\%} & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} \\
100	\midrule
101	s42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\
102	s43 & ISR & 61 & 0.830 & \textbf{96.7} & 0 & 3.3 \\
103	s44 & ISR & 89 & 0.902 & \textbf{86.5} & 0 & 13.5$^\dagger$ \\
104	\cmidrule{1-7}
105	 & mean$\pm$std & 77$\pm$14 & --- & 64.5 & 17.3 & ${\sim}$16 \\
106	\midrule
107	s42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\
108	s43 & Rand & 88 & 0.058 & 0 & \textbf{93.2} & 6.8 \\
109	s44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\
110	\cmidrule{1-7}
111	 & mean$\pm$std & 85$\pm$6 & 0.086$\pm$.039 & 0 & 81.3$\pm$11 & 18.7$\pm$11 \\
112	\bottomrule
113	\end{tabular}
114	\caption{ISR vs Random at $\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\% vs 0\%). H1 is GRPO-universal, higher under random (81.3\%) than ISR (17.3\%)---ISR converts H1 into H7. $^\dagger$s44's 12 ``genuine'' samples all have $n_{\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\times$.}
115	\label{tab:beta01-3seed}
116	\end{table}
117	
118	Table~\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\% under random reward and 0--51.9\% under ISR. ISR reward does not reduce total hacking---it \emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\% vs Random s42: 70.9\%), and the random control achieves higher and more stable PR (85$\pm$6\% vs 77$\pm$14\%).
119	
120	\paragraph{Premise-count confound.}
121	Seed~42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each is more likely to appear necessary, inflating ISR independent of reasoning quality.
122	
123	To control for this, we compare ISR values only among genuine (non-hacking) samples with $\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$), a ratio of 1.06$\times$---no meaningful structural advantage. Of ISR s42's 26 nominal ``genuine'' samples, 15 have only 1--2 premises, where ISR$\geq$0.5 is a mathematical artifact of LOO on short inputs. The raw 2.4$\times$ ISR difference reduces to noise once premise count is controlled.
124	
125	\paragraph{High-dose ISR ($\beta{=}0.3$): classic Goodhart.}
126	At $\beta{=}0.3$, ISR reward causes PR to collapse to 18\%---a 5.2$\times$ degradation from exec-only. The matched random control achieves PR${=}$48\%, a 2.7$\times$ advantage, demonstrating that ISR at high dose is not merely unhelpful but \emph{actively harmful} relative to a structurally uninformative signal.
127	
128	\paragraph{Dose-response pattern.}
129	Together, the two dose levels reveal a complete Goodhart trajectory~\citep{karwowski-goodhart-rl, gao-reward-overoptimization}: at low dose ($\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.
130	
131	\subsection{Cross-Logic Diagnostic Transfer}
132	\label{sec:crosslogic}
133	
134	To test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.
135	
136	\begin{figure}[t]
137	\centering
138	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
139	\caption{Cross-logic ISR and Prolog STA gaming breakdown. \textbf{(a)}~Exec-only ISR is near-zero in both FOL and Prolog, confirming cross-logic diagnostic transfer. Seed~44 FOL ($\dagger$tautological) and seed~43 FOL ($\ddagger$sampling eval) are annotated. \textbf{(b)}~Prolog STA (ISR-as-reward) produces universal Goodhart: 3/3 seeds converge to gaming via distinct mechanisms---conclusion duplication, degenerate syntax, and query-as-fact---with 0\% genuine proofs.}
140	\label{fig:prolog-comparison}
141	\end{figure}
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\setlength{\tabcolsep}{3pt}
147	\begin{tabular}{llcccc}
148	\toprule
149	\textbf{Logic} & \textbf{Condition} & \textbf{Seed} & \textbf{PR\%} & \textbf{ISR}$^*$ & \textbf{Mode} \\
150	\midrule
151	\multicolumn{6}{l}{\textit{Exec-only (diagnostic transfer)}} \\
152	FOL & Exec & s42 & 93 & 0.132 & H1 embedding \\
153	FOL & Exec & s43$^\dagger$ & 14 & 0.000 & Repetition \\
154	FOL & Exec & s44 & 98 & 0.582$^\ddagger$ & Tautological \\
155	\cmidrule{1-6}
156	Prolog & Exec & s42 & 83 & 0.037 & Ground facts \\
157	Prolog & Exec & s43 & 56 & 0.015 & Degraded \\
158	Prolog & Exec & s44 & 21 & 0.387$^\S$ & Degraded \\
159	\midrule
160	\multicolumn{6}{l}{\textit{ISR-as-reward (Goodhart transfer)}} \\
161	Prolog & STA & s42 & 50 & 1.000$^\|$ & H7 100\% \\
162	Prolog & STA & s43 & 38 & 0.185$^\|$ & Degen.\ syntax$^\P$ \\
163	Prolog & STA & s44 & 97 & 0.912$^\|$ & Query-as-fact$^\#$ \\
164	\bottomrule
165	\end{tabular}
166	\caption{Cross-logic transfer (proved-only ISR$^*$). \textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\% genuine). $^\dagger$Sampling eval ($T{=}0.7$); not strictly comparable with greedy-decoded results. $^\ddagger$2-component artifact. $^\S$Small-sample ($n{=}$21). $^\|$Gaming-inflated. $^\P$Uppercase pseudo-Prolog; $n_{\text{nec}}{=}1$ for 38/38. $^\#$NL$\to$snake\_case atom as fact+query; $n_{\text{nec}}{=}1$ for 95/97.}
167	\label{tab:prolog-crosslogic}
168	\end{table}
169	
170	\paragraph{Diagnostic transfer.}
171	Table~\ref{tab:prolog-crosslogic} (top) and Figure~\ref{fig:prolog-comparison}(a) show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\sigma{=}$47pp) replicates in Prolog ($\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.
172	
173	We note an important semantic distinction: low ISR in Prolog exec-only reflects \emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \emph{metric gaming}. ISR must be interpreted relative to the training objective.
174	
175	\paragraph{Universal Goodhart in Prolog.}
176	Table~\ref{tab:prolog-crosslogic} (bottom) and Figure~\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:
177	\begin{itemize}[nosep,leftmargin=*]
178	  \item \textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).
179	  \item \textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \texttt{MARY\_IS\_AN\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).
180	  \item \textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\_case atoms and sets them as both fact and query, achieving PR${=}$97\% with $n_{\text{necessary}}{=}1$ for 95/97. Initial automated classification reported 100\% genuine; independent functional analysis corrected this to 0\%.
181	\end{itemize}
182	This result is stronger than the FOL finding: FOL ISR $\beta{=}0.1$ retains ${\sim}$16\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics enable more complete exploitation, eliminating the genuine residual observed in FOL.
183	
184	\paragraph{Classifier limitations.}
185	The Prolog results expose a blind spot of text-match hacking classifiers. Seeds~s43 and s44 bypass the strict H7/H1 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\text{necessary}}$ distribution.
186	
187	\subsection{Hacking Taxonomy}
188	\label{sec:taxonomy}
189	
190	\begin{figure}[t]
191	\centering
192	\includegraphics[width=\columnwidth]{figures/fig3_hacking_composition.pdf}
193	\caption{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking prevalence. SFT exhibits near-zero hacking (92.9\% genuine).}
194	\label{fig:hacking-composition}
195	\end{figure}
196	
197	\begin{table}[t]
198	\centering
199	\small
200	\setlength{\tabcolsep}{3pt}
201	\begin{tabular}{p{1.6cm}p{2.0cm}cccc}
202	\toprule
203	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rand} & \textbf{SFT} \\
204	\midrule
205	H1 & Concl.\ among premises & 87 & 17 & 81 & 7 \\
206	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{65} & 0 & 0 \\
207	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
208	Repetition & Output degen. & $\bullet$ & --- & --- & --- \\
209	Contradiction & $n_{\text{comp}}{\uparrow}$, ISR${\to}$0 & $\bullet$ & --- & --- & --- \\
210	C-w/o-util. & Complex, redundant & 0 & 0 & 4 & 0 \\
211	Q-as-fact & Atom = fact+query & --- & --- & --- & --- \\
212	\bottomrule
213	\end{tabular}
214	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed means. Exec: H1${=}$87\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-crosslogic}).}
215	\label{tab:hacking-taxonomy}
216	\end{table}
217	
218	Across all conditions, seeds, and logic types, we identify seven distinct hacking modes (Table~\ref{tab:hacking-taxonomy}, Figure~\ref{fig:hacking-composition}):
219	
220	\begin{enumerate}[nosep,leftmargin=*]
221	  \item \textbf{H1: Conclusion embedding.} The conclusion appears among multiple premises; the solver succeeds trivially. GRPO-universal: 52--93\% of proved samples across all RL reward types.
222	  \item \textbf{H7: Conclusion duplication.} A single premise identical to the conclusion. ISR-specific: 64.5\% under ISR $\beta{=}0.1$ vs 0\% under random.
223	  \item \textbf{Tautological collapse.} Two-component formalizations where premise${=}$conclusion (exec-only s44, 94\% of outputs, mean components${=}$2.04).
224	  \item \textbf{Repetition collapse.} Identical premises repeated until the token limit (exec-only s43, 87\% hit max length).
225	  \item \textbf{Contradiction explosion.} Excessive premises (mean 18.55 components at 1000 steps) that trivially entail any conclusion via embedded contradictions.
226	  \item \textbf{Complexity-without-utility.} Syntactically complex but semantically vacuous premises (random $\beta{=}0.1$, 3.8\%).
227	  \item \textbf{Query-as-fact gaming.} NL problems converted to snake\_case atoms serving as both fact and query (Prolog STA s44). Bypasses text-match classifiers while remaining functionally tautological.
228	\end{enumerate}
229	
230	The reward signal determines hacking \emph{composition} but not \emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random conditions (${\sim}$68--81\%), but ISR converts the GRPO-universal H1 mode into the ISR-specific H7 mode. SFT remains the only condition with near-zero hacking (92.9\% genuine), confirming that hacking is RL-reward-specific. Different reward formulations produce characteristic hacking signatures---a finding that may inform future diagnostic design.
231	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "1a6305b7-0fa9-4ec0-b2f4-b8fdd23d0658",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\\S\\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\\S\\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Model and training.}\nWe use Qwen3-4B as the base model, trained with GRPO~\\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of FOLIO~\\citep{folio} (\\texttt{train\\_500\\_seed42.jsonl}), a corpus of human-annotated first-order logic problems, held constant across all seeds and conditions.\n\n\\paragraph{Solvers and logic types.}\nFor first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\\text{exec}} \\in \\{0, 1\\}$ is binary: 1 if the solver returns a proof, 0 otherwise.\n\n\\paragraph{Evaluation.}\nWe evaluate on a held-out set of 100 FOLIO examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \\texttt{eval\\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), proved-only ISR (ISR$^*$, computed over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant. All tabulated ISR values are proved-only unless otherwise noted.\n\n\\paragraph{Reward formulations.}\nWe compare six conditions:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Exec-only}: $r = r_{\\text{exec}}$ (baseline)\n  \\item \\textbf{ISR $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$, with $\\beta \\in \\{0.1, 0.3\\}$\n  \\item \\textbf{Random $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$, $u \\sim \\mathcal{U}(0,1)$, matching ISR's range but providing no structural signal\n  \\item \\textbf{SFT}: Standard supervised fine-tuning on gold formalizations (no RL)\n\\end{itemize}\n\n\\paragraph{Output classification.}\nWe classify proved outputs into three categories: \\textbf{H7} (single-premise tautology where the sole premise equals the conclusion), \\textbf{H1} (multi-premise conclusion embedding where the conclusion appears among the premises), and \\textbf{Genuine} (no conclusion duplication detected). Classification uses text matching cross-validated with functional analysis of the LOO necessity distribution ($n_{\\text{necessary}}$).\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse trajectory under exec-only GRPO (seed~42). PR rises from 32\\% to 96\\% while proved-only ISR falls from 0.642 to 0.003 over 1000 steps. By step~1000, 94.8\\% of proved samples have ISR${=}$0. Component count inflates from 6.58 to 18.55, indicating contradiction explosion.}\n\\label{fig:isr-collapse}\n\\end{figure}\n\nWe first establish that ISR detects structural degeneration invisible to prove rate.\nFigure~\\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).\nAt 100 steps, the model produces structurally sound formalizations: PR${=}$32\\%, proved-only ISR${=}$0.642.\nBy 500 steps, PR reaches 93\\% but ISR collapses to 0.132---87.1\\% of proved samples embed the conclusion among the premises (H1), making proof trivially achievable.\nAt 1000 steps, PR${=}$96\\% while ISR drops to 0.003: every proved sample contains the conclusion in its premises (H1${=}$100\\%), and the mean component count rises from 6.58 to 18.55.\nThe model generates excessive premises that trivially entail any conclusion via contradiction explosion.\nThe ISR trajectory (0.642 $\\to$ 0.132 $\\to$ 0.003) is monotonically decreasing with no recovery signal: extended training worsens structural degeneration.\n\n\\paragraph{Cross-seed instability.}\nThe three exec-only seeds diverge radically, underscoring that single-seed evaluation is unreliable for GRPO-trained formalizers.\nSeed~42 achieves PR${=}$93\\% via conclusion embedding (H1${=}$87.1\\%).\nSeed~43 collapses to PR${=}$14\\% with ISR${=}$0.000 through repetition collapse---87\\% of outputs hit the maximum token length.\nSeed~44 reaches PR${=}$98\\% but through tautological collapse: the model generates two-component formalizations where the sole premise equals the conclusion (H7${=}$100\\%, mean components${=}$2.04).\nDespite PR values ranging from 14\\% to 98\\%, all three seeds exhibit structural degeneration detectable by ISR.\nThe cross-seed PR standard deviation ($\\pm$47 percentage points) is itself a finding: GRPO exec-only training is highly unstable, and aggregate metrics obscure qualitatively different failure modes.\n\n\\paragraph{SFT baseline.}\nTo confirm that hacking is RL-specific, we train a supervised baseline on gold formalizations.\nSFT achieves PR${=}$14\\% with proved-only ISR${=}$0.571: 92.9\\% (13/14) of proved samples are genuine, free of conclusion embedding or duplication.\nOnly 1 of 14 proved samples exhibits H1 (7.1\\%), and no H7 instances occur.\nThe near-absence of hacking confirms that the structural degeneration documented above is a consequence of RL reward optimization, not model capacity or data limitations.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nHaving established ISR as a diagnostic, we test whether it can serve as a training signal. The answer is negative: ISR-as-reward exhibits \\emph{meta-level} Goodhart's Law~\\citep{manheim-goodhart-taxonomy}---the diagnostic metric itself becomes the target of gaming when optimized.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{llcccccccl}\n\\toprule\n\\textbf{Condition} & \\textbf{Reward} & $\\boldsymbol{\\beta}$ & $\\boldsymbol{n}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Mode} \\\\\n\\midrule\nBase (0-shot) & --- & --- & 1 & 12 & --- & --- & --- & --- & --- \\\\\nSFT & supervised & --- & 1 & 14 & 0.571 & 0 & 7 & \\textbf{93} & Genuine \\\\\n\\midrule\nExec-only & $r_e$ & --- & 1$^\\dagger$ & 93 & 0.132 & 0 & 87 & 13 & H1 embedding \\\\\nISR & $r_e(1{+}\\beta{\\cdot}\\text{ISR})$ & 0.1 & 3 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{65} & 17 & ${\\sim}$16 & H7 gaming \\\\\nRandom & $r_e(1{+}\\beta{\\cdot}U)$ & 0.1 & 3 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.039} & 0 & 81 & 19 & H1 embedding \\\\\n\\midrule\nISR & $r_e(1{+}\\beta{\\cdot}\\text{ISR})$ & 0.3 & 1 & 18 & 0.143 & --- & --- & --- & PR collapse \\\\\nRandom & $r_e(1{+}\\beta{\\cdot}U)$ & 0.3 & 1 & 48 & 0.094 & --- & --- & --- & Redundant \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); per-seed ISR in Table~\\ref{tab:beta01-3seed}. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\ns42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\\ns43 & ISR & 61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\\ns44 & ISR & 89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 77$\\pm$14 & --- & 64.5 & 17.3 & ${\\sim}$16 \\\\\n\\midrule\ns42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\\\\ns43 & Rand & 88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\\ns44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 85$\\pm$6 & 0.086$\\pm$.039 & 0 & 81.3$\\pm$11 & 18.7$\\pm$11 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ISR vs Random at $\\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\\% vs 0\\%). H1 is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%)---ISR converts H1 into H7. $^\\dagger$s44's 12 ``genuine'' samples all have $n_{\\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\\times$.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\nTable~\\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).\n\n\\paragraph{Premise-count confound.}\nSeed~42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each is more likely to appear necessary, inflating ISR independent of reasoning quality.\n\nTo control for this, we compare ISR values only among genuine (non-hacking) samples with $\\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$), a ratio of 1.06$\\times$---no meaningful structural advantage. Of ISR s42's 26 nominal ``genuine'' samples, 15 have only 1--2 premises, where ISR$\\geq$0.5 is a mathematical artifact of LOO on short inputs. The raw 2.4$\\times$ ISR difference reduces to noise once premise count is controlled.\n\n\\paragraph{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR reward causes PR to collapse to 18\\%---a 5.2$\\times$ degradation from exec-only. The matched random control achieves PR${=}$48\\%, a 2.7$\\times$ advantage, demonstrating that ISR at high dose is not merely unhelpful but \\emph{actively harmful} relative to a structurally uninformative signal.\n\n\\paragraph{Dose-response pattern.}\nTogether, the two dose levels reveal a complete Goodhart trajectory~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization}: at low dose ($\\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nTo test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic ISR and Prolog STA gaming breakdown. \\textbf{(a)}~Exec-only ISR is near-zero in both FOL and Prolog, confirming cross-logic diagnostic transfer. Seed~44 FOL ($\\dagger$tautological) and seed~43 FOL ($\\ddagger$sampling eval) are annotated. \\textbf{(b)}~Prolog STA (ISR-as-reward) produces universal Goodhart: 3/3 seeds converge to gaming via distinct mechanisms---conclusion duplication, degenerate syntax, and query-as-fact---with 0\\% genuine proofs.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43$^\\dagger$ & 14 & 0.000 & Repetition \\\\\nFOL & Exec & s44 & 98 & 0.582$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 83 & 0.037 & Ground facts \\\\\nProlog & Exec & s43 & 56 & 0.015 & Degraded \\\\\nProlog & Exec & s44 & 21 & 0.387$^\\S$ & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 50 & 1.000$^\\|$ & H7 100\\% \\\\\nProlog & STA & s43 & 38 & 0.185$^\\|$ & Degen.\\ syntax$^\\P$ \\\\\nProlog & STA & s44 & 97 & 0.912$^\\|$ & Query-as-fact$^\\#$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer (proved-only ISR$^*$). \\textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \\textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\\% genuine). $^\\dagger$Sampling eval ($T{=}0.7$); not strictly comparable with greedy-decoded results. $^\\ddagger$2-component artifact. $^\\S$Small-sample ($n{=}$21). $^\\|$Gaming-inflated. $^\\P$Uppercase pseudo-Prolog; $n_{\\text{nec}}{=}1$ for 38/38. $^\\#$NL$\\to$snake\\_case atom as fact+query; $n_{\\text{nec}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\paragraph{Diagnostic transfer.}\nTable~\\ref{tab:prolog-crosslogic} (top) and Figure~\\ref{fig:prolog-comparison}(a) show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\\sigma{=}$47pp) replicates in Prolog ($\\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.\n\nWe note an important semantic distinction: low ISR in Prolog exec-only reflects \\emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \\emph{metric gaming}. ISR must be interpreted relative to the training objective.\n\n\\paragraph{Universal Goodhart in Prolog.}\nTable~\\ref{tab:prolog-crosslogic} (bottom) and Figure~\\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).\n  \\item \\textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).\n  \\item \\textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\\_case atoms and sets them as both fact and query, achieving PR${=}$97\\% with $n_{\\text{necessary}}{=}1$ for 95/97. Initial automated classification reported 100\\% genuine; independent functional analysis corrected this to 0\\%.\n\\end{itemize}\nThis result is stronger than the FOL finding: FOL ISR $\\beta{=}0.1$ retains ${\\sim}$16\\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics enable more complete exploitation, eliminating the genuine residual observed in FOL.\n\n\\paragraph{Classifier limitations.}\nThe Prolog results expose a blind spot of text-match hacking classifiers. Seeds~s43 and s44 bypass the strict H7/H1 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\\text{necessary}}$ distribution.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking prevalence. SFT exhibits near-zero hacking (92.9\\% genuine).}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{p{1.6cm}p{2.0cm}cccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rand} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ among premises & 87 & 17 & 81 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{65} & 0 & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & --- & --- & --- \\\\\nContradiction & $n_{\\text{comp}}{\\uparrow}$, ISR${\\to}$0 & $\\bullet$ & --- & --- & --- \\\\\nC-w/o-util. & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed means. Exec: H1${=}$87\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nAcross all conditions, seeds, and logic types, we identify seven distinct hacking modes (Table~\\ref{tab:hacking-taxonomy}, Figure~\\ref{fig:hacking-composition}):\n\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{H1: Conclusion embedding.} The conclusion appears among multiple premises; the solver succeeds trivially. GRPO-universal: 52--93\\% of proved samples across all RL reward types.\n  \\item \\textbf{H7: Conclusion duplication.} A single premise identical to the conclusion. ISR-specific: 64.5\\% under ISR $\\beta{=}0.1$ vs 0\\% under random.\n  \\item \\textbf{Tautological collapse.} Two-component formalizations where premise${=}$conclusion (exec-only s44, 94\\% of outputs, mean components${=}$2.04).\n  \\item \\textbf{Repetition collapse.} Identical premises repeated until the token limit (exec-only s43, 87\\% hit max length).\n  \\item \\textbf{Contradiction explosion.} Excessive premises (mean 18.55 components at 1000 steps) that trivially entail any conclusion via embedded contradictions.\n  \\item \\textbf{Complexity-without-utility.} Syntactically complex but semantically vacuous premises (random $\\beta{=}0.1$, 3.8\\%).\n  \\item \\textbf{Query-as-fact gaming.} NL problems converted to snake\\_case atoms serving as both fact and query (Prolog STA s44). Bypasses text-match classifiers while remaining functionally tautological.\n\\end{enumerate}\n\nThe reward signal determines hacking \\emph{composition} but not \\emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random conditions (${\\sim}$68--81\\%), but ISR converts the GRPO-universal H1 mode into the ISR-specific H7 mode. SFT remains the only condition with near-zero hacking (92.9\\% genuine), confirming that hacking is RL-reward-specific. Different reward formulations produce characteristic hacking signatures---a finding that may inform future diagnostic design.\n",
      "numLines": 231,
      "startLine": 1,
      "totalLines": 231
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_019MFr7xyRA8hRwyb89wTeSY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "8809ac2e-b402-43ad-bd48-235ee154472b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QEh8TK9JCaf1xB5aPW9eir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10140,
      "cache_read_input_tokens": 33762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10140
      },
      "output_tokens": 47,
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

_source line 8 · 2026-05-14T20:00:36.406Z_

<details><summary>↩ Tool result · `toolu_019MFr7xyRA8hRwyb89wTeSY`</summary>

```text
1	% Appendix — solver-trace-ablation
2	% Requires: booktabs, amsmath, enumitem packages (loaded in paper.tex)
3	
4	\appendix
5	
6	\section{Experimental Setup}
7	\label{app:setup}
8	
9	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
10	All RL conditions use the same GRPO configuration; only the reward function differs.
11	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
12	
13	\begin{table}[h]
14	\centering
15	\caption{Training hyperparameters for all GRPO experiments.}
16	\label{tab:hyperparams}
17	\begin{tabular}{@{}ll@{}}
18	\toprule
19	\textbf{Parameter} & \textbf{Value} \\
20	\midrule
21	\multicolumn{2}{@{}l}{\textit{Model}} \\
22	Base model & Qwen3-4B \\
23	Precision & BF16 \\
24	\midrule
25	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
26	Rollouts per prompt ($K$) & 8 \\
27	Training steps (default) & 500 \\
28	Training steps (extended) & 1000 \\
29	Learning rate & $1 \times 10^{-6}$ \\
30	Per-device batch size & 4 \\
31	Gradient accumulation steps & 2 \\
32	Effective batch size & 8 \\
33	Max completion length & 512 tokens \\
34	Random seeds & 42, 43, 44 \\
35	\midrule
36	\multicolumn{2}{@{}l}{\textit{Data}} \\
37	Training set & FOLIO, 500 examples \\
38	Evaluation set & FOLIO, 100 examples (held-out) \\
39	Training data file & \texttt{train\_500\_seed42.jsonl} \\
40	\midrule
41	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
42	FOL solver & Prover9 \\
43	Prolog solver & SWI-Prolog 8.4.2 \\
44	\midrule
45	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
46	Decoding strategy & Greedy (temperature = 0) \\
47	ISR computation & \texttt{eval\_sta.py} (unified) \\
48	ISR variant reported & Proved-only ISR (ISR$^*$) \\
49	\midrule
50	\multicolumn{2}{@{}l}{\textit{Reward Conditions (6 total)}} \\
51	Exec-only & $r = r_{\text{exec}}$ \\
52	ISR $\beta{=}0.1$ & $r = r_{\text{exec}} \cdot (1 + 0.1 \cdot \text{ISR})$ \\
53	ISR $\beta{=}0.3$ & $r = r_{\text{exec}} \cdot (1 + 0.3 \cdot \text{ISR})$ \\
54	Random $\beta{=}0.1$ & $r = r_{\text{exec}} \cdot (1 + 0.1 \cdot u),\; u{\sim}\mathcal{U}(0,1)$ \\
55	Random $\beta{=}0.3$ & $r = r_{\text{exec}} \cdot (1 + 0.3 \cdot u)$ \\
56	SFT & Supervised fine-tuning (no RL) \\
57	\bottomrule
58	\end{tabular}
59	\end{table}
60	
61	\paragraph{Evaluation exception.}
62	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$= 0.7$) rather than greedy decoding.
63	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
64	
65	
66	\section{Hacking Mode Definitions}
67	\label{app:hacking-modes}
68	
69	We identify seven distinct reward hacking modes across all experiments.
70	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
71	
72	\subsection{H1 --- Conclusion Embedding}
73	
74	\paragraph{Definition.}
75	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
76	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
77	
78	\paragraph{Example (FOL).}
79	\begin{verbatim}
80	Premises:
81	  all x (bird(x) -> flies(x)).
82	  bird(tweety).
83	  flies(tweety).        % <-- conclusion embedded
84	Conclusion: flies(tweety).
85	\end{verbatim}
86	
87	\paragraph{ISR interaction.}
88	Variable. The embedded premise has ISR~$= 1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
89	ISR does not distinguish trivial from substantive necessity.
90	
91	\paragraph{Prevalence.}
92	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 52--100\% across all RL conditions.
93	Under exec-only and Random reward, it manifests as H1 (52--93\%); under ISR reward, it shifts to H7 (64.5\% mean).
94	
95	
96	\subsection{H7 --- Conclusion Duplication}
97	
98	\paragraph{Definition.}
99	The entire formalization collapses to a single premise whose content is identical to the conclusion.
100	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
101	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
102	
103	\paragraph{Example (FOL).}
104	\begin{verbatim}
105	Premises:
106	  all x ((A(x) & B(x)) -> (C(x) | D(x))).
107	Conclusion:
108	  all x ((A(x) & B(x)) -> (C(x) | D(x))).
109	\end{verbatim}
110	
111	\paragraph{ISR interaction.}
112	ISR~$\approx 0.8$--$1.0$.
113	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
114	H7 is the only mode that simultaneously games both exec reward and ISR reward.
115	
116	\paragraph{Prevalence.}
117	ISR-specific: 3-seed mean = 66.4\% under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
118	\textbf{Zero} occurrences under Random~$\beta{=}0.1$ across all three seeds ($0/256$).
119	
120	
121	\subsection{Tautological Collapse}
122	
123	\paragraph{Definition.}
124	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
125	
126	\paragraph{Example (FOL).}
127	\begin{verbatim}
128	Premises: p(a).
129	Conclusion: p(a).
130	\end{verbatim}
131	
132	\paragraph{ISR interaction.}
133	ISR~$= 1.0$ (the sole premise is necessary).
134	Distinguished from H7 by having low component count ($n_{\text{comp}} \approx 2$) and atomic formulas rather than complex sub-structured conclusions.
135	
136	\paragraph{Prevalence.}
137	Dominant in FOL exec-only seed~44 (PR~$= 0.98$, mean~$n_{\text{comp}} = 2.04$, 100\%~H7 by strict classifier).
138	Also observed in Prolog exec+STA seed~42 (100\%~H7, PR~$= 0.50$).
139	
140	
141	\subsection{Repetition Collapse}
142	
143	\paragraph{Definition.}
144	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
145	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
146	
147	\paragraph{Example (Prolog).}
148	\begin{verbatim}
149	penguin(fido).
150	penguin(fido).
151	penguin(fido).
152	... (repeated to 512 tokens)
153	query(penguin(fido)).
154	\end{verbatim}
155	
156	\paragraph{ISR interaction.}
157	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
158	ISR correctly diagnoses this degeneration.
159	
160	\paragraph{Prevalence.}
161	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$= 14\%$, ISR~$= 0$).
162	
163	
164	\subsection{Complexity-without-Utility}
165	
166	\paragraph{Definition.}
167	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.
168	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
169	
170	\paragraph{Example (FOL).}
171	\begin{verbatim}
172	Premises:
173	  all x all y (R(x,y) -> exists z (S(x,z) & T(z,y))).
174	  all x (P(x) -> Q(x)).
175	  P(a).                   % <-- only this needed
176	Conclusion: Q(a).
177	\end{verbatim}
178	
179	\paragraph{ISR interaction.}
180	ISR correctly identifies the vacuous premises (ISR~$= 0$ for each), pulling down the mean ISR.
181	This is the mode ISR is best calibrated for.
182	
183	\paragraph{Prevalence.}
184	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
185	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
186	
187	
188	\subsection{Contradiction Explosion}
189	
190	\paragraph{Definition.}
191	The component count grows unboundedly over training.
192	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
193	Individual premises may register as ISR~$= 0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
194	
195	\paragraph{Example (FOL, 1000-step exec-only).}
196	\begin{verbatim}
197	Premises:
198	  c1. c2. c3. ... c18.   % 18.55 mean components
199	  % conclusion embedded among premises
200	Conclusion: Q(a).
201	\end{verbatim}
202	
203	\paragraph{ISR interaction.}
204	ISR~$\approx 0$ (at 1000 steps: ISR~$= 0.003$, with 94.8\% of proved samples having ISR~$= 0$).
205	
206	\paragraph{Prevalence.}
207	Observed in extended exec-only training (seed~42, 1000 steps).
208	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
209	
210	
211	\subsection{Query-as-Fact Gaming}
212	
213	\paragraph{Definition.}
214	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
215	Prolog trivially proves the query by unifying with the fact.
216	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
217	
218	\paragraph{Example (Prolog).}
219	\begin{verbatim}
220	% NL: "Fido is happy."
221	% Model output:
222	fido_is_happy.
223	:- fido_is_happy.     % query = fact
224	\end{verbatim}
225	
226	\paragraph{ISR interaction.}
227	ISR~$\approx 0.9$--$1.0$.
228	The fact is necessarily necessary (its removal breaks the query), inflating ISR.
229	Functionally equivalent to H7 but with a distinct surface mechanism.
230	
231	\paragraph{Prevalence.}
232	Observed in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.885$).
233	95/97 proved samples have $n_{\text{necessary}} = 1$, confirming functional tautology despite the strict classifier reporting 100\% genuine.
234	
235	
236	\section{Per-Seed Detailed Results}
237	\label{app:detailed-results}
238	
239	Tables~\ref{tab:fol-detailed} and \ref{tab:prolog-detailed} report full per-seed results for all experiment conditions.
240	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
241	ISR values are proved-only ISR$^*$.
242	
243	\begin{table*}[t]
244	\centering
245	\caption{Detailed per-seed results: FOL (Prover9). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\ = percentage among proved samples.  ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$); 3-seed mean includes this methodological difference.}
246	\label{tab:fol-detailed}
247	\small
248	\begin{tabular}{@{}llccccccl@{}}
249	\toprule
250	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} & \textbf{Notes} \\
251	\midrule
252	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
253	Base model (no training)
254	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
255	Ground-truth FOL
256	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
257	SFT
258	  & 42 & ${\sim}$8 ep. & 0.14 & 0.571 & 0 & 7.1 & \textbf{92.9} & Supervised, no RL \\
259	\midrule
260	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
261	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
262	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 12.9 & \\
263	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
264	  & 43 & 500 & 0.14 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Sampling $T{=}0.7$ \\
265	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
266	\cmidrule(l){2-9}
267	  & \multicolumn{2}{l}{3-seed mean$\pm$std$^\dagger$} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step only \\
268	\midrule
269	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
270	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{30.9} & Mixed H1+H7 \\
271	  & 43 & 500 & 0.61 & 0.830 & \textbf{96.7} & 0 & ${\sim}$3 & H7 dominant \\
272	  & 44 & 500 & 0.89 & 0.902 & 86.5 & 0 & ${\sim}$13.5 & H7 dominant \\
273	\cmidrule(l){2-9}
274	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
275	\midrule
276	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
277	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & Goodhart collapse \\
278	\midrule
279	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
280	  & 42 & 500 & 0.79 & 0.131 & 0 & 70.9 & 29.1 & \\
281	  & 43 & 500 & 0.88 & 0.058 & 0 & 93.2 & 6.8 & \\
282	  & 44 & 500 & 0.89 & 0.070 & 0 & 79.8 & 20.2 & \\
283	\cmidrule(l){2-9}
284	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.85{\pm}0.06$} & & \makebox[0pt][l]{$0.086{\pm}0.039$} & & & H7 = 0\% all seeds \\
285	\midrule
286	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
287	  & 42 & 500 & 0.48 & 0.094 & --- & --- & --- & $n_{\text{comp}} = 9.6$ \\
288	\bottomrule
289	\end{tabular}
290	\end{table*}
291	
292	
293	\begin{table*}[t]
294	\centering
295	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\ = percentage among proved samples.  ``---'' indicates data not available.}
296	\label{tab:prolog-detailed}
297	\small
298	\begin{tabular}{@{}llcccccl@{}}
299	\toprule
300	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} & \textbf{Notes} \\
301	\midrule
302	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
303	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
304	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
305	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
306	\cmidrule(l){2-8}
307	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
308	\midrule
309	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
310	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
311	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
312	  & 44 & 0.97 & 0.885 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
313	\cmidrule(l){2-8}
314	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.690{\pm}0.44$} & & 3/3 Goodhart, 0\% genuine \\
315	\bottomrule
316	\end{tabular}
317	
318	\vspace{4pt}
319	{\footnotesize
320	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}} = 1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
321	$^b$ Strict classifier reports Genuine$\,{=}\,$100\%, but 95/97 proved samples have $n_{\text{necessary}} = 1$. The model converts NL to snake\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\
322	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
323	}
324	\end{table*}
325	
326	
327	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
328	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
329	ISR$^* = 0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4\%$) $\to$ $0.003$ at 1000 steps ($-99.6\%$ from step 100).
330	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
331	By step 1000, 94.8\% of proved samples have ISR~$= 0$ and the mean component count rises to 18.55.
332	
333	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
334	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% genuine proofs, but each discovers a different gaming mechanism:
335	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
336	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
337	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
338	The diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
339	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "6e2b3622-7549-4c11-a988-d86f1b42336f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n% Requires: booktabs, amsmath, enumitem packages (loaded in paper.tex)\n\n\\appendix\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 8 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nTraining data file & \\texttt{train\\_500\\_seed42.jsonl} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding strategy & Greedy (temperature = 0) \\\\\nISR computation & \\texttt{eval\\_sta.py} (unified) \\\\\nISR variant reported & Proved-only ISR (ISR$^*$) \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Reward Conditions (6 total)}} \\\\\nExec-only & $r = r_{\\text{exec}}$ \\\\\nISR $\\beta{=}0.1$ & $r = r_{\\text{exec}} \\cdot (1 + 0.1 \\cdot \\text{ISR})$ \\\\\nISR $\\beta{=}0.3$ & $r = r_{\\text{exec}} \\cdot (1 + 0.3 \\cdot \\text{ISR})$ \\\\\nRandom $\\beta{=}0.1$ & $r = r_{\\text{exec}} \\cdot (1 + 0.1 \\cdot u),\\; u{\\sim}\\mathcal{U}(0,1)$ \\\\\nRandom $\\beta{=}0.3$ & $r = r_{\\text{exec}} \\cdot (1 + 0.3 \\cdot u)$ \\\\\nSFT & Supervised fine-tuning (no RL) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$= 0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify seven distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\n\n\\subsection{H1 --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).        % <-- conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$= 1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 52--100\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as H1 (52--93\\%); under ISR reward, it shifts to H7 (64.5\\% mean).\n\n\n\\subsection{H7 --- Conclusion Duplication}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises:\n  all x ((A(x) & B(x)) -> (C(x) | D(x))).\nConclusion:\n  all x ((A(x) & B(x)) -> (C(x) | D(x))).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nH7 is the only mode that simultaneously games both exec reward and ISR reward.\n\n\\paragraph{Prevalence.}\nISR-specific: 3-seed mean = 66.4\\% under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\n\\textbf{Zero} occurrences under Random~$\\beta{=}0.1$ across all three seeds ($0/256$).\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$= 1.0$ (the sole premise is necessary).\nDistinguished from H7 by having low component count ($n_{\\text{comp}} \\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$= 0.98$, mean~$n_{\\text{comp}} = 2.04$, 100\\%~H7 by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\%~H7, PR~$= 0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$= 14\\%$, ISR~$= 0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) -> exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).                   % <-- only this needed\nConclusion: Q(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$= 0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$= 0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18.   % 18.55 mean components\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$= 0.003$, with 94.8\\% of proved samples having ISR~$= 0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe fact is necessarily necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to H7 but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.885$).\n95/97 proved samples have $n_{\\text{necessary}} = 1$, confirming functional tautology despite the strict classifier reporting 100\\% genuine.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-detailed} and \\ref{tab:prolog-detailed} report full per-seed results for all experiment conditions.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\\ = percentage among proved samples.  ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$); 3-seed mean includes this methodological difference.}\n\\label{tab:fol-detailed}\n\\small\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & ${\\sim}$8 ep. & 0.14 & 0.571 & 0 & 7.1 & \\textbf{92.9} & Supervised, no RL \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 12.9 & \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.14 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Sampling $T{=}0.7$ \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std$^\\dagger$} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step only \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{30.9} & Mixed H1+H7 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{96.7} & 0 & ${\\sim}$3 & H7 dominant \\\\\n  & 44 & 500 & 0.89 & 0.902 & 86.5 & 0 & ${\\sim}$13.5 & H7 dominant \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & Goodhart collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 70.9 & 29.1 & \\\\\n  & 43 & 500 & 0.88 & 0.058 & 0 & 93.2 & 6.8 & \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 79.8 & 20.2 & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.85{\\pm}0.06$} & & \\makebox[0pt][l]{$0.086{\\pm}0.039$} & & & H7 = 0\\% all seeds \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & --- & --- & --- & $n_{\\text{comp}} = 9.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.53{\\pm}0.31$} & & \\makebox[0pt][l]{$0.146{\\pm}0.21$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & H7 tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional H7$^a$ \\\\\n  & 44 & 0.97 & 0.885 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.62{\\pm}0.31$} & & \\makebox[0pt][l]{$0.690{\\pm}0.44$} & & 3/3 Goodhart, 0\\% genuine \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict H7 classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}} = 1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Genuine$\\,{=}\\,$100\\%, but 95/97 proved samples have $n_{\\text{necessary}} = 1$. The model converts NL to snake\\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^* = 0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4\\%$) $\\to$ $0.003$ at 1000 steps ($-99.6\\%$ from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$= 0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% genuine proofs, but each discovers a different gaming mechanism:\nseed~42 produces clean H7 tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n",
      "numLines": 339,
      "startLine": 1,
      "totalLines": 339
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "7c8ada87-c259-4d71-93c2-c6da4cb7a10b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019QvqsctqsS92oKFXtfruff",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8408,
      "cache_read_input_tokens": 43902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8408
      },
      "output_tokens": 84,
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_015vnYvkgyqc2CZbzf6adGHC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "5c2c0eb2-97fe-487e-8250-3e0f529b1d6b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019QvqsctqsS92oKFXtfruff",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8408,
      "cache_read_input_tokens": 43902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8408
      },
      "output_tokens": 84,
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

_source line 11 · 2026-05-14T20:00:41.774Z_

<details><summary>↩ Tool result · `toolu_015vnYvkgyqc2CZbzf6adGHC`</summary>

```text
1	% Method section — solver-trace-ablation
2	% Requires: algorithm, algorithmic, amsmath, enumitem packages
3	
4	\section{Method}
5	\label{sec:method}
6	
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig1_sta_overview.pdf}
10	\caption{Overview of Solver Trace Ablation (STA). (a) Formalization pipeline: NL input is formalized into logical representation and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations to compute ISR. (c) ISR as diagnostic vs.\ ISR as reward: when the diagnostic becomes the optimization target, meta-level Goodhart's Law emerges.}
11	\label{fig:sta-overview}
12	\end{figure*}
13	
14	\subsection{Task: NL to Formal Logic}
15	\label{sec:task}
16	
17	Given natural language premises $P_1, \ldots, P_k$ and a conclusion $C$, the task is to produce a formal logic program $F = \{c_1, \ldots, c_n\}$, where each component $c_i$ is a premise encoding (in FOL) or a clause/fact (in Prolog), with one distinguished component encoding the query derived from $C$.
18	An external solver $S$ determines whether $F$ constitutes a valid proof:
19	$S(F) \in \{\textit{proved}, \textit{failed}\}$.
20	We experiment with two solver backends: Prover9 for first-order logic and SWI-Prolog for Prolog programs (\autoref{fig:sta-overview}a).
21	
22	\subsection{GRPO Training}
23	\label{sec:grpo}
24	
25	We train formalizers with Group Relative Policy Optimization \citep[GRPO;][]{deepseekmath}.
26	For each training prompt, the policy samples $K{=}8$ rollouts.
27	Each rollout receives a binary \emph{execution reward}:
28	\begin{equation}
29	  r_{\text{exec}}(x) = \mathbf{1}\bigl[S(F_x) = \textit{proved}\bigr]
30	  \label{eq:rexec}
31	\end{equation}
32	where $F_x$ is the formalization produced by rollout $x$.
33	Advantages are computed group-relative: $A_i = (r_i - \bar{r}) / \sigma_r$ within each prompt's rollout group, and the policy update maximizes expected advantage under a clipped surrogate objective with KL regularization.
34	
35	This setup optimizes \emph{prove rate}---the fraction of rollouts yielding a proved formalization---but provides no signal about the \emph{structural quality} of proved outputs.
36	A formalization that embeds the conclusion among its premises, producing a trivially provable tautology, receives the same reward as a faithful multi-step derivation.
37	
38	\subsection{Solver Trace Ablation (STA)}
39	\label{sec:sta}
40	
41	To diagnose structural quality, we propose \emph{Solver Trace Ablation} (STA), a leave-one-out protocol that tests whether each component of a proved formalization is individually necessary for proof success (\autoref{fig:sta-overview}b).
42	
43	\paragraph{Protocol.}
44	Given a proved formalization $x$ with $n$ components $\{c_1, \ldots, c_n\}$, STA constructs $n$ ablated variants $x \setminus \{c_i\}$, each with one component removed, and re-runs the solver on each.
45	A component $c_i$ is \emph{necessary} if its removal causes proof failure: $S(x \setminus \{c_i\}) = \textit{failed}$.
46	What constitutes a component depends on the logic type: individual premises in FOL, individual clauses or ground facts in Prolog.
47	
48	\paragraph{Intensional Structural Reward.}
49	We define ISR as the fraction of necessary components:
50	\begin{equation}
51	  \text{ISR}(x) = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}\bigl[S(x \setminus \{c_i\}) = \textit{failed}\bigr]
52	  \label{eq:isr}
53	\end{equation}
54	ISR $\in [0, 1]$ and is defined only for proved formalizations ($r_{\text{exec}}(x) = 1$).
55	ISR $= 1$ indicates a maximally tight formalization where every component is individually necessary; ISR $= 0$ indicates complete redundancy.
56	The protocol is solver-agnostic: it applies to any solver that accepts component-level input manipulation, requiring $n{+}1$ solver calls per sample (one initial verification plus $n$ ablations).
57	
58	Algorithm~\ref{alg:sta} gives the full procedure.
59	
60	\begin{algorithm}[t]
61	\caption{Solver Trace Ablation (STA)}
62	\label{alg:sta}
63	\begin{algorithmic}[1]
64	\REQUIRE Formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
65	\ENSURE ISR score $\in [0,1]$ or $\bot$ (undefined)
66	\IF{$S(x) \neq \textit{proved}$}
67	  \RETURN $\bot$
68	\ENDIF
69	\STATE $n_{\text{nec}} \gets 0$
70	\FOR{$i = 1$ \TO $n$}
71	  \STATE $x' \gets x \setminus \{c_i\}$
72	  \IF{$S(x') = \textit{failed}$}
73	    \STATE $n_{\text{nec}} \gets n_{\text{nec}} + 1$
74	  \ENDIF
75	\ENDFOR
76	\RETURN $n_{\text{nec}} \mathbin{/} n$
77	\end{algorithmic}
78	\end{algorithm}
79	
80	STA draws on the same intuition as mutation testing in software engineering \citep{demillo1978, jia-harman-survey}: systematically perturbing a program to assess whether each element contributes to the overall result.
81	The key difference is that STA operates on solver \emph{inputs} (formalizations) rather than program code, and targets component necessity rather than test adequacy.
82	
83	\paragraph{ISR limitations.}
84	ISR measures syntactic component necessity, not semantic faithfulness to the natural language input.
85	It is also subject to a component-count confound: formalizations with fewer components yield mechanically higher ISR, since each component carries a larger share of the proof burden under LOO ablation.
86	We control for this confound in our analysis (\S\ref{sec:goodhart}).
87	
88	\subsection{ISR as Reward Signal}
89	\label{sec:rewards}
90	
91	Having defined ISR as a diagnostic, we investigate whether it can serve as a training signal (\autoref{fig:sta-overview}c).
92	We study six reward conditions across two formulations.
93	For all RL conditions, bonuses apply only to proved samples; unproved samples receive $r = 0$.
94	
95	\paragraph{Exec-only (baseline).}
96	$r = r_{\text{exec}}$.
97	Binary solver verification with no structural component.
98	
99	\paragraph{Additive ISR.}
100	\begin{equation}
101	  r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR}(x)), \quad \beta \in \{0.1, 0.3\}
102	  \label{eq:additive-isr}
103	\end{equation}
104	ISR provides a bonus proportional to structural tightness, gated on proof success.
105	The multiplicative gating ensures that unproved samples never receive an ISR bonus.
106	
107	\paragraph{Additive Random (control).}
108	\begin{equation}
109	  r = r_{\text{exec}} \cdot (1 + \beta \cdot u), \quad u \sim \mathcal{U}(0,1), \quad \beta \in \{0.1, 0.3\}
110	  \label{eq:additive-random}
111	\end{equation}
112	Replacing ISR with uniform noise isolates the causal effect of ISR-specific structural signal from general reward-shaping effects (variance injection, magnitude scaling).
113	
114	\paragraph{SFT baseline.}
115	Supervised fine-tuning on gold formalizations with no reinforcement learning, confirming whether observed hacking behaviors are RL-reward-specific or artifacts of general fine-tuning.
116	
117	Each RL condition is trained across three random seeds (42, 43, 44).
118	Seeds control model initialization and training stochasticity; all seeds share identical training data (\S\ref{sec:setup}).
119	
120	\subsection{Hacking Taxonomy}
121	\label{sec:taxonomy-method}
122	
123	Analysis of trained models across reward conditions, seeds, and logic types reveals seven distinct reward hacking modes (full quantitative analysis in \S\ref{sec:taxonomy}):
124	
125	\begin{enumerate}[leftmargin=*, itemsep=2pt]
126	\item \textbf{Conclusion Embedding (H1).}
127	The conclusion appears verbatim as one of multiple premises; the solver succeeds trivially regardless of the other premises.
128	
129	\item \textbf{Conclusion Duplication (H7).}
130	The formalization collapses to a single premise identical to the conclusion.
131	LOO ablation marks this sole component as necessary, yielding ISR$=$1 by construction.
132	
133	\item \textbf{Tautological Collapse.}
134	Two-component formalizations where the premise and query are identical.
135	
136	\item \textbf{Repetition Collapse.}
137	Identical premises or clauses repeated until the token limit.
138	Removing any single copy leaves the others intact, yielding ISR $\approx 0$.
139	
140	\item \textbf{Complexity-without-utility.}
141	Excessive syntactically complex but semantically vacuous components, none individually necessary.
142	
143	\item \textbf{Contradiction Explosion.}
144	Unbounded component count growth over training, with the excess premises trivially entailing any conclusion.
145	
146	\item \textbf{Query-as-fact Gaming.}
147	The model converts the natural language conclusion into an atom and includes it as both a fact and the query.
148	This mode bypasses text-match classifiers designed for H1/H7.
149	\end{enumerate}
150	
151	Modes are identified by a two-stage classification procedure.
152	First, strict normalized text matching detects H1 and H7 by comparing each premise against the query.
153	Second, functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA catches modes that evade text matching---particularly query-as-fact gaming, where the gaming mechanism produces surface-level novelty invisible to exact-match classifiers.
154	Samples not assigned to any hacking mode are classified as \emph{genuine}.
155	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "01b6b2d6-7cca-49c6-9ff4-8fa597670860",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
      "content": "% Method section — solver-trace-ablation\n% Requires: algorithm, algorithmic, amsmath, enumitem packages\n\n\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{Overview of Solver Trace Ablation (STA). (a) Formalization pipeline: NL input is formalized into logical representation and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations to compute ISR. (c) ISR as diagnostic vs.\\ ISR as reward: when the diagnostic becomes the optimization target, meta-level Goodhart's Law emerges.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\n\\subsection{Task: NL to Formal Logic}\n\\label{sec:task}\n\nGiven natural language premises $P_1, \\ldots, P_k$ and a conclusion $C$, the task is to produce a formal logic program $F = \\{c_1, \\ldots, c_n\\}$, where each component $c_i$ is a premise encoding (in FOL) or a clause/fact (in Prolog), with one distinguished component encoding the query derived from $C$.\nAn external solver $S$ determines whether $F$ constitutes a valid proof:\n$S(F) \\in \\{\\textit{proved}, \\textit{failed}\\}$.\nWe experiment with two solver backends: Prover9 for first-order logic and SWI-Prolog for Prolog programs (\\autoref{fig:sta-overview}a).\n\n\\subsection{GRPO Training}\n\\label{sec:grpo}\n\nWe train formalizers with Group Relative Policy Optimization \\citep[GRPO;][]{deepseekmath}.\nFor each training prompt, the policy samples $K{=}8$ rollouts.\nEach rollout receives a binary \\emph{execution reward}:\n\\begin{equation}\n  r_{\\text{exec}}(x) = \\mathbf{1}\\bigl[S(F_x) = \\textit{proved}\\bigr]\n  \\label{eq:rexec}\n\\end{equation}\nwhere $F_x$ is the formalization produced by rollout $x$.\nAdvantages are computed group-relative: $A_i = (r_i - \\bar{r}) / \\sigma_r$ within each prompt's rollout group, and the policy update maximizes expected advantage under a clipped surrogate objective with KL regularization.\n\nThis setup optimizes \\emph{prove rate}---the fraction of rollouts yielding a proved formalization---but provides no signal about the \\emph{structural quality} of proved outputs.\nA formalization that embeds the conclusion among its premises, producing a trivially provable tautology, receives the same reward as a faithful multi-step derivation.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\nTo diagnose structural quality, we propose \\emph{Solver Trace Ablation} (STA), a leave-one-out protocol that tests whether each component of a proved formalization is individually necessary for proof success (\\autoref{fig:sta-overview}b).\n\n\\paragraph{Protocol.}\nGiven a proved formalization $x$ with $n$ components $\\{c_1, \\ldots, c_n\\}$, STA constructs $n$ ablated variants $x \\setminus \\{c_i\\}$, each with one component removed, and re-runs the solver on each.\nA component $c_i$ is \\emph{necessary} if its removal causes proof failure: $S(x \\setminus \\{c_i\\}) = \\textit{failed}$.\nWhat constitutes a component depends on the logic type: individual premises in FOL, individual clauses or ground facts in Prolog.\n\n\\paragraph{Intensional Structural Reward.}\nWe define ISR as the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n} \\sum_{i=1}^{n} \\mathbf{1}\\bigl[S(x \\setminus \\{c_i\\}) = \\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR $\\in [0, 1]$ and is defined only for proved formalizations ($r_{\\text{exec}}(x) = 1$).\nISR $= 1$ indicates a maximally tight formalization where every component is individually necessary; ISR $= 0$ indicates complete redundancy.\nThe protocol is solver-agnostic: it applies to any solver that accepts component-level input manipulation, requiring $n{+}1$ solver calls per sample (one initial verification plus $n$ ablations).\n\nAlgorithm~\\ref{alg:sta} gives the full procedure.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE ISR score $\\in [0,1]$ or $\\bot$ (undefined)\n\\IF{$S(x) \\neq \\textit{proved}$}\n  \\RETURN $\\bot$\n\\ENDIF\n\\STATE $n_{\\text{nec}} \\gets 0$\n\\FOR{$i = 1$ \\TO $n$}\n  \\STATE $x' \\gets x \\setminus \\{c_i\\}$\n  \\IF{$S(x') = \\textit{failed}$}\n    \\STATE $n_{\\text{nec}} \\gets n_{\\text{nec}} + 1$\n  \\ENDIF\n\\ENDFOR\n\\RETURN $n_{\\text{nec}} \\mathbin{/} n$\n\\end{algorithmic}\n\\end{algorithm}\n\nSTA draws on the same intuition as mutation testing in software engineering \\citep{demillo1978, jia-harman-survey}: systematically perturbing a program to assess whether each element contributes to the overall result.\nThe key difference is that STA operates on solver \\emph{inputs} (formalizations) rather than program code, and targets component necessity rather than test adequacy.\n\n\\paragraph{ISR limitations.}\nISR measures syntactic component necessity, not semantic faithfulness to the natural language input.\nIt is also subject to a component-count confound: formalizations with fewer components yield mechanically higher ISR, since each component carries a larger share of the proof burden under LOO ablation.\nWe control for this confound in our analysis (\\S\\ref{sec:goodhart}).\n\n\\subsection{ISR as Reward Signal}\n\\label{sec:rewards}\n\nHaving defined ISR as a diagnostic, we investigate whether it can serve as a training signal (\\autoref{fig:sta-overview}c).\nWe study six reward conditions across two formulations.\nFor all RL conditions, bonuses apply only to proved samples; unproved samples receive $r = 0$.\n\n\\paragraph{Exec-only (baseline).}\n$r = r_{\\text{exec}}$.\nBinary solver verification with no structural component.\n\n\\paragraph{Additive ISR.}\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR}(x)), \\quad \\beta \\in \\{0.1, 0.3\\}\n  \\label{eq:additive-isr}\n\\end{equation}\nISR provides a bonus proportional to structural tightness, gated on proof success.\nThe multiplicative gating ensures that unproved samples never receive an ISR bonus.\n\n\\paragraph{Additive Random (control).}\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u), \\quad u \\sim \\mathcal{U}(0,1), \\quad \\beta \\in \\{0.1, 0.3\\}\n  \\label{eq:additive-random}\n\\end{equation}\nReplacing ISR with uniform noise isolates the causal effect of ISR-specific structural signal from general reward-shaping effects (variance injection, magnitude scaling).\n\n\\paragraph{SFT baseline.}\nSupervised fine-tuning on gold formalizations with no reinforcement learning, confirming whether observed hacking behaviors are RL-reward-specific or artifacts of general fine-tuning.\n\nEach RL condition is trained across three random seeds (42, 43, 44).\nSeeds control model initialization and training stochasticity; all seeds share identical training data (\\S\\ref{sec:setup}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy-method}\n\nAnalysis of trained models across reward conditions, seeds, and logic types reveals seven distinct reward hacking modes (full quantitative analysis in \\S\\ref{sec:taxonomy}):\n\n\\begin{enumerate}[leftmargin=*, itemsep=2pt]\n\\item \\textbf{Conclusion Embedding (H1).}\nThe conclusion appears verbatim as one of multiple premises; the solver succeeds trivially regardless of the other premises.\n\n\\item \\textbf{Conclusion Duplication (H7).}\nThe formalization collapses to a single premise identical to the conclusion.\nLOO ablation marks this sole component as necessary, yielding ISR$=$1 by construction.\n\n\\item \\textbf{Tautological Collapse.}\nTwo-component formalizations where the premise and query are identical.\n\n\\item \\textbf{Repetition Collapse.}\nIdentical premises or clauses repeated until the token limit.\nRemoving any single copy leaves the others intact, yielding ISR $\\approx 0$.\n\n\\item \\textbf{Complexity-without-utility.}\nExcessive syntactically complex but semantically vacuous components, none individually necessary.\n\n\\item \\textbf{Contradiction Explosion.}\nUnbounded component count growth over training, with the excess premises trivially entailing any conclusion.\n\n\\item \\textbf{Query-as-fact Gaming.}\nThe model converts the natural language conclusion into an atom and includes it as both a fact and the query.\nThis mode bypasses text-match classifiers designed for H1/H7.\n\\end{enumerate}\n\nModes are identified by a two-stage classification procedure.\nFirst, strict normalized text matching detects H1 and H7 by comparing each premise against the query.\nSecond, functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA catches modes that evade text matching---particularly query-as-fact gaming, where the gaming mechanism produces surface-level novelty invisible to exact-match classifiers.\nSamples not assigned to any hacking mode are classified as \\emph{genuine}.\n",
      "numLines": 155,
      "startLine": 1,
      "totalLines": 155
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01Tzv5Pgu6PL2Ngy7xHvaUgP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "ae672cb5-64d6-493e-9607-49e47ca81ed2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MXuxJgvSj9X1bPoEEUsX73",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 52310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4052
      },
      "output_tokens": 47,
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

_source line 13 · 2026-05-14T20:00:47.226Z_

<details><summary>↩ Tool result · `toolu_01Tzv5Pgu6PL2Ngy7xHvaUgP`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.
9	Without a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from models that exploit solver mechanics.
10	This gap is particularly consequential in reinforcement learning settings, where the optimizer will find and exploit any shortcut the reward function fails to penalize~\cite{skalse-reward-hacking, reward-hacking-survey}.
11	
12	Neurosymbolic approaches combine large language models with external solvers for logical reasoning.
13	Prompting-based methods such as SatLM~\cite{satlm}, Logic-LM~\cite{logic-lm}, and LINC~\cite{linc} translate natural language to formal representations verified by automated provers, but evaluate correctness through execution alone without examining the internal structure of proved outputs.
14	Recent work applies reinforcement learning---specifically Group Relative Policy Optimization~\cite[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by theorem provers~\cite{mellgren-prolog-grpo, logic-rl}.
15	The standard reward signal in these systems is binary execution feedback: 1 if the solver returns a proof, 0 otherwise.
16	This drives rapid improvement in prove rate but provides no gradient on structural quality---a formalization where every premise contributes to a valid derivation receives the same reward as one that smuggles the conclusion into the premises.
17	Process reward models~\cite{lightman-verify-step} offer finer-grained step-level supervision for mathematical reasoning, but require expensive human annotations and do not transfer to arbitrary solver-backed verification settings.
18	No existing method provides an annotation-free, solver-agnostic diagnostic for structural integrity in neurosymbolic outputs.
19	
20	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing in software engineering~\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\autoref{fig:sta-overview}).
21	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR).
22	ISR${=}$1 indicates a maximally tight formalization where every component is individually necessary; ISR${=}$0 indicates complete structural redundancy.
23	The protocol is solver-agnostic, requiring only a solver that accepts component-level input manipulation.
24	Applied as a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\cite{folio} data, ISR reveals a structural collapse trajectory entirely invisible to prove rate: ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\% degradation---while prove rate simultaneously rises from 32\% to 96\%.
25	Three random seeds diverge radically (PR $\sigma{=}$47\,pp), each converging to a qualitatively different degeneration mode: conclusion embedding, repetition collapse, and tautological collapse.
26	A supervised fine-tuning (SFT) baseline achieves 92.9\% genuine proofs with near-zero hacking, confirming that the structural collapse is a consequence of RL reward optimization, not model capacity or data limitations.
27	
28	Given ISR's diagnostic power, a natural question is whether it can serve as a training signal to steer models toward structurally sound formalizations.
29	The answer is negative: when ISR is incorporated into the reward ($r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR})$), the model games the diagnostic metric itself---a phenomenon we characterize as \emph{meta-level Goodhart's Law}~\cite{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.
30	At low dose ($\beta{=}0.1$), two of three seeds are dominated by \emph{conclusion duplication}: the model generates a single premise identical to the conclusion, achieving ISR${=}$1 by construction while encoding no reasoning.
31	Across three seeds, 64.5\% of proved samples exhibit this ISR-specific gaming mode (H7), compared to 0\% under a matched random-reward control.
32	The remaining seed's apparent ISR advantage is entirely a premise-count artifact: controlling for component count eliminates the difference (1.06$\times$; \S\ref{sec:goodhart}).
33	At high dose ($\beta{=}0.3$), classic Goodhart collapse occurs: prove rate falls to 18\%, compared to 48\% for a matched random control~\cite{gao-reward-overoptimization}.
34	This dose-response pattern---low-dose proxy gaming followed by high-dose performance collapse---maps onto established Goodhart dynamics but occurs at the \emph{meta} level: ISR was designed to detect gaming, yet becomes the target of gaming when optimized.
35	
36	We further validate that both the diagnostic utility and the Goodhart phenomenon transfer across formal languages.
37	In Prolog experiments using SWI-Prolog as the solver, exec-only training produces proved-only ISR near zero for two of three seeds, replicating the FOL diagnostic finding.
38	When ISR is added as a Prolog training reward, the result is \emph{universal} Goodhart: all three seeds converge to gaming with 0\% genuine proofs---stronger than the FOL result, where ${\sim}$16\% genuine residual persists---each via a distinct mechanism (tautological collapse, degenerate syntax, and query-as-fact gaming).
39	
40	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we make four contributions:
41	
42	\begin{enumerate}[nosep,leftmargin=*]
43	\item We introduce Solver Trace Ablation and establish ISR as a diagnostic that detects reward hacking invisible to prove rate, documenting a complete collapse trajectory ($0.642 \to 0.132 \to 0.003$) over 1000 GRPO training steps; an SFT baseline confirms hacking is RL-specific (92.9\% genuine vs.\ $\leq$19\% mean across RL conditions).
44	\item We empirically characterize meta-level Goodhart's Law in neurosymbolic RL---a diagnostic designed to detect gaming becomes gamed when used as reward---and identify the premise-count confound, a systematic LOO bias where fewer components mechanically inflate ISR, that explains the sole apparent improvement (1.06$\times$ premise-matched).
45	\item We demonstrate cross-logic diagnostic transfer from FOL/Prover9 to Prolog/SWI-Prolog, where ISR-as-reward produces universal Goodhart (3/3 seeds gaming, 0\% genuine), demonstrating that simpler formal semantics enable more complete exploitation.
46	\item We catalog 7 reward hacking modes across conditions and logic types, including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of automated hacking diagnostics.
47	\end{enumerate}
48	
49	\noindent \S\ref{sec:related-work} surveys related work; \S\ref{sec:method} introduces the STA protocol; \S\ref{sec:experiments} presents experiments; \S\ref{sec:discussion} discusses implications.
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "634d130c-9cc8-48c6-82d5-351c0fbe729e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on first-order logic problems---yet 87\\% of its proved outputs embed the conclusion verbatim among the premises.\nThe solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.\nThis structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.\n\nProve rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.\nWithout a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from models that exploit solver mechanics.\nThis gap is particularly consequential in reinforcement learning settings, where the optimizer will find and exploit any shortcut the reward function fails to penalize~\\cite{skalse-reward-hacking, reward-hacking-survey}.\n\nNeurosymbolic approaches combine large language models with external solvers for logical reasoning.\nPrompting-based methods such as SatLM~\\cite{satlm}, Logic-LM~\\cite{logic-lm}, and LINC~\\cite{linc} translate natural language to formal representations verified by automated provers, but evaluate correctness through execution alone without examining the internal structure of proved outputs.\nRecent work applies reinforcement learning---specifically Group Relative Policy Optimization~\\cite[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by theorem provers~\\cite{mellgren-prolog-grpo, logic-rl}.\nThe standard reward signal in these systems is binary execution feedback: 1 if the solver returns a proof, 0 otherwise.\nThis drives rapid improvement in prove rate but provides no gradient on structural quality---a formalization where every premise contributes to a valid derivation receives the same reward as one that smuggles the conclusion into the premises.\nProcess reward models~\\cite{lightman-verify-step} offer finer-grained step-level supervision for mathematical reasoning, but require expensive human annotations and do not transfer to arbitrary solver-backed verification settings.\nNo existing method provides an annotation-free, solver-agnostic diagnostic for structural integrity in neurosymbolic outputs.\n\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing in software engineering~\\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\\autoref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR).\nISR${=}$1 indicates a maximally tight formalization where every component is individually necessary; ISR${=}$0 indicates complete structural redundancy.\nThe protocol is solver-agnostic, requiring only a solver that accepts component-level input manipulation.\nApplied as a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\cite{folio} data, ISR reveals a structural collapse trajectory entirely invisible to prove rate: ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\\% degradation---while prove rate simultaneously rises from 32\\% to 96\\%.\nThree random seeds diverge radically (PR $\\sigma{=}$47\\,pp), each converging to a qualitatively different degeneration mode: conclusion embedding, repetition collapse, and tautological collapse.\nA supervised fine-tuning (SFT) baseline achieves 92.9\\% genuine proofs with near-zero hacking, confirming that the structural collapse is a consequence of RL reward optimization, not model capacity or data limitations.\n\nGiven ISR's diagnostic power, a natural question is whether it can serve as a training signal to steer models toward structurally sound formalizations.\nThe answer is negative: when ISR is incorporated into the reward ($r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$), the model games the diagnostic metric itself---a phenomenon we characterize as \\emph{meta-level Goodhart's Law}~\\cite{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.\nAt low dose ($\\beta{=}0.1$), two of three seeds are dominated by \\emph{conclusion duplication}: the model generates a single premise identical to the conclusion, achieving ISR${=}$1 by construction while encoding no reasoning.\nAcross three seeds, 64.5\\% of proved samples exhibit this ISR-specific gaming mode (H7), compared to 0\\% under a matched random-reward control.\nThe remaining seed's apparent ISR advantage is entirely a premise-count artifact: controlling for component count eliminates the difference (1.06$\\times$; \\S\\ref{sec:goodhart}).\nAt high dose ($\\beta{=}0.3$), classic Goodhart collapse occurs: prove rate falls to 18\\%, compared to 48\\% for a matched random control~\\cite{gao-reward-overoptimization}.\nThis dose-response pattern---low-dose proxy gaming followed by high-dose performance collapse---maps onto established Goodhart dynamics but occurs at the \\emph{meta} level: ISR was designed to detect gaming, yet becomes the target of gaming when optimized.\n\nWe further validate that both the diagnostic utility and the Goodhart phenomenon transfer across formal languages.\nIn Prolog experiments using SWI-Prolog as the solver, exec-only training produces proved-only ISR near zero for two of three seeds, replicating the FOL diagnostic finding.\nWhen ISR is added as a Prolog training reward, the result is \\emph{universal} Goodhart: all three seeds converge to gaming with 0\\% genuine proofs---stronger than the FOL result, where ${\\sim}$16\\% genuine residual persists---each via a distinct mechanism (tautological collapse, degenerate syntax, and query-as-fact gaming).\n\nAcross 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we make four contributions:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item We introduce Solver Trace Ablation and establish ISR as a diagnostic that detects reward hacking invisible to prove rate, documenting a complete collapse trajectory ($0.642 \\to 0.132 \\to 0.003$) over 1000 GRPO training steps; an SFT baseline confirms hacking is RL-specific (92.9\\% genuine vs.\\ $\\leq$19\\% mean across RL conditions).\n\\item We empirically characterize meta-level Goodhart's Law in neurosymbolic RL---a diagnostic designed to detect gaming becomes gamed when used as reward---and identify the premise-count confound, a systematic LOO bias where fewer components mechanically inflate ISR, that explains the sole apparent improvement (1.06$\\times$ premise-matched).\n\\item We demonstrate cross-logic diagnostic transfer from FOL/Prover9 to Prolog/SWI-Prolog, where ISR-as-reward produces universal Goodhart (3/3 seeds gaming, 0\\% genuine), demonstrating that simpler formal semantics enable more complete exploitation.\n\\item We catalog 7 reward hacking modes across conditions and logic types, including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of automated hacking diagnostics.\n\\end{enumerate}\n\n\\noindent \\S\\ref{sec:related-work} surveys related work; \\S\\ref{sec:method} introduces the STA protocol; \\S\\ref{sec:experiments} presents experiments; \\S\\ref{sec:discussion} discusses implications.\n",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 50
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "f61814a8-9dc3-4df9-99c7-9b6d73ff0460",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WUQHqa8d5zTnw5WX3dhPPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3011,
      "cache_read_input_tokens": 56362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3011
      },
      "output_tokens": 37,
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

<details open><summary>🔧 Tool call — Grep · `toolu_01EUd4dtHzPMRmJHueVazk3h`</summary>

```json
{
  "pattern": "tab:fol-detailed|tab:prolog-detailed|tab:hyperparams|tab:beta01-3seed|tab:prolog-crosslogic|fig:prolog-comparison|sec:hacking-defs|app:hacking-modes",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "1fe02766-6f02-4176-9b2f-023b81fe5566",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WUQHqa8d5zTnw5WX3dhPPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3011,
      "cache_read_input_tokens": 56362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3011
      },
      "output_tokens": 37,
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

_source line 16 · 2026-05-14T20:01:04.215Z_

<details><summary>↩ Tool result · `toolu_01EUd4dtHzPMRmJHueVazk3h`</summary>

```text
paper/appendix.tex:9:Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
paper/appendix.tex:16:\label{tab:hyperparams}
paper/appendix.tex:67:\label{app:hacking-modes}
paper/appendix.tex:239:Tables~\ref{tab:fol-detailed} and \ref{tab:prolog-detailed} report full per-seed results for all experiment conditions.
paper/appendix.tex:246:\label{tab:fol-detailed}
paper/appendix.tex:296:\label{tab:prolog-detailed}
paper/appendix.tex:328:Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
paper/experiments.tex:86:[Omitted long matching line]
paper/experiments.tex:115:\label{tab:beta01-3seed}
paper/experiments.tex:118:Table~\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\% under random reward and 0--51.9\% under ISR. ISR reward does not reduce total hacking---it \emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\% vs Random s42: 70.9\%), and the random control achieves higher and more stable PR (85$\pm$6\% vs 77$\pm$14\%).
paper/experiments.tex:140:\label{fig:prolog-comparison}
paper/experiments.tex:167:\label{tab:prolog-crosslogic}
paper/experiments.tex:171:[Omitted long matching line]
paper/experiments.tex:176:Table~\ref{tab:prolog-crosslogic} (bottom) and Figure~\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:
paper/experiments.tex:214:\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed means. Exec: H1${=}$87\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-crosslogic}).}
paper/main.aux:828:[Omitted long matching line]
paper/main.aux:829:[Omitted long matching line]
paper/main.aux:832:[Omitted long matching line]
paper/main.aux:894:[Omitted long matching line]
paper/main.aux:931:[Omitted long matching line]
paper/main.aux:966:\@writefile{lot}{\contentsline {table}{\numberline {4}{\ignorespaces Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta {=}0.1$ 3-seed means. Exec: H1${=}$87\% in s42; $\bullet $ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref {tab:prolog-crosslogic}).}}{11}{table.caption.34}\protected@file@percent }
paper/main.aux:967:\newlabel{tab:hacking-taxonomy}{{4}{11}{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta {=}0.1$ 3-seed means. Exec: H1${=}$87\% in s42; $\bullet $ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref {tab:prolog-crosslogic})}{table.caption.34}{}}
paper/main.aux:1392:\newlabel{app:hacking-modes}{{B}{14}{Hacking Mode Definitions}{appendix.B}{}}
paper/main.aux:1629:\newlabel{tab:hyperparams}{{5}{17}{Training hyperparameters for all GRPO experiments}{table.caption.43}{}}
paper/main.aux:1631:\newlabel{tab:fol-detailed}{{6}{18}{Detailed per-seed results: FOL (Prover9). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger $s43 uses sampling eval ($T{=}0.7$); 3-seed mean includes this methodological difference}{table.caption.73}{}}
paper/main.aux:1633:\newlabel{tab:prolog-detailed}{{7}{18}{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\ = percentage among proved samples. ``---'' indicates data not available}{table.caption.74}{}}
paper/paper.aux:815:[Omitted long matching line]
paper/paper.aux:816:[Omitted long matching line]
paper/paper.aux:819:[Omitted long matching line]
paper/paper.aux:842:\newlabel{fig:prolog-comparison}{{3}{9}{Prolog exec-only ISR across three seeds. ISR$^*$ is near-zero for all seeds (s42${=}$0.037, s43${=}$0.015), replicating the FOL finding that exec-only training produces structurally degenerate outputs regardless of PR. Seed~44 ISR$^*{=}$0.387 is a small-sample artifact ($n{=}$21 proved). Cross-seed PR instability ($\sigma {=}$31pp) also replicates}{figure.caption.27}{}}
paper/paper.aux:868:[Omitted long matching line]
paper/paper.aux:901:\@writefile{lot}{\contentsline {table}{\numberline {4}{\ignorespaces Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta {=}0.1$ 3-seed means. Exec: H1${=}$87\% in s42; $\bullet $ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref {tab:prolog-crosslogic}).}}{10}{table.caption.33}\protected@file@percent }
paper/paper.aux:902:\newlabel{tab:hacking-taxonomy}{{4}{10}{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta {=}0.1$ 3-seed means. Exec: H1${=}$87\% in s42; $\bullet $ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref {tab:prolog-crosslogic})}{table.caption.33}{}}
paper/discussion.tex:20:Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:beta01-3seed}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "9a01ebbd-dd13-4d54-9be7-7f27ac2f7152",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/appendix.tex:9:Table~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\npaper/appendix.tex:16:\\label{tab:hyperparams}\npaper/appendix.tex:67:\\label{app:hacking-modes}\npaper/appendix.tex:239:Tables~\\ref{tab:fol-detailed} and \\ref{tab:prolog-detailed} report full per-seed results for all experiment conditions.\npaper/appendix.tex:246:\\label{tab:fol-detailed}\npaper/appendix.tex:296:\\label{tab:prolog-detailed}\npaper/appendix.tex:328:Table~\\ref{tab:fol-detailed} traces the ISR collapse over training:\npaper/experiments.tex:86:[Omitted long matching line]\npaper/experiments.tex:115:\\label{tab:beta01-3seed}\npaper/experiments.tex:118:Table~\\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).\npaper/experiments.tex:140:\\label{fig:prolog-comparison}\npaper/experiments.tex:167:\\label{tab:prolog-crosslogic}\npaper/experiments.tex:171:[Omitted long matching line]\npaper/experiments.tex:176:Table~\\ref{tab:prolog-crosslogic} (bottom) and Figure~\\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\npaper/experiments.tex:214:\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed means. Exec: H1${=}$87\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-crosslogic}).}\npaper/main.aux:828:[Omitted long matching line]\npaper/main.aux:829:[Omitted long matching line]\npaper/main.aux:832:[Omitted long matching line]\npaper/main.aux:894:[Omitted long matching line]\npaper/main.aux:931:[Omitted long matching line]\npaper/main.aux:966:\\@writefile{lot}{\\contentsline {table}{\\numberline {4}{\\ignorespaces Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta {=}0.1$ 3-seed means. Exec: H1${=}$87\\% in s42; $\\bullet $ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref {tab:prolog-crosslogic}).}}{11}{table.caption.34}\\protected@file@percent }\npaper/main.aux:967:\\newlabel{tab:hacking-taxonomy}{{4}{11}{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta {=}0.1$ 3-seed means. Exec: H1${=}$87\\% in s42; $\\bullet $ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref {tab:prolog-crosslogic})}{table.caption.34}{}}\npaper/main.aux:1392:\\newlabel{app:hacking-modes}{{B}{14}{Hacking Mode Definitions}{appendix.B}{}}\npaper/main.aux:1629:\\newlabel{tab:hyperparams}{{5}{17}{Training hyperparameters for all GRPO experiments}{table.caption.43}{}}\npaper/main.aux:1631:\\newlabel{tab:fol-detailed}{{6}{18}{Detailed per-seed results: FOL (Prover9). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger $s43 uses sampling eval ($T{=}0.7$); 3-seed mean includes this methodological difference}{table.caption.73}{}}\npaper/main.aux:1633:\\newlabel{tab:prolog-detailed}{{7}{18}{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\\ = percentage among proved samples. ``---'' indicates data not available}{table.caption.74}{}}\npaper/paper.aux:815:[Omitted long matching line]\npaper/paper.aux:816:[Omitted long matching line]\npaper/paper.aux:819:[Omitted long matching line]\npaper/paper.aux:842:\\newlabel{fig:prolog-comparison}{{3}{9}{Prolog exec-only ISR across three seeds. ISR$^*$ is near-zero for all seeds (s42${=}$0.037, s43${=}$0.015), replicating the FOL finding that exec-only training produces structurally degenerate outputs regardless of PR. Seed~44 ISR$^*{=}$0.387 is a small-sample artifact ($n{=}$21 proved). Cross-seed PR instability ($\\sigma {=}$31pp) also replicates}{figure.caption.27}{}}\npaper/paper.aux:868:[Omitted long matching line]\npaper/paper.aux:901:\\@writefile{lot}{\\contentsline {table}{\\numberline {4}{\\ignorespaces Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta {=}0.1$ 3-seed means. Exec: H1${=}$87\\% in s42; $\\bullet $ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref {tab:prolog-crosslogic}).}}{10}{table.caption.33}\\protected@file@percent }\npaper/paper.aux:902:\\newlabel{tab:hacking-taxonomy}{{4}{10}{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta {=}0.1$ 3-seed means. Exec: H1${=}$87\\% in s42; $\\bullet $ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref {tab:prolog-crosslogic})}{table.caption.33}{}}\npaper/discussion.tex:20:Premise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:beta01-3seed}).",
    "numLines": 34
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "3fb8efaa-4dd0-46dc-977c-60d4465c6711",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UHGAAT76VB7KPbpo1RB83d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3111,
      "cache_read_input_tokens": 59373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3111
      },
      "output_tokens": 56,
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

Now I have full context. Let me execute the edits.

### Edit 1: experiments.tex — remove Tab 4, Tab 5, fig4, compress §4.4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "078308ae-e8a5-49db-8583-238796a1b035",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UHGAAT76VB7KPbpo1RB83d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3111,
      "cache_read_input_tokens": 59373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3111
      },
      "output_tokens": 56,
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

<details open><summary>🔧 Tool call — Edit · `toolu_015qTJsB4r4BTKnNcyNApfrS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); per-seed ISR in Table~\\ref{tab:beta01-3seed}. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}",
  "new_string": "\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); per-seed ISR in Appendix Table~\\ref{tab:beta01-3seed}. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "5c096dbc-7561-4dd5-ba9e-d4cd876e348d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UHGAAT76VB7KPbpo1RB83d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3111,
      "cache_read_input_tokens": 59373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3111
      },
      "output_tokens": 56,
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

_source line 20 · 2026-05-14T20:02:42.884Z_

<details><summary>↩ Tool result · reported error · `toolu_015qTJsB4r4BTKnNcyNApfrS`</summary>

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
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "718ed856-17b4-4a8c-a650-e38a4d13a410",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_018JFsxA8pZACTogPHKRQbKV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": 80,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "5bff8ae1-4388-41c1-afe4-288a8715d231",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VQdKL1bdRx3mVrmtj9crgf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5519,
      "cache_read_input_tokens": 62484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5519
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

_source line 22 · 2026-05-14T20:02:47.526Z_

<details><summary>↩ Tool result · `toolu_018JFsxA8pZACTogPHKRQbKV`</summary>

```text
80	Random & $r_e(1{+}\beta{\cdot}U)$ & 0.1 & 3 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.039} & 0 & 81 & 19 & H1 embedding \\
81	\midrule
82	ISR & $r_e(1{+}\beta{\cdot}\text{ISR})$ & 0.3 & 1 & 18 & 0.143 & --- & --- & --- & PR collapse \\
83	Random & $r_e(1{+}\beta{\cdot}U)$ & 0.3 & 1 & 48 & 0.094 & --- & --- & --- & Redundant \\
84	\bottomrule
85	\end{tabular}
86	\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\pm$std. ISR$^*$: proved-only. $U \sim \mathcal{U}(0,1)$; $r_e = r_{\text{exec}}$. $^\dagger$Seed~42 shown; see \S\ref{sec:diagnostic} for 3-seed divergence. $\ddagger$ISR omitted: inflated by H7 gaming (64.5\% of proved samples are single-premise tautologies); per-seed ISR in Table~\ref{tab:beta01-3seed}. H7/H1/Gen.\% unavailable for $\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\% bolded per group.}
87	\label{tab:goodhart-landscape}
88	\end{table*}
89	
90	\paragraph{Low-dose ISR ($\beta{=}0.1$): ISR-specific gaming.}
91	Table~\ref{tab:goodhart-landscape} summarizes results across conditions. At $\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\% of proved samples (149/231). In contrast, all three random control seeds show \emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.
92	
93	\begin{table}[t]
94	\centering
95	\small
96	\setlength{\tabcolsep}{3pt}
97	\begin{tabular}{llccccc}
98	\toprule
99	\textbf{Seed} & \textbf{Cond.} & \textbf{PR\%} & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} \\
100	\midrule
101	s42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\
102	s43 & ISR & 61 & 0.830 & \textbf{96.7} & 0 & 3.3 \\
103	s44 & ISR & 89 & 0.902 & \textbf{86.5} & 0 & 13.5$^\dagger$ \\
104	\cmidrule{1-7}
105	 & mean$\pm$std & 77$\pm$14 & --- & 64.5 & 17.3 & ${\sim}$16 \\
106	\midrule
107	s42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\
108	s43 & Rand & 88 & 0.058 & 0 & \textbf{93.2} & 6.8 \\
109	s44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\
110	\cmidrule{1-7}
111	 & mean$\pm$std & 85$\pm$6 & 0.086$\pm$.039 & 0 & 81.3$\pm$11 & 18.7$\pm$11 \\
112	\bottomrule
113	\end{tabular}
114	\caption{ISR vs Random at $\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\% vs 0\%). H1 is GRPO-universal, higher under random (81.3\%) than ISR (17.3\%)---ISR converts H1 into H7. $^\dagger$s44's 12 ``genuine'' samples all have $n_{\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\times$.}
115	\label{tab:beta01-3seed}
116	\end{table}
117	
118	Table~\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\% under random reward and 0--51.9\% under ISR. ISR reward does not reduce total hacking---it \emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\% vs Random s42: 70.9\%), and the random control achieves higher and more stable PR (85$\pm$6\% vs 77$\pm$14\%).
119	
120	\paragraph{Premise-count confound.}
121	Seed~42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each is more likely to appear necessary, inflating ISR independent of reasoning quality.
122	
123	To control for this, we compare ISR values only among genuine (non-hacking) samples with $\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$), a ratio of 1.06$\times$---no meaningful structural advantage. Of ISR s42's 25 nominal ``genuine'' samples, 15 have only 1--2 premises, where ISR$\geq$0.5 is a mathematical artifact of LOO on short inputs. The raw 2.4$\times$ ISR difference reduces to noise once premise count is controlled.
124	
125	\paragraph{High-dose ISR ($\beta{=}0.3$): classic Goodhart.}
126	At $\beta{=}0.3$, ISR reward causes PR to collapse to 18\%---a 5.2$\times$ degradation from exec-only. The matched random control achieves PR${=}$48\%, a 2.7$\times$ advantage, demonstrating that ISR at high dose is not merely unhelpful but \emph{actively harmful} relative to a structurally uninformative signal.
127	
128	\paragraph{Dose-response pattern.}
129	Together, the two dose levels reveal a complete Goodhart trajectory~\citep{karwowski-goodhart-rl, gao-reward-overoptimization}: at low dose ($\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.
130	
131	\subsection{Cross-Logic Diagnostic Transfer}
132	\label{sec:crosslogic}
133	
134	To test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.
135	
136	\begin{figure}[t]
137	\centering
138	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
139	\caption{Cross-logic ISR and Prolog STA gaming breakdown. \textbf{(a)}~Exec-only ISR is near-zero in both FOL and Prolog, confirming cross-logic diagnostic transfer. Seed~44 FOL ($\dagger$tautological) and seed~43 FOL ($\ddagger$sampling eval) are annotated. \textbf{(b)}~Prolog STA (ISR-as-reward) produces universal Goodhart: 3/3 seeds converge to gaming via distinct mechanisms---conclusion duplication, degenerate syntax, and query-as-fact---with 0\% genuine proofs.}
140	\label{fig:prolog-comparison}
141	\end{figure}
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\setlength{\tabcolsep}{3pt}
147	\begin{tabular}{llcccc}
148	\toprule
149	\textbf{Logic} & \textbf{Condition} & \textbf{Seed} & \textbf{PR\%} & \textbf{ISR}$^*$ & \textbf{Mode} \\
150	\midrule
151	\multicolumn{6}{l}{\textit{Exec-only (diagnostic transfer)}} \\
152	FOL & Exec & s42 & 93 & 0.132 & H1 embedding \\
153	FOL & Exec & s43$^\dagger$ & 14 & 0.000 & Repetition \\
154	FOL & Exec & s44 & 98 & 0.582$^\ddagger$ & Tautological \\
155	\cmidrule{1-6}
156	Prolog & Exec & s42 & 83 & 0.037 & Ground facts \\
157	Prolog & Exec & s43 & 56 & 0.015 & Degraded \\
158	Prolog & Exec & s44 & 21 & 0.387$^\S$ & Degraded \\
159	\midrule
160	\multicolumn{6}{l}{\textit{ISR-as-reward (Goodhart transfer)}} \\
161	Prolog & STA & s42 & 50 & 1.000$^\|$ & H7 100\% \\
162	Prolog & STA & s43 & 38 & 0.185$^\|$ & Degen.\ syntax$^\P$ \\
163	Prolog & STA & s44 & 97 & 0.912$^\|$ & Query-as-fact$^\#$ \\
164	\bottomrule
165	\end{tabular}
166	\caption{Cross-logic transfer (proved-only ISR$^*$). \textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\% genuine). $^\dagger$Sampling eval ($T{=}0.7$); not strictly comparable with greedy-decoded results. $^\ddagger$2-component artifact. $^\S$Small-sample ($n{=}$21). $^\|$Gaming-inflated. $^\P$Uppercase pseudo-Prolog; $n_{\text{nec}}{=}1$ for 38/38. $^\#$NL$\to$snake\_case atom as fact+query; $n_{\text{nec}}{=}1$ for 95/97.}
167	\label{tab:prolog-crosslogic}
168	\end{table}
169	
170	\paragraph{Diagnostic transfer.}
171	Table~\ref{tab:prolog-crosslogic} (top) and Figure~\ref{fig:prolog-comparison}(a) show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\sigma{=}$47pp) replicates in Prolog ($\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.
172	
173	We note an important semantic distinction: low ISR in Prolog exec-only reflects \emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \emph{metric gaming}. ISR must be interpreted relative to the training objective.
174	
175	\paragraph{Universal Goodhart in Prolog.}
176	Table~\ref{tab:prolog-crosslogic} (bottom) and Figure~\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:
177	\begin{itemize}[nosep,leftmargin=*]
178	  \item \textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).
179	  \item \textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \texttt{MARY\_IS\_AN\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "da9b10af-3fa0-412c-974a-045ef9c09428",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "Random & $r_e(1{+}\\beta{\\cdot}U)$ & 0.1 & 3 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.039} & 0 & 81 & 19 & H1 embedding \\\\\n\\midrule\nISR & $r_e(1{+}\\beta{\\cdot}\\text{ISR})$ & 0.3 & 1 & 18 & 0.143 & --- & --- & --- & PR collapse \\\\\nRandom & $r_e(1{+}\\beta{\\cdot}U)$ & 0.3 & 1 & 48 & 0.094 & --- & --- & --- & Redundant \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); per-seed ISR in Table~\\ref{tab:beta01-3seed}. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\ns42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\\ns43 & ISR & 61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\\ns44 & ISR & 89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 77$\\pm$14 & --- & 64.5 & 17.3 & ${\\sim}$16 \\\\\n\\midrule\ns42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\\\\ns43 & Rand & 88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\\ns44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 85$\\pm$6 & 0.086$\\pm$.039 & 0 & 81.3$\\pm$11 & 18.7$\\pm$11 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ISR vs Random at $\\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\\% vs 0\\%). H1 is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%)---ISR converts H1 into H7. $^\\dagger$s44's 12 ``genuine'' samples all have $n_{\\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\\times$.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\nTable~\\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).\n\n\\paragraph{Premise-count confound.}\nSeed~42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each is more likely to appear necessary, inflating ISR independent of reasoning quality.\n\nTo control for this, we compare ISR values only among genuine (non-hacking) samples with $\\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$), a ratio of 1.06$\\times$---no meaningful structural advantage. Of ISR s42's 25 nominal ``genuine'' samples, 15 have only 1--2 premises, where ISR$\\geq$0.5 is a mathematical artifact of LOO on short inputs. The raw 2.4$\\times$ ISR difference reduces to noise once premise count is controlled.\n\n\\paragraph{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR reward causes PR to collapse to 18\\%---a 5.2$\\times$ degradation from exec-only. The matched random control achieves PR${=}$48\\%, a 2.7$\\times$ advantage, demonstrating that ISR at high dose is not merely unhelpful but \\emph{actively harmful} relative to a structurally uninformative signal.\n\n\\paragraph{Dose-response pattern.}\nTogether, the two dose levels reveal a complete Goodhart trajectory~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization}: at low dose ($\\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nTo test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic ISR and Prolog STA gaming breakdown. \\textbf{(a)}~Exec-only ISR is near-zero in both FOL and Prolog, confirming cross-logic diagnostic transfer. Seed~44 FOL ($\\dagger$tautological) and seed~43 FOL ($\\ddagger$sampling eval) are annotated. \\textbf{(b)}~Prolog STA (ISR-as-reward) produces universal Goodhart: 3/3 seeds converge to gaming via distinct mechanisms---conclusion duplication, degenerate syntax, and query-as-fact---with 0\\% genuine proofs.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43$^\\dagger$ & 14 & 0.000 & Repetition \\\\\nFOL & Exec & s44 & 98 & 0.582$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 83 & 0.037 & Ground facts \\\\\nProlog & Exec & s43 & 56 & 0.015 & Degraded \\\\\nProlog & Exec & s44 & 21 & 0.387$^\\S$ & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 50 & 1.000$^\\|$ & H7 100\\% \\\\\nProlog & STA & s43 & 38 & 0.185$^\\|$ & Degen.\\ syntax$^\\P$ \\\\\nProlog & STA & s44 & 97 & 0.912$^\\|$ & Query-as-fact$^\\#$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer (proved-only ISR$^*$). \\textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \\textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\\% genuine). $^\\dagger$Sampling eval ($T{=}0.7$); not strictly comparable with greedy-decoded results. $^\\ddagger$2-component artifact. $^\\S$Small-sample ($n{=}$21). $^\\|$Gaming-inflated. $^\\P$Uppercase pseudo-Prolog; $n_{\\text{nec}}{=}1$ for 38/38. $^\\#$NL$\\to$snake\\_case atom as fact+query; $n_{\\text{nec}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\paragraph{Diagnostic transfer.}\nTable~\\ref{tab:prolog-crosslogic} (top) and Figure~\\ref{fig:prolog-comparison}(a) show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\\sigma{=}$47pp) replicates in Prolog ($\\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.\n\nWe note an important semantic distinction: low ISR in Prolog exec-only reflects \\emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \\emph{metric gaming}. ISR must be interpreted relative to the training objective.\n\n\\paragraph{Universal Goodhart in Prolog.}\nTable~\\ref{tab:prolog-crosslogic} (bottom) and Figure~\\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).\n  \\item \\textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).",
      "numLines": 100,
      "startLine": 80,
      "totalLines": 231
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "87f199cb-3028-4528-a9a9-7976e9568eb8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TP1nPPNoT6FXWPtpiSfFk6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4980,
      "cache_read_input_tokens": 68003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4980
      },
      "output_tokens": 41,
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

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01SisJY5Lxf218W2HbCzUtjW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); per-seed ISR in Table~\\ref{tab:beta01-3seed}. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\ns42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\\ns43 & ISR & 61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\\ns44 & ISR & 89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 77$\\pm$14 & --- & 64.5 & 17.3 & ${\\sim}$16 \\\\\n\\midrule\ns42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\\\\ns43 & Rand & 88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\\ns44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 85$\\pm$6 & 0.086$\\pm$.039 & 0 & 81.3$\\pm$11 & 18.7$\\pm$11 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ISR vs Random at $\\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\\% vs 0\\%). H1 is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%)---ISR converts H1 into H7. $^\\dagger$s44's 12 ``genuine'' samples all have $n_{\\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\\times$.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\nTable~\\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).",
  "new_string": "\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); see Appendix Table~\\ref{tab:beta01-3seed} for per-seed breakdown. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.\n\nConclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR (see Appendix Table~\\ref{tab:beta01-3seed} for per-seed breakdown). ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "a962412c-bd8d-4baa-ade6-d5e7802628c9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TP1nPPNoT6FXWPtpiSfFk6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4980,
      "cache_read_input_tokens": 68003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4980
      },
      "output_tokens": 41,
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

_source line 25 · 2026-05-14T20:03:31.355Z_

<details><summary>↩ Tool result · `toolu_01SisJY5Lxf218W2HbCzUtjW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "247113c1-436f-46f0-b5a3-5eb5e9ee256a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); per-seed ISR in Table~\\ref{tab:beta01-3seed}. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\ns42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\\ns43 & ISR & 61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\\ns44 & ISR & 89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 77$\\pm$14 & --- & 64.5 & 17.3 & ${\\sim}$16 \\\\\n\\midrule\ns42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\\\\ns43 & Rand & 88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\\ns44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 85$\\pm$6 & 0.086$\\pm$.039 & 0 & 81.3$\\pm$11 & 18.7$\\pm$11 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ISR vs Random at $\\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\\% vs 0\\%). H1 is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%)---ISR converts H1 into H7. $^\\dagger$s44's 12 ``genuine'' samples all have $n_{\\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\\times$.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\nTable~\\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).",
    "newString": "\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); see Appendix Table~\\ref{tab:beta01-3seed} for per-seed breakdown. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.\n\nConclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR (see Appendix Table~\\ref{tab:beta01-3seed} for per-seed breakdown). ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\\S\\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\\S\\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Model and training.}\nWe use Qwen3-4B as the base model, trained with GRPO~\\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of FOLIO~\\citep{folio} (\\texttt{train\\_500\\_seed42.jsonl}), a corpus of human-annotated first-order logic problems, held constant across all seeds and conditions.\n\n\\paragraph{Solvers and logic types.}\nFor first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\\text{exec}} \\in \\{0, 1\\}$ is binary: 1 if the solver returns a proof, 0 otherwise.\n\n\\paragraph{Evaluation.}\nWe evaluate on a held-out set of 100 FOLIO examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \\texttt{eval\\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), proved-only ISR (ISR$^*$, computed over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant. All tabulated ISR values are proved-only unless otherwise noted.\n\n\\paragraph{Reward formulations.}\nWe compare six conditions:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Exec-only}: $r = r_{\\text{exec}}$ (baseline)\n  \\item \\textbf{ISR $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$, with $\\beta \\in \\{0.1, 0.3\\}$\n  \\item \\textbf{Random $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$, $u \\sim \\mathcal{U}(0,1)$, matching ISR's range but providing no structural signal\n  \\item \\textbf{SFT}: Standard supervised fine-tuning on gold formalizations (no RL)\n\\end{itemize}\n\n\\paragraph{Output classification.}\nWe classify proved outputs into three categories: \\textbf{H7} (single-premise tautology where the sole premise equals the conclusion), \\textbf{H1} (multi-premise conclusion embedding where the conclusion appears among the premises), and \\textbf{Genuine} (no conclusion duplication detected). Classification uses text matching cross-validated with functional analysis of the LOO necessity distribution ($n_{\\text{necessary}}$).\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse trajectory under exec-only GRPO (seed~42). PR rises from 32\\% to 96\\% while proved-only ISR falls from 0.642 to 0.003 over 1000 steps. By step~1000, 94.8\\% of proved samples have ISR${=}$0. Component count inflates from 6.58 to 18.55, indicating contradiction explosion.}\n\\label{fig:isr-collapse}\n\\end{figure}\n\nWe first establish that ISR detects structural degeneration invisible to prove rate.\nFigure~\\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).\nAt 100 steps, the model produces structurally sound formalizations: PR${=}$32\\%, proved-only ISR${=}$0.642.\nBy 500 steps, PR reaches 93\\% but ISR collapses to 0.132---87.1\\% of proved samples embed the conclusion among the premises (H1), making proof trivially achievable.\nAt 1000 steps, PR${=}$96\\% while ISR drops to 0.003: every proved sample contains the conclusion in its premises (H1${=}$100\\%), and the mean component count rises from 6.58 to 18.55.\nThe model generates excessive premises that trivially entail any conclusion via contradiction explosion.\nThe ISR trajectory (0.642 $\\to$ 0.132 $\\to$ 0.003) is monotonically decreasing with no recovery signal: extended training worsens structural degeneration.\n\n\\paragraph{Cross-seed instability.}\nThe three exec-only seeds diverge radically, underscoring that single-seed evaluation is unreliable for GRPO-trained formalizers.\nSeed~42 achieves PR${=}$93\\% via conclusion embedding (H1${=}$87.1\\%).\nSeed~43 collapses to PR${=}$14\\% with ISR${=}$0.000 through repetition collapse---87\\% of outputs hit the maximum token length.\nSeed~44 reaches PR${=}$98\\% but through tautological collapse: the model generates two-component formalizations where the sole premise equals the conclusion (H7${=}$100\\%, mean components${=}$2.04).\nDespite PR values ranging from 14\\% to 98\\%, all three seeds exhibit structural degeneration detectable by ISR.\nThe cross-seed PR standard deviation ($\\pm$47 percentage points) is itself a finding: GRPO exec-only training is highly unstable, and aggregate metrics obscure qualitatively different failure modes.\n\n\\paragraph{SFT baseline.}\nTo confirm that hacking is RL-specific, we train a supervised baseline on gold formalizations.\nSFT achieves PR${=}$14\\% with proved-only ISR${=}$0.571: 92.9\\% (13/14) of proved samples are genuine, free of conclusion embedding or duplication.\nOnly 1 of 14 proved samples exhibits H1 (7.1\\%), and no H7 instances occur.\nThe near-absence of hacking confirms that the structural degeneration documented above is a consequence of RL reward optimization, not model capacity or data limitations.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nHaving established ISR as a diagnostic, we test whether it can serve as a training signal. The answer is negative: ISR-as-reward exhibits \\emph{meta-level} Goodhart's Law~\\citep{manheim-goodhart-taxonomy}---the diagnostic metric itself becomes the target of gaming when optimized.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{llcccccccl}\n\\toprule\n\\textbf{Condition} & \\textbf{Reward} & $\\boldsymbol{\\beta}$ & $\\boldsymbol{n}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Mode} \\\\\n\\midrule\nBase (0-shot) & --- & --- & 1 & 12 & --- & --- & --- & --- & --- \\\\\nSFT & supervised & --- & 1 & 14 & 0.571 & 0 & 7 & \\textbf{93} & Genuine \\\\\n\\midrule\nExec-only & $r_e$ & --- & 1$^\\dagger$ & 93 & 0.132 & 0 & 87 & 13 & H1 embedding \\\\\nISR & $r_e(1{+}\\beta{\\cdot}\\text{ISR})$ & 0.1 & 3 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{65} & 17 & ${\\sim}$16 & H7 gaming \\\\\nRandom & $r_e(1{+}\\beta{\\cdot}U)$ & 0.1 & 3 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.039} & 0 & 81 & 19 & H1 embedding \\\\\n\\midrule\nISR & $r_e(1{+}\\beta{\\cdot}\\text{ISR})$ & 0.3 & 1 & 18 & 0.143 & --- & --- & --- & PR collapse \\\\\nRandom & $r_e(1{+}\\beta{\\cdot}U)$ & 0.3 & 1 & 48 & 0.094 & --- & --- & --- & Redundant \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); per-seed ISR in Table~\\ref{tab:beta01-3seed}. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\ns42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\\ns43 & ISR & 61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\\ns44 & ISR & 89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 77$\\pm$14 & --- & 64.5 & 17.3 & ${\\sim}$16 \\\\\n\\midrule\ns42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\\\\ns43 & Rand & 88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\\ns44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 85$\\pm$6 & 0.086$\\pm$.039 & 0 & 81.3$\\pm$11 & 18.7$\\pm$11 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ISR vs Random at $\\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\\% vs 0\\%). H1 is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%)---ISR converts H1 into H7. $^\\dagger$s44's 12 ``genuine'' samples all have $n_{\\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\\times$.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\nTable~\\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).\n\n\\paragraph{Premise-count confound.}\nSeed~42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each is more likely to appear necessary, inflating ISR independent of reasoning quality.\n\nTo control for this, we compare ISR values only among genuine (non-hacking) samples with $\\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$), a ratio of 1.06$\\times$---no meaningful structural advantage. Of ISR s42's 25 nominal ``genuine'' samples, 15 have only 1--2 premises, where ISR$\\geq$0.5 is a mathematical artifact of LOO on short inputs. The raw 2.4$\\times$ ISR difference reduces to noise once premise count is controlled.\n\n\\paragraph{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR reward causes PR to collapse to 18\\%---a 5.2$\\times$ degradation from exec-only. The matched random control achieves PR${=}$48\\%, a 2.7$\\times$ advantage, demonstrating that ISR at high dose is not merely unhelpful but \\emph{actively harmful} relative to a structurally uninformative signal.\n\n\\paragraph{Dose-response pattern.}\nTogether, the two dose levels reveal a complete Goodhart trajectory~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization}: at low dose ($\\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nTo test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic ISR and Prolog STA gaming breakdown. \\textbf{(a)}~Exec-only ISR is near-zero in both FOL and Prolog, confirming cross-logic diagnostic transfer. Seed~44 FOL ($\\dagger$tautological) and seed~43 FOL ($\\ddagger$sampling eval) are annotated. \\textbf{(b)}~Prolog STA (ISR-as-reward) produces universal Goodhart: 3/3 seeds converge to gaming via distinct mechanisms---conclusion duplication, degenerate syntax, and query-as-fact---with 0\\% genuine proofs.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43$^\\dagger$ & 14 & 0.000 & Repetition \\\\\nFOL & Exec & s44 & 98 & 0.582$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 83 & 0.037 & Ground facts \\\\\nProlog & Exec & s43 & 56 & 0.015 & Degraded \\\\\nProlog & Exec & s44 & 21 & 0.387$^\\S$ & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 50 & 1.000$^\\|$ & H7 100\\% \\\\\nProlog & STA & s43 & 38 & 0.185$^\\|$ & Degen.\\ syntax$^\\P$ \\\\\nProlog & STA & s44 & 97 & 0.912$^\\|$ & Query-as-fact$^\\#$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer (proved-only ISR$^*$). \\textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \\textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\\% genuine). $^\\dagger$Sampling eval ($T{=}0.7$); not strictly comparable with greedy-decoded results. $^\\ddagger$2-component artifact. $^\\S$Small-sample ($n{=}$21). $^\\|$Gaming-inflated. $^\\P$Uppercase pseudo-Prolog; $n_{\\text{nec}}{=}1$ for 38/38. $^\\#$NL$\\to$snake\\_case atom as fact+query; $n_{\\text{nec}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\paragraph{Diagnostic transfer.}\nTable~\\ref{tab:prolog-crosslogic} (top) and Figure~\\ref{fig:prolog-comparison}(a) show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\\sigma{=}$47pp) replicates in Prolog ($\\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.\n\nWe note an important semantic distinction: low ISR in Prolog exec-only reflects \\emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \\emph{metric gaming}. ISR must be interpreted relative to the training objective.\n\n\\paragraph{Universal Goodhart in Prolog.}\nTable~\\ref{tab:prolog-crosslogic} (bottom) and Figure~\\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).\n  \\item \\textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).\n  \\item \\textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\\_case atoms and sets them as both fact and query, achieving PR${=}$97\\% with $n_{\\text{necessary}}{=}1$ for 95/97. Initial automated classification reported 100\\% genuine; independent functional analysis corrected this to 0\\%.\n\\end{itemize}\nThis result is stronger than the FOL finding: FOL ISR $\\beta{=}0.1$ retains ${\\sim}$16\\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics enable more complete exploitation, eliminating the genuine residual observed in FOL.\n\n\\paragraph{Classifier limitations.}\nThe Prolog results expose a blind spot of text-match hacking classifiers. Seeds~s43 and s44 bypass the strict H7/H1 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\\text{necessary}}$ distribution.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking prevalence. SFT exhibits near-zero hacking (92.9\\% genuine).}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{p{1.6cm}p{2.0cm}cccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rand} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ among premises & 87 & 17 & 81 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{65} & 0 & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & --- & --- & --- \\\\\nContradiction & $n_{\\text{comp}}{\\uparrow}$, ISR${\\to}$0 & $\\bullet$ & --- & --- & --- \\\\\nC-w/o-util. & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed means. Exec: H1${=}$87\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nAcross all conditions, seeds, and logic types, we identify seven distinct hacking modes (Table~\\ref{tab:hacking-taxonomy}, Figure~\\ref{fig:hacking-composition}):\n\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{H1: Conclusion embedding.} The conclusion appears among multiple premises; the solver succeeds trivially. Conclusion embedding in some form (H1 or H7) is GRPO-universal at 68--97\\% across all RL conditions.\n  \\item \\textbf{H7: Conclusion duplication.} A single premise identical to the conclusion. ISR-specific: 64.5\\% under ISR $\\beta{=}0.1$ vs 0\\% under random.\n  \\item \\textbf{Tautological collapse.} Two-component formalizations where premise${=}$conclusion (exec-only s44, 94\\% of outputs, mean components${=}$2.04).\n  \\item \\textbf{Repetition collapse.} Identical premises repeated until the token limit (exec-only s43, 87\\% hit max length).\n  \\item \\textbf{Contradiction explosion.} Excessive premises (mean 18.55 components at 1000 steps) that trivially entail any conclusion via embedded contradictions.\n  \\item \\textbf{Complexity-without-utility.} Syntactically complex but semantically vacuous premises (random $\\beta{=}0.1$, 3.8\\%).\n  \\item \\textbf{Query-as-fact gaming.} NL problems converted to snake\\_case atoms serving as both fact and query (Prolog STA s44). Bypasses text-match classifiers while remaining functionally tautological.\n\\end{enumerate}\n\nThe reward signal determines hacking \\emph{composition} but not \\emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random conditions (${\\sim}$82\\% pooled across seeds), but ISR converts the GRPO-universal H1 mode into the ISR-specific H7 mode. SFT remains the only condition with near-zero hacking (92.9\\% genuine), confirming that hacking is RL-reward-specific. Different reward formulations produce characteristic hacking signatures---a finding that may inform future diagnostic design.\n",
    "structuredPatch": [
      {
        "oldStart": 83,
        "oldLines": 40,
        "newStart": 83,
        "newLines": 15,
        "lines": [
          " Random & $r_e(1{+}\\beta{\\cdot}U)$ & 0.3 & 1 & 48 & 0.094 & --- & --- & --- & Redundant \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); per-seed ISR in Table~\\ref{tab:beta01-3seed}. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}",
          "+\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); see Appendix Table~\\ref{tab:beta01-3seed} for per-seed breakdown. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}",
          " \\label{tab:goodhart-landscape}",
          " \\end{table*}",
          " ",
          " \\paragraph{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}",
          " Table~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.",
          " ",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\small",
          "-\\setlength{\\tabcolsep}{3pt}",
          "-\\begin{tabular}{llccccc}",
          "-\\toprule",
          "-\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\",
          "-\\midrule",
          "-s42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\",
          "-s43 & ISR & 61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\",
          "-s44 & ISR & 89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\",
          "-\\cmidrule{1-7}",
          "- & mean$\\pm$std & 77$\\pm$14 & --- & 64.5 & 17.3 & ${\\sim}$16 \\\\",
          "-\\midrule",
          "-s42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\\\",
          "-s43 & Rand & 88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\",
          "-s44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\\\",
          "-\\cmidrule{1-7}",
          "- & mean$\\pm$std & 85$\\pm$6 & 0.086$\\pm$.039 & 0 & 81.3$\\pm$11 & 18.7$\\pm$11 \\\\",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\caption{ISR vs Random at $\\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\\% vs 0\\%). H1 is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%)---ISR converts H1 into H7. $^\\dagger$s44's 12 ``genuine'' samples all have $n_{\\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\\times$.}",
          "-\\label{tab:beta01-3seed}",
          "-\\end{table}",
          "+Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR (see Appendix Table~\\ref{tab:beta01-3seed} for per-seed breakdown). ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).",
          " ",
          "-Table~\\ref{tab:beta01-3seed} provides the full per-seed breakdown. Conclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR. ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).",
          "-",
          " \\paragraph{Premise-count confound.}",
          " Seed~42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each is more likely to appear necessary, inflating ISR independent of reasoning quality.",
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

_source line 26_

Now compress §4.4 (Cross-Logic Diagnostic Transfer) — remove fig and table, condense to one paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "7a9922b6-3961-4fd1-8939-144d25b8ae40",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011h371AnND3hs9ZEjRx5uQ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2730,
      "cache_read_input_tokens": 72983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2730
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_018d3nYcSKDKSWcFFdBrRqeu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nTo test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic ISR and Prolog STA gaming breakdown. \\textbf{(a)}~Exec-only ISR is near-zero in both FOL and Prolog, confirming cross-logic diagnostic transfer. Seed~44 FOL ($\\dagger$tautological) and seed~43 FOL ($\\ddagger$sampling eval) are annotated. \\textbf{(b)}~Prolog STA (ISR-as-reward) produces universal Goodhart: 3/3 seeds converge to gaming via distinct mechanisms---conclusion duplication, degenerate syntax, and query-as-fact---with 0\\% genuine proofs.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43$^\\dagger$ & 14 & 0.000 & Repetition \\\\\nFOL & Exec & s44 & 98 & 0.582$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 83 & 0.037 & Ground facts \\\\\nProlog & Exec & s43 & 56 & 0.015 & Degraded \\\\\nProlog & Exec & s44 & 21 & 0.387$^\\S$ & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 50 & 1.000$^\\|$ & H7 100\\% \\\\\nProlog & STA & s43 & 38 & 0.185$^\\|$ & Degen.\\ syntax$^\\P$ \\\\\nProlog & STA & s44 & 97 & 0.912$^\\|$ & Query-as-fact$^\\#$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer (proved-only ISR$^*$). \\textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \\textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\\% genuine). $^\\dagger$Sampling eval ($T{=}0.7$); not strictly comparable with greedy-decoded results. $^\\ddagger$2-component artifact. $^\\S$Small-sample ($n{=}$21). $^\\|$Gaming-inflated. $^\\P$Uppercase pseudo-Prolog; $n_{\\text{nec}}{=}1$ for 38/38. $^\\#$NL$\\to$snake\\_case atom as fact+query; $n_{\\text{nec}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\paragraph{Diagnostic transfer.}\nTable~\\ref{tab:prolog-crosslogic} (top) and Figure~\\ref{fig:prolog-comparison}(a) show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\\sigma{=}$47pp) replicates in Prolog ($\\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.\n\nWe note an important semantic distinction: low ISR in Prolog exec-only reflects \\emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \\emph{metric gaming}. ISR must be interpreted relative to the training objective.\n\n\\paragraph{Universal Goodhart in Prolog.}\nTable~\\ref{tab:prolog-crosslogic} (bottom) and Figure~\\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).\n  \\item \\textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).\n  \\item \\textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\\_case atoms and sets them as both fact and query, achieving PR${=}$97\\% with $n_{\\text{necessary}}{=}1$ for 95/97. Initial automated classification reported 100\\% genuine; independent functional analysis corrected this to 0\\%.\n\\end{itemize}\nThis result is stronger than the FOL finding: FOL ISR $\\beta{=}0.1$ retains ${\\sim}$16\\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics enable more complete exploitation, eliminating the genuine residual observed in FOL.\n\n\\paragraph{Classifier limitations.}\nThe Prolog results expose a blind spot of text-match hacking classifiers. Seeds~s43 and s44 bypass the strict H7/H1 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\\text{necessary}}$ distribution.",
  "new_string": "\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nAs preliminary evidence that ISR generalizes beyond a single formal language, we replicated both the diagnostic and reward experiments using SWI-Prolog 8.4.2 as the solver (full results in Appendix Figure~\\ref{fig:prolog-comparison} and Appendix Table~\\ref{tab:prolog-crosslogic}). Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming diagnostic transfer despite moderate-to-high PR; we note that low ISR here reflects \\emph{redundant coding}---repeated ground facts where removing any single copy leaves the proof intact---rather than absence of reasoning, contrasting with the metric-gaming high ISR under Prolog STA. With ISR added as a Prolog reward, all three STA seeds converge to gaming with 0\\% genuine across 185 proved samples (universal Goodhart, stronger than the FOL ${\\sim}$16\\% genuine residual): s42 produces clean H7 tautologies (50/50, ISR$^*{=}$1.000), s43 generates uppercase pseudo-Prolog that bypasses text-match classifiers but is functionally H7 ($n_{\\text{nec}}{=}1$ for 38/38), and s44 develops query-as-fact gaming where NL is converted to snake\\_case atoms used as both fact and query (ISR$^*{=}$0.912, $n_{\\text{nec}}{=}1$ for 95/97). These results suggest that simpler formal semantics enable more complete exploitation, and motivate cross-validation of hacking classifiers with functional metrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "4b3f48da-8493-4680-be2d-6e86bcdca50a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011h371AnND3hs9ZEjRx5uQ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2730,
      "cache_read_input_tokens": 72983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2730
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

_source line 28 · 2026-05-14T20:04:25.231Z_

<details><summary>↩ Tool result · `toolu_018d3nYcSKDKSWcFFdBrRqeu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "e53e19e0-0f00-4e8e-9de7-5cdaf046fa43",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nTo test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic ISR and Prolog STA gaming breakdown. \\textbf{(a)}~Exec-only ISR is near-zero in both FOL and Prolog, confirming cross-logic diagnostic transfer. Seed~44 FOL ($\\dagger$tautological) and seed~43 FOL ($\\ddagger$sampling eval) are annotated. \\textbf{(b)}~Prolog STA (ISR-as-reward) produces universal Goodhart: 3/3 seeds converge to gaming via distinct mechanisms---conclusion duplication, degenerate syntax, and query-as-fact---with 0\\% genuine proofs.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43$^\\dagger$ & 14 & 0.000 & Repetition \\\\\nFOL & Exec & s44 & 98 & 0.582$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 83 & 0.037 & Ground facts \\\\\nProlog & Exec & s43 & 56 & 0.015 & Degraded \\\\\nProlog & Exec & s44 & 21 & 0.387$^\\S$ & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 50 & 1.000$^\\|$ & H7 100\\% \\\\\nProlog & STA & s43 & 38 & 0.185$^\\|$ & Degen.\\ syntax$^\\P$ \\\\\nProlog & STA & s44 & 97 & 0.912$^\\|$ & Query-as-fact$^\\#$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer (proved-only ISR$^*$). \\textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \\textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\\% genuine). $^\\dagger$Sampling eval ($T{=}0.7$); not strictly comparable with greedy-decoded results. $^\\ddagger$2-component artifact. $^\\S$Small-sample ($n{=}$21). $^\\|$Gaming-inflated. $^\\P$Uppercase pseudo-Prolog; $n_{\\text{nec}}{=}1$ for 38/38. $^\\#$NL$\\to$snake\\_case atom as fact+query; $n_{\\text{nec}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\paragraph{Diagnostic transfer.}\nTable~\\ref{tab:prolog-crosslogic} (top) and Figure~\\ref{fig:prolog-comparison}(a) show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\\sigma{=}$47pp) replicates in Prolog ($\\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.\n\nWe note an important semantic distinction: low ISR in Prolog exec-only reflects \\emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \\emph{metric gaming}. ISR must be interpreted relative to the training objective.\n\n\\paragraph{Universal Goodhart in Prolog.}\nTable~\\ref{tab:prolog-crosslogic} (bottom) and Figure~\\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).\n  \\item \\textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).\n  \\item \\textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\\_case atoms and sets them as both fact and query, achieving PR${=}$97\\% with $n_{\\text{necessary}}{=}1$ for 95/97. Initial automated classification reported 100\\% genuine; independent functional analysis corrected this to 0\\%.\n\\end{itemize}\nThis result is stronger than the FOL finding: FOL ISR $\\beta{=}0.1$ retains ${\\sim}$16\\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics enable more complete exploitation, eliminating the genuine residual observed in FOL.\n\n\\paragraph{Classifier limitations.}\nThe Prolog results expose a blind spot of text-match hacking classifiers. Seeds~s43 and s44 bypass the strict H7/H1 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\\text{necessary}}$ distribution.",
    "newString": "\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nAs preliminary evidence that ISR generalizes beyond a single formal language, we replicated both the diagnostic and reward experiments using SWI-Prolog 8.4.2 as the solver (full results in Appendix Figure~\\ref{fig:prolog-comparison} and Appendix Table~\\ref{tab:prolog-crosslogic}). Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming diagnostic transfer despite moderate-to-high PR; we note that low ISR here reflects \\emph{redundant coding}---repeated ground facts where removing any single copy leaves the proof intact---rather than absence of reasoning, contrasting with the metric-gaming high ISR under Prolog STA. With ISR added as a Prolog reward, all three STA seeds converge to gaming with 0\\% genuine across 185 proved samples (universal Goodhart, stronger than the FOL ${\\sim}$16\\% genuine residual): s42 produces clean H7 tautologies (50/50, ISR$^*{=}$1.000), s43 generates uppercase pseudo-Prolog that bypasses text-match classifiers but is functionally H7 ($n_{\\text{nec}}{=}1$ for 38/38), and s44 develops query-as-fact gaming where NL is converted to snake\\_case atoms used as both fact and query (ISR$^*{=}$0.912, $n_{\\text{nec}}{=}1$ for 95/97). These results suggest that simpler formal semantics enable more complete exploitation, and motivate cross-validation of hacking classifiers with functional metrics.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\\S\\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\\S\\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Model and training.}\nWe use Qwen3-4B as the base model, trained with GRPO~\\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of FOLIO~\\citep{folio} (\\texttt{train\\_500\\_seed42.jsonl}), a corpus of human-annotated first-order logic problems, held constant across all seeds and conditions.\n\n\\paragraph{Solvers and logic types.}\nFor first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\\text{exec}} \\in \\{0, 1\\}$ is binary: 1 if the solver returns a proof, 0 otherwise.\n\n\\paragraph{Evaluation.}\nWe evaluate on a held-out set of 100 FOLIO examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \\texttt{eval\\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), proved-only ISR (ISR$^*$, computed over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant. All tabulated ISR values are proved-only unless otherwise noted.\n\n\\paragraph{Reward formulations.}\nWe compare six conditions:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Exec-only}: $r = r_{\\text{exec}}$ (baseline)\n  \\item \\textbf{ISR $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$, with $\\beta \\in \\{0.1, 0.3\\}$\n  \\item \\textbf{Random $\\beta$}: $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u)$, $u \\sim \\mathcal{U}(0,1)$, matching ISR's range but providing no structural signal\n  \\item \\textbf{SFT}: Standard supervised fine-tuning on gold formalizations (no RL)\n\\end{itemize}\n\n\\paragraph{Output classification.}\nWe classify proved outputs into three categories: \\textbf{H7} (single-premise tautology where the sole premise equals the conclusion), \\textbf{H1} (multi-premise conclusion embedding where the conclusion appears among the premises), and \\textbf{Genuine} (no conclusion duplication detected). Classification uses text matching cross-validated with functional analysis of the LOO necessity distribution ($n_{\\text{necessary}}$).\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse trajectory under exec-only GRPO (seed~42). PR rises from 32\\% to 96\\% while proved-only ISR falls from 0.642 to 0.003 over 1000 steps. By step~1000, 94.8\\% of proved samples have ISR${=}$0. Component count inflates from 6.58 to 18.55, indicating contradiction explosion.}\n\\label{fig:isr-collapse}\n\\end{figure}\n\nWe first establish that ISR detects structural degeneration invisible to prove rate.\nFigure~\\ref{fig:isr-collapse} traces ISR and PR over training for exec-only GRPO (seed~42).\nAt 100 steps, the model produces structurally sound formalizations: PR${=}$32\\%, proved-only ISR${=}$0.642.\nBy 500 steps, PR reaches 93\\% but ISR collapses to 0.132---87.1\\% of proved samples embed the conclusion among the premises (H1), making proof trivially achievable.\nAt 1000 steps, PR${=}$96\\% while ISR drops to 0.003: every proved sample contains the conclusion in its premises (H1${=}$100\\%), and the mean component count rises from 6.58 to 18.55.\nThe model generates excessive premises that trivially entail any conclusion via contradiction explosion.\nThe ISR trajectory (0.642 $\\to$ 0.132 $\\to$ 0.003) is monotonically decreasing with no recovery signal: extended training worsens structural degeneration.\n\n\\paragraph{Cross-seed instability.}\nThe three exec-only seeds diverge radically, underscoring that single-seed evaluation is unreliable for GRPO-trained formalizers.\nSeed~42 achieves PR${=}$93\\% via conclusion embedding (H1${=}$87.1\\%).\nSeed~43 collapses to PR${=}$14\\% with ISR${=}$0.000 through repetition collapse---87\\% of outputs hit the maximum token length.\nSeed~44 reaches PR${=}$98\\% but through tautological collapse: the model generates two-component formalizations where the sole premise equals the conclusion (H7${=}$100\\%, mean components${=}$2.04).\nDespite PR values ranging from 14\\% to 98\\%, all three seeds exhibit structural degeneration detectable by ISR.\nThe cross-seed PR standard deviation ($\\pm$47 percentage points) is itself a finding: GRPO exec-only training is highly unstable, and aggregate metrics obscure qualitatively different failure modes.\n\n\\paragraph{SFT baseline.}\nTo confirm that hacking is RL-specific, we train a supervised baseline on gold formalizations.\nSFT achieves PR${=}$14\\% with proved-only ISR${=}$0.571: 92.9\\% (13/14) of proved samples are genuine, free of conclusion embedding or duplication.\nOnly 1 of 14 proved samples exhibits H1 (7.1\\%), and no H7 instances occur.\nThe near-absence of hacking confirms that the structural degeneration documented above is a consequence of RL reward optimization, not model capacity or data limitations.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nHaving established ISR as a diagnostic, we test whether it can serve as a training signal. The answer is negative: ISR-as-reward exhibits \\emph{meta-level} Goodhart's Law~\\citep{manheim-goodhart-taxonomy}---the diagnostic metric itself becomes the target of gaming when optimized.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{llcccccccl}\n\\toprule\n\\textbf{Condition} & \\textbf{Reward} & $\\boldsymbol{\\beta}$ & $\\boldsymbol{n}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Mode} \\\\\n\\midrule\nBase (0-shot) & --- & --- & 1 & 12 & --- & --- & --- & --- & --- \\\\\nSFT & supervised & --- & 1 & 14 & 0.571 & 0 & 7 & \\textbf{93} & Genuine \\\\\n\\midrule\nExec-only & $r_e$ & --- & 1$^\\dagger$ & 93 & 0.132 & 0 & 87 & 13 & H1 embedding \\\\\nISR & $r_e(1{+}\\beta{\\cdot}\\text{ISR})$ & 0.1 & 3 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{65} & 17 & ${\\sim}$16 & H7 gaming \\\\\nRandom & $r_e(1{+}\\beta{\\cdot}U)$ & 0.1 & 3 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.039} & 0 & 81 & 19 & H1 embedding \\\\\n\\midrule\nISR & $r_e(1{+}\\beta{\\cdot}\\text{ISR})$ & 0.3 & 1 & 18 & 0.143 & --- & --- & --- & PR collapse \\\\\nRandom & $r_e(1{+}\\beta{\\cdot}U)$ & 0.3 & 1 & 48 & 0.094 & --- & --- & --- & Redundant \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. $n$: number of seeds; 3-seed rows show mean$\\pm$std. ISR$^*$: proved-only. $U \\sim \\mathcal{U}(0,1)$; $r_e = r_{\\text{exec}}$. $^\\dagger$Seed~42 shown; see \\S\\ref{sec:diagnostic} for 3-seed divergence. $\\ddagger$ISR omitted: inflated by H7 gaming (64.5\\% of proved samples are single-premise tautologies); see Appendix Table~\\ref{tab:beta01-3seed} for per-seed breakdown. H7/H1/Gen.\\% unavailable for $\\beta{=}0.3$ (single seed, not fully classified). Best PR and Gen.\\% bolded per group.}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\paragraph{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nTable~\\ref{tab:goodhart-landscape} summarizes results across conditions. At $\\beta{=}0.1$, two of three ISR seeds (s43, s44) are dominated by H7---the model generates a single premise identical to the conclusion, trivially achieving both high PR and high ISR. Across the three ISR seeds, H7 accounts for 64.5\\% of proved samples (149/231). In contrast, all three random control seeds show \\emph{zero} H7 instances (0/256). H7 is exclusively induced by the ISR reward signal.\n\nConclusion embedding (H1) is a GRPO-universal strategy: it appears at 70.9--93.2\\% under random reward and 0--51.9\\% under ISR (see Appendix Table~\\ref{tab:beta01-3seed} for per-seed breakdown). ISR reward does not reduce total hacking---it \\emph{converts} H1 into the more extreme H7 form. Overall conclusion-in-premise rates are comparable (ISR s42: 67.9\\% vs Random s42: 70.9\\%), and the random control achieves higher and more stable PR (85$\\pm$6\\% vs 77$\\pm$14\\%).\n\n\\paragraph{Premise-count confound.}\nSeed~42 under ISR---the only seed not dominated by H7---shows higher raw proved-only ISR (0.415 vs 0.131 for random). However, this apparent advantage is entirely a premise minimization artifact. ISR-trained models produce shorter formalizations (mean 5.58 components vs 8.46 for random), and LOO-based metrics are mathematically biased by component count: fewer premises mean each is more likely to appear necessary, inflating ISR independent of reasoning quality.\n\nTo control for this, we compare ISR values only among genuine (non-hacking) samples with $\\geq$3 premises: ISR genuine achieves 0.258 ($n{=}11$) versus random genuine at 0.243 ($n{=}21$), a ratio of 1.06$\\times$---no meaningful structural advantage. Of ISR s42's 25 nominal ``genuine'' samples, 15 have only 1--2 premises, where ISR$\\geq$0.5 is a mathematical artifact of LOO on short inputs. The raw 2.4$\\times$ ISR difference reduces to noise once premise count is controlled.\n\n\\paragraph{High-dose ISR ($\\beta{=}0.3$): classic Goodhart.}\nAt $\\beta{=}0.3$, ISR reward causes PR to collapse to 18\\%---a 5.2$\\times$ degradation from exec-only. The matched random control achieves PR${=}$48\\%, a 2.7$\\times$ advantage, demonstrating that ISR at high dose is not merely unhelpful but \\emph{actively harmful} relative to a structurally uninformative signal.\n\n\\paragraph{Dose-response pattern.}\nTogether, the two dose levels reveal a complete Goodhart trajectory~\\citep{karwowski-goodhart-rl, gao-reward-overoptimization}: at low dose ($\\beta{=}0.1$), the model games the proxy metric itself (ISR inflation via H7), producing high ISR scores that mask structural degeneration; at high dose ($\\beta{=}0.3$), the ISR signal overwhelms the execution reward, causing format collapse and PR degradation. No dose yields genuine structural improvement.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nTo test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic ISR and Prolog STA gaming breakdown. \\textbf{(a)}~Exec-only ISR is near-zero in both FOL and Prolog, confirming cross-logic diagnostic transfer. Seed~44 FOL ($\\dagger$tautological) and seed~43 FOL ($\\ddagger$sampling eval) are annotated. \\textbf{(b)}~Prolog STA (ISR-as-reward) produces universal Goodhart: 3/3 seeds converge to gaming via distinct mechanisms---conclusion duplication, degenerate syntax, and query-as-fact---with 0\\% genuine proofs.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43$^\\dagger$ & 14 & 0.000 & Repetition \\\\\nFOL & Exec & s44 & 98 & 0.582$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 83 & 0.037 & Ground facts \\\\\nProlog & Exec & s43 & 56 & 0.015 & Degraded \\\\\nProlog & Exec & s44 & 21 & 0.387$^\\S$ & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 50 & 1.000$^\\|$ & H7 100\\% \\\\\nProlog & STA & s43 & 38 & 0.185$^\\|$ & Degen.\\ syntax$^\\P$ \\\\\nProlog & STA & s44 & 97 & 0.912$^\\|$ & Query-as-fact$^\\#$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer (proved-only ISR$^*$). \\textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \\textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\\% genuine). $^\\dagger$Sampling eval ($T{=}0.7$); not strictly comparable with greedy-decoded results. $^\\ddagger$2-component artifact. $^\\S$Small-sample ($n{=}$21). $^\\|$Gaming-inflated. $^\\P$Uppercase pseudo-Prolog; $n_{\\text{nec}}{=}1$ for 38/38. $^\\#$NL$\\to$snake\\_case atom as fact+query; $n_{\\text{nec}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\paragraph{Diagnostic transfer.}\nTable~\\ref{tab:prolog-crosslogic} (top) and Figure~\\ref{fig:prolog-comparison}(a) show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\\sigma{=}$47pp) replicates in Prolog ($\\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.\n\nWe note an important semantic distinction: low ISR in Prolog exec-only reflects \\emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \\emph{metric gaming}. ISR must be interpreted relative to the training objective.\n\n\\paragraph{Universal Goodhart in Prolog.}\nTable~\\ref{tab:prolog-crosslogic} (bottom) and Figure~\\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).\n  \\item \\textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).\n  \\item \\textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\\_case atoms and sets them as both fact and query, achieving PR${=}$97\\% with $n_{\\text{necessary}}{=}1$ for 95/97. Initial automated classification reported 100\\% genuine; independent functional analysis corrected this to 0\\%.\n\\end{itemize}\nThis result is stronger than the FOL finding: FOL ISR $\\beta{=}0.1$ retains ${\\sim}$16\\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics enable more complete exploitation, eliminating the genuine residual observed in FOL.\n\n\\paragraph{Classifier limitations.}\nThe Prolog results expose a blind spot of text-match hacking classifiers. Seeds~s43 and s44 bypass the strict H7/H1 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\\text{necessary}}$ distribution.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking mode composition across reward conditions (proved samples). ISR reward converts H1 (conclusion embedding) into the more extreme H7 (conclusion duplication) without reducing total hacking prevalence. SFT exhibits near-zero hacking (92.9\\% genuine).}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{p{1.6cm}p{2.0cm}cccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rand} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ among premises & 87 & 17 & 81 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{65} & 0 & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & --- & --- & --- \\\\\nContradiction & $n_{\\text{comp}}{\\uparrow}$, ISR${\\to}$0 & $\\bullet$ & --- & --- & --- \\\\\nC-w/o-util. & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed means. Exec: H1${=}$87\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000~steps). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nAcross all conditions, seeds, and logic types, we identify seven distinct hacking modes (Table~\\ref{tab:hacking-taxonomy}, Figure~\\ref{fig:hacking-composition}):\n\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{H1: Conclusion embedding.} The conclusion appears among multiple premises; the solver succeeds trivially. Conclusion embedding in some form (H1 or H7) is GRPO-universal at 68--97\\% across all RL conditions.\n  \\item \\textbf{H7: Conclusion duplication.} A single premise identical to the conclusion. ISR-specific: 64.5\\% under ISR $\\beta{=}0.1$ vs 0\\% under random.\n  \\item \\textbf{Tautological collapse.} Two-component formalizations where premise${=}$conclusion (exec-only s44, 94\\% of outputs, mean components${=}$2.04).\n  \\item \\textbf{Repetition collapse.} Identical premises repeated until the token limit (exec-only s43, 87\\% hit max length).\n  \\item \\textbf{Contradiction explosion.} Excessive premises (mean 18.55 components at 1000 steps) that trivially entail any conclusion via embedded contradictions.\n  \\item \\textbf{Complexity-without-utility.} Syntactically complex but semantically vacuous premises (random $\\beta{=}0.1$, 3.8\\%).\n  \\item \\textbf{Query-as-fact gaming.} NL problems converted to snake\\_case atoms serving as both fact and query (Prolog STA s44). Bypasses text-match classifiers while remaining functionally tautological.\n\\end{enumerate}\n\nThe reward signal determines hacking \\emph{composition} but not \\emph{prevalence}: total conclusion-in-premise rates are comparable across ISR and random conditions (${\\sim}$82\\% pooled across seeds), but ISR converts the GRPO-universal H1 mode into the ISR-specific H7 mode. SFT remains the only condition with near-zero hacking (92.9\\% genuine), confirming that hacking is RL-reward-specific. Different reward formulations produce characteristic hacking signatures---a finding that may inform future diagnostic design.\n",
    "structuredPatch": [
      {
        "oldStart": 106,
        "oldLines": 59,
        "newStart": 106,
        "newLines": 8,
        "lines": [
          " \\subsection{Cross-Logic Diagnostic Transfer}",
          " \\label{sec:crosslogic}",
          " ",
          "-To test whether ISR generalizes beyond a single formal language, we replicate the diagnostic and reward experiments using Prolog with SWI-Prolog 8.4.2 as the solver.",
          "+As preliminary evidence that ISR generalizes beyond a single formal language, we replicated both the diagnostic and reward experiments using SWI-Prolog 8.4.2 as the solver (full results in Appendix Figure~\\ref{fig:prolog-comparison} and Appendix Table~\\ref{tab:prolog-crosslogic}). Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming diagnostic transfer despite moderate-to-high PR; we note that low ISR here reflects \\emph{redundant coding}---repeated ground facts where removing any single copy leaves the proof intact---rather than absence of reasoning, contrasting with the metric-gaming high ISR under Prolog STA. With ISR added as a Prolog reward, all three STA seeds converge to gaming with 0\\% genuine across 185 proved samples (universal Goodhart, stronger than the FOL ${\\sim}$16\\% genuine residual): s42 produces clean H7 tautologies (50/50, ISR$^*{=}$1.000), s43 generates uppercase pseudo-Prolog that bypasses text-match classifiers but is functionally H7 ($n_{\\text{nec}}{=}1$ for 38/38), and s44 develops query-as-fact gaming where NL is converted to snake\\_case atoms used as both fact and query (ISR$^*{=}$0.912, $n_{\\text{nec}}{=}1$ for 95/97). These results suggest that simpler formal semantics enable more complete exploitation, and motivate cross-validation of hacking classifiers with functional metrics.",
          " ",
          "-\\begin{figure}[t]",
          "-\\centering",
          "-\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}",
          "-\\caption{Cross-logic ISR and Prolog STA gaming breakdown. \\textbf{(a)}~Exec-only ISR is near-zero in both FOL and Prolog, confirming cross-logic diagnostic transfer. Seed~44 FOL ($\\dagger$tautological) and seed~43 FOL ($\\ddagger$sampling eval) are annotated. \\textbf{(b)}~Prolog STA (ISR-as-reward) produces universal Goodhart: 3/3 seeds converge to gaming via distinct mechanisms---conclusion duplication, degenerate syntax, and query-as-fact---with 0\\% genuine proofs.}",
          "-\\label{fig:prolog-comparison}",
          "-\\end{figure}",
          "-",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\small",
          "-\\setlength{\\tabcolsep}{3pt}",
          "-\\begin{tabular}{llcccc}",
          "-\\toprule",
          "-\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{Mode} \\\\",
          "-\\midrule",
          "-\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\",
          "-FOL & Exec & s42 & 93 & 0.132 & H1 embedding \\\\",
          "-FOL & Exec & s43$^\\dagger$ & 14 & 0.000 & Repetition \\\\",
          "-FOL & Exec & s44 & 98 & 0.582$^\\ddagger$ & Tautological \\\\",
          "-\\cmidrule{1-6}",
          "-Prolog & Exec & s42 & 83 & 0.037 & Ground facts \\\\",
          "-Prolog & Exec & s43 & 56 & 0.015 & Degraded \\\\",
          "-Prolog & Exec & s44 & 21 & 0.387$^\\S$ & Degraded \\\\",
          "-\\midrule",
          "-\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\",
          "-Prolog & STA & s42 & 50 & 1.000$^\\|$ & H7 100\\% \\\\",
          "-Prolog & STA & s43 & 38 & 0.185$^\\|$ & Degen.\\ syntax$^\\P$ \\\\",
          "-Prolog & STA & s44 & 97 & 0.912$^\\|$ & Query-as-fact$^\\#$ \\\\",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\caption{Cross-logic transfer (proved-only ISR$^*$). \\textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \\textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\\% genuine). $^\\dagger$Sampling eval ($T{=}0.7$); not strictly comparable with greedy-decoded results. $^\\ddagger$2-component artifact. $^\\S$Small-sample ($n{=}$21). $^\\|$Gaming-inflated. $^\\P$Uppercase pseudo-Prolog; $n_{\\text{nec}}{=}1$ for 38/38. $^\\#$NL$\\to$snake\\_case atom as fact+query; $n_{\\text{nec}}{=}1$ for 95/97.}",
          "-\\label{tab:prolog-crosslogic}",
          "-\\end{table}",
          "-",
          "-\\paragraph{Diagnostic transfer.}",
          "-Table~\\ref{tab:prolog-crosslogic} (top) and Figure~\\ref{fig:prolog-comparison}(a) show that ISR detects structural degeneration in Prolog as it does in FOL. Two of three Prolog exec-only seeds yield proved-only ISR near zero (s42${=}$0.037, s43${=}$0.015), confirming structurally degenerate outputs despite moderate-to-high PR. Seed~44 (ISR$^*{=}$0.387) is a small-sample artifact: only 21 of 100 samples prove, and the higher ISR reflects variance from this sparse denominator. Cross-seed PR instability in FOL ($\\sigma{=}$47pp) replicates in Prolog ($\\sigma{=}$31pp), and both logic types produce qualitatively different collapse modes across seeds.",
          "-",
          "-We note an important semantic distinction: low ISR in Prolog exec-only reflects \\emph{redundant coding}---the model generates repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning. This contrasts with the high ISR under Prolog STA (below), which reflects \\emph{metric gaming}. ISR must be interpreted relative to the training objective.",
          "-",
          "-\\paragraph{Universal Goodhart in Prolog.}",
          "-Table~\\ref{tab:prolog-crosslogic} (bottom) and Figure~\\ref{fig:prolog-comparison}(b) reveal the strongest Goodhart result: all three Prolog STA seeds converge to gaming, with 0\\% genuine proofs across all 185 proved samples. Each seed develops a distinct gaming pathway:",
          "-\\begin{itemize}[nosep,leftmargin=*]",
          "-  \\item \\textbf{s42}: Clean H7---a single Prolog clause identical to the query (50/50 proved, ISR$^*{=}$1.000 because the sole component is trivially necessary).",
          "-  \\item \\textbf{s43}: Degenerate syntax---uppercase pseudo-Prolog (e.g., \\texttt{MARY\\_IS\\_AN\\_AVADEOTE.}). A text-match classifier labels these as genuine, but functional analysis shows $n_{\\text{necessary}}{=}1$ for all 38 proved samples (functionally H7).",
          "-  \\item \\textbf{s44}: Query-as-fact gaming---the model converts NL problems to snake\\_case atoms and sets them as both fact and query, achieving PR${=}$97\\% with $n_{\\text{necessary}}{=}1$ for 95/97. Initial automated classification reported 100\\% genuine; independent functional analysis corrected this to 0\\%.",
          "-\\end{itemize}",
          "-This result is stronger than the FOL finding: FOL ISR $\\beta{=}0.1$ retains ${\\sim}$16\\% genuine residual across seeds, while Prolog STA produces zero. Prolog's simpler semantics enable more complete exploitation, eliminating the genuine residual observed in FOL.",
          "-",
          "-\\paragraph{Classifier limitations.}",
          "-The Prolog results expose a blind spot of text-match hacking classifiers. Seeds~s43 and s44 bypass the strict H7/H1 classifier through surface-level novelty (non-standard casing, atom-level encoding) while remaining functionally tautological ($n_{\\text{necessary}}{=}1$). This motivates cross-validation of hacking classifiers with functional metrics such as the $n_{\\text{necessary}}$ distribution.",
          "-",
          " \\subsection{Hacking Taxonomy}",
          " \\label{sec:taxonomy}",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01D7RqEDkTCZHf5zHDL8dcA9`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "58fda832-713c-4863-b57c-4d5e7c32de68",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LCKNTHrAtj5ayMBr1oMT8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3511,
      "cache_read_input_tokens": 75713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3511
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

_source line 30 · 2026-05-14T20:04:27.723Z_

<details><summary>↩ Tool result · `toolu_01D7RqEDkTCZHf5zHDL8dcA9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "e9a6f287-ec71-4b01-97fa-7b750d0752b6",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 79
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01H9fZJLAk2QYD7MGW94jzmd`</summary>

```json
{
  "todos": [
    {
      "content": "Move Tab 4 (tab:beta01-3seed) from experiments.tex to appendix.tex",
      "activeForm": "Moving Tab 4 to appendix",
      "status": "completed"
    },
    {
      "content": "Compress §4.4 cross-logic, remove fig4 and Tab 5",
      "activeForm": "Compressing §4.4 and removing Tab 5/fig4",
      "status": "completed"
    },
    {
      "content": "Add Tab 4, Tab 5, fig4 to appendix.tex (and fix 0.885→0.912)",
      "activeForm": "Adding moved content to appendix.tex",
      "status": "in_progress"
    },
    {
      "content": "Compress method.tex Hacking Taxonomy enumerate",
      "activeForm": "Compressing method.tex taxonomy",
      "status": "pending"
    },
    {
      "content": "Compress introduction.tex contributions list",
      "activeForm": "Compressing introduction.tex contributions",
      "status": "pending"
    },
    {
      "content": "Compile and verify page count ≤ 12 / body ≤ 8",
      "activeForm": "Compiling and verifying page count",
      "status": "pending"
    }
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
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "e1b62b75-468d-47eb-8595-d0d788e4fdfc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01W2jqPAi6t7AbwkrCzuqoJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 66495,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 66495
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 63445
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T20:04:44.147Z_

<details><summary>↩ Tool result · `toolu_01H9fZJLAk2QYD7MGW94jzmd`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "decb300e-ac27-474a-8056-52d1622cc8a2",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Move Tab 4 (tab:beta01-3seed) from experiments.tex to appendix.tex",
        "status": "completed",
        "activeForm": "Moving Tab 4 to appendix"
      },
      {
        "content": "Compress §4.4 cross-logic, remove fig4 and Tab 5",
        "status": "completed",
        "activeForm": "Compressing §4.4 and removing Tab 5/fig4"
      },
      {
        "content": "Add Tab 4, Tab 5, fig4 to appendix.tex (and fix 0.885→0.912)",
        "status": "in_progress",
        "activeForm": "Adding moved content to appendix.tex"
      },
      {
        "content": "Compress method.tex Hacking Taxonomy enumerate",
        "status": "pending",
        "activeForm": "Compressing method.tex taxonomy"
      },
      {
        "content": "Compress introduction.tex contributions list",
        "status": "pending",
        "activeForm": "Compressing introduction.tex contributions"
      },
      {
        "content": "Compile and verify page count ≤ 12 / body ≤ 8",
        "status": "pending",
        "activeForm": "Compiling and verifying page count"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 33_

### Edit 2: appendix.tex — add moved tables/figure, fix 0.885 → 0.912

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "bddf9628-c9b9-430c-90fa-5ee557bdc92c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013R6KHKvzCyMvV5xvm14Qco",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 82829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 517
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01Xz5TjpwYNRoXdYfivEWg3j`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "old_string": "\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-detailed} and \\ref{tab:prolog-detailed} report full per-seed results for all experiment conditions.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]",
  "new_string": "\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-detailed} and \\ref{tab:prolog-detailed} report full per-seed results for all experiment conditions.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\subsection{ISR vs Random at $\\beta{=}0.1$ (FOL)}\n\nTable~\\ref{tab:beta01-3seed} provides the full per-seed breakdown for the low-dose ISR vs.\\ matched random control comparison referenced in \\S\\ref{sec:goodhart}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Cond.} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} \\\\\n\\midrule\ns42 & ISR & 81 & 0.415 & 16.0 & 51.9 & 30.9 \\\\\ns43 & ISR & 61 & 0.830 & \\textbf{96.7} & 0 & 3.3 \\\\\ns44 & ISR & 89 & 0.902 & \\textbf{86.5} & 0 & 13.5$^\\dagger$ \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 77$\\pm$14 & --- & 64.5 & 17.3 & ${\\sim}$16 \\\\\n\\midrule\ns42 & Rand & 79 & 0.131 & 0 & 70.9 & 29.1 \\\\\ns43 & Rand & 88 & 0.058 & 0 & \\textbf{93.2} & 6.8 \\\\\ns44 & Rand & 89 & 0.070 & 0 & 79.8 & 20.2 \\\\\n\\cmidrule{1-7}\n & mean$\\pm$std & 85$\\pm$6 & 0.086$\\pm$.039 & 0 & 81.3$\\pm$11 & 18.7$\\pm$11 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ISR vs Random at $\\beta{=}0.1$: per-seed comparison. ISR$^*$: proved-only. ISR mean omitted for ISR-reward seeds (inflated by H7 gaming). H7 is ISR-specific (64.5\\% vs 0\\%). H1 is GRPO-universal, higher under random (81.3\\%) than ISR (17.3\\%)---ISR converts H1 into H7. $^\\dagger$s44's 12 ``genuine'' samples all have $n_{\\text{prem}}{=}1$ (H7 classifier false negatives). Premise-count-matched genuine ISR: 0.258 (ISR, $n{=}11$) vs 0.243 (random, $n{=}21$) $= 1.06\\times$.}\n\\label{tab:beta01-3seed}\n\\end{table}\n\n\\subsection{Cross-Logic Transfer (FOL vs Prolog)}\n\nFigure~\\ref{fig:prolog-comparison} and Table~\\ref{tab:prolog-crosslogic} present the cross-logic exec-only diagnostic and Prolog STA Goodhart results referenced in \\S\\ref{sec:crosslogic}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic ISR and Prolog STA gaming breakdown. \\textbf{(a)}~Exec-only ISR is near-zero in both FOL and Prolog, confirming cross-logic diagnostic transfer. Seed~44 FOL ($\\dagger$tautological) and seed~43 FOL ($\\ddagger$sampling eval, $T{=}0.7$) are annotated. \\textbf{(b)}~Prolog STA (ISR-as-reward) produces universal Goodhart: 3/3 seeds converge to gaming via distinct mechanisms---conclusion duplication, degenerate syntax, and query-as-fact---with 0\\% genuine proofs.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Logic} & \\textbf{Condition} & \\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR}$^*$ & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Exec-only (diagnostic transfer)}} \\\\\nFOL & Exec & s42 & 93 & 0.132 & H1 embedding \\\\\nFOL & Exec & s43$^\\dagger$ & 14 & 0.000 & Repetition \\\\\nFOL & Exec & s44 & 98 & 0.582$^\\ddagger$ & Tautological \\\\\n\\cmidrule{1-6}\nProlog & Exec & s42 & 83 & 0.037 & Ground facts \\\\\nProlog & Exec & s43 & 56 & 0.015 & Degraded \\\\\nProlog & Exec & s44 & 21 & 0.387$^\\S$ & Degraded \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{ISR-as-reward (Goodhart transfer)}} \\\\\nProlog & STA & s42 & 50 & 1.000$^\\|$ & H7 100\\% \\\\\nProlog & STA & s43 & 38 & 0.185$^\\|$ & Degen.\\ syntax$^\\P$ \\\\\nProlog & STA & s44 & 97 & 0.912$^\\|$ & Query-as-fact$^\\#$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-logic transfer (proved-only ISR$^*$). \\textit{Top}: Exec-only ISR near-zero in both logics, confirming diagnostic transfer. \\textit{Bottom}: Prolog STA yields universal Goodhart (3/3 gaming, 0\\% genuine). $^\\dagger$Sampling eval ($T{=}0.7$); not strictly comparable with greedy-decoded results. $^\\ddagger$2-component artifact. $^\\S$Small-sample ($n{=}$21). $^\\|$Gaming-inflated. $^\\P$Uppercase pseudo-Prolog; $n_{\\text{nec}}{=}1$ for 38/38. $^\\#$NL$\\to$snake\\_case atom as fact+query; $n_{\\text{nec}}{=}1$ for 95/97.}\n\\label{tab:prolog-crosslogic}\n\\end{table}\n\n\\begin{table*}[t]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "c9960cbf-c8cd-4fb0-b747-ca95b8f8c948",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013R6KHKvzCyMvV5xvm14Qco",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 82829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 517
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

_source line 35 · 2026-05-14T20:05:36.051Z_

<details><summary>↩ Tool result · reported error · `toolu_01Xz5TjpwYNRoXdYfivEWg3j`</summary>

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
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "a5897b24-31bb-4be9-9d7f-35a789a3526b",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01BytgdfPjTMfWHdiv52gunh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 230,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "266baec9-8df1-4374-963d-fd689e3e44bf",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Ni2Lhw3GXeBc5fUTPULjRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2837,
      "cache_read_input_tokens": 83346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2837
      },
      "output_tokens": 51,
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

_source line 37 · 2026-05-14T20:05:43.506Z_

<details><summary>↩ Tool result · `toolu_01BytgdfPjTMfWHdiv52gunh`</summary>

```text
230	
231	\paragraph{Prevalence.}
232	Observed in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.885$).
233	95/97 proved samples have $n_{\text{necessary}} = 1$, confirming functional tautology despite the strict classifier reporting 100\% genuine.
234	
235	
236	\section{Per-Seed Detailed Results}
237	\label{app:detailed-results}
238	
239	Tables~\ref{tab:fol-detailed} and \ref{tab:prolog-detailed} report full per-seed results for all experiment conditions.
240	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
241	ISR values are proved-only ISR$^*$.
242	
243	\begin{table*}[t]
244	\centering
245	\caption{Detailed per-seed results: FOL (Prover9). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\ = percentage among proved samples.  ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$); 3-seed mean includes this methodological difference.}
246	\label{tab:fol-detailed}
247	\small
248	\begin{tabular}{@{}llccccccl@{}}
249	\toprule
250	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{Gen.\%} & \textbf{Notes} \\
251	\midrule
252	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
253	Base model (no training)
254	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
255	Ground-truth FOL
256	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
257	SFT
258	  & 42 & ${\sim}$8 ep. & 0.14 & 0.571 & 0 & 7.1 & \textbf{92.9} & Supervised, no RL \\
259	\midrule
260	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
261	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
262	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 12.9 & \\
263	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
264	  & 43 & 500 & 0.14 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Sampling $T{=}0.7$ \\
265	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
266	\cmidrule(l){2-9}
267	  & \multicolumn{2}{l}{3-seed mean$\pm$std$^\dagger$} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step only \\
268	\midrule
269	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
270	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{30.9} & Mixed H1+H7 \\
271	  & 43 & 500 & 0.61 & 0.830 & \textbf{96.7} & 0 & ${\sim}$3 & H7 dominant \\
272	  & 44 & 500 & 0.89 & 0.902 & 86.5 & 0 & ${\sim}$13.5 & H7 dominant \\
273	\cmidrule(l){2-9}
274	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
275	\midrule
276	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
277	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & Goodhart collapse \\
278	\midrule
279	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "ca3242d8-2894-43be-9f0a-528d8d262440",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.885$).\n95/97 proved samples have $n_{\\text{necessary}} = 1$, confirming functional tautology despite the strict classifier reporting 100\\% genuine.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-detailed} and \\ref{tab:prolog-detailed} report full per-seed results for all experiment conditions.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\\ = percentage among proved samples.  ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$); 3-seed mean includes this methodological difference.}\n\\label{tab:fol-detailed}\n\\small\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & ${\\sim}$8 ep. & 0.14 & 0.571 & 0 & 7.1 & \\textbf{92.9} & Supervised, no RL \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 12.9 & \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.14 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Sampling $T{=}0.7$ \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std$^\\dagger$} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step only \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{30.9} & Mixed H1+H7 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{96.7} & 0 & ${\\sim}$3 & H7 dominant \\\\\n  & 44 & 500 & 0.89 & 0.902 & 86.5 & 0 & ${\\sim}$13.5 & H7 dominant \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & Goodhart collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\",
      "numLines": 50,
      "startLine": 230,
      "totalLines": 339
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01YWFWzVEKSAW5GHXeF2XBzF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "old_string": "Observed in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.885$).",
  "new_string": "Observed in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.912$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "18e23e9d-4bb2-49eb-b5b5-2ad45e563140",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01AD71QtVUgn17usweJSGLoS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1850,
      "cache_read_input_tokens": 86183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1850
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

_source line 39 · 2026-05-14T20:05:49.339Z_

<details><summary>↩ Tool result · `toolu_01YWFWzVEKSAW5GHXeF2XBzF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed6a07bf-b4ac-4b98-bc2f-08c1266f96d5",
  "uuid": "ffd89d89-0367-431e-9861-228623b9899e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "oldString": "Observed in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.885$).",
    "newString": "Observed in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.912$).",
    "originalFile": "% Appendix — solver-trace-ablation\n% Requires: booktabs, amsmath, enumitem packages (loaded in paper.tex)\n\n\\appendix\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 8 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nTraining data file & \\texttt{train\\_500\\_seed42.jsonl} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding strategy & Greedy (temperature = 0) \\\\\nISR computation & \\texttt{eval\\_sta.py} (unified) \\\\\nISR variant reported & Proved-only ISR (ISR$^*$) \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Reward Conditions (6 total)}} \\\\\nExec-only & $r = r_{\\text{exec}}$ \\\\\nISR $\\beta{=}0.1$ & $r = r_{\\text{exec}} \\cdot (1 + 0.1 \\cdot \\text{ISR})$ \\\\\nISR $\\beta{=}0.3$ & $r = r_{\\text{exec}} \\cdot (1 + 0.3 \\cdot \\text{ISR})$ \\\\\nRandom $\\beta{=}0.1$ & $r = r_{\\text{exec}} \\cdot (1 + 0.1 \\cdot u),\\; u{\\sim}\\mathcal{U}(0,1)$ \\\\\nRandom $\\beta{=}0.3$ & $r = r_{\\text{exec}} \\cdot (1 + 0.3 \\cdot u)$ \\\\\nSFT & Supervised fine-tuning (no RL) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$= 0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify seven distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\n\n\\subsection{H1 --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).        % <-- conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$= 1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as H1 (71--93\\%); under ISR reward, it shifts to H7 (64.5\\% mean).\n\n\n\\subsection{H7 --- Conclusion Duplication}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises:\n  all x ((A(x) & B(x)) -> (C(x) | D(x))).\nConclusion:\n  all x ((A(x) & B(x)) -> (C(x) | D(x))).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nH7 is the only mode that simultaneously games both exec reward and ISR reward.\n\n\\paragraph{Prevalence.}\nISR-specific: 3-seed mean = 66.4\\% under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\n\\textbf{Zero} occurrences under Random~$\\beta{=}0.1$ across all three seeds ($0/256$).\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$= 1.0$ (the sole premise is necessary).\nDistinguished from H7 by having low component count ($n_{\\text{comp}} \\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$= 0.98$, mean~$n_{\\text{comp}} = 2.04$, 100\\%~H7 by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\%~H7, PR~$= 0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$= 14\\%$, ISR~$= 0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) -> exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).                   % <-- only this needed\nConclusion: Q(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$= 0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$= 0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18.   % 18.55 mean components\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$= 0.003$, with 94.8\\% of proved samples having ISR~$= 0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe fact is necessarily necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to H7 but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.885$).\n95/97 proved samples have $n_{\\text{necessary}} = 1$, confirming functional tautology despite the strict classifier reporting 100\\% genuine.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-detailed} and \\ref{tab:prolog-detailed} report full per-seed results for all experiment conditions.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\\ = percentage among proved samples.  ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$); 3-seed mean includes this methodological difference.}\n\\label{tab:fol-detailed}\n\\small\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & ${\\sim}$8 ep. & 0.14 & 0.571 & 0 & 7.1 & \\textbf{92.9} & Supervised, no RL \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 12.9 & \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.14 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Sampling $T{=}0.7$ \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std$^\\dagger$} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step only \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{30.9} & Mixed H1+H7 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{96.7} & 0 & ${\\sim}$3 & H7 dominant \\\\\n  & 44 & 500 & 0.89 & 0.902 & 86.5 & 0 & ${\\sim}$13.5 & H7 dominant \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & Goodhart collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 70.9 & 29.1 & \\\\\n  & 43 & 500 & 0.88 & 0.058 & 0 & 93.2 & 6.8 & \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 79.8 & 20.2 & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.85{\\pm}0.06$} & & \\makebox[0pt][l]{$0.086{\\pm}0.039$} & & & H7 = 0\\% all seeds \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & --- & --- & --- & $n_{\\text{comp}} = 9.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/Gen.\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{Gen.\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.53{\\pm}0.31$} & & \\makebox[0pt][l]{$0.146{\\pm}0.21$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & H7 tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional H7$^a$ \\\\\n  & 44 & 0.97 & 0.885 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.62{\\pm}0.31$} & & \\makebox[0pt][l]{$0.690{\\pm}0.44$} & & 3/3 Goodhart, 0\\% genuine \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict H7 classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}} = 1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Genuine$\\,{=}\\,$100\\%, but 95/97 proved samples have $n_{\\text{necessary}} = 1$. The model converts NL to snake\\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^* = 0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4\\%$) $\\to$ $0.003$ at 1000 steps ($-99.6\\%$ from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$= 0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% genuine proofs, but each discovers a different gaming mechanism:\nseed~42 produces clean H7 tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n",
    "structuredPatch": [
      {
        "oldStart": 229,
        "oldLines": 7,
        "newStart": 229,
        "newLines": 7,
        "lines": [
          " Functionally equivalent to H7 but with a distinct surface mechanism.",
          " ",
          " \\paragraph{Prevalence.}",
          "-Observed in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.885$).",
          "+Observed in Prolog exec+STA seed~44 (PR~$= 0.97$, ISR~$= 0.912$).",
          " 95/97 proved samples have $n_{\\text{necessary}} = 1$, confirming functional tautology despite the strict classifier reporting 100\\% genuine.",
          " ",
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
