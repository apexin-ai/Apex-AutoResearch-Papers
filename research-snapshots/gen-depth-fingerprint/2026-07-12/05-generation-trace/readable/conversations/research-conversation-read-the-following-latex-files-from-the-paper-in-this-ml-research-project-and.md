# Research conversation: Read the following LaTeX files from the paper in this ML research project and extract EVERY numerical value (percentages

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a0b7e1d09f9ad6ef8.jsonl`
- **Structured JSON:** [`01c961cdf7fc4ac08365.json`](../../sessions/01/01c961cdf7fc4ac08365.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-25T20:38:14.205Z_

Read the following LaTeX files from the paper in this ML research project and extract EVERY numerical value (percentages, F1 scores, accuracy, counts, ratios, p-values, effect sizes, etc.) along with its context. For each number, note: (1) which file/line it appears in, (2) the exact value, (3) what it claims to measure.

Files to read (all under /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/):
- abstract.tex
- introduction.tex
- method.tex
- results.tex
- discussion.tex
- conclusion.tex
- limitations.tex

Return a structured list of ALL numbers found, grouped by file. Be exhaustive - don't skip any numerical claim. Include line numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "a0b7e1d09f9ad6ef8",
  "type": "user",
  "uuid": "ce4de2c2-1071-40ff-8d1c-ac6a65e46b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T20:38:14.212Z_

```json
{
  "parentUuid": "ce4de2c2-1071-40ff-8d1c-ac6a65e46b33",
  "isSidechain": true,
  "agentId": "a0b7e1d09f9ad6ef8",
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
      "mcp__agent-ml-research__add_constraint",
      "mcp__agent-ml-research__approve_experiment",
      "mcp__agent-ml-research__approve_secret_request",
      "mcp__agent-ml-research__archive_project",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_agent_queue_item",
      "mcp__agent-ml-research__cancel_pending_director_messages",
      "mcp__agent-ml-research__check_credentials",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__complete_mvp",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__create_project",
      "mcp__agent-ml-research__delete_secret",
      "mcp__agent-ml-research__director_allocate_gpus",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_main_agent",
      "mcp__agent-ml-research__director_post_to_manager",
      "mcp__agent-ml-research__director_post_to_paper_agent",
      "mcp__agent-ml-research__director_reply_to_user",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__dream_simulate",
      "mcp__agent-ml-research__feishu_read_chat_history",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__feishu_upload_file",
      "mcp__agent-ml-research__get_agent_queue_status",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_dream_status",
      "mcp__agent-ml-research__get_dream_trend",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_project_status",
      "mcp__agent-ml-research__get_resource_inventory",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__keepalive_respond",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_projects",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_secrets",
      "mcp__agent-ml-research__list_ssh_hosts",
      "mcp__agent-ml-research__list_workspace_projects",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__log_decision",
      "mcp__agent-ml-research__log_mistake",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__post_to_reviewer",
      "mcp__agent-ml-research__ralph_respond",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_server",
      "mcp__agent-ml-research__reject_experiment",
      "mcp__agent-ml-research__reject_secret_request",
      "mcp__agent-ml-research__remove_constraint",
      "mcp__agent-ml-research__remove_server",
      "mcp__agent-ml-research__replace_agent_queue",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__research_director_post_to_study_director",
      "mcp__agent-ml-research__should_skip_dream",
      "mcp__agent-ml-research__store_secret",
      "mcp__agent-ml-research__submit_paper_to_review",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_project_config",
      "mcp__agent-ml-research__update_review_issues",
      "mcp__agent-ml-research__update_roadmap",
      "mcp__agent-ml-research__update_skill",
      "mcp__agent-ml-research__upgrade_to_dual_group",
      "mcp__agent-ml-research__urgent_agent_message"
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
      "mcp__agent-ml-research__add_constraint",
      "mcp__agent-ml-research__approve_experiment",
      "mcp__agent-ml-research__approve_secret_request",
      "mcp__agent-ml-research__archive_project",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_agent_queue_item",
      "mcp__agent-ml-research__cancel_pending_director_messages",
      "mcp__agent-ml-research__check_credentials",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__complete_mvp",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__create_project",
      "mcp__agent-ml-research__delete_secret",
      "mcp__agent-ml-research__director_allocate_gpus",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_main_agent",
      "mcp__agent-ml-research__director_post_to_manager",
      "mcp__agent-ml-research__director_post_to_paper_agent",
      "mcp__agent-ml-research__director_reply_to_user",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__dream_simulate",
      "mcp__agent-ml-research__feishu_read_chat_history",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__feishu_upload_file",
      "mcp__agent-ml-research__get_agent_queue_status",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_dream_status",
      "mcp__agent-ml-research__get_dream_trend",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_project_status",
      "mcp__agent-ml-research__get_resource_inventory",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__keepalive_respond",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_projects",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_secrets",
      "mcp__agent-ml-research__list_ssh_hosts",
      "mcp__agent-ml-research__list_workspace_projects",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__log_decision",
      "mcp__agent-ml-research__log_mistake",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__post_to_reviewer",
      "mcp__agent-ml-research__ralph_respond",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_server",
      "mcp__agent-ml-research__reject_experiment",
      "mcp__agent-ml-research__reject_secret_request",
      "mcp__agent-ml-research__remove_constraint",
      "mcp__agent-ml-research__remove_server",
      "mcp__agent-ml-research__replace_agent_queue",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__research_director_post_to_study_director",
      "mcp__agent-ml-research__should_skip_dream",
      "mcp__agent-ml-research__store_secret",
      "mcp__agent-ml-research__submit_paper_to_review",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_project_config",
      "mcp__agent-ml-research__update_review_issues",
      "mcp__agent-ml-research__update_roadmap",
      "mcp__agent-ml-research__update_skill",
      "mcp__agent-ml-research__upgrade_to_dual_group",
      "mcp__agent-ml-research__urgent_agent_message"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "345b6c8d-6669-4dc5-b35f-eb57c169e828",
  "timestamp": "2026-05-25T20:38:14.212Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-25T20:38:23.549Z_



I'll read all seven LaTeX files to extract every numerical value.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "345b6c8d-6669-4dc5-b35f-eb57c169e828",
  "isSidechain": true,
  "agentId": "a0b7e1d09f9ad6ef8",
  "requestId": "req_011CbPvxZKUH5W4DYZWbCAMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e74c1219-ce41-4442-9937-3c48adb43790",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxxoxQPipPofbvDCX13DRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34357,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34357,
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

_source line 4 · 2026-05-25T20:38:24.154Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LXNYwLMosUFt16GBxx5a4A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e74c1219-ce41-4442-9937-3c48adb43790",
  "isSidechain": true,
  "agentId": "a0b7e1d09f9ad6ef8",
  "requestId": "req_011CbPvxZKUH5W4DYZWbCAMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbccd030-aeda-442d-b059-8a5379ff3f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxxoxQPipPofbvDCX13DRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34357,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34357,
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

_source line 5 · 2026-05-25T20:38:24.175Z_

<details><summary>↩ Tool result · `toolu_01LXNYwLMosUFt16GBxx5a4A`</summary>

```text
1	% Abstract — Depth Profiling of Recursive LLM Generation Chains
2	\begin{abstract}
3	As large language model (LLM) outputs re-enter training corpora and seed further generation, understanding how recursive generation reshapes text distributions is critical for data provenance and corpus curation. Existing detectors answer only the binary human-or-machine question, ignoring \emph{generation depth}; we introduce \emph{depth profiling} to address this gap.
4	We decompose distributional drift under recursive generation into location and shape components. Across eight base-model generators from five families, negative log-likelihood (NLL) location features drift monotonically with depth (effect size $d{=}0.74$--$1.05$) while three shape features remain near-stationary ($d < 0.10$), with entropy std intermediate ($d{=}0.46$). We term this ${\geq}8{\times}$ effect-size gap the \emph{differential depth response} (DDR).
5	Prior work documents \emph{what converges}; the central finding here is \emph{what is approximately preserved}: shape stability complements location drift for ordinal depth grading without per-generator calibration. A lightweight ensemble achieves leak-free binary F1\,=\,0.694 (gen-1 vs.\ gen-2+) and 3-class F1\,=\,0.762 under 8-generator leave-one-generator-out evaluation; cross-model chains (5 generators) reach binary F1\,=\,0.830 (gen-0 seeds shared across generators; \S\ref{sec:generation}).
6	Instruction tuning compresses DDR and bounds current applicability to base models\footnote{Code and data are available at \url{https://anonymous.4open.science/r/gen-depth-fingerprint-3FB3/}.}.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbccd030-aeda-442d-b059-8a5379ff3f7b",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "a0b7e1d09f9ad6ef8",
  "type": "user",
  "uuid": "f909a512-aebb-42ab-9e6f-10b9b495ffa7",
  "sourceToolAssistantUUID": "fbccd030-aeda-442d-b059-8a5379ff3f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T20:38:24.530Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tvc4AvbGLVvJk5uLSktMMM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f909a512-aebb-42ab-9e6f-10b9b495ffa7",
  "isSidechain": true,
  "agentId": "a0b7e1d09f9ad6ef8",
  "requestId": "req_011CbPvxZKUH5W4DYZWbCAMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5e05f76-1c1d-46bb-8bb0-a9d32a694c3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxxoxQPipPofbvDCX13DRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34357,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34357,
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

_source line 7 · 2026-05-25T20:38:24.534Z_

<details><summary>↩ Tool result · `toolu_01Tvc4AvbGLVvJk5uLSktMMM`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1 An estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}. As these outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{generation depths}; each successive cycle reshapes distributional properties in ways that matter for data provenance, corpus auditing, and contamination monitoring in base-model pretraining corpora \cite{ccnet,dsir} as well as model collapse analysis \cite{curse_of_recursion,strong_model_collapse}. Understanding \emph{how} recursive generation alters text distributions, and which properties change versus which are preserved, is therefore a prerequisite for principled corpus curation, yet current methods address only binary human-or-machine detection \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Base models provide the cleanest substrate to isolate depth effects from alignment-induced changes.
6	We find that recursive generation produces a decomposable depth profile: distributional \emph{location} drifts with depth while \emph{shape} remains stable across generators, an asymmetry sufficient for cross-generator depth prediction.
7	
8	\looseness=-1 Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}, yet existing analyses characterize \emph{that} and \emph{why} convergence occurs without decomposing what drifts from what is preserved.
9	We introduce \emph{depth profiling} (coarse ordinal classification into gen-0\,/\,gen-1\,/\,gen-2+), and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy\footnote{Throughout, ``entropy'' denotes per-token NLL under the reference model (Pythia-410M), not information-theoretic entropy; see \S\ref{sec:features}.}, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains ${\geq}8{\times}$ more stable (effect size $d{=}0.74$--$1.05$ vs.\ $d < 0.10$ for three near-stationary features; entropy std is intermediate at $d{=}0.46$; boundary features show additional nuance; convergent effect-size measures confirm this partition).
10	We term this location/shape asymmetry the \emph{differential depth response} (DDR; Figure~\ref{fig:ddr-trajectory}), an empirical regularity of base-model autoregressive generation that is mechanistically distinct from model collapse \cite{curse_of_recursion}. Model collapse erodes tail coverage via weight updates; DDR instead analyzes fixed-parameter inference chains.
11	The stationary shape component complements location drift for depth prediction without per-generator calibration.
12	
13	\begin{figure*}[t!]
14	\centering
15	\includegraphics[width=\textwidth]{fig_ddr_trajectory.pdf}
16	\caption{Feature trajectories across generation depth ($y$-axis: $z$-scored feature values). \textbf{Top row (drifting)}: entropy mean and hapax ratio decline monotonically across all eight generators ($|\rho| > 0.59$). \textbf{Bottom row (stationary)}: entropy max and tail decay remain flat ($|\rho| < 0.07$). Colored lines: individual generators; diamonds: cross-generator mean (red for drifting, blue for stationary). This dichotomy defines the DDR.}
17	\label{fig:ddr-trajectory}
18	\end{figure*}
19	We focus on base (pretrained) models; instruction tuning degrades depth signal (Appendix~\ref{app:instruct}).
20	Figure~\ref{fig:framework} summarizes the pipeline: recursive generation chains (\S\ref{sec:generation}), feature extraction with DDR partitioning (\S\ref{sec:features}), and leave-one-generator-out evaluation (\S\ref{sec:evaluation}).
21	
22	\looseness=-1 As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 (macro-averaged LOGO; pooled: 0.705), matching multi-detector ensembles (0.708) at ${\sim}2.4\times$ lower cost; an end-to-end QLoRA \cite{qlora} (Quantized Low-Rank Adaptation) classifier reaches 3-class F1\,=\,0.905 (within-model 5-fold CV; Appendix~\ref{app:qlora}), and the depth signal thus extends well beyond handcrafted features.
23	
24	Our contributions:
25	\begin{enumerate}[nosep,leftmargin=*]
26	    \item \textbf{Empirical decomposition (DDR).} Across eight generators from five families, we decompose inference-chain drift into two primary response zones (drifting, $d{=}0.74$--$1.05$; near-stationary, $d < 0.10$) plus one intermediate feature ($d{=}0.46$). Where prior work documents \emph{what converges} \cite{curious_decline,markovian_chains}, DDR identifies \emph{what is approximately preserved}, an empirical regularity with analytical utility for depth classification without per-generator calibration. DDR is a descriptive empirical finding; the classification value lies in this decomposition rather than the classifier itself.
27	    \item \textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B; exploratory evidence extends to 14B, Appendix~\ref{app:9gen-scale}), with leave-one-generator-out cross-validation as the primary evaluation protocol.
28	    \item \textbf{Scope characterization.} Systematic evaluation across temperature, prompt type, instruction tuning, model scale, domain transfer, and perturbation robustness maps the operational envelope of depth profiling.
29	\end{enumerate}
30	
31	\begin{figure*}[t]
32	\centering
33	\includegraphics[width=\textwidth]{fig2_framework.pdf}
34	\caption{Depth profiling pipeline. (a)~Human seeds are iteratively fed through generator $G$ to produce chains of increasing depth. (b)~Seven features extracted from NLL distributions group into three DDR zones: drifting (red), intermediate (purple), near-stationary (blue). (c)~LOGO evaluation holds out one generator for testing.}
35	\label{fig:framework}
36	\end{figure*}
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5e05f76-1c1d-46bb-8bb0-a9d32a694c3b",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "a0b7e1d09f9ad6ef8",
  "type": "user",
  "uuid": "f588cfc9-1609-4039-b1a9-f8c253ad45b3",
  "sourceToolAssistantUUID": "c5e05f76-1c1d-46bb-8bb0-a9d32a694c3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T20:38:25.004Z_

<details open><summary>🔧 Tool call — Read · `toolu_016KTry1cjRGxu4j42wQ1aKE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f588cfc9-1609-4039-b1a9-f8c253ad45b3",
  "isSidechain": true,
  "agentId": "a0b7e1d09f9ad6ef8",
  "requestId": "req_011CbPvxZKUH5W4DYZWbCAMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39e67a01-c3a7-422c-89de-d6dccd055cba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxxoxQPipPofbvDCX13DRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34357,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34357,
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

_source line 9 · 2026-05-25T20:38:25.018Z_

<details><summary>↩ Tool result · `toolu_016KTry1cjRGxu4j42wQ1aKE`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{table}[t!]
5	\centering
6	\footnotesize
7	\caption{Seven distributional features. ``Entropy'' features are per-token NLL under Pythia-410M (\S\ref{sec:features}); surface features require no reference model. DDR analysis (\S\ref{sec:results-differential}) reveals entropy mean, TTR, and hapax ratio drift with depth while entropy max, min, and tail decay remain near-stationary; entropy std is intermediate.}
8	\label{tab:features}
9	\setlength{\tabcolsep}{4pt}
10	\begin{tabular}{@{}llp{3.0cm}@{}}
11	\toprule
12	\textbf{Feature} & \textbf{Source} & \textbf{Measures} \\
13	\midrule
14	\texttt{entropy\_mean} \textit{\scriptsize(NLL)} & Ref.\ NLL & Central tendency of token surprise \\
15	\texttt{entropy\_std} \textit{\scriptsize(NLL)}  & Ref.\ NLL & Spread of token surprise \\
16	\texttt{entropy\_max} \textit{\scriptsize(NLL)}  & Ref.\ NLL & Maximum token surprise \\
17	\texttt{entropy\_min} \textit{\scriptsize(NLL)}  & Ref.\ NLL & Minimum token surprise \\
18	\texttt{tail\_decay}   & Ref.\ NLL & Log-prob decay slope (ranks 100--1K) \\
19	\midrule
20	\texttt{ttr}           & Surface & Type-token ratio \\
21	\texttt{hapax\_ratio}  & Surface & Proportion of hapax legomena \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\subsection{Task Formulation}
27	\label{sec:task}
28	
29	Given a text $x$, we predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$: human-written ($d{=}0$), first-generation LLM output ($d{=}1$), or text produced by two or more recursive LLM generations ($d{=}2{+}$).
30	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$ (human corpus), $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic autoregressive generation.
31	Depths beyond 2 are merged into $2{+}$ because feature convergence compresses inter-class margins at deeper levels (\S\ref{sec:results-differential}).
32	
33	\subsection{Generation Chain Construction}
34	\label{sec:generation}
35	
36	\looseness=-1 We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
37	\looseness=-1 These span a 13$\times$ parameter range (0.6B--8B) across five architectures; Qwen's overrepresentation (3/8) is a limitation mitigated by LOFO (F1\,=\,0.686; \S\ref{sec:results-classification}).
38	
39	\looseness=-1 For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
40	The same seed pool serves as gen-0 for all generators, controlling for input content; in LOGO evaluation this creates a potential train--test overlap for gen-0, addressed by our binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
41	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
42	We generate up to depth~4 to empirically confirm convergence: 5-class LOGO yields macro F1\,$\approx$\,0.50, with depths 2--4 near-indistinguishable (gen-2/gen-3 per-class F1\,$<$\,0.27; Appendix~\ref{app:finer-depth}). This motivates the gen-2+ class collapse.
43	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
44	After filtering chain breaks and passages too short for feature extraction, 37{,}058 texts remain across all depths (Appendix~\ref{app:dataset-stats}); depths 2--4 are collapsed into $2{+}$.
45	
46	\subsection{Feature Extraction}
47	\label{sec:features}
48	
49	\paragraph{Terminology.} Throughout this paper, we refer to per-token cross-entropy loss under a fixed reference model as ``entropy'' for conciseness; these are reference-model NLL values, not true information-theoretic entropy of the generating distribution.
50	
51	We use interpretable distributional statistics so that the DDR partition remains transparent; end-to-end neural features improve classification ($+$10.0\,pp; Appendix~\ref{app:qlora}) but obscure the decomposition (LOFO confirms both feature groups contribute independently; Appendix~\ref{app:lofo}).
52	
53	\looseness=-1 We extract seven distributional features per text (Table~\ref{tab:features}), covering the NLL distribution's location, spread, extremes, and tail structure, plus two reference-free surface diversity measures; six additional NLL statistics were rejected for redundancy ($|r| > 0.65$, $\Delta$F1\,$\leq$\,$-0.011$; Appendix~\ref{app:feature-candidate}).
54	
55	\paragraph{Reference-model features.}
56	\looseness=-1 A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
57	Cross-family reference validation (Appendix~\ref{app:cross-ref}) shows F1 spread of only 0.013 across Pythia, OLMo, and Qwen references, so DDR is reference-model agnostic; however, all tested references are causal LMs.
58	From the resulting NLL sequence, we extract five statistics: mean, standard deviation, maximum, and minimum of the token-level NLL, plus tail\_decay (the slope of the vocabulary-level averaged log-probability distribution in ranks 100--1000), which captures the power-law regime where depth-induced compression is most detectable.
59	
60	\paragraph{Surface features.}
61	Two features capture lexical diversity without requiring a reference model: type-token ratio (TTR) and the proportion of words appearing exactly once (hapax\_ratio).
62	
63	\paragraph{Feature complementarity.}
64	These features exhibit a \emph{differential depth response} (DDR), separating into drifting and non-drifting groups (\S\ref{sec:results-differential}; pairwise correlations in Appendix~\ref{sec:appendix-feature-correlation}).
65	TTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.
66	
67	\subsection{Evaluation Protocol}
68	\label{sec:evaluation}
69	
70	\paragraph{Cross-validation.}
71	\looseness=-1 We evaluate generalization via \textbf{Leave-One-Generator-Out (LOGO)} cross-validation: each fold holds out one generator entirely, so the classifier must generalize to a generator absent from training. This constitutes the strictest per-model protocol for assessing deployment against previously unseen generators.
72	LOGO does not isolate family-level effects; \textbf{Leave-One-Family-Out (LOFO)} addresses this by holding out entire model families (binary F1\,=\,0.686; \S\ref{sec:results-classification}).
73	Generator subsets vary across experiments (Appendix~\ref{app:gen-subsets-section}).
74	
75	\paragraph{Classifier.}
76	\looseness=-1 We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$; fixed without tuning), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
77	Alternative classifiers (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}); hyperparameter sensitivity (max\_depth sweep) shows F1 variation $\leq$2.0\,pp, so discriminative power resides in the features, not the classifier.
78	
79	\paragraph{Metrics and statistical testing.}
80	The primary metric is \textbf{macro-averaged F1} over the three depth classes, with 95\% bootstrap confidence intervals (CIs; $n{=}1{,}000$).
81	All $p$-values are two-sided with Bonferroni correction within each family of simultaneous tests.
82	
83	\paragraph{Baselines.}
84	We compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
85	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation to ensure a controlled comparison.
86	
87	\paragraph{Length confound control.}
88	Since TTR and hapax\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\S\ref{sec:results-classification}; Appendix~\ref{app:length}).
89	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39e67a01-c3a7-422c-89de-d6dccd055cba",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "a0b7e1d09f9ad6ef8",
  "type": "user",
  "uuid": "35c553bc-69a4-46fc-a3df-e32956a83a6d",
  "sourceToolAssistantUUID": "39e67a01-c3a7-422c-89de-d6dccd055cba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T20:38:25.485Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UcERD7vpPihx95eHqArmxQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35c553bc-69a4-46fc-a3df-e32956a83a6d",
  "isSidechain": true,
  "agentId": "a0b7e1d09f9ad6ef8",
  "requestId": "req_011CbPvxZKUH5W4DYZWbCAMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22539241-253d-40fc-92d5-9491511c72ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxxoxQPipPofbvDCX13DRw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34357,
      "cache_read_input_tokens": 0,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34357
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 325,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 34357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34357,
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

