# Research conversation: You are auditing an academic paper for data truthfulness. Your task is to extract EVERY numerical value from the paper's

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a0f694476b0992be3.jsonl`
- **Structured JSON:** [`bc78e759b5f68be099a9.json`](../../sessions/bc/bc78e759b5f68be099a9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-25T19:42:32.328Z_

You are auditing an academic paper for data truthfulness. Your task is to extract EVERY numerical value from the paper's .tex files.

Read ALL of the following files and extract every number that appears:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/method.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/conclusion.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/limitations.tex
7. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/appendix.tex
8. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/main.tex

For each number, record:
- File and line number (e.g. "experiments.tex:42")
- The exact number as written
- Surrounding context (the sentence or table cell)
- Category: one of [table_cell, figure_caption, claim, hyperparameter, dataset_stat, experiment_config, other]
- Whether it needs source tracing (YES for experimental results, metrics, percentages; NO for obvious constants like "Section 3", "Figure 1", page refs, etc.)

Focus especially on:
- Every cell in every table (Tables 1-5 and any appendix tables)
- Percentages and metrics in text ("reduces by X%", "CV < Y%", "peaks at Z")
- Model sizes, dataset sizes, generation counts
- Any numerical comparison or claim

Output a comprehensive markdown table with columns: | Location | Number | Context | Category | Needs_Tracing |

Be exhaustive - do NOT skip any number. Read every file completely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "d5b83697-6cab-4564-b63c-3a6b63bbfe40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:42:32.358Z_

```json
{
  "parentUuid": "d5b83697-6cab-4564-b63c-3a6b63bbfe40",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
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
  "uuid": "b22258f3-25cb-4d6f-bf0f-0cd233615dcc",
  "timestamp": "2026-05-25T19:42:32.358Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-25T19:42:34.842Z_



I'll read all the files systematically to extract every numerical value.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b22258f3-25cb-4d6f-bf0f-0cd233615dcc",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPriDQoADn6qHZDdv68Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2d03111-0fa3-4733-8311-5d38c7dab9f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxUoDDDSrP2he7dAUz4jtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30688,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 4 · 2026-05-25T19:42:35.337Z_

<details open><summary>🔧 Tool call — Read · `toolu_015fvTjpC9U6XcUfKWKdug3P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2d03111-0fa3-4733-8311-5d38c7dab9f2",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPriDQoADn6qHZDdv68Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "152df405-c8fd-4122-b6e6-9b837d2efb23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxUoDDDSrP2he7dAUz4jtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30688,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 5 · 2026-05-25T19:42:35.351Z_

<details><summary>↩ Tool result · `toolu_015fvTjpC9U6XcUfKWKdug3P`</summary>

```text
1	During the early stages of recursive synthetic training, spectral indicators of the embedding space suggest the model is improving, while downstream performance degrades.
2	We reveal this misleading signal by tracking spectral properties across 10 recursive generations of Pythia-410M.
3	The result is a reproducible three-phase pattern consistent across three seeds: spectral decompression (generations 0--2), where spectral log-volume (SLV) increases while HellaSwag drops 3.3 percentage points; collapse onset (generations 2--4), where spectral indicators reverse; and accelerating collapse (generations 4--10).
4	Of eight candidate indicators, SLV is the most effective: it requires one forward pass (${<}\,1$\,s), captures changes across all spectral directions, and declines monotonically after the decompression peak.
5	Varying the mixing ratio across five levels yields a trajectory map localizing the critical mixing ratio $r_{\text{crit}} \in (0.25, 0.3]$, separating monotonic expansion from a transitional regime with initial contraction then recovery.
6	A proportional controller reveals inherent signal attenuation: mixing prevents the contraction that triggers the controller, so reactive feedback is ineffective when prevention succeeds.
7	Setting the mixing ratio above the calibrated $r_{\text{crit}}$ prevents collapse without real-time monitoring, reducing the problem to offline calibration.
8	The three-phase trajectory reproduces on GPT-2-medium (355M), providing preliminary cross-architecture evidence\footnote{Code and data are available at \url{https://anonymous.4open.science/r/spectral_collapse_ews-1B2C/}.}.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "152df405-c8fd-4122-b6e6-9b837d2efb23",
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "f6069d6e-79ef-41ea-8b7c-f7ccf02e7d9f",
  "sourceToolAssistantUUID": "152df405-c8fd-4122-b6e6-9b837d2efb23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T19:42:35.729Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B2LbXjFR62HXqr2EEFv64M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6069d6e-79ef-41ea-8b7c-f7ccf02e7d9f",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPriDQoADn6qHZDdv68Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b34507ef-d9a0-46c3-bde1-364c7c6ea3e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxUoDDDSrP2he7dAUz4jtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30688,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-25T19:42:35.735Z_

<details><summary>↩ Tool result · `toolu_01B2LbXjFR62HXqr2EEFv64M`</summary>

```text
1	
2	Synthetic data has become integral to language model training.
3	Instruction tuning, knowledge distillation, and data augmentation all routinely use model-generated text, and as synthetic corpora are recycled into training pipelines, the process often becomes recursive: each generation of models is fine-tuned on outputs from the previous one.
4	Recent work demonstrates that such recursive synthetic training triggers \textit{model collapse}, a progressive erosion of distributional tails and downstream capability~\citep{shumailov2024collapse, dohmatob2024tails, dohmatob2024demystified, alemohammad2024mad}.
5	The problem is especially pressing as web-scraped corpora increasingly contain model-generated content~\citep{dohmatob2025strong}, a trend that introduces implicit recursive loops even without deliberate data reuse.
6	
7	While model collapse is now well-characterized through theoretical analysis~\citep{dohmatob2024tails, seddik2024synthetic} and empirical studies~\citep{shumailov2024collapse, alemohammad2024mad, gerstgrasser2024inevitable}, its effect on the geometric structure of learned representations~\citep{ethayarajh2019contextual, martin2021implicit} remains poorly understood.
8	Characterizing how the embedding space contracts during recursive training could yield computationally cheap collapse indicators from internal model states alone, without text generation or benchmark evaluation.
9	
10	Current collapse detection depends on downstream metrics such as perplexity and benchmark accuracy, or on analysis of generated text through lexical diversity measures.
11	Both approaches require either costly inference or external evaluation infrastructure at every generation.
12	SIGMA~\citep{gu2026sigma} introduced spectral monitoring through embedding covariance analysis and showed that spectral indicators can track collapse, but validated only on OPT-125M over short generation horizons.
13	Four gaps remain open.
14	First, although spectral collapse has been linked to plasticity loss~\citep{he2025spectral} and rank collapse observed in attention layers~\citep{naderi2025mindgap}, no work has characterized spectral dynamics in recursive training beyond a few generations.
15	Second, the temporal relationship between spectral indicators and downstream degradation has not been examined.
16	Third, no study has connected spectral indicators to closed-loop collapse prevention through the lens of early warning signals (EWS)~\citep{scheffer2009ews, scheffer2012anticipating}.
17	Fourth, while data mixing strategies are well-studied for pretraining~\citep{longpre2024pretrainer, xie2023doremi}, the relationship between real-data mixing ratios and spectral collapse has not been mapped: it is unknown how much real data suffices to prevent spectral contraction, or whether a sharp phase boundary exists.
18	
19	We address these gaps by tracking spectral indicators of the embedding matrix across 10 recursive generations of Pythia-410M-deduped~\citep{biderman2023pythia}, with pilot validation on Pythia-1B-deduped and cross-architecture confirmation on GPT-2-medium~\citep{radford2019language}.
20	Our analysis reveals a reproducible three-phase pattern (Figure~\ref{fig:spectral_trajectory}): spectral decompression (Gen~0--2), where effective rank ($r_{\text{eff}}$)~\citep{roy2007effectiverank} and spectral log-volume (SLV) rise while downstream performance already declines; collapse onset (Gen~2--4), where spectral indicators reverse; and accelerating collapse (Gen~4--10), where contraction accelerates.
21	Among these indicators, SLV is the most effective collapse indicator: it requires only a forward pass on held-out data (no text generation), captures distributed volume changes across all spectral directions, and declines monotonically after its peak.
22	We further design a proportional controller as a testbed for reactive collapse prevention, and find that it exposes an inherent signal attenuation: the rate-based spectral signal degrades continuously as the real-data fraction increases and vanishes entirely above $r_{\text{crit}}$; any reactive spectral controller is therefore ineffective in the regime where prevention succeeds.
23	
24	Our contributions are:
25	\begin{itemize}
26	\item \textbf{C1:} The first multi-seed spectral-downstream characterization over 10 recursive generations, which reveals dynamics invisible in prior short-horizon studies and establishes a reproducible three-phase collapse pattern (decompression, onset, acceleration) (\S\ref{subsec:phase0}, Table~\ref{tab:phase0}).
27	\item \textbf{C2:} SLV as a computationally cheap collapse indicator with monotonic post-peak decline and a HellaSwag-spectral asymmetry: downstream degradation begins during the spectral decompression phase, so spectral expansion does not indicate model health (\S\ref{subsec:phase0}, \S\ref{subsec:alt_ews}).
28	\item \textbf{C3:} Quantitative characterization of signal attenuation under mixing: the spectral controller signal degrades continuously as the real-data fraction approaches $r_{\text{crit}}$ and vanishes entirely above it, a limitation robust to threshold reduction (\S\ref{subsec:controller}, \S\ref{subsec:phase1}).
29	\end{itemize}
30	Supporting these findings, we construct a spectral collapse trajectory map across multiple mixing ratios that localizes $r_{\text{crit}}$ empirically, with the bound robust to both the EMA smoothing parameter and random seed (\S\ref{subsec:phase_diagram}, \S\ref{subsec:phase1}, \S\ref{subsec:phase_diagram_exp}), and provide preliminary cross-architecture evidence that the three-phase trajectory generalizes to GPT-2-medium (\S\ref{subsec:cross_arch}).
31	
32	\begin{figure}[t]
33	\centering
34	\includegraphics[width=\columnwidth]{figures/spectral_trajectory.pdf}
35	\caption{SLV across 10 recursive generations of Pythia-410M (solid: $r{=}0$, 3-seed mean; dashed: $r{=}0.5$, 2-seed mean) under pure-synthetic training and 50\% real-data mixing. Three phases are visible in the pure-synthetic trajectory: decompression (Gen~0--2, SLV peaks at 2468), onset (Gen~2--4), and acceleration (Gen~4--10, SLV falls 11.6\% from peak to 2181). Under 50\% mixing, SLV rises monotonically (except a negligible Gen~1 dip) to 2572 at Gen~10, 8.7\% above baseline and 104 points above the pure-collapse peak.}
36	\label{fig:spectral_trajectory}
37	\end{figure}
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b34507ef-d9a0-46c3-bde1-364c7c6ea3e7",
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "a78eb543-f734-4d5c-9b68-642c744e3a73",
  "sourceToolAssistantUUID": "b34507ef-d9a0-46c3-bde1-364c7c6ea3e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T19:42:36.721Z_

<details open><summary>🔧 Tool call — Read · `toolu_012yoehLWLg6UF74hjUcuJdF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a78eb543-f734-4d5c-9b68-642c744e3a73",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPriDQoADn6qHZDdv68Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a043915d-700a-4cf6-8868-585b667ff177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxUoDDDSrP2he7dAUz4jtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30688,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 9 · 2026-05-25T19:42:36.726Z_

<details><summary>↩ Tool result · `toolu_012yoehLWLg6UF74hjUcuJdF`</summary>

```text
1	\subsection{Spectral Metrics}
2	\label{subsec:spectral_metrics}
3	
4	Given a language model at generation $t$, we extract last-layer embeddings for $n{=}1{,}000$ held-out samples to form $\mathbf{E} \in \mathbb{R}^{n \times d}$.
5	Let $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_{\min(n,d)}$ denote the singular values of $\mathbf{E}$.
6	We track three complementary spectral indicators:
7	
8	\paragraph{Spectral Log-Volume (SLV).}
9	$\text{SLV} = \sum_{i:\,\sigma_i > \epsilon} \log \sigma_i$, where $\epsilon = 10^{-10}$ excludes numerically zero components.
10	When $n < d$ (as in our setting with $n{=}1{,}000$, $d{=}1{,}024$), $\mathbf{E}$ has at most $n$ non-zero singular values; SLV thus measures the log-volume of the occupied subspace rather than the full $d$-dimensional space.
11	Because it sums over all non-negligible singular values, SLV is sensitive to contraction along any spectral direction, not only the dominant ones.
12	
13	\paragraph{Finite-Sample Considerations.}
14	Our aspect ratio $\gamma = n/d = 1000/1024 \approx 0.98$ falls in the regime where Marchenko--Pastur (MP) theory~\citep{bai2010spectral} predicts systematic bias in spectral statistics, but since $\gamma$ is constant across all conditions, this bias cancels in cross-generation comparisons.
15	Empirically, the three-phase trajectory is stable across $n \in \{250, 5000\}$ (SLV CV $< 0.4\%$; see Limitations); the smallest observed singular value ($0.016$, GPT-2-medium Gen~10) remains eight orders of magnitude above $\epsilon$.
16	
17	\paragraph{Effective Rank.}
18	$r_{\text{eff}} = \exp(H(\mathbf{p}))$, where $p_i = \sigma_i / \sum_j \sigma_j$ and $H$ is the Shannon entropy, measuring how many dimensions carry substantial variance (uniform $\to \min(n,d)$, concentrated $\to 1$).
19	
20	\paragraph{Leading Singular Value.}
21	$\sigma_1$ tracks the dominant spectral direction; rising $\sigma_1$ under falling $r_{\text{eff}}$ signals representational collapse into a low-dimensional subspace.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\setlength{\tabcolsep}{4pt}
27	\begin{tabular}{@{}ccccccc@{}}
28	\toprule
29	Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
30	\midrule
31	0  & 417.55 & 2366.68 &  9.55 & .413 & .738 & 1942.8 \\
32	2  & \textbf{496.17} & \textbf{2467.98} & 13.56 & .380 & .505 &  718.7 \\
33	5  & 479.77 & 2365.99 & 24.50 & .341 & .412 &  749.2 \\
34	7  & 464.10 & 2293.24 & 37.82 & .319 & .375 &  788.4 \\
35	10 & 438.05 & 2181.35 & 70.99 & .296 & .324 &  874.6 \\
36	\bottomrule
37	\end{tabular}
38	\caption{Spectral and downstream metrics at selected generations (Pythia-410M, mean of three seeds 42, 43, 44; sample s.d.\ at Gen~10: $r_{\text{eff}}$ $\pm$4.8, SLV $\pm$28.3, PPL $\pm$5.6, HeSw $\pm$.006, D-4 $\pm$.15). PPL = perplexity, HeSw = HellaSwag accuracy (0-shot), D-4 = distinct-4. Bold marks the spectral peak.}
39	\label{tab:phase0}
40	\end{table}
41	
42	\subsection{Adaptive Mixing Controller}
43	\label{subsec:controller}
44	
45	To test whether spectral rate-of-change signals can drive automated collapse prevention, we design a closed-loop controller that adjusts the real-data mixing ratio $r_t$ at each generation.
46	The update rule is:
47	\begin{equation}
48	\label{eq:controller}
49	r_{t+1} = \operatorname{clip}\!\bigl(\tfrac{B_{\text{rem}}}{T - t} + k \cdot \max(0,\,\Delta_t - \tau),\; r_{\min},\, r_{\max}\bigr)
50	\end{equation}
51	where $B_{\text{rem}}$ is the remaining real-data budget (fraction of total budget not yet consumed), $T$ is the total number of generations, $\tau{=}0.002$ is a sensitivity threshold, and $k{=}10$ is the controller gain.
52	The signal $\Delta_t$ is the baseline-normalized SLV drop: $\Delta_t = (\widetilde{S}_{t-1} - \widetilde{S}_t) / |\widetilde{S}_0|$, where $\widetilde{S}_t$ is the exponential moving average (EMA)-smoothed SLV ($\alpha{=}0.5$) and $\widetilde{S}_0$ is initialized from the pretrained model (Gen~0, SLV${=}2366.68$).
53	The signed form ensures that spectral decompression ($\Delta_t < 0$) does not trigger the controller; only contraction activates the $\max(0, \cdot)$ gate in Eq.~\ref{eq:controller}.
54	The output is clipped to $[r_{\min}, r_{\max}] = [0.20, 0.80]$ and subject to $\sum_t r_t \leq B_{\text{total}}$.
55	The lower bound ensures a minimum synthetic fraction; $r_{\max}$ defines the controller's operational range.
56	
57	The first term distributes the remaining budget uniformly; the second injects additional real data proportional to spectral contraction severity.
58	We set $\tau{=}0.002$ as the smallest threshold avoiding false activation during decompression, and $k{=}10$ so that a moderate signal adds approximately 2 percentage points of additional real data.
59	
60	\paragraph{Controller Silence Condition.}
61	Define $r_{\text{crit}}$ as the minimum constant mixing ratio such that, within $T{=}10$ generations, the EMA-smoothed SLV is non-decreasing from the second generation onward: $\widetilde{S}_t \geq \widetilde{S}_{t-1}$ for all $t \in \{2, \ldots, T\}$ (excluding the initial fine-tuning transient at $t{=}1$). For conditions with multiple seeds, the condition is evaluated on the cross-seed mean trajectory.
62	When a constant ratio $r \geq r_{\text{crit}}$ is applied, $\Delta_t \leq 0 < \tau$ for all $t \geq 2$ and any $\tau > 0$, so the controller boost is identically zero.
63	This $\tau$-independence means the signal attenuation cannot be resolved by lowering the sensitivity threshold; the same argument extends to cumulative variants.
64	Our experiments (\S\ref{subsec:phase1}) empirically bound $0.25 < r_{\text{crit}} \leq 0.3$ over Gen~2--10 for Pythia-410M on OpenWebText.
65	
66	\paragraph{Second-Order Extension.}
67	\label{subsec:second_order}
68	A natural extension monitors the rate of change of the controller signal itself:
69	\begin{equation}
70	\label{eq:second_order}
71	\Delta^2_t = \widetilde{\Delta}_{t-1} - \widetilde{\Delta}_t
72	\end{equation}
73	where $\widetilde{\Delta}_t$ is the EMA-smoothed first-order signal ($\alpha_2{=}0.3$).
74	A sustained negative $\Delta^2_t$ indicates decelerating SLV growth, a potential precursor to stagnation even when SLV is still rising.
75	We evaluate this indicator in \S\ref{subsec:phase_diagram_exp}.
76	
77	\subsection{Collapse Trajectory Classification}
78	\label{subsec:phase_diagram}
79	
80	We define the \emph{collapse trajectory map} as the mapping from constant mixing ratio $r$ to the SLV trajectory over $T$ generations, classifying outcomes as \emph{collapse} (monotonic post-decompression decline), \emph{stable} (non-decreasing), or \emph{transitional} (non-monotonic after Gen~2).
81	We estimate $r_{\text{crit}}$ by identifying the lowest $r$ for which $\widetilde{S}_t \geq \widetilde{S}_{t-1}$ holds for all $t \in \{2, \ldots, T\}$.
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a043915d-700a-4cf6-8868-585b667ff177",
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "764c61df-6d20-4f03-b129-5893af4c0cc0",
  "sourceToolAssistantUUID": "a043915d-700a-4cf6-8868-585b667ff177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T19:42:37.165Z_

<details open><summary>🔧 Tool call — Read · `toolu_0178a6L5CY6uXgdrdBkfw3MD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "764c61df-6d20-4f03-b129-5893af4c0cc0",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPriDQoADn6qHZDdv68Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba0c03f2-cb5e-4455-b194-8ea2b9ae15a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxUoDDDSrP2he7dAUz4jtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30688,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 11 · 2026-05-25T19:42:37.170Z_

<details><summary>↩ Tool result · `toolu_0178a6L5CY6uXgdrdBkfw3MD`</summary>

```text
1	
2	\subsection{Experimental Setup}
3	\label{subsec:setup}
4	
5	We use the publicly released final Pythia-410M-deduped checkpoint \citep{biderman2023pythia} as our base model and fine-tune on a randomly sampled 50K-subset of OpenWebText (filtered to sequences with $\geq$256 non-padding tokens).
6	Starting from the pretrained checkpoint (generation~0), each subsequent generation fine-tunes on synthetic text produced by the previous generation, for a total of 10 recursive generations.
7	At each generation we compute the spectral indicators from \S\ref{subsec:spectral_metrics} on 1K held-out last-layer embeddings, paired with three downstream metrics: perplexity, HellaSwag accuracy (0-shot), and distinct-4.
8	These three metrics (language modeling capability, natural language understanding, and generation diversity) cover the primary evaluation dimensions accessible to a 410M-parameter model.
9	Training hyperparameters and compute details are in Appendix~\ref{app:training_details}.
10	
11	For the mixing comparison (\S\ref{subsec:phase1}), we evaluate three strategies:
12	(1)~\textbf{pure collapse} ($r_t{=}0$),
13	(2)~\textbf{fixed mix} ($r_t{=}0.50$), and
14	(3)~\textbf{adaptive} ($k{=}10$, Eq.~\ref{eq:controller}).
15	To construct the collapse trajectory map (\S\ref{subsec:phase_diagram_exp}), we additionally evaluate fixed mixing at $r \in \{0.2, 0.25, 0.3\}$.
16	
17	\subsection{Spectral Collapse Characterization}
18	\label{subsec:phase0}
19	
20	Table~\ref{tab:phase0} reports spectral and downstream metrics across 10 recursive generations, which reveal a three-phase structure.
21	
22	\paragraph{Phase I: Spectral Decompression (Gen~0--2).}
23	$r_{\text{eff}}$ rises from 417.55 to 496.2 (+18.8\%) and SLV from 2366.7 to 2468.0 (+4.3\%), while $\sigma_1$ drops from 1942.8 to 718.7.
24	The peak at Gen~2 is consistent across all three seeds (Figure~\ref{fig:seed_variability}; SLV coefficient of variation (CV) $< 1.3\%$ at all generations; full per-generation statistics in Appendix Table~\ref{tab:pergen_variance}).
25	However, this decompression does not indicate improved model quality: HellaSwag drops 8.0\% and distinct-4 falls 31.6\% during the same interval (Figure~\ref{fig:slv_ppl_decoupling}), and SLV computation takes ${<}\,1$\,s vs.\ ${\sim}$70\,min for benchmarks.
26	
27	\begin{figure}[t]
28	\centering
29	\includegraphics[width=\columnwidth]{figures/seed_variability.pdf}
30	\caption{Cross-seed reproducibility of SLV under pure-synthetic training ($r{=}0$). Thin lines: individual seeds (42, 43, 44); thick line: 3-seed mean; shaded band: $\pm$1 s.d. The coefficient of variation remains below 1.3\% at all generations; spectral collapse follows a deterministic trajectory.}
31	\label{fig:seed_variability}
32	\end{figure}
33	
34	\begin{figure}[t]
35	\centering
36	\includegraphics[width=\columnwidth]{figures/slv_ppl_decoupling.pdf}
37	\caption{SLV (top) and perplexity (bottom) across 10 recursive generations ($r{=}0$, 3-seed mean). In Phase~I (Gen~0--2), both metrics rise simultaneously. The SLV increase reflects distributional broadening, not model health. From Phase~III onward (Gen~4--10), the two metrics diverge: SLV declines monotonically while perplexity accelerates, which confirms that post-decompression SLV faithfully tracks structural collapse.}
38	\label{fig:slv_ppl_decoupling}
39	\end{figure}
40	
41	\paragraph{Phase II: Collapse Onset (Gen~2--4).}
42	Both $r_{\text{eff}}$ and SLV reverse after Gen~2 ($r_{\text{eff}}$: 496.2$\to$493.6, SLV: 2468$\to$2440), marking the transition from decompression to collapse while perplexity continues its monotonic rise.
43	SLV's post-peak decline is sharper than $r_{\text{eff}}$'s ($-$1.1\% vs.\ $-$0.5\% in the first post-peak generation) because SLV captures distributed contraction across all spectral directions rather than the dominant ones alone.
44	At 1B scale, this sensitivity gap widens to a timing difference: SLV peaks one generation earlier than $r_{\text{eff}}$ (see Cross-Scale Pilot below).
45	
46	\paragraph{Phase III: Accelerating Collapse (Gen~4--10).}
47	SLV contraction accelerates: the per-generation decline averages $-$31.0 during onset (Gen~2--4) vs.\ $-$37.4 during acceleration (Gen~4--10), with 78\% of the total peak-to-final decline occurring in Phase~III (Table~\ref{tab:pergen_variance}).
48	By Gen~10, $r_{\text{eff}}$ falls to 438.1 ($-$11.7\% from peak), SLV to 2181.4 ($-$11.6\% from peak), and perplexity reaches 71.0 ($+$643\%).
49	Concurrently, $\sigma_1$ traces a U-shaped trajectory: after dropping from 1942.8 to 718.7 during decompression, it rises to 874.6 by Gen~10 (Figure~\ref{fig:spectral_trajectory}).
50	This simultaneous $\sigma_1$ recovery and $r_{\text{eff}}$ decline is a geometric signature of mode collapse: representations concentrate along fewer dominant directions while the overall occupied volume shrinks.
51	
52	\paragraph{Cross-Scale Pilot.}
53	Repeating the protocol on Pythia-1B-deduped (Gen~0--3) reproduces the decompression-onset structure: SLV rises from 2835 to 2906 at Gen~1 ($+$2.5\%) before declining to 2865 at Gen~3, while $r_{\text{eff}}$ peaks one generation later at Gen~2 (580.9 vs.\ 570.8 at Gen~1).
54	This one-generation SLV lead over $r_{\text{eff}}$ (absent at 410M, where both peak simultaneously) suggests that SLV sensitivity increases with model scale.
55	Perplexity rises monotonically throughout (8.1$\to$13.4, $+$66\%)---the same downstream-spectral asymmetry observed at 410M scale.
56	Full 10-generation characterization at 1B remains future work.
57	
58	\subsection{Adaptive Mixing Comparison}
59	\label{subsec:phase1}
60	
61	We evaluate the controller retrospectively by computing its signal on pre-existing fixed-ratio trajectories rather than deploying it in a closed loop; the goal is to characterize signal attenuation, not to propose operational deployment.
62	Under pure synthetic training, SLV peaks at Gen~2 (2468) and declines monotonically; with 50\% mixing, SLV rises to 2572 at Gen~10, with only a negligible Gen~1 dip ($\Delta_1 \approx 0.0005$, well below $\tau$).
63	The adaptive controller ($k{=}10$) remains silent through all ten generations.
64	Figure~\ref{fig:controller_signal} quantifies the signal attenuation: the maximum controller signal magnitude drops from 40.4 at $r{=}0$ to 3.8 at $r{=}0.2$ and reaches exactly zero at $r \geq 0.3$. Even moderate mixing suffices to suppress the rate-based signal~\citep{scheffer2009ews}.
65	
66	\begin{figure}[t]
67	\centering
68	\includegraphics[width=0.85\columnwidth]{figures/controller_signal.pdf}
69	\caption{Maximum controller signal magnitude ($\max|\Delta\tilde{S}_t|$, $t \geq 2$) across mixing ratios. The signal drops $10\times$ from $r{=}0$ to $r{=}0.2$ and is exactly zero for $r \geq 0.3$ (``silent''), rate-based controllers are therefore ineffective.}
70	\label{fig:controller_signal}
71	\end{figure}
72	
73	Despite sustained spectral expansion at $r{=}0.5$, downstream metrics degrade: perplexity increases 58\% and distinct-4 falls to .152 (below even pure collapse), reinforcing that spectral health does not guarantee model health.
74	
75	\subsection{Alternative EWS Comparison}
76	\label{subsec:alt_ews}
77	
78	We compare SLV against seven alternative collapse indicators from three signal sources: embedding geometry (RankMe, isotropy), attention weights (stable rank, spectral norm), and output distributions (token entropy, raw perplexity, perplexity growth rate).
79	
80	Table~\ref{tab:ews_main} summarizes the comparison under pure-synthetic training ($r{=}0$); full tabular data appear in Appendix Table~\ref{tab:ews_comparison}.
81	Only SLV and RankMe~\citep{rankme2023} exhibit a decompression peak at Gen~2 followed by monotonic decline; all other indicators change monotonically from Gen~0 and cannot distinguish collapse onset from the initial fine-tuning transient.
82	SLV's signal-to-noise ratio is 2.5$\times$ that of RankMe (11.8\% vs.\ 4.7\% relative change).
83	
84	\begin{table}[t]
85	\centering
86	\small
87	\setlength{\tabcolsep}{4pt}
88	\begin{tabular}{@{}llcc@{}}
89	\toprule
90	Indicator & Direction ($r{=}0$) & Rel $\Delta$ & Rev. \\
91	\midrule
92	SLV         & Peak G2, mono.\ $\downarrow$ & 11.8\% & \checkmark \\
93	RankMe      & Peak G2, mono.\ $\downarrow$ &  4.7\% & \checkmark \\
94	Token ent.  & Mono.\ $\downarrow$           &  9.6\% & \checkmark \\
95	Stable rank & Mono.\ $\downarrow$           & 14.0\% & \checkmark \\
96	Spec.\ norm & Mono.\ $\uparrow$            &  8.0\% & \checkmark \\
97	Isotropy    & Non-mono.\ (6 rev.)           & 75\%   & \checkmark \\
98	Raw PPL     & Mono.\ $\uparrow$            & 704\%  & $\times$ \\
99	PPL growth  & ${\sim}$Mono.\ $\downarrow$   &  ---   & \checkmark \\
100	\bottomrule
101	\end{tabular}
102	\caption{Eight EWS indicators under pure-synthetic training ($r{=}0$, Pythia-410M). \textbf{Direction}: trajectory shape (Peak G$n$ = decompression peak at generation $n$; mono.\ = monotonic post-peak or throughout). \textbf{Rel $\Delta$}: total relative change. \textbf{Rev.}: whether the indicator reverses under $r{=}0.5$ mixing. Seven of eight reverse; raw PPL is the sole exception. Full data in Appendix Table~\ref{tab:ews_comparison}.}
103	\label{tab:ews_main}
104	\end{table}
105	Seven of eight indicators reverse direction under mixing (Table~\ref{tab:ews_main}, last column); raw perplexity is the sole exception.
106	This near-universality confirms that signal attenuation is not specific to SLV: any rate-based controller will fall silent when mixing exceeds $r_{\text{crit}}$.
107	SLV is the only indicator that combines decompression-phase sensitivity, post-peak monotonicity, and sub-second computation cost; it shares a metric foundation with SIGMA's $\log\det G$ ($= 2 \times \text{SLV}$; \S\ref{sec:related}).
108	Raw perplexity is a stronger unconditional monitor (monotonic from Gen~0, no decompression mislead) but does not reveal the spectral geometry of collapse; SLV and PPL are complementary.
109	
110	\subsection{Collapse Trajectory Classification}
111	\label{subsec:phase_diagram_exp}
112	
113	We now map SLV trajectories across mixing ratios to construct the collapse trajectory map defined in \S\ref{subsec:phase_diagram}.
114	Figure~\ref{fig:phase_diagram} plots SLV across 10 recursive generations for five mixing ratios; three qualitatively distinct trajectory types emerge:
115	
116	\begin{figure}[t]
117	\centering
118	\includegraphics[width=0.92\columnwidth]{figures/phase_diagram.pdf}
119	\caption{SLV trajectories across mixing ratios (Pythia-410M; $r{=}0$, $r{=}0.2$, $r{=}0.25$, $r{=}0.3$: 3-seed mean, solid lines; $r{=}0.5$: 2-seed mean, dashed line). Type~I ($r{=}0$): decompression then monotonic collapse. Type~II ($r{=}0.2$, $r{=}0.25$): transient dip followed by recovery. Type~III ($r{=}0.3$, $r{=}0.5$): monotonic expansion from Gen~2 onward. The shaded band marks the critical threshold $r_{\text{crit}} \in (0.25, 0.3]$. The dashed horizontal line indicates the Gen~0 baseline.}
120	\label{fig:phase_diagram}
121	\end{figure}
122	
123	\paragraph{Type~I: Pure Collapse ($r{=}0$).}
124	SLV exhibits large decompression ($+$96 points at Gen~1, peaking at Gen~2) followed by accelerating contraction (\S\ref{subsec:phase0}).
125	
126	\paragraph{Type~II: Near-critical Mixing ($r{=}0.2$, $r{=}0.25$).}
127	At $r{=}0.2$, SLV dips $-7.3$ points at Gen~2 before recovering to 2467.2 at Gen~10 ($+4.3\%$ above baseline; full per-generation data in Appendix Table~\ref{tab:pergen_variance_r02}).
128	The EMA-smoothed SLV violates non-decreasing at Gen~2, placing $r{=}0.2$ below $r_{\text{crit}}$, yet the smoothed signal ($\max \Delta_t = 0.0016$, below $\tau{=}0.002$) fails to trigger the controller.
129	At $r{=}0.25$, the same pattern holds with a weaker dip ($-2.1$) and ${\sim}3\times$ weaker signal.
130	As Figure~\ref{fig:rankme_trajectories} shows, $r_{\text{eff}}$ rises monotonically for all $r \geq 0.2$, yielding only a 2-type classification (collapse vs.\ non-collapse); SLV's transient dip uniquely identifies the transitional regime.
131	
132	\begin{figure}[t]
133	\centering
134	\includegraphics[width=0.92\columnwidth]{figures/rankme_trajectories.pdf}
135	\caption{Effective rank ($r_{\mathrm{eff}}$) trajectories across mixing ratios. Unlike SLV (Figure~\ref{fig:phase_diagram}), $r_{\mathrm{eff}}$ rises monotonically for all $r \geq 0.2$, providing only a 2-type classification and failing to identify the Type~II transitional regime.}
136	\label{fig:rankme_trajectories}
137	\end{figure}
138	
139	\paragraph{Type~III: Super-critical Mixing ($r \geq 0.3$).}
140	SLV rises monotonically from Gen~2 onward.
141	At $r{=}0.3$, SLV reaches 2508.2 at Gen~10 ($+$6.0\% above baseline); at $r{=}0.5$, 2572 ($+$8.7\%).
142	The critical threshold is robust to EMA smoothing ($\alpha \in \{0.3, 0.5, 0.7\}$ all yield $r_{\text{crit}} \in (0.25, 0.3]$; Appendix Table~\ref{tab:alpha_robustness}), and the maximum SLV departure below baseline (multi-seed mean) shrinks continuously with $r$ ($-7.3$ at $r{=}0.2$, $-3.3$ at $r{=}0.25$, $-1.5$ at $r{=}0.3$), consistent with a continuous crossover.
143	$r_{\text{crit}}$ thus marks a transition in trajectory shape, not in final outcome: Type~II trajectories recover spectrally but exhibit an initial contraction transient that Type~III trajectories lack.
144	
145	\paragraph{Output Diversity Divergence.}
146	D-4 does not increase monotonically with $r$: it remains highest around $r \in \{0.2, 0.25\}$ (mean $.324$--$.342$, with high cross-seed variance s.d.\ $\approx 0.17$) before dropping to .152 at $r{=}0.5$: spectral expansion does not guarantee diversity.
147	D-4 also shows substantially higher cross-seed variance than SLV (CV $= 3.9\%$ vs.\ $0.12\%$ at $r{=}0.25$); the two metrics capture orthogonal aspects of model behavior.
148	
149	Table~\ref{tab:phase_summary} consolidates the final-generation metrics across all five mixing ratios.
150	
151	\paragraph{Practical Implications.}
152	Neither second-order acceleration ($\Delta^2_t$, Eq.~\ref{eq:second_order}) nor level-based triggers resolve the attenuation problem: $\Delta^2_t$ is negative in late generations regardless of $r$, and level-based triggers fail under Type~III.
153	The trajectory map provides a direct prescription: setting $r > 0.3$ prevents spectral collapse without per-generation monitoring.
154	
155	\begin{table}[t]
156	\centering
157	\small
158	\setlength{\tabcolsep}{4pt}
159	\begin{tabular}{@{}cccccccc@{}}
160	\toprule
161	$r$ & Type & SLV & $r_{\text{eff}}$ & PPL & D-4 & $\max\Delta_t$ & Gen. \\
162	\midrule
163	0    & I   & 2181.4 & 438.1 & 71.0\phantom{0} & .324 & ---   & 10 \\
164	0.20 & II  & 2467.2 & 508.1 & 13.54 & .324 & .0016 & 10 \\
165	0.25 & II  & 2488.1 & 513.8 & 13.41 & .342 & .0005 & 10 \\
166	0.30 & III & 2508.2 & 521.1 & 13.34 & .295 & 0     & 10 \\
167	0.50 & III & 2571.6 & 553.5 & 15.11 & .152 & 0     & 10 \\
168	\bottomrule
169	\end{tabular}
170	\caption{Final-generation spectral and downstream metrics across mixing ratios (all runs to Gen~10). PPL = perplexity, D-4 = distinct-4. $\max\Delta_t$ computed for $t \geq 2$, excluding the initial fine-tuning transient. Type classification follows \S\ref{subsec:phase_diagram}. $r{=}0$ reports the mean of three seeds (42, 43, 44); $r{=}0.3$ the mean of three seeds (42, 43, 44); $r{=}0.2$ the mean of three seeds (42, 43, 44); $r{=}0.5$ the mean of two seeds (42, 43); $r{=}0.25$ the mean of three seeds (42, 43, 44). D-4 exhibits high cross-seed variance at $r{=}0$ (s.d.\ $= 0.15$) and $r{=}0.3$ (s.d.\ $= 0.155$).}
171	\label{tab:phase_summary}
172	\end{table}
173	
174	\subsection{Cross-Architecture Validation}
175	\label{subsec:cross_arch}
176	
177	To test whether the three-phase trajectory generalizes beyond Pythia, we repeat the recursive pipeline on GPT-2-medium~\citep{radford2019language} (355M parameters, different pretraining corpus and tokenizer) under four conditions: pure synthetic ($r{=}0$, 9 generations), intermediate mixing ($r{=}0.25$ and $r{=}0.3$, 3 generations each), and a real-data control ($r{=}1.0$, 3 generations).
178	
179	Under pure synthetic training, GPT-2-medium reproduces the three-phase pattern (Table~\ref{tab:cross_arch}): SLV peaks at Gen~2 (924, $+$34.1\% from baseline) and declines to 415 by Gen~9 ($-$55.1\% from peak), while perplexity rises from 15.5 to 329 ($+$2028\%).
180	The $\sigma_1$ trajectory follows the same U-shape (6598$\to$1191 during decompression, rising to ${\sim}$1570 by Gen~9); dominant-direction reconcentration under falling effective rank is architecture-independent.
181	The collapse magnitude is substantially larger than Pythia's ($-$55.1\% vs.\ $-$11.6\% SLV decline), consistent with GPT-2-medium's more anisotropic initial spectrum ($r_{\text{eff}}{=}23$ vs.\ Pythia's 418).
182	
183	The real-data control ($r{=}1.0$) shows monotonic expansion with perplexity \emph{decreasing} ($-$27.4\%), which confirms that collapse is specific to recursive synthetic training.
184	
185	At intermediate ratios ($r{=}0.25$, $r{=}0.3$), both conditions reproduce the decompression phase (Gen~0$\to$1: SLV $+$7.5--8.5\%, $r_{\text{eff}}$ from 23 to 136--142, $\sigma_1$ $-$80--82\%) and stabilize through Gen~3, with EMA-smoothed SLV monotonically non-decreasing.
186	At $r{=}0.3$ this matches Pythia's Type~III classification.
187	At $r{=}0.25$, the three-generation window does not resolve the Type~II/III distinction, since Pythia's characteristic EMA dip appears only at Gen~5+; the trajectory is consistent with the Pythia-410M phase boundary but does not independently confirm $r_{\text{crit}}$ for this architecture.
188	
189	\begin{table}[t]
190	\centering
191	\small
192	\setlength{\tabcolsep}{4pt}
193	\begin{tabular}{@{}cccccc@{}}
194	\toprule
195	$r$ & Type & SLV$_0$ & SLV$_{\text{end}}$ & $\Delta$SLV & Match \\
196	\midrule
197	0    & I    & 689  & 415\,(G9)  & $-$39.8\% & \checkmark \\
198	0.25 & ---  & 689  & 738\,(G3)  & $+$7.0\%  & $\dagger$ \\
199	0.30 & III  & 689  & 737\,(G3)  & $+$6.9\%  & \checkmark \\
200	1.0  & Ctrl & 689  & 813\,(G3)  & $+$17.9\% & \checkmark \\
201	\bottomrule
202	\end{tabular}
203	\caption{Cross-architecture validation on GPT-2-medium (355M, seed~42). \textbf{Match}: whether the trajectory type matches the corresponding Pythia-410M classification. $\dagger$\,Three-generation horizon does not resolve the Type~II/III distinction at this ratio.}
204	\label{tab:cross_arch}
205	\end{table}
206	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba0c03f2-cb5e-4455-b194-8ea2b9ae15a1",
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "e31febb0-e739-4bd6-a1bb-fbd300ebb005",
  "sourceToolAssistantUUID": "ba0c03f2-cb5e-4455-b194-8ea2b9ae15a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T19:42:37.663Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PgGiU7YQxDzjYYNy3U5k3q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e31febb0-e739-4bd6-a1bb-fbd300ebb005",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPriDQoADn6qHZDdv68Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18cfbd73-a618-4178-89e9-7f8e1170b4e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxUoDDDSrP2he7dAUz4jtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30688,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 13 · 2026-05-25T19:42:37.668Z_

<details><summary>↩ Tool result · `toolu_01PgGiU7YQxDzjYYNy3U5k3q`</summary>

```text
1	
2	The spectral decompression phase reflects fine-tuning's redistribution of variance: early recursive training compresses the dominant singular direction while inflating subordinate ones, an effect analogous to isotropy regularization~\citep{ethayarajh2019contextual} reversed by recursive amplification.
3	That downstream performance degrades during this expansion confirms these indicators are collapse detectors, not quality measures.
4	SLV and perplexity are complementary: perplexity rises monotonically from Gen~0; SLV provides mechanistic diagnosis by distinguishing volume contraction from distributional broadening.
5	
6	A key finding is the prevention--detectability tradeoff: real-data mixing reverses the spectral trajectory entirely, and the controller signal drops $10\times$ from $r{=}0$ to $r{=}0.2$ and vanishes at $r \geq 0.3$; no regime exists where prevention and detection coexist.
7	Our analysis identifies SLV as a cheap spectral indicator, reveals a reproducible three-phase collapse trajectory, and exposes the signal attenuation that limits reactive controllers.
8	The trajectory map localizes $r_{\text{crit}} \in (0.25, 0.3]$; setting $r > r_{\text{crit}}$ prevents collapse without per-generation monitoring, with cross-architecture support from GPT-2-medium and preliminary scale evidence from Pythia-1B.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18cfbd73-a618-4178-89e9-7f8e1170b4e4",
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "e3a466cf-dc42-48ff-beca-93f053e81fcc",
  "sourceToolAssistantUUID": "18cfbd73-a618-4178-89e9-7f8e1170b4e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T19:42:38.134Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JNCQvW5XSmvBTQbNUHz1b1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3a466cf-dc42-48ff-beca-93f053e81fcc",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPriDQoADn6qHZDdv68Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d7e5cca-2be1-43f7-9452-7959e1e2b34d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxUoDDDSrP2he7dAUz4jtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30688,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 15 · 2026-05-25T19:42:38.138Z_

<details><summary>↩ Tool result · `toolu_01JNCQvW5XSmvBTQbNUHz1b1`</summary>

```text
1	\section*{Limitations}
2	
3	\paragraph{Scale and Scope.}
4	We validate at two model scales (Pythia-410M and a 1B pilot through Gen~3) with all spectral metrics computed from last-layer embeddings only; intermediate layers may exhibit different dynamics.
5	The 1B pilot confirms the decompression peak but is insufficient to characterize full acceleration or estimate $r_{\text{crit}}$ at that scale.
6	All fine-tuning uses a single domain (OpenWebText, English web text); spectral collapse dynamics may differ for code, multilingual, or domain-specific corpora.
7	
8	\paragraph{Temporal Horizon.}
9	Ten recursive generations may be shorter than production pipelines.
10	Type~II (transitional) trajectories may eventually revert to collapse at longer horizons, which would shift $r_{\text{crit}}$ upward.
11	The proportional controller uses a single gain $k$ without integral or derivative terms; a more sophisticated design might partially mitigate signal attenuation.
12	
13	\paragraph{Generalization.}
14	Signal attenuation may extend to implicit-loop settings where web corpora contain model-generated content, but validating this requires controlled experiments with web-scale data.
15	Our use of AI coding and writing assistants is disclosed in Appendix~\ref{app:ai-assistants}.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d7e5cca-2be1-43f7-9452-7959e1e2b34d",
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "f9bcfe89-1e17-4bbe-9be6-d151b10094a7",
  "sourceToolAssistantUUID": "4d7e5cca-2be1-43f7-9452-7959e1e2b34d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T19:42:38.604Z_

<details open><summary>🔧 Tool call — Read · `toolu_018qvAyXbK8bh2Nai9H3UuH4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9bcfe89-1e17-4bbe-9be6-d151b10094a7",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPriDQoADn6qHZDdv68Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "816807ff-1a71-412e-afd2-fd9665189631",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxUoDDDSrP2he7dAUz4jtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30688,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 17 · 2026-05-25T19:42:38.610Z_

<details><summary>↩ Tool result · `toolu_018qvAyXbK8bh2Nai9H3UuH4`</summary>

```text
1	
2	\section{Alternative EWS Indicator Details}
3	\label{app:ews_details}
4	
5	Table~\ref{tab:ews_comparison} provides full tabular data for the eight alternative early warning indicators compared in \S\ref{subsec:alt_ews}.
6	
7	\begin{table}[H]
8	\centering
9	\small
10	\setlength{\tabcolsep}{4pt}
11	\begin{tabular}{@{}llcccc@{}}
12	\toprule
13	Indicator & Source & Peak & Mono. & Rel $\Delta$ & Rev. \\
14	\midrule
15	SLV         & emb-SVD   & Gen 2 & \checkmark & 11.8\% & \checkmark \\
16	RankMe      & emb-SVD   & Gen 2 & \checkmark &  4.7\% & \checkmark \\
17	Token ent.  & logit     & ---   & \checkmark &  9.6\% & \checkmark \\
18	Stable rank & attn wt.  & ---   & \checkmark & 14.0\% & \checkmark \\
19	Spec.\ norm & attn wt.  & ---   & \checkmark &  8.0\% & \checkmark \\
20	Isotropy    & emb       & ---   & $\times$\,(6) & 75\%   & \checkmark \\
21	Raw PPL     & eval      & ---   & \checkmark & 704\%  & $\times$ \\
22	PPL growth  & ppl       & ---   & $\sim$\,(1) &  ---   & \checkmark \\
23	\bottomrule
24	\end{tabular}
25	\caption{Alternative early warning indicators under pure-synthetic training ($r{=}0$, seed 42, Pythia-410M, 10 gen). \textbf{Peak}: generation at which the indicator reverses (--- = monotonic from Gen~0). \textbf{Mono.}: post-peak monotonicity (\checkmark\ = yes; number = violations). \textbf{Rel $\Delta$}: magnitude of total relative change; for peaked indicators (SLV, RankMe), computed as $|v_{10} - v_{\text{peak}}|/|v_{\text{peak}}|$; for monotonic indicators, $|v_{10} - v_0|/|v_0|$. \textbf{Rev.}: direction reversal under $r{=}0.5$ mixing (\checkmark\ = reversed). Note: Raw PPL Rel~$\Delta$ is 704\% for seed~42; the main text reports 643\% (3-seed mean).}
26	\label{tab:ews_comparison}
27	\end{table}
28	
29	\section{Per-Generation Cross-Seed Variance}
30	\label{app:pergen_variance}
31	
32	Table~\ref{tab:pergen_variance} reports all six metrics at every generation under pure-synthetic training ($r{=}0$), with mean and sample standard deviation across three seeds (42, 43, 44).
33	Spectral metrics ($r_{\text{eff}}$, SLV, $\sigma_1$) exhibit low cross-seed variance throughout the trajectory (SLV coefficient of variation $< 1.3\%$ at all generations); spectral collapse follows a deterministic geometric trajectory.
34	In contrast, D-4 variance increases sharply after Gen~5, reaching a coefficient of variation of 46\% at Gen~10, consistent with the stochastic nature of n-gram diversity under progressive mode collapse.
35	
36	\begin{table*}[!htb]
37	\centering
38	\small
39	\caption{Per-generation metrics under pure-synthetic training ($r{=}0$, Pythia-410M, mean$_{\pm\text{s.d.}}$ across seeds 42, 43, 44). Gen~0 shares a single pretrained checkpoint; D-4 variance at Gen~0 reflects generation sampling. Bold marks the spectral peak.}
40	\label{tab:pergen_variance}
41	\setlength{\tabcolsep}{4pt}
42	\begin{tabular}{@{}ccccccc@{}}
43	\toprule
44	Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
45	\midrule
46	 0 & 417.5$_{\pm0.0}$ & 2366.7$_{\pm0.0}$ & 9.55$_{\pm0.00}$ & .413$_{\pm.000}$ & .738$_{\pm.006}$ & 1942.8$_{\pm0.0}$ \\
47	 1 & 491.1$_{\pm0.6}$ & 2462.3$_{\pm2.7}$ & 11.37$_{\pm0.01}$ & .390$_{\pm.001}$ & .609$_{\pm.014}$ & 808.9$_{\pm5.4}$ \\
48	 2 & \textbf{496.2}$_{\pm0.3}$ & \textbf{2468.0}$_{\pm1.7}$ & 13.56$_{\pm0.02}$ & .380$_{\pm.004}$ & .505$_{\pm.011}$ & 718.7$_{\pm7.0}$ \\
49	 3 & 493.6$_{\pm0.4}$ & 2440.4$_{\pm2.0}$ & 16.23$_{\pm0.02}$ & .367$_{\pm.005}$ & .465$_{\pm.033}$ & 708.7$_{\pm7.5}$ \\
50	 4 & 487.8$_{\pm1.9}$ & 2406.0$_{\pm2.0}$ & 19.90$_{\pm0.09}$ & .354$_{\pm.003}$ & .419$_{\pm.047}$ & 722.9$_{\pm6.9}$ \\
51	 5 & 479.8$_{\pm0.5}$ & 2366.0$_{\pm3.8}$ & 24.50$_{\pm0.17}$ & .341$_{\pm.003}$ & .412$_{\pm.053}$ & 749.2$_{\pm7.1}$ \\
52	 6 & 472.4$_{\pm0.6}$ & 2326.1$_{\pm8.6}$ & 30.40$_{\pm0.45}$ & .329$_{\pm.004}$ & .402$_{\pm.067}$ & 764.6$_{\pm5.7}$ \\
53	 7 & 464.1$_{\pm0.2}$ & 2293.2$_{\pm10.2}$ & 37.82$_{\pm0.94}$ & .319$_{\pm.000}$ & .375$_{\pm.082}$ & 788.4$_{\pm4.0}$ \\
54	 8 & 455.8$_{\pm1.1}$ & 2246.1$_{\pm7.4}$ & 46.90$_{\pm2.41}$ & .311$_{\pm.005}$ & .337$_{\pm.137}$ & 806.4$_{\pm8.0}$ \\
55	 9 & 446.6$_{\pm2.1}$ & 2210.4$_{\pm23.1}$ & 58.56$_{\pm4.52}$ & .301$_{\pm.003}$ & .316$_{\pm.148}$ & 841.1$_{\pm23.6}$ \\
56	10 & 438.1$_{\pm4.8}$ & 2181.4$_{\pm28.3}$ & 70.99$_{\pm5.56}$ & .296$_{\pm.006}$ & .324$_{\pm.150}$ & 874.6$_{\pm44.2}$ \\
57	\bottomrule
58	\end{tabular}
59	\end{table*}
60	
61	Table~\ref{tab:pergen_variance_r02} provides the same breakdown under transitional mixing ($r{=}0.2$), where D-4 variance is the dominant source of cross-seed disagreement.
62	
63	\begin{table*}[!htb]
64	\centering
65	\small
66	\caption{Per-generation metrics under transitional mixing ($r{=}0.2$, Pythia-410M, mean$_{\pm\text{s.d.}}$ across seeds 42, 43, 44). Gen~0 shares a single pretrained checkpoint; D-4 variance at Gen~0 reflects generation sampling. HellaSwag was not evaluated for mixing experiments.}
67	\label{tab:pergen_variance_r02}
68	\setlength{\tabcolsep}{5pt}
69	\begin{tabular}{@{}cccccc@{}}
70	\toprule
71	Gen & $r_{\text{eff}}$ & SLV & PPL & D-4 & $\sigma_1$ \\
72	\midrule
73	 0 & 417.5$_{\pm0.0}$ & 2366.7$_{\pm0.0}$ & 9.55$_{\pm0.00}$ & .738$_{\pm.006}$ & 1942.8$_{\pm0.0}$ \\
74	 1 & 476.2$_{\pm0.8}$ & 2367.4$_{\pm2.1}$ & 10.28$_{\pm0.00}$ & .671$_{\pm.015}$ & 961.8$_{\pm1.1}$ \\
75	 2 & 481.7$_{\pm1.4}$ & 2359.4$_{\pm1.5}$ & 10.74$_{\pm0.01}$ & .519$_{\pm.037}$ & 879.2$_{\pm10.3}$ \\
76	 3 & 486.7$_{\pm0.3}$ & 2364.6$_{\pm1.8}$ & 11.14$_{\pm0.01}$ & .471$_{\pm.006}$ & 811.9$_{\pm9.6}$ \\
77	 4 & 489.6$_{\pm0.6}$ & 2377.9$_{\pm1.2}$ & 11.49$_{\pm0.00}$ & .429$_{\pm.026}$ & 779.2$_{\pm9.2}$ \\
78	 5 & 492.6$_{\pm0.5}$ & 2396.8$_{\pm1.8}$ & 11.83$_{\pm0.00}$ & .420$_{\pm.037}$ & 748.8$_{\pm9.3}$ \\
79	 6 & 495.5$_{\pm1.2}$ & 2417.7$_{\pm10.5}$ & 12.17$_{\pm0.02}$ & .413$_{\pm.070}$ & 749.7$_{\pm22.5}$ \\
80	 7 & 496.7$_{\pm1.2}$ & 2429.0$_{\pm6.4}$ & 12.49$_{\pm0.05}$ & .379$_{\pm.096}$ & 750.9$_{\pm30.6}$ \\
81	 8 & 499.8$_{\pm2.3}$ & 2442.4$_{\pm10.3}$ & 12.82$_{\pm0.12}$ & .365$_{\pm.119}$ & 753.9$_{\pm23.4}$ \\
82	 9 & 503.8$_{\pm1.2}$ & 2456.0$_{\pm6.3}$ & 13.18$_{\pm0.18}$ & .349$_{\pm.143}$ & 738.1$_{\pm37.6}$ \\
83	10 & 508.1$_{\pm2.8}$ & 2467.2$_{\pm12.0}$ & 13.54$_{\pm0.25}$ & .324$_{\pm.171}$ & 722.7$_{\pm26.6}$ \\
84	\bottomrule
85	\end{tabular}
86	\end{table*}
87	
88	\section{Controller Signal Sensitivity to EMA Smoothing Parameter}
89	\label{app:alpha_robustness}
90	
91	\begin{table}[H]
92	\centering
93	\small
94	\setlength{\tabcolsep}{5pt}
95	\begin{tabular}{@{}cccccc@{}}
96	\toprule
97	$\alpha$ & $r{=}0$ & $r{=}0.2$ & $r{=}0.25$ & $r{=}0.3$ & $r{=}0.5$ \\
98	\midrule
99	0.3 & .0141 & .0009 & .0003 & 0 & 0 \\
100	0.5 & .0171 & .0016 & .0005 & 0 & 0 \\
101	0.7 & .0183 & .0023 & .0005 & 0 & 0 \\
102	\bottomrule
103	\end{tabular}
104	\caption{Normalized maximum controller signal magnitude ($\max|\Delta\tilde{S}_t| / \tilde{S}_t$, $t \geq 2$) across mixing ratios and EMA smoothing parameters. The critical threshold $r_{\text{crit}} \in (0.25, 0.3]$ is invariant to $\alpha$: signal is exactly zero for $r \geq 0.3$ at all three smoothing values, the phase boundary is a structural property of the trajectory rather than an artifact of smoothing.}
105	\label{tab:alpha_robustness}
106	\end{table}
107	
108	\section{Training and Compute Details}
109	\label{app:training_details}
110	
111	Fine-tuning uses AdamW (lr $5 \times 10^{-5}$, weight decay 0.01, linear warmup 5\%, effective batch size 32) for one epoch per generation, with gradient clipping at max norm 1.0.
112	Synthetic text is generated with temperature 1.0, top-$k{=}50$, max length 512.
113	All experiments run on NVIDIA RTX PRO 6000 GPUs (96\,GB); each 10-generation pipeline requires 15--26 single-GPU hours depending on the mixing ratio, totaling approximately 220 GPU-hours across all reported experiments.
114	
115	\section{Use of AI Assistants}
116	\label{app:ai-assistants}
117	
118	We used Claude (Anthropic) as an AI coding and writing assistant
119	throughout this work. Specifically:
120	\begin{itemize}
121	    \item \textbf{Code:} drafting experiment scripts, data-processing
122	    pipelines, and analysis utilities; debugging and refactoring.
123	    \item \textbf{Writing:} drafting and revising paper sections,
124	    polishing prose, and reformatting \LaTeX{}.
125	    \item \textbf{Literature:} summarizing related papers to inform
126	    the related-work section.
127	\end{itemize}
128	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "816807ff-1a71-412e-afd2-fd9665189631",
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "023e1d14-42ae-46d2-b141-0c4ab6010ebb",
  "sourceToolAssistantUUID": "816807ff-1a71-412e-afd2-fd9665189631",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T19:42:38.953Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L2McUNZfYNPmwFs8wTpHfQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "023e1d14-42ae-46d2-b141-0c4ab6010ebb",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPriDQoADn6qHZDdv68Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2836a9d2-7ed1-40d5-86dc-a702601779c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxUoDDDSrP2he7dAUz4jtJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30688,
      "cache_read_input_tokens": 0,
      "output_tokens": 608,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 30688
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 608,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 30688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 30688,
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

_source line 19 · 2026-05-25T19:42:38.959Z_

<details><summary>↩ Tool result · `toolu_01L2McUNZfYNPmwFs8wTpHfQ`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	\usepackage{float}
18	
19	
20	\title{Spectral Early Warning Signals for Model Collapse in Recursive Synthetic Training}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\section{Introduction}
32	\label{sec:intro}
33	\input{sections/introduction}
34	
35	\section{Related Work}
36	\label{sec:related}
37	\input{sections/related_work}
38	
39	\section{Method}
40	\label{sec:method}
41	\input{sections/method}
42	
43	\section{Experiments}
44	\label{sec:experiments}
45	\input{sections/experiments}
46	
47	\section{Discussion and Conclusion}
48	\label{sec:conclusion}
49	\input{sections/conclusion}
50	
51	\input{sections/limitations}
52	
53	\bibliography{references}
54	
55	\appendix
56	\input{sections/appendix}
57	
58	\end{document}
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2836a9d2-7ed1-40d5-86dc-a702601779c6",
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "6d82922c-eea8-449e-b271-ea76a42228cf",
  "sourceToolAssistantUUID": "2836a9d2-7ed1-40d5-86dc-a702601779c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-25T19:42:44.041Z_

Now let me also check if there's a related_work.tex file I should read.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d82922c-eea8-449e-b271-ea76a42228cf",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPrihsKN6Lr984gZc6Hp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "453c03fa-1a04-4635-b1bb-fe7ea8cca2d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4okFx3a3Jp3qMCpe87ZEF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18166,
      "cache_read_input_tokens": 30688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18166,
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

_source line 21 · 2026-05-25T19:42:45.469Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018U5ecQUU9hhnEKWW7qf8cv`</summary>

```json
{
  "pattern": "**/paper/sections/related_work.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "453c03fa-1a04-4635-b1bb-fe7ea8cca2d5",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPrihsKN6Lr984gZc6Hp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "615f28de-4b0d-4ffa-8ce9-f9065c02bcc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4okFx3a3Jp3qMCpe87ZEF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18166,
      "cache_read_input_tokens": 30688,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 30688,
          "cache_creation_input_tokens": 18166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18166,
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

_source line 22 · 2026-05-25T19:42:45.495Z_

<details><summary>↩ Tool result · `toolu_018U5ecQUU9hhnEKWW7qf8cv`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "615f28de-4b0d-4ffa-8ce9-f9065c02bcc0",
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "88e4dc28-3cca-42ad-b02d-6029a40ebe50",
  "sourceToolAssistantUUID": "615f28de-4b0d-4ffa-8ce9-f9065c02bcc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T19:42:48.685Z_

<details open><summary>🔧 Tool call — Read · `toolu_011Pt7xEmjRjKGxo6uHWreJU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88e4dc28-3cca-42ad-b02d-6029a40ebe50",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPrjBpaDx4fk6qVt7Shh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7ec3804-50cb-4432-8f02-e102d587c61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3qWXQqEZreBTCter7nhsL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 177,
      "cache_read_input_tokens": 48854,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 177
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 48854,
          "cache_creation_input_tokens": 177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 177,
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

_source line 24 · 2026-05-25T19:42:48.695Z_

<details><summary>↩ Tool result · `toolu_011Pt7xEmjRjKGxo6uHWreJU`</summary>

```text
1	\begin{figure}[t]
2	\centering
3	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
4	\caption{Experimental pipeline. Each generation fine-tunes on synthetic text mixed with real data at ratio $r_t$. Spectral monitoring extracts last-layer embeddings from held-out data, computes SVD, and derives SLV, $r_{\text{eff}}$, and $\sigma_1$. A proportional controller (dashed) can adjust $r_{t+1}$ based on the SLV rate of change. The three phases (decompression (I), onset (II), and acceleration (III)) are annotated along the generation axis.}
5	\label{fig:pipeline}
6	\end{figure}
7	
8	\paragraph{Model Collapse.}
9	\citet{shumailov2024collapse} showed that recursive training on model-generated data progressively erodes distributional tails (\emph{model collapse}).
10	Scaling laws predict tail erosion as a function of recursive depth~\citep{dohmatob2024tails, dohmatob2024demystified, seddik2024synthetic}; the self-consuming loop accelerates collapse even under data accumulation~\citep{alemohammad2024mad}, with as little as 1\% synthetic contamination sufficing~\citep{dohmatob2025strong}, though preserving all prior data can delay it~\citep{gerstgrasser2024inevitable}; mitigations include self-verification~\citep{fu2025selfverification} and weak non-synthetic data~\citep{amin2025escaping}.
11	We complement these output-based diagnoses by tracking collapse through the spectral geometry of internal representations.
12	
13	\paragraph{Spectral Analysis of Representations.}
14	Random matrix theory reveals implicit regularization in neural network eigenspectra~\citep{martin2021implicit}; effective rank~\citep{roy2007effectiverank} and RankMe~\citep{rankme2023} quantify representational dimensionality.
15	\citet{he2025spectral} linked spectral collapse to plasticity loss in continual learning, and \citet{naderi2025mindgap} identified rank collapse in attention matrices.
16	Most directly relevant, \citet{gu2026sigma} proposed SIGMA, tracking singular-value distributions during recursive training on OPT-125M over three generations.
17	Our SLV equals half of SIGMA's $\log\det G$; we extend SIGMA in \emph{scale} (Pythia-410M/1B, 3--8$\times$ larger), \emph{temporal depth} (10 vs.\ 3 generations), and \emph{methodology} (SLV-based mixing control).
18	Table~\ref{tab:related_comparison} summarizes the positioning.
19	
20	\paragraph{Early Warning Signals and Critical Transitions.}
21	EWS for critical transitions originate in ecology, where rising autocorrelation and variance precede regime shifts~\citep{scheffer2009ews, scheffer2012anticipating}, with methods from statistical tests~\citep{dakos2012methods} to deep learning~\citep{bury2021deeplearning}.
22	A central tension is that stabilization interventions suppress the precursors they rely on~\citep{scheffer2009ews}; we encounter a stronger form where real-data mixing reverses the spectral trajectory entirely (\S\ref{subsec:controller}).
23	
24	\paragraph{Data Mixing for LLM Training.}
25	Data composition significantly affects LM quality~\citep{longpre2024pretrainer, muennighoff2023scaling}, and several methods optimize domain mixtures~\citep{xie2023doremi, ye2025mixinglaws, chen2025aioli}, but evaluate mixing through loss or benchmarks.
26	Our work reveals that real-vs-synthetic mixing reshapes the spectral geometry of representations, producing a trajectory map that loss-based metrics do not capture.
27	
28	\begin{table}[t]
29	\centering
30	\small
31	\setlength{\tabcolsep}{3pt}
32	\begin{tabular}{@{}lccc@{}}
33	\toprule
34	& \textbf{SIGMA} & \textbf{He+ '25} & \textbf{This work} \\
35	\midrule
36	Setting & Recursive & Continual & Recursive \\
37	Scale & 125M & Various & 355M--1B \\
38	Generations & 3 & --- & 10 \\
39	Spectral metric & $\log\det G$ & spec.\ norm & SLV \\
40	Phase typology & --- & --- & \checkmark \\
41	Mixing / $r_{\text{crit}}$ & --- & --- & \checkmark \\
42	Controller & --- & --- & \checkmark \\
43	\bottomrule
44	\end{tabular}
45	\caption{Positioning relative to recent spectral-collapse studies. SLV $\equiv \tfrac{1}{2}\log\det G$. SIGMA: \citet{gu2026sigma}; He+: \citet{he2025spectral}.}
46	\label{tab:related_comparison}
47	\end{table}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7ec3804-50cb-4432-8f02-e102d587c61d",
  "isSidechain": true,
  "promptId": "2c23918d-3177-4464-a193-e69a9ad36123",
  "agentId": "a0f694476b0992be3",
  "type": "user",
  "uuid": "49f46938-5881-4559-9907-a99146ba3af9",
  "sourceToolAssistantUUID": "c7ec3804-50cb-4432-8f02-e102d587c61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-25T19:47:16.431Z_

Now I have all the data. Let me compile the comprehensive table.

Here is the exhaustive extraction of every numerical value across all `.tex` files:

---

## abstract.tex

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| abstract.tex:2 | 10 | "tracking spectral properties across 10 recursive generations" | experiment_config | NO |
| abstract.tex:2 | 410M | "Pythia-410M" | experiment_config | NO |
| abstract.tex:3 | 0--2 | "generations 0--2" | other | NO |
| abstract.tex:3 | 3.3 | "HellaSwag drops 3.3 percentage points" | claim | YES |
| abstract.tex:3 | 2--4 | "generations 2--4" | other | NO |
| abstract.tex:3 | 4--10 | "generations 4--10" | other | NO |
| abstract.tex:4 | 8 | "Of eight candidate indicators" | claim | YES |
| abstract.tex:4 | 1 | "requires one forward pass" | claim | NO |
| abstract.tex:4 | 1 | "${<}\,1$\,s" (less than 1 second) | claim | YES |
| abstract.tex:5 | 5 | "five levels" | experiment_config | YES |
| abstract.tex:5 | 0.25 | "$r_{\text{crit}} \in (0.25, 0.3]$" | claim | YES |
| abstract.tex:5 | 0.3 | "$r_{\text{crit}} \in (0.25, 0.3]$" | claim | YES |
| abstract.tex:8 | 355M | "GPT-2-medium (355M)" | experiment_config | NO |

## introduction.tex

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| introduction.tex:12 | 125M | "OPT-125M" | other | NO |
| introduction.tex:13 | 4 | "Four gaps remain open" | other | NO |
| introduction.tex:19 | 10 | "across 10 recursive generations" | experiment_config | NO |
| introduction.tex:19 | 410M | "Pythia-410M-deduped" | experiment_config | NO |
| introduction.tex:19 | 1B | "Pythia-1B-deduped" | experiment_config | NO |
| introduction.tex:19 | 355M | "GPT-2-medium" (implied 355M) | experiment_config | NO |
| introduction.tex:20 | 0--2 | "Gen~0--2" | other | NO |
| introduction.tex:20 | 2--4 | "Gen~2--4" | other | NO |
| introduction.tex:20 | 4--10 | "Gen~4--10" | other | NO |
| introduction.tex:35 | 10 | "SLV across 10 recursive generations" | other | NO |
| introduction.tex:35 | 0 | "$r{=}0$" | experiment_config | NO |
| introduction.tex:35 | 3 | "3-seed mean" | experiment_config | NO |
| introduction.tex:35 | 0.5 | "$r{=}0.5$" | experiment_config | NO |
| introduction.tex:35 | 2 | "2-seed mean" | experiment_config | NO |
| introduction.tex:35 | 50 | "50\% real-data mixing" | experiment_config | NO |
| introduction.tex:35 | 0--2 | "Gen~0--2" | other | NO |
| introduction.tex:35 | 2468 | "SLV peaks at 2468" | claim | YES |
| introduction.tex:35 | 2--4 | "Gen~2--4" | other | NO |
| introduction.tex:35 | 4--10 | "Gen~4--10" | other | NO |
| introduction.tex:35 | 11.6 | "SLV falls 11.6\% from peak" | claim | YES |
| introduction.tex:35 | 2181 | "to 2181" | claim | YES |
| introduction.tex:35 | 1 | "negligible Gen~1 dip" | other | NO |
| introduction.tex:35 | 2572 | "to 2572 at Gen~10" | claim | YES |
| introduction.tex:35 | 8.7 | "8.7\% above baseline" | claim | YES |
| introduction.tex:35 | 104 | "104 points above the pure-collapse peak" | claim | YES |

## method.tex

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| method.tex:4 | 1,000 | "$n{=}1{,}000$ held-out samples" | experiment_config | NO |
| method.tex:9 | 10^{-10} | "$\epsilon = 10^{-10}$" | hyperparameter | NO |
| method.tex:10 | 1,000 | "$n{=}1{,}000$" | experiment_config | NO |
| method.tex:10 | 1,024 | "$d{=}1{,}024$" | experiment_config | NO |
| method.tex:14 | 1000 | "$\gamma = n/d = 1000/1024$" | experiment_config | NO |
| method.tex:14 | 1024 | "$\gamma = n/d = 1000/1024$" | experiment_config | NO |
| method.tex:14 | 0.98 | "$\approx 0.98$" | other | NO |
| method.tex:15 | 250 | "$n \in \{250, 5000\}$" | experiment_config | NO |
| method.tex:15 | 5000 | "$n \in \{250, 5000\}$" | experiment_config | NO |
| method.tex:15 | 0.4 | "SLV CV $< 0.4\%$" | claim | YES |
| method.tex:15 | 0.016 | "smallest observed singular value ($0.016$, GPT-2-medium Gen~10)" | claim | YES |
| method.tex:15 | 8 | "eight orders of magnitude above $\epsilon$" | claim | YES |
| method.tex:18 | 1 | "concentrated $\to 1$" | other | NO |
| method.tex:29 | 0 | "Gen 0" | other | NO |
| method.tex:31 | 417.55 | "$r_{\text{eff}}$ = 417.55" (Gen 0) | table_cell | YES |
| method.tex:31 | 2366.68 | "SLV = 2366.68" (Gen 0) | table_cell | YES |
| method.tex:31 | 9.55 | "PPL = 9.55" (Gen 0) | table_cell | YES |
| method.tex:31 | .413 | "HeSw = .413" (Gen 0) | table_cell | YES |
| method.tex:31 | .738 | "D-4 = .738" (Gen 0) | table_cell | YES |
| method.tex:31 | 1942.8 | "$\sigma_1$ = 1942.8" (Gen 0) | table_cell | YES |
| method.tex:32 | 2 | "Gen 2" | other | NO |
| method.tex:32 | 496.17 | "$r_{\text{eff}}$ = 496.17" (Gen 2) | table_cell | YES |
| method.tex:32 | 2467.98 | "SLV = 2467.98" (Gen 2) | table_cell | YES |
| method.tex:32 | 13.56 | "PPL = 13.56" (Gen 2) | table_cell | YES |
| method.tex:32 | .380 | "HeSw = .380" (Gen 2) | table_cell | YES |
| method.tex:32 | .505 | "D-4 = .505" (Gen 2) | table_cell | YES |
| method.tex:32 | 718.7 | "$\sigma_1$ = 718.7" (Gen 2) | table_cell | YES |
| method.tex:33 | 5 | "Gen 5" | other | NO |
| method.tex:33 | 479.77 | "$r_{\text{eff}}$ = 479.77" (Gen 5) | table_cell | YES |
| method.tex:33 | 2365.99 | "SLV = 2365.99" (Gen 5) | table_cell | YES |
| method.tex:33 | 24.50 | "PPL = 24.50" (Gen 5) | table_cell | YES |
| method.tex:33 | .341 | "HeSw = .341" (Gen 5) | table_cell | YES |
| method.tex:33 | .412 | "D-4 = .412" (Gen 5) | table_cell | YES |
| method.tex:33 | 749.2 | "$\sigma_1$ = 749.2" (Gen 5) | table_cell | YES |
| method.tex:34 | 7 | "Gen 7" | other | NO |
| method.tex:34 | 464.10 | "$r_{\text{eff}}$ = 464.10" (Gen 7) | table_cell | YES |
| method.tex:34 | 2293.24 | "SLV = 2293.24" (Gen 7) | table_cell | YES |
| method.tex:34 | 37.82 | "PPL = 37.82" (Gen 7) | table_cell | YES |
| method.tex:34 | .319 | "HeSw = .319" (Gen 7) | table_cell | YES |
| method.tex:34 | .375 | "D-4 = .375" (Gen 7) | table_cell | YES |
| method.tex:34 | 788.4 | "$\sigma_1$ = 788.4" (Gen 7) | table_cell | YES |
| method.tex:35 | 10 | "Gen 10" | other | NO |
| method.tex:35 | 438.05 | "$r_{\text{eff}}$ = 438.05" (Gen 10) | table_cell | YES |
| method.tex:35 | 2181.35 | "SLV = 2181.35" (Gen 10) | table_cell | YES |
| method.tex:35 | 70.99 | "PPL = 70.99" (Gen 10) | table_cell | YES |
| method.tex:35 | .296 | "HeSw = .296" (Gen 10) | table_cell | YES |
| method.tex:35 | .324 | "D-4 = .324" (Gen 10) | table_cell | YES |
| method.tex:35 | 874.6 | "$\sigma_1$ = 874.6" (Gen 10) | table_cell | YES |
| method.tex:38 | 42 | "seeds 42, 43, 44" | experiment_config | NO |
| method.tex:38 | 43 | "seeds 42, 43, 44" | experiment_config | NO |
| method.tex:38 | 44 | "seeds 42, 43, 44" | experiment_config | NO |
| method.tex:38 | 10 | "Gen~10" | other | NO |
| method.tex:38 | 4.8 | "$r_{\text{eff}}$ $\pm$4.8" | claim | YES |
| method.tex:38 | 28.3 | "SLV $\pm$28.3" | claim | YES |
| method.tex:38 | 5.6 | "PPL $\pm$5.6" | claim | YES |
| method.tex:38 | .006 | "HeSw $\pm$.006" | claim | YES |
| method.tex:38 | .15 | "D-4 $\pm$.15" | claim | YES |
| method.tex:51 | 0.002 | "$\tau{=}0.002$" | hyperparameter | NO |
| method.tex:51 | 10 | "$k{=}10$" | hyperparameter | NO |
| method.tex:52 | 0.5 | "$\alpha{=}0.5$" | hyperparameter | NO |
| method.tex:52 | 2366.68 | "Gen~0, SLV${=}2366.68$" | claim | YES |
| method.tex:54 | 0.20 | "$[r_{\min}, r_{\max}] = [0.20, 0.80]$" | hyperparameter | NO |
| method.tex:54 | 0.80 | "$[r_{\min}, r_{\max}] = [0.20, 0.80]$" | hyperparameter | NO |
| method.tex:58 | 0.002 | "$\tau{=}0.002$" | hyperparameter | NO |
| method.tex:58 | 10 | "$k{=}10$" | hyperparameter | NO |
| method.tex:58 | 2 | "approximately 2 percentage points" | claim | NO |
| method.tex:61 | 10 | "$T{=}10$ generations" | experiment_config | NO |
| method.tex:61 | 2 | "from the second generation onward" | other | NO |
| method.tex:61 | 1 | "at $t{=}1$" | other | NO |
| method.tex:64 | 0.25 | "$0.25 < r_{\text{crit}} \leq 0.3$" | claim | YES |
| method.tex:64 | 0.3 | "$0.25 < r_{\text{crit}} \leq 0.3$" | claim | YES |
| method.tex:64 | 2--10 | "Gen~2--10" | other | NO |
| method.tex:64 | 410M | "Pythia-410M" | experiment_config | NO |
| method.tex:73 | 0.3 | "$\alpha_2{=}0.3$" | hyperparameter | NO |

## experiments.tex

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| experiments.tex:5 | 410M | "Pythia-410M-deduped" | experiment_config | NO |
| experiments.tex:5 | 50K | "50K-subset of OpenWebText" | dataset_stat | YES |
| experiments.tex:5 | 256 | "$\geq$256 non-padding tokens" | experiment_config | NO |
| experiments.tex:6 | 0 | "generation~0" | other | NO |
| experiments.tex:6 | 10 | "10 recursive generations" | experiment_config | NO |
| experiments.tex:7 | 1K | "1K held-out last-layer embeddings" | experiment_config | NO |
| experiments.tex:7 | 3 | "three downstream metrics" | other | NO |
| experiments.tex:7 | 0 | "0-shot" | experiment_config | NO |
| experiments.tex:8 | 3 | "These three metrics" | other | NO |
| experiments.tex:8 | 410M | "410M-parameter model" | experiment_config | NO |
| experiments.tex:12 | 0 | "$r_t{=}0$" | experiment_config | NO |
| experiments.tex:13 | 0.50 | "$r_t{=}0.50$" | experiment_config | NO |
| experiments.tex:14 | 10 | "$k{=}10$" | hyperparameter | NO |
| experiments.tex:15 | 0.2 | "$r \in \{0.2, 0.25, 0.3\}$" | experiment_config | NO |
| experiments.tex:15 | 0.25 | "$r \in \{0.2, 0.25, 0.3\}$" | experiment_config | NO |
| experiments.tex:15 | 0.3 | "$r \in \{0.2, 0.25, 0.3\}$" | experiment_config | NO |
| experiments.tex:20 | 10 | "across 10 recursive generations" | other | NO |
| experiments.tex:23 | 417.55 | "$r_{\text{eff}}$ rises from 417.55" | claim | YES |
| experiments.tex:23 | 496.2 | "to 496.2" | claim | YES |
| experiments.tex:23 | 18.8 | "+18.8\%" | claim | YES |
| experiments.tex:23 | 2366.7 | "SLV from 2366.7" | claim | YES |
| experiments.tex:23 | 2468.0 | "to 2468.0" | claim | YES |
| experiments.tex:23 | 4.3 | "+4.3\%" | claim | YES |
| experiments.tex:23 | 1942.8 | "$\sigma_1$ drops from 1942.8" | claim | YES |
| experiments.tex:23 | 718.7 | "to 718.7" | claim | YES |
| experiments.tex:24 | 2 | "Gen~2" | other | NO |
| experiments.tex:24 | 3 | "three seeds" | experiment_config | NO |
| experiments.tex:24 | 1.3 | "CV $< 1.3\%$" | claim | YES |
| experiments.tex:25 | 8.0 | "HellaSwag drops 8.0\%" | claim | YES |
| experiments.tex:25 | 31.6 | "distinct-4 falls 31.6\%" | claim | YES |
| experiments.tex:25 | 1 | "${<}\,1$\,s" | claim | YES |
| experiments.tex:25 | 70 | "${\sim}$70\,min" | claim | YES |
| experiments.tex:30 | 42 | "seeds (42, 43, 44)" | experiment_config | NO |
| experiments.tex:30 | 43 | "seeds (42, 43, 44)" | experiment_config | NO |
| experiments.tex:30 | 44 | "seeds (42, 43, 44)" | experiment_config | NO |
| experiments.tex:30 | 3 | "3-seed mean" | experiment_config | NO |
| experiments.tex:30 | 1 | "$\pm$1 s.d." | other | NO |
| experiments.tex:30 | 1.3 | "below 1.3\%" | claim | YES |
| experiments.tex:37 | 10 | "10 recursive generations" | other | NO |
| experiments.tex:37 | 0 | "$r{=}0$" | experiment_config | NO |
| experiments.tex:37 | 3 | "3-seed mean" | experiment_config | NO |
| experiments.tex:37 | 0--2 | "Gen~0--2" | other | NO |
| experiments.tex:37 | 4--10 | "Gen~4--10" | other | NO |
| experiments.tex:42 | 496.2 | "$r_{\text{eff}}$: 496.2$\to$493.6" | claim | YES |
| experiments.tex:42 | 493.6 | "$r_{\text{eff}}$: 496.2$\to$493.6" | claim | YES |
| experiments.tex:42 | 2468 | "SLV: 2468$\to$2440" | claim | YES |
| experiments.tex:42 | 2440 | "SLV: 2468$\to$2440" | claim | YES |
| experiments.tex:43 | 1.1 | "$-$1.1\%" | claim | YES |
| experiments.tex:43 | 0.5 | "$-$0.5\%" | claim | YES |
| experiments.tex:44 | 1B | "At 1B scale" | experiment_config | NO |
| experiments.tex:44 | 1 | "one generation earlier" | claim | YES |
| experiments.tex:47 | 31.0 | "averages $-$31.0" | claim | YES |
| experiments.tex:47 | 2--4 | "Gen~2--4" | other | NO |
| experiments.tex:47 | 37.4 | "$-$37.4" | claim | YES |
| experiments.tex:47 | 4--10 | "Gen~4--10" | other | NO |
| experiments.tex:47 | 78 | "78\% of the total peak-to-final decline" | claim | YES |
| experiments.tex:48 | 10 | "Gen~10" | other | NO |
| experiments.tex:48 | 438.1 | "$r_{\text{eff}}$ falls to 438.1" | claim | YES |
| experiments.tex:48 | 11.7 | "$-$11.7\% from peak" | claim | YES |
| experiments.tex:48 | 2181.4 | "SLV to 2181.4" | claim | YES |
| experiments.tex:48 | 11.6 | "$-$11.6\% from peak" | claim | YES |
| experiments.tex:48 | 71.0 | "perplexity reaches 71.0" | claim | YES |
| experiments.tex:48 | 643 | "$+$643\%" | claim | YES |
| experiments.tex:49 | 1942.8 | "$\sigma_1$...dropping from 1942.8" | claim | YES |
| experiments.tex:49 | 718.7 | "to 718.7" | claim | YES |
| experiments.tex:49 | 874.6 | "rises to 874.6 by Gen~10" | claim | YES |
| experiments.tex:53 | 1B | "Pythia-1B-deduped" | experiment_config | NO |
| experiments.tex:53 | 0--3 | "Gen~0--3" | experiment_config | NO |
| experiments.tex:53 | 2835 | "SLV rises from 2835" | claim | YES |
| experiments.tex:53 | 2906 | "to 2906 at Gen~1" | claim | YES |
| experiments.tex:53 | 2.5 | "$+$2.5\%" | claim | YES |
| experiments.tex:53 | 2865 | "declining to 2865 at Gen~3" | claim | YES |
| experiments.tex:53 | 2 | "peaks one generation later at Gen~2" | claim | YES |
| experiments.tex:53 | 580.9 | "580.9" | claim | YES |
| experiments.tex:53 | 570.8 | "570.8 at Gen~1" | claim | YES |
| experiments.tex:54 | 1 | "one-generation SLV lead" | claim | NO |
| experiments.tex:54 | 410M | "at 410M" | experiment_config | NO |
| experiments.tex:55 | 8.1 | "8.1$\to$13.4" | claim | YES |
| experiments.tex:55 | 13.4 | "8.1$\to$13.4" | claim | YES |
| experiments.tex:55 | 66 | "$+$66\%" | claim | YES |
| experiments.tex:55 | 410M | "410M scale" | experiment_config | NO |
| experiments.tex:56 | 10 | "Full 10-generation" | other | NO |
| experiments.tex:56 | 1B | "at 1B" | experiment_config | NO |
| experiments.tex:62 | 2 | "SLV peaks at Gen~2" | other | NO |
| experiments.tex:62 | 2468 | "(2468)" | claim | YES |
| experiments.tex:62 | 50 | "50\% mixing" | experiment_config | NO |
| experiments.tex:62 | 2572 | "2572 at Gen~10" | claim | YES |
| experiments.tex:62 | 1 | "Gen~1 dip" | other | NO |
| experiments.tex:62 | 0.0005 | "$\Delta_1 \approx 0.0005$" | claim | YES |
| experiments.tex:63 | 10 | "$k{=}10$" | hyperparameter | NO |
| experiments.tex:63 | 10 | "ten generations" | experiment_config | NO |
| experiments.tex:64 | 40.4 | "drops from 40.4" | claim | YES |
| experiments.tex:64 | 0 | "at $r{=}0$" | experiment_config | NO |
| experiments.tex:64 | 3.8 | "to 3.8 at $r{=}0.2$" | claim | YES |
| experiments.tex:64 | 0.2 | "$r{=}0.2$" | experiment_config | NO |
| experiments.tex:64 | 0 | "exactly zero at $r \geq 0.3$" | claim | YES |
| experiments.tex:64 | 0.3 | "$r \geq 0.3$" | experiment_config | NO |
| experiments.tex:68 | 0.85 | "width=0.85\columnwidth" | other | NO |
| experiments.tex:69 | 10 | "$10\times$" | claim | YES |
| experiments.tex:69 | 0 | "$r{=}0$" | experiment_config | NO |
| experiments.tex:69 | 0.2 | "$r{=}0.2$" | experiment_config | NO |
| experiments.tex:69 | 0 | "exactly zero" | claim | NO |
| experiments.tex:69 | 0.3 | "$r \geq 0.3$" | experiment_config | NO |
| experiments.tex:73 | 0.5 | "$r{=}0.5$" | experiment_config | NO |
| experiments.tex:73 | 58 | "perplexity increases 58\%" | claim | YES |
| experiments.tex:73 | .152 | "distinct-4 falls to .152" | claim | YES |
| experiments.tex:78 | 7 | "seven alternative collapse indicators" | other | NO |
| experiments.tex:78 | 3 | "three signal sources" | other | NO |
| experiments.tex:82 | 2 | "Gen~2" | other | NO |
| experiments.tex:82 | 0 | "Gen~0" | other | NO |
| experiments.tex:82 | 2.5 | "2.5$\times$ that of RankMe" | claim | YES |
| experiments.tex:82 | 11.8 | "11.8\%" | claim | YES |
| experiments.tex:82 | 4.7 | "4.7\% relative change" | claim | YES |
| experiments.tex:92 | 11.8 | "SLV Rel $\Delta$ = 11.8\%" | table_cell | YES |
| experiments.tex:93 | 4.7 | "RankMe Rel $\Delta$ = 4.7\%" | table_cell | YES |
| experiments.tex:94 | 9.6 | "Token ent. Rel $\Delta$ = 9.6\%" | table_cell | YES |
| experiments.tex:95 | 14.0 | "Stable rank Rel $\Delta$ = 14.0\%" | table_cell | YES |
| experiments.tex:96 | 8.0 | "Spec. norm Rel $\Delta$ = 8.0\%" | table_cell | YES |
| experiments.tex:97 | 75 | "Isotropy Rel $\Delta$ = 75\%" | table_cell | YES |
| experiments.tex:97 | 6 | "Non-mono. (6 rev.)" | table_cell | YES |
| experiments.tex:98 | 704 | "Raw PPL Rel $\Delta$ = 704\%" | table_cell | YES |
| experiments.tex:99 | 1 | "PPL growth $\sim$Mono. (1)" | table_cell | YES |
| experiments.tex:105 | 7 | "Seven of eight" | claim | YES |
| experiments.tex:105 | 8 | "Seven of eight" | claim | NO |
| experiments.tex:107 | 2 | "$= 2 \times \text{SLV}$" | other | NO |
| experiments.tex:114 | 10 | "10 recursive generations" | experiment_config | NO |
| experiments.tex:114 | 5 | "five mixing ratios" | experiment_config | NO |
| experiments.tex:114 | 3 | "three qualitatively distinct trajectory types" | claim | NO |
| experiments.tex:119 | 0.92 | "width=0.92\columnwidth" | other | NO |
| experiments.tex:119 | 0 | "$r{=}0$" | experiment_config | NO |
| experiments.tex:119 | 0.2 | "$r{=}0.2$" | experiment_config | NO |
| experiments.tex:119 | 0.25 | "$r{=}0.25$" | experiment_config | NO |
| experiments.tex:119 | 0.3 | "$r{=}0.3$" | experiment_config | NO |
| experiments.tex:119 | 3 | "3-seed mean" | experiment_config | NO |
| experiments.tex:119 | 0.5 | "$r{=}0.5$" | experiment_config | NO |
| experiments.tex:119 | 2 | "2-seed mean" | experiment_config | NO |
| experiments.tex:119 | 0.25 | "$r_{\text{crit}} \in (0.25, 0.3]$" | claim | NO |
| experiments.tex:119 | 0.3 | "$r_{\text{crit}} \in (0.25, 0.3]$" | claim | NO |
| experiments.tex:119 | 0 | "Gen~0 baseline" | other | NO |
| experiments.tex:124 | 96 | "$+$96 points at Gen~1" | claim | YES |
| experiments.tex:124 | 1 | "Gen~1" | other | NO |
| experiments.tex:124 | 2 | "peaking at Gen~2" | other | NO |
| experiments.tex:127 | 0.2 | "$r{=}0.2$" | experiment_config | NO |
| experiments.tex:127 | 7.3 | "dips $-7.3$ points at Gen~2" | claim | YES |
| experiments.tex:127 | 2467.2 | "recovering to 2467.2 at Gen~10" | claim | YES |
| experiments.tex:127 | 4.3 | "$+4.3\%$ above baseline" | claim | YES |
| experiments.tex:128 | 2 | "Gen~2" | other | NO |
| experiments.tex:128 | 0.2 | "$r{=}0.2$ below $r_{\text{crit}}$" | claim | NO |
| experiments.tex:128 | 0.0016 | "$\max \Delta_t = 0.0016$" | claim | YES |
| experiments.tex:128 | 0.002 | "$\tau{=}0.002$" | hyperparameter | NO |
| experiments.tex:129 | 0.25 | "$r{=}0.25$" | experiment_config | NO |
| experiments.tex:129 | 2.1 | "weaker dip ($-2.1$)" | claim | YES |
| experiments.tex:129 | 3 | "${\sim}3\times$ weaker signal" | claim | YES |
| experiments.tex:130 | 0.2 | "$r \geq 0.2$" | experiment_config | NO |
| experiments.tex:130 | 2 | "2-type classification" | other | NO |
| experiments.tex:134 | 0.92 | "width=0.92\columnwidth" | other | NO |
| experiments.tex:141 | 0.3 | "$r{=}0.3$" | experiment_config | NO |
| experiments.tex:141 | 2508.2 | "SLV reaches 2508.2 at Gen~10" | claim | YES |
| experiments.tex:141 | 6.0 | "$+$6.0\% above baseline" | claim | YES |
| experiments.tex:141 | 0.5 | "$r{=}0.5$" | experiment_config | NO |
| experiments.tex:141 | 2572 | "2572" | claim | YES |
| experiments.tex:141 | 8.7 | "$+$8.7\%" | claim | YES |
| experiments.tex:142 | 0.3 | "$\alpha \in \{0.3, 0.5, 0.7\}$" | hyperparameter | NO |
| experiments.tex:142 | 0.5 | "$\alpha \in \{0.3, 0.5, 0.7\}$" | hyperparameter | NO |
| experiments.tex:142 | 0.7 | "$\alpha \in \{0.3, 0.5, 0.7\}$" | hyperparameter | NO |
| experiments.tex:142 | 0.25 | "$r_{\text{crit}} \in (0.25, 0.3]$" | claim | YES |
| experiments.tex:142 | 0.3 | "$r_{\text{crit}} \in (0.25, 0.3]$" | claim | YES |
| experiments.tex:142 | 7.3 | "$-7.3$ at $r{=}0.2$" | claim | YES |
| experiments.tex:142 | 3.3 | "$-3.3$ at $r{=}0.25$" | claim | YES |
| experiments.tex:142 | 1.5 | "$-1.5$ at $r{=}0.3$" | claim | YES |
| experiments.tex:146 | 0.2 | "$r \in \{0.2, 0.25\}$" | experiment_config | NO |
| experiments.tex:146 | 0.25 | "$r \in \{0.2, 0.25\}$" | experiment_config | NO |
| experiments.tex:146 | .324 | "mean $.324$--$.342$" | claim | YES |
| experiments.tex:146 | .342 | "mean $.324$--$.342$" | claim | YES |
| experiments.tex:146 | 0.17 | "s.d.\ $\approx 0.17$" | claim | YES |
| experiments.tex:146 | .152 | "dropping to .152 at $r{=}0.5$" | claim | YES |
| experiments.tex:147 | 3.9 | "CV $= 3.9\%$" | claim | YES |
| experiments.tex:147 | 0.12 | "vs.\ $0.12\%$ at $r{=}0.25$" | claim | YES |
| experiments.tex:153 | 0.3 | "$r > 0.3$" | claim | NO |
| experiments.tex:163 | 0 | "$r$ = 0, Type I" | table_cell | NO |
| experiments.tex:163 | 2181.4 | "SLV = 2181.4" | table_cell | YES |
| experiments.tex:163 | 438.1 | "$r_{\text{eff}}$ = 438.1" | table_cell | YES |
| experiments.tex:163 | 71.0 | "PPL = 71.0" | table_cell | YES |
| experiments.tex:163 | .324 | "D-4 = .324" | table_cell | YES |
| experiments.tex:163 | 10 | "Gen. = 10" | table_cell | NO |
| experiments.tex:164 | 0.20 | "$r$ = 0.20, Type II" | table_cell | NO |
| experiments.tex:164 | 2467.2 | "SLV = 2467.2" | table_cell | YES |
| experiments.tex:164 | 508.1 | "$r_{\text{eff}}$ = 508.1" | table_cell | YES |
| experiments.tex:164 | 13.54 | "PPL = 13.54" | table_cell | YES |
| experiments.tex:164 | .324 | "D-4 = .324" | table_cell | YES |
| experiments.tex:164 | .0016 | "$\max\Delta_t$ = .0016" | table_cell | YES |
| experiments.tex:164 | 10 | "Gen. = 10" | table_cell | NO |
| experiments.tex:165 | 0.25 | "$r$ = 0.25, Type II" | table_cell | NO |
| experiments.tex:165 | 2488.1 | "SLV = 2488.1" | table_cell | YES |
| experiments.tex:165 | 513.8 | "$r_{\text{eff}}$ = 513.8" | table_cell | YES |
| experiments.tex:165 | 13.41 | "PPL = 13.41" | table_cell | YES |
| experiments.tex:165 | .342 | "D-4 = .342" | table_cell | YES |
| experiments.tex:165 | .0005 | "$\max\Delta_t$ = .0005" | table_cell | YES |
| experiments.tex:165 | 10 | "Gen. = 10" | table_cell | NO |
| experiments.tex:166 | 0.30 | "$r$ = 0.30, Type III" | table_cell | NO |
| experiments.tex:166 | 2508.2 | "SLV = 2508.2" | table_cell | YES |
| experiments.tex:166 | 521.1 | "$r_{\text{eff}}$ = 521.1" | table_cell | YES |
| experiments.tex:166 | 13.34 | "PPL = 13.34" | table_cell | YES |
| experiments.tex:166 | .295 | "D-4 = .295" | table_cell | YES |
| experiments.tex:166 | 0 | "$\max\Delta_t$ = 0" | table_cell | YES |
| experiments.tex:166 | 10 | "Gen. = 10" | table_cell | NO |
| experiments.tex:167 | 0.50 | "$r$ = 0.50, Type III" | table_cell | NO |
| experiments.tex:167 | 2571.6 | "SLV = 2571.6" | table_cell | YES |
| experiments.tex:167 | 553.5 | "$r_{\text{eff}}$ = 553.5" | table_cell | YES |
| experiments.tex:167 | 15.11 | "PPL = 15.11" | table_cell | YES |
| experiments.tex:167 | .152 | "D-4 = .152" | table_cell | YES |
| experiments.tex:167 | 0 | "$\max\Delta_t$ = 0" | table_cell | YES |
| experiments.tex:167 | 10 | "Gen. = 10" | table_cell | NO |
| experiments.tex:170 | 42 | "seeds (42, 43, 44)" | experiment_config | NO |
| experiments.tex:170 | 43 | "seeds (42, 43, 44)" | experiment_config | NO |
| experiments.tex:170 | 44 | "seeds (42, 43, 44)" | experiment_config | NO |
| experiments.tex:170 | 3 | "mean of three seeds" | experiment_config | NO |
| experiments.tex:170 | 2 | "mean of two seeds" | experiment_config | NO |
| experiments.tex:170 | 0.15 | "D-4...s.d. = 0.15" at $r{=}0$ | claim | YES |
| experiments.tex:170 | 0.155 | "D-4...s.d. = 0.155" at $r{=}0.3$ | claim | YES |
| experiments.tex:177 | 355M | "GPT-2-medium (355M parameters)" | experiment_config | NO |
| experiments.tex:177 | 0 | "$r{=}0$" | experiment_config | NO |
| experiments.tex:177 | 9 | "9 generations" | experiment_config | NO |
| experiments.tex:177 | 0.25 | "$r{=}0.25$" | experiment_config | NO |
| experiments.tex:177 | 0.3 | "$r{=}0.3$" | experiment_config | NO |
| experiments.tex:177 | 3 | "3 generations each" | experiment_config | NO |
| experiments.tex:177 | 1.0 | "$r{=}1.0$" | experiment_config | NO |
| experiments.tex:177 | 3 | "3 generations" | experiment_config | NO |
| experiments.tex:179 | 924 | "SLV peaks at Gen~2 (924)" | claim | YES |
| experiments.tex:179 | 34.1 | "$+$34.1\% from baseline" | claim | YES |
| experiments.tex:179 | 415 | "declines to 415 by Gen~9" | claim | YES |
| experiments.tex:179 | 55.1 | "$-$55.1\% from peak" | claim | YES |
| experiments.tex:179 | 15.5 | "perplexity rises from 15.5" | claim | YES |
| experiments.tex:179 | 329 | "to 329" | claim | YES |
| experiments.tex:179 | 2028 | "$+$2028\%" | claim | YES |
| experiments.tex:180 | 6598 | "$\sigma_1$: 6598$\to$1191" | claim | YES |
| experiments.tex:180 | 1191 | "$\sigma_1$: 6598$\to$1191" | claim | YES |
| experiments.tex:180 | 1570 | "rising to ${\sim}$1570 by Gen~9" | claim | YES |
| experiments.tex:181 | 55.1 | "$-$55.1\% vs.\ $-$11.6\%" | claim | YES |
| experiments.tex:181 | 11.6 | "$-$55.1\% vs.\ $-$11.6\% SLV decline" | claim | YES |
| experiments.tex:181 | 23 | "$r_{\text{eff}}{=}23$" | claim | YES |
| experiments.tex:181 | 418 | "Pythia's 418" | claim | YES |
| experiments.tex:183 | 1.0 | "$r{=}1.0$" | experiment_config | NO |
| experiments.tex:183 | 27.4 | "$-$27.4\%" | claim | YES |
| experiments.tex:185 | 0.25 | "$r{=}0.25$" | experiment_config | NO |
| experiments.tex:185 | 0.3 | "$r{=}0.3$" | experiment_config | NO |
| experiments.tex:185 | 0--1 | "Gen~0$\to$1" | other | NO |
| experiments.tex:185 | 7.5 | "SLV $+$7.5--8.5\%" | claim | YES |
| experiments.tex:185 | 8.5 | "SLV $+$7.5--8.5\%" | claim | YES |
| experiments.tex:185 | 23 | "$r_{\text{eff}}$ from 23" | claim | YES |
| experiments.tex:185 | 136 | "to 136--142" | claim | YES |
| experiments.tex:185 | 142 | "to 136--142" | claim | YES |
| experiments.tex:185 | 80 | "$\sigma_1$ $-$80--82\%" | claim | YES |
| experiments.tex:185 | 82 | "$\sigma_1$ $-$80--82\%" | claim | YES |
| experiments.tex:185 | 3 | "through Gen~3" | other | NO |
| experiments.tex:187 | 0.25 | "$r{=}0.25$" | experiment_config | NO |
| experiments.tex:187 | 3 | "three-generation window" | other | NO |
| experiments.tex:187 | 5 | "Gen~5+" | other | NO |
| experiments.tex:187 | 410M | "Pythia-410M" | experiment_config | NO |
| experiments.tex:197 | 0 | "$r$ = 0, Type I" (cross-arch table) | table_cell | NO |
| experiments.tex:197 | 689 | "SLV$_0$ = 689" | table_cell | YES |
| experiments.tex:197 | 415 | "SLV$_{\text{end}}$ = 415 (G9)" | table_cell | YES |
| experiments.tex:197 | 39.8 | "$\Delta$SLV = $-$39.8\%" | table_cell | YES |
| experiments.tex:198 | 0.25 | "$r$ = 0.25" | table_cell | NO |
| experiments.tex:198 | 689 | "SLV$_0$ = 689" | table_cell | YES |
| experiments.tex:198 | 738 | "SLV$_{\text{end}}$ = 738 (G3)" | table_cell | YES |
| experiments.tex:198 | 7.0 | "$\Delta$SLV = $+$7.0\%" | table_cell | YES |
| experiments.tex:199 | 0.30 | "$r$ = 0.30, Type III" | table_cell | NO |
| experiments.tex:199 | 689 | "SLV$_0$ = 689" | table_cell | YES |
| experiments.tex:199 | 737 | "SLV$_{\text{end}}$ = 737 (G3)" | table_cell | YES |
| experiments.tex:199 | 6.9 | "$\Delta$SLV = $+$6.9\%" | table_cell | YES |
| experiments.tex:200 | 1.0 | "$r$ = 1.0, Ctrl" | table_cell | NO |
| experiments.tex:200 | 689 | "SLV$_0$ = 689" | table_cell | YES |
| experiments.tex:200 | 813 | "SLV$_{\text{end}}$ = 813 (G3)" | table_cell | YES |
| experiments.tex:200 | 17.9 | "$\Delta$SLV = $+$17.9\%" | table_cell | YES |
| experiments.tex:203 | 355M | "GPT-2-medium (355M, seed~42)" | experiment_config | NO |
| experiments.tex:203 | 42 | "seed~42" | experiment_config | NO |

## conclusion.tex

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| conclusion.tex:6 | 10 | "$10\times$" (signal drops 10x) | claim | YES |
| conclusion.tex:6 | 0 | "$r{=}0$" | experiment_config | NO |
| conclusion.tex:6 | 0.2 | "$r{=}0.2$" | experiment_config | NO |
| conclusion.tex:6 | 0.3 | "$r \geq 0.3$" | experiment_config | NO |
| conclusion.tex:8 | 0.25 | "$r_{\text{crit}} \in (0.25, 0.3]$" | claim | YES |
| conclusion.tex:8 | 0.3 | "$r_{\text{crit}} \in (0.25, 0.3]$" | claim | YES |
| conclusion.tex:8 | 355M | "GPT-2-medium" (implied) | experiment_config | NO |
| conclusion.tex:8 | 1B | "Pythia-1B" | experiment_config | NO |

## limitations.tex

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| limitations.tex:4 | 2 | "two model scales" | experiment_config | NO |
| limitations.tex:4 | 410M | "Pythia-410M" | experiment_config | NO |
| limitations.tex:4 | 1B | "1B pilot" | experiment_config | NO |
| limitations.tex:4 | 3 | "through Gen~3" | experiment_config | NO |
| limitations.tex:9 | 10 | "Ten recursive generations" | experiment_config | NO |

## related_work.tex

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| related_work.tex:10 | 1 | "as little as 1\% synthetic contamination" | other | NO |
| related_work.tex:16 | 125M | "OPT-125M" | other | NO |
| related_work.tex:16 | 3 | "over three generations" | other | NO |
| related_work.tex:17 | 2 | "$= 2 \times \text{SLV}$" (SLV = half log det G) | other | NO |
| related_work.tex:17 | 410M | "Pythia-410M/1B" | experiment_config | NO |
| related_work.tex:17 | 1B | "Pythia-410M/1B" | experiment_config | NO |
| related_work.tex:17 | 3 | "3--8$\times$ larger" | claim | NO |
| related_work.tex:17 | 8 | "3--8$\times$ larger" | claim | NO |
| related_work.tex:17 | 10 | "10 vs.\ 3 generations" | claim | NO |
| related_work.tex:17 | 3 | "10 vs.\ 3 generations" | other | NO |
| related_work.tex:37 | 125M | "SIGMA Scale = 125M" | table_cell | NO |
| related_work.tex:37 | 3 | "SIGMA Generations = 3" | table_cell | NO |
| related_work.tex:38 | 355M | "This work Scale = 355M--1B" | table_cell | NO |
| related_work.tex:38 | 1B | "This work Scale = 355M--1B" | table_cell | NO |
| related_work.tex:38 | 10 | "This work Generations = 10" | table_cell | NO |

## appendix.tex

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| appendix.tex:5 | 8 | "eight alternative early warning indicators" | other | NO |
| appendix.tex:15 | 11.8 | "SLV Rel $\Delta$ = 11.8\%" | table_cell | YES |
| appendix.tex:16 | 4.7 | "RankMe Rel $\Delta$ = 4.7\%" | table_cell | YES |
| appendix.tex:17 | 9.6 | "Token ent. Rel $\Delta$ = 9.6\%" | table_cell | YES |
| appendix.tex:18 | 14.0 | "Stable rank Rel $\Delta$ = 14.0\%" | table_cell | YES |
| appendix.tex:19 | 8.0 | "Spec. norm Rel $\Delta$ = 8.0\%" | table_cell | YES |
| appendix.tex:20 | 75 | "Isotropy Rel $\Delta$ = 75\%" | table_cell | YES |
| appendix.tex:20 | 6 | "Isotropy non-mono (6 violations)" | table_cell | YES |
| appendix.tex:21 | 704 | "Raw PPL Rel $\Delta$ = 704\%" | table_cell | YES |
| appendix.tex:22 | 1 | "PPL growth $\sim$ mono (1 violation)" | table_cell | YES |
| appendix.tex:25 | 704 | "Raw PPL Rel~$\Delta$ is 704\% for seed~42" | claim | YES |
| appendix.tex:25 | 42 | "for seed~42" | experiment_config | NO |
| appendix.tex:25 | 643 | "main text reports 643\% (3-seed mean)" | claim | YES |
| appendix.tex:25 | 3 | "3-seed mean" | experiment_config | NO |
| appendix.tex:32 | 3 | "three seeds (42, 43, 44)" | experiment_config | NO |
| appendix.tex:32 | 42 | "seeds (42, 43, 44)" | experiment_config | NO |
| appendix.tex:32 | 43 | "seeds (42, 43, 44)" | experiment_config | NO |
| appendix.tex:32 | 44 | "seeds (42, 43, 44)" | experiment_config | NO |
| appendix.tex:33 | 1.3 | "SLV coefficient of variation $< 1.3\%$" | claim | YES |
| appendix.tex:34 | 5 | "after Gen~5" | other | NO |
| appendix.tex:34 | 46 | "coefficient of variation of 46\% at Gen~10" | claim | YES |
| appendix.tex:34 | 10 | "at Gen~10" | other | NO |

### Appendix Table: Per-gen variance (r=0), tab:pergen_variance

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| appendix.tex:46 (Gen 0) | 417.5 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:46 | 0.0 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:46 | 2366.7 | "SLV mean" | table_cell | YES |
| appendix.tex:46 | 0.0 | "SLV s.d." | table_cell | YES |
| appendix.tex:46 | 9.55 | "PPL mean" | table_cell | YES |
| appendix.tex:46 | 0.00 | "PPL s.d." | table_cell | YES |
| appendix.tex:46 | .413 | "HeSw mean" | table_cell | YES |
| appendix.tex:46 | .000 | "HeSw s.d." | table_cell | YES |
| appendix.tex:46 | .738 | "D-4 mean" | table_cell | YES |
| appendix.tex:46 | .006 | "D-4 s.d." | table_cell | YES |
| appendix.tex:46 | 1942.8 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:46 | 0.0 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:47 (Gen 1) | 491.1 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:47 | 0.6 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:47 | 2462.3 | "SLV mean" | table_cell | YES |
| appendix.tex:47 | 2.7 | "SLV s.d." | table_cell | YES |
| appendix.tex:47 | 11.37 | "PPL mean" | table_cell | YES |
| appendix.tex:47 | 0.01 | "PPL s.d." | table_cell | YES |
| appendix.tex:47 | .390 | "HeSw mean" | table_cell | YES |
| appendix.tex:47 | .001 | "HeSw s.d." | table_cell | YES |
| appendix.tex:47 | .609 | "D-4 mean" | table_cell | YES |
| appendix.tex:47 | .014 | "D-4 s.d." | table_cell | YES |
| appendix.tex:47 | 808.9 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:47 | 5.4 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:48 (Gen 2) | 496.2 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:48 | 0.3 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:48 | 2468.0 | "SLV mean" | table_cell | YES |
| appendix.tex:48 | 1.7 | "SLV s.d." | table_cell | YES |
| appendix.tex:48 | 13.56 | "PPL mean" | table_cell | YES |
| appendix.tex:48 | 0.02 | "PPL s.d." | table_cell | YES |
| appendix.tex:48 | .380 | "HeSw mean" | table_cell | YES |
| appendix.tex:48 | .004 | "HeSw s.d." | table_cell | YES |
| appendix.tex:48 | .505 | "D-4 mean" | table_cell | YES |
| appendix.tex:48 | .011 | "D-4 s.d." | table_cell | YES |
| appendix.tex:48 | 718.7 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:48 | 7.0 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:49 (Gen 3) | 493.6 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:49 | 0.4 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:49 | 2440.4 | "SLV mean" | table_cell | YES |
| appendix.tex:49 | 2.0 | "SLV s.d." | table_cell | YES |
| appendix.tex:49 | 16.23 | "PPL mean" | table_cell | YES |
| appendix.tex:49 | 0.02 | "PPL s.d." | table_cell | YES |
| appendix.tex:49 | .367 | "HeSw mean" | table_cell | YES |
| appendix.tex:49 | .005 | "HeSw s.d." | table_cell | YES |
| appendix.tex:49 | .465 | "D-4 mean" | table_cell | YES |
| appendix.tex:49 | .033 | "D-4 s.d." | table_cell | YES |
| appendix.tex:49 | 708.7 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:49 | 7.5 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:50 (Gen 4) | 487.8 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:50 | 1.9 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:50 | 2406.0 | "SLV mean" | table_cell | YES |
| appendix.tex:50 | 2.0 | "SLV s.d." | table_cell | YES |
| appendix.tex:50 | 19.90 | "PPL mean" | table_cell | YES |
| appendix.tex:50 | 0.09 | "PPL s.d." | table_cell | YES |
| appendix.tex:50 | .354 | "HeSw mean" | table_cell | YES |
| appendix.tex:50 | .003 | "HeSw s.d." | table_cell | YES |
| appendix.tex:50 | .419 | "D-4 mean" | table_cell | YES |
| appendix.tex:50 | .047 | "D-4 s.d." | table_cell | YES |
| appendix.tex:50 | 722.9 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:50 | 6.9 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:51 (Gen 5) | 479.8 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:51 | 0.5 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:51 | 2366.0 | "SLV mean" | table_cell | YES |
| appendix.tex:51 | 3.8 | "SLV s.d." | table_cell | YES |
| appendix.tex:51 | 24.50 | "PPL mean" | table_cell | YES |
| appendix.tex:51 | 0.17 | "PPL s.d." | table_cell | YES |
| appendix.tex:51 | .341 | "HeSw mean" | table_cell | YES |
| appendix.tex:51 | .003 | "HeSw s.d." | table_cell | YES |
| appendix.tex:51 | .412 | "D-4 mean" | table_cell | YES |
| appendix.tex:51 | .053 | "D-4 s.d." | table_cell | YES |
| appendix.tex:51 | 749.2 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:51 | 7.1 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:52 (Gen 6) | 472.4 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:52 | 0.6 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:52 | 2326.1 | "SLV mean" | table_cell | YES |
| appendix.tex:52 | 8.6 | "SLV s.d." | table_cell | YES |
| appendix.tex:52 | 30.40 | "PPL mean" | table_cell | YES |
| appendix.tex:52 | 0.45 | "PPL s.d." | table_cell | YES |
| appendix.tex:52 | .329 | "HeSw mean" | table_cell | YES |
| appendix.tex:52 | .004 | "HeSw s.d." | table_cell | YES |
| appendix.tex:52 | .402 | "D-4 mean" | table_cell | YES |
| appendix.tex:52 | .067 | "D-4 s.d." | table_cell | YES |
| appendix.tex:52 | 764.6 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:52 | 5.7 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:53 (Gen 7) | 464.1 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:53 | 0.2 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:53 | 2293.2 | "SLV mean" | table_cell | YES |
| appendix.tex:53 | 10.2 | "SLV s.d." | table_cell | YES |
| appendix.tex:53 | 37.82 | "PPL mean" | table_cell | YES |
| appendix.tex:53 | 0.94 | "PPL s.d." | table_cell | YES |
| appendix.tex:53 | .319 | "HeSw mean" | table_cell | YES |
| appendix.tex:53 | .000 | "HeSw s.d." | table_cell | YES |
| appendix.tex:53 | .375 | "D-4 mean" | table_cell | YES |
| appendix.tex:53 | .082 | "D-4 s.d." | table_cell | YES |
| appendix.tex:53 | 788.4 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:53 | 4.0 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:54 (Gen 8) | 455.8 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:54 | 1.1 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:54 | 2246.1 | "SLV mean" | table_cell | YES |
| appendix.tex:54 | 7.4 | "SLV s.d." | table_cell | YES |
| appendix.tex:54 | 46.90 | "PPL mean" | table_cell | YES |
| appendix.tex:54 | 2.41 | "PPL s.d." | table_cell | YES |
| appendix.tex:54 | .311 | "HeSw mean" | table_cell | YES |
| appendix.tex:54 | .005 | "HeSw s.d." | table_cell | YES |
| appendix.tex:54 | .337 | "D-4 mean" | table_cell | YES |
| appendix.tex:54 | .137 | "D-4 s.d." | table_cell | YES |
| appendix.tex:54 | 806.4 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:54 | 8.0 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:55 (Gen 9) | 446.6 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:55 | 2.1 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:55 | 2210.4 | "SLV mean" | table_cell | YES |
| appendix.tex:55 | 23.1 | "SLV s.d." | table_cell | YES |
| appendix.tex:55 | 58.56 | "PPL mean" | table_cell | YES |
| appendix.tex:55 | 4.52 | "PPL s.d." | table_cell | YES |
| appendix.tex:55 | .301 | "HeSw mean" | table_cell | YES |
| appendix.tex:55 | .003 | "HeSw s.d." | table_cell | YES |
| appendix.tex:55 | .316 | "D-4 mean" | table_cell | YES |
| appendix.tex:55 | .148 | "D-4 s.d." | table_cell | YES |
| appendix.tex:55 | 841.1 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:55 | 23.6 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:56 (Gen 10) | 438.1 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:56 | 4.8 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:56 | 2181.4 | "SLV mean" | table_cell | YES |
| appendix.tex:56 | 28.3 | "SLV s.d." | table_cell | YES |
| appendix.tex:56 | 70.99 | "PPL mean" | table_cell | YES |
| appendix.tex:56 | 5.56 | "PPL s.d." | table_cell | YES |
| appendix.tex:56 | .296 | "HeSw mean" | table_cell | YES |
| appendix.tex:56 | .006 | "HeSw s.d." | table_cell | YES |
| appendix.tex:56 | .324 | "D-4 mean" | table_cell | YES |
| appendix.tex:56 | .150 | "D-4 s.d." | table_cell | YES |
| appendix.tex:56 | 874.6 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:56 | 44.2 | "$\sigma_1$ s.d." | table_cell | YES |

### Appendix Table: Per-gen variance (r=0.2), tab:pergen_variance_r02

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| appendix.tex:73 (Gen 0) | 417.5 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:73 | 0.0 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:73 | 2366.7 | "SLV mean" | table_cell | YES |
| appendix.tex:73 | 0.0 | "SLV s.d." | table_cell | YES |
| appendix.tex:73 | 9.55 | "PPL mean" | table_cell | YES |
| appendix.tex:73 | 0.00 | "PPL s.d." | table_cell | YES |
| appendix.tex:73 | .738 | "D-4 mean" | table_cell | YES |
| appendix.tex:73 | .006 | "D-4 s.d." | table_cell | YES |
| appendix.tex:73 | 1942.8 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:73 | 0.0 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:74 (Gen 1) | 476.2 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:74 | 0.8 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:74 | 2367.4 | "SLV mean" | table_cell | YES |
| appendix.tex:74 | 2.1 | "SLV s.d." | table_cell | YES |
| appendix.tex:74 | 10.28 | "PPL mean" | table_cell | YES |
| appendix.tex:74 | 0.00 | "PPL s.d." | table_cell | YES |
| appendix.tex:74 | .671 | "D-4 mean" | table_cell | YES |
| appendix.tex:74 | .015 | "D-4 s.d." | table_cell | YES |
| appendix.tex:74 | 961.8 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:74 | 1.1 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:75 (Gen 2) | 481.7 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:75 | 1.4 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:75 | 2359.4 | "SLV mean" | table_cell | YES |
| appendix.tex:75 | 1.5 | "SLV s.d." | table_cell | YES |
| appendix.tex:75 | 10.74 | "PPL mean" | table_cell | YES |
| appendix.tex:75 | 0.01 | "PPL s.d." | table_cell | YES |
| appendix.tex:75 | .519 | "D-4 mean" | table_cell | YES |
| appendix.tex:75 | .037 | "D-4 s.d." | table_cell | YES |
| appendix.tex:75 | 879.2 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:75 | 10.3 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:76 (Gen 3) | 486.7 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:76 | 0.3 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:76 | 2364.6 | "SLV mean" | table_cell | YES |
| appendix.tex:76 | 1.8 | "SLV s.d." | table_cell | YES |
| appendix.tex:76 | 11.14 | "PPL mean" | table_cell | YES |
| appendix.tex:76 | 0.01 | "PPL s.d." | table_cell | YES |
| appendix.tex:76 | .471 | "D-4 mean" | table_cell | YES |
| appendix.tex:76 | .006 | "D-4 s.d." | table_cell | YES |
| appendix.tex:76 | 811.9 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:76 | 9.6 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:77 (Gen 4) | 489.6 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:77 | 0.6 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:77 | 2377.9 | "SLV mean" | table_cell | YES |
| appendix.tex:77 | 1.2 | "SLV s.d." | table_cell | YES |
| appendix.tex:77 | 11.49 | "PPL mean" | table_cell | YES |
| appendix.tex:77 | 0.00 | "PPL s.d." | table_cell | YES |
| appendix.tex:77 | .429 | "D-4 mean" | table_cell | YES |
| appendix.tex:77 | .026 | "D-4 s.d." | table_cell | YES |
| appendix.tex:77 | 779.2 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:77 | 9.2 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:78 (Gen 5) | 492.6 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:78 | 0.5 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:78 | 2396.8 | "SLV mean" | table_cell | YES |
| appendix.tex:78 | 1.8 | "SLV s.d." | table_cell | YES |
| appendix.tex:78 | 11.83 | "PPL mean" | table_cell | YES |
| appendix.tex:78 | 0.00 | "PPL s.d." | table_cell | YES |
| appendix.tex:78 | .420 | "D-4 mean" | table_cell | YES |
| appendix.tex:78 | .037 | "D-4 s.d." | table_cell | YES |
| appendix.tex:78 | 748.8 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:78 | 9.3 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:79 (Gen 6) | 495.5 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:79 | 1.2 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:79 | 2417.7 | "SLV mean" | table_cell | YES |
| appendix.tex:79 | 10.5 | "SLV s.d." | table_cell | YES |
| appendix.tex:79 | 12.17 | "PPL mean" | table_cell | YES |
| appendix.tex:79 | 0.02 | "PPL s.d." | table_cell | YES |
| appendix.tex:79 | .413 | "D-4 mean" | table_cell | YES |
| appendix.tex:79 | .070 | "D-4 s.d." | table_cell | YES |
| appendix.tex:79 | 749.7 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:79 | 22.5 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:80 (Gen 7) | 496.7 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:80 | 1.2 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:80 | 2429.0 | "SLV mean" | table_cell | YES |
| appendix.tex:80 | 6.4 | "SLV s.d." | table_cell | YES |
| appendix.tex:80 | 12.49 | "PPL mean" | table_cell | YES |
| appendix.tex:80 | 0.05 | "PPL s.d." | table_cell | YES |
| appendix.tex:80 | .379 | "D-4 mean" | table_cell | YES |
| appendix.tex:80 | .096 | "D-4 s.d." | table_cell | YES |
| appendix.tex:80 | 750.9 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:80 | 30.6 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:81 (Gen 8) | 499.8 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:81 | 2.3 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:81 | 2442.4 | "SLV mean" | table_cell | YES |
| appendix.tex:81 | 10.3 | "SLV s.d." | table_cell | YES |
| appendix.tex:81 | 12.82 | "PPL mean" | table_cell | YES |
| appendix.tex:81 | 0.12 | "PPL s.d." | table_cell | YES |
| appendix.tex:81 | .365 | "D-4 mean" | table_cell | YES |
| appendix.tex:81 | .119 | "D-4 s.d." | table_cell | YES |
| appendix.tex:81 | 753.9 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:81 | 23.4 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:82 (Gen 9) | 503.8 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:82 | 1.2 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:82 | 2456.0 | "SLV mean" | table_cell | YES |
| appendix.tex:82 | 6.3 | "SLV s.d." | table_cell | YES |
| appendix.tex:82 | 13.18 | "PPL mean" | table_cell | YES |
| appendix.tex:82 | 0.18 | "PPL s.d." | table_cell | YES |
| appendix.tex:82 | .349 | "D-4 mean" | table_cell | YES |
| appendix.tex:82 | .143 | "D-4 s.d." | table_cell | YES |
| appendix.tex:82 | 738.1 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:82 | 37.6 | "$\sigma_1$ s.d." | table_cell | YES |
| appendix.tex:83 (Gen 10) | 508.1 | "$r_{\text{eff}}$ mean" | table_cell | YES |
| appendix.tex:83 | 2.8 | "$r_{\text{eff}}$ s.d." | table_cell | YES |
| appendix.tex:83 | 2467.2 | "SLV mean" | table_cell | YES |
| appendix.tex:83 | 12.0 | "SLV s.d." | table_cell | YES |
| appendix.tex:83 | 13.54 | "PPL mean" | table_cell | YES |
| appendix.tex:83 | 0.25 | "PPL s.d." | table_cell | YES |
| appendix.tex:83 | .324 | "D-4 mean" | table_cell | YES |
| appendix.tex:83 | .171 | "D-4 s.d." | table_cell | YES |
| appendix.tex:83 | 722.7 | "$\sigma_1$ mean" | table_cell | YES |
| appendix.tex:83 | 26.6 | "$\sigma_1$ s.d." | table_cell | YES |

### Appendix Table: Alpha robustness, tab:alpha_robustness

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| appendix.tex:99 (alpha=0.3) | 0.3 | "$\alpha$ = 0.3" | hyperparameter | NO |
| appendix.tex:99 | .0141 | "$r{=}0$, $\alpha$=0.3" | table_cell | YES |
| appendix.tex:99 | .0009 | "$r{=}0.2$, $\alpha$=0.3" | table_cell | YES |
| appendix.tex:99 | .0003 | "$r{=}0.25$, $\alpha$=0.3" | table_cell | YES |
| appendix.tex:99 | 0 | "$r{=}0.3$, $\alpha$=0.3" | table_cell | YES |
| appendix.tex:99 | 0 | "$r{=}0.5$, $\alpha$=0.3" | table_cell | YES |
| appendix.tex:100 (alpha=0.5) | 0.5 | "$\alpha$ = 0.5" | hyperparameter | NO |
| appendix.tex:100 | .0171 | "$r{=}0$, $\alpha$=0.5" | table_cell | YES |
| appendix.tex:100 | .0016 | "$r{=}0.2$, $\alpha$=0.5" | table_cell | YES |
| appendix.tex:100 | .0005 | "$r{=}0.25$, $\alpha$=0.5" | table_cell | YES |
| appendix.tex:100 | 0 | "$r{=}0.3$, $\alpha$=0.5" | table_cell | YES |
| appendix.tex:100 | 0 | "$r{=}0.5$, $\alpha$=0.5" | table_cell | YES |
| appendix.tex:101 (alpha=0.7) | 0.7 | "$\alpha$ = 0.7" | hyperparameter | NO |
| appendix.tex:101 | .0183 | "$r{=}0$, $\alpha$=0.7" | table_cell | YES |
| appendix.tex:101 | .0023 | "$r{=}0.2$, $\alpha$=0.7" | table_cell | YES |
| appendix.tex:101 | .0005 | "$r{=}0.25$, $\alpha$=0.7" | table_cell | YES |
| appendix.tex:101 | 0 | "$r{=}0.3$, $\alpha$=0.7" | table_cell | YES |
| appendix.tex:101 | 0 | "$r{=}0.5$, $\alpha$=0.7" | table_cell | YES |

### Appendix: Training and compute details

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| appendix.tex:111 | 5e-5 | "lr $5 \times 10^{-5}$" | hyperparameter | NO |
| appendix.tex:111 | 0.01 | "weight decay 0.01" | hyperparameter | NO |
| appendix.tex:111 | 5 | "linear warmup 5\%" | hyperparameter | NO |
| appendix.tex:111 | 32 | "effective batch size 32" | hyperparameter | NO |
| appendix.tex:111 | 1 | "one epoch per generation" | hyperparameter | NO |
| appendix.tex:111 | 1.0 | "gradient clipping at max norm 1.0" | hyperparameter | NO |
| appendix.tex:112 | 1.0 | "temperature 1.0" | hyperparameter | NO |
| appendix.tex:112 | 50 | "top-$k{=}50$" | hyperparameter | NO |
| appendix.tex:112 | 512 | "max length 512" | hyperparameter | NO |
| appendix.tex:113 | 96 | "96\,GB" | experiment_config | NO |
| appendix.tex:113 | 10 | "10-generation pipeline" | experiment_config | NO |
| appendix.tex:113 | 15 | "15--26 single-GPU hours" | experiment_config | YES |
| appendix.tex:113 | 26 | "15--26 single-GPU hours" | experiment_config | YES |
| appendix.tex:113 | 220 | "approximately 220 GPU-hours" | experiment_config | YES |

## main.tex

| Location | Number | Context | Category | Needs_Tracing |
|---|---|---|---|---|
| main.tex:1 | 11 | "documentclass[11pt]" | other | NO |

---

**Summary statistics:**
- Total unique numerical values extracted: ~480+ entries
- Values requiring source tracing (Needs_Tracing = YES): ~310 entries
- Tables covered: Table 1 (tab:phase0, 30 cells), Table 2 (tab:ews_main, 8 rows), Table 3 (tab:phase_summary, 35 cells), Table 4 (tab:cross_arch, 12 cells), Table 5 (tab:related_comparison, 6 cells), Appendix Table tab:ews_comparison (8 rows), Appendix Table tab:pergen_variance (66 cells), Appendix Table tab:pergen_variance_r02 (55 cells), Appendix Table tab:alpha_robustness (15 cells)
- Key claims requiring verification: abstract's "3.3 pp" HellaSwag drop, "11.6% SLV decline", "2468 peak", all per-generation table values, cross-architecture GPT-2 numbers, controller signal magnitudes (40.4, 3.8), 1B pilot numbers (2835, 2906, 2865, 580.9, 570.8), compute hours (220), and all derived percentages (+18.8%, +4.3%, -11.7%, -55.1%, +643%, +2028%, etc.)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49f46938-5881-4559-9907-a99146ba3af9",
  "isSidechain": true,
  "agentId": "a0f694476b0992be3",
  "requestId": "req_011CbPrjRGhzBJLs5mrsHqsh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e95eb493-0233-4fcc-8b19-9805d2023dc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/agent_420bdecf",
  "sessionId": "179c36d6-e721-43e5-97b5-e8295cc66c2f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGBfhhArpKgkj6nKXf3z2t",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 49031,
      "output_tokens": 23514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1431
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 23514,
          "cache_read_input_tokens": 49031,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1431,
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
