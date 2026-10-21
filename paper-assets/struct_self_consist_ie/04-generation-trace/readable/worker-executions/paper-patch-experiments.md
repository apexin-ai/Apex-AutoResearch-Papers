# paper patch experiments

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_paper_patch-experiments_20260516T024604.log`
- **Structured JSON:** [`1708defc985b16d117f6.json`](../../sessions/17/1708defc985b16d117f6.json)

## Before a recorded user message

56 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
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
  "uuid": "4df64b51-b9b1-40b3-8368-5af766886263",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1778907000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1cd96f10-5b55-4e43-a20a-8c53e91abee8",
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current experiments.tex file to understand its structure and content before making edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "e5afb7e4-b723-4074-9ab8-975df0f75864",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bSLLhF5dt7jhcYcsMhR1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14198,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14198
      },
      "output_tokens": 30,
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

Let me read the current file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "51f94bf4-eb23-4fec-9eb0-47a6c8bb442d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bSLLhF5dt7jhcYcsMhR1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14198,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14198
      },
      "output_tokens": 30,
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

<details open><summary>🔧 Tool call — Read · `toolu_01U5Pb8QPDLm6hejeMrLK5iZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "7ee50f54-a11a-4586-91b6-037e9665d0cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bSLLhF5dt7jhcYcsMhR1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14198,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14198
      },
      "output_tokens": 30,
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

_source line 7 · 2026-05-16T02:46:13.700Z_

<details><summary>↩ Tool result · `toolu_01U5Pb8QPDLm6hejeMrLK5iZ`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.
12	This gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\S\ref{sec:complexity_robustness}).
13	
14	\paragraph{Models.}
15	Our primary model is \textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.
16	For cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.
17	
18	\paragraph{Sampling and Evaluation.}
19	For each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.
20	We use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.
21	Quality estimation is measured along two axes: \textit{rank correlation} with instance-level F1 via Spearman $\rho$ and Kendall $\tau$, and \textit{binary discrimination} via AUROC (instances above vs.\ below median F1).
22	Downstream utility is assessed through \textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.
23	Instance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.
24	The greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.
25	
26	\paragraph{Confidence Signals.}
27	We compare five signals from three families (detailed in \S\ref{sec:signals}).
28	\textit{Structural} signals operate on extracted entity/relation sets: \textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \textbf{Soft Jaccard (SJ)} measures pairwise set similarity \cite{jaccard1901distribution}.
29	\textit{Surface} signals operate on string representations: \textbf{Fleiss' $\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \cite{fleiss1971agreement}, and \textbf{Exact Match (EM)} computes the fraction of identical sample pairs.
30	The \textit{model-internal} signal is \textbf{log-probability (logprob)}, the mean token-level log-likelihood.
31	
32	\paragraph{Implementation.}
33	Inference uses vLLM with XGrammar constrained decoding \cite{willard2023guided} to enforce valid JSON output structure.
34	A span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.
35	All confidence signals are computed from the $N$ samples without access to gold labels.
36	
37	%% ============================================================
38	\subsection{Quality Estimation Results}
39	\label{sec:qe_results}
40	
41	\begin{table*}[t]
42	\centering
43	\small
44	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}
45	\label{tab:quality_estimation}
46	\begin{tabular}{ll cc cc cc cc}
47	\toprule
48	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
49	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
50	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
51	\midrule
52	Voting Conf. & Structural & \textbf{.502} & \textbf{.728} & \textbf{.422} & \textbf{.716} & .424 & .789 & .426 & .709 \\
53	Soft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \textbf{.431} & .704 \\
54	Fleiss' $\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\
55	Exact Match  & Surface    & .257 & .623 & .100 & .504 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
56	Log-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \textbf{.761} \\
57	\bottomrule
58	\end{tabular}
59	\end{table*}
60	
61	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
62	
63	\paragraph{Structural signals dominate on complex schemas.}
64	On SciERC NER, Voting Confidence achieves $\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\rho{=}0.357$), and all remaining signals ($\rho{\leq}0.265$).
65	Voting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.
66	The structural advantage persists on RE, where Voting ($\rho{=}0.422$) again leads.
67	However, all signals weaken on RE: 44\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.
68	Notably, FK ($\rho{=}0.253$) exceeds SJ ($\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.
69	
70	\paragraph{Signal rankings shift with task difficulty.}
71	On CoNLL NER, where greedy decoding achieves ${>}$91\% micro F1, the signal landscape changes substantially.
72	Exact Match leads with $\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\rho{=}0.436$) and Voting ($\rho{=}0.424$).
73	When most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.
74	This reversal---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.
75	
76	\paragraph{Cross-model stability.}
77	Comparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\rho{=}0.436$ (Qwen) vs.\ $\rho{=}0.431$ (LLaMA), a gap of only 0.005.
78	This model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.
79	The SJ--FK gap also narrows with schema simplification: $\Delta\rho{=}0.092$ on SciERC NER (6 entity types) vs.\ $\Delta\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.
80	
81	\paragraph{The logprob paradox.}
82	Log-probability reveals a dissociation between ranking and classification.
83	On CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\rho$ (0.307) among all signals.
84	This pattern indicates that logprob assigns well-separated scores to easy vs.\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.
85	We return to this distinction in \S\ref{sec:complexity_robustness} and visualize it in Figure~\ref{fig:signal_heatmap}.
86	
87	\paragraph{Oracle headroom and practical ceilings.}
88	On CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.
89	When the model already operates near its performance ceiling, confidence signals serve as \textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.
90	We therefore focus selection analysis (\S\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.
91	
92	%% ============================================================
93	\subsection{The Correlation-Selection Gap}
94	\label{sec:selection_gap}
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM produces binary agreement without sample ranking.}
100	\label{tab:selection}
101	\begin{tabular}{lcc}
102	\toprule
103	Method & NER F1 & RE F1 \\
104	\midrule
105	Oracle & 0.769 & 0.561 \\
106	\midrule
107	Log-prob           & 0.609 & \textbf{0.397} \\
108	Ensemble (SJ+Vot.) & 0.604 & 0.367 \\
109	Soft Jaccard       & 0.604 & 0.368 \\
110	Voting             & 0.596 & 0.338 \\
111	Exact Match        & ---   & ---   \\
112	\midrule
113	Greedy ($T{=}0$)   & \textbf{0.609} & 0.374 \\
114	Random             & 0.580 & 0.338 \\
115	\bottomrule
116	\end{tabular}
117	\end{table}
118	
119	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.
120	Table~\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).
121	
122	\paragraph{NER: no signal surpasses greedy.}
123	The oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).
124	Yet no confidence signal closes this gap.
125	Log-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\rho{=}0.502$), selects to only 0.596, \textit{below} greedy.
126	An ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.
127	The greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.
128	The Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.
129	
130	\paragraph{RE: logprob uniquely succeeds.}
131	For RE, log-probability is the only signal to exceed greedy (0.397 vs.\ 0.374, +2.3~pp).
132	Structural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.
133	The oracle gap of 18.7~pp (0.561 vs.\ 0.374) indicates substantially more per-instance variance than NER.
134	Log-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.
135	
136	\paragraph{Quality estimation $\neq$ output selection.}
137	We attribute this gap (Figure~\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best for a given input.
138	When per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.
139	
140	\paragraph{Implications for test-time scaling.}
141	This correlation-selection gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}.
142	Scaling inference compute through repeated sampling assumes a selector can identify the best sample.
143	Our results show that for structured prediction, existing confidence signals serve as quality \textit{estimators}---useful for flagging unreliable predictions---but not as effective \textit{selectors}.
144	Closing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \cite{cobbe2021verifiers} or pairwise comparison models.
145	
146	%% ============================================================
147	\subsection{Task Complexity and Signal Robustness}
148	\label{sec:complexity_robustness}
149	
150	\paragraph{Task difficulty as a boundary condition.}
151	Signal effectiveness varies systematically with task difficulty.
152	On CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\rho{=}0.451$); on SciERC NER (micro F1$\,{\approx}\,$0.66), SJ overtakes EM ($\rho{=}0.357$ vs.\ 0.257); on SciERC RE, where 44\% of instances score zero F1, all signals converge to $\rho{\approx}0.25$.
153	The NER--RE difference is statistically confirmed: Fisher's $z$-test on $\rho_\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.
154	
155	\paragraph{Per-relation diagnostic.}
156	RE signal degradation is relation-specific.
157	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
158	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
159	
160	\paragraph{Capability stratification.}
161	SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
162	The SJ advantage over logprob remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.
163	
164	\paragraph{Method boundary: WNUT-17.}
165	WNUT-17 establishes where the approach breaks down.
166	SJ achieves $\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\% of instances at zero F1.
167	Log-probability shows a strong \textit{negative} correlation ($\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.
168	This is a boundary of the method, not a limitation of the datasets.
169	
170	\begin{table}[t]
171	\centering
172	\small
173	\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\rho$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
174	\label{tab:robustness}
175	\begin{tabular}{llcc}
176	\toprule
177	& & NER $\rho$ & RE $\rho$ \\
178	\midrule
179	\multicolumn{4}{l}{\textit{Temperature} ($N{=}8$)} \\
180	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
181	\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\
182	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
183	\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\
184	\midrule
185	\multicolumn{4}{l}{\textit{Sample size} ($T{=}1.0$)} \\
186	\quad SJ & $N{=}8$  & 0.357 & 0.211 \\
187	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
188	\quad FK & $N{=}8$  & 0.265 & 0.253 \\
189	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
190	\bottomrule
191	\end{tabular}
192	\end{table}
193	
194	\paragraph{Robustness analysis.}
195	Table~\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.
196	\textit{Temperature.}
197	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.
198	FK shows mixed behavior: NER $\rho$ drops by 0.056, while RE $\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
199	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.357 vs.\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
200	
201	\textit{Sample size.}
202	Increasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\rho$ improves from 0.357 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).
203	FK benefits less ($\rho{\approx}0.280$ at $N{=}16$ vs.\ 0.265 at $N{=}8$).
204	For RE at $N{=}16$, SJ ($\rho{=}0.281$), FK ($\rho{=}0.279$), and logprob ($\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.
205	
206	\paragraph{Cross-model transfer.}
207	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, 3-seed mean).
208	On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
209	On conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
210	
211	\paragraph{Evaluation circularity.}
212	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
213	Evaluation circularity is negligible.
214	
215	\paragraph{Conditional filtering reveals signal divergence.}
216	Filtering to non-zero F1 instances improves SJ correlations: NER $\rho{=}0.412$ (from 0.357), RE $\rho{=}0.368$ at $N{=}8$.
217	At $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\rho{=}0.308$, while logprob drops to $\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.
218	For applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\rho{\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.
219	
220	\paragraph{Binary filtering vs.\ continuous ranking.}
221	The logprob paradox observed in Table~\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.
222	Log-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).
223	Figure~\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.
224	Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.
225	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "7cee5645-6029-4294-ae88-bd6757e6c6bb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n",
      "numLines": 225,
      "startLine": 1,
      "totalLines": 225
    }
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full file. Let me plan the edits carefully:

