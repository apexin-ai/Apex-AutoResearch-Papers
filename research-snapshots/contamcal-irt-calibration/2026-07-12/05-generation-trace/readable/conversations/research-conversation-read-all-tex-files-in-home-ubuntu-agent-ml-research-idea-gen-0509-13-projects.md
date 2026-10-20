# Research conversation: Read ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ a

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a109e78e0e9d19555.jsonl`
- **Structured JSON:** [`9d410861e6c32364df0e.json`](../../sessions/9d/9d410861e6c32364df0e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-25T08:31:14.674Z_

Read ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ and extract every quantitative claim (numbers, percentages, pp changes, counts, thresholds, confidence intervals, p-values, etc.). 

For each number, record:
1. The file and approximate line number
2. The exact value stated
3. What it refers to (e.g., "Phi-4 MMLU delta", "BCa CI for Gemma-2", "number of MMLU items")
4. Whether it appears in running text, a table, or figure caption

Group findings by topic/metric so duplicates across sections are easy to spot.

Files to read: abstract.tex, introduction.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex

Focus especially on:
- Model accuracy values and delta-accuracy (pp changes)
- Confidence intervals
- P-values and statistical thresholds
- Counts (items, models, seeds, parameters)
- Hyperparameters (learning rate, batch size, epochs)
- Effect sizes (Cohen's d, AUC, tau)

Output a structured report organized by metric/claim, showing where each number appears across files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "11782fd2-7628-470f-929f-3f4ef34130e0",
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

_source line 2 · 2026-05-25T08:31:14.679Z_

```json
{
  "parentUuid": "11782fd2-7628-470f-929f-3f4ef34130e0",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
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
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
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
  "uuid": "33f117d4-a013-479e-a040-5b4c5aaa1f7e",
  "timestamp": "2026-05-25T08:31:14.679Z",
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

### Assistant

_source line 3 · 2026-05-25T08:31:17.595Z_



I'll read all the .tex files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33f117d4-a013-479e-a040-5b4c5aaa1f7e",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXB5QXDX3zStpX8yDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2412e292-2ccc-45c2-b4ed-0f4c73596a1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4w7Dps1MzvtsFTcziMNLm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30284,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30284,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T08:31:18.044Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U6TohCAgVWTfqEbN4ewvJD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2412e292-2ccc-45c2-b4ed-0f4c73596a1c",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXB5QXDX3zStpX8yDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d10fd902-3734-4520-ab6c-850ae539db29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4w7Dps1MzvtsFTcziMNLm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30284,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30284,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T08:31:18.055Z_

<details><summary>↩ Tool result · `toolu_01U6TohCAgVWTfqEbN4ewvJD`</summary>

```text
1	Benchmark contamination is widely assumed to inflate language model scores, yet its actual effect has never been measured across model families. We perform controlled supervised fine-tuning (SFT) injection at five dosage levels into six models (7B to 14.7B) from five open-source families and discover a spectrum of dose-response patterns, not uniform inflation. Two patterns replicate across independent families: Immune (Phi-4, LLaMA-3.1) and Benefit (statistically significant for Gemma-2, bootstrap 95\% CI [$+$1.49, $+$3.14]\,pp; borderline for OLMo-2 and Falcon3). Collapse and V-recovery are each observed in one family (Qwen2.5) across three seeds but remain preliminary pending independent replication. Effects are benchmark-conditional: MMLU-targeted contamination improves GSM8K in five of six families, even those harmed on MMLU. Difference-in-differences analysis detects no item-specific memorization; a volume-matched control attributes 45\% of Benefit to data quantity. ContamCal, our diagnostic framework combining multi-signal exposure mapping with contamination-augmented Item Response Theory (IRT), enables domain-level contamination diagnosis with credible intervals, revealing that Social Sciences contamination effects are negative while STEM effects are positive, a pattern invisible to aggregate scoring. Out-of-sample validation on LLaMA-3.1-8B confirms that model family characteristics beyond baseline ability modulate vulnerability. Model-specific dose-response profiling is necessary for reliable benchmark interpretation.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d10fd902-3734-4520-ab6c-850ae539db29",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "7f032a88-b6b9-4fc2-9de9-8e4a258b8906",
  "sourceToolAssistantUUID": "d10fd902-3734-4520-ab6c-850ae539db29",
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

_source line 6 · 2026-05-25T08:31:19.747Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F8gAKKQ2JPcYCvELiiCCSr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f032a88-b6b9-4fc2-9de9-8e4a258b8906",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXB5QXDX3zStpX8yDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3982b018-2651-4ccd-9461-f5c0c48a4811",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4w7Dps1MzvtsFTcziMNLm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30284,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30284,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T08:31:19.758Z_

<details><summary>↩ Tool result · `toolu_01F8gAKKQ2JPcYCvELiiCCSr`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models (LLMs), yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled supervised fine-tuning (SFT) injection (Low-Rank Adaptation [LoRA], five dosage levels) into six models spanning five independent families from five labs (Alibaba, Microsoft, Allen AI, Google, TII) and discover a spectrum of dose-response patterns (Figure~\ref{fig:dose_response}, Table~\ref{tab:taxonomy})---from immunity (Phi-4, $\pm$0.5pp) and benefit ($+$3--4pp, three families) to collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{figures/fig_dose_response.pdf}
10	\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; LLaMA-3.1 at seed$=$0). Immune and Benefit replicate across families; Collapse and V-recovery are preliminary (Qwen2.5-specific). Cross-seed stability in Table~\ref{tab:cross_seed}.}
11	\label{fig:dose_response}
12	\end{figure}
13	
14	Across six models, three lower-baseline models benefit ($+$3.2 to $+$4.2pp), one is immune (Phi-4), and the remaining two (both Qwen2.5) show harm---with the 14B model 5$\times$ more fragile than 7B (Figure~\ref{fig:baseline_vulnerability}). These effects are benchmark-conditional: the same model can collapse on MMLU ($-$9.4pp) yet gain on GSM8K ($+$13pp). ContamCal, our diagnostic framework combining multi-signal exposure mapping with contamination-augmented Item Response Theory (IRT; 2PL+$\gamma_k$), enables this characterization.
15	
16	\begin{table}[t]
17	\centering
18	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% bootstrap CI, $B=10{,}000$). Stab.: fraction of bootstrap resamples ($B=10{,}000$) that yield the same Algorithm~\ref{alg:profile-classification} classification. Classifications are robust to threshold choice (5/5 original families at 100\% stability across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
19	\label{tab:taxonomy}
20	\setlength{\tabcolsep}{2pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{llcccccc}
23	\toprule
24	Pattern & Model & Base & $\Delta$acc & CI & Peak & St. & R. \\
25	\midrule
26	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% & \checkmark \\
27	Collapse & Qwen-14B & 69.4\% & $-$9.4pp\textsuperscript{$\ddagger$} & [$-$12.74, $-$9.0] & --- & 100\% & $\triangle$ \\
28	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% & $\triangle$ \\
29	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & n-mono. & 76.6\% & \checkmark \\
30	Benefit & Falcon3 7B & 58.8\% & $+$4.2pp & [$+$3.60, $+$4.79] & mono. & 96.1\% & \checkmark \\
31	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% & \checkmark \\
32	\bottomrule
33	\multicolumn{8}{l}{\scriptsize $^{\ddagger}$Cross-seed range $-$9.4 to $-$25.0pp (s42/s123/s0); see Table~\ref{tab:cross_seed}.} \\
34	\multicolumn{8}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.55pp ($<$1pp threshold), s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.} \\
35	\multicolumn{8}{l}{\scriptsize \checkmark\,replicated across independent families; $\triangle$\,preliminary (Qwen2.5-specific, pending replication).}
36	\end{tabular}}
37	\end{table}
38	
39	Our contributions:
40	\begin{enumerate}
41	    \item \textbf{Dose-response profiles with cross-seed and cross-benchmark validation.} Controlled injection across five families reveals two replicated patterns (Immune, Benefit) and two preliminary Qwen2.5-specific patterns (Collapse, V-recovery). Out-of-sample validation on LLaMA-3.1-8B confirms generalizability. Cross-benchmark transfer reveals directional reversal on GSM8K for three families. Multi-seed evaluation ($n\!=\!3$) shows direction is reproducible but magnitude is seed-sensitive.
42	    \item \textbf{Domain-level contamination diagnosis via IRT.} ContamCal embeds multi-signal Reciprocal Rank Fusion (RRF) exposure scores in a contamination-augmented IRT model (2PL+$\gamma$)---an application of standard explanatory IRT \citep{deboeck_2004_explanatory_irt} to LLM contamination---enabling domain-level diagnosis with credible intervals. Domain analysis reveals opposing contamination directions (Social Sciences $\gamma_d < 0$, STEM $\gamma_d > 0$) invisible to aggregate scoring. No item-specific memorization is detected via difference-in-differences (minimum detectable effect size [MDES] 1.25--2.05pp).
43	    \item \textbf{Diagnostic pipeline requirements and signal failure.} Min-K\%++ \citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (paired Cohen's $d = -1.98$ at d100). RRF-based multi-signal fusion is essential: a single-signal pipeline produces severe model misfit (posterior predictive $p$-value [PPP] $< 0.001$). Simulation establishes $\gamma$ recovery requires $J \geq 50$ at area under the curve (AUC) $\geq 0.55$, above current practice ($J = 8$--$30$).
44	\end{enumerate}
45	
46	\noindent Code and data are available at \url{https://github.com/anonymous-nlp-2026-2/contamcal-irt-calibration}.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3982b018-2651-4ccd-9461-f5c0c48a4811",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "03bf8ca9-3a0a-43d6-bba4-aad38caa6822",
  "sourceToolAssistantUUID": "3982b018-2651-4ccd-9461-f5c0c48a4811",
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

_source line 8 · 2026-05-25T08:31:19.796Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WBUDFMz4gpA9ZG4j1sjx3b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03bf8ca9-3a0a-43d6-bba4-aad38caa6822",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXB5QXDX3zStpX8yDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "710ad22f-2194-4d8e-b307-fc212902131f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4w7Dps1MzvtsFTcziMNLm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30284,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30284,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T08:31:19.802Z_

<details><summary>↩ Tool result · `toolu_01WBUDFMz4gpA9ZG4j1sjx3b`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in three stages (Figure~\ref{fig:pipeline}): Stage~1 estimates per-item contamination exposure via training-free signal fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to recover clean ability estimates with credible intervals; Stage~3 classifies dose-response trajectories into canonical patterns.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{de_ayala_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \citep{kadavath2022}; concurrent work by \citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\mathcal{S} = \{\text{S1, S2, S4}\}$) and applies to any benchmark without auxiliary data. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_failure}. Item-level classification performance of the exposure scores is reported in Appendix~\ref{sec:sij_classification}.
17	
18	We aggregate signals via Reciprocal Rank Fusion \citep[RRF;][]{cormack_2009_rrf}:
19	\begin{equation}
20	\label{eq:rrf}
21	    e_{ij} = \sum_{s \in \mathcal{S}} \frac{1}{\kappa + r_{s}(i)},
22	\end{equation}
23	where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\kappa=60$ is the standard RRF smoothing constant, robust to near-random component signals, and $|\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to $e_{ij} \in [0,1]$; the distribution is highly right-skewed (mean 0.041).
24	
25	\subsection{Stage 2: Contamination-Augmented IRT}
26	\label{sec:stage2}
27	
28	\begin{figure}[t]
29	\centering
30	\includegraphics[width=0.92\columnwidth]{figures/fig_baseline_vulnerability.pdf}
31	\caption{Baseline MMLU accuracy vs.\ contamination response at d100 ($N\!=\!6$). Vertical bars show cross-seed range ($n\!=\!2$--$3$ seeds). Shaded band marks the threshold region (61.9--66.1\%) separating Benefit from Harm patterns (observational, not validated; extended in Appendix~\ref{sec:baseline_vs_effect}).}
32	\label{fig:baseline_vulnerability}
33	\end{figure}
34	
35	\paragraph{Primary model: 2PL+$\gamma$.}
36	Our primary specification augments the two-parameter logistic (2PL) model \citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:
37	\begin{equation}
38	\label{eq:2pl_gamma}
39	    P(y_{ijk} = 1) = \sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
40	\end{equation}
41	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \in \mathbb{R}$ is item difficulty, $\theta_j$ is model ability, and $\gamma_k$ is the scalar contamination effect for benchmark~$k$ ($\gamma$ without subscript denotes the pooled effect; $\gamma_d$ denotes per-domain effects, \S\ref{sec:domain_differential}). Each benchmark is fitted independently; when finer-grained diagnosis is needed, we replace $\gamma_k$ with per-domain effects $\gamma_d$ ($d=1,\ldots,D$), fitting Eq.~\eqref{eq:2pl_gamma} separately for each cognitive domain within a benchmark (\S\ref{sec:domain_differential}).
42	
43	We place $\gamma_k$ outside the item discrimination bracket, modeling contamination as a fixed logit shift \citep{de_ayala_2009_irt} rather than the uniform DIF form that would scale contamination effects with item discrimination. A comparison with the uniform DIF alternative ($\gamma$ inside the discrimination bracket) yields equivalent model fit (Appendix~\ref{sec:dif_comparison}). For MC-format benchmarks, a four-parameter logistic (4PL) extension adds guessing and ceiling asymptotes (Appendix~\ref{sec:4pl_details}); this requires $J \geq 16$ and is not used in domain-level analyses ($J = 13$).
44	
45	\paragraph{Inference.}
46	We perform Bayesian inference via the No-U-Turn Sampler (NUTS) \citep{hoffman2014} in Stan \citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_k \sim \mathcal{N}(0,1)$. At $J=16$, the $\gamma$ posterior is sensitive to the prior (up to 2.6$\times$ shift across reasonable alternatives; Appendix~\ref{sec:prior_sensitivity}); we therefore treat $\gamma$ estimates as directional indicators rather than precise effect sizes. Convergence requires split-$\hat{R} < 1.01$ and bulk effective sample size (ESS)~$> 400$ for all parameters. Model fit is assessed via the posterior predictive $p$-value (PPP), where values near 0.5 indicate adequate fit.
47	
48	\paragraph{Calibrated score.}
49	The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:
50	\begin{equation}
51	\label{eq:calibrated}
52	    \text{Acc}_{j}^{\text{cal}} = \frac{1}{I_k} \sum_{i=1}^{I_k}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)\right],
53	\end{equation}
54	with credible intervals from posterior quantiles. In practice, we average $\sigma(a_i(\theta_j - b_i))$ over posterior draws with $e_{ij}=0$; the spread of draws yields the credible interval. Models with noisier exposure signals receive wider intervals by construction.
55	
56	\paragraph{Identifiability.}
57	\label{sec:fisher}
58	\label{sec:value_decomposition}
59	The reliability of $\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\geq$0.55 with $J \geq 50$ (Appendix~\ref{sec:identifiability_appendix}; data-generating process (DGP) robustness in Appendix~\ref{sec:threshold_dgp}). Empirically, exposure scores $e_{ij}$ and item difficulty $b_i$ are near-orthogonal (Pearson $|r|<0.13$, $R^2<0.014$ across benchmarks), so $\gamma$ is identified from dosage-induced variation rather than confounded with difficulty. Eq.~\eqref{eq:calibrated} depends on $\theta_j$, not $\gamma$ directly, predicting that vanilla 2PL ($\gamma\!=\!0$) achieves comparable calibration to 2PL+$\gamma$, with $\gamma_k$ serving diagnosis rather than calibration (\S\ref{sec:calibration_results}).
60	
61	\subsection{Dose-Response Profile Classification}
62	\label{sec:classification}
63	
64	Independent of the IRT calibration pipeline, we classify dose-response profiles via a deterministic decision tree (Algorithm~\ref{alg:profile-classification} in Appendix~\ref{sec:classification_algorithm}) parameterized by noise threshold $\tau{=}2$\,pp and severity threshold $\sigma{=}5$\,pp, drawing on pharmacological dose-response modeling \citep{hill1910aggregation,ritz2015dose}. The tree branches on the end-to-end accuracy shift $\Delta{=}a_{100}{-}a_0$, mid-dosage minimum, and maximum mid-trajectory deviation to assign one of four patterns: \textsc{Immune}, \textsc{Collapse}, \textsc{V-recovery}, or \textsc{Benefit}. All thresholds are explicit and adjustable; a 30-combination $(\tau, \sigma)$ grid sweep confirms all families are stable (180/180 pairs; Appendix~\ref{sec:classification_sensitivity}). Family-level classification uses \emph{direction} as the primary criterion (\S\ref{sec:cross_seed}): Immune if the bootstrap CI of the cross-seed mean $\Delta$(d100) includes zero and $|\text{mean}~\Delta| < \tau$; Borderline if the CI includes zero but $|\text{mean}~\Delta| \geq \tau$; otherwise Harm/Benefit by sign. Parametric model selection (Appendix~\ref{sec:parametric_dr}) confirms these classifications for extreme effects but lacks power at $n\!=\!3$ seeds, motivating the rule-based approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "710ad22f-2194-4d8e-b307-fc212902131f",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "637e12e5-009d-45a2-992b-35ce8a0e4721",
  "sourceToolAssistantUUID": "710ad22f-2194-4d8e-b307-fc212902131f",
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

_source line 10 · 2026-05-25T08:31:20.218Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fp9JbrHW4Tit2AKUdUMage`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "637e12e5-009d-45a2-992b-35ce8a0e4721",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXB5QXDX3zStpX8yDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a66c881-a763-4366-86f3-eac4392fa910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4w7Dps1MzvtsFTcziMNLm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30284,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30284,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T08:31:20.224Z_

<details><summary>↩ Tool result · `toolu_01Fp9JbrHW4Tit2AKUdUMage`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning five independent model families from five labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), Gemma-2 \citep{gemmateam2024gemma2} (9B), and Falcon3 \citep{tiiuae2024falcon3} (7B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, dropout$=0$, targeting all attention and multilayer perceptron (MLP) projections; lr$=5\times10^{-5}$, bf16, 1 epoch, batch size$=1$, gradient accumulation$=16$, warmup ratio$=0.03$; trainable parameters range from 0.45\% of Phi-4 14.7B to 2.10\% of Qwen2.5-0.5B; convergence in Appendix~\ref{sec:training_convergence}) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus, yielding 50.0k (d000), 50.8k (d005), 54.1k (d025), 58.3k (d050), and 66.5k (d100) total training examples ($+$33\% volume at d100 vs.\ d000).
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The four cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 55 checkpoints spanning nine sizes across five families. We exclude 0.5B from multiple-choice (MC) IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}; details in Appendix~\ref{sec:exclusion_details}). We additionally validate our dose-response profiles on a held-out sixth family, LLaMA-3.1-8B \citep{grattafiori2024llama3} (Meta), which was not used during profile construction. LLaMA-3.1 is trained at three dosage levels (d000, d025, d100) to verify that Algorithm~\ref{alg:profile-classification} generalizes to unseen model families.
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
17	
18	\textbf{ARC-Challenge} \citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.
19	
20	\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought (CoT) reasoning: the d000 baseline drops to 17.8\% (vs.\ 73--84\% for other families), indicating CoT collapse rather than a contamination effect.
21	
22	All multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.
23	
24	We assess calibration quality via mean absolute error (MAE) (calibrated vs.\ ground-truth clean accuracy), Kendall $\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\gamma$ direction ($P(\gamma\!<\!0 \mid \text{data})$), and split-$\hat{R}$ convergence.
25	
26	\subsection{Baselines}
27	\label{sec:baselines}
28	
29	We compare against seven baselines (Table~\ref{tab:baselines}): \textbf{B0-Raw} (no adjustment), \textbf{B1-Remove\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \textbf{B2-Single2PL+$\gamma$} (aggregate $\gamma$ without domain stratification), \textbf{B3-Vanilla2PL} ($\gamma=0$, isolating IRT ability estimation), \textbf{B4-LinearRegression} (residuals on exposure scores), \textbf{B5-Emperor} (mitigation strategies from \citet{sun2025emperor}; B5b uses the best-performing variant), and \textbf{B6-DCR} (our reimplementation following \citealp{xu2025dcr}).
30	
31	\begin{table}[t]
32	\centering
33	\caption{MMLU method comparison on 300 randomly subsampled items (Qwen2.5, $J$=16). ARC results in Appendix~\ref{sec:arc_irt}.}
34	\label{tab:baselines}
35	\footnotesize
36	\begin{tabular}{lcc}
37	\toprule
38	Method & MAE & $\tau$ \\
39	\midrule
40	B0: Raw Accuracy & \textbf{0.006} & 0.767 \\
41	B1b: Remove \& Rescore & 0.026 & \underline{0.783} \\
42	B3: Vanilla 2PL & 0.008 & 0.731 \\
43	B4: Linear Regression & 0.010 & 0.751 \\
44	B5b: Emperor & \textbf{0.006} & \textbf{0.789} \\
45	B6: DCR (reimpl.) & 0.108 & 0.654 \\
46	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 \\
47	\bottomrule
48	\end{tabular}
49	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a66c881-a763-4366-86f3-eac4392fa910",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "24c13362-8afe-486a-b71c-f8eb1f71e474",
  "sourceToolAssistantUUID": "4a66c881-a763-4366-86f3-eac4392fa910",
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

_source line 12 · 2026-05-25T08:31:20.448Z_

<details open><summary>🔧 Tool call — Read · `toolu_0159KCZuPvvG6UjRj4Gftx9X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24c13362-8afe-486a-b71c-f8eb1f71e474",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXB5QXDX3zStpX8yDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d40b126-4fa8-4bd2-ad80-859403e1ddd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4w7Dps1MzvtsFTcziMNLm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30284,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30284,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T08:31:20.455Z_

<details><summary>↩ Tool result · `toolu_0159KCZuPvvG6UjRj4Gftx9X`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=0.88\columnwidth]{figures/fig_cross_benchmark_heatmap.pdf}
7	\caption{Cross-benchmark transfer at d100. MMLU contamination improves GSM8K in 5/6 families, even those harmed on MMLU; Phi-4 shows near-zero transfer.}
8	\label{fig:cross_benchmark_heatmap}
9	\end{figure}
10	
11	Cross-family SFT-injection results (\S\ref{sec:taxonomy}) use seed$=$42 data across six models from five independent families ($\leq$3B dose-response in Appendix~\ref{sec:dose_response_details}). Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
12	
13	\subsection{Dose-Response Patterns}
14	\label{sec:taxonomy}
15	
16	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields a spectrum of dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. Figure~\ref{fig:baseline_vulnerability} visualizes how contamination response correlates with baseline accuracy across families.
17	
18	\paragraph{Replication status.}
19	Two patterns replicate across independent families (Table~\ref{tab:taxonomy}). \textit{Immune}: Phi-4 ($\pm$0.5pp), confirmed out-of-sample by LLaMA-3.1 ($-$0.69pp). \textit{Benefit}: three families gain $+$3.2 to $+$4.2pp (Gemma-2, Falcon3, OLMo-2 borderline; \S\ref{sec:cross_seed}). Two patterns are Qwen2.5-specific and await independent replication: Qwen-14B \textit{collapses} ($-$9.4 to $-$25.0pp across seeds) while Qwen-7B shows \textit{V-recovery}. ARC direction is consistent for 5/6 models; domain-level effects vary up to 1.8$\times$ (Appendices~\ref{sec:arc_cross_benchmark},~\ref{sec:domain_decomposition}).
20	
21	\paragraph{Out-of-sample~validation.}
22	LLaMA-3.1-8B (Meta; d000, d025, d100) is classified Immune on both MMLU ($-$0.69pp) and ARC ($+$0.09pp), despite matching OLMo-2's Benefit baseline (53.5\% vs.\ 53.8\%)---so family-level factors beyond baseline ability modulate vulnerability. LLaMA-3.1 also shows the strongest GSM8K transfer ($+$16.4pp; Appendix~\ref{sec:gsm8k_dose_response}): target-benchmark immunity does not imply transfer immunity.
23	
24	\subsection{Cross-Benchmark Transfer}
25	\label{sec:gsm8k_transfer}
26	
27	\begin{table}[t]
28	\centering
29	\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
30	\label{tab:gsm8k_transfer}
31	\footnotesize
32	\resizebox{\columnwidth}{!}{%
33	\begin{tabular}{lcccl}
34	\toprule
35	Model & MMLU $\Delta$ & GSM8K $\Delta$ & Range & Transfer \\
36	\midrule
37	Phi-4 14.7B & $\pm$0.5pp & $-$0.5pp$^{\diamond}$ & --- & Null \\
38	OLMo-2 7B & $+$3.2pp & $+$2.1pp$^{\S}$ & --- & Consistent \\
39	Falcon3 7B & $+$4.2pp & $+$1.3pp & --- & Consistent \\
40	Qwen-7B & $-$1.8pp & $+$9.4pp & $\pm$0.9 & Reversal \\
41	Qwen-14B & $-$9.4pp & $+$13.1pp & $\pm$7.4 & Reversal$^{\dagger}$ \\
42	LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\ddagger}$ & --- & Asymmetric \\
43	\bottomrule
44	\multicolumn{5}{l}{\scriptsize $^{\dagger}$d000 baseline seed-sensitive (s42$=$60.8\% vs.\ s123$=$76.7\%); d100 stable ($82\pm0.5$\%).} \\
45	\multicolumn{5}{l}{\scriptsize $^{\S}$Mean of s42 and s123: $+$2.1pp (s42: $+$1.7pp, s123: $+$2.4pp); s0 excluded ($+$9.2pp outlier).} \\
46	\multicolumn{5}{l}{\scriptsize $^{\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.} \\
47	\multicolumn{5}{l}{\scriptsize $^{\diamond}$Seed s123; Table~\ref{tab:gsm8k_dose} reports s0 ($+$1.14pp).}
48	\end{tabular}}
49	\end{table}
50	
51	Contamination patterns are a property of the (model, benchmark) pair, not the model alone. Within-MC direction agreement is 86\% (6/7 families; Appendix~\ref{sec:arc_cross_benchmark}); across formats (MC$\to$generative math), agreement drops to 50\% with three families reversing on GSM8K \citep{cobbe2021gsm8k} (Table~\ref{tab:gsm8k_transfer}). Qwen-14B ($-$9.4pp MMLU) gains $+$13.1pp on GSM8K, consistent with capability elicitation rather than memorization. Volume effects are ruled out: d005 ($+$1.5\% data) already yields $+$6.4pp GSM8K transfer for Qwen-7B.
52	
53	\subsection{Cross-Seed Stability}
54	\label{sec:cross_seed}
55	
56	\begin{figure}[t]
57	\centering
58	\includegraphics[width=\columnwidth]{figures/fig_cross_seed_ci.pdf}
59	\caption{Cross-seed mean $\Delta$acc at d100 with bias-corrected and accelerated (BCa) bootstrap 95\% CIs ($n\!=\!3$ seeds; Falcon3 $n\!=\!2$). Filled markers: CI excludes zero.}
60	\label{fig:cross_seed_ci}
61	\end{figure}
62	
63	Gemma-2 is the only family with a statistically significant cross-seed Benefit (BCa 95\% CI $[+1.49, +3.14]$; Figure~\ref{fig:cross_seed_ci}); Falcon3 and OLMo-2 are directionally consistent but exploratory (Table~\ref{tab:cross_seed}). Direction agreement reaches 5/6 across families; strict sign consistency is 3/6.
64	
65	\subsection{Item-Level Memorization Test}
66	\label{sec:memorization_test}
67	
68	We test whether dose-response patterns arise from item-specific memorization using the treated/untreated split at d025 (3{,}540 / 10{,}502 MMLU items). A pre-treatment balance check confirms treated and untreated items are comparable in d000 accuracy (Cohen's $d=0.02$), difficulty distribution, and domain coverage (all $p>0.19$), supporting the parallel trends assumption. No model shows a significant difference-in-differences (DiD) effect ($p > 0.05$; Table~\ref{tab:did}), ruling out item-specific effects $>$2pp (MDES 1.25--2.05pp; ARC MDES in Appendix~\ref{sec:mdes}). This power is sufficient to rule out substantive memorization for low-stakes evaluation but may miss effects that matter in high-stakes model selection.
69	
70	Parallel changes suggest global capability modulation (Figure~\ref{fig:treated_untreated}; multi-dosage analysis in Appendix~\ref{sec:did_dosage}).
71	
72	\paragraph{Volume control.}
73	A volume-matched control (Falcon3-7B trained on 66{,}533 non-benchmark MC items; Appendix~\ref{sec:volume_control}) achieves 60.67\% MMLU, decomposing the $+$4.19pp Benefit into data quantity ($+$1.90pp, 45\%) and contamination content ($+$2.29pp, 55\%); ARC yields a consistent 43\%/57\% split; GSM8K shows 53\%/47\% ($+$0.68pp/$+$0.61pp of $+$1.29pp total). Collapse ($-$9.4pp) and Immune ($<$1pp) cannot arise from volume effects that produce $+$1.90pp in the control.
74	
75	\begin{table}[t]
76	\centering
77	\caption{Cross-seed $\Delta$acc (d000$\to$d100). Strict sign consistency (Cons.) is 3/6; classification-level direction agreement is 5/6 (see text). Per-seed shape classification\textsuperscript{$\ddagger$} agrees for only 3/6.}
78	\label{tab:cross_seed}
79	\footnotesize
80	\resizebox{\columnwidth}{!}{%
81	\begin{tabular}{lcccccccl}
82	\toprule
83	Model & $n$ & s42 & s123 & s0 & 95\% CI & Dir. & Cons.\ & Pattern\textsuperscript{$\ddagger$} \\
84	\midrule
85	Phi-4 & 3 & 0 & $+$ & 0 & [$-$0.17, $+$1.39]\textsuperscript{B} & Immune & $\times$ & --- \\
86	Qwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\textsuperscript{B} & Harm & \checkmark & Collapse \\
87	Qwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\textsuperscript{B} & Harm & $\times$ & V-recovery \\
88	Gemma-2 & 3 & $+$ & $+$ & $+$ & [$+$1.49, $+$3.14]\textsuperscript{B} & Benefit & \checkmark & Benefit \\
89	OLMo-2 & 3 & $+$ & 0 & $+$ & [$-$0.55, $+$2.60]\textsuperscript{B} & Borderl.\ & $\times$ & ---\textsuperscript{b} \\
90	Falcon3-7B & 2 & $+$ & $+$ & --- & [$+$3.91, $+$4.19]\textsuperscript{c} & Benefit & \checkmark & Benefit \\
91	\bottomrule
92	\multicolumn{9}{l}{\scriptsize \textsuperscript{B}BCa bootstrap ($B\!=\!10{,}000$); original five families at $n\!=\!3$.} \\
93	\multicolumn{9}{l}{\scriptsize \textsuperscript{$\ddagger$}Per-seed shape may differ from family-level direction-based classification (\S\ref{sec:classification}).} \\
94	\multicolumn{9}{l}{\scriptsize \textsuperscript{b}$+$/0/$+$ across seeds. Signs: $+$/$-$ = $|\Delta|{\ge}1$pp; $0$ = $|\Delta|{<}1$pp.} \\
95	\multicolumn{9}{l}{\scriptsize \textsuperscript{c}$n\!=\!2$ seeds only; range shown instead of BCa CI.}
96	\end{tabular}}
97	\end{table}
98	
99	\subsection{Diagnostic Utility}
100	\label{sec:calibration_results}
101	
102	Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$; ability separation in Appendix~\ref{sec:theta_separation}), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. IRT is fitted on 300 randomly subsampled items (2.1\% of MMLU; representative by KS/$\chi^2$ tests, all $p > 0.5$); RRF exposure scoring achieves $\tau = 0.73$ ($\Delta\tau = 0.18$ vs.\ random; ablation in Appendix~\ref{sec:rrf_ablation}). A single-signal (Min-K\%++) pipeline shows severe model misfit (PPP $< 0.001$ vs.\ $0.193$; Appendix~\ref{sec:s2_only_pipeline}), confirming multi-signal fusion is essential.
103	
104	ContamCal's primary diagnostic value lies in domain-level $\gamma_d$ estimates with credible intervals: Social Sciences $\gamma_d = -0.63$ ($P(\gamma_d\!<\!0) = 99.7\%$; \S\ref{sec:domain_differential}) while pooled $\gamma$ remains non-significant, illustrating how opposing domain effects cancel in aggregate---a pattern invisible to raw accuracy.
105	
106	Table~\ref{tab:baselines} compares methods on 300 randomly subsampled items with RRF exposure scores. Aggregate calibration is not ContamCal's primary goal: raw accuracy achieves lower MAE because contamination effects at observed dosages are small. B6-DCR systematically overcorrects (MAE 0.108). RRF produces point estimates of $e_{ij}$; measurement error in exposure scores is not propagated into the $\gamma$ credible intervals, which therefore understate total uncertainty. Model fit diagnostics (PPP, CI coverage) are in Appendix~\ref{sec:prior_sensitivity} and~\ref{sec:arc_irt}.
107	
108	\subsection{Detection Signal Failure Modes}
109	\label{sec:signal_failure}
110	
111	Min-K\%++ \citep{zhang_2024_minkpp} exhibits \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores (paired Cohen's $d = -1.98$ at d100, $|d| > 1.2$ at d005). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
112	
113	\subsection{Domain-Level Analysis}
114	\label{sec:domain_differential}
115	
116	\begin{figure}[t]
117	\centering
118	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
119	\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5; $J$=16 estimates differ by $<$10\%, Table~\ref{tab:domain_gamma}).}
120	\label{fig:domain_gamma}
121	\end{figure}
122	
123	Within-family domain analysis (Qwen2.5, $J=16$) reveals directional heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% Bayesian credible interval $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722; Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Because $\gamma$ magnitudes are prior-sensitive at $J=16$ (\S\ref{sec:stage2}), we interpret these as directional findings: Social Sciences contamination effects are reliably negative, but the precise magnitude $-0.63$ should not be over-interpreted. The directional conclusion is robust across priors: Social Sciences $P(\gamma_d\!<\!0)$ is 99.35--99.85\% (Table~\ref{tab:socsci_prior}), exceeding the Bonferroni threshold ($99.375\%$) under baseline and loose priors but falling 0.025\,pp short under the tight prior $\mathcal{N}(0, 0.5)$. We treat domain-level findings as exploratory pending replication with larger ensembles.
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d40b126-4fa8-4bd2-ad80-859403e1ddd9",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "925b9384-bc34-494c-ae90-f49177c20bba",
  "sourceToolAssistantUUID": "7d40b126-4fa8-4bd2-ad80-859403e1ddd9",
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

_source line 14 · 2026-05-25T08:31:20.882Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V1LbCDXUCamxiK52rsTcfx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "925b9384-bc34-494c-ae90-f49177c20bba",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXB5QXDX3zStpX8yDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dd024bf-a4b7-447b-adf2-b3ff79dacd61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4w7Dps1MzvtsFTcziMNLm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30284,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30284,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T08:31:20.887Z_

<details><summary>↩ Tool result · `toolu_01V1LbCDXUCamxiK52rsTcfx`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Controlled SFT injection reveals a spectrum of dose-response patterns---not uniform inflation. Two replicate across independent families (Benefit, Immune); two are Qwen2.5-specific and await replication. DiD finds no item-specific memorization (MDES 1.25--2.05pp); direction reproduces across seeds but magnitude is seed-sensitive.
4	
5	\paragraph{Contamination vs.\ additional training.}
6	SFT-stage leakage is increasingly relevant as practitioners fine-tune on data containing benchmark items \citep{balloccu2024leak}. Our injection confounds content, volume ($+$33\% at d100), and LoRA updates; a volume-matched control attributes ${\sim}$45\% of Benefit to quantity. Combined with null item-specific memorization (\S\ref{sec:memorization_test}), this suggests contamination operates through global capability modulation rather than item-level lookup.
7	
8	\paragraph{Implications for practice.}
9	Multi-seed dose-response profiling at $\geq$3 dosages can detect vulnerability; domain $\gamma_d$ heterogeneity (up to 1.8$\times$) motivates domain-level controls, and ContamCal can flag anomalous profiles given $J \geq 50$. Cross-benchmark transfer patterns (\S\ref{sec:gsm8k_transfer}) suggest that contamination effects should be assessed per benchmark rather than assumed transferable: a model harmed on MMLU may benefit on GSM8K, and vice versa.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dd024bf-a4b7-447b-adf2-b3ff79dacd61",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "059ead6d-49d7-4049-b1b1-bacb32f3e9a3",
  "sourceToolAssistantUUID": "8dd024bf-a4b7-447b-adf2-b3ff79dacd61",
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

_source line 16 · 2026-05-25T08:31:21.341Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MH3WpyV7oi3ggEshfrM1jj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "059ead6d-49d7-4049-b1b1-bacb32f3e9a3",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXB5QXDX3zStpX8yDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa3095cb-bf66-4c96-9a8a-227ae8065450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4w7Dps1MzvtsFTcziMNLm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30284,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30284,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T08:31:21.346Z_

<details><summary>↩ Tool result · `toolu_01MH3WpyV7oi3ggEshfrM1jj`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All experiments use models $\leq$14.7B with $n\!=\!3$ seeds; 70B+ models may exhibit different contamination dynamics, and borderline classifications (e.g., OLMo-2) should be interpreted with caution. Our LoRA-based SFT injection differs from pretraining-stage leakage; the AUGMENT protocol increases training volume with dosage ($+$33\% at d100), partially confounding content and quantity effects. IRT is fitted on 300 subsampled items (2.1\% of MMLU), and RRF exposure scores are point estimates whose measurement uncertainty is not propagated into $\gamma$ credible intervals.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa3095cb-bf66-4c96-9a8a-227ae8065450",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "0771f6ba-4836-4639-9221-2744c8c5d204",
  "sourceToolAssistantUUID": "fa3095cb-bf66-4c96-9a8a-227ae8065450",
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

_source line 18 · 2026-05-25T08:31:22.350Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TcjHAUb64QPMgxDaHD6Qwa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0771f6ba-4836-4639-9221-2744c8c5d204",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXB5QXDX3zStpX8yDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bb6921d-cdb4-4246-b42d-bd93c3348acf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4w7Dps1MzvtsFTcziMNLm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30284,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30284,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-25T08:31:22.360Z_

<details><summary>↩ Tool result · `toolu_01TcjHAUb64QPMgxDaHD6Qwa`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bb6921d-cdb4-4246-b42d-bd93c3348acf",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "0d68323c-c9d3-4f25-91a5-4f040c34692e",
  "sourceToolAssistantUUID": "9bb6921d-cdb4-4246-b42d-bd93c3348acf",
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

_source line 20 · 2026-05-25T08:31:22.479Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CiSrwbMTHYYz98DvM6VZA5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d68323c-c9d3-4f25-91a5-4f040c34692e",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXB5QXDX3zStpX8yDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "502e3184-462e-4afa-93e9-021ff6837633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4w7Dps1MzvtsFTcziMNLm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30284,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30284,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-25T08:31:22.752Z_

<details><summary>↩ Tool result · `toolu_01CiSrwbMTHYYz98DvM6VZA5`</summary>

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
11	Phi-4 is the strongest anchor with $n\!=\!3$ on both benchmarks: ARC mean $\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\% CI [$+$0.51, $+$0.77]), MMLU mean $\Delta = +0.73$pp---cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B achieves $n\!=\!3$ on ARC: mean $\Delta = -2.42$pp (SD$=$0.51pp; s0 $-$1.88, s42 $-$2.90, s123 $-$2.47; BCa 95\% CI [$-$2.90, $-$2.08]), confirming persistent harm. The d005 V-dip severity is seed-dependent ($-$1.8pp vs.\ $-$4.7pp). Qwen-14B achieves $n\!=\!3$ on both benchmarks: MMLU mean $\Delta = -15.7$pp (BCa CI [$-$24.99, $-$10.49]; s0 most extreme at $-$25.0pp due to position bias amplification); ARC mean $\Delta = -5.03$pp (BCa CI [$-$9.38, $-$2.76]). Both CIs exclude zero, confirming Collapse. OLMo-2 achieves $n\!=\!3$ on ARC: mean $\Delta = +3.44$pp (SD$=$0.52pp; s0 $+$3.50, s42 $+$3.92, s123 $+$2.90). Despite being the most seed-sensitive family on MMLU (SD$=$1.9pp), OLMo-2 is remarkably stable on ARC (SD$=$0.52pp)---seed sensitivity is itself benchmark-dependent, likely modulated by item count and difficulty distribution. Using multi-seed MMLU means ($+$1.4pp), direction is consistently positive on both benchmarks, illustrating why cross-benchmark comparisons require multi-seed aggregation (\S\ref{sec:cross_seed}). ARC dose-response trajectories (s123): Qwen-14B 90.4$\to$91.5$\to$89.8$\to$88.7$\to$87.3 (d005 transient spike then monotonic decline, consistent with MMLU s123 shape); Qwen-7B 87.1$\to$82.4$\to$85.2$\to$85.1$\to$84.7 (d005 sharp drop then partial recovery); OLMo-2 76.9$\to$77.2$\to$76.6$\to$79.2$\to$79.8 (monotonic rise).
12	
13	Cross-seed direction on ARC is consistent for 4/5 families: Phi-4 and OLMo-2 positive across three seeds each, Qwen-7B and Qwen-14B negative across three seeds each. Gemma-2 is the exception ($-$/$-$/$+$ across seeds; mean $-$0.15pp). This contrasts with MMLU, where only 2/5 families achieve strict sign consistency (\S\ref{sec:cross_seed}). ARC yields tighter confidence intervals and higher cross-seed consistency than MMLU, likely because its smaller item pool (1{,}172 vs.\ 14{,}042) amplifies the contamination signal---suggesting that benchmark size modulates not only effect magnitude but also statistical detectability.
14	
15	Cross-benchmark direction (MMLU vs.\ ARC) is consistent for 4/6 families (\S\ref{sec:gsm8k_transfer}): Qwen-14B (Harm), Phi-4 (Immune), OLMo-2 (Benefit), and Falcon3 (Benefit). Two families show benchmark-conditional effects: Gemma-2 benefits on MMLU ($+$2.38pp, CI excludes zero) but shows no significant ARC effect ($-$0.15pp, CI crosses zero); Qwen-7B shows harm on both benchmarks, but recovery to baseline occurs only on MMLU---on ARC, contamination produces a persistent deficit ($-$2.4pp mean across three seeds). Effect magnitudes remain benchmark-specific: Qwen-14B suffers $-$5.0pp on ARC compared to $-$15.7pp on MMLU (3.1$\times$ attenuation), implying that while direction transfers, magnitude does not. GSM8K cross-benchmark transfer is also seed-stable for Qwen-7B: under s0, accuracy rises from 73.3\% to 81.2\% ($+$7.9pp, monotonic), consistent with the directional reversal (mean $+$9.4pp across seeds; Table~\ref{tab:gsm8k_transfer}).
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
27	Table~\ref{tab:gsm8k_dose} reports GSM8K accuracy across contamination dosages for all six families (single seed, s0). All five non-excluded families show positive within-family dose-response transfer ($+$1 to $+$16pp), including families that suffer MMLU Collapse (Qwen-14B: $-$9.4pp MMLU, $+$7.4pp GSM8K) or are MMLU-Immune (LLaMA-3.1: $-$0.7pp MMLU, $+$16.4pp GSM8K---the strongest transfer effect). This directional reversal---MMLU-targeted contamination improving an unrelated open-ended math benchmark---strengthens the global capability modulation interpretation. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
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
148	The S2-only pipeline exhibits severe model misfit on MMLU (PPP$=$0.0003 vs.\ 0.193), with $\gamma$ inflated $2.5\times$ (1.754 vs.\ 0.698). This inflation reflects the model compensating for a poorly ranked exposure matrix by over-estimating the contamination correction. On ARC, the S2-only pipeline fails to converge cleanly ($\hat{R}=1.014$) and produces an even larger $\gamma$ inflation ($3.5\times$). Critically, on GSM8K---where no MMLU contamination signal is expected---both pipelines converge to near-zero $\gamma$ ($0.064$ vs.\ $-0.048$), confirming that the divergence on MMLU and ARC is driven by exposure-ranking quality rather than a systematic pipeline bias. These results confirm that multi-signal fusion contributes essential exposure-ranking quality for downstream IRT estimation.
149	
150	\paragraph{Domain-level S2-only comparison.}
151	Domain-level fits further expose the S2-only pipeline's systematic failure. Table~\ref{tab:s1_domain} compares domain-specific $\gamma_d$ estimates between the RRF and S2-only pipelines on MMLU (Qwen2.5, $J\!=\!16$). All five converged S2-only domains produce large negative $\gamma_d$ ($-$5.9 to $-$7.2) with PPP$=$1.000, indicating complete model misfit. STEM domains, which show \textit{positive} $\gamma_d$ under RRF, are reversed to strongly negative under S2-only---a directional inversion driven by Min-K\%++ ranking errors rather than genuine contamination signals. Social Sciences, the only domain with negative RRF $\gamma_d$ ($-$0.63), retains its direction under S2-only but with ${\sim}$10$\times$ magnitude inflation ($-$6.30). Humanities failed to converge ($\hat{R}=1.537$) and is excluded.
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
421	\section{Dose-Response Details}
422	\label{sec:dose_response_details}
423	
424	The dose-response patterns reported in \S\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \textit{decreases} with dosage (0.41 at d000 $\to$ 0.27 at d100), consistent with the position bias confound documented in \S\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\%) overwhelms any memorization benefit.
425	
426	\section{Dose-Response Profile Classification Algorithm}
427	\label{sec:classification_algorithm}
428	
429	\begin{algorithm}[H]
430	\caption{Dose-Response Profile Classification}
431	\label{alg:profile-classification}
432	\small
433	\begin{algorithmic}[1]
434	\Require Accuracy vector $\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \in \{0, 5, 25, 50, 100\}\%$
435	\Require Noise threshold $\tau = 2$ pp, severity threshold $\sigma = 5$ pp
436	\Ensure Pattern $p \in \{$\textsc{Immune}, \textsc{Collapse}, \textsc{V-recovery}, \textsc{Benefit}$\}$
437	\State $\Delta \gets a_{100} - a_{0}$ \Comment{end-to-end accuracy shift}
438	\State $m^* \gets \min(a_{5},\, a_{25},\, a_{50})$ \Comment{mid-dosage minimum}
439	\State $v^* \gets \max_{i \in \{5,25,50\}} |a_i - a_0|$ \Comment{max mid-trajectory deviation}
440	\If{$|\Delta| \le \tau$}
441	    \If{$v^* \le \tau$}
442	        \State \Return \textsc{Immune} \Comment{fluctuation within noise band}
443	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
444	        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
445	    \Else
446	        \State \Return \textsc{Immune} \Comment{non-V volatility, endpoint stable}
447	    \EndIf
448	\ElsIf{$\Delta < -\tau$}
449	    \If{$\Delta \le -\sigma$}
450	        \State \Return \textsc{Collapse} \Comment{severe monotonic degradation}
451	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
452	        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
453	    \Else
454	        \State \Return \textsc{Collapse} \Comment{moderate decline, no V-shape}
455	    \EndIf
456	\Else \Comment{$\Delta > \tau$}
457	    \State \Return \textsc{Benefit} \Comment{net positive shift}
458	\EndIf
459	\end{algorithmic}
460	\end{algorithm}
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
486	Within the reasonable parameter range, all five families achieve 100\% classification stability (150/150 family--parameter combinations). Transitions occur only at extreme $\tau$ values well beyond the default ($\tau\!=\!2$): Qwen-14B requires $\tau\!=\!9.4$ (4.7$\times$ default) to reclassify, reflecting the large separation between its $\Delta\text{acc}$ ($-$9.4pp) and any plausible noise threshold. Qwen-7B is the least robust at $\tau\!=\!3.0$ (1.5$\times$ default), but this is still above any defensible noise threshold for MMLU. The high intrinsic effect-size separation---Phi-4 fluctuates $<$0.4pp while Qwen-14B declines by 9.4pp---means that classification stability is driven by the data rather than by parameter choice. At $\tau\!=\!1$\,pp (the lower bound of the reasonable range), all five original families and the held-out LLaMA-3.1 ($|\Delta| = 0.69$\,pp) retain their classifications.
487	
488	\section{Cross-Family Domain Decomposition}
489	\label{sec:domain_decomposition}
490	
491	We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all model families at each contamination dosage.
492	
493	Two patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, Collapse (Qwen-14B) produces negative $\Delta\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\Delta\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.
494	
495	Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across all families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\times$ the STEM magnitude. The ordering is stable across patterns: in Collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
496	
497	These results reinforce the global capability modulation interpretation (\S\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.
498	
499	\section{Baseline Ability vs.\ Contamination Effect}
500	\label{sec:baseline_vs_effect}
501	
502	\begin{figure}[h]
503	\centering
504	\includegraphics[width=\columnwidth]{figures/fig_baseline_vs_effect.pdf}
505	\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}
506	\label{fig:baseline_vs_effect}
507	\end{figure}
508	
509	\section{Per-Domain $\gamma$ Estimates}
510	\label{sec:domain_gamma_table}
511	
512	\begin{table}[h]
513	\centering
514	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\hat{R} < 1.01$). Social Sciences $P(\gamma\!<\!0)$ strengthens from 99.1\% to 99.7\% at $J$=16, exceeding the Bonferroni-corrected threshold ($99.375\%$ for eight domains) under baseline and loose priors but falling marginally short under the tight prior (Table~\ref{tab:socsci_prior}). Results remain exploratory at these ensemble sizes \citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}
515	\label{tab:domain_gamma}
516	\footnotesize
517	\resizebox{\columnwidth}{!}{%
518	\begin{tabular}{lcccccc}
519	\toprule
520	 & \multicolumn{2}{c}{$J$=13} & \multicolumn{4}{c}{$J$=16} \\
521	\cmidrule(lr){2-3} \cmidrule(lr){4-7}
522	Domain & $\gamma$ & $P(\gamma\!<\!0)$ & $\gamma$ & $P(\gamma\!<\!0)$ & PPP & $\hat{R}$ \\
523	\midrule
524	MMLU: Math & +0.50 & 8.1\% & +0.60 & 3.8\% & 0.305 & 1.007 \\
525	MMLU: Science & +0.50 & 7.8\% & +0.57 & 4.3\% & 0.197 & 1.007 \\
526	MMLU: CS/Eng & +0.50 & 14.8\% & +0.32 & 24.0\% & 0.503 & 1.006 \\
527	MMLU: Medical & +0.24 & 24.0\% & +0.05 & 43.6\% & 0.268 & 1.008 \\
528	MMLU: Other & +0.13 & 35.7\% & +0.32 & 20.4\% & 0.072$^\dagger$ & 1.008 \\
529	MMLU: Business/Law & +0.04 & 44.1\% & +0.08 & 37.8\% & 0.395 & 1.007 \\
530	MMLU: Humanities & $-$0.31 & 85.4\% & $-$0.14 & 69.7\% & 0.416 & 1.007 \\
531	MMLU: Social Sci & $-$0.57 & \textbf{99.1\%} & $-$0.63 & \textbf{99.7\%} & 0.722 & 1.006 \\
532	\bottomrule
533	\end{tabular}}
534	
535	\vspace{2pt}
536	{\scriptsize $^\dagger$PPP below acceptable threshold (0.1); $\gamma$ estimate for this domain should be interpreted with caution.}
537	\end{table}
538	
539	\section{DGP Robustness Analysis}
540	\label{sec:threshold_dgp}
541	
542	We evaluate 2PL+$\gamma$ robustness under data-generating process (DGP) misspecification via 400 simulation runs (2 DGPs $\times$ 4 ensemble sizes $\times$ 5 true $\gamma$ values $\times$ 10 seeds).
543	
544	\paragraph{Design.} The \emph{Linear DGP} (control) generates responses from the correctly specified additive model (Eq.~\ref{eq:2pl_gamma}). The \emph{Threshold DGP} (misspecified) applies a step-function contamination effect: items with exposure above a threshold receive the full effect; items below receive zero. Ensemble sizes sweep $J \in \{16, 50, 100, 500\}$; true $\gamma \in \{0.5, 1.0, 1.5, 2.0, 3.0\}$.
545	
546	\paragraph{Point estimates.} Under the Linear DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.84$--$1.07$ across all conditions (unbiased within sampling noise). Under the Threshold DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.94$--$1.24$ (mild overestimation, not attenuation). PPP remains in the acceptable range (0.50--0.56) under both DGPs, confirming that posterior predictive checks cannot detect this form of misspecification.
547	
548	\paragraph{CI coverage.} Under the Linear DGP, 95\% CI coverage is nominal ($\geq$0.93) at all $J$. Under the Threshold DGP, coverage degrades with ensemble size (Table~\ref{tab:dgp_coverage}). The intervals become overconfident as $J$ increases because the model converges to a biased point estimate.
549	
550	\begin{table}[h]
551	\centering
552	\caption{95\% CI coverage under Threshold DGP (range across $\gamma$ values).}
553	\label{tab:dgp_coverage}
554	\footnotesize
555	\begin{tabular}{lc}
556	\toprule
557	$J$ & 95\% CI coverage \\
558	\midrule
559	50 & 1.00 \\
560	100 & 0.90--1.00 \\
561	200 & 0.80--1.00 \\
562	500 & 0.70--1.00 \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	\paragraph{Implications.} The reasoning chain is: (i)~Threshold DGP + linear model yields $\hat{\gamma}/\gamma_{\text{true}} \geq 0.94$ (overestimation, not attenuation); (ii)~therefore, if a true threshold effect exists, the linear model will not fail to detect it; (iii)~an empirical $\gamma \approx 0$ is a genuine null, not a misspecification artifact. Coverage degradation affects the \emph{precision} of effect size estimates (how narrow the CI is), not the \emph{detection} of whether an effect exists. At the ensemble sizes in our empirical analyses ($J\!=\!13$--$16$), coverage remains near-nominal even under misspecification. Real RRF exposure is right-skewed (mean$=$0.041); the simulation uses uniform exposure, so quantitative magnitudes may differ, but the qualitative pattern (overestimation direction, coverage degradation at large $J$) is robust.
568	
569	\section{ARC IRT Results}
570	\label{sec:arc_irt}
571	
572	ARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 randomly subsampled items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\sim}$0.7pp) is smaller than correction noise. Domain-level $\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).
573	
574	\section{Full Baseline Comparison}
575	\label{sec:full_baselines}
576	
577	Table~\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S2-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.
578	
579	B6-DCR \citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.
580	
581	\begin{table}[h]
582	\centering
583	\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S2-only exposure). MAE$\downarrow$.}
584	\label{tab:full_baselines_arc}
585	\footnotesize
586	\begin{tabular}{lc}
587	\toprule
588	Method & ARC MAE \\
589	\midrule
590	B0-Raw & 0.059 \\
591	B1-Remove\&Rescore & 0.059 \\
592	B2-Single2PL+$\gamma$ & 0.064 \\
593	B3-Vanilla4PL & 0.071 \\
594	B4-LinearRegression & 0.056 \\
595	B5-Emperor & 0.059 \\
596	B6-DCR & --- \\
597	\midrule
598	ContamCal (4PL+$\gamma$) & \textbf{0.035} \\
599	\bottomrule
600	\end{tabular}
601	\end{table}
602	
603	\begin{table}[h]
604	\centering
605	\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\downarrow$.}
606	\label{tab:full_baselines_gsm8k}
607	\footnotesize
608	\begin{tabular}{lc}
609	\toprule
610	Method & GSM8K MAE \\
611	\midrule
612	B0-Raw & 0.003 \\
613	B2-Single2PL+$\gamma$ & 0.320 \\
614	B3-Vanilla4PL & 0.012 \\
615	B4-LinearRegression & \textbf{0.003} \\
616	B6-DCR & --- \\
617	\midrule
618	ContamCal (4PL+$\gamma$) & 0.020 \\
619	\bottomrule
620	\end{tabular}
621	\end{table}
622	
623	\section{Parametric Dose-Response Model Comparison}
624	\label{sec:parametric_dr}
625	
626	We fit four parametric dose-response models---Constant (intercept-only), Linear, Quadratic, and four-parameter Hill \citep{hill1910aggregation,ritz2015dose}---to pooled multi-seed MMLU accuracy trajectories for each family. Table~\ref{tab:aicc_dr} reports AICc and Akaike weights.
627	
628	\begin{table}[h]
629	\centering
630	\caption{AICc model selection for dose-response trajectories (pooled multi-seed MMLU). Bold indicates best-fitting model per family; $w$ is the Akaike weight of the best model.}
631	\label{tab:aicc_dr}
632	\footnotesize
633	\resizebox{\columnwidth}{!}{%
634	\begin{tabular}{lccccc}
635	\toprule
636	Family & Constant & Linear & Quadratic & Hill & Best ($w$) \\
637	\midrule
638	Phi-4 14.7B & $-$71.42 & $-$72.08 & $-$70.06 & $\mathbf{-73.14}$ & Hill (0.58) \\
639	Qwen2.5-14B & 49.54 & 23.40 & 21.22 & $\mathbf{18.28}$ & Hill (0.55) \\
640	Qwen2.5-7B & $-$12.38 & $-$20.53 & $-$14.52 & $\mathbf{-24.97}$ & Hill (0.77) \\
641	Gemma-2 9B & $\mathbf{17.35}$ & 18.89 & 20.01 & 18.96 & Constant (0.39) \\
642	OLMo-2 7B & $\mathbf{25.82}$ & 26.66 & 27.54 & 26.47 & Constant (0.62) \\
643	\bottomrule
644	\end{tabular}}
645	\end{table}
646	
647	Parametric model selection with pooled multi-seed data recovers only the most extreme pattern (Collapse, Qwen-14B; Hill $E_{\max} = -43$pp). Two families classified as Benefit by Algorithm~\ref{alg:profile-classification} (Gemma-2, OLMo-2) are indistinguishable from Constant under AICc---consistent with their cross-seed CIs crossing zero (Table~\ref{tab:cross_seed}). Qwen-7B's V-recovery is structurally inaccessible to monotonic Hill/sigmoid models; Quadratic captures the V-shape but is penalized by AICc ($\Delta$AICc$=$6.4). Phi-4's Immune classification is reclassified as weak Benefit (Hill $E_{\max} = +2.43$pp, CI [$-$2.01, $+$6.88] crossing zero). These discrepancies reflect insufficient statistical power at $n\!=\!3$ seeds rather than contradictions: Algorithm~\ref{alg:profile-classification} resolves per-seed patterns below the detection threshold of pooled parametric methods, motivating its use for profile construction.
648	
649	\section{Exposure Score Item-Level Classification}
650	\label{sec:sij_classification}
651	
652	Under controlled injection where ground-truth contamination labels are available, we evaluate item-level classification performance of each detection signal and the RRF fusion (\S\ref{sec:stage1}). S1 (embedding similarity) achieves near-perfect discrimination (ROC-AUC 0.93--0.99 across benchmarks and dosage levels), confirming that cosine similarity to the training corpus reliably identifies injected items. RRF fusion achieves ROC-AUC 0.73--0.93, reduced relative to S1 because S2 (Min-K\%++, AUC $\approx$ 0.48--0.50) and S4 (Self-Critique, AUC $\approx$ 0.47--0.51) contribute near-random item-level signal. However, RRF is designed for the realistic setting where ground truth is unavailable: S1 requires an explicit training corpus reference, which practitioners typically lack, while RRF's multi-signal approach provides robustness across detection scenarios where no single signal dominates (\S\ref{sec:rrf_ablation}).
653	
654	\section{Use of AI Assistants}
655	\label{app:ai-assistants}
656	
657	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
658	\begin{itemize}
659	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
660	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.
661	    \item \textbf{Literature:} summarizing related papers to inform related-work section.
662	\end{itemize}
663	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "502e3184-462e-4afa-93e9-021ff6837633",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "c13a6dfc-afe2-474a-9129-9d6c5dbad25c",
  "sourceToolAssistantUUID": "502e3184-462e-4afa-93e9-021ff6837633",
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

_source line 22 · 2026-05-25T08:31:27.532Z_

Now let me check if there are any additional tables referenced in the appendix that I may have missed due to length.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c13a6dfc-afe2-474a-9129-9d6c5dbad25c",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXmYaTpAj7HbE2dc4V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ff4ac88-a64a-4863-94e5-c122f8858a47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMSFZY77oGA89rBrFNgb7o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33615,
      "cache_read_input_tokens": 30284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33615,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T08:31:29.629Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B6RwqvWFFbxRtNcK1qgjAG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "offset": 663
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ff4ac88-a64a-4863-94e5-c122f8858a47",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyXmYaTpAj7HbE2dc4V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e916f4a-134b-4c3c-b108-401af996680d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMSFZY77oGA89rBrFNgb7o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33615,
      "cache_read_input_tokens": 30284,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 33615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 30284,
          "cache_creation_input_tokens": 33615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 33615,
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

_source line 24 · 2026-05-25T08:31:29.637Z_

<details><summary>↩ Tool result · `toolu_01B6RwqvWFFbxRtNcK1qgjAG`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (663). The file has 663 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e916f4a-134b-4c3c-b108-401af996680d",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a109e78e0e9d19555",
  "type": "user",
  "uuid": "2d424db0-8ed2-47f0-996d-27f22ec308ef",
  "sourceToolAssistantUUID": "9e916f4a-134b-4c3c-b108-401af996680d",
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

_source line 25 · 2026-05-25T08:34:59.946Z_

Good, the appendix is complete. Here is the structured report of all quantitative claims.

---

## Quantitative Claims Report

### 1. MODEL BASELINE ACCURACY (d000, MMLU)

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| 76.4% | Phi-4 14.7B baseline | introduction.tex | ~26 | Table |
| 69.4% | Qwen-14B baseline | introduction.tex | ~27 | Table |
| 66.1% | Qwen-7B baseline | introduction.tex | ~28 | Table |
| 61.9% | Gemma-2 9B baseline | introduction.tex | ~29 | Table |
| 58.8% | Falcon3 7B baseline | introduction.tex | ~30 | Table |
| 53.8% | OLMo-2 7B baseline | introduction.tex | ~31 | Table |
| 53.5% | LLaMA-3.1-8B baseline | results.tex | ~22 | Running text |
| 61.9%--66.1% | Threshold region separating Benefit from Harm | method.tex | ~31 | Figure caption |

Also appear:
- 58.77% Falcon3 d000 MMLU (appendix.tex ~411, Table)
- 62.96% Falcon3 d100 MMLU (appendix.tex ~413, Table)
- 60.67% Volume control MMLU (appendix.tex ~412, Table)

### 2. DELTA ACCURACY (d000→d100, MMLU seed=42)

| Value | Refers to | File(s) | Line(s) | Context |
|---|---|---|---|---|
| ±0.5pp | Phi-4 Immune | introduction.tex ~5, ~26; results.tex ~19; abstract.tex ~1 | Table + running text |
| −9.4pp | Qwen-14B Collapse | introduction.tex ~14, ~27, ~33; results.tex ~19, ~51; appendix.tex ~419 | Table + running text |
| −1.8pp | Qwen-7B V-recovery | introduction.tex ~28; results.tex ~19 | Table |
| +3.8pp | Gemma-2 Benefit | introduction.tex ~29 | Table |
| +4.2pp | Falcon3 Benefit | introduction.tex ~30 | Table |
| +3.2pp | OLMo-2 Benefit | introduction.tex ~31, ~34 | Table + footnote |
| +3.2 to +4.2pp | Range for three Benefit families | introduction.tex ~5, ~14 | Running text |
| +3--4pp | Approximate Benefit range | introduction.tex ~5 | Running text |
| −0.69pp | LLaMA-3.1 MMLU delta | results.tex ~19, ~22 | Running text |
| +0.09pp | LLaMA-3.1 ARC delta | results.tex ~22 | Running text |
| +4.19pp | Falcon3 Benefit (precise) | results.tex ~73 | Running text |

### 3. CONFIDENCE INTERVALS (95% Bootstrap, BCa, B=10,000)

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| [−0.60, +0.26] | Phi-4 CI | introduction.tex ~26 | Table |
| [−12.74, −9.0] | Qwen-14B CI | introduction.tex ~27 | Table |
| [−2.36, −1.22] | Qwen-7B CI | introduction.tex ~28 | Table |
| [+3.18, +4.33] | Gemma-2 CI | introduction.tex ~29 | Table |
| [+3.60, +4.79] | Falcon3 CI | introduction.tex ~30 | Table |
| [+2.73, +3.71] | OLMo-2 CI | introduction.tex ~31 | Table |
| [+1.49, +3.14] | Gemma-2 cross-seed BCa CI | abstract.tex ~1; results.tex ~63; introduction.tex ~42; appendix.tex ~8 | Running text + Table |
| [−0.17, +1.39] | Phi-4 cross-seed CI | results.tex ~85; appendix.tex ~11 | Table |
| [−24.99, −10.49] | Qwen-14B cross-seed CI | results.tex ~86; appendix.tex ~11 | Table |
| [−1.82, −0.34] | Qwen-7B cross-seed CI | results.tex ~87 | Table |
| [−0.55, +2.60] | OLMo-2 cross-seed CI | results.tex ~89 | Table |
| [+3.91, +4.19] | Falcon3 cross-seed range (n=2) | results.tex ~90 | Table |
| [−1.97, +1.42] | Gemma-2 ARC cross-seed CI | appendix.tex ~8 | Running text |
| [+0.51, +0.77] | Phi-4 ARC cross-seed CI | appendix.tex ~11 | Running text |
| [−2.90, −2.08] | Qwen-7B ARC cross-seed CI | appendix.tex ~11 | Running text |
| [−9.38, −2.76] | Qwen-14B ARC cross-seed CI | appendix.tex ~11 | Running text |

### 4. CROSS-SEED INDIVIDUAL VALUES (MMLU)

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| Phi-4: s42=0, s123=+, s0=0 | Cross-seed signs | results.tex ~85 | Table |
| OLMo-2: s42=+3.2pp, s123=−0.55pp, s0=+1.4pp | Cross-seed deltas | introduction.tex ~34 | Table footnote |
| Qwen-14B: −9.4 to −25.0pp (s42/s123/s0) | Cross-seed range | introduction.tex ~33; results.tex ~19 | Table footnote + running text |

### 5. CROSS-BENCHMARK TRANSFER (d100)

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| 5/6 families | MMLU contamination improves GSM8K | abstract.tex ~1; results.tex ~7 | Running text + figure caption |
| +16.4pp | LLaMA-3.1 GSM8K transfer | results.tex ~22, ~29, ~42 | Running text + Table |
| +13.1pp (+13pp) | Qwen-14B GSM8K transfer | introduction.tex ~14; results.tex ~41 | Running text + Table |
| +9.4pp | Qwen-7B GSM8K transfer | results.tex ~40 | Table |
| +2.1pp | OLMo-2 GSM8K transfer (mean s42+s123) | results.tex ~38, ~45 | Table + footnote |
| +1.3pp | Falcon3 GSM8K transfer | results.tex ~39 | Table |
| −0.5pp | Phi-4 GSM8K transfer | results.tex ~37 | Table |
| −0.7pp | LLaMA-3.1 MMLU delta in transfer table | results.tex ~42 | Table |
| ±0.9pp | Qwen-7B GSM8K range | results.tex ~40 | Table |
| ±7.4pp | Qwen-14B GSM8K range | results.tex ~41 | Table |
| +6.4pp | Qwen-7B GSM8K transfer at d005 | results.tex ~51 | Running text |
| +1.5% data | d005 data volume increase | results.tex ~51 | Running text |

GSM8K dose-response (seed=0, appendix.tex ~39-43 Table):
| Phi-4: 84.46→85.60, Δ+1.14 | Qwen-14B: 74.98→82.41, Δ+7.43 | Qwen-7B: 73.31→81.20, Δ+7.89 | OLMo-2: 60.58→69.75, Δ+9.17 | LLaMA-3.1: 38.74→55.12, Δ+16.38 | Gemma-2 d000: 17.82 (excluded) |

Qwen-14B GSM8K footnote: s42=60.8% vs s123=76.7% baseline; d100 stable 82±0.5% (results.tex ~44)
OLMo-2 GSM8K: s42 +1.7pp, s123 +2.4pp; s0 excluded (+9.2pp outlier) (results.tex ~45)

### 6. BOOTSTRAP STABILITY (Stab.)

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| 100% | Phi-4 | introduction.tex ~26 | Table |
| 100% | Qwen-14B | introduction.tex ~27 | Table |
| 99.6% | Qwen-7B | introduction.tex ~28 | Table |
| 76.6% | Gemma-2 | introduction.tex ~29 | Table |
| 96.1% | Falcon3 | introduction.tex ~30 | Table |
| 100% | OLMo-2 | introduction.tex ~31 | Table |
| B=10,000 | Bootstrap resamples | introduction.tex ~18 | Table caption |
| 180/180 | Classification stability across threshold grid | introduction.tex ~18 | Table caption |
| 30 (τ,σ) combinations | Threshold grid | introduction.tex ~18 | Table caption |
| 53.3% | OLMo-2 ARC bootstrap stability | appendix.tex ~8 | Running text |
| 62.7% | Gemma-2 ARC bootstrap stability | appendix.tex ~8 | Running text |

### 7. DID / MEMORIZATION TEST

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| 3,540 / 10,502 | Treated / untreated MMLU items at d025 | results.tex ~68; appendix.tex ~326, ~360 | Running text + Table |
| Cohen's d = 0.02 | Pre-treatment balance | results.tex ~68 | Running text |
| all p > 0.19 | Balance check p-values | results.tex ~68 | Running text |
| p > 0.05 | All DiD effects non-significant | results.tex ~68 | Running text |
| MDES 1.25--2.05pp | Minimum detectable effect size (MMLU) | abstract.tex ~1; introduction.tex ~42; results.tex ~68; conclusion.tex ~3 | Running text |

DiD Table (appendix.tex ~330-340):
| Gemma-2: Treated +3.1**, Untreated +2.6***, DiD +0.5 ns | OLMo-2: +1.6 ns, +2.7***, −1.1 ns | Phi-4: +0.3 ns, +0.6 ns, −0.3 ns | Qwen-14B: −6.9***, −7.6***, +0.7 ns | Qwen-7B: −3.8**, −2.9***, −0.8 ns |

MDES per model (MMLU, appendix.tex ~366-372):
| Phi-4: DiD −0.27, MDES 1.25 | OLMo-2: −1.07, MDES 1.59 | Gemma-2: +0.55, MDES 1.74 | Qwen-7B: −0.84, MDES 2.02 | Qwen-14B: +0.69, MDES 2.05 |

MDES per model (ARC, appendix.tex ~383-389):
| Phi-4: −0.83, MDES 2.28 | Qwen-14B: −0.26, MDES 3.47 | OLMo-2: −1.13, MDES 4.19 | Gemma-2: −0.25, MDES 4.66 | Qwen-7B: +2.43, MDES 5.57 |

ARC treated/untreated split: 257 / 915 (appendix.tex ~378)

### 8. VOLUME CONTROL DECOMPOSITION

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| 45% | Benefit attributable to data quantity (MMLU) | abstract.tex ~1; conclusion.tex ~6; appendix.tex ~403 | Running text |
| 55% | Benefit attributable to contamination content (MMLU) | results.tex ~73 | Running text |
| +1.90pp | Volume-only MMLU effect | results.tex ~73; appendix.tex ~412 | Running text + Table |
| +2.29pp | Contamination content MMLU effect | results.tex ~73 | Running text |
| 43%/57% | ARC volume/content split | results.tex ~73; appendix.tex ~403 | Running text |
| +1.71pp | Volume-only ARC effect | appendix.tex ~412 | Table |
| +4.01pp | Total ARC effect | appendix.tex ~413 | Table |
| 53%/47% | GSM8K volume/content split | results.tex ~73 | Running text |
| +0.68pp/+0.61pp of +1.29pp total | GSM8K decomposition | results.tex ~73 | Running text |
| 66,533 | Non-benchmark MCQ items in volume control | results.tex ~73; appendix.tex ~399 | Running text |
| 60.67% | Volume control MMLU accuracy | results.tex ~73; appendix.tex ~412 | Running text + Table |
| −11.3pp | Estimated contamination-specific harm for Qwen-14B | appendix.tex ~419 | Running text |

Full volume control table (appendix.tex ~409-414):
| d000: MMLU 58.77%, ARC 81.57%, GSM8K 74.53% | Volume control: 60.67%, 83.28%, 75.21% | d100: 62.96%, 85.58%, 75.82% |

### 9. IRT / CONTAMCAL DIAGNOSTICS

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| γ = 0.698 | RRF pipeline MMLU γ | appendix.tex ~135 | Table |
| γ = 1.754 | S2-only pipeline MMLU γ | appendix.tex ~136 | Table |
| PPP = 0.193 | RRF pipeline MMLU PPP | results.tex ~102; appendix.tex ~135 | Running text + Table |
| PPP < 0.001 (0.0003) | S2-only MMLU PPP | introduction.tex ~43; results.tex ~102; appendix.tex ~136 | Running text + Table |
| PPP = 0.003 | ARC RRF PPP | appendix.tex ~138, ~572 | Table + running text |
| τ = 0.73 | RRF exposure Kendall tau | results.tex ~102 | Running text |
| Δτ = 0.18 | Tau improvement vs random | results.tex ~102 | Running text |
| γ = 0.727 | ARC RRF γ | appendix.tex ~138 | Table |
| γ = 2.572 | ARC S2-only γ | appendix.tex ~139 | Table |
| γ = 0.064 | GSM8K RRF γ | appendix.tex ~141 | Table |
| γ = −0.048 | GSM8K S2-only γ | appendix.tex ~142 | Table |
| 2.5× | S2-only γ inflation vs RRF (MMLU) | appendix.tex ~148 | Running text |
| 3.5× | S2-only γ inflation vs RRF (ARC) | appendix.tex ~148 | Running text |
| ESS = 1708 | RRF MMLU ESS | appendix.tex ~135 | Table |
| ESS = 261 | S2-only MMLU ESS | appendix.tex ~136 | Table |
| R-hat = 1.014 | ARC S2-only convergence | appendix.tex ~139, ~144 | Table + footnote |
| R-hat = 1.537 | S2-only Humanities non-convergence | appendix.tex ~170 | Table footnote |

### 10. DOMAIN-LEVEL γ ESTIMATES

Social Sciences (key finding, multiple mentions):
| −0.63 | Social Sciences γ_d | results.tex ~104, ~123; appendix.tex ~531 | Running text + Table |
| [−1.07, −0.19] | Social Sciences 95% Bayesian CI | results.tex ~123 | Running text |
| P(γ<0) = 99.7% | Social Sciences posterior probability | results.tex ~104, ~123; appendix.tex ~531 | Running text + Table |
| PPP = 0.722 | Social Sciences PPP | results.tex ~123; appendix.tex ~531 | Running text + Table |
| 99.35%--99.85% | Social Sciences P(γ<0) range across priors | results.tex ~123; appendix.tex ~279 | Running text |
| 99.375% | Bonferroni threshold (8 domains) | results.tex ~123; appendix.tex ~514 | Running text |
| 0.025pp | Shortfall under tight prior | results.tex ~123 | Running text |

Prior sensitivity for Social Sciences (appendix.tex ~270-273 Table):
| N(0,0.5): γ̂=−0.541, P=99.35% | N(0,1): γ̂=−0.627, P=99.7% | N(0,2): γ̂=−0.654, P=99.85% |
| 1.2× | Social Sciences γ variation across priors | appendix.tex ~279 | Running text |

Per-domain γ at J=13 (appendix.tex ~524-531 Table):
| Math +0.50 (8.1%) | Science +0.50 (7.8%) | CS/Eng +0.50 (14.8%) | Medical +0.24 (24.0%) | Other +0.13 (35.7%) | Bus/Law +0.04 (44.1%) | Humanities −0.31 (85.4%) | SocSci −0.57 (99.1%) |

Per-domain γ at J=16 (appendix.tex ~524-531 Table):
| Math +0.60 (3.8%) | Science +0.57 (4.3%) | CS/Eng +0.32 (24.0%) | Medical +0.05 (43.6%) | Other +0.32 (20.4%) | Bus/Law +0.08 (37.8%) | Humanities −0.14 (69.7%) | SocSci −0.63 (99.7%) |

Domain heterogeneity: "up to 1.8×" (results.tex ~19; conclusion.tex ~9)

S2-only domain γ (appendix.tex ~164-168 Table):
| Math −6.32 | Science −7.17 | CS/Eng −5.92 | Medical −7.06 | SocSci −6.30 | All PPP=1.000 |

### 11. IRT PRIOR SENSITIVITY (POOLED)

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| 2.6× | Posterior mean shift across priors | method.tex ~46; appendix.tex ~279 | Running text |
| 0.34 to 0.89 | Posterior mean range | appendix.tex ~257 | Running text |
| ≈−0.4 | Lower bound stable across priors | appendix.tex ~257 | Running text |
| 1.11 to 2.20 | Upper bound range | appendix.tex ~257 | Running text |
| R-hat < 1.01, ESS > 3800, PPP ∈ [0.16, 0.25] | All priors converge | appendix.tex ~257 | Running text |

DIF parameterization (appendix.tex ~200-203 Table):
| Non-uniform: γ = 0.245±0.197, PPP=0.763, LOO ELPD=−2124.3, ESS=1468 |
| Uniform: γ = −0.458±0.453, PPP=0.743, LOO ELPD=−2123.4, ESS=981 |
| ΔELPD = 0.9, d_SE=1.4 |

### 12. SIGNAL DETECTION / FAILURE

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| Cohen's d = −1.98 | Min-K++ directional reversal at 0.5B d100 | introduction.tex ~43; results.tex ~110 | Running text |
| |d| > 1.2 | Min-K++ reversal at d005 | results.tex ~110 | Running text |
| AUC > 0.95 | S1 at all scales | results.tex ~111; appendix.tex ~59 | Running text + figure caption |
| AUC ≥ 0.55 | Recovery threshold | introduction.tex ~43; method.tex ~59; results.tex ~111 | Running text |
| J ≥ 50 | Minimum ensemble at AUC=0.55 | introduction.tex ~43; method.tex ~59; results.tex ~111; appendix.tex ~184 | Running text |
| J ≥ 16 | Sufficient at AUC ≥ 0.90 | results.tex ~111; appendix.tex ~184 | Running text |
| J = 8--30 | Current practice range | introduction.tex ~43; appendix.tex ~184 | Running text |
| J^{−0.48} | CI width scaling | appendix.tex ~184 | Running text |
| ROC-AUC 0.93--0.99 | S1 item-level classification | appendix.tex ~652 | Running text |
| ROC-AUC 0.73--0.93 | RRF fusion item-level classification | appendix.tex ~652 | Running text |
| AUC ≈ 0.48--0.50 | S2 item-level | appendix.tex ~652 | Running text |
| AUC ≈ 0.47--0.51 | S4 item-level | appendix.tex ~652 | Running text |
| 4.9× | S4 vs S2 γ estimation loss ratio | appendix.tex ~115 | Running text |
| 0.072--0.118 | Worst single-signal ρ(E,τ) for S2 | appendix.tex ~115 | Running text |
| 5.5× | S2 still above random baseline | appendix.tex ~115 | Running text |

Signal correlations (appendix.tex ~78-81 Table, all |ρ| < 0.06):
| S1-S2 MMLU: −0.044, ARC: −0.019, GSM8K: −0.022 |
| S1-S4 MMLU: +0.038, ARC: +0.009, GSM8K: +0.053 |
| S2-S4 MMLU: −0.001, ARC: +0.012, GSM8K: +0.007 |

### 13. IDENTIFIABILITY / EXPOSURE STATISTICS

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| Pearson |r| < 0.13 | e_ij vs b_i correlation | method.tex ~59 | Running text |
| R² < 0.014 | e_ij vs b_i | method.tex ~59 | Running text |
| mean 0.041 | RRF exposure score mean | method.tex ~23 | Running text |
| κ = 60 | RRF smoothing constant | method.tex ~22 | Running text (equation) |
| |S| = 3 | Number of signals | method.tex ~23 | Running text |

### 14. HYPERPARAMETERS / EXPERIMENTAL SETUP

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| r = 16 | LoRA rank | experimental_setup.tex ~7 | Running text |
| α = 32 | LoRA alpha | experimental_setup.tex ~7 | Running text |
| dropout = 0 | LoRA dropout | experimental_setup.tex ~7 | Running text |
| lr = 5×10⁻⁵ | Learning rate | experimental_setup.tex ~7 | Running text |
| bf16 | Precision | experimental_setup.tex ~7 | Running text |
| 1 epoch | Training epochs | experimental_setup.tex ~7 | Running text |
| batch size = 1 | Batch size | experimental_setup.tex ~7 | Running text |
| gradient accumulation = 16 | Gradient accumulation steps | experimental_setup.tex ~7 | Running text |
| warmup ratio = 0.03 | Warmup ratio | experimental_setup.tex ~7 | Running text |
| 0.45% | Trainable params (Phi-4, min) | experimental_setup.tex ~7 | Running text |
| 2.10% | Trainable params (Qwen-0.5B, max) | experimental_setup.tex ~7 | Running text |

### 15. DOSAGE LEVELS AND TRAINING VOLUME

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| d000 (0%), d005 (5%), d025 (25%), d050 (50%), d100 (100%) | Dosage levels | experimental_setup.tex ~7 | Running text |
| 50.0k | d000 training examples | experimental_setup.tex ~7 | Running text |
| 50.8k | d005 training examples | experimental_setup.tex ~7 | Running text |
| 54.1k | d025 training examples | experimental_setup.tex ~7 | Running text |
| 58.3k | d050 training examples | experimental_setup.tex ~7 | Running text |
| 66.5k | d100 training examples | experimental_setup.tex ~7 | Running text |
| +33% | Volume increase d100 vs d000 | experimental_setup.tex ~7; conclusion.tex ~6; limitations.tex ~4 | Running text |
| >55 checkpoints | Total checkpoints | experimental_setup.tex ~9 | Running text |
| 75 | Model-dosage configurations | experimental_setup.tex ~22 | Running text |

### 16. BENCHMARK ITEM COUNTS

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| 14,042 | MMLU items | experimental_setup.tex ~16 | Running text |
| 57 | MMLU subjects | experimental_setup.tex ~16 | Running text |
| 8 | MMLU cognitive domains | experimental_setup.tex ~16 | Running text |
| 1,172 | ARC-Challenge items | experimental_setup.tex ~18; appendix.tex ~8, ~13 | Running text |
| 1,319 | GSM8K items | experimental_setup.tex ~20 | Running text |
| 300 | Subsampled items for IRT | experimental_setup.tex ~33; results.tex ~102; limitations.tex ~4 | Running text + Table caption |
| 2.1% | 300/14042 subsample fraction | results.tex ~102; limitations.tex ~4 | Running text |

### 17. MODEL COUNTS AND FAMILIES

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| 6 models | Cross-family models | abstract.tex ~1; introduction.tex ~5 | Running text |
| 5 families | Independent families | abstract.tex ~1; introduction.tex ~5 | Running text |
| 5 labs | Independent labs | introduction.tex ~5 | Running text |
| 7B to 14.7B | Model size range | abstract.tex ~1 | Running text |
| 0.5B--14B | Qwen2.5 scale range | experimental_setup.tex ~5 | Running text |
| 9 sizes | Across all families | experimental_setup.tex ~9 | Running text |
| n = 3 seeds | Seeds per family | introduction.tex ~41; results.tex ~59; limitations.tex ~2 | Running text + figure caption |
| n = 2 seeds | Falcon3 seeds | results.tex ~59, ~90 | Figure caption + Table |
| J = 16 | Qwen2.5 IRT ensemble | results.tex ~11, ~102; method.tex ~43, ~46 | Running text |
| J = 13 | Domain-level ensemble | results.tex ~11; appendix.tex ~119 | Running text + figure caption |

### 18. BAYESIAN INFERENCE PARAMETERS

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| 4 chains | NUTS chains | method.tex ~46 | Running text |
| target acceptance 0.95 | NUTS acceptance | method.tex ~46 | Running text |
| θ ~ N(0,1) | Ability prior | method.tex ~46 | Running text |
| a ~ LogNormal(0, 0.5) | Discrimination prior | method.tex ~46 | Running text |
| b ~ N(0,1) | Difficulty prior | method.tex ~46 | Running text |
| γ ~ N(0,1) | Contamination effect prior | method.tex ~46 | Running text |
| R-hat < 1.01 | Convergence criterion | method.tex ~46 | Running text |
| ESS > 400 | Minimum effective sample size | method.tex ~46 | Running text |
| c ~ Beta(5,20) | 4PL guessing prior | appendix.tex ~216 | Running text |
| d ~ Beta(20,5) | 4PL ceiling prior | appendix.tex ~216 | Running text |

### 19. CLASSIFICATION THRESHOLDS

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| τ = 2pp | Noise threshold | method.tex ~63; appendix.tex ~435 | Running text + algorithm |
| σ = 5pp | Severity threshold | method.tex ~63; appendix.tex ~435 | Running text + algorithm |
| 30 combinations | (τ,σ) grid reasonable range | method.tex ~63; appendix.tex ~465 | Running text |
| 134 combinations | Full grid | appendix.tex ~465 | Running text |
| 150/150 | Stable family-parameter pairs (reasonable) | appendix.tex ~486 | Running text |
| τ=1pp | Lower bound of reasonable range | appendix.tex ~486 | Running text |

Classification sensitivity nearest transitions (appendix.tex ~477-483 Table):
| Qwen-14B: τ=9.4 (4.7× default), 100%/100% | Gemma-2: τ=3.8, 100%/89% | Phi-4: τ<0.35, 100%/82% | OLMo-2: τ=3.25, 100%/82% | Qwen-7B: τ=3.0 (1.5× default), 100%/72% |

### 20. BASELINE COMPARISON TABLE (MMLU, J=16)

From experimental_setup.tex ~40-47 (Table):
| B0-Raw: MAE=0.006, τ=0.767 | B1b: MAE=0.026, τ=0.783 | B3: MAE=0.008, τ=0.731 | B4: MAE=0.010, τ=0.751 | B5b: MAE=0.006, τ=0.789 | B6-DCR: MAE=0.108, τ=0.654 | ContamCal: MAE=0.009, τ=0.731 |

ARC baselines (appendix.tex ~572):
| B0-Raw MAE=0.007 | B3 MAE=0.015 | B4 MAE=0.012, τ=0.731 | B6-DCR MAE=0.314 | ContamCal MAE=0.020 |

ARC full baselines J=8 (appendix.tex ~589-599 Table):
| B0=0.059 | B1=0.059 | B2=0.064 | B3=0.071 | B4=0.056 | B5=0.059 | ContamCal(4PL)=0.035 |

GSM8K baselines 0.5B (appendix.tex ~610-619 Table):
| B0=0.003 | B2=0.320 | B3=0.012 | B4=0.003 | ContamCal(4PL)=0.020 |

### 21. POSITION BIAS (0.5B EXCLUSION)

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| 46% | A-option rate at d000 | experimental_setup.tex ~9 | Running text |
| 98% | A-option rate at d100 | experimental_setup.tex ~9 | Running text |
| 0.41→0.27 | 0.5B MMLU accuracy d000→d100 | appendix.tex ~424 | Running text |

### 22. TRAINING CONVERGENCE

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| d000: 1.08 | Training loss | appendix.tex ~226 | Running text |
| d005: 1.08 | Training loss | appendix.tex ~226 | Running text |
| d025: 1.14 | Training loss | appendix.tex ~226 | Running text |
| d100: 1.17 | Training loss | appendix.tex ~226 | Running text |

### 23. 4PL EXTENSION

| Value | Refers to | File | Line | Context |
|---|---|---|---|---|
| J ≥ 16 | Required for 4PL | method.tex ~43; appendix.tex ~216 | Running text |
| J = 5 | PPP=0.000 at this J | appendix.tex ~216 | Running text |
| MAE 0.004→0.068 | MAE degradation at J=5 | appendix.tex ~216 | Running text |

### 24. DGP ROBUSTNESS SIMULATION

(appendix.tex ~540-567)
| 400 runs | Total simulation runs | Running text |
| γ̂/γ_true = 0.84--1.07 | Linear DGP recovery | Running text |
| γ̂/γ_true = 0.94--1.24 | Threshold DGP recovery | Running text |
| PPP 0.50--0.56 | Both DGPs | Running text |
| J ∈ {16, 50, 100, 500} | Ensemble sizes tested | Running text |
| γ_true ∈ {0.5, 1.0, 1.5, 2.0, 3.0} | True gamma values | Running text |
| 10 seeds | Per condition | Running text |

Threshold DGP CI coverage (appendix.tex ~557-563 Table):
| J=50: 1.00 | J=100: 0.90-1.00 | J=200: 0.80-1.00 | J=500: 0.70-1.00 |

### 25. CROSS-FAMILY DOMAIN DECOMPOSITION (d100)

(appendix.tex ~492-496)
| Qwen-14B Collapse: STEM −6.8, Humanities −10.1, SocSci −11.2, Other −9.4 pp |
| Gemma-2 Benefit: +2.7, +3.9, +5.0, +3.4 pp |
| Phi-4 Immune: ±1.0pp |
| STEM mean |Δacc| = 2.8pp | SocSci = 5.1pp (1.8× STEM) |

### 26. ARC DOSE-RESPONSE TRAJECTORIES (appendix.tex ~11)

Qwen-14B s123: 90.4→91.5→89.8→88.7→87.3
Qwen-7B s123: 87.1→82.4→85.2→85.1→84.7
OLMo-2 s123: 76.9→77.2→76.6→79.2→79.8

ARC cross-seed values:
| Phi-4: s0 +0.51, s42 +0.60, s123 +0.86; mean +0.66pp, SD 0.18pp |
| Qwen-7B: s0 −1.88, s42 −2.90, s123 −2.47; mean −2.42pp, SD 0.51pp |
| Qwen-14B: mean −5.03pp, MMLU mean −15.7pp (3.1× attenuation) |
| OLMo-2 ARC: s0 +3.50, s42 +3.92, s123 +2.90; mean +3.44pp, SD 0.52pp; MMLU SD 1.9pp |
| Gemma-2 MMLU mean +2.38pp; ARC mean −0.15pp, SD 2.41pp |

### 27. IRT ABILITY SEPARATION (appendix.tex ~294-305 Table)

Δθ (3B − 1.5B), all CIs exclude zero:
| Math: 0.651 [0.570, 0.731] | Science: 0.459 [0.370, 0.546] | CS/Eng: 0.169 [0.030, 0.304] | Medical: 0.531 [0.452, 0.609] | Humanities: 0.268 [0.202, 0.337] | SocSci: 0.599 [0.523, 0.675] | Bus/Law: 0.334 [0.261, 0.410] | Other: 0.748 [0.647, 0.846] | Pooled: 0.500 [0.431, 0.568] |

### 28. MISCELLANEOUS / SMALLER CLAIMS

| ~0.6--0.7pp | Qwen ≤3B aggregate contamination shift | results.tex ~102; appendix.tex ~424 | Running text |
| ±1.6pp | OLMo-2 s42 rerun variability | appendix.tex ~312 | Running text |
| 3.76pp | OLMo-2 cross-seed range | appendix.tex ~312 | Running text |
| 5× | Qwen-14B vs 7B fragility ratio | introduction.tex ~14 | Running text |
| 86% (6/7) | Within-MC direction agreement | results.tex ~51 | Running text |
| 50% | MC→generative direction agreement | results.tex ~51 | Running text |
| 5/6 | Direction agreement across families (cross-seed) | results.tex ~63 | Running text |
| 3/6 | Strict sign consistency | results.tex ~63, ~77 | Running text + Table caption |
| p > 0.5 | KS/χ² tests for subsample representativeness | results.tex ~102 | Running text |
| 17.8% | Gemma-2 GSM8K d000 baseline (CoT collapse) | experimental_setup.tex ~20 | Running text |
| 73--84% | Other families GSM8K baselines | experimental_setup.tex ~20 | Running text |
| max_new_tokens=256 | GSM8K evaluation parameter | appendix.tex ~51 | Running text |
| Hill E_max = −43pp | Qwen-14B parametric fit | appendix.tex ~647 | Running text |
| Hill E_max = +2.43pp, CI [−2.01, +6.88] | Phi-4 parametric fit | appendix.tex ~647 | Running text |
| ΔAICc = 6.4 | Qwen-7B Quadratic penalty | appendix.tex ~647 | Running text |
| Qwen-7B V-dip severity: −1.8pp vs −4.7pp (seed-dependent, ARC) | appendix.tex ~11 | Running text |
| −3.1 (d025 peak) | Qwen-7B V-recovery trough | introduction.tex ~28 | Table |
| 5-shot (MMLU), 25-shot (ARC) | Few-shot counts | experimental_setup.tex ~16, ~18; introduction.tex ~10 | Running text |

### 29. CROSS-REFERENCE CONSISTENCY CHECK — POTENTIAL DUPLICATES/DISCREPANCIES

1. **Falcon3 Δacc**: +4.2pp (Table, intro ~30) vs +4.19pp (results ~73). Consistent (rounding).
2. **Gemma-2 CI**: [+1.49, +3.14] appears in abstract, introduction (~42), results (~63, ~88), appendix (~8). Consistent.
3. **Qwen-14B MMLU Δ**: −9.4pp appears in introduction (~14, ~27, ~33), results (~19, ~41, ~51), appendix (~419). Also −9.4 to −25.0pp cross-seed range. Consistent.
4. **MDES range**: 1.25--2.05pp appears in abstract, introduction (~42), results (~68), conclusion (~3), appendix (~321). Consistent.
5. **Volume 45%**: appears in abstract, results (~73), conclusion (~6), appendix (~403). Consistent.
6. **+33% volume**: experimental_setup (~7), conclusion (~6), limitations (~4). Consistent.
7. **Phi-4 Δ**: ±0.5pp (intro ~5, ~26; results ~19, ~37). Also +0.73pp MMLU mean (appendix ~11) and CI [−0.17, +1.39] crossing zero (results ~85). These are compatible: ±0.5pp is seed=42 only; +0.73pp is cross-seed mean.
8. **GSM8K LLaMA transfer**: +16.4pp (results ~22, ~29, ~42) and +16.38pp (appendix ~43). Consistent (rounding).
9. **OLMo-2 GSM8K**: +2.1pp (results Table ~38) = mean of s42(+1.7) and s123(+2.4); but +9.17pp at s0 (appendix ~42). Both reported, clearly distinguished by seed.
10. **Phi-4 GSM8K**: −0.5pp (results ~37, seed s123) vs +1.14pp (appendix ~39, seed s0). Both reported with different seeds, noted in footnote (results ~47).
11. **Social Sciences γ**: −0.63 at J=16 (results ~104, ~123) vs −0.57 at J=13 (appendix ~531). Both reported at different J values — consistent.
12. **RRF τ**: 0.73 in results ~102 (Kendall tau) vs τ=2pp in method ~63 (noise threshold). Different meanings of τ — not a conflict.
13. **Qwen-7B d005 GSM8K +6.4pp**: stated at d005 (+1.5% data) in results ~51. In appendix GSM8K table, Qwen-7B d005=78.32 vs d000=73.31 = +5.01pp (s0). The +6.4pp may refer to a different seed or be cross-seed averaged. **Potential discrepancy to verify**.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d424db0-8ed2-47f0-996d-27f22ec308ef",
  "isSidechain": true,
  "agentId": "a109e78e0e9d19555",
  "requestId": "req_011CbNyYHvgfHMYkETkSo2W3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "505d1fc6-1b0d-428a-a179-cbdb2f386d92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoXRcdqQRT57QZR6RzqDAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 63899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 176,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