_source line 11 · 2026-05-25T20:38:25.489Z_

<details><summary>↩ Tool result · `toolu_01UcERD7vpPihx95eHqArmxQ`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{fig_transfer_heatmap.pdf}
7	\caption{Cross-generator $8{\times}8$ transfer matrix (binary F1, gen-1 vs.\ gen-2+). Mean cross-generator F1\,=\,0.810 [95\% CI: 0.796, 0.822]; uniformly high off-diagonal values confirm depth signal transfers across five families without calibration.}
8	\label{fig:transfer-heatmap}
9	\end{figure}
10	
11	\subsection{Depth Classification Performance}
12	\label{sec:results-classification}
13	
14	\looseness=-1 The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}); cross-generator F1 spread of 9.1\,pp captures generator selection uncertainty.
15	This 3-class metric is inflated by shared gen-0 seeds (per-class gen-0 F1\,$\approx$\,0.94; \S\ref{sec:generation}); we therefore report \textbf{leak-free binary F1} (gen-1 vs.\ gen-2+)\,=\,0.694 (CI [0.688, 0.700]) throughout, excluding gen-0 entirely.
16	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B; std.\ dev.\ 0.028), with the primary difficulty at the gen-1\,/\,gen-2+ boundary (Appendix~\ref{app:confusion}).
17	
18	\paragraph{Cross-model generalization.}
19	\looseness=-1 Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]; Appendix~\ref{app:cross-model-detail}) under 5-generator LOGO.\footnote{Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B; generator-level LOGO with bootstrap CIs ($n$\,=\,1{,}000).}
20	Single-generator transfer confirms the signal is not a mixed-chain artifact (mean transfer F1\,=\,0.810, Figure~\ref{fig:transfer-heatmap}; full $8{\times}8$ matrix: Appendix~\ref{app:transfer}; LOFO\,=\,0.686); analysis of variance (ANOVA) confirms generator identity contributes ${<}1$\% of feature variance ($\eta^2_{\text{gen}} \leq 0.009$; Appendix~\ref{app:cross-model-detail}).
21	A scale effect emerges: smaller models achieve higher F1 (Pythia-2.8B: 0.724 vs.\ Mistral-7B: 0.633), partly due to same-family affinity with the Pythia-410M reference (spread $\leq$0.013; \S\ref{sec:results-differential}).
22	An end-to-end QLoRA classifier reaches 3-class F1\,=\,0.905 (within-model 5-fold CV; $+$10.0\,pp; Appendix~\ref{app:qlora}), evidence that additional depth signal resides in token-level representations. On instruct data, QLoRA recovers to 0.89--0.91 (within-model; Appendix~\ref{app:instruct}); the decomposition, not the classifier, is DDR's primary contribution.
23	
24	\paragraph{Confound controls.}
25	\looseness=-1 Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770; Appendix~\ref{app:length}); independent-seed evaluation with disjoint pools (F1\,=\,0.680; Appendix~\ref{app:seed-control}), so the classifier captures generative degradation rather than seed-specific content.
26	
27	\paragraph{Error analysis.}
28	\looseness=-1 The gen-1\,/\,gen-2+ boundary is the primary failure point: depth-2 samples (the shallowest within the 2+ class) exhibit the highest error rate (48.4\%), decreasing monotonically to 20.3\% at depth-4 (Appendix~\ref{app:error-analysis}) due to insufficient accumulated drift beyond the large gen-0$\to$gen-1 distributional shift.
29	Error rates decrease monotonically at deeper generations ($\leq$29.2\% at gen-3+); DDR signal thus strengthens with chain length, and the DDR decomposition is the primary analytical contribution.
30	
31	\begin{table}[t]
32	\centering
33	\footnotesize
34	\caption{8-generator LOGO macro-F1 (bootstrap 95\% CIs, $n$\,=\,1{,}000). Binary F1 excludes gen-0. $^{\dagger}$3-class F1 has upward bias from shared gen-0 seeds; independent-seed controls confirm the signal (F1\,=\,0.680; Appendix~\ref{app:seed-control}).}
35	\label{tab:logo-results}
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{@{}llcccc@{}}
38	\toprule
39	\textbf{Model} & \textbf{Family} & \textbf{Params} & \textbf{Bin F1} & \textbf{95\% CI} & \textbf{3-class F1}$^{\dagger}$ \\
40	\midrule
41	Pythia-2.8B     & Pythia  & 2.8B & \textbf{0.724} & [.707, .742] & 0.798 \\
42	Pythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \textbf{0.806} \\
43	Qwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\
44	Llama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\
45	OLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\
46	Qwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\
47	Qwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\
48	Mistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\
49	\midrule
50	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.694} & [.688, .700] & \textbf{0.762} \\
51	\multicolumn{3}{l}{\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\
52	\bottomrule
53	\end{tabular}}
54	\end{table}
55	
56	\subsection{Differential Depth Response}
57	\label{sec:results-differential}
58	
59	\paragraph{Formal definition.}
60	\looseness=-1 For feature $f$ measured across depths $d \in \{0,1,2{+}\}$, we define its \emph{depth sensitivity} as $\text{DDR}(f) = |\rho(\text{depth}, f)|$, where $\rho$ is Spearman correlation over all per-text measurements.
61	A feature is classified as \emph{drifting} if Cohen's $d > 0.50$ between adjacent depths, or \emph{stationary} if $d < 0.15$; the two-cluster structure is robust across $\varepsilon \in [0.10, 0.75]$ ($k$-means silhouette\,=\,0.660, $p{=}0.030$; exhaustive split enumeration ranks this partition first; independent replication in all eight generators; Appendix~\ref{app:ddr-validation}).
62	\looseness=-1 Recursive inputs grow increasingly self-typical~\citep{markovian_chains}; this predicts location drift with shape invariance (confirmed across nucleus, greedy, and top-$k$ strategies; Appendix~\ref{app:decoding-strategy}).
63	
64	\looseness=-1 Figure~\ref{fig:ddr-trajectory} reveals the dichotomy: central-tendency features (entropy mean, TTR, hapax ratio) decline monotonically with depth, while shape features (entropy max, tail decay, entropy min) remain flat (per-feature distributions: Appendix~\ref{app:feature-distributions}; qualitative chain example: Appendix~\ref{app:qualitative}).
65	The partition is binary ($k{=}2$; silhouette\,=\,0.660), with entropy std as the sole \emph{intermediate} member ($d{=}0.46$, $|\rho|{=}0.16$), distinct from three near-stationary features ($d < 0.10$; Appendix~\ref{app:ddr-validation}).
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
70	\caption{Differential depth response (DDR). Drifting features (red; $|\rho| > 0.60$, effect size $d{=}0.74$--$1.05$) shift monotonically with generation depth; near-stationary features (blue; $d \leq 0.10$) are approximately preserved; entropy std (purple; $d{=}0.46$) is intermediate. Diamonds: cross-generator means; dots: per-generator values.}
71	\label{fig:feature-drift}
72	\end{figure}
73	
74	\looseness=-1 Pooled Spearman correlations corroborate the split: drifting features show $|\rho| > 0.60$ (hapax ratio $-0.64$, TTR $-0.62$, entropy mean $-0.60$) vs.\ $|\rho| \leq 0.16$ for entropy max and tail decay; entropy min reaches $|\rho|{=}0.40$ due to its gen-0/gen-1 boundary sensitivity (discussed below). This persistent magnitude gap defines the DDR partition (Figure~\ref{fig:feature-drift}).
75	
76	\begin{figure}[t]
77	\centering
78	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
79	\caption{LOGO binary F1 vs.\ inference cost (8-gen pooled). The 7-feature ensemble (one 410M model) matches multi-detector ensembles (1.4B total) at ${\sim}2.4\times$ lower cost. RTX 5090 timings.}
80	\label{fig:baseline-ci}
81	\end{figure}
82	
83	\paragraph{Quantification.}
84	\looseness=-1 Cohen's $d$ shows a ${\geq}8{\times}$ gap between drifting ($d{=}0.74$--$1.05$) and near-stationary ($d < 0.10$); KS, Glass's $\Delta$, Cliff's $\delta$ corroborate (Appendix~\ref{app:ddr-validation}).
85	Entropy min and tail decay are \emph{boundary features}: entropy min is near-stationary for gen-1/gen-2+ ($d{=}0.016$) but sensitive at gen-0/gen-1; tail decay passes two one-sided tests (TOST) equivalence (Appendix~\ref{app:tost}) for only 4/8 generators (per-generator $|d|{=}0.07$--$0.22$).
86	\paragraph{Validation.}
87	\looseness=-1 Each hold-out generator independently recovers the identical partition (silhouette 0.505--0.760); TOST confirms near-stationarity for entropy min (8/8) and entropy max (6/8); permutation testing confirms the split as non-random ($p{=}0.030$). Per-feature convergence dynamics (Figure~\ref{fig:convergence}), per-family DDR consistency (Appendix~\ref{app:family-ddr}), and causal feature analysis (Appendix~\ref{app:ddr-causality}) appear in Appendices~\ref{app:ddr-validation}--\ref{app:convergence}.
88	
89	\paragraph{Feature complementarity.}
90	\looseness=-1 The full 7-feature set (F1\,=\,0.773, 10-fold stratified cross-validation) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \approx 0$; Appendix~\ref{app:ablation-table}).
91	Group ablation (10-fold stratified CV) confirms complementarity: 3-class F1 gains $+$5.3\,pp when non-drifting features are added (drifting-only 0.716, all-7 0.769), while binary detection is already saturated by location drift alone (drifting-only 0.697 vs.\ all-7 0.700); shape stability thus contributes to depth \emph{grading}, not detection.
92	TTR and hapax ratio ($r = 0.97$) are retained for marginal LOFO gains (Appendix~\ref{app:lofo}).
93	
94	\paragraph{Cross-family reference models.}
95	\looseness=-1 Alternative references (OLMo-2-1B, Qwen3-0.6B) yield F1 spread of only 0.013 (Appendix~\ref{app:cross-ref}); same-family proximity may inflate Pythia F1 by up to 1.2\,pp, but the DDR partition is preserved.
96	
97	\paragraph{Temperature and prompt-type sensitivity.}
98	\looseness=-1 All four tested generators degrade at $t{=}0.9$ ($-$9.3 to $-$26.0\,pp binary F1; Appendix~\ref{app:sampling-sensitivity}); continuation chains show the strongest drift (F1\,=\,0.781; Appendix~\ref{app:prompt-type}).
99	The DDR partition hierarchy is preserved across temperatures (Appendix~\ref{app:ddr-temp-stability}), including cross-temperature transfer (Appendix~\ref{app:cross-temp}); random word replacement at 10\% degrades binary F1 by only 8\,pp (Appendix~\ref{app:human-edit}).
100	
101	
102	\subsection{Comparison with Detection Baselines}
103	\label{sec:results-baselines}
104	
105	\begin{table}[t]
106	\centering
107	\footnotesize
108	\caption{Depth classification (8-gen LOGO, pooled). Binary F1 excludes gen-0. 7-feature: one 410M model; 4-det ensembles: two models, 1.4B. QLoRA (\S\ref{sec:results-classification}) uses full token sequences (within-model 5-fold CV, not LOGO), serving as an information-asymmetric ceiling.}
109	\label{tab:baselines}
110	\resizebox{\columnwidth}{!}{%
111	\begin{tabular}{lcccc}
112	\toprule
113	\textbf{Method} & \textbf{Feat.} & \textbf{3-class F1} & \textbf{Bin F1} & \textbf{ms/text} \\
114	\midrule
115	4-det.\ + surface     & 6 & \textbf{0.795} & \textbf{0.708} & 22.8 \\
116	4-detector ens.\      & 4 & 0.785 & 0.700 & 22.8 \\
117	7-feature (ours)      & 7 & 0.774 & 0.705 & \textbf{9.7} \\
118	\midrule
119	Avg-LogProb           & 1 & 0.707 & 0.673 & --- \\
120	FastDetectGPT         & 1 & 0.660 & 0.569 & --- \\
121	LD-Score              & 1 & 0.630 & 0.675 & --- \\
122	Binoculars            & 1 & 0.411 & 0.539 & --- \\
123	\bottomrule
124	\end{tabular}}
125	\end{table}
126	
127	\looseness=-1 We next ask whether existing detection methods, designed for binary real-vs-synthetic classification, incidentally capture depth structure, repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\ref{tab:baselines}).
128	The strongest baseline is a 4-detector + surface feature ensemble (binary F1\,=\,0.708), which pools four detection scores with TTR and hapax ratio; among individual detectors, Avg-LogProb provides the most meaningful single-feature comparison.
129	
130	\looseness=-1 The 7-feature ensemble matches the 4-detector+surface ensemble on binary F1 (0.705 vs.\ 0.708; Figure~\ref{fig:baseline-ci}) at ${\sim}2.4\times$ lower cost, though the latter leads by 2.1\,pp on 3-class F1 (0.795 vs.\ 0.774); both surpass individual detectors by 3.0--16.6\,pp.
131	The DDR decomposition explains why depth discrimination is achievable: location features carry the signal and shape features enable cross-generator transfer (\S\ref{sec:discussion}), all with a single 410M reference model; ordinal-specific methods (CORAL, Frank-Hall) yield comparable F1 (Appendix~\ref{app:classifier}).
132	Among individual detectors, LD-Score and Avg-LogProb best capture depth structure (binary F1\,=\,0.675 and 0.673); FastDetectGPT captures 3-class ordering (F1\,=\,0.660) but struggles with binary depth separation (F1\,=\,0.569); Binoculars is least informative (binary F1\,=\,0.539).
133	Concurrent iterative-generation studies use different chain operators and cannot be directly included as depth baselines (Appendix~\ref{app:iterative-comparison}).
134	
135	\begin{figure*}[t]
136	\centering
137	\includegraphics[width=\textwidth]{fig_convergence_dynamics.pdf}
138	\caption{Feature convergence dynamics. (a)~Drifting features (red) and intermediate entropy std (purple): $|d| > 0.46$ by gen-2+. (b)~Near-stationary features (blue): $|d| < 0.25$ at all depths. Shape stability persists across chain lengths.}
139	\label{fig:convergence}
140	\end{figure*}
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22539241-253d-40fc-92d5-9491511c72ff",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "a0b7e1d09f9ad6ef8",
  "type": "user",
  "uuid": "a0dd341f-2505-49cd-8b1a-4576cd2a5aa6",
  "sourceToolAssistantUUID": "22539241-253d-40fc-92d5-9491511c72ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T20:38:49.699Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3BCavJABEWbXN6buZPFrC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0dd341f-2505-49cd-8b1a-4576cd2a5aa6",
  "isSidechain": true,
  "agentId": "a0b7e1d09f9ad6ef8",
  "requestId": "req_011CbPvyPtxqJrs33gx6F7aB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca485189-d306-4312-a27f-a19dcc1933af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2GkyTj8z1DnWf6Q6ZHeHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11292,
      "cache_read_input_tokens": 34357,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11292
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 34357,
          "cache_creation_input_tokens": 11292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11292,
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