1. **Add 4B Scale Ablation** - After "Robustness analysis" paragraph (after line 204), before "Cross-model transfer" (line 206)
2. **Add Free-form Ablation** - After the 4B paragraph
3. **Add ε=0.05 Justification** - Near line 215-218 (conditional filtering paragraph)
4. **Fix Fisher's z-test** - Line 153
5. **Add RE (preliminary)** - Table 1 caption (line 44), Table 2 caption (line 99), Table 3 caption (line 173)


6. **Add Figure environments** - Three figures at specified locations
7. **Define n=81 RE subset** - Line 160-162 area

I'll work from the bottom of the file upward to keep line numbers stable as I make changes. Starting with the figure environments, then the ε=0.05 justification, followed by the ablation sections, and finally the n=81 definition and table captions.

Before I start editing, I need to verify that the figure files actually exist. Let me also double-check the robustness table since it has RE columns that need the preliminary label added as well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "9207d9a0-5a13-4b63-9dcd-12b58e867587",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQDnuogFrrttJSShAbaKZx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6442,
      "cache_read_input_tokens": 25899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6442
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

_source line 9_

Let me verify the figure files exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "2630d400-f538-4bb7-b913-881b33900836",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQDnuogFrrttJSShAbaKZx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6442,
      "cache_read_input_tokens": 25899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6442
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

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_013YJdhjpFBZfG3ZqfCwCXUU`</summary>

```json
{
  "pattern": "**/*.{png,pdf}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "292eab27-5a80-4e4e-98bb-8b6b6881da86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQDnuogFrrttJSShAbaKZx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6442,
      "cache_read_input_tokens": 25899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6442
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

_source line 11 · 2026-05-16T02:46:32.352Z_

<details><summary>↩ Tool result · `toolu_013YJdhjpFBZfG3ZqfCwCXUU`</summary>

```text
artifacts/figures/fig_signal_heatmap.pdf
artifacts/figures/fig_correlation_selection_gap.pdf
artifacts/figures/fig_temperature_robustness.pdf
artifacts/figures/fig_signal_heatmap.png
artifacts/figures/fig_correlation_selection_gap.png
artifacts/figures/fig_temperature_robustness.png
artifacts/figures/fig_reliability_1024.pdf
artifacts/figures/fig_reliability_1024.png
artifacts/figures/fig_selection_gap_1024.pdf
artifacts/figures/fig_selection_gap_1024.png
artifacts/figures/fig_signal_heatmap_1024.pdf
artifacts/figures/fig_signal_heatmap_1024.png
artifacts/figures/fig_length_logprob_scatter.pdf
artifacts/figures/fig_length_logprob_scatter.png
artifacts/figures/fig_selection_gap.pdf
artifacts/figures/fig_selection_gap.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "656c5740-4db8-4b9f-97f4-2c3502f065cb",
  "tool_use_result": {
    "filenames": [
      "artifacts/figures/fig_signal_heatmap.pdf",
      "artifacts/figures/fig_correlation_selection_gap.pdf",
      "artifacts/figures/fig_temperature_robustness.pdf",
      "artifacts/figures/fig_signal_heatmap.png",
      "artifacts/figures/fig_correlation_selection_gap.png",
      "artifacts/figures/fig_temperature_robustness.png",
      "artifacts/figures/fig_reliability_1024.pdf",
      "artifacts/figures/fig_reliability_1024.png",
      "artifacts/figures/fig_selection_gap_1024.pdf",
      "artifacts/figures/fig_selection_gap_1024.png",
      "artifacts/figures/fig_signal_heatmap_1024.pdf",
      "artifacts/figures/fig_signal_heatmap_1024.png",
      "artifacts/figures/fig_length_logprob_scatter.pdf",
      "artifacts/figures/fig_length_logprob_scatter.png",
      "artifacts/figures/fig_selection_gap.pdf",
      "artifacts/figures/fig_selection_gap.png"
    ],
    "durationMs": 9,
    "numFiles": 16,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Good, all three figure files exist. Now let me make the edits from bottom to top.

Let me plan carefully:

**Edit 1**: Add fig:reliability after line 223 (after "Figure~\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.")
Actually, looking at line 223, the figure reference is already there. The figure environment should go right before or after the paragraph that references it. Let me put it right before the "Binary filtering" paragraph (before line 220) or after line 223. I'll put it after line 223 since the text references the figure.


Wait, the task says to add it near the binary filtering paragraph's end, so I should place it after line 224 instead. Actually, for LaTeX to handle the float properly, I'll add it right before the "Binary filtering" paragraph so it appears close to where it's referenced.

**Edit 2**: Add ε=0.05 justification in the conditional filtering paragraph (lines 215-218).

**Edit 3**: Add 4B scale ablation and free-form ablation between the "Robustness analysis" section and wherever it ends.

**Edit 4**: Add n=81 definition around line 161-162.

**Edit 5**: Fix Fisher's z-test at line 153.

**Edit 6**: Add fig:selection_gap near line 137.

**Edit 7**: Add RE preliminary to Table 2 caption (line 99).

**Edit 8**: Add fig:signal_heatmap near line 85.

**Edit 9**: Add RE preliminary to Table 1 caption (line 44).

**Edit 10**: Add RE preliminary to robustness table caption (line 173).

I'll work through these from the bottom up to avoid shifting line numbers as I make changes. First, I need to verify whether I should use `fig_selection_gap` or `fig_selection_gap_1024` based on what the task specifies.

Now I'm ready to apply all the edits. I'll proceed from the bottom of the file upward, starting with the fig:reliability reference after line 223, then moving through the conditional filtering paragraph, the ablation sections, and finally the figure and caption additions at the top of the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "74db6e93-2bfc-4b86-9f79-08819a16e880",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HagLfBvEYJbRVifTk9cLGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 32341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 875
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

_source line 13_

Now I'll make all edits bottom-to-top to keep line numbers stable. Starting with the edits near the end of the file.

**Edit 1**: Add fig:reliability after the binary filtering paragraph (after line 223).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "69d23adb-9262-4e6f-a78e-0f8f5abf064b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HagLfBvEYJbRVifTk9cLGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 32341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 875
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

_source line 14_

<details open><summary>🔧 Tool call — Edit · `toolu_01DMQib7Nc7xgaQrnKzgk6XF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "\tPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.",
  "new_string": "\tPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "5a22bcbf-0b45-45ff-8aa0-2b04457684d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HagLfBvEYJbRVifTk9cLGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 32341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 875
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

_source line 15 · 2026-05-16T02:46:51.673Z_

<details><summary>↩ Tool result · reported error · `toolu_01DMQib7Nc7xgaQrnKzgk6XF`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String: 	Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "22b22d51-fbb6-40f1-a7d5-02aeb743984c",
  "tool_use_result": "Error: String to replace not found in file.\nString: \tPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency."
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01TjMmDHwfGWDG1aWJ4WyaXC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "offset": 220,
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
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "066e53e9-12dd-4574-9e7c-b8b0451017bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129sYq54ff2MgkbZhhcyxzN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1224,
      "cache_read_input_tokens": 33216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1224
      },
      "output_tokens": 69,
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

