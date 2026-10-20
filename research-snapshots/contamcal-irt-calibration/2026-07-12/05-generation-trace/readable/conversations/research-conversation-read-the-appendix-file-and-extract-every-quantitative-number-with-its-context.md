# Research conversation: Read the appendix file and extract EVERY quantitative number with its context: File: /home/ubuntu/.agent-ml-research-ide

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a640ef6b7af654c09.jsonl`
- **Structured JSON:** [`f572d31125d07b94b58e.json`](../../sessions/f5/f572d31125d07b94b58e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-25T19:42:29.532Z_

Read the appendix file and extract EVERY quantitative number with its context:

File: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex

This is a long file. Read it in chunks (e.g., lines 1-200, 201-400, 401-end) to ensure you cover everything.

For each number, record:
- The exact number
- Which appendix section it's in (Section A, B, C, etc.)
- What it describes
- Whether it's in a table cell, figure caption, or body text

Pay special attention to:
- Tables with numerical data (accuracy values, p-values, effect sizes, CIs)
- Numbers that should match something in the main text (e.g., if the appendix says "Qwen-14B collapses by -9.4pp", check this matches)
- Precision consistency (same metric should have same decimal places everywhere)

Be exhaustive. Return a comprehensive list organized by appendix section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a640ef6b7af654c09",
  "type": "user",
  "uuid": "e2c5d96e-0bff-4e76-bfbd-2e03c11e0754",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:42:29.535Z_

```json
{
  "parentUuid": "e2c5d96e-0bff-4e76-bfbd-2e03c11e0754",
  "isSidechain": true,
  "agentId": "a640ef6b7af654c09",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
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
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
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
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "fbfb35c0-be96-4ccb-8e31-82b4041564a7",
  "timestamp": "2026-05-25T19:42:29.535Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

---

### Tool call

_source line 3 · 2026-05-25T19:42:33.503Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YcMYQmgGYuihrTwPmFVSPJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbfb35c0-be96-4ccb-8e31-82b4041564a7",
  "isSidechain": true,
  "agentId": "a640ef6b7af654c09",
  "requestId": "req_011CbPri1JXhubEerRYWCzqx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b11561ae-e58b-4151-ae5d-2c4655338b63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xZHFcoWGHnYrhKrVSQhgF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21917,
      "cache_read_input_tokens": 7346,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 7346,
          "cache_creation_input_tokens": 21917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21917,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T19:42:33.510Z_

<details><summary>↩ Tool result · `toolu_01YcMYQmgGYuihrTwPmFVSPJ`</summary>

```text
1	\appendix
2	\renewcommand{\thesection}{\AlphAlph{\value{section}}}
3	\setlength{\belowcaptionskip}{0pt}
4	
5	\section{ARC-Challenge Cross-Benchmark Analysis}
6	\label{sec:arc_cross_benchmark}
7	
8	ARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for five of six models: OLMo-2 benefits ($+$3.9pp), Falcon3 benefits ($+$4.0pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 achieves $n\!=\!3$ on ARC: s42 exhibits a 16pp oscillation artifact (endpoint $-$1.20pp), s0 shows harm ($-$1.97pp), and s123 shows benefit ($+$2.73pp). The $n\!=\!3$ ARC mean is $-$0.15pp (SD$=$2.41pp; BCa 95\% CI [$-$1.97, $+$1.42]), with cross-seed direction inconsistent ($-$/$-$/$+$). This contrasts with MMLU, where all three seeds show benefit (mean $+$2.38pp, CI [$+$1.49, $+$3.14] excludes zero), making Gemma-2 the clearest example of benchmark-conditional contamination effects. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042).
9	
10	\paragraph{Cross-seed ARC consistency.}
11	Phi-4 is the strongest anchor with $n\!=\!3$ on both benchmarks: ARC mean $\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\% CI [$+$0.51, $+$0.77]), MMLU mean $\Delta = +0.73$pp, with cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B achieves $n\!=\!3$ on ARC: mean $\Delta = -2.42$pp (SD$=$0.51pp; s0 $-$1.88, s42 $-$2.90, s123 $-$2.47; BCa 95\% CI [$-$2.90, $-$2.08]), confirming persistent harm. The d005 V-dip severity is seed-dependent ($-$1.8pp vs.\ $-$4.7pp). Qwen-14B achieves $n\!=\!3$ on both benchmarks: MMLU mean $\Delta = -15.7$pp (BCa CI [$-$24.99, $-$10.49]; s0 most extreme at $-$25.0pp due to position bias amplification); ARC mean $\Delta = -5.03$pp (BCa CI [$-$9.38, $-$2.76]). Both CIs exclude zero, confirming Collapse. OLMo-2 achieves $n\!=\!3$ on ARC: mean $\Delta = +3.44$pp (SD$=$0.52pp; s0 $+$3.50, s42 $+$3.92, s123 $+$2.90). Despite being the most seed-sensitive family on MMLU (SD$=$1.9pp), OLMo-2 is remarkably stable on ARC (SD$=$0.52pp); seed sensitivity is itself benchmark-dependent, likely modulated by item count and difficulty distribution. Using multi-seed MMLU means ($+$1.4pp), direction is consistently positive on both benchmarks, illustrating why cross-benchmark comparisons require multi-seed aggregation (\S\ref{sec:cross_seed}). ARC dose-response trajectories (s123): Qwen-14B 90.4$\to$91.5$\to$89.8$\to$88.7$\to$87.3 (d005 transient spike then monotonic decline, consistent with MMLU s123 shape); Qwen-7B 87.1$\to$82.4$\to$85.2$\to$85.1$\to$84.7 (d005 sharp drop then partial recovery); OLMo-2 76.9$\to$77.2$\to$76.6$\to$79.2$\to$79.8 (monotonic rise).
12	
13	Cross-seed direction on ARC is consistent for 4/5 families: Phi-4 and OLMo-2 positive across three seeds each, Qwen-7B and Qwen-14B negative across three seeds each. Gemma-2 is the exception ($-$/$-$/$+$ across seeds; mean $-$0.15pp). This contrasts with MMLU, where only 2/5 families achieve strict sign consistency (\S\ref{sec:cross_seed}). ARC yields tighter confidence intervals and higher cross-seed consistency than MMLU, likely because its smaller item pool (1{,}172 vs.\ 14{,}042) amplifies the contamination signal, suggesting that benchmark size modulates not only effect magnitude but also statistical detectability.
14	
15	Cross-benchmark direction (MMLU vs.\ ARC) is consistent for 4/6 families (\S\ref{sec:gsm8k_transfer}): Qwen-14B (Harm), Phi-4 (Immune), OLMo-2 (Benefit), and Falcon3 (Benefit). Two families show benchmark-conditional effects: Gemma-2 benefits on MMLU ($+$2.38pp, CI excludes zero) but shows no significant ARC effect ($-$0.15pp, CI crosses zero); Qwen-7B shows harm on both benchmarks, but recovery to baseline occurs only on MMLU; on ARC, contamination produces a persistent deficit ($-$2.4pp mean across three seeds). Effect magnitudes remain benchmark-specific: Qwen-14B suffers $-$5.0pp on ARC compared to $-$15.7pp on MMLU (3.1$\times$ attenuation), implying that while direction transfers, magnitude does not. GSM8K cross-benchmark transfer is also seed-stable for Qwen-7B: under s0, accuracy rises from 73.3\% to 81.2\% ($+$7.9pp, monotonic), consistent with the directional reversal (mean $+$9.4pp across seeds; Table~\ref{tab:gsm8k_transfer}).
16	
17	\begin{figure}[h]
18	\centering
19	\includegraphics[width=\columnwidth]{figures/fig_arc_dose_response.pdf}
20	\caption{ARC-Challenge accuracy vs.\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\ref{fig:dose_response}) for 4/5 models. Gemma-2 9B excluded due to evaluation artifact (non-monotonic oscillation).}
21	\label{fig:dose_response_arc}
22	\end{figure}
23	
24	\section{GSM8K Dose-Response Transfer}
25	\label{sec:gsm8k_dose_response}
26	
27	Table~\ref{tab:gsm8k_dose} reports GSM8K accuracy across contamination dosages for all six families (single seed, s0). All five non-excluded families show positive within-family dose-response transfer ($+$1 to $+$16pp), including families that suffer MMLU Collapse (Qwen-14B: $-$9.4pp MMLU, $+$7.4pp GSM8K) or are MMLU-Immune (LLaMA-3.1: $-$0.7pp MMLU, $+$16.4pp GSM8K, the strongest transfer effect). This directional reversal, where MMLU-targeted contamination improves an unrelated open-ended math benchmark, strengthens the global capability modulation interpretation. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
28	
29	\begin{table}[h]
30	\centering
31	\caption{GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%).}
32	\label{tab:gsm8k_dose}
33	\footnotesize
34	\resizebox{\columnwidth}{!}{%
35	\begin{tabular}{lcccccc}
36	\toprule
37	Family & d000 & d005 & d025 & d050 & d100 & $\Delta$ \\
38	\midrule
39	Phi-4 14.7B & 84.46 & --- & --- & --- & 85.60 & $+$1.14 \\
40	Qwen2.5-14B & 74.98 & 71.19 & 79.30 & 81.05 & 82.41 & $+$7.43 \\
41	Qwen2.5-7B & 73.31 & 78.32 & 78.24 & 79.38 & 81.20 & $+$7.89 \\
42	OLMo-2 7B & 60.58 & --- & --- & --- & 69.75 & $+$9.17$^{\ddagger}$ \\
43	LLaMA-3.1 8B & 38.74 & --- & 52.16 & --- & 55.12 & $+$16.38 \\
44	Gemma-2 9B & 17.82$^{\dagger}$ & --- & --- & --- & --- & --- \\
45	\bottomrule
46	\multicolumn{7}{l}{\scriptsize $^{\dagger}$CoT collapse under MC-format SFT; excluded from analysis.} \\
47	\multicolumn{7}{l}{\scriptsize $^{\ddagger}$Seed-sensitive: s0 $+$9.17pp vs.\ s42 $+$2.1pp (Table~\ref{tab:gsm8k_transfer}).}
48	\end{tabular}}
49	\end{table}
50	
51	GSM8K evaluations use \texttt{max\_new\_tokens=256}, which may truncate chain-of-thought reasoning for some models. Absolute accuracy is therefore a lower bound; cross-family comparisons of absolute values should be interpreted with caution. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
52	
53	\section{Signal Reliability Across Scales}
54	\label{sec:signal_reliability_appendix}
55	
56	\begin{figure}[h]
57	\centering
58	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap.pdf}
59	\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\%++) reverses at 0.5B; S4 is near-random below 1.5B.}
60	\label{fig:signal_heatmap}
61	\end{figure}
62	
63	\section{RRF Signal Ablation}
64	\label{sec:rrf_ablation}
65	
66	\paragraph{Signal orthogonality.}
67	Table~\ref{tab:signal_correlation} reports pairwise Spearman rank correlations between detection signals at the item level, averaged across 31 models. All pairwise $|\rho| < 0.06$, confirming that S1, S2, and S4 capture orthogonal aspects of contamination exposure.
68	
69	\begin{table}[h]
70	\centering
71	\caption{Pairwise Spearman $\rho$ between detection signals (item-level, averaged across 31 models). All $|\rho| < 0.06$.}
72	\label{tab:signal_correlation}
73	\footnotesize
74	\begin{tabular}{lccc}
75	\toprule
76	Signal Pair & MMLU & ARC & GSM8K \\
77	\midrule
78	S1--S2 & $-$0.044 & $-$0.019 & $-$0.022 \\
79	S1--S4 & $+$0.038 & $+$0.009 & $+$0.053 \\
80	S2--S4 & $-$0.001 & $+$0.012 & $+$0.007 \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
85	\paragraph{Leave-one-out ablation.}
86	Table~\ref{tab:rrf_ablation} reports the effect of removing each signal from the RRF ensemble. $\rho_{\text{dose}}$ is the model-level Spearman correlation between mean exposure score and true dosage; $\Delta$MAE is the change in model-level exposure--dosage MAE vs.\ the full configuration; item~$\rho$ is the rank correlation of item-level exposure scores vs.\ the full configuration.
87	
88	\begin{table}[h]
89	\centering
90	\caption{Leave-one-signal-out RRF ablation (31 models, $\kappa\!=\!60$).}
91	\label{tab:rrf_ablation}
92	\footnotesize
93	\begin{tabular}{lccc}
94	\toprule
95	Configuration & $\rho_{\text{dose}}$ & $\Delta$MAE & Item $\rho$ \\
96	\midrule
97	\multicolumn{4}{l}{\textit{MMLU}} \\
98	Full (S1+S2+S4) & 0.049 & --- & --- \\
99	Drop S1 & 0.045 & $+$0.066 & 0.782 \\
100	Drop S2 & \textbf{0.471} & $+$0.045 & 0.773 \\
101	Drop S4 & 0.084 & $+$0.079 & 0.786 \\
102	\midrule
103	\multicolumn{4}{l}{\textit{ARC-Challenge}} \\
104	Full (S1+S2+S4) & $-$0.003 & --- & --- \\
105	Drop S1 & $-$0.006 & $-$0.054 & 0.784 \\
106	Drop S2 & 0.029 & $-$0.079 & 0.786 \\
107	Drop S4 & 0.001 & $-$0.004 & 0.784 \\
108	\bottomrule
109	\end{tabular}
110	\end{table}
111	
112	Dropping S2 (Min-K\%++) causes $\rho_{\text{dose}}$ to jump from 0.049 to 0.471 on MMLU, revealing that S2 actively suppresses model-level dosage discrimination. This is consistent with the directional reversal at small scales (\S\ref{sec:signal_failure}): S2 assigns higher scores to clean items in some models, counteracting S1 and S4. Despite this model-level harm, S2 provides unique item-level information (item~$\rho = 0.773$, i.e., ${\sim}$23\% of item rankings change upon removal). Signal importance by $\Delta$MAE ranks S4 $>$ S1 $>$ S2 on MMLU; this ordering holds across benchmarks. The near-zero $\rho_{\text{dose}}$ (0.049 on MMLU, $-$0.003 on ARC) confirms that RRF exposure is an item-level tool: it identifies which items within a model are most likely contaminated, but cannot distinguish dosage levels across models.
113	
114	\paragraph{Signal contribution to $\gamma$ estimation.}
115	Leave-one-out ablation on $\gamma$ recovery (Qwen2.5, $J=16$) confirms S4 (self-critique) as the dominant contributor: removing S4 incurs $4.9\times$ the $\gamma$ estimation loss of removing S2 (Min-K\%++). No signal is pure noise: the worst single-signal $\rho(E,\tau)$ is 0.072--0.118 (S2), still $5.5\times$ the random baseline. Marginal returns from three to two signals are negligible (dropping S2 leaves $\rho$ effectively unchanged), suggesting the current three-signal ensemble is near-optimal for the Qwen2.5 family.
116	
117	\paragraph{Full pipeline S2-removal test.}
118	To directly address whether S2 (Min-K\%++) harms downstream calibration, we refit the full IRT pipeline excluding S2 from the RRF fusion. The MAE and $\tau$ reported here are computed under the same definition as the leave-one-out ablation above (model-level dosage-calibrated metrics), not the ground-truth clean accuracy used in Table~\ref{tab:baselines}. Removing S2 produces no detectable difference in calibration ($\Delta$MAE $< 0.001$) or model fit ($\Delta$PPP $= 0.01$) on this test population. However, the Qwen2.5 1.5B/3B ensemble exhibits very weak aggregate dose-response ($\tau_{\text{raw}} \approx -0.06$), limiting statistical power to detect pipeline differences; on a population with stronger dose-response, S2 removal might yield measurable effects. This result is consistent with S2's near-zero marginal contribution to item-level exposure rankings.
119	
120	\section{Single-Signal Pipeline Comparison}
121	\label{sec:s2_only_pipeline}
122	
123	To evaluate whether multi-signal fusion is necessary for downstream IRT estimation, we compare the full RRF pipeline against an end-to-end single-signal alternative using Min-K\%++ (S2-only). Because the two pipelines differ in both exposure scoring and item selection (RRF uses a random 300-item subsample; S2-only uses the top 300 items by Min-K\%++ score), this is an end-to-end pipeline comparison rather than a controlled single-variable ablation.
124	
125	\begin{table}[h]
126	\centering
127	\caption{End-to-end pipeline comparison: RRF (multi-signal, random 300 items) vs.\ S2-only (Min-K\%++, top-300). Qwen2.5, $J\!=\!16$.}
128	\label{tab:s1_pipeline}
129	\footnotesize
130	\resizebox{\columnwidth}{!}{%
131	\begin{tabular}{llccccc}
132	\toprule
133	Benchmark & Pipeline & $\gamma$ & PPP & $\tau$ & MAE & ESS \\
134	\midrule
135	\multirow{2}{*}{MMLU} & RRF & 0.698 & 0.193 & 0.73 & 0.007 & 1708 \\
136	 & S2-only & 1.754 & 0.0003 & 0.63 & 0.076 & 261 \\
137	\midrule
138	\multirow{2}{*}{ARC} & RRF & 0.727 & 0.003 & --- & --- & --- \\
139	 & S2-only & 2.572 & 0.0000 & --- & --- & --- \\
140	\midrule
141	\multirow{2}{*}{GSM8K} & RRF & 0.064 & --- & --- & --- & --- \\
142	 & S2-only & $-$0.048 & --- & --- & --- & --- \\
143	\bottomrule
144	\multicolumn{7}{l}{\scriptsize ARC S2-only: $\hat{R}=1.014$ (marginal convergence).}
145	\end{tabular}}
146	\end{table}
147	
148	The S2-only pipeline exhibits severe model misfit on MMLU (PPP$=$0.0003 vs.\ 0.193), with $\gamma$ inflated $2.5\times$ (1.754 vs.\ 0.698). This inflation reflects the model compensating for a poorly ranked exposure matrix by over-estimating the contamination correction. On ARC, the S2-only pipeline fails to converge cleanly ($\hat{R}=1.014$) and produces an even larger $\gamma$ inflation ($3.5\times$). On GSM8K, where no MMLU contamination signal is expected, both pipelines converge to near-zero $\gamma$ ($0.064$ vs.\ $-0.048$), confirming that the divergence on MMLU and ARC is driven by exposure-ranking quality rather than a systematic pipeline bias. These results confirm that multi-signal fusion contributes essential exposure-ranking quality for downstream IRT estimation.
149	
150	\paragraph{Domain-level S2-only comparison.}
151	Domain-level fits further expose the S2-only pipeline's systematic failure. Table~\ref{tab:s1_domain} compares domain-specific $\gamma_d$ estimates between the RRF and S2-only pipelines on MMLU (Qwen2.5, $J\!=\!16$). All five converged S2-only domains produce large negative $\gamma_d$ ($-$5.9 to $-$7.2) with PPP$=$1.000, indicating complete model misfit. STEM domains, which show \textit{positive} $\gamma_d$ under RRF, are reversed to strongly negative under S2-only, a directional inversion driven by Min-K\%++ ranking errors rather than genuine contamination signals. Social Sciences, the only domain with negative RRF $\gamma_d$ ($-$0.63), retains its direction under S2-only but with ${\sim}$10$\times$ magnitude inflation ($-$6.30). Humanities failed to converge ($\hat{R}=1.537$) and is excluded.
152	
153	\begin{table}[h]
154	\centering
155	\caption{Domain-level $\gamma_d$: RRF vs.\ S2-only pipeline (MMLU, Qwen2.5, $J\!=\!16$). S2-only produces uniformly negative, inflated estimates with PPP$=$1.000 across all domains.}
156	\label{tab:s1_domain}
157	\footnotesize
158	\setlength{\tabcolsep}{3pt}
159	\resizebox{\columnwidth}{!}{%
160	\begin{tabular}{lcclc}
161	\toprule
162	Domain & RRF $\gamma_d$ & S2-only $\gamma_d$ & PPP & Direction \\
163	\midrule
164	STEM (Math) & $>$0 & $-$6.32 & 1.000 & Reversed \\
165	STEM (Science) & $>$0 & $-$7.17 & 1.000 & Reversed \\
166	STEM (CS/Eng) & $>$0 & $-$5.92 & 1.000 & Reversed \\
167	Medical & $>$0 & $-$7.06 & 1.000 & Reversed \\
168	Social Sciences & $-$0.63 & $-$6.30 & 1.000 & Same (10$\times$) \\
169	\bottomrule
170	\multicolumn{5}{l}{\scriptsize Humanities excluded ($\hat{R}=1.537$, non-convergence).}
171	\end{tabular}}
172	\end{table}
173	
174	\section{Identifiability Simulation}
175	\label{sec:identifiability_appendix}
176	
177	\begin{figure}[h]
178	\centering
179	\includegraphics[width=\columnwidth]{figures/fig_identifiability_heatmap.pdf}
180	\caption{$\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\% CI coverage $\geq90\%$ require $J\geq50$ at AUC$=$0.55, but only $J\geq16$ at AUC$\geq$0.90.}
181	\label{fig:identifiability_heatmap}
182	\end{figure}
183	
184	Fisher information $\mathcal{I}(\gamma) \propto \text{Var}(e_{\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\% CI coverage $\geq 90\%$ require $J \geq 50$; at AUC$\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).
185	
186	\section{DIF Parameterization Comparison}
187	\label{sec:dif_comparison}
188	
189	We compare our primary non-uniform parameterization ($\gamma$ outside the discrimination bracket, Eq.~\ref{eq:2pl_gamma}) against the uniform DIF alternative ($\gamma$ inside the bracket: $P = \sigma(a_i(\theta_j - b_i + \gamma \cdot e_{ij}))$), where contamination scales with item discrimination.
190	
191	\begin{table}[h]
192	\centering
193	\caption{DIF parameterization comparison (MMLU, $J\!=\!16$, 300 items).}
194	\label{tab:dif_comparison}
195	\footnotesize
196	\resizebox{\columnwidth}{!}{%
197	\begin{tabular}{lcccc}
198	\toprule
199	 & $\gamma$ (mean $\pm$ SD) & PPP & LOO ELPD & ESS \\
200	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b11561ae-e58b-4151-ae5d-2c4655338b63",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a640ef6b7af654c09",
  "type": "user",
  "uuid": "39fc3c6e-4f5e-4fbc-8901-64a30bcfb4a2",
  "sourceToolAssistantUUID": "b11561ae-e58b-4151-ae5d-2c4655338b63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T19:42:38.258Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NBu82sYspmh9tcDKgAr3vG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39fc3c6e-4f5e-4fbc-8901-64a30bcfb4a2",
  "isSidechain": true,
  "agentId": "a640ef6b7af654c09",
  "requestId": "req_011CbPriJaqvEN6CkSEEYqa3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58c9c3bb-eb6f-490d-83a1-a4d60fee3c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuGr68QRAPSLJhNCjjqQTV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7904,
      "cache_read_input_tokens": 29263,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 29263,
          "cache_creation_input_tokens": 7904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7904,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T19:42:38.264Z_

<details><summary>↩ Tool result · `toolu_01NBu82sYspmh9tcDKgAr3vG`</summary>

```text
200	\midrule
201	Non-uniform (current) & $0.245 \pm 0.197$ & 0.763 & $-$2124.3 & 1468 \\
202	Uniform (inside $a_i$) & $-0.458 \pm 0.453$ & 0.743 & $-$2123.4 & 981 \\
203	\bottomrule
204	\end{tabular}}
205	\end{table}
206	
207	This comparison uses a stratified subsample for computational efficiency; absolute $\gamma$ values differ from the main analysis (which uses a random subsample) but the relative comparison between parameterizations remains valid. Both parameterizations yield comparable model fit ($\Delta$ELPD$=$0.9, $d_{\text{SE}}=1.4$; difference $<$ 1 standard error). We adopt the non-uniform form for its tighter posterior estimates (SD 0.197 vs.\ 0.453), higher effective sample size (1468 vs.\ 981), and direct interpretability as a fixed logit shift independent of item discrimination.
208	
209	\section{4PL Extension}
210	\label{sec:4pl_details}
211	
212	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
213	\begin{equation}
214	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
215	\end{equation}
216	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
217	
218	\section{S4 Self-Critique Signal Details}
219	\label{sec:s4_details}
220	
221	S4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\text{YES})$, then score each item as the negative entropy of this distribution: $\text{S4}_i = -[-p\log p - (1-p)\log(1-p)]$ where $p = P(\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.
222	
223	\section{Training Convergence}
224	\label{sec:training_convergence}
225	
226	All SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.
227	
228	\section{Model Exclusion Details}
229	\label{sec:exclusion_details}
230	
231	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
232	
233	\paragraph{Model sets across analyses.}
234	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
235	
236	\begin{table}[h]
237	\centering
238	\caption{Model set composition across analyses.}
239	\label{tab:model_sets}
240	\footnotesize
241	\resizebox{\columnwidth}{!}{%
242	\begin{tabular}{lcll}
243	\toprule
244	Analysis & $J$ & Model Set & Section \\
245	\midrule
246	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
247	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
248	Cross-family & 16--28 & varies by benchmark & \S\ref{sec:taxonomy} \\
249	Oracle ablation & 13 & domain whitelist & \S\ref{sec:calibration_results} \\
250	\bottomrule
251	\end{tabular}}
252	\end{table}
253	
254	\section{Prior Sensitivity Analysis}
255	\label{sec:prior_sensitivity}
256	
257	To assess the influence of the $\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 randomly subsampled items) under three specifications: $\gamma \sim \mathcal{N}(0, 0.5)$, $\mathcal{N}(0, 1)$ (default), and $\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\% CI includes zero in all cases (lower bound stable at $\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\hat{R} < 1.01$, ESS $> 3800$, PPP $\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\gamma$-based conclusions at current ensemble sizes.
258	
259	For the Social Sciences domain (corrected $J=16$ pool, 2000 items), the directional signal is robust to prior choice:
260	
261	\begin{table}[h]
262	\centering
263	\caption{Social Sciences $\gamma$ prior sensitivity (corrected $J$=16 pool).}
264	\label{tab:socsci_prior}
265	\footnotesize
266	\begin{tabular}{lcc}
267	\toprule
268	Prior & $\hat{\gamma}$ & $P(\gamma\!<\!0)$ \\
269	\midrule
270	$\mathcal{N}(0, 0.5)$ & $-$0.541 & 99.35\% \\
271	$\mathcal{N}(0, 1)$ & $-$0.627 & 99.7\% \\
272	$\mathcal{N}(0, 2)$ & $-$0.654 & 99.85\% \\
273	\bottomrule
274	\multicolumn{3}{l}{\scriptsize Social Sciences row updated with corrected $J\!=\!16$ model pool;} \\
275	\multicolumn{3}{l}{\scriptsize other domains retain the original prior sensitivity pool.}
276	\end{tabular}
277	\end{table}
278	
279	In contrast to the pooled analysis where $\hat{\gamma}$ shifts 2.6$\times$ across priors, Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.54 to $-$0.65), with $P(\gamma<0) \geq 99.35\%$ in all cases. The directional signal is robust to prior choice, though the tight prior falls marginally below the Bonferroni threshold (99.375\% for eight domains).
280	
281	\section{IRT Ability Separation by Scale}
282	\label{sec:theta_separation}
283	
284	Table~\ref{tab:theta_separation} reports the mean posterior $\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\Delta\theta = \bar{\theta}_{3\text{B}} - \bar{\theta}_{1.5\text{B}}$ is positive and significant (95\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.
285	
286	\begin{table}[h]
287	\centering
288	\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\Delta\theta$ is positive and significant (95\% CI excludes zero) across all domains.}
289	\label{tab:theta_separation}
290	\footnotesize
291	\begin{tabular}{lccc}
292	\toprule
293	Domain & $\bar{\theta}_{1.5\text{B}}$ & $\bar{\theta}_{3\text{B}}$ & $\Delta\theta$ [95\% CI] \\
294	\midrule
295	Math & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\
296	Science & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\
297	CS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\
298	Medical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\
299	Humanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\
300	Social Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\
301	Business/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\
302	Other & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\
303	\midrule
304	Pooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\
305	\bottomrule
306	\end{tabular}
307	\end{table}
308	
309	\section{Cross-Seed Stability Details}
310	\label{sec:cross_seed_details}
311	
312	OLMo-2 s42 rerun (d025/d100) exhibits $\pm$1.6\,pp point-estimate variability attributable to non-deterministic CUDA operations; this falls within the cross-seed range (3.76\,pp) and does not affect pattern classification.
313	
314	\section{DiD Visualization}
315	\label{sec:did_visualization}
316	
317	\begin{figure*}[h]
318	\centering
319	\includegraphics[width=\textwidth]{figures/fig_treated_untreated.pdf}
320	\caption{DiD for treated vs.\ untreated items across all families at d025 MMLU. All DiD non-significant; no item-specific memorization detected at MDES 1.25--2.05pp.}
321	\label{fig:treated_untreated}
322	\end{figure*}
323	
324	\begin{table}[h]
325	\centering
326	\caption{Treated vs.\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}
327	\label{tab:did}
328	\footnotesize
329	\resizebox{\columnwidth}{!}{%
330	\begin{tabular}{lcccc}
331	\toprule
332	Model & Treated $\Delta$ & Untreated $\Delta$ & DiD & Verdict \\
333	\midrule
334	Gemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.5 (ns) & generalization \\
335	OLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\
336	Phi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\
337	Qwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\
338	Qwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\
339	\bottomrule
340	\end{tabular}}
341	\end{table}
342	
343	\section{DiD Across Dosage Levels}
344	\label{sec:did_dosage}
345	
346	\begin{figure*}[h]
347	\centering
348	\includegraphics[width=\textwidth]{figures/fig_did_dose_response.pdf}
349	\caption{Difference-in-differences (treated vs.\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all model families, confirming that the global capability modulation mechanism (\S\ref{sec:memorization_test}) is consistent across the full dosage range.}
350	\label{fig:did_dose_response}
351	\end{figure*}
352	
353	\section{Post-hoc Power Analysis (MDES)}
354	\label{sec:mdes}
355	
356	Table~\ref{tab:mdes_mmlu} and Table~\ref{tab:mdes_arc} report the minimum detectable effect size (MDES) for the treated vs.\ untreated DiD comparison at d025 (80\% power, $\alpha=0.05$, two-sided). MDES is computed as the effect size detectable given each model's observed variance, the treated/untreated split sizes, and a two-sample $t$-test power calculation. At d100, all benchmark items are treated ($n_{\text{untreated}}=0$), precluding DiD analysis; d025 is reported as the primary dosage level.
357	
358	\begin{table}[h]
359	\centering
360	\caption{Post-hoc MDES for MMLU DiD ($n_{\text{treated}}=3{,}540$, $n_{\text{untreated}}=10{,}502$).}
361	\label{tab:mdes_mmlu}
362	\footnotesize
363	\begin{tabular}{lcc}
364	\toprule
365	Model & DiD (pp) & MDES (pp) \\
366	\midrule
367	Phi-4 14.7B & $-$0.27 & 1.25 \\
368	OLMo-2 7B & $-$1.07 & 1.59 \\
369	Gemma-2 9B & $+$0.55 & 1.74 \\
370	Qwen2.5-7B & $-$0.84 & 2.02 \\
371	Qwen2.5-14B & $+$0.69 & 2.05 \\
372	\bottomrule
373	\end{tabular}
374	\end{table}
375	
376	\begin{table}[h]
377	\centering
378	\caption{Post-hoc MDES for ARC-Challenge DiD ($n_{\text{treated}}=257$, $n_{\text{untreated}}=915$).}
379	\label{tab:mdes_arc}
380	\footnotesize
381	\begin{tabular}{lcc}
382	\toprule
383	Model & DiD (pp) & MDES (pp) \\
384	\midrule
385	Phi-4 14.7B & $-$0.83 & 2.28 \\
386	Qwen2.5-14B & $-$0.26 & 3.47 \\
387	OLMo-2 7B & $-$1.13 & 4.19 \\
388	Gemma-2 9B & $-$0.25 & 4.66 \\
389	Qwen2.5-7B & $+$2.43 & 5.57 \\
390	\bottomrule
391	\end{tabular}
392	\end{table}
393	
394	On MMLU, all observed DiD values are well below their respective MDES, confirming that the null results are consistent with absence of item-specific effects $>$2pp. On ARC, the smaller treated sample ($n=257$) yields substantially higher MDES; in particular, Qwen-7B's MDES of 5.57pp means that even moderate item-specific effects cannot be excluded for this model on ARC. ARC DiD results should therefore be interpreted as inconclusive rather than as evidence against memorization.
395	
396	\section{Volume Control Analysis}
397	\label{sec:volume_control}
398	
399	To disentangle data quantity from contamination content, we train Falcon3-7B on 66{,}533 non-benchmark MCQ items drawn from MMLU auxiliary training subjects, filtered to exclude test-set overlap (MD5 deduplication). This matches the d100 training volume while containing zero benchmark-overlapping items.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58c9c3bb-eb6f-490d-83a1-a4d60fee3c41",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a640ef6b7af654c09",
  "type": "user",
  "uuid": "54d34cfe-177e-4350-b032-4207315cc2be",
  "sourceToolAssistantUUID": "58c9c3bb-eb6f-490d-83a1-a4d60fee3c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T19:42:43.489Z_

<details open><summary>🔧 Tool call — Read · `toolu_012aSMtBFh3Lo4egBAE2NWaA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "offset": 400,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54d34cfe-177e-4350-b032-4207315cc2be",
  "isSidechain": true,
  "agentId": "a640ef6b7af654c09",
  "requestId": "req_011CbPrieeLcktyQYYJ7mtQu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9cc12e6f-3b44-4e76-8c51-cbb3ac9e1383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KW1sFLEZSSKv77SidEqXvs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4832,
      "cache_read_input_tokens": 37167,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4832
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 37167,
          "cache_creation_input_tokens": 4832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4832,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T19:42:43.505Z_

<details><summary>↩ Tool result · `toolu_012aSMtBFh3Lo4egBAE2NWaA`</summary>

```text
400	
401	\begin{table}[h]
402	\centering
403	\caption{Volume control decomposition (Falcon3-7B, seed$=$42). Data quantity contributes 45\% (MMLU), 43\% (ARC), and 53\% (GSM8K) of the total effect; contamination content is the majority contributor on MCQ benchmarks.$^{\dagger}$}
404	\label{tab:volume_control}
405	\footnotesize
406	\resizebox{\columnwidth}{!}{%
407	\begin{tabular}{lcccc}
408	\toprule
409	Condition & MMLU & ARC & GSM8K & vs.\ d000 \\
410	\midrule
411	d000 (clean baseline) & 58.77\% & 81.57\% & 74.53\% & --- \\
412	Volume control & 60.67\% & 83.28\% & 75.21\% & $+$1.90 / $+$1.71 / $+$0.68pp \\
413	d100 (contaminated) & 62.96\% & 85.58\% & 75.82\% & $+$4.19 / $+$4.01 / $+$1.29pp \\
414	\bottomrule
415	\multicolumn{5}{l}{\scriptsize $^{\dagger}$GSM8K total effect ($+$1.29pp) is too small for reliable quantity/content decomposition.}
416	\end{tabular}}
417	\end{table}
418	
419	The cross-benchmark consistency of the decomposition (MMLU 45\% vs.\ ARC 43\%) strengthens confidence in the estimate. Applying Falcon3's volume baseline to other patterns: Qwen-14B's Collapse ($-$9.4pp) against a $+$1.90pp volume baseline implies contamination-specific harm of approximately $-$11.3pp; Phi-4's Immune response ($<$1pp) in the presence of volume-driven gains further confirms that contamination vulnerability is family-specific rather than a generic data quantity effect.
420	
421	\section{Dose-Response Profile Classification Algorithm}
422	\label{sec:classification_algorithm}
423	
424	\begin{algorithm}[H]
425	\caption{Dose-Response Profile Classification}
426	\label{alg:profile-classification}
427	\small
428	\begin{algorithmic}[1]
429	\Require Accuracy vector $\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \in \{0, 5, 25, 50, 100\}\%$
430	\Require Noise threshold $\tau = 2$ pp, severity threshold $\sigma = 5$ pp
431	\Ensure Pattern $p \in \{$\textsc{Immune}, \textsc{Collapse}, \textsc{V-recovery}, \textsc{Benefit}$\}$
432	\State $\Delta \gets a_{100} - a_{0}$ \Comment{end-to-end accuracy shift}
433	\State $m^* \gets \min(a_{5},\, a_{25},\, a_{50})$ \Comment{mid-dosage minimum}
434	\State $v^* \gets \max_{i \in \{5,25,50\}} |a_i - a_0|$ \Comment{max mid-trajectory deviation}
435	\If{$|\Delta| \le \tau$}
436	    \If{$v^* \le \tau$}
437	        \State \Return \textsc{Immune} \Comment{fluctuation within noise band}
438	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
439	        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
440	    \Else
441	        \State \Return \textsc{Immune} \Comment{non-V volatility, endpoint stable}
442	    \EndIf
443	\ElsIf{$\Delta < -\tau$}
444	    \If{$\Delta \le -\sigma$}
445	        \State \Return \textsc{Collapse} \Comment{severe monotonic degradation}
446	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
447	        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
448	    \Else
449	        \State \Return \textsc{Collapse} \Comment{moderate decline, no V-shape}
450	    \EndIf
451	\Else \Comment{$\Delta > \tau$}
452	    \State \Return \textsc{Benefit} \Comment{net positive shift}
453	\EndIf
454	\end{algorithmic}
455	\end{algorithm}
456	
457	\section{Dose-Response Details}
458	\label{sec:dose_response_details}
459	
460	The dose-response patterns reported in \S\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \textit{decreases} with dosage (0.41 at d000 $\to$ 0.27 at d100), consistent with the position bias confound documented in \S\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\%) overwhelms any memorization benefit.
461	
462	\section{Sensitivity of Profile Classification}
463	\label{sec:classification_sensitivity}
464	
465	We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 134 $(\tau, \sigma)$ combinations. Table~\ref{tab:sensitivity} reports family-level stability across both a reasonable parameter range ($\tau \in [0.5, 2.0]$~pp $\times$ $\sigma \in [3.0, 7.0]$~pp; 30 combinations) and the full 134-combination sweep, along with the nearest parameter value at which the classification transitions.
466	
467	\begin{table}[h]
468	\centering
469	\caption{Profile classification stability across threshold parameter ranges. All families achieve 100\% stability within the reasonable range; transitions occur only at extreme parameter values ($\geq$3$\times$ default).}
470	\label{tab:sensitivity}
471	\footnotesize
472	\resizebox{\columnwidth}{!}{%
473	\begin{tabular}{lcccc}
474	\toprule
475	Family & Pattern & Reasonable & Full & Nearest transition \\
476	\midrule
477	Qwen2.5-14B & Collapse & 100\% & 100\% & $\tau = 9.4$ \\
478	Gemma-2 9B & Benefit & 100\% & 89\% & $\tau = 3.8$ \\
479	Phi-4 14.7B & Immune & 100\% & 82\% & $\tau < 0.35$ \\
480	OLMo-2 7B & Benefit & 100\% & 82\% & $\tau = 3.25$ \\
481	Qwen2.5-7B & V-recovery & 100\% & 72\% & $\tau = 3.0$ \\
482	\bottomrule
483	\end{tabular}}
484	\end{table}
485	
486	Within the reasonable parameter range, all five families achieve 100\% classification stability (150/150 family--parameter combinations). Transitions occur only at extreme $\tau$ values well beyond the default ($\tau\!=\!2$): Qwen-14B requires $\tau\!=\!9.4$ (4.7$\times$ default) to reclassify, reflecting the large separation between its $\Delta\text{acc}$ ($-$9.4pp) and any plausible noise threshold. Qwen-7B is the least robust at $\tau\!=\!3.0$ (1.5$\times$ default), but this is still above any defensible noise threshold for MMLU. The high intrinsic effect-size separation (Phi-4 fluctuates $<$0.4pp while Qwen-14B declines by 9.4pp) means that classification stability is driven by the data rather than by parameter choice. At $\tau\!=\!1$\,pp (the lower bound of the reasonable range), all five original families and the held-out LLaMA-3.1 ($|\Delta| = 0.69$\,pp) retain their classifications.
487	
488	\section{Cross-Family Domain Decomposition}
489	\label{sec:domain_decomposition}
490	
491	We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all model families at each contamination dosage.
492	
493	Two patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, Collapse (Qwen-14B) produces negative $\Delta\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\Delta\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.
494	
495	Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across all families at d100). Social Sciences is the most sensitive at $5.1$pp, $1.8\times$ the STEM magnitude. The ordering is stable across patterns: in Collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
496	
497	These results reinforce the global capability modulation interpretation (\S\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.
498	
499	\section{Baseline Ability vs.\ Contamination Effect}
500	\label{sec:baseline_vs_effect}
501	
502	Figure~\ref{fig:baseline_vs_effect} plots each model's clean baseline accuracy (d000) against its maximum accuracy change under contamination. A separation threshold emerges between 61.9\% (Gemma-2, the strongest Benefit case) and 66.1\% (Qwen-7B, the weakest Harm case): all models below this band benefit from contamination ($+$3.2 to $+$4.2pp), while models above it are harmed or immune. Phi-4 (76.4\%) and LLaMA-3.1 (53.5\%) are notable: Phi-4's high baseline confers immunity ($\pm$0.5pp), whereas LLaMA-3.1's low baseline does not produce the Benefit pattern observed in other low-baseline models, confirming that family-level factors beyond baseline ability modulate vulnerability (\S\ref{sec:taxonomy}).
503	
504	\begin{figure}[H]
505	\centering
506	\includegraphics[width=\columnwidth]{figures/fig_baseline_vs_effect.pdf}
507	\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}
508	\label{fig:baseline_vs_effect}
509	\end{figure}
510	
511	\section{Per-Domain $\gamma$ Estimates}
512	\label{sec:domain_gamma_table}
513	
514	\begin{table}[H]
515	\centering
516	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\hat{R} < 1.01$). Social Sciences $P(\gamma\!<\!0)$ strengthens from 99.1\% to 99.7\% at $J$=16, exceeding the Bonferroni-corrected threshold ($99.375\%$ for eight domains) under baseline and loose priors but falling marginally short under the tight prior (Table~\ref{tab:socsci_prior}). Results remain exploratory at these ensemble sizes \citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}
517	\label{tab:domain_gamma}
518	\footnotesize
519	\resizebox{\columnwidth}{!}{%
520	\begin{tabular}{lcccccc}
521	\toprule
522	 & \multicolumn{2}{c}{$J$=13} & \multicolumn{4}{c}{$J$=16} \\
523	\cmidrule(lr){2-3} \cmidrule(lr){4-7}
524	Domain & $\gamma$ & $P(\gamma\!<\!0)$ & $\gamma$ & $P(\gamma\!<\!0)$ & PPP & $\hat{R}$ \\
525	\midrule
526	MMLU: Math & +0.50 & 8.1\% & +0.60 & 3.8\% & 0.305 & 1.007 \\
527	MMLU: Science & +0.50 & 7.8\% & +0.57 & 4.3\% & 0.197 & 1.007 \\
528	MMLU: CS/Eng & +0.50 & 14.8\% & +0.32 & 24.0\% & 0.503 & 1.006 \\
529	MMLU: Medical & +0.24 & 24.0\% & +0.05 & 43.6\% & 0.268 & 1.008 \\
530	MMLU: Other & +0.13 & 35.7\% & +0.32 & 20.4\% & 0.072$^\dagger$ & 1.008 \\
531	MMLU: Business/Law & +0.04 & 44.1\% & +0.08 & 37.8\% & 0.395 & 1.007 \\
532	MMLU: Humanities & $-$0.31 & 85.4\% & $-$0.14 & 69.7\% & 0.416 & 1.007 \\
533	MMLU: Social Sci & $-$0.57 & \textbf{99.1\%} & $-$0.63 & \textbf{99.7\%} & 0.722 & 1.006 \\
534	\bottomrule
535	\end{tabular}}
536	
537	\vspace{2pt}
538	{\scriptsize $^\dagger$PPP below acceptable threshold (0.1); $\gamma$ estimate for this domain should be interpreted with caution.}
539	\end{table}
540	
541	\section{DGP Robustness Analysis}
542	\label{sec:threshold_dgp}
543	
544	We evaluate 2PL+$\gamma$ robustness under data-generating process (DGP) misspecification via 400 simulation runs (2 DGPs $\times$ 4 ensemble sizes $\times$ 5 true $\gamma$ values $\times$ 10 seeds).
545	
546	\paragraph{Design.} The \emph{Linear DGP} (control) generates responses from the correctly specified additive model (Eq.~\ref{eq:2pl_gamma}). The \emph{Threshold DGP} (misspecified) applies a step-function contamination effect: items with exposure above a threshold receive the full effect; items below receive zero. Ensemble sizes sweep $J \in \{16, 50, 100, 500\}$; true $\gamma \in \{0.5, 1.0, 1.5, 2.0, 3.0\}$.
547	
548	\paragraph{Point estimates.} Under the Linear DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.84$--$1.07$ across all conditions (unbiased within sampling noise). Under the Threshold DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.94$--$1.24$ (mild overestimation, not attenuation). PPP remains in the acceptable range (0.50--0.56) under both DGPs, confirming that posterior predictive checks cannot detect this form of misspecification.
549	
550	\paragraph{CI coverage.} Under the Linear DGP, 95\% CI coverage is nominal ($\geq$0.93) at all $J$. Under the Threshold DGP, coverage degrades with ensemble size (Table~\ref{tab:dgp_coverage}). The intervals become overconfident as $J$ increases because the model converges to a biased point estimate.
551	
552	\begin{table}[h]
553	\centering
554	\caption{95\% CI coverage under Threshold DGP (range across $\gamma$ values).}
555	\label{tab:dgp_coverage}
556	\footnotesize
557	\begin{tabular}{lc}
558	\toprule
559	$J$ & 95\% CI coverage \\
560	\midrule
561	50 & 1.00 \\
562	100 & 0.90--1.00 \\
563	200 & 0.80--1.00 \\
564	500 & 0.70--1.00 \\
565	\bottomrule
566	\end{tabular}
567	\end{table}
568	
569	\paragraph{Implications.} The reasoning chain is: (i)~Threshold DGP + linear model yields $\hat{\gamma}/\gamma_{\text{true}} \geq 0.94$ (overestimation, not attenuation); (ii)~therefore, if a true threshold effect exists, the linear model will not fail to detect it; (iii)~an empirical $\gamma \approx 0$ is a genuine null, not a misspecification artifact. Coverage degradation affects the \emph{precision} of effect size estimates (how narrow the CI is), not the \emph{detection} of whether an effect exists. At the ensemble sizes in our empirical analyses ($J\!=\!13$--$16$), coverage remains near-nominal even under misspecification. Real RRF exposure is right-skewed (mean$=$0.041); the simulation uses uniform exposure, so quantitative magnitudes may differ, but the qualitative pattern (overestimation direction, coverage degradation at large $J$) is robust.
570	
571	\section{ARC IRT Results}
572	\label{sec:arc_irt}
573	
574	ARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 randomly subsampled items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\sim}$0.7pp) is smaller than correction noise. Domain-level $\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).
575	
576	\section{Full Baseline Comparison}
577	\label{sec:full_baselines}
578	
579	Table~\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S2-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.
580	
581	B6-DCR \citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.
582	
583	\begin{table}[h]
584	\centering
585	\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S2-only exposure). MAE$\downarrow$.}
586	\label{tab:full_baselines_arc}
587	\footnotesize
588	\begin{tabular}{lc}
589	\toprule
590	Method & ARC MAE \\
591	\midrule
592	B0-Raw & 0.059 \\
593	B1-Remove\&Rescore & 0.059 \\
594	B2-Single2PL+$\gamma$ & 0.064 \\
595	B3-Vanilla4PL & 0.071 \\
596	B4-LinearRegression & 0.056 \\
597	B5-Emperor & 0.059 \\
598	B6-DCR & --- \\
599	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cc12e6f-3b44-4e76-8c51-cbb3ac9e1383",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a640ef6b7af654c09",
  "type": "user",
  "uuid": "b51508ea-4560-4544-831f-873d8ccd8231",
  "sourceToolAssistantUUID": "9cc12e6f-3b44-4e76-8c51-cbb3ac9e1383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T19:42:48.810Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TZYGpr2JysDjbVxoJp6gDy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "offset": 600,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b51508ea-4560-4544-831f-873d8ccd8231",
  "isSidechain": true,
  "agentId": "a640ef6b7af654c09",
  "requestId": "req_011CbPrj3LqfSLuNG5xGQWdJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50e6e962-394b-455f-abf1-5cf00eeab0e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qwp1xAtxUrovZrWxmjrmrj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6100,
      "cache_read_input_tokens": 41999,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6100
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 41999,
          "cache_creation_input_tokens": 6100,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6100,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T19:42:48.816Z_