### Tool call

_source line 13 · 2026-05-25T20:38:49.703Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QVCA34iUDnhEYkJu5L8UpD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca485189-d306-4312-a27f-a19dcc1933af",
  "isSidechain": true,
  "agentId": "a0b7e1d09f9ad6ef8",
  "requestId": "req_011CbPvyPtxqJrs33gx6F7aB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ed22459-58dc-44eb-a4d9-bdd9f1933c12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2GkyTj8z1DnWf6Q6ZHeHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11292,
      "cache_read_input_tokens": 34357,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11292
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 34357,
          "cache_creation_input_tokens": 11292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11292,
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

### Tool call

_source line 14 · 2026-05-25T20:38:49.706Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V8rWjZDKPVZ1X4NdFBfskC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ed22459-58dc-44eb-a4d9-bdd9f1933c12",
  "isSidechain": true,
  "agentId": "a0b7e1d09f9ad6ef8",
  "requestId": "req_011CbPvyPtxqJrs33gx6F7aB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8016e8a-dad3-4de3-acf3-bcc3acc77824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2GkyTj8z1DnWf6Q6ZHeHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11292,
      "cache_read_input_tokens": 34357,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11292
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 34357,
          "cache_creation_input_tokens": 11292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11292,
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

_source line 15 · 2026-05-25T20:38:49.712Z_