_source line 17 · 2026-05-16T02:46:55.768Z_

<details><summary>↩ Tool result · `toolu_01TjMmDHwfGWDG1aWJ4WyaXC`</summary>

```text
220	\paragraph{Binary filtering vs.\ continuous ranking.}
221	The logprob paradox observed in Table~\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.
222	Log-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).
223	Figure~\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.
224	Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.
225	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "84dca79a-cbaf-4245-8b40-bba7031d5f50",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
      "content": "\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n",
      "numLines": 6,
      "startLine": 220,
      "totalLines": 225
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01FEiZaC7BsrpQpinEvzzPtj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.",
  "new_string": "Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "00d0218f-bb4c-443f-9be5-4a4af0fb68a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbD1V73X41iXpfH7RUP7tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 327,
      "cache_read_input_tokens": 34440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 327
      },
      "output_tokens": 69,
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

_source line 19 · 2026-05-16T02:47:00.904Z_

<details><summary>↩ Tool result · `toolu_01FEiZaC7BsrpQpinEvzzPtj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "995d54ce-9265-4fdf-8538-7a72a93f1761",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
    "oldString": "Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.",
    "newString": "Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n",
    "structuredPatch": [
      {
        "oldStart": 222,
        "oldLines": 3,
        "newStart": 222,
        "newLines": 10,
        "lines": [
          " Log-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).",
          " Figure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.",
          " Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.",
          "+",
          "+\\begin{figure}[t]",
          "+\\centering",
          "+\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}",
          "+\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}",
          "+\\label{fig:reliability}",
          "+\\end{figure}"
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

_source line 20_

**Edit 2**: Add ε=0.05 justification in the conditional filtering paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "05550a82-948d-48b4-8aab-339064a74dc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dTkX1uFEZfA6ZHosgPaAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 357,
      "cache_read_input_tokens": 34767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 357
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01Az5rzvP4dFPotmCqrn9a8c`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "\\paragraph{Conditional filtering reveals signal divergence.}\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.",
  "new_string": "\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "bef544a3-308a-4199-9cd8-31bb904d9821",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dTkX1uFEZfA6ZHosgPaAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 357,
      "cache_read_input_tokens": 34767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 357
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

_source line 22 · 2026-05-16T02:47:07.545Z_

<details><summary>↩ Tool result · `toolu_01Az5rzvP4dFPotmCqrn9a8c`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "4acd4636-21bc-4e24-b225-cd48e1757670",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
    "oldString": "\\paragraph{Conditional filtering reveals signal divergence.}\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.",
    "newString": "\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 213,
        "oldLines": 6,
        "newStart": 213,
        "newLines": 7,
        "lines": [
          " Evaluation circularity is negligible.",
          " ",
          " \\paragraph{Conditional filtering reveals signal divergence.}",
          "+We define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).",
          " Filtering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.",
          " At $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.",
          " For applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit."
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

_source line 23_

**Edit 3**: Add 4B scale ablation and free-form ablation between robustness analysis and cross-model transfer.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "8c7a8455-9b55-4362-88db-3978c049904f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrcvPX8UBXFfLfRfEx5GDb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 35124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 565
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

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01LXPCRqBoLTs1j8m9ivjkpg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER",
  "new_string": "\\paragraph{Scale ablation: 4B vs.\\ 8B.}\nTo isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}\n\\label{tab:scale-ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& 8B & 4B & 8B & 4B & 8B & 4B \\\\\n\\midrule\nSJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\\nFK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\\n\\midrule\nGreedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\\nOracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.\nYet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "ec2d74d4-b464-49d6-aa6a-b3aee290b888",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrcvPX8UBXFfLfRfEx5GDb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 35124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 565
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

_source line 25 · 2026-05-16T02:47:33.156Z_

<details><summary>↩ Tool result · `toolu_01LXPCRqBoLTs1j8m9ivjkpg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "9b9911f8-34a9-4cb9-a76a-4e6209ced2a8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
    "oldString": "\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER",
    "newString": "\\paragraph{Scale ablation: 4B vs.\\ 8B.}\nTo isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}\n\\label{tab:scale-ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& 8B & 4B & 8B & 4B & 8B & 4B \\\\\n\\midrule\nSJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\\nFK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\\n\\midrule\nGreedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\\nOracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.\nYet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 203,
        "oldLines": 6,
        "newStart": 203,
        "newLines": 43,
        "lines": [
          " FK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).",
          " For RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.",
          " ",
          "+\\paragraph{Scale ablation: 4B vs.\\ 8B.}",
          "+To isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.",
          "+",
          "+\\begin{table}[t]",
          "+\\centering",
          "+\\small",
          "+\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}",
          "+\\label{tab:scale-ablation}",
          "+\\begin{tabular}{lcccccc}",
          "+\\toprule",
          "+& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\",
          "+\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}",
          "+& 8B & 4B & 8B & 4B & 8B & 4B \\\\",
          "+\\midrule",
          "+SJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\",
          "+FK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\",
          "+\\midrule",
          "+Greedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\",
          "+Oracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          "+Table~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.",
          "+Yet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.",
          "+On CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.",
          "+The gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.",
          "+",
          "+\\paragraph{Free-form decoding ablation.}",
          "+One concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.",
          "+We test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.",
          "+The fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.",
          "+Crucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).",
          "+NER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).",
          "+Score compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.",
          "+This reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.",
          "+",
          " \\paragraph{Cross-model transfer.}",
          " LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).",
          " On CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$."
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

**Edit 4**: Add RE preliminary to robustness table caption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "463da42f-7a3d-45fa-9a8c-00b09e66b4d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vXPFmN35V6jehAvUEduYT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1317,
      "cache_read_input_tokens": 35689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1317
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_014BRDwadhR6bWj3qGtqhK6Y`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}",
  "new_string": "\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "fb84c2c4-59d4-4ccf-a2f1-c0b37f55dddb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vXPFmN35V6jehAvUEduYT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1317,
      "cache_read_input_tokens": 35689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1317
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

_source line 28 · 2026-05-16T02:47:39.465Z_

<details><summary>↩ Tool result · `toolu_014BRDwadhR6bWj3qGtqhK6Y`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "2ff9c7c0-5158-46a6-8090-9c727565cd7c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
    "oldString": "\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}",
    "newString": "\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Scale ablation: 4B vs.\\ 8B.}\nTo isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}\n\\label{tab:scale-ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& 8B & 4B & 8B & 4B & 8B & 4B \\\\\n\\midrule\nSJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\\nFK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\\n\\midrule\nGreedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\\nOracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.\nYet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 170,
        "oldLines": 7,
        "newStart": 170,
        "newLines": 7,
        "lines": [
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}",
          "+\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}",
          " \\label{tab:robustness}",
          " \\begin{tabular}{llcc}",
          " \\toprule"
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

_source line 29_

**Edit 5**: Add n=81 RE definition in capability stratification paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "a2a183ea-5949-4cf0-aff5-0beea8dfa67b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVPP4NUhDXrdeZBNZWCfND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 361,
      "cache_read_input_tokens": 37006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 361
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

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01Xr6KuvNmBYpEQDrjSt81S9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.",
  "new_string": "SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nSimilarly, RE instances with ${\\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "d6ac3bda-7891-46e4-aa6b-743002782cd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVPP4NUhDXrdeZBNZWCfND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 361,
      "cache_read_input_tokens": 37006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 361
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

_source line 31 · 2026-05-16T02:47:49.948Z_

<details><summary>↩ Tool result · `toolu_01Xr6KuvNmBYpEQDrjSt81S9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "0767fbbc-5d6a-46e2-a221-b1c0f8c91df5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
    "oldString": "SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.",
    "newString": "SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nSimilarly, RE instances with ${\\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Scale ablation: 4B vs.\\ 8B.}\nTo isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}\n\\label{tab:scale-ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& 8B & 4B & 8B & 4B & 8B & 4B \\\\\n\\midrule\nSJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\\nFK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\\n\\midrule\nGreedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\\nOracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.\nYet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 159,
        "oldLines": 6,
        "newStart": 159,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Capability stratification.}",
          " SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.",
          "+Similarly, RE instances with ${\\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.",
          " The SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.",
          " ",
          " \\paragraph{Method boundary: WNUT-17.}"
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

_source line 32_

**Edit 6**: Fix Fisher's z-test description.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "ef81d5cc-7f07-40f1-a8c6-13dfbbcd086c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUnij6nTeJweDNAHocGrYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 573,
      "cache_read_input_tokens": 37367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 573
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

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01R66o44Xgpk5qvmCsi2E7Rp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.",
  "new_string": "Fisher's $z$-test comparing SJ $\\rho$ between NER ($\\rho{=}0.357$) and RE ($\\rho{=}0.211$) yields $z{=}2.31$, $p{=}0.021$, confirming statistically significant task-dependent degradation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "aaafdf43-9898-466b-b47c-1b9f97607b4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUnij6nTeJweDNAHocGrYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 573,
      "cache_read_input_tokens": 37367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 573
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

_source line 34 · 2026-05-16T02:47:54.893Z_

<details><summary>↩ Tool result · `toolu_01R66o44Xgpk5qvmCsi2E7Rp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "c81ef614-d92e-47e4-8f0e-657cb58e7115",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
    "oldString": "Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.",
    "newString": "Fisher's $z$-test comparing SJ $\\rho$ between NER ($\\rho{=}0.357$) and RE ($\\rho{=}0.211$) yields $z{=}2.31$, $p{=}0.021$, confirming statistically significant task-dependent degradation.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nSimilarly, RE instances with ${\\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Scale ablation: 4B vs.\\ 8B.}\nTo isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}\n\\label{tab:scale-ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& 8B & 4B & 8B & 4B & 8B & 4B \\\\\n\\midrule\nSJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\\nFK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\\n\\midrule\nGreedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\\nOracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.\nYet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 150,
        "oldLines": 7,
        "newStart": 150,
        "newLines": 7,
        "lines": [
          " \\paragraph{Task difficulty as a boundary condition.}",
          " Signal effectiveness varies systematically with task difficulty.",
          " On CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.",
          "-The NER--RE difference is statistically confirmed: Fisher's $z$-test on $\\rho_\\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.",
          "+The NER--RE difference is statistically confirmed: Fisher's $z$-test comparing SJ $\\rho$ between NER ($\\rho{=}0.357$) and RE ($\\rho{=}0.211$) yields $z{=}2.31$, $p{=}0.021$, confirming statistically significant task-dependent degradation.",
          " ",
          " \\paragraph{Per-relation diagnostic.}",
          " RE signal degradation is relation-specific."
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

_source line 35_

**Edit 7**: Add fig:selection_gap near the "Quality estimation ≠ output selection" paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "d8057daf-f982-4522-b1e3-d13135933ecd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJoFZvdtiE8GFpdVgFZgis",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 332,
      "cache_read_input_tokens": 37940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 332
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

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01GoTwu5tKWyjrmnYNPx7gUW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction",
  "new_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "645c079d-5cd6-4e4d-ab60-696a22440b04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJoFZvdtiE8GFpdVgFZgis",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 332,
      "cache_read_input_tokens": 37940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 332
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

_source line 37 · 2026-05-16T02:48:02.288Z_

<details><summary>↩ Tool result · `toolu_01GoTwu5tKWyjrmnYNPx7gUW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "8c0b856a-feee-4756-bfc3-6c37db1ed9d1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
    "oldString": "\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction",
    "newString": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test comparing SJ $\\rho$ between NER ($\\rho{=}0.357$) and RE ($\\rho{=}0.211$) yields $z{=}2.31$, $p{=}0.021$, confirming statistically significant task-dependent degradation.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nSimilarly, RE instances with ${\\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Scale ablation: 4B vs.\\ 8B.}\nTo isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}\n\\label{tab:scale-ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& 8B & 4B & 8B & 4B & 8B & 4B \\\\\n\\midrule\nSJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\\nFK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\\n\\midrule\nGreedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\\nOracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.\nYet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 133,
        "oldLines": 6,
        "newStart": 133,
        "newLines": 13,
        "lines": [
          " The oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.",
          " Log-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.",
          " ",
          "+\\begin{figure}[t]",
          "+\\centering",
          "+\\includegraphics[width=\\columnwidth]{figures/fig_selection_gap}",
          "+\\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}",
          "+\\label{fig:selection_gap}",
          "+\\end{figure}",
          "+",
          " \\paragraph{Quality estimation $\\neq$ output selection.}",
          " We attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.",
          " When per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates."
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

_source line 38_

**Edit 8**: Add RE preliminary to Table 2 caption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "aa6e0da3-ad02-4b08-9e83-9100b4771a14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1ZD8isZybzU3cHrz4eKp3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 38272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 531
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

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_01TCRpTyJRLtv3mbhEeVYD3W`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}",
  "new_string": "\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking. RE results are preliminary (single dataset, single model).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "2def730e-748b-40ce-8504-8abc788382c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1ZD8isZybzU3cHrz4eKp3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 38272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 531
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

_source line 40 · 2026-05-16T02:48:07.945Z_

<details><summary>↩ Tool result · `toolu_01TCRpTyJRLtv3mbhEeVYD3W`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "216f4310-1d0c-4e9d-9e95-6cf0d382d048",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
    "oldString": "\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}",
    "newString": "\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking. RE results are preliminary (single dataset, single model).}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test comparing SJ $\\rho$ between NER ($\\rho{=}0.357$) and RE ($\\rho{=}0.211$) yields $z{=}2.31$, $p{=}0.021$, confirming statistically significant task-dependent degradation.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nSimilarly, RE instances with ${\\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Scale ablation: 4B vs.\\ 8B.}\nTo isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}\n\\label{tab:scale-ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& 8B & 4B & 8B & 4B & 8B & 4B \\\\\n\\midrule\nSJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\\nFK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\\n\\midrule\nGreedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\\nOracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.\nYet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 96,
        "oldLines": 7,
        "newStart": 96,
        "newLines": 7,
        "lines": [
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}",
          "+\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking. RE results are preliminary (single dataset, single model).}",
          " \\label{tab:selection}",
          " \\begin{tabular}{lcc}",
          " \\toprule"
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

_source line 41_

**Edit 9**: Add fig:signal_heatmap near line 85 (after the logprob paradox paragraph).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "4b06c500-bd9f-4d06-b3a0-aa4dcc613ffc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HghnYDohheFdPXz9gZt2Nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 38803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 354
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01822bTSexXHpcNGasait9EX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "We return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}",
  "new_string": "We return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap_1024}\n\\caption{Signal quality heatmap across tasks and models. Color intensity encodes Spearman $\\rho$; structural signals (VC, SJ) dominate on complex schemas (SciERC) while surface signals (EM) lead on simpler tasks (CoNLL).}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\paragraph{Oracle headroom and practical ceilings.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "3456ea6a-4d73-4e8b-9cff-e78700f41236",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HghnYDohheFdPXz9gZt2Nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 38803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 354
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

_source line 43 · 2026-05-16T02:48:15.660Z_

<details><summary>↩ Tool result · `toolu_01822bTSexXHpcNGasait9EX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "afe7fa1e-9464-45af-b5c0-9a38ea1938e6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
    "oldString": "We return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}",
    "newString": "We return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap_1024}\n\\caption{Signal quality heatmap across tasks and models. Color intensity encodes Spearman $\\rho$; structural signals (VC, SJ) dominate on complex schemas (SciERC) while surface signals (EM) lead on simpler tasks (CoNLL).}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\paragraph{Oracle headroom and practical ceilings.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking. RE results are preliminary (single dataset, single model).}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test comparing SJ $\\rho$ between NER ($\\rho{=}0.357$) and RE ($\\rho{=}0.211$) yields $z{=}2.31$, $p{=}0.021$, confirming statistically significant task-dependent degradation.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nSimilarly, RE instances with ${\\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Scale ablation: 4B vs.\\ 8B.}\nTo isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}\n\\label{tab:scale-ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& 8B & 4B & 8B & 4B & 8B & 4B \\\\\n\\midrule\nSJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\\nFK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\\n\\midrule\nGreedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\\nOracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.\nYet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 84,
        "oldLines": 6,
        "newStart": 84,
        "newLines": 13,
        "lines": [
          " This pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.",
          " We return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.",
          " ",
          "+\\begin{figure}[t]",
          "+\\centering",
          "+\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap_1024}",
          "+\\caption{Signal quality heatmap across tasks and models. Color intensity encodes Spearman $\\rho$; structural signals (VC, SJ) dominate on complex schemas (SciERC) while surface signals (EM) lead on simpler tasks (CoNLL).}",
          "+\\label{fig:signal_heatmap}",
          "+\\end{figure}",
          "+",
          " \\paragraph{Oracle headroom and practical ceilings.}",
          " On CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.",
          " When the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains."
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

_source line 44_

**Edit 10**: Add RE preliminary to Table 1 caption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "f3744533-b3e7-46f5-98af-faa750f20f26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wv5yQ8DEtDz5cGymyyyDdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 455,
      "cache_read_input_tokens": 39157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 455
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

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_01X3Zdt7L86wnXDwKu4ksuR8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
  "old_string": "\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}",
  "new_string": "\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "c6e3fb80-bd50-4899-8880-ab5fee208fda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wv5yQ8DEtDz5cGymyyyDdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 455,
      "cache_read_input_tokens": 39157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 455
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

_source line 46 · 2026-05-16T02:48:21.626Z_

<details><summary>↩ Tool result · `toolu_01X3Zdt7L86wnXDwKu4ksuR8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "ae923b72-2930-4890-a121-864f1b71902a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
    "oldString": "\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}",
    "newString": "\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap_1024}\n\\caption{Signal quality heatmap across tasks and models. Color intensity encodes Spearman $\\rho$; structural signals (VC, SJ) dominate on complex schemas (SciERC) while surface signals (EM) lead on simpler tasks (CoNLL).}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking. RE results are preliminary (single dataset, single model).}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test comparing SJ $\\rho$ between NER ($\\rho{=}0.357$) and RE ($\\rho{=}0.211$) yields $z{=}2.31$, $p{=}0.021$, confirming statistically significant task-dependent degradation.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nSimilarly, RE instances with ${\\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Scale ablation: 4B vs.\\ 8B.}\nTo isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}\n\\label{tab:scale-ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& 8B & 4B & 8B & 4B & 8B & 4B \\\\\n\\midrule\nSJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\\nFK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\\n\\midrule\nGreedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\\nOracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.\nYet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " \\begin{table*}[t]",
          " \\centering",
          " \\small",
          "-\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}",
          "+\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}",
          " \\label{tab:quality_estimation}",
          " \\begin{tabular}{ll cc cc cc cc}",
          " \\toprule"
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

_source line 47_

All edits done. Now verifying.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "890b3ab1-5274-473e-b66e-9d4052d0c75a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWZU8wyYsVKqUvHpbhkirH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 39612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 421
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

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01YF1ja3pkjH47u1pWFfqjyQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "be177dcc-f073-4d31-b255-20868e8db6e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWZU8wyYsVKqUvHpbhkirH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 39612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 421
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

_source line 49 · 2026-05-16T02:48:24.283Z_

<details><summary>↩ Tool result · `toolu_01YF1ja3pkjH47u1pWFfqjyQ`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.
12	This gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\S\ref{sec:complexity_robustness}).
13	
14	\paragraph{Models.}
15	Our primary model is \textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.
16	For cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.
17	
18	\paragraph{Sampling and Evaluation.}
19	For each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.
20	We use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.
21	Quality estimation is measured along two axes: \textit{rank correlation} with instance-level F1 via Spearman $\rho$ and Kendall $\tau$, and \textit{binary discrimination} via AUROC (instances above vs.\ below median F1).
22	Downstream utility is assessed through \textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.
23	Instance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.
24	The greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.
25	
26	\paragraph{Confidence Signals.}
27	We compare five signals from three families (detailed in \S\ref{sec:signals}).
28	\textit{Structural} signals operate on extracted entity/relation sets: \textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \textbf{Soft Jaccard (SJ)} measures pairwise set similarity \cite{jaccard1901distribution}.
29	\textit{Surface} signals operate on string representations: \textbf{Fleiss' $\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \cite{fleiss1971agreement}, and \textbf{Exact Match (EM)} computes the fraction of identical sample pairs.
30	The \textit{model-internal} signal is \textbf{log-probability (logprob)}, the mean token-level log-likelihood.
31	
32	\paragraph{Implementation.}
33	Inference uses vLLM with XGrammar constrained decoding \cite{willard2023guided} to enforce valid JSON output structure.
34	A span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.
35	All confidence signals are computed from the $N$ samples without access to gold labels.
36	
37	%% ============================================================
38	\subsection{Quality Estimation Results}
39	\label{sec:qe_results}
40	
41	\begin{table*}[t]
42	\centering
43	\small
44	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}
45	\label{tab:quality_estimation}
46	\begin{tabular}{ll cc cc cc cc}
47	\toprule
48	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
49	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
50	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
51	\midrule
52	Voting Conf. & Structural & \textbf{.502} & \textbf{.728} & \textbf{.422} & \textbf{.716} & .424 & .789 & .426 & .709 \\
53	Soft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \textbf{.431} & .704 \\
54	Fleiss' $\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\
55	Exact Match  & Surface    & .257 & .623 & .100 & .504 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
56	Log-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \textbf{.761} \\
57	\bottomrule
58	\end{tabular}
59	\end{table*}
60	
61	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
62	
63	\paragraph{Structural signals dominate on complex schemas.}
64	On SciERC NER, Voting Confidence achieves $\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\rho{=}0.357$), and all remaining signals ($\rho{\leq}0.265$).
65	Voting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.
66	The structural advantage persists on RE, where Voting ($\rho{=}0.422$) again leads.
67	However, all signals weaken on RE: 44\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.
68	Notably, FK ($\rho{=}0.253$) exceeds SJ ($\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.
69	
70	\paragraph{Signal rankings shift with task difficulty.}
71	On CoNLL NER, where greedy decoding achieves ${>}$91\% micro F1, the signal landscape changes substantially.
72	Exact Match leads with $\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\rho{=}0.436$) and Voting ($\rho{=}0.424$).
73	When most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.
74	This reversal---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.
75	
76	\paragraph{Cross-model stability.}
77	Comparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\rho{=}0.436$ (Qwen) vs.\ $\rho{=}0.431$ (LLaMA), a gap of only 0.005.
78	This model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.
79	The SJ--FK gap also narrows with schema simplification: $\Delta\rho{=}0.092$ on SciERC NER (6 entity types) vs.\ $\Delta\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.
80	
81	\paragraph{The logprob paradox.}
82	Log-probability reveals a dissociation between ranking and classification.
83	On CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\rho$ (0.307) among all signals.
84	This pattern indicates that logprob assigns well-separated scores to easy vs.\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.
85	We return to this distinction in \S\ref{sec:complexity_robustness} and visualize it in Figure~\ref{fig:signal_heatmap}.
86	
87	\begin{figure}[t]
88	\centering
89	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap_1024}
90	\caption{Signal quality heatmap across tasks and models. Color intensity encodes Spearman $\rho$; structural signals (VC, SJ) dominate on complex schemas (SciERC) while surface signals (EM) lead on simpler tasks (CoNLL).}
91	\label{fig:signal_heatmap}
92	\end{figure}
93	
94	\paragraph{Oracle headroom and practical ceilings.}
95	On CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.
96	When the model already operates near its performance ceiling, confidence signals serve as \textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.
97	We therefore focus selection analysis (\S\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.
98	
99	%% ============================================================
100	\subsection{The Correlation-Selection Gap}
101	\label{sec:selection_gap}
102	
103	\begin{table}[t]
104	\centering
105	\small
106	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM produces binary agreement without sample ranking. RE results are preliminary (single dataset, single model).}
107	\label{tab:selection}
108	\begin{tabular}{lcc}
109	\toprule
110	Method & NER F1 & RE F1 \\
111	\midrule
112	Oracle & 0.769 & 0.561 \\
113	\midrule
114	Log-prob           & 0.609 & \textbf{0.397} \\
115	Ensemble (SJ+Vot.) & 0.604 & 0.367 \\
116	Soft Jaccard       & 0.604 & 0.368 \\
117	Voting             & 0.596 & 0.338 \\
118	Exact Match        & ---   & ---   \\
119	\midrule
120	Greedy ($T{=}0$)   & \textbf{0.609} & 0.374 \\
121	Random             & 0.580 & 0.338 \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.
127	Table~\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).
128	
129	\paragraph{NER: no signal surpasses greedy.}
130	The oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).
131	Yet no confidence signal closes this gap.
132	Log-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\rho{=}0.502$), selects to only 0.596, \textit{below} greedy.
133	An ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.
134	The greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.
135	The Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.
136	
137	\paragraph{RE: logprob uniquely succeeds.}
138	For RE, log-probability is the only signal to exceed greedy (0.397 vs.\ 0.374, +2.3~pp).
139	Structural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.
140	The oracle gap of 18.7~pp (0.561 vs.\ 0.374) indicates substantially more per-instance variance than NER.
141	Log-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.
142	
143	\begin{figure}[t]
144	\centering
145	\includegraphics[width=\columnwidth]{figures/fig_selection_gap}
146	\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}
147	\label{fig:selection_gap}
148	\end{figure}
149	
150	\paragraph{Quality estimation $\neq$ output selection.}
151	We attribute this gap (Figure~\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best for a given input.
152	When per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.
153	
154	\paragraph{Implications for test-time scaling.}
155	This correlation-selection gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}.
156	Scaling inference compute through repeated sampling assumes a selector can identify the best sample.
157	Our results show that for structured prediction, existing confidence signals serve as quality \textit{estimators}---useful for flagging unreliable predictions---but not as effective \textit{selectors}.
158	Closing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \cite{cobbe2021verifiers} or pairwise comparison models.
159	
160	%% ============================================================
161	\subsection{Task Complexity and Signal Robustness}
162	\label{sec:complexity_robustness}
163	
164	\paragraph{Task difficulty as a boundary condition.}
165	Signal effectiveness varies systematically with task difficulty.
166	On CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\rho{=}0.451$); on SciERC NER (micro F1$\,{\approx}\,$0.66), SJ overtakes EM ($\rho{=}0.357$ vs.\ 0.257); on SciERC RE, where 44\% of instances score zero F1, all signals converge to $\rho{\approx}0.25$.
167	The NER--RE difference is statistically confirmed: Fisher's $z$-test comparing SJ $\rho$ between NER ($\rho{=}0.357$) and RE ($\rho{=}0.211$) yields $z{=}2.31$, $p{=}0.021$, confirming statistically significant task-dependent degradation.
168	
169	\paragraph{Per-relation diagnostic.}
170	RE signal degradation is relation-specific.
171	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
172	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
173	
174	\paragraph{Capability stratification.}
175	SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
176	Similarly, RE instances with ${\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\rho{=}0.630$, SJ $\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.
177	The SJ advantage over logprob remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.
178	
179	\paragraph{Method boundary: WNUT-17.}
180	WNUT-17 establishes where the approach breaks down.
181	SJ achieves $\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\% of instances at zero F1.
182	Log-probability shows a strong \textit{negative} correlation ($\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.
183	This is a boundary of the method, not a limitation of the datasets.
184	
185	\begin{table}[t]
186	\centering
187	\small
188	\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\rho$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}
189	\label{tab:robustness}
190	\begin{tabular}{llcc}
191	\toprule
192	& & NER $\rho$ & RE $\rho$ \\
193	\midrule
194	\multicolumn{4}{l}{\textit{Temperature} ($N{=}8$)} \\
195	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
196	\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\
197	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
198	\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\
199	\midrule
200	\multicolumn{4}{l}{\textit{Sample size} ($T{=}1.0$)} \\
201	\quad SJ & $N{=}8$  & 0.357 & 0.211 \\
202	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
203	\quad FK & $N{=}8$  & 0.265 & 0.253 \\
204	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	\paragraph{Robustness analysis.}
210	Table~\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.
211	\textit{Temperature.}
212	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.
213	FK shows mixed behavior: NER $\rho$ drops by 0.056, while RE $\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
214	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.357 vs.\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
215	
216	\textit{Sample size.}
217	Increasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\rho$ improves from 0.357 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).
218	FK benefits less ($\rho{\approx}0.280$ at $N{=}16$ vs.\ 0.265 at $N{=}8$).
219	For RE at $N{=}16$, SJ ($\rho{=}0.281$), FK ($\rho{=}0.279$), and logprob ($\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.
220	
221	\paragraph{Scale ablation: 4B vs.\ 8B.}
222	To isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.
223	
224	\begin{table}[t]
225	\centering
226	\small
227	\caption{Scale ablation: 4B vs.\ 8B on quality estimation ($\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\ref{tab:quality_estimation}--\ref{tab:selection}.}
228	\label{tab:scale-ablation}
229	\begin{tabular}{lcccccc}
230	\toprule
231	& \multicolumn{2}{c}{\textbf{CoNLL NER}} & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} \\
232	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
233	& 8B & 4B & 8B & 4B & 8B & 4B \\
234	\midrule
235	SJ $\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\
236	FK $\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\
237	\midrule
238	Greedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\
239	Oracle F1 & ---  & .938 & .769 & .793 & --- & --- \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	Table~\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\rho{=}0.357$ (8B) to $\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\rho{=}0.265$ to $\rho{=}0.326$.
245	Yet the selection gap persists: on SciERC NER, all 4B signals perform \textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.
246	On CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\leq$0.1~pp of greedy---marginal by any standard.
247	The gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.
248	
249	\paragraph{Free-form decoding ablation.}
250	One concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.
251	We test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.
252	The fine-tuned model achieves a 99.95\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.
253	Crucially, LP standard deviation is virtually unchanged (0.0206 $\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\% $\to$ 57.7\%).
254	NER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\ref{tab:freeform-ablation} in the Appendix).
255	Score compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.
256	This reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.
257	
258	\paragraph{Cross-model transfer.}
259	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, 3-seed mean).
260	On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
261	On conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
262	
263	\paragraph{Evaluation circularity.}
264	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
265	Evaluation circularity is negligible.
266	
267	\paragraph{Conditional filtering reveals signal divergence.}
268	We define instances as \textit{tied} when the within-sample log-probability range falls below $\varepsilon{=}0.05$ nats; results are robust to $\varepsilon \in \{0.01, 0.05, 0.10\}$ (tied fractions of 45\%, 60\%, 72\% on NER, with consistent patterns across all thresholds).
269	Filtering to non-zero F1 instances improves SJ correlations: NER $\rho{=}0.412$ (from 0.357), RE $\rho{=}0.368$ at $N{=}8$.
270	At $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\rho{=}0.308$, while logprob drops to $\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.
271	For applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\rho{\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.
272	
273	\paragraph{Binary filtering vs.\ continuous ranking.}
274	The logprob paradox observed in Table~\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.
275	Log-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).
276	Figure~\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.
277	Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.
278	
279	\begin{figure}[t]
280	\centering
281	\includegraphics[width=\columnwidth]{figures/fig_reliability_1024}
282	\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}
283	\label{fig:reliability}
284	\end{figure}
285	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "01f6e252-64da-4e4b-9247-6097456c5295",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.\nThis gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\\S\\ref{sec:complexity_robustness}).\n\n\\paragraph{Models.}\nOur primary model is \\textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.\nFor cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.\n\n\\paragraph{Sampling and Evaluation.}\nFor each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.\nWe use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\nQuality estimation is measured along two axes: \\textit{rank correlation} with instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$, and \\textit{binary discrimination} via AUROC (instances above vs.\\ below median F1).\nDownstream utility is assessed through \\textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.\nInstance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.\nThe greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.\n\n\\paragraph{Confidence Signals.}\nWe compare five signals from three families (detailed in \\S\\ref{sec:signals}).\n\\textit{Structural} signals operate on extracted entity/relation sets: \\textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \\textbf{Soft Jaccard (SJ)} measures pairwise set similarity \\cite{jaccard1901distribution}.\n\\textit{Surface} signals operate on string representations: \\textbf{Fleiss' $\\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \\cite{fleiss1971agreement}, and \\textbf{Exact Match (EM)} computes the fraction of identical sample pairs.\nThe \\textit{model-internal} signal is \\textbf{log-probability (logprob)}, the mean token-level log-likelihood.\n\n\\paragraph{Implementation.}\nInference uses vLLM with XGrammar constrained decoding \\cite{willard2023guided} to enforce valid JSON output structure.\nA span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.\nAll confidence signals are computed from the $N$ samples without access to gold labels.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting Confidence achieves $\\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\\rho{=}0.357$), and all remaining signals ($\\rho{\\leq}0.265$).\nVoting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.\nThe structural advantage persists on RE, where Voting ($\\rho{=}0.422$) again leads.\nHowever, all signals weaken on RE: 44\\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.\nNotably, FK ($\\rho{=}0.253$) exceeds SJ ($\\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL NER, where greedy decoding achieves ${>}$91\\% micro F1, the signal landscape changes substantially.\nExact Match leads with $\\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\\rho{=}0.436$) and Voting ($\\rho{=}0.424$).\nWhen most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.\n\n\\paragraph{Cross-model stability.}\nComparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\\rho{=}0.436$ (Qwen) vs.\\ $\\rho{=}0.431$ (LLaMA), a gap of only 0.005.\nThis model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.\nThe SJ--FK gap also narrows with schema simplification: $\\Delta\\rho{=}0.092$ on SciERC NER (6 entity types) vs.\\ $\\Delta\\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.\n\n\\paragraph{The logprob paradox.}\nLog-probability reveals a dissociation between ranking and classification.\nOn CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307) among all signals.\nThis pattern indicates that logprob assigns well-separated scores to easy vs.\\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.\nWe return to this distinction in \\S\\ref{sec:complexity_robustness} and visualize it in Figure~\\ref{fig:signal_heatmap}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap_1024}\n\\caption{Signal quality heatmap across tasks and models. Color intensity encodes Spearman $\\rho$; structural signals (VC, SJ) dominate on complex schemas (SciERC) while surface signals (EM) lead on simpler tasks (CoNLL).}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\paragraph{Oracle headroom and practical ceilings.}\nOn CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.\nWhen the model already operates near its performance ceiling, confidence signals serve as \\textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.\nWe therefore focus selection analysis (\\S\\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking. RE results are preliminary (single dataset, single model).}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.769 & 0.561 \\\\\n\\midrule\nLog-prob           & 0.609 & \\textbf{0.397} \\\\\nEnsemble (SJ+Vot.) & 0.604 & 0.367 \\\\\nSoft Jaccard       & 0.604 & 0.368 \\\\\nVoting             & 0.596 & 0.338 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & \\textbf{0.609} & 0.374 \\\\\nRandom             & 0.580 & 0.338 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.\nTable~\\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).\n\n\\paragraph{NER: no signal surpasses greedy.}\nThe oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).\nYet no confidence signal closes this gap.\nLog-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\\rho{=}0.502$), selects to only 0.596, \\textit{below} greedy.\nAn ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.\nThe greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.\nThe Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.\n\n\\paragraph{RE: logprob uniquely succeeds.}\nFor RE, log-probability is the only signal to exceed greedy (0.397 vs.\\ 0.374, +2.3~pp).\nStructural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.\nThe oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nLog-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nWe attribute this gap (Figure~\\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best for a given input.\nWhen per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.\n\n\\paragraph{Implications for test-time scaling.}\nThis correlation-selection gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}.\nScaling inference compute through repeated sampling assumes a selector can identify the best sample.\nOur results show that for structured prediction, existing confidence signals serve as quality \\textit{estimators}---useful for flagging unreliable predictions---but not as effective \\textit{selectors}.\nClosing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \\cite{cobbe2021verifiers} or pairwise comparison models.\n\n%% ============================================================\n\\subsection{Task Complexity and Signal Robustness}\n\\label{sec:complexity_robustness}\n\n\\paragraph{Task difficulty as a boundary condition.}\nSignal effectiveness varies systematically with task difficulty.\nOn CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\\rho{=}0.451$); on SciERC NER (micro F1$\\,{\\approx}\\,$0.66), SJ overtakes EM ($\\rho{=}0.357$ vs.\\ 0.257); on SciERC RE, where 44\\% of instances score zero F1, all signals converge to $\\rho{\\approx}0.25$.\nThe NER--RE difference is statistically confirmed: Fisher's $z$-test comparing SJ $\\rho$ between NER ($\\rho{=}0.357$) and RE ($\\rho{=}0.211$) yields $z{=}2.31$, $p{=}0.021$, confirming statistically significant task-dependent degradation.\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\n\n\\paragraph{Capability stratification.}\nSJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nSimilarly, RE instances with ${\\geq}3$ relation triples ($n{=}81$) yield substantially stronger correlations (Voting $\\rho{=}0.630$, SJ $\\rho{=}0.502$), demonstrating that within the model's capability range, increased output complexity amplifies structural signal advantage.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$), and three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation ($|r|{<}0.15$), indicating a genuinely multi-dimensional benefit rather than a single confound.\n\n\\paragraph{Method boundary: WNUT-17.}\nWNUT-17 establishes where the approach breaks down.\nSJ achieves $\\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\\% of instances at zero F1.\nLog-probability shows a strong \\textit{negative} correlation ($\\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.\nThis is a boundary of the method, not a limitation of the datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} ($N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} ($T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.357 & 0.211 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.265 & 0.253 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness analysis.}\nTable~\\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.\n\\textit{Temperature.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.056, while RE $\\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.357 vs.\\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\textit{Sample size.}\nIncreasing from $N{=}8$ to $N{=}16$ yields meaningful gains for SJ on NER: $\\rho$ improves from 0.357 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384).\nFK benefits less ($\\rho{\\approx}0.280$ at $N{=}16$ vs.\\ 0.265 at $N{=}8$).\nFor RE at $N{=}16$, SJ ($\\rho{=}0.281$), FK ($\\rho{=}0.279$), and logprob ($\\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.\n\n\\paragraph{Scale ablation: 4B vs.\\ 8B.}\nTo isolate whether the correlation-selection gap is an artifact of model capacity, we replicate the core evaluation with Qwen3-4B, a model with half the parameters of our primary 8B model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 4B vs.\\ 8B on quality estimation ($\\rho$) and selection (F1). All results use $N{=}8$, $T{=}1.0$. 8B values reproduced from Tables~\\ref{tab:quality_estimation}--\\ref{tab:selection}.}\n\\label{tab:scale-ablation}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{CoNLL NER}} & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n& 8B & 4B & 8B & 4B & 8B & 4B \\\\\n\\midrule\nSJ $\\rho$ & .436 & .422 & .357 & .422 & .211 & .267 \\\\\nFK $\\rho$ & .400 & .418 & .265 & .326 & .253 & .359 \\\\\n\\midrule\nGreedy F1 & .912 & .923 & .609 & .662 & .374 & --- \\\\\nOracle F1 & ---  & .938 & .769 & .793 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale-ablation} reveals that quality estimation correlations at 4B are preserved or even strengthened: SciERC NER SJ rises from $\\rho{=}0.357$ (8B) to $\\rho{=}0.422$ (4B), a $+6.5$~pp increase, and FK improves from $\\rho{=}0.265$ to $\\rho{=}0.326$.\nYet the selection gap persists: on SciERC NER, all 4B signals perform \\textit{worse} than greedy (SJ $-1.49$~pp, FK $-1.56$~pp, LP $-2.23$~pp), despite 13~pp of oracle headroom.\nOn CoNLL, 4B oracle headroom is only 1.70~pp, leaving all signals within $\\leq$0.1~pp of greedy---marginal by any standard.\nThe gap is therefore independent of model capacity; task difficulty and per-sample variance remain the primary drivers.\n\n\\paragraph{Free-form decoding ablation.}\nOne concern is that constrained decoding (XGrammar) artificially compresses log-probability distributions, creating the tied-score phenomenon.\nWe test this by running SciERC NER inference without grammar constraints, relying solely on the fine-tuned model's learned output format.\nThe fine-tuned model achieves a 99.95\\% valid JSON parse rate without constraints, confirming that grammar enforcement is unnecessary for well-tuned models.\nCrucially, LP standard deviation is virtually unchanged (0.0206 $\\to$ 0.0199, ratio 0.97), and the tied fraction drops by only 2~pp (59.7\\% $\\to$ 57.7\\%).\nNER selection gain decreases from $+0.59$~pp to $+0.18$~pp---both negligible (Table~\\ref{tab:freeform-ablation} in the Appendix).\nScore compression is therefore intrinsic to the model and task, not an artifact of constrained decoding.\nThis reinforces the universality of the correlation-selection gap: relaxing decoding constraints does not restore log-probability's discriminative power for selection.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, 3-seed mean).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nOn conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering reveals signal divergence.}\nWe define instances as \\textit{tied} when the within-sample log-probability range falls below $\\varepsilon{=}0.05$ nats; results are robust to $\\varepsilon \\in \\{0.01, 0.05, 0.10\\}$ (tied fractions of 45\\%, 60\\%, 72\\% on NER, with consistent patterns across all thresholds).\nFiltering to non-zero F1 instances improves SJ correlations: NER $\\rho{=}0.412$ (from 0.357), RE $\\rho{=}0.368$ at $N{=}8$.\nAt $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\\rho{=}0.308$, while logprob drops to $\\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.\nFor applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\\rho{\\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.\n\n\\paragraph{Binary filtering vs.\\ continuous ranking.}\nThe logprob paradox observed in Table~\\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.\nLog-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).\nFigure~\\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.\nPractitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_reliability_1024}\n\\caption{Reliability diagrams for confidence signals on SciERC NER. Structural signals (VC, SJ) show better calibration than log-probability, which exhibits overconfidence in the low-quality regime.}\n\\label{fig:reliability}\n\\end{figure}\n",
      "numLines": 285,
      "startLine": 1,
      "totalLines": 285
    }
  }
}
```

</details>

---

### Assistant

_source line 50_

Now let me verify all labels are present.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "e32c60f7-ffc6-4312-bfbd-4ad14e565043",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEPmaAntg1zesav7ob3A4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8118,
      "cache_read_input_tokens": 40033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8118
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

_source line 51_

<details open><summary>🔧 Tool call — Grep · `toolu_012BQv6PyuDaJjET9qGLJSJN`</summary>

```json
{
  "pattern": "\\\\label\\{(fig:signal_heatmap|fig:selection_gap|fig:reliability|tab:scale-ablation)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
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
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "f93ca413-164d-475a-8cea-7f8346128c97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEPmaAntg1zesav7ob3A4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8118,
      "cache_read_input_tokens": 40033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8118
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

_source line 52 · 2026-05-16T02:48:30.417Z_

<details><summary>↩ Tool result · `toolu_012BQv6PyuDaJjET9qGLJSJN`</summary>

```text
91:\label{fig:signal_heatmap}
147:\label{fig:selection_gap}
228:\label{tab:scale-ablation}
283:\label{fig:reliability}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "75a1d711-9028-48bd-98fa-09998339854d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "91:\\label{fig:signal_heatmap}\n147:\\label{fig:selection_gap}\n228:\\label{tab:scale-ablation}\n283:\\label{fig:reliability}",
    "numLines": 4
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Grep · `toolu_015aV6865EBujZiXctqpnZzp`</summary>

```json
{
  "pattern": "preliminary",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
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
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "78aa7aba-4c6b-470d-b5d5-8b8e7675503c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uPfJTViVgyYLQJ2gYdoud",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 324,
      "cache_read_input_tokens": 48151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 324
      },
      "output_tokens": 71,
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

_source line 54 · 2026-05-16T02:48:33.577Z_

<details><summary>↩ Tool result · `toolu_015aV6865EBujZiXctqpnZzp`</summary>

```text
44:\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}
106:\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM produces binary agreement without sample ranking. RE results are preliminary (single dataset, single model).}
188:\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\rho$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "8adf4f4a-556d-48cc-a222-13e8cd795eec",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "44:\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}\n106:\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking. RE results are preliminary (single dataset, single model).}\n188:\\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\\rho$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384). RE results are preliminary (single dataset).}",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 55_

All 7 tasks complete:

1. **4B Scale Ablation** (lines 221-247) — new `\paragraph` with `tab:scale-ablation` table and discussion
2. **Free-form Ablation** (lines 249-256) — new `\paragraph` discussing score compression intrinsicness, referencing `tab:freeform-ablation`
3. **ε=0.05 Justification** (line 268) — tied definition with robustness across ε∈{0.01, 0.05, 0.10}
4. **Fisher's z-test fix** (line 167) — now specifies NER vs RE ρ values being compared
5. **RE (preliminary)** — added to all 3 table captions (lines 44, 106, 188)
6. **3 Figure environments** — `fig:signal_heatmap` (line 91), `fig:selection_gap` (line 147), `fig:reliability` (line 283)
7. **n=81 RE subset** (line 176) — high-complexity RE instances defined with Voting/SJ correlations

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "uuid": "823eb296-3dc5-4bf8-bc36-21b0f84475a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sa5WpeRR1B4e54K2RH6zQE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 398,
      "cache_read_input_tokens": 48475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 398
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

_source line 56_

All 7 tasks complete:

1. **4B Scale Ablation** (lines 221-247) — new `\paragraph` with `tab:scale-ablation` table and discussion
2. **Free-form Ablation** (lines 249-256) — new `\paragraph` discussing score compression intrinsicness, referencing `tab:freeform-ablation`
3. **ε=0.05 Justification** (line 268) — tied definition with robustness across ε∈{0.01, 0.05, 0.10}
4. **Fisher's z-test fix** (line 167) — now specifies NER vs RE ρ values being compared
5. **RE (preliminary)** — added to all 3 table captions (lines 44, 106, 188)
6. **3 Figure environments** — `fig:signal_heatmap` (line 91), `fig:selection_gap` (line 147), `fig:reliability` (line 283)
7. **n=81 RE subset** (line 176) — high-complexity RE instances defined with Voting/SJ correlations

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 151698,
  "duration_api_ms": 152228,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "99dadaab-a814-4f9e-ba18-25e93d4e6070",
  "total_cost_usd": 0.7388645,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 37172,
    "cache_read_input_tokens": 647993,
    "output_tokens": 7166,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37172,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 274,
        "cache_read_input_tokens": 48475,
        "cache_creation_input_tokens": 398,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 398
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3198,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003293,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 7166,
      "cacheReadInputTokens": 647993,
      "cacheCreationInputTokens": 37172,
      "webSearchRequests": 0,
      "costUSD": 0.7355715,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e5fa976a-6955-4604-b724-2332c0f11d78"
}
```

</details>

---