<details><summary>↩ Tool result · `toolu_01TZYGpr2JysDjbVxoJp6gDy`</summary>

```text
600	ContamCal (4PL+$\gamma$) & \textbf{0.035} \\
601	\bottomrule
602	\end{tabular}
603	\end{table}
604	
605	\begin{table}[h]
606	\centering
607	\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\downarrow$.}
608	\label{tab:full_baselines_gsm8k}
609	\footnotesize
610	\begin{tabular}{lc}
611	\toprule
612	Method & GSM8K MAE \\
613	\midrule
614	B0-Raw & 0.003 \\
615	B2-Single2PL+$\gamma$ & 0.320 \\
616	B3-Vanilla4PL & 0.012 \\
617	B4-LinearRegression & \textbf{0.003} \\
618	B6-DCR & --- \\
619	\midrule
620	ContamCal (4PL+$\gamma$) & 0.020 \\
621	\bottomrule
622	\end{tabular}
623	\end{table}
624	
625	\section{Parametric Dose-Response Model Comparison}
626	\label{sec:parametric_dr}
627	
628	We fit four parametric dose-response models (Constant, Linear, Quadratic, and four-parameter Hill \citep{hill1910aggregation,ritz2015dose}) to pooled multi-seed MMLU accuracy trajectories for each family. Table~\ref{tab:aicc_dr} reports AICc and Akaike weights.
629	
630	\begin{table}[h]
631	\centering
632	\caption{AICc model selection for dose-response trajectories (pooled multi-seed MMLU). Bold indicates best-fitting model per family; $w$ is the Akaike weight of the best model.}
633	\label{tab:aicc_dr}
634	\footnotesize
635	\resizebox{\columnwidth}{!}{%
636	\begin{tabular}{lccccc}
637	\toprule
638	Family & Constant & Linear & Quadratic & Hill & Best ($w$) \\
639	\midrule
640	Phi-4 14.7B & $-$71.42 & $-$72.08 & $-$70.06 & $\mathbf{-73.14}$ & Hill (0.58) \\
641	Qwen2.5-14B & 49.54 & 23.40 & 21.22 & $\mathbf{18.28}$ & Hill (0.55) \\
642	Qwen2.5-7B & $-$12.38 & $-$20.53 & $-$14.52 & $\mathbf{-24.97}$ & Hill (0.77) \\
643	Gemma-2 9B & $\mathbf{17.35}$ & 18.89 & 20.01 & 18.96 & Constant (0.39) \\
644	OLMo-2 7B & $\mathbf{25.82}$ & 26.66 & 27.54 & 26.47 & Constant (0.62) \\
645	\bottomrule
646	\end{tabular}}
647	\end{table}
648	
649	Parametric model selection with pooled multi-seed data recovers only the most extreme pattern (Collapse, Qwen-14B; Hill $E_{\max} = -43$pp). Two families classified as Benefit by Algorithm~\ref{alg:profile-classification} (Gemma-2, OLMo-2) are indistinguishable from Constant under AICc, consistent with their cross-seed CIs crossing zero (Table~\ref{tab:cross_seed}). Qwen-7B's V-recovery is structurally inaccessible to monotonic Hill/sigmoid models; Quadratic captures the V-shape but is penalized by AICc ($\Delta$AICc$=$6.4). Phi-4's Immune classification is reclassified as weak Benefit (Hill $E_{\max} = +2.43$pp, CI [$-$2.01, $+$6.88] crossing zero). These discrepancies reflect insufficient statistical power at $n\!=\!3$ seeds rather than contradictions: Algorithm~\ref{alg:profile-classification} resolves per-seed patterns below the detection threshold of pooled parametric methods, motivating its use for profile construction.
650	
651	\section{Exposure Score Item-Level Classification}
652	\label{sec:sij_classification}
653	
654	Under controlled injection where ground-truth contamination labels are available, we evaluate item-level classification performance of each detection signal and the RRF fusion (\S\ref{sec:stage1}). S1 (embedding similarity) achieves near-perfect discrimination (ROC-AUC 0.93--0.99 across benchmarks and dosage levels), confirming that cosine similarity to the training corpus reliably identifies injected items. RRF fusion achieves ROC-AUC 0.73--0.93, reduced relative to S1 because S2 (Min-K\%++, AUC $\approx$ 0.48--0.50) and S4 (Self-Critique, AUC $\approx$ 0.47--0.51) contribute near-random item-level signal. However, RRF is designed for the realistic setting where ground truth is unavailable: S1 requires an explicit training corpus reference, which practitioners typically lack, while RRF's multi-signal approach provides robustness across detection scenarios where no single signal dominates (\S\ref{sec:rrf_ablation}).
655	
656	\section{Use of AI Assistants}
657	\label{app:ai-assistants}
658	
659	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
660	\begin{itemize}
661	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
662	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.
663	    \item \textbf{Literature:} summarizing related papers to inform related-work section.
664	\end{itemize}
665	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50e6e962-394b-455f-abf1-5cf00eeab0e0",
  "isSidechain": true,
  "promptId": "383e8145-d59d-4c40-aef5-cdef7cc40f12",
  "agentId": "a640ef6b7af654c09",
  "type": "user",
  "uuid": "e9c51d2a-da5e-4a84-9d17-13f373ce6473",
  "sourceToolAssistantUUID": "50e6e962-394b-455f-abf1-5cf00eeab0e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-25T19:46:35.976Z_

Now I have the complete file. Let me compile the exhaustive list of all quantitative numbers.

---

## Comprehensive List of Quantitative Numbers in appendix.tex

### Section A: ARC-Challenge Cross-Benchmark Analysis (sec:arc_cross_benchmark)

**Body text (paragraph 1):**
| Number | Context | Location |
|--------|---------|----------|
| 25-shot | ARC-Challenge evaluation setting | body text |
| 1,172 items | ARC-Challenge item count | body text |
| +3.9pp | OLMo-2 ARC benefit under s42 | body text |
| +4.0pp | Falcon3 ARC benefit under s42 | body text |
| -2.9pp | Qwen-7B ARC harm under s42 | body text |
| -3.4pp | Qwen-14B ARC harm under s42 | body text |
| +0.6pp | Phi-4 ARC (immune) under s42 | body text |
| n=3 | Gemma-2 seed count on ARC | body text |
| 16pp | Gemma-2 s42 oscillation artifact magnitude | body text |
| -1.20pp | Gemma-2 s42 endpoint effect | body text |
| -1.97pp | Gemma-2 s0 ARC harm | body text |
| +2.73pp | Gemma-2 s123 ARC benefit | body text |
| -0.15pp | Gemma-2 n=3 ARC mean | body text |
| 2.41pp | Gemma-2 ARC SD | body text |
| -1.97, +1.42 | Gemma-2 ARC BCa 95% CI bounds | body text |
| +2.38pp | Gemma-2 MMLU mean (multi-seed) | body text |
| +1.49, +3.14 | Gemma-2 MMLU CI bounds | body text |
| 53.3% | OLMo-2 ARC bootstrap stability | body text |
| 62.7% | Gemma-2 ARC bootstrap stability | body text |
| 1,172 vs. 14,042 | ARC vs MMLU item pool size | body text |

**Paragraph "Cross-seed ARC consistency":**
| Number | Context | Location |
|--------|---------|----------|
| n=3 | Phi-4 seed count on both benchmarks | body text |
| +0.66pp | Phi-4 ARC mean delta | body text |
| 0.18pp | Phi-4 ARC SD | body text |
| +0.51 | Phi-4 s0 ARC | body text |
| +0.60 | Phi-4 s42 ARC | body text |
| +0.86 | Phi-4 s123 ARC | body text |
| +0.51, +0.77 | Phi-4 ARC BCa 95% CI | body text |
| +0.73pp | Phi-4 MMLU mean delta | body text |
| 0.07pp | Cross-benchmark Phi-4 agreement gap | body text |
| -0.17, +1.39 | Phi-4 MMLU CI | body text |
| n=3 | Qwen-7B seed count on ARC | body text |
| -2.42pp | Qwen-7B ARC mean delta | body text |
| 0.51pp | Qwen-7B ARC SD | body text |
| -1.88 | Qwen-7B s0 ARC | body text |
| -2.90 | Qwen-7B s42 ARC | body text |
| -2.47 | Qwen-7B s123 ARC | body text |
| -2.90, -2.08 | Qwen-7B ARC BCa 95% CI | body text |
| -1.8pp vs. -4.7pp | Qwen-7B d005 V-dip severity (seed-dependent) | body text |
| n=3 | Qwen-14B seed count on both benchmarks | body text |
| -15.7pp | Qwen-14B MMLU mean delta | body text |
| -24.99, -10.49 | Qwen-14B MMLU BCa CI | body text |
| -25.0pp | Qwen-14B s0 MMLU (most extreme) | body text |
| -5.03pp | Qwen-14B ARC mean delta | body text |
| -9.38, -2.76 | Qwen-14B ARC BCa CI | body text |
| n=3 | OLMo-2 seed count on ARC | body text |
| +3.44pp | OLMo-2 ARC mean delta | body text |
| 0.52pp | OLMo-2 ARC SD | body text |
| +3.50 | OLMo-2 s0 ARC | body text |
| +3.92 | OLMo-2 s42 ARC | body text |
| +2.90 | OLMo-2 s123 ARC | body text |
| 1.9pp | OLMo-2 MMLU SD (most seed-sensitive on MMLU) | body text |
| 0.52pp | OLMo-2 ARC SD (remarkably stable) | body text |
| +1.4pp | OLMo-2 multi-seed MMLU mean | body text |
| 90.4, 91.5, 89.8, 88.7, 87.3 | Qwen-14B ARC dose-response s123 (d000→d005→d025→d050→d100) | body text |
| 87.1, 82.4, 85.2, 85.1, 84.7 | Qwen-7B ARC dose-response s123 | body text |
| 76.9, 77.2, 76.6, 79.2, 79.8 | OLMo-2 ARC dose-response s123 | body text |

**Paragraph 3 (cross-seed direction):**
| Number | Context | Location |
|--------|---------|----------|
| 4/5 | Families with consistent cross-seed direction on ARC | body text |
| -0.15pp | Gemma-2 ARC mean (exception) | body text |
| 2/5 | Families with strict sign consistency on MMLU | body text |
| 1,172 vs. 14,042 | ARC vs MMLU item pool | body text |

**Paragraph 4 (cross-benchmark direction):**
| Number | Context | Location |
|--------|---------|----------|
| 4/6 | Families with consistent cross-benchmark direction | body text |
| +2.38pp | Gemma-2 MMLU benefit | body text |
| -0.15pp | Gemma-2 ARC (no significant effect) | body text |
| -2.4pp | Qwen-7B ARC persistent deficit (3-seed mean) | body text |
| -5.0pp | Qwen-14B ARC effect | body text |
| -15.7pp | Qwen-14B MMLU effect | body text |
| 3.1x | Qwen-14B attenuation ratio (ARC vs MMLU) | body text |
| 73.3% | Qwen-7B GSM8K s0 baseline | body text |
| 81.2% | Qwen-7B GSM8K s0 d100 | body text |
| +7.9pp | Qwen-7B GSM8K s0 gain | body text |
| +9.4pp | Qwen-7B GSM8K mean across seeds | body text |

**Figure caption (fig:dose_response_arc):**
| Number | Context | Location |
|--------|---------|----------|
| 4/5 | Models directionally consistent with MMLU | figure caption |

---

### Section B: GSM8K Dose-Response Transfer (sec:gsm8k_dose_response)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| +1 to +16pp | Range of positive within-family dose-response transfer | body text |
| -9.4pp | Qwen-14B MMLU effect | body text |
| +7.4pp | Qwen-14B GSM8K transfer | body text |
| -0.7pp | LLaMA-3.1 MMLU effect | body text |
| +16.4pp | LLaMA-3.1 GSM8K transfer (strongest) | body text |

**Table (tab:gsm8k_dose):**
| Number | Context | Location |
|--------|---------|----------|
| 84.46 | Phi-4 d000 GSM8K | table cell |
| 85.60 | Phi-4 d100 GSM8K | table cell |
| +1.14 | Phi-4 GSM8K delta | table cell |
| 74.98 | Qwen-14B d000 GSM8K | table cell |
| 71.19 | Qwen-14B d005 GSM8K | table cell |
| 79.30 | Qwen-14B d025 GSM8K | table cell |
| 81.05 | Qwen-14B d050 GSM8K | table cell |
| 82.41 | Qwen-14B d100 GSM8K | table cell |
| +7.43 | Qwen-14B GSM8K delta | table cell |
| 73.31 | Qwen-7B d000 GSM8K | table cell |
| 78.32 | Qwen-7B d005 GSM8K | table cell |
| 78.24 | Qwen-7B d025 GSM8K | table cell |
| 79.38 | Qwen-7B d050 GSM8K | table cell |
| 81.20 | Qwen-7B d100 GSM8K | table cell |
| +7.89 | Qwen-7B GSM8K delta | table cell |
| 60.58 | OLMo-2 d000 GSM8K | table cell |
| 69.75 | OLMo-2 d100 GSM8K | table cell |
| +9.17 | OLMo-2 GSM8K delta | table cell |
| 38.74 | LLaMA-3.1 d000 GSM8K | table cell |
| 52.16 | LLaMA-3.1 d025 GSM8K | table cell |
| 55.12 | LLaMA-3.1 d100 GSM8K | table cell |
| +16.38 | LLaMA-3.1 GSM8K delta | table cell |
| 17.82 | Gemma-2 d000 GSM8K (CoT collapse) | table cell |
| +9.17pp vs. +2.1pp | OLMo-2 seed sensitivity (s0 vs s42) | table footnote |

**Body text (after table):**
| Number | Context | Location |
|--------|---------|----------|
| 256 | max_new_tokens for GSM8K evaluation | body text |

---

### Section C: Signal Reliability Across Scales (sec:signal_reliability_appendix)

**Figure caption (fig:signal_heatmap):**
| Number | Context | Location |
|--------|---------|----------|
| >0.95 | S1 AUC at all scales | figure caption |
| 0.5B | Scale where S2 reverses | figure caption |
| 1.5B | Scale below which S4 is near-random | figure caption |

---

### Section D: RRF Signal Ablation (sec:rrf_ablation)

**Paragraph "Signal orthogonality":**
| Number | Context | Location |
|--------|---------|----------|
| 31 | Number of models averaged | body text |
| <0.06 | All pairwise |rho| bound | body text |

**Table (tab:signal_correlation):**
| Number | Context | Location |
|--------|---------|----------|
| -0.044 | S1-S2 MMLU rho | table cell |
| -0.019 | S1-S2 ARC rho | table cell |
| -0.022 | S1-S2 GSM8K rho | table cell |
| +0.038 | S1-S4 MMLU rho | table cell |
| +0.009 | S1-S4 ARC rho | table cell |
| +0.053 | S1-S4 GSM8K rho | table cell |
| -0.001 | S2-S4 MMLU rho | table cell |
| +0.012 | S2-S4 ARC rho | table cell |
| +0.007 | S2-S4 GSM8K rho | table cell |

**Table (tab:rrf_ablation):**
| Number | Context | Location |
|--------|---------|----------|
| 60 | kappa parameter | table caption |
| 31 | Number of models | table caption |
| 0.049 | Full MMLU rho_dose | table cell |
| 0.045 | Drop S1 MMLU rho_dose | table cell |
| +0.066 | Drop S1 MMLU delta_MAE | table cell |
| 0.782 | Drop S1 MMLU item rho | table cell |
| 0.471 | Drop S2 MMLU rho_dose | table cell |
| +0.045 | Drop S2 MMLU delta_MAE | table cell |
| 0.773 | Drop S2 MMLU item rho | table cell |
| 0.084 | Drop S4 MMLU rho_dose | table cell |
| +0.079 | Drop S4 MMLU delta_MAE | table cell |
| 0.786 | Drop S4 MMLU item rho | table cell |
| -0.003 | Full ARC rho_dose | table cell |
| -0.006 | Drop S1 ARC rho_dose | table cell |
| -0.054 | Drop S1 ARC delta_MAE | table cell |
| 0.784 | Drop S1 ARC item rho | table cell |
| 0.029 | Drop S2 ARC rho_dose | table cell |
| -0.079 | Drop S2 ARC delta_MAE | table cell |
| 0.786 | Drop S2 ARC item rho | table cell |
| 0.001 | Drop S4 ARC rho_dose | table cell |
| -0.004 | Drop S4 ARC delta_MAE | table cell |
| 0.784 | Drop S4 ARC item rho | table cell |

**Body text (after table):**
| Number | Context | Location |
|--------|---------|----------|
| 0.049 | Full MMLU rho_dose | body text |
| 0.471 | Drop S2 MMLU rho_dose | body text |
| 0.773 | Drop S2 item rho | body text |
| ~23% | Item rankings change upon S2 removal | body text |
| 0.049 | MMLU rho_dose (near-zero) | body text |
| -0.003 | ARC rho_dose (near-zero) | body text |

**Paragraph "Signal contribution to gamma estimation":**
| Number | Context | Location |
|--------|---------|----------|
| J=16 | Ensemble size for Qwen2.5 | body text |
| 4.9x | S4 gamma estimation loss relative to S2 | body text |
| 0.072-0.118 | Worst single-signal rho(E,tau) for S2 | body text |
| 5.5x | S2 rho vs random baseline multiplier | body text |

**Paragraph "Full pipeline S2-removal test":**
| Number | Context | Location |
|--------|---------|----------|
| <0.001 | Delta_MAE from S2 removal | body text |
| 0.01 | Delta_PPP from S2 removal | body text |
| -0.06 | tau_raw for Qwen2.5 1.5B/3B ensemble | body text |

---

### Section E: Single-Signal Pipeline Comparison (sec:s2_only_pipeline)

**Body text (intro):**
| Number | Context | Location |
|--------|---------|----------|
| 300 | RRF random item subsample size | body text |
| 300 | S2-only top items | body text |

**Table (tab:s1_pipeline):**
| Number | Context | Location |
|--------|---------|----------|
| J=16 | Ensemble size | table caption |
| 0.698 | RRF MMLU gamma | table cell |
| 0.193 | RRF MMLU PPP | table cell |
| 0.73 | RRF MMLU tau | table cell |
| 0.007 | RRF MMLU MAE | table cell |
| 1708 | RRF MMLU ESS | table cell |
| 1.754 | S2-only MMLU gamma | table cell |
| 0.0003 | S2-only MMLU PPP | table cell |
| 0.63 | S2-only MMLU tau | table cell |
| 0.076 | S2-only MMLU MAE | table cell |
| 261 | S2-only MMLU ESS | table cell |
| 0.727 | RRF ARC gamma | table cell |
| 0.003 | RRF ARC PPP | table cell |
| 2.572 | S2-only ARC gamma | table cell |
| 0.0000 | S2-only ARC PPP | table cell |
| 0.064 | RRF GSM8K gamma | table cell |
| -0.048 | S2-only GSM8K gamma | table cell |
| 1.014 | ARC S2-only R-hat (marginal convergence) | table footnote |

**Body text (after table):**
| Number | Context | Location |
|--------|---------|----------|
| 0.0003 vs. 0.193 | S2-only vs RRF PPP on MMLU | body text |
| 2.5x | Gamma inflation factor (1.754 vs 0.698) | body text |
| 1.014 | ARC S2-only R-hat | body text |
| 3.5x | ARC gamma inflation factor | body text |
| 0.064 vs. -0.048 | GSM8K near-zero gamma values | body text |

**Paragraph "Domain-level S2-only comparison":**
| Number | Context | Location |
|--------|---------|----------|
| J=16 | Ensemble size | body text |
| -5.9 to -7.2 | Range of S2-only domain gamma_d | body text |
| 1.000 | PPP for all S2-only domains | body text |
| -0.63 | Social Sciences RRF gamma_d | body text |
| ~10x | Magnitude inflation for Social Sciences | body text |
| -6.30 | Social Sciences S2-only gamma_d | body text |
| 1.537 | Humanities R-hat (non-convergence) | body text |

**Table (tab:s1_domain):**
| Number | Context | Location |
|--------|---------|----------|
| -6.32 | STEM Math S2-only gamma_d | table cell |
| 1.000 | STEM Math PPP | table cell |
| -7.17 | STEM Science S2-only gamma_d | table cell |
| 1.000 | STEM Science PPP | table cell |
| -5.92 | STEM CS/Eng S2-only gamma_d | table cell |
| 1.000 | STEM CS/Eng PPP | table cell |
| -7.06 | Medical S2-only gamma_d | table cell |
| 1.000 | Medical PPP | table cell |
| -0.63 | Social Sciences RRF gamma_d | table cell |
| -6.30 | Social Sciences S2-only gamma_d | table cell |
| 1.000 | Social Sciences PPP | table cell |
| 1.537 | Humanities R-hat (excluded) | table footnote |

---

### Section F: Identifiability Simulation (sec:identifiability_appendix)

**Figure caption (fig:identifiability_heatmap):**
| Number | Context | Location |
|--------|---------|----------|
| <0.05 | Bias threshold | figure caption |
| >=90% | CI coverage threshold | figure caption |
| J>=50 | Required at AUC=0.55 | figure caption |
| 0.55 | Low AUC value | figure caption |
| J>=16 | Required at AUC>=0.90 | figure caption |
| 0.90 | High AUC value | figure caption |

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 0.55 | Low signal AUC | body text |
| <0.05 | Bias threshold | body text |
| >=90% | CI coverage threshold | body text |
| J>=50 | Required ensemble size at AUC=0.55 | body text |
| 0.90 | High AUC (S1 achieves in practice) | body text |
| J=16 | Sufficient ensemble size at high AUC | body text |
| J^{-0.48} | CI width scaling exponent | body text |
| J=8-30 | Current practice range | body text |

---

### Section G: DIF Parameterization Comparison (sec:dif_comparison)

**Table (tab:dif_comparison):**
| Number | Context | Location |
|--------|---------|----------|
| J=16 | Ensemble size | table caption |
| 300 | Items subsampled | table caption |
| 0.245 | Non-uniform gamma mean | table cell |
| 0.197 | Non-uniform gamma SD | table cell |
| 0.763 | Non-uniform PPP | table cell |
| -2124.3 | Non-uniform LOO ELPD | table cell |
| 1468 | Non-uniform ESS | table cell |
| -0.458 | Uniform gamma mean | table cell |
| 0.453 | Uniform gamma SD | table cell |
| 0.743 | Uniform PPP | table cell |
| -2123.4 | Uniform LOO ELPD | table cell |
| 981 | Uniform ESS | table cell |

**Body text (after table):**
| Number | Context | Location |
|--------|---------|----------|
| 0.9 | Delta_ELPD between parameterizations | body text |
| 1.4 | d_SE (standard error of delta) | body text |
| 0.197 vs. 0.453 | SD comparison between parameterizations | body text |
| 1468 vs. 981 | ESS comparison | body text |

---

### Section H: 4PL Extension (sec:4pl_details)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 5, 20 | Beta prior parameters for c_i | body text |
| 20, 5 | Beta prior parameters for d_i | body text |
| J>=16 | Required to avoid overparameterization | body text |
| J=5 | Insufficient ensemble size | body text |
| 0.000 | PPP at J=5 (4PL+gamma) | body text |
| 0.004 to 0.068 | MAE degradation at J=5 | body text |
| J=13 | Domain-level analysis ensemble size | body text |
| J=16 | Pooled calibration ensemble size | body text |

---

### Section I: S4 Self-Critique Signal Details (sec:s4_details)

No quantitative numbers beyond formula descriptions.

---

### Section J: Training Convergence (sec:training_convergence)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 1.08 | d000 final training loss | body text |
| 1.08 | d005 final training loss | body text |
| 1.14 | d025 final training loss | body text |
| 1.17 | d100 final training loss | body text |

---

### Section K: Model Exclusion Details (sec:exclusion_details)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 16 | Models remaining after 0.5B exclusion | body text |
| 3 | 3B checkpoints removed | body text |
| 2 | Checkpoints with naming mismatch | body text |
| 1 | Checkpoint lacking unified eval | body text |
| alpha=32 | Unified hyperparameter setting | body text |
| 5e-5 | Learning rate for standardized protocol | body text |
| alpha=32 | LoRA alpha | body text |

**Table (tab:model_sets):**
| Number | Context | Location |
|--------|---------|----------|
| 16 | J for pooled baselines | table cell |
| 8 | Qwen-1.5B models (pooled) | table cell |
| 8 | Qwen-3B models (pooled) | table cell |
| 13 | J for domain gamma | table cell |
| 8 | Qwen-1.5B models (domain) | table cell |
| 5 | Qwen-3B models (domain) | table cell |
| 16-28 | J range for cross-family | table cell |
| 13 | J for oracle ablation | table cell |

---

### Section L: Prior Sensitivity Analysis (sec:prior_sensitivity)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| J=16 | Ensemble size | body text |
| 300 | Items subsampled | body text |
| 0.5 | Tight prior SD | body text |
| 1 | Default prior SD | body text |
| 2 | Loose prior SD | body text |
| 0.34 to 0.89 | Posterior mean shift across priors | body text |
| -0.4 | Approximate lower bound (stable) | body text |
| 1.11 to 2.20 | Upper bound range | body text |
| <1.01 | R-hat convergence criterion | body text |
| >3800 | ESS across all fits | body text |
| 0.16 to 0.25 | PPP range | body text |

**Table (tab:socsci_prior):**
| Number | Context | Location |
|--------|---------|----------|
| J=16 | Corrected pool size | table caption |
| -0.541 | Social Sci gamma under N(0,0.5) | table cell |
| 99.35% | P(gamma<0) under N(0,0.5) | table cell |
| -0.627 | Social Sci gamma under N(0,1) | table cell |
| 99.7% | P(gamma<0) under N(0,1) | table cell |
| -0.654 | Social Sci gamma under N(0,2) | table cell |
| 99.85% | P(gamma<0) under N(0,2) | table cell |

**Body text (after table):**
| Number | Context | Location |
|--------|---------|----------|
| 2.6x | Pooled gamma shift across priors | body text |
| 1.2x | Social Sciences gamma variation across priors | body text |
| -0.54 to -0.65 | Social Sciences gamma range | body text |
| >=99.35% | P(gamma<0) in all prior cases | body text |
| 99.375% | Bonferroni threshold (eight domains) | body text |

---

### Section M: IRT Ability Separation by Scale (sec:theta_separation)

**Table (tab:theta_separation):**
| Number | Context | Location |
|--------|---------|----------|
| J=13 | Ensemble size | table caption |
| -0.532 | Math theta_1.5B | table cell |
| 0.119 | Math theta_3B | table cell |
| 0.651 | Math delta_theta | table cell |
| 0.570, 0.731 | Math 95% CI | table cell |
| 0.321 | Science theta_1.5B | table cell |
| 0.780 | Science theta_3B | table cell |
| 0.459 | Science delta_theta | table cell |
| 0.370, 0.546 | Science 95% CI | table cell |
| 0.372 | CS/Eng theta_1.5B | table cell |
| 0.542 | CS/Eng theta_3B | table cell |
| 0.169 | CS/Eng delta_theta | table cell |
| 0.030, 0.304 | CS/Eng 95% CI | table cell |
| 0.521 | Medical theta_1.5B | table cell |
| 1.053 | Medical theta_3B | table cell |
| 0.531 | Medical delta_theta | table cell |
| 0.452, 0.609 | Medical 95% CI | table cell |
| 0.228 | Humanities theta_1.5B | table cell |
| 0.496 | Humanities theta_3B | table cell |
| 0.268 | Humanities delta_theta | table cell |
| 0.202, 0.337 | Humanities 95% CI | table cell |
| 0.940 | Social Sci theta_1.5B | table cell |
| 1.540 | Social Sci theta_3B | table cell |
| 0.599 | Social Sci delta_theta | table cell |
| 0.523, 0.675 | Social Sci 95% CI | table cell |
| 0.083 | Business/Law theta_1.5B | table cell |
| 0.417 | Business/Law theta_3B | table cell |
| 0.334 | Business/Law delta_theta | table cell |
| 0.261, 0.410 | Business/Law 95% CI | table cell |
| 0.817 | Other theta_1.5B | table cell |
| 1.565 | Other theta_3B | table cell |
| 0.748 | Other delta_theta | table cell |
| 0.647, 0.846 | Other 95% CI | table cell |
| 0.311 | Pooled theta_1.5B | table cell |
| 0.811 | Pooled theta_3B | table cell |
| 0.500 | Pooled delta_theta | table cell |
| 0.431, 0.568 | Pooled 95% CI | table cell |

---

### Section N: Cross-Seed Stability Details (sec:cross_seed_details)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| +/-1.6pp | OLMo-2 s42 rerun variability | body text |
| 3.76pp | OLMo-2 cross-seed range | body text |

---

### Section O: DiD Visualization (sec:did_visualization)

**Figure caption (fig:treated_untreated):**
| Number | Context | Location |
|--------|---------|----------|
| 1.25-2.05pp | MDES range | figure caption |

**Table (tab:did):**
| Number | Context | Location |
|--------|---------|----------|
| 3,540 / 10,502 | Treated / untreated item split | table caption |
| +3.1 | Gemma-2 Treated delta (p<.01) | table cell |
| +2.6 | Gemma-2 Untreated delta (p<.001) | table cell |
| +0.5 | Gemma-2 DiD (ns) | table cell |
| +1.6 | OLMo-2 Treated delta (ns) | table cell |
| +2.7 | OLMo-2 Untreated delta (p<.001) | table cell |
| -1.1 | OLMo-2 DiD (ns) | table cell |
| +0.3 | Phi-4 Treated delta (ns) | table cell |
| +0.6 | Phi-4 Untreated delta (ns) | table cell |
| -0.3 | Phi-4 DiD (ns) | table cell |
| -6.9 | Qwen-14B Treated delta (p<.001) | table cell |
| -7.6 | Qwen-14B Untreated delta (p<.001) | table cell |
| +0.7 | Qwen-14B DiD (ns) | table cell |
| -3.8 | Qwen-7B Treated delta (p<.01) | table cell |
| -2.9 | Qwen-7B Untreated delta (p<.001) | table cell |
| -0.8 | Qwen-7B DiD (ns) | table cell |

---

### Section P: DiD Across Dosage Levels (sec:did_dosage)

No additional numbers beyond figure caption reference.

---

### Section Q: Post-hoc Power Analysis / MDES (sec:mdes)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 80% | Power level | body text |
| 0.05 | Alpha (significance level) | body text |

**Table (tab:mdes_mmlu):**
| Number | Context | Location |
|--------|---------|----------|
| 3,540 | n_treated MMLU | table caption |
| 10,502 | n_untreated MMLU | table caption |
| -0.27 | Phi-4 DiD (pp) | table cell |
| 1.25 | Phi-4 MDES (pp) | table cell |
| -1.07 | OLMo-2 DiD (pp) | table cell |
| 1.59 | OLMo-2 MDES (pp) | table cell |
| +0.55 | Gemma-2 DiD (pp) | table cell |
| 1.74 | Gemma-2 MDES (pp) | table cell |
| -0.84 | Qwen-7B DiD (pp) | table cell |
| 2.02 | Qwen-7B MDES (pp) | table cell |
| +0.69 | Qwen-14B DiD (pp) | table cell |
| 2.05 | Qwen-14B MDES (pp) | table cell |

**Table (tab:mdes_arc):**
| Number | Context | Location |
|--------|---------|----------|
| 257 | n_treated ARC | table caption |
| 915 | n_untreated ARC | table caption |
| -0.83 | Phi-4 ARC DiD (pp) | table cell |
| 2.28 | Phi-4 ARC MDES (pp) | table cell |
| -0.26 | Qwen-14B ARC DiD (pp) | table cell |
| 3.47 | Qwen-14B ARC MDES (pp) | table cell |
| -1.13 | OLMo-2 ARC DiD (pp) | table cell |
| 4.19 | OLMo-2 ARC MDES (pp) | table cell |
| -0.25 | Gemma-2 ARC DiD (pp) | table cell |
| 4.66 | Gemma-2 ARC MDES (pp) | table cell |
| +2.43 | Qwen-7B ARC DiD (pp) | table cell |
| 5.57 | Qwen-7B ARC MDES (pp) | table cell |

**Body text (after tables):**
| Number | Context | Location |
|--------|---------|----------|
| >2pp | MMLU: absence of item-specific effects threshold | body text |
| n=257 | ARC treated sample size | body text |
| 5.57pp | Qwen-7B ARC MDES | body text |

---

### Section R: Volume Control Analysis (sec:volume_control)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 66,533 | Non-benchmark MCQ items | body text |

**Table (tab:volume_control):**
| Number | Context | Location |
|--------|---------|----------|
| 45% | Volume contribution on MMLU | table caption |
| 43% | Volume contribution on ARC | table caption |
| 53% | Volume contribution on GSM8K | table caption |
| 58.77% | Falcon3 d000 MMLU | table cell |
| 81.57% | Falcon3 d000 ARC | table cell |
| 74.53% | Falcon3 d000 GSM8K | table cell |
| 60.67% | Falcon3 volume control MMLU | table cell |
| 83.28% | Falcon3 volume control ARC | table cell |
| 75.21% | Falcon3 volume control GSM8K | table cell |
| 62.96% | Falcon3 d100 MMLU | table cell |
| 85.58% | Falcon3 d100 ARC | table cell |
| 75.82% | Falcon3 d100 GSM8K | table cell |
| +1.90 | Volume control delta MMLU (pp) | table cell |
| +1.71 | Volume control delta ARC (pp) | table cell |
| +0.68pp | Volume control delta GSM8K | table cell |
| +4.19 | d100 delta MMLU (pp) | table cell |
| +4.01 | d100 delta ARC (pp) | table cell |
| +1.29pp | d100 delta GSM8K | table cell |

**Body text (after table):**
| Number | Context | Location |
|--------|---------|----------|
| 45% vs. 43% | MMLU vs ARC volume decomposition consistency | body text |
| -9.4pp | Qwen-14B Collapse magnitude | body text |
| +1.90pp | Volume baseline | body text |
| ~-11.3pp | Implied contamination-specific harm for Qwen-14B | body text |
| <1pp | Phi-4 Immune response | body text |

---

### Section S: Dose-Response Profile Classification Algorithm (sec:classification_algorithm)

**Algorithm parameters:**
| Number | Context | Location |
|--------|---------|----------|
| tau=2pp | Noise threshold | algorithm |
| sigma=5pp | Severity threshold | algorithm |
| 0, 5, 25, 50, 100% | Dosage levels | algorithm |

---

### Section T: Dose-Response Details (sec:dose_response_details)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| ~0.6-0.7pp | MMLU accuracy increase at 1.5B/3B | body text |
| 0.41 | 0.5B MMLU accuracy at d000 | body text |
| 0.27 | 0.5B MMLU accuracy at d100 | body text |
| 98% | A-option bias at 0.5B | body text |

---

### Section U: Sensitivity of Profile Classification (sec:classification_sensitivity)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 134 | Total (tau, sigma) combinations swept | body text |
| 0.5 to 2.0 pp | Tau reasonable range | body text |
| 3.0 to 7.0 pp | Sigma reasonable range | body text |
| 30 | Reasonable range combinations | body text |

**Table (tab:sensitivity):**
| Number | Context | Location |
|--------|---------|----------|
| 100% | Qwen-14B reasonable stability | table cell |
| 100% | Qwen-14B full stability | table cell |
| tau=9.4 | Qwen-14B nearest transition | table cell |
| 100% | Gemma-2 reasonable stability | table cell |
| 89% | Gemma-2 full stability | table cell |
| tau=3.8 | Gemma-2 nearest transition | table cell |
| 100% | Phi-4 reasonable stability | table cell |
| 82% | Phi-4 full stability | table cell |
| tau<0.35 | Phi-4 nearest transition | table cell |
| 100% | OLMo-2 reasonable stability | table cell |
| 82% | OLMo-2 full stability | table cell |
| tau=3.25 | OLMo-2 nearest transition | table cell |
| 100% | Qwen-7B reasonable stability | table cell |
| 72% | Qwen-7B full stability | table cell |
| tau=3.0 | Qwen-7B nearest transition | table cell |

**Body text (after table):**
| Number | Context | Location |
|--------|---------|----------|
| 150/150 | All family-parameter combinations stable in reasonable range | body text |
| tau=9.4 | Qwen-14B transition threshold | body text |
| 4.7x | Qwen-14B transition as multiple of default | body text |
| -9.4pp | Qwen-14B delta_acc | body text |
| tau=3.0 | Qwen-7B transition (1.5x default) | body text |
| 1.5x | Qwen-7B transition as multiple of default | body text |
| <0.4pp | Phi-4 fluctuation | body text |
| 9.4pp | Qwen-14B decline | body text |
| tau=1pp | Lower bound of reasonable range | body text |
| 0.69pp | LLaMA-3.1 |delta| | body text |

---

### Section V: Cross-Family Domain Decomposition (sec:domain_decomposition)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| -6.8pp | Qwen-14B STEM d100 delta | body text |
| -10.1pp | Qwen-14B Humanities d100 delta | body text |
| -11.2pp | Qwen-14B Social Sciences d100 delta | body text |
| -9.4pp | Qwen-14B Other d100 delta | body text |
| +2.7pp | Gemma-2 STEM d100 delta | body text |
| +3.9pp | Gemma-2 Humanities d100 delta | body text |
| +5.0pp | Gemma-2 Social Sciences d100 delta | body text |
| +3.4pp | Gemma-2 Other d100 delta | body text |
| +/-1.0pp | Phi-4 Immune range across domains | body text |
| >1pp | Crossover noise band threshold | body text |
| +0.28pp | V-recovery Humanities exception | body text |
| 2.8pp | STEM mean |delta_acc| at d100 (most resilient) | body text |
| 5.1pp | Social Sciences mean |delta_acc| at d100 (most sensitive) | body text |
| 1.8x | Social Sciences vs STEM magnitude ratio | body text |

---

### Section W: Baseline Ability vs. Contamination Effect (sec:baseline_vs_effect)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 61.9% | Gemma-2 d000 baseline (strongest Benefit) | body text |
| 66.1% | Qwen-7B d000 baseline (weakest Harm) | body text |
| +3.2 to +4.2pp | Range of benefit for models below threshold | body text |
| 76.4% | Phi-4 d000 baseline | body text |
| +/-0.5pp | Phi-4 immunity range | body text |
| 53.5% | LLaMA-3.1 d000 baseline | body text |

---

### Section X: Per-Domain Gamma Estimates (sec:domain_gamma_table)

**Table (tab:domain_gamma):**
| Number | Context | Location |
|--------|---------|----------|
| J=13 and J=16 | Ensemble sizes | table caption |
| 99.375% | Bonferroni-corrected threshold (8 domains) | table caption |
| +0.50 | Math J=13 gamma | table cell |
| 8.1% | Math J=13 P(gamma<0) | table cell |
| +0.60 | Math J=16 gamma | table cell |
| 3.8% | Math J=16 P(gamma<0) | table cell |
| 0.305 | Math PPP | table cell |
| 1.007 | Math R-hat | table cell |
| +0.50 | Science J=13 gamma | table cell |
| 7.8% | Science J=13 P(gamma<0) | table cell |
| +0.57 | Science J=16 gamma | table cell |
| 4.3% | Science J=16 P(gamma<0) | table cell |
| 0.197 | Science PPP | table cell |
| 1.007 | Science R-hat | table cell |
| +0.50 | CS/Eng J=13 gamma | table cell |
| 14.8% | CS/Eng J=13 P(gamma<0) | table cell |
| +0.32 | CS/Eng J=16 gamma | table cell |
| 24.0% | CS/Eng J=16 P(gamma<0) | table cell |
| 0.503 | CS/Eng PPP | table cell |
| 1.006 | CS/Eng R-hat | table cell |
| +0.24 | Medical J=13 gamma | table cell |
| 24.0% | Medical J=13 P(gamma<0) | table cell |
| +0.05 | Medical J=16 gamma | table cell |
| 43.6% | Medical J=16 P(gamma<0) | table cell |
| 0.268 | Medical PPP | table cell |
| 1.008 | Medical R-hat | table cell |
| +0.13 | Other J=13 gamma | table cell |
| 35.7% | Other J=13 P(gamma<0) | table cell |
| +0.32 | Other J=16 gamma | table cell |
| 20.4% | Other J=16 P(gamma<0) | table cell |
| 0.072 | Other PPP (below threshold) | table cell |
| 1.008 | Other R-hat | table cell |
| +0.04 | Business/Law J=13 gamma | table cell |
| 44.1% | Business/Law J=13 P(gamma<0) | table cell |
| +0.08 | Business/Law J=16 gamma | table cell |
| 37.8% | Business/Law J=16 P(gamma<0) | table cell |
| 0.395 | Business/Law PPP | table cell |
| 1.007 | Business/Law R-hat | table cell |
| -0.31 | Humanities J=13 gamma | table cell |
| 85.4% | Humanities J=13 P(gamma<0) | table cell |
| -0.14 | Humanities J=16 gamma | table cell |
| 69.7% | Humanities J=16 P(gamma<0) | table cell |
| 0.416 | Humanities PPP | table cell |
| 1.007 | Humanities R-hat | table cell |
| -0.57 | Social Sci J=13 gamma | table cell |
| 99.1% | Social Sci J=13 P(gamma<0) | table cell |
| -0.63 | Social Sci J=16 gamma | table cell |
| 99.7% | Social Sci J=16 P(gamma<0) | table cell |
| 0.722 | Social Sci PPP | table cell |
| 1.006 | Social Sci R-hat | table cell |
| 0.1 | PPP acceptable threshold (footnote) | table footnote |

---

### Section Y: DGP Robustness Analysis (sec:threshold_dgp)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 400 | Total simulation runs | body text |
| 2 | Number of DGPs | body text |
| 4 | Number of ensemble sizes | body text |
| 5 | Number of true gamma values | body text |
| 10 | Number of seeds | body text |
| J in {16, 50, 100, 500} | Ensemble sizes swept | body text |
| gamma in {0.5, 1.0, 1.5, 2.0, 3.0} | True gamma values | body text |
| 0.84-1.07 | Linear DGP gamma_hat/gamma_true ratio | body text |
| 0.94-1.24 | Threshold DGP gamma_hat/gamma_true ratio | body text |
| 0.50-0.56 | PPP range under both DGPs | body text |
| >=0.93 | Linear DGP CI coverage (nominal) | body text |

**Table (tab:dgp_coverage):**
| Number | Context | Location |
|--------|---------|----------|
| 50 | J value | table cell |
| 1.00 | CI coverage at J=50 | table cell |
| 100 | J value | table cell |
| 0.90-1.00 | CI coverage at J=100 | table cell |
| 200 | J value | table cell |
| 0.80-1.00 | CI coverage at J=200 | table cell |
| 500 | J value | table cell |
| 0.70-1.00 | CI coverage at J=500 | table cell |

**Paragraph "Implications":**
| Number | Context | Location |
|--------|---------|----------|
| >=0.94 | Threshold DGP gamma_hat/gamma_true lower bound | body text |
| ~0 | Empirical gamma value | body text |
| J=13-16 | Empirical analysis ensemble sizes | body text |
| 0.041 | Mean real RRF exposure (right-skewed) | body text |

---

### Section Z: ARC IRT Results (sec:arc_irt)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 0.003 | ARC PPP at J=16 | body text |
| 1,172 vs. 14,042 | ARC vs MMLU item pool | body text |
| J=16 | Ensemble size for ARC baseline | body text |
| 300 | Items subsampled | body text |
| 0.007 | B0-Raw MAE (ARC) | body text |
| 0.015 | B3-Vanilla2PL MAE (ARC) | body text |
| 0.012 | B4-LinearRegression MAE (ARC) | body text |
| 0.731 | B4 tau (best rank correlation) | body text |
| 0.314 | B6-DCR MAE (ARC, systematic overcorrection) | body text |
| 0.020 | ContamCal MAE (ARC) | body text |
| ~0.7pp | Aggregate ARC contamination effect | body text |
| J=8, 13, 16 | Tested J configurations for domain-level ARC | body text |
| <0.05 | PPP in all ARC domain-level cases | body text |

---

### Section AA: Full Baseline Comparison (sec:full_baselines)

**Body text (intro):**
| Number | Context | Location |
|--------|---------|----------|
| J=16 | MMLU/ARC ensemble size | body text |
| J=24 | GSM8K ensemble size | body text |
| J=8 | ARC 0.5B+1.5B configuration | body text |
| 0.056 | B4-LinearRegression MAE on ARC | body text |

**Table (tab:full_baselines_arc):**
| Number | Context | Location |
|--------|---------|----------|
| J=8 | Ensemble size | table caption |
| 0.059 | B0-Raw ARC MAE | table cell |
| 0.059 | B1-Remove&Rescore ARC MAE | table cell |
| 0.064 | B2-Single2PL+gamma ARC MAE | table cell |
| 0.071 | B3-Vanilla4PL ARC MAE | table cell |
| 0.056 | B4-LinearRegression ARC MAE | table cell |
| 0.059 | B5-Emperor ARC MAE | table cell |
| 0.035 | ContamCal (4PL+gamma) ARC MAE (best) | table cell |

**Table (tab:full_baselines_gsm8k):**
| Number | Context | Location |
|--------|---------|----------|
| 0.003 | B0-Raw GSM8K MAE | table cell |
| 0.320 | B2-Single2PL+gamma GSM8K MAE | table cell |
| 0.012 | B3-Vanilla4PL GSM8K MAE | table cell |
| 0.003 | B4-LinearRegression GSM8K MAE (best) | table cell |
| 0.020 | ContamCal (4PL+gamma) GSM8K MAE | table cell |

---

### Section AB: Parametric Dose-Response Model Comparison (sec:parametric_dr)

**Table (tab:aicc_dr):**
| Number | Context | Location |
|--------|---------|----------|
| -71.42 | Phi-4 Constant AICc | table cell |
| -72.08 | Phi-4 Linear AICc | table cell |
| -70.06 | Phi-4 Quadratic AICc | table cell |
| -73.14 | Phi-4 Hill AICc (best) | table cell |
| 0.58 | Phi-4 Hill Akaike weight | table cell |
| 49.54 | Qwen-14B Constant AICc | table cell |
| 23.40 | Qwen-14B Linear AICc | table cell |
| 21.22 | Qwen-14B Quadratic AICc | table cell |
| 18.28 | Qwen-14B Hill AICc (best) | table cell |
| 0.55 | Qwen-14B Hill Akaike weight | table cell |
| -12.38 | Qwen-7B Constant AICc | table cell |
| -20.53 | Qwen-7B Linear AICc | table cell |
| -14.52 | Qwen-7B Quadratic AICc | table cell |
| -24.97 | Qwen-7B Hill AICc (best) | table cell |
| 0.77 | Qwen-7B Hill Akaike weight | table cell |
| 17.35 | Gemma-2 Constant AICc (best) | table cell |
| 18.89 | Gemma-2 Linear AICc | table cell |
| 20.01 | Gemma-2 Quadratic AICc | table cell |
| 18.96 | Gemma-2 Hill AICc | table cell |
| 0.39 | Gemma-2 Constant Akaike weight | table cell |
| 25.82 | OLMo-2 Constant AICc (best) | table cell |
| 26.66 | OLMo-2 Linear AICc | table cell |
| 27.54 | OLMo-2 Quadratic AICc | table cell |
| 26.47 | OLMo-2 Hill AICc | table cell |
| 0.62 | OLMo-2 Constant Akaike weight | table cell |

**Body text (after table):**
| Number | Context | Location |
|--------|---------|----------|
| -43pp | Qwen-14B Hill E_max | body text |
| 6.4 | Qwen-7B Quadratic delta_AICc | body text |
| +2.43pp | Phi-4 Hill E_max (weak Benefit) | body text |
| -2.01, +6.88 | Phi-4 Hill E_max CI (crosses zero) | body text |
| n=3 | Number of seeds (insufficient power) | body text |

---

### Section AC: Exposure Score Item-Level Classification (sec:sij_classification)

**Body text:**
| Number | Context | Location |
|--------|---------|----------|
| 0.93-0.99 | S1 ROC-AUC range | body text |
| 0.73-0.93 | RRF fusion ROC-AUC range | body text |
| ~0.48-0.50 | S2 (Min-K\%++) AUC | body text |
| ~0.47-0.51 | S4 (Self-Critique) AUC | body text |

---

### Key Cross-Reference Checks (numbers that should match main text):

1. **"Qwen-14B collapses by -9.4pp"** — appears in Section A (body text: "-15.7pp" on MMLU), Section B ("-9.4pp MMLU" for Qwen-14B in GSM8K context), Section R ("-9.4pp" for Collapse magnitude), and Section U ("-9.4pp" as Qwen-14B delta_acc). Note: -9.4pp appears to refer to the s42 single-seed value, while -15.7pp is the multi-seed mean. These may need verification against main text for consistency.

2. **Item counts**: 1,172 (ARC) and 14,042 (MMLU) appear consistently in Sections A and Z.

3. **3,540 / 10,502 treated/untreated split** appears in both the DiD table caption and the MDES table caption (consistent).

4. **Social Sciences gamma**: -0.63 appears in the domain gamma table (J=16), the prior sensitivity analysis, and the S2-only pipeline comparison (consistent).

5. **Precision consistency issues to flag**:
   - GSM8K table uses 2 decimal places for accuracy (e.g., 84.46%) while some body text references round differently (+7.4pp in body vs +7.43 in table)
   - ARC dose-response values in body text use 1 decimal (90.4, 91.5, etc.)
   - DiD table uses 1 decimal place for pp values
   - MDES tables use 2 decimal places
   - Gamma estimates use 2-3 decimal places consistently within tables but vary across tables

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9c51d2a-da5e-4a84-9d17-13f373ce6473",
  "isSidechain": true,
  "agentId": "a640ef6b7af654c09",
  "requestId": "req_011CbPrjS55FidxbtgPnYFTs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c7b08b6-359b-4ab2-acca-64dabe8be6c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8s2K2YKF9FepMRNsJYTfZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1771,
      "cache_read_input_tokens": 48099,
      "output_tokens": 15250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1771
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15250,
          "cache_read_input_tokens": 48099,
          "cache_creation_input_tokens": 1771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1771,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