<details><summary>↩ Tool result · `toolu_01Q3BCavJABEWbXN6buZPFrC`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\looseness=-1 DDR reflects monotonic NLL compression under recursive generation (Appendix~\ref{app:nll-distribution}).
5	Shape stability is not trivially predictable from architecture: entropy\_max is bounded by $\log|V|{\approx}10.8$ nats but observed values fall far below this ceiling; tail\_decay lacks an obvious bound yet remains near-stationary ($|d|{=}0.10$--$0.22$); entropy\_std drifts ($d{=}0.46$) despite shared NLL derivation.
6	ANOVA confirms depth explains ${>}48{\times}$ more variance in location than shape features (Appendix~\ref{app:variance-decomposition}).
7	
8	\paragraph{Relationship to model collapse.}
9	\looseness=-1 Model collapse erodes tail coverage via weight updates, and shape features \emph{do} change under retraining \cite{curse_of_recursion,strong_model_collapse}. DDR, by contrast, characterizes fixed-parameter inference where shape remains stable.
10	Shape stability is thus specific to the fixed-parameter regime, not an a priori consequence of architecture; DDR complements concurrent iterative-generation studies (Appendix~\ref{app:iterative-comparison}).
11	
12	\paragraph{Temperature sensitivity.}
13	\looseness=-1 Higher sampling temperature ($\tau > 0.7$) flattens token probability distributions, narrowing NLL variance and diluting the location shift that drifting features capture (\S\ref{sec:results-differential}).
14	The DDR partition hierarchy is preserved across all tested temperatures (Appendix~\ref{app:ddr-temp-stability}), but signal strength is temperature-dependent, bounding current applicability to moderate sampling.
15	
16	\paragraph{Error structure and scope.}
17	\looseness=-1 The gen-1$\to$gen-2+ boundary is the primary failure point (error rate 48.4\%; Appendix~\ref{app:error-analysis}): gen-1 texts retain sufficient diversity to overlap with gen-0; deeper generations show monotonically decreasing error ($\leq$29.2\%), so DDR-based classifiers are most reliable for heavily recycled content.
18	The DDR partition is robust across decoding strategies, temperatures, and reference models (Appendices~\ref{app:decoding-strategy}--\ref{app:cross-ref}).
19	Instruction tuning compresses DDR (Appendix~\ref{app:instruct}), but QLoRA recovery to F1\,=\,0.89--0.91 (within-model) shows the signal persists.
20	Cross-domain (F1\,=\,0.74--0.75; Appendix~\ref{app:domain}) and 9-generator (Appendix~\ref{app:9gen-scale}) evaluations confirm generalization.
21	DDR enables corpus contamination detection and synthetic data pipeline auditing; depth-aware filtering does not improve perplexity (Appendix~\ref{app:downstream}), so DDR identifies \emph{provenance} rather than \emph{fluency degradation}. Finer-grained 5-class classification yields F1\,$\approx$\,0.50 (Appendix~\ref{app:finer-depth}), a resolution limit of three depth classes.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca485189-d306-4312-a27f-a19dcc1933af",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "a0b7e1d09f9ad6ef8",
  "type": "user",
  "uuid": "7905893b-fdbc-49e4-a6fe-1d4a79d0d205",
  "sourceToolAssistantUUID": "ca485189-d306-4312-a27f-a19dcc1933af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T20:38:49.714Z_

<details><summary>↩ Tool result · `toolu_01V8rWjZDKPVZ1X4NdFBfskC`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\looseness=-1 All eight generators are base (pretrained) models with $\leq$8.2B parameters; instruction-tuned variants show substantially degraded depth signal (within-model 3-class F1 drops 3.7--19.9\,pp; Appendix~\ref{app:instruct}), though QLoRA partially recovers (F1\,=\,0.89--0.91, within-model); this pattern is consistent with signal compression rather than elimination.
5	The evaluation assumes English Wikipedia seeds, a fixed decoding regime ($t{=}0.7$, nucleus $p{=}0.9$), and an English-centric reference model (Pythia-410M); cross-temperature transfer is tested (Appendix~\ref{app:cross-temp}) but cross-lingual generalization remains untested.
6	Depth resolution is bounded at three classes (gen-0\,/\,gen-1\,/\,gen-2+); finer-grained 5-class classification yields F1\,$\approx$\,0.50 with deeper depths mutually indistinguishable (Appendix~\ref{app:finer-depth}).
7	DDR signal strength is temperature-dependent; at $\tau{=}0.9$, classification performance degrades substantially ($-$9.3 to $-$26.0\,pp binary F1), and cross-temperature transfer at production scales remains untested.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8016e8a-dad3-4de3-acf3-bcc3acc77824",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "a0b7e1d09f9ad6ef8",
  "type": "user",
  "uuid": "263a2adf-6762-4864-bf77-a321d1010213",
  "sourceToolAssistantUUID": "e8016e8a-dad3-4de3-acf3-bcc3acc77824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T20:38:49.717Z_

<details><summary>↩ Tool result · `toolu_01QVCA34iUDnhEYkJu5L8UpD`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1 Recursive generation produces a decomposable depth response: location features drift monotonically while shape features remain approximately preserved. This asymmetry supports cross-generator depth classification (F1\,=\,0.694--0.762; 5-generator cross-model F1\,=\,0.830) under moderate sampling temperatures ($\tau \leq 0.7$).
5	Instruction tuning compresses DDR, bounding current applicability to base models; QLoRA recovery (F1\,=\,0.89--0.91, within-model) points to tractable extension to instruct settings.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ed22459-58dc-44eb-a4d9-bdd9f1933c12",
  "isSidechain": true,
  "promptId": "9243f9ff-97eb-4b62-8508-cf084c8569d2",
  "agentId": "a0b7e1d09f9ad6ef8",
  "type": "user",
  "uuid": "73a02ebe-d211-46b0-9fc7-cb7d977ae761",
  "sourceToolAssistantUUID": "6ed22459-58dc-44eb-a4d9-bdd9f1933c12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-25T20:40:34.666Z_

Here is the exhaustive extraction of every numerical value from the seven LaTeX files, grouped by file with line numbers.

---

## **abstract.tex**

| Line | Value | Claims to measure |
|------|-------|-------------------|
| 4 | `d = 0.74–1.05` | Cohen's d effect size for NLL location features drifting with depth |
| 4 | `d < 0.10` | Cohen's d for three near-stationary shape features |
| 4 | `d = 0.46` | Cohen's d for entropy std (intermediate feature) |
| 4 | `>=8x` | Effect-size gap ratio between drifting and near-stationary features (the DDR) |
| 5 | `F1 = 0.694` | Leak-free binary F1 (gen-1 vs gen-2+), 8-generator LOGO |
| 5 | `F1 = 0.762` | 3-class F1 under 8-generator LOGO |
| 5 | `5` | Number of generators in cross-model chains |
| 5 | `F1 = 0.830` | Binary F1 for cross-model chains |

---

## **introduction.tex**

| Line | Value | Claims to measure |
|------|-------|-------------------|
| 4 | `7–17%` | Estimated fraction of recent scientific publications with substantial LLM-modified content |
| 9 | `0.6B–8B` | Parameter range of eight base-model generators |
| 9 | `d = 0.74–1.05` | Cohen's d for drifting features (NLL location) |
| 9 | `d < 0.10` | Cohen's d for three near-stationary features |
| 9 | `d = 0.46` | Cohen's d for entropy std (intermediate) |
| 9 | `>=8x` | Effect-size gap between drifting and near-stationary features |
| 16 | `|ρ| > 0.59` | Spearman correlation for drifting features (entropy mean, hapax ratio) |
| 16 | `|ρ| < 0.07` | Spearman correlation for stationary features (entropy max, tail decay) |
| 22 | `F1 = 0.694` | Leak-free binary F1 (macro-averaged LOGO) |
| 22 | `0.705` | Pooled binary F1 |
| 22 | `0.708` | Multi-detector ensemble binary F1 |
| 22 | `~2.4x` | Cost reduction factor vs multi-detector ensemble |
| 22 | `F1 = 0.905` | 3-class F1, end-to-end QLoRA classifier (within-model 5-fold CV) |
| 26 | `d = 0.74–1.05` | Cohen's d for drifting features (reiterated in contributions) |
| 26 | `d < 0.10` | Cohen's d for near-stationary features (reiterated) |
| 26 | `d = 0.46` | Cohen's d for intermediate feature (reiterated) |
| 27 | `37K` | Number of texts in the constructed dataset |
| 27 | `0.6B–8B` | Parameter range of generators (reiterated) |
| 27 | `14B` | Scale of exploratory evidence extension |

---

## **method.tex**

| Line | Value | Claims to measure |
|------|-------|-------------------|
| 18 | `100–1K` (ranks 100–1000) | Rank range for tail_decay log-prob slope computation |
| 29 | `{0, 1, 2+}` | Depth class labels |
| 36 | `2.8B` | Pythia-2.8B parameter count |
| 36 | `1B` | Pythia-1B parameter count |
| 36 | `1.7B` | Qwen3-1.7B parameter count |
| 36 | `0.6B` | Qwen3-0.6B parameter count |
| 36 | `8B` | Qwen3-8B-Base parameter count |
| 36 | `3B` | Llama-3.2-3B parameter count |
| 36 | `7B` | Mistral-7B parameter count |
| 37 | `13x` | Parameter range ratio (0.6B to 8B) |
| 37 | `0.6B–8B` | Parameter range |
| 37 | `3/8` | Qwen overrepresentation (3 out of 8 generators) |
| 37 | `F1 = 0.686` | LOFO binary F1 mitigating Qwen overrepresentation |
| 39 | `1,000` | Approximate number of seed passages per generator |
| 41 | `4` | Maximum generation chain depth (gen-0 through gen-4) |
| 42 | `F1 ≈ 0.50` | 5-class LOGO macro F1 |
| 42 | `F1 < 0.27` | Gen-2/gen-3 per-class F1 in 5-class setting |
| 43 | `τ = 0.7` | Sampling temperature |
| 43 | `p = 0.9` | Nucleus sampling top-p |
| 43 | `256` | Maximum new tokens per generation |
| 44 | `37,058` | Total texts after filtering |
| 51 | `+10.0 pp` | F1 improvement from end-to-end neural features over handcrafted |
| 53 | `|r| > 0.65` | Correlation threshold for rejecting redundant features |
| 53 | `ΔF1 ≤ −0.011` | F1 impact of rejected features |
| 53 | `6` | Number of additional NLL statistics rejected |
| 57 | `0.013` | F1 spread across Pythia, OLMo, Qwen references (cross-ref validation) |
| 58 | `5` (five statistics) | Number of NLL statistics extracted |
| 58 | `100–1000` | Rank range for tail_decay |
| 65 | `r = 0.97` | Correlation between TTR and hapax ratio |
| 72 | `F1 = 0.686` | LOFO binary F1 (reiterated) |
| 76 | `200` | XGBoost n_estimators |
| 76 | `6` | XGBoost max_depth |
| 76 | `0.1` | XGBoost learning rate |
| 77 | `≤2.0 pp` | F1 variation across max_depth sweep |
| 80 | `95%` | Bootstrap confidence interval level |
| 80 | `n = 1,000` | Number of bootstrap resamples |

---

## **results.tex**

| Line | Value | Claims to measure |
|------|-------|-------------------|
| 7 | `8×8` | Transfer matrix dimensions |
| 7 | `F1 = 0.810` | Mean cross-generator transfer F1 (binary) |
| 7 | `CI: [0.796, 0.822]` | 95% CI for mean cross-generator transfer F1 |
| 14 | `F1 = 0.762` | 3-class LOGO F1 |
| 14 | `CI [0.758, 0.766]` | 95% CI for 3-class LOGO F1 |
| 14 | `N = 37,058` | Total sample size |
| 14 | `9.1 pp` | Cross-generator F1 spread |
| 15 | `F1 ≈ 0.94` | Per-class gen-0 F1 (inflated by shared seeds) |
| 15 | `F1 = 0.694` | Leak-free binary F1 (gen-1 vs gen-2+) |
| 15 | `CI [0.688, 0.700]` | 95% CI for leak-free binary F1 |
| 16 | `0.633` | Lowest per-generator binary F1 (Mistral-7B) |
| 16 | `0.724` | Highest per-generator binary F1 (Pythia-2.8B) |
| 16 | `0.028` | Standard deviation of per-generator binary F1 |
| 19 | `F1 = 0.830` | Cross-model chain binary F1 |
| 19 | `CI [.818, .841]` | 95% CI for cross-model chain binary F1 |
| 19 | `n = 1,000` | Bootstrap resamples for cross-model CI |
| 20 | `F1 = 0.810` | Mean single-generator transfer F1 |
| 20 | `0.686` | LOFO F1 |
| 20 | `<1%` | Percentage of feature variance explained by generator identity (ANOVA) |
| 20 | `η²_gen ≤ 0.009` | Eta-squared for generator identity effect |
| 21 | `0.724` | Pythia-2.8B binary F1 |
| 21 | `0.633` | Mistral-7B binary F1 |
| 21 | `≤0.013` | F1 spread across reference models |
| 22 | `F1 = 0.905` | QLoRA 3-class F1 (within-model 5-fold CV) |
| 22 | `+10.0 pp` | F1 gain of QLoRA over handcrafted features |
| 22 | `0.89–0.91` | QLoRA F1 on instruct data (within-model) |
| 25 | `F1 = 0.724` | Length-matched subsampling binary F1 |
| 25 | `0.770` | Original binary F1 before length matching |
| 25 | `F1 = 0.680` | Independent-seed evaluation F1 |
| 28 | `48.4%` | Error rate for depth-2 samples (shallowest in 2+ class) |
| 28 | `20.3%` | Error rate at depth-4 |
| 29 | `≤29.2%` | Error rate at gen-3+ |
| 34 | `n = 1,000` | Bootstrap resamples for Table 2 CIs |
| 34 | `F1 = 0.680` | Independent-seed control F1 (reiterated) |
| 41 | `0.724` | Pythia-2.8B binary F1 (Table 2) |
| 41 | `CI [.707, .742]` | 95% CI for Pythia-2.8B |
| 41 | `0.798` | Pythia-2.8B 3-class F1 |
| 42 | `0.718` | Pythia-1B binary F1 |
| 42 | `CI [.700, .735]` | 95% CI for Pythia-1B |
| 42 | `0.806` | Pythia-1B 3-class F1 |
| 43 | `0.709` | Qwen3-1.7B binary F1 |
| 43 | `CI [.693, .726]` | 95% CI for Qwen3-1.7B |
| 43 | `0.772` | Qwen3-1.7B 3-class F1 |
| 44 | `0.697` | Llama-3.2-3B binary F1 |
| 44 | `CI [.680, .713]` | 95% CI for Llama-3.2-3B |
| 44 | `0.775` | Llama-3.2-3B 3-class F1 |
| 45 | `0.695` | OLMo-2-1B binary F1 |
| 45 | `CI [.679, .711]` | 95% CI for OLMo-2-1B |
| 45 | `0.781` | OLMo-2-1B 3-class F1 |
| 46 | `0.692` | Qwen3-8B binary F1 |
| 46 | `CI [.674, .708]` | 95% CI for Qwen3-8B |
| 46 | `0.714` | Qwen3-8B 3-class F1 |
| 46 | `8.2B` | Qwen3-8B parameter count |
| 47 | `0.691` | Qwen3-0.6B binary F1 |
| 47 | `CI [.673, .709]` | 95% CI for Qwen3-0.6B |
| 47 | `0.780` | Qwen3-0.6B 3-class F1 |
| 48 | `0.633` | Mistral-7B binary F1 |
| 48 | `CI [.617, .648]` | 95% CI for Mistral-7B |
| 48 | `0.682` | Mistral-7B 3-class F1 |
| 48 | `7.0B` | Mistral-7B parameter count |
| 50 | `0.694` | Average 8-gen LOGO binary F1 |
| 50 | `CI [.688, .700]` | 95% CI for average binary F1 |
| 50 | `0.762` | Average 8-gen LOGO 3-class F1 |
| 51 | `0.686` | LOFO family-level binary F1 |
| 61 | `d > 0.50` | Cohen's d threshold for "drifting" classification |
| 61 | `d < 0.15` | Cohen's d threshold for "stationary" classification |
| 61 | `ε ∈ [0.10, 0.75]` | Threshold range over which 2-cluster structure is robust |
| 61 | `0.660` | k-means silhouette score |
| 61 | `p = 0.030` | Permutation test p-value for DDR partition |
| 65 | `k = 2` | Number of clusters in DDR partition |
| 65 | `0.660` | Silhouette score (reiterated) |
| 65 | `d = 0.46` | Cohen's d for entropy std |
| 65 | `|ρ| = 0.16` | Spearman correlation for entropy std |
| 65 | `d < 0.10` | Cohen's d for three near-stationary features |
| 70 | `|ρ| > 0.60` | Spearman correlation threshold for drifting features |
| 70 | `d = 0.74–1.05` | Cohen's d range for drifting features |
| 70 | `d ≤ 0.10` | Cohen's d for near-stationary features |
| 70 | `d = 0.46` | Cohen's d for entropy std (reiterated) |
| 74 | `|ρ| > 0.60` | Pooled Spearman threshold for drifting features |
| 74 | `-0.64` | Hapax ratio Spearman ρ with depth |
| 74 | `-0.62` | TTR Spearman ρ with depth |
| 74 | `-0.60` | Entropy mean Spearman ρ with depth |
| 74 | `|ρ| ≤ 0.16` | Spearman ρ for entropy max and tail decay |
| 74 | `|ρ| = 0.40` | Entropy min Spearman ρ with depth |
| 79 | `~2.4x` | Cost reduction factor (reiterated in figure caption) |
| 84 | `d = 0.74–1.05` | Cohen's d gap, drifting features (reiterated) |
| 84 | `d < 0.10` | Cohen's d, near-stationary (reiterated) |
| 84 | `>=8x` | Gap ratio (reiterated) |
| 85 | `d = 0.016` | Cohen's d for entropy min at gen-1/gen-2+ boundary |
| 85 | `4/8` | Generators passing TOST equivalence for tail decay |
| 85 | `|d| = 0.07–0.22` | Per-generator Cohen's d range for tail decay |
| 87 | `0.505–0.760` | Range of hold-out generator silhouette scores |
| 87 | `8/8` | Generators confirming TOST near-stationarity for entropy min |
| 87 | `6/8` | Generators confirming TOST near-stationarity for entropy max |
| 87 | `p = 0.030` | Permutation test p-value (reiterated) |
| 90 | `F1 = 0.773` | Full 7-feature set F1 (10-fold stratified CV) |
| 90 | `0.688` | Surface-only F1 (10-fold CV) |
| 90 | `0.713` | Reference-only F1 (10-fold CV) |
| 90 | `p ≈ 0` | McNemar test p-value |
| 91 | `+5.3 pp` | 3-class F1 gain from adding non-drifting features |
| 91 | `0.716` | Drifting-only 3-class F1 (10-fold CV) |
| 91 | `0.769` | All-7 3-class F1 (10-fold CV) |
| 91 | `0.697` | Drifting-only binary F1 |
| 91 | `0.700` | All-7 binary F1 |
| 95 | `0.013` | F1 spread across alternative reference models |
| 95 | `1.2 pp` | Maximum same-family proximity F1 inflation for Pythia |
| 98 | `-9.3 to -26.0 pp` | Binary F1 degradation at temperature 0.9 |
| 98 | `F1 = 0.781` | Continuation chain binary F1 |
| 99 | `10%` | Random word replacement rate |
| 99 | `8 pp` | Binary F1 degradation from 10% random word replacement |
| 108 | `1.4B` | Total parameter count for 4-detector ensembles (two models) |
| 115 | `6` | Number of features in 4-det + surface ensemble |
| 115 | `0.795` | 3-class F1 for 4-det + surface ensemble |
| 115 | `0.708` | Binary F1 for 4-det + surface ensemble |
| 115 | `22.8` | ms/text for 4-det + surface ensemble |
| 116 | `4` | Number of features in 4-detector ensemble |
| 116 | `0.785` | 3-class F1 for 4-detector ensemble |
| 116 | `0.700` | Binary F1 for 4-detector ensemble |
| 116 | `22.8` | ms/text for 4-detector ensemble |
| 117 | `7` | Number of features in proposed method |
| 117 | `0.774` | 3-class F1 for 7-feature ensemble |
| 117 | `0.705` | Binary F1 for 7-feature ensemble |
| 117 | `9.7` | ms/text for 7-feature ensemble |
| 119 | `1` | Number of features for Avg-LogProb |
| 119 | `0.707` | 3-class F1 for Avg-LogProb |
| 119 | `0.673` | Binary F1 for Avg-LogProb |
| 120 | `1` | Number of features for FastDetectGPT |
| 120 | `0.660` | 3-class F1 for FastDetectGPT |
| 120 | `0.569` | Binary F1 for FastDetectGPT |
| 121 | `1` | Number of features for LD-Score |
| 121 | `0.630` | 3-class F1 for LD-Score |
| 121 | `0.675` | Binary F1 for LD-Score |
| 122 | `1` | Number of features for Binoculars |
| 122 | `0.411` | 3-class F1 for Binoculars |
| 122 | `0.539` | Binary F1 for Binoculars |
| 130 | `0.705 vs 0.708` | Binary F1 comparison (7-feature vs 4-det+surface) |
| 130 | `~2.4x` | Cost reduction factor (reiterated) |
| 130 | `2.1 pp` | 3-class F1 gap (0.795 vs 0.774) |
| 130 | `3.0–16.6 pp` | F1 margin over individual detectors |
| 132 | `0.675` | LD-Score binary F1 (reiterated) |
| 132 | `0.673` | Avg-LogProb binary F1 (reiterated) |
| 132 | `0.660` | FastDetectGPT 3-class F1 (reiterated) |
| 132 | `0.569` | FastDetectGPT binary F1 (reiterated) |
| 132 | `0.539` | Binoculars binary F1 (reiterated) |
| 138 | `|d| > 0.46` | Effect size for drifting + intermediate features by gen-2+ |
| 138 | `|d| < 0.25` | Effect size for near-stationary features at all depths |

---

## **discussion.tex**

| Line | Value | Claims to measure |
|------|-------|-------------------|
| 5 | `≈10.8 nats` | log|V| upper bound for entropy_max |
| 5 | `|d| = 0.10–0.22` | Per-generator Cohen's d for tail_decay |
| 5 | `d = 0.46` | Cohen's d for entropy_std |
| 6 | `>48x` | Ratio of depth-explained variance in location vs shape features (ANOVA) |
| 13 | `τ > 0.7` | Temperature threshold above which signal degrades |
| 17 | `48.4%` | Error rate at gen-1→gen-2+ boundary |
| 17 | `≤29.2%` | Error rate at deeper generations |
| 19 | `F1 = 0.89–0.91` | QLoRA F1 on instruct data (within-model) |
| 20 | `F1 = 0.74–0.75` | Cross-domain evaluation F1 |
| 21 | `F1 ≈ 0.50` | 5-class classification F1 |
| 21 | `3` | Resolution limit (three depth classes) |

---

## **conclusion.tex**

| Line | Value | Claims to measure |
|------|-------|-------------------|
| 4 | `F1 = 0.694–0.762` | Range of cross-generator depth classification F1 (binary to 3-class) |
| 4 | `F1 = 0.830` | 5-generator cross-model binary F1 |
| 4 | `τ ≤ 0.7` | Temperature applicability bound |
| 5 | `F1 = 0.89–0.91` | QLoRA recovery F1 on instruct data (within-model) |

---

## **limitations.tex**

| Line | Value | Claims to measure |
|------|-------|-------------------|
| 4 | `≤8.2B` | Maximum generator parameter count |
| 4 | `3.7–19.9 pp` | 3-class F1 drop for instruction-tuned variants vs base |
| 4 | `F1 = 0.89–0.91` | QLoRA partial recovery F1 (within-model, instruct) |
| 5 | `t = 0.7` | Fixed decoding temperature |
| 5 | `p = 0.9` | Fixed nucleus sampling p |
| 6 | `3` | Number of depth classes (resolution limit) |
| 6 | `F1 ≈ 0.50` | 5-class classification F1 |
| 7 | `τ = 0.9` | Higher temperature tested |
| 7 | `-9.3 to -26.0 pp` | Binary F1 degradation at τ=0.9 |

---

**Summary counts**: ~190 distinct numerical value occurrences across the 7 files (many are repeated across sections for consistency). The unique claimed measurements include approximately 75 distinct numbers, with the remainder being restatements in different sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73a02ebe-d211-46b0-9fc7-cb7d977ae761",
  "isSidechain": true,
  "agentId": "a0b7e1d09f9ad6ef8",
  "requestId": "req_011CbPw1B5b1XXJpC6BpfMi2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f05c704-a5b7-467b-a6b7-5d7a23214e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "282ff675-1cbc-4eff-a27e-300a27df5081",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTaCwFcPBrCuuoGhy8sF5c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 400,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 45649,
      "output_tokens": 6514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1298
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 400,
          "output_tokens": 6514,
          "cache_read_input_tokens": 45649,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1298,
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
